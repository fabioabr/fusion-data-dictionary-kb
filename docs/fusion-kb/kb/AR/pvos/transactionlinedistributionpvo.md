---
id: DOC-AR-PVO-TransactionLineDistributionPVO
doc_type: system-doc
title: "TransactionLineDistributionPVO — PVO Accounts Receivable"
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
  - TransactionLineDistributionPVO
  - transactionlinedistributionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionLineDistributionPVO

## 📌 Visão Geral

Extrai as distribuições contábeis das linhas de transação, detalhando como cada linha impacta as contas do GL por vendedor e centro de custo. Fundamental para reconciliação contábil granular e análise de rentabilidade por produto.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.TransactionLineDistributionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 2455 | 48 | 1 | 226 | 9% |

---

## 🔗 Tabelas Relacionadas

- [[ar_batches_all|AR_BATCHES_ALL]] — 46 atributos (1 BICC)
- [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]] — 5 atributos (1 BICC)
- [[ar_deferred_lines_all|AR_DEFERRED_LINES_ALL]] — 18 atributos
- [[ar_interest_headers_all|AR_INTEREST_HEADERS_ALL]] — 35 atributos
- [[ar_interest_lines_all|AR_INTEREST_LINES_ALL]] — 22 atributos (4 BICC)
- [[ar_lookups|AR_LOOKUPS]] — 4 atributos (1 BICC)
- [[ar_memo_lines_all_b|AR_MEMO_LINES_ALL_B]] — 18 atributos (1 BICC)
- [[ar_memo_lines_all_tl|AR_MEMO_LINES_ALL_TL]] — 5 atributos (2 BICC)
- [[ar_payment_schedules_all|AR_PAYMENT_SCHEDULES_ALL]] — 93 atributos (1 BICC)
- [[ar_recon_difference_details|AR_RECON_DIFFERENCE_DETAILS]] — 17 atributos
- [[ar_revenue_adjustments_all|AR_REVENUE_ADJUSTMENTS_ALL]] — 32 atributos (1 BICC)
- [[ce_bank_acct_uses_all|CE_BANK_ACCT_USES_ALL]] — 30 atributos (1 BICC)
- [[ce_internal_bank_accts_v|CE_INTERNAL_BANK_ACCTS_V]] — 81 atributos (1 BICC)
- [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]] — 5 atributos (1 BICC)
- [[fnd_territories_vl|FND_TERRITORIES_VL]] — 9 atributos (1 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 1 atributos
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 18 atributos (2 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 3 atributos
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 18 atributos (3 BICC)
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 40 atributos (4 BICC)
- [[hz_cust_account_roles|HZ_CUST_ACCOUNT_ROLES]] — 2 atributos
- [[hz_cust_acct_sites_all|HZ_CUST_ACCT_SITES_ALL]] — 15 atributos
- [[hz_cust_site_uses_all|HZ_CUST_SITE_USES_ALL]] — 6 atributos
- [[hz_locations|HZ_LOCATIONS]] — 26 atributos (20 BICC)
- [[hz_parties|HZ_PARTIES]] — 38 atributos (4 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 12 atributos (3 BICC)
- [[hz_party_site_uses|HZ_PARTY_SITE_USES]] — 3 atributos (1 BICC)
- [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]] — 44 atributos (2 BICC)
- [[iby_fndcpt_tx_extensions|IBY_FNDCPT_TX_EXTENSIONS]] — 28 atributos (2 BICC)
- [[inv_units_of_measure_b|INV_UNITS_OF_MEASURE_B]] — 3 atributos
- [[inv_units_of_measure_tl|INV_UNITS_OF_MEASURE_TL]] — 4 atributos (2 BICC)
- [[jtf_rs_salesreps|JTF_RS_SALESREPS]] — 2 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos
- [[per_users|PER_USERS]] — 9 atributos
- [[ra_batches_all|RA_BATCHES_ALL]] — 33 atributos (1 BICC)
- [[ra_batch_sources_all|RA_BATCH_SOURCES_ALL]] — 124 atributos (3 BICC)
- [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]] — 733 atributos (75 BICC)
- [[ra_customer_trx_lines_all|RA_CUSTOMER_TRX_LINES_ALL]] — 596 atributos (57 BICC)
- [[ra_cust_trx_line_gl_dist_all|RA_CUST_TRX_LINE_GL_DIST_ALL]] — 40 atributos (1 PKs, 19 BICC)
- [[ra_cust_trx_line_salesreps_all|RA_CUST_TRX_LINE_SALESREPS_ALL]] — 26 atributos (3 BICC)
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
| 4 | RevCashRcptObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | RevCashRcptReceiptNumber | RECEIPT_NUMBER | — | ✅ |

### [[ar_deferred_lines_all|AR_DEFERRED_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeferredLineAcctdAmountDueOriginal | ACCTD_AMOUNT_DUE_ORIGINAL | — | — |
| 2 | DeferredLineAcctdAmountPending | ACCTD_AMOUNT_PENDING | — | — |
| 3 | DeferredLineAcctdAmountRecognized | ACCTD_AMOUNT_RECOGNIZED | — | — |
| 4 | DeferredLineAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 5 | DeferredLineAmountPending | AMOUNT_PENDING | — | — |
| 6 | DeferredLineAmountRecognized | AMOUNT_RECOGNIZED | — | — |
| 7 | DeferredLineCreatedBy | CREATED_BY | — | — |
| 8 | DeferredLineCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 9 | DeferredLineCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 10 | DeferredLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | DeferredLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | DeferredLineLineCollectibleFlag | LINE_COLLECTIBLE_FLAG | — | — |
| 13 | DeferredLineManualOverrideFlag | MANUAL_OVERRIDE_FLAG | — | — |
| 14 | DeferredLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | DeferredLineOrgId | ORG_ID | — | — |
| 16 | DeferredLineOriginalCollectibilityFlag | ORIGINAL_COLLECTIBILITY_FLAG | — | — |
| 17 | DeferredLineParentLineId | PARENT_LINE_ID | — | — |
| 18 | DeferredLineRequestId | REQUEST_ID | — | — |

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
| 2 | MemoLineCreatedBy | CREATED_BY | — | — |
| 3 | MemoLineCreationDate | CREATION_DATE | — | — |
| 4 | MemoLineEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 5 | MemoLineEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 6 | MemoLineInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 7 | MemoLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | MemoLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | MemoLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | MemoLineLineType | LINE_TYPE | — | — |
| 11 | MemoLineMemoLineId | MEMO_LINE_ID | — | — |
| 12 | MemoLineMemoLineSeqId | MEMO_LINE_SEQ_ID | — | — |
| 13 | MemoLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | MemoLineSetId | SET_ID | — | — |
| 15 | MemoLineTaxCode | TAX_CODE | — | — |
| 16 | MemoLineTaxProductCategory | TAX_PRODUCT_CATEGORY | — | — |
| 17 | MemoLineUnitStdPrice | UNIT_STD_PRICE | — | — |
| 18 | MemoLineUomCode | UOM_CODE | — | — |

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
| 1 | TransactionLineBRAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | — |
| 2 | TransactionLineBRActiveClaimFlag | ACTIVE_CLAIM_FLAG | — | — |
| 3 | TransactionLineBRActualDateClosed | ACTUAL_DATE_CLOSED | — | — |
| 4 | TransactionLineBRAdjustmentAmountLast | ADJUSTMENT_AMOUNT_LAST | — | — |
| 5 | TransactionLineBRAdjustmentDateLast | ADJUSTMENT_DATE_LAST | — | — |
| 6 | TransactionLineBRAdjustmentGlDateLast | ADJUSTMENT_GL_DATE_LAST | — | — |
| 7 | TransactionLineBRAdjustmentIdLast | ADJUSTMENT_ID_LAST | — | — |
| 8 | TransactionLineBRAmountAdjusted | AMOUNT_ADJUSTED | — | — |
| 9 | TransactionLineBRAmountAdjustedPending | AMOUNT_ADJUSTED_PENDING | — | — |
| 10 | TransactionLineBRAmountApplied | AMOUNT_APPLIED | — | — |
| 11 | TransactionLineBRAmountCredited | AMOUNT_CREDITED | — | — |
| 12 | TransactionLineBRAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 13 | TransactionLineBRAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 14 | TransactionLineBRAmountInDispute | AMOUNT_IN_DISPUTE | — | — |
| 15 | TransactionLineBRAmountLineItemsOriginal | AMOUNT_LINE_ITEMS_ORIGINAL | — | — |
| 16 | TransactionLineBRAmountLineItemsRemaining | AMOUNT_LINE_ITEMS_REMAINING | — | — |
| 17 | TransactionLineBRAmountOnAccount | AMOUNT_ON_ACCOUNT | — | — |
| 18 | TransactionLineBRAmountOtherAccount | AMOUNT_OTHER_ACCOUNT | — | — |
| 19 | TransactionLineBRAssociatedCashReceiptId | ASSOCIATED_CASH_RECEIPT_ID | — | — |
| 20 | TransactionLineBRBrAmountAssigned | BR_AMOUNT_ASSIGNED | — | — |
| 21 | TransactionLineBRCallDateLast | CALL_DATE_LAST | — | — |
| 22 | TransactionLineBRCashAppliedAmountLast | CASH_APPLIED_AMOUNT_LAST | — | — |
| 23 | TransactionLineBRCashAppliedDateLast | CASH_APPLIED_DATE_LAST | — | — |
| 24 | TransactionLineBRCashAppliedIdLast | CASH_APPLIED_ID_LAST | — | — |
| 25 | TransactionLineBRCashAppliedStatusLast | CASH_APPLIED_STATUS_LAST | — | — |
| 26 | TransactionLineBRCashGlDateLast | CASH_GL_DATE_LAST | — | — |
| 27 | TransactionLineBRCashReceiptAmountLast | CASH_RECEIPT_AMOUNT_LAST | — | — |
| 28 | TransactionLineBRCashReceiptDateLast | CASH_RECEIPT_DATE_LAST | — | — |
| 29 | TransactionLineBRCashReceiptId | CASH_RECEIPT_ID | — | — |
| 30 | TransactionLineBRCashReceiptIdLast | CASH_RECEIPT_ID_LAST | — | — |
| 31 | TransactionLineBRCashReceiptStatusLast | CASH_RECEIPT_STATUS_LAST | — | — |
| 32 | TransactionLineBRCollectorLast | COLLECTOR_LAST | — | — |
| 33 | TransactionLineBRConsInvId | CONS_INV_ID | — | — |
| 34 | TransactionLineBRConsInvIdRev | CONS_INV_ID_REV | — | — |
| 35 | TransactionLineBRCreatedBy | CREATED_BY | — | — |
| 36 | TransactionLineBRCreationDate | CREATION_DATE | — | — |
| 37 | TransactionLineBRCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 38 | TransactionLineBRCustomerId | CUSTOMER_ID | — | — |
| 39 | TransactionLineBRCustomerSiteUseId | CUSTOMER_SITE_USE_ID | — | — |
| 40 | TransactionLineBRCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 41 | TransactionLineBRDiscountDate | DISCOUNT_DATE | — | — |
| 42 | TransactionLineBRDiscountOriginal | DISCOUNT_ORIGINAL | — | — |
| 43 | TransactionLineBRDiscountRemaining | DISCOUNT_REMAINING | — | — |
| 44 | TransactionLineBRDiscountTakenEarned | DISCOUNT_TAKEN_EARNED | — | — |
| 45 | TransactionLineBRDiscountTakenUnearned | DISCOUNT_TAKEN_UNEARNED | — | — |
| 46 | TransactionLineBRDisputeDate | DISPUTE_DATE | — | — |
| 47 | TransactionLineBRDueDate | DUE_DATE | — | — |
| 48 | TransactionLineBRDunningLevelOverrideDate | DUNNING_LEVEL_OVERRIDE_DATE | — | — |
| 49 | TransactionLineBRExchangeDate | EXCHANGE_DATE | — | — |
| 50 | TransactionLineBRExchangeRate | EXCHANGE_RATE | — | — |
| 51 | TransactionLineBRExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 52 | TransactionLineBRExcludeFromConsBillFlag | EXCLUDE_FROM_CONS_BILL_FLAG | — | — |
| 53 | TransactionLineBRExcludeFromDunningFlag | EXCLUDE_FROM_DUNNING_FLAG | — | — |
| 54 | TransactionLineBRFollowUpCodeLast | FOLLOW_UP_CODE_LAST | — | — |
| 55 | TransactionLineBRFollowUpDateLast | FOLLOW_UP_DATE_LAST | — | — |
| 56 | TransactionLineBRFreightOriginal | FREIGHT_ORIGINAL | — | — |
| 57 | TransactionLineBRFreightRemaining | FREIGHT_REMAINING | — | — |
| 58 | TransactionLineBRGlDate | GL_DATE | — | — |
| 59 | TransactionLineBRGlDateClosed | GL_DATE_CLOSED | — | — |
| 60 | TransactionLineBRInCollection | IN_COLLECTION | — | — |
| 61 | TransactionLineBRInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 62 | TransactionLineBRLastChargeDate | LAST_CHARGE_DATE | — | — |
| 63 | TransactionLineBRLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 64 | TransactionLineBRLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 65 | TransactionLineBRLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 66 | TransactionLineBRNumberOfDueDates | NUMBER_OF_DUE_DATES | — | — |
| 67 | TransactionLineBRObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 68 | TransactionLineBROrgId | ORG_ID | — | — |
| 69 | TransactionLineBRPaymentApproval | PAYMENT_APPROVAL | — | — |
| 70 | TransactionLineBRPaymentScheduleClass | CLASS | — | — |
| 71 | TransactionLineBRPaymentScheduleId | PAYMENT_SCHEDULE_ID | — | — |
| 72 | TransactionLineBRProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 73 | TransactionLineBRProgramId | PROGRAM_ID | — | — |
| 74 | TransactionLineBRProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 75 | TransactionLineBRPromiseAmountLast | PROMISE_AMOUNT_LAST | — | — |
| 76 | TransactionLineBRPromiseDateLast | PROMISE_DATE_LAST | — | — |
| 77 | TransactionLineBRReceiptConfirmedFlag | RECEIPT_CONFIRMED_FLAG | — | — |
| 78 | TransactionLineBRReceivablesChargesCharged | RECEIVABLES_CHARGES_CHARGED | — | — |
| 79 | TransactionLineBRReceivablesChargesRemaining | RECEIVABLES_CHARGES_REMAINING | — | — |
| 80 | TransactionLineBRRequestId | REQUEST_ID | — | — |
| 81 | TransactionLineBRReservedType | RESERVED_TYPE | — | — |
| 82 | TransactionLineBRReservedValue | RESERVED_VALUE | — | — |
| 83 | TransactionLineBRReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 84 | TransactionLineBRSecondLastChargeDate | SECOND_LAST_CHARGE_DATE | — | — |
| 85 | TransactionLineBRSelectedForReceiptBatchId | SELECTED_FOR_RECEIPT_BATCH_ID | — | — |
| 86 | TransactionLineBRStagedDunningLevel | STAGED_DUNNING_LEVEL | — | — |
| 87 | TransactionLineBRStatus | STATUS | — | — |
| 88 | TransactionLineBRTaxOriginal | TAX_ORIGINAL | — | — |
| 89 | TransactionLineBRTaxRemaining | TAX_REMAINING | — | — |
| 90 | TransactionLineBRTermId | TERM_ID | — | — |
| 91 | TransactionLineBRTermsSequenceNumber | TERMS_SEQUENCE_NUMBER | — | — |
| 92 | TransactionLineBRTrxDate | TRX_DATE | — | — |
| 93 | TransactionLineBRTrxNumber | TRX_NUMBER | — | — |

### [[ar_recon_difference_details|AR_RECON_DIFFERENCE_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReconDiffAccountedAmount | ACCOUNTED_AMOUNT | — | — |
| 2 | ReconDiffAccountingDate | ACCOUNTING_DATE | — | — |
| 3 | ReconDiffCauseOfDifferenceCode | CAUSE_OF_DIFFERENCE_CODE | — | — |
| 4 | ReconDiffCreatedBy | CREATED_BY | — | — |
| 5 | ReconDiffCreationDate | CREATION_DATE | — | — |
| 6 | ReconDiffDocDistId | DOCUMENT_DISTRIBUTION_ID | — | — |
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

### [[ar_revenue_adjustments_all|AR_REVENUE_ADJUSTMENTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RevenueAdjustmentAmount | AMOUNT | — | — |
| 2 | RevenueAdjustmentAmountMode | AMOUNT_MODE | — | — |
| 3 | RevenueAdjustmentApplicationDate | APPLICATION_DATE | — | — |
| 4 | RevenueAdjustmentCreatedBy | CREATED_BY | — | — |
| 5 | RevenueAdjustmentCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 6 | RevenueAdjustmentFromCategoryId | FROM_CATEGORY_ID | — | — |
| 7 | RevenueAdjustmentFromCustTrxLineId | FROM_CUST_TRX_LINE_ID | — | — |
| 8 | RevenueAdjustmentFromInventoryItemId | FROM_INVENTORY_ITEM_ID | — | — |
| 9 | RevenueAdjustmentFromResourceSalesrepId | FROM_RESOURCE_SALESREP_ID | — | — |
| 10 | RevenueAdjustmentFromSalesgroupId | FROM_SALESGROUP_ID | — | — |
| 11 | RevenueAdjustmentGlDate | GL_DATE | — | — |
| 12 | RevenueAdjustmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | RevenueAdjustmentLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | RevenueAdjustmentLineSelectionMode | LINE_SELECTION_MODE | — | — |
| 15 | RevenueAdjustmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | RevenueAdjustmentOrgId | ORG_ID | — | — |
| 17 | RevenueAdjustmentPercent | PERCENT | — | — |
| 18 | RevenueAdjustmentProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 19 | RevenueAdjustmentProgramId | PROGRAM_ID | — | — |
| 20 | RevenueAdjustmentProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 21 | RevenueAdjustmentReasonCode | REASON_CODE | — | — |
| 22 | RevenueAdjustmentRequestId | REQUEST_ID | — | — |
| 23 | RevenueAdjustmentRevenueAdjustmentId | REVENUE_ADJUSTMENT_ID | — | — |
| 24 | RevenueAdjustmentRevenueAdjustmentNumber | REVENUE_ADJUSTMENT_NUMBER | — | ✅ |
| 25 | RevenueAdjustmentSalesCreditType | SALES_CREDIT_TYPE | — | — |
| 26 | RevenueAdjustmentStatus | STATUS | — | — |
| 27 | RevenueAdjustmentToCategoryId | TO_CATEGORY_ID | — | — |
| 28 | RevenueAdjustmentToCustTrxLineId | TO_CUST_TRX_LINE_ID | — | — |
| 29 | RevenueAdjustmentToInventoryItemId | TO_INVENTORY_ITEM_ID | — | — |
| 30 | RevenueAdjustmentToResourceSalesrepId | TO_RESOURCE_SALESREP_ID | — | — |
| 31 | RevenueAdjustmentToSalesgroupId | TO_SALESGROUP_ID | — | — |
| 32 | RevenueAdjustmentType | TYPE | — | — |

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

### [[ce_internal_bank_accts_v|CE_INTERNAL_BANK_ACCTS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankAccountAccountClassification | ACCOUNT_CLASSIFICATION | — | — |
| 2 | BankAccountAccountHolderId | ACCOUNT_HOLDER_ID | — | — |
| 3 | BankAccountAccountHolderName | ACCOUNT_HOLDER_NAME | — | — |
| 4 | BankAccountAccountHolderNameAlt | ACCOUNT_HOLDER_NAME_ALT | — | — |
| 5 | BankAccountAccountOwnerOrgId | ACCOUNT_OWNER_ORG_ID | — | — |
| 6 | BankAccountAccountOwnerPartyId | ACCOUNT_OWNER_PARTY_ID | — | — |
| 7 | BankAccountAccountSuffix | ACCOUNT_SUFFIX | — | — |
| 8 | BankAccountAgencyLocationCode | AGENCY_LOCATION_CODE | — | — |
| 9 | BankAccountApUseAllowedFlag | AP_USE_ALLOWED_FLAG | — | — |
| 10 | BankAccountArUseAllowedFlag | AR_USE_ALLOWED_FLAG | — | — |
| 11 | BankAccountAssetCodeCombinationId | ASSET_CODE_COMBINATION_ID | — | — |
| 12 | BankAccountBankAccountId | BANK_ACCOUNT_ID | — | — |
| 13 | BankAccountBankAccountName | BANK_ACCOUNT_NAME | — | — |
| 14 | BankAccountBankAccountNameAlt | BANK_ACCOUNT_NAME_ALT | — | — |
| 15 | BankAccountBankAccountNum | BANK_ACCOUNT_NUM | — | — |
| 16 | BankAccountBankAccountNumElectronic | BANK_ACCOUNT_NUM_ELECTRONIC | — | — |
| 17 | BankAccountBankAccountType | BANK_ACCOUNT_TYPE | — | — |
| 18 | BankAccountBankBranchId | BANK_BRANCH_ID | — | — |
| 19 | BankAccountBankChargesCcid | BANK_CHARGES_CCID | — | — |
| 20 | BankAccountBankExchangeRateType | BANK_EXCHANGE_RATE_TYPE | — | — |
| 21 | BankAccountBankId | BANK_ID | — | — |
| 22 | BankAccountCashClearingCcid | CASH_CLEARING_CCID | — | — |
| 23 | BankAccountCashflowDisplayOrder | CASHFLOW_DISPLAY_ORDER | — | — |
| 24 | BankAccountCashpoolMinPaymentAmt | CASHPOOL_MIN_PAYMENT_AMT | — | — |
| 25 | BankAccountCashpoolMinReceiptAmt | CASHPOOL_MIN_RECEIPT_AMT | — | — |
| 26 | BankAccountCashpoolRoundFactor | CASHPOOL_ROUND_FACTOR | — | — |
| 27 | BankAccountCashpoolRoundRule | CASHPOOL_ROUND_RULE | — | — |
| 28 | BankAccountCheckDigits | CHECK_DIGITS | — | — |
| 29 | BankAccountCreatedBy | CREATED_BY | — | — |
| 30 | BankAccountCreationDate | CREATION_DATE | — | — |
| 31 | BankAccountCurrencyCode | CURRENCY_CODE | — | — |
| 32 | BankAccountDataSecurityFlag | DATA_SECURITY_FLAG | — | — |
| 33 | BankAccountDescription | DESCRIPTION | — | — |
| 34 | BankAccountDescriptionCode1 | DESCRIPTION_CODE1 | — | — |
| 35 | BankAccountDescriptionCode2 | DESCRIPTION_CODE2 | — | — |
| 36 | BankAccountEftRequesterIdentifier | EFT_REQUESTER_IDENTIFIER | — | — |
| 37 | BankAccountEftUserNum | EFT_USER_NUM | — | — |
| 38 | BankAccountEndDate | END_DATE | — | — |
| 39 | BankAccountFxChargeCcid | FX_CHARGE_CCID | — | — |
| 40 | BankAccountGlCurExcRateType | GL_CUR_EXC_RATE_TYPE | — | — |
| 41 | BankAccountIbanNumber | IBAN_NUMBER | — | — |
| 42 | BankAccountInterestScheduleId | INTEREST_SCHEDULE_ID | — | — |
| 43 | BankAccountLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 44 | BankAccountLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 45 | BankAccountLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 46 | BankAccountManualToleranceRuleId | MANUAL_TOLERANCE_RULE_ID | — | — |
| 47 | BankAccountMaskedAccountNum | MASKED_ACCOUNT_NUM | — | — |
| 48 | BankAccountMaskedIban | MASKED_IBAN | — | — |
| 49 | BankAccountMaxCheckAmount | MAX_CHECK_AMOUNT | — | — |
| 50 | BankAccountMaxOutlay | MAX_OUTLAY | — | — |
| 51 | BankAccountMaxTargetBalance | MAX_TARGET_BALANCE | — | — |
| 52 | BankAccountMinCheckAmount | MIN_CHECK_AMOUNT | — | — |
| 53 | BankAccountMinTargetBalance | MIN_TARGET_BALANCE | — | — |
| 54 | BankAccountMultiCurrencyAllowedFlag | MULTI_CURRENCY_ALLOWED_FLAG | — | — |
| 55 | BankAccountNettingAcctFlag | NETTING_ACCT_FLAG | — | — |
| 56 | BankAccountObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 57 | BankAccountParsingRuleSetId | PARSING_RULE_SET_ID | — | — |
| 58 | BankAccountPayUseAllowedFlag | PAY_USE_ALLOWED_FLAG | — | — |
| 59 | BankAccountPoolBankChargeBearerCode | POOL_BANK_CHARGE_BEARER_CODE | — | — |
| 60 | BankAccountPoolPaymentMethodCode | POOL_PAYMENT_METHOD_CODE | — | — |
| 61 | BankAccountPoolPaymentReasonCode | POOL_PAYMENT_REASON_CODE | — | — |
| 62 | BankAccountPoolPaymentReasonComments | POOL_PAYMENT_REASON_COMMENTS | — | — |
| 63 | BankAccountPoolRemittanceMessage1 | POOL_REMITTANCE_MESSAGE1 | — | — |
| 64 | BankAccountPoolRemittanceMessage2 | POOL_REMITTANCE_MESSAGE2 | — | — |
| 65 | BankAccountPoolRemittanceMessage3 | POOL_REMITTANCE_MESSAGE3 | — | — |
| 66 | BankAccountPooledFlag | POOLED_FLAG | — | — |
| 67 | BankAccountProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 68 | BankAccountProgramId | PROGRAM_ID | — | — |
| 69 | BankAccountProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 70 | BankAccountReconDifferenceCcid | RECON_DIFFERENCE_CCID | — | — |
| 71 | BankAccountReconForBankXrateDateType | RECON_FOR_BANK_XRATE_DATE_TYPE | — | — |
| 72 | BankAccountReconForeignBankXrateType | RECON_FOREIGN_BANK_XRATE_TYPE | — | — |
| 73 | BankAccountReconRulesetId | RECON_RULESET_ID | — | — |
| 74 | BankAccountReconStartDate | RECON_START_DATE | — | — |
| 75 | BankAccountRequestId | REQUEST_ID | — | — |
| 76 | BankAccountSecondaryAccountReference | SECONDARY_ACCOUNT_REFERENCE | — | — |
| 77 | BankAccountShortAccountName | SHORT_ACCOUNT_NAME | — | — |
| 78 | BankAccountStartDate | START_DATE | — | — |
| 79 | BankAccountXtrBankAccountReference | XTR_BANK_ACCOUNT_REFERENCE | — | — |
| 80 | BankAccountXtrUseAllowedFlag | XTR_USE_ALLOWED_FLAG | — | — |
| 81 | BankAccountZeroAmountAllowed | ZERO_AMOUNT_ALLOWED | — | — |

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

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 2 | LedgersLedgerId | LEDGER_ID | — | — |
| 3 | LedgersObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgUnitTransEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | OrgUnitTransEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | OrgUnitTransLanguage | LANGUAGE | — | — |
| 4 | OrgUnitTransName | NAME | — | — |
| 5 | OrgUnitTransOrganizationId | ORGANIZATION_ID | — | — |
| 6 | OrgUnitTransSourceLang | SOURCE_LANG | — | — |
| 7 | OrganizationUnitEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | OrganizationUnitEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | OrganizationUnitLanguage | LANGUAGE | — | — |
| 10 | OrganizationUnitName1 | NAME | — | ✅ |
| 11 | OrganizationUnitNonRevEffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 12 | OrganizationUnitNonRevEffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 13 | OrganizationUnitNonRevLanguage | LANGUAGE | — | — |
| 14 | OrganizationUnitNonRevName | NAME | — | ✅ |
| 15 | OrganizationUnitNonRevObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | OrganizationUnitNonRevOrganizationId1 | ORGANIZATION_ID | — | — |
| 17 | OrganizationUnitObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | OrganizationUnitOrganizationId | ORGANIZATION_ID | — | — |

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
| 32 | PayingCustAcctAccountName | ACCOUNT_NAME | — | ✅ |
| 33 | PayingCustAcctCustAccountId | CUST_ACCOUNT_ID | — | — |
| 34 | PayingCustAcctPartyId | PARTY_ID | — | — |
| 35 | ShipToCustAcctAccountName | ACCOUNT_NAME | — | ✅ |
| 36 | ShipToCustAcctCustAccountId | CUST_ACCOUNT_ID | — | — |
| 37 | ShipToCustAcctPartyId | PARTY_ID | — | — |
| 38 | SoldToCustAcctAccountName | ACCOUNT_NAME | — | ✅ |
| 39 | SoldToCustAcctCustAccountId | CUST_ACCOUNT_ID | — | — |
| 40 | SoldToCustAcctPartyId | PARTY_ID | — | — |

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
| 7 | ShipToAddrSiteCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 8 | ShipToAddrSiteLanguage | ACCT_SITE_LANGUAGE | — | — |
| 9 | ShipToAddrSitePartySiteId | PARTY_SITE_ID | — | — |
| 10 | ShipToSiteCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 11 | ShipToSiteLanguage | ACCT_SITE_LANGUAGE | — | — |
| 12 | ShipToSitePartySiteId | PARTY_SITE_ID | — | — |
| 13 | SoldToSiteCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 14 | SoldToSiteLanguage | ACCT_SITE_LANGUAGE | — | — |
| 15 | SoldToSitePartySiteId | PARTY_SITE_ID | — | — |

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
| 10 | ResourceSalesrepPartyEmailAddress | EMAIL_ADDRESS | — | — |
| 11 | ResourceSalesrepPartyPartyId | PARTY_ID | — | — |
| 12 | ResourceSalesrepPartyPartyName | PARTY_NAME | — | ✅ |
| 13 | ResourceSalesrepPartyPartyNumber | PARTY_NUMBER | — | — |
| 14 | ResourceSalesrepPartyPartyType | PARTY_TYPE | — | — |
| 15 | ResourceSalesrepPartyPersonFirstName | PERSON_FIRST_NAME | — | — |
| 16 | ResourceSalesrepPartyPersonLastName | PERSON_LAST_NAME | — | — |
| 17 | ResourceSalesrepPartyPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 18 | ResourceSalesrepPartyPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 19 | ResourceSalesrepPartyPersonTitle | PERSON_TITLE | — | — |
| 20 | ResourceSalesrepPartyPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | — |
| 21 | ShipToContactPartyPartyId | PARTY_ID | — | — |
| 22 | ShipToContactPartyPartyName | PARTY_NAME | — | ✅ |
| 23 | ShipToContactPartyPartyNumber | PARTY_NUMBER | — | — |
| 24 | ShipToContactPartyPartyType | PARTY_TYPE | — | — |
| 25 | ShipToContactPartyPersonFirstName | PERSON_FIRST_NAME | — | — |
| 26 | ShipToContactPartyPersonLastName | PERSON_LAST_NAME | — | — |
| 27 | ShipToContactPartyPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 28 | ShipToContactPartyPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 29 | ShipToContactPartyPersonTitle | PERSON_TITLE | — | — |
| 30 | SoldToContactPartyPartyId | PARTY_ID | — | — |
| 31 | SoldToContactPartyPartyName | PARTY_NAME | — | ✅ |
| 32 | SoldToContactPartyPartyNumber | PARTY_NUMBER | — | — |
| 33 | SoldToContactPartyPartyType | PARTY_TYPE | — | — |
| 34 | SoldToContactPartyPersonFirstName | PERSON_FIRST_NAME | — | — |
| 35 | SoldToContactPartyPersonLastName | PERSON_LAST_NAME | — | — |
| 36 | SoldToContactPartyPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 37 | SoldToContactPartyPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 38 | SoldToContactPartyPersonTitle | PERSON_TITLE | — | — |

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

### [[jtf_rs_salesreps|JTF_RS_SALESREPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResourceSalesrepResourceId | RESOURCE_ID | — | — |
| 2 | ResourceSalesrepResourceSalesrepId | RESOURCE_SALESREP_ID | — | — |

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
| 7 | SoldToPartyId | SOLD_TO_PARTY_ID | — | — |
| 8 | TransactionHeaderBRAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 9 | TransactionHeaderBRAgreementId | AGREEMENT_ID | — | — |
| 10 | TransactionHeaderBRApplicationId | APPLICATION_ID | — | — |
| 11 | TransactionHeaderBRApprovalCode | APPROVAL_CODE | — | — |
| 12 | TransactionHeaderBRAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 13 | TransactionHeaderBRBatchId | BATCH_ID | — | — |
| 14 | TransactionHeaderBRBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 15 | TransactionHeaderBRBillTemplateId | BILL_TEMPLATE_ID | — | — |
| 16 | TransactionHeaderBRBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 17 | TransactionHeaderBRBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 18 | TransactionHeaderBRBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 19 | TransactionHeaderBRBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 20 | TransactionHeaderBRBillingDate | BILLING_DATE | — | — |
| 21 | TransactionHeaderBRBrAmount | BR_AMOUNT | — | — |
| 22 | TransactionHeaderBRBrOnHoldFlag | BR_ON_HOLD_FLAG | — | — |
| 23 | TransactionHeaderBRBrUnpaidFlag | BR_UNPAID_FLAG | — | — |
| 24 | TransactionHeaderBRCcErrorCode | CC_ERROR_CODE | — | — |
| 25 | TransactionHeaderBRCcErrorFlag | CC_ERROR_FLAG | — | — |
| 26 | TransactionHeaderBRCcErrorText | CC_ERROR_TEXT | — | — |
| 27 | TransactionHeaderBRCompleteFlag | COMPLETE_FLAG | — | — |
| 28 | TransactionHeaderBRContractId | CONTRACT_ID | — | — |
| 29 | TransactionHeaderBRCreatedBy | CREATED_BY | — | — |
| 30 | TransactionHeaderBRCreatedFrom | CREATED_FROM | — | — |
| 31 | TransactionHeaderBRCreationDate | CREATION_DATE | — | — |
| 32 | TransactionHeaderBRCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | — |
| 33 | TransactionHeaderBRCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | — |
| 34 | TransactionHeaderBRCtReference | CT_REFERENCE | — | — |
| 35 | TransactionHeaderBRCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 36 | TransactionHeaderBRCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 37 | TransactionHeaderBRCustomerReference | CUSTOMER_REFERENCE | — | — |
| 38 | TransactionHeaderBRCustomerReferenceDate | CUSTOMER_REFERENCE_DATE | — | — |
| 39 | TransactionHeaderBRCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 40 | TransactionHeaderBRDefaultTaxExemptFlag | DEFAULT_TAX_EXEMPT_FLAG | — | — |
| 41 | TransactionHeaderBRDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 42 | TransactionHeaderBRDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 43 | TransactionHeaderBRDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 44 | TransactionHeaderBRDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 45 | TransactionHeaderBRDraweeBankAccountId | DRAWEE_BANK_ACCOUNT_ID | — | — |
| 46 | TransactionHeaderBRDraweeContactId | DRAWEE_CONTACT_ID | — | — |
| 47 | TransactionHeaderBRDraweeId | DRAWEE_ID | — | — |
| 48 | TransactionHeaderBRDraweeSiteUseId | DRAWEE_SITE_USE_ID | — | — |
| 49 | TransactionHeaderBREdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 50 | TransactionHeaderBREdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 51 | TransactionHeaderBREndDateCommitment | END_DATE_COMMITMENT | — | — |
| 52 | TransactionHeaderBRExchangeDate | EXCHANGE_DATE | — | — |
| 53 | TransactionHeaderBRExchangeRate | EXCHANGE_RATE | — | — |
| 54 | TransactionHeaderBRExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 55 | TransactionHeaderBRFinanceCharges | FINANCE_CHARGES | — | — |
| 56 | TransactionHeaderBRFobPoint | FOB_POINT | — | — |
| 57 | TransactionHeaderBRInitialCustomerTrxId | INITIAL_CUSTOMER_TRX_ID | — | — |
| 58 | TransactionHeaderBRIntercompanyFlag | INTERCOMPANY_FLAG | — | — |
| 59 | TransactionHeaderBRInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 60 | TransactionHeaderBRInterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | — |
| 61 | TransactionHeaderBRInterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | — |
| 62 | TransactionHeaderBRInterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | — |
| 63 | TransactionHeaderBRInterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | — |
| 64 | TransactionHeaderBRInterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | — |
| 65 | TransactionHeaderBRInterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | — |
| 66 | TransactionHeaderBRInterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | — |
| 67 | TransactionHeaderBRInterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | — |
| 68 | TransactionHeaderBRInterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | — |
| 69 | TransactionHeaderBRInterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | — |
| 70 | TransactionHeaderBRInterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | — |
| 71 | TransactionHeaderBRInterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | — |
| 72 | TransactionHeaderBRInterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | — |
| 73 | TransactionHeaderBRInterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | — |
| 74 | TransactionHeaderBRInterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | — |
| 75 | TransactionHeaderBRInterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | — |
| 76 | TransactionHeaderBRInternalNotes | INTERNAL_NOTES | — | — |
| 77 | TransactionHeaderBRInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 78 | TransactionHeaderBRInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 79 | TransactionHeaderBRLastPrintedSequenceNum | LAST_PRINTED_SEQUENCE_NUM | — | — |
| 80 | TransactionHeaderBRLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 81 | TransactionHeaderBRLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 82 | TransactionHeaderBRLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 83 | TransactionHeaderBRLateChargesAssessed | LATE_CHARGES_ASSESSED | — | — |
| 84 | TransactionHeaderBRLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 85 | TransactionHeaderBRObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 86 | TransactionHeaderBROldTrxNumber | OLD_TRX_NUMBER | — | — |
| 87 | TransactionHeaderBROrgId | ORG_ID | — | — |
| 88 | TransactionHeaderBROrigSystemBatchName | ORIG_SYSTEM_BATCH_NAME | — | — |
| 89 | TransactionHeaderBROverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 90 | TransactionHeaderBRPayingCustomerId | PAYING_CUSTOMER_ID | — | — |
| 91 | TransactionHeaderBRPayingSiteUseId | PAYING_SITE_USE_ID | — | — |
| 92 | TransactionHeaderBRPaymentAttributes | PAYMENT_ATTRIBUTES | — | — |
| 93 | TransactionHeaderBRPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 94 | TransactionHeaderBRPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 95 | TransactionHeaderBRPostRequestId | POST_REQUEST_ID | — | — |
| 96 | TransactionHeaderBRPostingControlId | POSTING_CONTROL_ID | — | — |
| 97 | TransactionHeaderBRPrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 98 | TransactionHeaderBRPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 99 | TransactionHeaderBRPrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | — |
| 100 | TransactionHeaderBRPrintingCount | PRINTING_COUNT | — | — |
| 101 | TransactionHeaderBRPrintingLastPrinted | PRINTING_LAST_PRINTED | — | — |
| 102 | TransactionHeaderBRPrintingOption | PRINTING_OPTION | — | — |
| 103 | TransactionHeaderBRPrintingOriginalDate | PRINTING_ORIGINAL_DATE | — | — |
| 104 | TransactionHeaderBRPrintingPending | PRINTING_PENDING | — | — |
| 105 | TransactionHeaderBRProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 106 | TransactionHeaderBRProgramId | PROGRAM_ID | — | — |
| 107 | TransactionHeaderBRProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 108 | TransactionHeaderBRPurchaseOrder | PURCHASE_ORDER | — | — |
| 109 | TransactionHeaderBRPurchaseOrderDate | PURCHASE_ORDER_DATE | — | — |
| 110 | TransactionHeaderBRPurchaseOrderRevision | PURCHASE_ORDER_REVISION | — | — |
| 111 | TransactionHeaderBRRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 112 | TransactionHeaderBRReasonCode | REASON_CODE | — | — |
| 113 | TransactionHeaderBRReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 114 | TransactionHeaderBRRecurredFromTrxNumber | RECURRED_FROM_TRX_NUMBER | — | — |
| 115 | TransactionHeaderBRRelatedBatchSourceSeqId | RELATED_BATCH_SOURCE_SEQ_ID | — | — |
| 116 | TransactionHeaderBRRelatedCustomerTrxId | RELATED_CUSTOMER_TRX_ID | — | — |
| 117 | TransactionHeaderBRRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 118 | TransactionHeaderBRRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 119 | TransactionHeaderBRRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 120 | TransactionHeaderBRRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 121 | TransactionHeaderBRRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 122 | TransactionHeaderBRRequestId | REQUEST_ID | — | — |
| 123 | TransactionHeaderBRReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 124 | TransactionHeaderBRSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 125 | TransactionHeaderBRShipDateActual | SHIP_DATE_ACTUAL | — | — |
| 126 | TransactionHeaderBRShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 127 | TransactionHeaderBRShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 128 | TransactionHeaderBRShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 129 | TransactionHeaderBRShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 130 | TransactionHeaderBRShipVia | SHIP_VIA | — | — |
| 131 | TransactionHeaderBRShipmentId | SHIPMENT_ID | — | — |
| 132 | TransactionHeaderBRSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 133 | TransactionHeaderBRSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 134 | TransactionHeaderBRSoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | — |
| 135 | TransactionHeaderBRSourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 136 | TransactionHeaderBRSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 137 | TransactionHeaderBRSpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 138 | TransactionHeaderBRStartDateCommitment | START_DATE_COMMITMENT | — | — |
| 139 | TransactionHeaderBRStatusTrx | STATUS_TRX | — | — |
| 140 | TransactionHeaderBRTermDueDate | TERM_DUE_DATE | — | — |
| 141 | TransactionHeaderBRTermId | TERM_ID | — | — |
| 142 | TransactionHeaderBRTerritoryId | TERRITORY_ID | — | — |
| 143 | TransactionHeaderBRTrxClass | TRX_CLASS | — | — |
| 144 | TransactionHeaderBRTrxDate | TRX_DATE | — | — |
| 145 | TransactionHeaderBRTrxNumber | TRX_NUMBER | — | — |
| 146 | TransactionHeaderBRUpgradeMethod | UPGRADE_METHOD | — | — |
| 147 | TransactionHeaderBRWaybillNumber | WAYBILL_NUMBER | — | — |
| 148 | TransactionHeaderBRWhUpdateDate | WH_UPDATE_DATE | — | — |
| 149 | TransactionHeaderDistAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 150 | TransactionHeaderDistAgreementId | AGREEMENT_ID | — | — |
| 151 | TransactionHeaderDistApplicationId | APPLICATION_ID | — | — |
| 152 | TransactionHeaderDistApprovalCode | APPROVAL_CODE | — | — |
| 153 | TransactionHeaderDistAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 154 | TransactionHeaderDistBatchId | BATCH_ID | — | — |
| 155 | TransactionHeaderDistBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 156 | TransactionHeaderDistBillTemplateId | BILL_TEMPLATE_ID | — | — |
| 157 | TransactionHeaderDistBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 158 | TransactionHeaderDistBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 159 | TransactionHeaderDistBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 160 | TransactionHeaderDistBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 161 | TransactionHeaderDistBillingDate | BILLING_DATE | — | ✅ |
| 162 | TransactionHeaderDistBrAmount | BR_AMOUNT | — | — |
| 163 | TransactionHeaderDistBrOnHoldFlag | BR_ON_HOLD_FLAG | — | — |
| 164 | TransactionHeaderDistBrUnpaidFlag | BR_UNPAID_FLAG | — | — |
| 165 | TransactionHeaderDistCcErrorCode | CC_ERROR_CODE | — | — |
| 166 | TransactionHeaderDistCcErrorFlag | CC_ERROR_FLAG | — | — |
| 167 | TransactionHeaderDistCcErrorText | CC_ERROR_TEXT | — | — |
| 168 | TransactionHeaderDistComments | COMMENTS | — | ✅ |
| 169 | TransactionHeaderDistCompleteFlag | COMPLETE_FLAG | — | ✅ |
| 170 | TransactionHeaderDistContractId | CONTRACT_ID | — | — |
| 171 | TransactionHeaderDistCreatedBy | CREATED_BY | — | ✅ |
| 172 | TransactionHeaderDistCreatedFrom | CREATED_FROM | — | ✅ |
| 173 | TransactionHeaderDistCreationDate | CREATION_DATE | — | ✅ |
| 174 | TransactionHeaderDistCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | ✅ |
| 175 | TransactionHeaderDistCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | ✅ |
| 176 | TransactionHeaderDistCtReference | CT_REFERENCE | — | ✅ |
| 177 | TransactionHeaderDistCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 178 | TransactionHeaderDistCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 179 | TransactionHeaderDistCustomerReference | CUSTOMER_REFERENCE | — | ✅ |
| 180 | TransactionHeaderDistCustomerReferenceDate | CUSTOMER_REFERENCE_DATE | — | ✅ |
| 181 | TransactionHeaderDistCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 182 | TransactionHeaderDistDefaultTaxExemptFlag | DEFAULT_TAX_EXEMPT_FLAG | — | ✅ |
| 183 | TransactionHeaderDistDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | ✅ |
| 184 | TransactionHeaderDistDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 185 | TransactionHeaderDistDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 186 | TransactionHeaderDistDelContactEmailAddress | DEL_CONTACT_EMAIL_ADDRESS | — | — |
| 187 | TransactionHeaderDistDeliveryMethodCode | DELIVERY_METHOD_CODE | — | — |
| 188 | TransactionHeaderDistDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 189 | TransactionHeaderDistDocSequenceValue | DOC_SEQUENCE_VALUE | — | ✅ |
| 190 | TransactionHeaderDistDocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 191 | TransactionHeaderDistDraweeBankAccountId | DRAWEE_BANK_ACCOUNT_ID | — | — |
| 192 | TransactionHeaderDistDraweeContactId | DRAWEE_CONTACT_ID | — | — |
| 193 | TransactionHeaderDistDraweeId | DRAWEE_ID | — | — |
| 194 | TransactionHeaderDistDraweeSiteUseId | DRAWEE_SITE_USE_ID | — | — |
| 195 | TransactionHeaderDistEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 196 | TransactionHeaderDistEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 197 | TransactionHeaderDistEndDateCommitment | END_DATE_COMMITMENT | — | ✅ |
| 198 | TransactionHeaderDistExchangeDate | EXCHANGE_DATE | — | ✅ |
| 199 | TransactionHeaderDistExchangeRate | EXCHANGE_RATE | — | ✅ |
| 200 | TransactionHeaderDistExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 201 | TransactionHeaderDistFinanceCharges | FINANCE_CHARGES | — | ✅ |
| 202 | TransactionHeaderDistFobPoint | FOB_POINT | — | ✅ |
| 203 | TransactionHeaderDistInitialCustomerTrxId | INITIAL_CUSTOMER_TRX_ID | — | — |
| 204 | TransactionHeaderDistIntercompanyFlag | INTERCOMPANY_FLAG | — | ✅ |
| 205 | TransactionHeaderDistInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 206 | TransactionHeaderDistInterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | ✅ |
| 207 | TransactionHeaderDistInterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | ✅ |
| 208 | TransactionHeaderDistInterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | ✅ |
| 209 | TransactionHeaderDistInterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | ✅ |
| 210 | TransactionHeaderDistInterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | ✅ |
| 211 | TransactionHeaderDistInterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | ✅ |
| 212 | TransactionHeaderDistInterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | ✅ |
| 213 | TransactionHeaderDistInterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | ✅ |
| 214 | TransactionHeaderDistInterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | ✅ |
| 215 | TransactionHeaderDistInterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | ✅ |
| 216 | TransactionHeaderDistInterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | ✅ |
| 217 | TransactionHeaderDistInterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | ✅ |
| 218 | TransactionHeaderDistInterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | ✅ |
| 219 | TransactionHeaderDistInterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | ✅ |
| 220 | TransactionHeaderDistInterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | ✅ |
| 221 | TransactionHeaderDistInterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | ✅ |
| 222 | TransactionHeaderDistInternalNotes | INTERNAL_NOTES | — | ✅ |
| 223 | TransactionHeaderDistInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 224 | TransactionHeaderDistInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 225 | TransactionHeaderDistLastPrintedSequenceNum | LAST_PRINTED_SEQUENCE_NUM | — | ✅ |
| 226 | TransactionHeaderDistLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 227 | TransactionHeaderDistLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 228 | TransactionHeaderDistLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 229 | TransactionHeaderDistLateChargesAssessed | LATE_CHARGES_ASSESSED | — | ✅ |
| 230 | TransactionHeaderDistLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 231 | TransactionHeaderDistObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 232 | TransactionHeaderDistOldTrxNumber | OLD_TRX_NUMBER | — | — |
| 233 | TransactionHeaderDistOrgId | ORG_ID | — | — |
| 234 | TransactionHeaderDistOrigSystemBatchName | ORIG_SYSTEM_BATCH_NAME | — | ✅ |
| 235 | TransactionHeaderDistOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 236 | TransactionHeaderDistPayingCustomerId | PAYING_CUSTOMER_ID | — | — |
| 237 | TransactionHeaderDistPayingSiteUseId | PAYING_SITE_USE_ID | — | — |
| 238 | TransactionHeaderDistPaymentAttributes | PAYMENT_ATTRIBUTES | — | — |
| 239 | TransactionHeaderDistPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 240 | TransactionHeaderDistPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 241 | TransactionHeaderDistPostRequestId | POST_REQUEST_ID | — | — |
| 242 | TransactionHeaderDistPostingControlId | POSTING_CONTROL_ID | — | — |
| 243 | TransactionHeaderDistPrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 244 | TransactionHeaderDistPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 245 | TransactionHeaderDistPrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | — |
| 246 | TransactionHeaderDistPrintingCount | PRINTING_COUNT | — | ✅ |
| 247 | TransactionHeaderDistPrintingLastPrinted | PRINTING_LAST_PRINTED | — | — |
| 248 | TransactionHeaderDistPrintingOption | PRINTING_OPTION | — | ✅ |
| 249 | TransactionHeaderDistPrintingOriginalDate | PRINTING_ORIGINAL_DATE | — | ✅ |
| 250 | TransactionHeaderDistPrintingPending | PRINTING_PENDING | — | ✅ |
| 251 | TransactionHeaderDistProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 252 | TransactionHeaderDistProgramId | PROGRAM_ID | — | — |
| 253 | TransactionHeaderDistProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 254 | TransactionHeaderDistPurchaseOrder | PURCHASE_ORDER | — | ✅ |
| 255 | TransactionHeaderDistPurchaseOrderDate | PURCHASE_ORDER_DATE | — | ✅ |
| 256 | TransactionHeaderDistPurchaseOrderRevision | PURCHASE_ORDER_REVISION | — | ✅ |
| 257 | TransactionHeaderDistRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 258 | TransactionHeaderDistReasonCode | REASON_CODE | — | ✅ |
| 259 | TransactionHeaderDistReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 260 | TransactionHeaderDistRecurredFromTrxNumber | RECURRED_FROM_TRX_NUMBER | — | — |
| 261 | TransactionHeaderDistRelatedBatchSourceSeqId | RELATED_BATCH_SOURCE_SEQ_ID | — | — |
| 262 | TransactionHeaderDistRelatedCustomerTrxId | RELATED_CUSTOMER_TRX_ID | — | — |
| 263 | TransactionHeaderDistRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 264 | TransactionHeaderDistRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 265 | TransactionHeaderDistRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 266 | TransactionHeaderDistRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 267 | TransactionHeaderDistRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 268 | TransactionHeaderDistRequestId | REQUEST_ID | — | — |
| 269 | TransactionHeaderDistRequiresManualScheduling | REQUIRES_MANUAL_SCHEDULING | — | ✅ |
| 270 | TransactionHeaderDistRevRecApplication | REV_REC_APPLICATION | — | ✅ |
| 271 | TransactionHeaderDistReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 272 | TransactionHeaderDistSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 273 | TransactionHeaderDistShipDateActual | SHIP_DATE_ACTUAL | — | ✅ |
| 274 | TransactionHeaderDistShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 275 | TransactionHeaderDistShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 276 | TransactionHeaderDistShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 277 | TransactionHeaderDistShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 278 | TransactionHeaderDistShipVia | SHIP_VIA | — | ✅ |
| 279 | TransactionHeaderDistShipmentId | SHIPMENT_ID | — | — |
| 280 | TransactionHeaderDistSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 281 | TransactionHeaderDistSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 282 | TransactionHeaderDistSoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | — |
| 283 | TransactionHeaderDistSourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 284 | TransactionHeaderDistSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 285 | TransactionHeaderDistSpecialInstructions | SPECIAL_INSTRUCTIONS | — | ✅ |
| 286 | TransactionHeaderDistStartDateCommitment | START_DATE_COMMITMENT | — | ✅ |
| 287 | TransactionHeaderDistStatusTrx | STATUS_TRX | — | ✅ |
| 288 | TransactionHeaderDistTermDueDate | TERM_DUE_DATE | — | ✅ |
| 289 | TransactionHeaderDistTermId | TERM_ID | — | — |
| 290 | TransactionHeaderDistTerritoryId | TERRITORY_ID | — | — |
| 291 | TransactionHeaderDistTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 292 | TransactionHeaderDistTrxClass | TRX_CLASS | — | ✅ |
| 293 | TransactionHeaderDistTrxDate | TRX_DATE | — | ✅ |
| 294 | TransactionHeaderDistTrxNumber | TRX_NUMBER | — | ✅ |
| 295 | TransactionHeaderDistUpgradeMethod | UPGRADE_METHOD | — | — |
| 296 | TransactionHeaderDistUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | ✅ |
| 297 | TransactionHeaderDistWaybillNumber | WAYBILL_NUMBER | — | ✅ |
| 298 | TransactionHeaderDistWhUpdateDate | WH_UPDATE_DATE | — | — |
| 299 | TransactionHeaderLineAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 300 | TransactionHeaderLineAgreementId | AGREEMENT_ID | — | — |
| 301 | TransactionHeaderLineApplicationId | APPLICATION_ID | — | — |
| 302 | TransactionHeaderLineApprovalCode | APPROVAL_CODE | — | — |
| 303 | TransactionHeaderLineAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 304 | TransactionHeaderLineBatchId | BATCH_ID | — | — |
| 305 | TransactionHeaderLineBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 306 | TransactionHeaderLineBillTemplateId | BILL_TEMPLATE_ID | — | ✅ |
| 307 | TransactionHeaderLineBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 308 | TransactionHeaderLineBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 309 | TransactionHeaderLineBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 310 | TransactionHeaderLineBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 311 | TransactionHeaderLineBillingDate | BILLING_DATE | — | — |
| 312 | TransactionHeaderLineBrAmount | BR_AMOUNT | — | — |
| 313 | TransactionHeaderLineBrOnHoldFlag | BR_ON_HOLD_FLAG | — | — |
| 314 | TransactionHeaderLineBrUnpaidFlag | BR_UNPAID_FLAG | — | — |
| 315 | TransactionHeaderLineCcErrorCode | CC_ERROR_CODE | — | — |
| 316 | TransactionHeaderLineCcErrorFlag | CC_ERROR_FLAG | — | — |
| 317 | TransactionHeaderLineCcErrorText | CC_ERROR_TEXT | — | — |
| 318 | TransactionHeaderLineComments | COMMENTS | — | — |
| 319 | TransactionHeaderLineCompleteFlag | COMPLETE_FLAG | — | — |
| 320 | TransactionHeaderLineContractId | CONTRACT_ID | — | — |
| 321 | TransactionHeaderLineCreatedBy | CREATED_BY | — | — |
| 322 | TransactionHeaderLineCreatedFrom | CREATED_FROM | — | — |
| 323 | TransactionHeaderLineCreationDate | CREATION_DATE | — | — |
| 324 | TransactionHeaderLineCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | — |
| 325 | TransactionHeaderLineCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | — |
| 326 | TransactionHeaderLineCtReference | CT_REFERENCE | — | — |
| 327 | TransactionHeaderLineCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 328 | TransactionHeaderLineCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 329 | TransactionHeaderLineCustomerReference | CUSTOMER_REFERENCE | — | — |
| 330 | TransactionHeaderLineCustomerReferenceDate | CUSTOMER_REFERENCE_DATE | — | — |
| 331 | TransactionHeaderLineCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 332 | TransactionHeaderLineDefaultTaxExemptFlag | DEFAULT_TAX_EXEMPT_FLAG | — | — |
| 333 | TransactionHeaderLineDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 334 | TransactionHeaderLineDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 335 | TransactionHeaderLineDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 336 | TransactionHeaderLineDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 337 | TransactionHeaderLineDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 338 | TransactionHeaderLineDocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 339 | TransactionHeaderLineDraweeBankAccountId | DRAWEE_BANK_ACCOUNT_ID | — | — |
| 340 | TransactionHeaderLineDraweeContactId | DRAWEE_CONTACT_ID | — | — |
| 341 | TransactionHeaderLineDraweeId | DRAWEE_ID | — | — |
| 342 | TransactionHeaderLineDraweeSiteUseId | DRAWEE_SITE_USE_ID | — | — |
| 343 | TransactionHeaderLineEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 344 | TransactionHeaderLineEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 345 | TransactionHeaderLineEndDateCommitment | END_DATE_COMMITMENT | — | — |
| 346 | TransactionHeaderLineExchangeDate | EXCHANGE_DATE | — | — |
| 347 | TransactionHeaderLineExchangeRate | EXCHANGE_RATE | — | — |
| 348 | TransactionHeaderLineExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 349 | TransactionHeaderLineFinanceCharges | FINANCE_CHARGES | — | — |
| 350 | TransactionHeaderLineFobPoint | FOB_POINT | — | — |
| 351 | TransactionHeaderLineInitialCustomerTrxId | INITIAL_CUSTOMER_TRX_ID | — | — |
| 352 | TransactionHeaderLineIntercompanyFlag | INTERCOMPANY_FLAG | — | — |
| 353 | TransactionHeaderLineInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 354 | TransactionHeaderLineInterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | — |
| 355 | TransactionHeaderLineInterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | — |
| 356 | TransactionHeaderLineInterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | — |
| 357 | TransactionHeaderLineInterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | — |
| 358 | TransactionHeaderLineInterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | — |
| 359 | TransactionHeaderLineInterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | — |
| 360 | TransactionHeaderLineInterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | — |
| 361 | TransactionHeaderLineInterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | — |
| 362 | TransactionHeaderLineInterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | — |
| 363 | TransactionHeaderLineInterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | — |
| 364 | TransactionHeaderLineInterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | — |
| 365 | TransactionHeaderLineInterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | — |
| 366 | TransactionHeaderLineInterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | — |
| 367 | TransactionHeaderLineInterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | — |
| 368 | TransactionHeaderLineInterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | — |
| 369 | TransactionHeaderLineInterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | — |
| 370 | TransactionHeaderLineInternalNotes | INTERNAL_NOTES | — | — |
| 371 | TransactionHeaderLineInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 372 | TransactionHeaderLineInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 373 | TransactionHeaderLineLastPrintedSequenceNum | LAST_PRINTED_SEQUENCE_NUM | — | — |
| 374 | TransactionHeaderLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 375 | TransactionHeaderLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 376 | TransactionHeaderLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 377 | TransactionHeaderLineLateChargesAssessed | LATE_CHARGES_ASSESSED | — | — |
| 378 | TransactionHeaderLineLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 379 | TransactionHeaderLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 380 | TransactionHeaderLineOldTrxNumber | OLD_TRX_NUMBER | — | — |
| 381 | TransactionHeaderLineOrgId | ORG_ID | — | — |
| 382 | TransactionHeaderLineOrigSystemBatchName | ORIG_SYSTEM_BATCH_NAME | — | — |
| 383 | TransactionHeaderLineOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 384 | TransactionHeaderLinePayingCustomerId | PAYING_CUSTOMER_ID | — | — |
| 385 | TransactionHeaderLinePayingSiteUseId | PAYING_SITE_USE_ID | — | — |
| 386 | TransactionHeaderLinePaymentAttributes | PAYMENT_ATTRIBUTES | — | — |
| 387 | TransactionHeaderLinePaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 388 | TransactionHeaderLinePaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 389 | TransactionHeaderLinePostRequestId | POST_REQUEST_ID | — | — |
| 390 | TransactionHeaderLinePostingControlId | POSTING_CONTROL_ID | — | — |
| 391 | TransactionHeaderLinePrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 392 | TransactionHeaderLinePreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 393 | TransactionHeaderLinePrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | — |
| 394 | TransactionHeaderLinePrintingCount | PRINTING_COUNT | — | — |
| 395 | TransactionHeaderLinePrintingLastPrinted | PRINTING_LAST_PRINTED | — | — |
| 396 | TransactionHeaderLinePrintingOption | PRINTING_OPTION | — | — |
| 397 | TransactionHeaderLinePrintingOriginalDate | PRINTING_ORIGINAL_DATE | — | — |
| 398 | TransactionHeaderLinePrintingPending | PRINTING_PENDING | — | — |
| 399 | TransactionHeaderLineProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 400 | TransactionHeaderLineProgramId | PROGRAM_ID | — | — |
| 401 | TransactionHeaderLineProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 402 | TransactionHeaderLinePurchaseOrder | PURCHASE_ORDER | — | — |
| 403 | TransactionHeaderLinePurchaseOrderDate | PURCHASE_ORDER_DATE | — | — |
| 404 | TransactionHeaderLinePurchaseOrderRevision | PURCHASE_ORDER_REVISION | — | — |
| 405 | TransactionHeaderLineRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 406 | TransactionHeaderLineReasonCode | REASON_CODE | — | — |
| 407 | TransactionHeaderLineReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 408 | TransactionHeaderLineRecurredFromTrxNumber | RECURRED_FROM_TRX_NUMBER | — | — |
| 409 | TransactionHeaderLineRelatedBatchSourceSeqId | RELATED_BATCH_SOURCE_SEQ_ID | — | — |
| 410 | TransactionHeaderLineRelatedCustomerTrxId | RELATED_CUSTOMER_TRX_ID | — | — |
| 411 | TransactionHeaderLineRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 412 | TransactionHeaderLineRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 413 | TransactionHeaderLineRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 414 | TransactionHeaderLineRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 415 | TransactionHeaderLineRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 416 | TransactionHeaderLineRequestId | REQUEST_ID | — | — |
| 417 | TransactionHeaderLineRequiresManualScheduling | REQUIRES_MANUAL_SCHEDULING | — | — |
| 418 | TransactionHeaderLineReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 419 | TransactionHeaderLineSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 420 | TransactionHeaderLineShipDateActual | SHIP_DATE_ACTUAL | — | — |
| 421 | TransactionHeaderLineShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 422 | TransactionHeaderLineShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 423 | TransactionHeaderLineShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 424 | TransactionHeaderLineShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 425 | TransactionHeaderLineShipVia | SHIP_VIA | — | — |
| 426 | TransactionHeaderLineShipmentId | SHIPMENT_ID | — | — |
| 427 | TransactionHeaderLineSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 428 | TransactionHeaderLineSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 429 | TransactionHeaderLineSoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | — |
| 430 | TransactionHeaderLineSourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 431 | TransactionHeaderLineSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 432 | TransactionHeaderLineSpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 433 | TransactionHeaderLineStartDateCommitment | START_DATE_COMMITMENT | — | — |
| 434 | TransactionHeaderLineStatusTrx | STATUS_TRX | — | — |
| 435 | TransactionHeaderLineTermDueDate | TERM_DUE_DATE | — | — |
| 436 | TransactionHeaderLineTermId | TERM_ID | — | — |
| 437 | TransactionHeaderLineTerritoryId | TERRITORY_ID | — | — |
| 438 | TransactionHeaderLineTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 439 | TransactionHeaderLineTrxClass | TRX_CLASS | — | — |
| 440 | TransactionHeaderLineTrxDate | TRX_DATE | — | — |
| 441 | TransactionHeaderLineTrxNumber | TRX_NUMBER | — | — |
| 442 | TransactionHeaderLineUpgradeMethod | UPGRADE_METHOD | — | — |
| 443 | TransactionHeaderLineUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 444 | TransactionHeaderLineWaybillNumber | WAYBILL_NUMBER | — | — |
| 445 | TransactionHeaderLineWhUpdateDate | WH_UPDATE_DATE | — | — |
| 446 | TransactionHeaderPreviousAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 447 | TransactionHeaderPreviousAgreementId | AGREEMENT_ID | — | — |
| 448 | TransactionHeaderPreviousApplicationId | APPLICATION_ID | — | — |
| 449 | TransactionHeaderPreviousApprovalCode | APPROVAL_CODE | — | — |
| 450 | TransactionHeaderPreviousAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 451 | TransactionHeaderPreviousBatchId | BATCH_ID | — | — |
| 452 | TransactionHeaderPreviousBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 453 | TransactionHeaderPreviousBillTemplateId | BILL_TEMPLATE_ID | — | — |
| 454 | TransactionHeaderPreviousBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 455 | TransactionHeaderPreviousBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 456 | TransactionHeaderPreviousBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 457 | TransactionHeaderPreviousBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 458 | TransactionHeaderPreviousBillingDate | BILLING_DATE | — | — |
| 459 | TransactionHeaderPreviousBrAmount | BR_AMOUNT | — | — |
| 460 | TransactionHeaderPreviousBrOnHoldFlag | BR_ON_HOLD_FLAG | — | — |
| 461 | TransactionHeaderPreviousBrUnpaidFlag | BR_UNPAID_FLAG | — | — |
| 462 | TransactionHeaderPreviousCcErrorCode | CC_ERROR_CODE | — | — |
| 463 | TransactionHeaderPreviousCcErrorFlag | CC_ERROR_FLAG | — | — |
| 464 | TransactionHeaderPreviousCcErrorText | CC_ERROR_TEXT | — | — |
| 465 | TransactionHeaderPreviousCompleteFlag | COMPLETE_FLAG | — | — |
| 466 | TransactionHeaderPreviousContractId | CONTRACT_ID | — | — |
| 467 | TransactionHeaderPreviousCreatedBy | CREATED_BY | — | — |
| 468 | TransactionHeaderPreviousCreatedFrom | CREATED_FROM | — | — |
| 469 | TransactionHeaderPreviousCreationDate | CREATION_DATE | — | — |
| 470 | TransactionHeaderPreviousCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | — |
| 471 | TransactionHeaderPreviousCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | — |
| 472 | TransactionHeaderPreviousCtReference | CT_REFERENCE | — | — |
| 473 | TransactionHeaderPreviousCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 474 | TransactionHeaderPreviousCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 475 | TransactionHeaderPreviousCustomerReference | CUSTOMER_REFERENCE | — | — |
| 476 | TransactionHeaderPreviousCustomerReferenceDate | CUSTOMER_REFERENCE_DATE | — | — |
| 477 | TransactionHeaderPreviousCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 478 | TransactionHeaderPreviousDefaultTaxExemptFlag | DEFAULT_TAX_EXEMPT_FLAG | — | — |
| 479 | TransactionHeaderPreviousDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 480 | TransactionHeaderPreviousDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 481 | TransactionHeaderPreviousDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 482 | TransactionHeaderPreviousDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 483 | TransactionHeaderPreviousDraweeBankAccountId | DRAWEE_BANK_ACCOUNT_ID | — | — |
| 484 | TransactionHeaderPreviousDraweeContactId | DRAWEE_CONTACT_ID | — | — |
| 485 | TransactionHeaderPreviousDraweeId | DRAWEE_ID | — | — |
| 486 | TransactionHeaderPreviousDraweeSiteUseId | DRAWEE_SITE_USE_ID | — | — |
| 487 | TransactionHeaderPreviousEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 488 | TransactionHeaderPreviousEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 489 | TransactionHeaderPreviousEndDateCommitment | END_DATE_COMMITMENT | — | — |
| 490 | TransactionHeaderPreviousExchangeDate | EXCHANGE_DATE | — | — |
| 491 | TransactionHeaderPreviousExchangeRate | EXCHANGE_RATE | — | — |
| 492 | TransactionHeaderPreviousExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 493 | TransactionHeaderPreviousFinanceCharges | FINANCE_CHARGES | — | — |
| 494 | TransactionHeaderPreviousFobPoint | FOB_POINT | — | — |
| 495 | TransactionHeaderPreviousInitialCustomerTrxId | INITIAL_CUSTOMER_TRX_ID | — | — |
| 496 | TransactionHeaderPreviousIntercompanyFlag | INTERCOMPANY_FLAG | — | — |
| 497 | TransactionHeaderPreviousInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 498 | TransactionHeaderPreviousInterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | — |
| 499 | TransactionHeaderPreviousInterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | — |
| 500 | TransactionHeaderPreviousInterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | — |
| 501 | TransactionHeaderPreviousInterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | — |
| 502 | TransactionHeaderPreviousInterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | — |
| 503 | TransactionHeaderPreviousInterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | — |
| 504 | TransactionHeaderPreviousInterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | — |
| 505 | TransactionHeaderPreviousInterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | — |
| 506 | TransactionHeaderPreviousInterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | — |
| 507 | TransactionHeaderPreviousInterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | — |
| 508 | TransactionHeaderPreviousInterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | — |
| 509 | TransactionHeaderPreviousInterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | — |
| 510 | TransactionHeaderPreviousInterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | — |
| 511 | TransactionHeaderPreviousInterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | — |
| 512 | TransactionHeaderPreviousInterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | — |
| 513 | TransactionHeaderPreviousInterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | — |
| 514 | TransactionHeaderPreviousInternalNotes | INTERNAL_NOTES | — | — |
| 515 | TransactionHeaderPreviousInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 516 | TransactionHeaderPreviousInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 517 | TransactionHeaderPreviousLastPrintedSequenceNum | LAST_PRINTED_SEQUENCE_NUM | — | — |
| 518 | TransactionHeaderPreviousLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 519 | TransactionHeaderPreviousLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 520 | TransactionHeaderPreviousLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 521 | TransactionHeaderPreviousLateChargesAssessed | LATE_CHARGES_ASSESSED | — | — |
| 522 | TransactionHeaderPreviousLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 523 | TransactionHeaderPreviousObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 524 | TransactionHeaderPreviousOldTrxNumber | OLD_TRX_NUMBER | — | — |
| 525 | TransactionHeaderPreviousOrgId | ORG_ID | — | — |
| 526 | TransactionHeaderPreviousOrigSystemBatchName | ORIG_SYSTEM_BATCH_NAME | — | — |
| 527 | TransactionHeaderPreviousOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 528 | TransactionHeaderPreviousPayingCustomerId | PAYING_CUSTOMER_ID | — | — |
| 529 | TransactionHeaderPreviousPayingSiteUseId | PAYING_SITE_USE_ID | — | — |
| 530 | TransactionHeaderPreviousPaymentAttributes | PAYMENT_ATTRIBUTES | — | — |
| 531 | TransactionHeaderPreviousPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 532 | TransactionHeaderPreviousPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 533 | TransactionHeaderPreviousPostRequestId | POST_REQUEST_ID | — | — |
| 534 | TransactionHeaderPreviousPostingControlId | POSTING_CONTROL_ID | — | — |
| 535 | TransactionHeaderPreviousPrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 536 | TransactionHeaderPreviousPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 537 | TransactionHeaderPreviousPrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | — |
| 538 | TransactionHeaderPreviousPrintingCount | PRINTING_COUNT | — | — |
| 539 | TransactionHeaderPreviousPrintingLastPrinted | PRINTING_LAST_PRINTED | — | — |
| 540 | TransactionHeaderPreviousPrintingOption | PRINTING_OPTION | — | — |
| 541 | TransactionHeaderPreviousPrintingOriginalDate | PRINTING_ORIGINAL_DATE | — | — |
| 542 | TransactionHeaderPreviousPrintingPending | PRINTING_PENDING | — | — |
| 543 | TransactionHeaderPreviousProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 544 | TransactionHeaderPreviousProgramId | PROGRAM_ID | — | — |
| 545 | TransactionHeaderPreviousProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 546 | TransactionHeaderPreviousPurchaseOrder | PURCHASE_ORDER | — | — |
| 547 | TransactionHeaderPreviousPurchaseOrderDate | PURCHASE_ORDER_DATE | — | — |
| 548 | TransactionHeaderPreviousPurchaseOrderRevision | PURCHASE_ORDER_REVISION | — | — |
| 549 | TransactionHeaderPreviousRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 550 | TransactionHeaderPreviousReasonCode | REASON_CODE | — | — |
| 551 | TransactionHeaderPreviousReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 552 | TransactionHeaderPreviousRecurredFromTrxNumber | RECURRED_FROM_TRX_NUMBER | — | — |
| 553 | TransactionHeaderPreviousRelatedBatchSourceSeqId | RELATED_BATCH_SOURCE_SEQ_ID | — | — |
| 554 | TransactionHeaderPreviousRelatedCustomerTrxId | RELATED_CUSTOMER_TRX_ID | — | — |
| 555 | TransactionHeaderPreviousRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 556 | TransactionHeaderPreviousRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 557 | TransactionHeaderPreviousRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 558 | TransactionHeaderPreviousRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 559 | TransactionHeaderPreviousRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 560 | TransactionHeaderPreviousRequestId | REQUEST_ID | — | — |
| 561 | TransactionHeaderPreviousReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 562 | TransactionHeaderPreviousSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 563 | TransactionHeaderPreviousShipDateActual | SHIP_DATE_ACTUAL | — | — |
| 564 | TransactionHeaderPreviousShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 565 | TransactionHeaderPreviousShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 566 | TransactionHeaderPreviousShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 567 | TransactionHeaderPreviousShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 568 | TransactionHeaderPreviousShipVia | SHIP_VIA | — | — |
| 569 | TransactionHeaderPreviousShipmentId | SHIPMENT_ID | — | — |
| 570 | TransactionHeaderPreviousSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 571 | TransactionHeaderPreviousSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 572 | TransactionHeaderPreviousSoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | — |
| 573 | TransactionHeaderPreviousSourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 574 | TransactionHeaderPreviousSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 575 | TransactionHeaderPreviousSpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 576 | TransactionHeaderPreviousStartDateCommitment | START_DATE_COMMITMENT | — | — |
| 577 | TransactionHeaderPreviousStatusTrx | STATUS_TRX | — | — |
| 578 | TransactionHeaderPreviousTermDueDate | TERM_DUE_DATE | — | — |
| 579 | TransactionHeaderPreviousTermId | TERM_ID | — | — |
| 580 | TransactionHeaderPreviousTerritoryId | TERRITORY_ID | — | — |
| 581 | TransactionHeaderPreviousTrxClass | TRX_CLASS | — | — |
| 582 | TransactionHeaderPreviousTrxDate | TRX_DATE | — | — |
| 583 | TransactionHeaderPreviousTrxNumber | TRX_NUMBER | — | ✅ |
| 584 | TransactionHeaderPreviousUpgradeMethod | UPGRADE_METHOD | — | — |
| 585 | TransactionHeaderPreviousWaybillNumber | WAYBILL_NUMBER | — | — |
| 586 | TransactionHeaderPreviousWhUpdateDate | WH_UPDATE_DATE | — | — |
| 587 | TrxHeaderPrevAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 588 | TrxHeaderPrevAgreementId | AGREEMENT_ID | — | — |
| 589 | TrxHeaderPrevApplicationId | APPLICATION_ID | — | — |
| 590 | TrxHeaderPrevApprovalCode | APPROVAL_CODE | — | — |
| 591 | TrxHeaderPrevAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 592 | TrxHeaderPrevBatchId | BATCH_ID | — | — |
| 593 | TrxHeaderPrevBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 594 | TrxHeaderPrevBillTemplateId | BILL_TEMPLATE_ID | — | — |
| 595 | TrxHeaderPrevBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 596 | TrxHeaderPrevBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 597 | TrxHeaderPrevBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 598 | TrxHeaderPrevBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 599 | TrxHeaderPrevBillingDate | BILLING_DATE | — | — |
| 600 | TrxHeaderPrevBrAmount | BR_AMOUNT | — | — |
| 601 | TrxHeaderPrevBrOnHoldFlag | BR_ON_HOLD_FLAG | — | — |
| 602 | TrxHeaderPrevBrUnpaidFlag | BR_UNPAID_FLAG | — | — |
| 603 | TrxHeaderPrevCcErrorCode | CC_ERROR_CODE | — | — |
| 604 | TrxHeaderPrevCcErrorFlag | CC_ERROR_FLAG | — | — |
| 605 | TrxHeaderPrevCcErrorText | CC_ERROR_TEXT | — | — |
| 606 | TrxHeaderPrevComments | COMMENTS | — | — |
| 607 | TrxHeaderPrevCompleteFlag | COMPLETE_FLAG | — | — |
| 608 | TrxHeaderPrevContractId | CONTRACT_ID | — | — |
| 609 | TrxHeaderPrevCreatedBy | CREATED_BY | — | — |
| 610 | TrxHeaderPrevCreatedFrom | CREATED_FROM | — | — |
| 611 | TrxHeaderPrevCreationDate | CREATION_DATE | — | — |
| 612 | TrxHeaderPrevCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | — |
| 613 | TrxHeaderPrevCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | — |
| 614 | TrxHeaderPrevCtReference | CT_REFERENCE | — | — |
| 615 | TrxHeaderPrevCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 616 | TrxHeaderPrevCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 617 | TrxHeaderPrevCustomerReference | CUSTOMER_REFERENCE | — | — |
| 618 | TrxHeaderPrevCustomerReferenceDate | CUSTOMER_REFERENCE_DATE | — | — |
| 619 | TrxHeaderPrevCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 620 | TrxHeaderPrevDefaultTaxExemptFlag | DEFAULT_TAX_EXEMPT_FLAG | — | — |
| 621 | TrxHeaderPrevDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 622 | TrxHeaderPrevDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 623 | TrxHeaderPrevDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 624 | TrxHeaderPrevDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 625 | TrxHeaderPrevDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 626 | TrxHeaderPrevDocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 627 | TrxHeaderPrevDraweeBankAccountId | DRAWEE_BANK_ACCOUNT_ID | — | — |
| 628 | TrxHeaderPrevDraweeContactId | DRAWEE_CONTACT_ID | — | — |
| 629 | TrxHeaderPrevDraweeId | DRAWEE_ID | — | — |
| 630 | TrxHeaderPrevDraweeSiteUseId | DRAWEE_SITE_USE_ID | — | — |
| 631 | TrxHeaderPrevEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 632 | TrxHeaderPrevEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 633 | TrxHeaderPrevEndDateCommitment | END_DATE_COMMITMENT | — | — |
| 634 | TrxHeaderPrevExchangeDate | EXCHANGE_DATE | — | — |
| 635 | TrxHeaderPrevExchangeRate | EXCHANGE_RATE | — | — |
| 636 | TrxHeaderPrevExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 637 | TrxHeaderPrevFinanceCharges | FINANCE_CHARGES | — | — |
| 638 | TrxHeaderPrevFobPoint | FOB_POINT | — | — |
| 639 | TrxHeaderPrevInitialCustomerTrxId | INITIAL_CUSTOMER_TRX_ID | — | — |
| 640 | TrxHeaderPrevIntercompanyFlag | INTERCOMPANY_FLAG | — | — |
| 641 | TrxHeaderPrevInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 642 | TrxHeaderPrevInterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | — |
| 643 | TrxHeaderPrevInterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | — |
| 644 | TrxHeaderPrevInterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | — |
| 645 | TrxHeaderPrevInterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | — |
| 646 | TrxHeaderPrevInterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | — |
| 647 | TrxHeaderPrevInterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | — |
| 648 | TrxHeaderPrevInterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | — |
| 649 | TrxHeaderPrevInterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | — |
| 650 | TrxHeaderPrevInterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | — |
| 651 | TrxHeaderPrevInterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | — |
| 652 | TrxHeaderPrevInterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | — |
| 653 | TrxHeaderPrevInterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | — |
| 654 | TrxHeaderPrevInterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | — |
| 655 | TrxHeaderPrevInterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | — |
| 656 | TrxHeaderPrevInterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | — |
| 657 | TrxHeaderPrevInterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | — |
| 658 | TrxHeaderPrevInternalNotes | INTERNAL_NOTES | — | — |
| 659 | TrxHeaderPrevInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 660 | TrxHeaderPrevInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 661 | TrxHeaderPrevLastPrintedSequenceNum | LAST_PRINTED_SEQUENCE_NUM | — | — |
| 662 | TrxHeaderPrevLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 663 | TrxHeaderPrevLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 664 | TrxHeaderPrevLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 665 | TrxHeaderPrevLateChargesAssessed | LATE_CHARGES_ASSESSED | — | — |
| 666 | TrxHeaderPrevLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 667 | TrxHeaderPrevObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 668 | TrxHeaderPrevOldTrxNumber | OLD_TRX_NUMBER | — | — |
| 669 | TrxHeaderPrevOrgId | ORG_ID | — | — |
| 670 | TrxHeaderPrevOrigSystemBatchName | ORIG_SYSTEM_BATCH_NAME | — | — |
| 671 | TrxHeaderPrevOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 672 | TrxHeaderPrevPayingCustomerId | PAYING_CUSTOMER_ID | — | — |
| 673 | TrxHeaderPrevPayingSiteUseId | PAYING_SITE_USE_ID | — | — |
| 674 | TrxHeaderPrevPaymentAttributes | PAYMENT_ATTRIBUTES | — | — |
| 675 | TrxHeaderPrevPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 676 | TrxHeaderPrevPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 677 | TrxHeaderPrevPostRequestId | POST_REQUEST_ID | — | — |
| 678 | TrxHeaderPrevPostingControlId | POSTING_CONTROL_ID | — | — |
| 679 | TrxHeaderPrevPrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 680 | TrxHeaderPrevPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 681 | TrxHeaderPrevPrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | — |
| 682 | TrxHeaderPrevPrintingCount | PRINTING_COUNT | — | — |
| 683 | TrxHeaderPrevPrintingLastPrinted | PRINTING_LAST_PRINTED | — | — |
| 684 | TrxHeaderPrevPrintingOption | PRINTING_OPTION | — | — |
| 685 | TrxHeaderPrevPrintingOriginalDate | PRINTING_ORIGINAL_DATE | — | — |
| 686 | TrxHeaderPrevPrintingPending | PRINTING_PENDING | — | — |
| 687 | TrxHeaderPrevProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 688 | TrxHeaderPrevProgramId | PROGRAM_ID | — | — |
| 689 | TrxHeaderPrevProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 690 | TrxHeaderPrevPurchaseOrder | PURCHASE_ORDER | — | — |
| 691 | TrxHeaderPrevPurchaseOrderDate | PURCHASE_ORDER_DATE | — | — |
| 692 | TrxHeaderPrevPurchaseOrderRevision | PURCHASE_ORDER_REVISION | — | — |
| 693 | TrxHeaderPrevRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 694 | TrxHeaderPrevReasonCode | REASON_CODE | — | — |
| 695 | TrxHeaderPrevReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 696 | TrxHeaderPrevRecurredFromTrxNumber | RECURRED_FROM_TRX_NUMBER | — | — |
| 697 | TrxHeaderPrevRelatedBatchSourceSeqId | RELATED_BATCH_SOURCE_SEQ_ID | — | — |
| 698 | TrxHeaderPrevRelatedCustomerTrxId | RELATED_CUSTOMER_TRX_ID | — | — |
| 699 | TrxHeaderPrevRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 700 | TrxHeaderPrevRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 701 | TrxHeaderPrevRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 702 | TrxHeaderPrevRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 703 | TrxHeaderPrevRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 704 | TrxHeaderPrevRequestId | REQUEST_ID | — | — |
| 705 | TrxHeaderPrevRequiresManualScheduling | REQUIRES_MANUAL_SCHEDULING | — | — |
| 706 | TrxHeaderPrevReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 707 | TrxHeaderPrevSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 708 | TrxHeaderPrevShipDateActual | SHIP_DATE_ACTUAL | — | — |
| 709 | TrxHeaderPrevShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 710 | TrxHeaderPrevShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 711 | TrxHeaderPrevShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 712 | TrxHeaderPrevShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 713 | TrxHeaderPrevShipVia | SHIP_VIA | — | — |
| 714 | TrxHeaderPrevShipmentId | SHIPMENT_ID | — | — |
| 715 | TrxHeaderPrevSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 716 | TrxHeaderPrevSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 717 | TrxHeaderPrevSoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | — |
| 718 | TrxHeaderPrevSourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 719 | TrxHeaderPrevSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 720 | TrxHeaderPrevSpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 721 | TrxHeaderPrevStartDateCommitment | START_DATE_COMMITMENT | — | — |
| 722 | TrxHeaderPrevStatusTrx | STATUS_TRX | — | — |
| 723 | TrxHeaderPrevTermDueDate | TERM_DUE_DATE | — | — |
| 724 | TrxHeaderPrevTermId | TERM_ID | — | — |
| 725 | TrxHeaderPrevTerritoryId | TERRITORY_ID | — | — |
| 726 | TrxHeaderPrevTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 727 | TrxHeaderPrevTrxClass | TRX_CLASS | — | — |
| 728 | TrxHeaderPrevTrxDate | TRX_DATE | — | — |
| 729 | TrxHeaderPrevTrxNumber | TRX_NUMBER | — | — |
| 730 | TrxHeaderPrevUpgradeMethod | UPGRADE_METHOD | — | — |
| 731 | TrxHeaderPrevUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 732 | TrxHeaderPrevWaybillNumber | WAYBILL_NUMBER | — | — |
| 733 | TrxHeaderPrevWhUpdateDate | WH_UPDATE_DATE | — | — |

### [[ra_customer_trx_lines_all|RA_CUSTOMER_TRX_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionLineAccountingRuleDuration | ACCOUNTING_RULE_DURATION | — | ✅ |
| 2 | TransactionLineAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 3 | TransactionLineAcctdAmountDueOriginal | ACCTD_AMOUNT_DUE_ORIGINAL | — | — |
| 4 | TransactionLineAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | — |
| 5 | TransactionLineAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 6 | TransactionLineAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 7 | TransactionLineAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | ✅ |
| 8 | TransactionLineAssessableValue | ASSESSABLE_VALUE | — | ✅ |
| 9 | TransactionLineAutoruleCompleteFlag | AUTORULE_COMPLETE_FLAG | — | ✅ |
| 10 | TransactionLineAutoruleDurationProcessed | AUTORULE_DURATION_PROCESSED | — | — |
| 11 | TransactionLineAutotax | AUTOTAX | — | ✅ |
| 12 | TransactionLineBrAdjustmentId | BR_ADJUSTMENT_ID | — | — |
| 13 | TransactionLineBrRefCustomerTrxId | BR_REF_CUSTOMER_TRX_ID | — | — |
| 14 | TransactionLineBrRefPaymentScheduleId | BR_REF_PAYMENT_SCHEDULE_ID | — | — |
| 15 | TransactionLineChrgAcctdAmountRemaining | CHRG_ACCTD_AMOUNT_REMAINING | — | — |
| 16 | TransactionLineChrgAmountRemaining | CHRG_AMOUNT_REMAINING | — | — |
| 17 | TransactionLineContractLineId | CONTRACT_LINE_ID | — | — |
| 18 | TransactionLineCreatedBy | CREATED_BY | — | — |
| 19 | TransactionLineCreationDate | CREATION_DATE | — | — |
| 20 | TransactionLineCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 21 | TransactionLineCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 22 | TransactionLineDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 23 | TransactionLineDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 24 | TransactionLineDeferralExclusionFlag | DEFERRAL_EXCLUSION_FLAG | — | ✅ |
| 25 | TransactionLineDescription | DESCRIPTION | — | ✅ |
| 26 | TransactionLineExtendedAcctdAmount | EXTENDED_ACCTD_AMOUNT | — | — |
| 27 | TransactionLineExtendedAmount | EXTENDED_AMOUNT | — | — |
| 28 | TransactionLineFairMarketValueAmount | FAIR_MARKET_VALUE_AMOUNT | — | — |
| 29 | TransactionLineFrtAdjAcctdRemaining | FRT_ADJ_ACCTD_REMAINING | — | — |
| 30 | TransactionLineFrtAdjRemaining | FRT_ADJ_REMAINING | — | — |
| 31 | TransactionLineFrtEdAcctdAmount | FRT_ED_ACCTD_AMOUNT | — | — |
| 32 | TransactionLineFrtEdAmount | FRT_ED_AMOUNT | — | — |
| 33 | TransactionLineFrtUnedAcctdAmount | FRT_UNED_ACCTD_AMOUNT | — | — |
| 34 | TransactionLineFrtUnedAmount | FRT_UNED_AMOUNT | — | — |
| 35 | TransactionLineGrossExtendedAmount | GROSS_EXTENDED_AMOUNT | — | — |
| 36 | TransactionLineGrossUnitSellingPrice | GROSS_UNIT_SELLING_PRICE | — | ✅ |
| 37 | TransactionLineHistoricalFlag | HISTORICAL_FLAG | — | — |
| 38 | TransactionLineInitAccountingRuleDuration | ACCOUNTING_RULE_DURATION | — | — |
| 39 | TransactionLineInitAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 40 | TransactionLineInitAcctdAmountDueOriginal | ACCTD_AMOUNT_DUE_ORIGINAL | — | — |
| 41 | TransactionLineInitAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | — |
| 42 | TransactionLineInitAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 43 | TransactionLineInitAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 44 | TransactionLineInitAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 45 | TransactionLineInitAssessableValue | ASSESSABLE_VALUE | — | — |
| 46 | TransactionLineInitAutoruleCompleteFlag | AUTORULE_COMPLETE_FLAG | — | — |
| 47 | TransactionLineInitAutoruleDurationProcessed | AUTORULE_DURATION_PROCESSED | — | — |
| 48 | TransactionLineInitAutotax | AUTOTAX | — | — |
| 49 | TransactionLineInitBrAdjustmentId | BR_ADJUSTMENT_ID | — | — |
| 50 | TransactionLineInitBrRefCustomerTrxId | BR_REF_CUSTOMER_TRX_ID | — | — |
| 51 | TransactionLineInitBrRefPaymentScheduleId | BR_REF_PAYMENT_SCHEDULE_ID | — | — |
| 52 | TransactionLineInitChrgAcctdAmountRemaining | CHRG_ACCTD_AMOUNT_REMAINING | — | — |
| 53 | TransactionLineInitChrgAmountRemaining | CHRG_AMOUNT_REMAINING | — | — |
| 54 | TransactionLineInitContractLineId | CONTRACT_LINE_ID | — | — |
| 55 | TransactionLineInitCreatedBy | CREATED_BY | — | — |
| 56 | TransactionLineInitCreationDate | CREATION_DATE | — | — |
| 57 | TransactionLineInitCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 58 | TransactionLineInitCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 59 | TransactionLineInitDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 60 | TransactionLineInitDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 61 | TransactionLineInitDeferralExclusionFlag | DEFERRAL_EXCLUSION_FLAG | — | — |
| 62 | TransactionLineInitDescription | DESCRIPTION | — | — |
| 63 | TransactionLineInitExtendedAcctdAmount | EXTENDED_ACCTD_AMOUNT | — | — |
| 64 | TransactionLineInitExtendedAmount | EXTENDED_AMOUNT | — | — |
| 65 | TransactionLineInitFairMarketValueAmount | FAIR_MARKET_VALUE_AMOUNT | — | — |
| 66 | TransactionLineInitFrtAdjAcctdRemaining | FRT_ADJ_ACCTD_REMAINING | — | — |
| 67 | TransactionLineInitFrtAdjRemaining | FRT_ADJ_REMAINING | — | — |
| 68 | TransactionLineInitFrtEdAcctdAmount | FRT_ED_ACCTD_AMOUNT | — | — |
| 69 | TransactionLineInitFrtEdAmount | FRT_ED_AMOUNT | — | — |
| 70 | TransactionLineInitFrtUnedAcctdAmount | FRT_UNED_ACCTD_AMOUNT | — | — |
| 71 | TransactionLineInitFrtUnedAmount | FRT_UNED_AMOUNT | — | — |
| 72 | TransactionLineInitGrossExtendedAmount | GROSS_EXTENDED_AMOUNT | — | — |
| 73 | TransactionLineInitGrossUnitSellingPrice | GROSS_UNIT_SELLING_PRICE | — | — |
| 74 | TransactionLineInitHistoricalFlag | HISTORICAL_FLAG | — | — |
| 75 | TransactionLineInitInitialCustomerTrxLineId | INITIAL_CUSTOMER_TRX_LINE_ID | — | — |
| 76 | TransactionLineInitInterestLineId | INTEREST_LINE_ID | — | — |
| 77 | TransactionLineInitInterfaceLineAttribute1 | INTERFACE_LINE_ATTRIBUTE1 | — | — |
| 78 | TransactionLineInitInterfaceLineAttribute10 | INTERFACE_LINE_ATTRIBUTE10 | — | — |
| 79 | TransactionLineInitInterfaceLineAttribute11 | INTERFACE_LINE_ATTRIBUTE11 | — | — |
| 80 | TransactionLineInitInterfaceLineAttribute12 | INTERFACE_LINE_ATTRIBUTE12 | — | — |
| 81 | TransactionLineInitInterfaceLineAttribute13 | INTERFACE_LINE_ATTRIBUTE13 | — | — |
| 82 | TransactionLineInitInterfaceLineAttribute14 | INTERFACE_LINE_ATTRIBUTE14 | — | — |
| 83 | TransactionLineInitInterfaceLineAttribute15 | INTERFACE_LINE_ATTRIBUTE15 | — | — |
| 84 | TransactionLineInitInterfaceLineAttribute2 | INTERFACE_LINE_ATTRIBUTE2 | — | — |
| 85 | TransactionLineInitInterfaceLineAttribute3 | INTERFACE_LINE_ATTRIBUTE3 | — | — |
| 86 | TransactionLineInitInterfaceLineAttribute4 | INTERFACE_LINE_ATTRIBUTE4 | — | — |
| 87 | TransactionLineInitInterfaceLineAttribute5 | INTERFACE_LINE_ATTRIBUTE5 | — | — |
| 88 | TransactionLineInitInterfaceLineAttribute6 | INTERFACE_LINE_ATTRIBUTE6 | — | — |
| 89 | TransactionLineInitInterfaceLineAttribute7 | INTERFACE_LINE_ATTRIBUTE7 | — | — |
| 90 | TransactionLineInitInterfaceLineAttribute8 | INTERFACE_LINE_ATTRIBUTE8 | — | — |
| 91 | TransactionLineInitInterfaceLineAttribute9 | INTERFACE_LINE_ATTRIBUTE9 | — | — |
| 92 | TransactionLineInitInterfaceLineContext | INTERFACE_LINE_CONTEXT | — | — |
| 93 | TransactionLineInitInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 94 | TransactionLineInitInvoicedLineAcctgLevel | INVOICED_LINE_ACCTG_LEVEL | — | — |
| 95 | TransactionLineInitItemContext | ITEM_CONTEXT | — | — |
| 96 | TransactionLineInitItemExceptionRateId | ITEM_EXCEPTION_RATE_ID | — | — |
| 97 | TransactionLineInitLastPeriodToCredit | LAST_PERIOD_TO_CREDIT | — | — |
| 98 | TransactionLineInitLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 99 | TransactionLineInitLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 100 | TransactionLineInitLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 101 | TransactionLineInitLineIntendedUse | LINE_INTENDED_USE | — | — |
| 102 | TransactionLineInitLineNumber | LINE_NUMBER | — | — |
| 103 | TransactionLineInitLineRecoverable | LINE_RECOVERABLE | — | — |
| 104 | TransactionLineInitLineType | LINE_TYPE | — | — |
| 105 | TransactionLineInitLinkToCustTrxLineId | LINK_TO_CUST_TRX_LINE_ID | — | — |
| 106 | TransactionLineInitLinkToParentlineAttribute1 | LINK_TO_PARENTLINE_ATTRIBUTE1 | — | — |
| 107 | TransactionLineInitLinkToParentlineAttribute10 | LINK_TO_PARENTLINE_ATTRIBUTE10 | — | — |
| 108 | TransactionLineInitLinkToParentlineAttribute11 | LINK_TO_PARENTLINE_ATTRIBUTE11 | — | — |
| 109 | TransactionLineInitLinkToParentlineAttribute12 | LINK_TO_PARENTLINE_ATTRIBUTE12 | — | — |
| 110 | TransactionLineInitLinkToParentlineAttribute13 | LINK_TO_PARENTLINE_ATTRIBUTE13 | — | — |
| 111 | TransactionLineInitLinkToParentlineAttribute14 | LINK_TO_PARENTLINE_ATTRIBUTE14 | — | — |
| 112 | TransactionLineInitLinkToParentlineAttribute15 | LINK_TO_PARENTLINE_ATTRIBUTE15 | — | — |
| 113 | TransactionLineInitLinkToParentlineAttribute2 | LINK_TO_PARENTLINE_ATTRIBUTE2 | — | — |
| 114 | TransactionLineInitLinkToParentlineAttribute3 | LINK_TO_PARENTLINE_ATTRIBUTE3 | — | — |
| 115 | TransactionLineInitLinkToParentlineAttribute4 | LINK_TO_PARENTLINE_ATTRIBUTE4 | — | — |
| 116 | TransactionLineInitLinkToParentlineAttribute5 | LINK_TO_PARENTLINE_ATTRIBUTE5 | — | — |
| 117 | TransactionLineInitLinkToParentlineAttribute6 | LINK_TO_PARENTLINE_ATTRIBUTE6 | — | — |
| 118 | TransactionLineInitLinkToParentlineAttribute7 | LINK_TO_PARENTLINE_ATTRIBUTE7 | — | — |
| 119 | TransactionLineInitLinkToParentlineAttribute8 | LINK_TO_PARENTLINE_ATTRIBUTE8 | — | — |
| 120 | TransactionLineInitLinkToParentlineAttribute9 | LINK_TO_PARENTLINE_ATTRIBUTE9 | — | — |
| 121 | TransactionLineInitLinkToParentlineContext | LINK_TO_PARENTLINE_CONTEXT | — | — |
| 122 | TransactionLineInitLocationSegmentId | LOCATION_SEGMENT_ID | — | — |
| 123 | TransactionLineInitMemoLineSeqId | MEMO_LINE_SEQ_ID | — | — |
| 124 | TransactionLineInitMovementId | MOVEMENT_ID | — | — |
| 125 | TransactionLineInitMrcExtendedAcctdAmount | MRC_EXTENDED_ACCTD_AMOUNT | — | — |
| 126 | TransactionLineInitObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 127 | TransactionLineInitOrgId | ORG_ID | — | — |
| 128 | TransactionLineInitOverrideAutoAccountingFlag | OVERRIDE_AUTO_ACCOUNTING_FLAG | — | — |
| 129 | TransactionLineInitPaymentSetId | PAYMENT_SET_ID | — | — |
| 130 | TransactionLineInitPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 131 | TransactionLineInitPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 132 | TransactionLineInitPreviousCustomerTrxLineId | PREVIOUS_CUSTOMER_TRX_LINE_ID | — | — |
| 133 | TransactionLineInitProductCategory | PRODUCT_CATEGORY | — | — |
| 134 | TransactionLineInitProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | — |
| 135 | TransactionLineInitProductType | PRODUCT_TYPE | — | — |
| 136 | TransactionLineInitProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 137 | TransactionLineInitProgramId | PROGRAM_ID | — | — |
| 138 | TransactionLineInitProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 139 | TransactionLineInitQuantityCredited | QUANTITY_CREDITED | — | — |
| 140 | TransactionLineInitQuantityInvoiced | QUANTITY_INVOICED | — | — |
| 141 | TransactionLineInitQuantityOrdered | QUANTITY_ORDERED | — | — |
| 142 | TransactionLineInitReasonCode | REASON_CODE | — | — |
| 143 | TransactionLineInitRequestId | REQUEST_ID | — | — |
| 144 | TransactionLineInitRevenueAmount | REVENUE_AMOUNT | — | — |
| 145 | TransactionLineInitRuleEndDate | RULE_END_DATE | — | — |
| 146 | TransactionLineInitRuleStartDate | RULE_START_DATE | — | — |
| 147 | TransactionLineInitSalesOrder | SALES_ORDER | — | — |
| 148 | TransactionLineInitSalesOrderDate | SALES_ORDER_DATE | — | — |
| 149 | TransactionLineInitSalesOrderLine | SALES_ORDER_LINE | — | — |
| 150 | TransactionLineInitSalesOrderRevision | SALES_ORDER_REVISION | — | — |
| 151 | TransactionLineInitSalesOrderSource | SALES_ORDER_SOURCE | — | — |
| 152 | TransactionLineInitSalesTaxId | SALES_TAX_ID | — | — |
| 153 | TransactionLineInitSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 154 | TransactionLineInitShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 155 | TransactionLineInitShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 156 | TransactionLineInitShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 157 | TransactionLineInitShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 158 | TransactionLineInitSourceDataKey1 | SOURCE_DATA_KEY1 | — | — |
| 159 | TransactionLineInitSourceDataKey2 | SOURCE_DATA_KEY2 | — | — |
| 160 | TransactionLineInitSourceDataKey3 | SOURCE_DATA_KEY3 | — | — |
| 161 | TransactionLineInitSourceDataKey4 | SOURCE_DATA_KEY4 | — | — |
| 162 | TransactionLineInitSourceDataKey5 | SOURCE_DATA_KEY5 | — | — |
| 163 | TransactionLineInitSourceDocumentLineId | SOURCE_DOCUMENT_LINE_ID | — | — |
| 164 | TransactionLineInitSourceDocumentLineNumber | SOURCE_DOCUMENT_LINE_NUMBER | — | — |
| 165 | TransactionLineInitTaxAction | TAX_ACTION | — | — |
| 166 | TransactionLineInitTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 167 | TransactionLineInitTaxExemptFlag | TAX_EXEMPT_FLAG | — | — |
| 168 | TransactionLineInitTaxExemptNumber | TAX_EXEMPT_NUMBER | — | — |
| 169 | TransactionLineInitTaxExemptReasonCode | TAX_EXEMPT_REASON_CODE | — | — |
| 170 | TransactionLineInitTaxExemptionId | TAX_EXEMPTION_ID | — | — |
| 171 | TransactionLineInitTaxLineId | TAX_LINE_ID | — | — |
| 172 | TransactionLineInitTaxPrecedence | TAX_PRECEDENCE | — | — |
| 173 | TransactionLineInitTaxRate | TAX_RATE | — | — |
| 174 | TransactionLineInitTaxRecoverable | TAX_RECOVERABLE | — | — |
| 175 | TransactionLineInitTaxVendorReturnCode | TAX_VENDOR_RETURN_CODE | — | — |
| 176 | TransactionLineInitTaxableAmount | TAXABLE_AMOUNT | — | — |
| 177 | TransactionLineInitTaxableFlag | TAXABLE_FLAG | — | — |
| 178 | TransactionLineInitTranslatedDescription | TRANSLATED_DESCRIPTION | — | — |
| 179 | TransactionLineInitTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 180 | TransactionLineInitUnitSellingPrice | UNIT_SELLING_PRICE | — | — |
| 181 | TransactionLineInitUnitStandardPrice | UNIT_STANDARD_PRICE | — | — |
| 182 | TransactionLineInitUomCode | UOM_CODE | — | — |
| 183 | TransactionLineInitUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 184 | TransactionLineInitVatTaxId | VAT_TAX_ID | — | — |
| 185 | TransactionLineInitWarehouseId | WAREHOUSE_ID | — | — |
| 186 | TransactionLineInitWhUpdateDate | WH_UPDATE_DATE | — | — |
| 187 | TransactionLineInitialCustomerTrxLineId | INITIAL_CUSTOMER_TRX_LINE_ID | — | — |
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
| 215 | TransactionLineLineRecoverable | LINE_RECOVERABLE | — | — |
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
| 392 | TransactionLinePreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 393 | TransactionLinePreviousCustomerTrxLineId | PREVIOUS_CUSTOMER_TRX_LINE_ID | — | — |
| 394 | TransactionLineProductCategory | PRODUCT_CATEGORY | — | ✅ |
| 395 | TransactionLineProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | ✅ |
| 396 | TransactionLineProductType | PRODUCT_TYPE | — | ✅ |
| 397 | TransactionLineProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 398 | TransactionLineProgramId | PROGRAM_ID | — | — |
| 399 | TransactionLineProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 400 | TransactionLinePrvAccountingRuleDuration | ACCOUNTING_RULE_DURATION | — | — |
| 401 | TransactionLinePrvAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 402 | TransactionLinePrvAcctdAmountDueOriginal | ACCTD_AMOUNT_DUE_ORIGINAL | — | — |
| 403 | TransactionLinePrvAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | — |
| 404 | TransactionLinePrvAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 405 | TransactionLinePrvAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 406 | TransactionLinePrvAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 407 | TransactionLinePrvAssessableValue | ASSESSABLE_VALUE | — | — |
| 408 | TransactionLinePrvAutoruleCompleteFlag | AUTORULE_COMPLETE_FLAG | — | — |
| 409 | TransactionLinePrvAutoruleDurationProcessed | AUTORULE_DURATION_PROCESSED | — | — |
| 410 | TransactionLinePrvAutotax | AUTOTAX | — | — |
| 411 | TransactionLinePrvBrAdjustmentId | BR_ADJUSTMENT_ID | — | — |
| 412 | TransactionLinePrvBrRefCustomerTrxId | BR_REF_CUSTOMER_TRX_ID | — | — |
| 413 | TransactionLinePrvBrRefPaymentScheduleId | BR_REF_PAYMENT_SCHEDULE_ID | — | — |
| 414 | TransactionLinePrvChrgAcctdAmountRemaining | CHRG_ACCTD_AMOUNT_REMAINING | — | — |
| 415 | TransactionLinePrvChrgAmountRemaining | CHRG_AMOUNT_REMAINING | — | — |
| 416 | TransactionLinePrvContractLineId | CONTRACT_LINE_ID | — | — |
| 417 | TransactionLinePrvCreatedBy | CREATED_BY | — | — |
| 418 | TransactionLinePrvCreationDate | CREATION_DATE | — | — |
| 419 | TransactionLinePrvCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 420 | TransactionLinePrvCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 421 | TransactionLinePrvDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 422 | TransactionLinePrvDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 423 | TransactionLinePrvDeferralExclusionFlag | DEFERRAL_EXCLUSION_FLAG | — | — |
| 424 | TransactionLinePrvDescription | DESCRIPTION | — | — |
| 425 | TransactionLinePrvExtendedAcctdAmount | EXTENDED_ACCTD_AMOUNT | — | — |
| 426 | TransactionLinePrvExtendedAmount | EXTENDED_AMOUNT | — | — |
| 427 | TransactionLinePrvFairMarketValueAmount | FAIR_MARKET_VALUE_AMOUNT | — | — |
| 428 | TransactionLinePrvFrtAdjAcctdRemaining | FRT_ADJ_ACCTD_REMAINING | — | — |
| 429 | TransactionLinePrvFrtAdjRemaining | FRT_ADJ_REMAINING | — | — |
| 430 | TransactionLinePrvFrtEdAcctdAmount | FRT_ED_ACCTD_AMOUNT | — | — |
| 431 | TransactionLinePrvFrtEdAmount | FRT_ED_AMOUNT | — | — |
| 432 | TransactionLinePrvFrtUnedAcctdAmount | FRT_UNED_ACCTD_AMOUNT | — | — |
| 433 | TransactionLinePrvFrtUnedAmount | FRT_UNED_AMOUNT | — | — |
| 434 | TransactionLinePrvGrossExtendedAmount | GROSS_EXTENDED_AMOUNT | — | — |
| 435 | TransactionLinePrvGrossUnitSellingPrice | GROSS_UNIT_SELLING_PRICE | — | — |
| 436 | TransactionLinePrvHistoricalFlag | HISTORICAL_FLAG | — | — |
| 437 | TransactionLinePrvInitialCustomerTrxLineId | INITIAL_CUSTOMER_TRX_LINE_ID | — | — |
| 438 | TransactionLinePrvInterestLineId | INTEREST_LINE_ID | — | — |
| 439 | TransactionLinePrvInterfaceLineAttribute1 | INTERFACE_LINE_ATTRIBUTE1 | — | — |
| 440 | TransactionLinePrvInterfaceLineAttribute10 | INTERFACE_LINE_ATTRIBUTE10 | — | — |
| 441 | TransactionLinePrvInterfaceLineAttribute11 | INTERFACE_LINE_ATTRIBUTE11 | — | — |
| 442 | TransactionLinePrvInterfaceLineAttribute12 | INTERFACE_LINE_ATTRIBUTE12 | — | — |
| 443 | TransactionLinePrvInterfaceLineAttribute13 | INTERFACE_LINE_ATTRIBUTE13 | — | — |
| 444 | TransactionLinePrvInterfaceLineAttribute14 | INTERFACE_LINE_ATTRIBUTE14 | — | — |
| 445 | TransactionLinePrvInterfaceLineAttribute15 | INTERFACE_LINE_ATTRIBUTE15 | — | — |
| 446 | TransactionLinePrvInterfaceLineAttribute2 | INTERFACE_LINE_ATTRIBUTE2 | — | — |
| 447 | TransactionLinePrvInterfaceLineAttribute3 | INTERFACE_LINE_ATTRIBUTE3 | — | — |
| 448 | TransactionLinePrvInterfaceLineAttribute4 | INTERFACE_LINE_ATTRIBUTE4 | — | — |
| 449 | TransactionLinePrvInterfaceLineAttribute5 | INTERFACE_LINE_ATTRIBUTE5 | — | — |
| 450 | TransactionLinePrvInterfaceLineAttribute6 | INTERFACE_LINE_ATTRIBUTE6 | — | — |
| 451 | TransactionLinePrvInterfaceLineAttribute7 | INTERFACE_LINE_ATTRIBUTE7 | — | — |
| 452 | TransactionLinePrvInterfaceLineAttribute8 | INTERFACE_LINE_ATTRIBUTE8 | — | — |
| 453 | TransactionLinePrvInterfaceLineAttribute9 | INTERFACE_LINE_ATTRIBUTE9 | — | — |
| 454 | TransactionLinePrvInterfaceLineContext | INTERFACE_LINE_CONTEXT | — | — |
| 455 | TransactionLinePrvInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 456 | TransactionLinePrvInvoicedLineAcctgLevel | INVOICED_LINE_ACCTG_LEVEL | — | — |
| 457 | TransactionLinePrvItemContext | ITEM_CONTEXT | — | — |
| 458 | TransactionLinePrvItemExceptionRateId | ITEM_EXCEPTION_RATE_ID | — | — |
| 459 | TransactionLinePrvLastPeriodToCredit | LAST_PERIOD_TO_CREDIT | — | — |
| 460 | TransactionLinePrvLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 461 | TransactionLinePrvLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 462 | TransactionLinePrvLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 463 | TransactionLinePrvLineIntendedUse | LINE_INTENDED_USE | — | — |
| 464 | TransactionLinePrvLineNumber | LINE_NUMBER | — | ✅ |
| 465 | TransactionLinePrvLineRecoverable | LINE_RECOVERABLE | — | — |
| 466 | TransactionLinePrvLineType | LINE_TYPE | — | — |
| 467 | TransactionLinePrvLinkToCustTrxLineId | LINK_TO_CUST_TRX_LINE_ID | — | — |
| 468 | TransactionLinePrvLinkToParentlineAttribute1 | LINK_TO_PARENTLINE_ATTRIBUTE1 | — | — |
| 469 | TransactionLinePrvLinkToParentlineAttribute10 | LINK_TO_PARENTLINE_ATTRIBUTE10 | — | — |
| 470 | TransactionLinePrvLinkToParentlineAttribute11 | LINK_TO_PARENTLINE_ATTRIBUTE11 | — | — |
| 471 | TransactionLinePrvLinkToParentlineAttribute12 | LINK_TO_PARENTLINE_ATTRIBUTE12 | — | — |
| 472 | TransactionLinePrvLinkToParentlineAttribute13 | LINK_TO_PARENTLINE_ATTRIBUTE13 | — | — |
| 473 | TransactionLinePrvLinkToParentlineAttribute14 | LINK_TO_PARENTLINE_ATTRIBUTE14 | — | — |
| 474 | TransactionLinePrvLinkToParentlineAttribute15 | LINK_TO_PARENTLINE_ATTRIBUTE15 | — | — |
| 475 | TransactionLinePrvLinkToParentlineAttribute2 | LINK_TO_PARENTLINE_ATTRIBUTE2 | — | — |
| 476 | TransactionLinePrvLinkToParentlineAttribute3 | LINK_TO_PARENTLINE_ATTRIBUTE3 | — | — |
| 477 | TransactionLinePrvLinkToParentlineAttribute4 | LINK_TO_PARENTLINE_ATTRIBUTE4 | — | — |
| 478 | TransactionLinePrvLinkToParentlineAttribute5 | LINK_TO_PARENTLINE_ATTRIBUTE5 | — | — |
| 479 | TransactionLinePrvLinkToParentlineAttribute6 | LINK_TO_PARENTLINE_ATTRIBUTE6 | — | — |
| 480 | TransactionLinePrvLinkToParentlineAttribute7 | LINK_TO_PARENTLINE_ATTRIBUTE7 | — | — |
| 481 | TransactionLinePrvLinkToParentlineAttribute8 | LINK_TO_PARENTLINE_ATTRIBUTE8 | — | — |
| 482 | TransactionLinePrvLinkToParentlineAttribute9 | LINK_TO_PARENTLINE_ATTRIBUTE9 | — | — |
| 483 | TransactionLinePrvLinkToParentlineContext | LINK_TO_PARENTLINE_CONTEXT | — | — |
| 484 | TransactionLinePrvLocationSegmentId | LOCATION_SEGMENT_ID | — | — |
| 485 | TransactionLinePrvMemoLineSeqId | MEMO_LINE_SEQ_ID | — | — |
| 486 | TransactionLinePrvMovementId | MOVEMENT_ID | — | — |
| 487 | TransactionLinePrvMrcExtendedAcctdAmount | MRC_EXTENDED_ACCTD_AMOUNT | — | — |
| 488 | TransactionLinePrvObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 489 | TransactionLinePrvOrgId | ORG_ID | — | — |
| 490 | TransactionLinePrvOverrideAutoAccountingFlag | OVERRIDE_AUTO_ACCOUNTING_FLAG | — | — |
| 491 | TransactionLinePrvPaymentSetId | PAYMENT_SET_ID | — | — |
| 492 | TransactionLinePrvPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 493 | TransactionLinePrvPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 494 | TransactionLinePrvPreviousCustomerTrxLineId | PREVIOUS_CUSTOMER_TRX_LINE_ID | — | — |
| 495 | TransactionLinePrvProductCategory | PRODUCT_CATEGORY | — | — |
| 496 | TransactionLinePrvProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | — |
| 497 | TransactionLinePrvProductType | PRODUCT_TYPE | — | — |
| 498 | TransactionLinePrvProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 499 | TransactionLinePrvProgramId | PROGRAM_ID | — | — |
| 500 | TransactionLinePrvProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 501 | TransactionLinePrvQuantityCredited | QUANTITY_CREDITED | — | — |
| 502 | TransactionLinePrvQuantityInvoiced | QUANTITY_INVOICED | — | — |
| 503 | TransactionLinePrvQuantityOrdered | QUANTITY_ORDERED | — | — |
| 504 | TransactionLinePrvReasonCode | REASON_CODE | — | — |
| 505 | TransactionLinePrvRequestId | REQUEST_ID | — | — |
| 506 | TransactionLinePrvRevenueAmount | REVENUE_AMOUNT | — | — |
| 507 | TransactionLinePrvRuleEndDate | RULE_END_DATE | — | — |
| 508 | TransactionLinePrvRuleStartDate | RULE_START_DATE | — | — |
| 509 | TransactionLinePrvSalesOrder | SALES_ORDER | — | — |
| 510 | TransactionLinePrvSalesOrderDate | SALES_ORDER_DATE | — | — |
| 511 | TransactionLinePrvSalesOrderLine | SALES_ORDER_LINE | — | — |
| 512 | TransactionLinePrvSalesOrderRevision | SALES_ORDER_REVISION | — | — |
| 513 | TransactionLinePrvSalesOrderSource | SALES_ORDER_SOURCE | — | — |
| 514 | TransactionLinePrvSalesTaxId | SALES_TAX_ID | — | — |
| 515 | TransactionLinePrvSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 516 | TransactionLinePrvShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 517 | TransactionLinePrvShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 518 | TransactionLinePrvShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 519 | TransactionLinePrvShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 520 | TransactionLinePrvSourceDataKey1 | SOURCE_DATA_KEY1 | — | — |
| 521 | TransactionLinePrvSourceDataKey2 | SOURCE_DATA_KEY2 | — | — |
| 522 | TransactionLinePrvSourceDataKey3 | SOURCE_DATA_KEY3 | — | — |
| 523 | TransactionLinePrvSourceDataKey4 | SOURCE_DATA_KEY4 | — | — |
| 524 | TransactionLinePrvSourceDataKey5 | SOURCE_DATA_KEY5 | — | — |
| 525 | TransactionLinePrvSourceDocumentLineId | SOURCE_DOCUMENT_LINE_ID | — | — |
| 526 | TransactionLinePrvSourceDocumentLineNumber | SOURCE_DOCUMENT_LINE_NUMBER | — | — |
| 527 | TransactionLinePrvTaxAction | TAX_ACTION | — | — |
| 528 | TransactionLinePrvTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 529 | TransactionLinePrvTaxExemptFlag | TAX_EXEMPT_FLAG | — | — |
| 530 | TransactionLinePrvTaxExemptNumber | TAX_EXEMPT_NUMBER | — | — |
| 531 | TransactionLinePrvTaxExemptReasonCode | TAX_EXEMPT_REASON_CODE | — | — |
| 532 | TransactionLinePrvTaxExemptionId | TAX_EXEMPTION_ID | — | — |
| 533 | TransactionLinePrvTaxLineId | TAX_LINE_ID | — | — |
| 534 | TransactionLinePrvTaxPrecedence | TAX_PRECEDENCE | — | — |
| 535 | TransactionLinePrvTaxRate | TAX_RATE | — | — |
| 536 | TransactionLinePrvTaxRecoverable | TAX_RECOVERABLE | — | — |
| 537 | TransactionLinePrvTaxVendorReturnCode | TAX_VENDOR_RETURN_CODE | — | — |
| 538 | TransactionLinePrvTaxableAmount | TAXABLE_AMOUNT | — | — |
| 539 | TransactionLinePrvTaxableFlag | TAXABLE_FLAG | — | — |
| 540 | TransactionLinePrvTranslatedDescription | TRANSLATED_DESCRIPTION | — | — |
| 541 | TransactionLinePrvTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 542 | TransactionLinePrvUnitSellingPrice | UNIT_SELLING_PRICE | — | — |
| 543 | TransactionLinePrvUnitStandardPrice | UNIT_STANDARD_PRICE | — | — |
| 544 | TransactionLinePrvUomCode | UOM_CODE | — | — |
| 545 | TransactionLinePrvUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 546 | TransactionLinePrvVatTaxId | VAT_TAX_ID | — | — |
| 547 | TransactionLinePrvWarehouseId | WAREHOUSE_ID | — | — |
| 548 | TransactionLinePrvWhUpdateDate | WH_UPDATE_DATE | — | — |
| 549 | TransactionLineQuantityCredited | QUANTITY_CREDITED | — | — |
| 550 | TransactionLineQuantityInvoiced | QUANTITY_INVOICED | — | — |
| 551 | TransactionLineQuantityOrdered | QUANTITY_ORDERED | — | — |
| 552 | TransactionLineReasonCode | REASON_CODE | — | ✅ |
| 553 | TransactionLineRequestId | REQUEST_ID | — | — |
| 554 | TransactionLineRevenueAmount | REVENUE_AMOUNT | — | — |
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
| 567 | TransactionLineShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 568 | TransactionLineSourceDataKey1 | SOURCE_DATA_KEY1 | — | — |
| 569 | TransactionLineSourceDataKey2 | SOURCE_DATA_KEY2 | — | — |
| 570 | TransactionLineSourceDataKey3 | SOURCE_DATA_KEY3 | — | — |
| 571 | TransactionLineSourceDataKey4 | SOURCE_DATA_KEY4 | — | — |
| 572 | TransactionLineSourceDataKey5 | SOURCE_DATA_KEY5 | — | — |
| 573 | TransactionLineSourceDocumentLineId | SOURCE_DOCUMENT_LINE_ID | — | — |
| 574 | TransactionLineSourceDocumentLineNumber | SOURCE_DOCUMENT_LINE_NUMBER | — | — |
| 575 | TransactionLineTaxAction | TAX_ACTION | — | — |
| 576 | TransactionLineTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | ✅ |
| 577 | TransactionLineTaxExemptFlag | TAX_EXEMPT_FLAG | — | ✅ |
| 578 | TransactionLineTaxExemptNumber | TAX_EXEMPT_NUMBER | — | ✅ |
| 579 | TransactionLineTaxExemptReasonCode | TAX_EXEMPT_REASON_CODE | — | ✅ |
| 580 | TransactionLineTaxExemptionId | TAX_EXEMPTION_ID | — | — |
| 581 | TransactionLineTaxLineId | TAX_LINE_ID | — | — |
| 582 | TransactionLineTaxPrecedence | TAX_PRECEDENCE | — | ✅ |
| 583 | TransactionLineTaxRate | TAX_RATE | — | ✅ |
| 584 | TransactionLineTaxRecoverable | TAX_RECOVERABLE | — | — |
| 585 | TransactionLineTaxVendorReturnCode | TAX_VENDOR_RETURN_CODE | — | ✅ |
| 586 | TransactionLineTaxableAmount | TAXABLE_AMOUNT | — | — |
| 587 | TransactionLineTaxableFlag | TAXABLE_FLAG | — | — |
| 588 | TransactionLineTranslatedDescription | TRANSLATED_DESCRIPTION | — | — |
| 589 | TransactionLineTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 590 | TransactionLineUnitSellingPrice | UNIT_SELLING_PRICE | — | ✅ |
| 591 | TransactionLineUnitStandardPrice | UNIT_STANDARD_PRICE | — | ✅ |
| 592 | TransactionLineUomCode | UOM_CODE | — | ✅ |
| 593 | TransactionLineUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | ✅ |
| 594 | TransactionLineVatTaxId | VAT_TAX_ID | — | — |
| 595 | TransactionLineWarehouseId | WAREHOUSE_ID | — | — |
| 596 | TransactionLineWhUpdateDate | WH_UPDATE_DATE | — | — |

### [[ra_cust_trx_line_gl_dist_all|RA_CUST_TRX_LINE_GL_DIST_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustTrxLineGlDistId | CUST_TRX_LINE_GL_DIST_ID | 🔑 | ✅ |
| 2 | TransactionLineDistributionAccountClass | ACCOUNT_CLASS | — | ✅ |
| 3 | TransactionLineDistributionAccountSetFlag | ACCOUNT_SET_FLAG | — | ✅ |
| 4 | TransactionLineDistributionAcctdAmount | ACCTD_AMOUNT | — | ✅ |
| 5 | TransactionLineDistributionAmount | AMOUNT | — | ✅ |
| 6 | TransactionLineDistributionCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 7 | TransactionLineDistributionCollectedTaxCcid | COLLECTED_TAX_CCID | — | — |
| 8 | TransactionLineDistributionCollectedTaxConcatSeg | COLLECTED_TAX_CONCAT_SEG | — | ✅ |
| 9 | TransactionLineDistributionComments | COMMENTS | — | ✅ |
| 10 | TransactionLineDistributionConcatenatedSegments | CONCATENATED_SEGMENTS | — | ✅ |
| 11 | TransactionLineDistributionCreatedBy | CREATED_BY | — | — |
| 12 | TransactionLineDistributionCreationDate | CREATION_DATE | — | — |
| 13 | TransactionLineDistributionCustTrxLineSalesrepId | CUST_TRX_LINE_SALESREP_ID | — | ✅ |
| 14 | TransactionLineDistributionCustomerTrxId | CUSTOMER_TRX_ID | — | ✅ |
| 15 | TransactionLineDistributionCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | ✅ |
| 16 | TransactionLineDistributionEventId | EVENT_ID | — | ✅ |
| 17 | TransactionLineDistributionGlDate | GL_DATE | — | ✅ |
| 18 | TransactionLineDistributionGlPostedDate | GL_POSTED_DATE | — | ✅ |
| 19 | TransactionLineDistributionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | TransactionLineDistributionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | TransactionLineDistributionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 22 | TransactionLineDistributionLatestRecFlag | LATEST_REC_FLAG | — | ✅ |
| 23 | TransactionLineDistributionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 24 | TransactionLineDistributionOrgId | ORG_ID | — | — |
| 25 | TransactionLineDistributionOriginalGlDate | ORIGINAL_GL_DATE | — | ✅ |
| 26 | TransactionLineDistributionPercent | PERCENT | — | ✅ |
| 27 | TransactionLineDistributionPostRequestId | POST_REQUEST_ID | — | — |
| 28 | TransactionLineDistributionPostingControlId | POSTING_CONTROL_ID | — | ✅ |
| 29 | TransactionLineDistributionProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 30 | TransactionLineDistributionProgramId | PROGRAM_ID | — | — |
| 31 | TransactionLineDistributionProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 32 | TransactionLineDistributionRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 33 | TransactionLineDistributionRecOffsetFlag | REC_OFFSET_FLAG | — | — |
| 34 | TransactionLineDistributionRequestId | REQUEST_ID | — | — |
| 35 | TransactionLineDistributionRevAdjClassTemp | REV_ADJ_CLASS_TEMP | — | — |
| 36 | TransactionLineDistributionRevenueAdjustmentId | REVENUE_ADJUSTMENT_ID | — | — |
| 37 | TransactionLineDistributionRoundingCorrectionFlag | ROUNDING_CORRECTION_FLAG | — | — |
| 38 | TransactionLineDistributionSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 39 | TransactionLineDistributionTransferToCosting | TRANSFER_TO_COSTING | — | — |
| 40 | TransactionLineDistributionUserGeneratedFlag | USER_GENERATED_FLAG | — | — |

### [[ra_cust_trx_line_salesreps_all|RA_CUST_TRX_LINE_SALESREPS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SalesCreditAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | SalesCreditCreatedBy | CREATED_BY | — | — |
| 3 | SalesCreditCreationDate | CREATION_DATE | — | — |
| 4 | SalesCreditCustTrxLineSalesrepId | CUST_TRX_LINE_SALESREP_ID | — | — |
| 5 | SalesCreditCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 6 | SalesCreditCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 7 | SalesCreditLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | SalesCreditLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | SalesCreditLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | SalesCreditNonRevenueAmountSplit | NON_REVENUE_AMOUNT_SPLIT | — | — |
| 11 | SalesCreditNonRevenuePercentSplit | NON_REVENUE_PERCENT_SPLIT | — | ✅ |
| 12 | SalesCreditNonRevenueSalesgroupId | NON_REVENUE_SALESGROUP_ID | — | — |
| 13 | SalesCreditObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | SalesCreditOrgId | ORG_ID | — | — |
| 15 | SalesCreditOriginalLineSalesrepId | ORIGINAL_LINE_SALESREP_ID | — | — |
| 16 | SalesCreditPrevCustTrxLineSalesrepId | PREV_CUST_TRX_LINE_SALESREP_ID | — | — |
| 17 | SalesCreditProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 18 | SalesCreditProgramId | PROGRAM_ID | — | — |
| 19 | SalesCreditProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 20 | SalesCreditRequestId | REQUEST_ID | — | — |
| 21 | SalesCreditResourceSalesrepId | RESOURCE_SALESREP_ID | — | — |
| 22 | SalesCreditRevenueAdjustmentId | REVENUE_ADJUSTMENT_ID | — | — |
| 23 | SalesCreditRevenueAmountSplit | REVENUE_AMOUNT_SPLIT | — | — |
| 24 | SalesCreditRevenuePercentSplit | REVENUE_PERCENT_SPLIT | — | ✅ |
| 25 | SalesCreditRevenueSalesgroupId | REVENUE_SALESGROUP_ID | — | — |
| 26 | SalesCreditWhUpdateDate | WH_UPDATE_DATE | — | — |

### [[ra_rules|RA_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvDistRuleDescription | DESCRIPTION | — | — |
| 2 | InvDistRuleName | NAME | — | ✅ |
| 3 | InvDistRuleRuleId | RULE_ID | — | — |
| 4 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

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
| 65 | DtlTaxLineObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 66 | DtlTaxLineOffsetFlag | OFFSET_FLAG | — | — |
| 67 | DtlTaxLineOffsetTaxRateCode | OFFSET_TAX_RATE_CODE | — | — |
| 68 | DtlTaxLineOrigSelfAssessedFlag | ORIG_SELF_ASSESSED_FLAG | — | — |
| 69 | DtlTaxLineOrigTaxAmt | ORIG_TAX_AMT | — | — |
| 70 | DtlTaxLineOrigTaxAmtIncludedFlag | ORIG_TAX_AMT_INCLUDED_FLAG | — | — |
| 71 | DtlTaxLineOrigTaxAmtTaxCurr | ORIG_TAX_AMT_TAX_CURR | — | — |
| 72 | DtlTaxLineOrigTaxJurisdictionCode | ORIG_TAX_JURISDICTION_CODE | — | — |
| 73 | DtlTaxLineOrigTaxRate | ORIG_TAX_RATE | — | — |
| 74 | DtlTaxLineOrigTaxRateCode | ORIG_TAX_RATE_CODE | — | — |
| 75 | DtlTaxLineOrigTaxStatusCode | ORIG_TAX_STATUS_CODE | — | — |
| 76 | DtlTaxLineOrigTaxableAmt | ORIG_TAXABLE_AMT | — | — |
| 77 | DtlTaxLineOrigTaxableAmtTaxCurr | ORIG_TAXABLE_AMT_TAX_CURR | — | — |
| 78 | DtlTaxLineOtherDocLineAmt | OTHER_DOC_LINE_AMT | — | — |
| 79 | DtlTaxLineOtherDocLineTaxAmt | OTHER_DOC_LINE_TAX_AMT | — | — |
| 80 | DtlTaxLineOtherDocLineTaxableAmt | OTHER_DOC_LINE_TAXABLE_AMT | — | — |
| 81 | DtlTaxLineOtherDocSource | OTHER_DOC_SOURCE | — | — |
| 82 | DtlTaxLineOverriddenFlag | OVERRIDDEN_FLAG | — | — |
| 83 | DtlTaxLinePlaceOfSupply | PLACE_OF_SUPPLY | — | — |
| 84 | DtlTaxLinePlaceOfSupplyTypeCode | PLACE_OF_SUPPLY_TYPE_CODE | — | — |
| 85 | DtlTaxLinePrdTotalTaxAmt | PRD_TOTAL_TAX_AMT | — | — |
| 86 | DtlTaxLinePrdTotalTaxAmtFunclCurr | PRD_TOTAL_TAX_AMT_FUNCL_CURR | — | — |
| 87 | DtlTaxLinePrdTotalTaxAmtTaxCurr | PRD_TOTAL_TAX_AMT_TAX_CURR | — | — |
| 88 | DtlTaxLinePrecision | PRECISION | — | — |
| 89 | DtlTaxLineProcessForRecoveryFlag | PROCESS_FOR_RECOVERY_FLAG | — | — |
| 90 | DtlTaxLineProrationCode | PRORATION_CODE | — | — |
| 91 | DtlTaxLinePurgeFlag | PURGE_FLAG | — | — |
| 92 | DtlTaxLineRecTaxAmt | REC_TAX_AMT | — | — |
| 93 | DtlTaxLineRecTaxAmtFunclCurr | REC_TAX_AMT_FUNCL_CURR | — | — |
| 94 | DtlTaxLineRecTaxAmtTaxCurr | REC_TAX_AMT_TAX_CURR | — | — |
| 95 | DtlTaxLineRecalcRequiredFlag | RECALC_REQUIRED_FLAG | — | — |
| 96 | DtlTaxLineRecordTypeCode | RECORD_TYPE_CODE | — | — |
| 97 | DtlTaxLineRefDocEntityCode | REF_DOC_ENTITY_CODE | — | — |
| 98 | DtlTaxLineRefDocEventClassCode | REF_DOC_EVENT_CLASS_CODE | — | — |
| 99 | DtlTaxLineRefDocLineQuantity | REF_DOC_LINE_QUANTITY | — | — |
| 100 | DtlTaxLineRefDocTrxLevelType | REF_DOC_TRX_LEVEL_TYPE | — | — |
| 101 | DtlTaxLineRegistrationPartyType | REGISTRATION_PARTY_TYPE | — | — |
| 102 | DtlTaxLineRelatedDocDate | RELATED_DOC_DATE | — | — |
| 103 | DtlTaxLineRelatedDocEntityCode | RELATED_DOC_ENTITY_CODE | — | — |
| 104 | DtlTaxLineRelatedDocEventClassCode | RELATED_DOC_EVENT_CLASS_CODE | — | — |
| 105 | DtlTaxLineRelatedDocNumber | RELATED_DOC_NUMBER | — | — |
| 106 | DtlTaxLineRelatedDocTrxLevelType | RELATED_DOC_TRX_LEVEL_TYPE | — | — |
| 107 | DtlTaxLineReportingCurrencyCode | REPORTING_CURRENCY_CODE | — | — |
| 108 | DtlTaxLineReportingOnlyFlag | REPORTING_ONLY_FLAG | — | — |
| 109 | DtlTaxLineRoundingLevelCode | ROUNDING_LEVEL_CODE | — | — |
| 110 | DtlTaxLineRoundingLvlPartyType | ROUNDING_LVL_PARTY_TYPE | — | — |
| 111 | DtlTaxLineRoundingRuleCode | ROUNDING_RULE_CODE | — | — |
| 112 | DtlTaxLineSelfAssessedFlag | SELF_ASSESSED_FLAG | — | — |
| 113 | DtlTaxLineSettlementFlag | SETTLEMENT_FLAG | — | — |
| 114 | DtlTaxLineSyncWithPrvdrFlag | SYNC_WITH_PRVDR_FLAG | — | — |
| 115 | DtlTaxLineTax | TAX | — | — |
| 116 | DtlTaxLineTaxAmt | TAX_AMT | — | — |
| 117 | DtlTaxLineTaxAmtFunclCurr | TAX_AMT_FUNCL_CURR | — | — |
| 118 | DtlTaxLineTaxAmtIncludedFlag | TAX_AMT_INCLUDED_FLAG | — | — |
| 119 | DtlTaxLineTaxAmtTaxCurr | TAX_AMT_TAX_CURR | — | — |
| 120 | DtlTaxLineTaxApportionmentFlag | TAX_APPORTIONMENT_FLAG | — | — |
| 121 | DtlTaxLineTaxApportionmentLineNumber | TAX_APPORTIONMENT_LINE_NUMBER | — | — |
| 122 | DtlTaxLineTaxBaseModifierRate | TAX_BASE_MODIFIER_RATE | — | — |
| 123 | DtlTaxLineTaxCalculationFormula | TAX_CALCULATION_FORMULA | — | — |
| 124 | DtlTaxLineTaxCode | TAX_CODE | — | — |
| 125 | DtlTaxLineTaxCurrencyCode | TAX_CURRENCY_CODE | — | — |
| 126 | DtlTaxLineTaxCurrencyConversionDate | TAX_CURRENCY_CONVERSION_DATE | — | — |
| 127 | DtlTaxLineTaxCurrencyConversionRate | TAX_CURRENCY_CONVERSION_RATE | — | — |
| 128 | DtlTaxLineTaxCurrencyConversionType | TAX_CURRENCY_CONVERSION_TYPE | — | — |
| 129 | DtlTaxLineTaxDate | TAX_DATE | — | — |
| 130 | DtlTaxLineTaxDetermineDate | TAX_DETERMINE_DATE | — | — |
| 131 | DtlTaxLineTaxEventClassCode | TAX_EVENT_CLASS_CODE | — | — |
| 132 | DtlTaxLineTaxEventTypeCode | TAX_EVENT_TYPE_CODE | — | — |
| 133 | DtlTaxLineTaxHoldCode | TAX_HOLD_CODE | — | — |
| 134 | DtlTaxLineTaxHoldReleasedCode | TAX_HOLD_RELEASED_CODE | — | — |
| 135 | DtlTaxLineTaxJurisdictionCode | TAX_JURISDICTION_CODE | — | — |
| 136 | DtlTaxLineTaxLineId | TAX_LINE_ID | — | — |
| 137 | DtlTaxLineTaxLineNumber | TAX_LINE_NUMBER | — | — |
| 138 | DtlTaxLineTaxOnlyLineFlag | TAX_ONLY_LINE_FLAG | — | — |
| 139 | DtlTaxLineTaxPointDate | TAX_POINT_DATE | — | — |
| 140 | DtlTaxLineTaxRate | TAX_RATE | — | — |
| 141 | DtlTaxLineTaxRateBeforeException | TAX_RATE_BEFORE_EXCEPTION | — | — |
| 142 | DtlTaxLineTaxRateBeforeExemption | TAX_RATE_BEFORE_EXEMPTION | — | — |
| 143 | DtlTaxLineTaxRateCode | TAX_RATE_CODE | — | — |
| 144 | DtlTaxLineTaxRateNameBeforeException | TAX_RATE_NAME_BEFORE_EXCEPTION | — | — |
| 145 | DtlTaxLineTaxRateNameBeforeExemption | TAX_RATE_NAME_BEFORE_EXEMPTION | — | — |
| 146 | DtlTaxLineTaxRateType | TAX_RATE_TYPE | — | — |
| 147 | DtlTaxLineTaxRegimeCode | TAX_REGIME_CODE | — | — |
| 148 | DtlTaxLineTaxRegistrationNumber | TAX_REGISTRATION_NUMBER | — | — |
| 149 | DtlTaxLineTaxStatusCode | TAX_STATUS_CODE | — | — |
| 150 | DtlTaxLineTaxTypeCode | TAX_TYPE_CODE | — | — |
| 151 | DtlTaxLineTaxableAmt | TAXABLE_AMT | — | — |
| 152 | DtlTaxLineTaxableAmtFunclCurr | TAXABLE_AMT_FUNCL_CURR | — | — |
| 153 | DtlTaxLineTaxableAmtTaxCurr | TAXABLE_AMT_TAX_CURR | — | — |
| 154 | DtlTaxLineTaxableBasisFormula | TAXABLE_BASIS_FORMULA | — | — |
| 155 | DtlTaxLineTrxCurrencyCode | TRX_CURRENCY_CODE | — | — |
| 156 | DtlTaxLineTrxDate | TRX_DATE | — | — |
| 157 | DtlTaxLineTrxLevelType | TRX_LEVEL_TYPE | — | — |
| 158 | DtlTaxLineTrxLineDate | TRX_LINE_DATE | — | — |
| 159 | DtlTaxLineTrxLineIndex | TRX_LINE_INDEX | — | — |
| 160 | DtlTaxLineTrxLineNumber | TRX_LINE_NUMBER | — | — |
| 161 | DtlTaxLineTrxLineQuantity | TRX_LINE_QUANTITY | — | — |
| 162 | DtlTaxLineTrxNumber | TRX_NUMBER | — | — |
| 163 | DtlTaxLineUnitPrice | UNIT_PRICE | — | — |
| 164 | DtlTaxLineUnroundedTaxAmt | UNROUNDED_TAX_AMT | — | — |
| 165 | DtlTaxLineUnroundedTaxableAmt | UNROUNDED_TAXABLE_AMT | — | — |

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
