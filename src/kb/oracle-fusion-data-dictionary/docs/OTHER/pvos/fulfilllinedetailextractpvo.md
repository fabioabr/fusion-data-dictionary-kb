---
id: DOC-OTHER-PVO-FulfillLineDetailExtractPVO
doc_type: system-doc
title: "FulfillLineDetailExtractPVO — PVO Cross-Module"
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
  - FulfillLineDetailExtractPVO
  - fulfilllinedetailextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FulfillLineDetailExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fulfill Line Detail Extract. Acessa as tabelas: DOO_FULFILL_LINE_DETAILS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.FulfillLineDetailExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 36 | 1 | 1 | 36 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_fulfill_line_details|DOO_FULFILL_LINE_DETAILS]] — 36 atributos (1 PKs, 36 BICC)

---

## ⚙️ Atributos

### [[doo_fulfill_line_details|DOO_FULFILL_LINE_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FulfillLineDetailActualDeliveryDate | ACTUAL_DELIVERY_DATE | — | ✅ |
| 2 | FulfillLineDetailAvailabilityShipDate | AVAILABILITY_SHIP_DATE | — | ✅ |
| 3 | FulfillLineDetailBillOfLadingNumber | BILL_OF_LADING_NUMBER | — | ✅ |
| 4 | FulfillLineDetailBillingTransactionAmount | BILLING_TRANSACTION_AMOUNT | — | ✅ |
| 5 | FulfillLineDetailBillingTransactionDate | BILLING_TRANSACTION_DATE | — | ✅ |
| 6 | FulfillLineDetailBillingTransactionNumber | BILLING_TRANSACTION_NUMBER | — | ✅ |
| 7 | FulfillLineDetailCreatedBy | CREATED_BY | — | ✅ |
| 8 | FulfillLineDetailCreationDate | CREATION_DATE | — | ✅ |
| 9 | FulfillLineDetailCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | ✅ |
| 10 | FulfillLineDetailDeliveryName | DELIVERY_NAME | — | ✅ |
| 11 | FulfillLineDetailDeltaType | DELTA_TYPE | — | ✅ |
| 12 | FulfillLineDetailExceptionFlag | EXCEPTION_FLAG | — | ✅ |
| 13 | FulfillLineDetailFulfillLineDetailId | FULFILL_LINE_DETAIL_ID | 🔑 | ✅ |
| 14 | FulfillLineDetailFulfillLineId | FULFILL_LINE_ID | — | ✅ |
| 15 | FulfillLineDetailLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | FulfillLineDetailLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | FulfillLineDetailLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | FulfillLineDetailModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 19 | FulfillLineDetailObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 20 | FulfillLineDetailQuantity | QUANTITY | — | ✅ |
| 21 | FulfillLineDetailReferenceFlineDetailId | REFERENCE_FLINE_DETAIL_ID | — | ✅ |
| 22 | FulfillLineDetailRmaReceiptDate | RMA_RECEIPT_DATE | — | ✅ |
| 23 | FulfillLineDetailRmaReceiptLineNumber | RMA_RECEIPT_LINE_NUMBER | — | ✅ |
| 24 | FulfillLineDetailRmaReceiptNumber | RMA_RECEIPT_NUMBER | — | ✅ |
| 25 | FulfillLineDetailRmaReceiptTransactionId | RMA_RECEIPT_TRANSACTION_ID | — | ✅ |
| 26 | FulfillLineDetailSecondaryQuantity | SECONDARY_QUANTITY | — | ✅ |
| 27 | FulfillLineDetailShipmentRequestedQuantity | SHIPMENT_REQUESTED_QUANTITY | — | ✅ |
| 28 | FulfillLineDetailStatus | STATUS | — | ✅ |
| 29 | FulfillLineDetailStatusAsofDate | STATUS_ASOF_DATE | — | ✅ |
| 30 | FulfillLineDetailTaskType | TASK_TYPE | — | ✅ |
| 31 | FulfillLineDetailTrackingNumber | TRACKING_NUMBER | — | ✅ |
| 32 | FulfillLineDetailTradeComplianceCode | TRADE_COMPLIANCE_CODE | — | ✅ |
| 33 | FulfillLineDetailTradeComplianceExplanation | TRADE_COMPLIANCE_EXPLANATION | — | ✅ |
| 34 | FulfillLineDetailTradeComplianceResultCode | TRADE_COMPLIANCE_RESULT_CODE | — | ✅ |
| 35 | FulfillLineDetailTradeComplianceTypeCode | TRADE_COMPLIANCE_TYPE_CODE | — | ✅ |
| 36 | FulfillLineDetailWaybillNumber | WAYBILL_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
