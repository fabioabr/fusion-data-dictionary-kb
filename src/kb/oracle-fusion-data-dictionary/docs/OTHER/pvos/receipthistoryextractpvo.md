---
id: DOC-OTHER-PVO-ReceiptHistoryExtractPVO
doc_type: system-doc
title: "ReceiptHistoryExtractPVO — PVO Cross-Module"
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
  - ReceiptHistoryExtractPVO
  - receipthistoryextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReceiptHistoryExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Receipt History Extract. Acessa as tabelas: AR_CASH_RECEIPT_HISTORY_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.ReceiptHistoryExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 57 | 1 | 1 | 41 | 72% |

---

## 🔗 Tabelas Relacionadas

- [[ar_cash_receipt_history_all|AR_CASH_RECEIPT_HISTORY_ALL]] — 57 atributos (1 PKs, 41 BICC)

---

## ⚙️ Atributos

### [[ar_cash_receipt_history_all|AR_CASH_RECEIPT_HISTORY_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArCashReceiptHistoryAccountCodeCombinationId | ACCOUNT_CODE_COMBINATION_ID | — | ✅ |
| 2 | ArCashReceiptHistoryAcctdAmount | ACCTD_AMOUNT | — | ✅ |
| 3 | ArCashReceiptHistoryAcctdFactorDiscountAmount | ACCTD_FACTOR_DISCOUNT_AMOUNT | — | ✅ |
| 4 | ArCashReceiptHistoryAmount | AMOUNT | — | ✅ |
| 5 | ArCashReceiptHistoryAttribute1 | ATTRIBUTE1 | — | — |
| 6 | ArCashReceiptHistoryAttribute10 | ATTRIBUTE10 | — | — |
| 7 | ArCashReceiptHistoryAttribute11 | ATTRIBUTE11 | — | — |
| 8 | ArCashReceiptHistoryAttribute12 | ATTRIBUTE12 | — | — |
| 9 | ArCashReceiptHistoryAttribute13 | ATTRIBUTE13 | — | — |
| 10 | ArCashReceiptHistoryAttribute14 | ATTRIBUTE14 | — | — |
| 11 | ArCashReceiptHistoryAttribute15 | ATTRIBUTE15 | — | — |
| 12 | ArCashReceiptHistoryAttribute2 | ATTRIBUTE2 | — | — |
| 13 | ArCashReceiptHistoryAttribute3 | ATTRIBUTE3 | — | — |
| 14 | ArCashReceiptHistoryAttribute4 | ATTRIBUTE4 | — | — |
| 15 | ArCashReceiptHistoryAttribute5 | ATTRIBUTE5 | — | — |
| 16 | ArCashReceiptHistoryAttribute6 | ATTRIBUTE6 | — | — |
| 17 | ArCashReceiptHistoryAttribute7 | ATTRIBUTE7 | — | — |
| 18 | ArCashReceiptHistoryAttribute8 | ATTRIBUTE8 | — | — |
| 19 | ArCashReceiptHistoryAttribute9 | ATTRIBUTE9 | — | — |
| 20 | ArCashReceiptHistoryAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 21 | ArCashReceiptHistoryBankChargeAccountCcid | BANK_CHARGE_ACCOUNT_CCID | — | ✅ |
| 22 | ArCashReceiptHistoryBatchId | BATCH_ID | — | ✅ |
| 23 | ArCashReceiptHistoryCashReceiptHistoryId | CASH_RECEIPT_HISTORY_ID | 🔑 | ✅ |
| 24 | ArCashReceiptHistoryCashReceiptId | CASH_RECEIPT_ID | — | ✅ |
| 25 | ArCashReceiptHistoryCreatedBy | CREATED_BY | — | ✅ |
| 26 | ArCashReceiptHistoryCreatedFrom | CREATED_FROM | — | ✅ |
| 27 | ArCashReceiptHistoryCreationDate | CREATION_DATE | — | ✅ |
| 28 | ArCashReceiptHistoryCurrentRecordFlag | CURRENT_RECORD_FLAG | — | ✅ |
| 29 | ArCashReceiptHistoryEventId | EVENT_ID | — | ✅ |
| 30 | ArCashReceiptHistoryExchangeDate | EXCHANGE_DATE | — | ✅ |
| 31 | ArCashReceiptHistoryExchangeRate | EXCHANGE_RATE | — | ✅ |
| 32 | ArCashReceiptHistoryExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 33 | ArCashReceiptHistoryFactorDiscountAmount | FACTOR_DISCOUNT_AMOUNT | — | ✅ |
| 34 | ArCashReceiptHistoryFactorFlag | FACTOR_FLAG | — | ✅ |
| 35 | ArCashReceiptHistoryFirstPostedRecordFlag | FIRST_POSTED_RECORD_FLAG | — | ✅ |
| 36 | ArCashReceiptHistoryGlDate | GL_DATE | — | ✅ |
| 37 | ArCashReceiptHistoryGlPostedDate | GL_POSTED_DATE | — | ✅ |
| 38 | ArCashReceiptHistoryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 39 | ArCashReceiptHistoryLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 40 | ArCashReceiptHistoryLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 41 | ArCashReceiptHistoryNoteStatus | NOTE_STATUS | — | ✅ |
| 42 | ArCashReceiptHistoryObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 43 | ArCashReceiptHistoryOrgId | ORG_ID | — | ✅ |
| 44 | ArCashReceiptHistoryPostableFlag | POSTABLE_FLAG | — | ✅ |
| 45 | ArCashReceiptHistoryPostingControlId | POSTING_CONTROL_ID | — | ✅ |
| 46 | ArCashReceiptHistoryProgramApplicationId | PROGRAM_APPLICATION_ID | — | ✅ |
| 47 | ArCashReceiptHistoryProgramId | PROGRAM_ID | — | ✅ |
| 48 | ArCashReceiptHistoryProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 49 | ArCashReceiptHistoryPrvStatCashReceiptHistId | PRV_STAT_CASH_RECEIPT_HIST_ID | — | ✅ |
| 50 | ArCashReceiptHistoryRequestId | REQUEST_ID | — | ✅ |
| 51 | ArCashReceiptHistoryReversalCashReceiptHistId | REVERSAL_CASH_RECEIPT_HIST_ID | — | ✅ |
| 52 | ArCashReceiptHistoryReversalCreatedFrom | REVERSAL_CREATED_FROM | — | ✅ |
| 53 | ArCashReceiptHistoryReversalGlDate | REVERSAL_GL_DATE | — | ✅ |
| 54 | ArCashReceiptHistoryReversalGlPostedDate | REVERSAL_GL_POSTED_DATE | — | ✅ |
| 55 | ArCashReceiptHistoryReversalPostingControlId | REVERSAL_POSTING_CONTROL_ID | — | ✅ |
| 56 | ArCashReceiptHistoryStatus | STATUS | — | ✅ |
| 57 | ArCashReceiptHistoryTrxDate | TRX_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
