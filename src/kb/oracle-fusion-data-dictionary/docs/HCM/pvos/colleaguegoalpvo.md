---
id: DOC-HCM-PVO-ColleagueGoalPVO
doc_type: system-doc
title: "ColleagueGoalPVO — PVO Human Capital Management"
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
  - ColleagueGoalPVO
  - colleaguegoalpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ColleagueGoalPVO

## 📌 Visão Geral

Extrai metas de colegas com status de aprovacao para visibilidade lateral. Suporta alinhamento de objetivos entre pares e colaboracao.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmGoalCoreAM.ColleagueGoalPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 1 | 7 | 78% |

---

## 🔗 Tabelas Relacionadas

- [[hrg_goals|HRG_GOALS]] — 9 atributos (1 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[hrg_goals|HRG_GOALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalId | GOAL_ID | 🔑 | ✅ |
| 2 | GoalPEOApprovalStatusCode | APPROVAL_STATUS_CODE | — | ✅ |
| 3 | GoalPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | GoalPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | GoalPEOGoalApprovalState | GOAL_APPROVAL_STATE | — | — |
| 6 | GoalPEOHrchyAccessGrantDate | HRCHY_ACCESS_GRANT_DATE | — | — |
| 7 | GoalPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | GoalPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | GoalPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
