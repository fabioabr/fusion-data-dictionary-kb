---
id: DOC-OTHER-PVO-AcctHistoryPVO
doc_type: system-doc
title: "AcctHistoryPVO — PVO Cross-Module"
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
  - AcctHistoryPVO
  - accthistorypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AcctHistoryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Acct History. Acessa as tabelas: CE_ACCT_HISTORY.

**Caminho:** `FscmTopModelAM.FinCeCashTransactionsAM.AcctHistoryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 1 | 1 | 1 | 5% |

---

## 🔗 Tabelas Relacionadas

- [[ce_acct_history|CE_ACCT_HISTORY]] — 22 atributos (1 PKs, 1 BICC)

---

## ⚙️ Atributos

### [[ce_acct_history|CE_ACCT_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcctHistoryAccountingDate | ACCOUNTING_DATE | — | — |
| 2 | AcctHistoryAcctHistoryId | ACCT_HISTORY_ID | 🔑 | ✅ |
| 3 | AcctHistoryClearedAmount | CLEARED_AMOUNT | — | — |
| 4 | AcctHistoryClearedDate | CLEARED_DATE | — | — |
| 5 | AcctHistoryClearedExchangeDate | CLEARED_EXCHANGE_DATE | — | — |
| 6 | AcctHistoryClearedExchangeRate | CLEARED_EXCHANGE_RATE | — | — |
| 7 | AcctHistoryClearedExchangeRateType | CLEARED_EXCHANGE_RATE_TYPE | — | — |
| 8 | AcctHistoryCreatedBy | CREATED_BY | — | — |
| 9 | AcctHistoryCreationDate | CREATION_DATE | — | — |
| 10 | AcctHistoryCurrentRecordFlag | CURRENT_RECORD_FLAG | — | — |
| 11 | AcctHistoryEventId | EVENT_ID | — | — |
| 12 | AcctHistoryEventType | EVENT_TYPE | — | — |
| 13 | AcctHistoryLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 14 | AcctHistoryLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | AcctHistoryLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | AcctHistoryObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | AcctHistoryReversalFirstDistId | REVERSAL_FIRST_DIST_ID | — | — |
| 18 | AcctHistoryReversalIndicatorFlag | REVERSAL_INDICATOR_FLAG | — | — |
| 19 | AcctHistoryReversalSecondDistNum | REVERSAL_SECOND_DIST_NUM | — | — |
| 20 | AcctHistoryStatusCode | STATUS_CODE | — | — |
| 21 | AcctHistoryTransactionId | TRANSACTION_ID | — | — |
| 22 | AcctHistoryTransactionSource | TRANSACTION_SOURCE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
