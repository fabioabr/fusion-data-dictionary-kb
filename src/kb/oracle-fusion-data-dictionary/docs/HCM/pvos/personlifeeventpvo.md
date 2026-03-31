---
id: DOC-HCM-PVO-PersonLifeEventPVO
doc_type: system-doc
title: "PersonLifeEventPVO — PVO Human Capital Management"
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
  - PersonLifeEventPVO
  - personlifeeventpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonLifeEventPVO

## 📌 Visão Geral

Extrai eventos de vida dos colaboradores no contexto de benefícios (casamento, nascimento, etc.), com datas e status. Dispara elegibilidade para alterações em planos de benefícios.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.PersonLifeEventPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 81 | 4 | 1 | 19 | 23% |

---

## 🔗 Tabelas Relacionadas

- [[ben_benefit_relations_f|BEN_BENEFIT_RELATIONS_F]] — 9 atributos (3 BICC)
- [[ben_per_benefit_group_f|BEN_PER_BENEFIT_GROUP_F]] — 4 atributos (1 BICC)
- [[ben_per_in_ler|BEN_PER_IN_LER]] — 65 atributos (1 PKs, 15 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 3 atributos

---

## ⚙️ Atributos

### [[ben_benefit_relations_f|BEN_BENEFIT_RELATIONS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BenefitRelSystemCd | BENEFIT_REL_SYSTEM_CD | — | — |
| 2 | BenefitRelationId1 | BENEFIT_RELATION_ID | — | — |
| 3 | BenefitRelationName | BENEFIT_RELATION_NAME | — | ✅ |
| 4 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 5 | EffectiveEndDate2 | EFFECTIVE_END_DATE | — | — |
| 6 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | PrimaryRel | PRIMARY_REL | — | ✅ |
| 8 | RelPrmryAsgId | REL_PRMRY_ASG_ID | — | — |
| 9 | Status | STATUS | — | — |

### [[ben_per_benefit_group_f|BEN_PER_BENEFIT_GROUP_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BenefitGroupId | BENEFIT_GROUP_ID | — | — |
| 2 | EffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 3 | EffectiveStartDate1 | EFFECTIVE_START_DATE | — | ✅ |
| 4 | LeBenefitGroupId | LE_BENEFIT_GROUP_ID | — | — |

### [[ben_per_in_ler|BEN_PER_IN_LER]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentId | ASSIGNMENT_ID | — | — |
| 2 | BcktDt | BCKT_DT | — | ✅ |
| 3 | BcktPerInLerId | BCKT_PER_IN_LER_ID | — | — |
| 4 | BenefitRelationId | BENEFIT_RELATION_ID | — | — |
| 5 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 6 | ClsdDt | CLSD_DT | — | ✅ |
| 7 | CreatedBy | CREATED_BY | — | ✅ |
| 8 | CreationDate | CREATION_DATE | — | ✅ |
| 9 | GroupPlId | GROUP_PL_ID | — | — |
| 10 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 11 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 12 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | LegalEntityId | LEGAL_ENTITY_ID | — | — |
| 16 | LerId | LER_ID | — | ✅ |
| 17 | LerTypeCd | LER_TYPE_CD | — | — |
| 18 | LfEvtOcrdDt | LF_EVT_OCRD_DT | — | ✅ |
| 19 | NtfnDt | NTFN_DT | — | ✅ |
| 20 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | PerInLerId | PER_IN_LER_ID | 🔑 | ✅ |
| 22 | PerInLerStatCd | PER_IN_LER_STAT_CD | — | ✅ |
| 23 | PersonId | PERSON_ID | — | — |
| 24 | PilAttribute1 | PIL_ATTRIBUTE1 | — | — |
| 25 | PilAttribute10 | PIL_ATTRIBUTE10 | — | — |
| 26 | PilAttribute11 | PIL_ATTRIBUTE11 | — | — |
| 27 | PilAttribute12 | PIL_ATTRIBUTE12 | — | — |
| 28 | PilAttribute13 | PIL_ATTRIBUTE13 | — | — |
| 29 | PilAttribute14 | PIL_ATTRIBUTE14 | — | — |
| 30 | PilAttribute15 | PIL_ATTRIBUTE15 | — | — |
| 31 | PilAttribute16 | PIL_ATTRIBUTE16 | — | — |
| 32 | PilAttribute17 | PIL_ATTRIBUTE17 | — | — |
| 33 | PilAttribute18 | PIL_ATTRIBUTE18 | — | — |
| 34 | PilAttribute19 | PIL_ATTRIBUTE19 | — | — |
| 35 | PilAttribute2 | PIL_ATTRIBUTE2 | — | — |
| 36 | PilAttribute20 | PIL_ATTRIBUTE20 | — | — |
| 37 | PilAttribute21 | PIL_ATTRIBUTE21 | — | — |
| 38 | PilAttribute22 | PIL_ATTRIBUTE22 | — | — |
| 39 | PilAttribute23 | PIL_ATTRIBUTE23 | — | — |
| 40 | PilAttribute24 | PIL_ATTRIBUTE24 | — | — |
| 41 | PilAttribute25 | PIL_ATTRIBUTE25 | — | — |
| 42 | PilAttribute26 | PIL_ATTRIBUTE26 | — | — |
| 43 | PilAttribute27 | PIL_ATTRIBUTE27 | — | — |
| 44 | PilAttribute28 | PIL_ATTRIBUTE28 | — | — |
| 45 | PilAttribute29 | PIL_ATTRIBUTE29 | — | — |
| 46 | PilAttribute3 | PIL_ATTRIBUTE3 | — | — |
| 47 | PilAttribute30 | PIL_ATTRIBUTE30 | — | — |
| 48 | PilAttribute4 | PIL_ATTRIBUTE4 | — | — |
| 49 | PilAttribute5 | PIL_ATTRIBUTE5 | — | — |
| 50 | PilAttribute6 | PIL_ATTRIBUTE6 | — | — |
| 51 | PilAttribute7 | PIL_ATTRIBUTE7 | — | — |
| 52 | PilAttribute8 | PIL_ATTRIBUTE8 | — | — |
| 53 | PilAttribute9 | PIL_ATTRIBUTE9 | — | — |
| 54 | PilAttributeCategory | PIL_ATTRIBUTE_CATEGORY | — | — |
| 55 | ProcdDt | PROCD_DT | — | ✅ |
| 56 | ProdCd | PROD_CD | — | — |
| 57 | ProgramAppName | PROGRAM_APP_NAME | — | — |
| 58 | ProgramName | PROGRAM_NAME | — | — |
| 59 | ProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 60 | PrvsStatCd | PRVS_STAT_CD | — | — |
| 61 | PtnlLerForPerId | PTNL_LER_FOR_PER_ID | — | — |
| 62 | RequestId | REQUEST_ID | — | — |
| 63 | StrtdDt | STRTD_DT | — | ✅ |
| 64 | TrgrTablePkId | TRGR_TABLE_PK_ID | — | — |
| 65 | VoiddDt | VOIDD_DT | — | ✅ |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate3 | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate2 | EFFECTIVE_START_DATE | — | — |
| 3 | PersonId1 | PERSON_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
