---
id: DOC-OTHER-PVO-ExpenditureTypeView
doc_type: system-doc
title: "ExpenditureTypeView — PVO Cross-Module"
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
  - ExpenditureTypeView
  - expendituretypeview
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpenditureTypeView

## 📌 Visão Geral

View Object para extração BICC de dados de Expenditure Type View. Acessa as tabelas: PJF_EXP_CATEGORIES_VL, PJF_EXP_TYPES_VL, PJF_UNITS_OF_MEASURE_V.

**Caminho:** `FscmTopModelAM.PjfSetupTransactionsAM.ExpenditureTypeView`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 3 | 1 | 20 | 67% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_exp_categories_vl|PJF_EXP_CATEGORIES_VL]] — 11 atributos (6 BICC)
- [[pjf_exp_types_vl|PJF_EXP_TYPES_VL]] — 16 atributos (1 PKs, 13 BICC)
- [[pjf_units_of_measure_v|PJF_UNITS_OF_MEASURE_V]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[pjf_exp_categories_vl|PJF_EXP_CATEGORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureCategoryCreatedBy | CREATED_BY | — | — |
| 2 | ExpenditureCategoryCreationDate | CREATION_DATE | — | — |
| 3 | ExpenditureCategoryDescription | DESCRIPTION | — | ✅ |
| 4 | ExpenditureCategoryEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 5 | ExpenditureCategoryExpenditureCategoryId | EXPENDITURE_CATEGORY_ID | — | ✅ |
| 6 | ExpenditureCategoryExpenditureCategoryName | EXPENDITURE_CATEGORY_NAME | — | ✅ |
| 7 | ExpenditureCategoryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ExpenditureCategoryLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ExpenditureCategoryLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ExpenditureCategoryObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ExpenditureCategoryStartDateActive | START_DATE_ACTIVE | — | ✅ |

### [[pjf_exp_types_vl|PJF_EXP_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureTypeCostRateFlag | COST_RATE_FLAG | — | ✅ |
| 2 | ExpenditureTypeCreatedBy | CREATED_BY | — | ✅ |
| 3 | ExpenditureTypeCreationDate | CREATION_DATE | — | ✅ |
| 4 | ExpenditureTypeDescription | DESCRIPTION | — | ✅ |
| 5 | ExpenditureTypeEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 6 | ExpenditureTypeExpenditureCategoryId | EXPENDITURE_CATEGORY_ID | — | — |
| 7 | ExpenditureTypeExpenditureTypeName | EXPENDITURE_TYPE_NAME | — | ✅ |
| 8 | ExpenditureTypeId | EXPENDITURE_TYPE_ID | 🔑 | ✅ |
| 9 | ExpenditureTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | ExpenditureTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | ExpenditureTypeLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | ExpenditureTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | ExpenditureTypeProceedsFlag | PROCEEDS_FLAG | — | ✅ |
| 14 | ExpenditureTypeRevenueCategoryCode | REVENUE_CATEGORY_CODE | — | ✅ |
| 15 | ExpenditureTypeStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 16 | ExpenditureTypeUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |

### [[pjf_units_of_measure_v|PJF_UNITS_OF_MEASURE_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UnitOfMeasurePEODescription | DESCRIPTION | — | — |
| 2 | UnitOfMeasurePEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 3 | UnitOfMeasurePEOUomCode | UOM_CODE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
