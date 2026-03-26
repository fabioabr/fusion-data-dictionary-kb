#!/usr/bin/env python3
"""
extract_pvo_i18n.py — Extrai frases traduzíveis de .json (PVO) e gera .i18n.json (só BR)

Uso:
    python extract_pvo_i18n.py <arquivo.json>
    python extract_pvo_i18n.py --batch <pasta>

Gera {arquivo}.i18n.json na mesma pasta do .json, com items {id, br, en:null, es:null}
"""

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path


def md5_hash(content: str) -> str:
    return hashlib.md5(content.encode('utf-8')).hexdigest()


def extract_phrases(data: dict) -> list[str]:
    """Extrai frases traduzíveis de um JSON de PVO."""
    phrases = []
    seen = set()

    def add(text: str):
        """Adiciona frase se não for vazia, duplicada ou puramente técnica."""
        if not text or not isinstance(text, str):
            return
        text = text.strip()
        if not text or text in seen:
            return
        # Skip valores puramente técnicos
        if len(text) <= 1:
            return
        seen.add(text)
        phrases.append(text)

    # Extrair meta.description
    meta = data.get('meta', {})
    if meta.get('description'):
        add(meta['description'])

    # Extrair descrições de atributos
    attributes = data.get('attributes', [])
    for attr in attributes:
        if isinstance(attr, dict):
            desc = attr.get('description')
            if desc:
                add(desc)

    return phrases


def generate_i18n_json(json_path: str, force: bool = False) -> str:
    """Gera .i18n.json para um .json de PVO. Retorna path ou status."""
    with open(json_path, 'r', encoding='utf-8') as f:
        content = f.read()

    file_hash = md5_hash(content)

    # Gerar nome do i18n: arquivo.json → arquivo.i18n.json
    base = json_path
    if base.endswith('.json'):
        base = base[:-5]
    i18n_path = base + '.i18n.json'

    # Check cache
    if os.path.exists(i18n_path) and not force:
        with open(i18n_path, 'r', encoding='utf-8') as f:
            existing = json.load(f)
        if existing.get('source_hash') == file_hash:
            return 'CACHED'

    # Parse JSON
    try:
        data = json.loads(content)
    except json.JSONDecodeError as e:
        return f'SKIP (JSON inválido: {e})'

    # Extract
    phrases = extract_phrases(data)
    if not phrases:
        return 'SKIP (sem texto traduzível)'

    # Build i18n JSON
    i18n_data = {
        "source": Path(json_path).name,
        "source_hash": file_hash,
        "translated_at": None,
        "items": [
            {"id": i + 1, "br": phrase, "en": None, "es": None}
            for i, phrase in enumerate(phrases)
        ]
    }

    with open(i18n_path, 'w', encoding='utf-8') as f:
        json.dump(i18n_data, f, ensure_ascii=False, indent=2)

    return i18n_path


def main():
    parser = argparse.ArgumentParser(
        description='Extrai frases traduzíveis de .json (PVO) para .i18n.json'
    )
    parser.add_argument('input', nargs='?', help='Caminho para arquivo .json')
    parser.add_argument('--batch', help='Caminho para pasta com arquivos .json')
    parser.add_argument('--force', action='store_true',
                        help='Regenerar mesmo se cache válido')
    args = parser.parse_args()

    json_files = []
    if args.batch:
        batch_path = Path(args.batch)
        if not batch_path.is_dir():
            print(f'Erro: pasta não encontrada: {args.batch}')
            sys.exit(1)
        json_files = sorted(batch_path.glob('*.json'))
        # Excluir arquivos .i18n.json da lista de entrada
        json_files = [f for f in json_files if not f.name.endswith('.i18n.json')]
    elif args.input:
        input_path = Path(args.input)
        if not input_path.is_file():
            print(f'Erro: arquivo não encontrado: {args.input}')
            sys.exit(1)
        if input_path.name.endswith('.i18n.json'):
            print('Erro: arquivo de entrada não pode ser .i18n.json')
            sys.exit(1)
        json_files = [input_path]
    else:
        parser.print_help()
        sys.exit(1)

    if not json_files:
        print('Nenhum arquivo .json encontrado.')
        sys.exit(0)

    print(f'Extraindo de {len(json_files)} arquivo(s)...')

    ok = 0
    cached = 0
    skipped = 0
    errors = 0

    for i, f in enumerate(json_files):
        result = generate_i18n_json(str(f), args.force)
        if result == 'CACHED':
            cached += 1
        elif result.startswith('SKIP'):
            skipped += 1
            print(f'  [{i+1}/{len(json_files)}] {f.name} -> {result}')
        elif result.startswith('ERRO'):
            errors += 1
            print(f'  [{i+1}/{len(json_files)}] {f.name} -> {result}')
        else:
            ok += 1
            # Contar itens gerados
            with open(result, 'r', encoding='utf-8') as fh:
                i18n_data = json.load(fh)
            item_count = len(i18n_data.get('items', []))
            print(f'  [{i+1}/{len(json_files)}] {f.name} -> {Path(result).name} ({item_count} items)')

    print(f'\nResumo: Extraídos={ok}, Cache={cached}, Pulados={skipped}, Erros={errors}')


if __name__ == '__main__':
    main()
