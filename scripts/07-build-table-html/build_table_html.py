#!/usr/bin/env python3
"""
build_html.py — Gera HTML de system-doc (data dictionary) a partir de .md + .i18n.md

Uso:
    python build_html.py <arquivo.md> [--mode standalone|linked] [--assets-dir <path>]
    python build_html.py --batch <pasta> [--mode standalone|linked] [--assets-dir <path>]

Exemplos:
    python build_html.py ar_adjustments_all.md
    python build_html.py --batch src/kb/oracle-fusion-data-dictionary/docs/AR/tables/
    python build_html.py ar_adjustments_all.md --mode linked --assets-dir ../../../assets/data-dictionary
"""

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path


# ============================================================
# PARSERS
# ============================================================

def parse_front_matter(content: str) -> tuple[dict, str]:
    """Extrai front matter YAML e retorna (metadata_dict, body)."""
    if not content.startswith('---'):
        return {}, content
    end = content.find('---', 3)
    if end == -1:
        return {}, content
    fm_text = content[3:end].strip()
    body = content[end + 3:].strip()

    meta = {}
    current_key = None
    current_list = None
    for line in fm_text.split('\n'):
        stripped = line.strip()
        if stripped.startswith('#') or not stripped:
            continue
        if stripped.startswith('- ') and current_key:
            if current_list is None:
                current_list = []
                meta[current_key] = current_list
            current_list.append(stripped[2:].strip().strip('"').strip("'"))
            continue
        if ':' in stripped:
            key, _, val = stripped.partition(':')
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            current_key = key
            current_list = None
            if val.startswith('[') and val.endswith(']'):
                meta[key] = [v.strip().strip('"').strip("'") for v in val[1:-1].split(',')]
            elif val:
                meta[key] = val
            else:
                meta[key] = None
    return meta, body


def _normalize_section_name(name: str) -> str:
    """Normaliza nomes de seção para lidar com variações de acentuação."""
    mappings = {
        'Visao Geral': 'Visão Geral',
        'Proposito de Negocio': 'Propósito de Negócio',
        'Colunas Principais': 'Colunas Principais',
        'Uso Tipico': 'Uso Típico',
        'Observacoes': 'Observações',
        'Referencias': 'Referências',
        'Relacionamentos': 'Relacionamentos',
    }
    return mappings.get(name, name)


def parse_md_body(body: str) -> dict:
    """Parseia o body do .md em seções estruturadas."""
    sections = {}
    current_section = None
    current_content = []

    for line in body.split('\n'):
        if line.startswith('## '):
            if current_section:
                sections[current_section] = '\n'.join(current_content).strip()
            # Remove emojis do nome da seção
            section_name = re.sub(r'^##\s*[^\w\s]*\s*', '', line).strip()
            section_name = _normalize_section_name(section_name)
            current_section = section_name
            current_content = []
        elif current_section:
            current_content.append(line)

    if current_section:
        sections[current_section] = '\n'.join(current_content).strip()

    return sections


