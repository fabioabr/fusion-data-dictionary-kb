---
id: DOC-OTHER-PVO-RoutingStepPhasePVO
doc_type: system-doc
title: "RoutingStepPhasePVO — PVO Cross-Module"
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
  - RoutingStepPhasePVO
  - routingstepphasepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RoutingStepPhasePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Routing Step Phase. Acessa as tabelas: IRC_PHASES_TL, IRC_ROUTING_STEPS_B.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecProcessLifecycleAM.RoutingStepPhasePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 2 | 1 | 6 | 32% |

---

## 🔗 Tabelas Relacionadas

- [[irc_phases_tl|IRC_PHASES_TL]] — 5 atributos (2 BICC)
- [[irc_routing_steps_b|IRC_ROUTING_STEPS_B]] — 14 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[irc_phases_tl|IRC_PHASES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PhaseTranslationPEODescription | DESCRIPTION | — | ✅ |
| 2 | PhaseTranslationPEOLanguage | LANGUAGE | — | — |
| 3 | PhaseTranslationPEOName | NAME | — | ✅ |
| 4 | PhaseTranslationPEOPhaseId | PHASE_ID | — | — |
| 5 | PhaseTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[irc_routing_steps_b|IRC_ROUTING_STEPS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Code | CODE | — | ✅ |
| 2 | IsCompletionFlag | IS_COMPLETION_FLAG | — | — |
| 3 | IsInitialFlag | IS_INITIAL_FLAG | — | — |
| 4 | LastActivationDate | LAST_ACTIVATION_DATE | — | — |
| 5 | LastDeactivationDate | LAST_DEACTIVATION_DATE | — | — |
| 6 | PhaseId | PHASE_ID | — | ✅ |
| 7 | ProcessId | PROCESS_ID | — | — |
| 8 | PublicStateId | PUBLIC_STATE_ID | — | — |
| 9 | RoutingStepId | ROUTING_STEP_ID | 🔑 | ✅ |
| 10 | SequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 11 | SettingId | SETTING_ID | — | — |
| 12 | StepStatus | STEP_STATUS | — | — |
| 13 | SubProcessId | SUB_PROCESS_ID | — | — |
| 14 | TypeCode | TYPE_CODE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
