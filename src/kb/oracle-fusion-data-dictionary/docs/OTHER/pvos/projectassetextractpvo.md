---
id: DOC-OTHER-PVO-ProjectAssetExtractPVO
doc_type: system-doc
title: "ProjectAssetExtractPVO — PVO Cross-Module"
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
  - ProjectAssetExtractPVO
  - projectassetextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectAssetExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Asset Extract. Acessa as tabelas: PJC_PRJ_ASSETS_ALL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjcBiccExtractAM.ProjectAssetExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 66 | 1 | 1 | 51 | 77% |

---

## 🔗 Tabelas Relacionadas

- [[pjc_prj_assets_all|PJC_PRJ_ASSETS_ALL]] — 66 atributos (1 PKs, 51 BICC)

---

## ⚙️ Atributos

### [[pjc_prj_assets_all|PJC_PRJ_ASSETS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjcPrjAssetsAllAmortizeFlag | AMORTIZE_FLAG | — | ✅ |
| 2 | PjcPrjAssetsAllAssetCategoryId | ASSET_CATEGORY_ID | — | ✅ |
| 3 | PjcPrjAssetsAllAssetDescription | ASSET_DESCRIPTION | — | ✅ |
| 4 | PjcPrjAssetsAllAssetKeyCcid | ASSET_KEY_CCID | — | ✅ |
| 5 | PjcPrjAssetsAllAssetName | ASSET_NAME | — | ✅ |
| 6 | PjcPrjAssetsAllAssetNumber | ASSET_NUMBER | — | ✅ |
| 7 | PjcPrjAssetsAllAssetUnits | ASSET_UNITS | — | ✅ |
| 8 | PjcPrjAssetsAllAssignedToPersonId | ASSIGNED_TO_PERSON_ID | — | ✅ |
| 9 | PjcPrjAssetsAllAttribute1 | ATTRIBUTE1 | — | ✅ |
| 10 | PjcPrjAssetsAllAttribute10 | ATTRIBUTE10 | — | — |
| 11 | PjcPrjAssetsAllAttribute11 | ATTRIBUTE11 | — | — |
| 12 | PjcPrjAssetsAllAttribute12 | ATTRIBUTE12 | — | — |
| 13 | PjcPrjAssetsAllAttribute13 | ATTRIBUTE13 | — | — |
| 14 | PjcPrjAssetsAllAttribute14 | ATTRIBUTE14 | — | — |
| 15 | PjcPrjAssetsAllAttribute15 | ATTRIBUTE15 | — | — |
| 16 | PjcPrjAssetsAllAttribute2 | ATTRIBUTE2 | — | — |
| 17 | PjcPrjAssetsAllAttribute3 | ATTRIBUTE3 | — | — |
| 18 | PjcPrjAssetsAllAttribute4 | ATTRIBUTE4 | — | — |
| 19 | PjcPrjAssetsAllAttribute5 | ATTRIBUTE5 | — | — |
| 20 | PjcPrjAssetsAllAttribute6 | ATTRIBUTE6 | — | — |
| 21 | PjcPrjAssetsAllAttribute7 | ATTRIBUTE7 | — | — |
| 22 | PjcPrjAssetsAllAttribute8 | ATTRIBUTE8 | — | — |
| 23 | PjcPrjAssetsAllAttribute9 | ATTRIBUTE9 | — | — |
| 24 | PjcPrjAssetsAllAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 25 | PjcPrjAssetsAllBookTypeCode | BOOK_TYPE_CODE | — | ✅ |
| 26 | PjcPrjAssetsAllCapitalEventId | CAPITAL_EVENT_ID | — | ✅ |
| 27 | PjcPrjAssetsAllCapitalHoldFlag | CAPITAL_HOLD_FLAG | — | ✅ |
| 28 | PjcPrjAssetsAllCapitalizedCost | CAPITALIZED_COST | — | ✅ |
| 29 | PjcPrjAssetsAllCapitalizedDate | CAPITALIZED_DATE | — | ✅ |
| 30 | PjcPrjAssetsAllCapitalizedFlag | CAPITALIZED_FLAG | — | ✅ |
| 31 | PjcPrjAssetsAllCostAdjustmentFlag | COST_ADJUSTMENT_FLAG | — | ✅ |
| 32 | PjcPrjAssetsAllCreatedBy | CREATED_BY | — | ✅ |
| 33 | PjcPrjAssetsAllCreationDate | CREATION_DATE | — | ✅ |
| 34 | PjcPrjAssetsAllDatePlacedInService | DATE_PLACED_IN_SERVICE | — | ✅ |
| 35 | PjcPrjAssetsAllDepreciateFlag | DEPRECIATE_FLAG | — | ✅ |
| 36 | PjcPrjAssetsAllDepreciationExpenseCcid | DEPRECIATION_EXPENSE_CCID | — | ✅ |
| 37 | PjcPrjAssetsAllEstimatedAssetUnits | ESTIMATED_ASSET_UNITS | — | ✅ |
| 38 | PjcPrjAssetsAllEstimatedCost | ESTIMATED_COST | — | ✅ |
| 39 | PjcPrjAssetsAllEstimatedInServiceDate | ESTIMATED_IN_SERVICE_DATE | — | ✅ |
| 40 | PjcPrjAssetsAllFaAssetId | FA_ASSET_ID | — | ✅ |
| 41 | PjcPrjAssetsAllFaPeriodName | FA_PERIOD_NAME | — | ✅ |
| 42 | PjcPrjAssetsAllGroupedCipCost | GROUPED_CIP_COST | — | ✅ |
| 43 | PjcPrjAssetsAllJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 44 | PjcPrjAssetsAllJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 45 | PjcPrjAssetsAllLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 46 | PjcPrjAssetsAllLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 47 | PjcPrjAssetsAllLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 48 | PjcPrjAssetsAllLocationId | LOCATION_ID | — | ✅ |
| 49 | PjcPrjAssetsAllManufacturerName | MANUFACTURER_NAME | — | ✅ |
| 50 | PjcPrjAssetsAllModelNumber | MODEL_NUMBER | — | ✅ |
| 51 | PjcPrjAssetsAllNewMasterFlag | NEW_MASTER_FLAG | — | ✅ |
| 52 | PjcPrjAssetsAllObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 53 | PjcPrjAssetsAllOrgId | ORG_ID | — | ✅ |
| 54 | PjcPrjAssetsAllParentAssetId | PARENT_ASSET_ID | — | ✅ |
| 55 | PjcPrjAssetsAllPmAssetReference | PM_ASSET_REFERENCE | — | ✅ |
| 56 | PjcPrjAssetsAllPmProductCode | PM_PRODUCT_CODE | — | ✅ |
| 57 | PjcPrjAssetsAllProjectAssetId | PROJECT_ASSET_ID | 🔑 | ✅ |
| 58 | PjcPrjAssetsAllProjectAssetName | ASSET_NAME | — | ✅ |
| 59 | PjcPrjAssetsAllProjectAssetType | PROJECT_ASSET_TYPE | — | ✅ |
| 60 | PjcPrjAssetsAllProjectId | PROJECT_ID | — | ✅ |
| 61 | PjcPrjAssetsAllRequestId | REQUEST_ID | — | ✅ |
| 62 | PjcPrjAssetsAllRetTargetAssetId | RET_TARGET_ASSET_ID | — | ✅ |
| 63 | PjcPrjAssetsAllReversalDate | REVERSAL_DATE | — | ✅ |
| 64 | PjcPrjAssetsAllReverseFlag | REVERSE_FLAG | — | ✅ |
| 65 | PjcPrjAssetsAllSerialNumber | SERIAL_NUMBER | — | ✅ |
| 66 | PjcPrjAssetsAllTagNumber | TAG_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
