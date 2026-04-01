---
id: DOC-PO-PVO-BrowsingCategoryTranslationExtractPVO
doc_type: system-doc
title: "BrowsingCategoryTranslationExtractPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - BrowsingCategoryTranslationExtractPVO
  - browsingcategorytranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BrowsingCategoryTranslationExtractPVO

## 📌 Visão Geral

Extrai traduções dos nomes de categorias de navegação para múltiplos idiomas. Garante que o catálogo de compras seja acessível e compreensível em todas as localidades da organização.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PorBiccExtractAM.BrowsingCategoryTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[por_browse_categories_tl|POR_BROWSE_CATEGORIES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[por_browse_categories_tl|POR_BROWSE_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryDescription | CATEGORY_DESCRIPTION | — | ✅ |
| 2 | CategoryId | CATEGORY_ID | 🔑 | ✅ |
| 3 | CategoryName | CATEGORY_NAME | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | Language | LANGUAGE | 🔑 | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
