---
id: DOC-OTHER-PVO-ExpenditureTypeExtractPVO
doc_type: system-doc
title: "ExpenditureTypeExtractPVO — PVO Cross-Module"
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
  - ExpenditureTypeExtractPVO
  - expendituretypeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpenditureTypeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Expenditure Type Extract. Acessa as tabelas: PJF_EXP_TYPES_B, PJF_EXP_TYPES_TL, PJF_UNITS_OF_MEASURE_V.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ExpenditureTypeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 43 | 3 | 1 | 27 | 63% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_exp_types_b|PJF_EXP_TYPES_B]] — 30 atributos (1 PKs, 14 BICC)
- [[pjf_exp_types_tl|PJF_EXP_TYPES_TL]] — 11 atributos (11 BICC)
- [[pjf_units_of_measure_v|PJF_UNITS_OF_MEASURE_V]] — 2 atributos (2 BICC)

---

## ⚙️ Atributos

### [[pjf_exp_types_b|PJF_EXP_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureTypeBasePEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | ExpenditureTypeBasePEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | ExpenditureTypeBasePEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | ExpenditureTypeBasePEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | ExpenditureTypeBasePEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | ExpenditureTypeBasePEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | ExpenditureTypeBasePEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | ExpenditureTypeBasePEOAttribute2 | ATTRIBUTE2 | — | — |
| 9 | ExpenditureTypeBasePEOAttribute3 | ATTRIBUTE3 | — | — |
| 10 | ExpenditureTypeBasePEOAttribute4 | ATTRIBUTE4 | — | — |
| 11 | ExpenditureTypeBasePEOAttribute5 | ATTRIBUTE5 | — | — |
| 12 | ExpenditureTypeBasePEOAttribute6 | ATTRIBUTE6 | — | — |
| 13 | ExpenditureTypeBasePEOAttribute7 | ATTRIBUTE7 | — | — |
| 14 | ExpenditureTypeBasePEOAttribute8 | ATTRIBUTE8 | — | — |
| 15 | ExpenditureTypeBasePEOAttribute9 | ATTRIBUTE9 | — | — |
| 16 | ExpenditureTypeBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | ExpenditureTypeBasePEOCostRateFlag | COST_RATE_FLAG | — | ✅ |
| 18 | ExpenditureTypeBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 19 | ExpenditureTypeBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 20 | ExpenditureTypeBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 21 | ExpenditureTypeBasePEOExpenditureCategoryId | EXPENDITURE_CATEGORY_ID | — | ✅ |
| 22 | ExpenditureTypeBasePEOExpenditureTypeId | EXPENDITURE_TYPE_ID | 🔑 | ✅ |
| 23 | ExpenditureTypeBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | ExpenditureTypeBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 25 | ExpenditureTypeBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 26 | ExpenditureTypeBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 27 | ExpenditureTypeBasePEOProceedsFlag | PROCEEDS_FLAG | — | ✅ |
| 28 | ExpenditureTypeBasePEORevenueCategoryCode | REVENUE_CATEGORY_CODE | — | ✅ |
| 29 | ExpenditureTypeBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 30 | ExpenditureTypeBasePEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |

### [[pjf_exp_types_tl|PJF_EXP_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureTypeTranslangPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ExpenditureTypeTranslangPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ExpenditureTypeTranslangPEODescription | DESCRIPTION | — | ✅ |
| 4 | ExpenditureTypeTranslangPEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | ✅ |
| 5 | ExpenditureTypeTranslangPEOExpenditureTypeName | EXPENDITURE_TYPE_NAME | — | ✅ |
| 6 | ExpenditureTypeTranslangPEOLanguage | LANGUAGE | — | ✅ |
| 7 | ExpenditureTypeTranslangPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ExpenditureTypeTranslangPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | ExpenditureTypeTranslangPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ExpenditureTypeTranslangPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ExpenditureTypeTranslangPEOSourceLang | SOURCE_LANG | — | ✅ |

### [[pjf_units_of_measure_v|PJF_UNITS_OF_MEASURE_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UnitOfMeasurePEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 2 | UnitOfMeasurePEOUomCode | UOM_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
