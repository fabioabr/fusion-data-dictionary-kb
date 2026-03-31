---
id: DOC-PO-PVO-SupplierProductsAndServicesExtractPVO
doc_type: system-doc
title: "SupplierProductsAndServicesExtractPVO — PVO Purchasing"
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
  - SupplierProductsAndServicesExtractPVO
  - supplierproductsandservicesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierProductsAndServicesExtractPVO

## 📌 Visão Geral

Extrai os produtos e serviços oferecidos por cada fornecedor para carga BICC, com categorias UNSPSC e descrições. Alimenta análises de capacidade de fornecimento e mapeamento de mercado.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PozBiccExtractAM.SupplierProductsAndServicesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[poz_sup_products_services|POZ_SUP_PRODUCTS_SERVICES]] — 11 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[poz_sup_products_services|POZ_SUP_PRODUCTS_SERVICES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryId | CATEGORY_ID | — | ✅ |
| 2 | ClassificationId | CLASSIFICATION_ID | 🔑 | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | PurchasingCatFlag | PURCHASING_CAT_FLAG | — | ✅ |
| 10 | Status | STATUS | — | ✅ |
| 11 | VendorId | VENDOR_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
