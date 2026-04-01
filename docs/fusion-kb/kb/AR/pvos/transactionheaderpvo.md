---
id: DOC-AR-PVO-TransactionHeaderPVO
doc_type: system-doc
title: "TransactionHeaderPVO — PVO Accounts Receivable"
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
  - TransactionHeaderPVO
  - transactionheaderpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionHeaderPVO

## 📌 Visão Geral

Extrai os cabeçalhos das transações de Contas a Receber (faturas, notas de débito/crédito), incluindo cliente, valor total, data, condições de pagamento, endereço e classificação. Central para análise de faturamento, aging, inadimplência e relacionamento com clientes.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.TransactionHeaderPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 936 | 28 | 1 | 123 | 13% |

---

## 🔗 Tabelas Relacionadas

- [[ar_batches_all|AR_BATCHES_ALL]] — 41 atributos
- [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]] — 5 atributos (1 BICC)
- [[ar_interest_headers_all|AR_INTEREST_HEADERS_ALL]] — 35 atributos
- [[ar_lookups|AR_LOOKUPS]] — 4 atributos (2 BICC)
- [[ar_payment_schedules_all|AR_PAYMENT_SCHEDULES_ALL]] — 93 atributos
- [[ce_bank_acct_uses_all|CE_BANK_ACCT_USES_ALL]] — 25 atributos
- [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]] — 5 atributos (1 BICC)
- [[fnd_territories_vl|FND_TERRITORIES_VL]] — 9 atributos (1 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 2 atributos (1 BICC)
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 13 atributos (1 BICC)
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 71 atributos (6 BICC)
- [[hz_cust_account_roles|HZ_CUST_ACCOUNT_ROLES]] — 2 atributos
- [[hz_cust_acct_sites_all|HZ_CUST_ACCT_SITES_ALL]] — 15 atributos
- [[hz_cust_site_uses_all|HZ_CUST_SITE_USES_ALL]] — 6 atributos
- [[hz_locations|HZ_LOCATIONS]] — 26 atributos (20 BICC)
- [[hz_parties|HZ_PARTIES]] — 27 atributos (3 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 12 atributos (3 BICC)
- [[hz_party_site_uses|HZ_PARTY_SITE_USES]] — 3 atributos (1 BICC)
- [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]] — 49 atributos (3 BICC)
- [[iby_fndcpt_tx_extensions|IBY_FNDCPT_TX_EXTENSIONS]] — 14 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos
- [[per_users|PER_USERS]] — 9 atributos
- [[ra_batches_all|RA_BATCHES_ALL]] — 27 atributos
- [[ra_batch_sources_all|RA_BATCH_SOURCES_ALL]] — 114 atributos (1 BICC)
- [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]] — 306 atributos (1 PKs, 74 BICC)
- [[ra_rules|RA_RULES]] — 4 atributos (1 BICC)
- [[zx_fc_user_defined_v|ZX_FC_USER_DEFINED_V]] — 3 atributos (1 BICC)
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
| 11 | ReceiptBatchCurrencyCode | CURRENCY_CODE | — | — |
| 12 | ReceiptBatchDepositDate | DEPOSIT_DATE | — | — |
| 13 | ReceiptBatchExchangeDate | EXCHANGE_DATE | — | — |
| 14 | ReceiptBatchExchangeRate | EXCHANGE_RATE | — | — |
| 15 | ReceiptBatchExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 16 | ReceiptBatchGlDate | GL_DATE | — | — |
| 17 | ReceiptBatchLockboxBatchName | LOCKBOX_BATCH_NAME | — | — |
| 18 | ReceiptBatchLockboxId | LOCKBOX_ID | — | — |
| 19 | ReceiptBatchMediaReference | MEDIA_REFERENCE | — | — |
| 20 | ReceiptBatchName | NAME | — | — |
| 21 | ReceiptBatchObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | ReceiptBatchOldRemittanceBankBranchId | OLD_REMITTANCE_BANK_BRANCH_ID | — | — |
| 23 | ReceiptBatchOperationRequestId | OPERATION_REQUEST_ID | — | — |
| 24 | ReceiptBatchOrgId | ORG_ID | — | — |
| 25 | ReceiptBatchProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 26 | ReceiptBatchProgramId | PROGRAM_ID | — | — |
| 27 | ReceiptBatchProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 28 | ReceiptBatchPurgedChildrenFlag | PURGED_CHILDREN_FLAG | — | — |
| 29 | ReceiptBatchReceiptClassId | RECEIPT_CLASS_ID | — | — |
| 30 | ReceiptBatchReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 31 | ReceiptBatchRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 32 | ReceiptBatchRemitMethodCode | REMIT_METHOD_CODE | — | — |
| 33 | ReceiptBatchRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 34 | ReceiptBatchRemittanceBankBranchId | REMITTANCE_BANK_BRANCH_ID | — | — |
| 35 | ReceiptBatchRequestId | REQUEST_ID | — | — |
| 36 | ReceiptBatchSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 37 | ReceiptBatchStatus | STATUS | — | — |
| 38 | ReceiptBatchTransmissionId | TRANSMISSION_ID | — | — |
| 39 | ReceiptBatchTransmissionRequestId | TRANSMISSION_REQUEST_ID | — | — |
| 40 | ReceiptBatchType | TYPE | — | — |
| 41 | ReceiptBatchWithRecourseFlag | WITH_RECOURSE_FLAG | — | — |

