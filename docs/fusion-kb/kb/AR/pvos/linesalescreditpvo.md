---
id: DOC-AR-PVO-LineSalesCreditPVO
doc_type: system-doc
title: "LineSalesCreditPVO — PVO Accounts Receivable"
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
  - LineSalesCreditPVO
  - linesalescreditpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LineSalesCreditPVO

## 📌 Visão Geral

Extrai os créditos de vendas no nível de linha da transação, com detalhamento por item, vendedor e percentual. Viabiliza o cálculo granular de comissões por produto/serviço e a análise de rentabilidade por linha de negócio.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.LineSalesCreditPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 2171 | 43 | 1 | 208 | 10% |

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
- [[ar_revenue_adjustments_all|AR_REVENUE_ADJUSTMENTS_ALL]] — 28 atributos (1 BICC)
- [[ce_bank_acct_uses_all|CE_BANK_ACCT_USES_ALL]] — 25 atributos
- [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]] — 5 atributos (1 BICC)
- [[fnd_territories_vl|FND_TERRITORIES_VL]] — 9 atributos (1 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 1 atributos
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 18 atributos (2 BICC)
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 18 atributos (3 BICC)
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 40 atributos (4 BICC)
- [[hz_cust_account_roles|HZ_CUST_ACCOUNT_ROLES]] — 4 atributos
- [[hz_cust_acct_sites_all|HZ_CUST_ACCT_SITES_ALL]] — 15 atributos
- [[hz_cust_site_uses_all|HZ_CUST_SITE_USES_ALL]] — 6 atributos
- [[hz_locations|HZ_LOCATIONS]] — 26 atributos (20 BICC)
- [[hz_parties|HZ_PARTIES]] — 27 atributos (3 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 12 atributos (3 BICC)
- [[hz_party_site_uses|HZ_PARTY_SITE_USES]] — 3 atributos (1 BICC)
- [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]] — 44 atributos (2 BICC)
- [[iby_fndcpt_tx_extensions|IBY_FNDCPT_TX_EXTENSIONS]] — 28 atributos (2 BICC)
- [[inv_units_of_measure_b|INV_UNITS_OF_MEASURE_B]] — 3 atributos
- [[inv_units_of_measure_tl|INV_UNITS_OF_MEASURE_TL]] — 4 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos
- [[per_users|PER_USERS]] — 9 atributos
- [[ra_batches_all|RA_BATCHES_ALL]] — 33 atributos (1 BICC)
- [[ra_batch_sources_all|RA_BATCH_SOURCES_ALL]] — 124 atributos (3 BICC)
- [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]] — 586 atributos (73 BICC)
- [[ra_customer_trx_lines_all|RA_CUSTOMER_TRX_LINES_ALL]] — 596 atributos (57 BICC)
- [[ra_cust_trx_line_salesreps_all|RA_CUST_TRX_LINE_SALESREPS_ALL]] — 50 atributos (1 PKs, 9 BICC)
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
| 1 | PaymentSchedulesAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | — |
| 2 | PaymentSchedulesActiveClaimFlag | ACTIVE_CLAIM_FLAG | — | — |
| 3 | PaymentSchedulesActualDateClosed | ACTUAL_DATE_CLOSED | — | — |
| 4 | PaymentSchedulesAdjustmentAmountLast | ADJUSTMENT_AMOUNT_LAST | — | — |
| 5 | PaymentSchedulesAdjustmentDateLast | ADJUSTMENT_DATE_LAST | — | — |
| 6 | PaymentSchedulesAdjustmentGlDateLast | ADJUSTMENT_GL_DATE_LAST | — | — |
| 7 | PaymentSchedulesAdjustmentIdLast | ADJUSTMENT_ID_LAST | — | — |
| 8 | PaymentSchedulesAmountAdjusted | AMOUNT_ADJUSTED | — | — |
| 9 | PaymentSchedulesAmountAdjustedPending | AMOUNT_ADJUSTED_PENDING | — | — |
| 10 | PaymentSchedulesAmountApplied | AMOUNT_APPLIED | — | — |
| 11 | PaymentSchedulesAmountCredited | AMOUNT_CREDITED | — | — |
| 12 | PaymentSchedulesAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 13 | PaymentSchedulesAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 14 | PaymentSchedulesAmountInDispute | AMOUNT_IN_DISPUTE | — | — |
| 15 | PaymentSchedulesAmountLineItemsOriginal | AMOUNT_LINE_ITEMS_ORIGINAL | — | — |
| 16 | PaymentSchedulesAmountLineItemsRemaining | AMOUNT_LINE_ITEMS_REMAINING | — | — |
| 17 | PaymentSchedulesAmountOnAccount | AMOUNT_ON_ACCOUNT | — | — |
| 18 | PaymentSchedulesAmountOtherAccount | AMOUNT_OTHER_ACCOUNT | — | — |
| 19 | PaymentSchedulesAssociatedCashReceiptId | ASSOCIATED_CASH_RECEIPT_ID | — | — |
| 20 | PaymentSchedulesBrAmountAssigned | BR_AMOUNT_ASSIGNED | — | — |
| 21 | PaymentSchedulesCallDateLast | CALL_DATE_LAST | — | — |
| 22 | PaymentSchedulesCashAppliedAmountLast | CASH_APPLIED_AMOUNT_LAST | — | — |
| 23 | PaymentSchedulesCashAppliedDateLast | CASH_APPLIED_DATE_LAST | — | — |
| 24 | PaymentSchedulesCashAppliedIdLast | CASH_APPLIED_ID_LAST | — | — |
| 25 | PaymentSchedulesCashAppliedStatusLast | CASH_APPLIED_STATUS_LAST | — | — |
| 26 | PaymentSchedulesCashGlDateLast | CASH_GL_DATE_LAST | — | — |
| 27 | PaymentSchedulesCashReceiptAmountLast | CASH_RECEIPT_AMOUNT_LAST | — | — |
| 28 | PaymentSchedulesCashReceiptDateLast | CASH_RECEIPT_DATE_LAST | — | — |
| 29 | PaymentSchedulesCashReceiptId | CASH_RECEIPT_ID | — | — |
| 30 | PaymentSchedulesCashReceiptIdLast | CASH_RECEIPT_ID_LAST | — | — |
| 31 | PaymentSchedulesCashReceiptStatusLast | CASH_RECEIPT_STATUS_LAST | — | — |
| 32 | PaymentSchedulesCollectorLast | COLLECTOR_LAST | — | — |
| 33 | PaymentSchedulesConsInvId | CONS_INV_ID | — | — |
| 34 | PaymentSchedulesConsInvIdRev | CONS_INV_ID_REV | — | — |
| 35 | PaymentSchedulesCreatedBy | CREATED_BY | — | — |
| 36 | PaymentSchedulesCreationDate | CREATION_DATE | — | — |
| 37 | PaymentSchedulesCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 38 | PaymentSchedulesCustomerId | CUSTOMER_ID | — | — |
| 39 | PaymentSchedulesCustomerSiteUseId | CUSTOMER_SITE_USE_ID | — | — |
| 40 | PaymentSchedulesCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 41 | PaymentSchedulesDiscountDate | DISCOUNT_DATE | — | — |
| 42 | PaymentSchedulesDiscountOriginal | DISCOUNT_ORIGINAL | — | — |
| 43 | PaymentSchedulesDiscountRemaining | DISCOUNT_REMAINING | — | — |
| 44 | PaymentSchedulesDiscountTakenEarned | DISCOUNT_TAKEN_EARNED | — | — |
| 45 | PaymentSchedulesDiscountTakenUnearned | DISCOUNT_TAKEN_UNEARNED | — | — |
| 46 | PaymentSchedulesDisputeDate | DISPUTE_DATE | — | — |
| 47 | PaymentSchedulesDueDate | DUE_DATE | — | — |
| 48 | PaymentSchedulesDunningLevelOverrideDate | DUNNING_LEVEL_OVERRIDE_DATE | — | — |
| 49 | PaymentSchedulesExchangeDate | EXCHANGE_DATE | — | — |
| 50 | PaymentSchedulesExchangeRate | EXCHANGE_RATE | — | — |
| 51 | PaymentSchedulesExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 52 | PaymentSchedulesExcludeFromConsBillFlag | EXCLUDE_FROM_CONS_BILL_FLAG | — | — |
| 53 | PaymentSchedulesExcludeFromDunningFlag | EXCLUDE_FROM_DUNNING_FLAG | — | — |
| 54 | PaymentSchedulesFollowUpCodeLast | FOLLOW_UP_CODE_LAST | — | — |
| 55 | PaymentSchedulesFollowUpDateLast | FOLLOW_UP_DATE_LAST | — | — |
| 56 | PaymentSchedulesFreightOriginal | FREIGHT_ORIGINAL | — | — |
| 57 | PaymentSchedulesFreightRemaining | FREIGHT_REMAINING | — | — |
| 58 | PaymentSchedulesGlDate | GL_DATE | — | — |
| 59 | PaymentSchedulesGlDateClosed | GL_DATE_CLOSED | — | — |
| 60 | PaymentSchedulesInCollection | IN_COLLECTION | — | — |
| 61 | PaymentSchedulesInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 62 | PaymentSchedulesLastChargeDate | LAST_CHARGE_DATE | — | — |
| 63 | PaymentSchedulesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 64 | PaymentSchedulesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 65 | PaymentSchedulesLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 66 | PaymentSchedulesNumberOfDueDates | NUMBER_OF_DUE_DATES | — | — |
| 67 | PaymentSchedulesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 68 | PaymentSchedulesOrgId | ORG_ID | — | — |
| 69 | PaymentSchedulesPaymentApproval | PAYMENT_APPROVAL | — | — |
| 70 | PaymentSchedulesPaymentScheduleClass | CLASS | — | — |
| 71 | PaymentSchedulesPaymentScheduleId | PAYMENT_SCHEDULE_ID | — | — |
| 72 | PaymentSchedulesProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 73 | PaymentSchedulesProgramId | PROGRAM_ID | — | — |
| 74 | PaymentSchedulesProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 75 | PaymentSchedulesPromiseAmountLast | PROMISE_AMOUNT_LAST | — | — |
| 76 | PaymentSchedulesPromiseDateLast | PROMISE_DATE_LAST | — | — |
| 77 | PaymentSchedulesReceiptConfirmedFlag | RECEIPT_CONFIRMED_FLAG | — | — |
| 78 | PaymentSchedulesReceivablesChargesCharged | RECEIVABLES_CHARGES_CHARGED | — | — |
| 79 | PaymentSchedulesReceivablesChargesRemaining | RECEIVABLES_CHARGES_REMAINING | — | — |
| 80 | PaymentSchedulesRequestId | REQUEST_ID | — | — |
| 81 | PaymentSchedulesReservedType | RESERVED_TYPE | — | — |
| 82 | PaymentSchedulesReservedValue | RESERVED_VALUE | — | — |
| 83 | PaymentSchedulesReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 84 | PaymentSchedulesSecondLastChargeDate | SECOND_LAST_CHARGE_DATE | — | — |
| 85 | PaymentSchedulesSelectedForReceiptBatchId | SELECTED_FOR_RECEIPT_BATCH_ID | — | — |
| 86 | PaymentSchedulesStagedDunningLevel | STAGED_DUNNING_LEVEL | — | — |
| 87 | PaymentSchedulesStatus | STATUS | — | — |
| 88 | PaymentSchedulesTaxOriginal | TAX_ORIGINAL | — | — |
| 89 | PaymentSchedulesTaxRemaining | TAX_REMAINING | — | — |
| 90 | PaymentSchedulesTermId | TERM_ID | — | — |
| 91 | PaymentSchedulesTermsSequenceNumber | TERMS_SEQUENCE_NUMBER | — | — |
| 92 | PaymentSchedulesTrxDate | TRX_DATE | — | — |
| 93 | PaymentSchedulesTrxNumber | TRX_NUMBER | — | — |

