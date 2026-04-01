---
id: DOC-OTHER-PVO-UOMIntraClassPVO
doc_type: system-doc
title: "UOMIntraClassPVO — PVO Cross-Module"
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
  - UOMIntraClassPVO
  - uomintraclasspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# UOMIntraClassPVO

## 📌 Visão Geral

View Object para extração BICC de dados de UOMIntra Class. Acessa as tabelas: INV_UOMINTRACLASS_V.

**Caminho:** `FscmTopModelAM.InvUomPublicViewAM.UOMIntraClassPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 7 | 1 | 3 | 6 | 86% |

---

## 🔗 Tabelas Relacionadas

- [[inv_uomintraclass_v|INV_UOMINTRACLASS_V]] — 7 atributos (3 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[inv_uomintraclass_v|INV_UOMINTRACLASS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConvDisableDate | CONV_DISABLE_DATE | — | ✅ |
| 2 | ConvLastUpdateDate | CONV_LAST_UPDATE_DATE | — | ✅ |
| 3 | FromUomCode | FROM_UOM_CODE | 🔑 | ✅ |
| 4 | InventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 5 | ToUomCode | TO_UOM_CODE | 🔑 | ✅ |
| 6 | ToUomDisableDate | TO_UOM_DISABLE_DATE | — | — |
| 7 | ToUomLastUpdateDate | TO_UOM_LAST_UPDATE_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
