---
id: DOC-AR-PVO-CmrAllPeriodCloseTxnsPVO
doc_type: system-doc
title: "CmrAllPeriodCloseTxnsPVO — PVO Accounts Receivable"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ar
  - data-dictionary
  - pvo
  - bicc
aliases:
  - CmrAllPeriodCloseTxnsPVO
  - cmrallperiodclosetxnspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrAllPeriodCloseTxnsPVO

## 📌 Visão Geral

Extrai todas as transações pendentes no fechamento de período do módulo de Contas a Receber, incluindo erros de validação. Essencial para o processo de fechamento contábil mensal, identificando transações que impedem o encerramento do período.

**Caminho:** `FscmTopModelAM.ReceiptAccountingAM.CmrAllPeriodCloseTxnsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 79 | 3 | 2 | 59 | 75% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_all_period_valerr_txns_v|CMR_ALL_PERIOD_VALERR_TXNS_V]] — 31 atributos (2 PKs, 24 BICC)
- [[cmr_period_close_actions_v|CMR_PERIOD_CLOSE_ACTIONS_V]] — 28 atributos (15 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 20 atributos (20 BICC)

---

## ⚙️ Atributos

### [[cmr_all_period_valerr_txns_v|CMR_ALL_PERIOD_VALERR_TXNS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrAllPeriodCloseTxnsPEOBillToBusinessUnitId | BILL_TO_BUSINESS_UNIT_ID | — | ✅ |
| 2 | CmrAllPeriodCloseTxnsPEOBuId | BU_ID | — | — |
| 3 | CmrAllPeriodCloseTxnsPEOConvertToLetz | CONVERT_TO_LETZ | — | — |
| 4 | CmrAllPeriodCloseTxnsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 5 | CmrAllPeriodCloseTxnsPEODestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 6 | CmrAllPeriodCloseTxnsPEODistributionType | DISTRIBUTION_TYPE | — | ✅ |
| 7 | CmrAllPeriodCloseTxnsPEODocumentTypeCode | DOCUMENT_TYPE_CODE | — | ✅ |
| 8 | CmrAllPeriodCloseTxnsPEOEndDate | END_DATE | — | ✅ |
| 9 | CmrAllPeriodCloseTxnsPEOErrorCode | ERROR_CODE | — | ✅ |
| 10 | CmrAllPeriodCloseTxnsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 11 | CmrAllPeriodCloseTxnsPEOInventoryOrgId | INVENTORY_ORG_ID | — | ✅ |
| 12 | CmrAllPeriodCloseTxnsPEOItemOrganizationId | ITEM_ORGANIZATION_ID | — | — |
| 13 | CmrAllPeriodCloseTxnsPEOLeTimeOffset | LE_TIME_OFFSET | — | — |
| 14 | CmrAllPeriodCloseTxnsPEOLedgerId | LEDGER_ID | — | — |
| 15 | CmrAllPeriodCloseTxnsPEOPeriodName | PERIOD_NAME | — | ✅ |
| 16 | CmrAllPeriodCloseTxnsPEOPeriodNum | PERIOD_NUM | — | ✅ |
| 17 | CmrAllPeriodCloseTxnsPEOPeriodSetName | PERIOD_SET_NAME | — | ✅ |
| 18 | CmrAllPeriodCloseTxnsPEOPeriodType | PERIOD_TYPE | — | ✅ |
| 19 | CmrAllPeriodCloseTxnsPEOPeriodYear | PERIOD_YEAR | — | ✅ |
| 20 | CmrAllPeriodCloseTxnsPEOServerEndDate | SERVER_END_DATE | — | — |
| 21 | CmrAllPeriodCloseTxnsPEOServerStartDate | SERVER_START_DATE | — | — |
| 22 | CmrAllPeriodCloseTxnsPEOSourceTable | SOURCE_TABLE | 🔑 | ✅ |
| 23 | CmrAllPeriodCloseTxnsPEOStartDate | START_DATE | — | ✅ |
| 24 | CmrAllPeriodCloseTxnsPEOTransactionAmt | TRANSACTION_AMT | — | ✅ |
| 25 | CmrAllPeriodCloseTxnsPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 26 | CmrAllPeriodCloseTxnsPEOTransactionId | TRANSACTION_ID | 🔑 | ✅ |
| 27 | CmrAllPeriodCloseTxnsPEOTransactionLineNumber | TRANSACTION_LINE_NUMBER | — | ✅ |
| 28 | CmrAllPeriodCloseTxnsPEOTransactionNumber | TRANSACTION_NUMBER | — | ✅ |
| 29 | CmrAllPeriodCloseTxnsPEOTransactionQty | TRANSACTION_QTY | — | ✅ |
| 30 | CmrAllPeriodCloseTxnsPEOTransactionType | TRANSACTION_TYPE | — | ✅ |
| 31 | CmrAllPeriodCloseTxnsPEOTransactionUomCode | TRANSACTION_UOM_CODE | — | ✅ |

### [[cmr_period_close_actions_v|CMR_PERIOD_CLOSE_ACTIONS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrPeriodCloseActionsPEOBuId | BU_ID | — | ✅ |
| 2 | CmrPeriodCloseActionsPEOEndDate | END_DATE | — | ✅ |
| 3 | CmrPeriodCloseActionsPEOIntransitPoAccJobFlag | INTRANSIT_PO_ACC_JOB_FLAG | — | — |
| 4 | CmrPeriodCloseActionsPEOIntransitPoRptNotAccCount | INTRANSIT_PO_RPT_NOT_ACC_COUNT | — | — |
| 5 | CmrPeriodCloseActionsPEOLeTimeOffset | LE_TIME_OFFSET | — | — |
| 6 | CmrPeriodCloseActionsPEOLedgerId | LEDGER_ID | — | — |
| 7 | CmrPeriodCloseActionsPEOPendingAccrClrCount | PENDING_ACCR_CLR_COUNT | — | ✅ |
| 8 | CmrPeriodCloseActionsPEOPendingDistCount | PENDING_DIST_COUNT | — | ✅ |
| 9 | CmrPeriodCloseActionsPEOPendingIntReversalsCount | PENDING_INT_REVERSALS_COUNT | — | — |
| 10 | CmrPeriodCloseActionsPEOPendingInvoiceIntfCount | PENDING_INVOICE_INTF_COUNT | — | ✅ |
| 11 | CmrPeriodCloseActionsPEOPendingInvoiceVarCount | PENDING_INVOICE_VAR_COUNT | — | ✅ |
| 12 | CmrPeriodCloseActionsPEOPendingPeriodAccrCount | PENDING_PERIOD_ACCR_COUNT | — | ✅ |
| 13 | CmrPeriodCloseActionsPEOPendingReceiptCount | PENDING_RECEIPT_COUNT | — | ✅ |
| 14 | CmrPeriodCloseActionsPEOPendingReceiptIntfCount | PENDING_RECEIPT_INTF_COUNT | — | ✅ |
| 15 | CmrPeriodCloseActionsPEOPendingRpaCount | PENDING_RPA_COUNT | — | ✅ |
| 16 | CmrPeriodCloseActionsPEOPendingTraCount | PENDING_TRA_COUNT | — | ✅ |
| 17 | CmrPeriodCloseActionsPEOPendingTraIntfCount | PENDING_TRA_INTF_COUNT | — | ✅ |
| 18 | CmrPeriodCloseActionsPEOPeriodName | PERIOD_NAME | — | ✅ |
| 19 | CmrPeriodCloseActionsPEOPeriodNum | PERIOD_NUM | — | — |
| 20 | CmrPeriodCloseActionsPEOPeriodSetName | PERIOD_SET_NAME | — | — |
| 21 | CmrPeriodCloseActionsPEOPeriodType | PERIOD_TYPE | — | — |
| 22 | CmrPeriodCloseActionsPEOPeriodYear | PERIOD_YEAR | — | — |
| 23 | CmrPeriodCloseActionsPEOServerEndDate | SERVER_END_DATE | — | — |
| 24 | CmrPeriodCloseActionsPEOServerStartDate | SERVER_START_DATE | — | — |
| 25 | CmrPeriodCloseActionsPEOStartDate | START_DATE | — | — |
| 26 | CmrPeriodCloseActionsPEOUnimportedInvoiceCount | UNIMPORTED_INVOICE_COUNT | — | ✅ |
| 27 | CmrPeriodCloseActionsPEOUnimportedReceiptCount | UNIMPORTED_RECEIPT_COUNT | — | ✅ |
| 28 | CmrPeriodCloseActionsPEOUninterfacedIntShptsCount | UNINTERFACED_INT_SHPTS_COUNT | — | — |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOBusinessUnitId | BU_ID | — | ✅ |
| 2 | BusinessUnitPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | BusinessUnitPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | BusinessUnitPEODateFrom | DATE_FROM | — | ✅ |
| 5 | BusinessUnitPEODateTo | DATE_TO | — | ✅ |
| 6 | BusinessUnitPEODefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | ✅ |
| 7 | BusinessUnitPEODefaultSetId | DEFAULT_SET_ID | — | ✅ |
| 8 | BusinessUnitPEOEnabledForHrFlag | ENABLED_FOR_HR_FLAG | — | ✅ |
| 9 | BusinessUnitPEOEnterpriseId | BUSINESS_GROUP_ID | — | ✅ |
| 10 | BusinessUnitPEOFinancialsBusinessUnitId | FIN_BUSINESS_UNIT_ID | — | ✅ |
| 11 | BusinessUnitPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | BusinessUnitPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | BusinessUnitPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | BusinessUnitPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 15 | BusinessUnitPEOLocationId | LOCATION_ID | — | ✅ |
| 16 | BusinessUnitPEOManagerId | MANAGER_ID | — | ✅ |
| 17 | BusinessUnitPEOName | BU_NAME | — | ✅ |
| 18 | BusinessUnitPEOPrimaryLedgerId | PRIMARY_LEDGER_ID | — | ✅ |
| 19 | BusinessUnitPEOShortCode | SHORT_CODE | — | ✅ |
| 20 | BusinessUnitPEOStatus | STATUS | — | ✅ |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
