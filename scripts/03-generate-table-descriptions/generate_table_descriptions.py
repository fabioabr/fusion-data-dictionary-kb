#!/usr/bin/env python3
"""
generate_table_descriptions.py — Enriquece .md de tabelas via Anthropic API (Claude)

Lê esqueletos de tabela em src/kb/.../docs/{MOD}/tables/*.md e envia à API do Claude
para gerar descrições ricas: visão geral, propósito de negócio, colunas detalhadas,
relacionamentos e exemplos SQL.

Uso:
    python generate_table_descriptions.py --module GL
    python generate_table_descriptions.py --module GL --table gl_balances
    python generate_table_descriptions.py --module GL --force
    python generate_table_descriptions.py --module GL --dry-run
    python generate_table_descriptions.py --module GL --batch-size 5

Dependências:
    pip install anthropic
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("ERRO: SDK Anthropic não encontrado. Instale com: pip install anthropic")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Configuração
# ---------------------------------------------------------------------------

MODEL = "claude-sonnet-4-20250514"
# Pricing Sonnet: input $3/M tokens, output $15/M tokens
COST_INPUT_PER_M = 3.0
COST_OUTPUT_PER_M = 15.0
API_DELAY_SECONDS = 1.0
MAX_TOKENS = 8192

PLACEHOLDER_MARKERS = [
    "(a ser preenchido na etapa 03)",
    "(a ser preenchido)",
    "(to be filled)",
    "(pendente)",
]

MODULE_NAMES = {
    "GL": "General Ledger",
    "AP": "Accounts Payable",
    "AR": "Accounts Receivable",
    "PO": "Procurement",
    "HCM": "Human Capital Management",
    "SCM": "Supply Chain Management",
    "FIN": "Financials Shared",
    "PRJ": "Projects",
    "GRC": "Governance Risk Compliance",
    "OKC": "Contracts",
    "GMS": "Grants Management",
    "SRP": "Sales Compensation",
    "PSC": "Public Sector",
    "STU": "Student",
    "HED": "Higher Education",
    "MFG": "Manufacturing",
}

CATEGORY_VALUES = [
    "PK", "FK", "Financeiro", "Período", "Classificação",
    "Auditoria", "Controle", "Status", "Configuração",
    "Identificação", "Referência", "Conversão", "DFF", "Sistema",
    "Data", "Flag", "Versionamento",
]


# ---------------------------------------------------------------------------
# Parsing do .md existente
# ---------------------------------------------------------------------------

def parse_front_matter(content: str) -> tuple[dict, str]:
    """Separa front matter YAML do corpo Markdown. Retorna (fm_dict, body)."""
    if not content.startswith("---"):
        return {}, content

    end = content.find("---", 3)
    if end == -1:
        return {}, content

    fm_raw = content[3:end].strip()
    body = content[end + 3:].strip()

    # Parse YAML simples (sem dependência de PyYAML)
    fm = {}
    current_key = None
    current_list = None
    for line in fm_raw.split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        # Lista item
        if stripped.startswith("- ") and current_key:
            if current_list is None:
                current_list = []
                fm[current_key] = current_list
            current_list.append(stripped[2:].strip().strip('"').strip("'"))
            continue

        # Key: value
        if ":" in stripped:
            parts = stripped.split(":", 1)
            key = parts[0].strip()
            val = parts[1].strip().strip('"').strip("'")
            current_key = key
            current_list = None
            if val:
                fm[key] = val
            # se val vazio, pode ser início de lista — aguardamos
            continue

    return fm, body


def extract_columns_from_table(body: str) -> list[dict]:
    """Extrai colunas da tabela Markdown no corpo do .md."""
    columns = []
    in_table = False

    for line in body.split("\n"):
        stripped = line.strip()
        # Detecta header da tabela de colunas
        if "| # |" in stripped and "Coluna" in stripped:
            in_table = True
            continue
        if in_table and stripped.startswith("|---"):
            continue
        if in_table and stripped.startswith("|"):
            cells = [c.strip() for c in stripped.split("|")]
            # Remove cells vazias das bordas
            cells = [c for c in cells if c != ""]
            if len(cells) >= 6:
                col = {
                    "num": cells[0],
                    "name": cells[1],
                    "type": cells[2] if len(cells) > 2 else "",
                    "nullable": cells[3] if len(cells) > 3 else "",
                    "category": cells[4] if len(cells) > 4 else "",
                    "description": cells[5] if len(cells) > 5 else "",
                    "fk": cells[6] if len(cells) > 6 else "—",
                    "confidence": cells[7] if len(cells) > 7 else "",
                }
                columns.append(col)
        elif in_table and not stripped.startswith("|"):
            in_table = False

    return columns


def needs_enrichment(content: str, force: bool = False) -> bool:
    """Verifica se o .md precisa de enriquecimento."""
    if force:
        return True

    lower = content.lower()

    # Checa marcadores de placeholder
    for marker in PLACEHOLDER_MARKERS:
        if marker.lower() in lower:
            return True

    # Checa se falta seção de Uso Típico (sem SQL examples)
    if "## 📎 uso típico" not in lower and "## uso típico" not in lower:
        return True

    # Checa se falta seção de Relacionamentos
    if "## 🔗 relacionamentos" not in lower and "## relacionamentos" not in lower:
        return True

    return False


# ---------------------------------------------------------------------------
# Prompt para a API
# ---------------------------------------------------------------------------

def build_system_prompt(module_code: str) -> str:
    """Monta o system prompt para o Claude."""
    module_name = MODULE_NAMES.get(module_code, module_code)
    categories_str = ", ".join(CATEGORY_VALUES)

    return f"""Você é um especialista em Oracle Fusion Cloud ERP, especificamente no módulo {module_name} ({module_code}).