def parse_columns_table(text: str) -> list[dict]:
    """Parseia a tabela Markdown de colunas. Detecta formato pelo header."""
    columns = []
    lines = text.split('\n')
    in_table = False
    col_map = {}  # maps header name -> index

    for line in lines:
        stripped = line.strip()

        # Detect header row
        if not in_table and stripped.startswith('|') and ('Coluna' in stripped or 'Column' in stripped or 'Tipo' in stripped):
            headers = [h.strip().lower() for h in stripped.split('|')[1:-1]]
            for i, h in enumerate(headers):
                # Normalize header names
                if h in ('#', 'num'): col_map['num'] = i
                elif h in ('coluna', 'column'): col_map['name'] = i
                elif h in ('tipo', 'type'): col_map['type'] = i
                elif h in ('nulo?', 'null?', 'nulo'): col_map['nullable'] = i
                elif h in ('categoria', 'category', 'cat'): col_map['category'] = i
                elif h in ('descrição', 'description', 'desc'): col_map['description'] = i
                elif h in ('fk', 'foreign key', 'chave'): col_map['fk'] = i
                elif h in ('confiança', 'confidence', 'conf'): col_map['confidence'] = i
            in_table = True
            continue

        if stripped.startswith('|---') or stripped.startswith('|--'):
            continue

        if in_table and stripped.startswith('|'):
            cells = [c.strip() for c in stripped.split('|')[1:-1]]
            if len(cells) < 3:
                continue

            def get(key, default=''):
                idx = col_map.get(key)
                if idx is not None and idx < len(cells):
                    return cells[idx].strip()
                return default

            # Extract FK from any cell that has wikilinks
            fk = None
            fk_idx = col_map.get('fk')
            if fk_idx is not None and fk_idx < len(cells):
                fk_raw = cells[fk_idx].strip()
                fk_match = re.search(r'\[\[([^\]]+)\]\]', fk_raw)
                if fk_match:
                    fk = fk_match.group(1)
                elif fk_raw and fk_raw not in ('—', '-', ''):
                    fk = fk_raw
            else:
                # No FK column — scan all cells for wikilinks
                for cell in cells:
                    fk_match = re.search(r'\[\[([^\]]+)\]\]', cell)
                    if fk_match:
                        fk = fk_match.group(1)
                        break

            # Extract confidence
            conf_str = get('confidence', '')
            conf_match = re.search(r'(\d+)%', conf_str)
            confidence = int(conf_match.group(1)) if conf_match else 0

            # Determine num
            num_str = get('num', '')
            num = int(num_str) if num_str.isdigit() else len(columns) + 1

            # Nullable
            nullable_str = get('nullable', 'NULL').upper()
            nullable = nullable_str != 'NOT NULL'

            # Category and description
            category = get('category', '')
            description = get('description', '')

            # If no description column found, try to detect from content
            if not description and not col_map.get('description'):
                # Maybe description is in a different position — check for longest text cell
                # Skip num, name, type, nullable which are short/technical
                known_indices = set(col_map.values())
                for i, cell in enumerate(cells):
                    if i not in known_indices and len(cell) > 20 and not re.match(r'^[A-Z_()0-9]+$', cell):
                        description = cell
                        break

            # Clean category from description if embedded (e.g., "PK. Identificador...")
            if not category and description:
                pk_match = re.match(r'^(PK|FK|WHO|DFF|Chave|Key)\.\s*(.*)', description)
                if pk_match:
                    category = pk_match.group(1)
                    description = pk_match.group(2)

            columns.append({
                'num': num,
                'name': get('name', f'COL_{num}'),
                'type': get('type', ''),
                'nullable': nullable,
                'category': category,
                'description': description,
                'fk': fk,
                'confidence': confidence,
            })
        elif in_table and not stripped.startswith('|'):
            in_table = False

    return columns


