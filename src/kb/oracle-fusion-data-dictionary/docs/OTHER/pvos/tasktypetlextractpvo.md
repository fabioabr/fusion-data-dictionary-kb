---
id: DOC-OTHER-PVO-TaskTypeTLExtractPVO
doc_type: system-doc
title: "TaskTypeTLExtractPVO — PVO Cross-Module"
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
  - TaskTypeTLExtractPVO
  - tasktypetlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaskTypeTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Task Type TLExtract. Acessa as tabelas: DOO_TASK_TYPES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.TaskTypeTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_task_types_tl|DOO_TASK_TYPES_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[doo_task_types_tl|DOO_TASK_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskTypeTranslationCreatedBy | CREATED_BY | — | ✅ |
| 2 | TaskTypeTranslationCreationDate | CREATION_DATE | — | ✅ |
| 3 | TaskTypeTranslationDescription | DESCRIPTION | — | ✅ |
| 4 | TaskTypeTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | TaskTypeTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | TaskTypeTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | TaskTypeTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | TaskTypeTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | TaskTypeTranslationSourceLang | SOURCE_LANG | — | ✅ |
| 10 | TaskTypeTranslationTaskTypeId | TASK_TYPE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
