#!/usr/bin/env python3
"""
batch_translate.py — Gera .i18n.md para todos os .md de uma pasta via Ollama API

Uso:
    python batch_translate.py <pasta_com_md>
    python batch_translate.py src/kb/oracle-fusion-data-dictionary/docs/AR/tables/

Chama Ollama REST API diretamente (localhost:11434) para traduzir texto.
"""

import argparse
import hashlib
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


# ============================================================
# OLLAMA API
# ============================================================

def ollama_translate(text: str, target_lang: str, retries: int = 2) -> str:
    """Traduz texto via Ollama REST API."""
    lang_map = {'en': 'English', 'es': 'Spanish'}
    target = lang_map.get(target_lang, target_lang)

    prompt = f"Translate the following text from Portuguese to {target}. Keep technical terms in English (write-off, subledger, posting, workflow, NSF, General Ledger, Accounts Receivable, business unit, multi-org, Descriptive Flexfield, etc.). Only output the translation, nothing else.\n\n{text}"

    payload = json.dumps({
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.1, "num_predict": 4096}
    }).encode('utf-8')

    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(OLLAMA_URL, data=payload, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=120) as resp:
                result = json.loads(resp.read().decode('utf-8'))
                return result.get('response', '').strip()
        except Exception as e:
            if attempt < retries:
                time.sleep(2)
                continue
            print(f"    WARN: Translation failed after {retries + 1} attempts: {e}")
            return text  # fallback: return original

    return text


# ============================================================
# MD PARSER (lightweight)
# ============================================================

def parse_front_matter(content: str) -> tuple[dict, str]:
    """Extrai front matter e body."""
    if not content.startswith('---'):
        return {}, content
    end = content.find('---', 3)
    if end == -1:
        return {}, content
    return {}, content[end + 3:].strip()


def extract_translatable_blocks(body: str) -> list[dict]:
    """Extrai blocos traduzíveis do body do .md (sem code blocks, sem front matter, sem wikilinks internos)."""
    blocks = []
    in_code = False
    current_section = ""

    for line in body.split('\n'):
        stripped = line.strip()

        # Toggle code blocks
        if stripped.startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            continue

        # Skip separators
        if stripped == '---' or not stripped:
            continue

        # Headings
        if stripped.startswith('## '):
            section_text = re.sub(r'^##\s*[^\w\s]*\s*', '', stripped).strip()
            current_section = section_text
            blocks.append({'type': 'heading', 'text': section_text, 'line': line})
            continue
        if stripped.startswith('### '):
            sub_text = re.sub(r'^###\s*', '', stripped).strip()
            blocks.append({'type': 'subheading', 'text': sub_text, 'line': line})
            continue

        # Callouts - extract text content
        if stripped.startswith('> [!'):
            # Callout header: > [!note] Title
            match = re.match(r'>\s*\[!\w+\]\s*(.*)', stripped)
            if match and match.group(1):
                blocks.append({'type': 'callout_title', 'text': match.group(1), 'line': line})
            continue
        if stripped.startswith('> '):
            callout_text = stripped[2:].strip()
            if callout_text:
                # Remove markdown formatting for translation
                clean = re.sub(r'`[^`]+`', '', callout_text).strip()
                if clean:
                    blocks.append({'type': 'callout_body', 'text': callout_text, 'line': line})
            continue

        # List items
        if stripped.startswith('- '):
            item_text = stripped[2:].strip()
            # Skip pure code references
            if item_text.startswith('`') and item_text.endswith('`'):
                continue
            # Extract description part (after code)
            blocks.append({'type': 'list_item', 'text': item_text, 'line': line})
            continue

        # Table rows - extract only description cells
        if stripped.startswith('|') and not stripped.startswith('|---') and not stripped.startswith('| #') and not stripped.startswith('| Coluna') and not stripped.startswith('| Column'):
            cells = [c.strip() for c in stripped.split('|')[1:-1]]
            if len(cells) >= 6:
                # cells[4] = Category, cells[5] = Description
                cat = cells[4].strip()
                desc = cells[5].strip()
                if desc and not desc.startswith('`'):
                    blocks.append({'type': 'table_cat', 'text': cat, 'cell_index': 4, 'line': line})
                    blocks.append({'type': 'table_desc', 'text': desc, 'cell_index': 5, 'line': line})
            continue

        # Regular paragraphs
        if stripped and not stripped.startswith('|'):
            blocks.append({'type': 'paragraph', 'text': stripped, 'line': line})

    return blocks


def group_blocks_for_translation(blocks: list[dict]) -> list[str]:
    """Agrupa blocos em textos para enviar ao Ollama (eficiência)."""
    texts = []
    for b in blocks:
        clean = b['text']
        # Remove markdown bold/code for translation
        clean = re.sub(r'\*\*([^*]+)\*\*', r'\1', clean)
        clean = re.sub(r'`([^`]+)`', r'\1', clean)
        # Remove wikilinks
        clean = re.sub(r'\[\[([^\]]+)\]\]', r'\1', clean)
        if clean.strip():
            texts.append(clean.strip())
    return texts


# ============================================================
# i18n.md BUILDER
# ============================================================

