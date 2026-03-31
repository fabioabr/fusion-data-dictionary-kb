---
id: DOC-OTHER-PVO-CstTransactionsErrorsPVO
doc_type: system-doc
title: "CstTransactionsErrorsPVO — PVO Cross-Module"
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
  - CstTransactionsErrorsPVO
  - csttransactionserrorspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstTransactionsErrorsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Transactions Errors. Acessa as tabelas: CST_ALL_COST_TRANSACTIONS_V, CST_ALL_INTF_TRANSACTIONS_V, CST_COST_ORGS_V (+6).

**Caminho:** `FscmTopModelAM.CstPeriodStatusAM.CstTransactionsErrorsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 400 | 9 | 7 | 391 | 98% |

---

## 🔗 Tabelas Relacionadas

- [[cst_all_cost_transactions_v|CST_ALL_COST_TRANSACTIONS_V]] — 64 atributos (63 BICC)
- [[cst_all_intf_transactions_v|CST_ALL_INTF_TRANSACTIONS_V]] — 21 atributos (21 BICC)
- [[cst_cost_orgs_v|CST_COST_ORGS_V]] — 6 atributos (6 BICC)
- [[cst_cost_org_books|CST_COST_ORG_BOOKS]] — 61 atributos (61 BICC)
- [[cst_cp_errors|CST_CP_ERRORS]] — 32 atributos (32 BICC)
- [[cst_inv_transactions|CST_INV_TRANSACTIONS]] — 127 atributos (127 BICC)
- [[cst_period_close_actions|CST_PERIOD_CLOSE_ACTIONS]] — 42 atributos (34 BICC)
- [[cst_transaction_errors|CST_TRANSACTION_ERRORS]] — 15 atributos (7 PKs, 15 BICC)
- [[gl_calendars|GL_CALENDARS]] — 32 atributos (32 BICC)

---

## ⚙️ Atributos

### [[cst_all_cost_transactions_v|CST_ALL_COST_TRANSACTIONS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostAllTransactionsVPEOAccountingStatus | ACCOUNTING_STATUS | — | ✅ |
| 2 | CostAllTransactionsVPEOBaseTxnActionId | BASE_TXN_ACTION_ID | — | ✅ |
| 3 | CostAllTransactionsVPEOBaseTxnSourceTypeId | BASE_TXN_SOURCE_TYPE_ID | — | ✅ |
| 4 | CostAllTransactionsVPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | ✅ |
| 5 | CostAllTransactionsVPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 6 | CostAllTransactionsVPEOCogsPercentage | COGS_PERCENTAGE | — | ✅ |
| 7 | CostAllTransactionsVPEOConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 8 | CostAllTransactionsVPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 9 | CostAllTransactionsVPEOCostDate | COST_DATE | — | ✅ |
| 10 | CostAllTransactionsVPEOCostMethodCode | COST_METHOD_CODE | — | ✅ |
| 11 | CostAllTransactionsVPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 12 | CostAllTransactionsVPEOCostStatus | COST_STATUS | — | ✅ |
| 13 | CostAllTransactionsVPEOCostTransactionType | COST_TRANSACTION_TYPE | — | ✅ |
| 14 | CostAllTransactionsVPEOCreatedBy1 | CREATED_BY | — | ✅ |
| 15 | CostAllTransactionsVPEOCreationDate1 | CREATION_DATE | — | ✅ |
| 16 | CostAllTransactionsVPEOCstInvTransactionDtlId | CST_INV_TRANSACTION_DTL_ID | — | ✅ |
| 17 | CostAllTransactionsVPEOCstInvTransactionId | CST_INV_TRANSACTION_ID | — | ✅ |
| 18 | CostAllTransactionsVPEOCstWoOperationTxnId | CST_WO_OPERATION_TXN_ID | — | ✅ |
| 19 | CostAllTransactionsVPEOCstWoResourceTxnId | CST_WO_RESOURCE_TXN_ID | — | ✅ |
| 20 | CostAllTransactionsVPEOCstWorkOrderId | CST_WORK_ORDER_ID | — | ✅ |
| 21 | CostAllTransactionsVPEOCstWorkOrderOperationId | CST_WORK_ORDER_OPERATION_ID | — | ✅ |
| 22 | CostAllTransactionsVPEODeliveryId | DELIVERY_ID | — | ✅ |
| 23 | CostAllTransactionsVPEODooFullfillLineId | DOO_FULLFILL_LINE_ID | — | ✅ |
| 24 | CostAllTransactionsVPEOExternalSystemRefId1 | EXTERNAL_SYSTEM_REF_ID | — | ✅ |
| 25 | CostAllTransactionsVPEOFromGradeCode | FROM_GRADE_CODE | — | ✅ |
| 26 | CostAllTransactionsVPEOGradeCode | GRADE_CODE | — | ✅ |
| 27 | CostAllTransactionsVPEOIntransitFlag | INTRANSIT_FLAG | — | ✅ |
| 28 | CostAllTransactionsVPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 29 | CostAllTransactionsVPEOInventoryOrgId | INVENTORY_ORG_ID | — | ✅ |
| 30 | CostAllTransactionsVPEOItemOrganizationId | ITEM_ORGANIZATION_ID | — | — |
| 31 | CostAllTransactionsVPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 32 | CostAllTransactionsVPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 33 | CostAllTransactionsVPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 34 | CostAllTransactionsVPEOLeTimezoneCode | LE_TIMEZONE_CODE | — | ✅ |
| 35 | CostAllTransactionsVPEOLotNumber | LOT_NUMBER | — | ✅ |
| 36 | CostAllTransactionsVPEOParentLotNumber | PARENT_LOT_NUMBER | — | ✅ |
| 37 | CostAllTransactionsVPEOPoDistributionId | PO_DISTRIBUTION_ID | — | ✅ |
| 38 | CostAllTransactionsVPEOQuantity | QUANTITY | — | ✅ |
| 39 | CostAllTransactionsVPEORcvTransactionId | RCV_TRANSACTION_ID | — | ✅ |
| 40 | CostAllTransactionsVPEOResourceId | RESOURCE_ID | — | ✅ |
| 41 | CostAllTransactionsVPEORevenueLineId | REVENUE_LINE_ID | — | ✅ |
| 42 | CostAllTransactionsVPEORmaTransactionId | RMA_TRANSACTION_ID | — | ✅ |
| 43 | CostAllTransactionsVPEOSerialNumber | SERIAL_NUMBER | — | ✅ |
| 44 | CostAllTransactionsVPEOShipmentFullfillLineId | SHIPMENT_FULLFILL_LINE_ID | — | ✅ |
| 45 | CostAllTransactionsVPEOSourceTable | SOURCE_TABLE | — | ✅ |
| 46 | CostAllTransactionsVPEOSupplyType | SUPPLY_TYPE | — | ✅ |
| 47 | CostAllTransactionsVPEOToGradeCode | TO_GRADE_CODE | — | ✅ |
| 48 | CostAllTransactionsVPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 49 | CostAllTransactionsVPEOTransactionFlowType | TRANSACTION_FLOW_TYPE | — | ✅ |
| 50 | CostAllTransactionsVPEOTransactionId1 | TRANSACTION_ID | — | ✅ |
| 51 | CostAllTransactionsVPEOTransactionQty | TRANSACTION_QTY | — | ✅ |
| 52 | CostAllTransactionsVPEOTransactionReasonId | TRANSACTION_REASON_ID | — | ✅ |
| 53 | CostAllTransactionsVPEOTransferCostOrgId | TRANSFER_COST_ORG_ID | — | ✅ |
| 54 | CostAllTransactionsVPEOTransferCstInvTxnId | TRANSFER_CST_INV_TXN_ID | — | ✅ |
| 55 | CostAllTransactionsVPEOTxnSourceDocNumber | TXN_SOURCE_DOC_NUMBER | — | ✅ |
| 56 | CostAllTransactionsVPEOTxnSourceDocType | TXN_SOURCE_DOC_TYPE | — | ✅ |
| 57 | CostAllTransactionsVPEOTxnSourceRefDocNumber | TXN_SOURCE_REF_DOC_NUMBER | — | ✅ |
| 58 | CostAllTransactionsVPEOTxnSourceRefDocType | TXN_SOURCE_REF_DOC_TYPE | — | ✅ |
| 59 | CostAllTransactionsVPEOUomCode | UOM_CODE | — | ✅ |
| 60 | CostAllTransactionsVPEOValUnitId | VAL_UNIT_ID | — | ✅ |
| 61 | CostAllTransactionsVPEOVendorLotNumber | VENDOR_LOT_NUMBER | — | ✅ |
| 62 | CostAllTransactionsVPEOWoOperationResourceId | WO_OPERATION_RESOURCE_ID | — | ✅ |
| 63 | CostAllTransactionsVPEOWorkCenterId | WORK_CENTER_ID | — | ✅ |
| 64 | CostAllTransactionsVPEOWshDeliveryDetailId | WSH_DELIVERY_DETAIL_ID | — | ✅ |

### [[cst_all_intf_transactions_v|CST_ALL_INTF_TRANSACTIONS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstAllIntfTransactionsPEOBaseTxnActionId | BASE_TXN_ACTION_ID | — | ✅ |
| 2 | CstAllIntfTransactionsPEOBaseTxnSourceTypeId | BASE_TXN_SOURCE_TYPE_ID | — | ✅ |
| 3 | CstAllIntfTransactionsPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | ✅ |
| 4 | CstAllIntfTransactionsPEOCreatedBy1 | CREATED_BY | — | ✅ |
| 5 | CstAllIntfTransactionsPEOCreationDate1 | CREATION_DATE | — | ✅ |
| 6 | CstAllIntfTransactionsPEOExternalSystemRefId1 | EXTERNAL_SYSTEM_REF_ID | — | ✅ |
| 7 | CstAllIntfTransactionsPEOExternalSystemReference1 | EXTERNAL_SYSTEM_REFERENCE | — | ✅ |
| 8 | CstAllIntfTransactionsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 9 | CstAllIntfTransactionsPEOInventoryOrgId | INVENTORY_ORG_ID | — | ✅ |
| 10 | CstAllIntfTransactionsPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 11 | CstAllIntfTransactionsPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | CstAllIntfTransactionsPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 13 | CstAllIntfTransactionsPEOQuantity | QUANTITY | — | ✅ |
| 14 | CstAllIntfTransactionsPEOResourceId | RESOURCE_ID | — | ✅ |
| 15 | CstAllIntfTransactionsPEOSourceTable | SOURCE_TABLE | — | ✅ |
| 16 | CstAllIntfTransactionsPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 17 | CstAllIntfTransactionsPEOTxnSourceDocNumber | TXN_SOURCE_DOC_NUMBER | — | ✅ |
| 18 | CstAllIntfTransactionsPEOTxnSourceDocType | TXN_SOURCE_DOC_TYPE | — | ✅ |
| 19 | CstAllIntfTransactionsPEOTxnSourceRefDocNumber | TXN_SOURCE_REF_DOC_NUMBER | — | ✅ |
| 20 | CstAllIntfTransactionsPEOTxnSourceRefDocType | TXN_SOURCE_REF_DOC_TYPE | — | ✅ |
| 21 | CstAllIntfTransactionsPEOUomCode | UOM_CODE | — | ✅ |

### [[cst_cost_orgs_v|CST_COST_ORGS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostOrganizationVPEOCostOrgCode | COST_ORG_CODE | — | ✅ |
| 2 | CostOrganizationVPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 3 | CostOrganizationVPEOCostOrgName | COST_ORG_NAME | — | ✅ |
| 4 | CostOrganizationVPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 5 | CostOrganizationVPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 6 | CostOrganizationVPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |

### [[cst_cost_org_books|CST_COST_ORG_BOOKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostOrgBookPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 2 | CostOrgBookPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 3 | CostOrgBookPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 4 | CostOrgBookPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 5 | CostOrgBookPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 6 | CostOrgBookPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 7 | CostOrgBookPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 8 | CostOrgBookPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 9 | CostOrgBookPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 10 | CostOrgBookPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 11 | CostOrgBookPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 12 | CostOrgBookPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 13 | CostOrgBookPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 14 | CostOrgBookPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 15 | CostOrgBookPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 16 | CostOrgBookPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 17 | CostOrgBookPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 18 | CostOrgBookPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 19 | CostOrgBookPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 20 | CostOrgBookPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 21 | CostOrgBookPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 22 | CostOrgBookPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 23 | CostOrgBookPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 24 | CostOrgBookPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 25 | CostOrgBookPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 26 | CostOrgBookPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 27 | CostOrgBookPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 28 | CostOrgBookPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 29 | CostOrgBookPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 30 | CostOrgBookPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 31 | CostOrgBookPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 32 | CostOrgBookPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 33 | CostOrgBookPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 34 | CostOrgBookPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 35 | CostOrgBookPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 36 | CostOrgBookPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 37 | CostOrgBookPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 38 | CostOrgBookPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 39 | CostOrgBookPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 40 | CostOrgBookPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 41 | CostOrgBookPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 42 | CostOrgBookPEOCalendarId | CALENDAR_ID | — | ✅ |
| 43 | CostOrgBookPEOConversionType | CONVERSION_TYPE | — | ✅ |
| 44 | CostOrgBookPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 45 | CostOrgBookPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 46 | CostOrgBookPEOCreateAccountingFlag | CREATE_ACCOUNTING_FLAG | — | ✅ |
| 47 | CostOrgBookPEOCreatedBy1 | CREATED_BY | — | ✅ |
| 48 | CostOrgBookPEOCreationDate1 | CREATION_DATE | — | ✅ |
| 49 | CostOrgBookPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 50 | CostOrgBookPEOFirstLedgerPeriodName | FIRST_LEDGER_PERIOD_NAME | — | ✅ |
| 51 | CostOrgBookPEOFromDate | FROM_DATE | — | ✅ |
| 52 | CostOrgBookPEOInactiveDate | INACTIVE_DATE | — | ✅ |
| 53 | CostOrgBookPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 54 | CostOrgBookPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 55 | CostOrgBookPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 56 | CostOrgBookPEOLedgerId | LEDGER_ID | — | ✅ |
| 57 | CostOrgBookPEOMaintainTransactionsFlag | MAINTAIN_TRANSACTIONS_FLAG | — | ✅ |
| 58 | CostOrgBookPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 59 | CostOrgBookPEOOpenPeriodsNum | OPEN_PERIODS_NUM | — | ✅ |
| 60 | CostOrgBookPEOPrimaryBookFlag | PRIMARY_BOOK_FLAG | — | ✅ |
| 61 | CostOrgBookPEOToDate | TO_DATE | — | ✅ |

### [[cst_cp_errors|CST_CP_ERRORS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstCpErrorsPEOAccountedDate | ACCOUNTED_DATE | — | ✅ |
| 2 | CstCpErrorsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 3 | CstCpErrorsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 4 | CstCpErrorsPEOCpErrorId1 | CP_ERROR_ID | — | ✅ |
| 5 | CstCpErrorsPEOCreatedBy1 | CREATED_BY | — | ✅ |
| 6 | CstCpErrorsPEOCreationDate1 | CREATION_DATE | — | ✅ |
| 7 | CstCpErrorsPEOErrorCode | ERROR_CODE | — | ✅ |
| 8 | CstCpErrorsPEOJobDefinitionName1 | JOB_DEFINITION_NAME | — | ✅ |
| 9 | CstCpErrorsPEOJobDefinitionPackage1 | JOB_DEFINITION_PACKAGE | — | ✅ |
| 10 | CstCpErrorsPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 11 | CstCpErrorsPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | CstCpErrorsPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 13 | CstCpErrorsPEOMessage | MESSAGE | — | ✅ |
| 14 | CstCpErrorsPEOMessageType | MESSAGE_TYPE | — | ✅ |
| 15 | CstCpErrorsPEOProcessorName | PROCESSOR_NAME | — | ✅ |
| 16 | CstCpErrorsPEORequestId1 | REQUEST_ID | — | ✅ |
| 17 | CstCpErrorsPEORowCount | ROW_COUNT | — | ✅ |
| 18 | CstCpErrorsPEORunControl | RUN_CONTROL | — | ✅ |
| 19 | CstCpErrorsPEOSubprocessorName | SUBPROCESSOR_NAME | — | ✅ |
| 20 | CstCpErrorsPEOTableName | TABLE_NAME | — | ✅ |
| 21 | CstCpErrorsPEOToken1Name | TOKEN1_NAME | — | ✅ |
| 22 | CstCpErrorsPEOToken1Value | TOKEN1_VALUE | — | ✅ |
| 23 | CstCpErrorsPEOToken2Name | TOKEN2_NAME | — | ✅ |
| 24 | CstCpErrorsPEOToken2Value | TOKEN2_VALUE | — | ✅ |
| 25 | CstCpErrorsPEOToken3Name | TOKEN3_NAME | — | ✅ |
| 26 | CstCpErrorsPEOToken3Value | TOKEN3_VALUE | — | ✅ |
| 27 | CstCpErrorsPEOToken4Name | TOKEN4_NAME | — | ✅ |
| 28 | CstCpErrorsPEOToken4Value | TOKEN4_VALUE | — | ✅ |
| 29 | CstCpErrorsPEOToken5Name | TOKEN5_NAME | — | ✅ |
| 30 | CstCpErrorsPEOToken5Value | TOKEN5_VALUE | — | ✅ |
| 31 | CstCpErrorsPEOToken6Name | TOKEN6_NAME | — | ✅ |
| 32 | CstCpErrorsPEOToken6Value | TOKEN6_VALUE | — | ✅ |

### [[cst_inv_transactions|CST_INV_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstInvTransactionsPEOAttribute1 | ATTRIBUTE1 | — | ✅ |
| 2 | CstInvTransactionsPEOAttribute10 | ATTRIBUTE10 | — | ✅ |
| 3 | CstInvTransactionsPEOAttribute11 | ATTRIBUTE11 | — | ✅ |
| 4 | CstInvTransactionsPEOAttribute12 | ATTRIBUTE12 | — | ✅ |
| 5 | CstInvTransactionsPEOAttribute13 | ATTRIBUTE13 | — | ✅ |
| 6 | CstInvTransactionsPEOAttribute14 | ATTRIBUTE14 | — | ✅ |
| 7 | CstInvTransactionsPEOAttribute15 | ATTRIBUTE15 | — | ✅ |
| 8 | CstInvTransactionsPEOAttribute16 | ATTRIBUTE16 | — | ✅ |
| 9 | CstInvTransactionsPEOAttribute17 | ATTRIBUTE17 | — | ✅ |
| 10 | CstInvTransactionsPEOAttribute18 | ATTRIBUTE18 | — | ✅ |
| 11 | CstInvTransactionsPEOAttribute19 | ATTRIBUTE19 | — | ✅ |
| 12 | CstInvTransactionsPEOAttribute2 | ATTRIBUTE2 | — | ✅ |
| 13 | CstInvTransactionsPEOAttribute20 | ATTRIBUTE20 | — | ✅ |
| 14 | CstInvTransactionsPEOAttribute21 | ATTRIBUTE21 | — | ✅ |
| 15 | CstInvTransactionsPEOAttribute22 | ATTRIBUTE22 | — | ✅ |
| 16 | CstInvTransactionsPEOAttribute23 | ATTRIBUTE23 | — | ✅ |
| 17 | CstInvTransactionsPEOAttribute24 | ATTRIBUTE24 | — | ✅ |
| 18 | CstInvTransactionsPEOAttribute25 | ATTRIBUTE25 | — | ✅ |
| 19 | CstInvTransactionsPEOAttribute26 | ATTRIBUTE26 | — | ✅ |
| 20 | CstInvTransactionsPEOAttribute27 | ATTRIBUTE27 | — | ✅ |
| 21 | CstInvTransactionsPEOAttribute28 | ATTRIBUTE28 | — | ✅ |
| 22 | CstInvTransactionsPEOAttribute29 | ATTRIBUTE29 | — | ✅ |
| 23 | CstInvTransactionsPEOAttribute3 | ATTRIBUTE3 | — | ✅ |
| 24 | CstInvTransactionsPEOAttribute30 | ATTRIBUTE30 | — | ✅ |
| 25 | CstInvTransactionsPEOAttribute4 | ATTRIBUTE4 | — | ✅ |
| 26 | CstInvTransactionsPEOAttribute5 | ATTRIBUTE5 | — | ✅ |
| 27 | CstInvTransactionsPEOAttribute6 | ATTRIBUTE6 | — | ✅ |
| 28 | CstInvTransactionsPEOAttribute7 | ATTRIBUTE7 | — | ✅ |
| 29 | CstInvTransactionsPEOAttribute8 | ATTRIBUTE8 | — | ✅ |
| 30 | CstInvTransactionsPEOAttribute9 | ATTRIBUTE9 | — | ✅ |
| 31 | CstInvTransactionsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 32 | CstInvTransactionsPEOBaseTxnActionId | BASE_TXN_ACTION_ID | — | ✅ |
| 33 | CstInvTransactionsPEOBaseTxnSourceTypeId | BASE_TXN_SOURCE_TYPE_ID | — | ✅ |
| 34 | CstInvTransactionsPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | ✅ |
| 35 | CstInvTransactionsPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 36 | CstInvTransactionsPEOCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 37 | CstInvTransactionsPEOCostPreprocessingStatus | COST_PREPROCESSING_STATUS | — | ✅ |
| 38 | CstInvTransactionsPEOCreatedBy1 | CREATED_BY | — | ✅ |
| 39 | CstInvTransactionsPEOCreationDate1 | CREATION_DATE | — | ✅ |
| 40 | CstInvTransactionsPEOCstInvTransactionId | CST_INV_TRANSACTION_ID | — | ✅ |
| 41 | CstInvTransactionsPEODooFullfillLineId | DOO_FULLFILL_LINE_ID | — | ✅ |
| 42 | CstInvTransactionsPEOExpenseTransactionFlag | EXPENSE_TRANSACTION_FLAG | — | ✅ |
| 43 | CstInvTransactionsPEOExternalSystemRefId1 | EXTERNAL_SYSTEM_REF_ID | — | ✅ |
| 44 | CstInvTransactionsPEOExternalSystemReference1 | EXTERNAL_SYSTEM_REFERENCE | — | ✅ |
| 45 | CstInvTransactionsPEOFobPoint | FOB_POINT | — | ✅ |
| 46 | CstInvTransactionsPEOIntercompanyInvoicingFlag | INTERCOMPANY_INVOICING_FLAG | — | ✅ |
| 47 | CstInvTransactionsPEOInterfaceBatchName | INTERFACE_BATCH_NAME | — | ✅ |
| 48 | CstInvTransactionsPEOInterfaceBatchNumber | INTERFACE_BATCH_NUMBER | — | ✅ |
| 49 | CstInvTransactionsPEOInternalProfitTracking | INTERNAL_PROFIT_TRACKING | — | ✅ |
| 50 | CstInvTransactionsPEOIntransitFlag | INTRANSIT_FLAG | — | ✅ |
| 51 | CstInvTransactionsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 52 | CstInvTransactionsPEOInventoryOrgId | INVENTORY_ORG_ID | — | ✅ |
| 53 | CstInvTransactionsPEOJobDefinitionName1 | JOB_DEFINITION_NAME | — | ✅ |
| 54 | CstInvTransactionsPEOJobDefinitionPackage1 | JOB_DEFINITION_PACKAGE | — | ✅ |
| 55 | CstInvTransactionsPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 56 | CstInvTransactionsPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 57 | CstInvTransactionsPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 58 | CstInvTransactionsPEOLocatorId | LOCATOR_ID | — | ✅ |
| 59 | CstInvTransactionsPEOOrigTransferInventoryOrgId | ORIG_TRANSFER_INVENTORY_ORG_ID | — | ✅ |
| 60 | CstInvTransactionsPEOOriginalTransactionTempId | ORIGINAL_TRANSACTION_TEMP_ID | — | ✅ |
| 61 | CstInvTransactionsPEOParentTransactionId | PARENT_TRANSACTION_ID | — | ✅ |
| 62 | CstInvTransactionsPEOPjcBillableFlag | PJC_BILLABLE_FLAG | — | ✅ |
| 63 | CstInvTransactionsPEOPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | ✅ |
| 64 | CstInvTransactionsPEOPjcContextCategory | PJC_CONTEXT_CATEGORY | — | ✅ |
| 65 | CstInvTransactionsPEOPjcContractId | PJC_CONTRACT_ID | — | ✅ |
| 66 | CstInvTransactionsPEOPjcContractLineId | PJC_CONTRACT_LINE_ID | — | ✅ |
| 67 | CstInvTransactionsPEOPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | ✅ |
| 68 | CstInvTransactionsPEOPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | ✅ |
| 69 | CstInvTransactionsPEOPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | ✅ |
| 70 | CstInvTransactionsPEOPjcOrganizationId | PJC_ORGANIZATION_ID | — | ✅ |
| 71 | CstInvTransactionsPEOPjcProjectId | PJC_PROJECT_ID | — | ✅ |
| 72 | CstInvTransactionsPEOPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | ✅ |
| 73 | CstInvTransactionsPEOPjcReservedAttribute10 | PJC_RESERVED_ATTRIBUTE10 | — | ✅ |
| 74 | CstInvTransactionsPEOPjcReservedAttribute2 | PJC_RESERVED_ATTRIBUTE2 | — | ✅ |
| 75 | CstInvTransactionsPEOPjcReservedAttribute3 | PJC_RESERVED_ATTRIBUTE3 | — | ✅ |
| 76 | CstInvTransactionsPEOPjcReservedAttribute4 | PJC_RESERVED_ATTRIBUTE4 | — | ✅ |
| 77 | CstInvTransactionsPEOPjcReservedAttribute5 | PJC_RESERVED_ATTRIBUTE5 | — | ✅ |
| 78 | CstInvTransactionsPEOPjcReservedAttribute6 | PJC_RESERVED_ATTRIBUTE6 | — | ✅ |
| 79 | CstInvTransactionsPEOPjcReservedAttribute7 | PJC_RESERVED_ATTRIBUTE7 | — | ✅ |
| 80 | CstInvTransactionsPEOPjcReservedAttribute8 | PJC_RESERVED_ATTRIBUTE8 | — | ✅ |
| 81 | CstInvTransactionsPEOPjcReservedAttribute9 | PJC_RESERVED_ATTRIBUTE9 | — | ✅ |
| 82 | CstInvTransactionsPEOPjcTaskId | PJC_TASK_ID | — | ✅ |
| 83 | CstInvTransactionsPEOPjcUserDefAttribute1 | PJC_USER_DEF_ATTRIBUTE1 | — | ✅ |
| 84 | CstInvTransactionsPEOPjcUserDefAttribute10 | PJC_USER_DEF_ATTRIBUTE10 | — | ✅ |
| 85 | CstInvTransactionsPEOPjcUserDefAttribute2 | PJC_USER_DEF_ATTRIBUTE2 | — | ✅ |
| 86 | CstInvTransactionsPEOPjcUserDefAttribute3 | PJC_USER_DEF_ATTRIBUTE3 | — | ✅ |
| 87 | CstInvTransactionsPEOPjcUserDefAttribute4 | PJC_USER_DEF_ATTRIBUTE4 | — | ✅ |
| 88 | CstInvTransactionsPEOPjcUserDefAttribute5 | PJC_USER_DEF_ATTRIBUTE5 | — | ✅ |
| 89 | CstInvTransactionsPEOPjcUserDefAttribute6 | PJC_USER_DEF_ATTRIBUTE6 | — | ✅ |
| 90 | CstInvTransactionsPEOPjcUserDefAttribute7 | PJC_USER_DEF_ATTRIBUTE7 | — | ✅ |
| 91 | CstInvTransactionsPEOPjcUserDefAttribute8 | PJC_USER_DEF_ATTRIBUTE8 | — | ✅ |
| 92 | CstInvTransactionsPEOPjcUserDefAttribute9 | PJC_USER_DEF_ATTRIBUTE9 | — | ✅ |
| 93 | CstInvTransactionsPEOPjcWorkTypeId | PJC_WORK_TYPE_ID | — | ✅ |
| 94 | CstInvTransactionsPEOPoDistributionId | PO_DISTRIBUTION_ID | — | ✅ |
| 95 | CstInvTransactionsPEOPreprocessingStatus | PREPROCESSING_STATUS | — | ✅ |
| 96 | CstInvTransactionsPEOPricingOption | PRICING_OPTION | — | ✅ |
| 97 | CstInvTransactionsPEOPrimaryQty | PRIMARY_QTY | — | ✅ |
| 98 | CstInvTransactionsPEOPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 99 | CstInvTransactionsPEOPriorBusinessUnitId | PRIOR_BUSINESS_UNIT_ID | — | ✅ |
| 100 | CstInvTransactionsPEOPriorInventoryOrgId | PRIOR_INVENTORY_ORG_ID | — | ✅ |
| 101 | CstInvTransactionsPEORcvTransactionId | RCV_TRANSACTION_ID | — | ✅ |
| 102 | CstInvTransactionsPEORequestId1 | REQUEST_ID | — | ✅ |
| 103 | CstInvTransactionsPEOSecondaryTransactionQty | SECONDARY_TRANSACTION_QTY | — | ✅ |
| 104 | CstInvTransactionsPEOSecondaryTransactionUomCode | SECONDARY_TRANSACTION_UOM_CODE | — | ✅ |
| 105 | CstInvTransactionsPEOSubinventoryCode | SUBINVENTORY_CODE | — | ✅ |
| 106 | CstInvTransactionsPEOSuccessorBusinessUnitId | SUCCESSOR_BUSINESS_UNIT_ID | — | ✅ |
| 107 | CstInvTransactionsPEOSuccessorInventoryOrgId | SUCCESSOR_INVENTORY_ORG_ID | — | ✅ |
| 108 | CstInvTransactionsPEOTransactionCreationDate | TRANSACTION_CREATION_DATE | — | ✅ |
| 109 | CstInvTransactionsPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 110 | CstInvTransactionsPEOTransactionFlowType | TRANSACTION_FLOW_TYPE | — | ✅ |
| 111 | CstInvTransactionsPEOTransactionQty | TRANSACTION_QTY | — | ✅ |
| 112 | CstInvTransactionsPEOTransactionReasonId | TRANSACTION_REASON_ID | — | ✅ |
| 113 | CstInvTransactionsPEOTransactionTempId | TRANSACTION_TEMP_ID | — | ✅ |
| 114 | CstInvTransactionsPEOTransactionTimezoneCode | TRANSACTION_TIMEZONE_CODE | — | ✅ |
| 115 | CstInvTransactionsPEOTransactionUomCode | TRANSACTION_UOM_CODE | — | ✅ |
| 116 | CstInvTransactionsPEOTransferCstInvTxnId | TRANSFER_CST_INV_TXN_ID | — | ✅ |
| 117 | CstInvTransactionsPEOTransferInventoryOrgId | TRANSFER_INVENTORY_ORG_ID | — | ✅ |
| 118 | CstInvTransactionsPEOTransferLocatorId | TRANSFER_LOCATOR_ID | — | ✅ |
| 119 | CstInvTransactionsPEOTransferPercentage | TRANSFER_PERCENTAGE | — | ✅ |
| 120 | CstInvTransactionsPEOTransferSubinventoryCode | TRANSFER_SUBINVENTORY_CODE | — | ✅ |
| 121 | CstInvTransactionsPEOTransferTransactionId | TRANSFER_TRANSACTION_ID | — | ✅ |
| 122 | CstInvTransactionsPEOTxnGroupId | TXN_GROUP_ID | — | ✅ |
| 123 | CstInvTransactionsPEOTxnSourceDocNumber | TXN_SOURCE_DOC_NUMBER | — | ✅ |
| 124 | CstInvTransactionsPEOTxnSourceDocType | TXN_SOURCE_DOC_TYPE | — | ✅ |
| 125 | CstInvTransactionsPEOTxnSourceRefDocNumber | TXN_SOURCE_REF_DOC_NUMBER | — | ✅ |
| 126 | CstInvTransactionsPEOTxnSourceRefDocType | TXN_SOURCE_REF_DOC_TYPE | — | ✅ |
| 127 | CstInvTransactionsPEOWshDeliveryDetailId | WSH_DELIVERY_DETAIL_ID | — | ✅ |

### [[cst_period_close_actions|CST_PERIOD_CLOSE_ACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstPeriodCloseActionsPEOArErrorsCount | AR_ERRORS_COUNT | — | ✅ |
| 2 | CstPeriodCloseActionsPEOArPendingCount | AR_PENDING_COUNT | — | ✅ |
| 3 | CstPeriodCloseActionsPEOCitePendingCount | CITE_PENDING_COUNT | — | — |
| 4 | CstPeriodCloseActionsPEOComplWoNotClosed | COMPL_WO_NOT_CLOSED | — | ✅ |
| 5 | CstPeriodCloseActionsPEOComplWoPendingCount | COMPL_WO_PENDING_COUNT | — | ✅ |
| 6 | CstPeriodCloseActionsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 7 | CstPeriodCloseActionsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 8 | CstPeriodCloseActionsPEOCreatedBy1 | CREATED_BY | — | ✅ |
| 9 | CstPeriodCloseActionsPEOCreationDate1 | CREATION_DATE | — | ✅ |
| 10 | CstPeriodCloseActionsPEOCstInvOnhandMismatchQty | CST_INV_ONHAND_MISMATCH_QTY | — | ✅ |
| 11 | CstPeriodCloseActionsPEOCtePendingCount | CTE_PENDING_COUNT | — | — |
| 12 | CstPeriodCloseActionsPEODistributionErrorsCount | DISTRIBUTION_ERRORS_COUNT | — | ✅ |
| 13 | CstPeriodCloseActionsPEODistributionPendingCount | DISTRIBUTION_PENDING_COUNT | — | ✅ |
| 14 | CstPeriodCloseActionsPEOFromStatusCode | FROM_STATUS_CODE | — | ✅ |
| 15 | CstPeriodCloseActionsPEOInvErrorsCount | INV_ERRORS_COUNT | — | ✅ |
| 16 | CstPeriodCloseActionsPEOInvPendingCount | INV_PENDING_COUNT | — | ✅ |
| 17 | CstPeriodCloseActionsPEOJournalsErrorsCount | JOURNALS_ERRORS_COUNT | — | ✅ |
| 18 | CstPeriodCloseActionsPEOJournalsPendingCount | JOURNALS_PENDING_COUNT | — | ✅ |
| 19 | CstPeriodCloseActionsPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 20 | CstPeriodCloseActionsPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 21 | CstPeriodCloseActionsPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 22 | CstPeriodCloseActionsPEOMatchInvOnhandWithCst | MATCH_INV_ONHAND_WITH_CST | — | ✅ |
| 23 | CstPeriodCloseActionsPEOPendAcctEventsCount | PEND_ACCT_EVENTS_COUNT | — | — |
| 24 | CstPeriodCloseActionsPEOPendOhRatesAbsCount | PEND_OH_RATES_ABS_COUNT | — | — |
| 25 | CstPeriodCloseActionsPEOPendScenarioAbsCount | PEND_SCENARIO_ABS_COUNT | — | — |
| 26 | CstPeriodCloseActionsPEOPendingAccountingEvents | PENDING_ACCOUNTING_EVENTS | — | — |
| 27 | CstPeriodCloseActionsPEOPendingDcogsTransactions | PENDING_DCOGS_TRANSACTIONS | — | ✅ |
| 28 | CstPeriodCloseActionsPEOPendingInterfaceTxns | PENDING_INTERFACE_TXNS | — | ✅ |
| 29 | CstPeriodCloseActionsPEOPendingIntfTxnCount | PENDING_INTF_TXN_COUNT | — | ✅ |
| 30 | CstPeriodCloseActionsPEOPendingOhRatesAbsorption | PENDING_OH_RATES_ABSORPTION | — | — |
| 31 | CstPeriodCloseActionsPEOPendingScenarioAbsorption | PENDING_SCENARIO_ABSORPTION | — | — |
| 32 | CstPeriodCloseActionsPEOPeriodName | PERIOD_NAME | — | ✅ |
| 33 | CstPeriodCloseActionsPEOProcessStartDate | PROCESS_START_DATE | — | ✅ |
| 34 | CstPeriodCloseActionsPEOProcessStatusCode | PROCESS_STATUS_CODE | — | ✅ |
| 35 | CstPeriodCloseActionsPEORunId | RUN_ID | — | ✅ |
| 36 | CstPeriodCloseActionsPEOToStatusCode | TO_STATUS_CODE | — | ✅ |
| 37 | CstPeriodCloseActionsPEOUncostedTransactions | UNCOSTED_TRANSACTIONS | — | ✅ |
| 38 | CstPeriodCloseActionsPEOUncostedTxnCount | UNCOSTED_TXN_COUNT | — | ✅ |
| 39 | CstPeriodCloseActionsPEOUnimportedInvTransactions | UNIMPORTED_INV_TRANSACTIONS | — | ✅ |
| 40 | CstPeriodCloseActionsPEOUnprocessedDistributions | UNPROCESSED_DISTRIBUTIONS | — | ✅ |
| 41 | CstPeriodCloseActionsPEOUnprocessedJournals | UNPROCESSED_JOURNALS | — | ✅ |
| 42 | CstPeriodCloseActionsPEOWipPendingCount | WIP_PENDING_COUNT | — | ✅ |

### [[cst_transaction_errors|CST_TRANSACTION_ERRORS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CpErrorId | CP_ERROR_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | ExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | 🔑 | ✅ |
| 5 | ExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | 🔑 | ✅ |
| 6 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 7 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | RequestId | REQUEST_ID | — | ✅ |
| 12 | TransactionId | TRANSACTION_ID | 🔑 | ✅ |
| 13 | WoExtSystemRefId | WO_EXT_SYSTEM_REF_ID | 🔑 | ✅ |
| 14 | WoOpExtSystemRefId | WO_OP_EXT_SYSTEM_REF_ID | 🔑 | ✅ |
| 15 | WoResExtSystemRefId | WO_RES_EXT_SYSTEM_REF_ID | 🔑 | ✅ |

### [[gl_calendars|GL_CALENDARS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlCalendarsAdjPeriodFreqCode | ADJ_PERIOD_FREQ_CODE | — | ✅ |
| 2 | GlCalendarsAdjPeriodsNum | ADJ_PERIODS_NUM | — | ✅ |
| 3 | GlCalendarsAttribute1 | ATTRIBUTE1 | — | ✅ |
| 4 | GlCalendarsAttribute2 | ATTRIBUTE2 | — | ✅ |
| 5 | GlCalendarsAttribute3 | ATTRIBUTE3 | — | ✅ |
| 6 | GlCalendarsAttribute4 | ATTRIBUTE4 | — | ✅ |
| 7 | GlCalendarsAttribute5 | ATTRIBUTE5 | — | ✅ |
| 8 | GlCalendarsAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 9 | GlCalendarsCalendarId | CALENDAR_ID | — | ✅ |
| 10 | GlCalendarsCalendarStartDate | CALENDAR_START_DATE | — | ✅ |
| 11 | GlCalendarsCalendarTypeCode | CALENDAR_TYPE_CODE | — | ✅ |
| 12 | GlCalendarsCreatedBy1 | CREATED_BY | — | ✅ |
| 13 | GlCalendarsCreationDate1 | CREATION_DATE | — | ✅ |
| 14 | GlCalendarsDescription | DESCRIPTION | — | ✅ |
| 15 | GlCalendarsLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 16 | GlCalendarsLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | GlCalendarsLastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 18 | GlCalendarsLatestYearStartDate | LATEST_YEAR_START_DATE | — | ✅ |
| 19 | GlCalendarsLegacyCalendarFlag | LEGACY_CALENDAR_FLAG | — | ✅ |
| 20 | GlCalendarsLegacyRulesEnabledFlag | LEGACY_RULES_ENABLED_FLAG | — | ✅ |
| 21 | GlCalendarsNonAdjPeriodFreqCode | NON_ADJ_PERIOD_FREQ_CODE | — | ✅ |
| 22 | GlCalendarsNonAdjPeriodsNum | NON_ADJ_PERIODS_NUM | — | ✅ |
| 23 | GlCalendarsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 24 | GlCalendarsPeriodNameFormatCode | PERIOD_NAME_FORMAT_CODE | — | ✅ |
| 25 | GlCalendarsPeriodNameSeparatorCode | PERIOD_NAME_SEPARATOR_CODE | — | ✅ |
| 26 | GlCalendarsPeriodSetId | PERIOD_SET_ID | — | ✅ |
| 27 | GlCalendarsPeriodSetName | PERIOD_SET_NAME | — | ✅ |
| 28 | GlCalendarsPeriodType | PERIOD_TYPE | — | ✅ |
| 29 | GlCalendarsPeriodTypeId | PERIOD_TYPE_ID | — | ✅ |
| 30 | GlCalendarsSecurityFlag | SECURITY_FLAG | — | ✅ |
| 31 | GlCalendarsUserPeriodNamePrefix | USER_PERIOD_NAME_PREFIX | — | ✅ |
| 32 | GlCalendarsUserPeriodSetName | USER_PERIOD_SET_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
