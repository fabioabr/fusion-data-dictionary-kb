---
id: DOC-PO-PVO-SupplierFactLessFactPVO
doc_type: system-doc
title: "SupplierFactLessFactPVO — PVO Purchasing"
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
  - SupplierFactLessFactPVO
  - supplierfactlessfactpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierFactLessFactPVO

## 📌 Visão Geral

Extrai métricas agregadas de fornecedores sem dimensões transacionais diretas (factless fact), combinando sites e contatos. Suporta dashboards executivos e contagens de fornecedores ativos.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.SupplierFactLessFactPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 7 | 1 | 6 | 7 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[poz_supp_sites_contacts_v|POZ_SUPP_SITES_CONTACTS_V]] — 7 atributos (6 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[poz_supp_sites_contacts_v|POZ_SUPP_SITES_CONTACTS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CarrierId | CARRIER_ID | — | ✅ |
| 2 | PartySiteId | PARTY_SITE_ID | 🔑 | ✅ |
| 3 | PersonPartyId | PERSON_PARTY_ID | 🔑 | ✅ |
| 4 | PrcBuId | PRC_BU_ID | 🔑 | ✅ |
| 5 | SuppPartyId | SUPP_PARTY_ID | 🔑 | ✅ |
| 6 | VendorId | VENDOR_ID | 🔑 | ✅ |
| 7 | VendorSiteId | VENDOR_SITE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
