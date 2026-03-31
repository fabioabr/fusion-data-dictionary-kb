---
id: DOC-HCM-PVO-DriversLicensesPVO
doc_type: system-doc
title: "DriversLicensesPVO — PVO Human Capital Management"
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
  - DriversLicensesPVO
  - driverslicensespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DriversLicensesPVO

## 📌 Visão Geral

Extrai dados de carteiras de habilitação dos colaboradores, incluindo tipo, validade e categoria. Utilizado em compliance e requisitos de cargo.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.DriversLicensesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 31 | 2 | 1 | 20 | 65% |

---

## 🔗 Tabelas Relacionadas

- [[per_drivers_licenses|PER_DRIVERS_LICENSES]] — 21 atributos (1 PKs, 18 BICC)
- [[per_drivers_license_types|PER_DRIVERS_LICENSE_TYPES]] — 10 atributos (2 BICC)

---

## ⚙️ Atributos

### [[per_drivers_licenses|PER_DRIVERS_LICENSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DriversLicenseId | DRIVERS_LICENSE_ID | 🔑 | ✅ |
| 2 | DriversLicensesPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | DriversLicensesPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | DriversLicensesPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | DriversLicensesPEODateFrom | DATE_FROM | — | ✅ |
| 6 | DriversLicensesPEODateTo | DATE_TO | — | ✅ |
| 7 | DriversLicensesPEOIssuingAuthority | ISSUING_AUTHORITY | — | ✅ |
| 8 | DriversLicensesPEOIssuingCountry | ISSUING_COUNTRY | — | ✅ |
| 9 | DriversLicensesPEOIssuingLocation | ISSUING_LOCATION | — | ✅ |
| 10 | DriversLicensesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | DriversLicensesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | DriversLicensesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | DriversLicensesPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 14 | DriversLicensesPEOLicenseNumber | LICENSE_NUMBER | — | ✅ |
| 15 | DriversLicensesPEOLicenseSuspended | LICENSE_SUSPENDED | — | ✅ |
| 16 | DriversLicensesPEONumberOfPoints | NUMBER_OF_POINTS | — | ✅ |
| 17 | DriversLicensesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | DriversLicensesPEOPersonId | PERSON_ID | — | ✅ |
| 19 | DriversLicensesPEOSuspendedFromDate | SUSPENDED_FROM_DATE | — | ✅ |
| 20 | DriversLicensesPEOSuspendedToDate | SUSPENDED_TO_DATE | — | ✅ |
| 21 | DriversLicensesPEOViolations | VIOLATIONS | — | ✅ |

### [[per_drivers_license_types|PER_DRIVERS_LICENSE_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DriversLicenseTypesPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | DriversLicenseTypesPEOCreatedBy | CREATED_BY | — | — |
| 3 | DriversLicenseTypesPEOCreationDate | CREATION_DATE | — | — |
| 4 | DriversLicenseTypesPEODriversLicenseId | DRIVERS_LICENSE_ID | — | — |
| 5 | DriversLicenseTypesPEODriversLicenseTypeId | DRIVERS_LICENSE_TYPE_ID | — | — |
| 6 | DriversLicenseTypesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | DriversLicenseTypesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | DriversLicenseTypesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | DriversLicenseTypesPEOLicenseType | LICENSE_TYPE | — | ✅ |
| 10 | DriversLicenseTypesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
