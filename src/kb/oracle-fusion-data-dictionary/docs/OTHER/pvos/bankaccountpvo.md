---
id: DOC-OTHER-PVO-BankAccountPVO
doc_type: system-doc
title: "BankAccountPVO — PVO Cross-Module"
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
  - BankAccountPVO
  - bankaccountpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BankAccountPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Bank Account. Acessa as tabelas: CE_BANKS_V, CE_BANK_BRANCHES_V, CE_INTERNAL_BANK_ACCTS_V (+1).

**Caminho:** `FscmTopModelAM.FinCeBankRelationshipsAM.BankAccountPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 221 | 4 | 1 | 27 | 12% |

---

## 🔗 Tabelas Relacionadas

- [[ce_banks_v|CE_BANKS_V]] — 35 atributos (1 BICC)
- [[ce_bank_branches_v|CE_BANK_BRANCHES_V]] — 33 atributos (1 BICC)
- [[ce_internal_bank_accts_v|CE_INTERNAL_BANK_ACCTS_V]] — 81 atributos (1 PKs, 21 BICC)
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 72 atributos (4 BICC)

---

## ⚙️ Atributos

### [[ce_banks_v|CE_BANKS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankAddressLine1 | ADDRESS_LINE1 | — | — |
| 2 | BankAddressLine2 | ADDRESS_LINE2 | — | — |
| 3 | BankAddressLine3 | ADDRESS_LINE3 | — | — |
| 4 | BankAddressLine4 | ADDRESS_LINE4 | — | — |
| 5 | BankBankAdminEmail | BANK_ADMIN_EMAIL | — | — |
| 6 | BankBankInstitutionType | BANK_INSTITUTION_TYPE | — | — |
| 7 | BankBankName | BANK_NAME | — | ✅ |
| 8 | BankBankNameAlt | BANK_NAME_ALT | — | — |
| 9 | BankBankNumber | BANK_NUMBER | — | — |
| 10 | BankBankPartyId | BANK_PARTY_ID | — | — |
| 11 | BankCity | CITY | — | — |
| 12 | BankCountry | COUNTRY | — | — |
| 13 | BankDescription | DESCRIPTION | — | — |
| 14 | BankEndDate | END_DATE | — | — |
| 15 | BankHomeCountry | HOME_COUNTRY | — | — |
| 16 | BankPkId | PK_ID | — | — |
| 17 | BankProvince | PROVINCE | — | — |
| 18 | BankRowId | ROW_ID | — | — |
| 19 | BankShortBankName | SHORT_BANK_NAME | — | — |
| 20 | BankSiteAddressLine1 | SITE_ADDRESS_LINE1 | — | — |
| 21 | BankSiteAddressLine2 | SITE_ADDRESS_LINE2 | — | — |
| 22 | BankSiteAddressLine3 | SITE_ADDRESS_LINE3 | — | — |
| 23 | BankSiteAddressLine4 | SITE_ADDRESS_LINE4 | — | — |
| 24 | BankSiteCity | SITE_CITY | — | — |
| 25 | BankSiteCountry | SITE_COUNTRY | — | — |
| 26 | BankSiteCounty | SITE_COUNTY | — | — |
| 27 | BankSiteLocationId | SITE_LOCATION_ID | — | — |
| 28 | BankSiteProvince | SITE_PROVINCE | — | — |
| 29 | BankSiteState | SITE_STATE | — | — |
| 30 | BankSiteZip | SITE_ZIP | — | — |
| 31 | BankStartDate | START_DATE | — | — |
| 32 | BankState | STATE | — | — |
| 33 | BankTaxRegistrationNumber | TAX_REGISTRATION_NUMBER | — | — |
| 34 | BankTaxpayerId | TAXPAYER_ID | — | — |
| 35 | BankZip | ZIP | — | — |

### [[ce_bank_branches_v|CE_BANK_BRANCHES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankBranchAddressLine1 | ADDRESS_LINE1 | — | — |
| 2 | BankBranchAddressLine2 | ADDRESS_LINE2 | — | — |
| 3 | BankBranchAddressLine3 | ADDRESS_LINE3 | — | — |
| 4 | BankBranchAddressLine4 | ADDRESS_LINE4 | — | — |
| 5 | BankBranchBankBranchName | BANK_BRANCH_NAME | — | ✅ |
| 6 | BankBranchBankBranchNameAlt | BANK_BRANCH_NAME_ALT | — | — |
| 7 | BankBranchBankBranchType | BANK_BRANCH_TYPE | — | — |
| 8 | BankBranchBankCode | BANK_CODE | — | — |
| 9 | BankBranchBankHomeCountry | BANK_HOME_COUNTRY | — | — |
| 10 | BankBranchBankInstitutionType | BANK_INSTITUTION_TYPE | — | — |
| 11 | BankBranchBankName | BANK_NAME | — | — |
| 12 | BankBranchBankNameAlt | BANK_NAME_ALT | — | — |
| 13 | BankBranchBankNumber | BANK_NUMBER | — | — |
| 14 | BankBranchBankPartyId | BANK_PARTY_ID | — | — |
| 15 | BankBranchBranchNumber | BRANCH_NUMBER | — | — |
| 16 | BankBranchBranchPartyId | BRANCH_PARTY_ID | — | — |
| 17 | BankBranchCity | CITY | — | — |
| 18 | BankBranchCountry | COUNTRY | — | — |
| 19 | BankBranchCountryName | COUNTRY_NAME | — | — |
| 20 | BankBranchDescription | DESCRIPTION | — | — |
| 21 | BankBranchEdiIdNumber | EDI_ID_NUMBER | — | — |
| 22 | BankBranchEdiLocation | EDI_LOCATION | — | — |
| 23 | BankBranchEftSwiftCode | EFT_SWIFT_CODE | — | — |
| 24 | BankBranchEftUserNumber | EFT_USER_NUMBER | — | — |
| 25 | BankBranchEndDate | END_DATE | — | — |
| 26 | BankBranchPkId | PK_ID | — | — |
| 27 | BankBranchProvince | PROVINCE | — | — |
| 28 | BankBranchRfc | RFC | — | — |
| 29 | BankBranchRowId | ROW_ID | — | — |
| 30 | BankBranchShortBankName | SHORT_BANK_NAME | — | — |
| 31 | BankBranchStartDate | START_DATE | — | — |
| 32 | BankBranchState | STATE | — | — |
| 33 | BankBranchZip | ZIP | — | — |

### [[ce_internal_bank_accts_v|CE_INTERNAL_BANK_ACCTS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankAccountAccountClassification | ACCOUNT_CLASSIFICATION | — | — |
| 2 | BankAccountAccountHolderId | ACCOUNT_HOLDER_ID | — | — |
| 3 | BankAccountAccountHolderName | ACCOUNT_HOLDER_NAME | — | ✅ |
| 4 | BankAccountAccountHolderNameAlt | ACCOUNT_HOLDER_NAME_ALT | — | — |
| 5 | BankAccountAccountOwnerOrgId | ACCOUNT_OWNER_ORG_ID | — | — |
| 6 | BankAccountAccountOwnerPartyId | ACCOUNT_OWNER_PARTY_ID | — | — |
| 7 | BankAccountAccountSuffix | ACCOUNT_SUFFIX | — | — |
| 8 | BankAccountAgencyLocationCode | AGENCY_LOCATION_CODE | — | — |
| 9 | BankAccountApUseAllowedFlag | AP_USE_ALLOWED_FLAG | — | ✅ |
| 10 | BankAccountArUseAllowedFlag | AR_USE_ALLOWED_FLAG | — | ✅ |
| 11 | BankAccountAssetCodeCombinationId | ASSET_CODE_COMBINATION_ID | — | — |
| 12 | BankAccountBankAccountName | BANK_ACCOUNT_NAME | — | ✅ |
| 13 | BankAccountBankAccountNameAlt | BANK_ACCOUNT_NAME_ALT | — | ✅ |
| 14 | BankAccountBankAccountNum | BANK_ACCOUNT_NUM | — | ✅ |
| 15 | BankAccountBankAccountNumElectronic | BANK_ACCOUNT_NUM_ELECTRONIC | — | — |
| 16 | BankAccountBankAccountType | BANK_ACCOUNT_TYPE | — | ✅ |
| 17 | BankAccountBankBranchId | BANK_BRANCH_ID | — | — |
| 18 | BankAccountBankChargesCcid | BANK_CHARGES_CCID | — | — |
| 19 | BankAccountBankExchangeRateType | BANK_EXCHANGE_RATE_TYPE | — | — |
| 20 | BankAccountBankId | BANK_ID | — | — |
| 21 | BankAccountCashClearingCcid | CASH_CLEARING_CCID | — | — |
| 22 | BankAccountCashflowDisplayOrder | CASHFLOW_DISPLAY_ORDER | — | — |
| 23 | BankAccountCashpoolMinPaymentAmt | CASHPOOL_MIN_PAYMENT_AMT | — | — |
| 24 | BankAccountCashpoolMinReceiptAmt | CASHPOOL_MIN_RECEIPT_AMT | — | — |
| 25 | BankAccountCashpoolRoundFactor | CASHPOOL_ROUND_FACTOR | — | — |
| 26 | BankAccountCashpoolRoundRule | CASHPOOL_ROUND_RULE | — | — |
| 27 | BankAccountCheckDigits | CHECK_DIGITS | — | — |
| 28 | BankAccountCreatedBy | CREATED_BY | — | ✅ |
| 29 | BankAccountCreationDate | CREATION_DATE | — | ✅ |
| 30 | BankAccountCurrencyCode | CURRENCY_CODE | — | ✅ |
| 31 | BankAccountDataSecurityFlag | DATA_SECURITY_FLAG | — | — |
| 32 | BankAccountDescription | DESCRIPTION | — | ✅ |
| 33 | BankAccountDescriptionCode1 | DESCRIPTION_CODE1 | — | — |
| 34 | BankAccountDescriptionCode2 | DESCRIPTION_CODE2 | — | — |
| 35 | BankAccountEftRequesterIdentifier | EFT_REQUESTER_IDENTIFIER | — | — |
| 36 | BankAccountEftUserNum | EFT_USER_NUM | — | — |
| 37 | BankAccountEndDate | END_DATE | — | ✅ |
| 38 | BankAccountFxChargeCcid | FX_CHARGE_CCID | — | — |
| 39 | BankAccountGlCurExcRateType | GL_CUR_EXC_RATE_TYPE | — | ✅ |
| 40 | BankAccountIbanNumber | IBAN_NUMBER | — | — |
| 41 | BankAccountId | BANK_ACCOUNT_ID | 🔑 | ✅ |
| 42 | BankAccountInterestScheduleId | INTEREST_SCHEDULE_ID | — | — |
| 43 | BankAccountLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 44 | BankAccountLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 45 | BankAccountLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 46 | BankAccountManualToleranceRuleId | MANUAL_TOLERANCE_RULE_ID | — | — |
| 47 | BankAccountMaskedAccountNum | MASKED_ACCOUNT_NUM | — | ✅ |
| 48 | BankAccountMaskedIban | MASKED_IBAN | — | ✅ |
| 49 | BankAccountMaxCheckAmount | MAX_CHECK_AMOUNT | — | — |
| 50 | BankAccountMaxOutlay | MAX_OUTLAY | — | — |
| 51 | BankAccountMaxTargetBalance | MAX_TARGET_BALANCE | — | — |
| 52 | BankAccountMinCheckAmount | MIN_CHECK_AMOUNT | — | — |
| 53 | BankAccountMinTargetBalance | MIN_TARGET_BALANCE | — | — |
| 54 | BankAccountMultiCurrencyAllowedFlag | MULTI_CURRENCY_ALLOWED_FLAG | — | — |
| 55 | BankAccountNettingAcctFlag | NETTING_ACCT_FLAG | — | — |
| 56 | BankAccountObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 57 | BankAccountParsingRuleSetId | PARSING_RULE_SET_ID | — | — |
| 58 | BankAccountPayUseAllowedFlag | PAY_USE_ALLOWED_FLAG | — | ✅ |
| 59 | BankAccountPoolBankChargeBearerCode | POOL_BANK_CHARGE_BEARER_CODE | — | — |
| 60 | BankAccountPoolPaymentMethodCode | POOL_PAYMENT_METHOD_CODE | — | — |
| 61 | BankAccountPoolPaymentReasonCode | POOL_PAYMENT_REASON_CODE | — | — |
| 62 | BankAccountPoolPaymentReasonComments | POOL_PAYMENT_REASON_COMMENTS | — | — |
| 63 | BankAccountPoolRemittanceMessage1 | POOL_REMITTANCE_MESSAGE1 | — | — |
| 64 | BankAccountPoolRemittanceMessage2 | POOL_REMITTANCE_MESSAGE2 | — | — |
| 65 | BankAccountPoolRemittanceMessage3 | POOL_REMITTANCE_MESSAGE3 | — | — |
| 66 | BankAccountPooledFlag | POOLED_FLAG | — | — |
| 67 | BankAccountProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 68 | BankAccountProgramId | PROGRAM_ID | — | — |
| 69 | BankAccountProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 70 | BankAccountReconDifferenceCcid | RECON_DIFFERENCE_CCID | — | — |
| 71 | BankAccountReconForBankXrateDateType | RECON_FOR_BANK_XRATE_DATE_TYPE | — | — |
| 72 | BankAccountReconForeignBankXrateType | RECON_FOREIGN_BANK_XRATE_TYPE | — | — |
| 73 | BankAccountReconRulesetId | RECON_RULESET_ID | — | — |
| 74 | BankAccountReconStartDate | RECON_START_DATE | — | — |
| 75 | BankAccountRequestId | REQUEST_ID | — | — |
| 76 | BankAccountSecondaryAccountReference | SECONDARY_ACCOUNT_REFERENCE | — | — |
| 77 | BankAccountShortAccountName | SHORT_ACCOUNT_NAME | — | ✅ |
| 78 | BankAccountStartDate | START_DATE | — | ✅ |
| 79 | BankAccountXtrBankAccountReference | XTR_BANK_ACCOUNT_REFERENCE | — | — |
| 80 | BankAccountXtrUseAllowedFlag | XTR_USE_ALLOWED_FLAG | — | — |
| 81 | BankAccountZeroAmountAllowed | ZERO_AMOUNT_ALLOWED | — | — |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankExcRateTypeConversionType | CONVERSION_TYPE | — | — |
| 2 | BankExcRateTypeCreatedBy | CREATED_BY | — | — |
| 3 | BankExcRateTypeCreationDate | CREATION_DATE | — | — |
| 4 | BankExcRateTypeDescription | DESCRIPTION | — | — |
| 5 | BankExcRateTypeEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 6 | BankExcRateTypeEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 7 | BankExcRateTypeFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 8 | BankExcRateTypeFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 9 | BankExcRateTypeFemScenario | FEM_SCENARIO | — | — |
| 10 | BankExcRateTypeFemTimeframe | FEM_TIMEFRAME | — | — |
| 11 | BankExcRateTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | BankExcRateTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | BankExcRateTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | BankExcRateTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | BankExcRateTypePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 16 | BankExcRateTypeSecurityFlag | SECURITY_FLAG | — | — |
| 17 | BankExcRateTypeUserConversionType | USER_CONVERSION_TYPE | — | — |
| 18 | BankExcRateTypeUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |
| 19 | GlCurExcRateTypeConversionType | CONVERSION_TYPE | — | — |
| 20 | GlCurExcRateTypeCreatedBy | CREATED_BY | — | — |
| 21 | GlCurExcRateTypeCreationDate | CREATION_DATE | — | — |
| 22 | GlCurExcRateTypeDescription | DESCRIPTION | — | — |
| 23 | GlCurExcRateTypeEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 24 | GlCurExcRateTypeEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 25 | GlCurExcRateTypeFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 26 | GlCurExcRateTypeFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 27 | GlCurExcRateTypeFemScenario | FEM_SCENARIO | — | — |
| 28 | GlCurExcRateTypeFemTimeframe | FEM_TIMEFRAME | — | — |
| 29 | GlCurExcRateTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | GlCurExcRateTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 31 | GlCurExcRateTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 32 | GlCurExcRateTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 33 | GlCurExcRateTypePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 34 | GlCurExcRateTypeSecurityFlag | SECURITY_FLAG | — | — |
| 35 | GlCurExcRateTypeUserConversionType | USER_CONVERSION_TYPE | — | — |
| 36 | GlCurExcRateTypeUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |
| 37 | ReconFrnBankXrateDateTypeConversionType | CONVERSION_TYPE | — | — |
| 38 | ReconFrnBankXrateDateTypeCreatedBy | CREATED_BY | — | — |
| 39 | ReconFrnBankXrateDateTypeCreationDate | CREATION_DATE | — | — |
| 40 | ReconFrnBankXrateDateTypeDescription | DESCRIPTION | — | — |
| 41 | ReconFrnBankXrateDateTypeEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 42 | ReconFrnBankXrateDateTypeEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 43 | ReconFrnBankXrateDateTypeFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 44 | ReconFrnBankXrateDateTypeFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 45 | ReconFrnBankXrateDateTypeFemScenario | FEM_SCENARIO | — | — |
| 46 | ReconFrnBankXrateDateTypeFemTimeframe | FEM_TIMEFRAME | — | — |
| 47 | ReconFrnBankXrateDateTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 48 | ReconFrnBankXrateDateTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 49 | ReconFrnBankXrateDateTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 50 | ReconFrnBankXrateDateTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 51 | ReconFrnBankXrateDateTypePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 52 | ReconFrnBankXrateDateTypeSecurityFlag | SECURITY_FLAG | — | — |
| 53 | ReconFrnBankXrateDateTypeUserConversionType | USER_CONVERSION_TYPE | — | — |
| 54 | ReconFrnBankXrateDateTypeUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |
| 55 | ReconFrnBankXrateTypeConversionType | CONVERSION_TYPE | — | — |
| 56 | ReconFrnBankXrateTypeCreatedBy | CREATED_BY | — | — |
| 57 | ReconFrnBankXrateTypeCreationDate | CREATION_DATE | — | — |
| 58 | ReconFrnBankXrateTypeDescription | DESCRIPTION | — | — |
| 59 | ReconFrnBankXrateTypeEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 60 | ReconFrnBankXrateTypeEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 61 | ReconFrnBankXrateTypeFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 62 | ReconFrnBankXrateTypeFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 63 | ReconFrnBankXrateTypeFemScenario | FEM_SCENARIO | — | — |
| 64 | ReconFrnBankXrateTypeFemTimeframe | FEM_TIMEFRAME | — | — |
| 65 | ReconFrnBankXrateTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 66 | ReconFrnBankXrateTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 67 | ReconFrnBankXrateTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 68 | ReconFrnBankXrateTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 69 | ReconFrnBankXrateTypePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 70 | ReconFrnBankXrateTypeSecurityFlag | SECURITY_FLAG | — | — |
| 71 | ReconFrnBankXrateTypeUserConversionType | USER_CONVERSION_TYPE | — | — |
| 72 | ReconFrnBankXrateTypeUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
