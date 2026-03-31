---
id: DOC-OTHER-PVO-CostDistributionLinesExtractPVO
doc_type: system-doc
title: "CostDistributionLinesExtractPVO — PVO Cross-Module"
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
  - CostDistributionLinesExtractPVO
  - costdistributionlinesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CostDistributionLinesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cost Distribution Lines Extract. Acessa as tabelas: CST_COST_DISTRIBUTION_LINES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CostDistributionLinesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 1 | 1 | 29 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_distribution_lines|CST_COST_DISTRIBUTION_LINES]] — 29 atributos (1 PKs, 29 BICC)

---

## ⚙️ Atributos

### [[cst_cost_distribution_lines|CST_COST_DISTRIBUTION_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostDistributionLinesPEOAccountingDefinitionId | ACCOUNTING_DEFINITION_ID | — | ✅ |
| 2 | CostDistributionLinesPEOAccountingLineType | ACCOUNTING_LINE_TYPE | — | ✅ |
| 3 | CostDistributionLinesPEOAeHeaderId | AE_HEADER_ID | — | ✅ |
| 4 | CostDistributionLinesPEOAeLineNum | AE_LINE_NUM | — | ✅ |
| 5 | CostDistributionLinesPEOCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 6 | CostDistributionLinesPEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 7 | CostDistributionLinesPEOCostId | COST_ID | — | ✅ |
| 8 | CostDistributionLinesPEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | CostDistributionLinesPEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | CostDistributionLinesPEODistributionId | DISTRIBUTION_ID | — | ✅ |
| 11 | CostDistributionLinesPEODistributionLineId | DISTRIBUTION_LINE_ID | 🔑 | ✅ |
| 12 | CostDistributionLinesPEODistributionQuantityRate | DISTRIBUTION_QUANTITY_RATE | — | ✅ |
| 13 | CostDistributionLinesPEODrCrSign | DR_CR_SIGN | — | ✅ |
| 14 | CostDistributionLinesPEOEnteredCurrencyAmount | ENTERED_CURRENCY_AMOUNT | — | ✅ |
| 15 | CostDistributionLinesPEOEnteredCurrencyCode | ENTERED_CURRENCY_CODE | — | ✅ |
| 16 | CostDistributionLinesPEOEventId | EVENT_ID | — | ✅ |
| 17 | CostDistributionLinesPEOExchangeDate | EXCHANGE_DATE | — | ✅ |
| 18 | CostDistributionLinesPEOExchangeRate | EXCHANGE_RATE | — | ✅ |
| 19 | CostDistributionLinesPEOExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 20 | CostDistributionLinesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | CostDistributionLinesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 22 | CostDistributionLinesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 23 | CostDistributionLinesPEOLedgerAmount | LEDGER_AMOUNT | — | ✅ |
| 24 | CostDistributionLinesPEOLineNumber | LINE_NUMBER | — | ✅ |
| 25 | CostDistributionLinesPEOPjcTxnStatusCode | PJC_TXN_STATUS_CODE | — | ✅ |
| 26 | CostDistributionLinesPEOSlaCodeCombinationId | SLA_CODE_COMBINATION_ID | — | ✅ |
| 27 | CostDistributionLinesPEOSourceTable | SOURCE_TABLE | — | ✅ |
| 28 | CostDistributionLinesPEOTransactionCostId | TRANSACTION_COST_ID | — | ✅ |
| 29 | CostDistributionLinesPEOTransactionEventId | TRANSACTION_EVENT_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
