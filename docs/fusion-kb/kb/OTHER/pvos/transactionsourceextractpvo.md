---
id: DOC-OTHER-PVO-TransactionSourceExtractPVO
doc_type: system-doc
title: "TransactionSourceExtractPVO — PVO Cross-Module"
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
  - TransactionSourceExtractPVO
  - transactionsourceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionSourceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transaction Source Extract. Acessa as tabelas: PJF_TXN_SOURCES_B, PJF_TXN_SOURCES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.TransactionSourceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 40 | 2 | 1 | 24 | 60% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_txn_sources_b|PJF_TXN_SOURCES_B]] — 29 atributos (1 PKs, 13 BICC)
- [[pjf_txn_sources_tl|PJF_TXN_SOURCES_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[pjf_txn_sources_b|PJF_TXN_SOURCES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionSourceBasePEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | TransactionSourceBasePEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | TransactionSourceBasePEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | TransactionSourceBasePEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | TransactionSourceBasePEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | TransactionSourceBasePEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | TransactionSourceBasePEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | TransactionSourceBasePEOAttribute2 | ATTRIBUTE2 | — | — |
| 9 | TransactionSourceBasePEOAttribute3 | ATTRIBUTE3 | — | — |
| 10 | TransactionSourceBasePEOAttribute4 | ATTRIBUTE4 | — | — |
| 11 | TransactionSourceBasePEOAttribute5 | ATTRIBUTE5 | — | — |
| 12 | TransactionSourceBasePEOAttribute6 | ATTRIBUTE6 | — | — |
| 13 | TransactionSourceBasePEOAttribute7 | ATTRIBUTE7 | — | — |
| 14 | TransactionSourceBasePEOAttribute8 | ATTRIBUTE8 | — | — |
| 15 | TransactionSourceBasePEOAttribute9 | ATTRIBUTE9 | — | — |
| 16 | TransactionSourceBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | TransactionSourceBasePEOBatchSize | BATCH_SIZE | — | ✅ |
| 18 | TransactionSourceBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 19 | TransactionSourceBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 20 | TransactionSourceBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | TransactionSourceBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 22 | TransactionSourceBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 23 | TransactionSourceBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 24 | TransactionSourceBasePEOPostProcessingExtension | POST_PROCESSING_EXTENSION | — | ✅ |
| 25 | TransactionSourceBasePEOPreProcessingExtension | PRE_PROCESSING_EXTENSION | — | ✅ |
| 26 | TransactionSourceBasePEOPredefinedFlag | PREDEFINED_FLAG | — | ✅ |
| 27 | TransactionSourceBasePEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 28 | TransactionSourceBasePEOTransactionSource | TRANSACTION_SOURCE | — | ✅ |
| 29 | TransactionSourceBasePEOTransactionSourceId | TRANSACTION_SOURCE_ID | 🔑 | ✅ |

### [[pjf_txn_sources_tl|PJF_TXN_SOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionSourceTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | TransactionSourceTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | TransactionSourceTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | TransactionSourceTLPEOLanguage | LANGUAGE | — | ✅ |
| 5 | TransactionSourceTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | TransactionSourceTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | TransactionSourceTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | TransactionSourceTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | TransactionSourceTLPEOSourceLang | SOURCE_LANG | — | ✅ |
| 10 | TransactionSourceTLPEOTransactionSourceId | TRANSACTION_SOURCE_ID | — | ✅ |
| 11 | TransactionSourceTLPEOUserTransactionSource | USER_TRANSACTION_SOURCE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
