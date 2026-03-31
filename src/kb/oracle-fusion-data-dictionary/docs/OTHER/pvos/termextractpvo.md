---
id: DOC-OTHER-PVO-TermExtractPVO
doc_type: system-doc
title: "TermExtractPVO — PVO Cross-Module"
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
  - TermExtractPVO
  - termextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TermExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Term Extract. Acessa as tabelas: GMS_TERMS_B, GMS_TERMS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.TermExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 2 | 1 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_terms_b|GMS_TERMS_B]] — 10 atributos (1 PKs, 10 BICC)
- [[gms_terms_tl|GMS_TERMS_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[gms_terms_b|GMS_TERMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TermBaseCreatedBy | CREATED_BY | — | ✅ |
| 2 | TermBaseCreationDate | CREATION_DATE | — | ✅ |
| 3 | TermBaseEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 4 | TermBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | TermBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | TermBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | TermBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | TermBaseStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 9 | TermBaseTermCategoryId | TERM_CATEGORY_ID | — | ✅ |
| 10 | TermBaseTermId | TERM_ID | 🔑 | ✅ |

### [[gms_terms_tl|GMS_TERMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TermTransLangCreatedBy | CREATED_BY | — | ✅ |
| 2 | TermTransLangCreationDate | CREATION_DATE | — | ✅ |
| 3 | TermTransLangDescription | DESCRIPTION | — | ✅ |
| 4 | TermTransLangLanguage | LANGUAGE | — | ✅ |
| 5 | TermTransLangLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | TermTransLangLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | TermTransLangLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | TermTransLangObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | TermTransLangSourceLang | SOURCE_LANG | — | ✅ |
| 10 | TermTransLangTermId | TERM_ID | — | ✅ |
| 11 | TermTransLangTermName | TERM_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
