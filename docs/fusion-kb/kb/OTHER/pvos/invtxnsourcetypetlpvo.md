---
id: DOC-OTHER-PVO-InvTxnSourceTypeTLPVO
doc_type: system-doc
title: "InvTxnSourceTypeTLPVO — PVO Cross-Module"
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
  - InvTxnSourceTypeTLPVO
  - invtxnsourcetypetlpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvTxnSourceTypeTLPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inv Txn Source Type TL. Acessa as tabelas: INV_TXN_SOURCE_TYPES_TL.

**Caminho:** `FscmTopModelAM.InventoryAM.InvTxnSourceTypeTLPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 9 | 82% |

---

## 🔗 Tabelas Relacionadas

- [[inv_txn_source_types_tl|INV_TXN_SOURCE_TYPES_TL]] — 11 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[inv_txn_source_types_tl|INV_TXN_SOURCE_TYPES_TL]]

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
| 10 | TransactionSourceTypeId | TRANSACTION_SOURCE_TYPE_ID | 🔑 | ✅ |
| 11 | TransactionSourceTypeName | TRANSACTION_SOURCE_TYPE_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
