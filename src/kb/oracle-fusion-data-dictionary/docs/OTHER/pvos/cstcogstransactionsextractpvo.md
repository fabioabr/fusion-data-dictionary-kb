---
id: DOC-OTHER-PVO-CstCogsTransactionsExtractPVO
doc_type: system-doc
title: "CstCogsTransactionsExtractPVO — PVO Cross-Module"
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
  - CstCogsTransactionsExtractPVO
  - cstcogstransactionsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstCogsTransactionsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Cogs Transactions Extract. Acessa as tabelas: CST_COGS_TRANSACTIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstCogsTransactionsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 1 | 1 | 27 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cogs_transactions|CST_COGS_TRANSACTIONS]] — 27 atributos (1 PKs, 27 BICC)

---

## ⚙️ Atributos

### [[cst_cogs_transactions|CST_COGS_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstCogsTransactionsPEOAccountingStatus | ACCOUNTING_STATUS | — | ✅ |
| 2 | CstCogsTransactionsPEOCogsPercentage | COGS_PERCENTAGE | — | ✅ |
| 3 | CstCogsTransactionsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 4 | CstCogsTransactionsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 5 | CstCogsTransactionsPEOCostStatus | COST_STATUS | — | ✅ |
| 6 | CstCogsTransactionsPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | CstCogsTransactionsPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | CstCogsTransactionsPEOCstTransactionId | CST_TRANSACTION_ID | — | ✅ |
| 9 | CstCogsTransactionsPEODeliveryId | DELIVERY_ID | — | ✅ |
| 10 | CstCogsTransactionsPEODocumentType | DOCUMENT_TYPE | — | ✅ |
| 11 | CstCogsTransactionsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 12 | CstCogsTransactionsPEOInventoryOrgId | INVENTORY_ORG_ID | — | ✅ |
| 13 | CstCogsTransactionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | CstCogsTransactionsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | CstCogsTransactionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | CstCogsTransactionsPEOLeTimezoneCode | LE_TIMEZONE_CODE | — | ✅ |
| 17 | CstCogsTransactionsPEOPeriodName | PERIOD_NAME | — | ✅ |
| 18 | CstCogsTransactionsPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 19 | CstCogsTransactionsPEORevenueLineId | REVENUE_LINE_ID | — | ✅ |
| 20 | CstCogsTransactionsPEORmaTransactionId | RMA_TRANSACTION_ID | — | ✅ |
| 21 | CstCogsTransactionsPEOShipmentFullfillLineId | SHIPMENT_FULLFILL_LINE_ID | — | ✅ |
| 22 | CstCogsTransactionsPEOTransactionActionId | TRANSACTION_ACTION_ID | — | ✅ |
| 23 | CstCogsTransactionsPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 24 | CstCogsTransactionsPEOTransactionId | TRANSACTION_ID | 🔑 | ✅ |
| 25 | CstCogsTransactionsPEOTransactionSourceTypeId | TRANSACTION_SOURCE_TYPE_ID | — | ✅ |
| 26 | CstCogsTransactionsPEOTransactionTypeId | TRANSACTION_TYPE_ID | — | ✅ |
| 27 | CstCogsTransactionsPEOVariancePostedFlag | VARIANCE_POSTED_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