def parse_relationships(text: str) -> dict:
    """Parseia a seção de relacionamentos. Suporta múltiplos formatos."""
    parents = []
    children = []
    current = None
    all_rels = []  # fallback if no pai/filha sections

    for line in text.split('\n'):
        stripped = line.strip()

        # Detect section headers (only ### headings or plain text lines, NOT table rows)
        if not stripped.startswith('|'):
            lower = stripped.lower()
            if ('tabelas-pai' in lower or 'parent table' in lower or 'fk de entrada' in lower
                    or (stripped.startswith('###') and ('pai' in lower or 'parent' in lower))):
                current = parents
                continue
            elif ('tabelas-filha' in lower or 'child table' in lower or 'fk de sa' in lower
                    or (stripped.startswith('###') and ('filha' in lower or 'child' in lower))):
                current = children
                continue

        # Skip table headers and separators
        if stripped.startswith('|---') or stripped.startswith('|--'):
            continue
        if stripped.startswith('|') and ('Tabela' in stripped or 'Table' in stripped or 'Chave' in stripped):
            continue

        # Format 1: - [[table]] or **TABLE** — description (via `COLUMN`)
        if stripped.startswith('- '):
            table_match = re.search(r'\[\[([^\]]+)\]\]', stripped)
            if not table_match:
                # Try bold table name: **TABLE_NAME**
                bold_match = re.search(r'\*\*([A-Z][A-Z0-9_]+)\*\*', stripped)
                if bold_match:
                    table_match = bold_match
            col_match = re.search(r'`([A-Z_]+(?:\s*=\s*\'[^\']+\')?)`', stripped)
            # Description: text after — or after ]] or in parentheses
            desc = ''
            desc_match = re.search(r'\(([^)]+)\)', stripped)
            if desc_match:
                desc = desc_match.group(1)
            elif '—' in stripped:
                desc = stripped.split('—', 1)[1].strip()
                desc = re.sub(r'\[\[([^\]]+)\]\]', r'\1', desc)
                desc = re.sub(r'`[^`]+`', '', desc).strip()
                desc = re.sub(r'\(via\s*\)', '', desc).strip()
                desc = re.sub(r'^\s*[-—]\s*', '', desc).strip()

            if table_match:
                rel = {
                    'table': table_match.group(1),
                    'column': col_match.group(1) if col_match else '',
                    'desc': desc,
                }
                if current is not None:
                    current.append(rel)
                else:
                    all_rels.append(rel)
            continue

        # Format 2: | [[table]] | COLUMN | Type | Description |
        if stripped.startswith('|'):
            cells = [c.strip() for c in stripped.split('|')[1:-1]]
            if len(cells) >= 2:
                table_match = re.search(r'\[\[([^\]]+)\]\]', cells[0])
                if table_match:
                    col = cells[1] if len(cells) > 1 else ''
                    desc = cells[-1] if len(cells) > 2 else ''
                    # Clean desc
                    desc = re.sub(r'\[\[([^\]]+)\]\]', r'\1', desc)
                    rel = {
                        'table': table_match.group(1),
                        'column': col.strip(),
                        'desc': desc.strip(),
                    }
                    if current is not None:
                        current.append(rel)
                    else:
                        all_rels.append(rel)

    # If no pai/filha sections were found, put all rels in parents
    if not parents and not children and all_rels:
        parents = all_rels

    return {'parents': parents, 'children': children}


def parse_sql_section(text: str) -> tuple[list[dict], list[dict]]:
    """Parseia a seção SQL em queries e filtros. Suporta com/sem ### headings."""
    queries = []
    filters = []
    current_title = None
    current_code = []
    in_code = False
    in_filters = False
    query_counter = 0

    for line in text.split('\n'):
        stripped = line.strip()

        if stripped.startswith('### '):
            if current_code:
                query_counter += 1
                queries.append({'title': current_title or f'Query {query_counter}', 'code': '\n'.join(current_code).strip()})
                current_code = []
            title = re.sub(r'^###\s*', '', stripped)
            if 'filtro' in title.lower() or 'filter' in title.lower():
                in_filters = True
                current_title = None
            else:
                in_filters = False
                current_title = title
        elif stripped.startswith('```'):
            if in_code:
                in_code = False
                # If no title yet, try to extract from SQL comment
                if not current_title and current_code:
                    for cl in current_code:
                        comment_match = re.match(r'^--\s*(.+)', cl.strip())
                        if comment_match:
                            current_title = comment_match.group(1).strip()
                            break
            else:
                in_code = True
        elif in_code:
            current_code.append(line)
        elif in_filters and stripped.startswith('- '):
            code_match = re.search(r'`([^`]+)`', stripped)
            desc_match = re.search(r'[—-]\s*(.+)$', stripped)
            if code_match:
                filters.append({
                    'code': code_match.group(1),
                    'desc': desc_match.group(1).strip() if desc_match else '',
                })
        elif not in_code and not in_filters and stripped.startswith('- '):
            # Filters without ### heading
            code_match = re.search(r'`([^`]+)`', stripped)
            if code_match:
                desc_match = re.search(r'[—-]\s*(.+)$', stripped)
                filters.append({
                    'code': code_match.group(1),
                    'desc': desc_match.group(1).strip() if desc_match else '',
                })

    if current_code:
        query_counter += 1
        queries.append({'title': current_title or f'Query {query_counter}', 'code': '\n'.join(current_code).strip()})

    return queries, filters


