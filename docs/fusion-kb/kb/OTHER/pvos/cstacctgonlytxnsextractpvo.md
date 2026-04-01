---
id: DOC-OTHER-PVO-CstAcctgOnlyTxnsExtractPVO
doc_type: system-doc
title: "CstAcctgOnlyTxnsExtractPVO — PVO Cross-Module"
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
  - CstAcctgOnlyTxnsExtractPVO
  - cstacctgonlytxnsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstAcctgOnlyTxnsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Acctg Only Txns Extract. Acessa as tabelas: CST_ACCTG_ONLY_TXNS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstAcctgOnlyTxnsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 1 | 1 | 24 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_acctg_only_txns|CST_ACCTG_ONLY_TXNS]] — 24 atributos (1 PKs, 24 BICC)

---

## ⚙️ Atributos

### [[cst_acctg_only_txns|CST_ACCTG_ONLY_TXNS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstAcctgOnlyTxnsPEOAccountingStatus | ACCOUNTING_STATUS | — | ✅ |
| 2 | CstAcctgOnlyTxnsPEOAcctgOnlyTxnsId | ACCTG_ONLY_TXNS_ID | 🔑 | ✅ |
| 3 | CstAcctgOnlyTxnsPEOConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 4 | CstAcctgOnlyTxnsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 5 | CstAcctgOnlyTxnsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 6 | CstAcctgOnlyTxnsPEOCostStatus | COST_STATUS | — | ✅ |
| 7 | CstAcctgOnlyTxnsPEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | CstAcctgOnlyTxnsPEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | CstAcctgOnlyTxnsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 10 | CstAcctgOnlyTxnsPEODistributionId | DISTRIBUTION_ID | — | ✅ |
| 11 | CstAcctgOnlyTxnsPEOEntityCode | ENTITY_CODE | — | ✅ |
| 12 | CstAcctgOnlyTxnsPEOEventClassCode | EVENT_CLASS_CODE | — | ✅ |
| 13 | CstAcctgOnlyTxnsPEOEventTypeCode | EVENT_TYPE_CODE | — | ✅ |
| 14 | CstAcctgOnlyTxnsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 15 | CstAcctgOnlyTxnsPEOInventoryOrgId | INVENTORY_ORG_ID | — | ✅ |
| 16 | CstAcctgOnlyTxnsPEOInvoiceToExpAmt | INVOICE_TO_EXP_AMT | — | ✅ |
| 17 | CstAcctgOnlyTxnsPEOInvoiceToExpTxnId | INVOICE_TO_EXP_TXN_ID | — | ✅ |
| 18 | CstAcctgOnlyTxnsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | CstAcctgOnlyTxnsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 20 | CstAcctgOnlyTxnsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 21 | CstAcctgOnlyTxnsPEOLeTimezoneCode | LE_TIMEZONE_CODE | — | ✅ |
| 22 | CstAcctgOnlyTxnsPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 23 | CstAcctgOnlyTxnsPEOTransactionFlowType | TRANSACTION_FLOW_TYPE | — | ✅ |
| 24 | CstAcctgOnlyTxnsPEOTxnAccountDate | TXN_ACCOUNT_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
