---
id: DOC-OTHER-PVO-CmrTradeOverheadsExtractPVO
doc_type: system-doc
title: "CmrTradeOverheadsExtractPVO — PVO Cross-Module"
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
  - CmrTradeOverheadsExtractPVO
  - cmrtradeoverheadsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrTradeOverheadsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cmr Trade Overheads Extract. Acessa as tabelas: CMR_TRADE_OVERHEADS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CmrBiccExtractAM.CmrTradeOverheadsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_trade_overheads|CMR_TRADE_OVERHEADS]] — 16 atributos (1 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[cmr_trade_overheads|CMR_TRADE_OVERHEADS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrTradeOverheadsPEOCostDate | COST_DATE | — | ✅ |
| 2 | CmrTradeOverheadsPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | CmrTradeOverheadsPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | CmrTradeOverheadsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 5 | CmrTradeOverheadsPEOExpensePoolId | EXPENSE_POOL_ID | — | ✅ |
| 6 | CmrTradeOverheadsPEOInvTransactionId | INV_TRANSACTION_ID | — | ✅ |
| 7 | CmrTradeOverheadsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | CmrTradeOverheadsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | CmrTradeOverheadsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | CmrTradeOverheadsPEOProcessedByRaFlag | PROCESSED_BY_RA_FLAG | — | ✅ |
| 11 | CmrTradeOverheadsPEOTradeEventId | TRADE_EVENT_ID | — | ✅ |
| 12 | CmrTradeOverheadsPEOTradeOverheadId | TRADE_OVERHEAD_ID | 🔑 | ✅ |
| 13 | CmrTradeOverheadsPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 14 | CmrTradeOverheadsPEOUnitCost | UNIT_COST | — | ✅ |
| 15 | CmrTradeOverheadsPEOUomCode | UOM_CODE | — | ✅ |
| 16 | CmrTradeOverheadsPEOUomConversionFactor | UOM_CONVERSION_FACTOR | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
