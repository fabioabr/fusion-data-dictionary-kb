---
id: DOC-OTHER-PVO-ParticipantDetailPVO
doc_type: system-doc
title: "ParticipantDetailPVO — PVO Cross-Module"
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
  - ParticipantDetailPVO
  - participantdetailpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ParticipantDetailPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Participant Detail. Acessa as tabelas: CN_SRP_PARTICIPANTS_ALL, CN_SRP_PARTICIPANT_DETAILS_ALL.

**Caminho:** `FscmTopModelAM.ParticipantSetupAM.ParticipantDetailPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 2 | 1 | 15 | 68% |

---

## 🔗 Tabelas Relacionadas

- [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]] — 4 atributos (1 BICC)
- [[cn_srp_participant_details_all|CN_SRP_PARTICIPANT_DETAILS_ALL]] — 18 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 2 | ParticipantId1 | PARTICIPANT_ID | — | — |
| 3 | ParticipantPEOSourceSystemId | SOURCE_SYSTEM_ID | — | — |
| 4 | PartyId | PARTY_ID | — | ✅ |

### [[cn_srp_participant_details_all|CN_SRP_PARTICIPANT_DETAILS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 2 | CostCenter | COST_CENTER | — | ✅ |
| 3 | CountryCode | COUNTRY_CODE | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 7 | EndDate | END_DATE | — | ✅ |
| 8 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 9 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | OrgId | ORG_ID | — | — |
| 15 | ParticipantDetailId | PARTICIPANT_DETAIL_ID | 🔑 | ✅ |
| 16 | ParticipantId | PARTICIPANT_ID | — | ✅ |
| 17 | RequestId | REQUEST_ID | — | ✅ |
| 18 | StartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
