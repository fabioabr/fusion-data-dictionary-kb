---
id: DOC-OTHER-PVO-CstWOResourceTxnsExtractPVO
doc_type: system-doc
title: "CstWOResourceTxnsExtractPVO — PVO Cross-Module"
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
  - CstWOResourceTxnsExtractPVO
  - cstworesourcetxnsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstWOResourceTxnsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst WOResource Txns Extract. Acessa as tabelas: CST_WO_RESOURCE_TXNS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstWOResourceTxnsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 66 | 1 | 1 | 34 | 52% |

---

## 🔗 Tabelas Relacionadas

- [[cst_wo_resource_txns|CST_WO_RESOURCE_TXNS]] — 66 atributos (1 PKs, 34 BICC)

---

## ⚙️ Atributos

### [[cst_wo_resource_txns|CST_WO_RESOURCE_TXNS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstWOResourceTxnsPEOBaseTxnActionId | BASE_TXN_ACTION_ID | — | ✅ |
| 2 | CstWOResourceTxnsPEOBaseTxnSourceTypeId | BASE_TXN_SOURCE_TYPE_ID | — | ✅ |
| 3 | CstWOResourceTxnsPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | ✅ |
| 4 | CstWOResourceTxnsPEOBasisType | BASIS_TYPE | — | ✅ |
| 5 | CstWOResourceTxnsPEOChargeType | CHARGE_TYPE | — | ✅ |
| 6 | CstWOResourceTxnsPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | CstWOResourceTxnsPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | CstWOResourceTxnsPEOCstWoOperationTxnId | CST_WO_OPERATION_TXN_ID | — | ✅ |
| 9 | CstWOResourceTxnsPEOCstWoResourceTxnId | CST_WO_RESOURCE_TXN_ID | 🔑 | ✅ |
| 10 | CstWOResourceTxnsPEOCstWorkOrderId | CST_WORK_ORDER_ID | — | ✅ |
| 11 | CstWOResourceTxnsPEOCstWorkOrderOperationId | CST_WORK_ORDER_OPERATION_ID | — | ✅ |
| 12 | CstWOResourceTxnsPEOEquipmentInstanceId | EQUIPMENT_INSTANCE_ID | — | ✅ |
| 13 | CstWOResourceTxnsPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | ✅ |
| 14 | CstWOResourceTxnsPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | ✅ |
| 15 | CstWOResourceTxnsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 16 | CstWOResourceTxnsPEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | ✅ |
| 17 | CstWOResourceTxnsPEOLaborInstanceId | LABOR_INSTANCE_ID | — | ✅ |
| 18 | CstWOResourceTxnsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | CstWOResourceTxnsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 20 | CstWOResourceTxnsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 21 | CstWOResourceTxnsPEOPjcBillableFlag | PJC_BILLABLE_FLAG | — | — |
| 22 | CstWOResourceTxnsPEOPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | — |
| 23 | CstWOResourceTxnsPEOPjcContextCategory | PJC_CONTEXT_CATEGORY | — | — |
| 24 | CstWOResourceTxnsPEOPjcContractId | PJC_CONTRACT_ID | — | — |
| 25 | CstWOResourceTxnsPEOPjcContractLineId | PJC_CONTRACT_LINE_ID | — | — |
| 26 | CstWOResourceTxnsPEOPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 27 | CstWOResourceTxnsPEOPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | — |
| 28 | CstWOResourceTxnsPEOPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | — |
| 29 | CstWOResourceTxnsPEOPjcOrganizationId | PJC_ORGANIZATION_ID | — | — |
| 30 | CstWOResourceTxnsPEOPjcProjectId | PJC_PROJECT_ID | — | — |
| 31 | CstWOResourceTxnsPEOPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 32 | CstWOResourceTxnsPEOPjcReservedAttribute10 | PJC_RESERVED_ATTRIBUTE10 | — | — |
| 33 | CstWOResourceTxnsPEOPjcReservedAttribute2 | PJC_RESERVED_ATTRIBUTE2 | — | — |
| 34 | CstWOResourceTxnsPEOPjcReservedAttribute3 | PJC_RESERVED_ATTRIBUTE3 | — | — |
| 35 | CstWOResourceTxnsPEOPjcReservedAttribute4 | PJC_RESERVED_ATTRIBUTE4 | — | — |
| 36 | CstWOResourceTxnsPEOPjcReservedAttribute5 | PJC_RESERVED_ATTRIBUTE5 | — | — |
| 37 | CstWOResourceTxnsPEOPjcReservedAttribute6 | PJC_RESERVED_ATTRIBUTE6 | — | — |
| 38 | CstWOResourceTxnsPEOPjcReservedAttribute7 | PJC_RESERVED_ATTRIBUTE7 | — | — |
| 39 | CstWOResourceTxnsPEOPjcReservedAttribute8 | PJC_RESERVED_ATTRIBUTE8 | — | — |
| 40 | CstWOResourceTxnsPEOPjcReservedAttribute9 | PJC_RESERVED_ATTRIBUTE9 | — | — |
| 41 | CstWOResourceTxnsPEOPjcTaskId | PJC_TASK_ID | — | — |
| 42 | CstWOResourceTxnsPEOPjcUserDefAttribute1 | PJC_USER_DEF_ATTRIBUTE1 | — | — |
| 43 | CstWOResourceTxnsPEOPjcUserDefAttribute10 | PJC_USER_DEF_ATTRIBUTE10 | — | — |
| 44 | CstWOResourceTxnsPEOPjcUserDefAttribute2 | PJC_USER_DEF_ATTRIBUTE2 | — | — |
| 45 | CstWOResourceTxnsPEOPjcUserDefAttribute3 | PJC_USER_DEF_ATTRIBUTE3 | — | — |
| 46 | CstWOResourceTxnsPEOPjcUserDefAttribute4 | PJC_USER_DEF_ATTRIBUTE4 | — | — |
| 47 | CstWOResourceTxnsPEOPjcUserDefAttribute5 | PJC_USER_DEF_ATTRIBUTE5 | — | — |
| 48 | CstWOResourceTxnsPEOPjcUserDefAttribute6 | PJC_USER_DEF_ATTRIBUTE6 | — | — |
| 49 | CstWOResourceTxnsPEOPjcUserDefAttribute7 | PJC_USER_DEF_ATTRIBUTE7 | — | — |
| 50 | CstWOResourceTxnsPEOPjcUserDefAttribute8 | PJC_USER_DEF_ATTRIBUTE8 | — | — |
| 51 | CstWOResourceTxnsPEOPjcUserDefAttribute9 | PJC_USER_DEF_ATTRIBUTE9 | — | — |
| 52 | CstWOResourceTxnsPEOPjcWorkTypeId | PJC_WORK_TYPE_ID | — | — |
| 53 | CstWOResourceTxnsPEOPrimaryQuantity | PRIMARY_QUANTITY | — | ✅ |
| 54 | CstWOResourceTxnsPEOPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 55 | CstWOResourceTxnsPEOProcessedByCaFlag | PROCESSED_BY_CA_FLAG | — | ✅ |
| 56 | CstWOResourceTxnsPEOResourceActivityCode | RESOURCE_ACTIVITY_CODE | — | ✅ |
| 57 | CstWOResourceTxnsPEOResourceId | RESOURCE_ID | — | ✅ |
| 58 | CstWOResourceTxnsPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 59 | CstWOResourceTxnsPEOTransactionQuantity | TRANSACTION_QUANTITY | — | ✅ |
| 60 | CstWOResourceTxnsPEOTransactionTypeCode | TRANSACTION_TYPE_CODE | — | ✅ |
| 61 | CstWOResourceTxnsPEOTransactionUomCode | TRANSACTION_UOM_CODE | — | ✅ |
| 62 | CstWOResourceTxnsPEOWoOperationResourceId | WO_OPERATION_RESOURCE_ID | — | ✅ |
| 63 | CstWOResourceTxnsPEOWoOperationTransactionId | WO_OPERATION_TRANSACTION_ID | — | ✅ |
| 64 | CstWOResourceTxnsPEOWorkCenterId | WORK_CENTER_ID | — | ✅ |
| 65 | CstWOResourceTxnsPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |
| 66 | CstWOResourceTxnsPEOWorkOrderOperationId | WORK_ORDER_OPERATION_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
