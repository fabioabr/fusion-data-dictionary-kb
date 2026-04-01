---
id: DOC-AR-PVO-CustomerProfile
doc_type: system-doc
title: "CustomerProfile — PVO Accounts Receivable"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ar
  - data-dictionary
  - pvo
  - bicc
aliases:
  - CustomerProfile
  - customerprofile
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CustomerProfile

## 📌 Visão Geral

Extrai os perfis de cliente no nível de conta, com dados de hierarquia de cobrança, limites de crédito por moeda, termos de pagamento e regras de agrupamento de faturas. Essencial para parametrização de políticas comerciais e análise de risco por cliente.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.CustomerProfile`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 320 | 14 | 1 | 110 | 34% |

---

## 🔗 Tabelas Relacionadas

- [[ar_app_exception_rules|AR_APP_EXCEPTION_RULES]] — 13 atributos (2 BICC)
- [[ar_autocash_hierarchies|AR_AUTOCASH_HIERARCHIES]] — 4 atributos (2 BICC)
- [[ar_automatch_rules|AR_AUTOMATCH_RULES]] — 26 atributos (2 BICC)
- [[ar_charge_schedules|AR_CHARGE_SCHEDULES]] — 3 atributos (1 BICC)
- [[ar_collectors|AR_COLLECTORS]] — 18 atributos (6 BICC)
- [[ar_standard_text_tl|AR_STANDARD_TEXT_TL]] — 10 atributos (2 BICC)
- [[ar_statement_cycles|AR_STATEMENT_CYCLES]] — 3 atributos (1 BICC)
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 12 atributos (1 BICC)
- [[hz_customer_profiles_f|HZ_CUSTOMER_PROFILES_F]] — 84 atributos (1 PKs, 55 BICC)
- [[hz_cust_profile_amts_f|HZ_CUST_PROFILE_AMTS_F]] — 46 atributos (28 BICC)
- [[hz_cust_profile_classes|HZ_CUST_PROFILE_CLASSES]] — 60 atributos (5 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 4 atributos (1 BICC)
- [[ra_grouping_rules|RA_GROUPING_RULES]] — 13 atributos (2 BICC)
- [[ra_terms_tl|RA_TERMS_TL]] — 24 atributos (2 BICC)

---

## ⚙️ Atributos

### [[ar_app_exception_rules|AR_APP_EXCEPTION_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExceptionRuleActiveFlag | ACTIVE_FLAG | — | — |
| 2 | ExceptionRuleCreatedBy | CREATED_BY | — | — |
| 3 | ExceptionRuleCreationDate | CREATION_DATE | — | — |
| 4 | ExceptionRuleDescription | DESCRIPTION | — | — |
| 5 | ExceptionRuleEndDate | END_DATE | — | — |
| 6 | ExceptionRuleExceptionRuleId | EXCEPTION_RULE_ID | — | — |
| 7 | ExceptionRuleLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ExceptionRuleLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ExceptionRuleLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ExceptionRuleName | NAME | — | ✅ |
| 11 | ExceptionRuleObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ExceptionRuleSetId | SET_ID | — | — |
| 13 | ExceptionRuleStartDate | START_DATE | — | — |

### [[ar_autocash_hierarchies|AR_AUTOCASH_HIERARCHIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AutoCshHierarchyAutocashHierarchyId | AUTOCASH_HIERARCHY_ID | — | — |
| 2 | AutoCshHierarchyForAdrAutocashHierarchyId | AUTOCASH_HIERARCHY_ID | — | — |
| 3 | AutoCshHierarchyForAdrHierarchyName | HIERARCHY_NAME | — | ✅ |
| 4 | AutoCshHierarchyHierarchyName | HIERARCHY_NAME | — | ✅ |

### [[ar_automatch_rules|AR_AUTOMATCH_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AutomatchRuleActiveFlag | ACTIVE_FLAG | — | — |
| 2 | AutomatchRuleAmountWeight | AMOUNT_WEIGHT | — | — |
| 3 | AutomatchRuleAutomatchRuleId | AUTOMATCH_RULE_ID | — | — |
| 4 | AutomatchRuleCreatedBy | CREATED_BY | — | — |
| 5 | AutomatchRuleCreationDate | CREATION_DATE | — | — |
| 6 | AutomatchRuleCustomerThreshold | CUSTOMER_THRESHOLD | — | — |
| 7 | AutomatchRuleCustomerWeight | CUSTOMER_WEIGHT | — | — |
| 8 | AutomatchRuleDescription | DESCRIPTION | — | — |
| 9 | AutomatchRuleEndDate | END_DATE | — | — |
| 10 | AutomatchRuleLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | AutomatchRuleLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | AutomatchRuleLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | AutomatchRuleMinMatchThreshold | MIN_MATCH_THRESHOLD | — | — |
| 14 | AutomatchRuleName | NAME | — | ✅ |
| 15 | AutomatchRuleNetFreightWeight | NET_FREIGHT_WEIGHT | — | — |
| 16 | AutomatchRuleNetTaxFreightWeight | NET_TAX_FREIGHT_WEIGHT | — | — |
| 17 | AutomatchRuleNetTaxWeight | NET_TAX_WEIGHT | — | — |
| 18 | AutomatchRuleNetUndiscWeight | NET_UNDISC_WEIGHT | — | — |
| 19 | AutomatchRuleNumberOfDaysClosed | NUMBER_OF_DAYS_CLOSED | — | — |
| 20 | AutomatchRuleObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | AutomatchRuleRemittanceRegexp | REMITTANCE_REGEXP | — | — |
| 22 | AutomatchRuleSetId | SET_ID | — | — |
| 23 | AutomatchRuleStartDate | START_DATE | — | — |
| 24 | AutomatchRuleTransactionRegexp | TRANSACTION_REGEXP | — | — |
| 25 | AutomatchRuleTransactionThreshold | TRANSACTION_THRESHOLD | — | — |
| 26 | AutomatchRuleTransactionWeight | TRANSACTION_WEIGHT | — | — |

### [[ar_charge_schedules|AR_CHARGE_SCHEDULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChargeSchedulesScheduleDescription | SCHEDULE_DESCRIPTION | — | — |
| 2 | ChargeSchedulesScheduleId | SCHEDULE_ID | — | — |
| 3 | ChargeSchedulesScheduleName | SCHEDULE_NAME | — | ✅ |

### [[ar_collectors|AR_COLLECTORS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CollectorsAlias | ALIAS | — | — |
| 2 | CollectorsAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 3 | CollectorsCollectorId | COLLECTOR_ID | — | — |
| 4 | CollectorsCreatedBy | CREATED_BY | — | ✅ |
| 5 | CollectorsCreationDate | CREATION_DATE | — | ✅ |
| 6 | CollectorsDescription | DESCRIPTION | — | — |
| 7 | CollectorsEmployeeId | EMPLOYEE_ID | — | — |
| 8 | CollectorsInactiveDate | INACTIVE_DATE | — | — |
| 9 | CollectorsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | CollectorsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | CollectorsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | CollectorsName | NAME | — | ✅ |
| 13 | CollectorsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | CollectorsResourceId | RESOURCE_ID | — | — |
| 15 | CollectorsResourceType | RESOURCE_TYPE | — | — |
| 16 | CollectorsSetId | SET_ID | — | — |
| 17 | CollectorsStatus | STATUS | — | — |
| 18 | CollectorsTelephoneNumber | TELEPHONE_NUMBER | — | — |

### [[ar_standard_text_tl|AR_STANDARD_TEXT_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StdTextTransTLCreatedBy | CREATED_BY | — | — |
| 2 | StdTextTransTLCreationDate | CREATION_DATE | — | — |
| 3 | StdTextTransTLLanguage | LANGUAGE | — | — |
| 4 | StdTextTransTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | StdTextTransTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | StdTextTransTLLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | StdTextTransTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | StdTextTransTLSourceLang | SOURCE_LANG | — | — |
| 9 | StdTextTransTLStandardTextId | STANDARD_TEXT_ID | — | — |
| 10 | StdTextTransTLText | TEXT | — | ✅ |

### [[ar_statement_cycles|AR_STATEMENT_CYCLES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StatementCycleName | NAME | — | ✅ |
| 2 | StatementCycleObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | StatementCycleStatementCycleId | STATEMENT_CYCLE_ID | — | — |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlConvTypeConversionType | CONVERSION_TYPE | — | — |
| 2 | GlConvTypeEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 3 | GlConvTypeEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 4 | GlConvTypeFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 5 | GlConvTypeFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 6 | GlConvTypeFemScenario | FEM_SCENARIO | — | — |
| 7 | GlConvTypeFemTimeframe | FEM_TIMEFRAME | — | — |
| 8 | GlConvTypePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 9 | GlConvTypeSecurityFlag | SECURITY_FLAG | — | — |
| 10 | GlConvTypeUserConversionType | USER_CONVERSION_TYPE | — | ✅ |
| 11 | GlConvTypeUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |
| 12 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[hz_customer_profiles_f|HZ_CUSTOMER_PROFILES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreditLimit | CREDIT_LIMIT | — | ✅ |
| 2 | CustAccountProfileId | CUST_ACCOUNT_PROFILE_ID | 🔑 | ✅ |
| 3 | CustomerProfileAccountStatus | ACCOUNT_STATUS | — | ✅ |
| 4 | CustomerProfileApplicationId | APPLICATION_ID | — | — |
| 5 | CustomerProfileAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 6 | CustomerProfileAutoRecInclDisputedFlag | AUTO_REC_INCL_DISPUTED_FLAG | — | ✅ |
| 7 | CustomerProfileAutocashHierarchyId | AUTOCASH_HIERARCHY_ID | — | — |
| 8 | CustomerProfileAutocashHierarchyIdForAdr | AUTOCASH_HIERARCHY_ID_FOR_ADR | — | — |
| 9 | CustomerProfileAutomatchRuleId | AUTOMATCH_RULE_ID | — | — |
| 10 | CustomerProfileB2bTpCode | B2B_TP_CODE | — | ✅ |
| 11 | CustomerProfileChargeBeginDate | CHARGE_BEGIN_DATE | — | ✅ |
| 12 | CustomerProfileChargeOnFinanceChargeFlag | CHARGE_ON_FINANCE_CHARGE_FLAG | — | ✅ |
| 13 | CustomerProfileClearingDays | CLEARING_DAYS | — | — |
| 14 | CustomerProfileCollectorId | COLLECTOR_ID | — | ✅ |
| 15 | CustomerProfileConsBillLevel | CONS_BILL_LEVEL | — | ✅ |
| 16 | CustomerProfileConsInvFlag | CONS_INV_FLAG | — | ✅ |
| 17 | CustomerProfileConsInvType | CONS_INV_TYPE | — | ✅ |
| 18 | CustomerProfileCreatedBy | CREATED_BY | — | ✅ |
| 19 | CustomerProfileCreatedByModule | CREATED_BY_MODULE | — | ✅ |
| 20 | CustomerProfileCreationDate | CREATION_DATE | — | ✅ |
| 21 | CustomerProfileCreditAnalystId | CREDIT_ANALYST_ID | — | — |
| 22 | CustomerProfileCreditBalanceStatements | CREDIT_BALANCE_STATEMENTS | — | ✅ |
| 23 | CustomerProfileCreditChecking | CREDIT_CHECKING | — | ✅ |
| 24 | CustomerProfileCreditClassification | CREDIT_CLASSIFICATION | — | ✅ |
| 25 | CustomerProfileCreditCurrencyCode | CREDIT_CURRENCY_CODE | — | ✅ |
| 26 | CustomerProfileCreditHold | CREDIT_HOLD | — | ✅ |
| 27 | CustomerProfileCreditItemsFlag | CREDIT_ITEMS_FLAG | — | — |
| 28 | CustomerProfileCreditRating | CREDIT_RATING | — | ✅ |
| 29 | CustomerProfileCustAccountId | CUST_ACCOUNT_ID | — | — |
| 30 | CustomerProfileDiscountGraceDays | DISCOUNT_GRACE_DAYS | — | ✅ |
| 31 | CustomerProfileDiscountTerms | DISCOUNT_TERMS | — | ✅ |
| 32 | CustomerProfileDisputedTransactionsFlag | DISPUTED_TRANSACTIONS_FLAG | — | — |
| 33 | CustomerProfileDunningLetters | DUNNING_LETTERS | — | ✅ |
| 34 | CustomerProfileEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 35 | CustomerProfileEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 36 | CustomerProfileExceptionRuleId | EXCEPTION_RULE_ID | — | — |
| 37 | CustomerProfileGroupingRuleId | GROUPING_RULE_ID | — | — |
| 38 | CustomerProfileHoldChargedInvoicesFlag | HOLD_CHARGED_INVOICES_FLAG | — | ✅ |
| 39 | CustomerProfileInterestCalculationPeriod | INTEREST_CALCULATION_PERIOD | — | ✅ |
| 40 | CustomerProfileInterestCharges | INTEREST_CHARGES | — | ✅ |
| 41 | CustomerProfileInterestPeriodDays | INTEREST_PERIOD_DAYS | — | ✅ |
| 42 | CustomerProfileJgzzAttributeCategory | JGZZ_ATTRIBUTE_CATEGORY | — | — |
| 43 | CustomerProfileLastCreditReviewDate | LAST_CREDIT_REVIEW_DATE | — | — |
| 44 | CustomerProfileLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 45 | CustomerProfileLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 46 | CustomerProfileLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 47 | CustomerProfileLateChargeCalculationTrx | LATE_CHARGE_CALCULATION_TRX | — | ✅ |
| 48 | CustomerProfileLateChargeTermId | LATE_CHARGE_TERM_ID | — | ✅ |
| 49 | CustomerProfileLateChargeType | LATE_CHARGE_TYPE | — | ✅ |
| 50 | CustomerProfileLockboxMatchingOption | LOCKBOX_MATCHING_OPTION | — | ✅ |
| 51 | CustomerProfileMatchByAutoupdateFlag | MATCH_BY_AUTOUPDATE_FLAG | — | ✅ |
| 52 | CustomerProfileMessageTextId | MESSAGE_TEXT_ID | — | — |
| 53 | CustomerProfileMultipleInterestRatesFlag | MULTIPLE_INTEREST_RATES_FLAG | — | ✅ |
| 54 | CustomerProfileNextCreditReviewDate | NEXT_CREDIT_REVIEW_DATE | — | — |
| 55 | CustomerProfileObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 56 | CustomerProfileOrderAmountLimit | ORDER_AMOUNT_LIMIT | — | ✅ |
| 57 | CustomerProfileOverrideTerms | OVERRIDE_TERMS | — | ✅ |
| 58 | CustomerProfilePartyId | PARTY_ID | — | — |
| 59 | CustomerProfilePaymentGraceDays | PAYMENT_GRACE_DAYS | — | ✅ |
| 60 | CustomerProfilePercentCollectable | PERCENT_COLLECTABLE | — | ✅ |
| 61 | CustomerProfilePrefContactMethod | PREF_CONTACT_METHOD | — | ✅ |
| 62 | CustomerProfilePrintingOptionCode | PRINTING_OPTION_CODE | — | ✅ |
| 63 | CustomerProfileProfileClassId | PROFILE_CLASS_ID | — | — |
| 64 | CustomerProfileProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 65 | CustomerProfileProgramId | PROGRAM_ID | — | — |
| 66 | CustomerProfileProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 67 | CustomerProfileRequestId | REQUEST_ID | — | — |
| 68 | CustomerProfileReviewCycle | REVIEW_CYCLE | — | — |
| 69 | CustomerProfileRiskCode | RISK_CODE | — | ✅ |
| 70 | CustomerProfileSendStatements | SEND_STATEMENTS | — | ✅ |
| 71 | CustomerProfileSiteUseId | SITE_USE_ID | — | — |
| 72 | CustomerProfileStandardTerms | STANDARD_TERMS | — | ✅ |
| 73 | CustomerProfileStatementCycleId | STATEMENT_CYCLE_ID | — | — |
| 74 | CustomerProfileStatus | STATUS | — | — |
| 75 | CustomerProfileTaxPrintingOption | TAX_PRINTING_OPTION | — | — |
| 76 | CustomerProfileTolerance | TOLERANCE | — | ✅ |
| 77 | CustomerProfileTxnDeliveryMethod | TXN_DELIVERY_METHOD | — | ✅ |
| 78 | CustomerProfileWhUpdateDate | WH_UPDATE_DATE | — | — |
| 79 | CustomerProfileXmlCbFlag | XML_CB_FLAG | — | ✅ |
| 80 | CustomerProfileXmlCmFlag | XML_CM_FLAG | — | ✅ |
| 81 | CustomerProfileXmlDmFlag | XML_DM_FLAG | — | ✅ |
| 82 | CustomerProfileXmlInvFlag | XML_INV_FLAG | — | ✅ |
| 83 | ExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 84 | OffsetDays | OFFSET_DAYS | — | ✅ |

### [[hz_cust_profile_amts_f|HZ_CUST_PROFILE_AMTS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustomerFinancialProfileApplicationId | APPLICATION_ID | — | — |
| 2 | CustomerFinancialProfileAutoRecMinReceiptAmount | AUTO_REC_MIN_RECEIPT_AMOUNT | — | ✅ |
| 3 | CustomerFinancialProfileCreatedBy | CREATED_BY | — | ✅ |
| 4 | CustomerFinancialProfileCreatedByModule | CREATED_BY_MODULE | — | ✅ |
| 5 | CustomerFinancialProfileCreationDate | CREATION_DATE | — | ✅ |
| 6 | CustomerFinancialProfileCurrencyCode | CURRENCY_CODE | — | ✅ |
| 7 | CustomerFinancialProfileCustAccountId | CUST_ACCOUNT_ID | — | — |
| 8 | CustomerFinancialProfileCustAccountProfileId | CUST_ACCOUNT_PROFILE_ID | — | — |
| 9 | CustomerFinancialProfileCustAcctProfileAmtId | CUST_ACCT_PROFILE_AMT_ID | — | — |
| 10 | CustomerFinancialProfileEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 11 | CustomerFinancialProfileEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 12 | CustomerFinancialProfileExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 13 | CustomerFinancialProfileExpirationDate | EXPIRATION_DATE | — | — |
| 14 | CustomerFinancialProfileGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 15 | CustomerFinancialProfileInterestFixedAmount | INTEREST_FIXED_AMOUNT | — | ✅ |
| 16 | CustomerFinancialProfileInterestRate | INTEREST_RATE | — | ✅ |
| 17 | CustomerFinancialProfileInterestScheduleId | INTEREST_SCHEDULE_ID | — | ✅ |
| 18 | CustomerFinancialProfileInterestType | INTEREST_TYPE | — | ✅ |
| 19 | CustomerFinancialProfileJgzzAttributeCategory | JGZZ_ATTRIBUTE_CATEGORY | — | — |
| 20 | CustomerFinancialProfileLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | CustomerFinancialProfileLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 22 | CustomerFinancialProfileLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 23 | CustomerFinancialProfileMaxInterestCharge | MAX_INTEREST_CHARGE | — | ✅ |
| 24 | CustomerFinancialProfileMinDunningAmount | MIN_DUNNING_AMOUNT | — | ✅ |
| 25 | CustomerFinancialProfileMinDunningInvoiceAmount | MIN_DUNNING_INVOICE_AMOUNT | — | ✅ |
| 26 | CustomerFinancialProfileMinFcBalanceAmount | MIN_FC_BALANCE_AMOUNT | — | ✅ |
| 27 | CustomerFinancialProfileMinFcBalanceOverdueType | MIN_FC_BALANCE_OVERDUE_TYPE | — | ✅ |
| 28 | CustomerFinancialProfileMinFcBalancePercent | MIN_FC_BALANCE_PERCENT | — | ✅ |
| 29 | CustomerFinancialProfileMinFcInvoiceAmount | MIN_FC_INVOICE_AMOUNT | — | ✅ |
| 30 | CustomerFinancialProfileMinFcInvoiceOverdueType | MIN_FC_INVOICE_OVERDUE_TYPE | — | ✅ |
| 31 | CustomerFinancialProfileMinFcInvoicePercent | MIN_FC_INVOICE_PERCENT | — | ✅ |
| 32 | CustomerFinancialProfileMinInterestCharge | MIN_INTEREST_CHARGE | — | ✅ |
| 33 | CustomerFinancialProfileMinStatementAmount | MIN_STATEMENT_AMOUNT | — | ✅ |
| 34 | CustomerFinancialProfileObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 35 | CustomerFinancialProfileOverallCreditLimit | OVERALL_CREDIT_LIMIT | — | ✅ |
| 36 | CustomerFinancialProfilePenaltyFixedAmount | PENALTY_FIXED_AMOUNT | — | ✅ |
| 37 | CustomerFinancialProfilePenaltyRate | PENALTY_RATE | — | ✅ |
| 38 | CustomerFinancialProfilePenaltyScheduleId | PENALTY_SCHEDULE_ID | — | — |
| 39 | CustomerFinancialProfilePenaltyType | PENALTY_TYPE | — | ✅ |
| 40 | CustomerFinancialProfileProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 41 | CustomerFinancialProfileProgramId | PROGRAM_ID | — | — |
| 42 | CustomerFinancialProfileProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 43 | CustomerFinancialProfileRequestId | REQUEST_ID | — | — |
| 44 | CustomerFinancialProfileSiteUseId | SITE_USE_ID | — | — |
| 45 | CustomerFinancialProfileTrxCreditLimit | TRX_CREDIT_LIMIT | — | ✅ |
| 46 | CustomerFinancialProfileWhUpdateDate | WH_UPDATE_DATE | — | — |

### [[hz_cust_profile_classes|HZ_CUST_PROFILE_CLASSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustomerProfileClassesAutoRecInclDisputedFlag | AUTO_REC_INCL_DISPUTED_FLAG | — | — |
| 2 | CustomerProfileClassesAutocashHierarchyId | AUTOCASH_HIERARCHY_ID | — | — |
| 3 | CustomerProfileClassesAutocashHierarchyIdForAdr | AUTOCASH_HIERARCHY_ID_FOR_ADR | — | — |
| 4 | CustomerProfileClassesAutomatchRuleId | AUTOMATCH_RULE_ID | — | — |
| 5 | CustomerProfileClassesChargeBeginDate | CHARGE_BEGIN_DATE | — | — |
| 6 | CustomerProfileClassesChargeOnFinanceChargeFlag | CHARGE_ON_FINANCE_CHARGE_FLAG | — | — |
| 7 | CustomerProfileClassesCombineDunningLetters | COMBINE_DUNNING_LETTERS | — | — |
| 8 | CustomerProfileClassesConsBillLevel | CONS_BILL_LEVEL | — | — |
| 9 | CustomerProfileClassesConsInvFlag | CONS_INV_FLAG | — | — |
| 10 | CustomerProfileClassesConsInvType | CONS_INV_TYPE | — | — |
| 11 | CustomerProfileClassesCopyMethod | COPY_METHOD | — | — |
| 12 | CustomerProfileClassesCreatedBy | CREATED_BY | — | — |
| 13 | CustomerProfileClassesCreationDate | CREATION_DATE | — | — |
| 14 | CustomerProfileClassesCreditAnalystId | CREDIT_ANALYST_ID | — | — |
| 15 | CustomerProfileClassesCreditBalanceStatements | CREDIT_BALANCE_STATEMENTS | — | — |
| 16 | CustomerProfileClassesCreditChecking | CREDIT_CHECKING | — | — |
| 17 | CustomerProfileClassesCreditClassification | CREDIT_CLASSIFICATION | — | — |
| 18 | CustomerProfileClassesCreditItemsFlag | CREDIT_ITEMS_FLAG | — | — |
| 19 | CustomerProfileClassesDescription | DESCRIPTION | — | ✅ |
| 20 | CustomerProfileClassesDiscountGraceDays | DISCOUNT_GRACE_DAYS | — | — |
| 21 | CustomerProfileClassesDiscountTerms | DISCOUNT_TERMS | — | — |
| 22 | CustomerProfileClassesDisputedTransactionsFlag | DISPUTED_TRANSACTIONS_FLAG | — | — |
| 23 | CustomerProfileClassesDunningLetters | DUNNING_LETTERS | — | — |
| 24 | CustomerProfileClassesExceptionRuleId | EXCEPTION_RULE_ID | — | — |
| 25 | CustomerProfileClassesGroupingRuleId | GROUPING_RULE_ID | — | — |
| 26 | CustomerProfileClassesHoldChargedInvoicesFlag | HOLD_CHARGED_INVOICES_FLAG | — | — |
| 27 | CustomerProfileClassesInterestCalculationPeriod | INTEREST_CALCULATION_PERIOD | — | — |
| 28 | CustomerProfileClassesInterestCharges | INTEREST_CHARGES | — | — |
| 29 | CustomerProfileClassesInterestPeriodDays | INTEREST_PERIOD_DAYS | — | — |
| 30 | CustomerProfileClassesJgzzAttributeCategory | JGZZ_ATTRIBUTE_CATEGORY | — | — |
| 31 | CustomerProfileClassesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | CustomerProfileClassesLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 33 | CustomerProfileClassesLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 34 | CustomerProfileClassesLateChargeCalculationTrx | LATE_CHARGE_CALCULATION_TRX | — | — |
| 35 | CustomerProfileClassesLateChargeTermId | LATE_CHARGE_TERM_ID | — | — |
| 36 | CustomerProfileClassesLateChargeType | LATE_CHARGE_TYPE | — | — |
| 37 | CustomerProfileClassesLockboxMatchingOption | LOCKBOX_MATCHING_OPTION | — | — |
| 38 | CustomerProfileClassesMatchByAutoupdateFlag | MATCH_BY_AUTOUPDATE_FLAG | — | — |
| 39 | CustomerProfileClassesMessageTextId | MESSAGE_TEXT_ID | — | — |
| 40 | CustomerProfileClassesMultipleInterestRatesFlag | MULTIPLE_INTEREST_RATES_FLAG | — | — |
| 41 | CustomerProfileClassesName | NAME | — | ✅ |
| 42 | CustomerProfileClassesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 43 | CustomerProfileClassesOutsideReporting | OUTSIDE_REPORTING | — | — |
| 44 | CustomerProfileClassesOverrideTerms | OVERRIDE_TERMS | — | — |
| 45 | CustomerProfileClassesPaymentGraceDays | PAYMENT_GRACE_DAYS | — | — |
| 46 | CustomerProfileClassesPrefContactMethod | PREF_CONTACT_METHOD | — | — |
| 47 | CustomerProfileClassesProfileClassId | PROFILE_CLASS_ID | — | — |
| 48 | CustomerProfileClassesProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 49 | CustomerProfileClassesProgramId | PROGRAM_ID | — | — |
| 50 | CustomerProfileClassesProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 51 | CustomerProfileClassesRequestId | REQUEST_ID | — | — |
| 52 | CustomerProfileClassesReviewCycle | REVIEW_CYCLE | — | — |
| 53 | CustomerProfileClassesReviewCycleDays | REVIEW_CYCLE_DAYS | — | — |
| 54 | CustomerProfileClassesStandardTerms | STANDARD_TERMS | — | — |
| 55 | CustomerProfileClassesStatementCycleId | STATEMENT_CYCLE_ID | — | — |
| 56 | CustomerProfileClassesStatements | STATEMENTS | — | — |
| 57 | CustomerProfileClassesStatus | STATUS | — | — |
| 58 | CustomerProfileClassesTaxPrintingOption | TAX_PRINTING_OPTION | — | — |
| 59 | CustomerProfileClassesTolerance | TOLERANCE | — | — |
| 60 | CustomerProfileClassesWhUpdateDate | WH_UPDATE_DATE | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNameDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PersonNameEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonNameEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PersonNamePersonNameId | PERSON_NAME_ID | — | — |

### [[ra_grouping_rules|RA_GROUPING_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RaGrpRuleAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | RaGrpRuleCreatedBy | CREATED_BY | — | — |
| 3 | RaGrpRuleCreationDate | CREATION_DATE | — | — |
| 4 | RaGrpRuleDescription | DESCRIPTION | — | — |
| 5 | RaGrpRuleEndDate | END_DATE | — | — |
| 6 | RaGrpRuleGroupingRuleId | GROUPING_RULE_ID | — | — |
| 7 | RaGrpRuleLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | RaGrpRuleLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | RaGrpRuleLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | RaGrpRuleName | NAME | — | ✅ |
| 11 | RaGrpRuleObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | RaGrpRuleOrderingRuleId | ORDERING_RULE_ID | — | — |
| 13 | RaGrpRuleStartDate | START_DATE | — | — |

### [[ra_terms_tl|RA_TERMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LatePaymentTermTranslCreatedBy | CREATED_BY | — | — |
| 2 | LatePaymentTermTranslCreationDate | CREATION_DATE | — | — |
| 3 | LatePaymentTermTranslDescription | DESCRIPTION | — | — |
| 4 | LatePaymentTermTranslLanguage | LANGUAGE | — | — |
| 5 | LatePaymentTermTranslLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LatePaymentTermTranslLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LatePaymentTermTranslLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | LatePaymentTermTranslName | NAME | — | — |
| 9 | LatePaymentTermTranslObjVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | LatePaymentTermTranslSetId | SET_ID | — | — |
| 11 | LatePaymentTermTranslSourceLang | SOURCE_LANG | — | — |
| 12 | LatePaymentTermTranslTermId | TERM_ID | — | — |
| 13 | PayTermTransObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | PaymentTermTranslationCreatedBy | CREATED_BY | — | — |
| 15 | PaymentTermTranslationCreationDate | CREATION_DATE | — | — |
| 16 | PaymentTermTranslationDescription | DESCRIPTION | — | — |
| 17 | PaymentTermTranslationLanguage | LANGUAGE | — | — |
| 18 | PaymentTermTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | PaymentTermTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | PaymentTermTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 21 | PaymentTermTranslationName | NAME | — | — |
| 22 | PaymentTermTranslationSetId | SET_ID | — | — |
| 23 | PaymentTermTranslationSourceLang | SOURCE_LANG | — | — |
| 24 | PaymentTermTranslationTermId | TERM_ID | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
