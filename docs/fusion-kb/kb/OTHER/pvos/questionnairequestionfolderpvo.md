---
id: DOC-OTHER-PVO-QuestionnaireQuestionFolderPVO
doc_type: system-doc
title: "QuestionnaireQuestionFolderPVO — PVO Cross-Module"
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
  - QuestionnaireQuestionFolderPVO
  - questionnairequestionfolderpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QuestionnaireQuestionFolderPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Questionnaire Question Folder. Acessa as tabelas: HRQ_CATEGORIES_B, HRQ_CATEGORIES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.QuestionnaireAM.QuestionnaireQuestionFolderPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 2 | 5 | 8 | 89% |

---

## 🔗 Tabelas Relacionadas

- [[hrq_categories_b|HRQ_CATEGORIES_B]] — 4 atributos (2 PKs, 3 BICC)
- [[hrq_categories_tl|HRQ_CATEGORIES_TL]] — 5 atributos (3 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[hrq_categories_b|HRQ_CATEGORIES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | CategoryBPEOCategoryId | CATEGORY_ID | 🔑 | ✅ |
| 3 | CategoryBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | CategoryBPEOSubscriberId | SUBSCRIBER_ID | — | — |

### [[hrq_categories_tl|HRQ_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | CategoryTranslationPEOCategoryId | CATEGORY_ID | 🔑 | ✅ |
| 3 | CategoryTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 4 | CategoryTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | CategoryTranslationPEOName | NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