def parse_notes(text: str) -> list[str]:
    """Parseia observações como lista de strings."""
    notes = []
    for line in text.split('\n'):
        stripped = line.strip()
        if stripped.startswith('- '):
            note = stripped[2:].strip()
            # Converter markdown bold/code para HTML
            note = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', note)
            note = re.sub(r'`([^`]+)`', r'<code>\1</code>', note)
            notes.append(note)
    return notes


def parse_business_purpose(text: str) -> list[str]:
    """Parseia propósito de negócio como lista ou parágrafos."""
    items = []
    for line in text.split('\n'):
        stripped = line.strip()
        if not stripped or stripped.startswith('---') or stripped.startswith('>') or stripped.startswith('#'):
            continue
        if stripped.startswith('- '):
            item = stripped[2:].strip()
            item = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', item)
            items.append(item)
        elif not items or not stripped.startswith('- '):
            # Paragraph text — treat each sentence or paragraph as an item
            clean = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', stripped)
            if clean and len(clean) > 10:
                items.append(clean)
    return items


# ============================================================
# i18n PARSER
# ============================================================

def parse_i18n(i18n_path: str) -> dict:
    """Parseia o .i18n.md e retorna {lang: {section: content}}."""
    if not os.path.exists(i18n_path):
        return {}

    with open(i18n_path, 'r', encoding='utf-8') as f:
        content = f.read()

    _, body = parse_front_matter(content)

    result = {}
    current_lang = None
    current_content = []

    for line in body.split('\n'):
        lang_match = re.match(r'<!--\s*LANG:\s*(\w+)\s*-->', line.strip())
        if lang_match:
            if current_lang:
                result[current_lang] = '\n'.join(current_content).strip()
            current_lang = lang_match.group(1)
            current_content = []
        elif line.strip().startswith('<!-- =='):
            continue
        elif current_lang:
            current_content.append(line)

    if current_lang:
        result[current_lang] = '\n'.join(current_content).strip()

    return result


def make_i18n_field(pt_value, i18n_data: dict, section_name: str, parser_fn=None):
    """Cria campo i18n {pt, en, es} a partir do valor PT e dos dados i18n."""
    result = {'pt': pt_value}

    for lang, content in i18n_data.items():
        sections = parse_md_body(content)
        # Tentar encontrar a seção equivalente
        for key, val in sections.items():
            if _section_matches(key, section_name):
                if parser_fn:
                    result[lang] = parser_fn(val)
                else:
                    result[lang] = val
                break

    return result


def _section_matches(key: str, target: str) -> bool:
    """Verifica se uma seção i18n corresponde à seção PT."""
    mappings = {
        'Visão Geral': ['Overview', 'Visión General'],
        'Propósito de Negócio': ['Business Purpose', 'Propósito de Negocio'],
        'Colunas Principais': ['Main Columns', 'Columnas Principales'],
        'Relacionamentos': ['Relationships', 'Relaciones'],
        'Uso Típico': ['Typical Use', 'Uso Típico'],
        'Observações': ['Notes', 'Observaciones'],
        'Referências': ['References', 'Referencias'],
    }
    if key == target:
        return True
    alternatives = mappings.get(target, [])
    return key in alternatives


# ============================================================
# VARIAVEIS
# ============================================================

