# Pipeline de Geracao — Data Dictionary Oracle Fusion

## Visao Geral

Pipeline de 10 passos para extrair, enriquecer, traduzir e publicar o dicionario de dados do Oracle Fusion Cloud (BICC) como documentacao HTML standalone navegavel.

## Passos

| Passo | Nome | Descricao |
|-------|------|-----------|
| 01 | EXTRACT-TABLES | Extrai metadados de tabelas do Excel BICC |
| 02 | EXTRACT-PVOS | Extrai dados de PVOs do Excel BICC |
| 03 | GENERATE-TABLE-DESC | LLM gera descricoes ricas para tabelas |
| 04 | GENERATE-PVO-DESC | LLM gera descricoes de negocio para PVOs |
| 05 | CREATE-I18N | Extrai conteudo traduzivel para .i18n.json |
| 06 | TRANSLATE | Traduz i18n para EN e ES |
| 06b | BUILD-REVERSE-INDEX | Gera indice reverso tabela → PVOs |
| 07 | BUILD-TABLE-HTML | Gera HTML standalone a partir de .md |
| 08 | BUILD-PVO-HTML | Gera HTML standalone a partir de .json (PVO) |
| 09 | BUILD-MODULE-INDEX | Gera index.html por modulo |
| 10 | BUILD-PORTAL | Atualiza portal principal (docs/index.html) |

## Pre-requisitos

- Python 3.12+
- openpyxl (`pip install openpyxl`)
- Ollama local (`http://localhost:11434`) com modelo `translategemma:4b`
- Anthropic API key (variavel `ANTHROPIC_API_KEY`) — para passos 03 e 04

## Fontes de Dados (Excel BICC)

- **FSCM:** `src/raw-files/Rel13_25A_BICC_FSCM_Database_Mapping_with_ViewObjects.xlsx`
- **HCM:** `src/raw-files/Rel13_25A_BICC_HCM_Database_Mapping_with_ViewObjects.xlsx`

Mapeamento de tabelas:

- `src/kb/oracle-fusion-data-dictionary/docs/table-mappings.txt`

## Caminhos de Saida

| Tipo | Caminho |
|------|---------|
| Markdown (.md) | `src/kb/oracle-fusion-data-dictionary/docs/{MODULE}/tables/` |
| JSON PVO (.json) | `src/kb/oracle-fusion-data-dictionary/docs/{MODULE}/pvos/` |
| HTML tabelas | `docs/fusion-kb/data-dictionary/{MODULE}/tables/` |
| HTML PVOs | `docs/fusion-kb/data-dictionary/{MODULE}/pvos/` |
| Indice reverso PVO | `scripts/config/table_to_pvos_map.json` |
| Indice modulo | `docs/fusion-kb/data-dictionary/{MODULE}/index.html` |
| Portal | `docs/index.html` |

## Grafo de Dependencias

```
01 ──→ 03 ──→ 05 ──→ 06 ──┬──→ 07 ──┐
                           │         ├──→ 09 ──→ 10
02 ──→ 04 ──→ 05 ──→ 06 ──┼──→ 08 ──┘
                           │
                           └──→ 06b ──→ 07
```

**Legenda:**

- `01 → 03` — Esqueletos .md alimentam geracao de descricoes
- `02 → 04` — JSONs PVO alimentam geracao de descricoes
- `03/04 → 05` — Conteudo enriquecido alimenta extracao i18n
- `05 → 06` — Arquivos .i18n.json alimentam traducao
- `06 → 06b` — PVO JSONs + i18n alimentam indice reverso tabela→PVOs
- `06b → 07` — Indice reverso alimenta aba "PVOs Relacionados" no HTML de tabelas
- `06 → 07/08` — Traducoes prontas alimentam geracao HTML
- `07/08 → 09` — HTMLs individuais alimentam indice do modulo
- `09 → 10` — Indices de modulo alimentam portal principal

## Passos que Requerem LLM

| Passo | Modelo |
|-------|--------|
| 03 — generate-table-descriptions | Claude Opus (Anthropic API) |
| 04 — generate-pvo-descriptions | Claude Opus (Anthropic API) |

## Passo que Requer Ollama

| Passo | Modelo |
|-------|--------|
| 06 — translate | translategemma:4b (Ollama local) |

## Configuracao

Arquivo de configuracao central: `scripts/config/modules.json`

Contem fontes Excel, modulos com icones/cores e configuracao Ollama.
