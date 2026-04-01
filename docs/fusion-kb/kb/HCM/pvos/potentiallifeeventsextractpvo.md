---
id: DOC-HCM-PVO-PotentialLifeEventsExtractPVO
doc_type: system-doc
title: "PotentialLifeEventsExtractPVO — PVO Human Capital Management"
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
  - PotentialLifeEventsExtractPVO
  - potentiallifeeventsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PotentialLifeEventsExtractPVO

## 📌 Visão Geral

Extrai eventos de vida potenciais para BICC, com vínculo ao beneficiário e business group. Suporta analytics de eventos pendentes de processamento no ciclo de benefícios.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.BenefitsBiccExtractAM.PotentialLifeEventsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 38 | 1 | 1 | 38 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ben_ptnl_ler_for_per|BEN_PTNL_LER_FOR_PER]] — 38 atributos (1 PKs, 38 BICC)

---

## ⚙️ Atributos

### [[ben_ptnl_ler_for_per|BEN_PTNL_LER_FOR_PER]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BenefitRelationId | BENEFIT_RELATION_ID | — | ✅ |
| 2 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 3 | ClpsedBy | CLPSED_BY | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | CsdByPtnlLerForPerId | CSD_BY_PTNL_LER_FOR_PER_ID | — | ✅ |
| 7 | DtctdDt | DTCTD_DT | — | ✅ |
| 8 | EnrtPerdId | ENRT_PERD_ID | — | ✅ |
| 9 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 10 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 11 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | LegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 15 | LerId | LER_ID | — | ✅ |
| 16 | LerTypeCd | LER_TYPE_CD | — | ✅ |
| 17 | LfEvtOcrdDt | LF_EVT_OCRD_DT | — | ✅ |
| 18 | MnlDt | MNL_DT | — | ✅ |
| 19 | MnloDt | MNLO_DT | — | ✅ |
| 20 | NtfnDt | NTFN_DT | — | ✅ |
| 21 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 22 | PersonId | PERSON_ID | — | ✅ |
| 23 | ProcdDt | PROCD_DT | — | ✅ |
| 24 | ProdCd | PROD_CD | — | ✅ |
| 25 | ProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 26 | ProgramName | PROGRAM_NAME | — | ✅ |
| 27 | ProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 28 | PtnlAddnlChar1 | PTNL_ADDNL_CHAR1 | — | ✅ |
| 29 | PtnlAddnlChar2 | PTNL_ADDNL_CHAR2 | — | ✅ |
| 30 | PtnlAddnlChar3 | PTNL_ADDNL_CHAR3 | — | ✅ |
| 31 | PtnlAddnlNumber1 | PTNL_ADDNL_NUMBER1 | — | ✅ |
| 32 | PtnlLerForPerId | PTNL_LER_FOR_PER_ID | 🔑 | ✅ |
| 33 | PtnlLerForPerSrcCd | PTNL_LER_FOR_PER_SRC_CD | — | ✅ |
| 34 | PtnlLerForPerStatCd | PTNL_LER_FOR_PER_STAT_CD | — | ✅ |
| 35 | RequestId | REQUEST_ID | — | ✅ |
| 36 | TrgrTablePkId | TRGR_TABLE_PK_ID | — | ✅ |
| 37 | UnprocdDt | UNPROCD_DT | — | ✅ |
| 38 | VoiddDt | VOIDD_DT | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
