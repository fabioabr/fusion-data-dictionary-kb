---
id: DOC-PO-PVO-SupplierAccessibleSitePVO
doc_type: system-doc
title: "SupplierAccessibleSitePVO — PVO Purchasing"
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
  - SupplierAccessibleSitePVO
  - supplieraccessiblesitepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierAccessibleSitePVO

## 📌 Visão Geral

Extrai os sites de fornecedores acessíveis ao usuário corrente, aplicando filtros de segurança por unidade de negócio. Garante que apenas sites autorizados sejam visíveis e utilizáveis nas transações.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.SupplierAccessibleSitePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 1 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[poz_supp_access_sites_v|POZ_SUPP_ACCESS_SITES_V]] — 10 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[poz_supp_access_sites_v|POZ_SUPP_ACCESS_SITES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccessibleSitePartySiteName | PARTY_SITE_NAME | — | ✅ |
| 2 | AccessibleSitePrcBuId | PRC_BU_ID | — | ✅ |
| 3 | AccessibleSiteSegment1 | SEGMENT1 | — | ✅ |
| 4 | AccessibleSiteSiteInactiveDate | INACTIVE_DATE | — | ✅ |
| 5 | AccessibleSiteSupplierEnabledFlag | ENABLED_FLAG | — | ✅ |
| 6 | AccessibleSiteSupplierEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 7 | AccessibleSiteSupplierName | SUPPLIER_NAME | — | ✅ |
| 8 | AccessibleSiteVendorId | VENDOR_ID | — | ✅ |
| 9 | AccessibleSiteVendorSiteCode | VENDOR_SITE_CODE | — | ✅ |
| 10 | VendorSiteId | VENDOR_SITE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
