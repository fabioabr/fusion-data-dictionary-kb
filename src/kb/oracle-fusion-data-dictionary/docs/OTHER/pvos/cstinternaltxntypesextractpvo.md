---
id: DOC-OTHER-PVO-CstInternalTxnTypesExtractPVO
doc_type: system-doc
title: "CstInternalTxnTypesExtractPVO — PVO Cross-Module"
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
  - CstInternalTxnTypesExtractPVO
  - cstinternaltxntypesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstInternalTxnTypesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Internal Txn Types Extract. Acessa as tabelas: CST_INTERNAL_TXN_TYPES_B, CST_INTERNAL_TXN_TYPES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstInternalTxnTypesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 2 | 2 | 18 | 75% |

---

## 🔗 Tabelas Relacionadas

- [[cst_internal_txn_types_b|CST_INTERNAL_TXN_TYPES_B]] — 12 atributos (2 PKs, 11 BICC)
- [[cst_internal_txn_types_tl|CST_INTERNAL_TXN_TYPES_TL]] — 12 atributos (7 BICC)

---

## ⚙️ Atributos

### [[cst_internal_txn_types_b|CST_INTERNAL_TXN_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstInternalTxnTypesBPEOBaseTxnActionId | BASE_TXN_ACTION_ID | — | ✅ |
| 2 | CstInternalTxnTypesBPEOBaseTxnSourceTypeId | BASE_TXN_SOURCE_TYPE_ID | 🔑 | ✅ |
| 3 | CstInternalTxnTypesBPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | 🔑 | ✅ |
| 4 | CstInternalTxnTypesBPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | CstInternalTxnTypesBPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | CstInternalTxnTypesBPEOEndDate | END_DATE | — | ✅ |
| 7 | CstInternalTxnTypesBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | CstInternalTxnTypesBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | CstInternalTxnTypesBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | CstInternalTxnTypesBPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 11 | CstInternalTxnTypesBPEOStartDate | START_DATE | — | ✅ |
| 12 | CstInternalTxnTypesBPEOUserDefinedFlag | USER_DEFINED_FLAG | — | ✅ |

### [[cst_internal_txn_types_tl|CST_INTERNAL_TXN_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstInternalTxnTypesTLPEOBaseTxnSourceTypeId | BASE_TXN_SOURCE_TYPE_ID | — | — |
| 2 | CstInternalTxnTypesTLPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | — |
| 3 | CstInternalTxnTypesTLPEOBaseTxnTypeName | BASE_TXN_TYPE_NAME | — | ✅ |
| 4 | CstInternalTxnTypesTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | CstInternalTxnTypesTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | CstInternalTxnTypesTLPEODescription | DESCRIPTION | — | ✅ |
| 7 | CstInternalTxnTypesTLPEOLanguage | LANGUAGE | — | — |
| 8 | CstInternalTxnTypesTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | CstInternalTxnTypesTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | CstInternalTxnTypesTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | CstInternalTxnTypesTLPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 12 | CstInternalTxnTypesTLPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
