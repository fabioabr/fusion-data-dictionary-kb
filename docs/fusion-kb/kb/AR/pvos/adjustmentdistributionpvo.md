---
id: DOC-AR-PVO-AdjustmentDistributionPVO
doc_type: system-doc
title: "AdjustmentDistributionPVO — PVO Accounts Receivable"
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
  - AdjustmentDistributionPVO
  - adjustmentdistributionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AdjustmentDistributionPVO

## 📌 Visão Geral

Extrai as distribuições contábeis dos ajustes em recebíveis, detalhando como cada ajuste impacta contas do razão geral. Fundamental para reconciliação contábil, fechamento de período e rastreamento de impacto financeiro dos ajustes.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.AdjustmentDistributionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 1781 | 32 | 1 | 129 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[ar_adjustments_all|AR_ADJUSTMENTS_ALL]] — 59 atributos (20 BICC)
- [[ar_batches_all|AR_BATCHES_ALL]] — 92 atributos (2 BICC)
- [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]] — 86 atributos (3 BICC)
- [[ar_cons_inv_all|AR_CONS_INV_ALL]] — 50 atributos (3 BICC)
- [[ar_distributions_all|AR_DISTRIBUTIONS_ALL]] — 103 atributos (1 PKs, 23 BICC)
- [[ar_distribution_sets_all|AR_DISTRIBUTION_SETS_ALL]] — 12 atributos (2 BICC)
- [[ar_interest_headers_all|AR_INTEREST_HEADERS_ALL]] — 70 atributos
- [[ar_interest_lines_all|AR_INTEREST_LINES_ALL]] — 22 atributos (4 BICC)
- [[ar_payment_schedules_all|AR_PAYMENT_SCHEDULES_ALL]] — 93 atributos (13 BICC)
- [[ar_receivables_trx_all|AR_RECEIVABLES_TRX_ALL]] — 25 atributos (3 BICC)
- [[ar_receivable_applications_all|AR_RECEIVABLE_APPLICATIONS_ALL]] — 84 atributos (1 BICC)
- [[ar_recon_difference_details|AR_RECON_DIFFERENCE_DETAILS]] — 17 atributos
- [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]] — 12 atributos (2 BICC)
- [[fnd_territories_vl|FND_TERRITORIES_VL]] — 9 atributos
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 1 atributos
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 36 atributos (4 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 3 atributos
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 23 atributos
- [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]] — 3 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos
- [[per_users|PER_USERS]] — 17 atributos (1 BICC)
- [[ra_batches_all|RA_BATCHES_ALL]] — 33 atributos (1 BICC)
- [[ra_batch_sources_all|RA_BATCH_SOURCES_ALL]] — 124 atributos (2 BICC)
- [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]] — 462 atributos (35 BICC)
- [[ra_customer_trx_lines_all|RA_CUSTOMER_TRX_LINES_ALL]] — 301 atributos (2 BICC)
- [[ra_cust_trx_types_all|RA_CUST_TRX_TYPES_ALL]] — 7 atributos (5 BICC)
- [[ra_rules|RA_RULES]] — 3 atributos (1 BICC)
- [[ra_terms_b|RA_TERMS_B]] — 3 atributos
- [[ra_terms_lines|RA_TERMS_LINES]] — 4 atributos (1 BICC)
- [[ra_terms_vl|RA_TERMS_VL]] — 3 atributos
- [[xla_events|XLA_EVENTS]] — 11 atributos
- [[zx_fc_user_defined_v|ZX_FC_USER_DEFINED_V]] — 3 atributos

---

## ⚙️ Atributos

### [[ar_adjustments_all|AR_ADJUSTMENTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustmentAcctdAmount | ACCTD_AMOUNT | — | — |
| 2 | AdjustmentAdjTaxAcctRule | ADJ_TAX_ACCT_RULE | — | — |
| 3 | AdjustmentAdjustmentId | ADJUSTMENT_ID | — | ✅ |
| 4 | AdjustmentAdjustmentNumber | ADJUSTMENT_NUMBER | — | ✅ |
| 5 | AdjustmentAdjustmentType | ADJUSTMENT_TYPE | — | ✅ |
| 6 | AdjustmentAmount | AMOUNT | — | — |
| 7 | AdjustmentApplyDate | APPLY_DATE | — | ✅ |
| 8 | AdjustmentApprovedBy | APPROVED_BY | — | — |
| 9 | AdjustmentAssociatedApplicationId | ASSOCIATED_APPLICATION_ID | — | — |
| 10 | AdjustmentAssociatedCashReceiptId | ASSOCIATED_CASH_RECEIPT_ID | — | — |
| 11 | AdjustmentAutomaticallyGenerated | AUTOMATICALLY_GENERATED | — | — |
| 12 | AdjustmentAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 13 | AdjustmentBatchId | BATCH_ID | — | — |
| 14 | AdjustmentChargebackCustomerTrxId | CHARGEBACK_CUSTOMER_TRX_ID | — | — |
| 15 | AdjustmentCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 16 | AdjustmentComments | COMMENTS | — | ✅ |
| 17 | AdjustmentConsInvId | CONS_INV_ID | — | — |
| 18 | AdjustmentCreatedBy | CREATED_BY | — | ✅ |
| 19 | AdjustmentCreatedFrom | CREATED_FROM | — | — |
| 20 | AdjustmentCreationDate | CREATION_DATE | — | ✅ |
| 21 | AdjustmentCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 22 | AdjustmentCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 23 | AdjustmentDistributionSetId | DISTRIBUTION_SET_ID | — | — |
| 24 | AdjustmentDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 25 | AdjustmentDocSequenceValue | DOC_SEQUENCE_VALUE | — | ✅ |
| 26 | AdjustmentEventId | EVENT_ID | — | ✅ |
| 27 | AdjustmentFreightAdjusted | FREIGHT_ADJUSTED | — | — |
| 28 | AdjustmentGlDate | GL_DATE | — | ✅ |
| 29 | AdjustmentGlPostedDate | GL_POSTED_DATE | — | ✅ |
| 30 | AdjustmentInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 31 | AdjustmentInterestLineId | INTEREST_LINE_ID | — | — |
| 32 | AdjustmentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 33 | AdjustmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 34 | AdjustmentLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 35 | AdjustmentLineAdjusted | LINE_ADJUSTED | — | — |
| 36 | AdjustmentLinkToTrxHistId | LINK_TO_TRX_HIST_ID | — | — |
| 37 | AdjustmentMrcAcctdAmount | MRC_ACCTD_AMOUNT | — | — |
| 38 | AdjustmentMrcGlPostedDate | MRC_GL_POSTED_DATE | — | — |
| 39 | AdjustmentMrcPostingControlId | MRC_POSTING_CONTROL_ID | — | — |
| 40 | AdjustmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 41 | AdjustmentOrgId | ORG_ID | — | ✅ |
| 42 | AdjustmentPaymentScheduleId | PAYMENT_SCHEDULE_ID | — | — |
| 43 | AdjustmentPostable | POSTABLE | — | ✅ |
| 44 | AdjustmentPostingControlId | POSTING_CONTROL_ID | — | ✅ |
| 45 | AdjustmentProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 46 | AdjustmentProgramId | PROGRAM_ID | — | — |
| 47 | AdjustmentProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 48 | AdjustmentReasonCode | REASON_CODE | — | ✅ |
| 49 | AdjustmentReceivablesChargesAdjusted | RECEIVABLES_CHARGES_ADJUSTED | — | — |
| 50 | AdjustmentReceivablesTrxId | RECEIVABLES_TRX_ID | — | — |
| 51 | AdjustmentRequestId | REQUEST_ID | — | — |
| 52 | AdjustmentSetOfBooksId | SET_OF_BOOKS_ID | — | ✅ |
| 53 | AdjustmentStatus | STATUS | — | ✅ |
| 54 | AdjustmentSubsequentTrxId | SUBSEQUENT_TRX_ID | — | — |
| 55 | AdjustmentTaxAdjusted | TAX_ADJUSTED | — | — |
| 56 | AdjustmentType | TYPE | — | ✅ |
| 57 | AdjustmentUpgradeMethod | UPGRADE_METHOD | — | — |
| 58 | AdjustmentUssglTransactionCode | USSGL_TRANSACTION_CODE | — | — |
| 59 | AdjustmentUssglTransactionCodeContext | USSGL_TRANSACTION_CODE_CONTEXT | — | — |

### [[ar_batches_all|AR_BATCHES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReceiptBatch1AutoPrintProgramId | AUTO_PRINT_PROGRAM_ID | — | — |
| 2 | ReceiptBatch1AutoTransProgramId | AUTO_TRANS_PROGRAM_ID | — | — |
| 3 | ReceiptBatch1BankDepositNumber | BANK_DEPOSIT_NUMBER | — | — |
| 4 | ReceiptBatch1BatchAppliedStatus | BATCH_APPLIED_STATUS | — | — |
| 5 | ReceiptBatch1BatchDate | BATCH_DATE | — | — |
| 6 | ReceiptBatch1BatchId | BATCH_ID | — | — |
| 7 | ReceiptBatch1BatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 8 | ReceiptBatch1ClosedDate | CLOSED_DATE | — | — |
| 9 | ReceiptBatch1ControlAmount | CONTROL_AMOUNT | — | — |
| 10 | ReceiptBatch1ControlCount | CONTROL_COUNT | — | — |
| 11 | ReceiptBatch1CreatedBy | CREATED_BY | — | — |
| 12 | ReceiptBatch1CreationDate | CREATION_DATE | — | — |
| 13 | ReceiptBatch1CurrencyCode | CURRENCY_CODE | — | — |
| 14 | ReceiptBatch1DepositDate | DEPOSIT_DATE | — | — |
| 15 | ReceiptBatch1ExchangeDate | EXCHANGE_DATE | — | — |
| 16 | ReceiptBatch1ExchangeRate | EXCHANGE_RATE | — | — |
| 17 | ReceiptBatch1ExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 18 | ReceiptBatch1GlDate | GL_DATE | — | — |
| 19 | ReceiptBatch1LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | ReceiptBatch1LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | ReceiptBatch1LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 22 | ReceiptBatch1LockboxBatchName | LOCKBOX_BATCH_NAME | — | — |
| 23 | ReceiptBatch1LockboxId | LOCKBOX_ID | — | — |
| 24 | ReceiptBatch1MediaReference | MEDIA_REFERENCE | — | — |
| 25 | ReceiptBatch1Name | NAME | — | — |
| 26 | ReceiptBatch1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 27 | ReceiptBatch1OldRemittanceBankBranchId | OLD_REMITTANCE_BANK_BRANCH_ID | — | — |
| 28 | ReceiptBatch1OperationRequestId | OPERATION_REQUEST_ID | — | — |
| 29 | ReceiptBatch1OrgId | ORG_ID | — | — |
| 30 | ReceiptBatch1ProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 31 | ReceiptBatch1ProgramId | PROGRAM_ID | — | — |
| 32 | ReceiptBatch1ProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 33 | ReceiptBatch1PurgedChildrenFlag | PURGED_CHILDREN_FLAG | — | — |
| 34 | ReceiptBatch1ReceiptClassId | RECEIPT_CLASS_ID | — | — |
| 35 | ReceiptBatch1ReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 36 | ReceiptBatch1RemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 37 | ReceiptBatch1RemitMethodCode | REMIT_METHOD_CODE | — | — |
| 38 | ReceiptBatch1RemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 39 | ReceiptBatch1RemittanceBankBranchId | REMITTANCE_BANK_BRANCH_ID | — | — |
| 40 | ReceiptBatch1RequestId | REQUEST_ID | — | — |
| 41 | ReceiptBatch1SetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 42 | ReceiptBatch1Status | STATUS | — | — |
| 43 | ReceiptBatch1TransmissionId | TRANSMISSION_ID | — | — |
| 44 | ReceiptBatch1TransmissionRequestId | TRANSMISSION_REQUEST_ID | — | — |
| 45 | ReceiptBatch1Type | TYPE | — | — |
| 46 | ReceiptBatch1WithRecourseFlag | WITH_RECOURSE_FLAG | — | — |
| 47 | ReceiptBatchAutoPrintProgramId | AUTO_PRINT_PROGRAM_ID | — | — |
| 48 | ReceiptBatchAutoTransProgramId | AUTO_TRANS_PROGRAM_ID | — | — |
| 49 | ReceiptBatchBankDepositNumber | BANK_DEPOSIT_NUMBER | — | — |
| 50 | ReceiptBatchBatchAppliedStatus | BATCH_APPLIED_STATUS | — | — |
| 51 | ReceiptBatchBatchDate | BATCH_DATE | — | — |
| 52 | ReceiptBatchBatchId | BATCH_ID | — | — |
| 53 | ReceiptBatchBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 54 | ReceiptBatchClosedDate | CLOSED_DATE | — | — |
| 55 | ReceiptBatchControlAmount | CONTROL_AMOUNT | — | — |
| 56 | ReceiptBatchControlCount | CONTROL_COUNT | — | — |
| 57 | ReceiptBatchCreatedBy | CREATED_BY | — | — |
| 58 | ReceiptBatchCreationDate | CREATION_DATE | — | — |
| 59 | ReceiptBatchCurrencyCode | CURRENCY_CODE | — | — |
| 60 | ReceiptBatchDepositDate | DEPOSIT_DATE | — | — |
| 61 | ReceiptBatchExchangeDate | EXCHANGE_DATE | — | — |
| 62 | ReceiptBatchExchangeRate | EXCHANGE_RATE | — | — |
| 63 | ReceiptBatchExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 64 | ReceiptBatchGlDate | GL_DATE | — | — |
| 65 | ReceiptBatchLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 66 | ReceiptBatchLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 67 | ReceiptBatchLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 68 | ReceiptBatchLockboxBatchName | LOCKBOX_BATCH_NAME | — | — |
| 69 | ReceiptBatchLockboxId | LOCKBOX_ID | — | — |
| 70 | ReceiptBatchMediaReference | MEDIA_REFERENCE | — | — |
| 71 | ReceiptBatchName | NAME | — | — |
| 72 | ReceiptBatchObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 73 | ReceiptBatchOldRemittanceBankBranchId | OLD_REMITTANCE_BANK_BRANCH_ID | — | — |
| 74 | ReceiptBatchOperationRequestId | OPERATION_REQUEST_ID | — | — |
| 75 | ReceiptBatchOrgId | ORG_ID | — | — |
| 76 | ReceiptBatchProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 77 | ReceiptBatchProgramId | PROGRAM_ID | — | — |
| 78 | ReceiptBatchProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 79 | ReceiptBatchPurgedChildrenFlag | PURGED_CHILDREN_FLAG | — | — |
| 80 | ReceiptBatchReceiptClassId | RECEIPT_CLASS_ID | — | — |
| 81 | ReceiptBatchReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 82 | ReceiptBatchRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 83 | ReceiptBatchRemitMethodCode | REMIT_METHOD_CODE | — | — |
| 84 | ReceiptBatchRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 85 | ReceiptBatchRemittanceBankBranchId | REMITTANCE_BANK_BRANCH_ID | — | — |
| 86 | ReceiptBatchRequestId | REQUEST_ID | — | — |
| 87 | ReceiptBatchSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 88 | ReceiptBatchStatus | STATUS | — | — |
| 89 | ReceiptBatchTransmissionId | TRANSMISSION_ID | — | — |
| 90 | ReceiptBatchTransmissionRequestId | TRANSMISSION_REQUEST_ID | — | — |
| 91 | ReceiptBatchType | TYPE | — | — |
| 92 | ReceiptBatchWithRecourseFlag | WITH_RECOURSE_FLAG | — | — |

### [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReceiptActualValueDate | ACTUAL_VALUE_DATE | — | — |
| 2 | ReceiptAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 3 | ReceiptAmount | AMOUNT | — | — |
| 4 | ReceiptAnticipatedClearingDate | ANTICIPATED_CLEARING_DATE | — | — |
| 5 | ReceiptApplicationNotes | APPLICATION_NOTES | — | — |
| 6 | ReceiptApprovalCode | APPROVAL_CODE | — | — |
| 7 | ReceiptAutoapplyFlag | AUTOAPPLY_FLAG | — | — |
| 8 | ReceiptAutomatchRequestId | AUTOMATCH_REQUEST_ID | — | — |
| 9 | ReceiptAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 10 | ReceiptCashReceiptId | CASH_RECEIPT_ID | — | — |
| 11 | ReceiptCcErrorCode | CC_ERROR_CODE | — | — |
| 12 | ReceiptCcErrorFlag | CC_ERROR_FLAG | — | — |
| 13 | ReceiptCcErrorText | CC_ERROR_TEXT | — | — |
| 14 | ReceiptCodeCombinationId | CODE_COMBINATION_ID | — | — |
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
| 57 | ReceiptReceiptBatchId | RECEIPT_BATCH_ID | — | — |
| 58 | ReceiptReceiptDate | RECEIPT_DATE | — | — |
| 59 | ReceiptReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 60 | ReceiptReceiptNumber | RECEIPT_NUMBER | — | ✅ |
| 61 | ReceiptReceivablesTrxId | RECEIVABLES_TRX_ID | — | — |
| 62 | ReceiptReconFlag | RECON_FLAG | — | — |
| 63 | ReceiptReferenceId | REFERENCE_ID | — | — |
| 64 | ReceiptReferenceType | REFERENCE_TYPE | — | — |
| 65 | ReceiptRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 66 | ReceiptRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 67 | ReceiptRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 68 | ReceiptRequestId | REQUEST_ID | — | — |
| 69 | ReceiptResourceId | RESOURCE_ID | — | — |
| 70 | ReceiptReversalCategory | REVERSAL_CATEGORY | — | — |
| 71 | ReceiptReversalComments | REVERSAL_COMMENTS | — | — |
| 72 | ReceiptReversalDate | REVERSAL_DATE | — | — |
| 73 | ReceiptReversalReasonCode | REVERSAL_REASON_CODE | — | — |
| 74 | ReceiptSelectedForFactoringFlag | SELECTED_FOR_FACTORING_FLAG | — | — |
| 75 | ReceiptSelectedRemittanceBatchId | SELECTED_REMITTANCE_BATCH_ID | — | — |
| 76 | ReceiptSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 77 | ReceiptStatus | STATUS | — | — |
| 78 | ReceiptTaxRate | TAX_RATE | — | — |
| 79 | ReceiptType | TYPE | — | — |
| 80 | ReceiptUniqueReference | UNIQUE_REFERENCE | — | — |
| 81 | ReceiptUssglTransactionCode | USSGL_TRANSACTION_CODE | — | — |
| 82 | ReceiptUssglTransactionCodeContext | USSGL_TRANSACTION_CODE_CONTEXT | — | — |
| 83 | ReceiptVatTaxId | VAT_TAX_ID | — | — |
| 84 | ReverseReceiptCashReceiptId | CASH_RECEIPT_ID | — | — |
| 85 | ReverseReceiptObjectVersionNumber8 | OBJECT_VERSION_NUMBER | — | — |
| 86 | ReverseReceiptReceiptNumber | RECEIPT_NUMBER | — | ✅ |

