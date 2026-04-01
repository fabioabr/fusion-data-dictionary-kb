---
id: DOC-GL-PVO-JournalHeaderPVO
doc_type: system-doc
title: "JournalHeaderPVO — PVO General Ledger"
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
  - JournalHeaderPVO
  - journalheaderpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JournalHeaderPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Journal Header. Acessa as tabelas: FND_DOCUMENT_SEQUENCES, FUN_SEQ_VERSIONS, GL_CALENDARS (+7).

**Caminho:** `FscmTopModelAM.FinGlJrnlEntriesAM.JournalHeaderPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 302 | 10 | 1 | 77 | 25% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]] — 8 atributos (3 BICC)
- [[fun_seq_versions|FUN_SEQ_VERSIONS]] — 18 atributos (4 BICC)
- [[gl_calendars|GL_CALENDARS]] — 21 atributos
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 14 atributos
- [[gl_encumbrance_types_vl|GL_ENCUMBRANCE_TYPES_VL]] — 2 atributos (2 BICC)
- [[gl_je_batches|GL_JE_BATCHES]] — 37 atributos (17 BICC)
- [[gl_je_headers|GL_JE_HEADERS]] — 68 atributos (1 PKs, 41 BICC)
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
| 9 | ConversionTypePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 10 | ConversionTypeSecurityFlag | SECURITY_FLAG | — | — |
| 11 | ConversionTypeUserConversionType | USER_CONVERSION_TYPE | — | — |
| 12 | ConversionTypeUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |
| 13 | CreatedByPersonNameObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 14 | LastUpdatedByPersonNameObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |

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
| 26 | JrnlBatchPeriodSetName | PERIOD_SET_NAME | — | — |
| 27 | JrnlBatchPostedDate | POSTED_DATE | — | ✅ |
| 28 | JrnlBatchPostedDateTime | POSTED_DATE | — | — |
| 29 | JrnlBatchPostingRunId | POSTING_RUN_ID | — | — |
| 30 | JrnlBatchRequestId | REQUEST_ID | — | — |
| 31 | JrnlBatchRunningTotalAccountedCr | RUNNING_TOTAL_ACCOUNTED_CR | — | — |
| 32 | JrnlBatchRunningTotalAccountedDr | RUNNING_TOTAL_ACCOUNTED_DR | — | — |
| 33 | JrnlBatchRunningTotalCr | RUNNING_TOTAL_CR | — | ✅ |
| 34 | JrnlBatchRunningTotalDr | RUNNING_TOTAL_DR | — | ✅ |
| 35 | JrnlBatchStatus | STATUS | — | — |
| 36 | JrnlBatchStatusVerified | STATUS_VERIFIED | — | — |
| 37 | JrnlBatchUnreservationPacketId | UNRESERVATION_PACKET_ID | — | — |

### [[gl_je_headers|GL_JE_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JeHeaderId | JE_HEADER_ID | 🔑 | ✅ |
| 2 | JrnlHdrAccrualRevChangeSignFlagCode | ACCRUAL_REV_CHANGE_SIGN_FLAG | — | ✅ |
| 3 | JrnlHdrAccrualRevEffectiveDate | ACCRUAL_REV_EFFECTIVE_DATE | — | — |
| 4 | JrnlHdrAccrualRevFlag | ACCRUAL_REV_FLAG | — | ✅ |
| 5 | JrnlHdrAccrualRevJeHeaderId | ACCRUAL_REV_JE_HEADER_ID | — | — |
| 6 | JrnlHdrAccrualRevPeriodName | ACCRUAL_REV_PERIOD_NAME | — | ✅ |
| 7 | JrnlHdrAccrualRevStatus | ACCRUAL_REV_STATUS | — | ✅ |
| 8 | JrnlHdrActualFlag | ACTUAL_FLAG | — | ✅ |
| 9 | JrnlHdrBalancedJeFlag | BALANCED_JE_FLAG | — | — |
| 10 | JrnlHdrBalancingSegmentValue | BALANCING_SEGMENT_VALUE | — | ✅ |
| 11 | JrnlHdrBudgetVersionId | BUDGET_VERSION_ID | — | — |
| 12 | JrnlHdrCloseAcctSeqAssignId | CLOSE_ACCT_SEQ_ASSIGN_ID | — | — |
| 13 | JrnlHdrCloseAcctSeqValue | CLOSE_ACCT_SEQ_VALUE | — | ✅ |
| 14 | JrnlHdrCloseAcctSeqVersionId | CLOSE_ACCT_SEQ_VERSION_ID | — | — |
| 15 | JrnlHdrControlTotal | CONTROL_TOTAL | — | ✅ |
| 16 | JrnlHdrConversionFlag | CONVERSION_FLAG | — | ✅ |
| 17 | JrnlHdrCrBalSegValue | CR_BAL_SEG_VALUE | — | ✅ |
| 18 | JrnlHdrCreatedBy | CREATED_BY | — | ✅ |
| 19 | JrnlHdrCreationDate | CREATION_DATE | — | — |
| 20 | JrnlHdrCurrencyCode | CURRENCY_CODE | — | ✅ |
| 21 | JrnlHdrCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 22 | JrnlHdrCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 23 | JrnlHdrCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 24 | JrnlHdrDateCreated | DATE_CREATED | — | ✅ |
| 25 | JrnlHdrDefaultEffectiveDate | DEFAULT_EFFECTIVE_DATE | — | ✅ |
| 26 | JrnlHdrDescription | DESCRIPTION | — | ✅ |
| 27 | JrnlHdrDisplayAlcJournalFlag | DISPLAY_ALC_JOURNAL_FLAG | — | — |
| 28 | JrnlHdrDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 29 | JrnlHdrDocSequenceValue | DOC_SEQUENCE_VALUE | — | ✅ |
| 30 | JrnlHdrDrBalSegValue | DR_BAL_SEG_VALUE | — | ✅ |
| 31 | JrnlHdrEarliestPostableDate | EARLIEST_POSTABLE_DATE | — | — |
| 32 | JrnlHdrEncumbranceTypeId | ENCUMBRANCE_TYPE_ID | — | — |
| 33 | JrnlHdrExternalReference | EXTERNAL_REFERENCE | — | ✅ |
| 34 | JrnlHdrFromRecurringHeaderId | FROM_RECURRING_HEADER_ID | — | — |
| 35 | JrnlHdrIntercompanyMode | INTERCOMPANY_MODE | — | — |
| 36 | JrnlHdrJeBatchId | JE_BATCH_ID | — | — |
| 37 | JrnlHdrJeCategory | JE_CATEGORY | — | — |
| 38 | JrnlHdrJeFromSlaFlag | JE_FROM_SLA_FLAG | — | ✅ |
| 39 | JrnlHdrJeSource | JE_SOURCE | — | — |
| 40 | JrnlHdrLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 41 | JrnlHdrLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 42 | JrnlHdrLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 43 | JrnlHdrLedgerId | LEDGER_ID | — | — |
| 44 | JrnlHdrLocalDocSequenceId | LOCAL_DOC_SEQUENCE_ID | — | — |
| 45 | JrnlHdrLocalDocSequenceValue | LOCAL_DOC_SEQUENCE_VALUE | — | ✅ |
| 46 | JrnlHdrMultiBalSegFlag | MULTI_BAL_SEG_FLAG | — | — |
| 47 | JrnlHdrMultiCurrencyFlag | MULTI_CURRENCY_FLAG | — | ✅ |
| 48 | JrnlHdrName | NAME | — | ✅ |
| 49 | JrnlHdrObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 50 | JrnlHdrOriginatingBalSegValue | ORIGINATING_BAL_SEG_VALUE | — | ✅ |
| 51 | JrnlHdrParentJeHeaderId | PARENT_JE_HEADER_ID | — | ✅ |
| 52 | JrnlHdrPeriodName | PERIOD_NAME | — | ✅ |
| 53 | JrnlHdrPostCurrencyCode | POST_CURRENCY_CODE | — | — |
| 54 | JrnlHdrPostMultiCurrencyFlag | POST_MULTI_CURRENCY_FLAG | — | ✅ |
| 55 | JrnlHdrPostedDate | POSTED_DATE | — | ✅ |
| 56 | JrnlHdrPostedDateTime | POSTED_DATE | — | — |
| 57 | JrnlHdrPostingAcctSeqAssignId | POSTING_ACCT_SEQ_ASSIGN_ID | — | — |
| 58 | JrnlHdrPostingAcctSeqValue | POSTING_ACCT_SEQ_VALUE | — | ✅ |
| 59 | JrnlHdrPostingAcctSeqVersionId | POSTING_ACCT_SEQ_VERSION_ID | — | — |
| 60 | JrnlHdrReferenceDate | REFERENCE_DATE | — | ✅ |
| 61 | JrnlHdrReversedJeHeaderId | REVERSED_JE_HEADER_ID | — | ✅ |
| 62 | JrnlHdrRunningTotalAccountedCr | RUNNING_TOTAL_ACCOUNTED_CR | — | ✅ |
| 63 | JrnlHdrRunningTotalAccountedDr | RUNNING_TOTAL_ACCOUNTED_DR | — | ✅ |
| 64 | JrnlHdrRunningTotalCr | RUNNING_TOTAL_CR | — | ✅ |
| 65 | JrnlHdrRunningTotalDr | RUNNING_TOTAL_DR | — | ✅ |
| 66 | JrnlHdrStatus | STATUS | — | ✅ |
| 67 | JrnlHdrTaxLegalEntityId | TAX_LEGAL_ENTITY_ID | — | — |
| 68 | JrnlHdrTaxStatusCode | TAX_STATUS_CODE | — | — |

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
