---
id: DOC-OTHER-PVO-GenealogyWhereUsedPVO
doc_type: system-doc
title: "GenealogyWhereUsedPVO — PVO Cross-Module"
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
  - GenealogyWhereUsedPVO
  - genealogywhereusedpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GenealogyWhereUsedPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Genealogy Where Used. Acessa as tabelas: CSE_GENEALOGY_WHERE_USED_V.

**Caminho:** `FscmTopModelAM.ProductGenealogyAM.GenealogyWhereUsedPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 1 | 3 | 14 | 48% |

---

## 🔗 Tabelas Relacionadas

- [[cse_genealogy_where_used_v|CSE_GENEALOGY_WHERE_USED_V]] — 29 atributos (3 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[cse_genealogy_where_used_v|CSE_GENEALOGY_WHERE_USED_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChildGenObjectId | CHILD_GEN_OBJECT_ID | 🔑 | ✅ |
| 2 | ChildItemId | CHILD_ITEM_ID | — | — |
| 3 | ChildLotNumber | CHILD_LOT_NUMBER | — | — |
| 4 | ChildOrganizationId | CHILD_ORGANIZATION_ID | — | — |
| 5 | ChildOrigDate | CHILD_ORIG_DATE | — | — |
| 6 | ChildOrigDocNumber | CHILD_ORIG_DOC_NUMBER | — | ✅ |
| 7 | ChildOrigDocType | CHILD_ORIG_DOC_TYPE | — | ✅ |
| 8 | ChildOrigQuantity | CHILD_ORIG_QUANTITY | — | ✅ |
| 9 | ChildSerialNumber | CHILD_SERIAL_NUMBER | — | — |
| 10 | LeafChildGenObjectId | LEAF_CHILD_GEN_OBJECT_ID | — | ✅ |
| 11 | LeafChildItemId | LEAF_CHILD_ITEM_ID | — | — |
| 12 | LeafChildLotNumber | LEAF_CHILD_LOT_NUMBER | — | — |
| 13 | LeafChildOrganizationId | LEAF_CHILD_ORGANIZATION_ID | — | — |
| 14 | LeafChildOrigDate | LEAF_CHILD_ORIG_DATE | — | — |
| 15 | LeafChildOrigDocNumber | LEAF_CHILD_ORIG_DOC_NUMBER | — | ✅ |
| 16 | LeafChildOrigDocType | LEAF_CHILD_ORIG_DOC_TYPE | — | ✅ |
| 17 | LeafChildOrigQuantity | LEAF_CHILD_ORIG_QUANTITY | — | ✅ |
| 18 | LeafChildSerialNumber | LEAF_CHILD_SERIAL_NUMBER | — | — |
| 19 | ParentGenObjectId | PARENT_GEN_OBJECT_ID | 🔑 | ✅ |
| 20 | ParentItemId | PARENT_ITEM_ID | — | — |
| 21 | ParentLevel | PARENT_LEVEL | — | ✅ |
| 22 | ParentLotNumber | PARENT_LOT_NUMBER | — | — |
| 23 | ParentOrganizationId | PARENT_ORGANIZATION_ID | — | — |
| 24 | ParentOrigDate | PARENT_ORIG_DATE | — | — |
| 25 | ParentOrigDocNumber | PARENT_ORIG_DOC_NUMBER | — | ✅ |
| 26 | ParentOrigDocType | PARENT_ORIG_DOC_TYPE | — | ✅ |
| 27 | ParentOrigQuantity | PARENT_ORIG_QUANTITY | — | ✅ |
| 28 | ParentSerialNumber | PARENT_SERIAL_NUMBER | — | — |
| 29 | RelationshipTypeCode | RELATIONSHIP_TYPE_CODE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