### [[ar_cons_inv_all|AR_CONS_INV_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConsBillConsInvId1 | CONS_INV_ID | — | — |
| 2 | ConsBillObjectVersionNumber8 | OBJECT_VERSION_NUMBER | — | — |
| 3 | ConsBillingNumber1 | CONS_BILLING_NUMBER | — | — |
| 4 | ConsolidationBillAgingBucket1Amt | AGING_BUCKET1_AMT | — | — |
| 5 | ConsolidationBillAgingBucket2Amt | AGING_BUCKET2_AMT | — | — |
| 6 | ConsolidationBillAgingBucket3Amt | AGING_BUCKET3_AMT | — | — |
| 7 | ConsolidationBillAgingBucket4Amt | AGING_BUCKET4_AMT | — | — |
| 8 | ConsolidationBillAgingBucket5Amt | AGING_BUCKET5_AMT | — | — |
| 9 | ConsolidationBillAgingBucket6Amt | AGING_BUCKET6_AMT | — | — |
| 10 | ConsolidationBillAgingBucket7Amt | AGING_BUCKET7_AMT | — | — |
| 11 | ConsolidationBillBeginningBalance | BEGINNING_BALANCE | — | — |
| 12 | ConsolidationBillBillLevelFlag | BILL_LEVEL_FLAG | — | — |
| 13 | ConsolidationBillBillingCycleId | BILLING_CYCLE_ID | — | — |
| 14 | ConsolidationBillBillingDate | BILLING_DATE | — | — |
| 15 | ConsolidationBillConcurrentRequestId | CONCURRENT_REQUEST_ID | — | — |
| 16 | ConsolidationBillConsBillingNumber | CONS_BILLING_NUMBER | — | ✅ |
| 17 | ConsolidationBillConsInvId | CONS_INV_ID | — | — |
| 18 | ConsolidationBillConsInvType | CONS_INV_TYPE | — | — |
| 19 | ConsolidationBillCreatedBy | CREATED_BY | — | — |
| 20 | ConsolidationBillCreationDate | CREATION_DATE | — | — |
| 21 | ConsolidationBillCurrencyCode | CURRENCY_CODE | — | — |
| 22 | ConsolidationBillCustomerId | CUSTOMER_ID | — | — |
| 23 | ConsolidationBillCutOffDate | CUT_OFF_DATE | — | — |
| 24 | ConsolidationBillDueDate | DUE_DATE | — | — |
| 25 | ConsolidationBillEndingBalance | ENDING_BALANCE | — | — |
| 26 | ConsolidationBillIssueDate | ISSUE_DATE | — | — |
| 27 | ConsolidationBillLastBillingDate | LAST_BILLING_DATE | — | — |
| 28 | ConsolidationBillLastChargeDate | LAST_CHARGE_DATE | — | — |
| 29 | ConsolidationBillLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | ConsolidationBillLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 31 | ConsolidationBillLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 32 | ConsolidationBillObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 33 | ConsolidationBillOrgId | ORG_ID | — | — |
| 34 | ConsolidationBillPrintStatus | PRINT_STATUS | — | — |
| 35 | ConsolidationBillRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 36 | ConsolidationBillRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 37 | ConsolidationBillSiteUseId | SITE_USE_ID | — | — |
| 38 | ConsolidationBillStartDate | START_DATE | — | — |
| 39 | ConsolidationBillStatus | STATUS | — | — |
| 40 | ConsolidationBillTermId | TERM_ID | — | — |
| 41 | ConsolidationBillTotalAdjustmentsAmt | TOTAL_ADJUSTMENTS_AMT | — | — |
| 42 | ConsolidationBillTotalCreditsAmt | TOTAL_CREDITS_AMT | — | — |
| 43 | ConsolidationBillTotalFinanceChargesAmt | TOTAL_FINANCE_CHARGES_AMT | — | — |
| 44 | ConsolidationBillTotalReceiptsAmt | TOTAL_RECEIPTS_AMT | — | — |
| 45 | ConsolidationBillTotalTaxAmt | TOTAL_TAX_AMT | — | — |
| 46 | ConsolidationBillTotalTrxAmt | TOTAL_TRX_AMT | — | — |
| 47 | ConsolidationBillUnpaidReason | UNPAID_REASON | — | — |
| 48 | RevConsBillConsBillingNumber | CONS_BILLING_NUMBER | — | ✅ |
| 49 | RevConsBillConsInvId | CONS_INV_ID | — | — |
| 50 | RevConsBillObjectVersionNumber7 | OBJECT_VERSION_NUMBER | — | — |

### [[ar_distributions_all|AR_DISTRIBUTIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CashDistributionAcctdAmountCr | ACCTD_AMOUNT_CR | — | ✅ |
| 2 | CashDistributionAcctdAmountDr | ACCTD_AMOUNT_DR | — | ✅ |
| 3 | CashDistributionActivityBucket | ACTIVITY_BUCKET | — | ✅ |
| 4 | CashDistributionAmountCr | AMOUNT_CR | — | ✅ |
| 5 | CashDistributionAmountDr | AMOUNT_DR | — | ✅ |
| 6 | CashDistributionCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 7 | CashDistributionCreatedBy | CREATED_BY | — | — |
| 8 | CashDistributionCreationDate | CREATION_DATE | — | — |
| 9 | CashDistributionCurrencyCode | CURRENCY_CODE | — | — |
| 10 | CashDistributionCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 11 | CashDistributionCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 12 | CashDistributionCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 13 | CashDistributionFromAcctdAmountCr | FROM_ACCTD_AMOUNT_CR | — | ✅ |
| 14 | CashDistributionFromAcctdAmountDr | FROM_ACCTD_AMOUNT_DR | — | ✅ |
| 15 | CashDistributionFromAmountCr | FROM_AMOUNT_CR | — | ✅ |
| 16 | CashDistributionFromAmountDr | FROM_AMOUNT_DR | — | ✅ |
| 17 | CashDistributionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | CashDistributionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | CashDistributionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | CashDistributionLocationSegmentId | LOCATION_SEGMENT_ID | — | — |
| 21 | CashDistributionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | CashDistributionOrgId | ORG_ID | — | — |
| 23 | CashDistributionRefAccountClass | REF_ACCOUNT_CLASS | — | ✅ |
| 24 | CashDistributionRefCustTrxLineGlDistId | REF_CUST_TRX_LINE_GL_DIST_ID | — | — |
| 25 | CashDistributionRefCustomerTrxLineId | REF_CUSTOMER_TRX_LINE_ID | — | — |
| 26 | CashDistributionRefDistCcid | REF_DIST_CCID | — | — |
| 27 | CashDistributionRefLineId | REF_LINE_ID | — | — |
| 28 | CashDistributionRefMfDistFlag | REF_MF_DIST_FLAG | — | — |
| 29 | CashDistributionReversalFlag | REVERSAL_FLAG | — | — |
| 30 | CashDistributionReversedSourceId | REVERSED_SOURCE_ID | — | — |
| 31 | CashDistributionSourceId | SOURCE_ID | — | ✅ |
| 32 | CashDistributionSourceIdSecondary | SOURCE_ID_SECONDARY | — | — |
| 33 | CashDistributionSourceTable | SOURCE_TABLE | — | ✅ |
| 34 | CashDistributionSourceTableSecondary | SOURCE_TABLE_SECONDARY | — | — |
| 35 | CashDistributionSourceType | SOURCE_TYPE | — | ✅ |
| 36 | CashDistributionSourceTypeSecondary | SOURCE_TYPE_SECONDARY | — | — |
| 37 | CashDistributionTaxCodeId | TAX_CODE_ID | — | — |
| 38 | CashDistributionTaxGroupCodeId | TAX_GROUP_CODE_ID | — | — |
| 39 | CashDistributionTaxId | TAX_ID | — | — |
| 40 | CashDistributionTaxLinkId | TAX_LINK_ID | — | — |
| 41 | CashDistributionTaxableAccountedCr | TAXABLE_ACCOUNTED_CR | — | ✅ |
| 42 | CashDistributionTaxableAccountedDr | TAXABLE_ACCOUNTED_DR | — | ✅ |
| 43 | CashDistributionTaxableEnteredCr | TAXABLE_ENTERED_CR | — | ✅ |
| 44 | CashDistributionTaxableEnteredDr | TAXABLE_ENTERED_DR | — | ✅ |
| 45 | CashDistributionThirdPartyId | THIRD_PARTY_ID | — | — |
| 46 | CashDistributionThirdPartySubId | THIRD_PARTY_SUB_ID | — | — |
| 47 | CshDistRefLineAcctdAmountCr | ACCTD_AMOUNT_CR | — | — |
| 48 | CshDistRefLineAcctdAmountDr | ACCTD_AMOUNT_DR | — | — |
| 49 | CshDistRefLineActivityBucket | ACTIVITY_BUCKET | — | — |
| 50 | CshDistRefLineAmountCr | AMOUNT_CR | — | — |
| 51 | CshDistRefLineAmountDr | AMOUNT_DR | — | — |
| 52 | CshDistRefLineCurrencyCode | CURRENCY_CODE | — | — |
| 53 | CshDistRefLineCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | — |
| 54 | CshDistRefLineCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | — |
| 55 | CshDistRefLineCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | — |
| 56 | CshDistRefLineFromAcctdAmountCr | FROM_ACCTD_AMOUNT_CR | — | — |
| 57 | CshDistRefLineFromAcctdAmountDr | FROM_ACCTD_AMOUNT_DR | — | — |
| 58 | CshDistRefLineFromAmountCr | FROM_AMOUNT_CR | — | — |
| 59 | CshDistRefLineFromAmountDr | FROM_AMOUNT_DR | — | — |
| 60 | CshDistRefLineLineId | LINE_ID | — | — |
| 61 | CshDistRefLineRefAccountClass | REF_ACCOUNT_CLASS | — | — |
| 62 | CshDistRefLineRefMfDistFlag | REF_MF_DIST_FLAG | — | — |
| 63 | CshDistRefLineReversalFlag | REVERSAL_FLAG | — | — |
| 64 | CshDistRefLineSourceId | SOURCE_ID | — | — |
| 65 | CshDistRefLineSourceIdSecondary | SOURCE_ID_SECONDARY | — | — |
| 66 | CshDistRefLineSourceTable | SOURCE_TABLE | — | — |
| 67 | CshDistRefLineSourceTableSecondary | SOURCE_TABLE_SECONDARY | — | — |
| 68 | CshDistRefLineSourceType | SOURCE_TYPE | — | — |
| 69 | CshDistRefLineSourceTypeSecondary | SOURCE_TYPE_SECONDARY | — | — |
| 70 | CshDistRefLineTaxableAccountedCr | TAXABLE_ACCOUNTED_CR | — | — |
| 71 | CshDistRefLineTaxableAccountedDr | TAXABLE_ACCOUNTED_DR | — | — |
| 72 | CshDistRefLineTaxableEnteredCr | TAXABLE_ENTERED_CR | — | — |
| 73 | CshDistRefLineTaxableEnteredDr | TAXABLE_ENTERED_DR | — | — |
| 74 | CshDistRevSrcAcctdAmountCr | ACCTD_AMOUNT_CR | — | — |
| 75 | CshDistRevSrcAcctdAmountDr | ACCTD_AMOUNT_DR | — | — |
| 76 | CshDistRevSrcActivityBucket | ACTIVITY_BUCKET | — | — |
| 77 | CshDistRevSrcAmountCr | AMOUNT_CR | — | — |
| 78 | CshDistRevSrcAmountDr | AMOUNT_DR | — | — |
| 79 | CshDistRevSrcCurrencyCode | CURRENCY_CODE | — | — |
| 80 | CshDistRevSrcCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | — |
| 81 | CshDistRevSrcCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | — |
| 82 | CshDistRevSrcCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | — |
| 83 | CshDistRevSrcFromAcctdAmountCr | FROM_ACCTD_AMOUNT_CR | — | — |
| 84 | CshDistRevSrcFromAcctdAmountDr | FROM_ACCTD_AMOUNT_DR | — | — |
| 85 | CshDistRevSrcFromAmountCr | FROM_AMOUNT_CR | — | — |
| 86 | CshDistRevSrcFromAmountDr | FROM_AMOUNT_DR | — | — |
| 87 | CshDistRevSrcLineId | LINE_ID | — | — |
| 88 | CshDistRevSrcRefAccountClass | REF_ACCOUNT_CLASS | — | — |
| 89 | CshDistRevSrcRefMfDistFlag | REF_MF_DIST_FLAG | — | — |
| 90 | CshDistRevSrcReversalFlag | REVERSAL_FLAG | — | — |
| 91 | CshDistRevSrcSourceId | SOURCE_ID | — | — |
| 92 | CshDistRevSrcSourceIdSecondary | SOURCE_ID_SECONDARY | — | — |
| 93 | CshDistRevSrcSourceTable | SOURCE_TABLE | — | — |
| 94 | CshDistRevSrcSourceTableSecondary | SOURCE_TABLE_SECONDARY | — | — |
| 95 | CshDistRevSrcSourceType | SOURCE_TYPE | — | — |
| 96 | CshDistRevSrcSourceTypeSecondary | SOURCE_TYPE_SECONDARY | — | — |
| 97 | CshDistRevSrcTaxableAccountedCr | TAXABLE_ACCOUNTED_CR | — | — |
| 98 | CshDistRevSrcTaxableAccountedDr | TAXABLE_ACCOUNTED_DR | — | — |
| 99 | CshDistRevSrcTaxableEnteredCr | TAXABLE_ENTERED_CR | — | — |
| 100 | CshDistRevSrcTaxableEnteredDr | TAXABLE_ENTERED_DR | — | — |
| 101 | LineId | LINE_ID | 🔑 | ✅ |
| 102 | ObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 103 | ObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |

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

### [[ar_interest_headers_all|AR_INTEREST_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IntrstHdrChargeBeginDate | CHARGE_BEGIN_DATE | — | — |
| 2 | IntrstHdrChargeOnFinanceChargeFlag | CHARGE_ON_FINANCE_CHARGE_FLAG | — | — |
| 3 | IntrstHdrCreditItemsFlag | CREDIT_ITEMS_FLAG | — | — |
| 4 | IntrstHdrCurrencyCode | CURRENCY_CODE | — | — |
| 5 | IntrstHdrDisplayFlag | DISPLAY_FLAG | — | — |
| 6 | IntrstHdrDisputedTransactionsFlag | DISPUTED_TRANSACTIONS_FLAG | — | — |
| 7 | IntrstHdrExchangeRate | EXCHANGE_RATE | — | — |
| 8 | IntrstHdrExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 9 | IntrstHdrFinanceChargeDate | FINANCE_CHARGE_DATE | — | — |
| 10 | IntrstHdrHeaderType | HEADER_TYPE | — | — |
| 11 | IntrstHdrHoldChargedInvoicesFlag | HOLD_CHARGED_INVOICES_FLAG | — | — |
| 12 | IntrstHdrInterestCalculationPeriod | INTEREST_CALCULATION_PERIOD | — | — |
| 13 | IntrstHdrInterestFixedAmount | INTEREST_FIXED_AMOUNT | — | — |
| 14 | IntrstHdrInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 15 | IntrstHdrInterestPeriodDays | INTEREST_PERIOD_DAYS | — | — |
| 16 | IntrstHdrInterestRate | INTEREST_RATE | — | — |
| 17 | IntrstHdrInterestType | INTEREST_TYPE | — | — |
| 18 | IntrstHdrLastAccrueChargeDate | LAST_ACCRUE_CHARGE_DATE | — | — |
| 19 | IntrstHdrLateChargeCalculationTrx | LATE_CHARGE_CALCULATION_TRX | — | — |
| 20 | IntrstHdrMaxInterestCharge | MAX_INTEREST_CHARGE | — | — |
| 21 | IntrstHdrMinFcBalanceAmount | MIN_FC_BALANCE_AMOUNT | — | — |
| 22 | IntrstHdrMinFcBalanceOverdueType | MIN_FC_BALANCE_OVERDUE_TYPE | — | — |
| 23 | IntrstHdrMinFcBalancePercent | MIN_FC_BALANCE_PERCENT | — | — |
| 24 | IntrstHdrMinFcInvoiceAmount | MIN_FC_INVOICE_AMOUNT | — | — |
| 25 | IntrstHdrMinFcInvoiceOverdueType | MIN_FC_INVOICE_OVERDUE_TYPE | — | — |
| 26 | IntrstHdrMinFcInvoicePercent | MIN_FC_INVOICE_PERCENT | — | — |
| 27 | IntrstHdrMinInterestCharge | MIN_INTEREST_CHARGE | — | — |
| 28 | IntrstHdrMultipleInterestRatesFlag | MULTIPLE_INTEREST_RATES_FLAG | — | — |
| 29 | IntrstHdrPaymentGraceDays | PAYMENT_GRACE_DAYS | — | — |
| 30 | IntrstHdrPenaltyFixedAmount | PENALTY_FIXED_AMOUNT | — | — |
| 31 | IntrstHdrPenaltyRate | PENALTY_RATE | — | — |
| 32 | IntrstHdrPenaltyType | PENALTY_TYPE | — | — |
| 33 | IntrstHdrProcessMessage | PROCESS_MESSAGE | — | — |
| 34 | IntrstHdrProcessStatus | PROCESS_STATUS | — | — |
| 35 | IntrstHdrTrxHdrChargeBeginDate | CHARGE_BEGIN_DATE | — | — |
| 36 | IntrstHdrTrxHdrChargeOnFinanceChargeFlag | CHARGE_ON_FINANCE_CHARGE_FLAG | — | — |
| 37 | IntrstHdrTrxHdrCreditItemsFlag | CREDIT_ITEMS_FLAG | — | — |
| 38 | IntrstHdrTrxHdrCurrencyCode | CURRENCY_CODE | — | — |
| 39 | IntrstHdrTrxHdrDisplayFlag | DISPLAY_FLAG | — | — |
| 40 | IntrstHdrTrxHdrDisputedTransactionsFlag | DISPUTED_TRANSACTIONS_FLAG | — | — |
| 41 | IntrstHdrTrxHdrExchangeRate | EXCHANGE_RATE | — | — |
| 42 | IntrstHdrTrxHdrExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 43 | IntrstHdrTrxHdrFinanceChargeDate | FINANCE_CHARGE_DATE | — | — |
| 44 | IntrstHdrTrxHdrHeaderType | HEADER_TYPE | — | — |
| 45 | IntrstHdrTrxHdrHoldChargedInvoicesFlag | HOLD_CHARGED_INVOICES_FLAG | — | — |
| 46 | IntrstHdrTrxHdrInterestCalculationPeriod | INTEREST_CALCULATION_PERIOD | — | — |
| 47 | IntrstHdrTrxHdrInterestFixedAmount | INTEREST_FIXED_AMOUNT | — | — |
| 48 | IntrstHdrTrxHdrInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 49 | IntrstHdrTrxHdrInterestPeriodDays | INTEREST_PERIOD_DAYS | — | — |
| 50 | IntrstHdrTrxHdrInterestRate | INTEREST_RATE | — | — |
| 51 | IntrstHdrTrxHdrInterestType | INTEREST_TYPE | — | — |
| 52 | IntrstHdrTrxHdrLastAccrueChargeDate | LAST_ACCRUE_CHARGE_DATE | — | — |
| 53 | IntrstHdrTrxHdrLateChargeCalculationTrx | LATE_CHARGE_CALCULATION_TRX | — | — |
| 54 | IntrstHdrTrxHdrMaxInterestCharge | MAX_INTEREST_CHARGE | — | — |
| 55 | IntrstHdrTrxHdrMinFcBalanceAmount | MIN_FC_BALANCE_AMOUNT | — | — |
| 56 | IntrstHdrTrxHdrMinFcBalanceOverdueType | MIN_FC_BALANCE_OVERDUE_TYPE | — | — |
| 57 | IntrstHdrTrxHdrMinFcBalancePercent | MIN_FC_BALANCE_PERCENT | — | — |
| 58 | IntrstHdrTrxHdrMinFcInvoiceAmount | MIN_FC_INVOICE_AMOUNT | — | — |
| 59 | IntrstHdrTrxHdrMinFcInvoiceOverdueType | MIN_FC_INVOICE_OVERDUE_TYPE | — | — |
| 60 | IntrstHdrTrxHdrMinFcInvoicePercent | MIN_FC_INVOICE_PERCENT | — | — |
| 61 | IntrstHdrTrxHdrMinInterestCharge | MIN_INTEREST_CHARGE | — | — |
| 62 | IntrstHdrTrxHdrMultipleInterestRatesFlag | MULTIPLE_INTEREST_RATES_FLAG | — | — |
| 63 | IntrstHdrTrxHdrPaymentGraceDays | PAYMENT_GRACE_DAYS | — | — |
| 64 | IntrstHdrTrxHdrPenaltyFixedAmount | PENALTY_FIXED_AMOUNT | — | — |
| 65 | IntrstHdrTrxHdrPenaltyRate | PENALTY_RATE | — | — |
| 66 | IntrstHdrTrxHdrPenaltyType | PENALTY_TYPE | — | — |
| 67 | IntrstHdrTrxHdrProcessMessage | PROCESS_MESSAGE | — | — |
| 68 | IntrstHdrTrxHdrProcessStatus | PROCESS_STATUS | — | — |
| 69 | IntrstHdrTrxHdrWorkerNum | WORKER_NUM | — | — |
| 70 | IntrstHdrWorkerNum | WORKER_NUM | — | — |

