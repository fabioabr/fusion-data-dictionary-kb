---
id: DOC-OTHER-PVO-FiscalDocumentRcvChargeAllocsP
doc_type: system-doc
title: "FiscalDocumentRcvChargeAllocsP — PVO Cross-Module"
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
  - FiscalDocumentRcvChargeAllocsP
  - fiscaldocumentrcvchargeallocsp
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FiscalDocumentRcvChargeAllocsP

## 📌 Visão Geral

View Object para extração BICC de dados de Fiscal Document Rcv Charge Allocs P. Acessa as tabelas: AP_INVOICES_ALL, AP_PAYMENT_SCHEDULES_ALL, CMF_FD_IN_CONVERT_CFOPS_V (+23).

**Caminho:** `FscmTopModelAM.FiscalDocumentAM.FiscalDocumentRcvChargeAllocsP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 1329 | 26 | 1 | 141 | 11% |

---

## 🔗 Tabelas Relacionadas

- [[ap_invoices_all|AP_INVOICES_ALL]] — 163 atributos
- [[ap_payment_schedules_all|AP_PAYMENT_SCHEDULES_ALL]] — 5 atributos
- [[cmf_fd_in_convert_cfops_v|CMF_FD_IN_CONVERT_CFOPS_V]] — 2 atributos (2 BICC)
- [[cmf_fd_loc_info_persist_otbi_v|CMF_FD_LOC_INFO_PERSIST_OTBI_V]] — 79 atributos (12 BICC)
- [[cmf_fd_out_origin_cfops_v|CMF_FD_OUT_ORIGIN_CFOPS_V]] — 2 atributos (2 BICC)
- [[cmf_fiscal_doc_headers|CMF_FISCAL_DOC_HEADERS]] — 60 atributos (21 BICC)
- [[cmf_fiscal_doc_inv_org_v|CMF_FISCAL_DOC_INV_ORG_V]] — 5 atributos
- [[cmf_fiscal_doc_lines_vl|CMF_FISCAL_DOC_LINES_VL]] — 47 atributos (15 BICC)
- [[cmf_fiscal_proc_options|CMF_FISCAL_PROC_OPTIONS]] — 56 atributos
- [[cmf_rcv_charge_allocs|CMF_RCV_CHARGE_ALLOCS]] — 34 atributos (1 PKs, 18 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 42 atributos
- [[gl_ledgers|GL_LEDGERS]] — 86 atributos
- [[inv_cons_advice_headers|INV_CONS_ADVICE_HEADERS]] — 24 atributos
- [[inv_units_of_measure_vl|INV_UNITS_OF_MEASURE_VL]] — 41 atributos
- [[jg_fscl_hdrs_atrb_ext_all|JG_FSCL_HDRS_ATRB_EXT_ALL]] — 55 atributos (32 BICC)
- [[jg_fscl_hdr_dtls_atrb_ext_all|JG_FSCL_HDR_DTLS_ATRB_EXT_ALL]] — 18 atributos
- [[jg_fscl_lines_atrb_ext_all|JG_FSCL_LINES_ATRB_EXT_ALL]] — 23 atributos (5 BICC)
- [[jg_fscl_ln_dtls_atrb_ext_all|JG_FSCL_LN_DTLS_ATRB_EXT_ALL]] — 20 atributos
- [[jg_fscl_tax_lines_all|JG_FSCL_TAX_LINES_ALL]] — 72 atributos (22 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 210 atributos (8 BICC)
- [[per_users|PER_USERS]] — 176 atributos
- [[rcv_shipment_headers|RCV_SHIPMENT_HEADERS]] — 82 atributos
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
| 1 | FiscalDocLocInfoPersistPEODocumentHeaderId2 | DOCUMENT_HEADER_ID | — | — |
| 2 | FiscalDocLocInfoPersistPEODocumentNumber1 | DOCUMENT_NUMBER | — | — |
| 3 | FiscalDocLocInfoPersistPEOFiscalProcOptionsId1 | FISCAL_PROC_OPTIONS_ID | — | — |
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
| 3 | FiscalDocHeadersPEOBillToBusinessUnitId1 | BILL_TO_BUSINESS_UNIT_ID | — | — |
| 4 | FiscalDocHeadersPEOChargeAllocationStatus | CHARGE_ALLOCATION_STATUS | — | ✅ |
| 5 | FiscalDocHeadersPEOCmrInterfacedFlag | CMR_INTERFACED_FLAG | — | ✅ |
| 6 | FiscalDocHeadersPEOConversionRate | CONVERSION_RATE | — | — |
| 7 | FiscalDocHeadersPEOConverstionType | CONVERSTION_TYPE | — | — |
| 8 | FiscalDocHeadersPEOCountryCode | COUNTRY_CODE | — | ✅ |
| 9 | FiscalDocHeadersPEOCreatedBy2 | CREATED_BY | — | — |
| 10 | FiscalDocHeadersPEOCreationDate2 | CREATION_DATE | — | ✅ |
| 11 | FiscalDocHeadersPEOCurrency | CURRENCY | — | ✅ |
| 12 | FiscalDocHeadersPEODocumentHeaderId1 | DOCUMENT_HEADER_ID | — | ✅ |
| 13 | FiscalDocHeadersPEODocumentNumber | DOCUMENT_NUMBER | — | ✅ |
| 14 | FiscalDocHeadersPEODocumentStatus | DOCUMENT_STATUS | — | ✅ |
| 15 | FiscalDocHeadersPEODocumentType | DOCUMENT_TYPE | — | — |
| 16 | FiscalDocHeadersPEOExternalSystemRefId1 | EXTERNAL_SYSTEM_REF_ID | — | — |
| 17 | FiscalDocHeadersPEOExternalSystemReference1 | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 18 | FiscalDocHeadersPEOFiscalDocAssoctnsId | FISCAL_DOC_ASSOCTNS_ID | — | — |
| 19 | FiscalDocHeadersPEOFiscalProcOptionsId | FISCAL_PROC_OPTIONS_ID | — | — |
| 20 | FiscalDocHeadersPEOInterfacedFlag | INTERFACED_FLAG | — | — |
| 21 | FiscalDocHeadersPEOInvoiceInterfacedFlag | INVOICE_INTERFACED_FLAG | — | ✅ |
| 22 | FiscalDocHeadersPEOIssueDate | ISSUE_DATE | — | ✅ |
| 23 | FiscalDocHeadersPEOIssuerLocationId | ISSUER_LOCATION_ID | — | — |
| 24 | FiscalDocHeadersPEOIssuerPartyId | ISSUER_PARTY_ID | — | — |
| 25 | FiscalDocHeadersPEOIssuerPartySiteId | ISSUER_PARTY_SITE_ID | — | — |
| 26 | FiscalDocHeadersPEOIssuerTaxId | ISSUER_TAX_ID | — | — |
| 27 | FiscalDocHeadersPEOItemLineAmount | ITEM_LINE_AMOUNT | — | ✅ |
| 28 | FiscalDocHeadersPEOJobDefinitionName2 | JOB_DEFINITION_NAME | — | — |
| 29 | FiscalDocHeadersPEOJobDefinitionPackage2 | JOB_DEFINITION_PACKAGE | — | — |
| 30 | FiscalDocHeadersPEOLastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 31 | FiscalDocHeadersPEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 32 | FiscalDocHeadersPEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 33 | FiscalDocHeadersPEOModel | MODEL | — | ✅ |
| 34 | FiscalDocHeadersPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 35 | FiscalDocHeadersPEOOperationType | OPERATION_TYPE | — | — |
| 36 | FiscalDocHeadersPEOParentDocumentHeaderId | PARENT_DOCUMENT_HEADER_ID | — | — |
| 37 | FiscalDocHeadersPEOReason | REASON | — | — |
| 38 | FiscalDocHeadersPEOReceiverLocationId | RECEIVER_LOCATION_ID | — | — |
| 39 | FiscalDocHeadersPEOReceiverPartyId | RECEIVER_PARTY_ID | — | — |
| 40 | FiscalDocHeadersPEOReceiverPartySiteId | RECEIVER_PARTY_SITE_ID | — | — |
| 41 | FiscalDocHeadersPEOReceiverTaxId | RECEIVER_TAX_ID | — | — |
| 42 | FiscalDocHeadersPEOReferencedStatus | REFERENCED_STATUS | — | ✅ |
| 43 | FiscalDocHeadersPEORequestId2 | REQUEST_ID | — | — |
| 44 | FiscalDocHeadersPEOSchedulesAllocatedFlag | SCHEDULES_ALLOCATED_FLAG | — | ✅ |
| 45 | FiscalDocHeadersPEOSeries | SERIES | — | ✅ |
| 46 | FiscalDocHeadersPEOShipfromLocationId | SHIPFROM_LOCATION_ID | — | — |
| 47 | FiscalDocHeadersPEOShipfromPartyId | SHIPFROM_PARTY_ID | — | — |
| 48 | FiscalDocHeadersPEOShipfromPartySiteId | SHIPFROM_PARTY_SITE_ID | — | — |
| 49 | FiscalDocHeadersPEOShipfromTaxId | SHIPFROM_TAX_ID | — | — |
| 50 | FiscalDocHeadersPEOShiptoLocationId | SHIPTO_LOCATION_ID | — | — |
| 51 | FiscalDocHeadersPEOShiptoPartyId | SHIPTO_PARTY_ID | — | — |
| 52 | FiscalDocHeadersPEOShiptoPartySiteId | SHIPTO_PARTY_SITE_ID | — | — |
| 53 | FiscalDocHeadersPEOShiptoTaxId | SHIPTO_TAX_ID | — | — |
| 54 | FiscalDocHeadersPEOSoldToLegalEntityId | SOLD_TO_LEGAL_ENTITY_ID | — | — |
| 55 | FiscalDocHeadersPEOSourceDocumentType1 | SOURCE_DOCUMENT_TYPE | — | — |
| 56 | FiscalDocHeadersPEOSourceRefDocHeaderId | SOURCE_REF_DOC_HEADER_ID | — | — |
| 57 | FiscalDocHeadersPEOSubseries | SUBSERIES | — | ✅ |
| 58 | FiscalDocHeadersPEOTaxCalculationStatus | TAX_CALCULATION_STATUS | — | ✅ |
| 59 | FiscalDocHeadersPEOTotalAmount | TOTAL_AMOUNT | — | ✅ |
| 60 | FiscalDocHeadersPEOValidationStatus | VALIDATION_STATUS | — | — |

### [[cmf_fiscal_doc_inv_org_v|CMF_FISCAL_DOC_INV_ORG_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocInvOrgPEODestInventoryOrgId | DEST_INVENTORY_ORG_ID | — | — |
| 2 | FiscalDocInvOrgPEOFiscalDocHeaderId1 | FISCAL_DOC_HEADER_ID | — | — |
| 3 | FiscalDocInvOrgPEOFiscalDocLineId1 | FISCAL_DOC_LINE_ID | — | — |
| 4 | FiscalDocInvOrgPEOSourceDocType | SOURCE_DOC_TYPE | — | — |
| 5 | FiscalDocInvOrgPEOSrcInventoryOrgId | SRC_INVENTORY_ORG_ID | — | — |

### [[cmf_fiscal_doc_lines_vl|CMF_FISCAL_DOC_LINES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocumentLinesPEOChargesAmount | CHARGES_AMOUNT | — | — |
| 2 | FiscalDocumentLinesPEOCreatedBy1 | CREATED_BY | — | — |
| 3 | FiscalDocumentLinesPEOCreationDate1 | CREATION_DATE | — | — |
| 4 | FiscalDocumentLinesPEODistCodeCombinationId | DIST_CODE_COMBINATION_ID | — | — |
| 5 | FiscalDocumentLinesPEODocumentHeaderId | DOCUMENT_HEADER_ID | — | — |
| 6 | FiscalDocumentLinesPEODocumentLineId | DOCUMENT_LINE_ID | — | — |
| 7 | FiscalDocumentLinesPEOEfdItemCode | EFD_ITEM_CODE | — | ✅ |
| 8 | FiscalDocumentLinesPEOEfdItemDescription | EFD_ITEM_DESCRIPTION | — | ✅ |
| 9 | FiscalDocumentLinesPEOEfdProdAddInfo | EFD_PROD_ADD_INFO | — | ✅ |
| 10 | FiscalDocumentLinesPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | — |
| 11 | FiscalDocumentLinesPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 12 | FiscalDocumentLinesPEOFciControlNumber | FCI_CONTROL_NUMBER | — | — |
| 13 | FiscalDocumentLinesPEOFdAmount | FD_AMOUNT | — | ✅ |
| 14 | FiscalDocumentLinesPEOFdConvertedCfop | FD_CONVERTED_CFOP | — | — |
| 15 | FiscalDocumentLinesPEOFdOriginalCfop | FD_ORIGINAL_CFOP | — | — |
| 16 | FiscalDocumentLinesPEOFdPrice | FD_PRICE | — | ✅ |
| 17 | FiscalDocumentLinesPEOFdQuantity | FD_QUANTITY | — | ✅ |
| 18 | FiscalDocumentLinesPEOFdUom | FD_UOM | — | ✅ |
| 19 | FiscalDocumentLinesPEOFiscalClassification | FISCAL_CLASSIFICATION | — | — |
| 20 | FiscalDocumentLinesPEOFreightModal | FREIGHT_MODAL | — | — |
| 21 | FiscalDocumentLinesPEOIntendedUseId | INTENDED_USE_ID | — | — |
| 22 | FiscalDocumentLinesPEOItemDescription | ITEM_DESCRIPTION | — | — |
| 23 | FiscalDocumentLinesPEOItemId | ITEM_ID | — | — |
| 24 | FiscalDocumentLinesPEOJobDefinitionName1 | JOB_DEFINITION_NAME | — | — |
| 25 | FiscalDocumentLinesPEOJobDefinitionPackage1 | JOB_DEFINITION_PACKAGE | — | — |
| 26 | FiscalDocumentLinesPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 27 | FiscalDocumentLinesPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 28 | FiscalDocumentLinesPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 29 | FiscalDocumentLinesPEOLineNumber | LINE_NUMBER | — | ✅ |
| 30 | FiscalDocumentLinesPEOLineStatus | LINE_STATUS | — | ✅ |
| 31 | FiscalDocumentLinesPEOLineType | LINE_TYPE | — | ✅ |
| 32 | FiscalDocumentLinesPEONonRecoverableTax | NON_RECOVERABLE_TAX | — | — |
| 33 | FiscalDocumentLinesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 34 | FiscalDocumentLinesPEOPhysicalReceiptDate | PHYSICAL_RECEIPT_DATE | — | ✅ |
| 35 | FiscalDocumentLinesPEOPhysicalReceiptQuantity | PHYSICAL_RECEIPT_QUANTITY | — | ✅ |
| 36 | FiscalDocumentLinesPEOPhysicalReceiptUom | PHYSICAL_RECEIPT_UOM | — | ✅ |
| 37 | FiscalDocumentLinesPEOProductCategory | PRODUCT_CATEGORY | — | — |
| 38 | FiscalDocumentLinesPEOProductFiscalClassifId | PRODUCT_FISCAL_CLASSIF_ID | — | — |
| 39 | FiscalDocumentLinesPEORecoverablesTax | RECOVERABLES_TAX | — | — |
| 40 | FiscalDocumentLinesPEORefDocumentHeaderId | REF_DOCUMENT_HEADER_ID | — | — |
| 41 | FiscalDocumentLinesPEORefDocumentLineId | REF_DOCUMENT_LINE_ID | — | — |
| 42 | FiscalDocumentLinesPEORefFdDocumentType | REF_FD_DOCUMENT_TYPE | — | — |
| 43 | FiscalDocumentLinesPEOReqBuId1 | REQ_BU_ID | — | — |
| 44 | FiscalDocumentLinesPEORequestId1 | REQUEST_ID | — | — |
| 45 | FiscalDocumentLinesPEOScheduleSrcDocType | SCHEDULE_SRC_DOC_TYPE | — | — |
| 46 | FiscalDocumentLinesPEOSourceDocBuId | SOURCE_DOC_BU_ID | — | — |
| 47 | FiscalDocumentLinesPEOSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | ✅ |

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

### [[cmf_rcv_charge_allocs|CMF_RCV_CHARGE_ALLOCS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocumentRcvChargeAlloc1ActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | FiscalDocumentRcvChargeAlloc1BillToBusinessUnitId | BILL_TO_BUSINESS_UNIT_ID | — | — |
| 3 | FiscalDocumentRcvChargeAlloc1ChargeId | CHARGE_ID | — | — |
| 4 | FiscalDocumentRcvChargeAlloc1CmrPoLineLocationId | CMR_PO_LINE_LOCATION_ID | — | — |
| 5 | FiscalDocumentRcvChargeAlloc1CmrRcvTransactionId | CMR_RCV_TRANSACTION_ID | — | — |
| 6 | FiscalDocumentRcvChargeAlloc1CreatedBy | CREATED_BY | — | — |
| 7 | FiscalDocumentRcvChargeAlloc1CreationDate | CREATION_DATE | — | — |
| 8 | FiscalDocumentRcvChargeAlloc1CurrencyCode | CURRENCY_CODE | — | ✅ |
| 9 | FiscalDocumentRcvChargeAlloc1CurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 10 | FiscalDocumentRcvChargeAlloc1CurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 11 | FiscalDocumentRcvChargeAlloc1CurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 12 | FiscalDocumentRcvChargeAlloc1EffectiveDate | EFFECTIVE_DATE | — | ✅ |
| 13 | FiscalDocumentRcvChargeAlloc1FiscalDocHeaderId | FISCAL_DOC_HEADER_ID | — | — |
| 14 | FiscalDocumentRcvChargeAlloc1FiscalDocLineId | FISCAL_DOC_LINE_ID | — | — |
| 15 | FiscalDocumentRcvChargeAlloc1FiscalDocLineNum | FISCAL_DOC_LINE_NUM | — | ✅ |
| 16 | FiscalDocumentRcvChargeAlloc1IntercompanyBillToBuId | INTERCOMPANY_BILL_TO_BU_ID | — | — |
| 17 | FiscalDocumentRcvChargeAlloc1IntercompanyProcessedFlag | INTERCOMPANY_PROCESSED_FLAG | — | ✅ |
| 18 | FiscalDocumentRcvChargeAlloc1JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 19 | FiscalDocumentRcvChargeAlloc1JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 20 | FiscalDocumentRcvChargeAlloc1LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 21 | FiscalDocumentRcvChargeAlloc1LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 22 | FiscalDocumentRcvChargeAlloc1LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 23 | FiscalDocumentRcvChargeAlloc1MatReqBuFuncCurrencyCode | MAT_REQ_BU_FUNC_CURRENCY_CODE | — | ✅ |
| 24 | FiscalDocumentRcvChargeAlloc1PreprocessStatus | PREPROCESS_STATUS | — | ✅ |
| 25 | FiscalDocumentRcvChargeAlloc1PrimaryUomConvFactor | PRIMARY_UOM_CONV_FACTOR | — | ✅ |
| 26 | FiscalDocumentRcvChargeAlloc1ProcessedByCaFlag | PROCESSED_BY_CA_FLAG | — | ✅ |
| 27 | FiscalDocumentRcvChargeAlloc1ProcessedByRaFlag | PROCESSED_BY_RA_FLAG | — | ✅ |
| 28 | FiscalDocumentRcvChargeAlloc1ReqBuId | REQ_BU_ID | — | — |
| 29 | FiscalDocumentRcvChargeAlloc1RequestId | REQUEST_ID | — | — |
| 30 | FiscalDocumentRcvChargeAlloc1ServicePoFlag | SERVICE_PO_FLAG | — | ✅ |
| 31 | FiscalDocumentRcvChargeAlloc1SourceDocUomCode | SOURCE_DOC_UOM_CODE | — | ✅ |
| 32 | FiscalDocumentRcvChargeAlloc1UnitAmount | UNIT_AMOUNT | — | ✅ |
| 33 | FiscalDocumentRcvChargeAlloc1UnitTax | UNIT_TAX | — | ✅ |
| 34 | RcvChargeAllocId | RCV_CHARGE_ALLOC_ID | 🔑 | ✅ |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOBusinessUnitId | BU_ID | — | — |
| 2 | BusinessUnitPEOCreatedBy7 | CREATED_BY | — | — |
| 3 | BusinessUnitPEOCreationDate7 | CREATION_DATE | — | — |
| 4 | BusinessUnitPEODateFrom | DATE_FROM | — | — |
| 5 | BusinessUnitPEODateTo | DATE_TO | — | — |
| 6 | BusinessUnitPEODefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | — |
| 7 | BusinessUnitPEODefaultSetId | DEFAULT_SET_ID | — | — |
| 8 | BusinessUnitPEOEnabledForHrFlag | ENABLED_FOR_HR_FLAG | — | — |
| 9 | BusinessUnitPEOEnterpriseId | BUSINESS_GROUP_ID | — | — |
| 10 | BusinessUnitPEOFinancialsBusinessUnitId | FIN_BUSINESS_UNIT_ID | — | — |
| 11 | BusinessUnitPEOLastUpdateDate7 | LAST_UPDATE_DATE | — | — |
| 12 | BusinessUnitPEOLastUpdateLogin7 | LAST_UPDATE_LOGIN | — | — |
| 13 | BusinessUnitPEOLastUpdatedBy7 | LAST_UPDATED_BY | — | — |
| 14 | BusinessUnitPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 15 | BusinessUnitPEOLocationId | LOCATION_ID | — | — |
| 16 | BusinessUnitPEOManagerId | MANAGER_ID | — | — |
| 17 | BusinessUnitPEOName | BU_NAME | — | — |
| 18 | BusinessUnitPEOPrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |
| 19 | BusinessUnitPEOProfitCenterFlag | PROFIT_CENTER_FLAG | — | — |
| 20 | BusinessUnitPEOShortCode | SHORT_CODE | — | — |
| 21 | BusinessUnitPEOStatus | STATUS | — | — |
| 22 | HdrBusinessUnitPEOBusinessUnitId | BU_ID | — | — |
| 23 | HdrBusinessUnitPEOCreatedBy | CREATED_BY | — | — |
| 24 | HdrBusinessUnitPEOCreationDate | CREATION_DATE | — | — |
| 25 | HdrBusinessUnitPEODateFrom | DATE_FROM | — | — |
| 26 | HdrBusinessUnitPEODateTo | DATE_TO | — | — |
| 27 | HdrBusinessUnitPEODefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | — |
| 28 | HdrBusinessUnitPEODefaultSetId | DEFAULT_SET_ID | — | — |
| 29 | HdrBusinessUnitPEOEnabledForHrFlag | ENABLED_FOR_HR_FLAG | — | — |
| 30 | HdrBusinessUnitPEOEnterpriseId | BUSINESS_GROUP_ID | — | — |
| 31 | HdrBusinessUnitPEOFinancialsBusinessUnitId | FIN_BUSINESS_UNIT_ID | — | — |
| 32 | HdrBusinessUnitPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 33 | HdrBusinessUnitPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 34 | HdrBusinessUnitPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 35 | HdrBusinessUnitPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 36 | HdrBusinessUnitPEOLocationId | LOCATION_ID | — | — |
| 37 | HdrBusinessUnitPEOManagerId | MANAGER_ID | — | — |
| 38 | HdrBusinessUnitPEOName | BU_NAME | — | — |
| 39 | HdrBusinessUnitPEOPrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |
| 40 | HdrBusinessUnitPEOProfitCenterFlag | PROFIT_CENTER_FLAG | — | — |
| 41 | HdrBusinessUnitPEOShortCode | SHORT_CODE | — | — |
| 42 | HdrBusinessUnitPEOStatus | STATUS | — | — |

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

### [[inv_cons_advice_headers|INV_CONS_ADVICE_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConsumptionAdviceHeaderPEOAgreementHeaderId | AGREEMENT_HEADER_ID | — | — |
| 2 | ConsumptionAdviceHeaderPEOBpaRevisionNum | BPA_REVISION_NUM | — | — |
| 3 | ConsumptionAdviceHeaderPEOBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 4 | ConsumptionAdviceHeaderPEOConsumptionDate | CONSUMPTION_DATE | — | — |
| 5 | ConsumptionAdviceHeaderPEOConsumptionHeaderId | CONSUMPTION_HEADER_ID | — | — |
| 6 | ConsumptionAdviceHeaderPEOConsumptionNumber | CONSUMPTION_NUMBER | — | — |
| 7 | ConsumptionAdviceHeaderPEOCreatedBy1 | CREATED_BY | — | — |
| 8 | ConsumptionAdviceHeaderPEOCreationDate1 | CREATION_DATE | — | — |
| 9 | ConsumptionAdviceHeaderPEOEndCycleDate | END_CYCLE_DATE | — | — |
| 10 | ConsumptionAdviceHeaderPEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 11 | ConsumptionAdviceHeaderPEOJobDefinitionName1 | JOB_DEFINITION_NAME | — | — |
| 12 | ConsumptionAdviceHeaderPEOJobDefinitionPackage1 | JOB_DEFINITION_PACKAGE | — | — |
| 13 | ConsumptionAdviceHeaderPEOLastDateRevised | LAST_DATE_REVISED | — | — |
| 14 | ConsumptionAdviceHeaderPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 15 | ConsumptionAdviceHeaderPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 16 | ConsumptionAdviceHeaderPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 17 | ConsumptionAdviceHeaderPEOLatestRevisionNumber | LATEST_REVISION_NUMBER | — | — |
| 18 | ConsumptionAdviceHeaderPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 19 | ConsumptionAdviceHeaderPEOLotSerialDisplayFlag | LOT_SERIAL_DISPLAY_FLAG | — | — |
| 20 | ConsumptionAdviceHeaderPEONeedPublishing | NEED_PUBLISHING | — | — |
| 21 | ConsumptionAdviceHeaderPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 22 | ConsumptionAdviceHeaderPEOOwningEntityId | OWNING_ENTITY_ID | — | — |
| 23 | ConsumptionAdviceHeaderPEORequestId1 | REQUEST_ID | — | — |
| 24 | ConsumptionAdviceHeaderPEOStartCycleDate | START_CYCLE_DATE | — | — |

### [[inv_units_of_measure_vl|INV_UNITS_OF_MEASURE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LinesUnitOfMeasurePEO1AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | LinesUnitOfMeasurePEO1BaseUomFlag | BASE_UOM_FLAG | — | — |
| 3 | LinesUnitOfMeasurePEO1CreatedBy | CREATED_BY | — | — |
| 4 | LinesUnitOfMeasurePEO1CreationDate | CREATION_DATE | — | — |
| 5 | LinesUnitOfMeasurePEO1Description | DESCRIPTION | — | — |
| 6 | LinesUnitOfMeasurePEO1DisableDate | DISABLE_DATE | — | — |
| 7 | LinesUnitOfMeasurePEO1HasGeneratedCode | HAS_GENERATED_CODE | — | — |
| 8 | LinesUnitOfMeasurePEO1JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 9 | LinesUnitOfMeasurePEO1JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 10 | LinesUnitOfMeasurePEO1LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 11 | LinesUnitOfMeasurePEO1LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | LinesUnitOfMeasurePEO1LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | LinesUnitOfMeasurePEO1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | LinesUnitOfMeasurePEO1RequestId | REQUEST_ID | — | — |
| 15 | LinesUnitOfMeasurePEO1StandardPackFlag | STANDARD_PACK_FLAG | — | — |
| 16 | LinesUnitOfMeasurePEO1UnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 17 | LinesUnitOfMeasurePEO1UnitOfMeasureId | UNIT_OF_MEASURE_ID | — | — |
| 18 | LinesUnitOfMeasurePEO1UomClass | UOM_CLASS | — | — |
| 19 | LinesUnitOfMeasurePEO1UomCode | UOM_CODE | — | — |
| 20 | LinesUnitOfMeasurePEO1UomPluralDesc | UOM_PLURAL_DESC | — | — |
| 21 | LinesUnitOfMeasurePEO1UomReciprocalDesc | UOM_RECIPROCAL_DESC | — | — |
| 22 | UnitOfMeasurePEOBaseUomFlag | BASE_UOM_FLAG | — | — |
| 23 | UnitOfMeasurePEOCreatedBy8 | CREATED_BY | — | — |
| 24 | UnitOfMeasurePEOCreationDate8 | CREATION_DATE | — | — |
| 25 | UnitOfMeasurePEODescription | DESCRIPTION | — | — |
| 26 | UnitOfMeasurePEODisableDate | DISABLE_DATE | — | — |
| 27 | UnitOfMeasurePEOHasGeneratedCode | HAS_GENERATED_CODE | — | — |
| 28 | UnitOfMeasurePEOJobDefinitionName7 | JOB_DEFINITION_NAME | — | — |
| 29 | UnitOfMeasurePEOJobDefinitionPackage7 | JOB_DEFINITION_PACKAGE | — | — |
| 30 | UnitOfMeasurePEOLastUpdateDate8 | LAST_UPDATE_DATE | — | — |
| 31 | UnitOfMeasurePEOLastUpdateLogin8 | LAST_UPDATE_LOGIN | — | — |
| 32 | UnitOfMeasurePEOLastUpdatedBy8 | LAST_UPDATED_BY | — | — |
| 33 | UnitOfMeasurePEOObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |
| 34 | UnitOfMeasurePEORequestId7 | REQUEST_ID | — | — |
| 35 | UnitOfMeasurePEOStandardPackFlag | STANDARD_PACK_FLAG | — | — |
| 36 | UnitOfMeasurePEOUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 37 | UnitOfMeasurePEOUnitOfMeasureId | UNIT_OF_MEASURE_ID | — | — |
| 38 | UnitOfMeasurePEOUomClass | UOM_CLASS | — | — |
| 39 | UnitOfMeasurePEOUomCode | UOM_CODE | — | — |
| 40 | UnitOfMeasurePEOUomPluralDesc | UOM_PLURAL_DESC | — | — |
| 41 | UnitOfMeasurePEOUomReciprocalDesc | UOM_RECIPROCAL_DESC | — | — |

### [[jg_fscl_hdrs_atrb_ext_all|JG_FSCL_HDRS_ATRB_EXT_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocHeaderExtnEOApplicationId | APPLICATION_ID | — | — |
| 2 | FiscalDocHeaderExtnEOCommitmentStatementIdent | COMMITMENT_STATEMENT_IDENT | — | — |
| 3 | FiscalDocHeaderExtnEOContainerIdentifier | CONTAINER_IDENTIFIER | — | ✅ |
| 4 | FiscalDocHeaderExtnEOContingencyType | CONTINGENCY_TYPE | — | ✅ |
| 5 | FiscalDocHeaderExtnEOCreatedBy3 | CREATED_BY | — | — |
| 6 | FiscalDocHeaderExtnEOCreationDate3 | CREATION_DATE | — | — |
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
| 19 | FiscalDocHeaderExtnEOJobDefinitionName3 | JOB_DEFINITION_NAME | — | — |
| 20 | FiscalDocHeaderExtnEOJobDefinitionPackage3 | JOB_DEFINITION_PACKAGE | — | — |
| 21 | FiscalDocHeaderExtnEOLastUpdateDate3 | LAST_UPDATE_DATE | — | ✅ |
| 22 | FiscalDocHeaderExtnEOLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 23 | FiscalDocHeaderExtnEOLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 24 | FiscalDocHeaderExtnEOLegalReportingUnitId | LEGAL_REPORTING_UNIT_ID | — | — |
| 25 | FiscalDocHeaderExtnEOMatIssueRecptDate | MAT_ISSUE_RECPT_DATE | — | — |
| 26 | FiscalDocHeaderExtnEOMatIssueRecptHour | MAT_ISSUE_RECPT_HOUR | — | ✅ |
| 27 | FiscalDocHeaderExtnEONetWeight | NET_WEIGHT | — | ✅ |
| 28 | FiscalDocHeaderExtnEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 29 | FiscalDocHeaderExtnEOOrgId | ORG_ID | — | — |
| 30 | FiscalDocHeaderExtnEOPaymentOption | PAYMENT_OPTION | — | — |
| 31 | FiscalDocHeaderExtnEOPurchaseContract | PURCHASE_CONTRACT | — | ✅ |
| 32 | FiscalDocHeaderExtnEOQuantityCarried | QUANTITY_CARRIED | — | ✅ |
| 33 | FiscalDocHeaderExtnEORefComplementaryFdFlag | REF_COMPLEMENTARY_FD_FLAG | — | ✅ |
| 34 | FiscalDocHeaderExtnEORefDocIssuerStateCode | REF_DOC_ISSUER_STATE_CODE | — | ✅ |
| 35 | FiscalDocHeaderExtnEORefDocNum | REF_DOC_NUM | — | ✅ |
| 36 | FiscalDocHeaderExtnEORefFiscalDocDate | REF_FISCAL_DOC_DATE | — | ✅ |
| 37 | FiscalDocHeaderExtnEORefFiscalDocKey | REF_FISCAL_DOC_KEY | — | ✅ |
| 38 | FiscalDocHeaderExtnEORefIssuerTaxpayerId | REF_ISSUER_TAXPAYER_ID | — | ✅ |
| 39 | FiscalDocHeaderExtnEORefModel | REF_MODEL | — | ✅ |
| 40 | FiscalDocHeaderExtnEORefRuralFlag | REF_RURAL_FLAG | — | ✅ |
| 41 | FiscalDocHeaderExtnEORefSeries | REF_SERIES | — | ✅ |
| 42 | FiscalDocHeaderExtnEORequestId3 | REQUEST_ID | — | — |
| 43 | FiscalDocHeaderExtnEOSealNumber | SEAL_NUMBER | — | ✅ |
| 44 | FiscalDocHeaderExtnEOSeries1 | SERIES | — | ✅ |
| 45 | FiscalDocHeaderExtnEOServiceSeries | SERVICE_SERIES | — | ✅ |
| 46 | FiscalDocHeaderExtnEOServiceSituation | SERVICE_SITUATION | — | ✅ |
| 47 | FiscalDocHeaderExtnEOServiceTaxPaidFlag | SERVICE_TAX_PAID_FLAG | — | — |
| 48 | FiscalDocHeaderExtnEOServiceType | SERVICE_TYPE | — | ✅ |
| 49 | FiscalDocHeaderExtnEOTaxSettlementDate | TAX_SETTLEMENT_DATE | — | — |
| 50 | FiscalDocHeaderExtnEOTrxFdTypeDeterminant | TRX_FD_TYPE_DETERMINANT | — | ✅ |
| 51 | FiscalDocHeaderExtnEOTrxId | TRX_ID | — | — |
| 52 | FiscalDocHeaderExtnEOTrxNumber | TRX_NUMBER | — | ✅ |
| 53 | FiscalDocHeaderExtnEOWagonIdentification | WAGON_IDENTIFICATION | — | ✅ |
| 54 | FiscalDocHeaderExtnEOWhtSocialIntgProgAmt | WHT_SOCIAL_INTG_PROG_AMT | — | — |
| 55 | FiscalDocHeaderExtnEOWhtSsFinancingAmt | WHT_SS_FINANCING_AMT | — | — |

### [[jg_fscl_hdr_dtls_atrb_ext_all|JG_FSCL_HDR_DTLS_ATRB_EXT_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocHeaderDetailExtnEOApplicationId1 | APPLICATION_ID | — | — |
| 2 | FiscalDocHeaderDetailExtnEOCreatedBy4 | CREATED_BY | — | — |
| 3 | FiscalDocHeaderDetailExtnEOCreationDate4 | CREATION_DATE | — | — |
| 4 | FiscalDocHeaderDetailExtnEODocExtHdrId1 | DOC_EXT_HDR_ID | — | — |
| 5 | FiscalDocHeaderDetailExtnEOEntityCode1 | ENTITY_CODE | — | — |
| 6 | FiscalDocHeaderDetailExtnEOEventClassCode1 | EVENT_CLASS_CODE | — | — |
| 7 | FiscalDocHeaderDetailExtnEOHdrAtrbExtDtlId | HDR_ATRB_EXT_DTL_ID | — | — |
| 8 | FiscalDocHeaderDetailExtnEOJobDefinitionName4 | JOB_DEFINITION_NAME | — | — |
| 9 | FiscalDocHeaderDetailExtnEOJobDefinitionPackage4 | JOB_DEFINITION_PACKAGE | — | — |
| 10 | FiscalDocHeaderDetailExtnEOLastUpdateDate4 | LAST_UPDATE_DATE | — | — |
| 11 | FiscalDocHeaderDetailExtnEOLastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 12 | FiscalDocHeaderDetailExtnEOLastUpdatedBy4 | LAST_UPDATED_BY | — | — |
| 13 | FiscalDocHeaderDetailExtnEOObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 14 | FiscalDocHeaderDetailExtnEOOrgId1 | ORG_ID | — | — |
| 15 | FiscalDocHeaderDetailExtnEORecordType | RECORD_TYPE | — | — |
| 16 | FiscalDocHeaderDetailExtnEORequestId4 | REQUEST_ID | — | — |
| 17 | FiscalDocHeaderDetailExtnEOTaxRelatedLegalMessageFlag | TAX_RELATED_LEGAL_MESSAGE_FLAG | — | — |
| 18 | FiscalDocHeaderDetailExtnEOTrxId1 | TRX_ID | — | — |

### [[jg_fscl_lines_atrb_ext_all|JG_FSCL_LINES_ATRB_EXT_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocLineExtnEOApplicationId2 | APPLICATION_ID | — | — |
| 2 | FiscalDocLineExtnEOCreatedBy5 | CREATED_BY | — | — |
| 3 | FiscalDocLineExtnEOCreationDate5 | CREATION_DATE | — | — |
| 4 | FiscalDocLineExtnEODocExtHdrId2 | DOC_EXT_HDR_ID | — | — |
| 5 | FiscalDocLineExtnEODocExtLineId | DOC_EXT_LINE_ID | — | — |
| 6 | FiscalDocLineExtnEOEntityCode2 | ENTITY_CODE | — | — |
| 7 | FiscalDocLineExtnEOEventClassCode2 | EVENT_CLASS_CODE | — | — |
| 8 | FiscalDocLineExtnEOItemSerialNumber | ITEM_SERIAL_NUMBER | — | — |
| 9 | FiscalDocLineExtnEOJobDefinitionName5 | JOB_DEFINITION_NAME | — | — |
| 10 | FiscalDocLineExtnEOJobDefinitionPackage5 | JOB_DEFINITION_PACKAGE | — | — |
| 11 | FiscalDocLineExtnEOLastUpdateDate5 | LAST_UPDATE_DATE | — | — |
| 12 | FiscalDocLineExtnEOLastUpdateLogin5 | LAST_UPDATE_LOGIN | — | — |
| 13 | FiscalDocLineExtnEOLastUpdatedBy5 | LAST_UPDATED_BY | — | — |
| 14 | FiscalDocLineExtnEOLegalMessageText | LEGAL_MESSAGE_TEXT | — | ✅ |
| 15 | FiscalDocLineExtnEOObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 16 | FiscalDocLineExtnEOOrgId2 | ORG_ID | — | — |
| 17 | FiscalDocLineExtnEOProceedingIdentifier | PROCEEDING_IDENTIFIER | — | ✅ |
| 18 | FiscalDocLineExtnEOProceedingOrigin | PROCEEDING_ORIGIN | — | ✅ |
| 19 | FiscalDocLineExtnEORequestId5 | REQUEST_ID | — | — |
| 20 | FiscalDocLineExtnEOServiceSituation1 | SERVICE_SITUATION | — | ✅ |
| 21 | FiscalDocLineExtnEOTrxId2 | TRX_ID | — | — |
| 22 | FiscalDocLineExtnEOTrxLevelType | TRX_LEVEL_TYPE | — | ✅ |
| 23 | FiscalDocLineExtnEOTrxLineId | TRX_LINE_ID | — | — |

### [[jg_fscl_ln_dtls_atrb_ext_all|JG_FSCL_LN_DTLS_ATRB_EXT_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocLineDetailExtnEOApplicationId3 | APPLICATION_ID | — | — |
| 2 | FiscalDocLineDetailExtnEOCreatedBy6 | CREATED_BY | — | — |
| 3 | FiscalDocLineDetailExtnEOCreationDate6 | CREATION_DATE | — | — |
| 4 | FiscalDocLineDetailExtnEODocExtHdrId3 | DOC_EXT_HDR_ID | — | — |
| 5 | FiscalDocLineDetailExtnEODocExtLineDetailId | DOC_EXT_LINE_DETAIL_ID | — | — |
| 6 | FiscalDocLineDetailExtnEODocExtLineId1 | DOC_EXT_LINE_ID | — | — |
| 7 | FiscalDocLineDetailExtnEOEntityCode3 | ENTITY_CODE | — | — |
| 8 | FiscalDocLineDetailExtnEOEventClassCode3 | EVENT_CLASS_CODE | — | — |
| 9 | FiscalDocLineDetailExtnEOJobDefinitionName6 | JOB_DEFINITION_NAME | — | — |
| 10 | FiscalDocLineDetailExtnEOJobDefinitionPackage6 | JOB_DEFINITION_PACKAGE | — | — |
| 11 | FiscalDocLineDetailExtnEOLastUpdateDate6 | LAST_UPDATE_DATE | — | — |
| 12 | FiscalDocLineDetailExtnEOLastUpdateLogin6 | LAST_UPDATE_LOGIN | — | — |
| 13 | FiscalDocLineDetailExtnEOLastUpdatedBy6 | LAST_UPDATED_BY | — | — |
| 14 | FiscalDocLineDetailExtnEOObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 15 | FiscalDocLineDetailExtnEOOrgId3 | ORG_ID | — | — |
| 16 | FiscalDocLineDetailExtnEORequestId6 | REQUEST_ID | — | — |
| 17 | FiscalDocLineDetailExtnEOTrxId3 | TRX_ID | — | — |
| 18 | FiscalDocLineDetailExtnEOTrxLevelType1 | TRX_LEVEL_TYPE | — | — |
| 19 | FiscalDocLineDetailExtnEOTrxLineDetailId | TRX_LINE_DETAIL_ID | — | — |
| 20 | FiscalDocLineDetailExtnEOTrxLineId1 | TRX_LINE_ID | — | — |

### [[jg_fscl_tax_lines_all|JG_FSCL_TAX_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LinesFiscalDocTaxLineEOAdjustedTaxLineId | ADJUSTED_TAX_LINE_ID | — | — |
| 2 | LinesFiscalDocTaxLineEOApplicationId5 | APPLICATION_ID | — | — |
| 3 | LinesFiscalDocTaxLineEOCalTaxAmt | CAL_TAX_AMT | — | ✅ |
| 4 | LinesFiscalDocTaxLineEOCalTaxAmtTaxCurr | CAL_TAX_AMT_TAX_CURR | — | ✅ |
| 5 | LinesFiscalDocTaxLineEOCityCode | CITY_CODE | — | — |
| 6 | LinesFiscalDocTaxLineEOContentOwnerId | CONTENT_OWNER_ID | — | — |
| 7 | LinesFiscalDocTaxLineEOCreatedBy9 | CREATED_BY | — | — |
| 8 | LinesFiscalDocTaxLineEOCreationDate9 | CREATION_DATE | — | ✅ |
| 9 | LinesFiscalDocTaxLineEOEntityCode5 | ENTITY_CODE | — | — |
| 10 | LinesFiscalDocTaxLineEOEventClassCode5 | EVENT_CLASS_CODE | — | — |
| 11 | LinesFiscalDocTaxLineEOExemptCertificateNumber | EXEMPT_CERTIFICATE_NUMBER | — | — |
| 12 | LinesFiscalDocTaxLineEOExemptReasonCode | EXEMPT_REASON_CODE | — | — |
| 13 | LinesFiscalDocTaxLineEOInterfaceEntityCode | INTERFACE_ENTITY_CODE | — | — |
| 14 | LinesFiscalDocTaxLineEOInterfaceTaxLineId | INTERFACE_TAX_LINE_ID | — | — |
| 15 | LinesFiscalDocTaxLineEOJobDefinitionName8 | JOB_DEFINITION_NAME | — | — |
| 16 | LinesFiscalDocTaxLineEOJobDefinitionPackage8 | JOB_DEFINITION_PACKAGE | — | — |
| 17 | LinesFiscalDocTaxLineEOLastUpdateDate9 | LAST_UPDATE_DATE | — | ✅ |
| 18 | LinesFiscalDocTaxLineEOLastUpdateLogin9 | LAST_UPDATE_LOGIN | — | — |
| 19 | LinesFiscalDocTaxLineEOLastUpdatedBy9 | LAST_UPDATED_BY | — | — |
| 20 | LinesFiscalDocTaxLineEOMainTrxLineId | MAIN_TRX_LINE_ID | — | — |
| 21 | LinesFiscalDocTaxLineEOObjectVersionNumber7 | OBJECT_VERSION_NUMBER | — | — |
| 22 | LinesFiscalDocTaxLineEOOrgId4 | ORG_ID | — | — |
| 23 | LinesFiscalDocTaxLineEOOrigSelfAssessedFlag | ORIG_SELF_ASSESSED_FLAG | — | — |
| 24 | LinesFiscalDocTaxLineEOOrigTaxAmtIncludedFlag | ORIG_TAX_AMT_INCLUDED_FLAG | — | — |
| 25 | LinesFiscalDocTaxLineEOOrigTaxJurisdictionCode | ORIG_TAX_JURISDICTION_CODE | — | — |
| 26 | LinesFiscalDocTaxLineEOOrigTaxJurisdictionId | ORIG_TAX_JURISDICTION_ID | — | — |
| 27 | LinesFiscalDocTaxLineEOOrigTaxRate | ORIG_TAX_RATE | — | — |
| 28 | LinesFiscalDocTaxLineEOOrigTaxRateCode | ORIG_TAX_RATE_CODE | — | — |
| 29 | LinesFiscalDocTaxLineEOOrigTaxRateId | ORIG_TAX_RATE_ID | — | — |
| 30 | LinesFiscalDocTaxLineEOOrigTaxStatusCode | ORIG_TAX_STATUS_CODE | — | — |
| 31 | LinesFiscalDocTaxLineEOOrigTaxStatusId | ORIG_TAX_STATUS_ID | — | — |
| 32 | LinesFiscalDocTaxLineEOQuantity2 | QUANTITY | — | ✅ |
| 33 | LinesFiscalDocTaxLineEOReferenceDocLineAmt | REFERENCE_DOC_LINE_AMT | — | — |
| 34 | LinesFiscalDocTaxLineEOReferenceDocUnitPrice | REFERENCE_DOC_UNIT_PRICE | — | — |
| 35 | LinesFiscalDocTaxLineEOReportingTypeCode | REPORTING_TYPE_CODE | — | ✅ |
| 36 | LinesFiscalDocTaxLineEORequestId8 | REQUEST_ID | — | — |
| 37 | LinesFiscalDocTaxLineEOSelfAssessedFlag | SELF_ASSESSED_FLAG | — | ✅ |
| 38 | LinesFiscalDocTaxLineEOServiceItemCode | SERVICE_ITEM_CODE | — | — |
| 39 | LinesFiscalDocTaxLineEOTax | TAX | — | ✅ |
| 40 | LinesFiscalDocTaxLineEOTaxAmt | TAX_AMT | — | ✅ |
| 41 | LinesFiscalDocTaxLineEOTaxAmtIncludedFlag | TAX_AMT_INCLUDED_FLAG | — | ✅ |
| 42 | LinesFiscalDocTaxLineEOTaxAmtTaxCurr | TAX_AMT_TAX_CURR | — | ✅ |
| 43 | LinesFiscalDocTaxLineEOTaxCreditAmount | TAX_CREDIT_AMOUNT | — | — |
| 44 | LinesFiscalDocTaxLineEOTaxExceptionId | TAX_EXCEPTION_ID | — | — |
| 45 | LinesFiscalDocTaxLineEOTaxExemptionId | TAX_EXEMPTION_ID | — | — |
| 46 | LinesFiscalDocTaxLineEOTaxHoldCode | TAX_HOLD_CODE | — | ✅ |
| 47 | LinesFiscalDocTaxLineEOTaxId | TAX_ID | — | — |
| 48 | LinesFiscalDocTaxLineEOTaxJurisdictionCode | TAX_JURISDICTION_CODE | — | ✅ |
| 49 | LinesFiscalDocTaxLineEOTaxJurisdictionId | TAX_JURISDICTION_ID | — | — |
| 50 | LinesFiscalDocTaxLineEOTaxLineId | TAX_LINE_ID | — | — |
| 51 | LinesFiscalDocTaxLineEOTaxLineNumber | TAX_LINE_NUMBER | — | ✅ |
| 52 | LinesFiscalDocTaxLineEOTaxLineSourceCode | TAX_LINE_SOURCE_CODE | — | — |
| 53 | LinesFiscalDocTaxLineEOTaxOnlyLineFlag | TAX_ONLY_LINE_FLAG | — | — |
| 54 | LinesFiscalDocTaxLineEOTaxRate | TAX_RATE | — | ✅ |
| 55 | LinesFiscalDocTaxLineEOTaxRateCode | TAX_RATE_CODE | — | ✅ |
| 56 | LinesFiscalDocTaxLineEOTaxRateId | TAX_RATE_ID | — | — |
| 57 | LinesFiscalDocTaxLineEOTaxRegimeCode | TAX_REGIME_CODE | — | ✅ |
| 58 | LinesFiscalDocTaxLineEOTaxRegimeId | TAX_REGIME_ID | — | — |
| 59 | LinesFiscalDocTaxLineEOTaxSituationCode | TAX_SITUATION_CODE | — | — |
| 60 | LinesFiscalDocTaxLineEOTaxStatusCode | TAX_STATUS_CODE | — | ✅ |
| 61 | LinesFiscalDocTaxLineEOTaxStatusId | TAX_STATUS_ID | — | — |
| 62 | LinesFiscalDocTaxLineEOTaxableAmt | TAXABLE_AMT | — | ✅ |
| 63 | LinesFiscalDocTaxLineEOTaxableAmtDetermCode | TAXABLE_AMT_DETERM_CODE | — | — |
| 64 | LinesFiscalDocTaxLineEOTaxableBasisPercPayerOpr | TAXABLE_BASIS_PERC_PAYER_OPR | — | — |
| 65 | LinesFiscalDocTaxLineEOTaxableBasisReductionPerc | TAXABLE_BASIS_REDUCTION_PERC | — | — |
| 66 | LinesFiscalDocTaxLineEOTrxId4 | TRX_ID | — | — |
| 67 | LinesFiscalDocTaxLineEOTrxLevelType2 | TRX_LEVEL_TYPE | — | — |
| 68 | LinesFiscalDocTaxLineEOTrxLineId2 | TRX_LINE_ID | — | — |
| 69 | LinesFiscalDocTaxLineEOUomCode1 | UOM_CODE | — | ✅ |
| 70 | LinesFiscalDocTaxLineEOUserEnteredTaxAmt | USER_ENTERED_TAX_AMT | — | ✅ |
| 71 | LinesFiscalDocTaxLineEOUserEnteredTaxAmtTaxCurr | USER_ENTERED_TAX_AMT_TAX_CURR | — | ✅ |
| 72 | LinesFiscalDocTaxLineEOValueAddedMarginPerc | VALUE_ADDED_MARGIN_PERC | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HdrsCreatedByPersonNameDPEOBusinessGroupId6 | BUSINESS_GROUP_ID | — | — |
| 2 | HdrsCreatedByPersonNameDPEOCreatedBy16 | CREATED_BY | — | — |
| 3 | HdrsCreatedByPersonNameDPEOCreationDate16 | CREATION_DATE | — | — |
| 4 | HdrsCreatedByPersonNameDPEODisplayName | DISPLAY_NAME | — | — |
| 5 | HdrsCreatedByPersonNameDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | HdrsCreatedByPersonNameDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 7 | HdrsCreatedByPersonNameDPEOFirstName | FIRST_NAME | — | — |
| 8 | HdrsCreatedByPersonNameDPEOFullName | FULL_NAME | — | ✅ |
| 9 | HdrsCreatedByPersonNameDPEOHonors | HONORS | — | — |
| 10 | HdrsCreatedByPersonNameDPEOKnownAs | KNOWN_AS | — | — |
| 11 | HdrsCreatedByPersonNameDPEOLastName | LAST_NAME | — | — |
| 12 | HdrsCreatedByPersonNameDPEOLastUpdateDate16 | LAST_UPDATE_DATE | — | — |
| 13 | HdrsCreatedByPersonNameDPEOLastUpdateLogin16 | LAST_UPDATE_LOGIN | — | — |
| 14 | HdrsCreatedByPersonNameDPEOLastUpdatedBy16 | LAST_UPDATED_BY | — | — |
| 15 | HdrsCreatedByPersonNameDPEOLegislationCode | LEGISLATION_CODE | — | — |
| 16 | HdrsCreatedByPersonNameDPEOListName | LIST_NAME | — | — |
| 17 | HdrsCreatedByPersonNameDPEOMiddleNames | MIDDLE_NAMES | — | — |
| 18 | HdrsCreatedByPersonNameDPEOMilitaryRank | MILITARY_RANK | — | — |
| 19 | HdrsCreatedByPersonNameDPEOObjectVersionNumber14 | OBJECT_VERSION_NUMBER | — | — |
| 20 | HdrsCreatedByPersonNameDPEOOrderName | ORDER_NAME | — | — |
| 21 | HdrsCreatedByPersonNameDPEOPersonId6 | PERSON_ID | — | — |
| 22 | HdrsCreatedByPersonNameDPEOPersonNameId | PERSON_NAME_ID | — | — |
| 23 | HdrsCreatedByPersonNameDPEOPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 24 | HdrsCreatedByPersonNameDPEOPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 25 | HdrsCreatedByPersonNameDPEOSuffix | SUFFIX | — | — |
| 26 | HdrsCreatedByPersonNameDPEOTitle | TITLE | — | — |
| 27 | HeaderExtnToCreatedByPersonNBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 28 | HeaderExtnToCreatedByPersonNCreatedBy2 | CREATED_BY | — | — |
| 29 | HeaderExtnToCreatedByPersonNCreationDate2 | CREATION_DATE | — | — |
| 30 | HeaderExtnToCreatedByPersonNDisplayName | DISPLAY_NAME | — | — |
| 31 | HeaderExtnToCreatedByPersonNEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 32 | HeaderExtnToCreatedByPersonNEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 33 | HeaderExtnToCreatedByPersonNFirstName | FIRST_NAME | — | — |
| 34 | HeaderExtnToCreatedByPersonNFullName | FULL_NAME | — | ✅ |
| 35 | HeaderExtnToCreatedByPersonNHonors | HONORS | — | — |
| 36 | HeaderExtnToCreatedByPersonNKnownAs | KNOWN_AS | — | — |
| 37 | HeaderExtnToCreatedByPersonNLastName | LAST_NAME | — | — |
| 38 | HeaderExtnToCreatedByPersonNLastUpdateDate2 | LAST_UPDATE_DATE | — | — |
| 39 | HeaderExtnToCreatedByPersonNLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 40 | HeaderExtnToCreatedByPersonNLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 41 | HeaderExtnToCreatedByPersonNLegislationCode | LEGISLATION_CODE | — | — |
| 42 | HeaderExtnToCreatedByPersonNListName | LIST_NAME | — | — |
| 43 | HeaderExtnToCreatedByPersonNMiddleNames | MIDDLE_NAMES | — | — |
| 44 | HeaderExtnToCreatedByPersonNMilitaryRank | MILITARY_RANK | — | — |
| 45 | HeaderExtnToCreatedByPersonNNameType | NAME_TYPE | — | — |
| 46 | HeaderExtnToCreatedByPersonNObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 47 | HeaderExtnToCreatedByPersonNOrderName | ORDER_NAME | — | — |
| 48 | HeaderExtnToCreatedByPersonNPersonId2 | PERSON_ID | — | — |
| 49 | HeaderExtnToCreatedByPersonNPersonNameId | PERSON_NAME_ID | — | — |
| 50 | HeaderExtnToCreatedByPersonNPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 51 | HeaderExtnToCreatedByPersonNPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 52 | HeaderExtnToCreatedByPersonNSuffix | SUFFIX | — | — |
| 53 | HeaderExtnToCreatedByPersonNTitle | TITLE | — | — |
| 54 | HeaderExtnToLastUpdtdPersonNBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 55 | HeaderExtnToLastUpdtdPersonNCreatedBy3 | CREATED_BY | — | — |
| 56 | HeaderExtnToLastUpdtdPersonNCreationDate3 | CREATION_DATE | — | — |
| 57 | HeaderExtnToLastUpdtdPersonNDisplayName1 | DISPLAY_NAME | — | — |
| 58 | HeaderExtnToLastUpdtdPersonNEffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 59 | HeaderExtnToLastUpdtdPersonNEffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 60 | HeaderExtnToLastUpdtdPersonNFirstName1 | FIRST_NAME | — | — |
| 61 | HeaderExtnToLastUpdtdPersonNFullName1 | FULL_NAME | — | ✅ |
| 62 | HeaderExtnToLastUpdtdPersonNHonors1 | HONORS | — | — |
| 63 | HeaderExtnToLastUpdtdPersonNKnownAs1 | KNOWN_AS | — | — |
| 64 | HeaderExtnToLastUpdtdPersonNLastName1 | LAST_NAME | — | — |
| 65 | HeaderExtnToLastUpdtdPersonNLastUpdateDate3 | LAST_UPDATE_DATE | — | — |
| 66 | HeaderExtnToLastUpdtdPersonNLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 67 | HeaderExtnToLastUpdtdPersonNLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 68 | HeaderExtnToLastUpdtdPersonNLegislationCode1 | LEGISLATION_CODE | — | — |
| 69 | HeaderExtnToLastUpdtdPersonNListName1 | LIST_NAME | — | — |
| 70 | HeaderExtnToLastUpdtdPersonNMiddleNames1 | MIDDLE_NAMES | — | — |
| 71 | HeaderExtnToLastUpdtdPersonNMilitaryRank1 | MILITARY_RANK | — | — |
| 72 | HeaderExtnToLastUpdtdPersonNNameType1 | NAME_TYPE | — | — |
| 73 | HeaderExtnToLastUpdtdPersonNObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 74 | HeaderExtnToLastUpdtdPersonNOrderName1 | ORDER_NAME | — | — |
| 75 | HeaderExtnToLastUpdtdPersonNPersonId3 | PERSON_ID | — | — |
| 76 | HeaderExtnToLastUpdtdPersonNPersonNameId1 | PERSON_NAME_ID | — | — |
| 77 | HeaderExtnToLastUpdtdPersonNPreNameAdjunct1 | PRE_NAME_ADJUNCT | — | — |
| 78 | HeaderExtnToLastUpdtdPersonNPreviousLastName1 | PREVIOUS_LAST_NAME | — | — |
| 79 | HeaderExtnToLastUpdtdPersonNSuffix1 | SUFFIX | — | — |
| 80 | HeaderExtnToLastUpdtdPersonNTitle1 | TITLE | — | — |
| 81 | HrdsLUpdtdByPersonNameDPEO1_1BusinessGroupId7 | BUSINESS_GROUP_ID | — | — |
| 82 | HrdsLUpdtdByPersonNameDPEO1_1CreatedBy17 | CREATED_BY | — | — |
| 83 | HrdsLUpdtdByPersonNameDPEO1_1CreationDate17 | CREATION_DATE | — | — |
| 84 | HrdsLUpdtdByPersonNameDPEO1_1DisplayName1 | DISPLAY_NAME | — | — |
| 85 | HrdsLUpdtdByPersonNameDPEO1_1EffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 86 | HrdsLUpdtdByPersonNameDPEO1_1EffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 87 | HrdsLUpdtdByPersonNameDPEO1_1FirstName1 | FIRST_NAME | — | — |
| 88 | HrdsLUpdtdByPersonNameDPEO1_1FullName1 | FULL_NAME | — | ✅ |
| 89 | HrdsLUpdtdByPersonNameDPEO1_1Honors1 | HONORS | — | — |
| 90 | HrdsLUpdtdByPersonNameDPEO1_1KnownAs1 | KNOWN_AS | — | — |
| 91 | HrdsLUpdtdByPersonNameDPEO1_1LastName1 | LAST_NAME | — | — |
| 92 | HrdsLUpdtdByPersonNameDPEO1_1LastUpdateDate17 | LAST_UPDATE_DATE | — | — |
| 93 | HrdsLUpdtdByPersonNameDPEO1_1LastUpdateLogin17 | LAST_UPDATE_LOGIN | — | — |
| 94 | HrdsLUpdtdByPersonNameDPEO1_1LastUpdatedBy17 | LAST_UPDATED_BY | — | — |
| 95 | HrdsLUpdtdByPersonNameDPEO1_1LegislationCode1 | LEGISLATION_CODE | — | — |
| 96 | HrdsLUpdtdByPersonNameDPEO1_1ListName1 | LIST_NAME | — | — |
| 97 | HrdsLUpdtdByPersonNameDPEO1_1MiddleNames1 | MIDDLE_NAMES | — | — |
| 98 | HrdsLUpdtdByPersonNameDPEO1_1MilitaryRank1 | MILITARY_RANK | — | — |
| 99 | HrdsLUpdtdByPersonNameDPEO1_1ObjectVersionNumber15 | OBJECT_VERSION_NUMBER | — | — |
| 100 | HrdsLUpdtdByPersonNameDPEO1_1OrderName1 | ORDER_NAME | — | — |
| 101 | HrdsLUpdtdByPersonNameDPEO1_1PersonId7 | PERSON_ID | — | — |
| 102 | HrdsLUpdtdByPersonNameDPEO1_1PersonNameId1 | PERSON_NAME_ID | — | — |
| 103 | HrdsLUpdtdByPersonNameDPEO1_1PreNameAdjunct1 | PRE_NAME_ADJUNCT | — | — |
| 104 | HrdsLUpdtdByPersonNameDPEO1_1PreviousLastName1 | PREVIOUS_LAST_NAME | — | — |
| 105 | HrdsLUpdtdByPersonNameDPEO1_1Suffix1 | SUFFIX | — | — |
| 106 | HrdsLUpdtdByPersonNameDPEO1_1Title1 | TITLE | — | — |
| 107 | LinesCreatedByPersonNameDPEOBusinessGroupId10 | BUSINESS_GROUP_ID | — | — |
| 108 | LinesCreatedByPersonNameDPEOCreatedBy20 | CREATED_BY | — | — |
| 109 | LinesCreatedByPersonNameDPEOCreationDate20 | CREATION_DATE | — | — |
| 110 | LinesCreatedByPersonNameDPEODisplayName4 | DISPLAY_NAME | — | — |
| 111 | LinesCreatedByPersonNameDPEOEffectiveEndDate4 | EFFECTIVE_END_DATE | — | — |
| 112 | LinesCreatedByPersonNameDPEOEffectiveStartDate4 | EFFECTIVE_START_DATE | — | — |
| 113 | LinesCreatedByPersonNameDPEOFirstName4 | FIRST_NAME | — | — |
| 114 | LinesCreatedByPersonNameDPEOFullName4 | FULL_NAME | — | ✅ |
| 115 | LinesCreatedByPersonNameDPEOHonors4 | HONORS | — | — |
| 116 | LinesCreatedByPersonNameDPEOKnownAs4 | KNOWN_AS | — | — |
| 117 | LinesCreatedByPersonNameDPEOLastName4 | LAST_NAME | — | — |
| 118 | LinesCreatedByPersonNameDPEOLastUpdateDate20 | LAST_UPDATE_DATE | — | — |
| 119 | LinesCreatedByPersonNameDPEOLastUpdateLogin20 | LAST_UPDATE_LOGIN | — | — |
| 120 | LinesCreatedByPersonNameDPEOLastUpdatedBy20 | LAST_UPDATED_BY | — | — |
| 121 | LinesCreatedByPersonNameDPEOLegislationCode4 | LEGISLATION_CODE | — | — |
| 122 | LinesCreatedByPersonNameDPEOListName4 | LIST_NAME | — | — |
| 123 | LinesCreatedByPersonNameDPEOMiddleNames4 | MIDDLE_NAMES | — | — |
| 124 | LinesCreatedByPersonNameDPEOMilitaryRank4 | MILITARY_RANK | — | — |
| 125 | LinesCreatedByPersonNameDPEOObjectVersionNumber18 | OBJECT_VERSION_NUMBER | — | — |
| 126 | LinesCreatedByPersonNameDPEOOrderName4 | ORDER_NAME | — | — |
| 127 | LinesCreatedByPersonNameDPEOPersonId10 | PERSON_ID | — | — |
| 128 | LinesCreatedByPersonNameDPEOPersonNameId4 | PERSON_NAME_ID | — | — |
| 129 | LinesCreatedByPersonNameDPEOPreNameAdjunct4 | PRE_NAME_ADJUNCT | — | — |
| 130 | LinesCreatedByPersonNameDPEOPreviousLastName4 | PREVIOUS_LAST_NAME | — | — |
| 131 | LinesCreatedByPersonNameDPEOSuffix4 | SUFFIX | — | — |
| 132 | LinesCreatedByPersonNameDPEOTitle4 | TITLE | — | — |
| 133 | LinesLUpdtdByPersonNameDPEO1_1BusinessGroupId11 | BUSINESS_GROUP_ID | — | — |
| 134 | LinesLUpdtdByPersonNameDPEO1_1CreatedBy21 | CREATED_BY | — | — |
| 135 | LinesLUpdtdByPersonNameDPEO1_1CreationDate21 | CREATION_DATE | — | — |
| 136 | LinesLUpdtdByPersonNameDPEO1_1DisplayName5 | DISPLAY_NAME | — | — |
| 137 | LinesLUpdtdByPersonNameDPEO1_1EffectiveEndDate5 | EFFECTIVE_END_DATE | — | — |
| 138 | LinesLUpdtdByPersonNameDPEO1_1EffectiveStartDate5 | EFFECTIVE_START_DATE | — | — |
| 139 | LinesLUpdtdByPersonNameDPEO1_1FirstName5 | FIRST_NAME | — | — |
| 140 | LinesLUpdtdByPersonNameDPEO1_1FullName5 | FULL_NAME | — | ✅ |
| 141 | LinesLUpdtdByPersonNameDPEO1_1Honors5 | HONORS | — | — |
| 142 | LinesLUpdtdByPersonNameDPEO1_1KnownAs5 | KNOWN_AS | — | — |
| 143 | LinesLUpdtdByPersonNameDPEO1_1LastName5 | LAST_NAME | — | — |
| 144 | LinesLUpdtdByPersonNameDPEO1_1LastUpdateDate21 | LAST_UPDATE_DATE | — | — |
| 145 | LinesLUpdtdByPersonNameDPEO1_1LastUpdateLogin21 | LAST_UPDATE_LOGIN | — | — |
| 146 | LinesLUpdtdByPersonNameDPEO1_1LastUpdatedBy21 | LAST_UPDATED_BY | — | — |
| 147 | LinesLUpdtdByPersonNameDPEO1_1LegislationCode5 | LEGISLATION_CODE | — | — |
| 148 | LinesLUpdtdByPersonNameDPEO1_1ListName5 | LIST_NAME | — | — |
| 149 | LinesLUpdtdByPersonNameDPEO1_1MiddleNames5 | MIDDLE_NAMES | — | — |
| 150 | LinesLUpdtdByPersonNameDPEO1_1MilitaryRank5 | MILITARY_RANK | — | — |
| 151 | LinesLUpdtdByPersonNameDPEO1_1ObjectVersionNumber19 | OBJECT_VERSION_NUMBER | — | — |
| 152 | LinesLUpdtdByPersonNameDPEO1_1OrderName5 | ORDER_NAME | — | — |
| 153 | LinesLUpdtdByPersonNameDPEO1_1PersonId11 | PERSON_ID | — | — |
| 154 | LinesLUpdtdByPersonNameDPEO1_1PersonNameId5 | PERSON_NAME_ID | — | — |
| 155 | LinesLUpdtdByPersonNameDPEO1_1PreNameAdjunct5 | PRE_NAME_ADJUNCT | — | — |
| 156 | LinesLUpdtdByPersonNameDPEO1_1PreviousLastName5 | PREVIOUS_LAST_NAME | — | — |
| 157 | LinesLUpdtdByPersonNameDPEO1_1Suffix5 | SUFFIX | — | — |
| 158 | LinesLUpdtdByPersonNameDPEO1_1Title5 | TITLE | — | — |
| 159 | TaxLineCreatedByPersonNameDPBusinessGroupId8 | BUSINESS_GROUP_ID | — | — |
| 160 | TaxLineCreatedByPersonNameDPCreatedBy18 | CREATED_BY | — | — |
| 161 | TaxLineCreatedByPersonNameDPCreationDate18 | CREATION_DATE | — | — |
| 162 | TaxLineCreatedByPersonNameDPDisplayName2 | DISPLAY_NAME | — | — |
| 163 | TaxLineCreatedByPersonNameDPEffectiveEndDate2 | EFFECTIVE_END_DATE | — | — |
| 164 | TaxLineCreatedByPersonNameDPEffectiveStartDate2 | EFFECTIVE_START_DATE | — | — |
| 165 | TaxLineCreatedByPersonNameDPFirstName2 | FIRST_NAME | — | — |
| 166 | TaxLineCreatedByPersonNameDPFullName2 | FULL_NAME | — | ✅ |
| 167 | TaxLineCreatedByPersonNameDPHonors2 | HONORS | — | — |
| 168 | TaxLineCreatedByPersonNameDPKnownAs2 | KNOWN_AS | — | — |
| 169 | TaxLineCreatedByPersonNameDPLastName2 | LAST_NAME | — | — |
| 170 | TaxLineCreatedByPersonNameDPLastUpdateDate18 | LAST_UPDATE_DATE | — | — |
| 171 | TaxLineCreatedByPersonNameDPLastUpdateLogin18 | LAST_UPDATE_LOGIN | — | — |
| 172 | TaxLineCreatedByPersonNameDPLastUpdatedBy18 | LAST_UPDATED_BY | — | — |
| 173 | TaxLineCreatedByPersonNameDPLegislationCode2 | LEGISLATION_CODE | — | — |
| 174 | TaxLineCreatedByPersonNameDPListName2 | LIST_NAME | — | — |
| 175 | TaxLineCreatedByPersonNameDPMiddleNames2 | MIDDLE_NAMES | — | — |
| 176 | TaxLineCreatedByPersonNameDPMilitaryRank2 | MILITARY_RANK | — | — |
| 177 | TaxLineCreatedByPersonNameDPObjectVersionNumber16 | OBJECT_VERSION_NUMBER | — | — |
| 178 | TaxLineCreatedByPersonNameDPOrderName2 | ORDER_NAME | — | — |
| 179 | TaxLineCreatedByPersonNameDPPersonId8 | PERSON_ID | — | — |
| 180 | TaxLineCreatedByPersonNameDPPersonNameId2 | PERSON_NAME_ID | — | — |
| 181 | TaxLineCreatedByPersonNameDPPreNameAdjunct2 | PRE_NAME_ADJUNCT | — | — |
| 182 | TaxLineCreatedByPersonNameDPPreviousLastName2 | PREVIOUS_LAST_NAME | — | — |
| 183 | TaxLineCreatedByPersonNameDPSuffix2 | SUFFIX | — | — |
| 184 | TaxLineCreatedByPersonNameDPTitle2 | TITLE | — | — |
| 185 | TaxLineLUpdtdByPersonNameDPEBusinessGroupId9 | BUSINESS_GROUP_ID | — | — |
| 186 | TaxLineLUpdtdByPersonNameDPECreatedBy19 | CREATED_BY | — | — |
| 187 | TaxLineLUpdtdByPersonNameDPECreationDate19 | CREATION_DATE | — | — |
| 188 | TaxLineLUpdtdByPersonNameDPEDisplayName3 | DISPLAY_NAME | — | — |
| 189 | TaxLineLUpdtdByPersonNameDPEEffectiveEndDate3 | EFFECTIVE_END_DATE | — | — |
| 190 | TaxLineLUpdtdByPersonNameDPEEffectiveStartDate3 | EFFECTIVE_START_DATE | — | — |
| 191 | TaxLineLUpdtdByPersonNameDPEFirstName3 | FIRST_NAME | — | — |
| 192 | TaxLineLUpdtdByPersonNameDPEFullName3 | FULL_NAME | — | ✅ |
| 193 | TaxLineLUpdtdByPersonNameDPEHonors3 | HONORS | — | — |
| 194 | TaxLineLUpdtdByPersonNameDPEKnownAs3 | KNOWN_AS | — | — |
| 195 | TaxLineLUpdtdByPersonNameDPELastName3 | LAST_NAME | — | — |
| 196 | TaxLineLUpdtdByPersonNameDPELastUpdateDate19 | LAST_UPDATE_DATE | — | — |
| 197 | TaxLineLUpdtdByPersonNameDPELastUpdateLogin19 | LAST_UPDATE_LOGIN | — | — |
| 198 | TaxLineLUpdtdByPersonNameDPELastUpdatedBy19 | LAST_UPDATED_BY | — | — |
| 199 | TaxLineLUpdtdByPersonNameDPELegislationCode3 | LEGISLATION_CODE | — | — |
| 200 | TaxLineLUpdtdByPersonNameDPEListName3 | LIST_NAME | — | — |
| 201 | TaxLineLUpdtdByPersonNameDPEMiddleNames3 | MIDDLE_NAMES | — | — |
| 202 | TaxLineLUpdtdByPersonNameDPEMilitaryRank3 | MILITARY_RANK | — | — |
| 203 | TaxLineLUpdtdByPersonNameDPEObjectVersionNumber17 | OBJECT_VERSION_NUMBER | — | — |
| 204 | TaxLineLUpdtdByPersonNameDPEOrderName3 | ORDER_NAME | — | — |
| 205 | TaxLineLUpdtdByPersonNameDPEPersonId9 | PERSON_ID | — | — |
| 206 | TaxLineLUpdtdByPersonNameDPEPersonNameId3 | PERSON_NAME_ID | — | — |
| 207 | TaxLineLUpdtdByPersonNameDPEPreNameAdjunct3 | PRE_NAME_ADJUNCT | — | — |
| 208 | TaxLineLUpdtdByPersonNameDPEPreviousLastName3 | PREVIOUS_LAST_NAME | — | — |
| 209 | TaxLineLUpdtdByPersonNameDPESuffix3 | SUFFIX | — | — |
| 210 | TaxLineLUpdtdByPersonNameDPETitle3 | TITLE | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FDHeadersCreatedByUserPEOActiveFlag1 | ACTIVE_FLAG | — | — |
| 2 | FDHeadersCreatedByUserPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | FDHeadersCreatedByUserPEOCreatedBy10 | CREATED_BY | — | — |
| 4 | FDHeadersCreatedByUserPEOCreationDate10 | CREATION_DATE | — | — |
| 5 | FDHeadersCreatedByUserPEOCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 6 | FDHeadersCreatedByUserPEOEndDate | END_DATE | — | — |
| 7 | FDHeadersCreatedByUserPEOExternalId | EXTERNAL_ID | — | — |
| 8 | FDHeadersCreatedByUserPEOHrTerminated | HR_TERMINATED | — | — |
| 9 | FDHeadersCreatedByUserPEOLastUpdateDate10 | LAST_UPDATE_DATE | — | — |
| 10 | FDHeadersCreatedByUserPEOLastUpdateLogin10 | LAST_UPDATE_LOGIN | — | — |
| 11 | FDHeadersCreatedByUserPEOLastUpdatedBy10 | LAST_UPDATED_BY | — | — |
| 12 | FDHeadersCreatedByUserPEOMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 13 | FDHeadersCreatedByUserPEOObjectVersionNumber8 | OBJECT_VERSION_NUMBER | — | — |
| 14 | FDHeadersCreatedByUserPEOPartyId | PARTY_ID | — | — |
| 15 | FDHeadersCreatedByUserPEOPersonId | PERSON_ID | — | — |
| 16 | FDHeadersCreatedByUserPEOStartDate | START_DATE | — | — |
| 17 | FDHeadersCreatedByUserPEOSuspended | SUSPENDED | — | — |
| 18 | FDHeadersCreatedByUserPEOUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 19 | FDHeadersCreatedByUserPEOUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 20 | FDHeadersCreatedByUserPEOUserGuid | USER_GUID | — | — |
| 21 | FDHeadersCreatedByUserPEOUserId | USER_ID | — | — |
| 22 | FDHeadersCreatedByUserPEOUsername | USERNAME | — | — |
| 23 | FDHeadersLastUpdatedByUserPEActiveFlag2 | ACTIVE_FLAG | — | — |
| 24 | FDHeadersLastUpdatedByUserPEBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 25 | FDHeadersLastUpdatedByUserPECreatedBy11 | CREATED_BY | — | — |
| 26 | FDHeadersLastUpdatedByUserPECreationDate11 | CREATION_DATE | — | — |
| 27 | FDHeadersLastUpdatedByUserPECredentialsEmailSent1 | CREDENTIALS_EMAIL_SENT | — | — |
| 28 | FDHeadersLastUpdatedByUserPEEndDate1 | END_DATE | — | — |
| 29 | FDHeadersLastUpdatedByUserPEExternalId1 | EXTERNAL_ID | — | — |
| 30 | FDHeadersLastUpdatedByUserPEHrTerminated1 | HR_TERMINATED | — | — |
| 31 | FDHeadersLastUpdatedByUserPELastUpdateDate11 | LAST_UPDATE_DATE | — | — |
| 32 | FDHeadersLastUpdatedByUserPELastUpdateLogin11 | LAST_UPDATE_LOGIN | — | — |
| 33 | FDHeadersLastUpdatedByUserPELastUpdatedBy11 | LAST_UPDATED_BY | — | — |
| 34 | FDHeadersLastUpdatedByUserPEMultitenancyUsername1 | MULTITENANCY_USERNAME | — | — |
| 35 | FDHeadersLastUpdatedByUserPEObjectVersionNumber9 | OBJECT_VERSION_NUMBER | — | — |
| 36 | FDHeadersLastUpdatedByUserPEPartyId1 | PARTY_ID | — | — |
| 37 | FDHeadersLastUpdatedByUserPEPersonId1 | PERSON_ID | — | — |
| 38 | FDHeadersLastUpdatedByUserPEStartDate1 | START_DATE | — | — |
| 39 | FDHeadersLastUpdatedByUserPESuspended1 | SUSPENDED | — | — |
| 40 | FDHeadersLastUpdatedByUserPEUserDataChecksum1 | USER_DATA_CHECKSUM | — | — |
| 41 | FDHeadersLastUpdatedByUserPEUserDistinguishedName1 | USER_DISTINGUISHED_NAME | — | — |
| 42 | FDHeadersLastUpdatedByUserPEUserGuid1 | USER_GUID | — | — |
| 43 | FDHeadersLastUpdatedByUserPEUserId1 | USER_ID | — | — |
| 44 | FDHeadersLastUpdatedByUserPEUsername1 | USERNAME | — | — |
| 45 | FDLinesCreatedByUserPEOActiveFlag5 | ACTIVE_FLAG | — | — |
| 46 | FDLinesCreatedByUserPEOBusinessGroupId4 | BUSINESS_GROUP_ID | — | — |
| 47 | FDLinesCreatedByUserPEOCreatedBy14 | CREATED_BY | — | — |
| 48 | FDLinesCreatedByUserPEOCreationDate14 | CREATION_DATE | — | — |
| 49 | FDLinesCreatedByUserPEOCredentialsEmailSent4 | CREDENTIALS_EMAIL_SENT | — | — |
| 50 | FDLinesCreatedByUserPEOEndDate4 | END_DATE | — | — |
| 51 | FDLinesCreatedByUserPEOExternalId4 | EXTERNAL_ID | — | — |
| 52 | FDLinesCreatedByUserPEOHrTerminated4 | HR_TERMINATED | — | — |
| 53 | FDLinesCreatedByUserPEOLastUpdateDate14 | LAST_UPDATE_DATE | — | — |
| 54 | FDLinesCreatedByUserPEOLastUpdateLogin14 | LAST_UPDATE_LOGIN | — | — |
| 55 | FDLinesCreatedByUserPEOLastUpdatedBy14 | LAST_UPDATED_BY | — | — |
| 56 | FDLinesCreatedByUserPEOMultitenancyUsername4 | MULTITENANCY_USERNAME | — | — |
| 57 | FDLinesCreatedByUserPEOObjectVersionNumber12 | OBJECT_VERSION_NUMBER | — | — |
| 58 | FDLinesCreatedByUserPEOPartyId4 | PARTY_ID | — | — |
| 59 | FDLinesCreatedByUserPEOPersonId4 | PERSON_ID | — | — |
| 60 | FDLinesCreatedByUserPEOStartDate4 | START_DATE | — | — |
| 61 | FDLinesCreatedByUserPEOSuspended4 | SUSPENDED | — | — |
| 62 | FDLinesCreatedByUserPEOUserDataChecksum4 | USER_DATA_CHECKSUM | — | — |
| 63 | FDLinesCreatedByUserPEOUserDistinguishedName4 | USER_DISTINGUISHED_NAME | — | — |
| 64 | FDLinesCreatedByUserPEOUserGuid4 | USER_GUID | — | — |
| 65 | FDLinesCreatedByUserPEOUserId4 | USER_ID | — | — |
| 66 | FDLinesCreatedByUserPEOUsername4 | USERNAME | — | — |
| 67 | FDLinesLastUpdatedByUserPEO1_1ActiveFlag6 | ACTIVE_FLAG | — | — |
| 68 | FDLinesLastUpdatedByUserPEO1_1BusinessGroupId5 | BUSINESS_GROUP_ID | — | — |
| 69 | FDLinesLastUpdatedByUserPEO1_1CreatedBy15 | CREATED_BY | — | — |
| 70 | FDLinesLastUpdatedByUserPEO1_1CreationDate15 | CREATION_DATE | — | — |
| 71 | FDLinesLastUpdatedByUserPEO1_1CredentialsEmailSent5 | CREDENTIALS_EMAIL_SENT | — | — |
| 72 | FDLinesLastUpdatedByUserPEO1_1EndDate5 | END_DATE | — | — |
| 73 | FDLinesLastUpdatedByUserPEO1_1ExternalId5 | EXTERNAL_ID | — | — |
| 74 | FDLinesLastUpdatedByUserPEO1_1HrTerminated5 | HR_TERMINATED | — | — |
| 75 | FDLinesLastUpdatedByUserPEO1_1LastUpdateDate15 | LAST_UPDATE_DATE | — | — |
| 76 | FDLinesLastUpdatedByUserPEO1_1LastUpdateLogin15 | LAST_UPDATE_LOGIN | — | — |
| 77 | FDLinesLastUpdatedByUserPEO1_1LastUpdatedBy15 | LAST_UPDATED_BY | — | — |
| 78 | FDLinesLastUpdatedByUserPEO1_1MultitenancyUsername5 | MULTITENANCY_USERNAME | — | — |
| 79 | FDLinesLastUpdatedByUserPEO1_1ObjectVersionNumber13 | OBJECT_VERSION_NUMBER | — | — |
| 80 | FDLinesLastUpdatedByUserPEO1_1PartyId5 | PARTY_ID | — | — |
| 81 | FDLinesLastUpdatedByUserPEO1_1PersonId5 | PERSON_ID | — | — |
| 82 | FDLinesLastUpdatedByUserPEO1_1StartDate5 | START_DATE | — | — |
| 83 | FDLinesLastUpdatedByUserPEO1_1Suspended5 | SUSPENDED | — | — |
| 84 | FDLinesLastUpdatedByUserPEO1_1UserDataChecksum5 | USER_DATA_CHECKSUM | — | — |
| 85 | FDLinesLastUpdatedByUserPEO1_1UserDistinguishedName5 | USER_DISTINGUISHED_NAME | — | — |
| 86 | FDLinesLastUpdatedByUserPEO1_1UserGuid5 | USER_GUID | — | — |
| 87 | FDLinesLastUpdatedByUserPEO1_1UserId5 | USER_ID | — | — |
| 88 | FDLinesLastUpdatedByUserPEO1_1Username5 | USERNAME | — | — |
| 89 | FDTaxLineCreatedByUserPEOActiveFlag3 | ACTIVE_FLAG | — | — |
| 90 | FDTaxLineCreatedByUserPEOBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 91 | FDTaxLineCreatedByUserPEOCreatedBy12 | CREATED_BY | — | — |
| 92 | FDTaxLineCreatedByUserPEOCreationDate12 | CREATION_DATE | — | — |
| 93 | FDTaxLineCreatedByUserPEOCredentialsEmailSent2 | CREDENTIALS_EMAIL_SENT | — | — |
| 94 | FDTaxLineCreatedByUserPEOEndDate2 | END_DATE | — | — |
| 95 | FDTaxLineCreatedByUserPEOExternalId2 | EXTERNAL_ID | — | — |
| 96 | FDTaxLineCreatedByUserPEOHrTerminated2 | HR_TERMINATED | — | — |
| 97 | FDTaxLineCreatedByUserPEOLastUpdateDate12 | LAST_UPDATE_DATE | — | — |
| 98 | FDTaxLineCreatedByUserPEOLastUpdateLogin12 | LAST_UPDATE_LOGIN | — | — |
| 99 | FDTaxLineCreatedByUserPEOLastUpdatedBy12 | LAST_UPDATED_BY | — | — |
| 100 | FDTaxLineCreatedByUserPEOMultitenancyUsername2 | MULTITENANCY_USERNAME | — | — |
| 101 | FDTaxLineCreatedByUserPEOObjectVersionNumber10 | OBJECT_VERSION_NUMBER | — | — |
| 102 | FDTaxLineCreatedByUserPEOPartyId2 | PARTY_ID | — | — |
| 103 | FDTaxLineCreatedByUserPEOPersonId2 | PERSON_ID | — | — |
| 104 | FDTaxLineCreatedByUserPEOStartDate2 | START_DATE | — | — |
| 105 | FDTaxLineCreatedByUserPEOSuspended2 | SUSPENDED | — | — |
| 106 | FDTaxLineCreatedByUserPEOUserDataChecksum2 | USER_DATA_CHECKSUM | — | — |
| 107 | FDTaxLineCreatedByUserPEOUserDistinguishedName2 | USER_DISTINGUISHED_NAME | — | — |
| 108 | FDTaxLineCreatedByUserPEOUserGuid2 | USER_GUID | — | — |
| 109 | FDTaxLineCreatedByUserPEOUserId2 | USER_ID | — | — |
| 110 | FDTaxLineCreatedByUserPEOUsername2 | USERNAME | — | — |
| 111 | FDTaxLineLastUpdatedByUserPEActiveFlag4 | ACTIVE_FLAG | — | — |
| 112 | FDTaxLineLastUpdatedByUserPEBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 113 | FDTaxLineLastUpdatedByUserPECreatedBy13 | CREATED_BY | — | — |
| 114 | FDTaxLineLastUpdatedByUserPECreationDate13 | CREATION_DATE | — | — |
| 115 | FDTaxLineLastUpdatedByUserPECredentialsEmailSent3 | CREDENTIALS_EMAIL_SENT | — | — |
| 116 | FDTaxLineLastUpdatedByUserPEEndDate3 | END_DATE | — | — |
| 117 | FDTaxLineLastUpdatedByUserPEExternalId3 | EXTERNAL_ID | — | — |
| 118 | FDTaxLineLastUpdatedByUserPEHrTerminated3 | HR_TERMINATED | — | — |
| 119 | FDTaxLineLastUpdatedByUserPELastUpdateDate13 | LAST_UPDATE_DATE | — | — |
| 120 | FDTaxLineLastUpdatedByUserPELastUpdateLogin13 | LAST_UPDATE_LOGIN | — | — |
| 121 | FDTaxLineLastUpdatedByUserPELastUpdatedBy13 | LAST_UPDATED_BY | — | — |
| 122 | FDTaxLineLastUpdatedByUserPEMultitenancyUsername3 | MULTITENANCY_USERNAME | — | — |
| 123 | FDTaxLineLastUpdatedByUserPEObjectVersionNumber11 | OBJECT_VERSION_NUMBER | — | — |
| 124 | FDTaxLineLastUpdatedByUserPEPartyId3 | PARTY_ID | — | — |
| 125 | FDTaxLineLastUpdatedByUserPEPersonId3 | PERSON_ID | — | — |
| 126 | FDTaxLineLastUpdatedByUserPEStartDate3 | START_DATE | — | — |
| 127 | FDTaxLineLastUpdatedByUserPESuspended3 | SUSPENDED | — | — |
| 128 | FDTaxLineLastUpdatedByUserPEUserDataChecksum3 | USER_DATA_CHECKSUM | — | — |
| 129 | FDTaxLineLastUpdatedByUserPEUserDistinguishedName3 | USER_DISTINGUISHED_NAME | — | — |
| 130 | FDTaxLineLastUpdatedByUserPEUserGuid3 | USER_GUID | — | — |
| 131 | FDTaxLineLastUpdatedByUserPEUserId3 | USER_ID | — | — |
| 132 | FDTaxLineLastUpdatedByUserPEUsername3 | USERNAME | — | — |
| 133 | HeaderExtnEOtoCreatedByUserPActiveFlag | ACTIVE_FLAG | — | — |
| 134 | HeaderExtnEOtoCreatedByUserPBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 135 | HeaderExtnEOtoCreatedByUserPCreatedBy | CREATED_BY | — | — |
| 136 | HeaderExtnEOtoCreatedByUserPCreationDate | CREATION_DATE | — | — |
| 137 | HeaderExtnEOtoCreatedByUserPCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 138 | HeaderExtnEOtoCreatedByUserPEndDate | END_DATE | — | — |
| 139 | HeaderExtnEOtoCreatedByUserPExternalId | EXTERNAL_ID | — | — |
| 140 | HeaderExtnEOtoCreatedByUserPHrTerminated | HR_TERMINATED | — | — |
| 141 | HeaderExtnEOtoCreatedByUserPLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 142 | HeaderExtnEOtoCreatedByUserPLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 143 | HeaderExtnEOtoCreatedByUserPLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 144 | HeaderExtnEOtoCreatedByUserPMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 145 | HeaderExtnEOtoCreatedByUserPObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 146 | HeaderExtnEOtoCreatedByUserPPartyId | PARTY_ID | — | — |
| 147 | HeaderExtnEOtoCreatedByUserPPersonId | PERSON_ID | — | — |
| 148 | HeaderExtnEOtoCreatedByUserPStartDate | START_DATE | — | — |
| 149 | HeaderExtnEOtoCreatedByUserPSuspended | SUSPENDED | — | — |
| 150 | HeaderExtnEOtoCreatedByUserPUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 151 | HeaderExtnEOtoCreatedByUserPUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 152 | HeaderExtnEOtoCreatedByUserPUserGuid | USER_GUID | — | — |
| 153 | HeaderExtnEOtoCreatedByUserPUserId | USER_ID | — | — |
| 154 | HeaderExtnEOtoCreatedByUserPUsername | USERNAME | — | — |
| 155 | HeaderExtnToLastUpdtdUserPEOActiveFlag1 | ACTIVE_FLAG | — | — |
| 156 | HeaderExtnToLastUpdtdUserPEOBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 157 | HeaderExtnToLastUpdtdUserPEOCreatedBy1 | CREATED_BY | — | — |
| 158 | HeaderExtnToLastUpdtdUserPEOCreationDate1 | CREATION_DATE | — | — |
| 159 | HeaderExtnToLastUpdtdUserPEOCredentialsEmailSent1 | CREDENTIALS_EMAIL_SENT | — | — |
| 160 | HeaderExtnToLastUpdtdUserPEOEndDate1 | END_DATE | — | — |
| 161 | HeaderExtnToLastUpdtdUserPEOExternalId1 | EXTERNAL_ID | — | — |
| 162 | HeaderExtnToLastUpdtdUserPEOHrTerminated1 | HR_TERMINATED | — | — |
| 163 | HeaderExtnToLastUpdtdUserPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 164 | HeaderExtnToLastUpdtdUserPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 165 | HeaderExtnToLastUpdtdUserPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 166 | HeaderExtnToLastUpdtdUserPEOMultitenancyUsername1 | MULTITENANCY_USERNAME | — | — |
| 167 | HeaderExtnToLastUpdtdUserPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 168 | HeaderExtnToLastUpdtdUserPEOPartyId1 | PARTY_ID | — | — |
| 169 | HeaderExtnToLastUpdtdUserPEOPersonId1 | PERSON_ID | — | — |
| 170 | HeaderExtnToLastUpdtdUserPEOStartDate1 | START_DATE | — | — |
| 171 | HeaderExtnToLastUpdtdUserPEOSuspended1 | SUSPENDED | — | — |
| 172 | HeaderExtnToLastUpdtdUserPEOUserDataChecksum1 | USER_DATA_CHECKSUM | — | — |
| 173 | HeaderExtnToLastUpdtdUserPEOUserDistinguishedName1 | USER_DISTINGUISHED_NAME | — | — |
| 174 | HeaderExtnToLastUpdtdUserPEOUserGuid1 | USER_GUID | — | — |
| 175 | HeaderExtnToLastUpdtdUserPEOUserId1 | USER_ID | — | — |
| 176 | HeaderExtnToLastUpdtdUserPEOUsername1 | USERNAME | — | — |

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
| 73 | RcvShipmentHeadersShipmentNum | SHIPMENT_NUM | — | — |
| 74 | RcvShipmentHeadersShippedDate | SHIPPED_DATE | — | — |
| 75 | RcvShipmentHeadersSpecialHandlingCode | SPECIAL_HANDLING_CODE | — | — |
| 76 | RcvShipmentHeadersTarWeight | TAR_WEIGHT | — | — |
| 77 | RcvShipmentHeadersTarWeightUomCode | TAR_WEIGHT_UOM_CODE | — | — |
| 78 | RcvShipmentHeadersTaxAmount | TAX_AMOUNT | — | — |
| 79 | RcvShipmentHeadersTaxName | TAX_NAME | — | — |
| 80 | RcvShipmentHeadersVendorId | VENDOR_ID | — | — |
| 81 | RcvShipmentHeadersVendorSiteId | VENDOR_SITE_ID | — | — |
| 82 | RcvShipmentHeadersWaybillAirbillNum | WAYBILL_AIRBILL_NUM | — | — |

### [[zx_fc_intended_use_v|ZX_FC_INTENDED_USE_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LineIntendedUsePEOClassificationId | CLASSIFICATION_ID | — | — |
| 2 | LineIntendedUsePEOCode | CODE | — | — |
| 3 | LineIntendedUsePEOCountryCode1 | COUNTRY_CODE | — | — |
| 4 | LineIntendedUsePEOEffectiveFrom | EFFECTIVE_FROM | — | — |
| 5 | LineIntendedUsePEOEffectiveTo | EFFECTIVE_TO | — | — |
| 6 | LineIntendedUsePEOName1 | NAME | — | ✅ |

### [[zx_fc_product_categories_v|ZX_FC_PRODUCT_CATEGORIES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProductCategoriesPEOClassificationCode1 | CLASSIFICATION_CODE | — | — |
| 2 | ProductCategoriesPEOClassificationId1 | CLASSIFICATION_ID | — | — |
| 3 | ProductCategoriesPEOClassificationName1 | CLASSIFICATION_NAME | — | ✅ |
| 4 | ProductCategoriesPEOConcatLeafCode | CONCAT_LEAF_CODE | — | — |
| 5 | ProductCategoriesPEOConcatLeafName | CONCAT_LEAF_NAME | — | — |
| 6 | ProductCategoriesPEOCountryCode3 | COUNTRY_CODE | — | — |
| 7 | ProductCategoriesPEOEffectiveFrom2 | EFFECTIVE_FROM | — | — |
| 8 | ProductCategoriesPEOEffectiveTo2 | EFFECTIVE_TO | — | — |

### [[zx_fc_product_fiscal_v|ZX_FC_PRODUCT_FISCAL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProductFiscClassificationsPE1CategoryId | CATEGORY_ID | — | — |
| 2 | ProductFiscClassificationsPE1CategorySetId | CATEGORY_SET_ID | — | — |
| 3 | ProductFiscClassificationsPE1ClassificationCode2 | CLASSIFICATION_CODE | — | — |
| 4 | ProductFiscClassificationsPE1ClassificationName2 | CLASSIFICATION_NAME | — | ✅ |
| 5 | ProductFiscClassificationsPE1CountryCode4 | COUNTRY_CODE | — | — |
| 6 | ProductFiscClassificationsPE1EffectiveTo3 | EFFECTIVE_TO | — | — |
| 7 | ProductFiscClassificationsPE1StructureId | STRUCTURE_ID | — | — |
| 8 | ProductFiscClassificationsPE1StructureName | STRUCTURE_NAME | — | — |

### [[zx_fc_user_defined_v|ZX_FC_USER_DEFINED_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserDefinedFiscClassPEOClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | UserDefinedFiscClassPEOClassificationName | CLASSIFICATION_NAME | — | ✅ |
| 3 | UserDefinedFiscClassPEOCountryCode2 | COUNTRY_CODE | — | — |
| 4 | UserDefinedFiscClassPEOEffectiveFrom1 | EFFECTIVE_FROM | — | — |
| 5 | UserDefinedFiscClassPEOEffectiveTo1 | EFFECTIVE_TO | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
