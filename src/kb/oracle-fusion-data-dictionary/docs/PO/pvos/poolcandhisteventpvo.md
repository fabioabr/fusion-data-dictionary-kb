---
id: DOC-PO-PVO-PoolCandHistEventPVO
doc_type: system-doc
title: "PoolCandHistEventPVO — PVO Purchasing"
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
  - PoolCandHistEventPVO
  - poolcandhisteventpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PoolCandHistEventPVO

## 📌 Visão Geral

Extrai o histórico de eventos de candidatos em pools (adição, remoção, mudança de status, fases do processo). Permite auditoria completa e análise de movimentação no banco de talentos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecSourcingCandPoolsAM.PoolCandHistEventPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 35 | 7 | 1 | 16 | 46% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_pools_vl|HRT_POOLS_VL]] — 1 atributos
- [[hrt_pool_members|HRT_POOL_MEMBERS]] — 5 atributos (1 BICC)
- [[irc_hist_event_b|IRC_HIST_EVENT_B]] — 2 atributos (2 BICC)
- [[irc_lc_history|IRC_LC_HISTORY]] — 21 atributos (1 PKs, 10 BICC)
- [[irc_phases_b|IRC_PHASES_B]] — 2 atributos (1 BICC)
- [[irc_processes_b|IRC_PROCESSES_B]] — 2 atributos (1 BICC)
- [[irc_states_b|IRC_STATES_B]] — 2 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hrt_pools_vl|HRT_POOLS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PoolId1 | POOL_ID | — | — |

### [[hrt_pool_members|HRT_POOL_MEMBERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EnterpriseId | ENTERPRISE_ID | — | — |
| 2 | MemberId | MEMBER_ID | — | ✅ |
| 3 | PoolId | POOL_ID | — | — |
| 4 | PoolMemberId | POOL_MEMBER_ID | — | — |
| 5 | PoolMemberPEOCreationDate | CREATION_DATE | — | — |

### [[irc_hist_event_b|IRC_HIST_EVENT_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HistoryEventTypeBPEOEventTypeCode | CODE | — | ✅ |
| 2 | HistoryEventTypeBPEOEventTypeId | EVENT_TYPE_ID | — | ✅ |

### [[irc_lc_history|IRC_LC_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HistoryEventId | HISTORY_EVENT_ID | 🔑 | ✅ |
| 2 | LCHistoryPEOActionId | ACTION_ID | — | — |
| 3 | LCHistoryPEOComments | COMMENTS | — | — |
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
| 15 | LCHistoryPEOReasonId | REASON_ID | — | — |
| 16 | LCHistoryPEORoutingStepId | ROUTING_STEP_ID | — | — |
| 17 | LCHistoryPEOSourceObjectId | SOURCE_OBJECT_ID | — | — |
| 18 | LCHistoryPEOStateId | STATE_ID | — | ✅ |
| 19 | LCHistoryPEOSubjectId | SUBJECT_ID | — | ✅ |
| 20 | StepDuration | STEP_DURATION | — | ✅ |
| 21 | TraceLog | TRACE_LOG | — | — |

### [[irc_phases_b|IRC_PHASES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PhaseBPEOCode | CODE | — | ✅ |
| 2 | PhaseId | PHASE_ID | — | — |

### [[irc_processes_b|IRC_PROCESSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcessBPEOCode | CODE | — | ✅ |
| 2 | ProcessId | PROCESS_ID | — | — |

### [[irc_states_b|IRC_STATES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StateBPEOCode | CODE | — | ✅ |
| 2 | StateId | STATE_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
