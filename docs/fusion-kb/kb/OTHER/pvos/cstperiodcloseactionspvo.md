---
id: DOC-OTHER-PVO-CstPeriodCloseActionsPVO
doc_type: system-doc
title: "CstPeriodCloseActionsPVO — PVO Cross-Module"
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
  - CstPeriodCloseActionsPVO
  - cstperiodcloseactionspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstPeriodCloseActionsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Period Close Actions. Acessa as tabelas: CST_PERIOD_CLOSE_ACTIONS.

**Caminho:** `FscmTopModelAM.CstPeriodStatusAM.CstPeriodCloseActionsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 42 | 1 | 1 | 34 | 81% |

---

## 🔗 Tabelas Relacionadas

- [[cst_period_close_actions|CST_PERIOD_CLOSE_ACTIONS]] — 42 atributos (1 PKs, 34 BICC)

---

## ⚙️ Atributos

### [[cst_period_close_actions|CST_PERIOD_CLOSE_ACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CitePendingCount | CITE_PENDING_COUNT | — | — |
| 2 | CstPeriodCloseActionsPEOArErrorsCount | AR_ERRORS_COUNT | — | ✅ |
| 3 | CstPeriodCloseActionsPEOArPendingCount | AR_PENDING_COUNT | — | ✅ |
| 4 | CstPeriodCloseActionsPEOComplWoNotClosed | COMPL_WO_NOT_CLOSED | — | ✅ |
| 5 | CstPeriodCloseActionsPEOComplWoPendingCount | COMPL_WO_PENDING_COUNT | — | ✅ |
| 6 | CstPeriodCloseActionsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 7 | CstPeriodCloseActionsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 8 | CstPeriodCloseActionsPEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | CstPeriodCloseActionsPEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | CstPeriodCloseActionsPEOCstInvOnhandMismatchQty | CST_INV_ONHAND_MISMATCH_QTY | — | ✅ |
| 11 | CstPeriodCloseActionsPEODistributionErrorsCount | DISTRIBUTION_ERRORS_COUNT | — | ✅ |
| 12 | CstPeriodCloseActionsPEODistributionPendingCount | DISTRIBUTION_PENDING_COUNT | — | ✅ |
| 13 | CstPeriodCloseActionsPEOFromStatusCode | FROM_STATUS_CODE | — | ✅ |
| 14 | CstPeriodCloseActionsPEOInvErrorsCount | INV_ERRORS_COUNT | — | ✅ |
| 15 | CstPeriodCloseActionsPEOInvPendingCount | INV_PENDING_COUNT | — | ✅ |
| 16 | CstPeriodCloseActionsPEOJournalsErrorsCount | JOURNALS_ERRORS_COUNT | — | ✅ |
| 17 | CstPeriodCloseActionsPEOJournalsPendingCount | JOURNALS_PENDING_COUNT | — | ✅ |
| 18 | CstPeriodCloseActionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | CstPeriodCloseActionsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 20 | CstPeriodCloseActionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 21 | CstPeriodCloseActionsPEOMatchInvOnhandWithCst | MATCH_INV_ONHAND_WITH_CST | — | ✅ |
| 22 | CstPeriodCloseActionsPEOPendScenarioAbsCount | PEND_SCENARIO_ABS_COUNT | — | — |
| 23 | CstPeriodCloseActionsPEOPendingDcogsTransactions | PENDING_DCOGS_TRANSACTIONS | — | ✅ |
| 24 | CstPeriodCloseActionsPEOPendingInterfaceTxns | PENDING_INTERFACE_TXNS | — | ✅ |
| 25 | CstPeriodCloseActionsPEOPendingIntfTxnCount | PENDING_INTF_TXN_COUNT | — | ✅ |
| 26 | CstPeriodCloseActionsPEOPendingScenarioAbsorption | PENDING_SCENARIO_ABSORPTION | — | — |
| 27 | CstPeriodCloseActionsPEOPeriodName | PERIOD_NAME | — | ✅ |
| 28 | CstPeriodCloseActionsPEOProcessStartDate | PROCESS_START_DATE | — | ✅ |
| 29 | CstPeriodCloseActionsPEOProcessStatusCode | PROCESS_STATUS_CODE | — | ✅ |
| 30 | CstPeriodCloseActionsPEORunId | RUN_ID | 🔑 | ✅ |
| 31 | CstPeriodCloseActionsPEOToStatusCode | TO_STATUS_CODE | — | ✅ |
| 32 | CstPeriodCloseActionsPEOUncostedTransactions | UNCOSTED_TRANSACTIONS | — | ✅ |
| 33 | CstPeriodCloseActionsPEOUncostedTxnCount | UNCOSTED_TXN_COUNT | — | ✅ |
| 34 | CstPeriodCloseActionsPEOUnimportedInvTransactions | UNIMPORTED_INV_TRANSACTIONS | — | ✅ |
| 35 | CstPeriodCloseActionsPEOUnprocessedDistributions | UNPROCESSED_DISTRIBUTIONS | — | ✅ |
| 36 | CstPeriodCloseActionsPEOUnprocessedJournals | UNPROCESSED_JOURNALS | — | ✅ |
| 37 | CstPeriodCloseActionsPEOWipPendingCount | WIP_PENDING_COUNT | — | ✅ |
| 38 | CtePendingCount | CTE_PENDING_COUNT | — | — |
| 39 | PendAcctEventsCount | PEND_ACCT_EVENTS_COUNT | — | — |
| 40 | PendOhRatesAbsCount | PEND_OH_RATES_ABS_COUNT | — | — |
| 41 | PendingAccountingEvents | PENDING_ACCOUNTING_EVENTS | — | — |
| 42 | PendingOhRatesAbsorption | PENDING_OH_RATES_ABSORPTION | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
