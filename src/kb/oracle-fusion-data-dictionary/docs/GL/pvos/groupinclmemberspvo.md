---
id: DOC-GL-PVO-GroupInclMembersPVO
doc_type: system-doc
title: "GroupInclMembersPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - GroupInclMembersPVO
  - groupinclmemberspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GroupInclMembersPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Group Incl Members. Acessa as tabelas: HWM_GRP_INCL_MEMBERS_VIEW, PER_ALL_PEOPLE_F, PER_PERSON_NAMES_F_V.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GroupsAM.GroupInclMembersPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 3 | 1 | 12 | 71% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_grp_incl_members_view|HWM_GRP_INCL_MEMBERS_VIEW]] — 9 atributos (1 PKs, 8 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 4 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 4 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hwm_grp_incl_members_view|HWM_GRP_INCL_MEMBERS_VIEW]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | GrpId | GRP_ID | — | ✅ |
| 4 | GrpInclMemberId | GRP_INCL_MEMBER_ID | 🔑 | ✅ |
| 5 | InclFlag | INCL_FLAG | — | — |
| 6 | InclMemberId | INCL_MEMBER_ID | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate1 | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonId | PERSON_ID | — | — |
| 4 | PersonNumber | PERSON_NUMBER | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | FullName | FULL_NAME | — | ✅ |
| 4 | PersonNameId | PERSON_NAME_ID | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
