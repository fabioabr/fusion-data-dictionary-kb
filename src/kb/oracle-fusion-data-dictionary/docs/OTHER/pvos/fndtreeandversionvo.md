---
id: DOC-OTHER-PVO-FndTreeAndVersionVO
doc_type: system-doc
title: "FndTreeAndVersionVO — PVO Cross-Module"
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
  - FndTreeAndVersionVO
  - fndtreeandversionvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FndTreeAndVersionVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fnd Tree And Version VO. Acessa as tabelas: FND_TREE_FLATTENING_HISTORY, FND_TREE_VERSION_VL, FND_TREE_VL.

**Caminho:** `FscmTopModelAM.FinExtractAM.AnalyticsExtractServiceAM.FndTreeAndVersionVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 3 | 2 | 29 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_tree_flattening_history|FND_TREE_FLATTENING_HISTORY]] — 5 atributos (5 BICC)
- [[fnd_tree_version_vl|FND_TREE_VERSION_VL]] — 13 atributos (13 BICC)
- [[fnd_tree_vl|FND_TREE_VL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[fnd_tree_flattening_history|FND_TREE_FLATTENING_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FlatHistTreeCode | TREE_CODE | — | ✅ |
| 2 | FlatHistTreeStructureCode | TREE_STRUCTURE_CODE | — | ✅ |
| 3 | FlatHistTreeVersionId | TREE_VERSION_ID | — | ✅ |
| 4 | FlatteningType | FLATTENING_TYPE | — | ✅ |
| 5 | ProcessPoint | PROCESS_POINT | — | ✅ |

### [[fnd_tree_version_vl|FND_TREE_VERSION_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TreeVersionId | TREE_VERSION_ID | — | ✅ |
| 2 | VersionCreatedBy | CREATED_BY | — | ✅ |
| 3 | VersionCreationDate | CREATION_DATE | — | ✅ |
| 4 | VersionDescription | DESCRIPTION | — | ✅ |
| 5 | VersionEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 6 | VersionEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | VersionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | VersionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | VersionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | VersionName | TREE_VERSION_NAME | — | ✅ |
| 11 | VersionStatus | STATUS | — | ✅ |
| 12 | VersionTreeCode | TREE_CODE | — | ✅ |
| 13 | VersionTreeStructureCode | TREE_STRUCTURE_CODE | — | ✅ |

### [[fnd_tree_vl|FND_TREE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TreeCode | TREE_CODE | 🔑 | ✅ |
| 2 | TreeCreatedBy | CREATED_BY | — | ✅ |
| 3 | TreeCreationDate | CREATION_DATE | — | ✅ |
| 4 | TreeDescription | DESCRIPTION | — | ✅ |
| 5 | TreeIconName | ICON_NAME | — | ✅ |
| 6 | TreeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | TreeLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | TreeLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | TreeName | TREE_NAME | — | ✅ |
| 10 | TreeSetId | SET_ID | — | ✅ |
| 11 | TreeStructureCode | TREE_STRUCTURE_CODE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
