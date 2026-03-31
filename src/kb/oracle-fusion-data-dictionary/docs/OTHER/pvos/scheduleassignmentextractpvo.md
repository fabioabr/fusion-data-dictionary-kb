---
id: DOC-OTHER-PVO-ScheduleAssignmentExtractPVO
doc_type: system-doc
title: "ScheduleAssignmentExtractPVO — PVO Cross-Module"
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
  - ScheduleAssignmentExtractPVO
  - scheduleassignmentextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ScheduleAssignmentExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Schedule Assignment Extract. Acessa as tabelas: PER_SCHEDULE_ASSIGNMENTS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.WorkScheduleBiccExtractAM.ScheduleAssignmentExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[per_schedule_assignments|PER_SCHEDULE_ASSIGNMENTS]] — 15 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[per_schedule_assignments|PER_SCHEDULE_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | EndDate | END_DATE | — | ✅ |
| 4 | EnterpriseId | ENTERPRISE_ID | — | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | PrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 10 | ResourceId | RESOURCE_ID | — | ✅ |
| 11 | ResourceType | RESOURCE_TYPE | — | ✅ |
| 12 | ScheduleAssignmentId | SCHEDULE_ASSIGNMENT_ID | 🔑 | ✅ |
| 13 | ScheduleId | SCHEDULE_ID | — | ✅ |
| 14 | StartDate | START_DATE | — | ✅ |
| 15 | StartPatternDtlId | START_PATTERN_DTL_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
