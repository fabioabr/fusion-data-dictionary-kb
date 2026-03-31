---
id: DOC-AR-PVO-AdjustmentPVO
doc_type: system-doc
title: "AdjustmentPVO — PVO Accounts Receivable"
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
  - AdjustmentPVO
  - adjustmentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AdjustmentPVO

## 📌 Visão Geral

Extrai os ajustes realizados em transações de contas a receber (write-offs, reclassificações, correções), incluindo valores, motivos, status de aprovação e tipo de transação. Permite análise de perdas, gestão de inadimplência e auditoria de modificações no saldo de clientes.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.AdjustmentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 580 | 21 | 1 | 68 | 12% |

---

## 🔗 Tabelas Relacionadas

- [[ar_adjustments_all|AR_ADJUSTMENTS_ALL]] — 59 atributos (1 PKs, 23 BICC)
- [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]] — 86 atributos (3 BICC)
- [[ar_cons_inv_all|AR_CONS_INV_ALL]] — 49 atributos (3 BICC)
- [[ar_distribution_sets_all|AR_DISTRIBUTION_SETS_ALL]] — 6 atributos (1 BICC)
- [[ar_interest_headers_all|AR_INTEREST_HEADERS_ALL]] — 35 atributos
- [[ar_interest_lines_all|AR_INTEREST_LINES_ALL]] — 22 atributos (4 BICC)
- [[ar_payment_schedules_all|AR_PAYMENT_SCHEDULES_ALL]] — 72 atributos (9 BICC)
- [[ar_receivables_trx_all|AR_RECEIVABLES_TRX_ALL]] — 25 atributos (3 BICC)
- [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]] — 7 atributos (2 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 1 atributos
- [[gl_ledgers|GL_LEDGERS]] — 3 atributos
- [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]] — 3 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos
- [[per_users|PER_USERS]] — 16 atributos (1 BICC)
- [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]] — 156 atributos (11 BICC)
- [[ra_cust_trx_types_all|RA_CUST_TRX_TYPES_ALL]] — 7 atributos (5 BICC)
- [[ra_rules|RA_RULES]] — 3 atributos (1 BICC)
- [[ra_terms_b|RA_TERMS_B]] — 3 atributos
- [[ra_terms_lines|RA_TERMS_LINES]] — 3 atributos (1 BICC)
- [[ra_terms_vl|RA_TERMS_VL]] — 3 atributos
- [[xla_events|XLA_EVENTS]] — 11 atributos

---

## ⚙️ Atributos

