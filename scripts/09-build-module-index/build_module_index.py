#!/usr/bin/env python3
"""
build_module_index.py — Gera index.html para cada módulo do data dictionary

Uso:
    python build_module_index.py                    # Gera para todos os módulos
    python build_module_index.py --module AR        # Gera só para AR
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path


def load_table_map(mappings_path: str) -> dict:
    """Carrega table-mappings.txt e retorna {MODULE: [TABLE_NAME, ...]}."""
    modules = {}
    current_module = None
    current_name = None
    current_count = None
    in_core = False

    with open(mappings_path, 'r', encoding='utf-8') as f:
        for line in f:
            stripped = line.strip()
            mod_match = re.match(r'===\s*(\w+)\s*[—-]\s*(.+?)\s*\((\d+)\s*core', stripped)
            if mod_match:
                current_module = mod_match.group(1)
                current_name = mod_match.group(2).strip()
                current_count = int(mod_match.group(3))
                modules[current_module] = {'name': current_name, 'expected': current_count, 'tables': []}
                in_core = False
                continue
            if 'Core Tables' in stripped:
                in_core = True
                continue
            if 'Referenced Tables' in stripped:
                in_core = False
                continue
            if in_core and current_module and re.match(r'^[A-Z][A-Z0-9_]+$', stripped):
                modules[current_module]['tables'].append(stripped)

    return modules


def parse_md_summary(md_path: str) -> dict:
    """Extrai resumo de um .md (título, overview, contagem de colunas)."""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Front matter
    meta = {}
    if content.startswith('---'):
        end = content.find('---', 3)
        if end != -1:
            fm = content[3:end]
            for line in fm.split('\n'):
                if ':' in line and not line.strip().startswith('-') and not line.strip().startswith('#'):
                    k, _, v = line.partition(':')
                    meta[k.strip()] = v.strip().strip('"').strip("'")

    # Count columns (table rows)
    col_count = 0
    in_table = False
    pk_cols = []
    for line in content.split('\n'):
        stripped = line.strip()
        if stripped.startswith('| #') or stripped.startswith('| Coluna') or stripped.startswith('| Column'):
            in_table = True
            continue
        if stripped.startswith('|---'):
            continue
        if in_table and stripped.startswith('|'):
            col_count += 1
            cells = [c.strip() for c in stripped.split('|')[1:-1]]
            # Check for PK
            for cell in cells:
                if cell.upper() in ('PK', 'PK.') or cell.startswith('PK.') or cell.startswith('PK '):
                    if len(cells) > 1:
                        pk_cols.append(cells[1] if len(cells) > 1 else '')
                    break
        elif in_table and not stripped.startswith('|'):
            in_table = False

    # Overview (first paragraph after ## Visão Geral)
    overview = ''
    in_overview = False
    for line in content.split('\n'):
        if line.strip().startswith('## ') and ('Visão Geral' in line or 'Overview' in line):
            in_overview = True
            continue
        if in_overview and line.strip() and not line.strip().startswith('>') and not line.strip().startswith('---') and not line.strip().startswith('#'):
            overview = line.strip()
            overview = re.sub(r'\*\*([^*]+)\*\*', r'\1', overview)
            overview = re.sub(r'`([^`]+)`', r'\1', overview)
            if len(overview) > 200:
                overview = overview[:197] + '...'
            break

    title = meta.get('title', '').split('—')[-1].strip() if '—' in meta.get('title', '') else ''

    return {
        'title': title,
        'overview': overview,
        'col_count': col_count,
        'pk_cols': pk_cols,
    }


MODULE_META = {
    'GL': {'icon': 'ri-book-2-line', 'color': 'primary', 'name': 'General Ledger',
           'desc_pt': 'Contabilidade geral — razão contábil, lançamentos, saldos, calendários e estrutura de ledgers.',
           'desc_en': 'General accounting — general ledger, journal entries, balances, calendars, and ledger structure.',
           'desc_es': 'Contabilidad general — libro mayor, asientos contables, saldos, calendarios y estructura de ledgers.'},
    'AP': {'icon': 'ri-money-dollar-circle-line', 'color': 'warning', 'name': 'Accounts Payable',
           'desc_pt': 'Contas a pagar — faturas de fornecedores, pagamentos, cheques e distribuições contábeis.',
           'desc_en': 'Accounts payable — supplier invoices, payments, checks, and accounting distributions.',
           'desc_es': 'Cuentas por pagar — facturas de proveedores, pagos, cheques y distribuciones contables.'},
    'AR': {'icon': 'ri-hand-coin-line', 'color': 'success', 'name': 'Accounts Receivable',
           'desc_pt': 'Contas a receber — faturas, recebimentos, ajustes, schedules de pagamento e reconciliação.',
           'desc_en': 'Accounts receivable — invoices, receipts, adjustments, payment schedules, and reconciliation.',
           'desc_es': 'Cuentas por cobrar — facturas, recibos, ajustes, calendarios de pago y conciliación.'},
    'PO': {'icon': 'ri-shopping-cart-2-line', 'color': 'orange', 'name': 'Procurement',
           'desc_pt': 'Compras — ordens de compra, requisições, recebimentos, fornecedores e contratos.',
           'desc_en': 'Procurement — purchase orders, requisitions, receipts, suppliers, and contracts.',
           'desc_es': 'Compras — órdenes de compra, requisiciones, recepciones, proveedores y contratos.'},
    'HCM': {'icon': 'ri-team-line', 'color': 'teal', 'name': 'Human Capital Management',
            'desc_pt': 'Gestão de pessoas — colaboradores, cargos, folha de pagamento, benefícios e talent management.',
            'desc_en': 'Human capital management — employees, positions, payroll, benefits, and talent management.',
            'desc_es': 'Gestión de personas — colaboradores, cargos, nómina, beneficios y talent management.'},
}


def build_module_index(module_code: str, tables: list, project_root: Path, docs_root: Path):
    """Gera index.html para um módulo."""
    meta = MODULE_META.get(module_code, {})
    module_dir = docs_root / 'data-dictionary' / module_code
    tables_dir = module_dir / 'tables'
    md_base = project_root / 'src' / 'kb' / 'oracle-fusion-data-dictionary' / 'docs' / module_code / 'tables'

    # Collect table data
    table_data = []
    for table_name in sorted(tables):
        fname = table_name.lower()
        md_path = md_base / f'{fname}.md'
        has_html = (tables_dir / f'{fname}.html').exists()

        summary = {'title': '', 'overview': '', 'col_count': 0, 'pk_cols': []}
        if md_path.exists():
            summary = parse_md_summary(str(md_path))

        # Load i18n translations for overview
        overview_en = ''
        overview_es = ''
        i18n_path = md_base / f'{fname}.i18n.json'
        if i18n_path.exists() and summary['overview']:
            try:
                with open(str(i18n_path), 'r', encoding='utf-8') as jf:
                    i18n_data = json.load(jf)
                # Build lookup map
                i18n_map = {}
                for item in i18n_data.get('items', []):
                    if item.get('br'):
                        i18n_map[item['br']] = {'en': item.get('en', ''), 'es': item.get('es', '')}

                # Try exact match first, then substring
                ov_clean = summary['overview'].rstrip('.')
                for br_text, trans in i18n_map.items():
                    if br_text in ov_clean or ov_clean in br_text:
                        if len(br_text) > len(ov_clean) * 0.5:
                            overview_en = trans.get('en', '')
                            overview_es = trans.get('es', '')
                            if overview_en and len(overview_en) > 200:
                                overview_en = overview_en[:197] + '...'
                            if overview_es and len(overview_es) > 200:
                                overview_es = overview_es[:197] + '...'
                            break
            except Exception:
                pass

        table_data.append({
            'name': table_name,
            'title': summary['title'],
            'overview': summary['overview'],
            'overview_en': overview_en,
            'overview_es': overview_es,
            'col_count': summary['col_count'],
            'pk_count': len(summary['pk_cols']),
            'pks': ', '.join(summary['pk_cols']),
            'has_html': has_html,
        })

    # Collect PVO data
    pvo_data = []
    pvos_src_dir = project_root / 'src' / 'kb' / 'oracle-fusion-data-dictionary' / 'docs' / module_code / 'pvos'
    pvos_html_dir = docs_root / 'data-dictionary' / module_code / 'pvos'
    if pvos_src_dir.exists():
        for pvo_file in sorted(pvos_src_dir.glob('*.json')):
            if pvo_file.name.endswith('.i18n.json'):
                continue
            try:
                with open(str(pvo_file), 'r', encoding='utf-8') as jf:
                    pvo_json = json.load(jf)
                pvo_meta = pvo_json.get('meta', {})
                pvo_name = pvo_meta.get('pvo_name', pvo_file.stem)
                pvo_path = pvo_meta.get('full_path', '')
                pvo_desc = pvo_meta.get('description', '')
                attr_count = len(pvo_json.get('attributes', []))

                # Truncate description
                if len(pvo_desc) > 200:
                    pvo_desc = pvo_desc[:197] + '...'

                # Load i18n
                pvo_desc_en = ''
                pvo_desc_es = ''
                i18n_file = pvos_src_dir / f'{pvo_file.stem}.i18n.json'
                if i18n_file.exists():
                    try:
                        with open(str(i18n_file), 'r', encoding='utf-8') as ijf:
                            i18n_pvo = json.load(ijf)
                        items = i18n_pvo.get('items', [])
                        if items:
                            pvo_desc_en = items[0].get('en', '')
                            pvo_desc_es = items[0].get('es', '')
                            if pvo_desc_en and len(pvo_desc_en) > 200:
                                pvo_desc_en = pvo_desc_en[:197] + '...'
                            if pvo_desc_es and len(pvo_desc_es) > 200:
                                pvo_desc_es = pvo_desc_es[:197] + '...'
                    except Exception:
                        pass

                has_pvo_html = (pvos_html_dir / f'{pvo_file.stem}.html').exists()

                pvo_data.append({
                    'name': pvo_name,
                    'path': pvo_path,
                    'desc': pvo_desc,
                    'desc_en': pvo_desc_en,
                    'desc_es': pvo_desc_es,
                    'attr_count': attr_count,
                    'has_html': has_pvo_html,
                })
            except Exception:
                pass

    pvo_count = len(pvo_data)
    has_pvos = pvo_count > 0

    # Read variaveis
    variaveis_path = project_root / 'docs' / 'assets' / 'variaveis.md'
    author = 'Fabio A. B. Rodrigues'
    email = ''
    company = 'Patria Investimentos'
    if variaveis_path.exists():
        with open(variaveis_path, 'r', encoding='utf-8') as f:
            for line in f:
                m = re.match(r'\|\s*`\{\{(\w+)\}\}`\s*\|\s*(.+?)\s*\|', line)
                if m:
                    if m.group(1) == 'AUTOR_NOME': author = m.group(2)
                    if m.group(1) == 'AUTOR_EMAIL': email = m.group(2)
                    if m.group(1) == 'EMPRESA': company = m.group(2)

    data_json = json.dumps(table_data, ensure_ascii=False)
    pvo_data_json = json.dumps(pvo_data, ensure_ascii=False)

    html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{meta.get("name", module_code)} — Data Dictionary</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/remixicon@4.1.0/fonts/remixicon.css" rel="stylesheet">
    <style>

:root {{
    --primary: #5BA4D9; --primary-dark: #3182B1; --primary-light: rgba(91, 164, 217, 0.12);
    --secondary: #5BB8C4; --success: #6ABF3B; --success-light: rgba(106, 191, 59, 0.12); --success-border: rgba(106, 191, 59, 0.3);
    --warning: #F4AC00; --warning-light: rgba(244, 172, 0, 0.12); --warning-border: rgba(244, 172, 0, 0.3);
    --danger: #E85D54; --info: #38BDF8; --info-light: rgba(56, 189, 248, 0.12); --info-border: rgba(56, 189, 248, 0.3);
    --bg: #0f1319; --card-bg: #1a1f2e; --text: #e2e8f0; --text-muted: #8b9ab5; --border: #2a3244;
    --purple: #9B96FF; --purple-light: rgba(155, 150, 255, 0.12); --orange: #FF9473; --teal: #2DD4BF;
    --card-header-bg: #141924; --th-bg: #141924; --th-bg-hover: #1e2638;
    --card-shadow: 0 2px 12px rgba(91, 164, 217, 0.1), 0 1px 4px rgba(0,0,0,0.3);
}}
[data-theme="light"] {{
    --primary: #3182B1; --primary-dark: #256a94; --primary-light: rgba(49, 130, 177, 0.1);
    --secondary: #418F9D; --success: #4C7E1B; --success-light: rgba(76, 126, 27, 0.08); --success-border: rgba(76, 126, 27, 0.25);
    --warning: #F4AC00; --warning-light: rgba(244, 172, 0, 0.08); --warning-border: rgba(244, 172, 0, 0.25);
    --danger: #C72F25; --info: #0EA5E8; --info-light: rgba(14, 165, 232, 0.08); --info-border: rgba(14, 165, 232, 0.25);
    --bg: #dde2e8; --card-bg: #ffffff; --text: #212B37; --text-muted: #6E829F; --border: #e2e8f0;
    --purple: #7B76FE; --purple-light: rgba(123, 118, 254, 0.08); --orange: #FE7C58; --teal: #00D8D8;
    --card-header-bg: rgba(49, 130, 177, 0.2); --th-bg: rgba(49, 130, 177, 0.2); --th-bg-hover: rgba(49, 130, 177, 0.23);
    --card-shadow: 0 2px 8px rgba(49, 130, 177, 0.24), 0 1px 3px rgba(0,0,0,0.1);
}}
[data-theme="light"] .search-input {{ background: #eaf1f7; }}

html, body, div, span, h1, h2, h3, h4, h5, h6, p, a, img, ul, ol, li,
header, footer, nav, section, article, aside, button, input, select, textarea,
table, tr, td, th, form, label, fieldset, legend {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: 'Poppins', sans-serif; background: var(--bg); color: var(--text); line-height: 1.5; }}
.container {{ max-width: 1400px; margin: 0 auto; padding: 0 24px; }}

.header {{ background: linear-gradient(135deg, #1a2332 0%, #15202e 50%, #1a2838 100%); color: white; padding: 36px 0 0; position: relative; overflow: hidden; }}
.header::before {{ content: ''; position: absolute; top: -50%; right: -10%; width: 500px; height: 500px; background: rgba(255,255,255,0.03); border-radius: 50%; z-index: 0; }}
.header-content {{ position: relative; z-index: 1; }}
.header-bc-row {{ display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; }}
.breadcrumb {{ font-size: 0.78rem; color: rgba(255,255,255,0.5); }}
.breadcrumb a {{ color: rgba(255,255,255,0.65); text-decoration: none; }}
.breadcrumb a:hover {{ color: white; text-decoration: underline; }}
.breadcrumb .sep {{ margin: 0 6px; opacity: 0.4; }}
.breadcrumb .current {{ color: rgba(255,255,255,0.9); font-weight: 500; }}
.header-controls {{ display: flex; align-items: center; gap: 8px; }}
.lang-btn {{ display: inline-flex; align-items: center; gap: 5px; background: rgba(255,255,255,0.08); border: 2px solid transparent; border-radius: 8px; padding: 4px 10px 4px 8px; font-family: 'Poppins', sans-serif; font-size: 0.72rem; font-weight: 600; letter-spacing: 0.3px; color: rgba(255,255,255,0.55); cursor: pointer; transition: all 0.25s; line-height: 1; }}
.lang-btn svg {{ flex-shrink: 0; }}
.lang-btn:hover {{ background: rgba(255,255,255,0.18); color: rgba(255,255,255,0.9); }}
.lang-btn.active {{ border-color: #ffffff; background: rgba(255,255,255,0.22); color: #ffffff; box-shadow: 0 0 8px rgba(255,255,255,0.25); }}
[data-theme="light"] .header {{ background: linear-gradient(135deg, #1a2332 0%, #15202e 50%, #1a2838 100%); color: white; }}
[data-theme="light"] .footer {{ background: linear-gradient(135deg, #1a2332 0%, #15202e 50%, #1a2838 100%); color: white; }}

.header-left {{ display: flex; align-items: center; gap: 16px; }}
.header-logo {{ height: 40px; }}
.logo-light {{ display: none; }} .logo-dark {{ display: inline-block; }}
.header h1 {{ font-size: 1.5rem; font-weight: 700; letter-spacing: -0.5px; }}
.header .subtitle {{ font-size: 0.95rem; opacity: 0.85; font-weight: 300; margin-top: 2px; }}
.header-badges {{ display: flex; gap: 8px; align-items: center; margin-top: 10px; }}
.header-badge {{ background: rgba(255,255,255,0.15); padding: 6px 14px; border-radius: 8px; font-size: 0.78rem; display: flex; align-items: center; gap: 6px; backdrop-filter: blur(10px); }}

.stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px; margin: 28px 0; }}
.stat-card {{ background: var(--card-bg); border-radius: 12px; padding: 18px 20px; box-shadow: var(--card-shadow); border: 1px solid var(--border); display: flex; align-items: center; gap: 14px; }}
.stat-card-icon {{ width: 44px; height: 44px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.3rem; color: white; flex-shrink: 0; }}
.stat-card-number {{ font-size: 1.12rem; font-weight: 700; line-height: 1.1; }}
.stat-card-label {{ font-size: 0.72rem; color: var(--text-muted); font-weight: 500; text-transform: uppercase; letter-spacing: 0.3px; }}
.bg-primary {{ background: var(--primary); }} .bg-success {{ background: var(--success); }}
.bg-info {{ background: var(--info); }} .bg-warning {{ background: var(--warning); }}
.bg-purple {{ background: var(--purple); }} .bg-orange {{ background: var(--orange); }} .bg-teal {{ background: var(--teal); }}

.search-container {{ position: relative; margin-bottom: 20px; }}
.search-icon {{ position: absolute; left: 16px; top: 50%; transform: translateY(-50%); color: var(--text-muted); font-size: 1.1rem; }}
.search-input {{ width: 100%; padding: 12px 16px 12px 44px; background: var(--card-bg); border: 1px solid var(--border); border-radius: 12px; color: var(--text); font-family: 'Poppins', sans-serif; font-size: 0.88rem; outline: none; transition: border-color 0.2s; }}
.search-input:focus {{ border-color: var(--primary); }}
.search-input::placeholder {{ color: var(--text-muted); }}

.table-wrapper {{ overflow-x: auto; }}
table {{ width: 100%; border-collapse: collapse; font-size: 0.82rem; }}
th {{ text-align: left; padding: 10px 14px; background: var(--th-bg); font-weight: 600; border-bottom: 2px solid var(--border); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.3px; color: var(--text-muted); }}
thead tr:hover th {{ background: var(--th-bg-hover); }}
td {{ padding: 10px 14px; border-bottom: 1px solid var(--border); }}
tr:hover {{ background: var(--primary-light); }}
tr {{ cursor: pointer; transition: background 0.15s; }}
.col-name {{ font-family: 'Courier New', monospace; font-weight: 600; color: var(--primary); font-size: 0.82rem; }}
.col-desc {{ font-size: 0.78rem; color: var(--text-muted); max-width: 500px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
.pill {{ display: inline-block; padding: 2px 10px; border-radius: 12px; font-size: 0.7rem; font-weight: 600; }}
.pill-success {{ background: var(--success-light); color: var(--success); border: 1px solid var(--success-border); }}
.pill-info {{ background: var(--info-light); color: var(--info); border: 1px solid var(--info-border); }}
.pill-warning {{ background: var(--warning-light); color: var(--warning); border: 1px solid var(--warning-border); }}
.no-results {{ text-align: center; padding: 48px 24px; color: var(--text-muted); font-size: 0.9rem; display: none; }}
.no-results i {{ font-size: 2.5rem; display: block; margin-bottom: 12px; }}

.tabs {{ display: flex; gap: 0; margin-bottom: 20px; border-bottom: 2px solid var(--border); }}
.tab-btn {{ padding: 10px 20px; background: none; border: none; border-bottom: 2px solid transparent; margin-bottom: -2px; color: var(--text-muted); font-family: 'Poppins', sans-serif; font-size: 0.85rem; font-weight: 500; cursor: pointer; display: flex; align-items: center; gap: 8px; transition: all 0.2s; }}
.tab-btn:hover {{ color: var(--text); }}
.tab-btn.active {{ color: var(--primary); border-bottom-color: var(--primary); font-weight: 600; }}
.tab-btn .tab-count {{ background: var(--primary-light); color: var(--primary); padding: 2px 8px; border-radius: 10px; font-size: 0.72rem; font-weight: 600; }}
.tab-panel {{ display: none; }}
.tab-panel.active {{ display: block; }}

.footer {{ background: linear-gradient(135deg, #1a2332 0%, #15202e 50%, #1a2838 100%); color: white; padding: 36px 0; position: relative; overflow: hidden; margin-top: 32px; }}
.footer::before {{ content: ''; position: absolute; bottom: -50%; left: -10%; width: 500px; height: 500px; background: rgba(255,255,255,0.03); border-radius: 50%; z-index: 0; }}
.footer-content {{ position: relative; z-index: 1; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 24px; }}
.footer-left {{ display: flex; align-items: center; gap: 16px; }}
.footer-avatar {{ width: 48px; height: 48px; border-radius: 12px; background: rgba(255,255,255,0.15); display: flex; align-items: center; justify-content: center; font-size: 1.1rem; font-weight: 700; }}
.footer-author-name {{ font-size: 0.95rem; font-weight: 600; }}
.footer-author-role {{ font-size: 0.78rem; opacity: 0.7; }}
.footer-author-email {{ font-size: 0.72rem; opacity: 0.55; }}
.footer-author-email a {{ color: rgba(255,255,255,0.55); text-decoration: none; }}
.footer-author-email a:hover {{ color: white; }}
.footer-right {{ text-align: right; }}
.footer-doc-title {{ font-size: 0.85rem; font-weight: 500; opacity: 0.9; }}
.footer-doc-detail {{ font-size: 0.72rem; opacity: 0.6; }}
.footer-seal {{ display: flex; align-items: center; gap: 8px; margin-top: 20px; padding-top: 16px; border-top: 1px solid rgba(255,255,255,0.12); font-size: 0.7rem; opacity: 0.5; justify-content: center; }}
.footer-seal i {{ font-size: 1rem; }}

.back-to-top {{ position: fixed; bottom: 32px; right: 32px; width: 44px; height: 44px; border-radius: 12px; background: var(--primary); color: white; border: none; cursor: pointer; display: flex; align-items: center; justify-content: center; font-size: 1.3rem; box-shadow: 0 4px 16px rgba(91,164,217,0.35); opacity: 0; visibility: hidden; transform: translateY(10px); transition: all 0.3s; z-index: 999; }}
.back-to-top.visible {{ opacity: 1; visibility: visible; transform: translateY(0); }}
.back-to-top:hover {{ background: var(--primary-dark); }}

@media (max-width: 768px) {{ .stats-grid {{ grid-template-columns: 1fr 1fr; }} .col-desc {{ max-width: 200px; }} }}
@media print {{ .header {{ background: #3182B1 !important; }} .search-container, .back-to-top {{ display: none; }} .tab-content {{ display: block !important; }} }}

    </style>
</head>
<body>

<header class="header">
    <div class="container">
        <div class="header-content">
            <div class="header-bc-row">
                <nav class="breadcrumb">
                    <a href="../../index.html">Oracle Fusion Data Dictionary</a><span class="sep">&rsaquo;</span>
                    <span class="current">{module_code} - {meta.get("name", module_code)}</span>
                </nav>
                <div class="header-controls">
                    <button class="lang-btn active" onclick="switchLang('pt')" id="lang-pt"><svg width="20" height="14" viewBox="0 0 20 14"><rect width="20" height="14" rx="1" fill="#009739"/><polygon points="10,1.5 19,7 10,12.5 1,7" fill="#FEDD00"/><circle cx="10" cy="7" r="3.2" fill="#012169"/><rect x="7.8" y="6.2" width="4.4" height="0.4" rx="0.2" fill="#fff" transform="rotate(-8 10 7)"/></svg> <span>PT</span></button>
                    <button class="lang-btn" onclick="switchLang('en')" id="lang-en"><svg width="20" height="14" viewBox="0 0 20 14"><rect width="20" height="14" rx="1" fill="#B22234"/><rect y="1.08" width="20" height="1.08" fill="#fff"/><rect y="3.23" width="20" height="1.08" fill="#fff"/><rect y="5.38" width="20" height="1.08" fill="#fff"/><rect y="7.54" width="20" height="1.08" fill="#fff"/><rect y="9.69" width="20" height="1.08" fill="#fff"/><rect y="11.85" width="20" height="1.08" fill="#fff"/><rect width="8" height="7.54" fill="#3C3B6E"/></svg> <span>EN</span></button>
                    <button class="lang-btn" onclick="switchLang('es')" id="lang-es"><svg width="20" height="14" viewBox="0 0 20 14"><rect width="20" height="14" rx="1" fill="#AA151B"/><rect y="3" width="20" height="8" fill="#F1BF00"/></svg> <span>ES</span></button>
                    <div class="header-badge" style="border:none;cursor:pointer" onclick="toggleTheme()"><i id="theme-icon" class="ri-sun-line"></i></div>
                </div>
            </div>
            <div class="header-left" style="margin-bottom:24px">
                <img class="header-logo logo-dark" src="../../../assets/logos/logo-dark.png" alt="Logo">
                <img class="header-logo logo-light" src="../../../assets/logos/logo-light.png" alt="Logo">
                <div>
                    <h1><i class="{meta.get('icon', 'ri-database-2-line')}" style="margin-right:8px"></i> {meta.get("name", module_code)} <span style="opacity:0.5;font-size:0.8em">({module_code})</span></h1>
                    <div class="subtitle" data-i18n="desc">{meta.get("desc_pt", "")}</div>
                    <div class="header-badges">
                        <div class="header-badge"><i class="ri-table-line"></i> {len(table_data)} tables</div>
                        {'<div class="header-badge"><i class="ri-eye-line"></i> ' + str(pvo_count) + ' PVOs</div>' if has_pvos else ''}
                        <div class="header-badge"><i class="ri-file-list-3-line"></i> Release 13/25A</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</header>

<div class="container">
    <div class="stats-grid">
        <div class="stat-card"><div class="stat-card-icon bg-{meta.get('color','primary')}"><i class="ri-table-line"></i></div><div><div class="stat-card-number" style="color:var(--{meta.get('color','primary')})">{len(table_data)}</div><div class="stat-card-label" data-i18n="stat_tables">Tabelas</div></div></div>
        <div class="stat-card"><div class="stat-card-icon bg-success"><i class="ri-check-double-line"></i></div><div><div class="stat-card-number" style="color:var(--success)">{sum(1 for t in table_data if t['has_html'])}</div><div class="stat-card-label" data-i18n="stat_documented">Documentadas</div></div></div>
        <div class="stat-card"><div class="stat-card-icon bg-warning"><i class="ri-time-line"></i></div><div><div class="stat-card-number" style="color:var(--warning)">{sum(1 for t in table_data if not t['has_html'])}</div><div class="stat-card-label" data-i18n="stat_pending">Pendentes</div></div></div>
        {'<div class="stat-card"><div class="stat-card-icon bg-purple"><i class="ri-eye-line"></i></div><div><div class="stat-card-number" style="color:var(--purple)">' + str(pvo_count) + '</div><div class="stat-card-label" data-i18n="stat_pvos">PVOs</div></div></div>' if has_pvos else ''}
    </div>

    {'<div class="tabs"><button class="tab-btn active" onclick="switchTab(' + "'tables'" + ')"><i class="ri-table-line"></i> <span data-i18n="tab_tables">Tabelas</span> <span class="tab-count">' + str(len(table_data)) + '</span></button><button class="tab-btn" onclick="switchTab(' + "'pvos'" + ')"><i class="ri-eye-line"></i> <span data-i18n="tab_pvos">PVOs</span> <span class="tab-count">' + str(pvo_count) + '</span></button></div>' if has_pvos else ''}

    <div class="tab-panel active" id="panel-tables">
    <div class="search-container">
        <i class="ri-search-line search-icon"></i>
        <input class="search-input" type="text" placeholder="Filtrar tabelas..." data-i18n-placeholder="search" oninput="filterTables(this.value)">
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th style="width:3%"></th>
                    <th style="width:25%" data-i18n="th_table">Tabela</th>
                    <th style="width:42%" data-i18n="th_desc">Descricao</th>
                    <th style="width:10%;text-align:center" data-i18n="th_cols">Campos</th>
                    <th style="width:10%" data-i18n="th_pk">PK</th>
                    <th style="width:10%;text-align:center">Status</th>
                </tr>
            </thead>
            <tbody id="table-body"></tbody>
        </table>
    </div>
    <div class="no-results" id="no-results"><i class="ri-search-eye-line"></i> <span data-i18n="no_results">Nenhuma tabela encontrada</span></div>
    </div>

    {'<div class="tab-panel" id="panel-pvos"><div class="search-container"><i class="ri-search-line search-icon"></i><input class="search-input" type="text" placeholder="Filtrar PVOs..." data-i18n-placeholder="search_pvo" oninput="filterPvos(this.value)"></div><div class="table-wrapper"><table><thead><tr><th style="width:3%"></th><th style="width:25%" data-i18n="th_pvo">PVO</th><th style="width:47%" data-i18n="th_desc">Descricao</th><th style="width:10%;text-align:center" data-i18n="th_attrs">Atributos</th><th style="width:10%;text-align:center">Status</th></tr></thead><tbody id="pvo-body"></tbody></table></div><div class="no-results" id="no-results-pvo"><i class="ri-search-eye-line"></i> <span data-i18n="no_results_pvo">Nenhum PVO encontrado</span></div></div>' if has_pvos else ''}
</div>

<footer class="footer">
    <div class="container">
        <div class="footer-content">
            <div class="footer-left">
                <div class="footer-avatar">FR</div>
                <div>
                    <div class="footer-author-name">{author}</div>
                    <div class="footer-author-role">Arquitetura e Produtividade Corporativa</div>
                    <div class="footer-author-email"><a href="mailto:{email}">{email}</a></div>
                </div>
            </div>
            <div class="footer-right">
                <div class="footer-doc-title">{company}</div>
                <div class="footer-doc-detail">{meta.get("name", module_code)} &middot; Data Dictionary</div>
            </div>
        </div>
        <div class="footer-seal"><i class="ri-shield-check-line"></i> Oracle Fusion Data Dictionary</div>
    </div>
</footer>

<button class="back-to-top" id="backToTop" onclick="window.scrollTo({{top:0,behavior:'smooth'}})"><i class="ri-arrow-up-line"></i></button>

<script>
var TABLES = {data_json};
var PVOS = {pvo_data_json};
var currentLang = 'pt';

var i18n = {{
    pt: {{ desc: '{meta.get("desc_pt","").replace("'", "\\'")}', stat_tables: 'Tabelas', stat_documented: 'Documentadas', stat_pending: 'Pendentes', stat_pvos: 'PVOs', search: 'Filtrar tabelas...', th_table: 'Tabela', th_desc: 'Descricao', th_cols: 'Campos', th_pk: 'PK', no_results: 'Nenhuma tabela encontrada', tab_tables: 'Tabelas', tab_pvos: 'PVOs', search_pvo: 'Filtrar PVOs...', th_pvo: 'PVO', th_attrs: 'Atributos', no_results_pvo: 'Nenhum PVO encontrado' }},
    en: {{ desc: '{meta.get("desc_en","").replace("'", "\\'")}', stat_tables: 'Tables', stat_documented: 'Documented', stat_pending: 'Pending', stat_pvos: 'PVOs', search: 'Filter tables...', th_table: 'Table', th_desc: 'Description', th_cols: 'Columns', th_pk: 'PK', no_results: 'No tables found', tab_tables: 'Tables', tab_pvos: 'PVOs', search_pvo: 'Filter PVOs...', th_pvo: 'PVO', th_attrs: 'Attributes', no_results_pvo: 'No PVOs found' }},
    es: {{ desc: '{meta.get("desc_es","").replace("'", "\\'")}', stat_tables: 'Tablas', stat_documented: 'Documentadas', stat_pending: 'Pendientes', stat_pvos: 'PVOs', search: 'Filtrar tablas...', th_table: 'Tabla', th_desc: 'Descripcion', th_cols: 'Campos', th_pk: 'PK', no_results: 'Ninguna tabla encontrada', tab_tables: 'Tablas', tab_pvos: 'PVOs', search_pvo: 'Filtrar PVOs...', th_pvo: 'PVO', th_attrs: 'Atributos', no_results_pvo: 'Ningun PVO encontrado' }}
}};

function renderTable(filter) {{
    var q = (filter || '').toLowerCase();
    var tbody = document.getElementById('table-body');
    var html = '';
    var count = 0;
    TABLES.forEach(function(t) {{
        var desc = currentLang === 'en' ? (t.overview_en || t.overview || '') : currentLang === 'es' ? (t.overview_es || t.overview || '') : (t.overview || '');
        var match = !q || t.name.toLowerCase().indexOf(q) >= 0 || desc.toLowerCase().indexOf(q) >= 0 || (t.title || '').toLowerCase().indexOf(q) >= 0;
        if (!match) return;
        count++;
        var href = t.has_html ? 'tables/' + t.name.toLowerCase() + '.html' + (currentLang !== 'pt' ? '?lang=' + currentLang : '') : '#';
        var status = t.has_html ? '<span class="pill pill-success"><i class="ri-check-line"></i></span>' : '<span class="pill pill-warning"><i class="ri-time-line"></i></span>';
        var clickable = t.has_html ? ' onclick="window.location.href=\\'' + href + '\\'"' : '';
        html += '<tr' + clickable + ' style="' + (t.has_html ? '' : 'opacity:0.5') + '">' +
            '<td><i class="ri-table-2" style="color:var(--{meta.get("color","primary")})"></i></td>' +
            '<td class="col-name">' + t.name + '</td>' +
            '<td class="col-desc">' + desc + '</td>' +
            '<td style="text-align:center">' + (t.col_count || '—') + '</td>' +
            '<td>' + (t.pks || '—') + '</td>' +
            '<td style="text-align:center">' + status + '</td></tr>';
    }});
    tbody.innerHTML = html;
    document.getElementById('no-results').style.display = count === 0 ? '' : 'none';
}}

function filterTables(q) {{ renderTable(q); }}

function renderPvos(filter) {{
    var q = (filter || '').toLowerCase();
    var tbody = document.getElementById('pvo-body');
    if (!tbody) return;
    var html = '';
    var count = 0;
    PVOS.forEach(function(p) {{
        var desc = currentLang === 'en' ? (p.desc_en || p.desc || '') : currentLang === 'es' ? (p.desc_es || p.desc || '') : (p.desc || '');
        var match = !q || p.name.toLowerCase().indexOf(q) >= 0 || desc.toLowerCase().indexOf(q) >= 0 || (p.path || '').toLowerCase().indexOf(q) >= 0;
        if (!match) return;
        count++;
        var href = p.has_html ? 'pvos/' + p.name.toLowerCase() + '.html' + (currentLang !== 'pt' ? '?lang=' + currentLang : '') : '#';
        var status = p.has_html ? '<span class="pill pill-success"><i class="ri-check-line"></i></span>' : '<span class="pill pill-warning"><i class="ri-time-line"></i></span>';
        var clickable = p.has_html ? ' onclick="window.location.href=\\'' + href + '\\'"' : '';
        html += '<tr' + clickable + ' style="' + (p.has_html ? '' : 'opacity:0.5') + '">' +
            '<td><i class="ri-eye-line" style="color:var(--purple)"></i></td>' +
            '<td class="col-name">' + p.name + '</td>' +
            '<td class="col-desc">' + desc + '</td>' +
            '<td style="text-align:center">' + (p.attr_count || '—') + '</td>' +
            '<td style="text-align:center">' + status + '</td></tr>';
    }});
    tbody.innerHTML = html;
    var nr = document.getElementById('no-results-pvo');
    if (nr) nr.style.display = count === 0 ? '' : 'none';
}}

function filterPvos(q) {{ renderPvos(q); }}

function switchTab(tab) {{
    document.querySelectorAll('.tab-btn').forEach(function(b) {{ b.classList.remove('active'); }});
    document.querySelectorAll('.tab-panel').forEach(function(p) {{ p.classList.remove('active'); }});
    document.querySelector('.tab-btn[onclick*="' + tab + '"]').classList.add('active');
    document.getElementById('panel-' + tab).classList.add('active');
}}

function switchLang(lang) {{
    currentLang = lang;
    localStorage.setItem('preferred-lang', lang);
    document.querySelectorAll('.lang-btn').forEach(function(b) {{ b.classList.remove('active'); }});
    document.getElementById('lang-' + lang).classList.add('active');
    document.querySelectorAll('[data-i18n]').forEach(function(el) {{
        var key = el.getAttribute('data-i18n');
        if (i18n[lang] && i18n[lang][key]) el.innerHTML = i18n[lang][key];
    }});
    document.querySelectorAll('[data-i18n-placeholder]').forEach(function(el) {{
        var key = el.getAttribute('data-i18n-placeholder');
        if (i18n[lang] && i18n[lang][key]) el.placeholder = i18n[lang][key];
    }});
    renderTable(document.querySelector('#panel-tables .search-input').value);
    renderPvos(document.querySelector('#panel-pvos .search-input') ? document.querySelector('#panel-pvos .search-input').value : '');
}}

function toggleTheme() {{
    var c = document.body.getAttribute('data-theme');
    document.body.setAttribute('data-theme', c === 'light' ? '' : 'light');
    document.getElementById('theme-icon').className = c === 'light' ? 'ri-sun-line' : 'ri-moon-line';
    localStorage.setItem('theme', document.body.getAttribute('data-theme') || 'dark');
}}

(function() {{
    var t = localStorage.getItem('theme');
    if (t === 'light') {{ document.body.setAttribute('data-theme', 'light'); document.getElementById('theme-icon').className = 'ri-moon-line'; }}
    var ul = new URLSearchParams(window.location.search).get('lang');
    var tl = ul || localStorage.getItem('preferred-lang');
    if (tl && tl !== 'pt') switchLang(tl);
    renderTable('');
    renderPvos('');
    var btn = document.getElementById('backToTop');
    window.addEventListener('scroll', function() {{ btn.classList.toggle('visible', window.scrollY > 300); }});
}})();
</script>
</body>
</html>'''

    output_path = module_dir / 'index.html'
    os.makedirs(str(module_dir), exist_ok=True)
    with open(str(output_path), 'w', encoding='utf-8') as f:
        f.write(html)
    return str(output_path)


def main():
    parser = argparse.ArgumentParser(description='Build module index pages')
    parser.add_argument('--module', help='Module code (e.g., AR). Default: all modules')
    args = parser.parse_args()

    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    docs_root = project_root / 'docs' / 'fusion-kb'

    mappings_path = project_root / 'src' / 'kb' / 'oracle-fusion-data-dictionary' / 'docs' / 'table-mappings.txt'
    modules = load_table_map(str(mappings_path))

    targets = [args.module.upper()] if args.module else list(modules.keys())

    for mod in targets:
        if mod not in modules:
            print(f'SKIP: {mod} not in table-mappings.txt')
            continue
        tables = modules[mod]['tables']
        result = build_module_index(mod, tables, project_root, docs_root)
        # Count pvos for log
        pvos_dir = project_root / 'src' / 'kb' / 'oracle-fusion-data-dictionary' / 'docs' / mod / 'pvos'
        pvo_count = len([f for f in pvos_dir.glob('*.json') if not f.name.endswith('.i18n.json')]) if pvos_dir.exists() else 0
        print(f'  OK {mod} ({len(tables)} tables, {pvo_count} pvos) -> {result}')

    print('Done.')


if __name__ == '__main__':
    main()