def load_variaveis(variaveis_path: str) -> dict:
    """Lê variaveis.md e retorna mapa de variáveis."""
    defaults = {
        'EMPRESA': 'Empresa',
        'EMPRESA_SIGLA': '',
        'AREA': '',
        'TEAM': '',
        'AUTOR_NOME': '',
        'AUTOR_INICIAIS': '',
        'AUTOR_CARGO': '',
        'AUTOR_EMAIL': '',
    }
    if not os.path.exists(variaveis_path):
        return defaults

    with open(variaveis_path, 'r', encoding='utf-8') as f:
        content = f.read()

    for line in content.split('\n'):
        # Parse: | `{{VAR}}` | valor |
        match = re.match(r'\|\s*`\{\{(\w+)\}\}`\s*\|\s*(.+?)\s*\|', line)
        if match:
            key = match.group(1)
            val = match.group(2).strip()
            if key in defaults:
                defaults[key] = val

    return defaults


# ============================================================
# TABLE MAP
# ============================================================

def load_table_map(mappings_path: str) -> dict:
    """Carrega table-mappings.txt e retorna {TABLE_NAME: MODULE_CODE}."""
    if not os.path.exists(mappings_path):
        return {}

    table_map = {}
    current_module = None

    with open(mappings_path, 'r', encoding='utf-8') as f:
        for line in f:
            stripped = line.strip()
            # Detectar módulo: === GL — General Ledger ===
            mod_match = re.match(r'===\s*(\w+)\s*—', stripped)
            if mod_match:
                current_module = mod_match.group(1)
                continue
            # Detectar tabela: nome em uppercase sem espaços
            if current_module and re.match(r'^[A-Z][A-Z0-9_]+$', stripped):
                table_map[stripped] = current_module

    return table_map


# ============================================================
# BUILD
# ============================================================

