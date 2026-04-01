---
id: DOC-AP-PVO-PaymentHistoryDistributionPVO
doc_type: system-doc
title: "PaymentHistoryDistributionPVO — PVO Accounts Payable"
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
  - PaymentHistoryDistributionPVO
  - paymenthistorydistributionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PaymentHistoryDistributionPVO

## 📌 Visão Geral

Extrai o histórico detalhado de distribuições contábeis dos pagamentos, incluindo eventos contábeis, banco, método de pagamento, descontos e reconciliação. Permite rastreabilidade contábil completa do ciclo de desembolso, desde a fatura até a compensação bancária.

**Caminho:** `FscmTopModelAM.FinApPmtSinglePaymentsAM.PaymentHistoryDistributionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 322 | 34 | 1 | 210 | 65% |

---

## 🔗 Tabelas Relacionadas

- [[ap_batches_all|AP_BATCHES_ALL]] — 3 atributos (2 BICC)
- [[ap_checks_all|AP_CHECKS_ALL]] — 47 atributos (45 BICC)
- [[ap_discount_offers_tl|AP_DISCOUNT_OFFERS_TL]] — 3 atributos (1 BICC)
- [[ap_distribution_sets_all|AP_DISTRIBUTION_SETS_ALL]] — 2 atributos (1 BICC)
- [[ap_invoices_all|AP_INVOICES_ALL]] — 38 atributos (35 BICC)
- [[ap_invoice_distributions_all|AP_INVOICE_DISTRIBUTIONS_ALL]] — 10 atributos (7 BICC)
- [[ap_invoice_payments_all|AP_INVOICE_PAYMENTS_ALL]] — 37 atributos (29 BICC)
- [[ap_inv_selection_criteria_all|AP_INV_SELECTION_CRITERIA_ALL]] — 2 atributos (1 BICC)
- [[ap_payment_history_all|AP_PAYMENT_HISTORY_ALL]] — 6 atributos (3 BICC)
- [[ap_payment_hist_dists|AP_PAYMENT_HIST_DISTS]] — 36 atributos (1 PKs, 16 BICC)
- [[ap_payment_schedules_all|AP_PAYMENT_SCHEDULES_ALL]] — 8 atributos (6 BICC)
- [[ap_recon_difference_details|AP_RECON_DIFFERENCE_DETAILS]] — 8 atributos
- [[ap_system_parameters_all|AP_SYSTEM_PARAMETERS_ALL]] — 4 atributos (2 BICC)
- [[ap_terms_tl|AP_TERMS_TL]] — 3 atributos (1 BICC)
- [[ce_all_bank_branches_v|CE_ALL_BANK_BRANCHES_V]] — 5 atributos (3 BICC)
- [[ce_bank_acct_uses_all|CE_BANK_ACCT_USES_ALL]] — 3 atributos (2 BICC)
- [[ce_internal_bank_accts_v|CE_INTERNAL_BANK_ACCTS_V]] — 2 atributos (1 BICC)
- [[ce_payment_documents|CE_PAYMENT_DOCUMENTS]] — 3 atributos (2 BICC)
- [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]] — 2 atributos (1 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 4 atributos (2 BICC)
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 17 atributos (9 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 3 atributos (1 BICC)
- [[hz_parties|HZ_PARTIES]] — 9 atributos (6 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 9 atributos (6 BICC)
- [[iby_acct_pmt_profiles_tl|IBY_ACCT_PMT_PROFILES_TL]] — 3 atributos (1 BICC)
- [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]] — 17 atributos (9 BICC)
- [[iby_payments_all|IBY_PAYMENTS_ALL]] — 2 atributos (1 BICC)
- [[iby_payment_codes_vl|IBY_PAYMENT_CODES_VL]] — 6 atributos (2 BICC)
- [[iby_payment_methods_tl|IBY_PAYMENT_METHODS_TL]] — 3 atributos (2 BICC)
- [[iby_pay_instructions_all|IBY_PAY_INSTRUCTIONS_ALL]] — 2 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 14 atributos (6 BICC)
- [[po_headers_all|PO_HEADERS_ALL]] — 5 atributos (3 BICC)
- [[xla_events|XLA_EVENTS]] — 4 atributos (2 BICC)
- [[zx_wht_tax_classification_v|ZX_WHT_TAX_CLASSIFICATION_V]] — 2 atributos (1 BICC)

---

## ⚙️ Atributos

### [[ap_batches_all|AP_BATCHES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceBatchBatchId | BATCH_ID | — | — |
| 2 | InvoiceBatchBatchName | BATCH_NAME | — | ✅ |
| 3 | InvoiceBatchLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[ap_checks_all|AP_CHECKS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChecksAddressLine1 | ADDRESS_LINE1 | — | ✅ |
| 2 | ChecksAddressLine2 | ADDRESS_LINE2 | — | ✅ |
| 3 | ChecksAddressLine3 | ADDRESS_LINE3 | — | ✅ |
| 4 | ChecksAddressLine4 | ADDRESS_LINE4 | — | ✅ |
| 5 | ChecksBankAccountType | BANK_ACCOUNT_TYPE | — | ✅ |
| 6 | ChecksBankChargeBearer | BANK_CHARGE_BEARER | — | ✅ |
| 7 | ChecksBankNum | BANK_NUM | — | ✅ |
| 8 | ChecksCheckDate | CHECK_DATE | — | ✅ |
| 9 | ChecksCheckId | CHECK_ID | — | ✅ |
| 10 | ChecksCheckNumber | CHECK_NUMBER | — | ✅ |
| 11 | ChecksCheckVoucherNum | CHECK_VOUCHER_NUM | — | ✅ |
| 12 | ChecksCheckrunName | CHECKRUN_NAME | — | ✅ |
| 13 | ChecksCity | CITY | — | ✅ |
| 14 | ChecksClearedDate | CLEARED_DATE | — | ✅ |
| 15 | ChecksCountry | COUNTRY | — | ✅ |
| 16 | ChecksCounty | COUNTY | — | ✅ |
| 17 | ChecksCreatedBy | CREATED_BY | — | ✅ |
| 18 | ChecksCreationDate | CREATION_DATE | — | ✅ |
| 19 | ChecksCurrencyCode | CURRENCY_CODE | — | ✅ |
| 20 | ChecksDescription | DESCRIPTION | — | ✅ |
| 21 | ChecksDocSequenceValue | DOC_SEQUENCE_VALUE | — | ✅ |
| 22 | ChecksExchangeDate | EXCHANGE_DATE | — | ✅ |
| 23 | ChecksExchangeRate | EXCHANGE_RATE | — | ✅ |
| 24 | ChecksFuturePayDueDate | FUTURE_PAY_DUE_DATE | — | ✅ |
| 25 | ChecksLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | ChecksLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 27 | ChecksLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 28 | ChecksMaturityExchangeDate | MATURITY_EXCHANGE_DATE | — | ✅ |
| 29 | ChecksMaturityExchangeRate | MATURITY_EXCHANGE_RATE | — | ✅ |
| 30 | ChecksMaturityExchangeRateType | MATURITY_EXCHANGE_RATE_TYPE | — | ✅ |
| 31 | ChecksPaymentMethodCode | PAYMENT_METHOD_CODE | — | ✅ |
| 32 | ChecksPaymentMethodLookupCode | PAYMENT_METHOD_LOOKUP_CODE | — | — |
| 33 | ChecksPaymentTypeFlag | PAYMENT_TYPE_FLAG | — | ✅ |
| 34 | ChecksProvince | PROVINCE | — | ✅ |
| 35 | ChecksReconFlag | RECON_FLAG | — | ✅ |
| 36 | ChecksReleasedDate | RELEASED_DATE | — | ✅ |
| 37 | ChecksRemitToAddressName | REMIT_TO_ADDRESS_NAME | — | ✅ |
| 38 | ChecksRemitToSupplierName | REMIT_TO_SUPPLIER_NAME | — | ✅ |
| 39 | ChecksSettlementPriority | SETTLEMENT_PRIORITY | — | ✅ |
| 40 | ChecksState | STATE | — | ✅ |
| 41 | ChecksStatusLookupCode | STATUS_LOOKUP_CODE | — | ✅ |
| 42 | ChecksStoppedDate | STOPPED_DATE | — | ✅ |
| 43 | ChecksVendorName | VENDOR_NAME | — | ✅ |
| 44 | ChecksVendorSiteCode | VENDOR_SITE_CODE | — | ✅ |
| 45 | ChecksVoidDate | VOID_DATE | — | ✅ |
| 46 | ChecksXCurrRateType | X_CURR_RATE_TYPE | — | ✅ |
| 47 | ChecksZip | ZIP | — | ✅ |

### [[ap_discount_offers_tl|AP_DISCOUNT_OFFERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DiscOfferTransDiscountOfferId | DISCOUNT_OFFER_ID | — | — |
| 2 | DiscOfferTransLanguage | LANGUAGE | — | — |
| 3 | DiscountOffersTranslationName | NAME | — | ✅ |

### [[ap_distribution_sets_all|AP_DISTRIBUTION_SETS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistributionSetDistributionSetId | DISTRIBUTION_SET_ID | — | — |
| 2 | DistributionSetLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[ap_invoices_all|AP_INVOICES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceHeaderAcctsPayCodeCombinationId | ACCTS_PAY_CODE_COMBINATION_ID | — | ✅ |
| 2 | InvoiceHeaderAmountPaid | AMOUNT_PAID | — | ✅ |
| 3 | InvoiceHeaderBaseAmount | BASE_AMOUNT | — | ✅ |
| 4 | InvoiceHeaderCancelledDate | CANCELLED_DATE | — | ✅ |
| 5 | InvoiceHeaderCreationDate | CREATION_DATE | — | ✅ |
| 6 | InvoiceHeaderDescription | DESCRIPTION | — | ✅ |
| 7 | InvoiceHeaderExchangeDate | EXCHANGE_DATE | — | ✅ |
| 8 | InvoiceHeaderExchangeRate | EXCHANGE_RATE | — | ✅ |
| 9 | InvoiceHeaderExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 10 | InvoiceHeaderInvoiceAmount | INVOICE_AMOUNT | — | ✅ |
| 11 | InvoiceHeaderInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 12 | InvoiceHeaderInvoiceDate | INVOICE_DATE | — | ✅ |
| 13 | InvoiceHeaderInvoiceId | INVOICE_ID | — | — |
| 14 | InvoiceHeaderInvoiceNum | INVOICE_NUM | — | ✅ |
| 15 | InvoiceHeaderInvoiceReceivedDate | INVOICE_RECEIVED_DATE | — | ✅ |
| 16 | InvoiceHeaderInvoiceTypeLookupCode | INVOICE_TYPE_LOOKUP_CODE | — | ✅ |
| 17 | InvoiceHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | InvoiceHeaderLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 19 | InvoiceHeaderOrgId | ORG_ID | — | ✅ |
| 20 | InvoiceHeaderPartyId | PARTY_ID | — | ✅ |
| 21 | InvoiceHeaderPaymentCurrencyCode | PAYMENT_CURRENCY_CODE | — | ✅ |
| 22 | InvoiceHeaderPaymentMethodCode | PAYMENT_METHOD_CODE | — | ✅ |
| 23 | InvoiceHeaderPaymentReasonComments | PAYMENT_REASON_COMMENTS | — | ✅ |
| 24 | InvoiceHeaderPaymentStatusFlag | PAYMENT_STATUS_FLAG | — | ✅ |
| 25 | InvoiceHeaderRoutingAttribute1 | ROUTING_ATTRIBUTE1 | — | ✅ |
| 26 | InvoiceHeaderRoutingAttribute2 | ROUTING_ATTRIBUTE2 | — | ✅ |
| 27 | InvoiceHeaderRoutingAttribute3 | ROUTING_ATTRIBUTE3 | — | ✅ |
| 28 | InvoiceHeaderRoutingAttribute4 | ROUTING_ATTRIBUTE4 | — | ✅ |
| 29 | InvoiceHeaderSchedInvoiceId | INVOICE_ID | — | — |
| 30 | InvoiceHeaderSchedLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 31 | InvoiceHeaderSetOfBooksId | SET_OF_BOOKS_ID | — | ✅ |
| 32 | InvoiceHeaderSettlementPriority | SETTLEMENT_PRIORITY | — | ✅ |
| 33 | InvoiceHeaderSource | SOURCE | — | ✅ |
| 34 | InvoiceHeaderTermsId | TERMS_ID | — | ✅ |
| 35 | InvoiceHeaderUniqueRemittanceIdentifier | UNIQUE_REMITTANCE_IDENTIFIER | — | ✅ |
| 36 | InvoiceHeaderVendorId | VENDOR_ID | — | — |
| 37 | InvoiceHeaderVendorSiteId | VENDOR_SITE_ID | — | ✅ |
| 38 | InvoiceHeaderVoucherNum | VOUCHER_NUM | — | ✅ |

### [[ap_invoice_distributions_all|AP_INVOICE_DISTRIBUTIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwtRelDistInvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | — |
| 2 | AwtRelDistLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | InvDistsInvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | — |
| 4 | InvDistsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | InvDistsPJC_EXPENDITURE_TYPE_ID | PJC_EXPENDITURE_TYPE_ID | — | ✅ |
| 6 | InvDistsPJC_ORGANIZATION_ID | PJC_ORGANIZATION_ID | — | ✅ |
| 7 | InvDistsPJC_PROJECT_ID | PJC_PROJECT_ID | — | ✅ |
| 8 | InvDistsPJC_TASK_ID | PJC_TASK_ID | — | ✅ |
| 9 | InvoiceDistributionDistributionLineNumber | DISTRIBUTION_LINE_NUMBER | — | ✅ |
| 10 | InvoiceDistributionInvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | — |

### [[ap_invoice_payments_all|AP_INVOICE_PAYMENTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DiscountOffersTransNameType | ASSIGNMENT_TYPE_CODE | — | — |
| 2 | InvoicePaymentAccountingDate | ACCOUNTING_DATE | — | ✅ |
| 3 | InvoicePaymentAcctsPayCodeCombinationId | ACCTS_PAY_CODE_COMBINATION_ID | — | — |
| 4 | InvoicePaymentAnnualPercentageRate | ANNUAL_PERCENTAGE_RATE | — | ✅ |
| 5 | InvoicePaymentAssetCodeCombinationId | ASSET_CODE_COMBINATION_ID | — | — |
| 6 | InvoicePaymentBankAccountNum | BANK_ACCOUNT_NUM | — | ✅ |
| 7 | InvoicePaymentBankAccountType | BANK_ACCOUNT_TYPE | — | ✅ |
| 8 | InvoicePaymentBankNum | BANK_NUM | — | ✅ |
| 9 | InvoicePaymentCheckId | CHECK_ID | — | — |
| 10 | InvoicePaymentCreatedBy | CREATED_BY | — | ✅ |
| 11 | InvoicePaymentCreationDate | CREATION_DATE | — | ✅ |
| 12 | InvoicePaymentDaysAccelerated | DAYS_ACCELERATED | — | ✅ |
| 13 | InvoicePaymentDiscountLost | DISCOUNT_LOST | — | ✅ |
| 14 | InvoicePaymentDiscountTaken | DISCOUNT_TAKEN | — | ✅ |
| 15 | InvoicePaymentDiscountTakenInvCurr | DISCOUNT_TAKEN_INV_CURR | — | ✅ |
| 16 | InvoicePaymentExchangeDate | EXCHANGE_DATE | — | ✅ |
| 17 | InvoicePaymentExchangeRate | EXCHANGE_RATE | — | ✅ |
| 18 | InvoicePaymentExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 19 | InvoicePaymentGainCodeCombinationId | GAIN_CODE_COMBINATION_ID | — | — |
| 20 | InvoicePaymentIbanNumber | IBAN_NUMBER | — | ✅ |
| 21 | InvoicePaymentInvoiceId | INVOICE_ID | — | ✅ |
| 22 | InvoicePaymentInvoicePaymentId | INVOICE_PAYMENT_ID | — | ✅ |
| 23 | InvoicePaymentInvoicePaymentType | INVOICE_PAYMENT_TYPE | — | ✅ |
| 24 | InvoicePaymentInvoicingVendorSiteId | INVOICING_VENDOR_SITE_ID | — | — |
| 25 | InvoicePaymentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | InvoicePaymentLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 27 | InvoicePaymentLossCodeCombinationId | LOSS_CODE_COMBINATION_ID | — | — |
| 28 | InvoicePaymentOrgId | ORG_ID | — | ✅ |
| 29 | InvoicePaymentPaymentNum | PAYMENT_NUM | — | ✅ |
| 30 | InvoicePaymentPeriodName | PERIOD_NAME | — | ✅ |
| 31 | InvoicePaymentPostedFlag | POSTED_FLAG | — | ✅ |
| 32 | InvoicePaymentRemitToAddressName | REMIT_TO_ADDRESS_NAME | — | ✅ |
| 33 | InvoicePaymentRemitToSupplierName | REMIT_TO_SUPPLIER_NAME | — | ✅ |
| 34 | InvoicePaymentReversalFlag | REVERSAL_FLAG | — | ✅ |
| 35 | InvoicePaymentReversalInvPmtId | REVERSAL_INV_PMT_ID | — | ✅ |
| 36 | InvoicePaymentSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 37 | InvoicePaymentXCurrRate | X_CURR_RATE | — | ✅ |

### [[ap_inv_selection_criteria_all|AP_INV_SELECTION_CRITERIA_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PmtProcReqInvCheckrunId | CHECKRUN_ID | — | — |
| 2 | PmtProcReqInvLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[ap_payment_history_all|AP_PAYMENT_HISTORY_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentHistoryCheckId | CHECK_ID | — | — |
| 2 | PaymentHistoryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | PaymentHistoryOrgId | ORG_ID | — | — |
| 4 | PaymentHistoryPaymentHistoryId | PAYMENT_HISTORY_ID | — | — |
| 5 | PaymentHistoryPostedFlag | POSTED_FLAG | — | ✅ |
| 6 | PaymentHistoryTransactionType | TRANSACTION_TYPE | — | ✅ |

### [[ap_payment_hist_dists|AP_PAYMENT_HIST_DISTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentHistDistId | PAYMENT_HIST_DIST_ID | 🔑 | ✅ |
| 2 | PaymentHistDistsAccountingEventId | ACCOUNTING_EVENT_ID | — | — |
| 3 | PaymentHistDistsAmount | AMOUNT | — | ✅ |
| 4 | PaymentHistDistsAmountVariance | AMOUNT_VARIANCE | — | ✅ |
| 5 | PaymentHistDistsAwtRelatedId | AWT_RELATED_ID | — | — |
| 6 | PaymentHistDistsBankCurrAmount | BANK_CURR_AMOUNT | — | ✅ |
| 7 | PaymentHistDistsClearedBaseAmount | CLEARED_BASE_AMOUNT | — | ✅ |
| 8 | PaymentHistDistsCreatedBy | CREATED_BY | — | — |
| 9 | PaymentHistDistsCreationDate | CREATION_DATE | — | ✅ |
| 10 | PaymentHistDistsHistoricalFlag | HISTORICAL_FLAG | — | — |
| 11 | PaymentHistDistsInvoiceAdjustmentEventId | INVOICE_ADJUSTMENT_EVENT_ID | — | — |
| 12 | PaymentHistDistsInvoiceBaseAmtVariance | INVOICE_BASE_AMT_VARIANCE | — | ✅ |
| 13 | PaymentHistDistsInvoiceBaseQtyVariance | INVOICE_BASE_QTY_VARIANCE | — | — |
| 14 | PaymentHistDistsInvoiceDistAmount | INVOICE_DIST_AMOUNT | — | ✅ |
| 15 | PaymentHistDistsInvoiceDistBaseAmount | INVOICE_DIST_BASE_AMOUNT | — | ✅ |
| 16 | PaymentHistDistsInvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | ✅ |
| 17 | PaymentHistDistsInvoicePaymentId | INVOICE_PAYMENT_ID | — | — |
| 18 | PaymentHistDistsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | PaymentHistDistsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | PaymentHistDistsLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 21 | PaymentHistDistsMaturedBaseAmount | MATURED_BASE_AMOUNT | — | ✅ |
| 22 | PaymentHistDistsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | PaymentHistDistsPaAdditionFlag | PA_ADDITION_FLAG | — | — |
| 24 | PaymentHistDistsPaidBaseAmount | PAID_BASE_AMOUNT | — | ✅ |
| 25 | PaymentHistDistsPayDistLookupCode | PAY_DIST_LOOKUP_CODE | — | ✅ |
| 26 | PaymentHistDistsPaymentHistoryId | PAYMENT_HISTORY_ID | — | — |
| 27 | PaymentHistDistsProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 28 | PaymentHistDistsProgramId | PROGRAM_ID | — | — |
| 29 | PaymentHistDistsProgramLoginId | PROGRAM_LOGIN_ID | — | — |
| 30 | PaymentHistDistsProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 31 | PaymentHistDistsQuantityVariance | QUANTITY_VARIANCE | — | — |
| 32 | PaymentHistDistsReleaseInvDistDerivedFrom | RELEASE_INV_DIST_DERIVED_FROM | — | — |
| 33 | PaymentHistDistsRequestId | REQUEST_ID | — | — |
| 34 | PaymentHistDistsReversalFlag | REVERSAL_FLAG | — | — |
| 35 | PaymentHistDistsReversedPayHistDistId | REVERSED_PAY_HIST_DIST_ID | — | ✅ |
| 36 | PaymentHistDistsRoundingAmt | ROUNDING_AMT | — | ✅ |

### [[ap_payment_schedules_all|AP_PAYMENT_SCHEDULES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceHeaderRemitToSupplierId | REMIT_TO_SUPPLIER_ID | — | ✅ |
| 2 | PaymentScheduleDueDate | DUE_DATE | — | ✅ |
| 3 | PaymentScheduleInvoiceId | INVOICE_ID | — | — |
| 4 | PaymentScheduleLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PaymentScheduleOrgId | ORG_ID | — | — |
| 6 | PaymentSchedulePaymentMethodCode | PAYMENT_METHOD_CODE | — | ✅ |
| 7 | PaymentSchedulePaymentNum | PAYMENT_NUM | — | ✅ |
| 8 | PaymentSchedulePaymentStatusFlag | PAYMENT_STATUS_FLAG | — | ✅ |

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

### [[ap_system_parameters_all|AP_SYSTEM_PARAMETERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SystemOptionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | SystemOptionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | SystemOptionOrgId | ORG_ID | — | — |
| 4 | SystemOptionWhenToAccountPmt | WHEN_TO_ACCOUNT_PMT | — | ✅ |

### [[ap_terms_tl|AP_TERMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentTermLanguage | LANGUAGE | — | — |
| 2 | PaymentTermName | NAME | — | ✅ |
| 3 | PaymentTermTermId | TERM_ID | — | — |

### [[ce_all_bank_branches_v|CE_ALL_BANK_BRANCHES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllBankBranchesBankName | BANK_NAME | — | ✅ |
| 2 | AllBankBranchesBranchNumber | BRANCH_NUMBER | — | ✅ |
| 3 | AllBankBranchesBranchPartyId | BRANCH_PARTY_ID | — | — |
| 4 | AllBankBranchesEftSwiftCode | EFT_SWIFT_CODE | — | — |
| 5 | ExtBnkAcctBankBranchName | BANK_BRANCH_NAME | — | ✅ |

### [[ce_bank_acct_uses_all|CE_BANK_ACCT_USES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankAccountUseBankAccountId | BANK_ACCOUNT_ID | — | ✅ |
| 2 | BankAccountUseBankAcctUseId | BANK_ACCT_USE_ID | — | — |
| 3 | BankAccountUseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[ce_internal_bank_accts_v|CE_INTERNAL_BANK_ACCTS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankAcctDistBankAccountId | BANK_ACCOUNT_ID | — | — |
| 2 | BankAcctDistLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[ce_payment_documents|CE_PAYMENT_DOCUMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayDocLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | PayDocPaymentDocumentId | PAYMENT_DOCUMENT_ID | — | — |
| 3 | PayDocPaymentDocumentName | PAYMENT_DOCUMENT_NAME | — | ✅ |

### [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocSequenceDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 2 | DocSequenceName | NAME | — | ✅ |

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitBusinessUnitId | BU_ID | — | — |
| 2 | BusinessUnitLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | InvoicingBuBusinessUnitId | BU_ID | — | — |
| 4 | InvoicingBuName | BU_NAME | — | ✅ |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankRateTypeConversionType | CONVERSION_TYPE | — | — |
| 2 | BankRateTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | ClearedExchangeRateTypeConversionType | CONVERSION_TYPE | — | — |
| 4 | ClearedExchangeRateTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ExchangeRateTypeConversionType | CONVERSION_TYPE | — | — |
| 6 | ExchangeRateTypeInvPaymentConversionType | CONVERSION_TYPE | — | — |
| 7 | ExchangeRateTypeInvPaymentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ExchangeRateTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ExchangeRateTypeUserConversionType | USER_CONVERSION_TYPE | — | ✅ |
| 10 | InvoiceConversionTypeConversionType | CONVERSION_TYPE | — | — |
| 11 | InvoiceConversionTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | MaturityExchangeRateTypeConversionType | CONVERSION_TYPE | — | — |
| 13 | MaturityExchangeRateTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | PaymentConversionTypeConversionType | CONVERSION_TYPE | — | — |
| 15 | PaymentConversionTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | PmtRateTypeConversionType | CONVERSION_TYPE | — | — |
| 17 | PmtRateTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 2 | LedgersLedgerId | LEDGER_ID | — | — |
| 3 | LedgersName | NAME | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyChkLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | PartyChkPartyId | PARTY_ID | — | — |
| 3 | PartyChkPartyName | PARTY_NAME | — | ✅ |
| 4 | PartyHdrLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PartyHdrPartyId | PARTY_ID | — | — |
| 6 | PartyInvPayLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PartyInvPayPartyId | PARTY_ID | — | — |
| 8 | PartyInvPayPartyName | PARTY_NAME | — | ✅ |
| 9 | PartyPartyName | PARTY_NAME | — | ✅ |

### [[hz_party_sites|HZ_PARTY_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartySiteChkLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | PartySiteChkPartySiteId | PARTY_SITE_ID | — | — |
| 3 | PartySiteChkPartySiteName | PARTY_SITE_NAME | — | ✅ |
| 4 | PartySiteHdrLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PartySiteHdrPartySiteId | PARTY_SITE_ID | — | — |
| 6 | PartySiteInvPayLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PartySiteInvPayPartySiteId | PARTY_SITE_ID | — | — |
| 8 | PartySiteInvPayPartySiteName | PARTY_SITE_NAME | — | ✅ |
| 9 | PartySitePartySiteName | PARTY_SITE_NAME | — | ✅ |

### [[iby_acct_pmt_profiles_tl|IBY_ACCT_PMT_PROFILES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayProfiLanguage | LANGUAGE | — | — |
| 2 | PayProfiPaymentProfileId | PAYMENT_PROFILE_ID | — | — |
| 3 | PayProfiPaymentProfileName | PAYMENT_PROFILE_NAME | — | ✅ |

### [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExtBnkAcctBaMaskSetting | BA_MASK_SETTING | — | — |
| 2 | ExtBnkAcctBankAccountName | BANK_ACCOUNT_NAME | — | ✅ |
| 3 | ExtBnkAcctBankBranchPartyFlag | BANK_BRANCH_PARTY_FLAG | — | — |
| 4 | ExtBnkAcctBranchNumber | BRANCH_NUMBER | — | ✅ |
| 5 | ExtBnkAcctCheckDigits | CHECK_DIGITS | — | ✅ |
| 6 | ExtBnkAcctCountryCode | COUNTRY_CODE | — | ✅ |
| 7 | ExtBnkAcctDescription | DESCRIPTION | — | ✅ |
| 8 | ExtBnkAcctExtBankAccountId | EXT_BANK_ACCOUNT_ID | — | — |
| 9 | ExtBnkAcctIban | IBAN | — | — |
| 10 | ExtBnkAcctMaskedBankAccountNum | MASKED_BANK_ACCOUNT_NUM | — | ✅ |
| 11 | ExtBnkAcctMaskedIban | MASKED_IBAN | — | — |
| 12 | ExtBnkAcctSecondaryAccountReference | SECONDARY_ACCOUNT_REFERENCE | — | ✅ |
| 13 | ExtBnkAcctSwiftCode | EFT_SWIFT_CODE | — | — |
| 14 | InvExtBnkAcctExtBankAccountId | EXT_BANK_ACCOUNT_ID | — | — |
| 15 | InvExtBnkAcctLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | PayExtBnkAcctExtBankAccountId | EXT_BANK_ACCOUNT_ID | — | — |
| 17 | PayExtBnkAcctLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[iby_payments_all|IBY_PAYMENTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChkPaymentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | ChkPaymentPaymentId | PAYMENT_ID | — | — |

### [[iby_payment_codes_vl|IBY_PAYMENT_CODES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayDelcodeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | PayDelcodePaymentCode | PAYMENT_CODE | — | — |
| 3 | PayDelcodePaymentCodeType | PAYMENT_CODE_TYPE | — | — |
| 4 | PayReacodeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PayReacodePaymentCode | PAYMENT_CODE | — | — |
| 6 | PayReacodePaymentCodeType | PAYMENT_CODE_TYPE | — | — |

### [[iby_payment_methods_tl|IBY_PAYMENT_METHODS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentMethodCode | PAYMENT_METHOD_CODE | — | ✅ |
| 2 | PaymentMethodLanguage | LANGUAGE | — | — |
| 3 | PaymentMethodName | PAYMENT_METHOD_NAME | — | ✅ |

### [[iby_pay_instructions_all|IBY_PAY_INSTRUCTIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayInstrnLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | PayInstrnPaymentInstructionId | PAYMENT_INSTRUCTION_ID | — | — |

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
| 8 | PersonNameStpByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 9 | PersonNameStpByEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 10 | PersonNameStpByPersonNameId | PERSON_NAME_ID | — | — |
| 11 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 12 | PersonUpdatedByEffectiveEndDate2 | EFFECTIVE_END_DATE | — | — |
| 13 | PersonUpdatedByEffectiveStartDate2 | EFFECTIVE_START_DATE | — | ✅ |
| 14 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[po_headers_all|PO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchaseOrderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | PurchaseOrderPoHeaderId | PO_HEADER_ID | — | — |
| 3 | PurchaseOrderSegment1 | SEGMENT1 | — | ✅ |
| 4 | QuickPurchaseOrderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | QuickPurchaseOrderPoHeaderId | PO_HEADER_ID | — | — |

### [[xla_events|XLA_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayEvntEventId | EVENT_ID | — | — |
| 2 | PayEvntLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | PayHistDistEvntEventId | EVENT_ID | — | — |
| 4 | PayHistDistEvntLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[zx_wht_tax_classification_v|ZX_WHT_TAX_CLASSIFICATION_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WithholdingTaxGroupGroupId | GROUP_ID | — | — |
| 2 | WithholdingTaxGroupLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
