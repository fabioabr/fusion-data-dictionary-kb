---
id: DOC-OTHER-PVO-PaymentScheduleExtractPVO
doc_type: system-doc
title: "PaymentScheduleExtractPVO — PVO Cross-Module"
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
  - PaymentScheduleExtractPVO
  - paymentscheduleextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PaymentScheduleExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Payment Schedule Extract. Acessa as tabelas: AR_PAYMENT_SCHEDULES_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.PaymentScheduleExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 127 | 1 | 1 | 80 | 63% |

---

## 🔗 Tabelas Relacionadas

- [[ar_payment_schedules_all|AR_PAYMENT_SCHEDULES_ALL]] — 127 atributos (1 PKs, 80 BICC)

---

## ⚙️ Atributos

### [[ar_payment_schedules_all|AR_PAYMENT_SCHEDULES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArPaymentScheduleAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | ✅ |
| 2 | ArPaymentScheduleActiveClaimFlag | ACTIVE_CLAIM_FLAG | — | ✅ |
| 3 | ArPaymentScheduleActualDateClosed | ACTUAL_DATE_CLOSED | — | ✅ |
| 4 | ArPaymentScheduleAmountAdjusted | AMOUNT_ADJUSTED | — | ✅ |
| 5 | ArPaymentScheduleAmountAdjustedPending | AMOUNT_ADJUSTED_PENDING | — | ✅ |
| 6 | ArPaymentScheduleAmountApplied | AMOUNT_APPLIED | — | ✅ |
| 7 | ArPaymentScheduleAmountCredited | AMOUNT_CREDITED | — | ✅ |
| 8 | ArPaymentScheduleAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | ✅ |
| 9 | ArPaymentScheduleAmountDueRemaining | AMOUNT_DUE_REMAINING | — | ✅ |
| 10 | ArPaymentScheduleAmountInDispute | AMOUNT_IN_DISPUTE | — | ✅ |
| 11 | ArPaymentScheduleAmountLineItemsOriginal | AMOUNT_LINE_ITEMS_ORIGINAL | — | ✅ |
| 12 | ArPaymentScheduleAmountLineItemsRemaining | AMOUNT_LINE_ITEMS_REMAINING | — | ✅ |
| 13 | ArPaymentScheduleAmountOnAccount | AMOUNT_ON_ACCOUNT | — | ✅ |
| 14 | ArPaymentScheduleAmountOtherAccount | AMOUNT_OTHER_ACCOUNT | — | ✅ |
| 15 | ArPaymentScheduleAssociatedCashReceiptId | ASSOCIATED_CASH_RECEIPT_ID | — | ✅ |
| 16 | ArPaymentScheduleAttribute1 | ATTRIBUTE1 | — | — |
| 17 | ArPaymentScheduleAttribute10 | ATTRIBUTE10 | — | — |
| 18 | ArPaymentScheduleAttribute11 | ATTRIBUTE11 | — | — |
| 19 | ArPaymentScheduleAttribute12 | ATTRIBUTE12 | — | — |
| 20 | ArPaymentScheduleAttribute13 | ATTRIBUTE13 | — | — |
| 21 | ArPaymentScheduleAttribute14 | ATTRIBUTE14 | — | — |
| 22 | ArPaymentScheduleAttribute15 | ATTRIBUTE15 | — | — |
| 23 | ArPaymentScheduleAttribute2 | ATTRIBUTE2 | — | — |
| 24 | ArPaymentScheduleAttribute3 | ATTRIBUTE3 | — | — |
| 25 | ArPaymentScheduleAttribute4 | ATTRIBUTE4 | — | — |
| 26 | ArPaymentScheduleAttribute5 | ATTRIBUTE5 | — | — |
| 27 | ArPaymentScheduleAttribute6 | ATTRIBUTE6 | — | — |
| 28 | ArPaymentScheduleAttribute7 | ATTRIBUTE7 | — | — |
| 29 | ArPaymentScheduleAttribute8 | ATTRIBUTE8 | — | — |
| 30 | ArPaymentScheduleAttribute9 | ATTRIBUTE9 | — | — |
| 31 | ArPaymentScheduleAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 32 | ArPaymentScheduleBrAmountAssigned | BR_AMOUNT_ASSIGNED | — | ✅ |
| 33 | ArPaymentScheduleCallDateLast | CALL_DATE_LAST | — | ✅ |
| 34 | ArPaymentScheduleCashReceiptId | CASH_RECEIPT_ID | — | ✅ |
| 35 | ArPaymentScheduleCollectorLast | COLLECTOR_LAST | — | ✅ |
| 36 | ArPaymentScheduleConsInvId | CONS_INV_ID | — | ✅ |
| 37 | ArPaymentScheduleConsInvIdRev | CONS_INV_ID_REV | — | ✅ |
| 38 | ArPaymentScheduleCreatedBy | CREATED_BY | — | ✅ |
| 39 | ArPaymentScheduleCreationDate | CREATION_DATE | — | ✅ |
| 40 | ArPaymentScheduleCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | ✅ |
| 41 | ArPaymentScheduleCustomerId | CUSTOMER_ID | — | ✅ |
| 42 | ArPaymentScheduleCustomerSiteUseId | CUSTOMER_SITE_USE_ID | — | ✅ |
| 43 | ArPaymentScheduleCustomerTrxId | CUSTOMER_TRX_ID | — | ✅ |
| 44 | ArPaymentScheduleDelContactEmailAddress | DEL_CONTACT_EMAIL_ADDRESS | — | ✅ |
| 45 | ArPaymentScheduleDiscountTakenEarned | DISCOUNT_TAKEN_EARNED | — | ✅ |
| 46 | ArPaymentScheduleDiscountTakenUnearned | DISCOUNT_TAKEN_UNEARNED | — | ✅ |
| 47 | ArPaymentScheduleDisputeDate | DISPUTE_DATE | — | ✅ |
| 48 | ArPaymentScheduleDueDate | DUE_DATE | — | ✅ |
| 49 | ArPaymentScheduleDunningLevelOverrideDate | DUNNING_LEVEL_OVERRIDE_DATE | — | ✅ |
| 50 | ArPaymentScheduleExchangeDate | EXCHANGE_DATE | — | ✅ |
| 51 | ArPaymentScheduleExchangeRate | EXCHANGE_RATE | — | ✅ |
| 52 | ArPaymentScheduleExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 53 | ArPaymentScheduleExcludeFromConsBillFlag | EXCLUDE_FROM_CONS_BILL_FLAG | — | ✅ |
| 54 | ArPaymentScheduleExcludeFromDunningFlag | EXCLUDE_FROM_DUNNING_FLAG | — | ✅ |
| 55 | ArPaymentScheduleFollowUpCodeLast | FOLLOW_UP_CODE_LAST | — | ✅ |
| 56 | ArPaymentScheduleFollowUpDateLast | FOLLOW_UP_DATE_LAST | — | ✅ |
| 57 | ArPaymentScheduleFreightOriginal | FREIGHT_ORIGINAL | — | ✅ |
| 58 | ArPaymentScheduleFreightRemaining | FREIGHT_REMAINING | — | ✅ |
| 59 | ArPaymentScheduleGlDate | GL_DATE | — | ✅ |
| 60 | ArPaymentScheduleGlDateClosed | GL_DATE_CLOSED | — | ✅ |
| 61 | ArPaymentScheduleGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 62 | ArPaymentScheduleGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 63 | ArPaymentScheduleGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 64 | ArPaymentScheduleGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 65 | ArPaymentScheduleGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 66 | ArPaymentScheduleGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 67 | ArPaymentScheduleGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 68 | ArPaymentScheduleGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 69 | ArPaymentScheduleGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 70 | ArPaymentScheduleGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 71 | ArPaymentScheduleGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 72 | ArPaymentScheduleGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 73 | ArPaymentScheduleGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 74 | ArPaymentScheduleGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 75 | ArPaymentScheduleGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 76 | ArPaymentScheduleGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 77 | ArPaymentScheduleGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 78 | ArPaymentScheduleGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 79 | ArPaymentScheduleGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 80 | ArPaymentScheduleGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 81 | ArPaymentScheduleGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 82 | ArPaymentScheduleGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 83 | ArPaymentScheduleGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 84 | ArPaymentScheduleGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 85 | ArPaymentScheduleGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 86 | ArPaymentScheduleGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 87 | ArPaymentScheduleGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 88 | ArPaymentScheduleGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 89 | ArPaymentScheduleGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 90 | ArPaymentScheduleGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 91 | ArPaymentScheduleGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 92 | ArPaymentScheduleInCollection | IN_COLLECTION | — | ✅ |
| 93 | ArPaymentScheduleInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 94 | ArPaymentScheduleLastChargeDate | LAST_CHARGE_DATE | — | ✅ |
| 95 | ArPaymentScheduleLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 96 | ArPaymentScheduleLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 97 | ArPaymentScheduleLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 98 | ArPaymentScheduleModuleId | MODULE_ID | — | ✅ |
| 99 | ArPaymentScheduleNumberOfDueDates | NUMBER_OF_DUE_DATES | — | ✅ |
| 100 | ArPaymentScheduleObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 101 | ArPaymentScheduleOrgId | ORG_ID | — | ✅ |
| 102 | ArPaymentSchedulePaymentApproval | PAYMENT_APPROVAL | — | ✅ |
| 103 | ArPaymentSchedulePaymentScheduleClass1 | CLASS | — | ✅ |
| 104 | ArPaymentSchedulePaymentScheduleId | PAYMENT_SCHEDULE_ID | 🔑 | ✅ |
| 105 | ArPaymentSchedulePrintRequestId | PRINT_REQUEST_ID | — | ✅ |
| 106 | ArPaymentScheduleProgramApplicationId | PROGRAM_APPLICATION_ID | — | ✅ |
| 107 | ArPaymentScheduleProgramId | PROGRAM_ID | — | ✅ |
| 108 | ArPaymentScheduleProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 109 | ArPaymentSchedulePromiseAmountLast | PROMISE_AMOUNT_LAST | — | ✅ |
| 110 | ArPaymentSchedulePromiseDateLast | PROMISE_DATE_LAST | — | ✅ |
| 111 | ArPaymentScheduleReceiptConfirmedFlag | RECEIPT_CONFIRMED_FLAG | — | ✅ |
| 112 | ArPaymentScheduleReceivablesChargesCharged | RECEIVABLES_CHARGES_CHARGED | — | ✅ |
| 113 | ArPaymentScheduleReceivablesChargesRemaining | RECEIVABLES_CHARGES_REMAINING | — | ✅ |
| 114 | ArPaymentScheduleRequestId | REQUEST_ID | — | ✅ |
| 115 | ArPaymentScheduleReservedType | RESERVED_TYPE | — | ✅ |
| 116 | ArPaymentScheduleReservedValue | RESERVED_VALUE | — | ✅ |
| 117 | ArPaymentScheduleReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | ✅ |
| 118 | ArPaymentScheduleSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 119 | ArPaymentScheduleSelectedForReceiptBatchId | SELECTED_FOR_RECEIPT_BATCH_ID | — | ✅ |
| 120 | ArPaymentScheduleStagedDunningLevel | STAGED_DUNNING_LEVEL | — | ✅ |
| 121 | ArPaymentScheduleStatus | STATUS | — | ✅ |
| 122 | ArPaymentScheduleTaxOriginal | TAX_ORIGINAL | — | ✅ |
| 123 | ArPaymentScheduleTaxRemaining | TAX_REMAINING | — | ✅ |
| 124 | ArPaymentScheduleTermId | TERM_ID | — | ✅ |
| 125 | ArPaymentScheduleTermsSequenceNumber | TERMS_SEQUENCE_NUMBER | — | ✅ |
| 126 | ArPaymentScheduleTrxDate | TRX_DATE | — | ✅ |
| 127 | ArPaymentScheduleTrxNumber | TRX_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
