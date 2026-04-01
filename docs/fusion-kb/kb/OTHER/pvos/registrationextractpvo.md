---
id: DOC-OTHER-PVO-RegistrationExtractPVO
doc_type: system-doc
title: "RegistrationExtractPVO — PVO Cross-Module"
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
  - RegistrationExtractPVO
  - registrationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RegistrationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Registration Extract. Acessa as tabelas: XLE_REGISTRATIONS.

**Caminho:** `FscmTopModelAM.FinExtractAM.XleBiccExtractAM.RegistrationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 1 | 1 | 20 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xle_registrations|XLE_REGISTRATIONS]] — 20 atributos (1 PKs, 20 BICC)

---

## ⚙️ Atributos

### [[xle_registrations|XLE_REGISTRATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RegistrationAlternateRegisteredName | ALTERNATE_REGISTERED_NAME | — | ✅ |
| 2 | RegistrationCreatedBy | CREATED_BY | — | ✅ |
| 3 | RegistrationCreationDate | CREATION_DATE | — | ✅ |
| 4 | RegistrationEffectiveFrom | EFFECTIVE_FROM | — | ✅ |
| 5 | RegistrationEffectiveTo | EFFECTIVE_TO | — | ✅ |
| 6 | RegistrationIdentifyingFlag | IDENTIFYING_FLAG | — | ✅ |
| 7 | RegistrationIssuingAuthorityId | ISSUING_AUTHORITY_ID | — | ✅ |
| 8 | RegistrationIssuingAuthoritySiteId | ISSUING_AUTHORITY_SITE_ID | — | ✅ |
| 9 | RegistrationJurisdictionId | JURISDICTION_ID | — | ✅ |
| 10 | RegistrationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | RegistrationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | RegistrationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | RegistrationLocationId | LOCATION_ID | — | ✅ |
| 14 | RegistrationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | RegistrationPlaceOfRegistration | PLACE_OF_REGISTRATION | — | ✅ |
| 16 | RegistrationRegisteredName | REGISTERED_NAME | — | ✅ |
| 17 | RegistrationRegistrationId | REGISTRATION_ID | 🔑 | ✅ |
| 18 | RegistrationRegistrationNumber | REGISTRATION_NUMBER | — | ✅ |
| 19 | RegistrationSourceId | SOURCE_ID | — | ✅ |
| 20 | RegistrationSourceTable | SOURCE_TABLE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
