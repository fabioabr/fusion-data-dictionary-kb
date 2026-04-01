---
id: DOC-OTHER-PVO-ItemSecurityInstanceGrant
doc_type: system-doc
title: "ItemSecurityInstanceGrant — PVO Cross-Module"
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
  - ItemSecurityInstanceGrant
  - itemsecurityinstancegrant
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemSecurityInstanceGrant

## 📌 Visão Geral

View Object para extração BICC de dados de Item Security Instance Grant. Acessa as tabelas: EGP_SYSTEM_ITEMS_B_V, INV_ORG_PARAMETERS.

**Caminho:** `FscmTopModelAM.EgpItemsPublicModelAM.ItemSecurityInstanceGrant`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 3 | 2 | 2 | 2 | 67% |

---

## 🔗 Tabelas Relacionadas

- [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]] — 2 atributos (2 PKs, 2 BICC)
- [[inv_org_parameters|INV_ORG_PARAMETERS]] — 1 atributos

---

## ⚙️ Atributos

### [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 2 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |

### [[inv_org_parameters|INV_ORG_PARAMETERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemOrganizationParameterPEOOrganizationId | ORGANIZATION_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
