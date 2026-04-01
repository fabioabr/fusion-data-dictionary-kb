---
id: DOC-OTHER-PVO-KeywordExtractPVO
doc_type: system-doc
title: "KeywordExtractPVO — PVO Cross-Module"
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
  - KeywordExtractPVO
  - keywordextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# KeywordExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Keyword Extract. Acessa as tabelas: GMS_KEYWORDS_B.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.KeywordExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 1 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_keywords_b|GMS_KEYWORDS_B]] — 9 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[gms_keywords_b|GMS_KEYWORDS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | KeywordBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | KeywordBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | KeywordBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 4 | KeywordBasePEOKeywordId | KEYWORD_ID | 🔑 | ✅ |
| 5 | KeywordBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | KeywordBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | KeywordBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | KeywordBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | KeywordBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
