---
id: DOC-OTHER-PVO-CstCostedVuOnhandPVO
doc_type: system-doc
title: "CstCostedVuOnhandPVO — PVO Cross-Module"
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
  - CstCostedVuOnhandPVO
  - cstcostedvuonhandpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstCostedVuOnhandPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Costed Vu Onhand. Acessa as tabelas: CST_COSTED_VU_ONHAND_V.

**Caminho:** `FscmTopModelAM.OnhandValuationAM.CstCostedVuOnhandPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 8 | 1 | 5 | 8 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_costed_vu_onhand_v|CST_COSTED_VU_ONHAND_V]] — 8 atributos (5 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[cst_costed_vu_onhand_v|CST_COSTED_VU_ONHAND_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostedVuOnhandPEOCostBookId | COST_BOOK_ID | 🔑 | ✅ |
| 2 | CostedVuOnhandPEOCostOrgId | COST_ORG_ID | 🔑 | ✅ |
| 3 | CostedVuOnhandPEOEffToDate | EFF_TO_DATE | — | ✅ |
| 4 | CostedVuOnhandPEOInventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 5 | CostedVuOnhandPEOQuantity | QUANTITY | — | ✅ |
| 6 | CostedVuOnhandPEOSnapshotDate | SNAPSHOT_DATE | 🔑 | ✅ |
| 7 | CostedVuOnhandPEOUomCode | UOM_CODE | — | ✅ |
| 8 | CostedVuOnhandPEOValUnitId | VAL_UNIT_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
