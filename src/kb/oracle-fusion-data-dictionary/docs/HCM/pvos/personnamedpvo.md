---
id: DOC-HCM-PVO-PersonNameDPVO
doc_type: system-doc
title: "PersonNameDPVO — PVO Human Capital Management"
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
  - PersonNameDPVO
  - personnamedpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonNameDPVO

## 📌 Visão Geral

Extrai dados de nome da pessoa no contexto de hierarquia gerencial, incluindo display name, primeiro nome e nome completo. Utilizado para resolução de nomes em organogramas.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ManagerHierarchyAM.PersonNameDPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 93 | 2 | 3 | 11 | 12% |

---

## 🔗 Tabelas Relacionadas

- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 4 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 89 atributos (3 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonDPEOPersonId | PERSON_ID | — | — |
| 4 | PersonDPEOPersonNumber | PERSON_NUMBER | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute1 | ATTRIBUTE1 | — | — |
| 2 | Attribute10 | ATTRIBUTE10 | — | — |
| 3 | Attribute11 | ATTRIBUTE11 | — | — |
| 4 | Attribute12 | ATTRIBUTE12 | — | — |
| 5 | Attribute13 | ATTRIBUTE13 | — | — |
| 6 | Attribute14 | ATTRIBUTE14 | — | — |
| 7 | Attribute15 | ATTRIBUTE15 | — | — |
| 8 | Attribute16 | ATTRIBUTE16 | — | — |
| 9 | Attribute17 | ATTRIBUTE17 | — | — |
| 10 | Attribute18 | ATTRIBUTE18 | — | — |
| 11 | Attribute19 | ATTRIBUTE19 | — | — |
| 12 | Attribute2 | ATTRIBUTE2 | — | — |
| 13 | Attribute20 | ATTRIBUTE20 | — | — |
| 14 | Attribute21 | ATTRIBUTE21 | — | — |
| 15 | Attribute22 | ATTRIBUTE22 | — | — |
| 16 | Attribute23 | ATTRIBUTE23 | — | — |
| 17 | Attribute24 | ATTRIBUTE24 | — | — |
| 18 | Attribute25 | ATTRIBUTE25 | — | — |
| 19 | Attribute26 | ATTRIBUTE26 | — | — |
| 20 | Attribute27 | ATTRIBUTE27 | — | — |
| 21 | Attribute28 | ATTRIBUTE28 | — | — |
| 22 | Attribute29 | ATTRIBUTE29 | — | — |
| 23 | Attribute3 | ATTRIBUTE3 | — | — |
| 24 | Attribute30 | ATTRIBUTE30 | — | — |
| 25 | Attribute4 | ATTRIBUTE4 | — | — |
| 26 | Attribute5 | ATTRIBUTE5 | — | — |
| 27 | Attribute6 | ATTRIBUTE6 | — | — |
| 28 | Attribute7 | ATTRIBUTE7 | — | — |
| 29 | Attribute8 | ATTRIBUTE8 | — | — |
| 30 | Attribute9 | ATTRIBUTE9 | — | — |
| 31 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 32 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 33 | CreatedBy | CREATED_BY | — | — |
| 34 | CreationDate | CREATION_DATE | — | — |
| 35 | DisplayName | DISPLAY_NAME | — | ✅ |
| 36 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 37 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 38 | FirstName | FIRST_NAME | — | ✅ |
| 39 | FullName | FULL_NAME | — | ✅ |
| 40 | Honors | HONORS | — | — |
| 41 | KnownAs | KNOWN_AS | — | — |
| 42 | LastName | LAST_NAME | — | ✅ |
| 43 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 44 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 45 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 46 | LegislationCode | LEGISLATION_CODE | — | — |
| 47 | ListName | LIST_NAME | — | — |
| 48 | MiddleNames | MIDDLE_NAMES | — | — |
| 49 | MilitaryRank | MILITARY_RANK | — | — |
| 50 | NamInformation1 | NAM_INFORMATION1 | — | — |
| 51 | NamInformation10 | NAM_INFORMATION10 | — | — |
| 52 | NamInformation11 | NAM_INFORMATION11 | — | — |
| 53 | NamInformation12 | NAM_INFORMATION12 | — | — |
| 54 | NamInformation13 | NAM_INFORMATION13 | — | — |
| 55 | NamInformation14 | NAM_INFORMATION14 | — | — |
| 56 | NamInformation15 | NAM_INFORMATION15 | — | — |
| 57 | NamInformation16 | NAM_INFORMATION16 | — | — |
| 58 | NamInformation17 | NAM_INFORMATION17 | — | — |
| 59 | NamInformation18 | NAM_INFORMATION18 | — | — |
| 60 | NamInformation19 | NAM_INFORMATION19 | — | — |
| 61 | NamInformation2 | NAM_INFORMATION2 | — | — |
| 62 | NamInformation20 | NAM_INFORMATION20 | — | — |
| 63 | NamInformation21 | NAM_INFORMATION21 | — | — |
| 64 | NamInformation22 | NAM_INFORMATION22 | — | — |
| 65 | NamInformation23 | NAM_INFORMATION23 | — | — |
| 66 | NamInformation24 | NAM_INFORMATION24 | — | — |
| 67 | NamInformation25 | NAM_INFORMATION25 | — | — |
| 68 | NamInformation26 | NAM_INFORMATION26 | — | — |
| 69 | NamInformation27 | NAM_INFORMATION27 | — | — |
| 70 | NamInformation28 | NAM_INFORMATION28 | — | — |
| 71 | NamInformation29 | NAM_INFORMATION29 | — | — |
| 72 | NamInformation3 | NAM_INFORMATION3 | — | — |
| 73 | NamInformation30 | NAM_INFORMATION30 | — | — |
| 74 | NamInformation4 | NAM_INFORMATION4 | — | — |
| 75 | NamInformation5 | NAM_INFORMATION5 | — | — |
| 76 | NamInformation6 | NAM_INFORMATION6 | — | — |
| 77 | NamInformation7 | NAM_INFORMATION7 | — | — |
| 78 | NamInformation8 | NAM_INFORMATION8 | — | — |
| 79 | NamInformation9 | NAM_INFORMATION9 | — | — |
| 80 | NamInformationCategory | NAM_INFORMATION_CATEGORY | — | — |
| 81 | NameType | NAME_TYPE | — | — |
| 82 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 83 | OrderName | ORDER_NAME | — | — |
| 84 | PersonId | PERSON_ID | — | ✅ |
| 85 | PersonNameId | PERSON_NAME_ID | 🔑 | ✅ |
| 86 | PreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 87 | PreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 88 | Suffix | SUFFIX | — | — |
| 89 | Title | TITLE | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
