---
id: DOC-OTHER-PVO-ExpenditureCategoryTranslationExtractPVO
doc_type: system-doc
title: "ExpenditureCategoryTranslationExtractPVO — PVO Cross-Module"
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
  - ExpenditureCategoryTranslationExtractPVO
  - expenditurecategorytranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpenditureCategoryTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Expenditure Category Translation Extract. Acessa as tabelas: PJF_EXP_CATEGORIES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ExpenditureCategoryTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_exp_categories_tl|PJF_EXP_CATEGORIES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[pjf_exp_categories_tl|PJF_EXP_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureCategoryTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ExpenditureCategoryTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ExpenditureCategoryTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | ExpenditureCategoryTLPEOExpenditureCategoryId | EXPENDITURE_CATEGORY_ID | 🔑 | ✅ |
| 5 | ExpenditureCategoryTLPEOExpenditureCategoryName | EXPENDITURE_CATEGORY_NAME | — | ✅ |
| 6 | ExpenditureCategoryTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | ExpenditureCategoryTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ExpenditureCategoryTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | ExpenditureCategoryTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ExpenditureCategoryTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ExpenditureCategoryTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
