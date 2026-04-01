---
id: DOC-OTHER-PVO-GenealogyCompositionExtractPVO
doc_type: system-doc
title: "GenealogyCompositionExtractPVO — PVO Cross-Module"
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
  - GenealogyCompositionExtractPVO
  - genealogycompositionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GenealogyCompositionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Genealogy Composition Extract. Acessa as tabelas: CSE_GENEALOGY_COMPOSITION.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.GenealogyCompositionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 34 | 1 | 3 | 34 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_genealogy_composition|CSE_GENEALOGY_COMPOSITION]] — 34 atributos (3 PKs, 34 BICC)

---

## ⚙️ Atributos

### [[cse_genealogy_composition|CSE_GENEALOGY_COMPOSITION]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChildGenObjectId | CHILD_GEN_OBJECT_ID | 🔑 | ✅ |
| 2 | ChildItemId | CHILD_ITEM_ID | — | ✅ |
| 3 | ChildLevel | CHILD_LEVEL | — | ✅ |
| 4 | ChildLotNumber | CHILD_LOT_NUMBER | — | ✅ |
| 5 | ChildOrganizationId | CHILD_ORGANIZATION_ID | — | ✅ |
| 6 | ChildOrigDate | CHILD_ORIG_DATE | — | ✅ |
| 7 | ChildOrigDocNumber | CHILD_ORIG_DOC_NUMBER | — | ✅ |
| 8 | ChildOrigDocType | CHILD_ORIG_DOC_TYPE | — | ✅ |
| 9 | ChildOrigQuantity | CHILD_ORIG_QUANTITY | — | ✅ |
| 10 | ChildSerialNumber | CHILD_SERIAL_NUMBER | — | ✅ |
| 11 | CreatedBy | CREATED_BY | — | ✅ |
| 12 | CreationDate | CREATION_DATE | — | ✅ |
| 13 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | ParentGenObjectId | PARENT_GEN_OBJECT_ID | 🔑 | ✅ |
| 17 | ParentItemId | PARENT_ITEM_ID | — | ✅ |
| 18 | ParentLotNumber | PARENT_LOT_NUMBER | — | ✅ |
| 19 | ParentOrganizationId | PARENT_ORGANIZATION_ID | — | ✅ |
| 20 | ParentOrigDate | PARENT_ORIG_DATE | — | ✅ |
| 21 | ParentOrigDocNumber | PARENT_ORIG_DOC_NUMBER | — | ✅ |
| 22 | ParentOrigDocType | PARENT_ORIG_DOC_TYPE | — | ✅ |
| 23 | ParentOrigQuantity | PARENT_ORIG_QUANTITY | — | ✅ |
| 24 | ParentSerialNumber | PARENT_SERIAL_NUMBER | — | ✅ |
| 25 | RelationshipTypeCode | RELATIONSHIP_TYPE_CODE | 🔑 | ✅ |
| 26 | RootGenObjectId | ROOT_GEN_OBJECT_ID | — | ✅ |
| 27 | RootItemId | ROOT_ITEM_ID | — | ✅ |
| 28 | RootLotNumber | ROOT_LOT_NUMBER | — | ✅ |
| 29 | RootOrganizationId | ROOT_ORGANIZATION_ID | — | ✅ |
| 30 | RootOrigDate | ROOT_ORIG_DATE | — | ✅ |
| 31 | RootOrigDocNumber | ROOT_ORIG_DOC_NUMBER | — | ✅ |
| 32 | RootOrigDocType | ROOT_ORIG_DOC_TYPE | — | ✅ |
| 33 | RootOrigQuantity | ROOT_ORIG_QUANTITY | — | ✅ |
| 34 | RootSerialNumber | ROOT_SERIAL_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
