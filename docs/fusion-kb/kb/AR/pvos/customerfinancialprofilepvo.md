---
id: DOC-AR-PVO-CustomerFinancialProfilePVO
doc_type: system-doc
title: "CustomerFinancialProfilePVO — PVO Accounts Receivable"
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
  - CustomerFinancialProfilePVO
  - customerfinancialprofilepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CustomerFinancialProfilePVO

## 📌 Visão Geral

Extrai o perfil financeiro completo dos clientes, incluindo limites de crédito, condições de pagamento, regras de cobrança automática, coletor responsável e ciclo de extratos. Central para gestão de risco de crédito, política de cobrança e classificação de clientes.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.CustomerFinancialProfilePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 494 | 15 | 3 | 18 | 4% |

---

## 🔗 Tabelas Relacionadas

- [[ar_app_exception_rules|AR_APP_EXCEPTION_RULES]] — 6 atributos
- [[ar_autocash_hierarchies|AR_AUTOCASH_HIERARCHIES]] — 18 atributos
- [[ar_automatch_rules|AR_AUTOMATCH_RULES]] — 19 atributos
- [[ar_charge_schedules|AR_CHARGE_SCHEDULES]] — 3 atributos
- [[ar_collectors|AR_COLLECTORS]] — 17 atributos (2 BICC)
- [[ar_standard_text_b|AR_STANDARD_TEXT_B]] — 7 atributos
- [[ar_statement_cycles|AR_STATEMENT_CYCLES]] — 6 atributos
- [[hz_customer_profiles_f|HZ_CUSTOMER_PROFILES_F]] — 86 atributos (4 BICC)
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 52 atributos
- [[hz_cust_profile_amts_f|HZ_CUST_PROFILE_AMTS_F]] — 60 atributos (3 PKs, 12 BICC)
- [[hz_cust_profile_classes|HZ_CUST_PROFILE_CLASSES]] — 70 atributos
- [[hz_cust_site_uses_all|HZ_CUST_SITE_USES_ALL]] — 54 atributos
- [[hz_parties|HZ_PARTIES]] — 75 atributos
- [[ra_grouping_rules|RA_GROUPING_RULES]] — 6 atributos
- [[ra_terms_vl|RA_TERMS_VL]] — 15 atributos

---

## ⚙️ Atributos

### [[ar_app_exception_rules|AR_APP_EXCEPTION_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExceptRuleActiveFlag | ACTIVE_FLAG | — | — |
| 2 | ExceptRuleDescription | DESCRIPTION | — | — |
| 3 | ExceptRuleEndDate | END_DATE | — | — |
| 4 | ExceptRuleExceptionRuleId | EXCEPTION_RULE_ID | — | — |
| 5 | ExceptRuleName | NAME | — | — |
| 6 | ExceptRuleStartDate | START_DATE | — | — |

### [[ar_autocash_hierarchies|AR_AUTOCASH_HIERARCHIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AutoCshHierarchyApplyPartialPayments | APPLY_PARTIAL_PAYMENTS | — | — |
| 2 | AutoCshHierarchyAutocashHierarchyId | AUTOCASH_HIERARCHY_ID | — | — |
| 3 | AutoCshHierarchyDescription | DESCRIPTION | — | — |
| 4 | AutoCshHierarchyForAdrApplyPartialPayments | APPLY_PARTIAL_PAYMENTS | — | — |
| 5 | AutoCshHierarchyForAdrAutocashHierarchyId | AUTOCASH_HIERARCHY_ID | — | — |
| 6 | AutoCshHierarchyForAdrDescription | DESCRIPTION | — | — |
| 7 | AutoCshHierarchyForAdrHierarchyName | HIERARCHY_NAME | — | — |
| 8 | AutoCshHierarchyForAdrIncludeDiscounts | INCLUDE_DISCOUNTS | — | — |
| 9 | AutoCshHierarchyForAdrIncludeDisputeItems | INCLUDE_DISPUTE_ITEMS | — | — |
| 10 | AutoCshHierarchyForAdrIncludeFinanceCharges | INCLUDE_FINANCE_CHARGES | — | — |
| 11 | AutoCshHierarchyForAdrRemainingAmount | REMAINING_AMOUNT | — | — |
| 12 | AutoCshHierarchyForAdrStatus | STATUS | — | — |
| 13 | AutoCshHierarchyHierarchyName | HIERARCHY_NAME | — | — |
| 14 | AutoCshHierarchyIncludeDiscounts | INCLUDE_DISCOUNTS | — | — |
| 15 | AutoCshHierarchyIncludeDisputeItems | INCLUDE_DISPUTE_ITEMS | — | — |
| 16 | AutoCshHierarchyIncludeFinanceCharges | INCLUDE_FINANCE_CHARGES | — | — |
| 17 | AutoCshHierarchyRemainingAmount | REMAINING_AMOUNT | — | — |
| 18 | AutoCshHierarchyStatus | STATUS | — | — |

### [[ar_automatch_rules|AR_AUTOMATCH_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AutoMatchRuleActiveFlag | ACTIVE_FLAG | — | — |
| 2 | AutoMatchRuleAmountWeight | AMOUNT_WEIGHT | — | — |
| 3 | AutoMatchRuleAutomatchRuleId | AUTOMATCH_RULE_ID | — | — |
| 4 | AutoMatchRuleCustomerThreshold | CUSTOMER_THRESHOLD | — | — |
| 5 | AutoMatchRuleCustomerWeight | CUSTOMER_WEIGHT | — | — |
| 6 | AutoMatchRuleDescription | DESCRIPTION | — | — |
| 7 | AutoMatchRuleEndDate | END_DATE | — | — |
| 8 | AutoMatchRuleMinMatchThreshold | MIN_MATCH_THRESHOLD | — | — |
| 9 | AutoMatchRuleName | NAME | — | — |
| 10 | AutoMatchRuleNetFreightWeight | NET_FREIGHT_WEIGHT | — | — |
| 11 | AutoMatchRuleNetTaxFreightWeight | NET_TAX_FREIGHT_WEIGHT | — | — |
| 12 | AutoMatchRuleNetTaxWeight | NET_TAX_WEIGHT | — | — |
| 13 | AutoMatchRuleNetUndiscWeight | NET_UNDISC_WEIGHT | — | — |
| 14 | AutoMatchRuleNumberOfDaysClosed | NUMBER_OF_DAYS_CLOSED | — | — |
| 15 | AutoMatchRuleRemittanceRegexp | REMITTANCE_REGEXP | — | — |
| 16 | AutoMatchRuleStartDate | START_DATE | — | — |
| 17 | AutoMatchRuleTransactionRegexp | TRANSACTION_REGEXP | — | — |
| 18 | AutoMatchRuleTransactionThreshold | TRANSACTION_THRESHOLD | — | — |
| 19 | AutoMatchRuleTransactionWeight | TRANSACTION_WEIGHT | — | — |

