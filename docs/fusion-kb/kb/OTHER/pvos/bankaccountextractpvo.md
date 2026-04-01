---
id: DOC-OTHER-PVO-BankAccountExtractPVO
doc_type: system-doc
title: "BankAccountExtractPVO — PVO Cross-Module"
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
  - BankAccountExtractPVO
  - bankaccountextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BankAccountExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Bank Account Extract. Acessa as tabelas: CE_BANK_ACCOUNTS.

**Caminho:** `FscmTopModelAM.FinExtractAM.CeBiccExtractAM.BankAccountExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 115 | 1 | 1 | 59 | 51% |

---

## 🔗 Tabelas Relacionadas

- [[ce_bank_accounts|CE_BANK_ACCOUNTS]] — 115 atributos (1 PKs, 59 BICC)

---

## ⚙️ Atributos

### [[ce_bank_accounts|CE_BANK_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankAccountReportPEOAccountClassification | ACCOUNT_CLASSIFICATION | — | ✅ |
| 2 | BankAccountReportPEOAccountHolderId | ACCOUNT_HOLDER_ID | — | ✅ |
| 3 | BankAccountReportPEOAccountHolderName | ACCOUNT_HOLDER_NAME | — | ✅ |
| 4 | BankAccountReportPEOAccountHolderNameAlt | ACCOUNT_HOLDER_NAME_ALT | — | ✅ |
| 5 | BankAccountReportPEOAccountOwnerOrgId | ACCOUNT_OWNER_ORG_ID | — | ✅ |
| 6 | BankAccountReportPEOAccountOwnerPartyId | ACCOUNT_OWNER_PARTY_ID | — | ✅ |
| 7 | BankAccountReportPEOAccountSuffix | ACCOUNT_SUFFIX | — | ✅ |
| 8 | BankAccountReportPEOAgencyLocationCode | AGENCY_LOCATION_CODE | — | ✅ |
| 9 | BankAccountReportPEOApUseAllowedFlag | AP_USE_ALLOWED_FLAG | — | ✅ |
| 10 | BankAccountReportPEOArUseAllowedFlag | AR_USE_ALLOWED_FLAG | — | ✅ |
| 11 | BankAccountReportPEOAssetCodeCombinationId | ASSET_CODE_COMBINATION_ID | — | ✅ |
| 12 | BankAccountReportPEOAttribute1 | ATTRIBUTE1 | — | — |
| 13 | BankAccountReportPEOAttribute10 | ATTRIBUTE10 | — | — |
| 14 | BankAccountReportPEOAttribute11 | ATTRIBUTE11 | — | — |
| 15 | BankAccountReportPEOAttribute12 | ATTRIBUTE12 | — | — |
| 16 | BankAccountReportPEOAttribute13 | ATTRIBUTE13 | — | — |
| 17 | BankAccountReportPEOAttribute14 | ATTRIBUTE14 | — | — |
| 18 | BankAccountReportPEOAttribute15 | ATTRIBUTE15 | — | — |
| 19 | BankAccountReportPEOAttribute2 | ATTRIBUTE2 | — | — |
| 20 | BankAccountReportPEOAttribute3 | ATTRIBUTE3 | — | — |
| 21 | BankAccountReportPEOAttribute4 | ATTRIBUTE4 | — | — |
| 22 | BankAccountReportPEOAttribute5 | ATTRIBUTE5 | — | — |
| 23 | BankAccountReportPEOAttribute6 | ATTRIBUTE6 | — | — |
| 24 | BankAccountReportPEOAttribute7 | ATTRIBUTE7 | — | — |
| 25 | BankAccountReportPEOAttribute8 | ATTRIBUTE8 | — | — |
| 26 | BankAccountReportPEOAttribute9 | ATTRIBUTE9 | — | — |
| 27 | BankAccountReportPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 28 | BankAccountReportPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 29 | BankAccountReportPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 30 | BankAccountReportPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 31 | BankAccountReportPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 32 | BankAccountReportPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 33 | BankAccountReportPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 34 | BankAccountReportPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 35 | BankAccountReportPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 36 | BankAccountReportPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 37 | BankAccountReportPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 38 | BankAccountReportPEOBankAccountId | BANK_ACCOUNT_ID | 🔑 | ✅ |
| 39 | BankAccountReportPEOBankAccountName | BANK_ACCOUNT_NAME | — | ✅ |
| 40 | BankAccountReportPEOBankAccountNameAlt | BANK_ACCOUNT_NAME_ALT | — | ✅ |
| 41 | BankAccountReportPEOBankAccountNum | BANK_ACCOUNT_NUM | — | ✅ |
| 42 | BankAccountReportPEOBankAccountNumElectronic | BANK_ACCOUNT_NUM_ELECTRONIC | — | ✅ |
| 43 | BankAccountReportPEOBankAccountType | BANK_ACCOUNT_TYPE | — | ✅ |
| 44 | BankAccountReportPEOBankBranchId | BANK_BRANCH_ID | — | ✅ |
| 45 | BankAccountReportPEOBankExchangeRateType | BANK_EXCHANGE_RATE_TYPE | — | ✅ |
| 46 | BankAccountReportPEOBankId | BANK_ID | — | ✅ |
| 47 | BankAccountReportPEOCashCcidFixedSegments | CASH_CCID_FIXED_SEGMENTS | — | ✅ |
| 48 | BankAccountReportPEOCashClearingCcid | CASH_CLEARING_CCID | — | ✅ |
| 49 | BankAccountReportPEOCheckDigits | CHECK_DIGITS | — | ✅ |
| 50 | BankAccountReportPEOCreatedBy | CREATED_BY | — | ✅ |
| 51 | BankAccountReportPEOCreationDate | CREATION_DATE | — | ✅ |
| 52 | BankAccountReportPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 53 | BankAccountReportPEODataSecurityFlag | DATA_SECURITY_FLAG | — | ✅ |
| 54 | BankAccountReportPEODescription | DESCRIPTION | — | ✅ |
| 55 | BankAccountReportPEOEftUserNum | EFT_USER_NUM | — | ✅ |
| 56 | BankAccountReportPEOEndDate | END_DATE | — | ✅ |
| 57 | BankAccountReportPEOGlCurExcRateType | GL_CUR_EXC_RATE_TYPE | — | ✅ |
| 58 | BankAccountReportPEOGlReconStartDate | GL_RECON_START_DATE | — | ✅ |
| 59 | BankAccountReportPEOGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 60 | BankAccountReportPEOGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 61 | BankAccountReportPEOGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 62 | BankAccountReportPEOGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 63 | BankAccountReportPEOGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 64 | BankAccountReportPEOGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 65 | BankAccountReportPEOGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 66 | BankAccountReportPEOGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | ✅ |
| 67 | BankAccountReportPEOGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 68 | BankAccountReportPEOGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 69 | BankAccountReportPEOGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 70 | BankAccountReportPEOGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 71 | BankAccountReportPEOGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 72 | BankAccountReportPEOGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 73 | BankAccountReportPEOGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 74 | BankAccountReportPEOGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 75 | BankAccountReportPEOGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 76 | BankAccountReportPEOGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 77 | BankAccountReportPEOGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 78 | BankAccountReportPEOGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 79 | BankAccountReportPEOGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 80 | BankAccountReportPEOGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 81 | BankAccountReportPEOGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 82 | BankAccountReportPEOGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 83 | BankAccountReportPEOGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 84 | BankAccountReportPEOGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 85 | BankAccountReportPEOGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 86 | BankAccountReportPEOGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 87 | BankAccountReportPEOGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 88 | BankAccountReportPEOGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 89 | BankAccountReportPEOGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 90 | BankAccountReportPEOIbanNumber | IBAN_NUMBER | — | ✅ |
| 91 | BankAccountReportPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 92 | BankAccountReportPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 93 | BankAccountReportPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 94 | BankAccountReportPEOManualToleranceRuleId | MANUAL_TOLERANCE_RULE_ID | — | ✅ |
| 95 | BankAccountReportPEOMaskedAccountNum | MASKED_ACCOUNT_NUM | — | ✅ |
| 96 | BankAccountReportPEOMaskedIban | MASKED_IBAN | — | ✅ |
| 97 | BankAccountReportPEOMaxCheckAmount | MAX_CHECK_AMOUNT | — | ✅ |
| 98 | BankAccountReportPEOMaxOutlay | MAX_OUTLAY | — | ✅ |
| 99 | BankAccountReportPEOMinCheckAmount | MIN_CHECK_AMOUNT | — | ✅ |
| 100 | BankAccountReportPEOMultiCashReconEnabledFlag | MULTI_CASH_RECON_ENABLED_FLAG | — | ✅ |
| 101 | BankAccountReportPEOMultiCurrencyAllowedFlag | MULTI_CURRENCY_ALLOWED_FLAG | — | ✅ |
| 102 | BankAccountReportPEONettingAcctFlag | NETTING_ACCT_FLAG | — | ✅ |
| 103 | BankAccountReportPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 104 | BankAccountReportPEOParsingRuleSetId | PARSING_RULE_SET_ID | — | ✅ |
| 105 | BankAccountReportPEOPayUseAllowedFlag | PAY_USE_ALLOWED_FLAG | — | ✅ |
| 106 | BankAccountReportPEOPooledFlag | POOLED_FLAG | — | ✅ |
| 107 | BankAccountReportPEOReconDifferenceCcid | RECON_DIFFERENCE_CCID | — | ✅ |
| 108 | BankAccountReportPEOReconRulesetId | RECON_RULESET_ID | — | ✅ |
| 109 | BankAccountReportPEOReconStartDate | RECON_START_DATE | — | ✅ |
| 110 | BankAccountReportPEOReversalProcessCode | REVERSAL_PROCESS_CODE | — | ✅ |
| 111 | BankAccountReportPEOSecondaryAccountReference | SECONDARY_ACCOUNT_REFERENCE | — | ✅ |
| 112 | BankAccountReportPEOStartDate | START_DATE | — | ✅ |
| 113 | BankAccountReportPEOTargetBalance | TARGET_BALANCE | — | ✅ |
| 114 | BankAccountReportPEOTransactionCalendarId | TRANSACTION_CALENDAR_ID | — | ✅ |
| 115 | BankAccountReportPEOZeroAmountAllowed | ZERO_AMOUNT_ALLOWED | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
