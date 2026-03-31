---
id: DOC-AR-PVO-ReceiptApplicationPVO
doc_type: system-doc
title: "ReceiptApplicationPVO — PVO Accounts Receivable"
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
  - ReceiptApplicationPVO
  - receiptapplicationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReceiptApplicationPVO

## 📌 Visão Geral

Extrai as aplicações de recebimentos a transações de Contas a Receber, incluindo valor aplicado, tipo de aplicação, regra utilizada e status. Central para rastrear como cada pagamento recebido foi alocado às faturas em aberto dos clientes.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.ReceiptApplicationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 1472 | 25 | 1 | 107 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[ar_app_rule_sets|AR_APP_RULE_SETS]] — 12 atributos (2 BICC)
- [[ar_batches_all|AR_BATCHES_ALL]] — 5 atributos (3 BICC)
- [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]] — 83 atributos (26 BICC)
- [[ar_collectors|AR_COLLECTORS]] — 11 atributos (1 BICC)
- [[ar_cons_inv_all|AR_CONS_INV_ALL]] — 88 atributos (3 BICC)
- [[ar_distribution_sets_all|AR_DISTRIBUTION_SETS_ALL]] — 12 atributos (2 BICC)
- [[ar_payment_schedules_all|AR_PAYMENT_SCHEDULES_ALL]] — 187 atributos (3 BICC)
- [[ar_receivables_trx_all|AR_RECEIVABLES_TRX_ALL]] — 50 atributos (4 BICC)
- [[ar_receivable_applications_all|AR_RECEIVABLE_APPLICATIONS_ALL]] — 168 atributos (1 PKs, 45 BICC)
- [[ce_bank_acct_uses_all|CE_BANK_ACCT_USES_ALL]] — 24 atributos
- [[ce_bank_branches_v|CE_BANK_BRANCHES_V]] — 33 atributos (1 BICC)
- [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]] — 5 atributos (1 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 3 atributos (1 BICC)
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 18 atributos (2 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 2 atributos
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 31 atributos (3 BICC)
- [[hz_parties|HZ_PARTIES]] — 5 atributos (1 BICC)
- [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]] — 44 atributos (2 BICC)
- [[iby_fndcpt_tx_extensions|IBY_FNDCPT_TX_EXTENSIONS]] — 14 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 33 atributos
- [[per_users|PER_USERS]] — 17 atributos
- [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]] — 425 atributos (4 BICC)
- [[ra_customer_trx_lines_all|RA_CUSTOMER_TRX_LINES_ALL]] — 149 atributos (2 BICC)
- [[xla_events|XLA_EVENTS]] — 11 atributos
- [[zx_sco_rates|ZX_SCO_RATES]] — 42 atributos

---

## ⚙️ Atributos

### [[ar_app_rule_sets|AR_APP_RULE_SETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AppRuleSetCreatedBy | CREATED_BY | — | — |
| 2 | AppRuleSetCreationDate | CREATION_DATE | — | — |
| 3 | AppRuleSetDescription | DESCRIPTION | — | — |
| 4 | AppRuleSetFreezeFlag | FREEZE_FLAG | — | — |
| 5 | AppRuleSetLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | AppRuleSetLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | AppRuleSetLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | AppRuleSetModuleId | MODULE_ID | — | — |
| 9 | AppRuleSetObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | AppRuleSetRuleSetId | RULE_SET_ID | — | — |
| 11 | AppRuleSetRuleSetName | RULE_SET_NAME | — | ✅ |
| 12 | AppRuleSetRuleSource | RULE_SOURCE | — | — |

### [[ar_batches_all|AR_BATCHES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReceiptBatchBatchId | BATCH_ID | — | ✅ |
| 2 | ReceiptBatchCurrencyCode | CURRENCY_CODE | — | — |
| 3 | ReceiptBatchName | NAME | — | ✅ |
| 4 | ReceiptBatchStatus | STATUS | — | ✅ |
| 5 | ReceiptBatchType | TYPE | — | — |

### [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReceiptActualValueDate | ACTUAL_VALUE_DATE | — | ✅ |
| 2 | ReceiptAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | ✅ |
| 3 | ReceiptAmount | AMOUNT | — | — |
| 4 | ReceiptAnticipatedClearingDate | ANTICIPATED_CLEARING_DATE | — | ✅ |
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
| 32 | ReceiptFactorDiscountAmount | FACTOR_DISCOUNT_AMOUNT | — | — |
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
| 64 | ReceiptReferenceType | REFERENCE_TYPE | — | — |
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
| 77 | ReceiptStatus | STATUS | — | ✅ |
| 78 | ReceiptTaxRate | TAX_RATE | — | ✅ |
| 79 | ReceiptType | TYPE | — | ✅ |
| 80 | ReceiptUniqueReference | UNIQUE_REFERENCE | — | — |
| 81 | ReceiptUssglTransactionCode | USSGL_TRANSACTION_CODE | — | — |
| 82 | ReceiptUssglTransactionCodeContext | USSGL_TRANSACTION_CODE_CONTEXT | — | — |
| 83 | ReceiptVatTaxId | VAT_TAX_ID | — | — |

### [[ar_collectors|AR_COLLECTORS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CollectorsAlias | ALIAS | — | — |
| 2 | CollectorsCollectorId | COLLECTOR_ID | — | — |
| 3 | CollectorsDescription | DESCRIPTION | — | — |
| 4 | CollectorsEmployeeId | EMPLOYEE_ID | — | — |
| 5 | CollectorsInactiveDate | INACTIVE_DATE | — | — |
| 6 | CollectorsName | NAME | — | ✅ |
| 7 | CollectorsResourceId | RESOURCE_ID | — | — |
| 8 | CollectorsResourceType | RESOURCE_TYPE | — | — |
| 9 | CollectorsSetId | SET_ID | — | — |
| 10 | CollectorsStatus | STATUS | — | — |
| 11 | CollectorsTelephoneNumber | TELEPHONE_NUMBER | — | — |

