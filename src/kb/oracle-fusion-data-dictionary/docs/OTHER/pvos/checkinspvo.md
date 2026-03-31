---
id: DOC-OTHER-PVO-CheckinsPVO
doc_type: system-doc
title: "CheckinsPVO — PVO Cross-Module"
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
  - CheckinsPVO
  - checkinspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CheckinsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Checkins. Acessa as tabelas: HRA_CHECK_IN_MEETINGS, HRA_CHECK_IN_TMPLS_VL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPerformanceDocsAM.CheckinsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 37 | 2 | 1 | 30 | 81% |

---

## 🔗 Tabelas Relacionadas

- [[hra_check_in_meetings|HRA_CHECK_IN_MEETINGS]] — 16 atributos (1 PKs, 12 BICC)
- [[hra_check_in_tmpls_vl|HRA_CHECK_IN_TMPLS_VL]] — 21 atributos (18 BICC)

---

## ⚙️ Atributos

### [[hra_check_in_meetings|HRA_CHECK_IN_MEETINGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CheckInMeetingPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CheckInMeetingPEOCheckInDate | CHECK_IN_DATE | — | ✅ |
| 3 | CheckInMeetingPEOCheckInMeetingId | CHECK_IN_MEETING_ID | 🔑 | ✅ |
| 4 | CheckInMeetingPEOCheckInTemplateId | CHECK_IN_TEMPLATE_ID | — | ✅ |
| 5 | CheckInMeetingPEOCreatedByPersonId | CREATED_BY_PERSON_ID | — | — |
| 6 | CheckInMeetingPEODocumentName | DOCUMENT_NAME | — | ✅ |
| 7 | CheckInMeetingPEOManagerPersonId | MANAGER_PERSON_ID | — | ✅ |
| 8 | CheckInMeetingPEOReviewPeriodId | REVIEW_PERIOD_ID | — | — |
| 9 | CheckInMeetingPEOWorkerAssignmentId | WORKER_ASSIGNMENT_ID | — | ✅ |
| 10 | CheckInMeetingPEOWorkerPersonId | WORKER_PERSON_ID | — | ✅ |
| 11 | CreatedBy | CREATED_BY | — | ✅ |
| 12 | CreationDate | CREATION_DATE | — | ✅ |
| 13 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[hra_check_in_tmpls_vl|HRA_CHECK_IN_TMPLS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TemplateCheckInPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | TemplateCheckInPEOCheckInTemplateId | CHECK_IN_TEMPLATE_ID | — | — |
| 3 | TemplateCheckInPEOComments | COMMENTS | — | ✅ |
| 4 | TemplateCheckInPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | TemplateCheckInPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | TemplateCheckInPEODateFrom | DATE_FROM | — | ✅ |
| 7 | TemplateCheckInPEODateTo | DATE_TO | — | ✅ |
| 8 | TemplateCheckInPEODevGoalsAutoPopulateFlag | DEV_GOALS_AUTO_POPULATE_FLAG | — | ✅ |
| 9 | TemplateCheckInPEODevelopmentGoalsFlag | DEVELOPMENT_GOALS_FLAG | — | ✅ |
| 10 | TemplateCheckInPEOFreeFormNotesFlag | FREE_FORM_NOTES_FLAG | — | — |
| 11 | TemplateCheckInPEOGeneralDiscussionTopicFlag | GENERAL_DISCUSSION_TOPIC_FLAG | — | ✅ |
| 12 | TemplateCheckInPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | TemplateCheckInPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | TemplateCheckInPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | TemplateCheckInPEOManagerQuestionnaireId | MANAGER_QUESTIONNAIRE_ID | — | ✅ |
| 16 | TemplateCheckInPEOName | NAME | — | ✅ |
| 17 | TemplateCheckInPEOPerfGoalsAutoPopulateFlag | PERF_GOALS_AUTO_POPULATE_FLAG | — | ✅ |
| 18 | TemplateCheckInPEOPerformanceGoalsFlag | PERFORMANCE_GOALS_FLAG | — | ✅ |
| 19 | TemplateCheckInPEOQuestionnaireFlag | QUESTIONNAIRE_FLAG | — | ✅ |
| 20 | TemplateCheckInPEOStatusCode | STATUS_CODE | — | ✅ |
| 21 | TemplateCheckInPEOWorkerQuestionnaireId | WORKER_QUESTIONNAIRE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
