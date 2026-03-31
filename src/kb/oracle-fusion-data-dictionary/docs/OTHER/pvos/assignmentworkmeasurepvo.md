---
id: DOC-OTHER-PVO-AssignmentWorkMeasurePVO
doc_type: system-doc
title: "AssignmentWorkMeasurePVO — PVO Cross-Module"
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
  - AssignmentWorkMeasurePVO
  - assignmentworkmeasurepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssignmentWorkMeasurePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Assignment Work Measure. Acessa as tabelas: PER_ASSIGN_WORK_MEASURES_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AssignmentAM.AssignmentWorkMeasurePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 1 | 2 | 14 | 74% |

---

## 🔗 Tabelas Relacionadas

- [[per_assign_work_measures_f|PER_ASSIGN_WORK_MEASURES_F]] — 19 atributos (2 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[per_assign_work_measures_f|PER_ASSIGN_WORK_MEASURES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignWorkMeasureId | ASSIGN_WORK_MEASURE_ID | 🔑 | ✅ |
| 2 | AssignmentWorkMeasurePEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | ✅ |
| 3 | AssignmentWorkMeasurePEOAddsToBudget | ADDS_TO_BUDGET | — | — |
| 4 | AssignmentWorkMeasurePEOAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 5 | AssignmentWorkMeasurePEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 6 | AssignmentWorkMeasurePEOCalcWMFlag | CALCULATE_WORKMEASURE_FLAG | — | — |
| 7 | AssignmentWorkMeasurePEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | AssignmentWorkMeasurePEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | AssignmentWorkMeasurePEOFreezeStartDate | FREEZE_START_DATE | — | ✅ |
| 10 | AssignmentWorkMeasurePEOFreezeUntilDate | FREEZE_UNTIL_DATE | — | ✅ |
| 11 | AssignmentWorkMeasurePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | AssignmentWorkMeasurePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | AssignmentWorkMeasurePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | AssignmentWorkMeasurePEOLegislationCode | LEGISLATION_CODE | — | — |
| 15 | AssignmentWorkMeasurePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | AssignmentWorkMeasurePEOUnit | UNIT | — | ✅ |
| 17 | AssignmentWorkMeasurePEOValue | VALUE | — | ✅ |
| 18 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 19 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