def build_data(md_path: str, table_map: dict, variaveis: dict = None) -> dict:
    """Constrói o objeto DATA a partir do .md e .i18n.md."""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    meta, body = parse_front_matter(content)
    sections = parse_md_body(body)

    # i18n
    i18n_path = md_path.replace('.md', '.i18n.md')
    i18n_data = parse_i18n(i18n_path)

    # Parse i18n sections for each language
    i18n_sections = {}
    for lang, lang_content in i18n_data.items():
        i18n_sections[lang] = parse_md_body(lang_content)

    # Overview
    overview_pt = ''
    for key in ['Visão Geral', 'Overview']:
        if key in sections:
            text = sections[key]
            # Remover callouts e pegar só o parágrafo principal
            lines = [l for l in text.split('\n') if l.strip() and not l.strip().startswith('>') and not l.strip().startswith('---')]
            overview_pt = ' '.join(l.strip() for l in lines)
            overview_pt = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', overview_pt)
            break

    overview = {'pt': overview_pt}
    for lang, lang_secs in i18n_sections.items():
        for key in ['Overview', 'Visión General', 'Visão Geral']:
            if key in lang_secs:
                lines = [l for l in lang_secs[key].split('\n') if l.strip() and not l.strip().startswith('>') and not l.strip().startswith('---')]
                text = ' '.join(l.strip() for l in lines)
                text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
                overview[lang] = text
                break

    # Alert (from callout)
    alert = {'pt': ''}
    for key in ['Visão Geral', 'Overview']:
        if key in sections:
            callout_lines = [l for l in sections[key].split('\n') if l.strip().startswith('> ') and not l.strip().startswith('> [!')]
            if callout_lines:
                alert_text = ' '.join(l.strip()[2:].strip() for l in callout_lines)
                alert_text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', alert_text)
                alert_text = re.sub(r'`([^`]+)`', r'<code>\1</code>', alert_text)
                alert['pt'] = alert_text
            break
    for lang, lang_secs in i18n_sections.items():
        for key in ['Overview', 'Visión General', 'Visão Geral']:
            if key in lang_secs:
                callout_lines = [l for l in lang_secs[key].split('\n') if l.strip().startswith('> ') and not l.strip().startswith('> [!')]
                if callout_lines:
                    text = ' '.join(l.strip()[2:].strip() for l in callout_lines)
                    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
                    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
                    alert[lang] = text
                break

    # Business purpose
    bp_pt = []
    for key in ['Propósito de Negócio', 'Business Purpose']:
        if key in sections:
            bp_pt = parse_business_purpose(sections[key])
            break

    business_purpose = {'pt': bp_pt}
    for lang, lang_secs in i18n_sections.items():
        for key in ['Business Purpose', 'Propósito de Negocio', 'Propósito de Negócio']:
            if key in lang_secs:
                business_purpose[lang] = parse_business_purpose(lang_secs[key])
                break

    # Columns (PT)
    columns_pt = []
    for key in ['Colunas Principais', 'Main Columns']:
        if key in sections:
            columns_pt = parse_columns_table(sections[key])
            break

    # Columns i18n (merge descriptions and categories)
    columns_i18n = {}
    for lang, lang_secs in i18n_sections.items():
        for key in ['Main Columns', 'Columnas Principales', 'Colunas Principais']:
            if key in lang_secs:
                columns_i18n[lang] = parse_columns_table(lang_secs[key])
                break

    # Build columns with i18n
    columns = []
    for i, col in enumerate(columns_pt):
        col_data = {
            'num': col['num'],
            'name': col['name'],
            'type': col['type'],
            'nullable': col['nullable'],
            'category': {'pt': col['category']},
            'description': {'pt': col['description']},
            'fk': col['fk'],
            'confidence': col['confidence'],
        }
        for lang, lang_cols in columns_i18n.items():
            if i < len(lang_cols):
                col_data['category'][lang] = lang_cols[i]['category']
                col_data['description'][lang] = lang_cols[i]['description']
        columns.append(col_data)

    # Relationships (PT)
    rels_pt = {'parents': [], 'children': []}
    for key in ['Relacionamentos', 'Relationships']:
        if key in sections:
            rels_pt = parse_relationships(sections[key])
            break

    # Relationships i18n
    rels_i18n = {}
    for lang, lang_secs in i18n_sections.items():
        for key in ['Relationships', 'Relaciones', 'Relacionamentos']:
            if key in lang_secs:
                rels_i18n[lang] = parse_relationships(lang_secs[key])
                break

    # Merge relationship descriptions
    relationships = {'parents': [], 'children': []}
    for i, rel in enumerate(rels_pt['parents']):
        r = {'table': rel['table'], 'column': rel['column'], 'desc': {'pt': rel['desc']}}
        for lang, lang_rels in rels_i18n.items():
            if i < len(lang_rels.get('parents', [])):
                r['desc'][lang] = lang_rels['parents'][i]['desc']
        relationships['parents'].append(r)
    for i, rel in enumerate(rels_pt['children']):
        r = {'table': rel['table'], 'column': rel['column'], 'desc': {'pt': rel['desc']}}
        for lang, lang_rels in rels_i18n.items():
            if i < len(lang_rels.get('children', [])):
                r['desc'][lang] = lang_rels['children'][i]['desc']
        relationships['children'].append(r)

    # SQL
    sql_pt = []
    filters_pt = []
    for key in ['Uso Típico', 'Typical Use']:
        if key in sections:
            sql_pt, filters_pt = parse_sql_section(sections[key])
            break

    # SQL i18n (only titles and filter descriptions)
    sql_i18n = {}
    filters_i18n = {}
    for lang, lang_secs in i18n_sections.items():
        for key in ['Typical Use', 'Uso Típico']:
            if key in lang_secs:
                s, f = parse_sql_section(lang_secs[key])
                sql_i18n[lang] = s
                filters_i18n[lang] = f
                break

    sql = []
    for i, q in enumerate(sql_pt):
        sq = {'title': {'pt': q['title']}, 'code': q['code']}
        for lang, lang_sql in sql_i18n.items():
            if i < len(lang_sql):
                sq['title'][lang] = lang_sql[i]['title']
        sql.append(sq)

    filters = []
    for i, f in enumerate(filters_pt):
        fi = {'code': f['code'], 'desc': {'pt': f['desc']}}
        for lang, lang_filters in filters_i18n.items():
            if i < len(lang_filters):
                fi['desc'][lang] = lang_filters[i]['desc']
        filters.append(fi)

    # Notes
    notes_pt = []
    for key in ['Observações', 'Notes']:
        if key in sections:
            notes_pt = parse_notes(sections[key])
            break

    notes = {'pt': notes_pt}
    for lang, lang_secs in i18n_sections.items():
        for key in ['Notes', 'Observaciones', 'Observações']:
            if key in lang_secs:
                notes[lang] = parse_notes(lang_secs[key])
                break

    # Stats
    categories = set()
    total_conf = 0
    for col in columns_pt:
        categories.add(col['category'])
        total_conf += col['confidence']
    avg_conf = round(total_conf / len(columns_pt)) if columns_pt else 0

    # Determine module code from path
    md_parent = Path(md_path).parent.name  # "tables"
    module_code = Path(md_path).parent.parent.name  # "AR"

    # Subtitle
    subtitle_pt = meta.get('title', '').split('—')[-1].strip() if '—' in meta.get('title', '') else meta.get('title', '')
    subtitle = {'pt': subtitle_pt}
    # Simple translations for subtitle
    for lang, lang_secs in i18n_sections.items():
        for key in ['Overview', 'Visión General']:
            if key in lang_secs:
                # Just use the PT subtitle for now - translator already handled this
                subtitle[lang] = subtitle_pt
                break

    return {
        'meta': {
            'id': meta.get('id', ''),
            'doc_type': meta.get('doc_type', 'system-doc'),
            'table_name': columns_pt[0]['name'].split('_')[0] + '_' if columns_pt else meta.get('title', '').split('—')[0].strip() if '—' in meta.get('title', '') else meta.get('title', ''),
            'subtitle': subtitle,
            'system': meta.get('system', ''),
            'module': meta.get('module', ''),
            'module_code': module_code,
            'status': meta.get('status', 'draft'),
            'owner': meta.get('owner', ''),
            'created_at': meta.get('created_at', ''),
            'company': (variaveis or {}).get('EMPRESA', ''),
            'author_name': (variaveis or {}).get('AUTOR_NOME', ''),
            'author_initials': (variaveis or {}).get('AUTOR_INICIAIS', ''),
            'author_role': (variaveis or {}).get('AUTOR_CARGO', ''),
            'author_email': (variaveis or {}).get('AUTOR_EMAIL', ''),
            'area': (variaveis or {}).get('AREA', ''),
        },
        'overview': overview,
        'alert': alert if alert.get('pt') else None,
        'business_purpose': business_purpose,
        'columns': columns,
        'relationships': relationships,
        'sql': sql,
        'filters': filters,
        'notes': notes,
        'stats': {
            'avg_confidence': avg_conf,
            'categories': len(categories),
        },
        'table_map': table_map,
    }


