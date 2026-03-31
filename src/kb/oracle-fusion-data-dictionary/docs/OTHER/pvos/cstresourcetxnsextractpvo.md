---
id: DOC-OTHER-PVO-CstResourceTxnsExtractPVO
doc_type: system-doc
title: "CstResourceTxnsExtractPVO — PVO Cross-Module"
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
  - CstResourceTxnsExtractPVO
  - cstresourcetxnsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstResourceTxnsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Resource Txns Extract. Acessa as tabelas: CST_RESOURCE_TRANSACTIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstResourceTxnsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 77 | 1 | 1 | 45 | 58% |

---

## 🔗 Tabelas Relacionadas

- [[cst_resource_transactions|CST_RESOURCE_TRANSACTIONS]] — 77 atributos (1 PKs, 45 BICC)

---

## ⚙️ Atributos

### [[cst_resource_transactions|CST_RESOURCE_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstResourceTxnsPEOAccountingStatus | ACCOUNTING_STATUS | — | ✅ |
| 2 | CstResourceTxnsPEOAdditionalProcessingCode | ADDITIONAL_PROCESSING_CODE | — | ✅ |
| 3 | CstResourceTxnsPEOBaseTxnActionId | BASE_TXN_ACTION_ID | — | ✅ |
| 4 | CstResourceTxnsPEOBaseTxnSourceTypeId | BASE_TXN_SOURCE_TYPE_ID | — | ✅ |
| 5 | CstResourceTxnsPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | ✅ |
| 6 | CstResourceTxnsPEOComponentGroupId | COMPONENT_GROUP_ID | — | ✅ |
| 7 | CstResourceTxnsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 8 | CstResourceTxnsPEOCostDate | COST_DATE | — | ✅ |
| 9 | CstResourceTxnsPEOCostMethodCode | COST_METHOD_CODE | — | ✅ |
| 10 | CstResourceTxnsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 11 | CstResourceTxnsPEOCostProfileId | COST_PROFILE_ID | — | ✅ |
| 12 | CstResourceTxnsPEOCostTransactionType | COST_TRANSACTION_TYPE | — | ✅ |
| 13 | CstResourceTxnsPEOCostingStatus | COSTING_STATUS | — | ✅ |
| 14 | CstResourceTxnsPEOCreatedBy | CREATED_BY | — | ✅ |
| 15 | CstResourceTxnsPEOCreationDate | CREATION_DATE | — | ✅ |
| 16 | CstResourceTxnsPEOCstWoResourceTxnId | CST_WO_RESOURCE_TXN_ID | — | ✅ |
| 17 | CstResourceTxnsPEOCstWorkOrderId | CST_WORK_ORDER_ID | — | ✅ |
| 18 | CstResourceTxnsPEOCstWorkOrderOperationId | CST_WORK_ORDER_OPERATION_ID | — | ✅ |
| 19 | CstResourceTxnsPEOEquipmentInstanceId | EQUIPMENT_INSTANCE_ID | — | ✅ |
| 20 | CstResourceTxnsPEOErrorCode | ERROR_CODE | — | ✅ |
| 21 | CstResourceTxnsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 22 | CstResourceTxnsPEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | ✅ |
| 23 | CstResourceTxnsPEOItemCostProfileId | ITEM_COST_PROFILE_ID | — | ✅ |
| 24 | CstResourceTxnsPEOLaborInstanceId | LABOR_INSTANCE_ID | — | ✅ |
| 25 | CstResourceTxnsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | CstResourceTxnsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 27 | CstResourceTxnsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 28 | CstResourceTxnsPEOLeTimezoneCode | LE_TIMEZONE_CODE | — | ✅ |
| 29 | CstResourceTxnsPEOPeriodName | PERIOD_NAME | — | ✅ |
| 30 | CstResourceTxnsPEOPjcBillableFlag | PJC_BILLABLE_FLAG | — | — |
| 31 | CstResourceTxnsPEOPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | — |
| 32 | CstResourceTxnsPEOPjcContextCategory | PJC_CONTEXT_CATEGORY | — | — |
| 33 | CstResourceTxnsPEOPjcContractId | PJC_CONTRACT_ID | — | — |
| 34 | CstResourceTxnsPEOPjcContractLineId | PJC_CONTRACT_LINE_ID | — | — |
| 35 | CstResourceTxnsPEOPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 36 | CstResourceTxnsPEOPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | — |
| 37 | CstResourceTxnsPEOPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | — |
| 38 | CstResourceTxnsPEOPjcOrganizationId | PJC_ORGANIZATION_ID | — | — |
| 39 | CstResourceTxnsPEOPjcProjectId | PJC_PROJECT_ID | — | — |
| 40 | CstResourceTxnsPEOPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 41 | CstResourceTxnsPEOPjcReservedAttribute10 | PJC_RESERVED_ATTRIBUTE10 | — | — |
| 42 | CstResourceTxnsPEOPjcReservedAttribute2 | PJC_RESERVED_ATTRIBUTE2 | — | — |
| 43 | CstResourceTxnsPEOPjcReservedAttribute3 | PJC_RESERVED_ATTRIBUTE3 | — | — |
| 44 | CstResourceTxnsPEOPjcReservedAttribute4 | PJC_RESERVED_ATTRIBUTE4 | — | — |
| 45 | CstResourceTxnsPEOPjcReservedAttribute5 | PJC_RESERVED_ATTRIBUTE5 | — | — |
| 46 | CstResourceTxnsPEOPjcReservedAttribute6 | PJC_RESERVED_ATTRIBUTE6 | — | — |
| 47 | CstResourceTxnsPEOPjcReservedAttribute7 | PJC_RESERVED_ATTRIBUTE7 | — | — |
| 48 | CstResourceTxnsPEOPjcReservedAttribute8 | PJC_RESERVED_ATTRIBUTE8 | — | — |
| 49 | CstResourceTxnsPEOPjcReservedAttribute9 | PJC_RESERVED_ATTRIBUTE9 | — | — |
| 50 | CstResourceTxnsPEOPjcTaskId | PJC_TASK_ID | — | — |
| 51 | CstResourceTxnsPEOPjcUserDefAttribute1 | PJC_USER_DEF_ATTRIBUTE1 | — | — |
| 52 | CstResourceTxnsPEOPjcUserDefAttribute10 | PJC_USER_DEF_ATTRIBUTE10 | — | — |
| 53 | CstResourceTxnsPEOPjcUserDefAttribute2 | PJC_USER_DEF_ATTRIBUTE2 | — | — |
| 54 | CstResourceTxnsPEOPjcUserDefAttribute3 | PJC_USER_DEF_ATTRIBUTE3 | — | — |
| 55 | CstResourceTxnsPEOPjcUserDefAttribute4 | PJC_USER_DEF_ATTRIBUTE4 | — | — |
| 56 | CstResourceTxnsPEOPjcUserDefAttribute5 | PJC_USER_DEF_ATTRIBUTE5 | — | — |
| 57 | CstResourceTxnsPEOPjcUserDefAttribute6 | PJC_USER_DEF_ATTRIBUTE6 | — | — |
| 58 | CstResourceTxnsPEOPjcUserDefAttribute7 | PJC_USER_DEF_ATTRIBUTE7 | — | — |
| 59 | CstResourceTxnsPEOPjcUserDefAttribute8 | PJC_USER_DEF_ATTRIBUTE8 | — | — |
| 60 | CstResourceTxnsPEOPjcUserDefAttribute9 | PJC_USER_DEF_ATTRIBUTE9 | — | — |
| 61 | CstResourceTxnsPEOPjcWorkTypeId | PJC_WORK_TYPE_ID | — | — |
| 62 | CstResourceTxnsPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 63 | CstResourceTxnsPEOPreprocessingStatus | PREPROCESSING_STATUS | — | ✅ |
| 64 | CstResourceTxnsPEOPrimaryQuantity | PRIMARY_QUANTITY | — | ✅ |
| 65 | CstResourceTxnsPEOPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 66 | CstResourceTxnsPEOResourceActivityCode | RESOURCE_ACTIVITY_CODE | — | ✅ |
| 67 | CstResourceTxnsPEOResourceId | RESOURCE_ID | — | ✅ |
| 68 | CstResourceTxnsPEOResourceTransactionId | RESOURCE_TRANSACTION_ID | 🔑 | ✅ |
| 69 | CstResourceTxnsPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 70 | CstResourceTxnsPEOTransactionQuantity | TRANSACTION_QUANTITY | — | ✅ |
| 71 | CstResourceTxnsPEOTransactionUomCode | TRANSACTION_UOM_CODE | — | ✅ |
| 72 | CstResourceTxnsPEOTxnSourceDocNumber | TXN_SOURCE_DOC_NUMBER | — | ✅ |
| 73 | CstResourceTxnsPEOTxnSourceDocType | TXN_SOURCE_DOC_TYPE | — | ✅ |
| 74 | CstResourceTxnsPEOTxnSourceRefDocNumber | TXN_SOURCE_REF_DOC_NUMBER | — | ✅ |
| 75 | CstResourceTxnsPEOTxnSourceRefDocType | TXN_SOURCE_REF_DOC_TYPE | — | ✅ |
| 76 | CstResourceTxnsPEOWoOperationResourceId | WO_OPERATION_RESOURCE_ID | — | ✅ |
| 77 | CstResourceTxnsPEOWorkCenterId | WORK_CENTER_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
