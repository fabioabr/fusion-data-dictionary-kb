---
id: DOC-OTHER-PVO-PersonLegislativeInfoPVO
doc_type: system-doc
title: "PersonLegislativeInfoPVO — PVO Cross-Module"
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
  - PersonLegislativeInfoPVO
  - personlegislativeinfopvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonLegislativeInfoPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Person Legislative Info. Acessa as tabelas: PER_PEOPLE_LEGISLATIVE_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.PersonLegislativeInfoPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 148 | 1 | 2 | 27 | 18% |

---

## 🔗 Tabelas Relacionadas

- [[per_people_legislative_f|PER_PEOPLE_LEGISLATIVE_F]] — 148 atributos (2 PKs, 27 BICC)

---

## ⚙️ Atributos

### [[per_people_legislative_f|PER_PEOPLE_LEGISLATIVE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | PersonLegislativeId | PERSON_LEGISLATIVE_ID | 🔑 | ✅ |
| 4 | PersonLegislativeInfoDPEOAttribute1 | ATTRIBUTE1 | — | — |
| 5 | PersonLegislativeInfoDPEOAttribute10 | ATTRIBUTE10 | — | — |
| 6 | PersonLegislativeInfoDPEOAttribute11 | ATTRIBUTE11 | — | — |
| 7 | PersonLegislativeInfoDPEOAttribute12 | ATTRIBUTE12 | — | — |
| 8 | PersonLegislativeInfoDPEOAttribute13 | ATTRIBUTE13 | — | — |
| 9 | PersonLegislativeInfoDPEOAttribute14 | ATTRIBUTE14 | — | — |
| 10 | PersonLegislativeInfoDPEOAttribute15 | ATTRIBUTE15 | — | — |
| 11 | PersonLegislativeInfoDPEOAttribute16 | ATTRIBUTE16 | — | — |
| 12 | PersonLegislativeInfoDPEOAttribute17 | ATTRIBUTE17 | — | — |
| 13 | PersonLegislativeInfoDPEOAttribute18 | ATTRIBUTE18 | — | — |
| 14 | PersonLegislativeInfoDPEOAttribute19 | ATTRIBUTE19 | — | — |
| 15 | PersonLegislativeInfoDPEOAttribute2 | ATTRIBUTE2 | — | — |
| 16 | PersonLegislativeInfoDPEOAttribute20 | ATTRIBUTE20 | — | — |
| 17 | PersonLegislativeInfoDPEOAttribute21 | ATTRIBUTE21 | — | — |
| 18 | PersonLegislativeInfoDPEOAttribute22 | ATTRIBUTE22 | — | — |
| 19 | PersonLegislativeInfoDPEOAttribute23 | ATTRIBUTE23 | — | — |
| 20 | PersonLegislativeInfoDPEOAttribute24 | ATTRIBUTE24 | — | — |
| 21 | PersonLegislativeInfoDPEOAttribute25 | ATTRIBUTE25 | — | — |
| 22 | PersonLegislativeInfoDPEOAttribute26 | ATTRIBUTE26 | — | — |
| 23 | PersonLegislativeInfoDPEOAttribute27 | ATTRIBUTE27 | — | — |
| 24 | PersonLegislativeInfoDPEOAttribute28 | ATTRIBUTE28 | — | — |
| 25 | PersonLegislativeInfoDPEOAttribute29 | ATTRIBUTE29 | — | — |
| 26 | PersonLegislativeInfoDPEOAttribute3 | ATTRIBUTE3 | — | — |
| 27 | PersonLegislativeInfoDPEOAttribute30 | ATTRIBUTE30 | — | — |
| 28 | PersonLegislativeInfoDPEOAttribute4 | ATTRIBUTE4 | — | — |
| 29 | PersonLegislativeInfoDPEOAttribute5 | ATTRIBUTE5 | — | — |
| 30 | PersonLegislativeInfoDPEOAttribute6 | ATTRIBUTE6 | — | — |
| 31 | PersonLegislativeInfoDPEOAttribute7 | ATTRIBUTE7 | — | — |
| 32 | PersonLegislativeInfoDPEOAttribute8 | ATTRIBUTE8 | — | — |
| 33 | PersonLegislativeInfoDPEOAttribute9 | ATTRIBUTE9 | — | — |
| 34 | PersonLegislativeInfoDPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 35 | PersonLegislativeInfoDPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 36 | PersonLegislativeInfoDPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 37 | PersonLegislativeInfoDPEOAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 38 | PersonLegislativeInfoDPEOAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 39 | PersonLegislativeInfoDPEOAttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 40 | PersonLegislativeInfoDPEOAttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 41 | PersonLegislativeInfoDPEOAttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 42 | PersonLegislativeInfoDPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 43 | PersonLegislativeInfoDPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 44 | PersonLegislativeInfoDPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 45 | PersonLegislativeInfoDPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 46 | PersonLegislativeInfoDPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 47 | PersonLegislativeInfoDPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 48 | PersonLegislativeInfoDPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 49 | PersonLegislativeInfoDPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 50 | PersonLegislativeInfoDPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 51 | PersonLegislativeInfoDPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 52 | PersonLegislativeInfoDPEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 53 | PersonLegislativeInfoDPEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 54 | PersonLegislativeInfoDPEOAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 55 | PersonLegislativeInfoDPEOAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 56 | PersonLegislativeInfoDPEOAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 57 | PersonLegislativeInfoDPEOAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 58 | PersonLegislativeInfoDPEOAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 59 | PersonLegislativeInfoDPEOAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 60 | PersonLegislativeInfoDPEOAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 61 | PersonLegislativeInfoDPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 62 | PersonLegislativeInfoDPEOAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 63 | PersonLegislativeInfoDPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 64 | PersonLegislativeInfoDPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 65 | PersonLegislativeInfoDPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 66 | PersonLegislativeInfoDPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 67 | PersonLegislativeInfoDPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 68 | PersonLegislativeInfoDPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 69 | PersonLegislativeInfoDPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 70 | PersonLegislativeInfoDPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 71 | PersonLegislativeInfoDPEOCreatedBy | CREATED_BY | — | ✅ |
| 72 | PersonLegislativeInfoDPEOCreationDate | CREATION_DATE | — | ✅ |
| 73 | PersonLegislativeInfoDPEOHighestEducationLevel | HIGHEST_EDUCATION_LEVEL | — | ✅ |
| 74 | PersonLegislativeInfoDPEOInformation1 | PER_INFORMATION1 | — | — |
| 75 | PersonLegislativeInfoDPEOInformation10 | PER_INFORMATION10 | — | ✅ |
| 76 | PersonLegislativeInfoDPEOInformation11 | PER_INFORMATION11 | — | ✅ |
| 77 | PersonLegislativeInfoDPEOInformation12 | PER_INFORMATION12 | — | ✅ |
| 78 | PersonLegislativeInfoDPEOInformation13 | PER_INFORMATION13 | — | ✅ |
| 79 | PersonLegislativeInfoDPEOInformation14 | PER_INFORMATION14 | — | ✅ |
| 80 | PersonLegislativeInfoDPEOInformation15 | PER_INFORMATION15 | — | ✅ |
| 81 | PersonLegislativeInfoDPEOInformation16 | PER_INFORMATION16 | — | ✅ |
| 82 | PersonLegislativeInfoDPEOInformation17 | PER_INFORMATION17 | — | ✅ |
| 83 | PersonLegislativeInfoDPEOInformation18 | PER_INFORMATION18 | — | ✅ |
| 84 | PersonLegislativeInfoDPEOInformation19 | PER_INFORMATION19 | — | ✅ |
| 85 | PersonLegislativeInfoDPEOInformation2 | PER_INFORMATION2 | — | — |
| 86 | PersonLegislativeInfoDPEOInformation20 | PER_INFORMATION20 | — | — |
| 87 | PersonLegislativeInfoDPEOInformation21 | PER_INFORMATION21 | — | — |
| 88 | PersonLegislativeInfoDPEOInformation22 | PER_INFORMATION22 | — | — |
| 89 | PersonLegislativeInfoDPEOInformation23 | PER_INFORMATION23 | — | — |
| 90 | PersonLegislativeInfoDPEOInformation24 | PER_INFORMATION24 | — | — |
| 91 | PersonLegislativeInfoDPEOInformation25 | PER_INFORMATION25 | — | — |
| 92 | PersonLegislativeInfoDPEOInformation26 | PER_INFORMATION26 | — | — |
| 93 | PersonLegislativeInfoDPEOInformation27 | PER_INFORMATION27 | — | — |
| 94 | PersonLegislativeInfoDPEOInformation28 | PER_INFORMATION28 | — | — |
| 95 | PersonLegislativeInfoDPEOInformation29 | PER_INFORMATION29 | — | — |
| 96 | PersonLegislativeInfoDPEOInformation3 | PER_INFORMATION3 | — | — |
| 97 | PersonLegislativeInfoDPEOInformation30 | PER_INFORMATION30 | — | — |
| 98 | PersonLegislativeInfoDPEOInformation4 | PER_INFORMATION4 | — | — |
| 99 | PersonLegislativeInfoDPEOInformation5 | PER_INFORMATION5 | — | — |
| 100 | PersonLegislativeInfoDPEOInformation6 | PER_INFORMATION6 | — | — |
| 101 | PersonLegislativeInfoDPEOInformation7 | PER_INFORMATION7 | — | — |
| 102 | PersonLegislativeInfoDPEOInformation8 | PER_INFORMATION8 | — | — |
| 103 | PersonLegislativeInfoDPEOInformation9 | PER_INFORMATION9 | — | — |
| 104 | PersonLegislativeInfoDPEOInformationCategory | PER_INFORMATION_CATEGORY | — | ✅ |
| 105 | PersonLegislativeInfoDPEOInformationDate1 | PER_INFORMATION_DATE1 | — | — |
| 106 | PersonLegislativeInfoDPEOInformationDate10 | PER_INFORMATION_DATE10 | — | — |
| 107 | PersonLegislativeInfoDPEOInformationDate11 | PER_INFORMATION_DATE11 | — | — |
| 108 | PersonLegislativeInfoDPEOInformationDate12 | PER_INFORMATION_DATE12 | — | — |
| 109 | PersonLegislativeInfoDPEOInformationDate13 | PER_INFORMATION_DATE13 | — | — |
| 110 | PersonLegislativeInfoDPEOInformationDate14 | PER_INFORMATION_DATE14 | — | — |
| 111 | PersonLegislativeInfoDPEOInformationDate15 | PER_INFORMATION_DATE15 | — | — |
| 112 | PersonLegislativeInfoDPEOInformationDate2 | PER_INFORMATION_DATE2 | — | — |
| 113 | PersonLegislativeInfoDPEOInformationDate3 | PER_INFORMATION_DATE3 | — | — |
| 114 | PersonLegislativeInfoDPEOInformationDate4 | PER_INFORMATION_DATE4 | — | — |
| 115 | PersonLegislativeInfoDPEOInformationDate5 | PER_INFORMATION_DATE5 | — | — |
| 116 | PersonLegislativeInfoDPEOInformationDate6 | PER_INFORMATION_DATE6 | — | — |
| 117 | PersonLegislativeInfoDPEOInformationDate7 | PER_INFORMATION_DATE7 | — | — |
| 118 | PersonLegislativeInfoDPEOInformationDate8 | PER_INFORMATION_DATE8 | — | — |
| 119 | PersonLegislativeInfoDPEOInformationDate9 | PER_INFORMATION_DATE9 | — | — |
| 120 | PersonLegislativeInfoDPEOInformationNumber1 | PER_INFORMATION_NUMBER1 | — | — |
| 121 | PersonLegislativeInfoDPEOInformationNumber10 | PER_INFORMATION_NUMBER10 | — | — |
| 122 | PersonLegislativeInfoDPEOInformationNumber11 | PER_INFORMATION_NUMBER11 | — | — |
| 123 | PersonLegislativeInfoDPEOInformationNumber12 | PER_INFORMATION_NUMBER12 | — | — |
| 124 | PersonLegislativeInfoDPEOInformationNumber13 | PER_INFORMATION_NUMBER13 | — | — |
| 125 | PersonLegislativeInfoDPEOInformationNumber14 | PER_INFORMATION_NUMBER14 | — | — |
| 126 | PersonLegislativeInfoDPEOInformationNumber15 | PER_INFORMATION_NUMBER15 | — | — |
| 127 | PersonLegislativeInfoDPEOInformationNumber16 | PER_INFORMATION_NUMBER16 | — | — |
| 128 | PersonLegislativeInfoDPEOInformationNumber17 | PER_INFORMATION_NUMBER17 | — | — |
| 129 | PersonLegislativeInfoDPEOInformationNumber18 | PER_INFORMATION_NUMBER18 | — | — |
| 130 | PersonLegislativeInfoDPEOInformationNumber19 | PER_INFORMATION_NUMBER19 | — | — |
| 131 | PersonLegislativeInfoDPEOInformationNumber2 | PER_INFORMATION_NUMBER2 | — | — |
| 132 | PersonLegislativeInfoDPEOInformationNumber20 | PER_INFORMATION_NUMBER20 | — | — |
| 133 | PersonLegislativeInfoDPEOInformationNumber3 | PER_INFORMATION_NUMBER3 | — | — |
| 134 | PersonLegislativeInfoDPEOInformationNumber4 | PER_INFORMATION_NUMBER4 | — | — |
| 135 | PersonLegislativeInfoDPEOInformationNumber5 | PER_INFORMATION_NUMBER5 | — | — |
| 136 | PersonLegislativeInfoDPEOInformationNumber6 | PER_INFORMATION_NUMBER6 | — | — |
| 137 | PersonLegislativeInfoDPEOInformationNumber7 | PER_INFORMATION_NUMBER7 | — | — |
| 138 | PersonLegislativeInfoDPEOInformationNumber8 | PER_INFORMATION_NUMBER8 | — | — |
| 139 | PersonLegislativeInfoDPEOInformationNumber9 | PER_INFORMATION_NUMBER9 | — | — |
| 140 | PersonLegislativeInfoDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 141 | PersonLegislativeInfoDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 142 | PersonLegislativeInfoDPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 143 | PersonLegislativeInfoDPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 144 | PersonLegislativeInfoDPEOMaritalStatus | MARITAL_STATUS | — | ✅ |
| 145 | PersonLegislativeInfoDPEOMaritalStatusDate | MARITAL_STATUS_DATE | — | ✅ |
| 146 | PersonLegislativeInfoDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 147 | PersonLegislativeInfoDPEOPersonId | PERSON_ID | — | ✅ |
| 148 | PersonLegislativeInfoDPEOSex | SEX | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
