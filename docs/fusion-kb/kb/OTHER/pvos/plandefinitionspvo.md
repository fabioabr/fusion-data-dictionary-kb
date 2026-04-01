---
id: DOC-OTHER-PVO-PlanDefinitionsPVO
doc_type: system-doc
title: "PlanDefinitionsPVO — PVO Cross-Module"
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
  - PlanDefinitionsPVO
  - plandefinitionspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlanDefinitionsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Plan Definitions. Acessa as tabelas: CMP_CWB_PLAN_DEFINITIONS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.CompensationAM.PlanDefinitionsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 1 | 2 | 23 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmp_cwb_plan_definitions|CMP_CWB_PLAN_DEFINITIONS]] — 23 atributos (2 PKs, 23 BICC)

---

## ⚙️ Atributos

### [[cmp_cwb_plan_definitions|CMP_CWB_PLAN_DEFINITIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 2 | PlanDefinitionId | PLAN_DEFINITION_ID | — | ✅ |
| 3 | PlanDefinitionsPEOApprovalMode | APPROVAL_MODE | — | ✅ |
| 4 | PlanDefinitionsPEOBudgetingStyle | BUDGETING_STYLE | — | ✅ |
| 5 | PlanDefinitionsPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 6 | PlanDefinitionsPEOComponentId | COMPONENT_ID | — | ✅ |
| 7 | PlanDefinitionsPEOCorporateCurrency | CORPORATE_CURRENCY | — | ✅ |
| 8 | PlanDefinitionsPEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | PlanDefinitionsPEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | PlanDefinitionsPEODefinitionType | DEFINITION_TYPE | — | ✅ |
| 11 | PlanDefinitionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | PlanDefinitionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | PlanDefinitionsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | PlanDefinitionsPEOOrderNum | ORDER_NUM | — | ✅ |
| 15 | PlanDefinitionsPEOPeriodId | PERIOD_ID | 🔑 | ✅ |
| 16 | PlanDefinitionsPEOPlanComponentCount | PLAN_COMPONENT_COUNT | — | ✅ |
| 17 | PlanDefinitionsPEOPlanId | PLAN_ID | 🔑 | ✅ |
| 18 | PlanDefinitionsPEOPoolComponentId | POOL_COMPONENT_ID | — | ✅ |
| 19 | PlanDefinitionsPEOPoolId | POOL_ID | — | ✅ |
| 20 | PlanDefinitionsPEOPostAsSalaryFlag | POST_AS_SALARY_FLAG | — | ✅ |
| 21 | PlanDefinitionsPEOStatusCode | STATUS_CODE | — | ✅ |
| 22 | PlanDefinitionsPEOSubmitMode | SUBMIT_MODE | — | ✅ |
| 23 | PlanDefinitionsPEOSystemOrderNum | SYSTEM_ORDER_NUM | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
