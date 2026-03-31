---
id: DOC-OTHER-PVO-InvTxnSourceTypeExtractPVO
doc_type: system-doc
title: "InvTxnSourceTypeExtractPVO — PVO Cross-Module"
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
  - InvTxnSourceTypeExtractPVO
  - invtxnsourcetypeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvTxnSourceTypeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inv Txn Source Type Extract. Acessa as tabelas: INV_TXN_SOURCE_TYPES_B, INV_TXN_SOURCE_TYPES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.InvBiccExtractAM.InvTxnSourceTypeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 2 | 1 | 28 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[inv_txn_source_types_b|INV_TXN_SOURCE_TYPES_B]] — 17 atributos (1 PKs, 17 BICC)
- [[inv_txn_source_types_tl|INV_TXN_SOURCE_TYPES_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[inv_txn_source_types_b|INV_TXN_SOURCE_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvTxnSourceTypeBPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | InvTxnSourceTypeBPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | InvTxnSourceTypeBPEODescriptiveFlexContextCode | DESCRIPTIVE_FLEX_CONTEXT_CODE | — | ✅ |
| 4 | InvTxnSourceTypeBPEOEndDate | END_DATE | — | ✅ |
| 5 | InvTxnSourceTypeBPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 6 | InvTxnSourceTypeBPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 7 | InvTxnSourceTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | InvTxnSourceTypeBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | InvTxnSourceTypeBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | InvTxnSourceTypeBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | InvTxnSourceTypeBPEORequestId | REQUEST_ID | — | ✅ |
| 12 | InvTxnSourceTypeBPEOStartDate | START_DATE | — | ✅ |
| 13 | InvTxnSourceTypeBPEOTransactionSource | TRANSACTION_SOURCE | — | ✅ |
| 14 | InvTxnSourceTypeBPEOTransactionSourceCategory | TRANSACTION_SOURCE_CATEGORY | — | ✅ |
| 15 | InvTxnSourceTypeBPEOUserDefinedFlag | USER_DEFINED_FLAG | — | ✅ |
| 16 | InvTxnSourceTypeBPEOValidatedFlag | VALIDATED_FLAG | — | ✅ |
| 17 | TransactionSourceTypeId | TRANSACTION_SOURCE_TYPE_ID | 🔑 | ✅ |

### [[inv_txn_source_types_tl|INV_TXN_SOURCE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvTxnSourceTypesTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | InvTxnSourceTypesTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | InvTxnSourceTypesTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | InvTxnSourceTypesTLPEOLanguage | LANGUAGE | — | ✅ |
| 5 | InvTxnSourceTypesTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | InvTxnSourceTypesTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | InvTxnSourceTypesTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | InvTxnSourceTypesTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | InvTxnSourceTypesTLPEOSourceLang | SOURCE_LANG | — | ✅ |
| 10 | InvTxnSourceTypesTLPEOTransactionSourceTypeId | TRANSACTION_SOURCE_TYPE_ID | — | ✅ |
| 11 | InvTxnSourceTypesTLPEOTransactionSourceTypeName | TRANSACTION_SOURCE_TYPE_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
