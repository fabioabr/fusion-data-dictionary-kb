---
id: DOC-OTHER-PVO-WhereUsedRollupDetailPVO
doc_type: system-doc
title: "WhereUsedRollupDetailPVO — PVO Cross-Module"
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
  - WhereUsedRollupDetailPVO
  - whereusedrollupdetailpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WhereUsedRollupDetailPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Where Used Rollup Detail. Acessa as tabelas: CST_COSTED_VU_ONHAND_V, CST_COST_ORGS_V, CST_COST_ORG_BOOKS (+8).

**Caminho:** `FscmTopModelAM.ScenariosAM.WhereUsedRollupDetailPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 916 | 11 | 1 | 67 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[cst_costed_vu_onhand_v|CST_COSTED_VU_ONHAND_V]] — 8 atributos (4 BICC)
- [[cst_cost_orgs_v|CST_COST_ORGS_V]] — 6 atributos
- [[cst_cost_org_books|CST_COST_ORG_BOOKS]] — 91 atributos
- [[cst_cost_org_parameters|CST_COST_ORG_PARAMETERS]] — 10 atributos
- [[cst_rollup_det_otbi_v|CST_ROLLUP_DET_OTBI_V]] — 42 atributos (7 BICC)
- [[cst_std_overhead_rates|CST_STD_OVERHEAD_RATES]] — 31 atributos (3 BICC)
- [[cst_std_overhead_rate_details|CST_STD_OVERHEAD_RATE_DETAILS]] — 12 atributos (2 BICC)
- [[cst_where_used_rollup_dtls_v|CST_WHERE_USED_ROLLUP_DTLS_V]] — 68 atributos (1 PKs, 37 BICC)
- [[po_headers_all|PO_HEADERS_ALL]] — 213 atributos (4 BICC)
- [[po_lines_all|PO_LINES_ALL]] — 188 atributos (5 BICC)
- [[po_line_locations_all|PO_LINE_LOCATIONS_ALL]] — 247 atributos (5 BICC)

---

## ⚙️ Atributos

### [[cst_costed_vu_onhand_v|CST_COSTED_VU_ONHAND_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostedVuOnhandPEOCostBookId | COST_BOOK_ID | — | — |
| 2 | CostedVuOnhandPEOCostOrgId | COST_ORG_ID | — | — |
| 3 | CostedVuOnhandPEOEffToDate | EFF_TO_DATE | — | ✅ |
| 4 | CostedVuOnhandPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 5 | CostedVuOnhandPEOQuantity | QUANTITY | — | ✅ |
| 6 | CostedVuOnhandPEOSnapshotDate | SNAPSHOT_DATE | — | ✅ |
| 7 | CostedVuOnhandPEOUomCode | UOM_CODE | — | ✅ |
| 8 | CostedVuOnhandPEOValUnitId | VAL_UNIT_ID | — | — |

### [[cst_cost_orgs_v|CST_COST_ORGS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostOrganizationVPEOCostOrgCode | COST_ORG_CODE | — | — |
| 2 | CostOrganizationVPEOCostOrgId | COST_ORG_ID | — | — |
| 3 | CostOrganizationVPEOCostOrgName | COST_ORG_NAME | — | — |
| 4 | CostOrganizationVPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 5 | CostOrganizationVPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 6 | CostOrganizationVPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |

### [[cst_cost_org_books|CST_COST_ORG_BOOKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostOrgBookPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | CostOrgBookPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | CostOrgBookPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | CostOrgBookPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | CostOrgBookPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | CostOrgBookPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | CostOrgBookPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | CostOrgBookPEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | CostOrgBookPEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | CostOrgBookPEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | CostOrgBookPEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | CostOrgBookPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | CostOrgBookPEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | CostOrgBookPEOAttribute21 | ATTRIBUTE21 | — | — |
| 15 | CostOrgBookPEOAttribute22 | ATTRIBUTE22 | — | — |
| 16 | CostOrgBookPEOAttribute23 | ATTRIBUTE23 | — | — |
| 17 | CostOrgBookPEOAttribute24 | ATTRIBUTE24 | — | — |
| 18 | CostOrgBookPEOAttribute25 | ATTRIBUTE25 | — | — |
| 19 | CostOrgBookPEOAttribute26 | ATTRIBUTE26 | — | — |
| 20 | CostOrgBookPEOAttribute27 | ATTRIBUTE27 | — | — |
| 21 | CostOrgBookPEOAttribute28 | ATTRIBUTE28 | — | — |
| 22 | CostOrgBookPEOAttribute29 | ATTRIBUTE29 | — | — |
| 23 | CostOrgBookPEOAttribute3 | ATTRIBUTE3 | — | — |
| 24 | CostOrgBookPEOAttribute30 | ATTRIBUTE30 | — | — |
| 25 | CostOrgBookPEOAttribute4 | ATTRIBUTE4 | — | — |
| 26 | CostOrgBookPEOAttribute5 | ATTRIBUTE5 | — | — |
| 27 | CostOrgBookPEOAttribute6 | ATTRIBUTE6 | — | — |
| 28 | CostOrgBookPEOAttribute7 | ATTRIBUTE7 | — | — |
| 29 | CostOrgBookPEOAttribute8 | ATTRIBUTE8 | — | — |
| 30 | CostOrgBookPEOAttribute9 | ATTRIBUTE9 | — | — |
| 31 | CostOrgBookPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 32 | CostOrgBookPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 33 | CostOrgBookPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 34 | CostOrgBookPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 35 | CostOrgBookPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 36 | CostOrgBookPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 37 | CostOrgBookPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 38 | CostOrgBookPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 39 | CostOrgBookPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 40 | CostOrgBookPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 41 | CostOrgBookPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 42 | CostOrgBookPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 43 | CostOrgBookPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 44 | CostOrgBookPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 45 | CostOrgBookPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 46 | CostOrgBookPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 47 | CostOrgBookPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 48 | CostOrgBookPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 49 | CostOrgBookPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 50 | CostOrgBookPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 51 | CostOrgBookPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 52 | CostOrgBookPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 53 | CostOrgBookPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 54 | CostOrgBookPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 55 | CostOrgBookPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 56 | CostOrgBookPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 57 | CostOrgBookPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 58 | CostOrgBookPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 59 | CostOrgBookPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 60 | CostOrgBookPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 61 | CostOrgBookPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 62 | CostOrgBookPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 63 | CostOrgBookPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 64 | CostOrgBookPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 65 | CostOrgBookPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 66 | CostOrgBookPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 67 | CostOrgBookPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 68 | CostOrgBookPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 69 | CostOrgBookPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 70 | CostOrgBookPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 71 | CostOrgBookPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 72 | CostOrgBookPEOCalendarId | CALENDAR_ID | — | — |
| 73 | CostOrgBookPEOConversionType | CONVERSION_TYPE | — | — |
| 74 | CostOrgBookPEOCostBookId | COST_BOOK_ID | — | — |
| 75 | CostOrgBookPEOCostOrgId | COST_ORG_ID | — | — |
| 76 | CostOrgBookPEOCreateAccountingFlag | CREATE_ACCOUNTING_FLAG | — | — |
| 77 | CostOrgBookPEOCreatedBy | CREATED_BY | — | — |
| 78 | CostOrgBookPEOCreationDate | CREATION_DATE | — | — |
| 79 | CostOrgBookPEOCurrencyCode | CURRENCY_CODE | — | — |
| 80 | CostOrgBookPEOFirstLedgerPeriodName | FIRST_LEDGER_PERIOD_NAME | — | — |
| 81 | CostOrgBookPEOFromDate | FROM_DATE | — | — |
| 82 | CostOrgBookPEOInactiveDate | INACTIVE_DATE | — | — |
| 83 | CostOrgBookPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 84 | CostOrgBookPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 85 | CostOrgBookPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 86 | CostOrgBookPEOLedgerId | LEDGER_ID | — | — |
| 87 | CostOrgBookPEOMaintainTransactionsFlag | MAINTAIN_TRANSACTIONS_FLAG | — | — |
| 88 | CostOrgBookPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 89 | CostOrgBookPEOOpenPeriodsNum | OPEN_PERIODS_NUM | — | — |
| 90 | CostOrgBookPEOPrimaryBookFlag | PRIMARY_BOOK_FLAG | — | — |
| 91 | CostOrgBookPEOToDate | TO_DATE | — | — |

### [[cst_cost_org_parameters|CST_COST_ORG_PARAMETERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostOrgParametersPEOCostOrgId | COST_ORG_ID | — | — |
| 2 | CostOrgParametersPEOCreatedBy | CREATED_BY | — | — |
| 3 | CostOrgParametersPEOCreationDate | CREATION_DATE | — | — |
| 4 | CostOrgParametersPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 5 | CostOrgParametersPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | CostOrgParametersPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | CostOrgParametersPEOMasterOrganizationId | MASTER_ORGANIZATION_ID | — | — |
| 8 | CostOrgParametersPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | CostOrgParametersPEOStdCostApprovalFlag | STD_COST_APPROVAL_FLAG | — | — |
| 10 | CostOrgParametersPEOValidationOrganizationId | VALIDATION_ORGANIZATION_ID | — | — |

### [[cst_rollup_det_otbi_v|CST_ROLLUP_DET_OTBI_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ScenarioRollupDetailPEOAllocatedExtendedCost | ALLOCATED_EXTENDED_COST | — | ✅ |
| 2 | ScenarioRollupDetailPEOAllocatedUnitCost | ALLOCATED_UNIT_COST | — | ✅ |
| 3 | ScenarioRollupDetailPEOBasisType | BASIS_TYPE | — | — |
| 4 | ScenarioRollupDetailPEOCostAllocationPercentage | COST_ALLOCATION_PERCENTAGE | — | — |
| 5 | ScenarioRollupDetailPEOCostComponentId | COST_COMPONENT_ID | — | — |
| 6 | ScenarioRollupDetailPEOCostElementId | COST_ELEMENT_ID | — | — |
| 7 | ScenarioRollupDetailPEOCostLevel | COST_LEVEL | — | — |
| 8 | ScenarioRollupDetailPEOCostUomCode | COST_UOM_CODE | — | — |
| 9 | ScenarioRollupDetailPEOCostingBatchOutputSize | COSTING_BATCH_OUTPUT_SIZE | — | — |
| 10 | ScenarioRollupDetailPEOCreatedBy | CREATED_BY | — | — |
| 11 | ScenarioRollupDetailPEOCreationDate | CREATION_DATE | — | — |
| 12 | ScenarioRollupDetailPEOCstOperationId | CST_OPERATION_ID | — | — |
| 13 | ScenarioRollupDetailPEOCumulativeExtendedCost | CUMULATIVE_EXTENDED_COST | — | ✅ |
| 14 | ScenarioRollupDetailPEOCumulativeUnitCost | CUMULATIVE_UNIT_COST | — | — |
| 15 | ScenarioRollupDetailPEOExpensePoolId | EXPENSE_POOL_ID | — | — |
| 16 | ScenarioRollupDetailPEOExtendedCost | EXTENDED_COST | — | ✅ |
| 17 | ScenarioRollupDetailPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 18 | ScenarioRollupDetailPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 19 | ScenarioRollupDetailPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 20 | ScenarioRollupDetailPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | ScenarioRollupDetailPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 22 | ScenarioRollupDetailPEOMaterialInventoryItemId | MATERIAL_INVENTORY_ITEM_ID | — | — |
| 23 | ScenarioRollupDetailPEOMaterialInventoryOrgId | MATERIAL_INVENTORY_ORG_ID | — | — |
| 24 | ScenarioRollupDetailPEOOutputInventoryItemId | OUTPUT_INVENTORY_ITEM_ID | — | — |
| 25 | ScenarioRollupDetailPEOOutputInventoryOrgId | OUTPUT_INVENTORY_ORG_ID | — | — |
| 26 | ScenarioRollupDetailPEOOverheadFlag | OVERHEAD_FLAG | — | ✅ |
| 27 | ScenarioRollupDetailPEOOverheadRateId | OVERHEAD_RATE_ID | — | — |
| 28 | ScenarioRollupDetailPEOQtyUomCode | QTY_UOM_CODE | — | — |
| 29 | ScenarioRollupDetailPEOQuantityUsage | QUANTITY_USAGE | — | — |
| 30 | ScenarioRollupDetailPEORequestId | REQUEST_ID | — | — |
| 31 | ScenarioRollupDetailPEOResourceId | RESOURCE_ID | — | — |
| 32 | ScenarioRollupDetailPEOResourceSeqNumber | RESOURCE_SEQ_NUMBER | — | — |
| 33 | ScenarioRollupDetailPEORunningExtendedTotal | RUNNING_EXTENDED_TOTAL | — | — |
| 34 | ScenarioRollupDetailPEORunningUnitTotal | RUNNING_UNIT_TOTAL | — | — |
| 35 | ScenarioRollupDetailPEOScenarioRollupDetailId | SCENARIO_ROLLUP_DETAIL_ID | — | — |
| 36 | ScenarioRollupDetailPEOScenarioRollupHeaderId | SCENARIO_ROLLUP_HEADER_ID | — | — |
| 37 | ScenarioRollupDetailPEOSourceType | SOURCE_TYPE | — | — |
| 38 | ScenarioRollupDetailPEOUnallocatedExtendedCost | UNALLOCATED_EXTENDED_COST | — | ✅ |
| 39 | ScenarioRollupDetailPEOUnallocatedUnitCost | UNALLOCATED_UNIT_COST | — | — |
| 40 | ScenarioRollupDetailPEOUnitCost | UNIT_COST | — | ✅ |
| 41 | ScenarioRollupDetailPEOWdOperationId | WD_OPERATION_ID | — | — |
| 42 | ScenarioRollupDetailPEOYieldFactor | YIELD_FACTOR | — | — |

### [[cst_std_overhead_rates|CST_STD_OVERHEAD_RATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OverheadRatesPEOBasisType | BASIS_TYPE | — | ✅ |
| 2 | OverheadRatesPEOCategoryId | CATEGORY_ID | — | — |
| 3 | OverheadRatesPEOCategorySetId | CATEGORY_SET_ID | — | — |
| 4 | OverheadRatesPEOCostBookId | COST_BOOK_ID | — | — |
| 5 | OverheadRatesPEOCostOrgId | COST_ORG_ID | — | — |
| 6 | OverheadRatesPEOCreatedBy | CREATED_BY | — | — |
| 7 | OverheadRatesPEOCreationDate | CREATION_DATE | — | — |
| 8 | OverheadRatesPEOCurrencyCode | CURRENCY_CODE | — | — |
| 9 | OverheadRatesPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 10 | OverheadRatesPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 11 | OverheadRatesPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 12 | OverheadRatesPEOInventoryOrgId | INVENTORY_ORG_ID | — | — |
| 13 | OverheadRatesPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 14 | OverheadRatesPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 15 | OverheadRatesPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 16 | OverheadRatesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | OverheadRatesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | OverheadRatesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | OverheadRatesPEOOverheadRateType | OVERHEAD_RATE_TYPE | — | ✅ |
| 20 | OverheadRatesPEOPreviousEffectiveEndDate | PREVIOUS_EFFECTIVE_END_DATE | — | — |
| 21 | OverheadRatesPEOPreviousEffectiveStartDate | PREVIOUS_EFFECTIVE_START_DATE | — | — |
| 22 | OverheadRatesPEOPreviousStdOverheadRateId | PREVIOUS_STD_OVERHEAD_RATE_ID | — | — |
| 23 | OverheadRatesPEORequestId | REQUEST_ID | — | — |
| 24 | OverheadRatesPEOResourceType | RESOURCE_TYPE | — | ✅ |
| 25 | OverheadRatesPEOScenarioEventId | SCENARIO_EVENT_ID | — | — |
| 26 | OverheadRatesPEOScenarioId | SCENARIO_ID | — | — |
| 27 | OverheadRatesPEOSourceDi | SOURCE_DI | — | — |
| 28 | OverheadRatesPEOStatusCode | STATUS_CODE | — | — |
| 29 | OverheadRatesPEOStdOverheadRateId | STD_OVERHEAD_RATE_ID | — | — |
| 30 | OverheadRatesPEOTotalRate | TOTAL_RATE | — | — |
| 31 | OverheadRatesPEOWorkCenterId | WORK_CENTER_ID | — | — |

### [[cst_std_overhead_rate_details|CST_STD_OVERHEAD_RATE_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OverheadRateDetailsPEOAbsorptionType | ABSORPTION_TYPE | — | ✅ |
| 2 | OverheadRateDetailsPEOCostElementId | COST_ELEMENT_ID | — | — |
| 3 | OverheadRateDetailsPEOCreatedBy | CREATED_BY | — | — |
| 4 | OverheadRateDetailsPEOCreationDate | CREATION_DATE | — | — |
| 5 | OverheadRateDetailsPEOExpensePoolId | EXPENSE_POOL_ID | — | — |
| 6 | OverheadRateDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | OverheadRateDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | OverheadRateDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | OverheadRateDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | OverheadRateDetailsPEOStdOverheadRateDetailId | STD_OVERHEAD_RATE_DETAIL_ID | — | — |
| 11 | OverheadRateDetailsPEOStdOverheadRateId | STD_OVERHEAD_RATE_ID | — | — |
| 12 | OverheadRateDetailsPEOUnitRate | UNIT_RATE | — | ✅ |

### [[cst_where_used_rollup_dtls_v|CST_WHERE_USED_ROLLUP_DTLS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Rollupkey | ROLLUPKEY | 🔑 | ✅ |
| 2 | WhereUsedRollupDetailPEOAllocatedExtendedCost | ALLOCATED_EXTENDED_COST | — | ✅ |
| 3 | WhereUsedRollupDetailPEOAllocatedUnitCost | ALLOCATED_UNIT_COST | — | ✅ |
| 4 | WhereUsedRollupDetailPEOAssemblyItemId | ASSEMBLY_ITEM_ID | — | — |
| 5 | WhereUsedRollupDetailPEOBasisType | BASIS_TYPE | — | ✅ |
| 6 | WhereUsedRollupDetailPEOBatchPrimaryUomCode | BATCH_PRIMARY_UOM_CODE | — | ✅ |
| 7 | WhereUsedRollupDetailPEOBatchQuantity | BATCH_QUANTITY | — | ✅ |
| 8 | WhereUsedRollupDetailPEOBatchUomCode | BATCH_UOM_CODE | — | ✅ |
| 9 | WhereUsedRollupDetailPEOBomLevel | BOM_LEVEL | — | ✅ |
| 10 | WhereUsedRollupDetailPEOCompCostUomCode | COMP_COST_UOM_CODE | — | — |
| 11 | WhereUsedRollupDetailPEOCostAllocationPercentage | COST_ALLOCATION_PERCENTAGE | — | ✅ |
| 12 | WhereUsedRollupDetailPEOCostBookId | COST_BOOK_ID | — | — |
| 13 | WhereUsedRollupDetailPEOCostEffectiveEndDate | COST_EFFECTIVE_END_DATE | — | ✅ |
| 14 | WhereUsedRollupDetailPEOCostEffectiveStartDate | COST_EFFECTIVE_START_DATE | — | ✅ |
| 15 | WhereUsedRollupDetailPEOCostOrgId | COST_ORG_ID | — | — |
| 16 | WhereUsedRollupDetailPEOCostUomCode | COST_UOM_CODE | — | ✅ |
| 17 | WhereUsedRollupDetailPEOCostUomConversionFactor | COST_UOM_CONVERSION_FACTOR | — | — |
| 18 | WhereUsedRollupDetailPEOCostingBatchOutputSize | COSTING_BATCH_OUTPUT_SIZE | — | ✅ |
| 19 | WhereUsedRollupDetailPEOCostingPriority | COSTING_PRIORITY | — | ✅ |
| 20 | WhereUsedRollupDetailPEOCumulativeExtendedCost | CUMULATIVE_EXTENDED_COST | — | ✅ |
| 21 | WhereUsedRollupDetailPEOCumulativeUnitCost | CUMULATIVE_UNIT_COST | — | ✅ |
| 22 | WhereUsedRollupDetailPEOCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | — |
| 23 | WhereUsedRollupDetailPEODetailSourceType | DETAIL_SOURCE_TYPE | — | ✅ |
| 24 | WhereUsedRollupDetailPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 25 | WhereUsedRollupDetailPEOExtendedCost | EXTENDED_COST | — | ✅ |
| 26 | WhereUsedRollupDetailPEOInvOrgId | INV_ORG_ID | — | — |
| 27 | WhereUsedRollupDetailPEOMaterialInventoryItemId | MATERIAL_INVENTORY_ITEM_ID | — | — |
| 28 | WhereUsedRollupDetailPEOMaterialInventoryOrgId | MATERIAL_INVENTORY_ORG_ID | — | — |
| 29 | WhereUsedRollupDetailPEOOrganizationId | ORGANIZATION_ID | — | — |
| 30 | WhereUsedRollupDetailPEOOrigOutputType | ORIG_OUTPUT_TYPE | — | ✅ |
| 31 | WhereUsedRollupDetailPEOOutputInventoryItemId | OUTPUT_INVENTORY_ITEM_ID | — | — |
| 32 | WhereUsedRollupDetailPEOOutputType | OUTPUT_TYPE | — | ✅ |
| 33 | WhereUsedRollupDetailPEOPoLineLocationId | PO_LINE_LOCATION_ID | — | — |
| 34 | WhereUsedRollupDetailPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 35 | WhereUsedRollupDetailPEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 36 | WhereUsedRollupDetailPEOPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 37 | WhereUsedRollupDetailPEOProductionPriority | PRODUCTION_PRIORITY | — | ✅ |
| 38 | WhereUsedRollupDetailPEOPublishedFlag | PUBLISHED_FLAG | — | ✅ |
| 39 | WhereUsedRollupDetailPEOQtyUomCode | QTY_UOM_CODE | — | ✅ |
| 40 | WhereUsedRollupDetailPEOQuantityUsage | QUANTITY_USAGE | — | ✅ |
| 41 | WhereUsedRollupDetailPEOResourceId | RESOURCE_ID | — | — |
| 42 | WhereUsedRollupDetailPEOResourceSeqNumber | RESOURCE_SEQ_NUMBER | — | ✅ |
| 43 | WhereUsedRollupDetailPEORollupHeaderKey | ROLLUP_HEADER_KEY | — | — |
| 44 | WhereUsedRollupDetailPEORollupHeaderLevel | ROLLUP_HEADER_LEVEL | — | — |
| 45 | WhereUsedRollupDetailPEORollupHeaderType | ROLLUP_HEADER_TYPE | — | — |
| 46 | WhereUsedRollupDetailPEORootMaterialItemId | ROOT_MATERIAL_ITEM_ID | — | — |
| 47 | WhereUsedRollupDetailPEORootResourceId | ROOT_RESOURCE_ID | — | — |
| 48 | WhereUsedRollupDetailPEOScenarioEventId | SCENARIO_EVENT_ID | — | — |
| 49 | WhereUsedRollupDetailPEOScenarioId | SCENARIO_ID | — | — |
| 50 | WhereUsedRollupDetailPEOScenarioRollupHeaderId | SCENARIO_ROLLUP_HEADER_ID | — | — |
| 51 | WhereUsedRollupDetailPEOSourceId | SOURCE_ID | — | — |
| 52 | WhereUsedRollupDetailPEOSourceType | SOURCE_TYPE | — | — |
| 53 | WhereUsedRollupDetailPEOStatusCode | STATUS_CODE | — | ✅ |
| 54 | WhereUsedRollupDetailPEOUnallocatedExtendedCost | UNALLOCATED_EXTENDED_COST | — | ✅ |
| 55 | WhereUsedRollupDetailPEOUnallocatedUnitCost | UNALLOCATED_UNIT_COST | — | — |
| 56 | WhereUsedRollupDetailPEOUnitCost | UNIT_COST | — | ✅ |
| 57 | WhereUsedRollupDetailPEOValUnitId | VAL_UNIT_ID | — | — |
| 58 | WhereUsedRollupDetailPEOVersionNumber | VERSION_NUMBER | — | ✅ |
| 59 | WhereUsedRollupDetailPEOWdCostingBatchOutputSize | WD_COSTING_BATCH_OUTPUT_SIZE | — | — |
| 60 | WhereUsedRollupDetailPEOWdOperationId | WD_OPERATION_ID | — | — |
| 61 | WhereUsedRollupDetailPEOWorkDefinitionId | WORK_DEFINITION_ID | — | — |
| 62 | WhereUsedRollupDetailPEOWorkDefinitionNameId | WORK_DEFINITION_NAME_ID | — | — |
| 63 | WhereUsedRollupDetailPEOWorkDefinitionType | WORK_DEFINITION_TYPE | — | ✅ |
| 64 | WhereUsedRollupDetailPEOWorkMethodCode | WORK_METHOD_CODE | — | ✅ |
| 65 | WhereUsedRollupDetailPEOWorkMethodId | WORK_METHOD_ID | — | ✅ |
| 66 | WhereUsedRollupDetailPEOWorkMethodName | WORK_METHOD_NAME | — | ✅ |
| 67 | WhereUsedRollupDetailPEOWorkOrderId | WORK_ORDER_ID | — | — |
| 68 | WhereUsedRollupDetailPEOYieldFactor | YIELD_FACTOR | — | ✅ |

### [[po_headers_all|PO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PoHeadersAllAcceptanceDueDate | ACCEPTANCE_DUE_DATE | — | — |
| 2 | PoHeadersAllAcceptanceRequiredFlag | ACCEPTANCE_REQUIRED_FLAG | — | — |
| 3 | PoHeadersAllAcceptanceWithinDays | ACCEPTANCE_WITHIN_DAYS | — | — |
| 4 | PoHeadersAllActiveVersionFlag | ACTIVE_VERSION_FLAG | — | — |
| 5 | PoHeadersAllAgentId | AGENT_ID | — | — |
| 6 | PoHeadersAllAgingOnsetPoint | AGING_ONSET_POINT | — | — |
| 7 | PoHeadersAllAgingPeriodDays | AGING_PERIOD_DAYS | — | — |
| 8 | PoHeadersAllAmountLimit | AMOUNT_LIMIT | — | — |
| 9 | PoHeadersAllAmountReleased | AMOUNT_RELEASED | — | — |
| 10 | PoHeadersAllApprovedDate | APPROVED_DATE | — | — |
| 11 | PoHeadersAllApprovedFlag | APPROVED_FLAG | — | — |
| 12 | PoHeadersAllAttribute1 | ATTRIBUTE1 | — | — |
| 13 | PoHeadersAllAttribute10 | ATTRIBUTE10 | — | — |
| 14 | PoHeadersAllAttribute11 | ATTRIBUTE11 | — | — |
| 15 | PoHeadersAllAttribute12 | ATTRIBUTE12 | — | — |
| 16 | PoHeadersAllAttribute13 | ATTRIBUTE13 | — | — |
| 17 | PoHeadersAllAttribute14 | ATTRIBUTE14 | — | — |
| 18 | PoHeadersAllAttribute15 | ATTRIBUTE15 | — | — |
| 19 | PoHeadersAllAttribute16 | ATTRIBUTE16 | — | — |
| 20 | PoHeadersAllAttribute17 | ATTRIBUTE17 | — | — |
| 21 | PoHeadersAllAttribute18 | ATTRIBUTE18 | — | — |
| 22 | PoHeadersAllAttribute19 | ATTRIBUTE19 | — | — |
| 23 | PoHeadersAllAttribute2 | ATTRIBUTE2 | — | — |
| 24 | PoHeadersAllAttribute20 | ATTRIBUTE20 | — | — |
| 25 | PoHeadersAllAttribute3 | ATTRIBUTE3 | — | — |
| 26 | PoHeadersAllAttribute4 | ATTRIBUTE4 | — | — |
| 27 | PoHeadersAllAttribute5 | ATTRIBUTE5 | — | — |
| 28 | PoHeadersAllAttribute6 | ATTRIBUTE6 | — | — |
| 29 | PoHeadersAllAttribute7 | ATTRIBUTE7 | — | — |
| 30 | PoHeadersAllAttribute8 | ATTRIBUTE8 | — | — |
| 31 | PoHeadersAllAttribute9 | ATTRIBUTE9 | — | — |
| 32 | PoHeadersAllAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 33 | PoHeadersAllAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 34 | PoHeadersAllAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 35 | PoHeadersAllAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 36 | PoHeadersAllAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 37 | PoHeadersAllAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 38 | PoHeadersAllAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 39 | PoHeadersAllAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 40 | PoHeadersAllAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 41 | PoHeadersAllAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 42 | PoHeadersAllAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 43 | PoHeadersAllAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 44 | PoHeadersAllAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 45 | PoHeadersAllAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 46 | PoHeadersAllAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 47 | PoHeadersAllAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 48 | PoHeadersAllAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 49 | PoHeadersAllAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 50 | PoHeadersAllAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 51 | PoHeadersAllAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 52 | PoHeadersAllAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 53 | PoHeadersAllAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 54 | PoHeadersAllAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 55 | PoHeadersAllAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 56 | PoHeadersAllAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 57 | PoHeadersAllAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 58 | PoHeadersAllAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 59 | PoHeadersAllAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 60 | PoHeadersAllAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 61 | PoHeadersAllAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 62 | PoHeadersAllAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 63 | PoHeadersAllAutoSourcingFlag | AUTO_SOURCING_FLAG | — | — |
| 64 | PoHeadersAllBillToLocationId | BILL_TO_LOCATION_ID | — | — |
| 65 | PoHeadersAllBillingCycleClosingDate | BILLING_CYCLE_CLOSING_DATE | — | — |
| 66 | PoHeadersAllBilltoBuId | BILLTO_BU_ID | — | — |
| 67 | PoHeadersAllBlanketTotalAmount | BLANKET_TOTAL_AMOUNT | — | — |
| 68 | PoHeadersAllBudgetControlEnabledFlag | BUDGET_CONTROL_ENABLED_FLAG | — | — |
| 69 | PoHeadersAllBuyerManagedTransportFlag | BUYER_MANAGED_TRANSPORT_FLAG | — | — |
| 70 | PoHeadersAllCancelFlag | CANCEL_FLAG | — | — |
| 71 | PoHeadersAllCarrierId | CARRIER_ID | — | — |
| 72 | PoHeadersAllCatAdminAuthEnabledFlag | CAT_ADMIN_AUTH_ENABLED_FLAG | — | — |
| 73 | PoHeadersAllCbcAccountingDate | CBC_ACCOUNTING_DATE | — | — |
| 74 | PoHeadersAllChangeRequestedBy | CHANGE_REQUESTED_BY | — | — |
| 75 | PoHeadersAllChangeSummary | CHANGE_SUMMARY | — | — |
| 76 | PoHeadersAllClosedDate | CLOSED_DATE | — | — |
| 77 | PoHeadersAllClosedDateTime | CLOSED_DATE | — | — |
| 78 | PoHeadersAllComments | COMMENTS | — | — |
| 79 | PoHeadersAllConfirmingOrderFlag | CONFIRMING_ORDER_FLAG | — | — |
| 80 | PoHeadersAllConsignedConsumptionFlag | CONSIGNED_CONSUMPTION_FLAG | — | — |
| 81 | PoHeadersAllConsumeReqDemandFlag | CONSUME_REQ_DEMAND_FLAG | — | — |
| 82 | PoHeadersAllConsumptionAdviceFrequency | CONSUMPTION_ADVICE_FREQUENCY | — | — |
| 83 | PoHeadersAllConsumptionAdviceSummary | CONSUMPTION_ADVICE_SUMMARY | — | — |
| 84 | PoHeadersAllContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 85 | PoHeadersAllContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 86 | PoHeadersAllContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 87 | PoHeadersAllCpaReference | CPA_REFERENCE | — | — |
| 88 | PoHeadersAllCreatedBy | CREATED_BY | — | — |
| 89 | PoHeadersAllCreatedLanguage | CREATED_LANGUAGE | — | — |
| 90 | PoHeadersAllCreationDate | CREATION_DATE | — | — |
| 91 | PoHeadersAllCurrencyCode1 | CURRENCY_CODE | — | ✅ |
| 92 | PoHeadersAllCurrentVersionId | CURRENT_VERSION_ID | — | — |
| 93 | PoHeadersAllDefaultConsignmentLineFlag | DEFAULT_CONSIGNMENT_LINE_FLAG | — | — |
| 94 | PoHeadersAllDefaultPoTradeOrgId | DEFAULT_PO_TRADE_ORG_ID | — | — |
| 95 | PoHeadersAllDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 96 | PoHeadersAllDisableAutosourcingFlag | DISABLE_AUTOSOURCING_FLAG | — | — |
| 97 | PoHeadersAllDocumentCreationMethod | DOCUMENT_CREATION_METHOD | — | ✅ |
| 98 | PoHeadersAllDocumentStatus | DOCUMENT_STATUS | — | — |
| 99 | PoHeadersAllEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 100 | PoHeadersAllEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 101 | PoHeadersAllEmailAddress | EMAIL_ADDRESS | — | — |
| 102 | PoHeadersAllEnabledFlag | ENABLED_FLAG | — | — |
| 103 | PoHeadersAllEncumbranceRequiredFlag | ENCUMBRANCE_REQUIRED_FLAG | — | — |
| 104 | PoHeadersAllEndDate1 | END_DATE | — | — |
| 105 | PoHeadersAllFax | FAX | — | — |
| 106 | PoHeadersAllFirmDate | FIRM_DATE | — | — |
| 107 | PoHeadersAllFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 108 | PoHeadersAllFirstPtyRegId | FIRST_PTY_REG_ID | — | — |
| 109 | PoHeadersAllFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 110 | PoHeadersAllFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 111 | PoHeadersAllFromHeaderId | FROM_HEADER_ID | — | — |
| 112 | PoHeadersAllFromTypeLookupCode | FROM_TYPE_LOOKUP_CODE | — | — |
| 113 | PoHeadersAllFrozenFlag | FROZEN_FLAG | — | — |
| 114 | PoHeadersAllFundsStatus | FUNDS_STATUS | — | — |
| 115 | PoHeadersAllGenerateOrdersAutomatic | GENERATE_ORDERS_AUTOMATIC | — | — |
| 116 | PoHeadersAllGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 117 | PoHeadersAllGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 118 | PoHeadersAllGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 119 | PoHeadersAllGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 120 | PoHeadersAllGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 121 | PoHeadersAllGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 122 | PoHeadersAllGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 123 | PoHeadersAllGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 124 | PoHeadersAllGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 125 | PoHeadersAllGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 126 | PoHeadersAllGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 127 | PoHeadersAllGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 128 | PoHeadersAllGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 129 | PoHeadersAllGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 130 | PoHeadersAllGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 131 | PoHeadersAllGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 132 | PoHeadersAllGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 133 | PoHeadersAllGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 134 | PoHeadersAllGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 135 | PoHeadersAllGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 136 | PoHeadersAllGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 137 | PoHeadersAllGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 138 | PoHeadersAllGroupRequisitionLines | GROUP_REQUISITION_LINES | — | — |
| 139 | PoHeadersAllGroupRequisitions | GROUP_REQUISITIONS | — | — |
| 140 | PoHeadersAllInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 141 | PoHeadersAllJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 142 | PoHeadersAllJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 143 | PoHeadersAllLastBilledDate | LAST_BILLED_DATE | — | — |
| 144 | PoHeadersAllLastReleaseDate | LAST_RELEASE_DATE | — | — |
| 145 | PoHeadersAllLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 146 | PoHeadersAllLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 147 | PoHeadersAllLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 148 | PoHeadersAllLastUpdatedProgram | LAST_UPDATED_PROGRAM | — | — |
| 149 | PoHeadersAllMergeRequestId | MERGE_REQUEST_ID | — | — |
| 150 | PoHeadersAllMinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 151 | PoHeadersAllModeOfTransport1 | MODE_OF_TRANSPORT | — | — |
| 152 | PoHeadersAllNoteToAuthorizer | NOTE_TO_AUTHORIZER | — | — |
| 153 | PoHeadersAllNoteToReceiver | NOTE_TO_RECEIVER | — | — |
| 154 | PoHeadersAllNoteToVendor | NOTE_TO_VENDOR | — | — |
| 155 | PoHeadersAllObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 156 | PoHeadersAllOrchestrationOrderFlag | ORCHESTRATION_ORDER_FLAG | — | — |
| 157 | PoHeadersAllPayOnCode | PAY_ON_CODE | — | — |
| 158 | PoHeadersAllPayOnUseFlag | PAY_ON_USE_FLAG | — | — |
| 159 | PoHeadersAllPcardId | PCARD_ID | — | — |
| 160 | PoHeadersAllPendingSignatureFlag | PENDING_SIGNATURE_FLAG | — | — |
| 161 | PoHeadersAllPoHeaderId | PO_HEADER_ID | — | ✅ |
| 162 | PoHeadersAllPrcBuId | PRC_BU_ID | — | — |
| 163 | PoHeadersAllPriceUpdateTolerance | PRICE_UPDATE_TOLERANCE | — | — |
| 164 | PoHeadersAllProgramAppName | PROGRAM_APP_NAME | — | — |
| 165 | PoHeadersAllProgramName | PROGRAM_NAME | — | — |
| 166 | PoHeadersAllPunchoutSourcingOnlyFlag | PUNCHOUT_SOURCING_ONLY_FLAG | — | — |
| 167 | PoHeadersAllRate | RATE | — | — |
| 168 | PoHeadersAllRateDate | RATE_DATE | — | — |
| 169 | PoHeadersAllRateType | RATE_TYPE | — | — |
| 170 | PoHeadersAllRebuildIndex | REBUILD_INDEX | — | — |
| 171 | PoHeadersAllReferenceNum | REFERENCE_NUM | — | — |
| 172 | PoHeadersAllReleaseMethod | RELEASE_METHOD | — | — |
| 173 | PoHeadersAllReqBuId | REQ_BU_ID | — | — |
| 174 | PoHeadersAllRequestId | REQUEST_ID | — | — |
| 175 | PoHeadersAllRetroPriceApplyUpdatesFlag | RETRO_PRICE_APPLY_UPDATES_FLAG | — | — |
| 176 | PoHeadersAllRetroPriceCommUpdatesFlag | RETRO_PRICE_COMM_UPDATES_FLAG | — | — |
| 177 | PoHeadersAllRetroPriceInitApprovalFlag | RETRO_PRICE_INIT_APPROVAL_FLAG | — | — |
| 178 | PoHeadersAllRetroPriceOpenOrderFlag | RETRO_PRICE_OPEN_ORDER_FLAG | — | — |
| 179 | PoHeadersAllReviewAutogeneratedReleases | REVIEW_AUTOGENERATED_RELEASES | — | — |
| 180 | PoHeadersAllRevisedDate | REVISED_DATE | — | — |
| 181 | PoHeadersAllRevisionNum | REVISION_NUM | — | — |
| 182 | PoHeadersAllSegment1 | SEGMENT1 | — | ✅ |
| 183 | PoHeadersAllSegment2 | SEGMENT2 | — | — |
| 184 | PoHeadersAllSegment3 | SEGMENT3 | — | — |
| 185 | PoHeadersAllSegment4 | SEGMENT4 | — | — |
| 186 | PoHeadersAllSegment5 | SEGMENT5 | — | — |
| 187 | PoHeadersAllServiceLevel | SERVICE_LEVEL | — | — |
| 188 | PoHeadersAllShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 189 | PoHeadersAllShippingControl | SHIPPING_CONTROL | — | — |
| 190 | PoHeadersAllSignatureRequiredFlag | SIGNATURE_REQUIRED_FLAG | — | — |
| 191 | PoHeadersAllSoldtoLeId | SOLDTO_LE_ID | — | — |
| 192 | PoHeadersAllStartDate | START_DATE | — | — |
| 193 | PoHeadersAllStyleId | STYLE_ID | — | — |
| 194 | PoHeadersAllSubmitApprovalAutomatic | SUBMIT_APPROVAL_AUTOMATIC | — | — |
| 195 | PoHeadersAllSubmitDate | SUBMIT_DATE | — | — |
| 196 | PoHeadersAllSummaryFlag | SUMMARY_FLAG | — | — |
| 197 | PoHeadersAllSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | — |
| 198 | PoHeadersAllTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 199 | PoHeadersAllTaxDocumentSubtype | TAX_DOCUMENT_SUBTYPE | — | — |
| 200 | PoHeadersAllTermsId1 | TERMS_ID | — | — |
| 201 | PoHeadersAllThirdPtyRegId | THIRD_PTY_REG_ID | — | — |
| 202 | PoHeadersAllTypeLookupCode | TYPE_LOOKUP_CODE | — | — |
| 203 | PoHeadersAllUpdateSourcingRulesFlag | UPDATE_SOURCING_RULES_FLAG | — | — |
| 204 | PoHeadersAllUseNeedByDate | USE_NEED_BY_DATE | — | — |
| 205 | PoHeadersAllUseSalesOrderNumberFlag | USE_SALES_ORDER_NUMBER_FLAG | — | — |
| 206 | PoHeadersAllUseShipTo | USE_SHIP_TO | — | — |
| 207 | PoHeadersAllVendorContactId | VENDOR_CONTACT_ID | — | — |
| 208 | PoHeadersAllVendorId | VENDOR_ID | — | — |
| 209 | PoHeadersAllVendorOrderNum | VENDOR_ORDER_NUM | — | — |
| 210 | PoHeadersAllVendorSiteId | VENDOR_SITE_ID | — | — |
| 211 | PoHeadersAllXmlChangeSendDate | XML_CHANGE_SEND_DATE | — | — |
| 212 | PoHeadersAllXmlFlag | XML_FLAG | — | — |
| 213 | PoHeadersAllXmlSendDate | XML_SEND_DATE | — | — |

### [[po_lines_all|PO_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PoLinesAllAgingPeriodDays | AGING_PERIOD_DAYS | — | — |
| 2 | PoLinesAllAllowDescriptionUpdateFlag | ALLOW_DESCRIPTION_UPDATE_FLAG | — | — |
| 3 | PoLinesAllAllowPriceOverrideFlag | ALLOW_PRICE_OVERRIDE_FLAG | — | — |
| 4 | PoLinesAllAmount | AMOUNT | — | — |
| 5 | PoLinesAllAmountReleased | AMOUNT_RELEASED | — | — |
| 6 | PoLinesAllAttribute1 | ATTRIBUTE1 | — | — |
| 7 | PoLinesAllAttribute10 | ATTRIBUTE10 | — | — |
| 8 | PoLinesAllAttribute11 | ATTRIBUTE11 | — | — |
| 9 | PoLinesAllAttribute12 | ATTRIBUTE12 | — | — |
| 10 | PoLinesAllAttribute13 | ATTRIBUTE13 | — | — |
| 11 | PoLinesAllAttribute14 | ATTRIBUTE14 | — | — |
| 12 | PoLinesAllAttribute15 | ATTRIBUTE15 | — | — |
| 13 | PoLinesAllAttribute16 | ATTRIBUTE16 | — | — |
| 14 | PoLinesAllAttribute17 | ATTRIBUTE17 | — | — |
| 15 | PoLinesAllAttribute18 | ATTRIBUTE18 | — | — |
| 16 | PoLinesAllAttribute19 | ATTRIBUTE19 | — | — |
| 17 | PoLinesAllAttribute2 | ATTRIBUTE2 | — | — |
| 18 | PoLinesAllAttribute20 | ATTRIBUTE20 | — | — |
| 19 | PoLinesAllAttribute3 | ATTRIBUTE3 | — | — |
| 20 | PoLinesAllAttribute4 | ATTRIBUTE4 | — | — |
| 21 | PoLinesAllAttribute5 | ATTRIBUTE5 | — | — |
| 22 | PoLinesAllAttribute6 | ATTRIBUTE6 | — | — |
| 23 | PoLinesAllAttribute7 | ATTRIBUTE7 | — | — |
| 24 | PoLinesAllAttribute8 | ATTRIBUTE8 | — | — |
| 25 | PoLinesAllAttribute9 | ATTRIBUTE9 | — | — |
| 26 | PoLinesAllAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 27 | PoLinesAllAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 28 | PoLinesAllAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 29 | PoLinesAllAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 30 | PoLinesAllAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 31 | PoLinesAllAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 32 | PoLinesAllAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 33 | PoLinesAllAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 34 | PoLinesAllAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 35 | PoLinesAllAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 36 | PoLinesAllAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 37 | PoLinesAllAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 38 | PoLinesAllAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 39 | PoLinesAllAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 40 | PoLinesAllAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 41 | PoLinesAllAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 42 | PoLinesAllAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 43 | PoLinesAllAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 44 | PoLinesAllAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 45 | PoLinesAllAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 46 | PoLinesAllAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 47 | PoLinesAllAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 48 | PoLinesAllAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 49 | PoLinesAllAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 50 | PoLinesAllAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 51 | PoLinesAllAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 52 | PoLinesAllAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 53 | PoLinesAllAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 54 | PoLinesAllAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 55 | PoLinesAllAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 56 | PoLinesAllAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 57 | PoLinesAllAuctionDisplayNumber | AUCTION_DISPLAY_NUMBER | — | — |
| 58 | PoLinesAllAuctionHeaderId | AUCTION_HEADER_ID | — | — |
| 59 | PoLinesAllAuctionLineNumber | AUCTION_LINE_NUMBER | — | — |
| 60 | PoLinesAllBaseModelId | BASE_MODEL_ID | — | — |
| 61 | PoLinesAllBaseModelPrice | BASE_MODEL_PRICE | — | — |
| 62 | PoLinesAllBaseQty | BASE_QTY | — | — |
| 63 | PoLinesAllBaseUnitPrice | BASE_UNIT_PRICE | — | — |
| 64 | PoLinesAllBaseUom | BASE_UOM | — | — |
| 65 | PoLinesAllBidLineNumber | BID_LINE_NUMBER | — | — |
| 66 | PoLinesAllBidNumber | BID_NUMBER | — | — |
| 67 | PoLinesAllCancelDate | CANCEL_DATE | — | — |
| 68 | PoLinesAllCancelFlag | CANCEL_FLAG | — | — |
| 69 | PoLinesAllCancelReason | CANCEL_REASON | — | — |
| 70 | PoLinesAllCancelledBy | CANCELLED_BY | — | — |
| 71 | PoLinesAllCapitalExpenseFlag | CAPITAL_EXPENSE_FLAG | — | — |
| 72 | PoLinesAllCategoryId | CATEGORY_ID | — | — |
| 73 | PoLinesAllClosedBy | CLOSED_BY | — | — |
| 74 | PoLinesAllClosedDate | CLOSED_DATE | — | — |
| 75 | PoLinesAllClosedReason | CLOSED_REASON | — | — |
| 76 | PoLinesAllCommittedAmount | COMMITTED_AMOUNT | — | — |
| 77 | PoLinesAllConfiguredItemFlag | CONFIGURED_ITEM_FLAG | — | — |
| 78 | PoLinesAllConsignmentLineFlag | CONSIGNMENT_LINE_FLAG | — | — |
| 79 | PoLinesAllContractId | CONTRACT_ID | — | — |
| 80 | PoLinesAllContractorFirstName | CONTRACTOR_FIRST_NAME | — | — |
| 81 | PoLinesAllContractorLastName | CONTRACTOR_LAST_NAME | — | — |
| 82 | PoLinesAllCreatedBy4 | CREATED_BY | — | — |
| 83 | PoLinesAllCreationDate4 | CREATION_DATE | — | — |
| 84 | PoLinesAllExpirationDate | EXPIRATION_DATE | — | — |
| 85 | PoLinesAllFirmDate | FIRM_DATE | — | — |
| 86 | PoLinesAllFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 87 | PoLinesAllFromHeaderId | FROM_HEADER_ID | — | — |
| 88 | PoLinesAllFromLineId | FROM_LINE_ID | — | — |
| 89 | PoLinesAllFromLineLocationId | FROM_LINE_LOCATION_ID | — | — |
| 90 | PoLinesAllFundsStatus | FUNDS_STATUS | — | — |
| 91 | PoLinesAllGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 92 | PoLinesAllGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 93 | PoLinesAllGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 94 | PoLinesAllGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 95 | PoLinesAllGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 96 | PoLinesAllGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 97 | PoLinesAllGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 98 | PoLinesAllGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 99 | PoLinesAllGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 100 | PoLinesAllGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 101 | PoLinesAllGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 102 | PoLinesAllGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 103 | PoLinesAllGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 104 | PoLinesAllGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 105 | PoLinesAllGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 106 | PoLinesAllGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 107 | PoLinesAllGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 108 | PoLinesAllGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 109 | PoLinesAllGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 110 | PoLinesAllGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 111 | PoLinesAllGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 112 | PoLinesAllGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 113 | PoLinesAllHazardClassId | HAZARD_CLASS_ID | — | — |
| 114 | PoLinesAllItemDescription | ITEM_DESCRIPTION | — | — |
| 115 | PoLinesAllItemId | ITEM_ID | — | — |
| 116 | PoLinesAllItemRevision | ITEM_REVISION | — | — |
| 117 | PoLinesAllJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 118 | PoLinesAllJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 119 | PoLinesAllJobId | JOB_ID | — | — |
| 120 | PoLinesAllLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 121 | PoLinesAllLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 122 | PoLinesAllLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 123 | PoLinesAllLastUpdatedProgram | LAST_UPDATED_PROGRAM | — | — |
| 124 | PoLinesAllLineNum | LINE_NUM | — | ✅ |
| 125 | PoLinesAllLineReferenceNum | LINE_REFERENCE_NUM | — | — |
| 126 | PoLinesAllLineStatus | LINE_STATUS | — | ✅ |
| 127 | PoLinesAllLineTypeId | LINE_TYPE_ID | — | — |
| 128 | PoLinesAllListPricePerUnit | LIST_PRICE_PER_UNIT | — | — |
| 129 | PoLinesAllManualPriceChangeFlag1 | MANUAL_PRICE_CHANGE_FLAG | — | — |
| 130 | PoLinesAllMarketPrice | MARKET_PRICE | — | — |
| 131 | PoLinesAllMatchingBasis | MATCHING_BASIS | — | — |
| 132 | PoLinesAllMaxRetainageAmount | MAX_RETAINAGE_AMOUNT | — | — |
| 133 | PoLinesAllMinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 134 | PoLinesAllNegotiatedByPreparerFlag | NEGOTIATED_BY_PREPARER_FLAG | — | — |
| 135 | PoLinesAllNextConsumptionAdvGenDate | NEXT_CONSUMPTION_ADV_GEN_DATE | — | — |
| 136 | PoLinesAllNotToExceedPrice | NOT_TO_EXCEED_PRICE | — | — |
| 137 | PoLinesAllNoteToVendor | NOTE_TO_VENDOR | — | — |
| 138 | PoLinesAllObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 139 | PoLinesAllOkeContractHeaderId | OKE_CONTRACT_HEADER_ID | — | — |
| 140 | PoLinesAllOkeContractVersionId | OKE_CONTRACT_VERSION_ID | — | — |
| 141 | PoLinesAllOptionsPrice | OPTIONS_PRICE | — | — |
| 142 | PoLinesAllOrderTypeLookupCode | ORDER_TYPE_LOOKUP_CODE | — | — |
| 143 | PoLinesAllOverToleranceErrorFlag | OVER_TOLERANCE_ERROR_FLAG | — | — |
| 144 | PoLinesAllPJC_CONTEXT_CATEGORY | PJC_CONTEXT_CATEGORY | — | — |
| 145 | PoLinesAllParentItemId | PARENT_ITEM_ID | — | — |
| 146 | PoLinesAllPoHeaderId | PO_HEADER_ID | — | — |
| 147 | PoLinesAllPoLineId | PO_LINE_ID | — | ✅ |
| 148 | PoLinesAllPrcBuId | PRC_BU_ID | — | — |
| 149 | PoLinesAllPreferredGrade | PREFERRED_GRADE | — | — |
| 150 | PoLinesAllPriceBreakLookupCode | PRICE_BREAK_LOOKUP_CODE | — | — |
| 151 | PoLinesAllPriceTypeLookupCode | PRICE_TYPE_LOOKUP_CODE | — | — |
| 152 | PoLinesAllProgramAppName | PROGRAM_APP_NAME | — | — |
| 153 | PoLinesAllProgramName | PROGRAM_NAME | — | — |
| 154 | PoLinesAllProgressPaymentRate | PROGRESS_PAYMENT_RATE | — | — |
| 155 | PoLinesAllPurchaseBasis | PURCHASE_BASIS | — | — |
| 156 | PoLinesAllQcGrade | QC_GRADE | — | — |
| 157 | PoLinesAllQtyRcvTolerance | QTY_RCV_TOLERANCE | — | — |
| 158 | PoLinesAllQuantity | QUANTITY | — | — |
| 159 | PoLinesAllQuantityCommitted | QUANTITY_COMMITTED | — | — |
| 160 | PoLinesAllRecoupmentRate | RECOUPMENT_RATE | — | — |
| 161 | PoLinesAllReferenceNum | REFERENCE_NUM | — | — |
| 162 | PoLinesAllReqBuId | REQ_BU_ID | — | — |
| 163 | PoLinesAllRequestId | REQUEST_ID | — | — |
| 164 | PoLinesAllRetainageRate | RETAINAGE_RATE | — | — |
| 165 | PoLinesAllRetroactiveDate | RETROACTIVE_DATE | — | — |
| 166 | PoLinesAllSecondaryQuantity | SECONDARY_QUANTITY | — | — |
| 167 | PoLinesAllSecondaryUomCode | SECONDARY_UOM_CODE | — | — |
| 168 | PoLinesAllSourceDocRevNum | SOURCE_DOC_REV_NUM | — | — |
| 169 | PoLinesAllStartDate | START_DATE | — | — |
| 170 | PoLinesAllSupplierParentItem | SUPPLIER_PARENT_ITEM | — | — |
| 171 | PoLinesAllSupplierPartAuxid | SUPPLIER_PART_AUXID | — | — |
| 172 | PoLinesAllSupplierRefNumber | SUPPLIER_REF_NUMBER | — | — |
| 173 | PoLinesAllSupplierTopModel | SUPPLIER_TOP_MODEL | — | — |
| 174 | PoLinesAllSvcAmountNotifSent | SVC_AMOUNT_NOTIF_SENT | — | — |
| 175 | PoLinesAllSvcCompletionNotifSent | SVC_COMPLETION_NOTIF_SENT | — | — |
| 176 | PoLinesAllTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 177 | PoLinesAllTaxCodeId | TAX_CODE_ID | — | — |
| 178 | PoLinesAllTaxExclusivePrice | TAX_EXCLUSIVE_PRICE | — | — |
| 179 | PoLinesAllTaxName1 | TAX_NAME | — | — |
| 180 | PoLinesAllTaxableFlag | TAXABLE_FLAG | — | — |
| 181 | PoLinesAllTopModelId | TOP_MODEL_ID | — | — |
| 182 | PoLinesAllType1099 | TYPE_1099 | — | — |
| 183 | PoLinesAllUnNumberId | UN_NUMBER_ID | — | — |
| 184 | PoLinesAllUnitPrice | UNIT_PRICE | — | ✅ |
| 185 | PoLinesAllUnorderedFlag | UNORDERED_FLAG | — | — |
| 186 | PoLinesAllUomCode | UOM_CODE | — | ✅ |
| 187 | PoLinesAllVendorProductNum | VENDOR_PRODUCT_NUM | — | — |
| 188 | PoLinesAllWorkOrderProduct | WORK_ORDER_PRODUCT | — | — |

### [[po_line_locations_all|PO_LINE_LOCATIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PoLineLocationsAllAccrueOnReceiptFlag | ACCRUE_ON_RECEIPT_FLAG | — | — |
| 2 | PoLineLocationsAllAllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | — |
| 3 | PoLineLocationsAllAmount | AMOUNT | — | — |
| 4 | PoLineLocationsAllAmountAccepted | AMOUNT_ACCEPTED | — | — |
| 5 | PoLineLocationsAllAmountBilled | AMOUNT_BILLED | — | — |
| 6 | PoLineLocationsAllAmountCancelled | AMOUNT_CANCELLED | — | — |
| 7 | PoLineLocationsAllAmountFinanced | AMOUNT_FINANCED | — | — |
| 8 | PoLineLocationsAllAmountReceived | AMOUNT_RECEIVED | — | — |
| 9 | PoLineLocationsAllAmountRecouped | AMOUNT_RECOUPED | — | — |
| 10 | PoLineLocationsAllAmountRejected | AMOUNT_REJECTED | — | — |
| 11 | PoLineLocationsAllAmountShipped | AMOUNT_SHIPPED | — | — |
| 12 | PoLineLocationsAllAnticipatedArrivalDate | ANTICIPATED_ARRIVAL_DATE | — | — |
| 13 | PoLineLocationsAllAssessableValue | ASSESSABLE_VALUE | — | — |
| 14 | PoLineLocationsAllAttribute1 | ATTRIBUTE1 | — | — |
| 15 | PoLineLocationsAllAttribute10 | ATTRIBUTE10 | — | — |
| 16 | PoLineLocationsAllAttribute11 | ATTRIBUTE11 | — | — |
| 17 | PoLineLocationsAllAttribute12 | ATTRIBUTE12 | — | — |
| 18 | PoLineLocationsAllAttribute13 | ATTRIBUTE13 | — | — |
| 19 | PoLineLocationsAllAttribute14 | ATTRIBUTE14 | — | — |
| 20 | PoLineLocationsAllAttribute15 | ATTRIBUTE15 | — | — |
| 21 | PoLineLocationsAllAttribute16 | ATTRIBUTE16 | — | — |
| 22 | PoLineLocationsAllAttribute17 | ATTRIBUTE17 | — | — |
| 23 | PoLineLocationsAllAttribute18 | ATTRIBUTE18 | — | — |
| 24 | PoLineLocationsAllAttribute19 | ATTRIBUTE19 | — | — |
| 25 | PoLineLocationsAllAttribute2 | ATTRIBUTE2 | — | — |
| 26 | PoLineLocationsAllAttribute20 | ATTRIBUTE20 | — | — |
| 27 | PoLineLocationsAllAttribute3 | ATTRIBUTE3 | — | — |
| 28 | PoLineLocationsAllAttribute4 | ATTRIBUTE4 | — | — |
| 29 | PoLineLocationsAllAttribute5 | ATTRIBUTE5 | — | — |
| 30 | PoLineLocationsAllAttribute6 | ATTRIBUTE6 | — | — |
| 31 | PoLineLocationsAllAttribute7 | ATTRIBUTE7 | — | — |
| 32 | PoLineLocationsAllAttribute8 | ATTRIBUTE8 | — | — |
| 33 | PoLineLocationsAllAttribute9 | ATTRIBUTE9 | — | — |
| 34 | PoLineLocationsAllAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 35 | PoLineLocationsAllAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 36 | PoLineLocationsAllAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 37 | PoLineLocationsAllAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 38 | PoLineLocationsAllAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 39 | PoLineLocationsAllAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 40 | PoLineLocationsAllAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 41 | PoLineLocationsAllAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 42 | PoLineLocationsAllAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 43 | PoLineLocationsAllAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 44 | PoLineLocationsAllAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 45 | PoLineLocationsAllAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 46 | PoLineLocationsAllAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 47 | PoLineLocationsAllAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 48 | PoLineLocationsAllAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 49 | PoLineLocationsAllAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 50 | PoLineLocationsAllAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 51 | PoLineLocationsAllAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 52 | PoLineLocationsAllAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 53 | PoLineLocationsAllAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 54 | PoLineLocationsAllAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 55 | PoLineLocationsAllAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 56 | PoLineLocationsAllAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 57 | PoLineLocationsAllAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 58 | PoLineLocationsAllAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 59 | PoLineLocationsAllAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 60 | PoLineLocationsAllAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 61 | PoLineLocationsAllAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 62 | PoLineLocationsAllAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 63 | PoLineLocationsAllAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 64 | PoLineLocationsAllAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 65 | PoLineLocationsAllAutoClosureMode | AUTO_CLOSURE_MODE | — | — |
| 66 | PoLineLocationsAllBackToBackFlag | BACK_TO_BACK_FLAG | — | — |
| 67 | PoLineLocationsAllBidPaymentId | BID_PAYMENT_ID | — | — |
| 68 | PoLineLocationsAllCalculateTaxFlag | CALCULATE_TAX_FLAG | — | — |
| 69 | PoLineLocationsAllCancelBudgetDate | CANCEL_BUDGET_DATE | — | — |
| 70 | PoLineLocationsAllCancelDate | CANCEL_DATE | — | — |
| 71 | PoLineLocationsAllCancelFlag | CANCEL_FLAG | — | — |
| 72 | PoLineLocationsAllCancelReason | CANCEL_REASON | — | — |
| 73 | PoLineLocationsAllCancelledBy | CANCELLED_BY | — | — |
| 74 | PoLineLocationsAllCarrierId | CARRIER_ID | — | — |
| 75 | PoLineLocationsAllChangePromisedDateReason | CHANGE_PROMISED_DATE_REASON | — | — |
| 76 | PoLineLocationsAllClosedBy | CLOSED_BY | — | — |
| 77 | PoLineLocationsAllClosedDate | CLOSED_DATE | — | — |
| 78 | PoLineLocationsAllClosedDateTime | CLOSED_DATE | — | — |
| 79 | PoLineLocationsAllClosedForInvoiceDate | CLOSED_FOR_INVOICE_DATE | — | — |
| 80 | PoLineLocationsAllClosedForReceivingDate | CLOSED_FOR_RECEIVING_DATE | — | — |
| 81 | PoLineLocationsAllClosedReason | CLOSED_REASON | — | — |
| 82 | PoLineLocationsAllConsignedFlag | CONSIGNED_FLAG | — | — |
| 83 | PoLineLocationsAllCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | — |
| 84 | PoLineLocationsAllCreatedBy | CREATED_BY | — | — |
| 85 | PoLineLocationsAllCreationDate | CREATION_DATE | — | — |
| 86 | PoLineLocationsAllCustomerItem | CUSTOMER_ITEM | — | — |
| 87 | PoLineLocationsAllCustomerItemDesc | CUSTOMER_ITEM_DESC | — | — |
| 88 | PoLineLocationsAllCustomerPoLineNumber | CUSTOMER_PO_LINE_NUMBER | — | — |
| 89 | PoLineLocationsAllCustomerPoNumber | CUSTOMER_PO_NUMBER | — | — |
| 90 | PoLineLocationsAllCustomerPoScheduleNumber | CUSTOMER_PO_SCHEDULE_NUMBER | — | — |
| 91 | PoLineLocationsAllDaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | — |
| 92 | PoLineLocationsAllDaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | — |
| 93 | PoLineLocationsAllDescription | DESCRIPTION | — | — |
| 94 | PoLineLocationsAllDestinationTypeCode | DESTINATION_TYPE_CODE | — | — |
| 95 | PoLineLocationsAllDropShipFlag | DROP_SHIP_FLAG | — | — |
| 96 | PoLineLocationsAllEncumberNow | ENCUMBER_NOW | — | — |
| 97 | PoLineLocationsAllEncumberedDate | ENCUMBERED_DATE | — | — |
| 98 | PoLineLocationsAllEncumberedFlag | ENCUMBERED_FLAG | — | — |
| 99 | PoLineLocationsAllEndDate | END_DATE | — | — |
| 100 | PoLineLocationsAllEnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | — |
| 101 | PoLineLocationsAllEstimatedTaxAmount | ESTIMATED_TAX_AMOUNT | — | — |
| 102 | PoLineLocationsAllFinalDischargeLocationId | FINAL_DISCHARGE_LOCATION_ID | — | — |
| 103 | PoLineLocationsAllFinalMatchFlag | FINAL_MATCH_FLAG | — | — |
| 104 | PoLineLocationsAllFirmDate | FIRM_DATE | — | — |
| 105 | PoLineLocationsAllFirmFlag | FIRM_FLAG | — | — |
| 106 | PoLineLocationsAllFirmReason | FIRM_REASON | — | — |
| 107 | PoLineLocationsAllFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 108 | PoLineLocationsAllFirmedBy | FIRMED_BY | — | — |
| 109 | PoLineLocationsAllFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 110 | PoLineLocationsAllFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 111 | PoLineLocationsAllFromHeaderId | FROM_HEADER_ID | — | — |
| 112 | PoLineLocationsAllFromLineId | FROM_LINE_ID | — | — |
| 113 | PoLineLocationsAllFromLineLocationId | FROM_LINE_LOCATION_ID | — | — |
| 114 | PoLineLocationsAllFundsStatus | FUNDS_STATUS | — | — |
| 115 | PoLineLocationsAllGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 116 | PoLineLocationsAllGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 117 | PoLineLocationsAllGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 118 | PoLineLocationsAllGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 119 | PoLineLocationsAllGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 120 | PoLineLocationsAllGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 121 | PoLineLocationsAllGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 122 | PoLineLocationsAllGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 123 | PoLineLocationsAllGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 124 | PoLineLocationsAllGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 125 | PoLineLocationsAllGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 126 | PoLineLocationsAllGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 127 | PoLineLocationsAllGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 128 | PoLineLocationsAllGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 129 | PoLineLocationsAllGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 130 | PoLineLocationsAllGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 131 | PoLineLocationsAllGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 132 | PoLineLocationsAllGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 133 | PoLineLocationsAllGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 134 | PoLineLocationsAllGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 135 | PoLineLocationsAllGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 136 | PoLineLocationsAllGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 137 | PoLineLocationsAllGroupName | GROUP_NAME | — | — |
| 138 | PoLineLocationsAllInputTaxClassificationCode | INPUT_TAX_CLASSIFICATION_CODE | — | — |
| 139 | PoLineLocationsAllInspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | — |
| 140 | PoLineLocationsAllInvoiceCloseTolerance | INVOICE_CLOSE_TOLERANCE | — | — |
| 141 | PoLineLocationsAllJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 142 | PoLineLocationsAllJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 143 | PoLineLocationsAllLastAcceptDate | LAST_ACCEPT_DATE | — | — |
| 144 | PoLineLocationsAllLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 145 | PoLineLocationsAllLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 146 | PoLineLocationsAllLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 147 | PoLineLocationsAllLeadTime | LEAD_TIME | — | — |
| 148 | PoLineLocationsAllLeadTimeUnit | LEAD_TIME_UNIT | — | — |
| 149 | PoLineLocationsAllLineIntendedUse | LINE_INTENDED_USE | — | — |
| 150 | PoLineLocationsAllLineIntendedUseId | LINE_INTENDED_USE_ID | — | — |
| 151 | PoLineLocationsAllLineLocationId | LINE_LOCATION_ID | — | ✅ |
| 152 | PoLineLocationsAllManualPriceChangeFlag | MANUAL_PRICE_CHANGE_FLAG | — | — |
| 153 | PoLineLocationsAllMatchOption | MATCH_OPTION | — | — |
| 154 | PoLineLocationsAllMatchingBasis | MATCHING_BASIS | — | — |
| 155 | PoLineLocationsAllModeOfTransport | MODE_OF_TRANSPORT | — | — |
| 156 | PoLineLocationsAllNeedByDate | NEED_BY_DATE | — | — |
| 157 | PoLineLocationsAllNoteToReceiver | NOTE_TO_RECEIVER | — | — |
| 158 | PoLineLocationsAllObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 159 | PoLineLocationsAllOrchestrationCode | ORCHESTRATION_CODE | — | — |
| 160 | PoLineLocationsAllOriginalShipmentId | ORIGINAL_SHIPMENT_ID | — | — |
| 161 | PoLineLocationsAllOutsourcedAssembly | OUTSOURCED_ASSEMBLY | — | — |
| 162 | PoLineLocationsAllPJC_CONTEXT_CATEGORY | PJC_CONTEXT_CATEGORY | — | — |
| 163 | PoLineLocationsAllPaymentType | PAYMENT_TYPE | — | — |
| 164 | PoLineLocationsAllPoHeaderId | PO_HEADER_ID | — | — |
| 165 | PoLineLocationsAllPoLineId | PO_LINE_ID | — | — |
| 166 | PoLineLocationsAllPoLineLocationsAllQuantity | QUANTITY | — | — |
| 167 | PoLineLocationsAllPoTradingOrganizationId | PO_TRADING_ORGANIZATION_ID | — | — |
| 168 | PoLineLocationsAllPrcBuId | PRC_BU_ID | — | — |
| 169 | PoLineLocationsAllPreferredGrade | PREFERRED_GRADE | — | — |
| 170 | PoLineLocationsAllPriceDiscount | PRICE_DISCOUNT | — | — |
| 171 | PoLineLocationsAllPriceOverride | PRICE_OVERRIDE | — | ✅ |
| 172 | PoLineLocationsAllProductCategory | PRODUCT_CATEGORY | — | — |
| 173 | PoLineLocationsAllProductFiscClassId | PRODUCT_FISC_CLASS_ID | — | — |
| 174 | PoLineLocationsAllProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | — |
| 175 | PoLineLocationsAllProductType | PRODUCT_TYPE | — | — |
| 176 | PoLineLocationsAllProgramAppName | PROGRAM_APP_NAME | — | — |
| 177 | PoLineLocationsAllProgramName | PROGRAM_NAME | — | — |
| 178 | PoLineLocationsAllPromisedDate | PROMISED_DATE | — | — |
| 179 | PoLineLocationsAllPromisedShipDate | PROMISED_SHIP_DATE | — | — |
| 180 | PoLineLocationsAllQtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | — |
| 181 | PoLineLocationsAllQtyRcvTolerance | QTY_RCV_TOLERANCE | — | — |
| 182 | PoLineLocationsAllQuantityAccepted | QUANTITY_ACCEPTED | — | — |
| 183 | PoLineLocationsAllQuantityBilled | QUANTITY_BILLED | — | — |
| 184 | PoLineLocationsAllQuantityCancelled | QUANTITY_CANCELLED | — | — |
| 185 | PoLineLocationsAllQuantityFinanced | QUANTITY_FINANCED | — | — |
| 186 | PoLineLocationsAllQuantityReceived | QUANTITY_RECEIVED | — | — |
| 187 | PoLineLocationsAllQuantityRecouped | QUANTITY_RECOUPED | — | — |
| 188 | PoLineLocationsAllQuantityRejected | QUANTITY_REJECTED | — | — |
| 189 | PoLineLocationsAllQuantityShipped | QUANTITY_SHIPPED | — | — |
| 190 | PoLineLocationsAllReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | — |
| 191 | PoLineLocationsAllReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 192 | PoLineLocationsAllReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | — |
| 193 | PoLineLocationsAllReceivingRoutingId | RECEIVING_ROUTING_ID | — | — |
| 194 | PoLineLocationsAllReopenFinalCloseDate | REOPEN_FINAL_CLOSE_DATE | — | — |
| 195 | PoLineLocationsAllReqBuId | REQ_BU_ID | — | — |
| 196 | PoLineLocationsAllRequestId | REQUEST_ID | — | — |
| 197 | PoLineLocationsAllRequestedShipDate | REQUESTED_SHIP_DATE | — | — |
| 198 | PoLineLocationsAllRetainageReleasedAmount | RETAINAGE_RELEASED_AMOUNT | — | — |
| 199 | PoLineLocationsAllRetainageWithheldAmount | RETAINAGE_WITHHELD_AMOUNT | — | — |
| 200 | PoLineLocationsAllRetroactiveDate | RETROACTIVE_DATE | — | — |
| 201 | PoLineLocationsAllSalesOrderLineNumber | SALES_ORDER_LINE_NUMBER | — | — |
| 202 | PoLineLocationsAllSalesOrderNumber | SALES_ORDER_NUMBER | — | — |
| 203 | PoLineLocationsAllSalesOrderScheduleNumber | SALES_ORDER_SCHEDULE_NUMBER | — | — |
| 204 | PoLineLocationsAllSalesOrderUpdateDate | SALES_ORDER_UPDATE_DATE | — | — |
| 205 | PoLineLocationsAllScheduleStatus | SCHEDULE_STATUS | — | ✅ |
| 206 | PoLineLocationsAllSecondaryQuantity | SECONDARY_QUANTITY | — | — |
| 207 | PoLineLocationsAllSecondaryQuantityAccepted | SECONDARY_QUANTITY_ACCEPTED | — | — |
| 208 | PoLineLocationsAllSecondaryQuantityCancelled | SECONDARY_QUANTITY_CANCELLED | — | — |
| 209 | PoLineLocationsAllSecondaryQuantityReceived | SECONDARY_QUANTITY_RECEIVED | — | — |
| 210 | PoLineLocationsAllSecondaryQuantityRejected | SECONDARY_QUANTITY_REJECTED | — | — |
| 211 | PoLineLocationsAllSecondaryQuantityShipped | SECONDARY_QUANTITY_SHIPPED | — | — |
| 212 | PoLineLocationsAllSecondaryUomCode | SECONDARY_UOM_CODE | — | — |
| 213 | PoLineLocationsAllServiceLevel | SERVICE_LEVEL | — | — |
| 214 | PoLineLocationsAllSfoAgreementLineNumber | SFO_AGREEMENT_LINE_NUMBER | — | — |
| 215 | PoLineLocationsAllSfoAgreementNumber | SFO_AGREEMENT_NUMBER | — | — |
| 216 | PoLineLocationsAllSfoPtrId | SFO_PTR_ID | — | — |
| 217 | PoLineLocationsAllShipToCustContactId | SHIP_TO_CUST_CONTACT_ID | — | — |
| 218 | PoLineLocationsAllShipToCustId | SHIP_TO_CUST_ID | — | — |
| 219 | PoLineLocationsAllShipToCustLocationId | SHIP_TO_CUST_LOCATION_ID | — | — |
| 220 | PoLineLocationsAllShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 221 | PoLineLocationsAllShipToOrganizationId | SHIP_TO_ORGANIZATION_ID | — | — |
| 222 | PoLineLocationsAllShipmentClosedDate | SHIPMENT_CLOSED_DATE | — | — |
| 223 | PoLineLocationsAllShipmentNum | SHIPMENT_NUM | — | ✅ |
| 224 | PoLineLocationsAllShipmentType | SHIPMENT_TYPE | — | ✅ |
| 225 | PoLineLocationsAllSourceShipmentId | SOURCE_SHIPMENT_ID | — | — |
| 226 | PoLineLocationsAllStartDate | START_DATE | — | — |
| 227 | PoLineLocationsAllSupplierOrderLineNumber | SUPPLIER_ORDER_LINE_NUMBER | — | — |
| 228 | PoLineLocationsAllTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 229 | PoLineLocationsAllTaxCodeId | TAX_CODE_ID | — | — |
| 230 | PoLineLocationsAllTaxName | TAX_NAME | — | — |
| 231 | PoLineLocationsAllTaxUserOverrideFlag | TAX_USER_OVERRIDE_FLAG | — | — |
| 232 | PoLineLocationsAllTaxableFlag | TAXABLE_FLAG | — | — |
| 233 | PoLineLocationsAllTermsId | TERMS_ID | — | — |
| 234 | PoLineLocationsAllTransactionFlowHeaderId | TRANSACTION_FLOW_HEADER_ID | — | — |
| 235 | PoLineLocationsAllTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 236 | PoLineLocationsAllUnencumberedQuantity | UNENCUMBERED_QUANTITY | — | — |
| 237 | PoLineLocationsAllUnitOfMeasureClass | UNIT_OF_MEASURE_CLASS | — | — |
| 238 | PoLineLocationsAllUomCode | UOM_CODE | — | — |
| 239 | PoLineLocationsAllUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 240 | PoLineLocationsAllValueBasis | VALUE_BASIS | — | — |
| 241 | PoLineLocationsAllVmiFlag | VMI_FLAG | — | — |
| 242 | PoLineLocationsAllWorkApproverId | WORK_APPROVER_ID | — | — |
| 243 | PoLineLocationsAllWorkOrderId | WORK_ORDER_ID | — | — |
| 244 | PoLineLocationsAllWorkOrderNumber | WORK_ORDER_NUMBER | — | — |
| 245 | PoLineLocationsAllWorkOrderOperationId | WORK_ORDER_OPERATION_ID | — | — |
| 246 | PoLineLocationsAllWorkOrderOperationSeq | WORK_ORDER_OPERATION_SEQ | — | — |
| 247 | PoLineLocationsAllWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
