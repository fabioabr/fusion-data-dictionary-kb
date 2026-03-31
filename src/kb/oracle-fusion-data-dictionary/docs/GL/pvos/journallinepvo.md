---
id: DOC-GL-PVO-JournalLinePVO
doc_type: system-doc
title: "JournalLinePVO — PVO General Ledger"
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
  - JournalLinePVO
  - journallinepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JournalLinePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Journal Line. Acessa as tabelas: FND_DOCUMENT_SEQUENCES, FUN_SEQ_VERSIONS, GL_CALENDARS (+12).

**Caminho:** `FscmTopModelAM.FinGlJrnlEntriesAM.JournalLinePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 419 | 15 | 2 | 122 | 29% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]] — 12 atributos (3 BICC)
- [[fun_seq_versions|FUN_SEQ_VERSIONS]] — 18 atributos (4 BICC)
- [[gl_calendars|GL_CALENDARS]] — 21 atributos
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 27 atributos (1 BICC)
- [[gl_encumbrance_types_vl|GL_ENCUMBRANCE_TYPES_VL]] — 2 atributos (2 BICC)
- [[gl_je_batches|GL_JE_BATCHES]] — 37 atributos (20 BICC)
- [[gl_je_headers|GL_JE_HEADERS]] — 68 atributos (38 BICC)
- [[gl_je_lines|GL_JE_LINES]] — 59 atributos (2 PKs, 34 BICC)
- [[gl_je_lines_recon|GL_JE_LINES_RECON]] — 6 atributos (4 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 8 atributos
- [[gl_period_statuses|GL_PERIOD_STATUSES]] — 25 atributos (5 BICC)
- [[gl_reconciliation_rules|GL_RECONCILIATION_RULES]] — 2 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 73 atributos (7 BICC)
- [[per_users|PER_USERS]] — 58 atributos (2 BICC)
- [[xle_entity_profiles|XLE_ENTITY_PROFILES]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocSequenceDbSequenceName | DB_SEQUENCE_NAME | — | ✅ |
| 2 | DocSequenceDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 3 | DocSequenceName | NAME | — | ✅ |
| 4 | DocSequenceType | TYPE | — | — |
| 5 | LocalDocSequenceDbSequenceName | DB_SEQUENCE_NAME | — | — |
| 6 | LocalDocSequenceDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 7 | LocalDocSequenceName | NAME | — | ✅ |
| 8 | LocalDocSequenceType | TYPE | — | — |
| 9 | SlaDocSequenceDbSequenceName | DB_SEQUENCE_NAME | — | — |
| 10 | SlaDocSequenceDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 11 | SlaDocSequenceName | NAME | — | — |
| 12 | SlaDocSequenceType | TYPE | — | — |

### [[fun_seq_versions|FUN_SEQ_VERSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FunCloseAcctSeqVersionsCurrentValue | CURRENT_VALUE | — | — |
| 2 | FunCloseAcctSeqVersionsEndDate | END_DATE | — | — |
| 3 | FunCloseAcctSeqVersionsHeaderName | HEADER_NAME | — | ✅ |
| 4 | FunCloseAcctSeqVersionsId | SEQ_VERSION_ID | — | — |
| 5 | FunCloseAcctSeqVersionsInitialValue | INITIAL_VALUE | — | — |
| 6 | FunCloseAcctSeqVersionsName | VERSION_NAME | — | ✅ |
| 7 | FunCloseAcctSeqVersionsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | FunCloseAcctSeqVersionsStartDate | START_DATE | — | — |
| 9 | FunCloseAcctSeqVersionsUseStatusCode | USE_STATUS_CODE | — | — |
| 10 | FunPostAcctSeqVersionsCurrentValue | CURRENT_VALUE | — | — |
| 11 | FunPostAcctSeqVersionsEndDate | END_DATE | — | — |
| 12 | FunPostAcctSeqVersionsHeaderName | HEADER_NAME | — | ✅ |
| 13 | FunPostAcctSeqVersionsId | SEQ_VERSION_ID | — | — |
| 14 | FunPostAcctSeqVersionsInitialValue | INITIAL_VALUE | — | — |
| 15 | FunPostAcctSeqVersionsName | VERSION_NAME | — | ✅ |
| 16 | FunPostAcctSeqVersionsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | FunPostAcctSeqVersionsStartDate | START_DATE | — | — |
| 18 | FunPostAcctSeqVersionsUseStatusCode | USE_STATUS_CODE | — | — |

### [[gl_calendars|GL_CALENDARS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CalendarAdjPeriodFreqCode | ADJ_PERIOD_FREQ_CODE | — | — |
| 2 | CalendarAdjPeriodsNum | ADJ_PERIODS_NUM | — | — |
| 3 | CalendarCalendarId | CALENDAR_ID | — | — |
| 4 | CalendarCalendarStartDate | CALENDAR_START_DATE | — | — |
| 5 | CalendarCalendarTypeCode | CALENDAR_TYPE_CODE | — | — |
| 6 | CalendarDescription | DESCRIPTION | — | — |
| 7 | CalendarLatestYearStartDate | LATEST_YEAR_START_DATE | — | — |
| 8 | CalendarLegacyCalendarFlag | LEGACY_CALENDAR_FLAG | — | — |
| 9 | CalendarLegacyRulesEnabledFlag | LEGACY_RULES_ENABLED_FLAG | — | — |
| 10 | CalendarNonAdjPeriodFreqCode | NON_ADJ_PERIOD_FREQ_CODE | — | — |
| 11 | CalendarNonAdjPeriodsNum | NON_ADJ_PERIODS_NUM | — | — |
| 12 | CalendarObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | CalendarPeriodNameFormatCode | PERIOD_NAME_FORMAT_CODE | — | — |
| 14 | CalendarPeriodNameSeparatorCode | PERIOD_NAME_SEPARATOR_CODE | — | — |
| 15 | CalendarPeriodSetId | PERIOD_SET_ID | — | — |
| 16 | CalendarPeriodSetName | PERIOD_SET_NAME | — | — |
| 17 | CalendarPeriodType | PERIOD_TYPE | — | — |
| 18 | CalendarPeriodTypeId | PERIOD_TYPE_ID | — | — |
| 19 | CalendarSecurityFlag | SECURITY_FLAG | — | — |
| 20 | CalendarUserPeriodNamePrefix | USER_PERIOD_NAME_PREFIX | — | — |
| 21 | CalendarUserPeriodSetName | USER_PERIOD_SET_NAME | — | — |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConversionTypeConversionType | CONVERSION_TYPE | — | — |
| 2 | ConversionTypeDescription | DESCRIPTION | — | — |
| 3 | ConversionTypeEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 4 | ConversionTypeEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 5 | ConversionTypeFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 6 | ConversionTypeFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 7 | ConversionTypeFemScenario | FEM_SCENARIO | — | — |
| 8 | ConversionTypeFemTimeframe | FEM_TIMEFRAME | — | — |
| 9 | ConversionTypeLineConversionType | CONVERSION_TYPE | — | — |
| 10 | ConversionTypeLineDescription | DESCRIPTION | — | — |
| 11 | ConversionTypeLineEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 12 | ConversionTypeLineEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 13 | ConversionTypeLineFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 14 | ConversionTypeLineFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 15 | ConversionTypeLineFemScenario | FEM_SCENARIO | — | — |
| 16 | ConversionTypeLineFemTimeframe | FEM_TIMEFRAME | — | — |
| 17 | ConversionTypeLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | ConversionTypeLinePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 19 | ConversionTypeLineSecurityFlag | SECURITY_FLAG | — | — |
| 20 | ConversionTypeLineUserConversionType | USER_CONVERSION_TYPE | — | ✅ |
| 21 | ConversionTypeLineUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |
| 22 | ConversionTypePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 23 | ConversionTypeSecurityFlag | SECURITY_FLAG | — | — |
| 24 | ConversionTypeUserConversionType | USER_CONVERSION_TYPE | — | — |
| 25 | ConversionTypeUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |
| 26 | CreatedByPersonNameObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 27 | LastUpdatedByPersonNameObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |

### [[gl_encumbrance_types_vl|GL_ENCUMBRANCE_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JournalEncumbranceTypeEncumbranceType | ENCUMBRANCE_TYPE | — | ✅ |
| 2 | JournalEncumbranceTypeEncumbranceTypeId | ENCUMBRANCE_TYPE_ID | — | ✅ |

### [[gl_je_batches|GL_JE_BATCHES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JrnlBatchAccountedPeriodType | ACCOUNTED_PERIOD_TYPE | — | ✅ |
| 2 | JrnlBatchActualFlag | ACTUAL_FLAG | — | ✅ |
| 3 | JrnlBatchApprovalStatusCode | APPROVAL_STATUS_CODE | — | ✅ |
| 4 | JrnlBatchApproverEmployeeId | APPROVER_EMPLOYEE_ID | — | — |
| 5 | JrnlBatchAverageJournalFlag | AVERAGE_JOURNAL_FLAG | — | — |
| 6 | JrnlBatchBudgetaryControlStatus | BUDGETARY_CONTROL_STATUS | — | — |
| 7 | JrnlBatchChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | ✅ |
| 8 | JrnlBatchControlTotal | CONTROL_TOTAL | — | ✅ |
| 9 | JrnlBatchCreatedBy | CREATED_BY | — | ✅ |
| 10 | JrnlBatchCreationDate | CREATION_DATE | — | ✅ |
| 11 | JrnlBatchDateCreated | DATE_CREATED | — | — |
| 12 | JrnlBatchDefaultEffectiveDate | DEFAULT_EFFECTIVE_DATE | — | ✅ |
| 13 | JrnlBatchDefaultPeriodName | DEFAULT_PERIOD_NAME | — | — |
| 14 | JrnlBatchDescription | DESCRIPTION | — | ✅ |
| 15 | JrnlBatchEarliestPostableDate | EARLIEST_POSTABLE_DATE | — | — |
| 16 | JrnlBatchGroupId | GROUP_ID | — | ✅ |
| 17 | JrnlBatchJeBatchId | JE_BATCH_ID | — | ✅ |
| 18 | JrnlBatchJeSource | JE_SOURCE | — | — |
| 19 | JrnlBatchLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | JrnlBatchLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | JrnlBatchLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 22 | JrnlBatchName | NAME | — | ✅ |
| 23 | JrnlBatchObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 24 | JrnlBatchPacketId | PACKET_ID | — | — |
| 25 | JrnlBatchParentJeBatchId | PARENT_JE_BATCH_ID | — | — |
| 26 | JrnlBatchPeriodSetName | PERIOD_SET_NAME | — | ✅ |
| 27 | JrnlBatchPostedDate | POSTED_DATE | — | ✅ |
| 28 | JrnlBatchPostedDateTime | POSTED_DATE | — | — |
| 29 | JrnlBatchPostingRunId | POSTING_RUN_ID | — | — |
| 30 | JrnlBatchRequestId | REQUEST_ID | — | — |
| 31 | JrnlBatchRunningTotalAccountedCr | RUNNING_TOTAL_ACCOUNTED_CR | — | ✅ |
| 32 | JrnlBatchRunningTotalAccountedDr | RUNNING_TOTAL_ACCOUNTED_DR | — | ✅ |
| 33 | JrnlBatchRunningTotalCr | RUNNING_TOTAL_CR | — | ✅ |
| 34 | JrnlBatchRunningTotalDr | RUNNING_TOTAL_DR | — | ✅ |
| 35 | JrnlBatchStatus | STATUS | — | — |
| 36 | JrnlBatchStatusVerified | STATUS_VERIFIED | — | — |
| 37 | JrnlBatchUnreservationPacketId | UNRESERVATION_PACKET_ID | — | — |

### [[gl_je_headers|GL_JE_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JrnlHdrAccrualRevChangeSignFlagCode | ACCRUAL_REV_CHANGE_SIGN_FLAG | — | ✅ |
| 2 | JrnlHdrAccrualRevEffectiveDate | ACCRUAL_REV_EFFECTIVE_DATE | — | — |
| 3 | JrnlHdrAccrualRevFlag | ACCRUAL_REV_FLAG | — | ✅ |
| 4 | JrnlHdrAccrualRevJeHeaderId | ACCRUAL_REV_JE_HEADER_ID | — | — |
| 5 | JrnlHdrAccrualRevPeriodName | ACCRUAL_REV_PERIOD_NAME | — | ✅ |
| 6 | JrnlHdrAccrualRevStatus | ACCRUAL_REV_STATUS | — | ✅ |
| 7 | JrnlHdrActualFlag | ACTUAL_FLAG | — | ✅ |
| 8 | JrnlHdrBalancedJeFlag | BALANCED_JE_FLAG | — | — |
| 9 | JrnlHdrBalancingSegmentValue | BALANCING_SEGMENT_VALUE | — | ✅ |
| 10 | JrnlHdrBudgetVersionId | BUDGET_VERSION_ID | — | — |
| 11 | JrnlHdrCloseAcctSeqAssignId | CLOSE_ACCT_SEQ_ASSIGN_ID | — | — |
| 12 | JrnlHdrCloseAcctSeqValue | CLOSE_ACCT_SEQ_VALUE | — | ✅ |
| 13 | JrnlHdrCloseAcctSeqVersionId | CLOSE_ACCT_SEQ_VERSION_ID | — | — |
| 14 | JrnlHdrControlTotal | CONTROL_TOTAL | — | — |
| 15 | JrnlHdrConversionFlag | CONVERSION_FLAG | — | ✅ |
| 16 | JrnlHdrCrBalSegValue | CR_BAL_SEG_VALUE | — | ✅ |
| 17 | JrnlHdrCreatedBy | CREATED_BY | — | ✅ |
| 18 | JrnlHdrCreationDate | CREATION_DATE | — | — |
| 19 | JrnlHdrCurrencyCode | CURRENCY_CODE | — | ✅ |
| 20 | JrnlHdrCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 21 | JrnlHdrCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 22 | JrnlHdrCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 23 | JrnlHdrDateCreated | DATE_CREATED | — | ✅ |
| 24 | JrnlHdrDefaultEffectiveDate | DEFAULT_EFFECTIVE_DATE | — | ✅ |
| 25 | JrnlHdrDescription | DESCRIPTION | — | ✅ |
| 26 | JrnlHdrDisplayAlcJournalFlag | DISPLAY_ALC_JOURNAL_FLAG | — | — |
| 27 | JrnlHdrDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 28 | JrnlHdrDocSequenceValue | DOC_SEQUENCE_VALUE | — | ✅ |
| 29 | JrnlHdrDrBalSegValue | DR_BAL_SEG_VALUE | — | ✅ |
| 30 | JrnlHdrEarliestPostableDate | EARLIEST_POSTABLE_DATE | — | — |
| 31 | JrnlHdrEncumbranceTypeId | ENCUMBRANCE_TYPE_ID | — | — |
| 32 | JrnlHdrExternalReference | EXTERNAL_REFERENCE | — | ✅ |
| 33 | JrnlHdrFromRecurringHeaderId | FROM_RECURRING_HEADER_ID | — | — |
| 34 | JrnlHdrIntercompanyMode | INTERCOMPANY_MODE | — | — |
| 35 | JrnlHdrJeBatchId | JE_BATCH_ID | — | — |
| 36 | JrnlHdrJeCategory | JE_CATEGORY | — | ✅ |
| 37 | JrnlHdrJeFromSlaFlag | JE_FROM_SLA_FLAG | — | ✅ |
| 38 | JrnlHdrJeHeaderId | JE_HEADER_ID | — | — |
| 39 | JrnlHdrJeSource | JE_SOURCE | — | ✅ |
| 40 | JrnlHdrLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 41 | JrnlHdrLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 42 | JrnlHdrLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 43 | JrnlHdrLedgerId | LEDGER_ID | — | ✅ |
| 44 | JrnlHdrLocalDocSequenceId | LOCAL_DOC_SEQUENCE_ID | — | — |
| 45 | JrnlHdrLocalDocSequenceValue | LOCAL_DOC_SEQUENCE_VALUE | — | ✅ |
| 46 | JrnlHdrMultiBalSegFlag | MULTI_BAL_SEG_FLAG | — | — |
| 47 | JrnlHdrMultiCurrencyFlag | MULTI_CURRENCY_FLAG | — | ✅ |
| 48 | JrnlHdrName | NAME | — | ✅ |
| 49 | JrnlHdrObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 50 | JrnlHdrOriginatingBalSegValue | ORIGINATING_BAL_SEG_VALUE | — | ✅ |
| 51 | JrnlHdrParentJeHeaderId | PARENT_JE_HEADER_ID | — | ✅ |
| 52 | JrnlHdrPeriodName | PERIOD_NAME | — | ✅ |
| 53 | JrnlHdrPostMultiCurrencyFlag | POST_MULTI_CURRENCY_FLAG | — | ✅ |
| 54 | JrnlHdrPostedDate | POSTED_DATE | — | ✅ |
| 55 | JrnlHdrPostedDateTime | POSTED_DATE | — | — |
| 56 | JrnlHdrPostingAcctSeqAssignId | POSTING_ACCT_SEQ_ASSIGN_ID | — | — |
| 57 | JrnlHdrPostingAcctSeqValue | POSTING_ACCT_SEQ_VALUE | — | ✅ |
| 58 | JrnlHdrPostingAcctSeqVersionId | POSTING_ACCT_SEQ_VERSION_ID | — | — |
| 59 | JrnlHdrReferenceDate | REFERENCE_DATE | — | ✅ |
| 60 | JrnlHdrReversedJeHeaderId | REVERSED_JE_HEADER_ID | — | ✅ |
| 61 | JrnlHdrRunningTotalAccountedCr | RUNNING_TOTAL_ACCOUNTED_CR | — | — |
| 62 | JrnlHdrRunningTotalAccountedDr | RUNNING_TOTAL_ACCOUNTED_DR | — | — |
| 63 | JrnlHdrRunningTotalCr | RUNNING_TOTAL_CR | — | — |
| 64 | JrnlHdrRunningTotalDr | RUNNING_TOTAL_DR | — | — |
| 65 | JrnlHdrStatus | STATUS | — | ✅ |
| 66 | JrnlHdrTaxLegalEntityId | TAX_LEGAL_ENTITY_ID | — | — |
| 67 | JrnlHdrTaxStatusCode | TAX_STATUS_CODE | — | — |
| 68 | JrnlHdrUssglTransactionCode | USSGL_TRANSACTION_CODE | — | — |

### [[gl_je_lines|GL_JE_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JeHeaderId | JE_HEADER_ID | 🔑 | ✅ |
| 2 | JeLineNum | JE_LINE_NUM | 🔑 | ✅ |
| 3 | JrnlLineAccountedCr | ACCOUNTED_CR | — | ✅ |
| 4 | JrnlLineAccountedDr | ACCOUNTED_DR | — | ✅ |
| 5 | JrnlLineAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 6 | JrnlLineCoProcessedFlag | CO_PROCESSED_FLAG | — | — |
| 7 | JrnlLineCoThirdParty | CO_THIRD_PARTY | — | — |
| 8 | JrnlLineCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 9 | JrnlLineCreatedBy | CREATED_BY | — | ✅ |
| 10 | JrnlLineCreationDate | CREATION_DATE | — | ✅ |
| 11 | JrnlLineCurrencyCode | CURRENCY_CODE | — | ✅ |
| 12 | JrnlLineCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 13 | JrnlLineCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 14 | JrnlLineCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 15 | JrnlLineDescription | DESCRIPTION | — | ✅ |
| 16 | JrnlLineEffectiveDate | EFFECTIVE_DATE | — | ✅ |
| 17 | JrnlLineEnteredCr | ENTERED_CR | — | ✅ |
| 18 | JrnlLineEnteredDr | ENTERED_DR | — | ✅ |
| 19 | JrnlLineGlSlLinkId | GL_SL_LINK_ID | — | ✅ |
| 20 | JrnlLineGlSlLinkTable | GL_SL_LINK_TABLE | — | — |
| 21 | JrnlLineIgnoreRateFlag | IGNORE_RATE_FLAG | — | — |
| 22 | JrnlLineInvoiceAmount | INVOICE_AMOUNT | — | — |
| 23 | JrnlLineInvoiceDate | INVOICE_DATE | — | — |
| 24 | JrnlLineInvoiceIdentifier | INVOICE_IDENTIFIER | — | — |
| 25 | JrnlLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | JrnlLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 27 | JrnlLineLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 28 | JrnlLineLedgerId | LEDGER_ID | — | ✅ |
| 29 | JrnlLineLineTypeCode | LINE_TYPE_CODE | — | ✅ |
| 30 | JrnlLineNo1 | NO1 | — | — |
| 31 | JrnlLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 32 | JrnlLinePeriodName | PERIOD_NAME | — | ✅ |
| 33 | JrnlLineReference1 | REFERENCE_1 | — | ✅ |
| 34 | JrnlLineReference10 | REFERENCE_10 | — | ✅ |
| 35 | JrnlLineReference2 | REFERENCE_2 | — | ✅ |
| 36 | JrnlLineReference3 | REFERENCE_3 | — | ✅ |
| 37 | JrnlLineReference4 | REFERENCE_4 | — | ✅ |
| 38 | JrnlLineReference5 | REFERENCE_5 | — | ✅ |
| 39 | JrnlLineReference6 | REFERENCE_6 | — | ✅ |
| 40 | JrnlLineReference7 | REFERENCE_7 | — | ✅ |
| 41 | JrnlLineReference8 | REFERENCE_8 | — | ✅ |
| 42 | JrnlLineReference9 | REFERENCE_9 | — | ✅ |
| 43 | JrnlLineStatAmount | STAT_AMOUNT | — | ✅ |
| 44 | JrnlLineStatus | STATUS | — | ✅ |
| 45 | JrnlLineSubledgerDocSequenceId | SUBLEDGER_DOC_SEQUENCE_ID | — | — |
| 46 | JrnlLineSubledgerDocSequenceValue | SUBLEDGER_DOC_SEQUENCE_VALUE | — | ✅ |
| 47 | JrnlLineTaxCode | TAX_CODE | — | — |
| 48 | JrnlLineTaxCodeId | TAX_CODE_ID | — | — |
| 49 | JrnlLineTaxCustomerName | TAX_CUSTOMER_NAME | — | — |
| 50 | JrnlLineTaxCustomerReference | TAX_CUSTOMER_REFERENCE | — | — |
| 51 | JrnlLineTaxDocumentDate | TAX_DOCUMENT_DATE | — | — |
| 52 | JrnlLineTaxDocumentIdentifier | TAX_DOCUMENT_IDENTIFIER | — | — |
| 53 | JrnlLineTaxGroupId | TAX_GROUP_ID | — | — |
| 54 | JrnlLineTaxLineFlag | TAX_LINE_FLAG | — | — |
| 55 | JrnlLineTaxRegistrationNumber | TAX_REGISTRATION_NUMBER | — | — |
| 56 | JrnlLineTaxRoundingRuleCode | TAX_ROUNDING_RULE_CODE | — | — |
| 57 | JrnlLineTaxTypeCode | TAX_TYPE_CODE | — | — |
| 58 | JrnlLineTaxableLineFlag | TAXABLE_LINE_FLAG | — | — |
| 59 | JrnlLineUssglTransactionCode | USSGL_TRANSACTION_CODE | — | — |

### [[gl_je_lines_recon|GL_JE_LINES_RECON]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JrnlReconLineJeHeaderId | JE_HEADER_ID | — | — |
| 2 | JrnlReconLineJeLineNum | JE_LINE_NUM | — | — |
| 3 | JrnlReconLineJgzzReconDate | JGZZ_RECON_DATE | — | ✅ |
| 4 | JrnlReconLineJgzzReconId | JGZZ_RECON_ID | — | ✅ |
| 5 | JrnlReconLineJgzzReconRef | JGZZ_RECON_REF | — | ✅ |
| 6 | JrnlReconLineJgzzReconStatus | JGZZ_RECON_STATUS | — | ✅ |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgerChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 2 | LedgerCurrencyCode | CURRENCY_CODE | — | — |
| 3 | LedgerDescription | DESCRIPTION | — | — |
| 4 | LedgerLedgerId | LEDGER_ID | — | — |
| 5 | LedgerName | NAME | — | — |
| 6 | LedgerObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | LedgerPeriodSetName | PERIOD_SET_NAME | — | — |
| 8 | LedgerShortName | SHORT_NAME | — | — |

### [[gl_period_statuses|GL_PERIOD_STATUSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PeriodStatusAdjustmentPeriodFlag | ADJUSTMENT_PERIOD_FLAG | — | ✅ |
| 2 | PeriodStatusApplicationId | APPLICATION_ID | — | ✅ |
| 3 | PeriodStatusChronologicalSeqStatusCode | CHRONOLOGICAL_SEQ_STATUS_CODE | — | — |
| 4 | PeriodStatusClosingStatus | CLOSING_STATUS | — | — |
| 5 | PeriodStatusCreatedBy | CREATED_BY | — | — |
| 6 | PeriodStatusCreationDate | CREATION_DATE | — | — |
| 7 | PeriodStatusEffectivePeriodNum | EFFECTIVE_PERIOD_NUM | — | — |
| 8 | PeriodStatusEliminationConfirmedFlag | ELIMINATION_CONFIRMED_FLAG | — | — |
| 9 | PeriodStatusEndDate | END_DATE | — | ✅ |
| 10 | PeriodStatusLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | PeriodStatusLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | PeriodStatusLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | PeriodStatusLedgerId | LEDGER_ID | — | — |
| 14 | PeriodStatusMigrationStatusCode | MIGRATION_STATUS_CODE | — | — |
| 15 | PeriodStatusObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | PeriodStatusPeriodName | PERIOD_NAME | — | — |
| 17 | PeriodStatusPeriodNum | PERIOD_NUM | — | — |
| 18 | PeriodStatusPeriodType | PERIOD_TYPE | — | — |
| 19 | PeriodStatusPeriodYear | PERIOD_YEAR | — | — |
| 20 | PeriodStatusQuarterNum | QUARTER_NUM | — | — |
| 21 | PeriodStatusQuarterStartDate | QUARTER_START_DATE | — | — |
| 22 | PeriodStatusSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 23 | PeriodStatusStartDate | START_DATE | — | ✅ |
| 24 | PeriodStatusTrackBcYtdFlag | TRACK_BC_YTD_FLAG | — | — |
| 25 | PeriodStatusYearStartDate | YEAR_START_DATE | — | — |

### [[gl_reconciliation_rules|GL_RECONCILIATION_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlReconciliationRulesPEOReconRuleId | RECON_RULE_ID | — | — |
| 2 | GlReconciliationRulesPEOReconRuleName | RECON_RULE_NAME | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BatchApprovedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | BatchApprovedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | BatchApprovedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | BatchApprovedByPersonId | PERSON_ID | — | — |
| 5 | BatchApprovedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | BatchCreatedByPersonNameCreationDate | CREATION_DATE | — | — |
| 7 | BatchCreatedByPersonNameEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | BatchCreatedByPersonNameEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | BatchCreatedByPersonNameLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 10 | BatchCreatedByPersonNamePersonId | PERSON_ID | — | — |
| 11 | BatchCreatedByPersonNamePersonNameDisplayName | DISPLAY_NAME | — | — |
| 12 | BatchCreatedByPersonNamePersonNameId | PERSON_NAME_ID | — | — |
| 13 | BatchLastUpdatedByPersonNameCreationDate | CREATION_DATE | — | — |
| 14 | BatchLastUpdatedByPersonNameEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 15 | BatchLastUpdatedByPersonNameEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 16 | BatchLastUpdatedByPersonNameLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 17 | BatchLastUpdatedByPersonNamePersonId | PERSON_ID | — | — |
| 18 | BatchLastUpdatedByPersonNamePersonNameDisplayName | DISPLAY_NAME | — | — |
| 19 | BatchLastUpdatedByPersonNamePersonNameId | PERSON_NAME_ID | — | — |
| 20 | CreatedByPersonNameBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 21 | CreatedByPersonNameCreatedBy | CREATED_BY | — | — |
| 22 | CreatedByPersonNameCreationDate | CREATION_DATE | — | — |
| 23 | CreatedByPersonNameDisplayName | DISPLAY_NAME | — | ✅ |
| 24 | CreatedByPersonNameEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 25 | CreatedByPersonNameEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 26 | CreatedByPersonNameFirstName | FIRST_NAME | — | — |
| 27 | CreatedByPersonNameFullName | FULL_NAME | — | — |
| 28 | CreatedByPersonNameHonors | HONORS | — | — |
| 29 | CreatedByPersonNameKnownAs | KNOWN_AS | — | — |
| 30 | CreatedByPersonNameLastName | LAST_NAME | — | — |
| 31 | CreatedByPersonNameLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | CreatedByPersonNameLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | CreatedByPersonNameLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 34 | CreatedByPersonNameLegislationCode | LEGISLATION_CODE | — | — |
| 35 | CreatedByPersonNameListName | LIST_NAME | — | — |
| 36 | CreatedByPersonNameMiddleNames | MIDDLE_NAMES | — | — |
| 37 | CreatedByPersonNameMilitaryRank | MILITARY_RANK | — | — |
| 38 | CreatedByPersonNameNameType | NAME_TYPE | — | — |
| 39 | CreatedByPersonNameObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 40 | CreatedByPersonNameOrderName | ORDER_NAME | — | — |
| 41 | CreatedByPersonNamePersonId | PERSON_ID | — | — |
| 42 | CreatedByPersonNamePersonNameId | PERSON_NAME_ID | — | — |
| 43 | CreatedByPersonNamePreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 44 | CreatedByPersonNamePreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 45 | CreatedByPersonNameSuffix | SUFFIX | — | — |
| 46 | CreatedByPersonNameTitle | TITLE | — | — |
| 47 | LastUpdatedByPersonNameBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 48 | LastUpdatedByPersonNameCreatedBy | CREATED_BY | — | — |
| 49 | LastUpdatedByPersonNameCreationDate | CREATION_DATE | — | — |
| 50 | LastUpdatedByPersonNameDisplayName | DISPLAY_NAME | — | ✅ |
| 51 | LastUpdatedByPersonNameEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 52 | LastUpdatedByPersonNameEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 53 | LastUpdatedByPersonNameFirstName | FIRST_NAME | — | — |
| 54 | LastUpdatedByPersonNameFullName | FULL_NAME | — | — |
| 55 | LastUpdatedByPersonNameHonors | HONORS | — | — |
| 56 | LastUpdatedByPersonNameKnownAs | KNOWN_AS | — | — |
| 57 | LastUpdatedByPersonNameLastName | LAST_NAME | — | — |
| 58 | LastUpdatedByPersonNameLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 59 | LastUpdatedByPersonNameLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 60 | LastUpdatedByPersonNameLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 61 | LastUpdatedByPersonNameLegislationCode | LEGISLATION_CODE | — | — |
| 62 | LastUpdatedByPersonNameListName | LIST_NAME | — | — |
| 63 | LastUpdatedByPersonNameMiddleNames | MIDDLE_NAMES | — | — |
| 64 | LastUpdatedByPersonNameMilitaryRank | MILITARY_RANK | — | — |
| 65 | LastUpdatedByPersonNameNameType | NAME_TYPE | — | — |
| 66 | LastUpdatedByPersonNameObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 67 | LastUpdatedByPersonNameOrderName | ORDER_NAME | — | — |
| 68 | LastUpdatedByPersonNamePersonId | PERSON_ID | — | — |
| 69 | LastUpdatedByPersonNamePersonNameId | PERSON_NAME_ID | — | — |
| 70 | LastUpdatedByPersonNamePreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 71 | LastUpdatedByPersonNamePreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 72 | LastUpdatedByPersonNameSuffix | SUFFIX | — | — |
| 73 | LastUpdatedByPersonNameTitle | TITLE | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BatchCreatedByUserCreatedBy | CREATED_BY | — | — |
| 2 | BatchCreatedByUserCreationDate | CREATION_DATE | — | — |
| 3 | BatchCreatedByUserLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 4 | BatchCreatedByUserLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | BatchCreatedByUserLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | BatchCreatedByUserObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | BatchCreatedByUserUserId | USER_ID | — | — |
| 8 | BatchCreatedByUserUsername | USERNAME | — | — |
| 9 | BatchLastUpdatedByUserCreatedBy | CREATED_BY | — | — |
| 10 | BatchLastUpdatedByUserCreationDate | CREATION_DATE | — | — |
| 11 | BatchLastUpdatedByUserLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 12 | BatchLastUpdatedByUserLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | BatchLastUpdatedByUserLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | BatchLastUpdatedByUserObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | BatchLastUpdatedByUserUserId | USER_ID | — | — |
| 16 | BatchLastUpdatedByUserUsername | USERNAME | — | — |
| 17 | CreatedByUserActiveFlag | ACTIVE_FLAG | — | — |
| 18 | CreatedByUserBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 19 | CreatedByUserCreatedBy | CREATED_BY | — | — |
| 20 | CreatedByUserCreationDate | CREATION_DATE | — | — |
| 21 | CreatedByUserCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 22 | CreatedByUserEndDate | END_DATE | — | — |
| 23 | CreatedByUserHrTerminated | HR_TERMINATED | — | — |
| 24 | CreatedByUserLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 25 | CreatedByUserLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 26 | CreatedByUserLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 27 | CreatedByUserMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 28 | CreatedByUserObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 29 | CreatedByUserPartyId | PARTY_ID | — | — |
| 30 | CreatedByUserPersonId | PERSON_ID | — | — |
| 31 | CreatedByUserStartDate | START_DATE | — | — |
| 32 | CreatedByUserSuspended | SUSPENDED | — | — |
| 33 | CreatedByUserUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 34 | CreatedByUserUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 35 | CreatedByUserUserGuid | USER_GUID | — | — |
| 36 | CreatedByUserUserId | USER_ID | — | — |
| 37 | CreatedByUserUsername | USERNAME | — | — |
| 38 | LastUpdatedByUserActiveFlag | ACTIVE_FLAG | — | — |
| 39 | LastUpdatedByUserBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 40 | LastUpdatedByUserCreatedBy | CREATED_BY | — | — |
| 41 | LastUpdatedByUserCreationDate | CREATION_DATE | — | — |
| 42 | LastUpdatedByUserCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 43 | LastUpdatedByUserEndDate | END_DATE | — | — |
| 44 | LastUpdatedByUserHrTerminated | HR_TERMINATED | — | — |
| 45 | LastUpdatedByUserLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 46 | LastUpdatedByUserLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 47 | LastUpdatedByUserLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 48 | LastUpdatedByUserMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 49 | LastUpdatedByUserObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 50 | LastUpdatedByUserPartyId | PARTY_ID | — | — |
| 51 | LastUpdatedByUserPersonId | PERSON_ID | — | — |
| 52 | LastUpdatedByUserStartDate | START_DATE | — | — |
| 53 | LastUpdatedByUserSuspended | SUSPENDED | — | — |
| 54 | LastUpdatedByUserUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 55 | LastUpdatedByUserUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 56 | LastUpdatedByUserUserGuid | USER_GUID | — | — |
| 57 | LastUpdatedByUserUserId | USER_ID | — | — |
| 58 | LastUpdatedByUserUsername | USERNAME | — | — |

### [[xle_entity_profiles|XLE_ENTITY_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JrnlHdrLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 2 | XleEntityProfilesName | NAME | — | ✅ |
| 3 | XleEntityProfilesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
