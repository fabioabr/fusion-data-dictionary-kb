---
id: DOC-OTHER-PVO-CmrFiscalDocumentDetailsExtractPVO
doc_type: system-doc
title: "CmrFiscalDocumentDetailsExtractPVO — PVO Cross-Module"
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
  - CmrFiscalDocumentDetailsExtractPVO
  - cmrfiscaldocumentdetailsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrFiscalDocumentDetailsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cmr Fiscal Document Details Extract. Acessa as tabelas: CMR_FISCAL_DOCUMENT_DETAILS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CmrBiccExtractAM.CmrFiscalDocumentDetailsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 47 | 1 | 1 | 47 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_fiscal_document_details|CMR_FISCAL_DOCUMENT_DETAILS]] — 47 atributos (1 PKs, 47 BICC)

---

## ⚙️ Atributos

### [[cmr_fiscal_document_details|CMR_FISCAL_DOCUMENT_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrFiscalDocumentDetailsPEOBillToBusinessUnitId | BILL_TO_BUSINESS_UNIT_ID | — | ✅ |
| 2 | CmrFiscalDocumentDetailsPEOChargeAmount | CHARGE_AMOUNT | — | ✅ |
| 3 | CmrFiscalDocumentDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | CmrFiscalDocumentDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | CmrFiscalDocumentDetailsPEOFdAccessKeyNumber | FD_ACCESS_KEY_NUMBER | — | ✅ |
| 6 | CmrFiscalDocumentDetailsPEOFdAcknowledgedDate | FD_ACKNOWLEDGED_DATE | — | ✅ |
| 7 | CmrFiscalDocumentDetailsPEOFdCurrencyCode | FD_CURRENCY_CODE | — | ✅ |
| 8 | CmrFiscalDocumentDetailsPEOFdCurrencyConversionDate | FD_CURRENCY_CONVERSION_DATE | — | ✅ |
| 9 | CmrFiscalDocumentDetailsPEOFdCurrencyConversionRate | FD_CURRENCY_CONVERSION_RATE | — | ✅ |
| 10 | CmrFiscalDocumentDetailsPEOFdCurrencyConversionType | FD_CURRENCY_CONVERSION_TYPE | — | ✅ |
| 11 | CmrFiscalDocumentDetailsPEOFdDocumentType | FD_DOCUMENT_TYPE | — | ✅ |
| 12 | CmrFiscalDocumentDetailsPEOFdHeaderId | FD_HEADER_ID | — | ✅ |
| 13 | CmrFiscalDocumentDetailsPEOFdLineId | FD_LINE_ID | — | ✅ |
| 14 | CmrFiscalDocumentDetailsPEOFdLineNumber | FD_LINE_NUMBER | — | ✅ |
| 15 | CmrFiscalDocumentDetailsPEOFdLineQuantity | FD_LINE_QUANTITY | — | ✅ |
| 16 | CmrFiscalDocumentDetailsPEOFdLineType | FD_LINE_TYPE | — | ✅ |
| 17 | CmrFiscalDocumentDetailsPEOFdLineUnitPrice | FD_LINE_UNIT_PRICE | — | ✅ |
| 18 | CmrFiscalDocumentDetailsPEOFdScheduleId | FD_SCHEDULE_ID | — | ✅ |
| 19 | CmrFiscalDocumentDetailsPEOFdUomCode | FD_UOM_CODE | — | ✅ |
| 20 | CmrFiscalDocumentDetailsPEOFiscalDocumentDetailId | FISCAL_DOCUMENT_DETAIL_ID | 🔑 | ✅ |
| 21 | CmrFiscalDocumentDetailsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 22 | CmrFiscalDocumentDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | CmrFiscalDocumentDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 24 | CmrFiscalDocumentDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 25 | CmrFiscalDocumentDetailsPEOProcessedByRaFlag | PROCESSED_BY_RA_FLAG | — | ✅ |
| 26 | CmrFiscalDocumentDetailsPEOProcurementBuId | PROCUREMENT_BU_ID | — | ✅ |
| 27 | CmrFiscalDocumentDetailsPEORcvTransactionId | RCV_TRANSACTION_ID | — | ✅ |
| 28 | CmrFiscalDocumentDetailsPEOReceiptLineNum | RECEIPT_LINE_NUM | — | ✅ |
| 29 | CmrFiscalDocumentDetailsPEOReceiptNum | RECEIPT_NUM | — | ✅ |
| 30 | CmrFiscalDocumentDetailsPEOReferenceFdHeaderId | REFERENCE_FD_HEADER_ID | — | ✅ |
| 31 | CmrFiscalDocumentDetailsPEOReferenceFdLineId | REFERENCE_FD_LINE_ID | — | ✅ |
| 32 | CmrFiscalDocumentDetailsPEOReqBuFuncCurrencyCode | REQ_BU_FUNC_CURRENCY_CODE | — | ✅ |
| 33 | CmrFiscalDocumentDetailsPEOReqBuFuncCurrencyRate | REQ_BU_FUNC_CURRENCY_RATE | — | ✅ |
| 34 | CmrFiscalDocumentDetailsPEORequisitionBuId | REQUISITION_BU_ID | — | ✅ |
| 35 | CmrFiscalDocumentDetailsPEOServicePoLineFlag | SERVICE_PO_LINE_FLAG | — | ✅ |
| 36 | CmrFiscalDocumentDetailsPEOShipToOrganizationId | SHIP_TO_ORGANIZATION_ID | — | ✅ |
| 37 | CmrFiscalDocumentDetailsPEOSoldToLegalEntityId | SOLD_TO_LEGAL_ENTITY_ID | — | ✅ |
| 38 | CmrFiscalDocumentDetailsPEOSourceDocumentCurrencyCode | SOURCE_DOCUMENT_CURRENCY_CODE | — | ✅ |
| 39 | CmrFiscalDocumentDetailsPEOSourceDocumentLineId | SOURCE_DOCUMENT_LINE_ID | — | ✅ |
| 40 | CmrFiscalDocumentDetailsPEOSourceDocumentScheduleId | SOURCE_DOCUMENT_SCHEDULE_ID | — | ✅ |
| 41 | CmrFiscalDocumentDetailsPEOSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | ✅ |
| 42 | CmrFiscalDocumentDetailsPEOSourceDocumentUomCode | SOURCE_DOCUMENT_UOM_CODE | — | ✅ |
| 43 | CmrFiscalDocumentDetailsPEOTaxAmount | TAX_AMOUNT | — | ✅ |
| 44 | CmrFiscalDocumentDetailsPEOTaxAmountIncludedFlag | TAX_AMOUNT_INCLUDED_FLAG | — | ✅ |
| 45 | CmrFiscalDocumentDetailsPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 46 | CmrFiscalDocumentDetailsPEOTransactionQty | TRANSACTION_QTY | — | ✅ |
| 47 | CmrFiscalDocumentDetailsPEOTransactionUomCode | TRANSACTION_UOM_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
