---
id: DOC-HCM-PVO-PersonDetailsPVO
doc_type: system-doc
title: "PersonDetailsPVO — PVO Human Capital Management"
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
  - PersonDetailsPVO
  - persondetailspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonDetailsPVO

## 📌 Visão Geral

Extrai detalhes cadastrais da pessoa (date-effective), como número de candidato e dados básicos de identificação. Serve como dimensão central para cruzamento com outros objetos HCM.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.PersonDetailsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 1 | 1 | 15 | 79% |

---

## 🔗 Tabelas Relacionadas

- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 19 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonDetailsPEOApplicantNumber | APPLICANT_NUMBER | — | ✅ |
| 4 | PersonDetailsPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 5 | PersonDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | PersonDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | PersonDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PersonDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | PersonDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | PersonDetailsPEOMailingAddressId | MAILING_ADDRESS_ID | — | — |
| 11 | PersonDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | PersonDetailsPEOPersonNumber | PERSON_NUMBER | — | ✅ |
| 13 | PersonDetailsPEOPrimaryEmailId | PRIMARY_EMAIL_ID | — | ✅ |
| 14 | PersonDetailsPEOPrimaryNidId | PRIMARY_NID_ID | — | — |
| 15 | PersonDetailsPEOPrimaryNidNumber | PRIMARY_NID_NUMBER | — | ✅ |
| 16 | PersonDetailsPEOPrimaryPhoneId | PRIMARY_PHONE_ID | — | ✅ |
| 17 | PersonDetailsPEOStartDate | START_DATE | — | ✅ |
| 18 | PersonDetailsPEOWaiveDataProtect | WAIVE_DATA_PROTECT | — | ✅ |
| 19 | PersonId | PERSON_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
