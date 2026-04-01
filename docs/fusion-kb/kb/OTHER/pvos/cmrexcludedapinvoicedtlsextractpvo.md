---
id: DOC-OTHER-PVO-CmrExcludedApInvoiceDtlsExtractPVO
doc_type: system-doc
title: "CmrExcludedApInvoiceDtlsExtractPVO — PVO Cross-Module"
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
  - CmrExcludedApInvoiceDtlsExtractPVO
  - cmrexcludedapinvoicedtlsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrExcludedApInvoiceDtlsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cmr Excluded Ap Invoice Dtls Extract. Acessa as tabelas: CMR_EXCLUDED_AP_INVOICE_DTLS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CmrBiccExtractAM.CmrExcludedApInvoiceDtlsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 59 | 1 | 2 | 59 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_excluded_ap_invoice_dtls|CMR_EXCLUDED_AP_INVOICE_DTLS]] — 59 atributos (2 PKs, 59 BICC)

---

## ⚙️ Atributos

### [[cmr_excluded_ap_invoice_dtls|CMR_EXCLUDED_AP_INVOICE_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrExcludedApInvoiceDtlsPEOAccountingDate | ACCOUNTING_DATE | — | ✅ |
| 2 | CmrExcludedApInvoiceDtlsPEOChargeApplicableToDistId | CHARGE_APPLICABLE_TO_DIST_ID | — | ✅ |
| 3 | CmrExcludedApInvoiceDtlsPEOCmrApInvoiceDistId | CMR_AP_INVOICE_DIST_ID | — | ✅ |
| 4 | CmrExcludedApInvoiceDtlsPEOCmrPoDistributionId | CMR_PO_DISTRIBUTION_ID | — | ✅ |
| 5 | CmrExcludedApInvoiceDtlsPEOCmrRcvTransactionId | CMR_RCV_TRANSACTION_ID | — | ✅ |
| 6 | CmrExcludedApInvoiceDtlsPEOConsumptionAdviceHeaderId | CONSUMPTION_ADVICE_HEADER_ID | — | ✅ |
| 7 | CmrExcludedApInvoiceDtlsPEOConsumptionAdviceLineId | CONSUMPTION_ADVICE_LINE_ID | — | ✅ |
| 8 | CmrExcludedApInvoiceDtlsPEOCorrectedInvoiceDistId | CORRECTED_INVOICE_DIST_ID | — | ✅ |
| 9 | CmrExcludedApInvoiceDtlsPEOCreatedBy | CREATED_BY | — | ✅ |
| 10 | CmrExcludedApInvoiceDtlsPEOCreationDate | CREATION_DATE | — | ✅ |
| 11 | CmrExcludedApInvoiceDtlsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 12 | CmrExcludedApInvoiceDtlsPEOCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 13 | CmrExcludedApInvoiceDtlsPEOCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 14 | CmrExcludedApInvoiceDtlsPEOCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 15 | CmrExcludedApInvoiceDtlsPEODistCodeCombinationId | DIST_CODE_COMBINATION_ID | — | ✅ |
| 16 | CmrExcludedApInvoiceDtlsPEODistributionMatchType | DISTRIBUTION_MATCH_TYPE | — | ✅ |
| 17 | CmrExcludedApInvoiceDtlsPEOExpenditureItemDate | EXPENDITURE_ITEM_DATE | — | ✅ |
| 18 | CmrExcludedApInvoiceDtlsPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | 🔑 | ✅ |
| 19 | CmrExcludedApInvoiceDtlsPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | 🔑 | ✅ |
| 20 | CmrExcludedApInvoiceDtlsPEOFinalMatchFlag | FINAL_MATCH_FLAG | — | ✅ |
| 21 | CmrExcludedApInvoiceDtlsPEOFiscalChargeType | FISCAL_CHARGE_TYPE | — | ✅ |
| 22 | CmrExcludedApInvoiceDtlsPEOFiscalDocHeaderId | FISCAL_DOC_HEADER_ID | — | ✅ |
| 23 | CmrExcludedApInvoiceDtlsPEOFiscalDocLineId | FISCAL_DOC_LINE_ID | — | ✅ |
| 24 | CmrExcludedApInvoiceDtlsPEOInclusiveFlag | INCLUSIVE_FLAG | — | ✅ |
| 25 | CmrExcludedApInvoiceDtlsPEOInvoiceAmt | INVOICE_AMT | — | ✅ |
| 26 | CmrExcludedApInvoiceDtlsPEOInvoiceBaseAmount | INVOICE_BASE_AMOUNT | — | ✅ |
| 27 | CmrExcludedApInvoiceDtlsPEOInvoiceCreationDate | INVOICE_CREATION_DATE | — | ✅ |
| 28 | CmrExcludedApInvoiceDtlsPEOInvoiceDistributionType | INVOICE_DISTRIBUTION_TYPE | — | ✅ |
| 29 | CmrExcludedApInvoiceDtlsPEOInvoiceId | INVOICE_ID | — | ✅ |
| 30 | CmrExcludedApInvoiceDtlsPEOInvoiceLineNumber | INVOICE_LINE_NUMBER | — | ✅ |
| 31 | CmrExcludedApInvoiceDtlsPEOInvoiceLineType | INVOICE_LINE_TYPE | — | ✅ |
| 32 | CmrExcludedApInvoiceDtlsPEOInvoiceNumber | INVOICE_NUMBER | — | ✅ |
| 33 | CmrExcludedApInvoiceDtlsPEOInvoiceQty | INVOICE_QTY | — | ✅ |
| 34 | CmrExcludedApInvoiceDtlsPEOInvoiceQtyInPoUom | INVOICE_QTY_IN_PO_UOM | — | ✅ |
| 35 | CmrExcludedApInvoiceDtlsPEOInvoiceQtyInPrimaryUom | INVOICE_QTY_IN_PRIMARY_UOM | — | ✅ |
| 36 | CmrExcludedApInvoiceDtlsPEOInvoiceSource | INVOICE_SOURCE | — | ✅ |
| 37 | CmrExcludedApInvoiceDtlsPEOInvoiceType | INVOICE_TYPE | — | ✅ |
| 38 | CmrExcludedApInvoiceDtlsPEOInvoicingBuFuncCurrCode | INVOICING_BU_FUNC_CURR_CODE | — | ✅ |
| 39 | CmrExcludedApInvoiceDtlsPEOInvoicingBusinessUnitId | INVOICING_BUSINESS_UNIT_ID | — | ✅ |
| 40 | CmrExcludedApInvoiceDtlsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 41 | CmrExcludedApInvoiceDtlsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 42 | CmrExcludedApInvoiceDtlsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 43 | CmrExcludedApInvoiceDtlsPEOLcmAssociationProcessedFlag | LCM_ASSOCIATION_PROCESSED_FLAG | — | ✅ |
| 44 | CmrExcludedApInvoiceDtlsPEOLcmEnabledFlag | LCM_ENABLED_FLAG | — | ✅ |
| 45 | CmrExcludedApInvoiceDtlsPEOLeTimezoneCode | LE_TIMEZONE_CODE | — | ✅ |
| 46 | CmrExcludedApInvoiceDtlsPEOLineCancelledFlag | LINE_CANCELLED_FLAG | — | ✅ |
| 47 | CmrExcludedApInvoiceDtlsPEOOnlineAssocProcessId | ONLINE_ASSOC_PROCESS_ID | — | ✅ |
| 48 | CmrExcludedApInvoiceDtlsPEOParentReversalId | PARENT_REVERSAL_ID | — | ✅ |
| 49 | CmrExcludedApInvoiceDtlsPEOPoDistributionId | PO_DISTRIBUTION_ID | — | ✅ |
| 50 | CmrExcludedApInvoiceDtlsPEOProcurementBusinessUnitId | PROCUREMENT_BUSINESS_UNIT_ID | — | ✅ |
| 51 | CmrExcludedApInvoiceDtlsPEORcvTransactionId | RCV_TRANSACTION_ID | — | ✅ |
| 52 | CmrExcludedApInvoiceDtlsPEORelatedDistributionId | RELATED_DISTRIBUTION_ID | — | ✅ |
| 53 | CmrExcludedApInvoiceDtlsPEOReversalFlag | REVERSAL_FLAG | — | ✅ |
| 54 | CmrExcludedApInvoiceDtlsPEOSelfAssessedFlag | SELF_ASSESSED_FLAG | — | ✅ |
| 55 | CmrExcludedApInvoiceDtlsPEOTaxCodeId | TAX_CODE_ID | — | ✅ |
| 56 | CmrExcludedApInvoiceDtlsPEOTaxPointBasis | TAX_POINT_BASIS | — | ✅ |
| 57 | CmrExcludedApInvoiceDtlsPEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 58 | CmrExcludedApInvoiceDtlsPEOVendorId | VENDOR_ID | — | ✅ |
| 59 | CmrExcludedApInvoiceDtlsPEOVendorSiteId | VENDOR_SITE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
