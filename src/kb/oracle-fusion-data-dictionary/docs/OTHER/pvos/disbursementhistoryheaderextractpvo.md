---
id: DOC-OTHER-PVO-DisbursementHistoryHeaderExtractPVO
doc_type: system-doc
title: "DisbursementHistoryHeaderExtractPVO — PVO Cross-Module"
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
  - DisbursementHistoryHeaderExtractPVO
  - disbursementhistoryheaderextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DisbursementHistoryHeaderExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Disbursement History Header Extract. Acessa as tabelas: AP_PAYMENT_HISTORY_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ApBiccExtractAM.DisbursementHistoryHeaderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 57 | 1 | 1 | 57 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ap_payment_history_all|AP_PAYMENT_HISTORY_ALL]] — 57 atributos (1 PKs, 57 BICC)

---

## ⚙️ Atributos

### [[ap_payment_history_all|AP_PAYMENT_HISTORY_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApPaymentHistoryAllAccountingDate | ACCOUNTING_DATE | — | ✅ |
| 2 | ApPaymentHistoryAllAccountingEventId | ACCOUNTING_EVENT_ID | — | ✅ |
| 3 | ApPaymentHistoryAllBankCurrencyCode | BANK_CURRENCY_CODE | — | ✅ |
| 4 | ApPaymentHistoryAllBankToBaseXrate | BANK_TO_BASE_XRATE | — | ✅ |
| 5 | ApPaymentHistoryAllBankToBaseXrateDate | BANK_TO_BASE_XRATE_DATE | — | ✅ |
| 6 | ApPaymentHistoryAllBankToBaseXrateType | BANK_TO_BASE_XRATE_TYPE | — | ✅ |
| 7 | ApPaymentHistoryAllChargeAmount | CHARGE_AMOUNT | — | ✅ |
| 8 | ApPaymentHistoryAllChargesBankAmount | CHARGES_BANK_AMOUNT | — | ✅ |
| 9 | ApPaymentHistoryAllChargesBaseAmount | CHARGES_BASE_AMOUNT | — | ✅ |
| 10 | ApPaymentHistoryAllChargesPmtAmount | CHARGES_PMT_AMOUNT | — | ✅ |
| 11 | ApPaymentHistoryAllCheckId | CHECK_ID | — | ✅ |
| 12 | ApPaymentHistoryAllCreatedBy | CREATED_BY | — | ✅ |
| 13 | ApPaymentHistoryAllCreationDate | CREATION_DATE | — | ✅ |
| 14 | ApPaymentHistoryAllCurrencyCode | CURRENCY_CODE | — | ✅ |
| 15 | ApPaymentHistoryAllErrorAmount | ERROR_AMOUNT | — | ✅ |
| 16 | ApPaymentHistoryAllErrorsBankAmount | ERRORS_BANK_AMOUNT | — | ✅ |
| 17 | ApPaymentHistoryAllErrorsBaseAmount | ERRORS_BASE_AMOUNT | — | ✅ |
| 18 | ApPaymentHistoryAllErrorsPmtAmount | ERRORS_PMT_AMOUNT | — | ✅ |
| 19 | ApPaymentHistoryAllGainLossIndicator | GAIN_LOSS_INDICATOR | — | ✅ |
| 20 | ApPaymentHistoryAllHistoricalFlag | HISTORICAL_FLAG | — | ✅ |
| 21 | ApPaymentHistoryAllInvoiceAdjustmentEventId | INVOICE_ADJUSTMENT_EVENT_ID | — | ✅ |
| 22 | ApPaymentHistoryAllLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | ApPaymentHistoryAllLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 24 | ApPaymentHistoryAllLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 25 | ApPaymentHistoryAllMatchedFlag | MATCHED_FLAG | — | ✅ |
| 26 | ApPaymentHistoryAllMrcBankToBaseXrate | MRC_BANK_TO_BASE_XRATE | — | ✅ |
| 27 | ApPaymentHistoryAllMrcBankToBaseXrateDate | MRC_BANK_TO_BASE_XRATE_DATE | — | ✅ |
| 28 | ApPaymentHistoryAllMrcBankToBaseXrateType | MRC_BANK_TO_BASE_XRATE_TYPE | — | ✅ |
| 29 | ApPaymentHistoryAllMrcChargesBaseAmount | MRC_CHARGES_BASE_AMOUNT | — | ✅ |
| 30 | ApPaymentHistoryAllMrcErrorsBaseAmount | MRC_ERRORS_BASE_AMOUNT | — | ✅ |
| 31 | ApPaymentHistoryAllMrcExchangeRate | MRC_EXCHANGE_RATE | — | ✅ |
| 32 | ApPaymentHistoryAllMrcExchangeRateDate | MRC_EXCHANGE_RATE_DATE | — | ✅ |
| 33 | ApPaymentHistoryAllMrcExchangeRateType | MRC_EXCHANGE_RATE_TYPE | — | ✅ |
| 34 | ApPaymentHistoryAllMrcPmtToBaseXrate | MRC_PMT_TO_BASE_XRATE | — | ✅ |
| 35 | ApPaymentHistoryAllMrcPmtToBaseXrateDate | MRC_PMT_TO_BASE_XRATE_DATE | — | ✅ |
| 36 | ApPaymentHistoryAllMrcPmtToBaseXrateType | MRC_PMT_TO_BASE_XRATE_TYPE | — | ✅ |
| 37 | ApPaymentHistoryAllMrcTrxBaseAmount | MRC_TRX_BASE_AMOUNT | — | ✅ |
| 38 | ApPaymentHistoryAllObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 39 | ApPaymentHistoryAllOrgId | ORG_ID | — | ✅ |
| 40 | ApPaymentHistoryAllPaymentHistoryId | PAYMENT_HISTORY_ID | 🔑 | ✅ |
| 41 | ApPaymentHistoryAllPmtCurrencyCode | PMT_CURRENCY_CODE | — | ✅ |
| 42 | ApPaymentHistoryAllPmtToBaseXrate | PMT_TO_BASE_XRATE | — | ✅ |
| 43 | ApPaymentHistoryAllPmtToBaseXrateDate | PMT_TO_BASE_XRATE_DATE | — | ✅ |
| 44 | ApPaymentHistoryAllPmtToBaseXrateType | PMT_TO_BASE_XRATE_TYPE | — | ✅ |
| 45 | ApPaymentHistoryAllPostedFlag | POSTED_FLAG | — | ✅ |
| 46 | ApPaymentHistoryAllProgramApplicationId | PROGRAM_APPLICATION_ID | — | ✅ |
| 47 | ApPaymentHistoryAllProgramId | PROGRAM_ID | — | ✅ |
| 48 | ApPaymentHistoryAllProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 49 | ApPaymentHistoryAllRelatedEventId | RELATED_EVENT_ID | — | ✅ |
| 50 | ApPaymentHistoryAllRequestId | REQUEST_ID | — | ✅ |
| 51 | ApPaymentHistoryAllRevPmtHistId | REV_PMT_HIST_ID | — | ✅ |
| 52 | ApPaymentHistoryAllTransactionAmount | TRANSACTION_AMOUNT | — | ✅ |
| 53 | ApPaymentHistoryAllTransactionDate | TRANSACTION_DATE | — | ✅ |
| 54 | ApPaymentHistoryAllTransactionType | TRANSACTION_TYPE | — | ✅ |
| 55 | ApPaymentHistoryAllTrxBankAmount | TRX_BANK_AMOUNT | — | ✅ |
| 56 | ApPaymentHistoryAllTrxBaseAmount | TRX_BASE_AMOUNT | — | ✅ |
| 57 | ApPaymentHistoryAllTrxPmtAmount | TRX_PMT_AMOUNT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
