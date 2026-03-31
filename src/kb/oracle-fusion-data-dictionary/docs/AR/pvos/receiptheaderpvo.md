---
id: DOC-AR-PVO-ReceiptHeaderPVO
doc_type: system-doc
title: "ReceiptHeaderPVO — PVO Accounts Receivable"
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
  - ReceiptHeaderPVO
  - receiptheaderpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReceiptHeaderPVO

## 📌 Visão Geral

Extrai os recebimentos de clientes (cash receipts), incluindo valor, método de recebimento, status, data, conta bancária e dados de câmbio. Permite análise de fluxo de caixa, reconciliação bancária, acompanhamento de inadimplência e gestão de tesouraria.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.ReceiptHeaderPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 749 | 19 | 1 | 58 | 8% |

---

## 🔗 Tabelas Relacionadas

- [[ar_batches_all|AR_BATCHES_ALL]] — 92 atributos (5 BICC)
- [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]] — 83 atributos (1 PKs, 29 BICC)
- [[ar_cash_receipt_history_all|AR_CASH_RECEIPT_HISTORY_ALL]] — 37 atributos
- [[ar_collectors|AR_COLLECTORS]] — 12 atributos (1 BICC)
- [[ar_distribution_sets_all|AR_DISTRIBUTION_SETS_ALL]] — 12 atributos (2 BICC)
- [[ar_payment_schedules_all|AR_PAYMENT_SCHEDULES_ALL]] — 93 atributos (6 BICC)
- [[ar_receivables_trx_all|AR_RECEIVABLES_TRX_ALL]] — 20 atributos (1 BICC)
- [[ce_bank_acct_uses_all|CE_BANK_ACCT_USES_ALL]] — 30 atributos (1 BICC)
- [[ce_bank_branches_v|CE_BANK_BRANCHES_V]] — 132 atributos (1 BICC)
- [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]] — 5 atributos (1 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 1 atributos
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 12 atributos (1 BICC)
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 31 atributos (3 BICC)
- [[hz_parties|HZ_PARTIES]] — 5 atributos (1 BICC)
- [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]] — 98 atributos (4 BICC)
- [[iby_fndcpt_tx_extensions|IBY_FNDCPT_TX_EXTENSIONS]] — 14 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 23 atributos
- [[per_users|PER_USERS]] — 7 atributos
- [[zx_sco_rates|ZX_SCO_RATES]] — 42 atributos (1 BICC)

---

## ⚙️ Atributos

### [[ar_batches_all|AR_BATCHES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReceiptBatchAutoPrintProgramId | AUTO_PRINT_PROGRAM_ID | — | — |
| 2 | ReceiptBatchAutoTransProgramId | AUTO_TRANS_PROGRAM_ID | — | — |
| 3 | ReceiptBatchBankDepositNumber | BANK_DEPOSIT_NUMBER | — | — |
| 4 | ReceiptBatchBatchAppliedStatus | BATCH_APPLIED_STATUS | — | — |
| 5 | ReceiptBatchBatchDate | BATCH_DATE | — | — |
| 6 | ReceiptBatchBatchId | BATCH_ID | — | ✅ |
| 7 | ReceiptBatchBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 8 | ReceiptBatchClosedDate | CLOSED_DATE | — | — |
| 9 | ReceiptBatchControlAmount | CONTROL_AMOUNT | — | — |
| 10 | ReceiptBatchControlCount | CONTROL_COUNT | — | — |
| 11 | ReceiptBatchCreatedBy | CREATED_BY | — | — |
| 12 | ReceiptBatchCreationDate | CREATION_DATE | — | — |
| 13 | ReceiptBatchCurrencyCode | CURRENCY_CODE | — | — |
| 14 | ReceiptBatchDepositDate | DEPOSIT_DATE | — | — |
| 15 | ReceiptBatchExchangeDate | EXCHANGE_DATE | — | — |
| 16 | ReceiptBatchExchangeRate | EXCHANGE_RATE | — | — |
| 17 | ReceiptBatchExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 18 | ReceiptBatchGlDate | GL_DATE | — | — |
| 19 | ReceiptBatchLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | ReceiptBatchLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | ReceiptBatchLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 22 | ReceiptBatchLockboxBatchName | LOCKBOX_BATCH_NAME | — | — |
| 23 | ReceiptBatchLockboxId | LOCKBOX_ID | — | — |
| 24 | ReceiptBatchMediaReference | MEDIA_REFERENCE | — | — |
| 25 | ReceiptBatchName | NAME | — | ✅ |
| 26 | ReceiptBatchObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 27 | ReceiptBatchOldRemittanceBankBranchId | OLD_REMITTANCE_BANK_BRANCH_ID | — | — |
| 28 | ReceiptBatchOperationRequestId | OPERATION_REQUEST_ID | — | — |
| 29 | ReceiptBatchOrgId | ORG_ID | — | — |
| 30 | ReceiptBatchProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 31 | ReceiptBatchProgramId | PROGRAM_ID | — | — |
| 32 | ReceiptBatchProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 33 | ReceiptBatchPurgedChildrenFlag | PURGED_CHILDREN_FLAG | — | — |
| 34 | ReceiptBatchReceiptClassId | RECEIPT_CLASS_ID | — | — |
| 35 | ReceiptBatchReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 36 | ReceiptBatchRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 37 | ReceiptBatchRemitMethodCode | REMIT_METHOD_CODE | — | — |
| 38 | ReceiptBatchRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 39 | ReceiptBatchRemittanceBankBranchId | REMITTANCE_BANK_BRANCH_ID | — | — |
| 40 | ReceiptBatchRequestId | REQUEST_ID | — | — |
| 41 | ReceiptBatchSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 42 | ReceiptBatchStatus | STATUS | — | ✅ |
| 43 | ReceiptBatchTransmissionId | TRANSMISSION_ID | — | — |
| 44 | ReceiptBatchTransmissionRequestId | TRANSMISSION_REQUEST_ID | — | — |
| 45 | ReceiptBatchType | TYPE | — | — |
| 46 | ReceiptBatchWithRecourseFlag | WITH_RECOURSE_FLAG | — | — |
| 47 | RemittanceBatchAutoPrintProgramId | AUTO_PRINT_PROGRAM_ID | — | — |
| 48 | RemittanceBatchAutoTransProgramId | AUTO_TRANS_PROGRAM_ID | — | — |
| 49 | RemittanceBatchBankDepositNumber | BANK_DEPOSIT_NUMBER | — | — |
| 50 | RemittanceBatchBatchAppliedStatus | BATCH_APPLIED_STATUS | — | — |
| 51 | RemittanceBatchBatchDate | BATCH_DATE | — | — |
| 52 | RemittanceBatchBatchId | BATCH_ID | — | — |
| 53 | RemittanceBatchBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 54 | RemittanceBatchClosedDate | CLOSED_DATE | — | — |
| 55 | RemittanceBatchControlAmount | CONTROL_AMOUNT | — | — |
| 56 | RemittanceBatchControlCount | CONTROL_COUNT | — | — |
| 57 | RemittanceBatchCreatedBy | CREATED_BY | — | — |
| 58 | RemittanceBatchCreationDate | CREATION_DATE | — | — |
| 59 | RemittanceBatchCurrencyCode | CURRENCY_CODE | — | — |
| 60 | RemittanceBatchDepositDate | DEPOSIT_DATE | — | — |
| 61 | RemittanceBatchExchangeDate | EXCHANGE_DATE | — | — |
| 62 | RemittanceBatchExchangeRate | EXCHANGE_RATE | — | — |
| 63 | RemittanceBatchExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 64 | RemittanceBatchGlDate | GL_DATE | — | — |
| 65 | RemittanceBatchLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 66 | RemittanceBatchLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 67 | RemittanceBatchLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 68 | RemittanceBatchLockboxBatchName | LOCKBOX_BATCH_NAME | — | — |
| 69 | RemittanceBatchLockboxId | LOCKBOX_ID | — | — |
| 70 | RemittanceBatchMediaReference | MEDIA_REFERENCE | — | — |
| 71 | RemittanceBatchName | NAME | — | — |
| 72 | RemittanceBatchObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 73 | RemittanceBatchOldRemittanceBankBranchId | OLD_REMITTANCE_BANK_BRANCH_ID | — | — |
| 74 | RemittanceBatchOperationRequestId | OPERATION_REQUEST_ID | — | — |
| 75 | RemittanceBatchOrgId | ORG_ID | — | — |
| 76 | RemittanceBatchProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 77 | RemittanceBatchProgramId | PROGRAM_ID | — | — |
| 78 | RemittanceBatchProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 79 | RemittanceBatchPurgedChildrenFlag | PURGED_CHILDREN_FLAG | — | — |
| 80 | RemittanceBatchReceiptClassId | RECEIPT_CLASS_ID | — | — |
| 81 | RemittanceBatchReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 82 | RemittanceBatchRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 83 | RemittanceBatchRemitMethodCode | REMIT_METHOD_CODE | — | — |
| 84 | RemittanceBatchRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 85 | RemittanceBatchRemittanceBankBranchId | REMITTANCE_BANK_BRANCH_ID | — | — |
| 86 | RemittanceBatchRequestId | REQUEST_ID | — | — |
| 87 | RemittanceBatchSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 88 | RemittanceBatchStatus | STATUS | — | — |
| 89 | RemittanceBatchTransmissionId | TRANSMISSION_ID | — | — |
| 90 | RemittanceBatchTransmissionRequestId | TRANSMISSION_REQUEST_ID | — | — |
| 91 | RemittanceBatchType | TYPE | — | — |
| 92 | RemittanceBatchWithRecourseFlag | WITH_RECOURSE_FLAG | — | — |

