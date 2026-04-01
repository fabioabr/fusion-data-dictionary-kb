---
id: DOC-OTHER-PVO-GenealogyCompositionPVO
doc_type: system-doc
title: "GenealogyCompositionPVO — PVO Cross-Module"
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
  - GenealogyCompositionPVO
  - genealogycompositionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GenealogyCompositionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Genealogy Composition. Acessa as tabelas: CSE_GENEALOGY_COMPOSITION_V.

**Caminho:** `FscmTopModelAM.ProductGenealogyAM.GenealogyCompositionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 1 | 3 | 14 | 48% |

---

## 🔗 Tabelas Relacionadas

- [[cse_genealogy_composition_v|CSE_GENEALOGY_COMPOSITION_V]] — 29 atributos (3 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[cse_genealogy_composition_v|CSE_GENEALOGY_COMPOSITION_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChildGenObjectId | CHILD_GEN_OBJECT_ID | 🔑 | ✅ |
| 2 | ChildItemId | CHILD_ITEM_ID | — | — |
| 3 | ChildLevel | CHILD_LEVEL | — | ✅ |
| 4 | ChildLotNumber | CHILD_LOT_NUMBER | — | — |
| 5 | ChildOrganizationId | CHILD_ORGANIZATION_ID | — | — |
| 6 | ChildOrigDate | CHILD_ORIG_DATE | — | — |
| 7 | ChildOrigDocNumber | CHILD_ORIG_DOC_NUMBER | — | ✅ |
| 8 | ChildOrigDocType | CHILD_ORIG_DOC_TYPE | — | ✅ |
| 9 | ChildOrigQuantity | CHILD_ORIG_QUANTITY | — | ✅ |
| 10 | ChildSerialNumber | CHILD_SERIAL_NUMBER | — | — |
| 11 | ParentGenObjectId | PARENT_GEN_OBJECT_ID | 🔑 | ✅ |
| 12 | ParentItemId | PARENT_ITEM_ID | — | — |
| 13 | ParentLotNumber | PARENT_LOT_NUMBER | — | — |
| 14 | ParentOrganizationId | PARENT_ORGANIZATION_ID | — | — |
| 15 | ParentOrigDate | PARENT_ORIG_DATE | — | — |
| 16 | ParentOrigDocNumber | PARENT_ORIG_DOC_NUMBER | — | ✅ |
| 17 | ParentOrigDocType | PARENT_ORIG_DOC_TYPE | — | ✅ |
| 18 | ParentOrigQuantity | PARENT_ORIG_QUANTITY | — | ✅ |
| 19 | ParentSerialNumber | PARENT_SERIAL_NUMBER | — | — |
| 20 | RelationshipTypeCode | RELATIONSHIP_TYPE_CODE | 🔑 | ✅ |
| 21 | RootGenObjectId | ROOT_GEN_OBJECT_ID | — | ✅ |
| 22 | RootItemId | ROOT_ITEM_ID | — | — |
| 23 | RootLotNumber | ROOT_LOT_NUMBER | — | — |
| 24 | RootOrganizationId | ROOT_ORGANIZATION_ID | — | — |
| 25 | RootOrigDate | ROOT_ORIG_DATE | — | — |
| 26 | RootOrigDocNumber | ROOT_ORIG_DOC_NUMBER | — | ✅ |
| 27 | RootOrigDocType | ROOT_ORIG_DOC_TYPE | — | ✅ |
| 28 | RootOrigQuantity | ROOT_ORIG_QUANTITY | — | ✅ |
| 29 | RootSerialNumber | ROOT_SERIAL_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
