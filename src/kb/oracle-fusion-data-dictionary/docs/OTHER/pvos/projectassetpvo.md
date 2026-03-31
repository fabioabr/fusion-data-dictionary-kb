---
id: DOC-OTHER-PVO-ProjectAssetPVO
doc_type: system-doc
title: "ProjectAssetPVO — PVO Cross-Module"
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
  - ProjectAssetPVO
  - projectassetpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectAssetPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Asset. Acessa as tabelas: FUN_ALL_BUSINESS_UNITS_V, PJC_PRJ_ASSETS_ALL, PJC_STANDARD_UNIT_COSTS (+1).

**Caminho:** `FscmTopModelAM.PjcCapitalAM.ProjectAssetPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 76 | 4 | 1 | 34 | 45% |

---

## 🔗 Tabelas Relacionadas

- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 1 atributos
- [[pjc_prj_assets_all|PJC_PRJ_ASSETS_ALL]] — 69 atributos (1 PKs, 32 BICC)
- [[pjc_standard_unit_costs|PJC_STANDARD_UNIT_COSTS]] — 4 atributos (1 BICC)
- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 2 atributos (1 BICC)

---

## ⚙️ Atributos

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOBusinessUnitID | BU_ID | — | — |

### [[pjc_prj_assets_all|PJC_PRJ_ASSETS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ParentProjectAssetPEOAssetDescription | ASSET_DESCRIPTION | — | ✅ |
| 2 | ParentProjectAssetPEOAssetName | ASSET_NAME | — | ✅ |
| 3 | ParentProjectAssetPEOAssetNumber | ASSET_NUMBER | — | ✅ |
| 4 | ParentProjectAssetPEOProjectAssetId | PROJECT_ASSET_ID | — | — |
| 5 | ProjectAssetId | PROJECT_ASSET_ID | 🔑 | ✅ |
| 6 | ProjectAssetPEOAmortizeFlag | AMORTIZE_FLAG | — | ✅ |
| 7 | ProjectAssetPEOAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 8 | ProjectAssetPEOAssetDescription | ASSET_DESCRIPTION | — | ✅ |
| 9 | ProjectAssetPEOAssetKeyCcid | ASSET_KEY_CCID | — | ✅ |
| 10 | ProjectAssetPEOAssetName | ASSET_NAME | — | ✅ |
| 11 | ProjectAssetPEOAssetNumber | ASSET_NUMBER | — | ✅ |
| 12 | ProjectAssetPEOAssetUnits | ASSET_UNITS | — | ✅ |
| 13 | ProjectAssetPEOAssignedToPersonId | ASSIGNED_TO_PERSON_ID | — | — |
| 14 | ProjectAssetPEOAttribute1 | ATTRIBUTE1 | — | — |
| 15 | ProjectAssetPEOAttribute10 | ATTRIBUTE10 | — | — |
| 16 | ProjectAssetPEOAttribute11 | ATTRIBUTE11 | — | — |
| 17 | ProjectAssetPEOAttribute12 | ATTRIBUTE12 | — | — |
| 18 | ProjectAssetPEOAttribute13 | ATTRIBUTE13 | — | — |
| 19 | ProjectAssetPEOAttribute14 | ATTRIBUTE14 | — | — |
| 20 | ProjectAssetPEOAttribute15 | ATTRIBUTE15 | — | — |
| 21 | ProjectAssetPEOAttribute2 | ATTRIBUTE2 | — | — |
| 22 | ProjectAssetPEOAttribute3 | ATTRIBUTE3 | — | — |
| 23 | ProjectAssetPEOAttribute4 | ATTRIBUTE4 | — | — |
| 24 | ProjectAssetPEOAttribute5 | ATTRIBUTE5 | — | — |
| 25 | ProjectAssetPEOAttribute6 | ATTRIBUTE6 | — | — |
| 26 | ProjectAssetPEOAttribute7 | ATTRIBUTE7 | — | — |
| 27 | ProjectAssetPEOAttribute8 | ATTRIBUTE8 | — | — |
| 28 | ProjectAssetPEOAttribute9 | ATTRIBUTE9 | — | — |
| 29 | ProjectAssetPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 30 | ProjectAssetPEOBookTypeCode | BOOK_TYPE_CODE | — | ✅ |
| 31 | ProjectAssetPEOCapitalEventId | CAPITAL_EVENT_ID | — | — |
| 32 | ProjectAssetPEOCapitalHoldFlag | CAPITAL_HOLD_FLAG | — | ✅ |
| 33 | ProjectAssetPEOCapitalizedCost | CAPITALIZED_COST | — | — |
| 34 | ProjectAssetPEOCapitalizedDate | CAPITALIZED_DATE | — | ✅ |
| 35 | ProjectAssetPEOCapitalizedFlag | CAPITALIZED_FLAG | — | — |
| 36 | ProjectAssetPEOCostAdjustmentFlag | COST_ADJUSTMENT_FLAG | — | — |
| 37 | ProjectAssetPEOCreatedBy | CREATED_BY | — | ✅ |
| 38 | ProjectAssetPEOCreationDate | CREATION_DATE | — | ✅ |
| 39 | ProjectAssetPEODatePlacedInService | DATE_PLACED_IN_SERVICE | — | ✅ |
| 40 | ProjectAssetPEODepreciateFlag | DEPRECIATE_FLAG | — | ✅ |
| 41 | ProjectAssetPEODepreciationExpenseCcid | DEPRECIATION_EXPENSE_CCID | — | — |
| 42 | ProjectAssetPEOEstimatedAssetUnits | ESTIMATED_ASSET_UNITS | — | ✅ |
| 43 | ProjectAssetPEOEstimatedCost | ESTIMATED_COST | — | ✅ |
| 44 | ProjectAssetPEOEstimatedInServiceDate | ESTIMATED_IN_SERVICE_DATE | — | ✅ |
| 45 | ProjectAssetPEOFaAssetId | FA_ASSET_ID | — | ✅ |
| 46 | ProjectAssetPEOFaPeriodName | FA_PERIOD_NAME | — | — |
| 47 | ProjectAssetPEOGroupedCipCost | GROUPED_CIP_COST | — | — |
| 48 | ProjectAssetPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 49 | ProjectAssetPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 50 | ProjectAssetPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 51 | ProjectAssetPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 52 | ProjectAssetPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 53 | ProjectAssetPEOLocationId | LOCATION_ID | — | — |
| 54 | ProjectAssetPEOManufacturerName | MANUFACTURER_NAME | — | ✅ |
| 55 | ProjectAssetPEOModelNumber | MODEL_NUMBER | — | ✅ |
| 56 | ProjectAssetPEONewMasterFlag | NEW_MASTER_FLAG | — | — |
| 57 | ProjectAssetPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 58 | ProjectAssetPEOOrgId | ORG_ID | — | — |
| 59 | ProjectAssetPEOParentAssetId | PARENT_ASSET_ID | — | — |
| 60 | ProjectAssetPEOPmAssetReference | PM_ASSET_REFERENCE | — | ✅ |
| 61 | ProjectAssetPEOPmProductCode | PM_PRODUCT_CODE | — | ✅ |
| 62 | ProjectAssetPEOProjectAssetType | PROJECT_ASSET_TYPE | — | ✅ |
| 63 | ProjectAssetPEOProjectId | PROJECT_ID | — | — |
| 64 | ProjectAssetPEORequestId | REQUEST_ID | — | — |
| 65 | ProjectAssetPEORetTargetAssetId | RET_TARGET_ASSET_ID | — | — |
| 66 | ProjectAssetPEOReversalDate | REVERSAL_DATE | — | ✅ |
| 67 | ProjectAssetPEOReverseFlag | REVERSE_FLAG | — | ✅ |
| 68 | ProjectAssetPEOSerialNumber | SERIAL_NUMBER | — | ✅ |
| 69 | ProjectAssetPEOTagNumber | TAG_NUMBER | — | ✅ |

### [[pjc_standard_unit_costs|PJC_STANDARD_UNIT_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StandardAssetUnitCostPEOAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 2 | StandardAssetUnitCostPEOBookTypeCode | BOOK_TYPE_CODE | — | — |
| 3 | StandardAssetUnitCostPEOStandardUnitCost | STANDARD_UNIT_COST | — | ✅ |
| 4 | StandardAssetUnitCostPEOStandardUnitCostId | STANDARD_UNIT_COST_ID | — | — |

### [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectBasePEOProjectId | PROJECT_ID | — | — |
| 2 | ProjectBasePEOProjfuncCurrencyCode | PROJFUNC_CURRENCY_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