### [[ar_charge_schedules|AR_CHARGE_SCHEDULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChargeScheduleScheduleDescription | SCHEDULE_DESCRIPTION | — | — |
| 2 | ChargeScheduleScheduleId | SCHEDULE_ID | — | — |
| 3 | ChargeScheduleScheduleName | SCHEDULE_NAME | — | — |

### [[ar_collectors|AR_COLLECTORS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CollectorsAlias | ALIAS | — | — |
| 2 | CollectorsCollectorId | COLLECTOR_ID | — | — |
| 3 | CollectorsCreatedBy | CREATED_BY | — | — |
| 4 | CollectorsCreationDate | CREATION_DATE | — | — |
| 5 | CollectorsDescription | DESCRIPTION | — | — |
| 6 | CollectorsEmployeeId | EMPLOYEE_ID | — | — |
| 7 | CollectorsInactiveDate | INACTIVE_DATE | — | — |
| 8 | CollectorsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | CollectorsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | CollectorsLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | CollectorsName | NAME | — | ✅ |
| 12 | CollectorsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | CollectorsResourceId | RESOURCE_ID | — | — |
| 14 | CollectorsResourceType | RESOURCE_TYPE | — | — |
| 15 | CollectorsSetId | SET_ID | — | — |
| 16 | CollectorsStatus | STATUS | — | — |
| 17 | CollectorsTelephoneNumber | TELEPHONE_NUMBER | — | — |

### [[ar_standard_text_b|AR_STANDARD_TEXT_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StdTxtBaseEndDate | END_DATE | — | — |
| 2 | StdTxtBaseName | NAME | — | — |
| 3 | StdTxtBaseStandardTextId | STANDARD_TEXT_ID | — | — |
| 4 | StdTxtBaseStartDate | START_DATE | — | — |
| 5 | StdTxtBaseText | TEXT | — | — |
| 6 | StdTxtBaseTextType | TEXT_TYPE | — | — |
| 7 | StdTxtBaseTextUseType | TEXT_USE_TYPE | — | — |

### [[ar_statement_cycles|AR_STATEMENT_CYCLES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StmtCycleDay | DAY | — | — |
| 2 | StmtCycleDescription | DESCRIPTION | — | — |
| 3 | StmtCycleInterval | INTERVAL | — | — |
| 4 | StmtCycleName | NAME | — | — |
| 5 | StmtCycleStatementCycleId | STATEMENT_CYCLE_ID | — | — |
| 6 | StmtCycleStatus | STATUS | — | — |

