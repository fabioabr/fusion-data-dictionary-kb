---
id: DOC-OTHER-PVO-GenealogyWhereUsedExtractPVO
doc_type: system-doc
title: "GenealogyWhereUsedExtractPVO — PVO Cross-Module"
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
  - GenealogyWhereUsedExtractPVO
  - genealogywhereusedextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GenealogyWhereUsedExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Genealogy Where Used Extract. Acessa as tabelas: CSE_GENEALOGY_WHERE_USED.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.GenealogyWhereUsedExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 34 | 1 | 3 | 34 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_genealogy_where_used|CSE_GENEALOGY_WHERE_USED]] — 34 atributos (3 PKs, 34 BICC)

---

## ⚙️ Atributos

### [[cse_genealogy_where_used|CSE_GENEALOGY_WHERE_USED]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChildGenObjectId | CHILD_GEN_OBJECT_ID | 🔑 | ✅ |
| 2 | ChildItemId | CHILD_ITEM_ID | — | ✅ |
| 3 | ChildLotNumber | CHILD_LOT_NUMBER | — | ✅ |
| 4 | ChildOrganizationId | CHILD_ORGANIZATION_ID | — | ✅ |
| 5 | ChildOrigDate | CHILD_ORIG_DATE | — | ✅ |
| 6 | ChildOrigDocNumber | CHILD_ORIG_DOC_NUMBER | — | ✅ |
| 7 | ChildOrigDocType | CHILD_ORIG_DOC_TYPE | — | ✅ |
| 8 | ChildOrigQuantity | CHILD_ORIG_QUANTITY | — | ✅ |
| 9 | ChildSerialNumber | CHILD_SERIAL_NUMBER | — | ✅ |
| 10 | CreatedBy | CREATED_BY | — | ✅ |
| 11 | CreationDate | CREATION_DATE | — | ✅ |
| 12 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | LeafChildGenObjectId | LEAF_CHILD_GEN_OBJECT_ID | — | ✅ |
| 16 | LeafChildItemId | LEAF_CHILD_ITEM_ID | — | ✅ |
| 17 | LeafChildLotNumber | LEAF_CHILD_LOT_NUMBER | — | ✅ |
| 18 | LeafChildOrganizationId | LEAF_CHILD_ORGANIZATION_ID | — | ✅ |
| 19 | LeafChildOrigDate | LEAF_CHILD_ORIG_DATE | — | ✅ |
| 20 | LeafChildOrigDocNumber | LEAF_CHILD_ORIG_DOC_NUMBER | — | ✅ |
| 21 | LeafChildOrigDocType | LEAF_CHILD_ORIG_DOC_TYPE | — | ✅ |
| 22 | LeafChildOrigQuantity | LEAF_CHILD_ORIG_QUANTITY | — | ✅ |
| 23 | LeafChildSerialNumber | LEAF_CHILD_SERIAL_NUMBER | — | ✅ |
| 24 | ParentGenObjectId | PARENT_GEN_OBJECT_ID | 🔑 | ✅ |
| 25 | ParentItemId | PARENT_ITEM_ID | — | ✅ |
| 26 | ParentLevel | PARENT_LEVEL | — | ✅ |
| 27 | ParentLotNumber | PARENT_LOT_NUMBER | — | ✅ |
| 28 | ParentOrganizationId | PARENT_ORGANIZATION_ID | — | ✅ |
| 29 | ParentOrigDate | PARENT_ORIG_DATE | — | ✅ |
| 30 | ParentOrigDocNumber | PARENT_ORIG_DOC_NUMBER | — | ✅ |
| 31 | ParentOrigDocType | PARENT_ORIG_DOC_TYPE | — | ✅ |
| 32 | ParentOrigQuantity | PARENT_ORIG_QUANTITY | — | ✅ |
| 33 | ParentSerialNumber | PARENT_SERIAL_NUMBER | — | ✅ |
| 34 | RelationshipTypeCode | RELATIONSHIP_TYPE_CODE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