### [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RevCashRcptCashReceiptId | CASH_RECEIPT_ID | — | — |
| 2 | RevCashRcptComments | COMMENTS | — | — |
| 3 | RevCashRcptIssuerName | ISSUER_NAME | — | — |
| 4 | RevCashRcptObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | RevCashRcptReceiptNumber | RECEIPT_NUMBER | — | ✅ |

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

### [[ar_lookups|AR_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrxClassDescription | DESCRIPTION | — | — |
| 2 | TrxClassLookupCode | LOOKUP_CODE | — | ✅ |
| 3 | TrxClassLookupType | LOOKUP_TYPE | — | — |
| 4 | TrxClassMeaning | MEANING | — | ✅ |

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
| 63 | PaymentScheduleLastUpdateDate | LAST_UPDATE_DATE | — | — |
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
| 2 | BusinessUnitName | BU_NAME | — | ✅ |

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
| 9 | DailyConversionTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | DailyConversionTypePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 11 | DailyConversionTypeSecurityFlag | SECURITY_FLAG | — | — |
| 12 | DailyConversionTypeUserConversionType | USER_CONVERSION_TYPE | — | ✅ |
| 13 | DailyConversionTypeUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |

### [[hz_cust_accounts|HZ_CUST_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustAcctAccountEstablishedDate | ACCOUNT_ESTABLISHED_DATE | — | — |
| 2 | CustAcctAccountName | ACCOUNT_NAME | — | — |
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
| 9 | TransactionBatchCurrencyCode | CURRENCY_CODE | — | — |
| 10 | TransactionBatchExchangeDate | EXCHANGE_DATE | — | — |
| 11 | TransactionBatchExchangeRate | EXCHANGE_RATE | — | — |
| 12 | TransactionBatchExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 13 | TransactionBatchGlDate | GL_DATE | — | — |
| 14 | TransactionBatchIssueDate | ISSUE_DATE | — | — |
| 15 | TransactionBatchMaturityDate | MATURITY_DATE | — | — |
| 16 | TransactionBatchName | NAME | — | — |
| 17 | TransactionBatchOrgId | ORG_ID | — | — |
| 18 | TransactionBatchProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 19 | TransactionBatchProgramId | PROGRAM_ID | — | — |
| 20 | TransactionBatchProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 21 | TransactionBatchPurgedChildrenFlag | PURGED_CHILDREN_FLAG | — | — |
| 22 | TransactionBatchRequestId | REQUEST_ID | — | — |
| 23 | TransactionBatchSelectionCriteriaId | SELECTION_CRITERIA_ID | — | — |
| 24 | TransactionBatchSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 25 | TransactionBatchSpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 26 | TransactionBatchStatus | STATUS | — | — |
| 27 | TransactionBatchType | TYPE | — | — |

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
| 18 | TransactionBatchSourceCreditMemoBatchSourceId | CREDIT_MEMO_BATCH_SOURCE_ID | — | — |
| 19 | TransactionBatchSourceCustTrxTypeRule | CUST_TRX_TYPE_RULE | — | — |
| 20 | TransactionBatchSourceCustomerBankAccountRule | CUSTOMER_BANK_ACCOUNT_RULE | — | — |
| 21 | TransactionBatchSourceDefaultInvTrxType | DEFAULT_INV_TRX_TYPE | — | — |
| 22 | TransactionBatchSourceDefaultInvTrxTypeSeqId | DEFAULT_INV_TRX_TYPE_SEQ_ID | — | — |
| 23 | TransactionBatchSourceDefaultReference | DEFAULT_REFERENCE | — | — |
| 24 | TransactionBatchSourceDeriveDateFlag | DERIVE_DATE_FLAG | — | — |
| 25 | TransactionBatchSourceDescription | DESCRIPTION | — | — |
| 26 | TransactionBatchSourceEndDate | END_DATE | — | — |
| 27 | TransactionBatchSourceFobPointRule | FOB_POINT_RULE | — | — |
| 28 | TransactionBatchSourceGlDatePeriodRule | GL_DATE_PERIOD_RULE | — | — |
| 29 | TransactionBatchSourceGroupingRuleId | GROUPING_RULE_ID | — | — |
| 30 | TransactionBatchSourceInvalidLinesRule | INVALID_LINES_RULE | — | — |
| 31 | TransactionBatchSourceInvalidTaxRateRule | INVALID_TAX_RATE_RULE | — | — |
| 32 | TransactionBatchSourceInventoryItemRule | INVENTORY_ITEM_RULE | — | — |
| 33 | TransactionBatchSourceInvoicingRuleRule | INVOICING_RULE_RULE | — | — |
| 34 | TransactionBatchSourceLastBatchNum | LAST_BATCH_NUM | — | — |
| 35 | TransactionBatchSourceLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 36 | TransactionBatchSourceMemoLineRule | MEMO_LINE_RULE | — | — |
| 37 | TransactionBatchSourceMemoReasonRule | MEMO_REASON_RULE | — | — |
| 38 | TransactionBatchSourceName | NAME | — | ✅ |
| 39 | TransactionBatchSourceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 40 | TransactionBatchSourceParentAccountingFlexfieldRule | ACCOUNTING_FLEXFIELD_RULE | — | — |
| 41 | TransactionBatchSourceParentAccountingRuleRule | ACCOUNTING_RULE_RULE | — | — |
| 42 | TransactionBatchSourceParentAgreementRule | AGREEMENT_RULE | — | — |
| 43 | TransactionBatchSourceParentAllowDuplicateTrxNumFlag | ALLOW_DUPLICATE_TRX_NUM_FLAG | — | — |
| 44 | TransactionBatchSourceParentAllowSalesCreditFlag | ALLOW_SALES_CREDIT_FLAG | — | — |
| 45 | TransactionBatchSourceParentAutoBatchNumberingFlag | AUTO_BATCH_NUMBERING_FLAG | — | — |
| 46 | TransactionBatchSourceParentAutoTrxNumberingFlag | AUTO_TRX_NUMBERING_FLAG | — | — |
| 47 | TransactionBatchSourceParentBatchSourceId | BATCH_SOURCE_ID | — | — |
| 48 | TransactionBatchSourceParentBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 49 | TransactionBatchSourceParentBatchSourceType | BATCH_SOURCE_TYPE | — | — |
| 50 | TransactionBatchSourceParentBillAddressRule | BILL_ADDRESS_RULE | — | — |
| 51 | TransactionBatchSourceParentBillContactRule | BILL_CONTACT_RULE | — | — |
| 52 | TransactionBatchSourceParentBillCustomerRule | BILL_CUSTOMER_RULE | — | — |
| 53 | TransactionBatchSourceParentCmBatchSourceSeqId | CM_BATCH_SOURCE_SEQ_ID | — | — |
| 54 | TransactionBatchSourceParentCopyDocNumberFlag | COPY_DOC_NUMBER_FLAG | — | — |
| 55 | TransactionBatchSourceParentCopyInvTidffToCmFlag | COPY_INV_TIDFF_TO_CM_FLAG | — | — |
| 56 | TransactionBatchSourceParentCreateClearingFlag | CREATE_CLEARING_FLAG | — | — |
| 57 | TransactionBatchSourceParentCreditMemoBatchSourceId | CREDIT_MEMO_BATCH_SOURCE_ID | — | — |
| 58 | TransactionBatchSourceParentCustTrxTypeRule | CUST_TRX_TYPE_RULE | — | — |
| 59 | TransactionBatchSourceParentCustomerBankAccountRule | CUSTOMER_BANK_ACCOUNT_RULE | — | — |
| 60 | TransactionBatchSourceParentDefaultInvTrxType | DEFAULT_INV_TRX_TYPE | — | — |
| 61 | TransactionBatchSourceParentDefaultInvTrxTypeSeqId | DEFAULT_INV_TRX_TYPE_SEQ_ID | — | — |
| 62 | TransactionBatchSourceParentDefaultReference | DEFAULT_REFERENCE | — | — |
| 63 | TransactionBatchSourceParentDeriveDateFlag | DERIVE_DATE_FLAG | — | — |
| 64 | TransactionBatchSourceParentDescription | DESCRIPTION | — | — |
| 65 | TransactionBatchSourceParentEndDate | END_DATE | — | — |
| 66 | TransactionBatchSourceParentFobPointRule | FOB_POINT_RULE | — | — |
| 67 | TransactionBatchSourceParentGlDatePeriodRule | GL_DATE_PERIOD_RULE | — | — |
| 68 | TransactionBatchSourceParentGroupingRuleId | GROUPING_RULE_ID | — | — |
| 69 | TransactionBatchSourceParentInvalidLinesRule | INVALID_LINES_RULE | — | — |
| 70 | TransactionBatchSourceParentInvalidTaxRateRule | INVALID_TAX_RATE_RULE | — | — |
| 71 | TransactionBatchSourceParentInventoryItemRule | INVENTORY_ITEM_RULE | — | — |
| 72 | TransactionBatchSourceParentInvoicingRuleRule | INVOICING_RULE_RULE | — | — |
| 73 | TransactionBatchSourceParentLastBatchNum | LAST_BATCH_NUM | — | — |
| 74 | TransactionBatchSourceParentLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 75 | TransactionBatchSourceParentMemoLineRule | MEMO_LINE_RULE | — | — |
| 76 | TransactionBatchSourceParentMemoReasonRule | MEMO_REASON_RULE | — | — |
| 77 | TransactionBatchSourceParentName | NAME | — | — |
| 78 | TransactionBatchSourceParentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 79 | TransactionBatchSourceParentReceiptHandlingOption | RECEIPT_HANDLING_OPTION | — | — |
| 80 | TransactionBatchSourceParentReceiptMethodRule | RECEIPT_METHOD_RULE | — | — |
| 81 | TransactionBatchSourceParentRelatedDocumentRule | RELATED_DOCUMENT_RULE | — | — |
| 82 | TransactionBatchSourceParentRevAccAllocationRule | REV_ACC_ALLOCATION_RULE | — | — |
| 83 | TransactionBatchSourceParentSalesCreditRule | SALES_CREDIT_RULE | — | — |
| 84 | TransactionBatchSourceParentSalesCreditTypeRule | SALES_CREDIT_TYPE_RULE | — | — |
| 85 | TransactionBatchSourceParentSalesTerritoryRule | SALES_TERRITORY_RULE | — | — |
| 86 | TransactionBatchSourceParentSalespersonRule | SALESPERSON_RULE | — | — |
| 87 | TransactionBatchSourceParentSetId | SET_ID | — | — |
| 88 | TransactionBatchSourceParentShipAddressRule | SHIP_ADDRESS_RULE | — | — |
| 89 | TransactionBatchSourceParentShipContactRule | SHIP_CONTACT_RULE | — | — |
| 90 | TransactionBatchSourceParentShipCustomerRule | SHIP_CUSTOMER_RULE | — | — |
| 91 | TransactionBatchSourceParentShipViaRule | SHIP_VIA_RULE | — | — |
| 92 | TransactionBatchSourceParentSoldCustomerRule | SOLD_CUSTOMER_RULE | — | — |
| 93 | TransactionBatchSourceParentStartDate | START_DATE | — | — |
| 94 | TransactionBatchSourceParentStatus | STATUS | — | — |
| 95 | TransactionBatchSourceParentTermRule | TERM_RULE | — | — |
| 96 | TransactionBatchSourceParentUnitOfMeasureRule | UNIT_OF_MEASURE_RULE | — | — |
| 97 | TransactionBatchSourceReceiptHandlingOption | RECEIPT_HANDLING_OPTION | — | — |
| 98 | TransactionBatchSourceReceiptMethodRule | RECEIPT_METHOD_RULE | — | — |
| 99 | TransactionBatchSourceRelatedDocumentRule | RELATED_DOCUMENT_RULE | — | — |
| 100 | TransactionBatchSourceRevAccAllocationRule | REV_ACC_ALLOCATION_RULE | — | — |
| 101 | TransactionBatchSourceSalesCreditRule | SALES_CREDIT_RULE | — | — |
| 102 | TransactionBatchSourceSalesCreditTypeRule | SALES_CREDIT_TYPE_RULE | — | — |
| 103 | TransactionBatchSourceSalesTerritoryRule | SALES_TERRITORY_RULE | — | — |
| 104 | TransactionBatchSourceSalespersonRule | SALESPERSON_RULE | — | — |
| 105 | TransactionBatchSourceSetId | SET_ID | — | — |
| 106 | TransactionBatchSourceShipAddressRule | SHIP_ADDRESS_RULE | — | — |
| 107 | TransactionBatchSourceShipContactRule | SHIP_CONTACT_RULE | — | — |
| 108 | TransactionBatchSourceShipCustomerRule | SHIP_CUSTOMER_RULE | — | — |
| 109 | TransactionBatchSourceShipViaRule | SHIP_VIA_RULE | — | — |
| 110 | TransactionBatchSourceSoldCustomerRule | SOLD_CUSTOMER_RULE | — | — |
| 111 | TransactionBatchSourceStartDate | START_DATE | — | — |
| 112 | TransactionBatchSourceStatus | STATUS | — | — |
| 113 | TransactionBatchSourceTermRule | TERM_RULE | — | — |
| 114 | TransactionBatchSourceUnitOfMeasureRule | UNIT_OF_MEASURE_RULE | — | — |

