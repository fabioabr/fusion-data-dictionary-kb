---
id: DOC-OTHER-PVO-RouteStepsExtractPVO
doc_type: system-doc
title: "RouteStepsExtractPVO — PVO Cross-Module"
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
  - RouteStepsExtractPVO
  - routestepsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RouteStepsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Route Steps Extract. Acessa as tabelas: EGO_ROUTE_STEPS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgoBiccExtractAM.RouteStepsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 1 | 1 | 30 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ego_route_steps|EGO_ROUTE_STEPS]] — 30 atributos (1 PKs, 30 BICC)

---

## ⚙️ Atributos

### [[ego_route_steps|EGO_ROUTE_STEPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RouteStepsPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | RouteStepsPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | RouteStepsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | RouteStepsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | RouteStepsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | RouteStepsPEOObjectName | OBJECT_NAME | — | ✅ |
| 7 | RouteStepsPEOObjectPk1 | OBJECT_PK1 | — | ✅ |
| 8 | RouteStepsPEOObjectPk2 | OBJECT_PK2 | — | ✅ |
| 9 | RouteStepsPEOObjectPk3 | OBJECT_PK3 | — | ✅ |
| 10 | RouteStepsPEOObjectPk4 | OBJECT_PK4 | — | ✅ |
| 11 | RouteStepsPEOObjectPk5 | OBJECT_PK5 | — | ✅ |
| 12 | RouteStepsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | RouteStepsPEOResponseRequiredFrom | RESPONSE_REQUIRED_FROM | — | ✅ |
| 14 | RouteStepsPEORouteId | ROUTE_ID | — | ✅ |
| 15 | RouteStepsPEORulesSupported | RULES_SUPPORTED | — | ✅ |
| 16 | RouteStepsPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 17 | RouteStepsPEOSkipFlag | SKIP_FLAG | — | ✅ |
| 18 | RouteStepsPEOStepActivityType | STEP_ACTIVITY_TYPE | — | ✅ |
| 19 | RouteStepsPEOStepEndDate | STEP_END_DATE | — | ✅ |
| 20 | RouteStepsPEOStepId | STEP_ID | 🔑 | ✅ |
| 21 | RouteStepsPEOStepSeqNumber | STEP_SEQ_NUMBER | — | ✅ |
| 22 | RouteStepsPEOStepStartDate | STEP_START_DATE | — | ✅ |
| 23 | RouteStepsPEOStepStatusCode | STEP_STATUS_CODE | — | ✅ |
| 24 | RouteStepsPEOTaskCompleteTime | TASK_COMPLETE_TIME | — | ✅ |
| 25 | RouteStepsPEOTaskRoutingSlipListBuilder | TASK_ROUTING_SLIP_LIST_BUILDER | — | ✅ |
| 26 | RouteStepsPEOTaskStageType | TASK_STAGE_TYPE | — | ✅ |
| 27 | RouteStepsPEOTaskStartTime | TASK_START_TIME | — | ✅ |
| 28 | RouteStepsPEOUserDefinedSupported | USER_DEFINED_SUPPORTED | — | ✅ |
| 29 | RouteStepsPEOWebServiceSupported | WEB_SERVICE_SUPPORTED | — | ✅ |
| 30 | RouteStepsPEOWorkflowInstanceId | WORKFLOW_INSTANCE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