### [[ar_revenue_adjustments_all|AR_REVENUE_ADJUSTMENTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RevAdjAmount | AMOUNT | — | — |
| 2 | RevAdjAmountMode | AMOUNT_MODE | — | — |
| 3 | RevAdjApplicationDate | APPLICATION_DATE | — | — |
| 4 | RevAdjCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 5 | RevAdjFromCategoryId | FROM_CATEGORY_ID | — | — |
| 6 | RevAdjFromCustTrxLineId | FROM_CUST_TRX_LINE_ID | — | — |
| 7 | RevAdjFromInventoryItemId | FROM_INVENTORY_ITEM_ID | — | — |
| 8 | RevAdjFromResourceSalesrepId | FROM_RESOURCE_SALESREP_ID | — | — |
| 9 | RevAdjFromSalesgroupId | FROM_SALESGROUP_ID | — | — |
| 10 | RevAdjGlDate | GL_DATE | — | — |
| 11 | RevAdjLineSelectionMode | LINE_SELECTION_MODE | — | — |
| 12 | RevAdjOrgId | ORG_ID | — | — |
| 13 | RevAdjPercent | PERCENT | — | — |
| 14 | RevAdjProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 15 | RevAdjProgramId | PROGRAM_ID | — | — |
| 16 | RevAdjProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 17 | RevAdjReasonCode | REASON_CODE | — | — |
| 18 | RevAdjRequestId | REQUEST_ID | — | — |
| 19 | RevAdjRevenueAdjustmentId | REVENUE_ADJUSTMENT_ID | — | — |
| 20 | RevAdjRevenueAdjustmentNumber | REVENUE_ADJUSTMENT_NUMBER | — | ✅ |
| 21 | RevAdjSalesCreditType | SALES_CREDIT_TYPE | — | — |
| 22 | RevAdjStatus | STATUS | — | — |
| 23 | RevAdjToCategoryId | TO_CATEGORY_ID | — | — |
| 24 | RevAdjToCustTrxLineId | TO_CUST_TRX_LINE_ID | — | — |
| 25 | RevAdjToInventoryItemId | TO_INVENTORY_ITEM_ID | — | — |
| 26 | RevAdjToResourceSalesrepId | TO_RESOURCE_SALESREP_ID | — | — |
| 27 | RevAdjToSalesgroupId | TO_SALESGROUP_ID | — | — |
| 28 | RevAdjType | TYPE | — | — |

