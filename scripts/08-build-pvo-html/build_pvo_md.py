#!/usr/bin/env python3
"""
build_pvo_md.py — Gera .md formal para PVOs a partir dos JSONs extraídos

Lê cada PVO JSON e gera um .md com front matter rico, seções de visão geral,
atributos agrupados por tabela, e tabelas relacionadas com wikilinks.

Uso:
    python build_pvo_md.py
    python build_pvo_md.py --module GL
    python build_pvo_md.py --module GL --pvo BalancePVO
    python build_pvo_md.py --dry-run
"""

import argparse
import json
import sys
from pathlib import Path

# Mapeamento de module_code para nome do módulo
MODULE_NAMES = {
    'AP': 'Accounts Payable',
    'AR': 'Accounts Receivable',
    'GL': 'General Ledger',
    'PO': 'Purchasing',
    'HCM': 'Human Capital Management',
    'OTHER': 'Cross-Module',
}


def load_variaveis(path: str) -> dict:
    """Carrega variáveis do variaveis.md."""
    result = {}
    p = Path(path)
    if not p.exists():
        return result
    with open(p, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if ':' in line and not line.startswith('#'):
                key, _, val = line.partition(':')
                result[key.strip()] = val.strip().strip('"').strip("'")
    return result


def build_md(pvo_json_path: str, variaveis: dict, table_map: dict) -> str:
    """Gera o conteúdo .md para um PVO."""
    with open(pvo_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    meta = data['meta']
    stats = data['stats']
    tables = data.get('tables', [])
    attributes = data.get('attributes', [])
    by_table = data.get('by_table', {})

    pvo_name = meta['pvo_name']
    module_code = meta.get('module_code', 'OTHER')
    module_name = MODULE_NAMES.get(module_code, module_code)
    description = meta.get('description', '')
    full_path = meta.get('full_path', '')

    # Carregar i18n se existir
    i18n_path = Path(pvo_json_path).with_suffix('.i18n.json')
    i18n_desc = {}
    if i18n_path.exists():
        try:
            with open(i18n_path, 'r', encoding='utf-8') as f:
                i18n_data = json.load(f)
            items = i18n_data.get('items', [])
            if items:
                i18n_desc = items[0]  # Primeiro item é a descrição
        except (json.JSONDecodeError, OSError):
            pass

    # Tags
    tags = ['oracle-fusion', module_code.lower(), 'data-dictionary', 'pvo']
    if stats.get('bicc_enabled', 0) > 0:
        tags.append('bicc')

    # ID: DOC-{MODULE}-PVO-{seq}
    pvo_id = f'DOC-{module_code}-PVO-{pvo_name}'

    # Front matter
    lines = []
    lines.append('---')
    lines.append(f'id: {pvo_id}')
    lines.append('doc_type: system-doc')
    lines.append(f'title: "{pvo_name} — PVO {module_name}"')
    lines.append('system: Oracle Fusion Cloud ERP')
    lines.append(f'module: {module_name}')
    lines.append('domain: Técnico')
    lines.append(f'owner: {variaveis.get("AUTOR_LOGIN", "fabio.patria")}')
    lines.append(f'team: {variaveis.get("EQUIPE", "dados")}')
    lines.append('status: draft')
    lines.append('confidentiality: internal')
    lines.append('tags:')
    for tag in tags:
        lines.append(f'  - {tag}')
    lines.append('aliases:')
    lines.append(f'  - {pvo_name}')
    lines.append(f'  - {pvo_name.lower()}')
    lines.append('source_format: markdown')
    lines.append('conversion_pipeline: json-to-md-v1')
    lines.append('conversion_quality: 100')
    lines.append('qa_score: 0')
    lines.append('qa_status: not_reviewed')
    lines.append('created_at: 2026-03-31')
    lines.append('updated_at: 2026-03-31')
    lines.append('---')
    lines.append('')

    # Título
    lines.append(f'# {pvo_name}')
    lines.append('')

    # Visão Geral
    lines.append('## 📌 Visão Geral')
    lines.append('')
    lines.append(description)
    lines.append('')
    if full_path:
        lines.append(f'**Caminho:** `{full_path}`')
        lines.append('')

    # Stats
    bicc_pct = stats.get('bicc_pct', 0)
    lines.append(f'| Atributos | Tabelas | PKs | BICC | BICC % |')
    lines.append(f'|-----------|---------|-----|------|--------|')
    lines.append(f'| {stats["total_attributes"]} | {stats["tables_count"]} | {stats["pk_count"]} | {stats["bicc_enabled"]} | {bicc_pct}% |')
    lines.append('')

    lines.append('---')
    lines.append('')

    # Tabelas Relacionadas
    lines.append('## 🔗 Tabelas Relacionadas')
    lines.append('')
    for tbl in tables:
        tbl_lower = tbl.lower()
        tbl_attrs = by_table.get(tbl, [])
        bicc_count = sum(1 for a in tbl_attrs if a.get('bicc'))
        pk_count = sum(1 for a in tbl_attrs if a.get('pk'))
        detail = []
        if pk_count:
            detail.append(f'{pk_count} PKs')
        if bicc_count:
            detail.append(f'{bicc_count} BICC')
        detail_str = f' ({", ".join(detail)})' if detail else ''
        lines.append(f'- [[{tbl_lower}|{tbl}]] — {len(tbl_attrs)} atributos{detail_str}')
    lines.append('')

    lines.append('---')
    lines.append('')

    # Atributos por Tabela
    lines.append('## ⚙️ Atributos')
    lines.append('')

    for tbl in tables:
        tbl_lower = tbl.lower()
        tbl_attrs = by_table.get(tbl, [])
        if not tbl_attrs:
            continue

        lines.append(f'### [[{tbl_lower}|{tbl}]]')
        lines.append('')
        lines.append('| # | Atributo | Coluna | PK | BICC |')
        lines.append('|---|----------|--------|----|------|')

        for idx, attr in enumerate(tbl_attrs, 1):
            pk_str = '🔑' if attr.get('pk') else '—'
            bicc_str = '✅' if attr.get('bicc') else '—'
            lines.append(f'| {idx} | {attr["attribute"]} | {attr["column"]} | {pk_str} | {bicc_str} |')

        lines.append('')

    lines.append('---')
    lines.append('')

    # Referências
    lines.append('## 📚 Referências')
    lines.append('')
    lines.append(f'- [[{module_code.lower()}-module-data-dictionary]] — Dossiê do módulo {module_code}')
    lines.append('')

    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='Build .md for PVOs from JSON')
    parser.add_argument('--module', default='', help='Module code (e.g., GL, AP). If empty, all modules.')
    parser.add_argument('--pvo', default='', help='Specific PVO name (e.g., BalancePVO)')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done')
    args = parser.parse_args()

    # Find project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    if not (project_root / 'CLAUDE.md').exists():
        project_root = Path.cwd()

    docs_dir = project_root / 'src' / 'kb' / 'oracle-fusion-data-dictionary' / 'docs'

    # Variaveis
    variaveis = load_variaveis(str(project_root / 'docs' / 'assets' / 'variaveis.md'))

    # Table map (for wikilinks validation - not critical)
    table_map = {}

    # Discover modules
    if args.module:
        module_dirs = [docs_dir / args.module]
    else:
        module_dirs = sorted(d for d in docs_dir.iterdir() if d.is_dir() and (d / 'pvos').is_dir())

    total_generated = 0
    total_skipped = 0

    for mod_dir in module_dirs:
        pvos_dir = mod_dir / 'pvos'
        if not pvos_dir.is_dir():
            continue

        module_code = mod_dir.name
        json_files = sorted(f for f in pvos_dir.glob('*.json') if not f.name.endswith('.i18n.json'))

        if args.pvo:
            json_files = [f for f in json_files if f.stem.lower() == args.pvo.lower()]

        if not json_files:
            continue

        print(f'Module {module_code}: {len(json_files)} PVOs')

        for jf in json_files:
            md_path = jf.with_suffix('.md')

            try:
                md_content = build_md(str(jf), variaveis, table_map)
            except Exception as e:
                print(f'  FAIL {jf.name}: {e}')
                total_skipped += 1
                continue

            if args.dry_run:
                print(f'  WOULD CREATE {md_path.name}')
            else:
                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(md_content)
                print(f'  OK {md_path.stem}.md')

            total_generated += 1

    print(f'\nDone. Generated: {total_generated}, Skipped: {total_skipped}')


if __name__ == '__main__':
    main()
