---
id: DOC-GL-PVO-LedgerPVO
doc_type: system-doc
title: "LedgerPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - LedgerPVO
  - ledgerpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LedgerPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Ledger. Acessa as tabelas: FND_CURRENCIES_VL, FND_KF_STR_INSTANCES_VL, GL_AUTOREV_CRITERIA_SETS (+8).

**Caminho:** `FscmTopModelAM.FinGlLedgerDefnAM.LedgerPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 178 | 11 | 1 | 29 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_currencies_vl|FND_CURRENCIES_VL]] — 17 atributos (1 BICC)
- [[fnd_kf_str_instances_vl|FND_KF_STR_INSTANCES_VL]] — 9 atributos (1 BICC)
- [[gl_autorev_criteria_sets|GL_AUTOREV_CRITERIA_SETS]] — 4 atributos
- [[gl_calendars|GL_CALENDARS]] — 21 atributos (3 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 80 atributos (1 PKs, 18 BICC)
- [[gl_period_types|GL_PERIOD_TYPES]] — 6 atributos
- [[gl_transaction_calendar|GL_TRANSACTION_CALENDAR]] — 11 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (2 BICC)
- [[per_users|PER_USERS]] — 10 atributos
- [[xla_acctg_methods_b|XLA_ACCTG_METHODS_B]] — 5 atributos (2 BICC)
- [[xla_acctg_methods_tl|XLA_ACCTG_METHODS_TL]] — 5 atributos (2 BICC)

---

## ⚙️ Atributos

### [[fnd_currencies_vl|FND_CURRENCIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurrencyContext | CONTEXT | — | — |
| 2 | CurrencyCurrencyCode | CURRENCY_CODE | — | ✅ |
| 3 | CurrencyCurrencyFlag | CURRENCY_FLAG | — | — |
| 4 | CurrencyDeriveEffective | DERIVE_EFFECTIVE | — | — |
| 5 | CurrencyDeriveFactor | DERIVE_FACTOR | — | — |
| 6 | CurrencyDeriveType | DERIVE_TYPE | — | — |
| 7 | CurrencyDescription | DESCRIPTION | — | — |
| 8 | CurrencyEnabledFlag | ENABLED_FLAG | — | — |
| 9 | CurrencyEndDateActive | END_DATE_ACTIVE | — | — |
| 10 | CurrencyExtendedPrecision | EXTENDED_PRECISION | — | — |
| 11 | CurrencyIsoFlag | ISO_FLAG | — | — |
| 12 | CurrencyIssuingTerritoryCode | ISSUING_TERRITORY_CODE | — | — |
| 13 | CurrencyMinimumAccountableUnit | MINIMUM_ACCOUNTABLE_UNIT | — | — |
| 14 | CurrencyName | NAME | — | — |
| 15 | CurrencyPrecision | PRECISION | — | — |
| 16 | CurrencyStartDateActive | START_DATE_ACTIVE | — | — |
| 17 | CurrencySymbol | SYMBOL | — | — |

### [[fnd_kf_str_instances_vl|FND_KF_STR_INSTANCES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | KeyFlexfieldStructureInstancApplicationId | APPLICATION_ID | — | — |
| 2 | KeyFlexfieldStructureInstancDescription | DESCRIPTION | — | — |
| 3 | KeyFlexfieldStructureInstancEnabledFlag | ENABLED_FLAG | — | — |
| 4 | KeyFlexfieldStructureInstancKeyFlexfieldCode | KEY_FLEXFIELD_CODE | — | — |
| 5 | KeyFlexfieldStructureInstancName | NAME | — | ✅ |
| 6 | KeyFlexfieldStructureInstancStructureId | STRUCTURE_ID | — | — |
| 7 | KeyFlexfieldStructureInstancStructureInstanceCode | STRUCTURE_INSTANCE_CODE | — | — |
| 8 | KeyFlexfieldStructureInstancStructureInstanceId | STRUCTURE_INSTANCE_ID | — | — |
| 9 | KeyFlexfieldStructureInstancStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |

### [[gl_autorev_criteria_sets|GL_AUTOREV_CRITERIA_SETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AutorevCriteriaSetCriteriaSetDesc | CRITERIA_SET_DESC | — | — |
| 2 | AutorevCriteriaSetCriteriaSetId | CRITERIA_SET_ID | — | — |
| 3 | AutorevCriteriaSetCriteriaSetName | CRITERIA_SET_NAME | — | — |
| 4 | AutorevCriteriaSetSecurityFlag | SECURITY_FLAG | — | — |

### [[gl_calendars|GL_CALENDARS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlCalendarsAdjPeriodFreqCode | ADJ_PERIOD_FREQ_CODE | — | — |
| 2 | GlCalendarsAdjPeriodsNum | ADJ_PERIODS_NUM | — | — |
| 3 | GlCalendarsCalendarId | CALENDAR_ID | — | — |
| 4 | GlCalendarsCalendarStartDate | CALENDAR_START_DATE | — | ✅ |
| 5 | GlCalendarsCalendarTypeCode | CALENDAR_TYPE_CODE | — | — |
| 6 | GlCalendarsDescription | DESCRIPTION | — | — |
| 7 | GlCalendarsLatestYearStartDate | LATEST_YEAR_START_DATE | — | — |
| 8 | GlCalendarsLegacyCalendarFlag | LEGACY_CALENDAR_FLAG | — | — |
| 9 | GlCalendarsLegacyRulesEnabledFlag | LEGACY_RULES_ENABLED_FLAG | — | — |
| 10 | GlCalendarsNonAdjPeriodFreqCode | NON_ADJ_PERIOD_FREQ_CODE | — | — |
| 11 | GlCalendarsNonAdjPeriodsNum | NON_ADJ_PERIODS_NUM | — | — |
| 12 | GlCalendarsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | GlCalendarsPeriodNameFormatCode | PERIOD_NAME_FORMAT_CODE | — | — |
| 14 | GlCalendarsPeriodNameSeparatorCode | PERIOD_NAME_SEPARATOR_CODE | — | — |
| 15 | GlCalendarsPeriodSetId | PERIOD_SET_ID | — | — |
| 16 | GlCalendarsPeriodSetName | PERIOD_SET_NAME | — | ✅ |
| 17 | GlCalendarsPeriodType | PERIOD_TYPE | — | ✅ |
| 18 | GlCalendarsPeriodTypeId | PERIOD_TYPE_ID | — | — |
| 19 | GlCalendarsSecurityFlag | SECURITY_FLAG | — | — |
| 20 | GlCalendarsUserPeriodNamePrefix | USER_PERIOD_NAME_PREFIX | — | — |
| 21 | GlCalendarsUserPeriodSetName | USER_PERIOD_SET_NAME | — | — |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgerAccountedPeriodType | ACCOUNTED_PERIOD_TYPE | — | ✅ |
| 2 | LedgerAlcLedgerTypeCode | ALC_LEDGER_TYPE_CODE | — | — |
| 3 | LedgerAllowIntercompanyPostFlag | ALLOW_INTERCOMPANY_POST_FLAG | — | — |
| 4 | LedgerAutomaticallyCreatedFlag | AUTOMATICALLY_CREATED_FLAG | — | — |
| 5 | LedgerAutorevAfterOpenPrdFlag | AUTOREV_AFTER_OPEN_PRD_FLAG | — | — |
| 6 | LedgerBalSegColumnName | BAL_SEG_COLUMN_NAME | — | ✅ |
| 7 | LedgerBalSegValueOptionCode | BAL_SEG_VALUE_OPTION_CODE | — | ✅ |
| 8 | LedgerBalSegValueSetId | BAL_SEG_VALUE_SET_ID | — | — |
| 9 | LedgerBudgetPeriodAvgRateType | BUDGET_PERIOD_AVG_RATE_TYPE | — | — |
| 10 | LedgerBudgetPeriodEndRateType | BUDGET_PERIOD_END_RATE_TYPE | — | — |
| 11 | LedgerChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | ✅ |
| 12 | LedgerCompleteFlag | COMPLETE_FLAG | — | — |
| 13 | LedgerCompletionStatusCode | COMPLETION_STATUS_CODE | — | — |
| 14 | LedgerConfigurationId | CONFIGURATION_ID | — | — |
| 15 | LedgerConsolidationLedgerFlag | CONSOLIDATION_LEDGER_FLAG | — | — |
| 16 | LedgerCreateJeFlag | CREATE_JE_FLAG | — | — |
| 17 | LedgerCreatedBy | CREATED_BY | — | ✅ |
| 18 | LedgerCreationDate | CREATION_DATE | — | ✅ |
| 19 | LedgerCriteriaSetId | CRITERIA_SET_ID | — | — |
| 20 | LedgerCumTransCodeCombinationId | CUM_TRANS_CODE_COMBINATION_ID | — | — |
| 21 | LedgerCurrencyCode | CURRENCY_CODE | — | ✅ |
| 22 | LedgerDailyTranslationRateType | DAILY_TRANSLATION_RATE_TYPE | — | — |
| 23 | LedgerDescription | DESCRIPTION | — | ✅ |
| 24 | LedgerEnableAutomaticTaxFlag | ENABLE_AUTOMATIC_TAX_FLAG | — | — |
| 25 | LedgerEnableAverageBalancesFlag | ENABLE_AVERAGE_BALANCES_FLAG | — | — |
| 26 | LedgerEnableBudgetaryControlFlag | ENABLE_BUDGETARY_CONTROL_FLAG | — | — |
| 27 | LedgerEnableJeApprovalFlag | ENABLE_JE_APPROVAL_FLAG | — | — |
| 28 | LedgerEnableReconciliationFlag | ENABLE_RECONCILIATION_FLAG | — | — |
| 29 | LedgerEnableRevalSsTrackFlag | ENABLE_REVAL_SS_TRACK_FLAG | — | — |
| 30 | LedgerEnableSecondaryTrackFlag | ENABLE_SECONDARY_TRACK_FLAG | — | — |
| 31 | LedgerFirstLedgerPeriodName | FIRST_LEDGER_PERIOD_NAME | — | — |
| 32 | LedgerFutureEnterablePeriodsLimit | FUTURE_ENTERABLE_PERIODS_LIMIT | — | — |
| 33 | LedgerId | LEDGER_ID | 🔑 | ✅ |
| 34 | LedgerImplicitAccessSetId | IMPLICIT_ACCESS_SET_ID | — | — |
| 35 | LedgerImplicitLedgerSetId | IMPLICIT_LEDGER_SET_ID | — | — |
| 36 | LedgerIntercoGainLossCcid | INTERCO_GAIN_LOSS_CCID | — | — |
| 37 | LedgerJrnlsGroupByDateFlag | JRNLS_GROUP_BY_DATE_FLAG | — | — |
| 38 | LedgerLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 39 | LedgerLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 40 | LedgerLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 41 | LedgerLatestEncumbranceYear | LATEST_ENCUMBRANCE_YEAR | — | — |
| 42 | LedgerLatestOpenedPeriodName | LATEST_OPENED_PERIOD_NAME | — | — |
| 43 | LedgerLeLedgerTypeCode | LE_LEDGER_TYPE_CODE | — | — |
| 44 | LedgerLedgerAttributes | LEDGER_ATTRIBUTES | — | — |
| 45 | LedgerLedgerCategoryCode | LEDGER_CATEGORY_CODE | — | ✅ |
| 46 | LedgerMgtSegColumnName | MGT_SEG_COLUMN_NAME | — | — |
| 47 | LedgerMgtSegValueOptionCode | MGT_SEG_VALUE_OPTION_CODE | — | — |
| 48 | LedgerMgtSegValueSetId | MGT_SEG_VALUE_SET_ID | — | — |
| 49 | LedgerName | NAME | — | ✅ |
| 50 | LedgerNetIncomeCodeCombinationId | NET_INCOME_CODE_COMBINATION_ID | — | — |
| 51 | LedgerObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 52 | LedgerObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 53 | LedgerPeriodAverageRateType | PERIOD_AVERAGE_RATE_TYPE | — | — |
| 54 | LedgerPeriodEndRateType | PERIOD_END_RATE_TYPE | — | — |
| 55 | LedgerPeriodSetName | PERIOD_SET_NAME | — | ✅ |
| 56 | LedgerPopUpStatAccountFlag | POP_UP_STAT_ACCOUNT_FLAG | — | — |
| 57 | LedgerPriorPrdNotificationFlag | PRIOR_PRD_NOTIFICATION_FLAG | — | — |
| 58 | LedgerRequireBudgetJournalsFlag | REQUIRE_BUDGET_JOURNALS_FLAG | — | — |
| 59 | LedgerResEncumbCodeCombinationId | RES_ENCUMB_CODE_COMBINATION_ID | — | — |
| 60 | LedgerRetEarnCodeCombinationId | RET_EARN_CODE_COMBINATION_ID | — | — |
| 61 | LedgerRevalFromPriLgrCurr | REVAL_FROM_PRI_LGR_CURR | — | — |
| 62 | LedgerRoundingCodeCombinationId | ROUNDING_CODE_COMBINATION_ID | — | — |
| 63 | LedgerShortName | SHORT_NAME | — | ✅ |
| 64 | LedgerSlaAccountingMethodCode | SLA_ACCOUNTING_METHOD_CODE | — | ✅ |
| 65 | LedgerSlaAccountingMethodType | SLA_ACCOUNTING_METHOD_TYPE | — | ✅ |
| 66 | LedgerSlaBalByLedgerCurrFlag | SLA_BAL_BY_LEDGER_CURR_FLAG | — | — |
| 67 | LedgerSlaDescriptionLanguage | SLA_DESCRIPTION_LANGUAGE | — | — |
| 68 | LedgerSlaEnteredCurBalSusCcid | SLA_ENTERED_CUR_BAL_SUS_CCID | — | — |
| 69 | LedgerSlaLedgerCashBasisFlag | SLA_LEDGER_CASH_BASIS_FLAG | — | — |
| 70 | LedgerSlaLedgerCurBalSusCcid | SLA_LEDGER_CUR_BAL_SUS_CCID | — | — |
| 71 | LedgerSlaSequencingFlag | SLA_SEQUENCING_FLAG | — | — |
| 72 | LedgerSuspenseAllowedFlag | SUSPENSE_ALLOWED_FLAG | — | ✅ |
| 73 | LedgerThresholdAmount | THRESHOLD_AMOUNT | — | — |
| 74 | LedgerTrackRoundingImbalanceFlag | TRACK_ROUNDING_IMBALANCE_FLAG | — | — |
| 75 | LedgerTransactionCalendarId | TRANSACTION_CALENDAR_ID | — | — |
| 76 | LedgerTranslateEodFlag | TRANSLATE_EOD_FLAG | — | — |
| 77 | LedgerTranslateQatdFlag | TRANSLATE_QATD_FLAG | — | — |
| 78 | LedgerTranslateYatdFlag | TRANSLATE_YATD_FLAG | — | — |
| 79 | LedgerUssglOptionCode | USSGL_OPTION_CODE | — | — |
| 80 | LedgerValidateJournalRefDate | VALIDATE_JOURNAL_REF_DATE | — | — |

### [[gl_period_types|GL_PERIOD_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcctPeriodTypeDescription | DESCRIPTION | — | — |
| 2 | AcctPeriodTypeNumberPerFiscalYear | NUMBER_PER_FISCAL_YEAR | — | — |
| 3 | AcctPeriodTypePeriodType | PERIOD_TYPE | — | — |
| 4 | AcctPeriodTypePeriodTypeId | PERIOD_TYPE_ID | — | — |
| 5 | AcctPeriodTypeUserPeriodType | USER_PERIOD_TYPE | — | — |
| 6 | AcctPeriodTypeYearTypeInName | YEAR_TYPE_IN_NAME | — | — |

### [[gl_transaction_calendar|GL_TRANSACTION_CALENDAR]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionCalendarDescription | DESCRIPTION | — | — |
| 2 | TransactionCalendarFriBusinessDayFlag | FRI_BUSINESS_DAY_FLAG | — | — |
| 3 | TransactionCalendarMonBusinessDayFlag | MON_BUSINESS_DAY_FLAG | — | — |
| 4 | TransactionCalendarName | NAME | — | — |
| 5 | TransactionCalendarSatBusinessDayFlag | SAT_BUSINESS_DAY_FLAG | — | — |
| 6 | TransactionCalendarSecurityFlag | SECURITY_FLAG | — | — |
| 7 | TransactionCalendarSunBusinessDayFlag | SUN_BUSINESS_DAY_FLAG | — | — |
| 8 | TransactionCalendarThuBusinessDayFlag | THU_BUSINESS_DAY_FLAG | — | — |
| 9 | TransactionCalendarTransactionCalendarId | TRANSACTION_CALENDAR_ID | — | — |
| 10 | TransactionCalendarTueBusinessDayFlag | TUE_BUSINESS_DAY_FLAG | — | — |
| 11 | TransactionCalendarWedBusinessDayFlag | WED_BUSINESS_DAY_FLAG | — | — |

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
| 1 | UserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | UserCreatedByPersonId | PERSON_ID | — | — |
| 3 | UserCreatedByUserGuid | USER_GUID | — | — |
| 4 | UserCreatedByUserId | USER_ID | — | — |
| 5 | UserCreatedByUsername | USERNAME | — | — |
| 6 | UserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 8 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 9 | UserUpdatedByUserId | USER_ID | — | — |
| 10 | UserUpdatedByUsername | USERNAME | — | — |

### [[xla_acctg_methods_b|XLA_ACCTG_METHODS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcctgMethodAccountingCoaId | ACCOUNTING_COA_ID | — | — |
| 2 | AcctgMethodAccountingMethodCode | ACCOUNTING_METHOD_CODE | — | ✅ |
| 3 | AcctgMethodAccountingMethodTypeCode | ACCOUNTING_METHOD_TYPE_CODE | — | ✅ |
| 4 | AcctgMethodEnabledFlag | ENABLED_FLAG | — | — |
| 5 | AcctgMethodTransactionCoaId | TRANSACTION_COA_ID | — | — |

### [[xla_acctg_methods_tl|XLA_ACCTG_METHODS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcctgMethodDescription | DESCRIPTION | — | ✅ |
| 2 | AcctgMethodName | NAME | — | ✅ |
| 3 | AcctgMethodTransAcctngMethodCode | ACCOUNTING_METHOD_CODE | — | — |
| 4 | AcctgMethodTransAcctngMethodTypeCode | ACCOUNTING_METHOD_TYPE_CODE | — | — |
| 5 | AcctgMethodTransLanguage | LANGUAGE | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
