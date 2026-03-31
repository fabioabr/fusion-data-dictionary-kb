---
id: DOC-AR-PVO-DisputeHistoryPVO
doc_type: system-doc
title: "DisputeHistoryPVO — PVO Accounts Receivable"
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
  - DisputeHistoryPVO
  - disputehistorypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DisputeHistoryPVO

## 📌 Visão Geral

Extrai o histórico de disputas (contestações) sobre transações de Contas a Receber, com datas, valores e status. Fundamental para gestão de litígios comerciais, acompanhamento de SLA de resolução e análise de causas raiz de contestações.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.DisputeHistoryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 3 | 3 | 8 | 53% |

---

## 🔗 Tabelas Relacionadas

- [[ar_dispute_history|AR_DISPUTE_HISTORY]] — 12 atributos (1 PKs, 6 BICC)
- [[ar_payment_schedules_all|AR_PAYMENT_SCHEDULES_ALL]] — 1 atributos (1 PKs, 1 BICC)
- [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]] — 2 atributos (1 PKs, 1 BICC)

---

## ⚙️ Atributos

### [[ar_dispute_history|AR_DISPUTE_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AmountDueRemaining | AMOUNT_DUE_REMAINING | — | ✅ |
| 2 | AmountInDispute | AMOUNT_IN_DISPUTE | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | — |
| 4 | CreatedFrom | CREATED_FROM | — | — |
| 5 | DisputeAmount | DISPUTE_AMOUNT | — | ✅ |
| 6 | DisputeHistoryId | DISPUTE_HISTORY_ID | 🔑 | ✅ |
| 7 | EndDate | END_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | PaymentScheduleId | PAYMENT_SCHEDULE_ID | — | — |
| 12 | StartDate | START_DATE | — | ✅ |

### [[ar_payment_schedules_all|AR_PAYMENT_SCHEDULES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentSchedulePaymentScheduleId | PAYMENT_SCHEDULE_ID | 🔑 | ✅ |

### [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionHeaderCustomerTrxId | CUSTOMER_TRX_ID | 🔑 | ✅ |
| 2 | TransactionHeaderSetOfBooksId | SET_OF_BOOKS_ID | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
