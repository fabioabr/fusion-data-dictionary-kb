---
id: DOC-OTHER-PVO-CmrTradeEventAvgCostExtractPVO
doc_type: system-doc
title: "CmrTradeEventAvgCostExtractPVO — PVO Cross-Module"
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
  - CmrTradeEventAvgCostExtractPVO
  - cmrtradeeventavgcostextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrTradeEventAvgCostExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cmr Trade Event Avg Cost Extract. Acessa as tabelas: CMR_TRADE_EVENT_AVG_COST.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CmrBiccExtractAM.CmrTradeEventAvgCostExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 1 | 1 | 28 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_trade_event_avg_cost|CMR_TRADE_EVENT_AVG_COST]] — 28 atributos (1 PKs, 28 BICC)

---

## ⚙️ Atributos

### [[cmr_trade_event_avg_cost|CMR_TRADE_EVENT_AVG_COST]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrTradeEventAvgCostPEOActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | CmrTradeEventAvgCostPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 3 | CmrTradeEventAvgCostPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | CmrTradeEventAvgCostPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | CmrTradeEventAvgCostPEOCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 6 | CmrTradeEventAvgCostPEODooFullfillLineId | DOO_FULLFILL_LINE_ID | — | ✅ |
| 7 | CmrTradeEventAvgCostPEOEffectiveDate | EFFECTIVE_DATE | — | ✅ |
| 8 | CmrTradeEventAvgCostPEOExtendedAmount | EXTENDED_AMOUNT | — | ✅ |
| 9 | CmrTradeEventAvgCostPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | ✅ |
| 10 | CmrTradeEventAvgCostPEOInterOrgShipmentInvTxnId | INTER_ORG_SHIPMENT_INV_TXN_ID | — | ✅ |
| 11 | CmrTradeEventAvgCostPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | CmrTradeEventAvgCostPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | CmrTradeEventAvgCostPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | CmrTradeEventAvgCostPEONewAverageCost | NEW_AVERAGE_COST | — | ✅ |
| 15 | CmrTradeEventAvgCostPEONewOnhandQty | NEW_ONHAND_QTY | — | ✅ |
| 16 | CmrTradeEventAvgCostPEOOwnershipChangeEventType | OWNERSHIP_CHANGE_EVENT_TYPE | — | ✅ |
| 17 | CmrTradeEventAvgCostPEOOwnershipChangeTxnId | OWNERSHIP_CHANGE_TXN_ID | — | ✅ |
| 18 | CmrTradeEventAvgCostPEOPoLineLocationId | PO_LINE_LOCATION_ID | — | ✅ |
| 19 | CmrTradeEventAvgCostPEOPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 20 | CmrTradeEventAvgCostPEOPriorAverageCost | PRIOR_AVERAGE_COST | — | ✅ |
| 21 | CmrTradeEventAvgCostPEOPriorOnhandQty | PRIOR_ONHAND_QTY | — | ✅ |
| 22 | CmrTradeEventAvgCostPEOPriorTradeEventAvgCostId | PRIOR_TRADE_EVENT_AVG_COST_ID | — | ✅ |
| 23 | CmrTradeEventAvgCostPEOTradeEventAvgCostId | TRADE_EVENT_AVG_COST_ID | 🔑 | ✅ |
| 24 | CmrTradeEventAvgCostPEOTradeInventoryOrgId | TRADE_INVENTORY_ORG_ID | — | ✅ |
| 25 | CmrTradeEventAvgCostPEOTransactionCost | TRANSACTION_COST | — | ✅ |
| 26 | CmrTradeEventAvgCostPEOTransferPricingUnitCost | TRANSFER_PRICING_UNIT_COST | — | ✅ |
| 27 | CmrTradeEventAvgCostPEOTransferPricingUomCode | TRANSFER_PRICING_UOM_CODE | — | ✅ |
| 28 | CmrTradeEventAvgCostPEOTxnCurrencyCode | TXN_CURRENCY_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
