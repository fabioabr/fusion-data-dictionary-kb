#!/usr/bin/env python3
"""
build_reverse_index.py — Gera mapa reverso tabela → atributos de PVOs

Varre todos os PVO JSONs e produz table_to_pvos_map.json com a lista
de atributos de PVO que referenciam cada coluna de cada tabela.

Deduplica PVOs que existem em múltiplos módulos (mesmo pvo_name + mesmo attr),
priorizando o módulo original da tabela.

Uso:
    python build_reverse_index.py
    python build_reverse_index.py --src-dir <docs_dir> --output <path>
"""

import argparse
import json
import os
import sys
from collections import defaultdict
from pathlib import Path


def build_reverse_map(src_dir: str) -> dict:
    """Varre PVO JSONs e retorna {TABLE_NAME: [attr_row, ...]}."""
    # Primeiro, coletar tudo em um dict temporário para deduplicar
    # Chave de dedup: (table, column, pvo_name, pvo_attr)
    raw = defaultdict(dict)  # {TABLE: {dedup_key: row}}
    src = Path(src_dir)

    # Carregar table-mappings para saber o módulo nativo de cada tabela
    table_native_mod = {}
    mappings_path = src / 'table-mappings.txt'
    if mappings_path.exists():
        import re
        current_module = None
        with open(mappings_path, 'r', encoding='utf-8') as f:
            for line in f:
                s = line.strip()
                mod_match = re.match(r'===\s*(\w+)\s*', s)
                if mod_match:
                    current_module = mod_match.group(1)
                elif current_module and re.match(r'^[A-Z][A-Z0-9_]+$', s):
                    table_native_mod[s] = current_module

    # Descobre todos os módulos com pasta pvos/
    module_dirs = sorted(d for d in src.iterdir() if d.is_dir() and (d / 'pvos').is_dir())

    total_pvos = 0
    for mod_dir in module_dirs:
        pvos_dir = mod_dir / 'pvos'
        json_files = sorted(f for f in pvos_dir.glob('*.json') if not f.name.endswith('.i18n.json'))

        for jf in json_files:
            try:
                with open(jf, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except (json.JSONDecodeError, OSError) as e:
                print(f'  WARN skip {jf.name}: {e}')
                continue

            meta = data.get('meta', {})
            attributes = data.get('attributes', [])

            if not attributes:
                continue

            pvo_name = meta.get('pvo_name', jf.stem)
            module_code = meta.get('module_code', mod_dir.name)

            for attr in attributes:
                table_name = attr.get('table', '')
                column = attr.get('column', '')
                if not table_name or not column:
                    continue

                table_upper = table_name.upper()
                dedup_key = (column, pvo_name, attr.get('name', ''))

                row = {
                    'column': column,
                    'pvo_name': pvo_name,
                    'pvo_attr': attr.get('name', ''),
                    'module_code': module_code,
                    'bicc': attr.get('bicc', False),
                }

                existing = raw[table_upper].get(dedup_key)
                if existing is None:
                    raw[table_upper][dedup_key] = row
                else:
                    # Preferir o módulo nativo da tabela
                    native_mod = table_native_mod.get(table_upper, '')
                    if module_code == native_mod and existing['module_code'] != native_mod:
                        raw[table_upper][dedup_key] = row

            total_pvos += 1

    # Converter para listas e ordenar
    reverse = {}
    total_attrs = 0
    for table_name, rows_dict in raw.items():
        rows = list(rows_dict.values())
        rows.sort(key=lambda r: (r['pvo_name'].lower(), r['column'].lower()))
        reverse[table_name] = rows
        total_attrs += len(rows)

    print(f'Processed {total_pvos} PVOs across {len(module_dirs)} modules')
    print(f'Reverse map: {len(reverse)} tables, {total_attrs} attribute rows (deduplicated)')

    return reverse


def main():
    parser = argparse.ArgumentParser(description='Build reverse index: table -> PVO attributes')
    parser.add_argument('--src-dir', default='', help='Path to docs dir with module folders')
    parser.add_argument('--output', default='', help='Output JSON path')
    args = parser.parse_args()

    # Find project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    if not (project_root / 'CLAUDE.md').exists():
        project_root = Path.cwd()

    src_dir = args.src_dir or str(project_root / 'src' / 'kb' / 'oracle-fusion-data-dictionary' / 'docs')
    output_path = args.output or str(project_root / 'scripts' / 'config' / 'table_to_pvos_map.json')

    if not os.path.isdir(src_dir):
        print(f'ERROR: Source dir not found: {src_dir}')
        sys.exit(1)

    print(f'Source: {src_dir}')
    print(f'Output: {output_path}')

    reverse_map = build_reverse_map(src_dir)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(reverse_map, f, ensure_ascii=False, indent=2)

    print(f'Written {output_path} ({os.path.getsize(output_path) / 1024:.0f} KB)')


if __name__ == '__main__':
    main()
