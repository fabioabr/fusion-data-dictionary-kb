---
id: DOC-OTHER-PVO-TermTranslationExtractPVO
doc_type: system-doc
title: "TermTranslationExtractPVO — PVO Cross-Module"
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
  - TermTranslationExtractPVO
  - termtranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TermTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Term Translation Extract. Acessa as tabelas: GMS_TERMS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.TermTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_terms_tl|GMS_TERMS_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[gms_terms_tl|GMS_TERMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TermTranslationCreatedBy | CREATED_BY | — | ✅ |
| 2 | TermTranslationCreationDate | CREATION_DATE | — | ✅ |
| 3 | TermTranslationDescription | DESCRIPTION | — | ✅ |
| 4 | TermTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | TermTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | TermTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | TermTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | TermTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | TermTranslationSourceLang | SOURCE_LANG | — | ✅ |
| 10 | TermTranslationTermId | TERM_ID | 🔑 | ✅ |
| 11 | TermTranslationTermName | TERM_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
