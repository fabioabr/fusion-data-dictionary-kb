---
id: DOC-HCM-PVO-FndTreeVersionDeptVO
doc_type: system-doc
title: "FndTreeVersionDeptVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - FndTreeVersionDeptVO
  - fndtreeversiondeptvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FndTreeVersionDeptVO

## 📌 Visão Geral

Disponibiliza versões de árvore hierárquica de departamentos com vigência. Utilizado para representação temporal da estrutura departamental.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.OrganizationAM.FndTreeVersionDeptVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 1 | 3 | 6 | 26% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_tree_version_vl|FND_TREE_VERSION_VL]] — 23 atributos (3 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[fnd_tree_version_vl|FND_TREE_VERSION_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangedSinceValidation | CHANGED_SINCE_VALIDATION | — | — |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | Description | DESCRIPTION | — | — |
| 5 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 6 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | LastValidationDate | LAST_VALIDATION_DATE | — | — |
| 11 | LastValidationResult | LAST_VALIDATION_RESULT | — | — |
| 12 | LastValidationResultId | LAST_VALIDATION_RESULT_ID | — | — |
| 13 | LevelCount | LEVEL_COUNT | — | — |
| 14 | LockDate | LOCK_DATE | — | — |
| 15 | LockedBy | LOCKED_BY | — | — |
| 16 | NodeCount | NODE_COUNT | — | — |
| 17 | SourceTreeVersionId | SOURCE_TREE_VERSION_ID | — | — |
| 18 | Status | STATUS | — | — |
| 19 | TreeCode | TREE_CODE | 🔑 | ✅ |
| 20 | TreeStructureCode | TREE_STRUCTURE_CODE | 🔑 | ✅ |
| 21 | TreeVersionId | TREE_VERSION_ID | 🔑 | ✅ |
| 22 | TreeVersionName | TREE_VERSION_NAME | — | — |
| 23 | VersionComment | VERSION_COMMENT | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