### [[ar_adjustments_all|AR_ADJUSTMENTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustmentAcctdAmount | ACCTD_AMOUNT | — | ✅ |
| 2 | AdjustmentAdjTaxAcctRule | ADJ_TAX_ACCT_RULE | — | — |
| 3 | AdjustmentAdjustmentNumber | ADJUSTMENT_NUMBER | — | ✅ |
| 4 | AdjustmentAdjustmentType | ADJUSTMENT_TYPE | — | ✅ |
| 5 | AdjustmentAmount | AMOUNT | — | ✅ |
| 6 | AdjustmentApplyDate | APPLY_DATE | — | ✅ |
| 7 | AdjustmentApprovedBy | APPROVED_BY | — | — |
| 8 | AdjustmentAssociatedApplicationId | ASSOCIATED_APPLICATION_ID | — | — |
| 9 | AdjustmentAssociatedCashReceiptId | ASSOCIATED_CASH_RECEIPT_ID | — | — |
| 10 | AdjustmentAutomaticallyGenerated | AUTOMATICALLY_GENERATED | — | — |
| 11 | AdjustmentAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 12 | AdjustmentBatchId | BATCH_ID | — | — |
| 13 | AdjustmentChargebackCustomerTrxId | CHARGEBACK_CUSTOMER_TRX_ID | — | — |
| 14 | AdjustmentCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 15 | AdjustmentComments | COMMENTS | — | ✅ |
| 16 | AdjustmentConsInvId | CONS_INV_ID | — | — |
| 17 | AdjustmentCreatedBy | CREATED_BY | — | ✅ |
| 18 | AdjustmentCreatedFrom | CREATED_FROM | — | — |
| 19 | AdjustmentCreationDate | CREATION_DATE | — | ✅ |
| 20 | AdjustmentCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 21 | AdjustmentCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 22 | AdjustmentDistributionSetId | DISTRIBUTION_SET_ID | — | — |
| 23 | AdjustmentDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 24 | AdjustmentDocSequenceValue | DOC_SEQUENCE_VALUE | — | ✅ |
| 25 | AdjustmentEventId | EVENT_ID | — | ✅ |
| 26 | AdjustmentFreightAdjusted | FREIGHT_ADJUSTED | — | ✅ |
| 27 | AdjustmentGlDate | GL_DATE | — | ✅ |
| 28 | AdjustmentGlPostedDate | GL_POSTED_DATE | — | ✅ |
| 29 | AdjustmentId | ADJUSTMENT_ID | 🔑 | ✅ |
| 30 | AdjustmentInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 31 | AdjustmentInterestLineId | INTEREST_LINE_ID | — | — |
| 32 | AdjustmentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 33 | AdjustmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 34 | AdjustmentLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 35 | AdjustmentLineAdjusted | LINE_ADJUSTED | — | ✅ |
| 36 | AdjustmentLinkToTrxHistId | LINK_TO_TRX_HIST_ID | — | — |
| 37 | AdjustmentMrcAcctdAmount | MRC_ACCTD_AMOUNT | — | — |
| 38 | AdjustmentMrcGlPostedDate | MRC_GL_POSTED_DATE | — | — |
| 39 | AdjustmentMrcPostingControlId | MRC_POSTING_CONTROL_ID | — | — |
| 40 | AdjustmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 41 | AdjustmentOrgId | ORG_ID | — | — |
| 42 | AdjustmentPaymentScheduleId | PAYMENT_SCHEDULE_ID | — | — |
| 43 | AdjustmentPostable | POSTABLE | — | ✅ |
| 44 | AdjustmentPostingControlId | POSTING_CONTROL_ID | — | ✅ |
| 45 | AdjustmentProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 46 | AdjustmentProgramId | PROGRAM_ID | — | — |
| 47 | AdjustmentProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 48 | AdjustmentReasonCode | REASON_CODE | — | ✅ |
| 49 | AdjustmentReceivablesChargesAdjusted | RECEIVABLES_CHARGES_ADJUSTED | — | ✅ |
| 50 | AdjustmentReceivablesTrxId | RECEIVABLES_TRX_ID | — | — |
| 51 | AdjustmentRequestId | REQUEST_ID | — | — |
| 52 | AdjustmentSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 53 | AdjustmentStatus | STATUS | — | — |
| 54 | AdjustmentSubsequentTrxId | SUBSEQUENT_TRX_ID | — | — |
| 55 | AdjustmentTaxAdjusted | TAX_ADJUSTED | — | ✅ |
| 56 | AdjustmentType | TYPE | — | ✅ |
| 57 | AdjustmentUpgradeMethod | UPGRADE_METHOD | — | — |
| 58 | AdjustmentUssglTransactionCode | USSGL_TRANSACTION_CODE | — | — |
| 59 | AdjustmentUssglTransactionCodeContext | USSGL_TRANSACTION_CODE_CONTEXT | — | — |

