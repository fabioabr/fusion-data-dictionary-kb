---
id: DOC-AR-PVO-TransactionLinePVO
doc_type: system-doc
title: "TransactionLinePVO — PVO Accounts Receivable"
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
  - TransactionLinePVO
  - transactionlinepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionLinePVO

## 📌 Visão Geral

Extrai as linhas das transações de Contas a Receber, com detalhamento por item, quantidade, valor unitário, impostos e classificação fiscal. Central para análise de composição de receita, precificação e reporte fiscal detalhado.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.TransactionLinePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 2114 | 41 | 1 | 220 | 10% |

---

## 🔗 Tabelas Relacionadas

- [[ar_batches_all|AR_BATCHES_ALL]] — 46 atributos (1 BICC)
- [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]] — 5 atributos (1 BICC)
- [[ar_deferred_lines_all|AR_DEFERRED_LINES_ALL]] — 20 atributos (7 BICC)
- [[ar_interest_headers_all|AR_INTEREST_HEADERS_ALL]] — 35 atributos
- [[ar_interest_lines_all|AR_INTEREST_LINES_ALL]] — 22 atributos (4 BICC)
- [[ar_lookups|AR_LOOKUPS]] — 4 atributos (1 BICC)
- [[ar_memo_lines_all_b|AR_MEMO_LINES_ALL_B]] — 13 atributos
- [[ar_memo_lines_all_tl|AR_MEMO_LINES_ALL_TL]] — 5 atributos (2 BICC)
- [[ar_payment_schedules_all|AR_PAYMENT_SCHEDULES_ALL]] — 93 atributos (1 BICC)
- [[ce_bank_acct_uses_all|CE_BANK_ACCT_USES_ALL]] — 30 atributos (1 BICC)
- [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]] — 5 atributos (1 BICC)
- [[fnd_territories_vl|FND_TERRITORIES_VL]] — 9 atributos (1 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 1 atributos
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 18 atributos (2 BICC)
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 6 atributos
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 71 atributos (5 BICC)
- [[hz_cust_account_roles|HZ_CUST_ACCOUNT_ROLES]] — 2 atributos
- [[hz_cust_acct_sites_all|HZ_CUST_ACCT_SITES_ALL]] — 12 atributos
- [[hz_cust_site_uses_all|HZ_CUST_SITE_USES_ALL]] — 6 atributos
- [[hz_locations|HZ_LOCATIONS]] — 26 atributos (20 BICC)
- [[hz_parties|HZ_PARTIES]] — 27 atributos (3 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 12 atributos (3 BICC)
- [[hz_party_site_uses|HZ_PARTY_SITE_USES]] — 3 atributos (1 BICC)
- [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]] — 44 atributos (2 BICC)
- [[iby_fndcpt_tx_extensions|IBY_FNDCPT_TX_EXTENSIONS]] — 28 atributos (2 BICC)
- [[inv_units_of_measure_b|INV_UNITS_OF_MEASURE_B]] — 3 atributos
- [[inv_units_of_measure_tl|INV_UNITS_OF_MEASURE_TL]] — 4 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (2 BICC)
- [[per_users|PER_USERS]] — 9 atributos
- [[ra_batches_all|RA_BATCHES_ALL]] — 33 atributos (1 BICC)
- [[ra_batch_sources_all|RA_BATCH_SOURCES_ALL]] — 124 atributos (3 BICC)
- [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]] — 587 atributos (76 BICC)
- [[ra_customer_trx_lines_all|RA_CUSTOMER_TRX_LINES_ALL]] — 600 atributos (1 PKs, 69 BICC)
- [[ra_rules|RA_RULES]] — 4 atributos (1 BICC)
- [[zx_fc_intended_use_v|ZX_FC_INTENDED_USE_V]] — 4 atributos (1 BICC)
- [[zx_fc_product_categories_v|ZX_FC_PRODUCT_CATEGORIES_V]] — 6 atributos (1 BICC)
- [[zx_fc_product_fiscal_v|ZX_FC_PRODUCT_FISCAL_V]] — 8 atributos (1 BICC)
- [[zx_fc_user_defined_v|ZX_FC_USER_DEFINED_V]] — 6 atributos (2 BICC)
- [[zx_lines|ZX_LINES]] — 165 atributos
- [[zx_product_types_v|ZX_PRODUCT_TYPES_V]] — 2 atributos (1 BICC)
- [[zx_registrations|ZX_REGISTRATIONS]] — 6 atributos (2 BICC)

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
| 6 | ReceiptBatchBatchId | BATCH_ID | — | — |
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
| 25 | ReceiptBatchName | NAME | — | — |
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
| 42 | ReceiptBatchStatus | STATUS | — | — |
| 43 | ReceiptBatchTransmissionId | TRANSMISSION_ID | — | — |
| 44 | ReceiptBatchTransmissionRequestId | TRANSMISSION_REQUEST_ID | — | — |
| 45 | ReceiptBatchType | TYPE | — | — |
| 46 | ReceiptBatchWithRecourseFlag | WITH_RECOURSE_FLAG | — | — |

### [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RevCashRcptCashReceiptId | CASH_RECEIPT_ID | — | — |
| 2 | RevCashRcptComments | COMMENTS | — | — |
| 3 | RevCashRcptIssuerName | ISSUER_NAME | — | — |
| 4 | RevCashRcptObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 5 | RevCashRcptReceiptNumber | RECEIPT_NUMBER | — | ✅ |

### [[ar_deferred_lines_all|AR_DEFERRED_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeferredLineAcctdAmountDueOriginal | ACCTD_AMOUNT_DUE_ORIGINAL | — | ✅ |
| 2 | DeferredLineAcctdAmountPending | ACCTD_AMOUNT_PENDING | — | ✅ |
| 3 | DeferredLineAcctdAmountRecognized | ACCTD_AMOUNT_RECOGNIZED | — | ✅ |
| 4 | DeferredLineAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | ✅ |
| 5 | DeferredLineAmountPending | AMOUNT_PENDING | — | ✅ |
| 6 | DeferredLineAmountRecognized | AMOUNT_RECOGNIZED | — | ✅ |
| 7 | DeferredLineCreatedBy | CREATED_BY | — | — |
| 8 | DeferredLineCreationDate | CREATION_DATE | — | — |
| 9 | DeferredLineCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 10 | DeferredLineCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 11 | DeferredLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | DeferredLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | DeferredLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | DeferredLineLineCollectibleFlag | LINE_COLLECTIBLE_FLAG | — | — |
| 15 | DeferredLineManualOverrideFlag | MANUAL_OVERRIDE_FLAG | — | — |
| 16 | DeferredLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | DeferredLineOrgId | ORG_ID | — | — |
| 18 | DeferredLineOriginalCollectibilityFlag | ORIGINAL_COLLECTIBILITY_FLAG | — | — |
| 19 | DeferredLineParentLineId | PARENT_LINE_ID | — | — |
| 20 | DeferredLineRequestId | REQUEST_ID | — | — |

### [[ar_interest_headers_all|AR_INTEREST_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IntrstHdrTrxHdrChargeBeginDate | CHARGE_BEGIN_DATE | — | — |
| 2 | IntrstHdrTrxHdrChargeOnFinanceChargeFlag | CHARGE_ON_FINANCE_CHARGE_FLAG | — | — |
| 3 | IntrstHdrTrxHdrCreditItemsFlag | CREDIT_ITEMS_FLAG | — | — |
| 4 | IntrstHdrTrxHdrCurrencyCode | CURRENCY_CODE | — | — |
| 5 | IntrstHdrTrxHdrDisplayFlag | DISPLAY_FLAG | — | — |
| 6 | IntrstHdrTrxHdrDisputedTransactionsFlag | DISPUTED_TRANSACTIONS_FLAG | — | — |
| 7 | IntrstHdrTrxHdrExchangeRate | EXCHANGE_RATE | — | — |
| 8 | IntrstHdrTrxHdrExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 9 | IntrstHdrTrxHdrFinanceChargeDate | FINANCE_CHARGE_DATE | — | — |
| 10 | IntrstHdrTrxHdrHeaderType | HEADER_TYPE | — | — |
| 11 | IntrstHdrTrxHdrHoldChargedInvoicesFlag | HOLD_CHARGED_INVOICES_FLAG | — | — |
| 12 | IntrstHdrTrxHdrInterestCalculationPeriod | INTEREST_CALCULATION_PERIOD | — | — |
| 13 | IntrstHdrTrxHdrInterestFixedAmount | INTEREST_FIXED_AMOUNT | — | — |
| 14 | IntrstHdrTrxHdrInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 15 | IntrstHdrTrxHdrInterestPeriodDays | INTEREST_PERIOD_DAYS | — | — |
| 16 | IntrstHdrTrxHdrInterestRate | INTEREST_RATE | — | — |
| 17 | IntrstHdrTrxHdrInterestType | INTEREST_TYPE | — | — |
| 18 | IntrstHdrTrxHdrLastAccrueChargeDate | LAST_ACCRUE_CHARGE_DATE | — | — |
| 19 | IntrstHdrTrxHdrLateChargeCalculationTrx | LATE_CHARGE_CALCULATION_TRX | — | — |
| 20 | IntrstHdrTrxHdrMaxInterestCharge | MAX_INTEREST_CHARGE | — | — |
| 21 | IntrstHdrTrxHdrMinFcBalanceAmount | MIN_FC_BALANCE_AMOUNT | — | — |
| 22 | IntrstHdrTrxHdrMinFcBalanceOverdueType | MIN_FC_BALANCE_OVERDUE_TYPE | — | — |
| 23 | IntrstHdrTrxHdrMinFcBalancePercent | MIN_FC_BALANCE_PERCENT | — | — |
| 24 | IntrstHdrTrxHdrMinFcInvoiceAmount | MIN_FC_INVOICE_AMOUNT | — | — |
| 25 | IntrstHdrTrxHdrMinFcInvoiceOverdueType | MIN_FC_INVOICE_OVERDUE_TYPE | — | — |
| 26 | IntrstHdrTrxHdrMinFcInvoicePercent | MIN_FC_INVOICE_PERCENT | — | — |
| 27 | IntrstHdrTrxHdrMinInterestCharge | MIN_INTEREST_CHARGE | — | — |
| 28 | IntrstHdrTrxHdrMultipleInterestRatesFlag | MULTIPLE_INTEREST_RATES_FLAG | — | — |
| 29 | IntrstHdrTrxHdrPaymentGraceDays | PAYMENT_GRACE_DAYS | — | — |
| 30 | IntrstHdrTrxHdrPenaltyFixedAmount | PENALTY_FIXED_AMOUNT | — | — |
| 31 | IntrstHdrTrxHdrPenaltyRate | PENALTY_RATE | — | — |
| 32 | IntrstHdrTrxHdrPenaltyType | PENALTY_TYPE | — | — |
| 33 | IntrstHdrTrxHdrProcessMessage | PROCESS_MESSAGE | — | — |
| 34 | IntrstHdrTrxHdrProcessStatus | PROCESS_STATUS | — | — |
| 35 | IntrstHdrTrxHdrWorkerNum | WORKER_NUM | — | — |

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

### [[ar_lookups|AR_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrxClassDescription | DESCRIPTION | — | — |
| 2 | TrxClassLookupCode | LOOKUP_CODE | — | — |
| 3 | TrxClassLookupType | LOOKUP_TYPE | — | — |
| 4 | TrxClassMeaning | MEANING | — | ✅ |

