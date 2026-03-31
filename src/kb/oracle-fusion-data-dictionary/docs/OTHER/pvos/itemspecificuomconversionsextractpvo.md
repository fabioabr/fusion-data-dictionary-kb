---
id: DOC-OTHER-PVO-ItemSpecificUOMConversionsExtractPVO
doc_type: system-doc
title: "ItemSpecificUOMConversionsExtractPVO — PVO Cross-Module"
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
  - ItemSpecificUOMConversionsExtractPVO
  - itemspecificuomconversionsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemSpecificUOMConversionsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Item Specific UOMConversions Extract. Acessa as tabelas: RCS_ITEM_UOM_CONVERSIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.ItemSpecificUOMConversionsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[rcs_item_uom_conversions|RCS_ITEM_UOM_CONVERSIONS]] — 11 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[rcs_item_uom_conversions|RCS_ITEM_UOM_CONVERSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConversionRate | CONVERSION_RATE | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | InventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 5 | ItemUomConvId | ITEM_UOM_CONV_ID | 🔑 | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | PrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 11 | TransactionUomCode | TRANSACTION_UOM_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
