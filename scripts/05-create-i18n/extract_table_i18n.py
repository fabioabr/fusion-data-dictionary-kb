#!/usr/bin/env python3
"""
extract_json.py — Extrai frases traduzíveis de .md e gera .i18n.json (só BR)

Uso:
    python extract_json.py <arquivo.md>
    python extract_json.py --batch <pasta>

Gera {arquivo}.i18n.json na mesma pasta do .md, com items {id, br, en:null, es:null}
"""

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path


def md5_hash(content: str) -> str:
    return hashlib.md5(content.encode('utf-8')).hexdigest()


def extract_phrases(content: str) -> list[str]:
    """Extrai frases traduzíveis do conteúdo .md (sem front matter)."""

    # Remove front matter
    if content.startswith('---'):
        end = content.find('---', 3)
        if end != -1:
            content = content[end + 3:].strip()

    phrases = []
    seen = set()  # dedup
    in_code = False

    def add(text: str):
        """Adiciona frase se não for vazia, duplicada ou técnica."""
        text = text.strip()
        if not text or text in seen:
            return
        # Skip pure technical
        if re.match(r'^[A-Z_]+$', text):  # ADJUSTMENT_ID
            return
        if re.match(r'^(NUMBER|VARCHAR2|DATE|TIMESTAMP|NOT NULL|NULL|PK|FK|DFF|Multi-Org|WHO)(\(\d+\))?$', text):
            return
        if text in ('—', '-', '---', '|', '#'):
            return
        seen.add(text)
        phrases.append(text)

    for line in content.split('\n'):
        stripped = line.strip()

        # Toggle code blocks
        if stripped.startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            continue

        # Skip empty/separators
        if not stripped or stripped == '---':
            continue

        # Skip table header separators
        if stripped.startswith('|---') or stripped.startswith('| ---'):
            continue

        # H1 — skip (table name, not translatable)
        if stripped.startswith('# ') and not stripped.startswith('## '):
            continue

        # H2 — extract text without emoji
        if stripped.startswith('## '):
            text = re.sub(r'^##\s*', '', stripped)
            text = re.sub(r'^[^\w\s]+\s*', '', text).strip()  # remove leading emojis
            if text:
                add(text)
            continue

        # H3 — extract text
        if stripped.startswith('### '):
            text = re.sub(r'^###\s*', '', stripped).strip()
            if text:
                add(text)
            continue

        # Callout header: > [!note] Title
        if stripped.startswith('> [!'):
            match = re.match(r'>\s*\[!\w+\]\s*(.*)', stripped)
            if match and match.group(1).strip():
                add(match.group(1).strip())
            continue

        # Callout body: > text
        if stripped.startswith('> '):
            text = stripped[2:].strip()
            # Remove markdown formatting for cleaner text
            clean = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
            clean = re.sub(r'`[^`]+`', '', clean).strip()
            if clean and len(clean) > 2:
                # Use original text (with bold markers removed but keep content)
                plain = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
                plain = re.sub(r'`([^`]+)`', r'\1', plain).strip()
                add(plain)
            continue

        # Table rows
        if stripped.startswith('|'):
            cells = [c.strip() for c in stripped.split('|')[1:-1]]

            # Table header row — extract translatable headers
            if any(c in ('Coluna', 'Descrição', 'Categoria', 'Confiança', 'Nulo?',
                          'Tabela Relacionada', 'Chave', 'Tipo') for c in cells):
                for cell in cells:
                    cell = cell.strip()
                    # Skip # and purely technical headers
                    if cell and cell != '#' and not re.match(r'^[A-Z_]+$', cell):
                        add(cell)
                continue

            # Data rows — extract only text-description cells
            # Identify which cells are translatable (not technical)
            for cell in cells:
                cell = cell.strip()
                if not cell or cell == '—' or cell == '-':
                    continue
                # Skip column names (UPPERCASE_WITH_UNDERSCORES)
                if re.match(r'^[A-Z][A-Z0-9_]+$', cell):
                    continue
                # Skip types
                if re.match(r'^(NUMBER|VARCHAR2|DATE|TIMESTAMP)', cell):
                    continue
                # Skip NULL/NOT NULL
                if cell in ('NULL', 'NOT NULL'):
                    continue
                # Skip confidence badges
                if re.match(r'^🟢|🟡|🔴', cell):
                    continue
                # Skip wikilinks alone
                if re.match(r'^\[\[[^\]]+\]\]$', cell):
                    continue
                # Skip pure numbers
                if re.match(r'^\d+$', cell):
                    continue
                # Clean wikilinks from text
                clean = re.sub(r'\[\[([^\]]+)\]\]', r'\1', cell)
                # Clean markdown
                clean = re.sub(r'\*\*([^*]+)\*\*', r'\1', clean)
                clean = re.sub(r'`([^`]+)`', r'\1', clean)
                clean = clean.strip()
                if clean and len(clean) > 1:
                    # Check if it's a description or category (translatable text)
                    # Technical labels that should still be translated
                    add(clean)
            continue

        # List items: - text or - **Label:** text
        if stripped.startswith('- '):
            item = stripped[2:].strip()

            # Filter: - `CODE` — description
            code_desc = re.match(r'^`[^`]+`\s*[—-]\s*(.+)$', item)
            if code_desc:
                add(code_desc.group(1).strip())
                continue

            # Filter: - [[wikilink]] — via `COL` (description)
            wiki_desc = re.match(r'^\[\[[^\]]+\]\]\s*[—-]\s*via\s*`[^`]+`\s*\(([^)]+)\)', item)
            if wiki_desc:
                add(wiki_desc.group(1).strip())
                continue

            # Filter: - [[wikilink]] — description (any format)
            wiki_general = re.match(r'^\*{0,2}\[\[[^\]]+\]\]\*{0,2}\s*[—-]\s*(.+)$', item)
            if wiki_general:
                desc = wiki_general.group(1).strip()
                # Clean out via `COL` part, keep the description text
                desc = re.sub(r'\(.*?via\s*`[^`]+`\)', '', desc)
                desc = re.sub(r'via\s*`[^`]+`', '', desc)
                desc = re.sub(r'\[\[([^\]]+)\]\]', r'\1', desc)
                desc = re.sub(r'`[^`]+`', '', desc)
                desc = re.sub(r'\(N:1\)|\(1:N\)|\(1:1\)|\(N:M\)', '', desc)
                desc = desc.strip().strip('()').strip('—-').strip()
                if desc and len(desc) > 3:
                    add(desc)
                continue

            # Filter: - **Label:** description
            label_desc = re.match(r'^\*\*([^*]+)\*\*[:\s]+(.+)$', item)
            if label_desc:
                add(label_desc.group(2).strip())
                continue

            # Regular list item — clean and add
            clean = re.sub(r'\*\*([^*]+)\*\*', r'\1', item)
            clean = re.sub(r'`([^`]+)`', r'\1', clean)
            clean = re.sub(r'\[\[([^\]]+)\]\]', r'\1', clean)
            clean = clean.strip()
            if clean and len(clean) > 2:
                add(clean)
            continue

        # Paragraphs
        if not stripped.startswith('|') and not stripped.startswith('['):
            clean = re.sub(r'\*\*([^*]+)\*\*', r'\1', stripped)
            clean = re.sub(r'`([^`]+)`', r'\1', clean)
            clean = re.sub(r'\[\[([^\]]+)\]\]', r'\1', clean)
            clean = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', clean)  # markdown links
            clean = clean.strip()
            if clean and len(clean) > 2:
                add(clean)

    return phrases


