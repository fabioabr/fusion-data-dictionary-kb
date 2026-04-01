---
id: DOC-OTHER-PVO-CstResourceCostsExtractPVO
doc_type: system-doc
title: "CstResourceCostsExtractPVO — PVO Cross-Module"
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
  - CstResourceCostsExtractPVO
  - cstresourcecostsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstResourceCostsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Resource Costs Extract. Acessa as tabelas: CST_RESOURCE_COSTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstResourceCostsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 1 | 1 | 27 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_resource_costs|CST_RESOURCE_COSTS]] — 27 atributos (1 PKs, 27 BICC)

---

## ⚙️ Atributos

### [[cst_resource_costs|CST_RESOURCE_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstResourceCostsPEOAdditionalProcessingCode | ADDITIONAL_PROCESSING_CODE | — | ✅ |
| 2 | CstResourceCostsPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | ✅ |
| 3 | CstResourceCostsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 4 | CstResourceCostsPEOCostDate | COST_DATE | — | ✅ |
| 5 | CstResourceCostsPEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 6 | CstResourceCostsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 7 | CstResourceCostsPEOCostReference | COST_REFERENCE | — | ✅ |
| 8 | CstResourceCostsPEOCostSource | COST_SOURCE | — | ✅ |
| 9 | CstResourceCostsPEOCostTransactionType | COST_TRANSACTION_TYPE | — | ✅ |
| 10 | CstResourceCostsPEOCreatedBy | CREATED_BY | — | ✅ |
| 11 | CstResourceCostsPEOCreationDate | CREATION_DATE | — | ✅ |
| 12 | CstResourceCostsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 13 | CstResourceCostsPEODistributionId | DISTRIBUTION_ID | — | ✅ |
| 14 | CstResourceCostsPEOEffDate | EFF_DATE | — | ✅ |
| 15 | CstResourceCostsPEOExpensePoolId | EXPENSE_POOL_ID | — | ✅ |
| 16 | CstResourceCostsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | CstResourceCostsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 18 | CstResourceCostsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | CstResourceCostsPEOPeriodName | PERIOD_NAME | — | ✅ |
| 20 | CstResourceCostsPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 21 | CstResourceCostsPEOQuantity | QUANTITY | — | ✅ |
| 22 | CstResourceCostsPEOResourceCostId | RESOURCE_COST_ID | 🔑 | ✅ |
| 23 | CstResourceCostsPEOResourceId | RESOURCE_ID | — | ✅ |
| 24 | CstResourceCostsPEOResourceTransactionId | RESOURCE_TRANSACTION_ID | — | ✅ |
| 25 | CstResourceCostsPEOStdResourceRateId | STD_RESOURCE_RATE_ID | — | ✅ |
| 26 | CstResourceCostsPEOUnitCost | UNIT_COST | — | ✅ |
| 27 | CstResourceCostsPEOUomCode | UOM_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
