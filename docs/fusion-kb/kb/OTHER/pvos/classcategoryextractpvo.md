---
id: DOC-OTHER-PVO-ClassCategoryExtractPVO
doc_type: system-doc
title: "ClassCategoryExtractPVO — PVO Cross-Module"
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
  - ClassCategoryExtractPVO
  - classcategoryextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ClassCategoryExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Class Category Extract. Acessa as tabelas: PJF_CLASS_CATEGORIES_B, PJF_CLASS_CATEGORIES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ClassCategoryExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 43 | 2 | 1 | 27 | 63% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_class_categories_b|PJF_CLASS_CATEGORIES_B]] — 32 atributos (1 PKs, 16 BICC)
- [[pjf_class_categories_tl|PJF_CLASS_CATEGORIES_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[pjf_class_categories_b|PJF_CLASS_CATEGORIES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClassCategoryBasePEOAllTypesValidFlag | ALL_TYPES_VALID_FLAG | — | ✅ |
| 2 | ClassCategoryBasePEOAllowPercentFlag | ALLOW_PERCENT_FLAG | — | ✅ |
| 3 | ClassCategoryBasePEOAttribute1 | ATTRIBUTE1 | — | — |
| 4 | ClassCategoryBasePEOAttribute10 | ATTRIBUTE10 | — | — |
| 5 | ClassCategoryBasePEOAttribute11 | ATTRIBUTE11 | — | — |
| 6 | ClassCategoryBasePEOAttribute12 | ATTRIBUTE12 | — | — |
| 7 | ClassCategoryBasePEOAttribute13 | ATTRIBUTE13 | — | — |
| 8 | ClassCategoryBasePEOAttribute14 | ATTRIBUTE14 | — | — |
| 9 | ClassCategoryBasePEOAttribute15 | ATTRIBUTE15 | — | — |
| 10 | ClassCategoryBasePEOAttribute2 | ATTRIBUTE2 | — | — |
| 11 | ClassCategoryBasePEOAttribute3 | ATTRIBUTE3 | — | — |
| 12 | ClassCategoryBasePEOAttribute4 | ATTRIBUTE4 | — | — |
| 13 | ClassCategoryBasePEOAttribute5 | ATTRIBUTE5 | — | — |
| 14 | ClassCategoryBasePEOAttribute6 | ATTRIBUTE6 | — | — |
| 15 | ClassCategoryBasePEOAttribute7 | ATTRIBUTE7 | — | — |
| 16 | ClassCategoryBasePEOAttribute8 | ATTRIBUTE8 | — | — |
| 17 | ClassCategoryBasePEOAttribute9 | ATTRIBUTE9 | — | — |
| 18 | ClassCategoryBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 19 | ClassCategoryBasePEOAutoaccountingFlag | AUTOACCOUNTING_FLAG | — | ✅ |
| 20 | ClassCategoryBasePEOClassCategoryId | CLASS_CATEGORY_ID | 🔑 | ✅ |
| 21 | ClassCategoryBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 22 | ClassCategoryBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 23 | ClassCategoryBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 24 | ClassCategoryBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 25 | ClassCategoryBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 26 | ClassCategoryBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 27 | ClassCategoryBasePEOMandatoryFlag | MANDATORY_FLAG | — | ✅ |
| 28 | ClassCategoryBasePEOObjectType | OBJECT_TYPE | — | ✅ |
| 29 | ClassCategoryBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 30 | ClassCategoryBasePEOPickOneCodeOnlyFlag | PICK_ONE_CODE_ONLY_FLAG | — | ✅ |
| 31 | ClassCategoryBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 32 | ClassCategoryBasePEOTotal100PercentFlag | TOTAL_100_PERCENT_FLAG | — | ✅ |

### [[pjf_class_categories_tl|PJF_CLASS_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClassCategoryTransLangPEOClassCategory | CLASS_CATEGORY | — | ✅ |
| 2 | ClassCategoryTransLangPEOClassCategoryId | CLASS_CATEGORY_ID | — | ✅ |
| 3 | ClassCategoryTransLangPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | ClassCategoryTransLangPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | ClassCategoryTransLangPEODescription | DESCRIPTION | — | ✅ |
| 6 | ClassCategoryTransLangPEOLanguage | LANGUAGE | — | ✅ |
| 7 | ClassCategoryTransLangPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ClassCategoryTransLangPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | ClassCategoryTransLangPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ClassCategoryTransLangPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ClassCategoryTransLangPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
