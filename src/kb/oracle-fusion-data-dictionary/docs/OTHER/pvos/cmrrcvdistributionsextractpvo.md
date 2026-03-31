---
id: DOC-OTHER-PVO-CmrRcvDistributionsExtractPVO
doc_type: system-doc
title: "CmrRcvDistributionsExtractPVO — PVO Cross-Module"
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
  - CmrRcvDistributionsExtractPVO
  - cmrrcvdistributionsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrRcvDistributionsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cmr Rcv Distributions Extract. Acessa as tabelas: CMR_RCV_DISTRIBUTIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CmrBiccExtractAM.CmrRcvDistributionsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 1 | 1 | 20 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_rcv_distributions|CMR_RCV_DISTRIBUTIONS]] — 20 atributos (1 PKs, 20 BICC)

---

## ⚙️ Atributos

### [[cmr_rcv_distributions|CMR_RCV_DISTRIBUTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrRcvDistributionsPEOAccountedQty | ACCOUNTED_QTY | — | ✅ |
| 2 | CmrRcvDistributionsPEOAccountingEventId | ACCOUNTING_EVENT_ID | — | ✅ |
| 3 | CmrRcvDistributionsPEOAccountingLineType | ACCOUNTING_LINE_TYPE | — | ✅ |
| 4 | CmrRcvDistributionsPEOBalanceType | BALANCE_TYPE | — | ✅ |
| 5 | CmrRcvDistributionsPEOCmrSubLedgerId | CMR_SUB_LEDGER_ID | 🔑 | ✅ |
| 6 | CmrRcvDistributionsPEOCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 7 | CmrRcvDistributionsPEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | CmrRcvDistributionsPEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | CmrRcvDistributionsPEOEaEnteredCurrencyCode | EA_ENTERED_CURRENCY_CODE | — | ✅ |
| 10 | CmrRcvDistributionsPEOEnteredCurrencyAmount | ENTERED_CURRENCY_AMOUNT | — | ✅ |
| 11 | CmrRcvDistributionsPEOEnteredCurrencyCode | ENTERED_CURRENCY_CODE | — | ✅ |
| 12 | CmrRcvDistributionsPEOEventCostId | EVENT_COST_ID | — | ✅ |
| 13 | CmrRcvDistributionsPEOEventId | EVENT_ID | — | ✅ |
| 14 | CmrRcvDistributionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | CmrRcvDistributionsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 16 | CmrRcvDistributionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | CmrRcvDistributionsPEOLedgerAmount | LEDGER_AMOUNT | — | ✅ |
| 18 | CmrRcvDistributionsPEOLedgerCurrencyCode | LEDGER_CURRENCY_CODE | — | ✅ |
| 19 | CmrRcvDistributionsPEOLineNumber | LINE_NUMBER | — | ✅ |
| 20 | CmrRcvDistributionsPEOPjcTxnStatusCode | PJC_TXN_STATUS_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
