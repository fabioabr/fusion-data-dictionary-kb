---
id: DOC-HCM-PVO-CompPlanSecured
doc_type: system-doc
title: "CompPlanSecured — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - CompPlanSecured
  - compplansecured
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CompPlanSecured

## 📌 Visão Geral

Planos de compensacao de incentivos com seguranca por unidade de negocio. Versao com filtros de acesso para consultas restritas por BU.

**Caminho:** `FscmTopModelAM.CompensationPlanAM.CompPlanSecured`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 3 | 1 | 18 | 82% |

---

## 🔗 Tabelas Relacionadas

- [[cn_comp_plans_all_b|CN_COMP_PLANS_ALL_B]] — 14 atributos (1 PKs, 12 BICC)
- [[cn_comp_plans_all_tl|CN_COMP_PLANS_ALL_TL]] — 6 atributos (5 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 2 atributos (1 BICC)

---

## ⚙️ Atributos

### [[cn_comp_plans_all_b|CN_COMP_PLANS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllowEcatOverlapFlag | ALLOW_ECAT_OVERLAP_FLAG | — | ✅ |
| 2 | ApprovalStatus | APPROVAL_STATUS | — | ✅ |
| 3 | CompPlanId | COMP_PLAN_ID | 🔑 | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | EndDate | END_DATE | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | OrgId | ORG_ID | — | — |
| 12 | PlanStatus | PLAN_STATUS | — | ✅ |
| 13 | StartDate | START_DATE | — | ✅ |
| 14 | TargetIncentive | TARGET_INCENTIVE | — | ✅ |

### [[cn_comp_plans_all_tl|CN_COMP_PLANS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CompPlanId1 | COMP_PLAN_ID | — | ✅ |
| 2 | CompPlanName | COMP_PLAN_NAME | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | DisplayName | DISPLAY_NAME | — | ✅ |
| 5 | Language | LANGUAGE | — | ✅ |
| 6 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitId | BU_ID | — | — |
| 2 | Name | BU_NAME | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
