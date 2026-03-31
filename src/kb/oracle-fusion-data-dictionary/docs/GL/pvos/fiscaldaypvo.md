---
id: DOC-GL-PVO-FiscalDayPVO
doc_type: system-doc
title: "FiscalDayPVO — PVO General Ledger"
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
  - FiscalDayPVO
  - fiscaldaypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FiscalDayPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fiscal Day. Acessa as tabelas: GL_CALENDARS, GL_FISCAL_DAY_V, GL_LEDGERS (+1).

**Caminho:** `FscmTopModelAM.FinGlCalAccAM.FiscalDayPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 138 | 4 | 5 | 22 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[gl_calendars|GL_CALENDARS]] — 26 atributos (3 BICC)
- [[gl_fiscal_day_v|GL_FISCAL_DAY_V]] — 29 atributos (5 PKs, 18 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 80 atributos (1 BICC)
- [[xcc_control_budgets|XCC_CONTROL_BUDGETS]] — 3 atributos

---

## ⚙️ Atributos

### [[gl_calendars|GL_CALENDARS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlCalendarsAdjPeriodFreqCode | ADJ_PERIOD_FREQ_CODE | — | — |
| 2 | GlCalendarsAdjPeriodsNum | ADJ_PERIODS_NUM | — | — |
| 3 | GlCalendarsCalendarId | CALENDAR_ID | — | ✅ |
| 4 | GlCalendarsCalendarStartDate | CALENDAR_START_DATE | — | — |
| 5 | GlCalendarsCalendarTypeCode | CALENDAR_TYPE_CODE | — | — |
| 6 | GlCalendarsCreatedBy | CREATED_BY | — | — |
| 7 | GlCalendarsCreationDate | CREATION_DATE | — | — |
| 8 | GlCalendarsDescription | DESCRIPTION | — | — |
| 9 | GlCalendarsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | GlCalendarsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | GlCalendarsLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | GlCalendarsLatestYearStartDate | LATEST_YEAR_START_DATE | — | — |
| 13 | GlCalendarsLegacyCalendarFlag | LEGACY_CALENDAR_FLAG | — | — |
| 14 | GlCalendarsLegacyRulesEnabledFlag | LEGACY_RULES_ENABLED_FLAG | — | — |
| 15 | GlCalendarsNonAdjPeriodFreqCode | NON_ADJ_PERIOD_FREQ_CODE | — | — |
| 16 | GlCalendarsNonAdjPeriodsNum | NON_ADJ_PERIODS_NUM | — | — |
| 17 | GlCalendarsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | GlCalendarsPeriodNameFormatCode | PERIOD_NAME_FORMAT_CODE | — | — |
| 19 | GlCalendarsPeriodNameSeparatorCode | PERIOD_NAME_SEPARATOR_CODE | — | — |
| 20 | GlCalendarsPeriodSetId | PERIOD_SET_ID | — | — |
| 21 | GlCalendarsPeriodSetName1 | PERIOD_SET_NAME | — | — |
| 22 | GlCalendarsPeriodType | PERIOD_TYPE | — | — |
| 23 | GlCalendarsPeriodTypeId | PERIOD_TYPE_ID | — | — |
| 24 | GlCalendarsSecurityFlag | SECURITY_FLAG | — | — |
| 25 | GlCalendarsUserPeriodNamePrefix | USER_PERIOD_NAME_PREFIX | — | — |
| 26 | GlCalendarsUserPeriodSetName | USER_PERIOD_SET_NAME | — | ✅ |

### [[gl_fiscal_day_v|GL_FISCAL_DAY_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | DayOfMonth | DAY_OF_MONTH | — | — |
| 4 | DayOfWeek | DAY_OF_WEEK | — | ✅ |
| 5 | DayOfYear | DAY_OF_YEAR | — | — |
| 6 | EnterpriseId | ENTERPRISE_ID | — | — |
| 7 | FiscalPeriodAdjustmentPeriodFlag | ADJUSTMENT_PERIOD_FLAG | — | ✅ |
| 8 | FiscalPeriodCreationDate | FISCAL_PERIOD_CREATION_DATE | — | — |
| 9 | FiscalPeriodEndDate | FISCAL_PERIOD_END_DATE | — | ✅ |
| 10 | FiscalPeriodLastUpdateDate | FISCAL_PERIOD_LAST_UPDATE_DATE | — | ✅ |
| 11 | FiscalPeriodName | FISCAL_PERIOD_NAME | — | ✅ |
| 12 | FiscalPeriodNumber | FISCAL_PERIOD_NUMBER | 🔑 | ✅ |
| 13 | FiscalPeriodSetId | FISCAL_PERIOD_SET_ID | — | ✅ |
| 14 | FiscalPeriodSetName | FISCAL_PERIOD_SET_NAME | 🔑 | ✅ |
| 15 | FiscalPeriodStartDate | FISCAL_PERIOD_START_DATE | — | ✅ |
| 16 | FiscalPeriodType | FISCAL_PERIOD_TYPE | 🔑 | ✅ |
| 17 | FiscalPeriodsetCreationDate | FISCAL_PERIODSET_CREATION_DATE | — | — |
| 18 | FiscalQuarterEndDate | FISCAL_QUARTER_END_DATE | — | ✅ |
| 19 | FiscalQuarterNumber | FISCAL_QUARTER_NUMBER | — | ✅ |
| 20 | FiscalQuarterStartDate | FISCAL_QUARTER_START_DATE | — | ✅ |
| 21 | FiscalYearEndDate | FISCAL_YEAR_END_DATE | — | ✅ |
| 22 | FiscalYearNumber | FISCAL_YEAR_NUMBER | 🔑 | ✅ |
| 23 | FiscalYearStartDate | FISCAL_YEAR_START_DATE | — | ✅ |
| 24 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 25 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 26 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 27 | ParentMonth | PARENT_MONTH | — | — |
| 28 | ParentWeek | PARENT_WEEK | — | — |
| 29 | ReportDate | REPORT_DATE | 🔑 | ✅ |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccountedPeriodType | ACCOUNTED_PERIOD_TYPE | — | — |
| 2 | AlcLedgerTypeCode | ALC_LEDGER_TYPE_CODE | — | — |
| 3 | AllowIntercompanyPostFlag | ALLOW_INTERCOMPANY_POST_FLAG | — | — |
| 4 | AutomaticallyCreatedFlag | AUTOMATICALLY_CREATED_FLAG | — | — |
| 5 | AutorevAfterOpenPrdFlag | AUTOREV_AFTER_OPEN_PRD_FLAG | — | — |
| 6 | BalSegColumnName | BAL_SEG_COLUMN_NAME | — | — |
| 7 | BalSegValueOptionCode | BAL_SEG_VALUE_OPTION_CODE | — | — |
| 8 | BalSegValueSetId | BAL_SEG_VALUE_SET_ID | — | — |
| 9 | BudgetPeriodAvgRateType | BUDGET_PERIOD_AVG_RATE_TYPE | — | — |
| 10 | BudgetPeriodEndRateType | BUDGET_PERIOD_END_RATE_TYPE | — | — |
| 11 | ChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 12 | CompleteFlag | COMPLETE_FLAG | — | — |
| 13 | CompletionStatusCode | COMPLETION_STATUS_CODE | — | — |
| 14 | ConfigurationId | CONFIGURATION_ID | — | — |
| 15 | ConsolidationLedgerFlag | CONSOLIDATION_LEDGER_FLAG | — | — |
| 16 | CreateJeFlag | CREATE_JE_FLAG | — | — |
| 17 | CriteriaSetId | CRITERIA_SET_ID | — | — |
| 18 | CumTransCodeCombinationId | CUM_TRANS_CODE_COMBINATION_ID | — | — |
| 19 | CurrencyCode | CURRENCY_CODE | — | — |
| 20 | DailyTranslationRateType | DAILY_TRANSLATION_RATE_TYPE | — | — |
| 21 | Description | DESCRIPTION | — | — |
| 22 | EnableAutomaticTaxFlag | ENABLE_AUTOMATIC_TAX_FLAG | — | — |
| 23 | EnableAverageBalancesFlag | ENABLE_AVERAGE_BALANCES_FLAG | — | — |
| 24 | EnableBudgetaryControlFlag | ENABLE_BUDGETARY_CONTROL_FLAG | — | — |
| 25 | EnableJeApprovalFlag | ENABLE_JE_APPROVAL_FLAG | — | — |
| 26 | EnableReconciliationFlag | ENABLE_RECONCILIATION_FLAG | — | — |
| 27 | EnableRevalSsTrackFlag | ENABLE_REVAL_SS_TRACK_FLAG | — | — |
| 28 | EnableSecondaryTrackFlag | ENABLE_SECONDARY_TRACK_FLAG | — | — |
| 29 | FirstLedgerPeriodName | FIRST_LEDGER_PERIOD_NAME | — | — |
| 30 | FutureEnterablePeriodsLimit | FUTURE_ENTERABLE_PERIODS_LIMIT | — | — |
| 31 | ImplicitAccessSetId | IMPLICIT_ACCESS_SET_ID | — | — |
| 32 | ImplicitLedgerSetId | IMPLICIT_LEDGER_SET_ID | — | — |
| 33 | IntercoGainLossCcid | INTERCO_GAIN_LOSS_CCID | — | — |
| 34 | JrnlsGroupByDateFlag | JRNLS_GROUP_BY_DATE_FLAG | — | — |
| 35 | LatestEncumbranceYear | LATEST_ENCUMBRANCE_YEAR | — | — |
| 36 | LatestOpenedPeriodName | LATEST_OPENED_PERIOD_NAME | — | — |
| 37 | LeLedgerTypeCode | LE_LEDGER_TYPE_CODE | — | — |
| 38 | LedgerAttributes | LEDGER_ATTRIBUTES | — | — |
| 39 | LedgerCategoryCode | LEDGER_CATEGORY_CODE | — | — |
| 40 | LedgerCreatedBy | CREATED_BY | — | — |
| 41 | LedgerCreationDate | CREATION_DATE | — | — |
| 42 | LedgerId | LEDGER_ID | — | — |
| 43 | LedgerLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 44 | LedgerLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 45 | LedgerLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 46 | LedgerName | NAME | — | — |
| 47 | MgtSegColumnName | MGT_SEG_COLUMN_NAME | — | — |
| 48 | MgtSegValueOptionCode | MGT_SEG_VALUE_OPTION_CODE | — | — |
| 49 | MgtSegValueSetId | MGT_SEG_VALUE_SET_ID | — | — |
| 50 | NetIncomeCodeCombinationId | NET_INCOME_CODE_COMBINATION_ID | — | — |
| 51 | ObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 52 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 53 | PeriodAverageRateType | PERIOD_AVERAGE_RATE_TYPE | — | — |
| 54 | PeriodEndRateType | PERIOD_END_RATE_TYPE | — | — |
| 55 | PeriodSetName | PERIOD_SET_NAME | — | — |
| 56 | PopUpStatAccountFlag | POP_UP_STAT_ACCOUNT_FLAG | — | — |
| 57 | PriorPrdNotificationFlag | PRIOR_PRD_NOTIFICATION_FLAG | — | — |
| 58 | RequireBudgetJournalsFlag | REQUIRE_BUDGET_JOURNALS_FLAG | — | — |
| 59 | ResEncumbCodeCombinationId | RES_ENCUMB_CODE_COMBINATION_ID | — | — |
| 60 | RetEarnCodeCombinationId | RET_EARN_CODE_COMBINATION_ID | — | — |
| 61 | RevalFromPriLgrCurr | REVAL_FROM_PRI_LGR_CURR | — | — |
| 62 | RoundingCodeCombinationId | ROUNDING_CODE_COMBINATION_ID | — | — |
| 63 | ShortName | SHORT_NAME | — | — |
| 64 | SlaAccountingMethodCode | SLA_ACCOUNTING_METHOD_CODE | — | — |
| 65 | SlaAccountingMethodType | SLA_ACCOUNTING_METHOD_TYPE | — | — |
| 66 | SlaBalByLedgerCurrFlag | SLA_BAL_BY_LEDGER_CURR_FLAG | — | — |
| 67 | SlaDescriptionLanguage | SLA_DESCRIPTION_LANGUAGE | — | — |
| 68 | SlaEnteredCurBalSusCcid | SLA_ENTERED_CUR_BAL_SUS_CCID | — | — |
| 69 | SlaLedgerCashBasisFlag | SLA_LEDGER_CASH_BASIS_FLAG | — | — |
| 70 | SlaLedgerCurBalSusCcid | SLA_LEDGER_CUR_BAL_SUS_CCID | — | — |
| 71 | SlaSequencingFlag | SLA_SEQUENCING_FLAG | — | — |
| 72 | SuspenseAllowedFlag | SUSPENSE_ALLOWED_FLAG | — | — |
| 73 | ThresholdAmount | THRESHOLD_AMOUNT | — | — |
| 74 | TrackRoundingImbalanceFlag | TRACK_ROUNDING_IMBALANCE_FLAG | — | — |
| 75 | TransactionCalendarId | TRANSACTION_CALENDAR_ID | — | — |
| 76 | TranslateEodFlag | TRANSLATE_EOD_FLAG | — | — |
| 77 | TranslateQatdFlag | TRANSLATE_QATD_FLAG | — | — |
| 78 | TranslateYatdFlag | TRANSLATE_YATD_FLAG | — | — |
| 79 | UssglOptionCode | USSGL_OPTION_CODE | — | — |
| 80 | ValidateJournalRefDate | VALIDATE_JOURNAL_REF_DATE | — | — |

### [[xcc_control_budgets|XCC_CONTROL_BUDGETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ControlBudgetUnsecuredChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 2 | ControlBudgetUnsecuredControlBudgetId | CONTROL_BUDGET_ID | — | — |
| 3 | ControlBudgetUnsecuredLedgerId | LEDGER_ID | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
