---
id: DOC-OTHER-PVO-JournalCategoryExtractPVO
doc_type: system-doc
title: "JournalCategoryExtractPVO — PVO Cross-Module"
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
  - JournalCategoryExtractPVO
  - journalcategoryextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JournalCategoryExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Journal Category Extract. Acessa as tabelas: GL_JE_CATEGORIES_B, GL_JE_CATEGORIES_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.GlBiccExtractAM.JournalCategoryExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 2 | 1 | 18 | 75% |

---

## 🔗 Tabelas Relacionadas

- [[gl_je_categories_b|GL_JE_CATEGORIES_B]] — 14 atributos (1 PKs, 8 BICC)
- [[gl_je_categories_tl|GL_JE_CATEGORIES_TL]] — 10 atributos (10 BICC)

---

## ⚙️ Atributos

### [[gl_je_categories_b|GL_JE_CATEGORIES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JournalCategoryAttrCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | JournalCategoryAttribute1 | ATTRIBUTE1 | — | — |
| 3 | JournalCategoryAttribute2 | ATTRIBUTE2 | — | — |
| 4 | JournalCategoryAttribute3 | ATTRIBUTE3 | — | — |
| 5 | JournalCategoryAttribute4 | ATTRIBUTE4 | — | — |
| 6 | JournalCategoryAttribute5 | ATTRIBUTE5 | — | — |
| 7 | JournalCategoryCreatedBy | CREATED_BY | — | ✅ |
| 8 | JournalCategoryCreationDate | CREATION_DATE | — | ✅ |
| 9 | JournalCategoryJeCategoryKey | JE_CATEGORY_KEY | — | ✅ |
| 10 | JournalCategoryJeCategoryName | JE_CATEGORY_NAME | 🔑 | ✅ |
| 11 | JournalCategoryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | JournalCategoryLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | JournalCategoryLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | JournalCategoryObjectVerNum | OBJECT_VERSION_NUMBER | — | ✅ |

### [[gl_je_categories_tl|GL_JE_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JrnlCatTransLangCreatedBy | CREATED_BY | — | ✅ |
| 2 | JrnlCatTransLangCreationDate | CREATION_DATE | — | ✅ |
| 3 | JrnlCatTransLangDescription | DESCRIPTION | — | ✅ |
| 4 | JrnlCatTransLangJeCategoryName | JE_CATEGORY_NAME | — | ✅ |
| 5 | JrnlCatTransLangLanguage | LANGUAGE | — | ✅ |
| 6 | JrnlCatTransLangLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | JrnlCatTransLangLastUpdateLogn | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | JrnlCatTransLangLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | JrnlCatTransLangSourceLang | SOURCE_LANG | — | ✅ |
| 10 | JrnlCatTransLangUserJeCatName | USER_JE_CATEGORY_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
