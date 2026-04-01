---
id: DOC-OTHER-PVO-RoutePeopleExtractPVO
doc_type: system-doc
title: "RoutePeopleExtractPVO — PVO Cross-Module"
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
  - RoutePeopleExtractPVO
  - routepeopleextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RoutePeopleExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Route People Extract. Acessa as tabelas: EGO_ROUTE_PEOPLE_BI_V.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgoBiccExtractAM.RoutePeopleExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 1 | 1 | 26 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ego_route_people_bi_v|EGO_ROUTE_PEOPLE_BI_V]] — 26 atributos (1 PKs, 26 BICC)

---

## ⚙️ Atributos

### [[ego_route_people_bi_v|EGO_ROUTE_PEOPLE_BI_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RoutePeoplePEOAdhocPeopleFlag | ADHOC_PEOPLE_FLAG | — | ✅ |
| 2 | RoutePeoplePEOAssigneeId | ASSIGNEE_ID | — | ✅ |
| 3 | RoutePeoplePEOAssigneeTypeCode | ASSIGNEE_TYPE_CODE | — | ✅ |
| 4 | RoutePeoplePEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | RoutePeoplePEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | RoutePeoplePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | RoutePeoplePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | RoutePeoplePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | RoutePeoplePEOObjectName | OBJECT_NAME | — | ✅ |
| 10 | RoutePeoplePEOObjectPk1 | OBJECT_PK1 | — | ✅ |
| 11 | RoutePeoplePEOObjectPk2 | OBJECT_PK2 | — | ✅ |
| 12 | RoutePeoplePEOObjectPk3 | OBJECT_PK3 | — | ✅ |
| 13 | RoutePeoplePEOObjectPk4 | OBJECT_PK4 | — | ✅ |
| 14 | RoutePeoplePEOObjectPk5 | OBJECT_PK5 | — | ✅ |
| 15 | RoutePeoplePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | RoutePeoplePEOOriginalAssigneeId | ORIGINAL_ASSIGNEE_ID | — | ✅ |
| 17 | RoutePeoplePEOOriginalAssigneeType | ORIGINAL_ASSIGNEE_TYPE | — | ✅ |
| 18 | RoutePeoplePEOReassignedTo | REASSIGNED_TO | — | ✅ |
| 19 | RoutePeoplePEOResponseCode | RESPONSE_CODE | — | ✅ |
| 20 | RoutePeoplePEOResponseDate | RESPONSE_DATE | — | ✅ |
| 21 | RoutePeoplePEOResponseRequiredFrom | RESPONSE_REQUIRED_FROM | — | ✅ |
| 22 | RoutePeoplePEORoutePeopleId | ROUTE_PEOPLE_ID | 🔑 | ✅ |
| 23 | RoutePeoplePEOStepId | STEP_ID | — | ✅ |
| 24 | RoutePeoplePEOTaskCompleteTime | TASK_COMPLETE_TIME | — | ✅ |
| 25 | RoutePeoplePEOTaskStartTime | TASK_START_TIME | — | ✅ |
| 26 | RoutePeoplePEOWfSubtaskInstanceId | WF_SUBTASK_INSTANCE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
