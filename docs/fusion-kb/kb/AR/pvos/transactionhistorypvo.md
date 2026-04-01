---
id: DOC-AR-PVO-TransactionHistoryPVO
doc_type: system-doc
title: "TransactionHistoryPVO — PVO Accounts Receivable"
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
  - TransactionHistoryPVO
  - transactionhistorypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionHistoryPVO

## 📌 Visão Geral

Extrai o histórico completo de eventos das transações de recebíveis (criação, aprovação, impressão, cancelamento), com datas, status e responsáveis. Fornece trilha de auditoria do ciclo de vida das transações para compliance e análise operacional.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.TransactionHistoryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 1463 | 41 | 1 | 59 | 4% |

---

## 🔗 Tabelas Relacionadas

- [[ar_batches_all|AR_BATCHES_ALL]] — 46 atributos (5 BICC)
- [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]] — 4 atributos
- [[ar_deferred_lines_all|AR_DEFERRED_LINES_ALL]] — 18 atributos
- [[ar_interest_headers_all|AR_INTEREST_HEADERS_ALL]] — 35 atributos
- [[ar_interest_lines_all|AR_INTEREST_LINES_ALL]] — 22 atributos
- [[ar_lookups|AR_LOOKUPS]] — 2 atributos
- [[ar_memo_lines_all_b|AR_MEMO_LINES_ALL_B]] — 18 atributos (1 BICC)
- [[ar_memo_lines_all_tl|AR_MEMO_LINES_ALL_TL]] — 5 atributos
- [[ar_payment_schedules_all|AR_PAYMENT_SCHEDULES_ALL]] — 3 atributos
- [[ar_transaction_history_all|AR_TRANSACTION_HISTORY_ALL]] — 33 atributos (1 PKs, 15 BICC)
- [[ce_bank_acct_uses_all|CE_BANK_ACCT_USES_ALL]] — 30 atributos (1 BICC)
- [[ce_internal_bank_accts_v|CE_INTERNAL_BANK_ACCTS_V]] — 81 atributos (1 BICC)
- [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]] — 5 atributos (1 BICC)
- [[fnd_territories_vl|FND_TERRITORIES_VL]] — 9 atributos
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 1 atributos
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 18 atributos (1 BICC)
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 6 atributos
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 37 atributos (1 BICC)
- [[hz_cust_account_roles|HZ_CUST_ACCOUNT_ROLES]] — 8 atributos
- [[hz_cust_acct_sites_all|HZ_CUST_ACCT_SITES_ALL]] — 6 atributos
- [[hz_cust_site_uses_all|HZ_CUST_SITE_USES_ALL]] — 6 atributos
- [[hz_parties|HZ_PARTIES]] — 2 atributos (1 BICC)
- [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]] — 47 atributos (1 BICC)
- [[iby_fndcpt_tx_extensions|IBY_FNDCPT_TX_EXTENSIONS]] — 14 atributos (1 BICC)
- [[iby_pmt_instr_uses_all|IBY_PMT_INSTR_USES_ALL]] — 2 atributos
- [[iby_trxn_summaries_all|IBY_TRXN_SUMMARIES_ALL]] — 2 atributos (1 BICC)
- [[inv_units_of_measure_b|INV_UNITS_OF_MEASURE_B]] — 4 atributos
- [[inv_units_of_measure_tl|INV_UNITS_OF_MEASURE_TL]] — 4 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (2 BICC)
- [[per_users|PER_USERS]] — 8 atributos
- [[ra_batches_all|RA_BATCHES_ALL]] — 39 atributos (4 BICC)
- [[ra_batch_sources_all|RA_BATCH_SOURCES_ALL]] — 127 atributos (4 BICC)
- [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]] — 298 atributos (17 BICC)
- [[ra_customer_trx_lines_all|RA_CUSTOMER_TRX_LINES_ALL]] — 318 atributos (2 BICC)
- [[ra_rules|RA_RULES]] — 4 atributos
- [[zx_fc_intended_use_v|ZX_FC_INTENDED_USE_V]] — 4 atributos
- [[zx_fc_product_categories_v|ZX_FC_PRODUCT_CATEGORIES_V]] — 6 atributos
- [[zx_fc_product_fiscal_v|ZX_FC_PRODUCT_FISCAL_V]] — 8 atributos
- [[zx_fc_user_defined_v|ZX_FC_USER_DEFINED_V]] — 6 atributos
- [[zx_lines|ZX_LINES]] — 165 atributos
- [[zx_product_types_v|ZX_PRODUCT_TYPES_V]] — 2 atributos

---

## ⚙️ Atributos

### [[ar_batches_all|AR_BATCHES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReceiptBatchAutoPrintProgramId | AUTO_PRINT_PROGRAM_ID | — | — |
| 2 | ReceiptBatchAutoTransProgramId | AUTO_TRANS_PROGRAM_ID | — | — |
| 3 | ReceiptBatchBankDepositNumber | BANK_DEPOSIT_NUMBER | — | — |
| 4 | ReceiptBatchBatchAppliedStatus | BATCH_APPLIED_STATUS | — | — |
| 5 | ReceiptBatchBatchDate | BATCH_DATE | — | ✅ |
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

### [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RevCashRcptCashReceiptId | CASH_RECEIPT_ID | — | — |
| 2 | RevCashRcptComments | COMMENTS | — | — |
| 3 | RevCashRcptIssuerName | ISSUER_NAME | — | — |
| 4 | RevCashRcptReceiptNumber | RECEIPT_NUMBER | — | — |

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
| 5 | IntrstLineDaysOfInterest | DAYS_OF_INTEREST | — | — |
| 6 | IntrstLineDaysOverdueLate | DAYS_OVERDUE_LATE | — | — |
| 7 | IntrstLineDueDate | DUE_DATE | — | — |
| 8 | IntrstLineFinanceChargeCharged | FINANCE_CHARGE_CHARGED | — | — |
| 9 | IntrstLineInterestCharged | INTEREST_CHARGED | — | — |
| 10 | IntrstLineInterestLineId | INTEREST_LINE_ID | — | — |
| 11 | IntrstLineInterestRate | INTEREST_RATE | — | — |
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
| 1 | TrxClassLookupCode | LOOKUP_CODE | — | — |
| 2 | TrxClassLookupType | LOOKUP_TYPE | — | — |

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
| 1 | MemoLineDescription | DESCRIPTION | — | — |
| 2 | MemoLineName | NAME | — | — |
| 3 | MemoLineTranslationLanguage | LANGUAGE | — | — |
| 4 | MemoLineTranslationMemoLineId | MEMO_LINE_ID | — | — |
| 5 | MemoLineTranslationSetId | SET_ID | — | — |

### [[ar_payment_schedules_all|AR_PAYMENT_SCHEDULES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BrPaymentSchedulesAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | — |
| 2 | BrPaymentSchedulesAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 3 | BrPaymentSchedulesPaymentScheduleId | PAYMENT_SCHEDULE_ID | — | — |

### [[ar_transaction_history_all|AR_TRANSACTION_HISTORY_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionHistoryAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | TransactionHistoryBatchId | BATCH_ID | — | — |
| 3 | TransactionHistoryComments | COMMENTS | — | — |
| 4 | TransactionHistoryCreatedBy | CREATED_BY | — | ✅ |
| 5 | TransactionHistoryCreatedFrom | CREATED_FROM | — | — |
| 6 | TransactionHistoryCreationDate | CREATION_DATE | — | ✅ |
| 7 | TransactionHistoryCurrentAccountedFlag | CURRENT_ACCOUNTED_FLAG | — | ✅ |
| 8 | TransactionHistoryCurrentRecordFlag | CURRENT_RECORD_FLAG | — | ✅ |
| 9 | TransactionHistoryCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 10 | TransactionHistoryEvent | EVENT | — | ✅ |
| 11 | TransactionHistoryEventId | EVENT_ID | — | — |
| 12 | TransactionHistoryFirstPostedRecordFlag | FIRST_POSTED_RECORD_FLAG | — | — |
| 13 | TransactionHistoryGlDate | GL_DATE | — | ✅ |
| 14 | TransactionHistoryGlPostedDate | GL_POSTED_DATE | — | ✅ |
| 15 | TransactionHistoryId | TRANSACTION_HISTORY_ID | 🔑 | ✅ |
| 16 | TransactionHistoryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | TransactionHistoryLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | TransactionHistoryLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | TransactionHistoryMaturityDate | MATURITY_DATE | — | ✅ |
| 20 | TransactionHistoryMrcCreatedFrom | MRC_CREATED_FROM | — | — |
| 21 | TransactionHistoryMrcGlPostedDate | MRC_GL_POSTED_DATE | — | — |
| 22 | TransactionHistoryMrcPostingControlId | MRC_POSTING_CONTROL_ID | — | — |
| 23 | TransactionHistoryObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 24 | TransactionHistoryOrgId | ORG_ID | — | — |
| 25 | TransactionHistoryPostableFlag | POSTABLE_FLAG | — | ✅ |
| 26 | TransactionHistoryPostingControlId | POSTING_CONTROL_ID | — | ✅ |
| 27 | TransactionHistoryProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 28 | TransactionHistoryProgramId | PROGRAM_ID | — | — |
| 29 | TransactionHistoryProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 30 | TransactionHistoryPrvTrxHistoryId | PRV_TRX_HISTORY_ID | — | — |
| 31 | TransactionHistoryRequestId | REQUEST_ID | — | — |
| 32 | TransactionHistoryStatus | STATUS | — | ✅ |
| 33 | TransactionHistoryTrxDate | TRX_DATE | — | ✅ |

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
| 9 | TerritoryTerritoryShortName | TERRITORY_SHORT_NAME | — | — |

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
| 17 | DailyConversionTypeUserConversionType | USER_CONVERSION_TYPE | — | — |
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
| 32 | PayingCustAcctAccountName | ACCOUNT_NAME | — | — |
| 33 | PayingCustAcctCustAccountId | CUST_ACCOUNT_ID | — | — |
| 34 | ShipToCustAcctAccountName | ACCOUNT_NAME | — | — |
| 35 | ShipToCustAcctCustAccountId | CUST_ACCOUNT_ID | — | — |
| 36 | SoldToCustAcctAccountName | ACCOUNT_NAME | — | — |
| 37 | SoldToCustAcctCustAccountId | CUST_ACCOUNT_ID | — | — |

