---
id: DOC-OTHER-PVO-RoutingStepEndActionPVO
doc_type: system-doc
title: "RoutingStepEndActionPVO — PVO Cross-Module"
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
  - RoutingStepEndActionPVO
  - routingstependactionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RoutingStepEndActionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Routing Step End Action. Acessa as tabelas: IRC_LC_ACTIONS_TL, IRC_LC_ACTION_USAGES_B, IRC_LC_ACTION_USAGES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecProcessLifecycleAM.RoutingStepEndActionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 3 | 1 | 6 | 40% |

---

## 🔗 Tabelas Relacionadas

- [[irc_lc_actions_tl|IRC_LC_ACTIONS_TL]] — 4 atributos (2 BICC)
- [[irc_lc_action_usages_b|IRC_LC_ACTION_USAGES_B]] — 7 atributos (1 PKs, 2 BICC)
- [[irc_lc_action_usages_tl|IRC_LC_ACTION_USAGES_TL]] — 4 atributos (2 BICC)

---

## ⚙️ Atributos

### [[irc_lc_actions_tl|IRC_LC_ACTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionTranslationPEOActionDescription | ACTION_DESCRIPTION | — | ✅ |
| 2 | ActionTranslationPEOActionId | ACTION_ID | — | — |
| 3 | ActionTranslationPEOActionName | ACTION_NAME | — | ✅ |
| 4 | ActionTranslationPEOLanguage | LANGUAGE | — | — |

### [[irc_lc_action_usages_b|IRC_LC_ACTION_USAGES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionId | ACTION_ID | — | ✅ |
| 2 | LastExecutionDate | LAST_EXECUTION_DATE | — | — |
| 3 | LastExecutionResult | LAST_EXECUTION_RESULT | — | — |
| 4 | RoutingStepId | ROUTING_STEP_ID | — | — |
| 5 | StepActionUsageCode | STEP_ACTION_USAGE_CODE | — | — |
| 6 | StepActionUsageId | STEP_ACTION_USAGE_ID | 🔑 | ✅ |
| 7 | TriggerEventCode | TRIGGER_EVENT_CODE | — | — |

### [[irc_lc_action_usages_tl|IRC_LC_ACTION_USAGES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionUsgTranslatePEOActionDescription | ACTION_DESCRIPTION | — | ✅ |
| 2 | ActionUsgTranslatePEOActionName | ACTION_NAME | — | ✅ |
| 3 | ActionUsgTranslatePEOLanguage | LANGUAGE | — | — |
| 4 | ActionUsgTranslatePEOStepActionUsageId | STEP_ACTION_USAGE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
