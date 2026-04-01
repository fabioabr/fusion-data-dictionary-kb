---
id: DOC-OTHER-PVO-PersonNamePVOViewAll
doc_type: system-doc
title: "PersonNamePVOViewAll — PVO Cross-Module"
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
  - PersonNamePVOViewAll
  - personnamepvoviewall
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonNamePVOViewAll

## 📌 Visão Geral

View Object para extração BICC de dados de Person Name View All. Acessa as tabelas: PER_ALL_PEOPLE_F, PER_PERSONS, PER_PERSON_NAMES_F_V (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.PersonNamePVOViewAll`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 68 | 4 | 3 | 62 | 91% |

---

## 🔗 Tabelas Relacionadas

- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 5 atributos (4 BICC)
- [[per_persons|PER_PERSONS]] — 2 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 58 atributos (3 PKs, 55 BICC)
- [[per_users|PER_USERS]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | PersonDetailsPEOPersonId | PERSON_ID | — | ✅ |
| 5 | PersonDetailsPEOPersonNumber | PERSON_NUMBER | — | ✅ |

### [[per_persons|PER_PERSONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | PersonPEOPersonId | PERSON_ID | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | PersonNameId | PERSON_NAME_ID | 🔑 | ✅ |
| 4 | PersonNamePEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 5 | PersonNamePEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | PersonNamePEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | PersonNamePEODisplayName | DISPLAY_NAME | — | ✅ |
| 8 | PersonNamePEOFirstName | FIRST_NAME | — | ✅ |
| 9 | PersonNamePEOFullName | FULL_NAME | — | ✅ |
| 10 | PersonNamePEOHonors | HONORS | — | ✅ |
| 11 | PersonNamePEOKnownAs | KNOWN_AS | — | ✅ |
| 12 | PersonNamePEOLastName | LAST_NAME | — | ✅ |
| 13 | PersonNamePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | PersonNamePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | PersonNamePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | PersonNamePEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 17 | PersonNamePEOListName | LIST_NAME | — | ✅ |
| 18 | PersonNamePEOMiddleNames | MIDDLE_NAMES | — | ✅ |
| 19 | PersonNamePEOMilitaryRank | MILITARY_RANK | — | ✅ |
| 20 | PersonNamePEONamInformation1 | NAM_INFORMATION1 | — | ✅ |
| 21 | PersonNamePEONamInformation10 | NAM_INFORMATION10 | — | ✅ |
| 22 | PersonNamePEONamInformation11 | NAM_INFORMATION11 | — | ✅ |
| 23 | PersonNamePEONamInformation12 | NAM_INFORMATION12 | — | ✅ |
| 24 | PersonNamePEONamInformation13 | NAM_INFORMATION13 | — | ✅ |
| 25 | PersonNamePEONamInformation14 | NAM_INFORMATION14 | — | ✅ |
| 26 | PersonNamePEONamInformation15 | NAM_INFORMATION15 | — | ✅ |
| 27 | PersonNamePEONamInformation16 | NAM_INFORMATION16 | — | ✅ |
| 28 | PersonNamePEONamInformation17 | NAM_INFORMATION17 | — | ✅ |
| 29 | PersonNamePEONamInformation18 | NAM_INFORMATION18 | — | ✅ |
| 30 | PersonNamePEONamInformation19 | NAM_INFORMATION19 | — | ✅ |
| 31 | PersonNamePEONamInformation2 | NAM_INFORMATION2 | — | ✅ |
| 32 | PersonNamePEONamInformation20 | NAM_INFORMATION20 | — | ✅ |
| 33 | PersonNamePEONamInformation21 | NAM_INFORMATION21 | — | ✅ |
| 34 | PersonNamePEONamInformation22 | NAM_INFORMATION22 | — | ✅ |
| 35 | PersonNamePEONamInformation23 | NAM_INFORMATION23 | — | ✅ |
| 36 | PersonNamePEONamInformation24 | NAM_INFORMATION24 | — | ✅ |
| 37 | PersonNamePEONamInformation25 | NAM_INFORMATION25 | — | ✅ |
| 38 | PersonNamePEONamInformation26 | NAM_INFORMATION26 | — | ✅ |
| 39 | PersonNamePEONamInformation27 | NAM_INFORMATION27 | — | ✅ |
| 40 | PersonNamePEONamInformation28 | NAM_INFORMATION28 | — | ✅ |
| 41 | PersonNamePEONamInformation29 | NAM_INFORMATION29 | — | ✅ |
| 42 | PersonNamePEONamInformation3 | NAM_INFORMATION3 | — | ✅ |
| 43 | PersonNamePEONamInformation30 | NAM_INFORMATION30 | — | ✅ |
| 44 | PersonNamePEONamInformation4 | NAM_INFORMATION4 | — | ✅ |
| 45 | PersonNamePEONamInformation5 | NAM_INFORMATION5 | — | ✅ |
| 46 | PersonNamePEONamInformation6 | NAM_INFORMATION6 | — | ✅ |
| 47 | PersonNamePEONamInformation7 | NAM_INFORMATION7 | — | ✅ |
| 48 | PersonNamePEONamInformation8 | NAM_INFORMATION8 | — | ✅ |
| 49 | PersonNamePEONamInformation9 | NAM_INFORMATION9 | — | ✅ |
| 50 | PersonNamePEONamInformationCategory | NAM_INFORMATION_CATEGORY | — | — |
| 51 | PersonNamePEONameType | NAME_TYPE | — | ✅ |
| 52 | PersonNamePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 53 | PersonNamePEOOrderName | ORDER_NAME | — | ✅ |
| 54 | PersonNamePEOPersonId | PERSON_ID | — | ✅ |
| 55 | PersonNamePEOPreNameAdjunct | PRE_NAME_ADJUNCT | — | ✅ |
| 56 | PersonNamePEOPreviousLastName | PREVIOUS_LAST_NAME | — | ✅ |
| 57 | PersonNamePEOSuffix | SUFFIX | — | ✅ |
| 58 | PersonNamePEOTitle | TITLE | — | ✅ |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | UserPEOUserId | USER_ID | — | — |
| 3 | UserPEOUsername | USERNAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