def build_i18n_content(body_pt: str, translations_en: dict, translations_es: dict) -> str:
    """Reconstrói o conteúdo traduzido mantendo a estrutura Markdown."""
    # Simple approach: translate the full body line by line using the translation map
    en_body = apply_translations(body_pt, translations_en)
    es_body = apply_translations(body_pt, translations_es)
    return en_body, es_body


def apply_translations(body: str, translations: dict) -> str:
    """Aplica traduções ao body, substituindo textos PT por traduções."""
    result_lines = []
    in_code = False

    for line in body.split('\n'):
        stripped = line.strip()

        # Code blocks: copy as-is
        if stripped.startswith('```'):
            in_code = not in_code
            result_lines.append(line)
            continue
        if in_code:
            result_lines.append(line)
            continue

        # Try to find and replace translatable text
        translated_line = line
        for pt_text, translated_text in translations.items():
            if pt_text in translated_line:
                translated_line = translated_line.replace(pt_text, translated_text)

        result_lines.append(translated_line)

    return '\n'.join(result_lines)


def translate_texts_batch(texts: list[str], target_lang: str) -> dict:
    """Traduz uma lista de textos e retorna mapa {original: traduzido}."""
    translations = {}

    # Batch: send all texts as numbered list
    if not texts:
        return translations

    # Split into chunks of 30 to avoid too-long prompts
    chunk_size = 30
    for i in range(0, len(texts), chunk_size):
        chunk = texts[i:i + chunk_size]
        numbered = '\n'.join(f'{j + 1}. {t}' for j, t in enumerate(chunk))

        result = ollama_translate(numbered, target_lang)

        # Parse numbered response
        for j, original in enumerate(chunk):
            # Try to find the numbered line in response
            pattern = rf'^{j + 1}\.\s*(.+)$'
            match = re.search(pattern, result, re.MULTILINE)
            if match:
                translations[original] = match.group(1).strip()
            else:
                # Fallback: try line by line
                result_lines = [l.strip() for l in result.split('\n') if l.strip()]
                # Remove numbering from lines
                clean_lines = []
                for rl in result_lines:
                    cl = re.sub(r'^\d+\.\s*', '', rl)
                    clean_lines.append(cl)
                if j < len(clean_lines):
                    translations[original] = clean_lines[j]

    return translations


def generate_i18n(md_path: str) -> str:
    """Gera o .i18n.md para um arquivo .md."""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Hash
    md5 = hashlib.md5(content.encode('utf-8')).hexdigest()

    # Check cache
    i18n_path = md_path.replace('.md', '.i18n.md')
    if os.path.exists(i18n_path):
        with open(i18n_path, 'r', encoding='utf-8') as f:
            existing = f.read()
        if f'source_hash: "{md5}"' in existing:
            return 'CACHED'

    # Parse
    _, body = parse_front_matter(content)
    blocks = extract_translatable_blocks(body)
    texts = group_blocks_for_translation(blocks)

    if not texts:
        return 'SKIP (no translatable text)'

    # Translate
    print(f"    Translating {len(texts)} text blocks to EN...")
    translations_en = translate_texts_batch(texts, 'en')
    print(f"    Translating {len(texts)} text blocks to ES...")
    translations_es = translate_texts_batch(texts, 'es')

    # Build translated bodies
    en_body, es_body = build_i18n_content(body, translations_en, translations_es)

    # Assemble .i18n.md
    filename = Path(md_path).name
    today = date.today().isoformat()

    i18n_content = f"""---
# === METADADOS DE TRADUCAO ===
source: "{filename}"
source_hash: "{md5}"
languages: [en, es]
translated_at: "{today}"
translator: "ollama-local"
---

<!-- ============================================================ -->
<!-- LANG: en                                                      -->
<!-- ============================================================ -->

{en_body}

<!-- ============================================================ -->
<!-- LANG: es                                                      -->
<!-- ============================================================ -->

{es_body}
"""

    with open(i18n_path, 'w', encoding='utf-8') as f:
        f.write(i18n_content)

    return i18n_path


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(description='Batch translate .md files to .i18n.md via Ollama')
    parser.add_argument('path', help='Folder with .md files or single .md file')
    parser.add_argument('--force', action='store_true', help='Re-translate even if cached')
    args = parser.parse_args()

    # Collect files
    p = Path(args.path)
    if p.is_dir():
        md_files = sorted(p.glob('*.md'))
        md_files = [f for f in md_files if not f.name.endswith('.i18n.md')]
    else:
        md_files = [p]

    print(f'Files to translate: {len(md_files)}')
    print(f'Ollama model: {OLLAMA_MODEL}')
    print()

    ok = 0
    cached = 0
    failed = 0
    start = time.time()

    for i, md_file in enumerate(md_files):
        print(f'[{i + 1}/{len(md_files)}] {md_file.name}')
        try:
            result = generate_i18n(str(md_file))
            if result == 'CACHED':
                print(f'    CACHED (hash unchanged)')
                cached += 1
            elif result.startswith('SKIP'):
                print(f'    {result}')
                cached += 1
            else:
                print(f'    OK -> {Path(result).name}')
                ok += 1
        except Exception as e:
            print(f'    FAIL: {e}')
            failed += 1

    elapsed = time.time() - start
    print(f'\nDone in {elapsed:.1f}s')
    print(f'  Translated: {ok}')
    print(f'  Cached/Skip: {cached}')
    print(f'  Failed: {failed}')


if __name__ == '__main__':
    main()