def fix_table_name(data: dict, md_path: str):
    """Corrige o table_name a partir do nome do arquivo."""
    filename = Path(md_path).stem  # ar_adjustments_all
    data['meta']['table_name'] = filename.upper()


def load_i18n_items(md_path: str) -> list:
    """Carrega items do .i18n.json se existir."""
    json_path = md_path.replace('.md', '.i18n.json')
    if not os.path.exists(json_path):
        return []

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data.get('items', [])


def build_html(md_path: str, template_path: str, output_path: str, table_map: dict, variaveis: dict = None, mode: str = 'standalone', logo_dark: str = '', logo_light: str = ''):
    """Gera o HTML final."""
    data = build_data(md_path, table_map, variaveis)
    fix_table_name(data, md_path)

    # Load i18n items and inject into DATA for JS-side lookup
    i18n_items = load_i18n_items(md_path)
    data['i18n'] = i18n_items

    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    # Page title
    title = data['meta']['table_name'] + ' — Data Dictionary'
    template = template.replace('{{PAGE_TITLE}}', title)

    # Logos
    template = template.replace('{{LOGO_DARK_PATH}}', logo_dark)
    template = template.replace('{{LOGO_LIGHT_PATH}}', logo_light)

    # Data injection
    data_json = json.dumps(data, ensure_ascii=False, indent=2)
    template = template.replace('{{DATA_JSON}}', data_json)

    # Ensure output dir exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template)

    return output_path


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(description='Build HTML for system-doc (data dictionary)')
    parser.add_argument('input', nargs='?', help='Path to .md file')
    parser.add_argument('--batch', help='Path to folder with .md files (batch mode)')
    parser.add_argument('--mode', default='standalone', choices=['standalone', 'linked'])
    parser.add_argument('--assets-dir', default='', help='Assets directory (for linked mode)')
    parser.add_argument('--output-dir', default='', help='Output directory (default: docs/data-dictionary/{MODULE}/tables/)')
    parser.add_argument('--table-map', default='', help='Path to table-mappings.txt')
    parser.add_argument('--template', default='', help='Path to template HTML')
    parser.add_argument('--logo-dark', default='../../../../assets/logos/logo-dark.png', help='Logo dark path (relative to HTML)')
    parser.add_argument('--logo-light', default='../../../../assets/logos/logo-light.png', help='Logo light path (relative to HTML)')
    args = parser.parse_args()

    # Find project root (look for CLAUDE.md)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    if not (project_root / 'CLAUDE.md').exists():
        project_root = Path.cwd()

    # Template
    template_path = args.template or str(script_dir / 'template_system_doc.html')
    if not os.path.exists(template_path):
        print(f'ERROR: Template not found: {template_path}')
        sys.exit(1)

    # Table map
    table_map_path = args.table_map
    if not table_map_path:
        candidates = [
            project_root / 'src' / 'kb' / 'oracle-fusion-data-dictionary' / 'docs' / 'table-mappings.txt',
        ]
        for c in candidates:
            if c.exists():
                table_map_path = str(c)
                break

    table_map = load_table_map(table_map_path) if table_map_path else {}
    print(f'Table map: {len(table_map)} tables loaded')

    # Variaveis
    variaveis_path = project_root / 'docs' / 'assets' / 'variaveis.md'
    variaveis = load_variaveis(str(variaveis_path))
    print(f'Variaveis: {variaveis.get("EMPRESA", "?")} / {variaveis.get("AUTOR_NOME", "?")}')

    # Collect .md files
    md_files = []
    if args.batch:
        batch_dir = Path(args.batch)
        md_files = sorted(batch_dir.glob('*.md'))
        # Exclude .i18n.md
        md_files = [f for f in md_files if not f.name.endswith('.i18n.md')]
    elif args.input:
        md_files = [Path(args.input)]
    else:
        parser.print_help()
        sys.exit(1)

    print(f'Processing {len(md_files)} file(s)...')

    for md_file in md_files:
        md_path = str(md_file)

        # Determine output path
        if args.output_dir:
            output_dir = Path(args.output_dir)
        else:
            # Auto: docs/data-dictionary/{MODULE}/tables/
            module_code = md_file.parent.parent.name  # e.g., "AR"
            output_dir = project_root / 'docs' / 'fusion-kb' / 'data-dictionary' / module_code / 'tables'

        output_path = str(output_dir / (md_file.stem + '.html'))

        try:
            result = build_html(
                md_path=md_path,
                template_path=template_path,
                output_path=output_path,
                table_map=table_map,
                variaveis=variaveis,
                mode=args.mode,
                logo_dark=args.logo_dark,
                logo_light=args.logo_light,
            )
            print(f'  OK {md_file.name} -> {result}')
        except Exception as e:
            print(f'  FAIL {md_file.name} - ERROR: {e}')

    print('Done.')


if __name__ == '__main__':
    main()
