---
id: DOC-HCM-066
doc_type: system-doc
title: "CE_BANK_ACCT_USES_ALL — (título a preencher)"
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
  - CE_BANK_ACCT_USES_ALL
  - ce_bank_acct_uses_all
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# CE_BANK_ACCT_USES_ALL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | AP_USE_ENABLE_FLAG | — | — | — | — | — | — |
| 2 | AR_USE_ENABLE_FLAG | — | — | — | — | — | — |
| 3 | AUTHORIZED_FLAG | — | — | — | — | — | — |
| 4 | BANK_ACCOUNT_ID | — | — | — | — | — | — |
| 5 | BANK_ACCT_USE_ID | — | — | — | — | — | — |
| 6 | CREATED_BY | — | — | — | — | — | — |
| 7 | CREATION_DATE | — | — | — | — | — | — |
| 8 | DEFAULT_ACCOUNT_FLAG | — | — | — | — | — | — |
| 9 | EFT_SCRIPT_NAME | — | — | — | — | — | — |
| 10 | END_DATE | — | — | — | — | — | — |
| 11 | FUNDING_LIMIT_CODE | — | — | — | — | — | — |
| 12 | INVESTMENT_LIMIT_CODE | — | — | — | — | — | — |
| 13 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 14 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 15 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 16 | LEGAL_ENTITY_ID | — | — | — | — | — | — |
| 17 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 18 | ORG_ID | — | — | — | — | — | — |
| 19 | ORG_PARTY_ID | — | — | — | — | — | — |
| 20 | PAY_USE_ENABLE_FLAG | — | — | — | — | — | — |
| 21 | PORTFOLIO_CODE | — | — | — | — | — | — |
| 22 | PRICING_MODEL | — | — | — | — | — | — |
| 23 | PRIMARY_FLAG | — | — | — | — | — | — |
| 24 | PROGRAM_APPLICATION_ID | — | — | — | — | — | — |
| 25 | PROGRAM_ID | — | — | — | — | — | — |
| 26 | PROGRAM_UPDATE_DATE | — | — | — | — | — | — |
| 27 | REQUEST_ID | — | — | — | — | — | — |
| 28 | XTR_BANK_ACCOUNT_REFERENCE | — | — | — | — | — | — |
| 29 | XTR_DEFAULT_SETTLEMENT_FLAG | — | — | — | — | — | — |
| 30 | XTR_USE_ENABLE_FLAG | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[bankaccountuseextractpvo|BankAccountUseExtractPVO]] (OTHER · BICC: 13/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AP_USE_ENABLE_FLAG | BankAccountUsePEOApUseEnableFlag | ✅ |
| AR_USE_ENABLE_FLAG | BankAccountUsePEOArUseEnableFlag | ✅ |
| BANK_ACCOUNT_ID | BankAccountUsePEOBankAccountId | ✅ |
| BANK_ACCT_USE_ID | BankAccountUsePEOBankAcctUseId | ✅ |
| CREATED_BY | BankAccountUsePEOCreatedBy | ✅ |
| CREATION_DATE | BankAccountUsePEOCreationDate | ✅ |
| END_DATE | BankAccountUsePEOEndDate | ✅ |
| LAST_UPDATE_DATE | BankAccountUsePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BankAccountUsePEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BankAccountUsePEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | BankAccountUsePEOObjectVersionNumber | ✅ |
| ORG_ID | BankAccountUsePEOOrgId | ✅ |
| PAY_USE_ENABLE_FLAG | BankAccountUsePEOPayUseEnableFlag | ✅ |

### [[disbursementheaderpvo|DisbursementHeaderPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BANK_ACCOUNT_ID | BankAccountUseBankAccountId | — |
| BANK_ACCT_USE_ID | BankAccountUseBankAcctUseId | — |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AP_USE_ENABLE_FLAG | BankAcctUsesApUseEnableFlag | — |
| AR_USE_ENABLE_FLAG | BankAcctUsesArUseEnableFlag | — |
| AUTHORIZED_FLAG | BankAcctUsesAuthorizedFlag | — |
| BANK_ACCOUNT_ID | BankAcctUsesBankAccountId | — |
| BANK_ACCT_USE_ID | BankAcctUsesBankAcctUseId | — |
| DEFAULT_ACCOUNT_FLAG | BankAcctUsesDefaultAccountFlag | — |
| EFT_SCRIPT_NAME | BankAcctUsesEftScriptName | — |
| END_DATE | BankAcctUsesEndDate | — |
| FUNDING_LIMIT_CODE | BankAcctUsesFundingLimitCode | — |
| INVESTMENT_LIMIT_CODE | BankAcctUsesInvestmentLimitCode | — |
| LEGAL_ENTITY_ID | BankAcctUsesLegalEntityId | — |
| OBJECT_VERSION_NUMBER | BankAcctUsesObjectVersionNumber | — |
| ORG_ID | BankAcctUsesOrgId | — |
| ORG_PARTY_ID | BankAcctUsesOrgPartyId | — |
| PAY_USE_ENABLE_FLAG | BankAcctUsesPayUseEnableFlag | — |
| PORTFOLIO_CODE | BankAcctUsesPortfolioCode | — |
| PRICING_MODEL | BankAcctUsesPricingModel | — |
| PRIMARY_FLAG | BankAcctUsesPrimaryFlag | — |
| PROGRAM_APPLICATION_ID | BankAcctUsesProgramApplicationId | — |
| PROGRAM_ID | BankAcctUsesProgramId | — |
| PROGRAM_UPDATE_DATE | BankAcctUsesProgramUpdateDate | — |
| REQUEST_ID | BankAcctUsesRequestId | — |
| XTR_BANK_ACCOUNT_REFERENCE | BankAcctUsesXtrBankAccountReference | — |
| XTR_DEFAULT_SETTLEMENT_FLAG | BankAcctUsesXtrDefaultSettlementFlag | — |
| XTR_USE_ENABLE_FLAG | BankAcctUsesXtrUseEnableFlag | — |

### [[miscreceiptdistributionpvo|MiscReceiptDistributionPVO]] (AR · BICC: 1/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AP_USE_ENABLE_FLAG | BankAccUseApUseEnableFlag | — |
| AR_USE_ENABLE_FLAG | BankAccUseArUseEnableFlag | — |
| AUTHORIZED_FLAG | BankAccUseAuthorizedFlag | — |
| BANK_ACCOUNT_ID | BankAccUseBankAccountId | — |
| BANK_ACCT_USE_ID | BankAccUseBankAcctUseId | — |
| CREATED_BY | BankAccUseCreatedBy | — |
| CREATION_DATE | BankAccUseCreationDate | — |
| DEFAULT_ACCOUNT_FLAG | BankAccUseDefaultAccountFlag | — |
| EFT_SCRIPT_NAME | BankAccUseEftScriptName | — |
| END_DATE | BankAccUseEndDate | — |
| FUNDING_LIMIT_CODE | BankAccUseFundingLimitCode | — |
| INVESTMENT_LIMIT_CODE | BankAccUseInvestmentLimitCode | — |
| LAST_UPDATE_DATE | BankAccUseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BankAccUseLastUpdateLogin | — |
| LAST_UPDATED_BY | BankAccUseLastUpdatedBy | — |
| LEGAL_ENTITY_ID | BankAccUseLegalEntityId | — |
| OBJECT_VERSION_NUMBER | BankAccUseObjectVersionNumber | — |
| ORG_ID | BankAccUseOrgId | — |
| ORG_PARTY_ID | BankAccUseOrgPartyId | — |
| PAY_USE_ENABLE_FLAG | BankAccUsePayUseEnableFlag | — |
| PORTFOLIO_CODE | BankAccUsePortfolioCode | — |
| PRICING_MODEL | BankAccUsePricingModel | — |
| PRIMARY_FLAG | BankAccUsePrimaryFlag | — |
| PROGRAM_APPLICATION_ID | BankAccUseProgramApplicationId | — |
| PROGRAM_ID | BankAccUseProgramId | — |
| PROGRAM_UPDATE_DATE | BankAccUseProgramUpdateDate | — |
| REQUEST_ID | BankAccUseRequestId | — |
| XTR_BANK_ACCOUNT_REFERENCE | BankAccUseXtrBankAccountReference | — |
| XTR_DEFAULT_SETTLEMENT_FLAG | BankAccUseXtrDefaultSettlementFlag | — |
| XTR_USE_ENABLE_FLAG | BankAccUseXtrUseEnableFlag | — |

### [[paiddisbursementschedulepvo|PaidDisbursementSchedulePVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BANK_ACCOUNT_ID | BankAccountUseBankAccountId | — |
| BANK_ACCT_USE_ID | BankAccountUseBankAcctUseId | — |

### [[paymenthistorydistributionpvo|PaymentHistoryDistributionPVO]] (AP · BICC: 2/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BANK_ACCOUNT_ID | BankAccountUseBankAccountId | ✅ |
| BANK_ACCT_USE_ID | BankAccountUseBankAcctUseId | — |
| LAST_UPDATE_DATE | BankAccountUseLastUpdateDate | ✅ |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR · BICC: 2/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AP_USE_ENABLE_FLAG | BankAccUseApUseEnableFlag | — |
| AR_USE_ENABLE_FLAG | BankAccUseArUseEnableFlag | — |
| AUTHORIZED_FLAG | BankAccUseAuthorizedFlag | — |
| BANK_ACCOUNT_ID | BankAccUseBankAccountId | ✅ |
| BANK_ACCT_USE_ID | BankAccUseBankAcctUseId | — |
| CREATED_BY | BankAccUseCreatedBy | — |
| CREATION_DATE | BankAccUseCreationDate | — |
| DEFAULT_ACCOUNT_FLAG | BankAccUseDefaultAccountFlag | — |
| EFT_SCRIPT_NAME | BankAccUseEftScriptName | — |
| END_DATE | BankAccUseEndDate | — |
| FUNDING_LIMIT_CODE | BankAccUseFundingLimitCode | — |
| INVESTMENT_LIMIT_CODE | BankAccUseInvestmentLimitCode | — |
| LAST_UPDATE_DATE | BankAccUseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BankAccUseLastUpdateLogin | — |
| LAST_UPDATED_BY | BankAccUseLastUpdatedBy | — |
| LEGAL_ENTITY_ID | BankAccUseLegalEntityId | — |
| OBJECT_VERSION_NUMBER | BankAccUseObjectVersionNumber | — |
| ORG_ID | BankAccUseOrgId | — |
| ORG_PARTY_ID | BankAccUseOrgPartyId | — |
| PAY_USE_ENABLE_FLAG | BankAccUsePayUseEnableFlag | — |
| PORTFOLIO_CODE | BankAccUsePortfolioCode | — |
| PRICING_MODEL | BankAccUsePricingModel | — |
| PRIMARY_FLAG | BankAccUsePrimaryFlag | — |
| PROGRAM_APPLICATION_ID | BankAccUseProgramApplicationId | — |
| PROGRAM_ID | BankAccUseProgramId | — |
| PROGRAM_UPDATE_DATE | BankAccUseProgramUpdateDate | — |
| REQUEST_ID | BankAccUseRequestId | — |
| XTR_BANK_ACCOUNT_REFERENCE | BankAccUseXtrBankAccountReference | — |
| XTR_DEFAULT_SETTLEMENT_FLAG | BankAccUseXtrDefaultSettlementFlag | — |
| XTR_USE_ENABLE_FLAG | BankAccUseXtrUseEnableFlag | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR · BICC: 1/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AP_USE_ENABLE_FLAG | BankAccUseApUseEnableFlag | — |
| AR_USE_ENABLE_FLAG | BankAccUseArUseEnableFlag | — |
| AUTHORIZED_FLAG | BankAccUseAuthorizedFlag | — |
| BANK_ACCOUNT_ID | BankAccUseBankAccountId | — |
| BANK_ACCT_USE_ID | BankAccUseBankAcctUseId | — |
| CREATED_BY | BankAccUseCreatedBy | — |
| CREATION_DATE | BankAccUseCreationDate | — |
| DEFAULT_ACCOUNT_FLAG | BankAccUseDefaultAccountFlag | — |
| EFT_SCRIPT_NAME | BankAccUseEftScriptName | — |
| END_DATE | BankAccUseEndDate | — |
| FUNDING_LIMIT_CODE | BankAccUseFundingLimitCode | — |
| INVESTMENT_LIMIT_CODE | BankAccUseInvestmentLimitCode | — |
| LAST_UPDATE_DATE | BankAccUseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BankAccUseLastUpdateLogin | — |
| LAST_UPDATED_BY | BankAccUseLastUpdatedBy | — |
| LEGAL_ENTITY_ID | BankAccUseLegalEntityId | — |
| OBJECT_VERSION_NUMBER | BankAccUseObjectVersionNumber | — |
| ORG_ID | BankAccUseOrgId | — |
| ORG_PARTY_ID | BankAccUseOrgPartyId | — |
| PAY_USE_ENABLE_FLAG | BankAccUsePayUseEnableFlag | — |
| PORTFOLIO_CODE | BankAccUsePortfolioCode | — |
| PRICING_MODEL | BankAccUsePricingModel | — |
| PRIMARY_FLAG | BankAccUsePrimaryFlag | — |
| PROGRAM_APPLICATION_ID | BankAccUseProgramApplicationId | — |
| PROGRAM_ID | BankAccUseProgramId | — |
| PROGRAM_UPDATE_DATE | BankAccUseProgramUpdateDate | — |
| REQUEST_ID | BankAccUseRequestId | — |
| XTR_BANK_ACCOUNT_REFERENCE | BankAccUseXtrBankAccountReference | — |
| XTR_DEFAULT_SETTLEMENT_FLAG | BankAccUseXtrDefaultSettlementFlag | — |
| XTR_USE_ENABLE_FLAG | BankAccUseXtrUseEnableFlag | — |

### [[receiptapplicationpvo|ReceiptApplicationPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AP_USE_ENABLE_FLAG | BankAcctUseApUseEnableFlag | — |
| AR_USE_ENABLE_FLAG | BankAcctUseArUseEnableFlag | — |
| AUTHORIZED_FLAG | BankAcctUseAuthorizedFlag | — |
| BANK_ACCOUNT_ID | BankAcctUseBankAccountId | — |
| BANK_ACCT_USE_ID | BankAcctUseBankAcctUseId | — |
| DEFAULT_ACCOUNT_FLAG | BankAcctUseDefaultAccountFlag | — |
| EFT_SCRIPT_NAME | BankAcctUseEftScriptName | — |
| END_DATE | BankAcctUseEndDate | — |
| FUNDING_LIMIT_CODE | BankAcctUseFundingLimitCode | — |
| INVESTMENT_LIMIT_CODE | BankAcctUseInvestmentLimitCode | — |
| LEGAL_ENTITY_ID | BankAcctUseLegalEntityId | — |
| ORG_ID | BankAcctUseOrgId | — |
| ORG_PARTY_ID | BankAcctUseOrgPartyId | — |
| PAY_USE_ENABLE_FLAG | BankAcctUsePayUseEnableFlag | — |
| PORTFOLIO_CODE | BankAcctUsePortfolioCode | — |
| PRICING_MODEL | BankAcctUsePricingModel | — |
| PRIMARY_FLAG | BankAcctUsePrimaryFlag | — |
| PROGRAM_APPLICATION_ID | BankAcctUseProgramApplicationId | — |
| PROGRAM_ID | BankAcctUseProgramId | — |
| PROGRAM_UPDATE_DATE | BankAcctUseProgramUpdateDate | — |
| REQUEST_ID | BankAcctUseRequestId | — |
| XTR_BANK_ACCOUNT_REFERENCE | BankAcctUseXtrBankAccountReference | — |
| XTR_DEFAULT_SETTLEMENT_FLAG | BankAcctUseXtrDefaultSettlementFlag | — |
| XTR_USE_ENABLE_FLAG | BankAcctUseXtrUseEnableFlag | — |

### [[receiptheaderpvo|ReceiptHeaderPVO]] (AR · BICC: 1/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AP_USE_ENABLE_FLAG | BankAcctUseApUseEnableFlag | — |
| AR_USE_ENABLE_FLAG | BankAcctUseArUseEnableFlag | — |
| AUTHORIZED_FLAG | BankAcctUseAuthorizedFlag | — |
| BANK_ACCOUNT_ID | BankAcctUseBankAccountId | — |
| BANK_ACCT_USE_ID | BankAcctUseBankAcctUseId | — |
| CREATED_BY | BankAcctUseCreatedBy | — |
| CREATION_DATE | BankAcctUseCreationDate | — |
| DEFAULT_ACCOUNT_FLAG | BankAcctUseDefaultAccountFlag | — |
| EFT_SCRIPT_NAME | BankAcctUseEftScriptName | — |
| END_DATE | BankAcctUseEndDate | — |
| FUNDING_LIMIT_CODE | BankAcctUseFundingLimitCode | — |
| INVESTMENT_LIMIT_CODE | BankAcctUseInvestmentLimitCode | — |
| LAST_UPDATE_DATE | BankAcctUseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BankAcctUseLastUpdateLogin | — |
| LAST_UPDATED_BY | BankAcctUseLastUpdatedBy | — |
| LEGAL_ENTITY_ID | BankAcctUseLegalEntityId | — |
| OBJECT_VERSION_NUMBER | BankAcctUseObjectVersionNumber | — |
| ORG_ID | BankAcctUseOrgId | — |
| ORG_PARTY_ID | BankAcctUseOrgPartyId | — |
| PAY_USE_ENABLE_FLAG | BankAcctUsePayUseEnableFlag | — |
| PORTFOLIO_CODE | BankAcctUsePortfolioCode | — |
| PRICING_MODEL | BankAcctUsePricingModel | — |
| PRIMARY_FLAG | BankAcctUsePrimaryFlag | — |
| PROGRAM_APPLICATION_ID | BankAcctUseProgramApplicationId | — |
| PROGRAM_ID | BankAcctUseProgramId | — |
| PROGRAM_UPDATE_DATE | BankAcctUseProgramUpdateDate | — |
| REQUEST_ID | BankAcctUseRequestId | — |
| XTR_BANK_ACCOUNT_REFERENCE | BankAcctUseXtrBankAccountReference | — |
| XTR_DEFAULT_SETTLEMENT_FLAG | BankAcctUseXtrDefaultSettlementFlag | — |
| XTR_USE_ENABLE_FLAG | BankAcctUseXtrUseEnableFlag | — |

### [[salesinvoicecustomertrxlinespvo|SalesInvoiceCustomerTrxLinesPVO]] (AR · BICC: 2/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AP_USE_ENABLE_FLAG | BankAccountUseApUseEnableFlag | — |
| AR_USE_ENABLE_FLAG | BankAccountUseArUseEnableFlag | — |
| AUTHORIZED_FLAG | BankAccountUseAuthorizedFlag | — |
| BANK_ACCOUNT_ID | BankAccountUseBankAccountId | — |
| BANK_ACCT_USE_ID | BankAccountUseBankAcctUseId | — |
| DEFAULT_ACCOUNT_FLAG | BankAccountUseDefaultAccountFlag | — |
| EFT_SCRIPT_NAME | BankAccountUseEftScriptName | — |
| END_DATE | BankAccountUseEndDate | ✅ |
| FUNDING_LIMIT_CODE | BankAccountUseFundingLimitCode | — |
| INVESTMENT_LIMIT_CODE | BankAccountUseInvestmentLimitCode | — |
| LEGAL_ENTITY_ID | BankAccountUseLegalEntityId | — |
| ORG_ID | BankAccountUseOrgId | ✅ |
| ORG_PARTY_ID | BankAccountUseOrgPartyId | — |
| PAY_USE_ENABLE_FLAG | BankAccountUsePayUseEnableFlag | — |
| PORTFOLIO_CODE | BankAccountUsePortfolioCode | — |
| PRICING_MODEL | BankAccountUsePricingModel | — |
| PRIMARY_FLAG | BankAccountUsePrimaryFlag | — |
| PROGRAM_APPLICATION_ID | BankAccountUseProgramApplicationId | — |
| PROGRAM_ID | BankAccountUseProgramId | — |
| PROGRAM_UPDATE_DATE | BankAccountUseProgramUpdateDate | — |
| REQUEST_ID | BankAccountUseRequestId | — |
| XTR_BANK_ACCOUNT_REFERENCE | BankAccountUseXtrBankAccountReference | — |
| XTR_DEFAULT_SETTLEMENT_FLAG | BankAccountUseXtrDefaultSettlementFlag | — |
| XTR_USE_ENABLE_FLAG | BankAccountUseXtrUseEnableFlag | — |

### [[transactionheaderbillsreceivablepvo|TransactionHeaderBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AP_USE_ENABLE_FLAG | BankAcctUsesApUseEnableFlag | — |
| AR_USE_ENABLE_FLAG | BankAcctUsesArUseEnableFlag | — |
| AUTHORIZED_FLAG | BankAcctUsesAuthorizedFlag | — |
| BANK_ACCOUNT_ID | BankAcctUsesBankAccountId | — |
| BANK_ACCT_USE_ID | BankAcctUsesBankAcctUseId | — |
| DEFAULT_ACCOUNT_FLAG | BankAcctUsesDefaultAccountFlag | — |
| EFT_SCRIPT_NAME | BankAcctUsesEftScriptName | — |
| END_DATE | BankAcctUsesEndDate | — |
| FUNDING_LIMIT_CODE | BankAcctUsesFundingLimitCode | — |
| INVESTMENT_LIMIT_CODE | BankAcctUsesInvestmentLimitCode | — |
| LEGAL_ENTITY_ID | BankAcctUsesLegalEntityId | — |
| OBJECT_VERSION_NUMBER | BankAcctUsesObjectVersionNumber | — |
| ORG_ID | BankAcctUsesOrgId | — |
| ORG_PARTY_ID | BankAcctUsesOrgPartyId | — |
| PAY_USE_ENABLE_FLAG | BankAcctUsesPayUseEnableFlag | — |
| PORTFOLIO_CODE | BankAcctUsesPortfolioCode | — |
| PRICING_MODEL | BankAcctUsesPricingModel | — |
| PRIMARY_FLAG | BankAcctUsesPrimaryFlag | — |
| PROGRAM_APPLICATION_ID | BankAcctUsesProgramApplicationId | — |
| PROGRAM_ID | BankAcctUsesProgramId | — |
| PROGRAM_UPDATE_DATE | BankAcctUsesProgramUpdateDate | — |
| REQUEST_ID | BankAcctUsesRequestId | — |
| XTR_BANK_ACCOUNT_REFERENCE | BankAcctUsesXtrBankAccountReference | — |
| XTR_DEFAULT_SETTLEMENT_FLAG | BankAcctUsesXtrDefaultSettlementFlag | — |
| XTR_USE_ENABLE_FLAG | BankAcctUsesXtrUseEnableFlag | — |

### [[transactionheadernovcpvo|TransactionHeaderNoVCPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AP_USE_ENABLE_FLAG | BankAcctUsesApUseEnableFlag | — |
| AR_USE_ENABLE_FLAG | BankAcctUsesArUseEnableFlag | — |
| AUTHORIZED_FLAG | BankAcctUsesAuthorizedFlag | — |
| BANK_ACCOUNT_ID | BankAcctUsesBankAccountId | — |
| BANK_ACCT_USE_ID | BankAcctUsesBankAcctUseId | — |
| DEFAULT_ACCOUNT_FLAG | BankAcctUsesDefaultAccountFlag | — |
| EFT_SCRIPT_NAME | BankAcctUsesEftScriptName | — |
| END_DATE | BankAcctUsesEndDate | — |
| FUNDING_LIMIT_CODE | BankAcctUsesFundingLimitCode | — |
| INVESTMENT_LIMIT_CODE | BankAcctUsesInvestmentLimitCode | — |
| LEGAL_ENTITY_ID | BankAcctUsesLegalEntityId | — |
| OBJECT_VERSION_NUMBER | BankAcctUsesObjectVersionNumber | — |
| ORG_ID | BankAcctUsesOrgId | — |
| ORG_PARTY_ID | BankAcctUsesOrgPartyId | — |
| PAY_USE_ENABLE_FLAG | BankAcctUsesPayUseEnableFlag | — |
| PORTFOLIO_CODE | BankAcctUsesPortfolioCode | — |
| PRICING_MODEL | BankAcctUsesPricingModel | — |
| PRIMARY_FLAG | BankAcctUsesPrimaryFlag | — |
| PROGRAM_APPLICATION_ID | BankAcctUsesProgramApplicationId | — |
| PROGRAM_ID | BankAcctUsesProgramId | — |
| PROGRAM_UPDATE_DATE | BankAcctUsesProgramUpdateDate | — |
| REQUEST_ID | BankAcctUsesRequestId | — |
| XTR_BANK_ACCOUNT_REFERENCE | BankAcctUsesXtrBankAccountReference | — |
| XTR_DEFAULT_SETTLEMENT_FLAG | BankAcctUsesXtrDefaultSettlementFlag | — |
| XTR_USE_ENABLE_FLAG | BankAcctUsesXtrUseEnableFlag | — |

### [[transactionheaderpvo|TransactionHeaderPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AP_USE_ENABLE_FLAG | BankAcctUsesApUseEnableFlag | — |
| AR_USE_ENABLE_FLAG | BankAcctUsesArUseEnableFlag | — |
| AUTHORIZED_FLAG | BankAcctUsesAuthorizedFlag | — |
| BANK_ACCOUNT_ID | BankAcctUsesBankAccountId | — |
| BANK_ACCT_USE_ID | BankAcctUsesBankAcctUseId | — |
| DEFAULT_ACCOUNT_FLAG | BankAcctUsesDefaultAccountFlag | — |
| EFT_SCRIPT_NAME | BankAcctUsesEftScriptName | — |
| END_DATE | BankAcctUsesEndDate | — |
| FUNDING_LIMIT_CODE | BankAcctUsesFundingLimitCode | — |
| INVESTMENT_LIMIT_CODE | BankAcctUsesInvestmentLimitCode | — |
| LEGAL_ENTITY_ID | BankAcctUsesLegalEntityId | — |
| OBJECT_VERSION_NUMBER | BankAcctUsesObjectVersionNumber | — |
| ORG_ID | BankAcctUsesOrgId | — |
| ORG_PARTY_ID | BankAcctUsesOrgPartyId | — |
| PAY_USE_ENABLE_FLAG | BankAcctUsesPayUseEnableFlag | — |
| PORTFOLIO_CODE | BankAcctUsesPortfolioCode | — |
| PRICING_MODEL | BankAcctUsesPricingModel | — |
| PRIMARY_FLAG | BankAcctUsesPrimaryFlag | — |
| PROGRAM_APPLICATION_ID | BankAcctUsesProgramApplicationId | — |
| PROGRAM_ID | BankAcctUsesProgramId | — |
| PROGRAM_UPDATE_DATE | BankAcctUsesProgramUpdateDate | — |
| REQUEST_ID | BankAcctUsesRequestId | — |
| XTR_BANK_ACCOUNT_REFERENCE | BankAcctUsesXtrBankAccountReference | — |
| XTR_DEFAULT_SETTLEMENT_FLAG | BankAcctUsesXtrDefaultSettlementFlag | — |
| XTR_USE_ENABLE_FLAG | BankAcctUsesXtrUseEnableFlag | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR · BICC: 1/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AP_USE_ENABLE_FLAG | BankAccountUseApUseEnableFlag | — |
| AR_USE_ENABLE_FLAG | BankAccountUseArUseEnableFlag | — |
| AUTHORIZED_FLAG | BankAccountUseAuthorizedFlag | — |
| BANK_ACCOUNT_ID | BankAccountUseBankAccountId | — |
| BANK_ACCT_USE_ID | BankAccountUseBankAcctUseId | — |
| CREATED_BY | BankAccountUseCreatedBy | — |
| CREATION_DATE | BankAccountUseCreationDate | — |
| DEFAULT_ACCOUNT_FLAG | BankAccountUseDefaultAccountFlag | — |
| EFT_SCRIPT_NAME | BankAccountUseEftScriptName | — |
| END_DATE | BankAccountUseEndDate | — |
| FUNDING_LIMIT_CODE | BankAccountUseFundingLimitCode | — |
| INVESTMENT_LIMIT_CODE | BankAccountUseInvestmentLimitCode | — |
| LAST_UPDATE_DATE | BankAccountUseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BankAccountUseLastUpdateLogin | — |
| LAST_UPDATED_BY | BankAccountUseLastUpdatedBy | — |
| LEGAL_ENTITY_ID | BankAccountUseLegalEntityId | — |
| OBJECT_VERSION_NUMBER | BankAccountUseObjectVersionNumber | — |
| ORG_ID | BankAccountUseOrgId | — |
| ORG_PARTY_ID | BankAccountUseOrgPartyId | — |
| PAY_USE_ENABLE_FLAG | BankAccountUsePayUseEnableFlag | — |
| PORTFOLIO_CODE | BankAccountUsePortfolioCode | — |
| PRICING_MODEL | BankAccountUsePricingModel | — |
| PRIMARY_FLAG | BankAccountUsePrimaryFlag | — |
| PROGRAM_APPLICATION_ID | BankAccountUseProgramApplicationId | — |
| PROGRAM_ID | BankAccountUseProgramId | — |
| PROGRAM_UPDATE_DATE | BankAccountUseProgramUpdateDate | — |
| REQUEST_ID | BankAccountUseRequestId | — |
| XTR_BANK_ACCOUNT_REFERENCE | BankAccountUseXtrBankAccountReference | — |
| XTR_DEFAULT_SETTLEMENT_FLAG | BankAccountUseXtrDefaultSettlementFlag | — |
| XTR_USE_ENABLE_FLAG | BankAccountUseXtrUseEnableFlag | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR · BICC: 1/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AP_USE_ENABLE_FLAG | BankAccountUseApUseEnableFlag | — |
| AR_USE_ENABLE_FLAG | BankAccountUseArUseEnableFlag | — |
| AUTHORIZED_FLAG | BankAccountUseAuthorizedFlag | — |
| BANK_ACCOUNT_ID | BankAccountUseBankAccountId | — |
| BANK_ACCT_USE_ID | BankAccountUseBankAcctUseId | — |
| CREATED_BY | BankAccountUseCreatedBy | — |
| CREATION_DATE | BankAccountUseCreationDate | — |
| DEFAULT_ACCOUNT_FLAG | BankAccountUseDefaultAccountFlag | — |
| EFT_SCRIPT_NAME | BankAccountUseEftScriptName | — |
| END_DATE | BankAccountUseEndDate | — |
| FUNDING_LIMIT_CODE | BankAccountUseFundingLimitCode | — |
| INVESTMENT_LIMIT_CODE | BankAccountUseInvestmentLimitCode | — |
| LAST_UPDATE_DATE | BankAccountUseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BankAccountUseLastUpdateLogin | — |
| LAST_UPDATED_BY | BankAccountUseLastUpdatedBy | — |
| LEGAL_ENTITY_ID | BankAccountUseLegalEntityId | — |
| OBJECT_VERSION_NUMBER | BankAccountUseObjectVersionNumber | — |
| ORG_ID | BankAccountUseOrgId | — |
| ORG_PARTY_ID | BankAccountUseOrgPartyId | — |
| PAY_USE_ENABLE_FLAG | BankAccountUsePayUseEnableFlag | — |
| PORTFOLIO_CODE | BankAccountUsePortfolioCode | — |
| PRICING_MODEL | BankAccountUsePricingModel | — |
| PRIMARY_FLAG | BankAccountUsePrimaryFlag | — |
| PROGRAM_APPLICATION_ID | BankAccountUseProgramApplicationId | — |
| PROGRAM_ID | BankAccountUseProgramId | — |
| PROGRAM_UPDATE_DATE | BankAccountUseProgramUpdateDate | — |
| REQUEST_ID | BankAccountUseRequestId | — |
| XTR_BANK_ACCOUNT_REFERENCE | BankAccountUseXtrBankAccountReference | — |
| XTR_DEFAULT_SETTLEMENT_FLAG | BankAccountUseXtrDefaultSettlementFlag | — |
| XTR_USE_ENABLE_FLAG | BankAccountUseXtrUseEnableFlag | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR · BICC: 1/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AP_USE_ENABLE_FLAG | BankAccountUseApUseEnableFlag | — |
| AR_USE_ENABLE_FLAG | BankAccountUseArUseEnableFlag | — |
| AUTHORIZED_FLAG | BankAccountUseAuthorizedFlag | — |
| BANK_ACCOUNT_ID | BankAccountUseBankAccountId | — |
| BANK_ACCT_USE_ID | BankAccountUseBankAcctUseId | — |
| CREATED_BY | BankAccountUseCreatedBy | — |
| CREATION_DATE | BankAccountUseCreationDate | — |
| DEFAULT_ACCOUNT_FLAG | BankAccountUseDefaultAccountFlag | — |
| EFT_SCRIPT_NAME | BankAccountUseEftScriptName | — |
| END_DATE | BankAccountUseEndDate | — |
| FUNDING_LIMIT_CODE | BankAccountUseFundingLimitCode | — |
| INVESTMENT_LIMIT_CODE | BankAccountUseInvestmentLimitCode | — |
| LAST_UPDATE_DATE | BankAccountUseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BankAccountUseLastUpdateLogin | — |
| LAST_UPDATED_BY | BankAccountUseLastUpdatedBy | — |
| LEGAL_ENTITY_ID | BankAccountUseLegalEntityId | — |
| OBJECT_VERSION_NUMBER | BankAccountUseObjectVersionNumber | — |
| ORG_ID | BankAccountUseOrgId | — |
| ORG_PARTY_ID | BankAccountUseOrgPartyId | — |
| PAY_USE_ENABLE_FLAG | BankAccountUsePayUseEnableFlag | — |
| PORTFOLIO_CODE | BankAccountUsePortfolioCode | — |
| PRICING_MODEL | BankAccountUsePricingModel | — |
| PRIMARY_FLAG | BankAccountUsePrimaryFlag | — |
| PROGRAM_APPLICATION_ID | BankAccountUseProgramApplicationId | — |
| PROGRAM_ID | BankAccountUseProgramId | — |
| PROGRAM_UPDATE_DATE | BankAccountUseProgramUpdateDate | — |
| REQUEST_ID | BankAccountUseRequestId | — |
| XTR_BANK_ACCOUNT_REFERENCE | BankAccountUseXtrBankAccountReference | — |
| XTR_DEFAULT_SETTLEMENT_FLAG | BankAccountUseXtrDefaultSettlementFlag | — |
| XTR_USE_ENABLE_FLAG | BankAccountUseXtrUseEnableFlag | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR · BICC: 1/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AP_USE_ENABLE_FLAG | BankAccountUseApUseEnableFlag | — |
| AR_USE_ENABLE_FLAG | BankAccountUseArUseEnableFlag | — |
| AUTHORIZED_FLAG | BankAccountUseAuthorizedFlag | — |
| BANK_ACCOUNT_ID | BankAccountUseBankAccountId | — |
| BANK_ACCT_USE_ID | BankAccountUseBankAcctUseId | — |
| CREATED_BY | BankAccountUseCreatedBy | — |
| CREATION_DATE | BankAccountUseCreationDate | — |
| DEFAULT_ACCOUNT_FLAG | BankAccountUseDefaultAccountFlag | — |
| EFT_SCRIPT_NAME | BankAccountUseEftScriptName | — |
| END_DATE | BankAccountUseEndDate | — |
| FUNDING_LIMIT_CODE | BankAccountUseFundingLimitCode | — |
| INVESTMENT_LIMIT_CODE | BankAccountUseInvestmentLimitCode | — |
| LAST_UPDATE_DATE | BankAccountUseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BankAccountUseLastUpdateLogin | — |
| LAST_UPDATED_BY | BankAccountUseLastUpdatedBy | — |
| LEGAL_ENTITY_ID | BankAccountUseLegalEntityId | — |
| OBJECT_VERSION_NUMBER | BankAccountUseObjectVersionNumber | — |
| ORG_ID | BankAccountUseOrgId | — |
| ORG_PARTY_ID | BankAccountUseOrgPartyId | — |
| PAY_USE_ENABLE_FLAG | BankAccountUsePayUseEnableFlag | — |
| PORTFOLIO_CODE | BankAccountUsePortfolioCode | — |
| PRICING_MODEL | BankAccountUsePricingModel | — |
| PRIMARY_FLAG | BankAccountUsePrimaryFlag | — |
| PROGRAM_APPLICATION_ID | BankAccountUseProgramApplicationId | — |
| PROGRAM_ID | BankAccountUseProgramId | — |
| PROGRAM_UPDATE_DATE | BankAccountUseProgramUpdateDate | — |
| REQUEST_ID | BankAccountUseRequestId | — |
| XTR_BANK_ACCOUNT_REFERENCE | BankAccountUseXtrBankAccountReference | — |
| XTR_DEFAULT_SETTLEMENT_FLAG | BankAccountUseXtrDefaultSettlementFlag | — |
| XTR_USE_ENABLE_FLAG | BankAccountUseXtrUseEnableFlag | — |

### [[transactionlinepvo|TransactionLinePVO]] (AR · BICC: 1/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AP_USE_ENABLE_FLAG | BankAccountUseApUseEnableFlag | — |
| AR_USE_ENABLE_FLAG | BankAccountUseArUseEnableFlag | — |
| AUTHORIZED_FLAG | BankAccountUseAuthorizedFlag | — |
| BANK_ACCOUNT_ID | BankAccountUseBankAccountId | — |
| BANK_ACCT_USE_ID | BankAccountUseBankAcctUseId | — |
| CREATED_BY | BankAccountUseCreatedBy | — |
| CREATION_DATE | BankAccountUseCreationDate | — |
| DEFAULT_ACCOUNT_FLAG | BankAccountUseDefaultAccountFlag | — |
| EFT_SCRIPT_NAME | BankAccountUseEftScriptName | — |
| END_DATE | BankAccountUseEndDate | — |
| FUNDING_LIMIT_CODE | BankAccountUseFundingLimitCode | — |
| INVESTMENT_LIMIT_CODE | BankAccountUseInvestmentLimitCode | — |
| LAST_UPDATE_DATE | BankAccountUseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BankAccountUseLastUpdateLogin | — |
| LAST_UPDATED_BY | BankAccountUseLastUpdatedBy | — |
| LEGAL_ENTITY_ID | BankAccountUseLegalEntityId | — |
| OBJECT_VERSION_NUMBER | BankAccountUseObjectVersionNumber | — |
| ORG_ID | BankAccountUseOrgId | — |
| ORG_PARTY_ID | BankAccountUseOrgPartyId | — |
| PAY_USE_ENABLE_FLAG | BankAccountUsePayUseEnableFlag | — |
| PORTFOLIO_CODE | BankAccountUsePortfolioCode | — |
| PRICING_MODEL | BankAccountUsePricingModel | — |
| PRIMARY_FLAG | BankAccountUsePrimaryFlag | — |
| PROGRAM_APPLICATION_ID | BankAccountUseProgramApplicationId | — |
| PROGRAM_ID | BankAccountUseProgramId | — |
| PROGRAM_UPDATE_DATE | BankAccountUseProgramUpdateDate | — |
| REQUEST_ID | BankAccountUseRequestId | — |
| XTR_BANK_ACCOUNT_REFERENCE | BankAccountUseXtrBankAccountReference | — |
| XTR_DEFAULT_SETTLEMENT_FLAG | BankAccountUseXtrDefaultSettlementFlag | — |
| XTR_USE_ENABLE_FLAG | BankAccountUseXtrUseEnableFlag | — |
