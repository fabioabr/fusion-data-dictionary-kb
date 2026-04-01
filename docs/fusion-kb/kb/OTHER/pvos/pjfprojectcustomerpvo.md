---
id: DOC-OTHER-PVO-PJFProjectCustomerPVO
doc_type: system-doc
title: "PJFProjectCustomerPVO — PVO Cross-Module"
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
  - PJFProjectCustomerPVO
  - pjfprojectcustomerpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PJFProjectCustomerPVO

## 📌 Visão Geral

View Object para extração BICC de dados de PJFProject Customer. Acessa as tabelas: HZ_PARTIES, PJF_PROJECT_PARTIES.

**Caminho:** `FscmTopModelAM.PjfProjectDefinitionAM.PJFProjectCustomerPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 31 | 2 | 1 | 5 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[hz_parties|HZ_PARTIES]] — 11 atributos (2 BICC)
- [[pjf_project_parties|PJF_PROJECT_PARTIES]] — 20 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustomerPartyPEOAddress1 | ADDRESS1 | — | — |
| 2 | CustomerPartyPEOAddress2 | ADDRESS2 | — | — |
| 3 | CustomerPartyPEOAddress3 | ADDRESS3 | — | — |
| 4 | CustomerPartyPEOAddress4 | ADDRESS4 | — | — |
| 5 | CustomerPartyPEOEmailAddress | EMAIL_ADDRESS | — | — |
| 6 | CustomerPartyPEOPartyId | PARTY_ID | — | — |
| 7 | CustomerPartyPEOPartyName | PARTY_NAME | — | ✅ |
| 8 | CustomerPartyPEOPartyNumber | PARTY_NUMBER | — | ✅ |
| 9 | CustomerPartyPEOPersonFirstName | PERSON_FIRST_NAME | — | — |
| 10 | CustomerPartyPEOPersonLastName | PERSON_LAST_NAME | — | — |
| 11 | CustomerPartyPEOPersonMiddleName | PERSON_MIDDLE_NAME | — | — |

### [[pjf_project_parties|PJF_PROJECT_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectPartyPEOCreatedBy | CREATED_BY | — | — |
| 2 | ProjectPartyPEOCreationDate | CREATION_DATE | — | — |
| 3 | ProjectPartyPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 4 | ProjectPartyPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ProjectPartyPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ProjectPartyPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ProjectPartyPEOLdapRequestId | LDAP_REQUEST_ID | — | — |
| 8 | ProjectPartyPEOObjectId | OBJECT_ID | — | — |
| 9 | ProjectPartyPEOObjectType | OBJECT_TYPE | — | — |
| 10 | ProjectPartyPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ProjectPartyPEOPjsTrackTime | PJS_TRACK_TIME | — | — |
| 12 | ProjectPartyPEOProjectId | PROJECT_ID | — | — |
| 13 | ProjectPartyPEOProjectPartyId | PROJECT_PARTY_ID | 🔑 | ✅ |
| 14 | ProjectPartyPEOProjectPartyType | PROJECT_PARTY_TYPE | — | — |
| 15 | ProjectPartyPEOProjectRoleId | PROJECT_ROLE_ID | — | — |
| 16 | ProjectPartyPEORelationshipId | RELATIONSHIP_ID | — | — |
| 17 | ProjectPartyPEOResourceId | RESOURCE_ID | — | — |
| 18 | ProjectPartyPEOResourceSourceId | RESOURCE_SOURCE_ID | — | ✅ |
| 19 | ProjectPartyPEOScheduledFlag | SCHEDULED_FLAG | — | — |
| 20 | ProjectPartyPEOStartDateActive | START_DATE_ACTIVE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
