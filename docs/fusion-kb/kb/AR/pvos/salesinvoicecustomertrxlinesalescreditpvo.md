---
id: DOC-AR-PVO-SalesInvoiceCustomerTrxLineSalesCreditPVO
doc_type: system-doc
title: "SalesInvoiceCustomerTrxLineSalesCreditPVO — PVO Accounts Receivable"
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
  - SalesInvoiceCustomerTrxLineSalesCreditPVO
  - salesinvoicecustomertrxlinesalescreditpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SalesInvoiceCustomerTrxLineSalesCreditPVO

## 📌 Visão Geral

Extrai os créditos de vendas por linha de fatura, vinculando vendedores e percentuais de comissão às linhas de transação. Permite calcular comissões detalhadas por item vendido e analisar a contribuição de cada vendedor por produto.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.SalesInvoiceCustomerTrxLineSalesCreditPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 537 | 7 | 1 | 19 | 4% |

---

## 🔗 Tabelas Relacionadas

- [[ar_interest_headers_all|AR_INTEREST_HEADERS_ALL]] — 35 atributos
- [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]] — 5 atributos
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 2 atributos (2 BICC)
- [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]] — 144 atributos (3 BICC)
- [[ra_customer_trx_lines_all|RA_CUSTOMER_TRX_LINES_ALL]] — 143 atributos
- [[ra_cust_trx_line_salesreps_all|RA_CUST_TRX_LINE_SALESREPS_ALL]] — 44 atributos (1 PKs, 13 BICC)
- [[zx_lines|ZX_LINES]] — 164 atributos (1 BICC)

---

## ⚙️ Atributos

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

### [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocSeqHdrAuditTableName | AUDIT_TABLE_NAME | — | — |
| 2 | DocSeqHdrDbSequenceName | DB_SEQUENCE_NAME | — | — |
| 3 | DocSeqHdrDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 4 | DocSeqHdrName | NAME | — | — |
| 5 | DocSeqHdrTableName | TABLE_NAME | — | — |

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitBusinessUnitId | BU_ID | — | ✅ |
| 2 | BusinessUnitName | BU_NAME | — | ✅ |

