---
id: DOC-OTHER-PVO-FndTreeNodeExtractPVO
doc_type: system-doc
title: "FndTreeNodeExtractPVO — PVO Cross-Module"
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
  - FndTreeNodeExtractPVO
  - fndtreenodeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FndTreeNodeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fnd Tree Node Extract. Acessa as tabelas: FND_TREE_NODE.

**Caminho:** `FscmTopModelAM.FinExtractAM.AnalyticsExtractServiceAM.FndTreeNodeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 34 | 1 | 4 | 34 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_tree_node|FND_TREE_NODE]] — 34 atributos (4 PKs, 34 BICC)

---

## ⚙️ Atributos

### [[fnd_tree_node|FND_TREE_NODE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChildCount | CHILD_COUNT | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | DataSourceId | DATA_SOURCE_ID | — | ✅ |
| 5 | Depth | DEPTH | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ParentDataSourceId | PARENT_DATA_SOURCE_ID | — | ✅ |
| 10 | ParentPk1Value | PARENT_PK1_VALUE | — | ✅ |
| 11 | ParentPk2Value | PARENT_PK2_VALUE | — | ✅ |
| 12 | ParentPk3Value | PARENT_PK3_VALUE | — | ✅ |
| 13 | ParentPk4Value | PARENT_PK4_VALUE | — | ✅ |
| 14 | ParentPk5Value | PARENT_PK5_VALUE | — | ✅ |
| 15 | ParentTreeLabelId | PARENT_TREE_LABEL_ID | — | ✅ |
| 16 | ParentTreeNodeId | PARENT_TREE_NODE_ID | — | ✅ |
| 17 | Pk1EndValue | PK1_END_VALUE | — | ✅ |
| 18 | Pk1StartValue | PK1_START_VALUE | — | ✅ |
| 19 | Pk2EndValue | PK2_END_VALUE | — | ✅ |
| 20 | Pk2StartValue | PK2_START_VALUE | — | ✅ |
| 21 | Pk3EndValue | PK3_END_VALUE | — | ✅ |
| 22 | Pk3StartValue | PK3_START_VALUE | — | ✅ |
| 23 | Pk4EndValue | PK4_END_VALUE | — | ✅ |
| 24 | Pk4StartValue | PK4_START_VALUE | — | ✅ |
| 25 | Pk5EndValue | PK5_END_VALUE | — | ✅ |
| 26 | Pk5StartValue | PK5_START_VALUE | — | ✅ |
| 27 | ReferenceTreeCode | REFERENCE_TREE_CODE | — | ✅ |
| 28 | ReferenceTreeVersionId | REFERENCE_TREE_VERSION_ID | — | ✅ |
| 29 | SortOrder | SORT_ORDER | — | ✅ |
| 30 | TreeCode | TREE_CODE | 🔑 | ✅ |
| 31 | TreeLabelId | TREE_LABEL_ID | — | ✅ |
| 32 | TreeNodeId | TREE_NODE_ID | 🔑 | ✅ |
| 33 | TreeStructureCode | TREE_STRUCTURE_CODE | 🔑 | ✅ |
| 34 | TreeVersionId | TREE_VERSION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
