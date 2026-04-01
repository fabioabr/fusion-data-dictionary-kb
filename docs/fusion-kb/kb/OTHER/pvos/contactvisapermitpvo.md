---
id: DOC-OTHER-PVO-ContactVisaPermitPVO
doc_type: system-doc
title: "ContactVisaPermitPVO — PVO Cross-Module"
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
  - ContactVisaPermitPVO
  - contactvisapermitpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContactVisaPermitPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Contact Visa Permit. Acessa as tabelas: PER_ALL_PEOPLE_F, PER_CONTACT_RELSHIPS_F, PER_VISAS_PERMITS_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.ContactVisaPermitPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 32 | 3 | 3 | 24 | 75% |

---

## 🔗 Tabelas Relacionadas

- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 3 atributos (1 BICC)
- [[per_contact_relships_f|PER_CONTACT_RELSHIPS_F]] — 4 atributos (1 BICC)
- [[per_visas_permits_f|PER_VISAS_PERMITS_F]] — 25 atributos (3 PKs, 22 BICC)

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

### [[per_visas_permits_f|PER_VISAS_PERMITS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | IssuingLocation | ISSUING_LOCATION | — | ✅ |
| 4 | VisaPermitId | VISA_PERMIT_ID | 🔑 | ✅ |
| 5 | VisaPermitPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 6 | VisaPermitPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | VisaPermitPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | VisaPermitPEOCurrentVisaPermit | CURRENT_VISA_PERMIT | — | ✅ |
| 9 | VisaPermitPEOEntryDate | ENTRY_DATE | — | ✅ |
| 10 | VisaPermitPEOExpirationDate | EXPIRATION_DATE | — | ✅ |
| 11 | VisaPermitPEOIssueDate | ISSUE_DATE | — | ✅ |
| 12 | VisaPermitPEOIssuingAuthority | ISSUING_AUTHORITY | — | ✅ |
| 13 | VisaPermitPEOIssuingCountry | ISSUING_COUNTRY | — | ✅ |
| 14 | VisaPermitPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | VisaPermitPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | VisaPermitPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | VisaPermitPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 18 | VisaPermitPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | VisaPermitPEOPersonId | PERSON_ID | — | ✅ |
| 20 | VisaPermitPEOProfession | PROFESSION | — | ✅ |
| 21 | VisaPermitPEOVisaPermitCategory | VISA_PERMIT_CATEGORY | — | ✅ |
| 22 | VisaPermitPEOVisaPermitNumber | VISA_PERMIT_NUMBER | — | ✅ |
| 23 | VisaPermitPEOVisaPermitStatus | VISA_PERMIT_STATUS | — | ✅ |
| 24 | VisaPermitPEOVisaPermitStatusDate | VISA_PERMIT_STATUS_DATE | — | ✅ |
| 25 | VisaPermitPEOVisaPermitType | VISA_PERMIT_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
