---
id: DOC-OTHER-PVO-CostBookTLPVO
doc_type: system-doc
title: "CostBookTLPVO — PVO Cross-Module"
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
  - CostBookTLPVO
  - costbooktlpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CostBookTLPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cost Book TL. Acessa as tabelas: CST_COST_BOOKS_TL.

**Caminho:** `FscmTopModelAM.CostBookAM.CostBookTLPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 8 | 80% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_books_tl|CST_COST_BOOKS_TL]] — 10 atributos (2 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[cst_cost_books_tl|CST_COST_BOOKS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostBookDesc | COST_BOOK_DESC | — | ✅ |
| 2 | CostBookId | COST_BOOK_ID | 🔑 | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | Language | LANGUAGE | 🔑 | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
