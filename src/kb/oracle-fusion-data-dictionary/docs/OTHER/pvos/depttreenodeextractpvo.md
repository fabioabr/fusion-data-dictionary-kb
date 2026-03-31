---
id: DOC-OTHER-PVO-DeptTreeNodeExtractPVO
doc_type: system-doc
title: "DeptTreeNodeExtractPVO — PVO Cross-Module"
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
  - DeptTreeNodeExtractPVO
  - depttreenodeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DeptTreeNodeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Dept Tree Node Extract. Acessa as tabelas: PER_DEPT_TREE_NODE.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.OrganizationBiccExtractAM.DeptTreeNodeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 35 | 1 | 4 | 35 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[per_dept_tree_node|PER_DEPT_TREE_NODE]] — 35 atributos (4 PKs, 35 BICC)

---

## ⚙️ Atributos

### [[per_dept_tree_node|PER_DEPT_TREE_NODE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChildCount | CHILD_COUNT | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | DataSourceId | DATA_SOURCE_ID | — | ✅ |
| 5 | Depth | DEPTH | — | ✅ |
| 6 | EnterpriseId | ENTERPRISE_ID | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ParentDataSourceId | PARENT_DATA_SOURCE_ID | — | ✅ |
| 11 | ParentPk1Value | PARENT_PK1_VALUE | — | ✅ |
| 12 | ParentPk2Value | PARENT_PK2_VALUE | — | ✅ |
| 13 | ParentPk3Value | PARENT_PK3_VALUE | — | ✅ |
| 14 | ParentPk4Value | PARENT_PK4_VALUE | — | ✅ |
| 15 | ParentPk5Value | PARENT_PK5_VALUE | — | ✅ |
| 16 | ParentTreeLabelId | PARENT_TREE_LABEL_ID | — | ✅ |
| 17 | ParentTreeNodeId | PARENT_TREE_NODE_ID | — | ✅ |
| 18 | Pk1EndValue | PK1_END_VALUE | — | ✅ |
| 19 | Pk1StartValue | PK1_START_VALUE | — | ✅ |
| 20 | Pk2EndValue | PK2_END_VALUE | — | ✅ |
| 21 | Pk2StartValue | PK2_START_VALUE | — | ✅ |
| 22 | Pk3EndValue | PK3_END_VALUE | — | ✅ |
| 23 | Pk3StartValue | PK3_START_VALUE | — | ✅ |
| 24 | Pk4EndValue | PK4_END_VALUE | — | ✅ |
| 25 | Pk4StartValue | PK4_START_VALUE | — | ✅ |
| 26 | Pk5EndValue | PK5_END_VALUE | — | ✅ |
| 27 | Pk5StartValue | PK5_START_VALUE | — | ✅ |
| 28 | ReferenceTreeCode | REFERENCE_TREE_CODE | — | ✅ |
| 29 | ReferenceTreeVersionId | REFERENCE_TREE_VERSION_ID | — | ✅ |
| 30 | SortOrder | SORT_ORDER | — | ✅ |
| 31 | TreeCode | TREE_CODE | 🔑 | ✅ |
| 32 | TreeLabelId | TREE_LABEL_ID | — | ✅ |
| 33 | TreeNodeId | TREE_NODE_ID | 🔑 | ✅ |
| 34 | TreeStructureCode | TREE_STRUCTURE_CODE | 🔑 | ✅ |
| 35 | TreeVersionId | TREE_VERSION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