### [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CashReceiptId | CASH_RECEIPT_ID | 🔑 | ✅ |
| 2 | ReceiptActualValueDate | ACTUAL_VALUE_DATE | — | ✅ |
| 3 | ReceiptAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | ✅ |
| 4 | ReceiptAmount | AMOUNT | — | ✅ |
| 5 | ReceiptAnticipatedClearingDate | ANTICIPATED_CLEARING_DATE | — | ✅ |
| 6 | ReceiptApplicationNotes | APPLICATION_NOTES | — | — |
| 7 | ReceiptApprovalCode | APPROVAL_CODE | — | — |
| 8 | ReceiptAutoapplyFlag | AUTOAPPLY_FLAG | — | — |
| 9 | ReceiptAutomatchRequestId | AUTOMATCH_REQUEST_ID | — | — |
| 10 | ReceiptAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 11 | ReceiptCcErrorCode | CC_ERROR_CODE | — | — |
| 12 | ReceiptCcErrorFlag | CC_ERROR_FLAG | — | — |
| 13 | ReceiptCcErrorText | CC_ERROR_TEXT | — | — |
| 14 | ReceiptCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 15 | ReceiptCollectorId | COLLECTOR_ID | — | — |
| 16 | ReceiptComments | COMMENTS | — | ✅ |
| 17 | ReceiptConfirmedFlag | CONFIRMED_FLAG | — | ✅ |
| 18 | ReceiptCreatedBy | CREATED_BY | — | ✅ |
| 19 | ReceiptCreationDate | CREATION_DATE | — | ✅ |
| 20 | ReceiptCurrencyCode | CURRENCY_CODE | — | — |
| 21 | ReceiptCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 22 | ReceiptCustomerBankBranchId | CUSTOMER_BANK_BRANCH_ID | — | — |
| 23 | ReceiptCustomerReceiptReference | CUSTOMER_RECEIPT_REFERENCE | — | ✅ |
| 24 | ReceiptCustomerSiteUseId | CUSTOMER_SITE_USE_ID | — | — |
| 25 | ReceiptDepositDate | DEPOSIT_DATE | — | ✅ |
| 26 | ReceiptDistributionSetId | DISTRIBUTION_SET_ID | — | — |
| 27 | ReceiptDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 28 | ReceiptDocSequenceValue | DOC_SEQUENCE_VALUE | — | ✅ |
| 29 | ReceiptExchangeDate | EXCHANGE_DATE | — | ✅ |
| 30 | ReceiptExchangeRate | EXCHANGE_RATE | — | ✅ |
| 31 | ReceiptExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 32 | ReceiptFactorDiscountAmount | FACTOR_DISCOUNT_AMOUNT | — | ✅ |
| 33 | ReceiptIssueDate | ISSUE_DATE | — | — |
| 34 | ReceiptIssuerBankBranchId | ISSUER_BANK_BRANCH_ID | — | — |
| 35 | ReceiptIssuerName | ISSUER_NAME | — | — |
| 36 | ReceiptLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 37 | ReceiptLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 38 | ReceiptLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 39 | ReceiptLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 40 | ReceiptLogicalGroupReference | LOGICAL_GROUP_REFERENCE | — | — |
| 41 | ReceiptMiscPaymentSource | MISC_PAYMENT_SOURCE | — | ✅ |
| 42 | ReceiptObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 43 | ReceiptOldCustomerBankAccountId | OLD_CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 44 | ReceiptOldCustomerBankBranchId | OLD_CUSTOMER_BANK_BRANCH_ID | — | — |
| 45 | ReceiptOldIssuerBankBranchId | OLD_ISSUER_BANK_BRANCH_ID | — | — |
| 46 | ReceiptOrgId | ORG_ID | — | — |
| 47 | ReceiptOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 48 | ReceiptPayFromCustomer | PAY_FROM_CUSTOMER | — | — |
| 49 | ReceiptPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 50 | ReceiptPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 51 | ReceiptPostmarkDate | POSTMARK_DATE | — | ✅ |
| 52 | ReceiptProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 53 | ReceiptProgramId | PROGRAM_ID | — | — |
| 54 | ReceiptProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 55 | ReceiptPromiseSource | PROMISE_SOURCE | — | — |
| 56 | ReceiptRecVersionNumber | REC_VERSION_NUMBER | — | — |
| 57 | ReceiptReceiptBatchId | RECEIPT_BATCH_ID | — | — |
| 58 | ReceiptReceiptDate | RECEIPT_DATE | — | ✅ |
| 59 | ReceiptReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 60 | ReceiptReceiptNumber | RECEIPT_NUMBER | — | ✅ |
| 61 | ReceiptReceivablesTrxId | RECEIVABLES_TRX_ID | — | — |
| 62 | ReceiptReconFlag | RECON_FLAG | — | — |
| 63 | ReceiptReferenceId | REFERENCE_ID | — | — |
| 64 | ReceiptReferenceType | REFERENCE_TYPE | — | ✅ |
| 65 | ReceiptRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 66 | ReceiptRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 67 | ReceiptRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 68 | ReceiptRequestId | REQUEST_ID | — | — |
| 69 | ReceiptResourceId | RESOURCE_ID | — | — |
| 70 | ReceiptReversalCategory | REVERSAL_CATEGORY | — | ✅ |
| 71 | ReceiptReversalComments | REVERSAL_COMMENTS | — | ✅ |
| 72 | ReceiptReversalDate | REVERSAL_DATE | — | ✅ |
| 73 | ReceiptReversalReasonCode | REVERSAL_REASON_CODE | — | ✅ |
| 74 | ReceiptSelectedForFactoringFlag | SELECTED_FOR_FACTORING_FLAG | — | — |
| 75 | ReceiptSelectedRemittanceBatchId | SELECTED_REMITTANCE_BATCH_ID | — | — |
| 76 | ReceiptSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 77 | ReceiptStatus | STATUS | — | — |
| 78 | ReceiptTaxRate | TAX_RATE | — | ✅ |
| 79 | ReceiptType | TYPE | — | ✅ |
| 80 | ReceiptUniqueReference | UNIQUE_REFERENCE | — | — |
| 81 | ReceiptUssglTransactionCode | USSGL_TRANSACTION_CODE | — | — |
| 82 | ReceiptUssglTransactionCodeContext | USSGL_TRANSACTION_CODE_CONTEXT | — | — |
| 83 | ReceiptVatTaxId | VAT_TAX_ID | — | — |

