---
id: DOC-OTHER-PVO-CstTradeEventCostsExtractPVO
doc_type: system-doc
title: "CstTradeEventCostsExtractPVO — PVO Cross-Module"
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
  - CstTradeEventCostsExtractPVO
  - csttradeeventcostsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstTradeEventCostsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Trade Event Costs Extract. Acessa as tabelas: CST_TRADE_EVENT_COSTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstTradeEventCostsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 1 | 1 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_trade_event_costs|CST_TRADE_EVENT_COSTS]] — 21 atributos (1 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[cst_trade_event_costs|CST_TRADE_EVENT_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstTradeEventCostsPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | CstTradeEventCostsPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | CstTradeEventCostsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 4 | CstTradeEventCostsPEOCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 5 | CstTradeEventCostsPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | ✅ |
| 6 | CstTradeEventCostsPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | ✅ |
| 7 | CstTradeEventCostsPEOIntfUnitCost | INTF_UNIT_COST | — | ✅ |
| 8 | CstTradeEventCostsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | CstTradeEventCostsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | CstTradeEventCostsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | CstTradeEventCostsPEOMarkupRate | MARKUP_RATE | — | ✅ |
| 12 | CstTradeEventCostsPEOOriginalUnitCost | ORIGINAL_UNIT_COST | — | ✅ |
| 13 | CstTradeEventCostsPEOSourceSystem | SOURCE_SYSTEM | — | ✅ |
| 14 | CstTradeEventCostsPEOTaxInclusiveFlag | TAX_INCLUSIVE_FLAG | — | ✅ |
| 15 | CstTradeEventCostsPEOTradeEventCostId | TRADE_EVENT_COST_ID | 🔑 | ✅ |
| 16 | CstTradeEventCostsPEOTradeEventId | TRADE_EVENT_ID | — | ✅ |
| 17 | CstTradeEventCostsPEOTransactionAmount | TRANSACTION_AMOUNT | — | ✅ |
| 18 | CstTradeEventCostsPEOTransferPriceComponent | TRANSFER_PRICE_COMPONENT | — | ✅ |
| 19 | CstTradeEventCostsPEOUnitCost | UNIT_COST | — | ✅ |
| 20 | CstTradeEventCostsPEOUnitCostUomFactor | UNIT_COST_UOM_FACTOR | — | ✅ |
| 21 | CstTradeEventCostsPEOUomCode | UOM_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
