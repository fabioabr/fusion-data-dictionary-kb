---
id: DOC-HCM-PVO-PersonPVO
doc_type: system-doc
title: "PersonPVO — PVO Human Capital Management"
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
  - PersonPVO
  - personpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonPVO

## 📌 Visão Geral

Extrai dados pessoais básicos dos colaboradores (tipo sanguíneo, idioma de correspondência, business group). Dimensão fundamental de pessoa para cruzamento entre módulos HCM.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.PersonPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 1 | 15 | 83% |

---

## 🔗 Tabelas Relacionadas

- [[per_persons|PER_PERSONS]] — 18 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[per_persons|PER_PERSONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonId | PERSON_ID | 🔑 | ✅ |
| 2 | PersonPEOBloodType | BLOOD_TYPE | — | ✅ |
| 3 | PersonPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 4 | PersonPEOCorrespondenceLanguage | CORRESPONDENCE_LANGUAGE | — | ✅ |
| 5 | PersonPEOCountryOfBirth | COUNTRY_OF_BIRTH | — | ✅ |
| 6 | PersonPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | PersonPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | PersonPEODateOfBirth | DATE_OF_BIRTH | — | ✅ |
| 9 | PersonPEODateOfDeath | DATE_OF_DEATH | — | ✅ |
| 10 | PersonPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | PersonPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | PersonPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | PersonPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | PersonPEOPartyId | PARTY_ID | — | ✅ |
| 15 | PersonPEORegionOfBirth | REGION_OF_BIRTH | — | ✅ |
| 16 | PersonPEOStartDate | START_DATE | — | ✅ |
| 17 | PersonPEOTownOfBirth | TOWN_OF_BIRTH | — | ✅ |
| 18 | PersonPEOUserGuid | USER_GUID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
