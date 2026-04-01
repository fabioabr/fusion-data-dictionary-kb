---
id: DOC-OTHER-PVO-KeywordViewPVO
doc_type: system-doc
title: "KeywordViewPVO — PVO Cross-Module"
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
  - KeywordViewPVO
  - keywordviewpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# KeywordViewPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Keyword View. Acessa as tabelas: GMS_KEYWORDS_VL.

**Caminho:** `FscmTopModelAM.GmsSetupAM.KeywordViewPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_keywords_vl|GMS_KEYWORDS_VL]] — 11 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[gms_keywords_vl|GMS_KEYWORDS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | KeywordId | KEYWORD_ID | 🔑 | ✅ |
| 2 | KeywordPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | KeywordPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | KeywordPEODescription | DESCRIPTION | — | ✅ |
| 5 | KeywordPEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 6 | KeywordPEOKeywordName | KEYWORD_NAME | — | ✅ |
| 7 | KeywordPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | KeywordPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | KeywordPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | KeywordPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | KeywordPEOStartDateActive | START_DATE_ACTIVE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
