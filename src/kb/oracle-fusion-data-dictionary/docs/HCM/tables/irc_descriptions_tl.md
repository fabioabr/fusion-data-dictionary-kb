---
id: DOC-HCM-479
doc_type: system-doc
title: "IRC_DESCRIPTIONS_TL — Descricoes (Traducoes)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Tecnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - recruiting
  - descriptions-tl
  - irc-recruiting
aliases:
  - IRC_DESCRIPTIONS_TL
  - irc_descriptions_tl
  - descriptions-tl
  - descriptions-tl-hcm
  - irc-descriptions-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_DESCRIPTIONS_TL

## Visao Geral

Traducoes das descricoes. Tabela `_TL`.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traducao** (Translation) — armazena textos multilingues associados a tabela `_B` correspondente. Chave composta pelo ID base + LANGUAGE.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Internacionalizacao:** Descricoes traduzidas para job postings.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DESCRIPTION_ID | NUMBER(18) | NOT NULL | PK/FK | Descricao base | IRC_DESCRIPTIONS_B | 🟢 90% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Idioma | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 90% |
| 4 | DESCRIPTION_TEXT | CLOB | NULL | Dados | Texto traduzido | — | 🟡 80% |
| 5 | DESCRIPTION_TITLE | VARCHAR2(240) | NULL | Dados | Titulo traduzido | — | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_descriptions_b]] — via `DESCRIPTION_ID` (registro base da descricao de vaga)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Descricoes em portugues
```sql
SELECT tl.DESCRIPTION_TITLE, tl.DESCRIPTION_TEXT
FROM   IRC_DESCRIPTIONS_TL tl WHERE tl.LANGUAGE = 'PT';
```

### Filtros comuns
- `LANGUAGE = 'PT'` — Portugues
---

## Observacoes

- DESCRIPTION_TEXT e CLOB — pode conter HTML.
---

## Referencias

- [Oracle Docs -- IRC_DESCRIPTIONS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircdescriptionstl.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[descriptionpvo|DescriptionPVO]] (HCM · BICC: 2/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| DESCRIPTION_ID | DescriptionId1 | — |
| LANGUAGE | Language | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| SOURCE_LANG | SourceLang | — |

### [[offerpvo|OfferPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION_ID | DescriptionTranslationPEODescriptionId | — |
| LANGUAGE | DescriptionTranslationPEOLanguage | — |
| NAME | DescriptionTranslationPEOName | — |
