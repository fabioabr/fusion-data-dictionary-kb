---
id: DOC-OTHER-PVO-CandidateEmailAddressesPVO
doc_type: system-doc
title: "CandidateEmailAddressesPVO — PVO Cross-Module"
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
  - CandidateEmailAddressesPVO
  - candidateemailaddressespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CandidateEmailAddressesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Candidate Email Addresses. Acessa as tabelas: PER_EMAIL_ADDRESSES.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecCandidatesAM.CandidateEmailAddressesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 4 | 29% |

---

## 🔗 Tabelas Relacionadas

- [[per_email_addresses|PER_EMAIL_ADDRESSES]] — 14 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[per_email_addresses|PER_EMAIL_ADDRESSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | DateFrom | DATE_FROM | — | — |
| 5 | DateTo | DATE_TO | — | — |
| 6 | EmailAddress | EMAIL_ADDRESS | — | ✅ |
| 7 | EmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 8 | EmailType | EMAIL_TYPE | — | ✅ |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | MasteredInLdapFlag | MASTERED_IN_LDAP_FLAG | — | — |
| 13 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | PersonId | PERSON_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
