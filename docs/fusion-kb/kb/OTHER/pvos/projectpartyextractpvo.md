---
id: DOC-OTHER-PVO-ProjectPartyExtractPVO
doc_type: system-doc
title: "ProjectPartyExtractPVO — PVO Cross-Module"
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
  - ProjectPartyExtractPVO
  - projectpartyextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectPartyExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Party Extract. Acessa as tabelas: PJF_PROJECT_PARTIES.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ProjectPartyExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 1 | 1 | 20 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_project_parties|PJF_PROJECT_PARTIES]] — 20 atributos (1 PKs, 20 BICC)

---

## ⚙️ Atributos

### [[pjf_project_parties|PJF_PROJECT_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectPartyPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProjectPartyPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProjectPartyPEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 4 | ProjectPartyPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ProjectPartyPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | ProjectPartyPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ProjectPartyPEOLdapRequestId | LDAP_REQUEST_ID | — | ✅ |
| 8 | ProjectPartyPEOObjectId | OBJECT_ID | — | ✅ |
| 9 | ProjectPartyPEOObjectType | OBJECT_TYPE | — | ✅ |
| 10 | ProjectPartyPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ProjectPartyPEOPjsTrackTime | PJS_TRACK_TIME | — | ✅ |
| 12 | ProjectPartyPEOProjectId | PROJECT_ID | — | ✅ |
| 13 | ProjectPartyPEOProjectPartyId | PROJECT_PARTY_ID | 🔑 | ✅ |
| 14 | ProjectPartyPEOProjectPartyType | PROJECT_PARTY_TYPE | — | ✅ |
| 15 | ProjectPartyPEOProjectRoleId | PROJECT_ROLE_ID | — | ✅ |
| 16 | ProjectPartyPEORelationshipId | RELATIONSHIP_ID | — | ✅ |
| 17 | ProjectPartyPEOResourceId | RESOURCE_ID | — | ✅ |
| 18 | ProjectPartyPEOResourceSourceId | RESOURCE_SOURCE_ID | — | ✅ |
| 19 | ProjectPartyPEOScheduledFlag | SCHEDULED_FLAG | — | ✅ |
| 20 | ProjectPartyPEOStartDateActive | START_DATE_ACTIVE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
