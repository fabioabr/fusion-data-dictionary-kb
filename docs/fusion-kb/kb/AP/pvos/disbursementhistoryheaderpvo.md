---
id: DOC-AP-PVO-DisbursementHistoryHeaderPVO
doc_type: system-doc
title: "DisbursementHistoryHeaderPVO — PVO Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ap
  - data-dictionary
  - pvo
  - bicc
aliases:
  - DisbursementHistoryHeaderPVO
  - disbursementhistoryheaderpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DisbursementHistoryHeaderPVO

## 📌 Visão Geral

Extrai o histórico de eventos dos desembolsos (compensação, cancelamento, estorno), incluindo datas, valores e unidade de negócio. Permite rastrear o ciclo de vida completo de cada pagamento e suportar auditorias de tesouraria.

**Caminho:** `FscmTopModelAM.FinApPmtSinglePaymentsAM.DisbursementHistoryHeaderPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 61 | 3 | 1 | 21 | 34% |

---

## 🔗 Tabelas Relacionadas

- [[ap_payment_history_all|AP_PAYMENT_HISTORY_ALL]] — 57 atributos (1 PKs, 21 BICC)
- [[ap_system_parameters_all|AP_SYSTEM_PARAMETERS_ALL]] — 3 atributos
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 1 atributos

---

## ⚙️ Atributos

### [[ap_payment_history_all|AP_PAYMENT_HISTORY_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentHistoryAccountingDate | ACCOUNTING_DATE | — | ✅ |
| 2 | PaymentHistoryAccountingEventId | ACCOUNTING_EVENT_ID | — | — |
| 3 | PaymentHistoryBankCurrencyCode | BANK_CURRENCY_CODE | — | ✅ |
| 4 | PaymentHistoryBankToBaseXrate | BANK_TO_BASE_XRATE | — | ✅ |
| 5 | PaymentHistoryBankToBaseXrateDate | BANK_TO_BASE_XRATE_DATE | — | ✅ |
| 6 | PaymentHistoryBankToBaseXrateType | BANK_TO_BASE_XRATE_TYPE | — | ✅ |
| 7 | PaymentHistoryChargeAmount | CHARGE_AMOUNT | — | — |
| 8 | PaymentHistoryChargesBankAmount | CHARGES_BANK_AMOUNT | — | — |
| 9 | PaymentHistoryChargesBaseAmount | CHARGES_BASE_AMOUNT | — | — |
| 10 | PaymentHistoryChargesPmtAmount | CHARGES_PMT_AMOUNT | — | — |
| 11 | PaymentHistoryCheckId | CHECK_ID | — | — |
| 12 | PaymentHistoryCreatedBy | CREATED_BY | — | — |
| 13 | PaymentHistoryCreationDate | CREATION_DATE | — | — |
| 14 | PaymentHistoryCurrencyCode | CURRENCY_CODE | — | ✅ |
| 15 | PaymentHistoryErrorAmount | ERROR_AMOUNT | — | — |
| 16 | PaymentHistoryErrorsBankAmount | ERRORS_BANK_AMOUNT | — | — |
| 17 | PaymentHistoryErrorsBaseAmount | ERRORS_BASE_AMOUNT | — | — |
| 18 | PaymentHistoryErrorsPmtAmount | ERRORS_PMT_AMOUNT | — | — |
| 19 | PaymentHistoryGainLossIndicator | GAIN_LOSS_INDICATOR | — | ✅ |
| 20 | PaymentHistoryHistoricalFlag | HISTORICAL_FLAG | — | — |
| 21 | PaymentHistoryId | PAYMENT_HISTORY_ID | 🔑 | ✅ |
| 22 | PaymentHistoryInvoiceAdjustmentEventId | INVOICE_ADJUSTMENT_EVENT_ID | — | — |
| 23 | PaymentHistoryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | PaymentHistoryLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 25 | PaymentHistoryLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 26 | PaymentHistoryMatchedFlag | MATCHED_FLAG | — | ✅ |
| 27 | PaymentHistoryMrcBankToBaseXrate | MRC_BANK_TO_BASE_XRATE | — | — |
| 28 | PaymentHistoryMrcBankToBaseXrateDate | MRC_BANK_TO_BASE_XRATE_DATE | — | — |
| 29 | PaymentHistoryMrcBankToBaseXrateType | MRC_BANK_TO_BASE_XRATE_TYPE | — | — |
| 30 | PaymentHistoryMrcChargesBaseAmount | MRC_CHARGES_BASE_AMOUNT | — | — |
| 31 | PaymentHistoryMrcErrorsBaseAmount | MRC_ERRORS_BASE_AMOUNT | — | — |
| 32 | PaymentHistoryMrcExchangeRate | MRC_EXCHANGE_RATE | — | — |
| 33 | PaymentHistoryMrcExchangeRateDate | MRC_EXCHANGE_RATE_DATE | — | — |
| 34 | PaymentHistoryMrcExchangeRateType | MRC_EXCHANGE_RATE_TYPE | — | — |
| 35 | PaymentHistoryMrcPmtToBaseXrate | MRC_PMT_TO_BASE_XRATE | — | — |
| 36 | PaymentHistoryMrcPmtToBaseXrateDate | MRC_PMT_TO_BASE_XRATE_DATE | — | — |
| 37 | PaymentHistoryMrcPmtToBaseXrateType | MRC_PMT_TO_BASE_XRATE_TYPE | — | — |
| 38 | PaymentHistoryMrcTrxBaseAmount | MRC_TRX_BASE_AMOUNT | — | — |
| 39 | PaymentHistoryObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 40 | PaymentHistoryOrgId | ORG_ID | — | — |
| 41 | PaymentHistoryPmtCurrencyCode | PMT_CURRENCY_CODE | — | ✅ |
| 42 | PaymentHistoryPmtToBaseXrate | PMT_TO_BASE_XRATE | — | ✅ |
| 43 | PaymentHistoryPmtToBaseXrateDate | PMT_TO_BASE_XRATE_DATE | — | ✅ |
| 44 | PaymentHistoryPmtToBaseXrateType | PMT_TO_BASE_XRATE_TYPE | — | ✅ |
| 45 | PaymentHistoryPostedFlag | POSTED_FLAG | — | ✅ |
| 46 | PaymentHistoryProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 47 | PaymentHistoryProgramId | PROGRAM_ID | — | — |
| 48 | PaymentHistoryProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 49 | PaymentHistoryRelatedEventId | RELATED_EVENT_ID | — | — |
| 50 | PaymentHistoryRequestId | REQUEST_ID | — | — |
| 51 | PaymentHistoryRevPmtHistId | REV_PMT_HIST_ID | — | — |
| 52 | PaymentHistoryTransactionAmount | TRANSACTION_AMOUNT | — | ✅ |
| 53 | PaymentHistoryTransactionDate | TRANSACTION_DATE | — | ✅ |
| 54 | PaymentHistoryTransactionType | TRANSACTION_TYPE | — | ✅ |
| 55 | PaymentHistoryTrxBankAmount | TRX_BANK_AMOUNT | — | ✅ |
| 56 | PaymentHistoryTrxBaseAmount | TRX_BASE_AMOUNT | — | ✅ |
| 57 | PaymentHistoryTrxPmtAmount | TRX_PMT_AMOUNT | — | ✅ |

### [[ap_system_parameters_all|AP_SYSTEM_PARAMETERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SystemOptionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | SystemOptionOrgId | ORG_ID | — | — |
| 3 | SystemOptionWhenToAccountPmt | WHEN_TO_ACCOUNT_PMT | — | — |

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitId | BU_ID | — | — |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
