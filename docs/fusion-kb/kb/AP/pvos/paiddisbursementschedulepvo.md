---
id: DOC-AP-PVO-PaidDisbursementSchedulePVO
doc_type: system-doc
title: "PaidDisbursementSchedulePVO — PVO Accounts Payable"
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
  - PaidDisbursementSchedulePVO
  - paiddisbursementschedulepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PaidDisbursementSchedulePVO

## 📌 Visão Geral

Extrai o detalhamento completo dos pagamentos realizados a fornecedores, incluindo fatura, parcela, desconto aplicado, banco, documento de pagamento e reconciliação. Essencial para reconciliação bancária, análise de descontos obtidos e auditoria do ciclo completo de pagamento.

**Caminho:** `FscmTopModelAM.FinApPmtSinglePaymentsAM.PaidDisbursementSchedulePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 216 | 23 | 1 | 131 | 61% |

---

## 🔗 Tabelas Relacionadas

- [[ap_batches_all|AP_BATCHES_ALL]] — 2 atributos (1 BICC)
- [[ap_checks_all|AP_CHECKS_ALL]] — 49 atributos (44 BICC)
- [[ap_discount_offers_tl|AP_DISCOUNT_OFFERS_TL]] — 3 atributos (1 BICC)
- [[ap_invoices_all|AP_INVOICES_ALL]] — 20 atributos (18 BICC)
- [[ap_invoice_payments_all|AP_INVOICE_PAYMENTS_ALL]] — 62 atributos (1 PKs, 29 BICC)
- [[ap_payment_schedules_all|AP_PAYMENT_SCHEDULES_ALL]] — 3 atributos (1 BICC)
- [[ap_recon_difference_details|AP_RECON_DIFFERENCE_DETAILS]] — 4 atributos
- [[ap_system_parameters_all|AP_SYSTEM_PARAMETERS_ALL]] — 3 atributos (1 BICC)
- [[ap_terms_tl|AP_TERMS_TL]] — 3 atributos (1 BICC)
- [[ce_all_bank_branches_v|CE_ALL_BANK_BRANCHES_V]] — 5 atributos (3 BICC)
- [[ce_bank_acct_uses_all|CE_BANK_ACCT_USES_ALL]] — 2 atributos
- [[ce_payment_documents|CE_PAYMENT_DOCUMENTS]] — 3 atributos (2 BICC)
- [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]] — 2 atributos (1 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 2 atributos (1 BICC)
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 2 atributos (1 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 3 atributos (1 BICC)
- [[hz_parties|HZ_PARTIES]] — 8 atributos (5 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 8 atributos (5 BICC)
- [[iby_acct_pmt_profiles_tl|IBY_ACCT_PMT_PROFILES_TL]] — 3 atributos (1 BICC)
- [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]] — 13 atributos (7 BICC)
- [[iby_payment_methods_tl|IBY_PAYMENT_METHODS_TL]] — 3 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 11 atributos (5 BICC)
- [[po_headers_all|PO_HEADERS_ALL]] — 2 atributos (1 BICC)

---

## ⚙️ Atributos

### [[ap_batches_all|AP_BATCHES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceBatchBatchId | BATCH_ID | — | — |
| 2 | InvoiceBatchBatchName | BATCH_NAME | — | ✅ |

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
| 9 | ChecksCheckId | CHECK_ID | — | — |
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
| 31 | ChecksOrgId | ORG_ID | — | — |
| 32 | ChecksPaymentMethodCode | PAYMENT_METHOD_CODE | — | ✅ |
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
| 43 | ChecksVendorId | VENDOR_ID | — | — |
| 44 | ChecksVendorName | VENDOR_NAME | — | ✅ |
| 45 | ChecksVendorSiteCode | VENDOR_SITE_CODE | — | ✅ |
| 46 | ChecksVendorSiteId | VENDOR_SITE_ID | — | — |
| 47 | ChecksVoidDate | VOID_DATE | — | ✅ |
| 48 | ChecksXCurrRateType | X_CURR_RATE_TYPE | — | ✅ |
| 49 | ChecksZip | ZIP | — | ✅ |

### [[ap_discount_offers_tl|AP_DISCOUNT_OFFERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DiscOfferTransDiscountOfferId | DISCOUNT_OFFER_ID | — | — |
| 2 | DiscOfferTransLanguage | LANGUAGE | — | — |
| 3 | DiscountOffersTranslationName | NAME | — | ✅ |

### [[ap_invoices_all|AP_INVOICES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceHeaderAmountPaid | AMOUNT_PAID | — | ✅ |
| 2 | InvoiceHeaderBaseAmount | BASE_AMOUNT | — | ✅ |
| 3 | InvoiceHeaderDescription | DESCRIPTION | — | ✅ |
| 4 | InvoiceHeaderExchangeDate | EXCHANGE_DATE | — | ✅ |
| 5 | InvoiceHeaderExchangeRate | EXCHANGE_RATE | — | ✅ |
| 6 | InvoiceHeaderExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 7 | InvoiceHeaderInvoiceAmount | INVOICE_AMOUNT | — | ✅ |
| 8 | InvoiceHeaderInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 9 | InvoiceHeaderInvoiceDate | INVOICE_DATE | — | ✅ |
| 10 | InvoiceHeaderInvoiceId | INVOICE_ID | — | — |
| 11 | InvoiceHeaderInvoiceNum | INVOICE_NUM | — | ✅ |
| 12 | InvoiceHeaderInvoiceTypeLookupCode | INVOICE_TYPE_LOOKUP_CODE | — | ✅ |
| 13 | InvoiceHeaderPaymentStatusFlag | PAYMENT_STATUS_FLAG | — | ✅ |
| 14 | InvoiceHeaderRoutingAttribute1 | ROUTING_ATTRIBUTE1 | — | ✅ |
| 15 | InvoiceHeaderRoutingAttribute2 | ROUTING_ATTRIBUTE2 | — | ✅ |
| 16 | InvoiceHeaderRoutingAttribute3 | ROUTING_ATTRIBUTE3 | — | ✅ |
| 17 | InvoiceHeaderRoutingAttribute4 | ROUTING_ATTRIBUTE4 | — | ✅ |
| 18 | InvoiceHeaderSettlementPriority | SETTLEMENT_PRIORITY | — | ✅ |
| 19 | InvoiceHeaderUniqueRemittanceIdentifier | UNIQUE_REMITTANCE_IDENTIFIER | — | ✅ |
| 20 | InvoiceHeaderVoucherNum | VOUCHER_NUM | — | ✅ |

### [[ap_invoice_payments_all|AP_INVOICE_PAYMENTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DiscountOffersTransNameType | ASSIGNMENT_TYPE_CODE | — | — |
| 2 | InvoicePaymentAccountingDate | ACCOUNTING_DATE | — | ✅ |
| 3 | InvoicePaymentAccountingEventId | ACCOUNTING_EVENT_ID | — | — |
| 4 | InvoicePaymentAcctsPayCodeCombinationId | ACCTS_PAY_CODE_COMBINATION_ID | — | — |
| 5 | InvoicePaymentAmount | AMOUNT | — | ✅ |
| 6 | InvoicePaymentAmountInvCurr | AMOUNT_INV_CURR | — | ✅ |
| 7 | InvoicePaymentAnnualPercentageRate | ANNUAL_PERCENTAGE_RATE | — | ✅ |
| 8 | InvoicePaymentAprAssignmentId | APR_ASSIGNMENT_ID | — | — |
| 9 | InvoicePaymentAssetCodeCombinationId | ASSET_CODE_COMBINATION_ID | — | — |
| 10 | InvoicePaymentAssetsAdditionFlag | ASSETS_ADDITION_FLAG | — | — |
| 11 | InvoicePaymentBankAccountNum | BANK_ACCOUNT_NUM | — | ✅ |
| 12 | InvoicePaymentBankAccountType | BANK_ACCOUNT_TYPE | — | ✅ |
| 13 | InvoicePaymentBankNum | BANK_NUM | — | ✅ |
| 14 | InvoicePaymentCheckId | CHECK_ID | — | ✅ |
| 15 | InvoicePaymentCreatedBy | CREATED_BY | — | — |
| 16 | InvoicePaymentCreationDate | CREATION_DATE | — | — |
| 17 | InvoicePaymentDaysAccelerated | DAYS_ACCELERATED | — | ✅ |
| 18 | InvoicePaymentDiscountLost | DISCOUNT_LOST | — | ✅ |
| 19 | InvoicePaymentDiscountLostInvCurr | DISCOUNT_LOST_INV_CURR | — | — |
| 20 | InvoicePaymentDiscountTaken | DISCOUNT_TAKEN | — | ✅ |
| 21 | InvoicePaymentDiscountTakenInvCurr | DISCOUNT_TAKEN_INV_CURR | — | ✅ |
| 22 | InvoicePaymentExchangeDate | EXCHANGE_DATE | — | ✅ |
| 23 | InvoicePaymentExchangeRate | EXCHANGE_RATE | — | ✅ |
| 24 | InvoicePaymentExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 25 | InvoicePaymentExternalBankAccountId | EXTERNAL_BANK_ACCOUNT_ID | — | — |
| 26 | InvoicePaymentGainCodeCombinationId | GAIN_CODE_COMBINATION_ID | — | — |
| 27 | InvoicePaymentIbanNumber | IBAN_NUMBER | — | ✅ |
| 28 | InvoicePaymentId | INVOICE_PAYMENT_ID | 🔑 | ✅ |
| 29 | InvoicePaymentInvOrgId | INV_ORG_ID | — | — |
| 30 | InvoicePaymentInvoiceBaseAmount | INVOICE_BASE_AMOUNT | — | ✅ |
| 31 | InvoicePaymentInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 32 | InvoicePaymentInvoiceId | INVOICE_ID | — | — |
| 33 | InvoicePaymentInvoicePaymentType | INVOICE_PAYMENT_TYPE | — | ✅ |
| 34 | InvoicePaymentInvoicingPartyId | INVOICING_PARTY_ID | — | — |
| 35 | InvoicePaymentInvoicingPartySiteId | INVOICING_PARTY_SITE_ID | — | — |
| 36 | InvoicePaymentInvoicingVendorSiteId | INVOICING_VENDOR_SITE_ID | — | — |
| 37 | InvoicePaymentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 38 | InvoicePaymentLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 39 | InvoicePaymentLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 40 | InvoicePaymentLossCodeCombinationId | LOSS_CODE_COMBINATION_ID | — | — |
| 41 | InvoicePaymentMrcExchangeDate | MRC_EXCHANGE_DATE | — | — |
| 42 | InvoicePaymentMrcExchangeRateType | MRC_EXCHANGE_RATE_TYPE | — | — |
| 43 | InvoicePaymentMrcFuturePayPostedFlag | MRC_FUTURE_PAY_POSTED_FLAG | — | — |
| 44 | InvoicePaymentMrcGainCodeCombinationId | MRC_GAIN_CODE_COMBINATION_ID | — | — |
| 45 | InvoicePaymentMrcInvoiceBaseAmount | MRC_INVOICE_BASE_AMOUNT | — | — |
| 46 | InvoicePaymentMrcLossCodeCombinationId | MRC_LOSS_CODE_COMBINATION_ID | — | — |
| 47 | InvoicePaymentMrcPaymentBaseAmount | MRC_PAYMENT_BASE_AMOUNT | — | — |
| 48 | InvoicePaymentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 49 | InvoicePaymentOrgId | ORG_ID | — | — |
| 50 | InvoicePaymentPaymentBaseAmount | PAYMENT_BASE_AMOUNT | — | ✅ |
| 51 | InvoicePaymentPaymentCurrencyCode | PAYMENT_CURRENCY_CODE | — | — |
| 52 | InvoicePaymentPaymentNum | PAYMENT_NUM | — | ✅ |
| 53 | InvoicePaymentPeriodName | PERIOD_NAME | — | ✅ |
| 54 | InvoicePaymentPostedFlag | POSTED_FLAG | — | ✅ |
| 55 | InvoicePaymentRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 56 | InvoicePaymentRemitToAddressName | REMIT_TO_ADDRESS_NAME | — | ✅ |
| 57 | InvoicePaymentRemitToSupplierId | REMIT_TO_SUPPLIER_ID | — | — |
| 58 | InvoicePaymentRemitToSupplierName | REMIT_TO_SUPPLIER_NAME | — | ✅ |
| 59 | InvoicePaymentReversalFlag | REVERSAL_FLAG | — | ✅ |
| 60 | InvoicePaymentReversalInvPmtId | REVERSAL_INV_PMT_ID | — | ✅ |
| 61 | InvoicePaymentSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 62 | InvoicePaymentXCurrRate | X_CURR_RATE | — | ✅ |

### [[ap_payment_schedules_all|AP_PAYMENT_SCHEDULES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentScheduleDueDate | DUE_DATE | — | ✅ |
| 2 | PaymentScheduleInvoiceId | INVOICE_ID | — | — |
| 3 | PaymentSchedulePaymentNum | PAYMENT_NUM | — | — |

### [[ap_recon_difference_details|AP_RECON_DIFFERENCE_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CauseOfDifferenceCode | CAUSE_OF_DIFFERENCE_CODE | — | — |
| 2 | ReconItemCode | RECON_ITEM_CODE | — | — |
| 3 | ReconTrxId | RECON_TRX_ID | — | — |
| 4 | RequestId | REQUEST_ID | — | — |

### [[ap_system_parameters_all|AP_SYSTEM_PARAMETERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SystemOptionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | SystemOptionOrgId | ORG_ID | — | — |
| 3 | SystemOptionWhenToAccountPmt | WHEN_TO_ACCOUNT_PMT | — | ✅ |

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
| 1 | BankAccountUseBankAccountId | BANK_ACCOUNT_ID | — | — |
| 2 | BankAccountUseBankAcctUseId | BANK_ACCT_USE_ID | — | — |

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
| 1 | InvoicingBuBusinessUnitId | BU_ID | — | — |
| 2 | InvoicingBuName | BU_NAME | — | ✅ |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExchangeRateTypeConversionType | CONVERSION_TYPE | — | — |
| 2 | ExchangeRateTypeUserConversionType | USER_CONVERSION_TYPE | — | ✅ |

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
| 4 | PartyInvPayLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PartyInvPayPartyId | PARTY_ID | — | — |
| 6 | PartyInvPayPartyName | PARTY_NAME | — | ✅ |
| 7 | PartyPartyId | PARTY_ID | — | — |
| 8 | PartyPartyName | PARTY_NAME | — | ✅ |

### [[hz_party_sites|HZ_PARTY_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartySiteChkLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | PartySiteChkPartySiteId | PARTY_SITE_ID | — | — |
| 3 | PartySiteChkPartySiteName | PARTY_SITE_NAME | — | ✅ |
| 4 | PartySiteInvPayLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PartySiteInvPayPartySiteId | PARTY_SITE_ID | — | — |
| 6 | PartySiteInvPayPartySiteName | PARTY_SITE_NAME | — | ✅ |
| 7 | PartySitePartySiteId | PARTY_SITE_ID | — | — |
| 8 | PartySitePartySiteName | PARTY_SITE_NAME | — | ✅ |

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

### [[iby_payment_methods_tl|IBY_PAYMENT_METHODS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentMethodCode | PAYMENT_METHOD_CODE | — | ✅ |
| 2 | PaymentMethodLanguage | LANGUAGE | — | — |
| 3 | PaymentMethodName | PAYMENT_METHOD_NAME | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 5 | PersonNameStpByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | PersonNameStpByEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | PersonNameStpByPersonNameId | PERSON_NAME_ID | — | — |
| 8 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 9 | PersonUpdatedByEffectiveEndDate2 | EFFECTIVE_END_DATE | — | — |
| 10 | PersonUpdatedByEffectiveStartDate2 | EFFECTIVE_START_DATE | — | ✅ |
| 11 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[po_headers_all|PO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchaseOrderPoHeaderId | PO_HEADER_ID | — | — |
| 2 | PurchaseOrderSegment1 | SEGMENT1 | — | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
