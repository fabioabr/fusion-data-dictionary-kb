---
id: DOC-OTHER-PVO-ResourceP
doc_type: system-doc
title: "ResourceP — PVO Cross-Module"
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
  - ResourceP
  - resourcep
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ResourceP

## 📌 Visão Geral

View Object para extração BICC de dados de Resource P. Acessa as tabelas: HZ_PARTIES, HZ_PARTY_USG_ASSIGNMENTS, JTF_RS_RESOURCE_PROFILES.

**Caminho:** `FscmTopModelAM.ContractsCoreAM.ResourceP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 3 | 2 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hz_parties|HZ_PARTIES]] — 5 atributos (5 BICC)
- [[hz_party_usg_assignments|HZ_PARTY_USG_ASSIGNMENTS]] — 4 atributos (4 BICC)
- [[jtf_rs_resource_profiles|JTF_RS_RESOURCE_PROFILES]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyName | PARTY_NAME | — | ✅ |
| 2 | PartyNumber | PARTY_NUMBER | — | ✅ |
| 3 | PartyPEOPartyId | PARTY_ID | — | ✅ |
| 4 | PartyType | PARTY_TYPE | — | ✅ |
| 5 | PartyUniqueName | PARTY_UNIQUE_NAME | — | ✅ |

### [[hz_party_usg_assignments|HZ_PARTY_USG_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyUsageAssignmentPEOPartyId | PARTY_ID | — | ✅ |
| 2 | PartyUsageCode | PARTY_USAGE_CODE | — | ✅ |
| 3 | PartyUsgAssignmentId | PARTY_USG_ASSIGNMENT_ID | — | ✅ |
| 4 | StatusFlag | STATUS_FLAG | — | ✅ |

### [[jtf_rs_resource_profiles|JTF_RS_RESOURCE_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EmailAddress | EMAIL_ADDRESS | — | ✅ |
| 2 | PartyId | PARTY_ID | — | ✅ |
| 3 | PersonFirstName | PERSON_FIRST_NAME | — | ✅ |
| 4 | PersonLastName | PERSON_LAST_NAME | — | ✅ |
| 5 | PersonName | PERSON_NAME | — | ✅ |
| 6 | PersonTitle | PERSON_TITLE | — | ✅ |
| 7 | PersonalEmailFlag | PERSONAL_EMAIL_FLAG | — | ✅ |
| 8 | PrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | ✅ |
| 9 | ResourceProfileId | RESOURCE_PROFILE_ID | 🔑 | ✅ |
| 10 | ResourceProfileId1 | RESOURCE_PROFILE_ID | 🔑 | ✅ |
| 11 | StartDateActive | START_DATE_ACTIVE | — | ✅ |
| 12 | TimezoneCode | TIMEZONE_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