### [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReceiptsActualValueDate | ACTUAL_VALUE_DATE | — | — |
| 2 | ReceiptsAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 3 | ReceiptsAmount | AMOUNT | — | — |
| 4 | ReceiptsAnticipatedClearingDate | ANTICIPATED_CLEARING_DATE | — | — |
| 5 | ReceiptsApplicationNotes | APPLICATION_NOTES | — | — |
| 6 | ReceiptsApprovalCode | APPROVAL_CODE | — | — |
| 7 | ReceiptsAutoapplyFlag | AUTOAPPLY_FLAG | — | — |
| 8 | ReceiptsAutomatchRequestId | AUTOMATCH_REQUEST_ID | — | — |
| 9 | ReceiptsAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 10 | ReceiptsCashReceiptId | CASH_RECEIPT_ID | — | — |
| 11 | ReceiptsCcErrorCode | CC_ERROR_CODE | — | — |
| 12 | ReceiptsCcErrorFlag | CC_ERROR_FLAG | — | — |
| 13 | ReceiptsCcErrorText | CC_ERROR_TEXT | — | — |
| 14 | ReceiptsCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 15 | ReceiptsCollectorId | COLLECTOR_ID | — | — |
| 16 | ReceiptsComments | COMMENTS | — | — |
| 17 | ReceiptsConfirmedFlag | CONFIRMED_FLAG | — | — |
| 18 | ReceiptsCreatedBy | CREATED_BY | — | — |
| 19 | ReceiptsCreationDate | CREATION_DATE | — | — |
| 20 | ReceiptsCurrencyCode | CURRENCY_CODE | — | — |
| 21 | ReceiptsCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 22 | ReceiptsCustomerBankBranchId | CUSTOMER_BANK_BRANCH_ID | — | — |
| 23 | ReceiptsCustomerReceiptReference | CUSTOMER_RECEIPT_REFERENCE | — | — |
| 24 | ReceiptsCustomerSiteUseId | CUSTOMER_SITE_USE_ID | — | — |
| 25 | ReceiptsDepositDate | DEPOSIT_DATE | — | — |
| 26 | ReceiptsDistributionSetId | DISTRIBUTION_SET_ID | — | — |
| 27 | ReceiptsDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 28 | ReceiptsDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 29 | ReceiptsExchangeDate | EXCHANGE_DATE | — | — |
| 30 | ReceiptsExchangeRate | EXCHANGE_RATE | — | — |
| 31 | ReceiptsExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 32 | ReceiptsFactorDiscountAmount | FACTOR_DISCOUNT_AMOUNT | — | — |
| 33 | ReceiptsIssueDate | ISSUE_DATE | — | — |
| 34 | ReceiptsIssuerBankBranchId | ISSUER_BANK_BRANCH_ID | — | — |
| 35 | ReceiptsIssuerName | ISSUER_NAME | — | — |
| 36 | ReceiptsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 37 | ReceiptsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 38 | ReceiptsLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 39 | ReceiptsLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 40 | ReceiptsLogicalGroupReference | LOGICAL_GROUP_REFERENCE | — | — |
| 41 | ReceiptsMiscPaymentSource | MISC_PAYMENT_SOURCE | — | — |
| 42 | ReceiptsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 43 | ReceiptsOldCustomerBankAccountId | OLD_CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 44 | ReceiptsOldCustomerBankBranchId | OLD_CUSTOMER_BANK_BRANCH_ID | — | — |
| 45 | ReceiptsOldIssuerBankBranchId | OLD_ISSUER_BANK_BRANCH_ID | — | — |
| 46 | ReceiptsOrgId | ORG_ID | — | — |
| 47 | ReceiptsOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 48 | ReceiptsPayFromCustomer | PAY_FROM_CUSTOMER | — | — |
| 49 | ReceiptsPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 50 | ReceiptsPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 51 | ReceiptsPostmarkDate | POSTMARK_DATE | — | — |
| 52 | ReceiptsProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 53 | ReceiptsProgramId | PROGRAM_ID | — | — |
| 54 | ReceiptsProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 55 | ReceiptsPromiseSource | PROMISE_SOURCE | — | — |
| 56 | ReceiptsRecVersionNumber | REC_VERSION_NUMBER | — | — |
| 57 | ReceiptsReceiptBatchId | RECEIPT_BATCH_ID | — | — |
| 58 | ReceiptsReceiptDate | RECEIPT_DATE | — | — |
| 59 | ReceiptsReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 60 | ReceiptsReceiptNumber | RECEIPT_NUMBER | — | ✅ |
| 61 | ReceiptsReceivablesTrxId | RECEIVABLES_TRX_ID | — | — |
| 62 | ReceiptsReconFlag | RECON_FLAG | — | — |
| 63 | ReceiptsReferenceId | REFERENCE_ID | — | — |
| 64 | ReceiptsReferenceType | REFERENCE_TYPE | — | — |
| 65 | ReceiptsRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 66 | ReceiptsRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 67 | ReceiptsRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 68 | ReceiptsRequestId | REQUEST_ID | — | — |
| 69 | ReceiptsResourceId | RESOURCE_ID | — | — |
| 70 | ReceiptsReversalCategory | REVERSAL_CATEGORY | — | — |
| 71 | ReceiptsReversalComments | REVERSAL_COMMENTS | — | — |
| 72 | ReceiptsReversalDate | REVERSAL_DATE | — | — |
| 73 | ReceiptsReversalReasonCode | REVERSAL_REASON_CODE | — | — |
| 74 | ReceiptsSelectedForFactoringFlag | SELECTED_FOR_FACTORING_FLAG | — | — |
| 75 | ReceiptsSelectedRemittanceBatchId | SELECTED_REMITTANCE_BATCH_ID | — | — |
| 76 | ReceiptsSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 77 | ReceiptsStatus | STATUS | — | — |
| 78 | ReceiptsTaxRate | TAX_RATE | — | — |
| 79 | ReceiptsType | TYPE | — | — |
| 80 | ReceiptsUniqueReference | UNIQUE_REFERENCE | — | — |
| 81 | ReceiptsUssglTransactionCode | USSGL_TRANSACTION_CODE | — | — |
| 82 | ReceiptsUssglTransactionCodeContext | USSGL_TRANSACTION_CODE_CONTEXT | — | — |
| 83 | ReceiptsVatTaxId | VAT_TAX_ID | — | — |
| 84 | ReverseReceiptCashReceiptId | CASH_RECEIPT_ID | — | — |
| 85 | ReverseReceiptObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 86 | ReverseReceiptReceiptNumber | RECEIPT_NUMBER | — | ✅ |

