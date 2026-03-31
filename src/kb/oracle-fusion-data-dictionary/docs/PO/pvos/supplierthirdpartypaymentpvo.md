---
id: DOC-PO-PVO-SupplierThirdPartyPaymentPVO
doc_type: system-doc
title: "SupplierThirdPartyPaymentPVO — PVO Purchasing"
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
  - SupplierThirdPartyPaymentPVO
  - supplierthirdpartypaymentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierThirdPartyPaymentPVO

## 📌 Visão Geral

Disponibiliza configurações de pagamento a terceiros para consulta, permitindo validar redirecionamentos de pagamento, sites beneficiários e prevenir erros em liquidações.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.SupplierThirdPartyPaymentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 6 | 1 | 12 | 40% |

---

## 🔗 Tabelas Relacionadas

- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 2 atributos (1 BICC)
- [[hz_parties|HZ_PARTIES]] — 2 atributos (1 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 3 atributos (1 BICC)
- [[poz_suppliers_v|POZ_SUPPLIERS_V]] — 4 atributos (2 BICC)
- [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]] — 5 atributos (1 BICC)
- [[poz_sup_thirdparty_payment_rel|POZ_SUP_THIRDPARTY_PAYMENT_REL]] — 14 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitBusinessUnitId | BU_ID | — | — |
| 2 | BusinessUnitName | BU_NAME | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyId | PARTY_ID | — | — |
| 2 | PartyName | PARTY_NAME | — | ✅ |

### [[hz_party_sites|HZ_PARTY_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocationId | LOCATION_ID | — | — |
| 2 | PartySiteId | PARTY_SITE_ID | — | — |
| 3 | PartySiteName | PARTY_SITE_NAME | — | ✅ |

### [[poz_suppliers_v|POZ_SUPPLIERS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | VendorId | VENDOR_ID | — | — |
| 2 | VendorId2 | VENDOR_ID | — | — |
| 3 | VendorName | VENDOR_NAME | — | ✅ |
| 4 | VendorName1 | VENDOR_NAME | — | ✅ |

### [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 2 | PrcBuId | PRC_BU_ID | — | — |
| 3 | VendorId1 | VENDOR_ID | — | — |
| 4 | VendorSiteCode | VENDOR_SITE_CODE | — | ✅ |
| 5 | VendorSiteId1 | VENDOR_SITE_ID | — | — |

### [[poz_sup_thirdparty_payment_rel|POZ_SUP_THIRDPARTY_PAYMENT_REL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | DefaultRelationshipFlag | DEFAULT_RELATIONSHIP_FLAG | — | ✅ |
| 4 | Description | DESCRIPTION | — | ✅ |
| 5 | FromDate | FROM_DATE | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | RemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 11 | RemitToSupplierId | REMIT_TO_SUPPLIER_ID | — | — |
| 12 | ToDate | TO_DATE | — | ✅ |
| 13 | TppRelationshipId | TPP_RELATIONSHIP_ID | 🔑 | ✅ |
| 14 | VendorSiteId | VENDOR_SITE_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
