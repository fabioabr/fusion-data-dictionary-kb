#!/usr/bin/env python3
"""
build_portal.py — Atualiza o portal principal (docs/index.html) com contadores atuais

Uso:
    python build_portal.py
    python build_portal.py --config Pipeline/config/modules.json
    python build_portal.py --dry-run

Varre docs/data-dictionary/ para contar tabelas e PVOs por módulo,
e atualiza os contadores e cards no docs/index.html existente.
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path


def find_project_root() -> Path:
    """Encontra a raiz do projeto subindo até achar Pipeline/config/modules.json."""
    current = Path(__file__).resolve().parent
    for _ in range(10):
        if (current / 'Pipeline' / 'config' / 'modules.json').exists():
            return current
        if (current / 'docs' / 'index.html').exists():
            return current
        current = current.parent
    # Fallback: dois níveis acima (Pipeline/10-build-portal/)
    return Path(__file__).resolve().parent.parent.parent


def count_html_files(directory: Path) -> int:
    """Conta arquivos .html em um diretório (não recursivo)."""
    if not directory.is_dir():
        return 0
    return len(list(directory.glob('*.html')))


def scan_modules(output_base: Path) -> dict:
    """Varre diretórios de módulos e conta tabelas/PVOs."""
    stats = {}
    if not output_base.is_dir():
        print(f'Aviso: diretório de saída não encontrado: {output_base}')
        return stats

    for module_dir in sorted(output_base.iterdir()):
        if not module_dir.is_dir():
            continue
        module_code = module_dir.name
        tables_count = count_html_files(module_dir / 'tables')
        pvos_count = count_html_files(module_dir / 'pvos')
        # Excluir index.html da contagem de tabelas se estiver na raiz
        if tables_count > 0 or pvos_count > 0:
            stats[module_code] = {
                'tables': tables_count,
                'pvos': pvos_count,
                'total': tables_count + pvos_count
            }
    return stats


def update_portal_stats(html: str, total_tables: int, total_pvos: int,
                        module_count: int) -> str:
    """Atualiza os contadores de estatísticas no HTML do portal."""

    # Padrão: procurar data-stat ou spans com IDs conhecidos
    # Atualizar total de tabelas
    html = re.sub(
        r'(id=["\']stat-tables["\'][^>]*>)\s*[\d.]+',
        rf'\g<1>{total_tables}',
        html
    )
    html = re.sub(
        r'(data-stat=["\']tables["\'][^>]*>)\s*[\d.]+',
        rf'\g<1>{total_tables}',
        html
    )

    # Atualizar total de PVOs
    html = re.sub(
        r'(id=["\']stat-pvos["\'][^>]*>)\s*[\d.]+',
        rf'\g<1>{total_pvos}',
        html
    )
    html = re.sub(
        r'(data-stat=["\']pvos["\'][^>]*>)\s*[\d.]+',
        rf'\g<1>{total_pvos}',
        html
    )

    # Atualizar total de módulos
    html = re.sub(
        r'(id=["\']stat-modules["\'][^>]*>)\s*[\d.]+',
        rf'\g<1>{module_count}',
        html
    )
    html = re.sub(
        r'(data-stat=["\']modules["\'][^>]*>)\s*[\d.]+',
        rf'\g<1>{module_count}',
        html
    )

    # Atualizar total geral (tabelas + PVOs)
    total = total_tables + total_pvos
    html = re.sub(
        r'(id=["\']stat-total["\'][^>]*>)\s*[\d.]+',
        rf'\g<1>{total}',
        html
    )
    html = re.sub(
        r'(data-stat=["\']total["\'][^>]*>)\s*[\d.]+',
        rf'\g<1>{total}',
        html
    )

    return html


def update_module_cards(html: str, module_stats: dict,
                        modules_config: dict) -> str:
    """Atualiza os cards de módulos no HTML com contadores corretos."""

    for code, stats in module_stats.items():
        tables = stats['tables']
        pvos = stats['pvos']

        # Atualizar contadores dentro de cards de módulo
        # Padrão: data-module="GL" ... <span class="table-count">N</span>
        pattern = rf'(data-module=["\']{code}["\'])'
        if re.search(pattern, html):
            # Procurar e atualizar table-count dentro do bloco do módulo
            # Abordagem: encontrar o bloco do card e atualizar contadores nele
            card_pattern = rf'(data-module=["\']{code}["\'].*?)(class=["\']table-count["\'][^>]*>)\s*\d+'
            html = re.sub(
                card_pattern,
                rf'\g<1>\g<2>{tables}',
                html,
                flags=re.DOTALL
            )
            card_pattern = rf'(data-module=["\']{code}["\'].*?)(class=["\']pvo-count["\'][^>]*>)\s*\d+'
            html = re.sub(
                card_pattern,
                rf'\g<1>\g<2>{pvos}',
                html,
                flags=re.DOTALL
            )

    return html


def update_js_module_data(html: str, module_stats: dict,
                          modules_config: dict) -> str:
    """Atualiza dados de módulos no JavaScript embutido, se existirem."""

    # Procurar bloco moduleData ou modules no JS
    # Padrão: const moduleData = { ... }
    # Atualizar contadores individuais
    for code, stats in module_stats.items():
        # Padrão: "GL": { ... tables: N, pvos: N ...}
        pattern = rf'(["\']?{code}["\']?\s*:\s*\{{[^}}]*?tables\s*:\s*)\d+'
        html = re.sub(pattern, rf'\g<1>{stats["tables"]}', html)
        pattern = rf'(["\']?{code}["\']?\s*:\s*\{{[^}}]*?pvos\s*:\s*)\d+'
        html = re.sub(pattern, rf'\g<1>{stats["pvos"]}', html)

    return html


def main():
    parser = argparse.ArgumentParser(
        description='Atualiza portal principal com contadores de tabelas/PVOs'
    )
    parser.add_argument('--config', default=None,
                        help='Caminho para modules.json')
    parser.add_argument('--dry-run', action='store_true',
                        help='Apenas mostra contagens, não altera arquivos')
    parser.add_argument('--portal', default=None,
                        help='Caminho para docs/index.html')
    args = parser.parse_args()

    # Encontrar raiz do projeto
    root = find_project_root()
    print(f'Raiz do projeto: {root}')

    # Carregar configuração
    config_path = args.config or str(root / 'Pipeline' / 'config' / 'modules.json')
    if not os.path.exists(config_path):
        print(f'Erro: configuração não encontrada: {config_path}')
        sys.exit(1)

    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    modules_config = config.get('modules', {})
    output_base = root / config.get('output_base', 'docs/data-dictionary')

    # Escanear módulos
    print(f'Escaneando: {output_base}')
    module_stats = scan_modules(output_base)

    if not module_stats:
        print('Nenhum módulo com HTMLs encontrado.')
        sys.exit(0)

    # Calcular totais
    total_tables = sum(s['tables'] for s in module_stats.values())
    total_pvos = sum(s['pvos'] for s in module_stats.values())
    module_count = len(module_stats)

    # Exibir resumo
    print(f'\n{"Módulo":<8} {"Tabelas":>8} {"PVOs":>8} {"Total":>8}')
    print('-' * 36)
    for code in sorted(module_stats.keys()):
        s = module_stats[code]
        name = modules_config.get(code, {}).get('name', code)
        print(f'{code:<8} {s["tables"]:>8} {s["pvos"]:>8} {s["total"]:>8}  ({name})')
    print('-' * 36)
    print(f'{"TOTAL":<8} {total_tables:>8} {total_pvos:>8} {total_tables + total_pvos:>8}')
    print(f'Módulos ativos: {module_count}')

    if args.dry_run:
        print('\n(dry-run: nenhum arquivo alterado)')
        return

    # Ler portal HTML
    portal_path = args.portal or str(root / 'docs' / 'index.html')
    if not os.path.exists(portal_path):
        print(f'\nErro: portal não encontrado: {portal_path}')
        sys.exit(1)

    with open(portal_path, 'r', encoding='utf-8') as f:
        html = f.read()

    original = html

    # Aplicar atualizações
    html = update_portal_stats(html, total_tables, total_pvos, module_count)
    html = update_module_cards(html, module_stats, modules_config)
    html = update_js_module_data(html, module_stats, modules_config)

    if html == original:
        print('\nNenhuma alteração necessária no portal.')
        return

    # Salvar
    with open(portal_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'\nPortal atualizado: {portal_path}')


if __name__ == '__main__':
    main()