### [[hz_cust_account_roles|HZ_CUST_ACCOUNT_ROLES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillToContactContactPersonId | CONTACT_PERSON_ID | — | — |
| 2 | BillToContactCustAccountRoleId | CUST_ACCOUNT_ROLE_ID | — | — |
| 3 | DraweeToContactContactPersonId | CONTACT_PERSON_ID | — | — |
| 4 | DraweeToContactCustAccountRoleId | CUST_ACCOUNT_ROLE_ID | — | — |
| 5 | ShipToContactContactPersonId | CONTACT_PERSON_ID | — | — |
| 6 | ShipToContactCustAccountRoleId | CUST_ACCOUNT_ROLE_ID | — | — |
| 7 | SoldToContactContactPersonId | CONTACT_PERSON_ID | — | — |
| 8 | SoldToContactCustAccountRoleId | CUST_ACCOUNT_ROLE_ID | — | — |

### [[hz_cust_acct_sites_all|HZ_CUST_ACCT_SITES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RmtToAddrSiteCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 2 | RmtToAddrSiteLanguage | ACCT_SITE_LANGUAGE | — | — |
| 3 | RmtToAddrSitePartySiteId | PARTY_SITE_ID | — | — |
| 4 | ShipToAddrSiteCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 5 | ShipToAddrSiteLanguage | ACCT_SITE_LANGUAGE | — | — |
| 6 | ShipToAddrSitePartySiteId | PARTY_SITE_ID | — | — |

### [[hz_cust_site_uses_all|HZ_CUST_SITE_USES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayingSiteUseCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 2 | PayingSiteUseSiteUseId | SITE_USE_ID | — | — |
| 3 | ShipToSiteUseCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 4 | ShipToSiteUseSiteUseId | SITE_USE_ID | — | — |
| 5 | SoldToSiteUseCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 6 | SoldToSiteUseSiteUseId | SITE_USE_ID | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DraweeContactPartyId | PARTY_ID | — | — |
| 2 | DraweeContactPartyName | PARTY_NAME | — | ✅ |

### [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DraweeBankAccountBankAccountName | BANK_ACCOUNT_NAME | — | — |
| 2 | DraweeBankAccountBankAccountNum | BANK_ACCOUNT_NUM | — | ✅ |
| 3 | DraweeBankAccountExtBankAccountId | EXT_BANK_ACCOUNT_ID | — | — |
| 4 | IbyExtBankAccountsAccountClassification | ACCOUNT_CLASSIFICATION | — | — |
| 5 | IbyExtBankAccountsAccountSuffix | ACCOUNT_SUFFIX | — | — |
| 6 | IbyExtBankAccountsAgencyLocationCode | AGENCY_LOCATION_CODE | — | — |
| 7 | IbyExtBankAccountsBaMaskSetting | BA_MASK_SETTING | — | — |
| 8 | IbyExtBankAccountsBaNumElecSecSegmentId | BA_NUM_ELEC_SEC_SEGMENT_ID | — | — |
| 9 | IbyExtBankAccountsBaNumSecSegmentId | BA_NUM_SEC_SEGMENT_ID | — | — |
| 10 | IbyExtBankAccountsBaUnmaskLength | BA_UNMASK_LENGTH | — | — |
| 11 | IbyExtBankAccountsBankAccountName | BANK_ACCOUNT_NAME | — | — |
| 12 | IbyExtBankAccountsBankAccountNameAlt | BANK_ACCOUNT_NAME_ALT | — | — |
| 13 | IbyExtBankAccountsBankAccountNum | BANK_ACCOUNT_NUM | — | — |
| 14 | IbyExtBankAccountsBankAccountNumElectronic | BANK_ACCOUNT_NUM_ELECTRONIC | — | — |
| 15 | IbyExtBankAccountsBankAccountNumHash1 | BANK_ACCOUNT_NUM_HASH1 | — | — |
| 16 | IbyExtBankAccountsBankAccountNumHash2 | BANK_ACCOUNT_NUM_HASH2 | — | — |
| 17 | IbyExtBankAccountsBankAccountType | BANK_ACCOUNT_TYPE | — | — |
| 18 | IbyExtBankAccountsBankId | BANK_ID | — | — |
| 19 | IbyExtBankAccountsBranchId | BRANCH_ID | — | — |
| 20 | IbyExtBankAccountsCheckDigits | CHECK_DIGITS | — | — |
| 21 | IbyExtBankAccountsCountryCode | COUNTRY_CODE | — | — |
| 22 | IbyExtBankAccountsCurrencyCode | CURRENCY_CODE | — | — |
| 23 | IbyExtBankAccountsDescription | DESCRIPTION | — | — |
| 24 | IbyExtBankAccountsEncrypted | ENCRYPTED | — | — |
| 25 | IbyExtBankAccountsEndDate | END_DATE | — | — |
| 26 | IbyExtBankAccountsExchangeRate | EXCHANGE_RATE | — | — |
| 27 | IbyExtBankAccountsExchangeRateAgreementNum | EXCHANGE_RATE_AGREEMENT_NUM | — | — |
| 28 | IbyExtBankAccountsExchangeRateAgreementType | EXCHANGE_RATE_AGREEMENT_TYPE | — | — |
| 29 | IbyExtBankAccountsExtBankAccountId | EXT_BANK_ACCOUNT_ID | — | — |
| 30 | IbyExtBankAccountsForeignPaymentUseFlag | FOREIGN_PAYMENT_USE_FLAG | — | — |
| 31 | IbyExtBankAccountsHedgingContractReference | HEDGING_CONTRACT_REFERENCE | — | — |
| 32 | IbyExtBankAccountsIban | IBAN | — | — |
| 33 | IbyExtBankAccountsIbanHash1 | IBAN_HASH1 | — | — |
| 34 | IbyExtBankAccountsIbanHash2 | IBAN_HASH2 | — | — |
| 35 | IbyExtBankAccountsIbanSecSegmentId | IBAN_SEC_SEGMENT_ID | — | — |
| 36 | IbyExtBankAccountsMaskedBankAccountNum | MASKED_BANK_ACCOUNT_NUM | — | — |
| 37 | IbyExtBankAccountsMaskedIban | MASKED_IBAN | — | — |
| 38 | IbyExtBankAccountsObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 39 | IbyExtBankAccountsPaymentFactorFlag | PAYMENT_FACTOR_FLAG | — | — |
| 40 | IbyExtBankAccountsProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 41 | IbyExtBankAccountsProgramId | PROGRAM_ID | — | — |
| 42 | IbyExtBankAccountsProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 43 | IbyExtBankAccountsRequestId | REQUEST_ID | — | — |
| 44 | IbyExtBankAccountsSaltVersion | SALT_VERSION | — | — |
| 45 | IbyExtBankAccountsSecondaryAccountReference | SECONDARY_ACCOUNT_REFERENCE | — | — |
| 46 | IbyExtBankAccountsShortAcctName | SHORT_ACCT_NAME | — | — |
| 47 | IbyExtBankAccountsStartDate | START_DATE | — | — |

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

### [[iby_pmt_instr_uses_all|IBY_PMT_INSTR_USES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DraweeToAccountInstrumentId | INSTRUMENT_ID | — | — |
| 2 | DraweeToAccountInstrumentPaymentUseId | INSTRUMENT_PAYMENT_USE_ID | — | — |

### [[iby_trxn_summaries_all|IBY_TRXN_SUMMARIES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IbyTrxnSummaryStatus | STATUS | — | ✅ |
| 2 | IbyTrxnSummaryTrxnmid | TRXNMID | — | — |

### [[inv_units_of_measure_b|INV_UNITS_OF_MEASURE_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UomJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 2 | UomObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 3 | UomUnitOfMeasureId | UNIT_OF_MEASURE_ID | — | — |
| 4 | UomUomCode | UOM_CODE | — | — |

