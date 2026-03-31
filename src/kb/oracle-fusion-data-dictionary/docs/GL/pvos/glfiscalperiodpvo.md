---
id: DOC-GL-PVO-GLFiscalPeriodPVO
doc_type: system-doc
title: "GLFiscalPeriodPVO — PVO General Ledger"
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
  - GLFiscalPeriodPVO
  - glfiscalperiodpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GLFiscalPeriodPVO

## 📌 Visão Geral

View Object para extração BICC de dados de GLFiscal Period. Acessa as tabelas: GL_CALENDARS, GL_FISCAL_PERIOD_V, GL_FISCAL_QUARTER_V (+3).

**Caminho:** `FscmTopModelAM.FinGlCalAccAM.GLFiscalPeriodPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 136 | 6 | 5 | 25 | 18% |

---

## 🔗 Tabelas Relacionadas

- [[gl_calendars|GL_CALENDARS]] — 26 atributos (4 BICC)
- [[gl_fiscal_period_v|GL_FISCAL_PERIOD_V]] — 17 atributos (4 PKs, 16 BICC)
- [[gl_fiscal_quarter_v|GL_FISCAL_QUARTER_V]] — 9 atributos (2 BICC)
- [[gl_fiscal_year_v|GL_FISCAL_YEAR_V]] — 6 atributos (2 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 75 atributos (1 PKs, 1 BICC)
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
| 21 | GlCalendarsPeriodSetName | PERIOD_SET_NAME | — | ✅ |
| 22 | GlCalendarsPeriodType | PERIOD_TYPE | — | — |
| 23 | GlCalendarsPeriodTypeId | PERIOD_TYPE_ID | — | — |
| 24 | GlCalendarsSecurityFlag | SECURITY_FLAG | — | — |
| 25 | GlCalendarsUserPeriodNamePrefix | USER_PERIOD_NAME_PREFIX | — | — |
| 26 | GlCalendarsUserPeriodSetName | USER_PERIOD_SET_NAME | — | ✅ |

### [[gl_fiscal_period_v|GL_FISCAL_PERIOD_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalPeriodAdjustmentPeriodFlag | ADJUSTMENT_PERIOD_FLAG | — | ✅ |
| 2 | FiscalPeriodFiscalPeriodCreationDate | FISCAL_PERIOD_CREATION_DATE | — | — |
| 3 | FiscalPeriodFiscalPeriodEndDate | FISCAL_PERIOD_END_DATE | — | ✅ |
| 4 | FiscalPeriodFiscalPeriodLastUpdateDate | FISCAL_PERIOD_LAST_UPDATE_DATE | — | ✅ |
| 5 | FiscalPeriodFiscalPeriodNumber | FISCAL_PERIOD_NUMBER | — | ✅ |
| 6 | FiscalPeriodFiscalPeriodSetCreationDate | FISCAL_PERIODSET_CREATION_DATE | — | ✅ |
| 7 | FiscalPeriodFiscalPeriodStartDate | FISCAL_PERIOD_START_DATE | — | ✅ |
| 8 | FiscalPeriodFiscalQuarterEndDate | FISCAL_QUARTER_END_DATE | — | ✅ |
| 9 | FiscalPeriodFiscalQuarterNumber | FISCAL_QUARTER_NUMBER | — | ✅ |
| 10 | FiscalPeriodFiscalQuarterStartDate | FISCAL_QUARTER_START_DATE | — | ✅ |
| 11 | FiscalPeriodFiscalYearEndDate | FISCAL_YEAR_END_DATE | — | ✅ |
| 12 | FiscalPeriodFiscalYearNumber | FISCAL_YEAR_NUMBER | — | ✅ |
| 13 | FiscalPeriodFiscalYearStartDate | FISCAL_YEAR_START_DATE | — | ✅ |
| 14 | FiscalPeriodName | FISCAL_PERIOD_NAME | 🔑 | ✅ |
| 15 | FiscalPeriodSetId | FISCAL_PERIOD_SET_ID | 🔑 | ✅ |
| 16 | FiscalPeriodSetName | FISCAL_PERIOD_SET_NAME | 🔑 | ✅ |
| 17 | FiscalPeriodType | FISCAL_PERIOD_TYPE | 🔑 | ✅ |

### [[gl_fiscal_quarter_v|GL_FISCAL_QUARTER_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalQuarterFiscalPeriodSetId | FISCAL_PERIOD_SET_ID | — | — |
| 2 | FiscalQuarterFiscalPeriodSetName | FISCAL_PERIOD_SET_NAME | — | — |
| 3 | FiscalQuarterFiscalPeriodType | FISCAL_PERIOD_TYPE | — | — |
| 4 | FiscalQuarterFiscalQuarterEndDate | FISCAL_QUARTER_END_DATE | — | ✅ |
| 5 | FiscalQuarterFiscalQuarterNumber | FISCAL_QUARTER_NUMBER | — | — |
| 6 | FiscalQuarterFiscalQuarterStartDate | FISCAL_QUARTER_START_DATE | — | ✅ |
| 7 | FiscalQuarterFiscalYearEndDate | FISCAL_YEAR_END_DATE | — | — |
| 8 | FiscalQuarterFiscalYearNumber | FISCAL_YEAR_NUMBER | — | — |
| 9 | FiscalQuarterFiscalYearStartDate | FISCAL_YEAR_START_DATE | — | — |

### [[gl_fiscal_year_v|GL_FISCAL_YEAR_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalYearFiscalPeriodSetId | FISCAL_PERIOD_SET_ID | — | — |
| 2 | FiscalYearFiscalPeriodSetName | FISCAL_PERIOD_SET_NAME | — | — |
| 3 | FiscalYearFiscalPeriodType | FISCAL_PERIOD_TYPE | — | — |
| 4 | FiscalYearFiscalYearEndDate | FISCAL_YEAR_END_DATE | — | ✅ |
| 5 | FiscalYearFiscalYearNumber | FISCAL_YEAR_NUMBER | — | — |
| 6 | FiscalYearFiscalYearStartDate | FISCAL_YEAR_START_DATE | — | ✅ |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgerAccountedPeriodType | ACCOUNTED_PERIOD_TYPE | — | — |
| 2 | LedgerAlcLedgerTypeCode | ALC_LEDGER_TYPE_CODE | — | — |
| 3 | LedgerAllowIntercompanyPostFlag | ALLOW_INTERCOMPANY_POST_FLAG | — | — |
| 4 | LedgerAutomaticallyCreatedFlag | AUTOMATICALLY_CREATED_FLAG | — | — |
| 5 | LedgerAutorevAfterOpenPrdFlag | AUTOREV_AFTER_OPEN_PRD_FLAG | — | — |
| 6 | LedgerBalSegColumnName | BAL_SEG_COLUMN_NAME | — | — |
| 7 | LedgerBalSegValueOptionCode | BAL_SEG_VALUE_OPTION_CODE | — | — |
| 8 | LedgerBalSegValueSetId | BAL_SEG_VALUE_SET_ID | — | — |
| 9 | LedgerBudgetPeriodAvgRateType | BUDGET_PERIOD_AVG_RATE_TYPE | — | — |
| 10 | LedgerBudgetPeriodEndRateType | BUDGET_PERIOD_END_RATE_TYPE | — | — |
| 11 | LedgerChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 12 | LedgerCompleteFlag | COMPLETE_FLAG | — | — |
| 13 | LedgerCompletionStatusCode | COMPLETION_STATUS_CODE | — | — |
| 14 | LedgerConfigurationId | CONFIGURATION_ID | — | — |
| 15 | LedgerConsolidationLedgerFlag | CONSOLIDATION_LEDGER_FLAG | — | — |
| 16 | LedgerCreateJeFlag | CREATE_JE_FLAG | — | — |
| 17 | LedgerCriteriaSetId | CRITERIA_SET_ID | — | — |
| 18 | LedgerCumTransCodeCombinationId | CUM_TRANS_CODE_COMBINATION_ID | — | — |
| 19 | LedgerCurrencyCode | CURRENCY_CODE | — | — |
| 20 | LedgerDailyTranslationRateType | DAILY_TRANSLATION_RATE_TYPE | — | — |
| 21 | LedgerDescription | DESCRIPTION | — | — |
| 22 | LedgerEnableAutomaticTaxFlag | ENABLE_AUTOMATIC_TAX_FLAG | — | — |
| 23 | LedgerEnableAverageBalancesFlag | ENABLE_AVERAGE_BALANCES_FLAG | — | — |
| 24 | LedgerEnableBudgetaryControlFlag | ENABLE_BUDGETARY_CONTROL_FLAG | — | — |
| 25 | LedgerEnableJeApprovalFlag | ENABLE_JE_APPROVAL_FLAG | — | — |
| 26 | LedgerEnableReconciliationFlag | ENABLE_RECONCILIATION_FLAG | — | — |
| 27 | LedgerEnableRevalSsTrackFlag | ENABLE_REVAL_SS_TRACK_FLAG | — | — |
| 28 | LedgerEnableSecondaryTrackFlag | ENABLE_SECONDARY_TRACK_FLAG | — | — |
| 29 | LedgerFirstLedgerPeriodName | FIRST_LEDGER_PERIOD_NAME | — | — |
| 30 | LedgerFutureEnterablePeriodsLimit | FUTURE_ENTERABLE_PERIODS_LIMIT | — | — |
| 31 | LedgerImplicitAccessSetId | IMPLICIT_ACCESS_SET_ID | — | — |
| 32 | LedgerImplicitLedgerSetId | IMPLICIT_LEDGER_SET_ID | — | — |
| 33 | LedgerIntercoGainLossCcid | INTERCO_GAIN_LOSS_CCID | — | — |
| 34 | LedgerJrnlsGroupByDateFlag | JRNLS_GROUP_BY_DATE_FLAG | — | — |
| 35 | LedgerLatestEncumbranceYear | LATEST_ENCUMBRANCE_YEAR | — | — |
| 36 | LedgerLatestOpenedPeriodName | LATEST_OPENED_PERIOD_NAME | — | — |
| 37 | LedgerLeLedgerTypeCode | LE_LEDGER_TYPE_CODE | — | — |
| 38 | LedgerLedgerAttributes | LEDGER_ATTRIBUTES | — | — |
| 39 | LedgerLedgerCategoryCode | LEDGER_CATEGORY_CODE | — | — |
| 40 | LedgerLedgerId | LEDGER_ID | 🔑 | ✅ |
| 41 | LedgerMgtSegColumnName | MGT_SEG_COLUMN_NAME | — | — |
| 42 | LedgerMgtSegValueOptionCode | MGT_SEG_VALUE_OPTION_CODE | — | — |
| 43 | LedgerMgtSegValueSetId | MGT_SEG_VALUE_SET_ID | — | — |
| 44 | LedgerName | NAME | — | — |
| 45 | LedgerNetIncomeCodeCombinationId | NET_INCOME_CODE_COMBINATION_ID | — | — |
| 46 | LedgerObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 47 | LedgerPeriodAverageRateType | PERIOD_AVERAGE_RATE_TYPE | — | — |
| 48 | LedgerPeriodEndRateType | PERIOD_END_RATE_TYPE | — | — |
| 49 | LedgerPeriodSetName | PERIOD_SET_NAME | — | — |
| 50 | LedgerPopUpStatAccountFlag | POP_UP_STAT_ACCOUNT_FLAG | — | — |
| 51 | LedgerPriorPrdNotificationFlag | PRIOR_PRD_NOTIFICATION_FLAG | — | — |
| 52 | LedgerRequireBudgetJournalsFlag | REQUIRE_BUDGET_JOURNALS_FLAG | — | — |
| 53 | LedgerResEncumbCodeCombinationId | RES_ENCUMB_CODE_COMBINATION_ID | — | — |
| 54 | LedgerRetEarnCodeCombinationId | RET_EARN_CODE_COMBINATION_ID | — | — |
| 55 | LedgerRevalFromPriLgrCurr | REVAL_FROM_PRI_LGR_CURR | — | — |
| 56 | LedgerRoundingCodeCombinationId | ROUNDING_CODE_COMBINATION_ID | — | — |
| 57 | LedgerShortName | SHORT_NAME | — | — |
| 58 | LedgerSlaAccountingMethodCode | SLA_ACCOUNTING_METHOD_CODE | — | — |
| 59 | LedgerSlaAccountingMethodType | SLA_ACCOUNTING_METHOD_TYPE | — | — |
| 60 | LedgerSlaBalByLedgerCurrFlag | SLA_BAL_BY_LEDGER_CURR_FLAG | — | — |
| 61 | LedgerSlaDescriptionLanguage | SLA_DESCRIPTION_LANGUAGE | — | — |
| 62 | LedgerSlaEnteredCurBalSusCcid | SLA_ENTERED_CUR_BAL_SUS_CCID | — | — |
| 63 | LedgerSlaLedgerCashBasisFlag | SLA_LEDGER_CASH_BASIS_FLAG | — | — |
| 64 | LedgerSlaLedgerCurBalSusCcid | SLA_LEDGER_CUR_BAL_SUS_CCID | — | — |
| 65 | LedgerSlaSequencingFlag | SLA_SEQUENCING_FLAG | — | — |
| 66 | LedgerSuspenseAllowedFlag | SUSPENSE_ALLOWED_FLAG | — | — |
| 67 | LedgerThresholdAmount | THRESHOLD_AMOUNT | — | — |
| 68 | LedgerTrackRoundingImbalanceFlag | TRACK_ROUNDING_IMBALANCE_FLAG | — | — |
| 69 | LedgerTransactionCalendarId | TRANSACTION_CALENDAR_ID | — | — |
| 70 | LedgerTranslateEodFlag | TRANSLATE_EOD_FLAG | — | — |
| 71 | LedgerTranslateQatdFlag | TRANSLATE_QATD_FLAG | — | — |
| 72 | LedgerTranslateYatdFlag | TRANSLATE_YATD_FLAG | — | — |
| 73 | LedgerUssglOptionCode | USSGL_OPTION_CODE | — | — |
| 74 | LedgerValidateJournalRefDate | VALIDATE_JOURNAL_REF_DATE | — | — |
| 75 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[xcc_control_budgets|XCC_CONTROL_BUDGETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ControlBudgetUnsecuredChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 2 | ControlBudgetUnsecuredControlBudgetId | CONTROL_BUDGET_ID | — | — |
| 3 | ControlBudgetUnsecuredLedgerId | LEDGER_ID | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
