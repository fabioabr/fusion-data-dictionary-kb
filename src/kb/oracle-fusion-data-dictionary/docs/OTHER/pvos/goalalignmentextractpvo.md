---
id: DOC-OTHER-PVO-GoalAlignmentExtractPVO
doc_type: system-doc
title: "GoalAlignmentExtractPVO — PVO Cross-Module"
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
  - GoalAlignmentExtractPVO
  - goalalignmentextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GoalAlignmentExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Goal Alignment Extract. Acessa as tabelas: HRG_GOAL_ALIGNMENTS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.GoalBiccExtractAM.GoalAlignmentExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 1 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hrg_goal_alignments|HRG_GOAL_ALIGNMENTS]] — 10 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[hrg_goal_alignments|HRG_GOAL_ALIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AlignedGoalId | ALIGNED_GOAL_ID | — | ✅ |
| 2 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | GoalAlignmentId | GOAL_ALIGNMENT_ID | 🔑 | ✅ |
| 6 | GoalId | GOAL_ID | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
