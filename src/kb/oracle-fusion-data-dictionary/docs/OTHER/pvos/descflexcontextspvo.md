---
id: DOC-OTHER-PVO-DescFlexContextsPVO
doc_type: system-doc
title: "DescFlexContextsPVO — PVO Cross-Module"
system: Oracle Fusion Cloud ERP
module: Cross-Module
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - other
  - data-dictionary
  - pvo
  - bicc
aliases:
  - DescFlexContextsPVO
  - descflexcontextspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DescFlexContextsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Desc Flex Contexts. Acessa as tabelas: FND_DF_CONTEXTS_B, FND_DF_CONTEXTS_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.AnalyticsExtractServiceAM.DescFlexContextsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 2 | 3 | 23 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_df_contexts_b|FND_DF_CONTEXTS_B]] — 16 atributos (3 PKs, 16 BICC)
- [[fnd_df_contexts_tl|FND_DF_CONTEXTS_TL]] — 7 atributos (7 BICC)

---

## ⚙️ Atributos

### [[fnd_df_contexts_b|FND_DF_CONTEXTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 2 | CExtAttribute1 | C_EXT_ATTRIBUTE1 | — | ✅ |
| 3 | CExtAttribute2 | C_EXT_ATTRIBUTE2 | — | ✅ |
| 4 | CExtAttribute3 | C_EXT_ATTRIBUTE3 | — | ✅ |
| 5 | CExtAttribute4 | C_EXT_ATTRIBUTE4 | — | ✅ |
| 6 | CExtAttribute5 | C_EXT_ATTRIBUTE5 | — | ✅ |
| 7 | ContextCode | CONTEXT_CODE | 🔑 | ✅ |
| 8 | CreatedBy | CREATED_BY | — | ✅ |
| 9 | CreationDate | CREATION_DATE | — | ✅ |
| 10 | DescriptiveFlexfieldCode | DESCRIPTIVE_FLEXFIELD_CODE | 🔑 | ✅ |
| 11 | EnabledFlag | ENABLED_FLAG | — | ✅ |
| 12 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | MultirowFlag | MULTIROW_FLAG | — | ✅ |
| 16 | TranslatableFlag | TRANSLATABLE_FLAG | — | ✅ |

### [[fnd_df_contexts_tl|FND_DF_CONTEXTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicationId1 | APPLICATION_ID | — | ✅ |
| 2 | ContextCode1 | CONTEXT_CODE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | DescriptiveFlexfieldCode1 | DESCRIPTIVE_FLEXFIELD_CODE | — | ✅ |
| 5 | Language | LANGUAGE | — | ✅ |
| 6 | Name | NAME | — | ✅ |
| 7 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
