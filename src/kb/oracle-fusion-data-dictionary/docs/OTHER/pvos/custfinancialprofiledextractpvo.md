---
id: DOC-OTHER-PVO-CustFinancialProfileDExtractPVO
doc_type: system-doc
title: "CustFinancialProfileDExtractPVO — PVO Cross-Module"
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
  - CustFinancialProfileDExtractPVO
  - custfinancialprofiledextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CustFinancialProfileDExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cust Financial Profile DExtract. Acessa as tabelas: HZ_CUST_PROFILE_AMTS_F.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.CustFinancialProfileDExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 97 | 1 | 3 | 44 | 45% |

---

## 🔗 Tabelas Relacionadas

- [[hz_cust_profile_amts_f|HZ_CUST_PROFILE_AMTS_F]] — 97 atributos (3 PKs, 44 BICC)

---

## ⚙️ Atributos

### [[hz_cust_profile_amts_f|HZ_CUST_PROFILE_AMTS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HzCustProfileAmtsFApplicationId | APPLICATION_ID | — | ✅ |
| 2 | HzCustProfileAmtsFAttribute1 | ATTRIBUTE1 | — | — |
| 3 | HzCustProfileAmtsFAttribute10 | ATTRIBUTE10 | — | — |
| 4 | HzCustProfileAmtsFAttribute11 | ATTRIBUTE11 | — | — |
| 5 | HzCustProfileAmtsFAttribute12 | ATTRIBUTE12 | — | — |
| 6 | HzCustProfileAmtsFAttribute13 | ATTRIBUTE13 | — | — |
| 7 | HzCustProfileAmtsFAttribute14 | ATTRIBUTE14 | — | — |
| 8 | HzCustProfileAmtsFAttribute15 | ATTRIBUTE15 | — | — |
| 9 | HzCustProfileAmtsFAttribute2 | ATTRIBUTE2 | — | — |
| 10 | HzCustProfileAmtsFAttribute3 | ATTRIBUTE3 | — | — |
| 11 | HzCustProfileAmtsFAttribute4 | ATTRIBUTE4 | — | — |
| 12 | HzCustProfileAmtsFAttribute5 | ATTRIBUTE5 | — | — |
| 13 | HzCustProfileAmtsFAttribute6 | ATTRIBUTE6 | — | — |
| 14 | HzCustProfileAmtsFAttribute7 | ATTRIBUTE7 | — | — |
| 15 | HzCustProfileAmtsFAttribute8 | ATTRIBUTE8 | — | — |
| 16 | HzCustProfileAmtsFAttribute9 | ATTRIBUTE9 | — | — |
| 17 | HzCustProfileAmtsFAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 18 | HzCustProfileAmtsFAutoRecMinReceiptAmount | AUTO_REC_MIN_RECEIPT_AMOUNT | — | ✅ |
| 19 | HzCustProfileAmtsFCreatedBy | CREATED_BY | — | ✅ |
| 20 | HzCustProfileAmtsFCreatedByModule | CREATED_BY_MODULE | — | ✅ |
| 21 | HzCustProfileAmtsFCreationDate | CREATION_DATE | — | ✅ |
| 22 | HzCustProfileAmtsFCurrencyCode | CURRENCY_CODE | — | ✅ |
| 23 | HzCustProfileAmtsFCustAccountId | CUST_ACCOUNT_ID | — | ✅ |
| 24 | HzCustProfileAmtsFCustAccountProfileId | CUST_ACCOUNT_PROFILE_ID | — | ✅ |
| 25 | HzCustProfileAmtsFCustAcctProfileAmtId | CUST_ACCT_PROFILE_AMT_ID | 🔑 | ✅ |
| 26 | HzCustProfileAmtsFEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 27 | HzCustProfileAmtsFEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 28 | HzCustProfileAmtsFExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 29 | HzCustProfileAmtsFExpirationDate | EXPIRATION_DATE | — | ✅ |
| 30 | HzCustProfileAmtsFGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 31 | HzCustProfileAmtsFGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 32 | HzCustProfileAmtsFGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 33 | HzCustProfileAmtsFGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 34 | HzCustProfileAmtsFGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 35 | HzCustProfileAmtsFGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 36 | HzCustProfileAmtsFGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 37 | HzCustProfileAmtsFGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 38 | HzCustProfileAmtsFGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 39 | HzCustProfileAmtsFGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 40 | HzCustProfileAmtsFGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 41 | HzCustProfileAmtsFGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 42 | HzCustProfileAmtsFGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 43 | HzCustProfileAmtsFGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 44 | HzCustProfileAmtsFGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 45 | HzCustProfileAmtsFGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 46 | HzCustProfileAmtsFGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 47 | HzCustProfileAmtsFGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 48 | HzCustProfileAmtsFGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 49 | HzCustProfileAmtsFGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 50 | HzCustProfileAmtsFGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 51 | HzCustProfileAmtsFInterestFixedAmount | INTEREST_FIXED_AMOUNT | — | ✅ |
| 52 | HzCustProfileAmtsFInterestRate | INTEREST_RATE | — | ✅ |
| 53 | HzCustProfileAmtsFInterestScheduleId | INTEREST_SCHEDULE_ID | — | ✅ |
| 54 | HzCustProfileAmtsFInterestType | INTEREST_TYPE | — | ✅ |
| 55 | HzCustProfileAmtsFJgzzAttribute1 | JGZZ_ATTRIBUTE1 | — | — |
| 56 | HzCustProfileAmtsFJgzzAttribute10 | JGZZ_ATTRIBUTE10 | — | — |
| 57 | HzCustProfileAmtsFJgzzAttribute11 | JGZZ_ATTRIBUTE11 | — | — |
| 58 | HzCustProfileAmtsFJgzzAttribute12 | JGZZ_ATTRIBUTE12 | — | — |
| 59 | HzCustProfileAmtsFJgzzAttribute13 | JGZZ_ATTRIBUTE13 | — | — |
| 60 | HzCustProfileAmtsFJgzzAttribute14 | JGZZ_ATTRIBUTE14 | — | — |
| 61 | HzCustProfileAmtsFJgzzAttribute15 | JGZZ_ATTRIBUTE15 | — | — |
| 62 | HzCustProfileAmtsFJgzzAttribute2 | JGZZ_ATTRIBUTE2 | — | — |
| 63 | HzCustProfileAmtsFJgzzAttribute3 | JGZZ_ATTRIBUTE3 | — | — |
| 64 | HzCustProfileAmtsFJgzzAttribute4 | JGZZ_ATTRIBUTE4 | — | — |
| 65 | HzCustProfileAmtsFJgzzAttribute5 | JGZZ_ATTRIBUTE5 | — | — |
| 66 | HzCustProfileAmtsFJgzzAttribute6 | JGZZ_ATTRIBUTE6 | — | — |
| 67 | HzCustProfileAmtsFJgzzAttribute7 | JGZZ_ATTRIBUTE7 | — | — |
| 68 | HzCustProfileAmtsFJgzzAttribute8 | JGZZ_ATTRIBUTE8 | — | — |
| 69 | HzCustProfileAmtsFJgzzAttribute9 | JGZZ_ATTRIBUTE9 | — | — |
| 70 | HzCustProfileAmtsFJgzzAttributeCategory | JGZZ_ATTRIBUTE_CATEGORY | — | — |
| 71 | HzCustProfileAmtsFLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 72 | HzCustProfileAmtsFLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 73 | HzCustProfileAmtsFLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 74 | HzCustProfileAmtsFMaxInterestCharge | MAX_INTEREST_CHARGE | — | ✅ |
| 75 | HzCustProfileAmtsFMinDunningAmount | MIN_DUNNING_AMOUNT | — | ✅ |
| 76 | HzCustProfileAmtsFMinDunningInvoiceAmount | MIN_DUNNING_INVOICE_AMOUNT | — | ✅ |
| 77 | HzCustProfileAmtsFMinFcBalanceAmount | MIN_FC_BALANCE_AMOUNT | — | ✅ |
| 78 | HzCustProfileAmtsFMinFcBalanceOverdueType | MIN_FC_BALANCE_OVERDUE_TYPE | — | ✅ |
| 79 | HzCustProfileAmtsFMinFcBalancePercent | MIN_FC_BALANCE_PERCENT | — | ✅ |
| 80 | HzCustProfileAmtsFMinFcInvoiceAmount | MIN_FC_INVOICE_AMOUNT | — | ✅ |
| 81 | HzCustProfileAmtsFMinFcInvoiceOverdueType | MIN_FC_INVOICE_OVERDUE_TYPE | — | ✅ |
| 82 | HzCustProfileAmtsFMinFcInvoicePercent | MIN_FC_INVOICE_PERCENT | — | ✅ |
| 83 | HzCustProfileAmtsFMinInterestCharge | MIN_INTEREST_CHARGE | — | ✅ |
| 84 | HzCustProfileAmtsFMinStatementAmount | MIN_STATEMENT_AMOUNT | — | ✅ |
| 85 | HzCustProfileAmtsFObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 86 | HzCustProfileAmtsFOverallCreditLimit | OVERALL_CREDIT_LIMIT | — | ✅ |
| 87 | HzCustProfileAmtsFPenaltyFixedAmount | PENALTY_FIXED_AMOUNT | — | ✅ |
| 88 | HzCustProfileAmtsFPenaltyRate | PENALTY_RATE | — | ✅ |
| 89 | HzCustProfileAmtsFPenaltyScheduleId | PENALTY_SCHEDULE_ID | — | ✅ |
| 90 | HzCustProfileAmtsFPenaltyType | PENALTY_TYPE | — | ✅ |
| 91 | HzCustProfileAmtsFProgramApplicationId | PROGRAM_APPLICATION_ID | — | ✅ |
| 92 | HzCustProfileAmtsFProgramId | PROGRAM_ID | — | ✅ |
| 93 | HzCustProfileAmtsFProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 94 | HzCustProfileAmtsFRequestId | REQUEST_ID | — | ✅ |
| 95 | HzCustProfileAmtsFSiteUseId | SITE_USE_ID | — | ✅ |
| 96 | HzCustProfileAmtsFTrxCreditLimit | TRX_CREDIT_LIMIT | — | ✅ |
| 97 | HzCustProfileAmtsFWhUpdateDate | WH_UPDATE_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
