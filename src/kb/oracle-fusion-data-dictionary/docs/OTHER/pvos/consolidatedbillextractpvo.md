---
id: DOC-OTHER-PVO-ConsolidatedBillExtractPVO
doc_type: system-doc
title: "ConsolidatedBillExtractPVO — PVO Cross-Module"
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
  - ConsolidatedBillExtractPVO
  - consolidatedbillextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ConsolidatedBillExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Consolidated Bill Extract. Acessa as tabelas: AR_CONS_INV_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.ConsolidatedBillExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 61 | 1 | 1 | 45 | 74% |

---

## 🔗 Tabelas Relacionadas

- [[ar_cons_inv_all|AR_CONS_INV_ALL]] — 61 atributos (1 PKs, 45 BICC)

---

## ⚙️ Atributos

### [[ar_cons_inv_all|AR_CONS_INV_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArConsInvAgingBucket1Amt | AGING_BUCKET1_AMT | — | ✅ |
| 2 | ArConsInvAgingBucket2Amt | AGING_BUCKET2_AMT | — | ✅ |
| 3 | ArConsInvAgingBucket3Amt | AGING_BUCKET3_AMT | — | ✅ |
| 4 | ArConsInvAgingBucket4Amt | AGING_BUCKET4_AMT | — | ✅ |
| 5 | ArConsInvAgingBucket5Amt | AGING_BUCKET5_AMT | — | ✅ |
| 6 | ArConsInvAgingBucket6Amt | AGING_BUCKET6_AMT | — | ✅ |
| 7 | ArConsInvAgingBucket7Amt | AGING_BUCKET7_AMT | — | ✅ |
| 8 | ArConsInvAttribute1 | ATTRIBUTE1 | — | — |
| 9 | ArConsInvAttribute10 | ATTRIBUTE10 | — | — |
| 10 | ArConsInvAttribute11 | ATTRIBUTE11 | — | — |
| 11 | ArConsInvAttribute12 | ATTRIBUTE12 | — | — |
| 12 | ArConsInvAttribute13 | ATTRIBUTE13 | — | — |
| 13 | ArConsInvAttribute14 | ATTRIBUTE14 | — | — |
| 14 | ArConsInvAttribute15 | ATTRIBUTE15 | — | — |
| 15 | ArConsInvAttribute2 | ATTRIBUTE2 | — | — |
| 16 | ArConsInvAttribute3 | ATTRIBUTE3 | — | — |
| 17 | ArConsInvAttribute4 | ATTRIBUTE4 | — | — |
| 18 | ArConsInvAttribute5 | ATTRIBUTE5 | — | — |
| 19 | ArConsInvAttribute6 | ATTRIBUTE6 | — | — |
| 20 | ArConsInvAttribute7 | ATTRIBUTE7 | — | — |
| 21 | ArConsInvAttribute8 | ATTRIBUTE8 | — | — |
| 22 | ArConsInvAttribute9 | ATTRIBUTE9 | — | — |
| 23 | ArConsInvAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 24 | ArConsInvBeginningBalance | BEGINNING_BALANCE | — | ✅ |
| 25 | ArConsInvBfbTemplateName | BFB_TEMPLATE_NAME | — | ✅ |
| 26 | ArConsInvBillLevelFlag | BILL_LEVEL_FLAG | — | ✅ |
| 27 | ArConsInvBillingCycleId | BILLING_CYCLE_ID | — | ✅ |
| 28 | ArConsInvBillingDate | BILLING_DATE | — | ✅ |
| 29 | ArConsInvConcurrentRequestId | CONCURRENT_REQUEST_ID | — | ✅ |
| 30 | ArConsInvConsBillingNumber | CONS_BILLING_NUMBER | — | ✅ |
| 31 | ArConsInvConsInvId | CONS_INV_ID | 🔑 | ✅ |
| 32 | ArConsInvConsInvType | CONS_INV_TYPE | — | ✅ |
| 33 | ArConsInvCreatedBy | CREATED_BY | — | ✅ |
| 34 | ArConsInvCreationDate | CREATION_DATE | — | ✅ |
| 35 | ArConsInvCurrencyCode | CURRENCY_CODE | — | ✅ |
| 36 | ArConsInvCustomerId | CUSTOMER_ID | — | ✅ |
| 37 | ArConsInvCutOffDate | CUT_OFF_DATE | — | ✅ |
| 38 | ArConsInvDueDate | DUE_DATE | — | ✅ |
| 39 | ArConsInvEndingBalance | ENDING_BALANCE | — | ✅ |
| 40 | ArConsInvIssueDate | ISSUE_DATE | — | ✅ |
| 41 | ArConsInvLastBillingDate | LAST_BILLING_DATE | — | ✅ |
| 42 | ArConsInvLastChargeDate | LAST_CHARGE_DATE | — | ✅ |
| 43 | ArConsInvLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 44 | ArConsInvLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 45 | ArConsInvLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 46 | ArConsInvObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 47 | ArConsInvOrgId | ORG_ID | — | ✅ |
| 48 | ArConsInvPrintStatus | PRINT_STATUS | — | ✅ |
| 49 | ArConsInvRemitToAddressId | REMIT_TO_ADDRESS_ID | — | ✅ |
| 50 | ArConsInvRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | ✅ |
| 51 | ArConsInvSiteUseId | SITE_USE_ID | — | ✅ |
| 52 | ArConsInvStartDate | START_DATE | — | ✅ |
| 53 | ArConsInvStatus | STATUS | — | ✅ |
| 54 | ArConsInvTermId | TERM_ID | — | ✅ |
| 55 | ArConsInvTotalAdjustmentsAmt | TOTAL_ADJUSTMENTS_AMT | — | ✅ |
| 56 | ArConsInvTotalCreditsAmt | TOTAL_CREDITS_AMT | — | ✅ |
| 57 | ArConsInvTotalReceiptsAmt | TOTAL_RECEIPTS_AMT | — | ✅ |
| 58 | ArConsInvTotalTaxAmt | TOTAL_TAX_AMT | — | ✅ |
| 59 | ArConsInvTotalTrxAmt | TOTAL_TRX_AMT | — | ✅ |
| 60 | ArConsInvUnpaidReason | UNPAID_REASON | — | ✅ |
| 61 | TotalFinanceChargesAmt | TOTAL_FINANCE_CHARGES_AMT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
