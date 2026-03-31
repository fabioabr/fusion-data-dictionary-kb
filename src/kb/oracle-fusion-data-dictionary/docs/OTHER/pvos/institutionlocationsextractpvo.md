---
id: DOC-OTHER-PVO-InstitutionLocationsExtractPVO
doc_type: system-doc
title: "InstitutionLocationsExtractPVO — PVO Cross-Module"
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
  - InstitutionLocationsExtractPVO
  - institutionlocationsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InstitutionLocationsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Institution Locations Extract. Acessa as tabelas: GMS_INSTITUTION_LOCATIONS.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.InstitutionLocationsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_institution_locations|GMS_INSTITUTION_LOCATIONS]] — 15 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[gms_institution_locations|GMS_INSTITUTION_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InstitutionLocationsPEOAwardLocation | AWARD_LOCATION | — | ✅ |
| 2 | InstitutionLocationsPEOBillingLocation | BILLING_LOCATION | — | ✅ |
| 3 | InstitutionLocationsPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | InstitutionLocationsPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | InstitutionLocationsPEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 6 | InstitutionLocationsPEOInstitutionId | INSTITUTION_ID | — | ✅ |
| 7 | InstitutionLocationsPEOInstnLocationId | INSTN_LOCATION_ID | 🔑 | ✅ |
| 8 | InstitutionLocationsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | InstitutionLocationsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | InstitutionLocationsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | InstitutionLocationsPEOLocationId | LOCATION_ID | — | ✅ |
| 12 | InstitutionLocationsPEOLocationUrl | LOCATION_URL | — | ✅ |
| 13 | InstitutionLocationsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | InstitutionLocationsPEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 15 | InstitutionLocationsPEOStartDateActive | START_DATE_ACTIVE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