### [[hz_customer_profiles_f|HZ_CUSTOMER_PROFILES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustProfileAccountStatus | ACCOUNT_STATUS | — | — |
| 2 | CustProfileApplicationId | APPLICATION_ID | — | — |
| 3 | CustProfileAutoRecInclDisputedFlag | AUTO_REC_INCL_DISPUTED_FLAG | — | — |
| 4 | CustProfileAutocashHierarchyId | AUTOCASH_HIERARCHY_ID | — | — |
| 5 | CustProfileAutocashHierarchyIdForAdr | AUTOCASH_HIERARCHY_ID_FOR_ADR | — | — |
| 6 | CustProfileAutomatchRuleId | AUTOMATCH_RULE_ID | — | — |
| 7 | CustProfileChargeBeginDate | CHARGE_BEGIN_DATE | — | — |
| 8 | CustProfileChargeOnFinanceChargeFlag | CHARGE_ON_FINANCE_CHARGE_FLAG | — | — |
| 9 | CustProfileClearingDays | CLEARING_DAYS | — | — |
| 10 | CustProfileCollectorId | COLLECTOR_ID | — | — |
| 11 | CustProfileConsBillLevel | CONS_BILL_LEVEL | — | — |
| 12 | CustProfileConsInvFlag | CONS_INV_FLAG | — | — |
| 13 | CustProfileConsInvType | CONS_INV_TYPE | — | — |
| 14 | CustProfileCreatedBy | CREATED_BY | — | — |
| 15 | CustProfileCreatedByModule | CREATED_BY_MODULE | — | — |
| 16 | CustProfileCreationDate | CREATION_DATE | — | — |
| 17 | CustProfileCreditAnalystId | CREDIT_ANALYST_ID | — | — |
| 18 | CustProfileCreditBalanceStatements | CREDIT_BALANCE_STATEMENTS | — | — |
| 19 | CustProfileCreditChecking | CREDIT_CHECKING | — | — |
| 20 | CustProfileCreditClassification | CREDIT_CLASSIFICATION | — | — |
| 21 | CustProfileCreditHold | CREDIT_HOLD | — | — |
| 22 | CustProfileCreditItemsFlag | CREDIT_ITEMS_FLAG | — | — |
| 23 | CustProfileCreditRating | CREDIT_RATING | — | ✅ |
| 24 | CustProfileCustAccountId | CUST_ACCOUNT_ID | — | — |
| 25 | CustProfileCustAccountProfileId | CUST_ACCOUNT_PROFILE_ID | — | — |
| 26 | CustProfileDiscountGraceDays | DISCOUNT_GRACE_DAYS | — | — |
| 27 | CustProfileDiscountTerms | DISCOUNT_TERMS | — | — |
| 28 | CustProfileDisputedTransactionsFlag | DISPUTED_TRANSACTIONS_FLAG | — | — |
| 29 | CustProfileDunningLetters | DUNNING_LETTERS | — | — |
| 30 | CustProfileEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 31 | CustProfileEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 32 | CustProfileExceptionRuleId | EXCEPTION_RULE_ID | — | — |
| 33 | CustProfileGroupingRuleId | GROUPING_RULE_ID | — | — |
| 34 | CustProfileHoldChargedInvoicesFlag | HOLD_CHARGED_INVOICES_FLAG | — | — |
| 35 | CustProfileInterestCalculationPeriod | INTEREST_CALCULATION_PERIOD | — | — |
| 36 | CustProfileInterestCharges | INTEREST_CHARGES | — | — |
| 37 | CustProfileInterestPeriodDays | INTEREST_PERIOD_DAYS | — | — |
| 38 | CustProfileJgzzAttribute1 | JGZZ_ATTRIBUTE1 | — | — |
| 39 | CustProfileJgzzAttribute10 | JGZZ_ATTRIBUTE10 | — | — |
| 40 | CustProfileJgzzAttribute11 | JGZZ_ATTRIBUTE11 | — | — |
| 41 | CustProfileJgzzAttribute12 | JGZZ_ATTRIBUTE12 | — | — |
| 42 | CustProfileJgzzAttribute13 | JGZZ_ATTRIBUTE13 | — | — |
| 43 | CustProfileJgzzAttribute14 | JGZZ_ATTRIBUTE14 | — | — |
| 44 | CustProfileJgzzAttribute15 | JGZZ_ATTRIBUTE15 | — | — |
| 45 | CustProfileJgzzAttribute2 | JGZZ_ATTRIBUTE2 | — | — |
| 46 | CustProfileJgzzAttribute3 | JGZZ_ATTRIBUTE3 | — | — |
| 47 | CustProfileJgzzAttribute4 | JGZZ_ATTRIBUTE4 | — | — |
| 48 | CustProfileJgzzAttribute5 | JGZZ_ATTRIBUTE5 | — | — |
| 49 | CustProfileJgzzAttribute6 | JGZZ_ATTRIBUTE6 | — | — |
| 50 | CustProfileJgzzAttribute7 | JGZZ_ATTRIBUTE7 | — | — |
| 51 | CustProfileJgzzAttribute8 | JGZZ_ATTRIBUTE8 | — | — |
| 52 | CustProfileJgzzAttribute9 | JGZZ_ATTRIBUTE9 | — | — |
| 53 | CustProfileJgzzAttributeCategory | JGZZ_ATTRIBUTE_CATEGORY | — | — |
| 54 | CustProfileLastCreditReviewDate | LAST_CREDIT_REVIEW_DATE | — | — |
| 55 | CustProfileLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 56 | CustProfileLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 57 | CustProfileLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 58 | CustProfileLateChargeCalculationTrx | LATE_CHARGE_CALCULATION_TRX | — | — |
| 59 | CustProfileLateChargeTermId | LATE_CHARGE_TERM_ID | — | — |
| 60 | CustProfileLateChargeType | LATE_CHARGE_TYPE | — | — |
| 61 | CustProfileLockboxMatchingOption | LOCKBOX_MATCHING_OPTION | — | — |
| 62 | CustProfileMatchByAutoupdateFlag | MATCH_BY_AUTOUPDATE_FLAG | — | — |
| 63 | CustProfileMessageTextId | MESSAGE_TEXT_ID | — | — |
| 64 | CustProfileMultipleInterestRatesFlag | MULTIPLE_INTEREST_RATES_FLAG | — | — |
| 65 | CustProfileNextCreditReviewDate | NEXT_CREDIT_REVIEW_DATE | — | — |
| 66 | CustProfileObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 67 | CustProfileOverrideTerms | OVERRIDE_TERMS | — | — |
| 68 | CustProfilePartyId | PARTY_ID | — | ✅ |
| 69 | CustProfilePaymentGraceDays | PAYMENT_GRACE_DAYS | — | — |
| 70 | CustProfilePercentCollectable | PERCENT_COLLECTABLE | — | — |
| 71 | CustProfilePrefContactMethod | PREF_CONTACT_METHOD | — | — |
| 72 | CustProfileProfileClassId | PROFILE_CLASS_ID | — | — |
| 73 | CustProfileProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 74 | CustProfileProgramId | PROGRAM_ID | — | — |
| 75 | CustProfileProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 76 | CustProfileRequestId | REQUEST_ID | — | — |
| 77 | CustProfileReviewCycle | REVIEW_CYCLE | — | — |
| 78 | CustProfileRiskCode | RISK_CODE | — | — |
| 79 | CustProfileSendStatements | SEND_STATEMENTS | — | — |
| 80 | CustProfileSiteUseId | SITE_USE_ID | — | ✅ |
| 81 | CustProfileStandardTerms | STANDARD_TERMS | — | — |
| 82 | CustProfileStatementCycleId | STATEMENT_CYCLE_ID | — | — |
| 83 | CustProfileStatus | STATUS | — | — |
| 84 | CustProfileTaxPrintingOption | TAX_PRINTING_OPTION | — | — |
| 85 | CustProfileTolerance | TOLERANCE | — | — |
| 86 | CustProfileWhUpdateDate | WH_UPDATE_DATE | — | — |