### [[ar_cash_receipt_history_all|AR_CASH_RECEIPT_HISTORY_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReceiptHistoryAccountCodeCombinationId | ACCOUNT_CODE_COMBINATION_ID | — | — |
| 2 | ReceiptHistoryAcctdAmount | ACCTD_AMOUNT | — | — |
| 3 | ReceiptHistoryAcctdFactorDiscountAmount | ACCTD_FACTOR_DISCOUNT_AMOUNT | — | — |
| 4 | ReceiptHistoryAmount | AMOUNT | — | — |
| 5 | ReceiptHistoryBankChargeAccountCcid | BANK_CHARGE_ACCOUNT_CCID | — | — |
| 6 | ReceiptHistoryBatchId | BATCH_ID | — | — |
| 7 | ReceiptHistoryCashReceiptHistoryId | CASH_RECEIPT_HISTORY_ID | — | — |
| 8 | ReceiptHistoryCashReceiptId | CASH_RECEIPT_ID | — | — |
| 9 | ReceiptHistoryCreatedBy | CREATED_BY | — | — |
| 10 | ReceiptHistoryCreatedFrom | CREATED_FROM | — | — |
| 11 | ReceiptHistoryCreationDate | CREATION_DATE | — | — |
| 12 | ReceiptHistoryCurrentRecordFlag | CURRENT_RECORD_FLAG | — | — |
| 13 | ReceiptHistoryEventId | EVENT_ID | — | — |
| 14 | ReceiptHistoryExchangeDate | EXCHANGE_DATE | — | — |
| 15 | ReceiptHistoryExchangeRate | EXCHANGE_RATE | — | — |
| 16 | ReceiptHistoryExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 17 | ReceiptHistoryFactorDiscountAmount | FACTOR_DISCOUNT_AMOUNT | — | — |
| 18 | ReceiptHistoryFactorFlag | FACTOR_FLAG | — | — |
| 19 | ReceiptHistoryFirstPostedRecordFlag | FIRST_POSTED_RECORD_FLAG | — | — |
| 20 | ReceiptHistoryGlDate | GL_DATE | — | — |
| 21 | ReceiptHistoryGlPostedDate | GL_POSTED_DATE | — | — |
| 22 | ReceiptHistoryNoteStatus | NOTE_STATUS | — | — |
| 23 | ReceiptHistoryOrgId | ORG_ID | — | — |
| 24 | ReceiptHistoryPostableFlag | POSTABLE_FLAG | — | — |
| 25 | ReceiptHistoryPostingControlId | POSTING_CONTROL_ID | — | — |
| 26 | ReceiptHistoryProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 27 | ReceiptHistoryProgramId | PROGRAM_ID | — | — |
| 28 | ReceiptHistoryProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 29 | ReceiptHistoryPrvStatCashReceiptHistId | PRV_STAT_CASH_RECEIPT_HIST_ID | — | — |
| 30 | ReceiptHistoryRequestId | REQUEST_ID | — | — |
| 31 | ReceiptHistoryReversalCashReceiptHistId | REVERSAL_CASH_RECEIPT_HIST_ID | — | — |
| 32 | ReceiptHistoryReversalCreatedFrom | REVERSAL_CREATED_FROM | — | — |
| 33 | ReceiptHistoryReversalGlDate | REVERSAL_GL_DATE | — | — |
| 34 | ReceiptHistoryReversalGlPostedDate | REVERSAL_GL_POSTED_DATE | — | — |
| 35 | ReceiptHistoryReversalPostingControlId | REVERSAL_POSTING_CONTROL_ID | — | — |
| 36 | ReceiptHistoryStatus | STATUS | — | — |
| 37 | ReceiptHistoryTrxDate | TRX_DATE | — | — |

### [[ar_collectors|AR_COLLECTORS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CollectorsAlias | ALIAS | — | — |
| 2 | CollectorsCollectorId | COLLECTOR_ID | — | — |
| 3 | CollectorsDescription | DESCRIPTION | — | — |
| 4 | CollectorsEmployeeId | EMPLOYEE_ID | — | — |
| 5 | CollectorsInactiveDate | INACTIVE_DATE | — | — |
| 6 | CollectorsName | NAME | — | ✅ |
| 7 | CollectorsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | CollectorsResourceId | RESOURCE_ID | — | — |
| 9 | CollectorsResourceType | RESOURCE_TYPE | — | — |
| 10 | CollectorsSetId | SET_ID | — | — |
| 11 | CollectorsStatus | STATUS | — | — |
| 12 | CollectorsTelephoneNumber | TELEPHONE_NUMBER | — | — |

### [[ar_distribution_sets_all|AR_DISTRIBUTION_SETS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistributionSetCreatedBy | CREATED_BY | — | — |
| 2 | DistributionSetCreationDate | CREATION_DATE | — | — |
| 3 | DistributionSetDescription | DESCRIPTION | — | — |
| 4 | DistributionSetDistributionSetId | DISTRIBUTION_SET_ID | — | — |
| 5 | DistributionSetDistributionSetName | DISTRIBUTION_SET_NAME | — | ✅ |
| 6 | DistributionSetLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | DistributionSetLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | DistributionSetLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | DistributionSetObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | DistributionSetOrgId | ORG_ID | — | — |
| 11 | DistributionSetStatus | STATUS | — | — |
| 12 | DistributionSetTotalPercentDistribution | TOTAL_PERCENT_DISTRIBUTION | — | — |

