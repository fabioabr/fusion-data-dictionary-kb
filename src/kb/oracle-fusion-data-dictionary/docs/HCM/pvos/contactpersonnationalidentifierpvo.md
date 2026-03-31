---
id: DOC-HCM-PVO-ContactPersonNationalIdentifierPVO
doc_type: system-doc
title: "ContactPersonNationalIdentifierPVO — PVO Human Capital Management"
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
  - ContactPersonNationalIdentifierPVO
  - contactpersonnationalidentifierpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContactPersonNationalIdentifierPVO

## 📌 Visão Geral

Extrai identificadores nacionais (CPF, RG) de contatos/dependentes. Fundamental para compliance fiscal e cadastro de beneficiarios de planos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.ContactPersonNationalIdentifierPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 3 | 1 | 14 | 61% |

---

## 🔗 Tabelas Relacionadas

- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 4 atributos (1 BICC)
- [[per_contact_relships_f|PER_CONTACT_RELSHIPS_F]] — 4 atributos (1 BICC)
- [[per_national_identifiers|PER_NATIONAL_IDENTIFIERS]] — 15 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContactPersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | ContactPersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | ContactPersonDetailsPEOPersonId | PERSON_ID | — | — |
| 4 | ContactPersonDetailsPEOPrimaryNidId | PRIMARY_NID_ID | — | — |

### [[per_contact_relships_f|PER_CONTACT_RELSHIPS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContactRelshipsPEOContactRelationshipId | CONTACT_RELATIONSHIP_ID | — | — |
| 2 | ContactRelshipsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | ContactRelshipsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | ContactRelshipsPEOPersonId | PERSON_ID | — | — |

### [[per_national_identifiers|PER_NATIONAL_IDENTIFIERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NationalIdentifierId | NATIONAL_IDENTIFIER_ID | 🔑 | ✅ |
| 2 | NationalIdentifierPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | NationalIdentifierPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | NationalIdentifierPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | NationalIdentifierPEOExpirationDate | EXPIRATION_DATE | — | ✅ |
| 6 | NationalIdentifierPEOIssueDate | ISSUE_DATE | — | ✅ |
| 7 | NationalIdentifierPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | NationalIdentifierPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | NationalIdentifierPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | NationalIdentifierPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 11 | NationalIdentifierPEONationalIdentifierNumber | NATIONAL_IDENTIFIER_NUMBER | — | ✅ |
| 12 | NationalIdentifierPEONationalIdentifierType | NATIONAL_IDENTIFIER_TYPE | — | ✅ |
| 13 | NationalIdentifierPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | NationalIdentifierPEOPersonId | PERSON_ID | — | ✅ |
| 15 | NationalIdentifierPEOPlaceOfIssue | PLACE_OF_ISSUE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
