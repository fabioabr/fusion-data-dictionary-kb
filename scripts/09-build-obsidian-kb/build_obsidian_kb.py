#!/usr/bin/env python3
"""
build_obsidian_kb.py — Monta a pasta KB (cofre Obsidian) com .md de tabelas e PVOs

Copia os .md de tabelas e PVOs para docs/fusion-kb/kb/{MODULE}/{tables,pvos}/,
gerando também um index.md por módulo e um index.md raiz para o vault.

Uso:
    python build_obsidian_kb.py
    python build_obsidian_kb.py --dry-run
"""

import argparse
import glob
import json
import os
import shutil
import sys
from pathlib import Path


MODULE_NAMES = {
    'AP': 'Accounts Payable',
    'AR': 'Accounts Receivable',
    'GL': 'General Ledger',
    'PO': 'Purchasing',
    'HCM': 'Human Capital Management',
    'OTHER': 'Cross-Module',
}


def build_module_index(module_code: str, tables: list, pvos: list) -> str:
    """Gera index.md para um módulo."""
    module_name = MODULE_NAMES.get(module_code, module_code)
    lines = []
    lines.append('---')
    lines.append(f'id: IDX-{module_code}')
    lines.append('doc_type: system-doc')
    lines.append(f'title: "{module_code} — {module_name}"')
    lines.append('system: Oracle Fusion Cloud ERP')
    lines.append(f'module: {module_name}')
    lines.append('domain: Técnico')
    lines.append('status: approved')
    lines.append('confidentiality: internal')
    lines.append('tags:')
    lines.append('  - oracle-fusion')
    lines.append(f'  - {module_code.lower()}')
    lines.append('  - data-dictionary')
    lines.append('  - index')
    lines.append('---')
    lines.append('')
    lines.append(f'# {module_code} — {module_name}')
    lines.append('')

    # Stats
    lines.append(f'| Tabelas | PVOs |')
    lines.append(f'|---------|------|')
    lines.append(f'| {len(tables)} | {len(pvos)} |')
    lines.append('')

    # Tabelas
    if tables:
        lines.append('## 📊 Tabelas')
        lines.append('')
        for t in sorted(tables):
            name = Path(t).stem
            lines.append(f'- [[{name}]]')
        lines.append('')

    # PVOs
    if pvos:
        lines.append('## 🔗 PVOs')
        lines.append('')
        for p in sorted(pvos):
            name = Path(p).stem
            lines.append(f'- [[{name}]]')
        lines.append('')

    return '\n'.join(lines)


