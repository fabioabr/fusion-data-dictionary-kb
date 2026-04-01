---
id: DOC-HCM-513
doc_type: system-doc
title: "IBY_EXT_BANK_ACCOUNTS — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - IBY_EXT_BANK_ACCOUNTS
  - iby_ext_bank_accounts
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# IBY_EXT_BANK_ACCOUNTS

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACCOUNT_CLASSIFICATION | — | — | — | — | — | — |
| 2 | ACCOUNT_SUFFIX | — | — | — | — | — | — |
| 3 | AGENCY_LOCATION_CODE | — | — | — | — | — | — |
| 4 | BANK_ACCOUNT_NAME | — | — | — | — | — | — |
| 5 | BANK_ACCOUNT_NAME_ALT | — | — | — | — | — | — |
| 6 | BANK_ACCOUNT_NUM | — | — | — | — | — | — |
| 7 | BANK_ACCOUNT_NUM_ELECTRONIC | — | — | — | — | — | — |
| 8 | BANK_ACCOUNT_NUM_HASH1 | — | — | — | — | — | — |
| 9 | BANK_ACCOUNT_NUM_HASH2 | — | — | — | — | — | — |
| 10 | BANK_ACCOUNT_TYPE | — | — | — | — | — | — |
| 11 | BANK_BRANCH_PARTY_FLAG | — | — | — | — | — | — |
| 12 | BANK_ID | — | — | — | — | — | — |
| 13 | BA_MASK_SETTING | — | — | — | — | — | — |
| 14 | BA_NUM_ELEC_SEC_SEGMENT_ID | — | — | — | — | — | — |
| 15 | BA_NUM_SEC_SEGMENT_ID | — | — | — | — | — | — |
| 16 | BA_UNMASK_LENGTH | — | — | — | — | — | — |
| 17 | BRANCH_ID | — | — | — | — | — | — |
| 18 | BRANCH_NUMBER | — | — | — | — | — | — |
| 19 | CHECK_DIGITS | — | — | — | — | — | — |
| 20 | COUNTRY_CODE | — | — | — | — | — | — |
| 21 | CREATED_BY | — | — | — | — | — | — |
| 22 | CREATION_DATE | — | — | — | — | — | — |
| 23 | CURRENCY_CODE | — | — | — | — | — | — |
| 24 | DESCRIPTION | — | — | — | — | — | — |
| 25 | EFT_SWIFT_CODE | — | — | — | — | — | — |
| 26 | ENCRYPTED | — | — | — | — | — | — |
| 27 | END_DATE | — | — | — | — | — | — |
| 28 | EXCHANGE_RATE | — | — | — | — | — | — |
| 29 | EXCHANGE_RATE_AGREEMENT_NUM | — | — | — | — | — | — |
| 30 | EXCHANGE_RATE_AGREEMENT_TYPE | — | — | — | — | — | — |
| 31 | EXT_BANK_ACCOUNT_ID | — | — | — | — | — | — |
| 32 | FOREIGN_PAYMENT_USE_FLAG | — | — | — | — | — | — |
| 33 | HEDGING_CONTRACT_REFERENCE | — | — | — | — | — | — |
| 34 | IBAN | — | — | — | — | — | — |
| 35 | IBAN_HASH1 | — | — | — | — | — | — |
| 36 | IBAN_HASH2 | — | — | — | — | — | — |
| 37 | IBAN_SEC_SEGMENT_ID | — | — | — | — | — | — |
| 38 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 39 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 40 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 41 | MASKED_BANK_ACCOUNT_NUM | — | — | — | — | — | — |
| 42 | MASKED_IBAN | — | — | — | — | — | — |
| 43 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 44 | PAYMENT_FACTOR_FLAG | — | — | — | — | — | — |
| 45 | PROGRAM_APPLICATION_ID | — | — | — | — | — | — |
| 46 | PROGRAM_ID | — | — | — | — | — | — |
| 47 | PROGRAM_UPDATE_DATE | — | — | — | — | — | — |
| 48 | REQUEST_ID | — | — | — | — | — | — |
| 49 | SALT_VERSION | — | — | — | — | — | — |
| 50 | SECONDARY_ACCOUNT_REFERENCE | — | — | — | — | — | — |
| 51 | SHORT_ACCT_NAME | — | — | — | — | — | — |
| 52 | START_DATE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[accountbankaccount|AccountBankAccount]] (AR · BICC: 8/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASSIFICATION | BankAccountAccountClassification | — |
| ACCOUNT_SUFFIX | BankAccountAccountSuffix | — |
| AGENCY_LOCATION_CODE | BankAccountAgencyLocationCode | — |
| BA_MASK_SETTING | BankAccountBaMaskSetting | — |
| BA_NUM_ELEC_SEC_SEGMENT_ID | BankAccountBaNumElecSecSegmentId | — |
| BA_NUM_SEC_SEGMENT_ID | BankAccountBaNumSecSegmentId | — |
| BA_UNMASK_LENGTH | BankAccountBaUnmaskLength | — |
| BANK_ACCOUNT_NAME | BankAccountBankAccountName | ✅ |
| BANK_ACCOUNT_NAME_ALT | BankAccountBankAccountNameAlt | — |
| BANK_ACCOUNT_NUM | BankAccountBankAccountNum | — |
| BANK_ACCOUNT_NUM_ELECTRONIC | BankAccountBankAccountNumElectronic | — |
| BANK_ACCOUNT_TYPE | BankAccountBankAccountType | ✅ |
| BANK_ID | BankAccountBankId | — |
| BRANCH_ID | BankAccountBranchId | — |
| CHECK_DIGITS | BankAccountCheckDigits | ✅ |
| COUNTRY_CODE | BankAccountCountryCode | — |
| CREATED_BY | BankAccountCreatedBy | — |
| CREATION_DATE | BankAccountCreationDate | — |
| CURRENCY_CODE | BankAccountCurrencyCode | ✅ |
| DESCRIPTION | BankAccountDescription | ✅ |
| ENCRYPTED | BankAccountEncrypted | — |
| END_DATE | BankAccountEndDate | — |
| EXCHANGE_RATE | BankAccountExchangeRate | — |
| EXCHANGE_RATE_AGREEMENT_NUM | BankAccountExchangeRateAgreementNum | — |
| EXCHANGE_RATE_AGREEMENT_TYPE | BankAccountExchangeRateAgreementType | — |
| EXT_BANK_ACCOUNT_ID | BankAccountExtBankAccountId | — |
| FOREIGN_PAYMENT_USE_FLAG | BankAccountForeignPaymentUseFlag | — |
| HEDGING_CONTRACT_REFERENCE | BankAccountHedgingContractReference | — |
| IBAN | BankAccountIban | — |
| IBAN_HASH1 | BankAccountIbanHash1 | — |
| IBAN_SEC_SEGMENT_ID | BankAccountIbanSecSegmentId | — |
| LAST_UPDATE_DATE | BankAccountLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BankAccountLastUpdateLogin | — |
| LAST_UPDATED_BY | BankAccountLastUpdatedBy | — |
| MASKED_BANK_ACCOUNT_NUM | BankAccountMaskedBankAccountNum | ✅ |
| MASKED_IBAN | BankAccountMaskedIban | ✅ |
| OBJECT_VERSION_NUMBER | BankAccountObjectVersionNumber | — |
| PAYMENT_FACTOR_FLAG | BankAccountPaymentFactorFlag | — |
| PROGRAM_APPLICATION_ID | BankAccountProgramApplicationId | — |
| PROGRAM_ID | BankAccountProgramId | — |
| PROGRAM_UPDATE_DATE | BankAccountProgramUpdateDate | — |
| REQUEST_ID | BankAccountRequestId | — |
| SALT_VERSION | BankAccountSaltVersion | — |
| SECONDARY_ACCOUNT_REFERENCE | BankAccountSecondaryAccountReference | — |
| SHORT_ACCT_NAME | BankAccountShortAcctName | — |
| START_DATE | BankAccountStartDate | — |

### [[adjustmentdistributionpvo|AdjustmentDistributionPVO]] (AR · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BANK_ACCOUNT_NUM | ExternalBankAccountBankAccountNum | ✅ |
| EXT_BANK_ACCOUNT_ID | ExternalBankAccountExtBankAccountId | — |
| OBJECT_VERSION_NUMBER | ExternalBankAccountObjectVersionNumber12 | — |

### [[adjustmentpvo|AdjustmentPVO]] (AR · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BANK_ACCOUNT_NUM | ExternalBankAccountBankAccountNum | ✅ |
| EXT_BANK_ACCOUNT_ID | ExternalBankAccountExtBankAccountId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber2 | — |

### [[disbursementheaderpvo|DisbursementHeaderPVO]] (AP · BICC: 7/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BA_MASK_SETTING | ExtBnkAcctBaMaskSetting | — |
| BANK_ACCOUNT_NAME | ExtBnkAcctBankAccountName | ✅ |
| BANK_BRANCH_PARTY_FLAG | ExtBnkAcctBankBranchPartyFlag | — |
| BRANCH_NUMBER | ExtBnkAcctBranchNumber | ✅ |
| CHECK_DIGITS | ExtBnkAcctCheckDigits | ✅ |
| COUNTRY_CODE | ExtBnkAcctCountryCode | ✅ |
| DESCRIPTION | ExtBnkAcctDescription | ✅ |
| EFT_SWIFT_CODE | ExtBnkAcctSwiftCode | — |
| EXT_BANK_ACCOUNT_ID | ExtBnkAcctExtBankAccountId | — |
| IBAN | ExtBnkAcctIban | — |
| MASKED_BANK_ACCOUNT_NUM | ExtBnkAcctMaskedBankAccountNum | ✅ |
| MASKED_IBAN | ExtBnkAcctMaskedIban | — |
| SECONDARY_ACCOUNT_REFERENCE | ExtBnkAcctSecondaryAccountReference | ✅ |

### [[expensedistributionpvo|ExpenseDistributionPVO]] (OTHER · BICC: 1/49)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASSIFICATION | InvExtBnkAcctAccountClassification | — |
| ACCOUNT_SUFFIX | InvExtBnkAcctAccountSuffix | — |
| AGENCY_LOCATION_CODE | InvExtBnkAcctAgencyLocationCode | — |
| BA_MASK_SETTING | InvExtBnkAcctBaMaskSetting | — |
| BA_NUM_ELEC_SEC_SEGMENT_ID | InvExtBnkAcctBaNumElecSecSegmentId | — |
| BA_NUM_SEC_SEGMENT_ID | InvExtBnkAcctBaNumSecSegmentId | — |
| BA_UNMASK_LENGTH | InvExtBnkAcctBaUnmaskLength | — |
| BANK_ACCOUNT_NAME | InvExtBnkAcctBankAccountName | — |
| BANK_ACCOUNT_NAME_ALT | InvExtBnkAcctBankAccountNameAlt | — |
| BANK_ACCOUNT_NUM | InvExtBnkAcctBankAccountNum | — |
| BANK_ACCOUNT_NUM_ELECTRONIC | InvExtBnkAcctBankAccountNumElectronic | — |
| BANK_ACCOUNT_NUM_HASH1 | InvExtBnkAcctBankAccountNumHash1 | — |
| BANK_ACCOUNT_NUM_HASH2 | InvExtBnkAcctBankAccountNumHash2 | — |
| BANK_ACCOUNT_TYPE | InvExtBnkAcctBankAccountType | — |
| BANK_ID | InvExtBnkAcctBankId | — |
| BRANCH_ID | InvExtBnkAcctBranchId | — |
| CHECK_DIGITS | InvExtBnkAcctCheckDigits | — |
| COUNTRY_CODE | InvExtBnkAcctCountryCode | — |
| CREATED_BY | InvExtBnkAcctCreatedBy | — |
| CREATION_DATE | InvExtBnkAcctCreationDate | — |
| CURRENCY_CODE | InvExtBnkAcctCurrencyCode | — |
| DESCRIPTION | InvExtBnkAcctDescription | — |
| ENCRYPTED | InvExtBnkAcctEncrypted | — |
| END_DATE | InvExtBnkAcctEndDate | — |
| EXCHANGE_RATE | InvExtBnkAcctExchangeRate | — |
| EXCHANGE_RATE_AGREEMENT_NUM | InvExtBnkAcctExchangeRateAgreementNum | — |
| EXCHANGE_RATE_AGREEMENT_TYPE | InvExtBnkAcctExchangeRateAgreementType | — |
| EXT_BANK_ACCOUNT_ID | InvExtBnkAcctExtBankAccountId | — |
| FOREIGN_PAYMENT_USE_FLAG | InvExtBnkAcctForeignPaymentUseFlag | — |
| HEDGING_CONTRACT_REFERENCE | InvExtBnkAcctHedgingContractReference | — |
| IBAN | InvExtBnkAcctIban | — |
| IBAN_HASH1 | InvExtBnkAcctIbanHash1 | — |
| IBAN_HASH2 | InvExtBnkAcctIbanHash2 | — |
| IBAN_SEC_SEGMENT_ID | InvExtBnkAcctIbanSecSegmentId | — |
| LAST_UPDATE_DATE | InvExtBnkAcctLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InvExtBnkAcctLastUpdateLogin | — |
| LAST_UPDATED_BY | InvExtBnkAcctLastUpdatedBy | — |
| MASKED_BANK_ACCOUNT_NUM | InvExtBnkAcctMaskedBankAccountNum | — |
| MASKED_IBAN | InvExtBnkAcctMaskedIban | — |
| OBJECT_VERSION_NUMBER | InvExtBnkAcctObjectVersionNumber | — |
| PAYMENT_FACTOR_FLAG | InvExtBnkAcctPaymentFactorFlag | — |
| PROGRAM_APPLICATION_ID | InvExtBnkAcctProgramApplicationId | — |
| PROGRAM_ID | InvExtBnkAcctProgramId | — |
| PROGRAM_UPDATE_DATE | InvExtBnkAcctProgramUpdateDate | — |
| REQUEST_ID | InvExtBnkAcctRequestId | — |
| SALT_VERSION | InvExtBnkAcctSaltVersion | — |
| SECONDARY_ACCOUNT_REFERENCE | InvExtBnkAcctSecondaryAccountReference | — |
| SHORT_ACCT_NAME | InvExtBnkAcctShortAcctName | — |
| START_DATE | InvExtBnkAcctStartDate | — |

### [[headersalescreditpvo|HeaderSalesCreditPVO]] (AR · BICC: 2/44)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASSIFICATION | IbyExtBankAccountsAccountClassification | — |
| ACCOUNT_SUFFIX | IbyExtBankAccountsAccountSuffix | — |
| AGENCY_LOCATION_CODE | IbyExtBankAccountsAgencyLocationCode | — |
| BA_MASK_SETTING | IbyExtBankAccountsBaMaskSetting | — |
| BA_NUM_ELEC_SEC_SEGMENT_ID | IbyExtBankAccountsBaNumElecSecSegmentId | — |
| BA_NUM_SEC_SEGMENT_ID | IbyExtBankAccountsBaNumSecSegmentId | — |
| BA_UNMASK_LENGTH | IbyExtBankAccountsBaUnmaskLength | — |
| BANK_ACCOUNT_NAME | IbyExtBankAccountsBankAccountName | ✅ |
| BANK_ACCOUNT_NAME_ALT | IbyExtBankAccountsBankAccountNameAlt | — |
| BANK_ACCOUNT_NUM | IbyExtBankAccountsBankAccountNum | ✅ |
| BANK_ACCOUNT_NUM_ELECTRONIC | IbyExtBankAccountsBankAccountNumElectronic | — |
| BANK_ACCOUNT_NUM_HASH1 | IbyExtBankAccountsBankAccountNumHash1 | — |
| BANK_ACCOUNT_NUM_HASH2 | IbyExtBankAccountsBankAccountNumHash2 | — |
| BANK_ACCOUNT_TYPE | IbyExtBankAccountsBankAccountType | — |
| BANK_ID | IbyExtBankAccountsBankId | — |
| BRANCH_ID | IbyExtBankAccountsBranchId | — |
| CHECK_DIGITS | IbyExtBankAccountsCheckDigits | — |
| COUNTRY_CODE | IbyExtBankAccountsCountryCode | — |
| CURRENCY_CODE | IbyExtBankAccountsCurrencyCode | — |
| DESCRIPTION | IbyExtBankAccountsDescription | — |
| ENCRYPTED | IbyExtBankAccountsEncrypted | — |
| END_DATE | IbyExtBankAccountsEndDate | — |
| EXCHANGE_RATE | IbyExtBankAccountsExchangeRate | — |
| EXCHANGE_RATE_AGREEMENT_NUM | IbyExtBankAccountsExchangeRateAgreementNum | — |
| EXCHANGE_RATE_AGREEMENT_TYPE | IbyExtBankAccountsExchangeRateAgreementType | — |
| EXT_BANK_ACCOUNT_ID | IbyExtBankAccountsExtBankAccountId | — |
| FOREIGN_PAYMENT_USE_FLAG | IbyExtBankAccountsForeignPaymentUseFlag | — |
| HEDGING_CONTRACT_REFERENCE | IbyExtBankAccountsHedgingContractReference | — |
| IBAN | IbyExtBankAccountsIban | — |
| IBAN_HASH1 | IbyExtBankAccountsIbanHash1 | — |
| IBAN_HASH2 | IbyExtBankAccountsIbanHash2 | — |
| IBAN_SEC_SEGMENT_ID | IbyExtBankAccountsIbanSecSegmentId | — |
| MASKED_BANK_ACCOUNT_NUM | IbyExtBankAccountsMaskedBankAccountNum | — |
| MASKED_IBAN | IbyExtBankAccountsMaskedIban | — |
| OBJECT_VERSION_NUMBER | IbyExtBankAccountsObjectVersionNumber | — |
| PAYMENT_FACTOR_FLAG | IbyExtBankAccountsPaymentFactorFlag | — |
| PROGRAM_APPLICATION_ID | IbyExtBankAccountsProgramApplicationId | — |
| PROGRAM_ID | IbyExtBankAccountsProgramId | — |
| PROGRAM_UPDATE_DATE | IbyExtBankAccountsProgramUpdateDate | — |
| REQUEST_ID | IbyExtBankAccountsRequestId | — |
| SALT_VERSION | IbyExtBankAccountsSaltVersion | — |
| SECONDARY_ACCOUNT_REFERENCE | IbyExtBankAccountsSecondaryAccountReference | — |
| SHORT_ACCT_NAME | IbyExtBankAccountsShortAcctName | — |
| START_DATE | IbyExtBankAccountsStartDate | — |

### [[invoiceheaderpvo|InvoiceHeaderPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EXT_BANK_ACCOUNT_ID | InvExtBnkAcctExtBankAccountId | — |
| LAST_UPDATE_DATE | InvExtBnkAcctLastUpdateDate | — |

### [[invoicepaymentschedulepvo|InvoicePaymentSchedulePVO]] (AP · BICC: 3/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHECK_DIGITS | ExtBnkAcctCheckDigits | ✅ |
| EXT_BANK_ACCOUNT_ID | ExtBnkAcctExtBankAccountId | — |
| EXT_BANK_ACCOUNT_ID | InvExtBnkAcctExtBankAccountId | — |
| LAST_UPDATE_DATE | InvExtBnkAcctLastUpdateDate | ✅ |
| MASKED_BANK_ACCOUNT_NUM | ExtBnkAcctMaskedBankAccountNum | ✅ |
| OBJECT_VERSION_NUMBER | ExtBnkAcctObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | InvExtBnkAcctObjectVersionNumber | — |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR · BICC: 2/44)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASSIFICATION | IbyExtBankAccountsAccountClassification | — |
| ACCOUNT_SUFFIX | IbyExtBankAccountsAccountSuffix | — |
| AGENCY_LOCATION_CODE | IbyExtBankAccountsAgencyLocationCode | — |
| BA_MASK_SETTING | IbyExtBankAccountsBaMaskSetting | — |
| BA_NUM_ELEC_SEC_SEGMENT_ID | IbyExtBankAccountsBaNumElecSecSegmentId | — |
| BA_NUM_SEC_SEGMENT_ID | IbyExtBankAccountsBaNumSecSegmentId | — |
| BA_UNMASK_LENGTH | IbyExtBankAccountsBaUnmaskLength | — |
| BANK_ACCOUNT_NAME | IbyExtBankAccountsBankAccountName | ✅ |
| BANK_ACCOUNT_NAME_ALT | IbyExtBankAccountsBankAccountNameAlt | — |
| BANK_ACCOUNT_NUM | IbyExtBankAccountsBankAccountNum | ✅ |
| BANK_ACCOUNT_NUM_ELECTRONIC | IbyExtBankAccountsBankAccountNumElectronic | — |
| BANK_ACCOUNT_NUM_HASH1 | IbyExtBankAccountsBankAccountNumHash1 | — |
| BANK_ACCOUNT_NUM_HASH2 | IbyExtBankAccountsBankAccountNumHash2 | — |
| BANK_ACCOUNT_TYPE | IbyExtBankAccountsBankAccountType | — |
| BANK_ID | IbyExtBankAccountsBankId | — |
| BRANCH_ID | IbyExtBankAccountsBranchId | — |
| CHECK_DIGITS | IbyExtBankAccountsCheckDigits | — |
| COUNTRY_CODE | IbyExtBankAccountsCountryCode | — |
| CURRENCY_CODE | IbyExtBankAccountsCurrencyCode | — |
| DESCRIPTION | IbyExtBankAccountsDescription | — |
| ENCRYPTED | IbyExtBankAccountsEncrypted | — |
| END_DATE | IbyExtBankAccountsEndDate | — |
| EXCHANGE_RATE | IbyExtBankAccountsExchangeRate | — |
| EXCHANGE_RATE_AGREEMENT_NUM | IbyExtBankAccountsExchangeRateAgreementNum | — |
| EXCHANGE_RATE_AGREEMENT_TYPE | IbyExtBankAccountsExchangeRateAgreementType | — |
| EXT_BANK_ACCOUNT_ID | IbyExtBankAccountsExtBankAccountId | — |
| FOREIGN_PAYMENT_USE_FLAG | IbyExtBankAccountsForeignPaymentUseFlag | — |
| HEDGING_CONTRACT_REFERENCE | IbyExtBankAccountsHedgingContractReference | — |
| IBAN | IbyExtBankAccountsIban | — |
| IBAN_HASH1 | IbyExtBankAccountsIbanHash1 | — |
| IBAN_HASH2 | IbyExtBankAccountsIbanHash2 | — |
| IBAN_SEC_SEGMENT_ID | IbyExtBankAccountsIbanSecSegmentId | — |
| MASKED_BANK_ACCOUNT_NUM | IbyExtBankAccountsMaskedBankAccountNum | — |
| MASKED_IBAN | IbyExtBankAccountsMaskedIban | — |
| OBJECT_VERSION_NUMBER | IbyExtBankAccountsObjectVersionNumber | — |
| PAYMENT_FACTOR_FLAG | IbyExtBankAccountsPaymentFactorFlag | — |
| PROGRAM_APPLICATION_ID | IbyExtBankAccountsProgramApplicationId | — |
| PROGRAM_ID | IbyExtBankAccountsProgramId | — |
| PROGRAM_UPDATE_DATE | IbyExtBankAccountsProgramUpdateDate | — |
| REQUEST_ID | IbyExtBankAccountsRequestId | — |
| SALT_VERSION | IbyExtBankAccountsSaltVersion | — |
| SECONDARY_ACCOUNT_REFERENCE | IbyExtBankAccountsSecondaryAccountReference | — |
| SHORT_ACCT_NAME | IbyExtBankAccountsShortAcctName | — |
| START_DATE | IbyExtBankAccountsStartDate | — |

