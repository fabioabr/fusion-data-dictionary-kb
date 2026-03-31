---
id: DOC-OTHER-PVO-CmrRcvEventsExtractPVO
doc_type: system-doc
title: "CmrRcvEventsExtractPVO — PVO Cross-Module"
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
  - CmrRcvEventsExtractPVO
  - cmrrcveventsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrRcvEventsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cmr Rcv Events Extract. Acessa as tabelas: CMR_RCV_EVENTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CmrBiccExtractAM.CmrRcvEventsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 92 | 1 | 1 | 92 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_rcv_events|CMR_RCV_EVENTS]] — 92 atributos (1 PKs, 92 BICC)

---

## ⚙️ Atributos

### [[cmr_rcv_events|CMR_RCV_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrRcvEventsPEOAccountedFlag | ACCOUNTED_FLAG | — | ✅ |
| 2 | CmrRcvEventsPEOAccountingEventId | ACCOUNTING_EVENT_ID | 🔑 | ✅ |
| 3 | CmrRcvEventsPEOBillToBusinessUnitId | BILL_TO_BUSINESS_UNIT_ID | — | ✅ |
| 4 | CmrRcvEventsPEOBudgetaryControlFlag | BUDGETARY_CONTROL_FLAG | — | ✅ |
| 5 | CmrRcvEventsPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 6 | CmrRcvEventsPEOCmrPoDistributionId | CMR_PO_DISTRIBUTION_ID | — | ✅ |
| 7 | CmrRcvEventsPEOCmrPoLineLocationId | CMR_PO_LINE_LOCATION_ID | — | ✅ |
| 8 | CmrRcvEventsPEOCmrRcvTransactionId | CMR_RCV_TRANSACTION_ID | — | ✅ |
| 9 | CmrRcvEventsPEOConsignedAcctDistBasis | CONSIGNED_ACCT_DIST_BASIS | — | ✅ |
| 10 | CmrRcvEventsPEOConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 11 | CmrRcvEventsPEOCreateAcctDistBasis | CREATE_ACCT_DIST_BASIS | — | ✅ |
| 12 | CmrRcvEventsPEOCreatedBy | CREATED_BY | — | ✅ |
| 13 | CmrRcvEventsPEOCreationDate | CREATION_DATE | — | ✅ |
| 14 | CmrRcvEventsPEOCstInvTransactionId | CST_INV_TRANSACTION_ID | — | ✅ |
| 15 | CmrRcvEventsPEODeliverToBusinessUnitId | DELIVER_TO_BUSINESS_UNIT_ID | — | ✅ |
| 16 | CmrRcvEventsPEODeliverToInventoryOrgId | DELIVER_TO_INVENTORY_ORG_ID | — | ✅ |
| 17 | CmrRcvEventsPEODooFullfillLineId | DOO_FULLFILL_LINE_ID | — | ✅ |
| 18 | CmrRcvEventsPEOEncumbranceAccountingFlag | ENCUMBRANCE_ACCOUNTING_FLAG | — | ✅ |
| 19 | CmrRcvEventsPEOEncumbranceReversalAcctAmt | ENCUMBRANCE_REVERSAL_ACCT_AMT | — | ✅ |
| 20 | CmrRcvEventsPEOEncumbranceReversalEntrAmt | ENCUMBRANCE_REVERSAL_ENTR_AMT | — | ✅ |
| 21 | CmrRcvEventsPEOEntityCode | ENTITY_CODE | — | ✅ |
| 22 | CmrRcvEventsPEOErrorCode | ERROR_CODE | — | ✅ |
| 23 | CmrRcvEventsPEOEventClassCode | EVENT_CLASS_CODE | — | ✅ |
| 24 | CmrRcvEventsPEOEventDate | EVENT_DATE | — | ✅ |
| 25 | CmrRcvEventsPEOEventId | EVENT_ID | — | ✅ |
| 26 | CmrRcvEventsPEOEventSource | EVENT_SOURCE | — | ✅ |
| 27 | CmrRcvEventsPEOEventSourceId | EVENT_SOURCE_ID | — | ✅ |
| 28 | CmrRcvEventsPEOEventTransactionId | EVENT_TRANSACTION_ID | — | ✅ |
| 29 | CmrRcvEventsPEOEventTxnTableName | EVENT_TXN_TABLE_NAME | — | ✅ |
| 30 | CmrRcvEventsPEOEventTypeCode | EVENT_TYPE_CODE | — | ✅ |
| 31 | CmrRcvEventsPEOExchangeRate | EXCHANGE_RATE | — | ✅ |
| 32 | CmrRcvEventsPEOExpRetroPriceFlag | EXP_RETRO_PRICE_FLAG | — | ✅ |
| 33 | CmrRcvEventsPEOFiscalDocAccessKnum | FISCAL_DOC_ACCESS_KNUM | — | ✅ |
| 34 | CmrRcvEventsPEOFiscalDocLineNumber | FISCAL_DOC_LINE_NUMBER | — | ✅ |
| 35 | CmrRcvEventsPEOFiscalDocNumber | FISCAL_DOC_NUMBER | — | ✅ |
| 36 | CmrRcvEventsPEOFiscalDocumentDetailId | FISCAL_DOCUMENT_DETAIL_ID | — | ✅ |
| 37 | CmrRcvEventsPEOFundReservationStatus | FUND_RESERVATION_STATUS | — | ✅ |
| 38 | CmrRcvEventsPEOGlDate | GL_DATE | — | ✅ |
| 39 | CmrRcvEventsPEOInvShippingTransactionId | INV_SHIPPING_TRANSACTION_ID | — | ✅ |
| 40 | CmrRcvEventsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 41 | CmrRcvEventsPEOInventoryOrgId | INVENTORY_ORG_ID | — | ✅ |
| 42 | CmrRcvEventsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 43 | CmrRcvEventsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 44 | CmrRcvEventsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 45 | CmrRcvEventsPEOLeTimezoneCode | LE_TIMEZONE_CODE | — | ✅ |
| 46 | CmrRcvEventsPEOLedgerId | LEDGER_ID | — | ✅ |
| 47 | CmrRcvEventsPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 48 | CmrRcvEventsPEOManualReceiptReqdFlag | MANUAL_RECEIPT_REQD_FLAG | — | ✅ |
| 49 | CmrRcvEventsPEOPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | ✅ |
| 50 | CmrRcvEventsPEOPjcTxnStatusCode | PJC_TXN_STATUS_CODE | — | ✅ |
| 51 | CmrRcvEventsPEOPoItemDescription | PO_ITEM_DESCRIPTION | — | ✅ |
| 52 | CmrRcvEventsPEOPoLineLocationId | PO_LINE_LOCATION_ID | — | ✅ |
| 53 | CmrRcvEventsPEOPoSyncCallFlag | PO_SYNC_CALL_FLAG | — | ✅ |
| 54 | CmrRcvEventsPEOPrimaryQty | PRIMARY_QTY | — | ✅ |
| 55 | CmrRcvEventsPEOPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 56 | CmrRcvEventsPEOPriorBusinessUnitId | PRIOR_BUSINESS_UNIT_ID | — | ✅ |
| 57 | CmrRcvEventsPEOPriorInventoryOrgId | PRIOR_INVENTORY_ORG_ID | — | ✅ |
| 58 | CmrRcvEventsPEOProcessingGroupId | PROCESSING_GROUP_ID | — | ✅ |
| 59 | CmrRcvEventsPEOReceiptCreationDate | RECEIPT_CREATION_DATE | — | ✅ |
| 60 | CmrRcvEventsPEORefFiscalDocAccessKnum | REF_FISCAL_DOC_ACCESS_KNUM | — | ✅ |
| 61 | CmrRcvEventsPEOReferenceDocNumber | REFERENCE_DOC_NUMBER | — | ✅ |
| 62 | CmrRcvEventsPEORootDeliverTxnDate | ROOT_DELIVER_TXN_DATE | — | ✅ |
| 63 | CmrRcvEventsPEORootReceiptEventDate | ROOT_RECEIPT_EVENT_DATE | — | ✅ |
| 64 | CmrRcvEventsPEOSecondaryTransactionQty | SECONDARY_TRANSACTION_QTY | — | ✅ |
| 65 | CmrRcvEventsPEOSecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 66 | CmrRcvEventsPEOShipFromInvOrgId | SHIP_FROM_INV_ORG_ID | — | ✅ |
| 67 | CmrRcvEventsPEOShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 68 | CmrRcvEventsPEOShipmentLineId | SHIPMENT_LINE_ID | — | ✅ |
| 69 | CmrRcvEventsPEOShipmentNumber | SHIPMENT_NUMBER | — | ✅ |
| 70 | CmrRcvEventsPEOSlaTransactionNumber | SLA_TRANSACTION_NUMBER | — | ✅ |
| 71 | CmrRcvEventsPEOSourceDocDistribNumber | SOURCE_DOC_DISTRIB_NUMBER | — | ✅ |
| 72 | CmrRcvEventsPEOSourceDocLineNumber | SOURCE_DOC_LINE_NUMBER | — | ✅ |
| 73 | CmrRcvEventsPEOSourceDocNumber | SOURCE_DOC_NUMBER | — | ✅ |
| 74 | CmrRcvEventsPEOSourceDocQty | SOURCE_DOC_QTY | — | ✅ |
| 75 | CmrRcvEventsPEOSourceDocShipmentNumber | SOURCE_DOC_SHIPMENT_NUMBER | — | ✅ |
| 76 | CmrRcvEventsPEOSourceDocUomCode | SOURCE_DOC_UOM_CODE | — | ✅ |
| 77 | CmrRcvEventsPEOTradeEventId | TRADE_EVENT_ID | — | ✅ |
| 78 | CmrRcvEventsPEOTradeOverheadId | TRADE_OVERHEAD_ID | — | ✅ |
| 79 | CmrRcvEventsPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 80 | CmrRcvEventsPEOTransactionId | TRANSACTION_ID | — | ✅ |
| 81 | CmrRcvEventsPEOTransactionQty | TRANSACTION_QTY | — | ✅ |
| 82 | CmrRcvEventsPEOTransactionReversalFlag | TRANSACTION_REVERSAL_FLAG | — | ✅ |
| 83 | CmrRcvEventsPEOTransactionTypeCode | TRANSACTION_TYPE_CODE | — | ✅ |
| 84 | CmrRcvEventsPEOTransactionUomCode | TRANSACTION_UOM_CODE | — | ✅ |
| 85 | CmrRcvEventsPEOTransferOrderDistId | TRANSFER_ORDER_DIST_ID | — | ✅ |
| 86 | CmrRcvEventsPEOTransferOrderHeaderId | TRANSFER_ORDER_HEADER_ID | — | ✅ |
| 87 | CmrRcvEventsPEOTransferOrderLineId | TRANSFER_ORDER_LINE_ID | — | ✅ |
| 88 | CmrRcvEventsPEOTropChargeLineId | TROP_CHARGE_LINE_ID | — | ✅ |
| 89 | CmrRcvEventsPEOUninvDelQty | UNINV_DEL_QTY | — | ✅ |
| 90 | CmrRcvEventsPEOVendorId | VENDOR_ID | — | ✅ |
| 91 | CmrRcvEventsPEOVendorSiteId | VENDOR_SITE_ID | — | ✅ |
| 92 | CmrRcvEventsPEOXccDataSetId | XCC_DATA_SET_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