### [[ar_payment_schedules_all|AR_PAYMENT_SCHEDULES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentScheduleAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | — |
| 2 | PaymentScheduleActiveClaimFlag | ACTIVE_CLAIM_FLAG | — | — |
| 3 | PaymentScheduleActualDateClosed | ACTUAL_DATE_CLOSED | — | — |
| 4 | PaymentScheduleAdjustmentAmountLast | ADJUSTMENT_AMOUNT_LAST | — | — |
| 5 | PaymentScheduleAdjustmentDateLast | ADJUSTMENT_DATE_LAST | — | — |
| 6 | PaymentScheduleAdjustmentGlDateLast | ADJUSTMENT_GL_DATE_LAST | — | — |
| 7 | PaymentScheduleAdjustmentIdLast | ADJUSTMENT_ID_LAST | — | — |
| 8 | PaymentScheduleAmountAdjusted | AMOUNT_ADJUSTED | — | — |
| 9 | PaymentScheduleAmountAdjustedPending | AMOUNT_ADJUSTED_PENDING | — | — |
| 10 | PaymentScheduleAmountApplied | AMOUNT_APPLIED | — | ✅ |
| 11 | PaymentScheduleAmountCredited | AMOUNT_CREDITED | — | — |
| 12 | PaymentScheduleAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | ✅ |
| 13 | PaymentScheduleAmountDueRemaining | AMOUNT_DUE_REMAINING | — | ✅ |
| 14 | PaymentScheduleAmountInDispute | AMOUNT_IN_DISPUTE | — | — |
| 15 | PaymentScheduleAmountLineItemsOriginal | AMOUNT_LINE_ITEMS_ORIGINAL | — | — |
| 16 | PaymentScheduleAmountLineItemsRemaining | AMOUNT_LINE_ITEMS_REMAINING | — | — |
| 17 | PaymentScheduleAmountOnAccount | AMOUNT_ON_ACCOUNT | — | ✅ |
| 18 | PaymentScheduleAmountOtherAccount | AMOUNT_OTHER_ACCOUNT | — | — |
| 19 | PaymentScheduleAssociatedCashReceiptId | ASSOCIATED_CASH_RECEIPT_ID | — | — |
| 20 | PaymentScheduleBrAmountAssigned | BR_AMOUNT_ASSIGNED | — | — |
| 21 | PaymentScheduleCallDateLast | CALL_DATE_LAST | — | — |
| 22 | PaymentScheduleCashAppliedAmountLast | CASH_APPLIED_AMOUNT_LAST | — | — |
| 23 | PaymentScheduleCashAppliedDateLast | CASH_APPLIED_DATE_LAST | — | — |
| 24 | PaymentScheduleCashAppliedIdLast | CASH_APPLIED_ID_LAST | — | — |
| 25 | PaymentScheduleCashAppliedStatusLast | CASH_APPLIED_STATUS_LAST | — | — |
| 26 | PaymentScheduleCashGlDateLast | CASH_GL_DATE_LAST | — | — |
| 27 | PaymentScheduleCashReceiptAmountLast | CASH_RECEIPT_AMOUNT_LAST | — | — |
| 28 | PaymentScheduleCashReceiptDateLast | CASH_RECEIPT_DATE_LAST | — | — |
| 29 | PaymentScheduleCashReceiptId | CASH_RECEIPT_ID | — | — |
| 30 | PaymentScheduleCashReceiptIdLast | CASH_RECEIPT_ID_LAST | — | — |
| 31 | PaymentScheduleCashReceiptStatusLast | CASH_RECEIPT_STATUS_LAST | — | — |
| 32 | PaymentScheduleCollectorLast | COLLECTOR_LAST | — | — |
| 33 | PaymentScheduleConsInvId | CONS_INV_ID | — | — |
| 34 | PaymentScheduleConsInvIdRev | CONS_INV_ID_REV | — | — |
| 35 | PaymentScheduleCreatedBy | CREATED_BY | — | — |
| 36 | PaymentScheduleCreationDate | CREATION_DATE | — | — |
| 37 | PaymentScheduleCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 38 | PaymentScheduleCustomerId | CUSTOMER_ID | — | — |
| 39 | PaymentScheduleCustomerSiteUseId | CUSTOMER_SITE_USE_ID | — | — |
| 40 | PaymentScheduleCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 41 | PaymentScheduleDiscountDate | DISCOUNT_DATE | — | — |
| 42 | PaymentScheduleDiscountOriginal | DISCOUNT_ORIGINAL | — | — |
| 43 | PaymentScheduleDiscountRemaining | DISCOUNT_REMAINING | — | — |
| 44 | PaymentScheduleDiscountTakenEarned | DISCOUNT_TAKEN_EARNED | — | — |
| 45 | PaymentScheduleDiscountTakenUnearned | DISCOUNT_TAKEN_UNEARNED | — | — |
| 46 | PaymentScheduleDisputeDate | DISPUTE_DATE | — | — |
| 47 | PaymentScheduleDueDate | DUE_DATE | — | ✅ |
| 48 | PaymentScheduleDunningLevelOverrideDate | DUNNING_LEVEL_OVERRIDE_DATE | — | — |
| 49 | PaymentScheduleExchangeDate | EXCHANGE_DATE | — | — |
| 50 | PaymentScheduleExchangeRate | EXCHANGE_RATE | — | — |
| 51 | PaymentScheduleExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 52 | PaymentScheduleExcludeFromConsBillFlag | EXCLUDE_FROM_CONS_BILL_FLAG | — | — |
| 53 | PaymentScheduleExcludeFromDunningFlag | EXCLUDE_FROM_DUNNING_FLAG | — | — |
| 54 | PaymentScheduleFollowUpCodeLast | FOLLOW_UP_CODE_LAST | — | — |
| 55 | PaymentScheduleFollowUpDateLast | FOLLOW_UP_DATE_LAST | — | — |
| 56 | PaymentScheduleFreightOriginal | FREIGHT_ORIGINAL | — | — |
| 57 | PaymentScheduleFreightRemaining | FREIGHT_REMAINING | — | — |
| 58 | PaymentScheduleGlDate | GL_DATE | — | — |
| 59 | PaymentScheduleGlDateClosed | GL_DATE_CLOSED | — | — |
| 60 | PaymentScheduleInCollection | IN_COLLECTION | — | — |
| 61 | PaymentScheduleInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 62 | PaymentScheduleLastChargeDate | LAST_CHARGE_DATE | — | — |
| 63 | PaymentScheduleLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 64 | PaymentScheduleLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 65 | PaymentScheduleLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 66 | PaymentScheduleNumberOfDueDates | NUMBER_OF_DUE_DATES | — | — |
| 67 | PaymentScheduleObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 68 | PaymentScheduleOrgId | ORG_ID | — | — |
| 69 | PaymentSchedulePaymentApproval | PAYMENT_APPROVAL | — | — |
| 70 | PaymentSchedulePaymentScheduleClass | CLASS | — | — |
| 71 | PaymentScheduleProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 72 | PaymentScheduleProgramId | PROGRAM_ID | — | — |
| 73 | PaymentScheduleProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 74 | PaymentSchedulePromiseAmountLast | PROMISE_AMOUNT_LAST | — | — |
| 75 | PaymentSchedulePromiseDateLast | PROMISE_DATE_LAST | — | — |
| 76 | PaymentScheduleReceiptConfirmedFlag | RECEIPT_CONFIRMED_FLAG | — | — |
| 77 | PaymentScheduleReceivablesChargesCharged | RECEIVABLES_CHARGES_CHARGED | — | — |
| 78 | PaymentScheduleReceivablesChargesRemaining | RECEIVABLES_CHARGES_REMAINING | — | — |
| 79 | PaymentScheduleRequestId | REQUEST_ID | — | — |
| 80 | PaymentScheduleReservedType | RESERVED_TYPE | — | — |
| 81 | PaymentScheduleReservedValue | RESERVED_VALUE | — | — |
| 82 | PaymentScheduleReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 83 | PaymentScheduleSecondLastChargeDate | SECOND_LAST_CHARGE_DATE | — | — |
| 84 | PaymentScheduleSelectedForReceiptBatchId | SELECTED_FOR_RECEIPT_BATCH_ID | — | — |
| 85 | PaymentScheduleStagedDunningLevel | STAGED_DUNNING_LEVEL | — | — |
| 86 | PaymentScheduleStatus | STATUS | — | — |
| 87 | PaymentScheduleTaxOriginal | TAX_ORIGINAL | — | — |
| 88 | PaymentScheduleTaxRemaining | TAX_REMAINING | — | — |
| 89 | PaymentScheduleTermId | TERM_ID | — | — |
| 90 | PaymentScheduleTermsSequenceNumber | TERMS_SEQUENCE_NUMBER | — | — |
| 91 | PaymentScheduleTrxDate | TRX_DATE | — | — |
| 92 | PaymentScheduleTrxNumber | TRX_NUMBER | — | — |
| 93 | PaymentSchedulesPaymentScheduleId | PAYMENT_SCHEDULE_ID | — | — |

### [[ar_receivables_trx_all|AR_RECEIVABLES_TRX_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RecActivityAccountingAffectFlag | ACCOUNTING_AFFECT_FLAG | — | — |
| 2 | RecActivityAssetTaxCode | ASSET_TAX_CODE | — | — |
| 3 | RecActivityCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 4 | RecActivityDefaultAcctgDistributionSet | DEFAULT_ACCTG_DISTRIBUTION_SET | — | — |
| 5 | RecActivityDescription | DESCRIPTION | — | — |
| 6 | RecActivityEndDateActive | END_DATE_ACTIVE | — | — |
| 7 | RecActivityGlAccountSource | GL_ACCOUNT_SOURCE | — | — |
| 8 | RecActivityInactiveDate | INACTIVE_DATE | — | — |
| 9 | RecActivityLiabilityTaxCode | LIABILITY_TAX_CODE | — | — |
| 10 | RecActivityName | NAME | — | ✅ |
| 11 | RecActivityObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | RecActivityOrgId | ORG_ID | — | — |
| 13 | RecActivityReceivablesTrxId | RECEIVABLES_TRX_ID | — | — |
| 14 | RecActivityRiskEliminationDays | RISK_ELIMINATION_DAYS | — | — |
| 15 | RecActivitySetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 16 | RecActivityStartDateActive | START_DATE_ACTIVE | — | — |
| 17 | RecActivityStatus | STATUS | — | — |
| 18 | RecActivityTaxCodeSource | TAX_CODE_SOURCE | — | — |
| 19 | RecActivityTaxRecoverableFlag | TAX_RECOVERABLE_FLAG | — | — |
| 20 | RecActivityType | TYPE | — | — |

### [[ce_bank_acct_uses_all|CE_BANK_ACCT_USES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankAcctUseApUseEnableFlag | AP_USE_ENABLE_FLAG | — | — |
| 2 | BankAcctUseArUseEnableFlag | AR_USE_ENABLE_FLAG | — | — |
| 3 | BankAcctUseAuthorizedFlag | AUTHORIZED_FLAG | — | — |
| 4 | BankAcctUseBankAccountId | BANK_ACCOUNT_ID | — | — |
| 5 | BankAcctUseBankAcctUseId | BANK_ACCT_USE_ID | — | — |
| 6 | BankAcctUseCreatedBy | CREATED_BY | — | — |
| 7 | BankAcctUseCreationDate | CREATION_DATE | — | — |
| 8 | BankAcctUseDefaultAccountFlag | DEFAULT_ACCOUNT_FLAG | — | — |
| 9 | BankAcctUseEftScriptName | EFT_SCRIPT_NAME | — | — |
| 10 | BankAcctUseEndDate | END_DATE | — | — |
| 11 | BankAcctUseFundingLimitCode | FUNDING_LIMIT_CODE | — | — |
| 12 | BankAcctUseInvestmentLimitCode | INVESTMENT_LIMIT_CODE | — | — |
| 13 | BankAcctUseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | BankAcctUseLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | BankAcctUseLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | BankAcctUseLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 17 | BankAcctUseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | BankAcctUseOrgId | ORG_ID | — | — |
| 19 | BankAcctUseOrgPartyId | ORG_PARTY_ID | — | — |
| 20 | BankAcctUsePayUseEnableFlag | PAY_USE_ENABLE_FLAG | — | — |
| 21 | BankAcctUsePortfolioCode | PORTFOLIO_CODE | — | — |
| 22 | BankAcctUsePricingModel | PRICING_MODEL | — | — |
| 23 | BankAcctUsePrimaryFlag | PRIMARY_FLAG | — | — |
| 24 | BankAcctUseProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 25 | BankAcctUseProgramId | PROGRAM_ID | — | — |
| 26 | BankAcctUseProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 27 | BankAcctUseRequestId | REQUEST_ID | — | — |
| 28 | BankAcctUseXtrBankAccountReference | XTR_BANK_ACCOUNT_REFERENCE | — | — |
| 29 | BankAcctUseXtrDefaultSettlementFlag | XTR_DEFAULT_SETTLEMENT_FLAG | — | — |
| 30 | BankAcctUseXtrUseEnableFlag | XTR_USE_ENABLE_FLAG | — | — |

