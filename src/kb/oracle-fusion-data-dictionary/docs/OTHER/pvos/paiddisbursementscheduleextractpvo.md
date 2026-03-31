---
id: DOC-OTHER-PVO-PaidDisbursementScheduleExtractPVO
doc_type: system-doc
title: "PaidDisbursementScheduleExtractPVO — PVO Cross-Module"
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
  - PaidDisbursementScheduleExtractPVO
  - paiddisbursementscheduleextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PaidDisbursementScheduleExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Paid Disbursement Schedule Extract. Acessa as tabelas: AP_INVOICE_PAYMENTS_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ApBiccExtractAM.PaidDisbursementScheduleExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 54 | 1 | 1 | 54 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ap_invoice_payments_all|AP_INVOICE_PAYMENTS_ALL]] — 54 atributos (1 PKs, 54 BICC)

---

## ⚙️ Atributos

### [[ap_invoice_payments_all|AP_INVOICE_PAYMENTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApInvoicePaymentsAllAccountingDate | ACCOUNTING_DATE | — | ✅ |
| 2 | ApInvoicePaymentsAllAccountingEventId | ACCOUNTING_EVENT_ID | — | ✅ |
| 3 | ApInvoicePaymentsAllAcctsPayCodeCombinationId | ACCTS_PAY_CODE_COMBINATION_ID | — | ✅ |
| 4 | ApInvoicePaymentsAllAmount | AMOUNT | — | ✅ |
| 5 | ApInvoicePaymentsAllAmountInvCurr | AMOUNT_INV_CURR | — | ✅ |
| 6 | ApInvoicePaymentsAllAnnualPercentageRate | ANNUAL_PERCENTAGE_RATE | — | ✅ |
| 7 | ApInvoicePaymentsAllAprAssignmentId | APR_ASSIGNMENT_ID | — | ✅ |
| 8 | ApInvoicePaymentsAllAssetCodeCombinationId | ASSET_CODE_COMBINATION_ID | — | ✅ |
| 9 | ApInvoicePaymentsAllAssetsAdditionFlag | ASSETS_ADDITION_FLAG | — | ✅ |
| 10 | ApInvoicePaymentsAllBankAccountNum | BANK_ACCOUNT_NUM | — | ✅ |
| 11 | ApInvoicePaymentsAllBankAccountType | BANK_ACCOUNT_TYPE | — | ✅ |
| 12 | ApInvoicePaymentsAllBankNum | BANK_NUM | — | ✅ |
| 13 | ApInvoicePaymentsAllCheckId | CHECK_ID | — | ✅ |
| 14 | ApInvoicePaymentsAllCreatedBy | CREATED_BY | — | ✅ |
| 15 | ApInvoicePaymentsAllCreationDate | CREATION_DATE | — | ✅ |
| 16 | ApInvoicePaymentsAllDaysAccelerated | DAYS_ACCELERATED | — | ✅ |
| 17 | ApInvoicePaymentsAllDiscountLost | DISCOUNT_LOST | — | ✅ |
| 18 | ApInvoicePaymentsAllDiscountLostInvCurr | DISCOUNT_LOST_INV_CURR | — | ✅ |
| 19 | ApInvoicePaymentsAllDiscountTaken | DISCOUNT_TAKEN | — | ✅ |
| 20 | ApInvoicePaymentsAllDiscountTakenInvCurr | DISCOUNT_TAKEN_INV_CURR | — | ✅ |
| 21 | ApInvoicePaymentsAllExchangeDate | EXCHANGE_DATE | — | ✅ |
| 22 | ApInvoicePaymentsAllExchangeRate | EXCHANGE_RATE | — | ✅ |
| 23 | ApInvoicePaymentsAllExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 24 | ApInvoicePaymentsAllExternalBankAccountId | EXTERNAL_BANK_ACCOUNT_ID | — | ✅ |
| 25 | ApInvoicePaymentsAllGainCodeCombinationId | GAIN_CODE_COMBINATION_ID | — | ✅ |
| 26 | ApInvoicePaymentsAllIbanNumber | IBAN_NUMBER | — | ✅ |
| 27 | ApInvoicePaymentsAllInvOrgId | INV_ORG_ID | — | ✅ |
| 28 | ApInvoicePaymentsAllInvoiceBaseAmount | INVOICE_BASE_AMOUNT | — | ✅ |
| 29 | ApInvoicePaymentsAllInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 30 | ApInvoicePaymentsAllInvoiceId | INVOICE_ID | — | ✅ |
| 31 | ApInvoicePaymentsAllInvoicePaymentId | INVOICE_PAYMENT_ID | 🔑 | ✅ |
| 32 | ApInvoicePaymentsAllInvoicePaymentType | INVOICE_PAYMENT_TYPE | — | ✅ |
| 33 | ApInvoicePaymentsAllInvoicingPartyId | INVOICING_PARTY_ID | — | ✅ |
| 34 | ApInvoicePaymentsAllInvoicingPartySiteId | INVOICING_PARTY_SITE_ID | — | ✅ |
| 35 | ApInvoicePaymentsAllInvoicingVendorSiteId | INVOICING_VENDOR_SITE_ID | — | ✅ |
| 36 | ApInvoicePaymentsAllLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 37 | ApInvoicePaymentsAllLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 38 | ApInvoicePaymentsAllLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 39 | ApInvoicePaymentsAllLossCodeCombinationId | LOSS_CODE_COMBINATION_ID | — | ✅ |
| 40 | ApInvoicePaymentsAllObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 41 | ApInvoicePaymentsAllOrgId | ORG_ID | — | ✅ |
| 42 | ApInvoicePaymentsAllPaymentBaseAmount | PAYMENT_BASE_AMOUNT | — | ✅ |
| 43 | ApInvoicePaymentsAllPaymentCurrencyCode | PAYMENT_CURRENCY_CODE | — | ✅ |
| 44 | ApInvoicePaymentsAllPaymentNum | PAYMENT_NUM | — | ✅ |
| 45 | ApInvoicePaymentsAllPeriodName | PERIOD_NAME | — | ✅ |
| 46 | ApInvoicePaymentsAllPostedFlag | POSTED_FLAG | — | ✅ |
| 47 | ApInvoicePaymentsAllRemitToAddressId | REMIT_TO_ADDRESS_ID | — | ✅ |
| 48 | ApInvoicePaymentsAllRemitToAddressName | REMIT_TO_ADDRESS_NAME | — | ✅ |
| 49 | ApInvoicePaymentsAllRemitToSupplierId | REMIT_TO_SUPPLIER_ID | — | ✅ |
| 50 | ApInvoicePaymentsAllRemitToSupplierName | REMIT_TO_SUPPLIER_NAME | — | ✅ |
| 51 | ApInvoicePaymentsAllReversalFlag | REVERSAL_FLAG | — | ✅ |
| 52 | ApInvoicePaymentsAllReversalInvPmtId | REVERSAL_INV_PMT_ID | — | ✅ |
| 53 | ApInvoicePaymentsAllSetOfBooksId | SET_OF_BOOKS_ID | — | ✅ |
| 54 | ApInvoicePaymentsAllXCurrRate | X_CURR_RATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
