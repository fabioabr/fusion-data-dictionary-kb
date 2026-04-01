---
id: DOC-OTHER-PVO-PlanComponent
doc_type: system-doc
title: "PlanComponent — PVO Cross-Module"
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
  - PlanComponent
  - plancomponent
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlanComponent

## 📌 Visão Geral

View Object para extração BICC de dados de Plan Component. Acessa as tabelas: CN_PLAN_COMPONENTS_ALL_B, CN_PLAN_COMPONENTS_ALL_TL, FUN_ALL_BUSINESS_UNITS_V.

**Caminho:** `FscmTopModelAM.CompensationPlanAM.PlanComponent`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 35 | 3 | 2 | 29 | 83% |

---

## 🔗 Tabelas Relacionadas

- [[cn_plan_components_all_b|CN_PLAN_COMPONENTS_ALL_B]] — 26 atributos (2 PKs, 24 BICC)
- [[cn_plan_components_all_tl|CN_PLAN_COMPONENTS_ALL_TL]] — 7 atributos (4 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 2 atributos (1 BICC)

---

## ⚙️ Atributos

### [[cn_plan_components_all_b|CN_PLAN_COMPONENTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApExpId | AP_EXP_ID | — | ✅ |
| 2 | ApLiabId | AP_LIAB_ID | — | ✅ |
| 3 | ApprovalStatus | APPROVAL_STATUS | — | ✅ |
| 4 | CalcVariableId | CALC_VARIABLE_ID | — | — |
| 5 | CalculationPhase | CALCULATION_PHASE | — | ✅ |
| 6 | CreatedBy | CREATED_BY | — | ✅ |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 9 | DeleteFlag | DELETE_FLAG | — | ✅ |
| 10 | EarningTypeId | EARNING_TYPE_ID | — | ✅ |
| 11 | EndDate | END_DATE | — | ✅ |
| 12 | IncentiveType | INCENTIVE_TYPE | — | ✅ |
| 13 | IncrementalType | INCREMENTAL_TYPE | — | ✅ |
| 14 | IndirectCredit | INDIRECT_CREDIT | — | ✅ |
| 15 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | OrgId | ORG_ID | 🔑 | ✅ |
| 20 | PaymentGroupCode | PAYMENT_GROUP_CODE | — | ✅ |
| 21 | PlanCompStatus | PLAN_COMP_STATUS | — | ✅ |
| 22 | PlanComponentId | PLAN_COMPONENT_ID | 🔑 | ✅ |
| 23 | ReportGroup | REPORT_GROUP | — | ✅ |
| 24 | SalesrepEnddatedFlag | SALESREP_ENDDATED_FLAG | — | ✅ |
| 25 | StartDate | START_DATE | — | ✅ |
| 26 | ThirdpartyPayeeFlag | THIRDPARTY_PAYEE_FLAG | — | ✅ |

### [[cn_plan_components_all_tl|CN_PLAN_COMPONENTS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | ✅ |
| 2 | DisplayName | DISPLAY_NAME | — | ✅ |
| 3 | Language | LANGUAGE | — | ✅ |
| 4 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 5 | OrgId1 | ORG_ID | — | — |
| 6 | PlanComponentId1 | PLAN_COMPONENT_ID | — | — |
| 7 | PlanComponentName | PLAN_COMPONENT_NAME | — | ✅ |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitId | BU_ID | — | — |
| 2 | Name | BU_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
