---
id: DOC-OTHER-PVO-AssignmentGradeStepPVO
doc_type: system-doc
title: "AssignmentGradeStepPVO — PVO Cross-Module"
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
  - AssignmentGradeStepPVO
  - assignmentgradesteppvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssignmentGradeStepPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Assignment Grade Step. Acessa as tabelas: PER_ASSIGN_GRADE_STEPS_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AssignmentAM.AssignmentGradeStepPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 1 | 3 | 20 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[per_assign_grade_steps_f|PER_ASSIGN_GRADE_STEPS_F]] — 20 atributos (3 PKs, 20 BICC)

---

## ⚙️ Atributos

### [[per_assign_grade_steps_f|PER_ASSIGN_GRADE_STEPS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignGradeStepId | ASSIGN_GRADE_STEP_ID | 🔑 | ✅ |
| 2 | AssignmentGradeStepPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | ✅ |
| 3 | AssignmentGradeStepPEOAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 4 | AssignmentGradeStepPEOAutoIncrementFlag | AUTO_INCREMENT_FLAG | — | ✅ |
| 5 | AssignmentGradeStepPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 6 | AssignmentGradeStepPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | AssignmentGradeStepPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | AssignmentGradeStepPEOGradeStepId | GRADE_STEP_ID | — | ✅ |
| 9 | AssignmentGradeStepPEOIncrementNumber | INCREMENT_NUMBER | — | ✅ |
| 10 | AssignmentGradeStepPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 11 | AssignmentGradeStepPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 12 | AssignmentGradeStepPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | AssignmentGradeStepPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | AssignmentGradeStepPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | AssignmentGradeStepPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | AssignmentGradeStepPEOPayScaleId | PAY_SCALE_ID | — | ✅ |
| 17 | AssignmentGradeStepPEOReason | REASON | — | ✅ |
| 18 | AssignmentGradeStepPEORequestId | REQUEST_ID | — | ✅ |
| 19 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 20 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
