---
id: DOC-OTHER-PVO-CategoryExtractPVO
doc_type: system-doc
title: "CategoryExtractPVO — PVO Cross-Module"
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
  - CategoryExtractPVO
  - categoryextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CategoryExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Category Extract. Acessa as tabelas: EGP_CATEGORIES_B, EGP_CATEGORIES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgpBiccExtractAM.CategoryExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 54 | 2 | 1 | 50 | 93% |

---

## 🔗 Tabelas Relacionadas

- [[egp_categories_b|EGP_CATEGORIES_B]] — 50 atributos (1 PKs, 50 BICC)
- [[egp_categories_tl|EGP_CATEGORIES_TL]] — 4 atributos

---

## ⚙️ Atributos

### [[egp_categories_b|EGP_CATEGORIES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryBasePEOAttribute1 | ATTRIBUTE1 | — | ✅ |
| 2 | CategoryBasePEOAttribute10 | ATTRIBUTE10 | — | ✅ |
| 3 | CategoryBasePEOAttribute11 | ATTRIBUTE11 | — | ✅ |
| 4 | CategoryBasePEOAttribute12 | ATTRIBUTE12 | — | ✅ |
| 5 | CategoryBasePEOAttribute13 | ATTRIBUTE13 | — | ✅ |
| 6 | CategoryBasePEOAttribute14 | ATTRIBUTE14 | — | ✅ |
| 7 | CategoryBasePEOAttribute15 | ATTRIBUTE15 | — | ✅ |
| 8 | CategoryBasePEOAttribute2 | ATTRIBUTE2 | — | ✅ |
| 9 | CategoryBasePEOAttribute3 | ATTRIBUTE3 | — | ✅ |
| 10 | CategoryBasePEOAttribute4 | ATTRIBUTE4 | — | ✅ |
| 11 | CategoryBasePEOAttribute5 | ATTRIBUTE5 | — | ✅ |
| 12 | CategoryBasePEOAttribute6 | ATTRIBUTE6 | — | ✅ |
| 13 | CategoryBasePEOAttribute7 | ATTRIBUTE7 | — | ✅ |
| 14 | CategoryBasePEOAttribute8 | ATTRIBUTE8 | — | ✅ |
| 15 | CategoryBasePEOAttribute9 | ATTRIBUTE9 | — | ✅ |
| 16 | CategoryBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 17 | CategoryBasePEOAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 18 | CategoryBasePEOAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 19 | CategoryBasePEOAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 20 | CategoryBasePEOAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 21 | CategoryBasePEOAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 22 | CategoryBasePEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 23 | CategoryBasePEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 24 | CategoryBasePEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 25 | CategoryBasePEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 26 | CategoryBasePEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 27 | CategoryBasePEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 28 | CategoryBasePEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 29 | CategoryBasePEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 30 | CategoryBasePEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 31 | CategoryBasePEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 32 | CategoryBasePEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 33 | CategoryBasePEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 34 | CategoryBasePEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 35 | CategoryBasePEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 36 | CategoryBasePEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 37 | CategoryBasePEOCategoryCode | CATEGORY_CODE | — | ✅ |
| 38 | CategoryBasePEOCategoryContentCode | CATEGORY_CONTENT_CODE | — | ✅ |
| 39 | CategoryBasePEOCategoryId | CATEGORY_ID | 🔑 | ✅ |
| 40 | CategoryBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 41 | CategoryBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 42 | CategoryBasePEODescription | DESCRIPTION | — | ✅ |
| 43 | CategoryBasePEODisableDate | DISABLE_DATE | — | ✅ |
| 44 | CategoryBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 45 | CategoryBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 46 | CategoryBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 47 | CategoryBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 48 | CategoryBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 49 | CategoryBasePEOSupplierEnabledFlag | SUPPLIER_ENABLED_FLAG | — | ✅ |
| 50 | CategoryBasePEOWebStatus | WEB_STATUS | — | ✅ |

### [[egp_categories_tl|EGP_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryTranslationPEOCategoryId | CATEGORY_ID | — | — |
| 2 | CategoryTranslationPEOCategoryName | CATEGORY_NAME | — | — |
| 3 | CategoryTranslationPEODescription | DESCRIPTION | — | — |
| 4 | CategoryTranslationPEOLanguage | LANGUAGE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