### [[ar_cons_inv_all|AR_CONS_INV_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConsTrxAgingBucket1Amt | AGING_BUCKET1_AMT | — | — |
| 2 | ConsTrxAgingBucket2Amt | AGING_BUCKET2_AMT | — | — |
| 3 | ConsTrxAgingBucket3Amt | AGING_BUCKET3_AMT | — | — |
| 4 | ConsTrxAgingBucket4Amt | AGING_BUCKET4_AMT | — | — |
| 5 | ConsTrxAgingBucket5Amt | AGING_BUCKET5_AMT | — | — |
| 6 | ConsTrxAgingBucket6Amt | AGING_BUCKET6_AMT | — | — |
| 7 | ConsTrxAgingBucket7Amt | AGING_BUCKET7_AMT | — | — |
| 8 | ConsTrxBeginningBalance | BEGINNING_BALANCE | — | — |
| 9 | ConsTrxBillLevelFlag | BILL_LEVEL_FLAG | — | — |
| 10 | ConsTrxBillingCycleId | BILLING_CYCLE_ID | — | — |
| 11 | ConsTrxBillingDate | BILLING_DATE | — | — |
| 12 | ConsTrxConcurrentRequestId | CONCURRENT_REQUEST_ID | — | — |
| 13 | ConsTrxConsBillingNumber | CONS_BILLING_NUMBER | — | ✅ |
| 14 | ConsTrxConsInvId | CONS_INV_ID | — | — |
| 15 | ConsTrxConsInvType | CONS_INV_TYPE | — | — |
| 16 | ConsTrxCreatedBy | CREATED_BY | — | — |
| 17 | ConsTrxCreationDate | CREATION_DATE | — | — |
| 18 | ConsTrxCurrencyCode | CURRENCY_CODE | — | — |
| 19 | ConsTrxCustomerId | CUSTOMER_ID | — | — |
| 20 | ConsTrxCutOffDate | CUT_OFF_DATE | — | — |
| 21 | ConsTrxDueDate | DUE_DATE | — | — |
| 22 | ConsTrxEndingBalance | ENDING_BALANCE | — | — |
| 23 | ConsTrxIssueDate | ISSUE_DATE | — | — |
| 24 | ConsTrxLastBillingDate | LAST_BILLING_DATE | — | — |
| 25 | ConsTrxLastChargeDate | LAST_CHARGE_DATE | — | — |
| 26 | ConsTrxLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 27 | ConsTrxLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 28 | ConsTrxLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 29 | ConsTrxObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 30 | ConsTrxOrgId | ORG_ID | — | — |
| 31 | ConsTrxPrintStatus | PRINT_STATUS | — | — |
| 32 | ConsTrxRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 33 | ConsTrxRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 34 | ConsTrxSiteUseId | SITE_USE_ID | — | — |
| 35 | ConsTrxStartDate | START_DATE | — | — |
| 36 | ConsTrxStatus | STATUS | — | — |
| 37 | ConsTrxTermId | TERM_ID | — | — |
| 38 | ConsTrxTotalAdjustmentsAmt | TOTAL_ADJUSTMENTS_AMT | — | — |
| 39 | ConsTrxTotalCreditsAmt | TOTAL_CREDITS_AMT | — | — |
| 40 | ConsTrxTotalFinanceChargesAmt | TOTAL_FINANCE_CHARGES_AMT | — | — |
| 41 | ConsTrxTotalReceiptsAmt | TOTAL_RECEIPTS_AMT | — | — |
| 42 | ConsTrxTotalTaxAmt | TOTAL_TAX_AMT | — | — |
| 43 | ConsTrxTotalTrxAmt | TOTAL_TRX_AMT | — | — |
| 44 | ConsTrxUnpaidReason | UNPAID_REASON | — | — |
| 45 | ToConsTrxAgingBucket1Amt | AGING_BUCKET1_AMT | — | — |
| 46 | ToConsTrxAgingBucket2Amt | AGING_BUCKET2_AMT | — | — |
| 47 | ToConsTrxAgingBucket3Amt | AGING_BUCKET3_AMT | — | — |
| 48 | ToConsTrxAgingBucket4Amt | AGING_BUCKET4_AMT | — | — |
| 49 | ToConsTrxAgingBucket5Amt | AGING_BUCKET5_AMT | — | — |
| 50 | ToConsTrxAgingBucket6Amt | AGING_BUCKET6_AMT | — | — |
| 51 | ToConsTrxAgingBucket7Amt | AGING_BUCKET7_AMT | — | — |
| 52 | ToConsTrxBeginningBalance | BEGINNING_BALANCE | — | — |
| 53 | ToConsTrxBillLevelFlag | BILL_LEVEL_FLAG | — | — |
| 54 | ToConsTrxBillingCycleId | BILLING_CYCLE_ID | — | — |
| 55 | ToConsTrxBillingDate | BILLING_DATE | — | — |
| 56 | ToConsTrxConcurrentRequestId | CONCURRENT_REQUEST_ID | — | — |
| 57 | ToConsTrxConsBillingNumber | CONS_BILLING_NUMBER | — | — |
| 58 | ToConsTrxConsInvId | CONS_INV_ID | — | — |
| 59 | ToConsTrxConsInvType | CONS_INV_TYPE | — | — |
| 60 | ToConsTrxCreatedBy | CREATED_BY | — | — |
| 61 | ToConsTrxCreationDate | CREATION_DATE | — | — |
| 62 | ToConsTrxCurrencyCode | CURRENCY_CODE | — | — |
| 63 | ToConsTrxCustomerId | CUSTOMER_ID | — | — |
| 64 | ToConsTrxCutOffDate | CUT_OFF_DATE | — | — |
| 65 | ToConsTrxDueDate | DUE_DATE | — | — |
| 66 | ToConsTrxEndingBalance | ENDING_BALANCE | — | — |
| 67 | ToConsTrxIssueDate | ISSUE_DATE | — | — |
| 68 | ToConsTrxLastBillingDate | LAST_BILLING_DATE | — | — |
| 69 | ToConsTrxLastChargeDate | LAST_CHARGE_DATE | — | — |
| 70 | ToConsTrxLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 71 | ToConsTrxLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 72 | ToConsTrxLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 73 | ToConsTrxObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 74 | ToConsTrxOrgId | ORG_ID | — | — |
| 75 | ToConsTrxPrintStatus | PRINT_STATUS | — | — |
| 76 | ToConsTrxRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 77 | ToConsTrxRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 78 | ToConsTrxSiteUseId | SITE_USE_ID | — | — |
| 79 | ToConsTrxStartDate | START_DATE | — | — |
| 80 | ToConsTrxStatus | STATUS | — | — |
| 81 | ToConsTrxTermId | TERM_ID | — | — |
| 82 | ToConsTrxTotalAdjustmentsAmt | TOTAL_ADJUSTMENTS_AMT | — | — |
| 83 | ToConsTrxTotalCreditsAmt | TOTAL_CREDITS_AMT | — | — |
| 84 | ToConsTrxTotalFinanceChargesAmt | TOTAL_FINANCE_CHARGES_AMT | — | — |
| 85 | ToConsTrxTotalReceiptsAmt | TOTAL_RECEIPTS_AMT | — | — |
| 86 | ToConsTrxTotalTaxAmt | TOTAL_TAX_AMT | — | — |
| 87 | ToConsTrxTotalTrxAmt | TOTAL_TRX_AMT | — | — |
| 88 | ToConsTrxUnpaidReason | UNPAID_REASON | — | — |

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
| 39 | PaymentScheduleCustomerSiteUseId | CUSTOMER_SITE_USE_ID | — | — |
| 40 | PaymentScheduleCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 41 | PaymentScheduleDiscountDate | DISCOUNT_DATE | — | — |
| 42 | PaymentScheduleDiscountOriginal | DISCOUNT_ORIGINAL | — | — |
| 43 | PaymentScheduleDiscountRemaining | DISCOUNT_REMAINING | — | — |
| 44 | PaymentScheduleDiscountTakenEarned | DISCOUNT_TAKEN_EARNED | — | — |
| 45 | PaymentScheduleDiscountTakenUnearned | DISCOUNT_TAKEN_UNEARNED | — | — |
| 46 | PaymentScheduleDisputeDate | DISPUTE_DATE | — | — |
| 47 | PaymentScheduleDueDate | DUE_DATE | — | — |
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
| 71 | PaymentSchedulePaymentScheduleId | PAYMENT_SCHEDULE_ID | — | — |
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
| 87 | PaymentScheduleStatus | STATUS | — | — |
| 88 | PaymentScheduleTaxOriginal | TAX_ORIGINAL | — | — |
| 89 | PaymentScheduleTaxRemaining | TAX_REMAINING | — | — |
| 90 | PaymentScheduleTermId | TERM_ID | — | — |
| 91 | PaymentScheduleTermsSequenceNumber | TERMS_SEQUENCE_NUMBER | — | — |
| 92 | PaymentScheduleTrxDate | TRX_DATE | — | — |
| 93 | PaymentScheduleTrxNumber | TRX_NUMBER | — | — |
| 94 | PaymentSchedulesAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | — |
| 95 | PaymentSchedulesActiveClaimFlag | ACTIVE_CLAIM_FLAG | — | — |
| 96 | PaymentSchedulesActualDateClosed | ACTUAL_DATE_CLOSED | — | — |
| 97 | PaymentSchedulesAdjustmentAmountLast | ADJUSTMENT_AMOUNT_LAST | — | — |
| 98 | PaymentSchedulesAdjustmentDateLast | ADJUSTMENT_DATE_LAST | — | — |
| 99 | PaymentSchedulesAdjustmentGlDateLast | ADJUSTMENT_GL_DATE_LAST | — | — |
| 100 | PaymentSchedulesAdjustmentIdLast | ADJUSTMENT_ID_LAST | — | — |
| 101 | PaymentSchedulesAmountAdjusted | AMOUNT_ADJUSTED | — | — |
| 102 | PaymentSchedulesAmountAdjustedPending | AMOUNT_ADJUSTED_PENDING | — | — |
| 103 | PaymentSchedulesAmountApplied | AMOUNT_APPLIED | — | — |
| 104 | PaymentSchedulesAmountCredited | AMOUNT_CREDITED | — | — |
| 105 | PaymentSchedulesAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 106 | PaymentSchedulesAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 107 | PaymentSchedulesAmountInDispute | AMOUNT_IN_DISPUTE | — | — |
| 108 | PaymentSchedulesAmountLineItemsOriginal | AMOUNT_LINE_ITEMS_ORIGINAL | — | — |
| 109 | PaymentSchedulesAmountLineItemsRemaining | AMOUNT_LINE_ITEMS_REMAINING | — | — |
| 110 | PaymentSchedulesAmountOnAccount | AMOUNT_ON_ACCOUNT | — | — |
| 111 | PaymentSchedulesAmountOtherAccount | AMOUNT_OTHER_ACCOUNT | — | — |
| 112 | PaymentSchedulesAssociatedCashReceiptId | ASSOCIATED_CASH_RECEIPT_ID | — | — |
| 113 | PaymentSchedulesBrAmountAssigned | BR_AMOUNT_ASSIGNED | — | — |
| 114 | PaymentSchedulesCallDateLast | CALL_DATE_LAST | — | — |
| 115 | PaymentSchedulesCashAppliedAmountLast | CASH_APPLIED_AMOUNT_LAST | — | — |
| 116 | PaymentSchedulesCashAppliedDateLast | CASH_APPLIED_DATE_LAST | — | — |
| 117 | PaymentSchedulesCashAppliedIdLast | CASH_APPLIED_ID_LAST | — | — |
| 118 | PaymentSchedulesCashAppliedStatusLast | CASH_APPLIED_STATUS_LAST | — | — |
| 119 | PaymentSchedulesCashGlDateLast | CASH_GL_DATE_LAST | — | — |
| 120 | PaymentSchedulesCashReceiptAmountLast | CASH_RECEIPT_AMOUNT_LAST | — | — |
| 121 | PaymentSchedulesCashReceiptDateLast | CASH_RECEIPT_DATE_LAST | — | — |
| 122 | PaymentSchedulesCashReceiptId1 | CASH_RECEIPT_ID | — | — |
| 123 | PaymentSchedulesCashReceiptIdLast | CASH_RECEIPT_ID_LAST | — | — |
| 124 | PaymentSchedulesCashReceiptStatusLast | CASH_RECEIPT_STATUS_LAST | — | — |
| 125 | PaymentSchedulesCollectorLast | COLLECTOR_LAST | — | — |
| 126 | PaymentSchedulesConsInvId | CONS_INV_ID | — | — |
| 127 | PaymentSchedulesConsInvIdRev | CONS_INV_ID_REV | — | — |
| 128 | PaymentSchedulesCreatedBy | CREATED_BY | — | — |
| 129 | PaymentSchedulesCreationDate | CREATION_DATE | — | — |
| 130 | PaymentSchedulesCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 131 | PaymentSchedulesCustomerId | CUSTOMER_ID | — | — |
| 132 | PaymentSchedulesCustomerSiteUseId | CUSTOMER_SITE_USE_ID | — | — |
| 133 | PaymentSchedulesCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 134 | PaymentSchedulesDebitMemoPaymentScheduleId | PAYMENT_SCHEDULE_ID | — | — |
| 135 | PaymentSchedulesDiscountDate | DISCOUNT_DATE | — | — |
| 136 | PaymentSchedulesDiscountOriginal | DISCOUNT_ORIGINAL | — | — |
| 137 | PaymentSchedulesDiscountRemaining | DISCOUNT_REMAINING | — | — |
| 138 | PaymentSchedulesDiscountTakenEarned | DISCOUNT_TAKEN_EARNED | — | — |
| 139 | PaymentSchedulesDiscountTakenUnearned | DISCOUNT_TAKEN_UNEARNED | — | — |
| 140 | PaymentSchedulesDisputeDate | DISPUTE_DATE | — | — |
| 141 | PaymentSchedulesDueDate | DUE_DATE | — | ✅ |
| 142 | PaymentSchedulesDunningLevelOverrideDate | DUNNING_LEVEL_OVERRIDE_DATE | — | — |
| 143 | PaymentSchedulesExchangeDate | EXCHANGE_DATE | — | — |
| 144 | PaymentSchedulesExchangeRate | EXCHANGE_RATE | — | — |
| 145 | PaymentSchedulesExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 146 | PaymentSchedulesExcludeFromConsBillFlag | EXCLUDE_FROM_CONS_BILL_FLAG | — | — |
| 147 | PaymentSchedulesExcludeFromDunningFlag | EXCLUDE_FROM_DUNNING_FLAG | — | — |
| 148 | PaymentSchedulesFollowUpCodeLast | FOLLOW_UP_CODE_LAST | — | — |
| 149 | PaymentSchedulesFollowUpDateLast | FOLLOW_UP_DATE_LAST | — | — |
| 150 | PaymentSchedulesFreightOriginal | FREIGHT_ORIGINAL | — | — |
| 151 | PaymentSchedulesFreightRemaining | FREIGHT_REMAINING | — | — |
| 152 | PaymentSchedulesGlDate | GL_DATE | — | — |
| 153 | PaymentSchedulesGlDateClosed | GL_DATE_CLOSED | — | — |
| 154 | PaymentSchedulesInCollection | IN_COLLECTION | — | — |
| 155 | PaymentSchedulesInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 156 | PaymentSchedulesLastChargeDate | LAST_CHARGE_DATE | — | — |
| 157 | PaymentSchedulesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 158 | PaymentSchedulesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 159 | PaymentSchedulesLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 160 | PaymentSchedulesNumberOfDueDates | NUMBER_OF_DUE_DATES | — | — |
| 161 | PaymentSchedulesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 162 | PaymentSchedulesOrgId | ORG_ID | — | — |
| 163 | PaymentSchedulesPaymentApproval | PAYMENT_APPROVAL | — | — |
| 164 | PaymentSchedulesPaymentScheduleClass1 | CLASS | — | — |
| 165 | PaymentSchedulesPaymentScheduleId | PAYMENT_SCHEDULE_ID | — | — |
| 166 | PaymentSchedulesProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 167 | PaymentSchedulesProgramId | PROGRAM_ID | — | — |
| 168 | PaymentSchedulesProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 169 | PaymentSchedulesPromiseAmountLast | PROMISE_AMOUNT_LAST | — | — |
| 170 | PaymentSchedulesPromiseDateLast | PROMISE_DATE_LAST | — | — |
| 171 | PaymentSchedulesReceiptConfirmedFlag1 | RECEIPT_CONFIRMED_FLAG | — | — |
| 172 | PaymentSchedulesReceivablesChargesCharged | RECEIVABLES_CHARGES_CHARGED | — | — |
| 173 | PaymentSchedulesReceivablesChargesRemaining | RECEIVABLES_CHARGES_REMAINING | — | — |
| 174 | PaymentSchedulesRequestId | REQUEST_ID | — | — |
| 175 | PaymentSchedulesReservedType | RESERVED_TYPE | — | — |
| 176 | PaymentSchedulesReservedValue | RESERVED_VALUE | — | — |
| 177 | PaymentSchedulesReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 178 | PaymentSchedulesSecondLastChargeDate | SECOND_LAST_CHARGE_DATE | — | — |
| 179 | PaymentSchedulesSelectedForReceiptBatchId | SELECTED_FOR_RECEIPT_BATCH_ID | — | — |
| 180 | PaymentSchedulesStagedDunningLevel | STAGED_DUNNING_LEVEL | — | — |
| 181 | PaymentSchedulesStatus | STATUS | — | — |
| 182 | PaymentSchedulesTaxOriginal | TAX_ORIGINAL | — | — |
| 183 | PaymentSchedulesTaxRemaining | TAX_REMAINING | — | — |
| 184 | PaymentSchedulesTermId | TERM_ID | — | — |
| 185 | PaymentSchedulesTermsSequenceNumber | TERMS_SEQUENCE_NUMBER | — | — |
| 186 | PaymentSchedulesTrxDate | TRX_DATE | — | — |
| 187 | PaymentSchedulesTrxNumber | TRX_NUMBER | — | — |

