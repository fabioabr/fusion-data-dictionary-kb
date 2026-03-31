---
id: DOC-OTHER-PVO-GroupMembersPVO
doc_type: system-doc
title: "GroupMembersPVO — PVO Cross-Module"
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
  - GroupMembersPVO
  - groupmemberspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GroupMembersPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Group Members. Acessa as tabelas: HWM_GRPS_B, HWM_GRPS_TL, HWM_GRP_MEMBERS_F (+2).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GroupsAM.GroupMembersPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 57 | 5 | 3 | 53 | 93% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_grps_b|HWM_GRPS_B]] — 23 atributos (23 BICC)
- [[hwm_grps_tl|HWM_GRPS_TL]] — 12 atributos (1 PKs, 12 BICC)
- [[hwm_grp_members_f|HWM_GRP_MEMBERS_F]] — 14 atributos (2 PKs, 14 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 4 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 4 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hwm_grps_b|HWM_GRPS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GroupsPEOApplicationUsageCd | APPL_USG_CD | — | ✅ |
| 2 | GroupsPEOAppliesToCd | APPLIES_TO_CD | — | ✅ |
| 3 | GroupsPEOAssignmentToUseCd | ASSIGNMENT_TO_USE_CD | — | ✅ |
| 4 | GroupsPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | GroupsPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | GroupsPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 7 | GroupsPEOEvaluateStatusCd | EVAL_STATUS_CD | — | ✅ |
| 8 | GroupsPEOFreezeFlag | FREEZE_FLAG | — | ✅ |
| 9 | GroupsPEOGroupCode | GRP_CODE | — | ✅ |
| 10 | GroupsPEOGroupId | GRP_ID | — | ✅ |
| 11 | GroupsPEOLastRefreshDate | LAST_REFRESH_DT | — | ✅ |
| 12 | GroupsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | GroupsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | GroupsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | GroupsPEOMassEvalFlag | MASS_EVAL_FLAG | — | ✅ |
| 16 | GroupsPEOMemTypeCd | MEM_TYPE_CD | — | ✅ |
| 17 | GroupsPEOModuleId | MODULE_ID | — | ✅ |
| 18 | GroupsPEONextRefreshDate | NEXT_REFRESH_DT | — | ✅ |
| 19 | GroupsPEONumberDaysNext | NUM_DAYS_NEXT | — | ✅ |
| 20 | GroupsPEONumberDaysPrev | NUM_DAYS_PREV | — | ✅ |
| 21 | GroupsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 22 | GroupsPEOOnlineEvaluateFlag | ONLINE_EVAL_FLAG | — | ✅ |
| 23 | GroupsPEORunType | RUN_TYPE | — | ✅ |

### [[hwm_grps_tl|HWM_GRPS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GroupsTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | GroupsTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | GroupsTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | GroupsTranslationPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 5 | GroupsTranslationPEOGroupId | GRP_ID | — | ✅ |
| 6 | GroupsTranslationPEOGroupName | GROUP_NAME | — | ✅ |
| 7 | GroupsTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 8 | GroupsTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | GroupsTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | GroupsTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | GroupsTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | GroupsTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

### [[hwm_grp_members_f|HWM_GRP_MEMBERS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GroupMembersDPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | GroupMembersDPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | GroupMembersDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 4 | GroupMembersDPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 5 | GroupMembersDPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 6 | GroupMembersDPEOGroupEvaluateProcessId | GRP_EVAL_PROCESS_ID | — | ✅ |
| 7 | GroupMembersDPEOGroupId | GRP_ID | — | ✅ |
| 8 | GroupMembersDPEOGroupMemberId | GRP_MEMBER_ID | 🔑 | ✅ |
| 9 | GroupMembersDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | GroupMembersDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | GroupMembersDPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | GroupMembersDPEOMemberId | MEMBER_ID | — | ✅ |
| 13 | GroupMembersDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | GroupMembersDPEORemarks | REMARKS | — | ✅ |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonDetailsPEOPersonId | PERSON_ID | — | — |
| 4 | PersonNumber | PERSON_NUMBER | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonName | FULL_NAME | — | ✅ |
| 2 | PersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | PersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