### [[miscreceiptdistributionpvo|MiscReceiptDistributionPVO]] (AR · BICC: 4/98)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASSIFICATION | ExtBankAccountAccountClassification | — |
| ACCOUNT_CLASSIFICATION | OldCustBankAccountAccountClassification | — |
| ACCOUNT_SUFFIX | ExtBankAccountAccountSuffix | — |
| ACCOUNT_SUFFIX | OldCustBankAccountAccountSuffix | — |
| AGENCY_LOCATION_CODE | ExtBankAccountAgencyLocationCode | — |
| AGENCY_LOCATION_CODE | OldCustBankAccountAgencyLocationCode | — |
| BA_MASK_SETTING | ExtBankAccountBaMaskSetting | — |
| BA_MASK_SETTING | OldCustBankAccountBaMaskSetting | — |
| BA_NUM_ELEC_SEC_SEGMENT_ID | ExtBankAccountBaNumElecSecSegmentId | — |
| BA_NUM_ELEC_SEC_SEGMENT_ID | OldCustBankAccountBaNumElecSecSegmentId | — |
| BA_NUM_SEC_SEGMENT_ID | ExtBankAccountBaNumSecSegmentId | — |
| BA_NUM_SEC_SEGMENT_ID | OldCustBankAccountBaNumSecSegmentId | — |
| BA_UNMASK_LENGTH | ExtBankAccountBaUnmaskLength | — |
| BA_UNMASK_LENGTH | OldCustBankAccountBaUnmaskLength | — |
| BANK_ACCOUNT_NAME | ExtBankAccountBankAccountName | ✅ |
| BANK_ACCOUNT_NAME | OldCustBankAccountBankAccountName | — |
| BANK_ACCOUNT_NAME_ALT | ExtBankAccountBankAccountNameAlt | — |
| BANK_ACCOUNT_NAME_ALT | OldCustBankAccountBankAccountNameAlt | — |
| BANK_ACCOUNT_NUM | ExtBankAccountBankAccountNum | ✅ |
| BANK_ACCOUNT_NUM | OldCustBankAccountBankAccountNum | — |
| BANK_ACCOUNT_NUM_ELECTRONIC | ExtBankAccountBankAccountNumElectronic | — |
| BANK_ACCOUNT_NUM_ELECTRONIC | OldCustBankAccountBankAccountNumElectronic | — |
| BANK_ACCOUNT_NUM_HASH1 | ExtBankAccountBankAccountNumHash1 | — |
| BANK_ACCOUNT_NUM_HASH1 | OldCustBankAccountBankAccountNumHash1 | — |
| BANK_ACCOUNT_NUM_HASH2 | ExtBankAccountBankAccountNumHash2 | — |
| BANK_ACCOUNT_NUM_HASH2 | OldCustBankAccountBankAccountNumHash2 | — |
| BANK_ACCOUNT_TYPE | ExtBankAccountBankAccountType | — |
| BANK_ACCOUNT_TYPE | OldCustBankAccountBankAccountType | — |
| BANK_ID | ExtBankAccountBankId | — |
| BANK_ID | OldCustBankAccountBankId | — |
| BRANCH_ID | ExtBankAccountBranchId | — |
| BRANCH_ID | OldCustBankAccountBranchId | — |
| CHECK_DIGITS | ExtBankAccountCheckDigits | — |
| CHECK_DIGITS | OldCustBankAccountCheckDigits | — |
| COUNTRY_CODE | ExtBankAccountCountryCode | — |
| COUNTRY_CODE | OldCustBankAccountCountryCode | — |
| CREATED_BY | ExtBankAccountCreatedBy | — |
| CREATED_BY | OldCustBankAccountCreatedBy | — |
| CREATION_DATE | ExtBankAccountCreationDate | — |
| CREATION_DATE | OldCustBankAccountCreationDate | — |
| CURRENCY_CODE | ExtBankAccountCurrencyCode | — |
| CURRENCY_CODE | OldCustBankAccountCurrencyCode | — |
| DESCRIPTION | ExtBankAccountDescription | — |
| DESCRIPTION | OldCustBankAccountDescription | — |
| ENCRYPTED | ExtBankAccountEncrypted | — |
| ENCRYPTED | OldCustBankAccountEncrypted | — |
| END_DATE | ExtBankAccountEndDate | — |
| END_DATE | OldCustBankAccountEndDate | — |
| EXCHANGE_RATE | ExtBankAccountExchangeRate | — |
| EXCHANGE_RATE | OldCustBankAccountExchangeRate | — |
| EXCHANGE_RATE_AGREEMENT_NUM | ExtBankAccountExchangeRateAgreementNum | — |
| EXCHANGE_RATE_AGREEMENT_NUM | OldCustBankAccountExchangeRateAgreementNum | — |
| EXCHANGE_RATE_AGREEMENT_TYPE | ExtBankAccountExchangeRateAgreementType | — |
| EXCHANGE_RATE_AGREEMENT_TYPE | OldCustBankAccountExchangeRateAgreementType | — |
| EXT_BANK_ACCOUNT_ID | ExtBankAccountExtBankAccountId | — |
| EXT_BANK_ACCOUNT_ID | OldCustBankAccountExtBankAccountId | — |
| FOREIGN_PAYMENT_USE_FLAG | ExtBankAccountForeignPaymentUseFlag | — |
| FOREIGN_PAYMENT_USE_FLAG | OldCustBankAccountForeignPaymentUseFlag | — |
| HEDGING_CONTRACT_REFERENCE | ExtBankAccountHedgingContractReference | — |
| HEDGING_CONTRACT_REFERENCE | OldCustBankAccountHedgingContractReference | — |
| IBAN | ExtBankAccountIban | — |
| IBAN | OldCustBankAccountIban | — |
| IBAN_HASH1 | ExtBankAccountIbanHash1 | — |
| IBAN_HASH1 | OldCustBankAccountIbanHash1 | — |
| IBAN_HASH2 | ExtBankAccountIbanHash2 | — |
| IBAN_HASH2 | OldCustBankAccountIbanHash2 | — |
| IBAN_SEC_SEGMENT_ID | ExtBankAccountIbanSecSegmentId | — |
| IBAN_SEC_SEGMENT_ID | OldCustBankAccountIbanSecSegmentId | — |
| LAST_UPDATE_DATE | ExtBankAccountLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | OldCustBankAccountLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExtBankAccountLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | OldCustBankAccountLastUpdateLogin | — |
| LAST_UPDATED_BY | ExtBankAccountLastUpdatedBy | — |
| LAST_UPDATED_BY | OldCustBankAccountLastUpdatedBy | — |
| MASKED_BANK_ACCOUNT_NUM | ExtBankAccountMaskedBankAccountNum | — |
| MASKED_BANK_ACCOUNT_NUM | OldCustBankAccountMaskedBankAccountNum | — |
| MASKED_IBAN | ExtBankAccountMaskedIban | — |
| MASKED_IBAN | OldCustBankAccountMaskedIban | — |
| OBJECT_VERSION_NUMBER | ExtBankAccountObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | OldCustBankAccountObjectVersionNumber | — |
| PAYMENT_FACTOR_FLAG | ExtBankAccountPaymentFactorFlag | — |
| PAYMENT_FACTOR_FLAG | OldCustBankAccountPaymentFactorFlag | — |
| PROGRAM_APPLICATION_ID | ExtBankAccountProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | OldCustBankAccountProgramApplicationId | — |
| PROGRAM_ID | ExtBankAccountProgramId | — |
| PROGRAM_ID | OldCustBankAccountProgramId | — |
| PROGRAM_UPDATE_DATE | ExtBankAccountProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | OldCustBankAccountProgramUpdateDate | — |
| REQUEST_ID | ExtBankAccountRequestId | — |
| REQUEST_ID | OldCustBankAccountRequestId | — |
| SALT_VERSION | ExtBankAccountSaltVersion | — |
| SALT_VERSION | OldCustBankAccountSaltVersion | — |
| SECONDARY_ACCOUNT_REFERENCE | ExtBankAccountSecondaryAccountReference | — |
| SECONDARY_ACCOUNT_REFERENCE | OldCustBankAccountSecondaryAccountReference | — |
| SHORT_ACCT_NAME | ExtBankAccountShortAcctName | — |
| SHORT_ACCT_NAME | OldCustBankAccountShortAcctName | — |
| START_DATE | ExtBankAccountStartDate | — |
| START_DATE | OldCustBankAccountStartDate | — |

