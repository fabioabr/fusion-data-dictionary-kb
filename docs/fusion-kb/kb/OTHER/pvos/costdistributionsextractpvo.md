---
id: DOC-OTHER-PVO-CostDistributionsExtractPVO
doc_type: system-doc
title: "CostDistributionsExtractPVO — PVO Cross-Module"
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
  - CostDistributionsExtractPVO
  - costdistributionsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CostDistributionsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cost Distributions Extract. Acessa as tabelas: CST_COST_DISTRIBUTIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CostDistributionsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 31 | 1 | 1 | 31 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_distributions|CST_COST_DISTRIBUTIONS]] — 31 atributos (1 PKs, 31 BICC)

---

## ⚙️ Atributos

### [[cst_cost_distributions|CST_COST_DISTRIBUTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostDistributionsPEOAccountedFlag | ACCOUNTED_FLAG | — | ✅ |
| 2 | CostDistributionsPEOAdditionalProcessingCode | ADDITIONAL_PROCESSING_CODE | — | ✅ |
| 3 | CostDistributionsPEOBaseCurrencyCode | BASE_CURRENCY_CODE | — | ✅ |
| 4 | CostDistributionsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 5 | CostDistributionsPEOCostOrganizationId | COST_ORGANIZATION_ID | — | ✅ |
| 6 | CostDistributionsPEOCostTransactionType | COST_TRANSACTION_TYPE | — | ✅ |
| 7 | CostDistributionsPEOCostTransactionUom | COST_TRANSACTION_UOM | — | ✅ |
| 8 | CostDistributionsPEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | CostDistributionsPEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | CostDistributionsPEODepTrxnId | DEP_TRXN_ID | — | ✅ |
| 11 | CostDistributionsPEODistributionId | DISTRIBUTION_ID | 🔑 | ✅ |
| 12 | CostDistributionsPEOEffDate | EFF_DATE | — | ✅ |
| 13 | CostDistributionsPEOEffDateChar | EFF_DATE_CHAR | — | ✅ |
| 14 | CostDistributionsPEOEntityCode | ENTITY_CODE | — | ✅ |
| 15 | CostDistributionsPEOEventClassCode | EVENT_CLASS_CODE | — | ✅ |
| 16 | CostDistributionsPEOEventId | EVENT_ID | — | ✅ |
| 17 | CostDistributionsPEOEventTypeCode | EVENT_TYPE_CODE | — | ✅ |
| 18 | CostDistributionsPEOGlDate | GL_DATE | — | ✅ |
| 19 | CostDistributionsPEOGrossMarginFlag | GROSS_MARGIN_FLAG | — | ✅ |
| 20 | CostDistributionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | CostDistributionsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 22 | CostDistributionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 23 | CostDistributionsPEOLayerQuantity | LAYER_QUANTITY | — | ✅ |
| 24 | CostDistributionsPEOLedgerId | LEDGER_ID | — | ✅ |
| 25 | CostDistributionsPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 26 | CostDistributionsPEOPeriodName | PERIOD_NAME | — | ✅ |
| 27 | CostDistributionsPEOPjcTxnStatusCode | PJC_TXN_STATUS_CODE | — | ✅ |
| 28 | CostDistributionsPEORecTrxnId | REC_TRXN_ID | — | ✅ |
| 29 | CostDistributionsPEOTransactionId | TRANSACTION_ID | — | ✅ |
| 30 | CostDistributionsPEOTransactionNumber | TRANSACTION_NUMBER | — | ✅ |
| 31 | CostDistributionsPEOValOnhandFlag | VAL_ONHAND_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