### [[ar_receivables_trx_all|AR_RECEIVABLES_TRX_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RcvTrxIdAccountingAffectFlag | ACCOUNTING_AFFECT_FLAG | — | — |
| 2 | RcvTrxIdAssetTaxCode | ASSET_TAX_CODE | — | — |
| 3 | RcvTrxIdCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 4 | RcvTrxIdCreatedBy | CREATED_BY | — | — |
| 5 | RcvTrxIdCreationDate | CREATION_DATE | — | — |
| 6 | RcvTrxIdDefaultAcctgDistributionSet | DEFAULT_ACCTG_DISTRIBUTION_SET | — | — |
| 7 | RcvTrxIdDescription | DESCRIPTION | — | — |
| 8 | RcvTrxIdEndDateActive | END_DATE_ACTIVE | — | — |
| 9 | RcvTrxIdGlAccountSource | GL_ACCOUNT_SOURCE | — | — |
| 10 | RcvTrxIdInactiveDate | INACTIVE_DATE | — | — |
| 11 | RcvTrxIdLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | RcvTrxIdLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | RcvTrxIdLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | RcvTrxIdLiabilityTaxCode | LIABILITY_TAX_CODE | — | — |
| 15 | RcvTrxIdName | NAME | — | ✅ |
| 16 | RcvTrxIdObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | RcvTrxIdOrgId | ORG_ID | — | — |
| 18 | RcvTrxIdReceivablesTrxId | RECEIVABLES_TRX_ID | — | — |
| 19 | RcvTrxIdRiskEliminationDays | RISK_ELIMINATION_DAYS | — | — |
| 20 | RcvTrxIdSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 21 | RcvTrxIdStartDateActive | START_DATE_ACTIVE | — | — |
| 22 | RcvTrxIdStatus | STATUS | — | — |
| 23 | RcvTrxIdTaxCodeSource | TAX_CODE_SOURCE | — | — |
| 24 | RcvTrxIdTaxRecoverableFlag | TAX_RECOVERABLE_FLAG | — | — |
| 25 | RcvTrxIdType | TYPE | — | — |
| 26 | ReceivableActivityAccountingAffectFlag | ACCOUNTING_AFFECT_FLAG | — | — |
| 27 | ReceivableActivityAssetTaxCode | ASSET_TAX_CODE | — | — |
| 28 | ReceivableActivityCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 29 | ReceivableActivityCreatedBy | CREATED_BY | — | — |
| 30 | ReceivableActivityCreationDate | CREATION_DATE | — | — |
| 31 | ReceivableActivityDefaultAcctgDistributionSet | DEFAULT_ACCTG_DISTRIBUTION_SET | — | — |
| 32 | ReceivableActivityDescription | DESCRIPTION | — | — |
| 33 | ReceivableActivityEndDateActive | END_DATE_ACTIVE | — | — |
| 34 | ReceivableActivityGlAccountSource | GL_ACCOUNT_SOURCE | — | — |
| 35 | ReceivableActivityInactiveDate | INACTIVE_DATE | — | — |
| 36 | ReceivableActivityLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 37 | ReceivableActivityLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 38 | ReceivableActivityLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 39 | ReceivableActivityLiabilityTaxCode | LIABILITY_TAX_CODE | — | — |
| 40 | ReceivableActivityName | NAME | — | ✅ |
| 41 | ReceivableActivityObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 42 | ReceivableActivityOrgId | ORG_ID | — | — |
| 43 | ReceivableActivityReceivablesTrxId | RECEIVABLES_TRX_ID | — | — |
| 44 | ReceivableActivityRiskEliminationDays | RISK_ELIMINATION_DAYS | — | — |
| 45 | ReceivableActivitySetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 46 | ReceivableActivityStartDateActive | START_DATE_ACTIVE | — | — |
| 47 | ReceivableActivityStatus | STATUS | — | — |
| 48 | ReceivableActivityTaxCodeSource | TAX_CODE_SOURCE | — | — |
| 49 | ReceivableActivityTaxRecoverableFlag | TAX_RECOVERABLE_FLAG | — | — |
| 50 | ReceivableActivityType | TYPE | — | — |

### [[ar_receivable_applications_all|AR_RECEIVABLE_APPLICATIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AppRcvAppAcctdAmountAppliedFrom | ACCTD_AMOUNT_APPLIED_FROM | — | — |
| 2 | AppRcvAppAcctdAmountAppliedTo | ACCTD_AMOUNT_APPLIED_TO | — | — |
| 3 | AppRcvAppAcctdEarnedDiscountTaken | ACCTD_EARNED_DISCOUNT_TAKEN | — | — |
| 4 | AppRcvAppAcctdUnearnedDiscountTaken | ACCTD_UNEARNED_DISCOUNT_TAKEN | — | — |
| 5 | AppRcvAppAmountApplied | AMOUNT_APPLIED | — | — |
| 6 | AppRcvAppAmountAppliedFrom | AMOUNT_APPLIED_FROM | — | — |
| 7 | AppRcvAppApplicationRefId | APPLICATION_REF_ID | — | — |
| 8 | AppRcvAppApplicationRefNum | APPLICATION_REF_NUM | — | — |
| 9 | AppRcvAppApplicationRefReason | APPLICATION_REF_REASON | — | — |
| 10 | AppRcvAppApplicationRefType | APPLICATION_REF_TYPE | — | — |
| 11 | AppRcvAppApplicationRule | APPLICATION_RULE | — | — |
| 12 | AppRcvAppApplicationType | APPLICATION_TYPE | — | — |
| 13 | AppRcvAppAppliedCustomerTrxId | APPLIED_CUSTOMER_TRX_ID | — | — |
| 14 | AppRcvAppAppliedCustomerTrxLineId | APPLIED_CUSTOMER_TRX_LINE_ID | — | — |
| 15 | AppRcvAppAppliedPaymentScheduleId | APPLIED_PAYMENT_SCHEDULE_ID | — | — |
| 16 | AppRcvAppAppliedRecAppId | APPLIED_REC_APP_ID | — | — |
| 17 | AppRcvAppApplyDate | APPLY_DATE | — | — |
| 18 | AppRcvAppCashReceiptHistoryId | CASH_RECEIPT_HISTORY_ID | — | — |
| 19 | AppRcvAppCashReceiptId | CASH_RECEIPT_ID | — | — |
| 20 | AppRcvAppChargebackCustomerTrxId | CHARGEBACK_CUSTOMER_TRX_ID | — | — |
| 21 | AppRcvAppChargesEdiscounted | CHARGES_EDISCOUNTED | — | — |
| 22 | AppRcvAppChargesUediscounted | CHARGES_UEDISCOUNTED | — | — |
| 23 | AppRcvAppCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 24 | AppRcvAppComments | COMMENTS | — | — |
| 25 | AppRcvAppConfirmedFlag | CONFIRMED_FLAG | — | — |
| 26 | AppRcvAppConsInvId | CONS_INV_ID | — | — |
| 27 | AppRcvAppConsInvIdTo | CONS_INV_ID_TO | — | — |
| 28 | AppRcvAppCreatedBy | CREATED_BY | — | — |
| 29 | AppRcvAppCreationDate | CREATION_DATE | — | — |
| 30 | AppRcvAppCustomerReason | CUSTOMER_REASON | — | — |
| 31 | AppRcvAppCustomerReference | CUSTOMER_REFERENCE | — | — |
| 32 | AppRcvAppCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 33 | AppRcvAppDaysLate | DAYS_LATE | — | — |
| 34 | AppRcvAppDisplay | DISPLAY | — | — |
| 35 | AppRcvAppEarnedDiscountCcid | EARNED_DISCOUNT_CCID | — | — |
| 36 | AppRcvAppEarnedDiscountTaken | EARNED_DISCOUNT_TAKEN | — | — |
| 37 | AppRcvAppEdiscTaxAcctRule | EDISC_TAX_ACCT_RULE | — | — |
| 38 | AppRcvAppEventId | EVENT_ID | — | — |
| 39 | AppRcvAppExceptionReasonCode | EXCEPTION_REASON_CODE | — | — |
| 40 | AppRcvAppFreightApplied | FREIGHT_APPLIED | — | — |
| 41 | AppRcvAppFreightEdiscounted | FREIGHT_EDISCOUNTED | — | — |
| 42 | AppRcvAppFreightUediscounted | FREIGHT_UEDISCOUNTED | — | — |
| 43 | AppRcvAppGlDate | GL_DATE | — | — |
| 44 | AppRcvAppGlPostedDate | GL_POSTED_DATE | — | — |
| 45 | AppRcvAppLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 46 | AppRcvAppLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 47 | AppRcvAppLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 48 | AppRcvAppLineApplied | LINE_APPLIED | — | — |
| 49 | AppRcvAppLineEdiscounted | LINE_EDISCOUNTED | — | — |
| 50 | AppRcvAppLineUediscounted | LINE_UEDISCOUNTED | — | — |
| 51 | AppRcvAppLinkToCustomerTrxId | LINK_TO_CUSTOMER_TRX_ID | — | — |
| 52 | AppRcvAppLinkToTrxHistId | LINK_TO_TRX_HIST_ID | — | — |
| 53 | AppRcvAppObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 54 | AppRcvAppOnAccountCustomer | ON_ACCOUNT_CUSTOMER | — | — |
| 55 | AppRcvAppOrgId | ORG_ID | — | — |
| 56 | AppRcvAppPaymentScheduleId | PAYMENT_SCHEDULE_ID | — | — |
| 57 | AppRcvAppPaymentSetId | PAYMENT_SET_ID | — | — |
| 58 | AppRcvAppPostable | POSTABLE | — | — |
| 59 | AppRcvAppPostingControlId | POSTING_CONTROL_ID | — | — |
| 60 | AppRcvAppProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 61 | AppRcvAppProgramId | PROGRAM_ID | — | — |
| 62 | AppRcvAppProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 63 | AppRcvAppReceivableApplicationId | RECEIVABLE_APPLICATION_ID | — | — |
| 64 | AppRcvAppReceivablesChargesApplied | RECEIVABLES_CHARGES_APPLIED | — | — |
| 65 | AppRcvAppReceivablesTrxId | RECEIVABLES_TRX_ID | — | — |
| 66 | AppRcvAppRequestId | REQUEST_ID | — | — |
| 67 | AppRcvAppReversalGlDate | REVERSAL_GL_DATE | — | — |
| 68 | AppRcvAppRuleSetId | RULE_SET_ID | — | — |
| 69 | AppRcvAppSecondaryApplicationRefId | SECONDARY_APPLICATION_REF_ID | — | — |
| 70 | AppRcvAppSecondaryApplicationRefNum | SECONDARY_APPLICATION_REF_NUM | — | — |
| 71 | AppRcvAppSecondaryApplicationRefType | SECONDARY_APPLICATION_REF_TYPE | — | — |
| 72 | AppRcvAppSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 73 | AppRcvAppStatus | STATUS | — | — |
| 74 | AppRcvAppTaxApplied | TAX_APPLIED | — | — |
| 75 | AppRcvAppTaxCode | TAX_CODE | — | — |
| 76 | AppRcvAppTaxEdiscounted | TAX_EDISCOUNTED | — | — |
| 77 | AppRcvAppTaxUediscounted | TAX_UEDISCOUNTED | — | — |
| 78 | AppRcvAppTransToReceiptRate | TRANS_TO_RECEIPT_RATE | — | — |
| 79 | AppRcvAppUnearnedDiscountCcid | UNEARNED_DISCOUNT_CCID | — | — |
| 80 | AppRcvAppUnearnedDiscountTaken | UNEARNED_DISCOUNT_TAKEN | — | — |
| 81 | AppRcvAppUnediscTaxAcctRule | UNEDISC_TAX_ACCT_RULE | — | — |
| 82 | AppRcvAppUpgradeMethod | UPGRADE_METHOD | — | — |
| 83 | AppRcvAppUssglTransactionCode | USSGL_TRANSACTION_CODE | — | — |
| 84 | AppRcvAppUssglTransactionCodeContext | USSGL_TRANSACTION_CODE_CONTEXT | — | — |
| 85 | ReceivableApplicationAcctdAmountAppliedFrom | ACCTD_AMOUNT_APPLIED_FROM | — | ✅ |
| 86 | ReceivableApplicationAcctdAmountAppliedTo | ACCTD_AMOUNT_APPLIED_TO | — | ✅ |
| 87 | ReceivableApplicationAcctdEarnedDiscountTaken | ACCTD_EARNED_DISCOUNT_TAKEN | — | ✅ |
| 88 | ReceivableApplicationAcctdUnearnedDiscountTaken | ACCTD_UNEARNED_DISCOUNT_TAKEN | — | ✅ |
| 89 | ReceivableApplicationAmountApplied | AMOUNT_APPLIED | — | ✅ |
| 90 | ReceivableApplicationAmountAppliedFrom | AMOUNT_APPLIED_FROM | — | ✅ |
| 91 | ReceivableApplicationApplicationRefId | APPLICATION_REF_ID | — | — |
| 92 | ReceivableApplicationApplicationRefNum | APPLICATION_REF_NUM | — | — |
| 93 | ReceivableApplicationApplicationRefReason | APPLICATION_REF_REASON | — | — |
| 94 | ReceivableApplicationApplicationRefType | APPLICATION_REF_TYPE | — | — |
| 95 | ReceivableApplicationApplicationRule | APPLICATION_RULE | — | — |
| 96 | ReceivableApplicationApplicationType | APPLICATION_TYPE | — | ✅ |
| 97 | ReceivableApplicationAppliedCustomerTrxId | APPLIED_CUSTOMER_TRX_ID | — | — |
| 98 | ReceivableApplicationAppliedCustomerTrxLineId | APPLIED_CUSTOMER_TRX_LINE_ID | — | — |
| 99 | ReceivableApplicationAppliedPaymentScheduleId | APPLIED_PAYMENT_SCHEDULE_ID | — | ✅ |
| 100 | ReceivableApplicationAppliedRecAppId | APPLIED_REC_APP_ID | — | — |
| 101 | ReceivableApplicationApplyDate | APPLY_DATE | — | ✅ |
| 102 | ReceivableApplicationCashReceiptHistoryId | CASH_RECEIPT_HISTORY_ID | — | — |
| 103 | ReceivableApplicationCashReceiptId | CASH_RECEIPT_ID | — | ✅ |
| 104 | ReceivableApplicationChargebackCustomerTrxId | CHARGEBACK_CUSTOMER_TRX_ID | — | — |
| 105 | ReceivableApplicationChargesEdiscounted | CHARGES_EDISCOUNTED | — | ✅ |
| 106 | ReceivableApplicationChargesUediscounted | CHARGES_UEDISCOUNTED | — | ✅ |
| 107 | ReceivableApplicationCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 108 | ReceivableApplicationComments | COMMENTS | — | ✅ |
| 109 | ReceivableApplicationConfirmedFlag | CONFIRMED_FLAG | — | — |
| 110 | ReceivableApplicationConsInvId | CONS_INV_ID | — | — |
| 111 | ReceivableApplicationConsInvIdTo | CONS_INV_ID_TO | — | — |
| 112 | ReceivableApplicationCreatedBy | CREATED_BY | — | ✅ |
| 113 | ReceivableApplicationCreationDate | CREATION_DATE | — | ✅ |
| 114 | ReceivableApplicationCustomerReason | CUSTOMER_REASON | — | ✅ |
| 115 | ReceivableApplicationCustomerReference | CUSTOMER_REFERENCE | — | ✅ |
| 116 | ReceivableApplicationCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 117 | ReceivableApplicationDaysLate | DAYS_LATE | — | ✅ |
| 118 | ReceivableApplicationDisplay | DISPLAY | — | ✅ |
| 119 | ReceivableApplicationEarnedDiscountCcid | EARNED_DISCOUNT_CCID | — | — |
| 120 | ReceivableApplicationEarnedDiscountTaken | EARNED_DISCOUNT_TAKEN | — | ✅ |
| 121 | ReceivableApplicationEdiscTaxAcctRule | EDISC_TAX_ACCT_RULE | — | — |
| 122 | ReceivableApplicationEventId | EVENT_ID | — | ✅ |
| 123 | ReceivableApplicationExceptionReasonCode | EXCEPTION_REASON_CODE | — | ✅ |
| 124 | ReceivableApplicationFreightApplied | FREIGHT_APPLIED | — | ✅ |
| 125 | ReceivableApplicationFreightEdiscounted | FREIGHT_EDISCOUNTED | — | ✅ |
| 126 | ReceivableApplicationFreightUediscounted | FREIGHT_UEDISCOUNTED | — | ✅ |
| 127 | ReceivableApplicationGlDate | GL_DATE | — | ✅ |
| 128 | ReceivableApplicationGlPostedDate | GL_POSTED_DATE | — | ✅ |
| 129 | ReceivableApplicationId | RECEIVABLE_APPLICATION_ID | 🔑 | ✅ |
| 130 | ReceivableApplicationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 131 | ReceivableApplicationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 132 | ReceivableApplicationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 133 | ReceivableApplicationLineApplied | LINE_APPLIED | — | ✅ |
| 134 | ReceivableApplicationLineEdiscounted | LINE_EDISCOUNTED | — | ✅ |
| 135 | ReceivableApplicationLineUediscounted | LINE_UEDISCOUNTED | — | ✅ |
| 136 | ReceivableApplicationLinkToCustomerTrxId | LINK_TO_CUSTOMER_TRX_ID | — | — |
| 137 | ReceivableApplicationLinkToTrxHistId | LINK_TO_TRX_HIST_ID | — | — |
| 138 | ReceivableApplicationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 139 | ReceivableApplicationOnAccountCustomer | ON_ACCOUNT_CUSTOMER | — | — |
| 140 | ReceivableApplicationOrgId | ORG_ID | — | — |
| 141 | ReceivableApplicationPaymentScheduleId | PAYMENT_SCHEDULE_ID | — | — |
| 142 | ReceivableApplicationPaymentSetId | PAYMENT_SET_ID | — | — |
| 143 | ReceivableApplicationPostable | POSTABLE | — | ✅ |
| 144 | ReceivableApplicationPostingControlId | POSTING_CONTROL_ID | — | ✅ |
| 145 | ReceivableApplicationProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 146 | ReceivableApplicationProgramId | PROGRAM_ID | — | — |
| 147 | ReceivableApplicationProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 148 | ReceivableApplicationReceivablesChargesApplied | RECEIVABLES_CHARGES_APPLIED | — | ✅ |
| 149 | ReceivableApplicationReceivablesTrxId | RECEIVABLES_TRX_ID | — | — |
| 150 | ReceivableApplicationRequestId | REQUEST_ID | — | — |
| 151 | ReceivableApplicationReversalGlDate | REVERSAL_GL_DATE | — | ✅ |
| 152 | ReceivableApplicationRuleSetId | RULE_SET_ID | — | — |
| 153 | ReceivableApplicationSecondaryApplicationRefId | SECONDARY_APPLICATION_REF_ID | — | — |
| 154 | ReceivableApplicationSecondaryApplicationRefNum | SECONDARY_APPLICATION_REF_NUM | — | — |
| 155 | ReceivableApplicationSecondaryApplicationRefType | SECONDARY_APPLICATION_REF_TYPE | — | — |
| 156 | ReceivableApplicationSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 157 | ReceivableApplicationStatus | STATUS | — | ✅ |
| 158 | ReceivableApplicationTaxApplied | TAX_APPLIED | — | ✅ |
| 159 | ReceivableApplicationTaxCode | TAX_CODE | — | ✅ |
| 160 | ReceivableApplicationTaxEdiscounted | TAX_EDISCOUNTED | — | ✅ |
| 161 | ReceivableApplicationTaxUediscounted | TAX_UEDISCOUNTED | — | ✅ |
| 162 | ReceivableApplicationTransToReceiptRate | TRANS_TO_RECEIPT_RATE | — | ✅ |
| 163 | ReceivableApplicationUnearnedDiscountCcid | UNEARNED_DISCOUNT_CCID | — | — |
| 164 | ReceivableApplicationUnearnedDiscountTaken | UNEARNED_DISCOUNT_TAKEN | — | ✅ |
| 165 | ReceivableApplicationUnediscTaxAcctRule | UNEDISC_TAX_ACCT_RULE | — | — |
| 166 | ReceivableApplicationUpgradeMethod | UPGRADE_METHOD | — | — |
| 167 | ReceivableApplicationUssglTransactionCode | USSGL_TRANSACTION_CODE | — | — |
| 168 | ReceivableApplicationUssglTransactionCodeContext | USSGL_TRANSACTION_CODE_CONTEXT | — | — |

