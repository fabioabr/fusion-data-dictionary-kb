---
id: DOC-OTHER-PVO-TermsViewPVO
doc_type: system-doc
title: "TermsViewPVO — PVO Cross-Module"
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
  - TermsViewPVO
  - termsviewpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TermsViewPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Terms View. Acessa as tabelas: GMS_TERMS_VL, GMS_TERM_CATEGORIES_VL.

**Caminho:** `FscmTopModelAM.GmsSetupAM.TermsViewPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 2 | 1 | 8 | 53% |

---

## 🔗 Tabelas Relacionadas

- [[gms_terms_vl|GMS_TERMS_VL]] — 12 atributos (1 PKs, 6 BICC)
- [[gms_term_categories_vl|GMS_TERM_CATEGORIES_VL]] — 3 atributos (2 BICC)

---

## ⚙️ Atributos

### [[gms_terms_vl|GMS_TERMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TermId | TERM_ID | 🔑 | ✅ |
| 2 | TermPEOCreatedBy | CREATED_BY | — | — |
| 3 | TermPEOCreationDate | CREATION_DATE | — | — |
| 4 | TermPEODescription | DESCRIPTION | — | ✅ |
| 5 | TermPEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 6 | TermPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | TermPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | TermPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | TermPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | TermPEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 11 | TermPEOTermCategoryId | TERM_CATEGORY_ID | — | — |
| 12 | TermPEOTermName | TERM_NAME | — | ✅ |

### [[gms_term_categories_vl|GMS_TERM_CATEGORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TermCategoryPEODescription | DESCRIPTION | — | ✅ |
| 2 | TermCategoryPEOTermCategoryId | TERM_CATEGORY_ID | — | — |
| 3 | TermCategoryPEOTermCategoryName | TERM_CATEGORY_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
