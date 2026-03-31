---
id: DOC-PO-PVO-SupplierBusinessClassificationExtractPVO
doc_type: system-doc
title: "SupplierBusinessClassificationExtractPVO — PVO Purchasing"
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
  - SupplierBusinessClassificationExtractPVO
  - supplierbusinessclassificationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierBusinessClassificationExtractPVO

## 📌 Visão Geral

Extrai as classificações de negócio dos fornecedores (porte, diversidade, certificações) para carga BICC, incluindo agência certificadora. Suporta compliance com políticas de diversidade.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PozBiccExtractAM.SupplierBusinessClassificationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 2 | 1 | 25 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[poz_bus_classifications|POZ_BUS_CLASSIFICATIONS]] — 21 atributos (1 PKs, 21 BICC)
- [[poz_certifying_agencies|POZ_CERTIFYING_AGENCIES]] — 4 atributos (4 BICC)

---

## ⚙️ Atributos

### [[poz_bus_classifications|POZ_BUS_CLASSIFICATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CertificateNumber | CERTIFICATE_NUMBER | — | ✅ |
| 2 | CertifyingAgencyId | CERTIFYING_AGENCY_ID | — | ✅ |
| 3 | ClassStatus | CLASS_STATUS | — | ✅ |
| 4 | ClassificationId | CLASSIFICATION_ID | 🔑 | ✅ |
| 5 | ConfirmedOn | CONFIRMED_ON | — | ✅ |
| 6 | CreatedBy | CREATED_BY | — | ✅ |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | Deleted | DELETED | — | ✅ |
| 9 | ExpirationDate | EXPIRATION_DATE | — | ✅ |
| 10 | ExtAttr1 | EXT_ATTR_1 | — | ✅ |
| 11 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | LookupCode | LOOKUP_CODE | — | ✅ |
| 15 | Notes | NOTES | — | ✅ |
| 16 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | OtherCertifyingAgency | OTHER_CERTIFYING_AGENCY | — | ✅ |
| 18 | PartyId | PARTY_ID | — | ✅ |
| 19 | ProvidedByContactId | PROVIDED_BY_CONTACT_ID | — | ✅ |
| 20 | StartDate | START_DATE | — | ✅ |
| 21 | VendorId | VENDOR_ID | — | ✅ |

### [[poz_certifying_agencies|POZ_CERTIFYING_AGENCIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CertifyingAgencyAgencyId | AGENCY_ID | — | ✅ |
| 2 | CertifyingAgencyDescription | DESCRIPTION | — | ✅ |
| 3 | CertifyingAgencyEndDate | END_DATE | — | ✅ |
| 4 | CertifyingAgencyName | NAME | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
