---
id: DOC-OTHER-PVO-KeywordTranslationPVO
doc_type: system-doc
title: "KeywordTranslationPVO — PVO Cross-Module"
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
  - KeywordTranslationPVO
  - keywordtranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# KeywordTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Keyword Translation. Acessa as tabelas: GMS_KEYWORDS_TL.

**Caminho:** `FscmTopModelAM.GmsSetupAM.KeywordTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_keywords_tl|GMS_KEYWORDS_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[gms_keywords_tl|GMS_KEYWORDS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | KeywordId | KEYWORD_ID | 🔑 | ✅ |
| 2 | KeywordTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | KeywordTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | KeywordTranslationPEODescription | DESCRIPTION | — | ✅ |
| 5 | KeywordTranslationPEOKeywordName | KEYWORD_NAME | — | ✅ |
| 6 | KeywordTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | KeywordTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | KeywordTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | KeywordTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | KeywordTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |
| 11 | Language | LANGUAGE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
