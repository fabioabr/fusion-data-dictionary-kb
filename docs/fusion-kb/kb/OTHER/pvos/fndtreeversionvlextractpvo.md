---
id: DOC-OTHER-PVO-FndTreeVersionVLExtractPVO
doc_type: system-doc
title: "FndTreeVersionVLExtractPVO — PVO Cross-Module"
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
  - FndTreeVersionVLExtractPVO
  - fndtreeversionvlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FndTreeVersionVLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fnd Tree Version VLExtract. Acessa as tabelas: FND_TREE_VERSION_VL.

**Caminho:** `FscmTopModelAM.FinExtractAM.AnalyticsExtractServiceAM.FndTreeVersionVLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 1 | 3 | 23 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_tree_version_vl|FND_TREE_VERSION_VL]] — 23 atributos (3 PKs, 23 BICC)

---

## ⚙️ Atributos

### [[fnd_tree_version_vl|FND_TREE_VERSION_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangedSinceValidation | CHANGED_SINCE_VALIDATION | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | Description | DESCRIPTION | — | ✅ |
| 5 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 6 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | LastValidationDate | LAST_VALIDATION_DATE | — | ✅ |
| 11 | LastValidationResult | LAST_VALIDATION_RESULT | — | ✅ |
| 12 | LastValidationResultId | LAST_VALIDATION_RESULT_ID | — | ✅ |
| 13 | LevelCount | LEVEL_COUNT | — | ✅ |
| 14 | LockDate | LOCK_DATE | — | ✅ |
| 15 | LockedBy | LOCKED_BY | — | ✅ |
| 16 | NodeCount | NODE_COUNT | — | ✅ |
| 17 | SourceTreeVersionId | SOURCE_TREE_VERSION_ID | — | ✅ |
| 18 | Status | STATUS | — | ✅ |
| 19 | TreeCode | TREE_CODE | 🔑 | ✅ |
| 20 | TreeStructureCode | TREE_STRUCTURE_CODE | 🔑 | ✅ |
| 21 | TreeVersionId | TREE_VERSION_ID | 🔑 | ✅ |
| 22 | TreeVersionName | TREE_VERSION_NAME | — | ✅ |
| 23 | VersionComment | VERSION_COMMENT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
