---
id: DOC-OTHER-PVO-PlanLineExtractP1
doc_type: system-doc
title: "PlanLineExtractP1 — PVO Cross-Module"
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
  - PlanLineExtractP1
  - planlineextractp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlanLineExtractP1

## 📌 Visão Geral

View Object para extração BICC de dados de Plan Line Extract P1. Acessa as tabelas: PJO_PLAN_LINES.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjoBiccExtractAM.PlanLineExtractP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 114 | 1 | 1 | 83 | 73% |

---

## 🔗 Tabelas Relacionadas

- [[pjo_plan_lines|PJO_PLAN_LINES]] — 114 atributos (1 PKs, 83 BICC)

---

## ⚙️ Atributos

### [[pjo_plan_lines|PJO_PLAN_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjoPlanLinesPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | PjoPlanLinesPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | PjoPlanLinesPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | PjoPlanLinesPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | PjoPlanLinesPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | PjoPlanLinesPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | PjoPlanLinesPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | PjoPlanLinesPEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | PjoPlanLinesPEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | PjoPlanLinesPEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | PjoPlanLinesPEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | PjoPlanLinesPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | PjoPlanLinesPEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | PjoPlanLinesPEOAttribute21 | ATTRIBUTE21 | — | — |
| 15 | PjoPlanLinesPEOAttribute22 | ATTRIBUTE22 | — | — |
| 16 | PjoPlanLinesPEOAttribute23 | ATTRIBUTE23 | — | — |
| 17 | PjoPlanLinesPEOAttribute24 | ATTRIBUTE24 | — | — |
| 18 | PjoPlanLinesPEOAttribute25 | ATTRIBUTE25 | — | — |
| 19 | PjoPlanLinesPEOAttribute26 | ATTRIBUTE26 | — | — |
| 20 | PjoPlanLinesPEOAttribute27 | ATTRIBUTE27 | — | — |
| 21 | PjoPlanLinesPEOAttribute28 | ATTRIBUTE28 | — | — |
| 22 | PjoPlanLinesPEOAttribute29 | ATTRIBUTE29 | — | — |
| 23 | PjoPlanLinesPEOAttribute3 | ATTRIBUTE3 | — | — |
| 24 | PjoPlanLinesPEOAttribute30 | ATTRIBUTE30 | — | — |
| 25 | PjoPlanLinesPEOAttribute4 | ATTRIBUTE4 | — | — |
| 26 | PjoPlanLinesPEOAttribute5 | ATTRIBUTE5 | — | — |
| 27 | PjoPlanLinesPEOAttribute6 | ATTRIBUTE6 | — | — |
| 28 | PjoPlanLinesPEOAttribute7 | ATTRIBUTE7 | — | — |
| 29 | PjoPlanLinesPEOAttribute8 | ATTRIBUTE8 | — | — |
| 30 | PjoPlanLinesPEOAttribute9 | ATTRIBUTE9 | — | — |
| 31 | PjoPlanLinesPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 32 | PjoPlanLinesPEOBillRateScheduleId | BILL_RATE_SCHEDULE_ID | — | ✅ |
| 33 | PjoPlanLinesPEOCostRateScheduleId | COST_RATE_SCHEDULE_ID | — | ✅ |
| 34 | PjoPlanLinesPEOCreatedBy | CREATED_BY | — | ✅ |
| 35 | PjoPlanLinesPEOCreationDate | CREATION_DATE | — | ✅ |
| 36 | PjoPlanLinesPEOIndRateScheduleId | IND_RATE_SCHEDULE_ID | — | ✅ |
| 37 | PjoPlanLinesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 38 | PjoPlanLinesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 39 | PjoPlanLinesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 40 | PjoPlanLinesPEOMultiErrorFlag | MULTI_ERROR_FLAG | — | ✅ |
| 41 | PjoPlanLinesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 42 | PjoPlanLinesPEOPlanLineId | PLAN_LINE_ID | 🔑 | ✅ |
| 43 | PjoPlanLinesPEOPlanVersionId | PLAN_VERSION_ID | — | ✅ |
| 44 | PjoPlanLinesPEOPlanningElementId | PLANNING_ELEMENT_ID | — | ✅ |
| 45 | PjoPlanLinesPEOTcAverageBillRate | TC_AVERAGE_BILL_RATE | — | ✅ |
| 46 | PjoPlanLinesPEOTcAverageBrdndCostRate | TC_AVERAGE_BRDND_COST_RATE | — | ✅ |
| 47 | PjoPlanLinesPEOTcAverageRawCostRate | TC_AVERAGE_RAW_COST_RATE | — | ✅ |
| 48 | PjoPlanLinesPEOTcAvgStdBillRate | TC_AVG_STD_BILL_RATE | — | ✅ |
| 49 | PjoPlanLinesPEOTcAvgStdBrdndCostRate | TC_AVG_STD_BRDND_COST_RATE | — | ✅ |
| 50 | PjoPlanLinesPEOTcAvgStdBrdndMultiplier | TC_AVG_STD_BRDND_MULTIPLIER | — | ✅ |
| 51 | PjoPlanLinesPEOTcAvgStdRawCostRate | TC_AVG_STD_RAW_COST_RATE | — | ✅ |
| 52 | PjoPlanLinesPEOTcBillRateOverride | TC_BILL_RATE_OVERRIDE | — | ✅ |
| 53 | PjoPlanLinesPEOTcBrdndCostRateOverride | TC_BRDND_COST_RATE_OVERRIDE | — | ✅ |
| 54 | PjoPlanLinesPEOTcEtcBillRate | TC_ETC_BILL_RATE | — | ✅ |
| 55 | PjoPlanLinesPEOTcEtcBrdndCostRate | TC_ETC_BRDND_COST_RATE | — | ✅ |
| 56 | PjoPlanLinesPEOTcEtcRawCostRate | TC_ETC_RAW_COST_RATE | — | ✅ |
| 57 | PjoPlanLinesPEOTcMarkupPercent | TC_MARKUP_PERCENT | — | ✅ |
| 58 | PjoPlanLinesPEOTcRawCostRateOverride | TC_RAW_COST_RATE_OVERRIDE | — | ✅ |
| 59 | PjoPlanLinesPEOTotalActQuantity | TOTAL_ACT_QUANTITY | — | ✅ |
| 60 | PjoPlanLinesPEOTotalExtQuantity | TOTAL_EXT_QUANTITY | — | ✅ |
| 61 | PjoPlanLinesPEOTotalPcActBrdndCost | TOTAL_PC_ACT_BRDND_COST | — | ✅ |
| 62 | PjoPlanLinesPEOTotalPcActRawCost | TOTAL_PC_ACT_RAW_COST | — | ✅ |
| 63 | PjoPlanLinesPEOTotalPcActRevenue | TOTAL_PC_ACT_REVENUE | — | ✅ |
| 64 | PjoPlanLinesPEOTotalPcBrdndCost | TOTAL_PC_BRDND_COST | — | ✅ |
| 65 | PjoPlanLinesPEOTotalPcExtBrdndCost | TOTAL_PC_EXT_BRDND_COST | — | ✅ |
| 66 | PjoPlanLinesPEOTotalPcExtRawCost | TOTAL_PC_EXT_RAW_COST | — | ✅ |
| 67 | PjoPlanLinesPEOTotalPcPoBrdndCost | TOTAL_PC_PO_BRDND_COST | — | ✅ |
| 68 | PjoPlanLinesPEOTotalPcPoRawCost | TOTAL_PC_PO_RAW_COST | — | ✅ |
| 69 | PjoPlanLinesPEOTotalPcRawCost | TOTAL_PC_RAW_COST | — | ✅ |
| 70 | PjoPlanLinesPEOTotalPcReqBrdndCost | TOTAL_PC_REQ_BRDND_COST | — | ✅ |
| 71 | PjoPlanLinesPEOTotalPcReqRawCost | TOTAL_PC_REQ_RAW_COST | — | ✅ |
| 72 | PjoPlanLinesPEOTotalPcRevenue | TOTAL_PC_REVENUE | — | ✅ |
| 73 | PjoPlanLinesPEOTotalPcSiBrdndCost | TOTAL_PC_SI_BRDND_COST | — | ✅ |
| 74 | PjoPlanLinesPEOTotalPcSiRawCost | TOTAL_PC_SI_RAW_COST | — | ✅ |
| 75 | PjoPlanLinesPEOTotalPcToBrdndCost | TOTAL_PC_TO_BRDND_COST | — | ✅ |
| 76 | PjoPlanLinesPEOTotalPcToRawCost | TOTAL_PC_TO_RAW_COST | — | ✅ |
| 77 | PjoPlanLinesPEOTotalPfcActBrdndCost | TOTAL_PFC_ACT_BRDND_COST | — | ✅ |
| 78 | PjoPlanLinesPEOTotalPfcActRawCost | TOTAL_PFC_ACT_RAW_COST | — | ✅ |
| 79 | PjoPlanLinesPEOTotalPfcActRevenue | TOTAL_PFC_ACT_REVENUE | — | ✅ |
| 80 | PjoPlanLinesPEOTotalPfcBrdndCost | TOTAL_PFC_BRDND_COST | — | ✅ |
| 81 | PjoPlanLinesPEOTotalPfcExtBrdndCost | TOTAL_PFC_EXT_BRDND_COST | — | ✅ |
| 82 | PjoPlanLinesPEOTotalPfcExtRawCost | TOTAL_PFC_EXT_RAW_COST | — | ✅ |
| 83 | PjoPlanLinesPEOTotalPfcPoBrdndCost | TOTAL_PFC_PO_BRDND_COST | — | ✅ |
| 84 | PjoPlanLinesPEOTotalPfcPoRawCost | TOTAL_PFC_PO_RAW_COST | — | ✅ |
| 85 | PjoPlanLinesPEOTotalPfcRawCost | TOTAL_PFC_RAW_COST | — | ✅ |
| 86 | PjoPlanLinesPEOTotalPfcReqBrdndCost | TOTAL_PFC_REQ_BRDND_COST | — | ✅ |
| 87 | PjoPlanLinesPEOTotalPfcReqRawCost | TOTAL_PFC_REQ_RAW_COST | — | ✅ |
| 88 | PjoPlanLinesPEOTotalPfcRevenue | TOTAL_PFC_REVENUE | — | ✅ |
| 89 | PjoPlanLinesPEOTotalPfcSiBrdndCost | TOTAL_PFC_SI_BRDND_COST | — | ✅ |
| 90 | PjoPlanLinesPEOTotalPfcSiRawCost | TOTAL_PFC_SI_RAW_COST | — | ✅ |
| 91 | PjoPlanLinesPEOTotalPfcToBrdndCost | TOTAL_PFC_TO_BRDND_COST | — | ✅ |
| 92 | PjoPlanLinesPEOTotalPfcToRawCost | TOTAL_PFC_TO_RAW_COST | — | ✅ |
| 93 | PjoPlanLinesPEOTotalPoQuantity | TOTAL_PO_QUANTITY | — | ✅ |
| 94 | PjoPlanLinesPEOTotalQuantity | TOTAL_QUANTITY | — | ✅ |
| 95 | PjoPlanLinesPEOTotalReqQuantity | TOTAL_REQ_QUANTITY | — | ✅ |
| 96 | PjoPlanLinesPEOTotalSiQuantity | TOTAL_SI_QUANTITY | — | ✅ |
| 97 | PjoPlanLinesPEOTotalTcActBrdndCost | TOTAL_TC_ACT_BRDND_COST | — | ✅ |
| 98 | PjoPlanLinesPEOTotalTcActRawCost | TOTAL_TC_ACT_RAW_COST | — | ✅ |
| 99 | PjoPlanLinesPEOTotalTcActRevenue | TOTAL_TC_ACT_REVENUE | — | ✅ |
| 100 | PjoPlanLinesPEOTotalTcBrdndCost | TOTAL_TC_BRDND_COST | — | ✅ |
| 101 | PjoPlanLinesPEOTotalTcExtBrdndCost | TOTAL_TC_EXT_BRDND_COST | — | ✅ |
| 102 | PjoPlanLinesPEOTotalTcExtRawCost | TOTAL_TC_EXT_RAW_COST | — | ✅ |
| 103 | PjoPlanLinesPEOTotalTcPoBrdndCost | TOTAL_TC_PO_BRDND_COST | — | ✅ |
| 104 | PjoPlanLinesPEOTotalTcPoRawCost | TOTAL_TC_PO_RAW_COST | — | ✅ |
| 105 | PjoPlanLinesPEOTotalTcRawCost | TOTAL_TC_RAW_COST | — | ✅ |
| 106 | PjoPlanLinesPEOTotalTcReqBrdndCost | TOTAL_TC_REQ_BRDND_COST | — | ✅ |
| 107 | PjoPlanLinesPEOTotalTcReqRawCost | TOTAL_TC_REQ_RAW_COST | — | ✅ |
| 108 | PjoPlanLinesPEOTotalTcRevenue | TOTAL_TC_REVENUE | — | ✅ |
| 109 | PjoPlanLinesPEOTotalTcSiBrdndCost | TOTAL_TC_SI_BRDND_COST | — | ✅ |
| 110 | PjoPlanLinesPEOTotalTcSiRawCost | TOTAL_TC_SI_RAW_COST | — | ✅ |
| 111 | PjoPlanLinesPEOTotalTcToBrdndCost | TOTAL_TC_TO_BRDND_COST | — | ✅ |
| 112 | PjoPlanLinesPEOTotalTcToRawCost | TOTAL_TC_TO_RAW_COST | — | ✅ |
| 113 | PjoPlanLinesPEOTotalToQuantity | TOTAL_TO_QUANTITY | — | ✅ |
| 114 | PjoPlanLinesPEOTxnCurrencyCode | TXN_CURRENCY_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
