---
id: DOC-OTHER-PVO-CmrApInvoiceDtlsExtractPVO
doc_type: system-doc
title: "CmrApInvoiceDtlsExtractPVO — PVO Cross-Module"
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
  - CmrApInvoiceDtlsExtractPVO
  - cmrapinvoicedtlsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrApInvoiceDtlsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cmr Ap Invoice Dtls Extract. Acessa as tabelas: CMR_AP_INVOICE_DTLS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CmrBiccExtractAM.CmrApInvoiceDtlsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 63 | 1 | 3 | 63 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_ap_invoice_dtls|CMR_AP_INVOICE_DTLS]] — 63 atributos (3 PKs, 63 BICC)

---

## ⚙️ Atributos

### [[cmr_ap_invoice_dtls|CMR_AP_INVOICE_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrApInvoiceDtlsPEOAccountingDate | ACCOUNTING_DATE | — | ✅ |
| 2 | CmrApInvoiceDtlsPEOChargeApplicableToDistId | CHARGE_APPLICABLE_TO_DIST_ID | — | ✅ |
| 3 | CmrApInvoiceDtlsPEOCmrApInvoiceDistId | CMR_AP_INVOICE_DIST_ID | 🔑 | ✅ |
| 4 | CmrApInvoiceDtlsPEOCmrApInvoiceLineId | CMR_AP_INVOICE_LINE_ID | — | ✅ |
| 5 | CmrApInvoiceDtlsPEOCmrPoDistributionId | CMR_PO_DISTRIBUTION_ID | — | ✅ |
| 6 | CmrApInvoiceDtlsPEOCmrRcvTransactionId | CMR_RCV_TRANSACTION_ID | — | ✅ |
| 7 | CmrApInvoiceDtlsPEOConsumptionAdviceHeaderId | CONSUMPTION_ADVICE_HEADER_ID | — | ✅ |
| 8 | CmrApInvoiceDtlsPEOConsumptionAdviceLineId | CONSUMPTION_ADVICE_LINE_ID | — | ✅ |
| 9 | CmrApInvoiceDtlsPEOCorrectedInvoiceDistId | CORRECTED_INVOICE_DIST_ID | — | ✅ |
| 10 | CmrApInvoiceDtlsPEOCreatedBy | CREATED_BY | — | ✅ |
| 11 | CmrApInvoiceDtlsPEOCreationDate | CREATION_DATE | — | ✅ |
| 12 | CmrApInvoiceDtlsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 13 | CmrApInvoiceDtlsPEOCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 14 | CmrApInvoiceDtlsPEOCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 15 | CmrApInvoiceDtlsPEOCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 16 | CmrApInvoiceDtlsPEODistCodeCombinationId | DIST_CODE_COMBINATION_ID | — | ✅ |
| 17 | CmrApInvoiceDtlsPEODistributionMatchType | DISTRIBUTION_MATCH_TYPE | — | ✅ |
| 18 | CmrApInvoiceDtlsPEOExpenditureItemDate | EXPENDITURE_ITEM_DATE | — | ✅ |
| 19 | CmrApInvoiceDtlsPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | 🔑 | ✅ |
| 20 | CmrApInvoiceDtlsPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | 🔑 | ✅ |
| 21 | CmrApInvoiceDtlsPEOFinalMatchFlag | FINAL_MATCH_FLAG | — | ✅ |
| 22 | CmrApInvoiceDtlsPEOFiscalChargeType | FISCAL_CHARGE_TYPE | — | ✅ |
| 23 | CmrApInvoiceDtlsPEOFiscalDocHeaderId | FISCAL_DOC_HEADER_ID | — | ✅ |
| 24 | CmrApInvoiceDtlsPEOFiscalDocLineId | FISCAL_DOC_LINE_ID | — | ✅ |
| 25 | CmrApInvoiceDtlsPEOInclusiveFlag | INCLUSIVE_FLAG | — | ✅ |
| 26 | CmrApInvoiceDtlsPEOInvoiceAmt | INVOICE_AMT | — | ✅ |
| 27 | CmrApInvoiceDtlsPEOInvoiceBaseAmount | INVOICE_BASE_AMOUNT | — | ✅ |
| 28 | CmrApInvoiceDtlsPEOInvoiceCreationDate | INVOICE_CREATION_DATE | — | ✅ |
| 29 | CmrApInvoiceDtlsPEOInvoiceDistributionType | INVOICE_DISTRIBUTION_TYPE | — | ✅ |
| 30 | CmrApInvoiceDtlsPEOInvoiceId | INVOICE_ID | — | ✅ |
| 31 | CmrApInvoiceDtlsPEOInvoiceLineNumber | INVOICE_LINE_NUMBER | — | ✅ |
| 32 | CmrApInvoiceDtlsPEOInvoiceLineType | INVOICE_LINE_TYPE | — | ✅ |
| 33 | CmrApInvoiceDtlsPEOInvoiceNumber | INVOICE_NUMBER | — | ✅ |
| 34 | CmrApInvoiceDtlsPEOInvoiceQty | INVOICE_QTY | — | ✅ |
| 35 | CmrApInvoiceDtlsPEOInvoiceQtyInPoUom | INVOICE_QTY_IN_PO_UOM | — | ✅ |
| 36 | CmrApInvoiceDtlsPEOInvoiceQtyInPrimaryUom | INVOICE_QTY_IN_PRIMARY_UOM | — | ✅ |
| 37 | CmrApInvoiceDtlsPEOInvoiceSource | INVOICE_SOURCE | — | ✅ |
| 38 | CmrApInvoiceDtlsPEOInvoiceType | INVOICE_TYPE | — | ✅ |
| 39 | CmrApInvoiceDtlsPEOInvoicingBuFuncCurrCode | INVOICING_BU_FUNC_CURR_CODE | — | ✅ |
| 40 | CmrApInvoiceDtlsPEOInvoicingBusinessUnitId | INVOICING_BUSINESS_UNIT_ID | — | ✅ |
| 41 | CmrApInvoiceDtlsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 42 | CmrApInvoiceDtlsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 43 | CmrApInvoiceDtlsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 44 | CmrApInvoiceDtlsPEOLcmAssociationProcessedFlag | LCM_ASSOCIATION_PROCESSED_FLAG | — | ✅ |
| 45 | CmrApInvoiceDtlsPEOLcmAssociationRequestId | LCM_ASSOCIATION_REQUEST_ID | — | ✅ |
| 46 | CmrApInvoiceDtlsPEOLcmEnabledFlag | LCM_ENABLED_FLAG | — | ✅ |
| 47 | CmrApInvoiceDtlsPEOLeTimezoneCode | LE_TIMEZONE_CODE | — | ✅ |
| 48 | CmrApInvoiceDtlsPEOLineCancelledFlag | LINE_CANCELLED_FLAG | — | ✅ |
| 49 | CmrApInvoiceDtlsPEOOnlineAssocProcessId | ONLINE_ASSOC_PROCESS_ID | — | ✅ |
| 50 | CmrApInvoiceDtlsPEOParentReversalId | PARENT_REVERSAL_ID | — | ✅ |
| 51 | CmrApInvoiceDtlsPEOPoDistributionId | PO_DISTRIBUTION_ID | — | ✅ |
| 52 | CmrApInvoiceDtlsPEOProcessedByCaFlag | PROCESSED_BY_CA_FLAG | — | ✅ |
| 53 | CmrApInvoiceDtlsPEOProcessedByRaFlag | PROCESSED_BY_RA_FLAG | — | ✅ |
| 54 | CmrApInvoiceDtlsPEOProcurementBusinessUnitId | PROCUREMENT_BUSINESS_UNIT_ID | — | ✅ |
| 55 | CmrApInvoiceDtlsPEORcvTransactionId | RCV_TRANSACTION_ID | — | ✅ |
| 56 | CmrApInvoiceDtlsPEORelatedDistributionId | RELATED_DISTRIBUTION_ID | — | ✅ |
| 57 | CmrApInvoiceDtlsPEOReversalFlag | REVERSAL_FLAG | — | ✅ |
| 58 | CmrApInvoiceDtlsPEOSelfAssessedFlag | SELF_ASSESSED_FLAG | — | ✅ |
| 59 | CmrApInvoiceDtlsPEOTaxCodeId | TAX_CODE_ID | — | ✅ |
| 60 | CmrApInvoiceDtlsPEOTaxPointBasis | TAX_POINT_BASIS | — | ✅ |
| 61 | CmrApInvoiceDtlsPEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 62 | CmrApInvoiceDtlsPEOVendorId | VENDOR_ID | — | ✅ |
| 63 | CmrApInvoiceDtlsPEOVendorSiteId | VENDOR_SITE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