### [[ce_bank_branches_v|CE_BANK_BRANCHES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustomerBankBranchAddressLine1 | ADDRESS_LINE1 | — | — |
| 2 | CustomerBankBranchAddressLine2 | ADDRESS_LINE2 | — | — |
| 3 | CustomerBankBranchAddressLine3 | ADDRESS_LINE3 | — | — |
| 4 | CustomerBankBranchAddressLine4 | ADDRESS_LINE4 | — | — |
| 5 | CustomerBankBranchBankBranchName | BANK_BRANCH_NAME | — | ✅ |
| 6 | CustomerBankBranchBankBranchNameAlt | BANK_BRANCH_NAME_ALT | — | — |
| 7 | CustomerBankBranchBankBranchType | BANK_BRANCH_TYPE | — | — |
| 8 | CustomerBankBranchBankCode | BANK_CODE | — | — |
| 9 | CustomerBankBranchBankHomeCountry | BANK_HOME_COUNTRY | — | — |
| 10 | CustomerBankBranchBankInstitutionType | BANK_INSTITUTION_TYPE | — | — |
| 11 | CustomerBankBranchBankName | BANK_NAME | — | — |
| 12 | CustomerBankBranchBankNameAlt | BANK_NAME_ALT | — | — |
| 13 | CustomerBankBranchBankNumber | BANK_NUMBER | — | — |
| 14 | CustomerBankBranchBankPartyId | BANK_PARTY_ID | — | — |
| 15 | CustomerBankBranchBranchNumber | BRANCH_NUMBER | — | — |
| 16 | CustomerBankBranchBranchPartyId | BRANCH_PARTY_ID | — | — |
| 17 | CustomerBankBranchCity | CITY | — | — |
| 18 | CustomerBankBranchCountry | COUNTRY | — | — |
| 19 | CustomerBankBranchCountryName | COUNTRY_NAME | — | — |
| 20 | CustomerBankBranchDescription | DESCRIPTION | — | — |
| 21 | CustomerBankBranchEdiIdNumber | EDI_ID_NUMBER | — | — |
| 22 | CustomerBankBranchEdiLocation | EDI_LOCATION | — | — |
| 23 | CustomerBankBranchEftSwiftCode | EFT_SWIFT_CODE | — | — |
| 24 | CustomerBankBranchEftUserNumber | EFT_USER_NUMBER | — | — |
| 25 | CustomerBankBranchEndDate | END_DATE | — | — |
| 26 | CustomerBankBranchPkId | PK_ID | — | — |
| 27 | CustomerBankBranchProvince | PROVINCE | — | — |
| 28 | CustomerBankBranchRfc | RFC | — | — |
| 29 | CustomerBankBranchRowId | ROW_ID | — | — |
| 30 | CustomerBankBranchShortBankName | SHORT_BANK_NAME | — | — |
| 31 | CustomerBankBranchStartDate | START_DATE | — | — |
| 32 | CustomerBankBranchState | STATE | — | — |
| 33 | CustomerBankBranchZip | ZIP | — | — |
| 34 | IssuerBankBranchAddressLine1 | ADDRESS_LINE1 | — | — |
| 35 | IssuerBankBranchAddressLine2 | ADDRESS_LINE2 | — | — |
| 36 | IssuerBankBranchAddressLine3 | ADDRESS_LINE3 | — | — |
| 37 | IssuerBankBranchAddressLine4 | ADDRESS_LINE4 | — | — |
| 38 | IssuerBankBranchBankBranchName | BANK_BRANCH_NAME | — | — |
| 39 | IssuerBankBranchBankBranchNameAlt | BANK_BRANCH_NAME_ALT | — | — |
| 40 | IssuerBankBranchBankBranchType | BANK_BRANCH_TYPE | — | — |
| 41 | IssuerBankBranchBankCode | BANK_CODE | — | — |
| 42 | IssuerBankBranchBankHomeCountry | BANK_HOME_COUNTRY | — | — |
| 43 | IssuerBankBranchBankInstitutionType | BANK_INSTITUTION_TYPE | — | — |
| 44 | IssuerBankBranchBankName | BANK_NAME | — | — |
| 45 | IssuerBankBranchBankNameAlt | BANK_NAME_ALT | — | — |
| 46 | IssuerBankBranchBankNumber | BANK_NUMBER | — | — |
| 47 | IssuerBankBranchBankPartyId | BANK_PARTY_ID | — | — |
| 48 | IssuerBankBranchBranchNumber | BRANCH_NUMBER | — | — |
| 49 | IssuerBankBranchBranchPartyId | BRANCH_PARTY_ID | — | — |
| 50 | IssuerBankBranchCity | CITY | — | — |
| 51 | IssuerBankBranchCountry | COUNTRY | — | — |
| 52 | IssuerBankBranchCountryName | COUNTRY_NAME | — | — |
| 53 | IssuerBankBranchDescription | DESCRIPTION | — | — |
| 54 | IssuerBankBranchEdiIdNumber | EDI_ID_NUMBER | — | — |
| 55 | IssuerBankBranchEdiLocation | EDI_LOCATION | — | — |
| 56 | IssuerBankBranchEftSwiftCode | EFT_SWIFT_CODE | — | — |
| 57 | IssuerBankBranchEftUserNumber | EFT_USER_NUMBER | — | — |
| 58 | IssuerBankBranchEndDate | END_DATE | — | — |
| 59 | IssuerBankBranchPkId | PK_ID | — | — |
| 60 | IssuerBankBranchProvince | PROVINCE | — | — |
| 61 | IssuerBankBranchRfc | RFC | — | — |
| 62 | IssuerBankBranchRowId | ROW_ID | — | — |
| 63 | IssuerBankBranchShortBankName | SHORT_BANK_NAME | — | — |
| 64 | IssuerBankBranchStartDate | START_DATE | — | — |
| 65 | IssuerBankBranchState | STATE | — | — |
| 66 | IssuerBankBranchZip | ZIP | — | — |
| 67 | OldCustomerBankBranchAddressLine1 | ADDRESS_LINE1 | — | — |
| 68 | OldCustomerBankBranchAddressLine2 | ADDRESS_LINE2 | — | — |
| 69 | OldCustomerBankBranchAddressLine3 | ADDRESS_LINE3 | — | — |
| 70 | OldCustomerBankBranchAddressLine4 | ADDRESS_LINE4 | — | — |
| 71 | OldCustomerBankBranchBankBranchName | BANK_BRANCH_NAME | — | — |
| 72 | OldCustomerBankBranchBankBranchNameAlt | BANK_BRANCH_NAME_ALT | — | — |
| 73 | OldCustomerBankBranchBankBranchType | BANK_BRANCH_TYPE | — | — |
| 74 | OldCustomerBankBranchBankCode | BANK_CODE | — | — |
| 75 | OldCustomerBankBranchBankHomeCountry | BANK_HOME_COUNTRY | — | — |
| 76 | OldCustomerBankBranchBankInstitutionType | BANK_INSTITUTION_TYPE | — | — |
| 77 | OldCustomerBankBranchBankName | BANK_NAME | — | — |
| 78 | OldCustomerBankBranchBankNameAlt | BANK_NAME_ALT | — | — |
| 79 | OldCustomerBankBranchBankNumber | BANK_NUMBER | — | — |
| 80 | OldCustomerBankBranchBankPartyId | BANK_PARTY_ID | — | — |
| 81 | OldCustomerBankBranchBranchNumber | BRANCH_NUMBER | — | — |
| 82 | OldCustomerBankBranchBranchPartyId | BRANCH_PARTY_ID | — | — |
| 83 | OldCustomerBankBranchCity | CITY | — | — |
| 84 | OldCustomerBankBranchCountry | COUNTRY | — | — |
| 85 | OldCustomerBankBranchCountryName | COUNTRY_NAME | — | — |
| 86 | OldCustomerBankBranchDescription | DESCRIPTION | — | — |
| 87 | OldCustomerBankBranchEdiIdNumber | EDI_ID_NUMBER | — | — |
| 88 | OldCustomerBankBranchEdiLocation | EDI_LOCATION | — | — |
| 89 | OldCustomerBankBranchEftSwiftCode | EFT_SWIFT_CODE | — | — |
| 90 | OldCustomerBankBranchEftUserNumber | EFT_USER_NUMBER | — | — |
| 91 | OldCustomerBankBranchEndDate | END_DATE | — | — |
| 92 | OldCustomerBankBranchPkId | PK_ID | — | — |
| 93 | OldCustomerBankBranchProvince | PROVINCE | — | — |
| 94 | OldCustomerBankBranchRfc | RFC | — | — |
| 95 | OldCustomerBankBranchRowId | ROW_ID | — | — |
| 96 | OldCustomerBankBranchShortBankName | SHORT_BANK_NAME | — | — |
| 97 | OldCustomerBankBranchStartDate | START_DATE | — | — |
| 98 | OldCustomerBankBranchState | STATE | — | — |
| 99 | OldCustomerBankBranchZip | ZIP | — | — |
| 100 | OldIssuerBankBranchAddressLine1 | ADDRESS_LINE1 | — | — |
| 101 | OldIssuerBankBranchAddressLine2 | ADDRESS_LINE2 | — | — |
| 102 | OldIssuerBankBranchAddressLine3 | ADDRESS_LINE3 | — | — |
| 103 | OldIssuerBankBranchAddressLine4 | ADDRESS_LINE4 | — | — |
| 104 | OldIssuerBankBranchBankBranchName | BANK_BRANCH_NAME | — | — |
| 105 | OldIssuerBankBranchBankBranchNameAlt | BANK_BRANCH_NAME_ALT | — | — |
| 106 | OldIssuerBankBranchBankBranchType | BANK_BRANCH_TYPE | — | — |
| 107 | OldIssuerBankBranchBankCode | BANK_CODE | — | — |
| 108 | OldIssuerBankBranchBankHomeCountry | BANK_HOME_COUNTRY | — | — |
| 109 | OldIssuerBankBranchBankInstitutionType | BANK_INSTITUTION_TYPE | — | — |
| 110 | OldIssuerBankBranchBankName | BANK_NAME | — | — |
| 111 | OldIssuerBankBranchBankNameAlt | BANK_NAME_ALT | — | — |
| 112 | OldIssuerBankBranchBankNumber | BANK_NUMBER | — | — |
| 113 | OldIssuerBankBranchBankPartyId | BANK_PARTY_ID | — | — |
| 114 | OldIssuerBankBranchBranchNumber | BRANCH_NUMBER | — | — |
| 115 | OldIssuerBankBranchBranchPartyId | BRANCH_PARTY_ID | — | — |
| 116 | OldIssuerBankBranchCity | CITY | — | — |
| 117 | OldIssuerBankBranchCountry | COUNTRY | — | — |
| 118 | OldIssuerBankBranchCountryName | COUNTRY_NAME | — | — |
| 119 | OldIssuerBankBranchDescription | DESCRIPTION | — | — |
| 120 | OldIssuerBankBranchEdiIdNumber | EDI_ID_NUMBER | — | — |
| 121 | OldIssuerBankBranchEdiLocation | EDI_LOCATION | — | — |
| 122 | OldIssuerBankBranchEftSwiftCode | EFT_SWIFT_CODE | — | — |
| 123 | OldIssuerBankBranchEftUserNumber | EFT_USER_NUMBER | — | — |
| 124 | OldIssuerBankBranchEndDate | END_DATE | — | — |
| 125 | OldIssuerBankBranchPkId | PK_ID | — | — |
| 126 | OldIssuerBankBranchProvince | PROVINCE | — | — |
| 127 | OldIssuerBankBranchRfc | RFC | — | — |
| 128 | OldIssuerBankBranchRowId | ROW_ID | — | — |
| 129 | OldIssuerBankBranchShortBankName | SHORT_BANK_NAME | — | — |
| 130 | OldIssuerBankBranchStartDate | START_DATE | — | — |
| 131 | OldIssuerBankBranchState | STATE | — | — |
| 132 | OldIssuerBankBranchZip | ZIP | — | — |