### [[ce_bank_acct_uses_all|CE_BANK_ACCT_USES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankAcctUsesApUseEnableFlag | AP_USE_ENABLE_FLAG | — | — |
| 2 | BankAcctUsesArUseEnableFlag | AR_USE_ENABLE_FLAG | — | — |
| 3 | BankAcctUsesAuthorizedFlag | AUTHORIZED_FLAG | — | — |
| 4 | BankAcctUsesBankAccountId | BANK_ACCOUNT_ID | — | — |
| 5 | BankAcctUsesBankAcctUseId | BANK_ACCT_USE_ID | — | — |
| 6 | BankAcctUsesDefaultAccountFlag | DEFAULT_ACCOUNT_FLAG | — | — |
| 7 | BankAcctUsesEftScriptName | EFT_SCRIPT_NAME | — | — |
| 8 | BankAcctUsesEndDate | END_DATE | — | — |
| 9 | BankAcctUsesFundingLimitCode | FUNDING_LIMIT_CODE | — | — |
| 10 | BankAcctUsesInvestmentLimitCode | INVESTMENT_LIMIT_CODE | — | — |
| 11 | BankAcctUsesLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 12 | BankAcctUsesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | BankAcctUsesOrgId | ORG_ID | — | — |
| 14 | BankAcctUsesOrgPartyId | ORG_PARTY_ID | — | — |
| 15 | BankAcctUsesPayUseEnableFlag | PAY_USE_ENABLE_FLAG | — | — |
| 16 | BankAcctUsesPortfolioCode | PORTFOLIO_CODE | — | — |
| 17 | BankAcctUsesPricingModel | PRICING_MODEL | — | — |
| 18 | BankAcctUsesPrimaryFlag | PRIMARY_FLAG | — | — |
| 19 | BankAcctUsesProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 20 | BankAcctUsesProgramId | PROGRAM_ID | — | — |
| 21 | BankAcctUsesProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 22 | BankAcctUsesRequestId | REQUEST_ID | — | — |
| 23 | BankAcctUsesXtrBankAccountReference | XTR_BANK_ACCOUNT_REFERENCE | — | — |
| 24 | BankAcctUsesXtrDefaultSettlementFlag | XTR_DEFAULT_SETTLEMENT_FLAG | — | — |
| 25 | BankAcctUsesXtrUseEnableFlag | XTR_USE_ENABLE_FLAG | — | — |

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
| 1 | NonRevSalesOrgEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | NonRevSalesOrgEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | NonRevSalesOrgLanguage | LANGUAGE | — | — |
| 4 | NonRevSalesOrgName | NAME | — | ✅ |
| 5 | NonRevSalesOrgObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | NonRevSalesOrgOrganizationId | ORGANIZATION_ID | — | — |
| 7 | OrgUnitTransEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | OrgUnitTransEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 9 | OrgUnitTransLanguage | LANGUAGE | — | — |
| 10 | OrgUnitTransName | NAME | — | — |
| 11 | OrgUnitTransOrganizationId | ORGANIZATION_ID | — | — |
| 12 | OrgUnitTransSourceLang | SOURCE_LANG | — | — |
| 13 | RevSalesOrgEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 14 | RevSalesOrgEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 15 | RevSalesOrgLanguage | LANGUAGE | — | — |
| 16 | RevSalesOrgName | NAME | — | ✅ |
| 17 | RevSalesOrgObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | RevSalesOrgOrganizationId | ORGANIZATION_ID | — | — |

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
| 3 | SoldToContactContactPersonId | CONTACT_PERSON_ID | — | — |
| 4 | SoldToContactCustAccountRoleId | CUST_ACCOUNT_ROLE_ID | — | — |

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
| 162 | TransactionHeaderBrOnHoldFlag | BR_ON_HOLD_FLAG | — | — |
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
| 180 | TransactionHeaderCustomerTrxId | CUSTOMER_TRX_ID | — | — |
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
| 243 | TransactionHeaderPrevAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 244 | TransactionHeaderPrevAgreementId | AGREEMENT_ID | — | — |
| 245 | TransactionHeaderPrevApplicationId | APPLICATION_ID | — | — |
| 246 | TransactionHeaderPrevApprovalCode | APPROVAL_CODE | — | — |
| 247 | TransactionHeaderPrevAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 248 | TransactionHeaderPrevBatchId | BATCH_ID | — | — |
| 249 | TransactionHeaderPrevBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 250 | TransactionHeaderPrevBillTemplateId | BILL_TEMPLATE_ID | — | — |
| 251 | TransactionHeaderPrevBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 252 | TransactionHeaderPrevBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 253 | TransactionHeaderPrevBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 254 | TransactionHeaderPrevBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 255 | TransactionHeaderPrevBillingDate | BILLING_DATE | — | — |
| 256 | TransactionHeaderPrevBrAmount | BR_AMOUNT | — | — |
| 257 | TransactionHeaderPrevBrOnHoldFlag | BR_ON_HOLD_FLAG | — | — |
| 258 | TransactionHeaderPrevBrUnpaidFlag | BR_UNPAID_FLAG | — | — |
| 259 | TransactionHeaderPrevCcErrorCode | CC_ERROR_CODE | — | — |
| 260 | TransactionHeaderPrevCcErrorFlag | CC_ERROR_FLAG | — | — |
| 261 | TransactionHeaderPrevCcErrorText | CC_ERROR_TEXT | — | — |
| 262 | TransactionHeaderPrevCompleteFlag | COMPLETE_FLAG | — | — |
| 263 | TransactionHeaderPrevContractId | CONTRACT_ID | — | — |
| 264 | TransactionHeaderPrevCreatedBy | CREATED_BY | — | — |
| 265 | TransactionHeaderPrevCreatedFrom | CREATED_FROM | — | — |
| 266 | TransactionHeaderPrevCreationDate | CREATION_DATE | — | — |
| 267 | TransactionHeaderPrevCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | — |
| 268 | TransactionHeaderPrevCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | — |
| 269 | TransactionHeaderPrevCtReference | CT_REFERENCE | — | — |
| 270 | TransactionHeaderPrevCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 271 | TransactionHeaderPrevCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 272 | TransactionHeaderPrevCustomerReference | CUSTOMER_REFERENCE | — | — |
| 273 | TransactionHeaderPrevCustomerReferenceDate | CUSTOMER_REFERENCE_DATE | — | — |
| 274 | TransactionHeaderPrevCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 275 | TransactionHeaderPrevDefaultTaxExemptFlag | DEFAULT_TAX_EXEMPT_FLAG | — | — |
| 276 | TransactionHeaderPrevDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 277 | TransactionHeaderPrevDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 278 | TransactionHeaderPrevDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 279 | TransactionHeaderPrevDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 280 | TransactionHeaderPrevDraweeBankAccountId | DRAWEE_BANK_ACCOUNT_ID | — | — |
| 281 | TransactionHeaderPrevDraweeContactId | DRAWEE_CONTACT_ID | — | — |
| 282 | TransactionHeaderPrevDraweeId | DRAWEE_ID | — | — |
| 283 | TransactionHeaderPrevDraweeSiteUseId | DRAWEE_SITE_USE_ID | — | — |
| 284 | TransactionHeaderPrevEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 285 | TransactionHeaderPrevEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 286 | TransactionHeaderPrevEndDateCommitment | END_DATE_COMMITMENT | — | — |
| 287 | TransactionHeaderPrevExchangeDate | EXCHANGE_DATE | — | — |
| 288 | TransactionHeaderPrevExchangeRate | EXCHANGE_RATE | — | — |
| 289 | TransactionHeaderPrevExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 290 | TransactionHeaderPrevFinanceCharges | FINANCE_CHARGES | — | — |
| 291 | TransactionHeaderPrevFobPoint | FOB_POINT | — | — |
| 292 | TransactionHeaderPrevInitialCustomerTrxId | INITIAL_CUSTOMER_TRX_ID | — | — |
| 293 | TransactionHeaderPrevIntercompanyFlag | INTERCOMPANY_FLAG | — | — |
| 294 | TransactionHeaderPrevInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 295 | TransactionHeaderPrevInterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | — |
| 296 | TransactionHeaderPrevInterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | — |
| 297 | TransactionHeaderPrevInterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | — |
| 298 | TransactionHeaderPrevInterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | — |
| 299 | TransactionHeaderPrevInterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | — |
| 300 | TransactionHeaderPrevInterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | — |
| 301 | TransactionHeaderPrevInterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | — |
| 302 | TransactionHeaderPrevInterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | — |
| 303 | TransactionHeaderPrevInterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | — |
| 304 | TransactionHeaderPrevInterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | — |
| 305 | TransactionHeaderPrevInterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | — |
| 306 | TransactionHeaderPrevInterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | — |
| 307 | TransactionHeaderPrevInterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | — |
| 308 | TransactionHeaderPrevInterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | — |
| 309 | TransactionHeaderPrevInterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | — |
| 310 | TransactionHeaderPrevInterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | — |
| 311 | TransactionHeaderPrevInternalNotes | INTERNAL_NOTES | — | — |
| 312 | TransactionHeaderPrevInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 313 | TransactionHeaderPrevInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 314 | TransactionHeaderPrevLastPrintedSequenceNum | LAST_PRINTED_SEQUENCE_NUM | — | — |
| 315 | TransactionHeaderPrevLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 316 | TransactionHeaderPrevLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 317 | TransactionHeaderPrevLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 318 | TransactionHeaderPrevLateChargesAssessed | LATE_CHARGES_ASSESSED | — | — |
| 319 | TransactionHeaderPrevLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 320 | TransactionHeaderPrevObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 321 | TransactionHeaderPrevOldTrxNumber | OLD_TRX_NUMBER | — | — |
| 322 | TransactionHeaderPrevOrgId | ORG_ID | — | — |
| 323 | TransactionHeaderPrevOrigSystemBatchName | ORIG_SYSTEM_BATCH_NAME | — | — |
| 324 | TransactionHeaderPrevOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 325 | TransactionHeaderPrevPayingCustomerId | PAYING_CUSTOMER_ID | — | — |
| 326 | TransactionHeaderPrevPayingSiteUseId | PAYING_SITE_USE_ID | — | — |
| 327 | TransactionHeaderPrevPaymentAttributes | PAYMENT_ATTRIBUTES | — | — |
| 328 | TransactionHeaderPrevPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 329 | TransactionHeaderPrevPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 330 | TransactionHeaderPrevPostRequestId | POST_REQUEST_ID | — | — |
| 331 | TransactionHeaderPrevPostingControlId | POSTING_CONTROL_ID | — | — |
| 332 | TransactionHeaderPrevPrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 333 | TransactionHeaderPrevPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 334 | TransactionHeaderPrevPrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | — |
| 335 | TransactionHeaderPrevPrintingCount | PRINTING_COUNT | — | — |
| 336 | TransactionHeaderPrevPrintingLastPrinted | PRINTING_LAST_PRINTED | — | — |
| 337 | TransactionHeaderPrevPrintingOption | PRINTING_OPTION | — | — |
| 338 | TransactionHeaderPrevPrintingOriginalDate | PRINTING_ORIGINAL_DATE | — | — |
| 339 | TransactionHeaderPrevPrintingPending | PRINTING_PENDING | — | — |
| 340 | TransactionHeaderPrevProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 341 | TransactionHeaderPrevProgramId | PROGRAM_ID | — | — |
| 342 | TransactionHeaderPrevProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 343 | TransactionHeaderPrevPurchaseOrder | PURCHASE_ORDER | — | — |
| 344 | TransactionHeaderPrevPurchaseOrderDate | PURCHASE_ORDER_DATE | — | — |
| 345 | TransactionHeaderPrevPurchaseOrderRevision | PURCHASE_ORDER_REVISION | — | — |
| 346 | TransactionHeaderPrevRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 347 | TransactionHeaderPrevReasonCode | REASON_CODE | — | — |
| 348 | TransactionHeaderPrevReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 349 | TransactionHeaderPrevRecurredFromTrxNumber | RECURRED_FROM_TRX_NUMBER | — | — |
| 350 | TransactionHeaderPrevRelatedBatchSourceSeqId | RELATED_BATCH_SOURCE_SEQ_ID | — | — |
| 351 | TransactionHeaderPrevRelatedCustomerTrxId | RELATED_CUSTOMER_TRX_ID | — | — |
| 352 | TransactionHeaderPrevRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 353 | TransactionHeaderPrevRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 354 | TransactionHeaderPrevRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 355 | TransactionHeaderPrevRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 356 | TransactionHeaderPrevRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 357 | TransactionHeaderPrevRequestId | REQUEST_ID | — | — |
| 358 | TransactionHeaderPrevReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 359 | TransactionHeaderPrevSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 360 | TransactionHeaderPrevShipDateActual | SHIP_DATE_ACTUAL | — | — |
| 361 | TransactionHeaderPrevShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 362 | TransactionHeaderPrevShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 363 | TransactionHeaderPrevShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 364 | TransactionHeaderPrevShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 365 | TransactionHeaderPrevShipVia | SHIP_VIA | — | — |
| 366 | TransactionHeaderPrevShipmentId | SHIPMENT_ID | — | — |
| 367 | TransactionHeaderPrevSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 368 | TransactionHeaderPrevSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 369 | TransactionHeaderPrevSoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | — |
| 370 | TransactionHeaderPrevSourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 371 | TransactionHeaderPrevSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 372 | TransactionHeaderPrevSpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 373 | TransactionHeaderPrevStartDateCommitment | START_DATE_COMMITMENT | — | — |
| 374 | TransactionHeaderPrevStatusTrx | STATUS_TRX | — | — |
| 375 | TransactionHeaderPrevTermDueDate | TERM_DUE_DATE | — | — |
| 376 | TransactionHeaderPrevTermId | TERM_ID | — | — |
| 377 | TransactionHeaderPrevTerritoryId | TERRITORY_ID | — | — |
| 378 | TransactionHeaderPrevTrxClass | TRX_CLASS | — | — |
| 379 | TransactionHeaderPrevTrxDate | TRX_DATE | — | — |
| 380 | TransactionHeaderPrevTrxNumber | TRX_NUMBER | — | ✅ |
| 381 | TransactionHeaderPrevUpgradeMethod | UPGRADE_METHOD | — | — |
| 382 | TransactionHeaderPrevWaybillNumber | WAYBILL_NUMBER | — | — |
| 383 | TransactionHeaderPrevWhUpdateDate | WH_UPDATE_DATE | — | — |
| 384 | TransactionHeaderPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 385 | TransactionHeaderPrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | — |
| 386 | TransactionHeaderPrintingCount | PRINTING_COUNT | — | ✅ |
| 387 | TransactionHeaderPrintingLastPrinted | PRINTING_LAST_PRINTED | — | — |
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
| 417 | TransactionHeaderShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 418 | TransactionHeaderShipVia | SHIP_VIA | — | ✅ |
| 419 | TransactionHeaderShipmentId | SHIPMENT_ID | — | — |
| 420 | TransactionHeaderSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 421 | TransactionHeaderSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 422 | TransactionHeaderSoldToPartyId | SOLD_TO_PARTY_ID | — | — |
| 423 | TransactionHeaderSoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | — |
| 424 | TransactionHeaderSourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 425 | TransactionHeaderSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 426 | TransactionHeaderSpecialInstructions | SPECIAL_INSTRUCTIONS | — | ✅ |
| 427 | TransactionHeaderStartDateCommitment | START_DATE_COMMITMENT | — | ✅ |
| 428 | TransactionHeaderStatusTrx | STATUS_TRX | — | ✅ |
| 429 | TransactionHeaderTermDueDate | TERM_DUE_DATE | — | ✅ |
| 430 | TransactionHeaderTermId | TERM_ID | — | — |
| 431 | TransactionHeaderTerritoryId | TERRITORY_ID | — | — |
| 432 | TransactionHeaderTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 433 | TransactionHeaderTrxClass | TRX_CLASS | — | ✅ |
| 434 | TransactionHeaderTrxDate | TRX_DATE | — | ✅ |
| 435 | TransactionHeaderTrxNumber | TRX_NUMBER | — | ✅ |
| 436 | TransactionHeaderUpgradeMethod | UPGRADE_METHOD | — | — |
| 437 | TransactionHeaderUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | ✅ |
| 438 | TransactionHeaderWaybillNumber | WAYBILL_NUMBER | — | ✅ |
| 439 | TransactionHeaderWhUpdateDate | WH_UPDATE_DATE | — | — |
| 440 | TrxHeaderPrevAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 441 | TrxHeaderPrevAgreementId | AGREEMENT_ID | — | — |
| 442 | TrxHeaderPrevApplicationId | APPLICATION_ID | — | — |
| 443 | TrxHeaderPrevApprovalCode | APPROVAL_CODE | — | — |
| 444 | TrxHeaderPrevAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 445 | TrxHeaderPrevBatchId | BATCH_ID | — | — |
| 446 | TrxHeaderPrevBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 447 | TrxHeaderPrevBillTemplateId | BILL_TEMPLATE_ID | — | — |
| 448 | TrxHeaderPrevBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 449 | TrxHeaderPrevBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 450 | TrxHeaderPrevBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 451 | TrxHeaderPrevBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 452 | TrxHeaderPrevBillingDate | BILLING_DATE | — | — |
| 453 | TrxHeaderPrevBrAmount | BR_AMOUNT | — | — |
| 454 | TrxHeaderPrevBrOnHoldFlag | BR_ON_HOLD_FLAG | — | — |
| 455 | TrxHeaderPrevBrUnpaidFlag | BR_UNPAID_FLAG | — | — |
| 456 | TrxHeaderPrevCcErrorCode | CC_ERROR_CODE | — | — |
| 457 | TrxHeaderPrevCcErrorFlag | CC_ERROR_FLAG | — | — |
| 458 | TrxHeaderPrevCcErrorText | CC_ERROR_TEXT | — | — |
| 459 | TrxHeaderPrevComments | COMMENTS | — | — |
| 460 | TrxHeaderPrevCompleteFlag | COMPLETE_FLAG | — | — |
| 461 | TrxHeaderPrevContractId | CONTRACT_ID | — | — |
| 462 | TrxHeaderPrevCreatedBy | CREATED_BY | — | — |
| 463 | TrxHeaderPrevCreatedFrom | CREATED_FROM | — | — |
| 464 | TrxHeaderPrevCreationDate | CREATION_DATE | — | — |
| 465 | TrxHeaderPrevCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | — |
| 466 | TrxHeaderPrevCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | — |
| 467 | TrxHeaderPrevCtReference | CT_REFERENCE | — | — |
| 468 | TrxHeaderPrevCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 469 | TrxHeaderPrevCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 470 | TrxHeaderPrevCustomerReference | CUSTOMER_REFERENCE | — | — |
| 471 | TrxHeaderPrevCustomerReferenceDate | CUSTOMER_REFERENCE_DATE | — | — |
| 472 | TrxHeaderPrevCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 473 | TrxHeaderPrevDefaultTaxExemptFlag | DEFAULT_TAX_EXEMPT_FLAG | — | — |
| 474 | TrxHeaderPrevDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 475 | TrxHeaderPrevDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 476 | TrxHeaderPrevDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 477 | TrxHeaderPrevDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 478 | TrxHeaderPrevDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 479 | TrxHeaderPrevDocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 480 | TrxHeaderPrevDraweeBankAccountId | DRAWEE_BANK_ACCOUNT_ID | — | — |
| 481 | TrxHeaderPrevDraweeContactId | DRAWEE_CONTACT_ID | — | — |
| 482 | TrxHeaderPrevDraweeId | DRAWEE_ID | — | — |
| 483 | TrxHeaderPrevDraweeSiteUseId | DRAWEE_SITE_USE_ID | — | — |
| 484 | TrxHeaderPrevEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 485 | TrxHeaderPrevEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 486 | TrxHeaderPrevEndDateCommitment | END_DATE_COMMITMENT | — | — |
| 487 | TrxHeaderPrevExchangeDate | EXCHANGE_DATE | — | — |
| 488 | TrxHeaderPrevExchangeRate | EXCHANGE_RATE | — | — |
| 489 | TrxHeaderPrevExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 490 | TrxHeaderPrevFinanceCharges | FINANCE_CHARGES | — | — |
| 491 | TrxHeaderPrevFobPoint | FOB_POINT | — | — |
| 492 | TrxHeaderPrevInitialCustomerTrxId | INITIAL_CUSTOMER_TRX_ID | — | — |
| 493 | TrxHeaderPrevIntercompanyFlag | INTERCOMPANY_FLAG | — | — |
| 494 | TrxHeaderPrevInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 495 | TrxHeaderPrevInterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | — |
| 496 | TrxHeaderPrevInterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | — |
| 497 | TrxHeaderPrevInterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | — |
| 498 | TrxHeaderPrevInterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | — |
| 499 | TrxHeaderPrevInterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | — |
| 500 | TrxHeaderPrevInterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | — |
| 501 | TrxHeaderPrevInterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | — |
| 502 | TrxHeaderPrevInterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | — |
| 503 | TrxHeaderPrevInterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | — |
| 504 | TrxHeaderPrevInterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | — |
| 505 | TrxHeaderPrevInterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | — |
| 506 | TrxHeaderPrevInterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | — |
| 507 | TrxHeaderPrevInterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | — |
| 508 | TrxHeaderPrevInterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | — |
| 509 | TrxHeaderPrevInterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | — |
| 510 | TrxHeaderPrevInterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | — |
| 511 | TrxHeaderPrevInternalNotes | INTERNAL_NOTES | — | — |
| 512 | TrxHeaderPrevInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 513 | TrxHeaderPrevInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 514 | TrxHeaderPrevLastPrintedSequenceNum | LAST_PRINTED_SEQUENCE_NUM | — | — |
| 515 | TrxHeaderPrevLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 516 | TrxHeaderPrevLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 517 | TrxHeaderPrevLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 518 | TrxHeaderPrevLateChargesAssessed | LATE_CHARGES_ASSESSED | — | — |
| 519 | TrxHeaderPrevLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 520 | TrxHeaderPrevObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 521 | TrxHeaderPrevOldTrxNumber | OLD_TRX_NUMBER | — | — |
| 522 | TrxHeaderPrevOrgId | ORG_ID | — | — |
| 523 | TrxHeaderPrevOrigSystemBatchName | ORIG_SYSTEM_BATCH_NAME | — | — |
| 524 | TrxHeaderPrevOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 525 | TrxHeaderPrevPayingCustomerId | PAYING_CUSTOMER_ID | — | — |
| 526 | TrxHeaderPrevPayingSiteUseId | PAYING_SITE_USE_ID | — | — |
| 527 | TrxHeaderPrevPaymentAttributes | PAYMENT_ATTRIBUTES | — | — |
| 528 | TrxHeaderPrevPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 529 | TrxHeaderPrevPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 530 | TrxHeaderPrevPostRequestId | POST_REQUEST_ID | — | — |
| 531 | TrxHeaderPrevPostingControlId | POSTING_CONTROL_ID | — | — |
| 532 | TrxHeaderPrevPrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 533 | TrxHeaderPrevPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 534 | TrxHeaderPrevPrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | — |
| 535 | TrxHeaderPrevPrintingCount | PRINTING_COUNT | — | — |
| 536 | TrxHeaderPrevPrintingLastPrinted | PRINTING_LAST_PRINTED | — | — |
| 537 | TrxHeaderPrevPrintingOption | PRINTING_OPTION | — | — |
| 538 | TrxHeaderPrevPrintingOriginalDate | PRINTING_ORIGINAL_DATE | — | — |
| 539 | TrxHeaderPrevPrintingPending | PRINTING_PENDING | — | — |
| 540 | TrxHeaderPrevProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 541 | TrxHeaderPrevProgramId | PROGRAM_ID | — | — |
| 542 | TrxHeaderPrevProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 543 | TrxHeaderPrevPurchaseOrder | PURCHASE_ORDER | — | — |
| 544 | TrxHeaderPrevPurchaseOrderDate | PURCHASE_ORDER_DATE | — | — |
| 545 | TrxHeaderPrevPurchaseOrderRevision | PURCHASE_ORDER_REVISION | — | — |
| 546 | TrxHeaderPrevRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 547 | TrxHeaderPrevReasonCode | REASON_CODE | — | — |
| 548 | TrxHeaderPrevReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 549 | TrxHeaderPrevRecurredFromTrxNumber | RECURRED_FROM_TRX_NUMBER | — | — |
| 550 | TrxHeaderPrevRelatedBatchSourceSeqId | RELATED_BATCH_SOURCE_SEQ_ID | — | — |
| 551 | TrxHeaderPrevRelatedCustomerTrxId | RELATED_CUSTOMER_TRX_ID | — | — |
| 552 | TrxHeaderPrevRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 553 | TrxHeaderPrevRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 554 | TrxHeaderPrevRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 555 | TrxHeaderPrevRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 556 | TrxHeaderPrevRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 557 | TrxHeaderPrevRequestId | REQUEST_ID | — | — |
| 558 | TrxHeaderPrevRequiresManualScheduling | REQUIRES_MANUAL_SCHEDULING | — | — |
| 559 | TrxHeaderPrevReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 560 | TrxHeaderPrevSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 561 | TrxHeaderPrevShipDateActual | SHIP_DATE_ACTUAL | — | — |
| 562 | TrxHeaderPrevShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 563 | TrxHeaderPrevShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 564 | TrxHeaderPrevShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 565 | TrxHeaderPrevShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 566 | TrxHeaderPrevShipVia | SHIP_VIA | — | — |
| 567 | TrxHeaderPrevShipmentId | SHIPMENT_ID | — | — |
| 568 | TrxHeaderPrevSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 569 | TrxHeaderPrevSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 570 | TrxHeaderPrevSoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | — |
| 571 | TrxHeaderPrevSourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 572 | TrxHeaderPrevSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 573 | TrxHeaderPrevSpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 574 | TrxHeaderPrevStartDateCommitment | START_DATE_COMMITMENT | — | — |
| 575 | TrxHeaderPrevStatusTrx | STATUS_TRX | — | — |
| 576 | TrxHeaderPrevTermDueDate | TERM_DUE_DATE | — | — |
| 577 | TrxHeaderPrevTermId | TERM_ID | — | — |
| 578 | TrxHeaderPrevTerritoryId | TERRITORY_ID | — | — |
| 579 | TrxHeaderPrevTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 580 | TrxHeaderPrevTrxClass | TRX_CLASS | — | — |
| 581 | TrxHeaderPrevTrxDate | TRX_DATE | — | — |
| 582 | TrxHeaderPrevTrxNumber | TRX_NUMBER | — | — |
| 583 | TrxHeaderPrevUpgradeMethod | UPGRADE_METHOD | — | — |
| 584 | TrxHeaderPrevUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 585 | TrxHeaderPrevWaybillNumber | WAYBILL_NUMBER | — | — |
| 586 | TrxHeaderPrevWhUpdateDate | WH_UPDATE_DATE | — | — |

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
| 392 | TransactionLinePrevAccountingRuleDuration | ACCOUNTING_RULE_DURATION | — | — |
| 393 | TransactionLinePrevAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 394 | TransactionLinePrevAcctdAmountDueOriginal | ACCTD_AMOUNT_DUE_ORIGINAL | — | — |
| 395 | TransactionLinePrevAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | — |
| 396 | TransactionLinePrevAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 397 | TransactionLinePrevAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 398 | TransactionLinePrevAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 399 | TransactionLinePrevAssessableValue | ASSESSABLE_VALUE | — | — |
| 400 | TransactionLinePrevAutoruleCompleteFlag | AUTORULE_COMPLETE_FLAG | — | — |
| 401 | TransactionLinePrevAutoruleDurationProcessed | AUTORULE_DURATION_PROCESSED | — | — |
| 402 | TransactionLinePrevAutotax | AUTOTAX | — | — |
| 403 | TransactionLinePrevBrAdjustmentId | BR_ADJUSTMENT_ID | — | — |
| 404 | TransactionLinePrevBrRefCustomerTrxId | BR_REF_CUSTOMER_TRX_ID | — | — |
| 405 | TransactionLinePrevBrRefPaymentScheduleId | BR_REF_PAYMENT_SCHEDULE_ID | — | — |
| 406 | TransactionLinePrevChrgAcctdAmountRemaining | CHRG_ACCTD_AMOUNT_REMAINING | — | — |
| 407 | TransactionLinePrevChrgAmountRemaining | CHRG_AMOUNT_REMAINING | — | — |
| 408 | TransactionLinePrevContractLineId | CONTRACT_LINE_ID | — | — |
| 409 | TransactionLinePrevCreatedBy | CREATED_BY | — | — |
| 410 | TransactionLinePrevCreationDate | CREATION_DATE | — | — |
| 411 | TransactionLinePrevCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 412 | TransactionLinePrevCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 413 | TransactionLinePrevDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 414 | TransactionLinePrevDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 415 | TransactionLinePrevDeferralExclusionFlag | DEFERRAL_EXCLUSION_FLAG | — | — |
| 416 | TransactionLinePrevDescription | DESCRIPTION | — | — |
| 417 | TransactionLinePrevExtendedAcctdAmount | EXTENDED_ACCTD_AMOUNT | — | — |
| 418 | TransactionLinePrevExtendedAmount | EXTENDED_AMOUNT | — | — |
| 419 | TransactionLinePrevFairMarketValueAmount | FAIR_MARKET_VALUE_AMOUNT | — | — |
| 420 | TransactionLinePrevFrtAdjAcctdRemaining | FRT_ADJ_ACCTD_REMAINING | — | — |
| 421 | TransactionLinePrevFrtAdjRemaining | FRT_ADJ_REMAINING | — | — |
| 422 | TransactionLinePrevFrtEdAcctdAmount | FRT_ED_ACCTD_AMOUNT | — | — |
| 423 | TransactionLinePrevFrtEdAmount | FRT_ED_AMOUNT | — | — |
| 424 | TransactionLinePrevFrtUnedAcctdAmount | FRT_UNED_ACCTD_AMOUNT | — | — |
| 425 | TransactionLinePrevFrtUnedAmount | FRT_UNED_AMOUNT | — | — |
| 426 | TransactionLinePrevGrossExtendedAmount | GROSS_EXTENDED_AMOUNT | — | — |
| 427 | TransactionLinePrevGrossUnitSellingPrice | GROSS_UNIT_SELLING_PRICE | — | — |
| 428 | TransactionLinePrevHistoricalFlag | HISTORICAL_FLAG | — | — |
| 429 | TransactionLinePrevInitialCustomerTrxLineId | INITIAL_CUSTOMER_TRX_LINE_ID | — | — |
| 430 | TransactionLinePrevInterestLineId | INTEREST_LINE_ID | — | — |
| 431 | TransactionLinePrevInterfaceLineAttribute1 | INTERFACE_LINE_ATTRIBUTE1 | — | — |
| 432 | TransactionLinePrevInterfaceLineAttribute10 | INTERFACE_LINE_ATTRIBUTE10 | — | — |
| 433 | TransactionLinePrevInterfaceLineAttribute11 | INTERFACE_LINE_ATTRIBUTE11 | — | — |
| 434 | TransactionLinePrevInterfaceLineAttribute12 | INTERFACE_LINE_ATTRIBUTE12 | — | — |
| 435 | TransactionLinePrevInterfaceLineAttribute13 | INTERFACE_LINE_ATTRIBUTE13 | — | — |
| 436 | TransactionLinePrevInterfaceLineAttribute14 | INTERFACE_LINE_ATTRIBUTE14 | — | — |
| 437 | TransactionLinePrevInterfaceLineAttribute15 | INTERFACE_LINE_ATTRIBUTE15 | — | — |
| 438 | TransactionLinePrevInterfaceLineAttribute2 | INTERFACE_LINE_ATTRIBUTE2 | — | — |
| 439 | TransactionLinePrevInterfaceLineAttribute3 | INTERFACE_LINE_ATTRIBUTE3 | — | — |
| 440 | TransactionLinePrevInterfaceLineAttribute4 | INTERFACE_LINE_ATTRIBUTE4 | — | — |
| 441 | TransactionLinePrevInterfaceLineAttribute5 | INTERFACE_LINE_ATTRIBUTE5 | — | — |
| 442 | TransactionLinePrevInterfaceLineAttribute6 | INTERFACE_LINE_ATTRIBUTE6 | — | — |
| 443 | TransactionLinePrevInterfaceLineAttribute7 | INTERFACE_LINE_ATTRIBUTE7 | — | — |
| 444 | TransactionLinePrevInterfaceLineAttribute8 | INTERFACE_LINE_ATTRIBUTE8 | — | — |
| 445 | TransactionLinePrevInterfaceLineAttribute9 | INTERFACE_LINE_ATTRIBUTE9 | — | — |
| 446 | TransactionLinePrevInterfaceLineContext | INTERFACE_LINE_CONTEXT | — | — |
| 447 | TransactionLinePrevInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 448 | TransactionLinePrevInvoicedLineAcctgLevel | INVOICED_LINE_ACCTG_LEVEL | — | — |
| 449 | TransactionLinePrevItemContext | ITEM_CONTEXT | — | — |
| 450 | TransactionLinePrevItemExceptionRateId | ITEM_EXCEPTION_RATE_ID | — | — |
| 451 | TransactionLinePrevLastPeriodToCredit | LAST_PERIOD_TO_CREDIT | — | — |
| 452 | TransactionLinePrevLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 453 | TransactionLinePrevLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 454 | TransactionLinePrevLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 455 | TransactionLinePrevLineIntendedUse | LINE_INTENDED_USE | — | — |
| 456 | TransactionLinePrevLineNumber | LINE_NUMBER | — | ✅ |
| 457 | TransactionLinePrevLineRecoverable | LINE_RECOVERABLE | — | — |
| 458 | TransactionLinePrevLineType | LINE_TYPE | — | — |
| 459 | TransactionLinePrevLinkToCustTrxLineId | LINK_TO_CUST_TRX_LINE_ID | — | — |
| 460 | TransactionLinePrevLinkToParentlineAttribute1 | LINK_TO_PARENTLINE_ATTRIBUTE1 | — | — |
| 461 | TransactionLinePrevLinkToParentlineAttribute10 | LINK_TO_PARENTLINE_ATTRIBUTE10 | — | — |
| 462 | TransactionLinePrevLinkToParentlineAttribute11 | LINK_TO_PARENTLINE_ATTRIBUTE11 | — | — |
| 463 | TransactionLinePrevLinkToParentlineAttribute12 | LINK_TO_PARENTLINE_ATTRIBUTE12 | — | — |
| 464 | TransactionLinePrevLinkToParentlineAttribute13 | LINK_TO_PARENTLINE_ATTRIBUTE13 | — | — |
| 465 | TransactionLinePrevLinkToParentlineAttribute14 | LINK_TO_PARENTLINE_ATTRIBUTE14 | — | — |
| 466 | TransactionLinePrevLinkToParentlineAttribute15 | LINK_TO_PARENTLINE_ATTRIBUTE15 | — | — |
| 467 | TransactionLinePrevLinkToParentlineAttribute2 | LINK_TO_PARENTLINE_ATTRIBUTE2 | — | — |
| 468 | TransactionLinePrevLinkToParentlineAttribute3 | LINK_TO_PARENTLINE_ATTRIBUTE3 | — | — |
| 469 | TransactionLinePrevLinkToParentlineAttribute4 | LINK_TO_PARENTLINE_ATTRIBUTE4 | — | — |
| 470 | TransactionLinePrevLinkToParentlineAttribute5 | LINK_TO_PARENTLINE_ATTRIBUTE5 | — | — |
| 471 | TransactionLinePrevLinkToParentlineAttribute6 | LINK_TO_PARENTLINE_ATTRIBUTE6 | — | — |
| 472 | TransactionLinePrevLinkToParentlineAttribute7 | LINK_TO_PARENTLINE_ATTRIBUTE7 | — | — |
| 473 | TransactionLinePrevLinkToParentlineAttribute8 | LINK_TO_PARENTLINE_ATTRIBUTE8 | — | — |
| 474 | TransactionLinePrevLinkToParentlineAttribute9 | LINK_TO_PARENTLINE_ATTRIBUTE9 | — | — |
| 475 | TransactionLinePrevLinkToParentlineContext | LINK_TO_PARENTLINE_CONTEXT | — | — |
| 476 | TransactionLinePrevLocationSegmentId | LOCATION_SEGMENT_ID | — | — |
| 477 | TransactionLinePrevMemoLineSeqId | MEMO_LINE_SEQ_ID | — | — |
| 478 | TransactionLinePrevMovementId | MOVEMENT_ID | — | — |
| 479 | TransactionLinePrevMrcExtendedAcctdAmount | MRC_EXTENDED_ACCTD_AMOUNT | — | — |
| 480 | TransactionLinePrevObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 481 | TransactionLinePrevOrgId | ORG_ID | — | — |
| 482 | TransactionLinePrevOverrideAutoAccountingFlag | OVERRIDE_AUTO_ACCOUNTING_FLAG | — | — |
| 483 | TransactionLinePrevPaymentSetId | PAYMENT_SET_ID | — | — |
| 484 | TransactionLinePrevPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 485 | TransactionLinePrevPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 486 | TransactionLinePrevPreviousCustomerTrxLineId | PREVIOUS_CUSTOMER_TRX_LINE_ID | — | — |
| 487 | TransactionLinePrevProductCategory | PRODUCT_CATEGORY | — | — |
| 488 | TransactionLinePrevProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | — |
| 489 | TransactionLinePrevProductType | PRODUCT_TYPE | — | — |
| 490 | TransactionLinePrevProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 491 | TransactionLinePrevProgramId | PROGRAM_ID | — | — |
| 492 | TransactionLinePrevProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 493 | TransactionLinePrevQuantityCredited | QUANTITY_CREDITED | — | — |
| 494 | TransactionLinePrevQuantityInvoiced | QUANTITY_INVOICED | — | — |
| 495 | TransactionLinePrevQuantityOrdered | QUANTITY_ORDERED | — | — |
| 496 | TransactionLinePrevReasonCode | REASON_CODE | — | — |
| 497 | TransactionLinePrevRequestId | REQUEST_ID | — | — |
| 498 | TransactionLinePrevRevenueAmount | REVENUE_AMOUNT | — | — |
| 499 | TransactionLinePrevRuleEndDate | RULE_END_DATE | — | — |
| 500 | TransactionLinePrevRuleStartDate | RULE_START_DATE | — | — |
| 501 | TransactionLinePrevSalesOrder | SALES_ORDER | — | — |
| 502 | TransactionLinePrevSalesOrderDate | SALES_ORDER_DATE | — | — |
| 503 | TransactionLinePrevSalesOrderLine | SALES_ORDER_LINE | — | — |
| 504 | TransactionLinePrevSalesOrderRevision | SALES_ORDER_REVISION | — | — |
| 505 | TransactionLinePrevSalesOrderSource | SALES_ORDER_SOURCE | — | — |
| 506 | TransactionLinePrevSalesTaxId | SALES_TAX_ID | — | — |
| 507 | TransactionLinePrevSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 508 | TransactionLinePrevShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 509 | TransactionLinePrevShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 510 | TransactionLinePrevShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 511 | TransactionLinePrevShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 512 | TransactionLinePrevSourceDataKey1 | SOURCE_DATA_KEY1 | — | — |
| 513 | TransactionLinePrevSourceDataKey2 | SOURCE_DATA_KEY2 | — | — |
| 514 | TransactionLinePrevSourceDataKey3 | SOURCE_DATA_KEY3 | — | — |
| 515 | TransactionLinePrevSourceDataKey4 | SOURCE_DATA_KEY4 | — | — |
| 516 | TransactionLinePrevSourceDataKey5 | SOURCE_DATA_KEY5 | — | — |
| 517 | TransactionLinePrevSourceDocumentLineId | SOURCE_DOCUMENT_LINE_ID | — | — |
| 518 | TransactionLinePrevSourceDocumentLineNumber | SOURCE_DOCUMENT_LINE_NUMBER | — | — |
| 519 | TransactionLinePrevTaxAction | TAX_ACTION | — | — |
| 520 | TransactionLinePrevTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 521 | TransactionLinePrevTaxExemptFlag | TAX_EXEMPT_FLAG | — | — |
| 522 | TransactionLinePrevTaxExemptNumber | TAX_EXEMPT_NUMBER | — | — |
| 523 | TransactionLinePrevTaxExemptReasonCode | TAX_EXEMPT_REASON_CODE | — | — |
| 524 | TransactionLinePrevTaxExemptionId | TAX_EXEMPTION_ID | — | — |
| 525 | TransactionLinePrevTaxLineId | TAX_LINE_ID | — | — |
| 526 | TransactionLinePrevTaxPrecedence | TAX_PRECEDENCE | — | — |
| 527 | TransactionLinePrevTaxRate | TAX_RATE | — | — |
| 528 | TransactionLinePrevTaxRecoverable | TAX_RECOVERABLE | — | — |
| 529 | TransactionLinePrevTaxVendorReturnCode | TAX_VENDOR_RETURN_CODE | — | — |
| 530 | TransactionLinePrevTaxableAmount | TAXABLE_AMOUNT | — | — |
| 531 | TransactionLinePrevTaxableFlag | TAXABLE_FLAG | — | — |
| 532 | TransactionLinePrevTranslatedDescription | TRANSLATED_DESCRIPTION | — | — |
| 533 | TransactionLinePrevTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 534 | TransactionLinePrevUnitSellingPrice | UNIT_SELLING_PRICE | — | — |
| 535 | TransactionLinePrevUnitStandardPrice | UNIT_STANDARD_PRICE | — | — |
| 536 | TransactionLinePrevUomCode | UOM_CODE | — | — |
| 537 | TransactionLinePrevUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 538 | TransactionLinePrevVatTaxId | VAT_TAX_ID | — | — |
| 539 | TransactionLinePrevWarehouseId | WAREHOUSE_ID | — | — |
| 540 | TransactionLinePrevWhUpdateDate | WH_UPDATE_DATE | — | — |
| 541 | TransactionLinePreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 542 | TransactionLinePreviousCustomerTrxLineId | PREVIOUS_CUSTOMER_TRX_LINE_ID | — | — |
| 543 | TransactionLineProductCategory | PRODUCT_CATEGORY | — | ✅ |
| 544 | TransactionLineProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | ✅ |
| 545 | TransactionLineProductType | PRODUCT_TYPE | — | ✅ |
| 546 | TransactionLineProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 547 | TransactionLineProgramId | PROGRAM_ID | — | — |
| 548 | TransactionLineProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
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

