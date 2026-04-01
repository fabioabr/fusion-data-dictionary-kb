---
id: DOC-OTHER-PVO-FndTreeVersionExtractPVO
doc_type: system-doc
title: "FndTreeVersionExtractPVO — PVO Cross-Module"
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
  - FndTreeVersionExtractPVO
  - fndtreeversionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FndTreeVersionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fnd Tree Version Extract. Acessa as tabelas: FND_TREE_VERSION.

**Caminho:** `FscmTopModelAM.FinExtractAM.AnalyticsExtractServiceAM.FndTreeVersionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 1 | 3 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_tree_version|FND_TREE_VERSION]] — 21 atributos (3 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[fnd_tree_version|FND_TREE_VERSION]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangedSinceValidation | CHANGED_SINCE_VALIDATION | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 5 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | LastValidationDate | LAST_VALIDATION_DATE | — | ✅ |
| 10 | LastValidationResult | LAST_VALIDATION_RESULT | — | ✅ |
| 11 | LastValidationResultId | LAST_VALIDATION_RESULT_ID | — | ✅ |
| 12 | LevelCount | LEVEL_COUNT | — | ✅ |
| 13 | LockDate | LOCK_DATE | — | ✅ |
| 14 | LockedBy | LOCKED_BY | — | ✅ |
| 15 | NodeCount | NODE_COUNT | — | ✅ |
| 16 | SeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 17 | SourceTreeVersionId | SOURCE_TREE_VERSION_ID | — | ✅ |
| 18 | Status | STATUS | — | ✅ |
| 19 | TreeCode | TREE_CODE | 🔑 | ✅ |
| 20 | TreeStructureCode | TREE_STRUCTURE_CODE | 🔑 | ✅ |
| 21 | TreeVersionId | TREE_VERSION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
