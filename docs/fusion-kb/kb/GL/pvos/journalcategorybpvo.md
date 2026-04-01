---
id: DOC-GL-PVO-JournalCategoryBPVO
doc_type: system-doc
title: "JournalCategoryBPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - JournalCategoryBPVO
  - journalcategorybpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JournalCategoryBPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Journal Category B. Acessa as tabelas: GL_JE_CATEGORIES_B, GL_JE_CATEGORIES_TL.

**Caminho:** `FscmTopModelAM.FinGlJrnlSetupCatAM.JournalCategoryBPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 31 | 2 | 1 | 8 | 26% |

---

## 🔗 Tabelas Relacionadas

- [[gl_je_categories_b|GL_JE_CATEGORIES_B]] — 9 atributos (1 PKs, 3 BICC)
- [[gl_je_categories_tl|GL_JE_CATEGORIES_TL]] — 22 atributos (5 BICC)

---

## ⚙️ Atributos

### [[gl_je_categories_b|GL_JE_CATEGORIES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JeCategoryName | JE_CATEGORY_NAME | 🔑 | ✅ |
| 2 | JrnlCatConsolidationFlag | CONSOLIDATION_FLAG | — | — |
| 3 | JrnlCatCreatedBy | CREATED_BY | — | — |
| 4 | JrnlCatCreationDate | CREATION_DATE | — | — |
| 5 | JrnlCatJeCategoryKey | JE_CATEGORY_KEY | — | ✅ |
| 6 | JrnlCatLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | JrnlCatLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | JrnlCatLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | JrnlCatObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[gl_je_categories_tl|GL_JE_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JrnlCatTranslatedCreatedBy | CREATED_BY | — | — |
| 2 | JrnlCatTranslatedCreationDate | CREATION_DATE | — | — |
| 3 | JrnlCatTranslatedDescription | DESCRIPTION | — | ✅ |
| 4 | JrnlCatTranslatedJeCategoryName | JE_CATEGORY_NAME | — | ✅ |
| 5 | JrnlCatTranslatedLangCreatedBy | CREATED_BY | — | — |
| 6 | JrnlCatTranslatedLangCreationDate | CREATION_DATE | — | — |
| 7 | JrnlCatTranslatedLangDescription | DESCRIPTION | — | — |
| 8 | JrnlCatTranslatedLangJeCategoryName | JE_CATEGORY_NAME | — | — |
| 9 | JrnlCatTranslatedLangLanguage | LANGUAGE | — | — |
| 10 | JrnlCatTranslatedLangLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 11 | JrnlCatTranslatedLangLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | JrnlCatTranslatedLangLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | JrnlCatTranslatedLangObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | JrnlCatTranslatedLangSourceLang | SOURCE_LANG | — | — |
| 15 | JrnlCatTranslatedLangUserJeCategoryName | USER_JE_CATEGORY_NAME | — | — |
| 16 | JrnlCatTranslatedLanguage | LANGUAGE | — | ✅ |
| 17 | JrnlCatTranslatedLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | JrnlCatTranslatedLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | JrnlCatTranslatedLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | JrnlCatTranslatedObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | JrnlCatTranslatedSourceLang | SOURCE_LANG | — | — |
| 22 | JrnlCatTranslatedUserJeCategoryName | USER_JE_CATEGORY_NAME | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
