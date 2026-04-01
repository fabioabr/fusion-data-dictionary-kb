---
id: DOC-OTHER-PVO-LegalEntityProfilePVO
doc_type: system-doc
title: "LegalEntityProfilePVO — PVO Cross-Module"
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
  - LegalEntityProfilePVO
  - legalentityprofilepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LegalEntityProfilePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Legal Entity Profile. Acessa as tabelas: XLE_ENTITY_PROFILES.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.OrganizationAM.LegalEntityProfilePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 73 | 1 | 1 | 3 | 4% |

---

## 🔗 Tabelas Relacionadas

- [[xle_entity_profiles|XLE_ENTITY_PROFILES]] — 73 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[xle_entity_profiles|XLE_ENTITY_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActivityCode | ACTIVITY_CODE | — | — |
| 2 | Attribute1 | ATTRIBUTE1 | — | — |
| 3 | Attribute10 | ATTRIBUTE10 | — | — |
| 4 | Attribute11 | ATTRIBUTE11 | — | — |
| 5 | Attribute12 | ATTRIBUTE12 | — | — |
| 6 | Attribute13 | ATTRIBUTE13 | — | — |
| 7 | Attribute14 | ATTRIBUTE14 | — | — |
| 8 | Attribute15 | ATTRIBUTE15 | — | — |
| 9 | Attribute16 | ATTRIBUTE16 | — | — |
| 10 | Attribute17 | ATTRIBUTE17 | — | — |
| 11 | Attribute18 | ATTRIBUTE18 | — | — |
| 12 | Attribute19 | ATTRIBUTE19 | — | — |
| 13 | Attribute2 | ATTRIBUTE2 | — | — |
| 14 | Attribute20 | ATTRIBUTE20 | — | — |
| 15 | Attribute3 | ATTRIBUTE3 | — | — |
| 16 | Attribute4 | ATTRIBUTE4 | — | — |
| 17 | Attribute5 | ATTRIBUTE5 | — | — |
| 18 | Attribute6 | ATTRIBUTE6 | — | — |
| 19 | Attribute7 | ATTRIBUTE7 | — | — |
| 20 | Attribute8 | ATTRIBUTE8 | — | — |
| 21 | Attribute9 | ATTRIBUTE9 | — | — |
| 22 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 23 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 29 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 30 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 31 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 32 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 33 | CreatedBy | CREATED_BY | — | — |
| 34 | CreationDate | CREATION_DATE | — | — |
| 35 | EffectiveFrom | EFFECTIVE_FROM | — | — |
| 36 | EffectiveTo | EFFECTIVE_TO | — | — |
| 37 | EnterpriseId | ENTERPRISE_ID | — | — |
| 38 | GeographyId | GEOGRAPHY_ID | — | — |
| 39 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 40 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 41 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 42 | LeInformation1 | LE_INFORMATION1 | — | — |
| 43 | LeInformation10 | LE_INFORMATION10 | — | — |
| 44 | LeInformation11 | LE_INFORMATION11 | — | — |
| 45 | LeInformation12 | LE_INFORMATION12 | — | — |
| 46 | LeInformation13 | LE_INFORMATION13 | — | — |
| 47 | LeInformation14 | LE_INFORMATION14 | — | — |
| 48 | LeInformation15 | LE_INFORMATION15 | — | — |
| 49 | LeInformation16 | LE_INFORMATION16 | — | — |
| 50 | LeInformation17 | LE_INFORMATION17 | — | — |
| 51 | LeInformation18 | LE_INFORMATION18 | — | — |
| 52 | LeInformation19 | LE_INFORMATION19 | — | — |
| 53 | LeInformation2 | LE_INFORMATION2 | — | — |
| 54 | LeInformation20 | LE_INFORMATION20 | — | — |
| 55 | LeInformation3 | LE_INFORMATION3 | — | — |
| 56 | LeInformation4 | LE_INFORMATION4 | — | — |
| 57 | LeInformation5 | LE_INFORMATION5 | — | — |
| 58 | LeInformation6 | LE_INFORMATION6 | — | — |
| 59 | LeInformation7 | LE_INFORMATION7 | — | — |
| 60 | LeInformation8 | LE_INFORMATION8 | — | — |
| 61 | LeInformation9 | LE_INFORMATION9 | — | — |
| 62 | LeInformationContext | LE_INFORMATION_CONTEXT | — | — |
| 63 | LegalEmployerFlag | LEGAL_EMPLOYER_FLAG | — | — |
| 64 | LegalEntityId | LEGAL_ENTITY_ID | 🔑 | ✅ |
| 65 | LegalEntityIdentifier | LEGAL_ENTITY_IDENTIFIER | — | ✅ |
| 66 | Name | NAME | — | — |
| 67 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 68 | ParentPsuId | PARENT_PSU_ID | — | — |
| 69 | PartyId | PARTY_ID | — | — |
| 70 | PsuFlag | PSU_FLAG | — | — |
| 71 | SubActivityCode | SUB_ACTIVITY_CODE | — | — |
| 72 | TransactingEntityFlag | TRANSACTING_ENTITY_FLAG | — | — |
| 73 | TypeOfCompany | TYPE_OF_COMPANY | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
