---
id: DOC-OTHER-PVO-JobAppHistEventPVO
doc_type: system-doc
title: "JobAppHistEventPVO — PVO Cross-Module"
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
  - JobAppHistEventPVO
  - jobapphisteventpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JobAppHistEventPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Job App Hist Event. Acessa as tabelas: IRC_HIST_EVENT_B, IRC_LC_HISTORY, IRC_LC_REASONS_B (+9).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecSubmissionsAM.JobAppHistEventPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 52 | 12 | 1 | 27 | 52% |

---

## 🔗 Tabelas Relacionadas

- [[irc_hist_event_b|IRC_HIST_EVENT_B]] — 2 atributos (1 BICC)
- [[irc_lc_history|IRC_LC_HISTORY]] — 21 atributos (1 PKs, 13 BICC)
- [[irc_lc_reasons_b|IRC_LC_REASONS_B]] — 3 atributos (2 BICC)
- [[irc_lc_reasons_tl|IRC_LC_REASONS_TL]] — 3 atributos (2 BICC)
- [[irc_offers|IRC_OFFERS]] — 3 atributos (2 BICC)
- [[irc_phases_b|IRC_PHASES_B]] — 3 atributos (1 BICC)
- [[irc_processes_b|IRC_PROCESSES_B]] — 2 atributos (1 BICC)
- [[irc_processes_tl|IRC_PROCESSES_TL]] — 3 atributos
- [[irc_requisitions_b|IRC_REQUISITIONS_B]] — 3 atributos (1 BICC)
- [[irc_routing_steps_b|IRC_ROUTING_STEPS_B]] — 2 atributos (1 BICC)
- [[irc_states_b|IRC_STATES_B]] — 2 atributos (1 BICC)
- [[irc_submissions|IRC_SUBMISSIONS]] — 5 atributos (2 BICC)

---

## ⚙️ Atributos

### [[irc_hist_event_b|IRC_HIST_EVENT_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HistoryEventTypeBPEOEventTypeCode | CODE | — | ✅ |
| 2 | HistoryEventTypeBPEOEventTypeId | EVENT_TYPE_ID | — | — |

### [[irc_lc_history|IRC_LC_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HistoryEventId | HISTORY_EVENT_ID | 🔑 | ✅ |
| 2 | LCHistoryPEOActionId | ACTION_ID | — | ✅ |
| 3 | LCHistoryPEOComments | COMMENTS | — | ✅ |
| 4 | LCHistoryPEOCreatedBy | CREATED_BY | — | — |
| 5 | LCHistoryPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | LCHistoryPEOEventDate | EVENT_DATE | — | ✅ |
| 7 | LCHistoryPEOEventTypeId | EVENT_TYPE_ID | — | ✅ |
| 8 | LCHistoryPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LCHistoryPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | LCHistoryPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | LCHistoryPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | LCHistoryPEOPersonId | PERSON_ID | — | — |
| 13 | LCHistoryPEOPhaseId | PHASE_ID | — | ✅ |
| 14 | LCHistoryPEOProcessId | PROCESS_ID | — | ✅ |
| 15 | LCHistoryPEOReasonId | REASON_ID | — | ✅ |
| 16 | LCHistoryPEORoutingStepId | ROUTING_STEP_ID | — | — |
| 17 | LCHistoryPEOSourceObjectId | SOURCE_OBJECT_ID | — | — |
| 18 | LCHistoryPEOStateId | STATE_ID | — | ✅ |
| 19 | LCHistoryPEOSubjectId | SUBJECT_ID | — | ✅ |
| 20 | StepDuration | STEP_DURATION | — | ✅ |
| 21 | TraceLog | TRACE_LOG | — | — |

### [[irc_lc_reasons_b|IRC_LC_REASONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReasonsBPEOReasonCode | REASON_CODE | — | ✅ |
| 2 | ReasonsBPEOReasonId | REASON_ID | — | — |
| 3 | ReasonsBPEOReasonStatusCode | REASON_STATUS_CODE | — | ✅ |

### [[irc_lc_reasons_tl|IRC_LC_REASONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReasonsTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 2 | ReasonsTranslationPEOReasonId | REASON_ID | — | — |
| 3 | ReasonsTranslationPEOReasonName | REASON_NAME | — | ✅ |

### [[irc_offers|IRC_OFFERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OffersPEOCreationDate | CREATION_DATE | — | ✅ |
| 2 | OffersPEOMoveToHrDate | MOVE_TO_HR_DATE | — | — |
| 3 | OffersPEOOfferId | OFFER_ID | — | ✅ |

### [[irc_phases_b|IRC_PHASES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PhaseBPEOCode | CODE | — | ✅ |
| 2 | PhaseBPEOPhaseId | PHASE_ID | — | — |
| 3 | PhaseBPEOPhaseSequenceNumber | SEQUENCE_NUMBER | — | — |

### [[irc_processes_b|IRC_PROCESSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcessBPEOCode | CODE | — | ✅ |
| 2 | ProcessBPEOProcessId | PROCESS_ID | — | — |

### [[irc_processes_tl|IRC_PROCESSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcessTranslationPEOLanguage | LANGUAGE | — | — |
| 2 | ProcessTranslationPEOName | NAME | — | — |
| 3 | ProcessTranslationPEOProcessId | PROCESS_ID | — | — |

### [[irc_requisitions_b|IRC_REQUISITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReqUsageCode | REQ_USAGE_CODE | — | — |
| 2 | RequisitionBPEOOpenDate | OPEN_DATE | — | — |
| 3 | RequisitionId | REQUISITION_ID | — | ✅ |

### [[irc_routing_steps_b|IRC_ROUTING_STEPS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RoutingStepBPEORoutingStepId | ROUTING_STEP_ID | — | — |
| 2 | RoutingStepBPEOSequenceNumber | SEQUENCE_NUMBER | — | ✅ |

### [[irc_states_b|IRC_STATES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StateBPEOCode | CODE | — | ✅ |
| 2 | StateBPEOStateId | STATE_ID | — | — |

### [[irc_submissions|IRC_SUBMISSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SubmissionId | SUBMISSION_ID | — | ✅ |
| 2 | SubmissionPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | SubmissionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | SubmissionPEOPersonId | PERSON_ID | — | — |
| 5 | SubmissionPEORequisitionId | REQUISITION_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
