---
id: DOC-HCM-PVO-PoolMgmtProcessPVO
doc_type: system-doc
title: "PoolMgmtProcessPVO — PVO Human Capital Management"
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
  - PoolMgmtProcessPVO
  - poolmgmtprocesspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PoolMgmtProcessPVO

## 📌 Visão Geral

Extrai os processos de gestão de pool de candidatos (recrutamento), com etapas de roteamento e configuração. Suporta automação e monitoramento do pipeline de candidatos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecProcessLifecycleAM.PoolMgmtProcessPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 37 | 3 | 1 | 16 | 43% |

---

## 🔗 Tabelas Relacionadas

- [[irc_processes_b|IRC_PROCESSES_B]] — 15 atributos (1 PKs, 8 BICC)
- [[irc_processes_tl|IRC_PROCESSES_TL]] — 5 atributos (2 BICC)
- [[irc_routing_steps_b|IRC_ROUTING_STEPS_B]] — 17 atributos (6 BICC)

---

## ⚙️ Atributos

### [[irc_processes_b|IRC_PROCESSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Code | CODE | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | IsActiveFlag | IS_ACTIVE_FLAG | — | — |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ModuleId | MODULE_ID | — | — |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | PhaseId | PHASE_ID | — | — |
| 11 | ProcessId | PROCESS_ID | 🔑 | ✅ |
| 12 | SeedDataSource | SEED_DATA_SOURCE | — | — |
| 13 | StatusCode | STATUS_CODE | — | ✅ |
| 14 | TypeCode | TYPE_CODE | — | ✅ |
| 15 | UsageCode | USAGE_CODE | — | — |

### [[irc_processes_tl|IRC_PROCESSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcessTranslationPEODescription | DESCRIPTION | — | ✅ |
| 2 | ProcessTranslationPEOLanguage | LANGUAGE | — | — |
| 3 | ProcessTranslationPEOName | NAME | — | ✅ |
| 4 | ProcessTranslationPEOProcessId | PROCESS_ID | — | — |
| 5 | ProcessTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[irc_routing_steps_b|IRC_ROUTING_STEPS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RoutingStepPhaseBPEOPhaseId | PHASE_ID | — | ✅ |
| 2 | RoutingStepPhaseBPEOProcessId | PROCESS_ID | — | — |
| 3 | RoutingStepPhaseBPEORoutingStepId | ROUTING_STEP_ID | — | — |
| 4 | RoutingStepPhaseBPEOSequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 5 | RoutingStepPhaseBPEOStateId | STATE_ID | — | ✅ |
| 6 | RoutingStepPhaseBPEOStepStatus | STEP_STATUS | — | — |
| 7 | RoutingStepPhaseBPEOSubProcessId | SUB_PROCESS_ID | — | — |
| 8 | RoutingStepPhaseBPEOTypeCode | TYPE_CODE | — | — |
| 9 | RoutingStepStateBPEOPhaseId | PHASE_ID | — | ✅ |
| 10 | RoutingStepStateBPEOProcessId | PROCESS_ID | — | — |
| 11 | RoutingStepStateBPEOPublicStateId | PUBLIC_STATE_ID | — | — |
| 12 | RoutingStepStateBPEORoutingStepId | ROUTING_STEP_ID | — | — |
| 13 | RoutingStepStateBPEOSequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 14 | RoutingStepStateBPEOStateId | STATE_ID | — | ✅ |
| 15 | RoutingStepStateBPEOStepStatus | STEP_STATUS | — | — |
| 16 | RoutingStepStateBPEOSubProcessId | SUB_PROCESS_ID | — | — |
| 17 | RoutingStepStateBPEOTypeCode | TYPE_CODE | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
