---
id: DOC-OTHER-PVO-ManualAdjustmentExtractPVO
doc_type: system-doc
title: "ManualAdjustmentExtractPVO — PVO Cross-Module"
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
  - ManualAdjustmentExtractPVO
  - manualadjustmentextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ManualAdjustmentExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Manual Adjustment Extract. Acessa as tabelas: CJM_MANUAL_ADJUSTMENTS_ALL_B.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CjmBiccExtractAM.ManualAdjustmentExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 54 | 1 | 1 | 54 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cjm_manual_adjustments_all_b|CJM_MANUAL_ADJUSTMENTS_ALL_B]] — 54 atributos (1 PKs, 54 BICC)

---

## ⚙️ Atributos

### [[cjm_manual_adjustments_all_b|CJM_MANUAL_ADJUSTMENTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccrualReversalFlag | ACCRUAL_REVERSAL_FLAG | — | ✅ |
| 2 | AccrualTypeCode | ACCRUAL_TYPE_CODE | — | ✅ |
| 3 | AdjustmentAmount | ADJUSTMENT_AMOUNT | — | ✅ |
| 4 | AdjustmentCurrencyCode | ADJUSTMENT_CURRENCY_CODE | — | ✅ |
| 5 | AdjustmentDate | ADJUSTMENT_DATE | — | ✅ |
| 6 | AdjustmentReasonId | ADJUSTMENT_REASON_ID | — | ✅ |
| 7 | AdjustmentTypeCode | ADJUSTMENT_TYPE_CODE | — | ✅ |
| 8 | AdjustmentTypeId | ADJUSTMENT_TYPE_ID | — | ✅ |
| 9 | ApprovedBy | APPROVED_BY | — | ✅ |
| 10 | ApprovedDate | APPROVED_DATE | — | ✅ |
| 11 | BillToCustomerId | BILL_TO_CUSTOMER_ID | — | ✅ |
| 12 | BillToLocationId | BILL_TO_LOCATION_ID | — | ✅ |
| 13 | CreatedBy | CREATED_BY | — | ✅ |
| 14 | CreationDate | CREATION_DATE | — | ✅ |
| 15 | CustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | ✅ |
| 16 | ExchangeRateDate | EXCHANGE_RATE_DATE | — | ✅ |
| 17 | ExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 18 | ExpectedReceiptDate | EXPECTED_RECEIPT_DATE | — | ✅ |
| 19 | InvoiceDate | INVOICE_DATE | — | ✅ |
| 20 | InvoiceId | INVOICE_ID | — | ✅ |
| 21 | InvoiceLineNumber | INVOICE_LINE_NUMBER | — | ✅ |
| 22 | InvoiceNumber | INVOICE_NUMBER | — | ✅ |
| 23 | InvoiceSourceApplication | INVOICE_SOURCE_APPLICATION | — | ✅ |
| 24 | InvoiceSourceCode | INVOICE_SOURCE_CODE | — | ✅ |
| 25 | ItemId | ITEM_ID | — | ✅ |
| 26 | ItemLevelCode | ITEM_LEVEL_CODE | — | ✅ |
| 27 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 29 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 30 | ManualAdjustmentId | MANUAL_ADJUSTMENT_ID | 🔑 | ✅ |
| 31 | ManualAdjustmentNumber | MANUAL_ADJUSTMENT_NUMBER | — | ✅ |
| 32 | ObjectId | OBJECT_ID | — | ✅ |
| 33 | ObjectLineId | OBJECT_LINE_ID | — | ✅ |
| 34 | ObjectType | OBJECT_TYPE | — | ✅ |
| 35 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 36 | OrigObjectLineNum | ORIG_OBJECT_LINE_NUM | — | ✅ |
| 37 | OrigObjectNumber | ORIG_OBJECT_NUMBER | — | ✅ |
| 38 | OwnerId | OWNER_ID | — | ✅ |
| 39 | PoDate | PO_DATE | — | ✅ |
| 40 | PoHeaderId | PO_HEADER_ID | — | ✅ |
| 41 | PoNumber | PO_NUMBER | — | ✅ |
| 42 | ProgramHeaderId | PROGRAM_HEADER_ID | — | ✅ |
| 43 | ProgramLineId | PROGRAM_LINE_ID | — | ✅ |
| 44 | ReceiptId | RECEIPT_ID | — | ✅ |
| 45 | ReceiptNumber | RECEIPT_NUMBER | — | ✅ |
| 46 | RequestedGlDate | REQUESTED_GL_DATE | — | ✅ |
| 47 | ShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 48 | SourceUtilizationId | SOURCE_UTILIZATION_ID | — | ✅ |
| 49 | StatusCode | STATUS_CODE | — | ✅ |
| 50 | TpItemId | TP_ITEM_ID | — | ✅ |
| 51 | TransactionDate | TRANSACTION_DATE | — | ✅ |
| 52 | TransactionId | TRANSACTION_ID | — | ✅ |
| 53 | VendorId | VENDOR_ID | — | ✅ |
| 54 | VendorSiteId | VENDOR_SITE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