Seu papel é enriquecer documentação de dicionário de dados de tabelas Oracle Fusion para uma base de conhecimento corporativa (Knowledge Base).

## Contexto
- Sistema: Oracle Fusion Cloud ERP (SaaS) — Release 13/25A
- Módulo: {module_name} ({module_code})
- Idioma: pt-BR (português brasileiro)
- Formato: Obsidian Markdown com [[wikilinks]]

## Regras de Escrita
- Toda descrição em pt-BR
- Usar [[wikilinks]] ao referenciar outras tabelas (ex: [[gl_ledgers]])
- Nomes de colunas sempre em MAIÚSCULAS
- Nomes de tabelas sempre em lowercase com [[wikilinks]]
- Termos técnicos Oracle podem ser mantidos em inglês (ex: ledger, journal, CCID)

## Naming Conventions Oracle Fusion
- *_ID → geralmente FK ou PK (NUMBER(18))
- *_DATE → data (DATE ou TIMESTAMP)
- *_FLAG → booleano (VARCHAR2(1): Y/N)
- *_CODE → código de classificação
- *_NUM ou *_NUMBER → número sequencial ou identificador
- *_NAME → nome descritivo
- *_STATUS → status do registro
- CREATED_BY, CREATION_DATE, LAST_UPDATED_BY, LAST_UPDATE_DATE → colunas de auditoria padrão WHO
- OBJECT_VERSION_NUMBER → controle de concorrência otimista
- ATTRIBUTE_CATEGORY, ATTRIBUTE1-15 → Descriptive Flexfield (DFF)
- *_TL → Translation table (multi-idioma)
- *_B → Base table
- *_VL → View Language (join B + TL)
- *_ALL → Multi-org (todas as business units)
- *_F → Date-effective (EFFECTIVE_START_DATE, EFFECTIVE_END_DATE)

## Categorias Válidas para Colunas
{categories_str}

## Formato de Resposta
Retorne um JSON válido (sem markdown code fences) com a seguinte estrutura:

