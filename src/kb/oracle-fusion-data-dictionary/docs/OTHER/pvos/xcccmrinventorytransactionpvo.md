---
id: DOC-OTHER-PVO-XccCmrInventoryTransactionPVO
doc_type: system-doc
title: "XccCmrInventoryTransactionPVO — PVO Cross-Module"
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
  - XccCmrInventoryTransactionPVO
  - xcccmrinventorytransactionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# XccCmrInventoryTransactionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Xcc Cmr Inventory Transaction. Acessa as tabelas: CMR_PURCHASE_ORDER_DTLS, CMR_RCV_DISTRIBUTIONS, CMR_RCV_EVENTS (+6).

**Caminho:** `FscmTopModelAM.FinCcControlEnginePublicModelAM.XccCmrInventoryTransactionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 91 | 9 | 1 | 39 | 43% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_purchase_order_dtls|CMR_PURCHASE_ORDER_DTLS]] — 11 atributos (3 BICC)
- [[cmr_rcv_distributions|CMR_RCV_DISTRIBUTIONS]] — 8 atributos (5 BICC)
- [[cmr_rcv_events|CMR_RCV_EVENTS]] — 37 atributos (1 PKs, 25 BICC)
- [[cmr_rcv_event_costs|CMR_RCV_EVENT_COSTS]] — 2 atributos
- [[cmr_rcv_event_types|CMR_RCV_EVENT_TYPES]] — 1 atributos (1 BICC)
- [[cmr_rcv_transactions|CMR_RCV_TRANSACTIONS]] — 5 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 12 atributos (2 BICC)
- [[per_users|PER_USERS]] — 8 atributos
- [[xla_event_types_vl|XLA_EVENT_TYPES_VL]] — 7 atributos (2 BICC)

---

## ⚙️ Atributos

### [[cmr_purchase_order_dtls|CMR_PURCHASE_ORDER_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchaseOrderDtlsAccrueOnReceiptFlag | ACCRUE_ON_RECEIPT_FLAG | — | — |
| 2 | PurchaseOrderDtlsActiveFlag | ACTIVE_FLAG | — | — |
| 3 | PurchaseOrderDtlsCmrPoDistributionId | CMR_PO_DISTRIBUTION_ID | — | — |
| 4 | PurchaseOrderDtlsConsignedFlag | CONSIGNED_FLAG | — | — |
| 5 | PurchaseOrderDtlsDestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 6 | PurchaseOrderDtlsDistributionNumber | DISTRIBUTION_NUMBER | — | ✅ |
| 7 | PurchaseOrderDtlsEventDate | EVENT_DATE | — | — |
| 8 | PurchaseOrderDtlsExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | — |
| 9 | PurchaseOrderDtlsExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 10 | PurchaseOrderDtlsPoNumber | PO_NUMBER | — | ✅ |
| 11 | PurchaseOrderDtlsSfoPrimaryTradeRelationId | SFO_PRIMARY_TRADE_RELATION_ID | — | — |

### [[cmr_rcv_distributions|CMR_RCV_DISTRIBUTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrRcvDistributionsAccountedQty | ACCOUNTED_QTY | — | ✅ |
| 2 | CmrRcvDistributionsAccountingLineType | ACCOUNTING_LINE_TYPE | — | ✅ |
| 3 | CmrRcvDistributionsCmrSubLedgerId | CMR_SUB_LEDGER_ID | — | — |
| 4 | CmrRcvDistributionsCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 5 | CmrRcvDistributionsEnteredCurrencyAmount | ENTERED_CURRENCY_AMOUNT | — | ✅ |
| 6 | CmrRcvDistributionsEnteredCurrencyCode | ENTERED_CURRENCY_CODE | — | — |
| 7 | CmrRcvDistributionsLedgerAmount | LEDGER_AMOUNT | — | ✅ |
| 8 | CmrRcvDistributionsLedgerCurrencyCode | LEDGER_CURRENCY_CODE | — | — |

### [[cmr_rcv_events|CMR_RCV_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccountingEventId | ACCOUNTING_EVENT_ID | 🔑 | ✅ |
| 2 | CmrRcvEventsAccountedFlag | ACCOUNTED_FLAG | — | ✅ |
| 3 | CmrRcvEventsBudgetaryControlFlag | BUDGETARY_CONTROL_FLAG | — | ✅ |
| 4 | CmrRcvEventsCmrPoDistributionId | CMR_PO_DISTRIBUTION_ID | — | — |
| 5 | CmrRcvEventsCmrRcvTransactionId | CMR_RCV_TRANSACTION_ID | — | — |
| 6 | CmrRcvEventsConsignedFlag | CONSIGNED_FLAG | — | — |
| 7 | CmrRcvEventsCreatedBy | CREATED_BY | — | ✅ |
| 8 | CmrRcvEventsCreationDate | CREATION_DATE | — | ✅ |
| 9 | CmrRcvEventsDestinationTypeCode | DESTINATION_TYPE_CODE | — | — |
| 10 | CmrRcvEventsEncumbranceAccountingFlag | ENCUMBRANCE_ACCOUNTING_FLAG | — | ✅ |
| 11 | CmrRcvEventsEncumbranceReversalAcctAmt | ENCUMBRANCE_REVERSAL_ACCT_AMT | — | — |
| 12 | CmrRcvEventsEncumbranceReversalEntrAmt | ENCUMBRANCE_REVERSAL_ENTR_AMT | — | — |
| 13 | CmrRcvEventsEnteredCurrencyCode | ENTERED_CURRENCY_CODE | — | ✅ |
| 14 | CmrRcvEventsEntityCode | ENTITY_CODE | — | — |
| 15 | CmrRcvEventsEventClassCode | EVENT_CLASS_CODE | — | ✅ |
| 16 | CmrRcvEventsEventId | EVENT_ID | — | — |
| 17 | CmrRcvEventsEventSource | EVENT_SOURCE | — | — |
| 18 | CmrRcvEventsEventTypeCode | EVENT_TYPE_CODE | — | ✅ |
| 19 | CmrRcvEventsFundReservationStatus | FUND_RESERVATION_STATUS | — | ✅ |
| 20 | CmrRcvEventsGlDate | GL_DATE | — | ✅ |
| 21 | CmrRcvEventsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | CmrRcvEventsLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 23 | CmrRcvEventsNonrecoverableTax | NONRECOVERABLE_TAX | — | ✅ |
| 24 | CmrRcvEventsPoUnitPrice | PO_UNIT_PRICE | — | ✅ |
| 25 | CmrRcvEventsPrimaryQty | PRIMARY_QTY | — | ✅ |
| 26 | CmrRcvEventsPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 27 | CmrRcvEventsReceiptCreationDate | RECEIPT_CREATION_DATE | — | — |
| 28 | CmrRcvEventsSlaTransactionNumber | SLA_TRANSACTION_NUMBER | — | ✅ |
| 29 | CmrRcvEventsSourceDocNumber | SOURCE_DOC_NUMBER | — | ✅ |
| 30 | CmrRcvEventsSourceDocQty | SOURCE_DOC_QTY | — | ✅ |
| 31 | CmrRcvEventsSourceDocUomCode | SOURCE_DOC_UOM_CODE | — | ✅ |
| 32 | CmrRcvEventsTransactionAmt | TRANSACTION_AMT | — | ✅ |
| 33 | CmrRcvEventsTransactionDate | TRANSACTION_DATE | — | ✅ |
| 34 | CmrRcvEventsTransactionQty | TRANSACTION_QTY | — | ✅ |
| 35 | CmrRcvEventsTransactionTypeCode | TRANSACTION_TYPE_CODE | — | — |
| 36 | CmrRcvEventsTransactionUomCode | TRANSACTION_UOM_CODE | — | ✅ |
| 37 | CmrRcvEventsTransferPrice | TRANSFER_PRICE | — | ✅ |

### [[cmr_rcv_event_costs|CMR_RCV_EVENT_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrRcvEventCostsAccountingEventId | ACCOUNTING_EVENT_ID | — | — |
| 2 | CmrRcvEventCostsEventCostId | EVENT_COST_ID | — | — |

### [[cmr_rcv_event_types|CMR_RCV_EVENT_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RcvEventTypesTransactionType | TRANSACTION_TYPE | — | ✅ |

### [[cmr_rcv_transactions|CMR_RCV_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrRcvTransactionsCmrRcvTransactionId | CMR_RCV_TRANSACTION_ID | — | — |
| 2 | CmrRcvTransactionsTransactionDate | TRANSACTION_DATE | — | ✅ |
| 3 | CmrRcvTransactionsTransactionQuantity | TRANSACTION_QUANTITY | — | — |
| 4 | CmrRcvTransactionsTransactionType | TRANSACTION_TYPE | — | — |
| 5 | CmrRcvTransactionsTransactionUomCode | TRANSACTION_UOM_CODE | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrRcvEventsPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | CmrRcvEventsPersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | CmrRcvEventsPersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | CmrRcvEventsPersonCreatedByFullName | FULL_NAME | — | — |
| 5 | CmrRcvEventsPersonCreatedByPersonId | PERSON_ID | — | — |
| 6 | CmrRcvEventsPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 7 | CmrRcvEventsPersonLastUpdateByDisplayName | DISPLAY_NAME | — | ✅ |
| 8 | CmrRcvEventsPersonLastUpdateByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 9 | CmrRcvEventsPersonLastUpdateByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 10 | CmrRcvEventsPersonLastUpdateByFullName | FULL_NAME | — | — |
| 11 | CmrRcvEventsPersonLastUpdateByPersonId | PERSON_ID | — | — |
| 12 | CmrRcvEventsPersonLastUpdateByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrRcvEventsUserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | CmrRcvEventsUserCreatedByPersonId | PERSON_ID | — | — |
| 3 | CmrRcvEventsUserCreatedByUserId | USER_ID | — | — |
| 4 | CmrRcvEventsUserCreatedByUsername | USERNAME | — | — |
| 5 | CmrRcvEventsUserLastUpdateByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | CmrRcvEventsUserLastUpdateByPersonId | PERSON_ID | — | — |
| 7 | CmrRcvEventsUserLastUpdateByUserId | USER_ID | — | — |
| 8 | CmrRcvEventsUserLastUpdateByUsername | USERNAME | — | — |

### [[xla_event_types_vl|XLA_EVENT_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventTypeTranslationApplicationId | APPLICATION_ID | — | — |
| 2 | EventTypeTranslationDescription | DESCRIPTION | — | ✅ |
| 3 | EventTypeTranslationEntityCode | ENTITY_CODE | — | — |
| 4 | EventTypeTranslationEventClassCode | EVENT_CLASS_CODE | — | — |
| 5 | EventTypeTranslationEventTypeCode | EVENT_TYPE_CODE | — | — |
| 6 | EventTypeTranslationName | NAME | — | ✅ |
| 7 | EventTypeTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