### [[ce_bank_acct_uses_all|CE_BANK_ACCT_USES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankAcctUseApUseEnableFlag | AP_USE_ENABLE_FLAG | — | — |
| 2 | BankAcctUseArUseEnableFlag | AR_USE_ENABLE_FLAG | — | — |
| 3 | BankAcctUseAuthorizedFlag | AUTHORIZED_FLAG | — | — |
| 4 | BankAcctUseBankAccountId | BANK_ACCOUNT_ID | — | — |
| 5 | BankAcctUseBankAcctUseId | BANK_ACCT_USE_ID | — | — |
| 6 | BankAcctUseDefaultAccountFlag | DEFAULT_ACCOUNT_FLAG | — | — |
| 7 | BankAcctUseEftScriptName | EFT_SCRIPT_NAME | — | — |
| 8 | BankAcctUseEndDate | END_DATE | — | — |
| 9 | BankAcctUseFundingLimitCode | FUNDING_LIMIT_CODE | — | — |
| 10 | BankAcctUseInvestmentLimitCode | INVESTMENT_LIMIT_CODE | — | — |
| 11 | BankAcctUseLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 12 | BankAcctUseOrgId | ORG_ID | — | — |
| 13 | BankAcctUseOrgPartyId | ORG_PARTY_ID | — | — |
| 14 | BankAcctUsePayUseEnableFlag | PAY_USE_ENABLE_FLAG | — | — |
| 15 | BankAcctUsePortfolioCode | PORTFOLIO_CODE | — | — |
| 16 | BankAcctUsePricingModel | PRICING_MODEL | — | — |
| 17 | BankAcctUsePrimaryFlag | PRIMARY_FLAG | — | — |
| 18 | BankAcctUseProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 19 | BankAcctUseProgramId | PROGRAM_ID | — | — |
| 20 | BankAcctUseProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 21 | BankAcctUseRequestId | REQUEST_ID | — | — |
| 22 | BankAcctUseXtrBankAccountReference | XTR_BANK_ACCOUNT_REFERENCE | — | — |
| 23 | BankAcctUseXtrDefaultSettlementFlag | XTR_DEFAULT_SETTLEMENT_FLAG | — | — |
| 24 | BankAcctUseXtrUseEnableFlag | XTR_USE_ENABLE_FLAG | — | — |

