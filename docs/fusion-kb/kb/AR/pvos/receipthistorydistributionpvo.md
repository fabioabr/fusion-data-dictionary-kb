---
id: DOC-AR-PVO-ReceiptHistoryDistributionPVO
doc_type: system-doc
title: "ReceiptHistoryDistributionPVO — PVO Accounts Receivable"
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
  - ReceiptHistoryDistributionPVO
  - receipthistorydistributionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReceiptHistoryDistributionPVO

## 📌 Visão Geral

Extrai as distribuições contábeis do histórico de recebimentos, rastreando como cada mudança de status impactou as contas do GL. Essencial para auditoria contábil e reconstrução do histórico de lançamentos de recebíveis.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.ReceiptHistoryDistributionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 479 | 13 | 1 | 55 | 11% |

---

## 🔗 Tabelas Relacionadas

- [[ar_batches_all|AR_BATCHES_ALL]] — 46 atributos (1 BICC)
- [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]] — 85 atributos (3 BICC)
- [[ar_cash_receipt_history_all|AR_CASH_RECEIPT_HISTORY_ALL]] — 52 atributos (20 BICC)
- [[ar_distributions_all|AR_DISTRIBUTIONS_ALL]] — 141 atributos (1 PKs, 24 BICC)
- [[ar_payment_schedules_all|AR_PAYMENT_SCHEDULES_ALL]] — 2 atributos (1 BICC)
- [[ar_recon_difference_details|AR_RECON_DIFFERENCE_DETAILS]] — 17 atributos
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 1 atributos
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 36 atributos (4 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 3 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos
- [[per_users|PER_USERS]] — 7 atributos
- [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]] — 3 atributos (1 BICC)
- [[ra_customer_trx_lines_all|RA_CUSTOMER_TRX_LINES_ALL]] — 76 atributos (1 BICC)

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
| 1 | HistoryAccountCodeCombinationId | ACCOUNT_CODE_COMBINATION_ID | — | — |
| 2 | HistoryAcctdAmount | ACCTD_AMOUNT | — | — |
| 3 | HistoryAcctdFactorDiscountAmount | ACCTD_FACTOR_DISCOUNT_AMOUNT | — | — |
| 4 | HistoryAmount | AMOUNT | — | — |
| 5 | HistoryBankChargeAccountCcid | BANK_CHARGE_ACCOUNT_CCID | — | — |
| 6 | HistoryBatchId | BATCH_ID | — | — |
| 7 | HistoryCashReceiptHistoryId | CASH_RECEIPT_HISTORY_ID | — | ✅ |
| 8 | HistoryCashReceiptId | CASH_RECEIPT_ID | — | — |
| 9 | HistoryCreatedBy | CREATED_BY | — | ✅ |
| 10 | HistoryCreatedFrom | CREATED_FROM | — | — |
| 11 | HistoryCreationDate | CREATION_DATE | — | ✅ |
| 12 | HistoryCurrentRecordFlag | CURRENT_RECORD_FLAG | — | ✅ |
| 13 | HistoryEventId | EVENT_ID | — | ✅ |
| 14 | HistoryExchangeDate | EXCHANGE_DATE | — | ✅ |
| 15 | HistoryExchangeRate | EXCHANGE_RATE | — | ✅ |
| 16 | HistoryExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 17 | HistoryFactorDiscountAmount | FACTOR_DISCOUNT_AMOUNT | — | — |
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
| 50 | PrvStatHistoryCashReceiptHistoryId | CASH_RECEIPT_HISTORY_ID | — | — |
| 51 | PrvStatHistoryCashReceiptId | CASH_RECEIPT_ID | — | — |
| 52 | PrvStatHistoryStatus | STATUS | — | ✅ |

