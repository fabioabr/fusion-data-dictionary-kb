---
id: DOC-OTHER-PVO-FosTaskTypeTranslationExtractPVO
doc_type: system-doc
title: "FosTaskTypeTranslationExtractPVO — PVO Cross-Module"
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
  - FosTaskTypeTranslationExtractPVO
  - fostasktypetranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FosTaskTypeTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fos Task Type Translation Extract. Acessa as tabelas: FOS_TASK_TYPE_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.FosBiccExtractAM.FosTaskTypeTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 2 | 12 | 86% |

---

## 🔗 Tabelas Relacionadas

- [[fos_task_type_tl|FOS_TASK_TYPE_TL]] — 14 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[fos_task_type_tl|FOS_TASK_TYPE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskTypeTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | TaskTypeTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | TaskTypeTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | TaskTypeTLPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 5 | TaskTypeTLPEOLanguage | LANGUAGE | 🔑 | — |
| 6 | TaskTypeTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | TaskTypeTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | TaskTypeTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | TaskTypeTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | TaskTypeTLPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 11 | TaskTypeTLPEOSourceLang | SOURCE_LANG | — | — |
| 12 | TaskTypeTLPEOTaskGroupName | TASK_GROUP_NAME | — | ✅ |
| 13 | TaskTypeTLPEOTaskName | TASK_NAME | — | ✅ |
| 14 | TaskTypeTLPEOTaskTypeId | TASK_TYPE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