### [[ar_cons_inv_all|AR_CONS_INV_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConsBillAgingBucket1Amt | AGING_BUCKET1_AMT | — | — |
| 2 | ConsBillAgingBucket2Amt | AGING_BUCKET2_AMT | — | — |
| 3 | ConsBillAgingBucket3Amt | AGING_BUCKET3_AMT | — | — |
| 4 | ConsBillAgingBucket4Amt | AGING_BUCKET4_AMT | — | — |
| 5 | ConsBillAgingBucket5Amt | AGING_BUCKET5_AMT | — | — |
| 6 | ConsBillAgingBucket6Amt | AGING_BUCKET6_AMT | — | — |
| 7 | ConsBillAgingBucket7Amt | AGING_BUCKET7_AMT | — | — |
| 8 | ConsBillBeginningBalance | BEGINNING_BALANCE | — | — |
| 9 | ConsBillBillLevelFlag | BILL_LEVEL_FLAG | — | — |
| 10 | ConsBillBillingCycleId | BILLING_CYCLE_ID | — | — |
| 11 | ConsBillBillingDate | BILLING_DATE | — | — |
| 12 | ConsBillConcurrentRequestId | CONCURRENT_REQUEST_ID | — | — |
| 13 | ConsBillConsBillingNumber | CONS_BILLING_NUMBER | — | ✅ |
| 14 | ConsBillConsInvId | CONS_INV_ID | — | — |
| 15 | ConsBillConsInvType | CONS_INV_TYPE | — | — |
| 16 | ConsBillCreatedBy | CREATED_BY | — | — |
| 17 | ConsBillCreationDate | CREATION_DATE | — | — |
| 18 | ConsBillCurrencyCode | CURRENCY_CODE | — | — |
| 19 | ConsBillCustomerId | CUSTOMER_ID | — | — |
| 20 | ConsBillCutOffDate | CUT_OFF_DATE | — | — |
| 21 | ConsBillDueDate | DUE_DATE | — | — |
| 22 | ConsBillEndingBalance | ENDING_BALANCE | — | — |
| 23 | ConsBillIssueDate | ISSUE_DATE | — | — |
| 24 | ConsBillLastBillingDate | LAST_BILLING_DATE | — | — |
| 25 | ConsBillLastChargeDate | LAST_CHARGE_DATE | — | — |
| 26 | ConsBillLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 27 | ConsBillLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 28 | ConsBillLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 29 | ConsBillObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 30 | ConsBillOrgId | ORG_ID | — | — |
| 31 | ConsBillPrintStatus | PRINT_STATUS | — | — |
| 32 | ConsBillRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 33 | ConsBillRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 34 | ConsBillSiteUseId | SITE_USE_ID | — | — |
| 35 | ConsBillStartDate | START_DATE | — | — |
| 36 | ConsBillStatus | STATUS | — | — |
| 37 | ConsBillTermId | TERM_ID | — | — |
| 38 | ConsBillTotalAdjustmentsAmt | TOTAL_ADJUSTMENTS_AMT | — | — |
| 39 | ConsBillTotalCreditsAmt | TOTAL_CREDITS_AMT | — | — |
| 40 | ConsBillTotalFinanceChargesAmt | TOTAL_FINANCE_CHARGES_AMT | — | — |
| 41 | ConsBillTotalReceiptsAmt | TOTAL_RECEIPTS_AMT | — | — |
| 42 | ConsBillTotalTaxAmt | TOTAL_TAX_AMT | — | — |
| 43 | ConsBillTotalTrxAmt | TOTAL_TRX_AMT | — | — |
| 44 | ConsBillUnpaidReason | UNPAID_REASON | — | — |
| 45 | ConsolidatedBillConsInvId | CONS_INV_ID | — | — |
| 46 | ConsolidatedBillObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 47 | RevConsBillConsBillingNumber1 | CONS_BILLING_NUMBER | — | ✅ |
| 48 | RevConsBillConsInvId1 | CONS_INV_ID | — | — |
| 49 | RevConsBillObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |

