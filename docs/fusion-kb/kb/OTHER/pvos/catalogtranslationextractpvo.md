---
id: DOC-OTHER-PVO-CatalogTranslationExtractPVO
doc_type: system-doc
title: "CatalogTranslationExtractPVO — PVO Cross-Module"
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
  - CatalogTranslationExtractPVO
  - catalogtranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CatalogTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Catalog Translation Extract. Acessa as tabelas: EGP_CATEGORY_SETS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgpBiccExtractAM.CatalogTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[egp_category_sets_tl|EGP_CATEGORY_SETS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[egp_category_sets_tl|EGP_CATEGORY_SETS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CatalogTranslationPEOCategorySetId | CATEGORY_SET_ID | 🔑 | ✅ |
| 2 | CatalogTranslationPEOCategorySetName | CATEGORY_SET_NAME | — | ✅ |
| 3 | CatalogTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | CatalogTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | CatalogTranslationPEODescription | DESCRIPTION | — | ✅ |
| 6 | CatalogTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | CatalogTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | CatalogTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | CatalogTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | CatalogTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
