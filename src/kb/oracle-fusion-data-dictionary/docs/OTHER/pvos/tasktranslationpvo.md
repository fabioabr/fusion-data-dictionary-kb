---
id: DOC-OTHER-PVO-TaskTranslationPVO
doc_type: system-doc
title: "TaskTranslationPVO — PVO Cross-Module"
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
  - TaskTranslationPVO
  - tasktranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaskTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Task Translation. Acessa as tabelas: PJF_PROJ_ELEMENTS_TL.

**Caminho:** `FscmTopModelAM.PjfProjectDefinitionAM.TaskTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 9 | 75% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_proj_elements_tl|PJF_PROJ_ELEMENTS_TL]] — 12 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[pjf_proj_elements_tl|PJF_PROJ_ELEMENTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | Language | LANGUAGE | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | Name | NAME | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ProjElementId | PROJ_ELEMENT_ID | 🔑 | ✅ |
| 11 | ProjectId | PROJECT_ID | — | — |
| 12 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