### [[hz_cust_accounts|HZ_CUST_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustAcctFinProfileAccountEstablishedDate | ACCOUNT_ESTABLISHED_DATE | — | — |
| 2 | CustAcctFinProfileAccountName | ACCOUNT_NAME | — | — |
| 3 | CustAcctFinProfileAccountNumber | ACCOUNT_NUMBER | — | — |
| 4 | CustAcctFinProfileArrivalsetsIncludeLinesFlag | ARRIVALSETS_INCLUDE_LINES_FLAG | — | — |
| 5 | CustAcctFinProfileAutopayFlag | AUTOPAY_FLAG | — | — |
| 6 | CustAcctFinProfileComments | COMMENTS | — | — |
| 7 | CustAcctFinProfileCoterminateDayMonth | COTERMINATE_DAY_MONTH | — | — |
| 8 | CustAcctFinProfileCreatedByModule | CREATED_BY_MODULE | — | — |
| 9 | CustAcctFinProfileCustAccountId | CUST_ACCOUNT_ID | — | — |
| 10 | CustAcctFinProfileCustomerClassCode | CUSTOMER_CLASS_CODE | — | — |
| 11 | CustAcctFinProfileCustomerType | CUSTOMER_TYPE | — | — |
| 12 | CustAcctFinProfileDateTypePreference | DATE_TYPE_PREFERENCE | — | — |
| 13 | CustAcctFinProfileDepositRefundMethod | DEPOSIT_REFUND_METHOD | — | — |
| 14 | CustAcctFinProfileHeldBillExpirationDate | HELD_BILL_EXPIRATION_DATE | — | — |
| 15 | CustAcctFinProfileHoldBillFlag | HOLD_BILL_FLAG | — | — |
| 16 | CustAcctFinProfileLastBatchId | LAST_BATCH_ID | — | — |
| 17 | CustAcctFinProfileNpaNumber | NPA_NUMBER | — | — |
| 18 | CustAcctFinProfileOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 19 | CustAcctFinProfilePartyId | PARTY_ID | — | — |
| 20 | CustAcctFinProfileSellingPartyId | SELLING_PARTY_ID | — | — |
| 21 | CustAcctFinProfileSourceCode | SOURCE_CODE | — | — |
| 22 | CustAcctFinProfileStatus | STATUS | — | — |
| 23 | CustAcctFinProfileStatusUpdateDate | STATUS_UPDATE_DATE | — | — |
| 24 | CustAcctFinProfileTaxCode | TAX_CODE | — | — |
| 25 | CustAcctFinProfileTaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | — |
| 26 | CustAcctFinProfileTaxRoundingRule | TAX_ROUNDING_RULE | — | — |
| 27 | CustAcctProfileAccountEstablishedDate | ACCOUNT_ESTABLISHED_DATE | — | — |
| 28 | CustAcctProfileAccountName | ACCOUNT_NAME | — | — |
| 29 | CustAcctProfileAccountNumber | ACCOUNT_NUMBER | — | — |
| 30 | CustAcctProfileArrivalsetsIncludeLinesFlag | ARRIVALSETS_INCLUDE_LINES_FLAG | — | — |
| 31 | CustAcctProfileAutopayFlag | AUTOPAY_FLAG | — | — |
| 32 | CustAcctProfileComments | COMMENTS | — | — |
| 33 | CustAcctProfileCoterminateDayMonth | COTERMINATE_DAY_MONTH | — | — |
| 34 | CustAcctProfileCreatedByModule | CREATED_BY_MODULE | — | — |
| 35 | CustAcctProfileCustAccountId | CUST_ACCOUNT_ID | — | — |
| 36 | CustAcctProfileCustomerClassCode | CUSTOMER_CLASS_CODE | — | — |
| 37 | CustAcctProfileCustomerType | CUSTOMER_TYPE | — | — |
| 38 | CustAcctProfileDateTypePreference | DATE_TYPE_PREFERENCE | — | — |
| 39 | CustAcctProfileDepositRefundMethod | DEPOSIT_REFUND_METHOD | — | — |
| 40 | CustAcctProfileHeldBillExpirationDate | HELD_BILL_EXPIRATION_DATE | — | — |
| 41 | CustAcctProfileHoldBillFlag | HOLD_BILL_FLAG | — | — |
| 42 | CustAcctProfileLastBatchId | LAST_BATCH_ID | — | — |
| 43 | CustAcctProfileNpaNumber | NPA_NUMBER | — | — |
| 44 | CustAcctProfileOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 45 | CustAcctProfilePartyId | PARTY_ID | — | — |
| 46 | CustAcctProfileSellingPartyId | SELLING_PARTY_ID | — | — |
| 47 | CustAcctProfileSourceCode | SOURCE_CODE | — | — |
| 48 | CustAcctProfileStatus | STATUS | — | — |
| 49 | CustAcctProfileStatusUpdateDate | STATUS_UPDATE_DATE | — | — |
| 50 | CustAcctProfileTaxCode | TAX_CODE | — | — |
| 51 | CustAcctProfileTaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | — |
| 52 | CustAcctProfileTaxRoundingRule | TAX_ROUNDING_RULE | — | — |