### [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionHeaderAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 2 | TransactionHeaderAgreementId | AGREEMENT_ID | — | — |
| 3 | TransactionHeaderApplicationId | APPLICATION_ID | — | — |
| 4 | TransactionHeaderApprovalCode | APPROVAL_CODE | — | — |
| 5 | TransactionHeaderAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 6 | TransactionHeaderBatchId | BATCH_ID | — | — |
| 7 | TransactionHeaderBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 8 | TransactionHeaderBillTemplateId | BILL_TEMPLATE_ID | — | — |
| 9 | TransactionHeaderBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 10 | TransactionHeaderBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 11 | TransactionHeaderBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 12 | TransactionHeaderBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 13 | TransactionHeaderBillingDate | BILLING_DATE | — | — |
| 14 | TransactionHeaderBrAmount | BR_AMOUNT | — | — |
| 15 | TransactionHeaderBrOnHoldFlag | BR_ON_HOLD_FLAG | — | — |
| 16 | TransactionHeaderBrUnpaidFlag | BR_UNPAID_FLAG | — | — |
| 17 | TransactionHeaderCcErrorCode | CC_ERROR_CODE | — | — |
| 18 | TransactionHeaderCcErrorFlag | CC_ERROR_FLAG | — | — |
| 19 | TransactionHeaderCcErrorText | CC_ERROR_TEXT | — | — |
| 20 | TransactionHeaderComments | COMMENTS | — | — |
| 21 | TransactionHeaderCompleteFlag | COMPLETE_FLAG | — | — |
| 22 | TransactionHeaderContractId | CONTRACT_ID | — | — |
| 23 | TransactionHeaderCreatedFrom | CREATED_FROM | — | — |
| 24 | TransactionHeaderCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | — |
| 25 | TransactionHeaderCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | — |
| 26 | TransactionHeaderCtReference | CT_REFERENCE | — | — |
| 27 | TransactionHeaderCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 28 | TransactionHeaderCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 29 | TransactionHeaderCustomerReference | CUSTOMER_REFERENCE | — | — |
| 30 | TransactionHeaderCustomerReferenceDate | CUSTOMER_REFERENCE_DATE | — | — |
| 31 | TransactionHeaderCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 32 | TransactionHeaderDefaultTaxExemptFlag | DEFAULT_TAX_EXEMPT_FLAG | — | — |
| 33 | TransactionHeaderDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 34 | TransactionHeaderDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 35 | TransactionHeaderDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 36 | TransactionHeaderDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 37 | TransactionHeaderDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 38 | TransactionHeaderDocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 39 | TransactionHeaderDraweeBankAccountId | DRAWEE_BANK_ACCOUNT_ID | — | — |
| 40 | TransactionHeaderDraweeContactId | DRAWEE_CONTACT_ID | — | — |
| 41 | TransactionHeaderDraweeId | DRAWEE_ID | — | — |
| 42 | TransactionHeaderDraweeSiteUseId | DRAWEE_SITE_USE_ID | — | — |
| 43 | TransactionHeaderEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 44 | TransactionHeaderEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 45 | TransactionHeaderEndDateCommitment | END_DATE_COMMITMENT | — | — |
| 46 | TransactionHeaderExchangeDate | EXCHANGE_DATE | — | — |
| 47 | TransactionHeaderExchangeRate | EXCHANGE_RATE | — | — |
| 48 | TransactionHeaderExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 49 | TransactionHeaderFinanceCharges | FINANCE_CHARGES | — | — |
| 50 | TransactionHeaderFobPoint | FOB_POINT | — | — |
| 51 | TransactionHeaderInitialCustomerTrxId | INITIAL_CUSTOMER_TRX_ID | — | — |
| 52 | TransactionHeaderIntercompanyFlag | INTERCOMPANY_FLAG | — | — |
| 53 | TransactionHeaderInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 54 | TransactionHeaderInterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | — |
| 55 | TransactionHeaderInterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | — |
| 56 | TransactionHeaderInterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | — |
| 57 | TransactionHeaderInterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | — |
| 58 | TransactionHeaderInterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | — |
| 59 | TransactionHeaderInterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | — |
| 60 | TransactionHeaderInterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | — |
| 61 | TransactionHeaderInterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | — |
| 62 | TransactionHeaderInterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | — |
| 63 | TransactionHeaderInterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | — |
| 64 | TransactionHeaderInterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | — |
| 65 | TransactionHeaderInterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | — |
| 66 | TransactionHeaderInterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | — |
| 67 | TransactionHeaderInterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | — |
| 68 | TransactionHeaderInterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | — |
| 69 | TransactionHeaderInterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | — |
| 70 | TransactionHeaderInternalNotes | INTERNAL_NOTES | — | — |
| 71 | TransactionHeaderInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 72 | TransactionHeaderInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 73 | TransactionHeaderLastPrintedSequenceNum | LAST_PRINTED_SEQUENCE_NUM | — | — |
| 74 | TransactionHeaderLateChargesAssessed | LATE_CHARGES_ASSESSED | — | — |
| 75 | TransactionHeaderLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 76 | TransactionHeaderOldTrxNumber | OLD_TRX_NUMBER | — | — |
| 77 | TransactionHeaderOrgId | ORG_ID | — | — |
| 78 | TransactionHeaderOrigSystemBatchName | ORIG_SYSTEM_BATCH_NAME | — | — |
| 79 | TransactionHeaderOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 80 | TransactionHeaderPayingCustomerId | PAYING_CUSTOMER_ID | — | — |
| 81 | TransactionHeaderPayingSiteUseId | PAYING_SITE_USE_ID | — | — |
| 82 | TransactionHeaderPaymentAttributes | PAYMENT_ATTRIBUTES | — | — |
| 83 | TransactionHeaderPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 84 | TransactionHeaderPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 85 | TransactionHeaderPostRequestId | POST_REQUEST_ID | — | — |
| 86 | TransactionHeaderPostingControlId | POSTING_CONTROL_ID | — | — |
| 87 | TransactionHeaderPrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 88 | TransactionHeaderPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 89 | TransactionHeaderPrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | — |
| 90 | TransactionHeaderPrintingCount | PRINTING_COUNT | — | — |
| 91 | TransactionHeaderPrintingLastPrinted | PRINTING_LAST_PRINTED | — | — |
| 92 | TransactionHeaderPrintingOption | PRINTING_OPTION | — | — |
| 93 | TransactionHeaderPrintingOriginalDate | PRINTING_ORIGINAL_DATE | — | — |
| 94 | TransactionHeaderPrintingPending | PRINTING_PENDING | — | — |
| 95 | TransactionHeaderProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 96 | TransactionHeaderProgramId | PROGRAM_ID | — | — |
| 97 | TransactionHeaderProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 98 | TransactionHeaderPurchaseOrder | PURCHASE_ORDER | — | — |
| 99 | TransactionHeaderPurchaseOrderDate | PURCHASE_ORDER_DATE | — | — |
| 100 | TransactionHeaderPurchaseOrderRevision | PURCHASE_ORDER_REVISION | — | — |
| 101 | TransactionHeaderRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 102 | TransactionHeaderReasonCode | REASON_CODE | — | — |
| 103 | TransactionHeaderReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 104 | TransactionHeaderRecurredFromTrxNumber | RECURRED_FROM_TRX_NUMBER | — | — |
| 105 | TransactionHeaderRelatedBatchSourceSeqId | RELATED_BATCH_SOURCE_SEQ_ID | — | — |
| 106 | TransactionHeaderRelatedCustomerTrxId | RELATED_CUSTOMER_TRX_ID | — | — |
| 107 | TransactionHeaderRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 108 | TransactionHeaderRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 109 | TransactionHeaderRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 110 | TransactionHeaderRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 111 | TransactionHeaderRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 112 | TransactionHeaderRequestId | REQUEST_ID | — | — |
| 113 | TransactionHeaderRequiresManualScheduling | REQUIRES_MANUAL_SCHEDULING | — | — |
| 114 | TransactionHeaderReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 115 | TransactionHeaderSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 116 | TransactionHeaderShipDateActual | SHIP_DATE_ACTUAL | — | — |
| 117 | TransactionHeaderShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 118 | TransactionHeaderShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 119 | TransactionHeaderShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 120 | TransactionHeaderShipToPartyId | SHIP_TO_PARTY_ID | — | ✅ |
| 121 | TransactionHeaderShipToPartySiteUseId | SHIP_TO_PARTY_SITE_USE_ID | — | ✅ |
| 122 | TransactionHeaderShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 123 | TransactionHeaderShipVia | SHIP_VIA | — | — |
| 124 | TransactionHeaderShipmentId | SHIPMENT_ID | — | — |
| 125 | TransactionHeaderSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 126 | TransactionHeaderSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 127 | TransactionHeaderSoldToPartyId | SOLD_TO_PARTY_ID | — | ✅ |
| 128 | TransactionHeaderSoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | — |
| 129 | TransactionHeaderSourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 130 | TransactionHeaderSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 131 | TransactionHeaderSpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 132 | TransactionHeaderStartDateCommitment | START_DATE_COMMITMENT | — | — |
| 133 | TransactionHeaderStatusTrx | STATUS_TRX | — | — |
| 134 | TransactionHeaderTermDueDate | TERM_DUE_DATE | — | — |
| 135 | TransactionHeaderTermId | TERM_ID | — | — |
| 136 | TransactionHeaderTerritoryId | TERRITORY_ID | — | — |
| 137 | TransactionHeaderTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 138 | TransactionHeaderTrxClass | TRX_CLASS | — | — |
| 139 | TransactionHeaderTrxDate | TRX_DATE | — | — |
| 140 | TransactionHeaderTrxNumber | TRX_NUMBER | — | — |
| 141 | TransactionHeaderUpgradeMethod | UPGRADE_METHOD | — | — |
| 142 | TransactionHeaderUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 143 | TransactionHeaderWaybillNumber | WAYBILL_NUMBER | — | — |
| 144 | TransactionHeaderWhUpdateDate | WH_UPDATE_DATE | — | — |

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
| 18 | TransactionLineCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 19 | TransactionLineCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 20 | TransactionLineDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 21 | TransactionLineDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 22 | TransactionLineDeferralExclusionFlag | DEFERRAL_EXCLUSION_FLAG | — | — |
| 23 | TransactionLineDescription | DESCRIPTION | — | — |
| 24 | TransactionLineExtendedAcctdAmount | EXTENDED_ACCTD_AMOUNT | — | — |
| 25 | TransactionLineExtendedAmount | EXTENDED_AMOUNT | — | — |
| 26 | TransactionLineFairMarketValueAmount | FAIR_MARKET_VALUE_AMOUNT | — | — |
| 27 | TransactionLineFrtAdjAcctdRemaining | FRT_ADJ_ACCTD_REMAINING | — | — |
| 28 | TransactionLineFrtAdjRemaining | FRT_ADJ_REMAINING | — | — |
| 29 | TransactionLineFrtEdAcctdAmount | FRT_ED_ACCTD_AMOUNT | — | — |
| 30 | TransactionLineFrtEdAmount | FRT_ED_AMOUNT | — | — |
| 31 | TransactionLineFrtUnedAcctdAmount | FRT_UNED_ACCTD_AMOUNT | — | — |
| 32 | TransactionLineFrtUnedAmount | FRT_UNED_AMOUNT | — | — |
| 33 | TransactionLineGrossExtendedAmount | GROSS_EXTENDED_AMOUNT | — | — |
| 34 | TransactionLineGrossUnitSellingPrice | GROSS_UNIT_SELLING_PRICE | — | — |
| 35 | TransactionLineHistoricalFlag | HISTORICAL_FLAG | — | — |
| 36 | TransactionLineInitialCustomerTrxLineId | INITIAL_CUSTOMER_TRX_LINE_ID | — | — |
| 37 | TransactionLineInterestLineId | INTEREST_LINE_ID | — | — |
| 38 | TransactionLineInterfaceLineAttribute1 | INTERFACE_LINE_ATTRIBUTE1 | — | — |
| 39 | TransactionLineInterfaceLineAttribute10 | INTERFACE_LINE_ATTRIBUTE10 | — | — |
| 40 | TransactionLineInterfaceLineAttribute11 | INTERFACE_LINE_ATTRIBUTE11 | — | — |
| 41 | TransactionLineInterfaceLineAttribute12 | INTERFACE_LINE_ATTRIBUTE12 | — | — |
| 42 | TransactionLineInterfaceLineAttribute13 | INTERFACE_LINE_ATTRIBUTE13 | — | — |
| 43 | TransactionLineInterfaceLineAttribute14 | INTERFACE_LINE_ATTRIBUTE14 | — | — |
| 44 | TransactionLineInterfaceLineAttribute15 | INTERFACE_LINE_ATTRIBUTE15 | — | — |
| 45 | TransactionLineInterfaceLineAttribute2 | INTERFACE_LINE_ATTRIBUTE2 | — | — |
| 46 | TransactionLineInterfaceLineAttribute3 | INTERFACE_LINE_ATTRIBUTE3 | — | — |
| 47 | TransactionLineInterfaceLineAttribute4 | INTERFACE_LINE_ATTRIBUTE4 | — | — |
| 48 | TransactionLineInterfaceLineAttribute5 | INTERFACE_LINE_ATTRIBUTE5 | — | — |
| 49 | TransactionLineInterfaceLineAttribute6 | INTERFACE_LINE_ATTRIBUTE6 | — | — |
| 50 | TransactionLineInterfaceLineAttribute7 | INTERFACE_LINE_ATTRIBUTE7 | — | — |
| 51 | TransactionLineInterfaceLineAttribute8 | INTERFACE_LINE_ATTRIBUTE8 | — | — |
| 52 | TransactionLineInterfaceLineAttribute9 | INTERFACE_LINE_ATTRIBUTE9 | — | — |
| 53 | TransactionLineInterfaceLineContext | INTERFACE_LINE_CONTEXT | — | — |
| 54 | TransactionLineInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 55 | TransactionLineInvoicedLineAcctgLevel | INVOICED_LINE_ACCTG_LEVEL | — | — |
| 56 | TransactionLineItemContext | ITEM_CONTEXT | — | — |
| 57 | TransactionLineItemExceptionRateId | ITEM_EXCEPTION_RATE_ID | — | — |
| 58 | TransactionLineLastPeriodToCredit | LAST_PERIOD_TO_CREDIT | — | — |
| 59 | TransactionLineLineIntendedUse | LINE_INTENDED_USE | — | — |
| 60 | TransactionLineLineNumber | LINE_NUMBER | — | — |
| 61 | TransactionLineLineRecoverable | LINE_RECOVERABLE | — | — |
| 62 | TransactionLineLineType | LINE_TYPE | — | — |
| 63 | TransactionLineLinkToCustTrxLineId | LINK_TO_CUST_TRX_LINE_ID | — | — |
| 64 | TransactionLineLinkToParentlineAttribute1 | LINK_TO_PARENTLINE_ATTRIBUTE1 | — | — |
| 65 | TransactionLineLinkToParentlineAttribute10 | LINK_TO_PARENTLINE_ATTRIBUTE10 | — | — |
| 66 | TransactionLineLinkToParentlineAttribute11 | LINK_TO_PARENTLINE_ATTRIBUTE11 | — | — |
| 67 | TransactionLineLinkToParentlineAttribute12 | LINK_TO_PARENTLINE_ATTRIBUTE12 | — | — |
| 68 | TransactionLineLinkToParentlineAttribute13 | LINK_TO_PARENTLINE_ATTRIBUTE13 | — | — |
| 69 | TransactionLineLinkToParentlineAttribute14 | LINK_TO_PARENTLINE_ATTRIBUTE14 | — | — |
| 70 | TransactionLineLinkToParentlineAttribute15 | LINK_TO_PARENTLINE_ATTRIBUTE15 | — | — |
| 71 | TransactionLineLinkToParentlineAttribute2 | LINK_TO_PARENTLINE_ATTRIBUTE2 | — | — |
| 72 | TransactionLineLinkToParentlineAttribute3 | LINK_TO_PARENTLINE_ATTRIBUTE3 | — | — |
| 73 | TransactionLineLinkToParentlineAttribute4 | LINK_TO_PARENTLINE_ATTRIBUTE4 | — | — |
| 74 | TransactionLineLinkToParentlineAttribute5 | LINK_TO_PARENTLINE_ATTRIBUTE5 | — | — |
| 75 | TransactionLineLinkToParentlineAttribute6 | LINK_TO_PARENTLINE_ATTRIBUTE6 | — | — |
| 76 | TransactionLineLinkToParentlineAttribute7 | LINK_TO_PARENTLINE_ATTRIBUTE7 | — | — |
| 77 | TransactionLineLinkToParentlineAttribute8 | LINK_TO_PARENTLINE_ATTRIBUTE8 | — | — |
| 78 | TransactionLineLinkToParentlineAttribute9 | LINK_TO_PARENTLINE_ATTRIBUTE9 | — | — |
| 79 | TransactionLineLinkToParentlineContext | LINK_TO_PARENTLINE_CONTEXT | — | — |
| 80 | TransactionLineLocationSegmentId | LOCATION_SEGMENT_ID | — | — |
| 81 | TransactionLineMemoLineSeqId | MEMO_LINE_SEQ_ID | — | — |
| 82 | TransactionLineMovementId | MOVEMENT_ID | — | — |
| 83 | TransactionLineMrcExtendedAcctdAmount | MRC_EXTENDED_ACCTD_AMOUNT | — | — |
| 84 | TransactionLineOrgId | ORG_ID | — | — |
| 85 | TransactionLineOverrideAutoAccountingFlag | OVERRIDE_AUTO_ACCOUNTING_FLAG | — | — |
| 86 | TransactionLinePaymentSetId | PAYMENT_SET_ID | — | — |
| 87 | TransactionLinePaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 88 | TransactionLinePreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 89 | TransactionLinePreviousCustomerTrxLineId | PREVIOUS_CUSTOMER_TRX_LINE_ID | — | — |
| 90 | TransactionLineProductCategory | PRODUCT_CATEGORY | — | — |
| 91 | TransactionLineProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | — |
| 92 | TransactionLineProductType | PRODUCT_TYPE | — | — |
| 93 | TransactionLineProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 94 | TransactionLineProgramId | PROGRAM_ID | — | — |
| 95 | TransactionLineProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 96 | TransactionLineQuantityCredited | QUANTITY_CREDITED | — | — |
| 97 | TransactionLineQuantityInvoiced | QUANTITY_INVOICED | — | — |
| 98 | TransactionLineQuantityOrdered | QUANTITY_ORDERED | — | — |
| 99 | TransactionLineReasonCode | REASON_CODE | — | — |
| 100 | TransactionLineRequestId | REQUEST_ID | — | — |
| 101 | TransactionLineRevenueAmount | REVENUE_AMOUNT | — | — |
| 102 | TransactionLineRuleEndDate | RULE_END_DATE | — | — |
| 103 | TransactionLineRuleStartDate | RULE_START_DATE | — | — |
| 104 | TransactionLineSalesOrder | SALES_ORDER | — | — |
| 105 | TransactionLineSalesOrderDate | SALES_ORDER_DATE | — | — |
| 106 | TransactionLineSalesOrderLine | SALES_ORDER_LINE | — | — |
| 107 | TransactionLineSalesOrderRevision | SALES_ORDER_REVISION | — | — |
| 108 | TransactionLineSalesOrderSource | SALES_ORDER_SOURCE | — | — |
| 109 | TransactionLineSalesTaxId | SALES_TAX_ID | — | — |
| 110 | TransactionLineSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 111 | TransactionLineShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 112 | TransactionLineShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 113 | TransactionLineShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 114 | TransactionLineShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 115 | TransactionLineSourceDataKey1 | SOURCE_DATA_KEY1 | — | — |
| 116 | TransactionLineSourceDataKey2 | SOURCE_DATA_KEY2 | — | — |
| 117 | TransactionLineSourceDataKey3 | SOURCE_DATA_KEY3 | — | — |
| 118 | TransactionLineSourceDataKey4 | SOURCE_DATA_KEY4 | — | — |
| 119 | TransactionLineSourceDataKey5 | SOURCE_DATA_KEY5 | — | — |
| 120 | TransactionLineSourceDocumentLineId | SOURCE_DOCUMENT_LINE_ID | — | — |
| 121 | TransactionLineSourceDocumentLineNumber | SOURCE_DOCUMENT_LINE_NUMBER | — | — |
| 122 | TransactionLineTaxAction | TAX_ACTION | — | — |
| 123 | TransactionLineTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 124 | TransactionLineTaxExemptFlag | TAX_EXEMPT_FLAG | — | — |
| 125 | TransactionLineTaxExemptNumber | TAX_EXEMPT_NUMBER | — | — |
| 126 | TransactionLineTaxExemptReasonCode | TAX_EXEMPT_REASON_CODE | — | — |
| 127 | TransactionLineTaxExemptionId | TAX_EXEMPTION_ID | — | — |
| 128 | TransactionLineTaxLineId | TAX_LINE_ID | — | — |
| 129 | TransactionLineTaxPrecedence | TAX_PRECEDENCE | — | — |
| 130 | TransactionLineTaxRate | TAX_RATE | — | — |
| 131 | TransactionLineTaxRecoverable | TAX_RECOVERABLE | — | — |
| 132 | TransactionLineTaxVendorReturnCode | TAX_VENDOR_RETURN_CODE | — | — |
| 133 | TransactionLineTaxableAmount | TAXABLE_AMOUNT | — | — |
| 134 | TransactionLineTaxableFlag | TAXABLE_FLAG | — | — |
| 135 | TransactionLineTranslatedDescription | TRANSLATED_DESCRIPTION | — | — |
| 136 | TransactionLineTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 137 | TransactionLineUnitSellingPrice | UNIT_SELLING_PRICE | — | — |
| 138 | TransactionLineUnitStandardPrice | UNIT_STANDARD_PRICE | — | — |
| 139 | TransactionLineUomCode | UOM_CODE | — | — |
| 140 | TransactionLineUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 141 | TransactionLineVatTaxId | VAT_TAX_ID | — | — |
| 142 | TransactionLineWarehouseId | WAREHOUSE_ID | — | — |
| 143 | TransactionLineWhUpdateDate | WH_UPDATE_DATE | — | — |

