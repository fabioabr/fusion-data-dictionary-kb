---
id: DOC-OTHER-PVO-FndTreeStructureExtractPVO
doc_type: system-doc
title: "FndTreeStructureExtractPVO — PVO Cross-Module"
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
  - FndTreeStructureExtractPVO
  - fndtreestructureextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FndTreeStructureExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fnd Tree Structure Extract. Acessa as tabelas: FND_TREE_STRUCTURE_VL.

**Caminho:** `FscmTopModelAM.FinExtractAM.AnalyticsExtractServiceAM.FndTreeStructureExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 33 | 1 | 1 | 33 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_tree_structure_vl|FND_TREE_STRUCTURE_VL]] — 33 atributos (1 PKs, 33 BICC)

---

## ⚙️ Atributos

### [[fnd_tree_structure_vl|FND_TREE_STRUCTURE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllowMultipleActiveVers | ALLOW_MULTIPLE_ACTIVE_VERS | — | ✅ |
| 2 | AllowMultipleRootNodes | ALLOW_MULTIPLE_ROOT_NODES | — | ✅ |
| 3 | AllowNodeLevelSecurity | ALLOW_NODE_LEVEL_SECURITY | — | ✅ |
| 4 | AllowRaggedNodes | ALLOW_RAGGED_NODES | — | ✅ |
| 5 | AllowSkipLevelNodes | ALLOW_SKIP_LEVEL_NODES | — | ✅ |
| 6 | ApplicationId | APPLICATION_ID | — | ✅ |
| 7 | BiViewObjectDefName | BI_VIEW_OBJECT_DEF_NAME | — | ✅ |
| 8 | CreatedBy | CREATED_BY | — | ✅ |
| 9 | CreationDate | CREATION_DATE | — | ✅ |
| 10 | CreationMode | CREATION_MODE | — | ✅ |
| 11 | Customizable | CUSTOMIZABLE | — | ✅ |
| 12 | Description | DESCRIPTION | — | ✅ |
| 13 | IdColFlattenedTable | ID_COL_FLATTENED_TABLE | — | ✅ |
| 14 | LabelingScheme | LABELING_SCHEME | — | ✅ |
| 15 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | ModuleId | MODULE_ID | — | ✅ |
| 19 | NdSearchViewObjectDefName | ND_SEARCH_VIEW_OBJECT_DEF_NAME | — | ✅ |
| 20 | NumberOfTrees | NUMBER_OF_TREES | — | ✅ |
| 21 | OptionalLabelEnforcement | OPTIONAL_LABEL_ENFORCEMENT | — | ✅ |
| 22 | ProtectedFlag | PROTECTED_FLAG | — | ✅ |
| 23 | RefreshInterval | REFRESH_INTERVAL | — | ✅ |
| 24 | RestrictByDate | RESTRICT_BY_DATE | — | ✅ |
| 25 | RestrictBySetid | RESTRICT_BY_SETID | — | ✅ |
| 26 | RowFlattenedTable | ROW_FLATTENED_TABLE | — | ✅ |
| 27 | SharingScheme | SHARING_SCHEME | — | ✅ |
| 28 | Status | STATUS | — | ✅ |
| 29 | TreeNodeTable | TREE_NODE_TABLE | — | ✅ |
| 30 | TreeNodeViewObjectDefName | TREE_NODE_VIEW_OBJECT_DEF_NAME | — | ✅ |
| 31 | TreeStructureCode | TREE_STRUCTURE_CODE | 🔑 | ✅ |
| 32 | TreeStructureName | TREE_STRUCTURE_NAME | — | ✅ |
| 33 | Versioning | VERSIONING | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
