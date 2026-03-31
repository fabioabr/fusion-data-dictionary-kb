---
id: DOC-OTHER-PVO-EmailAddressesPVO
doc_type: system-doc
title: "EmailAddressesPVO — PVO Cross-Module"
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
  - EmailAddressesPVO
  - emailaddressespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EmailAddressesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Email Addresses. Acessa as tabelas: PER_ALL_PEOPLE_F, PER_EMAIL_ADDRESSES.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.EmailAddressesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 2 | 1 | 12 | 67% |

---

## 🔗 Tabelas Relacionadas

- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 4 atributos (1 BICC)
- [[per_email_addresses|PER_EMAIL_ADDRESSES]] — 14 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonDetailsPEOPersonId | PERSON_ID | — | — |
| 4 | PersonDetailsPEOPrimaryEmailId | PRIMARY_EMAIL_ID | — | — |

### [[per_email_addresses|PER_EMAIL_ADDRESSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EmailAddressId | EMAIL_ADDRESS_ID | 🔑 | ✅ |
| 2 | EmailAddressesPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | EmailAddressesPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | EmailAddressesPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | EmailAddressesPEODateFrom | DATE_FROM | — | ✅ |
| 6 | EmailAddressesPEODateTo | DATE_TO | — | ✅ |
| 7 | EmailAddressesPEOEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 8 | EmailAddressesPEOEmailType | EMAIL_TYPE | — | ✅ |
| 9 | EmailAddressesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | EmailAddressesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | EmailAddressesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | EmailAddressesPEOMasteredInLdapFlag | MASTERED_IN_LDAP_FLAG | — | ✅ |
| 13 | EmailAddressesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | EmailAddressesPEOPersonId | PERSON_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
