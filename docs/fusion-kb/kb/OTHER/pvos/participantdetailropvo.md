---
id: DOC-OTHER-PVO-ParticipantDetailROPVO
doc_type: system-doc
title: "ParticipantDetailROPVO — PVO Cross-Module"
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
  - ParticipantDetailROPVO
  - participantdetailropvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ParticipantDetailROPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Participant Detail RO. Acessa as tabelas: CN_SRP_PARTICIPANTS_ALL, CN_SRP_PARTICIPANT_DETAILS_ALL.

**Caminho:** `FscmTopModelAM.ParticipantSetupAM.ParticipantDetailROPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 73 | 2 | 1 | 16 | 22% |

---

## 🔗 Tabelas Relacionadas

- [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]] — 5 atributos (2 BICC)
- [[cn_srp_participant_details_all|CN_SRP_PARTICIPANT_DETAILS_ALL]] — 68 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 2 | OrgId1 | ORG_ID | — | — |
| 3 | ParticipantId1 | PARTICIPANT_ID | — | — |
| 4 | PartyId | PARTY_ID | — | ✅ |
| 5 | SourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |

### [[cn_srp_participant_details_all|CN_SRP_PARTICIPANT_DETAILS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 2 | AttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 3 | AttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 4 | AttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 5 | AttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 6 | AttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 7 | AttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 8 | AttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 9 | AttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 10 | AttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 11 | AttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 12 | AttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 13 | AttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 14 | AttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 15 | AttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 16 | AttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 17 | AttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 18 | AttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 19 | AttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 20 | AttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 21 | AttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 22 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 24 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 29 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 30 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 31 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 32 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 33 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 34 | AttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 35 | AttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 36 | AttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 37 | AttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 38 | AttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 39 | AttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 40 | AttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 41 | AttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 42 | AttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 43 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 44 | AttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 45 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 46 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 47 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 48 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 49 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 50 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 51 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 52 | CostCenter | COST_CENTER | — | ✅ |
| 53 | CountryCode | COUNTRY_CODE | — | ✅ |
| 54 | CreatedBy | CREATED_BY | — | ✅ |
| 55 | CreationDate | CREATION_DATE | — | ✅ |
| 56 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 57 | EndDate | END_DATE | — | ✅ |
| 58 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 59 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 60 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 61 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 62 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 63 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 64 | OrgId | ORG_ID | — | — |
| 65 | ParticipantDetailId | PARTICIPANT_DETAIL_ID | 🔑 | ✅ |
| 66 | ParticipantId | PARTICIPANT_ID | — | ✅ |
| 67 | RequestId | REQUEST_ID | — | ✅ |
| 68 | StartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
