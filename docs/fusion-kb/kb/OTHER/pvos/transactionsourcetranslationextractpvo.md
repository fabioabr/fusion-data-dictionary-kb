---
id: DOC-OTHER-PVO-TransactionSourceTranslationExtractPVO
doc_type: system-doc
title: "TransactionSourceTranslationExtractPVO — PVO Cross-Module"
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
  - TransactionSourceTranslationExtractPVO
  - transactionsourcetranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionSourceTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transaction Source Translation Extract. Acessa as tabelas: PJF_TXN_SOURCES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.TransactionSourceTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_txn_sources_tl|PJF_TXN_SOURCES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[pjf_txn_sources_tl|PJF_TXN_SOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionSourceTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | TransactionSourceTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | TransactionSourceTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | TransactionSourceTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | TransactionSourceTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | TransactionSourceTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | TransactionSourceTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | TransactionSourceTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | TransactionSourceTLPEOSourceLang | SOURCE_LANG | — | ✅ |
| 10 | TransactionSourceTLPEOTransactionSourceId | TRANSACTION_SOURCE_ID | 🔑 | ✅ |
| 11 | TransactionSourceTLPEOUserTransactionSource | USER_TRANSACTION_SOURCE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
