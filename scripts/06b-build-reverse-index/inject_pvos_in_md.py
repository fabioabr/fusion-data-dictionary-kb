#!/usr/bin/env python3
"""
inject_pvos_in_md.py — Injeta seção "PVOs Relacionados" nos .md de tabelas

Lê o table_to_pvos_map.json e adiciona (ou atualiza) a seção de PVOs
em cada .md de tabela, antes da seção de Referências.

Uso:
    python inject_pvos_in_md.py
    python inject_pvos_in_md.py --dry-run
"""

import argparse
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path


def build_pvo_section(rows: list) -> str:
    """Gera o markdown da seção PVOs Relacionados."""
    # Agrupar por pvo_name
    pvos = OrderedDict()
    for r in rows:
        key = r['pvo_name']
        if key not in pvos:
            pvos[key] = {
                'module': r['module_code'],
                'columns': [],
                'bicc_count': 0,
                'total': 0,
            }
        pvos[key]['columns'].append((r['column'], r['pvo_attr'], r.get('bicc', False)))
        pvos[key]['total'] += 1
        if r.get('bicc'):
            pvos[key]['bicc_count'] += 1

    lines = []
    lines.append('## 🔗 PVOs Relacionados')
    lines.append('')

    for pvo_name, info in pvos.items():
        bicc_label = f' · BICC: {info["bicc_count"]}/{info["total"]}' if info['bicc_count'] else ''
        lines.append(f'### [[{pvo_name.lower()}|{pvo_name}]] ({info["module"]}{bicc_label})')
        lines.append('')
        lines.append('| Coluna da Tabela | Atributo do PVO | BICC |')
        lines.append('|------------------|-----------------|------|')
        for col, attr, bicc in sorted(info['columns'], key=lambda x: x[0].lower()):
            bicc_str = '✅' if bicc else '—'
            lines.append(f'| {col} | {attr} | {bicc_str} |')
        lines.append('')

    return '\n'.join(lines)


def inject_section(content: str, pvo_section: str) -> str:
    """Injeta ou atualiza a seção PVOs Relacionados no conteúdo do .md."""
    # Remover seção existente se houver
    content = re.sub(
        r'## 🔗 PVOs Relacionados\n.*?(?=## [^\n]|\Z)',
        '',
        content,
        flags=re.DOTALL,
    )

    # Limpar linhas em branco extras que sobraram
    content = re.sub(r'\n{3,}', '\n\n', content)

    # Inserir antes de "## 📚 Referências" se existir
    ref_match = re.search(r'^## 📚 Referências', content, re.MULTILINE)
    if ref_match:
        pos = ref_match.start()
        # Garantir separação
        before = content[:pos].rstrip('\n')
        after = content[pos:]
        content = before + '\n\n' + pvo_section + '\n---\n\n' + after
    else:
        # Inserir no final
        content = content.rstrip('\n') + '\n\n---\n\n' + pvo_section

    return content


def main():
    parser = argparse.ArgumentParser(description='Inject PVO section into table .md files')
    parser.add_argument('--dry-run', action='store_true', help='Show changes without writing')
    parser.add_argument('--table', default='', help='Process single table (e.g., GL_BALANCES)')
    args = parser.parse_args()

    # Find project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    if not (project_root / 'CLAUDE.md').exists():
        project_root = Path.cwd()

    # Load PVO map
    pvo_map_path = project_root / 'scripts' / 'config' / 'table_to_pvos_map.json'
    with open(pvo_map_path, 'r', encoding='utf-8') as f:
        pvo_map = json.load(f)
    print(f'PVO map: {len(pvo_map)} tabelas')

    # Find .md files
    docs_dir = project_root / 'src' / 'kb' / 'oracle-fusion-data-dictionary' / 'docs'
    md_files = sorted(docs_dir.glob('*/tables/*.md'))
    md_files = [f for f in md_files if not f.name.endswith('.i18n.md')]

    if args.table:
        md_files = [f for f in md_files if f.stem.upper() == args.table.upper()]

    print(f'Processing {len(md_files)} .md files...')

    updated = 0
    skipped = 0

    for md_file in md_files:
        table_name = md_file.stem.upper()
        rows = pvo_map.get(table_name)

        if not rows:
            skipped += 1
            continue

        pvo_section = build_pvo_section(rows)

        with open(md_file, 'r', encoding='utf-8') as f:
            original = f.read()

        new_content = inject_section(original, pvo_section)

        if new_content == original:
            skipped += 1
            continue

        if args.dry_run:
            print(f'  WOULD UPDATE {md_file.name} (+{len(rows)} PVO attrs)')
        else:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'  OK {md_file.name} (+{len(rows)} PVO attrs)')

        updated += 1

    print(f'\nDone. Updated: {updated}, Skipped: {skipped}')


if __name__ == '__main__':
    main()