### [[paiddisbursementschedulepvo|PaidDisbursementSchedulePVO]] (AP · BICC: 7/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BA_MASK_SETTING | ExtBnkAcctBaMaskSetting | — |
| BANK_ACCOUNT_NAME | ExtBnkAcctBankAccountName | ✅ |
| BANK_BRANCH_PARTY_FLAG | ExtBnkAcctBankBranchPartyFlag | — |
| BRANCH_NUMBER | ExtBnkAcctBranchNumber | ✅ |
| CHECK_DIGITS | ExtBnkAcctCheckDigits | ✅ |
| COUNTRY_CODE | ExtBnkAcctCountryCode | ✅ |
| DESCRIPTION | ExtBnkAcctDescription | ✅ |
| EFT_SWIFT_CODE | ExtBnkAcctSwiftCode | — |
| EXT_BANK_ACCOUNT_ID | ExtBnkAcctExtBankAccountId | — |
| IBAN | ExtBnkAcctIban | — |
| MASKED_BANK_ACCOUNT_NUM | ExtBnkAcctMaskedBankAccountNum | ✅ |
| MASKED_IBAN | ExtBnkAcctMaskedIban | — |
| SECONDARY_ACCOUNT_REFERENCE | ExtBnkAcctSecondaryAccountReference | ✅ |

### [[paymenthistorydistributionpvo|PaymentHistoryDistributionPVO]] (AP · BICC: 9/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BA_MASK_SETTING | ExtBnkAcctBaMaskSetting | — |
| BANK_ACCOUNT_NAME | ExtBnkAcctBankAccountName | ✅ |
| BANK_BRANCH_PARTY_FLAG | ExtBnkAcctBankBranchPartyFlag | — |
| BRANCH_NUMBER | ExtBnkAcctBranchNumber | ✅ |
| CHECK_DIGITS | ExtBnkAcctCheckDigits | ✅ |
| COUNTRY_CODE | ExtBnkAcctCountryCode | ✅ |
| DESCRIPTION | ExtBnkAcctDescription | ✅ |
| EFT_SWIFT_CODE | ExtBnkAcctSwiftCode | — |
| EXT_BANK_ACCOUNT_ID | ExtBnkAcctExtBankAccountId | — |
| EXT_BANK_ACCOUNT_ID | InvExtBnkAcctExtBankAccountId | — |
| EXT_BANK_ACCOUNT_ID | PayExtBnkAcctExtBankAccountId | — |
| IBAN | ExtBnkAcctIban | — |
| LAST_UPDATE_DATE | InvExtBnkAcctLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PayExtBnkAcctLastUpdateDate | ✅ |
| MASKED_BANK_ACCOUNT_NUM | ExtBnkAcctMaskedBankAccountNum | ✅ |
| MASKED_IBAN | ExtBnkAcctMaskedIban | — |
| SECONDARY_ACCOUNT_REFERENCE | ExtBnkAcctSecondaryAccountReference | ✅ |

