---
id: DOC-OTHER-PVO-PjsRbsElementsCFP1
doc_type: system-doc
title: "PjsRbsElementsCFP1 — PVO Cross-Module"
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
  - PjsRbsElementsCFP1
  - pjsrbselementscfp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PjsRbsElementsCFP1

## 📌 Visão Geral

View Object para extração BICC de dados de Pjs Rbs Elements CFP1. Acessa as tabelas: PJF_PROJECTS_ALL_B, PJF_RBS_ELEMENTS_VL, PJF_RBS_ELEMENT_NAMES_VL (+2).

**Caminho:** `FscmTopModelAM.PjsProjectPerformanceAM.PjsRbsElementsCFP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 54 | 5 | 2 | 39 | 72% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 1 atributos
- [[pjf_rbs_elements_vl|PJF_RBS_ELEMENTS_VL]] — 22 atributos (21 BICC)
- [[pjf_rbs_element_names_vl|PJF_RBS_ELEMENT_NAMES_VL]] — 22 atributos (11 BICC)
- [[pjf_rbs_prj_assignments|PJF_RBS_PRJ_ASSIGNMENTS]] — 6 atributos (4 BICC)
- [[pjs_rbs_elements_cf|PJS_RBS_ELEMENTS_CF]] — 3 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectBasePEOProjectId | PROJECT_ID | — | — |

### [[pjf_rbs_elements_vl|PJF_RBS_ELEMENTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Node0RbsPEOOutlineNumber | OUTLINE_NUMBER | — | ✅ |
| 2 | Node0RbsPEORbsElementId | RBS_ELEMENT_ID | — | — |
| 3 | Node10RbsPEOOutlineNumber | OUTLINE_NUMBER | — | ✅ |
| 4 | Node10RbsPEORbsElementId | RBS_ELEMENT_ID | — | ✅ |
| 5 | Node1RbsPEOOutlineNumber | OUTLINE_NUMBER | — | ✅ |
| 6 | Node1RbsPEORbsElementId | RBS_ELEMENT_ID | — | ✅ |
| 7 | Node2RbsPEOOutlineNumber | OUTLINE_NUMBER | — | ✅ |
| 8 | Node2RbsPEORbsElementId | RBS_ELEMENT_ID | — | ✅ |
| 9 | Node3RbsPEOOutlineNumber | OUTLINE_NUMBER | — | ✅ |
| 10 | Node3RbsPEORbsElementId | RBS_ELEMENT_ID | — | ✅ |
| 11 | Node4RbsPEOOutlineNumber | OUTLINE_NUMBER | — | ✅ |
| 12 | Node4RbsPEORbsElementId | RBS_ELEMENT_ID | — | ✅ |
| 13 | Node5RbsPEOOutlineNumber | OUTLINE_NUMBER | — | ✅ |
| 14 | Node5RbsPEORbsElementId | RBS_ELEMENT_ID | — | ✅ |
| 15 | Node6RbsPEOOutlineNumber | OUTLINE_NUMBER | — | ✅ |
| 16 | Node6RbsPEORbsElementId | RBS_ELEMENT_ID | — | ✅ |
| 17 | Node7RbsPEOOutlineNumber | OUTLINE_NUMBER | — | ✅ |
| 18 | Node7RbsPEORbsElementId | RBS_ELEMENT_ID | — | ✅ |
| 19 | Node8RbsPEOOutlineNumber | OUTLINE_NUMBER | — | ✅ |
| 20 | Node8RbsPEORbsElementId | RBS_ELEMENT_ID | — | ✅ |
| 21 | Node9RbsPEOOutlineNumber | OUTLINE_NUMBER | — | ✅ |
| 22 | Node9RbsPEORbsElementId | RBS_ELEMENT_ID | — | ✅ |

### [[pjf_rbs_element_names_vl|PJF_RBS_ELEMENT_NAMES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Node0RbsElemNamePEOName | NAME | — | ✅ |
| 2 | Node0RbsElemNamePEONameId | RBS_ELEMENT_NAME_ID | — | — |
| 3 | Node10RbsElemNamePEOName | NAME | — | ✅ |
| 4 | Node10RbsElemNamePEONameId | RBS_ELEMENT_NAME_ID | — | — |
| 5 | Node1RbsElemNamePEOName | NAME | — | ✅ |
| 6 | Node1RbsElemNamePEONameId | RBS_ELEMENT_NAME_ID | — | — |
| 7 | Node2RbsElemNamePEOName | NAME | — | ✅ |
| 8 | Node2RbsElemNamePEONameId | RBS_ELEMENT_NAME_ID | — | — |
| 9 | Node3RbsElemNamePEOName | NAME | — | ✅ |
| 10 | Node3RbsElemNamePEONameId | RBS_ELEMENT_NAME_ID | — | — |
| 11 | Node4RbsElemNamePEOName | NAME | — | ✅ |
| 12 | Node4RbsElemNamePEONameId | RBS_ELEMENT_NAME_ID | — | — |
| 13 | Node5RbsElemNamePEOName | NAME | — | ✅ |
| 14 | Node5RbsElemNamePEONameId | RBS_ELEMENT_NAME_ID | — | — |
| 15 | Node6RbsElemNamePEOName | NAME | — | ✅ |
| 16 | Node6RbsElemNamePEONameId | RBS_ELEMENT_NAME_ID | — | — |
| 17 | Node7RbsElemNamePEOName | NAME | — | ✅ |
| 18 | Node7RbsElemNamePEONameId | RBS_ELEMENT_NAME_ID | — | — |
| 19 | Node8RbsElemNamePEOName | NAME | — | ✅ |
| 20 | Node8RbsElemNamePEONameId | RBS_ELEMENT_NAME_ID | — | — |
| 21 | Node9RbsElemNamePEOName | NAME | — | ✅ |
| 22 | Node9RbsElemNamePEONameId | RBS_ELEMENT_NAME_ID | — | — |

### [[pjf_rbs_prj_assignments|PJF_RBS_PRJ_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RbsAssignPEOPlanningUsageFlag | PLANNING_USAGE_FLAG | — | ✅ |
| 2 | RbsAssignPEOPrimaryPlanRbsFlag | PRIMARY_PLANNING_RBS_FLAG | — | ✅ |
| 3 | RbsAssignPEOPrimaryReprtRbsFlag | PRIMARY_REPORTING_RBS_FLAG | — | ✅ |
| 4 | RbsAssignPEORbsHeaderId | RBS_HEADER_ID | — | — |
| 5 | RbsAssignPEORbsPrjAssignmentId | RBS_PRJ_ASSIGNMENT_ID | — | — |
| 6 | RbsAssignPEOReportingUsageFlag | REPORTING_USAGE_FLAG | — | ✅ |

### [[pjs_rbs_elements_cf|PJS_RBS_ELEMENTS_CF]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NodeIdLevel0 | NODE_ID_LEVEL_0 | 🔑 | ✅ |
| 2 | PjsRbsElemCFPEODistance | DISTANCE | — | ✅ |
| 3 | RbsVersionId | RBS_VERSION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
