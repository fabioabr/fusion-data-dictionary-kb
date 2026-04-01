---
id: DOC-PO-PVO-JobReqHistEventPVO
doc_type: system-doc
title: "JobReqHistEventPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - JobReqHistEventPVO
  - jobreqhisteventpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JobReqHistEventPVO

## 📌 Visão Geral

Extrai o histórico de eventos de requisições de contratação (criação, aprovação, preenchimento, cancelamento), com datas e responsáveis. Permite análise de tempo de ciclo e eficiência do processo de hiring.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecHiringRequisitionAM.JobReqHistEventPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 6 | 1 | 28 | 93% |

---

## 🔗 Tabelas Relacionadas

- [[irc_hist_event_b|IRC_HIST_EVENT_B]] — 2 atributos (2 BICC)
- [[irc_lc_history|IRC_LC_HISTORY]] — 19 atributos (1 PKs, 18 BICC)
- [[irc_phases_b|IRC_PHASES_B]] — 2 atributos (2 BICC)
- [[irc_processes_b|IRC_PROCESSES_B]] — 2 atributos (2 BICC)
- [[irc_requisitions_b|IRC_REQUISITIONS_B]] — 3 atributos (2 BICC)
- [[irc_states_b|IRC_STATES_B]] — 2 atributos (2 BICC)

---

## ⚙️ Atributos

### [[irc_hist_event_b|IRC_HIST_EVENT_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HistoryEventTypeBPEOEventTypeCode | CODE | — | ✅ |
| 2 | HistoryEventTypeBPEOEventTypeId | EVENT_TYPE_ID | — | ✅ |

### [[irc_lc_history|IRC_LC_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HistoryEventId | HISTORY_EVENT_ID | 🔑 | ✅ |
| 2 | LCHistoryPEOActionId | ACTION_ID | — | ✅ |
| 3 | LCHistoryPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | LCHistoryPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | LCHistoryPEOEventDate | EVENT_DATE | — | ✅ |
| 6 | LCHistoryPEOEventTypeId | EVENT_TYPE_ID | — | ✅ |
| 7 | LCHistoryPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LCHistoryPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LCHistoryPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | LCHistoryPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | LCHistoryPEOPersonId | PERSON_ID | — | ✅ |
| 12 | LCHistoryPEOPhaseId | PHASE_ID | — | ✅ |
| 13 | LCHistoryPEOProcessId | PROCESS_ID | — | ✅ |
| 14 | LCHistoryPEORoutingStepId | ROUTING_STEP_ID | — | ✅ |
| 15 | LCHistoryPEOSourceObjectId | SOURCE_OBJECT_ID | — | ✅ |
| 16 | LCHistoryPEOStateId | STATE_ID | — | ✅ |
| 17 | LCHistoryPEOSubjectId | SUBJECT_ID | — | ✅ |
| 18 | StepDuration | STEP_DURATION | — | ✅ |
| 19 | TraceLog | TRACE_LOG | — | — |

### [[irc_phases_b|IRC_PHASES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PhaseBPEOCode | CODE | — | ✅ |
| 2 | PhaseId | PHASE_ID | — | ✅ |

### [[irc_processes_b|IRC_PROCESSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcessBPEOCode | CODE | — | ✅ |
| 2 | ProcessId | PROCESS_ID | — | ✅ |

### [[irc_requisitions_b|IRC_REQUISITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequisitionBPEOOpenDate | OPEN_DATE | — | — |
| 2 | RequisitionBPEORequisitionTemplateId | REQUISITION_TEMPLATE_ID | — | ✅ |
| 3 | RequisitionId | REQUISITION_ID | — | ✅ |

### [[irc_states_b|IRC_STATES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StateBPEOCode | CODE | — | ✅ |
| 2 | StateId | STATE_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