### [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocSeqAuditTableName | AUDIT_TABLE_NAME | — | — |
| 2 | DocSeqDbSequenceName | DB_SEQUENCE_NAME | — | — |
| 3 | DocSeqDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 4 | DocSeqName | NAME | — | ✅ |
| 5 | DocSeqTableName | TABLE_NAME | — | — |

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitBusinessUnitId | BU_ID | — | — |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DailyConversionTypeConversionType | CONVERSION_TYPE | — | — |
| 2 | DailyConversionTypeDescription | DESCRIPTION | — | — |
| 3 | DailyConversionTypeEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 4 | DailyConversionTypeEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 5 | DailyConversionTypeFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 6 | DailyConversionTypeFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 7 | DailyConversionTypeFemScenario | FEM_SCENARIO | — | — |
| 8 | DailyConversionTypeFemTimeframe | FEM_TIMEFRAME | — | — |
| 9 | DailyConversionTypePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 10 | DailyConversionTypeSecurityFlag | SECURITY_FLAG | — | — |
| 11 | DailyConversionTypeUserConversionType | USER_CONVERSION_TYPE | — | ✅ |
| 12 | DailyConversionTypeUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |

### [[hz_cust_accounts|HZ_CUST_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustAcctAccountEstablishedDate | ACCOUNT_ESTABLISHED_DATE | — | — |
| 2 | CustAcctAccountName | ACCOUNT_NAME | — | ✅ |
| 3 | CustAcctAccountNumber | ACCOUNT_NUMBER | — | ✅ |
| 4 | CustAcctArrivalsetsIncludeLinesFlag | ARRIVALSETS_INCLUDE_LINES_FLAG | — | — |
| 5 | CustAcctAutopayFlag | AUTOPAY_FLAG | — | — |
| 6 | CustAcctComments | COMMENTS | — | — |
| 7 | CustAcctCoterminateDayMonth | COTERMINATE_DAY_MONTH | — | — |
| 8 | CustAcctCreatedBy | CREATED_BY | — | — |
| 9 | CustAcctCreatedByModule | CREATED_BY_MODULE | — | — |
| 10 | CustAcctCreationDate | CREATION_DATE | — | — |
| 11 | CustAcctCustAccountId | CUST_ACCOUNT_ID | — | — |
| 12 | CustAcctCustomerClassCode | CUSTOMER_CLASS_CODE | — | — |
| 13 | CustAcctCustomerType | CUSTOMER_TYPE | — | — |
| 14 | CustAcctDateTypePreference | DATE_TYPE_PREFERENCE | — | — |
| 15 | CustAcctDepositRefundMethod | DEPOSIT_REFUND_METHOD | — | — |
| 16 | CustAcctHeldBillExpirationDate | HELD_BILL_EXPIRATION_DATE | — | — |
| 17 | CustAcctHoldBillFlag | HOLD_BILL_FLAG | — | — |
| 18 | CustAcctLastBatchId | LAST_BATCH_ID | — | — |
| 19 | CustAcctLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | CustAcctLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | CustAcctLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 22 | CustAcctNpaNumber | NPA_NUMBER | — | — |
| 23 | CustAcctOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 24 | CustAcctPartyId | PARTY_ID | — | — |
| 25 | CustAcctSellingPartyId | SELLING_PARTY_ID | — | — |
| 26 | CustAcctSourceCode | SOURCE_CODE | — | — |
| 27 | CustAcctStatus | STATUS | — | — |
| 28 | CustAcctStatusUpdateDate | STATUS_UPDATE_DATE | — | — |
| 29 | CustAcctTaxCode | TAX_CODE | — | — |
| 30 | CustAcctTaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | — |
| 31 | CustAcctTaxRoundingRule | TAX_ROUNDING_RULE | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyId | PARTY_ID | — | — |
| 2 | PartyPartyId | PARTY_ID | — | — |
| 3 | PartyPartyName | PARTY_NAME | — | ✅ |
| 4 | PartyPartyNumber | PARTY_NUMBER | — | — |
| 5 | PernNameDisplayName | PARTY_NAME | — | — |

