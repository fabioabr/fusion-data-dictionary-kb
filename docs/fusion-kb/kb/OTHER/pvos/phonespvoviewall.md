---
id: DOC-OTHER-PVO-PhonesPVOViewAll
doc_type: system-doc
title: "PhonesPVOViewAll — PVO Cross-Module"
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
  - PhonesPVOViewAll
  - phonespvoviewall
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PhonesPVOViewAll

## 📌 Visão Geral

View Object para extração BICC de dados de Phones View All. Acessa as tabelas: PER_ALL_PEOPLE_F, PER_PHONES.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.PhonesPVOViewAll`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 2 | 1 | 17 | 71% |

---

## 🔗 Tabelas Relacionadas

- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 4 atributos (1 BICC)
- [[per_phones|PER_PHONES]] — 20 atributos (1 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonDetailsPEOPersonId | PERSON_ID | — | — |
| 4 | PersonDetailsPEOPrimaryPhoneId | PRIMARY_PHONE_ID | — | — |

### [[per_phones|PER_PHONES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PhoneId | PHONE_ID | 🔑 | ✅ |
| 2 | PhonesEOAreaCode | AREA_CODE | — | ✅ |
| 3 | PhonesEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | PhonesEOCountryCodeNumber | COUNTRY_CODE_NUMBER | — | ✅ |
| 5 | PhonesEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | PhonesEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | PhonesEODateFrom | DATE_FROM | — | ✅ |
| 8 | PhonesEODateTo | DATE_TO | — | ✅ |
| 9 | PhonesEOExtension | EXTENSION | — | ✅ |
| 10 | PhonesEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | PhonesEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | PhonesEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | PhonesEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 14 | PhonesEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | PhonesEOPersonId | PERSON_ID | — | ✅ |
| 16 | PhonesEOPhoneNumber | PHONE_NUMBER | — | ✅ |
| 17 | PhonesEOPhoneType | PHONE_TYPE | — | ✅ |
| 18 | PhonesEOSearchPhoneNumber | SEARCH_PHONE_NUMBER | — | — |
| 19 | PhonesEOSpeedDialNumber | SPEED_DIAL_NUMBER | — | ✅ |
| 20 | PhonesEOValidity | VALIDITY | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