### [[ar_distributions_all|AR_DISTRIBUTIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustmentDistributionAcctdAmountCr | ACCTD_AMOUNT_CR | — | — |
| 2 | AdjustmentDistributionAcctdAmountDr | ACCTD_AMOUNT_DR | — | — |
| 3 | AdjustmentDistributionActivityBucket | ACTIVITY_BUCKET | — | — |
| 4 | AdjustmentDistributionAmountCr | AMOUNT_CR | — | — |
| 5 | AdjustmentDistributionAmountDr | AMOUNT_DR | — | — |
| 6 | AdjustmentDistributionCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 7 | AdjustmentDistributionCreatedBy | CREATED_BY | — | — |
| 8 | AdjustmentDistributionCreationDate | CREATION_DATE | — | — |
| 9 | AdjustmentDistributionCurrencyCode | CURRENCY_CODE | — | — |
| 10 | AdjustmentDistributionCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | — |
| 11 | AdjustmentDistributionCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | — |
| 12 | AdjustmentDistributionCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | — |
| 13 | AdjustmentDistributionFromAcctdAmountCr | FROM_ACCTD_AMOUNT_CR | — | — |
| 14 | AdjustmentDistributionFromAcctdAmountDr | FROM_ACCTD_AMOUNT_DR | — | — |
| 15 | AdjustmentDistributionFromAmountCr | FROM_AMOUNT_CR | — | — |
| 16 | AdjustmentDistributionFromAmountDr | FROM_AMOUNT_DR | — | — |
| 17 | AdjustmentDistributionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | AdjustmentDistributionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | AdjustmentDistributionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | AdjustmentDistributionLineId | LINE_ID | — | — |
| 21 | AdjustmentDistributionLocationSegmentId | LOCATION_SEGMENT_ID | — | — |
| 22 | AdjustmentDistributionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | AdjustmentDistributionOrgId | ORG_ID | — | — |
| 24 | AdjustmentDistributionRefAccountClass | REF_ACCOUNT_CLASS | — | — |
| 25 | AdjustmentDistributionRefCustTrxLineGlDistId | REF_CUST_TRX_LINE_GL_DIST_ID | — | — |
| 26 | AdjustmentDistributionRefCustomerTrxLineId | REF_CUSTOMER_TRX_LINE_ID | — | — |
| 27 | AdjustmentDistributionRefDistCcid | REF_DIST_CCID | — | — |
| 28 | AdjustmentDistributionRefLineId | REF_LINE_ID | — | — |
| 29 | AdjustmentDistributionRefMfDistFlag | REF_MF_DIST_FLAG | — | — |
| 30 | AdjustmentDistributionReversalFlag | REVERSAL_FLAG | — | — |
| 31 | AdjustmentDistributionReversedSourceId | REVERSED_SOURCE_ID | — | — |
| 32 | AdjustmentDistributionSourceId | SOURCE_ID | — | — |
| 33 | AdjustmentDistributionSourceIdSecondary | SOURCE_ID_SECONDARY | — | — |
| 34 | AdjustmentDistributionSourceTable | SOURCE_TABLE | — | — |
| 35 | AdjustmentDistributionSourceTableSecondary | SOURCE_TABLE_SECONDARY | — | — |
| 36 | AdjustmentDistributionSourceType | SOURCE_TYPE | — | — |
| 37 | AdjustmentDistributionSourceTypeSecondary | SOURCE_TYPE_SECONDARY | — | — |
| 38 | AdjustmentDistributionTaxCodeId | TAX_CODE_ID | — | — |
| 39 | AdjustmentDistributionTaxGroupCodeId | TAX_GROUP_CODE_ID | — | — |
| 40 | AdjustmentDistributionTaxId | TAX_ID | — | — |
| 41 | AdjustmentDistributionTaxLinkId | TAX_LINK_ID | — | — |
| 42 | AdjustmentDistributionTaxableAccountedCr | TAXABLE_ACCOUNTED_CR | — | — |
| 43 | AdjustmentDistributionTaxableAccountedDr | TAXABLE_ACCOUNTED_DR | — | — |
| 44 | AdjustmentDistributionTaxableEnteredCr | TAXABLE_ENTERED_CR | — | — |
| 45 | AdjustmentDistributionTaxableEnteredDr | TAXABLE_ENTERED_DR | — | — |
| 46 | AdjustmentDistributionThirdPartyId | THIRD_PARTY_ID | — | — |
| 47 | AdjustmentDistributionThirdPartySubId | THIRD_PARTY_SUB_ID | — | — |
| 48 | CashDistributionAcctdAmountCr | ACCTD_AMOUNT_CR | — | ✅ |
| 49 | CashDistributionAcctdAmountDr | ACCTD_AMOUNT_DR | — | ✅ |
| 50 | CashDistributionActivityBucket | ACTIVITY_BUCKET | — | ✅ |
| 51 | CashDistributionAmountCr | AMOUNT_CR | — | ✅ |
| 52 | CashDistributionAmountDr | AMOUNT_DR | — | ✅ |
| 53 | CashDistributionCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 54 | CashDistributionCreatedBy | CREATED_BY | — | — |
| 55 | CashDistributionCreationDate | CREATION_DATE | — | — |
| 56 | CashDistributionCurrencyCode | CURRENCY_CODE | — | — |
| 57 | CashDistributionCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 58 | CashDistributionCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 59 | CashDistributionCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 60 | CashDistributionFromAcctdAmountCr | FROM_ACCTD_AMOUNT_CR | — | ✅ |
| 61 | CashDistributionFromAcctdAmountDr | FROM_ACCTD_AMOUNT_DR | — | ✅ |
| 62 | CashDistributionFromAmountCr | FROM_AMOUNT_CR | — | ✅ |
| 63 | CashDistributionFromAmountDr | FROM_AMOUNT_DR | — | ✅ |
| 64 | CashDistributionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 65 | CashDistributionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 66 | CashDistributionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 67 | CashDistributionLocationSegmentId | LOCATION_SEGMENT_ID | — | — |
| 68 | CashDistributionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 69 | CashDistributionOrgId | ORG_ID | — | — |
| 70 | CashDistributionRefAccountClass | REF_ACCOUNT_CLASS | — | ✅ |
| 71 | CashDistributionRefCustTrxLineGlDistId | REF_CUST_TRX_LINE_GL_DIST_ID | — | — |
| 72 | CashDistributionRefCustomerTrxLineId | REF_CUSTOMER_TRX_LINE_ID | — | — |
| 73 | CashDistributionRefDistCcid | REF_DIST_CCID | — | — |
| 74 | CashDistributionRefLineId | REF_LINE_ID | — | — |
| 75 | CashDistributionRefMfDistFlag | REF_MF_DIST_FLAG | — | — |
| 76 | CashDistributionReversalFlag | REVERSAL_FLAG | — | — |
| 77 | CashDistributionReversedSourceId | REVERSED_SOURCE_ID | — | — |
| 78 | CashDistributionSourceId | SOURCE_ID | — | ✅ |
| 79 | CashDistributionSourceIdSecondary | SOURCE_ID_SECONDARY | — | — |
| 80 | CashDistributionSourceTable | SOURCE_TABLE | — | ✅ |
| 81 | CashDistributionSourceTableSecondary | SOURCE_TABLE_SECONDARY | — | — |
| 82 | CashDistributionSourceType | SOURCE_TYPE | — | ✅ |
| 83 | CashDistributionSourceTypeSecondary | SOURCE_TYPE_SECONDARY | — | — |
| 84 | CashDistributionTaxCodeId | TAX_CODE_ID | — | — |
| 85 | CashDistributionTaxGroupCodeId | TAX_GROUP_CODE_ID | — | — |
| 86 | CashDistributionTaxId | TAX_ID | — | — |
| 87 | CashDistributionTaxLinkId | TAX_LINK_ID | — | — |
| 88 | CashDistributionTaxableAccountedCr | TAXABLE_ACCOUNTED_CR | — | ✅ |
| 89 | CashDistributionTaxableAccountedDr | TAXABLE_ACCOUNTED_DR | — | ✅ |
| 90 | CashDistributionTaxableEnteredCr | TAXABLE_ENTERED_CR | — | ✅ |
| 91 | CashDistributionTaxableEnteredDr | TAXABLE_ENTERED_DR | — | ✅ |
| 92 | CashDistributionThirdPartyId | THIRD_PARTY_ID | — | — |
| 93 | CashDistributionThirdPartySubId | THIRD_PARTY_SUB_ID | — | — |
| 94 | LineId | LINE_ID | 🔑 | ✅ |
| 95 | ReverseDistributionAcctdAmountCr | ACCTD_AMOUNT_CR | — | — |
| 96 | ReverseDistributionAcctdAmountDr | ACCTD_AMOUNT_DR | — | — |
| 97 | ReverseDistributionActivityBucket | ACTIVITY_BUCKET | — | — |
| 98 | ReverseDistributionAmountCr | AMOUNT_CR | — | — |
| 99 | ReverseDistributionAmountDr | AMOUNT_DR | — | — |
| 100 | ReverseDistributionCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 101 | ReverseDistributionCreatedBy | CREATED_BY | — | — |
| 102 | ReverseDistributionCreationDate | CREATION_DATE | — | — |
| 103 | ReverseDistributionCurrencyCode | CURRENCY_CODE | — | — |
| 104 | ReverseDistributionCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | — |
| 105 | ReverseDistributionCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | — |
| 106 | ReverseDistributionCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | — |
| 107 | ReverseDistributionFromAcctdAmountCr | FROM_ACCTD_AMOUNT_CR | — | — |
| 108 | ReverseDistributionFromAcctdAmountDr | FROM_ACCTD_AMOUNT_DR | — | — |
| 109 | ReverseDistributionFromAmountCr | FROM_AMOUNT_CR | — | — |
| 110 | ReverseDistributionFromAmountDr | FROM_AMOUNT_DR | — | — |
| 111 | ReverseDistributionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 112 | ReverseDistributionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 113 | ReverseDistributionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 114 | ReverseDistributionLineId | LINE_ID | — | — |
| 115 | ReverseDistributionLocationSegmentId | LOCATION_SEGMENT_ID | — | — |
| 116 | ReverseDistributionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 117 | ReverseDistributionOrgId | ORG_ID | — | — |
| 118 | ReverseDistributionRefAccountClass | REF_ACCOUNT_CLASS | — | — |
| 119 | ReverseDistributionRefCustTrxLineGlDistId | REF_CUST_TRX_LINE_GL_DIST_ID | — | — |
| 120 | ReverseDistributionRefCustomerTrxLineId | REF_CUSTOMER_TRX_LINE_ID | — | — |
| 121 | ReverseDistributionRefDistCcid | REF_DIST_CCID | — | — |
| 122 | ReverseDistributionRefLineId | REF_LINE_ID | — | — |
| 123 | ReverseDistributionRefMfDistFlag | REF_MF_DIST_FLAG | — | — |
| 124 | ReverseDistributionReversalFlag | REVERSAL_FLAG | — | — |
| 125 | ReverseDistributionReversedSourceId | REVERSED_SOURCE_ID | — | — |
| 126 | ReverseDistributionSourceId | SOURCE_ID | — | — |
| 127 | ReverseDistributionSourceIdSecondary | SOURCE_ID_SECONDARY | — | — |
| 128 | ReverseDistributionSourceTable | SOURCE_TABLE | — | — |
| 129 | ReverseDistributionSourceTableSecondary | SOURCE_TABLE_SECONDARY | — | — |
| 130 | ReverseDistributionSourceType | SOURCE_TYPE | — | — |
| 131 | ReverseDistributionSourceTypeSecondary | SOURCE_TYPE_SECONDARY | — | — |
| 132 | ReverseDistributionTaxCodeId | TAX_CODE_ID | — | — |
| 133 | ReverseDistributionTaxGroupCodeId | TAX_GROUP_CODE_ID | — | — |
| 134 | ReverseDistributionTaxId | TAX_ID | — | — |
| 135 | ReverseDistributionTaxLinkId | TAX_LINK_ID | — | — |
| 136 | ReverseDistributionTaxableAccountedCr | TAXABLE_ACCOUNTED_CR | — | — |
| 137 | ReverseDistributionTaxableAccountedDr | TAXABLE_ACCOUNTED_DR | — | — |
| 138 | ReverseDistributionTaxableEnteredCr | TAXABLE_ENTERED_CR | — | — |
| 139 | ReverseDistributionTaxableEnteredDr | TAXABLE_ENTERED_DR | — | — |
| 140 | ReverseDistributionThirdPartyId | THIRD_PARTY_ID | — | — |
| 141 | ReverseDistributionThirdPartySubId | THIRD_PARTY_SUB_ID | — | — |