### [[ar_interest_lines_all|AR_INTEREST_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IntrstLineActualDateClosed | ACTUAL_DATE_CLOSED | — | — |
| 2 | IntrstLineAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 3 | IntrstLineAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 4 | IntrstLineDailyInterestCharge | DAILY_INTEREST_CHARGE | — | — |
| 5 | IntrstLineDaysOfInterest | DAYS_OF_INTEREST | — | ✅ |
| 6 | IntrstLineDaysOverdueLate | DAYS_OVERDUE_LATE | — | ✅ |
| 7 | IntrstLineDueDate | DUE_DATE | — | — |
| 8 | IntrstLineFinanceChargeCharged | FINANCE_CHARGE_CHARGED | — | — |
| 9 | IntrstLineInterestCharged | INTEREST_CHARGED | — | ✅ |
| 10 | IntrstLineInterestLineId | INTEREST_LINE_ID | — | — |
| 11 | IntrstLineInterestRate | INTEREST_RATE | — | ✅ |
| 12 | IntrstLineLastChargeDate | LAST_CHARGE_DATE | — | — |
| 13 | IntrstLineOriginalTrxClass | ORIGINAL_TRX_CLASS | — | — |
| 14 | IntrstLineOutstandingAmount | OUTSTANDING_AMOUNT | — | — |
| 15 | IntrstLinePaymentDate | PAYMENT_DATE | — | — |
| 16 | IntrstLineProcessMessage | PROCESS_MESSAGE | — | — |
| 17 | IntrstLineProcessStatus | PROCESS_STATUS | — | — |
| 18 | IntrstLineRateEndDate | RATE_END_DATE | — | — |
| 19 | IntrstLineRateStartDate | RATE_START_DATE | — | — |
| 20 | IntrstLineScheduleDaysFrom | SCHEDULE_DAYS_FROM | — | — |
| 21 | IntrstLineScheduleDaysTo | SCHEDULE_DAYS_TO | — | — |
| 22 | IntrstLineType | TYPE | — | — |

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
| 10 | PaymentScheduleAmountApplied | AMOUNT_APPLIED | — | — |
| 11 | PaymentScheduleAmountCredited | AMOUNT_CREDITED | — | — |
| 12 | PaymentScheduleAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 13 | PaymentScheduleAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 14 | PaymentScheduleAmountInDispute | AMOUNT_IN_DISPUTE | — | — |
| 15 | PaymentScheduleAmountLineItemsOriginal | AMOUNT_LINE_ITEMS_ORIGINAL | — | — |
| 16 | PaymentScheduleAmountLineItemsRemaining | AMOUNT_LINE_ITEMS_REMAINING | — | — |
| 17 | PaymentScheduleAmountOnAccount | AMOUNT_ON_ACCOUNT | — | — |
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
| 39 | PaymentScheduleCustomerSiteUseId | CUSTOMER_SITE_USE_ID | — | ✅ |
| 40 | PaymentScheduleCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 41 | PaymentScheduleDiscountDate | DISCOUNT_DATE | — | — |
| 42 | PaymentScheduleDiscountOriginal | DISCOUNT_ORIGINAL | — | — |
| 43 | PaymentScheduleDiscountRemaining | DISCOUNT_REMAINING | — | — |
| 44 | PaymentScheduleDiscountTakenEarned | DISCOUNT_TAKEN_EARNED | — | — |
| 45 | PaymentScheduleDiscountTakenUnearned | DISCOUNT_TAKEN_UNEARNED | — | — |
| 46 | PaymentScheduleDisputeDate | DISPUTE_DATE | — | ✅ |
| 47 | PaymentScheduleDueDate | DUE_DATE | — | ✅ |
| 48 | PaymentScheduleDunningLevelOverrideDate | DUNNING_LEVEL_OVERRIDE_DATE | — | — |
| 49 | PaymentScheduleExchangeDate | EXCHANGE_DATE | — | ✅ |
| 50 | PaymentScheduleExchangeRate | EXCHANGE_RATE | — | ✅ |
| 51 | PaymentScheduleExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 52 | PaymentScheduleExcludeFromConsBillFlag | EXCLUDE_FROM_CONS_BILL_FLAG | — | — |
| 53 | PaymentScheduleExcludeFromDunningFlag | EXCLUDE_FROM_DUNNING_FLAG | — | — |
| 54 | PaymentScheduleFollowUpCodeLast | FOLLOW_UP_CODE_LAST | — | — |
| 55 | PaymentScheduleFollowUpDateLast | FOLLOW_UP_DATE_LAST | — | — |
| 56 | PaymentScheduleFreightOriginal | FREIGHT_ORIGINAL | — | — |
| 57 | PaymentScheduleFreightRemaining | FREIGHT_REMAINING | — | — |
| 58 | PaymentScheduleGlDate | GL_DATE | — | ✅ |
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
| 71 | PaymentSchedulePaymentScheduleId | PAYMENT_SCHEDULE_ID | — | ✅ |
| 72 | PaymentScheduleProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 73 | PaymentScheduleProgramId | PROGRAM_ID | — | — |
| 74 | PaymentScheduleProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 75 | PaymentSchedulePromiseAmountLast | PROMISE_AMOUNT_LAST | — | — |
| 76 | PaymentSchedulePromiseDateLast | PROMISE_DATE_LAST | — | — |
| 77 | PaymentScheduleReceiptConfirmedFlag | RECEIPT_CONFIRMED_FLAG | — | — |
| 78 | PaymentScheduleReceivablesChargesCharged | RECEIVABLES_CHARGES_CHARGED | — | — |
| 79 | PaymentScheduleReceivablesChargesRemaining | RECEIVABLES_CHARGES_REMAINING | — | — |
| 80 | PaymentScheduleRequestId | REQUEST_ID | — | — |
| 81 | PaymentScheduleReservedType | RESERVED_TYPE | — | — |
| 82 | PaymentScheduleReservedValue | RESERVED_VALUE | — | — |
| 83 | PaymentScheduleReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 84 | PaymentScheduleSecondLastChargeDate | SECOND_LAST_CHARGE_DATE | — | — |
| 85 | PaymentScheduleSelectedForReceiptBatchId | SELECTED_FOR_RECEIPT_BATCH_ID | — | — |
| 86 | PaymentScheduleStagedDunningLevel | STAGED_DUNNING_LEVEL | — | — |
| 87 | PaymentScheduleStatus | STATUS | — | ✅ |
| 88 | PaymentScheduleTaxOriginal | TAX_ORIGINAL | — | — |
| 89 | PaymentScheduleTaxRemaining | TAX_REMAINING | — | — |
| 90 | PaymentScheduleTermId | TERM_ID | — | — |
| 91 | PaymentScheduleTermsSequenceNumber | TERMS_SEQUENCE_NUMBER | — | ✅ |
| 92 | PaymentScheduleTrxDate | TRX_DATE | — | ✅ |
| 93 | PaymentScheduleTrxNumber | TRX_NUMBER | — | ✅ |

### [[ar_receivables_trx_all|AR_RECEIVABLES_TRX_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReceivableActivityAccountingAffectFlag | ACCOUNTING_AFFECT_FLAG | — | — |
| 2 | ReceivableActivityAssetTaxCode | ASSET_TAX_CODE | — | — |
| 3 | ReceivableActivityCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 4 | ReceivableActivityCreatedBy | CREATED_BY | — | — |
| 5 | ReceivableActivityCreationDate | CREATION_DATE | — | — |
| 6 | ReceivableActivityDefaultAcctgDistributionSet | DEFAULT_ACCTG_DISTRIBUTION_SET | — | — |
| 7 | ReceivableActivityDescription | DESCRIPTION | — | — |
| 8 | ReceivableActivityEndDateActive | END_DATE_ACTIVE | — | — |
| 9 | ReceivableActivityGlAccountSource | GL_ACCOUNT_SOURCE | — | — |
| 10 | ReceivableActivityInactiveDate | INACTIVE_DATE | — | — |
| 11 | ReceivableActivityLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | ReceivableActivityLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | ReceivableActivityLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | ReceivableActivityLiabilityTaxCode | LIABILITY_TAX_CODE | — | — |
| 15 | ReceivableActivityName | NAME | — | ✅ |
| 16 | ReceivableActivityObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | ReceivableActivityOrgId | ORG_ID | — | — |
| 18 | ReceivableActivityReceivablesTrxId | RECEIVABLES_TRX_ID | — | ✅ |
| 19 | ReceivableActivityRiskEliminationDays | RISK_ELIMINATION_DAYS | — | — |
| 20 | ReceivableActivitySetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 21 | ReceivableActivityStartDateActive | START_DATE_ACTIVE | — | — |
| 22 | ReceivableActivityStatus | STATUS | — | — |
| 23 | ReceivableActivityTaxCodeSource | TAX_CODE_SOURCE | — | — |
| 24 | ReceivableActivityTaxRecoverableFlag | TAX_RECOVERABLE_FLAG | — | — |
| 25 | ReceivableActivityType | TYPE | — | — |

### [[ar_receivable_applications_all|AR_RECEIVABLE_APPLICATIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReceivableApplication1AcctdAmountAppliedFrom | ACCTD_AMOUNT_APPLIED_FROM | — | — |
| 2 | ReceivableApplication1AcctdAmountAppliedTo | ACCTD_AMOUNT_APPLIED_TO | — | — |
| 3 | ReceivableApplication1AcctdEarnedDiscountTaken | ACCTD_EARNED_DISCOUNT_TAKEN | — | — |
| 4 | ReceivableApplication1AcctdUnearnedDiscountTaken | ACCTD_UNEARNED_DISCOUNT_TAKEN | — | — |
| 5 | ReceivableApplication1AmountApplied | AMOUNT_APPLIED | — | — |
| 6 | ReceivableApplication1AmountAppliedFrom | AMOUNT_APPLIED_FROM | — | — |
| 7 | ReceivableApplication1ApplicationRefId | APPLICATION_REF_ID | — | — |
| 8 | ReceivableApplication1ApplicationRefNum | APPLICATION_REF_NUM | — | — |
| 9 | ReceivableApplication1ApplicationRefReason | APPLICATION_REF_REASON | — | — |
| 10 | ReceivableApplication1ApplicationRefType | APPLICATION_REF_TYPE | — | — |
| 11 | ReceivableApplication1ApplicationRule | APPLICATION_RULE | — | — |
| 12 | ReceivableApplication1ApplicationType | APPLICATION_TYPE | — | — |
| 13 | ReceivableApplication1AppliedCustomerTrxId | APPLIED_CUSTOMER_TRX_ID | — | — |
| 14 | ReceivableApplication1AppliedCustomerTrxLineId | APPLIED_CUSTOMER_TRX_LINE_ID | — | — |
| 15 | ReceivableApplication1AppliedPaymentScheduleId | APPLIED_PAYMENT_SCHEDULE_ID | — | — |
| 16 | ReceivableApplication1AppliedRecAppId | APPLIED_REC_APP_ID | — | — |
| 17 | ReceivableApplication1ApplyDate | APPLY_DATE | — | — |
| 18 | ReceivableApplication1CashReceiptHistoryId | CASH_RECEIPT_HISTORY_ID | — | — |
| 19 | ReceivableApplication1CashReceiptId | CASH_RECEIPT_ID | — | — |
| 20 | ReceivableApplication1ChargebackCustomerTrxId | CHARGEBACK_CUSTOMER_TRX_ID | — | — |
| 21 | ReceivableApplication1ChargesEdiscounted | CHARGES_EDISCOUNTED | — | — |
| 22 | ReceivableApplication1ChargesUediscounted | CHARGES_UEDISCOUNTED | — | — |
| 23 | ReceivableApplication1CodeCombinationId | CODE_COMBINATION_ID | — | — |
| 24 | ReceivableApplication1Comments | COMMENTS | — | — |
| 25 | ReceivableApplication1ConfirmedFlag | CONFIRMED_FLAG | — | — |
| 26 | ReceivableApplication1ConsInvId | CONS_INV_ID | — | — |
| 27 | ReceivableApplication1ConsInvIdTo | CONS_INV_ID_TO | — | — |
| 28 | ReceivableApplication1CreatedBy | CREATED_BY | — | — |
| 29 | ReceivableApplication1CreationDate | CREATION_DATE | — | — |
| 30 | ReceivableApplication1CustomerReason | CUSTOMER_REASON | — | — |
| 31 | ReceivableApplication1CustomerReference | CUSTOMER_REFERENCE | — | — |
| 32 | ReceivableApplication1CustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 33 | ReceivableApplication1DaysLate | DAYS_LATE | — | — |
| 34 | ReceivableApplication1Display | DISPLAY | — | — |
| 35 | ReceivableApplication1EarnedDiscountCcid | EARNED_DISCOUNT_CCID | — | — |
| 36 | ReceivableApplication1EarnedDiscountTaken | EARNED_DISCOUNT_TAKEN | — | — |
| 37 | ReceivableApplication1EdiscTaxAcctRule | EDISC_TAX_ACCT_RULE | — | — |
| 38 | ReceivableApplication1EventId | EVENT_ID | — | — |
| 39 | ReceivableApplication1ExceptionReasonCode | EXCEPTION_REASON_CODE | — | — |
| 40 | ReceivableApplication1FreightApplied | FREIGHT_APPLIED | — | — |
| 41 | ReceivableApplication1FreightEdiscounted | FREIGHT_EDISCOUNTED | — | — |
| 42 | ReceivableApplication1FreightUediscounted | FREIGHT_UEDISCOUNTED | — | — |
| 43 | ReceivableApplication1GlDate | GL_DATE | — | — |
| 44 | ReceivableApplication1GlPostedDate | GL_POSTED_DATE | — | — |
| 45 | ReceivableApplication1LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 46 | ReceivableApplication1LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 47 | ReceivableApplication1LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 48 | ReceivableApplication1LineApplied | LINE_APPLIED | — | — |
| 49 | ReceivableApplication1LineEdiscounted | LINE_EDISCOUNTED | — | — |
| 50 | ReceivableApplication1LineUediscounted | LINE_UEDISCOUNTED | — | — |
| 51 | ReceivableApplication1LinkToCustomerTrxId | LINK_TO_CUSTOMER_TRX_ID | — | — |
| 52 | ReceivableApplication1LinkToTrxHistId | LINK_TO_TRX_HIST_ID | — | — |
| 53 | ReceivableApplication1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 54 | ReceivableApplication1OnAccountCustomer | ON_ACCOUNT_CUSTOMER | — | — |
| 55 | ReceivableApplication1OrgId | ORG_ID | — | — |
| 56 | ReceivableApplication1PaymentScheduleId | PAYMENT_SCHEDULE_ID | — | — |
| 57 | ReceivableApplication1PaymentSetId | PAYMENT_SET_ID | — | — |
| 58 | ReceivableApplication1Postable | POSTABLE | — | — |
| 59 | ReceivableApplication1PostingControlId | POSTING_CONTROL_ID | — | — |
| 60 | ReceivableApplication1ProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 61 | ReceivableApplication1ProgramId | PROGRAM_ID | — | — |
| 62 | ReceivableApplication1ProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 63 | ReceivableApplication1ReceivableApplicationId | RECEIVABLE_APPLICATION_ID | — | — |
| 64 | ReceivableApplication1ReceivablesChargesApplied | RECEIVABLES_CHARGES_APPLIED | — | — |
| 65 | ReceivableApplication1ReceivablesTrxId | RECEIVABLES_TRX_ID | — | — |
| 66 | ReceivableApplication1RequestId | REQUEST_ID | — | — |
| 67 | ReceivableApplication1ReversalGlDate | REVERSAL_GL_DATE | — | — |
| 68 | ReceivableApplication1RuleSetId | RULE_SET_ID | — | — |
| 69 | ReceivableApplication1SecondaryApplicationRefId | SECONDARY_APPLICATION_REF_ID | — | — |
| 70 | ReceivableApplication1SecondaryApplicationRefNum | SECONDARY_APPLICATION_REF_NUM | — | — |
| 71 | ReceivableApplication1SecondaryApplicationRefType | SECONDARY_APPLICATION_REF_TYPE | — | — |
| 72 | ReceivableApplication1SetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 73 | ReceivableApplication1Status | STATUS | — | — |
| 74 | ReceivableApplication1TaxApplied | TAX_APPLIED | — | — |
| 75 | ReceivableApplication1TaxCode | TAX_CODE | — | — |
| 76 | ReceivableApplication1TaxEdiscounted | TAX_EDISCOUNTED | — | — |
| 77 | ReceivableApplication1TaxUediscounted | TAX_UEDISCOUNTED | — | — |
| 78 | ReceivableApplication1TransToReceiptRate | TRANS_TO_RECEIPT_RATE | — | — |
| 79 | ReceivableApplication1UnearnedDiscountCcid | UNEARNED_DISCOUNT_CCID | — | — |
| 80 | ReceivableApplication1UnearnedDiscountTaken | UNEARNED_DISCOUNT_TAKEN | — | — |
| 81 | ReceivableApplication1UnediscTaxAcctRule | UNEDISC_TAX_ACCT_RULE | — | — |
| 82 | ReceivableApplication1UpgradeMethod | UPGRADE_METHOD | — | — |
| 83 | ReceivableApplication1UssglTransactionCode | USSGL_TRANSACTION_CODE | — | — |
| 84 | ReceivableApplication1UssglTransactionCodeContext | USSGL_TRANSACTION_CODE_CONTEXT | — | — |

