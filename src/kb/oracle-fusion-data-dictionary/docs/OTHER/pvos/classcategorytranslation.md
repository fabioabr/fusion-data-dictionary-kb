---
id: DOC-OTHER-PVO-ClassCategoryTranslation
doc_type: system-doc
title: "ClassCategoryTranslation — PVO Cross-Module"
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
  - ClassCategoryTranslation
  - classcategorytranslation
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ClassCategoryTranslation

## 📌 Visão Geral

View Object para extração BICC de dados de Class Category Translation. Acessa as tabelas: PJF_CLASS_CATEGORIES_TL.

**Caminho:** `FscmTopModelAM.PjfSetupProjectsAM.ClassCategoryTranslation`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 9 | 82% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_class_categories_tl|PJF_CLASS_CATEGORIES_TL]] — 11 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[pjf_class_categories_tl|PJF_CLASS_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClassCategory | CLASS_CATEGORY | — | ✅ |
| 2 | ClassCategoryId | CLASS_CATEGORY_ID | 🔑 | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | Description | DESCRIPTION | — | ✅ |
| 6 | Language | LANGUAGE | 🔑 | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
