---
id: DOC-GL-PVO-BalancePVO
doc_type: system-doc
title: "BalancePVO — PVO General Ledger"
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
  - BalancePVO
  - balancepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BalancePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Balance. Acessa as tabelas: GL_BALANCES, GL_ENCUMBRANCE_TYPES_VL, GL_LEDGERS (+3).

**Caminho:** `FscmTopModelAM.FinGlInquiryBalancesAM.BalancePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 171 | 6 | 8 | 31 | 18% |

---

## 🔗 Tabelas Relacionadas

- [[gl_balances|GL_BALANCES]] — 38 atributos (8 PKs, 23 BICC)
- [[gl_encumbrance_types_vl|GL_ENCUMBRANCE_TYPES_VL]] — 2 atributos (1 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 112 atributos (6 BICC)
- [[gl_ledger_segment_values|GL_LEDGER_SEGMENT_VALUES]] — 4 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 8 atributos (1 BICC)
- [[per_users|PER_USERS]] — 7 atributos

---

## ⚙️ Atributos

### [[gl_balances|GL_BALANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActualFlag | ACTUAL_FLAG | 🔑 | ✅ |
| 2 | BeginBalanceCr | BEGIN_BALANCE_CR | — | ✅ |
| 3 | BeginBalanceCrBeq | BEGIN_BALANCE_CR_BEQ | — | ✅ |
| 4 | BeginBalanceDr | BEGIN_BALANCE_DR | — | ✅ |
| 5 | BeginBalanceDrBeq | BEGIN_BALANCE_DR_BEQ | — | ✅ |
| 6 | BudgetVersionId | BUDGET_VERSION_ID | 🔑 | ✅ |
| 7 | CodeCombinationId | CODE_COMBINATION_ID | 🔑 | ✅ |
| 8 | CurrencyCode | CURRENCY_CODE | 🔑 | ✅ |
| 9 | EncumbranceTypeId | ENCUMBRANCE_TYPE_ID | 🔑 | ✅ |
| 10 | GlBalancesEncumbranceDocId | ENCUMBRANCE_DOC_ID | — | — |
| 11 | GlBalancesEncumbranceLineNum | ENCUMBRANCE_LINE_NUM | — | — |
| 12 | GlBalancesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | GlBalancesPeriodNum | PERIOD_NUM | — | — |
| 14 | GlBalancesPeriodToDateAdb | PERIOD_TO_DATE_ADB | — | — |
| 15 | GlBalancesPeriodType | PERIOD_TYPE | — | — |
| 16 | GlBalancesPeriodYear | PERIOD_YEAR | — | — |
| 17 | GlBalancesProjectToDateAdb | PROJECT_TO_DATE_ADB | — | — |
| 18 | GlBalancesProjectToDateCr | PROJECT_TO_DATE_CR | — | — |
| 19 | GlBalancesProjectToDateCrBeq | PROJECT_TO_DATE_CR_BEQ | — | — |
| 20 | GlBalancesProjectToDateDr | PROJECT_TO_DATE_DR | — | — |
| 21 | GlBalancesProjectToDateDrBeq | PROJECT_TO_DATE_DR_BEQ | — | — |
| 22 | GlBalancesQuarterToDateAdb | QUARTER_TO_DATE_ADB | — | — |
| 23 | GlBalancesQuarterToDateCr | QUARTER_TO_DATE_CR | — | ✅ |
| 24 | GlBalancesQuarterToDateCrBeq | QUARTER_TO_DATE_CR_BEQ | — | ✅ |
| 25 | GlBalancesQuarterToDateDr | QUARTER_TO_DATE_DR | — | ✅ |
| 26 | GlBalancesQuarterToDateDrBeq | QUARTER_TO_DATE_DR_BEQ | — | ✅ |
| 27 | GlBalancesRevaluationStatus | REVALUATION_STATUS | — | — |
| 28 | GlBalancesYearToDateAdb | YEAR_TO_DATE_ADB | — | — |
| 29 | LastUpdateDateBal | LAST_UPDATE_DATE | — | ✅ |
| 30 | LastUpdatedByBal | LAST_UPDATED_BY | — | ✅ |
| 31 | LedgerId | LEDGER_ID | 🔑 | ✅ |
| 32 | PeriodName | PERIOD_NAME | 🔑 | ✅ |
| 33 | PeriodNetCr | PERIOD_NET_CR | — | ✅ |
| 34 | PeriodNetCrBeq | PERIOD_NET_CR_BEQ | — | ✅ |
| 35 | PeriodNetDr | PERIOD_NET_DR | — | ✅ |
| 36 | PeriodNetDrBeq | PERIOD_NET_DR_BEQ | — | ✅ |
| 37 | TemplateId | TEMPLATE_ID | — | ✅ |
| 38 | TranslatedFlag | TRANSLATED_FLAG | 🔑 | ✅ |

### [[gl_encumbrance_types_vl|GL_ENCUMBRANCE_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EncumbranceType | ENCUMBRANCE_TYPE | — | ✅ |
| 2 | JournalEncumbranceTypeEncumbranceTypeId | ENCUMBRANCE_TYPE_ID | — | — |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | ✅ |
| 2 | GlLedgerAccountedPeriodType | ACCOUNTED_PERIOD_TYPE | — | — |
| 3 | GlLedgerAlcLedgerTypeCode | ALC_LEDGER_TYPE_CODE | — | — |
| 4 | GlLedgerAllowIntercompanyPostFlag | ALLOW_INTERCOMPANY_POST_FLAG | — | — |
| 5 | GlLedgerApDocSequencingOptionFlag | AP_DOC_SEQUENCING_OPTION_FLAG | — | — |
| 6 | GlLedgerArDocSequencingOptionFlag | AR_DOC_SEQUENCING_OPTION_FLAG | — | — |
| 7 | GlLedgerAttribute1 | ATTRIBUTE1 | — | — |
| 8 | GlLedgerAttribute10 | ATTRIBUTE10 | — | — |
| 9 | GlLedgerAttribute11 | ATTRIBUTE11 | — | — |
| 10 | GlLedgerAttribute12 | ATTRIBUTE12 | — | — |
| 11 | GlLedgerAttribute13 | ATTRIBUTE13 | — | — |
| 12 | GlLedgerAttribute14 | ATTRIBUTE14 | — | — |
| 13 | GlLedgerAttribute15 | ATTRIBUTE15 | — | — |
| 14 | GlLedgerAttribute2 | ATTRIBUTE2 | — | — |
| 15 | GlLedgerAttribute3 | ATTRIBUTE3 | — | — |
| 16 | GlLedgerAttribute4 | ATTRIBUTE4 | — | — |
| 17 | GlLedgerAttribute5 | ATTRIBUTE5 | — | — |
| 18 | GlLedgerAttribute6 | ATTRIBUTE6 | — | — |
| 19 | GlLedgerAttribute7 | ATTRIBUTE7 | — | — |
| 20 | GlLedgerAttribute8 | ATTRIBUTE8 | — | — |
| 21 | GlLedgerAttribute9 | ATTRIBUTE9 | — | — |
| 22 | GlLedgerAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 23 | GlLedgerAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | GlLedgerAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | GlLedgerAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | GlLedgerAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | GlLedgerAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | GlLedgerAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 29 | GlLedgerAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 30 | GlLedgerAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 31 | GlLedgerAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 32 | GlLedgerAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 33 | GlLedgerAutomateSecJrnlRevFlag | AUTOMATE_SEC_JRNL_REV_FLAG | — | — |
| 34 | GlLedgerAutomaticallyCreatedFlag | AUTOMATICALLY_CREATED_FLAG | — | — |
| 35 | GlLedgerAutorevAfterOpenPrdFlag | AUTOREV_AFTER_OPEN_PRD_FLAG | — | — |
| 36 | GlLedgerBalSegColumnName | BAL_SEG_COLUMN_NAME | — | — |
| 37 | GlLedgerBalSegValueOptionCode | BAL_SEG_VALUE_OPTION_CODE | — | — |
| 38 | GlLedgerBalSegValueSetId | BAL_SEG_VALUE_SET_ID | — | — |
| 39 | GlLedgerBudgetPeriodAvgRateType | BUDGET_PERIOD_AVG_RATE_TYPE | — | — |
| 40 | GlLedgerBudgetPeriodEndRateType | BUDGET_PERIOD_END_RATE_TYPE | — | — |
| 41 | GlLedgerCompleteFlag | COMPLETE_FLAG | — | — |
| 42 | GlLedgerCompletionStatusCode | COMPLETION_STATUS_CODE | — | — |
| 43 | GlLedgerConfigurationId | CONFIGURATION_ID | — | — |
| 44 | GlLedgerConsolidationLedgerFlag | CONSOLIDATION_LEDGER_FLAG | — | — |
| 45 | GlLedgerCreateJeFlag | CREATE_JE_FLAG | — | — |
| 46 | GlLedgerCreatedBy | CREATED_BY | — | — |
| 47 | GlLedgerCreationDate | CREATION_DATE | — | — |
| 48 | GlLedgerCriteriaSetId | CRITERIA_SET_ID | — | — |
| 49 | GlLedgerCumTransCodeCombinationId | CUM_TRANS_CODE_COMBINATION_ID | — | — |
| 50 | GlLedgerDailyTranslationRateType | DAILY_TRANSLATION_RATE_TYPE | — | — |
| 51 | GlLedgerDescription | DESCRIPTION | — | — |
| 52 | GlLedgerEnableAutomaticTaxFlag | ENABLE_AUTOMATIC_TAX_FLAG | — | — |
| 53 | GlLedgerEnableAverageBalancesFlag | ENABLE_AVERAGE_BALANCES_FLAG | — | — |
| 54 | GlLedgerEnableBudgetaryControlFlag | ENABLE_BUDGETARY_CONTROL_FLAG | — | — |
| 55 | GlLedgerEnableJeApprovalFlag | ENABLE_JE_APPROVAL_FLAG | — | — |
| 56 | GlLedgerEnableReconciliationFlag | ENABLE_RECONCILIATION_FLAG | — | — |
| 57 | GlLedgerEnableRevalSsTrackFlag | ENABLE_REVAL_SS_TRACK_FLAG | — | — |
| 58 | GlLedgerEnableSecondaryTrackFlag | ENABLE_SECONDARY_TRACK_FLAG | — | — |
| 59 | GlLedgerEnfSeqDateCorrelationCode | ENF_SEQ_DATE_CORRELATION_CODE | — | — |
| 60 | GlLedgerFirstLedgerPeriodName | FIRST_LEDGER_PERIOD_NAME | — | — |
| 61 | GlLedgerFutureEnterablePeriodsLimit | FUTURE_ENTERABLE_PERIODS_LIMIT | — | — |
| 62 | GlLedgerImplicitAccessSetId | IMPLICIT_ACCESS_SET_ID | — | — |
| 63 | GlLedgerImplicitLedgerSetId | IMPLICIT_LEDGER_SET_ID | — | — |
| 64 | GlLedgerIntercoGainLossCcid | INTERCO_GAIN_LOSS_CCID | — | — |
| 65 | GlLedgerJrnlsGroupByDateFlag | JRNLS_GROUP_BY_DATE_FLAG | — | — |
| 66 | GlLedgerLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 67 | GlLedgerLatestEncumbranceYear | LATEST_ENCUMBRANCE_YEAR | — | — |
| 68 | GlLedgerLatestOpenedPeriodName | LATEST_OPENED_PERIOD_NAME | — | — |
| 69 | GlLedgerLeLedgerTypeCode | LE_LEDGER_TYPE_CODE | — | — |
| 70 | GlLedgerLedgerAttributes | LEDGER_ATTRIBUTES | — | — |
| 71 | GlLedgerLedgerId | LEDGER_ID | — | — |
| 72 | GlLedgerMgtSegColumnName | MGT_SEG_COLUMN_NAME | — | — |
| 73 | GlLedgerMgtSegValueOptionCode | MGT_SEG_VALUE_OPTION_CODE | — | — |
| 74 | GlLedgerMgtSegValueSetId | MGT_SEG_VALUE_SET_ID | — | — |
| 75 | GlLedgerName | NAME | — | — |
| 76 | GlLedgerNetClosingBalFlag | NET_CLOSING_BAL_FLAG | — | — |
| 77 | GlLedgerNetIncomeCodeCombinationId | NET_INCOME_CODE_COMBINATION_ID | — | — |
| 78 | GlLedgerObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 79 | GlLedgerObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 80 | GlLedgerPeriodAverageRateType | PERIOD_AVERAGE_RATE_TYPE | — | — |
| 81 | GlLedgerPeriodEndRateType | PERIOD_END_RATE_TYPE | — | — |
| 82 | GlLedgerPeriodSetName | PERIOD_SET_NAME | — | ✅ |
| 83 | GlLedgerPopUpStatAccountFlag | POP_UP_STAT_ACCOUNT_FLAG | — | — |
| 84 | GlLedgerPriorPrdNotificationFlag | PRIOR_PRD_NOTIFICATION_FLAG | — | — |
| 85 | GlLedgerRequireBudgetJournalsFlag | REQUIRE_BUDGET_JOURNALS_FLAG | — | — |
| 86 | GlLedgerResEncumbCodeCombinationId | RES_ENCUMB_CODE_COMBINATION_ID | — | — |
| 87 | GlLedgerRetEarnCodeCombinationId | RET_EARN_CODE_COMBINATION_ID | — | — |
| 88 | GlLedgerRevalFromPriLgrCurr | REVAL_FROM_PRI_LGR_CURR | — | — |
| 89 | GlLedgerRoundingCodeCombinationId | ROUNDING_CODE_COMBINATION_ID | — | — |
| 90 | GlLedgerSequencingModeCode | SEQUENCING_MODE_CODE | — | — |
| 91 | GlLedgerShortName | SHORT_NAME | — | — |
| 92 | GlLedgerSlaAccountingMethodCode | SLA_ACCOUNTING_METHOD_CODE | — | — |
| 93 | GlLedgerSlaAccountingMethodType | SLA_ACCOUNTING_METHOD_TYPE | — | — |
| 94 | GlLedgerSlaBalByLedgerCurrFlag | SLA_BAL_BY_LEDGER_CURR_FLAG | — | — |
| 95 | GlLedgerSlaDescriptionLanguage | SLA_DESCRIPTION_LANGUAGE | — | — |
| 96 | GlLedgerSlaEnteredCurBalSusCcid | SLA_ENTERED_CUR_BAL_SUS_CCID | — | — |
| 97 | GlLedgerSlaLedgerCashBasisFlag | SLA_LEDGER_CASH_BASIS_FLAG | — | — |
| 98 | GlLedgerSlaLedgerCurBalSusCcid | SLA_LEDGER_CUR_BAL_SUS_CCID | — | — |
| 99 | GlLedgerSlaSequencingFlag | SLA_SEQUENCING_FLAG | — | — |
| 100 | GlLedgerSuspenseAllowedFlag | SUSPENSE_ALLOWED_FLAG | — | — |
| 101 | GlLedgerThresholdAmount | THRESHOLD_AMOUNT | — | — |
| 102 | GlLedgerTrackRoundingImbalanceFlag | TRACK_ROUNDING_IMBALANCE_FLAG | — | — |
| 103 | GlLedgerTransactionCalendarId | TRANSACTION_CALENDAR_ID | — | — |
| 104 | GlLedgerTranslateEodFlag | TRANSLATE_EOD_FLAG | — | — |
| 105 | GlLedgerTranslateQatdFlag | TRANSLATE_QATD_FLAG | — | — |
| 106 | GlLedgerTranslateYatdFlag | TRANSLATE_YATD_FLAG | — | — |
| 107 | GlLedgerUssglOptionCode | USSGL_OPTION_CODE | — | — |
| 108 | GlLedgerValidateJournalRefDate | VALIDATE_JOURNAL_REF_DATE | — | — |
| 109 | LastUpdateDateSob | LAST_UPDATE_DATE | — | ✅ |
| 110 | LastUpdatedBySob | LAST_UPDATED_BY | — | ✅ |
| 111 | LedgerCategoryCode | LEDGER_CATEGORY_CODE | — | ✅ |
| 112 | LedgerCurrencyCode | CURRENCY_CODE | — | ✅ |

### [[gl_ledger_segment_values|GL_LEDGER_SEGMENT_VALUES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgerSegValLedgerId | LEDGER_ID | — | — |
| 2 | LedgerSegValLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 3 | LedgerSegValSegmentTypeCode | SEGMENT_TYPE_CODE | — | — |
| 4 | LedgerSegValSegmentValue | SEGMENT_VALUE | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonUpdatedByCreatedBy | CREATED_BY | — | — |
| 2 | PersonUpdatedByCreationDate | CREATION_DATE | — | — |
| 3 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 4 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 5 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 6 | PersonUpdatedByLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | PersonUpdatedByLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LastUpdatedByUserCreatedBy | CREATED_BY | — | — |
| 2 | LastUpdatedByUserCreationDate | CREATION_DATE | — | — |
| 3 | LastUpdatedByUserLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 4 | LastUpdatedByUserLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 5 | LastUpdatedByUserPersonId | PERSON_ID | — | — |
| 6 | LastUpdatedByUserUserId | USER_ID | — | — |
| 7 | LastUpdatedByUserUsername | USERNAME | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
