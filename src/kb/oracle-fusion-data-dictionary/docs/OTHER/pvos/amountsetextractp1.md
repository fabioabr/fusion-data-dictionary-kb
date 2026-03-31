---
id: DOC-OTHER-PVO-AmountSetExtractP1
doc_type: system-doc
title: "AmountSetExtractP1 — PVO Cross-Module"
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
  - AmountSetExtractP1
  - amountsetextractp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AmountSetExtractP1

## 📌 Visão Geral

View Object para extração BICC de dados de Amount Set Extract P1. Acessa as tabelas: PJO_FIN_PLAN_AMT_SETS.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjoBiccExtractAM.AmountSetExtractP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 1 | 17 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjo_fin_plan_amt_sets|PJO_FIN_PLAN_AMT_SETS]] — 17 atributos (1 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[pjo_fin_plan_amt_sets|PJO_FIN_PLAN_AMT_SETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AmountSetPEOAllQtyFlag | ALL_QTY_FLAG | — | ✅ |
| 2 | AmountSetPEOAmountSetTypeCode | AMOUNT_SET_TYPE_CODE | — | ✅ |
| 3 | AmountSetPEOBillRateFlag | BILL_RATE_FLAG | — | ✅ |
| 4 | AmountSetPEOBrdndCostFlag | BRDND_COST_FLAG | — | ✅ |
| 5 | AmountSetPEOBrdndRateFlag | BRDND_RATE_FLAG | — | ✅ |
| 6 | AmountSetPEOCostQtyFlag | COST_QTY_FLAG | — | ✅ |
| 7 | AmountSetPEOCostRateFlag | COST_RATE_FLAG | — | ✅ |
| 8 | AmountSetPEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | AmountSetPEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | AmountSetPEOFinPlanAmtSetId | FIN_PLAN_AMT_SET_ID | 🔑 | ✅ |
| 11 | AmountSetPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | AmountSetPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | AmountSetPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | AmountSetPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | AmountSetPEORawCostFlag | RAW_COST_FLAG | — | ✅ |
| 16 | AmountSetPEORevenueFlag | REVENUE_FLAG | — | ✅ |
| 17 | AmountSetPEORevenueQtyFlag | REVENUE_QTY_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