### [[ar_recon_difference_details|AR_RECON_DIFFERENCE_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReconDiffAccountedAmount | ACCOUNTED_AMOUNT | — | — |
| 2 | ReconDiffAccountingDate | ACCOUNTING_DATE | — | — |
| 3 | ReconDiffCauseOfDifferenceCode | CAUSE_OF_DIFFERENCE_CODE | — | — |
| 4 | ReconDiffCreatedBy | CREATED_BY | — | — |
| 5 | ReconDiffCreationDate | CREATION_DATE | — | — |
| 6 | ReconDiffDocumentDistributionId | DOCUMENT_DISTRIBUTION_ID | — | — |
| 7 | ReconDiffDocumentId | DOCUMENT_ID | — | — |
| 8 | ReconDiffJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 9 | ReconDiffJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 10 | ReconDiffLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 11 | ReconDiffLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | ReconDiffLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | ReconDiffObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | ReconDiffOrgId | ORG_ID | — | — |
| 15 | ReconDiffReconItemCode | RECON_ITEM_CODE | — | — |
| 16 | ReconDiffReconTrxId | RECON_TRX_ID | — | — |
| 17 | ReconDiffRequestId | REQUEST_ID | — | — |

### [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocSeqAuditTableName | AUDIT_TABLE_NAME | — | — |
| 2 | DocSeqDbSequenceName | DB_SEQUENCE_NAME | — | — |
| 3 | DocSeqDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 4 | DocSeqHdrAuditTableName | AUDIT_TABLE_NAME | — | — |
| 5 | DocSeqHdrDbSequenceName | DB_SEQUENCE_NAME | — | — |
| 6 | DocSeqHdrDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 7 | DocSeqHdrName | NAME | — | — |
| 8 | DocSeqHdrTableName | TABLE_NAME | — | — |
| 9 | DocSeqName | NAME | — | ✅ |
| 10 | DocSeqTableName | TABLE_NAME | — | — |
| 11 | TrxDocSeqHdrDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 12 | TrxDocSeqHdrName | NAME | — | ✅ |