def build_root_index(modules: dict) -> str:
    """Gera index.md raiz do vault."""
    lines = []
    lines.append('---')
    lines.append('id: IDX-ROOT')
    lines.append('doc_type: system-doc')
    lines.append('title: "Oracle Fusion Data Dictionary"')
    lines.append('system: Oracle Fusion Cloud ERP')
    lines.append('module: Data Dictionary')
    lines.append('domain: Técnico')
    lines.append('status: approved')
    lines.append('confidentiality: internal')
    lines.append('tags:')
    lines.append('  - oracle-fusion')
    lines.append('  - data-dictionary')
    lines.append('  - index')
    lines.append('---')
    lines.append('')
    lines.append('# Oracle Fusion Data Dictionary')
    lines.append('')
    lines.append('Base de conhecimento do dicionário de dados Oracle Fusion Cloud ERP.')
    lines.append('')

    total_tables = 0
    total_pvos = 0

    lines.append('## 📦 Módulos')
    lines.append('')
    lines.append('| Módulo | Nome | Tabelas | PVOs |')
    lines.append('|--------|------|---------|------|')

    for mod_code in sorted(modules.keys()):
        mod = modules[mod_code]
        mod_name = MODULE_NAMES.get(mod_code, mod_code)
        t_count = mod['tables']
        p_count = mod['pvos']
        total_tables += t_count
        total_pvos += p_count
        lines.append(f'| [[{mod_code}]] | {mod_name} | {t_count} | {p_count} |')

    lines.append('')
    lines.append(f'**Total:** {total_tables} tabelas · {total_pvos} PVOs')
    lines.append('')

    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='Build Obsidian KB vault from .md files')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done')
    args = parser.parse_args()

    # Find project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    if not (project_root / 'CLAUDE.md').exists():
        project_root = Path.cwd()

    src_dir = project_root / 'src' / 'kb' / 'oracle-fusion-data-dictionary' / 'docs'
    kb_dir = project_root / 'docs' / 'fusion-kb' / 'kb'

    # Discover modules
    module_dirs = sorted(d for d in src_dir.iterdir()
                         if d.is_dir() and d.name not in ('Fusion KB', 'teste'))

    print(f'Source: {src_dir}')
    print(f'Output: {kb_dir}')
    print(f'Modules: {[d.name for d in module_dirs]}')
    print()

    total_copied = 0
    modules_summary = {}

    for mod_dir in module_dirs:
        module_code = mod_dir.name

        # Collect .md files (exclude .i18n.md)
        table_mds = sorted(f for f in (mod_dir / 'tables').glob('*.md')
                           if not f.name.endswith('.i18n.md')) if (mod_dir / 'tables').is_dir() else []
        pvo_mds = sorted(f for f in (mod_dir / 'pvos').glob('*.md')
                         if not f.name.endswith('.i18n.md')) if (mod_dir / 'pvos').is_dir() else []

        if not table_mds and not pvo_mds:
            continue

        modules_summary[module_code] = {'tables': len(table_mds), 'pvos': len(pvo_mds)}

        # Output dirs
        tables_out = kb_dir / module_code / 'tables'
        pvos_out = kb_dir / module_code / 'pvos'

        if not args.dry_run:
            tables_out.mkdir(parents=True, exist_ok=True)
            pvos_out.mkdir(parents=True, exist_ok=True)

        # Copy tables
        for f in table_mds:
            dst = tables_out / f.name
            if not args.dry_run:
                shutil.copy2(f, dst)
            total_copied += 1

        # Copy PVOs
        for f in pvo_mds:
            dst = pvos_out / f.name
            if not args.dry_run:
                shutil.copy2(f, dst)
            total_copied += 1

        # Module index
        mod_index = build_module_index(module_code, table_mds, pvo_mds)
        mod_index_path = kb_dir / module_code / f'{module_code}.md'
        if not args.dry_run:
            with open(mod_index_path, 'w', encoding='utf-8') as fh:
                fh.write(mod_index)

        print(f'  {module_code}: {len(table_mds)} tables, {len(pvo_mds)} PVOs')

    # Root index
    root_index = build_root_index(modules_summary)
    root_index_path = kb_dir / 'index.md'
    if not args.dry_run:
        kb_dir.mkdir(parents=True, exist_ok=True)
        with open(root_index_path, 'w', encoding='utf-8') as fh:
            fh.write(root_index)

    # Obsidian vault config
    obsidian_dir = kb_dir / '.obsidian'
    if not args.dry_run:
        obsidian_dir.mkdir(parents=True, exist_ok=True)

        # app.json — shortest path for wikilinks
        app_config = {
            "newLinkFormat": "shortest",
            "useMarkdownLinks": False,
            "showFrontmatter": True,
            "strictLineBreaks": False,
            "readableLineLength": True
        }
        with open(obsidian_dir / 'app.json', 'w', encoding='utf-8') as fh:
            json.dump(app_config, fh, indent=2)

        # workspace.json mínimo
        workspace = {
            "main": {
                "id": "main",
                "type": "split",
                "children": []
            }
        }
        with open(obsidian_dir / 'workspace.json', 'w', encoding='utf-8') as fh:
            json.dump(workspace, fh, indent=2)

    prefix = 'WOULD COPY' if args.dry_run else 'Copied'
    print(f'\n{prefix} {total_copied} files to {kb_dir}')
    print(f'Modules: {len(modules_summary)}')
    print(f'Obsidian vault config: {obsidian_dir}')

    if not args.dry_run:
        print(f'\nPronto! Abra "{kb_dir}" como vault no Obsidian.')


if __name__ == '__main__':
    main()
