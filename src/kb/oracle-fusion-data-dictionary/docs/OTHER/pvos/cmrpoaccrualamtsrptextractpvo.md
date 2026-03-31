---
id: DOC-OTHER-PVO-CmrPoAccrualAmtsRptExtractPVO
doc_type: system-doc
title: "CmrPoAccrualAmtsRptExtractPVO — PVO Cross-Module"
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
  - CmrPoAccrualAmtsRptExtractPVO
  - cmrpoaccrualamtsrptextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrPoAccrualAmtsRptExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cmr Po Accrual Amts Rpt Extract. Acessa as tabelas: CMR_PO_ACCRUAL_AMTS_RPT.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CmrBiccExtractAM.CmrPoAccrualAmtsRptExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 46 | 1 | 2 | 46 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_po_accrual_amts_rpt|CMR_PO_ACCRUAL_AMTS_RPT]] — 46 atributos (2 PKs, 46 BICC)

---

## ⚙️ Atributos

### [[cmr_po_accrual_amts_rpt|CMR_PO_ACCRUAL_AMTS_RPT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrPoAccrualAmtsRptPEOAccrualAccountId | ACCRUAL_ACCOUNT_ID | — | ✅ |
| 2 | CmrPoAccrualAmtsRptPEOAccrualAmt | ACCRUAL_AMT | — | ✅ |
| 3 | CmrPoAccrualAmtsRptPEOAccrualQty | ACCRUAL_QTY | — | ✅ |
| 4 | CmrPoAccrualAmtsRptPEOBillToBuId | BILL_TO_BU_ID | — | ✅ |
| 5 | CmrPoAccrualAmtsRptPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 6 | CmrPoAccrualAmtsRptPEOCategoryId | CATEGORY_ID | — | ✅ |
| 7 | CmrPoAccrualAmtsRptPEOChargeAccountId | CHARGE_ACCOUNT_ID | — | ✅ |
| 8 | CmrPoAccrualAmtsRptPEOCmrPoDistributionId | CMR_PO_DISTRIBUTION_ID | 🔑 | ✅ |
| 9 | CmrPoAccrualAmtsRptPEOCreatedBy | CREATED_BY | — | ✅ |
| 10 | CmrPoAccrualAmtsRptPEOCreationDate | CREATION_DATE | — | ✅ |
| 11 | CmrPoAccrualAmtsRptPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 12 | CmrPoAccrualAmtsRptPEOCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 13 | CmrPoAccrualAmtsRptPEOCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 14 | CmrPoAccrualAmtsRptPEOCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 15 | CmrPoAccrualAmtsRptPEODistributionNumber | DISTRIBUTION_NUMBER | — | ✅ |
| 16 | CmrPoAccrualAmtsRptPEOFuncCurrencyCode | FUNC_CURRENCY_CODE | — | ✅ |
| 17 | CmrPoAccrualAmtsRptPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 18 | CmrPoAccrualAmtsRptPEOInventoryOrgId | INVENTORY_ORG_ID | — | ✅ |
| 19 | CmrPoAccrualAmtsRptPEOInvoiceAmtFuncCurr | INVOICE_AMT_FUNC_CURR | — | ✅ |
| 20 | CmrPoAccrualAmtsRptPEOInvoiceVarianceAmt | INVOICE_VARIANCE_AMT | — | ✅ |
| 21 | CmrPoAccrualAmtsRptPEOInvoicedAmt | INVOICED_AMT | — | ✅ |
| 22 | CmrPoAccrualAmtsRptPEOInvoicedQty | INVOICED_QTY | — | ✅ |
| 23 | CmrPoAccrualAmtsRptPEOItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 24 | CmrPoAccrualAmtsRptPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 25 | CmrPoAccrualAmtsRptPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 26 | CmrPoAccrualAmtsRptPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 27 | CmrPoAccrualAmtsRptPEOLineNumber | LINE_NUMBER | — | ✅ |
| 28 | CmrPoAccrualAmtsRptPEOLineType | LINE_TYPE | — | ✅ |
| 29 | CmrPoAccrualAmtsRptPEOPeriodEndDate | PERIOD_END_DATE | — | ✅ |
| 30 | CmrPoAccrualAmtsRptPEOPeriodName | PERIOD_NAME | — | ✅ |
| 31 | CmrPoAccrualAmtsRptPEOPeriodStartDate | PERIOD_START_DATE | 🔑 | ✅ |
| 32 | CmrPoAccrualAmtsRptPEOPoAmount | PO_AMOUNT | — | ✅ |
| 33 | CmrPoAccrualAmtsRptPEOPoHeaderId | PO_HEADER_ID | — | ✅ |
| 34 | CmrPoAccrualAmtsRptPEOPoLineDistributionId | PO_LINE_DISTRIBUTION_ID | — | ✅ |
| 35 | CmrPoAccrualAmtsRptPEOPoLineId | PO_LINE_ID | — | ✅ |
| 36 | CmrPoAccrualAmtsRptPEOPoLineLocationId | PO_LINE_LOCATION_ID | — | ✅ |
| 37 | CmrPoAccrualAmtsRptPEOPoNumber | PO_NUMBER | — | ✅ |
| 38 | CmrPoAccrualAmtsRptPEOPoPrice | PO_PRICE | — | ✅ |
| 39 | CmrPoAccrualAmtsRptPEOPoQuantity | PO_QUANTITY | — | ✅ |
| 40 | CmrPoAccrualAmtsRptPEOPrimaryLedgerId | PRIMARY_LEDGER_ID | — | ✅ |
| 41 | CmrPoAccrualAmtsRptPEOReceivedAmt | RECEIVED_AMT | — | ✅ |
| 42 | CmrPoAccrualAmtsRptPEOReceivedQty | RECEIVED_QTY | — | ✅ |
| 43 | CmrPoAccrualAmtsRptPEOShipmentNumber | SHIPMENT_NUMBER | — | ✅ |
| 44 | CmrPoAccrualAmtsRptPEOUomCode | UOM_CODE | — | ✅ |
| 45 | CmrPoAccrualAmtsRptPEOVendorId | VENDOR_ID | — | ✅ |
| 46 | CmrPoAccrualAmtsRptPEOVendorSiteId | VENDOR_SITE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