### [[ar_memo_lines_all_b|AR_MEMO_LINES_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MemoLineAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 2 | MemoLineEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | MemoLineEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | MemoLineInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 5 | MemoLineLineType | LINE_TYPE | — | — |
| 6 | MemoLineMemoLineId | MEMO_LINE_ID | — | — |
| 7 | MemoLineMemoLineSeqId | MEMO_LINE_SEQ_ID | — | — |
| 8 | MemoLineSetId | SET_ID | — | — |
| 9 | MemoLineTaxCode | TAX_CODE | — | — |
| 10 | MemoLineTaxProductCategory | TAX_PRODUCT_CATEGORY | — | — |
| 11 | MemoLineUnitStdPrice | UNIT_STD_PRICE | — | — |
| 12 | MemoLineUomCode | UOM_CODE | — | — |
| 13 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[ar_memo_lines_all_tl|AR_MEMO_LINES_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MemoLineDescription | DESCRIPTION | — | ✅ |
| 2 | MemoLineName | NAME | — | ✅ |
| 3 | MemoLineTranslationLanguage | LANGUAGE | — | — |
| 4 | MemoLineTranslationMemoLineId | MEMO_LINE_ID | — | — |
| 5 | MemoLineTranslationSetId | SET_ID | — | — |

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

### [[ce_bank_acct_uses_all|CE_BANK_ACCT_USES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankAccountUseApUseEnableFlag | AP_USE_ENABLE_FLAG | — | — |
| 2 | BankAccountUseArUseEnableFlag | AR_USE_ENABLE_FLAG | — | — |
| 3 | BankAccountUseAuthorizedFlag | AUTHORIZED_FLAG | — | — |
| 4 | BankAccountUseBankAccountId | BANK_ACCOUNT_ID | — | — |
| 5 | BankAccountUseBankAcctUseId | BANK_ACCT_USE_ID | — | — |
| 6 | BankAccountUseCreatedBy | CREATED_BY | — | — |
| 7 | BankAccountUseCreationDate | CREATION_DATE | — | — |
| 8 | BankAccountUseDefaultAccountFlag | DEFAULT_ACCOUNT_FLAG | — | — |
| 9 | BankAccountUseEftScriptName | EFT_SCRIPT_NAME | — | — |
| 10 | BankAccountUseEndDate | END_DATE | — | — |
| 11 | BankAccountUseFundingLimitCode | FUNDING_LIMIT_CODE | — | — |
| 12 | BankAccountUseInvestmentLimitCode | INVESTMENT_LIMIT_CODE | — | — |
| 13 | BankAccountUseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | BankAccountUseLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | BankAccountUseLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | BankAccountUseLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 17 | BankAccountUseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | BankAccountUseOrgId | ORG_ID | — | — |
| 19 | BankAccountUseOrgPartyId | ORG_PARTY_ID | — | — |
| 20 | BankAccountUsePayUseEnableFlag | PAY_USE_ENABLE_FLAG | — | — |
| 21 | BankAccountUsePortfolioCode | PORTFOLIO_CODE | — | — |
| 22 | BankAccountUsePricingModel | PRICING_MODEL | — | — |
| 23 | BankAccountUsePrimaryFlag | PRIMARY_FLAG | — | — |
| 24 | BankAccountUseProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 25 | BankAccountUseProgramId | PROGRAM_ID | — | — |
| 26 | BankAccountUseProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 27 | BankAccountUseRequestId | REQUEST_ID | — | — |
| 28 | BankAccountUseXtrBankAccountReference | XTR_BANK_ACCOUNT_REFERENCE | — | — |
| 29 | BankAccountUseXtrDefaultSettlementFlag | XTR_DEFAULT_SETTLEMENT_FLAG | — | — |
| 30 | BankAccountUseXtrUseEnableFlag | XTR_USE_ENABLE_FLAG | — | — |

### [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocSeqHdrAuditTableName | AUDIT_TABLE_NAME | — | — |
| 2 | DocSeqHdrDbSequenceName | DB_SEQUENCE_NAME | — | — |
| 3 | DocSeqHdrDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 4 | DocSeqHdrName | NAME | — | ✅ |
| 5 | DocSeqHdrTableName | TABLE_NAME | — | — |

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
| 9 | TerritoryTerritoryShortName | TERRITORY_SHORT_NAME | — | ✅ |

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

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgUnitTransEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | OrgUnitTransEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | OrgUnitTransLanguage | LANGUAGE | — | — |
| 4 | OrgUnitTransName | NAME | — | — |
| 5 | OrgUnitTransOrganizationId | ORGANIZATION_ID | — | — |
| 6 | OrgUnitTransSourceLang | SOURCE_LANG | — | — |

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
| 8 | CustAcctCreatedBy | CREATED_BY | — | — |
| 9 | CustAcctCreatedByModule | CREATED_BY_MODULE | — | — |
| 10 | CustAcctCreationDate | CREATION_DATE | — | — |
| 11 | CustAcctCustAccountId | CUST_ACCOUNT_ID | — | — |
| 12 | CustAcctCustomerClassCode | CUSTOMER_CLASS_CODE | — | — |
| 13 | CustAcctCustomerType | CUSTOMER_TYPE | — | — |
| 14 | CustAcctDateTypePreference | DATE_TYPE_PREFERENCE | — | — |
| 15 | CustAcctDepositRefundMethod | DEPOSIT_REFUND_METHOD | — | — |
| 16 | CustAcctDraweeAccountEstablishedDate | ACCOUNT_ESTABLISHED_DATE | — | — |
| 17 | CustAcctDraweeAccountName | ACCOUNT_NAME | — | — |
| 18 | CustAcctDraweeAccountNumber | ACCOUNT_NUMBER | — | — |
| 19 | CustAcctDraweeArrivalsetsIncludeLinesFlag | ARRIVALSETS_INCLUDE_LINES_FLAG | — | — |
| 20 | CustAcctDraweeAutopayFlag | AUTOPAY_FLAG | — | — |
| 21 | CustAcctDraweeComments | COMMENTS | — | — |
| 22 | CustAcctDraweeCoterminateDayMonth | COTERMINATE_DAY_MONTH | — | — |
| 23 | CustAcctDraweeCreatedBy | CREATED_BY | — | — |
| 24 | CustAcctDraweeCreatedByModule | CREATED_BY_MODULE | — | — |
| 25 | CustAcctDraweeCreationDate | CREATION_DATE | — | — |
| 26 | CustAcctDraweeCustAccountId | CUST_ACCOUNT_ID | — | — |
| 27 | CustAcctDraweeCustomerClassCode | CUSTOMER_CLASS_CODE | — | — |
| 28 | CustAcctDraweeCustomerType | CUSTOMER_TYPE | — | — |
| 29 | CustAcctDraweeDateTypePreference | DATE_TYPE_PREFERENCE | — | — |
| 30 | CustAcctDraweeDepositRefundMethod | DEPOSIT_REFUND_METHOD | — | — |
| 31 | CustAcctDraweeHeldBillExpirationDate | HELD_BILL_EXPIRATION_DATE | — | — |
| 32 | CustAcctDraweeHoldBillFlag | HOLD_BILL_FLAG | — | — |
| 33 | CustAcctDraweeLastBatchId | LAST_BATCH_ID | — | — |
| 34 | CustAcctDraweeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 35 | CustAcctDraweeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 36 | CustAcctDraweeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 37 | CustAcctDraweeNpaNumber | NPA_NUMBER | — | — |
| 38 | CustAcctDraweeOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 39 | CustAcctDraweePartyId | PARTY_ID | — | — |
| 40 | CustAcctDraweeSellingPartyId | SELLING_PARTY_ID | — | — |
| 41 | CustAcctDraweeSourceCode | SOURCE_CODE | — | — |
| 42 | CustAcctDraweeStatus | STATUS | — | — |
| 43 | CustAcctDraweeStatusUpdateDate | STATUS_UPDATE_DATE | — | — |
| 44 | CustAcctDraweeTaxCode | TAX_CODE | — | — |
| 45 | CustAcctDraweeTaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | — |
| 46 | CustAcctDraweeTaxRoundingRule | TAX_ROUNDING_RULE | — | — |
| 47 | CustAcctHeldBillExpirationDate | HELD_BILL_EXPIRATION_DATE | — | — |
| 48 | CustAcctHoldBillFlag | HOLD_BILL_FLAG | — | — |
| 49 | CustAcctLastBatchId | LAST_BATCH_ID | — | — |
| 50 | CustAcctLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 51 | CustAcctLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 52 | CustAcctLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 53 | CustAcctNpaNumber | NPA_NUMBER | — | — |
| 54 | CustAcctOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 55 | CustAcctPartyId | PARTY_ID | — | — |
| 56 | CustAcctSellingPartyId | SELLING_PARTY_ID | — | — |
| 57 | CustAcctSourceCode | SOURCE_CODE | — | — |
| 58 | CustAcctStatus | STATUS | — | — |
| 59 | CustAcctStatusUpdateDate | STATUS_UPDATE_DATE | — | — |
| 60 | CustAcctTaxCode | TAX_CODE | — | — |
| 61 | CustAcctTaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | — |
| 62 | CustAcctTaxRoundingRule | TAX_ROUNDING_RULE | — | — |
| 63 | PayingCustAcctAccountName | ACCOUNT_NAME | — | ✅ |
| 64 | PayingCustAcctCustAccountId | CUST_ACCOUNT_ID | — | — |
| 65 | PayingCustAcctPartyId | PARTY_ID | — | — |
| 66 | ShipToCustAcctAccountName | ACCOUNT_NAME | — | ✅ |
| 67 | ShipToCustAcctCustAccountId | CUST_ACCOUNT_ID | — | — |
| 68 | ShipToCustAcctPartyId | PARTY_ID | — | — |
| 69 | SoldToCustAcctAccountName | ACCOUNT_NAME | — | ✅ |
| 70 | SoldToCustAcctCustAccountId | CUST_ACCOUNT_ID | — | — |
| 71 | SoldToCustAcctPartyId | PARTY_ID | — | — |

### [[hz_cust_account_roles|HZ_CUST_ACCOUNT_ROLES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillToContactContactPersonId | CONTACT_PERSON_ID | — | — |
| 2 | BillToContactCustAccountRoleId | CUST_ACCOUNT_ROLE_ID | — | — |

### [[hz_cust_acct_sites_all|HZ_CUST_ACCT_SITES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayingSiteCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 2 | PayingSiteLanguage | ACCT_SITE_LANGUAGE | — | — |
| 3 | PayingSitePartySiteId | PARTY_SITE_ID | — | — |
| 4 | RmtToAddrSiteCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 5 | RmtToAddrSiteLanguage | ACCT_SITE_LANGUAGE | — | — |
| 6 | RmtToAddrSitePartySiteId | PARTY_SITE_ID | — | — |
| 7 | ShipToSiteCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 8 | ShipToSiteLanguage | ACCT_SITE_LANGUAGE | — | — |
| 9 | ShipToSitePartySiteId | PARTY_SITE_ID | — | — |
| 10 | SoldToSiteCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 11 | SoldToSiteLanguage | ACCT_SITE_LANGUAGE | — | — |
| 12 | SoldToSitePartySiteId | PARTY_SITE_ID | — | — |

### [[hz_cust_site_uses_all|HZ_CUST_SITE_USES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayingSiteUseCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 2 | PayingSiteUseSiteUseId | SITE_USE_ID | — | — |
| 3 | ShipToSiteUseCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 4 | ShipToSiteUseSiteUseId | SITE_USE_ID | — | — |
| 5 | SoldToSiteUseCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 6 | SoldToSiteUseSiteUseId | SITE_USE_ID | — | — |

### [[hz_locations|HZ_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RmtLocationAddress1 | ADDRESS1 | — | ✅ |
| 2 | RmtLocationAddress2 | ADDRESS2 | — | ✅ |
| 3 | RmtLocationAddress3 | ADDRESS3 | — | ✅ |
| 4 | RmtLocationAddress4 | ADDRESS4 | — | ✅ |
| 5 | RmtLocationCity | CITY | — | ✅ |
| 6 | RmtLocationCountry | COUNTRY | — | ✅ |
| 7 | RmtLocationCounty | COUNTY | — | ✅ |
| 8 | RmtLocationDescription | DESCRIPTION | — | — |
| 9 | RmtLocationLocationId | LOCATION_ID | — | — |
| 10 | RmtLocationPosition | POSITION | — | — |
| 11 | RmtLocationPostalCode | POSTAL_CODE | — | ✅ |
| 12 | RmtLocationProvince | PROVINCE | — | ✅ |
| 13 | RmtLocationState | STATE | — | ✅ |
| 14 | ShipToAddrLocationAddress1 | ADDRESS1 | — | ✅ |
| 15 | ShipToAddrLocationAddress2 | ADDRESS2 | — | ✅ |
| 16 | ShipToAddrLocationAddress3 | ADDRESS3 | — | ✅ |
| 17 | ShipToAddrLocationAddress4 | ADDRESS4 | — | ✅ |
| 18 | ShipToAddrLocationCity | CITY | — | ✅ |
| 19 | ShipToAddrLocationCountry | COUNTRY | — | ✅ |
| 20 | ShipToAddrLocationCounty | COUNTY | — | ✅ |
| 21 | ShipToAddrLocationDescription | DESCRIPTION | — | — |
| 22 | ShipToAddrLocationLocationId | LOCATION_ID | — | — |
| 23 | ShipToAddrLocationPosition | POSITION | — | — |
| 24 | ShipToAddrLocationPostalCode | POSTAL_CODE | — | ✅ |
| 25 | ShipToAddrLocationProvince | PROVINCE | — | ✅ |
| 26 | ShipToAddrLocationState | STATE | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillToContactPartyPartyId | PARTY_ID | — | — |
| 2 | BillToContactPartyPartyName | PARTY_NAME | — | ✅ |
| 3 | BillToContactPartyPartyNumber | PARTY_NUMBER | — | — |
| 4 | BillToContactPartyPartyType | PARTY_TYPE | — | — |
| 5 | BillToContactPartyPersonFirstName | PERSON_FIRST_NAME | — | — |
| 6 | BillToContactPartyPersonLastName | PERSON_LAST_NAME | — | — |
| 7 | BillToContactPartyPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 8 | BillToContactPartyPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 9 | BillToContactPartyPersonTitle | PERSON_TITLE | — | — |
| 10 | ShipToContactPartyPartyId | PARTY_ID | — | — |
| 11 | ShipToContactPartyPartyName | PARTY_NAME | — | ✅ |
| 12 | ShipToContactPartyPartyNumber | PARTY_NUMBER | — | — |
| 13 | ShipToContactPartyPartyType | PARTY_TYPE | — | — |
| 14 | ShipToContactPartyPersonFirstName | PERSON_FIRST_NAME | — | — |
| 15 | ShipToContactPartyPersonLastName | PERSON_LAST_NAME | — | — |
| 16 | ShipToContactPartyPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 17 | ShipToContactPartyPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 18 | ShipToContactPartyPersonTitle | PERSON_TITLE | — | — |
| 19 | SoldToContactPartyPartyId | PARTY_ID | — | — |
| 20 | SoldToContactPartyPartyName | PARTY_NAME | — | ✅ |
| 21 | SoldToContactPartyPartyNumber | PARTY_NUMBER | — | — |
| 22 | SoldToContactPartyPartyType | PARTY_TYPE | — | — |
| 23 | SoldToContactPartyPersonFirstName | PERSON_FIRST_NAME | — | — |
| 24 | SoldToContactPartyPersonLastName | PERSON_LAST_NAME | — | — |
| 25 | SoldToContactPartyPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 26 | SoldToContactPartyPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 27 | SoldToContactPartyPersonTitle | PERSON_TITLE | — | — |

### [[hz_party_sites|HZ_PARTY_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayingPartySitePartySiteId | PARTY_SITE_ID | — | — |
| 2 | PayingPartySitePartySiteName | PARTY_SITE_NAME | — | ✅ |
| 3 | RmtPartySiteLocationId | LOCATION_ID | — | — |
| 4 | RmtPartySitePartySiteId | PARTY_SITE_ID | — | — |
| 5 | RmtPartySitePartySiteName | PARTY_SITE_NAME | — | — |
| 6 | ShipToAddrPartySiteLocationId | LOCATION_ID | — | — |
| 7 | ShipToAddrPartySitePartySiteId | PARTY_SITE_ID | — | — |
| 8 | ShipToAddrPartySitePartySiteName | PARTY_SITE_NAME | — | — |
| 9 | ShipToPartySitePartySiteId | PARTY_SITE_ID | — | — |
| 10 | ShipToPartySitePartySiteName | PARTY_SITE_NAME | — | ✅ |
| 11 | SoldToPartySitePartySiteId | PARTY_SITE_ID | — | — |
| 12 | SoldToPartySitePartySiteName | PARTY_SITE_NAME | — | ✅ |

### [[hz_party_site_uses|HZ_PARTY_SITE_USES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ShipToPartySiteUseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | ShipToPartySiteUseLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 3 | ShipToPartySiteUsePartySiteUseId | PARTY_SITE_USE_ID | — | — |

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
| 35 | IbyExtBankAccountsPaymentFactorFlag | PAYMENT_FACTOR_FLAG | — | — |
| 36 | IbyExtBankAccountsProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 37 | IbyExtBankAccountsProgramId | PROGRAM_ID | — | — |
| 38 | IbyExtBankAccountsProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 39 | IbyExtBankAccountsRequestId | REQUEST_ID | — | — |
| 40 | IbyExtBankAccountsSaltVersion | SALT_VERSION | — | — |
| 41 | IbyExtBankAccountsSecondaryAccountReference | SECONDARY_ACCOUNT_REFERENCE | — | — |
| 42 | IbyExtBankAccountsShortAcctName | SHORT_ACCT_NAME | — | — |
| 43 | IbyExtBankAccountsStartDate | START_DATE | — | — |
| 44 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |

### [[iby_fndcpt_tx_extensions|IBY_FNDCPT_TX_EXTENSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrxExtnHdrAdditionalInfo | ADDITIONAL_INFO | — | — |
| 2 | TrxExtnHdrEncrypted | ENCRYPTED | — | — |
| 3 | TrxExtnHdrInstrSecCodeLength | INSTR_SEC_CODE_LENGTH | — | — |
| 4 | TrxExtnHdrInstrumentSecurityCode | INSTRUMENT_SECURITY_CODE | — | — |
| 5 | TrxExtnHdrPaymentChannelCode | PAYMENT_CHANNEL_CODE | — | — |
| 6 | TrxExtnHdrPaymentSystemOrderNumber | PAYMENT_SYSTEM_ORDER_NUMBER | — | ✅ |
| 7 | TrxExtnHdrPoLineNumber | PO_LINE_NUMBER | — | — |
| 8 | TrxExtnHdrPoNumber | PO_NUMBER | — | — |
| 9 | TrxExtnHdrTrxnExtensionId | TRXN_EXTENSION_ID | — | — |
| 10 | TrxExtnHdrTrxnRefNumber1 | TRXN_REF_NUMBER1 | — | — |
| 11 | TrxExtnHdrTrxnRefNumber2 | TRXN_REF_NUMBER2 | — | — |
| 12 | TrxExtnHdrVoiceAuthorizationCode | VOICE_AUTHORIZATION_CODE | — | — |
| 13 | TrxExtnHdrVoiceAuthorizationDate | VOICE_AUTHORIZATION_DATE | — | — |
| 14 | TrxExtnHdrVoiceAuthorizationFlag | VOICE_AUTHORIZATION_FLAG | — | — |
| 15 | TrxExtnLineAdditionalInfo | ADDITIONAL_INFO | — | — |
| 16 | TrxExtnLineEncrypted | ENCRYPTED | — | — |
| 17 | TrxExtnLineInstrSecCodeLength | INSTR_SEC_CODE_LENGTH | — | — |
| 18 | TrxExtnLineInstrumentSecurityCode | INSTRUMENT_SECURITY_CODE | — | — |
| 19 | TrxExtnLinePaymentChannelCode | PAYMENT_CHANNEL_CODE | — | — |
| 20 | TrxExtnLinePaymentSystemOrderNumber | PAYMENT_SYSTEM_ORDER_NUMBER | — | ✅ |
| 21 | TrxExtnLinePoLineNumber | PO_LINE_NUMBER | — | — |
| 22 | TrxExtnLinePoNumber | PO_NUMBER | — | — |
| 23 | TrxExtnLineTrxnExtensionId | TRXN_EXTENSION_ID | — | — |
| 24 | TrxExtnLineTrxnRefNumber1 | TRXN_REF_NUMBER1 | — | — |
| 25 | TrxExtnLineTrxnRefNumber2 | TRXN_REF_NUMBER2 | — | — |
| 26 | TrxExtnLineVoiceAuthorizationCode | VOICE_AUTHORIZATION_CODE | — | — |
| 27 | TrxExtnLineVoiceAuthorizationDate | VOICE_AUTHORIZATION_DATE | — | — |
| 28 | TrxExtnLineVoiceAuthorizationFlag | VOICE_AUTHORIZATION_FLAG | — | — |

### [[inv_units_of_measure_b|INV_UNITS_OF_MEASURE_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UomJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 2 | UomUnitOfMeasureId | UNIT_OF_MEASURE_ID | — | — |
| 3 | UomUomCode | UOM_CODE | — | — |

### [[inv_units_of_measure_tl|INV_UNITS_OF_MEASURE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UomDescription | DESCRIPTION | — | ✅ |
| 2 | UomTLLanguage | LANGUAGE | — | — |
| 3 | UomTLUnitOfMeasureId | UNIT_OF_MEASURE_ID | — | — |
| 4 | UomUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | PersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | UserCreatedByUserGuid | USER_GUID | — | — |
| 3 | UserCreatedByUserId | USER_ID | — | — |
| 4 | UserCreatedByUsername | USERNAME | — | — |
| 5 | UserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 7 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 8 | UserUpdatedByUserId | USER_ID | — | — |
| 9 | UserUpdatedByUsername | USERNAME | — | — |

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
| 43 | TransactionBatchSourceName | NAME | — | ✅ |
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
| 1 | OriginalTransactionCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 2 | OriginalTransactionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | OriginalTransactionTrxNumber | TRX_NUMBER | — | ✅ |
| 4 | RelCustTrxHdrCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 5 | RelCustTrxHdrObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | RelCustTrxHdrTrxNumber | TRX_NUMBER | — | ✅ |
| 7 | TransactionHeaderAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 8 | TransactionHeaderAgreementId | AGREEMENT_ID | — | — |
| 9 | TransactionHeaderApplicationId | APPLICATION_ID | — | — |
| 10 | TransactionHeaderApprovalCode | APPROVAL_CODE | — | — |
| 11 | TransactionHeaderAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 12 | TransactionHeaderBRAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 13 | TransactionHeaderBRAgreementId | AGREEMENT_ID | — | — |
| 14 | TransactionHeaderBRApplicationId | APPLICATION_ID | — | — |
| 15 | TransactionHeaderBRApprovalCode | APPROVAL_CODE | — | — |
| 16 | TransactionHeaderBRAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 17 | TransactionHeaderBRBatchId | BATCH_ID | — | — |
| 18 | TransactionHeaderBRBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 19 | TransactionHeaderBRBillTemplateId | BILL_TEMPLATE_ID | — | — |
| 20 | TransactionHeaderBRBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 21 | TransactionHeaderBRBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 22 | TransactionHeaderBRBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 23 | TransactionHeaderBRBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 24 | TransactionHeaderBRBillingDate | BILLING_DATE | — | — |
| 25 | TransactionHeaderBRBrAmount | BR_AMOUNT | — | — |
| 26 | TransactionHeaderBRBrOnHoldFlag | BR_ON_HOLD_FLAG | — | — |
| 27 | TransactionHeaderBRBrUnpaidFlag | BR_UNPAID_FLAG | — | — |
| 28 | TransactionHeaderBRCcErrorCode | CC_ERROR_CODE | — | — |
| 29 | TransactionHeaderBRCcErrorFlag | CC_ERROR_FLAG | — | — |
| 30 | TransactionHeaderBRCcErrorText | CC_ERROR_TEXT | — | — |
| 31 | TransactionHeaderBRCompleteFlag | COMPLETE_FLAG | — | — |
| 32 | TransactionHeaderBRContractId | CONTRACT_ID | — | — |
| 33 | TransactionHeaderBRCreatedBy | CREATED_BY | — | — |
| 34 | TransactionHeaderBRCreatedFrom | CREATED_FROM | — | — |
| 35 | TransactionHeaderBRCreationDate | CREATION_DATE | — | — |
| 36 | TransactionHeaderBRCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | — |
| 37 | TransactionHeaderBRCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | — |
| 38 | TransactionHeaderBRCtReference | CT_REFERENCE | — | — |
| 39 | TransactionHeaderBRCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 40 | TransactionHeaderBRCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 41 | TransactionHeaderBRCustomerReference | CUSTOMER_REFERENCE | — | — |
| 42 | TransactionHeaderBRCustomerReferenceDate | CUSTOMER_REFERENCE_DATE | — | — |
| 43 | TransactionHeaderBRCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 44 | TransactionHeaderBRDefaultTaxExemptFlag | DEFAULT_TAX_EXEMPT_FLAG | — | — |
| 45 | TransactionHeaderBRDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 46 | TransactionHeaderBRDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 47 | TransactionHeaderBRDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 48 | TransactionHeaderBRDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 49 | TransactionHeaderBRDraweeBankAccountId | DRAWEE_BANK_ACCOUNT_ID | — | — |
| 50 | TransactionHeaderBRDraweeContactId | DRAWEE_CONTACT_ID | — | — |
| 51 | TransactionHeaderBRDraweeId | DRAWEE_ID | — | — |
| 52 | TransactionHeaderBRDraweeSiteUseId | DRAWEE_SITE_USE_ID | — | — |
| 53 | TransactionHeaderBREdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 54 | TransactionHeaderBREdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 55 | TransactionHeaderBREndDateCommitment | END_DATE_COMMITMENT | — | — |
| 56 | TransactionHeaderBRExchangeDate | EXCHANGE_DATE | — | — |
| 57 | TransactionHeaderBRExchangeRate | EXCHANGE_RATE | — | — |
| 58 | TransactionHeaderBRExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 59 | TransactionHeaderBRFinanceCharges | FINANCE_CHARGES | — | — |
| 60 | TransactionHeaderBRFobPoint | FOB_POINT | — | — |
| 61 | TransactionHeaderBRInitialCustomerTrxId | INITIAL_CUSTOMER_TRX_ID | — | — |
| 62 | TransactionHeaderBRIntercompanyFlag | INTERCOMPANY_FLAG | — | — |
| 63 | TransactionHeaderBRInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 64 | TransactionHeaderBRInterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | — |
| 65 | TransactionHeaderBRInterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | — |
| 66 | TransactionHeaderBRInterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | — |
| 67 | TransactionHeaderBRInterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | — |
| 68 | TransactionHeaderBRInterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | — |
| 69 | TransactionHeaderBRInterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | — |
| 70 | TransactionHeaderBRInterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | — |
| 71 | TransactionHeaderBRInterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | — |
| 72 | TransactionHeaderBRInterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | — |
| 73 | TransactionHeaderBRInterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | — |
| 74 | TransactionHeaderBRInterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | — |
| 75 | TransactionHeaderBRInterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | — |
| 76 | TransactionHeaderBRInterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | — |
| 77 | TransactionHeaderBRInterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | — |
| 78 | TransactionHeaderBRInterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | — |
| 79 | TransactionHeaderBRInterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | — |
| 80 | TransactionHeaderBRInternalNotes | INTERNAL_NOTES | — | — |
| 81 | TransactionHeaderBRInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 82 | TransactionHeaderBRInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 83 | TransactionHeaderBRLastPrintedSequenceNum | LAST_PRINTED_SEQUENCE_NUM | — | — |
| 84 | TransactionHeaderBRLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 85 | TransactionHeaderBRLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 86 | TransactionHeaderBRLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 87 | TransactionHeaderBRLateChargesAssessed | LATE_CHARGES_ASSESSED | — | — |
| 88 | TransactionHeaderBRLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 89 | TransactionHeaderBRObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 90 | TransactionHeaderBROldTrxNumber | OLD_TRX_NUMBER | — | — |
| 91 | TransactionHeaderBROrgId | ORG_ID | — | — |
| 92 | TransactionHeaderBROrigSystemBatchName | ORIG_SYSTEM_BATCH_NAME | — | — |
| 93 | TransactionHeaderBROverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 94 | TransactionHeaderBRPayingCustomerId | PAYING_CUSTOMER_ID | — | — |
| 95 | TransactionHeaderBRPayingSiteUseId | PAYING_SITE_USE_ID | — | — |
| 96 | TransactionHeaderBRPaymentAttributes | PAYMENT_ATTRIBUTES | — | — |
| 97 | TransactionHeaderBRPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 98 | TransactionHeaderBRPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 99 | TransactionHeaderBRPostRequestId | POST_REQUEST_ID | — | — |
| 100 | TransactionHeaderBRPostingControlId | POSTING_CONTROL_ID | — | — |
| 101 | TransactionHeaderBRPrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 102 | TransactionHeaderBRPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 103 | TransactionHeaderBRPrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | — |
| 104 | TransactionHeaderBRPrintingCount | PRINTING_COUNT | — | — |
| 105 | TransactionHeaderBRPrintingLastPrinted | PRINTING_LAST_PRINTED | — | — |
| 106 | TransactionHeaderBRPrintingOption | PRINTING_OPTION | — | — |
| 107 | TransactionHeaderBRPrintingOriginalDate | PRINTING_ORIGINAL_DATE | — | — |
| 108 | TransactionHeaderBRPrintingPending | PRINTING_PENDING | — | — |
| 109 | TransactionHeaderBRProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 110 | TransactionHeaderBRProgramId | PROGRAM_ID | — | — |
| 111 | TransactionHeaderBRProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 112 | TransactionHeaderBRPurchaseOrder | PURCHASE_ORDER | — | — |
| 113 | TransactionHeaderBRPurchaseOrderDate | PURCHASE_ORDER_DATE | — | — |
| 114 | TransactionHeaderBRPurchaseOrderRevision | PURCHASE_ORDER_REVISION | — | — |
| 115 | TransactionHeaderBRRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 116 | TransactionHeaderBRReasonCode | REASON_CODE | — | — |
| 117 | TransactionHeaderBRReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 118 | TransactionHeaderBRRecurredFromTrxNumber | RECURRED_FROM_TRX_NUMBER | — | — |
| 119 | TransactionHeaderBRRelatedBatchSourceSeqId | RELATED_BATCH_SOURCE_SEQ_ID | — | — |
| 120 | TransactionHeaderBRRelatedCustomerTrxId | RELATED_CUSTOMER_TRX_ID | — | — |
| 121 | TransactionHeaderBRRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 122 | TransactionHeaderBRRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 123 | TransactionHeaderBRRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 124 | TransactionHeaderBRRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 125 | TransactionHeaderBRRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 126 | TransactionHeaderBRRequestId | REQUEST_ID | — | — |
| 127 | TransactionHeaderBRReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 128 | TransactionHeaderBRSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 129 | TransactionHeaderBRShipDateActual | SHIP_DATE_ACTUAL | — | — |
| 130 | TransactionHeaderBRShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 131 | TransactionHeaderBRShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 132 | TransactionHeaderBRShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 133 | TransactionHeaderBRShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 134 | TransactionHeaderBRShipVia | SHIP_VIA | — | — |
| 135 | TransactionHeaderBRShipmentId | SHIPMENT_ID | — | — |
| 136 | TransactionHeaderBRSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 137 | TransactionHeaderBRSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 138 | TransactionHeaderBRSoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | — |
| 139 | TransactionHeaderBRSourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 140 | TransactionHeaderBRSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 141 | TransactionHeaderBRSpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 142 | TransactionHeaderBRStartDateCommitment | START_DATE_COMMITMENT | — | — |
| 143 | TransactionHeaderBRStatusTrx | STATUS_TRX | — | — |
| 144 | TransactionHeaderBRTermDueDate | TERM_DUE_DATE | — | — |
| 145 | TransactionHeaderBRTermId | TERM_ID | — | — |
| 146 | TransactionHeaderBRTerritoryId | TERRITORY_ID | — | — |
| 147 | TransactionHeaderBRTrxClass | TRX_CLASS | — | — |
| 148 | TransactionHeaderBRTrxDate | TRX_DATE | — | — |
| 149 | TransactionHeaderBRTrxNumber | TRX_NUMBER | — | — |
| 150 | TransactionHeaderBRUpgradeMethod | UPGRADE_METHOD | — | — |
| 151 | TransactionHeaderBRWaybillNumber | WAYBILL_NUMBER | — | — |
| 152 | TransactionHeaderBRWhUpdateDate | WH_UPDATE_DATE | — | — |
| 153 | TransactionHeaderBatchId | BATCH_ID | — | — |
| 154 | TransactionHeaderBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 155 | TransactionHeaderBillTemplateId | BILL_TEMPLATE_ID | — | ✅ |
| 156 | TransactionHeaderBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 157 | TransactionHeaderBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 158 | TransactionHeaderBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 159 | TransactionHeaderBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 160 | TransactionHeaderBillingDate | BILLING_DATE | — | ✅ |
| 161 | TransactionHeaderBrAmount | BR_AMOUNT | — | — |
| 162 | TransactionHeaderBrOnHoldFlag | BR_ON_HOLD_FLAG | — | ✅ |
| 163 | TransactionHeaderBrUnpaidFlag | BR_UNPAID_FLAG | — | — |
| 164 | TransactionHeaderCcErrorCode | CC_ERROR_CODE | — | — |
| 165 | TransactionHeaderCcErrorFlag | CC_ERROR_FLAG | — | — |
| 166 | TransactionHeaderCcErrorText | CC_ERROR_TEXT | — | — |
| 167 | TransactionHeaderComments | COMMENTS | — | ✅ |
| 168 | TransactionHeaderCompleteFlag | COMPLETE_FLAG | — | ✅ |
| 169 | TransactionHeaderContractId | CONTRACT_ID | — | — |
| 170 | TransactionHeaderCreatedBy | CREATED_BY | — | ✅ |
| 171 | TransactionHeaderCreatedFrom | CREATED_FROM | — | ✅ |
| 172 | TransactionHeaderCreationDate | CREATION_DATE | — | ✅ |
| 173 | TransactionHeaderCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | ✅ |
| 174 | TransactionHeaderCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | ✅ |
| 175 | TransactionHeaderCtReference | CT_REFERENCE | — | ✅ |
| 176 | TransactionHeaderCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 177 | TransactionHeaderCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 178 | TransactionHeaderCustomerReference | CUSTOMER_REFERENCE | — | ✅ |
| 179 | TransactionHeaderCustomerReferenceDate | CUSTOMER_REFERENCE_DATE | — | ✅ |
| 180 | TransactionHeaderCustomerTrxId | CUSTOMER_TRX_ID | — | ✅ |
| 181 | TransactionHeaderDefaultTaxExemptFlag | DEFAULT_TAX_EXEMPT_FLAG | — | ✅ |
| 182 | TransactionHeaderDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | ✅ |
| 183 | TransactionHeaderDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 184 | TransactionHeaderDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 185 | TransactionHeaderDelContactEmailAddress | DEL_CONTACT_EMAIL_ADDRESS | — | — |
| 186 | TransactionHeaderDeliveryMethodCode | DELIVERY_METHOD_CODE | — | — |
| 187 | TransactionHeaderDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 188 | TransactionHeaderDocSequenceValue | DOC_SEQUENCE_VALUE | — | ✅ |
| 189 | TransactionHeaderDocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 190 | TransactionHeaderDraweeBankAccountId | DRAWEE_BANK_ACCOUNT_ID | — | — |
| 191 | TransactionHeaderDraweeContactId | DRAWEE_CONTACT_ID | — | — |
| 192 | TransactionHeaderDraweeId | DRAWEE_ID | — | — |
| 193 | TransactionHeaderDraweeSiteUseId | DRAWEE_SITE_USE_ID | — | — |
| 194 | TransactionHeaderEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 195 | TransactionHeaderEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 196 | TransactionHeaderEndDateCommitment | END_DATE_COMMITMENT | — | ✅ |
| 197 | TransactionHeaderExchangeDate | EXCHANGE_DATE | — | ✅ |
| 198 | TransactionHeaderExchangeRate | EXCHANGE_RATE | — | ✅ |
| 199 | TransactionHeaderExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 200 | TransactionHeaderFinanceCharges | FINANCE_CHARGES | — | ✅ |
| 201 | TransactionHeaderFobPoint | FOB_POINT | — | ✅ |
| 202 | TransactionHeaderInitialCustomerTrxId | INITIAL_CUSTOMER_TRX_ID | — | — |
| 203 | TransactionHeaderIntercompanyFlag | INTERCOMPANY_FLAG | — | ✅ |
| 204 | TransactionHeaderInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 205 | TransactionHeaderInterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | ✅ |
| 206 | TransactionHeaderInterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | ✅ |
| 207 | TransactionHeaderInterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | ✅ |
| 208 | TransactionHeaderInterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | ✅ |
| 209 | TransactionHeaderInterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | ✅ |
| 210 | TransactionHeaderInterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | ✅ |
| 211 | TransactionHeaderInterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | ✅ |
| 212 | TransactionHeaderInterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | ✅ |
| 213 | TransactionHeaderInterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | ✅ |
| 214 | TransactionHeaderInterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | ✅ |
| 215 | TransactionHeaderInterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | ✅ |
| 216 | TransactionHeaderInterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | ✅ |
| 217 | TransactionHeaderInterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | ✅ |
| 218 | TransactionHeaderInterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | ✅ |
| 219 | TransactionHeaderInterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | ✅ |
| 220 | TransactionHeaderInterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | ✅ |
| 221 | TransactionHeaderInternalNotes | INTERNAL_NOTES | — | ✅ |
| 222 | TransactionHeaderInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 223 | TransactionHeaderInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 224 | TransactionHeaderLastPrintedSequenceNum | LAST_PRINTED_SEQUENCE_NUM | — | ✅ |
| 225 | TransactionHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 226 | TransactionHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 227 | TransactionHeaderLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 228 | TransactionHeaderLateChargesAssessed | LATE_CHARGES_ASSESSED | — | ✅ |
| 229 | TransactionHeaderLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 230 | TransactionHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 231 | TransactionHeaderOldTrxNumber | OLD_TRX_NUMBER | — | — |
| 232 | TransactionHeaderOrgId | ORG_ID | — | — |
| 233 | TransactionHeaderOrigSystemBatchName | ORIG_SYSTEM_BATCH_NAME | — | ✅ |
| 234 | TransactionHeaderOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 235 | TransactionHeaderPayingCustomerId | PAYING_CUSTOMER_ID | — | — |
| 236 | TransactionHeaderPayingSiteUseId | PAYING_SITE_USE_ID | — | — |
| 237 | TransactionHeaderPaymentAttributes | PAYMENT_ATTRIBUTES | — | — |
| 238 | TransactionHeaderPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 239 | TransactionHeaderPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 240 | TransactionHeaderPostRequestId | POST_REQUEST_ID | — | — |
| 241 | TransactionHeaderPostingControlId | POSTING_CONTROL_ID | — | — |
| 242 | TransactionHeaderPrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 243 | TransactionHeaderPreviousAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 244 | TransactionHeaderPreviousAgreementId | AGREEMENT_ID | — | — |
| 245 | TransactionHeaderPreviousApplicationId | APPLICATION_ID | — | — |
| 246 | TransactionHeaderPreviousApprovalCode | APPROVAL_CODE | — | — |
| 247 | TransactionHeaderPreviousAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 248 | TransactionHeaderPreviousBatchId | BATCH_ID | — | — |
| 249 | TransactionHeaderPreviousBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 250 | TransactionHeaderPreviousBillTemplateId | BILL_TEMPLATE_ID | — | — |
| 251 | TransactionHeaderPreviousBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 252 | TransactionHeaderPreviousBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 253 | TransactionHeaderPreviousBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 254 | TransactionHeaderPreviousBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 255 | TransactionHeaderPreviousBillingDate | BILLING_DATE | — | — |
| 256 | TransactionHeaderPreviousBrAmount | BR_AMOUNT | — | — |
| 257 | TransactionHeaderPreviousBrOnHoldFlag | BR_ON_HOLD_FLAG | — | — |
| 258 | TransactionHeaderPreviousBrUnpaidFlag | BR_UNPAID_FLAG | — | — |
| 259 | TransactionHeaderPreviousCcErrorCode | CC_ERROR_CODE | — | — |
| 260 | TransactionHeaderPreviousCcErrorFlag | CC_ERROR_FLAG | — | — |
| 261 | TransactionHeaderPreviousCcErrorText | CC_ERROR_TEXT | — | — |
| 262 | TransactionHeaderPreviousCompleteFlag | COMPLETE_FLAG | — | — |
| 263 | TransactionHeaderPreviousContractId | CONTRACT_ID | — | — |
| 264 | TransactionHeaderPreviousCreatedBy | CREATED_BY | — | — |
| 265 | TransactionHeaderPreviousCreatedFrom | CREATED_FROM | — | — |
| 266 | TransactionHeaderPreviousCreationDate | CREATION_DATE | — | — |
| 267 | TransactionHeaderPreviousCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | — |
| 268 | TransactionHeaderPreviousCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | — |
| 269 | TransactionHeaderPreviousCtReference | CT_REFERENCE | — | — |
| 270 | TransactionHeaderPreviousCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 271 | TransactionHeaderPreviousCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 272 | TransactionHeaderPreviousCustomerReference | CUSTOMER_REFERENCE | — | — |
| 273 | TransactionHeaderPreviousCustomerReferenceDate | CUSTOMER_REFERENCE_DATE | — | — |
| 274 | TransactionHeaderPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 275 | TransactionHeaderPreviousCustomerTrxId1 | CUSTOMER_TRX_ID | — | — |
| 276 | TransactionHeaderPreviousDefaultTaxExemptFlag | DEFAULT_TAX_EXEMPT_FLAG | — | — |
| 277 | TransactionHeaderPreviousDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 278 | TransactionHeaderPreviousDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 279 | TransactionHeaderPreviousDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 280 | TransactionHeaderPreviousDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 281 | TransactionHeaderPreviousDraweeBankAccountId | DRAWEE_BANK_ACCOUNT_ID | — | — |
| 282 | TransactionHeaderPreviousDraweeContactId | DRAWEE_CONTACT_ID | — | — |
| 283 | TransactionHeaderPreviousDraweeId | DRAWEE_ID | — | — |
| 284 | TransactionHeaderPreviousDraweeSiteUseId | DRAWEE_SITE_USE_ID | — | — |
| 285 | TransactionHeaderPreviousEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 286 | TransactionHeaderPreviousEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 287 | TransactionHeaderPreviousEndDateCommitment | END_DATE_COMMITMENT | — | — |
| 288 | TransactionHeaderPreviousExchangeDate | EXCHANGE_DATE | — | — |
| 289 | TransactionHeaderPreviousExchangeRate | EXCHANGE_RATE | — | — |
| 290 | TransactionHeaderPreviousExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 291 | TransactionHeaderPreviousFinanceCharges | FINANCE_CHARGES | — | — |
| 292 | TransactionHeaderPreviousFobPoint | FOB_POINT | — | — |
| 293 | TransactionHeaderPreviousInitialCustomerTrxId | INITIAL_CUSTOMER_TRX_ID | — | — |
| 294 | TransactionHeaderPreviousIntercompanyFlag | INTERCOMPANY_FLAG | — | — |
| 295 | TransactionHeaderPreviousInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 296 | TransactionHeaderPreviousInterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | — |
| 297 | TransactionHeaderPreviousInterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | — |
| 298 | TransactionHeaderPreviousInterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | — |
| 299 | TransactionHeaderPreviousInterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | — |
| 300 | TransactionHeaderPreviousInterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | — |
| 301 | TransactionHeaderPreviousInterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | — |
| 302 | TransactionHeaderPreviousInterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | — |
| 303 | TransactionHeaderPreviousInterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | — |
| 304 | TransactionHeaderPreviousInterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | — |
| 305 | TransactionHeaderPreviousInterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | — |
| 306 | TransactionHeaderPreviousInterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | — |
| 307 | TransactionHeaderPreviousInterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | — |
| 308 | TransactionHeaderPreviousInterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | — |
| 309 | TransactionHeaderPreviousInterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | — |
| 310 | TransactionHeaderPreviousInterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | — |
| 311 | TransactionHeaderPreviousInterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | — |
| 312 | TransactionHeaderPreviousInternalNotes | INTERNAL_NOTES | — | — |
| 313 | TransactionHeaderPreviousInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 314 | TransactionHeaderPreviousInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 315 | TransactionHeaderPreviousLastPrintedSequenceNum | LAST_PRINTED_SEQUENCE_NUM | — | — |
| 316 | TransactionHeaderPreviousLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 317 | TransactionHeaderPreviousLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 318 | TransactionHeaderPreviousLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 319 | TransactionHeaderPreviousLateChargesAssessed | LATE_CHARGES_ASSESSED | — | — |
| 320 | TransactionHeaderPreviousLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 321 | TransactionHeaderPreviousObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 322 | TransactionHeaderPreviousOldTrxNumber | OLD_TRX_NUMBER | — | — |
| 323 | TransactionHeaderPreviousOrgId | ORG_ID | — | — |
| 324 | TransactionHeaderPreviousOrigSystemBatchName | ORIG_SYSTEM_BATCH_NAME | — | — |
| 325 | TransactionHeaderPreviousOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 326 | TransactionHeaderPreviousPayingCustomerId | PAYING_CUSTOMER_ID | — | — |
| 327 | TransactionHeaderPreviousPayingSiteUseId | PAYING_SITE_USE_ID | — | — |
| 328 | TransactionHeaderPreviousPaymentAttributes | PAYMENT_ATTRIBUTES | — | — |
| 329 | TransactionHeaderPreviousPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 330 | TransactionHeaderPreviousPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 331 | TransactionHeaderPreviousPostRequestId | POST_REQUEST_ID | — | — |
| 332 | TransactionHeaderPreviousPostingControlId | POSTING_CONTROL_ID | — | — |
| 333 | TransactionHeaderPreviousPrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 334 | TransactionHeaderPreviousPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 335 | TransactionHeaderPreviousPrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | — |
| 336 | TransactionHeaderPreviousPrintingCount | PRINTING_COUNT | — | — |
| 337 | TransactionHeaderPreviousPrintingLastPrinted | PRINTING_LAST_PRINTED | — | — |
| 338 | TransactionHeaderPreviousPrintingOption | PRINTING_OPTION | — | — |
| 339 | TransactionHeaderPreviousPrintingOriginalDate | PRINTING_ORIGINAL_DATE | — | — |
| 340 | TransactionHeaderPreviousPrintingPending | PRINTING_PENDING | — | — |
| 341 | TransactionHeaderPreviousProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 342 | TransactionHeaderPreviousProgramId | PROGRAM_ID | — | — |
| 343 | TransactionHeaderPreviousProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 344 | TransactionHeaderPreviousPurchaseOrder | PURCHASE_ORDER | — | — |
| 345 | TransactionHeaderPreviousPurchaseOrderDate | PURCHASE_ORDER_DATE | — | — |
| 346 | TransactionHeaderPreviousPurchaseOrderRevision | PURCHASE_ORDER_REVISION | — | — |
| 347 | TransactionHeaderPreviousRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 348 | TransactionHeaderPreviousReasonCode | REASON_CODE | — | — |
| 349 | TransactionHeaderPreviousReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 350 | TransactionHeaderPreviousRecurredFromTrxNumber | RECURRED_FROM_TRX_NUMBER | — | — |
| 351 | TransactionHeaderPreviousRelatedBatchSourceSeqId | RELATED_BATCH_SOURCE_SEQ_ID | — | — |
| 352 | TransactionHeaderPreviousRelatedCustomerTrxId | RELATED_CUSTOMER_TRX_ID | — | — |
| 353 | TransactionHeaderPreviousRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 354 | TransactionHeaderPreviousRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 355 | TransactionHeaderPreviousRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 356 | TransactionHeaderPreviousRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 357 | TransactionHeaderPreviousRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 358 | TransactionHeaderPreviousRequestId | REQUEST_ID | — | — |
| 359 | TransactionHeaderPreviousReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 360 | TransactionHeaderPreviousSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 361 | TransactionHeaderPreviousShipDateActual | SHIP_DATE_ACTUAL | — | — |
| 362 | TransactionHeaderPreviousShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 363 | TransactionHeaderPreviousShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 364 | TransactionHeaderPreviousShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 365 | TransactionHeaderPreviousShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 366 | TransactionHeaderPreviousShipVia | SHIP_VIA | — | — |
| 367 | TransactionHeaderPreviousShipmentId | SHIPMENT_ID | — | — |
| 368 | TransactionHeaderPreviousSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 369 | TransactionHeaderPreviousSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 370 | TransactionHeaderPreviousSoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | — |
| 371 | TransactionHeaderPreviousSourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 372 | TransactionHeaderPreviousSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 373 | TransactionHeaderPreviousSpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 374 | TransactionHeaderPreviousStartDateCommitment | START_DATE_COMMITMENT | — | — |
| 375 | TransactionHeaderPreviousStatusTrx | STATUS_TRX | — | — |
| 376 | TransactionHeaderPreviousTermDueDate | TERM_DUE_DATE | — | — |
| 377 | TransactionHeaderPreviousTermId | TERM_ID | — | — |
| 378 | TransactionHeaderPreviousTerritoryId | TERRITORY_ID | — | — |
| 379 | TransactionHeaderPreviousTrxClass | TRX_CLASS | — | — |
| 380 | TransactionHeaderPreviousTrxDate | TRX_DATE | — | — |
| 381 | TransactionHeaderPreviousTrxNumber | TRX_NUMBER | — | ✅ |
| 382 | TransactionHeaderPreviousUpgradeMethod | UPGRADE_METHOD | — | — |
| 383 | TransactionHeaderPreviousWaybillNumber | WAYBILL_NUMBER | — | — |
| 384 | TransactionHeaderPreviousWhUpdateDate | WH_UPDATE_DATE | — | — |
| 385 | TransactionHeaderPrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | — |
| 386 | TransactionHeaderPrintingCount | PRINTING_COUNT | — | ✅ |
| 387 | TransactionHeaderPrintingLastPrinted | PRINTING_LAST_PRINTED | — | ✅ |
| 388 | TransactionHeaderPrintingOption | PRINTING_OPTION | — | ✅ |
| 389 | TransactionHeaderPrintingOriginalDate | PRINTING_ORIGINAL_DATE | — | ✅ |
| 390 | TransactionHeaderPrintingPending | PRINTING_PENDING | — | ✅ |
| 391 | TransactionHeaderProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 392 | TransactionHeaderProgramId | PROGRAM_ID | — | — |
| 393 | TransactionHeaderProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 394 | TransactionHeaderPurchaseOrder | PURCHASE_ORDER | — | ✅ |
| 395 | TransactionHeaderPurchaseOrderDate | PURCHASE_ORDER_DATE | — | ✅ |
| 396 | TransactionHeaderPurchaseOrderRevision | PURCHASE_ORDER_REVISION | — | ✅ |
| 397 | TransactionHeaderRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 398 | TransactionHeaderReasonCode | REASON_CODE | — | ✅ |
| 399 | TransactionHeaderReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 400 | TransactionHeaderRecurredFromTrxNumber | RECURRED_FROM_TRX_NUMBER | — | — |
| 401 | TransactionHeaderRelatedBatchSourceSeqId | RELATED_BATCH_SOURCE_SEQ_ID | — | — |
| 402 | TransactionHeaderRelatedCustomerTrxId | RELATED_CUSTOMER_TRX_ID | — | — |
| 403 | TransactionHeaderRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 404 | TransactionHeaderRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 405 | TransactionHeaderRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 406 | TransactionHeaderRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 407 | TransactionHeaderRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 408 | TransactionHeaderRequestId | REQUEST_ID | — | — |
| 409 | TransactionHeaderRequiresManualScheduling | REQUIRES_MANUAL_SCHEDULING | — | ✅ |
| 410 | TransactionHeaderRevRecApplication | REV_REC_APPLICATION | — | ✅ |
| 411 | TransactionHeaderReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 412 | TransactionHeaderSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 413 | TransactionHeaderShipDateActual | SHIP_DATE_ACTUAL | — | ✅ |
| 414 | TransactionHeaderShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 415 | TransactionHeaderShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 416 | TransactionHeaderShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 417 | TransactionHeaderShipToPartyId | SHIP_TO_PARTY_ID | — | — |
| 418 | TransactionHeaderShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 419 | TransactionHeaderShipVia | SHIP_VIA | — | ✅ |
| 420 | TransactionHeaderShipmentId | SHIPMENT_ID | — | — |
| 421 | TransactionHeaderSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 422 | TransactionHeaderSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 423 | TransactionHeaderSoldToPartyId | SOLD_TO_PARTY_ID | — | — |
| 424 | TransactionHeaderSoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | — |
| 425 | TransactionHeaderSourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 426 | TransactionHeaderSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 427 | TransactionHeaderSpecialInstructions | SPECIAL_INSTRUCTIONS | — | ✅ |
| 428 | TransactionHeaderStartDateCommitment | START_DATE_COMMITMENT | — | ✅ |
| 429 | TransactionHeaderStatusTrx | STATUS_TRX | — | ✅ |
| 430 | TransactionHeaderTermDueDate | TERM_DUE_DATE | — | ✅ |
| 431 | TransactionHeaderTermId | TERM_ID | — | — |
| 432 | TransactionHeaderTerritoryId | TERRITORY_ID | — | — |
| 433 | TransactionHeaderTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 434 | TransactionHeaderTrxClass | TRX_CLASS | — | ✅ |
| 435 | TransactionHeaderTrxDate | TRX_DATE | — | ✅ |
| 436 | TransactionHeaderTrxNumber | TRX_NUMBER | — | ✅ |
| 437 | TransactionHeaderUpgradeMethod | UPGRADE_METHOD | — | — |
| 438 | TransactionHeaderUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | ✅ |
| 439 | TransactionHeaderWaybillNumber | WAYBILL_NUMBER | — | ✅ |
| 440 | TransactionHeaderWhUpdateDate | WH_UPDATE_DATE | — | — |
| 441 | TrxHeaderPrevAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 442 | TrxHeaderPrevAgreementId | AGREEMENT_ID | — | — |
| 443 | TrxHeaderPrevApplicationId | APPLICATION_ID | — | — |
| 444 | TrxHeaderPrevApprovalCode | APPROVAL_CODE | — | — |
| 445 | TrxHeaderPrevAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 446 | TrxHeaderPrevBatchId | BATCH_ID | — | — |
| 447 | TrxHeaderPrevBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 448 | TrxHeaderPrevBillTemplateId | BILL_TEMPLATE_ID | — | — |
| 449 | TrxHeaderPrevBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 450 | TrxHeaderPrevBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 451 | TrxHeaderPrevBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 452 | TrxHeaderPrevBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 453 | TrxHeaderPrevBillingDate | BILLING_DATE | — | — |
| 454 | TrxHeaderPrevBrAmount | BR_AMOUNT | — | — |
| 455 | TrxHeaderPrevBrOnHoldFlag | BR_ON_HOLD_FLAG | — | — |
| 456 | TrxHeaderPrevBrUnpaidFlag | BR_UNPAID_FLAG | — | — |
| 457 | TrxHeaderPrevCcErrorCode | CC_ERROR_CODE | — | — |
| 458 | TrxHeaderPrevCcErrorFlag | CC_ERROR_FLAG | — | — |
| 459 | TrxHeaderPrevCcErrorText | CC_ERROR_TEXT | — | — |
| 460 | TrxHeaderPrevComments | COMMENTS | — | — |
| 461 | TrxHeaderPrevCompleteFlag | COMPLETE_FLAG | — | — |
| 462 | TrxHeaderPrevContractId | CONTRACT_ID | — | — |
| 463 | TrxHeaderPrevCreatedBy | CREATED_BY | — | — |
| 464 | TrxHeaderPrevCreatedFrom | CREATED_FROM | — | — |
| 465 | TrxHeaderPrevCreationDate | CREATION_DATE | — | — |
| 466 | TrxHeaderPrevCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | — |
| 467 | TrxHeaderPrevCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | — |
| 468 | TrxHeaderPrevCtReference | CT_REFERENCE | — | — |
| 469 | TrxHeaderPrevCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 470 | TrxHeaderPrevCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 471 | TrxHeaderPrevCustomerReference | CUSTOMER_REFERENCE | — | — |
| 472 | TrxHeaderPrevCustomerReferenceDate | CUSTOMER_REFERENCE_DATE | — | — |
| 473 | TrxHeaderPrevCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 474 | TrxHeaderPrevDefaultTaxExemptFlag | DEFAULT_TAX_EXEMPT_FLAG | — | — |
| 475 | TrxHeaderPrevDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 476 | TrxHeaderPrevDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 477 | TrxHeaderPrevDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 478 | TrxHeaderPrevDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 479 | TrxHeaderPrevDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 480 | TrxHeaderPrevDocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 481 | TrxHeaderPrevDraweeBankAccountId | DRAWEE_BANK_ACCOUNT_ID | — | — |
| 482 | TrxHeaderPrevDraweeContactId | DRAWEE_CONTACT_ID | — | — |
| 483 | TrxHeaderPrevDraweeId | DRAWEE_ID | — | — |
| 484 | TrxHeaderPrevDraweeSiteUseId | DRAWEE_SITE_USE_ID | — | — |
| 485 | TrxHeaderPrevEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 486 | TrxHeaderPrevEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 487 | TrxHeaderPrevEndDateCommitment | END_DATE_COMMITMENT | — | — |
| 488 | TrxHeaderPrevExchangeDate | EXCHANGE_DATE | — | — |
| 489 | TrxHeaderPrevExchangeRate | EXCHANGE_RATE | — | — |
| 490 | TrxHeaderPrevExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 491 | TrxHeaderPrevFinanceCharges | FINANCE_CHARGES | — | — |
| 492 | TrxHeaderPrevFobPoint | FOB_POINT | — | — |
| 493 | TrxHeaderPrevInitialCustomerTrxId | INITIAL_CUSTOMER_TRX_ID | — | — |
| 494 | TrxHeaderPrevIntercompanyFlag | INTERCOMPANY_FLAG | — | — |
| 495 | TrxHeaderPrevInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 496 | TrxHeaderPrevInterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | — |
| 497 | TrxHeaderPrevInterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | — |
| 498 | TrxHeaderPrevInterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | — |
| 499 | TrxHeaderPrevInterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | — |
| 500 | TrxHeaderPrevInterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | — |
| 501 | TrxHeaderPrevInterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | — |
| 502 | TrxHeaderPrevInterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | — |
| 503 | TrxHeaderPrevInterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | — |
| 504 | TrxHeaderPrevInterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | — |
| 505 | TrxHeaderPrevInterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | — |
| 506 | TrxHeaderPrevInterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | — |
| 507 | TrxHeaderPrevInterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | — |
| 508 | TrxHeaderPrevInterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | — |
| 509 | TrxHeaderPrevInterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | — |
| 510 | TrxHeaderPrevInterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | — |
| 511 | TrxHeaderPrevInterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | — |
| 512 | TrxHeaderPrevInternalNotes | INTERNAL_NOTES | — | — |
| 513 | TrxHeaderPrevInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 514 | TrxHeaderPrevInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 515 | TrxHeaderPrevLastPrintedSequenceNum | LAST_PRINTED_SEQUENCE_NUM | — | — |
| 516 | TrxHeaderPrevLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 517 | TrxHeaderPrevLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 518 | TrxHeaderPrevLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 519 | TrxHeaderPrevLateChargesAssessed | LATE_CHARGES_ASSESSED | — | — |
| 520 | TrxHeaderPrevLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 521 | TrxHeaderPrevObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 522 | TrxHeaderPrevOldTrxNumber | OLD_TRX_NUMBER | — | — |
| 523 | TrxHeaderPrevOrgId | ORG_ID | — | — |
| 524 | TrxHeaderPrevOrigSystemBatchName | ORIG_SYSTEM_BATCH_NAME | — | — |
| 525 | TrxHeaderPrevOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 526 | TrxHeaderPrevPayingCustomerId | PAYING_CUSTOMER_ID | — | — |
| 527 | TrxHeaderPrevPayingSiteUseId | PAYING_SITE_USE_ID | — | — |
| 528 | TrxHeaderPrevPaymentAttributes | PAYMENT_ATTRIBUTES | — | — |
| 529 | TrxHeaderPrevPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 530 | TrxHeaderPrevPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 531 | TrxHeaderPrevPostRequestId | POST_REQUEST_ID | — | — |
| 532 | TrxHeaderPrevPostingControlId | POSTING_CONTROL_ID | — | — |
| 533 | TrxHeaderPrevPrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 534 | TrxHeaderPrevPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 535 | TrxHeaderPrevPrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | — |
| 536 | TrxHeaderPrevPrintingCount | PRINTING_COUNT | — | — |
| 537 | TrxHeaderPrevPrintingLastPrinted | PRINTING_LAST_PRINTED | — | — |
| 538 | TrxHeaderPrevPrintingOption | PRINTING_OPTION | — | — |
| 539 | TrxHeaderPrevPrintingOriginalDate | PRINTING_ORIGINAL_DATE | — | — |
| 540 | TrxHeaderPrevPrintingPending | PRINTING_PENDING | — | — |
| 541 | TrxHeaderPrevProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 542 | TrxHeaderPrevProgramId | PROGRAM_ID | — | — |
| 543 | TrxHeaderPrevProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 544 | TrxHeaderPrevPurchaseOrder | PURCHASE_ORDER | — | — |
| 545 | TrxHeaderPrevPurchaseOrderDate | PURCHASE_ORDER_DATE | — | — |
| 546 | TrxHeaderPrevPurchaseOrderRevision | PURCHASE_ORDER_REVISION | — | — |
| 547 | TrxHeaderPrevRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 548 | TrxHeaderPrevReasonCode | REASON_CODE | — | — |
| 549 | TrxHeaderPrevReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 550 | TrxHeaderPrevRecurredFromTrxNumber | RECURRED_FROM_TRX_NUMBER | — | — |
| 551 | TrxHeaderPrevRelatedBatchSourceSeqId | RELATED_BATCH_SOURCE_SEQ_ID | — | — |
| 552 | TrxHeaderPrevRelatedCustomerTrxId | RELATED_CUSTOMER_TRX_ID | — | — |
| 553 | TrxHeaderPrevRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 554 | TrxHeaderPrevRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 555 | TrxHeaderPrevRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 556 | TrxHeaderPrevRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 557 | TrxHeaderPrevRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 558 | TrxHeaderPrevRequestId | REQUEST_ID | — | — |
| 559 | TrxHeaderPrevRequiresManualScheduling | REQUIRES_MANUAL_SCHEDULING | — | — |
| 560 | TrxHeaderPrevReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 561 | TrxHeaderPrevSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 562 | TrxHeaderPrevShipDateActual | SHIP_DATE_ACTUAL | — | — |
| 563 | TrxHeaderPrevShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 564 | TrxHeaderPrevShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 565 | TrxHeaderPrevShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 566 | TrxHeaderPrevShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 567 | TrxHeaderPrevShipVia | SHIP_VIA | — | — |
| 568 | TrxHeaderPrevShipmentId | SHIPMENT_ID | — | — |
| 569 | TrxHeaderPrevSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 570 | TrxHeaderPrevSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 571 | TrxHeaderPrevSoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | — |
| 572 | TrxHeaderPrevSourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 573 | TrxHeaderPrevSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 574 | TrxHeaderPrevSpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 575 | TrxHeaderPrevStartDateCommitment | START_DATE_COMMITMENT | — | — |
| 576 | TrxHeaderPrevStatusTrx | STATUS_TRX | — | — |
| 577 | TrxHeaderPrevTermDueDate | TERM_DUE_DATE | — | — |
| 578 | TrxHeaderPrevTermId | TERM_ID | — | — |
| 579 | TrxHeaderPrevTerritoryId | TERRITORY_ID | — | — |
| 580 | TrxHeaderPrevTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 581 | TrxHeaderPrevTrxClass | TRX_CLASS | — | — |
| 582 | TrxHeaderPrevTrxDate | TRX_DATE | — | — |
| 583 | TrxHeaderPrevTrxNumber | TRX_NUMBER | — | — |
| 584 | TrxHeaderPrevUpgradeMethod | UPGRADE_METHOD | — | — |
| 585 | TrxHeaderPrevUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 586 | TrxHeaderPrevWaybillNumber | WAYBILL_NUMBER | — | — |
| 587 | TrxHeaderPrevWhUpdateDate | WH_UPDATE_DATE | — | — |

### [[ra_customer_trx_lines_all|RA_CUSTOMER_TRX_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustomerTrxLineId | CUSTOMER_TRX_LINE_ID | 🔑 | ✅ |
| 2 | TransactionLineAccountingRuleDuration | ACCOUNTING_RULE_DURATION | — | ✅ |
| 3 | TransactionLineAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 4 | TransactionLineAcctdAmountDueOriginal | ACCTD_AMOUNT_DUE_ORIGINAL | — | — |
| 5 | TransactionLineAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | — |
| 6 | TransactionLineAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 7 | TransactionLineAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 8 | TransactionLineAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | ✅ |
| 9 | TransactionLineAssessableValue | ASSESSABLE_VALUE | — | ✅ |
| 10 | TransactionLineAutoruleCompleteFlag | AUTORULE_COMPLETE_FLAG | — | ✅ |
| 11 | TransactionLineAutoruleDurationProcessed | AUTORULE_DURATION_PROCESSED | — | — |
| 12 | TransactionLineAutotax | AUTOTAX | — | ✅ |
| 13 | TransactionLineBrAdjustmentId | BR_ADJUSTMENT_ID | — | — |
| 14 | TransactionLineBrRefCustomerTrxId | BR_REF_CUSTOMER_TRX_ID | — | — |
| 15 | TransactionLineBrRefPaymentScheduleId | BR_REF_PAYMENT_SCHEDULE_ID | — | — |
| 16 | TransactionLineChrgAcctdAmountRemaining | CHRG_ACCTD_AMOUNT_REMAINING | — | — |
| 17 | TransactionLineChrgAmountRemaining | CHRG_AMOUNT_REMAINING | — | — |
| 18 | TransactionLineContractLineId | CONTRACT_LINE_ID | — | — |
| 19 | TransactionLineCreatedBy | CREATED_BY | — | — |
| 20 | TransactionLineCreationDate | CREATION_DATE | — | — |
| 21 | TransactionLineCustomerTrxId | CUSTOMER_TRX_ID | — | ✅ |
| 22 | TransactionLineDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 23 | TransactionLineDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 24 | TransactionLineDeferralExclusionFlag | DEFERRAL_EXCLUSION_FLAG | — | ✅ |
| 25 | TransactionLineDescription | DESCRIPTION | — | ✅ |
| 26 | TransactionLineExtendedAcctdAmount | EXTENDED_ACCTD_AMOUNT | — | ✅ |
| 27 | TransactionLineExtendedAmount1 | EXTENDED_AMOUNT | — | — |
| 28 | TransactionLineFairMarketValueAmount | FAIR_MARKET_VALUE_AMOUNT | — | — |
| 29 | TransactionLineFrtAdjAcctdRemaining | FRT_ADJ_ACCTD_REMAINING | — | — |
| 30 | TransactionLineFrtAdjRemaining | FRT_ADJ_REMAINING | — | — |
| 31 | TransactionLineFrtEdAcctdAmount | FRT_ED_ACCTD_AMOUNT | — | — |
| 32 | TransactionLineFrtEdAmount | FRT_ED_AMOUNT | — | — |
| 33 | TransactionLineFrtUnedAcctdAmount | FRT_UNED_ACCTD_AMOUNT | — | — |
| 34 | TransactionLineFrtUnedAmount | FRT_UNED_AMOUNT | — | — |
| 35 | TransactionLineGrossExtendedAmount | GROSS_EXTENDED_AMOUNT | — | ✅ |
| 36 | TransactionLineGrossUnitSellingPrice | GROSS_UNIT_SELLING_PRICE | — | ✅ |
| 37 | TransactionLineHistoricalFlag | HISTORICAL_FLAG | — | — |
| 38 | TransactionLineInitialAccountingRuleDuration | ACCOUNTING_RULE_DURATION | — | — |
| 39 | TransactionLineInitialAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 40 | TransactionLineInitialAcctdAmountDueOriginal | ACCTD_AMOUNT_DUE_ORIGINAL | — | — |
| 41 | TransactionLineInitialAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | — |
| 42 | TransactionLineInitialAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 43 | TransactionLineInitialAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 44 | TransactionLineInitialAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 45 | TransactionLineInitialAssessableValue | ASSESSABLE_VALUE | — | — |
| 46 | TransactionLineInitialAutoruleCompleteFlag | AUTORULE_COMPLETE_FLAG | — | ✅ |
| 47 | TransactionLineInitialAutoruleDurationProcessed | AUTORULE_DURATION_PROCESSED | — | — |
| 48 | TransactionLineInitialAutotax | AUTOTAX | — | — |
| 49 | TransactionLineInitialBrAdjustmentId | BR_ADJUSTMENT_ID | — | — |
| 50 | TransactionLineInitialBrRefCustomerTrxId | BR_REF_CUSTOMER_TRX_ID | — | — |
| 51 | TransactionLineInitialBrRefPaymentScheduleId | BR_REF_PAYMENT_SCHEDULE_ID | — | — |
| 52 | TransactionLineInitialChrgAcctdAmountRemaining | CHRG_ACCTD_AMOUNT_REMAINING | — | — |
| 53 | TransactionLineInitialChrgAmountRemaining | CHRG_AMOUNT_REMAINING | — | — |
| 54 | TransactionLineInitialContractLineId | CONTRACT_LINE_ID | — | — |
| 55 | TransactionLineInitialCreatedBy | CREATED_BY | — | — |
| 56 | TransactionLineInitialCreationDate | CREATION_DATE | — | — |
| 57 | TransactionLineInitialCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 58 | TransactionLineInitialCustomerTrxLineId | INITIAL_CUSTOMER_TRX_LINE_ID | — | — |
| 59 | TransactionLineInitialCustomerTrxLineId1 | CUSTOMER_TRX_LINE_ID | — | — |
| 60 | TransactionLineInitialDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 61 | TransactionLineInitialDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 62 | TransactionLineInitialDeferralExclusionFlag | DEFERRAL_EXCLUSION_FLAG | — | — |
| 63 | TransactionLineInitialDescription | DESCRIPTION | — | — |
| 64 | TransactionLineInitialExtendedAcctdAmount | EXTENDED_ACCTD_AMOUNT | — | — |
| 65 | TransactionLineInitialExtendedAmount | EXTENDED_AMOUNT | — | — |
| 66 | TransactionLineInitialFairMarketValueAmount | FAIR_MARKET_VALUE_AMOUNT | — | — |
| 67 | TransactionLineInitialFrtAdjAcctdRemaining | FRT_ADJ_ACCTD_REMAINING | — | — |
| 68 | TransactionLineInitialFrtAdjRemaining | FRT_ADJ_REMAINING | — | — |
| 69 | TransactionLineInitialFrtEdAcctdAmount | FRT_ED_ACCTD_AMOUNT | — | — |
| 70 | TransactionLineInitialFrtEdAmount | FRT_ED_AMOUNT | — | — |
| 71 | TransactionLineInitialFrtUnedAcctdAmount | FRT_UNED_ACCTD_AMOUNT | — | — |
| 72 | TransactionLineInitialFrtUnedAmount | FRT_UNED_AMOUNT | — | — |
| 73 | TransactionLineInitialGrossExtendedAmount | GROSS_EXTENDED_AMOUNT | — | ✅ |
| 74 | TransactionLineInitialGrossUnitSellingPrice | GROSS_UNIT_SELLING_PRICE | — | — |
| 75 | TransactionLineInitialHistoricalFlag | HISTORICAL_FLAG | — | — |
| 76 | TransactionLineInitialInitialCustomerTrxLineId | INITIAL_CUSTOMER_TRX_LINE_ID | — | — |
| 77 | TransactionLineInitialInterestLineId | INTEREST_LINE_ID | — | — |
| 78 | TransactionLineInitialInterfaceLineAttribute1 | INTERFACE_LINE_ATTRIBUTE1 | — | — |
| 79 | TransactionLineInitialInterfaceLineAttribute10 | INTERFACE_LINE_ATTRIBUTE10 | — | — |
| 80 | TransactionLineInitialInterfaceLineAttribute11 | INTERFACE_LINE_ATTRIBUTE11 | — | — |
| 81 | TransactionLineInitialInterfaceLineAttribute12 | INTERFACE_LINE_ATTRIBUTE12 | — | — |
| 82 | TransactionLineInitialInterfaceLineAttribute13 | INTERFACE_LINE_ATTRIBUTE13 | — | — |
| 83 | TransactionLineInitialInterfaceLineAttribute14 | INTERFACE_LINE_ATTRIBUTE14 | — | — |
| 84 | TransactionLineInitialInterfaceLineAttribute15 | INTERFACE_LINE_ATTRIBUTE15 | — | — |
| 85 | TransactionLineInitialInterfaceLineAttribute2 | INTERFACE_LINE_ATTRIBUTE2 | — | — |
| 86 | TransactionLineInitialInterfaceLineAttribute3 | INTERFACE_LINE_ATTRIBUTE3 | — | — |
| 87 | TransactionLineInitialInterfaceLineAttribute4 | INTERFACE_LINE_ATTRIBUTE4 | — | — |
| 88 | TransactionLineInitialInterfaceLineAttribute5 | INTERFACE_LINE_ATTRIBUTE5 | — | — |
| 89 | TransactionLineInitialInterfaceLineAttribute6 | INTERFACE_LINE_ATTRIBUTE6 | — | — |
| 90 | TransactionLineInitialInterfaceLineAttribute7 | INTERFACE_LINE_ATTRIBUTE7 | — | — |
| 91 | TransactionLineInitialInterfaceLineAttribute8 | INTERFACE_LINE_ATTRIBUTE8 | — | — |
| 92 | TransactionLineInitialInterfaceLineAttribute9 | INTERFACE_LINE_ATTRIBUTE9 | — | — |
| 93 | TransactionLineInitialInterfaceLineContext | INTERFACE_LINE_CONTEXT | — | — |
| 94 | TransactionLineInitialInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 95 | TransactionLineInitialInvoicedLineAcctgLevel | INVOICED_LINE_ACCTG_LEVEL | — | — |
| 96 | TransactionLineInitialItemContext | ITEM_CONTEXT | — | — |
| 97 | TransactionLineInitialItemExceptionRateId | ITEM_EXCEPTION_RATE_ID | — | — |
| 98 | TransactionLineInitialLastPeriodToCredit | LAST_PERIOD_TO_CREDIT | — | — |
| 99 | TransactionLineInitialLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 100 | TransactionLineInitialLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 101 | TransactionLineInitialLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 102 | TransactionLineInitialLineIntendedUse | LINE_INTENDED_USE | — | — |
| 103 | TransactionLineInitialLineNumber | LINE_NUMBER | — | — |
| 104 | TransactionLineInitialLineRecoverable | LINE_RECOVERABLE | — | — |
| 105 | TransactionLineInitialLineType | LINE_TYPE | — | — |
| 106 | TransactionLineInitialLinkToCustTrxLineId | LINK_TO_CUST_TRX_LINE_ID | — | — |
| 107 | TransactionLineInitialLinkToParentlineAttribute1 | LINK_TO_PARENTLINE_ATTRIBUTE1 | — | — |
| 108 | TransactionLineInitialLinkToParentlineAttribute10 | LINK_TO_PARENTLINE_ATTRIBUTE10 | — | — |
| 109 | TransactionLineInitialLinkToParentlineAttribute11 | LINK_TO_PARENTLINE_ATTRIBUTE11 | — | — |
| 110 | TransactionLineInitialLinkToParentlineAttribute12 | LINK_TO_PARENTLINE_ATTRIBUTE12 | — | — |
| 111 | TransactionLineInitialLinkToParentlineAttribute13 | LINK_TO_PARENTLINE_ATTRIBUTE13 | — | — |
| 112 | TransactionLineInitialLinkToParentlineAttribute14 | LINK_TO_PARENTLINE_ATTRIBUTE14 | — | — |
| 113 | TransactionLineInitialLinkToParentlineAttribute15 | LINK_TO_PARENTLINE_ATTRIBUTE15 | — | — |
| 114 | TransactionLineInitialLinkToParentlineAttribute2 | LINK_TO_PARENTLINE_ATTRIBUTE2 | — | — |
| 115 | TransactionLineInitialLinkToParentlineAttribute3 | LINK_TO_PARENTLINE_ATTRIBUTE3 | — | — |
| 116 | TransactionLineInitialLinkToParentlineAttribute4 | LINK_TO_PARENTLINE_ATTRIBUTE4 | — | — |
| 117 | TransactionLineInitialLinkToParentlineAttribute5 | LINK_TO_PARENTLINE_ATTRIBUTE5 | — | — |
| 118 | TransactionLineInitialLinkToParentlineAttribute6 | LINK_TO_PARENTLINE_ATTRIBUTE6 | — | — |
| 119 | TransactionLineInitialLinkToParentlineAttribute7 | LINK_TO_PARENTLINE_ATTRIBUTE7 | — | — |
| 120 | TransactionLineInitialLinkToParentlineAttribute8 | LINK_TO_PARENTLINE_ATTRIBUTE8 | — | — |
| 121 | TransactionLineInitialLinkToParentlineAttribute9 | LINK_TO_PARENTLINE_ATTRIBUTE9 | — | — |
| 122 | TransactionLineInitialLinkToParentlineContext | LINK_TO_PARENTLINE_CONTEXT | — | — |
| 123 | TransactionLineInitialLocationSegmentId | LOCATION_SEGMENT_ID | — | — |
| 124 | TransactionLineInitialMemoLineSeqId | MEMO_LINE_SEQ_ID | — | — |
| 125 | TransactionLineInitialMovementId | MOVEMENT_ID | — | — |
| 126 | TransactionLineInitialMrcExtendedAcctdAmount | MRC_EXTENDED_ACCTD_AMOUNT | — | — |
| 127 | TransactionLineInitialObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 128 | TransactionLineInitialOrgId | ORG_ID | — | — |
| 129 | TransactionLineInitialOverrideAutoAccountingFlag | OVERRIDE_AUTO_ACCOUNTING_FLAG | — | — |
| 130 | TransactionLineInitialPaymentSetId | PAYMENT_SET_ID | — | — |
| 131 | TransactionLineInitialPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 132 | TransactionLineInitialPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 133 | TransactionLineInitialPreviousCustomerTrxLineId | PREVIOUS_CUSTOMER_TRX_LINE_ID | — | — |
| 134 | TransactionLineInitialProductCategory | PRODUCT_CATEGORY | — | — |
| 135 | TransactionLineInitialProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | — |
| 136 | TransactionLineInitialProductType | PRODUCT_TYPE | — | — |
| 137 | TransactionLineInitialProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 138 | TransactionLineInitialProgramId | PROGRAM_ID | — | — |
| 139 | TransactionLineInitialProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 140 | TransactionLineInitialQuantityCredited | QUANTITY_CREDITED | — | — |
| 141 | TransactionLineInitialQuantityInvoiced | QUANTITY_INVOICED | — | — |
| 142 | TransactionLineInitialQuantityOrdered | QUANTITY_ORDERED | — | — |
| 143 | TransactionLineInitialReasonCode | REASON_CODE | — | — |
| 144 | TransactionLineInitialRequestId | REQUEST_ID | — | — |
| 145 | TransactionLineInitialRevenueAmount | REVENUE_AMOUNT | — | — |
| 146 | TransactionLineInitialRuleEndDate | RULE_END_DATE | — | — |
| 147 | TransactionLineInitialRuleStartDate | RULE_START_DATE | — | — |
| 148 | TransactionLineInitialSalesOrder | SALES_ORDER | — | — |
| 149 | TransactionLineInitialSalesOrderDate | SALES_ORDER_DATE | — | — |
| 150 | TransactionLineInitialSalesOrderLine | SALES_ORDER_LINE | — | — |
| 151 | TransactionLineInitialSalesOrderRevision | SALES_ORDER_REVISION | — | — |
| 152 | TransactionLineInitialSalesOrderSource | SALES_ORDER_SOURCE | — | — |
| 153 | TransactionLineInitialSalesTaxId | SALES_TAX_ID | — | — |
| 154 | TransactionLineInitialSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 155 | TransactionLineInitialShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 156 | TransactionLineInitialShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 157 | TransactionLineInitialShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 158 | TransactionLineInitialShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 159 | TransactionLineInitialSourceDataKey1 | SOURCE_DATA_KEY1 | — | — |
| 160 | TransactionLineInitialSourceDataKey2 | SOURCE_DATA_KEY2 | — | — |
| 161 | TransactionLineInitialSourceDataKey3 | SOURCE_DATA_KEY3 | — | — |
| 162 | TransactionLineInitialSourceDataKey4 | SOURCE_DATA_KEY4 | — | — |
| 163 | TransactionLineInitialSourceDataKey5 | SOURCE_DATA_KEY5 | — | — |
| 164 | TransactionLineInitialSourceDocumentLineId | SOURCE_DOCUMENT_LINE_ID | — | — |
| 165 | TransactionLineInitialSourceDocumentLineNumber | SOURCE_DOCUMENT_LINE_NUMBER | — | — |
| 166 | TransactionLineInitialTaxAction | TAX_ACTION | — | — |
| 167 | TransactionLineInitialTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 168 | TransactionLineInitialTaxExemptFlag | TAX_EXEMPT_FLAG | — | — |
| 169 | TransactionLineInitialTaxExemptNumber | TAX_EXEMPT_NUMBER | — | — |
| 170 | TransactionLineInitialTaxExemptReasonCode | TAX_EXEMPT_REASON_CODE | — | — |
| 171 | TransactionLineInitialTaxExemptionId | TAX_EXEMPTION_ID | — | — |
| 172 | TransactionLineInitialTaxLineId | TAX_LINE_ID | — | — |
| 173 | TransactionLineInitialTaxPrecedence | TAX_PRECEDENCE | — | — |
| 174 | TransactionLineInitialTaxRate | TAX_RATE | — | — |
| 175 | TransactionLineInitialTaxRecoverable | TAX_RECOVERABLE | — | — |
| 176 | TransactionLineInitialTaxVendorReturnCode | TAX_VENDOR_RETURN_CODE | — | — |
| 177 | TransactionLineInitialTaxableAmount | TAXABLE_AMOUNT | — | — |
| 178 | TransactionLineInitialTaxableFlag | TAXABLE_FLAG | — | — |
| 179 | TransactionLineInitialTranslatedDescription | TRANSLATED_DESCRIPTION | — | — |
| 180 | TransactionLineInitialTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 181 | TransactionLineInitialUnitSellingPrice | UNIT_SELLING_PRICE | — | — |
| 182 | TransactionLineInitialUnitStandardPrice | UNIT_STANDARD_PRICE | — | — |
| 183 | TransactionLineInitialUomCode | UOM_CODE | — | — |
| 184 | TransactionLineInitialUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 185 | TransactionLineInitialVatTaxId | VAT_TAX_ID | — | — |
| 186 | TransactionLineInitialWarehouseId | WAREHOUSE_ID | — | — |
| 187 | TransactionLineInitialWhUpdateDate | WH_UPDATE_DATE | — | — |
| 188 | TransactionLineInterestLineId | INTEREST_LINE_ID | — | — |
| 189 | TransactionLineInterfaceLineAttribute1 | INTERFACE_LINE_ATTRIBUTE1 | — | ✅ |
| 190 | TransactionLineInterfaceLineAttribute10 | INTERFACE_LINE_ATTRIBUTE10 | — | ✅ |
| 191 | TransactionLineInterfaceLineAttribute11 | INTERFACE_LINE_ATTRIBUTE11 | — | ✅ |
| 192 | TransactionLineInterfaceLineAttribute12 | INTERFACE_LINE_ATTRIBUTE12 | — | ✅ |
| 193 | TransactionLineInterfaceLineAttribute13 | INTERFACE_LINE_ATTRIBUTE13 | — | ✅ |
| 194 | TransactionLineInterfaceLineAttribute14 | INTERFACE_LINE_ATTRIBUTE14 | — | ✅ |
| 195 | TransactionLineInterfaceLineAttribute15 | INTERFACE_LINE_ATTRIBUTE15 | — | ✅ |
| 196 | TransactionLineInterfaceLineAttribute2 | INTERFACE_LINE_ATTRIBUTE2 | — | ✅ |
| 197 | TransactionLineInterfaceLineAttribute3 | INTERFACE_LINE_ATTRIBUTE3 | — | ✅ |
| 198 | TransactionLineInterfaceLineAttribute4 | INTERFACE_LINE_ATTRIBUTE4 | — | ✅ |
| 199 | TransactionLineInterfaceLineAttribute5 | INTERFACE_LINE_ATTRIBUTE5 | — | ✅ |
| 200 | TransactionLineInterfaceLineAttribute6 | INTERFACE_LINE_ATTRIBUTE6 | — | ✅ |
| 201 | TransactionLineInterfaceLineAttribute7 | INTERFACE_LINE_ATTRIBUTE7 | — | ✅ |
| 202 | TransactionLineInterfaceLineAttribute8 | INTERFACE_LINE_ATTRIBUTE8 | — | ✅ |
| 203 | TransactionLineInterfaceLineAttribute9 | INTERFACE_LINE_ATTRIBUTE9 | — | ✅ |
| 204 | TransactionLineInterfaceLineContext | INTERFACE_LINE_CONTEXT | — | ✅ |
| 205 | TransactionLineInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 206 | TransactionLineInvoicedLineAcctgLevel | INVOICED_LINE_ACCTG_LEVEL | — | — |
| 207 | TransactionLineItemContext | ITEM_CONTEXT | — | ✅ |
| 208 | TransactionLineItemExceptionRateId | ITEM_EXCEPTION_RATE_ID | — | — |
| 209 | TransactionLineLastPeriodToCredit | LAST_PERIOD_TO_CREDIT | — | — |
| 210 | TransactionLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 211 | TransactionLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 212 | TransactionLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 213 | TransactionLineLineIntendedUse | LINE_INTENDED_USE | — | ✅ |
| 214 | TransactionLineLineNumber | LINE_NUMBER | — | ✅ |
| 215 | TransactionLineLineRecoverable | LINE_RECOVERABLE | — | ✅ |
| 216 | TransactionLineLineType | LINE_TYPE | — | ✅ |
| 217 | TransactionLineLinkAccountingRuleDuration | ACCOUNTING_RULE_DURATION | — | — |
| 218 | TransactionLineLinkAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 219 | TransactionLineLinkAcctdAmountDueOriginal | ACCTD_AMOUNT_DUE_ORIGINAL | — | — |
| 220 | TransactionLineLinkAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | — |
| 221 | TransactionLineLinkAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 222 | TransactionLineLinkAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 223 | TransactionLineLinkAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 224 | TransactionLineLinkAssessableValue | ASSESSABLE_VALUE | — | — |
| 225 | TransactionLineLinkAutoruleCompleteFlag | AUTORULE_COMPLETE_FLAG | — | — |
| 226 | TransactionLineLinkAutoruleDurationProcessed | AUTORULE_DURATION_PROCESSED | — | — |
| 227 | TransactionLineLinkAutotax | AUTOTAX | — | — |
| 228 | TransactionLineLinkBrAdjustmentId | BR_ADJUSTMENT_ID | — | — |
| 229 | TransactionLineLinkBrRefCustomerTrxId | BR_REF_CUSTOMER_TRX_ID | — | — |
| 230 | TransactionLineLinkBrRefPaymentScheduleId | BR_REF_PAYMENT_SCHEDULE_ID | — | — |
| 231 | TransactionLineLinkChrgAcctdAmountRemaining | CHRG_ACCTD_AMOUNT_REMAINING | — | — |
| 232 | TransactionLineLinkChrgAmountRemaining | CHRG_AMOUNT_REMAINING | — | — |
| 233 | TransactionLineLinkContractLineId | CONTRACT_LINE_ID | — | — |
| 234 | TransactionLineLinkCreatedBy | CREATED_BY | — | — |
| 235 | TransactionLineLinkCreationDate | CREATION_DATE | — | — |
| 236 | TransactionLineLinkCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 237 | TransactionLineLinkCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 238 | TransactionLineLinkDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 239 | TransactionLineLinkDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 240 | TransactionLineLinkDeferralExclusionFlag | DEFERRAL_EXCLUSION_FLAG | — | — |
| 241 | TransactionLineLinkDescription | DESCRIPTION | — | — |
| 242 | TransactionLineLinkExtendedAcctdAmount | EXTENDED_ACCTD_AMOUNT | — | — |
| 243 | TransactionLineLinkExtendedAmount | EXTENDED_AMOUNT | — | — |
| 244 | TransactionLineLinkFairMarketValueAmount | FAIR_MARKET_VALUE_AMOUNT | — | — |
| 245 | TransactionLineLinkFrtAdjAcctdRemaining | FRT_ADJ_ACCTD_REMAINING | — | — |
| 246 | TransactionLineLinkFrtAdjRemaining | FRT_ADJ_REMAINING | — | — |
| 247 | TransactionLineLinkFrtEdAcctdAmount | FRT_ED_ACCTD_AMOUNT | — | — |
| 248 | TransactionLineLinkFrtEdAmount | FRT_ED_AMOUNT | — | — |
| 249 | TransactionLineLinkFrtUnedAcctdAmount | FRT_UNED_ACCTD_AMOUNT | — | — |
| 250 | TransactionLineLinkFrtUnedAmount | FRT_UNED_AMOUNT | — | — |
| 251 | TransactionLineLinkGrossExtendedAmount | GROSS_EXTENDED_AMOUNT | — | — |
| 252 | TransactionLineLinkGrossUnitSellingPrice | GROSS_UNIT_SELLING_PRICE | — | — |
| 253 | TransactionLineLinkHistoricalFlag | HISTORICAL_FLAG | — | — |
| 254 | TransactionLineLinkInitialCustomerTrxLineId | INITIAL_CUSTOMER_TRX_LINE_ID | — | — |
| 255 | TransactionLineLinkInterestLineId | INTEREST_LINE_ID | — | — |
| 256 | TransactionLineLinkInterfaceLineAttribute1 | INTERFACE_LINE_ATTRIBUTE1 | — | — |
| 257 | TransactionLineLinkInterfaceLineAttribute10 | INTERFACE_LINE_ATTRIBUTE10 | — | — |
| 258 | TransactionLineLinkInterfaceLineAttribute11 | INTERFACE_LINE_ATTRIBUTE11 | — | — |
| 259 | TransactionLineLinkInterfaceLineAttribute12 | INTERFACE_LINE_ATTRIBUTE12 | — | — |
| 260 | TransactionLineLinkInterfaceLineAttribute13 | INTERFACE_LINE_ATTRIBUTE13 | — | — |
| 261 | TransactionLineLinkInterfaceLineAttribute14 | INTERFACE_LINE_ATTRIBUTE14 | — | — |
| 262 | TransactionLineLinkInterfaceLineAttribute15 | INTERFACE_LINE_ATTRIBUTE15 | — | — |
| 263 | TransactionLineLinkInterfaceLineAttribute2 | INTERFACE_LINE_ATTRIBUTE2 | — | — |
| 264 | TransactionLineLinkInterfaceLineAttribute3 | INTERFACE_LINE_ATTRIBUTE3 | — | — |
| 265 | TransactionLineLinkInterfaceLineAttribute4 | INTERFACE_LINE_ATTRIBUTE4 | — | — |
| 266 | TransactionLineLinkInterfaceLineAttribute5 | INTERFACE_LINE_ATTRIBUTE5 | — | — |
| 267 | TransactionLineLinkInterfaceLineAttribute6 | INTERFACE_LINE_ATTRIBUTE6 | — | — |
| 268 | TransactionLineLinkInterfaceLineAttribute7 | INTERFACE_LINE_ATTRIBUTE7 | — | — |
| 269 | TransactionLineLinkInterfaceLineAttribute8 | INTERFACE_LINE_ATTRIBUTE8 | — | — |
| 270 | TransactionLineLinkInterfaceLineAttribute9 | INTERFACE_LINE_ATTRIBUTE9 | — | — |
| 271 | TransactionLineLinkInterfaceLineContext | INTERFACE_LINE_CONTEXT | — | — |
| 272 | TransactionLineLinkInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 273 | TransactionLineLinkInvoicedLineAcctgLevel | INVOICED_LINE_ACCTG_LEVEL | — | — |
| 274 | TransactionLineLinkItemContext | ITEM_CONTEXT | — | — |
| 275 | TransactionLineLinkItemExceptionRateId | ITEM_EXCEPTION_RATE_ID | — | — |
| 276 | TransactionLineLinkLastPeriodToCredit | LAST_PERIOD_TO_CREDIT | — | — |
| 277 | TransactionLineLinkLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 278 | TransactionLineLinkLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 279 | TransactionLineLinkLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 280 | TransactionLineLinkLineIntendedUse | LINE_INTENDED_USE | — | — |
| 281 | TransactionLineLinkLineNumber | LINE_NUMBER | — | ✅ |
| 282 | TransactionLineLinkLineRecoverable | LINE_RECOVERABLE | — | — |
| 283 | TransactionLineLinkLineType | LINE_TYPE | — | — |
| 284 | TransactionLineLinkLinkToCustTrxLineId | LINK_TO_CUST_TRX_LINE_ID | — | — |
| 285 | TransactionLineLinkLinkToParentlineAttribute1 | LINK_TO_PARENTLINE_ATTRIBUTE1 | — | — |
| 286 | TransactionLineLinkLinkToParentlineAttribute10 | LINK_TO_PARENTLINE_ATTRIBUTE10 | — | — |
| 287 | TransactionLineLinkLinkToParentlineAttribute11 | LINK_TO_PARENTLINE_ATTRIBUTE11 | — | — |
| 288 | TransactionLineLinkLinkToParentlineAttribute12 | LINK_TO_PARENTLINE_ATTRIBUTE12 | — | — |
| 289 | TransactionLineLinkLinkToParentlineAttribute13 | LINK_TO_PARENTLINE_ATTRIBUTE13 | — | — |
| 290 | TransactionLineLinkLinkToParentlineAttribute14 | LINK_TO_PARENTLINE_ATTRIBUTE14 | — | — |
| 291 | TransactionLineLinkLinkToParentlineAttribute15 | LINK_TO_PARENTLINE_ATTRIBUTE15 | — | — |
| 292 | TransactionLineLinkLinkToParentlineAttribute2 | LINK_TO_PARENTLINE_ATTRIBUTE2 | — | — |
| 293 | TransactionLineLinkLinkToParentlineAttribute3 | LINK_TO_PARENTLINE_ATTRIBUTE3 | — | — |
| 294 | TransactionLineLinkLinkToParentlineAttribute4 | LINK_TO_PARENTLINE_ATTRIBUTE4 | — | — |
| 295 | TransactionLineLinkLinkToParentlineAttribute5 | LINK_TO_PARENTLINE_ATTRIBUTE5 | — | — |
| 296 | TransactionLineLinkLinkToParentlineAttribute6 | LINK_TO_PARENTLINE_ATTRIBUTE6 | — | — |
| 297 | TransactionLineLinkLinkToParentlineAttribute7 | LINK_TO_PARENTLINE_ATTRIBUTE7 | — | — |
| 298 | TransactionLineLinkLinkToParentlineAttribute8 | LINK_TO_PARENTLINE_ATTRIBUTE8 | — | — |
| 299 | TransactionLineLinkLinkToParentlineAttribute9 | LINK_TO_PARENTLINE_ATTRIBUTE9 | — | — |
| 300 | TransactionLineLinkLinkToParentlineContext | LINK_TO_PARENTLINE_CONTEXT | — | — |
| 301 | TransactionLineLinkLocationSegmentId | LOCATION_SEGMENT_ID | — | — |
| 302 | TransactionLineLinkMemoLineSeqId | MEMO_LINE_SEQ_ID | — | — |
| 303 | TransactionLineLinkMovementId | MOVEMENT_ID | — | — |
| 304 | TransactionLineLinkMrcExtendedAcctdAmount | MRC_EXTENDED_ACCTD_AMOUNT | — | — |
| 305 | TransactionLineLinkObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 306 | TransactionLineLinkOrgId | ORG_ID | — | — |
| 307 | TransactionLineLinkOverrideAutoAccountingFlag | OVERRIDE_AUTO_ACCOUNTING_FLAG | — | — |
| 308 | TransactionLineLinkPaymentSetId | PAYMENT_SET_ID | — | — |
| 309 | TransactionLineLinkPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 310 | TransactionLineLinkPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 311 | TransactionLineLinkPreviousCustomerTrxLineId | PREVIOUS_CUSTOMER_TRX_LINE_ID | — | — |
| 312 | TransactionLineLinkProductCategory | PRODUCT_CATEGORY | — | — |
| 313 | TransactionLineLinkProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | — |
| 314 | TransactionLineLinkProductType | PRODUCT_TYPE | — | — |
| 315 | TransactionLineLinkProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 316 | TransactionLineLinkProgramId | PROGRAM_ID | — | — |
| 317 | TransactionLineLinkProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 318 | TransactionLineLinkQuantityCredited | QUANTITY_CREDITED | — | — |
| 319 | TransactionLineLinkQuantityInvoiced | QUANTITY_INVOICED | — | — |
| 320 | TransactionLineLinkQuantityOrdered | QUANTITY_ORDERED | — | — |
| 321 | TransactionLineLinkReasonCode | REASON_CODE | — | — |
| 322 | TransactionLineLinkRequestId | REQUEST_ID | — | — |
| 323 | TransactionLineLinkRevenueAmount | REVENUE_AMOUNT | — | — |
| 324 | TransactionLineLinkRuleEndDate | RULE_END_DATE | — | — |
| 325 | TransactionLineLinkRuleStartDate | RULE_START_DATE | — | — |
| 326 | TransactionLineLinkSalesOrder | SALES_ORDER | — | — |
| 327 | TransactionLineLinkSalesOrderDate | SALES_ORDER_DATE | — | — |
| 328 | TransactionLineLinkSalesOrderLine | SALES_ORDER_LINE | — | — |
| 329 | TransactionLineLinkSalesOrderRevision | SALES_ORDER_REVISION | — | — |
| 330 | TransactionLineLinkSalesOrderSource | SALES_ORDER_SOURCE | — | — |
| 331 | TransactionLineLinkSalesTaxId | SALES_TAX_ID | — | — |
| 332 | TransactionLineLinkSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 333 | TransactionLineLinkShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 334 | TransactionLineLinkShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 335 | TransactionLineLinkShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 336 | TransactionLineLinkShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 337 | TransactionLineLinkSourceDataKey1 | SOURCE_DATA_KEY1 | — | — |
| 338 | TransactionLineLinkSourceDataKey2 | SOURCE_DATA_KEY2 | — | — |
| 339 | TransactionLineLinkSourceDataKey3 | SOURCE_DATA_KEY3 | — | — |
| 340 | TransactionLineLinkSourceDataKey4 | SOURCE_DATA_KEY4 | — | — |
| 341 | TransactionLineLinkSourceDataKey5 | SOURCE_DATA_KEY5 | — | — |
| 342 | TransactionLineLinkSourceDocumentLineId | SOURCE_DOCUMENT_LINE_ID | — | — |
| 343 | TransactionLineLinkSourceDocumentLineNumber | SOURCE_DOCUMENT_LINE_NUMBER | — | — |
| 344 | TransactionLineLinkTaxAction | TAX_ACTION | — | — |
| 345 | TransactionLineLinkTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 346 | TransactionLineLinkTaxExemptFlag | TAX_EXEMPT_FLAG | — | — |
| 347 | TransactionLineLinkTaxExemptNumber | TAX_EXEMPT_NUMBER | — | — |
| 348 | TransactionLineLinkTaxExemptReasonCode | TAX_EXEMPT_REASON_CODE | — | — |
| 349 | TransactionLineLinkTaxExemptionId | TAX_EXEMPTION_ID | — | — |
| 350 | TransactionLineLinkTaxLineId | TAX_LINE_ID | — | — |
| 351 | TransactionLineLinkTaxPrecedence | TAX_PRECEDENCE | — | — |
| 352 | TransactionLineLinkTaxRate | TAX_RATE | — | — |
| 353 | TransactionLineLinkTaxRecoverable | TAX_RECOVERABLE | — | — |
| 354 | TransactionLineLinkTaxVendorReturnCode | TAX_VENDOR_RETURN_CODE | — | — |
| 355 | TransactionLineLinkTaxableAmount | TAXABLE_AMOUNT | — | — |
| 356 | TransactionLineLinkTaxableFlag | TAXABLE_FLAG | — | — |
| 357 | TransactionLineLinkToCustTrxLineId | LINK_TO_CUST_TRX_LINE_ID | — | ✅ |
| 358 | TransactionLineLinkToParentlineAttribute1 | LINK_TO_PARENTLINE_ATTRIBUTE1 | — | — |
| 359 | TransactionLineLinkToParentlineAttribute10 | LINK_TO_PARENTLINE_ATTRIBUTE10 | — | — |
| 360 | TransactionLineLinkToParentlineAttribute11 | LINK_TO_PARENTLINE_ATTRIBUTE11 | — | — |
| 361 | TransactionLineLinkToParentlineAttribute12 | LINK_TO_PARENTLINE_ATTRIBUTE12 | — | — |
| 362 | TransactionLineLinkToParentlineAttribute13 | LINK_TO_PARENTLINE_ATTRIBUTE13 | — | — |
| 363 | TransactionLineLinkToParentlineAttribute14 | LINK_TO_PARENTLINE_ATTRIBUTE14 | — | — |
| 364 | TransactionLineLinkToParentlineAttribute15 | LINK_TO_PARENTLINE_ATTRIBUTE15 | — | — |
| 365 | TransactionLineLinkToParentlineAttribute2 | LINK_TO_PARENTLINE_ATTRIBUTE2 | — | — |
| 366 | TransactionLineLinkToParentlineAttribute3 | LINK_TO_PARENTLINE_ATTRIBUTE3 | — | — |
| 367 | TransactionLineLinkToParentlineAttribute4 | LINK_TO_PARENTLINE_ATTRIBUTE4 | — | — |
| 368 | TransactionLineLinkToParentlineAttribute5 | LINK_TO_PARENTLINE_ATTRIBUTE5 | — | — |
| 369 | TransactionLineLinkToParentlineAttribute6 | LINK_TO_PARENTLINE_ATTRIBUTE6 | — | — |
| 370 | TransactionLineLinkToParentlineAttribute7 | LINK_TO_PARENTLINE_ATTRIBUTE7 | — | — |
| 371 | TransactionLineLinkToParentlineAttribute8 | LINK_TO_PARENTLINE_ATTRIBUTE8 | — | — |
| 372 | TransactionLineLinkToParentlineAttribute9 | LINK_TO_PARENTLINE_ATTRIBUTE9 | — | — |
| 373 | TransactionLineLinkToParentlineContext | LINK_TO_PARENTLINE_CONTEXT | — | — |
| 374 | TransactionLineLinkTranslatedDescription | TRANSLATED_DESCRIPTION | — | — |
| 375 | TransactionLineLinkTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 376 | TransactionLineLinkUnitSellingPrice | UNIT_SELLING_PRICE | — | — |
| 377 | TransactionLineLinkUnitStandardPrice | UNIT_STANDARD_PRICE | — | — |
| 378 | TransactionLineLinkUomCode | UOM_CODE | — | — |
| 379 | TransactionLineLinkUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 380 | TransactionLineLinkVatTaxId | VAT_TAX_ID | — | — |
| 381 | TransactionLineLinkWarehouseId | WAREHOUSE_ID | — | — |
| 382 | TransactionLineLinkWhUpdateDate | WH_UPDATE_DATE | — | — |
| 383 | TransactionLineLocationSegmentId | LOCATION_SEGMENT_ID | — | — |
| 384 | TransactionLineMemoLineSeqId | MEMO_LINE_SEQ_ID | — | — |
| 385 | TransactionLineMovementId | MOVEMENT_ID | — | — |
| 386 | TransactionLineMrcExtendedAcctdAmount | MRC_EXTENDED_ACCTD_AMOUNT | — | — |
| 387 | TransactionLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 388 | TransactionLineOrgId | ORG_ID | — | — |
| 389 | TransactionLineOverrideAutoAccountingFlag | OVERRIDE_AUTO_ACCOUNTING_FLAG | — | — |
| 390 | TransactionLinePaymentSetId | PAYMENT_SET_ID | — | — |
| 391 | TransactionLinePaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 392 | TransactionLinePreviousAccountingRuleDuration | ACCOUNTING_RULE_DURATION | — | — |
| 393 | TransactionLinePreviousAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 394 | TransactionLinePreviousAcctdAmountDueOriginal | ACCTD_AMOUNT_DUE_ORIGINAL | — | — |
| 395 | TransactionLinePreviousAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | — |
| 396 | TransactionLinePreviousAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 397 | TransactionLinePreviousAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 398 | TransactionLinePreviousAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 399 | TransactionLinePreviousAssessableValue | ASSESSABLE_VALUE | — | — |
| 400 | TransactionLinePreviousAutoruleCompleteFlag | AUTORULE_COMPLETE_FLAG | — | — |
| 401 | TransactionLinePreviousAutoruleDurationProcessed | AUTORULE_DURATION_PROCESSED | — | — |
| 402 | TransactionLinePreviousAutotax | AUTOTAX | — | — |
| 403 | TransactionLinePreviousBrAdjustmentId | BR_ADJUSTMENT_ID | — | — |
| 404 | TransactionLinePreviousBrRefCustomerTrxId | BR_REF_CUSTOMER_TRX_ID | — | — |
| 405 | TransactionLinePreviousBrRefPaymentScheduleId | BR_REF_PAYMENT_SCHEDULE_ID | — | — |
| 406 | TransactionLinePreviousChrgAcctdAmountRemaining | CHRG_ACCTD_AMOUNT_REMAINING | — | — |
| 407 | TransactionLinePreviousChrgAmountRemaining | CHRG_AMOUNT_REMAINING | — | — |
| 408 | TransactionLinePreviousContractLineId | CONTRACT_LINE_ID | — | — |
| 409 | TransactionLinePreviousCreatedBy | CREATED_BY | — | — |
| 410 | TransactionLinePreviousCreationDate | CREATION_DATE | — | — |
| 411 | TransactionLinePreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 412 | TransactionLinePreviousCustomerTrxId1 | CUSTOMER_TRX_ID | — | — |
| 413 | TransactionLinePreviousCustomerTrxLineId | PREVIOUS_CUSTOMER_TRX_LINE_ID | — | — |
| 414 | TransactionLinePreviousCustomerTrxLineId1 | CUSTOMER_TRX_LINE_ID | — | — |
| 415 | TransactionLinePreviousDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 416 | TransactionLinePreviousDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 417 | TransactionLinePreviousDeferralExclusionFlag | DEFERRAL_EXCLUSION_FLAG | — | — |
| 418 | TransactionLinePreviousDescription | DESCRIPTION | — | — |
| 419 | TransactionLinePreviousExtendedAcctdAmount | EXTENDED_ACCTD_AMOUNT | — | — |
| 420 | TransactionLinePreviousExtendedAmount | EXTENDED_AMOUNT | — | — |
| 421 | TransactionLinePreviousFairMarketValueAmount | FAIR_MARKET_VALUE_AMOUNT | — | — |
| 422 | TransactionLinePreviousFrtAdjAcctdRemaining | FRT_ADJ_ACCTD_REMAINING | — | — |
| 423 | TransactionLinePreviousFrtAdjRemaining | FRT_ADJ_REMAINING | — | — |
| 424 | TransactionLinePreviousFrtEdAcctdAmount | FRT_ED_ACCTD_AMOUNT | — | — |
| 425 | TransactionLinePreviousFrtEdAmount | FRT_ED_AMOUNT | — | — |
| 426 | TransactionLinePreviousFrtUnedAcctdAmount | FRT_UNED_ACCTD_AMOUNT | — | — |
| 427 | TransactionLinePreviousFrtUnedAmount | FRT_UNED_AMOUNT | — | — |
| 428 | TransactionLinePreviousGrossExtendedAmount | GROSS_EXTENDED_AMOUNT | — | — |
| 429 | TransactionLinePreviousGrossUnitSellingPrice | GROSS_UNIT_SELLING_PRICE | — | — |
| 430 | TransactionLinePreviousHistoricalFlag | HISTORICAL_FLAG | — | — |
| 431 | TransactionLinePreviousInitialCustomerTrxLineId | INITIAL_CUSTOMER_TRX_LINE_ID | — | — |
| 432 | TransactionLinePreviousInterestLineId | INTEREST_LINE_ID | — | — |
| 433 | TransactionLinePreviousInterfaceLineAttribute1 | INTERFACE_LINE_ATTRIBUTE1 | — | — |
| 434 | TransactionLinePreviousInterfaceLineAttribute10 | INTERFACE_LINE_ATTRIBUTE10 | — | — |
| 435 | TransactionLinePreviousInterfaceLineAttribute11 | INTERFACE_LINE_ATTRIBUTE11 | — | — |
| 436 | TransactionLinePreviousInterfaceLineAttribute12 | INTERFACE_LINE_ATTRIBUTE12 | — | — |
| 437 | TransactionLinePreviousInterfaceLineAttribute13 | INTERFACE_LINE_ATTRIBUTE13 | — | — |
| 438 | TransactionLinePreviousInterfaceLineAttribute14 | INTERFACE_LINE_ATTRIBUTE14 | — | — |
| 439 | TransactionLinePreviousInterfaceLineAttribute15 | INTERFACE_LINE_ATTRIBUTE15 | — | — |
| 440 | TransactionLinePreviousInterfaceLineAttribute2 | INTERFACE_LINE_ATTRIBUTE2 | — | — |
| 441 | TransactionLinePreviousInterfaceLineAttribute3 | INTERFACE_LINE_ATTRIBUTE3 | — | — |
| 442 | TransactionLinePreviousInterfaceLineAttribute4 | INTERFACE_LINE_ATTRIBUTE4 | — | — |
| 443 | TransactionLinePreviousInterfaceLineAttribute5 | INTERFACE_LINE_ATTRIBUTE5 | — | — |
| 444 | TransactionLinePreviousInterfaceLineAttribute6 | INTERFACE_LINE_ATTRIBUTE6 | — | — |
| 445 | TransactionLinePreviousInterfaceLineAttribute7 | INTERFACE_LINE_ATTRIBUTE7 | — | — |
| 446 | TransactionLinePreviousInterfaceLineAttribute8 | INTERFACE_LINE_ATTRIBUTE8 | — | — |
| 447 | TransactionLinePreviousInterfaceLineAttribute9 | INTERFACE_LINE_ATTRIBUTE9 | — | — |
| 448 | TransactionLinePreviousInterfaceLineContext | INTERFACE_LINE_CONTEXT | — | — |
| 449 | TransactionLinePreviousInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 450 | TransactionLinePreviousInvoicedLineAcctgLevel | INVOICED_LINE_ACCTG_LEVEL | — | — |
| 451 | TransactionLinePreviousItemContext | ITEM_CONTEXT | — | — |
| 452 | TransactionLinePreviousItemExceptionRateId | ITEM_EXCEPTION_RATE_ID | — | — |
| 453 | TransactionLinePreviousLastPeriodToCredit | LAST_PERIOD_TO_CREDIT | — | — |
| 454 | TransactionLinePreviousLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 455 | TransactionLinePreviousLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 456 | TransactionLinePreviousLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 457 | TransactionLinePreviousLineIntendedUse | LINE_INTENDED_USE | — | — |
| 458 | TransactionLinePreviousLineNumber | LINE_NUMBER | — | ✅ |
| 459 | TransactionLinePreviousLineRecoverable | LINE_RECOVERABLE | — | — |
| 460 | TransactionLinePreviousLineType | LINE_TYPE | — | — |
| 461 | TransactionLinePreviousLinkToCustTrxLineId | LINK_TO_CUST_TRX_LINE_ID | — | — |
| 462 | TransactionLinePreviousLinkToParentlineAttribute1 | LINK_TO_PARENTLINE_ATTRIBUTE1 | — | — |
| 463 | TransactionLinePreviousLinkToParentlineAttribute10 | LINK_TO_PARENTLINE_ATTRIBUTE10 | — | — |
| 464 | TransactionLinePreviousLinkToParentlineAttribute11 | LINK_TO_PARENTLINE_ATTRIBUTE11 | — | — |
| 465 | TransactionLinePreviousLinkToParentlineAttribute12 | LINK_TO_PARENTLINE_ATTRIBUTE12 | — | — |
| 466 | TransactionLinePreviousLinkToParentlineAttribute13 | LINK_TO_PARENTLINE_ATTRIBUTE13 | — | — |
| 467 | TransactionLinePreviousLinkToParentlineAttribute14 | LINK_TO_PARENTLINE_ATTRIBUTE14 | — | — |
| 468 | TransactionLinePreviousLinkToParentlineAttribute15 | LINK_TO_PARENTLINE_ATTRIBUTE15 | — | — |
| 469 | TransactionLinePreviousLinkToParentlineAttribute2 | LINK_TO_PARENTLINE_ATTRIBUTE2 | — | — |
| 470 | TransactionLinePreviousLinkToParentlineAttribute3 | LINK_TO_PARENTLINE_ATTRIBUTE3 | — | — |
| 471 | TransactionLinePreviousLinkToParentlineAttribute4 | LINK_TO_PARENTLINE_ATTRIBUTE4 | — | — |
| 472 | TransactionLinePreviousLinkToParentlineAttribute5 | LINK_TO_PARENTLINE_ATTRIBUTE5 | — | — |
| 473 | TransactionLinePreviousLinkToParentlineAttribute6 | LINK_TO_PARENTLINE_ATTRIBUTE6 | — | — |
| 474 | TransactionLinePreviousLinkToParentlineAttribute7 | LINK_TO_PARENTLINE_ATTRIBUTE7 | — | — |
| 475 | TransactionLinePreviousLinkToParentlineAttribute8 | LINK_TO_PARENTLINE_ATTRIBUTE8 | — | — |
| 476 | TransactionLinePreviousLinkToParentlineAttribute9 | LINK_TO_PARENTLINE_ATTRIBUTE9 | — | — |
| 477 | TransactionLinePreviousLinkToParentlineContext | LINK_TO_PARENTLINE_CONTEXT | — | — |
| 478 | TransactionLinePreviousLocationSegmentId | LOCATION_SEGMENT_ID | — | — |
| 479 | TransactionLinePreviousMemoLineSeqId | MEMO_LINE_SEQ_ID | — | — |
| 480 | TransactionLinePreviousMovementId | MOVEMENT_ID | — | — |
| 481 | TransactionLinePreviousMrcExtendedAcctdAmount | MRC_EXTENDED_ACCTD_AMOUNT | — | — |
| 482 | TransactionLinePreviousObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 483 | TransactionLinePreviousOrgId | ORG_ID | — | — |
| 484 | TransactionLinePreviousOverrideAutoAccountingFlag | OVERRIDE_AUTO_ACCOUNTING_FLAG | — | — |
| 485 | TransactionLinePreviousPaymentSetId | PAYMENT_SET_ID | — | — |
| 486 | TransactionLinePreviousPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 487 | TransactionLinePreviousPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 488 | TransactionLinePreviousPreviousCustomerTrxLineId | PREVIOUS_CUSTOMER_TRX_LINE_ID | — | — |
| 489 | TransactionLinePreviousProductCategory | PRODUCT_CATEGORY | — | — |
| 490 | TransactionLinePreviousProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | — |
| 491 | TransactionLinePreviousProductType | PRODUCT_TYPE | — | — |
| 492 | TransactionLinePreviousProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 493 | TransactionLinePreviousProgramId | PROGRAM_ID | — | — |
| 494 | TransactionLinePreviousProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 495 | TransactionLinePreviousQuantityCredited | QUANTITY_CREDITED | — | — |
| 496 | TransactionLinePreviousQuantityInvoiced | QUANTITY_INVOICED | — | — |
| 497 | TransactionLinePreviousQuantityOrdered | QUANTITY_ORDERED | — | — |
| 498 | TransactionLinePreviousReasonCode | REASON_CODE | — | — |
| 499 | TransactionLinePreviousRequestId | REQUEST_ID | — | — |
| 500 | TransactionLinePreviousRevenueAmount | REVENUE_AMOUNT | — | — |
| 501 | TransactionLinePreviousRuleEndDate | RULE_END_DATE | — | — |
| 502 | TransactionLinePreviousRuleStartDate | RULE_START_DATE | — | — |
| 503 | TransactionLinePreviousSalesOrder | SALES_ORDER | — | — |
| 504 | TransactionLinePreviousSalesOrderDate | SALES_ORDER_DATE | — | — |
| 505 | TransactionLinePreviousSalesOrderLine | SALES_ORDER_LINE | — | — |
| 506 | TransactionLinePreviousSalesOrderRevision | SALES_ORDER_REVISION | — | — |
| 507 | TransactionLinePreviousSalesOrderSource | SALES_ORDER_SOURCE | — | — |
| 508 | TransactionLinePreviousSalesTaxId | SALES_TAX_ID | — | — |
| 509 | TransactionLinePreviousSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 510 | TransactionLinePreviousShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 511 | TransactionLinePreviousShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 512 | TransactionLinePreviousShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 513 | TransactionLinePreviousShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 514 | TransactionLinePreviousSourceDataKey1 | SOURCE_DATA_KEY1 | — | — |
| 515 | TransactionLinePreviousSourceDataKey2 | SOURCE_DATA_KEY2 | — | — |
| 516 | TransactionLinePreviousSourceDataKey3 | SOURCE_DATA_KEY3 | — | — |
| 517 | TransactionLinePreviousSourceDataKey4 | SOURCE_DATA_KEY4 | — | — |
| 518 | TransactionLinePreviousSourceDataKey5 | SOURCE_DATA_KEY5 | — | — |
| 519 | TransactionLinePreviousSourceDocumentLineId | SOURCE_DOCUMENT_LINE_ID | — | — |
| 520 | TransactionLinePreviousSourceDocumentLineNumber | SOURCE_DOCUMENT_LINE_NUMBER | — | — |
| 521 | TransactionLinePreviousTaxAction | TAX_ACTION | — | — |
| 522 | TransactionLinePreviousTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 523 | TransactionLinePreviousTaxExemptFlag | TAX_EXEMPT_FLAG | — | — |
| 524 | TransactionLinePreviousTaxExemptNumber | TAX_EXEMPT_NUMBER | — | — |
| 525 | TransactionLinePreviousTaxExemptReasonCode | TAX_EXEMPT_REASON_CODE | — | — |
| 526 | TransactionLinePreviousTaxExemptionId | TAX_EXEMPTION_ID | — | — |
| 527 | TransactionLinePreviousTaxLineId | TAX_LINE_ID | — | — |
| 528 | TransactionLinePreviousTaxPrecedence | TAX_PRECEDENCE | — | — |
| 529 | TransactionLinePreviousTaxRate | TAX_RATE | — | — |
| 530 | TransactionLinePreviousTaxRecoverable | TAX_RECOVERABLE | — | — |
| 531 | TransactionLinePreviousTaxVendorReturnCode | TAX_VENDOR_RETURN_CODE | — | — |
| 532 | TransactionLinePreviousTaxableAmount | TAXABLE_AMOUNT | — | — |
| 533 | TransactionLinePreviousTaxableFlag | TAXABLE_FLAG | — | — |
| 534 | TransactionLinePreviousTranslatedDescription | TRANSLATED_DESCRIPTION | — | — |
| 535 | TransactionLinePreviousTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 536 | TransactionLinePreviousUnitSellingPrice | UNIT_SELLING_PRICE | — | — |
| 537 | TransactionLinePreviousUnitStandardPrice | UNIT_STANDARD_PRICE | — | — |
| 538 | TransactionLinePreviousUomCode | UOM_CODE | — | — |
| 539 | TransactionLinePreviousUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 540 | TransactionLinePreviousVatTaxId | VAT_TAX_ID | — | — |
| 541 | TransactionLinePreviousWarehouseId | WAREHOUSE_ID | — | — |
| 542 | TransactionLinePreviousWhUpdateDate | WH_UPDATE_DATE | — | — |
| 543 | TransactionLineProductCategory | PRODUCT_CATEGORY | — | ✅ |
| 544 | TransactionLineProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | ✅ |
| 545 | TransactionLineProductType | PRODUCT_TYPE | — | ✅ |
| 546 | TransactionLineProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 547 | TransactionLineProgramId | PROGRAM_ID | — | — |
| 548 | TransactionLineProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 549 | TransactionLineQuantityCredited | QUANTITY_CREDITED | — | ✅ |
| 550 | TransactionLineQuantityInvoiced | QUANTITY_INVOICED | — | ✅ |
| 551 | TransactionLineQuantityOrdered | QUANTITY_ORDERED | — | ✅ |
| 552 | TransactionLineReasonCode | REASON_CODE | — | ✅ |
| 553 | TransactionLineRequestId | REQUEST_ID | — | — |
| 554 | TransactionLineRevenueAmount | REVENUE_AMOUNT | — | ✅ |
| 555 | TransactionLineRuleEndDate | RULE_END_DATE | — | ✅ |
| 556 | TransactionLineRuleStartDate | RULE_START_DATE | — | ✅ |
| 557 | TransactionLineSalesOrder | SALES_ORDER | — | ✅ |
| 558 | TransactionLineSalesOrderDate | SALES_ORDER_DATE | — | ✅ |
| 559 | TransactionLineSalesOrderLine | SALES_ORDER_LINE | — | ✅ |
| 560 | TransactionLineSalesOrderRevision | SALES_ORDER_REVISION | — | — |
| 561 | TransactionLineSalesOrderSource | SALES_ORDER_SOURCE | — | ✅ |
| 562 | TransactionLineSalesTaxId | SALES_TAX_ID | — | — |
| 563 | TransactionLineSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 564 | TransactionLineShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 565 | TransactionLineShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 566 | TransactionLineShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 567 | TransactionLineShipToPartyAddressId | SHIP_TO_PARTY_ADDRESS_ID | — | — |
| 568 | TransactionLineShipToPartyContactId | SHIP_TO_PARTY_CONTACT_ID | — | — |
| 569 | TransactionLineShipToPartyId | SHIP_TO_PARTY_ID | — | — |
| 570 | TransactionLineShipToPartySiteUseId | SHIP_TO_PARTY_SITE_USE_ID | — | — |
| 571 | TransactionLineShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 572 | TransactionLineSourceDataKey1 | SOURCE_DATA_KEY1 | — | — |
| 573 | TransactionLineSourceDataKey2 | SOURCE_DATA_KEY2 | — | — |
| 574 | TransactionLineSourceDataKey3 | SOURCE_DATA_KEY3 | — | — |
| 575 | TransactionLineSourceDataKey4 | SOURCE_DATA_KEY4 | — | — |
| 576 | TransactionLineSourceDataKey5 | SOURCE_DATA_KEY5 | — | — |
| 577 | TransactionLineSourceDocumentLineId | SOURCE_DOCUMENT_LINE_ID | — | — |
| 578 | TransactionLineSourceDocumentLineNumber | SOURCE_DOCUMENT_LINE_NUMBER | — | — |
| 579 | TransactionLineTaxAction | TAX_ACTION | — | — |
| 580 | TransactionLineTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | ✅ |
| 581 | TransactionLineTaxExemptFlag | TAX_EXEMPT_FLAG | — | ✅ |
| 582 | TransactionLineTaxExemptNumber | TAX_EXEMPT_NUMBER | — | ✅ |
| 583 | TransactionLineTaxExemptReasonCode | TAX_EXEMPT_REASON_CODE | — | ✅ |
| 584 | TransactionLineTaxExemptionId | TAX_EXEMPTION_ID | — | — |
| 585 | TransactionLineTaxLineId | TAX_LINE_ID | — | — |
| 586 | TransactionLineTaxPrecedence | TAX_PRECEDENCE | — | ✅ |
| 587 | TransactionLineTaxRate | TAX_RATE | — | ✅ |
| 588 | TransactionLineTaxRecoverable | TAX_RECOVERABLE | — | ✅ |
| 589 | TransactionLineTaxVendorReturnCode | TAX_VENDOR_RETURN_CODE | — | ✅ |
| 590 | TransactionLineTaxableAmount | TAXABLE_AMOUNT | — | ✅ |
| 591 | TransactionLineTaxableFlag | TAXABLE_FLAG | — | — |
| 592 | TransactionLineTranslatedDescription | TRANSLATED_DESCRIPTION | — | — |
| 593 | TransactionLineTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 594 | TransactionLineUnitSellingPrice1 | UNIT_SELLING_PRICE | — | — |
| 595 | TransactionLineUnitStandardPrice | UNIT_STANDARD_PRICE | — | ✅ |
| 596 | TransactionLineUomCode | UOM_CODE | — | ✅ |
| 597 | TransactionLineUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | ✅ |
| 598 | TransactionLineVatTaxId | VAT_TAX_ID | — | — |
| 599 | TransactionLineWarehouseId | WAREHOUSE_ID | — | — |
| 600 | TransactionLineWhUpdateDate | WH_UPDATE_DATE | — | — |

### [[ra_rules|RA_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvDistRuleDescription | DESCRIPTION | — | — |
| 2 | InvDistRuleName | NAME | — | ✅ |
| 3 | InvDistRuleObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | InvDistRuleRuleId | RULE_ID | — | — |

### [[zx_fc_intended_use_v|ZX_FC_INTENDED_USE_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LnIntndUseClassificationId | CLASSIFICATION_ID | — | — |
| 2 | LnIntndUseCode | CODE | — | — |
| 3 | LnIntndUseCountryCode | COUNTRY_CODE | — | — |
| 4 | LnIntndUseName | NAME | — | ✅ |

### [[zx_fc_product_categories_v|ZX_FC_PRODUCT_CATEGORIES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProdCatClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | ProdCatClassificationId | CLASSIFICATION_ID | — | — |
| 3 | ProdCatClassificationName | CLASSIFICATION_NAME | — | ✅ |
| 4 | ProdCatConcatLeafCode | CONCAT_LEAF_CODE | — | — |
| 5 | ProdCatConcatLeafName | CONCAT_LEAF_NAME | — | — |
| 6 | ProdCatCountryCode | COUNTRY_CODE | — | — |

### [[zx_fc_product_fiscal_v|ZX_FC_PRODUCT_FISCAL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProdFiscClsCategoryId | CATEGORY_ID | — | — |
| 2 | ProdFiscClsCategorySetId | CATEGORY_SET_ID | — | — |
| 3 | ProdFiscClsClassificationCode | CLASSIFICATION_CODE | — | — |
| 4 | ProdFiscClsClassificationName | CLASSIFICATION_NAME | — | ✅ |
| 5 | ProdFiscClsCountryCode | COUNTRY_CODE | — | — |
| 6 | ProdFiscClsEffectiveTo | EFFECTIVE_TO | — | — |
| 7 | ProdFiscClsStructureId | STRUCTURE_ID | — | — |
| 8 | ProdFiscClsStructureName | STRUCTURE_NAME | — | — |

### [[zx_fc_user_defined_v|ZX_FC_USER_DEFINED_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LineUsrDfndFiscClsClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | LineUsrDfndFiscClsClassificationName | CLASSIFICATION_NAME | — | ✅ |
| 3 | LineUsrDfndFiscClsCountryCode | COUNTRY_CODE | — | — |
| 4 | UsrDfndFiscClsClassificationCode | CLASSIFICATION_CODE | — | — |
| 5 | UsrDfndFiscClsClassificationName | CLASSIFICATION_NAME | — | ✅ |
| 6 | UsrDfndFiscClsCountryCode | COUNTRY_CODE | — | — |

### [[zx_lines|ZX_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DtlTaxLineAdjustedDocDate | ADJUSTED_DOC_DATE | — | — |
| 2 | DtlTaxLineAdjustedDocEntityCode | ADJUSTED_DOC_ENTITY_CODE | — | — |
| 3 | DtlTaxLineAdjustedDocEventClassCode | ADJUSTED_DOC_EVENT_CLASS_CODE | — | — |
| 4 | DtlTaxLineAdjustedDocNumber | ADJUSTED_DOC_NUMBER | — | — |
| 5 | DtlTaxLineAdjustedDocTrxLevelType | ADJUSTED_DOC_TRX_LEVEL_TYPE | — | — |
| 6 | DtlTaxLineAppliedFromEntityCode | APPLIED_FROM_ENTITY_CODE | — | — |
| 7 | DtlTaxLineAppliedFromEventClassCode | APPLIED_FROM_EVENT_CLASS_CODE | — | — |
| 8 | DtlTaxLineAppliedFromTrxLevelType | APPLIED_FROM_TRX_LEVEL_TYPE | — | — |
| 9 | DtlTaxLineAppliedFromTrxNumber | APPLIED_FROM_TRX_NUMBER | — | — |
| 10 | DtlTaxLineAppliedToEntityCode | APPLIED_TO_ENTITY_CODE | — | — |
| 11 | DtlTaxLineAppliedToEventClassCode | APPLIED_TO_EVENT_CLASS_CODE | — | — |
| 12 | DtlTaxLineAppliedToTrxLevelType | APPLIED_TO_TRX_LEVEL_TYPE | — | — |
| 13 | DtlTaxLineAppliedToTrxNumber | APPLIED_TO_TRX_NUMBER | — | — |
| 14 | DtlTaxLineAssociatedChildFrozenFlag | ASSOCIATED_CHILD_FROZEN_FLAG | — | — |
| 15 | DtlTaxLineCalTaxAmt | CAL_TAX_AMT | — | — |
| 16 | DtlTaxLineCalTaxAmtFunclCurr | CAL_TAX_AMT_FUNCL_CURR | — | — |
| 17 | DtlTaxLineCalTaxAmtTaxCurr | CAL_TAX_AMT_TAX_CURR | — | — |
| 18 | DtlTaxLineCancelFlag | CANCEL_FLAG | — | — |
| 19 | DtlTaxLineCompoundingDepTaxFlag | COMPOUNDING_DEP_TAX_FLAG | — | — |
| 20 | DtlTaxLineCompoundingTaxFlag | COMPOUNDING_TAX_FLAG | — | — |
| 21 | DtlTaxLineCompoundingTaxMissFlag | COMPOUNDING_TAX_MISS_FLAG | — | — |
| 22 | DtlTaxLineCopiedFromOtherDocFlag | COPIED_FROM_OTHER_DOC_FLAG | — | — |
| 23 | DtlTaxLineCtrlTotalLineTxAmt | CTRL_TOTAL_LINE_TX_AMT | — | — |
| 24 | DtlTaxLineCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | — |
| 25 | DtlTaxLineCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | — |
| 26 | DtlTaxLineCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | — |
| 27 | DtlTaxLineDeleteFlag | DELETE_FLAG | — | — |
| 28 | DtlTaxLineDocEventStatus | DOC_EVENT_STATUS | — | — |
| 29 | DtlTaxLineEnforceFromNaturalAcctFlag | ENFORCE_FROM_NATURAL_ACCT_FLAG | — | — |
| 30 | DtlTaxLineEntityCode | ENTITY_CODE | — | — |
| 31 | DtlTaxLineEventClassCode | EVENT_CLASS_CODE | — | — |
| 32 | DtlTaxLineEventTypeCode | EVENT_TYPE_CODE | — | — |
| 33 | DtlTaxLineExceptionRate | EXCEPTION_RATE | — | — |
| 34 | DtlTaxLineExemptCertificateNumber | EXEMPT_CERTIFICATE_NUMBER | — | — |
| 35 | DtlTaxLineExemptRateModifier | EXEMPT_RATE_MODIFIER | — | — |
| 36 | DtlTaxLineExemptReason | EXEMPT_REASON | — | — |
| 37 | DtlTaxLineExemptReasonCode | EXEMPT_REASON_CODE | — | — |
| 38 | DtlTaxLineFreezeUntilOverriddenFlag | FREEZE_UNTIL_OVERRIDDEN_FLAG | — | — |
| 39 | DtlTaxLineHistoricalFlag | HISTORICAL_FLAG | — | — |
| 40 | DtlTaxLineHqEstbRegNumber | HQ_ESTB_REG_NUMBER | — | — |
| 41 | DtlTaxLineInterfaceEntityCode | INTERFACE_ENTITY_CODE | — | — |
| 42 | DtlTaxLineItemDistChangedFlag | ITEM_DIST_CHANGED_FLAG | — | — |
| 43 | DtlTaxLineLastManualEntry | LAST_MANUAL_ENTRY | — | — |
| 44 | DtlTaxLineLegalEntityTaxRegNumber | LEGAL_ENTITY_TAX_REG_NUMBER | — | — |
| 45 | DtlTaxLineLegalMessageAppl2 | LEGAL_MESSAGE_APPL_2 | — | — |
| 46 | DtlTaxLineLegalMessageBasis | LEGAL_MESSAGE_BASIS | — | — |
| 47 | DtlTaxLineLegalMessageCalc | LEGAL_MESSAGE_CALC | — | — |
| 48 | DtlTaxLineLegalMessageExcpt | LEGAL_MESSAGE_EXCPT | — | — |
| 49 | DtlTaxLineLegalMessageExmpt | LEGAL_MESSAGE_EXMPT | — | — |
| 50 | DtlTaxLineLegalMessagePos | LEGAL_MESSAGE_POS | — | — |
| 51 | DtlTaxLineLegalMessageRate | LEGAL_MESSAGE_RATE | — | — |
| 52 | DtlTaxLineLegalMessageStatus | LEGAL_MESSAGE_STATUS | — | — |
| 53 | DtlTaxLineLegalMessageThreshold | LEGAL_MESSAGE_THRESHOLD | — | — |
| 54 | DtlTaxLineLegalMessageTrn | LEGAL_MESSAGE_TRN | — | — |
| 55 | DtlTaxLineLegalReportingStatus | LEGAL_REPORTING_STATUS | — | — |
| 56 | DtlTaxLineLineAmt | LINE_AMT | — | — |
| 57 | DtlTaxLineLineAssessableValue | LINE_ASSESSABLE_VALUE | — | — |
| 58 | DtlTaxLineManuallyEnteredFlag | MANUALLY_ENTERED_FLAG | — | — |
| 59 | DtlTaxLineMinimumAccountableUnit | MINIMUM_ACCOUNTABLE_UNIT | — | — |
| 60 | DtlTaxLineMrcTaxLineFlag | MRC_TAX_LINE_FLAG | — | — |
| 61 | DtlTaxLineMultipleJurisdictionsFlag | MULTIPLE_JURISDICTIONS_FLAG | — | — |
| 62 | DtlTaxLineNrecTaxAmt | NREC_TAX_AMT | — | — |
| 63 | DtlTaxLineNrecTaxAmtFunclCurr | NREC_TAX_AMT_FUNCL_CURR | — | — |
| 64 | DtlTaxLineNrecTaxAmtTaxCurr | NREC_TAX_AMT_TAX_CURR | — | — |
| 65 | DtlTaxLineOffsetFlag | OFFSET_FLAG | — | — |
| 66 | DtlTaxLineOffsetTaxRateCode | OFFSET_TAX_RATE_CODE | — | — |
| 67 | DtlTaxLineOrigSelfAssessedFlag | ORIG_SELF_ASSESSED_FLAG | — | — |
| 68 | DtlTaxLineOrigTaxAmt | ORIG_TAX_AMT | — | — |
| 69 | DtlTaxLineOrigTaxAmtIncludedFlag | ORIG_TAX_AMT_INCLUDED_FLAG | — | — |
| 70 | DtlTaxLineOrigTaxAmtTaxCurr | ORIG_TAX_AMT_TAX_CURR | — | — |
| 71 | DtlTaxLineOrigTaxJurisdictionCode | ORIG_TAX_JURISDICTION_CODE | — | — |
| 72 | DtlTaxLineOrigTaxRate | ORIG_TAX_RATE | — | — |
| 73 | DtlTaxLineOrigTaxRateCode | ORIG_TAX_RATE_CODE | — | — |
| 74 | DtlTaxLineOrigTaxStatusCode | ORIG_TAX_STATUS_CODE | — | — |
| 75 | DtlTaxLineOrigTaxableAmt | ORIG_TAXABLE_AMT | — | — |
| 76 | DtlTaxLineOrigTaxableAmtTaxCurr | ORIG_TAXABLE_AMT_TAX_CURR | — | — |
| 77 | DtlTaxLineOtherDocLineAmt | OTHER_DOC_LINE_AMT | — | — |
| 78 | DtlTaxLineOtherDocLineTaxAmt | OTHER_DOC_LINE_TAX_AMT | — | — |
| 79 | DtlTaxLineOtherDocLineTaxableAmt | OTHER_DOC_LINE_TAXABLE_AMT | — | — |
| 80 | DtlTaxLineOtherDocSource | OTHER_DOC_SOURCE | — | — |
| 81 | DtlTaxLineOverriddenFlag | OVERRIDDEN_FLAG | — | — |
| 82 | DtlTaxLinePlaceOfSupply | PLACE_OF_SUPPLY | — | — |
| 83 | DtlTaxLinePlaceOfSupplyTypeCode | PLACE_OF_SUPPLY_TYPE_CODE | — | — |
| 84 | DtlTaxLinePrdTotalTaxAmt | PRD_TOTAL_TAX_AMT | — | — |
| 85 | DtlTaxLinePrdTotalTaxAmtFunclCurr | PRD_TOTAL_TAX_AMT_FUNCL_CURR | — | — |
| 86 | DtlTaxLinePrdTotalTaxAmtTaxCurr | PRD_TOTAL_TAX_AMT_TAX_CURR | — | — |
| 87 | DtlTaxLinePrecision | PRECISION | — | — |
| 88 | DtlTaxLineProcessForRecoveryFlag | PROCESS_FOR_RECOVERY_FLAG | — | — |
| 89 | DtlTaxLineProrationCode | PRORATION_CODE | — | — |
| 90 | DtlTaxLinePurgeFlag | PURGE_FLAG | — | — |
| 91 | DtlTaxLineRecTaxAmt | REC_TAX_AMT | — | — |
| 92 | DtlTaxLineRecTaxAmtFunclCurr | REC_TAX_AMT_FUNCL_CURR | — | — |
| 93 | DtlTaxLineRecTaxAmtTaxCurr | REC_TAX_AMT_TAX_CURR | — | — |
| 94 | DtlTaxLineRecalcRequiredFlag | RECALC_REQUIRED_FLAG | — | — |
| 95 | DtlTaxLineRecordTypeCode | RECORD_TYPE_CODE | — | — |
| 96 | DtlTaxLineRefDocEntityCode | REF_DOC_ENTITY_CODE | — | — |
| 97 | DtlTaxLineRefDocEventClassCode | REF_DOC_EVENT_CLASS_CODE | — | — |
| 98 | DtlTaxLineRefDocLineQuantity | REF_DOC_LINE_QUANTITY | — | — |
| 99 | DtlTaxLineRefDocTrxLevelType | REF_DOC_TRX_LEVEL_TYPE | — | — |
| 100 | DtlTaxLineRegistrationPartyType | REGISTRATION_PARTY_TYPE | — | — |
| 101 | DtlTaxLineRelatedDocDate | RELATED_DOC_DATE | — | — |
| 102 | DtlTaxLineRelatedDocEntityCode | RELATED_DOC_ENTITY_CODE | — | — |
| 103 | DtlTaxLineRelatedDocEventClassCode | RELATED_DOC_EVENT_CLASS_CODE | — | — |
| 104 | DtlTaxLineRelatedDocNumber | RELATED_DOC_NUMBER | — | — |
| 105 | DtlTaxLineRelatedDocTrxLevelType | RELATED_DOC_TRX_LEVEL_TYPE | — | — |
| 106 | DtlTaxLineReportingCurrencyCode | REPORTING_CURRENCY_CODE | — | — |
| 107 | DtlTaxLineReportingOnlyFlag | REPORTING_ONLY_FLAG | — | — |
| 108 | DtlTaxLineRoundingLevelCode | ROUNDING_LEVEL_CODE | — | — |
| 109 | DtlTaxLineRoundingLvlPartyType | ROUNDING_LVL_PARTY_TYPE | — | — |
| 110 | DtlTaxLineRoundingRuleCode | ROUNDING_RULE_CODE | — | — |
| 111 | DtlTaxLineSelfAssessedFlag | SELF_ASSESSED_FLAG | — | — |
| 112 | DtlTaxLineSettlementFlag | SETTLEMENT_FLAG | — | — |
| 113 | DtlTaxLineSyncWithPrvdrFlag | SYNC_WITH_PRVDR_FLAG | — | — |
| 114 | DtlTaxLineTax | TAX | — | — |
| 115 | DtlTaxLineTaxAmt | TAX_AMT | — | — |
| 116 | DtlTaxLineTaxAmtFunclCurr | TAX_AMT_FUNCL_CURR | — | — |
| 117 | DtlTaxLineTaxAmtIncludedFlag | TAX_AMT_INCLUDED_FLAG | — | — |
| 118 | DtlTaxLineTaxAmtTaxCurr | TAX_AMT_TAX_CURR | — | — |
| 119 | DtlTaxLineTaxApportionmentFlag | TAX_APPORTIONMENT_FLAG | — | — |
| 120 | DtlTaxLineTaxApportionmentLineNumber | TAX_APPORTIONMENT_LINE_NUMBER | — | — |
| 121 | DtlTaxLineTaxBaseModifierRate | TAX_BASE_MODIFIER_RATE | — | — |
| 122 | DtlTaxLineTaxCalculationFormula | TAX_CALCULATION_FORMULA | — | — |
| 123 | DtlTaxLineTaxCode | TAX_CODE | — | — |
| 124 | DtlTaxLineTaxCurrencyCode | TAX_CURRENCY_CODE | — | — |
| 125 | DtlTaxLineTaxCurrencyConversionDate | TAX_CURRENCY_CONVERSION_DATE | — | — |
| 126 | DtlTaxLineTaxCurrencyConversionRate | TAX_CURRENCY_CONVERSION_RATE | — | — |
| 127 | DtlTaxLineTaxCurrencyConversionType | TAX_CURRENCY_CONVERSION_TYPE | — | — |
| 128 | DtlTaxLineTaxDate | TAX_DATE | — | — |
| 129 | DtlTaxLineTaxDetermineDate | TAX_DETERMINE_DATE | — | — |
| 130 | DtlTaxLineTaxEventClassCode | TAX_EVENT_CLASS_CODE | — | — |
| 131 | DtlTaxLineTaxEventTypeCode | TAX_EVENT_TYPE_CODE | — | — |
| 132 | DtlTaxLineTaxHoldCode | TAX_HOLD_CODE | — | — |
| 133 | DtlTaxLineTaxHoldReleasedCode | TAX_HOLD_RELEASED_CODE | — | — |
| 134 | DtlTaxLineTaxJurisdictionCode | TAX_JURISDICTION_CODE | — | — |
| 135 | DtlTaxLineTaxLineId | TAX_LINE_ID | — | — |
| 136 | DtlTaxLineTaxLineNumber | TAX_LINE_NUMBER | — | — |
| 137 | DtlTaxLineTaxOnlyLineFlag | TAX_ONLY_LINE_FLAG | — | — |
| 138 | DtlTaxLineTaxPointDate | TAX_POINT_DATE | — | — |
| 139 | DtlTaxLineTaxRate | TAX_RATE | — | — |
| 140 | DtlTaxLineTaxRateBeforeException | TAX_RATE_BEFORE_EXCEPTION | — | — |
| 141 | DtlTaxLineTaxRateBeforeExemption | TAX_RATE_BEFORE_EXEMPTION | — | — |
| 142 | DtlTaxLineTaxRateCode | TAX_RATE_CODE | — | — |
| 143 | DtlTaxLineTaxRateNameBeforeException | TAX_RATE_NAME_BEFORE_EXCEPTION | — | — |
| 144 | DtlTaxLineTaxRateNameBeforeExemption | TAX_RATE_NAME_BEFORE_EXEMPTION | — | — |
| 145 | DtlTaxLineTaxRateType | TAX_RATE_TYPE | — | — |
| 146 | DtlTaxLineTaxRegimeCode | TAX_REGIME_CODE | — | — |
| 147 | DtlTaxLineTaxRegistrationNumber | TAX_REGISTRATION_NUMBER | — | — |
| 148 | DtlTaxLineTaxStatusCode | TAX_STATUS_CODE | — | — |
| 149 | DtlTaxLineTaxTypeCode | TAX_TYPE_CODE | — | — |
| 150 | DtlTaxLineTaxableAmt | TAXABLE_AMT | — | — |
| 151 | DtlTaxLineTaxableAmtFunclCurr | TAXABLE_AMT_FUNCL_CURR | — | — |
| 152 | DtlTaxLineTaxableAmtTaxCurr | TAXABLE_AMT_TAX_CURR | — | — |
| 153 | DtlTaxLineTaxableBasisFormula | TAXABLE_BASIS_FORMULA | — | — |
| 154 | DtlTaxLineTrxCurrencyCode | TRX_CURRENCY_CODE | — | — |
| 155 | DtlTaxLineTrxDate | TRX_DATE | — | — |
| 156 | DtlTaxLineTrxLevelType | TRX_LEVEL_TYPE | — | — |
| 157 | DtlTaxLineTrxLineDate | TRX_LINE_DATE | — | — |
| 158 | DtlTaxLineTrxLineIndex | TRX_LINE_INDEX | — | — |
| 159 | DtlTaxLineTrxLineNumber | TRX_LINE_NUMBER | — | — |
| 160 | DtlTaxLineTrxLineQuantity | TRX_LINE_QUANTITY | — | — |
| 161 | DtlTaxLineTrxNumber | TRX_NUMBER | — | — |
| 162 | DtlTaxLineUnitPrice | UNIT_PRICE | — | — |
| 163 | DtlTaxLineUnroundedTaxAmt | UNROUNDED_TAX_AMT | — | — |
| 164 | DtlTaxLineUnroundedTaxableAmt | UNROUNDED_TAXABLE_AMT | — | — |
| 165 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |

### [[zx_product_types_v|ZX_PRODUCT_TYPES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProdTypeClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | ProdTypeClassificationName | CLASSIFICATION_NAME | — | ✅ |

### [[zx_registrations|ZX_REGISTRATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FirstPartyObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | FirstPartyRegistrationId | REGISTRATION_ID | — | — |
| 3 | FirstPartyRegistrationNumber | REGISTRATION_NUMBER | — | ✅ |
| 4 | ThirdPartyObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | ThirdPartyRegistrationId | REGISTRATION_ID | — | — |
| 6 | ThirdPartyRegistrationNumber | REGISTRATION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
