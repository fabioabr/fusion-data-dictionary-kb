---
id: DOC-OTHER-PVO-FiscalDocumentLinesP
doc_type: system-doc
title: "FiscalDocumentLinesP — PVO Cross-Module"
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
  - FiscalDocumentLinesP
  - fiscaldocumentlinesp
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FiscalDocumentLinesP

## 📌 Visão Geral

View Object para extração BICC de dados de Fiscal Document Lines P. Acessa as tabelas: AP_INVOICES_ALL, AP_PAYMENT_SCHEDULES_ALL, CMF_FD_IN_CONVERT_CFOPS_V (+22).

**Caminho:** `FscmTopModelAM.FiscalDocumentAM.FiscalDocumentLinesP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 1307 | 25 | 2 | 131 | 10% |

---

## 🔗 Tabelas Relacionadas

- [[ap_invoices_all|AP_INVOICES_ALL]] — 163 atributos
- [[ap_payment_schedules_all|AP_PAYMENT_SCHEDULES_ALL]] — 5 atributos
- [[cmf_fd_in_convert_cfops_v|CMF_FD_IN_CONVERT_CFOPS_V]] — 2 atributos (2 BICC)
- [[cmf_fd_loc_info_persist_otbi_v|CMF_FD_LOC_INFO_PERSIST_OTBI_V]] — 79 atributos (12 BICC)
- [[cmf_fd_out_origin_cfops_v|CMF_FD_OUT_ORIGIN_CFOPS_V]] — 2 atributos (2 BICC)
- [[cmf_fiscal_doc_headers|CMF_FISCAL_DOC_HEADERS]] — 61 atributos (21 BICC)
- [[cmf_fiscal_doc_inv_org_v|CMF_FISCAL_DOC_INV_ORG_V]] — 5 atributos
- [[cmf_fiscal_doc_lines_vl|CMF_FISCAL_DOC_LINES_VL]] — 48 atributos (2 PKs, 16 BICC)
- [[cmf_fiscal_proc_options|CMF_FISCAL_PROC_OPTIONS]] — 56 atributos
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 21 atributos
- [[gl_ledgers|GL_LEDGERS]] — 87 atributos
- [[inv_cons_advice_headers|INV_CONS_ADVICE_HEADERS]] — 25 atributos
- [[inv_units_of_measure_vl|INV_UNITS_OF_MEASURE_VL]] — 44 atributos (1 BICC)
- [[jg_fscl_hdrs_atrb_ext_all|JG_FSCL_HDRS_ATRB_EXT_ALL]] — 56 atributos (37 BICC)
- [[jg_fscl_hdr_dtls_atrb_ext_all|JG_FSCL_HDR_DTLS_ATRB_EXT_ALL]] — 20 atributos
- [[jg_fscl_lines_atrb_ext_all|JG_FSCL_LINES_ATRB_EXT_ALL]] — 23 atributos (5 BICC)
- [[jg_fscl_ln_dtls_atrb_ext_all|JG_FSCL_LN_DTLS_ATRB_EXT_ALL]] — 20 atributos (1 BICC)
- [[jg_fscl_tax_lines_all|JG_FSCL_TAX_LINES_ALL]] — 72 atributos (22 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 232 atributos (8 BICC)
- [[per_users|PER_USERS]] — 176 atributos
- [[rcv_shipment_headers|RCV_SHIPMENT_HEADERS]] — 83 atributos
- [[zx_fc_intended_use_v|ZX_FC_INTENDED_USE_V]] — 6 atributos (1 BICC)
- [[zx_fc_product_categories_v|ZX_FC_PRODUCT_CATEGORIES_V]] — 8 atributos (1 BICC)
- [[zx_fc_product_fiscal_v|ZX_FC_PRODUCT_FISCAL_V]] — 8 atributos (1 BICC)
- [[zx_fc_user_defined_v|ZX_FC_USER_DEFINED_V]] — 5 atributos (1 BICC)

---

## ⚙️ Atributos

### [[ap_invoices_all|AP_INVOICES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApInvoicesAllAcctsPayCodeCombinationId | ACCTS_PAY_CODE_COMBINATION_ID | — | — |
| 2 | ApInvoicesAllAmountApplicableToDiscount | AMOUNT_APPLICABLE_TO_DISCOUNT | — | — |
| 3 | ApInvoicesAllAmountPaid | AMOUNT_PAID | — | — |
| 4 | ApInvoicesAllAmtDueCcardCompany | AMT_DUE_CCARD_COMPANY | — | — |
| 5 | ApInvoicesAllAmtDueEmployee | AMT_DUE_EMPLOYEE | — | — |
| 6 | ApInvoicesAllApplicationId | APPLICATION_ID | — | — |
| 7 | ApInvoicesAllApprovalDescription | APPROVAL_DESCRIPTION | — | — |
| 8 | ApInvoicesAllApprovalIteration | APPROVAL_ITERATION | — | — |
| 9 | ApInvoicesAllApprovalReadyFlag | APPROVAL_READY_FLAG | — | — |
| 10 | ApInvoicesAllApprovalStatus | APPROVAL_STATUS | — | — |
| 11 | ApInvoicesAllApprovedAmount | APPROVED_AMOUNT | — | — |
| 12 | ApInvoicesAllAwardId | AWARD_ID | — | — |
| 13 | ApInvoicesAllAwtFlag | AWT_FLAG | — | — |
| 14 | ApInvoicesAllAwtGroupId | AWT_GROUP_ID | — | — |
| 15 | ApInvoicesAllBankChargeBearer | BANK_CHARGE_BEARER | — | — |
| 16 | ApInvoicesAllBaseAmount | BASE_AMOUNT | — | — |
| 17 | ApInvoicesAllBatchId | BATCH_ID | — | — |
| 18 | ApInvoicesAllBudgetDate | BUDGET_DATE | — | — |
| 19 | ApInvoicesAllCancelledAmount | CANCELLED_AMOUNT | — | — |
| 20 | ApInvoicesAllCancelledBy | CANCELLED_BY | — | — |
| 21 | ApInvoicesAllCancelledDate | CANCELLED_DATE | — | — |
| 22 | ApInvoicesAllCheckVatAmountPaid | CHECK_VAT_AMOUNT_PAID | — | — |
| 23 | ApInvoicesAllControlAmount | CONTROL_AMOUNT | — | — |
| 24 | ApInvoicesAllCorrectionPeriod | CORRECTION_PERIOD | — | — |
| 25 | ApInvoicesAllCorrectionYear | CORRECTION_YEAR | — | — |
| 26 | ApInvoicesAllCreatedBy | CREATED_BY | — | — |
| 27 | ApInvoicesAllCreationDate | CREATION_DATE | — | — |
| 28 | ApInvoicesAllCreditedInvoiceId | CREDITED_INVOICE_ID | — | — |
| 29 | ApInvoicesAllCustRegistrationCode | CUST_REGISTRATION_CODE | — | — |
| 30 | ApInvoicesAllCustRegistrationNumber | CUST_REGISTRATION_NUMBER | — | — |
| 31 | ApInvoicesAllDataSetId | DATA_SET_ID | — | — |
| 32 | ApInvoicesAllDeliveryChannelCode | DELIVERY_CHANNEL_CODE | — | — |
| 33 | ApInvoicesAllDescription | DESCRIPTION | — | — |
| 34 | ApInvoicesAllDiscIsInvLessTaxFlag | DISC_IS_INV_LESS_TAX_FLAG | — | — |
| 35 | ApInvoicesAllDiscountAmountTaken | DISCOUNT_AMOUNT_TAKEN | — | — |
| 36 | ApInvoicesAllDistributionSetId | DISTRIBUTION_SET_ID | — | — |
| 37 | ApInvoicesAllDocCategoryCode | DOC_CATEGORY_CODE | — | — |
| 38 | ApInvoicesAllDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 39 | ApInvoicesAllDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 40 | ApInvoicesAllDocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 41 | ApInvoicesAllEarliestSettlementDate | EARLIEST_SETTLEMENT_DATE | — | — |
| 42 | ApInvoicesAllEmployeeAddressCode | EMPLOYEE_ADDRESS_CODE | — | — |
| 43 | ApInvoicesAllExchangeDate | EXCHANGE_DATE | — | — |
| 44 | ApInvoicesAllExchangeRate | EXCHANGE_RATE | — | — |
| 45 | ApInvoicesAllExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 46 | ApInvoicesAllExcludeFreightFromDiscount | EXCLUDE_FREIGHT_FROM_DISCOUNT | — | — |
| 47 | ApInvoicesAllExclusivePaymentFlag | EXCLUSIVE_PAYMENT_FLAG | — | — |
| 48 | ApInvoicesAllExpenditureItemDate | EXPENDITURE_ITEM_DATE | — | — |
| 49 | ApInvoicesAllExpenditureOrganizationId | EXPENDITURE_ORGANIZATION_ID | — | — |
| 50 | ApInvoicesAllExpenditureType | EXPENDITURE_TYPE | — | — |
| 51 | ApInvoicesAllExternalBankAccountId | EXTERNAL_BANK_ACCOUNT_ID | — | — |
| 52 | ApInvoicesAllFirstPartyRegistrationId | FIRST_PARTY_REGISTRATION_ID | — | — |
| 53 | ApInvoicesAllFiscalDocAccessKey | FISCAL_DOC_ACCESS_KEY | — | — |
| 54 | ApInvoicesAllForceRevalidationFlag | FORCE_REVALIDATION_FLAG | — | — |
| 55 | ApInvoicesAllFreightAmount | FREIGHT_AMOUNT | — | — |
| 56 | ApInvoicesAllFundsStatus | FUNDS_STATUS | — | — |
| 57 | ApInvoicesAllGlDate | GL_DATE | — | — |
| 58 | ApInvoicesAllGoodsReceivedDate | GOODS_RECEIVED_DATE | — | — |
| 59 | ApInvoicesAllHistoricalFlag | HISTORICAL_FLAG | — | — |
| 60 | ApInvoicesAllImageDocumentNum | IMAGE_DOCUMENT_NUM | — | — |
| 61 | ApInvoicesAllImportDocumentDate | IMPORT_DOCUMENT_DATE | — | — |
| 62 | ApInvoicesAllImportDocumentNumber | IMPORT_DOCUMENT_NUMBER | — | — |
| 63 | ApInvoicesAllIntercompanyFlag | INTERCOMPANY_FLAG | — | — |
| 64 | ApInvoicesAllInternalContactEmail | INTERNAL_CONTACT_EMAIL | — | — |
| 65 | ApInvoicesAllInvoiceAmount | INVOICE_AMOUNT | — | — |
| 66 | ApInvoicesAllInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 67 | ApInvoicesAllInvoiceDate | INVOICE_DATE | — | — |
| 68 | ApInvoicesAllInvoiceId | INVOICE_ID | — | — |
| 69 | ApInvoicesAllInvoiceNum | INVOICE_NUM | — | — |
| 70 | ApInvoicesAllInvoiceReceivedDate | INVOICE_RECEIVED_DATE | — | — |
| 71 | ApInvoicesAllInvoiceTypeLookupCode | INVOICE_TYPE_LOOKUP_CODE | — | — |
| 72 | ApInvoicesAllJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 73 | ApInvoicesAllJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 74 | ApInvoicesAllLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 75 | ApInvoicesAllLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 76 | ApInvoicesAllLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 77 | ApInvoicesAllLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 78 | ApInvoicesAllLockTime | LOCK_TIME | — | — |
| 79 | ApInvoicesAllLockedBy | LOCKED_BY | — | — |
| 80 | ApInvoicesAllMergeRequestId | MERGE_REQUEST_ID | — | — |
| 81 | ApInvoicesAllMrcBaseAmount | MRC_BASE_AMOUNT | — | — |
| 82 | ApInvoicesAllMrcExchangeDate | MRC_EXCHANGE_DATE | — | — |
| 83 | ApInvoicesAllMrcExchangeRate | MRC_EXCHANGE_RATE | — | — |
| 84 | ApInvoicesAllMrcExchangeRateType | MRC_EXCHANGE_RATE_TYPE | — | — |
| 85 | ApInvoicesAllMrcPostingStatus | MRC_POSTING_STATUS | — | — |
| 86 | ApInvoicesAllNetOfRetainageFlag | NET_OF_RETAINAGE_FLAG | — | — |
| 87 | ApInvoicesAllObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 88 | ApInvoicesAllOrgId | ORG_ID | — | — |
| 89 | ApInvoicesAllPaDefaultDistCcid | PA_DEFAULT_DIST_CCID | — | — |
| 90 | ApInvoicesAllPaQuantity | PA_QUANTITY | — | — |
| 91 | ApInvoicesAllPaidOnBehalfEmployeeId | PAID_ON_BEHALF_EMPLOYEE_ID | — | — |
| 92 | ApInvoicesAllPartyId | PARTY_ID | — | — |
| 93 | ApInvoicesAllPartySiteId | PARTY_SITE_ID | — | — |
| 94 | ApInvoicesAllPayCurrInvoiceAmount | PAY_CURR_INVOICE_AMOUNT | — | — |
| 95 | ApInvoicesAllPayGroupLookupCode | PAY_GROUP_LOOKUP_CODE | — | — |
| 96 | ApInvoicesAllPayProcTrxnTypeCode | PAY_PROC_TRXN_TYPE_CODE | — | — |
| 97 | ApInvoicesAllPaymentAmountTotal | PAYMENT_AMOUNT_TOTAL | — | — |
| 98 | ApInvoicesAllPaymentCrossRate | PAYMENT_CROSS_RATE | — | — |
| 99 | ApInvoicesAllPaymentCrossRateDate | PAYMENT_CROSS_RATE_DATE | — | — |
| 100 | ApInvoicesAllPaymentCrossRateType | PAYMENT_CROSS_RATE_TYPE | — | — |
| 101 | ApInvoicesAllPaymentCurrencyCode | PAYMENT_CURRENCY_CODE | — | — |
| 102 | ApInvoicesAllPaymentFunction | PAYMENT_FUNCTION | — | — |
| 103 | ApInvoicesAllPaymentMethodCode | PAYMENT_METHOD_CODE | — | — |
| 104 | ApInvoicesAllPaymentMethodLookupCode | PAYMENT_METHOD_LOOKUP_CODE | — | — |
| 105 | ApInvoicesAllPaymentReasonCode | PAYMENT_REASON_CODE | — | — |
| 106 | ApInvoicesAllPaymentReasonComments | PAYMENT_REASON_COMMENTS | — | — |
| 107 | ApInvoicesAllPaymentStatusFlag | PAYMENT_STATUS_FLAG | — | — |
| 108 | ApInvoicesAllPoHeaderId | PO_HEADER_ID | — | — |
| 109 | ApInvoicesAllPoMatchedFlag | PO_MATCHED_FLAG | — | — |
| 110 | ApInvoicesAllPortOfEntryCode | PORT_OF_ENTRY_CODE | — | — |
| 111 | ApInvoicesAllPostingStatus | POSTING_STATUS | — | — |
| 112 | ApInvoicesAllPreWithholdingAmount | PRE_WITHHOLDING_AMOUNT | — | — |
| 113 | ApInvoicesAllProductTable | PRODUCT_TABLE | — | — |
| 114 | ApInvoicesAllProjectId | PROJECT_ID | — | — |
| 115 | ApInvoicesAllQuickCredit | QUICK_CREDIT | — | — |
| 116 | ApInvoicesAllQuickPoHeaderId | QUICK_PO_HEADER_ID | — | — |
| 117 | ApInvoicesAllRecurringPaymentId | RECURRING_PAYMENT_ID | — | — |
| 118 | ApInvoicesAllReference1 | REFERENCE_1 | — | — |
| 119 | ApInvoicesAllReference2 | REFERENCE_2 | — | — |
| 120 | ApInvoicesAllReferenceKey1 | REFERENCE_KEY1 | — | — |
| 121 | ApInvoicesAllReferenceKey2 | REFERENCE_KEY2 | — | — |
| 122 | ApInvoicesAllReferenceKey3 | REFERENCE_KEY3 | — | — |
| 123 | ApInvoicesAllReferenceKey4 | REFERENCE_KEY4 | — | — |
| 124 | ApInvoicesAllReferenceKey5 | REFERENCE_KEY5 | — | — |
| 125 | ApInvoicesAllReleaseAmountNetOfTax | RELEASE_AMOUNT_NET_OF_TAX | — | — |
| 126 | ApInvoicesAllRemittanceMessage1 | REMITTANCE_MESSAGE1 | — | — |
| 127 | ApInvoicesAllRemittanceMessage2 | REMITTANCE_MESSAGE2 | — | — |
| 128 | ApInvoicesAllRemittanceMessage3 | REMITTANCE_MESSAGE3 | — | — |
| 129 | ApInvoicesAllRequestId | REQUEST_ID | — | — |
| 130 | ApInvoicesAllRequesterId | REQUESTER_ID | — | — |
| 131 | ApInvoicesAllRoutingStatusLookupCode | ROUTING_STATUS_LOOKUP_CODE | — | — |
| 132 | ApInvoicesAllSelfAssessedTaxAmount | SELF_ASSESSED_TAX_AMOUNT | — | — |
| 133 | ApInvoicesAllSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 134 | ApInvoicesAllSettlementPriority | SETTLEMENT_PRIORITY | — | — |
| 135 | ApInvoicesAllSource | SOURCE | — | — |
| 136 | ApInvoicesAllSupplierTaxExchangeRate | SUPPLIER_TAX_EXCHANGE_RATE | — | — |
| 137 | ApInvoicesAllSupplierTaxInvoiceDate | SUPPLIER_TAX_INVOICE_DATE | — | — |
| 138 | ApInvoicesAllSupplierTaxInvoiceNumber | SUPPLIER_TAX_INVOICE_NUMBER | — | — |
| 139 | ApInvoicesAllTaskId | TASK_ID | — | — |
| 140 | ApInvoicesAllTaxInvoiceInternalSeq | TAX_INVOICE_INTERNAL_SEQ | — | — |
| 141 | ApInvoicesAllTaxInvoiceRecordingDate | TAX_INVOICE_RECORDING_DATE | — | — |
| 142 | ApInvoicesAllTaxRelatedInvoiceId | TAX_RELATED_INVOICE_ID | — | — |
| 143 | ApInvoicesAllTaxationCountry | TAXATION_COUNTRY | — | — |
| 144 | ApInvoicesAllTempCancelledAmount | TEMP_CANCELLED_AMOUNT | — | — |
| 145 | ApInvoicesAllTermsDate | TERMS_DATE | — | — |
| 146 | ApInvoicesAllTermsId | TERMS_ID | — | — |
| 147 | ApInvoicesAllThirdPartyRegistrationId | THIRD_PARTY_REGISTRATION_ID | — | — |
| 148 | ApInvoicesAllTotalTaxAmount | TOTAL_TAX_AMOUNT | — | — |
| 149 | ApInvoicesAllTransactionDeadline | TRANSACTION_DEADLINE | — | — |
| 150 | ApInvoicesAllTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 151 | ApInvoicesAllUniqueRemittanceIdentifier | UNIQUE_REMITTANCE_IDENTIFIER | — | — |
| 152 | ApInvoicesAllUriCheckDigit | URI_CHECK_DIGIT | — | — |
| 153 | ApInvoicesAllUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 154 | ApInvoicesAllUssglTransactionCode | USSGL_TRANSACTION_CODE | — | — |
| 155 | ApInvoicesAllUssglTrxCodeContext | USSGL_TRX_CODE_CONTEXT | — | — |
| 156 | ApInvoicesAllValidatedTaxAmount | VALIDATED_TAX_AMOUNT | — | — |
| 157 | ApInvoicesAllValidationRequestId | VALIDATION_REQUEST_ID | — | — |
| 158 | ApInvoicesAllValidationWorkerId | VALIDATION_WORKER_ID | — | — |
| 159 | ApInvoicesAllVendorContactId | VENDOR_CONTACT_ID | — | — |
| 160 | ApInvoicesAllVendorId | VENDOR_ID | — | — |
| 161 | ApInvoicesAllVendorSiteId | VENDOR_SITE_ID | — | — |
| 162 | ApInvoicesAllVoucherNum | VOUCHER_NUM | — | — |
| 163 | ApInvoicesAllWfapprovalStatus | WFAPPROVAL_STATUS | — | — |

### [[ap_payment_schedules_all|AP_PAYMENT_SCHEDULES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApInvoicesAllRelationshipId | RELATIONSHIP_ID | — | — |
| 2 | ApInvoicesAllRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 3 | ApInvoicesAllRemitToAddressName | REMIT_TO_ADDRESS_NAME | — | — |
| 4 | ApInvoicesAllRemitToSupplierId | REMIT_TO_SUPPLIER_ID | — | — |
| 5 | ApInvoicesAllRemitToSupplierName | REMIT_TO_SUPPLIER_NAME | — | — |

### [[cmf_fd_in_convert_cfops_v|CMF_FD_IN_CONVERT_CFOPS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocInBoundCFOPPEOClassificationCode | CLASSIFICATION_CODE | — | ✅ |
| 2 | FiscalDocInBoundCFOPPEOClassificationName | CLASSIFICATION_NAME | — | ✅ |

### [[cmf_fd_loc_info_persist_otbi_v|CMF_FD_LOC_INFO_PERSIST_OTBI_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocLocInfoPersistPEODocumentHeaderId | DOCUMENT_HEADER_ID | — | — |
| 2 | FiscalDocLocInfoPersistPEODocumentNumber | DOCUMENT_NUMBER | — | — |
| 3 | FiscalDocLocInfoPersistPEOFiscalProcOptionsId | FISCAL_PROC_OPTIONS_ID | — | — |
| 4 | FiscalDocLocInfoPersistPEOIssuerCustomerFormTaxNum | ISSUER_CUSTOMER_FORM_TAX_NUM | — | — |
| 5 | FiscalDocLocInfoPersistPEOIssuerCustomerLocationId | ISSUER_CUSTOMER_LOCATION_ID | — | — |
| 6 | FiscalDocLocInfoPersistPEOIssuerCustomerPartyId | ISSUER_CUSTOMER_PARTY_ID | — | — |
| 7 | FiscalDocLocInfoPersistPEOIssuerCustomerPartySiteId | ISSUER_CUSTOMER_PARTY_SITE_ID | — | — |
| 8 | FiscalDocLocInfoPersistPEOIssuerCustomerTaxId | ISSUER_CUSTOMER_TAX_ID | — | — |
| 9 | FiscalDocLocInfoPersistPEOIssuerCustomerTaxpayerId | ISSUER_CUSTOMER_TAXPAYER_ID | — | ✅ |
| 10 | FiscalDocLocInfoPersistPEOIssuerLeFormTaxNumber | ISSUER_LE_FORM_TAX_NUMBER | — | — |
| 11 | FiscalDocLocInfoPersistPEOIssuerLeId | ISSUER_LE_ID | — | — |
| 12 | FiscalDocLocInfoPersistPEOIssuerLeLocationId | ISSUER_LE_LOCATION_ID | — | — |
| 13 | FiscalDocLocInfoPersistPEOIssuerLeSiteId | ISSUER_LE_SITE_ID | — | — |
| 14 | FiscalDocLocInfoPersistPEOIssuerLeTaxId | ISSUER_LE_TAX_ID | — | — |
| 15 | FiscalDocLocInfoPersistPEOIssuerLeTaxpayerId | ISSUER_LE_TAXPAYER_ID | — | ✅ |
| 16 | FiscalDocLocInfoPersistPEOIssuerSupplierFormTaxNum | ISSUER_SUPPLIER_FORM_TAX_NUM | — | — |
| 17 | FiscalDocLocInfoPersistPEOIssuerSupplierLocationId | ISSUER_SUPPLIER_LOCATION_ID | — | — |
| 18 | FiscalDocLocInfoPersistPEOIssuerSupplierPartyId | ISSUER_SUPPLIER_PARTY_ID | — | — |
| 19 | FiscalDocLocInfoPersistPEOIssuerSupplierPartySiteId | ISSUER_SUPPLIER_PARTY_SITE_ID | — | — |
| 20 | FiscalDocLocInfoPersistPEOIssuerSupplierTaxId | ISSUER_SUPPLIER_TAX_ID | — | — |
| 21 | FiscalDocLocInfoPersistPEOIssuerSupplierTaxpayerId | ISSUER_SUPPLIER_TAXPAYER_ID | — | ✅ |
| 22 | FiscalDocLocInfoPersistPEOIssuerType | ISSUER_TYPE | — | — |
| 23 | FiscalDocLocInfoPersistPEOReceiverCustPartySiteId | RECEIVER_CUST_PARTY_SITE_ID | — | — |
| 24 | FiscalDocLocInfoPersistPEOReceiverCustomerFormTaxNum | RECEIVER_CUSTOMER_FORM_TAX_NUM | — | — |
| 25 | FiscalDocLocInfoPersistPEOReceiverCustomerLocationId | RECEIVER_CUSTOMER_LOCATION_ID | — | — |
| 26 | FiscalDocLocInfoPersistPEOReceiverCustomerPartyId | RECEIVER_CUSTOMER_PARTY_ID | — | — |
| 27 | FiscalDocLocInfoPersistPEOReceiverCustomerTaxId | RECEIVER_CUSTOMER_TAX_ID | — | — |
| 28 | FiscalDocLocInfoPersistPEOReceiverCustomerTaxpayerId | RECEIVER_CUSTOMER_TAXPAYER_ID | — | ✅ |
| 29 | FiscalDocLocInfoPersistPEOReceiverLeFormTaxNumber | RECEIVER_LE_FORM_TAX_NUMBER | — | — |
| 30 | FiscalDocLocInfoPersistPEOReceiverLeLocationId | RECEIVER_LE_LOCATION_ID | — | — |
| 31 | FiscalDocLocInfoPersistPEOReceiverLePartyId | RECEIVER_LE_PARTY_ID | — | — |
| 32 | FiscalDocLocInfoPersistPEOReceiverLePartySiteId | RECEIVER_LE_PARTY_SITE_ID | — | — |
| 33 | FiscalDocLocInfoPersistPEOReceiverLeTaxId | RECEIVER_LE_TAX_ID | — | — |
| 34 | FiscalDocLocInfoPersistPEOReceiverLeTaxpayerId | RECEIVER_LE_TAXPAYER_ID | — | ✅ |
| 35 | FiscalDocLocInfoPersistPEOReceiverSuppPartySiteId | RECEIVER_SUPP_PARTY_SITE_ID | — | — |
| 36 | FiscalDocLocInfoPersistPEOReceiverSupplierFormTaxNum | RECEIVER_SUPPLIER_FORM_TAX_NUM | — | — |
| 37 | FiscalDocLocInfoPersistPEOReceiverSupplierLocationId | RECEIVER_SUPPLIER_LOCATION_ID | — | — |
| 38 | FiscalDocLocInfoPersistPEOReceiverSupplierPartyId | RECEIVER_SUPPLIER_PARTY_ID | — | — |
| 39 | FiscalDocLocInfoPersistPEOReceiverSupplierTaxId | RECEIVER_SUPPLIER_TAX_ID | — | — |
| 40 | FiscalDocLocInfoPersistPEOReceiverSupplierTaxpayerId | RECEIVER_SUPPLIER_TAXPAYER_ID | — | ✅ |
| 41 | FiscalDocLocInfoPersistPEOReceiverType | RECEIVER_TYPE | — | — |
| 42 | FiscalDocLocInfoPersistPEOShipfromCustPartySiteId | SHIPFROM_CUST_PARTY_SITE_ID | — | — |
| 43 | FiscalDocLocInfoPersistPEOShipfromCustomerFormTaxNum | SHIPFROM_CUSTOMER_FORM_TAX_NUM | — | — |
| 44 | FiscalDocLocInfoPersistPEOShipfromCustomerLocationId | SHIPFROM_CUSTOMER_LOCATION_ID | — | — |
| 45 | FiscalDocLocInfoPersistPEOShipfromCustomerPartyId | SHIPFROM_CUSTOMER_PARTY_ID | — | — |
| 46 | FiscalDocLocInfoPersistPEOShipfromCustomerTaxId | SHIPFROM_CUSTOMER_TAX_ID | — | — |
| 47 | FiscalDocLocInfoPersistPEOShipfromCustomerTaxpayerId | SHIPFROM_CUSTOMER_TAXPAYER_ID | — | ✅ |
| 48 | FiscalDocLocInfoPersistPEOShipfromLeFormTaxNumber | SHIPFROM_LE_FORM_TAX_NUMBER | — | — |
| 49 | FiscalDocLocInfoPersistPEOShipfromLeLocationId | SHIPFROM_LE_LOCATION_ID | — | — |
| 50 | FiscalDocLocInfoPersistPEOShipfromLePartyId | SHIPFROM_LE_PARTY_ID | — | — |
| 51 | FiscalDocLocInfoPersistPEOShipfromLePartySiteId | SHIPFROM_LE_PARTY_SITE_ID | — | — |
| 52 | FiscalDocLocInfoPersistPEOShipfromLeTaxId | SHIPFROM_LE_TAX_ID | — | — |
| 53 | FiscalDocLocInfoPersistPEOShipfromLeTaxpayerId | SHIPFROM_LE_TAXPAYER_ID | — | ✅ |
| 54 | FiscalDocLocInfoPersistPEOShipfromSuppPartySiteId | SHIPFROM_SUPP_PARTY_SITE_ID | — | — |
| 55 | FiscalDocLocInfoPersistPEOShipfromSupplierFormTaxNum | SHIPFROM_SUPPLIER_FORM_TAX_NUM | — | — |
| 56 | FiscalDocLocInfoPersistPEOShipfromSupplierLocationId | SHIPFROM_SUPPLIER_LOCATION_ID | — | — |
| 57 | FiscalDocLocInfoPersistPEOShipfromSupplierPartyId | SHIPFROM_SUPPLIER_PARTY_ID | — | — |
| 58 | FiscalDocLocInfoPersistPEOShipfromSupplierTaxId | SHIPFROM_SUPPLIER_TAX_ID | — | — |
| 59 | FiscalDocLocInfoPersistPEOShipfromSupplierTaxpayerId | SHIPFROM_SUPPLIER_TAXPAYER_ID | — | ✅ |
| 60 | FiscalDocLocInfoPersistPEOShipfromType | SHIPFROM_TYPE | — | — |
| 61 | FiscalDocLocInfoPersistPEOShiptoCustPartySiteId | SHIPTO_CUST_PARTY_SITE_ID | — | — |
| 62 | FiscalDocLocInfoPersistPEOShiptoCustomerFormTaxNum | SHIPTO_CUSTOMER_FORM_TAX_NUM | — | — |
| 63 | FiscalDocLocInfoPersistPEOShiptoCustomerLocationId | SHIPTO_CUSTOMER_LOCATION_ID | — | — |
| 64 | FiscalDocLocInfoPersistPEOShiptoCustomerPartyId | SHIPTO_CUSTOMER_PARTY_ID | — | — |
| 65 | FiscalDocLocInfoPersistPEOShiptoCustomerTaxId | SHIPTO_CUSTOMER_TAX_ID | — | — |
| 66 | FiscalDocLocInfoPersistPEOShiptoCustomerTaxpayerId | SHIPTO_CUSTOMER_TAXPAYER_ID | — | ✅ |
| 67 | FiscalDocLocInfoPersistPEOShiptoLeFormTaxNumber | SHIPTO_LE_FORM_TAX_NUMBER | — | — |
| 68 | FiscalDocLocInfoPersistPEOShiptoLeLocationId | SHIPTO_LE_LOCATION_ID | — | — |
| 69 | FiscalDocLocInfoPersistPEOShiptoLePartyId | SHIPTO_LE_PARTY_ID | — | — |
| 70 | FiscalDocLocInfoPersistPEOShiptoLePartySiteId | SHIPTO_LE_PARTY_SITE_ID | — | — |
| 71 | FiscalDocLocInfoPersistPEOShiptoLeTaxId | SHIPTO_LE_TAX_ID | — | — |
| 72 | FiscalDocLocInfoPersistPEOShiptoLeTaxpayerId | SHIPTO_LE_TAXPAYER_ID | — | ✅ |
| 73 | FiscalDocLocInfoPersistPEOShiptoSuppPartySiteId | SHIPTO_SUPP_PARTY_SITE_ID | — | — |
| 74 | FiscalDocLocInfoPersistPEOShiptoSupplierFormTaxNum | SHIPTO_SUPPLIER_FORM_TAX_NUM | — | — |
| 75 | FiscalDocLocInfoPersistPEOShiptoSupplierLocationId | SHIPTO_SUPPLIER_LOCATION_ID | — | — |
| 76 | FiscalDocLocInfoPersistPEOShiptoSupplierPartyId | SHIPTO_SUPPLIER_PARTY_ID | — | — |
| 77 | FiscalDocLocInfoPersistPEOShiptoSupplierTaxId | SHIPTO_SUPPLIER_TAX_ID | — | — |
| 78 | FiscalDocLocInfoPersistPEOShiptoSupplierTaxpayerId | SHIPTO_SUPPLIER_TAXPAYER_ID | — | ✅ |
| 79 | FiscalDocLocInfoPersistPEOShiptoType | SHIPTO_TYPE | — | — |

### [[cmf_fd_out_origin_cfops_v|CMF_FD_OUT_ORIGIN_CFOPS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocOutBoundCFOPPEOClassificationCode1 | CLASSIFICATION_CODE | — | ✅ |
| 2 | FiscalDocOutBoundCFOPPEOClassificationName1 | CLASSIFICATION_NAME | — | ✅ |

### [[cmf_fiscal_doc_headers|CMF_FISCAL_DOC_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocHeadersPEOAccessKeyNumber | ACCESS_KEY_NUMBER | — | ✅ |
| 2 | FiscalDocHeadersPEOAcknowledgedDate | ACKNOWLEDGED_DATE | — | ✅ |
| 3 | FiscalDocHeadersPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | FiscalDocHeadersPEOBillToBusinessUnitId | BILL_TO_BUSINESS_UNIT_ID | — | — |
| 5 | FiscalDocHeadersPEOChargeAllocationStatus | CHARGE_ALLOCATION_STATUS | — | ✅ |
| 6 | FiscalDocHeadersPEOCmrInterfacedFlag | CMR_INTERFACED_FLAG | — | ✅ |
| 7 | FiscalDocHeadersPEOConversionRate | CONVERSION_RATE | — | — |
| 8 | FiscalDocHeadersPEOConverstionType | CONVERSTION_TYPE | — | — |
| 9 | FiscalDocHeadersPEOCountryCode | COUNTRY_CODE | — | ✅ |
| 10 | FiscalDocHeadersPEOCreatedBy | CREATED_BY | — | — |
| 11 | FiscalDocHeadersPEOCreationDate | CREATION_DATE | — | ✅ |
| 12 | FiscalDocHeadersPEOCurrency | CURRENCY | — | ✅ |
| 13 | FiscalDocHeadersPEODocumentHeaderId | DOCUMENT_HEADER_ID | — | ✅ |
| 14 | FiscalDocHeadersPEODocumentNumber | DOCUMENT_NUMBER | — | ✅ |
| 15 | FiscalDocHeadersPEODocumentStatus | DOCUMENT_STATUS | — | ✅ |
| 16 | FiscalDocHeadersPEODocumentType | DOCUMENT_TYPE | — | — |
| 17 | FiscalDocHeadersPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | — |
| 18 | FiscalDocHeadersPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 19 | FiscalDocHeadersPEOFiscalDocAssoctnsId | FISCAL_DOC_ASSOCTNS_ID | — | — |
| 20 | FiscalDocHeadersPEOFiscalProcOptionsId | FISCAL_PROC_OPTIONS_ID | — | — |
| 21 | FiscalDocHeadersPEOInterfacedFlag | INTERFACED_FLAG | — | — |
| 22 | FiscalDocHeadersPEOInvoiceInterfacedFlag | INVOICE_INTERFACED_FLAG | — | ✅ |
| 23 | FiscalDocHeadersPEOIssueDate | ISSUE_DATE | — | ✅ |
| 24 | FiscalDocHeadersPEOIssuerLocationId | ISSUER_LOCATION_ID | — | — |
| 25 | FiscalDocHeadersPEOIssuerPartyId | ISSUER_PARTY_ID | — | — |
| 26 | FiscalDocHeadersPEOIssuerPartySiteId | ISSUER_PARTY_SITE_ID | — | — |
| 27 | FiscalDocHeadersPEOIssuerTaxId | ISSUER_TAX_ID | — | — |
| 28 | FiscalDocHeadersPEOItemLineAmount | ITEM_LINE_AMOUNT | — | ✅ |
| 29 | FiscalDocHeadersPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 30 | FiscalDocHeadersPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 31 | FiscalDocHeadersPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | FiscalDocHeadersPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | FiscalDocHeadersPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 34 | FiscalDocHeadersPEOModel | MODEL | — | ✅ |
| 35 | FiscalDocHeadersPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 36 | FiscalDocHeadersPEOOperationType | OPERATION_TYPE | — | — |
| 37 | FiscalDocHeadersPEOParentDocumentHeaderId | PARENT_DOCUMENT_HEADER_ID | — | — |
| 38 | FiscalDocHeadersPEOReason | REASON | — | — |
| 39 | FiscalDocHeadersPEOReceiverLocationId | RECEIVER_LOCATION_ID | — | — |
| 40 | FiscalDocHeadersPEOReceiverPartyId | RECEIVER_PARTY_ID | — | — |
| 41 | FiscalDocHeadersPEOReceiverPartySiteId | RECEIVER_PARTY_SITE_ID | — | — |
| 42 | FiscalDocHeadersPEOReceiverTaxId | RECEIVER_TAX_ID | — | — |
| 43 | FiscalDocHeadersPEOReferencedStatus | REFERENCED_STATUS | — | ✅ |
| 44 | FiscalDocHeadersPEORequestId | REQUEST_ID | — | — |
| 45 | FiscalDocHeadersPEOSchedulesAllocatedFlag | SCHEDULES_ALLOCATED_FLAG | — | ✅ |
| 46 | FiscalDocHeadersPEOSeries | SERIES | — | ✅ |
| 47 | FiscalDocHeadersPEOShipfromLocationId | SHIPFROM_LOCATION_ID | — | — |
| 48 | FiscalDocHeadersPEOShipfromPartyId | SHIPFROM_PARTY_ID | — | — |
| 49 | FiscalDocHeadersPEOShipfromPartySiteId | SHIPFROM_PARTY_SITE_ID | — | — |
| 50 | FiscalDocHeadersPEOShipfromTaxId | SHIPFROM_TAX_ID | — | — |
| 51 | FiscalDocHeadersPEOShiptoLocationId | SHIPTO_LOCATION_ID | — | — |
| 52 | FiscalDocHeadersPEOShiptoPartyId | SHIPTO_PARTY_ID | — | — |
| 53 | FiscalDocHeadersPEOShiptoPartySiteId | SHIPTO_PARTY_SITE_ID | — | — |
| 54 | FiscalDocHeadersPEOShiptoTaxId | SHIPTO_TAX_ID | — | — |
| 55 | FiscalDocHeadersPEOSoldToLegalEntityId | SOLD_TO_LEGAL_ENTITY_ID | — | — |
| 56 | FiscalDocHeadersPEOSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 57 | FiscalDocHeadersPEOSourceRefDocHeaderId | SOURCE_REF_DOC_HEADER_ID | — | — |
| 58 | FiscalDocHeadersPEOSubseries | SUBSERIES | — | ✅ |
| 59 | FiscalDocHeadersPEOTaxCalculationStatus | TAX_CALCULATION_STATUS | — | ✅ |
| 60 | FiscalDocHeadersPEOTotalAmount | TOTAL_AMOUNT | — | ✅ |
| 61 | FiscalDocHeadersPEOValidationStatus | VALIDATION_STATUS | — | — |

### [[cmf_fiscal_doc_inv_org_v|CMF_FISCAL_DOC_INV_ORG_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocInvOrgPEODestInventoryOrgId | DEST_INVENTORY_ORG_ID | — | — |
| 2 | FiscalDocInvOrgPEOFiscalDocHeaderId | FISCAL_DOC_HEADER_ID | — | — |
| 3 | FiscalDocInvOrgPEOFiscalDocLineId | FISCAL_DOC_LINE_ID | — | — |
| 4 | FiscalDocInvOrgPEOSourceDocType | SOURCE_DOC_TYPE | — | — |
| 5 | FiscalDocInvOrgPEOSrcInventoryOrgId | SRC_INVENTORY_ORG_ID | — | — |

### [[cmf_fiscal_doc_lines_vl|CMF_FISCAL_DOC_LINES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocumentLineId | DOCUMENT_LINE_ID | 🔑 | ✅ |
| 2 | FiscalDocumentLinesPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 3 | FiscalDocumentLinesPEOChargesAmount | CHARGES_AMOUNT | — | — |
| 4 | FiscalDocumentLinesPEOCreatedBy | CREATED_BY | — | — |
| 5 | FiscalDocumentLinesPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | FiscalDocumentLinesPEODistCodeCombinationId | DIST_CODE_COMBINATION_ID | — | — |
| 7 | FiscalDocumentLinesPEODocumentHeaderId | DOCUMENT_HEADER_ID | — | — |
| 8 | FiscalDocumentLinesPEOEfdItemCode | EFD_ITEM_CODE | — | ✅ |
| 9 | FiscalDocumentLinesPEOEfdItemDescription | EFD_ITEM_DESCRIPTION | — | ✅ |
| 10 | FiscalDocumentLinesPEOEfdProdAddInfo | EFD_PROD_ADD_INFO | — | ✅ |
| 11 | FiscalDocumentLinesPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | — |
| 12 | FiscalDocumentLinesPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 13 | FiscalDocumentLinesPEOFciControlNumber | FCI_CONTROL_NUMBER | — | — |
| 14 | FiscalDocumentLinesPEOFdAmount | FD_AMOUNT | — | ✅ |
| 15 | FiscalDocumentLinesPEOFdConvertedCfop | FD_CONVERTED_CFOP | — | — |
| 16 | FiscalDocumentLinesPEOFdOriginalCfop | FD_ORIGINAL_CFOP | — | — |
| 17 | FiscalDocumentLinesPEOFdPrice | FD_PRICE | — | ✅ |
| 18 | FiscalDocumentLinesPEOFdQuantity | FD_QUANTITY | — | ✅ |
| 19 | FiscalDocumentLinesPEOFdUom | FD_UOM | — | — |
| 20 | FiscalDocumentLinesPEOFiscalClassification | FISCAL_CLASSIFICATION | — | — |
| 21 | FiscalDocumentLinesPEOFreightModal | FREIGHT_MODAL | — | — |
| 22 | FiscalDocumentLinesPEOIntendedUseId | INTENDED_USE_ID | — | — |
| 23 | FiscalDocumentLinesPEOItemDescription | ITEM_DESCRIPTION | — | — |
| 24 | FiscalDocumentLinesPEOItemId | ITEM_ID | — | — |
| 25 | FiscalDocumentLinesPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 26 | FiscalDocumentLinesPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 27 | FiscalDocumentLinesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | FiscalDocumentLinesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 29 | FiscalDocumentLinesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 30 | FiscalDocumentLinesPEOLineNumber | LINE_NUMBER | — | ✅ |
| 31 | FiscalDocumentLinesPEOLineStatus | LINE_STATUS | — | ✅ |
| 32 | FiscalDocumentLinesPEOLineType | LINE_TYPE | — | ✅ |
| 33 | FiscalDocumentLinesPEONonRecoverableTax | NON_RECOVERABLE_TAX | — | — |
| 34 | FiscalDocumentLinesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 35 | FiscalDocumentLinesPEOPhysicalReceiptDate | PHYSICAL_RECEIPT_DATE | — | ✅ |
| 36 | FiscalDocumentLinesPEOPhysicalReceiptQuantity | PHYSICAL_RECEIPT_QUANTITY | — | ✅ |
| 37 | FiscalDocumentLinesPEOPhysicalReceiptUom | PHYSICAL_RECEIPT_UOM | — | ✅ |
| 38 | FiscalDocumentLinesPEOProductCategory | PRODUCT_CATEGORY | — | — |
| 39 | FiscalDocumentLinesPEOProductFiscalClassifId | PRODUCT_FISCAL_CLASSIF_ID | — | — |
| 40 | FiscalDocumentLinesPEORecoverablesTax | RECOVERABLES_TAX | — | — |
| 41 | FiscalDocumentLinesPEORefDocumentHeaderId | REF_DOCUMENT_HEADER_ID | — | — |
| 42 | FiscalDocumentLinesPEORefDocumentLineId | REF_DOCUMENT_LINE_ID | 🔑 | — |
| 43 | FiscalDocumentLinesPEORefFdDocumentType | REF_FD_DOCUMENT_TYPE | — | — |
| 44 | FiscalDocumentLinesPEOReqBuId | REQ_BU_ID | — | — |
| 45 | FiscalDocumentLinesPEORequestId | REQUEST_ID | — | — |
| 46 | FiscalDocumentLinesPEOScheduleSrcDocType | SCHEDULE_SRC_DOC_TYPE | — | — |
| 47 | FiscalDocumentLinesPEOSourceDocBuId | SOURCE_DOC_BU_ID | — | — |
| 48 | FiscalDocumentLinesPEOSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | ✅ |

### [[cmf_fiscal_proc_options|CMF_FISCAL_PROC_OPTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalProcOptionsPEOAdditionalMatchRule | ADDITIONAL_MATCH_RULE | — | — |
| 2 | FiscalProcOptionsPEOChangeDocStatusFlag | CHANGE_DOC_STATUS_FLAG | — | — |
| 3 | FiscalProcOptionsPEOChargeAllocation1Flag | CHARGE_ALLOCATION_1_FLAG | — | — |
| 4 | FiscalProcOptionsPEOChargeAllocationFlag | CHARGE_ALLOCATION_FLAG | — | — |
| 5 | FiscalProcOptionsPEOChargesDistributionFlag | CHARGES_DISTRIBUTION_FLAG | — | — |
| 6 | FiscalProcOptionsPEOComplementaryFlag | COMPLEMENTARY_FLAG | — | — |
| 7 | FiscalProcOptionsPEOComplementaryLineType | COMPLEMENTARY_LINE_TYPE | — | — |
| 8 | FiscalProcOptionsPEOComplementaryTypeManualPr | COMPLEMENTARY_TYPE_MANUAL_PR | — | — |
| 9 | FiscalProcOptionsPEOCostDistribution | COST_DISTRIBUTION | — | — |
| 10 | FiscalProcOptionsPEOCountryCode | COUNTRY_CODE | — | — |
| 11 | FiscalProcOptionsPEOCreatedBy | CREATED_BY | — | — |
| 12 | FiscalProcOptionsPEOCreationDate | CREATION_DATE | — | — |
| 13 | FiscalProcOptionsPEODeleteAllowedFlag | DELETE_ALLOWED_FLAG | — | — |
| 14 | FiscalProcOptionsPEODocumentTypeCode | DOCUMENT_TYPE_CODE | — | — |
| 15 | FiscalProcOptionsPEOElectronicModel | ELECTRONIC_MODEL | — | — |
| 16 | FiscalProcOptionsPEOEndDate | END_DATE | — | — |
| 17 | FiscalProcOptionsPEOExcludedTaxesFromMiscChrge | EXCLUDED_TAXES_FROM_MISC_CHRGE | — | — |
| 18 | FiscalProcOptionsPEOFdCurrencyCode | FD_CURRENCY_CODE | — | — |
| 19 | FiscalProcOptionsPEOFdHeaderLineRelationship | FD_HEADER_LINE_RELATIONSHIP | — | — |
| 20 | FiscalProcOptionsPEOFdUsage | FD_USAGE | — | — |
| 21 | FiscalProcOptionsPEOFiscalAttributesFlag | FISCAL_ATTRIBUTES_FLAG | — | — |
| 22 | FiscalProcOptionsPEOFiscalProcOptionsId | FISCAL_PROC_OPTIONS_ID | — | — |
| 23 | FiscalProcOptionsPEOHoldMgmtFlag | HOLD_MGMT_FLAG | — | — |
| 24 | FiscalProcOptionsPEOIfaceApFlag | IFACE_AP_FLAG | — | — |
| 25 | FiscalProcOptionsPEOIfaceCstFlag | IFACE_CST_FLAG | — | — |
| 26 | FiscalProcOptionsPEOIfaceRcvFlag | IFACE_RCV_FLAG | — | — |
| 27 | FiscalProcOptionsPEOInformativeCharges | INFORMATIVE_CHARGES | — | — |
| 28 | FiscalProcOptionsPEOIssuerType | ISSUER_TYPE | — | — |
| 29 | FiscalProcOptionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 30 | FiscalProcOptionsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 31 | FiscalProcOptionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 32 | FiscalProcOptionsPEOLegalProcessesFlag | LEGAL_PROCESSES_FLAG | — | — |
| 33 | FiscalProcOptionsPEOLineSrcDocTypeCode | LINE_SRC_DOC_TYPE_CODE | — | — |
| 34 | FiscalProcOptionsPEOManualPrQttyEntryFlag | MANUAL_PR_QTTY_ENTRY_FLAG | — | — |
| 35 | FiscalProcOptionsPEOMatchRefPrepaymentFlag | MATCH_REF_PREPAYMENT_FLAG | — | — |
| 36 | FiscalProcOptionsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 37 | FiscalProcOptionsPEOOperationType | OPERATION_TYPE | — | — |
| 38 | FiscalProcOptionsPEOParentProcessOptId | PARENT_PROCESS_OPT_ID | — | — |
| 39 | FiscalProcOptionsPEOPayablesDocTypeCode | PAYABLES_DOC_TYPE_CODE | — | — |
| 40 | FiscalProcOptionsPEOPhysicalRecptByOrderFd | PHYSICAL_RECPT_BY_ORDER_FD | — | — |
| 41 | FiscalProcOptionsPEOProcessCode | PROCESS_CODE | — | — |
| 42 | FiscalProcOptionsPEOProcessOptionCode | PROCESS_OPTION_CODE | — | — |
| 43 | FiscalProcOptionsPEOReceiverType | RECEIVER_TYPE | — | — |
| 44 | FiscalProcOptionsPEOReferenceAllowedFlag | REFERENCE_ALLOWED_FLAG | — | — |
| 45 | FiscalProcOptionsPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 46 | FiscalProcOptionsPEOSeriesReq | SERIES_REQ | — | — |
| 47 | FiscalProcOptionsPEOShipFromType | SHIP_FROM_TYPE | — | — |
| 48 | FiscalProcOptionsPEOShipToType | SHIP_TO_TYPE | — | — |
| 49 | FiscalProcOptionsPEOSourceDocumentTypeCode | SOURCE_DOCUMENT_TYPE_CODE | — | — |
| 50 | FiscalProcOptionsPEOSrcDocCurrencyCode | SRC_DOC_CURRENCY_CODE | — | — |
| 51 | FiscalProcOptionsPEOStartDate | START_DATE | — | — |
| 52 | FiscalProcOptionsPEOSubSeriesReq | SUB_SERIES_REQ | — | — |
| 53 | FiscalProcOptionsPEOTaxCalculationFlag | TAX_CALCULATION_FLAG | — | — |
| 54 | FiscalProcOptionsPEOUpdateRefPhysicalReceipt | UPDATE_REF_PHYSICAL_RECEIPT | — | — |
| 55 | FiscalProcOptionsPEOValidateRefDocFlag | VALIDATE_REF_DOC_FLAG | — | — |
| 56 | FiscalProcOptionsPEOValidationFlag | VALIDATION_FLAG | — | — |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOBusinessUnitId | BU_ID | — | — |
| 2 | BusinessUnitPEOCreatedBy | CREATED_BY | — | — |
| 3 | BusinessUnitPEOCreationDate | CREATION_DATE | — | — |
| 4 | BusinessUnitPEODateFrom | DATE_FROM | — | — |
| 5 | BusinessUnitPEODateTo | DATE_TO | — | — |
| 6 | BusinessUnitPEODefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | — |
| 7 | BusinessUnitPEODefaultSetId | DEFAULT_SET_ID | — | — |
| 8 | BusinessUnitPEOEnabledForHrFlag | ENABLED_FOR_HR_FLAG | — | — |
| 9 | BusinessUnitPEOEnterpriseId | BUSINESS_GROUP_ID | — | — |
| 10 | BusinessUnitPEOFinancialsBusinessUnitId | FIN_BUSINESS_UNIT_ID | — | — |
| 11 | BusinessUnitPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 12 | BusinessUnitPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | BusinessUnitPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | BusinessUnitPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 15 | BusinessUnitPEOLocationId | LOCATION_ID | — | — |
| 16 | BusinessUnitPEOManagerId | MANAGER_ID | — | — |
| 17 | BusinessUnitPEOName | BU_NAME | — | — |
| 18 | BusinessUnitPEOPrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |
| 19 | BusinessUnitPEOProfitCenterFlag | PROFIT_CENTER_FLAG | — | — |
| 20 | BusinessUnitPEOShortCode | SHORT_CODE | — | — |
| 21 | BusinessUnitPEOStatus | STATUS | — | — |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgerPEOAccountedPeriodType | ACCOUNTED_PERIOD_TYPE | — | — |
| 2 | LedgerPEOAlcLedgerTypeCode | ALC_LEDGER_TYPE_CODE | — | — |
| 3 | LedgerPEOAllowIntercompanyPostFlag | ALLOW_INTERCOMPANY_POST_FLAG | — | — |
| 4 | LedgerPEOApDocSequencingOptionFlag | AP_DOC_SEQUENCING_OPTION_FLAG | — | — |
| 5 | LedgerPEOArDocSequencingOptionFlag | AR_DOC_SEQUENCING_OPTION_FLAG | — | — |
| 6 | LedgerPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 7 | LedgerPEOAutomateSecJrnlRevFlag | AUTOMATE_SEC_JRNL_REV_FLAG | — | — |
| 8 | LedgerPEOAutomaticallyCreatedFlag | AUTOMATICALLY_CREATED_FLAG | — | — |
| 9 | LedgerPEOAutorevAfterOpenPrdFlag | AUTOREV_AFTER_OPEN_PRD_FLAG | — | — |
| 10 | LedgerPEOBalSegColumnName | BAL_SEG_COLUMN_NAME | — | — |
| 11 | LedgerPEOBalSegValueOptionCode | BAL_SEG_VALUE_OPTION_CODE | — | — |
| 12 | LedgerPEOBalSegValueSetId | BAL_SEG_VALUE_SET_ID | — | — |
| 13 | LedgerPEOBudgetPeriodAvgRateType | BUDGET_PERIOD_AVG_RATE_TYPE | — | — |
| 14 | LedgerPEOBudgetPeriodEndRateType | BUDGET_PERIOD_END_RATE_TYPE | — | — |
| 15 | LedgerPEOChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 16 | LedgerPEOCompleteFlag | COMPLETE_FLAG | — | — |
| 17 | LedgerPEOCompletionStatusCode | COMPLETION_STATUS_CODE | — | — |
| 18 | LedgerPEOConfigurationId | CONFIGURATION_ID | — | — |
| 19 | LedgerPEOConsolidationLedgerFlag | CONSOLIDATION_LEDGER_FLAG | — | — |
| 20 | LedgerPEOCreateJeFlag | CREATE_JE_FLAG | — | — |
| 21 | LedgerPEOCreatedBy | CREATED_BY | — | — |
| 22 | LedgerPEOCreationDate | CREATION_DATE | — | — |
| 23 | LedgerPEOCriteriaSetId | CRITERIA_SET_ID | — | — |
| 24 | LedgerPEOCumTransCodeCombinationId | CUM_TRANS_CODE_COMBINATION_ID | — | — |
| 25 | LedgerPEOCurrencyCode | CURRENCY_CODE | — | — |
| 26 | LedgerPEODailyTranslationRateType | DAILY_TRANSLATION_RATE_TYPE | — | — |
| 27 | LedgerPEODescription | DESCRIPTION | — | — |
| 28 | LedgerPEOEnableAutomaticTaxFlag | ENABLE_AUTOMATIC_TAX_FLAG | — | — |
| 29 | LedgerPEOEnableAverageBalancesFlag | ENABLE_AVERAGE_BALANCES_FLAG | — | — |
| 30 | LedgerPEOEnableBudgetaryControlFlag | ENABLE_BUDGETARY_CONTROL_FLAG | — | — |
| 31 | LedgerPEOEnableJeApprovalFlag | ENABLE_JE_APPROVAL_FLAG | — | — |
| 32 | LedgerPEOEnableReconciliationFlag | ENABLE_RECONCILIATION_FLAG | — | — |
| 33 | LedgerPEOEnableRevalSsTrackFlag | ENABLE_REVAL_SS_TRACK_FLAG | — | — |
| 34 | LedgerPEOEnableSecondaryTrackFlag | ENABLE_SECONDARY_TRACK_FLAG | — | — |
| 35 | LedgerPEOEnfSeqDateCorrelationCode | ENF_SEQ_DATE_CORRELATION_CODE | — | — |
| 36 | LedgerPEOFirstLedgerPeriodName | FIRST_LEDGER_PERIOD_NAME | — | — |
| 37 | LedgerPEOFutureEnterablePeriodsLimit | FUTURE_ENTERABLE_PERIODS_LIMIT | — | — |
| 38 | LedgerPEOImplicitAccessSetId | IMPLICIT_ACCESS_SET_ID | — | — |
| 39 | LedgerPEOImplicitLedgerSetId | IMPLICIT_LEDGER_SET_ID | — | — |
| 40 | LedgerPEOIntercoGainLossCcid | INTERCO_GAIN_LOSS_CCID | — | — |
| 41 | LedgerPEOJrnlsGroupByDateFlag | JRNLS_GROUP_BY_DATE_FLAG | — | — |
| 42 | LedgerPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 43 | LedgerPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 44 | LedgerPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 45 | LedgerPEOLatestEncumbranceYear | LATEST_ENCUMBRANCE_YEAR | — | — |
| 46 | LedgerPEOLatestOpenedPeriodName | LATEST_OPENED_PERIOD_NAME | — | — |
| 47 | LedgerPEOLeLedgerTypeCode | LE_LEDGER_TYPE_CODE | — | — |
| 48 | LedgerPEOLedgerAttributes | LEDGER_ATTRIBUTES | — | — |
| 49 | LedgerPEOLedgerCategoryCode | LEDGER_CATEGORY_CODE | — | — |
| 50 | LedgerPEOLedgerId | LEDGER_ID | — | — |
| 51 | LedgerPEOMgtSegColumnName | MGT_SEG_COLUMN_NAME | — | — |
| 52 | LedgerPEOMgtSegValueOptionCode | MGT_SEG_VALUE_OPTION_CODE | — | — |
| 53 | LedgerPEOMgtSegValueSetId | MGT_SEG_VALUE_SET_ID | — | — |
| 54 | LedgerPEOName | NAME | — | — |
| 55 | LedgerPEONetClosingBalFlag | NET_CLOSING_BAL_FLAG | — | — |
| 56 | LedgerPEONetIncomeCodeCombinationId | NET_INCOME_CODE_COMBINATION_ID | — | — |
| 57 | LedgerPEOObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 58 | LedgerPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 59 | LedgerPEOPeriodAverageRateType | PERIOD_AVERAGE_RATE_TYPE | — | — |
| 60 | LedgerPEOPeriodEndRateType | PERIOD_END_RATE_TYPE | — | — |
| 61 | LedgerPEOPeriodSetName | PERIOD_SET_NAME | — | — |
| 62 | LedgerPEOPopUpStatAccountFlag | POP_UP_STAT_ACCOUNT_FLAG | — | — |
| 63 | LedgerPEOPriorPrdNotificationFlag | PRIOR_PRD_NOTIFICATION_FLAG | — | — |
| 64 | LedgerPEORequireBudgetJournalsFlag | REQUIRE_BUDGET_JOURNALS_FLAG | — | — |
| 65 | LedgerPEOResEncumbCodeCombinationId | RES_ENCUMB_CODE_COMBINATION_ID | — | — |
| 66 | LedgerPEORetEarnCodeCombinationId | RET_EARN_CODE_COMBINATION_ID | — | — |
| 67 | LedgerPEORevalFromPriLgrCurr | REVAL_FROM_PRI_LGR_CURR | — | — |
| 68 | LedgerPEORoundingCodeCombinationId | ROUNDING_CODE_COMBINATION_ID | — | — |
| 69 | LedgerPEOSequencingModeCode | SEQUENCING_MODE_CODE | — | — |
| 70 | LedgerPEOShortName | SHORT_NAME | — | — |
| 71 | LedgerPEOSlaAccountingMethodCode | SLA_ACCOUNTING_METHOD_CODE | — | — |
| 72 | LedgerPEOSlaAccountingMethodType | SLA_ACCOUNTING_METHOD_TYPE | — | — |
| 73 | LedgerPEOSlaBalByLedgerCurrFlag | SLA_BAL_BY_LEDGER_CURR_FLAG | — | — |
| 74 | LedgerPEOSlaDescriptionLanguage | SLA_DESCRIPTION_LANGUAGE | — | — |
| 75 | LedgerPEOSlaEnteredCurBalSusCcid | SLA_ENTERED_CUR_BAL_SUS_CCID | — | — |
| 76 | LedgerPEOSlaLedgerCashBasisFlag | SLA_LEDGER_CASH_BASIS_FLAG | — | — |
| 77 | LedgerPEOSlaLedgerCurBalSusCcid | SLA_LEDGER_CUR_BAL_SUS_CCID | — | — |
| 78 | LedgerPEOSlaSequencingFlag | SLA_SEQUENCING_FLAG | — | — |
| 79 | LedgerPEOSuspenseAllowedFlag | SUSPENSE_ALLOWED_FLAG | — | — |
| 80 | LedgerPEOThresholdAmount | THRESHOLD_AMOUNT | — | — |
| 81 | LedgerPEOTrackRoundingImbalanceFlag | TRACK_ROUNDING_IMBALANCE_FLAG | — | — |
| 82 | LedgerPEOTransactionCalendarId | TRANSACTION_CALENDAR_ID | — | — |
| 83 | LedgerPEOTranslateEodFlag | TRANSLATE_EOD_FLAG | — | — |
| 84 | LedgerPEOTranslateQatdFlag | TRANSLATE_QATD_FLAG | — | — |
| 85 | LedgerPEOTranslateYatdFlag | TRANSLATE_YATD_FLAG | — | — |
| 86 | LedgerPEOUssglOptionCode | USSGL_OPTION_CODE | — | — |
| 87 | LedgerPEOValidateJournalRefDate | VALIDATE_JOURNAL_REF_DATE | — | — |

### [[inv_cons_advice_headers|INV_CONS_ADVICE_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConsumptionAdviceHeaderPEOAgreementHeaderId | AGREEMENT_HEADER_ID | — | — |
| 2 | ConsumptionAdviceHeaderPEOBpaRevisionNum | BPA_REVISION_NUM | — | — |
| 3 | ConsumptionAdviceHeaderPEOBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 4 | ConsumptionAdviceHeaderPEOConsumptionDate | CONSUMPTION_DATE | — | — |
| 5 | ConsumptionAdviceHeaderPEOConsumptionHeaderId | CONSUMPTION_HEADER_ID | — | — |
| 6 | ConsumptionAdviceHeaderPEOConsumptionHeaderId1 | CONSUMPTION_HEADER_ID | — | — |
| 7 | ConsumptionAdviceHeaderPEOConsumptionNumber | CONSUMPTION_NUMBER | — | — |
| 8 | ConsumptionAdviceHeaderPEOCreatedBy1 | CREATED_BY | — | — |
| 9 | ConsumptionAdviceHeaderPEOCreationDate1 | CREATION_DATE | — | — |
| 10 | ConsumptionAdviceHeaderPEOEndCycleDate | END_CYCLE_DATE | — | — |
| 11 | ConsumptionAdviceHeaderPEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 12 | ConsumptionAdviceHeaderPEOJobDefinitionName1 | JOB_DEFINITION_NAME | — | — |
| 13 | ConsumptionAdviceHeaderPEOJobDefinitionPackage1 | JOB_DEFINITION_PACKAGE | — | — |
| 14 | ConsumptionAdviceHeaderPEOLastDateRevised | LAST_DATE_REVISED | — | — |
| 15 | ConsumptionAdviceHeaderPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 16 | ConsumptionAdviceHeaderPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 17 | ConsumptionAdviceHeaderPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 18 | ConsumptionAdviceHeaderPEOLatestRevisionNumber | LATEST_REVISION_NUMBER | — | — |
| 19 | ConsumptionAdviceHeaderPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 20 | ConsumptionAdviceHeaderPEOLotSerialDisplayFlag | LOT_SERIAL_DISPLAY_FLAG | — | — |
| 21 | ConsumptionAdviceHeaderPEONeedPublishing | NEED_PUBLISHING | — | — |
| 22 | ConsumptionAdviceHeaderPEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 23 | ConsumptionAdviceHeaderPEOOwningEntityId | OWNING_ENTITY_ID | — | — |
| 24 | ConsumptionAdviceHeaderPEORequestId1 | REQUEST_ID | — | — |
| 25 | ConsumptionAdviceHeaderPEOStartCycleDate | START_CYCLE_DATE | — | — |

### [[inv_units_of_measure_vl|INV_UNITS_OF_MEASURE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FdLinesPhysRcptUomPEOBaseUomFlag | BASE_UOM_FLAG | — | — |
| 2 | FdLinesPhysRcptUomPEOCreatedBy4 | CREATED_BY | — | — |
| 3 | FdLinesPhysRcptUomPEOCreationDate4 | CREATION_DATE | — | — |
| 4 | FdLinesPhysRcptUomPEODescription | DESCRIPTION | — | — |
| 5 | FdLinesPhysRcptUomPEODisableDate | DISABLE_DATE | — | — |
| 6 | FdLinesPhysRcptUomPEOGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 7 | FdLinesPhysRcptUomPEOGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 8 | FdLinesPhysRcptUomPEOHasGeneratedCode | HAS_GENERATED_CODE | — | — |
| 9 | FdLinesPhysRcptUomPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 10 | FdLinesPhysRcptUomPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 11 | FdLinesPhysRcptUomPEOLastUpdateDate4 | LAST_UPDATE_DATE | — | — |
| 12 | FdLinesPhysRcptUomPEOLastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 13 | FdLinesPhysRcptUomPEOLastUpdatedBy4 | LAST_UPDATED_BY | — | — |
| 14 | FdLinesPhysRcptUomPEOObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |
| 15 | FdLinesPhysRcptUomPEORequestId | REQUEST_ID | — | — |
| 16 | FdLinesPhysRcptUomPEOStandardPackFlag | STANDARD_PACK_FLAG | — | — |
| 17 | FdLinesPhysRcptUomPEOUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 18 | FdLinesPhysRcptUomPEOUnitOfMeasureId | UNIT_OF_MEASURE_ID | — | — |
| 19 | FdLinesPhysRcptUomPEOUomClass | UOM_CLASS | — | — |
| 20 | FdLinesPhysRcptUomPEOUomCode | UOM_CODE | — | — |
| 21 | FdLinesPhysRcptUomPEOUomPluralDesc | UOM_PLURAL_DESC | — | — |
| 22 | FdLinesPhysRcptUomPEOUomReciprocalDesc | UOM_RECIPROCAL_DESC | — | — |
| 23 | UnitOfMeasurePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 24 | UnitOfMeasurePEOBaseUomFlag | BASE_UOM_FLAG | — | — |
| 25 | UnitOfMeasurePEOCreatedBy | CREATED_BY | — | — |
| 26 | UnitOfMeasurePEOCreationDate | CREATION_DATE | — | — |
| 27 | UnitOfMeasurePEODescription | DESCRIPTION | — | — |
| 28 | UnitOfMeasurePEODisableDate | DISABLE_DATE | — | — |
| 29 | UnitOfMeasurePEOGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 30 | UnitOfMeasurePEOHasGeneratedCode | HAS_GENERATED_CODE | — | — |
| 31 | UnitOfMeasurePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 32 | UnitOfMeasurePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 33 | UnitOfMeasurePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 34 | UnitOfMeasurePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 35 | UnitOfMeasurePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 36 | UnitOfMeasurePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 37 | UnitOfMeasurePEORequestId | REQUEST_ID | — | — |
| 38 | UnitOfMeasurePEOStandardPackFlag | STANDARD_PACK_FLAG | — | — |
| 39 | UnitOfMeasurePEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 40 | UnitOfMeasurePEOUnitOfMeasureId | UNIT_OF_MEASURE_ID | — | — |
| 41 | UnitOfMeasurePEOUomClass | UOM_CLASS | — | — |
| 42 | UnitOfMeasurePEOUomCode | UOM_CODE | — | — |
| 43 | UnitOfMeasurePEOUomPluralDesc | UOM_PLURAL_DESC | — | — |
| 44 | UnitOfMeasurePEOUomReciprocalDesc | UOM_RECIPROCAL_DESC | — | — |

### [[jg_fscl_hdrs_atrb_ext_all|JG_FSCL_HDRS_ATRB_EXT_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocHeaderExtnEOApplicationId | APPLICATION_ID | — | — |
| 2 | FiscalDocHeaderExtnEOCommitmentStatementIdent | COMMITMENT_STATEMENT_IDENT | — | — |
| 3 | FiscalDocHeaderExtnEOContainerIdentifier | CONTAINER_IDENTIFIER | — | ✅ |
| 4 | FiscalDocHeaderExtnEOContingencyType | CONTINGENCY_TYPE | — | ✅ |
| 5 | FiscalDocHeaderExtnEOCreatedBy | CREATED_BY | — | — |
| 6 | FiscalDocHeaderExtnEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | FiscalDocHeaderExtnEODocExtHdrId | DOC_EXT_HDR_ID | — | — |
| 8 | FiscalDocHeaderExtnEODocNature | DOC_NATURE | — | ✅ |
| 9 | FiscalDocHeaderExtnEOEntityCode | ENTITY_CODE | — | — |
| 10 | FiscalDocHeaderExtnEOEventClassCode | EVENT_CLASS_CODE | — | — |
| 11 | FiscalDocHeaderExtnEOFerryIdentification | FERRY_IDENTIFICATION | — | ✅ |
| 12 | FiscalDocHeaderExtnEOFiscalDocDate | FISCAL_DOC_DATE | — | ✅ |
| 13 | FiscalDocHeaderExtnEOFreightPartySiteId | FREIGHT_PARTY_SITE_ID | — | — |
| 14 | FiscalDocHeaderExtnEOFreightType | FREIGHT_TYPE | — | ✅ |
| 15 | FiscalDocHeaderExtnEOGoodsBrandCarried | GOODS_BRAND_CARRIED | — | ✅ |
| 16 | FiscalDocHeaderExtnEOGoodsTypeCarried | GOODS_TYPE_CARRIED | — | ✅ |
| 17 | FiscalDocHeaderExtnEOGrossWeight | GROSS_WEIGHT | — | ✅ |
| 18 | FiscalDocHeaderExtnEOIndustryType | INDUSTRY_TYPE | — | ✅ |
| 19 | FiscalDocHeaderExtnEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 20 | FiscalDocHeaderExtnEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 21 | FiscalDocHeaderExtnEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | FiscalDocHeaderExtnEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 23 | FiscalDocHeaderExtnEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 24 | FiscalDocHeaderExtnEOLegalReportingUnitId | LEGAL_REPORTING_UNIT_ID | — | — |
| 25 | FiscalDocHeaderExtnEOMatIssueRecptDate | MAT_ISSUE_RECPT_DATE | — | ✅ |
| 26 | FiscalDocHeaderExtnEOMatIssueRecptHour | MAT_ISSUE_RECPT_HOUR | — | ✅ |
| 27 | FiscalDocHeaderExtnEONetWeight | NET_WEIGHT | — | ✅ |
| 28 | FiscalDocHeaderExtnEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 29 | FiscalDocHeaderExtnEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 30 | FiscalDocHeaderExtnEOOrgId | ORG_ID | — | — |
| 31 | FiscalDocHeaderExtnEOPaymentOption | PAYMENT_OPTION | — | ✅ |
| 32 | FiscalDocHeaderExtnEOPurchaseContract | PURCHASE_CONTRACT | — | ✅ |
| 33 | FiscalDocHeaderExtnEOQuantityCarried | QUANTITY_CARRIED | — | ✅ |
| 34 | FiscalDocHeaderExtnEORefComplementaryFdFlag | REF_COMPLEMENTARY_FD_FLAG | — | ✅ |
| 35 | FiscalDocHeaderExtnEORefDocIssuerStateCode | REF_DOC_ISSUER_STATE_CODE | — | ✅ |
| 36 | FiscalDocHeaderExtnEORefDocNum | REF_DOC_NUM | — | ✅ |
| 37 | FiscalDocHeaderExtnEORefFiscalDocDate | REF_FISCAL_DOC_DATE | — | ✅ |
| 38 | FiscalDocHeaderExtnEORefFiscalDocKey | REF_FISCAL_DOC_KEY | — | ✅ |
| 39 | FiscalDocHeaderExtnEORefIssuerTaxpayerId | REF_ISSUER_TAXPAYER_ID | — | ✅ |
| 40 | FiscalDocHeaderExtnEORefModel | REF_MODEL | — | ✅ |
| 41 | FiscalDocHeaderExtnEORefRuralFlag | REF_RURAL_FLAG | — | ✅ |
| 42 | FiscalDocHeaderExtnEORefSeries | REF_SERIES | — | ✅ |
| 43 | FiscalDocHeaderExtnEORequestId | REQUEST_ID | — | — |
| 44 | FiscalDocHeaderExtnEOSealNumber | SEAL_NUMBER | — | ✅ |
| 45 | FiscalDocHeaderExtnEOSeries | SERIES | — | ✅ |
| 46 | FiscalDocHeaderExtnEOServiceSeries | SERVICE_SERIES | — | ✅ |
| 47 | FiscalDocHeaderExtnEOServiceSituation | SERVICE_SITUATION | — | ✅ |
| 48 | FiscalDocHeaderExtnEOServiceTaxPaidFlag | SERVICE_TAX_PAID_FLAG | — | ✅ |
| 49 | FiscalDocHeaderExtnEOServiceType | SERVICE_TYPE | — | ✅ |
| 50 | FiscalDocHeaderExtnEOTaxSettlementDate | TAX_SETTLEMENT_DATE | — | ✅ |
| 51 | FiscalDocHeaderExtnEOTrxFdTypeDeterminant | TRX_FD_TYPE_DETERMINANT | — | ✅ |
| 52 | FiscalDocHeaderExtnEOTrxId | TRX_ID | — | — |
| 53 | FiscalDocHeaderExtnEOTrxNumber | TRX_NUMBER | — | ✅ |
| 54 | FiscalDocHeaderExtnEOWagonIdentification | WAGON_IDENTIFICATION | — | ✅ |
| 55 | FiscalDocHeaderExtnEOWhtSocialIntgProgAmt | WHT_SOCIAL_INTG_PROG_AMT | — | — |
| 56 | FiscalDocHeaderExtnEOWhtSsFinancingAmt | WHT_SS_FINANCING_AMT | — | — |

### [[jg_fscl_hdr_dtls_atrb_ext_all|JG_FSCL_HDR_DTLS_ATRB_EXT_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocHeaderDetailExtnEOApplicationId | APPLICATION_ID | — | — |
| 2 | FiscalDocHeaderDetailExtnEOCreatedBy | CREATED_BY | — | — |
| 3 | FiscalDocHeaderDetailExtnEOCreationDate | CREATION_DATE | — | — |
| 4 | FiscalDocHeaderDetailExtnEODocExtHdrId | DOC_EXT_HDR_ID | — | — |
| 5 | FiscalDocHeaderDetailExtnEOEntityCode | ENTITY_CODE | — | — |
| 6 | FiscalDocHeaderDetailExtnEOEventClassCode | EVENT_CLASS_CODE | — | — |
| 7 | FiscalDocHeaderDetailExtnEOHdrAtrbExtDtlId | HDR_ATRB_EXT_DTL_ID | — | — |
| 8 | FiscalDocHeaderDetailExtnEOHdrAtrbExtDtlId1 | HDR_ATRB_EXT_DTL_ID | — | — |
| 9 | FiscalDocHeaderDetailExtnEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 10 | FiscalDocHeaderDetailExtnEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 11 | FiscalDocHeaderDetailExtnEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 12 | FiscalDocHeaderDetailExtnEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | FiscalDocHeaderDetailExtnEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | FiscalDocHeaderDetailExtnEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | FiscalDocHeaderDetailExtnEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 16 | FiscalDocHeaderDetailExtnEOOrgId | ORG_ID | — | — |
| 17 | FiscalDocHeaderDetailExtnEORecordType | RECORD_TYPE | — | — |
| 18 | FiscalDocHeaderDetailExtnEORequestId | REQUEST_ID | — | — |
| 19 | FiscalDocHeaderDetailExtnEOTaxRelatedLegalMessageFlag | TAX_RELATED_LEGAL_MESSAGE_FLAG | — | — |
| 20 | FiscalDocHeaderDetailExtnEOTrxId | TRX_ID | — | — |

### [[jg_fscl_lines_atrb_ext_all|JG_FSCL_LINES_ATRB_EXT_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocLineExtnEOApplicationId | APPLICATION_ID | — | — |
| 2 | FiscalDocLineExtnEOCreatedBy | CREATED_BY | — | — |
| 3 | FiscalDocLineExtnEOCreationDate | CREATION_DATE | — | — |
| 4 | FiscalDocLineExtnEODocExtHdrId | DOC_EXT_HDR_ID | — | — |
| 5 | FiscalDocLineExtnEODocExtLineId | DOC_EXT_LINE_ID | — | — |
| 6 | FiscalDocLineExtnEOEntityCode | ENTITY_CODE | — | — |
| 7 | FiscalDocLineExtnEOEventClassCode | EVENT_CLASS_CODE | — | — |
| 8 | FiscalDocLineExtnEOItemSerialNumber | ITEM_SERIAL_NUMBER | — | — |
| 9 | FiscalDocLineExtnEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 10 | FiscalDocLineExtnEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 11 | FiscalDocLineExtnEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 12 | FiscalDocLineExtnEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | FiscalDocLineExtnEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | FiscalDocLineExtnEOLegalMessageText | LEGAL_MESSAGE_TEXT | — | ✅ |
| 15 | FiscalDocLineExtnEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | FiscalDocLineExtnEOOrgId | ORG_ID | — | — |
| 17 | FiscalDocLineExtnEOProceedingIdentifier | PROCEEDING_IDENTIFIER | — | ✅ |
| 18 | FiscalDocLineExtnEOProceedingOrigin | PROCEEDING_ORIGIN | — | ✅ |
| 19 | FiscalDocLineExtnEORequestId | REQUEST_ID | — | — |
| 20 | FiscalDocLineExtnEOServiceSituation | SERVICE_SITUATION | — | ✅ |
| 21 | FiscalDocLineExtnEOTrxId | TRX_ID | — | — |
| 22 | FiscalDocLineExtnEOTrxLevelType | TRX_LEVEL_TYPE | — | ✅ |
| 23 | FiscalDocLineExtnEOTrxLineId | TRX_LINE_ID | — | — |

### [[jg_fscl_ln_dtls_atrb_ext_all|JG_FSCL_LN_DTLS_ATRB_EXT_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocLineDetailExtnEOApplicationId1 | APPLICATION_ID | — | — |
| 2 | FiscalDocLineDetailExtnEOCreatedBy1 | CREATED_BY | — | — |
| 3 | FiscalDocLineDetailExtnEOCreationDate1 | CREATION_DATE | — | — |
| 4 | FiscalDocLineDetailExtnEODocExtHdrId1 | DOC_EXT_HDR_ID | — | — |
| 5 | FiscalDocLineDetailExtnEODocExtLineDetailId | DOC_EXT_LINE_DETAIL_ID | — | — |
| 6 | FiscalDocLineDetailExtnEODocExtLineId1 | DOC_EXT_LINE_ID | — | — |
| 7 | FiscalDocLineDetailExtnEOEntityCode1 | ENTITY_CODE | — | — |
| 8 | FiscalDocLineDetailExtnEOEventClassCode1 | EVENT_CLASS_CODE | — | — |
| 9 | FiscalDocLineDetailExtnEOJobDefinitionName1 | JOB_DEFINITION_NAME | — | — |
| 10 | FiscalDocLineDetailExtnEOJobDefinitionPackage1 | JOB_DEFINITION_PACKAGE | — | — |
| 11 | FiscalDocLineDetailExtnEOLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 12 | FiscalDocLineDetailExtnEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 13 | FiscalDocLineDetailExtnEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 14 | FiscalDocLineDetailExtnEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 15 | FiscalDocLineDetailExtnEOOrgId1 | ORG_ID | — | — |
| 16 | FiscalDocLineDetailExtnEORequestId1 | REQUEST_ID | — | — |
| 17 | FiscalDocLineDetailExtnEOTrxId1 | TRX_ID | — | — |
| 18 | FiscalDocLineDetailExtnEOTrxLevelType1 | TRX_LEVEL_TYPE | — | ✅ |
| 19 | FiscalDocLineDetailExtnEOTrxLineDetailId | TRX_LINE_DETAIL_ID | — | — |
| 20 | FiscalDocLineDetailExtnEOTrxLineId1 | TRX_LINE_ID | — | — |

### [[jg_fscl_tax_lines_all|JG_FSCL_TAX_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocTaxLineEOAdjustedTaxLineId | ADJUSTED_TAX_LINE_ID | — | — |
| 2 | FiscalDocTaxLineEOApplicationId | APPLICATION_ID | — | — |
| 3 | FiscalDocTaxLineEOCalTaxAmt | CAL_TAX_AMT | — | ✅ |
| 4 | FiscalDocTaxLineEOCalTaxAmtTaxCurr | CAL_TAX_AMT_TAX_CURR | — | ✅ |
| 5 | FiscalDocTaxLineEOCityCode | CITY_CODE | — | — |
| 6 | FiscalDocTaxLineEOContentOwnerId | CONTENT_OWNER_ID | — | — |
| 7 | FiscalDocTaxLineEOCreatedBy | CREATED_BY | — | — |
| 8 | FiscalDocTaxLineEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | FiscalDocTaxLineEOEntityCode | ENTITY_CODE | — | — |
| 10 | FiscalDocTaxLineEOEventClassCode | EVENT_CLASS_CODE | — | — |
| 11 | FiscalDocTaxLineEOExemptCertificateNumber | EXEMPT_CERTIFICATE_NUMBER | — | — |
| 12 | FiscalDocTaxLineEOExemptReasonCode | EXEMPT_REASON_CODE | — | — |
| 13 | FiscalDocTaxLineEOInterfaceEntityCode | INTERFACE_ENTITY_CODE | — | — |
| 14 | FiscalDocTaxLineEOInterfaceTaxLineId | INTERFACE_TAX_LINE_ID | — | — |
| 15 | FiscalDocTaxLineEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 16 | FiscalDocTaxLineEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 17 | FiscalDocTaxLineEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | FiscalDocTaxLineEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | FiscalDocTaxLineEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | FiscalDocTaxLineEOMainTrxLineId | MAIN_TRX_LINE_ID | — | — |
| 21 | FiscalDocTaxLineEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | FiscalDocTaxLineEOOrgId | ORG_ID | — | — |
| 23 | FiscalDocTaxLineEOOrigSelfAssessedFlag | ORIG_SELF_ASSESSED_FLAG | — | — |
| 24 | FiscalDocTaxLineEOOrigTaxAmtIncludedFlag | ORIG_TAX_AMT_INCLUDED_FLAG | — | — |
| 25 | FiscalDocTaxLineEOOrigTaxJurisdictionCode | ORIG_TAX_JURISDICTION_CODE | — | — |
| 26 | FiscalDocTaxLineEOOrigTaxJurisdictionId | ORIG_TAX_JURISDICTION_ID | — | — |
| 27 | FiscalDocTaxLineEOOrigTaxRate | ORIG_TAX_RATE | — | — |
| 28 | FiscalDocTaxLineEOOrigTaxRateCode | ORIG_TAX_RATE_CODE | — | — |
| 29 | FiscalDocTaxLineEOOrigTaxRateId | ORIG_TAX_RATE_ID | — | — |
| 30 | FiscalDocTaxLineEOOrigTaxStatusCode | ORIG_TAX_STATUS_CODE | — | — |
| 31 | FiscalDocTaxLineEOOrigTaxStatusId | ORIG_TAX_STATUS_ID | — | — |
| 32 | FiscalDocTaxLineEOQuantity | QUANTITY | — | ✅ |
| 33 | FiscalDocTaxLineEOReferenceDocLineAmt | REFERENCE_DOC_LINE_AMT | — | — |
| 34 | FiscalDocTaxLineEOReferenceDocUnitPrice | REFERENCE_DOC_UNIT_PRICE | — | — |
| 35 | FiscalDocTaxLineEOReportingTypeCode | REPORTING_TYPE_CODE | — | ✅ |
| 36 | FiscalDocTaxLineEORequestId | REQUEST_ID | — | — |
| 37 | FiscalDocTaxLineEOSelfAssessedFlag | SELF_ASSESSED_FLAG | — | ✅ |
| 38 | FiscalDocTaxLineEOServiceItemCode | SERVICE_ITEM_CODE | — | — |
| 39 | FiscalDocTaxLineEOTax | TAX | — | ✅ |
| 40 | FiscalDocTaxLineEOTaxAmt | TAX_AMT | — | ✅ |
| 41 | FiscalDocTaxLineEOTaxAmtIncludedFlag | TAX_AMT_INCLUDED_FLAG | — | ✅ |
| 42 | FiscalDocTaxLineEOTaxAmtTaxCurr | TAX_AMT_TAX_CURR | — | ✅ |
| 43 | FiscalDocTaxLineEOTaxCreditAmount | TAX_CREDIT_AMOUNT | — | — |
| 44 | FiscalDocTaxLineEOTaxExceptionId | TAX_EXCEPTION_ID | — | — |
| 45 | FiscalDocTaxLineEOTaxExemptionId | TAX_EXEMPTION_ID | — | — |
| 46 | FiscalDocTaxLineEOTaxHoldCode | TAX_HOLD_CODE | — | ✅ |
| 47 | FiscalDocTaxLineEOTaxId | TAX_ID | — | — |
| 48 | FiscalDocTaxLineEOTaxJurisdictionCode | TAX_JURISDICTION_CODE | — | ✅ |
| 49 | FiscalDocTaxLineEOTaxJurisdictionId | TAX_JURISDICTION_ID | — | — |
| 50 | FiscalDocTaxLineEOTaxLineId | TAX_LINE_ID | — | — |
| 51 | FiscalDocTaxLineEOTaxLineNumber | TAX_LINE_NUMBER | — | ✅ |
| 52 | FiscalDocTaxLineEOTaxLineSourceCode | TAX_LINE_SOURCE_CODE | — | — |
| 53 | FiscalDocTaxLineEOTaxOnlyLineFlag | TAX_ONLY_LINE_FLAG | — | — |
| 54 | FiscalDocTaxLineEOTaxRate | TAX_RATE | — | ✅ |
| 55 | FiscalDocTaxLineEOTaxRateCode | TAX_RATE_CODE | — | ✅ |
| 56 | FiscalDocTaxLineEOTaxRateId | TAX_RATE_ID | — | — |
| 57 | FiscalDocTaxLineEOTaxRegimeCode | TAX_REGIME_CODE | — | ✅ |
| 58 | FiscalDocTaxLineEOTaxRegimeId | TAX_REGIME_ID | — | — |
| 59 | FiscalDocTaxLineEOTaxSituationCode | TAX_SITUATION_CODE | — | — |
| 60 | FiscalDocTaxLineEOTaxStatusCode | TAX_STATUS_CODE | — | ✅ |
| 61 | FiscalDocTaxLineEOTaxStatusId | TAX_STATUS_ID | — | — |
| 62 | FiscalDocTaxLineEOTaxableAmt | TAXABLE_AMT | — | ✅ |
| 63 | FiscalDocTaxLineEOTaxableAmtDetermCode | TAXABLE_AMT_DETERM_CODE | — | — |
| 64 | FiscalDocTaxLineEOTaxableBasisPercPayerOpr | TAXABLE_BASIS_PERC_PAYER_OPR | — | — |
| 65 | FiscalDocTaxLineEOTaxableBasisReductionPerc | TAXABLE_BASIS_REDUCTION_PERC | — | — |
| 66 | FiscalDocTaxLineEOTrxId | TRX_ID | — | — |
| 67 | FiscalDocTaxLineEOTrxLevelType | TRX_LEVEL_TYPE | — | — |
| 68 | FiscalDocTaxLineEOTrxLineId | TRX_LINE_ID | — | — |
| 69 | FiscalDocTaxLineEOUomCode | UOM_CODE | — | ✅ |
| 70 | FiscalDocTaxLineEOUserEnteredTaxAmt | USER_ENTERED_TAX_AMT | — | ✅ |
| 71 | FiscalDocTaxLineEOUserEnteredTaxAmtTaxCurr | USER_ENTERED_TAX_AMT_TAX_CURR | — | ✅ |
| 72 | FiscalDocTaxLineEOValueAddedMarginPerc | VALUE_ADDED_MARGIN_PERC | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedByPersonNameDPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CreatedByPersonNameDPEOCreatedBy | CREATED_BY | — | — |
| 3 | CreatedByPersonNameDPEOCreationDate | CREATION_DATE | — | — |
| 4 | CreatedByPersonNameDPEODisplayName | DISPLAY_NAME | — | — |
| 5 | CreatedByPersonNameDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | CreatedByPersonNameDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 7 | CreatedByPersonNameDPEOFirstName | FIRST_NAME | — | — |
| 8 | CreatedByPersonNameDPEOFullName | FULL_NAME | — | ✅ |
| 9 | CreatedByPersonNameDPEOHonors | HONORS | — | — |
| 10 | CreatedByPersonNameDPEOKnownAs | KNOWN_AS | — | — |
| 11 | CreatedByPersonNameDPEOLastName | LAST_NAME | — | — |
| 12 | CreatedByPersonNameDPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 13 | CreatedByPersonNameDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | CreatedByPersonNameDPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | CreatedByPersonNameDPEOLegislationCode | LEGISLATION_CODE | — | — |
| 16 | CreatedByPersonNameDPEOListName | LIST_NAME | — | — |
| 17 | CreatedByPersonNameDPEOMiddleNames | MIDDLE_NAMES | — | — |
| 18 | CreatedByPersonNameDPEOMilitaryRank | MILITARY_RANK | — | — |
| 19 | CreatedByPersonNameDPEONameType | NAME_TYPE | — | — |
| 20 | CreatedByPersonNameDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | CreatedByPersonNameDPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 22 | CreatedByPersonNameDPEOOrderName | ORDER_NAME | — | — |
| 23 | CreatedByPersonNameDPEOPersonId | PERSON_ID | — | — |
| 24 | CreatedByPersonNameDPEOPersonNameId | PERSON_NAME_ID | — | — |
| 25 | CreatedByPersonNameDPEOPersonNameId1 | PERSON_NAME_ID | — | — |
| 26 | CreatedByPersonNameDPEOPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 27 | CreatedByPersonNameDPEOPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 28 | CreatedByPersonNameDPEOSuffix | SUFFIX | — | — |
| 29 | CreatedByPersonNameDPEOTitle | TITLE | — | — |
| 30 | FdHxCrtdByPersonNameDPEOBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 31 | FdHxCrtdByPersonNameDPEOCreatedBy2 | CREATED_BY | — | — |
| 32 | FdHxCrtdByPersonNameDPEOCreationDate2 | CREATION_DATE | — | — |
| 33 | FdHxCrtdByPersonNameDPEODisplayName | DISPLAY_NAME | — | — |
| 34 | FdHxCrtdByPersonNameDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 35 | FdHxCrtdByPersonNameDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 36 | FdHxCrtdByPersonNameDPEOFirstName | FIRST_NAME | — | — |
| 37 | FdHxCrtdByPersonNameDPEOFullName | FULL_NAME | — | ✅ |
| 38 | FdHxCrtdByPersonNameDPEOHonors | HONORS | — | — |
| 39 | FdHxCrtdByPersonNameDPEOKnownAs | KNOWN_AS | — | — |
| 40 | FdHxCrtdByPersonNameDPEOLastName | LAST_NAME | — | — |
| 41 | FdHxCrtdByPersonNameDPEOLastUpdateDate2 | LAST_UPDATE_DATE | — | — |
| 42 | FdHxCrtdByPersonNameDPEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 43 | FdHxCrtdByPersonNameDPEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 44 | FdHxCrtdByPersonNameDPEOLegislationCode | LEGISLATION_CODE | — | — |
| 45 | FdHxCrtdByPersonNameDPEOListName | LIST_NAME | — | — |
| 46 | FdHxCrtdByPersonNameDPEOMiddleNames | MIDDLE_NAMES | — | — |
| 47 | FdHxCrtdByPersonNameDPEOMilitaryRank | MILITARY_RANK | — | — |
| 48 | FdHxCrtdByPersonNameDPEONameType | NAME_TYPE | — | — |
| 49 | FdHxCrtdByPersonNameDPEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 50 | FdHxCrtdByPersonNameDPEOObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 51 | FdHxCrtdByPersonNameDPEOOrderName | ORDER_NAME | — | — |
| 52 | FdHxCrtdByPersonNameDPEOPersonId2 | PERSON_ID | — | — |
| 53 | FdHxCrtdByPersonNameDPEOPersonNameId | PERSON_NAME_ID | — | — |
| 54 | FdHxCrtdByPersonNameDPEOPersonNameId1 | PERSON_NAME_ID | — | — |
| 55 | FdHxCrtdByPersonNameDPEOPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 56 | FdHxCrtdByPersonNameDPEOPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 57 | FdHxCrtdByPersonNameDPEOSuffix | SUFFIX | — | — |
| 58 | FdHxCrtdByPersonNameDPEOTitle | TITLE | — | — |
| 59 | FdHxLastUpdByPersonNameDPEOBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 60 | FdHxLastUpdByPersonNameDPEOCreatedBy3 | CREATED_BY | — | — |
| 61 | FdHxLastUpdByPersonNameDPEOCreationDate3 | CREATION_DATE | — | — |
| 62 | FdHxLastUpdByPersonNameDPEODisplayName1 | DISPLAY_NAME | — | — |
| 63 | FdHxLastUpdByPersonNameDPEOEffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 64 | FdHxLastUpdByPersonNameDPEOEffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 65 | FdHxLastUpdByPersonNameDPEOFirstName1 | FIRST_NAME | — | — |
| 66 | FdHxLastUpdByPersonNameDPEOFullName1 | FULL_NAME | — | ✅ |
| 67 | FdHxLastUpdByPersonNameDPEOHonors1 | HONORS | — | — |
| 68 | FdHxLastUpdByPersonNameDPEOKnownAs1 | KNOWN_AS | — | — |
| 69 | FdHxLastUpdByPersonNameDPEOLastName1 | LAST_NAME | — | — |
| 70 | FdHxLastUpdByPersonNameDPEOLastUpdateDate3 | LAST_UPDATE_DATE | — | — |
| 71 | FdHxLastUpdByPersonNameDPEOLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 72 | FdHxLastUpdByPersonNameDPEOLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 73 | FdHxLastUpdByPersonNameDPEOLegislationCode1 | LEGISLATION_CODE | — | — |
| 74 | FdHxLastUpdByPersonNameDPEOListName1 | LIST_NAME | — | — |
| 75 | FdHxLastUpdByPersonNameDPEOMiddleNames1 | MIDDLE_NAMES | — | — |
| 76 | FdHxLastUpdByPersonNameDPEOMilitaryRank1 | MILITARY_RANK | — | — |
| 77 | FdHxLastUpdByPersonNameDPEONameType1 | NAME_TYPE | — | — |
| 78 | FdHxLastUpdByPersonNameDPEOObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 79 | FdHxLastUpdByPersonNameDPEOObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 80 | FdHxLastUpdByPersonNameDPEOOrderName1 | ORDER_NAME | — | — |
| 81 | FdHxLastUpdByPersonNameDPEOPersonId3 | PERSON_ID | — | — |
| 82 | FdHxLastUpdByPersonNameDPEOPersonNameId2 | PERSON_NAME_ID | — | — |
| 83 | FdHxLastUpdByPersonNameDPEOPersonNameId3 | PERSON_NAME_ID | — | — |
| 84 | FdHxLastUpdByPersonNameDPEOPreNameAdjunct1 | PRE_NAME_ADJUNCT | — | — |
| 85 | FdHxLastUpdByPersonNameDPEOPreviousLastName1 | PREVIOUS_LAST_NAME | — | — |
| 86 | FdHxLastUpdByPersonNameDPEOSuffix1 | SUFFIX | — | — |
| 87 | FdHxLastUpdByPersonNameDPEOTitle1 | TITLE | — | — |
| 88 | FdLinesCrtdByPersonNameDPEOBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 89 | FdLinesCrtdByPersonNameDPEOCreatedBy2 | CREATED_BY | — | — |
| 90 | FdLinesCrtdByPersonNameDPEOCreationDate2 | CREATION_DATE | — | — |
| 91 | FdLinesCrtdByPersonNameDPEODisplayName | DISPLAY_NAME | — | — |
| 92 | FdLinesCrtdByPersonNameDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 93 | FdLinesCrtdByPersonNameDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 94 | FdLinesCrtdByPersonNameDPEOFirstName | FIRST_NAME | — | — |
| 95 | FdLinesCrtdByPersonNameDPEOFullName | FULL_NAME | — | ✅ |
| 96 | FdLinesCrtdByPersonNameDPEOHonors | HONORS | — | — |
| 97 | FdLinesCrtdByPersonNameDPEOKnownAs | KNOWN_AS | — | — |
| 98 | FdLinesCrtdByPersonNameDPEOLastName | LAST_NAME | — | — |
| 99 | FdLinesCrtdByPersonNameDPEOLastUpdateDate2 | LAST_UPDATE_DATE | — | — |
| 100 | FdLinesCrtdByPersonNameDPEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 101 | FdLinesCrtdByPersonNameDPEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 102 | FdLinesCrtdByPersonNameDPEOLegislationCode | LEGISLATION_CODE | — | — |
| 103 | FdLinesCrtdByPersonNameDPEOListName | LIST_NAME | — | — |
| 104 | FdLinesCrtdByPersonNameDPEOMiddleNames | MIDDLE_NAMES | — | — |
| 105 | FdLinesCrtdByPersonNameDPEOMilitaryRank | MILITARY_RANK | — | — |
| 106 | FdLinesCrtdByPersonNameDPEONameType | NAME_TYPE | — | — |
| 107 | FdLinesCrtdByPersonNameDPEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 108 | FdLinesCrtdByPersonNameDPEOObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 109 | FdLinesCrtdByPersonNameDPEOOrderName | ORDER_NAME | — | — |
| 110 | FdLinesCrtdByPersonNameDPEOPersonId2 | PERSON_ID | — | — |
| 111 | FdLinesCrtdByPersonNameDPEOPersonNameId | PERSON_NAME_ID | — | — |
| 112 | FdLinesCrtdByPersonNameDPEOPersonNameId1 | PERSON_NAME_ID | — | — |
| 113 | FdLinesCrtdByPersonNameDPEOPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 114 | FdLinesCrtdByPersonNameDPEOPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 115 | FdLinesCrtdByPersonNameDPEOSuffix | SUFFIX | — | — |
| 116 | FdLinesCrtdByPersonNameDPEOTitle | TITLE | — | — |
| 117 | FdLinesLastUpdByPersonNameDPBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 118 | FdLinesLastUpdByPersonNameDPCreatedBy3 | CREATED_BY | — | — |
| 119 | FdLinesLastUpdByPersonNameDPCreationDate3 | CREATION_DATE | — | — |
| 120 | FdLinesLastUpdByPersonNameDPDisplayName1 | DISPLAY_NAME | — | — |
| 121 | FdLinesLastUpdByPersonNameDPEffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 122 | FdLinesLastUpdByPersonNameDPEffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 123 | FdLinesLastUpdByPersonNameDPFirstName1 | FIRST_NAME | — | — |
| 124 | FdLinesLastUpdByPersonNameDPFullName1 | FULL_NAME | — | ✅ |
| 125 | FdLinesLastUpdByPersonNameDPHonors1 | HONORS | — | — |
| 126 | FdLinesLastUpdByPersonNameDPKnownAs1 | KNOWN_AS | — | — |
| 127 | FdLinesLastUpdByPersonNameDPLastName1 | LAST_NAME | — | — |
| 128 | FdLinesLastUpdByPersonNameDPLastUpdateDate3 | LAST_UPDATE_DATE | — | — |
| 129 | FdLinesLastUpdByPersonNameDPLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 130 | FdLinesLastUpdByPersonNameDPLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 131 | FdLinesLastUpdByPersonNameDPLegislationCode1 | LEGISLATION_CODE | — | — |
| 132 | FdLinesLastUpdByPersonNameDPListName1 | LIST_NAME | — | — |
| 133 | FdLinesLastUpdByPersonNameDPMiddleNames1 | MIDDLE_NAMES | — | — |
| 134 | FdLinesLastUpdByPersonNameDPMilitaryRank1 | MILITARY_RANK | — | — |
| 135 | FdLinesLastUpdByPersonNameDPNameType1 | NAME_TYPE | — | — |
| 136 | FdLinesLastUpdByPersonNameDPObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 137 | FdLinesLastUpdByPersonNameDPObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 138 | FdLinesLastUpdByPersonNameDPOrderName1 | ORDER_NAME | — | — |
| 139 | FdLinesLastUpdByPersonNameDPPersonId3 | PERSON_ID | — | — |
| 140 | FdLinesLastUpdByPersonNameDPPersonNameId2 | PERSON_NAME_ID | — | — |
| 141 | FdLinesLastUpdByPersonNameDPPersonNameId3 | PERSON_NAME_ID | — | — |
| 142 | FdLinesLastUpdByPersonNameDPPreNameAdjunct1 | PRE_NAME_ADJUNCT | — | — |
| 143 | FdLinesLastUpdByPersonNameDPPreviousLastName1 | PREVIOUS_LAST_NAME | — | — |
| 144 | FdLinesLastUpdByPersonNameDPSuffix1 | SUFFIX | — | — |
| 145 | FdLinesLastUpdByPersonNameDPTitle1 | TITLE | — | — |
| 146 | FdTaxCrtdByPersonNameDPEOBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 147 | FdTaxCrtdByPersonNameDPEOCreatedBy2 | CREATED_BY | — | — |
| 148 | FdTaxCrtdByPersonNameDPEOCreationDate2 | CREATION_DATE | — | — |
| 149 | FdTaxCrtdByPersonNameDPEODisplayName | DISPLAY_NAME | — | — |
| 150 | FdTaxCrtdByPersonNameDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 151 | FdTaxCrtdByPersonNameDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 152 | FdTaxCrtdByPersonNameDPEOFirstName | FIRST_NAME | — | — |
| 153 | FdTaxCrtdByPersonNameDPEOFullName | FULL_NAME | — | ✅ |
| 154 | FdTaxCrtdByPersonNameDPEOHonors | HONORS | — | — |
| 155 | FdTaxCrtdByPersonNameDPEOKnownAs | KNOWN_AS | — | — |
| 156 | FdTaxCrtdByPersonNameDPEOLastName | LAST_NAME | — | — |
| 157 | FdTaxCrtdByPersonNameDPEOLastUpdateDate2 | LAST_UPDATE_DATE | — | — |
| 158 | FdTaxCrtdByPersonNameDPEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 159 | FdTaxCrtdByPersonNameDPEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 160 | FdTaxCrtdByPersonNameDPEOLegislationCode | LEGISLATION_CODE | — | — |
| 161 | FdTaxCrtdByPersonNameDPEOListName | LIST_NAME | — | — |
| 162 | FdTaxCrtdByPersonNameDPEOMiddleNames | MIDDLE_NAMES | — | — |
| 163 | FdTaxCrtdByPersonNameDPEOMilitaryRank | MILITARY_RANK | — | — |
| 164 | FdTaxCrtdByPersonNameDPEONameType | NAME_TYPE | — | — |
| 165 | FdTaxCrtdByPersonNameDPEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 166 | FdTaxCrtdByPersonNameDPEOObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 167 | FdTaxCrtdByPersonNameDPEOOrderName | ORDER_NAME | — | — |
| 168 | FdTaxCrtdByPersonNameDPEOPersonId2 | PERSON_ID | — | — |
| 169 | FdTaxCrtdByPersonNameDPEOPersonNameId | PERSON_NAME_ID | — | — |
| 170 | FdTaxCrtdByPersonNameDPEOPersonNameId1 | PERSON_NAME_ID | — | — |
| 171 | FdTaxCrtdByPersonNameDPEOPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 172 | FdTaxCrtdByPersonNameDPEOPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 173 | FdTaxCrtdByPersonNameDPEOSuffix | SUFFIX | — | — |
| 174 | FdTaxCrtdByPersonNameDPEOTitle | TITLE | — | — |
| 175 | FdTaxLastUpdByPersonNameDPEOBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 176 | FdTaxLastUpdByPersonNameDPEOCreatedBy3 | CREATED_BY | — | — |
| 177 | FdTaxLastUpdByPersonNameDPEOCreationDate3 | CREATION_DATE | — | — |
| 178 | FdTaxLastUpdByPersonNameDPEODisplayName1 | DISPLAY_NAME | — | — |
| 179 | FdTaxLastUpdByPersonNameDPEOEffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 180 | FdTaxLastUpdByPersonNameDPEOEffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 181 | FdTaxLastUpdByPersonNameDPEOFirstName1 | FIRST_NAME | — | — |
| 182 | FdTaxLastUpdByPersonNameDPEOFullName1 | FULL_NAME | — | ✅ |
| 183 | FdTaxLastUpdByPersonNameDPEOHonors1 | HONORS | — | — |
| 184 | FdTaxLastUpdByPersonNameDPEOKnownAs1 | KNOWN_AS | — | — |
| 185 | FdTaxLastUpdByPersonNameDPEOLastName1 | LAST_NAME | — | — |
| 186 | FdTaxLastUpdByPersonNameDPEOLastUpdateDate3 | LAST_UPDATE_DATE | — | — |
| 187 | FdTaxLastUpdByPersonNameDPEOLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 188 | FdTaxLastUpdByPersonNameDPEOLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 189 | FdTaxLastUpdByPersonNameDPEOLegislationCode1 | LEGISLATION_CODE | — | — |
| 190 | FdTaxLastUpdByPersonNameDPEOListName1 | LIST_NAME | — | — |
| 191 | FdTaxLastUpdByPersonNameDPEOMiddleNames1 | MIDDLE_NAMES | — | — |
| 192 | FdTaxLastUpdByPersonNameDPEOMilitaryRank1 | MILITARY_RANK | — | — |
| 193 | FdTaxLastUpdByPersonNameDPEONameType1 | NAME_TYPE | — | — |
| 194 | FdTaxLastUpdByPersonNameDPEOObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 195 | FdTaxLastUpdByPersonNameDPEOObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 196 | FdTaxLastUpdByPersonNameDPEOOrderName1 | ORDER_NAME | — | — |
| 197 | FdTaxLastUpdByPersonNameDPEOPersonId3 | PERSON_ID | — | — |
| 198 | FdTaxLastUpdByPersonNameDPEOPersonNameId2 | PERSON_NAME_ID | — | — |
| 199 | FdTaxLastUpdByPersonNameDPEOPersonNameId3 | PERSON_NAME_ID | — | — |
| 200 | FdTaxLastUpdByPersonNameDPEOPreNameAdjunct1 | PRE_NAME_ADJUNCT | — | — |
| 201 | FdTaxLastUpdByPersonNameDPEOPreviousLastName1 | PREVIOUS_LAST_NAME | — | — |
| 202 | FdTaxLastUpdByPersonNameDPEOSuffix1 | SUFFIX | — | — |
| 203 | FdTaxLastUpdByPersonNameDPEOTitle1 | TITLE | — | — |
| 204 | LastUpdatedByPersonNameDPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 205 | LastUpdatedByPersonNameDPEOCreatedBy | CREATED_BY | — | — |
| 206 | LastUpdatedByPersonNameDPEOCreationDate | CREATION_DATE | — | — |
| 207 | LastUpdatedByPersonNameDPEODisplayName | DISPLAY_NAME | — | — |
| 208 | LastUpdatedByPersonNameDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 209 | LastUpdatedByPersonNameDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 210 | LastUpdatedByPersonNameDPEOFirstName | FIRST_NAME | — | — |
| 211 | LastUpdatedByPersonNameDPEOFullName | FULL_NAME | — | ✅ |
| 212 | LastUpdatedByPersonNameDPEOHonors | HONORS | — | — |
| 213 | LastUpdatedByPersonNameDPEOKnownAs | KNOWN_AS | — | — |
| 214 | LastUpdatedByPersonNameDPEOLastName | LAST_NAME | — | — |
| 215 | LastUpdatedByPersonNameDPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 216 | LastUpdatedByPersonNameDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 217 | LastUpdatedByPersonNameDPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 218 | LastUpdatedByPersonNameDPEOLegislationCode | LEGISLATION_CODE | — | — |
| 219 | LastUpdatedByPersonNameDPEOListName | LIST_NAME | — | — |
| 220 | LastUpdatedByPersonNameDPEOMiddleNames | MIDDLE_NAMES | — | — |
| 221 | LastUpdatedByPersonNameDPEOMilitaryRank | MILITARY_RANK | — | — |
| 222 | LastUpdatedByPersonNameDPEONameType | NAME_TYPE | — | — |
| 223 | LastUpdatedByPersonNameDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 224 | LastUpdatedByPersonNameDPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 225 | LastUpdatedByPersonNameDPEOOrderName | ORDER_NAME | — | — |
| 226 | LastUpdatedByPersonNameDPEOPersonId | PERSON_ID | — | — |
| 227 | LastUpdatedByPersonNameDPEOPersonNameId | PERSON_NAME_ID | — | — |
| 228 | LastUpdatedByPersonNameDPEOPersonNameId1 | PERSON_NAME_ID | — | — |
| 229 | LastUpdatedByPersonNameDPEOPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 230 | LastUpdatedByPersonNameDPEOPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 231 | LastUpdatedByPersonNameDPEOSuffix | SUFFIX | — | — |
| 232 | LastUpdatedByPersonNameDPEOTitle | TITLE | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedByUserPEOActiveFlag | ACTIVE_FLAG | — | — |
| 2 | CreatedByUserPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | CreatedByUserPEOCreatedBy | CREATED_BY | — | — |
| 4 | CreatedByUserPEOCreationDate | CREATION_DATE | — | — |
| 5 | CreatedByUserPEOCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 6 | CreatedByUserPEOEndDate | END_DATE | — | — |
| 7 | CreatedByUserPEOExternalId | EXTERNAL_ID | — | — |
| 8 | CreatedByUserPEOHrTerminated | HR_TERMINATED | — | — |
| 9 | CreatedByUserPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 10 | CreatedByUserPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | CreatedByUserPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | CreatedByUserPEOMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 13 | CreatedByUserPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | CreatedByUserPEOPartyId | PARTY_ID | — | — |
| 15 | CreatedByUserPEOPersonId | PERSON_ID | — | — |
| 16 | CreatedByUserPEOStartDate | START_DATE | — | — |
| 17 | CreatedByUserPEOSuspended | SUSPENDED | — | — |
| 18 | CreatedByUserPEOUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 19 | CreatedByUserPEOUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 20 | CreatedByUserPEOUserGuid | USER_GUID | — | — |
| 21 | CreatedByUserPEOUserId | USER_ID | — | — |
| 22 | CreatedByUserPEOUsername | USERNAME | — | — |
| 23 | FdHdrExtnCrtdByUserPEOActiveFlag | ACTIVE_FLAG | — | — |
| 24 | FdHdrExtnCrtdByUserPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 25 | FdHdrExtnCrtdByUserPEOCreatedBy | CREATED_BY | — | — |
| 26 | FdHdrExtnCrtdByUserPEOCreationDate | CREATION_DATE | — | — |
| 27 | FdHdrExtnCrtdByUserPEOCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 28 | FdHdrExtnCrtdByUserPEOEndDate | END_DATE | — | — |
| 29 | FdHdrExtnCrtdByUserPEOExternalId | EXTERNAL_ID | — | — |
| 30 | FdHdrExtnCrtdByUserPEOHrTerminated | HR_TERMINATED | — | — |
| 31 | FdHdrExtnCrtdByUserPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 32 | FdHdrExtnCrtdByUserPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | FdHdrExtnCrtdByUserPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 34 | FdHdrExtnCrtdByUserPEOMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 35 | FdHdrExtnCrtdByUserPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 36 | FdHdrExtnCrtdByUserPEOPartyId | PARTY_ID | — | — |
| 37 | FdHdrExtnCrtdByUserPEOPersonId | PERSON_ID | — | — |
| 38 | FdHdrExtnCrtdByUserPEOStartDate | START_DATE | — | — |
| 39 | FdHdrExtnCrtdByUserPEOSuspended | SUSPENDED | — | — |
| 40 | FdHdrExtnCrtdByUserPEOUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 41 | FdHdrExtnCrtdByUserPEOUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 42 | FdHdrExtnCrtdByUserPEOUserGuid | USER_GUID | — | — |
| 43 | FdHdrExtnCrtdByUserPEOUserId | USER_ID | — | — |
| 44 | FdHdrExtnCrtdByUserPEOUsername | USERNAME | — | — |
| 45 | FdHdrExtnLastUpdByUserPEOActiveFlag1 | ACTIVE_FLAG | — | — |
| 46 | FdHdrExtnLastUpdByUserPEOBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 47 | FdHdrExtnLastUpdByUserPEOCreatedBy1 | CREATED_BY | — | — |
| 48 | FdHdrExtnLastUpdByUserPEOCreationDate1 | CREATION_DATE | — | — |
| 49 | FdHdrExtnLastUpdByUserPEOCredentialsEmailSent1 | CREDENTIALS_EMAIL_SENT | — | — |
| 50 | FdHdrExtnLastUpdByUserPEOEndDate1 | END_DATE | — | — |
| 51 | FdHdrExtnLastUpdByUserPEOExternalId1 | EXTERNAL_ID | — | — |
| 52 | FdHdrExtnLastUpdByUserPEOHrTerminated1 | HR_TERMINATED | — | — |
| 53 | FdHdrExtnLastUpdByUserPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 54 | FdHdrExtnLastUpdByUserPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 55 | FdHdrExtnLastUpdByUserPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 56 | FdHdrExtnLastUpdByUserPEOMultitenancyUsername1 | MULTITENANCY_USERNAME | — | — |
| 57 | FdHdrExtnLastUpdByUserPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 58 | FdHdrExtnLastUpdByUserPEOPartyId1 | PARTY_ID | — | — |
| 59 | FdHdrExtnLastUpdByUserPEOPersonId1 | PERSON_ID | — | — |
| 60 | FdHdrExtnLastUpdByUserPEOStartDate1 | START_DATE | — | — |
| 61 | FdHdrExtnLastUpdByUserPEOSuspended1 | SUSPENDED | — | — |
| 62 | FdHdrExtnLastUpdByUserPEOUserDataChecksum1 | USER_DATA_CHECKSUM | — | — |
| 63 | FdHdrExtnLastUpdByUserPEOUserDistinguishedName1 | USER_DISTINGUISHED_NAME | — | — |
| 64 | FdHdrExtnLastUpdByUserPEOUserGuid1 | USER_GUID | — | — |
| 65 | FdHdrExtnLastUpdByUserPEOUserId1 | USER_ID | — | — |
| 66 | FdHdrExtnLastUpdByUserPEOUsername1 | USERNAME | — | — |
| 67 | FdLinesCreatedByUserPEOActiveFlag | ACTIVE_FLAG | — | — |
| 68 | FdLinesCreatedByUserPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 69 | FdLinesCreatedByUserPEOCreatedBy | CREATED_BY | — | — |
| 70 | FdLinesCreatedByUserPEOCreationDate | CREATION_DATE | — | — |
| 71 | FdLinesCreatedByUserPEOCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 72 | FdLinesCreatedByUserPEOEndDate | END_DATE | — | — |
| 73 | FdLinesCreatedByUserPEOExternalId | EXTERNAL_ID | — | — |
| 74 | FdLinesCreatedByUserPEOHrTerminated | HR_TERMINATED | — | — |
| 75 | FdLinesCreatedByUserPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 76 | FdLinesCreatedByUserPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 77 | FdLinesCreatedByUserPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 78 | FdLinesCreatedByUserPEOMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 79 | FdLinesCreatedByUserPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 80 | FdLinesCreatedByUserPEOPartyId | PARTY_ID | — | — |
| 81 | FdLinesCreatedByUserPEOPersonId | PERSON_ID | — | — |
| 82 | FdLinesCreatedByUserPEOStartDate | START_DATE | — | — |
| 83 | FdLinesCreatedByUserPEOSuspended | SUSPENDED | — | — |
| 84 | FdLinesCreatedByUserPEOUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 85 | FdLinesCreatedByUserPEOUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 86 | FdLinesCreatedByUserPEOUserGuid | USER_GUID | — | — |
| 87 | FdLinesCreatedByUserPEOUserId | USER_ID | — | — |
| 88 | FdLinesCreatedByUserPEOUsername | USERNAME | — | — |
| 89 | FdLinesLastUpdByUserPEOActiveFlag1 | ACTIVE_FLAG | — | — |
| 90 | FdLinesLastUpdByUserPEOBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 91 | FdLinesLastUpdByUserPEOCreatedBy1 | CREATED_BY | — | — |
| 92 | FdLinesLastUpdByUserPEOCreationDate1 | CREATION_DATE | — | — |
| 93 | FdLinesLastUpdByUserPEOCredentialsEmailSent1 | CREDENTIALS_EMAIL_SENT | — | — |
| 94 | FdLinesLastUpdByUserPEOEndDate1 | END_DATE | — | — |
| 95 | FdLinesLastUpdByUserPEOExternalId1 | EXTERNAL_ID | — | — |
| 96 | FdLinesLastUpdByUserPEOHrTerminated1 | HR_TERMINATED | — | — |
| 97 | FdLinesLastUpdByUserPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 98 | FdLinesLastUpdByUserPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 99 | FdLinesLastUpdByUserPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 100 | FdLinesLastUpdByUserPEOMultitenancyUsername1 | MULTITENANCY_USERNAME | — | — |
| 101 | FdLinesLastUpdByUserPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 102 | FdLinesLastUpdByUserPEOPartyId1 | PARTY_ID | — | — |
| 103 | FdLinesLastUpdByUserPEOPersonId1 | PERSON_ID | — | — |
| 104 | FdLinesLastUpdByUserPEOStartDate1 | START_DATE | — | — |
| 105 | FdLinesLastUpdByUserPEOSuspended1 | SUSPENDED | — | — |
| 106 | FdLinesLastUpdByUserPEOUserDataChecksum1 | USER_DATA_CHECKSUM | — | — |
| 107 | FdLinesLastUpdByUserPEOUserDistinguishedName1 | USER_DISTINGUISHED_NAME | — | — |
| 108 | FdLinesLastUpdByUserPEOUserGuid1 | USER_GUID | — | — |
| 109 | FdLinesLastUpdByUserPEOUserId1 | USER_ID | — | — |
| 110 | FdLinesLastUpdByUserPEOUsername1 | USERNAME | — | — |
| 111 | FdTaxCreatedByUserPEOActiveFlag | ACTIVE_FLAG | — | — |
| 112 | FdTaxCreatedByUserPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 113 | FdTaxCreatedByUserPEOCreatedBy | CREATED_BY | — | — |
| 114 | FdTaxCreatedByUserPEOCreationDate | CREATION_DATE | — | — |
| 115 | FdTaxCreatedByUserPEOCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 116 | FdTaxCreatedByUserPEOEndDate | END_DATE | — | — |
| 117 | FdTaxCreatedByUserPEOExternalId | EXTERNAL_ID | — | — |
| 118 | FdTaxCreatedByUserPEOHrTerminated | HR_TERMINATED | — | — |
| 119 | FdTaxCreatedByUserPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 120 | FdTaxCreatedByUserPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 121 | FdTaxCreatedByUserPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 122 | FdTaxCreatedByUserPEOMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 123 | FdTaxCreatedByUserPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 124 | FdTaxCreatedByUserPEOPartyId | PARTY_ID | — | — |
| 125 | FdTaxCreatedByUserPEOPersonId | PERSON_ID | — | — |
| 126 | FdTaxCreatedByUserPEOStartDate | START_DATE | — | — |
| 127 | FdTaxCreatedByUserPEOSuspended | SUSPENDED | — | — |
| 128 | FdTaxCreatedByUserPEOUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 129 | FdTaxCreatedByUserPEOUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 130 | FdTaxCreatedByUserPEOUserGuid | USER_GUID | — | — |
| 131 | FdTaxCreatedByUserPEOUserId | USER_ID | — | — |
| 132 | FdTaxCreatedByUserPEOUsername | USERNAME | — | — |
| 133 | FdTaxLastUpdByUserPEOActiveFlag1 | ACTIVE_FLAG | — | — |
| 134 | FdTaxLastUpdByUserPEOBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 135 | FdTaxLastUpdByUserPEOCreatedBy1 | CREATED_BY | — | — |
| 136 | FdTaxLastUpdByUserPEOCreationDate1 | CREATION_DATE | — | — |
| 137 | FdTaxLastUpdByUserPEOCredentialsEmailSent1 | CREDENTIALS_EMAIL_SENT | — | — |
| 138 | FdTaxLastUpdByUserPEOEndDate1 | END_DATE | — | — |
| 139 | FdTaxLastUpdByUserPEOExternalId1 | EXTERNAL_ID | — | — |
| 140 | FdTaxLastUpdByUserPEOHrTerminated1 | HR_TERMINATED | — | — |
| 141 | FdTaxLastUpdByUserPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 142 | FdTaxLastUpdByUserPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 143 | FdTaxLastUpdByUserPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 144 | FdTaxLastUpdByUserPEOMultitenancyUsername1 | MULTITENANCY_USERNAME | — | — |
| 145 | FdTaxLastUpdByUserPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 146 | FdTaxLastUpdByUserPEOPartyId1 | PARTY_ID | — | — |
| 147 | FdTaxLastUpdByUserPEOPersonId1 | PERSON_ID | — | — |
| 148 | FdTaxLastUpdByUserPEOStartDate1 | START_DATE | — | — |
| 149 | FdTaxLastUpdByUserPEOSuspended1 | SUSPENDED | — | — |
| 150 | FdTaxLastUpdByUserPEOUserDataChecksum1 | USER_DATA_CHECKSUM | — | — |
| 151 | FdTaxLastUpdByUserPEOUserDistinguishedName1 | USER_DISTINGUISHED_NAME | — | — |
| 152 | FdTaxLastUpdByUserPEOUserGuid1 | USER_GUID | — | — |
| 153 | FdTaxLastUpdByUserPEOUserId1 | USER_ID | — | — |
| 154 | FdTaxLastUpdByUserPEOUsername1 | USERNAME | — | — |
| 155 | LastUpdatedUserPEOActiveFlag | ACTIVE_FLAG | — | — |
| 156 | LastUpdatedUserPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 157 | LastUpdatedUserPEOCreatedBy | CREATED_BY | — | — |
| 158 | LastUpdatedUserPEOCreationDate | CREATION_DATE | — | — |
| 159 | LastUpdatedUserPEOCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 160 | LastUpdatedUserPEOEndDate | END_DATE | — | — |
| 161 | LastUpdatedUserPEOExternalId | EXTERNAL_ID | — | — |
| 162 | LastUpdatedUserPEOHrTerminated | HR_TERMINATED | — | — |
| 163 | LastUpdatedUserPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 164 | LastUpdatedUserPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 165 | LastUpdatedUserPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 166 | LastUpdatedUserPEOMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 167 | LastUpdatedUserPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 168 | LastUpdatedUserPEOPartyId | PARTY_ID | — | — |
| 169 | LastUpdatedUserPEOPersonId | PERSON_ID | — | — |
| 170 | LastUpdatedUserPEOStartDate | START_DATE | — | — |
| 171 | LastUpdatedUserPEOSuspended | SUSPENDED | — | — |
| 172 | LastUpdatedUserPEOUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 173 | LastUpdatedUserPEOUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 174 | LastUpdatedUserPEOUserGuid | USER_GUID | — | — |
| 175 | LastUpdatedUserPEOUserId | USER_ID | — | — |
| 176 | LastUpdatedUserPEOUsername | USERNAME | — | — |

### [[rcv_shipment_headers|RCV_SHIPMENT_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RcvShipmentHeadersApprovalStatus | APPROVAL_STATUS | — | — |
| 2 | RcvShipmentHeadersAsnStatus | ASN_STATUS | — | — |
| 3 | RcvShipmentHeadersAsnType | ASN_TYPE | — | — |
| 4 | RcvShipmentHeadersBillOfLading | BILL_OF_LADING | — | — |
| 5 | RcvShipmentHeadersCarrierEquipment | CARRIER_EQUIPMENT | — | — |
| 6 | RcvShipmentHeadersCarrierMethod | CARRIER_METHOD | — | — |
| 7 | RcvShipmentHeadersComments | COMMENTS | — | — |
| 8 | RcvShipmentHeadersConversionDate | CONVERSION_DATE | — | — |
| 9 | RcvShipmentHeadersConversionRate | CONVERSION_RATE | — | — |
| 10 | RcvShipmentHeadersConversionRateType | CONVERSION_RATE_TYPE | — | — |
| 11 | RcvShipmentHeadersCreatedBy | CREATED_BY | — | — |
| 12 | RcvShipmentHeadersCreationDate | CREATION_DATE | — | — |
| 13 | RcvShipmentHeadersCurrencyCode | CURRENCY_CODE | — | — |
| 14 | RcvShipmentHeadersCustomerId | CUSTOMER_ID | — | — |
| 15 | RcvShipmentHeadersCustomerSiteId | CUSTOMER_SITE_ID | — | — |
| 16 | RcvShipmentHeadersEdiControlNum | EDI_CONTROL_NUM | — | — |
| 17 | RcvShipmentHeadersEmployeeId | EMPLOYEE_ID | — | — |
| 18 | RcvShipmentHeadersExpectedReceiptDate | EXPECTED_RECEIPT_DATE | — | — |
| 19 | RcvShipmentHeadersFreightAmount | FREIGHT_AMOUNT | — | — |
| 20 | RcvShipmentHeadersFreightBillNumber | FREIGHT_BILL_NUMBER | — | — |
| 21 | RcvShipmentHeadersFreightCarrierId | FREIGHT_CARRIER_ID | — | — |
| 22 | RcvShipmentHeadersFreightTerms | FREIGHT_TERMS | — | — |
| 23 | RcvShipmentHeadersGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 24 | RcvShipmentHeadersGrossWeight | GROSS_WEIGHT | — | — |
| 25 | RcvShipmentHeadersGrossWeightUomCode | GROSS_WEIGHT_UOM_CODE | — | — |
| 26 | RcvShipmentHeadersHazardClass | HAZARD_CLASS | — | — |
| 27 | RcvShipmentHeadersHazardCode | HAZARD_CODE | — | — |
| 28 | RcvShipmentHeadersHazardDescription | HAZARD_DESCRIPTION | — | — |
| 29 | RcvShipmentHeadersHeaderInterfaceId | HEADER_INTERFACE_ID | — | — |
| 30 | RcvShipmentHeadersInvoiceAmount | INVOICE_AMOUNT | — | — |
| 31 | RcvShipmentHeadersInvoiceDate | INVOICE_DATE | — | — |
| 32 | RcvShipmentHeadersInvoiceNum | INVOICE_NUM | — | — |
| 33 | RcvShipmentHeadersInvoiceStatusCode | INVOICE_STATUS_CODE | — | — |
| 34 | RcvShipmentHeadersJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 35 | RcvShipmentHeadersJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 36 | RcvShipmentHeadersLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 37 | RcvShipmentHeadersLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 38 | RcvShipmentHeadersLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 39 | RcvShipmentHeadersLspFlag | LSP_FLAG | — | — |
| 40 | RcvShipmentHeadersNetWeight | NET_WEIGHT | — | — |
| 41 | RcvShipmentHeadersNetWeightUomCode | NET_WEIGHT_UOM_CODE | — | — |
| 42 | RcvShipmentHeadersNoticeCreationDate | NOTICE_CREATION_DATE | — | — |
| 43 | RcvShipmentHeadersNumOfContainers | NUM_OF_CONTAINERS | — | — |
| 44 | RcvShipmentHeadersObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 45 | RcvShipmentHeadersOrganizationId | ORGANIZATION_ID | — | — |
| 46 | RcvShipmentHeadersPackagingCode | PACKAGING_CODE | — | — |
| 47 | RcvShipmentHeadersPackingSlip | PACKING_SLIP | — | — |
| 48 | RcvShipmentHeadersPaymentTermsId | PAYMENT_TERMS_ID | — | — |
| 49 | RcvShipmentHeadersPerformancePeriodFrom | PERFORMANCE_PERIOD_FROM | — | — |
| 50 | RcvShipmentHeadersPerformancePeriodTo | PERFORMANCE_PERIOD_TO | — | — |
| 51 | RcvShipmentHeadersRaDocCreationDate | RA_DOC_CREATION_DATE | — | — |
| 52 | RcvShipmentHeadersRaDocLastUpdateDate | RA_DOC_LAST_UPDATE_DATE | — | — |
| 53 | RcvShipmentHeadersRaDocRevisionDate | RA_DOC_REVISION_DATE | — | — |
| 54 | RcvShipmentHeadersRaDocRevisionNumber | RA_DOC_REVISION_NUMBER | — | — |
| 55 | RcvShipmentHeadersRaDocumentCode | RA_DOCUMENT_CODE | — | — |
| 56 | RcvShipmentHeadersRaDocumentNumber | RA_DOCUMENT_NUMBER | — | — |
| 57 | RcvShipmentHeadersRaDooSourceSystemId | RA_DOO_SOURCE_SYSTEM_ID | — | — |
| 58 | RcvShipmentHeadersRaNoteToReceiver | RA_NOTE_TO_RECEIVER | — | — |
| 59 | RcvShipmentHeadersRaOrigSystemRef | RA_ORIG_SYSTEM_REF | — | — |
| 60 | RcvShipmentHeadersRaOutsourcerContactId | RA_OUTSOURCER_CONTACT_ID | — | — |
| 61 | RcvShipmentHeadersRaOutsourcerPartyId | RA_OUTSOURCER_PARTY_ID | — | — |
| 62 | RcvShipmentHeadersReceiptAdviceNumber | RECEIPT_ADVICE_NUMBER | — | — |
| 63 | RcvShipmentHeadersReceiptNum | RECEIPT_NUM | — | — |
| 64 | RcvShipmentHeadersReceiptSourceCode | RECEIPT_SOURCE_CODE | — | — |
| 65 | RcvShipmentHeadersRemitToSiteId | REMIT_TO_SITE_ID | — | — |
| 66 | RcvShipmentHeadersRequestDate | REQUEST_DATE | — | — |
| 67 | RcvShipmentHeadersRequestId | REQUEST_ID | — | — |
| 68 | RcvShipmentHeadersRmaBuId | RMA_BU_ID | — | — |
| 69 | RcvShipmentHeadersShipFromLocationId | SHIP_FROM_LOCATION_ID | — | — |
| 70 | RcvShipmentHeadersShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 71 | RcvShipmentHeadersShipToOrgId | SHIP_TO_ORG_ID | — | — |
| 72 | RcvShipmentHeadersShipmentHeaderId | SHIPMENT_HEADER_ID | — | — |
| 73 | RcvShipmentHeadersShipmentHeaderId1 | SHIPMENT_HEADER_ID | — | — |
| 74 | RcvShipmentHeadersShipmentNum | SHIPMENT_NUM | — | — |
| 75 | RcvShipmentHeadersShippedDate | SHIPPED_DATE | — | — |
| 76 | RcvShipmentHeadersSpecialHandlingCode | SPECIAL_HANDLING_CODE | — | — |
| 77 | RcvShipmentHeadersTarWeight | TAR_WEIGHT | — | — |
| 78 | RcvShipmentHeadersTarWeightUomCode | TAR_WEIGHT_UOM_CODE | — | — |
| 79 | RcvShipmentHeadersTaxAmount | TAX_AMOUNT | — | — |
| 80 | RcvShipmentHeadersTaxName | TAX_NAME | — | — |
| 81 | RcvShipmentHeadersVendorId | VENDOR_ID | — | — |
| 82 | RcvShipmentHeadersVendorSiteId | VENDOR_SITE_ID | — | — |
| 83 | RcvShipmentHeadersWaybillAirbillNum | WAYBILL_AIRBILL_NUM | — | — |

### [[zx_fc_intended_use_v|ZX_FC_INTENDED_USE_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LineIntendedUsePEOClassificationId | CLASSIFICATION_ID | — | — |
| 2 | LineIntendedUsePEOCode | CODE | — | — |
| 3 | LineIntendedUsePEOCountryCode | COUNTRY_CODE | — | — |
| 4 | LineIntendedUsePEOEffectiveFrom | EFFECTIVE_FROM | — | — |
| 5 | LineIntendedUsePEOEffectiveTo | EFFECTIVE_TO | — | — |
| 6 | LineIntendedUsePEOName | NAME | — | ✅ |

### [[zx_fc_product_categories_v|ZX_FC_PRODUCT_CATEGORIES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProductCategoriesPEOClassificationCode1 | CLASSIFICATION_CODE | — | — |
| 2 | ProductCategoriesPEOClassificationId1 | CLASSIFICATION_ID | — | — |
| 3 | ProductCategoriesPEOClassificationName1 | CLASSIFICATION_NAME | — | ✅ |
| 4 | ProductCategoriesPEOConcatLeafCode | CONCAT_LEAF_CODE | — | — |
| 5 | ProductCategoriesPEOConcatLeafName | CONCAT_LEAF_NAME | — | — |
| 6 | ProductCategoriesPEOCountryCode2 | COUNTRY_CODE | — | — |
| 7 | ProductCategoriesPEOEffectiveFrom2 | EFFECTIVE_FROM | — | — |
| 8 | ProductCategoriesPEOEffectiveTo2 | EFFECTIVE_TO | — | — |

### [[zx_fc_product_fiscal_v|ZX_FC_PRODUCT_FISCAL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProductFiscClassificatnsPEOCategoryId | CATEGORY_ID | — | — |
| 2 | ProductFiscClassificatnsPEOCategorySetId | CATEGORY_SET_ID | — | — |
| 3 | ProductFiscClassificatnsPEOClassificationCode2 | CLASSIFICATION_CODE | — | — |
| 4 | ProductFiscClassificatnsPEOClassificationName2 | CLASSIFICATION_NAME | — | ✅ |
| 5 | ProductFiscClassificatnsPEOCountryCode3 | COUNTRY_CODE | — | — |
| 6 | ProductFiscClassificatnsPEOEffectiveTo3 | EFFECTIVE_TO | — | — |
| 7 | ProductFiscClassificatnsPEOStructureId | STRUCTURE_ID | — | — |
| 8 | ProductFiscClassificatnsPEOStructureName | STRUCTURE_NAME | — | — |

### [[zx_fc_user_defined_v|ZX_FC_USER_DEFINED_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserDefinedFiscClassPEOClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | UserDefinedFiscClassPEOClassificationName | CLASSIFICATION_NAME | — | ✅ |
| 3 | UserDefinedFiscClassPEOCountryCode1 | COUNTRY_CODE | — | — |
| 4 | UserDefinedFiscClassPEOEffectiveFrom1 | EFFECTIVE_FROM | — | — |
| 5 | UserDefinedFiscClassPEOEffectiveTo1 | EFFECTIVE_TO | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