### [[ce_bank_branches_v|CE_BANK_BRANCHES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankBranchAddressLine1 | ADDRESS_LINE1 | — | — |
| 2 | BankBranchAddressLine2 | ADDRESS_LINE2 | — | — |
| 3 | BankBranchAddressLine3 | ADDRESS_LINE3 | — | — |
| 4 | BankBranchAddressLine4 | ADDRESS_LINE4 | — | — |
| 5 | BankBranchBankBranchName | BANK_BRANCH_NAME | — | ✅ |
| 6 | BankBranchBankBranchNameAlt | BANK_BRANCH_NAME_ALT | — | — |
| 7 | BankBranchBankBranchType | BANK_BRANCH_TYPE | — | — |
| 8 | BankBranchBankCode | BANK_CODE | — | — |
| 9 | BankBranchBankHomeCountry | BANK_HOME_COUNTRY | — | — |
| 10 | BankBranchBankInstitutionType | BANK_INSTITUTION_TYPE | — | — |
| 11 | BankBranchBankName | BANK_NAME | — | — |
| 12 | BankBranchBankNameAlt | BANK_NAME_ALT | — | — |
| 13 | BankBranchBankNumber | BANK_NUMBER | — | — |
| 14 | BankBranchBankPartyId | BANK_PARTY_ID | — | — |
| 15 | BankBranchBranchNumber | BRANCH_NUMBER | — | — |
| 16 | BankBranchBranchPartyId | BRANCH_PARTY_ID | — | — |
| 17 | BankBranchCity | CITY | — | — |
| 18 | BankBranchCountry | COUNTRY | — | — |
| 19 | BankBranchCountryName | COUNTRY_NAME | — | — |
| 20 | BankBranchDescription | DESCRIPTION | — | — |
| 21 | BankBranchEdiIdNumber | EDI_ID_NUMBER | — | — |
| 22 | BankBranchEdiLocation | EDI_LOCATION | — | — |
| 23 | BankBranchEftSwiftCode | EFT_SWIFT_CODE | — | — |
| 24 | BankBranchEftUserNumber | EFT_USER_NUMBER | — | — |
| 25 | BankBranchEndDate | END_DATE | — | — |
| 26 | BankBranchPkId | PK_ID | — | — |
| 27 | BankBranchProvince | PROVINCE | — | — |
| 28 | BankBranchRfc | RFC | — | — |
| 29 | BankBranchRowId | ROW_ID | — | — |
| 30 | BankBranchShortBankName | SHORT_BANK_NAME | — | — |
| 31 | BankBranchStartDate | START_DATE | — | — |
| 32 | BankBranchState | STATE | — | — |
| 33 | BankBranchZip | ZIP | — | — |

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
| 2 | TrxHeaderBusinessUnitId | BU_ID | — | — |
| 3 | TrxHeaderBusinessUnitName | BU_NAME | — | ✅ |

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

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 2 | LedgersLedgerId | LEDGER_ID | — | — |

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
| 1 | IbyExtBankAccountsAccountClassification | ACCOUNT_CLASSIFICATION | — | — |
| 2 | IbyExtBankAccountsAccountSuffix | ACCOUNT_SUFFIX | — | — |
| 3 | IbyExtBankAccountsAgencyLocationCode | AGENCY_LOCATION_CODE | — | — |
| 4 | IbyExtBankAccountsBaMaskSetting | BA_MASK_SETTING | — | — |
| 5 | IbyExtBankAccountsBaNumElecSecSegmentId | BA_NUM_ELEC_SEC_SEGMENT_ID | — | — |
| 6 | IbyExtBankAccountsBaNumSecSegmentId | BA_NUM_SEC_SEGMENT_ID | — | — |
| 7 | IbyExtBankAccountsBaUnmaskLength | BA_UNMASK_LENGTH | — | — |
| 8 | IbyExtBankAccountsBankAccountName | BANK_ACCOUNT_NAME | — | ✅ |
| 9 | IbyExtBankAccountsBankAccountNameAlt | BANK_ACCOUNT_NAME_ALT | — | — |
| 10 | IbyExtBankAccountsBankAccountNum | BANK_ACCOUNT_NUM | — | ✅ |
| 11 | IbyExtBankAccountsBankAccountNumElectronic | BANK_ACCOUNT_NUM_ELECTRONIC | — | — |
| 12 | IbyExtBankAccountsBankAccountNumHash1 | BANK_ACCOUNT_NUM_HASH1 | — | — |
| 13 | IbyExtBankAccountsBankAccountNumHash2 | BANK_ACCOUNT_NUM_HASH2 | — | — |
| 14 | IbyExtBankAccountsBankAccountType | BANK_ACCOUNT_TYPE | — | — |
| 15 | IbyExtBankAccountsBankId | BANK_ID | — | — |
| 16 | IbyExtBankAccountsBranchId | BRANCH_ID | — | — |
| 17 | IbyExtBankAccountsCheckDigits | CHECK_DIGITS | — | — |
| 18 | IbyExtBankAccountsCountryCode | COUNTRY_CODE | — | — |
| 19 | IbyExtBankAccountsCurrencyCode | CURRENCY_CODE | — | — |
| 20 | IbyExtBankAccountsDescription | DESCRIPTION | — | — |
| 21 | IbyExtBankAccountsEncrypted | ENCRYPTED | — | — |
| 22 | IbyExtBankAccountsEndDate | END_DATE | — | — |
| 23 | IbyExtBankAccountsExchangeRate | EXCHANGE_RATE | — | — |
| 24 | IbyExtBankAccountsExchangeRateAgreementNum | EXCHANGE_RATE_AGREEMENT_NUM | — | — |
| 25 | IbyExtBankAccountsExchangeRateAgreementType | EXCHANGE_RATE_AGREEMENT_TYPE | — | — |
| 26 | IbyExtBankAccountsExtBankAccountId | EXT_BANK_ACCOUNT_ID | — | — |
| 27 | IbyExtBankAccountsForeignPaymentUseFlag | FOREIGN_PAYMENT_USE_FLAG | — | — |
| 28 | IbyExtBankAccountsHedgingContractReference | HEDGING_CONTRACT_REFERENCE | — | — |
| 29 | IbyExtBankAccountsIban | IBAN | — | — |
| 30 | IbyExtBankAccountsIbanHash1 | IBAN_HASH1 | — | — |
| 31 | IbyExtBankAccountsIbanHash2 | IBAN_HASH2 | — | — |
| 32 | IbyExtBankAccountsIbanSecSegmentId | IBAN_SEC_SEGMENT_ID | — | — |
| 33 | IbyExtBankAccountsMaskedBankAccountNum | MASKED_BANK_ACCOUNT_NUM | — | — |
| 34 | IbyExtBankAccountsMaskedIban | MASKED_IBAN | — | — |
| 35 | IbyExtBankAccountsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 36 | IbyExtBankAccountsPaymentFactorFlag | PAYMENT_FACTOR_FLAG | — | — |
| 37 | IbyExtBankAccountsProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 38 | IbyExtBankAccountsProgramId | PROGRAM_ID | — | — |
| 39 | IbyExtBankAccountsProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 40 | IbyExtBankAccountsRequestId | REQUEST_ID | — | — |
| 41 | IbyExtBankAccountsSaltVersion | SALT_VERSION | — | — |
| 42 | IbyExtBankAccountsSecondaryAccountReference | SECONDARY_ACCOUNT_REFERENCE | — | — |
| 43 | IbyExtBankAccountsShortAcctName | SHORT_ACCT_NAME | — | — |
| 44 | IbyExtBankAccountsStartDate | START_DATE | — | — |

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
| 24 | RAPersonCreatedByDisplayName | DISPLAY_NAME | — | — |
| 25 | RAPersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 26 | RAPersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 27 | RAPersonCreatedByPersonId | PERSON_ID | — | — |
| 28 | RAPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 29 | RAPersonUpdatedByDisplayName | DISPLAY_NAME | — | — |
| 30 | RAPersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 31 | RAPersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 32 | RAPersonUpdatedByPersonId | PERSON_ID | — | — |
| 33 | RAPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 3 | RAUserCreatedByPersonId | PERSON_ID | — | — |
| 4 | RAUserCreatedByUserGuid | USER_GUID | — | — |
| 5 | RAUserCreatedByUserId | USER_ID | — | — |
| 6 | RAUserCreatedByUsername | USERNAME | — | — |
| 7 | RAUserUpdatedByPersonId | PERSON_ID | — | — |
| 8 | RAUserUpdatedByUserGuid | USER_GUID | — | — |
| 9 | RAUserUpdatedByUserId | USER_ID | — | — |
| 10 | RAUserUpdatedByUsername | USERNAME | — | — |
| 11 | UserCreatedByUserGuid | USER_GUID | — | — |
| 12 | UserCreatedByUserId | USER_ID | — | — |
| 13 | UserCreatedByUsername | USERNAME | — | — |
| 14 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 15 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 16 | UserUpdatedByUserId | USER_ID | — | — |
| 17 | UserUpdatedByUsername | USERNAME | — | — |

