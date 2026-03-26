#!/usr/bin/env python3
"""
build_pvo_html.py — Gera HTML de PVOs a partir dos JSONs extraídos

Uso:
    python build_pvo_html.py --module GL
    python build_pvo_html.py --module GL --pvo BalancePVO
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path


def load_variaveis(path: str) -> dict:
    defaults = {'EMPRESA': '', 'AUTOR_NOME': '', 'AUTOR_INICIAIS': '', 'AUTOR_CARGO': '', 'AUTOR_EMAIL': '', 'AREA': ''}
    if not os.path.exists(path):
        return defaults
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            m = re.match(r'\|\s*`\{\{(\w+)\}\}`\s*\|\s*(.+?)\s*\|', line)
            if m and m.group(1) in defaults:
                defaults[m.group(1)] = m.group(2)
    return defaults


def load_table_map(path: str) -> dict:
    if not os.path.exists(path):
        return {}
    table_map = {}
    current_module = None
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            s = line.strip()
            mod_match = re.match(r'===\s*(\w+)\s*', s)
            if mod_match:
                current_module = mod_match.group(1)
            elif current_module and re.match(r'^[A-Z][A-Z0-9_]+$', s):
                table_map[s] = current_module
    return table_map


def build_pvo_html(pvo_json_path: str, template_path: str, output_path: str, variaveis: dict, table_map: dict):
    """Gera HTML de um PVO."""
    with open(pvo_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    meta = data['meta']
    title = f'{meta["pvo_name"]} — PVO Data Dictionary'

    # Load i18n translations for description
    i18n_path = pvo_json_path.replace('.json', '.i18n.json')
    i18n_items = []
    if os.path.exists(i18n_path):
        with open(i18n_path, 'r', encoding='utf-8') as f:
            i18n_data = json.load(f)
        i18n_items = i18n_data.get('items', [])

    # Inject DATA
    data['table_map'] = table_map
    data['i18n'] = i18n_items
    data['meta']['company'] = variaveis.get('EMPRESA', '')
    data['meta']['author_name'] = variaveis.get('AUTOR_NOME', '')
    data['meta']['author_initials'] = variaveis.get('AUTOR_INICIAIS', '')
    data['meta']['author_role'] = variaveis.get('AUTOR_CARGO', '')
    data['meta']['author_email'] = variaveis.get('AUTOR_EMAIL', '')
    data['meta']['area'] = variaveis.get('AREA', '')

    template = template.replace('{{PAGE_TITLE}}', title)
    template = template.replace('{{LOGO_DARK_PATH}}', '../../../../assets/logos/logo-dark.png')
    template = template.replace('{{LOGO_LIGHT_PATH}}', '../../../../assets/logos/logo-light.png')
    template = template.replace('{{DATA_JSON}}', json.dumps(data, ensure_ascii=False))

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template)

    return output_path


def main():
    parser = argparse.ArgumentParser(description='Build PVO HTML pages')
    parser.add_argument('--module', required=True, help='Module code (GL, AP, AR, PO, HCM)')
    parser.add_argument('--pvo', help='Specific PVO name (e.g., BalancePVO)')
    args = parser.parse_args()

    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    mod = args.module.upper()

    template_path = str(script_dir / 'template_pvo.html')
    if not os.path.exists(template_path):
        print(f'ERROR: Template not found: {template_path}')
        sys.exit(1)

    variaveis = load_variaveis(str(project_root / 'docs' / 'assets' / 'variaveis.md'))
    table_map = load_table_map(str(project_root / 'src' / 'kb' / 'oracle-fusion-data-dictionary' / 'docs' / 'table-mappings.txt'))

    pvos_dir = project_root / 'src' / 'kb' / 'oracle-fusion-data-dictionary' / 'docs' / mod / 'pvos'
    output_dir = project_root / 'docs' / 'fusion-kb' / 'data-dictionary' / mod / 'pvos'

    if not pvos_dir.exists():
        print(f'No PVO JSONs found in {pvos_dir}')
        sys.exit(1)

    json_files = sorted(f for f in pvos_dir.glob('*.json') if not f.name.endswith('.i18n.json'))
    if args.pvo:
        json_files = [f for f in json_files if args.pvo.lower() in f.stem.lower()]

    print(f'Building {len(json_files)} PVO HTMLs for {mod}...')

    for jf in json_files:
        output_path = str(output_dir / (jf.stem + '.html'))
        try:
            result = build_pvo_html(str(jf), template_path, output_path, variaveis, table_map)
            print(f'  OK {jf.stem}.html')
        except Exception as e:
            print(f'  FAIL {jf.stem}: {e}')

    print(f'Done. {len(json_files)} HTMLs in {output_dir}')


if __name__ == '__main__':
    main()