### [[inv_units_of_measure_tl|INV_UNITS_OF_MEASURE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UomDescription | DESCRIPTION | — | — |
| 2 | UomTLLanguage | LANGUAGE | — | — |
| 3 | UomTLUnitOfMeasureId | UNIT_OF_MEASURE_ID | — | — |
| 4 | UomUnitOfMeasure | UNIT_OF_MEASURE | — | — |

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
| 1 | UserCreatedByPersonId | PERSON_ID | — | — |
| 2 | UserCreatedByUserGuid | USER_GUID | — | — |
| 3 | UserCreatedByUserId | USER_ID | — | — |
| 4 | UserCreatedByUsername | USERNAME | — | — |
| 5 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 6 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 7 | UserUpdatedByUserId | USER_ID | — | — |
| 8 | UserUpdatedByUsername | USERNAME | — | — |

### [[ra_batches_all|RA_BATCHES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionBatchBatchBatchId | BATCH_ID | — | — |
| 2 | TransactionBatchBatchBatchProcessStatus | BATCH_PROCESS_STATUS | — | — |
| 3 | TransactionBatchBatchCurrencyCode | CURRENCY_CODE | — | — |
| 4 | TransactionBatchBatchDate | BATCH_DATE | — | — |
| 5 | TransactionBatchBatchId | BATCH_ID | — | ✅ |
| 6 | TransactionBatchBatchName | NAME | — | — |
| 7 | TransactionBatchBatchProcessStatus | BATCH_PROCESS_STATUS | — | — |
| 8 | TransactionBatchBatchSourceId | BATCH_SOURCE_ID | — | — |
| 9 | TransactionBatchBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 10 | TransactionBatchBatchStatus | STATUS | — | — |
| 11 | TransactionBatchBatchType | TYPE | — | — |
| 12 | TransactionBatchComments | COMMENTS | — | — |
| 13 | TransactionBatchControlAmount | CONTROL_AMOUNT | — | — |
| 14 | TransactionBatchControlCount | CONTROL_COUNT | — | — |
| 15 | TransactionBatchCreatedBy | CREATED_BY | — | — |
| 16 | TransactionBatchCreationDate | CREATION_DATE | — | — |
| 17 | TransactionBatchCurrencyCode | CURRENCY_CODE | — | — |
| 18 | TransactionBatchExchangeDate | EXCHANGE_DATE | — | — |
| 19 | TransactionBatchExchangeRate | EXCHANGE_RATE | — | — |
| 20 | TransactionBatchExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 21 | TransactionBatchGlDate | GL_DATE | — | — |
| 22 | TransactionBatchIssueDate | ISSUE_DATE | — | — |
| 23 | TransactionBatchLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | TransactionBatchLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 25 | TransactionBatchLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 26 | TransactionBatchMaturityDate | MATURITY_DATE | — | — |
| 27 | TransactionBatchName | NAME | — | ✅ |
| 28 | TransactionBatchObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 29 | TransactionBatchOrgId | ORG_ID | — | — |
| 30 | TransactionBatchProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 31 | TransactionBatchProgramId | PROGRAM_ID | — | — |
| 32 | TransactionBatchProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 33 | TransactionBatchPurgedChildrenFlag | PURGED_CHILDREN_FLAG | — | — |
| 34 | TransactionBatchRequestId | REQUEST_ID | — | — |
| 35 | TransactionBatchSelectionCriteriaId | SELECTION_CRITERIA_ID | — | — |
| 36 | TransactionBatchSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 37 | TransactionBatchSpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 38 | TransactionBatchStatus | STATUS | — | ✅ |
| 39 | TransactionBatchType | TYPE | — | — |