{{
  "overview": "Descrição de 2-4 frases sobre o propósito da tabela no contexto do módulo. Explicar o que armazena e por que é importante.",
  "overview_note": "Nota adicional opcional (callout [!note]) — ex: volumetria, sufixo _ALL, etc. Null se não aplicável.",
  "business_purpose": [
    "Caso de uso 1: Descrição breve",
    "Caso de uso 2: Descrição breve"
  ],
  "columns": [
    {{
      "name": "COLUMN_NAME",
      "type": "NUMBER(18)",
      "nullable": "NOT NULL",
      "category": "PK",
      "description": "Descrição em pt-BR da coluna",
      "fk_table": "nome_tabela_referenciada ou null",
      "confidence": 95
    }}
  ],
  "relationships": {{
    "parents": [
      {{"table": "nome_tabela", "column": "COLUMN_NAME", "description": "Descrição da relação"}}
    ],
    "children": [
      {{"table": "nome_tabela", "column": "COLUMN_NAME", "description": "Descrição da relação"}}
    ]
  }},
  "sql_examples": [
    {{
      "title": "Título do exemplo",
      "code": "SELECT ... FROM ...",
      "filters": ["Descrição do filtro 1", "Descrição do filtro 2"]
    }}
  ],
  "observations": [
    "Observação 1 sobre a tabela",
    "Observação 2 sobre a tabela"
  ],
  "oracle_doc_url": "https://docs.oracle.com/en/cloud/saas/..."
}}

## Regras para Confiança
- 95-100%: Coluna bem documentada na documentação oficial Oracle, nome e tipo confirmados
- 75-90%: Coluna inferida por naming convention Oracle, alta probabilidade de estar correta
- 50-70%: Coluna incerta, pode variar entre releases ou não existir no ambiente específico

## Regras para FK
- Se uma coluna *_ID referencia outra tabela conhecida, indicar em fk_table (lowercase, sem [[]])
- Colunas de auditoria (CREATED_BY etc.) não têm FK
- Na dúvida, colocar null"""


def build_user_prompt(table_name: str, module_code: str, columns: list[dict], existing_body: str) -> str:
    """Monta o user prompt com os dados da tabela."""
    module_name = MODULE_NAMES.get(module_code, module_code)

    columns_text = ""
    for col in columns:
        columns_text += f"  - {col['name']} ({col['type']}, {col['nullable']})\n"

    if not columns_text:
        # Tentar extrair colunas do body se a tabela não foi parseada
        columns_text = "  (não disponível — infira a partir do nome da tabela e module Oracle Fusion)\n"

    prompt = f"""Enriqueça a documentação da tabela Oracle Fusion Cloud abaixo.

**Tabela:** {table_name}
**Módulo:** {module_name} ({module_code})

**Colunas existentes no esqueleto:**
{columns_text}

**Conteúdo atual do .md (para contexto):**
```
{existing_body[:3000]}
```

