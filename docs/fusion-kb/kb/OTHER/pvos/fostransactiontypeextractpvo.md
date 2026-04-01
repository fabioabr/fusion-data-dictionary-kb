---
id: DOC-OTHER-PVO-FosTransactionTypeExtractPVO
doc_type: system-doc
title: "FosTransactionTypeExtractPVO — PVO Cross-Module"
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
  - FosTransactionTypeExtractPVO
  - fostransactiontypeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FosTransactionTypeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fos Transaction Type Extract. Acessa as tabelas: FOS_TRANSACTION_TYPE_B, FOS_TRANSACTION_TYPE_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.FosBiccExtractAM.FosTransactionTypeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 2 | 1 | 26 | 93% |

---

## 🔗 Tabelas Relacionadas

- [[fos_transaction_type_b|FOS_TRANSACTION_TYPE_B]] — 14 atributos (1 PKs, 14 BICC)
- [[fos_transaction_type_tl|FOS_TRANSACTION_TYPE_TL]] — 14 atributos (12 BICC)

---

## ⚙️ Atributos

### [[fos_transaction_type_b|FOS_TRANSACTION_TYPE_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionTypeBPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | TransactionTypeBPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | TransactionTypeBPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 4 | TransactionTypeBPEOFlowType | FLOW_TYPE | — | ✅ |
| 5 | TransactionTypeBPEOForwardTransactionType | FORWARD_TRANSACTION_TYPE | — | ✅ |
| 6 | TransactionTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | TransactionTypeBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | TransactionTypeBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | TransactionTypeBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | TransactionTypeBPEOReturnTransactionType | RETURN_TRANSACTION_TYPE | — | ✅ |
| 11 | TransactionTypeBPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 12 | TransactionTypeBPEOTaskType | TASK_TYPE | — | ✅ |
| 13 | TransactionTypeBPEOTransactionType | TRANSACTION_TYPE | — | ✅ |
| 14 | TransactionTypeBPEOTransactionTypeId | TRANSACTION_TYPE_ID | 🔑 | ✅ |

### [[fos_transaction_type_tl|FOS_TRANSACTION_TYPE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionTypeTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | TransactionTypeTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | TransactionTypeTLPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 4 | TransactionTypeTLPEOForwardTransactionName | FORWARD_TRANSACTION_NAME | — | ✅ |
| 5 | TransactionTypeTLPEOLanguage | LANGUAGE | — | — |
| 6 | TransactionTypeTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | TransactionTypeTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | TransactionTypeTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | TransactionTypeTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | TransactionTypeTLPEOReturnTransactionName | RETURN_TRANSACTION_NAME | — | ✅ |
| 11 | TransactionTypeTLPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 12 | TransactionTypeTLPEOSourceLang | SOURCE_LANG | — | — |
| 13 | TransactionTypeTLPEOTransactionName | TRANSACTION_NAME | — | ✅ |
| 14 | TransactionTypeTLPEOTransactionTypeId | TRANSACTION_TYPE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