### [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ControlCompletionReasonCode | CONTROL_COMPLETION_REASON_CODE | — | — |
| 2 | CustomerTrxId | CUSTOMER_TRX_ID | 🔑 | ✅ |
| 3 | RelCustTrxHdrCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 4 | RelCustTrxHdrObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | RelCustTrxHdrTrxNumber | TRX_NUMBER | — | ✅ |
| 6 | TransactionHeaderAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 7 | TransactionHeaderAgreementId | AGREEMENT_ID | — | — |
| 8 | TransactionHeaderApplicationId | APPLICATION_ID | — | — |
| 9 | TransactionHeaderApprovalCode | APPROVAL_CODE | — | — |
| 10 | TransactionHeaderAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 11 | TransactionHeaderBatchId | BATCH_ID | — | — |
| 12 | TransactionHeaderBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 13 | TransactionHeaderBillTemplateId | BILL_TEMPLATE_ID | — | ✅ |
| 14 | TransactionHeaderBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 15 | TransactionHeaderBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 16 | TransactionHeaderBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 17 | TransactionHeaderBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 18 | TransactionHeaderBillingDate | BILLING_DATE | — | ✅ |
| 19 | TransactionHeaderBrAmount | BR_AMOUNT | — | ✅ |
| 20 | TransactionHeaderBrOnHoldFlag | BR_ON_HOLD_FLAG | — | ✅ |
| 21 | TransactionHeaderBrUnpaidFlag | BR_UNPAID_FLAG | — | — |
| 22 | TransactionHeaderCcErrorCode | CC_ERROR_CODE | — | — |
| 23 | TransactionHeaderCcErrorFlag | CC_ERROR_FLAG | — | — |
| 24 | TransactionHeaderCcErrorText | CC_ERROR_TEXT | — | — |
| 25 | TransactionHeaderComments | COMMENTS | — | ✅ |
| 26 | TransactionHeaderCompleteFlag | COMPLETE_FLAG | — | ✅ |
| 27 | TransactionHeaderContractId | CONTRACT_ID | — | — |
| 28 | TransactionHeaderCreatedBy | CREATED_BY | — | ✅ |
| 29 | TransactionHeaderCreatedFrom | CREATED_FROM | — | ✅ |
| 30 | TransactionHeaderCreationDate | CREATION_DATE | — | ✅ |
| 31 | TransactionHeaderCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | ✅ |
| 32 | TransactionHeaderCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | ✅ |
| 33 | TransactionHeaderCtReference | CT_REFERENCE | — | ✅ |
| 34 | TransactionHeaderCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 35 | TransactionHeaderCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 36 | TransactionHeaderCustomerReference | CUSTOMER_REFERENCE | — | ✅ |
| 37 | TransactionHeaderCustomerReferenceDate | CUSTOMER_REFERENCE_DATE | — | ✅ |
| 38 | TransactionHeaderDefaultTaxExemptFlag | DEFAULT_TAX_EXEMPT_FLAG | — | ✅ |
| 39 | TransactionHeaderDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | ✅ |
| 40 | TransactionHeaderDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 41 | TransactionHeaderDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 42 | TransactionHeaderDelContactEmailAddress | DEL_CONTACT_EMAIL_ADDRESS | — | — |
| 43 | TransactionHeaderDeliveryMethodCode | DELIVERY_METHOD_CODE | — | — |
| 44 | TransactionHeaderDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 45 | TransactionHeaderDocSequenceValue | DOC_SEQUENCE_VALUE | — | ✅ |
| 46 | TransactionHeaderDocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 47 | TransactionHeaderDraweeBankAccountId | DRAWEE_BANK_ACCOUNT_ID | — | — |
| 48 | TransactionHeaderDraweeContactId | DRAWEE_CONTACT_ID | — | — |
| 49 | TransactionHeaderDraweeId | DRAWEE_ID | — | — |
| 50 | TransactionHeaderDraweeSiteUseId | DRAWEE_SITE_USE_ID | — | — |
| 51 | TransactionHeaderEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 52 | TransactionHeaderEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 53 | TransactionHeaderEndDateCommitment | END_DATE_COMMITMENT | — | ✅ |
| 54 | TransactionHeaderExchangeDate | EXCHANGE_DATE | — | ✅ |
| 55 | TransactionHeaderExchangeRate | EXCHANGE_RATE | — | ✅ |
| 56 | TransactionHeaderExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 57 | TransactionHeaderFinanceCharges | FINANCE_CHARGES | — | ✅ |
| 58 | TransactionHeaderFobPoint | FOB_POINT | — | ✅ |
| 59 | TransactionHeaderInitialCustomerTrxId | INITIAL_CUSTOMER_TRX_ID | — | — |
| 60 | TransactionHeaderIntercompanyFlag | INTERCOMPANY_FLAG | — | ✅ |
| 61 | TransactionHeaderInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 62 | TransactionHeaderInterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | ✅ |
| 63 | TransactionHeaderInterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | ✅ |
| 64 | TransactionHeaderInterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | ✅ |
| 65 | TransactionHeaderInterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | ✅ |
| 66 | TransactionHeaderInterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | ✅ |
| 67 | TransactionHeaderInterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | ✅ |
| 68 | TransactionHeaderInterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | ✅ |
| 69 | TransactionHeaderInterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | ✅ |
| 70 | TransactionHeaderInterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | ✅ |
| 71 | TransactionHeaderInterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | ✅ |
| 72 | TransactionHeaderInterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | ✅ |
| 73 | TransactionHeaderInterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | ✅ |
| 74 | TransactionHeaderInterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | ✅ |
| 75 | TransactionHeaderInterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | ✅ |
| 76 | TransactionHeaderInterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | ✅ |
| 77 | TransactionHeaderInterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | ✅ |
| 78 | TransactionHeaderInternalNotes | INTERNAL_NOTES | — | ✅ |
| 79 | TransactionHeaderInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 80 | TransactionHeaderInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 81 | TransactionHeaderLastPrintedSequenceNum | LAST_PRINTED_SEQUENCE_NUM | — | ✅ |
| 82 | TransactionHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 83 | TransactionHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 84 | TransactionHeaderLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 85 | TransactionHeaderLateChargesAssessed | LATE_CHARGES_ASSESSED | — | ✅ |
| 86 | TransactionHeaderLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 87 | TransactionHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 88 | TransactionHeaderOldTrxNumber | OLD_TRX_NUMBER | — | — |
| 89 | TransactionHeaderOrgId | ORG_ID | — | — |
| 90 | TransactionHeaderOrigSystemBatchName | ORIG_SYSTEM_BATCH_NAME | — | ✅ |
| 91 | TransactionHeaderOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 92 | TransactionHeaderPayingCustomerId | PAYING_CUSTOMER_ID | — | — |
| 93 | TransactionHeaderPayingSiteUseId | PAYING_SITE_USE_ID | — | — |
| 94 | TransactionHeaderPaymentAttributes | PAYMENT_ATTRIBUTES | — | — |
| 95 | TransactionHeaderPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 96 | TransactionHeaderPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 97 | TransactionHeaderPostRequestId | POST_REQUEST_ID | — | — |
| 98 | TransactionHeaderPostingControlId | POSTING_CONTROL_ID | — | — |
| 99 | TransactionHeaderPrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 100 | TransactionHeaderPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 101 | TransactionHeaderPrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | — |
| 102 | TransactionHeaderPrintingCount | PRINTING_COUNT | — | ✅ |
| 103 | TransactionHeaderPrintingLastPrinted | PRINTING_LAST_PRINTED | — | ✅ |
| 104 | TransactionHeaderPrintingOption | PRINTING_OPTION | — | ✅ |
| 105 | TransactionHeaderPrintingOriginalDate | PRINTING_ORIGINAL_DATE | — | ✅ |
| 106 | TransactionHeaderPrintingPending | PRINTING_PENDING | — | ✅ |
| 107 | TransactionHeaderProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 108 | TransactionHeaderProgramId | PROGRAM_ID | — | — |
| 109 | TransactionHeaderProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 110 | TransactionHeaderPurchaseOrder | PURCHASE_ORDER | — | ✅ |
| 111 | TransactionHeaderPurchaseOrderDate | PURCHASE_ORDER_DATE | — | ✅ |
| 112 | TransactionHeaderPurchaseOrderRevision | PURCHASE_ORDER_REVISION | — | ✅ |
| 113 | TransactionHeaderRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 114 | TransactionHeaderReasonCode | REASON_CODE | — | ✅ |
| 115 | TransactionHeaderReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 116 | TransactionHeaderRecurredFromTrxNumber | RECURRED_FROM_TRX_NUMBER | — | — |
| 117 | TransactionHeaderRelatedBatchSourceSeqId | RELATED_BATCH_SOURCE_SEQ_ID | — | — |
| 118 | TransactionHeaderRelatedCustomerTrxId | RELATED_CUSTOMER_TRX_ID | — | — |
| 119 | TransactionHeaderRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 120 | TransactionHeaderRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 121 | TransactionHeaderRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 122 | TransactionHeaderRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 123 | TransactionHeaderRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 124 | TransactionHeaderRequestId | REQUEST_ID | — | — |
| 125 | TransactionHeaderRequiresManualScheduling | REQUIRES_MANUAL_SCHEDULING | — | ✅ |
| 126 | TransactionHeaderRevRecApplication | REV_REC_APPLICATION | — | ✅ |
| 127 | TransactionHeaderReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 128 | TransactionHeaderSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 129 | TransactionHeaderShipDateActual | SHIP_DATE_ACTUAL | — | ✅ |
| 130 | TransactionHeaderShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 131 | TransactionHeaderShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 132 | TransactionHeaderShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 133 | TransactionHeaderShipToPartyAddressId | SHIP_TO_PARTY_ADDRESS_ID | — | — |
| 134 | TransactionHeaderShipToPartyContactId | SHIP_TO_PARTY_CONTACT_ID | — | — |
| 135 | TransactionHeaderShipToPartyId | SHIP_TO_PARTY_ID | — | — |
| 136 | TransactionHeaderShipToPartySiteUseId | SHIP_TO_PARTY_SITE_USE_ID | — | — |
| 137 | TransactionHeaderShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 138 | TransactionHeaderShipVia | SHIP_VIA | — | ✅ |
| 139 | TransactionHeaderShipmentId | SHIPMENT_ID | — | — |
| 140 | TransactionHeaderSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 141 | TransactionHeaderSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 142 | TransactionHeaderSoldToPartyId | SOLD_TO_PARTY_ID | — | — |
| 143 | TransactionHeaderSoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | — |
| 144 | TransactionHeaderSourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 145 | TransactionHeaderSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 146 | TransactionHeaderSpecialInstructions | SPECIAL_INSTRUCTIONS | — | ✅ |
| 147 | TransactionHeaderStartDateCommitment | START_DATE_COMMITMENT | — | ✅ |
| 148 | TransactionHeaderStatusTrx | STATUS_TRX | — | ✅ |
| 149 | TransactionHeaderTermDueDate | TERM_DUE_DATE | — | ✅ |
| 150 | TransactionHeaderTermId | TERM_ID | — | — |
| 151 | TransactionHeaderTerritoryId | TERRITORY_ID | — | — |
| 152 | TransactionHeaderTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 153 | TransactionHeaderTrxClass | TRX_CLASS | — | ✅ |
| 154 | TransactionHeaderTrxDate | TRX_DATE | — | ✅ |
| 155 | TransactionHeaderTrxNumber | TRX_NUMBER | — | ✅ |
| 156 | TransactionHeaderUpgradeMethod | UPGRADE_METHOD | — | — |
| 157 | TransactionHeaderUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | ✅ |
| 158 | TransactionHeaderWaybillNumber | WAYBILL_NUMBER | — | ✅ |
| 159 | TransactionHeaderWhUpdateDate | WH_UPDATE_DATE | — | — |
| 160 | TrxHeaderPrevAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 161 | TrxHeaderPrevAgreementId | AGREEMENT_ID | — | — |
| 162 | TrxHeaderPrevApplicationId | APPLICATION_ID | — | — |
| 163 | TrxHeaderPrevApprovalCode | APPROVAL_CODE | — | — |
| 164 | TrxHeaderPrevAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 165 | TrxHeaderPrevBatchId | BATCH_ID | — | — |
| 166 | TrxHeaderPrevBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 167 | TrxHeaderPrevBillTemplateId | BILL_TEMPLATE_ID | — | — |
| 168 | TrxHeaderPrevBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 169 | TrxHeaderPrevBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 170 | TrxHeaderPrevBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 171 | TrxHeaderPrevBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 172 | TrxHeaderPrevBillingDate | BILLING_DATE | — | — |
| 173 | TrxHeaderPrevBrAmount | BR_AMOUNT | — | — |
| 174 | TrxHeaderPrevBrOnHoldFlag | BR_ON_HOLD_FLAG | — | — |
| 175 | TrxHeaderPrevBrUnpaidFlag | BR_UNPAID_FLAG | — | — |
| 176 | TrxHeaderPrevCcErrorCode | CC_ERROR_CODE | — | — |
| 177 | TrxHeaderPrevCcErrorFlag | CC_ERROR_FLAG | — | — |
| 178 | TrxHeaderPrevCcErrorText | CC_ERROR_TEXT | — | — |
| 179 | TrxHeaderPrevComments | COMMENTS | — | — |
| 180 | TrxHeaderPrevCompleteFlag | COMPLETE_FLAG | — | — |
| 181 | TrxHeaderPrevContractId | CONTRACT_ID | — | — |
| 182 | TrxHeaderPrevCreatedBy | CREATED_BY | — | — |
| 183 | TrxHeaderPrevCreatedFrom | CREATED_FROM | — | — |
| 184 | TrxHeaderPrevCreationDate | CREATION_DATE | — | — |
| 185 | TrxHeaderPrevCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | — |
| 186 | TrxHeaderPrevCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | — |
| 187 | TrxHeaderPrevCtReference | CT_REFERENCE | — | — |
| 188 | TrxHeaderPrevCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 189 | TrxHeaderPrevCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 190 | TrxHeaderPrevCustomerReference | CUSTOMER_REFERENCE | — | — |
| 191 | TrxHeaderPrevCustomerReferenceDate | CUSTOMER_REFERENCE_DATE | — | — |
| 192 | TrxHeaderPrevCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 193 | TrxHeaderPrevDefaultTaxExemptFlag | DEFAULT_TAX_EXEMPT_FLAG | — | — |
| 194 | TrxHeaderPrevDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 195 | TrxHeaderPrevDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 196 | TrxHeaderPrevDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 197 | TrxHeaderPrevDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 198 | TrxHeaderPrevDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 199 | TrxHeaderPrevDocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 200 | TrxHeaderPrevDraweeBankAccountId | DRAWEE_BANK_ACCOUNT_ID | — | — |
| 201 | TrxHeaderPrevDraweeContactId | DRAWEE_CONTACT_ID | — | — |
| 202 | TrxHeaderPrevDraweeId | DRAWEE_ID | — | — |
| 203 | TrxHeaderPrevDraweeSiteUseId | DRAWEE_SITE_USE_ID | — | — |
| 204 | TrxHeaderPrevEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 205 | TrxHeaderPrevEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 206 | TrxHeaderPrevEndDateCommitment | END_DATE_COMMITMENT | — | — |
| 207 | TrxHeaderPrevExchangeDate | EXCHANGE_DATE | — | — |
| 208 | TrxHeaderPrevExchangeRate | EXCHANGE_RATE | — | — |
| 209 | TrxHeaderPrevExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 210 | TrxHeaderPrevFinanceCharges | FINANCE_CHARGES | — | — |
| 211 | TrxHeaderPrevFobPoint | FOB_POINT | — | — |
| 212 | TrxHeaderPrevInitialCustomerTrxId | INITIAL_CUSTOMER_TRX_ID | — | — |
| 213 | TrxHeaderPrevIntercompanyFlag | INTERCOMPANY_FLAG | — | — |
| 214 | TrxHeaderPrevInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 215 | TrxHeaderPrevInterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | — |
| 216 | TrxHeaderPrevInterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | — |
| 217 | TrxHeaderPrevInterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | — |
| 218 | TrxHeaderPrevInterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | — |
| 219 | TrxHeaderPrevInterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | — |
| 220 | TrxHeaderPrevInterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | — |
| 221 | TrxHeaderPrevInterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | — |
| 222 | TrxHeaderPrevInterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | — |
| 223 | TrxHeaderPrevInterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | — |
| 224 | TrxHeaderPrevInterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | — |
| 225 | TrxHeaderPrevInterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | — |
| 226 | TrxHeaderPrevInterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | — |
| 227 | TrxHeaderPrevInterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | — |
| 228 | TrxHeaderPrevInterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | — |
| 229 | TrxHeaderPrevInterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | — |
| 230 | TrxHeaderPrevInterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | — |
| 231 | TrxHeaderPrevInternalNotes | INTERNAL_NOTES | — | — |
| 232 | TrxHeaderPrevInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 233 | TrxHeaderPrevInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 234 | TrxHeaderPrevLastPrintedSequenceNum | LAST_PRINTED_SEQUENCE_NUM | — | — |
| 235 | TrxHeaderPrevLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 236 | TrxHeaderPrevLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 237 | TrxHeaderPrevLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 238 | TrxHeaderPrevLateChargesAssessed | LATE_CHARGES_ASSESSED | — | — |
| 239 | TrxHeaderPrevLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 240 | TrxHeaderPrevObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 241 | TrxHeaderPrevOldTrxNumber | OLD_TRX_NUMBER | — | — |
| 242 | TrxHeaderPrevOrgId | ORG_ID | — | — |
| 243 | TrxHeaderPrevOrigSystemBatchName | ORIG_SYSTEM_BATCH_NAME | — | — |
| 244 | TrxHeaderPrevOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 245 | TrxHeaderPrevPayingCustomerId | PAYING_CUSTOMER_ID | — | — |
| 246 | TrxHeaderPrevPayingSiteUseId | PAYING_SITE_USE_ID | — | — |
| 247 | TrxHeaderPrevPaymentAttributes | PAYMENT_ATTRIBUTES | — | — |
| 248 | TrxHeaderPrevPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 249 | TrxHeaderPrevPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 250 | TrxHeaderPrevPostRequestId | POST_REQUEST_ID | — | — |
| 251 | TrxHeaderPrevPostingControlId | POSTING_CONTROL_ID | — | — |
| 252 | TrxHeaderPrevPrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 253 | TrxHeaderPrevPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 254 | TrxHeaderPrevPrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | — |
| 255 | TrxHeaderPrevPrintingCount | PRINTING_COUNT | — | — |
| 256 | TrxHeaderPrevPrintingLastPrinted | PRINTING_LAST_PRINTED | — | — |
| 257 | TrxHeaderPrevPrintingOption | PRINTING_OPTION | — | — |
| 258 | TrxHeaderPrevPrintingOriginalDate | PRINTING_ORIGINAL_DATE | — | — |
| 259 | TrxHeaderPrevPrintingPending | PRINTING_PENDING | — | — |
| 260 | TrxHeaderPrevProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 261 | TrxHeaderPrevProgramId | PROGRAM_ID | — | — |
| 262 | TrxHeaderPrevProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 263 | TrxHeaderPrevPurchaseOrder | PURCHASE_ORDER | — | — |
| 264 | TrxHeaderPrevPurchaseOrderDate | PURCHASE_ORDER_DATE | — | — |
| 265 | TrxHeaderPrevPurchaseOrderRevision | PURCHASE_ORDER_REVISION | — | — |
| 266 | TrxHeaderPrevRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 267 | TrxHeaderPrevReasonCode | REASON_CODE | — | — |
| 268 | TrxHeaderPrevReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 269 | TrxHeaderPrevRecurredFromTrxNumber | RECURRED_FROM_TRX_NUMBER | — | — |
| 270 | TrxHeaderPrevRelatedBatchSourceSeqId | RELATED_BATCH_SOURCE_SEQ_ID | — | — |
| 271 | TrxHeaderPrevRelatedCustomerTrxId | RELATED_CUSTOMER_TRX_ID | — | — |
| 272 | TrxHeaderPrevRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 273 | TrxHeaderPrevRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 274 | TrxHeaderPrevRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 275 | TrxHeaderPrevRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 276 | TrxHeaderPrevRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 277 | TrxHeaderPrevRequestId | REQUEST_ID | — | — |
| 278 | TrxHeaderPrevRequiresManualScheduling | REQUIRES_MANUAL_SCHEDULING | — | — |
| 279 | TrxHeaderPrevReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 280 | TrxHeaderPrevSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 281 | TrxHeaderPrevShipDateActual | SHIP_DATE_ACTUAL | — | — |
| 282 | TrxHeaderPrevShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 283 | TrxHeaderPrevShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 284 | TrxHeaderPrevShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 285 | TrxHeaderPrevShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 286 | TrxHeaderPrevShipVia | SHIP_VIA | — | — |
| 287 | TrxHeaderPrevShipmentId | SHIPMENT_ID | — | — |
| 288 | TrxHeaderPrevSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 289 | TrxHeaderPrevSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 290 | TrxHeaderPrevSoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | — |
| 291 | TrxHeaderPrevSourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 292 | TrxHeaderPrevSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 293 | TrxHeaderPrevSpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 294 | TrxHeaderPrevStartDateCommitment | START_DATE_COMMITMENT | — | — |
| 295 | TrxHeaderPrevStatusTrx | STATUS_TRX | — | — |
| 296 | TrxHeaderPrevTermDueDate | TERM_DUE_DATE | — | — |
| 297 | TrxHeaderPrevTermId | TERM_ID | — | — |
| 298 | TrxHeaderPrevTerritoryId | TERRITORY_ID | — | — |
| 299 | TrxHeaderPrevTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 300 | TrxHeaderPrevTrxClass | TRX_CLASS | — | — |
| 301 | TrxHeaderPrevTrxDate | TRX_DATE | — | — |
| 302 | TrxHeaderPrevTrxNumber | TRX_NUMBER | — | ✅ |
| 303 | TrxHeaderPrevUpgradeMethod | UPGRADE_METHOD | — | — |
| 304 | TrxHeaderPrevUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 305 | TrxHeaderPrevWaybillNumber | WAYBILL_NUMBER | — | — |
| 306 | TrxHeaderPrevWhUpdateDate | WH_UPDATE_DATE | — | — |

### [[ra_rules|RA_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvDistRuleDescription | DESCRIPTION | — | — |
| 2 | InvDistRuleName | NAME | — | ✅ |
| 3 | InvDistRuleObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | InvDistRuleRuleId | RULE_ID | — | — |

### [[zx_fc_user_defined_v|ZX_FC_USER_DEFINED_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UsrDfndFiscClsClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | UsrDfndFiscClsClassificationName | CLASSIFICATION_NAME | — | ✅ |
| 3 | UsrDfndFiscClsCountryCode | COUNTRY_CODE | — | — |

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