### [[hz_cust_profile_amts_f|HZ_CUST_PROFILE_AMTS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustAcctProfileAmtId | CUST_ACCT_PROFILE_AMT_ID | 🔑 | ✅ |
| 2 | CustFinProfileApplicationId | APPLICATION_ID | — | — |
| 3 | CustFinProfileAutoRecMinReceiptAmount | AUTO_REC_MIN_RECEIPT_AMOUNT | — | — |
| 4 | CustFinProfileCreatedBy | CREATED_BY | — | ✅ |
| 5 | CustFinProfileCreatedByModule | CREATED_BY_MODULE | — | — |
| 6 | CustFinProfileCreationDate | CREATION_DATE | — | ✅ |
| 7 | CustFinProfileCurrencyCode | CURRENCY_CODE | — | ✅ |
| 8 | CustFinProfileCustAccountId | CUST_ACCOUNT_ID | — | ✅ |
| 9 | CustFinProfileCustAccountProfileId | CUST_ACCOUNT_PROFILE_ID | — | — |
| 10 | CustFinProfileExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 11 | CustFinProfileExpirationDate | EXPIRATION_DATE | — | ✅ |
| 12 | CustFinProfileInterestFixedAmount | INTEREST_FIXED_AMOUNT | — | — |
| 13 | CustFinProfileInterestRate | INTEREST_RATE | — | — |
| 14 | CustFinProfileInterestScheduleId | INTEREST_SCHEDULE_ID | — | — |
| 15 | CustFinProfileInterestType | INTEREST_TYPE | — | — |
| 16 | CustFinProfileJgzzAttribute1 | JGZZ_ATTRIBUTE1 | — | — |
| 17 | CustFinProfileJgzzAttribute10 | JGZZ_ATTRIBUTE10 | — | — |
| 18 | CustFinProfileJgzzAttribute11 | JGZZ_ATTRIBUTE11 | — | — |
| 19 | CustFinProfileJgzzAttribute12 | JGZZ_ATTRIBUTE12 | — | — |
| 20 | CustFinProfileJgzzAttribute13 | JGZZ_ATTRIBUTE13 | — | — |
| 21 | CustFinProfileJgzzAttribute14 | JGZZ_ATTRIBUTE14 | — | — |
| 22 | CustFinProfileJgzzAttribute15 | JGZZ_ATTRIBUTE15 | — | — |
| 23 | CustFinProfileJgzzAttribute2 | JGZZ_ATTRIBUTE2 | — | — |
| 24 | CustFinProfileJgzzAttribute3 | JGZZ_ATTRIBUTE3 | — | — |
| 25 | CustFinProfileJgzzAttribute4 | JGZZ_ATTRIBUTE4 | — | — |
| 26 | CustFinProfileJgzzAttribute5 | JGZZ_ATTRIBUTE5 | — | — |
| 27 | CustFinProfileJgzzAttribute6 | JGZZ_ATTRIBUTE6 | — | — |
| 28 | CustFinProfileJgzzAttribute7 | JGZZ_ATTRIBUTE7 | — | — |
| 29 | CustFinProfileJgzzAttribute8 | JGZZ_ATTRIBUTE8 | — | — |
| 30 | CustFinProfileJgzzAttribute9 | JGZZ_ATTRIBUTE9 | — | — |
| 31 | CustFinProfileJgzzAttributeCategory | JGZZ_ATTRIBUTE_CATEGORY | — | — |
| 32 | CustFinProfileLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 33 | CustFinProfileLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 34 | CustFinProfileLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 35 | CustFinProfileMaxInterestCharge | MAX_INTEREST_CHARGE | — | — |
| 36 | CustFinProfileMinDunningAmount | MIN_DUNNING_AMOUNT | — | — |
| 37 | CustFinProfileMinDunningInvoiceAmount | MIN_DUNNING_INVOICE_AMOUNT | — | — |
| 38 | CustFinProfileMinFcBalanceAmount | MIN_FC_BALANCE_AMOUNT | — | — |
| 39 | CustFinProfileMinFcBalanceOverdueType | MIN_FC_BALANCE_OVERDUE_TYPE | — | — |
| 40 | CustFinProfileMinFcBalancePercent | MIN_FC_BALANCE_PERCENT | — | — |
| 41 | CustFinProfileMinFcInvoiceAmount | MIN_FC_INVOICE_AMOUNT | — | — |
| 42 | CustFinProfileMinFcInvoiceOverdueType | MIN_FC_INVOICE_OVERDUE_TYPE | — | — |
| 43 | CustFinProfileMinFcInvoicePercent | MIN_FC_INVOICE_PERCENT | — | — |
| 44 | CustFinProfileMinInterestCharge | MIN_INTEREST_CHARGE | — | — |
| 45 | CustFinProfileMinStatementAmount | MIN_STATEMENT_AMOUNT | — | — |
| 46 | CustFinProfileObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 47 | CustFinProfileOverallCreditLimit | OVERALL_CREDIT_LIMIT | — | ✅ |
| 48 | CustFinProfilePenaltyFixedAmount | PENALTY_FIXED_AMOUNT | — | — |
| 49 | CustFinProfilePenaltyRate | PENALTY_RATE | — | — |
| 50 | CustFinProfilePenaltyScheduleId | PENALTY_SCHEDULE_ID | — | — |
| 51 | CustFinProfilePenaltyType | PENALTY_TYPE | — | — |
| 52 | CustFinProfileProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 53 | CustFinProfileProgramId | PROGRAM_ID | — | — |
| 54 | CustFinProfileProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 55 | CustFinProfileRequestId | REQUEST_ID | — | — |
| 56 | CustFinProfileSiteUseId | SITE_USE_ID | — | — |
| 57 | CustFinProfileTrxCreditLimit | TRX_CREDIT_LIMIT | — | ✅ |
| 58 | CustFinProfileWhUpdateDate | WH_UPDATE_DATE | — | — |
| 59 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 60 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |

### [[hz_cust_profile_classes|HZ_CUST_PROFILE_CLASSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustProfileClsAutoRecInclDisputedFlag | AUTO_REC_INCL_DISPUTED_FLAG | — | — |
| 2 | CustProfileClsAutocashHierarchyId | AUTOCASH_HIERARCHY_ID | — | — |
| 3 | CustProfileClsAutocashHierarchyIdForAdr | AUTOCASH_HIERARCHY_ID_FOR_ADR | — | — |
| 4 | CustProfileClsAutomatchRuleId | AUTOMATCH_RULE_ID | — | — |
| 5 | CustProfileClsChargeBeginDate | CHARGE_BEGIN_DATE | — | — |
| 6 | CustProfileClsChargeOnFinanceChargeFlag | CHARGE_ON_FINANCE_CHARGE_FLAG | — | — |
| 7 | CustProfileClsCollectorId | COLLECTOR_ID | — | — |
| 8 | CustProfileClsCombineDunningLetters | COMBINE_DUNNING_LETTERS | — | — |
| 9 | CustProfileClsConsBillLevel | CONS_BILL_LEVEL | — | — |
| 10 | CustProfileClsConsInvFlag | CONS_INV_FLAG | — | — |
| 11 | CustProfileClsConsInvType | CONS_INV_TYPE | — | — |
| 12 | CustProfileClsCopyMethod | COPY_METHOD | — | — |
| 13 | CustProfileClsCreditAnalystId | CREDIT_ANALYST_ID | — | — |
| 14 | CustProfileClsCreditBalanceStatements | CREDIT_BALANCE_STATEMENTS | — | — |
| 15 | CustProfileClsCreditChecking | CREDIT_CHECKING | — | — |
| 16 | CustProfileClsCreditClassification | CREDIT_CLASSIFICATION | — | — |
| 17 | CustProfileClsCreditItemsFlag | CREDIT_ITEMS_FLAG | — | — |
| 18 | CustProfileClsDescription | DESCRIPTION | — | — |
| 19 | CustProfileClsDiscountGraceDays | DISCOUNT_GRACE_DAYS | — | — |
| 20 | CustProfileClsDiscountTerms | DISCOUNT_TERMS | — | — |
| 21 | CustProfileClsDisputedTransactionsFlag | DISPUTED_TRANSACTIONS_FLAG | — | — |
| 22 | CustProfileClsDunningLetters | DUNNING_LETTERS | — | — |
| 23 | CustProfileClsExceptionRuleId | EXCEPTION_RULE_ID | — | — |
| 24 | CustProfileClsGroupingRuleId | GROUPING_RULE_ID | — | — |
| 25 | CustProfileClsHoldChargedInvoicesFlag | HOLD_CHARGED_INVOICES_FLAG | — | — |
| 26 | CustProfileClsInterestCalculationPeriod | INTEREST_CALCULATION_PERIOD | — | — |
| 27 | CustProfileClsInterestCharges | INTEREST_CHARGES | — | — |
| 28 | CustProfileClsInterestPeriodDays | INTEREST_PERIOD_DAYS | — | — |
| 29 | CustProfileClsJgzzAttribute1 | JGZZ_ATTRIBUTE1 | — | — |
| 30 | CustProfileClsJgzzAttribute10 | JGZZ_ATTRIBUTE10 | — | — |
| 31 | CustProfileClsJgzzAttribute11 | JGZZ_ATTRIBUTE11 | — | — |
| 32 | CustProfileClsJgzzAttribute12 | JGZZ_ATTRIBUTE12 | — | — |
| 33 | CustProfileClsJgzzAttribute13 | JGZZ_ATTRIBUTE13 | — | — |
| 34 | CustProfileClsJgzzAttribute14 | JGZZ_ATTRIBUTE14 | — | — |
| 35 | CustProfileClsJgzzAttribute15 | JGZZ_ATTRIBUTE15 | — | — |
| 36 | CustProfileClsJgzzAttribute2 | JGZZ_ATTRIBUTE2 | — | — |
| 37 | CustProfileClsJgzzAttribute3 | JGZZ_ATTRIBUTE3 | — | — |
| 38 | CustProfileClsJgzzAttribute4 | JGZZ_ATTRIBUTE4 | — | — |
| 39 | CustProfileClsJgzzAttribute5 | JGZZ_ATTRIBUTE5 | — | — |
| 40 | CustProfileClsJgzzAttribute6 | JGZZ_ATTRIBUTE6 | — | — |
| 41 | CustProfileClsJgzzAttribute7 | JGZZ_ATTRIBUTE7 | — | — |
| 42 | CustProfileClsJgzzAttribute8 | JGZZ_ATTRIBUTE8 | — | — |
| 43 | CustProfileClsJgzzAttribute9 | JGZZ_ATTRIBUTE9 | — | — |
| 44 | CustProfileClsJgzzAttributeCategory | JGZZ_ATTRIBUTE_CATEGORY | — | — |
| 45 | CustProfileClsLateChargeCalculationTrx | LATE_CHARGE_CALCULATION_TRX | — | — |
| 46 | CustProfileClsLateChargeTermId | LATE_CHARGE_TERM_ID | — | — |
| 47 | CustProfileClsLateChargeType | LATE_CHARGE_TYPE | — | — |
| 48 | CustProfileClsLockboxMatchingOption | LOCKBOX_MATCHING_OPTION | — | — |
| 49 | CustProfileClsMatchByAutoupdateFlag | MATCH_BY_AUTOUPDATE_FLAG | — | — |
| 50 | CustProfileClsMessageTextId | MESSAGE_TEXT_ID | — | — |
| 51 | CustProfileClsMultipleInterestRatesFlag | MULTIPLE_INTEREST_RATES_FLAG | — | — |
| 52 | CustProfileClsName | NAME | — | — |
| 53 | CustProfileClsOutsideReporting | OUTSIDE_REPORTING | — | — |
| 54 | CustProfileClsOverrideTerms | OVERRIDE_TERMS | — | — |
| 55 | CustProfileClsPaymentGraceDays | PAYMENT_GRACE_DAYS | — | — |
| 56 | CustProfileClsPrefContactMethod | PREF_CONTACT_METHOD | — | — |
| 57 | CustProfileClsProfileClassId | PROFILE_CLASS_ID | — | — |
| 58 | CustProfileClsProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 59 | CustProfileClsProgramId | PROGRAM_ID | — | — |
| 60 | CustProfileClsProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 61 | CustProfileClsRequestId | REQUEST_ID | — | — |
| 62 | CustProfileClsReviewCycle | REVIEW_CYCLE | — | — |
| 63 | CustProfileClsReviewCycleDays | REVIEW_CYCLE_DAYS | — | — |
| 64 | CustProfileClsStandardTerms | STANDARD_TERMS | — | — |
| 65 | CustProfileClsStatementCycleId | STATEMENT_CYCLE_ID | — | — |
| 66 | CustProfileClsStatements | STATEMENTS | — | — |
| 67 | CustProfileClsStatus | STATUS | — | — |
| 68 | CustProfileClsTaxPrintingOption | TAX_PRINTING_OPTION | — | — |
| 69 | CustProfileClsTolerance | TOLERANCE | — | — |
| 70 | CustProfileClsWhUpdateDate | WH_UPDATE_DATE | — | — |

