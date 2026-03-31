---
id: DOC-OTHER-PVO-ReceivableApplicationExtractPVO
doc_type: system-doc
title: "ReceivableApplicationExtractPVO — PVO Cross-Module"
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
  - ReceivableApplicationExtractPVO
  - receivableapplicationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReceivableApplicationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Receivable Application Extract. Acessa as tabelas: AR_RECEIVABLE_APPLICATIONS_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.ReceivableApplicationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 129 | 1 | 1 | 82 | 64% |

---

## 🔗 Tabelas Relacionadas

- [[ar_receivable_applications_all|AR_RECEIVABLE_APPLICATIONS_ALL]] — 129 atributos (1 PKs, 82 BICC)

---

## ⚙️ Atributos

### [[ar_receivable_applications_all|AR_RECEIVABLE_APPLICATIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArReceivableApplicationAcctdAmountAppliedFrom | ACCTD_AMOUNT_APPLIED_FROM | — | ✅ |
| 2 | ArReceivableApplicationAcctdAmountAppliedTo | ACCTD_AMOUNT_APPLIED_TO | — | ✅ |
| 3 | ArReceivableApplicationAcctdEarnedDiscountTaken | ACCTD_EARNED_DISCOUNT_TAKEN | — | ✅ |
| 4 | ArReceivableApplicationAcctdUnearnedDiscountTaken | ACCTD_UNEARNED_DISCOUNT_TAKEN | — | ✅ |
| 5 | ArReceivableApplicationAmountApplied | AMOUNT_APPLIED | — | ✅ |
| 6 | ArReceivableApplicationAmountAppliedFrom | AMOUNT_APPLIED_FROM | — | ✅ |
| 7 | ArReceivableApplicationApplicationRefId | APPLICATION_REF_ID | — | ✅ |
| 8 | ArReceivableApplicationApplicationRefNum | APPLICATION_REF_NUM | — | ✅ |
| 9 | ArReceivableApplicationApplicationRefReason | APPLICATION_REF_REASON | — | ✅ |
| 10 | ArReceivableApplicationApplicationRefType | APPLICATION_REF_TYPE | — | ✅ |
| 11 | ArReceivableApplicationApplicationRule | APPLICATION_RULE | — | ✅ |
| 12 | ArReceivableApplicationApplicationType | APPLICATION_TYPE | — | ✅ |
| 13 | ArReceivableApplicationAppliedCustomerTrxId | APPLIED_CUSTOMER_TRX_ID | — | ✅ |
| 14 | ArReceivableApplicationAppliedCustomerTrxLineId | APPLIED_CUSTOMER_TRX_LINE_ID | — | ✅ |
| 15 | ArReceivableApplicationAppliedPaymentScheduleId | APPLIED_PAYMENT_SCHEDULE_ID | — | ✅ |
| 16 | ArReceivableApplicationAppliedRecAppId | APPLIED_REC_APP_ID | — | ✅ |
| 17 | ArReceivableApplicationApplyDate | APPLY_DATE | — | ✅ |
| 18 | ArReceivableApplicationAttribute1 | ATTRIBUTE1 | — | — |
| 19 | ArReceivableApplicationAttribute10 | ATTRIBUTE10 | — | — |
| 20 | ArReceivableApplicationAttribute11 | ATTRIBUTE11 | — | — |
| 21 | ArReceivableApplicationAttribute12 | ATTRIBUTE12 | — | — |
| 22 | ArReceivableApplicationAttribute13 | ATTRIBUTE13 | — | — |
| 23 | ArReceivableApplicationAttribute14 | ATTRIBUTE14 | — | — |
| 24 | ArReceivableApplicationAttribute15 | ATTRIBUTE15 | — | — |
| 25 | ArReceivableApplicationAttribute2 | ATTRIBUTE2 | — | — |
| 26 | ArReceivableApplicationAttribute3 | ATTRIBUTE3 | — | — |
| 27 | ArReceivableApplicationAttribute4 | ATTRIBUTE4 | — | — |
| 28 | ArReceivableApplicationAttribute5 | ATTRIBUTE5 | — | — |
| 29 | ArReceivableApplicationAttribute6 | ATTRIBUTE6 | — | — |
| 30 | ArReceivableApplicationAttribute7 | ATTRIBUTE7 | — | — |
| 31 | ArReceivableApplicationAttribute8 | ATTRIBUTE8 | — | — |
| 32 | ArReceivableApplicationAttribute9 | ATTRIBUTE9 | — | — |
| 33 | ArReceivableApplicationAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 34 | ArReceivableApplicationCashReceiptHistoryId | CASH_RECEIPT_HISTORY_ID | — | ✅ |
| 35 | ArReceivableApplicationCashReceiptId | CASH_RECEIPT_ID | — | ✅ |
| 36 | ArReceivableApplicationChargesEdiscounted | CHARGES_EDISCOUNTED | — | ✅ |
| 37 | ArReceivableApplicationChargesUediscounted | CHARGES_UEDISCOUNTED | — | ✅ |
| 38 | ArReceivableApplicationCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 39 | ArReceivableApplicationComments | COMMENTS | — | ✅ |
| 40 | ArReceivableApplicationConfirmedFlag | CONFIRMED_FLAG | — | ✅ |
| 41 | ArReceivableApplicationConsInvId | CONS_INV_ID | — | ✅ |
| 42 | ArReceivableApplicationConsInvIdTo | CONS_INV_ID_TO | — | ✅ |
| 43 | ArReceivableApplicationCreatedBy | CREATED_BY | — | ✅ |
| 44 | ArReceivableApplicationCreationDate | CREATION_DATE | — | ✅ |
| 45 | ArReceivableApplicationCustomerReason | CUSTOMER_REASON | — | ✅ |
| 46 | ArReceivableApplicationCustomerReference | CUSTOMER_REFERENCE | — | ✅ |
| 47 | ArReceivableApplicationCustomerTrxId | CUSTOMER_TRX_ID | — | ✅ |
| 48 | ArReceivableApplicationDaysLate | DAYS_LATE | — | ✅ |
| 49 | ArReceivableApplicationDisplay | DISPLAY | — | ✅ |
| 50 | ArReceivableApplicationEarnedDiscountCcid | EARNED_DISCOUNT_CCID | — | ✅ |
| 51 | ArReceivableApplicationEarnedDiscountTaken | EARNED_DISCOUNT_TAKEN | — | ✅ |
| 52 | ArReceivableApplicationEdiscTaxAcctRule | EDISC_TAX_ACCT_RULE | — | ✅ |
| 53 | ArReceivableApplicationEventId | EVENT_ID | — | ✅ |
| 54 | ArReceivableApplicationExceptionReasonCode | EXCEPTION_REASON_CODE | — | ✅ |
| 55 | ArReceivableApplicationFreightApplied | FREIGHT_APPLIED | — | ✅ |
| 56 | ArReceivableApplicationFreightEdiscounted | FREIGHT_EDISCOUNTED | — | ✅ |
| 57 | ArReceivableApplicationFreightUediscounted | FREIGHT_UEDISCOUNTED | — | ✅ |
| 58 | ArReceivableApplicationGlDate | GL_DATE | — | ✅ |
| 59 | ArReceivableApplicationGlPostedDate | GL_POSTED_DATE | — | ✅ |
| 60 | ArReceivableApplicationGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 61 | ArReceivableApplicationGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 62 | ArReceivableApplicationGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 63 | ArReceivableApplicationGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 64 | ArReceivableApplicationGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 65 | ArReceivableApplicationGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 66 | ArReceivableApplicationGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 67 | ArReceivableApplicationGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 68 | ArReceivableApplicationGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 69 | ArReceivableApplicationGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 70 | ArReceivableApplicationGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 71 | ArReceivableApplicationGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 72 | ArReceivableApplicationGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 73 | ArReceivableApplicationGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 74 | ArReceivableApplicationGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 75 | ArReceivableApplicationGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 76 | ArReceivableApplicationGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 77 | ArReceivableApplicationGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 78 | ArReceivableApplicationGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 79 | ArReceivableApplicationGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 80 | ArReceivableApplicationGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 81 | ArReceivableApplicationGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 82 | ArReceivableApplicationGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 83 | ArReceivableApplicationGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 84 | ArReceivableApplicationGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 85 | ArReceivableApplicationGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 86 | ArReceivableApplicationGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 87 | ArReceivableApplicationGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 88 | ArReceivableApplicationGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 89 | ArReceivableApplicationGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 90 | ArReceivableApplicationGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 91 | ArReceivableApplicationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 92 | ArReceivableApplicationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 93 | ArReceivableApplicationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 94 | ArReceivableApplicationLineApplied | LINE_APPLIED | — | ✅ |
| 95 | ArReceivableApplicationLineEdiscounted | LINE_EDISCOUNTED | — | ✅ |
| 96 | ArReceivableApplicationLineUediscounted | LINE_UEDISCOUNTED | — | ✅ |
| 97 | ArReceivableApplicationLinkToCustomerTrxId | LINK_TO_CUSTOMER_TRX_ID | — | ✅ |
| 98 | ArReceivableApplicationLinkToTrxHistId | LINK_TO_TRX_HIST_ID | — | ✅ |
| 99 | ArReceivableApplicationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 100 | ArReceivableApplicationOrgId | ORG_ID | — | ✅ |
| 101 | ArReceivableApplicationPaymentScheduleId | PAYMENT_SCHEDULE_ID | — | ✅ |
| 102 | ArReceivableApplicationPaymentSetId | PAYMENT_SET_ID | — | ✅ |
| 103 | ArReceivableApplicationPostable | POSTABLE | — | ✅ |
| 104 | ArReceivableApplicationPostingControlId | POSTING_CONTROL_ID | — | ✅ |
| 105 | ArReceivableApplicationProgramApplicationId | PROGRAM_APPLICATION_ID | — | ✅ |
| 106 | ArReceivableApplicationProgramId | PROGRAM_ID | — | ✅ |
| 107 | ArReceivableApplicationProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 108 | ArReceivableApplicationReceivableApplicationId | RECEIVABLE_APPLICATION_ID | 🔑 | ✅ |
| 109 | ArReceivableApplicationReceivablesChargesApplied | RECEIVABLES_CHARGES_APPLIED | — | ✅ |
| 110 | ArReceivableApplicationReceivablesTrxId | RECEIVABLES_TRX_ID | — | ✅ |
| 111 | ArReceivableApplicationRequestId | REQUEST_ID | — | ✅ |
| 112 | ArReceivableApplicationReversalGlDate | REVERSAL_GL_DATE | — | ✅ |
| 113 | ArReceivableApplicationRuleSetId | RULE_SET_ID | — | ✅ |
| 114 | ArReceivableApplicationSecondaryApplicationRefId | SECONDARY_APPLICATION_REF_ID | — | ✅ |
| 115 | ArReceivableApplicationSecondaryApplicationRefNum | SECONDARY_APPLICATION_REF_NUM | — | ✅ |
| 116 | ArReceivableApplicationSecondaryApplicationRefType | SECONDARY_APPLICATION_REF_TYPE | — | ✅ |
| 117 | ArReceivableApplicationSetOfBooksId | SET_OF_BOOKS_ID | — | ✅ |
| 118 | ArReceivableApplicationStatus | STATUS | — | ✅ |
| 119 | ArReceivableApplicationTaxApplied | TAX_APPLIED | — | ✅ |
| 120 | ArReceivableApplicationTaxCode | TAX_CODE | — | ✅ |
| 121 | ArReceivableApplicationTaxEdiscounted | TAX_EDISCOUNTED | — | ✅ |
| 122 | ArReceivableApplicationTaxUediscounted | TAX_UEDISCOUNTED | — | ✅ |
| 123 | ArReceivableApplicationTransToReceiptRate | TRANS_TO_RECEIPT_RATE | — | ✅ |
| 124 | ArReceivableApplicationUnearnedDiscountCcid | UNEARNED_DISCOUNT_CCID | — | ✅ |
| 125 | ArReceivableApplicationUnearnedDiscountTaken | UNEARNED_DISCOUNT_TAKEN | — | ✅ |
| 126 | ArReceivableApplicationUnediscTaxAcctRule | UNEDISC_TAX_ACCT_RULE | — | ✅ |
| 127 | ArReceivableApplicationUpgradeMethod | UPGRADE_METHOD | — | ✅ |
| 128 | ArReceivableApplicationUssglTransactionCode | USSGL_TRANSACTION_CODE | — | ✅ |
| 129 | ArReceivableApplicationUssglTransactionCodeContext | USSGL_TRANSACTION_CODE_CONTEXT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
