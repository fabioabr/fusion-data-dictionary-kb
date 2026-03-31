---
id: DOC-OTHER-PVO-UOMInterClassPVO
doc_type: system-doc
title: "UOMInterClassPVO — PVO Cross-Module"
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
  - UOMInterClassPVO
  - uominterclasspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# UOMInterClassPVO

## 📌 Visão Geral

View Object para extração BICC de dados de UOMInter Class. Acessa as tabelas: INV_UOMINTERCLASS_V.

**Caminho:** `FscmTopModelAM.InvUomPublicViewAM.UOMInterClassPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 3 | 7 | 78% |

---

## 🔗 Tabelas Relacionadas

- [[inv_uominterclass_v|INV_UOMINTERCLASS_V]] — 9 atributos (3 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[inv_uominterclass_v|INV_UOMINTERCLASS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConvDisableDate | CONV_DISABLE_DATE | — | ✅ |
| 2 | ConvLastUpdateDate | CONV_LAST_UPDATE_DATE | — | ✅ |
| 3 | FromUomCode | FROM_UOM_CODE | 🔑 | ✅ |
| 4 | FromUomDisableDate | FROM_UOM_DISABLE_DATE | — | — |
| 5 | FromUomLastUpdateDate | FROM_UOM_LAST_UPDATE_DATE | — | ✅ |
| 6 | InventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 7 | ToUomCode | TO_UOM_CODE | 🔑 | ✅ |
| 8 | ToUomDisableDate | TO_UOM_DISABLE_DATE | — | — |
| 9 | ToUomLastUpdateDate | TO_UOM_LAST_UPDATE_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
