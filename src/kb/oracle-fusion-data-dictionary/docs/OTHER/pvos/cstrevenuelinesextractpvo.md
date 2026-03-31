---
id: DOC-OTHER-PVO-CstRevenueLinesExtractPVO
doc_type: system-doc
title: "CstRevenueLinesExtractPVO — PVO Cross-Module"
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
  - CstRevenueLinesExtractPVO
  - cstrevenuelinesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstRevenueLinesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Revenue Lines Extract. Acessa as tabelas: CST_REVENUE_LINES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstRevenueLinesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 51 | 1 | 1 | 51 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_revenue_lines|CST_REVENUE_LINES]] — 51 atributos (1 PKs, 51 BICC)

---

## ⚙️ Atributos

### [[cst_revenue_lines|CST_REVENUE_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RevenueLinesPEOAcctdAmount | ACCTD_AMOUNT | — | ✅ |
| 2 | RevenueLinesPEOAtoTopModelFlineId | ATO_TOP_MODEL_FLINE_ID | — | ✅ |
| 3 | RevenueLinesPEOAtoTopModelItemId | ATO_TOP_MODEL_ITEM_ID | — | ✅ |
| 4 | RevenueLinesPEOBillToCustomerId | BILL_TO_CUSTOMER_ID | — | ✅ |
| 5 | RevenueLinesPEOBillToSiteUseId | BILL_TO_SITE_USE_ID | — | ✅ |
| 6 | RevenueLinesPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 7 | RevenueLinesPEOConfigInventoryItemId | CONFIG_INVENTORY_ITEM_ID | — | ✅ |
| 8 | RevenueLinesPEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | RevenueLinesPEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | RevenueLinesPEOCustomerTrxId | CUSTOMER_TRX_ID | — | ✅ |
| 11 | RevenueLinesPEOCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | ✅ |
| 12 | RevenueLinesPEODeliveryId | DELIVERY_ID | — | ✅ |
| 13 | RevenueLinesPEODocumentType | DOCUMENT_TYPE | — | ✅ |
| 14 | RevenueLinesPEODooFlinePriceAdjustmentId | DOO_FLINE_PRICE_ADJUSTMENT_ID | — | ✅ |
| 15 | RevenueLinesPEODooFulfillLineId | DOO_FULFILL_LINE_ID | — | ✅ |
| 16 | RevenueLinesPEODooOrderNumber | DOO_ORDER_NUMBER | — | ✅ |
| 17 | RevenueLinesPEODooOrderType | DOO_ORDER_TYPE | — | ✅ |
| 18 | RevenueLinesPEODooReferenceFulfillLineId | DOO_REFERENCE_FULFILL_LINE_ID | — | ✅ |
| 19 | RevenueLinesPEOExtendedAmount | EXTENDED_AMOUNT | — | ✅ |
| 20 | RevenueLinesPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | ✅ |
| 21 | RevenueLinesPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | ✅ |
| 22 | RevenueLinesPEOGlDate | GL_DATE | — | ✅ |
| 23 | RevenueLinesPEOGrossMarginFlag | GROSS_MARGIN_FLAG | — | ✅ |
| 24 | RevenueLinesPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 25 | RevenueLinesPEOInventoryOrgId | INVENTORY_ORG_ID | — | ✅ |
| 26 | RevenueLinesPEOInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 27 | RevenueLinesPEOInvoiceDate | INVOICE_DATE | — | ✅ |
| 28 | RevenueLinesPEOInvoiceLineAmount | INVOICE_LINE_AMOUNT | — | ✅ |
| 29 | RevenueLinesPEOInvoiceNumber | INVOICE_NUMBER | — | ✅ |
| 30 | RevenueLinesPEOInvoiceSource | INVOICE_SOURCE | — | ✅ |
| 31 | RevenueLinesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | RevenueLinesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 33 | RevenueLinesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 34 | RevenueLinesPEOLedgerId | LEDGER_ID | — | ✅ |
| 35 | RevenueLinesPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 36 | RevenueLinesPEOLoadRequestId | LOAD_REQUEST_ID | — | ✅ |
| 37 | RevenueLinesPEOParentFulfillLineId | PARENT_FULFILL_LINE_ID | — | ✅ |
| 38 | RevenueLinesPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 39 | RevenueLinesPEOPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | ✅ |
| 40 | RevenueLinesPEOPreviousCustomerTrxLineId | PREVIOUS_CUSTOMER_TRX_LINE_ID | — | ✅ |
| 41 | RevenueLinesPEOQuantityInvoiced | QUANTITY_INVOICED | — | ✅ |
| 42 | RevenueLinesPEOReferenceLineId | REFERENCE_LINE_ID | — | ✅ |
| 43 | RevenueLinesPEORevenueAccount | REVENUE_ACCOUNT | — | ✅ |
| 44 | RevenueLinesPEORevenueAmount | REVENUE_AMOUNT | — | ✅ |
| 45 | RevenueLinesPEORevenueLineId | REVENUE_LINE_ID | 🔑 | ✅ |
| 46 | RevenueLinesPEORevenuePercentage | REVENUE_PERCENTAGE | — | ✅ |
| 47 | RevenueLinesPEORootParentFulfillLineId | ROOT_PARENT_FULFILL_LINE_ID | — | ✅ |
| 48 | RevenueLinesPEOTxnProcessingGroupId | TXN_PROCESSING_GROUP_ID | — | ✅ |
| 49 | RevenueLinesPEOUnitSellingPrice | UNIT_SELLING_PRICE | — | ✅ |
| 50 | RevenueLinesPEOUomCode | UOM_CODE | — | ✅ |
| 51 | RevenueLinesPEOWarehouseId | WAREHOUSE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
