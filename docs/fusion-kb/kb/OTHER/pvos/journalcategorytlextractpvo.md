---
id: DOC-OTHER-PVO-JournalCategoryTLExtractPVO
doc_type: system-doc
title: "JournalCategoryTLExtractPVO — PVO Cross-Module"
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
  - JournalCategoryTLExtractPVO
  - journalcategorytlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JournalCategoryTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Journal Category TLExtract. Acessa as tabelas: GL_JE_CATEGORIES_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.GlBiccExtractAM.JournalCategoryTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gl_je_categories_tl|GL_JE_CATEGORIES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[gl_je_categories_tl|GL_JE_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JrnlCatTranslationCreatedBy | CREATED_BY | — | ✅ |
| 2 | JrnlCatTranslationCreationDate | CREATION_DATE | — | ✅ |
| 3 | JrnlCatTranslationDescription | DESCRIPTION | — | ✅ |
| 4 | JrnlCatTranslationJeCategoryName | JE_CATEGORY_NAME | 🔑 | ✅ |
| 5 | JrnlCatTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | JrnlCatTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | JrnlCatTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | JrnlCatTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | JrnlCatTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | JrnlCatTranslationSourceLang | SOURCE_LANG | — | ✅ |
| 11 | JrnlCatTranslationUserJeCategoryName | USER_JE_CATEGORY_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