### [[ra_batch_sources_all|RA_BATCH_SOURCES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BrTrxBatchSourcesBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 2 | BrTrxBatchSourcesDescription | DESCRIPTION | — | ✅ |
| 3 | BrTrxBatchSourcesName | NAME | — | ✅ |
| 4 | TransactionBatchSourceAccountingFlexfieldRule | ACCOUNTING_FLEXFIELD_RULE | — | — |
| 5 | TransactionBatchSourceAccountingRuleRule | ACCOUNTING_RULE_RULE | — | — |
| 6 | TransactionBatchSourceAgreementRule | AGREEMENT_RULE | — | — |
| 7 | TransactionBatchSourceAllowDuplicateTrxNumFlag | ALLOW_DUPLICATE_TRX_NUM_FLAG | — | — |
| 8 | TransactionBatchSourceAllowSalesCreditFlag | ALLOW_SALES_CREDIT_FLAG | — | — |
| 9 | TransactionBatchSourceAutoBatchNumberingFlag | AUTO_BATCH_NUMBERING_FLAG | — | — |
| 10 | TransactionBatchSourceAutoTrxNumberingFlag | AUTO_TRX_NUMBERING_FLAG | — | — |
| 11 | TransactionBatchSourceBatchSourceId | BATCH_SOURCE_ID | — | — |
| 12 | TransactionBatchSourceBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 13 | TransactionBatchSourceBatchSourceType | BATCH_SOURCE_TYPE | — | — |
| 14 | TransactionBatchSourceBillAddressRule | BILL_ADDRESS_RULE | — | — |
| 15 | TransactionBatchSourceBillContactRule | BILL_CONTACT_RULE | — | — |
| 16 | TransactionBatchSourceBillCustomerRule | BILL_CUSTOMER_RULE | — | — |
| 17 | TransactionBatchSourceCmBatchSourceSeqId | CM_BATCH_SOURCE_SEQ_ID | — | — |
| 18 | TransactionBatchSourceCopyDocNumberFlag | COPY_DOC_NUMBER_FLAG | — | — |
| 19 | TransactionBatchSourceCopyInvTidffToCmFlag | COPY_INV_TIDFF_TO_CM_FLAG | — | — |
| 20 | TransactionBatchSourceCreateClearingFlag | CREATE_CLEARING_FLAG | — | — |
| 21 | TransactionBatchSourceCreatedBy | CREATED_BY | — | — |
| 22 | TransactionBatchSourceCreationDate | CREATION_DATE | — | — |
| 23 | TransactionBatchSourceCreditMemoBatchSourceId | CREDIT_MEMO_BATCH_SOURCE_ID | — | — |
| 24 | TransactionBatchSourceCustTrxTypeRule | CUST_TRX_TYPE_RULE | — | — |
| 25 | TransactionBatchSourceCustomerBankAccountRule | CUSTOMER_BANK_ACCOUNT_RULE | — | — |
| 26 | TransactionBatchSourceDefaultInvTrxType | DEFAULT_INV_TRX_TYPE | — | — |
| 27 | TransactionBatchSourceDefaultInvTrxTypeSeqId | DEFAULT_INV_TRX_TYPE_SEQ_ID | — | — |
| 28 | TransactionBatchSourceDefaultReference | DEFAULT_REFERENCE | — | — |
| 29 | TransactionBatchSourceDeriveDateFlag | DERIVE_DATE_FLAG | — | — |
| 30 | TransactionBatchSourceDescription | DESCRIPTION | — | — |
| 31 | TransactionBatchSourceEndDate | END_DATE | — | — |
| 32 | TransactionBatchSourceFobPointRule | FOB_POINT_RULE | — | — |
| 33 | TransactionBatchSourceGlDatePeriodRule | GL_DATE_PERIOD_RULE | — | — |
| 34 | TransactionBatchSourceGroupingRuleId | GROUPING_RULE_ID | — | — |
| 35 | TransactionBatchSourceInvalidLinesRule | INVALID_LINES_RULE | — | — |
| 36 | TransactionBatchSourceInvalidTaxRateRule | INVALID_TAX_RATE_RULE | — | — |
| 37 | TransactionBatchSourceInventoryItemRule | INVENTORY_ITEM_RULE | — | — |
| 38 | TransactionBatchSourceInvoicingRuleRule | INVOICING_RULE_RULE | — | — |
| 39 | TransactionBatchSourceLastBatchNum | LAST_BATCH_NUM | — | — |
| 40 | TransactionBatchSourceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 41 | TransactionBatchSourceLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 42 | TransactionBatchSourceLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 43 | TransactionBatchSourceLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 44 | TransactionBatchSourceMemoLineRule | MEMO_LINE_RULE | — | — |
| 45 | TransactionBatchSourceMemoReasonRule | MEMO_REASON_RULE | — | — |
| 46 | TransactionBatchSourceName | NAME | — | — |
| 47 | TransactionBatchSourceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 48 | TransactionBatchSourceParentAccountingFlexfieldRule | ACCOUNTING_FLEXFIELD_RULE | — | — |
| 49 | TransactionBatchSourceParentAccountingRuleRule | ACCOUNTING_RULE_RULE | — | — |
| 50 | TransactionBatchSourceParentAgreementRule | AGREEMENT_RULE | — | — |
| 51 | TransactionBatchSourceParentAllowDuplicateTrxNumFlag | ALLOW_DUPLICATE_TRX_NUM_FLAG | — | — |
| 52 | TransactionBatchSourceParentAllowSalesCreditFlag | ALLOW_SALES_CREDIT_FLAG | — | — |
| 53 | TransactionBatchSourceParentAutoBatchNumberingFlag | AUTO_BATCH_NUMBERING_FLAG | — | — |
| 54 | TransactionBatchSourceParentAutoTrxNumberingFlag | AUTO_TRX_NUMBERING_FLAG | — | — |
| 55 | TransactionBatchSourceParentBatchSourceId | BATCH_SOURCE_ID | — | — |
| 56 | TransactionBatchSourceParentBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 57 | TransactionBatchSourceParentBatchSourceType | BATCH_SOURCE_TYPE | — | — |
| 58 | TransactionBatchSourceParentBillAddressRule | BILL_ADDRESS_RULE | — | — |
| 59 | TransactionBatchSourceParentBillContactRule | BILL_CONTACT_RULE | — | — |
| 60 | TransactionBatchSourceParentBillCustomerRule | BILL_CUSTOMER_RULE | — | — |
| 61 | TransactionBatchSourceParentCmBatchSourceSeqId | CM_BATCH_SOURCE_SEQ_ID | — | — |
| 62 | TransactionBatchSourceParentCopyDocNumberFlag | COPY_DOC_NUMBER_FLAG | — | — |
| 63 | TransactionBatchSourceParentCopyInvTidffToCmFlag | COPY_INV_TIDFF_TO_CM_FLAG | — | — |
| 64 | TransactionBatchSourceParentCreateClearingFlag | CREATE_CLEARING_FLAG | — | — |
| 65 | TransactionBatchSourceParentCreatedBy | CREATED_BY | — | — |
| 66 | TransactionBatchSourceParentCreationDate | CREATION_DATE | — | — |
| 67 | TransactionBatchSourceParentCreditMemoBatchSourceId | CREDIT_MEMO_BATCH_SOURCE_ID | — | — |
| 68 | TransactionBatchSourceParentCustTrxTypeRule | CUST_TRX_TYPE_RULE | — | — |
| 69 | TransactionBatchSourceParentCustomerBankAccountRule | CUSTOMER_BANK_ACCOUNT_RULE | — | — |
| 70 | TransactionBatchSourceParentDefaultInvTrxType | DEFAULT_INV_TRX_TYPE | — | — |
| 71 | TransactionBatchSourceParentDefaultInvTrxTypeSeqId | DEFAULT_INV_TRX_TYPE_SEQ_ID | — | — |
| 72 | TransactionBatchSourceParentDefaultReference | DEFAULT_REFERENCE | — | — |
| 73 | TransactionBatchSourceParentDeriveDateFlag | DERIVE_DATE_FLAG | — | — |
| 74 | TransactionBatchSourceParentDescription | DESCRIPTION | — | — |
| 75 | TransactionBatchSourceParentEndDate | END_DATE | — | — |
| 76 | TransactionBatchSourceParentFobPointRule | FOB_POINT_RULE | — | — |
| 77 | TransactionBatchSourceParentGlDatePeriodRule | GL_DATE_PERIOD_RULE | — | — |
| 78 | TransactionBatchSourceParentGroupingRuleId | GROUPING_RULE_ID | — | — |
| 79 | TransactionBatchSourceParentInvalidLinesRule | INVALID_LINES_RULE | — | — |
| 80 | TransactionBatchSourceParentInvalidTaxRateRule | INVALID_TAX_RATE_RULE | — | — |
| 81 | TransactionBatchSourceParentInventoryItemRule | INVENTORY_ITEM_RULE | — | — |
| 82 | TransactionBatchSourceParentInvoicingRuleRule | INVOICING_RULE_RULE | — | — |
| 83 | TransactionBatchSourceParentLastBatchNum | LAST_BATCH_NUM | — | — |
| 84 | TransactionBatchSourceParentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 85 | TransactionBatchSourceParentLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 86 | TransactionBatchSourceParentLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 87 | TransactionBatchSourceParentLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 88 | TransactionBatchSourceParentMemoLineRule | MEMO_LINE_RULE | — | — |
| 89 | TransactionBatchSourceParentMemoReasonRule | MEMO_REASON_RULE | — | — |
| 90 | TransactionBatchSourceParentName | NAME | — | — |
| 91 | TransactionBatchSourceParentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 92 | TransactionBatchSourceParentReceiptHandlingOption | RECEIPT_HANDLING_OPTION | — | — |
| 93 | TransactionBatchSourceParentReceiptMethodRule | RECEIPT_METHOD_RULE | — | — |
| 94 | TransactionBatchSourceParentRelatedDocumentRule | RELATED_DOCUMENT_RULE | — | — |
| 95 | TransactionBatchSourceParentRevAccAllocationRule | REV_ACC_ALLOCATION_RULE | — | — |
| 96 | TransactionBatchSourceParentSalesCreditRule | SALES_CREDIT_RULE | — | — |
| 97 | TransactionBatchSourceParentSalesCreditTypeRule | SALES_CREDIT_TYPE_RULE | — | — |
| 98 | TransactionBatchSourceParentSalesTerritoryRule | SALES_TERRITORY_RULE | — | — |
| 99 | TransactionBatchSourceParentSalespersonRule | SALESPERSON_RULE | — | — |
| 100 | TransactionBatchSourceParentSetId | SET_ID | — | — |
| 101 | TransactionBatchSourceParentShipAddressRule | SHIP_ADDRESS_RULE | — | — |
| 102 | TransactionBatchSourceParentShipContactRule | SHIP_CONTACT_RULE | — | — |
| 103 | TransactionBatchSourceParentShipCustomerRule | SHIP_CUSTOMER_RULE | — | — |
| 104 | TransactionBatchSourceParentShipViaRule | SHIP_VIA_RULE | — | — |
| 105 | TransactionBatchSourceParentSoldCustomerRule | SOLD_CUSTOMER_RULE | — | — |
| 106 | TransactionBatchSourceParentStartDate | START_DATE | — | — |
| 107 | TransactionBatchSourceParentStatus | STATUS | — | — |
| 108 | TransactionBatchSourceParentTermRule | TERM_RULE | — | — |
| 109 | TransactionBatchSourceParentUnitOfMeasureRule | UNIT_OF_MEASURE_RULE | — | — |
| 110 | TransactionBatchSourceReceiptHandlingOption | RECEIPT_HANDLING_OPTION | — | — |
| 111 | TransactionBatchSourceReceiptMethodRule | RECEIPT_METHOD_RULE | — | — |
| 112 | TransactionBatchSourceRelatedDocumentRule | RELATED_DOCUMENT_RULE | — | — |
| 113 | TransactionBatchSourceRevAccAllocationRule | REV_ACC_ALLOCATION_RULE | — | — |
| 114 | TransactionBatchSourceSalesCreditRule | SALES_CREDIT_RULE | — | — |
| 115 | TransactionBatchSourceSalesCreditTypeRule | SALES_CREDIT_TYPE_RULE | — | — |
| 116 | TransactionBatchSourceSalesTerritoryRule | SALES_TERRITORY_RULE | — | — |
| 117 | TransactionBatchSourceSalespersonRule | SALESPERSON_RULE | — | — |
| 118 | TransactionBatchSourceSetId | SET_ID | — | — |
| 119 | TransactionBatchSourceShipAddressRule | SHIP_ADDRESS_RULE | — | — |
| 120 | TransactionBatchSourceShipContactRule | SHIP_CONTACT_RULE | — | — |
| 121 | TransactionBatchSourceShipCustomerRule | SHIP_CUSTOMER_RULE | — | — |
| 122 | TransactionBatchSourceShipViaRule | SHIP_VIA_RULE | — | — |
| 123 | TransactionBatchSourceSoldCustomerRule | SOLD_CUSTOMER_RULE | — | — |
| 124 | TransactionBatchSourceStartDate | START_DATE | — | — |
| 125 | TransactionBatchSourceStatus | STATUS | — | — |
| 126 | TransactionBatchSourceTermRule | TERM_RULE | — | — |
| 127 | TransactionBatchSourceUnitOfMeasureRule | UNIT_OF_MEASURE_RULE | — | — |

