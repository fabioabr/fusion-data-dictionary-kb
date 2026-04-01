---
id: DOC-OTHER-PVO-ExpenseDistributionPVO
doc_type: system-doc
title: "ExpenseDistributionPVO — PVO Cross-Module"
system: Oracle Fusion Cloud ERP
module: Cross-Module
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - other
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ExpenseDistributionPVO
  - expensedistributionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpenseDistributionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Expense Distribution. Acessa as tabelas: AP_BATCHES_ALL, AP_DISTRIBUTION_SETS_ALL, AP_INVOICES_ALL (+20).

**Caminho:** `FscmTopModelAM.FinExmEntrySharedAM.ExpenseDistributionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 1317 | 23 | 1 | 127 | 10% |

---

## 🔗 Tabelas Relacionadas

- [[ap_batches_all|AP_BATCHES_ALL]] — 25 atributos (1 BICC)
- [[ap_distribution_sets_all|AP_DISTRIBUTION_SETS_ALL]] — 12 atributos (1 BICC)
- [[ap_invoices_all|AP_INVOICES_ALL]] — 133 atributos (4 BICC)
- [[exm_credit_card_trxns|EXM_CREDIT_CARD_TRXNS]] — 146 atributos (1 BICC)
- [[exm_expenses|EXM_EXPENSES]] — 96 atributos (50 BICC)
- [[exm_expense_dists|EXM_EXPENSE_DISTS]] — 77 atributos (1 PKs, 15 BICC)
- [[exm_expense_reports|EXM_EXPENSE_REPORTS]] — 108 atributos (31 BICC)
- [[exm_expense_templates|EXM_EXPENSE_TEMPLATES]] — 21 atributos (1 BICC)
- [[exm_expense_types|EXM_EXPENSE_TYPES]] — 27 atributos (1 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 1 atributos
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 54 atributos (3 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 86 atributos
- [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]] — 4 atributos
- [[hr_all_organization_units_f_vl|HR_ALL_ORGANIZATION_UNITS_F_VL]] — 51 atributos (1 BICC)
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 4 atributos
- [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]] — 49 atributos (1 BICC)
- [[iby_payment_codes_vl|IBY_PAYMENT_CODES_VL]] — 30 atributos (2 BICC)
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 8 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 93 atributos (7 BICC)
- [[per_users|PER_USERS]] — 30 atributos
- [[pjf_exp_types_tl|PJF_EXP_TYPES_TL]] — 10 atributos (2 BICC)
- [[po_headers_all|PO_HEADERS_ALL]] — 222 atributos (2 BICC)
- [[zx_wht_tax_classification_v|ZX_WHT_TAX_CLASSIFICATION_V]] — 30 atributos (3 BICC)

---

## ⚙️ Atributos

### [[ap_batches_all|AP_BATCHES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceBatchActualInvoiceCount | ACTUAL_INVOICE_COUNT | — | — |
| 2 | InvoiceBatchActualInvoiceTotal | ACTUAL_INVOICE_TOTAL | — | — |
| 3 | InvoiceBatchBatchCodeCombinationId | BATCH_CODE_COMBINATION_ID | — | — |
| 4 | InvoiceBatchBatchDate | BATCH_DATE | — | — |
| 5 | InvoiceBatchBatchId | BATCH_ID | — | — |
| 6 | InvoiceBatchBatchName | BATCH_NAME | — | — |
| 7 | InvoiceBatchControlInvoiceCount | CONTROL_INVOICE_COUNT | — | — |
| 8 | InvoiceBatchControlInvoiceTotal | CONTROL_INVOICE_TOTAL | — | — |
| 9 | InvoiceBatchCreatedBy | CREATED_BY | — | — |
| 10 | InvoiceBatchCreationDate | CREATION_DATE | — | — |
| 11 | InvoiceBatchDocCategoryCode | DOC_CATEGORY_CODE | — | — |
| 12 | InvoiceBatchGlDate | GL_DATE | — | — |
| 13 | InvoiceBatchHoldLookupCode | HOLD_LOOKUP_CODE | — | — |
| 14 | InvoiceBatchHoldReason | HOLD_REASON | — | — |
| 15 | InvoiceBatchInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 16 | InvoiceBatchInvoiceTypeLookupCode | INVOICE_TYPE_LOOKUP_CODE | — | — |
| 17 | InvoiceBatchLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | InvoiceBatchLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | InvoiceBatchLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | InvoiceBatchObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | InvoiceBatchOrgId | ORG_ID | — | — |
| 22 | InvoiceBatchPayGroupLookupCode | PAY_GROUP_LOOKUP_CODE | — | — |
| 23 | InvoiceBatchPaymentCurrencyCode | PAYMENT_CURRENCY_CODE | — | — |
| 24 | InvoiceBatchPaymentPriority | PAYMENT_PRIORITY | — | — |
| 25 | InvoiceBatchTermsId | TERMS_ID | — | — |

### [[ap_distribution_sets_all|AP_DISTRIBUTION_SETS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistributionSetCreatedBy | CREATED_BY | — | — |
| 2 | DistributionSetCreationDate | CREATION_DATE | — | — |
| 3 | DistributionSetDescription | DESCRIPTION | — | — |
| 4 | DistributionSetDistributionSetId | DISTRIBUTION_SET_ID | — | — |
| 5 | DistributionSetDistributionSetName | DISTRIBUTION_SET_NAME | — | — |
| 6 | DistributionSetInactiveDate | INACTIVE_DATE | — | — |
| 7 | DistributionSetLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | DistributionSetLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | DistributionSetLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | DistributionSetObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | DistributionSetOrgId | ORG_ID | — | — |
| 12 | DistributionSetTotalPercentDistribution | TOTAL_PERCENT_DISTRIBUTION | — | — |

### [[ap_invoices_all|AP_INVOICES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceAcctsPayCodeCombinationId | ACCTS_PAY_CODE_COMBINATION_ID | — | — |
| 2 | InvoiceAmountApplicableToDiscount | AMOUNT_APPLICABLE_TO_DISCOUNT | — | — |
| 3 | InvoiceAmountPaid | AMOUNT_PAID | — | — |
| 4 | InvoiceAmtDueCcardCompany | AMT_DUE_CCARD_COMPANY | — | — |
| 5 | InvoiceAmtDueEmployee | AMT_DUE_EMPLOYEE | — | — |
| 6 | InvoiceApplicationId | APPLICATION_ID | — | — |
| 7 | InvoiceApprovalDescription | APPROVAL_DESCRIPTION | — | — |
| 8 | InvoiceApprovalIteration | APPROVAL_ITERATION | — | — |
| 9 | InvoiceApprovalReadyFlag | APPROVAL_READY_FLAG | — | — |
| 10 | InvoiceApprovalStatus | APPROVAL_STATUS | — | — |
| 11 | InvoiceApprovedAmount | APPROVED_AMOUNT | — | — |
| 12 | InvoiceAwardId | AWARD_ID | — | — |
| 13 | InvoiceAwtFlag | AWT_FLAG | — | — |
| 14 | InvoiceAwtGroupId | AWT_GROUP_ID | — | — |
| 15 | InvoiceBankChargeBearer | BANK_CHARGE_BEARER | — | — |
| 16 | InvoiceBaseAmount | BASE_AMOUNT | — | — |
| 17 | InvoiceBatchId | BATCH_ID | — | — |
| 18 | InvoiceCancelledAmount | CANCELLED_AMOUNT | — | — |
| 19 | InvoiceCancelledBy | CANCELLED_BY | — | — |
| 20 | InvoiceCancelledDate | CANCELLED_DATE | — | — |
| 21 | InvoiceControlAmount | CONTROL_AMOUNT | — | — |
| 22 | InvoiceCreatedBy | CREATED_BY | — | — |
| 23 | InvoiceCreationDate | CREATION_DATE | — | — |
| 24 | InvoiceCreditedInvoiceId | CREDITED_INVOICE_ID | — | — |
| 25 | InvoiceCustRegistrationCode | CUST_REGISTRATION_CODE | — | — |
| 26 | InvoiceCustRegistrationNumber | CUST_REGISTRATION_NUMBER | — | — |
| 27 | InvoiceDeliveryChannelCode | DELIVERY_CHANNEL_CODE | — | — |
| 28 | InvoiceDescription | DESCRIPTION | — | — |
| 29 | InvoiceDiscIsInvLessTaxFlag | DISC_IS_INV_LESS_TAX_FLAG | — | — |
| 30 | InvoiceDiscountAmountTaken | DISCOUNT_AMOUNT_TAKEN | — | — |
| 31 | InvoiceDistributionSetId | DISTRIBUTION_SET_ID | — | — |
| 32 | InvoiceDocCategoryCode | DOC_CATEGORY_CODE | — | — |
| 33 | InvoiceDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 34 | InvoiceDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 35 | InvoiceDocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 36 | InvoiceEarliestSettlementDate | EARLIEST_SETTLEMENT_DATE | — | — |
| 37 | InvoiceExchangeDate | EXCHANGE_DATE | — | — |
| 38 | InvoiceExchangeRate | EXCHANGE_RATE | — | — |
| 39 | InvoiceExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 40 | InvoiceExcludeFreightFromDiscount | EXCLUDE_FREIGHT_FROM_DISCOUNT | — | — |
| 41 | InvoiceExclusivePaymentFlag | EXCLUSIVE_PAYMENT_FLAG | — | — |
| 42 | InvoiceExternalBankAccountId | EXTERNAL_BANK_ACCOUNT_ID | — | — |
| 43 | InvoiceForceRevalidationFlag | FORCE_REVALIDATION_FLAG | — | — |
| 44 | InvoiceFreightAmount | FREIGHT_AMOUNT | — | — |
| 45 | InvoiceGlDate | GL_DATE | — | — |
| 46 | InvoiceGoodsReceivedDate | GOODS_RECEIVED_DATE | — | — |
| 47 | InvoiceHistoricalFlag | HISTORICAL_FLAG | — | — |
| 48 | InvoiceIntercompanyFlag | INTERCOMPANY_FLAG | — | — |
| 49 | InvoiceInternalContactEmail | INTERNAL_CONTACT_EMAIL | — | — |
| 50 | InvoiceInvoiceAmount | INVOICE_AMOUNT | — | — |
| 51 | InvoiceInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 52 | InvoiceInvoiceDate | INVOICE_DATE | — | ✅ |
| 53 | InvoiceInvoiceId | INVOICE_ID | — | — |
| 54 | InvoiceInvoiceNum | INVOICE_NUM | — | ✅ |
| 55 | InvoiceInvoiceReceivedDate | INVOICE_RECEIVED_DATE | — | — |
| 56 | InvoiceInvoiceTypeLookupCode | INVOICE_TYPE_LOOKUP_CODE | — | — |
| 57 | InvoiceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 58 | InvoiceLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 59 | InvoiceLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 60 | InvoiceLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 61 | InvoiceMrcBaseAmount | MRC_BASE_AMOUNT | — | — |
| 62 | InvoiceMrcExchangeDate | MRC_EXCHANGE_DATE | — | — |
| 63 | InvoiceMrcExchangeRate | MRC_EXCHANGE_RATE | — | — |
| 64 | InvoiceMrcExchangeRateType | MRC_EXCHANGE_RATE_TYPE | — | — |
| 65 | InvoiceMrcPostingStatus | MRC_POSTING_STATUS | — | — |
| 66 | InvoiceNetOfRetainageFlag | NET_OF_RETAINAGE_FLAG | — | — |
| 67 | InvoiceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 68 | InvoiceOrgId | ORG_ID | — | — |
| 69 | InvoicePaidOnBehalfEmployeeId | PAID_ON_BEHALF_EMPLOYEE_ID | — | — |
| 70 | InvoicePartyId | PARTY_ID | — | — |
| 71 | InvoicePartySiteId | PARTY_SITE_ID | — | — |
| 72 | InvoicePayCurrInvoiceAmount | PAY_CURR_INVOICE_AMOUNT | — | — |
| 73 | InvoicePayGroupLookupCode | PAY_GROUP_LOOKUP_CODE | — | — |
| 74 | InvoicePayProcTrxnTypeCode | PAY_PROC_TRXN_TYPE_CODE | — | — |
| 75 | InvoicePaymentAmountTotal | PAYMENT_AMOUNT_TOTAL | — | — |
| 76 | InvoicePaymentCrossRate | PAYMENT_CROSS_RATE | — | — |
| 77 | InvoicePaymentCrossRateDate | PAYMENT_CROSS_RATE_DATE | — | — |
| 78 | InvoicePaymentCrossRateType | PAYMENT_CROSS_RATE_TYPE | — | — |
| 79 | InvoicePaymentCurrencyCode | PAYMENT_CURRENCY_CODE | — | — |
| 80 | InvoicePaymentFunction | PAYMENT_FUNCTION | — | — |
| 81 | InvoicePaymentMethodCode | PAYMENT_METHOD_CODE | — | — |
| 82 | InvoicePaymentMethodLookupCode | PAYMENT_METHOD_LOOKUP_CODE | — | — |
| 83 | InvoicePaymentReasonCode | PAYMENT_REASON_CODE | — | — |
| 84 | InvoicePaymentReasonComments | PAYMENT_REASON_COMMENTS | — | — |
| 85 | InvoicePaymentStatusFlag | PAYMENT_STATUS_FLAG | — | — |
| 86 | InvoicePoHeaderId | PO_HEADER_ID | — | — |
| 87 | InvoicePortOfEntryCode | PORT_OF_ENTRY_CODE | — | — |
| 88 | InvoicePostingStatus | POSTING_STATUS | — | — |
| 89 | InvoicePreWithholdingAmount | PRE_WITHHOLDING_AMOUNT | — | — |
| 90 | InvoiceProductTable | PRODUCT_TABLE | — | — |
| 91 | InvoiceQuickCredit | QUICK_CREDIT | — | — |
| 92 | InvoiceQuickPoHeaderId | QUICK_PO_HEADER_ID | — | — |
| 93 | InvoiceRecurringPaymentId | RECURRING_PAYMENT_ID | — | — |
| 94 | InvoiceReference1 | REFERENCE_1 | — | — |
| 95 | InvoiceReference2 | REFERENCE_2 | — | — |
| 96 | InvoiceReferenceKey1 | REFERENCE_KEY1 | — | — |
| 97 | InvoiceReferenceKey2 | REFERENCE_KEY2 | — | — |
| 98 | InvoiceReferenceKey3 | REFERENCE_KEY3 | — | — |
| 99 | InvoiceReferenceKey4 | REFERENCE_KEY4 | — | — |
| 100 | InvoiceReferenceKey5 | REFERENCE_KEY5 | — | — |
| 101 | InvoiceReleaseAmountNetOfTax | RELEASE_AMOUNT_NET_OF_TAX | — | — |
| 102 | InvoiceRemittanceMessage1 | REMITTANCE_MESSAGE1 | — | — |
| 103 | InvoiceRemittanceMessage2 | REMITTANCE_MESSAGE2 | — | — |
| 104 | InvoiceRemittanceMessage3 | REMITTANCE_MESSAGE3 | — | — |
| 105 | InvoiceRequesterId | REQUESTER_ID | — | — |
| 106 | InvoiceSelfAssessedTaxAmount | SELF_ASSESSED_TAX_AMOUNT | — | — |
| 107 | InvoiceSetOfBooksId | SET_OF_BOOKS_ID | — | ✅ |
| 108 | InvoiceSettlementPriority | SETTLEMENT_PRIORITY | — | — |
| 109 | InvoiceSource | SOURCE | — | — |
| 110 | InvoiceSupplierTaxExchangeRate | SUPPLIER_TAX_EXCHANGE_RATE | — | — |
| 111 | InvoiceSupplierTaxInvoiceDate | SUPPLIER_TAX_INVOICE_DATE | — | — |
| 112 | InvoiceSupplierTaxInvoiceNumber | SUPPLIER_TAX_INVOICE_NUMBER | — | — |
| 113 | InvoiceTaxInvoiceInternalSeq | TAX_INVOICE_INTERNAL_SEQ | — | — |
| 114 | InvoiceTaxInvoiceRecordingDate | TAX_INVOICE_RECORDING_DATE | — | — |
| 115 | InvoiceTaxRelatedInvoiceId | TAX_RELATED_INVOICE_ID | — | — |
| 116 | InvoiceTaxationCountry | TAXATION_COUNTRY | — | — |
| 117 | InvoiceTempCancelledAmount | TEMP_CANCELLED_AMOUNT | — | — |
| 118 | InvoiceTermsDate | TERMS_DATE | — | — |
| 119 | InvoiceTermsId | TERMS_ID | — | — |
| 120 | InvoiceTotalTaxAmount | TOTAL_TAX_AMOUNT | — | — |
| 121 | InvoiceTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 122 | InvoiceUniqueRemittanceIdentifier | UNIQUE_REMITTANCE_IDENTIFIER | — | — |
| 123 | InvoiceUriCheckDigit | URI_CHECK_DIGIT | — | — |
| 124 | InvoiceUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 125 | InvoiceUssglTransactionCode | USSGL_TRANSACTION_CODE | — | — |
| 126 | InvoiceUssglTrxCodeContext | USSGL_TRX_CODE_CONTEXT | — | — |
| 127 | InvoiceValidatedTaxAmount | VALIDATED_TAX_AMOUNT | — | — |
| 128 | InvoiceValidationRequestId | VALIDATION_REQUEST_ID | — | — |
| 129 | InvoiceVendorContactId | VENDOR_CONTACT_ID | — | — |
| 130 | InvoiceVendorId | VENDOR_ID | — | — |
| 131 | InvoiceVendorSiteId | VENDOR_SITE_ID | — | — |
| 132 | InvoiceVoucherNum | VOUCHER_NUM | — | — |
| 133 | InvoiceWfapprovalStatus | WFAPPROVAL_STATUS | — | — |

### [[exm_credit_card_trxns|EXM_CREDIT_CARD_TRXNS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpCreditCardTrxAirAgencyNumber | AIR_AGENCY_NUMBER | — | — |
| 2 | ExpCreditCardTrxAirArrivalCity | AIR_ARRIVAL_CITY | — | — |
| 3 | ExpCreditCardTrxAirArrivalDate | AIR_ARRIVAL_DATE | — | — |
| 4 | ExpCreditCardTrxAirBaseFareAmount | AIR_BASE_FARE_AMOUNT | — | — |
| 5 | ExpCreditCardTrxAirCarrierAbbreviation | AIR_CARRIER_ABBREVIATION | — | — |
| 6 | ExpCreditCardTrxAirCarrierCode | AIR_CARRIER_CODE | — | — |
| 7 | ExpCreditCardTrxAirDepartureCity | AIR_DEPARTURE_CITY | — | — |
| 8 | ExpCreditCardTrxAirDepartureDate | AIR_DEPARTURE_DATE | — | — |
| 9 | ExpCreditCardTrxAirExchangedTicketNumber | AIR_EXCHANGED_TICKET_NUMBER | — | — |
| 10 | ExpCreditCardTrxAirFareBasisCode | AIR_FARE_BASIS_CODE | — | — |
| 11 | ExpCreditCardTrxAirIssuerCity | AIR_ISSUER_CITY | — | — |
| 12 | ExpCreditCardTrxAirPassengerName | AIR_PASSENGER_NAME | — | — |
| 13 | ExpCreditCardTrxAirRefundTicketNumber | AIR_REFUND_TICKET_NUMBER | — | — |
| 14 | ExpCreditCardTrxAirRouting | AIR_ROUTING | — | — |
| 15 | ExpCreditCardTrxAirServiceClass | AIR_SERVICE_CLASS | — | — |
| 16 | ExpCreditCardTrxAirStopoverFlag | AIR_STOPOVER_FLAG | — | — |
| 17 | ExpCreditCardTrxAirTicketIssuer | AIR_TICKET_ISSUER | — | — |
| 18 | ExpCreditCardTrxAirTicketNumber | AIR_TICKET_NUMBER | — | — |
| 19 | ExpCreditCardTrxAirTotalFeesAmount | AIR_TOTAL_FEES_AMOUNT | — | — |
| 20 | ExpCreditCardTrxAtmCashAdvance | ATM_CASH_ADVANCE | — | — |
| 21 | ExpCreditCardTrxAtmFeeAmount | ATM_FEE_AMOUNT | — | — |
| 22 | ExpCreditCardTrxAtmId | ATM_ID | — | — |
| 23 | ExpCreditCardTrxAtmNetworkId | ATM_NETWORK_ID | — | — |
| 24 | ExpCreditCardTrxAtmTransactionDate | ATM_TRANSACTION_DATE | — | — |
| 25 | ExpCreditCardTrxAtmType | ATM_TYPE | — | — |
| 26 | ExpCreditCardTrxAudioVisualCharges | AUDIO_VISUAL_CHARGES | — | — |
| 27 | ExpCreditCardTrxAuthTrxnNumber | AUTH_TRXN_NUMBER | — | — |
| 28 | ExpCreditCardTrxBanquetCharges | BANQUET_CHARGES | — | — |
| 29 | ExpCreditCardTrxBilledAmount | BILLED_AMOUNT | — | — |
| 30 | ExpCreditCardTrxBilledCurrencyCode | BILLED_CURRENCY_CODE | — | — |
| 31 | ExpCreditCardTrxBilledDate | BILLED_DATE | — | — |
| 32 | ExpCreditCardTrxBilledDecimal | BILLED_DECIMAL | — | — |
| 33 | ExpCreditCardTrxBillingCntlAcctNumber | BILLING_CNTL_ACCT_NUMBER | — | — |
| 34 | ExpCreditCardTrxCarClass | CAR_CLASS | — | — |
| 35 | ExpCreditCardTrxCarDailyRate | CAR_DAILY_RATE | — | — |
| 36 | ExpCreditCardTrxCarGasAmount | CAR_GAS_AMOUNT | — | — |
| 37 | ExpCreditCardTrxCarInsuranceAmount | CAR_INSURANCE_AMOUNT | — | — |
| 38 | ExpCreditCardTrxCarMileageAmount | CAR_MILEAGE_AMOUNT | — | — |
| 39 | ExpCreditCardTrxCarRentalAgreementNumber | CAR_RENTAL_AGREEMENT_NUMBER | — | — |
| 40 | ExpCreditCardTrxCarRentalDate | CAR_RENTAL_DATE | — | — |
| 41 | ExpCreditCardTrxCarRentalDays | CAR_RENTAL_DAYS | — | — |
| 42 | ExpCreditCardTrxCarRentalLocation | CAR_RENTAL_LOCATION | — | — |
| 43 | ExpCreditCardTrxCarRentalState | CAR_RENTAL_STATE | — | — |
| 44 | ExpCreditCardTrxCarRenterName | CAR_RENTER_NAME | — | — |
| 45 | ExpCreditCardTrxCarReturnDate | CAR_RETURN_DATE | — | — |
| 46 | ExpCreditCardTrxCarReturnLocation | CAR_RETURN_LOCATION | — | — |
| 47 | ExpCreditCardTrxCarReturnState | CAR_RETURN_STATE | — | — |
| 48 | ExpCreditCardTrxCarTotalMileage | CAR_TOTAL_MILEAGE | — | — |
| 49 | ExpCreditCardTrxCardAcceptorId | CARD_ACCEPTOR_ID | — | — |
| 50 | ExpCreditCardTrxCardId | CARD_ID | — | — |
| 51 | ExpCreditCardTrxCardIssuerNumber | CARD_ISSUER_NUMBER | — | — |
| 52 | ExpCreditCardTrxCardNumber | CARD_NUMBER | — | — |
| 53 | ExpCreditCardTrxCardProgramId | CARD_PROGRAM_ID | — | — |
| 54 | ExpCreditCardTrxCashAdvances | CASH_ADVANCES | — | — |
| 55 | ExpCreditCardTrxCompanyAccountId | COMPANY_ACCOUNT_ID | — | — |
| 56 | ExpCreditCardTrxCompanyNumber | COMPANY_NUMBER | — | — |
| 57 | ExpCreditCardTrxConferenceRoomCharges | CONFERENCE_ROOM_CHARGES | — | — |
| 58 | ExpCreditCardTrxCreatedBy | CREATED_BY | — | — |
| 59 | ExpCreditCardTrxCreationDate | CREATION_DATE | — | — |
| 60 | ExpCreditCardTrxCreditCardTrxnId | CREDIT_CARD_TRXN_ID | — | — |
| 61 | ExpCreditCardTrxCurrencyConversionExponent | CURRENCY_CONVERSION_EXPONENT | — | — |
| 62 | ExpCreditCardTrxCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | — |
| 63 | ExpCreditCardTrxDebitFlag | DEBIT_FLAG | — | — |
| 64 | ExpCreditCardTrxDescription | DESCRIPTION | — | — |
| 65 | ExpCreditCardTrxDisputeDate | DISPUTE_DATE | — | — |
| 66 | ExpCreditCardTrxEarlyDepartureCharges | EARLY_DEPARTURE_CHARGES | — | — |
| 67 | ExpCreditCardTrxEmployeeNumber | EMPLOYEE_NUMBER | — | — |
| 68 | ExpCreditCardTrxFinancialCategory | FINANCIAL_CATEGORY | — | — |
| 69 | ExpCreditCardTrxFolioType | FOLIO_TYPE | — | — |
| 70 | ExpCreditCardTrxHotelArrivalDate | HOTEL_ARRIVAL_DATE | — | — |
| 71 | ExpCreditCardTrxHotelBarAmount | HOTEL_BAR_AMOUNT | — | — |
| 72 | ExpCreditCardTrxHotelBusinessAmount | HOTEL_BUSINESS_AMOUNT | — | — |
| 73 | ExpCreditCardTrxHotelCashDisbAmount | HOTEL_CASH_DISB_AMOUNT | — | — |
| 74 | ExpCreditCardTrxHotelChargeDesc | HOTEL_CHARGE_DESC | — | — |
| 75 | ExpCreditCardTrxHotelCity | HOTEL_CITY | — | — |
| 76 | ExpCreditCardTrxHotelDepartDate | HOTEL_DEPART_DATE | — | — |
| 77 | ExpCreditCardTrxHotelFolioNumber | HOTEL_FOLIO_NUMBER | — | — |
| 78 | ExpCreditCardTrxHotelGiftShopAmount | HOTEL_GIFT_SHOP_AMOUNT | — | — |
| 79 | ExpCreditCardTrxHotelGuestName | HOTEL_GUEST_NAME | — | — |
| 80 | ExpCreditCardTrxHotelHealthAmount | HOTEL_HEALTH_AMOUNT | — | — |
| 81 | ExpCreditCardTrxHotelLaundryAmount | HOTEL_LAUNDRY_AMOUNT | — | — |
| 82 | ExpCreditCardTrxHotelMiscAmount | HOTEL_MISC_AMOUNT | — | — |
| 83 | ExpCreditCardTrxHotelMovieAmount | HOTEL_MOVIE_AMOUNT | — | — |
| 84 | ExpCreditCardTrxHotelNoShowFlag | HOTEL_NO_SHOW_FLAG | — | — |
| 85 | ExpCreditCardTrxHotelParkingAmount | HOTEL_PARKING_AMOUNT | — | — |
| 86 | ExpCreditCardTrxHotelRestaurantAmount | HOTEL_RESTAURANT_AMOUNT | — | — |
| 87 | ExpCreditCardTrxHotelRoomAmount | HOTEL_ROOM_AMOUNT | — | — |
| 88 | ExpCreditCardTrxHotelRoomRate | HOTEL_ROOM_RATE | — | — |
| 89 | ExpCreditCardTrxHotelRoomServiceAmount | HOTEL_ROOM_SERVICE_AMOUNT | — | — |
| 90 | ExpCreditCardTrxHotelRoomTax | HOTEL_ROOM_TAX | — | — |
| 91 | ExpCreditCardTrxHotelRoomType | HOTEL_ROOM_TYPE | — | — |
| 92 | ExpCreditCardTrxHotelState | HOTEL_STATE | — | — |
| 93 | ExpCreditCardTrxHotelStayDuration | HOTEL_STAY_DURATION | — | — |
| 94 | ExpCreditCardTrxHotelTelephoneAmount | HOTEL_TELEPHONE_AMOUNT | — | — |
| 95 | ExpCreditCardTrxHotelTipAmount | HOTEL_TIP_AMOUNT | — | — |
| 96 | ExpCreditCardTrxHotelTransportationAmount | HOTEL_TRANSPORTATION_AMOUNT | — | — |
| 97 | ExpCreditCardTrxInterbankCardassocNumber | INTERBANK_CARDASSOC_NUMBER | — | — |
| 98 | ExpCreditCardTrxInternetAccessCharges | INTERNET_ACCESS_CHARGES | — | — |
| 99 | ExpCreditCardTrxLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 100 | ExpCreditCardTrxLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 101 | ExpCreditCardTrxLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 102 | ExpCreditCardTrxLocalTax | LOCAL_TAX | — | — |
| 103 | ExpCreditCardTrxMarketCode | MARKET_CODE | — | — |
| 104 | ExpCreditCardTrxMerchantActivity | MERCHANT_ACTIVITY | — | — |
| 105 | ExpCreditCardTrxMerchantAddress1 | MERCHANT_ADDRESS1 | — | — |
| 106 | ExpCreditCardTrxMerchantAddress2 | MERCHANT_ADDRESS2 | — | — |
| 107 | ExpCreditCardTrxMerchantAddress3 | MERCHANT_ADDRESS3 | — | — |
| 108 | ExpCreditCardTrxMerchantAddress4 | MERCHANT_ADDRESS4 | — | — |
| 109 | ExpCreditCardTrxMerchantCategoryCode | MERCHANT_CATEGORY_CODE | — | — |
| 110 | ExpCreditCardTrxMerchantCity | MERCHANT_CITY | — | — |
| 111 | ExpCreditCardTrxMerchantCountry | MERCHANT_COUNTRY | — | — |
| 112 | ExpCreditCardTrxMerchantName1 | MERCHANT_NAME1 | — | — |
| 113 | ExpCreditCardTrxMerchantName2 | MERCHANT_NAME2 | — | — |
| 114 | ExpCreditCardTrxMerchantPostalCode | MERCHANT_POSTAL_CODE | — | — |
| 115 | ExpCreditCardTrxMerchantProvinceState | MERCHANT_PROVINCE_STATE | — | — |
| 116 | ExpCreditCardTrxMerchantReference | MERCHANT_REFERENCE | — | — |
| 117 | ExpCreditCardTrxMerchantTaxId | MERCHANT_TAX_ID | — | — |
| 118 | ExpCreditCardTrxMiniBarAmount | MINI_BAR_AMOUNT | — | — |
| 119 | ExpCreditCardTrxMisIndustryCode | MIS_INDUSTRY_CODE | — | — |
| 120 | ExpCreditCardTrxNationalTax | NATIONAL_TAX | — | — |
| 121 | ExpCreditCardTrxObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 122 | ExpCreditCardTrxOtherTax | OTHER_TAX | — | — |
| 123 | ExpCreditCardTrxPaymentDueFromCode | PAYMENT_DUE_FROM_CODE | — | — |
| 124 | ExpCreditCardTrxPaymentFlag | PAYMENT_FLAG | — | — |
| 125 | ExpCreditCardTrxPostedAmount | POSTED_AMOUNT | — | — |
| 126 | ExpCreditCardTrxPostedCurrencyCode | POSTED_CURRENCY_CODE | — | — |
| 127 | ExpCreditCardTrxPostedDate | POSTED_DATE | — | — |
| 128 | ExpCreditCardTrxPostedDecimal | POSTED_DECIMAL | — | — |
| 129 | ExpCreditCardTrxRecordType | RECORD_TYPE | — | — |
| 130 | ExpCreditCardTrxReferenceNumber | REFERENCE_NUMBER | — | ✅ |
| 131 | ExpCreditCardTrxReqCntlAcctNumber | REQ_CNTL_ACCT_NUMBER | — | — |
| 132 | ExpCreditCardTrxRequestId | REQUEST_ID | — | — |
| 133 | ExpCreditCardTrxRestaurantBeverageAmount | RESTAURANT_BEVERAGE_AMOUNT | — | — |
| 134 | ExpCreditCardTrxRestaurantFoodAmount | RESTAURANT_FOOD_AMOUNT | — | — |
| 135 | ExpCreditCardTrxRestaurantTipAmount | RESTAURANT_TIP_AMOUNT | — | — |
| 136 | ExpCreditCardTrxReviewedFlag | REVIEWED_FLAG | — | — |
| 137 | ExpCreditCardTrxSicCode | SIC_CODE | — | — |
| 138 | ExpCreditCardTrxTotalTax | TOTAL_TAX | — | — |
| 139 | ExpCreditCardTrxTransactionAmount | TRANSACTION_AMOUNT | — | — |
| 140 | ExpCreditCardTrxTransactionDate | TRANSACTION_DATE | — | — |
| 141 | ExpCreditCardTrxTransactionStatus | TRANSACTION_STATUS | — | — |
| 142 | ExpCreditCardTrxTransactionType | TRANSACTION_TYPE | — | — |
| 143 | ExpCreditCardTrxTransportationCharges | TRANSPORTATION_CHARGES | — | — |
| 144 | ExpCreditCardTrxTrxnAvailableDate | TRXN_AVAILABLE_DATE | — | — |
| 145 | ExpCreditCardTrxTrxnDetailFlag | TRXN_DETAIL_FLAG | — | — |
| 146 | ExpCreditCardTrxValidateCode | VALIDATE_CODE | — | — |

### [[exm_expenses|EXM_EXPENSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpAllocationReason | ALLOCATION_REASON | — | — |
| 2 | ExpAllocationSplitCode | ALLOCATION_SPLIT_CODE | — | — |
| 3 | ExpAssignmentId | ASSIGNMENT_ID | — | — |
| 4 | ExpAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 5 | ExpAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 6 | ExpAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 7 | ExpAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 8 | ExpAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 9 | ExpAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 10 | ExpAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 11 | ExpAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 12 | ExpAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 13 | ExpAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 14 | ExpAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 15 | ExpAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 16 | ExpAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 17 | ExpAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 18 | ExpAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 19 | ExpAuditAdjustmentReason | AUDIT_ADJUSTMENT_REASON | — | — |
| 20 | ExpAuditAdjustmentReasonCode | AUDIT_ADJUSTMENT_REASON_CODE | — | ✅ |
| 21 | ExpAvgMileageRate | AVG_MILEAGE_RATE | — | ✅ |
| 22 | ExpAwtGroupId | AWT_GROUP_ID | — | — |
| 23 | ExpCardId | CARD_ID | — | — |
| 24 | ExpCcPrepaidInvoiceId | CC_PREPAID_INVOICE_ID | — | — |
| 25 | ExpCheckoutDate | CHECKOUT_DATE | — | — |
| 26 | ExpCountryOfSupply | COUNTRY_OF_SUPPLY | — | — |
| 27 | ExpCreatedBy | CREATED_BY | — | ✅ |
| 28 | ExpCreationDate | CREATION_DATE | — | ✅ |
| 29 | ExpCreditCardTrxnId | CREDIT_CARD_TRXN_ID | — | — |
| 30 | ExpDailyDistance | DAILY_DISTANCE | — | ✅ |
| 31 | ExpDepartureLocationId | DEPARTURE_LOCATION_ID | — | — |
| 32 | ExpDescription | DESCRIPTION | — | ✅ |
| 33 | ExpDestinationFrom | DESTINATION_FROM | — | ✅ |
| 34 | ExpDestinationTo | DESTINATION_TO | — | ✅ |
| 35 | ExpDistanceUnitCode | DISTANCE_UNIT_CODE | — | ✅ |
| 36 | ExpEmpDefaultCostCenter | EMP_DEFAULT_COST_CENTER | — | ✅ |
| 37 | ExpEndDate | END_DATE | — | ✅ |
| 38 | ExpExchangeRate | EXCHANGE_RATE | — | ✅ |
| 39 | ExpExpenseCategoryCode | EXPENSE_CATEGORY_CODE | — | ✅ |
| 40 | ExpExpenseId | EXPENSE_ID | — | ✅ |
| 41 | ExpExpenseReportId | EXPENSE_REPORT_ID | — | ✅ |
| 42 | ExpExpenseSource | EXPENSE_SOURCE | — | ✅ |
| 43 | ExpExpenseTemplateId | EXPENSE_TEMPLATE_ID | — | — |
| 44 | ExpExpenseTypeCategoryCode | EXPENSE_TYPE_CATEGORY_CODE | — | ✅ |
| 45 | ExpExpenseTypeId | EXPENSE_TYPE_ID | — | ✅ |
| 46 | ExpFlightNumber | FLIGHT_NUMBER | — | ✅ |
| 47 | ExpFuelType | FUEL_TYPE | — | ✅ |
| 48 | ExpFuncCurrencyAmount | FUNC_CURRENCY_AMOUNT | — | ✅ |
| 49 | ExpInactiveEmpProcessId | INACTIVE_EMP_PROCESS_ID | — | — |
| 50 | ExpItemizationParentExpenseId | ITEMIZATION_PARENT_EXPENSE_ID | — | ✅ |
| 51 | ExpJustification | JUSTIFICATION | — | ✅ |
| 52 | ExpJustificationRequiredFlag | JUSTIFICATION_REQUIRED_FLAG | — | ✅ |
| 53 | ExpLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 54 | ExpLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 55 | ExpLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 56 | ExpLicensePlateNumber | LICENSE_PLATE_NUMBER | — | — |
| 57 | ExpLocation | LOCATION | — | ✅ |
| 58 | ExpLocationId | LOCATION_ID | — | ✅ |
| 59 | ExpMerchantDocumentNumber | MERCHANT_DOCUMENT_NUMBER | — | ✅ |
| 60 | ExpMerchantName | MERCHANT_NAME | — | ✅ |
| 61 | ExpMerchantReference | MERCHANT_REFERENCE | — | — |
| 62 | ExpMerchantTaxRegNumber | MERCHANT_TAX_REG_NUMBER | — | — |
| 63 | ExpMerchantTaxpayerId | MERCHANT_TAXPAYER_ID | — | — |
| 64 | ExpMileageRateAdjustedFlag | MILEAGE_RATE_ADJUSTED_FLAG | — | — |
| 65 | ExpNumberOfAttendees | NUMBER_OF_ATTENDEES | — | ✅ |
| 66 | ExpNumberPeople | NUMBER_PEOPLE | — | — |
| 67 | ExpObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 68 | ExpOrgId | ORG_ID | — | ✅ |
| 69 | ExpOrigReimbursableAmount | ORIG_REIMBURSABLE_AMOUNT | — | ✅ |
| 70 | ExpPassengerAmount | PASSENGER_AMOUNT | — | — |
| 71 | ExpPassengerRateType | PASSENGER_RATE_TYPE | — | — |
| 72 | ExpPersonId | PERSON_ID | — | — |
| 73 | ExpPolicyShortpayFlag | POLICY_SHORTPAY_FLAG | — | ✅ |
| 74 | ExpPolicyViolatedFlag | POLICY_VIOLATED_FLAG | — | ✅ |
| 75 | ExpPreparerId | PREPARER_ID | — | — |
| 76 | ExpRangeHigh | RANGE_HIGH | — | — |
| 77 | ExpRangeLow | RANGE_LOW | — | — |
| 78 | ExpRatePerPassenger | RATE_PER_PASSENGER | — | — |
| 79 | ExpReceiptAmount | RECEIPT_AMOUNT | — | — |
| 80 | ExpReceiptCurrencyCode | RECEIPT_CURRENCY_CODE | — | ✅ |
| 81 | ExpReceiptMissingFlag | RECEIPT_MISSING_FLAG | — | ✅ |
| 82 | ExpReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | ✅ |
| 83 | ExpReceiptVerifiedFlag | RECEIPT_VERIFIED_FLAG | — | ✅ |
| 84 | ExpReimbursableAmount | REIMBURSABLE_AMOUNT | — | ✅ |
| 85 | ExpReimbursementCurrencyCode | REIMBURSEMENT_CURRENCY_CODE | — | ✅ |
| 86 | ExpSequenceNum | SEQUENCE_NUM | — | ✅ |
| 87 | ExpStartDate | START_DATE | — | ✅ |
| 88 | ExpTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | ✅ |
| 89 | ExpTicketClassCode | TICKET_CLASS_CODE | — | ✅ |
| 90 | ExpTicketNumber | TICKET_NUMBER | — | ✅ |
| 91 | ExpTravelType | TRAVEL_TYPE | — | ✅ |
| 92 | ExpTripDistance | TRIP_DISTANCE | — | ✅ |
| 93 | ExpUomDays | UOM_DAYS | — | — |
| 94 | ExpVehicleCategoryCode | VEHICLE_CATEGORY_CODE | — | ✅ |
| 95 | ExpVehicleType | VEHICLE_TYPE | — | ✅ |
| 96 | FullExpExpenseCMC | EXPENSE_CREATION_METHOD_CODE | — | — |

### [[exm_expense_dists|EXM_EXPENSE_DISTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpDistCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 2 | ExpDistCostCenter | COST_CENTER | — | ✅ |
| 3 | ExpDistCreatedBy | CREATED_BY | — | ✅ |
| 4 | ExpDistCreationDate | CREATION_DATE | — | ✅ |
| 5 | ExpDistExpenseId | EXPENSE_ID | — | — |
| 6 | ExpDistExpenseReportId | EXPENSE_REPORT_ID | — | — |
| 7 | ExpDistLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ExpDistLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ExpDistLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ExpDistObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ExpDistOrgId | ORG_ID | — | — |
| 12 | ExpDistPjcBillableFlag | PJC_BILLABLE_FLAG | — | — |
| 13 | ExpDistPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | — |
| 14 | ExpDistPjcContextCategory | PJC_CONTEXT_CATEGORY | — | — |
| 15 | ExpDistPjcContractId | PJC_CONTRACT_ID | — | — |
| 16 | ExpDistPjcContractLineId | PJC_CONTRACT_LINE_ID | — | — |
| 17 | ExpDistPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 18 | ExpDistPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | ✅ |
| 19 | ExpDistPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | — |
| 20 | ExpDistPjcOrganizationId | PJC_ORGANIZATION_ID | — | ✅ |
| 21 | ExpDistPjcProjectId | PJC_PROJECT_ID | — | ✅ |
| 22 | ExpDistPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 23 | ExpDistPjcReservedAttribute10 | PJC_RESERVED_ATTRIBUTE10 | — | — |
| 24 | ExpDistPjcReservedAttribute2 | PJC_RESERVED_ATTRIBUTE2 | — | — |
| 25 | ExpDistPjcReservedAttribute3 | PJC_RESERVED_ATTRIBUTE3 | — | — |
| 26 | ExpDistPjcReservedAttribute4 | PJC_RESERVED_ATTRIBUTE4 | — | — |
| 27 | ExpDistPjcReservedAttribute5 | PJC_RESERVED_ATTRIBUTE5 | — | — |
| 28 | ExpDistPjcReservedAttribute6 | PJC_RESERVED_ATTRIBUTE6 | — | — |
| 29 | ExpDistPjcReservedAttribute7 | PJC_RESERVED_ATTRIBUTE7 | — | — |
| 30 | ExpDistPjcReservedAttribute8 | PJC_RESERVED_ATTRIBUTE8 | — | — |
| 31 | ExpDistPjcReservedAttribute9 | PJC_RESERVED_ATTRIBUTE9 | — | — |
| 32 | ExpDistPjcTaskId | PJC_TASK_ID | — | ✅ |
| 33 | ExpDistPjcUserDefAttribute1 | PJC_USER_DEF_ATTRIBUTE1 | — | — |
| 34 | ExpDistPjcUserDefAttribute10 | PJC_USER_DEF_ATTRIBUTE10 | — | — |
| 35 | ExpDistPjcUserDefAttribute2 | PJC_USER_DEF_ATTRIBUTE2 | — | — |
| 36 | ExpDistPjcUserDefAttribute3 | PJC_USER_DEF_ATTRIBUTE3 | — | — |
| 37 | ExpDistPjcUserDefAttribute4 | PJC_USER_DEF_ATTRIBUTE4 | — | — |
| 38 | ExpDistPjcUserDefAttribute5 | PJC_USER_DEF_ATTRIBUTE5 | — | — |
| 39 | ExpDistPjcUserDefAttribute6 | PJC_USER_DEF_ATTRIBUTE6 | — | — |
| 40 | ExpDistPjcUserDefAttribute7 | PJC_USER_DEF_ATTRIBUTE7 | — | — |
| 41 | ExpDistPjcUserDefAttribute8 | PJC_USER_DEF_ATTRIBUTE8 | — | — |
| 42 | ExpDistPjcUserDefAttribute9 | PJC_USER_DEF_ATTRIBUTE9 | — | — |
| 43 | ExpDistPjcWorkTypeId | PJC_WORK_TYPE_ID | — | — |
| 44 | ExpDistPreparerModifiedFlag | PREPARER_MODIFIED_FLAG | — | — |
| 45 | ExpDistReimbursableAmount | REIMBURSABLE_AMOUNT | — | ✅ |
| 46 | ExpDistSegment1 | SEGMENT1 | — | ✅ |
| 47 | ExpDistSegment10 | SEGMENT10 | — | — |
| 48 | ExpDistSegment11 | SEGMENT11 | — | — |
| 49 | ExpDistSegment12 | SEGMENT12 | — | — |
| 50 | ExpDistSegment13 | SEGMENT13 | — | — |
| 51 | ExpDistSegment14 | SEGMENT14 | — | — |
| 52 | ExpDistSegment15 | SEGMENT15 | — | — |
| 53 | ExpDistSegment16 | SEGMENT16 | — | — |
| 54 | ExpDistSegment17 | SEGMENT17 | — | — |
| 55 | ExpDistSegment18 | SEGMENT18 | — | — |
| 56 | ExpDistSegment19 | SEGMENT19 | — | — |
| 57 | ExpDistSegment2 | SEGMENT2 | — | — |
| 58 | ExpDistSegment20 | SEGMENT20 | — | — |
| 59 | ExpDistSegment21 | SEGMENT21 | — | — |
| 60 | ExpDistSegment22 | SEGMENT22 | — | — |
| 61 | ExpDistSegment23 | SEGMENT23 | — | — |
| 62 | ExpDistSegment24 | SEGMENT24 | — | — |
| 63 | ExpDistSegment25 | SEGMENT25 | — | — |
| 64 | ExpDistSegment26 | SEGMENT26 | — | — |
| 65 | ExpDistSegment27 | SEGMENT27 | — | — |
| 66 | ExpDistSegment28 | SEGMENT28 | — | — |
| 67 | ExpDistSegment29 | SEGMENT29 | — | — |
| 68 | ExpDistSegment3 | SEGMENT3 | — | ✅ |
| 69 | ExpDistSegment30 | SEGMENT30 | — | — |
| 70 | ExpDistSegment4 | SEGMENT4 | — | — |
| 71 | ExpDistSegment5 | SEGMENT5 | — | — |
| 72 | ExpDistSegment6 | SEGMENT6 | — | — |
| 73 | ExpDistSegment7 | SEGMENT7 | — | — |
| 74 | ExpDistSegment8 | SEGMENT8 | — | — |
| 75 | ExpDistSegment9 | SEGMENT9 | — | — |
| 76 | ExpDistSequenceNum | SEQUENCE_NUM | — | ✅ |
| 77 | ExpenseDistId | EXPENSE_DIST_ID | 🔑 | ✅ |

### [[exm_expense_reports|EXM_EXPENSE_REPORTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpHdrAssignmentId | ASSIGNMENT_ID | — | — |
| 2 | ExpHdrAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 3 | ExpHdrAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 4 | ExpHdrAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 5 | ExpHdrAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 6 | ExpHdrAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 7 | ExpHdrAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 8 | ExpHdrAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 9 | ExpHdrAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 10 | ExpHdrAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 11 | ExpHdrAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 12 | ExpHdrAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 13 | ExpHdrAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 14 | ExpHdrAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 15 | ExpHdrAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 16 | ExpHdrAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 17 | ExpHdrAuditCode | AUDIT_CODE | — | ✅ |
| 18 | ExpHdrAuditReturnReasonCode | AUDIT_RETURN_REASON_CODE | — | ✅ |
| 19 | ExpHdrAwtGroupId | AWT_GROUP_ID | — | — |
| 20 | ExpHdrBothpayFlag | BOTHPAY_FLAG | — | — |
| 21 | ExpHdrCashExpensePaidDate | CASH_EXPENSE_PAID_DATE | — | ✅ |
| 22 | ExpHdrCreatedBy | CREATED_BY | — | ✅ |
| 23 | ExpHdrCreationDate | CREATION_DATE | — | ✅ |
| 24 | ExpHdrCurrentApproverId | CURRENT_APPROVER_ID | — | ✅ |
| 25 | ExpHdrExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 26 | ExpHdrExpRepProcessingId | EXP_REP_PROCESSING_ID | — | — |
| 27 | ExpHdrExpenseReportDate | EXPENSE_REPORT_DATE | — | ✅ |
| 28 | ExpHdrExpenseReportId | EXPENSE_REPORT_ID | — | ✅ |
| 29 | ExpHdrExpenseReportNum | EXPENSE_REPORT_NUM | — | ✅ |
| 30 | ExpHdrExpenseReportTotal | EXPENSE_REPORT_TOTAL | — | ✅ |
| 31 | ExpHdrExpenseStatusCode | EXPENSE_STATUS_CODE | — | ✅ |
| 32 | ExpHdrExpenseStatusDate | EXPENSE_STATUS_DATE | — | ✅ |
| 33 | ExpHdrExportRejectCode | EXPORT_REJECT_CODE | — | — |
| 34 | ExpHdrExportRequestId | EXPORT_REQUEST_ID | — | — |
| 35 | ExpHdrFinalApprovalDate | FINAL_APPROVAL_DATE | — | ✅ |
| 36 | ExpHdrHoldingExpenseReportId | HOLDING_EXPENSE_REPORT_ID | — | — |
| 37 | ExpHdrImagedReceiptsStatusCode | IMAGED_RECEIPTS_STATUS_CODE | — | ✅ |
| 38 | ExpHdrLastAuditBy | LAST_AUDIT_BY | — | — |
| 39 | ExpHdrLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 40 | ExpHdrLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 41 | ExpHdrLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 42 | ExpHdrObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 43 | ExpHdrOrgId | ORG_ID | — | ✅ |
| 44 | ExpHdrOverrideApproverId | OVERRIDE_APPROVER_ID | — | ✅ |
| 45 | ExpHdrParentExpenseReportId | PARENT_EXPENSE_REPORT_ID | — | ✅ |
| 46 | ExpHdrPaymentMethodCode | PAYMENT_METHOD_CODE | — | ✅ |
| 47 | ExpHdrPersonId | PERSON_ID | — | ✅ |
| 48 | ExpHdrPreparerId | PREPARER_ID | — | — |
| 49 | ExpHdrPrntAssignmentId | ASSIGNMENT_ID | — | — |
| 50 | ExpHdrPrntAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 51 | ExpHdrPrntAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 52 | ExpHdrPrntAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 53 | ExpHdrPrntAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 54 | ExpHdrPrntAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 55 | ExpHdrPrntAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 56 | ExpHdrPrntAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 57 | ExpHdrPrntAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 58 | ExpHdrPrntAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 59 | ExpHdrPrntAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 60 | ExpHdrPrntAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 61 | ExpHdrPrntAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 62 | ExpHdrPrntAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 63 | ExpHdrPrntAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 64 | ExpHdrPrntAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 65 | ExpHdrPrntAuditCode | AUDIT_CODE | — | — |
| 66 | ExpHdrPrntAuditReturnReasonCode | AUDIT_RETURN_REASON_CODE | — | — |
| 67 | ExpHdrPrntAwtGroupId | AWT_GROUP_ID | — | — |
| 68 | ExpHdrPrntBothpayFlag | BOTHPAY_FLAG | — | — |
| 69 | ExpHdrPrntCreatedBy | CREATED_BY | — | — |
| 70 | ExpHdrPrntCurrentApproverId | CURRENT_APPROVER_ID | — | — |
| 71 | ExpHdrPrntExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 72 | ExpHdrPrntExpRepProcessingId | EXP_REP_PROCESSING_ID | — | — |
| 73 | ExpHdrPrntExpenseReportDate | EXPENSE_REPORT_DATE | — | — |
| 74 | ExpHdrPrntExpenseReportId | EXPENSE_REPORT_ID | — | — |
| 75 | ExpHdrPrntExpenseReportNum | EXPENSE_REPORT_NUM | — | ✅ |
| 76 | ExpHdrPrntExpenseReportTotal | EXPENSE_REPORT_TOTAL | — | — |
| 77 | ExpHdrPrntExpenseStatusCode | EXPENSE_STATUS_CODE | — | — |
| 78 | ExpHdrPrntExpenseStatusDate | EXPENSE_STATUS_DATE | — | — |
| 79 | ExpHdrPrntExportRejectCode | EXPORT_REJECT_CODE | — | — |
| 80 | ExpHdrPrntExportRequestId | EXPORT_REQUEST_ID | — | — |
| 81 | ExpHdrPrntHoldingExpenseReportId | HOLDING_EXPENSE_REPORT_ID | — | — |
| 82 | ExpHdrPrntLastAuditBy | LAST_AUDIT_BY | — | — |
| 83 | ExpHdrPrntLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 84 | ExpHdrPrntLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 85 | ExpHdrPrntLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 86 | ExpHdrPrntObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 87 | ExpHdrPrntOrgId | ORG_ID | — | — |
| 88 | ExpHdrPrntOverrideApproverId | OVERRIDE_APPROVER_ID | — | — |
| 89 | ExpHdrPrntParentExpenseReportId | PARENT_EXPENSE_REPORT_ID | — | — |
| 90 | ExpHdrPrntPersonId | PERSON_ID | — | — |
| 91 | ExpHdrPrntPreparerId | PREPARER_ID | — | — |
| 92 | ExpHdrPrntPurpose | PURPOSE | — | — |
| 93 | ExpHdrPrntReceiptsFilingNumber | RECEIPTS_FILING_NUMBER | — | — |
| 94 | ExpHdrPrntReceiptsReceivedDate | RECEIPTS_RECEIVED_DATE | — | — |
| 95 | ExpHdrPrntReceiptsStatusCode | RECEIPTS_STATUS_CODE | — | — |
| 96 | ExpHdrPrntReimbursementCurrencyCode | REIMBURSEMENT_CURRENCY_CODE | — | — |
| 97 | ExpHdrPrntReportSubmitDate | REPORT_SUBMIT_DATE | — | — |
| 98 | ExpHdrPrntShortpayTypeCode | SHORTPAY_TYPE_CODE | — | — |
| 99 | ExpHdrPrntUnappliedAdvancesJust | UNAPPLIED_ADVANCES_JUST | — | — |
| 100 | ExpHdrPurpose | PURPOSE | — | ✅ |
| 101 | ExpHdrReceiptsFilingNumber | RECEIPTS_FILING_NUMBER | — | ✅ |
| 102 | ExpHdrReceiptsReceivedDate | RECEIPTS_RECEIVED_DATE | — | ✅ |
| 103 | ExpHdrReceiptsStatusCode | RECEIPTS_STATUS_CODE | — | ✅ |
| 104 | ExpHdrReimbursementCurrencyCode | REIMBURSEMENT_CURRENCY_CODE | — | ✅ |
| 105 | ExpHdrReportSubmitDate | REPORT_SUBMIT_DATE | — | ✅ |
| 106 | ExpHdrShortpayTypeCode | SHORTPAY_TYPE_CODE | — | ✅ |
| 107 | ExpHdrUnappliedAdvancesJust | UNAPPLIED_ADVANCES_JUST | — | — |
| 108 | FullReportCMC | REPORT_CREATION_METHOD_CODE | — | — |

### [[exm_expense_templates|EXM_EXPENSE_TEMPLATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenseTemplatePEOAllowRcptMissingFlag | ALLOW_RCPT_MISSING_FLAG | — | — |
| 2 | ExpenseTemplatePEOCashReceiptReqFlag | CASH_RECEIPT_REQ_FLAG | — | — |
| 3 | ExpenseTemplatePEOCashReceiptReqLimit | CASH_RECEIPT_REQ_LIMIT | — | — |
| 4 | ExpenseTemplatePEOCcReceiptReqFlag | CC_RECEIPT_REQ_FLAG | — | — |
| 5 | ExpenseTemplatePEOCcReceiptReqLimit | CC_RECEIPT_REQ_LIMIT | — | — |
| 6 | ExpenseTemplatePEOCreatedBy | CREATED_BY | — | — |
| 7 | ExpenseTemplatePEOCreationDate | CREATION_DATE | — | — |
| 8 | ExpenseTemplatePEODescription | DESCRIPTION | — | — |
| 9 | ExpenseTemplatePEODfltCcExpTypeId | DFLT_CC_EXP_TYPE_ID | — | — |
| 10 | ExpenseTemplatePEODispRcptViolationFlag | DISP_RCPT_VIOLATION_FLAG | — | — |
| 11 | ExpenseTemplatePEOEnableCcMappingFlag | ENABLE_CC_MAPPING_FLAG | — | — |
| 12 | ExpenseTemplatePEOExpenseTemplateId | EXPENSE_TEMPLATE_ID | — | — |
| 13 | ExpenseTemplatePEOInactiveDate | INACTIVE_DATE | — | — |
| 14 | ExpenseTemplatePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 15 | ExpenseTemplatePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | ExpenseTemplatePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | ExpenseTemplatePEOName | NAME | — | ✅ |
| 18 | ExpenseTemplatePEONegativeRcptReqFlag | NEGATIVE_RCPT_REQ_FLAG | — | — |
| 19 | ExpenseTemplatePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | ExpenseTemplatePEOOrgId | ORG_ID | — | — |
| 21 | ExpenseTemplatePEOStartDate | START_DATE | — | — |

### [[exm_expense_types|EXM_EXPENSE_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenseTypePEOCategoryCode | CATEGORY_CODE | — | — |
| 2 | ExpenseTypePEOCcReceiptRequiredFlag | CC_RECEIPT_REQUIRED_FLAG | — | — |
| 3 | ExpenseTypePEOCcReceiptThreshold | CC_RECEIPT_THRESHOLD | — | — |
| 4 | ExpenseTypePEOCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 5 | ExpenseTypePEOCreatedBy | CREATED_BY | — | — |
| 6 | ExpenseTypePEOCreationDate | CREATION_DATE | — | — |
| 7 | ExpenseTypePEODefaultProjExpendType | DEFAULT_PROJ_EXPEND_TYPE | — | — |
| 8 | ExpenseTypePEODescription | DESCRIPTION | — | — |
| 9 | ExpenseTypePEODispRcptViolationFlag | DISP_RCPT_VIOLATION_FLAG | — | — |
| 10 | ExpenseTypePEOEnableProjectsFlag | ENABLE_PROJECTS_FLAG | — | — |
| 11 | ExpenseTypePEOEndDate | END_DATE | — | — |
| 12 | ExpenseTypePEOExpenseTemplateId | EXPENSE_TEMPLATE_ID | — | — |
| 13 | ExpenseTypePEOExpenseTypeId | EXPENSE_TYPE_ID | — | — |
| 14 | ExpenseTypePEOItemizationBehaviourCode | ITEMIZATION_BEHAVIOUR_CODE | — | — |
| 15 | ExpenseTypePEOItemizationOnlyFlag | ITEMIZATION_ONLY_FLAG | — | — |
| 16 | ExpenseTypePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 17 | ExpenseTypePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | ExpenseTypePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | ExpenseTypePEOName | NAME | — | ✅ |
| 20 | ExpenseTypePEONegativeRcptReqCode | NEGATIVE_RCPT_REQ_CODE | — | — |
| 21 | ExpenseTypePEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 22 | ExpenseTypePEOOrgId1 | ORG_ID | — | — |
| 23 | ExpenseTypePEORcptRequiredProjFlag | RCPT_REQUIRED_PROJ_FLAG | — | — |
| 24 | ExpenseTypePEOReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 25 | ExpenseTypePEOReceiptThreshold | RECEIPT_THRESHOLD | — | — |
| 26 | ExpenseTypePEOStartDate | START_DATE | — | — |
| 27 | ExpenseTypePEOTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUBusinessUnitId | BU_ID | — | — |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceConversionTypeConversionType | CONVERSION_TYPE | — | — |
| 2 | InvoiceConversionTypeCreatedBy | CREATED_BY | — | — |
| 3 | InvoiceConversionTypeCreationDate | CREATION_DATE | — | — |
| 4 | InvoiceConversionTypeDescription | DESCRIPTION | — | — |
| 5 | InvoiceConversionTypeEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 6 | InvoiceConversionTypeEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 7 | InvoiceConversionTypeFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 8 | InvoiceConversionTypeFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 9 | InvoiceConversionTypeFemScenario | FEM_SCENARIO | — | — |
| 10 | InvoiceConversionTypeFemTimeframe | FEM_TIMEFRAME | — | — |
| 11 | InvoiceConversionTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | InvoiceConversionTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | InvoiceConversionTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | InvoiceConversionTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | InvoiceConversionTypePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 16 | InvoiceConversionTypeSecurityFlag | SECURITY_FLAG | — | — |
| 17 | InvoiceConversionTypeUserConversionType | USER_CONVERSION_TYPE | — | — |
| 18 | InvoiceConversionTypeUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |
| 19 | PaymentConversionTypeConversionType | CONVERSION_TYPE | — | — |
| 20 | PaymentConversionTypeCreatedBy | CREATED_BY | — | — |
| 21 | PaymentConversionTypeCreationDate | CREATION_DATE | — | — |
| 22 | PaymentConversionTypeDescription | DESCRIPTION | — | — |
| 23 | PaymentConversionTypeEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 24 | PaymentConversionTypeEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 25 | PaymentConversionTypeFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 26 | PaymentConversionTypeFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 27 | PaymentConversionTypeFemScenario | FEM_SCENARIO | — | — |
| 28 | PaymentConversionTypeFemTimeframe | FEM_TIMEFRAME | — | — |
| 29 | PaymentConversionTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | PaymentConversionTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 31 | PaymentConversionTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 32 | PaymentConversionTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 33 | PaymentConversionTypePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 34 | PaymentConversionTypeSecurityFlag | SECURITY_FLAG | — | — |
| 35 | PaymentConversionTypeUserConversionType | USER_CONVERSION_TYPE | — | — |
| 36 | PaymentConversionTypeUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |
| 37 | RateTypeConversionType | CONVERSION_TYPE | — | — |
| 38 | RateTypeCreatedBy | CREATED_BY | — | — |
| 39 | RateTypeCreationDate | CREATION_DATE | — | — |
| 40 | RateTypeDescription | DESCRIPTION | — | — |
| 41 | RateTypeEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 42 | RateTypeEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 43 | RateTypeFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 44 | RateTypeFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 45 | RateTypeFemScenario | FEM_SCENARIO | — | — |
| 46 | RateTypeFemTimeframe | FEM_TIMEFRAME | — | — |
| 47 | RateTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 48 | RateTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 49 | RateTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 50 | RateTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 51 | RateTypePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 52 | RateTypeSecurityFlag | SECURITY_FLAG | — | — |
| 53 | RateTypeUserConversionType | USER_CONVERSION_TYPE | — | — |
| 54 | RateTypeUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlLedgersAccountedPeriodType | ACCOUNTED_PERIOD_TYPE | — | — |
| 2 | GlLedgersAlcLedgerTypeCode | ALC_LEDGER_TYPE_CODE | — | — |
| 3 | GlLedgersAllowIntercompanyPostFlag | ALLOW_INTERCOMPANY_POST_FLAG | — | — |
| 4 | GlLedgersApDocSequencingOptionFlag | AP_DOC_SEQUENCING_OPTION_FLAG | — | — |
| 5 | GlLedgersArDocSequencingOptionFlag | AR_DOC_SEQUENCING_OPTION_FLAG | — | — |
| 6 | GlLedgersAutomateSecJrnlRevFlag | AUTOMATE_SEC_JRNL_REV_FLAG | — | — |
| 7 | GlLedgersAutomaticallyCreatedFlag | AUTOMATICALLY_CREATED_FLAG | — | — |
| 8 | GlLedgersAutorevAfterOpenPrdFlag | AUTOREV_AFTER_OPEN_PRD_FLAG | — | — |
| 9 | GlLedgersBalSegColumnName | BAL_SEG_COLUMN_NAME | — | — |
| 10 | GlLedgersBalSegValueOptionCode | BAL_SEG_VALUE_OPTION_CODE | — | — |
| 11 | GlLedgersBalSegValueSetId | BAL_SEG_VALUE_SET_ID | — | — |
| 12 | GlLedgersBudgetPeriodAvgRateType | BUDGET_PERIOD_AVG_RATE_TYPE | — | — |
| 13 | GlLedgersBudgetPeriodEndRateType | BUDGET_PERIOD_END_RATE_TYPE | — | — |
| 14 | GlLedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 15 | GlLedgersCompleteFlag | COMPLETE_FLAG | — | — |
| 16 | GlLedgersCompletionStatusCode | COMPLETION_STATUS_CODE | — | — |
| 17 | GlLedgersConfigurationId | CONFIGURATION_ID | — | — |
| 18 | GlLedgersConsolidationLedgerFlag | CONSOLIDATION_LEDGER_FLAG | — | — |
| 19 | GlLedgersCreateJeFlag | CREATE_JE_FLAG | — | — |
| 20 | GlLedgersCreatedBy | CREATED_BY | — | — |
| 21 | GlLedgersCreationDate | CREATION_DATE | — | — |
| 22 | GlLedgersCriteriaSetId | CRITERIA_SET_ID | — | — |
| 23 | GlLedgersCumTransCodeCombinationId | CUM_TRANS_CODE_COMBINATION_ID | — | — |
| 24 | GlLedgersCurrencyCode | CURRENCY_CODE | — | — |
| 25 | GlLedgersDailyTranslationRateType | DAILY_TRANSLATION_RATE_TYPE | — | — |
| 26 | GlLedgersDescription | DESCRIPTION | — | — |
| 27 | GlLedgersEnableAutomaticTaxFlag | ENABLE_AUTOMATIC_TAX_FLAG | — | — |
| 28 | GlLedgersEnableAverageBalancesFlag | ENABLE_AVERAGE_BALANCES_FLAG | — | — |
| 29 | GlLedgersEnableBudgetaryControlFlag | ENABLE_BUDGETARY_CONTROL_FLAG | — | — |
| 30 | GlLedgersEnableJeApprovalFlag | ENABLE_JE_APPROVAL_FLAG | — | — |
| 31 | GlLedgersEnableReconciliationFlag | ENABLE_RECONCILIATION_FLAG | — | — |
| 32 | GlLedgersEnableRevalSsTrackFlag | ENABLE_REVAL_SS_TRACK_FLAG | — | — |
| 33 | GlLedgersEnableSecondaryTrackFlag | ENABLE_SECONDARY_TRACK_FLAG | — | — |
| 34 | GlLedgersEnfSeqDateCorrelationCode | ENF_SEQ_DATE_CORRELATION_CODE | — | — |
| 35 | GlLedgersFirstLedgerPeriodName | FIRST_LEDGER_PERIOD_NAME | — | — |
| 36 | GlLedgersFutureEnterablePeriodsLimit | FUTURE_ENTERABLE_PERIODS_LIMIT | — | — |
| 37 | GlLedgersImplicitAccessSetId | IMPLICIT_ACCESS_SET_ID | — | — |
| 38 | GlLedgersImplicitLedgerSetId | IMPLICIT_LEDGER_SET_ID | — | — |
| 39 | GlLedgersIntercoGainLossCcid | INTERCO_GAIN_LOSS_CCID | — | — |
| 40 | GlLedgersJrnlsGroupByDateFlag | JRNLS_GROUP_BY_DATE_FLAG | — | — |
| 41 | GlLedgersLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 42 | GlLedgersLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 43 | GlLedgersLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 44 | GlLedgersLatestEncumbranceYear | LATEST_ENCUMBRANCE_YEAR | — | — |
| 45 | GlLedgersLatestOpenedPeriodName | LATEST_OPENED_PERIOD_NAME | — | — |
| 46 | GlLedgersLeLedgerTypeCode | LE_LEDGER_TYPE_CODE | — | — |
| 47 | GlLedgersLedgerAttributes | LEDGER_ATTRIBUTES | — | — |
| 48 | GlLedgersLedgerCategoryCode | LEDGER_CATEGORY_CODE | — | — |
| 49 | GlLedgersLedgerId | LEDGER_ID | — | — |
| 50 | GlLedgersMgtSegColumnName | MGT_SEG_COLUMN_NAME | — | — |
| 51 | GlLedgersMgtSegValueOptionCode | MGT_SEG_VALUE_OPTION_CODE | — | — |
| 52 | GlLedgersMgtSegValueSetId | MGT_SEG_VALUE_SET_ID | — | — |
| 53 | GlLedgersName | NAME | — | — |
| 54 | GlLedgersNetClosingBalFlag | NET_CLOSING_BAL_FLAG | — | — |
| 55 | GlLedgersNetIncomeCodeCombinationId | NET_INCOME_CODE_COMBINATION_ID | — | — |
| 56 | GlLedgersObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 57 | GlLedgersObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 58 | GlLedgersPeriodAverageRateType | PERIOD_AVERAGE_RATE_TYPE | — | — |
| 59 | GlLedgersPeriodEndRateType | PERIOD_END_RATE_TYPE | — | — |
| 60 | GlLedgersPeriodSetName | PERIOD_SET_NAME | — | — |
| 61 | GlLedgersPopUpStatAccountFlag | POP_UP_STAT_ACCOUNT_FLAG | — | — |
| 62 | GlLedgersPriorPrdNotificationFlag | PRIOR_PRD_NOTIFICATION_FLAG | — | — |
| 63 | GlLedgersRequireBudgetJournalsFlag | REQUIRE_BUDGET_JOURNALS_FLAG | — | — |
| 64 | GlLedgersResEncumbCodeCombinationId | RES_ENCUMB_CODE_COMBINATION_ID | — | — |
| 65 | GlLedgersRetEarnCodeCombinationId | RET_EARN_CODE_COMBINATION_ID | — | — |
| 66 | GlLedgersRevalFromPriLgrCurr | REVAL_FROM_PRI_LGR_CURR | — | — |
| 67 | GlLedgersRoundingCodeCombinationId | ROUNDING_CODE_COMBINATION_ID | — | — |
| 68 | GlLedgersSequencingModeCode | SEQUENCING_MODE_CODE | — | — |
| 69 | GlLedgersShortName | SHORT_NAME | — | — |
| 70 | GlLedgersSlaAccountingMethodCode | SLA_ACCOUNTING_METHOD_CODE | — | — |
| 71 | GlLedgersSlaAccountingMethodType | SLA_ACCOUNTING_METHOD_TYPE | — | — |
| 72 | GlLedgersSlaBalByLedgerCurrFlag | SLA_BAL_BY_LEDGER_CURR_FLAG | — | — |
| 73 | GlLedgersSlaDescriptionLanguage | SLA_DESCRIPTION_LANGUAGE | — | — |
| 74 | GlLedgersSlaEnteredCurBalSusCcid | SLA_ENTERED_CUR_BAL_SUS_CCID | — | — |
| 75 | GlLedgersSlaLedgerCashBasisFlag | SLA_LEDGER_CASH_BASIS_FLAG | — | — |
| 76 | GlLedgersSlaLedgerCurBalSusCcid | SLA_LEDGER_CUR_BAL_SUS_CCID | — | — |
| 77 | GlLedgersSlaSequencingFlag | SLA_SEQUENCING_FLAG | — | — |
| 78 | GlLedgersSuspenseAllowedFlag | SUSPENSE_ALLOWED_FLAG | — | — |
| 79 | GlLedgersThresholdAmount | THRESHOLD_AMOUNT | — | — |
| 80 | GlLedgersTrackRoundingImbalanceFlag | TRACK_ROUNDING_IMBALANCE_FLAG | — | — |
| 81 | GlLedgersTransactionCalendarId | TRANSACTION_CALENDAR_ID | — | — |
| 82 | GlLedgersTranslateEodFlag | TRANSLATE_EOD_FLAG | — | — |
| 83 | GlLedgersTranslateQatdFlag | TRANSLATE_QATD_FLAG | — | — |
| 84 | GlLedgersTranslateYatdFlag | TRANSLATE_YATD_FLAG | — | — |
| 85 | GlLedgersUssglOptionCode | USSGL_OPTION_CODE | — | — |
| 86 | GlLedgersValidateJournalRefDate | VALIDATE_JOURNAL_REF_DATE | — | — |

### [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | OrganizationEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | OrganizationLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 4 | OrganizationOrganizationId | ORGANIZATION_ID | — | — |

### [[hr_all_organization_units_f_vl|HR_ALL_ORGANIZATION_UNITS_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationUnitActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | OrganizationUnitAttribute1 | ATTRIBUTE1 | — | — |
| 3 | OrganizationUnitAttribute10 | ATTRIBUTE10 | — | — |
| 4 | OrganizationUnitAttribute11 | ATTRIBUTE11 | — | — |
| 5 | OrganizationUnitAttribute12 | ATTRIBUTE12 | — | — |
| 6 | OrganizationUnitAttribute13 | ATTRIBUTE13 | — | — |
| 7 | OrganizationUnitAttribute14 | ATTRIBUTE14 | — | — |
| 8 | OrganizationUnitAttribute15 | ATTRIBUTE15 | — | — |
| 9 | OrganizationUnitAttribute16 | ATTRIBUTE16 | — | — |
| 10 | OrganizationUnitAttribute17 | ATTRIBUTE17 | — | — |
| 11 | OrganizationUnitAttribute18 | ATTRIBUTE18 | — | — |
| 12 | OrganizationUnitAttribute19 | ATTRIBUTE19 | — | — |
| 13 | OrganizationUnitAttribute2 | ATTRIBUTE2 | — | — |
| 14 | OrganizationUnitAttribute20 | ATTRIBUTE20 | — | — |
| 15 | OrganizationUnitAttribute21 | ATTRIBUTE21 | — | — |
| 16 | OrganizationUnitAttribute22 | ATTRIBUTE22 | — | — |
| 17 | OrganizationUnitAttribute23 | ATTRIBUTE23 | — | — |
| 18 | OrganizationUnitAttribute24 | ATTRIBUTE24 | — | — |
| 19 | OrganizationUnitAttribute25 | ATTRIBUTE25 | — | — |
| 20 | OrganizationUnitAttribute26 | ATTRIBUTE26 | — | — |
| 21 | OrganizationUnitAttribute27 | ATTRIBUTE27 | — | — |
| 22 | OrganizationUnitAttribute28 | ATTRIBUTE28 | — | — |
| 23 | OrganizationUnitAttribute29 | ATTRIBUTE29 | — | — |
| 24 | OrganizationUnitAttribute3 | ATTRIBUTE3 | — | — |
| 25 | OrganizationUnitAttribute30 | ATTRIBUTE30 | — | — |
| 26 | OrganizationUnitAttribute4 | ATTRIBUTE4 | — | — |
| 27 | OrganizationUnitAttribute5 | ATTRIBUTE5 | — | — |
| 28 | OrganizationUnitAttribute6 | ATTRIBUTE6 | — | — |
| 29 | OrganizationUnitAttribute7 | ATTRIBUTE7 | — | — |
| 30 | OrganizationUnitAttribute8 | ATTRIBUTE8 | — | — |
| 31 | OrganizationUnitAttribute9 | ATTRIBUTE9 | — | — |
| 32 | OrganizationUnitAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 33 | OrganizationUnitBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 34 | OrganizationUnitCostAllocationKeyflexId | COST_ALLOCATION_KEYFLEX_ID | — | — |
| 35 | OrganizationUnitCreatedBy | CREATED_BY | — | — |
| 36 | OrganizationUnitCreationDate | CREATION_DATE | — | — |
| 37 | OrganizationUnitEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 38 | OrganizationUnitEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 39 | OrganizationUnitEstablishmentId | ESTABLISHMENT_ID | — | — |
| 40 | OrganizationUnitInternalAddressLine | INTERNAL_ADDRESS_LINE | — | — |
| 41 | OrganizationUnitInternalExternalFlag | INTERNAL_EXTERNAL_FLAG | — | — |
| 42 | OrganizationUnitLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 43 | OrganizationUnitLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 44 | OrganizationUnitLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 45 | OrganizationUnitLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 46 | OrganizationUnitLocationId | LOCATION_ID | — | — |
| 47 | OrganizationUnitName | NAME | — | ✅ |
| 48 | OrganizationUnitObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 49 | OrganizationUnitOrganizationCode | ORGANIZATION_CODE | — | — |
| 50 | OrganizationUnitOrganizationId | ORGANIZATION_ID | — | — |
| 51 | OrganizationUnitType | TYPE | — | — |

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUPrimaryLedgerId | ORG_INFORMATION3 | — | — |
| 2 | OrgInfoEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | OrgInfoEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | OrgInfoOrgInformationId | ORG_INFORMATION_ID | — | — |

### [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvExtBnkAcctAccountClassification | ACCOUNT_CLASSIFICATION | — | — |
| 2 | InvExtBnkAcctAccountSuffix | ACCOUNT_SUFFIX | — | — |
| 3 | InvExtBnkAcctAgencyLocationCode | AGENCY_LOCATION_CODE | — | — |
| 4 | InvExtBnkAcctBaMaskSetting | BA_MASK_SETTING | — | — |
| 5 | InvExtBnkAcctBaNumElecSecSegmentId | BA_NUM_ELEC_SEC_SEGMENT_ID | — | — |
| 6 | InvExtBnkAcctBaNumSecSegmentId | BA_NUM_SEC_SEGMENT_ID | — | — |
| 7 | InvExtBnkAcctBaUnmaskLength | BA_UNMASK_LENGTH | — | — |
| 8 | InvExtBnkAcctBankAccountName | BANK_ACCOUNT_NAME | — | — |
| 9 | InvExtBnkAcctBankAccountNameAlt | BANK_ACCOUNT_NAME_ALT | — | — |
| 10 | InvExtBnkAcctBankAccountNum | BANK_ACCOUNT_NUM | — | — |
| 11 | InvExtBnkAcctBankAccountNumElectronic | BANK_ACCOUNT_NUM_ELECTRONIC | — | — |
| 12 | InvExtBnkAcctBankAccountNumHash1 | BANK_ACCOUNT_NUM_HASH1 | — | — |
| 13 | InvExtBnkAcctBankAccountNumHash2 | BANK_ACCOUNT_NUM_HASH2 | — | — |
| 14 | InvExtBnkAcctBankAccountType | BANK_ACCOUNT_TYPE | — | — |
| 15 | InvExtBnkAcctBankId | BANK_ID | — | — |
| 16 | InvExtBnkAcctBranchId | BRANCH_ID | — | — |
| 17 | InvExtBnkAcctCheckDigits | CHECK_DIGITS | — | — |
| 18 | InvExtBnkAcctCountryCode | COUNTRY_CODE | — | — |
| 19 | InvExtBnkAcctCreatedBy | CREATED_BY | — | — |
| 20 | InvExtBnkAcctCreationDate | CREATION_DATE | — | — |
| 21 | InvExtBnkAcctCurrencyCode | CURRENCY_CODE | — | — |
| 22 | InvExtBnkAcctDescription | DESCRIPTION | — | — |
| 23 | InvExtBnkAcctEncrypted | ENCRYPTED | — | — |
| 24 | InvExtBnkAcctEndDate | END_DATE | — | — |
| 25 | InvExtBnkAcctExchangeRate | EXCHANGE_RATE | — | — |
| 26 | InvExtBnkAcctExchangeRateAgreementNum | EXCHANGE_RATE_AGREEMENT_NUM | — | — |
| 27 | InvExtBnkAcctExchangeRateAgreementType | EXCHANGE_RATE_AGREEMENT_TYPE | — | — |
| 28 | InvExtBnkAcctExtBankAccountId | EXT_BANK_ACCOUNT_ID | — | — |
| 29 | InvExtBnkAcctForeignPaymentUseFlag | FOREIGN_PAYMENT_USE_FLAG | — | — |
| 30 | InvExtBnkAcctHedgingContractReference | HEDGING_CONTRACT_REFERENCE | — | — |
| 31 | InvExtBnkAcctIban | IBAN | — | — |
| 32 | InvExtBnkAcctIbanHash1 | IBAN_HASH1 | — | — |
| 33 | InvExtBnkAcctIbanHash2 | IBAN_HASH2 | — | — |
| 34 | InvExtBnkAcctIbanSecSegmentId | IBAN_SEC_SEGMENT_ID | — | — |
| 35 | InvExtBnkAcctLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 36 | InvExtBnkAcctLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 37 | InvExtBnkAcctLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 38 | InvExtBnkAcctMaskedBankAccountNum | MASKED_BANK_ACCOUNT_NUM | — | — |
| 39 | InvExtBnkAcctMaskedIban | MASKED_IBAN | — | — |
| 40 | InvExtBnkAcctObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 41 | InvExtBnkAcctPaymentFactorFlag | PAYMENT_FACTOR_FLAG | — | — |
| 42 | InvExtBnkAcctProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 43 | InvExtBnkAcctProgramId | PROGRAM_ID | — | — |
| 44 | InvExtBnkAcctProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 45 | InvExtBnkAcctRequestId | REQUEST_ID | — | — |
| 46 | InvExtBnkAcctSaltVersion | SALT_VERSION | — | — |
| 47 | InvExtBnkAcctSecondaryAccountReference | SECONDARY_ACCOUNT_REFERENCE | — | — |
| 48 | InvExtBnkAcctShortAcctName | SHORT_ACCT_NAME | — | — |
| 49 | InvExtBnkAcctStartDate | START_DATE | — | — |

### [[iby_payment_codes_vl|IBY_PAYMENT_CODES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayDelcodeCreatedBy | CREATED_BY | — | — |
| 2 | PayDelcodeCreationDate | CREATION_DATE | — | — |
| 3 | PayDelcodeDescription | DESCRIPTION | — | — |
| 4 | PayDelcodeEndDate | END_DATE | — | — |
| 5 | PayDelcodeFormatValue | FORMAT_VALUE | — | — |
| 6 | PayDelcodeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PayDelcodeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | PayDelcodeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | PayDelcodeMeaning | MEANING | — | — |
| 10 | PayDelcodeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | PayDelcodePaymentCode | PAYMENT_CODE | — | — |
| 12 | PayDelcodePaymentCodeType | PAYMENT_CODE_TYPE | — | — |
| 13 | PayDelcodeSeededFlag | SEEDED_FLAG | — | — |
| 14 | PayDelcodeStartDate | START_DATE | — | — |
| 15 | PayDelcodeTerritoryCode | TERRITORY_CODE | — | — |
| 16 | PayReacodeCreatedBy | CREATED_BY | — | — |
| 17 | PayReacodeCreationDate | CREATION_DATE | — | — |
| 18 | PayReacodeDescription | DESCRIPTION | — | — |
| 19 | PayReacodeEndDate | END_DATE | — | — |
| 20 | PayReacodeFormatValue | FORMAT_VALUE | — | — |
| 21 | PayReacodeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | PayReacodeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 23 | PayReacodeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 24 | PayReacodeMeaning | MEANING | — | — |
| 25 | PayReacodeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 26 | PayReacodePaymentCode | PAYMENT_CODE | — | — |
| 27 | PayReacodePaymentCodeType | PAYMENT_CODE_TYPE | — | — |
| 28 | PayReacodeSeededFlag | SEEDED_FLAG | — | — |
| 29 | PayReacodeStartDate | START_DATE | — | — |
| 30 | PayReacodeTerritoryCode | TERRITORY_CODE | — | — |

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentAssignmentId | ASSIGNMENT_ID | — | — |
| 2 | AssignmentEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | AssignmentEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 4 | AssignmentEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 5 | AssignmentEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 6 | AssignmentExpenseCheckAddress | EXPENSE_CHECK_ADDRESS | — | ✅ |
| 7 | AssignmentLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 8 | AssignmentPersonId | PERSON_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistPersonCreatedByDisplayName | DISPLAY_NAME | — | — |
| 2 | DistPersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | DistPersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | DistPersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | DistPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | DistPersonUpadatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 7 | DistPersonUpdatedByDisplayName | DISPLAY_NAME | — | — |
| 8 | DistPersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 9 | DistPersonUpdatedByLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | DistPersonUpdatedByPersonId | PERSON_ID | — | — |
| 11 | DistPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |
| 12 | ExpHdrPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 13 | ExpHdrPersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 14 | ExpHdrPersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 15 | ExpHdrPersonUpdatedByPersonId | PERSON_ID | — | — |
| 16 | ExpHdrPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |
| 17 | ExpHdrPreparerNameDisplayName | DISPLAY_NAME | — | ✅ |
| 18 | ExpHdrPreparerNameEffEndDate | EFFECTIVE_END_DATE | — | — |
| 19 | ExpHdrPreparerNameEffStartDate | EFFECTIVE_START_DATE | — | — |
| 20 | ExpHdrPreparerNamePersonNameId | PERSON_NAME_ID | — | — |
| 21 | ExpPersonCreatedByPersonId | PERSON_ID | — | — |
| 22 | ExpPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 23 | ExpPersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 24 | ExpPersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 25 | ExpPersonUpdatedByPersonId | PERSON_ID | — | — |
| 26 | ExpPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |
| 27 | ExpenHdrPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 28 | ExpenHdrPersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 29 | ExpenHdrPersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 30 | ExpenHdrPersonCreatedByPersonId | PERSON_ID | — | — |
| 31 | ExpenHdrPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 32 | ExpenPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 33 | ExpenPersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 34 | ExpenPersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 35 | ExpenPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 36 | PersonNamePEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 37 | PersonNamePEOCreatedBy1 | CREATED_BY | — | — |
| 38 | PersonNamePEOCreationDate1 | CREATION_DATE | — | — |
| 39 | PersonNamePEODisplayName | DISPLAY_NAME | — | ✅ |
| 40 | PersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 41 | PersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 42 | PersonNamePEOFirstName | FIRST_NAME | — | — |
| 43 | PersonNamePEOFullName | FULL_NAME | — | — |
| 44 | PersonNamePEOHonors | HONORS | — | — |
| 45 | PersonNamePEOKnownAs | KNOWN_AS | — | — |
| 46 | PersonNamePEOLastName | LAST_NAME | — | — |
| 47 | PersonNamePEOLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 48 | PersonNamePEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 49 | PersonNamePEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 50 | PersonNamePEOLegislationCode | LEGISLATION_CODE | — | — |
| 51 | PersonNamePEOListName | LIST_NAME | — | — |
| 52 | PersonNamePEOMiddleNames | MIDDLE_NAMES | — | — |
| 53 | PersonNamePEOMilitaryRank | MILITARY_RANK | — | — |
| 54 | PersonNamePEONamInformation1 | NAM_INFORMATION1 | — | — |
| 55 | PersonNamePEONamInformation10 | NAM_INFORMATION10 | — | — |
| 56 | PersonNamePEONamInformation11 | NAM_INFORMATION11 | — | — |
| 57 | PersonNamePEONamInformation12 | NAM_INFORMATION12 | — | — |
| 58 | PersonNamePEONamInformation13 | NAM_INFORMATION13 | — | — |
| 59 | PersonNamePEONamInformation14 | NAM_INFORMATION14 | — | — |
| 60 | PersonNamePEONamInformation15 | NAM_INFORMATION15 | — | — |
| 61 | PersonNamePEONamInformation16 | NAM_INFORMATION16 | — | — |
| 62 | PersonNamePEONamInformation17 | NAM_INFORMATION17 | — | — |
| 63 | PersonNamePEONamInformation18 | NAM_INFORMATION18 | — | — |
| 64 | PersonNamePEONamInformation19 | NAM_INFORMATION19 | — | — |
| 65 | PersonNamePEONamInformation2 | NAM_INFORMATION2 | — | — |
| 66 | PersonNamePEONamInformation20 | NAM_INFORMATION20 | — | — |
| 67 | PersonNamePEONamInformation21 | NAM_INFORMATION21 | — | — |
| 68 | PersonNamePEONamInformation22 | NAM_INFORMATION22 | — | — |
| 69 | PersonNamePEONamInformation23 | NAM_INFORMATION23 | — | — |
| 70 | PersonNamePEONamInformation24 | NAM_INFORMATION24 | — | — |
| 71 | PersonNamePEONamInformation25 | NAM_INFORMATION25 | — | — |
| 72 | PersonNamePEONamInformation26 | NAM_INFORMATION26 | — | — |
| 73 | PersonNamePEONamInformation27 | NAM_INFORMATION27 | — | — |
| 74 | PersonNamePEONamInformation28 | NAM_INFORMATION28 | — | — |
| 75 | PersonNamePEONamInformation29 | NAM_INFORMATION29 | — | — |
| 76 | PersonNamePEONamInformation3 | NAM_INFORMATION3 | — | — |
| 77 | PersonNamePEONamInformation30 | NAM_INFORMATION30 | — | — |
| 78 | PersonNamePEONamInformation4 | NAM_INFORMATION4 | — | — |
| 79 | PersonNamePEONamInformation5 | NAM_INFORMATION5 | — | — |
| 80 | PersonNamePEONamInformation6 | NAM_INFORMATION6 | — | — |
| 81 | PersonNamePEONamInformation7 | NAM_INFORMATION7 | — | — |
| 82 | PersonNamePEONamInformation8 | NAM_INFORMATION8 | — | — |
| 83 | PersonNamePEONamInformation9 | NAM_INFORMATION9 | — | — |
| 84 | PersonNamePEONamInformationCategory | NAM_INFORMATION_CATEGORY | — | — |
| 85 | PersonNamePEONameType | NAME_TYPE | — | — |
| 86 | PersonNamePEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 87 | PersonNamePEOOrderName | ORDER_NAME | — | — |
| 88 | PersonNamePEOPersonId1 | PERSON_ID | — | — |
| 89 | PersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |
| 90 | PersonNamePEOPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 91 | PersonNamePEOPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 92 | PersonNamePEOSuffix | SUFFIX | — | — |
| 93 | PersonNamePEOTitle | TITLE | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistUserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | DistUserCreatedByPersonId | PERSON_ID | — | — |
| 3 | DistUserCreatedByUserGuid | USER_GUID | — | — |
| 4 | DistUserCreatedByUserId | USER_ID | — | — |
| 5 | DistUserCreatedByUsername | USERNAME | — | — |
| 6 | DistUserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | DistUserUpdatedByPersonId | PERSON_ID | — | — |
| 8 | DistUserUpdatedByUserGuid | USER_GUID | — | — |
| 9 | DistUserUpdatedByUserId | USER_ID | — | — |
| 10 | DistUserUpdatedByUsername | USERNAME | — | — |
| 11 | ExpHdrUserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ExpHdrUserUpdatedByPersonId | PERSON_ID | — | — |
| 13 | ExpHdrUserUpdatedByUserGuid | USER_GUID | — | — |
| 14 | ExpHdrUserUpdatedByUserId | USER_ID | — | — |
| 15 | ExpHdrUserUpdatedByUsername | USERNAME | — | — |
| 16 | ExpUserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | ExpUserUpdatedByPersonId | PERSON_ID | — | — |
| 18 | ExpUserUpdatedByUserGuid | USER_GUID | — | — |
| 19 | ExpUserUpdatedByUserId | USER_ID | — | — |
| 20 | ExpUserUpdatedByUsername | USERNAME | — | — |
| 21 | ExpenCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | ExpenCreatedByPersonId | PERSON_ID | — | — |
| 23 | ExpenCreatedByUserGuid | USER_GUID | — | — |
| 24 | ExpenCreatedByUserId | USER_ID | — | — |
| 25 | ExpenCreatedByUsername | USERNAME | — | — |
| 26 | ExpenHdrCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 27 | ExpenHdrCreatedByPersonId | PERSON_ID | — | — |
| 28 | ExpenHdrCreatedByUserGuid | USER_GUID | — | — |
| 29 | ExpenHdrCreatedByUserId | USER_ID | — | — |
| 30 | ExpenHdrCreatedByUsername | USERNAME | — | — |

### [[pjf_exp_types_tl|PJF_EXP_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureTypeCreatedBy1 | CREATED_BY | — | — |
| 2 | ExpenditureTypeCreationDate1 | CREATION_DATE | — | — |
| 3 | ExpenditureTypeDescription | DESCRIPTION | — | ✅ |
| 4 | ExpenditureTypeExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 5 | ExpenditureTypeExpenditureTypeName | EXPENDITURE_TYPE_NAME | — | ✅ |
| 6 | ExpenditureTypeLanguage | LANGUAGE | — | — |
| 7 | ExpenditureTypeLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 8 | ExpenditureTypeLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 9 | ExpenditureTypeLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 10 | ExpenditureTypeObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |

### [[po_headers_all|PO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchaseOrderAcceptanceDueDate | ACCEPTANCE_DUE_DATE | — | — |
| 2 | PurchaseOrderAcceptanceRequiredFlag | ACCEPTANCE_REQUIRED_FLAG | — | — |
| 3 | PurchaseOrderAcceptanceWithinDays | ACCEPTANCE_WITHIN_DAYS | — | — |
| 4 | PurchaseOrderAgentId | AGENT_ID | — | — |
| 5 | PurchaseOrderAmountLimit | AMOUNT_LIMIT | — | — |
| 6 | PurchaseOrderAmountReleased | AMOUNT_RELEASED | — | — |
| 7 | PurchaseOrderApprovedDate | APPROVED_DATE | — | — |
| 8 | PurchaseOrderApprovedFlag | APPROVED_FLAG | — | — |
| 9 | PurchaseOrderAutoSourcingFlag | AUTO_SOURCING_FLAG | — | — |
| 10 | PurchaseOrderBillToLocationId | BILL_TO_LOCATION_ID | — | — |
| 11 | PurchaseOrderBlanketTotalAmount | BLANKET_TOTAL_AMOUNT | — | — |
| 12 | PurchaseOrderCancelFlag | CANCEL_FLAG | — | — |
| 13 | PurchaseOrderCarrierId | CARRIER_ID | — | — |
| 14 | PurchaseOrderCatAdminAuthEnabledFlag | CAT_ADMIN_AUTH_ENABLED_FLAG | — | — |
| 15 | PurchaseOrderCbcAccountingDate | CBC_ACCOUNTING_DATE | — | — |
| 16 | PurchaseOrderChangeRequestedBy | CHANGE_REQUESTED_BY | — | — |
| 17 | PurchaseOrderChangeSummary | CHANGE_SUMMARY | — | — |
| 18 | PurchaseOrderClosedDate | CLOSED_DATE | — | — |
| 19 | PurchaseOrderComments | COMMENTS | — | — |
| 20 | PurchaseOrderConfirmingOrderFlag | CONFIRMING_ORDER_FLAG | — | — |
| 21 | PurchaseOrderConsignedConsumptionFlag | CONSIGNED_CONSUMPTION_FLAG | — | — |
| 22 | PurchaseOrderConsumeReqDemandFlag | CONSUME_REQ_DEMAND_FLAG | — | — |
| 23 | PurchaseOrderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 24 | PurchaseOrderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 25 | PurchaseOrderContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 26 | PurchaseOrderCpaReference | CPA_REFERENCE | — | — |
| 27 | PurchaseOrderCreatedBy | CREATED_BY | — | — |
| 28 | PurchaseOrderCreatedLanguage | CREATED_LANGUAGE | — | — |
| 29 | PurchaseOrderCreationDate | CREATION_DATE | — | — |
| 30 | PurchaseOrderCurrencyCode | CURRENCY_CODE | — | — |
| 31 | PurchaseOrderCurrentVersionId | CURRENT_VERSION_ID | — | — |
| 32 | PurchaseOrderDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 33 | PurchaseOrderDocumentCreationMethod | DOCUMENT_CREATION_METHOD | — | — |
| 34 | PurchaseOrderDocumentStatus | DOCUMENT_STATUS | — | — |
| 35 | PurchaseOrderEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 36 | PurchaseOrderEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 37 | PurchaseOrderEmailAddress | EMAIL_ADDRESS | — | — |
| 38 | PurchaseOrderEnabledFlag | ENABLED_FLAG | — | — |
| 39 | PurchaseOrderEncumbranceRequiredFlag | ENCUMBRANCE_REQUIRED_FLAG | — | — |
| 40 | PurchaseOrderEndDate | END_DATE | — | — |
| 41 | PurchaseOrderFax | FAX | — | — |
| 42 | PurchaseOrderFirmDate | FIRM_DATE | — | — |
| 43 | PurchaseOrderFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 44 | PurchaseOrderFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 45 | PurchaseOrderFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 46 | PurchaseOrderFromHeaderId | FROM_HEADER_ID | — | — |
| 47 | PurchaseOrderFromTypeLookupCode | FROM_TYPE_LOOKUP_CODE | — | — |
| 48 | PurchaseOrderFrozenFlag | FROZEN_FLAG | — | — |
| 49 | PurchaseOrderGenerateOrdersAutomatic | GENERATE_ORDERS_AUTOMATIC | — | — |
| 50 | PurchaseOrderGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 51 | PurchaseOrderGroupRequisitionLines | GROUP_REQUISITION_LINES | — | — |
| 52 | PurchaseOrderGroupRequisitions | GROUP_REQUISITIONS | — | — |
| 53 | PurchaseOrderInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 54 | PurchaseOrderJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 55 | PurchaseOrderJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 56 | PurchaseOrderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 57 | PurchaseOrderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 58 | PurchaseOrderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 59 | PurchaseOrderLastUpdatedProgram | LAST_UPDATED_PROGRAM | — | — |
| 60 | PurchaseOrderMinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 61 | PurchaseOrderNoteToAuthorizer | NOTE_TO_AUTHORIZER | — | — |
| 62 | PurchaseOrderNoteToReceiver | NOTE_TO_RECEIVER | — | — |
| 63 | PurchaseOrderNoteToVendor | NOTE_TO_VENDOR | — | — |
| 64 | PurchaseOrderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 65 | PurchaseOrderPayOnCode | PAY_ON_CODE | — | — |
| 66 | PurchaseOrderPcardId | PCARD_ID | — | — |
| 67 | PurchaseOrderPendingSignatureFlag | PENDING_SIGNATURE_FLAG | — | — |
| 68 | PurchaseOrderPoHeaderId | PO_HEADER_ID | — | — |
| 69 | PurchaseOrderPrcBuId | PRC_BU_ID | — | — |
| 70 | PurchaseOrderPriceUpdateTolerance | PRICE_UPDATE_TOLERANCE | — | — |
| 71 | PurchaseOrderProgramAppName | PROGRAM_APP_NAME | — | — |
| 72 | PurchaseOrderProgramName | PROGRAM_NAME | — | — |
| 73 | PurchaseOrderRate | RATE | — | — |
| 74 | PurchaseOrderRateDate | RATE_DATE | — | — |
| 75 | PurchaseOrderRateType | RATE_TYPE | — | — |
| 76 | PurchaseOrderReferenceNum | REFERENCE_NUM | — | — |
| 77 | PurchaseOrderReleaseMethod | RELEASE_METHOD | — | — |
| 78 | PurchaseOrderReqBuId | REQ_BU_ID | — | — |
| 79 | PurchaseOrderRequestId | REQUEST_ID | — | — |
| 80 | PurchaseOrderRetroPriceApplyUpdatesFlag | RETRO_PRICE_APPLY_UPDATES_FLAG | — | — |
| 81 | PurchaseOrderRetroPriceCommUpdatesFlag | RETRO_PRICE_COMM_UPDATES_FLAG | — | — |
| 82 | PurchaseOrderReviewAutogeneratedReleases | REVIEW_AUTOGENERATED_RELEASES | — | — |
| 83 | PurchaseOrderRevisedDate | REVISED_DATE | — | — |
| 84 | PurchaseOrderRevisionNum | REVISION_NUM | — | — |
| 85 | PurchaseOrderSegment1 | SEGMENT1 | — | — |
| 86 | PurchaseOrderSegment2 | SEGMENT2 | — | — |
| 87 | PurchaseOrderSegment3 | SEGMENT3 | — | — |
| 88 | PurchaseOrderSegment4 | SEGMENT4 | — | — |
| 89 | PurchaseOrderSegment5 | SEGMENT5 | — | — |
| 90 | PurchaseOrderShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 91 | PurchaseOrderShippingControl | SHIPPING_CONTROL | — | — |
| 92 | PurchaseOrderStartDate | START_DATE | — | — |
| 93 | PurchaseOrderStyleId | STYLE_ID | — | — |
| 94 | PurchaseOrderSubmitApprovalAutomatic | SUBMIT_APPROVAL_AUTOMATIC | — | — |
| 95 | PurchaseOrderSubmitDate | SUBMIT_DATE | — | — |
| 96 | PurchaseOrderSummaryFlag | SUMMARY_FLAG | — | — |
| 97 | PurchaseOrderSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | — |
| 98 | PurchaseOrderTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 99 | PurchaseOrderTaxDocumentSubtype | TAX_DOCUMENT_SUBTYPE | — | — |
| 100 | PurchaseOrderTermsId | TERMS_ID | — | — |
| 101 | PurchaseOrderTypeLookupCode | TYPE_LOOKUP_CODE | — | — |
| 102 | PurchaseOrderUpdateSourcingRulesFlag | UPDATE_SOURCING_RULES_FLAG | — | — |
| 103 | PurchaseOrderUseNeedByDate | USE_NEED_BY_DATE | — | — |
| 104 | PurchaseOrderUseShipTo | USE_SHIP_TO | — | — |
| 105 | PurchaseOrderVendorContactId | VENDOR_CONTACT_ID | — | — |
| 106 | PurchaseOrderVendorId | VENDOR_ID | — | — |
| 107 | PurchaseOrderVendorOrderNum | VENDOR_ORDER_NUM | — | — |
| 108 | PurchaseOrderVendorSiteId | VENDOR_SITE_ID | — | — |
| 109 | PurchaseOrderXmlChangeSendDate | XML_CHANGE_SEND_DATE | — | — |
| 110 | PurchaseOrderXmlFlag | XML_FLAG | — | — |
| 111 | PurchaseOrderXmlSendDate | XML_SEND_DATE | — | — |
| 112 | QuickPurchaseOrderAcceptanceDueDate | ACCEPTANCE_DUE_DATE | — | — |
| 113 | QuickPurchaseOrderAcceptanceRequiredFlag | ACCEPTANCE_REQUIRED_FLAG | — | — |
| 114 | QuickPurchaseOrderAcceptanceWithinDays | ACCEPTANCE_WITHIN_DAYS | — | — |
| 115 | QuickPurchaseOrderAgentId | AGENT_ID | — | — |
| 116 | QuickPurchaseOrderAmountLimit | AMOUNT_LIMIT | — | — |
| 117 | QuickPurchaseOrderAmountReleased | AMOUNT_RELEASED | — | — |
| 118 | QuickPurchaseOrderApprovedDate | APPROVED_DATE | — | — |
| 119 | QuickPurchaseOrderApprovedFlag | APPROVED_FLAG | — | — |
| 120 | QuickPurchaseOrderAutoSourcingFlag | AUTO_SOURCING_FLAG | — | — |
| 121 | QuickPurchaseOrderBillToLocationId | BILL_TO_LOCATION_ID | — | — |
| 122 | QuickPurchaseOrderBlanketTotalAmount | BLANKET_TOTAL_AMOUNT | — | — |
| 123 | QuickPurchaseOrderCancelFlag | CANCEL_FLAG | — | — |
| 124 | QuickPurchaseOrderCarrierId | CARRIER_ID | — | — |
| 125 | QuickPurchaseOrderCatAdminAuthEnabledFlag | CAT_ADMIN_AUTH_ENABLED_FLAG | — | — |
| 126 | QuickPurchaseOrderCbcAccountingDate | CBC_ACCOUNTING_DATE | — | — |
| 127 | QuickPurchaseOrderChangeRequestedBy | CHANGE_REQUESTED_BY | — | — |
| 128 | QuickPurchaseOrderChangeSummary | CHANGE_SUMMARY | — | — |
| 129 | QuickPurchaseOrderClosedDate | CLOSED_DATE | — | — |
| 130 | QuickPurchaseOrderComments | COMMENTS | — | — |
| 131 | QuickPurchaseOrderConfirmingOrderFlag | CONFIRMING_ORDER_FLAG | — | — |
| 132 | QuickPurchaseOrderConsignedConsumptionFlag | CONSIGNED_CONSUMPTION_FLAG | — | — |
| 133 | QuickPurchaseOrderConsumeReqDemandFlag | CONSUME_REQ_DEMAND_FLAG | — | — |
| 134 | QuickPurchaseOrderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 135 | QuickPurchaseOrderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 136 | QuickPurchaseOrderContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 137 | QuickPurchaseOrderCpaReference | CPA_REFERENCE | — | — |
| 138 | QuickPurchaseOrderCreatedBy | CREATED_BY | — | — |
| 139 | QuickPurchaseOrderCreatedLanguage | CREATED_LANGUAGE | — | — |
| 140 | QuickPurchaseOrderCreationDate | CREATION_DATE | — | — |
| 141 | QuickPurchaseOrderCurrencyCode | CURRENCY_CODE | — | — |
| 142 | QuickPurchaseOrderCurrentVersionId | CURRENT_VERSION_ID | — | — |
| 143 | QuickPurchaseOrderDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 144 | QuickPurchaseOrderDocumentCreationMethod | DOCUMENT_CREATION_METHOD | — | — |
| 145 | QuickPurchaseOrderDocumentStatus | DOCUMENT_STATUS | — | — |
| 146 | QuickPurchaseOrderEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 147 | QuickPurchaseOrderEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 148 | QuickPurchaseOrderEmailAddress | EMAIL_ADDRESS | — | — |
| 149 | QuickPurchaseOrderEnabledFlag | ENABLED_FLAG | — | — |
| 150 | QuickPurchaseOrderEncumbranceRequiredFlag | ENCUMBRANCE_REQUIRED_FLAG | — | — |
| 151 | QuickPurchaseOrderEndDate | END_DATE | — | — |
| 152 | QuickPurchaseOrderFax | FAX | — | — |
| 153 | QuickPurchaseOrderFirmDate | FIRM_DATE | — | — |
| 154 | QuickPurchaseOrderFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 155 | QuickPurchaseOrderFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 156 | QuickPurchaseOrderFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 157 | QuickPurchaseOrderFromHeaderId | FROM_HEADER_ID | — | — |
| 158 | QuickPurchaseOrderFromTypeLookupCode | FROM_TYPE_LOOKUP_CODE | — | — |
| 159 | QuickPurchaseOrderFrozenFlag | FROZEN_FLAG | — | — |
| 160 | QuickPurchaseOrderGenerateOrdersAutomatic | GENERATE_ORDERS_AUTOMATIC | — | — |
| 161 | QuickPurchaseOrderGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 162 | QuickPurchaseOrderGroupRequisitionLines | GROUP_REQUISITION_LINES | — | — |
| 163 | QuickPurchaseOrderGroupRequisitions | GROUP_REQUISITIONS | — | — |
| 164 | QuickPurchaseOrderInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 165 | QuickPurchaseOrderJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 166 | QuickPurchaseOrderJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 167 | QuickPurchaseOrderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 168 | QuickPurchaseOrderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 169 | QuickPurchaseOrderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 170 | QuickPurchaseOrderLastUpdatedProgram | LAST_UPDATED_PROGRAM | — | — |
| 171 | QuickPurchaseOrderMinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 172 | QuickPurchaseOrderNoteToAuthorizer | NOTE_TO_AUTHORIZER | — | — |
| 173 | QuickPurchaseOrderNoteToReceiver | NOTE_TO_RECEIVER | — | — |
| 174 | QuickPurchaseOrderNoteToVendor | NOTE_TO_VENDOR | — | — |
| 175 | QuickPurchaseOrderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 176 | QuickPurchaseOrderPayOnCode | PAY_ON_CODE | — | — |
| 177 | QuickPurchaseOrderPcardId | PCARD_ID | — | — |
| 178 | QuickPurchaseOrderPendingSignatureFlag | PENDING_SIGNATURE_FLAG | — | — |
| 179 | QuickPurchaseOrderPoHeaderId | PO_HEADER_ID | — | — |
| 180 | QuickPurchaseOrderPrcBuId | PRC_BU_ID | — | — |
| 181 | QuickPurchaseOrderPriceUpdateTolerance | PRICE_UPDATE_TOLERANCE | — | — |
| 182 | QuickPurchaseOrderProgramAppName | PROGRAM_APP_NAME | — | — |
| 183 | QuickPurchaseOrderProgramName | PROGRAM_NAME | — | — |
| 184 | QuickPurchaseOrderRate | RATE | — | — |
| 185 | QuickPurchaseOrderRateDate | RATE_DATE | — | — |
| 186 | QuickPurchaseOrderRateType | RATE_TYPE | — | — |
| 187 | QuickPurchaseOrderReferenceNum | REFERENCE_NUM | — | — |
| 188 | QuickPurchaseOrderReleaseMethod | RELEASE_METHOD | — | — |
| 189 | QuickPurchaseOrderReqBuId | REQ_BU_ID | — | — |
| 190 | QuickPurchaseOrderRequestId | REQUEST_ID | — | — |
| 191 | QuickPurchaseOrderRetroPriceApplyUpdatesFlag | RETRO_PRICE_APPLY_UPDATES_FLAG | — | — |
| 192 | QuickPurchaseOrderRetroPriceCommUpdatesFlag | RETRO_PRICE_COMM_UPDATES_FLAG | — | — |
| 193 | QuickPurchaseOrderReviewAutogeneratedReleases | REVIEW_AUTOGENERATED_RELEASES | — | — |
| 194 | QuickPurchaseOrderRevisedDate | REVISED_DATE | — | — |
| 195 | QuickPurchaseOrderRevisionNum | REVISION_NUM | — | — |
| 196 | QuickPurchaseOrderSegment1 | SEGMENT1 | — | — |
| 197 | QuickPurchaseOrderSegment2 | SEGMENT2 | — | — |
| 198 | QuickPurchaseOrderSegment3 | SEGMENT3 | — | — |
| 199 | QuickPurchaseOrderSegment4 | SEGMENT4 | — | — |
| 200 | QuickPurchaseOrderSegment5 | SEGMENT5 | — | — |
| 201 | QuickPurchaseOrderShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 202 | QuickPurchaseOrderShippingControl | SHIPPING_CONTROL | — | — |
| 203 | QuickPurchaseOrderStartDate | START_DATE | — | — |
| 204 | QuickPurchaseOrderStyleId | STYLE_ID | — | — |
| 205 | QuickPurchaseOrderSubmitApprovalAutomatic | SUBMIT_APPROVAL_AUTOMATIC | — | — |
| 206 | QuickPurchaseOrderSubmitDate | SUBMIT_DATE | — | — |
| 207 | QuickPurchaseOrderSummaryFlag | SUMMARY_FLAG | — | — |
| 208 | QuickPurchaseOrderSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | — |
| 209 | QuickPurchaseOrderTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 210 | QuickPurchaseOrderTaxDocumentSubtype | TAX_DOCUMENT_SUBTYPE | — | — |
| 211 | QuickPurchaseOrderTermsId | TERMS_ID | — | — |
| 212 | QuickPurchaseOrderTypeLookupCode | TYPE_LOOKUP_CODE | — | — |
| 213 | QuickPurchaseOrderUpdateSourcingRulesFlag | UPDATE_SOURCING_RULES_FLAG | — | — |
| 214 | QuickPurchaseOrderUseNeedByDate | USE_NEED_BY_DATE | — | — |
| 215 | QuickPurchaseOrderUseShipTo | USE_SHIP_TO | — | — |
| 216 | QuickPurchaseOrderVendorContactId | VENDOR_CONTACT_ID | — | — |
| 217 | QuickPurchaseOrderVendorId | VENDOR_ID | — | — |
| 218 | QuickPurchaseOrderVendorOrderNum | VENDOR_ORDER_NUM | — | — |
| 219 | QuickPurchaseOrderVendorSiteId | VENDOR_SITE_ID | — | — |
| 220 | QuickPurchaseOrderXmlChangeSendDate | XML_CHANGE_SEND_DATE | — | — |
| 221 | QuickPurchaseOrderXmlFlag | XML_FLAG | — | — |
| 222 | QuickPurchaseOrderXmlSendDate | XML_SEND_DATE | — | — |

### [[zx_wht_tax_classification_v|ZX_WHT_TAX_CLASSIFICATION_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WithholdingTaxGrpExpCreatedBy | CREATED_BY | — | — |
| 2 | WithholdingTaxGrpExpCreationDate | CREATION_DATE | — | — |
| 3 | WithholdingTaxGrpExpDescription | DESCRIPTION | — | — |
| 4 | WithholdingTaxGrpExpGroupId | GROUP_ID | — | — |
| 5 | WithholdingTaxGrpExpInactiveDate | INACTIVE_DATE | — | — |
| 6 | WithholdingTaxGrpExpLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | WithholdingTaxGrpExpLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | WithholdingTaxGrpExpLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | WithholdingTaxGrpExpName | NAME | — | — |
| 10 | WithholdingTaxGrpExpObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | WithholdingTaxGrpExpRptCreatedBy | CREATED_BY | — | — |
| 12 | WithholdingTaxGrpExpRptCreationDate | CREATION_DATE | — | — |
| 13 | WithholdingTaxGrpExpRptDescription | DESCRIPTION | — | — |
| 14 | WithholdingTaxGrpExpRptGroupId | GROUP_ID | — | — |
| 15 | WithholdingTaxGrpExpRptInactiveDate | INACTIVE_DATE | — | — |
| 16 | WithholdingTaxGrpExpRptLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | WithholdingTaxGrpExpRptLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | WithholdingTaxGrpExpRptLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | WithholdingTaxGrpExpRptName | NAME | — | — |
| 20 | WithholdingTaxGrpExpRptObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | WithholdingTaxGrpInvCreatedBy | CREATED_BY | — | — |
| 22 | WithholdingTaxGrpInvCreationDate | CREATION_DATE | — | — |
| 23 | WithholdingTaxGrpInvDescription | DESCRIPTION | — | — |
| 24 | WithholdingTaxGrpInvGroupId | GROUP_ID | — | — |
| 25 | WithholdingTaxGrpInvInactiveDate | INACTIVE_DATE | — | — |
| 26 | WithholdingTaxGrpInvLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 27 | WithholdingTaxGrpInvLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 28 | WithholdingTaxGrpInvLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 29 | WithholdingTaxGrpInvName | NAME | — | — |
| 30 | WithholdingTaxGrpInvObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
