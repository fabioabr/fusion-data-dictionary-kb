---
id: DOC-OTHER-PVO-InterestHeaderExtractPVO
doc_type: system-doc
title: "InterestHeaderExtractPVO — PVO Cross-Module"
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
  - InterestHeaderExtractPVO
  - interestheaderextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InterestHeaderExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Interest Header Extract. Acessa as tabelas: AR_INTEREST_HEADERS_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.InterestHeaderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 55 | 1 | 1 | 55 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ar_interest_headers_all|AR_INTEREST_HEADERS_ALL]] — 55 atributos (1 PKs, 55 BICC)

---

## ⚙️ Atributos

### [[ar_interest_headers_all|AR_INTEREST_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArInterestHeaderChargeBeginDate | CHARGE_BEGIN_DATE | — | ✅ |
| 2 | ArInterestHeaderChargeOnFinanceChargeFlag | CHARGE_ON_FINANCE_CHARGE_FLAG | — | ✅ |
| 3 | ArInterestHeaderCollectorId | COLLECTOR_ID | — | ✅ |
| 4 | ArInterestHeaderCreatedBy | CREATED_BY | — | ✅ |
| 5 | ArInterestHeaderCreationDate | CREATION_DATE | — | ✅ |
| 6 | ArInterestHeaderCreditItemsFlag | CREDIT_ITEMS_FLAG | — | ✅ |
| 7 | ArInterestHeaderCurrencyCode | CURRENCY_CODE | — | ✅ |
| 8 | ArInterestHeaderCustAcctProfileAmtId | CUST_ACCT_PROFILE_AMT_ID | — | ✅ |
| 9 | ArInterestHeaderCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | ✅ |
| 10 | ArInterestHeaderCustomerId | CUSTOMER_ID | — | ✅ |
| 11 | ArInterestHeaderCustomerProfileId | CUSTOMER_PROFILE_ID | — | ✅ |
| 12 | ArInterestHeaderCustomerSiteUseId | CUSTOMER_SITE_USE_ID | — | ✅ |
| 13 | ArInterestHeaderDisplayFlag | DISPLAY_FLAG | — | ✅ |
| 14 | ArInterestHeaderDisputedTransactionsFlag | DISPUTED_TRANSACTIONS_FLAG | — | ✅ |
| 15 | ArInterestHeaderExchangeRate | EXCHANGE_RATE | — | ✅ |
| 16 | ArInterestHeaderExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 17 | ArInterestHeaderFinanceChargeDate | FINANCE_CHARGE_DATE | — | ✅ |
| 18 | ArInterestHeaderHeaderType | HEADER_TYPE | — | ✅ |
| 19 | ArInterestHeaderHoldChargedInvoicesFlag | HOLD_CHARGED_INVOICES_FLAG | — | ✅ |
| 20 | ArInterestHeaderInterestBatchId | INTEREST_BATCH_ID | — | ✅ |
| 21 | ArInterestHeaderInterestCalculationPeriod | INTEREST_CALCULATION_PERIOD | — | ✅ |
| 22 | ArInterestHeaderInterestFixedAmount | INTEREST_FIXED_AMOUNT | — | ✅ |
| 23 | ArInterestHeaderInterestHeaderId | INTEREST_HEADER_ID | 🔑 | ✅ |
| 24 | ArInterestHeaderInterestPeriodDays | INTEREST_PERIOD_DAYS | — | ✅ |
| 25 | ArInterestHeaderInterestRate | INTEREST_RATE | — | ✅ |
| 26 | ArInterestHeaderInterestScheduleId | INTEREST_SCHEDULE_ID | — | ✅ |
| 27 | ArInterestHeaderInterestType | INTEREST_TYPE | — | ✅ |
| 28 | ArInterestHeaderLastAccrueChargeDate | LAST_ACCRUE_CHARGE_DATE | — | ✅ |
| 29 | ArInterestHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | ArInterestHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 31 | ArInterestHeaderLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 32 | ArInterestHeaderLateChargeCalculationTrx | LATE_CHARGE_CALCULATION_TRX | — | ✅ |
| 33 | ArInterestHeaderLateChargeTermId | LATE_CHARGE_TERM_ID | — | ✅ |
| 34 | ArInterestHeaderLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 35 | ArInterestHeaderMaxInterestCharge | MAX_INTEREST_CHARGE | — | ✅ |
| 36 | ArInterestHeaderMessageTextId | MESSAGE_TEXT_ID | — | ✅ |
| 37 | ArInterestHeaderMinFcBalanceAmount | MIN_FC_BALANCE_AMOUNT | — | ✅ |
| 38 | ArInterestHeaderMinFcBalanceOverdueType | MIN_FC_BALANCE_OVERDUE_TYPE | — | ✅ |
| 39 | ArInterestHeaderMinFcBalancePercent | MIN_FC_BALANCE_PERCENT | — | ✅ |
| 40 | ArInterestHeaderMinFcInvoiceAmount | MIN_FC_INVOICE_AMOUNT | — | ✅ |
| 41 | ArInterestHeaderMinFcInvoiceOverdueType | MIN_FC_INVOICE_OVERDUE_TYPE | — | ✅ |
| 42 | ArInterestHeaderMinFcInvoicePercent | MIN_FC_INVOICE_PERCENT | — | ✅ |
| 43 | ArInterestHeaderMinInterestCharge | MIN_INTEREST_CHARGE | — | ✅ |
| 44 | ArInterestHeaderMultipleInterestRatesFlag | MULTIPLE_INTEREST_RATES_FLAG | — | ✅ |
| 45 | ArInterestHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 46 | ArInterestHeaderOrgId | ORG_ID | — | ✅ |
| 47 | ArInterestHeaderPaymentGraceDays | PAYMENT_GRACE_DAYS | — | ✅ |
| 48 | ArInterestHeaderPenaltyFixedAmount | PENALTY_FIXED_AMOUNT | — | ✅ |
| 49 | ArInterestHeaderPenaltyRate | PENALTY_RATE | — | ✅ |
| 50 | ArInterestHeaderPenaltyScheduleId | PENALTY_SCHEDULE_ID | — | ✅ |
| 51 | ArInterestHeaderPenaltyType | PENALTY_TYPE | — | ✅ |
| 52 | ArInterestHeaderProcessMessage | PROCESS_MESSAGE | — | ✅ |
| 53 | ArInterestHeaderProcessStatus | PROCESS_STATUS | — | ✅ |
| 54 | ArInterestHeaderRequestId | REQUEST_ID | — | ✅ |
| 55 | ArInterestHeaderWorkerNum | WORKER_NUM | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