### [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelCustTrxHdrCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 2 | RelCustTrxHdrTrxNumber | TRX_NUMBER | — | — |
| 3 | TransactionHeaderBrCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 4 | TransactionHeaderBrObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | TransactionHeaderDistAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 6 | TransactionHeaderDistAgreementId | AGREEMENT_ID | — | — |
| 7 | TransactionHeaderDistApplicationId | APPLICATION_ID | — | — |
| 8 | TransactionHeaderDistApprovalCode | APPROVAL_CODE | — | — |
| 9 | TransactionHeaderDistAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 10 | TransactionHeaderDistBatchId | BATCH_ID | — | — |
| 11 | TransactionHeaderDistBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 12 | TransactionHeaderDistBillTemplateId | BILL_TEMPLATE_ID | — | — |
| 13 | TransactionHeaderDistBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 14 | TransactionHeaderDistBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 15 | TransactionHeaderDistBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 16 | TransactionHeaderDistBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 17 | TransactionHeaderDistBillingDate | BILLING_DATE | — | — |
| 18 | TransactionHeaderDistBrAmount | BR_AMOUNT | — | — |
| 19 | TransactionHeaderDistBrOnHoldFlag | BR_ON_HOLD_FLAG | — | ✅ |
| 20 | TransactionHeaderDistBrUnpaidFlag | BR_UNPAID_FLAG | — | — |
| 21 | TransactionHeaderDistCcErrorCode | CC_ERROR_CODE | — | — |
| 22 | TransactionHeaderDistCcErrorFlag | CC_ERROR_FLAG | — | — |
| 23 | TransactionHeaderDistCcErrorText | CC_ERROR_TEXT | — | — |
| 24 | TransactionHeaderDistComments | COMMENTS | — | — |
| 25 | TransactionHeaderDistCompleteFlag | COMPLETE_FLAG | — | ✅ |
| 26 | TransactionHeaderDistContractId | CONTRACT_ID | — | — |
| 27 | TransactionHeaderDistCreatedBy | CREATED_BY | — | — |
| 28 | TransactionHeaderDistCreatedFrom | CREATED_FROM | — | — |
| 29 | TransactionHeaderDistCreationDate | CREATION_DATE | — | — |
| 30 | TransactionHeaderDistCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | — |
| 31 | TransactionHeaderDistCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | — |
| 32 | TransactionHeaderDistCtReference | CT_REFERENCE | — | — |
| 33 | TransactionHeaderDistCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 34 | TransactionHeaderDistCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 35 | TransactionHeaderDistCustomerReference | CUSTOMER_REFERENCE | — | — |
| 36 | TransactionHeaderDistCustomerReferenceDate | CUSTOMER_REFERENCE_DATE | — | — |
| 37 | TransactionHeaderDistCustomerTrxId | CUSTOMER_TRX_ID | — | ✅ |
| 38 | TransactionHeaderDistDefaultTaxExemptFlag | DEFAULT_TAX_EXEMPT_FLAG | — | — |
| 39 | TransactionHeaderDistDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 40 | TransactionHeaderDistDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 41 | TransactionHeaderDistDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 42 | TransactionHeaderDistDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 43 | TransactionHeaderDistDocSequenceValue | DOC_SEQUENCE_VALUE | — | ✅ |
| 44 | TransactionHeaderDistDocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 45 | TransactionHeaderDistDraweeBankAccountId | DRAWEE_BANK_ACCOUNT_ID | — | — |
| 46 | TransactionHeaderDistDraweeContactId | DRAWEE_CONTACT_ID | — | — |
| 47 | TransactionHeaderDistDraweeId | DRAWEE_ID | — | — |
| 48 | TransactionHeaderDistDraweeSiteUseId | DRAWEE_SITE_USE_ID | — | — |
| 49 | TransactionHeaderDistEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 50 | TransactionHeaderDistEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 51 | TransactionHeaderDistEndDateCommitment | END_DATE_COMMITMENT | — | — |
| 52 | TransactionHeaderDistExchangeDate | EXCHANGE_DATE | — | ✅ |
| 53 | TransactionHeaderDistExchangeRate | EXCHANGE_RATE | — | ✅ |
| 54 | TransactionHeaderDistExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 55 | TransactionHeaderDistFinanceCharges | FINANCE_CHARGES | — | ✅ |
| 56 | TransactionHeaderDistFobPoint | FOB_POINT | — | — |
| 57 | TransactionHeaderDistInitialCustomerTrxId | INITIAL_CUSTOMER_TRX_ID | — | — |
| 58 | TransactionHeaderDistIntercompanyFlag | INTERCOMPANY_FLAG | — | ✅ |
| 59 | TransactionHeaderDistInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 60 | TransactionHeaderDistInterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | — |
| 61 | TransactionHeaderDistInterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | — |
| 62 | TransactionHeaderDistInterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | — |
| 63 | TransactionHeaderDistInterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | — |
| 64 | TransactionHeaderDistInterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | — |
| 65 | TransactionHeaderDistInterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | — |
| 66 | TransactionHeaderDistInterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | — |
| 67 | TransactionHeaderDistInterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | — |
| 68 | TransactionHeaderDistInterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | — |
| 69 | TransactionHeaderDistInterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | — |
| 70 | TransactionHeaderDistInterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | — |
| 71 | TransactionHeaderDistInterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | — |
| 72 | TransactionHeaderDistInterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | — |
| 73 | TransactionHeaderDistInterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | — |
| 74 | TransactionHeaderDistInterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | — |
| 75 | TransactionHeaderDistInterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | — |
| 76 | TransactionHeaderDistInternalNotes | INTERNAL_NOTES | — | — |
| 77 | TransactionHeaderDistInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 78 | TransactionHeaderDistInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 79 | TransactionHeaderDistLastPrintedSequenceNum | LAST_PRINTED_SEQUENCE_NUM | — | — |
| 80 | TransactionHeaderDistLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 81 | TransactionHeaderDistLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 82 | TransactionHeaderDistLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 83 | TransactionHeaderDistLateChargesAssessed | LATE_CHARGES_ASSESSED | — | ✅ |
| 84 | TransactionHeaderDistLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 85 | TransactionHeaderDistObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 86 | TransactionHeaderDistOldTrxNumber | OLD_TRX_NUMBER | — | — |
| 87 | TransactionHeaderDistOrgId | ORG_ID | — | — |
| 88 | TransactionHeaderDistOrigSystemBatchName | ORIG_SYSTEM_BATCH_NAME | — | — |
| 89 | TransactionHeaderDistOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 90 | TransactionHeaderDistPayingCustomerId | PAYING_CUSTOMER_ID | — | — |
| 91 | TransactionHeaderDistPayingSiteUseId | PAYING_SITE_USE_ID | — | — |
| 92 | TransactionHeaderDistPaymentAttributes | PAYMENT_ATTRIBUTES | — | — |
| 93 | TransactionHeaderDistPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 94 | TransactionHeaderDistPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 95 | TransactionHeaderDistPostRequestId | POST_REQUEST_ID | — | — |
| 96 | TransactionHeaderDistPostingControlId | POSTING_CONTROL_ID | — | — |
| 97 | TransactionHeaderDistPrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 98 | TransactionHeaderDistPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 99 | TransactionHeaderDistPrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | — |
| 100 | TransactionHeaderDistPrintingCount | PRINTING_COUNT | — | — |
| 101 | TransactionHeaderDistPrintingLastPrinted | PRINTING_LAST_PRINTED | — | ✅ |
| 102 | TransactionHeaderDistPrintingOption | PRINTING_OPTION | — | — |
| 103 | TransactionHeaderDistPrintingOriginalDate | PRINTING_ORIGINAL_DATE | — | — |
| 104 | TransactionHeaderDistPrintingPending | PRINTING_PENDING | — | — |
| 105 | TransactionHeaderDistProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 106 | TransactionHeaderDistProgramId | PROGRAM_ID | — | — |
| 107 | TransactionHeaderDistProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 108 | TransactionHeaderDistPurchaseOrder | PURCHASE_ORDER | — | — |
| 109 | TransactionHeaderDistPurchaseOrderDate | PURCHASE_ORDER_DATE | — | — |
| 110 | TransactionHeaderDistPurchaseOrderRevision | PURCHASE_ORDER_REVISION | — | — |
| 111 | TransactionHeaderDistRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 112 | TransactionHeaderDistReasonCode | REASON_CODE | — | — |
| 113 | TransactionHeaderDistReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 114 | TransactionHeaderDistRecurredFromTrxNumber | RECURRED_FROM_TRX_NUMBER | — | — |
| 115 | TransactionHeaderDistRelatedBatchSourceSeqId | RELATED_BATCH_SOURCE_SEQ_ID | — | — |
| 116 | TransactionHeaderDistRelatedCustomerTrxId | RELATED_CUSTOMER_TRX_ID | — | — |
| 117 | TransactionHeaderDistRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 118 | TransactionHeaderDistRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 119 | TransactionHeaderDistRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 120 | TransactionHeaderDistRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 121 | TransactionHeaderDistRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 122 | TransactionHeaderDistRequestId | REQUEST_ID | — | — |
| 123 | TransactionHeaderDistRequiresManualScheduling | REQUIRES_MANUAL_SCHEDULING | — | — |
| 124 | TransactionHeaderDistReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 125 | TransactionHeaderDistSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 126 | TransactionHeaderDistShipDateActual | SHIP_DATE_ACTUAL | — | — |
| 127 | TransactionHeaderDistShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 128 | TransactionHeaderDistShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 129 | TransactionHeaderDistShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 130 | TransactionHeaderDistShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 131 | TransactionHeaderDistShipVia | SHIP_VIA | — | — |
| 132 | TransactionHeaderDistShipmentId | SHIPMENT_ID | — | — |
| 133 | TransactionHeaderDistSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 134 | TransactionHeaderDistSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 135 | TransactionHeaderDistSoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | — |
| 136 | TransactionHeaderDistSourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 137 | TransactionHeaderDistSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 138 | TransactionHeaderDistSpecialInstructions | SPECIAL_INSTRUCTIONS | — | ✅ |
| 139 | TransactionHeaderDistStartDateCommitment | START_DATE_COMMITMENT | — | — |
| 140 | TransactionHeaderDistStatusTrx | STATUS_TRX | — | — |
| 141 | TransactionHeaderDistTermDueDate | TERM_DUE_DATE | — | — |
| 142 | TransactionHeaderDistTermId | TERM_ID | — | — |
| 143 | TransactionHeaderDistTerritoryId | TERRITORY_ID | — | — |
| 144 | TransactionHeaderDistTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 145 | TransactionHeaderDistTrxClass | TRX_CLASS | — | — |
| 146 | TransactionHeaderDistTrxDate | TRX_DATE | — | ✅ |
| 147 | TransactionHeaderDistTrxNumber | TRX_NUMBER | — | ✅ |
| 148 | TransactionHeaderDistUpgradeMethod | UPGRADE_METHOD | — | — |
| 149 | TransactionHeaderDistUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 150 | TransactionHeaderDistWaybillNumber | WAYBILL_NUMBER | — | — |
| 151 | TransactionHeaderDistWhUpdateDate | WH_UPDATE_DATE | — | — |
| 152 | TrxHeaderPrevAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 153 | TrxHeaderPrevAgreementId | AGREEMENT_ID | — | — |
| 154 | TrxHeaderPrevApplicationId | APPLICATION_ID | — | — |
| 155 | TrxHeaderPrevApprovalCode | APPROVAL_CODE | — | — |
| 156 | TrxHeaderPrevAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 157 | TrxHeaderPrevBatchId | BATCH_ID | — | — |
| 158 | TrxHeaderPrevBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 159 | TrxHeaderPrevBillTemplateId | BILL_TEMPLATE_ID | — | — |
| 160 | TrxHeaderPrevBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 161 | TrxHeaderPrevBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 162 | TrxHeaderPrevBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 163 | TrxHeaderPrevBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 164 | TrxHeaderPrevBillingDate | BILLING_DATE | — | — |
| 165 | TrxHeaderPrevBrAmount | BR_AMOUNT | — | — |
| 166 | TrxHeaderPrevBrOnHoldFlag | BR_ON_HOLD_FLAG | — | — |
| 167 | TrxHeaderPrevBrUnpaidFlag | BR_UNPAID_FLAG | — | — |
| 168 | TrxHeaderPrevCcErrorCode | CC_ERROR_CODE | — | — |
| 169 | TrxHeaderPrevCcErrorFlag | CC_ERROR_FLAG | — | — |
| 170 | TrxHeaderPrevCcErrorText | CC_ERROR_TEXT | — | — |
| 171 | TrxHeaderPrevComments | COMMENTS | — | — |
| 172 | TrxHeaderPrevCompleteFlag | COMPLETE_FLAG | — | — |
| 173 | TrxHeaderPrevContractId | CONTRACT_ID | — | — |
| 174 | TrxHeaderPrevCreatedBy | CREATED_BY | — | — |
| 175 | TrxHeaderPrevCreatedFrom | CREATED_FROM | — | — |
| 176 | TrxHeaderPrevCreationDate | CREATION_DATE | — | — |
| 177 | TrxHeaderPrevCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | — |
| 178 | TrxHeaderPrevCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | — |
| 179 | TrxHeaderPrevCtReference | CT_REFERENCE | — | — |
| 180 | TrxHeaderPrevCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 181 | TrxHeaderPrevCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 182 | TrxHeaderPrevCustomerReference | CUSTOMER_REFERENCE | — | — |
| 183 | TrxHeaderPrevCustomerReferenceDate | CUSTOMER_REFERENCE_DATE | — | — |
| 184 | TrxHeaderPrevCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 185 | TrxHeaderPrevDefaultTaxExemptFlag | DEFAULT_TAX_EXEMPT_FLAG | — | — |
| 186 | TrxHeaderPrevDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 187 | TrxHeaderPrevDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 188 | TrxHeaderPrevDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 189 | TrxHeaderPrevDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 190 | TrxHeaderPrevDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 191 | TrxHeaderPrevDocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 192 | TrxHeaderPrevDraweeBankAccountId | DRAWEE_BANK_ACCOUNT_ID | — | — |
| 193 | TrxHeaderPrevDraweeContactId | DRAWEE_CONTACT_ID | — | — |
| 194 | TrxHeaderPrevDraweeId | DRAWEE_ID | — | — |
| 195 | TrxHeaderPrevDraweeSiteUseId | DRAWEE_SITE_USE_ID | — | — |
| 196 | TrxHeaderPrevEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 197 | TrxHeaderPrevEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 198 | TrxHeaderPrevEndDateCommitment | END_DATE_COMMITMENT | — | — |
| 199 | TrxHeaderPrevExchangeDate | EXCHANGE_DATE | — | — |
| 200 | TrxHeaderPrevExchangeRate | EXCHANGE_RATE | — | — |
| 201 | TrxHeaderPrevExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 202 | TrxHeaderPrevFinanceCharges | FINANCE_CHARGES | — | — |
| 203 | TrxHeaderPrevFobPoint | FOB_POINT | — | — |
| 204 | TrxHeaderPrevInitialCustomerTrxId | INITIAL_CUSTOMER_TRX_ID | — | — |
| 205 | TrxHeaderPrevIntercompanyFlag | INTERCOMPANY_FLAG | — | — |
| 206 | TrxHeaderPrevInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 207 | TrxHeaderPrevInterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | — |
| 208 | TrxHeaderPrevInterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | — |
| 209 | TrxHeaderPrevInterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | — |
| 210 | TrxHeaderPrevInterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | — |
| 211 | TrxHeaderPrevInterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | — |
| 212 | TrxHeaderPrevInterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | — |
| 213 | TrxHeaderPrevInterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | — |
| 214 | TrxHeaderPrevInterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | — |
| 215 | TrxHeaderPrevInterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | — |
| 216 | TrxHeaderPrevInterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | — |
| 217 | TrxHeaderPrevInterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | — |
| 218 | TrxHeaderPrevInterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | — |
| 219 | TrxHeaderPrevInterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | — |
| 220 | TrxHeaderPrevInterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | — |
| 221 | TrxHeaderPrevInterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | — |
| 222 | TrxHeaderPrevInterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | — |
| 223 | TrxHeaderPrevInternalNotes | INTERNAL_NOTES | — | — |
| 224 | TrxHeaderPrevInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 225 | TrxHeaderPrevInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 226 | TrxHeaderPrevLastPrintedSequenceNum | LAST_PRINTED_SEQUENCE_NUM | — | — |
| 227 | TrxHeaderPrevLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 228 | TrxHeaderPrevLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 229 | TrxHeaderPrevLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 230 | TrxHeaderPrevLateChargesAssessed | LATE_CHARGES_ASSESSED | — | — |
| 231 | TrxHeaderPrevLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 232 | TrxHeaderPrevObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 233 | TrxHeaderPrevOldTrxNumber | OLD_TRX_NUMBER | — | — |
| 234 | TrxHeaderPrevOrgId | ORG_ID | — | — |
| 235 | TrxHeaderPrevOrigSystemBatchName | ORIG_SYSTEM_BATCH_NAME | — | — |
| 236 | TrxHeaderPrevOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 237 | TrxHeaderPrevPayingCustomerId | PAYING_CUSTOMER_ID | — | — |
| 238 | TrxHeaderPrevPayingSiteUseId | PAYING_SITE_USE_ID | — | — |
| 239 | TrxHeaderPrevPaymentAttributes | PAYMENT_ATTRIBUTES | — | — |
| 240 | TrxHeaderPrevPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 241 | TrxHeaderPrevPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 242 | TrxHeaderPrevPostRequestId | POST_REQUEST_ID | — | — |
| 243 | TrxHeaderPrevPostingControlId | POSTING_CONTROL_ID | — | — |
| 244 | TrxHeaderPrevPrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 245 | TrxHeaderPrevPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 246 | TrxHeaderPrevPrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | — |
| 247 | TrxHeaderPrevPrintingCount | PRINTING_COUNT | — | — |
| 248 | TrxHeaderPrevPrintingLastPrinted | PRINTING_LAST_PRINTED | — | — |
| 249 | TrxHeaderPrevPrintingOption | PRINTING_OPTION | — | — |
| 250 | TrxHeaderPrevPrintingOriginalDate | PRINTING_ORIGINAL_DATE | — | — |
| 251 | TrxHeaderPrevPrintingPending | PRINTING_PENDING | — | — |
| 252 | TrxHeaderPrevProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 253 | TrxHeaderPrevProgramId | PROGRAM_ID | — | — |
| 254 | TrxHeaderPrevProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 255 | TrxHeaderPrevPurchaseOrder | PURCHASE_ORDER | — | — |
| 256 | TrxHeaderPrevPurchaseOrderDate | PURCHASE_ORDER_DATE | — | — |
| 257 | TrxHeaderPrevPurchaseOrderRevision | PURCHASE_ORDER_REVISION | — | — |
| 258 | TrxHeaderPrevRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 259 | TrxHeaderPrevReasonCode | REASON_CODE | — | — |
| 260 | TrxHeaderPrevReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 261 | TrxHeaderPrevRecurredFromTrxNumber | RECURRED_FROM_TRX_NUMBER | — | — |
| 262 | TrxHeaderPrevRelatedBatchSourceSeqId | RELATED_BATCH_SOURCE_SEQ_ID | — | — |
| 263 | TrxHeaderPrevRelatedCustomerTrxId | RELATED_CUSTOMER_TRX_ID | — | — |
| 264 | TrxHeaderPrevRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 265 | TrxHeaderPrevRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 266 | TrxHeaderPrevRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 267 | TrxHeaderPrevRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 268 | TrxHeaderPrevRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 269 | TrxHeaderPrevRequestId | REQUEST_ID | — | — |
| 270 | TrxHeaderPrevRequiresManualScheduling | REQUIRES_MANUAL_SCHEDULING | — | — |
| 271 | TrxHeaderPrevReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 272 | TrxHeaderPrevSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 273 | TrxHeaderPrevShipDateActual | SHIP_DATE_ACTUAL | — | — |
| 274 | TrxHeaderPrevShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 275 | TrxHeaderPrevShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 276 | TrxHeaderPrevShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 277 | TrxHeaderPrevShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 278 | TrxHeaderPrevShipVia | SHIP_VIA | — | — |
| 279 | TrxHeaderPrevShipmentId | SHIPMENT_ID | — | — |
| 280 | TrxHeaderPrevSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 281 | TrxHeaderPrevSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 282 | TrxHeaderPrevSoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | — |
| 283 | TrxHeaderPrevSourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 284 | TrxHeaderPrevSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 285 | TrxHeaderPrevSpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 286 | TrxHeaderPrevStartDateCommitment | START_DATE_COMMITMENT | — | — |
| 287 | TrxHeaderPrevStatusTrx | STATUS_TRX | — | — |
| 288 | TrxHeaderPrevTermDueDate | TERM_DUE_DATE | — | — |
| 289 | TrxHeaderPrevTermId | TERM_ID | — | — |
| 290 | TrxHeaderPrevTerritoryId | TERRITORY_ID | — | — |
| 291 | TrxHeaderPrevTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 292 | TrxHeaderPrevTrxClass | TRX_CLASS | — | — |
| 293 | TrxHeaderPrevTrxDate | TRX_DATE | — | — |
| 294 | TrxHeaderPrevTrxNumber | TRX_NUMBER | — | — |
| 295 | TrxHeaderPrevUpgradeMethod | UPGRADE_METHOD | — | — |
| 296 | TrxHeaderPrevUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 297 | TrxHeaderPrevWaybillNumber | WAYBILL_NUMBER | — | — |
| 298 | TrxHeaderPrevWhUpdateDate | WH_UPDATE_DATE | — | — |

