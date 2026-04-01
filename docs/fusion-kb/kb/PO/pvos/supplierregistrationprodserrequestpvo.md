---
id: DOC-PO-PVO-SupplierRegistrationProdSerRequestPVO
doc_type: system-doc
title: "SupplierRegistrationProdSerRequestPVO — PVO Purchasing"
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
  - SupplierRegistrationProdSerRequestPVO
  - supplierregistrationprodserrequestpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierRegistrationProdSerRequestPVO

## 📌 Visão Geral

Extrai os produtos e serviços declarados durante o registro de fornecedores, com categorias e atributos. Permite avaliação da capacidade de fornecimento antes da homologação formal.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.SupplierRegistrationProdSerRequestPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 2 | 2 | 5 | 29% |

---

## 🔗 Tabelas Relacionadas

- [[poz_product_service_requests|POZ_PRODUCT_SERVICE_REQUESTS]] — 12 atributos (1 PKs, 3 BICC)
- [[poz_supp_prod_services_attr_v|POZ_SUPP_PROD_SERVICES_ATTR_V]] — 5 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[poz_product_service_requests|POZ_PRODUCT_SERVICE_REQUESTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PsRequestId | PS_REQUEST_ID | 🔑 | ✅ |
| 2 | SupplierRegProdSerReqCategoryId | CATEGORY_ID | — | — |
| 3 | SupplierRegProdSerReqCreatedBy | CREATED_BY | — | — |
| 4 | SupplierRegProdSerReqCreationDate | CREATION_DATE | — | — |
| 5 | SupplierRegProdSerReqLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | SupplierRegProdSerReqLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | SupplierRegProdSerReqLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | SupplierRegProdSerReqMappingId | MAPPING_ID | — | — |
| 9 | SupplierRegProdSerReqObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | SupplierRegProdSerReqPurchasingCatFlag | PURCHASING_CAT_FLAG | — | — |
| 11 | SupplierRegProdSerReqRequestStatus | REQUEST_STATUS | — | ✅ |
| 12 | SupplierRegProdSerReqRequestType | REQUEST_TYPE | — | — |

### [[poz_supp_prod_services_attr_v|POZ_SUPP_PROD_SERVICES_ATTR_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupplierProdAndServAttrAncestorCategoryDescription | ANCESTOR_CATEGORY_DESCRIPTION | — | ✅ |
| 2 | SupplierProdAndServAttrAncestorCategoryId | ANCESTOR_CATEGORY_ID | — | — |
| 3 | SupplierProdAndServAttrAncestorCategoryName | ANCESTOR_CATEGORY_NAME | 🔑 | ✅ |
| 4 | SupplierProdAndServAttrCalculatedPath | CALCULATED_PATH | — | — |
| 5 | SupplierProdAndServAttrCategoryId | CATEGORY_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
