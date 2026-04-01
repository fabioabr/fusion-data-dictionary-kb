---
id: DOC-AR-PVO-ReceiptHistoryPVO
doc_type: system-doc
title: "ReceiptHistoryPVO — PVO Accounts Receivable"
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
  - ReceiptHistoryPVO
  - receipthistorypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReceiptHistoryPVO

## 📌 Visão Geral

Extrai o histórico completo de eventos dos recebimentos (criação, confirmação, estorno, compensação), com datas, valores e responsáveis. Fornece trilha de auditoria completa do ciclo de vida de cada recebimento para compliance e análise operacional.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.ReceiptHistoryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 319 | 9 | 1 | 33 | 10% |

---

## 🔗 Tabelas Relacionadas

- [[ar_batches_all|AR_BATCHES_ALL]] — 46 atributos (1 BICC)
- [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]] — 85 atributos (3 BICC)
- [[ar_cash_receipt_history_all|AR_CASH_RECEIPT_HISTORY_ALL]] — 147 atributos (1 PKs, 26 BICC)
- [[ar_payment_schedules_all|AR_PAYMENT_SCHEDULES_ALL]] — 2 atributos (1 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 1 atributos
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 18 atributos (2 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 3 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos
- [[per_users|PER_USERS]] — 7 atributos

---

## ⚙️ Atributos

### [[ar_batches_all|AR_BATCHES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BatchAutoPrintProgramId | AUTO_PRINT_PROGRAM_ID | — | — |
| 2 | BatchAutoTransProgramId | AUTO_TRANS_PROGRAM_ID | — | — |
| 3 | BatchBankDepositNumber | BANK_DEPOSIT_NUMBER | — | — |
| 4 | BatchBatchAppliedStatus | BATCH_APPLIED_STATUS | — | — |
| 5 | BatchBatchDate | BATCH_DATE | — | — |
| 6 | BatchBatchId | BATCH_ID | — | — |
| 7 | BatchBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 8 | BatchClosedDate | CLOSED_DATE | — | — |
| 9 | BatchControlAmount | CONTROL_AMOUNT | — | — |
| 10 | BatchControlCount | CONTROL_COUNT | — | — |
| 11 | BatchCreatedBy | CREATED_BY | — | — |
| 12 | BatchCreationDate | CREATION_DATE | — | — |
| 13 | BatchCurrencyCode | CURRENCY_CODE | — | — |
| 14 | BatchDepositDate | DEPOSIT_DATE | — | — |
| 15 | BatchExchangeDate | EXCHANGE_DATE | — | — |
| 16 | BatchExchangeRate | EXCHANGE_RATE | — | — |
| 17 | BatchExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 18 | BatchGlDate | GL_DATE | — | — |
| 19 | BatchLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | BatchLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | BatchLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 22 | BatchLockboxBatchName | LOCKBOX_BATCH_NAME | — | — |
| 23 | BatchLockboxId | LOCKBOX_ID | — | — |
| 24 | BatchMediaReference | MEDIA_REFERENCE | — | — |
| 25 | BatchName | NAME | — | — |
| 26 | BatchObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 27 | BatchOldRemittanceBankBranchId | OLD_REMITTANCE_BANK_BRANCH_ID | — | — |
| 28 | BatchOperationRequestId | OPERATION_REQUEST_ID | — | — |
| 29 | BatchOrgId | ORG_ID | — | — |
| 30 | BatchProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 31 | BatchProgramId | PROGRAM_ID | — | — |
| 32 | BatchProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 33 | BatchPurgedChildrenFlag | PURGED_CHILDREN_FLAG | — | — |
| 34 | BatchReceiptClassId | RECEIPT_CLASS_ID | — | — |
| 35 | BatchReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 36 | BatchRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 37 | BatchRemitMethodCode | REMIT_METHOD_CODE | — | — |
| 38 | BatchRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 39 | BatchRemittanceBankBranchId | REMITTANCE_BANK_BRANCH_ID | — | — |
| 40 | BatchRequestId | REQUEST_ID | — | — |
| 41 | BatchSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 42 | BatchStatus | STATUS | — | — |
| 43 | BatchTransmissionId | TRANSMISSION_ID | — | — |
| 44 | BatchTransmissionRequestId | TRANSMISSION_REQUEST_ID | — | — |
| 45 | BatchType | TYPE | — | — |
| 46 | BatchWithRecourseFlag | WITH_RECOURSE_FLAG | — | — |

### [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReceiptActualValueDate | ACTUAL_VALUE_DATE | — | — |
| 2 | ReceiptAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 3 | ReceiptAmount | AMOUNT | — | — |
| 4 | ReceiptAnticipatedClearingDate | ANTICIPATED_CLEARING_DATE | — | — |
| 5 | ReceiptApplicationNotes | APPLICATION_NOTES | — | — |
| 6 | ReceiptApprovalCode | APPROVAL_CODE | — | — |
| 7 | ReceiptAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 8 | ReceiptAutoapplyFlag | AUTOAPPLY_FLAG | — | — |
| 9 | ReceiptAutomatchRequestId | AUTOMATCH_REQUEST_ID | — | — |
| 10 | ReceiptAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 11 | ReceiptCashReceiptId | CASH_RECEIPT_ID | — | — |
| 12 | ReceiptCcErrorCode | CC_ERROR_CODE | — | — |
| 13 | ReceiptCcErrorFlag | CC_ERROR_FLAG | — | — |
| 14 | ReceiptCcErrorText | CC_ERROR_TEXT | — | — |
| 15 | ReceiptCollectorId | COLLECTOR_ID | — | — |
| 16 | ReceiptComments | COMMENTS | — | — |
| 17 | ReceiptConfirmedFlag | CONFIRMED_FLAG | — | — |
| 18 | ReceiptCreatedBy | CREATED_BY | — | — |
| 19 | ReceiptCreationDate | CREATION_DATE | — | — |
| 20 | ReceiptCurrencyCode | CURRENCY_CODE | — | — |
| 21 | ReceiptCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 22 | ReceiptCustomerBankBranchId | CUSTOMER_BANK_BRANCH_ID | — | — |
| 23 | ReceiptCustomerReceiptReference | CUSTOMER_RECEIPT_REFERENCE | — | — |
| 24 | ReceiptCustomerSiteUseId | CUSTOMER_SITE_USE_ID | — | — |
| 25 | ReceiptDepositDate | DEPOSIT_DATE | — | — |
| 26 | ReceiptDistributionSetId | DISTRIBUTION_SET_ID | — | — |
| 27 | ReceiptDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 28 | ReceiptDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 29 | ReceiptExchangeDate | EXCHANGE_DATE | — | — |
| 30 | ReceiptExchangeRate | EXCHANGE_RATE | — | — |
| 31 | ReceiptExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 32 | ReceiptFactorDiscountAmount | FACTOR_DISCOUNT_AMOUNT | — | — |
| 33 | ReceiptIssueDate | ISSUE_DATE | — | — |
| 34 | ReceiptIssuerBankBranchId | ISSUER_BANK_BRANCH_ID | — | — |
| 35 | ReceiptIssuerName | ISSUER_NAME | — | — |
| 36 | ReceiptLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 37 | ReceiptLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 38 | ReceiptLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 39 | ReceiptLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 40 | ReceiptLogicalGroupReference | LOGICAL_GROUP_REFERENCE | — | — |
| 41 | ReceiptMiscPaymentSource | MISC_PAYMENT_SOURCE | — | — |
| 42 | ReceiptObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 43 | ReceiptOldCustomerBankAccountId | OLD_CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 44 | ReceiptOldCustomerBankBranchId | OLD_CUSTOMER_BANK_BRANCH_ID | — | — |
| 45 | ReceiptOldIssuerBankBranchId | OLD_ISSUER_BANK_BRANCH_ID | — | — |
| 46 | ReceiptOrgId | ORG_ID | — | — |
| 47 | ReceiptOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 48 | ReceiptPayFromCustomer | PAY_FROM_CUSTOMER | — | — |
| 49 | ReceiptPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 50 | ReceiptPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 51 | ReceiptPostmarkDate | POSTMARK_DATE | — | — |
| 52 | ReceiptProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 53 | ReceiptProgramId | PROGRAM_ID | — | — |
| 54 | ReceiptProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 55 | ReceiptPromiseSource | PROMISE_SOURCE | — | — |
| 56 | ReceiptRecVersionNumber | REC_VERSION_NUMBER | — | — |
| 57 | ReceiptReceiptCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 58 | ReceiptReceiptDate | RECEIPT_DATE | — | — |
| 59 | ReceiptReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 60 | ReceiptReceiptNumber | RECEIPT_NUMBER | — | ✅ |
| 61 | ReceiptReceiptReceiptBatchId | RECEIPT_BATCH_ID | — | — |
| 62 | ReceiptReceivablesTrxId | RECEIVABLES_TRX_ID | — | — |
| 63 | ReceiptReconFlag | RECON_FLAG | — | — |
| 64 | ReceiptReferenceId | REFERENCE_ID | — | — |
| 65 | ReceiptReferenceType | REFERENCE_TYPE | — | — |
| 66 | ReceiptRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 67 | ReceiptRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 68 | ReceiptRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 69 | ReceiptRequestId | REQUEST_ID | — | — |
| 70 | ReceiptResourceId | RESOURCE_ID | — | — |
| 71 | ReceiptReversalCategory | REVERSAL_CATEGORY | — | — |
| 72 | ReceiptReversalComments | REVERSAL_COMMENTS | — | — |
| 73 | ReceiptReversalDate | REVERSAL_DATE | — | — |
| 74 | ReceiptReversalReasonCode | REVERSAL_REASON_CODE | — | — |
| 75 | ReceiptSelectedForFactoringFlag | SELECTED_FOR_FACTORING_FLAG | — | — |
| 76 | ReceiptSelectedRemittanceBatchId | SELECTED_REMITTANCE_BATCH_ID | — | — |
| 77 | ReceiptSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 78 | ReceiptStatus | STATUS | — | — |
| 79 | ReceiptTaxAmount | TAX_AMOUNT | — | — |
| 80 | ReceiptTaxRate | TAX_RATE | — | — |
| 81 | ReceiptType | TYPE | — | ✅ |
| 82 | ReceiptUniqueReference | UNIQUE_REFERENCE | — | — |
| 83 | ReceiptUssglTransactionCode | USSGL_TRANSACTION_CODE | — | — |
| 84 | ReceiptUssglTransactionCodeContext | USSGL_TRANSACTION_CODE_CONTEXT | — | — |
| 85 | ReceiptVatTaxId | VAT_TAX_ID | — | — |

### [[ar_cash_receipt_history_all|AR_CASH_RECEIPT_HISTORY_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CashReceiptHistoryId | CASH_RECEIPT_HISTORY_ID | 🔑 | ✅ |
| 2 | HistoryAccountCodeCombinationId | ACCOUNT_CODE_COMBINATION_ID | — | — |
| 3 | HistoryAcctdAmount | ACCTD_AMOUNT | — | ✅ |
| 4 | HistoryAcctdFactorDiscountAmount | ACCTD_FACTOR_DISCOUNT_AMOUNT | — | ✅ |
| 5 | HistoryAmount | AMOUNT | — | ✅ |
| 6 | HistoryBankChargeAccountCcid | BANK_CHARGE_ACCOUNT_CCID | — | — |
| 7 | HistoryBatchId | BATCH_ID | — | — |
| 8 | HistoryCashReceiptId | CASH_RECEIPT_ID | — | — |
| 9 | HistoryCreatedBy | CREATED_BY | — | ✅ |
| 10 | HistoryCreatedFrom | CREATED_FROM | — | — |
| 11 | HistoryCreationDate | CREATION_DATE | — | ✅ |
| 12 | HistoryCurrentRecordFlag | CURRENT_RECORD_FLAG | — | ✅ |
| 13 | HistoryEventId | EVENT_ID | — | ✅ |
| 14 | HistoryExchangeDate | EXCHANGE_DATE | — | ✅ |
| 15 | HistoryExchangeRate | EXCHANGE_RATE | — | ✅ |
| 16 | HistoryExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 17 | HistoryFactorDiscountAmount | FACTOR_DISCOUNT_AMOUNT | — | ✅ |
| 18 | HistoryFactorFlag | FACTOR_FLAG | — | — |
| 19 | HistoryFirstPostedRecordFlag | FIRST_POSTED_RECORD_FLAG | — | ✅ |
| 20 | HistoryGlDate | GL_DATE | — | ✅ |
| 21 | HistoryGlPostedDate | GL_POSTED_DATE | — | ✅ |
| 22 | HistoryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | HistoryLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 24 | HistoryLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 25 | HistoryMrcAcctdAmount | MRC_ACCTD_AMOUNT | — | — |
| 26 | HistoryMrcAcctdFactorDiscAmount | MRC_ACCTD_FACTOR_DISC_AMOUNT | — | — |
| 27 | HistoryMrcExchangeDate | MRC_EXCHANGE_DATE | — | — |
| 28 | HistoryMrcExchangeRate | MRC_EXCHANGE_RATE | — | — |
| 29 | HistoryMrcExchangeRateType | MRC_EXCHANGE_RATE_TYPE | — | — |
| 30 | HistoryMrcGlPostedDate | MRC_GL_POSTED_DATE | — | — |
| 31 | HistoryMrcPostingControlId | MRC_POSTING_CONTROL_ID | — | — |
| 32 | HistoryMrcReversalGlPostedDate | MRC_REVERSAL_GL_POSTED_DATE | — | — |
| 33 | HistoryNoteStatus | NOTE_STATUS | — | — |
| 34 | HistoryObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 35 | HistoryOrgId | ORG_ID | — | — |
| 36 | HistoryPostableFlag | POSTABLE_FLAG | — | ✅ |
| 37 | HistoryPostingControlId | POSTING_CONTROL_ID | — | ✅ |
| 38 | HistoryProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 39 | HistoryProgramId | PROGRAM_ID | — | — |
| 40 | HistoryProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 41 | HistoryPrvStatCashReceiptHistId | PRV_STAT_CASH_RECEIPT_HIST_ID | — | — |
| 42 | HistoryRequestId | REQUEST_ID | — | — |
| 43 | HistoryReversalCashReceiptHistId | REVERSAL_CASH_RECEIPT_HIST_ID | — | — |
| 44 | HistoryReversalCreatedFrom | REVERSAL_CREATED_FROM | — | — |
| 45 | HistoryReversalGlDate | REVERSAL_GL_DATE | — | ✅ |
| 46 | HistoryReversalGlPostedDate | REVERSAL_GL_POSTED_DATE | — | ✅ |
| 47 | HistoryReversalPostingControlId | REVERSAL_POSTING_CONTROL_ID | — | — |
| 48 | HistoryStatus | STATUS | — | ✅ |
| 49 | HistoryTrxDate | TRX_DATE | — | ✅ |
| 50 | PrvStatHistoryAccountCodeCombinationId | ACCOUNT_CODE_COMBINATION_ID | — | — |
| 51 | PrvStatHistoryAcctdAmount | ACCTD_AMOUNT | — | — |
| 52 | PrvStatHistoryAcctdFactorDiscountAmount | ACCTD_FACTOR_DISCOUNT_AMOUNT | — | — |
| 53 | PrvStatHistoryAmount | AMOUNT | — | — |
| 54 | PrvStatHistoryBankChargeAccountCcid | BANK_CHARGE_ACCOUNT_CCID | — | — |
| 55 | PrvStatHistoryBatchId | BATCH_ID | — | — |
| 56 | PrvStatHistoryCashReceiptHistoryId | CASH_RECEIPT_HISTORY_ID | — | — |
| 57 | PrvStatHistoryCashReceiptId | CASH_RECEIPT_ID | — | — |
| 58 | PrvStatHistoryCreatedBy | CREATED_BY | — | — |
| 59 | PrvStatHistoryCreatedFrom | CREATED_FROM | — | — |
| 60 | PrvStatHistoryCreationDate | CREATION_DATE | — | — |
| 61 | PrvStatHistoryCurrentRecordFlag | CURRENT_RECORD_FLAG | — | — |
| 62 | PrvStatHistoryEventId | EVENT_ID | — | — |
| 63 | PrvStatHistoryExchangeDate | EXCHANGE_DATE | — | — |
| 64 | PrvStatHistoryExchangeRate | EXCHANGE_RATE | — | — |
| 65 | PrvStatHistoryExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 66 | PrvStatHistoryFactorDiscountAmount | FACTOR_DISCOUNT_AMOUNT | — | — |
| 67 | PrvStatHistoryFactorFlag | FACTOR_FLAG | — | — |
| 68 | PrvStatHistoryFirstPostedRecordFlag | FIRST_POSTED_RECORD_FLAG | — | — |
| 69 | PrvStatHistoryGlDate | GL_DATE | — | — |
| 70 | PrvStatHistoryGlPostedDate | GL_POSTED_DATE | — | — |
| 71 | PrvStatHistoryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 72 | PrvStatHistoryLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 73 | PrvStatHistoryLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 74 | PrvStatHistoryMrcAcctdAmount | MRC_ACCTD_AMOUNT | — | — |
| 75 | PrvStatHistoryMrcAcctdFactorDiscAmount | MRC_ACCTD_FACTOR_DISC_AMOUNT | — | — |
| 76 | PrvStatHistoryMrcExchangeDate | MRC_EXCHANGE_DATE | — | — |
| 77 | PrvStatHistoryMrcExchangeRate | MRC_EXCHANGE_RATE | — | — |
| 78 | PrvStatHistoryMrcExchangeRateType | MRC_EXCHANGE_RATE_TYPE | — | — |
| 79 | PrvStatHistoryMrcGlPostedDate | MRC_GL_POSTED_DATE | — | — |
| 80 | PrvStatHistoryMrcPostingControlId | MRC_POSTING_CONTROL_ID | — | — |
| 81 | PrvStatHistoryMrcReversalGlPostedDate | MRC_REVERSAL_GL_POSTED_DATE | — | — |
| 82 | PrvStatHistoryNoteStatus | NOTE_STATUS | — | — |
| 83 | PrvStatHistoryObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 84 | PrvStatHistoryOrgId | ORG_ID | — | — |
| 85 | PrvStatHistoryPostableFlag | POSTABLE_FLAG | — | — |
| 86 | PrvStatHistoryPostingControlId | POSTING_CONTROL_ID | — | — |
| 87 | PrvStatHistoryProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 88 | PrvStatHistoryProgramId | PROGRAM_ID | — | — |
| 89 | PrvStatHistoryProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 90 | PrvStatHistoryPrvStatCashReceiptHistId | PRV_STAT_CASH_RECEIPT_HIST_ID | — | — |
| 91 | PrvStatHistoryRequestId | REQUEST_ID | — | — |
| 92 | PrvStatHistoryReversalCashReceiptHistId | REVERSAL_CASH_RECEIPT_HIST_ID | — | — |
| 93 | PrvStatHistoryReversalCreatedFrom | REVERSAL_CREATED_FROM | — | — |
| 94 | PrvStatHistoryReversalGlDate | REVERSAL_GL_DATE | — | — |
| 95 | PrvStatHistoryReversalGlPostedDate | REVERSAL_GL_POSTED_DATE | — | — |
| 96 | PrvStatHistoryReversalPostingControlId | REVERSAL_POSTING_CONTROL_ID | — | — |
| 97 | PrvStatHistoryStatus | STATUS | — | ✅ |
| 98 | PrvStatHistoryTrxDate | TRX_DATE | — | — |
| 99 | RevHistoryAccountCodeCombinationId | ACCOUNT_CODE_COMBINATION_ID | — | — |
| 100 | RevHistoryAcctdAmount | ACCTD_AMOUNT | — | — |
| 101 | RevHistoryAcctdFactorDiscountAmount | ACCTD_FACTOR_DISCOUNT_AMOUNT | — | — |
| 102 | RevHistoryAmount | AMOUNT | — | — |
| 103 | RevHistoryBankChargeAccountCcid | BANK_CHARGE_ACCOUNT_CCID | — | — |
| 104 | RevHistoryBatchId | BATCH_ID | — | — |
| 105 | RevHistoryCashReceiptHistoryId | CASH_RECEIPT_HISTORY_ID | — | — |
| 106 | RevHistoryCashReceiptId | CASH_RECEIPT_ID | — | — |
| 107 | RevHistoryCreatedBy | CREATED_BY | — | — |
| 108 | RevHistoryCreatedFrom | CREATED_FROM | — | — |
| 109 | RevHistoryCreationDate | CREATION_DATE | — | — |
| 110 | RevHistoryCurrentRecordFlag | CURRENT_RECORD_FLAG | — | — |
| 111 | RevHistoryEventId | EVENT_ID | — | — |
| 112 | RevHistoryExchangeDate | EXCHANGE_DATE | — | — |
| 113 | RevHistoryExchangeRate | EXCHANGE_RATE | — | — |
| 114 | RevHistoryExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 115 | RevHistoryFactorDiscountAmount | FACTOR_DISCOUNT_AMOUNT | — | — |
| 116 | RevHistoryFactorFlag | FACTOR_FLAG | — | — |
| 117 | RevHistoryFirstPostedRecordFlag | FIRST_POSTED_RECORD_FLAG | — | — |
| 118 | RevHistoryGlDate | GL_DATE | — | — |
| 119 | RevHistoryGlPostedDate | GL_POSTED_DATE | — | — |
| 120 | RevHistoryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 121 | RevHistoryLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 122 | RevHistoryLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 123 | RevHistoryMrcAcctdAmount | MRC_ACCTD_AMOUNT | — | — |
| 124 | RevHistoryMrcAcctdFactorDiscAmount | MRC_ACCTD_FACTOR_DISC_AMOUNT | — | — |
| 125 | RevHistoryMrcExchangeDate | MRC_EXCHANGE_DATE | — | — |
| 126 | RevHistoryMrcExchangeRate | MRC_EXCHANGE_RATE | — | — |
| 127 | RevHistoryMrcExchangeRateType | MRC_EXCHANGE_RATE_TYPE | — | — |
| 128 | RevHistoryMrcGlPostedDate | MRC_GL_POSTED_DATE | — | — |
| 129 | RevHistoryMrcPostingControlId | MRC_POSTING_CONTROL_ID | — | — |
| 130 | RevHistoryMrcReversalGlPostedDate | MRC_REVERSAL_GL_POSTED_DATE | — | — |
| 131 | RevHistoryNoteStatus | NOTE_STATUS | — | — |
| 132 | RevHistoryObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 133 | RevHistoryOrgId | ORG_ID | — | — |
| 134 | RevHistoryPostableFlag | POSTABLE_FLAG | — | — |
| 135 | RevHistoryPostingControlId | POSTING_CONTROL_ID | — | — |
| 136 | RevHistoryProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 137 | RevHistoryProgramId | PROGRAM_ID | — | — |
| 138 | RevHistoryProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 139 | RevHistoryPrvStatCashReceiptHistId | PRV_STAT_CASH_RECEIPT_HIST_ID | — | — |
| 140 | RevHistoryRequestId | REQUEST_ID | — | — |
| 141 | RevHistoryReversalCashReceiptHistId | REVERSAL_CASH_RECEIPT_HIST_ID | — | — |
| 142 | RevHistoryReversalCreatedFrom | REVERSAL_CREATED_FROM | — | — |
| 143 | RevHistoryReversalGlDate | REVERSAL_GL_DATE | — | — |
| 144 | RevHistoryReversalGlPostedDate | REVERSAL_GL_POSTED_DATE | — | — |
| 145 | RevHistoryReversalPostingControlId | REVERSAL_POSTING_CONTROL_ID | — | — |
| 146 | RevHistoryStatus | STATUS | — | — |
| 147 | RevHistoryTrxDate | TRX_DATE | — | — |

### [[ar_payment_schedules_all|AR_PAYMENT_SCHEDULES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentSchedulesDueDate | DUE_DATE | — | ✅ |
| 2 | PaymentSchedulesPaymentScheduleId | PAYMENT_SCHEDULE_ID | — | — |

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitBusinessUnitId | BU_ID | — | — |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DailyConvTypeConversionType | CONVERSION_TYPE | — | — |
| 2 | DailyConvTypeCreatedBy | CREATED_BY | — | — |
| 3 | DailyConvTypeCreationDate | CREATION_DATE | — | — |
| 4 | DailyConvTypeDescription | DESCRIPTION | — | — |
| 5 | DailyConvTypeEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 6 | DailyConvTypeEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 7 | DailyConvTypeFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 8 | DailyConvTypeFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 9 | DailyConvTypeFemScenario | FEM_SCENARIO | — | — |
| 10 | DailyConvTypeFemTimeframe | FEM_TIMEFRAME | — | — |
| 11 | DailyConvTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | DailyConvTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | DailyConvTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | DailyConvTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | DailyConvTypePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 16 | DailyConvTypeSecurityFlag | SECURITY_FLAG | — | — |
| 17 | DailyConvTypeUserConversionType | USER_CONVERSION_TYPE | — | ✅ |
| 18 | DailyConvTypeUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 2 | LedgersLedgerId | LEDGER_ID | — | — |
| 3 | LedgersObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | — |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | — |
| 7 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | PersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserCreatedByUserGuid | USER_GUID | — | — |
| 2 | UserCreatedByUserId | USER_ID | — | — |
| 3 | UserCreatedByUsername | USERNAME | — | — |
| 4 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 5 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 6 | UserUpdatedByUserId | USER_ID | — | — |
| 7 | UserUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
