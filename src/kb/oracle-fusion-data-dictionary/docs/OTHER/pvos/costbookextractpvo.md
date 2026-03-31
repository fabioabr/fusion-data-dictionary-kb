---
id: DOC-OTHER-PVO-CostBookExtractPVO
doc_type: system-doc
title: "CostBookExtractPVO — PVO Cross-Module"
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
  - CostBookExtractPVO
  - costbookextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CostBookExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cost Book Extract. Acessa as tabelas: CST_COST_BOOKS_B, CST_COST_BOOKS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CostBookExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 59 | 2 | 1 | 57 | 97% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_books_b|CST_COST_BOOKS_B]] — 49 atributos (1 PKs, 49 BICC)
- [[cst_cost_books_tl|CST_COST_BOOKS_TL]] — 10 atributos (8 BICC)

---

## ⚙️ Atributos

### [[cst_cost_books_b|CST_COST_BOOKS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostBookBPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 2 | CostBookBPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 3 | CostBookBPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 4 | CostBookBPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 5 | CostBookBPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 6 | CostBookBPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 7 | CostBookBPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 8 | CostBookBPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 9 | CostBookBPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 10 | CostBookBPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 11 | CostBookBPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 12 | CostBookBPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 13 | CostBookBPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 14 | CostBookBPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 15 | CostBookBPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 16 | CostBookBPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 17 | CostBookBPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 18 | CostBookBPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 19 | CostBookBPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 20 | CostBookBPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 21 | CostBookBPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 22 | CostBookBPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 23 | CostBookBPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 24 | CostBookBPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 25 | CostBookBPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 26 | CostBookBPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 27 | CostBookBPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 28 | CostBookBPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 29 | CostBookBPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 30 | CostBookBPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 31 | CostBookBPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 32 | CostBookBPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 33 | CostBookBPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 34 | CostBookBPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 35 | CostBookBPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 36 | CostBookBPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 37 | CostBookBPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 38 | CostBookBPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 39 | CostBookBPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 40 | CostBookBPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 41 | CostBookBPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 42 | CostBookBPEOCostBookCode | COST_BOOK_CODE | — | ✅ |
| 43 | CostBookBPEOCostBookId | COST_BOOK_ID | 🔑 | ✅ |
| 44 | CostBookBPEOCreatedBy | CREATED_BY | — | ✅ |
| 45 | CostBookBPEOCreationDate | CREATION_DATE | — | ✅ |
| 46 | CostBookBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 47 | CostBookBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 48 | CostBookBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 49 | CostBookBPEOPeriodicAverageFlag | PERIODIC_AVERAGE_FLAG | — | ✅ |

### [[cst_cost_books_tl|CST_COST_BOOKS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostBookTLPEOCostBookDesc | COST_BOOK_DESC | — | ✅ |
| 2 | CostBookTLPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 3 | CostBookTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | CostBookTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | CostBookTLPEOLanguage | LANGUAGE | — | — |
| 6 | CostBookTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | CostBookTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | CostBookTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | CostBookTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | CostBookTLPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
