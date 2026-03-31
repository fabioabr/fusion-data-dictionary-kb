---
id: DOC-OTHER-PVO-CstInvoiceToExpTxnsExtractPVO
doc_type: system-doc
title: "CstInvoiceToExpTxnsExtractPVO — PVO Cross-Module"
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
  - CstInvoiceToExpTxnsExtractPVO
  - cstinvoicetoexptxnsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstInvoiceToExpTxnsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Invoice To Exp Txns Extract. Acessa as tabelas: CST_INVOICE_TO_EXP_TXNS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstInvoiceToExpTxnsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 1 | 1 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_invoice_to_exp_txns|CST_INVOICE_TO_EXP_TXNS]] — 21 atributos (1 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[cst_invoice_to_exp_txns|CST_INVOICE_TO_EXP_TXNS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstInvoiceToExpTxnsPEOCmrPoDistributionId | CMR_PO_DISTRIBUTION_ID | — | ✅ |
| 2 | CstInvoiceToExpTxnsPEOCmrPoLineLocationId | CMR_PO_LINE_LOCATION_ID | — | ✅ |
| 3 | CstInvoiceToExpTxnsPEOCmrRcvTransactionId | CMR_RCV_TRANSACTION_ID | — | ✅ |
| 4 | CstInvoiceToExpTxnsPEOConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 5 | CstInvoiceToExpTxnsPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | CstInvoiceToExpTxnsPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | CstInvoiceToExpTxnsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 8 | CstInvoiceToExpTxnsPEOCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 9 | CstInvoiceToExpTxnsPEOCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 10 | CstInvoiceToExpTxnsPEOCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 11 | CstInvoiceToExpTxnsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 12 | CstInvoiceToExpTxnsPEOInventoryOrgId | INVENTORY_ORG_ID | — | ✅ |
| 13 | CstInvoiceToExpTxnsPEOInvoiceToExpAmt | INVOICE_TO_EXP_AMT | — | ✅ |
| 14 | CstInvoiceToExpTxnsPEOInvoiceToExpTxnId | INVOICE_TO_EXP_TXN_ID | 🔑 | ✅ |
| 15 | CstInvoiceToExpTxnsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | CstInvoiceToExpTxnsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | CstInvoiceToExpTxnsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | CstInvoiceToExpTxnsPEOPreprocessedFlag | PREPROCESSED_FLAG | — | ✅ |
| 19 | CstInvoiceToExpTxnsPEOReverseInvoiceToExpTxnId | REVERSE_INVOICE_TO_EXP_TXN_ID | — | ✅ |
| 20 | CstInvoiceToExpTxnsPEOTransactionFlowType | TRANSACTION_FLOW_TYPE | — | ✅ |
| 21 | CstInvoiceToExpTxnsPEOTxnAccountDate | TXN_ACCOUNT_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
