---
id: DOC-OTHER-PVO-TaskStructureTranslationExtractPVO
doc_type: system-doc
title: "TaskStructureTranslationExtractPVO — PVO Cross-Module"
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
  - TaskStructureTranslationExtractPVO
  - taskstructuretranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaskStructureTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Task Structure Translation Extract. Acessa as tabelas: PJF_PROJ_ELEMENTS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.TaskStructureTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_proj_elements_tl|PJF_PROJ_ELEMENTS_TL]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[pjf_proj_elements_tl|PJF_PROJ_ELEMENTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskStructureTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | TaskStructureTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | TaskStructureTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | TaskStructureTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | TaskStructureTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | TaskStructureTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | TaskStructureTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | TaskStructureTranslationPEOName | NAME | — | ✅ |
| 9 | TaskStructureTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | TaskStructureTranslationPEOProjElementId | PROJ_ELEMENT_ID | 🔑 | ✅ |
| 11 | TaskStructureTranslationPEOProjectId | PROJECT_ID | — | ✅ |
| 12 | TaskStructureTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
