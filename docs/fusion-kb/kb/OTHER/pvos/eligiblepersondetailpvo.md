---
id: DOC-OTHER-PVO-EligiblePersonDetailPVO
doc_type: system-doc
title: "EligiblePersonDetailPVO — PVO Cross-Module"
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
  - EligiblePersonDetailPVO
  - eligiblepersondetailpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EligiblePersonDetailPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Eligible Person Detail. Acessa as tabelas: BEN_ELIG_PERSON_DETAILS_V, PER_ALL_PEOPLE_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.EligiblePersonDetailPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 67 | 2 | 1 | 40 | 60% |

---

## 🔗 Tabelas Relacionadas

- [[ben_elig_person_details_v|BEN_ELIG_PERSON_DETAILS_V]] — 64 atributos (1 PKs, 40 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 3 atributos

---

## ⚙️ Atributos

### [[ben_elig_person_details_v|BEN_ELIG_PERSON_DETAILS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgeVal | AGE_VAL | — | ✅ |
| 2 | BenefitGroupId | BENEFIT_GROUP_ID | — | — |
| 3 | BenefitRelationId | BENEFIT_RELATION_ID | — | — |
| 4 | BenefitRelationName | BENEFIT_RELATION_NAME | — | ✅ |
| 5 | CompRefAmt | COMP_REF_AMT | — | ✅ |
| 6 | DpntOthrPlCvrdRlFlag | DPNT_OTHR_PL_CVRD_RL_FLAG | — | ✅ |
| 7 | EligCreatedBy | ELIG_CREATED_BY | — | ✅ |
| 8 | EligCreationDate | ELIG_CREATION_DATE | — | ✅ |
| 9 | EligEffectiveEndDate | ELIG_EFFECTIVE_END_DATE | — | ✅ |
| 10 | EligEffectiveStartDate | ELIG_EFFECTIVE_START_DATE | — | ✅ |
| 11 | EligFlag | ELIG_FLAG | — | ✅ |
| 12 | EligLastUpdateDate | ELIG_LAST_UPDATE_DATE | — | ✅ |
| 13 | EligLastUpdateLogin | ELIG_LAST_UPDATE_LOGIN | — | ✅ |
| 14 | EligLastUpdatedBy | ELIG_LAST_UPDATED_BY | — | ✅ |
| 15 | EligPerId | ELIG_PER_ID | 🔑 | ✅ |
| 16 | EligPerOptId | ELIG_PER_OPT_ID | — | — |
| 17 | FrzAgeFlag | FRZ_AGE_FLAG | — | ✅ |
| 18 | GrpEffectiveEndDate | GRP_EFFECTIVE_END_DATE | — | — |
| 19 | GrpEffectiveStartDate | GRP_EFFECTIVE_START_DATE | — | ✅ |
| 20 | HrsWkdVal | HRS_WKD_VAL | — | ✅ |
| 21 | LegalEntityId | LEGAL_ENTITY_ID | — | — |
| 22 | LerId | LER_ID | — | — |
| 23 | LosVal | LOS_VAL | — | ✅ |
| 24 | NoMxPrtnOvridThruFlag | NO_MX_PRTN_OVRID_THRU_FLAG | — | ✅ |
| 25 | OptCreatedBy | OPT_CREATED_BY | — | ✅ |
| 26 | OptCreationDate | OPT_CREATION_DATE | — | ✅ |
| 27 | OptEffectiveEndDate | OPT_EFFECTIVE_END_DATE | — | — |
| 28 | OptEffectiveStartDate | OPT_EFFECTIVE_START_DATE | — | ✅ |
| 29 | OptId | OPT_ID | — | — |
| 30 | OptLastUpdateDate | OPT_LAST_UPDATE_DATE | — | ✅ |
| 31 | OptLastUpdateLogin | OPT_LAST_UPDATE_LOGIN | — | ✅ |
| 32 | OptLastUpdatedBy | OPT_LAST_UPDATED_BY | — | ✅ |
| 33 | PctFlTmVal | PCT_FL_TM_VAL | — | ✅ |
| 34 | PerInLerId | PER_IN_LER_ID | — | — |
| 35 | PersonId | PERSON_ID | — | — |
| 36 | PgmId | PGM_ID | — | — |
| 37 | Pl2EffectiveEndDate | PL2_EFFECTIVE_END_DATE | — | — |
| 38 | Pl2EffectiveStartDate | PL2_EFFECTIVE_START_DATE | — | ✅ |
| 39 | PlEffectiveEndDate | PL_EFFECTIVE_END_DATE | — | — |
| 40 | PlEffectiveStartDate | PL_EFFECTIVE_START_DATE | — | ✅ |
| 41 | PlId | PL_ID | — | — |
| 42 | PlKeyEeFlag | PL_KEY_EE_FLAG | — | ✅ |
| 43 | PlTyp2EffectiveEndDate | PL_TYP2_EFFECTIVE_END_DATE | — | — |
| 44 | PlTyp2EffectiveStartDate | PL_TYP2_EFFECTIVE_START_DATE | — | ✅ |
| 45 | PlTyp3EffectiveEndDate | PL_TYP3_EFFECTIVE_END_DATE | — | — |
| 46 | PlTyp3EffectiveStartDate | PL_TYP3_EFFECTIVE_START_DATE | — | ✅ |
| 47 | PlTypEffectiveEndDate | PL_TYP_EFFECTIVE_END_DATE | — | — |
| 48 | PlTypEffectiveStartDate | PL_TYP_EFFECTIVE_START_DATE | — | ✅ |
| 49 | PlTypId | PL_TYP_ID | — | — |
| 50 | PlipEffectiveEndDate | PLIP_EFFECTIVE_END_DATE | — | — |
| 51 | PlipEffectiveStartDate | PLIP_EFFECTIVE_START_DATE | — | ✅ |
| 52 | PlipId | PLIP_ID | — | — |
| 53 | PrimaryRel | PRIMARY_REL | — | ✅ |
| 54 | PrtnEndDt | PRTN_END_DT | — | ✅ |
| 55 | PrtnOvridnRsnCd | PRTN_OVRIDN_RSN_CD | — | ✅ |
| 56 | PrtnOvridnThruDt | PRTN_OVRIDN_THRU_DT | — | ✅ |
| 57 | PrtnStrtDt | PRTN_STRT_DT | — | ✅ |
| 58 | PtipEffectiveEndDate | PTIP_EFFECTIVE_END_DATE | — | — |
| 59 | PtipEffectiveStartDate | PTIP_EFFECTIVE_START_DATE | — | ✅ |
| 60 | PtipId | PTIP_ID | — | — |
| 61 | RelEffectiveEndDate | REL_EFFECTIVE_END_DATE | — | — |
| 62 | RelEffectiveStartDate | REL_EFFECTIVE_START_DATE | — | ✅ |
| 63 | RelPrmryAsgId | REL_PRMRY_ASG_ID | — | — |
| 64 | WvCtfnTypCd | WV_CTFN_TYP_CD | — | ✅ |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | PersonId1 | PERSON_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
