---
id: DOC-OTHER-PVO-CustomerAssetBuiltStructurePVO
doc_type: system-doc
title: "CustomerAssetBuiltStructurePVO — PVO Cross-Module"
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
  - CustomerAssetBuiltStructurePVO
  - customerassetbuiltstructurepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CustomerAssetBuiltStructurePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Customer Asset Built Structure. Acessa as tabelas: CSE_AS_BUILT_STRUCTURES_V.

**Caminho:** `FscmTopModelAM.CustomerAssetAM.CustomerAssetBuiltStructurePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 38 | 1 | 3 | 6 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[cse_as_built_structures_v|CSE_AS_BUILT_STRUCTURES_V]] — 38 atributos (3 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[cse_as_built_structures_v|CSE_AS_BUILT_STRUCTURES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | ActiveStartDate | ACTIVE_START_DATE | — | — |
| 3 | ChildAssetId | CHILD_ASSET_ID | 🔑 | ✅ |
| 4 | ChildAssetItemId | CHILD_ASSET_ITEM_ID | — | — |
| 5 | ChildAssetItemOrgId | CHILD_ASSET_ITEM_ORG_ID | — | — |
| 6 | ChildAssetLotNumber | CHILD_ASSET_LOT_NUMBER | — | — |
| 7 | ChildAssetNumber | CHILD_ASSET_NUMBER | — | — |
| 8 | ChildAssetSerialNumber | CHILD_ASSET_SERIAL_NUMBER | — | — |
| 9 | ChildAssetSoId | CHILD_ASSET_SO_ID | — | — |
| 10 | ChildAssetSoLineId | CHILD_ASSET_SO_LINE_ID | — | — |
| 11 | ChildAssetSoLineNumber | CHILD_ASSET_SO_LINE_NUMBER | — | — |
| 12 | ChildAssetSoNumber | CHILD_ASSET_SO_NUMBER | — | — |
| 13 | ChildLevel | CHILD_LEVEL | — | ✅ |
| 14 | ChildLpadChars | CHILD_LPAD_CHARS | — | — |
| 15 | LeafNode | LEAF_NODE | — | — |
| 16 | ParentAssetId | PARENT_ASSET_ID | 🔑 | ✅ |
| 17 | ParentAssetItemId | PARENT_ASSET_ITEM_ID | — | — |
| 18 | ParentAssetItemOrgId | PARENT_ASSET_ITEM_ORG_ID | — | — |
| 19 | ParentAssetLogicalFlag | PARENT_ASSET_LOGICAL_FLAG | — | — |
| 20 | ParentAssetLotNumber | PARENT_ASSET_LOT_NUMBER | — | — |
| 21 | ParentAssetNumber | PARENT_ASSET_NUMBER | — | — |
| 22 | ParentAssetSerialNumber | PARENT_ASSET_SERIAL_NUMBER | — | — |
| 23 | ParentAssetSoId | PARENT_ASSET_SO_ID | — | — |
| 24 | ParentAssetSoLineId | PARENT_ASSET_SO_LINE_ID | — | — |
| 25 | ParentAssetSoLineNumber | PARENT_ASSET_SO_LINE_NUMBER | — | — |
| 26 | ParentAssetSoNumber | PARENT_ASSET_SO_NUMBER | — | — |
| 27 | RelationshipTypeCode | RELATIONSHIP_TYPE_CODE | — | ✅ |
| 28 | RootAssetId | ROOT_ASSET_ID | 🔑 | ✅ |
| 29 | RootAssetItemId | ROOT_ASSET_ITEM_ID | — | — |
| 30 | RootAssetItemOrgId | ROOT_ASSET_ITEM_ORG_ID | — | — |
| 31 | RootAssetLogicalFlag | ROOT_ASSET_LOGICAL_FLAG | — | — |
| 32 | RootAssetLotNumber | ROOT_ASSET_LOT_NUMBER | — | — |
| 33 | RootAssetNumber | ROOT_ASSET_NUMBER | — | — |
| 34 | RootAssetSerialNumber | ROOT_ASSET_SERIAL_NUMBER | — | — |
| 35 | RootAssetSoId | ROOT_ASSET_SO_ID | — | — |
| 36 | RootAssetSoLineId | ROOT_ASSET_SO_LINE_ID | — | — |
| 37 | RootAssetSoLineNumber | ROOT_ASSET_SO_LINE_NUMBER | — | — |
| 38 | RootAssetSoNumber | ROOT_ASSET_SO_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
