---
id: DOC-OTHER-PVO-SchedulerProfileOptionPVO
doc_type: system-doc
title: "SchedulerProfileOptionPVO — PVO Cross-Module"
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
  - SchedulerProfileOptionPVO
  - schedulerprofileoptionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SchedulerProfileOptionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Scheduler Profile Option. Acessa as tabelas: HXT_SCH_PROF_DEFAULT_VIEW, PER_ALL_PEOPLE_F, PER_PERSON_NAMES_F_V.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.SetupOptionsAM.SchedulerProfileOptionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 40 | 3 | 4 | 22 | 55% |

---

## 🔗 Tabelas Relacionadas

- [[hxt_sch_prof_default_view|HXT_SCH_PROF_DEFAULT_VIEW]] — 32 atributos (4 PKs, 18 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 4 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 4 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hxt_sch_prof_default_view|HXT_SCH_PROF_DEFAULT_VIEW]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreatedBy1 | CREATED_BY1 | — | — |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | CreationDate1 | CREATION_DATE1 | — | — |
| 5 | DateFrom | DATE_FROM | — | — |
| 6 | DateTo | DATE_TO | — | — |
| 7 | Description | DESCRIPTION | — | ✅ |
| 8 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 9 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 10 | FirstDayOfWeek | FIRST_DAY_OF_WEEK | — | — |
| 11 | GroupManagerId | GROUP_MANAGER_ID | — | ✅ |
| 12 | GrpId | GRP_ID | — | — |
| 13 | GrpInclMemberId | GRP_INCL_MEMBER_ID | — | — |
| 14 | InclMemberId | INCL_MEMBER_ID | — | — |
| 15 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | LastUpdateDate1 | LAST_UPDATE_DATE1 | — | ✅ |
| 17 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 18 | LastUpdateLogin1 | LAST_UPDATE_LOGIN1 | — | — |
| 19 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 20 | LastUpdatedBy1 | LAST_UPDATED_BY1 | — | — |
| 21 | Name | NAME | — | ✅ |
| 22 | OverStaffThreshold | OVER_STAFF_THRESHOLD | — | ✅ |
| 23 | Precedence | PRECEDENCE | — | — |
| 24 | ProductArea | PRODUCT_AREA | — | — |
| 25 | SchedulingGroupId | SCHEDULING_GROUP_ID | — | — |
| 26 | SetupOptionValCd | SETUP_OPTION_VAL_CD | — | ✅ |
| 27 | SetupOptionValId | SETUP_OPTION_VAL_ID | 🔑 | ✅ |
| 28 | SetupProfileAsgId | SETUP_PROFILE_ASG_ID | 🔑 | ✅ |
| 29 | SetupProfileCd | SETUP_PROFILE_CD | — | ✅ |
| 30 | SetupProfileId | SETUP_PROFILE_ID | — | ✅ |
| 31 | Type | TYPE | — | — |
| 32 | UnderStaffThreshold | UNDER_STAFF_THRESHOLD | — | ✅ |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate2 | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate2 | EFFECTIVE_START_DATE | — | ✅ |
| 3 | GroupManagerPersonNumber | PERSON_NUMBER | — | ✅ |
| 4 | PersonId | PERSON_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate1 | EFFECTIVE_START_DATE | — | ✅ |
| 3 | GroupManagerName | FULL_NAME | — | ✅ |
| 4 | PersonNameId | PERSON_NAME_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
