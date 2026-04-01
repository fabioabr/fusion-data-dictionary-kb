---
id: DOC-OTHER-PVO-PerAssignFTECountPVO
doc_type: system-doc
title: "PerAssignFTECountPVO — PVO Cross-Module"
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
  - PerAssignFTECountPVO
  - perassignftecountpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PerAssignFTECountPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Per Assign FTECount. Acessa as tabelas: PER_ASSIGN_WORK_MEASURES_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AssignmentAM.PerAssignFTECountPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 3 | 7 | 39% |

---

## 🔗 Tabelas Relacionadas

- [[per_assign_work_measures_f|PER_ASSIGN_WORK_MEASURES_F]] — 18 atributos (3 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[per_assign_work_measures_f|PER_ASSIGN_WORK_MEASURES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignWorkMeasureId | ASSIGN_WORK_MEASURE_ID | 🔑 | ✅ |
| 2 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 3 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 4 | PerAssignFTECountPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 5 | PerAssignFTECountPEOAddsToBudget | ADDS_TO_BUDGET | — | — |
| 6 | PerAssignFTECountPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 7 | PerAssignFTECountPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 8 | PerAssignFTECountPEOCalcWMFlag | CALCULATE_WORKMEASURE_FLAG | — | ✅ |
| 9 | PerAssignFTECountPEOCreatedBy | CREATED_BY | — | ✅ |
| 10 | PerAssignFTECountPEOCreationDate | CREATION_DATE | — | — |
| 11 | PerAssignFTECountPEOFreezeStartDate | FREEZE_START_DATE | — | — |
| 12 | PerAssignFTECountPEOFreezeUntilDate | FREEZE_UNTIL_DATE | — | — |
| 13 | PerAssignFTECountPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | PerAssignFTECountPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | PerAssignFTECountPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | PerAssignFTECountPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | PerAssignFTECountPEOUnit | UNIT | — | — |
| 18 | PerAssignFTECountPEOValue | VALUE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