### [[prepaymentappliationdistributionpvo|PrepaymentAppliationDistributionPVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EXT_BANK_ACCOUNT_ID | InvExtBnkAcctExtBankAccountId | — |
| LAST_UPDATE_DATE | InvExtBnkAcctLastUpdateDate | ✅ |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR · BICC: 2/98)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASSIFICATION | ExtBankAccountAccountClassification | — |
| ACCOUNT_CLASSIFICATION | OldCustBankAccountAccountClassification | — |
| ACCOUNT_SUFFIX | ExtBankAccountAccountSuffix | — |
| ACCOUNT_SUFFIX | OldCustBankAccountAccountSuffix | — |
| AGENCY_LOCATION_CODE | ExtBankAccountAgencyLocationCode | — |
| AGENCY_LOCATION_CODE | OldCustBankAccountAgencyLocationCode | — |
| BA_MASK_SETTING | ExtBankAccountBaMaskSetting | — |
| BA_MASK_SETTING | OldCustBankAccountBaMaskSetting | — |
| BA_NUM_ELEC_SEC_SEGMENT_ID | ExtBankAccountBaNumElecSecSegmentId | — |
| BA_NUM_ELEC_SEC_SEGMENT_ID | OldCustBankAccountBaNumElecSecSegmentId | — |
| BA_NUM_SEC_SEGMENT_ID | ExtBankAccountBaNumSecSegmentId | — |
| BA_NUM_SEC_SEGMENT_ID | OldCustBankAccountBaNumSecSegmentId | — |
| BA_UNMASK_LENGTH | ExtBankAccountBaUnmaskLength | — |
| BA_UNMASK_LENGTH | OldCustBankAccountBaUnmaskLength | — |
| BANK_ACCOUNT_NAME | ExtBankAccountBankAccountName | — |
| BANK_ACCOUNT_NAME | OldCustBankAccountBankAccountName | — |
| BANK_ACCOUNT_NAME_ALT | ExtBankAccountBankAccountNameAlt | — |
| BANK_ACCOUNT_NAME_ALT | OldCustBankAccountBankAccountNameAlt | — |
| BANK_ACCOUNT_NUM | ExtBankAccountBankAccountNum | — |
| BANK_ACCOUNT_NUM | OldCustBankAccountBankAccountNum | — |
| BANK_ACCOUNT_NUM_ELECTRONIC | ExtBankAccountBankAccountNumElectronic | — |
| BANK_ACCOUNT_NUM_ELECTRONIC | OldCustBankAccountBankAccountNumElectronic | — |
| BANK_ACCOUNT_NUM_HASH1 | ExtBankAccountBankAccountNumHash1 | — |
| BANK_ACCOUNT_NUM_HASH1 | OldCustBankAccountBankAccountNumHash1 | — |
| BANK_ACCOUNT_NUM_HASH2 | ExtBankAccountBankAccountNumHash2 | — |
| BANK_ACCOUNT_NUM_HASH2 | OldCustBankAccountBankAccountNumHash2 | — |
| BANK_ACCOUNT_TYPE | ExtBankAccountBankAccountType | — |
| BANK_ACCOUNT_TYPE | OldCustBankAccountBankAccountType | — |
| BANK_ID | ExtBankAccountBankId | — |
| BANK_ID | OldCustBankAccountBankId | — |
| BRANCH_ID | ExtBankAccountBranchId | — |
| BRANCH_ID | OldCustBankAccountBranchId | — |
| CHECK_DIGITS | ExtBankAccountCheckDigits | — |
| CHECK_DIGITS | OldCustBankAccountCheckDigits | — |
| COUNTRY_CODE | ExtBankAccountCountryCode | — |
| COUNTRY_CODE | OldCustBankAccountCountryCode | — |
| CREATED_BY | ExtBankAccountCreatedBy | — |
| CREATED_BY | OldCustBankAccountCreatedBy | — |
| CREATION_DATE | ExtBankAccountCreationDate | — |
| CREATION_DATE | OldCustBankAccountCreationDate | — |
| CURRENCY_CODE | ExtBankAccountCurrencyCode | — |
| CURRENCY_CODE | OldCustBankAccountCurrencyCode | — |
| DESCRIPTION | ExtBankAccountDescription | — |
| DESCRIPTION | OldCustBankAccountDescription | — |
| ENCRYPTED | ExtBankAccountEncrypted | — |
| ENCRYPTED | OldCustBankAccountEncrypted | — |
| END_DATE | ExtBankAccountEndDate | — |
| END_DATE | OldCustBankAccountEndDate | — |
| EXCHANGE_RATE | ExtBankAccountExchangeRate | — |
| EXCHANGE_RATE | OldCustBankAccountExchangeRate | — |
| EXCHANGE_RATE_AGREEMENT_NUM | ExtBankAccountExchangeRateAgreementNum | — |
| EXCHANGE_RATE_AGREEMENT_NUM | OldCustBankAccountExchangeRateAgreementNum | — |
| EXCHANGE_RATE_AGREEMENT_TYPE | ExtBankAccountExchangeRateAgreementType | — |
| EXCHANGE_RATE_AGREEMENT_TYPE | OldCustBankAccountExchangeRateAgreementType | — |
| EXT_BANK_ACCOUNT_ID | ExtBankAccountExtBankAccountId | — |
| EXT_BANK_ACCOUNT_ID | OldCustBankAccountExtBankAccountId | — |
| FOREIGN_PAYMENT_USE_FLAG | ExtBankAccountForeignPaymentUseFlag | — |
| FOREIGN_PAYMENT_USE_FLAG | OldCustBankAccountForeignPaymentUseFlag | — |
| HEDGING_CONTRACT_REFERENCE | ExtBankAccountHedgingContractReference | — |
| HEDGING_CONTRACT_REFERENCE | OldCustBankAccountHedgingContractReference | — |
| IBAN | ExtBankAccountIban | — |
| IBAN | OldCustBankAccountIban | — |
| IBAN_HASH1 | ExtBankAccountIbanHash1 | — |
| IBAN_HASH1 | OldCustBankAccountIbanHash1 | — |
| IBAN_HASH2 | ExtBankAccountIbanHash2 | — |
| IBAN_HASH2 | OldCustBankAccountIbanHash2 | — |
| IBAN_SEC_SEGMENT_ID | ExtBankAccountIbanSecSegmentId | — |
| IBAN_SEC_SEGMENT_ID | OldCustBankAccountIbanSecSegmentId | — |
| LAST_UPDATE_DATE | ExtBankAccountLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | OldCustBankAccountLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExtBankAccountLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | OldCustBankAccountLastUpdateLogin | — |
| LAST_UPDATED_BY | ExtBankAccountLastUpdatedBy | — |
| LAST_UPDATED_BY | OldCustBankAccountLastUpdatedBy | — |
| MASKED_BANK_ACCOUNT_NUM | ExtBankAccountMaskedBankAccountNum | — |
| MASKED_BANK_ACCOUNT_NUM | OldCustBankAccountMaskedBankAccountNum | — |
| MASKED_IBAN | ExtBankAccountMaskedIban | — |
| MASKED_IBAN | OldCustBankAccountMaskedIban | — |
| OBJECT_VERSION_NUMBER | ExtBankAccountObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | OldCustBankAccountObjectVersionNumber | — |
| PAYMENT_FACTOR_FLAG | ExtBankAccountPaymentFactorFlag | — |
| PAYMENT_FACTOR_FLAG | OldCustBankAccountPaymentFactorFlag | — |
| PROGRAM_APPLICATION_ID | ExtBankAccountProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | OldCustBankAccountProgramApplicationId | — |
| PROGRAM_ID | ExtBankAccountProgramId | — |
| PROGRAM_ID | OldCustBankAccountProgramId | — |
| PROGRAM_UPDATE_DATE | ExtBankAccountProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | OldCustBankAccountProgramUpdateDate | — |
| REQUEST_ID | ExtBankAccountRequestId | — |
| REQUEST_ID | OldCustBankAccountRequestId | — |
| SALT_VERSION | ExtBankAccountSaltVersion | — |
| SALT_VERSION | OldCustBankAccountSaltVersion | — |
| SECONDARY_ACCOUNT_REFERENCE | ExtBankAccountSecondaryAccountReference | — |
| SECONDARY_ACCOUNT_REFERENCE | OldCustBankAccountSecondaryAccountReference | — |
| SHORT_ACCT_NAME | ExtBankAccountShortAcctName | — |
| SHORT_ACCT_NAME | OldCustBankAccountShortAcctName | — |
| START_DATE | ExtBankAccountStartDate | — |
| START_DATE | OldCustBankAccountStartDate | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR · BICC: 4/98)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASSIFICATION | ExtBankAccountAccountClassification | — |
| ACCOUNT_CLASSIFICATION | OldCustBankAccountAccountClassification | — |
| ACCOUNT_SUFFIX | ExtBankAccountAccountSuffix | — |
| ACCOUNT_SUFFIX | OldCustBankAccountAccountSuffix | — |
| AGENCY_LOCATION_CODE | ExtBankAccountAgencyLocationCode | — |
| AGENCY_LOCATION_CODE | OldCustBankAccountAgencyLocationCode | — |
| BA_MASK_SETTING | ExtBankAccountBaMaskSetting | — |
| BA_MASK_SETTING | OldCustBankAccountBaMaskSetting | — |
| BA_NUM_ELEC_SEC_SEGMENT_ID | ExtBankAccountBaNumElecSecSegmentId | — |
| BA_NUM_ELEC_SEC_SEGMENT_ID | OldCustBankAccountBaNumElecSecSegmentId | — |
| BA_NUM_SEC_SEGMENT_ID | ExtBankAccountBaNumSecSegmentId | — |
| BA_NUM_SEC_SEGMENT_ID | OldCustBankAccountBaNumSecSegmentId | — |
| BA_UNMASK_LENGTH | ExtBankAccountBaUnmaskLength | — |
| BA_UNMASK_LENGTH | OldCustBankAccountBaUnmaskLength | — |
| BANK_ACCOUNT_NAME | ExtBankAccountBankAccountName | ✅ |
| BANK_ACCOUNT_NAME | OldCustBankAccountBankAccountName | — |
| BANK_ACCOUNT_NAME_ALT | ExtBankAccountBankAccountNameAlt | — |
| BANK_ACCOUNT_NAME_ALT | OldCustBankAccountBankAccountNameAlt | — |
| BANK_ACCOUNT_NUM | ExtBankAccountBankAccountNum | ✅ |
| BANK_ACCOUNT_NUM | OldCustBankAccountBankAccountNum | — |
| BANK_ACCOUNT_NUM_ELECTRONIC | ExtBankAccountBankAccountNumElectronic | — |
| BANK_ACCOUNT_NUM_ELECTRONIC | OldCustBankAccountBankAccountNumElectronic | — |
| BANK_ACCOUNT_NUM_HASH1 | ExtBankAccountBankAccountNumHash1 | — |
| BANK_ACCOUNT_NUM_HASH1 | OldCustBankAccountBankAccountNumHash1 | — |
| BANK_ACCOUNT_NUM_HASH2 | ExtBankAccountBankAccountNumHash2 | — |
| BANK_ACCOUNT_NUM_HASH2 | OldCustBankAccountBankAccountNumHash2 | — |
| BANK_ACCOUNT_TYPE | ExtBankAccountBankAccountType | — |
| BANK_ACCOUNT_TYPE | OldCustBankAccountBankAccountType | — |
| BANK_ID | ExtBankAccountBankId | — |
| BANK_ID | OldCustBankAccountBankId | — |
| BRANCH_ID | ExtBankAccountBranchId | — |
| BRANCH_ID | OldCustBankAccountBranchId | — |
| CHECK_DIGITS | ExtBankAccountCheckDigits | — |
| CHECK_DIGITS | OldCustBankAccountCheckDigits | — |
| COUNTRY_CODE | ExtBankAccountCountryCode | — |
| COUNTRY_CODE | OldCustBankAccountCountryCode | — |
| CREATED_BY | ExtBankAccountCreatedBy | — |
| CREATED_BY | OldCustBankAccountCreatedBy | — |
| CREATION_DATE | ExtBankAccountCreationDate | — |
| CREATION_DATE | OldCustBankAccountCreationDate | — |
| CURRENCY_CODE | ExtBankAccountCurrencyCode | — |
| CURRENCY_CODE | OldCustBankAccountCurrencyCode | — |
| DESCRIPTION | ExtBankAccountDescription | — |
| DESCRIPTION | OldCustBankAccountDescription | — |
| ENCRYPTED | ExtBankAccountEncrypted | — |
| ENCRYPTED | OldCustBankAccountEncrypted | — |
| END_DATE | ExtBankAccountEndDate | — |
| END_DATE | OldCustBankAccountEndDate | — |
| EXCHANGE_RATE | ExtBankAccountExchangeRate | — |
| EXCHANGE_RATE | OldCustBankAccountExchangeRate | — |
| EXCHANGE_RATE_AGREEMENT_NUM | ExtBankAccountExchangeRateAgreementNum | — |
| EXCHANGE_RATE_AGREEMENT_NUM | OldCustBankAccountExchangeRateAgreementNum | — |
| EXCHANGE_RATE_AGREEMENT_TYPE | ExtBankAccountExchangeRateAgreementType | — |
| EXCHANGE_RATE_AGREEMENT_TYPE | OldCustBankAccountExchangeRateAgreementType | — |
| EXT_BANK_ACCOUNT_ID | ExtBankAccountExtBankAccountId | — |
| EXT_BANK_ACCOUNT_ID | OldCustBankAccountExtBankAccountId | — |
| FOREIGN_PAYMENT_USE_FLAG | ExtBankAccountForeignPaymentUseFlag | — |
| FOREIGN_PAYMENT_USE_FLAG | OldCustBankAccountForeignPaymentUseFlag | — |
| HEDGING_CONTRACT_REFERENCE | ExtBankAccountHedgingContractReference | — |
| HEDGING_CONTRACT_REFERENCE | OldCustBankAccountHedgingContractReference | — |
| IBAN | ExtBankAccountIban | — |
| IBAN | OldCustBankAccountIban | — |
| IBAN_HASH1 | ExtBankAccountIbanHash1 | — |
| IBAN_HASH1 | OldCustBankAccountIbanHash1 | — |
| IBAN_HASH2 | ExtBankAccountIbanHash2 | — |
| IBAN_HASH2 | OldCustBankAccountIbanHash2 | — |
| IBAN_SEC_SEGMENT_ID | ExtBankAccountIbanSecSegmentId | — |
| IBAN_SEC_SEGMENT_ID | OldCustBankAccountIbanSecSegmentId | — |
| LAST_UPDATE_DATE | ExtBankAccountLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | OldCustBankAccountLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExtBankAccountLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | OldCustBankAccountLastUpdateLogin | — |
| LAST_UPDATED_BY | ExtBankAccountLastUpdatedBy | — |
| LAST_UPDATED_BY | OldCustBankAccountLastUpdatedBy | — |
| MASKED_BANK_ACCOUNT_NUM | ExtBankAccountMaskedBankAccountNum | — |
| MASKED_BANK_ACCOUNT_NUM | OldCustBankAccountMaskedBankAccountNum | — |
| MASKED_IBAN | ExtBankAccountMaskedIban | — |
| MASKED_IBAN | OldCustBankAccountMaskedIban | — |
| OBJECT_VERSION_NUMBER | ExtBankAccountObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | OldCustBankAccountObjectVersionNumber | — |
| PAYMENT_FACTOR_FLAG | ExtBankAccountPaymentFactorFlag | — |
| PAYMENT_FACTOR_FLAG | OldCustBankAccountPaymentFactorFlag | — |
| PROGRAM_APPLICATION_ID | ExtBankAccountProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | OldCustBankAccountProgramApplicationId | — |
| PROGRAM_ID | ExtBankAccountProgramId | — |
| PROGRAM_ID | OldCustBankAccountProgramId | — |
| PROGRAM_UPDATE_DATE | ExtBankAccountProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | OldCustBankAccountProgramUpdateDate | — |
| REQUEST_ID | ExtBankAccountRequestId | — |
| REQUEST_ID | OldCustBankAccountRequestId | — |
| SALT_VERSION | ExtBankAccountSaltVersion | — |
| SALT_VERSION | OldCustBankAccountSaltVersion | — |
| SECONDARY_ACCOUNT_REFERENCE | ExtBankAccountSecondaryAccountReference | — |
| SECONDARY_ACCOUNT_REFERENCE | OldCustBankAccountSecondaryAccountReference | — |
| SHORT_ACCT_NAME | ExtBankAccountShortAcctName | — |
| SHORT_ACCT_NAME | OldCustBankAccountShortAcctName | — |
| START_DATE | ExtBankAccountStartDate | — |
| START_DATE | OldCustBankAccountStartDate | — |

### [[receiptapplicationpvo|ReceiptApplicationPVO]] (AR · BICC: 2/44)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASSIFICATION | IbyExtBankAccountsAccountClassification | — |
| ACCOUNT_SUFFIX | IbyExtBankAccountsAccountSuffix | — |
| AGENCY_LOCATION_CODE | IbyExtBankAccountsAgencyLocationCode | — |
| BA_MASK_SETTING | IbyExtBankAccountsBaMaskSetting | — |
| BA_NUM_ELEC_SEC_SEGMENT_ID | IbyExtBankAccountsBaNumElecSecSegmentId | — |
| BA_NUM_SEC_SEGMENT_ID | IbyExtBankAccountsBaNumSecSegmentId | — |
| BA_UNMASK_LENGTH | IbyExtBankAccountsBaUnmaskLength | — |
| BANK_ACCOUNT_NAME | IbyExtBankAccountsBankAccountName | ✅ |
| BANK_ACCOUNT_NAME_ALT | IbyExtBankAccountsBankAccountNameAlt | — |
| BANK_ACCOUNT_NUM | IbyExtBankAccountsBankAccountNum | ✅ |
| BANK_ACCOUNT_NUM_ELECTRONIC | IbyExtBankAccountsBankAccountNumElectronic | — |
| BANK_ACCOUNT_NUM_HASH1 | IbyExtBankAccountsBankAccountNumHash1 | — |
| BANK_ACCOUNT_NUM_HASH2 | IbyExtBankAccountsBankAccountNumHash2 | — |
| BANK_ACCOUNT_TYPE | IbyExtBankAccountsBankAccountType | — |
| BANK_ID | IbyExtBankAccountsBankId | — |
| BRANCH_ID | IbyExtBankAccountsBranchId | — |
| CHECK_DIGITS | IbyExtBankAccountsCheckDigits | — |
| COUNTRY_CODE | IbyExtBankAccountsCountryCode | — |
| CURRENCY_CODE | IbyExtBankAccountsCurrencyCode | — |
| DESCRIPTION | IbyExtBankAccountsDescription | — |
| ENCRYPTED | IbyExtBankAccountsEncrypted | — |
| END_DATE | IbyExtBankAccountsEndDate | — |
| EXCHANGE_RATE | IbyExtBankAccountsExchangeRate | — |
| EXCHANGE_RATE_AGREEMENT_NUM | IbyExtBankAccountsExchangeRateAgreementNum | — |
| EXCHANGE_RATE_AGREEMENT_TYPE | IbyExtBankAccountsExchangeRateAgreementType | — |
| EXT_BANK_ACCOUNT_ID | IbyExtBankAccountsExtBankAccountId | — |
| FOREIGN_PAYMENT_USE_FLAG | IbyExtBankAccountsForeignPaymentUseFlag | — |
| HEDGING_CONTRACT_REFERENCE | IbyExtBankAccountsHedgingContractReference | — |
| IBAN | IbyExtBankAccountsIban | — |
| IBAN_HASH1 | IbyExtBankAccountsIbanHash1 | — |
| IBAN_HASH2 | IbyExtBankAccountsIbanHash2 | — |
| IBAN_SEC_SEGMENT_ID | IbyExtBankAccountsIbanSecSegmentId | — |
| MASKED_BANK_ACCOUNT_NUM | IbyExtBankAccountsMaskedBankAccountNum | — |
| MASKED_IBAN | IbyExtBankAccountsMaskedIban | — |
| OBJECT_VERSION_NUMBER | IbyExtBankAccountsObjectVersionNumber | — |
| PAYMENT_FACTOR_FLAG | IbyExtBankAccountsPaymentFactorFlag | — |
| PROGRAM_APPLICATION_ID | IbyExtBankAccountsProgramApplicationId | — |
| PROGRAM_ID | IbyExtBankAccountsProgramId | — |
| PROGRAM_UPDATE_DATE | IbyExtBankAccountsProgramUpdateDate | — |
| REQUEST_ID | IbyExtBankAccountsRequestId | — |
| SALT_VERSION | IbyExtBankAccountsSaltVersion | — |
| SECONDARY_ACCOUNT_REFERENCE | IbyExtBankAccountsSecondaryAccountReference | — |
| SHORT_ACCT_NAME | IbyExtBankAccountsShortAcctName | — |
| START_DATE | IbyExtBankAccountsStartDate | — |

