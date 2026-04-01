---
id: DOC-AP-PVO-InvoiceHeaderPVO
doc_type: system-doc
title: "InvoiceHeaderPVO — PVO Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ap
  - data-dictionary
  - pvo
  - bicc
aliases:
  - InvoiceHeaderPVO
  - invoiceheaderpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvoiceHeaderPVO

## 📌 Visão Geral

Extrai os cabeçalhos de faturas de fornecedores, incluindo dados do fornecedor, moeda, valor total, lote, condições de pagamento, status de aprovação e histórico. Permite análise completa de contas a pagar, aging de fornecedores, controle de fluxo de caixa e auditoria de faturas.

**Caminho:** `FscmTopModelAM.FinApInvTransactionsAM.InvoiceHeaderPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 231 | 18 | 1 | 96 | 42% |

---

## 🔗 Tabelas Relacionadas

- [[ap_batches_all|AP_BATCHES_ALL]] — 2 atributos (2 BICC)
- [[ap_distribution_sets_all|AP_DISTRIBUTION_SETS_ALL]] — 2 atributos (1 BICC)
- [[ap_invoices_all|AP_INVOICES_ALL]] — 160 atributos (1 PKs, 72 BICC)
- [[ap_inv_aprvl_hist_all|AP_INV_APRVL_HIST_ALL]] — 6 atributos
- [[ap_payment_schedules_all|AP_PAYMENT_SCHEDULES_ALL]] — 5 atributos
- [[fnd_attached_documents|FND_ATTACHED_DOCUMENTS]] — 2 atributos
- [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]] — 2 atributos (1 BICC)
- [[fnd_doc_sequence_categories|FND_DOC_SEQUENCE_CATEGORIES]] — 4 atributos (2 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 1 atributos
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 2 atributos (1 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 2 atributos
- [[hz_parties|HZ_PARTIES]] — 3 atributos (2 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 3 atributos (2 BICC)
- [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]] — 2 atributos
- [[iby_payment_codes_vl|IBY_PAYMENT_CODES_VL]] — 6 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 20 atributos (7 BICC)
- [[po_headers_all|PO_HEADERS_ALL]] — 3 atributos (2 BICC)
- [[zx_registrations|ZX_REGISTRATIONS]] — 6 atributos (4 BICC)

---

## ⚙️ Atributos

### [[ap_batches_all|AP_BATCHES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceBatchBatchId | BATCH_ID | — | ✅ |
| 2 | InvoiceBatchBatchName | BATCH_NAME | — | ✅ |

### [[ap_distribution_sets_all|AP_DISTRIBUTION_SETS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistributionSetDistributionSetId | DISTRIBUTION_SET_ID | — | — |
| 2 | DistributionSetOrgId | ORG_ID | — | ✅ |

### [[ap_invoices_all|AP_INVOICES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvHdrCrInvInvoiceId | INVOICE_ID | — | — |
| 2 | InvHdrCrInvInvoiceNum | INVOICE_NUM | — | ✅ |
| 3 | InvHdrTaxRelInvInvoiceId | INVOICE_ID | — | — |
| 4 | InvHdrTaxRelInvInvoiceNum | INVOICE_NUM | — | ✅ |
| 5 | InvoiceHdrTransactionDeadline | TRANSACTION_DEADLINE | — | ✅ |
| 6 | InvoiceHeaderAcctsPayCodeCombinationId | ACCTS_PAY_CODE_COMBINATION_ID | — | — |
| 7 | InvoiceHeaderAmountApplicableToDiscount | AMOUNT_APPLICABLE_TO_DISCOUNT | — | ✅ |
| 8 | InvoiceHeaderAmountPaid | AMOUNT_PAID | — | ✅ |
| 9 | InvoiceHeaderAmtDueCcardCompany | AMT_DUE_CCARD_COMPANY | — | — |
| 10 | InvoiceHeaderAmtDueEmployee | AMT_DUE_EMPLOYEE | — | — |
| 11 | InvoiceHeaderApplicationId | APPLICATION_ID | — | — |
| 12 | InvoiceHeaderApprovalDescription | APPROVAL_DESCRIPTION | — | ✅ |
| 13 | InvoiceHeaderApprovalIteration | APPROVAL_ITERATION | — | ✅ |
| 14 | InvoiceHeaderApprovalReadyFlag | APPROVAL_READY_FLAG | — | — |
| 15 | InvoiceHeaderApprovalStatus | APPROVAL_STATUS | — | ✅ |
| 16 | InvoiceHeaderApprovedAmount | APPROVED_AMOUNT | — | — |
| 17 | InvoiceHeaderAwardId | AWARD_ID | — | — |
| 18 | InvoiceHeaderAwtFlag | AWT_FLAG | — | — |
| 19 | InvoiceHeaderAwtGroupId | AWT_GROUP_ID | — | — |
| 20 | InvoiceHeaderBankChargeBearer | BANK_CHARGE_BEARER | — | — |
| 21 | InvoiceHeaderBaseAmount | BASE_AMOUNT | — | ✅ |
| 22 | InvoiceHeaderBatchId | BATCH_ID | — | — |
| 23 | InvoiceHeaderBudgetDate | BUDGET_DATE | — | ✅ |
| 24 | InvoiceHeaderCancelledAmount | CANCELLED_AMOUNT | — | ✅ |
| 25 | InvoiceHeaderCancelledBy | CANCELLED_BY | — | ✅ |
| 26 | InvoiceHeaderCancelledDate | CANCELLED_DATE | — | ✅ |
| 27 | InvoiceHeaderCheckVatAmountPaid | CHECK_VAT_AMOUNT_PAID | — | — |
| 28 | InvoiceHeaderControlAmount | CONTROL_AMOUNT | — | ✅ |
| 29 | InvoiceHeaderCorrectionPeriod | CORRECTION_PERIOD | — | ✅ |
| 30 | InvoiceHeaderCorrectionYear | CORRECTION_YEAR | — | ✅ |
| 31 | InvoiceHeaderCreatedBy | CREATED_BY | — | ✅ |
| 32 | InvoiceHeaderCreationDate | CREATION_DATE | — | ✅ |
| 33 | InvoiceHeaderCreditedInvoiceId | CREDITED_INVOICE_ID | — | — |
| 34 | InvoiceHeaderCustRegistrationCode | CUST_REGISTRATION_CODE | — | — |
| 35 | InvoiceHeaderCustRegistrationNumber | CUST_REGISTRATION_NUMBER | — | — |
| 36 | InvoiceHeaderDeliveryChannelCode | DELIVERY_CHANNEL_CODE | — | — |
| 37 | InvoiceHeaderDescription | DESCRIPTION | — | ✅ |
| 38 | InvoiceHeaderDiscIsInvLessTaxFlag | DISC_IS_INV_LESS_TAX_FLAG | — | — |
| 39 | InvoiceHeaderDiscountAmountTaken | DISCOUNT_AMOUNT_TAKEN | — | ✅ |
| 40 | InvoiceHeaderDistributionSetId | DISTRIBUTION_SET_ID | — | — |
| 41 | InvoiceHeaderDocCategoryCode | DOC_CATEGORY_CODE | — | ✅ |
| 42 | InvoiceHeaderDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 43 | InvoiceHeaderDocSequenceValue | DOC_SEQUENCE_VALUE | — | ✅ |
| 44 | InvoiceHeaderDocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 45 | InvoiceHeaderEarliestSettlementDate | EARLIEST_SETTLEMENT_DATE | — | ✅ |
| 46 | InvoiceHeaderEmployeeAddressCode | EMPLOYEE_ADDRESS_CODE | — | — |
| 47 | InvoiceHeaderExchangeDate | EXCHANGE_DATE | — | ✅ |
| 48 | InvoiceHeaderExchangeRate | EXCHANGE_RATE | — | ✅ |
| 49 | InvoiceHeaderExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 50 | InvoiceHeaderExcludeFreightFromDiscount | EXCLUDE_FREIGHT_FROM_DISCOUNT | — | ✅ |
| 51 | InvoiceHeaderExclusivePaymentFlag | EXCLUSIVE_PAYMENT_FLAG | — | ✅ |
| 52 | InvoiceHeaderExpenditureItemDate | EXPENDITURE_ITEM_DATE | — | — |
| 53 | InvoiceHeaderExpenditureOrganizationId | EXPENDITURE_ORGANIZATION_ID | — | — |
| 54 | InvoiceHeaderExpenditureType | EXPENDITURE_TYPE | — | — |
| 55 | InvoiceHeaderExternalBankAccountId | EXTERNAL_BANK_ACCOUNT_ID | — | — |
| 56 | InvoiceHeaderFiscalDocAccessKey | FISCAL_DOC_ACCESS_KEY | — | — |
| 57 | InvoiceHeaderForceRevalidationFlag | FORCE_REVALIDATION_FLAG | — | — |
| 58 | InvoiceHeaderFreightAmount | FREIGHT_AMOUNT | — | ✅ |
| 59 | InvoiceHeaderFundsStatus | FUNDS_STATUS | — | ✅ |
| 60 | InvoiceHeaderGlDate | GL_DATE | — | ✅ |
| 61 | InvoiceHeaderGoodsReceivedDate | GOODS_RECEIVED_DATE | — | ✅ |
| 62 | InvoiceHeaderHistoricalFlag | HISTORICAL_FLAG | — | — |
| 63 | InvoiceHeaderImportDocumentDate | IMPORT_DOCUMENT_DATE | — | ✅ |
| 64 | InvoiceHeaderImportDocumentNumber | IMPORT_DOCUMENT_NUMBER | — | — |
| 65 | InvoiceHeaderIntercompanyFlag | INTERCOMPANY_FLAG | — | ✅ |
| 66 | InvoiceHeaderInternalContactEmail | INTERNAL_CONTACT_EMAIL | — | — |
| 67 | InvoiceHeaderInvoiceAmount | INVOICE_AMOUNT | — | ✅ |
| 68 | InvoiceHeaderInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 69 | InvoiceHeaderInvoiceDate | INVOICE_DATE | — | ✅ |
| 70 | InvoiceHeaderInvoiceNum | INVOICE_NUM | — | ✅ |
| 71 | InvoiceHeaderInvoiceReceivedDate | INVOICE_RECEIVED_DATE | — | ✅ |
| 72 | InvoiceHeaderInvoiceTypeLookupCode | INVOICE_TYPE_LOOKUP_CODE | — | ✅ |
| 73 | InvoiceHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 74 | InvoiceHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 75 | InvoiceHeaderLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 76 | InvoiceHeaderLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 77 | InvoiceHeaderMrcBaseAmount | MRC_BASE_AMOUNT | — | — |
| 78 | InvoiceHeaderMrcExchangeDate | MRC_EXCHANGE_DATE | — | — |
| 79 | InvoiceHeaderMrcExchangeRate | MRC_EXCHANGE_RATE | — | — |
| 80 | InvoiceHeaderMrcExchangeRateType | MRC_EXCHANGE_RATE_TYPE | — | — |
| 81 | InvoiceHeaderMrcPostingStatus | MRC_POSTING_STATUS | — | — |
| 82 | InvoiceHeaderNetOfRetainageFlag | NET_OF_RETAINAGE_FLAG | — | ✅ |
| 83 | InvoiceHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 84 | InvoiceHeaderOrgId | ORG_ID | — | — |
| 85 | InvoiceHeaderPaDefaultDistCcid | PA_DEFAULT_DIST_CCID | — | — |
| 86 | InvoiceHeaderPaQuantity | PA_QUANTITY | — | — |
| 87 | InvoiceHeaderPaidOnBehalfEmployeeId | PAID_ON_BEHALF_EMPLOYEE_ID | — | — |
| 88 | InvoiceHeaderPartyId | PARTY_ID | — | — |
| 89 | InvoiceHeaderPartySiteId | PARTY_SITE_ID | — | — |
| 90 | InvoiceHeaderPayCurrInvoiceAmount | PAY_CURR_INVOICE_AMOUNT | — | — |
| 91 | InvoiceHeaderPayGroupLookupCode | PAY_GROUP_LOOKUP_CODE | — | ✅ |
| 92 | InvoiceHeaderPayProcTrxnTypeCode | PAY_PROC_TRXN_TYPE_CODE | — | — |
| 93 | InvoiceHeaderPaymentAmountTotal | PAYMENT_AMOUNT_TOTAL | — | ✅ |
| 94 | InvoiceHeaderPaymentCrossRate | PAYMENT_CROSS_RATE | — | ✅ |
| 95 | InvoiceHeaderPaymentCrossRateDate | PAYMENT_CROSS_RATE_DATE | — | ✅ |
| 96 | InvoiceHeaderPaymentCrossRateType | PAYMENT_CROSS_RATE_TYPE | — | ✅ |
| 97 | InvoiceHeaderPaymentCurrencyCode | PAYMENT_CURRENCY_CODE | — | ✅ |
| 98 | InvoiceHeaderPaymentFunction | PAYMENT_FUNCTION | — | — |
| 99 | InvoiceHeaderPaymentMethodCode | PAYMENT_METHOD_CODE | — | — |
| 100 | InvoiceHeaderPaymentMethodLookupCode | PAYMENT_METHOD_LOOKUP_CODE | — | — |
| 101 | InvoiceHeaderPaymentReasonCode | PAYMENT_REASON_CODE | — | — |
| 102 | InvoiceHeaderPaymentReasonComments | PAYMENT_REASON_COMMENTS | — | ✅ |
| 103 | InvoiceHeaderPaymentStatusFlag | PAYMENT_STATUS_FLAG | — | ✅ |
| 104 | InvoiceHeaderPoHeaderId | PO_HEADER_ID | — | — |
| 105 | InvoiceHeaderPortOfEntryCode | PORT_OF_ENTRY_CODE | — | ✅ |
| 106 | InvoiceHeaderPostingStatus | POSTING_STATUS | — | ✅ |
| 107 | InvoiceHeaderPreWithholdingAmount | PRE_WITHHOLDING_AMOUNT | — | — |
| 108 | InvoiceHeaderProductTable | PRODUCT_TABLE | — | — |
| 109 | InvoiceHeaderProjectId | PROJECT_ID | — | — |
| 110 | InvoiceHeaderQuickCredit | QUICK_CREDIT | — | — |
| 111 | InvoiceHeaderQuickPoHeaderId | QUICK_PO_HEADER_ID | — | — |
| 112 | InvoiceHeaderRecurringPaymentId | RECURRING_PAYMENT_ID | — | — |
| 113 | InvoiceHeaderReference1 | REFERENCE_1 | — | — |
| 114 | InvoiceHeaderReference2 | REFERENCE_2 | — | — |
| 115 | InvoiceHeaderReferenceKey1 | REFERENCE_KEY1 | — | — |
| 116 | InvoiceHeaderReferenceKey2 | REFERENCE_KEY2 | — | — |
| 117 | InvoiceHeaderReferenceKey3 | REFERENCE_KEY3 | — | — |
| 118 | InvoiceHeaderReferenceKey4 | REFERENCE_KEY4 | — | — |
| 119 | InvoiceHeaderReferenceKey5 | REFERENCE_KEY5 | — | — |
| 120 | InvoiceHeaderReleaseAmountNetOfTax | RELEASE_AMOUNT_NET_OF_TAX | — | ✅ |
| 121 | InvoiceHeaderRemittanceMessage1 | REMITTANCE_MESSAGE1 | — | — |
| 122 | InvoiceHeaderRemittanceMessage2 | REMITTANCE_MESSAGE2 | — | — |
| 123 | InvoiceHeaderRemittanceMessage3 | REMITTANCE_MESSAGE3 | — | — |
| 124 | InvoiceHeaderRequesterId | REQUESTER_ID | — | — |
| 125 | InvoiceHeaderRoutingAttribute1 | ROUTING_ATTRIBUTE1 | — | ✅ |
| 126 | InvoiceHeaderRoutingAttribute2 | ROUTING_ATTRIBUTE2 | — | ✅ |
| 127 | InvoiceHeaderRoutingAttribute3 | ROUTING_ATTRIBUTE3 | — | ✅ |
| 128 | InvoiceHeaderRoutingAttribute4 | ROUTING_ATTRIBUTE4 | — | ✅ |
| 129 | InvoiceHeaderRoutingAttribute5 | ROUTING_ATTRIBUTE5 | — | — |
| 130 | InvoiceHeaderRoutingStatusLookupCode | ROUTING_STATUS_LOOKUP_CODE | — | ✅ |
| 131 | InvoiceHeaderSelfAssessedTaxAmount | SELF_ASSESSED_TAX_AMOUNT | — | ✅ |
| 132 | InvoiceHeaderSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 133 | InvoiceHeaderSettlementPriority | SETTLEMENT_PRIORITY | — | ✅ |
| 134 | InvoiceHeaderSource | SOURCE | — | — |
| 135 | InvoiceHeaderSupplierTaxExchangeRate | SUPPLIER_TAX_EXCHANGE_RATE | — | ✅ |
| 136 | InvoiceHeaderSupplierTaxInvoiceDate | SUPPLIER_TAX_INVOICE_DATE | — | ✅ |
| 137 | InvoiceHeaderSupplierTaxInvoiceNumber | SUPPLIER_TAX_INVOICE_NUMBER | — | ✅ |
| 138 | InvoiceHeaderTaskId | TASK_ID | — | — |
| 139 | InvoiceHeaderTaxInvoiceInternalSeq | TAX_INVOICE_INTERNAL_SEQ | — | ✅ |
| 140 | InvoiceHeaderTaxInvoiceRecordingDate | TAX_INVOICE_RECORDING_DATE | — | ✅ |
| 141 | InvoiceHeaderTaxRelatedInvoiceId | TAX_RELATED_INVOICE_ID | — | — |
| 142 | InvoiceHeaderTaxationCountry | TAXATION_COUNTRY | — | ✅ |
| 143 | InvoiceHeaderTempCancelledAmount | TEMP_CANCELLED_AMOUNT | — | — |
| 144 | InvoiceHeaderTermsDate | TERMS_DATE | — | ✅ |
| 145 | InvoiceHeaderTermsId | TERMS_ID | — | — |
| 146 | InvoiceHeaderTotalTaxAmount | TOTAL_TAX_AMOUNT | — | ✅ |
| 147 | InvoiceHeaderTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 148 | InvoiceHeaderUniqueRemittanceIdentifier | UNIQUE_REMITTANCE_IDENTIFIER | — | ✅ |
| 149 | InvoiceHeaderUriCheckDigit | URI_CHECK_DIGIT | — | — |
| 150 | InvoiceHeaderUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 151 | InvoiceHeaderUssglTransactionCode | USSGL_TRANSACTION_CODE | — | — |
| 152 | InvoiceHeaderUssglTrxCodeContext | USSGL_TRX_CODE_CONTEXT | — | — |
| 153 | InvoiceHeaderValidatedTaxAmount | VALIDATED_TAX_AMOUNT | — | — |
| 154 | InvoiceHeaderValidationRequestId | VALIDATION_REQUEST_ID | — | — |
| 155 | InvoiceHeaderVendorContactId | VENDOR_CONTACT_ID | — | — |
| 156 | InvoiceHeaderVendorId | VENDOR_ID | — | — |
| 157 | InvoiceHeaderVendorSiteId | VENDOR_SITE_ID | — | — |
| 158 | InvoiceHeaderVoucherNum | VOUCHER_NUM | — | ✅ |
| 159 | InvoiceHeaderWfapprovalStatus | WFAPPROVAL_STATUS | — | ✅ |
| 160 | InvoiceId | INVOICE_ID | 🔑 | ✅ |

### [[ap_inv_aprvl_hist_all|AP_INV_APRVL_HIST_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvAprvlHistAllAmountApproved | AMOUNT_APPROVED | — | — |
| 2 | InvAprvlHistAllApprovalHistoryId | APPROVAL_HISTORY_ID | — | — |
| 3 | InvAprvlHistAllApproverId | APPROVER_ID | — | — |
| 4 | InvAprvlHistAllCreationDate | CREATION_DATE | — | — |
| 5 | InvAprvlHistAllHistoryType | HISTORY_TYPE | — | — |
| 6 | InvAprvlHistAllResponse | RESPONSE | — | — |

### [[ap_payment_schedules_all|AP_PAYMENT_SCHEDULES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceHeaderRelationshipId | RELATIONSHIP_ID | — | — |
| 2 | InvoiceHeaderRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 3 | InvoiceHeaderRemitToAddressName | REMIT_TO_ADDRESS_NAME | — | — |
| 4 | InvoiceHeaderRemitToSupplierId | REMIT_TO_SUPPLIER_ID | — | — |
| 5 | InvoiceHeaderRemitToSupplierName | REMIT_TO_SUPPLIER_NAME | — | — |

### [[fnd_attached_documents|FND_ATTACHED_DOCUMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AttachedDocumentsAttachedDocumentId | ATTACHED_DOCUMENT_ID | — | — |
| 2 | AttachedDocumentsEnterpriseId | ENTERPRISE_ID | — | — |

### [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocSequenceDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 2 | DocSequenceName | NAME | — | ✅ |

### [[fnd_doc_sequence_categories|FND_DOC_SEQUENCE_CATEGORIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocSeqCatApplicationId | APPLICATION_ID | — | — |
| 2 | DocSeqCatCode | CODE | — | — |
| 3 | DocSeqCatDescription | DESCRIPTION | — | ✅ |
| 4 | DocSeqCatName | NAME | — | ✅ |

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitBusinessUnitId | BU_ID | — | — |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceConversionTypeConversionType | CONVERSION_TYPE | — | — |
| 2 | InvoiceConversionTypeUserConversionType | USER_CONVERSION_TYPE | — | ✅ |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 2 | LedgersLedgerId | LEDGER_ID | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | PartyPartyId | PARTY_ID | — | — |
| 3 | PartyPartyName | PARTY_NAME | — | ✅ |

### [[hz_party_sites|HZ_PARTY_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartySiteLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | PartySitePartySiteId | PARTY_SITE_ID | — | — |
| 3 | PartySitePartySiteName | PARTY_SITE_NAME | — | ✅ |

### [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvExtBnkAcctExtBankAccountId | EXT_BANK_ACCOUNT_ID | — | — |
| 2 | InvExtBnkAcctLastUpdateDate | LAST_UPDATE_DATE | — | — |

### [[iby_payment_codes_vl|IBY_PAYMENT_CODES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayDelcodeLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 2 | PayDelcodePaymentCode | PAYMENT_CODE | — | — |
| 3 | PayDelcodePaymentCodeType | PAYMENT_CODE_TYPE | — | — |
| 4 | PayReacodeLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 5 | PayReacodePaymentCode | PAYMENT_CODE | — | — |
| 6 | PayReacodePaymentCodeType | PAYMENT_CODE_TYPE | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AprvlPersonNameDisplayName1 | DISPLAY_NAME | — | — |
| 2 | AprvlPersonNameEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | AprvlPersonNameEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | AprvlPersonNamePersonNameId | PERSON_NAME_ID | — | — |
| 5 | PersonCancelledByDisplayName | DISPLAY_NAME | — | ✅ |
| 6 | PersonCancelledByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | PersonCancelledByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 8 | PersonCancelledByPersonNameId | PERSON_NAME_ID | — | — |
| 9 | PersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 10 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 11 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 12 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 13 | PersonNameDisplayName | DISPLAY_NAME | — | ✅ |
| 14 | PersonNameEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 15 | PersonNameEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 16 | PersonNamePersonNameId | PERSON_NAME_ID | — | — |
| 17 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 18 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 19 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 20 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[po_headers_all|PO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchaseOrderClosedDate | CLOSED_DATE | — | ✅ |
| 2 | PurchaseOrderPoHeaderId | PO_HEADER_ID | — | — |
| 3 | PurchaseOrderSegment1 | SEGMENT1 | — | ✅ |

### [[zx_registrations|ZX_REGISTRATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FirstPartyTaxRegistrationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | FirstPartyTaxRegistrationRegistrationId | REGISTRATION_ID | — | — |
| 3 | FirstPartyTaxRegistrationRegistrationNumber | REGISTRATION_NUMBER | — | ✅ |
| 4 | ThirdPartyTaxRegistrationLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 5 | ThirdPartyTaxRegistrationRegistrationId1 | REGISTRATION_ID | — | — |
| 6 | ThirdPartyTaxRegistrationRegistrationNumber1 | REGISTRATION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
