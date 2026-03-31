---
id: DOC-OTHER-PVO-PerAssignHeadCountPVO
doc_type: system-doc
title: "PerAssignHeadCountPVO — PVO Cross-Module"
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
  - PerAssignHeadCountPVO
  - perassignheadcountpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PerAssignHeadCountPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Per Assign Head Count. Acessa as tabelas: PER_ASSIGN_WORK_MEASURES_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AssignmentAM.PerAssignHeadCountPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 3 | 5 | 29% |

---

## 🔗 Tabelas Relacionadas

- [[per_assign_work_measures_f|PER_ASSIGN_WORK_MEASURES_F]] — 17 atributos (3 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[per_assign_work_measures_f|PER_ASSIGN_WORK_MEASURES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignWorkMeasureId | ASSIGN_WORK_MEASURE_ID | 🔑 | ✅ |
| 2 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 3 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 4 | PerAssignHeadCountPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 5 | PerAssignHeadCountPEOAddsToBudget | ADDS_TO_BUDGET | — | — |
| 6 | PerAssignHeadCountPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 7 | PerAssignHeadCountPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 8 | PerAssignHeadCountPEOCreatedBy | CREATED_BY | — | — |
| 9 | PerAssignHeadCountPEOCreationDate | CREATION_DATE | — | — |
| 10 | PerAssignHeadCountPEOFreezeStartDate | FREEZE_START_DATE | — | — |
| 11 | PerAssignHeadCountPEOFreezeUntilDate | FREEZE_UNTIL_DATE | — | — |
| 12 | PerAssignHeadCountPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | PerAssignHeadCountPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | PerAssignHeadCountPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | PerAssignHeadCountPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | PerAssignHeadCountPEOUnit | UNIT | — | — |
| 17 | PerAssignHeadCountPEOValue | VALUE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
