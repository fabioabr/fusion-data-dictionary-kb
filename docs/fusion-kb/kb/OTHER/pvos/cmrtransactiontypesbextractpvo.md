---
id: DOC-OTHER-PVO-CmrTransactionTypesBExtractPVO
doc_type: system-doc
title: "CmrTransactionTypesBExtractPVO — PVO Cross-Module"
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
  - CmrTransactionTypesBExtractPVO
  - cmrtransactiontypesbextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrTransactionTypesBExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cmr Transaction Types BExtract. Acessa as tabelas: CMR_TRANSACTION_TYPES_B.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CmrBiccExtractAM.CmrTransactionTypesBExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_transaction_types_b|CMR_TRANSACTION_TYPES_B]] — 15 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[cmr_transaction_types_b|CMR_TRANSACTION_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrTransactionTypesBPEOActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | CmrTransactionTypesBPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | CmrTransactionTypesBPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | CmrTransactionTypesBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | CmrTransactionTypesBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | CmrTransactionTypesBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | CmrTransactionTypesBPEOProductCode | PRODUCT_CODE | — | ✅ |
| 8 | CmrTransactionTypesBPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 9 | CmrTransactionTypesBPEOTransactionGroupName | TRANSACTION_GROUP_NAME | — | ✅ |
| 10 | CmrTransactionTypesBPEOTransactionTypeCode | TRANSACTION_TYPE_CODE | — | ✅ |
| 11 | CmrTransactionTypesBPEOTransactionTypeId | TRANSACTION_TYPE_ID | 🔑 | ✅ |
| 12 | CmrTransactionTypesBPEOTxnDateInLeTzFlag | TXN_DATE_IN_LE_TZ_FLAG | — | ✅ |
| 13 | CmrTransactionTypesBPEOXccSourceAction | XCC_SOURCE_ACTION | — | ✅ |
| 14 | CmrTransactionTypesBPEOXccTransactionSubtypeCode | XCC_TRANSACTION_SUBTYPE_CODE | — | ✅ |
| 15 | CmrTransactionTypesBPEOXccTransactionType | XCC_TRANSACTION_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
