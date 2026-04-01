---
id: DOC-OTHER-PVO-ReceiptHeaderExtractPVO
doc_type: system-doc
title: "ReceiptHeaderExtractPVO — PVO Cross-Module"
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
  - ReceiptHeaderExtractPVO
  - receiptheaderextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReceiptHeaderExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Receipt Header Extract. Acessa as tabelas: AR_CASH_RECEIPTS_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.ReceiptHeaderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 135 | 1 | 1 | 88 | 65% |

---

## 🔗 Tabelas Relacionadas

- [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]] — 135 atributos (1 PKs, 88 BICC)

---

## ⚙️ Atributos

### [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArCashReceiptActualValueDate | ACTUAL_VALUE_DATE | — | ✅ |
| 2 | ArCashReceiptAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | ✅ |
| 3 | ArCashReceiptAmount | AMOUNT | — | ✅ |
| 4 | ArCashReceiptAnticipatedClearingDate | ANTICIPATED_CLEARING_DATE | — | ✅ |
| 5 | ArCashReceiptApplicationNotes | APPLICATION_NOTES | — | ✅ |
| 6 | ArCashReceiptApprovalCode | APPROVAL_CODE | — | ✅ |
| 7 | ArCashReceiptAttribute1 | ATTRIBUTE1 | — | — |
| 8 | ArCashReceiptAttribute10 | ATTRIBUTE10 | — | — |
| 9 | ArCashReceiptAttribute11 | ATTRIBUTE11 | — | — |
| 10 | ArCashReceiptAttribute12 | ATTRIBUTE12 | — | — |
| 11 | ArCashReceiptAttribute13 | ATTRIBUTE13 | — | — |
| 12 | ArCashReceiptAttribute14 | ATTRIBUTE14 | — | — |
| 13 | ArCashReceiptAttribute15 | ATTRIBUTE15 | — | — |
| 14 | ArCashReceiptAttribute2 | ATTRIBUTE2 | — | — |
| 15 | ArCashReceiptAttribute3 | ATTRIBUTE3 | — | — |
| 16 | ArCashReceiptAttribute4 | ATTRIBUTE4 | — | — |
| 17 | ArCashReceiptAttribute5 | ATTRIBUTE5 | — | — |
| 18 | ArCashReceiptAttribute6 | ATTRIBUTE6 | — | — |
| 19 | ArCashReceiptAttribute7 | ATTRIBUTE7 | — | — |
| 20 | ArCashReceiptAttribute8 | ATTRIBUTE8 | — | — |
| 21 | ArCashReceiptAttribute9 | ATTRIBUTE9 | — | — |
| 22 | ArCashReceiptAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 23 | ArCashReceiptAutoapplyFlag | AUTOAPPLY_FLAG | — | ✅ |
| 24 | ArCashReceiptAutomatchRequestId | AUTOMATCH_REQUEST_ID | — | ✅ |
| 25 | ArCashReceiptAxAccountedFlag | AX_ACCOUNTED_FLAG | — | ✅ |
| 26 | ArCashReceiptCashReceiptId | CASH_RECEIPT_ID | 🔑 | ✅ |
| 27 | ArCashReceiptCcErrorCode | CC_ERROR_CODE | — | ✅ |
| 28 | ArCashReceiptCcErrorFlag | CC_ERROR_FLAG | — | ✅ |
| 29 | ArCashReceiptCcErrorText | CC_ERROR_TEXT | — | ✅ |
| 30 | ArCashReceiptCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 31 | ArCashReceiptCollectorId | COLLECTOR_ID | — | ✅ |
| 32 | ArCashReceiptComments | COMMENTS | — | ✅ |
| 33 | ArCashReceiptConfirmedFlag | CONFIRMED_FLAG | — | ✅ |
| 34 | ArCashReceiptCreatedBy | CREATED_BY | — | ✅ |
| 35 | ArCashReceiptCreationDate | CREATION_DATE | — | ✅ |
| 36 | ArCashReceiptCurrencyCode | CURRENCY_CODE | — | ✅ |
| 37 | ArCashReceiptCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | ✅ |
| 38 | ArCashReceiptCustomerBankBranchId | CUSTOMER_BANK_BRANCH_ID | — | ✅ |
| 39 | ArCashReceiptCustomerReceiptReference | CUSTOMER_RECEIPT_REFERENCE | — | ✅ |
| 40 | ArCashReceiptCustomerSiteUseId | CUSTOMER_SITE_USE_ID | — | ✅ |
| 41 | ArCashReceiptDepositDate | DEPOSIT_DATE | — | ✅ |
| 42 | ArCashReceiptDistributionSetId | DISTRIBUTION_SET_ID | — | ✅ |
| 43 | ArCashReceiptDocSequenceId | DOC_SEQUENCE_ID | — | ✅ |
| 44 | ArCashReceiptDocSequenceValue | DOC_SEQUENCE_VALUE | — | ✅ |
| 45 | ArCashReceiptExchangeDate | EXCHANGE_DATE | — | ✅ |
| 46 | ArCashReceiptExchangeRate | EXCHANGE_RATE | — | ✅ |
| 47 | ArCashReceiptExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 48 | ArCashReceiptFactorDiscountAmount | FACTOR_DISCOUNT_AMOUNT | — | ✅ |
| 49 | ArCashReceiptGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 50 | ArCashReceiptGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 51 | ArCashReceiptGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 52 | ArCashReceiptGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 53 | ArCashReceiptGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 54 | ArCashReceiptGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 55 | ArCashReceiptGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 56 | ArCashReceiptGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 57 | ArCashReceiptGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 58 | ArCashReceiptGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 59 | ArCashReceiptGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 60 | ArCashReceiptGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 61 | ArCashReceiptGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 62 | ArCashReceiptGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 63 | ArCashReceiptGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 64 | ArCashReceiptGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 65 | ArCashReceiptGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 66 | ArCashReceiptGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 67 | ArCashReceiptGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 68 | ArCashReceiptGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 69 | ArCashReceiptGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 70 | ArCashReceiptGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 71 | ArCashReceiptGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 72 | ArCashReceiptGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 73 | ArCashReceiptGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 74 | ArCashReceiptGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 75 | ArCashReceiptGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 76 | ArCashReceiptGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 77 | ArCashReceiptGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 78 | ArCashReceiptGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 79 | ArCashReceiptGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 80 | ArCashReceiptIssueDate | ISSUE_DATE | — | ✅ |
| 81 | ArCashReceiptIssuerBankBranchId | ISSUER_BANK_BRANCH_ID | — | ✅ |
| 82 | ArCashReceiptIssuerName | ISSUER_NAME | — | ✅ |
| 83 | ArCashReceiptLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 84 | ArCashReceiptLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 85 | ArCashReceiptLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 86 | ArCashReceiptLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 87 | ArCashReceiptLogicalGroupReference | LOGICAL_GROUP_REFERENCE | — | ✅ |
| 88 | ArCashReceiptMiscPaymentSource | MISC_PAYMENT_SOURCE | — | ✅ |
| 89 | ArCashReceiptObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 90 | ArCashReceiptOldCustomerBankAccountId | OLD_CUSTOMER_BANK_ACCOUNT_ID | — | ✅ |
| 91 | ArCashReceiptOldCustomerBankBranchId | OLD_CUSTOMER_BANK_BRANCH_ID | — | ✅ |
| 92 | ArCashReceiptOldIssuerBankBranchId | OLD_ISSUER_BANK_BRANCH_ID | — | ✅ |
| 93 | ArCashReceiptOrgId | ORG_ID | — | ✅ |
| 94 | ArCashReceiptOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | ✅ |
| 95 | ArCashReceiptPayFromCustomer | PAY_FROM_CUSTOMER | — | ✅ |
| 96 | ArCashReceiptPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | ✅ |
| 97 | ArCashReceiptPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | ✅ |
| 98 | ArCashReceiptPostmarkDate | POSTMARK_DATE | — | ✅ |
| 99 | ArCashReceiptPrevCustomerSiteUseId | PREV_CUSTOMER_SITE_USE_ID | — | ✅ |
| 100 | ArCashReceiptPrevPayFromCustomer | PREV_PAY_FROM_CUSTOMER | — | ✅ |
| 101 | ArCashReceiptProgramApplicationId | PROGRAM_APPLICATION_ID | — | ✅ |
| 102 | ArCashReceiptProgramId | PROGRAM_ID | — | ✅ |
| 103 | ArCashReceiptProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 104 | ArCashReceiptPromiseSource | PROMISE_SOURCE | — | ✅ |
| 105 | ArCashReceiptRecVersionNumber | REC_VERSION_NUMBER | — | ✅ |
| 106 | ArCashReceiptReceiptBatchId | RECEIPT_BATCH_ID | — | ✅ |
| 107 | ArCashReceiptReceiptDate | RECEIPT_DATE | — | ✅ |
| 108 | ArCashReceiptReceiptMethodId | RECEIPT_METHOD_ID | — | ✅ |
| 109 | ArCashReceiptReceiptNumber | RECEIPT_NUMBER | — | ✅ |
| 110 | ArCashReceiptReceivablesTrxId | RECEIVABLES_TRX_ID | — | ✅ |
| 111 | ArCashReceiptRecommendationCount | RECOMMENDATION_COUNT | — | ✅ |
| 112 | ArCashReceiptReconFlag | RECON_FLAG | — | ✅ |
| 113 | ArCashReceiptReferenceId | REFERENCE_ID | — | ✅ |
| 114 | ArCashReceiptReferenceType | REFERENCE_TYPE | — | ✅ |
| 115 | ArCashReceiptRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | ✅ |
| 116 | ArCashReceiptRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | ✅ |
| 117 | ArCashReceiptRemittanceBatchId | REMITTANCE_BATCH_ID | — | ✅ |
| 118 | ArCashReceiptRequestId | REQUEST_ID | — | ✅ |
| 119 | ArCashReceiptResourceId | RESOURCE_ID | — | ✅ |
| 120 | ArCashReceiptReversalCategory | REVERSAL_CATEGORY | — | ✅ |
| 121 | ArCashReceiptReversalComments | REVERSAL_COMMENTS | — | ✅ |
| 122 | ArCashReceiptReversalDate | REVERSAL_DATE | — | ✅ |
| 123 | ArCashReceiptReversalReasonCode | REVERSAL_REASON_CODE | — | ✅ |
| 124 | ArCashReceiptSelectedForFactoringFlag | SELECTED_FOR_FACTORING_FLAG | — | ✅ |
| 125 | ArCashReceiptSelectedRemittanceBatchId | SELECTED_REMITTANCE_BATCH_ID | — | ✅ |
| 126 | ArCashReceiptSetOfBooksId | SET_OF_BOOKS_ID | — | ✅ |
| 127 | ArCashReceiptStatus | STATUS | — | ✅ |
| 128 | ArCashReceiptStructuredPaymentReference | STRUCTURED_PAYMENT_REFERENCE | — | ✅ |
| 129 | ArCashReceiptTaxAmount | TAX_AMOUNT | — | ✅ |
| 130 | ArCashReceiptTaxRate | TAX_RATE | — | ✅ |
| 131 | ArCashReceiptType | TYPE | — | ✅ |
| 132 | ArCashReceiptUniqueReference | UNIQUE_REFERENCE | — | ✅ |
| 133 | ArCashReceiptUssglTransactionCode | USSGL_TRANSACTION_CODE | — | ✅ |
| 134 | ArCashReceiptUssglTransactionCodeContext | USSGL_TRANSACTION_CODE_CONTEXT | — | ✅ |
| 135 | ArCashReceiptVatTaxId | VAT_TAX_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