### [[hz_cust_site_uses_all|HZ_CUST_SITE_USES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustAcctSiteUseFinProfileBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 2 | CustAcctSiteUseFinProfileCreatedByModule | CREATED_BY_MODULE | — | — |
| 3 | CustAcctSiteUseFinProfileCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 4 | CustAcctSiteUseFinProfileEndDate | END_DATE | — | — |
| 5 | CustAcctSiteUseFinProfileFinchrgReceivablesTrxId | FINCHRG_RECEIVABLES_TRX_ID | — | — |
| 6 | CustAcctSiteUseFinProfileGsaIndicator | GSA_INDICATOR | — | — |
| 7 | CustAcctSiteUseFinProfileLastAccrueChargeDate | LAST_ACCRUE_CHARGE_DATE | — | — |
| 8 | CustAcctSiteUseFinProfileLastUnaccrueChargeDate | LAST_UNACCRUE_CHARGE_DATE | — | — |
| 9 | CustAcctSiteUseFinProfileLocation | LOCATION | — | — |
| 10 | CustAcctSiteUseFinProfileOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 11 | CustAcctSiteUseFinProfilePaymentTermId | PAYMENT_TERM_ID | — | — |
| 12 | CustAcctSiteUseFinProfilePrimaryFlag | PRIMARY_FLAG | — | — |
| 13 | CustAcctSiteUseFinProfileSecondLastAccrueChargeDate | SECOND_LAST_ACCRUE_CHARGE_DATE | — | — |
| 14 | CustAcctSiteUseFinProfileSecondLastUnaccrueChrgDate | SECOND_LAST_UNACCRUE_CHRG_DATE | — | — |
| 15 | CustAcctSiteUseFinProfileSetId | SET_ID | — | — |
| 16 | CustAcctSiteUseFinProfileSicCode | SIC_CODE | — | — |
| 17 | CustAcctSiteUseFinProfileSiteUseCode | SITE_USE_CODE | — | — |
| 18 | CustAcctSiteUseFinProfileSiteUseId | SITE_USE_ID | — | — |
| 19 | CustAcctSiteUseFinProfileSortPriority | SORT_PRIORITY | — | — |
| 20 | CustAcctSiteUseFinProfileStartDate | START_DATE | — | — |
| 21 | CustAcctSiteUseFinProfileStatus | STATUS | — | — |
| 22 | CustAcctSiteUseFinProfileTaxClassification | TAX_CLASSIFICATION | — | — |
| 23 | CustAcctSiteUseFinProfileTaxCode | TAX_CODE | — | — |
| 24 | CustAcctSiteUseFinProfileTaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | — |
| 25 | CustAcctSiteUseFinProfileTaxReference | TAX_REFERENCE | — | — |
| 26 | CustAcctSiteUseFinProfileTaxRoundingRule | TAX_ROUNDING_RULE | — | — |
| 27 | CustAcctSiteUseFinProfileTerritoryId | TERRITORY_ID | — | — |
| 28 | CustAcctSiteUseProfileBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 29 | CustAcctSiteUseProfileCreatedByModule | CREATED_BY_MODULE | — | — |
| 30 | CustAcctSiteUseProfileCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 31 | CustAcctSiteUseProfileEndDate | END_DATE | — | — |
| 32 | CustAcctSiteUseProfileFinchrgReceivablesTrxId | FINCHRG_RECEIVABLES_TRX_ID | — | — |
| 33 | CustAcctSiteUseProfileGsaIndicator | GSA_INDICATOR | — | — |
| 34 | CustAcctSiteUseProfileLastAccrueChargeDate | LAST_ACCRUE_CHARGE_DATE | — | — |
| 35 | CustAcctSiteUseProfileLastUnaccrueChargeDate | LAST_UNACCRUE_CHARGE_DATE | — | — |
| 36 | CustAcctSiteUseProfileLocation | LOCATION | — | — |
| 37 | CustAcctSiteUseProfileOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 38 | CustAcctSiteUseProfilePaymentTermId | PAYMENT_TERM_ID | — | — |
| 39 | CustAcctSiteUseProfilePrimaryFlag | PRIMARY_FLAG | — | — |
| 40 | CustAcctSiteUseProfileSecondLastAccrueChargeDate | SECOND_LAST_ACCRUE_CHARGE_DATE | — | — |
| 41 | CustAcctSiteUseProfileSecondLastUnaccrueChrgDate | SECOND_LAST_UNACCRUE_CHRG_DATE | — | — |
| 42 | CustAcctSiteUseProfileSetId | SET_ID | — | — |
| 43 | CustAcctSiteUseProfileSicCode | SIC_CODE | — | — |
| 44 | CustAcctSiteUseProfileSiteUseCode | SITE_USE_CODE | — | — |
| 45 | CustAcctSiteUseProfileSiteUseId | SITE_USE_ID | — | — |
| 46 | CustAcctSiteUseProfileSortPriority | SORT_PRIORITY | — | — |
| 47 | CustAcctSiteUseProfileStartDate | START_DATE | — | — |
| 48 | CustAcctSiteUseProfileStatus | STATUS | — | — |
| 49 | CustAcctSiteUseProfileTaxClassification | TAX_CLASSIFICATION | — | — |
| 50 | CustAcctSiteUseProfileTaxCode | TAX_CODE | — | — |
| 51 | CustAcctSiteUseProfileTaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | — |
| 52 | CustAcctSiteUseProfileTaxReference | TAX_REFERENCE | — | — |
| 53 | CustAcctSiteUseProfileTaxRoundingRule | TAX_ROUNDING_RULE | — | — |
| 54 | CustAcctSiteUseProfileTerritoryId | TERRITORY_ID | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyProfileAddress1 | ADDRESS1 | — | — |
| 2 | PartyProfileAddress2 | ADDRESS2 | — | — |
| 3 | PartyProfileAddress3 | ADDRESS3 | — | — |
| 4 | PartyProfileAddress4 | ADDRESS4 | — | — |
| 5 | PartyProfileAnalysisFy | ANALYSIS_FY | — | — |
| 6 | PartyProfileCategoryCode | CATEGORY_CODE | — | — |
| 7 | PartyProfileCeoName | CEO_NAME | — | — |
| 8 | PartyProfileCertReasonCode | CERT_REASON_CODE | — | — |
| 9 | PartyProfileCertificationLevel | CERTIFICATION_LEVEL | — | — |
| 10 | PartyProfileCity | CITY | — | — |
| 11 | PartyProfileComments | COMMENTS | — | — |
| 12 | PartyProfileCountry | COUNTRY | — | — |
| 13 | PartyProfileCounty | COUNTY | — | — |
| 14 | PartyProfileCreatedByModule | CREATED_BY_MODULE | — | — |
| 15 | PartyProfileCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 16 | PartyProfileDateOfBirth | DATE_OF_BIRTH | — | — |
| 17 | PartyProfileDunsNumberC | DUNS_NUMBER_C | — | — |
| 18 | PartyProfileEmailAddress | EMAIL_ADDRESS | — | — |
| 19 | PartyProfileEmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 20 | PartyProfileFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 21 | PartyProfileGender | GENDER | — | — |
| 22 | PartyProfileGroupType | GROUP_TYPE | — | — |
| 23 | PartyProfileGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | — |
| 24 | PartyProfileHomeCountry | HOME_COUNTRY | — | — |
| 25 | PartyProfileHqBranchInd | HQ_BRANCH_IND | — | — |
| 26 | PartyProfileIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 27 | PartyProfileIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | — |
| 28 | PartyProfileInternalFlag | INTERNAL_FLAG | — | — |
| 29 | PartyProfileJgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 30 | PartyProfileLanguageName | LANGUAGE_NAME | — | — |
| 31 | PartyProfileMaritalStatus | MARITAL_STATUS | — | — |
| 32 | PartyProfileMissionStatement | MISSION_STATEMENT | — | — |
| 33 | PartyProfileNextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 34 | PartyProfileOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 35 | PartyProfilePartyId | PARTY_ID | — | — |
| 36 | PartyProfilePartyName | PARTY_NAME | — | — |
| 37 | PartyProfilePartyNumber | PARTY_NUMBER | — | — |
| 38 | PartyProfilePartyType | PARTY_TYPE | — | — |
| 39 | PartyProfilePersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 40 | PartyProfilePersonFirstName | PERSON_FIRST_NAME | — | — |
| 41 | PartyProfilePersonLastName | PERSON_LAST_NAME | — | — |
| 42 | PartyProfilePersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 43 | PartyProfilePersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 44 | PartyProfilePersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 45 | PartyProfilePersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 46 | PartyProfilePersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 47 | PartyProfilePersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 48 | PartyProfilePersonTitle | PERSON_TITLE | — | — |
| 49 | PartyProfilePostalCode | POSTAL_CODE | — | — |
| 50 | PartyProfilePrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 51 | PartyProfilePreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 52 | PartyProfilePreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 53 | PartyProfilePreferredName | PREFERRED_NAME | — | — |
| 54 | PartyProfilePreferredNameId | PREFERRED_NAME_ID | — | — |
| 55 | PartyProfilePrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | — |
| 56 | PartyProfilePrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 57 | PartyProfilePrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 58 | PartyProfilePrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 59 | PartyProfilePrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 60 | PartyProfilePrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 61 | PartyProfilePrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | — |
| 62 | PartyProfilePrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 63 | PartyProfilePrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 64 | PartyProfileProvince | PROVINCE | — | — |
| 65 | PartyProfileSalutation | SALUTATION | — | — |
| 66 | PartyProfileSicCode | SIC_CODE | — | — |
| 67 | PartyProfileSicCodeType | SIC_CODE_TYPE | — | — |
| 68 | PartyProfileState | STATE | — | — |
| 69 | PartyProfileStatus | STATUS | — | — |
| 70 | PartyProfileThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 71 | PartyProfileTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 72 | PartyProfileUrl | URL | — | — |
| 73 | PartyProfileUserGuid | USER_GUID | — | — |
| 74 | PartyProfileValidatedFlag | VALIDATED_FLAG | — | — |
| 75 | PartyProfileYearEstablished | YEAR_ESTABLISHED | — | — |

