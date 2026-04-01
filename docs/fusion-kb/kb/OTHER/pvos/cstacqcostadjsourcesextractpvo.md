---
id: DOC-OTHER-PVO-CstAcqCostAdjSourcesExtractPVO
doc_type: system-doc
title: "CstAcqCostAdjSourcesExtractPVO — PVO Cross-Module"
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
  - CstAcqCostAdjSourcesExtractPVO
  - cstacqcostadjsourcesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstAcqCostAdjSourcesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Acq Cost Adj Sources Extract. Acessa as tabelas: CST_ACQ_COST_ADJ_SOURCES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstAcqCostAdjSourcesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 6 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_acq_cost_adj_sources|CST_ACQ_COST_ADJ_SOURCES]] — 13 atributos (6 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[cst_acq_cost_adj_sources|CST_ACQ_COST_ADJ_SOURCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstAcqCostAdjSourcesPEOAdjustmentTransactionId | ADJUSTMENT_TRANSACTION_ID | 🔑 | ✅ |
| 2 | CstAcqCostAdjSourcesPEOChargeLineNumber | CHARGE_LINE_NUMBER | 🔑 | ✅ |
| 3 | CstAcqCostAdjSourcesPEOCmrApInvoiceDistId | CMR_AP_INVOICE_DIST_ID | 🔑 | ✅ |
| 4 | CstAcqCostAdjSourcesPEOCmrPoDistributionId | CMR_PO_DISTRIBUTION_ID | 🔑 | ✅ |
| 5 | CstAcqCostAdjSourcesPEOConsPriceUpdEffectiveDate | CONS_PRICE_UPD_EFFECTIVE_DATE | — | ✅ |
| 6 | CstAcqCostAdjSourcesPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | CstAcqCostAdjSourcesPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | CstAcqCostAdjSourcesPEOFiscalDocHeaderId | FISCAL_DOC_HEADER_ID | 🔑 | ✅ |
| 9 | CstAcqCostAdjSourcesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | CstAcqCostAdjSourcesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | CstAcqCostAdjSourcesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | CstAcqCostAdjSourcesPEOPoEventDate | PO_EVENT_DATE | — | ✅ |
| 13 | CstAcqCostAdjSourcesPEOTradeOperationId | TRADE_OPERATION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