### [[ar_distribution_sets_all|AR_DISTRIBUTION_SETS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistributionSetDescription | DESCRIPTION | — | — |
| 2 | DistributionSetDistributionSetId | DISTRIBUTION_SET_ID | — | — |
| 3 | DistributionSetDistributionSetName | DISTRIBUTION_SET_NAME | — | ✅ |
| 4 | DistributionSetOrgId | ORG_ID | — | — |
| 5 | DistributionSetStatus | STATUS | — | — |
| 6 | DistributionSetTotalPercentDistribution | TOTAL_PERCENT_DISTRIBUTION | — | — |

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
| 35 | IntrstHdrWorkerNum | WORKER_NUM | — | — |

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
| 1 | PmtScheduleAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | — |
| 2 | PmtScheduleActiveClaimFlag | ACTIVE_CLAIM_FLAG | — | — |
| 3 | PmtScheduleActualDateClosed | ACTUAL_DATE_CLOSED | — | — |
| 4 | PmtScheduleAdjustmentAmountLast | ADJUSTMENT_AMOUNT_LAST | — | — |
| 5 | PmtScheduleAdjustmentDateLast | ADJUSTMENT_DATE_LAST | — | — |
| 6 | PmtScheduleAdjustmentGlDateLast | ADJUSTMENT_GL_DATE_LAST | — | — |
| 7 | PmtScheduleAdjustmentIdLast | ADJUSTMENT_ID_LAST | — | — |
| 8 | PmtScheduleAmountAdjusted | AMOUNT_ADJUSTED | — | — |
| 9 | PmtScheduleAmountAdjustedPending | AMOUNT_ADJUSTED_PENDING | — | — |
| 10 | PmtScheduleAmountApplied | AMOUNT_APPLIED | — | — |
| 11 | PmtScheduleAmountCredited | AMOUNT_CREDITED | — | — |
| 12 | PmtScheduleAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 13 | PmtScheduleAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 14 | PmtScheduleAmountInDispute | AMOUNT_IN_DISPUTE | — | — |
| 15 | PmtScheduleAmountLineItemsOriginal | AMOUNT_LINE_ITEMS_ORIGINAL | — | — |
| 16 | PmtScheduleAmountLineItemsRemaining | AMOUNT_LINE_ITEMS_REMAINING | — | — |
| 17 | PmtScheduleAmountOnAccount | AMOUNT_ON_ACCOUNT | — | — |
| 18 | PmtScheduleAmountOtherAccount | AMOUNT_OTHER_ACCOUNT | — | — |
| 19 | PmtScheduleAssociatedCashReceiptId | ASSOCIATED_CASH_RECEIPT_ID | — | — |
| 20 | PmtScheduleBrAmountAssigned | BR_AMOUNT_ASSIGNED | — | — |
| 21 | PmtScheduleCallDateLast | CALL_DATE_LAST | — | — |
| 22 | PmtScheduleCashReceiptId | CASH_RECEIPT_ID | — | — |
| 23 | PmtScheduleCollectorLast | COLLECTOR_LAST | — | — |
| 24 | PmtScheduleConsInvId | CONS_INV_ID | — | — |
| 25 | PmtScheduleConsInvIdRev | CONS_INV_ID_REV | — | — |
| 26 | PmtScheduleCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 27 | PmtScheduleCustomerId | CUSTOMER_ID | — | — |
| 28 | PmtScheduleCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 29 | PmtScheduleDiscountDate | DISCOUNT_DATE | — | — |
| 30 | PmtScheduleDiscountOriginal | DISCOUNT_ORIGINAL | — | — |
| 31 | PmtScheduleDiscountRemaining | DISCOUNT_REMAINING | — | — |
| 32 | PmtScheduleDiscountTakenEarned | DISCOUNT_TAKEN_EARNED | — | — |
| 33 | PmtScheduleDiscountTakenUnearned | DISCOUNT_TAKEN_UNEARNED | — | — |
| 34 | PmtScheduleDisputeDate | DISPUTE_DATE | — | ✅ |
| 35 | PmtScheduleDueDate | DUE_DATE | — | ✅ |
| 36 | PmtScheduleExchangeDate | EXCHANGE_DATE | — | ✅ |
| 37 | PmtScheduleExchangeRate | EXCHANGE_RATE | — | ✅ |
| 38 | PmtScheduleExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 39 | PmtScheduleExcludeFromConsBillFlag | EXCLUDE_FROM_CONS_BILL_FLAG | — | — |
| 40 | PmtScheduleFollowUpCodeLast | FOLLOW_UP_CODE_LAST | — | — |
| 41 | PmtScheduleFollowUpDateLast | FOLLOW_UP_DATE_LAST | — | — |
| 42 | PmtScheduleFreightOriginal | FREIGHT_ORIGINAL | — | — |
| 43 | PmtScheduleFreightRemaining | FREIGHT_REMAINING | — | — |
| 44 | PmtScheduleGlDate | GL_DATE | — | ✅ |
| 45 | PmtScheduleGlDateClosed | GL_DATE_CLOSED | — | — |
| 46 | PmtScheduleInCollection | IN_COLLECTION | — | — |
| 47 | PmtScheduleInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 48 | PmtScheduleLastChargeDate | LAST_CHARGE_DATE | — | — |
| 49 | PmtScheduleNumberOfDueDates | NUMBER_OF_DUE_DATES | — | — |
| 50 | PmtScheduleObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 51 | PmtScheduleOrgId | ORG_ID | — | — |
| 52 | PmtSchedulePaymentApproval | PAYMENT_APPROVAL | — | — |
| 53 | PmtSchedulePaymentScheduleClass | CLASS | — | — |
| 54 | PmtSchedulePaymentScheduleId | PAYMENT_SCHEDULE_ID | — | — |
| 55 | PmtSchedulePromiseAmountLast | PROMISE_AMOUNT_LAST | — | — |
| 56 | PmtSchedulePromiseDateLast | PROMISE_DATE_LAST | — | — |
| 57 | PmtScheduleReceivablesChargesCharged | RECEIVABLES_CHARGES_CHARGED | — | — |
| 58 | PmtScheduleReceivablesChargesRemaining | RECEIVABLES_CHARGES_REMAINING | — | — |
| 59 | PmtScheduleRequestId | REQUEST_ID | — | — |
| 60 | PmtScheduleReservedType | RESERVED_TYPE | — | — |
| 61 | PmtScheduleReservedValue | RESERVED_VALUE | — | — |
| 62 | PmtScheduleReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 63 | PmtScheduleSecondLastChargeDate | SECOND_LAST_CHARGE_DATE | — | — |
| 64 | PmtScheduleSelectedForReceiptBatchId | SELECTED_FOR_RECEIPT_BATCH_ID | — | — |
| 65 | PmtScheduleStagedDunningLevel | STAGED_DUNNING_LEVEL | — | — |
| 66 | PmtScheduleStatus | STATUS | — | ✅ |
| 67 | PmtScheduleTaxOriginal | TAX_ORIGINAL | — | — |
| 68 | PmtScheduleTaxRemaining | TAX_REMAINING | — | — |
| 69 | PmtScheduleTermId | TERM_ID | — | — |
| 70 | PmtScheduleTermsSequenceNumber | TERMS_SEQUENCE_NUMBER | — | — |
| 71 | PmtScheduleTrxDate | TRX_DATE | — | ✅ |
| 72 | PmtScheduleTrxNumber | TRX_NUMBER | — | ✅ |

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

