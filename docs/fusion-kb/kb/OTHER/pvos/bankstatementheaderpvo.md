---
id: DOC-OTHER-PVO-BankStatementHeaderPVO
doc_type: system-doc
title: "BankStatementHeaderPVO — PVO Cross-Module"
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
  - BankStatementHeaderPVO
  - bankstatementheaderpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BankStatementHeaderPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Bank Statement Header. Acessa as tabelas: CE_INTERNAL_BANK_ACCTS_V, CE_STATEMENT_HEADERS, PER_PERSON_NAMES_F_V (+1).

**Caminho:** `FscmTopModelAM.FinCeBankStatementsAM.BankStatementHeaderPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 122 | 4 | 1 | 18 | 15% |

---

## 🔗 Tabelas Relacionadas

- [[ce_internal_bank_accts_v|CE_INTERNAL_BANK_ACCTS_V]] — 81 atributos (1 BICC)
- [[ce_statement_headers|CE_STATEMENT_HEADERS]] — 21 atributos (1 PKs, 15 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (2 BICC)
- [[per_users|PER_USERS]] — 10 atributos

---

## ⚙️ Atributos

### [[ce_internal_bank_accts_v|CE_INTERNAL_BANK_ACCTS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankAccountAccountClassification | ACCOUNT_CLASSIFICATION | — | — |
| 2 | BankAccountAccountHolderId | ACCOUNT_HOLDER_ID | — | — |
| 3 | BankAccountAccountHolderName | ACCOUNT_HOLDER_NAME | — | — |
| 4 | BankAccountAccountHolderNameAlt | ACCOUNT_HOLDER_NAME_ALT | — | — |
| 5 | BankAccountAccountOwnerOrgId | ACCOUNT_OWNER_ORG_ID | — | — |
| 6 | BankAccountAccountOwnerPartyId | ACCOUNT_OWNER_PARTY_ID | — | — |
| 7 | BankAccountAccountSuffix | ACCOUNT_SUFFIX | — | — |
| 8 | BankAccountAgencyLocationCode | AGENCY_LOCATION_CODE | — | — |
| 9 | BankAccountApUseAllowedFlag | AP_USE_ALLOWED_FLAG | — | — |
| 10 | BankAccountArUseAllowedFlag | AR_USE_ALLOWED_FLAG | — | — |
| 11 | BankAccountAssetCodeCombinationId | ASSET_CODE_COMBINATION_ID | — | — |
| 12 | BankAccountBankAccountId | BANK_ACCOUNT_ID | — | — |
| 13 | BankAccountBankAccountName | BANK_ACCOUNT_NAME | — | — |
| 14 | BankAccountBankAccountNameAlt | BANK_ACCOUNT_NAME_ALT | — | — |
| 15 | BankAccountBankAccountNum | BANK_ACCOUNT_NUM | — | — |
| 16 | BankAccountBankAccountNumElectronic | BANK_ACCOUNT_NUM_ELECTRONIC | — | — |
| 17 | BankAccountBankAccountType | BANK_ACCOUNT_TYPE | — | — |
| 18 | BankAccountBankBranchId | BANK_BRANCH_ID | — | — |
| 19 | BankAccountBankChargesCcid | BANK_CHARGES_CCID | — | — |
| 20 | BankAccountBankExchangeRateType | BANK_EXCHANGE_RATE_TYPE | — | — |
| 21 | BankAccountBankId | BANK_ID | — | — |
| 22 | BankAccountCashClearingCcid | CASH_CLEARING_CCID | — | — |
| 23 | BankAccountCashflowDisplayOrder | CASHFLOW_DISPLAY_ORDER | — | — |
| 24 | BankAccountCashpoolMinPaymentAmt | CASHPOOL_MIN_PAYMENT_AMT | — | — |
| 25 | BankAccountCashpoolMinReceiptAmt | CASHPOOL_MIN_RECEIPT_AMT | — | — |
| 26 | BankAccountCashpoolRoundFactor | CASHPOOL_ROUND_FACTOR | — | — |
| 27 | BankAccountCashpoolRoundRule | CASHPOOL_ROUND_RULE | — | — |
| 28 | BankAccountCheckDigits | CHECK_DIGITS | — | — |
| 29 | BankAccountCreatedBy | CREATED_BY | — | — |
| 30 | BankAccountCreationDate | CREATION_DATE | — | — |
| 31 | BankAccountCurrencyCode | CURRENCY_CODE | — | — |
| 32 | BankAccountDataSecurityFlag | DATA_SECURITY_FLAG | — | — |
| 33 | BankAccountDescription | DESCRIPTION | — | — |
| 34 | BankAccountDescriptionCode1 | DESCRIPTION_CODE1 | — | — |
| 35 | BankAccountDescriptionCode2 | DESCRIPTION_CODE2 | — | — |
| 36 | BankAccountEftRequesterIdentifier | EFT_REQUESTER_IDENTIFIER | — | — |
| 37 | BankAccountEftUserNum | EFT_USER_NUM | — | — |
| 38 | BankAccountEndDate | END_DATE | — | — |
| 39 | BankAccountFxChargeCcid | FX_CHARGE_CCID | — | — |
| 40 | BankAccountGlCurExcRateType | GL_CUR_EXC_RATE_TYPE | — | — |
| 41 | BankAccountIbanNumber | IBAN_NUMBER | — | — |
| 42 | BankAccountInterestScheduleId | INTEREST_SCHEDULE_ID | — | — |
| 43 | BankAccountLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 44 | BankAccountLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 45 | BankAccountLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 46 | BankAccountManualToleranceRuleId | MANUAL_TOLERANCE_RULE_ID | — | — |
| 47 | BankAccountMaskedAccountNum | MASKED_ACCOUNT_NUM | — | — |
| 48 | BankAccountMaskedIban | MASKED_IBAN | — | — |
| 49 | BankAccountMaxCheckAmount | MAX_CHECK_AMOUNT | — | — |
| 50 | BankAccountMaxOutlay | MAX_OUTLAY | — | — |
| 51 | BankAccountMaxTargetBalance | MAX_TARGET_BALANCE | — | — |
| 52 | BankAccountMinCheckAmount | MIN_CHECK_AMOUNT | — | — |
| 53 | BankAccountMinTargetBalance | MIN_TARGET_BALANCE | — | — |
| 54 | BankAccountMultiCurrencyAllowedFlag | MULTI_CURRENCY_ALLOWED_FLAG | — | — |
| 55 | BankAccountNettingAcctFlag | NETTING_ACCT_FLAG | — | — |
| 56 | BankAccountObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 57 | BankAccountParsingRuleSetId | PARSING_RULE_SET_ID | — | — |
| 58 | BankAccountPayUseAllowedFlag | PAY_USE_ALLOWED_FLAG | — | — |
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
| 77 | BankAccountShortAccountName | SHORT_ACCOUNT_NAME | — | — |
| 78 | BankAccountStartDate | START_DATE | — | — |
| 79 | BankAccountXtrBankAccountReference | XTR_BANK_ACCOUNT_REFERENCE | — | — |
| 80 | BankAccountXtrUseAllowedFlag | XTR_USE_ALLOWED_FLAG | — | — |
| 81 | BankAccountZeroAmountAllowed | ZERO_AMOUNT_ALLOWED | — | — |

### [[ce_statement_headers|CE_STATEMENT_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StatementHeaderAutorecProcessCode | AUTOREC_PROCESS_CODE | — | — |
| 2 | StatementHeaderAutorecProcessId | AUTOREC_PROCESS_ID | — | — |
| 3 | StatementHeaderBankAccountId | BANK_ACCOUNT_ID | — | — |
| 4 | StatementHeaderCreatedBy | CREATED_BY | — | ✅ |
| 5 | StatementHeaderCreationDate | CREATION_DATE | — | ✅ |
| 6 | StatementHeaderCurrencyCode | CURRENCY_CODE | — | ✅ |
| 7 | StatementHeaderElectronicSeqNum | ELECTRONIC_SEQ_NUM | — | ✅ |
| 8 | StatementHeaderId | STATEMENT_HEADER_ID | 🔑 | ✅ |
| 9 | StatementHeaderInboundFileId | INBOUND_FILE_ID | — | — |
| 10 | StatementHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | StatementHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | StatementHeaderLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | StatementHeaderLegalSeqNum | LEGAL_SEQ_NUM | — | ✅ |
| 14 | StatementHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | StatementHeaderReconStatusCode | RECON_STATUS_CODE | — | ✅ |
| 16 | StatementHeaderStatementDate | STATEMENT_DATE | — | ✅ |
| 17 | StatementHeaderStatementEntryType | STATEMENT_ENTRY_TYPE | — | ✅ |
| 18 | StatementHeaderStatementNumber | STATEMENT_NUMBER | — | ✅ |
| 19 | StatementHeaderStatementType | STATEMENT_TYPE | — | ✅ |
| 20 | StatementHeaderStmtFromDate | STMT_FROM_DATE | — | ✅ |
| 21 | StatementHeaderStmtToDate | STMT_TO_DATE | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | PersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 3 | UserCreatedByPersonId | PERSON_ID | — | — |
| 4 | UserCreatedByUserGuid | USER_GUID | — | — |
| 5 | UserCreatedByUserId | USER_ID | — | — |
| 6 | UserCreatedByUsername | USERNAME | — | — |
| 7 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 8 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 9 | UserUpdatedByUserId | USER_ID | — | — |
| 10 | UserUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