### [[ar_payment_schedules_all|AR_PAYMENT_SCHEDULES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentSchedulesDueDate | DUE_DATE | — | ✅ |
| 2 | PaymentSchedulesPaymentScheduleId | PAYMENT_SCHEDULE_ID | — | — |

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

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitBusinessUnitId | BU_ID | — | — |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DailyConversionTypeConversionType | CONVERSION_TYPE | — | — |
| 2 | DailyConversionTypeCreatedBy | CREATED_BY | — | — |
| 3 | DailyConversionTypeCreationDate | CREATION_DATE | — | — |
| 4 | DailyConversionTypeDescription | DESCRIPTION | — | — |
| 5 | DailyConversionTypeEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 6 | DailyConversionTypeEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 7 | DailyConversionTypeFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 8 | DailyConversionTypeFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 9 | DailyConversionTypeFemScenario | FEM_SCENARIO | — | — |
| 10 | DailyConversionTypeFemTimeframe | FEM_TIMEFRAME | — | — |
| 11 | DailyConversionTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | DailyConversionTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | DailyConversionTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | DailyConversionTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | DailyConversionTypePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 16 | DailyConversionTypeSecurityFlag | SECURITY_FLAG | — | — |
| 17 | DailyConversionTypeUserConversionType | USER_CONVERSION_TYPE | — | ✅ |
| 18 | DailyConversionTypeUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |
| 19 | HistoryDailyRateConversionType | CONVERSION_TYPE | — | — |
| 20 | HistoryDailyRateCreatedBy | CREATED_BY | — | — |
| 21 | HistoryDailyRateCreationDate | CREATION_DATE | — | — |
| 22 | HistoryDailyRateDescription | DESCRIPTION | — | — |
| 23 | HistoryDailyRateEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 24 | HistoryDailyRateEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 25 | HistoryDailyRateFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 26 | HistoryDailyRateFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 27 | HistoryDailyRateFemScenario | FEM_SCENARIO | — | — |
| 28 | HistoryDailyRateFemTimeframe | FEM_TIMEFRAME | — | — |
| 29 | HistoryDailyRateLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | HistoryDailyRateLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 31 | HistoryDailyRateLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 32 | HistoryDailyRateObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 33 | HistoryDailyRatePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 34 | HistoryDailyRateSecurityFlag | SECURITY_FLAG | — | — |
| 35 | HistoryDailyRateUserConversionType | USER_CONVERSION_TYPE | — | ✅ |
| 36 | HistoryDailyRateUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 2 | LedgersLedgerId | LEDGER_ID | — | — |
| 3 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |

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

