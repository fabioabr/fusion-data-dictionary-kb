---
id: DOC-OTHER-PVO-DeptTreeNodeRFExtractPVO
doc_type: system-doc
title: "DeptTreeNodeRFExtractPVO — PVO Cross-Module"
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
  - DeptTreeNodeRFExtractPVO
  - depttreenoderfextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DeptTreeNodeRFExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Dept Tree Node RFExtract. Acessa as tabelas: PER_DEPT_TREE_NODE_RF.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.OrganizationBiccExtractAM.DeptTreeNodeRFExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 1 | 6 | 28 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[per_dept_tree_node_rf|PER_DEPT_TREE_NODE_RF]] — 28 atributos (6 PKs, 28 BICC)

---

## ⚙️ Atributos

### [[per_dept_tree_node_rf|PER_DEPT_TREE_NODE_RF]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AncestorDataSourceId | ANCESTOR_DATA_SOURCE_ID | — | ✅ |
| 2 | AncestorPk1Value | ANCESTOR_PK1_VALUE | — | ✅ |
| 3 | AncestorPk2Value | ANCESTOR_PK2_VALUE | — | ✅ |
| 4 | AncestorPk3Value | ANCESTOR_PK3_VALUE | — | ✅ |
| 5 | AncestorPk4Value | ANCESTOR_PK4_VALUE | — | ✅ |
| 6 | AncestorPk5Value | ANCESTOR_PK5_VALUE | — | ✅ |
| 7 | AncestorTreeLabelId | ANCESTOR_TREE_LABEL_ID | — | ✅ |
| 8 | AncestorTreeNodeId | ANCESTOR_TREE_NODE_ID | — | ✅ |
| 9 | CreatedBy | CREATED_BY | — | ✅ |
| 10 | CreationDate | CREATION_DATE | — | ✅ |
| 11 | DataSourceId | DATA_SOURCE_ID | — | ✅ |
| 12 | Distance | DISTANCE | — | ✅ |
| 13 | EnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 14 | IsLeaf | IS_LEAF | — | ✅ |
| 15 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | Pk1Value | PK1_VALUE | — | ✅ |
| 19 | Pk2Value | PK2_VALUE | — | ✅ |
| 20 | Pk3Value | PK3_VALUE | — | ✅ |
| 21 | Pk4Value | PK4_VALUE | — | ✅ |
| 22 | Pk5Value | PK5_VALUE | — | ✅ |
| 23 | RfTreeNodeId | RF_TREE_NODE_ID | 🔑 | ✅ |
| 24 | TreeCode | TREE_CODE | 🔑 | ✅ |
| 25 | TreeLabelId | TREE_LABEL_ID | — | ✅ |
| 26 | TreeNodeId | TREE_NODE_ID | 🔑 | ✅ |
| 27 | TreeStructureCode | TREE_STRUCTURE_CODE | 🔑 | ✅ |
| 28 | TreeVersionId | TREE_VERSION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
