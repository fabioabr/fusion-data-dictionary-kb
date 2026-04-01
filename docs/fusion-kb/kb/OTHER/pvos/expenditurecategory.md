---
id: DOC-OTHER-PVO-ExpenditureCategory
doc_type: system-doc
title: "ExpenditureCategory — PVO Cross-Module"
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
  - ExpenditureCategory
  - expenditurecategory
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpenditureCategory

## 📌 Visão Geral

View Object para extração BICC de dados de Expenditure Category. Acessa as tabelas: PJF_EXP_CATEGORIES_B.

**Caminho:** `FscmTopModelAM.PjfSetupTransactionsAM.ExpenditureCategory`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 1 | 7 | 70% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_exp_categories_b|PJF_EXP_CATEGORIES_B]] — 10 atributos (1 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[pjf_exp_categories_b|PJF_EXP_CATEGORIES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureCategoryBaseAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | ExpenditureCategoryBaseCreatedBy | CREATED_BY | — | ✅ |
| 3 | ExpenditureCategoryBaseCreationDate | CREATION_DATE | — | ✅ |
| 4 | ExpenditureCategoryBaseEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 5 | ExpenditureCategoryBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ExpenditureCategoryBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ExpenditureCategoryBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ExpenditureCategoryBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ExpenditureCategoryBaseStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 10 | ExpenditureCategoryId | EXPENDITURE_CATEGORY_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
