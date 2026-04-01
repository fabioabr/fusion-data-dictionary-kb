---
id: DOC-OTHER-PVO-RoutingStepStatePVO
doc_type: system-doc
title: "RoutingStepStatePVO — PVO Cross-Module"
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
  - RoutingStepStatePVO
  - routingstepstatepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RoutingStepStatePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Routing Step State. Acessa as tabelas: IRC_ROUTING_STEPS_B, IRC_STATES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecProcessLifecycleAM.RoutingStepStatePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 2 | 1 | 8 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[irc_routing_steps_b|IRC_ROUTING_STEPS_B]] — 14 atributos (1 PKs, 5 BICC)
- [[irc_states_tl|IRC_STATES_TL]] — 10 atributos (3 BICC)

---

## ⚙️ Atributos

### [[irc_routing_steps_b|IRC_ROUTING_STEPS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Code | CODE | — | ✅ |
| 2 | IsCompletionFlag | IS_COMPLETION_FLAG | — | — |
| 3 | IsInitialFlag | IS_INITIAL_FLAG | — | — |
| 4 | LastActivationDate | LAST_ACTIVATION_DATE | — | — |
| 5 | LastDeactivationDate | LAST_DEACTIVATION_DATE | — | — |
| 6 | ProcessId | PROCESS_ID | — | — |
| 7 | PublicStateId | PUBLIC_STATE_ID | — | ✅ |
| 8 | RoutingStepId | ROUTING_STEP_ID | 🔑 | ✅ |
| 9 | SequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 10 | SettingId | SETTING_ID | — | — |
| 11 | StateId | STATE_ID | — | ✅ |
| 12 | StepStatus | STEP_STATUS | — | — |
| 13 | SubProcessId | SUB_PROCESS_ID | — | — |
| 14 | TypeCode | TYPE_CODE | — | — |

### [[irc_states_tl|IRC_STATES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PublicStateTranslationPEOActionDescription | DESCRIPTION | — | — |
| 2 | PublicStateTranslationPEOLanguage | LANGUAGE | — | — |
| 3 | PublicStateTranslationPEOName | NAME | — | ✅ |
| 4 | PublicStateTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 5 | PublicStateTranslationPEOStateId | STATE_ID | — | — |
| 6 | StateTranslationPEODescription | DESCRIPTION | — | ✅ |
| 7 | StateTranslationPEOLanguage | LANGUAGE | — | — |
| 8 | StateTranslationPEOName | NAME | — | ✅ |
| 9 | StateTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 10 | StateTranslationPEOStateId | STATE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
