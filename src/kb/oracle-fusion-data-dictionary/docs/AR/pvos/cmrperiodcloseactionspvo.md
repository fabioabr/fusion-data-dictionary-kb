---
id: DOC-AR-PVO-CmrPeriodCloseActionsPVO
doc_type: system-doc
title: "CmrPeriodCloseActionsPVO — PVO Accounts Receivable"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ar
  - data-dictionary
  - pvo
  - bicc
aliases:
  - CmrPeriodCloseActionsPVO
  - cmrperiodcloseactionspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrPeriodCloseActionsPVO

## 📌 Visão Geral

Extrai as ações de fechamento de período do módulo de Contas a Receber, com status e detalhes de execução. Controla o checklist de atividades necessárias para concluir o fechamento contábil mensal.

**Caminho:** `FscmTopModelAM.ReceiptAccountingAM.CmrPeriodCloseActionsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 1 | 2 | 25 | 86% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_period_close_actions_v|CMR_PERIOD_CLOSE_ACTIONS_V]] — 29 atributos (2 PKs, 25 BICC)

---

## ⚙️ Atributos

### [[cmr_period_close_actions_v|CMR_PERIOD_CLOSE_ACTIONS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrPeriodCloseActionsPEOBuId | BU_ID | 🔑 | ✅ |
| 2 | CmrPeriodCloseActionsPEOEndDate | END_DATE | — | ✅ |
| 3 | CmrPeriodCloseActionsPEOIntransitPoAccJobFlag | INTRANSIT_PO_ACC_JOB_FLAG | — | — |
| 4 | CmrPeriodCloseActionsPEOIntransitPoRptNotAccCount | INTRANSIT_PO_RPT_NOT_ACC_COUNT | — | — |
| 5 | CmrPeriodCloseActionsPEOLeTimeOffset | LE_TIME_OFFSET | — | ✅ |
| 6 | CmrPeriodCloseActionsPEOLedgerId | LEDGER_ID | — | ✅ |
| 7 | CmrPeriodCloseActionsPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 8 | CmrPeriodCloseActionsPEOPendingAccrClrCount | PENDING_ACCR_CLR_COUNT | — | ✅ |
| 9 | CmrPeriodCloseActionsPEOPendingDistCount | PENDING_DIST_COUNT | — | ✅ |
| 10 | CmrPeriodCloseActionsPEOPendingIntReversalsCount | PENDING_INT_REVERSALS_COUNT | — | — |
| 11 | CmrPeriodCloseActionsPEOPendingInvoiceIntfCount | PENDING_INVOICE_INTF_COUNT | — | ✅ |
| 12 | CmrPeriodCloseActionsPEOPendingInvoiceVarCount | PENDING_INVOICE_VAR_COUNT | — | ✅ |
| 13 | CmrPeriodCloseActionsPEOPendingPeriodAccrCount | PENDING_PERIOD_ACCR_COUNT | — | ✅ |
| 14 | CmrPeriodCloseActionsPEOPendingReceiptCount | PENDING_RECEIPT_COUNT | — | ✅ |
| 15 | CmrPeriodCloseActionsPEOPendingReceiptIntfCount | PENDING_RECEIPT_INTF_COUNT | — | ✅ |
| 16 | CmrPeriodCloseActionsPEOPendingRpaCount | PENDING_RPA_COUNT | — | ✅ |
| 17 | CmrPeriodCloseActionsPEOPendingTraCount | PENDING_TRA_COUNT | — | ✅ |
| 18 | CmrPeriodCloseActionsPEOPendingTraIntfCount | PENDING_TRA_INTF_COUNT | — | ✅ |
| 19 | CmrPeriodCloseActionsPEOPeriodName | PERIOD_NAME | 🔑 | ✅ |
| 20 | CmrPeriodCloseActionsPEOPeriodNum | PERIOD_NUM | — | ✅ |
| 21 | CmrPeriodCloseActionsPEOPeriodSetName | PERIOD_SET_NAME | — | ✅ |
| 22 | CmrPeriodCloseActionsPEOPeriodType | PERIOD_TYPE | — | ✅ |
| 23 | CmrPeriodCloseActionsPEOPeriodYear | PERIOD_YEAR | — | ✅ |
| 24 | CmrPeriodCloseActionsPEOServerEndDate | SERVER_END_DATE | — | ✅ |
| 25 | CmrPeriodCloseActionsPEOServerStartDate | SERVER_START_DATE | — | ✅ |
| 26 | CmrPeriodCloseActionsPEOStartDate | START_DATE | — | ✅ |
| 27 | CmrPeriodCloseActionsPEOUnimportedInvoiceCount | UNIMPORTED_INVOICE_COUNT | — | ✅ |
| 28 | CmrPeriodCloseActionsPEOUnimportedReceiptCount | UNIMPORTED_RECEIPT_COUNT | — | ✅ |
| 29 | CmrPeriodCloseActionsPEOUninterfacedIntShptsCount | UNINTERFACED_INT_SHPTS_COUNT | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