### [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrxnHdrComments | COMMENTS | — | — |
| 2 | TrxnHdrCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 3 | TrxnHdrTrxNumber | TRX_NUMBER | — | ✅ |

### [[ra_customer_trx_lines_all|RA_CUSTOMER_TRX_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrxLineRefCustAccountingRuleDuration | ACCOUNTING_RULE_DURATION | — | — |
| 2 | TrxLineRefCustAcctdAmountDueOriginal | ACCTD_AMOUNT_DUE_ORIGINAL | — | — |
| 3 | TrxLineRefCustAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | — |
| 4 | TrxLineRefCustAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 5 | TrxLineRefCustAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 6 | TrxLineRefCustAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 7 | TrxLineRefCustAssessableValue | ASSESSABLE_VALUE | — | — |
| 8 | TrxLineRefCustAutoruleCompleteFlag | AUTORULE_COMPLETE_FLAG | — | — |
| 9 | TrxLineRefCustAutoruleDurationProcessed | AUTORULE_DURATION_PROCESSED | — | — |
| 10 | TrxLineRefCustAutotax | AUTOTAX | — | — |
| 11 | TrxLineRefCustChrgAcctdAmountRemaining | CHRG_ACCTD_AMOUNT_REMAINING | — | — |
| 12 | TrxLineRefCustChrgAmountRemaining | CHRG_AMOUNT_REMAINING | — | — |
| 13 | TrxLineRefCustCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 14 | TrxLineRefCustDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 15 | TrxLineRefCustDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 16 | TrxLineRefCustDeferralExclusionFlag | DEFERRAL_EXCLUSION_FLAG | — | — |
| 17 | TrxLineRefCustDescription | DESCRIPTION | — | — |
| 18 | TrxLineRefCustExtendedAcctdAmount | EXTENDED_ACCTD_AMOUNT | — | — |
| 19 | TrxLineRefCustExtendedAmount | EXTENDED_AMOUNT | — | — |
| 20 | TrxLineRefCustFairMarketValueAmount | FAIR_MARKET_VALUE_AMOUNT | — | — |
| 21 | TrxLineRefCustFrtAdjAcctdRemaining | FRT_ADJ_ACCTD_REMAINING | — | — |
| 22 | TrxLineRefCustFrtAdjRemaining | FRT_ADJ_REMAINING | — | — |
| 23 | TrxLineRefCustFrtEdAcctdAmount | FRT_ED_ACCTD_AMOUNT | — | — |
| 24 | TrxLineRefCustFrtEdAmount | FRT_ED_AMOUNT | — | — |
| 25 | TrxLineRefCustFrtUnedAcctdAmount | FRT_UNED_ACCTD_AMOUNT | — | — |
| 26 | TrxLineRefCustFrtUnedAmount | FRT_UNED_AMOUNT | — | — |
| 27 | TrxLineRefCustGrossExtendedAmount | GROSS_EXTENDED_AMOUNT | — | — |
| 28 | TrxLineRefCustGrossUnitSellingPrice | GROSS_UNIT_SELLING_PRICE | — | — |
| 29 | TrxLineRefCustHistoricalFlag | HISTORICAL_FLAG | — | — |
| 30 | TrxLineRefCustInvoicedLineAcctgLevel | INVOICED_LINE_ACCTG_LEVEL | — | — |
| 31 | TrxLineRefCustItemContext | ITEM_CONTEXT | — | — |
| 32 | TrxLineRefCustLastPeriodToCredit | LAST_PERIOD_TO_CREDIT | — | — |
| 33 | TrxLineRefCustLineIntendedUse | LINE_INTENDED_USE | — | — |
| 34 | TrxLineRefCustLineNumber | LINE_NUMBER | — | — |
| 35 | TrxLineRefCustLineRecoverable | LINE_RECOVERABLE | — | — |
| 36 | TrxLineRefCustLineType | LINE_TYPE | — | — |
| 37 | TrxLineRefCustMrcExtendedAcctdAmount | MRC_EXTENDED_ACCTD_AMOUNT | — | — |
| 38 | TrxLineRefCustOverrideAutoAccountingFlag | OVERRIDE_AUTO_ACCOUNTING_FLAG | — | — |
| 39 | TrxLineRefCustProductCategory | PRODUCT_CATEGORY | — | — |
| 40 | TrxLineRefCustProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | — |
| 41 | TrxLineRefCustProductType | PRODUCT_TYPE | — | — |
| 42 | TrxLineRefCustProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 43 | TrxLineRefCustQuantityCredited | QUANTITY_CREDITED | — | — |
| 44 | TrxLineRefCustQuantityInvoiced | QUANTITY_INVOICED | — | — |
| 45 | TrxLineRefCustQuantityOrdered | QUANTITY_ORDERED | — | — |
| 46 | TrxLineRefCustReasonCode | REASON_CODE | — | — |
| 47 | TrxLineRefCustRevenueAmount | REVENUE_AMOUNT | — | — |
| 48 | TrxLineRefCustRuleEndDate | RULE_END_DATE | — | — |
| 49 | TrxLineRefCustRuleStartDate | RULE_START_DATE | — | — |
| 50 | TrxLineRefCustSalesOrder | SALES_ORDER | — | — |
| 51 | TrxLineRefCustSalesOrderDate | SALES_ORDER_DATE | — | — |
| 52 | TrxLineRefCustSalesOrderLine | SALES_ORDER_LINE | — | — |
| 53 | TrxLineRefCustSalesOrderRevision | SALES_ORDER_REVISION | — | — |
| 54 | TrxLineRefCustSalesOrderSource | SALES_ORDER_SOURCE | — | — |
| 55 | TrxLineRefCustSourceDocumentLineNumber | SOURCE_DOCUMENT_LINE_NUMBER | — | — |
| 56 | TrxLineRefCustTaxAction | TAX_ACTION | — | — |
| 57 | TrxLineRefCustTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 58 | TrxLineRefCustTaxExemptFlag | TAX_EXEMPT_FLAG | — | — |
| 59 | TrxLineRefCustTaxExemptNumber | TAX_EXEMPT_NUMBER | — | — |
| 60 | TrxLineRefCustTaxExemptReasonCode | TAX_EXEMPT_REASON_CODE | — | — |
| 61 | TrxLineRefCustTaxPrecedence | TAX_PRECEDENCE | — | — |
| 62 | TrxLineRefCustTaxRate | TAX_RATE | — | — |
| 63 | TrxLineRefCustTaxRecoverable | TAX_RECOVERABLE | — | — |
| 64 | TrxLineRefCustTaxVendorReturnCode | TAX_VENDOR_RETURN_CODE | — | — |
| 65 | TrxLineRefCustTaxableAmount | TAXABLE_AMOUNT | — | — |
| 66 | TrxLineRefCustTaxableFlag | TAXABLE_FLAG | — | — |
| 67 | TrxLineRefCustTranslatedDescription | TRANSLATED_DESCRIPTION | — | — |
| 68 | TrxLineRefCustTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 69 | TrxLineRefCustUnitSellingPrice | UNIT_SELLING_PRICE | — | — |
| 70 | TrxLineRefCustUnitStandardPrice | UNIT_STANDARD_PRICE | — | — |
| 71 | TrxLineRefCustUomCode | UOM_CODE | — | — |
| 72 | TrxLineRefCustUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 73 | TrxLineRefCustWhUpdateDate | WH_UPDATE_DATE | — | — |
| 74 | TrxnLinCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 75 | TrxnLinDescription | DESCRIPTION | — | — |
| 76 | TrxnLinLineNumber | LINE_NUMBER | — | ✅ |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