### [[ra_cust_trx_line_salesreps_all|RA_CUST_TRX_LINE_SALESREPS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustTrxLineSalesrepId | CUST_TRX_LINE_SALESREP_ID | 🔑 | ✅ |
| 2 | LineSalesCreditCreatedBy | CREATED_BY | — | — |
| 3 | LineSalesCreditCreationDate | CREATION_DATE | — | — |
| 4 | LineSalesCreditCustomerTrxId | CUSTOMER_TRX_ID | — | ✅ |
| 5 | LineSalesCreditCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | ✅ |
| 6 | LineSalesCreditLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LineSalesCreditLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LineSalesCreditLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | LineSalesCreditNonRevenueAmountSplit | NON_REVENUE_AMOUNT_SPLIT | — | ✅ |
| 10 | LineSalesCreditNonRevenuePercentSplit | NON_REVENUE_PERCENT_SPLIT | — | ✅ |
| 11 | LineSalesCreditNonRevenueSalesgroupId | NON_REVENUE_SALESGROUP_ID | — | — |
| 12 | LineSalesCreditObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | LineSalesCreditOrgId | ORG_ID | — | — |
| 14 | LineSalesCreditOriginalLineSalesrepId | ORIGINAL_LINE_SALESREP_ID | — | — |
| 15 | LineSalesCreditPrevCustTrxLineSalesrepId | PREV_CUST_TRX_LINE_SALESREP_ID | — | — |
| 16 | LineSalesCreditProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 17 | LineSalesCreditProgramId | PROGRAM_ID | — | — |
| 18 | LineSalesCreditProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 19 | LineSalesCreditRequestId | REQUEST_ID | — | — |
| 20 | LineSalesCreditResourceSalesrepId | RESOURCE_SALESREP_ID | — | — |
| 21 | LineSalesCreditRevenueAdjustmentId | REVENUE_ADJUSTMENT_ID | — | — |
| 22 | LineSalesCreditRevenueAmountSplit | REVENUE_AMOUNT_SPLIT | — | ✅ |
| 23 | LineSalesCreditRevenuePercentSplit | REVENUE_PERCENT_SPLIT | — | ✅ |
| 24 | LineSalesCreditRevenueSalesgroupId | REVENUE_SALESGROUP_ID | — | — |
| 25 | LineSalesCreditWhUpdateDate | WH_UPDATE_DATE | — | — |
| 26 | SalesCreditPrevCreatedBy | CREATED_BY | — | — |
| 27 | SalesCreditPrevCreationDate | CREATION_DATE | — | — |
| 28 | SalesCreditPrevCustTrxLineSalesrepId | CUST_TRX_LINE_SALESREP_ID | — | — |
| 29 | SalesCreditPrevCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 30 | SalesCreditPrevCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 31 | SalesCreditPrevLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | SalesCreditPrevLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | SalesCreditPrevLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 34 | SalesCreditPrevNonRevenueAmountSplit | NON_REVENUE_AMOUNT_SPLIT | — | — |
| 35 | SalesCreditPrevNonRevenuePercentSplit | NON_REVENUE_PERCENT_SPLIT | — | — |
| 36 | SalesCreditPrevNonRevenueSalesgroupId | NON_REVENUE_SALESGROUP_ID | — | — |
| 37 | SalesCreditPrevObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 38 | SalesCreditPrevOrgId | ORG_ID | — | — |
| 39 | SalesCreditPrevOriginalLineSalesrepId | ORIGINAL_LINE_SALESREP_ID | — | — |
| 40 | SalesCreditPrevPrevCustTrxLineSalesrepId | PREV_CUST_TRX_LINE_SALESREP_ID | — | — |
| 41 | SalesCreditPrevProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 42 | SalesCreditPrevProgramId | PROGRAM_ID | — | — |
| 43 | SalesCreditPrevProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 44 | SalesCreditPrevRequestId | REQUEST_ID | — | — |
| 45 | SalesCreditPrevResourceSalesrepId | RESOURCE_SALESREP_ID | — | — |
| 46 | SalesCreditPrevRevenueAdjustmentId | REVENUE_ADJUSTMENT_ID | — | — |
| 47 | SalesCreditPrevRevenueAmountSplit | REVENUE_AMOUNT_SPLIT | — | — |
| 48 | SalesCreditPrevRevenuePercentSplit | REVENUE_PERCENT_SPLIT | — | — |
| 49 | SalesCreditPrevRevenueSalesgroupId | REVENUE_SALESGROUP_ID | — | — |
| 50 | SalesCreditPrevWhUpdateDate | WH_UPDATE_DATE | — | — |

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
| 65 | DtlTaxLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
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