### [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChrgBkTrxHdrAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 2 | ChrgBkTrxHdrAgreementId | AGREEMENT_ID | — | — |
| 3 | ChrgBkTrxHdrApplicationId | APPLICATION_ID | — | — |
| 4 | ChrgBkTrxHdrApprovalCode | APPROVAL_CODE | — | — |
| 5 | ChrgBkTrxHdrAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 6 | ChrgBkTrxHdrBatchId | BATCH_ID | — | — |
| 7 | ChrgBkTrxHdrBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 8 | ChrgBkTrxHdrBillTemplateId | BILL_TEMPLATE_ID | — | — |
| 9 | ChrgBkTrxHdrBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 10 | ChrgBkTrxHdrBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 11 | ChrgBkTrxHdrBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 12 | ChrgBkTrxHdrBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 13 | ChrgBkTrxHdrBillingDate | BILLING_DATE | — | — |
| 14 | ChrgBkTrxHdrBrAmount | BR_AMOUNT | — | — |
| 15 | ChrgBkTrxHdrBrOnHoldFlag | BR_ON_HOLD_FLAG | — | — |
| 16 | ChrgBkTrxHdrBrUnpaidFlag | BR_UNPAID_FLAG | — | — |
| 17 | ChrgBkTrxHdrCcErrorCode | CC_ERROR_CODE | — | — |
| 18 | ChrgBkTrxHdrCcErrorFlag | CC_ERROR_FLAG | — | — |
| 19 | ChrgBkTrxHdrCcErrorText | CC_ERROR_TEXT | — | — |
| 20 | ChrgBkTrxHdrCompleteFlag | COMPLETE_FLAG | — | — |
| 21 | ChrgBkTrxHdrContractId | CONTRACT_ID | — | — |
| 22 | ChrgBkTrxHdrCreatedBy | CREATED_BY | — | — |
| 23 | ChrgBkTrxHdrCreatedFrom | CREATED_FROM | — | — |
| 24 | ChrgBkTrxHdrCreationDate | CREATION_DATE | — | — |
| 25 | ChrgBkTrxHdrCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | — |
| 26 | ChrgBkTrxHdrCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | — |
| 27 | ChrgBkTrxHdrCtReference | CT_REFERENCE | — | — |
| 28 | ChrgBkTrxHdrCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 29 | ChrgBkTrxHdrCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 30 | ChrgBkTrxHdrCustomerReference | CUSTOMER_REFERENCE | — | — |
| 31 | ChrgBkTrxHdrCustomerReferenceDate | CUSTOMER_REFERENCE_DATE | — | — |
| 32 | ChrgBkTrxHdrCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 33 | ChrgBkTrxHdrDefaultTaxExemptFlag | DEFAULT_TAX_EXEMPT_FLAG | — | — |
| 34 | ChrgBkTrxHdrDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 35 | ChrgBkTrxHdrDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 36 | ChrgBkTrxHdrDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 37 | ChrgBkTrxHdrDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 38 | ChrgBkTrxHdrDraweeBankAccountId | DRAWEE_BANK_ACCOUNT_ID | — | — |
| 39 | ChrgBkTrxHdrDraweeContactId | DRAWEE_CONTACT_ID | — | — |
| 40 | ChrgBkTrxHdrDraweeId | DRAWEE_ID | — | — |
| 41 | ChrgBkTrxHdrDraweeSiteUseId | DRAWEE_SITE_USE_ID | — | — |
| 42 | ChrgBkTrxHdrEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 43 | ChrgBkTrxHdrEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 44 | ChrgBkTrxHdrEndDateCommitment | END_DATE_COMMITMENT | — | — |
| 45 | ChrgBkTrxHdrExchangeDate | EXCHANGE_DATE | — | — |
| 46 | ChrgBkTrxHdrExchangeRate | EXCHANGE_RATE | — | — |
| 47 | ChrgBkTrxHdrExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 48 | ChrgBkTrxHdrFinanceCharges | FINANCE_CHARGES | — | — |
| 49 | ChrgBkTrxHdrFobPoint | FOB_POINT | — | — |
| 50 | ChrgBkTrxHdrInitialCustomerTrxId | INITIAL_CUSTOMER_TRX_ID | — | — |
| 51 | ChrgBkTrxHdrIntercompanyFlag | INTERCOMPANY_FLAG | — | — |
| 52 | ChrgBkTrxHdrInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 53 | ChrgBkTrxHdrInterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | — |
| 54 | ChrgBkTrxHdrInterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | — |
| 55 | ChrgBkTrxHdrInterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | — |
| 56 | ChrgBkTrxHdrInterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | — |
| 57 | ChrgBkTrxHdrInterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | — |
| 58 | ChrgBkTrxHdrInterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | — |
| 59 | ChrgBkTrxHdrInterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | — |
| 60 | ChrgBkTrxHdrInterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | — |
| 61 | ChrgBkTrxHdrInterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | — |
| 62 | ChrgBkTrxHdrInterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | — |
| 63 | ChrgBkTrxHdrInterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | — |
| 64 | ChrgBkTrxHdrInterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | — |
| 65 | ChrgBkTrxHdrInterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | — |
| 66 | ChrgBkTrxHdrInterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | — |
| 67 | ChrgBkTrxHdrInterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | — |
| 68 | ChrgBkTrxHdrInterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | — |
| 69 | ChrgBkTrxHdrInternalNotes | INTERNAL_NOTES | — | — |
| 70 | ChrgBkTrxHdrInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 71 | ChrgBkTrxHdrInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 72 | ChrgBkTrxHdrLastPrintedSequenceNum | LAST_PRINTED_SEQUENCE_NUM | — | — |
| 73 | ChrgBkTrxHdrLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 74 | ChrgBkTrxHdrLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 75 | ChrgBkTrxHdrLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 76 | ChrgBkTrxHdrLateChargesAssessed | LATE_CHARGES_ASSESSED | — | — |
| 77 | ChrgBkTrxHdrLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 78 | ChrgBkTrxHdrObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 79 | ChrgBkTrxHdrOldTrxNumber | OLD_TRX_NUMBER | — | — |
| 80 | ChrgBkTrxHdrOrgId | ORG_ID | — | — |
| 81 | ChrgBkTrxHdrOrigSystemBatchName | ORIG_SYSTEM_BATCH_NAME | — | — |
| 82 | ChrgBkTrxHdrOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 83 | ChrgBkTrxHdrPayingCustomerId | PAYING_CUSTOMER_ID | — | — |
| 84 | ChrgBkTrxHdrPayingSiteUseId | PAYING_SITE_USE_ID | — | — |
| 85 | ChrgBkTrxHdrPaymentAttributes | PAYMENT_ATTRIBUTES | — | — |
| 86 | ChrgBkTrxHdrPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 87 | ChrgBkTrxHdrPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 88 | ChrgBkTrxHdrPostRequestId | POST_REQUEST_ID | — | — |
| 89 | ChrgBkTrxHdrPostingControlId | POSTING_CONTROL_ID | — | — |
| 90 | ChrgBkTrxHdrPrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 91 | ChrgBkTrxHdrPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 92 | ChrgBkTrxHdrPrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | — |
| 93 | ChrgBkTrxHdrPrintingCount | PRINTING_COUNT | — | — |
| 94 | ChrgBkTrxHdrPrintingLastPrinted | PRINTING_LAST_PRINTED | — | — |
| 95 | ChrgBkTrxHdrPrintingOption | PRINTING_OPTION | — | — |
| 96 | ChrgBkTrxHdrPrintingOriginalDate | PRINTING_ORIGINAL_DATE | — | — |
| 97 | ChrgBkTrxHdrPrintingPending | PRINTING_PENDING | — | — |
| 98 | ChrgBkTrxHdrProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 99 | ChrgBkTrxHdrProgramId | PROGRAM_ID | — | — |
| 100 | ChrgBkTrxHdrProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 101 | ChrgBkTrxHdrPurchaseOrder | PURCHASE_ORDER | — | — |
| 102 | ChrgBkTrxHdrPurchaseOrderDate | PURCHASE_ORDER_DATE | — | — |
| 103 | ChrgBkTrxHdrPurchaseOrderRevision | PURCHASE_ORDER_REVISION | — | — |
| 104 | ChrgBkTrxHdrRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 105 | ChrgBkTrxHdrReasonCode | REASON_CODE | — | — |
| 106 | ChrgBkTrxHdrReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 107 | ChrgBkTrxHdrRecurredFromTrxNumber | RECURRED_FROM_TRX_NUMBER | — | — |
| 108 | ChrgBkTrxHdrRelatedBatchSourceSeqId | RELATED_BATCH_SOURCE_SEQ_ID | — | — |
| 109 | ChrgBkTrxHdrRelatedCustomerTrxId | RELATED_CUSTOMER_TRX_ID | — | — |
| 110 | ChrgBkTrxHdrRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 111 | ChrgBkTrxHdrRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 112 | ChrgBkTrxHdrRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 113 | ChrgBkTrxHdrRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 114 | ChrgBkTrxHdrRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 115 | ChrgBkTrxHdrRequestId | REQUEST_ID | — | — |
| 116 | ChrgBkTrxHdrReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 117 | ChrgBkTrxHdrSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 118 | ChrgBkTrxHdrShipDateActual | SHIP_DATE_ACTUAL | — | — |
| 119 | ChrgBkTrxHdrShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 120 | ChrgBkTrxHdrShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 121 | ChrgBkTrxHdrShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 122 | ChrgBkTrxHdrShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 123 | ChrgBkTrxHdrShipVia | SHIP_VIA | — | — |
| 124 | ChrgBkTrxHdrShipmentId | SHIPMENT_ID | — | — |
| 125 | ChrgBkTrxHdrSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 126 | ChrgBkTrxHdrSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 127 | ChrgBkTrxHdrSoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | — |
| 128 | ChrgBkTrxHdrSourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 129 | ChrgBkTrxHdrSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 130 | ChrgBkTrxHdrSpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 131 | ChrgBkTrxHdrStartDateCommitment | START_DATE_COMMITMENT | — | — |
| 132 | ChrgBkTrxHdrStatusTrx | STATUS_TRX | — | — |
| 133 | ChrgBkTrxHdrTermDueDate | TERM_DUE_DATE | — | — |
| 134 | ChrgBkTrxHdrTermId | TERM_ID | — | — |
| 135 | ChrgBkTrxHdrTerritoryId | TERRITORY_ID | — | — |
| 136 | ChrgBkTrxHdrTrxClass | TRX_CLASS | — | — |
| 137 | ChrgBkTrxHdrTrxDate | TRX_DATE | — | — |
| 138 | ChrgBkTrxHdrTrxNumber | TRX_NUMBER | — | — |
| 139 | ChrgBkTrxHdrUpgradeMethod | UPGRADE_METHOD | — | — |
| 140 | ChrgBkTrxHdrWaybillNumber | WAYBILL_NUMBER | — | — |
| 141 | ChrgBkTrxHdrWhUpdateDate | WH_UPDATE_DATE | — | — |
| 142 | LinkToTrxHdrAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 143 | LinkToTrxHdrAgreementId | AGREEMENT_ID | — | — |
| 144 | LinkToTrxHdrApplicationId | APPLICATION_ID | — | — |
| 145 | LinkToTrxHdrApprovalCode | APPROVAL_CODE | — | — |
| 146 | LinkToTrxHdrAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 147 | LinkToTrxHdrBatchId | BATCH_ID | — | — |
| 148 | LinkToTrxHdrBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 149 | LinkToTrxHdrBillTemplateId | BILL_TEMPLATE_ID | — | — |
| 150 | LinkToTrxHdrBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 151 | LinkToTrxHdrBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 152 | LinkToTrxHdrBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 153 | LinkToTrxHdrBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 154 | LinkToTrxHdrBillingDate | BILLING_DATE | — | — |
| 155 | LinkToTrxHdrBrAmount | BR_AMOUNT | — | — |
| 156 | LinkToTrxHdrBrOnHoldFlag | BR_ON_HOLD_FLAG | — | — |
| 157 | LinkToTrxHdrBrUnpaidFlag | BR_UNPAID_FLAG | — | — |
| 158 | LinkToTrxHdrCcErrorCode | CC_ERROR_CODE | — | — |
| 159 | LinkToTrxHdrCcErrorFlag | CC_ERROR_FLAG | — | — |
| 160 | LinkToTrxHdrCcErrorText | CC_ERROR_TEXT | — | — |
| 161 | LinkToTrxHdrCompleteFlag | COMPLETE_FLAG | — | — |
| 162 | LinkToTrxHdrContractId | CONTRACT_ID | — | — |
| 163 | LinkToTrxHdrCreatedBy | CREATED_BY | — | — |
| 164 | LinkToTrxHdrCreatedFrom | CREATED_FROM | — | — |
| 165 | LinkToTrxHdrCreationDate | CREATION_DATE | — | — |
| 166 | LinkToTrxHdrCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | — |
| 167 | LinkToTrxHdrCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | — |
| 168 | LinkToTrxHdrCtReference | CT_REFERENCE | — | — |
| 169 | LinkToTrxHdrCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 170 | LinkToTrxHdrCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 171 | LinkToTrxHdrCustomerReference | CUSTOMER_REFERENCE | — | — |
| 172 | LinkToTrxHdrCustomerReferenceDate | CUSTOMER_REFERENCE_DATE | — | — |
| 173 | LinkToTrxHdrCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 174 | LinkToTrxHdrDefaultTaxExemptFlag | DEFAULT_TAX_EXEMPT_FLAG | — | — |
| 175 | LinkToTrxHdrDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 176 | LinkToTrxHdrDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 177 | LinkToTrxHdrDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 178 | LinkToTrxHdrDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 179 | LinkToTrxHdrDraweeBankAccountId | DRAWEE_BANK_ACCOUNT_ID | — | — |
| 180 | LinkToTrxHdrDraweeContactId | DRAWEE_CONTACT_ID | — | — |
| 181 | LinkToTrxHdrDraweeId | DRAWEE_ID | — | — |
| 182 | LinkToTrxHdrDraweeSiteUseId | DRAWEE_SITE_USE_ID | — | — |
| 183 | LinkToTrxHdrEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 184 | LinkToTrxHdrEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 185 | LinkToTrxHdrEndDateCommitment | END_DATE_COMMITMENT | — | — |
| 186 | LinkToTrxHdrExchangeDate | EXCHANGE_DATE | — | — |
| 187 | LinkToTrxHdrExchangeRate | EXCHANGE_RATE | — | — |
| 188 | LinkToTrxHdrExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 189 | LinkToTrxHdrFinanceCharges | FINANCE_CHARGES | — | — |
| 190 | LinkToTrxHdrFobPoint | FOB_POINT | — | — |
| 191 | LinkToTrxHdrInitialCustomerTrxId | INITIAL_CUSTOMER_TRX_ID | — | — |
| 192 | LinkToTrxHdrIntercompanyFlag | INTERCOMPANY_FLAG | — | — |
| 193 | LinkToTrxHdrInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 194 | LinkToTrxHdrInterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | — |
| 195 | LinkToTrxHdrInterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | — |
| 196 | LinkToTrxHdrInterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | — |
| 197 | LinkToTrxHdrInterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | — |
| 198 | LinkToTrxHdrInterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | — |
| 199 | LinkToTrxHdrInterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | — |
| 200 | LinkToTrxHdrInterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | — |
| 201 | LinkToTrxHdrInterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | — |
| 202 | LinkToTrxHdrInterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | — |
| 203 | LinkToTrxHdrInterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | — |
| 204 | LinkToTrxHdrInterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | — |
| 205 | LinkToTrxHdrInterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | — |
| 206 | LinkToTrxHdrInterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | — |
| 207 | LinkToTrxHdrInterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | — |
| 208 | LinkToTrxHdrInterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | — |
| 209 | LinkToTrxHdrInterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | — |
| 210 | LinkToTrxHdrInternalNotes | INTERNAL_NOTES | — | — |
| 211 | LinkToTrxHdrInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 212 | LinkToTrxHdrInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 213 | LinkToTrxHdrLastPrintedSequenceNum | LAST_PRINTED_SEQUENCE_NUM | — | — |
| 214 | LinkToTrxHdrLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 215 | LinkToTrxHdrLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 216 | LinkToTrxHdrLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 217 | LinkToTrxHdrLateChargesAssessed | LATE_CHARGES_ASSESSED | — | — |
| 218 | LinkToTrxHdrLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 219 | LinkToTrxHdrObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 220 | LinkToTrxHdrOldTrxNumber | OLD_TRX_NUMBER | — | — |
| 221 | LinkToTrxHdrOrgId | ORG_ID | — | — |
| 222 | LinkToTrxHdrOrigSystemBatchName | ORIG_SYSTEM_BATCH_NAME | — | — |
| 223 | LinkToTrxHdrOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 224 | LinkToTrxHdrPayingCustomerId | PAYING_CUSTOMER_ID | — | — |
| 225 | LinkToTrxHdrPayingSiteUseId | PAYING_SITE_USE_ID | — | — |
| 226 | LinkToTrxHdrPaymentAttributes | PAYMENT_ATTRIBUTES | — | — |
| 227 | LinkToTrxHdrPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 228 | LinkToTrxHdrPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 229 | LinkToTrxHdrPostRequestId | POST_REQUEST_ID | — | — |
| 230 | LinkToTrxHdrPostingControlId | POSTING_CONTROL_ID | — | — |
| 231 | LinkToTrxHdrPrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 232 | LinkToTrxHdrPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 233 | LinkToTrxHdrPrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | — |
| 234 | LinkToTrxHdrPrintingCount | PRINTING_COUNT | — | — |
| 235 | LinkToTrxHdrPrintingLastPrinted | PRINTING_LAST_PRINTED | — | — |
| 236 | LinkToTrxHdrPrintingOption | PRINTING_OPTION | — | — |
| 237 | LinkToTrxHdrPrintingOriginalDate | PRINTING_ORIGINAL_DATE | — | — |
| 238 | LinkToTrxHdrPrintingPending | PRINTING_PENDING | — | — |
| 239 | LinkToTrxHdrProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 240 | LinkToTrxHdrProgramId | PROGRAM_ID | — | — |
| 241 | LinkToTrxHdrProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 242 | LinkToTrxHdrPurchaseOrder | PURCHASE_ORDER | — | — |
| 243 | LinkToTrxHdrPurchaseOrderDate | PURCHASE_ORDER_DATE | — | — |
| 244 | LinkToTrxHdrPurchaseOrderRevision | PURCHASE_ORDER_REVISION | — | — |
| 245 | LinkToTrxHdrRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 246 | LinkToTrxHdrReasonCode | REASON_CODE | — | — |
| 247 | LinkToTrxHdrReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 248 | LinkToTrxHdrRecurredFromTrxNumber | RECURRED_FROM_TRX_NUMBER | — | — |
| 249 | LinkToTrxHdrRelatedBatchSourceSeqId | RELATED_BATCH_SOURCE_SEQ_ID | — | — |
| 250 | LinkToTrxHdrRelatedCustomerTrxId | RELATED_CUSTOMER_TRX_ID | — | — |
| 251 | LinkToTrxHdrRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 252 | LinkToTrxHdrRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 253 | LinkToTrxHdrRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 254 | LinkToTrxHdrRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 255 | LinkToTrxHdrRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 256 | LinkToTrxHdrRequestId | REQUEST_ID | — | — |
| 257 | LinkToTrxHdrReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 258 | LinkToTrxHdrSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 259 | LinkToTrxHdrShipDateActual | SHIP_DATE_ACTUAL | — | — |
| 260 | LinkToTrxHdrShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 261 | LinkToTrxHdrShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 262 | LinkToTrxHdrShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 263 | LinkToTrxHdrShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 264 | LinkToTrxHdrShipVia | SHIP_VIA | — | — |
| 265 | LinkToTrxHdrShipmentId | SHIPMENT_ID | — | — |
| 266 | LinkToTrxHdrSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 267 | LinkToTrxHdrSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 268 | LinkToTrxHdrSoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | — |
| 269 | LinkToTrxHdrSourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 270 | LinkToTrxHdrSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 271 | LinkToTrxHdrSpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 272 | LinkToTrxHdrStartDateCommitment | START_DATE_COMMITMENT | — | — |
| 273 | LinkToTrxHdrStatusTrx | STATUS_TRX | — | — |
| 274 | LinkToTrxHdrTermDueDate | TERM_DUE_DATE | — | — |
| 275 | LinkToTrxHdrTermId | TERM_ID | — | — |
| 276 | LinkToTrxHdrTerritoryId | TERRITORY_ID | — | — |
| 277 | LinkToTrxHdrTrxClass | TRX_CLASS | — | — |
| 278 | LinkToTrxHdrTrxDate | TRX_DATE | — | — |
| 279 | LinkToTrxHdrTrxNumber | TRX_NUMBER | — | — |
| 280 | LinkToTrxHdrUpgradeMethod | UPGRADE_METHOD | — | — |
| 281 | LinkToTrxHdrWaybillNumber | WAYBILL_NUMBER | — | — |
| 282 | LinkToTrxHdrWhUpdateDate | WH_UPDATE_DATE | — | — |
| 283 | TrxHdrCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 284 | TrxHdrTrxNumber | TRX_NUMBER | — | ✅ |
| 285 | TrxHeaderAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 286 | TrxHeaderAgreementId | AGREEMENT_ID | — | — |
| 287 | TrxHeaderApplicationId | APPLICATION_ID | — | — |
| 288 | TrxHeaderApprovalCode | APPROVAL_CODE | — | — |
| 289 | TrxHeaderAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 290 | TrxHeaderBatchId | BATCH_ID | — | — |
| 291 | TrxHeaderBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 292 | TrxHeaderBillTemplateId | BILL_TEMPLATE_ID | — | — |
| 293 | TrxHeaderBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 294 | TrxHeaderBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 295 | TrxHeaderBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 296 | TrxHeaderBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 297 | TrxHeaderBillingDate | BILLING_DATE | — | — |
| 298 | TrxHeaderBrAmount | BR_AMOUNT | — | — |
| 299 | TrxHeaderBrOnHoldFlag | BR_ON_HOLD_FLAG | — | — |
| 300 | TrxHeaderBrUnpaidFlag | BR_UNPAID_FLAG | — | — |
| 301 | TrxHeaderCcErrorCode | CC_ERROR_CODE | — | — |
| 302 | TrxHeaderCcErrorFlag | CC_ERROR_FLAG | — | — |
| 303 | TrxHeaderCcErrorText | CC_ERROR_TEXT | — | — |
| 304 | TrxHeaderCompleteFlag | COMPLETE_FLAG | — | — |
| 305 | TrxHeaderContractId | CONTRACT_ID | — | — |
| 306 | TrxHeaderCreatedBy | CREATED_BY | — | — |
| 307 | TrxHeaderCreatedFrom | CREATED_FROM | — | — |
| 308 | TrxHeaderCreationDate | CREATION_DATE | — | — |
| 309 | TrxHeaderCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | — |
| 310 | TrxHeaderCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | — |
| 311 | TrxHeaderCtReference | CT_REFERENCE | — | — |
| 312 | TrxHeaderCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 313 | TrxHeaderCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 314 | TrxHeaderCustomerReference | CUSTOMER_REFERENCE | — | — |
| 315 | TrxHeaderCustomerReferenceDate | CUSTOMER_REFERENCE_DATE | — | — |
| 316 | TrxHeaderCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 317 | TrxHeaderDefaultTaxExemptFlag | DEFAULT_TAX_EXEMPT_FLAG | — | — |
| 318 | TrxHeaderDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 319 | TrxHeaderDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 320 | TrxHeaderDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 321 | TrxHeaderDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 322 | TrxHeaderDraweeBankAccountId | DRAWEE_BANK_ACCOUNT_ID | — | — |
| 323 | TrxHeaderDraweeContactId | DRAWEE_CONTACT_ID | — | — |
| 324 | TrxHeaderDraweeId | DRAWEE_ID | — | — |
| 325 | TrxHeaderDraweeSiteUseId | DRAWEE_SITE_USE_ID | — | — |
| 326 | TrxHeaderEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 327 | TrxHeaderEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 328 | TrxHeaderEndDateCommitment | END_DATE_COMMITMENT | — | — |
| 329 | TrxHeaderExchangeDate | EXCHANGE_DATE | — | — |
| 330 | TrxHeaderExchangeRate | EXCHANGE_RATE | — | — |
| 331 | TrxHeaderExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 332 | TrxHeaderFinanceCharges | FINANCE_CHARGES | — | — |
| 333 | TrxHeaderFobPoint | FOB_POINT | — | — |
| 334 | TrxHeaderInitialCustomerTrxId | INITIAL_CUSTOMER_TRX_ID | — | — |
| 335 | TrxHeaderIntercompanyFlag | INTERCOMPANY_FLAG | — | — |
| 336 | TrxHeaderInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 337 | TrxHeaderInterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | — |
| 338 | TrxHeaderInterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | — |
| 339 | TrxHeaderInterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | — |
| 340 | TrxHeaderInterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | — |
| 341 | TrxHeaderInterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | — |
| 342 | TrxHeaderInterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | — |
| 343 | TrxHeaderInterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | — |
| 344 | TrxHeaderInterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | — |
| 345 | TrxHeaderInterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | — |
| 346 | TrxHeaderInterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | — |
| 347 | TrxHeaderInterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | — |
| 348 | TrxHeaderInterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | — |
| 349 | TrxHeaderInterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | — |
| 350 | TrxHeaderInterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | — |
| 351 | TrxHeaderInterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | — |
| 352 | TrxHeaderInterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | — |
| 353 | TrxHeaderInternalNotes | INTERNAL_NOTES | — | — |
| 354 | TrxHeaderInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 355 | TrxHeaderInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 356 | TrxHeaderLastPrintedSequenceNum | LAST_PRINTED_SEQUENCE_NUM | — | — |
| 357 | TrxHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 358 | TrxHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 359 | TrxHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 360 | TrxHeaderLateChargesAssessed | LATE_CHARGES_ASSESSED | — | — |
| 361 | TrxHeaderLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 362 | TrxHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 363 | TrxHeaderOldTrxNumber | OLD_TRX_NUMBER | — | — |
| 364 | TrxHeaderOrgId | ORG_ID | — | — |
| 365 | TrxHeaderOrigSystemBatchName | ORIG_SYSTEM_BATCH_NAME | — | — |
| 366 | TrxHeaderOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 367 | TrxHeaderPayingCustomerId | PAYING_CUSTOMER_ID | — | — |
| 368 | TrxHeaderPayingSiteUseId | PAYING_SITE_USE_ID | — | — |
| 369 | TrxHeaderPaymentAttributes | PAYMENT_ATTRIBUTES | — | — |
| 370 | TrxHeaderPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 371 | TrxHeaderPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 372 | TrxHeaderPostRequestId | POST_REQUEST_ID | — | — |
| 373 | TrxHeaderPostingControlId | POSTING_CONTROL_ID | — | — |
| 374 | TrxHeaderPrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 375 | TrxHeaderPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 376 | TrxHeaderPrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | — |
| 377 | TrxHeaderPrintingCount | PRINTING_COUNT | — | — |
| 378 | TrxHeaderPrintingLastPrinted | PRINTING_LAST_PRINTED | — | — |
| 379 | TrxHeaderPrintingOption | PRINTING_OPTION | — | — |
| 380 | TrxHeaderPrintingOriginalDate | PRINTING_ORIGINAL_DATE | — | — |
| 381 | TrxHeaderPrintingPending | PRINTING_PENDING | — | — |
| 382 | TrxHeaderProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 383 | TrxHeaderProgramId | PROGRAM_ID | — | — |
| 384 | TrxHeaderProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 385 | TrxHeaderPurchaseOrder | PURCHASE_ORDER | — | — |
| 386 | TrxHeaderPurchaseOrderDate | PURCHASE_ORDER_DATE | — | — |
| 387 | TrxHeaderPurchaseOrderRevision | PURCHASE_ORDER_REVISION | — | — |
| 388 | TrxHeaderRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 389 | TrxHeaderReasonCode | REASON_CODE | — | — |
| 390 | TrxHeaderReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 391 | TrxHeaderRecurredFromTrxNumber | RECURRED_FROM_TRX_NUMBER | — | — |
| 392 | TrxHeaderRelatedBatchSourceSeqId | RELATED_BATCH_SOURCE_SEQ_ID | — | — |
| 393 | TrxHeaderRelatedCustomerTrxId | RELATED_CUSTOMER_TRX_ID | — | — |
| 394 | TrxHeaderRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 395 | TrxHeaderRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 396 | TrxHeaderRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 397 | TrxHeaderRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 398 | TrxHeaderRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 399 | TrxHeaderRequestId | REQUEST_ID | — | — |
| 400 | TrxHeaderReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 401 | TrxHeaderSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 402 | TrxHeaderShipDateActual | SHIP_DATE_ACTUAL | — | — |
| 403 | TrxHeaderShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 404 | TrxHeaderShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 405 | TrxHeaderShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 406 | TrxHeaderShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 407 | TrxHeaderShipVia | SHIP_VIA | — | — |
| 408 | TrxHeaderShipmentId | SHIPMENT_ID | — | — |
| 409 | TrxHeaderSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 410 | TrxHeaderSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 411 | TrxHeaderSoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | — |
| 412 | TrxHeaderSourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 413 | TrxHeaderSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 414 | TrxHeaderSpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 415 | TrxHeaderStartDateCommitment | START_DATE_COMMITMENT | — | — |
| 416 | TrxHeaderStatusTrx | STATUS_TRX | — | — |
| 417 | TrxHeaderTermDueDate | TERM_DUE_DATE | — | — |
| 418 | TrxHeaderTermId | TERM_ID | — | — |
| 419 | TrxHeaderTerritoryId | TERRITORY_ID | — | — |
| 420 | TrxHeaderTrxClass | TRX_CLASS | — | — |
| 421 | TrxHeaderTrxDate | TRX_DATE | — | — |
| 422 | TrxHeaderTrxNumber | TRX_NUMBER | — | — |
| 423 | TrxHeaderUpgradeMethod | UPGRADE_METHOD | — | — |
| 424 | TrxHeaderWaybillNumber | WAYBILL_NUMBER | — | — |
| 425 | TrxHeaderWhUpdateDate | WH_UPDATE_DATE | — | — |

