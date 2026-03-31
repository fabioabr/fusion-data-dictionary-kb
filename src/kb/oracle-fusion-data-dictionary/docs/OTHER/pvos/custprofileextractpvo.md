---
id: DOC-OTHER-PVO-CustProfileExtractPVO
doc_type: system-doc
title: "CustProfileExtractPVO — PVO Cross-Module"
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
  - CustProfileExtractPVO
  - custprofileextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CustProfileExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cust Profile Extract. Acessa as tabelas: HZ_CUSTOMER_PROFILES_F.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.CustProfileExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 147 | 1 | 3 | 84 | 57% |

---

## 🔗 Tabelas Relacionadas

- [[hz_customer_profiles_f|HZ_CUSTOMER_PROFILES_F]] — 147 atributos (3 PKs, 84 BICC)

---

## ⚙️ Atributos

### [[hz_customer_profiles_f|HZ_CUSTOMER_PROFILES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HzCustProfileFAccountStatus | ACCOUNT_STATUS | — | ✅ |
| 2 | HzCustProfileFApplicationId | APPLICATION_ID | — | ✅ |
| 3 | HzCustProfileFAttribute1 | ATTRIBUTE1 | — | — |
| 4 | HzCustProfileFAttribute10 | ATTRIBUTE10 | — | — |
| 5 | HzCustProfileFAttribute11 | ATTRIBUTE11 | — | — |
| 6 | HzCustProfileFAttribute12 | ATTRIBUTE12 | — | — |
| 7 | HzCustProfileFAttribute13 | ATTRIBUTE13 | — | — |
| 8 | HzCustProfileFAttribute14 | ATTRIBUTE14 | — | — |
| 9 | HzCustProfileFAttribute15 | ATTRIBUTE15 | — | — |
| 10 | HzCustProfileFAttribute2 | ATTRIBUTE2 | — | — |
| 11 | HzCustProfileFAttribute3 | ATTRIBUTE3 | — | — |
| 12 | HzCustProfileFAttribute4 | ATTRIBUTE4 | — | — |
| 13 | HzCustProfileFAttribute5 | ATTRIBUTE5 | — | — |
| 14 | HzCustProfileFAttribute6 | ATTRIBUTE6 | — | — |
| 15 | HzCustProfileFAttribute7 | ATTRIBUTE7 | — | — |
| 16 | HzCustProfileFAttribute8 | ATTRIBUTE8 | — | — |
| 17 | HzCustProfileFAttribute9 | ATTRIBUTE9 | — | — |
| 18 | HzCustProfileFAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 19 | HzCustProfileFAutoRecInclDisputedFlag | AUTO_REC_INCL_DISPUTED_FLAG | — | ✅ |
| 20 | HzCustProfileFAutocashHierarchyId | AUTOCASH_HIERARCHY_ID | — | ✅ |
| 21 | HzCustProfileFAutocashHierarchyIdForAdr | AUTOCASH_HIERARCHY_ID_FOR_ADR | — | ✅ |
| 22 | HzCustProfileFAutomatchRuleId | AUTOMATCH_RULE_ID | — | ✅ |
| 23 | HzCustProfileFB2bTpCode | B2B_TP_CODE | — | ✅ |
| 24 | HzCustProfileFChargeBeginDate | CHARGE_BEGIN_DATE | — | ✅ |
| 25 | HzCustProfileFChargeOnFinanceChargeFlag | CHARGE_ON_FINANCE_CHARGE_FLAG | — | ✅ |
| 26 | HzCustProfileFClearingDays | CLEARING_DAYS | — | ✅ |
| 27 | HzCustProfileFCollectorId | COLLECTOR_ID | — | ✅ |
| 28 | HzCustProfileFConsBillLevel | CONS_BILL_LEVEL | — | ✅ |
| 29 | HzCustProfileFConsInvFlag | CONS_INV_FLAG | — | ✅ |
| 30 | HzCustProfileFConsInvType | CONS_INV_TYPE | — | ✅ |
| 31 | HzCustProfileFCreatedBy | CREATED_BY | — | ✅ |
| 32 | HzCustProfileFCreatedByModule | CREATED_BY_MODULE | — | ✅ |
| 33 | HzCustProfileFCreationDate | CREATION_DATE | — | ✅ |
| 34 | HzCustProfileFCreditAnalystId | CREDIT_ANALYST_ID | — | ✅ |
| 35 | HzCustProfileFCreditBalanceStatements | CREDIT_BALANCE_STATEMENTS | — | ✅ |
| 36 | HzCustProfileFCreditChecking | CREDIT_CHECKING | — | ✅ |
| 37 | HzCustProfileFCreditClassification | CREDIT_CLASSIFICATION | — | ✅ |
| 38 | HzCustProfileFCreditCurrencyCode | CREDIT_CURRENCY_CODE | — | ✅ |
| 39 | HzCustProfileFCreditHold | CREDIT_HOLD | — | ✅ |
| 40 | HzCustProfileFCreditItemsFlag | CREDIT_ITEMS_FLAG | — | ✅ |
| 41 | HzCustProfileFCreditLimit | CREDIT_LIMIT | — | ✅ |
| 42 | HzCustProfileFCreditRating | CREDIT_RATING | — | ✅ |
| 43 | HzCustProfileFCreditReviewCycle | CREDIT_REVIEW_CYCLE | — | ✅ |
| 44 | HzCustProfileFCustAccountId | CUST_ACCOUNT_ID | — | ✅ |
| 45 | HzCustProfileFCustAccountProfileId | CUST_ACCOUNT_PROFILE_ID | 🔑 | ✅ |
| 46 | HzCustProfileFDiscountGraceDays | DISCOUNT_GRACE_DAYS | — | ✅ |
| 47 | HzCustProfileFDiscountTerms | DISCOUNT_TERMS | — | ✅ |
| 48 | HzCustProfileFDisputedTransactionsFlag | DISPUTED_TRANSACTIONS_FLAG | — | ✅ |
| 49 | HzCustProfileFDunningLetters | DUNNING_LETTERS | — | ✅ |
| 50 | HzCustProfileFEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 51 | HzCustProfileFEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 52 | HzCustProfileFExceptionRuleId | EXCEPTION_RULE_ID | — | ✅ |
| 53 | HzCustProfileFExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 54 | HzCustProfileFGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 55 | HzCustProfileFGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 56 | HzCustProfileFGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 57 | HzCustProfileFGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 58 | HzCustProfileFGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 59 | HzCustProfileFGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 60 | HzCustProfileFGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 61 | HzCustProfileFGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 62 | HzCustProfileFGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 63 | HzCustProfileFGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 64 | HzCustProfileFGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 65 | HzCustProfileFGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 66 | HzCustProfileFGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 67 | HzCustProfileFGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 68 | HzCustProfileFGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 69 | HzCustProfileFGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 70 | HzCustProfileFGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 71 | HzCustProfileFGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 72 | HzCustProfileFGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 73 | HzCustProfileFGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 74 | HzCustProfileFGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 75 | HzCustProfileFGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 76 | HzCustProfileFGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 77 | HzCustProfileFGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 78 | HzCustProfileFGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 79 | HzCustProfileFGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 80 | HzCustProfileFGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 81 | HzCustProfileFGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 82 | HzCustProfileFGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 83 | HzCustProfileFGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 84 | HzCustProfileFGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 85 | HzCustProfileFGroupingRuleId | GROUPING_RULE_ID | — | ✅ |
| 86 | HzCustProfileFHoldChargedInvoicesFlag | HOLD_CHARGED_INVOICES_FLAG | — | ✅ |
| 87 | HzCustProfileFInterestCalculationPeriod | INTEREST_CALCULATION_PERIOD | — | ✅ |
| 88 | HzCustProfileFInterestCharges | INTEREST_CHARGES | — | ✅ |
| 89 | HzCustProfileFInterestPeriodDays | INTEREST_PERIOD_DAYS | — | ✅ |
| 90 | HzCustProfileFJgzzAttribute1 | JGZZ_ATTRIBUTE1 | — | — |
| 91 | HzCustProfileFJgzzAttribute10 | JGZZ_ATTRIBUTE10 | — | — |
| 92 | HzCustProfileFJgzzAttribute11 | JGZZ_ATTRIBUTE11 | — | — |
| 93 | HzCustProfileFJgzzAttribute12 | JGZZ_ATTRIBUTE12 | — | — |
| 94 | HzCustProfileFJgzzAttribute13 | JGZZ_ATTRIBUTE13 | — | — |
| 95 | HzCustProfileFJgzzAttribute14 | JGZZ_ATTRIBUTE14 | — | — |
| 96 | HzCustProfileFJgzzAttribute15 | JGZZ_ATTRIBUTE15 | — | — |
| 97 | HzCustProfileFJgzzAttribute2 | JGZZ_ATTRIBUTE2 | — | — |
| 98 | HzCustProfileFJgzzAttribute3 | JGZZ_ATTRIBUTE3 | — | — |
| 99 | HzCustProfileFJgzzAttribute4 | JGZZ_ATTRIBUTE4 | — | — |
| 100 | HzCustProfileFJgzzAttribute5 | JGZZ_ATTRIBUTE5 | — | — |
| 101 | HzCustProfileFJgzzAttribute6 | JGZZ_ATTRIBUTE6 | — | — |
| 102 | HzCustProfileFJgzzAttribute7 | JGZZ_ATTRIBUTE7 | — | — |
| 103 | HzCustProfileFJgzzAttribute8 | JGZZ_ATTRIBUTE8 | — | — |
| 104 | HzCustProfileFJgzzAttribute9 | JGZZ_ATTRIBUTE9 | — | — |
| 105 | HzCustProfileFJgzzAttributeCategory | JGZZ_ATTRIBUTE_CATEGORY | — | — |
| 106 | HzCustProfileFLastCreditReviewDate | LAST_CREDIT_REVIEW_DATE | — | ✅ |
| 107 | HzCustProfileFLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 108 | HzCustProfileFLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 109 | HzCustProfileFLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 110 | HzCustProfileFLateChargeCalculationTrx | LATE_CHARGE_CALCULATION_TRX | — | ✅ |
| 111 | HzCustProfileFLateChargeTermId | LATE_CHARGE_TERM_ID | — | ✅ |
| 112 | HzCustProfileFLateChargeType | LATE_CHARGE_TYPE | — | ✅ |
| 113 | HzCustProfileFLockboxMatchingOption | LOCKBOX_MATCHING_OPTION | — | ✅ |
| 114 | HzCustProfileFMatchByAutoupdateFlag | MATCH_BY_AUTOUPDATE_FLAG | — | ✅ |
| 115 | HzCustProfileFMessageTextId | MESSAGE_TEXT_ID | — | ✅ |
| 116 | HzCustProfileFMultipleInterestRatesFlag | MULTIPLE_INTEREST_RATES_FLAG | — | ✅ |
| 117 | HzCustProfileFNextCreditReviewDate | NEXT_CREDIT_REVIEW_DATE | — | ✅ |
| 118 | HzCustProfileFObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 119 | HzCustProfileFOffsetDays | OFFSET_DAYS | — | ✅ |
| 120 | HzCustProfileFOrderAmountLimit | ORDER_AMOUNT_LIMIT | — | ✅ |
| 121 | HzCustProfileFOverrideTerms | OVERRIDE_TERMS | — | ✅ |
| 122 | HzCustProfileFPartyId | PARTY_ID | — | ✅ |
| 123 | HzCustProfileFPaymentGraceDays | PAYMENT_GRACE_DAYS | — | ✅ |
| 124 | HzCustProfileFPercentCollectable | PERCENT_COLLECTABLE | — | ✅ |
| 125 | HzCustProfileFPrefContactMethod | PREF_CONTACT_METHOD | — | ✅ |
| 126 | HzCustProfileFPrintingOptionCode | PRINTING_OPTION_CODE | — | ✅ |
| 127 | HzCustProfileFProfileClassId | PROFILE_CLASS_ID | — | ✅ |
| 128 | HzCustProfileFProgramApplicationId | PROGRAM_APPLICATION_ID | — | ✅ |
| 129 | HzCustProfileFProgramId | PROGRAM_ID | — | ✅ |
| 130 | HzCustProfileFProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 131 | HzCustProfileFRequestId | REQUEST_ID | — | ✅ |
| 132 | HzCustProfileFReviewCycle | REVIEW_CYCLE | — | ✅ |
| 133 | HzCustProfileFRiskCode | RISK_CODE | — | ✅ |
| 134 | HzCustProfileFSendStatements | SEND_STATEMENTS | — | ✅ |
| 135 | HzCustProfileFSiteUseId | SITE_USE_ID | — | ✅ |
| 136 | HzCustProfileFStandardTerms | STANDARD_TERMS | — | ✅ |
| 137 | HzCustProfileFStatementCycleId | STATEMENT_CYCLE_ID | — | ✅ |
| 138 | HzCustProfileFStatus | STATUS | — | ✅ |
| 139 | HzCustProfileFStmtDeliveryMethod | STMT_DELIVERY_METHOD | — | ✅ |
| 140 | HzCustProfileFTaxPrintingOption | TAX_PRINTING_OPTION | — | ✅ |
| 141 | HzCustProfileFTolerance | TOLERANCE | — | ✅ |
| 142 | HzCustProfileFTxnDeliveryMethod | TXN_DELIVERY_METHOD | — | ✅ |
| 143 | HzCustProfileFWhUpdateDate | WH_UPDATE_DATE | — | ✅ |
| 144 | HzCustProfileFXmlCbFlag | XML_CB_FLAG | — | ✅ |
| 145 | HzCustProfileFXmlCmFlag | XML_CM_FLAG | — | ✅ |
| 146 | HzCustProfileFXmlDmFlag | XML_DM_FLAG | — | ✅ |
| 147 | HzCustProfileFXmlInvFlag | XML_INV_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
