---
id: DOC-OTHER-PVO-CstWorkOrderCostsPVO
doc_type: system-doc
title: "CstWorkOrderCostsPVO — PVO Cross-Module"
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
  - CstWorkOrderCostsPVO
  - cstworkordercostspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstWorkOrderCostsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Work Order Costs. Acessa as tabelas: CST_ALL_COST_TRANSACTIONS_V, CST_COST_ORGS_V, CST_COST_ORG_BOOKS (+10).

**Caminho:** `FscmTopModelAM.WorkOrderCostAM.CstWorkOrderCostsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 205 | 13 | 1 | 87 | 42% |

---

## 🔗 Tabelas Relacionadas

- [[cst_all_cost_transactions_v|CST_ALL_COST_TRANSACTIONS_V]] — 73 atributos (2 BICC)
- [[cst_cost_orgs_v|CST_COST_ORGS_V]] — 5 atributos (5 BICC)
- [[cst_cost_org_books|CST_COST_ORG_BOOKS]] — 7 atributos (3 BICC)
- [[cst_work_orders|CST_WORK_ORDERS]] — 37 atributos (28 BICC)
- [[cst_work_order_costs|CST_WORK_ORDER_COSTS]] — 30 atributos (1 PKs, 27 BICC)
- [[cst_work_order_operations|CST_WORK_ORDER_OPERATIONS]] — 18 atributos (9 BICC)
- [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]] — 3 atributos
- [[gl_calendars|GL_CALENDARS]] — 6 atributos (6 BICC)
- [[inv_org_parameters|INV_ORG_PARAMETERS]] — 2 atributos (1 BICC)
- [[wie_work_orders_b|WIE_WORK_ORDERS_B]] — 2 atributos (1 BICC)
- [[wie_wo_assets|WIE_WO_ASSETS]] — 13 atributos (3 BICC)
- [[wis_wd_versions|WIS_WD_VERSIONS]] — 2 atributos (1 BICC)
- [[wis_work_centers_vl|WIS_WORK_CENTERS_VL]] — 7 atributos (1 BICC)

---

## ⚙️ Atributos

### [[cst_all_cost_transactions_v|CST_ALL_COST_TRANSACTIONS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostAllTransactionsVPEOAccountingStatus | ACCOUNTING_STATUS | — | ✅ |
| 2 | CostAllTransactionsVPEOBaseTxnActionId | BASE_TXN_ACTION_ID | — | — |
| 3 | CostAllTransactionsVPEOBaseTxnSourceTypeId | BASE_TXN_SOURCE_TYPE_ID | — | — |
| 4 | CostAllTransactionsVPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | — |
| 5 | CostAllTransactionsVPEOBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 6 | CostAllTransactionsVPEOCogsPercentage | COGS_PERCENTAGE | — | — |
| 7 | CostAllTransactionsVPEOConsignedFlag | CONSIGNED_FLAG | — | — |
| 8 | CostAllTransactionsVPEOCostBookId | COST_BOOK_ID | — | — |
| 9 | CostAllTransactionsVPEOCostDate | COST_DATE | — | — |
| 10 | CostAllTransactionsVPEOCostMethodCode | COST_METHOD_CODE | — | — |
| 11 | CostAllTransactionsVPEOCostOrgId | COST_ORG_ID | — | — |
| 12 | CostAllTransactionsVPEOCostStatus | COST_STATUS | — | — |
| 13 | CostAllTransactionsVPEOCostTransactionType | COST_TRANSACTION_TYPE | — | — |
| 14 | CostAllTransactionsVPEOCreatedBy | CREATED_BY | — | — |
| 15 | CostAllTransactionsVPEOCreationDate | CREATION_DATE | — | — |
| 16 | CostAllTransactionsVPEOCstInvTransactionDtlId | CST_INV_TRANSACTION_DTL_ID | — | — |
| 17 | CostAllTransactionsVPEOCstInvTransactionId | CST_INV_TRANSACTION_ID | — | — |
| 18 | CostAllTransactionsVPEOCstWoOperationTxnId | CST_WO_OPERATION_TXN_ID | — | — |
| 19 | CostAllTransactionsVPEOCstWoResourceTxnId | CST_WO_RESOURCE_TXN_ID | — | — |
| 20 | CostAllTransactionsVPEOCstWorkOrderId | CST_WORK_ORDER_ID | — | — |
| 21 | CostAllTransactionsVPEOCstWorkOrderOperationId | CST_WORK_ORDER_OPERATION_ID | — | — |
| 22 | CostAllTransactionsVPEODeliveryId | DELIVERY_ID | — | — |
| 23 | CostAllTransactionsVPEODooFullfillLineId | DOO_FULLFILL_LINE_ID | — | — |
| 24 | CostAllTransactionsVPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | — |
| 25 | CostAllTransactionsVPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 26 | CostAllTransactionsVPEOFiscalDocAccessKnum | FISCAL_DOC_ACCESS_KNUM | — | — |
| 27 | CostAllTransactionsVPEOFiscalDocHeaderId | FISCAL_DOC_HEADER_ID | — | — |
| 28 | CostAllTransactionsVPEOFiscalDocLineId | FISCAL_DOC_LINE_ID | — | — |
| 29 | CostAllTransactionsVPEOFiscalDocScheduleId | FISCAL_DOC_SCHEDULE_ID | — | — |
| 30 | CostAllTransactionsVPEOFromGradeCode | FROM_GRADE_CODE | — | — |
| 31 | CostAllTransactionsVPEOGradeCode | GRADE_CODE | — | — |
| 32 | CostAllTransactionsVPEOIntransitFlag | INTRANSIT_FLAG | — | — |
| 33 | CostAllTransactionsVPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 34 | CostAllTransactionsVPEOInventoryOrgId | INVENTORY_ORG_ID | — | — |
| 35 | CostAllTransactionsVPEOItemOrganizationId | ITEM_ORGANIZATION_ID | — | — |
| 36 | CostAllTransactionsVPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 37 | CostAllTransactionsVPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 38 | CostAllTransactionsVPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 39 | CostAllTransactionsVPEOLeTimezoneCode | LE_TIMEZONE_CODE | — | — |
| 40 | CostAllTransactionsVPEOLotNumber | LOT_NUMBER | — | — |
| 41 | CostAllTransactionsVPEOParentLotNumber | PARENT_LOT_NUMBER | — | — |
| 42 | CostAllTransactionsVPEOPoDistributionId | PO_DISTRIBUTION_ID | — | — |
| 43 | CostAllTransactionsVPEOQuantity | QUANTITY | — | — |
| 44 | CostAllTransactionsVPEORcvTransactionId | RCV_TRANSACTION_ID | — | — |
| 45 | CostAllTransactionsVPEORefFiscalDocAccessKnum | REF_FISCAL_DOC_ACCESS_KNUM | — | — |
| 46 | CostAllTransactionsVPEORefFiscalDocHeaderId | REF_FISCAL_DOC_HEADER_ID | — | — |
| 47 | CostAllTransactionsVPEORefFiscalDocLineId | REF_FISCAL_DOC_LINE_ID | — | — |
| 48 | CostAllTransactionsVPEORefFiscalDocScheduleId | REF_FISCAL_DOC_SCHEDULE_ID | — | — |
| 49 | CostAllTransactionsVPEOResourceId | RESOURCE_ID | — | — |
| 50 | CostAllTransactionsVPEORevenueLineId | REVENUE_LINE_ID | — | — |
| 51 | CostAllTransactionsVPEORmaTransactionId | RMA_TRANSACTION_ID | — | — |
| 52 | CostAllTransactionsVPEOSerialNumber | SERIAL_NUMBER | — | — |
| 53 | CostAllTransactionsVPEOShipmentFullfillLineId | SHIPMENT_FULLFILL_LINE_ID | — | — |
| 54 | CostAllTransactionsVPEOSourceTable | SOURCE_TABLE | — | — |
| 55 | CostAllTransactionsVPEOSupplyType | SUPPLY_TYPE | — | — |
| 56 | CostAllTransactionsVPEOToGradeCode | TO_GRADE_CODE | — | — |
| 57 | CostAllTransactionsVPEOTransactionDate | TRANSACTION_DATE | — | — |
| 58 | CostAllTransactionsVPEOTransactionFlowType | TRANSACTION_FLOW_TYPE | — | — |
| 59 | CostAllTransactionsVPEOTransactionId | TRANSACTION_ID | — | — |
| 60 | CostAllTransactionsVPEOTransactionQty | TRANSACTION_QTY | — | — |
| 61 | CostAllTransactionsVPEOTransactionReasonId | TRANSACTION_REASON_ID | — | — |
| 62 | CostAllTransactionsVPEOTransferCostOrgId | TRANSFER_COST_ORG_ID | — | — |
| 63 | CostAllTransactionsVPEOTransferCstInvTxnId | TRANSFER_CST_INV_TXN_ID | — | — |
| 64 | CostAllTransactionsVPEOTxnSourceDocNumber | TXN_SOURCE_DOC_NUMBER | — | — |
| 65 | CostAllTransactionsVPEOTxnSourceDocType | TXN_SOURCE_DOC_TYPE | — | — |
| 66 | CostAllTransactionsVPEOTxnSourceRefDocNumber | TXN_SOURCE_REF_DOC_NUMBER | — | — |
| 67 | CostAllTransactionsVPEOTxnSourceRefDocType | TXN_SOURCE_REF_DOC_TYPE | — | — |
| 68 | CostAllTransactionsVPEOUomCode | UOM_CODE | — | — |
| 69 | CostAllTransactionsVPEOValUnitId | VAL_UNIT_ID | — | — |
| 70 | CostAllTransactionsVPEOVendorLotNumber | VENDOR_LOT_NUMBER | — | — |
| 71 | CostAllTransactionsVPEOWoOperationResourceId | WO_OPERATION_RESOURCE_ID | — | — |
| 72 | CostAllTransactionsVPEOWorkCenterId | WORK_CENTER_ID | — | — |
| 73 | CostAllTransactionsVPEOWshDeliveryDetailId | WSH_DELIVERY_DETAIL_ID | — | — |

### [[cst_cost_orgs_v|CST_COST_ORGS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostOrganizationVPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 2 | CostOrganizationVPEOCostOrgName | COST_ORG_NAME | — | ✅ |
| 3 | CostOrganizationVPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 4 | CostOrganizationVPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | CostOrganizationVPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |

### [[cst_cost_org_books|CST_COST_ORG_BOOKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostOrgBookPEOCalendarId | CALENDAR_ID | — | — |
| 2 | CostOrgBookPEOCdConversionType | CD_CONVERSION_TYPE | — | — |
| 3 | CostOrgBookPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 4 | CostOrgBookPEOCostOrgId1 | COST_ORG_ID | — | ✅ |
| 5 | CostOrgBookPEOLedgerId | LEDGER_ID | — | ✅ |
| 6 | CostOrgBookPEOPrimaryBookFlag | PRIMARY_BOOK_FLAG | — | — |
| 7 | CostOrgBookPEOUsdConversionType | USD_CONVERSION_TYPE | — | — |

### [[cst_work_orders|CST_WORK_ORDERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstWorkOrdersPEOClosedDate | CLOSED_DATE | — | ✅ |
| 2 | CstWorkOrdersPEOCompletionDate | COMPLETION_DATE | — | ✅ |
| 3 | CstWorkOrdersPEOContractMfgFlag | CONTRACT_MFG_FLAG | — | ✅ |
| 4 | CstWorkOrdersPEOContractMfgPoLineLocId | CONTRACT_MFG_PO_LINE_LOC_ID | — | ✅ |
| 5 | CstWorkOrdersPEOCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | — |
| 6 | CstWorkOrdersPEOCreatedBy1 | CREATED_BY | — | ✅ |
| 7 | CstWorkOrdersPEOCreationDate1 | CREATION_DATE | — | ✅ |
| 8 | CstWorkOrdersPEOCstWorkOrderId1 | CST_WORK_ORDER_ID | — | ✅ |
| 9 | CstWorkOrdersPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | ✅ |
| 10 | CstWorkOrdersPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | ✅ |
| 11 | CstWorkOrdersPEOInventoryAssetFlag | INVENTORY_ASSET_FLAG | — | ✅ |
| 12 | CstWorkOrdersPEOInventoryItemId1 | INVENTORY_ITEM_ID | — | ✅ |
| 13 | CstWorkOrdersPEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | ✅ |
| 14 | CstWorkOrdersPEOJobDefinitionName1 | JOB_DEFINITION_NAME | — | ✅ |
| 15 | CstWorkOrdersPEOJobDefinitionPackage1 | JOB_DEFINITION_PACKAGE | — | ✅ |
| 16 | CstWorkOrdersPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 17 | CstWorkOrdersPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 18 | CstWorkOrdersPEOReleasedDate | RELEASED_DATE | — | ✅ |
| 19 | CstWorkOrdersPEORequestId1 | REQUEST_ID | — | ✅ |
| 20 | CstWorkOrdersPEOWorkDefinitionAsOfDate | WORK_DEFINITION_AS_OF_DATE | — | ✅ |
| 21 | CstWorkOrdersPEOWorkDefinitionId | WORK_DEFINITION_ID | — | ✅ |
| 22 | CstWorkOrdersPEOWorkDefinitionVersionId | WORK_DEFINITION_VERSION_ID | — | ✅ |
| 23 | CstWorkOrdersPEOWorkMethodId | WORK_METHOD_ID | — | ✅ |
| 24 | CstWorkOrdersPEOWorkOrderLessFlag | WORK_ORDER_LESS_FLAG | — | ✅ |
| 25 | CstWorkOrdersPEOWorkOrderNumber | WORK_ORDER_NUMBER | — | ✅ |
| 26 | CstWorkOrdersPEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | ✅ |
| 27 | CstWorkOrdersPEOWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | ✅ |
| 28 | CstWorkOrdersPEOWorkOrderType | WORK_ORDER_TYPE | — | ✅ |
| 29 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 30 | PJC_CONTRACT_ID | PJC_CONTRACT_ID | — | — |
| 31 | PJC_EXPENDITURE_ITEM_DATE | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 32 | PJC_EXPENDITURE_TYPE_ID | PJC_EXPENDITURE_TYPE_ID | — | — |
| 33 | PJC_ORGANIZATION_ID | PJC_ORGANIZATION_ID | — | — |
| 34 | PJC_PROJECT_ID | PJC_PROJECT_ID | — | — |
| 35 | PJC_RESERVED_ATTRIBUTE1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 36 | PJC_TASK_ID | PJC_TASK_ID | — | — |
| 37 | PJC_WORK_TYPE_ID | PJC_WORK_TYPE_ID | — | — |

### [[cst_work_order_costs|CST_WORK_ORDER_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstWorkOrderCostsPEOAbsorptionType | ABSORPTION_TYPE | — | ✅ |
| 2 | CstWorkOrderCostsPEOCostBookId | COST_BOOK_ID | — | — |
| 3 | CstWorkOrderCostsPEOCostDate | COST_DATE | — | ✅ |
| 4 | CstWorkOrderCostsPEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 5 | CstWorkOrderCostsPEOCostId | COST_ID | — | ✅ |
| 6 | CstWorkOrderCostsPEOCostOrgId | COST_ORG_ID | — | — |
| 7 | CstWorkOrderCostsPEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | CstWorkOrderCostsPEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | CstWorkOrderCostsPEOCstWorkOrderId | CST_WORK_ORDER_ID | — | ✅ |
| 10 | CstWorkOrderCostsPEOCstWorkOrderOperationId | CST_WORK_ORDER_OPERATION_ID | — | ✅ |
| 11 | CstWorkOrderCostsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 12 | CstWorkOrderCostsPEOExpensePoolId | EXPENSE_POOL_ID | — | ✅ |
| 13 | CstWorkOrderCostsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 14 | CstWorkOrderCostsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 15 | CstWorkOrderCostsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 16 | CstWorkOrderCostsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | CstWorkOrderCostsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 18 | CstWorkOrderCostsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | CstWorkOrderCostsPEOPoItemDescription | PO_ITEM_DESCRIPTION | — | — |
| 20 | CstWorkOrderCostsPEOQuantity | QUANTITY | — | ✅ |
| 21 | CstWorkOrderCostsPEORecloseFlag | RECLOSE_FLAG | — | ✅ |
| 22 | CstWorkOrderCostsPEORequestId | REQUEST_ID | — | ✅ |
| 23 | CstWorkOrderCostsPEOResourceId | RESOURCE_ID | — | ✅ |
| 24 | CstWorkOrderCostsPEOSourceTable | SOURCE_TABLE | — | ✅ |
| 25 | CstWorkOrderCostsPEOTransactionId | TRANSACTION_ID | — | ✅ |
| 26 | CstWorkOrderCostsPEOUnitCost | UNIT_COST | — | ✅ |
| 27 | CstWorkOrderCostsPEOUomCode | UOM_CODE | — | ✅ |
| 28 | CstWorkOrderCostsPEOWipCostType | WIP_COST_TYPE | — | ✅ |
| 29 | CstWorkOrderCostsPEOWipTxnSign | WIP_TXN_SIGN | — | ✅ |
| 30 | WorkOrderCostId | WORK_ORDER_COST_ID | 🔑 | ✅ |

### [[cst_work_order_operations|CST_WORK_ORDER_OPERATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstWorkOrderOperationsPEOCreatedBy | CREATED_BY | — | — |
| 2 | CstWorkOrderOperationsPEOCreationDate | CREATION_DATE | — | — |
| 3 | CstWorkOrderOperationsPEOCstWorkOrderId | CST_WORK_ORDER_ID | — | — |
| 4 | CstWorkOrderOperationsPEOCstWorkOrderOperationId | CST_WORK_ORDER_OPERATION_ID | — | — |
| 5 | CstWorkOrderOperationsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 6 | CstWorkOrderOperationsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 7 | CstWorkOrderOperationsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | CstWorkOrderOperationsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | CstWorkOrderOperationsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | CstWorkOrderOperationsPEOOperationSeqNumber | OPERATION_SEQ_NUMBER | — | ✅ |
| 11 | CstWorkOrderOperationsPEOOperationType | OPERATION_TYPE | — | ✅ |
| 12 | CstWorkOrderOperationsPEOOspItemId | OSP_ITEM_ID | — | ✅ |
| 13 | CstWorkOrderOperationsPEORequestId | REQUEST_ID | — | — |
| 14 | CstWorkOrderOperationsPEOSupplierId | SUPPLIER_ID | — | ✅ |
| 15 | CstWorkOrderOperationsPEOSupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 16 | CstWorkOrderOperationsPEOWorkCenterId | WORK_CENTER_ID | — | ✅ |
| 17 | CstWorkOrderOperationsPEOWorkDefinitionOperationId | WORK_DEFINITION_OPERATION_ID | — | ✅ |
| 18 | CstWorkOrderOperationsPEOWorkOrderOperationId | WORK_ORDER_OPERATION_ID | — | ✅ |

### [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemBasePEOBaseItemId | BASE_ITEM_ID | — | — |
| 2 | ItemBasePEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 3 | ItemBasePEOOrganizationId | ORGANIZATION_ID | — | — |

### [[gl_calendars|GL_CALENDARS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CalendarPEOCalendarId | CALENDAR_ID | — | ✅ |
| 2 | CalendarPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 3 | CalendarPEOPeriodSetId | PERIOD_SET_ID | — | ✅ |
| 4 | CalendarPEOPeriodSetName | PERIOD_SET_NAME | — | ✅ |
| 5 | CalendarPEOPeriodType | PERIOD_TYPE | — | ✅ |
| 6 | CalendarPEOPeriodTypeId | PERIOD_TYPE_ID | — | ✅ |

### [[inv_org_parameters|INV_ORG_PARAMETERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemOrganizationParameterPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 2 | ItemOrganizationParameterPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[wie_work_orders_b|WIE_WORK_ORDERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderAnalyticsPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |
| 2 | WorkOrderAnalyticsPEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | — |

### [[wie_wo_assets|WIE_WO_ASSETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderAssetsPEOAssetId | ASSET_ID | — | ✅ |
| 2 | WorkOrderAssetsPEOCreatedBy | CREATED_BY | — | — |
| 3 | WorkOrderAssetsPEOCreationDate | CREATION_DATE | — | — |
| 4 | WorkOrderAssetsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 5 | WorkOrderAssetsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 6 | WorkOrderAssetsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | WorkOrderAssetsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | WorkOrderAssetsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | WorkOrderAssetsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | WorkOrderAssetsPEOOrganizationId | ORGANIZATION_ID | — | — |
| 11 | WorkOrderAssetsPEORequestId | REQUEST_ID | — | — |
| 12 | WorkOrderAssetsPEOWoAssetId | WO_ASSET_ID | — | ✅ |
| 13 | WorkOrderAssetsPEOWorkOrderId | WORK_ORDER_ID | — | — |

### [[wis_wd_versions|WIS_WD_VERSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkDefinitionVersionPEOVersionNumber | VERSION_NUMBER | — | ✅ |
| 2 | WorkDefinitionVersionPEOWorkDefinitionVersionId | WORK_DEFINITION_VERSION_ID | — | — |

### [[wis_work_centers_vl|WIS_WORK_CENTERS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkCenterPEOInactiveDate | INACTIVE_DATE | — | — |
| 2 | WorkCenterPEOOrganizationId | ORGANIZATION_ID | — | — |
| 3 | WorkCenterPEOWorkAreaId | WORK_AREA_ID | — | — |
| 4 | WorkCenterPEOWorkCenterCode | WORK_CENTER_CODE | — | — |
| 5 | WorkCenterPEOWorkCenterDescription | WORK_CENTER_DESCRIPTION | — | ✅ |
| 6 | WorkCenterPEOWorkCenterId | WORK_CENTER_ID | — | — |
| 7 | WorkCenterPEOWorkCenterName | WORK_CENTER_NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