### [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocSeqAuditTableName | AUDIT_TABLE_NAME | — | — |
| 2 | DocSeqDbSequenceName | DB_SEQUENCE_NAME | — | — |
| 3 | DocSeqDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 4 | DocSeqName | NAME | — | ✅ |
| 5 | DocSeqTableName | TABLE_NAME | — | — |
| 6 | TrxDocSeqHdrDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 7 | TrxDocSeqHdrName | NAME | — | ✅ |

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitBusinessUnitId | BU_ID | — | — |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 2 | LedgersLedgerId | LEDGER_ID | — | — |
| 3 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExternalBankAccountBankAccountNum | BANK_ACCOUNT_NUM | — | ✅ |
| 2 | ExternalBankAccountExtBankAccountId | EXT_BANK_ACCOUNT_ID | — | — |
| 3 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |

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
| 9 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 10 | UserCreatedByUserGuid | USER_GUID | — | — |
| 11 | UserCreatedByUserId | USER_ID | — | — |
| 12 | UserCreatedByUsername | USERNAME | — | — |
| 13 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 14 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 15 | UserUpdatedByUserId | USER_ID | — | — |
| 16 | UserUpdatedByUsername | USERNAME | — | — |

### [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionHeaderPBillingDate | BILLING_DATE | — | ✅ |
| 2 | TransactionHeaderPCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | ✅ |
| 3 | TransactionHeaderPCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | ✅ |
| 4 | TransactionHeaderPCustomerReference | CUSTOMER_REFERENCE | — | ✅ |
| 5 | TransactionHeaderPCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 6 | TransactionHeaderPDocSequenceValue | DOC_SEQUENCE_VALUE | — | ✅ |
| 7 | TransactionHeaderPFinanceCharges | FINANCE_CHARGES | — | ✅ |
| 8 | TransactionHeaderPIntercompanyFlag | INTERCOMPANY_FLAG | — | ✅ |
| 9 | TransactionHeaderPObjectVersionNumber8 | OBJECT_VERSION_NUMBER | — | — |
| 10 | TrxHeaderAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 11 | TrxHeaderAgreementId | AGREEMENT_ID | — | — |
| 12 | TrxHeaderApplicationId | APPLICATION_ID | — | — |
| 13 | TrxHeaderApprovalCode | APPROVAL_CODE | — | — |
| 14 | TrxHeaderAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 15 | TrxHeaderBatchId | BATCH_ID | — | — |
| 16 | TrxHeaderBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 17 | TrxHeaderBillTemplateId | BILL_TEMPLATE_ID | — | ✅ |
| 18 | TrxHeaderBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 19 | TrxHeaderBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 20 | TrxHeaderBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 21 | TrxHeaderBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 22 | TrxHeaderBillingDate | BILLING_DATE | — | — |
| 23 | TrxHeaderBrAmount | BR_AMOUNT | — | — |
| 24 | TrxHeaderBrOnHoldFlag | BR_ON_HOLD_FLAG | — | — |
| 25 | TrxHeaderBrUnpaidFlag | BR_UNPAID_FLAG | — | — |
| 26 | TrxHeaderCcErrorCode | CC_ERROR_CODE | — | — |
| 27 | TrxHeaderCcErrorFlag | CC_ERROR_FLAG | — | — |
| 28 | TrxHeaderCcErrorText | CC_ERROR_TEXT | — | — |
| 29 | TrxHeaderComments | COMMENTS | — | — |
| 30 | TrxHeaderCompleteFlag | COMPLETE_FLAG | — | — |
| 31 | TrxHeaderContractId | CONTRACT_ID | — | — |
| 32 | TrxHeaderCreatedBy | CREATED_BY | — | — |
| 33 | TrxHeaderCreatedFrom | CREATED_FROM | — | — |
| 34 | TrxHeaderCreationDate | CREATION_DATE | — | — |
| 35 | TrxHeaderCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | — |
| 36 | TrxHeaderCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | — |
| 37 | TrxHeaderCtReference | CT_REFERENCE | — | — |
| 38 | TrxHeaderCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 39 | TrxHeaderCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 40 | TrxHeaderCustomerReference | CUSTOMER_REFERENCE | — | — |
| 41 | TrxHeaderCustomerReferenceDate | CUSTOMER_REFERENCE_DATE | — | — |
| 42 | TrxHeaderCustomerTrxId | CUSTOMER_TRX_ID | — | ✅ |
| 43 | TrxHeaderDefaultTaxExemptFlag | DEFAULT_TAX_EXEMPT_FLAG | — | — |
| 44 | TrxHeaderDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 45 | TrxHeaderDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 46 | TrxHeaderDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 47 | TrxHeaderDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 48 | TrxHeaderDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 49 | TrxHeaderDocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 50 | TrxHeaderDraweeBankAccountId | DRAWEE_BANK_ACCOUNT_ID | — | — |
| 51 | TrxHeaderDraweeContactId | DRAWEE_CONTACT_ID | — | — |
| 52 | TrxHeaderDraweeId | DRAWEE_ID | — | — |
| 53 | TrxHeaderDraweeSiteUseId | DRAWEE_SITE_USE_ID | — | — |
| 54 | TrxHeaderEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 55 | TrxHeaderEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 56 | TrxHeaderEndDateCommitment | END_DATE_COMMITMENT | — | — |
| 57 | TrxHeaderExchangeDate | EXCHANGE_DATE | — | — |
| 58 | TrxHeaderExchangeRate | EXCHANGE_RATE | — | — |
| 59 | TrxHeaderExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 60 | TrxHeaderFinanceCharges | FINANCE_CHARGES | — | — |
| 61 | TrxHeaderFobPoint | FOB_POINT | — | — |
| 62 | TrxHeaderInitialCustomerTrxId | INITIAL_CUSTOMER_TRX_ID | — | — |
| 63 | TrxHeaderIntercompanyFlag | INTERCOMPANY_FLAG | — | — |
| 64 | TrxHeaderInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 65 | TrxHeaderInterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | — |
| 66 | TrxHeaderInterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | — |
| 67 | TrxHeaderInterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | — |
| 68 | TrxHeaderInterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | — |
| 69 | TrxHeaderInterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | — |
| 70 | TrxHeaderInterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | — |
| 71 | TrxHeaderInterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | — |
| 72 | TrxHeaderInterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | — |
| 73 | TrxHeaderInterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | — |
| 74 | TrxHeaderInterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | — |
| 75 | TrxHeaderInterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | — |
| 76 | TrxHeaderInterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | — |
| 77 | TrxHeaderInterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | — |
| 78 | TrxHeaderInterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | — |
| 79 | TrxHeaderInterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | — |
| 80 | TrxHeaderInterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | — |
| 81 | TrxHeaderInternalNotes | INTERNAL_NOTES | — | — |
| 82 | TrxHeaderInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 83 | TrxHeaderInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 84 | TrxHeaderLastPrintedSequenceNum | LAST_PRINTED_SEQUENCE_NUM | — | — |
| 85 | TrxHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 86 | TrxHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 87 | TrxHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 88 | TrxHeaderLateChargesAssessed | LATE_CHARGES_ASSESSED | — | — |
| 89 | TrxHeaderLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 90 | TrxHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 91 | TrxHeaderOldTrxNumber | OLD_TRX_NUMBER | — | — |
| 92 | TrxHeaderOrgId | ORG_ID | — | — |
| 93 | TrxHeaderOrigSystemBatchName | ORIG_SYSTEM_BATCH_NAME | — | — |
| 94 | TrxHeaderOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 95 | TrxHeaderPayingCustomerId | PAYING_CUSTOMER_ID | — | — |
| 96 | TrxHeaderPayingSiteUseId | PAYING_SITE_USE_ID | — | — |
| 97 | TrxHeaderPaymentAttributes | PAYMENT_ATTRIBUTES | — | — |
| 98 | TrxHeaderPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 99 | TrxHeaderPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 100 | TrxHeaderPostRequestId | POST_REQUEST_ID | — | — |
| 101 | TrxHeaderPostingControlId | POSTING_CONTROL_ID | — | — |
| 102 | TrxHeaderPrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 103 | TrxHeaderPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 104 | TrxHeaderPrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | — |
| 105 | TrxHeaderPrintingCount | PRINTING_COUNT | — | — |
| 106 | TrxHeaderPrintingLastPrinted | PRINTING_LAST_PRINTED | — | — |
| 107 | TrxHeaderPrintingOption | PRINTING_OPTION | — | — |
| 108 | TrxHeaderPrintingOriginalDate | PRINTING_ORIGINAL_DATE | — | — |
| 109 | TrxHeaderPrintingPending | PRINTING_PENDING | — | — |
| 110 | TrxHeaderProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 111 | TrxHeaderProgramId | PROGRAM_ID | — | — |
| 112 | TrxHeaderProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 113 | TrxHeaderPurchaseOrder | PURCHASE_ORDER | — | — |
| 114 | TrxHeaderPurchaseOrderDate | PURCHASE_ORDER_DATE | — | — |
| 115 | TrxHeaderPurchaseOrderRevision | PURCHASE_ORDER_REVISION | — | — |
| 116 | TrxHeaderRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 117 | TrxHeaderReasonCode | REASON_CODE | — | — |
| 118 | TrxHeaderReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 119 | TrxHeaderRecurredFromTrxNumber | RECURRED_FROM_TRX_NUMBER | — | — |
| 120 | TrxHeaderRelatedBatchSourceSeqId | RELATED_BATCH_SOURCE_SEQ_ID | — | — |
| 121 | TrxHeaderRelatedCustomerTrxId | RELATED_CUSTOMER_TRX_ID | — | — |
| 122 | TrxHeaderRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 123 | TrxHeaderRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 124 | TrxHeaderRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 125 | TrxHeaderRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 126 | TrxHeaderRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 127 | TrxHeaderRequestId | REQUEST_ID | — | — |
| 128 | TrxHeaderRequiresManualScheduling | REQUIRES_MANUAL_SCHEDULING | — | — |
| 129 | TrxHeaderReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 130 | TrxHeaderSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 131 | TrxHeaderShipDateActual | SHIP_DATE_ACTUAL | — | — |
| 132 | TrxHeaderShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 133 | TrxHeaderShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 134 | TrxHeaderShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 135 | TrxHeaderShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 136 | TrxHeaderShipVia | SHIP_VIA | — | — |
| 137 | TrxHeaderShipmentId | SHIPMENT_ID | — | — |
| 138 | TrxHeaderSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 139 | TrxHeaderSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 140 | TrxHeaderSoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | — |
| 141 | TrxHeaderSourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 142 | TrxHeaderSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 143 | TrxHeaderSpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 144 | TrxHeaderStartDateCommitment | START_DATE_COMMITMENT | — | — |
| 145 | TrxHeaderStatusTrx | STATUS_TRX | — | — |
| 146 | TrxHeaderTermDueDate | TERM_DUE_DATE | — | — |
| 147 | TrxHeaderTermId | TERM_ID | — | — |
| 148 | TrxHeaderTerritoryId | TERRITORY_ID | — | — |
| 149 | TrxHeaderTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 150 | TrxHeaderTrxClass | TRX_CLASS | — | — |
| 151 | TrxHeaderTrxDate | TRX_DATE | — | — |
| 152 | TrxHeaderTrxNumber | TRX_NUMBER | — | ✅ |
| 153 | TrxHeaderUpgradeMethod | UPGRADE_METHOD | — | — |
| 154 | TrxHeaderUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 155 | TrxHeaderWaybillNumber | WAYBILL_NUMBER | — | — |
| 156 | TrxHeaderWhUpdateDate | WH_UPDATE_DATE | — | — |

### [[ra_cust_trx_types_all|RA_CUST_TRX_TYPES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionTypeAccountingAffectFlag | ACCOUNTING_AFFECT_FLAG | — | ✅ |
| 2 | TransactionTypeCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 3 | TransactionTypeDescription | DESCRIPTION | — | ✅ |
| 4 | TransactionTypeName | NAME | — | ✅ |
| 5 | TransactionTypeObjectVersionNumber7 | OBJECT_VERSION_NUMBER | — | — |
| 6 | TransactionTypePostToGl | POST_TO_GL | — | ✅ |
| 7 | TransactionTypeType | TYPE | — | ✅ |

### [[ra_rules|RA_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvDistRuleName | NAME | — | ✅ |
| 2 | InvDistRuleObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
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
| 2 | PaymentTermLineObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |
| 3 | PaymentTermLineSequenceNum | SEQUENCE_NUM | — | ✅ |

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

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
