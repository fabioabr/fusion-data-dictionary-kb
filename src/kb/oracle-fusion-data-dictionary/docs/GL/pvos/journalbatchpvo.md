---
id: DOC-GL-PVO-JournalBatchPVO
doc_type: system-doc
title: "JournalBatchPVO — PVO General Ledger"
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
  - JournalBatchPVO
  - journalbatchpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JournalBatchPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Journal Batch. Acessa as tabelas: GL_CALENDARS, GL_JE_BATCHES, PER_PERSON_NAMES_F_V (+1).

**Caminho:** `FscmTopModelAM.FinGlJrnlEntriesAM.JournalBatchPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 95 | 4 | 1 | 22 | 23% |

---

## 🔗 Tabelas Relacionadas

- [[gl_calendars|GL_CALENDARS]] — 21 atributos
- [[gl_je_batches|GL_JE_BATCHES]] — 37 atributos (1 PKs, 19 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 21 atributos (3 BICC)
- [[per_users|PER_USERS]] — 16 atributos

---

## ⚙️ Atributos

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

### [[gl_je_batches|GL_JE_BATCHES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JeBatchId | JE_BATCH_ID | 🔑 | ✅ |
| 2 | JournalBatchAccountedPeriodType | ACCOUNTED_PERIOD_TYPE | — | ✅ |
| 3 | JournalBatchActualFlag | ACTUAL_FLAG | — | ✅ |
| 4 | JournalBatchApprovalStatusCode | APPROVAL_STATUS_CODE | — | ✅ |
| 5 | JournalBatchApproverEmployeeId | APPROVER_EMPLOYEE_ID | — | — |
| 6 | JournalBatchAverageJournalFlag | AVERAGE_JOURNAL_FLAG | — | — |
| 7 | JournalBatchBudgetaryControlStatus | BUDGETARY_CONTROL_STATUS | — | — |
| 8 | JournalBatchChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | ✅ |
| 9 | JournalBatchControlTotal | CONTROL_TOTAL | — | ✅ |
| 10 | JournalBatchCreatedBy | CREATED_BY | — | ✅ |
| 11 | JournalBatchCreationDate | CREATION_DATE | — | ✅ |
| 12 | JournalBatchDateCreated | DATE_CREATED | — | — |
| 13 | JournalBatchDefaultEffectiveDate | DEFAULT_EFFECTIVE_DATE | — | ✅ |
| 14 | JournalBatchDefaultPeriodName | DEFAULT_PERIOD_NAME | — | — |
| 15 | JournalBatchDescription | DESCRIPTION | — | ✅ |
| 16 | JournalBatchEarliestPostableDate | EARLIEST_POSTABLE_DATE | — | — |
| 17 | JournalBatchGroupId | GROUP_ID | — | ✅ |
| 18 | JournalBatchJeSource | JE_SOURCE | — | — |
| 19 | JournalBatchLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | JournalBatchLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | JournalBatchLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 22 | JournalBatchName | NAME | — | ✅ |
| 23 | JournalBatchObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 24 | JournalBatchPacketId | PACKET_ID | — | — |
| 25 | JournalBatchParentJeBatchId | PARENT_JE_BATCH_ID | — | — |
| 26 | JournalBatchPeriodSetName | PERIOD_SET_NAME | — | — |
| 27 | JournalBatchPostedDate | POSTED_DATE | — | ✅ |
| 28 | JournalBatchPostedDateTime | POSTED_DATE | — | — |
| 29 | JournalBatchPostingRunId | POSTING_RUN_ID | — | — |
| 30 | JournalBatchRequestId | REQUEST_ID | — | — |
| 31 | JournalBatchRunningTotalAccountedCr | RUNNING_TOTAL_ACCOUNTED_CR | — | ✅ |
| 32 | JournalBatchRunningTotalAccountedDr | RUNNING_TOTAL_ACCOUNTED_DR | — | ✅ |
| 33 | JournalBatchRunningTotalCr | RUNNING_TOTAL_CR | — | ✅ |
| 34 | JournalBatchRunningTotalDr | RUNNING_TOTAL_DR | — | ✅ |
| 35 | JournalBatchStatus | STATUS | — | — |
| 36 | JournalBatchStatusVerified | STATUS_VERIFIED | — | — |
| 37 | JournalBatchUnreservationPacketId | UNRESERVATION_PACKET_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BatchApprovedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | BatchApprovedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | BatchApprovedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | BatchApprovedByPersonId | PERSON_ID | — | — |
| 5 | BatchApprovedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | CreatedByPersonNameCreatedBy | CREATED_BY | — | — |
| 7 | CreatedByPersonNameCreationDate | CREATION_DATE | — | — |
| 8 | CreatedByPersonNameDisplayName | DISPLAY_NAME | — | ✅ |
| 9 | CreatedByPersonNameEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 10 | CreatedByPersonNameEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 11 | CreatedByPersonNameLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 12 | CreatedByPersonNameLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | CreatedByPersonNamePersonNameId | PERSON_NAME_ID | — | — |
| 14 | LastUpdatedByPersonNameCreatedBy | CREATED_BY | — | — |
| 15 | LastUpdatedByPersonNameCreationDate | CREATION_DATE | — | — |
| 16 | LastUpdatedByPersonNameDisplayName | DISPLAY_NAME | — | ✅ |
| 17 | LastUpdatedByPersonNameEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 18 | LastUpdatedByPersonNameEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 19 | LastUpdatedByPersonNameLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 20 | LastUpdatedByPersonNameLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 21 | LastUpdatedByPersonNamePersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedByUserCreatedBy | CREATED_BY | — | — |
| 2 | CreatedByUserCreationDate | CREATION_DATE | — | — |
| 3 | CreatedByUserLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 4 | CreatedByUserLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 5 | CreatedByUserObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | CreatedByUserPersonId | PERSON_ID | — | — |
| 7 | CreatedByUserUserId | USER_ID | — | — |
| 8 | CreatedByUserUsername | USERNAME | — | — |
| 9 | LastUpdatedByUserCreatedBy | CREATED_BY | — | — |
| 10 | LastUpdatedByUserCreationDate | CREATION_DATE | — | — |
| 11 | LastUpdatedByUserLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 12 | LastUpdatedByUserLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | LastUpdatedByUserObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | LastUpdatedByUserPersonId | PERSON_ID | — | — |
| 15 | LastUpdatedByUserUserId | USER_ID | — | — |
| 16 | LastUpdatedByUserUsername | USERNAME | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