### [[ra_cust_trx_line_salesreps_all|RA_CUST_TRX_LINE_SALESREPS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustTrxLineSalesrepId | CUST_TRX_LINE_SALESREP_ID | 🔑 | ✅ |
| 2 | SalesCreditCreatedBy | CREATED_BY | — | ✅ |
| 3 | SalesCreditCreationDate | CREATION_DATE | — | ✅ |
| 4 | SalesCreditCustomerTrxId | CUSTOMER_TRX_ID | — | ✅ |
| 5 | SalesCreditCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | ✅ |
| 6 | SalesCreditLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | SalesCreditLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | SalesCreditLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | SalesCreditNonRevenueAmountSplit | NON_REVENUE_AMOUNT_SPLIT | — | ✅ |
| 10 | SalesCreditNonRevenuePercentSplit | NON_REVENUE_PERCENT_SPLIT | — | ✅ |
| 11 | SalesCreditNonRevenueSalesgroupId | NON_REVENUE_SALESGROUP_ID | — | — |
| 12 | SalesCreditObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | SalesCreditOrgId | ORG_ID | — | ✅ |
| 14 | SalesCreditOriginalLineSalesrepId | ORIGINAL_LINE_SALESREP_ID | — | — |
| 15 | SalesCreditPrevCustTrxLineSalesrepId | PREV_CUST_TRX_LINE_SALESREP_ID | — | — |
| 16 | SalesCreditPreviousCustTrxLineSalesrepId | CUST_TRX_LINE_SALESREP_ID | — | — |
| 17 | SalesCreditPreviousCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 18 | SalesCreditPreviousCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 19 | SalesCreditPreviousNonRevenueAmountSplit | NON_REVENUE_AMOUNT_SPLIT | — | — |
| 20 | SalesCreditPreviousNonRevenuePercentSplit | NON_REVENUE_PERCENT_SPLIT | — | — |
| 21 | SalesCreditPreviousNonRevenueSalesgroupId | NON_REVENUE_SALESGROUP_ID | — | — |
| 22 | SalesCreditPreviousOrgId | ORG_ID | — | — |
| 23 | SalesCreditPreviousOriginalLineSalesrepId | ORIGINAL_LINE_SALESREP_ID | — | — |
| 24 | SalesCreditPreviousPrevCustTrxLineSalesrepId | PREV_CUST_TRX_LINE_SALESREP_ID | — | — |
| 25 | SalesCreditPreviousProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 26 | SalesCreditPreviousProgramId | PROGRAM_ID | — | — |
| 27 | SalesCreditPreviousProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 28 | SalesCreditPreviousRequestId | REQUEST_ID | — | — |
| 29 | SalesCreditPreviousResourceSalesrepId | RESOURCE_SALESREP_ID | — | — |
| 30 | SalesCreditPreviousRevenueAdjustmentId | REVENUE_ADJUSTMENT_ID | — | — |
| 31 | SalesCreditPreviousRevenueAmountSplit | REVENUE_AMOUNT_SPLIT | — | — |
| 32 | SalesCreditPreviousRevenuePercentSplit | REVENUE_PERCENT_SPLIT | — | — |
| 33 | SalesCreditPreviousRevenueSalesgroupId | REVENUE_SALESGROUP_ID | — | — |
| 34 | SalesCreditPreviousWhUpdateDate | WH_UPDATE_DATE | — | — |
| 35 | SalesCreditProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 36 | SalesCreditProgramId | PROGRAM_ID | — | — |
| 37 | SalesCreditProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 38 | SalesCreditRequestId | REQUEST_ID | — | — |
| 39 | SalesCreditResourceSalesrepId | RESOURCE_SALESREP_ID | — | ✅ |
| 40 | SalesCreditRevenueAdjustmentId | REVENUE_ADJUSTMENT_ID | — | — |
| 41 | SalesCreditRevenueAmountSplit | REVENUE_AMOUNT_SPLIT | — | ✅ |
| 42 | SalesCreditRevenuePercentSplit | REVENUE_PERCENT_SPLIT | — | ✅ |
| 43 | SalesCreditRevenueSalesgroupId | REVENUE_SALESGROUP_ID | — | — |
| 44 | SalesCreditWhUpdateDate | WH_UPDATE_DATE | — | — |

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
| 24 | DtlTaxLineCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
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

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
