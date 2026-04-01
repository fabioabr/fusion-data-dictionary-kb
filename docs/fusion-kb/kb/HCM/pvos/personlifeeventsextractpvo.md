---
id: DOC-HCM-PVO-PersonLifeEventsExtractPVO
doc_type: system-doc
title: "PersonLifeEventsExtractPVO — PVO Human Capital Management"
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
  - PersonLifeEventsExtractPVO
  - personlifeeventsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonLifeEventsExtractPVO

## 📌 Visão Geral

Extrai eventos de vida para BICC, com vínculo ao beneficiário e datas de processamento. Suporta analytics do ciclo de life events e impacto nas inscrições de benefícios.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.BenefitsBiccExtractAM.PersonLifeEventsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 34 | 1 | 1 | 34 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ben_per_in_ler|BEN_PER_IN_LER]] — 34 atributos (1 PKs, 34 BICC)

---

## ⚙️ Atributos

### [[ben_per_in_ler|BEN_PER_IN_LER]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentId | ASSIGNMENT_ID | — | ✅ |
| 2 | BcktDt | BCKT_DT | — | ✅ |
| 3 | BcktPerInLerId | BCKT_PER_IN_LER_ID | — | ✅ |
| 4 | BenefitRelationId | BENEFIT_RELATION_ID | — | ✅ |
| 5 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 6 | ClsdDt | CLSD_DT | — | ✅ |
| 7 | CreatedBy | CREATED_BY | — | ✅ |
| 8 | CreationDate | CREATION_DATE | — | ✅ |
| 9 | GroupPlId | GROUP_PL_ID | — | ✅ |
| 10 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 11 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 12 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | LegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 16 | LerId | LER_ID | — | ✅ |
| 17 | LerTypeCd | LER_TYPE_CD | — | ✅ |
| 18 | LfEvtOcrdDt | LF_EVT_OCRD_DT | — | ✅ |
| 19 | NtfnDt | NTFN_DT | — | ✅ |
| 20 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 21 | PerInLerId | PER_IN_LER_ID | 🔑 | ✅ |
| 22 | PerInLerStatCd | PER_IN_LER_STAT_CD | — | ✅ |
| 23 | PersonId | PERSON_ID | — | ✅ |
| 24 | ProcdDt | PROCD_DT | — | ✅ |
| 25 | ProdCd | PROD_CD | — | ✅ |
| 26 | ProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 27 | ProgramName | PROGRAM_NAME | — | ✅ |
| 28 | ProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 29 | PrvsStatCd | PRVS_STAT_CD | — | ✅ |
| 30 | PtnlLerForPerId | PTNL_LER_FOR_PER_ID | — | ✅ |
| 31 | RequestId | REQUEST_ID | — | ✅ |
| 32 | StrtdDt | STRTD_DT | — | ✅ |
| 33 | TrgrTablePkId | TRGR_TABLE_PK_ID | — | ✅ |
| 34 | VoiddDt | VOIDD_DT | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
