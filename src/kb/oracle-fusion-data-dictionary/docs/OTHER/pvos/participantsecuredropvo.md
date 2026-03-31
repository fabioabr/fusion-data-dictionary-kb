---
id: DOC-OTHER-PVO-ParticipantSecuredROPVO
doc_type: system-doc
title: "ParticipantSecuredROPVO — PVO Cross-Module"
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
  - ParticipantSecuredROPVO
  - participantsecuredropvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ParticipantSecuredROPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Participant Secured RO. Acessa as tabelas: CN_SRP_PARTICIPANTS_ALL, HZ_PARTIES.

**Caminho:** `FscmTopModelAM.ParticipantSetupAM.ParticipantSecuredROPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 38 | 2 | 1 | 26 | 68% |

---

## 🔗 Tabelas Relacionadas

- [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]] — 28 atributos (1 PKs, 20 BICC)
- [[hz_parties|HZ_PARTIES]] — 10 atributos (6 BICC)

---

## ⚙️ Atributos

### [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | AnalystId | ANALYST_ID | — | ✅ |
| 3 | AnalystObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | AnalystParticipantId | PARTICIPANT_ID | — | — |
| 5 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 6 | CompensationEndDate | COMPENSATION_END_DATE | — | ✅ |
| 7 | CreatedBy | CREATED_BY | — | ✅ |
| 8 | CreationDate | CREATION_DATE | — | ✅ |
| 9 | DisplayIdentifier | DISPLAY_IDENTIFIER | — | — |
| 10 | EndDate | END_DATE | — | ✅ |
| 11 | HoldPaymentFlag | HOLD_PAYMENT_FLAG | — | ✅ |
| 12 | HoldReason | HOLD_REASON | — | ✅ |
| 13 | HrPrimaryWorkerNumber | HR_PRIMARY_WORKER_NUMBER | — | ✅ |
| 14 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 15 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 16 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 18 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | OrgId | ORG_ID | — | — |
| 21 | ParticipantId | PARTICIPANT_ID | 🔑 | ✅ |
| 22 | ParticipantType | PARTICIPANT_TYPE | — | ✅ |
| 23 | PartyId | PARTY_ID | — | ✅ |
| 24 | PayeeOnly | PAYEE_ONLY | — | ✅ |
| 25 | RequestId | REQUEST_ID | — | ✅ |
| 26 | SourceSystem | SOURCE_SYSTEM | — | ✅ |
| 27 | SourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 28 | StartDate | START_DATE | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AnalystEmailAddress | EMAIL_ADDRESS | — | — |
| 2 | AnalystName | PARTY_NAME | — | ✅ |
| 3 | AnalystPartyPEOPartyId | PARTY_ID | — | — |
| 4 | ParticipantEmailAddress | EMAIL_ADDRESS | — | — |
| 5 | ParticipantFirstName | PERSON_FIRST_NAME | — | ✅ |
| 6 | ParticipantLastName | PERSON_LAST_NAME | — | ✅ |
| 7 | ParticipantName | PARTY_NAME | — | ✅ |
| 8 | ParticipantPartyPEOPartyId | PARTY_ID | — | — |
| 9 | PartyNumber | PARTY_NUMBER | — | ✅ |
| 10 | UserGuid | USER_GUID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
