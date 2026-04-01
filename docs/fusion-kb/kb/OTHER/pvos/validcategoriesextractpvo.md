---
id: DOC-OTHER-PVO-ValidCategoriesExtractPVO
doc_type: system-doc
title: "ValidCategoriesExtractPVO — PVO Cross-Module"
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
  - ValidCategoriesExtractPVO
  - validcategoriesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ValidCategoriesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Valid Categories Extract. Acessa as tabelas: EGP_CATEGORY_SET_VALID_CATS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgpBiccExtractAM.ValidCategoriesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[egp_category_set_valid_cats|EGP_CATEGORY_SET_VALID_CATS]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[egp_category_set_valid_cats|EGP_CATEGORY_SET_VALID_CATS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ValidCategoryPEOCategoryId | CATEGORY_ID | 🔑 | ✅ |
| 2 | ValidCategoryPEOCategorySetId | CATEGORY_SET_ID | 🔑 | ✅ |
| 3 | ValidCategoryPEOCategorySharedFlag | CATEGORY_SHARED_FLAG | — | ✅ |
| 4 | ValidCategoryPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | ValidCategoryPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | ValidCategoryPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ValidCategoryPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | ValidCategoryPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ValidCategoryPEOParentCategoryId | PARENT_CATEGORY_ID | — | ✅ |
| 10 | ValidCategoryPEOReferenceCategorySetId | REFERENCE_CATEGORY_SET_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