### [[receiptheaderpvo|ReceiptHeaderPVO]] (AR · BICC: 4/98)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASSIFICATION | ExtBankAccountAccountClassification | — |
| ACCOUNT_CLASSIFICATION | OldCustBankAccountAccountClassification | — |
| ACCOUNT_SUFFIX | ExtBankAccountAccountSuffix | — |
| ACCOUNT_SUFFIX | OldCustBankAccountAccountSuffix | — |
| AGENCY_LOCATION_CODE | ExtBankAccountAgencyLocationCode | — |
| AGENCY_LOCATION_CODE | OldCustBankAccountAgencyLocationCode | — |
| BA_MASK_SETTING | ExtBankAccountBaMaskSetting | — |
| BA_MASK_SETTING | OldCustBankAccountBaMaskSetting | — |
| BA_NUM_ELEC_SEC_SEGMENT_ID | ExtBankAccountBaNumElecSecSegmentId | — |
| BA_NUM_ELEC_SEC_SEGMENT_ID | OldCustBankAccountBaNumElecSecSegmentId | — |
| BA_NUM_SEC_SEGMENT_ID | ExtBankAccountBaNumSecSegmentId | — |
| BA_NUM_SEC_SEGMENT_ID | OldCustBankAccountBaNumSecSegmentId | — |
| BA_UNMASK_LENGTH | ExtBankAccountBaUnmaskLength | — |
| BA_UNMASK_LENGTH | OldCustBankAccountBaUnmaskLength | — |
| BANK_ACCOUNT_NAME | ExtBankAccountBankAccountName | ✅ |
| BANK_ACCOUNT_NAME | OldCustBankAccountBankAccountName | — |
| BANK_ACCOUNT_NAME_ALT | ExtBankAccountBankAccountNameAlt | — |
| BANK_ACCOUNT_NAME_ALT | OldCustBankAccountBankAccountNameAlt | — |
| BANK_ACCOUNT_NUM | ExtBankAccountBankAccountNum | ✅ |
| BANK_ACCOUNT_NUM | OldCustBankAccountBankAccountNum | — |
| BANK_ACCOUNT_NUM_ELECTRONIC | ExtBankAccountBankAccountNumElectronic | — |
| BANK_ACCOUNT_NUM_ELECTRONIC | OldCustBankAccountBankAccountNumElectronic | — |
| BANK_ACCOUNT_NUM_HASH1 | ExtBankAccountBankAccountNumHash1 | — |
| BANK_ACCOUNT_NUM_HASH1 | OldCustBankAccountBankAccountNumHash1 | — |
| BANK_ACCOUNT_NUM_HASH2 | ExtBankAccountBankAccountNumHash2 | — |
| BANK_ACCOUNT_NUM_HASH2 | OldCustBankAccountBankAccountNumHash2 | — |
| BANK_ACCOUNT_TYPE | ExtBankAccountBankAccountType | — |
| BANK_ACCOUNT_TYPE | OldCustBankAccountBankAccountType | — |
| BANK_ID | ExtBankAccountBankId | — |
| BANK_ID | OldCustBankAccountBankId | — |
| BRANCH_ID | ExtBankAccountBranchId | — |
| BRANCH_ID | OldCustBankAccountBranchId | — |
| CHECK_DIGITS | ExtBankAccountCheckDigits | — |
| CHECK_DIGITS | OldCustBankAccountCheckDigits | — |
| COUNTRY_CODE | ExtBankAccountCountryCode | — |
| COUNTRY_CODE | OldCustBankAccountCountryCode | — |
| CREATED_BY | ExtBankAccountCreatedBy | — |
| CREATED_BY | OldCustBankAccountCreatedBy | — |
| CREATION_DATE | ExtBankAccountCreationDate | — |
| CREATION_DATE | OldCustBankAccountCreationDate | — |
| CURRENCY_CODE | ExtBankAccountCurrencyCode | — |
| CURRENCY_CODE | OldCustBankAccountCurrencyCode | — |
| DESCRIPTION | ExtBankAccountDescription | — |
| DESCRIPTION | OldCustBankAccountDescription | — |
| ENCRYPTED | ExtBankAccountEncrypted | — |
| ENCRYPTED | OldCustBankAccountEncrypted | — |
| END_DATE | ExtBankAccountEndDate | — |
| END_DATE | OldCustBankAccountEndDate | — |
| EXCHANGE_RATE | ExtBankAccountExchangeRate | — |
| EXCHANGE_RATE | OldCustBankAccountExchangeRate | — |
| EXCHANGE_RATE_AGREEMENT_NUM | ExtBankAccountExchangeRateAgreementNum | — |
| EXCHANGE_RATE_AGREEMENT_NUM | OldCustBankAccountExchangeRateAgreementNum | — |
| EXCHANGE_RATE_AGREEMENT_TYPE | ExtBankAccountExchangeRateAgreementType | — |
| EXCHANGE_RATE_AGREEMENT_TYPE | OldCustBankAccountExchangeRateAgreementType | — |
| EXT_BANK_ACCOUNT_ID | ExtBankAccountExtBankAccountId | — |
| EXT_BANK_ACCOUNT_ID | OldCustBankAccountExtBankAccountId | — |
| FOREIGN_PAYMENT_USE_FLAG | ExtBankAccountForeignPaymentUseFlag | — |
| FOREIGN_PAYMENT_USE_FLAG | OldCustBankAccountForeignPaymentUseFlag | — |
| HEDGING_CONTRACT_REFERENCE | ExtBankAccountHedgingContractReference | — |
| HEDGING_CONTRACT_REFERENCE | OldCustBankAccountHedgingContractReference | — |
| IBAN | ExtBankAccountIban | — |
| IBAN | OldCustBankAccountIban | — |
| IBAN_HASH1 | ExtBankAccountIbanHash1 | — |
| IBAN_HASH1 | OldCustBankAccountIbanHash1 | — |
| IBAN_HASH2 | ExtBankAccountIbanHash2 | — |
| IBAN_HASH2 | OldCustBankAccountIbanHash2 | — |
| IBAN_SEC_SEGMENT_ID | ExtBankAccountIbanSecSegmentId | — |
| IBAN_SEC_SEGMENT_ID | OldCustBankAccountIbanSecSegmentId | — |
| LAST_UPDATE_DATE | ExtBankAccountLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | OldCustBankAccountLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExtBankAccountLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | OldCustBankAccountLastUpdateLogin | — |
| LAST_UPDATED_BY | ExtBankAccountLastUpdatedBy | — |
| LAST_UPDATED_BY | OldCustBankAccountLastUpdatedBy | — |
| MASKED_BANK_ACCOUNT_NUM | ExtBankAccountMaskedBankAccountNum | — |
| MASKED_BANK_ACCOUNT_NUM | OldCustBankAccountMaskedBankAccountNum | — |
| MASKED_IBAN | ExtBankAccountMaskedIban | — |
| MASKED_IBAN | OldCustBankAccountMaskedIban | — |
| OBJECT_VERSION_NUMBER | ExtBankAccountObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | OldCustBankAccountObjectVersionNumber | — |
| PAYMENT_FACTOR_FLAG | ExtBankAccountPaymentFactorFlag | — |
| PAYMENT_FACTOR_FLAG | OldCustBankAccountPaymentFactorFlag | — |
| PROGRAM_APPLICATION_ID | ExtBankAccountProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | OldCustBankAccountProgramApplicationId | — |
| PROGRAM_ID | ExtBankAccountProgramId | — |
| PROGRAM_ID | OldCustBankAccountProgramId | — |
| PROGRAM_UPDATE_DATE | ExtBankAccountProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | OldCustBankAccountProgramUpdateDate | — |
| REQUEST_ID | ExtBankAccountRequestId | — |
| REQUEST_ID | OldCustBankAccountRequestId | — |
| SALT_VERSION | ExtBankAccountSaltVersion | — |
| SALT_VERSION | OldCustBankAccountSaltVersion | — |
| SECONDARY_ACCOUNT_REFERENCE | ExtBankAccountSecondaryAccountReference | — |
| SECONDARY_ACCOUNT_REFERENCE | OldCustBankAccountSecondaryAccountReference | — |
| SHORT_ACCT_NAME | ExtBankAccountShortAcctName | — |
| SHORT_ACCT_NAME | OldCustBankAccountShortAcctName | — |
| START_DATE | ExtBankAccountStartDate | — |
| START_DATE | OldCustBankAccountStartDate | — |

### [[sitebankaccount|SiteBankAccount]] (AR · BICC: 8/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASSIFICATION | BankAccountAccountClassification | — |
| ACCOUNT_SUFFIX | BankAccountAccountSuffix | — |
| AGENCY_LOCATION_CODE | BankAccountAgencyLocationCode | — |
| BA_MASK_SETTING | BankAccountBaMaskSetting | — |
| BA_NUM_ELEC_SEC_SEGMENT_ID | BankAccountBaNumElecSecSegmentId | — |
| BA_NUM_SEC_SEGMENT_ID | BankAccountBaNumSecSegmentId | — |
| BA_UNMASK_LENGTH | BankAccountBaUnmaskLength | — |
| BANK_ACCOUNT_NAME | BankAccountBankAccountName | ✅ |
| BANK_ACCOUNT_NAME_ALT | BankAccountBankAccountNameAlt | — |
| BANK_ACCOUNT_NUM | BankAccountBankAccountNum | — |
| BANK_ACCOUNT_NUM_ELECTRONIC | BankAccountBankAccountNumElectronic | — |
| BANK_ACCOUNT_TYPE | BankAccountBankAccountType | ✅ |
| BANK_ID | BankAccountBankId | — |
| BRANCH_ID | BankAccountBranchId | — |
| CHECK_DIGITS | BankAccountCheckDigits | ✅ |
| COUNTRY_CODE | BankAccountCountryCode | — |
| CREATED_BY | BankAccountCreatedBy | — |
| CREATION_DATE | BankAccountCreationDate | — |
| CURRENCY_CODE | BankAccountCurrencyCode | ✅ |
| DESCRIPTION | BankAccountDescription | ✅ |
| ENCRYPTED | BankAccountEncrypted | — |
| END_DATE | BankAccountEndDate | — |
| EXCHANGE_RATE | BankAccountExchangeRate | — |
| EXCHANGE_RATE_AGREEMENT_NUM | BankAccountExchangeRateAgreementNum | — |
| EXCHANGE_RATE_AGREEMENT_TYPE | BankAccountExchangeRateAgreementType | — |
| EXT_BANK_ACCOUNT_ID | BankAccountExtBankAccountId | — |
| FOREIGN_PAYMENT_USE_FLAG | BankAccountForeignPaymentUseFlag | — |
| HEDGING_CONTRACT_REFERENCE | BankAccountHedgingContractReference | — |
| IBAN | BankAccountIban | — |
| IBAN_HASH1 | BankAccountIbanHash1 | — |
| IBAN_SEC_SEGMENT_ID | BankAccountIbanSecSegmentId | — |
| LAST_UPDATE_DATE | BankAccountLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BankAccountLastUpdateLogin | — |
| LAST_UPDATED_BY | BankAccountLastUpdatedBy | — |
| MASKED_BANK_ACCOUNT_NUM | BankAccountMaskedBankAccountNum | ✅ |
| MASKED_IBAN | BankAccountMaskedIban | ✅ |
| OBJECT_VERSION_NUMBER | BankAccountObjectVersionNumber | — |
| PAYMENT_FACTOR_FLAG | BankAccountPaymentFactorFlag | — |
| PROGRAM_APPLICATION_ID | BankAccountProgramApplicationId | — |
| PROGRAM_ID | BankAccountProgramId | — |
| PROGRAM_UPDATE_DATE | BankAccountProgramUpdateDate | — |
| REQUEST_ID | BankAccountRequestId | — |
| SALT_VERSION | BankAccountSaltVersion | — |
| SECONDARY_ACCOUNT_REFERENCE | BankAccountSecondaryAccountReference | — |
| SHORT_ACCT_NAME | BankAccountShortAcctName | — |
| START_DATE | BankAccountStartDate | — |

### [[supplieraddressbankaccountpvo|SupplierAddressBankAccountPVO]] (PO · BICC: 10/45)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASSIFICATION | BankAccountAccountClassification | — |
| ACCOUNT_SUFFIX | BankAccountAccountSuffix | — |
| AGENCY_LOCATION_CODE | BankAccountAgencyLocationCode | — |
| BA_MASK_SETTING | BankAccountBaMaskSetting | — |
| BA_NUM_ELEC_SEC_SEGMENT_ID | BankAccountBaNumElecSecSegmentId | — |
| BA_NUM_SEC_SEGMENT_ID | BankAccountBaNumSecSegmentId | — |
| BA_UNMASK_LENGTH | BankAccountBaUnmaskLength | — |
| BANK_ACCOUNT_NAME | BankAccountBankAccountName | ✅ |
| BANK_ACCOUNT_NAME_ALT | BankAccountBankAccountNameAlt | — |
| BANK_ACCOUNT_TYPE | BankAccountBankAccountType | ✅ |
| BANK_ID | BankAccountBankId | — |
| BRANCH_ID | BankAccountBranchId | — |
| CHECK_DIGITS | BankAccountCheckDigits | — |
| COUNTRY_CODE | BankAccountCountryCode | — |
| CREATED_BY | BankAccountCreatedBy | ✅ |
| CREATION_DATE | BankAccountCreationDate | ✅ |
| CURRENCY_CODE | BankAccountCurrencyCode | ✅ |
| DESCRIPTION | BankAccountDescription | — |
| ENCRYPTED | BankAccountEncrypted | — |
| END_DATE | BankAccountEndDate | — |
| EXCHANGE_RATE | BankAccountExchangeRate | — |
| EXCHANGE_RATE_AGREEMENT_NUM | BankAccountExchangeRateAgreementNum | — |
| EXCHANGE_RATE_AGREEMENT_TYPE | BankAccountExchangeRateAgreementType | — |
| EXT_BANK_ACCOUNT_ID | ExtBankAccountId | ✅ |
| FOREIGN_PAYMENT_USE_FLAG | BankAccountForeignPaymentUseFlag | — |
| HEDGING_CONTRACT_REFERENCE | BankAccountHedgingContractReference | — |
| IBAN | BankAccountIban | — |
| IBAN_HASH1 | BankAccountIbanHash1 | — |
| IBAN_HASH2 | BankAccountIbanHash2 | — |
| IBAN_SEC_SEGMENT_ID | BankAccountIbanSecSegmentId | — |
| LAST_UPDATE_DATE | BankAccountLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BankAccountLastUpdateLogin | — |
| LAST_UPDATED_BY | BankAccountLastUpdatedBy | ✅ |
| MASKED_BANK_ACCOUNT_NUM | BankAccountMaskedBankAccountNum | ✅ |
| MASKED_IBAN | BankAccountMaskedIban | ✅ |
| OBJECT_VERSION_NUMBER | BankAccountObjectVersionNumber | — |
| PAYMENT_FACTOR_FLAG | BankAccountPaymentFactorFlag | — |
| PROGRAM_APPLICATION_ID | BankAccountProgramApplicationId | — |
| PROGRAM_ID | BankAccountProgramId | — |
| PROGRAM_UPDATE_DATE | BankAccountProgramUpdateDate | — |
| REQUEST_ID | BankAccountRequestId | — |
| SALT_VERSION | BankAccountSaltVersion | — |
| SECONDARY_ACCOUNT_REFERENCE | BankAccountSecondaryAccountReference | — |
| SHORT_ACCT_NAME | BankAccountShortAcctName | — |
| START_DATE | BankAccountStartDate | — |

