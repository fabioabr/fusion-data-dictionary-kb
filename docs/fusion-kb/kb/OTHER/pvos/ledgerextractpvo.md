---
id: DOC-OTHER-PVO-LedgerExtractPVO
doc_type: system-doc
title: "LedgerExtractPVO — PVO Cross-Module"
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
  - LedgerExtractPVO
  - ledgerextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LedgerExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Ledger Extract. Acessa as tabelas: GL_LEDGERS, XLA_ACCTG_METHODS_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.GlBiccExtractAM.LedgerExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 104 | 2 | 1 | 73 | 70% |

---

## 🔗 Tabelas Relacionadas

- [[gl_ledgers|GL_LEDGERS]] — 99 atributos (1 PKs, 73 BICC)
- [[xla_acctg_methods_tl|XLA_ACCTG_METHODS_TL]] — 5 atributos

---

## ⚙️ Atributos

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgerAccountedPeriodType | ACCOUNTED_PERIOD_TYPE | — | ✅ |
| 2 | LedgerAllowIntercompanyPostFlag | ALLOW_INTERCOMPANY_POST_FLAG | — | ✅ |
| 3 | LedgerApDocSequencingOptionFlag | AP_DOC_SEQUENCING_OPTION_FLAG | — | ✅ |
| 4 | LedgerArDocSequencingOptionFlag | AR_DOC_SEQUENCING_OPTION_FLAG | — | ✅ |
| 5 | LedgerAttribute1 | ATTRIBUTE1 | — | — |
| 6 | LedgerAttribute10 | ATTRIBUTE10 | — | — |
| 7 | LedgerAttribute11 | ATTRIBUTE11 | — | — |
| 8 | LedgerAttribute12 | ATTRIBUTE12 | — | — |
| 9 | LedgerAttribute13 | ATTRIBUTE13 | — | — |
| 10 | LedgerAttribute14 | ATTRIBUTE14 | — | — |
| 11 | LedgerAttribute15 | ATTRIBUTE15 | — | — |
| 12 | LedgerAttribute2 | ATTRIBUTE2 | — | — |
| 13 | LedgerAttribute3 | ATTRIBUTE3 | — | — |
| 14 | LedgerAttribute4 | ATTRIBUTE4 | — | — |
| 15 | LedgerAttribute5 | ATTRIBUTE5 | — | — |
| 16 | LedgerAttribute6 | ATTRIBUTE6 | — | — |
| 17 | LedgerAttribute7 | ATTRIBUTE7 | — | — |
| 18 | LedgerAttribute8 | ATTRIBUTE8 | — | — |
| 19 | LedgerAttribute9 | ATTRIBUTE9 | — | — |
| 20 | LedgerAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 21 | LedgerAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 22 | LedgerAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 23 | LedgerAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 24 | LedgerAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 25 | LedgerAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 26 | LedgerAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 27 | LedgerAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 28 | LedgerAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 29 | LedgerAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 30 | LedgerAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 31 | LedgerAutomateSecJrnlRevFlag | AUTOMATE_SEC_JRNL_REV_FLAG | — | ✅ |
| 32 | LedgerAutorevAfterOpenPrdFlag | AUTOREV_AFTER_OPEN_PRD_FLAG | — | ✅ |
| 33 | LedgerBalSegColumnName | BAL_SEG_COLUMN_NAME | — | ✅ |
| 34 | LedgerBalSegValueOptionCode | BAL_SEG_VALUE_OPTION_CODE | — | ✅ |
| 35 | LedgerBalSegValueSetId | BAL_SEG_VALUE_SET_ID | — | ✅ |
| 36 | LedgerChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | ✅ |
| 37 | LedgerCompleteFlag | COMPLETE_FLAG | — | ✅ |
| 38 | LedgerCompletionStatusCode | COMPLETION_STATUS_CODE | — | ✅ |
| 39 | LedgerConfigurationId | CONFIGURATION_ID | — | ✅ |
| 40 | LedgerCreatedBy | CREATED_BY | — | ✅ |
| 41 | LedgerCreationDate | CREATION_DATE | — | ✅ |
| 42 | LedgerCriteriaSetId | CRITERIA_SET_ID | — | ✅ |
| 43 | LedgerCumTransCodeCombinationId | CUM_TRANS_CODE_COMBINATION_ID | — | ✅ |
| 44 | LedgerCurrencyCode | CURRENCY_CODE | — | ✅ |
| 45 | LedgerDailyTranslationRateType | DAILY_TRANSLATION_RATE_TYPE | — | ✅ |
| 46 | LedgerDescription | DESCRIPTION | — | ✅ |
| 47 | LedgerEnableAutomaticTaxFlag | ENABLE_AUTOMATIC_TAX_FLAG | — | ✅ |
| 48 | LedgerEnableAverageBalancesFlag | ENABLE_AVERAGE_BALANCES_FLAG | — | ✅ |
| 49 | LedgerEnableBudgetaryControlFlag | ENABLE_BUDGETARY_CONTROL_FLAG | — | ✅ |
| 50 | LedgerEnableJeApprovalFlag | ENABLE_JE_APPROVAL_FLAG | — | ✅ |
| 51 | LedgerEnableReconciliationFlag | ENABLE_RECONCILIATION_FLAG | — | ✅ |
| 52 | LedgerEnableRevalSsTrackFlag | ENABLE_REVAL_SS_TRACK_FLAG | — | ✅ |
| 53 | LedgerEnfSeqDateCorrelationCode | ENF_SEQ_DATE_CORRELATION_CODE | — | ✅ |
| 54 | LedgerFirstLedgerPeriodName | FIRST_LEDGER_PERIOD_NAME | — | ✅ |
| 55 | LedgerFutureEnterablePeriodsLimit | FUTURE_ENTERABLE_PERIODS_LIMIT | — | ✅ |
| 56 | LedgerImplicitAccessSetId | IMPLICIT_ACCESS_SET_ID | — | ✅ |
| 57 | LedgerIntercoGainLossCcid | INTERCO_GAIN_LOSS_CCID | — | ✅ |
| 58 | LedgerJrnlsGroupByDateFlag | JRNLS_GROUP_BY_DATE_FLAG | — | ✅ |
| 59 | LedgerLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 60 | LedgerLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 61 | LedgerLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 62 | LedgerLatestEncumbranceYear | LATEST_ENCUMBRANCE_YEAR | — | ✅ |
| 63 | LedgerLatestOpenedPeriodName | LATEST_OPENED_PERIOD_NAME | — | ✅ |
| 64 | LedgerLedgerCategoryCode | LEDGER_CATEGORY_CODE | — | ✅ |
| 65 | LedgerLedgerId | LEDGER_ID | 🔑 | ✅ |
| 66 | LedgerMinimumThresholdAmount | MINIMUM_THRESHOLD_AMOUNT | — | ✅ |
| 67 | LedgerName | NAME | — | ✅ |
| 68 | LedgerNetClosingBalFlag | NET_CLOSING_BAL_FLAG | — | ✅ |
| 69 | LedgerNetIncomeCodeCombinationId | NET_INCOME_CODE_COMBINATION_ID | — | ✅ |
| 70 | LedgerObjectTypeCode | OBJECT_TYPE_CODE | — | ✅ |
| 71 | LedgerObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 72 | LedgerPeriodAverageRateType | PERIOD_AVERAGE_RATE_TYPE | — | ✅ |
| 73 | LedgerPeriodEndRateType | PERIOD_END_RATE_TYPE | — | ✅ |
| 74 | LedgerPeriodSetName | PERIOD_SET_NAME | — | ✅ |
| 75 | LedgerPopUpStatAccountFlag | POP_UP_STAT_ACCOUNT_FLAG | — | ✅ |
| 76 | LedgerPriorPrdNotificationFlag | PRIOR_PRD_NOTIFICATION_FLAG | — | ✅ |
| 77 | LedgerRequireBudgetJournalsFlag | REQUIRE_BUDGET_JOURNALS_FLAG | — | ✅ |
| 78 | LedgerResEncumbCodeCombinationId | RES_ENCUMB_CODE_COMBINATION_ID | — | ✅ |
| 79 | LedgerRetEarnCodeCombinationId | RET_EARN_CODE_COMBINATION_ID | — | ✅ |
| 80 | LedgerRevalFromPriLgrCurr | REVAL_FROM_PRI_LGR_CURR | — | ✅ |
| 81 | LedgerRoundingCodeCombinationId | ROUNDING_CODE_COMBINATION_ID | — | ✅ |
| 82 | LedgerSequencingModeCode | SEQUENCING_MODE_CODE | — | ✅ |
| 83 | LedgerShortName | SHORT_NAME | — | ✅ |
| 84 | LedgerSlaAccountingMethodCode | SLA_ACCOUNTING_METHOD_CODE | — | ✅ |
| 85 | LedgerSlaAccountingMethodType | SLA_ACCOUNTING_METHOD_TYPE | — | ✅ |
| 86 | LedgerSlaBalByLedgerCurrFlag | SLA_BAL_BY_LEDGER_CURR_FLAG | — | ✅ |
| 87 | LedgerSlaDescriptionLanguage | SLA_DESCRIPTION_LANGUAGE | — | ✅ |
| 88 | LedgerSlaEnteredCurBalSusCcid | SLA_ENTERED_CUR_BAL_SUS_CCID | — | ✅ |
| 89 | LedgerSlaLedgerCashBasisFlag | SLA_LEDGER_CASH_BASIS_FLAG | — | ✅ |
| 90 | LedgerSlaLedgerCurBalSusCcid | SLA_LEDGER_CUR_BAL_SUS_CCID | — | ✅ |
| 91 | LedgerSlaSequencingFlag | SLA_SEQUENCING_FLAG | — | ✅ |
| 92 | LedgerSuspenseAllowedFlag | SUSPENSE_ALLOWED_FLAG | — | ✅ |
| 93 | LedgerThresholdAmount | THRESHOLD_AMOUNT | — | ✅ |
| 94 | LedgerTrackRoundingImbalanceFlag | TRACK_ROUNDING_IMBALANCE_FLAG | — | ✅ |
| 95 | LedgerTransactionCalendarId | TRANSACTION_CALENDAR_ID | — | ✅ |
| 96 | LedgerTranslateEodFlag | TRANSLATE_EOD_FLAG | — | ✅ |
| 97 | LedgerTranslateQatdFlag | TRANSLATE_QATD_FLAG | — | ✅ |
| 98 | LedgerTranslateYatdFlag | TRANSLATE_YATD_FLAG | — | ✅ |
| 99 | LedgerValidateJournalRefDate | VALIDATE_JOURNAL_REF_DATE | — | ✅ |

### [[xla_acctg_methods_tl|XLA_ACCTG_METHODS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcctgMethodTLAccountingMethodCode | ACCOUNTING_METHOD_CODE | — | — |
| 2 | AcctgMethodTLAccountingMethodTypeCode | ACCOUNTING_METHOD_TYPE_CODE | — | — |
| 3 | AcctgMethodTLDescription | DESCRIPTION | — | — |
| 4 | AcctgMethodTLLanguage | LANGUAGE | — | — |
| 5 | AcctgMethodTLName | NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
