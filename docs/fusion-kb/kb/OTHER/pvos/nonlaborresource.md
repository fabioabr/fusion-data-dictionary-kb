---
id: DOC-OTHER-PVO-NonLaborResource
doc_type: system-doc
title: "NonLaborResource — PVO Cross-Module"
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
  - NonLaborResource
  - nonlaborresource
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NonLaborResource

## 📌 Visão Geral

View Object para extração BICC de dados de Non Labor Resource. Acessa as tabelas: PJF_EXP_TYPES_B, PJF_EXP_TYPES_TL, PJF_NON_LABOR_RES_B (+1).

**Caminho:** `FscmTopModelAM.PjfSetupTransactionsAM.NonLaborResource`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 47 | 4 | 1 | 10 | 21% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_exp_types_b|PJF_EXP_TYPES_B]] — 14 atributos (1 BICC)
- [[pjf_exp_types_tl|PJF_EXP_TYPES_TL]] — 11 atributos (1 BICC)
- [[pjf_non_labor_res_b|PJF_NON_LABOR_RES_B]] — 11 atributos (1 PKs, 7 BICC)
- [[pjf_non_labor_res_tl|PJF_NON_LABOR_RES_TL]] — 11 atributos (1 BICC)

---

## ⚙️ Atributos

### [[pjf_exp_types_b|PJF_EXP_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureTypeBasePEOCostRateFlag | COST_RATE_FLAG | — | — |
| 2 | ExpenditureTypeBasePEOCreatedBy | CREATED_BY | — | — |
| 3 | ExpenditureTypeBasePEOCreationDate | CREATION_DATE | — | — |
| 4 | ExpenditureTypeBasePEOEndDateActive | END_DATE_ACTIVE | — | — |
| 5 | ExpenditureTypeBasePEOExpenditureCategoryId | EXPENDITURE_CATEGORY_ID | — | — |
| 6 | ExpenditureTypeBasePEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 7 | ExpenditureTypeBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ExpenditureTypeBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ExpenditureTypeBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ExpenditureTypeBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ExpenditureTypeBasePEOProceedsFlag | PROCEEDS_FLAG | — | — |
| 12 | ExpenditureTypeBasePEORevenueCategoryCode | REVENUE_CATEGORY_CODE | — | — |
| 13 | ExpenditureTypeBasePEOStartDateActive | START_DATE_ACTIVE | — | — |
| 14 | ExpenditureTypeBasePEOUnitOfMeasure | UNIT_OF_MEASURE | — | — |

### [[pjf_exp_types_tl|PJF_EXP_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureTypeTranslationPE1CreatedBy | CREATED_BY | — | — |
| 2 | ExpenditureTypeTranslationPE1CreationDate | CREATION_DATE | — | — |
| 3 | ExpenditureTypeTranslationPE1Description | DESCRIPTION | — | — |
| 4 | ExpenditureTypeTranslationPE1ExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 5 | ExpenditureTypeTranslationPE1ExpenditureTypeName | EXPENDITURE_TYPE_NAME | — | — |
| 6 | ExpenditureTypeTranslationPE1Language | LANGUAGE | — | — |
| 7 | ExpenditureTypeTranslationPE1LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ExpenditureTypeTranslationPE1LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ExpenditureTypeTranslationPE1LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ExpenditureTypeTranslationPE1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ExpenditureTypeTranslationPE1SourceLang | SOURCE_LANG | — | — |

### [[pjf_non_labor_res_b|PJF_NON_LABOR_RES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NonLaborResourceBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | NonLaborResourceBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | NonLaborResourceBasePEOEndDateActive | END_DATE_ACTIVE | — | — |
| 4 | NonLaborResourceBasePEOEquipmentResourceFlag | EQUIPMENT_RESOURCE_FLAG | — | ✅ |
| 5 | NonLaborResourceBasePEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | ✅ |
| 6 | NonLaborResourceBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | NonLaborResourceBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | NonLaborResourceBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | NonLaborResourceBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | NonLaborResourceBasePEOStartDateActive | START_DATE_ACTIVE | — | — |
| 11 | NonLaborResourceId | NON_LABOR_RESOURCE_ID | 🔑 | ✅ |

### [[pjf_non_labor_res_tl|PJF_NON_LABOR_RES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NonLaborResourceTranslationP1CreatedBy | CREATED_BY | — | — |
| 2 | NonLaborResourceTranslationP1CreationDate | CREATION_DATE | — | — |
| 3 | NonLaborResourceTranslationP1Description | DESCRIPTION | — | — |
| 4 | NonLaborResourceTranslationP1Language | LANGUAGE | — | — |
| 5 | NonLaborResourceTranslationP1LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | NonLaborResourceTranslationP1LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | NonLaborResourceTranslationP1LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | NonLaborResourceTranslationP1NlrName | NLR_NAME | — | — |
| 9 | NonLaborResourceTranslationP1NonLaborResourceId | NON_LABOR_RESOURCE_ID | — | — |
| 10 | NonLaborResourceTranslationP1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | NonLaborResourceTranslationP1SourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
