---
id: DOC-OTHER-PVO-InterestLineExtractPVO
doc_type: system-doc
title: "InterestLineExtractPVO — PVO Cross-Module"
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
  - InterestLineExtractPVO
  - interestlineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InterestLineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Interest Line Extract. Acessa as tabelas: AR_INTEREST_LINES_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.InterestLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 33 | 1 | 1 | 33 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ar_interest_lines_all|AR_INTEREST_LINES_ALL]] — 33 atributos (1 PKs, 33 BICC)

---

## ⚙️ Atributos

### [[ar_interest_lines_all|AR_INTEREST_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArInterestLineActualDateClosed | ACTUAL_DATE_CLOSED | — | ✅ |
| 2 | ArInterestLineAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | ✅ |
| 3 | ArInterestLineAmountDueRemaining | AMOUNT_DUE_REMAINING | — | ✅ |
| 4 | ArInterestLineCreatedBy | CREATED_BY | — | ✅ |
| 5 | ArInterestLineCreationDate | CREATION_DATE | — | ✅ |
| 6 | ArInterestLineDaysOfInterest | DAYS_OF_INTEREST | — | ✅ |
| 7 | ArInterestLineDaysOverdueLate | DAYS_OVERDUE_LATE | — | ✅ |
| 8 | ArInterestLineDueDate | DUE_DATE | — | ✅ |
| 9 | ArInterestLineFinanceChargeCharged | FINANCE_CHARGE_CHARGED | — | ✅ |
| 10 | ArInterestLineInterestCharged | INTEREST_CHARGED | — | ✅ |
| 11 | ArInterestLineInterestHeaderId | INTEREST_HEADER_ID | — | ✅ |
| 12 | ArInterestLineInterestLineId | INTEREST_LINE_ID | 🔑 | ✅ |
| 13 | ArInterestLineInterestRate | INTEREST_RATE | — | ✅ |
| 14 | ArInterestLineLastChargeDate | LAST_CHARGE_DATE | — | ✅ |
| 15 | ArInterestLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | ArInterestLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | ArInterestLineLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | ArInterestLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 19 | ArInterestLineOrgId | ORG_ID | — | ✅ |
| 20 | ArInterestLineOriginalTrxClass | ORIGINAL_TRX_CLASS | — | ✅ |
| 21 | ArInterestLineOriginalTrxId | ORIGINAL_TRX_ID | — | ✅ |
| 22 | ArInterestLineOutstandingAmount | OUTSTANDING_AMOUNT | — | ✅ |
| 23 | ArInterestLinePaymentDate | PAYMENT_DATE | — | ✅ |
| 24 | ArInterestLinePaymentScheduleId | PAYMENT_SCHEDULE_ID | — | ✅ |
| 25 | ArInterestLineProcessMessage | PROCESS_MESSAGE | — | ✅ |
| 26 | ArInterestLineProcessStatus | PROCESS_STATUS | — | ✅ |
| 27 | ArInterestLineRateEndDate | RATE_END_DATE | — | ✅ |
| 28 | ArInterestLineRateStartDate | RATE_START_DATE | — | ✅ |
| 29 | ArInterestLineReceivablesTrxId | RECEIVABLES_TRX_ID | — | ✅ |
| 30 | ArInterestLineScheduleDaysFrom | SCHEDULE_DAYS_FROM | — | ✅ |
| 31 | ArInterestLineScheduleDaysTo | SCHEDULE_DAYS_TO | — | ✅ |
| 32 | ArInterestLineType | TYPE | — | ✅ |
| 33 | DailyInterestCharge | DAILY_INTEREST_CHARGE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
