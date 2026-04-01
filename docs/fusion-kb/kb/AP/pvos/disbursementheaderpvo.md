---
id: DOC-AP-PVO-DisbursementHeaderPVO
doc_type: system-doc
title: "DisbursementHeaderPVO — PVO Accounts Payable"
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
  - DisbursementHeaderPVO
  - disbursementheaderpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DisbursementHeaderPVO

## 📌 Visão Geral

Extrai os cabeçalhos de desembolsos (pagamentos emitidos), incluindo dados do fornecedor, banco, conta bancária, método de pagamento, moeda e valores. Permite controle de tesouraria, reconciliação bancária e análise do fluxo de saída de caixa.

**Caminho:** `FscmTopModelAM.FinApPmtSinglePaymentsAM.DisbursementHeaderPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 169 | 14 | 1 | 74 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[ap_checks_all|AP_CHECKS_ALL]] — 114 atributos (1 PKs, 49 BICC)
- [[ap_system_parameters_all|AP_SYSTEM_PARAMETERS_ALL]] — 3 atributos (1 BICC)
- [[ce_all_bank_branches_v|CE_ALL_BANK_BRANCHES_V]] — 5 atributos (3 BICC)
- [[ce_bank_acct_uses_all|CE_BANK_ACCT_USES_ALL]] — 2 atributos
- [[ce_payment_documents|CE_PAYMENT_DOCUMENTS]] — 3 atributos (2 BICC)
- [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]] — 2 atributos (1 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 1 atributos
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 2 atributos (1 BICC)
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 4 atributos
- [[hz_parties|HZ_PARTIES]] — 3 atributos (2 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 3 atributos (2 BICC)
- [[iby_acct_pmt_profiles_tl|IBY_ACCT_PMT_PROFILES_TL]] — 3 atributos (1 BICC)
- [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]] — 13 atributos (7 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 11 atributos (5 BICC)

---

## ⚙️ Atributos

### [[ap_checks_all|AP_CHECKS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CheckId | CHECK_ID | 🔑 | ✅ |
| 2 | ChecksActualValueDate | ACTUAL_VALUE_DATE | — | ✅ |
| 3 | ChecksAddressLine1 | ADDRESS_LINE1 | — | ✅ |
| 4 | ChecksAddressLine2 | ADDRESS_LINE2 | — | ✅ |
| 5 | ChecksAddressLine3 | ADDRESS_LINE3 | — | ✅ |
| 6 | ChecksAddressLine4 | ADDRESS_LINE4 | — | ✅ |
| 7 | ChecksAddressStyle | ADDRESS_STYLE | — | — |
| 8 | ChecksAmount | AMOUNT | — | ✅ |
| 9 | ChecksAnticipatedValueDate | ANTICIPATED_VALUE_DATE | — | — |
| 10 | ChecksBankAccountName | BANK_ACCOUNT_NAME | — | — |
| 11 | ChecksBankAccountNum | BANK_ACCOUNT_NUM | — | — |
| 12 | ChecksBankAccountType | BANK_ACCOUNT_TYPE | — | ✅ |
| 13 | ChecksBankChargeBearer | BANK_CHARGE_BEARER | — | ✅ |
| 14 | ChecksBankNum | BANK_NUM | — | ✅ |
| 15 | ChecksBaseAmount | BASE_AMOUNT | — | ✅ |
| 16 | ChecksCeBankAcctUseId | CE_BANK_ACCT_USE_ID | — | — |
| 17 | ChecksCheckDate | CHECK_DATE | — | ✅ |
| 18 | ChecksCheckFormatId | CHECK_FORMAT_ID | — | — |
| 19 | ChecksCheckNumber | CHECK_NUMBER | — | ✅ |
| 20 | ChecksCheckStockId | CHECK_STOCK_ID | — | — |
| 21 | ChecksCheckVoucherNum | CHECK_VOUCHER_NUM | — | ✅ |
| 22 | ChecksCheckrunId | CHECKRUN_ID | — | — |
| 23 | ChecksCheckrunName | CHECKRUN_NAME | — | ✅ |
| 24 | ChecksCity | CITY | — | ✅ |
| 25 | ChecksClearedAmount | CLEARED_AMOUNT | — | ✅ |
| 26 | ChecksClearedBaseAmount | CLEARED_BASE_AMOUNT | — | — |
| 27 | ChecksClearedChargesAmount | CLEARED_CHARGES_AMOUNT | — | — |
| 28 | ChecksClearedChargesBaseAmount | CLEARED_CHARGES_BASE_AMOUNT | — | — |
| 29 | ChecksClearedDate | CLEARED_DATE | — | ✅ |
| 30 | ChecksClearedErrorAmount | CLEARED_ERROR_AMOUNT | — | — |
| 31 | ChecksClearedErrorBaseAmount | CLEARED_ERROR_BASE_AMOUNT | — | — |
| 32 | ChecksClearedExchangeDate | CLEARED_EXCHANGE_DATE | — | — |
| 33 | ChecksClearedExchangeRate | CLEARED_EXCHANGE_RATE | — | — |
| 34 | ChecksClearedExchangeRateType | CLEARED_EXCHANGE_RATE_TYPE | — | — |
| 35 | ChecksCompletedPmtsGroupId | COMPLETED_PMTS_GROUP_ID | — | — |
| 36 | ChecksCountry | COUNTRY | — | ✅ |
| 37 | ChecksCounty | COUNTY | — | ✅ |
| 38 | ChecksCreatedBy | CREATED_BY | — | ✅ |
| 39 | ChecksCreationDate | CREATION_DATE | — | ✅ |
| 40 | ChecksCurrencyCode | CURRENCY_CODE | — | ✅ |
| 41 | ChecksDescription | DESCRIPTION | — | ✅ |
| 42 | ChecksDocCategoryCode | DOC_CATEGORY_CODE | — | — |
| 43 | ChecksDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 44 | ChecksDocSequenceValue | DOC_SEQUENCE_VALUE | — | ✅ |
| 45 | ChecksEmployeeAddressCode | EMPLOYEE_ADDRESS_CODE | — | — |
| 46 | ChecksExchangeDate | EXCHANGE_DATE | — | ✅ |
| 47 | ChecksExchangeRate | EXCHANGE_RATE | — | ✅ |
| 48 | ChecksExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 49 | ChecksExternalBankAccountId | EXTERNAL_BANK_ACCOUNT_ID | — | — |
| 50 | ChecksFuturePayDueDate | FUTURE_PAY_DUE_DATE | — | ✅ |
| 51 | ChecksLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 52 | ChecksLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 53 | ChecksLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 54 | ChecksLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 55 | ChecksLogicalGroupReference | LOGICAL_GROUP_REFERENCE | — | — |
| 56 | ChecksMaturityExchangeDate | MATURITY_EXCHANGE_DATE | — | ✅ |
| 57 | ChecksMaturityExchangeRate | MATURITY_EXCHANGE_RATE | — | ✅ |
| 58 | ChecksMaturityExchangeRateType | MATURITY_EXCHANGE_RATE_TYPE | — | ✅ |
| 59 | ChecksMrcBaseAmount | MRC_BASE_AMOUNT | — | — |
| 60 | ChecksMrcClearedBaseAmount | MRC_CLEARED_BASE_AMOUNT | — | — |
| 61 | ChecksMrcClearedChargesBaseAmt | MRC_CLEARED_CHARGES_BASE_AMT | — | — |
| 62 | ChecksMrcClearedErrorBaseAmount | MRC_CLEARED_ERROR_BASE_AMOUNT | — | — |
| 63 | ChecksMrcClearedExchangeDate | MRC_CLEARED_EXCHANGE_DATE | — | — |
| 64 | ChecksMrcClearedExchangeRate | MRC_CLEARED_EXCHANGE_RATE | — | — |
| 65 | ChecksMrcClearedExchangeRateType | MRC_CLEARED_EXCHANGE_RATE_TYPE | — | — |
| 66 | ChecksMrcExchangeDate | MRC_EXCHANGE_DATE | — | — |
| 67 | ChecksMrcExchangeRate | MRC_EXCHANGE_RATE | — | — |
| 68 | ChecksMrcExchangeRateType | MRC_EXCHANGE_RATE_TYPE | — | — |
| 69 | ChecksMrcMaturityExgDate | MRC_MATURITY_EXG_DATE | — | — |
| 70 | ChecksMrcMaturityExgRate | MRC_MATURITY_EXG_RATE | — | — |
| 71 | ChecksMrcMaturityExgRateType | MRC_MATURITY_EXG_RATE_TYPE | — | — |
| 72 | ChecksMrcStampDutyBaseAmt | MRC_STAMP_DUTY_BASE_AMT | — | — |
| 73 | ChecksObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 74 | ChecksOrgId | ORG_ID | — | — |
| 75 | ChecksPartyId | PARTY_ID | — | — |
| 76 | ChecksPartySiteId | PARTY_SITE_ID | — | — |
| 77 | ChecksPaymentDocumentId | PAYMENT_DOCUMENT_ID | — | — |
| 78 | ChecksPaymentId | PAYMENT_ID | — | — |
| 79 | ChecksPaymentInstructionId | PAYMENT_INSTRUCTION_ID | — | — |
| 80 | ChecksPaymentMethodCode | PAYMENT_METHOD_CODE | — | ✅ |
| 81 | ChecksPaymentMethodLookupCode | PAYMENT_METHOD_LOOKUP_CODE | — | — |
| 82 | ChecksPaymentProfileId | PAYMENT_PROFILE_ID | — | — |
| 83 | ChecksPaymentTypeFlag | PAYMENT_TYPE_FLAG | — | ✅ |
| 84 | ChecksPositivePayStatusCode | POSITIVE_PAY_STATUS_CODE | — | — |
| 85 | ChecksProvince | PROVINCE | — | ✅ |
| 86 | ChecksReconFlag | RECON_FLAG | — | ✅ |
| 87 | ChecksReconciliationBatchId | RECONCILIATION_BATCH_ID | — | — |
| 88 | ChecksRelationshipId | RELATIONSHIP_ID | — | — |
| 89 | ChecksReleasedBy | RELEASED_BY | — | — |
| 90 | ChecksReleasedDate | RELEASED_DATE | — | ✅ |
| 91 | ChecksRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 92 | ChecksRemitToAddressName | REMIT_TO_ADDRESS_NAME | — | ✅ |
| 93 | ChecksRemitToSupplierId | REMIT_TO_SUPPLIER_ID | — | — |
| 94 | ChecksRemitToSupplierName | REMIT_TO_SUPPLIER_NAME | — | ✅ |
| 95 | ChecksRequestId | REQUEST_ID | — | — |
| 96 | ChecksSettlementPriority | SETTLEMENT_PRIORITY | — | ✅ |
| 97 | ChecksStampDutyAmt | STAMP_DUTY_AMT | — | — |
| 98 | ChecksStampDutyBaseAmt | STAMP_DUTY_BASE_AMT | — | — |
| 99 | ChecksState | STATE | — | ✅ |
| 100 | ChecksStatusLookupCode | STATUS_LOOKUP_CODE | — | ✅ |
| 101 | ChecksStoppedBy | STOPPED_BY | — | — |
| 102 | ChecksStoppedDate | STOPPED_DATE | — | ✅ |
| 103 | ChecksTransferPriority | TRANSFER_PRIORITY | — | — |
| 104 | ChecksTreasuryPayDate | TREASURY_PAY_DATE | — | — |
| 105 | ChecksTreasuryPayNumber | TREASURY_PAY_NUMBER | — | — |
| 106 | ChecksUssglTransactionCode | USSGL_TRANSACTION_CODE | — | — |
| 107 | ChecksUssglTrxCodeContext | USSGL_TRX_CODE_CONTEXT | — | — |
| 108 | ChecksVendorId | VENDOR_ID | — | — |
| 109 | ChecksVendorName | VENDOR_NAME | — | ✅ |
| 110 | ChecksVendorSiteCode | VENDOR_SITE_CODE | — | ✅ |
| 111 | ChecksVendorSiteId | VENDOR_SITE_ID | — | — |
| 112 | ChecksVoidDate | VOID_DATE | — | ✅ |
| 113 | ChecksXCurrRateType | X_CURR_RATE_TYPE | — | ✅ |
| 114 | ChecksZip | ZIP | — | ✅ |

### [[ap_system_parameters_all|AP_SYSTEM_PARAMETERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SystemOptionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | SystemOptionOrgId | ORG_ID | — | — |
| 3 | SystemOptionWhenToAccountPmt | WHEN_TO_ACCOUNT_PMT | — | ✅ |

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
| 1 | BusinessUnitBusinessUnitId | BU_ID | — | — |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExchangeRateTypeConversionType | CONVERSION_TYPE | — | — |
| 2 | ExchangeRateTypeUserConversionType | USER_CONVERSION_TYPE | — | ✅ |

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPrimaryLedgerId | ORG_INFORMATION3 | — | — |
| 2 | OrgInfoEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | OrgInfoEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | OrgInfoOrgInformationId | ORG_INFORMATION_ID | — | — |

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
| 3 | PartySitePartySiteName | PARTY_SITE_NAME | — | ✅ |

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

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