### [[fnd_territories_vl|FND_TERRITORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TerritoryAlternateTerritoryCode | ALTERNATE_TERRITORY_CODE | — | — |
| 2 | TerritoryCurrencyCode | CURRENCY_CODE | — | — |
| 3 | TerritoryDescription | DESCRIPTION | — | — |
| 4 | TerritoryEuCode | EU_CODE | — | — |
| 5 | TerritoryIsoNumericCode | ISO_NUMERIC_CODE | — | — |
| 6 | TerritoryIsoTerritoryCode | ISO_TERRITORY_CODE | — | — |
| 7 | TerritoryNlsTerritory | NLS_TERRITORY | — | — |
| 8 | TerritoryTerritoryCode | TERRITORY_CODE | — | — |
| 9 | TerritoryTerritoryShortName | TERRITORY_SHORT_NAME | — | — |

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitBusinessUnitId | BU_ID | — | — |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CashDailyConversionTypeConversionType | CONVERSION_TYPE | — | — |
| 2 | CashDailyConversionTypeCreatedBy | CREATED_BY | — | — |
| 3 | CashDailyConversionTypeCreationDate | CREATION_DATE | — | ✅ |
| 4 | CashDailyConversionTypeDescription | DESCRIPTION | — | — |
| 5 | CashDailyConversionTypeEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 6 | CashDailyConversionTypeEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 7 | CashDailyConversionTypeFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 8 | CashDailyConversionTypeFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 9 | CashDailyConversionTypeFemScenario | FEM_SCENARIO | — | — |
| 10 | CashDailyConversionTypeFemTimeframe | FEM_TIMEFRAME | — | — |
| 11 | CashDailyConversionTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | CashDailyConversionTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | CashDailyConversionTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | CashDailyConversionTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | CashDailyConversionTypePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 16 | CashDailyConversionTypeSecurityFlag | SECURITY_FLAG | — | — |
| 17 | CashDailyConversionTypeUserConversionType | USER_CONVERSION_TYPE | — | ✅ |
| 18 | CashDailyConversionTypeUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |
| 19 | DailyConversionTypeConversionType | CONVERSION_TYPE | — | — |
| 20 | DailyConversionTypeCreatedBy | CREATED_BY | — | — |
| 21 | DailyConversionTypeCreationDate | CREATION_DATE | — | — |
| 22 | DailyConversionTypeDescription | DESCRIPTION | — | — |
| 23 | DailyConversionTypeEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 24 | DailyConversionTypeEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 25 | DailyConversionTypeFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 26 | DailyConversionTypeFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 27 | DailyConversionTypeFemScenario | FEM_SCENARIO | — | — |
| 28 | DailyConversionTypeFemTimeframe | FEM_TIMEFRAME | — | — |
| 29 | DailyConversionTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | DailyConversionTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 31 | DailyConversionTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 32 | DailyConversionTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 33 | DailyConversionTypePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 34 | DailyConversionTypeSecurityFlag | SECURITY_FLAG | — | — |
| 35 | DailyConversionTypeUserConversionType | USER_CONVERSION_TYPE | — | — |
| 36 | DailyConversionTypeUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 2 | LedgersLedgerId | LEDGER_ID | — | — |
| 3 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[hz_cust_accounts|HZ_CUST_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustAcctAccountEstablishedDate | ACCOUNT_ESTABLISHED_DATE | — | — |
| 2 | CustAcctAccountName | ACCOUNT_NAME | — | — |
| 3 | CustAcctAccountNumber | ACCOUNT_NUMBER | — | — |
| 4 | CustAcctArrivalsetsIncludeLinesFlag | ARRIVALSETS_INCLUDE_LINES_FLAG | — | — |
| 5 | CustAcctAutopayFlag | AUTOPAY_FLAG | — | — |
| 6 | CustAcctComments | COMMENTS | — | — |
| 7 | CustAcctCoterminateDayMonth | COTERMINATE_DAY_MONTH | — | — |
| 8 | CustAcctCreatedByModule | CREATED_BY_MODULE | — | — |
| 9 | CustAcctCustAccountId | CUST_ACCOUNT_ID | — | — |
| 10 | CustAcctCustomerClassCode | CUSTOMER_CLASS_CODE | — | — |
| 11 | CustAcctCustomerType | CUSTOMER_TYPE | — | — |
| 12 | CustAcctDateTypePreference | DATE_TYPE_PREFERENCE | — | — |
| 13 | CustAcctDepositRefundMethod | DEPOSIT_REFUND_METHOD | — | — |
| 14 | CustAcctHeldBillExpirationDate | HELD_BILL_EXPIRATION_DATE | — | — |
| 15 | CustAcctHoldBillFlag | HOLD_BILL_FLAG | — | — |
| 16 | CustAcctNpaNumber | NPA_NUMBER | — | — |
| 17 | CustAcctOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 18 | CustAcctSourceCode | SOURCE_CODE | — | — |
| 19 | CustAcctStatus | STATUS | — | — |
| 20 | CustAcctStatusUpdateDate | STATUS_UPDATE_DATE | — | — |
| 21 | CustAcctTaxCode | TAX_CODE | — | — |
| 22 | CustAcctTaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | — |
| 23 | CustAcctTaxRoundingRule | TAX_ROUNDING_RULE | — | — |

### [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExternalBankAccountBankAccountNum | BANK_ACCOUNT_NUM | — | ✅ |
| 2 | ExternalBankAccountExtBankAccountId | EXT_BANK_ACCOUNT_ID | — | — |
| 3 | ExternalBankAccountObjectVersionNumber12 | OBJECT_VERSION_NUMBER | — | — |

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
| 1 | ApprovedUserActiveFlag | ACTIVE_FLAG | — | — |
| 2 | ApprovedUserEndDate | END_DATE | — | — |
| 3 | ApprovedUserHrTerminated | HR_TERMINATED | — | — |
| 4 | ApprovedUserStartDate | START_DATE | — | — |
| 5 | ApprovedUserSuspended | SUSPENDED | — | — |
| 6 | ApprovedUserUserGuid | USER_GUID | — | — |
| 7 | ApprovedUserUserId | USER_ID | — | — |
| 8 | ApprovedUserUsername | USERNAME | — | ✅ |
| 9 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 10 | ObjectVersionNumber8 | OBJECT_VERSION_NUMBER | — | — |
| 11 | UserCreatedByUserGuid | USER_GUID | — | — |
| 12 | UserCreatedByUserId | USER_ID | — | — |
| 13 | UserCreatedByUsername | USERNAME | — | — |
| 14 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 15 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 16 | UserUpdatedByUserId | USER_ID | — | — |
| 17 | UserUpdatedByUsername | USERNAME | — | — |

### [[ra_batches_all|RA_BATCHES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionBatchBatchDate | BATCH_DATE | — | — |
| 2 | TransactionBatchBatchId | BATCH_ID | — | — |
| 3 | TransactionBatchBatchProcessStatus | BATCH_PROCESS_STATUS | — | — |
| 4 | TransactionBatchBatchSourceId | BATCH_SOURCE_ID | — | — |
| 5 | TransactionBatchBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 6 | TransactionBatchComments | COMMENTS | — | — |
| 7 | TransactionBatchControlAmount | CONTROL_AMOUNT | — | — |
| 8 | TransactionBatchControlCount | CONTROL_COUNT | — | — |
| 9 | TransactionBatchCreatedBy | CREATED_BY | — | — |
| 10 | TransactionBatchCreationDate | CREATION_DATE | — | — |
| 11 | TransactionBatchCurrencyCode | CURRENCY_CODE | — | — |
| 12 | TransactionBatchExchangeDate | EXCHANGE_DATE | — | — |
| 13 | TransactionBatchExchangeRate | EXCHANGE_RATE | — | — |
| 14 | TransactionBatchExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 15 | TransactionBatchGlDate | GL_DATE | — | — |
| 16 | TransactionBatchIssueDate | ISSUE_DATE | — | — |
| 17 | TransactionBatchLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | TransactionBatchLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | TransactionBatchLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | TransactionBatchMaturityDate | MATURITY_DATE | — | — |
| 21 | TransactionBatchName | NAME | — | — |
| 22 | TransactionBatchObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | TransactionBatchOrgId | ORG_ID | — | — |
| 24 | TransactionBatchProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 25 | TransactionBatchProgramId | PROGRAM_ID | — | — |
| 26 | TransactionBatchProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 27 | TransactionBatchPurgedChildrenFlag | PURGED_CHILDREN_FLAG | — | — |
| 28 | TransactionBatchRequestId | REQUEST_ID | — | — |
| 29 | TransactionBatchSelectionCriteriaId | SELECTION_CRITERIA_ID | — | — |
| 30 | TransactionBatchSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 31 | TransactionBatchSpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 32 | TransactionBatchStatus | STATUS | — | — |
| 33 | TransactionBatchType | TYPE | — | — |

### [[ra_batch_sources_all|RA_BATCH_SOURCES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionBatchSourceAccountingFlexfieldRule | ACCOUNTING_FLEXFIELD_RULE | — | — |
| 2 | TransactionBatchSourceAccountingRuleRule | ACCOUNTING_RULE_RULE | — | — |
| 3 | TransactionBatchSourceAgreementRule | AGREEMENT_RULE | — | — |
| 4 | TransactionBatchSourceAllowDuplicateTrxNumFlag | ALLOW_DUPLICATE_TRX_NUM_FLAG | — | — |
| 5 | TransactionBatchSourceAllowSalesCreditFlag | ALLOW_SALES_CREDIT_FLAG | — | — |
| 6 | TransactionBatchSourceAutoBatchNumberingFlag | AUTO_BATCH_NUMBERING_FLAG | — | — |
| 7 | TransactionBatchSourceAutoTrxNumberingFlag | AUTO_TRX_NUMBERING_FLAG | — | — |
| 8 | TransactionBatchSourceBatchSourceId | BATCH_SOURCE_ID | — | — |
| 9 | TransactionBatchSourceBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 10 | TransactionBatchSourceBatchSourceType | BATCH_SOURCE_TYPE | — | — |
| 11 | TransactionBatchSourceBillAddressRule | BILL_ADDRESS_RULE | — | — |
| 12 | TransactionBatchSourceBillContactRule | BILL_CONTACT_RULE | — | — |
| 13 | TransactionBatchSourceBillCustomerRule | BILL_CUSTOMER_RULE | — | — |
| 14 | TransactionBatchSourceCmBatchSourceSeqId | CM_BATCH_SOURCE_SEQ_ID | — | — |
| 15 | TransactionBatchSourceCopyDocNumberFlag | COPY_DOC_NUMBER_FLAG | — | — |
| 16 | TransactionBatchSourceCopyInvTidffToCmFlag | COPY_INV_TIDFF_TO_CM_FLAG | — | — |
| 17 | TransactionBatchSourceCreateClearingFlag | CREATE_CLEARING_FLAG | — | — |
| 18 | TransactionBatchSourceCreatedBy | CREATED_BY | — | — |
| 19 | TransactionBatchSourceCreationDate | CREATION_DATE | — | — |
| 20 | TransactionBatchSourceCreditMemoBatchSourceId | CREDIT_MEMO_BATCH_SOURCE_ID | — | — |
| 21 | TransactionBatchSourceCustTrxTypeRule | CUST_TRX_TYPE_RULE | — | — |
| 22 | TransactionBatchSourceCustomerBankAccountRule | CUSTOMER_BANK_ACCOUNT_RULE | — | — |
| 23 | TransactionBatchSourceDefaultInvTrxType | DEFAULT_INV_TRX_TYPE | — | — |
| 24 | TransactionBatchSourceDefaultInvTrxTypeSeqId | DEFAULT_INV_TRX_TYPE_SEQ_ID | — | — |
| 25 | TransactionBatchSourceDefaultReference | DEFAULT_REFERENCE | — | — |
| 26 | TransactionBatchSourceDeriveDateFlag | DERIVE_DATE_FLAG | — | — |
| 27 | TransactionBatchSourceDescription | DESCRIPTION | — | — |
| 28 | TransactionBatchSourceEndDate | END_DATE | — | — |
| 29 | TransactionBatchSourceFobPointRule | FOB_POINT_RULE | — | — |
| 30 | TransactionBatchSourceGlDatePeriodRule | GL_DATE_PERIOD_RULE | — | — |
| 31 | TransactionBatchSourceGroupingRuleId | GROUPING_RULE_ID | — | — |
| 32 | TransactionBatchSourceInvalidLinesRule | INVALID_LINES_RULE | — | — |
| 33 | TransactionBatchSourceInvalidTaxRateRule | INVALID_TAX_RATE_RULE | — | — |
| 34 | TransactionBatchSourceInventoryItemRule | INVENTORY_ITEM_RULE | — | — |
| 35 | TransactionBatchSourceInvoicingRuleRule | INVOICING_RULE_RULE | — | — |
| 36 | TransactionBatchSourceLastBatchNum | LAST_BATCH_NUM | — | — |
| 37 | TransactionBatchSourceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 38 | TransactionBatchSourceLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 39 | TransactionBatchSourceLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 40 | TransactionBatchSourceLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 41 | TransactionBatchSourceMemoLineRule | MEMO_LINE_RULE | — | — |
| 42 | TransactionBatchSourceMemoReasonRule | MEMO_REASON_RULE | — | — |
| 43 | TransactionBatchSourceName | NAME | — | — |
| 44 | TransactionBatchSourceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 45 | TransactionBatchSourceParentAccountingFlexfieldRule | ACCOUNTING_FLEXFIELD_RULE | — | — |
| 46 | TransactionBatchSourceParentAccountingRuleRule | ACCOUNTING_RULE_RULE | — | — |
| 47 | TransactionBatchSourceParentAgreementRule | AGREEMENT_RULE | — | — |
| 48 | TransactionBatchSourceParentAllowDuplicateTrxNumFlag | ALLOW_DUPLICATE_TRX_NUM_FLAG | — | — |
| 49 | TransactionBatchSourceParentAllowSalesCreditFlag | ALLOW_SALES_CREDIT_FLAG | — | — |
| 50 | TransactionBatchSourceParentAutoBatchNumberingFlag | AUTO_BATCH_NUMBERING_FLAG | — | — |
| 51 | TransactionBatchSourceParentAutoTrxNumberingFlag | AUTO_TRX_NUMBERING_FLAG | — | — |
| 52 | TransactionBatchSourceParentBatchSourceId | BATCH_SOURCE_ID | — | — |
| 53 | TransactionBatchSourceParentBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 54 | TransactionBatchSourceParentBatchSourceType | BATCH_SOURCE_TYPE | — | — |
| 55 | TransactionBatchSourceParentBillAddressRule | BILL_ADDRESS_RULE | — | — |
| 56 | TransactionBatchSourceParentBillContactRule | BILL_CONTACT_RULE | — | — |
| 57 | TransactionBatchSourceParentBillCustomerRule | BILL_CUSTOMER_RULE | — | — |
| 58 | TransactionBatchSourceParentCmBatchSourceSeqId | CM_BATCH_SOURCE_SEQ_ID | — | — |
| 59 | TransactionBatchSourceParentCopyDocNumberFlag | COPY_DOC_NUMBER_FLAG | — | — |
| 60 | TransactionBatchSourceParentCopyInvTidffToCmFlag | COPY_INV_TIDFF_TO_CM_FLAG | — | — |
| 61 | TransactionBatchSourceParentCreateClearingFlag | CREATE_CLEARING_FLAG | — | — |
| 62 | TransactionBatchSourceParentCreatedBy | CREATED_BY | — | — |
| 63 | TransactionBatchSourceParentCreationDate | CREATION_DATE | — | — |
| 64 | TransactionBatchSourceParentCreditMemoBatchSourceId | CREDIT_MEMO_BATCH_SOURCE_ID | — | — |
| 65 | TransactionBatchSourceParentCustTrxTypeRule | CUST_TRX_TYPE_RULE | — | — |
| 66 | TransactionBatchSourceParentCustomerBankAccountRule | CUSTOMER_BANK_ACCOUNT_RULE | — | — |
| 67 | TransactionBatchSourceParentDefaultInvTrxType | DEFAULT_INV_TRX_TYPE | — | — |
| 68 | TransactionBatchSourceParentDefaultInvTrxTypeSeqId | DEFAULT_INV_TRX_TYPE_SEQ_ID | — | — |
| 69 | TransactionBatchSourceParentDefaultReference | DEFAULT_REFERENCE | — | — |
| 70 | TransactionBatchSourceParentDeriveDateFlag | DERIVE_DATE_FLAG | — | — |
| 71 | TransactionBatchSourceParentDescription | DESCRIPTION | — | — |
| 72 | TransactionBatchSourceParentEndDate | END_DATE | — | — |
| 73 | TransactionBatchSourceParentFobPointRule | FOB_POINT_RULE | — | — |
| 74 | TransactionBatchSourceParentGlDatePeriodRule | GL_DATE_PERIOD_RULE | — | — |
| 75 | TransactionBatchSourceParentGroupingRuleId | GROUPING_RULE_ID | — | — |
| 76 | TransactionBatchSourceParentInvalidLinesRule | INVALID_LINES_RULE | — | — |
| 77 | TransactionBatchSourceParentInvalidTaxRateRule | INVALID_TAX_RATE_RULE | — | — |
| 78 | TransactionBatchSourceParentInventoryItemRule | INVENTORY_ITEM_RULE | — | — |
| 79 | TransactionBatchSourceParentInvoicingRuleRule | INVOICING_RULE_RULE | — | — |
| 80 | TransactionBatchSourceParentLastBatchNum | LAST_BATCH_NUM | — | — |
| 81 | TransactionBatchSourceParentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 82 | TransactionBatchSourceParentLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 83 | TransactionBatchSourceParentLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 84 | TransactionBatchSourceParentLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 85 | TransactionBatchSourceParentMemoLineRule | MEMO_LINE_RULE | — | — |
| 86 | TransactionBatchSourceParentMemoReasonRule | MEMO_REASON_RULE | — | — |
| 87 | TransactionBatchSourceParentName | NAME | — | — |
| 88 | TransactionBatchSourceParentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 89 | TransactionBatchSourceParentReceiptHandlingOption | RECEIPT_HANDLING_OPTION | — | — |
| 90 | TransactionBatchSourceParentReceiptMethodRule | RECEIPT_METHOD_RULE | — | — |
| 91 | TransactionBatchSourceParentRelatedDocumentRule | RELATED_DOCUMENT_RULE | — | — |
| 92 | TransactionBatchSourceParentRevAccAllocationRule | REV_ACC_ALLOCATION_RULE | — | — |
| 93 | TransactionBatchSourceParentSalesCreditRule | SALES_CREDIT_RULE | — | — |
| 94 | TransactionBatchSourceParentSalesCreditTypeRule | SALES_CREDIT_TYPE_RULE | — | — |
| 95 | TransactionBatchSourceParentSalesTerritoryRule | SALES_TERRITORY_RULE | — | — |
| 96 | TransactionBatchSourceParentSalespersonRule | SALESPERSON_RULE | — | — |
| 97 | TransactionBatchSourceParentSetId | SET_ID | — | — |
| 98 | TransactionBatchSourceParentShipAddressRule | SHIP_ADDRESS_RULE | — | — |
| 99 | TransactionBatchSourceParentShipContactRule | SHIP_CONTACT_RULE | — | — |
| 100 | TransactionBatchSourceParentShipCustomerRule | SHIP_CUSTOMER_RULE | — | — |
| 101 | TransactionBatchSourceParentShipViaRule | SHIP_VIA_RULE | — | — |
| 102 | TransactionBatchSourceParentSoldCustomerRule | SOLD_CUSTOMER_RULE | — | — |
| 103 | TransactionBatchSourceParentStartDate | START_DATE | — | — |
| 104 | TransactionBatchSourceParentStatus | STATUS | — | — |
| 105 | TransactionBatchSourceParentTermRule | TERM_RULE | — | — |
| 106 | TransactionBatchSourceParentUnitOfMeasureRule | UNIT_OF_MEASURE_RULE | — | — |
| 107 | TransactionBatchSourceReceiptHandlingOption | RECEIPT_HANDLING_OPTION | — | — |
| 108 | TransactionBatchSourceReceiptMethodRule | RECEIPT_METHOD_RULE | — | — |
| 109 | TransactionBatchSourceRelatedDocumentRule | RELATED_DOCUMENT_RULE | — | — |
| 110 | TransactionBatchSourceRevAccAllocationRule | REV_ACC_ALLOCATION_RULE | — | — |
| 111 | TransactionBatchSourceSalesCreditRule | SALES_CREDIT_RULE | — | — |
| 112 | TransactionBatchSourceSalesCreditTypeRule | SALES_CREDIT_TYPE_RULE | — | — |
| 113 | TransactionBatchSourceSalesTerritoryRule | SALES_TERRITORY_RULE | — | — |
| 114 | TransactionBatchSourceSalespersonRule | SALESPERSON_RULE | — | — |
| 115 | TransactionBatchSourceSetId | SET_ID | — | — |
| 116 | TransactionBatchSourceShipAddressRule | SHIP_ADDRESS_RULE | — | — |
| 117 | TransactionBatchSourceShipContactRule | SHIP_CONTACT_RULE | — | — |
| 118 | TransactionBatchSourceShipCustomerRule | SHIP_CUSTOMER_RULE | — | — |
| 119 | TransactionBatchSourceShipViaRule | SHIP_VIA_RULE | — | — |
| 120 | TransactionBatchSourceSoldCustomerRule | SOLD_CUSTOMER_RULE | — | — |
| 121 | TransactionBatchSourceStartDate | START_DATE | — | — |
| 122 | TransactionBatchSourceStatus | STATUS | — | — |
| 123 | TransactionBatchSourceTermRule | TERM_RULE | — | — |
| 124 | TransactionBatchSourceUnitOfMeasureRule | UNIT_OF_MEASURE_RULE | — | — |

### [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionHeader1AddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 2 | TransactionHeader1AgreementId | AGREEMENT_ID | — | — |
| 3 | TransactionHeader1ApplicationId | APPLICATION_ID | — | — |
| 4 | TransactionHeader1ApprovalCode | APPROVAL_CODE | — | — |
| 5 | TransactionHeader1AxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 6 | TransactionHeader1BatchId | BATCH_ID | — | — |
| 7 | TransactionHeader1BatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 8 | TransactionHeader1BillTemplateId | BILL_TEMPLATE_ID | — | — |
| 9 | TransactionHeader1BillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 10 | TransactionHeader1BillToContactId | BILL_TO_CONTACT_ID | — | — |
| 11 | TransactionHeader1BillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 12 | TransactionHeader1BillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 13 | TransactionHeader1BillingDate | BILLING_DATE | — | — |
| 14 | TransactionHeader1BrAmount | BR_AMOUNT | — | — |
| 15 | TransactionHeader1BrOnHoldFlag | BR_ON_HOLD_FLAG | — | — |
| 16 | TransactionHeader1BrUnpaidFlag | BR_UNPAID_FLAG | — | — |
| 17 | TransactionHeader1CcErrorCode | CC_ERROR_CODE | — | — |
| 18 | TransactionHeader1CcErrorFlag | CC_ERROR_FLAG | — | — |
| 19 | TransactionHeader1CcErrorText | CC_ERROR_TEXT | — | — |
| 20 | TransactionHeader1Comments | COMMENTS | — | — |
| 21 | TransactionHeader1CompleteFlag | COMPLETE_FLAG | — | — |
| 22 | TransactionHeader1ContractId | CONTRACT_ID | — | — |
| 23 | TransactionHeader1CreatedBy | CREATED_BY | — | — |
| 24 | TransactionHeader1CreatedFrom | CREATED_FROM | — | — |
| 25 | TransactionHeader1CreationDate | CREATION_DATE | — | — |
| 26 | TransactionHeader1CreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | — |
| 27 | TransactionHeader1CreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | — |
| 28 | TransactionHeader1CtReference | CT_REFERENCE | — | — |
| 29 | TransactionHeader1CustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 30 | TransactionHeader1CustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 31 | TransactionHeader1CustomerReference | CUSTOMER_REFERENCE | — | — |
| 32 | TransactionHeader1CustomerReferenceDate | CUSTOMER_REFERENCE_DATE | — | — |
| 33 | TransactionHeader1CustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 34 | TransactionHeader1DefaultTaxExemptFlag | DEFAULT_TAX_EXEMPT_FLAG | — | — |
| 35 | TransactionHeader1DefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 36 | TransactionHeader1DefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 37 | TransactionHeader1DocSequenceId | DOC_SEQUENCE_ID | — | — |
| 38 | TransactionHeader1DocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 39 | TransactionHeader1DraweeBankAccountId | DRAWEE_BANK_ACCOUNT_ID | — | — |
| 40 | TransactionHeader1DraweeContactId | DRAWEE_CONTACT_ID | — | — |
| 41 | TransactionHeader1DraweeId | DRAWEE_ID | — | — |
| 42 | TransactionHeader1DraweeSiteUseId | DRAWEE_SITE_USE_ID | — | — |
| 43 | TransactionHeader1EdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 44 | TransactionHeader1EdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 45 | TransactionHeader1EndDateCommitment | END_DATE_COMMITMENT | — | — |
| 46 | TransactionHeader1ExchangeDate | EXCHANGE_DATE | — | — |
| 47 | TransactionHeader1ExchangeRate | EXCHANGE_RATE | — | — |
| 48 | TransactionHeader1ExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 49 | TransactionHeader1FinanceCharges | FINANCE_CHARGES | — | — |
| 50 | TransactionHeader1FobPoint | FOB_POINT | — | — |
| 51 | TransactionHeader1InitialCustomerTrxId | INITIAL_CUSTOMER_TRX_ID | — | — |
| 52 | TransactionHeader1IntercompanyFlag | INTERCOMPANY_FLAG | — | — |
| 53 | TransactionHeader1InterestHeaderId | INTEREST_HEADER_ID | — | — |
| 54 | TransactionHeader1InterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | — |
| 55 | TransactionHeader1InterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | — |
| 56 | TransactionHeader1InterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | — |
| 57 | TransactionHeader1InterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | — |
| 58 | TransactionHeader1InterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | — |
| 59 | TransactionHeader1InterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | — |
| 60 | TransactionHeader1InterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | — |
| 61 | TransactionHeader1InterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | — |
| 62 | TransactionHeader1InterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | — |
| 63 | TransactionHeader1InterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | — |
| 64 | TransactionHeader1InterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | — |
| 65 | TransactionHeader1InterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | — |
| 66 | TransactionHeader1InterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | — |
| 67 | TransactionHeader1InterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | — |
| 68 | TransactionHeader1InterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | — |
| 69 | TransactionHeader1InterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | — |
| 70 | TransactionHeader1InternalNotes | INTERNAL_NOTES | — | — |
| 71 | TransactionHeader1InvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 72 | TransactionHeader1InvoicingRuleId | INVOICING_RULE_ID | — | — |
| 73 | TransactionHeader1LastPrintedSequenceNum | LAST_PRINTED_SEQUENCE_NUM | — | — |
| 74 | TransactionHeader1LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 75 | TransactionHeader1LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 76 | TransactionHeader1LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 77 | TransactionHeader1LateChargesAssessed | LATE_CHARGES_ASSESSED | — | — |
| 78 | TransactionHeader1LegalEntityId | LEGAL_ENTITY_ID | — | — |
| 79 | TransactionHeader1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 80 | TransactionHeader1OldTrxNumber | OLD_TRX_NUMBER | — | — |
| 81 | TransactionHeader1OrgId | ORG_ID | — | — |
| 82 | TransactionHeader1OrigSystemBatchName | ORIG_SYSTEM_BATCH_NAME | — | — |
| 83 | TransactionHeader1OverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 84 | TransactionHeader1PayingCustomerId | PAYING_CUSTOMER_ID | — | — |
| 85 | TransactionHeader1PayingSiteUseId | PAYING_SITE_USE_ID | — | — |
| 86 | TransactionHeader1PaymentAttributes | PAYMENT_ATTRIBUTES | — | — |
| 87 | TransactionHeader1PaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 88 | TransactionHeader1PaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 89 | TransactionHeader1PostRequestId | POST_REQUEST_ID | — | — |
| 90 | TransactionHeader1PostingControlId | POSTING_CONTROL_ID | — | — |
| 91 | TransactionHeader1PrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 92 | TransactionHeader1PreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 93 | TransactionHeader1PrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | — |
| 94 | TransactionHeader1PrintingCount | PRINTING_COUNT | — | — |
| 95 | TransactionHeader1PrintingLastPrinted | PRINTING_LAST_PRINTED | — | — |
| 96 | TransactionHeader1PrintingOption | PRINTING_OPTION | — | — |
| 97 | TransactionHeader1PrintingOriginalDate | PRINTING_ORIGINAL_DATE | — | — |
| 98 | TransactionHeader1PrintingPending | PRINTING_PENDING | — | — |
| 99 | TransactionHeader1ProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 100 | TransactionHeader1ProgramId | PROGRAM_ID | — | — |
| 101 | TransactionHeader1ProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 102 | TransactionHeader1PurchaseOrder | PURCHASE_ORDER | — | — |
| 103 | TransactionHeader1PurchaseOrderDate | PURCHASE_ORDER_DATE | — | — |
| 104 | TransactionHeader1PurchaseOrderRevision | PURCHASE_ORDER_REVISION | — | — |
| 105 | TransactionHeader1RaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 106 | TransactionHeader1ReasonCode | REASON_CODE | — | — |
| 107 | TransactionHeader1ReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 108 | TransactionHeader1RecurredFromTrxNumber | RECURRED_FROM_TRX_NUMBER | — | — |
| 109 | TransactionHeader1RelatedBatchSourceSeqId | RELATED_BATCH_SOURCE_SEQ_ID | — | — |
| 110 | TransactionHeader1RelatedCustomerTrxId | RELATED_CUSTOMER_TRX_ID | — | — |
| 111 | TransactionHeader1RemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 112 | TransactionHeader1RemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 113 | TransactionHeader1RemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 114 | TransactionHeader1RemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 115 | TransactionHeader1RemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 116 | TransactionHeader1RequestId | REQUEST_ID | — | — |
| 117 | TransactionHeader1ReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 118 | TransactionHeader1SetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 119 | TransactionHeader1ShipDateActual | SHIP_DATE_ACTUAL | — | — |
| 120 | TransactionHeader1ShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 121 | TransactionHeader1ShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 122 | TransactionHeader1ShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 123 | TransactionHeader1ShipToPartyId | SHIP_TO_PARTY_ID | — | — |
| 124 | TransactionHeader1ShipToPartySiteUseId | SHIP_TO_PARTY_SITE_USE_ID | — | — |
| 125 | TransactionHeader1ShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 126 | TransactionHeader1ShipVia | SHIP_VIA | — | — |
| 127 | TransactionHeader1ShipmentId | SHIPMENT_ID | — | — |
| 128 | TransactionHeader1SoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 129 | TransactionHeader1SoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 130 | TransactionHeader1SoldToPartyId | SOLD_TO_PARTY_ID | — | — |
| 131 | TransactionHeader1SoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | — |
| 132 | TransactionHeader1SourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 133 | TransactionHeader1SourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 134 | TransactionHeader1SpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 135 | TransactionHeader1StartDateCommitment | START_DATE_COMMITMENT | — | — |
| 136 | TransactionHeader1StatusTrx | STATUS_TRX | — | — |
| 137 | TransactionHeader1TermDueDate | TERM_DUE_DATE | — | — |
| 138 | TransactionHeader1TermId | TERM_ID | — | — |
| 139 | TransactionHeader1TerritoryId | TERRITORY_ID | — | — |
| 140 | TransactionHeader1TrxClass | TRX_CLASS | — | — |
| 141 | TransactionHeader1TrxDate | TRX_DATE | — | — |
| 142 | TransactionHeader1TrxNumber | TRX_NUMBER | — | ✅ |
| 143 | TransactionHeader1UpgradeMethod | UPGRADE_METHOD | — | — |
| 144 | TransactionHeader1WaybillNumber | WAYBILL_NUMBER | — | — |
| 145 | TransactionHeader1WhUpdateDate | WH_UPDATE_DATE | — | — |
| 146 | TransactionHeaderAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 147 | TransactionHeaderAgreementId | AGREEMENT_ID | — | — |
| 148 | TransactionHeaderApplicationId | APPLICATION_ID | — | — |
| 149 | TransactionHeaderApprovalCode | APPROVAL_CODE | — | — |
| 150 | TransactionHeaderAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 151 | TransactionHeaderBatchId | BATCH_ID | — | — |
| 152 | TransactionHeaderBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 153 | TransactionHeaderBillTemplateId | BILL_TEMPLATE_ID | — | ✅ |
| 154 | TransactionHeaderBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 155 | TransactionHeaderBillToContactId | BILL_TO_CONTACT_ID | — | ✅ |
| 156 | TransactionHeaderBillToCustomerId | BILL_TO_CUSTOMER_ID | — | ✅ |
| 157 | TransactionHeaderBillToSiteUseId | BILL_TO_SITE_USE_ID | — | ✅ |
| 158 | TransactionHeaderBillingDate | BILLING_DATE | — | — |
| 159 | TransactionHeaderBrAmount | BR_AMOUNT | — | — |
| 160 | TransactionHeaderBrOnHoldFlag | BR_ON_HOLD_FLAG | — | — |
| 161 | TransactionHeaderBrUnpaidFlag | BR_UNPAID_FLAG | — | — |
| 162 | TransactionHeaderCcErrorCode | CC_ERROR_CODE | — | — |
| 163 | TransactionHeaderCcErrorFlag | CC_ERROR_FLAG | — | — |
| 164 | TransactionHeaderCcErrorText | CC_ERROR_TEXT | — | — |
| 165 | TransactionHeaderComments | COMMENTS | — | ✅ |
| 166 | TransactionHeaderCompleteFlag | COMPLETE_FLAG | — | — |
| 167 | TransactionHeaderContractId | CONTRACT_ID | — | — |
| 168 | TransactionHeaderCreatedBy | CREATED_BY | — | — |
| 169 | TransactionHeaderCreatedFrom | CREATED_FROM | — | — |
| 170 | TransactionHeaderCreationDate | CREATION_DATE | — | — |
| 171 | TransactionHeaderCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | — |
| 172 | TransactionHeaderCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | — |
| 173 | TransactionHeaderCtReference | CT_REFERENCE | — | — |
| 174 | TransactionHeaderCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | ✅ |
| 175 | TransactionHeaderCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 176 | TransactionHeaderCustomerReference | CUSTOMER_REFERENCE | — | — |
| 177 | TransactionHeaderCustomerReferenceDate | CUSTOMER_REFERENCE_DATE | — | — |
| 178 | TransactionHeaderCustomerTrxId | CUSTOMER_TRX_ID | — | ✅ |
| 179 | TransactionHeaderDefaultTaxExemptFlag | DEFAULT_TAX_EXEMPT_FLAG | — | — |
| 180 | TransactionHeaderDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 181 | TransactionHeaderDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 182 | TransactionHeaderDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 183 | TransactionHeaderDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 184 | TransactionHeaderDraweeBankAccountId | DRAWEE_BANK_ACCOUNT_ID | — | — |
| 185 | TransactionHeaderDraweeContactId | DRAWEE_CONTACT_ID | — | — |
| 186 | TransactionHeaderDraweeId | DRAWEE_ID | — | — |
| 187 | TransactionHeaderDraweeSiteUseId | DRAWEE_SITE_USE_ID | — | — |
| 188 | TransactionHeaderEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 189 | TransactionHeaderEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 190 | TransactionHeaderEndDateCommitment | END_DATE_COMMITMENT | — | — |
| 191 | TransactionHeaderExchangeDate | EXCHANGE_DATE | — | — |
| 192 | TransactionHeaderExchangeRate | EXCHANGE_RATE | — | — |
| 193 | TransactionHeaderExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 194 | TransactionHeaderFinanceCharges | FINANCE_CHARGES | — | — |
| 195 | TransactionHeaderFobPoint | FOB_POINT | — | — |
| 196 | TransactionHeaderInitialCustomerTrxId | INITIAL_CUSTOMER_TRX_ID | — | — |
| 197 | TransactionHeaderIntercompanyFlag | INTERCOMPANY_FLAG | — | — |
| 198 | TransactionHeaderInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 199 | TransactionHeaderInterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | ✅ |
| 200 | TransactionHeaderInterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | — |
| 201 | TransactionHeaderInterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | — |
| 202 | TransactionHeaderInterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | — |
| 203 | TransactionHeaderInterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | — |
| 204 | TransactionHeaderInterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | — |
| 205 | TransactionHeaderInterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | — |
| 206 | TransactionHeaderInterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | ✅ |
| 207 | TransactionHeaderInterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | — |
| 208 | TransactionHeaderInterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | — |
| 209 | TransactionHeaderInterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | — |
| 210 | TransactionHeaderInterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | — |
| 211 | TransactionHeaderInterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | — |
| 212 | TransactionHeaderInterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | — |
| 213 | TransactionHeaderInterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | — |
| 214 | TransactionHeaderInterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | ✅ |
| 215 | TransactionHeaderInternalNotes | INTERNAL_NOTES | — | — |
| 216 | TransactionHeaderInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 217 | TransactionHeaderInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 218 | TransactionHeaderLastPrintedSequenceNum | LAST_PRINTED_SEQUENCE_NUM | — | — |
| 219 | TransactionHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 220 | TransactionHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 221 | TransactionHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 222 | TransactionHeaderLateChargesAssessed | LATE_CHARGES_ASSESSED | — | — |
| 223 | TransactionHeaderLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 224 | TransactionHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 225 | TransactionHeaderOldTrxNumber | OLD_TRX_NUMBER | — | — |
| 226 | TransactionHeaderOrgId | ORG_ID | — | — |
| 227 | TransactionHeaderOrigSystemBatchName | ORIG_SYSTEM_BATCH_NAME | — | — |
| 228 | TransactionHeaderOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 229 | TransactionHeaderPayingCustomerId | PAYING_CUSTOMER_ID | — | — |
| 230 | TransactionHeaderPayingSiteUseId | PAYING_SITE_USE_ID | — | ✅ |
| 231 | TransactionHeaderPaymentAttributes | PAYMENT_ATTRIBUTES | — | — |
| 232 | TransactionHeaderPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 233 | TransactionHeaderPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 234 | TransactionHeaderPostRequestId | POST_REQUEST_ID | — | — |
| 235 | TransactionHeaderPostingControlId | POSTING_CONTROL_ID | — | — |
| 236 | TransactionHeaderPrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 237 | TransactionHeaderPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 238 | TransactionHeaderPrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | ✅ |
| 239 | TransactionHeaderPrintingCount | PRINTING_COUNT | — | — |
| 240 | TransactionHeaderPrintingLastPrinted | PRINTING_LAST_PRINTED | — | — |
| 241 | TransactionHeaderPrintingOption | PRINTING_OPTION | — | — |
| 242 | TransactionHeaderPrintingOriginalDate | PRINTING_ORIGINAL_DATE | — | — |
| 243 | TransactionHeaderPrintingPending | PRINTING_PENDING | — | — |
| 244 | TransactionHeaderProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 245 | TransactionHeaderProgramId | PROGRAM_ID | — | — |
| 246 | TransactionHeaderProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 247 | TransactionHeaderPurchaseOrder | PURCHASE_ORDER | — | ✅ |
| 248 | TransactionHeaderPurchaseOrderDate | PURCHASE_ORDER_DATE | — | — |
| 249 | TransactionHeaderPurchaseOrderRevision | PURCHASE_ORDER_REVISION | — | — |
| 250 | TransactionHeaderRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 251 | TransactionHeaderReasonCode | REASON_CODE | — | — |
| 252 | TransactionHeaderReceiptMethodId | RECEIPT_METHOD_ID | — | ✅ |
| 253 | TransactionHeaderRecurredFromTrxNumber | RECURRED_FROM_TRX_NUMBER | — | — |
| 254 | TransactionHeaderRelatedBatchSourceSeqId | RELATED_BATCH_SOURCE_SEQ_ID | — | — |
| 255 | TransactionHeaderRelatedCustomerTrxId | RELATED_CUSTOMER_TRX_ID | — | — |
| 256 | TransactionHeaderRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 257 | TransactionHeaderRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 258 | TransactionHeaderRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 259 | TransactionHeaderRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 260 | TransactionHeaderRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 261 | TransactionHeaderRequestId | REQUEST_ID | — | — |
| 262 | TransactionHeaderReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 263 | TransactionHeaderSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 264 | TransactionHeaderShipDateActual | SHIP_DATE_ACTUAL | — | — |
| 265 | TransactionHeaderShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 266 | TransactionHeaderShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 267 | TransactionHeaderShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 268 | TransactionHeaderShipToPartyId | SHIP_TO_PARTY_ID | — | — |
| 269 | TransactionHeaderShipToPartySiteUseId | SHIP_TO_PARTY_SITE_USE_ID | — | ✅ |
| 270 | TransactionHeaderShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | ✅ |
| 271 | TransactionHeaderShipVia | SHIP_VIA | — | — |
| 272 | TransactionHeaderShipmentId | SHIPMENT_ID | — | — |
| 273 | TransactionHeaderSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 274 | TransactionHeaderSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 275 | TransactionHeaderSoldToPartyId | SOLD_TO_PARTY_ID | — | — |
| 276 | TransactionHeaderSoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | ✅ |
| 277 | TransactionHeaderSourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 278 | TransactionHeaderSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 279 | TransactionHeaderSpecialInstructions | SPECIAL_INSTRUCTIONS | — | ✅ |
| 280 | TransactionHeaderStartDateCommitment | START_DATE_COMMITMENT | — | — |
| 281 | TransactionHeaderStatusTrx | STATUS_TRX | — | — |
| 282 | TransactionHeaderTermDueDate | TERM_DUE_DATE | — | — |
| 283 | TransactionHeaderTermId | TERM_ID | — | ✅ |
| 284 | TransactionHeaderTerritoryId | TERRITORY_ID | — | — |
| 285 | TransactionHeaderTrxClass | TRX_CLASS | — | — |
| 286 | TransactionHeaderTrxDate | TRX_DATE | — | ✅ |
| 287 | TransactionHeaderTrxNumber | TRX_NUMBER | — | ✅ |
| 288 | TransactionHeaderUpgradeMethod | UPGRADE_METHOD | — | — |
| 289 | TransactionHeaderWaybillNumber | WAYBILL_NUMBER | — | — |
| 290 | TransactionHeaderWhUpdateDate | WH_UPDATE_DATE | — | — |
| 291 | TrxHeaderBillingDate | BILLING_DATE | — | ✅ |
| 292 | TrxHeaderComments | COMMENTS | — | — |
| 293 | TrxHeaderCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | ✅ |
| 294 | TrxHeaderCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | ✅ |
| 295 | TrxHeaderCustomerReference | CUSTOMER_REFERENCE | — | ✅ |
| 296 | TrxHeaderCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 297 | TrxHeaderDocSequenceValue | DOC_SEQUENCE_VALUE | — | ✅ |
| 298 | TrxHeaderFinanceCharges | FINANCE_CHARGES | — | ✅ |
| 299 | TrxHeaderIntercompanyFlag | INTERCOMPANY_FLAG | — | ✅ |
| 300 | TrxHeaderObjectVersionNumber10 | OBJECT_VERSION_NUMBER | — | — |
| 301 | TrxHeaderObjectVersionNumber7 | OBJECT_VERSION_NUMBER | — | — |
| 302 | TrxHeaderPrevAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 303 | TrxHeaderPrevAgreementId | AGREEMENT_ID | — | — |
| 304 | TrxHeaderPrevApplicationId | APPLICATION_ID | — | — |
| 305 | TrxHeaderPrevApprovalCode | APPROVAL_CODE | — | — |
| 306 | TrxHeaderPrevAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 307 | TrxHeaderPrevBatchId | BATCH_ID | — | — |
| 308 | TrxHeaderPrevBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 309 | TrxHeaderPrevBillTemplateId | BILL_TEMPLATE_ID | — | — |
| 310 | TrxHeaderPrevBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 311 | TrxHeaderPrevBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 312 | TrxHeaderPrevBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 313 | TrxHeaderPrevBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 314 | TrxHeaderPrevBillingDate | BILLING_DATE | — | — |
| 315 | TrxHeaderPrevBrAmount | BR_AMOUNT | — | — |
| 316 | TrxHeaderPrevBrOnHoldFlag | BR_ON_HOLD_FLAG | — | — |
| 317 | TrxHeaderPrevBrUnpaidFlag | BR_UNPAID_FLAG | — | — |
| 318 | TrxHeaderPrevCcErrorCode | CC_ERROR_CODE | — | — |
| 319 | TrxHeaderPrevCcErrorFlag | CC_ERROR_FLAG | — | — |
| 320 | TrxHeaderPrevCcErrorText | CC_ERROR_TEXT | — | — |
| 321 | TrxHeaderPrevComments | COMMENTS | — | — |
| 322 | TrxHeaderPrevCompleteFlag | COMPLETE_FLAG | — | — |
| 323 | TrxHeaderPrevContractId | CONTRACT_ID | — | — |
| 324 | TrxHeaderPrevCreatedBy | CREATED_BY | — | — |
| 325 | TrxHeaderPrevCreatedFrom | CREATED_FROM | — | — |
| 326 | TrxHeaderPrevCreationDate | CREATION_DATE | — | — |
| 327 | TrxHeaderPrevCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | — |
| 328 | TrxHeaderPrevCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | — |
| 329 | TrxHeaderPrevCtReference | CT_REFERENCE | — | — |
| 330 | TrxHeaderPrevCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 331 | TrxHeaderPrevCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 332 | TrxHeaderPrevCustomerReference | CUSTOMER_REFERENCE | — | — |
| 333 | TrxHeaderPrevCustomerReferenceDate | CUSTOMER_REFERENCE_DATE | — | — |
| 334 | TrxHeaderPrevCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 335 | TrxHeaderPrevDefaultTaxExemptFlag | DEFAULT_TAX_EXEMPT_FLAG | — | — |
| 336 | TrxHeaderPrevDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 337 | TrxHeaderPrevDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 338 | TrxHeaderPrevDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 339 | TrxHeaderPrevDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 340 | TrxHeaderPrevDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 341 | TrxHeaderPrevDocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 342 | TrxHeaderPrevDraweeBankAccountId | DRAWEE_BANK_ACCOUNT_ID | — | — |
| 343 | TrxHeaderPrevDraweeContactId | DRAWEE_CONTACT_ID | — | — |
| 344 | TrxHeaderPrevDraweeId | DRAWEE_ID | — | — |
| 345 | TrxHeaderPrevDraweeSiteUseId | DRAWEE_SITE_USE_ID | — | — |
| 346 | TrxHeaderPrevEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 347 | TrxHeaderPrevEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 348 | TrxHeaderPrevEndDateCommitment | END_DATE_COMMITMENT | — | — |
| 349 | TrxHeaderPrevExchangeDate | EXCHANGE_DATE | — | — |
| 350 | TrxHeaderPrevExchangeRate | EXCHANGE_RATE | — | — |
| 351 | TrxHeaderPrevExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 352 | TrxHeaderPrevFinanceCharges | FINANCE_CHARGES | — | — |
| 353 | TrxHeaderPrevFobPoint | FOB_POINT | — | — |
| 354 | TrxHeaderPrevInitialCustomerTrxId | INITIAL_CUSTOMER_TRX_ID | — | — |
| 355 | TrxHeaderPrevIntercompanyFlag | INTERCOMPANY_FLAG | — | — |
| 356 | TrxHeaderPrevInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 357 | TrxHeaderPrevInterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | — |
| 358 | TrxHeaderPrevInterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | — |
| 359 | TrxHeaderPrevInterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | — |
| 360 | TrxHeaderPrevInterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | — |
| 361 | TrxHeaderPrevInterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | — |
| 362 | TrxHeaderPrevInterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | — |
| 363 | TrxHeaderPrevInterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | — |
| 364 | TrxHeaderPrevInterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | — |
| 365 | TrxHeaderPrevInterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | — |
| 366 | TrxHeaderPrevInterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | — |
| 367 | TrxHeaderPrevInterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | — |
| 368 | TrxHeaderPrevInterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | — |
| 369 | TrxHeaderPrevInterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | — |
| 370 | TrxHeaderPrevInterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | — |
| 371 | TrxHeaderPrevInterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | — |
| 372 | TrxHeaderPrevInterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | — |
| 373 | TrxHeaderPrevInternalNotes | INTERNAL_NOTES | — | — |
| 374 | TrxHeaderPrevInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 375 | TrxHeaderPrevInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 376 | TrxHeaderPrevLastPrintedSequenceNum | LAST_PRINTED_SEQUENCE_NUM | — | — |
| 377 | TrxHeaderPrevLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 378 | TrxHeaderPrevLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 379 | TrxHeaderPrevLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 380 | TrxHeaderPrevLateChargesAssessed | LATE_CHARGES_ASSESSED | — | — |
| 381 | TrxHeaderPrevLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 382 | TrxHeaderPrevObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 383 | TrxHeaderPrevOldTrxNumber | OLD_TRX_NUMBER | — | — |
| 384 | TrxHeaderPrevOrgId | ORG_ID | — | — |
| 385 | TrxHeaderPrevOrigSystemBatchName | ORIG_SYSTEM_BATCH_NAME | — | — |
| 386 | TrxHeaderPrevOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 387 | TrxHeaderPrevPayingCustomerId | PAYING_CUSTOMER_ID | — | — |
| 388 | TrxHeaderPrevPayingSiteUseId | PAYING_SITE_USE_ID | — | — |
| 389 | TrxHeaderPrevPaymentAttributes | PAYMENT_ATTRIBUTES | — | — |
| 390 | TrxHeaderPrevPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 391 | TrxHeaderPrevPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 392 | TrxHeaderPrevPostRequestId | POST_REQUEST_ID | — | — |
| 393 | TrxHeaderPrevPostingControlId | POSTING_CONTROL_ID | — | — |
| 394 | TrxHeaderPrevPrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 395 | TrxHeaderPrevPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 396 | TrxHeaderPrevPrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | — |
| 397 | TrxHeaderPrevPrintingCount | PRINTING_COUNT | — | — |
| 398 | TrxHeaderPrevPrintingLastPrinted | PRINTING_LAST_PRINTED | — | — |
| 399 | TrxHeaderPrevPrintingOption | PRINTING_OPTION | — | — |
| 400 | TrxHeaderPrevPrintingOriginalDate | PRINTING_ORIGINAL_DATE | — | — |
| 401 | TrxHeaderPrevPrintingPending | PRINTING_PENDING | — | — |
| 402 | TrxHeaderPrevProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 403 | TrxHeaderPrevProgramId | PROGRAM_ID | — | — |
| 404 | TrxHeaderPrevProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 405 | TrxHeaderPrevPurchaseOrder | PURCHASE_ORDER | — | — |
| 406 | TrxHeaderPrevPurchaseOrderDate | PURCHASE_ORDER_DATE | — | — |
| 407 | TrxHeaderPrevPurchaseOrderRevision | PURCHASE_ORDER_REVISION | — | — |
| 408 | TrxHeaderPrevRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 409 | TrxHeaderPrevReasonCode | REASON_CODE | — | — |
| 410 | TrxHeaderPrevReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 411 | TrxHeaderPrevRecurredFromTrxNumber | RECURRED_FROM_TRX_NUMBER | — | — |
| 412 | TrxHeaderPrevRelatedBatchSourceSeqId | RELATED_BATCH_SOURCE_SEQ_ID | — | — |
| 413 | TrxHeaderPrevRelatedCustomerTrxId | RELATED_CUSTOMER_TRX_ID | — | — |
| 414 | TrxHeaderPrevRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 415 | TrxHeaderPrevRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 416 | TrxHeaderPrevRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 417 | TrxHeaderPrevRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 418 | TrxHeaderPrevRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 419 | TrxHeaderPrevRequestId | REQUEST_ID | — | — |
| 420 | TrxHeaderPrevRequiresManualScheduling | REQUIRES_MANUAL_SCHEDULING | — | — |
| 421 | TrxHeaderPrevReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 422 | TrxHeaderPrevSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 423 | TrxHeaderPrevShipDateActual | SHIP_DATE_ACTUAL | — | — |
| 424 | TrxHeaderPrevShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 425 | TrxHeaderPrevShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 426 | TrxHeaderPrevShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 427 | TrxHeaderPrevShipToPartyId | SHIP_TO_PARTY_ID | — | — |
| 428 | TrxHeaderPrevShipToPartySiteUseId | SHIP_TO_PARTY_SITE_USE_ID | — | — |
| 429 | TrxHeaderPrevShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 430 | TrxHeaderPrevShipVia | SHIP_VIA | — | — |
| 431 | TrxHeaderPrevShipmentId | SHIPMENT_ID | — | — |
| 432 | TrxHeaderPrevSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 433 | TrxHeaderPrevSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 434 | TrxHeaderPrevSoldToPartyId | SOLD_TO_PARTY_ID | — | — |
| 435 | TrxHeaderPrevSoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | — |
| 436 | TrxHeaderPrevSourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 437 | TrxHeaderPrevSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 438 | TrxHeaderPrevSpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 439 | TrxHeaderPrevStartDateCommitment | START_DATE_COMMITMENT | — | — |
| 440 | TrxHeaderPrevStatusTrx | STATUS_TRX | — | — |
| 441 | TrxHeaderPrevTermDueDate | TERM_DUE_DATE | — | — |
| 442 | TrxHeaderPrevTermId | TERM_ID | — | — |
| 443 | TrxHeaderPrevTerritoryId | TERRITORY_ID | — | — |
| 444 | TrxHeaderPrevTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 445 | TrxHeaderPrevTrxClass | TRX_CLASS | — | — |
| 446 | TrxHeaderPrevTrxDate | TRX_DATE | — | — |
| 447 | TrxHeaderPrevTrxNumber | TRX_NUMBER | — | — |
| 448 | TrxHeaderPrevUpgradeMethod | UPGRADE_METHOD | — | — |
| 449 | TrxHeaderPrevUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 450 | TrxHeaderPrevWaybillNumber | WAYBILL_NUMBER | — | — |
| 451 | TrxHeaderPrevWhUpdateDate | WH_UPDATE_DATE | — | — |
| 452 | TrxHeaderShipToPartyId | SHIP_TO_PARTY_ID | — | — |
| 453 | TrxHeaderShipToPartySiteUseId | SHIP_TO_PARTY_SITE_USE_ID | — | — |
| 454 | TrxHeaderSoldToPartyId | SOLD_TO_PARTY_ID | — | — |
| 455 | TrxHeaderSpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 456 | TrxnHdrComments | COMMENTS | — | — |
| 457 | TrxnHdrCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 458 | TrxnHdrShipToPartyId | SHIP_TO_PARTY_ID | — | — |
| 459 | TrxnHdrShipToPartySiteUseId | SHIP_TO_PARTY_SITE_USE_ID | — | — |
| 460 | TrxnHdrSoldToPartyId | SOLD_TO_PARTY_ID | — | — |
| 461 | TrxnHdrSpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 462 | TrxnHdrTrxNumber | TRX_NUMBER | — | ✅ |

### [[ra_customer_trx_lines_all|RA_CUSTOMER_TRX_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 2 | ObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 3 | ObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |
| 4 | TransactionLineAccountingRuleDuration | ACCOUNTING_RULE_DURATION | — | — |
| 5 | TransactionLineAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 6 | TransactionLineAcctdAmountDueOriginal | ACCTD_AMOUNT_DUE_ORIGINAL | — | — |
| 7 | TransactionLineAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | — |
| 8 | TransactionLineAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 9 | TransactionLineAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 10 | TransactionLineAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 11 | TransactionLineAssessableValue | ASSESSABLE_VALUE | — | — |
| 12 | TransactionLineAutoruleCompleteFlag | AUTORULE_COMPLETE_FLAG | — | — |
| 13 | TransactionLineAutoruleDurationProcessed | AUTORULE_DURATION_PROCESSED | — | — |
| 14 | TransactionLineAutotax | AUTOTAX | — | — |
| 15 | TransactionLineBrAdjustmentId | BR_ADJUSTMENT_ID | — | — |
| 16 | TransactionLineBrRefCustomerTrxId | BR_REF_CUSTOMER_TRX_ID | — | — |
| 17 | TransactionLineBrRefPaymentScheduleId | BR_REF_PAYMENT_SCHEDULE_ID | — | — |
| 18 | TransactionLineChrgAcctdAmountRemaining | CHRG_ACCTD_AMOUNT_REMAINING | — | — |
| 19 | TransactionLineChrgAmountRemaining | CHRG_AMOUNT_REMAINING | — | — |
| 20 | TransactionLineContractLineId | CONTRACT_LINE_ID | — | — |
| 21 | TransactionLineCreatedBy | CREATED_BY | — | — |
| 22 | TransactionLineCreationDate | CREATION_DATE | — | — |
| 23 | TransactionLineCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 24 | TransactionLineCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 25 | TransactionLineDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 26 | TransactionLineDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 27 | TransactionLineDeferralExclusionFlag | DEFERRAL_EXCLUSION_FLAG | — | — |
| 28 | TransactionLineDescription | DESCRIPTION | — | — |
| 29 | TransactionLineExtendedAcctdAmount | EXTENDED_ACCTD_AMOUNT | — | — |
| 30 | TransactionLineExtendedAmount | EXTENDED_AMOUNT | — | — |
| 31 | TransactionLineFairMarketValueAmount | FAIR_MARKET_VALUE_AMOUNT | — | — |
| 32 | TransactionLineFrtAdjAcctdRemaining | FRT_ADJ_ACCTD_REMAINING | — | — |
| 33 | TransactionLineFrtAdjRemaining | FRT_ADJ_REMAINING | — | — |
| 34 | TransactionLineFrtEdAcctdAmount | FRT_ED_ACCTD_AMOUNT | — | — |
| 35 | TransactionLineFrtEdAmount | FRT_ED_AMOUNT | — | — |
| 36 | TransactionLineFrtUnedAcctdAmount | FRT_UNED_ACCTD_AMOUNT | — | — |
| 37 | TransactionLineFrtUnedAmount | FRT_UNED_AMOUNT | — | — |
| 38 | TransactionLineGrossExtendedAmount | GROSS_EXTENDED_AMOUNT | — | — |
| 39 | TransactionLineGrossUnitSellingPrice | GROSS_UNIT_SELLING_PRICE | — | — |
| 40 | TransactionLineHistoricalFlag | HISTORICAL_FLAG | — | — |
| 41 | TransactionLineInitialCustomerTrxLineId | INITIAL_CUSTOMER_TRX_LINE_ID | — | — |
| 42 | TransactionLineInterestLineId | INTEREST_LINE_ID | — | — |
| 43 | TransactionLineInterfaceLineAttribute1 | INTERFACE_LINE_ATTRIBUTE1 | — | — |
| 44 | TransactionLineInterfaceLineAttribute10 | INTERFACE_LINE_ATTRIBUTE10 | — | — |
| 45 | TransactionLineInterfaceLineAttribute11 | INTERFACE_LINE_ATTRIBUTE11 | — | — |
| 46 | TransactionLineInterfaceLineAttribute12 | INTERFACE_LINE_ATTRIBUTE12 | — | — |
| 47 | TransactionLineInterfaceLineAttribute13 | INTERFACE_LINE_ATTRIBUTE13 | — | — |
| 48 | TransactionLineInterfaceLineAttribute14 | INTERFACE_LINE_ATTRIBUTE14 | — | — |
| 49 | TransactionLineInterfaceLineAttribute15 | INTERFACE_LINE_ATTRIBUTE15 | — | — |
| 50 | TransactionLineInterfaceLineAttribute2 | INTERFACE_LINE_ATTRIBUTE2 | — | — |
| 51 | TransactionLineInterfaceLineAttribute3 | INTERFACE_LINE_ATTRIBUTE3 | — | — |
| 52 | TransactionLineInterfaceLineAttribute4 | INTERFACE_LINE_ATTRIBUTE4 | — | — |
| 53 | TransactionLineInterfaceLineAttribute5 | INTERFACE_LINE_ATTRIBUTE5 | — | — |
| 54 | TransactionLineInterfaceLineAttribute6 | INTERFACE_LINE_ATTRIBUTE6 | — | — |
| 55 | TransactionLineInterfaceLineAttribute7 | INTERFACE_LINE_ATTRIBUTE7 | — | — |
| 56 | TransactionLineInterfaceLineAttribute8 | INTERFACE_LINE_ATTRIBUTE8 | — | — |
| 57 | TransactionLineInterfaceLineAttribute9 | INTERFACE_LINE_ATTRIBUTE9 | — | — |
| 58 | TransactionLineInterfaceLineContext | INTERFACE_LINE_CONTEXT | — | — |
| 59 | TransactionLineInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 60 | TransactionLineInvoicedLineAcctgLevel | INVOICED_LINE_ACCTG_LEVEL | — | — |
| 61 | TransactionLineItemContext | ITEM_CONTEXT | — | — |
| 62 | TransactionLineItemExceptionRateId | ITEM_EXCEPTION_RATE_ID | — | — |
| 63 | TransactionLineLastPeriodToCredit | LAST_PERIOD_TO_CREDIT | — | — |
| 64 | TransactionLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 65 | TransactionLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 66 | TransactionLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 67 | TransactionLineLineIntendedUse | LINE_INTENDED_USE | — | — |
| 68 | TransactionLineLineNumber | LINE_NUMBER | — | — |
| 69 | TransactionLineLineRecoverable | LINE_RECOVERABLE | — | — |
| 70 | TransactionLineLineType | LINE_TYPE | — | — |
| 71 | TransactionLineLinkToCustTrxLineId | LINK_TO_CUST_TRX_LINE_ID | — | — |
| 72 | TransactionLineLinkToParentlineAttribute1 | LINK_TO_PARENTLINE_ATTRIBUTE1 | — | — |
| 73 | TransactionLineLinkToParentlineAttribute10 | LINK_TO_PARENTLINE_ATTRIBUTE10 | — | — |
| 74 | TransactionLineLinkToParentlineAttribute11 | LINK_TO_PARENTLINE_ATTRIBUTE11 | — | — |
| 75 | TransactionLineLinkToParentlineAttribute12 | LINK_TO_PARENTLINE_ATTRIBUTE12 | — | — |
| 76 | TransactionLineLinkToParentlineAttribute13 | LINK_TO_PARENTLINE_ATTRIBUTE13 | — | — |
| 77 | TransactionLineLinkToParentlineAttribute14 | LINK_TO_PARENTLINE_ATTRIBUTE14 | — | — |
| 78 | TransactionLineLinkToParentlineAttribute15 | LINK_TO_PARENTLINE_ATTRIBUTE15 | — | — |
| 79 | TransactionLineLinkToParentlineAttribute2 | LINK_TO_PARENTLINE_ATTRIBUTE2 | — | — |
| 80 | TransactionLineLinkToParentlineAttribute3 | LINK_TO_PARENTLINE_ATTRIBUTE3 | — | — |
| 81 | TransactionLineLinkToParentlineAttribute4 | LINK_TO_PARENTLINE_ATTRIBUTE4 | — | — |
| 82 | TransactionLineLinkToParentlineAttribute5 | LINK_TO_PARENTLINE_ATTRIBUTE5 | — | — |
| 83 | TransactionLineLinkToParentlineAttribute6 | LINK_TO_PARENTLINE_ATTRIBUTE6 | — | — |
| 84 | TransactionLineLinkToParentlineAttribute7 | LINK_TO_PARENTLINE_ATTRIBUTE7 | — | — |
| 85 | TransactionLineLinkToParentlineAttribute8 | LINK_TO_PARENTLINE_ATTRIBUTE8 | — | — |
| 86 | TransactionLineLinkToParentlineAttribute9 | LINK_TO_PARENTLINE_ATTRIBUTE9 | — | — |
| 87 | TransactionLineLinkToParentlineContext | LINK_TO_PARENTLINE_CONTEXT | — | — |
| 88 | TransactionLineLocationSegmentId | LOCATION_SEGMENT_ID | — | — |
| 89 | TransactionLineMemoLineSeqId | MEMO_LINE_SEQ_ID | — | — |
| 90 | TransactionLineMovementId | MOVEMENT_ID | — | — |
| 91 | TransactionLineMrcExtendedAcctdAmount | MRC_EXTENDED_ACCTD_AMOUNT | — | — |
| 92 | TransactionLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 93 | TransactionLineOrgId | ORG_ID | — | — |
| 94 | TransactionLineOverrideAutoAccountingFlag | OVERRIDE_AUTO_ACCOUNTING_FLAG | — | — |
| 95 | TransactionLinePaymentSetId | PAYMENT_SET_ID | — | — |
| 96 | TransactionLinePaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 97 | TransactionLinePreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 98 | TransactionLinePreviousCustomerTrxLineId | PREVIOUS_CUSTOMER_TRX_LINE_ID | — | — |
| 99 | TransactionLineProductCategory | PRODUCT_CATEGORY | — | — |
| 100 | TransactionLineProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | — |
| 101 | TransactionLineProductType | PRODUCT_TYPE | — | — |
| 102 | TransactionLineProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 103 | TransactionLineProgramId | PROGRAM_ID | — | — |
| 104 | TransactionLineProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 105 | TransactionLineQuantityCredited | QUANTITY_CREDITED | — | — |
| 106 | TransactionLineQuantityInvoiced | QUANTITY_INVOICED | — | — |
| 107 | TransactionLineQuantityOrdered | QUANTITY_ORDERED | — | — |
| 108 | TransactionLineReasonCode | REASON_CODE | — | — |
| 109 | TransactionLineRequestId | REQUEST_ID | — | — |
| 110 | TransactionLineRevenueAmount | REVENUE_AMOUNT | — | — |
| 111 | TransactionLineRuleEndDate | RULE_END_DATE | — | — |
| 112 | TransactionLineRuleStartDate | RULE_START_DATE | — | — |
| 113 | TransactionLineSalesOrder | SALES_ORDER | — | — |
| 114 | TransactionLineSalesOrderDate | SALES_ORDER_DATE | — | — |
| 115 | TransactionLineSalesOrderLine | SALES_ORDER_LINE | — | — |
| 116 | TransactionLineSalesOrderRevision | SALES_ORDER_REVISION | — | — |
| 117 | TransactionLineSalesOrderSource | SALES_ORDER_SOURCE | — | — |
| 118 | TransactionLineSalesTaxId | SALES_TAX_ID | — | — |
| 119 | TransactionLineSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 120 | TransactionLineShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 121 | TransactionLineShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 122 | TransactionLineShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 123 | TransactionLineShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 124 | TransactionLineSourceDataKey1 | SOURCE_DATA_KEY1 | — | — |
| 125 | TransactionLineSourceDataKey2 | SOURCE_DATA_KEY2 | — | — |
| 126 | TransactionLineSourceDataKey3 | SOURCE_DATA_KEY3 | — | — |
| 127 | TransactionLineSourceDataKey4 | SOURCE_DATA_KEY4 | — | — |
| 128 | TransactionLineSourceDataKey5 | SOURCE_DATA_KEY5 | — | — |
| 129 | TransactionLineSourceDocumentLineId | SOURCE_DOCUMENT_LINE_ID | — | — |
| 130 | TransactionLineSourceDocumentLineNumber | SOURCE_DOCUMENT_LINE_NUMBER | — | — |
| 131 | TransactionLineTaxAction | TAX_ACTION | — | — |
| 132 | TransactionLineTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 133 | TransactionLineTaxExemptFlag | TAX_EXEMPT_FLAG | — | — |
| 134 | TransactionLineTaxExemptNumber | TAX_EXEMPT_NUMBER | — | — |
| 135 | TransactionLineTaxExemptReasonCode | TAX_EXEMPT_REASON_CODE | — | — |
| 136 | TransactionLineTaxExemptionId | TAX_EXEMPTION_ID | — | — |
| 137 | TransactionLineTaxLineId | TAX_LINE_ID | — | — |
| 138 | TransactionLineTaxPrecedence | TAX_PRECEDENCE | — | — |
| 139 | TransactionLineTaxRate | TAX_RATE | — | — |
| 140 | TransactionLineTaxRecoverable | TAX_RECOVERABLE | — | — |
| 141 | TransactionLineTaxVendorReturnCode | TAX_VENDOR_RETURN_CODE | — | — |
| 142 | TransactionLineTaxableAmount | TAXABLE_AMOUNT | — | — |
| 143 | TransactionLineTaxableFlag | TAXABLE_FLAG | — | — |
| 144 | TransactionLineTranslatedDescription | TRANSLATED_DESCRIPTION | — | — |
| 145 | TransactionLineTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 146 | TransactionLineUnitSellingPrice | UNIT_SELLING_PRICE | — | — |
| 147 | TransactionLineUnitStandardPrice | UNIT_STANDARD_PRICE | — | — |
| 148 | TransactionLineUomCode | UOM_CODE | — | — |
| 149 | TransactionLineUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 150 | TransactionLineVatTaxId | VAT_TAX_ID | — | — |
| 151 | TransactionLineWarehouseId | WAREHOUSE_ID | — | — |
| 152 | TransactionLineWhUpdateDate | WH_UPDATE_DATE | — | — |
| 153 | TrxLineRefCustAccountingRuleDuration | ACCOUNTING_RULE_DURATION | — | — |
| 154 | TrxLineRefCustAcctdAmountDueOriginal | ACCTD_AMOUNT_DUE_ORIGINAL | — | — |
| 155 | TrxLineRefCustAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | — |
| 156 | TrxLineRefCustAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 157 | TrxLineRefCustAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 158 | TrxLineRefCustAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 159 | TrxLineRefCustAssessableValue | ASSESSABLE_VALUE | — | — |
| 160 | TrxLineRefCustAutoruleCompleteFlag | AUTORULE_COMPLETE_FLAG | — | — |
| 161 | TrxLineRefCustAutoruleDurationProcessed | AUTORULE_DURATION_PROCESSED | — | — |
| 162 | TrxLineRefCustAutotax | AUTOTAX | — | — |
| 163 | TrxLineRefCustChrgAcctdAmountRemaining | CHRG_ACCTD_AMOUNT_REMAINING | — | — |
| 164 | TrxLineRefCustChrgAmountRemaining | CHRG_AMOUNT_REMAINING | — | — |
| 165 | TrxLineRefCustCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 166 | TrxLineRefCustDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 167 | TrxLineRefCustDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 168 | TrxLineRefCustDeferralExclusionFlag | DEFERRAL_EXCLUSION_FLAG | — | — |
| 169 | TrxLineRefCustDescription | DESCRIPTION | — | — |
| 170 | TrxLineRefCustExtendedAcctdAmount | EXTENDED_ACCTD_AMOUNT | — | — |
| 171 | TrxLineRefCustExtendedAmount | EXTENDED_AMOUNT | — | — |
| 172 | TrxLineRefCustFairMarketValueAmount | FAIR_MARKET_VALUE_AMOUNT | — | — |
| 173 | TrxLineRefCustFrtAdjAcctdRemaining | FRT_ADJ_ACCTD_REMAINING | — | — |
| 174 | TrxLineRefCustFrtAdjRemaining | FRT_ADJ_REMAINING | — | — |
| 175 | TrxLineRefCustFrtEdAcctdAmount | FRT_ED_ACCTD_AMOUNT | — | — |
| 176 | TrxLineRefCustFrtEdAmount | FRT_ED_AMOUNT | — | — |
| 177 | TrxLineRefCustFrtUnedAcctdAmount | FRT_UNED_ACCTD_AMOUNT | — | — |
| 178 | TrxLineRefCustFrtUnedAmount | FRT_UNED_AMOUNT | — | — |
| 179 | TrxLineRefCustGrossExtendedAmount | GROSS_EXTENDED_AMOUNT | — | — |
| 180 | TrxLineRefCustGrossUnitSellingPrice | GROSS_UNIT_SELLING_PRICE | — | — |
| 181 | TrxLineRefCustHistoricalFlag | HISTORICAL_FLAG | — | — |
| 182 | TrxLineRefCustInvoicedLineAcctgLevel | INVOICED_LINE_ACCTG_LEVEL | — | — |
| 183 | TrxLineRefCustItemContext | ITEM_CONTEXT | — | — |
| 184 | TrxLineRefCustLastPeriodToCredit | LAST_PERIOD_TO_CREDIT | — | — |
| 185 | TrxLineRefCustLineIntendedUse | LINE_INTENDED_USE | — | — |
| 186 | TrxLineRefCustLineNumber | LINE_NUMBER | — | — |
| 187 | TrxLineRefCustLineRecoverable | LINE_RECOVERABLE | — | — |
| 188 | TrxLineRefCustLineType | LINE_TYPE | — | — |
| 189 | TrxLineRefCustMrcExtendedAcctdAmount | MRC_EXTENDED_ACCTD_AMOUNT | — | — |
| 190 | TrxLineRefCustOverrideAutoAccountingFlag | OVERRIDE_AUTO_ACCOUNTING_FLAG | — | — |
| 191 | TrxLineRefCustProductCategory | PRODUCT_CATEGORY | — | — |
| 192 | TrxLineRefCustProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | — |
| 193 | TrxLineRefCustProductType | PRODUCT_TYPE | — | — |
| 194 | TrxLineRefCustProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 195 | TrxLineRefCustQuantityCredited | QUANTITY_CREDITED | — | — |
| 196 | TrxLineRefCustQuantityInvoiced | QUANTITY_INVOICED | — | — |
| 197 | TrxLineRefCustQuantityOrdered | QUANTITY_ORDERED | — | — |
| 198 | TrxLineRefCustReasonCode | REASON_CODE | — | — |
| 199 | TrxLineRefCustRevenueAmount | REVENUE_AMOUNT | — | — |
| 200 | TrxLineRefCustRuleEndDate | RULE_END_DATE | — | — |
| 201 | TrxLineRefCustRuleStartDate | RULE_START_DATE | — | — |
| 202 | TrxLineRefCustSalesOrder | SALES_ORDER | — | — |
| 203 | TrxLineRefCustSalesOrderDate | SALES_ORDER_DATE | — | — |
| 204 | TrxLineRefCustSalesOrderLine | SALES_ORDER_LINE | — | — |
| 205 | TrxLineRefCustSalesOrderRevision | SALES_ORDER_REVISION | — | — |
| 206 | TrxLineRefCustSalesOrderSource | SALES_ORDER_SOURCE | — | — |
| 207 | TrxLineRefCustSourceDocumentLineNumber | SOURCE_DOCUMENT_LINE_NUMBER | — | — |
| 208 | TrxLineRefCustTaxAction | TAX_ACTION | — | — |
| 209 | TrxLineRefCustTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 210 | TrxLineRefCustTaxExemptFlag | TAX_EXEMPT_FLAG | — | — |
| 211 | TrxLineRefCustTaxExemptNumber | TAX_EXEMPT_NUMBER | — | — |
| 212 | TrxLineRefCustTaxExemptReasonCode | TAX_EXEMPT_REASON_CODE | — | — |
| 213 | TrxLineRefCustTaxPrecedence | TAX_PRECEDENCE | — | — |
| 214 | TrxLineRefCustTaxRate | TAX_RATE | — | — |
| 215 | TrxLineRefCustTaxRecoverable | TAX_RECOVERABLE | — | — |
| 216 | TrxLineRefCustTaxVendorReturnCode | TAX_VENDOR_RETURN_CODE | — | — |
| 217 | TrxLineRefCustTaxableAmount | TAXABLE_AMOUNT | — | — |
| 218 | TrxLineRefCustTaxableFlag | TAXABLE_FLAG | — | — |
| 219 | TrxLineRefCustTranslatedDescription | TRANSLATED_DESCRIPTION | — | — |
| 220 | TrxLineRefCustTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 221 | TrxLineRefCustUnitSellingPrice | UNIT_SELLING_PRICE | — | — |
| 222 | TrxLineRefCustUnitStandardPrice | UNIT_STANDARD_PRICE | — | — |
| 223 | TrxLineRefCustUomCode | UOM_CODE | — | — |
| 224 | TrxLineRefCustUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 225 | TrxLineRefCustWhUpdateDate | WH_UPDATE_DATE | — | — |
| 226 | TrxLineTaxlinkAccountingRuleDuration | ACCOUNTING_RULE_DURATION | — | — |
| 227 | TrxLineTaxlinkAcctdAmountDueOriginal | ACCTD_AMOUNT_DUE_ORIGINAL | — | — |
| 228 | TrxLineTaxlinkAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | — |
| 229 | TrxLineTaxlinkAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 230 | TrxLineTaxlinkAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 231 | TrxLineTaxlinkAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 232 | TrxLineTaxlinkAssessableValue | ASSESSABLE_VALUE | — | — |
| 233 | TrxLineTaxlinkAutoruleCompleteFlag | AUTORULE_COMPLETE_FLAG | — | — |
| 234 | TrxLineTaxlinkAutoruleDurationProcessed | AUTORULE_DURATION_PROCESSED | — | — |
| 235 | TrxLineTaxlinkAutotax | AUTOTAX | — | — |
| 236 | TrxLineTaxlinkChrgAcctdAmountRemaining | CHRG_ACCTD_AMOUNT_REMAINING | — | — |
| 237 | TrxLineTaxlinkChrgAmountRemaining | CHRG_AMOUNT_REMAINING | — | — |
| 238 | TrxLineTaxlinkCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 239 | TrxLineTaxlinkDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 240 | TrxLineTaxlinkDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 241 | TrxLineTaxlinkDeferralExclusionFlag | DEFERRAL_EXCLUSION_FLAG | — | — |
| 242 | TrxLineTaxlinkDescription | DESCRIPTION | — | — |
| 243 | TrxLineTaxlinkExtendedAcctdAmount | EXTENDED_ACCTD_AMOUNT | — | — |
| 244 | TrxLineTaxlinkExtendedAmount | EXTENDED_AMOUNT | — | — |
| 245 | TrxLineTaxlinkFairMarketValueAmount | FAIR_MARKET_VALUE_AMOUNT | — | — |
| 246 | TrxLineTaxlinkFrtAdjAcctdRemaining | FRT_ADJ_ACCTD_REMAINING | — | — |
| 247 | TrxLineTaxlinkFrtAdjRemaining | FRT_ADJ_REMAINING | — | — |
| 248 | TrxLineTaxlinkFrtEdAcctdAmount | FRT_ED_ACCTD_AMOUNT | — | — |
| 249 | TrxLineTaxlinkFrtEdAmount | FRT_ED_AMOUNT | — | — |
| 250 | TrxLineTaxlinkFrtUnedAcctdAmount | FRT_UNED_ACCTD_AMOUNT | — | — |
| 251 | TrxLineTaxlinkFrtUnedAmount | FRT_UNED_AMOUNT | — | — |
| 252 | TrxLineTaxlinkGrossExtendedAmount | GROSS_EXTENDED_AMOUNT | — | — |
| 253 | TrxLineTaxlinkGrossUnitSellingPrice | GROSS_UNIT_SELLING_PRICE | — | — |
| 254 | TrxLineTaxlinkHistoricalFlag | HISTORICAL_FLAG | — | — |
| 255 | TrxLineTaxlinkInvoicedLineAcctgLevel | INVOICED_LINE_ACCTG_LEVEL | — | — |
| 256 | TrxLineTaxlinkItemContext | ITEM_CONTEXT | — | — |
| 257 | TrxLineTaxlinkLastPeriodToCredit | LAST_PERIOD_TO_CREDIT | — | — |
| 258 | TrxLineTaxlinkLineIntendedUse | LINE_INTENDED_USE | — | — |
| 259 | TrxLineTaxlinkLineNumber | LINE_NUMBER | — | — |
| 260 | TrxLineTaxlinkLineRecoverable | LINE_RECOVERABLE | — | — |
| 261 | TrxLineTaxlinkLineType | LINE_TYPE | — | — |
| 262 | TrxLineTaxlinkMrcExtendedAcctdAmount | MRC_EXTENDED_ACCTD_AMOUNT | — | — |
| 263 | TrxLineTaxlinkOverrideAutoAccountingFlag | OVERRIDE_AUTO_ACCOUNTING_FLAG | — | — |
| 264 | TrxLineTaxlinkProductCategory | PRODUCT_CATEGORY | — | — |
| 265 | TrxLineTaxlinkProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | — |
| 266 | TrxLineTaxlinkProductType | PRODUCT_TYPE | — | — |
| 267 | TrxLineTaxlinkProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 268 | TrxLineTaxlinkQuantityCredited | QUANTITY_CREDITED | — | — |
| 269 | TrxLineTaxlinkQuantityInvoiced | QUANTITY_INVOICED | — | — |
| 270 | TrxLineTaxlinkQuantityOrdered | QUANTITY_ORDERED | — | — |
| 271 | TrxLineTaxlinkReasonCode | REASON_CODE | — | — |
| 272 | TrxLineTaxlinkRevenueAmount | REVENUE_AMOUNT | — | — |
| 273 | TrxLineTaxlinkRuleEndDate | RULE_END_DATE | — | — |
| 274 | TrxLineTaxlinkRuleStartDate | RULE_START_DATE | — | — |
| 275 | TrxLineTaxlinkSalesOrder | SALES_ORDER | — | — |
| 276 | TrxLineTaxlinkSalesOrderDate | SALES_ORDER_DATE | — | — |
| 277 | TrxLineTaxlinkSalesOrderLine | SALES_ORDER_LINE | — | — |
| 278 | TrxLineTaxlinkSalesOrderRevision | SALES_ORDER_REVISION | — | — |
| 279 | TrxLineTaxlinkSalesOrderSource | SALES_ORDER_SOURCE | — | — |
| 280 | TrxLineTaxlinkSourceDocumentLineNumber | SOURCE_DOCUMENT_LINE_NUMBER | — | — |
| 281 | TrxLineTaxlinkTaxAction | TAX_ACTION | — | — |
| 282 | TrxLineTaxlinkTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 283 | TrxLineTaxlinkTaxExemptFlag | TAX_EXEMPT_FLAG | — | — |
| 284 | TrxLineTaxlinkTaxExemptNumber | TAX_EXEMPT_NUMBER | — | — |
| 285 | TrxLineTaxlinkTaxExemptReasonCode | TAX_EXEMPT_REASON_CODE | — | — |
| 286 | TrxLineTaxlinkTaxPrecedence | TAX_PRECEDENCE | — | — |
| 287 | TrxLineTaxlinkTaxRate | TAX_RATE | — | — |
| 288 | TrxLineTaxlinkTaxRecoverable | TAX_RECOVERABLE | — | — |
| 289 | TrxLineTaxlinkTaxVendorReturnCode | TAX_VENDOR_RETURN_CODE | — | — |
| 290 | TrxLineTaxlinkTaxableAmount | TAXABLE_AMOUNT | — | — |
| 291 | TrxLineTaxlinkTaxableFlag | TAXABLE_FLAG | — | — |
| 292 | TrxLineTaxlinkTranslatedDescription | TRANSLATED_DESCRIPTION | — | — |
| 293 | TrxLineTaxlinkTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 294 | TrxLineTaxlinkUnitSellingPrice | UNIT_SELLING_PRICE | — | — |
| 295 | TrxLineTaxlinkUnitStandardPrice | UNIT_STANDARD_PRICE | — | — |
| 296 | TrxLineTaxlinkUomCode | UOM_CODE | — | — |
| 297 | TrxLineTaxlinkUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 298 | TrxLineTaxlinkWhUpdateDate | WH_UPDATE_DATE | — | — |
| 299 | TrxnLinCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 300 | TrxnLinDescription | DESCRIPTION | — | — |
| 301 | TrxnLinLineNumber | LINE_NUMBER | — | ✅ |

### [[ra_cust_trx_types_all|RA_CUST_TRX_TYPES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionTypeAccountingAffectFlag | ACCOUNTING_AFFECT_FLAG | — | ✅ |
| 2 | TransactionTypeCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 3 | TransactionTypeDescription | DESCRIPTION | — | ✅ |
| 4 | TransactionTypeName | NAME | — | ✅ |
| 5 | TransactionTypeObjectVersionNumber11 | OBJECT_VERSION_NUMBER | — | — |
| 6 | TransactionTypePostToGl | POST_TO_GL | — | ✅ |
| 7 | TransactionTypeType | TYPE | — | ✅ |

### [[ra_rules|RA_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvDistRuleName | NAME | — | ✅ |
| 2 | InvDistRuleObjectVersionNumber7 | OBJECT_VERSION_NUMBER | — | — |
| 3 | InvDistRuleRuleId | RULE_ID | — | — |

### [[ra_terms_b|RA_TERMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentTermBPEODescription | DESCRIPTION | — | — |
| 2 | PaymentTermBPEOName | NAME | — | — |
| 3 | PaymentTermBPEOTermId1 | TERM_ID | — | — |

### [[ra_terms_lines|RA_TERMS_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentTermBPEOTermId | TERM_ID | — | — |
| 2 | PaymentTermLineObjectVersionNumber9 | OBJECT_VERSION_NUMBER | — | — |
| 3 | PaymentTermLineSequenceNum | SEQUENCE_NUM | — | ✅ |
| 4 | PaymentTermLineTermId1 | TERM_ID | — | — |

### [[ra_terms_vl|RA_TERMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentTermTranslationDescription | DESCRIPTION | — | — |
| 2 | PaymentTermTranslationName | NAME | — | — |
| 3 | PaymentTermTranslationTermId | TERM_ID | — | — |

### [[xla_events|XLA_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventBudgetaryControlFlag | BUDGETARY_CONTROL_FLAG | — | — |
| 2 | EventEventDate | EVENT_DATE | — | — |
| 3 | EventEventId | EVENT_ID | — | — |
| 4 | EventEventNumber | EVENT_NUMBER | — | — |
| 5 | EventEventStatusCode | EVENT_STATUS_CODE | — | — |
| 6 | EventEventTypeCode | EVENT_TYPE_CODE | — | — |
| 7 | EventHasWarningsFlag | HAS_WARNINGS_FLAG | — | — |
| 8 | EventOnHoldFlag | ON_HOLD_FLAG | — | — |
| 9 | EventProcessStatusCode | PROCESS_STATUS_CODE | — | — |
| 10 | EventTransactionDate | TRANSACTION_DATE | — | — |
| 11 | EventUpgValidFlag | UPG_VALID_FLAG | — | — |

### [[zx_fc_user_defined_v|ZX_FC_USER_DEFINED_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UsrDfndFiscClsClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | UsrDfndFiscClsClassificationName | CLASSIFICATION_NAME | — | — |
| 3 | UsrDfndFiscClsCountryCode | COUNTRY_CODE | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
