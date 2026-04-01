---
id: DOC-HCM-PVO-PersonPhonePVO
doc_type: system-doc
title: "PersonPhonePVO — PVO Human Capital Management"
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
  - PersonPhonePVO
  - personphonepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonPhonePVO

## 📌 Visão Geral

Extrai números de telefone dos colaboradores vinculados ao cadastro de pessoa. Utilizado para diretório de contatos, comunicações de emergência e integrações de RH.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.PersonPhonePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 38 | 2 | 1 | 14 | 37% |

---

## 🔗 Tabelas Relacionadas

- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 18 atributos (4 BICC)
- [[per_phones|PER_PHONES]] — 20 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonDetailsPEOApplicantNumber | APPLICANT_NUMBER | — | — |
| 2 | PersonDetailsPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 3 | PersonDetailsPEOCreatedBy | CREATED_BY | — | — |
| 4 | PersonDetailsPEOCreationDate | CREATION_DATE | — | — |
| 5 | PersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | PersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | PersonDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PersonDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | PersonDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | PersonDetailsPEOMailingAddressId | MAILING_ADDRESS_ID | — | — |
| 11 | PersonDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | PersonDetailsPEOPersonId | PERSON_ID | — | — |
| 13 | PersonDetailsPEOPersonNumber | PERSON_NUMBER | — | — |
| 14 | PersonDetailsPEOPrimaryEmailId | PRIMARY_EMAIL_ID | — | — |
| 15 | PersonDetailsPEOPrimaryNidNumber | PRIMARY_NID_NUMBER | — | — |
| 16 | PersonDetailsPEOPrimaryPhoneId | PRIMARY_PHONE_ID | — | ✅ |
| 17 | PersonDetailsPEOStartDate | START_DATE | — | — |
| 18 | PersonDetailsPEOWaiveDataProtect | WAIVE_DATA_PROTECT | — | — |

### [[per_phones|PER_PHONES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PhoneId | PHONE_ID | 🔑 | ✅ |
| 2 | PhonesEOAreaCode | AREA_CODE | — | ✅ |
| 3 | PhonesEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | PhonesEOCountryCodeNumber | COUNTRY_CODE_NUMBER | — | ✅ |
| 5 | PhonesEOCreatedBy | CREATED_BY | — | — |
| 6 | PhonesEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | PhonesEODateFrom | DATE_FROM | — | ✅ |
| 8 | PhonesEODateTo | DATE_TO | — | ✅ |
| 9 | PhonesEOExtension | EXTENSION | — | — |
| 10 | PhonesEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | PhonesEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | PhonesEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | PhonesEOLegislationCode | LEGISLATION_CODE | — | — |
| 14 | PhonesEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | PhonesEOPersonId | PERSON_ID | — | ✅ |
| 16 | PhonesEOPhoneNumber | PHONE_NUMBER | — | ✅ |
| 17 | PhonesEOPhoneType | PHONE_TYPE | — | ✅ |
| 18 | PhonesEOSearchPhoneNumber | SEARCH_PHONE_NUMBER | — | — |
| 19 | PhonesEOSpeedDialNumber | SPEED_DIAL_NUMBER | — | — |
| 20 | PhonesEOValidity | VALIDITY | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