### [[ra_customer_trx_lines_all|RA_CUSTOMER_TRX_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionLineAccountingRuleDuration | ACCOUNTING_RULE_DURATION | — | — |
| 2 | TransactionLineAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 3 | TransactionLineAcctdAmountDueOriginal | ACCTD_AMOUNT_DUE_ORIGINAL | — | — |
| 4 | TransactionLineAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | — |
| 5 | TransactionLineAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 6 | TransactionLineAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 7 | TransactionLineAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 8 | TransactionLineAssessableValue | ASSESSABLE_VALUE | — | — |
| 9 | TransactionLineAutoruleCompleteFlag | AUTORULE_COMPLETE_FLAG | — | — |
| 10 | TransactionLineAutoruleDurationProcessed | AUTORULE_DURATION_PROCESSED | — | — |
| 11 | TransactionLineAutotax | AUTOTAX | — | — |
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
| 24 | TransactionLineDeferralExclusionFlag | DEFERRAL_EXCLUSION_FLAG | — | — |
| 25 | TransactionLineDescription | DESCRIPTION | — | — |
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
| 36 | TransactionLineGrossUnitSellingPrice | GROSS_UNIT_SELLING_PRICE | — | — |
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
| 189 | TransactionLineInterfaceLineAttribute1 | INTERFACE_LINE_ATTRIBUTE1 | — | — |
| 190 | TransactionLineInterfaceLineAttribute10 | INTERFACE_LINE_ATTRIBUTE10 | — | — |
| 191 | TransactionLineInterfaceLineAttribute11 | INTERFACE_LINE_ATTRIBUTE11 | — | — |
| 192 | TransactionLineInterfaceLineAttribute12 | INTERFACE_LINE_ATTRIBUTE12 | — | — |
| 193 | TransactionLineInterfaceLineAttribute13 | INTERFACE_LINE_ATTRIBUTE13 | — | — |
| 194 | TransactionLineInterfaceLineAttribute14 | INTERFACE_LINE_ATTRIBUTE14 | — | — |
| 195 | TransactionLineInterfaceLineAttribute15 | INTERFACE_LINE_ATTRIBUTE15 | — | — |
| 196 | TransactionLineInterfaceLineAttribute2 | INTERFACE_LINE_ATTRIBUTE2 | — | — |
| 197 | TransactionLineInterfaceLineAttribute3 | INTERFACE_LINE_ATTRIBUTE3 | — | — |
| 198 | TransactionLineInterfaceLineAttribute4 | INTERFACE_LINE_ATTRIBUTE4 | — | — |
| 199 | TransactionLineInterfaceLineAttribute5 | INTERFACE_LINE_ATTRIBUTE5 | — | — |
| 200 | TransactionLineInterfaceLineAttribute6 | INTERFACE_LINE_ATTRIBUTE6 | — | — |
| 201 | TransactionLineInterfaceLineAttribute7 | INTERFACE_LINE_ATTRIBUTE7 | — | — |
| 202 | TransactionLineInterfaceLineAttribute8 | INTERFACE_LINE_ATTRIBUTE8 | — | — |
| 203 | TransactionLineInterfaceLineAttribute9 | INTERFACE_LINE_ATTRIBUTE9 | — | — |
| 204 | TransactionLineInterfaceLineContext | INTERFACE_LINE_CONTEXT | — | — |
| 205 | TransactionLineInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 206 | TransactionLineInvoicedLineAcctgLevel | INVOICED_LINE_ACCTG_LEVEL | — | — |
| 207 | TransactionLineItemContext | ITEM_CONTEXT | — | — |
| 208 | TransactionLineItemExceptionRateId | ITEM_EXCEPTION_RATE_ID | — | — |
| 209 | TransactionLineLastPeriodToCredit | LAST_PERIOD_TO_CREDIT | — | — |
| 210 | TransactionLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 211 | TransactionLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 212 | TransactionLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 213 | TransactionLineLineIntendedUse | LINE_INTENDED_USE | — | — |
| 214 | TransactionLineLineNumber | LINE_NUMBER | — | — |
| 215 | TransactionLineLineRecoverable | LINE_RECOVERABLE | — | — |
| 216 | TransactionLineLineType | LINE_TYPE | — | — |
| 217 | TransactionLineLinkToCustTrxLineId | LINK_TO_CUST_TRX_LINE_ID | — | — |
| 218 | TransactionLineLinkToParentlineAttribute1 | LINK_TO_PARENTLINE_ATTRIBUTE1 | — | — |
| 219 | TransactionLineLinkToParentlineAttribute10 | LINK_TO_PARENTLINE_ATTRIBUTE10 | — | — |
| 220 | TransactionLineLinkToParentlineAttribute11 | LINK_TO_PARENTLINE_ATTRIBUTE11 | — | — |
| 221 | TransactionLineLinkToParentlineAttribute12 | LINK_TO_PARENTLINE_ATTRIBUTE12 | — | — |
| 222 | TransactionLineLinkToParentlineAttribute13 | LINK_TO_PARENTLINE_ATTRIBUTE13 | — | — |
| 223 | TransactionLineLinkToParentlineAttribute14 | LINK_TO_PARENTLINE_ATTRIBUTE14 | — | — |
| 224 | TransactionLineLinkToParentlineAttribute15 | LINK_TO_PARENTLINE_ATTRIBUTE15 | — | — |
| 225 | TransactionLineLinkToParentlineAttribute2 | LINK_TO_PARENTLINE_ATTRIBUTE2 | — | — |
| 226 | TransactionLineLinkToParentlineAttribute3 | LINK_TO_PARENTLINE_ATTRIBUTE3 | — | — |
| 227 | TransactionLineLinkToParentlineAttribute4 | LINK_TO_PARENTLINE_ATTRIBUTE4 | — | — |
| 228 | TransactionLineLinkToParentlineAttribute5 | LINK_TO_PARENTLINE_ATTRIBUTE5 | — | — |
| 229 | TransactionLineLinkToParentlineAttribute6 | LINK_TO_PARENTLINE_ATTRIBUTE6 | — | — |
| 230 | TransactionLineLinkToParentlineAttribute7 | LINK_TO_PARENTLINE_ATTRIBUTE7 | — | — |
| 231 | TransactionLineLinkToParentlineAttribute8 | LINK_TO_PARENTLINE_ATTRIBUTE8 | — | — |
| 232 | TransactionLineLinkToParentlineAttribute9 | LINK_TO_PARENTLINE_ATTRIBUTE9 | — | — |
| 233 | TransactionLineLinkToParentlineContext | LINK_TO_PARENTLINE_CONTEXT | — | — |
| 234 | TransactionLineLocationSegmentId | LOCATION_SEGMENT_ID | — | — |
| 235 | TransactionLineMemoLineSeqId | MEMO_LINE_SEQ_ID | — | — |
| 236 | TransactionLineMovementId | MOVEMENT_ID | — | — |
| 237 | TransactionLineMrcExtendedAcctdAmount | MRC_EXTENDED_ACCTD_AMOUNT | — | — |
| 238 | TransactionLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 239 | TransactionLineOrgId | ORG_ID | — | — |
| 240 | TransactionLineOverrideAutoAccountingFlag | OVERRIDE_AUTO_ACCOUNTING_FLAG | — | — |
| 241 | TransactionLinePaymentSetId | PAYMENT_SET_ID | — | — |
| 242 | TransactionLinePaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 243 | TransactionLineProductCategory | PRODUCT_CATEGORY | — | — |
| 244 | TransactionLineProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | — |
| 245 | TransactionLineProductType | PRODUCT_TYPE | — | — |
| 246 | TransactionLineProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 247 | TransactionLineProgramId | PROGRAM_ID | — | — |
| 248 | TransactionLineProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 249 | TransactionLinePrvAccountingRuleDuration | ACCOUNTING_RULE_DURATION | — | — |
| 250 | TransactionLinePrvAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 251 | TransactionLinePrvAcctdAmountDueOriginal | ACCTD_AMOUNT_DUE_ORIGINAL | — | — |
| 252 | TransactionLinePrvAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | — |
| 253 | TransactionLinePrvAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 254 | TransactionLinePrvAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 255 | TransactionLinePrvAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 256 | TransactionLinePrvAssessableValue | ASSESSABLE_VALUE | — | — |
| 257 | TransactionLinePrvAutoruleCompleteFlag | AUTORULE_COMPLETE_FLAG | — | — |
| 258 | TransactionLinePrvAutoruleDurationProcessed | AUTORULE_DURATION_PROCESSED | — | — |
| 259 | TransactionLinePrvAutotax | AUTOTAX | — | — |
| 260 | TransactionLinePrvBrAdjustmentId | BR_ADJUSTMENT_ID | — | — |
| 261 | TransactionLinePrvBrRefCustomerTrxId | BR_REF_CUSTOMER_TRX_ID | — | — |
| 262 | TransactionLinePrvBrRefPaymentScheduleId | BR_REF_PAYMENT_SCHEDULE_ID | — | — |
| 263 | TransactionLinePrvChrgAcctdAmountRemaining | CHRG_ACCTD_AMOUNT_REMAINING | — | — |
| 264 | TransactionLinePrvChrgAmountRemaining | CHRG_AMOUNT_REMAINING | — | — |
| 265 | TransactionLinePrvContractLineId | CONTRACT_LINE_ID | — | — |
| 266 | TransactionLinePrvCreatedBy | CREATED_BY | — | — |
| 267 | TransactionLinePrvCreationDate | CREATION_DATE | — | — |
| 268 | TransactionLinePrvCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 269 | TransactionLinePrvCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 270 | TransactionLinePrvObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 271 | TransactionLineQuantityCredited | QUANTITY_CREDITED | — | — |
| 272 | TransactionLineQuantityInvoiced | QUANTITY_INVOICED | — | — |
| 273 | TransactionLineQuantityOrdered | QUANTITY_ORDERED | — | — |
| 274 | TransactionLineReasonCode | REASON_CODE | — | — |
| 275 | TransactionLineRequestId | REQUEST_ID | — | — |
| 276 | TransactionLineRevenueAmount | REVENUE_AMOUNT | — | — |
| 277 | TransactionLineRuleEndDate | RULE_END_DATE | — | — |
| 278 | TransactionLineRuleStartDate | RULE_START_DATE | — | — |
| 279 | TransactionLineSalesOrder | SALES_ORDER | — | — |
| 280 | TransactionLineSalesOrderDate | SALES_ORDER_DATE | — | — |
| 281 | TransactionLineSalesOrderLine | SALES_ORDER_LINE | — | — |
| 282 | TransactionLineSalesOrderRevision | SALES_ORDER_REVISION | — | — |
| 283 | TransactionLineSalesOrderSource | SALES_ORDER_SOURCE | — | — |
| 284 | TransactionLineSalesTaxId | SALES_TAX_ID | — | — |
| 285 | TransactionLineSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 286 | TransactionLineShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 287 | TransactionLineShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 288 | TransactionLineShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 289 | TransactionLineShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 290 | TransactionLineSourceDataKey1 | SOURCE_DATA_KEY1 | — | — |
| 291 | TransactionLineSourceDataKey2 | SOURCE_DATA_KEY2 | — | — |
| 292 | TransactionLineSourceDataKey3 | SOURCE_DATA_KEY3 | — | — |
| 293 | TransactionLineSourceDataKey4 | SOURCE_DATA_KEY4 | — | — |
| 294 | TransactionLineSourceDataKey5 | SOURCE_DATA_KEY5 | — | — |
| 295 | TransactionLineSourceDocumentLineId | SOURCE_DOCUMENT_LINE_ID | — | — |
| 296 | TransactionLineSourceDocumentLineNumber | SOURCE_DOCUMENT_LINE_NUMBER | — | — |
| 297 | TransactionLineTaxAction | TAX_ACTION | — | — |
| 298 | TransactionLineTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 299 | TransactionLineTaxExemptFlag | TAX_EXEMPT_FLAG | — | — |
| 300 | TransactionLineTaxExemptNumber | TAX_EXEMPT_NUMBER | — | — |
| 301 | TransactionLineTaxExemptReasonCode | TAX_EXEMPT_REASON_CODE | — | — |
| 302 | TransactionLineTaxExemptionId | TAX_EXEMPTION_ID | — | — |
| 303 | TransactionLineTaxLineId | TAX_LINE_ID | — | — |
| 304 | TransactionLineTaxPrecedence | TAX_PRECEDENCE | — | — |
| 305 | TransactionLineTaxRate | TAX_RATE | — | — |
| 306 | TransactionLineTaxRecoverable | TAX_RECOVERABLE | — | — |
| 307 | TransactionLineTaxVendorReturnCode | TAX_VENDOR_RETURN_CODE | — | — |
| 308 | TransactionLineTaxableAmount | TAXABLE_AMOUNT | — | — |
| 309 | TransactionLineTaxableFlag | TAXABLE_FLAG | — | — |
| 310 | TransactionLineTranslatedDescription | TRANSLATED_DESCRIPTION | — | — |
| 311 | TransactionLineTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 312 | TransactionLineUnitSellingPrice | UNIT_SELLING_PRICE | — | — |
| 313 | TransactionLineUnitStandardPrice | UNIT_STANDARD_PRICE | — | — |
| 314 | TransactionLineUomCode | UOM_CODE | — | — |
| 315 | TransactionLineUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 316 | TransactionLineVatTaxId | VAT_TAX_ID | — | — |
| 317 | TransactionLineWarehouseId | WAREHOUSE_ID | — | — |
| 318 | TransactionLineWhUpdateDate | WH_UPDATE_DATE | — | — |

