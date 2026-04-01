---
id: DOC-OTHER-PVO-ExpenditureCategoryExtractPVO
doc_type: system-doc
title: "ExpenditureCategoryExtractPVO — PVO Cross-Module"
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
  - ExpenditureCategoryExtractPVO
  - expenditurecategoryextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpenditureCategoryExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Expenditure Category Extract. Acessa as tabelas: PJF_EXP_CATEGORIES_B, PJF_EXP_CATEGORIES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ExpenditureCategoryExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 36 | 2 | 1 | 36 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_exp_categories_b|PJF_EXP_CATEGORIES_B]] — 25 atributos (1 PKs, 25 BICC)
- [[pjf_exp_categories_tl|PJF_EXP_CATEGORIES_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[pjf_exp_categories_b|PJF_EXP_CATEGORIES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureCategoryBasePEOAttribute1 | ATTRIBUTE1 | — | ✅ |
| 2 | ExpenditureCategoryBasePEOAttribute10 | ATTRIBUTE10 | — | ✅ |
| 3 | ExpenditureCategoryBasePEOAttribute11 | ATTRIBUTE11 | — | ✅ |
| 4 | ExpenditureCategoryBasePEOAttribute12 | ATTRIBUTE12 | — | ✅ |
| 5 | ExpenditureCategoryBasePEOAttribute13 | ATTRIBUTE13 | — | ✅ |
| 6 | ExpenditureCategoryBasePEOAttribute14 | ATTRIBUTE14 | — | ✅ |
| 7 | ExpenditureCategoryBasePEOAttribute15 | ATTRIBUTE15 | — | ✅ |
| 8 | ExpenditureCategoryBasePEOAttribute2 | ATTRIBUTE2 | — | ✅ |
| 9 | ExpenditureCategoryBasePEOAttribute3 | ATTRIBUTE3 | — | ✅ |
| 10 | ExpenditureCategoryBasePEOAttribute4 | ATTRIBUTE4 | — | ✅ |
| 11 | ExpenditureCategoryBasePEOAttribute5 | ATTRIBUTE5 | — | ✅ |
| 12 | ExpenditureCategoryBasePEOAttribute6 | ATTRIBUTE6 | — | ✅ |
| 13 | ExpenditureCategoryBasePEOAttribute7 | ATTRIBUTE7 | — | ✅ |
| 14 | ExpenditureCategoryBasePEOAttribute8 | ATTRIBUTE8 | — | ✅ |
| 15 | ExpenditureCategoryBasePEOAttribute9 | ATTRIBUTE9 | — | ✅ |
| 16 | ExpenditureCategoryBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 17 | ExpenditureCategoryBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 18 | ExpenditureCategoryBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 19 | ExpenditureCategoryBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 20 | ExpenditureCategoryBasePEOExpenditureCategoryId | EXPENDITURE_CATEGORY_ID | 🔑 | ✅ |
| 21 | ExpenditureCategoryBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | ExpenditureCategoryBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 23 | ExpenditureCategoryBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | ExpenditureCategoryBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 25 | ExpenditureCategoryBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |

### [[pjf_exp_categories_tl|PJF_EXP_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureCategoryTLLangPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ExpenditureCategoryTLLangPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ExpenditureCategoryTLLangPEODescription | DESCRIPTION | — | ✅ |
| 4 | ExpenditureCategoryTLLangPEOExpenditureCategoryId | EXPENDITURE_CATEGORY_ID | — | ✅ |
| 5 | ExpenditureCategoryTLLangPEOLanguage | LANGUAGE | — | ✅ |
| 6 | ExpenditureCategoryTLLangPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ExpenditureCategoryTLLangPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | ExpenditureCategoryTLLangPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ExpenditureCategoryTLLangPEOName | EXPENDITURE_CATEGORY_NAME | — | ✅ |
| 10 | ExpenditureCategoryTLLangPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ExpenditureCategoryTLLangPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
