---
id: DOC-HCM-PVO-ContactEmailAddressesPVO
doc_type: system-doc
title: "ContactEmailAddressesPVO — PVO Human Capital Management"
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
  - ContactEmailAddressesPVO
  - contactemailaddressespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContactEmailAddressesPVO

## 📌 Visão Geral

Extrai e-mails de contatos/dependentes de colaboradores com vinculo de relacionamento. Suporta comunicacao com beneficiarios e dependentes.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.ContactEmailAddressesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 3 | 1 | 13 | 59% |

---

## 🔗 Tabelas Relacionadas

- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 4 atributos (1 BICC)
- [[per_contact_relships_f|PER_CONTACT_RELSHIPS_F]] — 4 atributos (1 BICC)
- [[per_email_addresses|PER_EMAIL_ADDRESSES]] — 14 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContactPersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | ContactPersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | ContactPersonDetailsPEOPersonId | PERSON_ID | — | — |
| 4 | ContactPersonDetailsPEOPrimaryEmailId | PRIMARY_EMAIL_ID | — | — |

### [[per_contact_relships_f|PER_CONTACT_RELSHIPS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContactRelshipsPEOContactRelationshipId | CONTACT_RELATIONSHIP_ID | — | — |
| 2 | ContactRelshipsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | ContactRelshipsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | ContactRelshipsPEOPersonId | PERSON_ID | — | — |

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

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