### [[ra_grouping_rules|RA_GROUPING_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrxReqGroupingRuleDescription | DESCRIPTION | — | — |
| 2 | TrxReqGroupingRuleEndDate | END_DATE | — | — |
| 3 | TrxReqGroupingRuleGroupingRuleId | GROUPING_RULE_ID | — | — |
| 4 | TrxReqGroupingRuleName | NAME | — | — |
| 5 | TrxReqGroupingRuleOrderingRuleId | ORDERING_RULE_ID | — | — |
| 6 | TrxReqGroupingRuleStartDate | START_DATE | — | — |

### [[ra_terms_vl|RA_TERMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PmtTermProfileBaseAmount | BASE_AMOUNT | — | — |
| 2 | PmtTermProfileBillingCycleId | BILLING_CYCLE_ID | — | — |
| 3 | PmtTermProfileCalcDiscountOnLinesFlag | CALC_DISCOUNT_ON_LINES_FLAG | — | — |
| 4 | PmtTermProfileCreditCheckFlag | CREDIT_CHECK_FLAG | — | — |
| 5 | PmtTermProfileDescription | DESCRIPTION | — | — |
| 6 | PmtTermProfileDueCutoffDay | DUE_CUTOFF_DAY | — | — |
| 7 | PmtTermProfileEndDateActive | END_DATE_ACTIVE | — | — |
| 8 | PmtTermProfileFirstInstallmentCode | FIRST_INSTALLMENT_CODE | — | — |
| 9 | PmtTermProfileInUse | IN_USE | — | — |
| 10 | PmtTermProfileName | NAME | — | — |
| 11 | PmtTermProfilePartialDiscountFlag | PARTIAL_DISCOUNT_FLAG | — | — |
| 12 | PmtTermProfilePrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 13 | PmtTermProfilePrintingLeadDays | PRINTING_LEAD_DAYS | — | — |
| 14 | PmtTermProfileStartDateActive | START_DATE_ACTIVE | — | — |
| 15 | PmtTermProfileTermId | TERM_ID | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
