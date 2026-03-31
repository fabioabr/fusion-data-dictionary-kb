---
id: DOC-OTHER-PVO-CmrRcvEventCostsExtractPVO
doc_type: system-doc
title: "CmrRcvEventCostsExtractPVO — PVO Cross-Module"
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
  - CmrRcvEventCostsExtractPVO
  - cmrrcveventcostsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrRcvEventCostsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cmr Rcv Event Costs Extract. Acessa as tabelas: CMR_RCV_EVENT_COSTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CmrBiccExtractAM.CmrRcvEventCostsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 36 | 1 | 1 | 36 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_rcv_event_costs|CMR_RCV_EVENT_COSTS]] — 36 atributos (1 PKs, 36 BICC)

---

## ⚙️ Atributos

### [[cmr_rcv_event_costs|CMR_RCV_EVENT_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrRcvEventCostsPEOAccountingEventId | ACCOUNTING_EVENT_ID | — | ✅ |
| 2 | CmrRcvEventCostsPEOAccrualClrId | ACCRUAL_CLR_ID | — | ✅ |
| 3 | CmrRcvEventCostsPEOChargeId | CHARGE_ID | — | ✅ |
| 4 | CmrRcvEventCostsPEOCmrApInvoiceDistId | CMR_AP_INVOICE_DIST_ID | — | ✅ |
| 5 | CmrRcvEventCostsPEOCmrPoDistributionId | CMR_PO_DISTRIBUTION_ID | — | ✅ |
| 6 | CmrRcvEventCostsPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | CmrRcvEventCostsPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | CmrRcvEventCostsPEOCrossBuFlag | CROSS_BU_FLAG | — | ✅ |
| 9 | CmrRcvEventCostsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 10 | CmrRcvEventCostsPEOCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 11 | CmrRcvEventCostsPEOCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 12 | CmrRcvEventCostsPEOCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 13 | CmrRcvEventCostsPEODestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 14 | CmrRcvEventCostsPEOEventCostId | EVENT_COST_ID | 🔑 | ✅ |
| 15 | CmrRcvEventCostsPEOEventCostSource | EVENT_COST_SOURCE | — | ✅ |
| 16 | CmrRcvEventCostsPEOEventCostSourceType | EVENT_COST_SOURCE_TYPE | — | ✅ |
| 17 | CmrRcvEventCostsPEOEventPriorUnitCost | EVENT_PRIOR_UNIT_COST | — | ✅ |
| 18 | CmrRcvEventCostsPEOEventUnitCost | EVENT_UNIT_COST | — | ✅ |
| 19 | CmrRcvEventCostsPEOInclusiveFlag | INCLUSIVE_FLAG | — | ✅ |
| 20 | CmrRcvEventCostsPEOInclusiveTax | INCLUSIVE_TAX | — | ✅ |
| 21 | CmrRcvEventCostsPEOIntercompanyInvoicingFlag | INTERCOMPANY_INVOICING_FLAG | — | ✅ |
| 22 | CmrRcvEventCostsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | CmrRcvEventCostsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 24 | CmrRcvEventCostsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 25 | CmrRcvEventCostsPEOProcurementBuFlag | PROCUREMENT_BU_FLAG | — | ✅ |
| 26 | CmrRcvEventCostsPEORcvChargeActualId | RCV_CHARGE_ACTUAL_ID | — | ✅ |
| 27 | CmrRcvEventCostsPEORcvChargeAllocId | RCV_CHARGE_ALLOC_ID | — | ✅ |
| 28 | CmrRcvEventCostsPEORcvChargeEstimateId | RCV_CHARGE_ESTIMATE_ID | — | ✅ |
| 29 | CmrRcvEventCostsPEOSelfAssessedFlag | SELF_ASSESSED_FLAG | — | ✅ |
| 30 | CmrRcvEventCostsPEOServiceLineTypePoFlag | SERVICE_LINE_TYPE_PO_FLAG | — | ✅ |
| 31 | CmrRcvEventCostsPEOTaxLiabilityFlag | TAX_LIABILITY_FLAG | — | ✅ |
| 32 | CmrRcvEventCostsPEOTradeEventAvgCostId | TRADE_EVENT_AVG_COST_ID | — | ✅ |
| 33 | CmrRcvEventCostsPEOTradeEventCostId | TRADE_EVENT_COST_ID | — | ✅ |
| 34 | CmrRcvEventCostsPEOTradeEventTaxId | TRADE_EVENT_TAX_ID | — | ✅ |
| 35 | CmrRcvEventCostsPEOTradeOverheadId | TRADE_OVERHEAD_ID | — | ✅ |
| 36 | CmrRcvEventCostsPEOTransactionTaxId | TRANSACTION_TAX_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
