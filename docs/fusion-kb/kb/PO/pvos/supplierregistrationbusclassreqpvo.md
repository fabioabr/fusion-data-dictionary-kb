---
id: DOC-PO-PVO-SupplierRegistrationBusClassReqPVO
doc_type: system-doc
title: "SupplierRegistrationBusClassReqPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - SupplierRegistrationBusClassReqPVO
  - supplierregistrationbusclassreqpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierRegistrationBusClassReqPVO

## 📌 Visão Geral

Extrai as classificações de negócio declaradas no registro de fornecedores (porte, diversidade), com agência certificadora. Suporta avaliação de elegibilidade no processo de onboarding.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.SupplierRegistrationBusClassReqPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 2 | 1 | 10 | 34% |

---

## 🔗 Tabelas Relacionadas

- [[poz_bus_class_reqs|POZ_BUS_CLASS_REQS]] — 27 atributos (1 PKs, 9 BICC)
- [[poz_certifying_agencies|POZ_CERTIFYING_AGENCIES]] — 2 atributos (1 BICC)

---

## ⚙️ Atributos

### [[poz_bus_class_reqs|POZ_BUS_CLASS_REQS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusClassRequestId | BUS_CLASS_REQUEST_ID | 🔑 | ✅ |
| 2 | SupplierRegBusClassReqCertificationAgency | CERTIFICATION_AGENCY | — | — |
| 3 | SupplierRegBusClassReqCertificationNo | CERTIFICATION_NO | — | ✅ |
| 4 | SupplierRegBusClassReqCertifyingAgencyId | CERTIFYING_AGENCY_ID | — | — |
| 5 | SupplierRegBusClassReqClassificationId | CLASSIFICATION_ID | — | — |
| 6 | SupplierRegBusClassReqClassificationIdOriginal | CLASSIFICATION_ID_ORIGINAL | — | — |
| 7 | SupplierRegBusClassReqConfirmedOn | CONFIRMED_ON | — | — |
| 8 | SupplierRegBusClassReqCreatedBy | CREATED_BY | — | — |
| 9 | SupplierRegBusClassReqCreationDate | CREATION_DATE | — | — |
| 10 | SupplierRegBusClassReqDupOfBcReqId | DUP_OF_BC_REQ_ID | — | — |
| 11 | SupplierRegBusClassReqExpirationDate | EXPIRATION_DATE | — | ✅ |
| 12 | SupplierRegBusClassReqExtAttr1 | EXT_ATTR_1 | — | ✅ |
| 13 | SupplierRegBusClassReqLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | SupplierRegBusClassReqLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | SupplierRegBusClassReqLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | SupplierRegBusClassReqLookupCode | LOOKUP_CODE | — | ✅ |
| 17 | SupplierRegBusClassReqMappingId | MAPPING_ID | — | — |
| 18 | SupplierRegBusClassReqNotes | NOTES | — | ✅ |
| 19 | SupplierRegBusClassReqObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | SupplierRegBusClassReqOtherCertifyingAgency | OTHER_CERTIFYING_AGENCY | — | ✅ |
| 21 | SupplierRegBusClassReqProcessStatus | PROCESS_STATUS | — | — |
| 22 | SupplierRegBusClassReqProvidedByContactId | PROVIDED_BY_CONTACT_ID | — | — |
| 23 | SupplierRegBusClassReqRequestStatus | REQUEST_STATUS | — | — |
| 24 | SupplierRegBusClassReqRequestType | REQUEST_TYPE | — | — |
| 25 | SupplierRegBusClassReqRowStatus | ROW_STATUS | — | — |
| 26 | SupplierRegBusClassReqStartDate | START_DATE | — | ✅ |
| 27 | SupplierRegBusClassReqStatus | STATUS | — | — |

### [[poz_certifying_agencies|POZ_CERTIFYING_AGENCIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupplierCertifyingAgenciesAgencyId | AGENCY_ID | — | — |
| 2 | SupplierCertifyingAgenciesName | NAME | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