### [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExtBankAccountAccountClassification | ACCOUNT_CLASSIFICATION | — | — |
| 2 | ExtBankAccountAccountSuffix | ACCOUNT_SUFFIX | — | — |
| 3 | ExtBankAccountAgencyLocationCode | AGENCY_LOCATION_CODE | — | — |
| 4 | ExtBankAccountBaMaskSetting | BA_MASK_SETTING | — | — |
| 5 | ExtBankAccountBaNumElecSecSegmentId | BA_NUM_ELEC_SEC_SEGMENT_ID | — | — |
| 6 | ExtBankAccountBaNumSecSegmentId | BA_NUM_SEC_SEGMENT_ID | — | — |
| 7 | ExtBankAccountBaUnmaskLength | BA_UNMASK_LENGTH | — | — |
| 8 | ExtBankAccountBankAccountName | BANK_ACCOUNT_NAME | — | ✅ |
| 9 | ExtBankAccountBankAccountNameAlt | BANK_ACCOUNT_NAME_ALT | — | — |
| 10 | ExtBankAccountBankAccountNum | BANK_ACCOUNT_NUM | — | ✅ |
| 11 | ExtBankAccountBankAccountNumElectronic | BANK_ACCOUNT_NUM_ELECTRONIC | — | — |
| 12 | ExtBankAccountBankAccountNumHash1 | BANK_ACCOUNT_NUM_HASH1 | — | — |
| 13 | ExtBankAccountBankAccountNumHash2 | BANK_ACCOUNT_NUM_HASH2 | — | — |
| 14 | ExtBankAccountBankAccountType | BANK_ACCOUNT_TYPE | — | — |
| 15 | ExtBankAccountBankId | BANK_ID | — | — |
| 16 | ExtBankAccountBranchId | BRANCH_ID | — | — |
| 17 | ExtBankAccountCheckDigits | CHECK_DIGITS | — | — |
| 18 | ExtBankAccountCountryCode | COUNTRY_CODE | — | — |
| 19 | ExtBankAccountCreatedBy | CREATED_BY | — | — |
| 20 | ExtBankAccountCreationDate | CREATION_DATE | — | — |
| 21 | ExtBankAccountCurrencyCode | CURRENCY_CODE | — | — |
| 22 | ExtBankAccountDescription | DESCRIPTION | — | — |
| 23 | ExtBankAccountEncrypted | ENCRYPTED | — | — |
| 24 | ExtBankAccountEndDate | END_DATE | — | — |
| 25 | ExtBankAccountExchangeRate | EXCHANGE_RATE | — | — |
| 26 | ExtBankAccountExchangeRateAgreementNum | EXCHANGE_RATE_AGREEMENT_NUM | — | — |
| 27 | ExtBankAccountExchangeRateAgreementType | EXCHANGE_RATE_AGREEMENT_TYPE | — | — |
| 28 | ExtBankAccountExtBankAccountId | EXT_BANK_ACCOUNT_ID | — | — |
| 29 | ExtBankAccountForeignPaymentUseFlag | FOREIGN_PAYMENT_USE_FLAG | — | — |
| 30 | ExtBankAccountHedgingContractReference | HEDGING_CONTRACT_REFERENCE | — | — |
| 31 | ExtBankAccountIban | IBAN | — | — |
| 32 | ExtBankAccountIbanHash1 | IBAN_HASH1 | — | — |
| 33 | ExtBankAccountIbanHash2 | IBAN_HASH2 | — | — |
| 34 | ExtBankAccountIbanSecSegmentId | IBAN_SEC_SEGMENT_ID | — | — |
| 35 | ExtBankAccountLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 36 | ExtBankAccountLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 37 | ExtBankAccountLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 38 | ExtBankAccountMaskedBankAccountNum | MASKED_BANK_ACCOUNT_NUM | — | — |
| 39 | ExtBankAccountMaskedIban | MASKED_IBAN | — | — |
| 40 | ExtBankAccountObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 41 | ExtBankAccountPaymentFactorFlag | PAYMENT_FACTOR_FLAG | — | — |
| 42 | ExtBankAccountProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 43 | ExtBankAccountProgramId | PROGRAM_ID | — | — |
| 44 | ExtBankAccountProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 45 | ExtBankAccountRequestId | REQUEST_ID | — | — |
| 46 | ExtBankAccountSaltVersion | SALT_VERSION | — | — |
| 47 | ExtBankAccountSecondaryAccountReference | SECONDARY_ACCOUNT_REFERENCE | — | — |
| 48 | ExtBankAccountShortAcctName | SHORT_ACCT_NAME | — | — |
| 49 | ExtBankAccountStartDate | START_DATE | — | — |
| 50 | OldCustBankAccountAccountClassification | ACCOUNT_CLASSIFICATION | — | — |
| 51 | OldCustBankAccountAccountSuffix | ACCOUNT_SUFFIX | — | — |
| 52 | OldCustBankAccountAgencyLocationCode | AGENCY_LOCATION_CODE | — | — |
| 53 | OldCustBankAccountBaMaskSetting | BA_MASK_SETTING | — | — |
| 54 | OldCustBankAccountBaNumElecSecSegmentId | BA_NUM_ELEC_SEC_SEGMENT_ID | — | — |
| 55 | OldCustBankAccountBaNumSecSegmentId | BA_NUM_SEC_SEGMENT_ID | — | — |
| 56 | OldCustBankAccountBaUnmaskLength | BA_UNMASK_LENGTH | — | — |
| 57 | OldCustBankAccountBankAccountName | BANK_ACCOUNT_NAME | — | — |
| 58 | OldCustBankAccountBankAccountNameAlt | BANK_ACCOUNT_NAME_ALT | — | — |
| 59 | OldCustBankAccountBankAccountNum | BANK_ACCOUNT_NUM | — | — |
| 60 | OldCustBankAccountBankAccountNumElectronic | BANK_ACCOUNT_NUM_ELECTRONIC | — | — |
| 61 | OldCustBankAccountBankAccountNumHash1 | BANK_ACCOUNT_NUM_HASH1 | — | — |
| 62 | OldCustBankAccountBankAccountNumHash2 | BANK_ACCOUNT_NUM_HASH2 | — | — |
| 63 | OldCustBankAccountBankAccountType | BANK_ACCOUNT_TYPE | — | — |
| 64 | OldCustBankAccountBankId | BANK_ID | — | — |
| 65 | OldCustBankAccountBranchId | BRANCH_ID | — | — |
| 66 | OldCustBankAccountCheckDigits | CHECK_DIGITS | — | — |
| 67 | OldCustBankAccountCountryCode | COUNTRY_CODE | — | — |
| 68 | OldCustBankAccountCreatedBy | CREATED_BY | — | — |
| 69 | OldCustBankAccountCreationDate | CREATION_DATE | — | — |
| 70 | OldCustBankAccountCurrencyCode | CURRENCY_CODE | — | — |
| 71 | OldCustBankAccountDescription | DESCRIPTION | — | — |
| 72 | OldCustBankAccountEncrypted | ENCRYPTED | — | — |
| 73 | OldCustBankAccountEndDate | END_DATE | — | — |
| 74 | OldCustBankAccountExchangeRate | EXCHANGE_RATE | — | — |
| 75 | OldCustBankAccountExchangeRateAgreementNum | EXCHANGE_RATE_AGREEMENT_NUM | — | — |
| 76 | OldCustBankAccountExchangeRateAgreementType | EXCHANGE_RATE_AGREEMENT_TYPE | — | — |
| 77 | OldCustBankAccountExtBankAccountId | EXT_BANK_ACCOUNT_ID | — | — |
| 78 | OldCustBankAccountForeignPaymentUseFlag | FOREIGN_PAYMENT_USE_FLAG | — | — |
| 79 | OldCustBankAccountHedgingContractReference | HEDGING_CONTRACT_REFERENCE | — | — |
| 80 | OldCustBankAccountIban | IBAN | — | — |
| 81 | OldCustBankAccountIbanHash1 | IBAN_HASH1 | — | — |
| 82 | OldCustBankAccountIbanHash2 | IBAN_HASH2 | — | — |
| 83 | OldCustBankAccountIbanSecSegmentId | IBAN_SEC_SEGMENT_ID | — | — |
| 84 | OldCustBankAccountLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 85 | OldCustBankAccountLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 86 | OldCustBankAccountLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 87 | OldCustBankAccountMaskedBankAccountNum | MASKED_BANK_ACCOUNT_NUM | — | — |
| 88 | OldCustBankAccountMaskedIban | MASKED_IBAN | — | — |
| 89 | OldCustBankAccountObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 90 | OldCustBankAccountPaymentFactorFlag | PAYMENT_FACTOR_FLAG | — | — |
| 91 | OldCustBankAccountProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 92 | OldCustBankAccountProgramId | PROGRAM_ID | — | — |
| 93 | OldCustBankAccountProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 94 | OldCustBankAccountRequestId | REQUEST_ID | — | — |
| 95 | OldCustBankAccountSaltVersion | SALT_VERSION | — | — |
| 96 | OldCustBankAccountSecondaryAccountReference | SECONDARY_ACCOUNT_REFERENCE | — | — |
| 97 | OldCustBankAccountShortAcctName | SHORT_ACCT_NAME | — | — |
| 98 | OldCustBankAccountStartDate | START_DATE | — | — |

