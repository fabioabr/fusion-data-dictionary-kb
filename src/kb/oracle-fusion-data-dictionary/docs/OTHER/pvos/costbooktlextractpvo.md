---
id: DOC-OTHER-PVO-CostBookTLExtractPVO
doc_type: system-doc
title: "CostBookTLExtractPVO — PVO Cross-Module"
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
  - CostBookTLExtractPVO
  - costbooktlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CostBookTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cost Book TLExtract. Acessa as tabelas: CST_COST_BOOKS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CostBookTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_books_tl|CST_COST_BOOKS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[cst_cost_books_tl|CST_COST_BOOKS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostBookTLPEOCostBookDesc | COST_BOOK_DESC | — | ✅ |
| 2 | CostBookTLPEOCostBookId | COST_BOOK_ID | 🔑 | ✅ |
| 3 | CostBookTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | CostBookTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | CostBookTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | CostBookTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | CostBookTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | CostBookTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | CostBookTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | CostBookTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