Retorne APENAS o JSON conforme a estrutura definida no system prompt.
- Mantenha TODAS as colunas listadas acima, enriquecendo a descrição de cada uma.
- Adicione pelo menos 2 exemplos SQL práticos e relevantes para o contexto do módulo.
- Identifique relacionamentos pai/filho com outras tabelas do módulo.
- As descrições devem ser em pt-BR, técnicas mas acessíveis.
"""
    return prompt


# ---------------------------------------------------------------------------
# Reconstrução do .md
# ---------------------------------------------------------------------------

def rebuild_md(fm_raw: str, table_name: str, data: dict, module_code: str) -> str:
    """Reconstrói o .md completo com os dados enriquecidos."""
    module_name = MODULE_NAMES.get(module_code, module_code)
    lines = []

    # Front matter (preservar original)
    lines.append(fm_raw)
    lines.append("")

    # Título
    lines.append(f"# {table_name}")
    lines.append("")

    # Visão Geral
    lines.append("## 📌 Visão Geral")
    lines.append("")
    lines.append(data.get("overview", ""))
    lines.append("")

    note = data.get("overview_note")
    if note:
        lines.append(f"> [!note] Nota")
        lines.append(f"> {note}")
        lines.append("")

    lines.append("---")
    lines.append("")

    # Propósito de Negócio
    lines.append("## 🧠 Propósito de Negócio")
    lines.append("")
    lines.append("Esta tabela é utilizada nos seguintes processos:")
    lines.append("")
    for purpose in data.get("business_purpose", []):
        # Se já tem formato "**Titulo:** desc", manter; senão formatar
        if purpose.startswith("**"):
            lines.append(f"- {purpose}")
        elif ":" in purpose:
            parts = purpose.split(":", 1)
            lines.append(f"- **{parts[0].strip()}:** {parts[1].strip()}")
        else:
            lines.append(f"- {purpose}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Colunas
    lines.append("## ⚙️ Colunas Principais")
    lines.append("")
    lines.append("> [!tip] Confiança")
    lines.append("> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).")
    lines.append("> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.")
    lines.append("> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.")
    lines.append("> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.")
    lines.append("")

    lines.append("| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |")
    lines.append("|---|--------|------|-------|-----------|-----------|-----|-----------|")

    for i, col in enumerate(data.get("columns", []), 1):
        name = col.get("name", "")
        col_type = col.get("type", "")
        nullable = col.get("nullable", "NULL")
        category = col.get("category", "")
        desc = col.get("description", "")
        fk_table = col.get("fk_table")
        confidence = col.get("confidence", 75)

        # Formatar FK
        if fk_table:
            fk_str = f"[[{fk_table}]]"
        else:
            fk_str = "—"

        # Formatar confiança
        if confidence >= 81:
            conf_str = f"🟢 {confidence}%"
        elif confidence >= 51:
            conf_str = f"🟡 {confidence}%"
        else:
            conf_str = f"🔴 {confidence}%"

        lines.append(f"| {i} | {name} | {col_type} | {nullable} | {category} | {desc} | {fk_str} | {conf_str} |")

    lines.append("")
    lines.append("---")
    lines.append("")

    # Relacionamentos
    lines.append("## 🔗 Relacionamentos")
    lines.append("")

    rels = data.get("relationships", {})
    parents = rels.get("parents", [])
    children = rels.get("children", [])

    lines.append("### Tabelas-pai (FK de entrada)")
    if parents:
        for p in parents:
            lines.append(f"- [[{p['table']}]] — via `{p['column']}` ({p.get('description', '')})")
    else:
        lines.append("- Nenhuma FK identificada.")
    lines.append("")

    lines.append("### Tabelas-filha (FK de saída)")
    if children:
        for c in children:
            lines.append(f"- [[{c['table']}]] — via `{c['column']}` ({c.get('description', '')})")
    else:
        lines.append("- Nenhuma FK direta identificada.")
    lines.append("")

    lines.append("---")
    lines.append("")

    # Uso Típico (SQL Examples)
    lines.append("## 📎 Uso Típico")
    lines.append("")

    sql_examples = data.get("sql_examples", [])
    for ex in sql_examples:
        lines.append(f"### {ex.get('title', 'Exemplo SQL')}")
        lines.append("```sql")
        lines.append(ex.get("code", ""))
        lines.append("```")
        lines.append("")

        filters = ex.get("filters", [])
        if filters:
            lines.append("### Filtros comuns")
            for f in filters:
                lines.append(f"- {f}")
            lines.append("")

    lines.append("---")
    lines.append("")

    # Observações
    observations = data.get("observations", [])
    if observations:
        lines.append("## 🔒 Observações")
        lines.append("")
        for obs in observations:
            lines.append(f"- {obs}")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Referências
    lines.append("## 📚 Referências")
    lines.append("")

    oracle_url = data.get("oracle_doc_url")
    if oracle_url and oracle_url != "null":
        doc_label = table_name.upper()
        lines.append(f"- [Oracle Docs — {doc_label}]({oracle_url})")

    module_dict_link = f"{module_code.lower()}-module-data-dictionary"
    lines.append(f"- [[{module_dict_link}]] — Dossiê do módulo {module_code}")

    return "\n".join(lines) + "\n"


def extract_front_matter_raw(content: str) -> str:
    """Extrai o front matter bruto (incluindo delimitadores ---)."""
    if not content.startswith("---"):
        return ""
    end = content.find("---", 3)
    if end == -1:
        return ""
    return content[: end + 3]


# ---------------------------------------------------------------------------
# API Anthropic
# ---------------------------------------------------------------------------

def call_anthropic(client: anthropic.Anthropic, system_prompt: str, user_prompt: str) -> tuple[dict | None, int, int]:
    """Chama a API Anthropic e retorna (json_parsed, input_tokens, output_tokens)."""
    message = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=system_prompt,
        messages=[
            {"role": "user", "content": user_prompt}
        ],
    )

    input_tokens = message.usage.input_tokens
    output_tokens = message.usage.output_tokens

    # Extrair texto da resposta
    raw_text = ""
    for block in message.content:
        if block.type == "text":
            raw_text += block.text

    # Limpar possíveis code fences
    raw_text = raw_text.strip()
    if raw_text.startswith("```json"):
        raw_text = raw_text[7:]
    elif raw_text.startswith("```"):
        raw_text = raw_text[3:]
    if raw_text.endswith("```"):
        raw_text = raw_text[:-3]
    raw_text = raw_text.strip()

    try:
        parsed = json.loads(raw_text)
        return parsed, input_tokens, output_tokens
    except json.JSONDecodeError as e:
        print(f"    ERRO ao parsear JSON da resposta: {e}")
        print(f"    Primeiros 500 chars: {raw_text[:500]}")
        return None, input_tokens, output_tokens


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # Forçar UTF-8 no stdout (Windows usa cp1252 por padrão)
    if sys.stdout.encoding != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if sys.stderr.encoding != "utf-8":
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(
        description="Enriquece .md de tabelas Oracle Fusion via Anthropic API (Claude)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  python generate_table_descriptions.py --module GL
  python generate_table_descriptions.py --module GL --table gl_balances
  python generate_table_descriptions.py --module GL --force
  python generate_table_descriptions.py --module GL --dry-run
  python generate_table_descriptions.py --module GL --batch-size 5
        """,
    )
    parser.add_argument("--module", required=True, help="Código do módulo (GL, AP, AR, PO, HCM, ...)")
    parser.add_argument("--table", help="Nome de uma tabela específica (sem extensão)")
    parser.add_argument("--force", action="store_true", help="Re-gerar mesmo se já enriquecido")
    parser.add_argument("--dry-run", action="store_true", help="Apenas mostrar o que seria feito")
    parser.add_argument("--batch-size", type=int, default=10, help="Tabelas por batch antes de pausar (default: 10)")
    args = parser.parse_args()

    module = args.module.upper()
    if module not in MODULE_NAMES:
        print(f"ERRO: Módulo '{module}' não reconhecido.")
        print(f"Módulos válidos: {', '.join(sorted(MODULE_NAMES.keys()))}")
        sys.exit(1)

    # Detectar project_root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent

    # Diretório das tabelas
    tables_dir = project_root / "src" / "kb" / "oracle-fusion-data-dictionary" / "docs" / module / "tables"
    if not tables_dir.exists():
        print(f"ERRO: Diretório não encontrado: {tables_dir}")
        sys.exit(1)

    # Listar .md files
    if args.table:
        target_file = tables_dir / f"{args.table.lower()}.md"
        if not target_file.exists():
            print(f"ERRO: Arquivo não encontrado: {target_file}")
            sys.exit(1)
        md_files = [target_file]
    else:
        md_files = sorted(tables_dir.glob("*.md"))

    if not md_files:
        print(f"Nenhum arquivo .md encontrado em: {tables_dir}")
        sys.exit(0)

    print(f"╔══════════════════════════════════════════════════════════════╗")
    print(f"║  generate_table_descriptions.py                            ║")
    print(f"║  Módulo: {MODULE_NAMES[module]} ({module}){' ' * max(0, 38 - len(MODULE_NAMES[module]) - len(module))}║")
    print(f"║  Modelo: {MODEL}{' ' * max(0, 50 - len(MODEL))}║")
    print(f"║  Tabelas encontradas: {len(md_files)}{' ' * max(0, 37 - len(str(len(md_files))))}║")
    print(f"╚══════════════════════════════════════════════════════════════╝")
    print()

    # Filtrar tabelas que precisam de enriquecimento
    to_process = []
    skipped = 0

    for md_file in md_files:
        content = md_file.read_text(encoding="utf-8")
        table_name = md_file.stem.upper()

        if needs_enrichment(content, force=args.force):
            to_process.append((md_file, table_name, content))
        else:
            skipped += 1

    print(f"  Tabelas a processar: {len(to_process)}")
    print(f"  Tabelas ignoradas (já enriquecidas): {skipped}")
    print()

    if not to_process:
        print("Nenhuma tabela precisa de enriquecimento. Use --force para re-gerar.")
        return

    if args.dry_run:
        print("=== DRY RUN — Tabelas que seriam processadas ===")
        for i, (md_file, table_name, _) in enumerate(to_process, 1):
            print(f"  {i:3d}. {table_name} — {md_file.name}")
        print()
        print(f"Total: {len(to_process)} tabelas")
        print(f"Custo estimado (aprox.): ~${len(to_process) * 0.02:.2f} USD")
        return

    # Verificar ANTHROPIC_API_KEY
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERRO: Variável de ambiente ANTHROPIC_API_KEY não definida.")
        print("  export ANTHROPIC_API_KEY='sk-ant-...'")
        sys.exit(1)

    # Inicializar cliente
    client = anthropic.Anthropic()
    system_prompt = build_system_prompt(module)

    # Tracking
    total_input_tokens = 0
    total_output_tokens = 0
    success_count = 0
    error_count = 0
    batch_count = 0

    print(f"Iniciando processamento ({len(to_process)} tabelas, batch de {args.batch_size})...")
    print("─" * 64)

    for i, (md_file, table_name, content) in enumerate(to_process, 1):
        # Batch control
        if batch_count >= args.batch_size and batch_count > 0:
            print()
            print(f"  ── Batch de {args.batch_size} concluído ({success_count} ok, {error_count} erro) ──")
            print(f"  Tokens até agora: {total_input_tokens:,} in / {total_output_tokens:,} out")
            cost_so_far = (total_input_tokens * COST_INPUT_PER_M + total_output_tokens * COST_OUTPUT_PER_M) / 1_000_000
            print(f"  Custo até agora: ${cost_so_far:.4f}")
            print()

            try:
                resp = input("  Continuar com o próximo batch? [S/n]: ").strip().lower()
                if resp in ("n", "no", "nao", "não"):
                    print("  Interrompido pelo usuário.")
                    break
            except (EOFError, KeyboardInterrupt):
                print("\n  Interrompido.")
                break

            batch_count = 0
            print()

        print(f"  [{i}/{len(to_process)}] {table_name}...", end=" ", flush=True)

        # Parse existing content
        fm, body = parse_front_matter(content)
        fm_raw = extract_front_matter_raw(content)
        columns = extract_columns_from_table(body)

        # Build prompt
        user_prompt = build_user_prompt(table_name, module, columns, body)

        # Call API
        try:
            data, in_tok, out_tok = call_anthropic(client, system_prompt, user_prompt)
            total_input_tokens += in_tok
            total_output_tokens += out_tok

            if data is None:
                print(f"FALHA (JSON inválido)")
                error_count += 1
                batch_count += 1
                time.sleep(API_DELAY_SECONDS)
                continue

            # Rebuild .md
            new_content = rebuild_md(fm_raw, table_name, data, module)

            # Write
            md_file.write_text(new_content, encoding="utf-8")

            col_count = len(data.get("columns", []))
            sql_count = len(data.get("sql_examples", []))
            print(f"OK ({col_count} cols, {sql_count} SQLs, {in_tok + out_tok:,} tokens)")

            success_count += 1

        except anthropic.APIError as e:
            print(f"ERRO API: {e}")
            error_count += 1

        except Exception as e:
            print(f"ERRO: {e}")
            error_count += 1

        batch_count += 1

        # Rate limiting
        if i < len(to_process):
            time.sleep(API_DELAY_SECONDS)

    # Sumário final
    total_cost = (total_input_tokens * COST_INPUT_PER_M + total_output_tokens * COST_OUTPUT_PER_M) / 1_000_000

    print()
    print("═" * 64)
    print(f"  RESUMO — {MODULE_NAMES[module]} ({module})")
    print("═" * 64)
    print(f"  Processadas:  {success_count}")
    print(f"  Erros:        {error_count}")
    print(f"  Ignoradas:    {skipped}")
    print(f"  Total .md:    {len(md_files)}")
    print("─" * 64)
    print(f"  Tokens input:  {total_input_tokens:>12,}")
    print(f"  Tokens output: {total_output_tokens:>12,}")
    print(f"  Custo total:   ${total_cost:>11.4f}")
    print("═" * 64)


if __name__ == "__main__":
    main()
