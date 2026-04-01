---
id: DOC-OTHER-PVO-PjtResourcesPVO
doc_type: system-doc
title: "PjtResourcesPVO — PVO Cross-Module"
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
  - PjtResourcesPVO
  - pjtresourcespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PjtResourcesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Pjt Resources. Acessa as tabelas: PER_PERSON_NAMES_F_V, PJF_RES_TYPES_VL, PJR_RESOURCE_POOLS_VL (+5).

**Caminho:** `FscmTopModelAM.PjtResourcesAM.PjtResourcesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 39 | 8 | 1 | 28 | 72% |

---

## 🔗 Tabelas Relacionadas

- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 5 atributos (1 BICC)
- [[pjf_res_types_vl|PJF_RES_TYPES_VL]] — 3 atributos (2 BICC)
- [[pjr_resource_pools_vl|PJR_RESOURCE_POOLS_VL]] — 2 atributos (2 BICC)
- [[pjr_resource_pool_assignments|PJR_RESOURCE_POOL_ASSIGNMENTS]] — 2 atributos (1 BICC)
- [[pjt_prj_enterprise_resource_b|PJT_PRJ_ENTERPRISE_RESOURCE_B]] — 17 atributos (1 PKs, 15 BICC)
- [[pjt_prj_enterprise_resource_tl|PJT_PRJ_ENTERPRISE_RESOURCE_TL]] — 6 atributos (3 BICC)
- [[pjt_project_roles_vl|PJT_PROJECT_ROLES_VL]] — 2 atributos (2 BICC)
- [[pjt_schedules_vl|PJT_SCHEDULES_VL]] — 2 atributos (2 BICC)

---

## ⚙️ Atributos

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNameDPEODisplayName | DISPLAY_NAME | — | — |
| 2 | PersonNameDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonNameDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | PersonNameDPEOPersonId | PERSON_ID | — | — |
| 5 | PersonNameDPEOPersonNameId | PERSON_NAME_ID | — | — |

### [[pjf_res_types_vl|PJF_RES_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectResourceTypePEODescription | DESCRIPTION | — | — |
| 2 | ProjectResourceTypePEOName | NAME | — | ✅ |
| 3 | ProjectResourceTypePEOResTypeId | RES_TYPE_ID | — | ✅ |

### [[pjr_resource_pools_vl|PJR_RESOURCE_POOLS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResourcePoolPEOName | NAME | — | ✅ |
| 2 | ResourcePoolPEOPoolId | POOL_ID | — | ✅ |

### [[pjr_resource_pool_assignments|PJR_RESOURCE_POOL_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResourcePoolAssignmentPEOPoolAssignmentId | POOL_ASSIGNMENT_ID | — | — |
| 2 | ResourcePoolAssignmentPEOPoolId | POOL_ID | — | ✅ |

### [[pjt_prj_enterprise_resource_b|PJT_PRJ_ENTERPRISE_RESOURCE_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrjEnterpriseResourceBasePEO1Email | EMAIL | — | ✅ |
| 2 | PrjEnterpriseResourceBasePEO1ResourceId | RESOURCE_ID | — | — |
| 3 | PrjEnterpriseResourceBasePEOBillRate | BILL_RATE | — | ✅ |
| 4 | PrjEnterpriseResourceBasePEOBillRateCurrencyCode | BILL_RATE_CURRENCY_CODE | — | ✅ |
| 5 | PrjEnterpriseResourceBasePEOCostRate | COST_RATE | — | ✅ |
| 6 | PrjEnterpriseResourceBasePEOCostRateCurrencyCode | COST_RATE_CURRENCY_CODE | — | ✅ |
| 7 | PrjEnterpriseResourceBasePEOEmail | EMAIL | — | ✅ |
| 8 | PrjEnterpriseResourceBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 9 | PrjEnterpriseResourceBasePEOFirstName | FIRST_NAME | — | ✅ |
| 10 | PrjEnterpriseResourceBasePEOLastName | LAST_NAME | — | ✅ |
| 11 | PrjEnterpriseResourceBasePEOPersonId | PERSON_ID | — | ✅ |
| 12 | PrjEnterpriseResourceBasePEOProjectRoleId | PROJECT_ROLE_ID | — | ✅ |
| 13 | PrjEnterpriseResourceBasePEOResMgmtFlag | RES_MGMT_FLAG | — | ✅ |
| 14 | PrjEnterpriseResourceBasePEOResourceClass | RESOURCE_CLASS | — | — |
| 15 | PrjEnterpriseResourceBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 16 | PrjEnterpriseResourceBasePEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 17 | ResourceId | RESOURCE_ID | 🔑 | ✅ |

### [[pjt_prj_enterprise_resource_tl|PJT_PRJ_ENTERPRISE_RESOURCE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrjEnterpriseResourceTLPEO1DisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PrjEnterpriseResourceTLPEO1Language | LANGUAGE | — | — |
| 3 | PrjEnterpriseResourceTLPEO1ResourceId | RESOURCE_ID | — | ✅ |
| 4 | PrjEnterpriseResourceTLPEODisplayName | DISPLAY_NAME | — | ✅ |
| 5 | PrjEnterpriseResourceTLPEOLanguage | LANGUAGE | — | — |
| 6 | PrjEnterpriseResourceTLPEOResourceId | RESOURCE_ID | — | — |

### [[pjt_project_roles_vl|PJT_PROJECT_ROLES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectRolePEOName | NAME | — | ✅ |
| 2 | ProjectRolePEOProjectRoleId | PROJECT_ROLE_ID | — | ✅ |

### [[pjt_schedules_vl|PJT_SCHEDULES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjtSchedulesPEOScheduleId | SCHEDULE_ID | — | ✅ |
| 2 | PjtSchedulesPEOScheduleName | SCHEDULE_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
