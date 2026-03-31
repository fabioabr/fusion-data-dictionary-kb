---
id: DOC-OTHER-PVO-InstitutionLocationsPVO
doc_type: system-doc
title: "InstitutionLocationsPVO — PVO Cross-Module"
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
  - InstitutionLocationsPVO
  - institutionlocationspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InstitutionLocationsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Institution Locations. Acessa as tabelas: GMS_INSTITUTION_LOCATIONS, HR_LOCATIONS_ALL_F_VL.

**Caminho:** `FscmTopModelAM.GmsSetupAM.InstitutionLocationsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 31 | 2 | 1 | 20 | 65% |

---

## 🔗 Tabelas Relacionadas

- [[gms_institution_locations|GMS_INSTITUTION_LOCATIONS]] — 15 atributos (1 PKs, 8 BICC)
- [[hr_locations_all_f_vl|HR_LOCATIONS_ALL_F_VL]] — 16 atributos (12 BICC)

---

## ⚙️ Atributos

### [[gms_institution_locations|GMS_INSTITUTION_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InstitutionLocationsPEOAwardLocation | AWARD_LOCATION | — | ✅ |
| 2 | InstitutionLocationsPEOBillingLocation | BILLING_LOCATION | — | ✅ |
| 3 | InstitutionLocationsPEOCreatedBy | CREATED_BY | — | — |
| 4 | InstitutionLocationsPEOCreationDate | CREATION_DATE | — | — |
| 5 | InstitutionLocationsPEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 6 | InstitutionLocationsPEOInstitutionId | INSTITUTION_ID | — | — |
| 7 | InstitutionLocationsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | InstitutionLocationsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | InstitutionLocationsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | InstitutionLocationsPEOLocationId | LOCATION_ID | — | — |
| 11 | InstitutionLocationsPEOLocationUrl | LOCATION_URL | — | ✅ |
| 12 | InstitutionLocationsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | InstitutionLocationsPEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 14 | InstitutionLocationsPEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 15 | InstnLocationId | INSTN_LOCATION_ID | 🔑 | ✅ |

### [[hr_locations_all_f_vl|HR_LOCATIONS_ALL_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocationDPEOAddressLine1 | ADDRESS_LINE_1 | — | ✅ |
| 2 | LocationDPEOAddressLine2 | ADDRESS_LINE_2 | — | ✅ |
| 3 | LocationDPEOAddressLine3 | ADDRESS_LINE_3 | — | ✅ |
| 4 | LocationDPEOAddressLine4 | ADDRESS_LINE_4 | — | ✅ |
| 5 | LocationDPEOBuilding | BUILDING | — | — |
| 6 | LocationDPEOCountry | COUNTRY | — | ✅ |
| 7 | LocationDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | LocationDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 9 | LocationDPEOEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 10 | LocationDPEOFloorNumber | FLOOR_NUMBER | — | — |
| 11 | LocationDPEOLocationId | LOCATION_ID | — | — |
| 12 | LocationDPEOLocationName | LOCATION_NAME | — | ✅ |
| 13 | LocationDPEOPostalCode | POSTAL_CODE | — | ✅ |
| 14 | LocationDPEOTelephoneNumber1 | TELEPHONE_NUMBER_1 | — | ✅ |
| 15 | LocationDPEOTelephoneNumber2 | TELEPHONE_NUMBER_2 | — | ✅ |
| 16 | LocationDPEOTownOrCity | TOWN_OR_CITY | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
