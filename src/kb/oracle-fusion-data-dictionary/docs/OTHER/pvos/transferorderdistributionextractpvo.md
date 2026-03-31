---
id: DOC-OTHER-PVO-TransferOrderDistributionExtractPVO
doc_type: system-doc
title: "TransferOrderDistributionExtractPVO — PVO Cross-Module"
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
  - TransferOrderDistributionExtractPVO
  - transferorderdistributionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransferOrderDistributionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transfer Order Distribution Extract. Acessa as tabelas: INV_TRANSFER_ORDER_DISTRIBS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.InvBiccExtractAM.TransferOrderDistributionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 33 | 1 | 1 | 21 | 64% |

---

## 🔗 Tabelas Relacionadas

- [[inv_transfer_order_distribs|INV_TRANSFER_ORDER_DISTRIBS]] — 33 atributos (1 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[inv_transfer_order_distribs|INV_TRANSFER_ORDER_DISTRIBS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TODistPEOBudgetDate | BUDGET_DATE | — | ✅ |
| 2 | TODistPEOCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 3 | TODistPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | TODistPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | TODistPEODeliveredQty | DELIVERED_QTY | — | ✅ |
| 6 | TODistPEODistributionAmount | DISTRIBUTION_AMOUNT | — | ✅ |
| 7 | TODistPEODistributionId | DISTRIBUTION_ID | 🔑 | ✅ |
| 8 | TODistPEODistributionNumber | DISTRIBUTION_NUMBER | — | ✅ |
| 9 | TODistPEODistributionQty | DISTRIBUTION_QTY | — | ✅ |
| 10 | TODistPEOFundsStatus | FUNDS_STATUS | — | ✅ |
| 11 | TODistPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | TODistPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | TODistPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | TODistPEOLineId | LINE_ID | — | ✅ |
| 15 | TODistPEONonrecoverableTax | NONRECOVERABLE_TAX | — | ✅ |
| 16 | TODistPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | TODistPEOPercent | PERCENT | — | ✅ |
| 18 | TODistPEOPjcBillableFlag | PJC_BILLABLE_FLAG | — | — |
| 19 | TODistPEOPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | — |
| 20 | TODistPEOPjcContextCategory | PJC_CONTEXT_CATEGORY | — | — |
| 21 | TODistPEOPjcContractId | PJC_CONTRACT_ID | — | — |
| 22 | TODistPEOPjcContractLineId | PJC_CONTRACT_LINE_ID | — | — |
| 23 | TODistPEOPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 24 | TODistPEOPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | — |
| 25 | TODistPEOPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | — |
| 26 | TODistPEOPjcOrganizationId | PJC_ORGANIZATION_ID | — | — |
| 27 | TODistPEOPjcProjectId | PJC_PROJECT_ID | — | — |
| 28 | TODistPEOPjcTaskId | PJC_TASK_ID | — | — |
| 29 | TODistPEOPjcWorkTypeId | PJC_WORK_TYPE_ID | — | — |
| 30 | TODistPEOPrimaryLedgerId | PRIMARY_LEDGER_ID | — | ✅ |
| 31 | TODistPEORecoverableTax | RECOVERABLE_TAX | — | ✅ |
| 32 | TODistPEOReqBuId | REQ_BU_ID | — | ✅ |
| 33 | TODistPEOReqDistributionId | REQ_DISTRIBUTION_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