### [[supplierbankaccountpvo|SupplierBankAccountPVO]] (PO · BICC: 10/45)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASSIFICATION | BankAccountAccountClassification | — |
| ACCOUNT_SUFFIX | BankAccountAccountSuffix | — |
| AGENCY_LOCATION_CODE | BankAccountAgencyLocationCode | — |
| BA_MASK_SETTING | BankAccountBaMaskSetting | — |
| BA_NUM_ELEC_SEC_SEGMENT_ID | BankAccountBaNumElecSecSegmentId | — |
| BA_NUM_SEC_SEGMENT_ID | BankAccountBaNumSecSegmentId | — |
| BA_UNMASK_LENGTH | BankAccountBaUnmaskLength | — |
| BANK_ACCOUNT_NAME | BankAccountBankAccountName | ✅ |
| BANK_ACCOUNT_NAME_ALT | BankAccountBankAccountNameAlt | — |
| BANK_ACCOUNT_TYPE | BankAccountBankAccountType | ✅ |
| BANK_ID | BankAccountBankId | — |
| BRANCH_ID | BankAccountBranchId | — |
| CHECK_DIGITS | BankAccountCheckDigits | — |
| COUNTRY_CODE | BankAccountCountryCode | — |
| CREATED_BY | BankAccountCreatedBy | ✅ |
| CREATION_DATE | BankAccountCreationDate | ✅ |
| CURRENCY_CODE | BankAccountCurrencyCode | ✅ |
| DESCRIPTION | BankAccountDescription | — |
| ENCRYPTED | BankAccountEncrypted | — |
| END_DATE | BankAccountEndDate | — |
| EXCHANGE_RATE | BankAccountExchangeRate | — |
| EXCHANGE_RATE_AGREEMENT_NUM | BankAccountExchangeRateAgreementNum | — |
| EXCHANGE_RATE_AGREEMENT_TYPE | BankAccountExchangeRateAgreementType | — |
| EXT_BANK_ACCOUNT_ID | ExtBankAccountId | ✅ |
| FOREIGN_PAYMENT_USE_FLAG | BankAccountForeignPaymentUseFlag | — |
| HEDGING_CONTRACT_REFERENCE | BankAccountHedgingContractReference | — |
| IBAN | BankAccountIban | — |
| IBAN_HASH1 | BankAccountIbanHash1 | — |
| IBAN_HASH2 | BankAccountIbanHash2 | — |
| IBAN_SEC_SEGMENT_ID | BankAccountIbanSecSegmentId | — |
| LAST_UPDATE_DATE | BankAccountLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BankAccountLastUpdateLogin | — |
| LAST_UPDATED_BY | BankAccountLastUpdatedBy | ✅ |
| MASKED_BANK_ACCOUNT_NUM | BankAccountMaskedBankAccountNum | ✅ |
| MASKED_IBAN | BankAccountMaskedIban | ✅ |
| OBJECT_VERSION_NUMBER | BankAccountObjectVersionNumber | — |
| PAYMENT_FACTOR_FLAG | BankAccountPaymentFactorFlag | — |
| PROGRAM_APPLICATION_ID | BankAccountProgramApplicationId | — |
| PROGRAM_ID | BankAccountProgramId | — |
| PROGRAM_UPDATE_DATE | BankAccountProgramUpdateDate | — |
| REQUEST_ID | BankAccountRequestId | — |
| SALT_VERSION | BankAccountSaltVersion | — |
| SECONDARY_ACCOUNT_REFERENCE | BankAccountSecondaryAccountReference | — |
| SHORT_ACCT_NAME | BankAccountShortAcctName | — |
| START_DATE | BankAccountStartDate | — |

### [[suppliersitebankaccountpvo|SupplierSiteBankAccountPVO]] (PO · BICC: 10/45)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASSIFICATION | BankAccountAccountClassification | — |
| ACCOUNT_SUFFIX | BankAccountAccountSuffix | — |
| AGENCY_LOCATION_CODE | BankAccountAgencyLocationCode | — |
| BA_MASK_SETTING | BankAccountBaMaskSetting | — |
| BA_NUM_ELEC_SEC_SEGMENT_ID | BankAccountBaNumElecSecSegmentId | — |
| BA_NUM_SEC_SEGMENT_ID | BankAccountBaNumSecSegmentId | — |
| BA_UNMASK_LENGTH | BankAccountBaUnmaskLength | — |
| BANK_ACCOUNT_NAME | BankAccountBankAccountName | ✅ |
| BANK_ACCOUNT_NAME_ALT | BankAccountBankAccountNameAlt | — |
| BANK_ACCOUNT_TYPE | BankAccountBankAccountType | ✅ |
| BANK_ID | BankAccountBankId | — |
| BRANCH_ID | BankAccountBranchId | — |
| CHECK_DIGITS | BankAccountCheckDigits | — |
| COUNTRY_CODE | BankAccountCountryCode | — |
| CREATED_BY | BankAccountCreatedBy | ✅ |
| CREATION_DATE | BankAccountCreationDate | ✅ |
| CURRENCY_CODE | BankAccountCurrencyCode | ✅ |
| DESCRIPTION | BankAccountDescription | — |
| ENCRYPTED | BankAccountEncrypted | — |
| END_DATE | BankAccountEndDate | — |
| EXCHANGE_RATE | BankAccountExchangeRate | — |
| EXCHANGE_RATE_AGREEMENT_NUM | BankAccountExchangeRateAgreementNum | — |
| EXCHANGE_RATE_AGREEMENT_TYPE | BankAccountExchangeRateAgreementType | — |
| EXT_BANK_ACCOUNT_ID | ExtBankAccountId | ✅ |
| FOREIGN_PAYMENT_USE_FLAG | BankAccountForeignPaymentUseFlag | — |
| HEDGING_CONTRACT_REFERENCE | BankAccountHedgingContractReference | — |
| IBAN | BankAccountIban | — |
| IBAN_HASH1 | BankAccountIbanHash1 | — |
| IBAN_HASH2 | BankAccountIbanHash2 | — |
| IBAN_SEC_SEGMENT_ID | BankAccountIbanSecSegmentId | — |
| LAST_UPDATE_DATE | BankAccountLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BankAccountLastUpdateLogin | — |
| LAST_UPDATED_BY | BankAccountLastUpdatedBy | ✅ |
| MASKED_BANK_ACCOUNT_NUM | BankAccountMaskedBankAccountNum | ✅ |
| MASKED_IBAN | BankAccountMaskedIban | ✅ |
| OBJECT_VERSION_NUMBER | BankAccountObjectVersionNumber | — |
| PAYMENT_FACTOR_FLAG | BankAccountPaymentFactorFlag | — |
| PROGRAM_APPLICATION_ID | BankAccountProgramApplicationId | — |
| PROGRAM_ID | BankAccountProgramId | — |
| PROGRAM_UPDATE_DATE | BankAccountProgramUpdateDate | — |
| REQUEST_ID | BankAccountRequestId | — |
| SALT_VERSION | BankAccountSaltVersion | — |
| SECONDARY_ACCOUNT_REFERENCE | BankAccountSecondaryAccountReference | — |
| SHORT_ACCT_NAME | BankAccountShortAcctName | — |
| START_DATE | BankAccountStartDate | — |

### [[transactionheaderbillsreceivablepvo|TransactionHeaderBillsReceivablePVO]] (AR · BICC: 1/49)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASSIFICATION | ExtBankAccountAccountClassification | — |
| ACCOUNT_SUFFIX | ExtBankAccountAccountSuffix | — |
| AGENCY_LOCATION_CODE | ExtBankAccountAgencyLocationCode | — |
| BA_MASK_SETTING | ExtBankAccountBaMaskSetting | — |
| BA_NUM_ELEC_SEC_SEGMENT_ID | ExtBankAccountBaNumElecSecSegmentId | — |
| BA_NUM_SEC_SEGMENT_ID | ExtBankAccountBaNumSecSegmentId | — |
| BA_UNMASK_LENGTH | ExtBankAccountBaUnmaskLength | — |
| BANK_ACCOUNT_NAME | ExtBankAccountBankAccountName | — |
| BANK_ACCOUNT_NAME_ALT | ExtBankAccountBankAccountNameAlt | — |
| BANK_ACCOUNT_NUM | ExtBankAccountBankAccountNum | — |
| BANK_ACCOUNT_NUM_ELECTRONIC | ExtBankAccountBankAccountNumElectronic | — |
| BANK_ACCOUNT_NUM_HASH1 | ExtBankAccountBankAccountNumHash1 | — |
| BANK_ACCOUNT_NUM_HASH2 | ExtBankAccountBankAccountNumHash2 | — |
| BANK_ACCOUNT_TYPE | ExtBankAccountBankAccountType | — |
| BANK_ID | ExtBankAccountBankId | — |
| BRANCH_ID | ExtBankAccountBranchId | — |
| CHECK_DIGITS | ExtBankAccountCheckDigits | — |
| COUNTRY_CODE | ExtBankAccountCountryCode | — |
| CREATED_BY | ExtBankAccountCreatedBy | — |
| CREATION_DATE | ExtBankAccountCreationDate | — |
| CURRENCY_CODE | ExtBankAccountCurrencyCode | — |
| DESCRIPTION | ExtBankAccountDescription | — |
| ENCRYPTED | ExtBankAccountEncrypted | — |
| END_DATE | ExtBankAccountEndDate | — |
| EXCHANGE_RATE | ExtBankAccountExchangeRate | — |
| EXCHANGE_RATE_AGREEMENT_NUM | ExtBankAccountExchangeRateAgreementNum | — |
| EXCHANGE_RATE_AGREEMENT_TYPE | ExtBankAccountExchangeRateAgreementType | — |
| EXT_BANK_ACCOUNT_ID | ExtBankAccountExtBankAccountId | — |
| FOREIGN_PAYMENT_USE_FLAG | ExtBankAccountForeignPaymentUseFlag | — |
| HEDGING_CONTRACT_REFERENCE | ExtBankAccountHedgingContractReference | — |
| IBAN | ExtBankAccountIban | — |
| IBAN_HASH1 | ExtBankAccountIbanHash1 | — |
| IBAN_HASH2 | ExtBankAccountIbanHash2 | — |
| IBAN_SEC_SEGMENT_ID | ExtBankAccountIbanSecSegmentId | — |
| LAST_UPDATE_DATE | ExtBankAccountLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExtBankAccountLastUpdateLogin | — |
| LAST_UPDATED_BY | ExtBankAccountLastUpdatedBy | — |
| MASKED_BANK_ACCOUNT_NUM | ExtBankAccountMaskedBankAccountNum | — |
| MASKED_IBAN | ExtBankAccountMaskedIban | — |
| OBJECT_VERSION_NUMBER | ExtBankAccountObjectVersionNumber | — |
| PAYMENT_FACTOR_FLAG | ExtBankAccountPaymentFactorFlag | — |
| PROGRAM_APPLICATION_ID | ExtBankAccountProgramApplicationId | — |
| PROGRAM_ID | ExtBankAccountProgramId | — |
| PROGRAM_UPDATE_DATE | ExtBankAccountProgramUpdateDate | — |
| REQUEST_ID | ExtBankAccountRequestId | — |
| SALT_VERSION | ExtBankAccountSaltVersion | — |
| SECONDARY_ACCOUNT_REFERENCE | ExtBankAccountSecondaryAccountReference | — |
| SHORT_ACCT_NAME | ExtBankAccountShortAcctName | — |
| START_DATE | ExtBankAccountStartDate | — |