### [[ra_rules|RA_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvDistRuleDescription | DESCRIPTION | — | — |
| 2 | InvDistRuleName | NAME | — | — |
| 3 | InvDistRuleObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 4 | InvDistRuleRuleId | RULE_ID | — | — |

### [[zx_fc_intended_use_v|ZX_FC_INTENDED_USE_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LnIntndUseClassificationId | CLASSIFICATION_ID | — | — |
| 2 | LnIntndUseCode | CODE | — | — |
| 3 | LnIntndUseCountryCode | COUNTRY_CODE | — | — |
| 4 | LnIntndUseName | NAME | — | — |

### [[zx_fc_product_categories_v|ZX_FC_PRODUCT_CATEGORIES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProdCatClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | ProdCatClassificationId | CLASSIFICATION_ID | — | — |
| 3 | ProdCatClassificationName | CLASSIFICATION_NAME | — | — |
| 4 | ProdCatConcatLeafCode | CONCAT_LEAF_CODE | — | — |
| 5 | ProdCatConcatLeafName | CONCAT_LEAF_NAME | — | — |
| 6 | ProdCatCountryCode | COUNTRY_CODE | — | — |

### [[zx_fc_product_fiscal_v|ZX_FC_PRODUCT_FISCAL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProdFiscClsCategoryId | CATEGORY_ID | — | — |
| 2 | ProdFiscClsCategorySetId | CATEGORY_SET_ID | — | — |
| 3 | ProdFiscClsClassificationCode | CLASSIFICATION_CODE | — | — |
| 4 | ProdFiscClsClassificationName | CLASSIFICATION_NAME | — | — |
| 5 | ProdFiscClsCountryCode | COUNTRY_CODE | — | — |
| 6 | ProdFiscClsEffectiveTo | EFFECTIVE_TO | — | — |
| 7 | ProdFiscClsStructureId | STRUCTURE_ID | — | — |
| 8 | ProdFiscClsStructureName | STRUCTURE_NAME | — | — |

### [[zx_fc_user_defined_v|ZX_FC_USER_DEFINED_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LineUsrDfndFiscClsClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | LineUsrDfndFiscClsClassificationName | CLASSIFICATION_NAME | — | — |
| 3 | LineUsrDfndFiscClsCountryCode | COUNTRY_CODE | — | — |
| 4 | UsrDfndFiscClsClassificationCode | CLASSIFICATION_CODE | — | — |
| 5 | UsrDfndFiscClsClassificationName | CLASSIFICATION_NAME | — | — |
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
| 65 | DtlTaxLineObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
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
| 165 | TaxLineIdTaxLineId | TAX_LINE_ID | — | — |

### [[zx_product_types_v|ZX_PRODUCT_TYPES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProdTypeClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | ProdTypeClassificationName | CLASSIFICATION_NAME | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
