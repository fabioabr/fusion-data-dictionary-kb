---
id: DOC-OTHER-PVO-BillingAccountingEventExtractPVO
doc_type: system-doc
title: "BillingAccountingEventExtractPVO — PVO Cross-Module"
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
  - BillingAccountingEventExtractPVO
  - billingaccountingeventextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BillingAccountingEventExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Billing Accounting Event Extract. Acessa as tabelas: PJB_ACCOUNTING_EVENTS.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjbBiccExtractAM.BillingAccountingEventExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 48 | 1 | 1 | 48 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjb_accounting_events|PJB_ACCOUNTING_EVENTS]] — 48 atributos (1 PKs, 48 BICC)

---

## ⚙️ Atributos

### [[pjb_accounting_events|PJB_ACCOUNTING_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillingAccountingEventPEOAccountingDate | ACCOUNTING_DATE | — | ✅ |
| 2 | BillingAccountingEventPEOAccountingEventId | ACCOUNTING_EVENT_ID | 🔑 | ✅ |
| 3 | BillingAccountingEventPEOAccountingEventType | ACCOUNTING_EVENT_TYPE | — | ✅ |
| 4 | BillingAccountingEventPEOAccountingPeriod | ACCOUNTING_PERIOD | — | ✅ |
| 5 | BillingAccountingEventPEOBillingTypeCode | BILLING_TYPE_CODE | — | ✅ |
| 6 | BillingAccountingEventPEOContCurrAccttransAmt | CONT_CURR_ACCTTRANS_AMT | — | ✅ |
| 7 | BillingAccountingEventPEOContractCurrencyCode | CONTRACT_CURRENCY_CODE | — | ✅ |
| 8 | BillingAccountingEventPEOContractId | CONTRACT_ID | — | ✅ |
| 9 | BillingAccountingEventPEOContractLineAmt | CONTRACT_LINE_AMT | — | ✅ |
| 10 | BillingAccountingEventPEOContractLineId | CONTRACT_LINE_ID | — | ✅ |
| 11 | BillingAccountingEventPEOCreatedBy | CREATED_BY | — | ✅ |
| 12 | BillingAccountingEventPEOCreationDate | CREATION_DATE | — | ✅ |
| 13 | BillingAccountingEventPEODescription | DESCRIPTION | — | ✅ |
| 14 | BillingAccountingEventPEOEnteredCurrAmt | ENTERED_CURR_AMT | — | ✅ |
| 15 | BillingAccountingEventPEOEnteredCurrCode | ENTERED_CURR_CODE | — | ✅ |
| 16 | BillingAccountingEventPEOInvCurrOverrideId | INV_CURR_OVERRIDE_ID | — | ✅ |
| 17 | BillingAccountingEventPEOInvoiceCurrDateType | INVOICE_CURR_DATE_TYPE | — | ✅ |
| 18 | BillingAccountingEventPEOInvoiceCurrExchgDate | INVOICE_CURR_EXCHG_DATE | — | ✅ |
| 19 | BillingAccountingEventPEOInvoiceCurrExchgRate | INVOICE_CURR_EXCHG_RATE | — | ✅ |
| 20 | BillingAccountingEventPEOInvoiceCurrRateType | INVOICE_CURR_RATE_TYPE | — | ✅ |
| 21 | BillingAccountingEventPEOItdContCurrPerfAmt | ITD_CONT_CURR_PERF_AMT | — | ✅ |
| 22 | BillingAccountingEventPEOItdEntCurrBilledAmt | ITD_ENT_CURR_BILLED_AMT | — | ✅ |
| 23 | BillingAccountingEventPEOItdEntCurrRevAmt | ITD_ENT_CURR_REV_AMT | — | ✅ |
| 24 | BillingAccountingEventPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 25 | BillingAccountingEventPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 26 | BillingAccountingEventPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 27 | BillingAccountingEventPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 28 | BillingAccountingEventPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 29 | BillingAccountingEventPEOLedgerCurrAmt | LEDGER_CURR_AMT | — | ✅ |
| 30 | BillingAccountingEventPEOLedgerCurrCode | LEDGER_CURR_CODE | — | ✅ |
| 31 | BillingAccountingEventPEOLedgerCurrExchgDate | LEDGER_CURR_EXCHG_DATE | — | ✅ |
| 32 | BillingAccountingEventPEOLedgerCurrExchgRate | LEDGER_CURR_EXCHG_RATE | — | ✅ |
| 33 | BillingAccountingEventPEOLedgerCurrRateDateType | LEDGER_CURR_RATE_DATE_TYPE | — | ✅ |
| 34 | BillingAccountingEventPEOLedgerCurrRateType | LEDGER_CURR_RATE_TYPE | — | ✅ |
| 35 | BillingAccountingEventPEOLedgerId | LEDGER_ID | — | ✅ |
| 36 | BillingAccountingEventPEOLineNum | LINE_NUM | — | ✅ |
| 37 | BillingAccountingEventPEOMajorVersion | MAJOR_VERSION | — | ✅ |
| 38 | BillingAccountingEventPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 39 | BillingAccountingEventPEOOrgId | ORG_ID | — | ✅ |
| 40 | BillingAccountingEventPEOPaDate | PA_DATE | — | ✅ |
| 41 | BillingAccountingEventPEOPaPeriod | PA_PERIOD | — | ✅ |
| 42 | BillingAccountingEventPEOPtdEntCurrReclassifyAmt | PTD_ENT_CURR_RECLASSIFY_AMT | — | ✅ |
| 43 | BillingAccountingEventPEOReclassificationDate | RECLASSIFICATION_DATE | — | ✅ |
| 44 | BillingAccountingEventPEORequestId | REQUEST_ID | — | ✅ |
| 45 | BillingAccountingEventPEOReversedAccountingEventId | REVERSED_ACCOUNTING_EVENT_ID | — | ✅ |
| 46 | BillingAccountingEventPEOReversedFlag | REVERSED_FLAG | — | ✅ |
| 47 | BillingAccountingEventPEOReversedLineNum | REVERSED_LINE_NUM | — | ✅ |
| 48 | BillingAccountingEventPEOSlaEventId | SLA_EVENT_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
