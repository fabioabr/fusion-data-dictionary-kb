---
id: DOC-HCM-PVO-GoalActionExtractPVO
doc_type: system-doc
title: "GoalActionExtractPVO — PVO Human Capital Management"
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
  - GoalActionExtractPVO
  - goalactionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GoalActionExtractPVO

## 📌 Visão Geral

Extrai ações vinculadas a metas (tarefas, links, marcos). Utilizado para rastrear planos de ação associados a objetivos individuais e organizacionais.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.GoalBiccExtractAM.GoalActionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 1 | 18 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hrg_goal_actions|HRG_GOAL_ACTIONS]] — 18 atributos (1 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[hrg_goal_actions|HRG_GOAL_ACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionName | ACTION_NAME | — | ✅ |
| 2 | ActionTypeCode | ACTION_TYPE_CODE | — | ✅ |
| 3 | ActionUrl | ACTION_URL | — | ✅ |
| 4 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 5 | Comments | COMMENTS | — | ✅ |
| 6 | CreatedBy | CREATED_BY | — | ✅ |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | GoalActionId | GOAL_ACTION_ID | 🔑 | ✅ |
| 9 | GoalId | GOAL_ID | — | ✅ |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | PercentCompleteCode | PERCENT_COMPLETE_CODE | — | ✅ |
| 15 | PriorityCode | PRIORITY_CODE | — | ✅ |
| 16 | StartDate | START_DATE | — | ✅ |
| 17 | StatusCode | STATUS_CODE | — | ✅ |
| 18 | TargetCompletionDate | TARGET_COMPLETION_DATE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
