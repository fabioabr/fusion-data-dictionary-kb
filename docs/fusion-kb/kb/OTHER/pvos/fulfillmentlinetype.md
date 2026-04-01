---
id: DOC-OTHER-PVO-FulfillmentLineType
doc_type: system-doc
title: "FulfillmentLineType — PVO Cross-Module"
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
  - FulfillmentLineType
  - fulfillmentlinetype
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FulfillmentLineType

## 📌 Visão Geral

View Object para extração BICC de dados de Fulfillment Line Type. Acessa as tabelas: OKC_LINE_TYPES_TL, OKC_LINE_TYPES_VL.

**Caminho:** `FscmTopModelAM.ContractsCoreAM.FulfillmentLineType`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 2 | 1 | 14 | 58% |

---

## 🔗 Tabelas Relacionadas

- [[okc_line_types_tl|OKC_LINE_TYPES_TL]] — 11 atributos (6 BICC)
- [[okc_line_types_vl|OKC_LINE_TYPES_VL]] — 13 atributos (1 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[okc_line_types_tl|OKC_LINE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LineTypeTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | LineTypeTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | LineTypeTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | LineTypeTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 5 | LineTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LineTypeTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LineTypeTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | LineTypeTranslationPEOLineTypeId | LINE_TYPE_ID | — | ✅ |
| 9 | LineTypeTranslationPEOName | NAME | — | ✅ |
| 10 | LineTypeTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | LineTypeTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

### [[okc_line_types_vl|OKC_LINE_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LineTypePEOCreatedBy | CREATED_BY | — | — |
| 2 | LineTypePEOCreationDate | CREATION_DATE | — | — |
| 3 | LineTypePEODescription | DESCRIPTION | — | ✅ |
| 4 | LineTypePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LineTypePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | LineTypePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | LineTypePEOLineTypeId | LINE_TYPE_ID | 🔑 | ✅ |
| 8 | LineTypePEOName | NAME | — | ✅ |
| 9 | LineTypePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | LineTypePEOParentLineTypeId | PARENT_LINE_TYPE_ID | — | ✅ |
| 11 | LineTypePEORecursiveYn | RECURSIVE_YN | — | ✅ |
| 12 | LineTypePEOSourceCode | SOURCE_CODE | — | ✅ |
| 13 | LineTypePEOSourceCodeClass | SOURCE_CODE_CLASS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
