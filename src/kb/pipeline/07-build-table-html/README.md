# Passo 07 — Gerar HTML de Tabelas

## Objetivo

Gerar arquivos HTML standalone a partir dos `.md` enriquecidos de tabelas,
incorporando traducoes i18n e seguindo o design system do projeto.

## DoR (Definition of Ready)

- Passo 06 concluido: `.i18n.json` com traducoes EN/ES preenchidas
- Passo 06b concluido: `scripts/config/table_to_pvos_map.json` gerado (indice reverso tabela→PVOs)
- Template HTML disponivel: `scripts/07-build-table-html/template_system_doc.html`
- Playground de referencia: `.claude/behavior/ui_ux/playground.html`

## DoD (Definition of Done)

- Um `.html` por tabela em `docs/fusion-kb/data-dictionary/{MODULE}/tables/`
- HTML e self-contained (CSS+JS inline, sem dependencias externas)
- Seletor de idioma funcional (PT-BR / EN / ES)
- Toggle tema claro/escuro funcional
- 5 abas: Visao Geral, Colunas, Relacionamentos, PVOs Relacionados, SQL
- Aba "PVOs Relacionados" exibe mapeamentos agrupados por PVO (condicional — so aparece se existirem PVOs)

## Entrada

- `src/kb/oracle-fusion-data-dictionary/docs/{MODULE}/tables/{TABLE}.md`
- `src/kb/oracle-fusion-data-dictionary/docs/{MODULE}/tables/{TABLE}.i18n.json`
- `scripts/config/table_to_pvos_map.json` (indice reverso gerado pelo passo 06b)
- `scripts/07-build-table-html/template_system_doc.html`

## Saida

- `docs/fusion-kb/data-dictionary/{MODULE}/tables/{TABLE_NAME}.html`

## Requer LLM

Nao.

## Uso

```bash
python scripts/07-build-table-html/build_table_html.py --batch src/kb/.../GL/tables/
python scripts/07-build-table-html/build_table_html.py src/kb/.../GL/tables/GL_JE_HEADERS.md
python scripts/07-build-table-html/build_table_html.py --module GL
```

## Notas

- O template usa design tokens do playground (`var(--*)`)
- Header e footer sempre em gradiente escuro, independente do tema
- Logo dark sempre visivel (header e sempre escuro)
- Tipografia: Poppins (Google Fonts), icones: Remix Icon (CDN)
- i18n via atributo `data-i18n` + dicionario JS embutido
- Re-execucao sobrescreve HTMLs existentes
