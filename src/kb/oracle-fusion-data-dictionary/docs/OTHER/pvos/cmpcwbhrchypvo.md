---
id: DOC-OTHER-PVO-CmpCwbHrchyPVO
doc_type: system-doc
title: "CmpCwbHrchyPVO — PVO Cross-Module"
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
  - CmpCwbHrchyPVO
  - cmpcwbhrchypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmpCwbHrchyPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cmp Cwb Hrchy. Acessa as tabelas: CMP_CWB_HRCHY_V.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.CompensationAM.CmpCwbHrchyPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 1 | 2 | 19 | 90% |

---

## 🔗 Tabelas Relacionadas

- [[cmp_cwb_hrchy_v|CMP_CWB_HRCHY_V]] — 21 atributos (2 PKs, 19 BICC)

---

## ⚙️ Atributos

### [[cmp_cwb_hrchy_v|CMP_CWB_HRCHY_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentId | ASSIGNMENT_ID | — | — |
| 2 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 3 | EmpAssignmentId | EMP_ASSIGNMENT_ID | — | ✅ |
| 4 | EmpPersonEventId | EMP_PERSON_EVENT_ID | 🔑 | ✅ |
| 5 | EmpPersonId | EMP_PERSON_ID | — | ✅ |
| 6 | HierarchyPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | HierarchyPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | HierarchyPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | HierarchyPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | HierarchyPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | HierarchyPEOLvlNum | LVL_NUM | — | ✅ |
| 12 | HierarchyPEONumberValue1 | NUMBER_VALUE1 | — | ✅ |
| 13 | HierarchyPEONumberValue2 | NUMBER_VALUE2 | — | ✅ |
| 14 | HierarchyPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | HierarchyPEOTextValue | TEXT_VALUE | — | ✅ |
| 16 | HrchyPeriodId | HRCHY_PERIOD_ID | — | ✅ |
| 17 | HrchyPlanId | HRCHY_PLAN_ID | — | ✅ |
| 18 | MgrAssignmentId | MGR_ASSIGNMENT_ID | — | ✅ |
| 19 | MgrPersonEventId | MGR_PERSON_EVENT_ID | 🔑 | ✅ |
| 20 | MgrPersonId | MGR_PERSON_ID | — | ✅ |
| 21 | PersonId | PERSON_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
