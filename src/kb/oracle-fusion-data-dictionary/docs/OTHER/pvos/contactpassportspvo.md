---
id: DOC-OTHER-PVO-ContactPassportsPVO
doc_type: system-doc
title: "ContactPassportsPVO — PVO Cross-Module"
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
  - ContactPassportsPVO
  - contactpassportspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContactPassportsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Contact Passports. Acessa as tabelas: PER_ALL_PEOPLE_F, PER_CONTACT_RELSHIPS_F, PER_PASSPORTS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.ContactPassportsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 3 | 1 | 17 | 68% |

---

## 🔗 Tabelas Relacionadas

- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 3 atributos (1 BICC)
- [[per_contact_relships_f|PER_CONTACT_RELSHIPS_F]] — 4 atributos (1 BICC)
- [[per_passports|PER_PASSPORTS]] — 18 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContactPersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | ContactPersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | ContactPersonDetailsPEOPersonId | PERSON_ID | — | — |

### [[per_contact_relships_f|PER_CONTACT_RELSHIPS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContactRelshipsPEOContactRelationshipId | CONTACT_RELATIONSHIP_ID | — | — |
| 2 | ContactRelshipsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | ContactRelshipsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | ContactRelshipsPEOPersonId | PERSON_ID | — | — |

### [[per_passports|PER_PASSPORTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PassportId | PASSPORT_ID | 🔑 | ✅ |
| 2 | PassportsPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | PassportsPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | PassportsPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | PassportsPEOExpirationDate | EXPIRATION_DATE | — | ✅ |
| 6 | PassportsPEOIssueDate | ISSUE_DATE | — | ✅ |
| 7 | PassportsPEOIssuingAuthority | ISSUING_AUTHORITY | — | ✅ |
| 8 | PassportsPEOIssuingCountry | ISSUING_COUNTRY | — | ✅ |
| 9 | PassportsPEOIssuingLocation | ISSUING_LOCATION | — | ✅ |
| 10 | PassportsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | PassportsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | PassportsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | PassportsPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 14 | PassportsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | PassportsPEOPassportNumber | PASSPORT_NUMBER | — | ✅ |
| 16 | PassportsPEOPassportType | PASSPORT_TYPE | — | ✅ |
| 17 | PassportsPEOPersonId | PERSON_ID | — | ✅ |
| 18 | PassportsPEOProfession | PROFESSION | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
