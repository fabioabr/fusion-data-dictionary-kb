---
id: DOC-OTHER-PVO-ClassCategoryTranslationExtractPVO
doc_type: system-doc
title: "ClassCategoryTranslationExtractPVO — PVO Cross-Module"
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
  - ClassCategoryTranslationExtractPVO
  - classcategorytranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ClassCategoryTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Class Category Translation Extract. Acessa as tabelas: PJF_CLASS_CATEGORIES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ClassCategoryTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_class_categories_tl|PJF_CLASS_CATEGORIES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[pjf_class_categories_tl|PJF_CLASS_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClassCategoryTranslationPEOClassCategory | CLASS_CATEGORY | — | ✅ |
| 2 | ClassCategoryTranslationPEOClassCategoryId | CLASS_CATEGORY_ID | 🔑 | ✅ |
| 3 | ClassCategoryTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | ClassCategoryTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | ClassCategoryTranslationPEODescription | DESCRIPTION | — | ✅ |
| 6 | ClassCategoryTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | ClassCategoryTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ClassCategoryTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | ClassCategoryTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ClassCategoryTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ClassCategoryTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