### [[iby_fndcpt_tx_extensions|IBY_FNDCPT_TX_EXTENSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrxExtnAdditionalInfo | ADDITIONAL_INFO | — | — |
| 2 | TrxExtnEncrypted | ENCRYPTED | — | — |
| 3 | TrxExtnInstrSecCodeLength | INSTR_SEC_CODE_LENGTH | — | — |
| 4 | TrxExtnInstrumentSecurityCode | INSTRUMENT_SECURITY_CODE | — | — |
| 5 | TrxExtnPaymentChannelCode | PAYMENT_CHANNEL_CODE | — | — |
| 6 | TrxExtnPaymentSystemOrderNumber | PAYMENT_SYSTEM_ORDER_NUMBER | — | ✅ |
| 7 | TrxExtnPoLineNumber | PO_LINE_NUMBER | — | — |
| 8 | TrxExtnPoNumber | PO_NUMBER | — | — |
| 9 | TrxExtnTrxnExtensionId | TRXN_EXTENSION_ID | — | — |
| 10 | TrxExtnTrxnRefNumber1 | TRXN_REF_NUMBER1 | — | — |
| 11 | TrxExtnTrxnRefNumber2 | TRXN_REF_NUMBER2 | — | — |
| 12 | TrxExtnVoiceAuthorizationCode | VOICE_AUTHORIZATION_CODE | — | — |
| 13 | TrxExtnVoiceAuthorizationDate | VOICE_AUTHORIZATION_DATE | — | — |
| 14 | TrxExtnVoiceAuthorizationFlag | VOICE_AUTHORIZATION_FLAG | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PernNameEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PernNameEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | PernNameFirstName | FIRST_NAME | — | — |
| 4 | PernNameFullName | FULL_NAME | — | — |
| 5 | PernNameLastName | LAST_NAME | — | — |
| 6 | PernNameListName | LIST_NAME | — | — |
| 7 | PernNameMiddleNames | MIDDLE_NAMES | — | — |
| 8 | PernNameNamInformationCategory | NAM_INFORMATION_CATEGORY | — | — |
| 9 | PernNameNameType | NAME_TYPE | — | — |
| 10 | PernNameOrderName | ORDER_NAME | — | — |
| 11 | PernNamePersonId | PERSON_ID | — | — |
| 12 | PernNamePersonNameId | PERSON_NAME_ID | — | — |
| 13 | PernNameTitle | TITLE | — | — |
| 14 | PersonCreatedByDisplayName | DISPLAY_NAME | — | — |
| 15 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 16 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 17 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 18 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 19 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | — |
| 20 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 21 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 22 | PersonUpdatedByPersonId | PERSON_ID | — | — |
| 23 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

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

### [[zx_sco_rates|ZX_SCO_RATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxRtScoActiveFlag | ACTIVE_FLAG | — | — |
| 2 | TaxRtScoAdjForAdhocAmtCode | ADJ_FOR_ADHOC_AMT_CODE | — | — |
| 3 | TaxRtScoAllowAdhocTaxRateFlag | ALLOW_ADHOC_TAX_RATE_FLAG | — | — |
| 4 | TaxRtScoAllowExceptionsFlag | ALLOW_EXCEPTIONS_FLAG | — | — |
| 5 | TaxRtScoAllowExemptionsFlag | ALLOW_EXEMPTIONS_FLAG | — | — |
| 6 | TaxRtScoDefRecSettlementOptionCode | DEF_REC_SETTLEMENT_OPTION_CODE | — | — |
| 7 | TaxRtScoDefaultFlgEffectiveFrom | DEFAULT_FLG_EFFECTIVE_FROM | — | — |
| 8 | TaxRtScoDefaultFlgEffectiveTo | DEFAULT_FLG_EFFECTIVE_TO | — | — |
| 9 | TaxRtScoDefaultRateFlag | DEFAULT_RATE_FLAG | — | — |
| 10 | TaxRtScoDefaultRecRateCode | DEFAULT_REC_RATE_CODE | — | — |
| 11 | TaxRtScoDefaultRecTypeCode | DEFAULT_REC_TYPE_CODE | — | — |
| 12 | TaxRtScoDescription | DESCRIPTION | — | — |
| 13 | TaxRtScoEffectiveFrom | EFFECTIVE_FROM | — | — |
| 14 | TaxRtScoEffectiveTo | EFFECTIVE_TO | — | — |
| 15 | TaxRtScoInclusiveTaxFlag | INCLUSIVE_TAX_FLAG | — | — |
| 16 | TaxRtScoObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | TaxRtScoOffsetStatusCode | OFFSET_STATUS_CODE | — | — |
| 18 | TaxRtScoOffsetTax | OFFSET_TAX | — | — |
| 19 | TaxRtScoOffsetTaxRateCode | OFFSET_TAX_RATE_CODE | — | — |
| 20 | TaxRtScoPercentageRate | PERCENTAGE_RATE | — | — |
| 21 | TaxRtScoProgramAppName | PROGRAM_APP_NAME | — | — |
| 22 | TaxRtScoProgramName | PROGRAM_NAME | — | — |
| 23 | TaxRtScoQuantityRate | QUANTITY_RATE | — | — |
| 24 | TaxRtScoRateTypeCode | RATE_TYPE_CODE | — | — |
| 25 | TaxRtScoRecordTypeCode | RECORD_TYPE_CODE | — | — |
| 26 | TaxRtScoRecoveryRuleCode | RECOVERY_RULE_CODE | — | — |
| 27 | TaxRtScoRecoveryTypeCode | RECOVERY_TYPE_CODE | — | — |
| 28 | TaxRtScoScheduleBasedRateFlag | SCHEDULE_BASED_RATE_FLAG | — | — |
| 29 | TaxRtScoSdeffFrom | SDEFF_FROM | — | — |
| 30 | TaxRtScoSdeffTo | SDEFF_TO | — | — |
| 31 | TaxRtScoTax | TAX | — | — |
| 32 | TaxRtScoTaxClass | TAX_CLASS | — | — |
| 33 | TaxRtScoTaxInclusiveOverrideFlag | TAX_INCLUSIVE_OVERRIDE_FLAG | — | — |
| 34 | TaxRtScoTaxJurisdictionCode | TAX_JURISDICTION_CODE | — | — |
| 35 | TaxRtScoTaxRateCode | TAX_RATE_CODE | — | — |
| 36 | TaxRtScoTaxRateId | TAX_RATE_ID | — | — |
| 37 | TaxRtScoTaxRateName | TAX_RATE_NAME | — | ✅ |
| 38 | TaxRtScoTaxRegimeCode | TAX_REGIME_CODE | — | — |
| 39 | TaxRtScoTaxStatusCode | TAX_STATUS_CODE | — | — |
| 40 | TaxRtScoTaxableBasisFormulaCode | TAXABLE_BASIS_FORMULA_CODE | — | — |
| 41 | TaxRtScoUomCode | UOM_CODE | — | — |
| 42 | TaxRtScoVatTransactionTypeCode | VAT_TRANSACTION_TYPE_CODE | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
