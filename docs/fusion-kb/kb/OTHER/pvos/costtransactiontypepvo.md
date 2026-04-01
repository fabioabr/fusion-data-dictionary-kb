---
id: DOC-OTHER-PVO-CostTransactionTypePVO
doc_type: system-doc
title: "CostTransactionTypePVO — PVO Cross-Module"
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
  - CostTransactionTypePVO
  - costtransactiontypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CostTransactionTypePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cost Transaction Type. Acessa as tabelas: CST_ALL_TXN_TYPES_V.

**Caminho:** `FscmTopModelAM.CostTransactionTypeAM.CostTransactionTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 8 | 1 | 2 | 7 | 88% |

---

## 🔗 Tabelas Relacionadas

- [[cst_all_txn_types_v|CST_ALL_TXN_TYPES_V]] — 8 atributos (2 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[cst_all_txn_types_v|CST_ALL_TXN_TYPES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostTransactionTypeEOBaseTxnActionId | BASE_TXN_ACTION_ID | — | ✅ |
| 2 | CostTransactionTypeEOBaseTxnSourceTypeId | BASE_TXN_SOURCE_TYPE_ID | 🔑 | ✅ |
| 3 | CostTransactionTypeEOBaseTxnTypeId | BASE_TXN_TYPE_ID | 🔑 | ✅ |
| 4 | CostTransactionTypeEOBaseTxnTypeName | BASE_TXN_TYPE_NAME | — | ✅ |
| 5 | CostTransactionTypeEODescription | DESCRIPTION | — | ✅ |
| 6 | CostTransactionTypeEOEndDate | END_DATE | — | ✅ |
| 7 | CostTransactionTypeEOStartDate | START_DATE | — | ✅ |
| 8 | CostTransactionTypeEOUserDefinedFlag | USER_DEFINED_FLAG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
