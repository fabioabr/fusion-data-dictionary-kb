#!/usr/bin/env python3
"""
translate_json.py — Preenche EN/ES nos .i18n.json via Ollama REST API

Uso:
    python translate_json.py <arquivo.i18n.json>
    python translate_json.py --batch <pasta>

Lê items com en:null/es:null e preenche via Ollama (translategemma:4b).
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.request
from datetime import date
from pathlib import Path

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "translategemma:4b"


def ollama_translate(text: str, target_lang: str) -> str:
    """Traduz texto via Ollama REST API."""
    lang_map = {'en': 'English', 'es': 'Spanish'}
    target = lang_map.get(target_lang, target_lang)

    prompt = (
        f"Translate from Portuguese to {target}. "
        f"Keep technical terms in English (write-off, subledger, posting, workflow, NSF, "
        f"General Ledger, Accounts Receivable, business unit, multi-org, Descriptive Flexfield, etc.). "
        f"Output ONLY the translation, nothing else.\n\n{text}"
    )

    payload = json.dumps({
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.1, "num_predict": 2048}
    }).encode('utf-8')

    try:
        req = urllib.request.Request(OLLAMA_URL, data=payload, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode('utf-8'))
            translated = result.get('response', '').strip()
            # Remove potential quotes wrapping the translation
            if translated.startswith('"') and translated.endswith('"'):
                translated = translated[1:-1]
            # Remove "Translation:" prefix if model adds it
            translated = re.sub(r'^(Translation|Traduccion|Traduc[a-z]+):\s*', '', translated, flags=re.IGNORECASE)
            return translated.strip()
    except Exception as e:
        print(f"    WARN: Translation failed: {e}")
        return None


def translate_batch_items(items: list[dict], target_lang: str, chunk_size: int = 25) -> int:
    """Traduz items em batch. Retorna quantidade traduzida."""
    # Filtra items que precisam de tradução
    pending = [item for item in items if item.get(target_lang) is None]
    if not pending:
        return 0

    translated_count = 0

    # Processar em chunks
    for i in range(0, len(pending), chunk_size):
        chunk = pending[i:i + chunk_size]

        # Montar lista numerada
        numbered_text = '\n'.join(f"{j+1}. {item['br']}" for j, item in enumerate(chunk))

        result = ollama_translate(numbered_text, target_lang)
        if not result:
            continue

        # Parsear resposta numerada
        result_lines = result.strip().split('\n')
        # Limpar numeração das linhas
        clean_lines = []
        for line in result_lines:
            line = line.strip()
            if not line:
                continue
            # Remove "1. ", "2. ", etc.
            cleaned = re.sub(r'^\d+\.\s*', '', line).strip()
            if cleaned:
                clean_lines.append(cleaned)

        # Mapear de volta
        for j, item in enumerate(chunk):
            if j < len(clean_lines):
                item[target_lang] = clean_lines[j]
                translated_count += 1
            else:
                # Fallback: traduzir individualmente
                single = ollama_translate(item['br'], target_lang)
                if single:
                    item[target_lang] = single
                    translated_count += 1

    return translated_count


def translate_file(json_path: str, force: bool = False) -> str:
    """Traduz um .i18n.json. Retorna status."""
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    items = data.get('items', [])
    if not items:
        return 'SKIP (no items)'

    # Check if already translated
    pending_en = sum(1 for item in items if item.get('en') is None)
    pending_es = sum(1 for item in items if item.get('es') is None)

    if pending_en == 0 and pending_es == 0 and not force:
        return 'CACHED (already translated)'

    total = len(items)
    translated_en = 0
    translated_es = 0

    # Translate EN
    if pending_en > 0 or force:
        if force:
            for item in items:
                item['en'] = None
        print(f"    EN: {pending_en}/{total} pending...")
        translated_en = translate_batch_items(items, 'en')
        print(f"    EN: {translated_en} translated")

    # Translate ES
    if pending_es > 0 or force:
        if force:
            for item in items:
                item['es'] = None
        print(f"    ES: {pending_es}/{total} pending...")
        translated_es = translate_batch_items(items, 'es')
        print(f"    ES: {translated_es} translated")

    # Update metadata
    data['translated_at'] = date.today().isoformat()

    # Save
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return f'OK (EN:{translated_en}, ES:{translated_es})'


def main():
    parser = argparse.ArgumentParser(description='Translate .i18n.json files via Ollama')
    parser.add_argument('input', nargs='?', help='Path to .i18n.json file')
    parser.add_argument('--batch', help='Path to folder with .i18n.json files')
    parser.add_argument('--force', action='store_true', help='Re-translate even if already done')
    args = parser.parse_args()

    json_files = []
    if args.batch:
        json_files = sorted(Path(args.batch).glob('*.i18n.json'))
    elif args.input:
        json_files = [Path(args.input)]
    else:
        parser.print_help()
        sys.exit(1)

    print(f'Translating {len(json_files)} file(s)...')
    print(f'Model: {OLLAMA_MODEL}')
    print()

    start = time.time()
    ok = 0
    cached = 0
    failed = 0

    for i, f in enumerate(json_files):
        print(f'[{i+1}/{len(json_files)}] {f.name}')
        try:
            result = translate_file(str(f), args.force)
            if 'CACHED' in result:
                print(f'    {result}')
                cached += 1
            elif result.startswith('OK'):
                print(f'    {result}')
                ok += 1
            else:
                print(f'    {result}')
                cached += 1
        except Exception as e:
            print(f'    FAIL: {e}')
            failed += 1

    elapsed = time.time() - start
    print(f'\nDone in {elapsed:.1f}s')
    print(f'  Translated: {ok}')
    print(f'  Cached: {cached}')
    print(f'  Failed: {failed}')


if __name__ == '__main__':
    main()