### [[transactionheadernovcpvo|TransactionHeaderNoVCPVO]] (AR · BICC: 1/49)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASSIFICATION | ExtBankAccountAccountClassification | — |
| ACCOUNT_SUFFIX | ExtBankAccountAccountSuffix | — |
| AGENCY_LOCATION_CODE | ExtBankAccountAgencyLocationCode | — |
| BA_MASK_SETTING | ExtBankAccountBaMaskSetting | — |
| BA_NUM_ELEC_SEC_SEGMENT_ID | ExtBankAccountBaNumElecSecSegmentId | — |
| BA_NUM_SEC_SEGMENT_ID | ExtBankAccountBaNumSecSegmentId | — |
| BA_UNMASK_LENGTH | ExtBankAccountBaUnmaskLength | — |
| BANK_ACCOUNT_NAME | ExtBankAccountBankAccountName | — |
| BANK_ACCOUNT_NAME_ALT | ExtBankAccountBankAccountNameAlt | — |
| BANK_ACCOUNT_NUM | ExtBankAccountBankAccountNum | — |
| BANK_ACCOUNT_NUM_ELECTRONIC | ExtBankAccountBankAccountNumElectronic | — |
| BANK_ACCOUNT_NUM_HASH1 | ExtBankAccountBankAccountNumHash1 | — |
| BANK_ACCOUNT_NUM_HASH2 | ExtBankAccountBankAccountNumHash2 | — |
| BANK_ACCOUNT_TYPE | ExtBankAccountBankAccountType | — |
| BANK_ID | ExtBankAccountBankId | — |
| BRANCH_ID | ExtBankAccountBranchId | — |
| CHECK_DIGITS | ExtBankAccountCheckDigits | — |
| COUNTRY_CODE | ExtBankAccountCountryCode | — |
| CREATED_BY | ExtBankAccountCreatedBy | — |
| CREATION_DATE | ExtBankAccountCreationDate | — |
| CURRENCY_CODE | ExtBankAccountCurrencyCode | — |
| DESCRIPTION | ExtBankAccountDescription | — |
| ENCRYPTED | ExtBankAccountEncrypted | — |
| END_DATE | ExtBankAccountEndDate | — |
| EXCHANGE_RATE | ExtBankAccountExchangeRate | — |
| EXCHANGE_RATE_AGREEMENT_NUM | ExtBankAccountExchangeRateAgreementNum | — |
| EXCHANGE_RATE_AGREEMENT_TYPE | ExtBankAccountExchangeRateAgreementType | — |
| EXT_BANK_ACCOUNT_ID | ExtBankAccountExtBankAccountId | — |
| FOREIGN_PAYMENT_USE_FLAG | ExtBankAccountForeignPaymentUseFlag | — |
| HEDGING_CONTRACT_REFERENCE | ExtBankAccountHedgingContractReference | — |
| IBAN | ExtBankAccountIban | — |
| IBAN_HASH1 | ExtBankAccountIbanHash1 | — |
| IBAN_HASH2 | ExtBankAccountIbanHash2 | — |
| IBAN_SEC_SEGMENT_ID | ExtBankAccountIbanSecSegmentId | — |
| LAST_UPDATE_DATE | ExtBankAccountLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExtBankAccountLastUpdateLogin | — |
| LAST_UPDATED_BY | ExtBankAccountLastUpdatedBy | — |
| MASKED_BANK_ACCOUNT_NUM | ExtBankAccountMaskedBankAccountNum | — |
| MASKED_IBAN | ExtBankAccountMaskedIban | — |
| OBJECT_VERSION_NUMBER | ExtBankAccountObjectVersionNumber | — |
| PAYMENT_FACTOR_FLAG | ExtBankAccountPaymentFactorFlag | — |
| PROGRAM_APPLICATION_ID | ExtBankAccountProgramApplicationId | — |
| PROGRAM_ID | ExtBankAccountProgramId | — |
| PROGRAM_UPDATE_DATE | ExtBankAccountProgramUpdateDate | — |
| REQUEST_ID | ExtBankAccountRequestId | — |
| SALT_VERSION | ExtBankAccountSaltVersion | — |
| SECONDARY_ACCOUNT_REFERENCE | ExtBankAccountSecondaryAccountReference | — |
| SHORT_ACCT_NAME | ExtBankAccountShortAcctName | — |
| START_DATE | ExtBankAccountStartDate | — |

### [[transactionheaderpvo|TransactionHeaderPVO]] (AR · BICC: 3/49)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASSIFICATION | ExtBankAccountAccountClassification | — |
| ACCOUNT_SUFFIX | ExtBankAccountAccountSuffix | — |
| AGENCY_LOCATION_CODE | ExtBankAccountAgencyLocationCode | — |
| BA_MASK_SETTING | ExtBankAccountBaMaskSetting | — |
| BA_NUM_ELEC_SEC_SEGMENT_ID | ExtBankAccountBaNumElecSecSegmentId | — |
| BA_NUM_SEC_SEGMENT_ID | ExtBankAccountBaNumSecSegmentId | — |
| BA_UNMASK_LENGTH | ExtBankAccountBaUnmaskLength | — |
| BANK_ACCOUNT_NAME | ExtBankAccountBankAccountName | ✅ |
| BANK_ACCOUNT_NAME_ALT | ExtBankAccountBankAccountNameAlt | — |
| BANK_ACCOUNT_NUM | ExtBankAccountBankAccountNum | ✅ |
| BANK_ACCOUNT_NUM_ELECTRONIC | ExtBankAccountBankAccountNumElectronic | — |
| BANK_ACCOUNT_NUM_HASH1 | ExtBankAccountBankAccountNumHash1 | — |
| BANK_ACCOUNT_NUM_HASH2 | ExtBankAccountBankAccountNumHash2 | — |
| BANK_ACCOUNT_TYPE | ExtBankAccountBankAccountType | — |
| BANK_ID | ExtBankAccountBankId | — |
| BRANCH_ID | ExtBankAccountBranchId | — |
| CHECK_DIGITS | ExtBankAccountCheckDigits | — |
| COUNTRY_CODE | ExtBankAccountCountryCode | — |
| CREATED_BY | ExtBankAccountCreatedBy | — |
| CREATION_DATE | ExtBankAccountCreationDate | — |
| CURRENCY_CODE | ExtBankAccountCurrencyCode | — |
| DESCRIPTION | ExtBankAccountDescription | — |
| ENCRYPTED | ExtBankAccountEncrypted | — |
| END_DATE | ExtBankAccountEndDate | — |
| EXCHANGE_RATE | ExtBankAccountExchangeRate | — |
| EXCHANGE_RATE_AGREEMENT_NUM | ExtBankAccountExchangeRateAgreementNum | — |
| EXCHANGE_RATE_AGREEMENT_TYPE | ExtBankAccountExchangeRateAgreementType | — |
| EXT_BANK_ACCOUNT_ID | ExtBankAccountExtBankAccountId | — |
| FOREIGN_PAYMENT_USE_FLAG | ExtBankAccountForeignPaymentUseFlag | — |
| HEDGING_CONTRACT_REFERENCE | ExtBankAccountHedgingContractReference | — |
| IBAN | ExtBankAccountIban | — |
| IBAN_HASH1 | ExtBankAccountIbanHash1 | — |
| IBAN_HASH2 | ExtBankAccountIbanHash2 | — |
| IBAN_SEC_SEGMENT_ID | ExtBankAccountIbanSecSegmentId | — |
| LAST_UPDATE_DATE | ExtBankAccountLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExtBankAccountLastUpdateLogin | — |
| LAST_UPDATED_BY | ExtBankAccountLastUpdatedBy | — |
| MASKED_BANK_ACCOUNT_NUM | ExtBankAccountMaskedBankAccountNum | — |
| MASKED_IBAN | ExtBankAccountMaskedIban | — |
| OBJECT_VERSION_NUMBER | ExtBankAccountObjectVersionNumber | — |
| PAYMENT_FACTOR_FLAG | ExtBankAccountPaymentFactorFlag | — |
| PROGRAM_APPLICATION_ID | ExtBankAccountProgramApplicationId | — |
| PROGRAM_ID | ExtBankAccountProgramId | — |
| PROGRAM_UPDATE_DATE | ExtBankAccountProgramUpdateDate | — |
| REQUEST_ID | ExtBankAccountRequestId | — |
| SALT_VERSION | ExtBankAccountSaltVersion | — |
| SECONDARY_ACCOUNT_REFERENCE | ExtBankAccountSecondaryAccountReference | — |
| SHORT_ACCT_NAME | ExtBankAccountShortAcctName | — |
| START_DATE | ExtBankAccountStartDate | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR · BICC: 1/47)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASSIFICATION | IbyExtBankAccountsAccountClassification | — |
| ACCOUNT_SUFFIX | IbyExtBankAccountsAccountSuffix | — |
| AGENCY_LOCATION_CODE | IbyExtBankAccountsAgencyLocationCode | — |
| BA_MASK_SETTING | IbyExtBankAccountsBaMaskSetting | — |
| BA_NUM_ELEC_SEC_SEGMENT_ID | IbyExtBankAccountsBaNumElecSecSegmentId | — |
| BA_NUM_SEC_SEGMENT_ID | IbyExtBankAccountsBaNumSecSegmentId | — |
| BA_UNMASK_LENGTH | IbyExtBankAccountsBaUnmaskLength | — |
| BANK_ACCOUNT_NAME | DraweeBankAccountBankAccountName | — |
| BANK_ACCOUNT_NAME | IbyExtBankAccountsBankAccountName | — |
| BANK_ACCOUNT_NAME_ALT | IbyExtBankAccountsBankAccountNameAlt | — |
| BANK_ACCOUNT_NUM | DraweeBankAccountBankAccountNum | ✅ |
| BANK_ACCOUNT_NUM | IbyExtBankAccountsBankAccountNum | — |
| BANK_ACCOUNT_NUM_ELECTRONIC | IbyExtBankAccountsBankAccountNumElectronic | — |
| BANK_ACCOUNT_NUM_HASH1 | IbyExtBankAccountsBankAccountNumHash1 | — |
| BANK_ACCOUNT_NUM_HASH2 | IbyExtBankAccountsBankAccountNumHash2 | — |
| BANK_ACCOUNT_TYPE | IbyExtBankAccountsBankAccountType | — |
| BANK_ID | IbyExtBankAccountsBankId | — |
| BRANCH_ID | IbyExtBankAccountsBranchId | — |
| CHECK_DIGITS | IbyExtBankAccountsCheckDigits | — |
| COUNTRY_CODE | IbyExtBankAccountsCountryCode | — |
| CURRENCY_CODE | IbyExtBankAccountsCurrencyCode | — |
| DESCRIPTION | IbyExtBankAccountsDescription | — |
| ENCRYPTED | IbyExtBankAccountsEncrypted | — |
| END_DATE | IbyExtBankAccountsEndDate | — |
| EXCHANGE_RATE | IbyExtBankAccountsExchangeRate | — |
| EXCHANGE_RATE_AGREEMENT_NUM | IbyExtBankAccountsExchangeRateAgreementNum | — |
| EXCHANGE_RATE_AGREEMENT_TYPE | IbyExtBankAccountsExchangeRateAgreementType | — |
| EXT_BANK_ACCOUNT_ID | DraweeBankAccountExtBankAccountId | — |
| EXT_BANK_ACCOUNT_ID | IbyExtBankAccountsExtBankAccountId | — |
| FOREIGN_PAYMENT_USE_FLAG | IbyExtBankAccountsForeignPaymentUseFlag | — |
| HEDGING_CONTRACT_REFERENCE | IbyExtBankAccountsHedgingContractReference | — |
| IBAN | IbyExtBankAccountsIban | — |
| IBAN_HASH1 | IbyExtBankAccountsIbanHash1 | — |
| IBAN_HASH2 | IbyExtBankAccountsIbanHash2 | — |
| IBAN_SEC_SEGMENT_ID | IbyExtBankAccountsIbanSecSegmentId | — |
| MASKED_BANK_ACCOUNT_NUM | IbyExtBankAccountsMaskedBankAccountNum | — |
| MASKED_IBAN | IbyExtBankAccountsMaskedIban | — |
| OBJECT_VERSION_NUMBER | IbyExtBankAccountsObjectVersionNumber3 | — |
| PAYMENT_FACTOR_FLAG | IbyExtBankAccountsPaymentFactorFlag | — |
| PROGRAM_APPLICATION_ID | IbyExtBankAccountsProgramApplicationId | — |
| PROGRAM_ID | IbyExtBankAccountsProgramId | — |
| PROGRAM_UPDATE_DATE | IbyExtBankAccountsProgramUpdateDate | — |
| REQUEST_ID | IbyExtBankAccountsRequestId | — |
| SALT_VERSION | IbyExtBankAccountsSaltVersion | — |
| SECONDARY_ACCOUNT_REFERENCE | IbyExtBankAccountsSecondaryAccountReference | — |
| SHORT_ACCT_NAME | IbyExtBankAccountsShortAcctName | — |
| START_DATE | IbyExtBankAccountsStartDate | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR · BICC: 1/47)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASSIFICATION | IbyExtBankAccountsAccountClassification | — |
| ACCOUNT_SUFFIX | IbyExtBankAccountsAccountSuffix | — |
| AGENCY_LOCATION_CODE | IbyExtBankAccountsAgencyLocationCode | — |
| BA_MASK_SETTING | IbyExtBankAccountsBaMaskSetting | — |
| BA_NUM_ELEC_SEC_SEGMENT_ID | IbyExtBankAccountsBaNumElecSecSegmentId | — |
| BA_NUM_SEC_SEGMENT_ID | IbyExtBankAccountsBaNumSecSegmentId | — |
| BA_UNMASK_LENGTH | IbyExtBankAccountsBaUnmaskLength | — |
| BANK_ACCOUNT_NAME | DraweeBankAccountBankAccountName | — |
| BANK_ACCOUNT_NAME | IbyExtBankAccountsBankAccountName | — |
| BANK_ACCOUNT_NAME_ALT | IbyExtBankAccountsBankAccountNameAlt | — |
| BANK_ACCOUNT_NUM | DraweeBankAccountBankAccountNum | ✅ |
| BANK_ACCOUNT_NUM | IbyExtBankAccountsBankAccountNum | — |
| BANK_ACCOUNT_NUM_ELECTRONIC | IbyExtBankAccountsBankAccountNumElectronic | — |
| BANK_ACCOUNT_NUM_HASH1 | IbyExtBankAccountsBankAccountNumHash1 | — |
| BANK_ACCOUNT_NUM_HASH2 | IbyExtBankAccountsBankAccountNumHash2 | — |
| BANK_ACCOUNT_TYPE | IbyExtBankAccountsBankAccountType | — |
| BANK_ID | IbyExtBankAccountsBankId | — |
| BRANCH_ID | IbyExtBankAccountsBranchId | — |
| CHECK_DIGITS | IbyExtBankAccountsCheckDigits | — |
| COUNTRY_CODE | IbyExtBankAccountsCountryCode | — |
| CURRENCY_CODE | IbyExtBankAccountsCurrencyCode | — |
| DESCRIPTION | IbyExtBankAccountsDescription | — |
| ENCRYPTED | IbyExtBankAccountsEncrypted | — |
| END_DATE | IbyExtBankAccountsEndDate | — |
| EXCHANGE_RATE | IbyExtBankAccountsExchangeRate | — |
| EXCHANGE_RATE_AGREEMENT_NUM | IbyExtBankAccountsExchangeRateAgreementNum | — |
| EXCHANGE_RATE_AGREEMENT_TYPE | IbyExtBankAccountsExchangeRateAgreementType | — |
| EXT_BANK_ACCOUNT_ID | DraweeBankAccountExtBankAccountId | — |
| EXT_BANK_ACCOUNT_ID | IbyExtBankAccountsExtBankAccountId | — |
| FOREIGN_PAYMENT_USE_FLAG | IbyExtBankAccountsForeignPaymentUseFlag | — |
| HEDGING_CONTRACT_REFERENCE | IbyExtBankAccountsHedgingContractReference | — |
| IBAN | IbyExtBankAccountsIban | — |
| IBAN_HASH1 | IbyExtBankAccountsIbanHash1 | — |
| IBAN_HASH2 | IbyExtBankAccountsIbanHash2 | — |
| IBAN_SEC_SEGMENT_ID | IbyExtBankAccountsIbanSecSegmentId | — |
| MASKED_BANK_ACCOUNT_NUM | IbyExtBankAccountsMaskedBankAccountNum | — |
| MASKED_IBAN | IbyExtBankAccountsMaskedIban | — |
| OBJECT_VERSION_NUMBER | IbyExtBankAccountsObjectVersionNumber3 | — |
| PAYMENT_FACTOR_FLAG | IbyExtBankAccountsPaymentFactorFlag | — |
| PROGRAM_APPLICATION_ID | IbyExtBankAccountsProgramApplicationId | — |
| PROGRAM_ID | IbyExtBankAccountsProgramId | — |
| PROGRAM_UPDATE_DATE | IbyExtBankAccountsProgramUpdateDate | — |
| REQUEST_ID | IbyExtBankAccountsRequestId | — |
| SALT_VERSION | IbyExtBankAccountsSaltVersion | — |
| SECONDARY_ACCOUNT_REFERENCE | IbyExtBankAccountsSecondaryAccountReference | — |
| SHORT_ACCT_NAME | IbyExtBankAccountsShortAcctName | — |
| START_DATE | IbyExtBankAccountsStartDate | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASSIFICATION | IbyExtBankAccountsAccountClassification | — |
| ACCOUNT_SUFFIX | IbyExtBankAccountsAccountSuffix | — |
| AGENCY_LOCATION_CODE | IbyExtBankAccountsAgencyLocationCode | — |
| BA_MASK_SETTING | IbyExtBankAccountsBaMaskSetting | — |
| BA_NUM_ELEC_SEC_SEGMENT_ID | IbyExtBankAccountsBaNumElecSecSegmentId | — |
| BA_NUM_SEC_SEGMENT_ID | IbyExtBankAccountsBaNumSecSegmentId | — |
| BA_UNMASK_LENGTH | IbyExtBankAccountsBaUnmaskLength | — |
| BANK_ACCOUNT_NAME | IbyExtBankAccountsBankAccountName | — |
| BANK_ACCOUNT_NAME_ALT | IbyExtBankAccountsBankAccountNameAlt | — |
| BANK_ACCOUNT_NUM | IbyExtBankAccountsBankAccountNum | — |
| BANK_ACCOUNT_NUM_ELECTRONIC | IbyExtBankAccountsBankAccountNumElectronic | — |
| BANK_ACCOUNT_NUM_HASH1 | IbyExtBankAccountsBankAccountNumHash1 | — |
| BANK_ACCOUNT_NUM_HASH2 | IbyExtBankAccountsBankAccountNumHash2 | — |
| BANK_ACCOUNT_TYPE | IbyExtBankAccountsBankAccountType | — |
| BANK_ID | IbyExtBankAccountsBankId | — |
| BRANCH_ID | IbyExtBankAccountsBranchId | — |
| CHECK_DIGITS | IbyExtBankAccountsCheckDigits | — |
| COUNTRY_CODE | IbyExtBankAccountsCountryCode | — |
| CURRENCY_CODE | IbyExtBankAccountsCurrencyCode | — |
| DESCRIPTION | IbyExtBankAccountsDescription | — |
| ENCRYPTED | IbyExtBankAccountsEncrypted | — |
| END_DATE | IbyExtBankAccountsEndDate | — |
| EXCHANGE_RATE | IbyExtBankAccountsExchangeRate | — |
| EXCHANGE_RATE_AGREEMENT_NUM | IbyExtBankAccountsExchangeRateAgreementNum | — |
| EXCHANGE_RATE_AGREEMENT_TYPE | IbyExtBankAccountsExchangeRateAgreementType | — |
| EXT_BANK_ACCOUNT_ID | IbyExtBankAccountsExtBankAccountId | — |
| FOREIGN_PAYMENT_USE_FLAG | IbyExtBankAccountsForeignPaymentUseFlag | — |
| HEDGING_CONTRACT_REFERENCE | IbyExtBankAccountsHedgingContractReference | — |
| IBAN | IbyExtBankAccountsIban | — |
| IBAN_HASH1 | IbyExtBankAccountsIbanHash1 | — |
| IBAN_HASH2 | IbyExtBankAccountsIbanHash2 | — |
| IBAN_SEC_SEGMENT_ID | IbyExtBankAccountsIbanSecSegmentId | — |
| MASKED_BANK_ACCOUNT_NUM | IbyExtBankAccountsMaskedBankAccountNum | — |
| MASKED_IBAN | IbyExtBankAccountsMaskedIban | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PAYMENT_FACTOR_FLAG | IbyExtBankAccountsPaymentFactorFlag | — |
| PROGRAM_APPLICATION_ID | IbyExtBankAccountsProgramApplicationId | — |
| PROGRAM_ID | IbyExtBankAccountsProgramId | — |
| PROGRAM_UPDATE_DATE | IbyExtBankAccountsProgramUpdateDate | — |
| REQUEST_ID | IbyExtBankAccountsRequestId | — |
| SALT_VERSION | IbyExtBankAccountsSaltVersion | — |
| SECONDARY_ACCOUNT_REFERENCE | IbyExtBankAccountsSecondaryAccountReference | — |
| SHORT_ACCT_NAME | IbyExtBankAccountsShortAcctName | — |
| START_DATE | IbyExtBankAccountsStartDate | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR · BICC: 2/44)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASSIFICATION | IbyExtBankAccountsAccountClassification | — |
| ACCOUNT_SUFFIX | IbyExtBankAccountsAccountSuffix | — |
| AGENCY_LOCATION_CODE | IbyExtBankAccountsAgencyLocationCode | — |
| BA_MASK_SETTING | IbyExtBankAccountsBaMaskSetting | — |
| BA_NUM_ELEC_SEC_SEGMENT_ID | IbyExtBankAccountsBaNumElecSecSegmentId | — |
| BA_NUM_SEC_SEGMENT_ID | IbyExtBankAccountsBaNumSecSegmentId | — |
| BA_UNMASK_LENGTH | IbyExtBankAccountsBaUnmaskLength | — |
| BANK_ACCOUNT_NAME | IbyExtBankAccountsBankAccountName | ✅ |
| BANK_ACCOUNT_NAME_ALT | IbyExtBankAccountsBankAccountNameAlt | — |
| BANK_ACCOUNT_NUM | IbyExtBankAccountsBankAccountNum | ✅ |
| BANK_ACCOUNT_NUM_ELECTRONIC | IbyExtBankAccountsBankAccountNumElectronic | — |
| BANK_ACCOUNT_NUM_HASH1 | IbyExtBankAccountsBankAccountNumHash1 | — |
| BANK_ACCOUNT_NUM_HASH2 | IbyExtBankAccountsBankAccountNumHash2 | — |
| BANK_ACCOUNT_TYPE | IbyExtBankAccountsBankAccountType | — |
| BANK_ID | IbyExtBankAccountsBankId | — |
| BRANCH_ID | IbyExtBankAccountsBranchId | — |
| CHECK_DIGITS | IbyExtBankAccountsCheckDigits | — |
| COUNTRY_CODE | IbyExtBankAccountsCountryCode | — |
| CURRENCY_CODE | IbyExtBankAccountsCurrencyCode | — |
| DESCRIPTION | IbyExtBankAccountsDescription | — |
| ENCRYPTED | IbyExtBankAccountsEncrypted | — |
| END_DATE | IbyExtBankAccountsEndDate | — |
| EXCHANGE_RATE | IbyExtBankAccountsExchangeRate | — |
| EXCHANGE_RATE_AGREEMENT_NUM | IbyExtBankAccountsExchangeRateAgreementNum | — |
| EXCHANGE_RATE_AGREEMENT_TYPE | IbyExtBankAccountsExchangeRateAgreementType | — |
| EXT_BANK_ACCOUNT_ID | IbyExtBankAccountsExtBankAccountId | — |
| FOREIGN_PAYMENT_USE_FLAG | IbyExtBankAccountsForeignPaymentUseFlag | — |
| HEDGING_CONTRACT_REFERENCE | IbyExtBankAccountsHedgingContractReference | — |
| IBAN | IbyExtBankAccountsIban | — |
| IBAN_HASH1 | IbyExtBankAccountsIbanHash1 | — |
| IBAN_HASH2 | IbyExtBankAccountsIbanHash2 | — |
| IBAN_SEC_SEGMENT_ID | IbyExtBankAccountsIbanSecSegmentId | — |
| MASKED_BANK_ACCOUNT_NUM | IbyExtBankAccountsMaskedBankAccountNum | — |
| MASKED_IBAN | IbyExtBankAccountsMaskedIban | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PAYMENT_FACTOR_FLAG | IbyExtBankAccountsPaymentFactorFlag | — |
| PROGRAM_APPLICATION_ID | IbyExtBankAccountsProgramApplicationId | — |
| PROGRAM_ID | IbyExtBankAccountsProgramId | — |
| PROGRAM_UPDATE_DATE | IbyExtBankAccountsProgramUpdateDate | — |
| REQUEST_ID | IbyExtBankAccountsRequestId | — |
| SALT_VERSION | IbyExtBankAccountsSaltVersion | — |
| SECONDARY_ACCOUNT_REFERENCE | IbyExtBankAccountsSecondaryAccountReference | — |
| SHORT_ACCT_NAME | IbyExtBankAccountsShortAcctName | — |
| START_DATE | IbyExtBankAccountsStartDate | — |

