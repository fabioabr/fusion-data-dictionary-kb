---
id: DOC-OTHER-PVO-MaterialOnHandPVO
doc_type: system-doc
title: "MaterialOnHandPVO — PVO Cross-Module"
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
  - MaterialOnHandPVO
  - materialonhandpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MaterialOnHandPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Material On Hand. Acessa as tabelas: WIE_MATERIAL_ORG_ON_HAND_QTY_V.

**Caminho:** `FscmTopModelAM.WorkOrderAM.MaterialOnHandPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 3 | 1 | 2 | 3 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wie_material_org_on_hand_qty_v|WIE_MATERIAL_ORG_ON_HAND_QTY_V]] — 3 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[wie_material_org_on_hand_qty_v|WIE_MATERIAL_ORG_ON_HAND_QTY_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MaterialOnHandPEOInventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 2 | MaterialOnHandPEOOnHandQty | ON_HAND_QTY | — | ✅ |
| 3 | MaterialOnHandPEOOrganizationId | ORGANIZATION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
