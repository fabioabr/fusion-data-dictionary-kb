---
id: DOC-OTHER-PVO-CstUncostedTxnErrorsP1
doc_type: system-doc
title: "CstUncostedTxnErrorsP1 — PVO Cross-Module"
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
  - CstUncostedTxnErrorsP1
  - cstuncostedtxnerrorsp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstUncostedTxnErrorsP1

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Uncosted Txn Errors P1. Acessa as tabelas: CST_UNCOSTED_TXN_ERRORS_V.

**Caminho:** `FscmTopModelAM.CstPeriodStatusAM.CstUncostedTxnErrorsP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 11 | 85% |

---

## 🔗 Tabelas Relacionadas

- [[cst_uncosted_txn_errors_v|CST_UNCOSTED_TXN_ERRORS_V]] — 13 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[cst_uncosted_txn_errors_v|CST_UNCOSTED_TXN_ERRORS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostBookId | COST_BOOK_ID | — | — |
| 2 | CostOrgId | COST_ORG_ID | — | — |
| 3 | ErrorCode | ERROR_CODE | — | ✅ |
| 4 | Message | MESSAGE | — | ✅ |
| 5 | MessageType | MESSAGE_TYPE | — | ✅ |
| 6 | ProcessorName | PROCESSOR_NAME | — | ✅ |
| 7 | Reference | REFERENCE | — | ✅ |
| 8 | ReferenceNumber | REFERENCE_NUMBER | — | ✅ |
| 9 | RequestId | REQUEST_ID | — | ✅ |
| 10 | RunControl | RUN_CONTROL | — | ✅ |
| 11 | SubprocessorName | SUBPROCESSOR_NAME | — | ✅ |
| 12 | TableName | TABLE_NAME | — | ✅ |
| 13 | TransactionId | TRANSACTION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
