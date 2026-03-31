---
id: DOC-OTHER-PVO-CstIncomingTxnCostSourcesExtractPVO
doc_type: system-doc
title: "CstIncomingTxnCostSourcesExtractPVO — PVO Cross-Module"
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
  - CstIncomingTxnCostSourcesExtractPVO
  - cstincomingtxncostsourcesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstIncomingTxnCostSourcesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Incoming Txn Cost Sources Extract. Acessa as tabelas: CST_INCOMING_TXN_COST_SOURCES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstIncomingTxnCostSourcesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 6 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_incoming_txn_cost_sources|CST_INCOMING_TXN_COST_SOURCES]] — 13 atributos (6 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[cst_incoming_txn_cost_sources|CST_INCOMING_TXN_COST_SOURCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstIncomingTxnCostSourcesPEOChargeLineNumber | CHARGE_LINE_NUMBER | 🔑 | ✅ |
| 2 | CstIncomingTxnCostSourcesPEOCmrApInvoiceDistId | CMR_AP_INVOICE_DIST_ID | 🔑 | ✅ |
| 3 | CstIncomingTxnCostSourcesPEOCmrPoDistributionId | CMR_PO_DISTRIBUTION_ID | 🔑 | ✅ |
| 4 | CstIncomingTxnCostSourcesPEOConsPriceUpdEffectiveDate | CONS_PRICE_UPD_EFFECTIVE_DATE | — | ✅ |
| 5 | CstIncomingTxnCostSourcesPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | CstIncomingTxnCostSourcesPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | CstIncomingTxnCostSourcesPEOCstInvTransactionId | CST_INV_TRANSACTION_ID | 🔑 | ✅ |
| 8 | CstIncomingTxnCostSourcesPEOFiscalDocHeaderId | FISCAL_DOC_HEADER_ID | 🔑 | ✅ |
| 9 | CstIncomingTxnCostSourcesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | CstIncomingTxnCostSourcesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | CstIncomingTxnCostSourcesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | CstIncomingTxnCostSourcesPEOPoEventDate | PO_EVENT_DATE | — | ✅ |
| 13 | CstIncomingTxnCostSourcesPEOTradeOperationId | TRADE_OPERATION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
