---
id: DOC-AP-PVO-PrepaymentAppliationDistributionPVO
doc_type: system-doc
title: "PrepaymentAppliationDistributionPVO — PVO Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ap
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PrepaymentAppliationDistributionPVO
  - prepaymentappliationdistributionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PrepaymentAppliationDistributionPVO

## 📌 Visão Geral

Extrai as distribuições contábeis de aplicações de adiantamentos (prepayments) em faturas de fornecedores, incluindo valores aplicados, conta contábil, impostos e referências a pedidos de compra. Essencial para controle de adiantamentos, reconciliação contábil e conformidade fiscal.

**Caminho:** `FscmTopModelAM.FinApInvTransactionsAM.PrepaymentAppliationDistributionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 192 | 30 | 1 | 97 | 51% |

---

## 🔗 Tabelas Relacionadas

- [[ap_batches_all|AP_BATCHES_ALL]] — 4 atributos (2 BICC)
- [[ap_distribution_sets_all|AP_DISTRIBUTION_SETS_ALL]] — 4 atributos (2 BICC)
- [[ap_invoices_all|AP_INVOICES_ALL]] — 8 atributos (3 BICC)
- [[ap_invoice_distributions_all|AP_INVOICE_DISTRIBUTIONS_ALL]] — 24 atributos (13 BICC)
- [[ap_invoice_lines_all|AP_INVOICE_LINES_ALL]] — 10 atributos (8 BICC)
- [[ap_invoice_payments_all|AP_INVOICE_PAYMENTS_ALL]] — 2 atributos (1 BICC)
- [[ap_prepay_app_dists|AP_PREPAY_APP_DISTS]] — 43 atributos (1 PKs, 29 BICC)
- [[ap_recon_difference_details|AP_RECON_DIFFERENCE_DETAILS]] — 8 atributos
- [[fa_book_controls|FA_BOOK_CONTROLS]] — 4 atributos (2 BICC)
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 8 atributos (4 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 2 atributos
- [[hz_locations|HZ_LOCATIONS]] — 8 atributos
- [[hz_parties|HZ_PARTIES]] — 3 atributos (2 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 2 atributos (1 BICC)
- [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]] — 2 atributos (1 BICC)
- [[iby_payment_codes_vl|IBY_PAYMENT_CODES_VL]] — 6 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 11 atributos (5 BICC)
- [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]] — 3 atributos (1 BICC)
- [[po_distributions_all|PO_DISTRIBUTIONS_ALL]] — 4 atributos (2 BICC)
- [[po_headers_all|PO_HEADERS_ALL]] — 5 atributos (3 BICC)
- [[po_lines_all|PO_LINES_ALL]] — 2 atributos (1 BICC)
- [[po_line_locations_all|PO_LINE_LOCATIONS_ALL]] — 2 atributos (1 BICC)
- [[rcv_shipment_headers|RCV_SHIPMENT_HEADERS]] — 6 atributos (4 BICC)
- [[rcv_shipment_lines|RCV_SHIPMENT_LINES]] — 3 atributos (2 BICC)
- [[rcv_transactions|RCV_TRANSACTIONS]] — 4 atributos (2 BICC)
- [[zx_jurisdictions_b|ZX_JURISDICTIONS_B]] — 3 atributos (1 BICC)
- [[zx_lines_summary|ZX_LINES_SUMMARY]] — 4 atributos (2 BICC)
- [[zx_rates_vl|ZX_RATES_VL]] — 2 atributos (1 BICC)
- [[zx_rec_nrec_dist|ZX_REC_NREC_DIST]] — 2 atributos (1 BICC)
- [[zx_regimes_b|ZX_REGIMES_B]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[ap_batches_all|AP_BATCHES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceBatchBatchId | BATCH_ID | — | — |
| 2 | InvoiceBatchDistBatchId | BATCH_ID | — | — |
| 3 | InvoiceBatchDistLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | InvoiceBatchLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[ap_distribution_sets_all|AP_DISTRIBUTION_SETS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistributionSetDistributionSetId | DISTRIBUTION_SET_ID | — | — |
| 2 | DistributionSetLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | DistributionSetLineDistributionSetId | DISTRIBUTION_SET_ID | — | — |
| 4 | DistributionSetLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[ap_invoices_all|AP_INVOICES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceHeaderAcctsPayCodeCombinationId | ACCTS_PAY_CODE_COMBINATION_ID | — | — |
| 2 | InvoiceHeaderInvoiceDate | INVOICE_DATE | — | — |
| 3 | InvoiceHeaderInvoiceId | INVOICE_ID | — | — |
| 4 | InvoiceHeaderInvoiceNum | INVOICE_NUM | — | ✅ |
| 5 | InvoiceHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | InvoiceHeaderPrtInvInvoiceDate | INVOICE_DATE | — | ✅ |
| 7 | InvoiceHeaderPrtInvInvoiceId | INVOICE_ID | — | — |
| 8 | InvoiceHeaderSetOfBooksId | SET_OF_BOOKS_ID | — | — |

### [[ap_invoice_distributions_all|AP_INVOICE_DISTRIBUTIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwtRelDistInvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | — |
| 2 | AwtRelDistLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | InvParenRevIdInvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | — |
| 4 | InvParenRevIdLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | InvoiceDistributionAccountingDate | ACCOUNTING_DATE | — | ✅ |
| 6 | InvoiceDistributionDistCodeCombinationId | DIST_CODE_COMBINATION_ID | — | — |
| 7 | InvoiceDistributionDistributionLineNumber | DISTRIBUTION_LINE_NUMBER | — | ✅ |
| 8 | InvoiceDistributionInvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | ✅ |
| 9 | InvoiceDistributionInvoiceId | INVOICE_ID | — | — |
| 10 | InvoiceDistributionInvoiceLineNumber | INVOICE_LINE_NUMBER | — | — |
| 11 | InvoiceDistributionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | InvoiceDistributionPostedFlag | POSTED_FLAG | — | ✅ |
| 13 | InvoiceDistributionPrepayDistAccountingDate | ACCOUNTING_DATE | — | ✅ |
| 14 | InvoiceDistributionPrepayDistDistributionLineNumber | DISTRIBUTION_LINE_NUMBER | — | ✅ |
| 15 | InvoiceDistributionPrepayDistInvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | — |
| 16 | InvoiceDistributionPrepayDistInvoiceLineNumber | INVOICE_LINE_NUMBER | — | ✅ |
| 17 | InvoiceDistributionPrepayDistPostedFlag | POSTED_FLAG | — | ✅ |
| 18 | InvoiceDistributionPrepayDistributionId | PREPAY_DISTRIBUTION_ID | — | — |
| 19 | InvoiceDistributionPrepaymentInvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | — |
| 20 | InvoiceDistributionPrepaymentInvoiceId | INVOICE_ID | — | — |
| 21 | PrepayAwtRelDistDistributionLineNumber | DISTRIBUTION_LINE_NUMBER | — | ✅ |
| 22 | PrepayAwtRelDistInvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | — |
| 23 | RelDistInvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | — |
| 24 | RelDistLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[ap_invoice_lines_all|AP_INVOICE_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceLineAmount | AMOUNT | — | ✅ |
| 2 | InvoiceLineBaseAmount | BASE_AMOUNT | — | ✅ |
| 3 | InvoiceLineIncludedTaxAmount | INCLUDED_TAX_AMOUNT | — | ✅ |
| 4 | InvoiceLineInvoiceId | INVOICE_ID | — | — |
| 5 | InvoiceLineInvoiceIncludesPrepayFlag | INVOICE_INCLUDES_PREPAY_FLAG | — | ✅ |
| 6 | InvoiceLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | InvoiceLineLineNumber | LINE_NUMBER | — | ✅ |
| 8 | InvoiceLineLineTypeLookupCode | LINE_TYPE_LOOKUP_CODE | — | ✅ |
| 9 | InvoiceLinePrepayInvoiceId | PREPAY_INVOICE_ID | — | — |
| 10 | InvoiceLinePrepayLineNumber | PREPAY_LINE_NUMBER | — | ✅ |

### [[ap_invoice_payments_all|AP_INVOICE_PAYMENTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaidDisbursementScheduleInvoicePaymentId | INVOICE_PAYMENT_ID | — | — |
| 2 | PaidDisbursementScheduleLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[ap_prepay_app_dists|AP_PREPAY_APP_DISTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrepayAppDistId | PREPAY_APP_DIST_ID | 🔑 | ✅ |
| 2 | PrepaymentApplicationAccountingEventId | ACCOUNTING_EVENT_ID | — | — |
| 3 | PrepaymentApplicationAmount | AMOUNT | — | ✅ |
| 4 | PrepaymentApplicationAmountVariance | AMOUNT_VARIANCE | — | ✅ |
| 5 | PrepaymentApplicationAwtRelatedId | AWT_RELATED_ID | — | — |
| 6 | PrepaymentApplicationBaseAmount | BASE_AMOUNT | — | ✅ |
| 7 | PrepaymentApplicationBaseAmtAtPrepayClrXrate | BASE_AMT_AT_PREPAY_CLR_XRATE | — | ✅ |
| 8 | PrepaymentApplicationBaseAmtAtPrepayPayXrate | BASE_AMT_AT_PREPAY_PAY_XRATE | — | ✅ |
| 9 | PrepaymentApplicationBaseAmtAtPrepayXrate | BASE_AMT_AT_PREPAY_XRATE | — | ✅ |
| 10 | PrepaymentApplicationBcEventId | BC_EVENT_ID | — | — |
| 11 | PrepaymentApplicationCreatedBy | CREATED_BY | — | ✅ |
| 12 | PrepaymentApplicationCreationDate | CREATION_DATE | — | ✅ |
| 13 | PrepaymentApplicationInvoiceBaseAmtVariance | INVOICE_BASE_AMT_VARIANCE | — | ✅ |
| 14 | PrepaymentApplicationInvoiceBaseQtyVariance | INVOICE_BASE_QTY_VARIANCE | — | — |
| 15 | PrepaymentApplicationInvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | ✅ |
| 16 | PrepaymentApplicationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | PrepaymentApplicationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | PrepaymentApplicationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | PrepaymentApplicationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | PrepaymentApplicationPaAdditionFlag | PA_ADDITION_FLAG | — | ✅ |
| 21 | PrepaymentApplicationPrepayAppDistributionId | PREPAY_APP_DISTRIBUTION_ID | — | ✅ |
| 22 | PrepaymentApplicationPrepayClrExchangeDate | PREPAY_CLR_EXCHANGE_DATE | — | ✅ |
| 23 | PrepaymentApplicationPrepayClrExchangeRate | PREPAY_CLR_EXCHANGE_RATE | — | ✅ |
| 24 | PrepaymentApplicationPrepayClrExchangeRateType | PREPAY_CLR_EXCHANGE_RATE_TYPE | — | ✅ |
| 25 | PrepaymentApplicationPrepayDistLookupCode | PREPAY_DIST_LOOKUP_CODE | — | ✅ |
| 26 | PrepaymentApplicationPrepayExchangeDate | PREPAY_EXCHANGE_DATE | — | ✅ |
| 27 | PrepaymentApplicationPrepayExchangeRate | PREPAY_EXCHANGE_RATE | — | ✅ |
| 28 | PrepaymentApplicationPrepayExchangeRateType | PREPAY_EXCHANGE_RATE_TYPE | — | ✅ |
| 29 | PrepaymentApplicationPrepayHistoryId | PREPAY_HISTORY_ID | — | — |
| 30 | PrepaymentApplicationPrepayPayExchangeDate | PREPAY_PAY_EXCHANGE_DATE | — | ✅ |
| 31 | PrepaymentApplicationPrepayPayExchangeRate | PREPAY_PAY_EXCHANGE_RATE | — | ✅ |
| 32 | PrepaymentApplicationPrepayPayExchangeRateType | PREPAY_PAY_EXCHANGE_RATE_TYPE | — | ✅ |
| 33 | PrepaymentApplicationProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 34 | PrepaymentApplicationProgramId | PROGRAM_ID | — | — |
| 35 | PrepaymentApplicationProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 36 | PrepaymentApplicationQuantityVariance | QUANTITY_VARIANCE | — | — |
| 37 | PrepaymentApplicationReleaseInvDistDerivedFrom | RELEASE_INV_DIST_DERIVED_FROM | — | — |
| 38 | PrepaymentApplicationRequestId | REQUEST_ID | — | — |
| 39 | PrepaymentApplicationReversedPrepayAppDistId | REVERSED_PREPAY_APP_DIST_ID | — | — |
| 40 | PrepaymentApplicationRoundAmtAtPrepayClrXrate | ROUND_AMT_AT_PREPAY_CLR_XRATE | — | ✅ |
| 41 | PrepaymentApplicationRoundAmtAtPrepayPayXrate | ROUND_AMT_AT_PREPAY_PAY_XRATE | — | ✅ |
| 42 | PrepaymentApplicationRoundAmtAtPrepayXrate | ROUND_AMT_AT_PREPAY_XRATE | — | ✅ |
| 43 | PrepaymentApplicationRoundingAmt | ROUNDING_AMT | — | ✅ |

### [[ap_recon_difference_details|AP_RECON_DIFFERENCE_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReconDiffAccountingDate | ACCOUNTING_DATE | — | — |
| 2 | ReconDiffCauseOfDifferenceCode | CAUSE_OF_DIFFERENCE_CODE | — | — |
| 3 | ReconDiffDocumentDistributionId | DOCUMENT_DISTRIBUTION_ID | — | — |
| 4 | ReconDiffDocumentId | DOCUMENT_ID | — | — |
| 5 | ReconDiffLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 6 | ReconDiffReconItemCode | RECON_ITEM_CODE | — | — |
| 7 | ReconDiffReconTrxId | RECON_TRX_ID | — | — |
| 8 | ReconDiffRequestId | REQUEST_ID | — | — |

### [[fa_book_controls|FA_BOOK_CONTROLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BookControlInvDistBookTypeCode | BOOK_TYPE_CODE | — | — |
| 2 | BookControlInvDistLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | BookControlInvLineBookTypeCode | BOOK_TYPE_CODE | — | — |
| 4 | BookControlInvLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistconversionTypeConversionType | CONVERSION_TYPE | — | — |
| 2 | DistconversionTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | PrepayClrExchangeRateTypeConversionType | CONVERSION_TYPE | — | — |
| 4 | PrepayClrExchangeRateTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PrepayExchangeRateTypeConversionType | CONVERSION_TYPE | — | — |
| 6 | PrepayExchangeRateTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PrepayPayExchangeRateTypeConversionType | CONVERSION_TYPE | — | — |
| 8 | PrepayPayExchangeRateTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgerInvDistChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 2 | LedgerInvDistLedgerId | LEDGER_ID | — | — |

### [[hz_locations|HZ_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FinalDischargeLocationAddress1 | ADDRESS1 | — | — |
| 2 | FinalDischargeLocationAddress2 | ADDRESS2 | — | — |
| 3 | FinalDischargeLocationAddress3 | ADDRESS3 | — | — |
| 4 | FinalDischargeLocationAddress4 | ADDRESS4 | — | — |
| 5 | FinalDischargeLocationCity | CITY | — | — |
| 6 | FinalDischargeLocationLocationId1 | LOCATION_ID | — | — |
| 7 | FinalDischargeLocationPostalCode | POSTAL_CODE | — | — |
| 8 | FinalDischargeLocationState | STATE | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | PartyPartyId | PARTY_ID | — | — |
| 3 | PartyPartyName | PARTY_NAME | — | ✅ |

### [[hz_party_sites|HZ_PARTY_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartySiteLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | PartySitePartySiteId | PARTY_SITE_ID | — | — |

### [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvExtBnkAcctExtBankAccountId | EXT_BANK_ACCOUNT_ID | — | — |
| 2 | InvExtBnkAcctLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[iby_payment_codes_vl|IBY_PAYMENT_CODES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayDelcodeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | PayDelcodePaymentCode | PAYMENT_CODE | — | — |
| 3 | PayDelcodePaymentCodeType | PAYMENT_CODE_TYPE | — | — |
| 4 | PayReacodeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PayReacodePaymentCode | PAYMENT_CODE | — | — |
| 6 | PayReacodePaymentCodeType | PAYMENT_CODE_TYPE | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 5 | PersonNameEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | PersonNameEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | PersonNamePersonNameId | PERSON_NAME_ID | — | — |
| 8 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 9 | PersonUpdatedByEffectiveEndDate2 | EFFECTIVE_END_DATE | — | — |
| 10 | PersonUpdatedByEffectiveStartDate2 | EFFECTIVE_START_DATE | — | ✅ |
| 11 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ShipFromLocationEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 2 | ShipFromLocationLastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 3 | ShipFromLocationVendorSiteId | VENDOR_SITE_ID | — | — |

### [[po_distributions_all|PO_DISTRIBUTIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PoDistributionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | PoDistributionPoDistributionId | PO_DISTRIBUTION_ID | — | — |
| 3 | PurchaseOrderDistLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | PurchaseOrderDistPoDistributionId | PO_DISTRIBUTION_ID | — | — |

### [[po_headers_all|PO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PoHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | PoHeaderPoHeaderId | PO_HEADER_ID | — | — |
| 3 | PurchaseOrderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | PurchaseOrderPoHeaderId | PO_HEADER_ID | — | — |
| 5 | PurchaseOrderSegment1 | SEGMENT1 | — | ✅ |

### [[po_lines_all|PO_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PoLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | PoLinePoLineId | PO_LINE_ID | — | — |

### [[po_line_locations_all|PO_LINE_LOCATIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PoLineLocLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | PoLineLocLineLocationId | LINE_LOCATION_ID | — | — |

### [[rcv_shipment_headers|RCV_SHIPMENT_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RcvShipHeaderInvDistLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | RcvShipHeaderInvDistRaDocLastUpdateDate | RA_DOC_LAST_UPDATE_DATE | — | ✅ |
| 3 | RcvShipHeaderInvDistShipmentHeaderId | SHIPMENT_HEADER_ID | — | — |
| 4 | RcvShipHeaderInvLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | RcvShipHeaderInvLineRaDocLastUpdateDate | RA_DOC_LAST_UPDATE_DATE | — | ✅ |
| 6 | RcvShipHeaderInvLineShipmentHeaderId | SHIPMENT_HEADER_ID | — | — |

### [[rcv_shipment_lines|RCV_SHIPMENT_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RcvShipLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | RcvShipLineRaDocLineLastUpdateDate | RA_DOC_LINE_LAST_UPDATE_DATE | — | ✅ |
| 3 | RcvShipLineShipmentLineId | SHIPMENT_LINE_ID | — | — |

### [[rcv_transactions|RCV_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RcvTransInvDistLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | RcvTransInvDistTransactionId | TRANSACTION_ID | — | — |
| 3 | RcvTransInvLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | RcvTransInvLineTransactionId | TRANSACTION_ID | — | — |

### [[zx_jurisdictions_b|ZX_JURISDICTIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxJurisLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | TaxJurisTaxJurisdictionCode | TAX_JURISDICTION_CODE | — | — |
| 3 | TaxJurisTaxJurisdictionId | TAX_JURISDICTION_ID | — | — |

### [[zx_lines_summary|ZX_LINES_SUMMARY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistSumTaxLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | DistSumTaxLineSummaryTaxLineId | SUMMARY_TAX_LINE_ID | — | — |
| 3 | SumTaxLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | SumTaxLineSummaryTaxLineId | SUMMARY_TAX_LINE_ID | — | — |

### [[zx_rates_vl|ZX_RATES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxRateLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | TaxRateTaxRateId | TAX_RATE_ID | — | — |

### [[zx_rec_nrec_dist|ZX_REC_NREC_DIST]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DetailTaxDistLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | DetailTaxDistRecNrecTaxDistId | REC_NREC_TAX_DIST_ID | — | — |

### [[zx_regimes_b|ZX_REGIMES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxRegimeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | TaxRegimeTaxRegimeCode | TAX_REGIME_CODE | — | — |
| 3 | TaxRegimeTaxRegimeId | TAX_REGIME_ID | — | — |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
