---
id: DOC-HCM-PVO-PersonPotentialLifeEventPVO
doc_type: system-doc
title: "PersonPotentialLifeEventPVO — PVO Human Capital Management"
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
  - PersonPotentialLifeEventPVO
  - personpotentiallifeeventpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonPotentialLifeEventPVO

## 📌 Visão Geral

Extrai eventos de vida potenciais (não confirmados) dos colaboradores no contexto de benefícios. Permite análise preditiva de elegibilidade e planejamento de enrollment.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.PersonPotentialLifeEventPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 49 | 4 | 1 | 22 | 45% |

---

## 🔗 Tabelas Relacionadas

- [[ben_benefit_relations_f|BEN_BENEFIT_RELATIONS_F]] — 10 atributos (3 BICC)
- [[ben_per_benefit_group_f|BEN_PER_BENEFIT_GROUP_F]] — 4 atributos (1 BICC)
- [[ben_ptnl_ler_for_per|BEN_PTNL_LER_FOR_PER]] — 32 atributos (1 PKs, 18 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 3 atributos

---

## ⚙️ Atributos

### [[ben_benefit_relations_f|BEN_BENEFIT_RELATIONS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BenefitRelSystemCd | BENEFIT_REL_SYSTEM_CD | — | — |
| 2 | BenefitRelationId1 | BENEFIT_RELATION_ID | — | — |
| 3 | BenefitRelationName | BENEFIT_RELATION_NAME | — | ✅ |
| 4 | EffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 5 | EffectiveEndDate2 | EFFECTIVE_END_DATE | — | — |
| 6 | EffectiveStartDate1 | EFFECTIVE_START_DATE | — | ✅ |
| 7 | LegalEntityId | LEGAL_ENTITY_ID | — | — |
| 8 | PrimaryRel | PRIMARY_REL | — | ✅ |
| 9 | RelPrmryAsgId | REL_PRMRY_ASG_ID | — | — |
| 10 | Status | STATUS | — | — |

### [[ben_per_benefit_group_f|BEN_PER_BENEFIT_GROUP_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BenefitGroupId | BENEFIT_GROUP_ID | — | — |
| 2 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | LeBenefitGroupId | LE_BENEFIT_GROUP_ID | — | — |

### [[ben_ptnl_ler_for_per|BEN_PTNL_LER_FOR_PER]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BenefitRelationId | BENEFIT_RELATION_ID | — | — |
| 2 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | CsdByPtnlLerForPerId | CSD_BY_PTNL_LER_FOR_PER_ID | — | — |
| 6 | DtctdDt | DTCTD_DT | — | ✅ |
| 7 | EnrtPerdId | ENRT_PERD_ID | — | — |
| 8 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 9 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | LerId | LER_ID | — | ✅ |
| 14 | LerTypeCd | LER_TYPE_CD | — | ✅ |
| 15 | LfEvtOcrdDt | LF_EVT_OCRD_DT | — | ✅ |
| 16 | MnlDt | MNL_DT | — | ✅ |
| 17 | MnloDt | MNLO_DT | — | — |
| 18 | NtfnDt | NTFN_DT | — | ✅ |
| 19 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | PersonId | PERSON_ID | — | — |
| 21 | ProcdDt | PROCD_DT | — | ✅ |
| 22 | ProdCd | PROD_CD | — | ✅ |
| 23 | ProgramAppName | PROGRAM_APP_NAME | — | — |
| 24 | ProgramName | PROGRAM_NAME | — | — |
| 25 | ProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 26 | PtnlLerForPerId | PTNL_LER_FOR_PER_ID | 🔑 | ✅ |
| 27 | PtnlLerForPerSrcCd | PTNL_LER_FOR_PER_SRC_CD | — | ✅ |
| 28 | PtnlLerForPerStatCd | PTNL_LER_FOR_PER_STAT_CD | — | ✅ |
| 29 | RequestId | REQUEST_ID | — | — |
| 30 | TrgrTablePkId | TRGR_TABLE_PK_ID | — | — |
| 31 | UnprocdDt | UNPROCD_DT | — | ✅ |
| 32 | VoiddDt | VOIDD_DT | — | ✅ |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate3 | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate2 | EFFECTIVE_START_DATE | — | — |
| 3 | PersonId1 | PERSON_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