def generate_i18n_json(md_path: str, force: bool = False) -> str:
    """Gera .i18n.json para um .md. Retorna path ou status."""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    file_hash = md5_hash(content)
    json_path = md_path.replace('.md', '.i18n.json')

    # Check cache
    if os.path.exists(json_path) and not force:
        with open(json_path, 'r', encoding='utf-8') as f:
            existing = json.load(f)
        if existing.get('source_hash') == file_hash:
            return 'CACHED'

    # Extract
    phrases = extract_phrases(content)
    if not phrases:
        return 'SKIP (no translatable text)'

    # Build JSON
    data = {
        "source": Path(md_path).name,
        "source_hash": file_hash,
        "translated_at": None,
        "items": [
            {"id": i + 1, "br": phrase, "en": None, "es": None}
            for i, phrase in enumerate(phrases)
        ]
    }

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return json_path


def main():
    parser = argparse.ArgumentParser(description='Extract translatable phrases from .md to .i18n.json')
    parser.add_argument('input', nargs='?', help='Path to .md file')
    parser.add_argument('--batch', help='Path to folder with .md files')
    parser.add_argument('--force', action='store_true', help='Regenerate even if cached')
    args = parser.parse_args()

    md_files = []
    if args.batch:
        md_files = sorted(Path(args.batch).glob('*.md'))
        md_files = [f for f in md_files if not f.name.endswith('.i18n.md')]
    elif args.input:
        md_files = [Path(args.input)]
    else:
        parser.print_help()
        sys.exit(1)

    print(f'Extracting from {len(md_files)} file(s)...')

    ok = 0
    cached = 0
    for i, f in enumerate(md_files):
        result = generate_i18n_json(str(f), args.force)
        if result == 'CACHED':
            cached += 1
        elif result.startswith('SKIP'):
            cached += 1
        else:
            ok += 1
            print(f'  [{i+1}/{len(md_files)}] {f.name} -> {Path(result).name} ({len(extract_phrases(open(str(f), encoding="utf-8").read()))} items)')

    print(f'\nDone. Extracted: {ok}, Cached: {cached}')


if __name__ == '__main__':
    main()
