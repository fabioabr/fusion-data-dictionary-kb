---
id: DOC-OTHER-PVO-TransactionSourceTranslation
doc_type: system-doc
title: "TransactionSourceTranslation — PVO Cross-Module"
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
  - TransactionSourceTranslation
  - transactionsourcetranslation
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionSourceTranslation

## 📌 Visão Geral

View Object para extração BICC de dados de Transaction Source Translation. Acessa as tabelas: PJF_TXN_SOURCES_TL.

**Caminho:** `FscmTopModelAM.PjfSetupTransactionsAM.TransactionSourceTranslation`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 9 | 82% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_txn_sources_tl|PJF_TXN_SOURCES_TL]] — 11 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[pjf_txn_sources_tl|PJF_TXN_SOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | Language | LANGUAGE | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | SourceLang | SOURCE_LANG | — | ✅ |
| 10 | TransactionSourceId | TRANSACTION_SOURCE_ID | 🔑 | ✅ |
| 11 | UserTransactionSource | USER_TRANSACTION_SOURCE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
