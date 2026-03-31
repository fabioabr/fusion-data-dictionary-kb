---
id: DOC-OTHER-PVO-GoalAlignmentPVO
doc_type: system-doc
title: "GoalAlignmentPVO — PVO Cross-Module"
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

View Object para extração BICC de dados de Goal Alignment. Acessa as tabelas: HRG_GOALS.

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

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
