---
id: DOC-HCM-PVO-CandidatePhonesPVO
doc_type: system-doc
title: "CandidatePhonesPVO — PVO Human Capital Management"
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
  - CandidatePhonesPVO
  - candidatephonespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CandidatePhonesPVO

## 📌 Visão Geral

Extrai telefones de candidatos com codigo de area e pais. Suporta contato telefonico e gestao de comunicacao com candidatos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecCandidatesAM.CandidatePhonesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 1 | 1 | 6 | 30% |

---

## 🔗 Tabelas Relacionadas

- [[per_phones|PER_PHONES]] — 20 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[per_phones|PER_PHONES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PhoneId | PHONE_ID | — | — |
| 2 | PhonesEOAreaCode | AREA_CODE | — | ✅ |
| 3 | PhonesEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | PhonesEOCountryCodeNumber | COUNTRY_CODE_NUMBER | — | ✅ |
| 5 | PhonesEOCreatedBy | CREATED_BY | — | — |
| 6 | PhonesEOCreationDate | CREATION_DATE | — | — |
| 7 | PhonesEODateFrom | DATE_FROM | — | — |
| 8 | PhonesEODateTo | DATE_TO | — | — |
| 9 | PhonesEOExtension | EXTENSION | — | — |
| 10 | PhonesEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | PhonesEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | PhonesEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | PhonesEOLegislationCode | LEGISLATION_CODE | — | — |
| 14 | PhonesEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | PhonesEOPersonId | PERSON_ID | 🔑 | ✅ |
| 16 | PhonesEOPhoneNumber | PHONE_NUMBER | — | ✅ |
| 17 | PhonesEOPhoneType | PHONE_TYPE | — | ✅ |
| 18 | PhonesEOSearchPhoneNumber | SEARCH_PHONE_NUMBER | — | — |
| 19 | PhonesEOSpeedDialNumber | SPEED_DIAL_NUMBER | — | — |
| 20 | Validity | VALIDITY | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
