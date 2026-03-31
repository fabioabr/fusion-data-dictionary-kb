---
id: DOC-GL-PVO-LedgerSetPVO
doc_type: system-doc
title: "LedgerSetPVO — PVO General Ledger"
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
  - LedgerSetPVO
  - ledgersetpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LedgerSetPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Ledger Set. Acessa as tabelas: FND_CURRENCIES_VL, FND_KF_STR_INSTANCES_VL, GL_AUTOREV_CRITERIA_SETS (+6).

**Caminho:** `FscmTopModelAM.FinGlLedgerSetAM.LedgerSetPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 251 | 9 | 1 | 13 | 5% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_currencies_vl|FND_CURRENCIES_VL]] — 17 atributos
- [[fnd_kf_str_instances_vl|FND_KF_STR_INSTANCES_VL]] — 9 atributos
- [[gl_autorev_criteria_sets|GL_AUTOREV_CRITERIA_SETS]] — 4 atributos
- [[gl_calendars|GL_CALENDARS]] — 21 atributos
- [[gl_ledgers|GL_LEDGERS]] — 158 atributos (1 PKs, 8 BICC)
- [[gl_ledger_set_assignments|GL_LEDGER_SET_ASSIGNMENTS]] — 11 atributos (3 BICC)
- [[gl_transaction_calendar|GL_TRANSACTION_CALENDAR]] — 11 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (2 BICC)
- [[per_users|PER_USERS]] — 10 atributos

---

## ⚙️ Atributos

### [[fnd_currencies_vl|FND_CURRENCIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurrencyContext | CONTEXT | — | — |
| 2 | CurrencyCurrencyCode | CURRENCY_CODE | — | — |
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
| 5 | KeyFlexfieldStructureInstancName | NAME | — | — |
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
| 4 | GlCalendarsCalendarStartDate | CALENDAR_START_DATE | — | — |
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
| 16 | GlCalendarsPeriodSetName | PERIOD_SET_NAME | — | — |
| 17 | GlCalendarsPeriodType | PERIOD_TYPE | — | — |
| 18 | GlCalendarsPeriodTypeId | PERIOD_TYPE_ID | — | — |
| 19 | GlCalendarsSecurityFlag | SECURITY_FLAG | — | — |
| 20 | GlCalendarsUserPeriodNamePrefix | USER_PERIOD_NAME_PREFIX | — | — |
| 21 | GlCalendarsUserPeriodSetName | USER_PERIOD_SET_NAME | — | — |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgerId | LEDGER_ID | 🔑 | ✅ |
| 2 | LedgerSetAccountedPeriodType | ACCOUNTED_PERIOD_TYPE | — | — |
| 3 | LedgerSetAlcLedgerTypeCode | ALC_LEDGER_TYPE_CODE | — | — |
| 4 | LedgerSetAllowIntercompanyPostFlag | ALLOW_INTERCOMPANY_POST_FLAG | — | — |
| 5 | LedgerSetAutomaticallyCreatedFlag | AUTOMATICALLY_CREATED_FLAG | — | — |
| 6 | LedgerSetAutorevAfterOpenPrdFlag | AUTOREV_AFTER_OPEN_PRD_FLAG | — | — |
| 7 | LedgerSetBalSegColumnName | BAL_SEG_COLUMN_NAME | — | — |
| 8 | LedgerSetBalSegValueOptionCode | BAL_SEG_VALUE_OPTION_CODE | — | — |
| 9 | LedgerSetBalSegValueSetId | BAL_SEG_VALUE_SET_ID | — | — |
| 10 | LedgerSetBudgetPeriodAvgRateType | BUDGET_PERIOD_AVG_RATE_TYPE | — | — |
| 11 | LedgerSetBudgetPeriodEndRateType | BUDGET_PERIOD_END_RATE_TYPE | — | — |
| 12 | LedgerSetChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 13 | LedgerSetCompleteFlag | COMPLETE_FLAG | — | — |
| 14 | LedgerSetCompletionStatusCode | COMPLETION_STATUS_CODE | — | — |
| 15 | LedgerSetConfigurationId | CONFIGURATION_ID | — | — |
| 16 | LedgerSetConsolidationLedgerFlag | CONSOLIDATION_LEDGER_FLAG | — | — |
| 17 | LedgerSetCreateJeFlag | CREATE_JE_FLAG | — | — |
| 18 | LedgerSetCreatedBy | CREATED_BY | — | — |
| 19 | LedgerSetCreationDate | CREATION_DATE | — | ✅ |
| 20 | LedgerSetCriteriaSetId | CRITERIA_SET_ID | — | — |
| 21 | LedgerSetCumTransCodeCombinationId | CUM_TRANS_CODE_COMBINATION_ID | — | — |
| 22 | LedgerSetCurrencyCode | CURRENCY_CODE | — | — |
| 23 | LedgerSetDailyTranslationRateType | DAILY_TRANSLATION_RATE_TYPE | — | — |
| 24 | LedgerSetDescription | DESCRIPTION | — | — |
| 25 | LedgerSetEnableAutomaticTaxFlag | ENABLE_AUTOMATIC_TAX_FLAG | — | — |
| 26 | LedgerSetEnableAverageBalancesFlag | ENABLE_AVERAGE_BALANCES_FLAG | — | — |
| 27 | LedgerSetEnableBudgetaryControlFlag | ENABLE_BUDGETARY_CONTROL_FLAG | — | — |
| 28 | LedgerSetEnableJeApprovalFlag | ENABLE_JE_APPROVAL_FLAG | — | — |
| 29 | LedgerSetEnableReconciliationFlag | ENABLE_RECONCILIATION_FLAG | — | — |
| 30 | LedgerSetEnableRevalSsTrackFlag | ENABLE_REVAL_SS_TRACK_FLAG | — | — |
| 31 | LedgerSetEnableSecondaryTrackFlag | ENABLE_SECONDARY_TRACK_FLAG | — | — |
| 32 | LedgerSetFirstLedgerPeriodName | FIRST_LEDGER_PERIOD_NAME | — | — |
| 33 | LedgerSetFutureEnterablePeriodsLimit | FUTURE_ENTERABLE_PERIODS_LIMIT | — | — |
| 34 | LedgerSetImplicitAccessSetId | IMPLICIT_ACCESS_SET_ID | — | — |
| 35 | LedgerSetImplicitLedgerSetId | IMPLICIT_LEDGER_SET_ID | — | — |
| 36 | LedgerSetJrnlsGroupByDateFlag | JRNLS_GROUP_BY_DATE_FLAG | — | — |
| 37 | LedgerSetLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 38 | LedgerSetLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 39 | LedgerSetLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 40 | LedgerSetLatestEncumbranceYear | LATEST_ENCUMBRANCE_YEAR | — | — |
| 41 | LedgerSetLatestOpenedPeriodName | LATEST_OPENED_PERIOD_NAME | — | — |
| 42 | LedgerSetLeLedgerTypeCode | LE_LEDGER_TYPE_CODE | — | — |
| 43 | LedgerSetLedgerAttributes | LEDGER_ATTRIBUTES | — | — |
| 44 | LedgerSetLedgerCategoryCode | LEDGER_CATEGORY_CODE | — | — |
| 45 | LedgerSetLedgerId | LEDGER_ID | — | ✅ |
| 46 | LedgerSetMgtSegColumnName | MGT_SEG_COLUMN_NAME | — | — |
| 47 | LedgerSetMgtSegValueOptionCode | MGT_SEG_VALUE_OPTION_CODE | — | — |
| 48 | LedgerSetMgtSegValueSetId | MGT_SEG_VALUE_SET_ID | — | — |
| 49 | LedgerSetName | NAME | — | ✅ |
| 50 | LedgerSetNetIncomeCodeCombinationId | NET_INCOME_CODE_COMBINATION_ID | — | — |
| 51 | LedgerSetObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 52 | LedgerSetObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 53 | LedgerSetPeriodAverageRateType | PERIOD_AVERAGE_RATE_TYPE | — | — |
| 54 | LedgerSetPeriodEndRateType | PERIOD_END_RATE_TYPE | — | — |
| 55 | LedgerSetPeriodSetName | PERIOD_SET_NAME | — | — |
| 56 | LedgerSetPopUpStatAccountFlag | POP_UP_STAT_ACCOUNT_FLAG | — | — |
| 57 | LedgerSetPriorPrdNotificationFlag | PRIOR_PRD_NOTIFICATION_FLAG | — | — |
| 58 | LedgerSetRequireBudgetJournalsFlag | REQUIRE_BUDGET_JOURNALS_FLAG | — | — |
| 59 | LedgerSetResEncumbCodeCombinationId | RES_ENCUMB_CODE_COMBINATION_ID | — | — |
| 60 | LedgerSetRetEarnCodeCombinationId | RET_EARN_CODE_COMBINATION_ID | — | — |
| 61 | LedgerSetRevalFromPriLgrCurr | REVAL_FROM_PRI_LGR_CURR | — | — |
| 62 | LedgerSetRoundingCodeCombinationId | ROUNDING_CODE_COMBINATION_ID | — | — |
| 63 | LedgerSetShortName | SHORT_NAME | — | — |
| 64 | LedgerSetSlaAccountingMethodCode | SLA_ACCOUNTING_METHOD_CODE | — | — |
| 65 | LedgerSetSlaAccountingMethodType | SLA_ACCOUNTING_METHOD_TYPE | — | — |
| 66 | LedgerSetSlaBalByLedgerCurrFlag | SLA_BAL_BY_LEDGER_CURR_FLAG | — | — |
| 67 | LedgerSetSlaDescriptionLanguage | SLA_DESCRIPTION_LANGUAGE | — | — |
| 68 | LedgerSetSlaEnteredCurBalSusCcid | SLA_ENTERED_CUR_BAL_SUS_CCID | — | — |
| 69 | LedgerSetSlaLedgerCashBasisFlag | SLA_LEDGER_CASH_BASIS_FLAG | — | — |
| 70 | LedgerSetSlaLedgerCurBalSusCcid | SLA_LEDGER_CUR_BAL_SUS_CCID | — | — |
| 71 | LedgerSetSlaSequencingFlag | SLA_SEQUENCING_FLAG | — | — |
| 72 | LedgerSetSuspenseAllowedFlag | SUSPENSE_ALLOWED_FLAG | — | — |
| 73 | LedgerSetThresholdAmount | THRESHOLD_AMOUNT | — | — |
| 74 | LedgerSetTrackRoundingImbalanceFlag | TRACK_ROUNDING_IMBALANCE_FLAG | — | — |
| 75 | LedgerSetTransactionCalendarId | TRANSACTION_CALENDAR_ID | — | — |
| 76 | LedgerSetTranslateEodFlag | TRANSLATE_EOD_FLAG | — | — |
| 77 | LedgerSetTranslateQatdFlag | TRANSLATE_QATD_FLAG | — | — |
| 78 | LedgerSetTranslateYatdFlag | TRANSLATE_YATD_FLAG | — | — |
| 79 | LedgerSetUssglOptionCode | USSGL_OPTION_CODE | — | — |
| 80 | LedgerSetValidateJournalRefDate | VALIDATE_JOURNAL_REF_DATE | — | — |
| 81 | LedgersAccountedPeriodType | ACCOUNTED_PERIOD_TYPE | — | — |
| 82 | LedgersAlcLedgerTypeCode | ALC_LEDGER_TYPE_CODE | — | — |
| 83 | LedgersAllowIntercompanyPostFlag | ALLOW_INTERCOMPANY_POST_FLAG | — | — |
| 84 | LedgersAutomaticallyCreatedFlag | AUTOMATICALLY_CREATED_FLAG | — | — |
| 85 | LedgersAutorevAfterOpenPrdFlag | AUTOREV_AFTER_OPEN_PRD_FLAG | — | — |
| 86 | LedgersBalSegColumnName | BAL_SEG_COLUMN_NAME | — | — |
| 87 | LedgersBalSegValueOptionCode | BAL_SEG_VALUE_OPTION_CODE | — | — |
| 88 | LedgersBalSegValueSetId | BAL_SEG_VALUE_SET_ID | — | — |
| 89 | LedgersBudgetPeriodAvgRateType | BUDGET_PERIOD_AVG_RATE_TYPE | — | — |
| 90 | LedgersBudgetPeriodEndRateType | BUDGET_PERIOD_END_RATE_TYPE | — | — |
| 91 | LedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 92 | LedgersCompleteFlag | COMPLETE_FLAG | — | — |
| 93 | LedgersCompletionStatusCode | COMPLETION_STATUS_CODE | — | — |
| 94 | LedgersConfigurationId | CONFIGURATION_ID | — | — |
| 95 | LedgersConsolidationLedgerFlag | CONSOLIDATION_LEDGER_FLAG | — | — |
| 96 | LedgersCreateJeFlag | CREATE_JE_FLAG | — | — |
| 97 | LedgersCreatedBy | CREATED_BY | — | ✅ |
| 98 | LedgersCreationDate | CREATION_DATE | — | — |
| 99 | LedgersCriteriaSetId | CRITERIA_SET_ID | — | — |
| 100 | LedgersCumTransCodeCombinationId | CUM_TRANS_CODE_COMBINATION_ID | — | — |
| 101 | LedgersCurrencyCode | CURRENCY_CODE | — | — |
| 102 | LedgersDailyTranslationRateType | DAILY_TRANSLATION_RATE_TYPE | — | — |
| 103 | LedgersDescription | DESCRIPTION | — | — |
| 104 | LedgersEnableAutomaticTaxFlag | ENABLE_AUTOMATIC_TAX_FLAG | — | — |
| 105 | LedgersEnableAverageBalancesFlag | ENABLE_AVERAGE_BALANCES_FLAG | — | — |
| 106 | LedgersEnableBudgetaryControlFlag | ENABLE_BUDGETARY_CONTROL_FLAG | — | — |
| 107 | LedgersEnableJeApprovalFlag | ENABLE_JE_APPROVAL_FLAG | — | — |
| 108 | LedgersEnableReconciliationFlag | ENABLE_RECONCILIATION_FLAG | — | — |
| 109 | LedgersEnableRevalSsTrackFlag | ENABLE_REVAL_SS_TRACK_FLAG | — | — |
| 110 | LedgersEnableSecondaryTrackFlag | ENABLE_SECONDARY_TRACK_FLAG | — | — |
| 111 | LedgersFirstLedgerPeriodName | FIRST_LEDGER_PERIOD_NAME | — | — |
| 112 | LedgersFutureEnterablePeriodsLimit | FUTURE_ENTERABLE_PERIODS_LIMIT | — | — |
| 113 | LedgersImplicitAccessSetId | IMPLICIT_ACCESS_SET_ID | — | — |
| 114 | LedgersImplicitLedgerSetId | IMPLICIT_LEDGER_SET_ID | — | — |
| 115 | LedgersJrnlsGroupByDateFlag | JRNLS_GROUP_BY_DATE_FLAG | — | — |
| 116 | LedgersLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 117 | LedgersLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 118 | LedgersLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 119 | LedgersLatestEncumbranceYear | LATEST_ENCUMBRANCE_YEAR | — | — |
| 120 | LedgersLatestOpenedPeriodName | LATEST_OPENED_PERIOD_NAME | — | — |
| 121 | LedgersLeLedgerTypeCode | LE_LEDGER_TYPE_CODE | — | — |
| 122 | LedgersLedgerAttributes | LEDGER_ATTRIBUTES | — | — |
| 123 | LedgersLedgerCategoryCode | LEDGER_CATEGORY_CODE | — | — |
| 124 | LedgersMgtSegColumnName | MGT_SEG_COLUMN_NAME | — | — |
| 125 | LedgersMgtSegValueOptionCode | MGT_SEG_VALUE_OPTION_CODE | — | — |
| 126 | LedgersMgtSegValueSetId | MGT_SEG_VALUE_SET_ID | — | — |
| 127 | LedgersName | NAME | — | — |
| 128 | LedgersNetIncomeCodeCombinationId | NET_INCOME_CODE_COMBINATION_ID | — | — |
| 129 | LedgersObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 130 | LedgersObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 131 | LedgersPeriodAverageRateType | PERIOD_AVERAGE_RATE_TYPE | — | — |
| 132 | LedgersPeriodEndRateType | PERIOD_END_RATE_TYPE | — | — |
| 133 | LedgersPeriodSetName | PERIOD_SET_NAME | — | — |
| 134 | LedgersPopUpStatAccountFlag | POP_UP_STAT_ACCOUNT_FLAG | — | — |
| 135 | LedgersPriorPrdNotificationFlag | PRIOR_PRD_NOTIFICATION_FLAG | — | — |
| 136 | LedgersRequireBudgetJournalsFlag | REQUIRE_BUDGET_JOURNALS_FLAG | — | — |
| 137 | LedgersResEncumbCodeCombinationId | RES_ENCUMB_CODE_COMBINATION_ID | — | — |
| 138 | LedgersRetEarnCodeCombinationId | RET_EARN_CODE_COMBINATION_ID | — | — |
| 139 | LedgersRevalFromPriLgrCurr | REVAL_FROM_PRI_LGR_CURR | — | — |
| 140 | LedgersRoundingCodeCombinationId | ROUNDING_CODE_COMBINATION_ID | — | — |
| 141 | LedgersShortName | SHORT_NAME | — | — |
| 142 | LedgersSlaAccountingMethodCode | SLA_ACCOUNTING_METHOD_CODE | — | — |
| 143 | LedgersSlaAccountingMethodType | SLA_ACCOUNTING_METHOD_TYPE | — | — |
| 144 | LedgersSlaBalByLedgerCurrFlag | SLA_BAL_BY_LEDGER_CURR_FLAG | — | — |
| 145 | LedgersSlaDescriptionLanguage | SLA_DESCRIPTION_LANGUAGE | — | — |
| 146 | LedgersSlaEnteredCurBalSusCcid | SLA_ENTERED_CUR_BAL_SUS_CCID | — | — |
| 147 | LedgersSlaLedgerCashBasisFlag | SLA_LEDGER_CASH_BASIS_FLAG | — | — |
| 148 | LedgersSlaLedgerCurBalSusCcid | SLA_LEDGER_CUR_BAL_SUS_CCID | — | — |
| 149 | LedgersSlaSequencingFlag | SLA_SEQUENCING_FLAG | — | — |
| 150 | LedgersSuspenseAllowedFlag | SUSPENSE_ALLOWED_FLAG | — | — |
| 151 | LedgersThresholdAmount | THRESHOLD_AMOUNT | — | — |
| 152 | LedgersTrackRoundingImbalanceFlag | TRACK_ROUNDING_IMBALANCE_FLAG | — | — |
| 153 | LedgersTransactionCalendarId | TRANSACTION_CALENDAR_ID | — | — |
| 154 | LedgersTranslateEodFlag | TRANSLATE_EOD_FLAG | — | — |
| 155 | LedgersTranslateQatdFlag | TRANSLATE_QATD_FLAG | — | — |
| 156 | LedgersTranslateYatdFlag | TRANSLATE_YATD_FLAG | — | — |
| 157 | LedgersUssglOptionCode | USSGL_OPTION_CODE | — | — |
| 158 | LedgersValidateJournalRefDate | VALIDATE_JOURNAL_REF_DATE | — | — |

### [[gl_ledger_set_assignments|GL_LEDGER_SET_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgerSetAssignmentCreatedBy | CREATED_BY | — | — |
| 2 | LedgerSetAssignmentCreationDate | CREATION_DATE | — | — |
| 3 | LedgerSetAssignmentEndDate | END_DATE | — | ✅ |
| 4 | LedgerSetAssignmentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LedgerSetAssignmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | LedgerSetAssignmentLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | LedgerSetAssignmentLedgerId | LEDGER_ID | — | — |
| 8 | LedgerSetAssignmentLedgerSetId | LEDGER_SET_ID | — | — |
| 9 | LedgerSetAssignmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | LedgerSetAssignmentStartDate | START_DATE | — | ✅ |
| 11 | LedgerSetAssignmentStatusCode | STATUS_CODE | — | — |

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

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