### [[transactionlinepvo|TransactionLinePVO]] (AR · BICC: 2/44)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASSIFICATION | IbyExtBankAccountsAccountClassification | — |
| ACCOUNT_SUFFIX | IbyExtBankAccountsAccountSuffix | — |
| AGENCY_LOCATION_CODE | IbyExtBankAccountsAgencyLocationCode | — |
| BA_MASK_SETTING | IbyExtBankAccountsBaMaskSetting | — |
| BA_NUM_ELEC_SEC_SEGMENT_ID | IbyExtBankAccountsBaNumElecSecSegmentId | — |
| BA_NUM_SEC_SEGMENT_ID | IbyExtBankAccountsBaNumSecSegmentId | — |
| BA_UNMASK_LENGTH | IbyExtBankAccountsBaUnmaskLength | — |
| BANK_ACCOUNT_NAME | IbyExtBankAccountsBankAccountName | ✅ |
| BANK_ACCOUNT_NAME_ALT | IbyExtBankAccountsBankAccountNameAlt | — |
| BANK_ACCOUNT_NUM | IbyExtBankAccountsBankAccountNum | ✅ |
| BANK_ACCOUNT_NUM_ELECTRONIC | IbyExtBankAccountsBankAccountNumElectronic | — |
| BANK_ACCOUNT_NUM_HASH1 | IbyExtBankAccountsBankAccountNumHash1 | — |
| BANK_ACCOUNT_NUM_HASH2 | IbyExtBankAccountsBankAccountNumHash2 | — |
| BANK_ACCOUNT_TYPE | IbyExtBankAccountsBankAccountType | — |
| BANK_ID | IbyExtBankAccountsBankId | — |
| BRANCH_ID | IbyExtBankAccountsBranchId | — |
| CHECK_DIGITS | IbyExtBankAccountsCheckDigits | — |
| COUNTRY_CODE | IbyExtBankAccountsCountryCode | — |
| CURRENCY_CODE | IbyExtBankAccountsCurrencyCode | — |
| DESCRIPTION | IbyExtBankAccountsDescription | — |
| ENCRYPTED | IbyExtBankAccountsEncrypted | — |
| END_DATE | IbyExtBankAccountsEndDate | — |
| EXCHANGE_RATE | IbyExtBankAccountsExchangeRate | — |
| EXCHANGE_RATE_AGREEMENT_NUM | IbyExtBankAccountsExchangeRateAgreementNum | — |
| EXCHANGE_RATE_AGREEMENT_TYPE | IbyExtBankAccountsExchangeRateAgreementType | — |
| EXT_BANK_ACCOUNT_ID | IbyExtBankAccountsExtBankAccountId | — |
| FOREIGN_PAYMENT_USE_FLAG | IbyExtBankAccountsForeignPaymentUseFlag | — |
| HEDGING_CONTRACT_REFERENCE | IbyExtBankAccountsHedgingContractReference | — |
| IBAN | IbyExtBankAccountsIban | — |
| IBAN_HASH1 | IbyExtBankAccountsIbanHash1 | — |
| IBAN_HASH2 | IbyExtBankAccountsIbanHash2 | — |
| IBAN_SEC_SEGMENT_ID | IbyExtBankAccountsIbanSecSegmentId | — |
| MASKED_BANK_ACCOUNT_NUM | IbyExtBankAccountsMaskedBankAccountNum | — |
| MASKED_IBAN | IbyExtBankAccountsMaskedIban | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PAYMENT_FACTOR_FLAG | IbyExtBankAccountsPaymentFactorFlag | — |
| PROGRAM_APPLICATION_ID | IbyExtBankAccountsProgramApplicationId | — |
| PROGRAM_ID | IbyExtBankAccountsProgramId | — |
| PROGRAM_UPDATE_DATE | IbyExtBankAccountsProgramUpdateDate | — |
| REQUEST_ID | IbyExtBankAccountsRequestId | — |
| SALT_VERSION | IbyExtBankAccountsSaltVersion | — |
| SECONDARY_ACCOUNT_REFERENCE | IbyExtBankAccountsSecondaryAccountReference | — |
| SHORT_ACCT_NAME | IbyExtBankAccountsShortAcctName | — |
| START_DATE | IbyExtBankAccountsStartDate | — |
