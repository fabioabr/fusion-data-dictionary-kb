---
id: DOC-HCM-PVO-LaborDemandPVO
doc_type: system-doc
title: "LaborDemandPVO — PVO Human Capital Management"
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
  - LaborDemandPVO
  - labordemandpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LaborDemandPVO

## 📌 Visão Geral

Disponibiliza demanda de mão de obra com perfil de escalonamento e recursos necessários. Utilizado para planejamento de workforce e scheduling.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmDemandAM.LaborDemandPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 5 | 3 | 5 | 31% |

---

## 🔗 Tabelas Relacionadas

- [[hts_labor_demand_view|HTS_LABOR_DEMAND_VIEW]] — 3 atributos (2 PKs, 3 BICC)
- [[hwm_grp_incl_members_view|HWM_GRP_INCL_MEMBERS_VIEW]] — 3 atributos
- [[hxt_setup_option_vals|HXT_SETUP_OPTION_VALS]] — 3 atributos (1 BICC)
- [[hxt_setup_profiles_vl|HXT_SETUP_PROFILES_VL]] — 2 atributos
- [[hxt_setup_profile_asgs|HXT_SETUP_PROFILE_ASGS]] — 5 atributos (1 PKs, 1 BICC)

---

## ⚙️ Atributos

### [[hts_labor_demand_view|HTS_LABOR_DEMAND_VIEW]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DemandDate | DEMAND_DATE | 🔑 | ✅ |
| 2 | ResourcesRequired | RESOURCES_REQUIRED | — | ✅ |
| 3 | SchedulerProfileId | SCHEDULER_PROFILE_ID | 🔑 | ✅ |

### [[hwm_grp_incl_members_view|HWM_GRP_INCL_MEMBERS_VIEW]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GrpId | GRP_ID | — | — |
| 2 | GrpInclMemberId | GRP_INCL_MEMBER_ID | — | — |
| 3 | InclMemberId | INCL_MEMBER_ID | — | — |

### [[hxt_setup_option_vals|HXT_SETUP_OPTION_VALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | SetupOptionValId | SETUP_OPTION_VAL_ID | — | — |

### [[hxt_setup_profiles_vl|HXT_SETUP_PROFILES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProductArea | PRODUCT_AREA | — | — |
| 2 | SetupProfileId | SETUP_PROFILE_ID | — | — |

### [[hxt_setup_profile_asgs|HXT_SETUP_PROFILE_ASGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignTo | ASSIGN_TO | — | — |
| 2 | DateFrom | DATE_FROM | — | — |
| 3 | DateTo | DATE_TO | — | — |
| 4 | ObjectId | OBJECT_ID | — | — |
| 5 | SetupProfileAsgId | SETUP_PROFILE_ASG_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
