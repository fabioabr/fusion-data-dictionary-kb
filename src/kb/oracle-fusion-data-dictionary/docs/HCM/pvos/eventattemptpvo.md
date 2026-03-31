---
id: DOC-HCM-PVO-EventAttemptPVO
doc_type: system-doc
title: "EventAttemptPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - EventAttemptPVO
  - eventattemptpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EventAttemptPVO

## 📌 Visão Geral

Registra tentativas de conclusão de eventos de aprendizagem com status de completude. Utilizado para rastrear progresso e taxa de conclusão de treinamentos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ContentAM.EventAttemptPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 1 | 1 | 3 | 11% |

---

## 🔗 Tabelas Relacionadas

- [[wlf_event_attempts|WLF_EVENT_ATTEMPTS]] — 28 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[wlf_event_attempts|WLF_EVENT_ATTEMPTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventAttemptPEOAttemptEndDate | ATTEMPT_END_DATE | — | — |
| 2 | EventAttemptPEOAvailableChildren | AVAILABLE_CHILDREN | — | — |
| 3 | EventAttemptPEOComments | COMMENTS | — | — |
| 4 | EventAttemptPEOCompletionDate | COMPLETION_DATE | — | — |
| 5 | EventAttemptPEOCompletionMasteryScore | COMPLETION_MASTERY_SCORE | — | — |
| 6 | EventAttemptPEOCompletionScore | COMPLETION_SCORE | — | — |
| 7 | EventAttemptPEOCompletionStatus | COMPLETION_STATUS | — | ✅ |
| 8 | EventAttemptPEOCreatedBy | CREATED_BY | — | — |
| 9 | EventAttemptPEOCreationDate | CREATION_DATE | — | — |
| 10 | EventAttemptPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 11 | EventAttemptPEOEventAttemptId | EVENT_ATTEMPT_ID | 🔑 | ✅ |
| 12 | EventAttemptPEOEventId | EVENT_ID | — | — |
| 13 | EventAttemptPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | EventAttemptPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | EventAttemptPEOLastUpdateMethod | LAST_UPDATE_METHOD | — | — |
| 16 | EventAttemptPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | EventAttemptPEOLatestAttemptInteractionId | LATEST_ATTEMPT_INTERACTION_ID | — | — |
| 18 | EventAttemptPEOLocation | LOCATION | — | — |
| 19 | EventAttemptPEONeedsStatusRollup | NEEDS_STATUS_ROLLUP | — | — |
| 20 | EventAttemptPEONeedsTimeRollup | NEEDS_TIME_ROLLUP | — | — |
| 21 | EventAttemptPEOObjStatusCalcMethod | OBJ_STATUS_CALC_METHOD | — | — |
| 22 | EventAttemptPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | EventAttemptPEOObjectiveMasteryScore | OBJECTIVE_MASTERY_SCORE | — | — |
| 24 | EventAttemptPEOObjectiveScore | OBJECTIVE_SCORE | — | — |
| 25 | EventAttemptPEOObjectiveStatus | OBJECTIVE_STATUS | — | — |
| 26 | EventAttemptPEOProgressMeasure | PROGRESS_MEASURE | — | — |
| 27 | EventAttemptPEORootAttemptId | ROOT_ATTEMPT_ID | — | — |
| 28 | TotalTime | TOTAL_TIME | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
