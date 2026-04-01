---
id: DOC-OTHER-PVO-AwardTermPVO
doc_type: system-doc
title: "AwardTermPVO — PVO Cross-Module"
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
  - AwardTermPVO
  - awardtermpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardTermPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Term. Acessa as tabelas: GMS_AWARD_TERMS_B, GMS_AWARD_TERMS_TL, GMS_TERMS_VL (+1).

**Caminho:** `FscmTopModelAM.GmsAwardAM.AwardTermPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 4 | 3 | 13 | 57% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_terms_b|GMS_AWARD_TERMS_B]] — 12 atributos (1 PKs, 4 BICC)
- [[gms_award_terms_tl|GMS_AWARD_TERMS_TL]] — 3 atributos (1 BICC)
- [[gms_terms_vl|GMS_TERMS_VL]] — 5 atributos (1 PKs, 5 BICC)
- [[gms_term_categories_vl|GMS_TERM_CATEGORIES_VL]] — 3 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[gms_award_terms_b|GMS_AWARD_TERMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardTermPEOAwardId | AWARD_ID | — | — |
| 2 | AwardTermPEOCreatedBy | CREATED_BY | — | — |
| 3 | AwardTermPEOCreationDate | CREATION_DATE | — | — |
| 4 | AwardTermPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | AwardTermPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | AwardTermPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | AwardTermPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | AwardTermPEOTermCategoryId | TERM_CATEGORY_ID | — | — |
| 9 | AwardTermPEOTermId | TERM_ID | — | — |
| 10 | AwardTermPEOTermOperand | TERM_OPERAND | — | ✅ |
| 11 | AwardTermPEOTermValue | TERM_VALUE | — | ✅ |
| 12 | Id | ID | 🔑 | ✅ |

### [[gms_award_terms_tl|GMS_AWARD_TERMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardTermTranslationPEODescription | DESCRIPTION | — | ✅ |
| 2 | AwardTermTranslationPEOId | ID | — | — |
| 3 | AwardTermTranslationPEOLanguage | LANGUAGE | — | — |

### [[gms_terms_vl|GMS_TERMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TermPEODescription | DESCRIPTION | — | ✅ |
| 2 | TermPEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 3 | TermPEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 4 | TermPEOTermId | TERM_ID | 🔑 | ✅ |
| 5 | TermPEOTermName | TERM_NAME | — | ✅ |

### [[gms_term_categories_vl|GMS_TERM_CATEGORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TermCategoryPEODescription | DESCRIPTION | — | ✅ |
| 2 | TermCategoryPEOTermCategoryId | TERM_CATEGORY_ID | 🔑 | ✅ |
| 3 | TermCategoryPEOTermCategoryName | TERM_CATEGORY_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
