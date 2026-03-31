---
id: DOC-PO-PVO-SupplierBusinessClassificationPVO
doc_type: system-doc
title: "SupplierBusinessClassificationPVO — PVO Purchasing"
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
  - SupplierBusinessClassificationPVO
  - supplierbusinessclassificationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierBusinessClassificationPVO

## 📌 Visão Geral

Disponibiliza classificações de negócio dos fornecedores para consulta, permitindo segmentação por porte, tipo de empresa, certificações de diversidade e programas de inclusão.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.SupplierBusinessClassificationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 2 | 2 | 19 | 66% |

---

## 🔗 Tabelas Relacionadas

- [[hz_parties|HZ_PARTIES]] — 4 atributos (1 PKs, 4 BICC)
- [[poz_business_classifications_v|POZ_BUSINESS_CLASSIFICATIONS_V]] — 25 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyId | PARTY_ID | 🔑 | ✅ |
| 2 | PartyPEOEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 3 | PersonFirstName | PERSON_FIRST_NAME | — | ✅ |
| 4 | PersonLastName | PERSON_LAST_NAME | — | ✅ |

### [[poz_business_classifications_v|POZ_BUSINESS_CLASSIFICATIONS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClassificationId | CLASSIFICATION_ID | 🔑 | ✅ |
| 2 | SuppBusinessClassificationCertificateNumber | CERTIFICATE_NUMBER | — | ✅ |
| 3 | SuppBusinessClassificationCertifyingAgency | CERTIFYING_AGENCY | — | ✅ |
| 4 | SuppBusinessClassificationCertifyingAgencyId | CERTIFYING_AGENCY_ID | — | — |
| 5 | SuppBusinessClassificationClassificationCode | LOOKUP_CODE | — | ✅ |
| 6 | SuppBusinessClassificationConfirmedOn | CONFIRMED_ON | — | ✅ |
| 7 | SuppBusinessClassificationCreatedBy | CREATED_BY | — | — |
| 8 | SuppBusinessClassificationCreationDate | CREATION_DATE | — | — |
| 9 | SuppBusinessClassificationDisplayedField | DISPLAYED_FIELD | — | ✅ |
| 10 | SuppBusinessClassificationExpirationDate | EXPIRATION_DATE | — | ✅ |
| 11 | SuppBusinessClassificationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | SuppBusinessClassificationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | SuppBusinessClassificationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | SuppBusinessClassificationNotes | NOTES | — | ✅ |
| 15 | SuppBusinessClassificationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | SuppBusinessClassificationOtherCertifyingAgency | OTHER_CERTIFYING_AGENCY | — | ✅ |
| 17 | SuppBusinessClassificationPartyId | PARTY_ID | — | — |
| 18 | SuppBusinessClassificationProvidedByContactId | PROVIDED_BY_CONTACT_ID | — | — |
| 19 | SuppBusinessClassificationSegment1 | SEGMENT1 | — | — |
| 20 | SuppBusinessClassificationStartDate | START_DATE | — | ✅ |
| 21 | SuppBusinessClassificationStatus | STATUS | — | ✅ |
| 22 | SuppBusinessClassificationSubClassificationCode | EXT_ATTR_1 | — | ✅ |
| 23 | SuppBusinessClassificationSubclass | SUBCLASS | — | ✅ |
| 24 | SuppBusinessClassificationSupplierName | SUPPLIER_NAME | — | ✅ |
| 25 | SuppBusinessClassificationVendorId | VENDOR_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
