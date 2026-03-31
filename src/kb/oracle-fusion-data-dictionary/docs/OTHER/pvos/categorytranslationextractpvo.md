---
id: DOC-OTHER-PVO-CategoryTranslationExtractPVO
doc_type: system-doc
title: "CategoryTranslationExtractPVO — PVO Cross-Module"
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
  - CategoryTranslationExtractPVO
  - categorytranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CategoryTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Category Translation Extract. Acessa as tabelas: EGP_CATEGORIES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgpBiccExtractAM.CategoryTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[egp_categories_tl|EGP_CATEGORIES_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[egp_categories_tl|EGP_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryTranslationPEOCategoryId | CATEGORY_ID | 🔑 | ✅ |
| 2 | CategoryTranslationPEOCategoryName | CATEGORY_NAME | — | ✅ |
| 3 | CategoryTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | CategoryTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | CategoryTranslationPEODescription | DESCRIPTION | — | ✅ |
| 6 | CategoryTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | CategoryTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | CategoryTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | CategoryTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | CategoryTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
