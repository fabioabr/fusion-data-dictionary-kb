---
id: DOC-OTHER-PVO-InvTxnTypePVO
doc_type: system-doc
title: "InvTxnTypePVO — PVO Cross-Module"
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
  - InvTxnTypePVO
  - invtxntypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvTxnTypePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inv Txn Type. Acessa as tabelas: INV_TRANSACTION_TYPES_B, INV_TRANSACTION_TYPES_TL.

**Caminho:** `FscmTopModelAM.InventoryAM.InvTxnTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 2 | 2 | 12 | 43% |

---

## 🔗 Tabelas Relacionadas

- [[inv_transaction_types_b|INV_TRANSACTION_TYPES_B]] — 17 atributos (1 PKs, 9 BICC)
- [[inv_transaction_types_tl|INV_TRANSACTION_TYPES_TL]] — 11 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[inv_transaction_types_b|INV_TRANSACTION_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvTransactionTypeBPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | InvTransactionTypeBPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | InvTransactionTypeBPEOEndDate | END_DATE | — | — |
| 4 | InvTransactionTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | InvTransactionTypeBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | InvTransactionTypeBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | InvTransactionTypeBPEOLocationRequiredFlag | LOCATION_REQUIRED_FLAG | — | ✅ |
| 8 | InvTransactionTypeBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | InvTransactionTypeBPEOShortageMsgBackgroundFlag | SHORTAGE_MSG_BACKGROUND_FLAG | — | — |
| 10 | InvTransactionTypeBPEOShortageMsgOnlineFlag | SHORTAGE_MSG_ONLINE_FLAG | — | — |
| 11 | InvTransactionTypeBPEOStartDate | START_DATE | — | — |
| 12 | InvTransactionTypeBPEOStatusControlFlag | STATUS_CONTROL_FLAG | — | ✅ |
| 13 | InvTransactionTypeBPEOTransactionActionId | TRANSACTION_ACTION_ID | — | ✅ |
| 14 | InvTransactionTypeBPEOTransactionSourceTypeId | TRANSACTION_SOURCE_TYPE_ID | — | ✅ |
| 15 | InvTransactionTypeBPEOTypeClass | TYPE_CLASS | — | — |
| 16 | InvTransactionTypeBPEOUserDefinedFlag | USER_DEFINED_FLAG | — | — |
| 17 | TransactionTypeId | TRANSACTION_TYPE_ID | 🔑 | ✅ |

### [[inv_transaction_types_tl|INV_TRANSACTION_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvTransactionTypeTLPEOCreatedBy | CREATED_BY | — | — |
| 2 | InvTransactionTypeTLPEOCreationDate | CREATION_DATE | — | — |
| 3 | InvTransactionTypeTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | InvTransactionTypeTLPEOLanguage | LANGUAGE | — | — |
| 5 | InvTransactionTypeTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | InvTransactionTypeTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | InvTransactionTypeTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | InvTransactionTypeTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | InvTransactionTypeTLPEOSourceLang | SOURCE_LANG | — | — |
| 10 | InvTransactionTypeTLPEOTransactionTypeId | TRANSACTION_TYPE_ID | — | — |
| 11 | InvTransactionTypeTLPEOTransactionTypeName | TRANSACTION_TYPE_NAME | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