### [[ra_customer_trx_lines_all|RA_CUSTOMER_TRX_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AppTrxLineAccountingRuleDuration | ACCOUNTING_RULE_DURATION | — | — |
| 2 | AppTrxLineAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 3 | AppTrxLineAcctdAmountDueOriginal | ACCTD_AMOUNT_DUE_ORIGINAL | — | — |
| 4 | AppTrxLineAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | — |
| 5 | AppTrxLineAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 6 | AppTrxLineAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 7 | AppTrxLineAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 8 | AppTrxLineAssessableValue | ASSESSABLE_VALUE | — | — |
| 9 | AppTrxLineAutoruleCompleteFlag | AUTORULE_COMPLETE_FLAG | — | — |
| 10 | AppTrxLineAutoruleDurationProcessed | AUTORULE_DURATION_PROCESSED | — | — |
| 11 | AppTrxLineAutotax | AUTOTAX | — | — |
| 12 | AppTrxLineBrAdjustmentId | BR_ADJUSTMENT_ID | — | — |
| 13 | AppTrxLineBrRefCustomerTrxId | BR_REF_CUSTOMER_TRX_ID | — | — |
| 14 | AppTrxLineBrRefPaymentScheduleId | BR_REF_PAYMENT_SCHEDULE_ID | — | — |
| 15 | AppTrxLineChrgAcctdAmountRemaining | CHRG_ACCTD_AMOUNT_REMAINING | — | — |
| 16 | AppTrxLineChrgAmountRemaining | CHRG_AMOUNT_REMAINING | — | — |
| 17 | AppTrxLineContractLineId | CONTRACT_LINE_ID | — | — |
| 18 | AppTrxLineCreatedBy | CREATED_BY | — | — |
| 19 | AppTrxLineCreationDate | CREATION_DATE | — | — |
| 20 | AppTrxLineCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 21 | AppTrxLineCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 22 | AppTrxLineDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 23 | AppTrxLineDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 24 | AppTrxLineDeferralExclusionFlag | DEFERRAL_EXCLUSION_FLAG | — | — |
| 25 | AppTrxLineDescription | DESCRIPTION | — | — |
| 26 | AppTrxLineExtendedAcctdAmount | EXTENDED_ACCTD_AMOUNT | — | — |
| 27 | AppTrxLineExtendedAmount | EXTENDED_AMOUNT | — | — |
| 28 | AppTrxLineFairMarketValueAmount | FAIR_MARKET_VALUE_AMOUNT | — | — |
| 29 | AppTrxLineFrtAdjAcctdRemaining | FRT_ADJ_ACCTD_REMAINING | — | — |
| 30 | AppTrxLineFrtAdjRemaining | FRT_ADJ_REMAINING | — | — |
| 31 | AppTrxLineFrtEdAcctdAmount | FRT_ED_ACCTD_AMOUNT | — | — |
| 32 | AppTrxLineFrtEdAmount | FRT_ED_AMOUNT | — | — |
| 33 | AppTrxLineFrtUnedAcctdAmount | FRT_UNED_ACCTD_AMOUNT | — | — |
| 34 | AppTrxLineFrtUnedAmount | FRT_UNED_AMOUNT | — | — |
| 35 | AppTrxLineGrossExtendedAmount | GROSS_EXTENDED_AMOUNT | — | — |
| 36 | AppTrxLineGrossUnitSellingPrice | GROSS_UNIT_SELLING_PRICE | — | — |
| 37 | AppTrxLineHistoricalFlag | HISTORICAL_FLAG | — | — |
| 38 | AppTrxLineInitialCustomerTrxLineId | INITIAL_CUSTOMER_TRX_LINE_ID | — | — |
| 39 | AppTrxLineInterestLineId | INTEREST_LINE_ID | — | — |
| 40 | AppTrxLineInterfaceLineAttribute1 | INTERFACE_LINE_ATTRIBUTE1 | — | — |
| 41 | AppTrxLineInterfaceLineAttribute10 | INTERFACE_LINE_ATTRIBUTE10 | — | — |
| 42 | AppTrxLineInterfaceLineAttribute11 | INTERFACE_LINE_ATTRIBUTE11 | — | — |
| 43 | AppTrxLineInterfaceLineAttribute12 | INTERFACE_LINE_ATTRIBUTE12 | — | — |
| 44 | AppTrxLineInterfaceLineAttribute13 | INTERFACE_LINE_ATTRIBUTE13 | — | — |
| 45 | AppTrxLineInterfaceLineAttribute14 | INTERFACE_LINE_ATTRIBUTE14 | — | — |
| 46 | AppTrxLineInterfaceLineAttribute15 | INTERFACE_LINE_ATTRIBUTE15 | — | — |
| 47 | AppTrxLineInterfaceLineAttribute2 | INTERFACE_LINE_ATTRIBUTE2 | — | — |
| 48 | AppTrxLineInterfaceLineAttribute3 | INTERFACE_LINE_ATTRIBUTE3 | — | — |
| 49 | AppTrxLineInterfaceLineAttribute4 | INTERFACE_LINE_ATTRIBUTE4 | — | — |
| 50 | AppTrxLineInterfaceLineAttribute5 | INTERFACE_LINE_ATTRIBUTE5 | — | — |
| 51 | AppTrxLineInterfaceLineAttribute6 | INTERFACE_LINE_ATTRIBUTE6 | — | — |
| 52 | AppTrxLineInterfaceLineAttribute7 | INTERFACE_LINE_ATTRIBUTE7 | — | — |
| 53 | AppTrxLineInterfaceLineAttribute8 | INTERFACE_LINE_ATTRIBUTE8 | — | — |
| 54 | AppTrxLineInterfaceLineAttribute9 | INTERFACE_LINE_ATTRIBUTE9 | — | — |
| 55 | AppTrxLineInterfaceLineContext | INTERFACE_LINE_CONTEXT | — | — |
| 56 | AppTrxLineInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 57 | AppTrxLineInvoicedLineAcctgLevel | INVOICED_LINE_ACCTG_LEVEL | — | — |
| 58 | AppTrxLineItemContext | ITEM_CONTEXT | — | — |
| 59 | AppTrxLineItemExceptionRateId | ITEM_EXCEPTION_RATE_ID | — | — |
| 60 | AppTrxLineLastPeriodToCredit | LAST_PERIOD_TO_CREDIT | — | — |
| 61 | AppTrxLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 62 | AppTrxLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 63 | AppTrxLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 64 | AppTrxLineLineIntendedUse | LINE_INTENDED_USE | — | — |
| 65 | AppTrxLineLineNumber | LINE_NUMBER | — | ✅ |
| 66 | AppTrxLineLineRecoverable | LINE_RECOVERABLE | — | — |
| 67 | AppTrxLineLineType | LINE_TYPE | — | — |
| 68 | AppTrxLineLinkToCustTrxLineId | LINK_TO_CUST_TRX_LINE_ID | — | — |
| 69 | AppTrxLineLinkToParentlineAttribute1 | LINK_TO_PARENTLINE_ATTRIBUTE1 | — | — |
| 70 | AppTrxLineLinkToParentlineAttribute10 | LINK_TO_PARENTLINE_ATTRIBUTE10 | — | — |
| 71 | AppTrxLineLinkToParentlineAttribute11 | LINK_TO_PARENTLINE_ATTRIBUTE11 | — | — |
| 72 | AppTrxLineLinkToParentlineAttribute12 | LINK_TO_PARENTLINE_ATTRIBUTE12 | — | — |
| 73 | AppTrxLineLinkToParentlineAttribute13 | LINK_TO_PARENTLINE_ATTRIBUTE13 | — | — |
| 74 | AppTrxLineLinkToParentlineAttribute14 | LINK_TO_PARENTLINE_ATTRIBUTE14 | — | — |
| 75 | AppTrxLineLinkToParentlineAttribute15 | LINK_TO_PARENTLINE_ATTRIBUTE15 | — | — |
| 76 | AppTrxLineLinkToParentlineAttribute2 | LINK_TO_PARENTLINE_ATTRIBUTE2 | — | — |
| 77 | AppTrxLineLinkToParentlineAttribute3 | LINK_TO_PARENTLINE_ATTRIBUTE3 | — | — |
| 78 | AppTrxLineLinkToParentlineAttribute4 | LINK_TO_PARENTLINE_ATTRIBUTE4 | — | — |
| 79 | AppTrxLineLinkToParentlineAttribute5 | LINK_TO_PARENTLINE_ATTRIBUTE5 | — | — |
| 80 | AppTrxLineLinkToParentlineAttribute6 | LINK_TO_PARENTLINE_ATTRIBUTE6 | — | — |
| 81 | AppTrxLineLinkToParentlineAttribute7 | LINK_TO_PARENTLINE_ATTRIBUTE7 | — | — |
| 82 | AppTrxLineLinkToParentlineAttribute8 | LINK_TO_PARENTLINE_ATTRIBUTE8 | — | — |
| 83 | AppTrxLineLinkToParentlineAttribute9 | LINK_TO_PARENTLINE_ATTRIBUTE9 | — | — |
| 84 | AppTrxLineLinkToParentlineContext | LINK_TO_PARENTLINE_CONTEXT | — | — |
| 85 | AppTrxLineLocationSegmentId | LOCATION_SEGMENT_ID | — | — |
| 86 | AppTrxLineMemoLineSeqId | MEMO_LINE_SEQ_ID | — | — |
| 87 | AppTrxLineMovementId | MOVEMENT_ID | — | — |
| 88 | AppTrxLineMrcExtendedAcctdAmount | MRC_EXTENDED_ACCTD_AMOUNT | — | — |
| 89 | AppTrxLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 90 | AppTrxLineOrgId | ORG_ID | — | — |
| 91 | AppTrxLineOverrideAutoAccountingFlag | OVERRIDE_AUTO_ACCOUNTING_FLAG | — | — |
| 92 | AppTrxLinePaymentSetId | PAYMENT_SET_ID | — | — |
| 93 | AppTrxLinePaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 94 | AppTrxLinePreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 95 | AppTrxLinePreviousCustomerTrxLineId | PREVIOUS_CUSTOMER_TRX_LINE_ID | — | — |
| 96 | AppTrxLineProductCategory | PRODUCT_CATEGORY | — | — |
| 97 | AppTrxLineProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | — |
| 98 | AppTrxLineProductType | PRODUCT_TYPE | — | — |
| 99 | AppTrxLineProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 100 | AppTrxLineProgramId | PROGRAM_ID | — | — |
| 101 | AppTrxLineProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 102 | AppTrxLineQuantityCredited | QUANTITY_CREDITED | — | — |
| 103 | AppTrxLineQuantityInvoiced | QUANTITY_INVOICED | — | — |
| 104 | AppTrxLineQuantityOrdered | QUANTITY_ORDERED | — | — |
| 105 | AppTrxLineReasonCode | REASON_CODE | — | — |
| 106 | AppTrxLineRequestId | REQUEST_ID | — | — |
| 107 | AppTrxLineRevenueAmount | REVENUE_AMOUNT | — | — |
| 108 | AppTrxLineRuleEndDate | RULE_END_DATE | — | — |
| 109 | AppTrxLineRuleStartDate | RULE_START_DATE | — | — |
| 110 | AppTrxLineSalesOrder | SALES_ORDER | — | — |
| 111 | AppTrxLineSalesOrderDate | SALES_ORDER_DATE | — | — |
| 112 | AppTrxLineSalesOrderLine | SALES_ORDER_LINE | — | — |
| 113 | AppTrxLineSalesOrderRevision | SALES_ORDER_REVISION | — | — |
| 114 | AppTrxLineSalesOrderSource | SALES_ORDER_SOURCE | — | — |
| 115 | AppTrxLineSalesTaxId | SALES_TAX_ID | — | — |
| 116 | AppTrxLineSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 117 | AppTrxLineShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 118 | AppTrxLineShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 119 | AppTrxLineShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 120 | AppTrxLineShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 121 | AppTrxLineSourceDataKey1 | SOURCE_DATA_KEY1 | — | — |
| 122 | AppTrxLineSourceDataKey2 | SOURCE_DATA_KEY2 | — | — |
| 123 | AppTrxLineSourceDataKey3 | SOURCE_DATA_KEY3 | — | — |
| 124 | AppTrxLineSourceDataKey4 | SOURCE_DATA_KEY4 | — | — |
| 125 | AppTrxLineSourceDataKey5 | SOURCE_DATA_KEY5 | — | — |
| 126 | AppTrxLineSourceDocumentLineId | SOURCE_DOCUMENT_LINE_ID | — | — |
| 127 | AppTrxLineSourceDocumentLineNumber | SOURCE_DOCUMENT_LINE_NUMBER | — | — |
| 128 | AppTrxLineTaxAction | TAX_ACTION | — | — |
| 129 | AppTrxLineTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 130 | AppTrxLineTaxExemptFlag | TAX_EXEMPT_FLAG | — | — |
| 131 | AppTrxLineTaxExemptNumber | TAX_EXEMPT_NUMBER | — | — |
| 132 | AppTrxLineTaxExemptReasonCode | TAX_EXEMPT_REASON_CODE | — | — |
| 133 | AppTrxLineTaxExemptionId | TAX_EXEMPTION_ID | — | — |
| 134 | AppTrxLineTaxLineId | TAX_LINE_ID | — | — |
| 135 | AppTrxLineTaxPrecedence | TAX_PRECEDENCE | — | — |
| 136 | AppTrxLineTaxRate | TAX_RATE | — | — |
| 137 | AppTrxLineTaxRecoverable | TAX_RECOVERABLE | — | — |
| 138 | AppTrxLineTaxVendorReturnCode | TAX_VENDOR_RETURN_CODE | — | — |
| 139 | AppTrxLineTaxableAmount | TAXABLE_AMOUNT | — | — |
| 140 | AppTrxLineTaxableFlag | TAXABLE_FLAG | — | — |
| 141 | AppTrxLineTranslatedDescription | TRANSLATED_DESCRIPTION | — | — |
| 142 | AppTrxLineTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 143 | AppTrxLineUnitSellingPrice | UNIT_SELLING_PRICE | — | — |
| 144 | AppTrxLineUnitStandardPrice | UNIT_STANDARD_PRICE | — | — |
| 145 | AppTrxLineUomCode | UOM_CODE | — | — |
| 146 | AppTrxLineUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 147 | AppTrxLineVatTaxId | VAT_TAX_ID | — | — |
| 148 | AppTrxLineWarehouseId | WAREHOUSE_ID | — | — |
| 149 | AppTrxLineWhUpdateDate | WH_UPDATE_DATE | — | — |

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
| 37 | TaxRtScoTaxRateName | TAX_RATE_NAME | — | — |
| 38 | TaxRtScoTaxRegimeCode | TAX_REGIME_CODE | — | — |
| 39 | TaxRtScoTaxStatusCode | TAX_STATUS_CODE | — | — |
| 40 | TaxRtScoTaxableBasisFormulaCode | TAXABLE_BASIS_FORMULA_CODE | — | — |
| 41 | TaxRtScoUomCode | UOM_CODE | — | — |
| 42 | TaxRtScoVatTransactionTypeCode | VAT_TRANSACTION_TYPE_CODE | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
