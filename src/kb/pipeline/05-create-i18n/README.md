# Passo 05 — Criar Arquivos I18N

## Objetivo

Extrair conteudo traduzivel de arquivos .md (tabelas) e .json (PVOs) para gerar arquivos .i18n.json contendo frases em pt-BR prontas para traducao.

## DOR (Definition of Ready)

- Passo 03 concluido: .md enriquecidos com descricoes
- Passo 04 concluido: .json com `meta.description` preenchido

## DOD (Definition of Done)

- Todo .md de tabela possui um .i18n.json correspondente
- Todo .json de PVO possui um .i18n.json correspondente
- Cada .i18n.json contem: source, source_hash, translated_at:null, items[]
- Itens tecnicos (nomes de colunas, tipos) foram excluidos corretamente

## Entrada

- `src/kb/oracle-fusion-data-dictionary/docs/{MODULE}/tables/{TABLE}.md`
- `src/kb/oracle-fusion-data-dictionary/docs/{MODULE}/pvos/{PVO}.json`

## Saida

- `src/kb/oracle-fusion-data-dictionary/docs/{MODULE}/tables/{TABLE}.i18n.json`
- `src/kb/oracle-fusion-data-dictionary/docs/{MODULE}/pvos/{PVO}.i18n.json`

## Requer LLM

Nao.

## Uso

### Tabelas (.md → .i18n.json)

```bash
python scripts/05-create-i18n/extract_table_i18n.py --batch src/kb/.../GL/tables/
python scripts/05-create-i18n/extract_table_i18n.py src/kb/.../GL/tables/GL_JE_HEADERS.md
```

### PVOs (.json → .i18n.json)

```bash
python scripts/05-create-i18n/extract_pvo_i18n.py --batch src/kb/.../GL/pvos/
python scripts/05-create-i18n/extract_pvo_i18n.py src/kb/.../GL/pvos/GlBalancePVO.json
```

## Notas

- Sao dois scripts separados: `extract_table_i18n.py` (para .md) e `extract_pvo_i18n.py` (para .json)
- O `source_hash` (MD5) permite cache: re-execucao pula arquivos inalterados
- Use `--force` para regenerar mesmo com cache valido
- Arquivos .i18n.json sao usados nos passos 06 (traducao) e 07/08 (HTML)
