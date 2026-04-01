---
id: DOC-HCM-PVO-GoalAlignmentPVO
doc_type: system-doc
title: "GoalAlignmentPVO — PVO Human Capital Management"
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
  - GoalAlignmentPVO
  - goalalignmentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GoalAlignmentPVO

## 📌 Visão Geral

Disponibiliza vínculos de alinhamento entre metas com nome da meta alinhada. Suporta visualização de cascateamento de objetivos na organização.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmGoalCoreAM.GoalAlignmentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 4 | 1 | 1 | 2 | 50% |

---

## 🔗 Tabelas Relacionadas

- [[hrg_goals|HRG_GOALS]] — 4 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[hrg_goals|HRG_GOALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalPEOGoalApprovalState | GOAL_APPROVAL_STATE | — | — |
| 2 | GoalPEOGoalName | GOAL_NAME | — | ✅ |
| 3 | GoalPEOLongDescription | LONG_DESCRIPTION | — | — |
| 4 | GoalpeogoalId | GOAL_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
