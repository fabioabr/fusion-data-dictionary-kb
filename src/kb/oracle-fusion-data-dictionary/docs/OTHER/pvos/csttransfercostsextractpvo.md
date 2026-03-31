---
id: DOC-OTHER-PVO-CstTransferCostsExtractPVO
doc_type: system-doc
title: "CstTransferCostsExtractPVO — PVO Cross-Module"
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
  - CstTransferCostsExtractPVO
  - csttransfercostsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstTransferCostsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Transfer Costs Extract. Acessa as tabelas: CST_TRANSFER_COSTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstTransferCostsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 34 | 1 | 1 | 34 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_transfer_costs|CST_TRANSFER_COSTS]] — 34 atributos (1 PKs, 34 BICC)

---

## ⚙️ Atributos

### [[cst_transfer_costs|CST_TRANSFER_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstTransferCostsPEOAbsorptionType | ABSORPTION_TYPE | — | ✅ |
| 2 | CstTransferCostsPEOAdditionalProcessingCode | ADDITIONAL_PROCESSING_CODE | — | ✅ |
| 3 | CstTransferCostsPEOAdjPostedFlag | ADJ_POSTED_FLAG | — | ✅ |
| 4 | CstTransferCostsPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | ✅ |
| 5 | CstTransferCostsPEOCmrPostedFlag | CMR_POSTED_FLAG | — | ✅ |
| 6 | CstTransferCostsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 7 | CstTransferCostsPEOCostDate | COST_DATE | — | ✅ |
| 8 | CstTransferCostsPEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 9 | CstTransferCostsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 10 | CstTransferCostsPEOCostReference | COST_REFERENCE | — | ✅ |
| 11 | CstTransferCostsPEOCostSource | COST_SOURCE | — | ✅ |
| 12 | CstTransferCostsPEOCostTransactionType | COST_TRANSACTION_TYPE | — | ✅ |
| 13 | CstTransferCostsPEOCreatedBy | CREATED_BY | — | ✅ |
| 14 | CstTransferCostsPEOCreationDate | CREATION_DATE | — | ✅ |
| 15 | CstTransferCostsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 16 | CstTransferCostsPEODepTrxnId | DEP_TRXN_ID | — | ✅ |
| 17 | CstTransferCostsPEODistributionId | DISTRIBUTION_ID | — | ✅ |
| 18 | CstTransferCostsPEODistributionType | DISTRIBUTION_TYPE | — | ✅ |
| 19 | CstTransferCostsPEOEffDate | EFF_DATE | — | ✅ |
| 20 | CstTransferCostsPEOExpensePoolId | EXPENSE_POOL_ID | — | ✅ |
| 21 | CstTransferCostsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 22 | CstTransferCostsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | CstTransferCostsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 24 | CstTransferCostsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 25 | CstTransferCostsPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 26 | CstTransferCostsPEOQuantity | QUANTITY | — | ✅ |
| 27 | CstTransferCostsPEORecTrxnId | REC_TRXN_ID | — | ✅ |
| 28 | CstTransferCostsPEOStdCostId | STD_COST_ID | — | ✅ |
| 29 | CstTransferCostsPEOTransactionCostId | TRANSACTION_COST_ID | — | ✅ |
| 30 | CstTransferCostsPEOTransactionId | TRANSACTION_ID | — | ✅ |
| 31 | CstTransferCostsPEOTransferCostId | TRANSFER_COST_ID | 🔑 | ✅ |
| 32 | CstTransferCostsPEOUnitCost | UNIT_COST | — | ✅ |
| 33 | CstTransferCostsPEOUomCode | UOM_CODE | — | ✅ |
| 34 | CstTransferCostsPEOValUnitId | VAL_UNIT_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
