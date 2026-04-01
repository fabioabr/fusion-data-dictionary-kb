---
id: DOC-OTHER-PVO-ExpenditureType
doc_type: system-doc
title: "ExpenditureType — PVO Cross-Module"
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
  - ExpenditureType
  - expendituretype
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpenditureType

## 📌 Visão Geral

View Object para extração BICC de dados de Expenditure Type. Acessa as tabelas: PJF_EXP_CATEGORIES_B, PJF_EXP_CATEGORIES_TL, PJF_EXP_TYPES_B (+2).

**Caminho:** `FscmTopModelAM.PjfSetupTransactionsAM.ExpenditureType`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 48 | 5 | 1 | 15 | 31% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_exp_categories_b|PJF_EXP_CATEGORIES_B]] — 9 atributos (1 BICC)
- [[pjf_exp_categories_tl|PJF_EXP_CATEGORIES_TL]] — 11 atributos (1 BICC)
- [[pjf_exp_types_b|PJF_EXP_TYPES_B]] — 14 atributos (1 PKs, 10 BICC)
- [[pjf_exp_types_tl|PJF_EXP_TYPES_TL]] — 11 atributos (3 BICC)
- [[pjf_units_of_measure_v|PJF_UNITS_OF_MEASURE_V]] — 3 atributos

---

## ⚙️ Atributos

### [[pjf_exp_categories_b|PJF_EXP_CATEGORIES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureCategoryBaseCreatedBy | CREATED_BY | — | — |
| 2 | ExpenditureCategoryBaseCreationDate | CREATION_DATE | — | — |
| 3 | ExpenditureCategoryBaseEndDateActive | END_DATE_ACTIVE | — | — |
| 4 | ExpenditureCategoryBaseExpenditureCategoryId | EXPENDITURE_CATEGORY_ID | — | — |
| 5 | ExpenditureCategoryBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ExpenditureCategoryBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ExpenditureCategoryBaseLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ExpenditureCategoryBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ExpenditureCategoryBaseStartDateActive | START_DATE_ACTIVE | — | — |

### [[pjf_exp_categories_tl|PJF_EXP_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureCategoryTransCreatedBy | CREATED_BY | — | — |
| 2 | ExpenditureCategoryTransCreationDate | CREATION_DATE | — | — |
| 3 | ExpenditureCategoryTransDescription | DESCRIPTION | — | — |
| 4 | ExpenditureCategoryTransExpenditureCategoryId | EXPENDITURE_CATEGORY_ID | — | — |
| 5 | ExpenditureCategoryTransExpenditureCategoryName | EXPENDITURE_CATEGORY_NAME | — | — |
| 6 | ExpenditureCategoryTransLanguage | LANGUAGE | — | — |
| 7 | ExpenditureCategoryTransLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ExpenditureCategoryTransLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ExpenditureCategoryTransLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ExpenditureCategoryTransObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ExpenditureCategoryTransSourceLang | SOURCE_LANG | — | — |

### [[pjf_exp_types_b|PJF_EXP_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureTypeBaseCostRateFlag | COST_RATE_FLAG | — | — |
| 2 | ExpenditureTypeBaseCreatedBy | CREATED_BY | — | ✅ |
| 3 | ExpenditureTypeBaseCreationDate | CREATION_DATE | — | ✅ |
| 4 | ExpenditureTypeBaseEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 5 | ExpenditureTypeBaseExpenditureCategoryId | EXPENDITURE_CATEGORY_ID | — | ✅ |
| 6 | ExpenditureTypeBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ExpenditureTypeBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ExpenditureTypeBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ExpenditureTypeBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ExpenditureTypeBaseProceedsFlag | PROCEEDS_FLAG | — | — |
| 11 | ExpenditureTypeBaseRevenueCategoryCode | REVENUE_CATEGORY_CODE | — | ✅ |
| 12 | ExpenditureTypeBaseStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 13 | ExpenditureTypeBaseUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 14 | ExpenditureTypeId | EXPENDITURE_TYPE_ID | 🔑 | ✅ |

### [[pjf_exp_types_tl|PJF_EXP_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureTypeTransCreatedBy | CREATED_BY | — | — |
| 2 | ExpenditureTypeTransCreationDate | CREATION_DATE | — | — |
| 3 | ExpenditureTypeTransDescription | DESCRIPTION | — | ✅ |
| 4 | ExpenditureTypeTransExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 5 | ExpenditureTypeTransExpenditureTypeName | EXPENDITURE_TYPE_NAME | — | ✅ |
| 6 | ExpenditureTypeTransLanguage | LANGUAGE | — | — |
| 7 | ExpenditureTypeTransLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ExpenditureTypeTransLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ExpenditureTypeTransLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ExpenditureTypeTransObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ExpenditureTypeTransSourceLang | SOURCE_LANG | — | — |

### [[pjf_units_of_measure_v|PJF_UNITS_OF_MEASURE_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UnitOfMeasurePEODescription | DESCRIPTION | — | — |
| 2 | UnitOfMeasurePEOUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 3 | UnitOfMeasurePEOUomCode | UOM_CODE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
