---
id: DOC-OTHER-PVO-CategoryTLExtractPVO
doc_type: system-doc
title: "CategoryTLExtractPVO — PVO Cross-Module"
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
  - CategoryTLExtractPVO
  - categorytlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CategoryTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Category TLExtract. Acessa as tabelas: FA_CATEGORIES_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.CategoryTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fa_categories_tl|FA_CATEGORIES_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[fa_categories_tl|FA_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryTranslationCategoryId | CATEGORY_ID | 🔑 | ✅ |
| 2 | CategoryTranslationCreatedBy | CREATED_BY | — | ✅ |
| 3 | CategoryTranslationCreationDate | CREATION_DATE | — | ✅ |
| 4 | CategoryTranslationDescription | DESCRIPTION | — | ✅ |
| 5 | CategoryTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | CategoryTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | CategoryTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | CategoryTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | CategoryTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | CategoryTranslationSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
