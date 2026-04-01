---
id: DOC-OTHER-PVO-PersonTypeUsagesPVO
doc_type: system-doc
title: "PersonTypeUsagesPVO — PVO Cross-Module"
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
  - PersonTypeUsagesPVO
  - persontypeusagespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonTypeUsagesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Person Type Usages. Acessa as tabelas: PER_PERSONS, PER_PERSON_TYPE_USAGES_M.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.PersonTypeUsagesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 2 | 1 | 10 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[per_persons|PER_PERSONS]] — 17 atributos (2 BICC)
- [[per_person_type_usages_m|PER_PERSON_TYPE_USAGES_M]] — 13 atributos (1 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[per_persons|PER_PERSONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonPEOBloodType | BLOOD_TYPE | — | — |
| 2 | PersonPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | PersonPEOCorrespondenceLanguage | CORRESPONDENCE_LANGUAGE | — | — |
| 4 | PersonPEOCountryOfBirth | COUNTRY_OF_BIRTH | — | — |
| 5 | PersonPEOCreatedBy | CREATED_BY | — | — |
| 6 | PersonPEOCreationDate | CREATION_DATE | — | — |
| 7 | PersonPEODateOfBirth | DATE_OF_BIRTH | — | — |
| 8 | PersonPEODateOfDeath | DATE_OF_DEATH | — | — |
| 9 | PersonPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | PersonPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | PersonPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | PersonPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | PersonPEOPartyId | PARTY_ID | — | — |
| 14 | PersonPEOPersonId | PERSON_ID | — | ✅ |
| 15 | PersonPEORegionOfBirth | REGION_OF_BIRTH | — | — |
| 16 | PersonPEOStartDate | START_DATE | — | — |
| 17 | PersonPEOTownOfBirth | TOWN_OF_BIRTH | — | — |

### [[per_person_type_usages_m|PER_PERSON_TYPE_USAGES_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | EffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | ✅ |
| 3 | EffectiveSequence | EFFECTIVE_SEQUENCE | — | ✅ |
| 4 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | PersonTypeUsageId | PERSON_TYPE_USAGE_ID | 🔑 | ✅ |
| 6 | PersonTypeUsagesPEOCreatedBy | CREATED_BY | — | — |
| 7 | PersonTypeUsagesPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | PersonTypeUsagesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | PersonTypeUsagesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | PersonTypeUsagesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | PersonTypeUsagesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | PersonTypeUsagesPEOPersonId | PERSON_ID | — | — |
| 13 | PersonTypeUsagesPEOSystemPersonType | SYSTEM_PERSON_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
