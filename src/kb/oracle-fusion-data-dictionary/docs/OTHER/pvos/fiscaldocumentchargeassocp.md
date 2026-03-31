---
id: DOC-OTHER-PVO-FiscalDocumentChargeAssocP
doc_type: system-doc
title: "FiscalDocumentChargeAssocP — PVO Cross-Module"
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
  - FiscalDocumentChargeAssocP
  - fiscaldocumentchargeassocp
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FiscalDocumentChargeAssocP

## 📌 Visão Geral

View Object para extração BICC de dados de Fiscal Document Charge Assoc P. Acessa as tabelas: AP_INVOICES_ALL, AP_PAYMENT_SCHEDULES_ALL, CMF_FD_IN_CONVERT_CFOPS_V (+25).

**Caminho:** `FscmTopModelAM.FiscalDocumentAM.FiscalDocumentChargeAssocP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 1382 | 28 | 1 | 18 | 1% |

---

## 🔗 Tabelas Relacionadas

- [[ap_invoices_all|AP_INVOICES_ALL]] — 163 atributos
- [[ap_payment_schedules_all|AP_PAYMENT_SCHEDULES_ALL]] — 5 atributos
- [[cmf_fd_in_convert_cfops_v|CMF_FD_IN_CONVERT_CFOPS_V]] — 2 atributos
- [[cmf_fd_loc_info_persist_otbi_v|CMF_FD_LOC_INFO_PERSIST_OTBI_V]] — 79 atributos
- [[cmf_fd_out_origin_cfops_v|CMF_FD_OUT_ORIGIN_CFOPS_V]] — 2 atributos
- [[cmf_fiscal_doc_charges|CMF_FISCAL_DOC_CHARGES]] — 24 atributos (7 BICC)
- [[cmf_fiscal_doc_charge_assoc|CMF_FISCAL_DOC_CHARGE_ASSOC]] — 20 atributos (1 PKs, 6 BICC)
- [[cmf_fiscal_doc_headers|CMF_FISCAL_DOC_HEADERS]] — 61 atributos
- [[cmf_fiscal_doc_inv_org_v|CMF_FISCAL_DOC_INV_ORG_V]] — 5 atributos
- [[cmf_fiscal_doc_lines_vl|CMF_FISCAL_DOC_LINES_VL]] — 48 atributos (3 BICC)
- [[cmf_fiscal_proc_options|CMF_FISCAL_PROC_OPTIONS]] — 56 atributos
- [[cml_charges_vl|CML_CHARGES_VL]] — 13 atributos (2 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 21 atributos
- [[gl_ledgers|GL_LEDGERS]] — 87 atributos
- [[inv_cons_advice_headers|INV_CONS_ADVICE_HEADERS]] — 24 atributos
- [[inv_units_of_measure_vl|INV_UNITS_OF_MEASURE_VL]] — 67 atributos
- [[jg_fscl_hdrs_atrb_ext_all|JG_FSCL_HDRS_ATRB_EXT_ALL]] — 55 atributos
- [[jg_fscl_hdr_dtls_atrb_ext_all|JG_FSCL_HDR_DTLS_ATRB_EXT_ALL]] — 18 atributos
- [[jg_fscl_lines_atrb_ext_all|JG_FSCL_LINES_ATRB_EXT_ALL]] — 23 atributos
- [[jg_fscl_ln_dtls_atrb_ext_all|JG_FSCL_LN_DTLS_ATRB_EXT_ALL]] — 20 atributos
- [[jg_fscl_tax_lines_all|JG_FSCL_TAX_LINES_ALL]] — 72 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 232 atributos
- [[per_users|PER_USERS]] — 176 atributos
- [[rcv_shipment_headers|RCV_SHIPMENT_HEADERS]] — 82 atributos
- [[zx_fc_intended_use_v|ZX_FC_INTENDED_USE_V]] — 6 atributos
- [[zx_fc_product_categories_v|ZX_FC_PRODUCT_CATEGORIES_V]] — 8 atributos
- [[zx_fc_product_fiscal_v|ZX_FC_PRODUCT_FISCAL_V]] — 8 atributos
- [[zx_fc_user_defined_v|ZX_FC_USER_DEFINED_V]] — 5 atributos

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
| 1 | FiscalDocInBoundCFOPPEOClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | FiscalDocInBoundCFOPPEOClassificationName | CLASSIFICATION_NAME | — | — |

### [[cmf_fd_loc_info_persist_otbi_v|CMF_FD_LOC_INFO_PERSIST_OTBI_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocLocInfoPersistPEODocumentHeaderId3 | DOCUMENT_HEADER_ID | — | — |
| 2 | FiscalDocLocInfoPersistPEODocumentNumber1 | DOCUMENT_NUMBER | — | — |
| 3 | FiscalDocLocInfoPersistPEOFiscalProcOptionsId1 | FISCAL_PROC_OPTIONS_ID | — | — |
| 4 | FiscalDocLocInfoPersistPEOIssuerCustomerFormTaxNum | ISSUER_CUSTOMER_FORM_TAX_NUM | — | — |
| 5 | FiscalDocLocInfoPersistPEOIssuerCustomerLocationId | ISSUER_CUSTOMER_LOCATION_ID | — | — |
| 6 | FiscalDocLocInfoPersistPEOIssuerCustomerPartyId | ISSUER_CUSTOMER_PARTY_ID | — | — |
| 7 | FiscalDocLocInfoPersistPEOIssuerCustomerPartySiteId | ISSUER_CUSTOMER_PARTY_SITE_ID | — | — |
| 8 | FiscalDocLocInfoPersistPEOIssuerCustomerTaxId | ISSUER_CUSTOMER_TAX_ID | — | — |
| 9 | FiscalDocLocInfoPersistPEOIssuerCustomerTaxpayerId | ISSUER_CUSTOMER_TAXPAYER_ID | — | — |
| 10 | FiscalDocLocInfoPersistPEOIssuerLeFormTaxNumber | ISSUER_LE_FORM_TAX_NUMBER | — | — |
| 11 | FiscalDocLocInfoPersistPEOIssuerLeId | ISSUER_LE_ID | — | — |
| 12 | FiscalDocLocInfoPersistPEOIssuerLeLocationId | ISSUER_LE_LOCATION_ID | — | — |
| 13 | FiscalDocLocInfoPersistPEOIssuerLeSiteId | ISSUER_LE_SITE_ID | — | — |
| 14 | FiscalDocLocInfoPersistPEOIssuerLeTaxId | ISSUER_LE_TAX_ID | — | — |
| 15 | FiscalDocLocInfoPersistPEOIssuerLeTaxpayerId | ISSUER_LE_TAXPAYER_ID | — | — |
| 16 | FiscalDocLocInfoPersistPEOIssuerSupplierFormTaxNum | ISSUER_SUPPLIER_FORM_TAX_NUM | — | — |
| 17 | FiscalDocLocInfoPersistPEOIssuerSupplierLocationId | ISSUER_SUPPLIER_LOCATION_ID | — | — |
| 18 | FiscalDocLocInfoPersistPEOIssuerSupplierPartyId | ISSUER_SUPPLIER_PARTY_ID | — | — |
| 19 | FiscalDocLocInfoPersistPEOIssuerSupplierPartySiteId | ISSUER_SUPPLIER_PARTY_SITE_ID | — | — |
| 20 | FiscalDocLocInfoPersistPEOIssuerSupplierTaxId | ISSUER_SUPPLIER_TAX_ID | — | — |
| 21 | FiscalDocLocInfoPersistPEOIssuerSupplierTaxpayerId | ISSUER_SUPPLIER_TAXPAYER_ID | — | — |
| 22 | FiscalDocLocInfoPersistPEOIssuerType | ISSUER_TYPE | — | — |
| 23 | FiscalDocLocInfoPersistPEOReceiverCustPartySiteId | RECEIVER_CUST_PARTY_SITE_ID | — | — |
| 24 | FiscalDocLocInfoPersistPEOReceiverCustomerFormTaxNum | RECEIVER_CUSTOMER_FORM_TAX_NUM | — | — |
| 25 | FiscalDocLocInfoPersistPEOReceiverCustomerLocationId | RECEIVER_CUSTOMER_LOCATION_ID | — | — |
| 26 | FiscalDocLocInfoPersistPEOReceiverCustomerPartyId | RECEIVER_CUSTOMER_PARTY_ID | — | — |
| 27 | FiscalDocLocInfoPersistPEOReceiverCustomerTaxId | RECEIVER_CUSTOMER_TAX_ID | — | — |
| 28 | FiscalDocLocInfoPersistPEOReceiverCustomerTaxpayerId | RECEIVER_CUSTOMER_TAXPAYER_ID | — | — |
| 29 | FiscalDocLocInfoPersistPEOReceiverLeFormTaxNumber | RECEIVER_LE_FORM_TAX_NUMBER | — | — |
| 30 | FiscalDocLocInfoPersistPEOReceiverLeLocationId | RECEIVER_LE_LOCATION_ID | — | — |
| 31 | FiscalDocLocInfoPersistPEOReceiverLePartyId | RECEIVER_LE_PARTY_ID | — | — |
| 32 | FiscalDocLocInfoPersistPEOReceiverLePartySiteId | RECEIVER_LE_PARTY_SITE_ID | — | — |
| 33 | FiscalDocLocInfoPersistPEOReceiverLeTaxId | RECEIVER_LE_TAX_ID | — | — |
| 34 | FiscalDocLocInfoPersistPEOReceiverLeTaxpayerId | RECEIVER_LE_TAXPAYER_ID | — | — |
| 35 | FiscalDocLocInfoPersistPEOReceiverSuppPartySiteId | RECEIVER_SUPP_PARTY_SITE_ID | — | — |
| 36 | FiscalDocLocInfoPersistPEOReceiverSupplierFormTaxNum | RECEIVER_SUPPLIER_FORM_TAX_NUM | — | — |
| 37 | FiscalDocLocInfoPersistPEOReceiverSupplierLocationId | RECEIVER_SUPPLIER_LOCATION_ID | — | — |
| 38 | FiscalDocLocInfoPersistPEOReceiverSupplierPartyId | RECEIVER_SUPPLIER_PARTY_ID | — | — |
| 39 | FiscalDocLocInfoPersistPEOReceiverSupplierTaxId | RECEIVER_SUPPLIER_TAX_ID | — | — |
| 40 | FiscalDocLocInfoPersistPEOReceiverSupplierTaxpayerId | RECEIVER_SUPPLIER_TAXPAYER_ID | — | — |
| 41 | FiscalDocLocInfoPersistPEOReceiverType | RECEIVER_TYPE | — | — |
| 42 | FiscalDocLocInfoPersistPEOShipfromCustPartySiteId | SHIPFROM_CUST_PARTY_SITE_ID | — | — |
| 43 | FiscalDocLocInfoPersistPEOShipfromCustomerFormTaxNum | SHIPFROM_CUSTOMER_FORM_TAX_NUM | — | — |
| 44 | FiscalDocLocInfoPersistPEOShipfromCustomerLocationId | SHIPFROM_CUSTOMER_LOCATION_ID | — | — |
| 45 | FiscalDocLocInfoPersistPEOShipfromCustomerPartyId | SHIPFROM_CUSTOMER_PARTY_ID | — | — |
| 46 | FiscalDocLocInfoPersistPEOShipfromCustomerTaxId | SHIPFROM_CUSTOMER_TAX_ID | — | — |
| 47 | FiscalDocLocInfoPersistPEOShipfromCustomerTaxpayerId | SHIPFROM_CUSTOMER_TAXPAYER_ID | — | — |
| 48 | FiscalDocLocInfoPersistPEOShipfromLeFormTaxNumber | SHIPFROM_LE_FORM_TAX_NUMBER | — | — |
| 49 | FiscalDocLocInfoPersistPEOShipfromLeLocationId | SHIPFROM_LE_LOCATION_ID | — | — |
| 50 | FiscalDocLocInfoPersistPEOShipfromLePartyId | SHIPFROM_LE_PARTY_ID | — | — |
| 51 | FiscalDocLocInfoPersistPEOShipfromLePartySiteId | SHIPFROM_LE_PARTY_SITE_ID | — | — |
| 52 | FiscalDocLocInfoPersistPEOShipfromLeTaxId | SHIPFROM_LE_TAX_ID | — | — |
| 53 | FiscalDocLocInfoPersistPEOShipfromLeTaxpayerId | SHIPFROM_LE_TAXPAYER_ID | — | — |
| 54 | FiscalDocLocInfoPersistPEOShipfromSuppPartySiteId | SHIPFROM_SUPP_PARTY_SITE_ID | — | — |
| 55 | FiscalDocLocInfoPersistPEOShipfromSupplierFormTaxNum | SHIPFROM_SUPPLIER_FORM_TAX_NUM | — | — |
| 56 | FiscalDocLocInfoPersistPEOShipfromSupplierLocationId | SHIPFROM_SUPPLIER_LOCATION_ID | — | — |
| 57 | FiscalDocLocInfoPersistPEOShipfromSupplierPartyId | SHIPFROM_SUPPLIER_PARTY_ID | — | — |
| 58 | FiscalDocLocInfoPersistPEOShipfromSupplierTaxId | SHIPFROM_SUPPLIER_TAX_ID | — | — |
| 59 | FiscalDocLocInfoPersistPEOShipfromSupplierTaxpayerId | SHIPFROM_SUPPLIER_TAXPAYER_ID | — | — |
| 60 | FiscalDocLocInfoPersistPEOShipfromType | SHIPFROM_TYPE | — | — |
| 61 | FiscalDocLocInfoPersistPEOShiptoCustPartySiteId | SHIPTO_CUST_PARTY_SITE_ID | — | — |
| 62 | FiscalDocLocInfoPersistPEOShiptoCustomerFormTaxNum | SHIPTO_CUSTOMER_FORM_TAX_NUM | — | — |
| 63 | FiscalDocLocInfoPersistPEOShiptoCustomerLocationId | SHIPTO_CUSTOMER_LOCATION_ID | — | — |
| 64 | FiscalDocLocInfoPersistPEOShiptoCustomerPartyId | SHIPTO_CUSTOMER_PARTY_ID | — | — |
| 65 | FiscalDocLocInfoPersistPEOShiptoCustomerTaxId | SHIPTO_CUSTOMER_TAX_ID | — | — |
| 66 | FiscalDocLocInfoPersistPEOShiptoCustomerTaxpayerId | SHIPTO_CUSTOMER_TAXPAYER_ID | — | — |
| 67 | FiscalDocLocInfoPersistPEOShiptoLeFormTaxNumber | SHIPTO_LE_FORM_TAX_NUMBER | — | — |
| 68 | FiscalDocLocInfoPersistPEOShiptoLeLocationId | SHIPTO_LE_LOCATION_ID | — | — |
| 69 | FiscalDocLocInfoPersistPEOShiptoLePartyId | SHIPTO_LE_PARTY_ID | — | — |
| 70 | FiscalDocLocInfoPersistPEOShiptoLePartySiteId | SHIPTO_LE_PARTY_SITE_ID | — | — |
| 71 | FiscalDocLocInfoPersistPEOShiptoLeTaxId | SHIPTO_LE_TAX_ID | — | — |
| 72 | FiscalDocLocInfoPersistPEOShiptoLeTaxpayerId | SHIPTO_LE_TAXPAYER_ID | — | — |
| 73 | FiscalDocLocInfoPersistPEOShiptoSuppPartySiteId | SHIPTO_SUPP_PARTY_SITE_ID | — | — |
| 74 | FiscalDocLocInfoPersistPEOShiptoSupplierFormTaxNum | SHIPTO_SUPPLIER_FORM_TAX_NUM | — | — |
| 75 | FiscalDocLocInfoPersistPEOShiptoSupplierLocationId | SHIPTO_SUPPLIER_LOCATION_ID | — | — |
| 76 | FiscalDocLocInfoPersistPEOShiptoSupplierPartyId | SHIPTO_SUPPLIER_PARTY_ID | — | — |
| 77 | FiscalDocLocInfoPersistPEOShiptoSupplierTaxId | SHIPTO_SUPPLIER_TAX_ID | — | — |
| 78 | FiscalDocLocInfoPersistPEOShiptoSupplierTaxpayerId | SHIPTO_SUPPLIER_TAXPAYER_ID | — | — |
| 79 | FiscalDocLocInfoPersistPEOShiptoType | SHIPTO_TYPE | — | — |

### [[cmf_fd_out_origin_cfops_v|CMF_FD_OUT_ORIGIN_CFOPS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocOutBoundCFOPPEOClassificationCode1 | CLASSIFICATION_CODE | — | — |
| 2 | FiscalDocOutBoundCFOPPEOClassificationName1 | CLASSIFICATION_NAME | — | — |

### [[cmf_fiscal_doc_charges|CMF_FISCAL_DOC_CHARGES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocumentChargesPEOAllocationBasis | ALLOCATION_BASIS | — | ✅ |
| 2 | FiscalDocumentChargesPEOAllocationUom | ALLOCATION_UOM | — | ✅ |
| 3 | FiscalDocumentChargesPEOAttributeCategory1 | ATTRIBUTE_CATEGORY | — | — |
| 4 | FiscalDocumentChargesPEOBasis | BASIS | — | ✅ |
| 5 | FiscalDocumentChargesPEOChargeAmount | CHARGE_AMOUNT | — | ✅ |
| 6 | FiscalDocumentChargesPEOChargeCode | CHARGE_CODE | — | — |
| 7 | FiscalDocumentChargesPEOChargeId | CHARGE_ID | — | — |
| 8 | FiscalDocumentChargesPEOChargeLineId1 | CHARGE_LINE_ID | — | — |
| 9 | FiscalDocumentChargesPEOChargeLineStatus | CHARGE_LINE_STATUS | — | ✅ |
| 10 | FiscalDocumentChargesPEOCreatedBy1 | CREATED_BY | — | — |
| 11 | FiscalDocumentChargesPEOCreationDate1 | CREATION_DATE | — | — |
| 12 | FiscalDocumentChargesPEODocumentHeaderId | DOCUMENT_HEADER_ID | — | — |
| 13 | FiscalDocumentChargesPEOExternalSystemRefId1 | EXTERNAL_SYSTEM_REF_ID | — | — |
| 14 | FiscalDocumentChargesPEOExternalSystemReference1 | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 15 | FiscalDocumentChargesPEOJobDefinitionName1 | JOB_DEFINITION_NAME | — | — |
| 16 | FiscalDocumentChargesPEOJobDefinitionPackage1 | JOB_DEFINITION_PACKAGE | — | — |
| 17 | FiscalDocumentChargesPEOLandedCostCharge | LANDED_COST_CHARGE | — | — |
| 18 | FiscalDocumentChargesPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 19 | FiscalDocumentChargesPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 20 | FiscalDocumentChargesPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 21 | FiscalDocumentChargesPEOLineNumber | LINE_NUMBER | — | ✅ |
| 22 | FiscalDocumentChargesPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 23 | FiscalDocumentChargesPEOPercentage | PERCENTAGE | — | ✅ |
| 24 | FiscalDocumentChargesPEORequestId1 | REQUEST_ID | — | — |

### [[cmf_fiscal_doc_charge_assoc|CMF_FISCAL_DOC_CHARGE_ASSOC]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChargeAssociationId | CHARGE_ASSOCIATION_ID | 🔑 | ✅ |
| 2 | FiscalDocumentChargeAssocPEOAllocatedAmount | ALLOCATED_AMOUNT | — | ✅ |
| 3 | FiscalDocumentChargeAssocPEOAllocationBaseValue | ALLOCATION_BASE_VALUE | — | ✅ |
| 4 | FiscalDocumentChargeAssocPEOAllocationPercentage | ALLOCATION_PERCENTAGE | — | ✅ |
| 5 | FiscalDocumentChargeAssocPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 6 | FiscalDocumentChargeAssocPEOChargeLineId | CHARGE_LINE_ID | — | — |
| 7 | FiscalDocumentChargeAssocPEOCreatedBy | CREATED_BY | — | — |
| 8 | FiscalDocumentChargeAssocPEOCreationDate | CREATION_DATE | — | — |
| 9 | FiscalDocumentChargeAssocPEODocumentLineId | DOCUMENT_LINE_ID | — | — |
| 10 | FiscalDocumentChargeAssocPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | — |
| 11 | FiscalDocumentChargeAssocPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 12 | FiscalDocumentChargeAssocPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 13 | FiscalDocumentChargeAssocPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 14 | FiscalDocumentChargeAssocPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | FiscalDocumentChargeAssocPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | FiscalDocumentChargeAssocPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | FiscalDocumentChargeAssocPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | FiscalDocumentChargeAssocPEORefDocumentHeaderId | REF_DOCUMENT_HEADER_ID | — | — |
| 19 | FiscalDocumentChargeAssocPEORequestId | REQUEST_ID | — | — |
| 20 | FiscalDocumentChargeAssocPEOVariablePercentage | VARIABLE_PERCENTAGE | — | ✅ |

### [[cmf_fiscal_doc_headers|CMF_FISCAL_DOC_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocHeadersPEOAccessKeyNumber | ACCESS_KEY_NUMBER | — | — |
| 2 | FiscalDocHeadersPEOAcknowledgedDate | ACKNOWLEDGED_DATE | — | — |
| 3 | FiscalDocHeadersPEOAttributeCategory3 | ATTRIBUTE_CATEGORY | — | — |
| 4 | FiscalDocHeadersPEOBillToBusinessUnitId | BILL_TO_BUSINESS_UNIT_ID | — | — |
| 5 | FiscalDocHeadersPEOChargeAllocationStatus | CHARGE_ALLOCATION_STATUS | — | — |
| 6 | FiscalDocHeadersPEOCmrInterfacedFlag | CMR_INTERFACED_FLAG | — | — |
| 7 | FiscalDocHeadersPEOConversionRate | CONVERSION_RATE | — | — |
| 8 | FiscalDocHeadersPEOConverstionType | CONVERSTION_TYPE | — | — |
| 9 | FiscalDocHeadersPEOCountryCode | COUNTRY_CODE | — | — |
| 10 | FiscalDocHeadersPEOCreatedBy3 | CREATED_BY | — | — |
| 11 | FiscalDocHeadersPEOCreationDate3 | CREATION_DATE | — | — |
| 12 | FiscalDocHeadersPEOCurrency | CURRENCY | — | — |
| 13 | FiscalDocHeadersPEODocumentHeaderId2 | DOCUMENT_HEADER_ID | — | — |
| 14 | FiscalDocHeadersPEODocumentNumber | DOCUMENT_NUMBER | — | — |
| 15 | FiscalDocHeadersPEODocumentStatus | DOCUMENT_STATUS | — | — |
| 16 | FiscalDocHeadersPEODocumentType | DOCUMENT_TYPE | — | — |
| 17 | FiscalDocHeadersPEOExternalSystemRefId3 | EXTERNAL_SYSTEM_REF_ID | — | — |
| 18 | FiscalDocHeadersPEOExternalSystemReference3 | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 19 | FiscalDocHeadersPEOFiscalDocAssoctnsId | FISCAL_DOC_ASSOCTNS_ID | — | — |
| 20 | FiscalDocHeadersPEOFiscalProcOptionsId | FISCAL_PROC_OPTIONS_ID | — | — |
| 21 | FiscalDocHeadersPEOInterfacedFlag | INTERFACED_FLAG | — | — |
| 22 | FiscalDocHeadersPEOInvoiceInterfacedFlag | INVOICE_INTERFACED_FLAG | — | — |
| 23 | FiscalDocHeadersPEOIssueDate | ISSUE_DATE | — | — |
| 24 | FiscalDocHeadersPEOIssuerLocationId | ISSUER_LOCATION_ID | — | — |
| 25 | FiscalDocHeadersPEOIssuerPartyId | ISSUER_PARTY_ID | — | — |
| 26 | FiscalDocHeadersPEOIssuerPartySiteId | ISSUER_PARTY_SITE_ID | — | — |
| 27 | FiscalDocHeadersPEOIssuerTaxId | ISSUER_TAX_ID | — | — |
| 28 | FiscalDocHeadersPEOItemLineAmount | ITEM_LINE_AMOUNT | — | — |
| 29 | FiscalDocHeadersPEOJobDefinitionName3 | JOB_DEFINITION_NAME | — | — |
| 30 | FiscalDocHeadersPEOJobDefinitionPackage3 | JOB_DEFINITION_PACKAGE | — | — |
| 31 | FiscalDocHeadersPEOLastUpdateDate3 | LAST_UPDATE_DATE | — | — |
| 32 | FiscalDocHeadersPEOLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 33 | FiscalDocHeadersPEOLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 34 | FiscalDocHeadersPEOModel | MODEL | — | — |
| 35 | FiscalDocHeadersPEOObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 36 | FiscalDocHeadersPEOOperationType | OPERATION_TYPE | — | — |
| 37 | FiscalDocHeadersPEOParentDocumentHeaderId | PARENT_DOCUMENT_HEADER_ID | — | — |
| 38 | FiscalDocHeadersPEOReason | REASON | — | — |
| 39 | FiscalDocHeadersPEOReceiverLocationId | RECEIVER_LOCATION_ID | — | — |
| 40 | FiscalDocHeadersPEOReceiverPartyId | RECEIVER_PARTY_ID | — | — |
| 41 | FiscalDocHeadersPEOReceiverPartySiteId | RECEIVER_PARTY_SITE_ID | — | — |
| 42 | FiscalDocHeadersPEOReceiverTaxId | RECEIVER_TAX_ID | — | — |
| 43 | FiscalDocHeadersPEOReferencedStatus | REFERENCED_STATUS | — | — |
| 44 | FiscalDocHeadersPEORequestId3 | REQUEST_ID | — | — |
| 45 | FiscalDocHeadersPEOSchedulesAllocatedFlag | SCHEDULES_ALLOCATED_FLAG | — | — |
| 46 | FiscalDocHeadersPEOSeries | SERIES | — | — |
| 47 | FiscalDocHeadersPEOShipfromLocationId | SHIPFROM_LOCATION_ID | — | — |
| 48 | FiscalDocHeadersPEOShipfromPartyId | SHIPFROM_PARTY_ID | — | — |
| 49 | FiscalDocHeadersPEOShipfromPartySiteId | SHIPFROM_PARTY_SITE_ID | — | — |
| 50 | FiscalDocHeadersPEOShipfromTaxId | SHIPFROM_TAX_ID | — | — |
| 51 | FiscalDocHeadersPEOShiptoLocationId | SHIPTO_LOCATION_ID | — | — |
| 52 | FiscalDocHeadersPEOShiptoPartyId | SHIPTO_PARTY_ID | — | — |
| 53 | FiscalDocHeadersPEOShiptoPartySiteId | SHIPTO_PARTY_SITE_ID | — | — |
| 54 | FiscalDocHeadersPEOShiptoTaxId | SHIPTO_TAX_ID | — | — |
| 55 | FiscalDocHeadersPEOSoldToLegalEntityId | SOLD_TO_LEGAL_ENTITY_ID | — | — |
| 56 | FiscalDocHeadersPEOSourceDocumentType1 | SOURCE_DOCUMENT_TYPE | — | — |
| 57 | FiscalDocHeadersPEOSourceRefDocHeaderId | SOURCE_REF_DOC_HEADER_ID | — | — |
| 58 | FiscalDocHeadersPEOSubseries | SUBSERIES | — | — |
| 59 | FiscalDocHeadersPEOTaxCalculationStatus | TAX_CALCULATION_STATUS | — | — |
| 60 | FiscalDocHeadersPEOTotalAmount | TOTAL_AMOUNT | — | — |
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
| 1 | FiscalDocumentLinesPEOAttributeCategory2 | ATTRIBUTE_CATEGORY | — | — |
| 2 | FiscalDocumentLinesPEOChargesAmount | CHARGES_AMOUNT | — | — |
| 3 | FiscalDocumentLinesPEOCreatedBy2 | CREATED_BY | — | — |
| 4 | FiscalDocumentLinesPEOCreationDate2 | CREATION_DATE | — | — |
| 5 | FiscalDocumentLinesPEODistCodeCombinationId | DIST_CODE_COMBINATION_ID | — | — |
| 6 | FiscalDocumentLinesPEODocumentHeaderId1 | DOCUMENT_HEADER_ID | — | — |
| 7 | FiscalDocumentLinesPEODocumentLineId1 | DOCUMENT_LINE_ID | — | — |
| 8 | FiscalDocumentLinesPEOEfdItemCode | EFD_ITEM_CODE | — | ✅ |
| 9 | FiscalDocumentLinesPEOEfdItemDescription | EFD_ITEM_DESCRIPTION | — | ✅ |
| 10 | FiscalDocumentLinesPEOEfdProdAddInfo | EFD_PROD_ADD_INFO | — | ✅ |
| 11 | FiscalDocumentLinesPEOExternalSystemRefId2 | EXTERNAL_SYSTEM_REF_ID | — | — |
| 12 | FiscalDocumentLinesPEOExternalSystemReference2 | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 13 | FiscalDocumentLinesPEOFciControlNumber | FCI_CONTROL_NUMBER | — | — |
| 14 | FiscalDocumentLinesPEOFdAmount | FD_AMOUNT | — | — |
| 15 | FiscalDocumentLinesPEOFdConvertedCfop | FD_CONVERTED_CFOP | — | — |
| 16 | FiscalDocumentLinesPEOFdOriginalCfop | FD_ORIGINAL_CFOP | — | — |
| 17 | FiscalDocumentLinesPEOFdPrice | FD_PRICE | — | — |
| 18 | FiscalDocumentLinesPEOFdQuantity | FD_QUANTITY | — | — |
| 19 | FiscalDocumentLinesPEOFdUom | FD_UOM | — | — |
| 20 | FiscalDocumentLinesPEOFiscalClassification | FISCAL_CLASSIFICATION | — | — |
| 21 | FiscalDocumentLinesPEOFreightModal | FREIGHT_MODAL | — | — |
| 22 | FiscalDocumentLinesPEOIntendedUseId | INTENDED_USE_ID | — | — |
| 23 | FiscalDocumentLinesPEOItemDescription | ITEM_DESCRIPTION | — | — |
| 24 | FiscalDocumentLinesPEOItemId | ITEM_ID | — | — |
| 25 | FiscalDocumentLinesPEOJobDefinitionName2 | JOB_DEFINITION_NAME | — | — |
| 26 | FiscalDocumentLinesPEOJobDefinitionPackage2 | JOB_DEFINITION_PACKAGE | — | — |
| 27 | FiscalDocumentLinesPEOLastUpdateDate2 | LAST_UPDATE_DATE | — | — |
| 28 | FiscalDocumentLinesPEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 29 | FiscalDocumentLinesPEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 30 | FiscalDocumentLinesPEOLineNumber1 | LINE_NUMBER | — | — |
| 31 | FiscalDocumentLinesPEOLineStatus | LINE_STATUS | — | — |
| 32 | FiscalDocumentLinesPEOLineType | LINE_TYPE | — | — |
| 33 | FiscalDocumentLinesPEONonRecoverableTax | NON_RECOVERABLE_TAX | — | — |
| 34 | FiscalDocumentLinesPEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 35 | FiscalDocumentLinesPEOPhysicalReceiptDate | PHYSICAL_RECEIPT_DATE | — | — |
| 36 | FiscalDocumentLinesPEOPhysicalReceiptQuantity | PHYSICAL_RECEIPT_QUANTITY | — | — |
| 37 | FiscalDocumentLinesPEOPhysicalReceiptUom | PHYSICAL_RECEIPT_UOM | — | — |
| 38 | FiscalDocumentLinesPEOProductCategory | PRODUCT_CATEGORY | — | — |
| 39 | FiscalDocumentLinesPEOProductFiscalClassifId | PRODUCT_FISCAL_CLASSIF_ID | — | — |
| 40 | FiscalDocumentLinesPEORecoverablesTax | RECOVERABLES_TAX | — | — |
| 41 | FiscalDocumentLinesPEORefDocumentHeaderId1 | REF_DOCUMENT_HEADER_ID | — | — |
| 42 | FiscalDocumentLinesPEORefDocumentLineId | REF_DOCUMENT_LINE_ID | — | — |
| 43 | FiscalDocumentLinesPEORefFdDocumentType | REF_FD_DOCUMENT_TYPE | — | — |
| 44 | FiscalDocumentLinesPEOReqBuId | REQ_BU_ID | — | — |
| 45 | FiscalDocumentLinesPEORequestId2 | REQUEST_ID | — | — |
| 46 | FiscalDocumentLinesPEOScheduleSrcDocType | SCHEDULE_SRC_DOC_TYPE | — | — |
| 47 | FiscalDocumentLinesPEOSourceDocBuId | SOURCE_DOC_BU_ID | — | — |
| 48 | FiscalDocumentLinesPEOSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |

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

### [[cml_charges_vl|CML_CHARGES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChargePEOAutoTaxCalculation | AUTO_TAX_CALCULATION | — | — |
| 2 | ChargePEOChargeCode1 | CHARGE_CODE | — | ✅ |
| 3 | ChargePEOChargeDesc | CHARGE_DESC | — | — |
| 4 | ChargePEOChargeId1 | CHARGE_ID | — | — |
| 5 | ChargePEODefaultAccrualOption | DEFAULT_ACCRUAL_OPTION | — | — |
| 6 | ChargePEODefaultAllocBasisCode | DEFAULT_ALLOC_BASIS_CODE | — | — |
| 7 | ChargePEODefaultAllocBasisUomCode | DEFAULT_ALLOC_BASIS_UOM_CODE | — | — |
| 8 | ChargePEOIsSeed | IS_SEED | — | — |
| 9 | ChargePEOName | NAME | — | ✅ |
| 10 | ChargePEOSetId | SET_ID | — | — |
| 11 | ChargePEOTaxApplicableFlag | TAX_APPLICABLE_FLAG | — | — |
| 12 | ChargePEOTaxType | TAX_TYPE | — | — |
| 13 | ChargePEOTrackMissingInvoicesFlag | TRACK_MISSING_INVOICES_FLAG | — | — |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOBusinessUnitId | BU_ID | — | — |
| 2 | BusinessUnitPEOCreatedBy8 | CREATED_BY | — | — |
| 3 | BusinessUnitPEOCreationDate8 | CREATION_DATE | — | — |
| 4 | BusinessUnitPEODateFrom | DATE_FROM | — | — |
| 5 | BusinessUnitPEODateTo | DATE_TO | — | — |
| 6 | BusinessUnitPEODefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | — |
| 7 | BusinessUnitPEODefaultSetId | DEFAULT_SET_ID | — | — |
| 8 | BusinessUnitPEOEnabledForHrFlag | ENABLED_FOR_HR_FLAG | — | — |
| 9 | BusinessUnitPEOEnterpriseId | BUSINESS_GROUP_ID | — | — |
| 10 | BusinessUnitPEOFinancialsBusinessUnitId | FIN_BUSINESS_UNIT_ID | — | — |
| 11 | BusinessUnitPEOLastUpdateDate8 | LAST_UPDATE_DATE | — | — |
| 12 | BusinessUnitPEOLastUpdateLogin8 | LAST_UPDATE_LOGIN | — | — |
| 13 | BusinessUnitPEOLastUpdatedBy8 | LAST_UPDATED_BY | — | — |
| 14 | BusinessUnitPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 15 | BusinessUnitPEOLocationId | LOCATION_ID | — | — |
| 16 | BusinessUnitPEOManagerId | MANAGER_ID | — | — |
| 17 | BusinessUnitPEOName1 | BU_NAME | — | — |
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
| 6 | LedgerPEOAttributeCategory8 | ATTRIBUTE_CATEGORY | — | — |
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
| 21 | LedgerPEOCreatedBy9 | CREATED_BY | — | — |
| 22 | LedgerPEOCreationDate9 | CREATION_DATE | — | — |
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
| 42 | LedgerPEOLastUpdateDate9 | LAST_UPDATE_DATE | — | — |
| 43 | LedgerPEOLastUpdateLogin9 | LAST_UPDATE_LOGIN | — | — |
| 44 | LedgerPEOLastUpdatedBy9 | LAST_UPDATED_BY | — | — |
| 45 | LedgerPEOLatestEncumbranceYear | LATEST_ENCUMBRANCE_YEAR | — | — |
| 46 | LedgerPEOLatestOpenedPeriodName | LATEST_OPENED_PERIOD_NAME | — | — |
| 47 | LedgerPEOLeLedgerTypeCode | LE_LEDGER_TYPE_CODE | — | — |
| 48 | LedgerPEOLedgerAttributes | LEDGER_ATTRIBUTES | — | — |
| 49 | LedgerPEOLedgerCategoryCode | LEDGER_CATEGORY_CODE | — | — |
| 50 | LedgerPEOLedgerId | LEDGER_ID | — | — |
| 51 | LedgerPEOMgtSegColumnName | MGT_SEG_COLUMN_NAME | — | — |
| 52 | LedgerPEOMgtSegValueOptionCode | MGT_SEG_VALUE_OPTION_CODE | — | — |
| 53 | LedgerPEOMgtSegValueSetId | MGT_SEG_VALUE_SET_ID | — | — |
| 54 | LedgerPEOName2 | NAME | — | — |
| 55 | LedgerPEONetClosingBalFlag | NET_CLOSING_BAL_FLAG | — | — |
| 56 | LedgerPEONetIncomeCodeCombinationId | NET_INCOME_CODE_COMBINATION_ID | — | — |
| 57 | LedgerPEOObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 58 | LedgerPEOObjectVersionNumber8 | OBJECT_VERSION_NUMBER | — | — |
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
| 1 | FdChargesUnitOfMeasurePEOBaseUomFlag1 | BASE_UOM_FLAG | — | — |
| 2 | FdChargesUnitOfMeasurePEOCreatedBy1 | CREATED_BY | — | — |
| 3 | FdChargesUnitOfMeasurePEOCreationDate1 | CREATION_DATE | — | — |
| 4 | FdChargesUnitOfMeasurePEODescription1 | DESCRIPTION | — | — |
| 5 | FdChargesUnitOfMeasurePEODisableDate1 | DISABLE_DATE | — | — |
| 6 | FdChargesUnitOfMeasurePEOGlobalAttribute11 | GLOBAL_ATTRIBUTE1 | — | — |
| 7 | FdChargesUnitOfMeasurePEOGlobalAttributeCategory1 | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 8 | FdChargesUnitOfMeasurePEOHasGeneratedCode1 | HAS_GENERATED_CODE | — | — |
| 9 | FdChargesUnitOfMeasurePEOJobDefinitionName1 | JOB_DEFINITION_NAME | — | — |
| 10 | FdChargesUnitOfMeasurePEOJobDefinitionPackage1 | JOB_DEFINITION_PACKAGE | — | — |
| 11 | FdChargesUnitOfMeasurePEOLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 12 | FdChargesUnitOfMeasurePEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 13 | FdChargesUnitOfMeasurePEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 14 | FdChargesUnitOfMeasurePEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 15 | FdChargesUnitOfMeasurePEORequestId1 | REQUEST_ID | — | — |
| 16 | FdChargesUnitOfMeasurePEOStandardPackFlag1 | STANDARD_PACK_FLAG | — | — |
| 17 | FdChargesUnitOfMeasurePEOUnitOfMeasure1 | UNIT_OF_MEASURE | — | — |
| 18 | FdChargesUnitOfMeasurePEOUnitOfMeasureId1 | UNIT_OF_MEASURE_ID | — | — |
| 19 | FdChargesUnitOfMeasurePEOUomClass1 | UOM_CLASS | — | — |
| 20 | FdChargesUnitOfMeasurePEOUomCode1 | UOM_CODE | — | — |
| 21 | FdChargesUnitOfMeasurePEOUomPluralDesc1 | UOM_PLURAL_DESC | — | — |
| 22 | FdChargesUnitOfMeasurePEOUomReciprocalDesc1 | UOM_RECIPROCAL_DESC | — | — |
| 23 | FdLinesUnitOfMeasurePEOBaseUomFlag | BASE_UOM_FLAG | — | — |
| 24 | FdLinesUnitOfMeasurePEOCreatedBy | CREATED_BY | — | — |
| 25 | FdLinesUnitOfMeasurePEOCreationDate | CREATION_DATE | — | — |
| 26 | FdLinesUnitOfMeasurePEODescription | DESCRIPTION | — | — |
| 27 | FdLinesUnitOfMeasurePEODisableDate | DISABLE_DATE | — | — |
| 28 | FdLinesUnitOfMeasurePEOGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 29 | FdLinesUnitOfMeasurePEOGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 30 | FdLinesUnitOfMeasurePEOHasGeneratedCode | HAS_GENERATED_CODE | — | — |
| 31 | FdLinesUnitOfMeasurePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 32 | FdLinesUnitOfMeasurePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 33 | FdLinesUnitOfMeasurePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 34 | FdLinesUnitOfMeasurePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 35 | FdLinesUnitOfMeasurePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 36 | FdLinesUnitOfMeasurePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 37 | FdLinesUnitOfMeasurePEORequestId | REQUEST_ID | — | — |
| 38 | FdLinesUnitOfMeasurePEOStandardPackFlag | STANDARD_PACK_FLAG | — | — |
| 39 | FdLinesUnitOfMeasurePEOUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 40 | FdLinesUnitOfMeasurePEOUnitOfMeasureId | UNIT_OF_MEASURE_ID | — | — |
| 41 | FdLinesUnitOfMeasurePEOUomClass | UOM_CLASS | — | — |
| 42 | FdLinesUnitOfMeasurePEOUomCode | UOM_CODE | — | — |
| 43 | FdLinesUnitOfMeasurePEOUomPluralDesc | UOM_PLURAL_DESC | — | — |
| 44 | FdLinesUnitOfMeasurePEOUomReciprocalDesc | UOM_RECIPROCAL_DESC | — | — |
| 45 | UnitOfMeasurePEOAttributeCategory9 | ATTRIBUTE_CATEGORY | — | — |
| 46 | UnitOfMeasurePEOBaseUomFlag | BASE_UOM_FLAG | — | — |
| 47 | UnitOfMeasurePEOCreatedBy10 | CREATED_BY | — | — |
| 48 | UnitOfMeasurePEOCreationDate10 | CREATION_DATE | — | — |
| 49 | UnitOfMeasurePEODescription1 | DESCRIPTION | — | — |
| 50 | UnitOfMeasurePEODisableDate | DISABLE_DATE | — | — |
| 51 | UnitOfMeasurePEOGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 52 | UnitOfMeasurePEOGlobalAttributeCategory4 | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 53 | UnitOfMeasurePEOHasGeneratedCode | HAS_GENERATED_CODE | — | — |
| 54 | UnitOfMeasurePEOJobDefinitionName8 | JOB_DEFINITION_NAME | — | — |
| 55 | UnitOfMeasurePEOJobDefinitionPackage8 | JOB_DEFINITION_PACKAGE | — | — |
| 56 | UnitOfMeasurePEOLastUpdateDate10 | LAST_UPDATE_DATE | — | — |
| 57 | UnitOfMeasurePEOLastUpdateLogin10 | LAST_UPDATE_LOGIN | — | — |
| 58 | UnitOfMeasurePEOLastUpdatedBy10 | LAST_UPDATED_BY | — | — |
| 59 | UnitOfMeasurePEOObjectVersionNumber9 | OBJECT_VERSION_NUMBER | — | — |
| 60 | UnitOfMeasurePEORequestId8 | REQUEST_ID | — | — |
| 61 | UnitOfMeasurePEOStandardPackFlag | STANDARD_PACK_FLAG | — | — |
| 62 | UnitOfMeasurePEOUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 63 | UnitOfMeasurePEOUnitOfMeasureId | UNIT_OF_MEASURE_ID | — | — |
| 64 | UnitOfMeasurePEOUomClass | UOM_CLASS | — | — |
| 65 | UnitOfMeasurePEOUomCode | UOM_CODE | — | — |
| 66 | UnitOfMeasurePEOUomPluralDesc | UOM_PLURAL_DESC | — | — |
| 67 | UnitOfMeasurePEOUomReciprocalDesc | UOM_RECIPROCAL_DESC | — | — |

### [[jg_fscl_hdrs_atrb_ext_all|JG_FSCL_HDRS_ATRB_EXT_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocHeaderExtnEOApplicationId | APPLICATION_ID | — | — |
| 2 | FiscalDocHeaderExtnEOCommitmentStatementIdent | COMMITMENT_STATEMENT_IDENT | — | — |
| 3 | FiscalDocHeaderExtnEOContainerIdentifier | CONTAINER_IDENTIFIER | — | — |
| 4 | FiscalDocHeaderExtnEOContingencyType | CONTINGENCY_TYPE | — | — |
| 5 | FiscalDocHeaderExtnEOCreatedBy4 | CREATED_BY | — | — |
| 6 | FiscalDocHeaderExtnEOCreationDate4 | CREATION_DATE | — | — |
| 7 | FiscalDocHeaderExtnEODocExtHdrId | DOC_EXT_HDR_ID | — | — |
| 8 | FiscalDocHeaderExtnEODocNature | DOC_NATURE | — | — |
| 9 | FiscalDocHeaderExtnEOEntityCode | ENTITY_CODE | — | — |
| 10 | FiscalDocHeaderExtnEOEventClassCode | EVENT_CLASS_CODE | — | — |
| 11 | FiscalDocHeaderExtnEOFerryIdentification | FERRY_IDENTIFICATION | — | — |
| 12 | FiscalDocHeaderExtnEOFiscalDocDate | FISCAL_DOC_DATE | — | — |
| 13 | FiscalDocHeaderExtnEOFreightPartySiteId | FREIGHT_PARTY_SITE_ID | — | — |
| 14 | FiscalDocHeaderExtnEOFreightType | FREIGHT_TYPE | — | — |
| 15 | FiscalDocHeaderExtnEOGoodsBrandCarried | GOODS_BRAND_CARRIED | — | — |
| 16 | FiscalDocHeaderExtnEOGoodsTypeCarried | GOODS_TYPE_CARRIED | — | — |
| 17 | FiscalDocHeaderExtnEOGrossWeight | GROSS_WEIGHT | — | — |
| 18 | FiscalDocHeaderExtnEOIndustryType | INDUSTRY_TYPE | — | — |
| 19 | FiscalDocHeaderExtnEOJobDefinitionName4 | JOB_DEFINITION_NAME | — | — |
| 20 | FiscalDocHeaderExtnEOJobDefinitionPackage4 | JOB_DEFINITION_PACKAGE | — | — |
| 21 | FiscalDocHeaderExtnEOLastUpdateDate4 | LAST_UPDATE_DATE | — | — |
| 22 | FiscalDocHeaderExtnEOLastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 23 | FiscalDocHeaderExtnEOLastUpdatedBy4 | LAST_UPDATED_BY | — | — |
| 24 | FiscalDocHeaderExtnEOLegalReportingUnitId | LEGAL_REPORTING_UNIT_ID | — | — |
| 25 | FiscalDocHeaderExtnEOMatIssueRecptDate | MAT_ISSUE_RECPT_DATE | — | — |
| 26 | FiscalDocHeaderExtnEOMatIssueRecptHour | MAT_ISSUE_RECPT_HOUR | — | — |
| 27 | FiscalDocHeaderExtnEONetWeight | NET_WEIGHT | — | — |
| 28 | FiscalDocHeaderExtnEOObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 29 | FiscalDocHeaderExtnEOOrgId | ORG_ID | — | — |
| 30 | FiscalDocHeaderExtnEOPaymentOption | PAYMENT_OPTION | — | — |
| 31 | FiscalDocHeaderExtnEOPurchaseContract | PURCHASE_CONTRACT | — | — |
| 32 | FiscalDocHeaderExtnEOQuantityCarried | QUANTITY_CARRIED | — | — |
| 33 | FiscalDocHeaderExtnEORefComplementaryFdFlag | REF_COMPLEMENTARY_FD_FLAG | — | — |
| 34 | FiscalDocHeaderExtnEORefDocIssuerStateCode | REF_DOC_ISSUER_STATE_CODE | — | — |
| 35 | FiscalDocHeaderExtnEORefDocNum | REF_DOC_NUM | — | — |
| 36 | FiscalDocHeaderExtnEORefFiscalDocDate | REF_FISCAL_DOC_DATE | — | — |
| 37 | FiscalDocHeaderExtnEORefFiscalDocKey | REF_FISCAL_DOC_KEY | — | — |
| 38 | FiscalDocHeaderExtnEORefIssuerTaxpayerId | REF_ISSUER_TAXPAYER_ID | — | — |
| 39 | FiscalDocHeaderExtnEORefModel | REF_MODEL | — | — |
| 40 | FiscalDocHeaderExtnEORefRuralFlag | REF_RURAL_FLAG | — | — |
| 41 | FiscalDocHeaderExtnEORefSeries | REF_SERIES | — | — |
| 42 | FiscalDocHeaderExtnEORequestId4 | REQUEST_ID | — | — |
| 43 | FiscalDocHeaderExtnEOSealNumber | SEAL_NUMBER | — | — |
| 44 | FiscalDocHeaderExtnEOSeries1 | SERIES | — | — |
| 45 | FiscalDocHeaderExtnEOServiceSeries | SERVICE_SERIES | — | — |
| 46 | FiscalDocHeaderExtnEOServiceSituation | SERVICE_SITUATION | — | — |
| 47 | FiscalDocHeaderExtnEOServiceTaxPaidFlag | SERVICE_TAX_PAID_FLAG | — | — |
| 48 | FiscalDocHeaderExtnEOServiceType | SERVICE_TYPE | — | — |
| 49 | FiscalDocHeaderExtnEOTaxSettlementDate | TAX_SETTLEMENT_DATE | — | — |
| 50 | FiscalDocHeaderExtnEOTrxFdTypeDeterminant | TRX_FD_TYPE_DETERMINANT | — | — |
| 51 | FiscalDocHeaderExtnEOTrxId | TRX_ID | — | — |
| 52 | FiscalDocHeaderExtnEOTrxNumber | TRX_NUMBER | — | — |
| 53 | FiscalDocHeaderExtnEOWagonIdentification | WAGON_IDENTIFICATION | — | — |
| 54 | FiscalDocHeaderExtnEOWhtSocialIntgProgAmt | WHT_SOCIAL_INTG_PROG_AMT | — | — |
| 55 | FiscalDocHeaderExtnEOWhtSsFinancingAmt | WHT_SS_FINANCING_AMT | — | — |

### [[jg_fscl_hdr_dtls_atrb_ext_all|JG_FSCL_HDR_DTLS_ATRB_EXT_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocHeaderDetailExtnEOApplicationId1 | APPLICATION_ID | — | — |
| 2 | FiscalDocHeaderDetailExtnEOCreatedBy5 | CREATED_BY | — | — |
| 3 | FiscalDocHeaderDetailExtnEOCreationDate5 | CREATION_DATE | — | — |
| 4 | FiscalDocHeaderDetailExtnEODocExtHdrId1 | DOC_EXT_HDR_ID | — | — |
| 5 | FiscalDocHeaderDetailExtnEOEntityCode1 | ENTITY_CODE | — | — |
| 6 | FiscalDocHeaderDetailExtnEOEventClassCode1 | EVENT_CLASS_CODE | — | — |
| 7 | FiscalDocHeaderDetailExtnEOHdrAtrbExtDtlId | HDR_ATRB_EXT_DTL_ID | — | — |
| 8 | FiscalDocHeaderDetailExtnEOJobDefinitionName5 | JOB_DEFINITION_NAME | — | — |
| 9 | FiscalDocHeaderDetailExtnEOJobDefinitionPackage5 | JOB_DEFINITION_PACKAGE | — | — |
| 10 | FiscalDocHeaderDetailExtnEOLastUpdateDate5 | LAST_UPDATE_DATE | — | — |
| 11 | FiscalDocHeaderDetailExtnEOLastUpdateLogin5 | LAST_UPDATE_LOGIN | — | — |
| 12 | FiscalDocHeaderDetailExtnEOLastUpdatedBy5 | LAST_UPDATED_BY | — | — |
| 13 | FiscalDocHeaderDetailExtnEOObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 14 | FiscalDocHeaderDetailExtnEOOrgId1 | ORG_ID | — | — |
| 15 | FiscalDocHeaderDetailExtnEORecordType | RECORD_TYPE | — | — |
| 16 | FiscalDocHeaderDetailExtnEORequestId5 | REQUEST_ID | — | — |
| 17 | FiscalDocHeaderDetailExtnEOTaxRelatedLegalMessageFlag | TAX_RELATED_LEGAL_MESSAGE_FLAG | — | — |
| 18 | FiscalDocHeaderDetailExtnEOTrxId1 | TRX_ID | — | — |

### [[jg_fscl_lines_atrb_ext_all|JG_FSCL_LINES_ATRB_EXT_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocLineExtnEOApplicationId2 | APPLICATION_ID | — | — |
| 2 | FiscalDocLineExtnEOCreatedBy6 | CREATED_BY | — | — |
| 3 | FiscalDocLineExtnEOCreationDate6 | CREATION_DATE | — | — |
| 4 | FiscalDocLineExtnEODocExtHdrId2 | DOC_EXT_HDR_ID | — | — |
| 5 | FiscalDocLineExtnEODocExtLineId | DOC_EXT_LINE_ID | — | — |
| 6 | FiscalDocLineExtnEOEntityCode2 | ENTITY_CODE | — | — |
| 7 | FiscalDocLineExtnEOEventClassCode2 | EVENT_CLASS_CODE | — | — |
| 8 | FiscalDocLineExtnEOItemSerialNumber | ITEM_SERIAL_NUMBER | — | — |
| 9 | FiscalDocLineExtnEOJobDefinitionName6 | JOB_DEFINITION_NAME | — | — |
| 10 | FiscalDocLineExtnEOJobDefinitionPackage6 | JOB_DEFINITION_PACKAGE | — | — |
| 11 | FiscalDocLineExtnEOLastUpdateDate6 | LAST_UPDATE_DATE | — | — |
| 12 | FiscalDocLineExtnEOLastUpdateLogin6 | LAST_UPDATE_LOGIN | — | — |
| 13 | FiscalDocLineExtnEOLastUpdatedBy6 | LAST_UPDATED_BY | — | — |
| 14 | FiscalDocLineExtnEOLegalMessageText | LEGAL_MESSAGE_TEXT | — | — |
| 15 | FiscalDocLineExtnEOObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |
| 16 | FiscalDocLineExtnEOOrgId2 | ORG_ID | — | — |
| 17 | FiscalDocLineExtnEOProceedingIdentifier | PROCEEDING_IDENTIFIER | — | — |
| 18 | FiscalDocLineExtnEOProceedingOrigin | PROCEEDING_ORIGIN | — | — |
| 19 | FiscalDocLineExtnEORequestId6 | REQUEST_ID | — | — |
| 20 | FiscalDocLineExtnEOServiceSituation1 | SERVICE_SITUATION | — | — |
| 21 | FiscalDocLineExtnEOTrxId2 | TRX_ID | — | — |
| 22 | FiscalDocLineExtnEOTrxLevelType | TRX_LEVEL_TYPE | — | — |
| 23 | FiscalDocLineExtnEOTrxLineId | TRX_LINE_ID | — | — |

### [[jg_fscl_ln_dtls_atrb_ext_all|JG_FSCL_LN_DTLS_ATRB_EXT_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocLineDetailExtnEOApplicationId3 | APPLICATION_ID | — | — |
| 2 | FiscalDocLineDetailExtnEOCreatedBy7 | CREATED_BY | — | — |
| 3 | FiscalDocLineDetailExtnEOCreationDate7 | CREATION_DATE | — | — |
| 4 | FiscalDocLineDetailExtnEODocExtHdrId3 | DOC_EXT_HDR_ID | — | — |
| 5 | FiscalDocLineDetailExtnEODocExtLineDetailId | DOC_EXT_LINE_DETAIL_ID | — | — |
| 6 | FiscalDocLineDetailExtnEODocExtLineId1 | DOC_EXT_LINE_ID | — | — |
| 7 | FiscalDocLineDetailExtnEOEntityCode3 | ENTITY_CODE | — | — |
| 8 | FiscalDocLineDetailExtnEOEventClassCode3 | EVENT_CLASS_CODE | — | — |
| 9 | FiscalDocLineDetailExtnEOJobDefinitionName7 | JOB_DEFINITION_NAME | — | — |
| 10 | FiscalDocLineDetailExtnEOJobDefinitionPackage7 | JOB_DEFINITION_PACKAGE | — | — |
| 11 | FiscalDocLineDetailExtnEOLastUpdateDate7 | LAST_UPDATE_DATE | — | — |
| 12 | FiscalDocLineDetailExtnEOLastUpdateLogin7 | LAST_UPDATE_LOGIN | — | — |
| 13 | FiscalDocLineDetailExtnEOLastUpdatedBy7 | LAST_UPDATED_BY | — | — |
| 14 | FiscalDocLineDetailExtnEOObjectVersionNumber7 | OBJECT_VERSION_NUMBER | — | — |
| 15 | FiscalDocLineDetailExtnEOOrgId3 | ORG_ID | — | — |
| 16 | FiscalDocLineDetailExtnEORequestId7 | REQUEST_ID | — | — |
| 17 | FiscalDocLineDetailExtnEOTrxId3 | TRX_ID | — | — |
| 18 | FiscalDocLineDetailExtnEOTrxLevelType1 | TRX_LEVEL_TYPE | — | — |
| 19 | FiscalDocLineDetailExtnEOTrxLineDetailId | TRX_LINE_DETAIL_ID | — | — |
| 20 | FiscalDocLineDetailExtnEOTrxLineId1 | TRX_LINE_ID | — | — |

### [[jg_fscl_tax_lines_all|JG_FSCL_TAX_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocTaxLineEOAdjustedTaxLineId | ADJUSTED_TAX_LINE_ID | — | — |
| 2 | FiscalDocTaxLineEOApplicationId | APPLICATION_ID | — | — |
| 3 | FiscalDocTaxLineEOCalTaxAmt | CAL_TAX_AMT | — | — |
| 4 | FiscalDocTaxLineEOCalTaxAmtTaxCurr | CAL_TAX_AMT_TAX_CURR | — | — |
| 5 | FiscalDocTaxLineEOCityCode | CITY_CODE | — | — |
| 6 | FiscalDocTaxLineEOContentOwnerId | CONTENT_OWNER_ID | — | — |
| 7 | FiscalDocTaxLineEOCreatedBy | CREATED_BY | — | — |
| 8 | FiscalDocTaxLineEOCreationDate | CREATION_DATE | — | — |
| 9 | FiscalDocTaxLineEOEntityCode | ENTITY_CODE | — | — |
| 10 | FiscalDocTaxLineEOEventClassCode | EVENT_CLASS_CODE | — | — |
| 11 | FiscalDocTaxLineEOExemptCertificateNumber | EXEMPT_CERTIFICATE_NUMBER | — | — |
| 12 | FiscalDocTaxLineEOExemptReasonCode | EXEMPT_REASON_CODE | — | — |
| 13 | FiscalDocTaxLineEOInterfaceEntityCode | INTERFACE_ENTITY_CODE | — | — |
| 14 | FiscalDocTaxLineEOInterfaceTaxLineId | INTERFACE_TAX_LINE_ID | — | — |
| 15 | FiscalDocTaxLineEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 16 | FiscalDocTaxLineEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 17 | FiscalDocTaxLineEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
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
| 32 | FiscalDocTaxLineEOQuantity | QUANTITY | — | — |
| 33 | FiscalDocTaxLineEOReferenceDocLineAmt | REFERENCE_DOC_LINE_AMT | — | — |
| 34 | FiscalDocTaxLineEOReferenceDocUnitPrice | REFERENCE_DOC_UNIT_PRICE | — | — |
| 35 | FiscalDocTaxLineEOReportingTypeCode | REPORTING_TYPE_CODE | — | — |
| 36 | FiscalDocTaxLineEORequestId | REQUEST_ID | — | — |
| 37 | FiscalDocTaxLineEOSelfAssessedFlag | SELF_ASSESSED_FLAG | — | — |
| 38 | FiscalDocTaxLineEOServiceItemCode | SERVICE_ITEM_CODE | — | — |
| 39 | FiscalDocTaxLineEOTax | TAX | — | — |
| 40 | FiscalDocTaxLineEOTaxAmt | TAX_AMT | — | — |
| 41 | FiscalDocTaxLineEOTaxAmtIncludedFlag | TAX_AMT_INCLUDED_FLAG | — | — |
| 42 | FiscalDocTaxLineEOTaxAmtTaxCurr | TAX_AMT_TAX_CURR | — | — |
| 43 | FiscalDocTaxLineEOTaxCreditAmount | TAX_CREDIT_AMOUNT | — | — |
| 44 | FiscalDocTaxLineEOTaxExceptionId | TAX_EXCEPTION_ID | — | — |
| 45 | FiscalDocTaxLineEOTaxExemptionId | TAX_EXEMPTION_ID | — | — |
| 46 | FiscalDocTaxLineEOTaxHoldCode | TAX_HOLD_CODE | — | — |
| 47 | FiscalDocTaxLineEOTaxId | TAX_ID | — | — |
| 48 | FiscalDocTaxLineEOTaxJurisdictionCode | TAX_JURISDICTION_CODE | — | — |
| 49 | FiscalDocTaxLineEOTaxJurisdictionId | TAX_JURISDICTION_ID | — | — |
| 50 | FiscalDocTaxLineEOTaxLineId | TAX_LINE_ID | — | — |
| 51 | FiscalDocTaxLineEOTaxLineNumber | TAX_LINE_NUMBER | — | — |
| 52 | FiscalDocTaxLineEOTaxLineSourceCode | TAX_LINE_SOURCE_CODE | — | — |
| 53 | FiscalDocTaxLineEOTaxOnlyLineFlag | TAX_ONLY_LINE_FLAG | — | — |
| 54 | FiscalDocTaxLineEOTaxRate | TAX_RATE | — | — |
| 55 | FiscalDocTaxLineEOTaxRateCode | TAX_RATE_CODE | — | — |
| 56 | FiscalDocTaxLineEOTaxRateId | TAX_RATE_ID | — | — |
| 57 | FiscalDocTaxLineEOTaxRegimeCode | TAX_REGIME_CODE | — | — |
| 58 | FiscalDocTaxLineEOTaxRegimeId | TAX_REGIME_ID | — | — |
| 59 | FiscalDocTaxLineEOTaxSituationCode | TAX_SITUATION_CODE | — | — |
| 60 | FiscalDocTaxLineEOTaxStatusCode | TAX_STATUS_CODE | — | — |
| 61 | FiscalDocTaxLineEOTaxStatusId | TAX_STATUS_ID | — | — |
| 62 | FiscalDocTaxLineEOTaxableAmt | TAXABLE_AMT | — | — |
| 63 | FiscalDocTaxLineEOTaxableAmtDetermCode | TAXABLE_AMT_DETERM_CODE | — | — |
| 64 | FiscalDocTaxLineEOTaxableBasisPercPayerOpr | TAXABLE_BASIS_PERC_PAYER_OPR | — | — |
| 65 | FiscalDocTaxLineEOTaxableBasisReductionPerc | TAXABLE_BASIS_REDUCTION_PERC | — | — |
| 66 | FiscalDocTaxLineEOTrxId | TRX_ID | — | — |
| 67 | FiscalDocTaxLineEOTrxLevelType | TRX_LEVEL_TYPE | — | — |
| 68 | FiscalDocTaxLineEOTrxLineId | TRX_LINE_ID | — | — |
| 69 | FiscalDocTaxLineEOUomCode | UOM_CODE | — | — |
| 70 | FiscalDocTaxLineEOUserEnteredTaxAmt | USER_ENTERED_TAX_AMT | — | — |
| 71 | FiscalDocTaxLineEOUserEnteredTaxAmtTaxCurr | USER_ENTERED_TAX_AMT_TAX_CURR | — | — |
| 72 | FiscalDocTaxLineEOValueAddedMarginPerc | VALUE_ADDED_MARGIN_PERC | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 2 | CreatedByPersonNameDPEOAttributeCategory10 | ATTRIBUTE_CATEGORY | — | — |
| 3 | CreatedByPersonNameDPEOBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 4 | CreatedByPersonNameDPEOCreatedBy13 | CREATED_BY | — | — |
| 5 | CreatedByPersonNameDPEOCreationDate13 | CREATION_DATE | — | — |
| 6 | CreatedByPersonNameDPEODisplayName | DISPLAY_NAME | — | — |
| 7 | CreatedByPersonNameDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | CreatedByPersonNameDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | CreatedByPersonNameDPEOFirstName | FIRST_NAME | — | — |
| 10 | CreatedByPersonNameDPEOFullName | FULL_NAME | — | — |
| 11 | CreatedByPersonNameDPEOHonors | HONORS | — | — |
| 12 | CreatedByPersonNameDPEOKnownAs | KNOWN_AS | — | — |
| 13 | CreatedByPersonNameDPEOLastName | LAST_NAME | — | — |
| 14 | CreatedByPersonNameDPEOLastUpdateDate13 | LAST_UPDATE_DATE | — | — |
| 15 | CreatedByPersonNameDPEOLastUpdateLogin13 | LAST_UPDATE_LOGIN | — | — |
| 16 | CreatedByPersonNameDPEOLastUpdatedBy13 | LAST_UPDATED_BY | — | — |
| 17 | CreatedByPersonNameDPEOLegislationCode | LEGISLATION_CODE | — | — |
| 18 | CreatedByPersonNameDPEOListName | LIST_NAME | — | — |
| 19 | CreatedByPersonNameDPEOMiddleNames | MIDDLE_NAMES | — | — |
| 20 | CreatedByPersonNameDPEOMilitaryRank | MILITARY_RANK | — | — |
| 21 | CreatedByPersonNameDPEONamInformationCategory | NAM_INFORMATION_CATEGORY | — | — |
| 22 | CreatedByPersonNameDPEONameType | NAME_TYPE | — | — |
| 23 | CreatedByPersonNameDPEOObjectVersionNumber12 | OBJECT_VERSION_NUMBER | — | — |
| 24 | CreatedByPersonNameDPEOOrderName | ORDER_NAME | — | — |
| 25 | CreatedByPersonNameDPEOPersonId2 | PERSON_ID | — | — |
| 26 | CreatedByPersonNameDPEOPersonNameId | PERSON_NAME_ID | — | — |
| 27 | CreatedByPersonNameDPEOPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 28 | CreatedByPersonNameDPEOPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 29 | CreatedByPersonNameDPEOSuffix | SUFFIX | — | — |
| 30 | CreatedByPersonNameDPEOTitle | TITLE | — | — |
| 31 | FdHxCrtdByPersonNameDPEOBusinessGroupId6 | BUSINESS_GROUP_ID | — | — |
| 32 | FdHxCrtdByPersonNameDPEOCreatedBy8 | CREATED_BY | — | — |
| 33 | FdHxCrtdByPersonNameDPEOCreationDate8 | CREATION_DATE | — | — |
| 34 | FdHxCrtdByPersonNameDPEODisplayName2 | DISPLAY_NAME | — | — |
| 35 | FdHxCrtdByPersonNameDPEOEffectiveEndDate2 | EFFECTIVE_END_DATE | — | — |
| 36 | FdHxCrtdByPersonNameDPEOEffectiveStartDate2 | EFFECTIVE_START_DATE | — | — |
| 37 | FdHxCrtdByPersonNameDPEOFirstName2 | FIRST_NAME | — | — |
| 38 | FdHxCrtdByPersonNameDPEOFullName2 | FULL_NAME | — | — |
| 39 | FdHxCrtdByPersonNameDPEOHonors2 | HONORS | — | — |
| 40 | FdHxCrtdByPersonNameDPEOKnownAs2 | KNOWN_AS | — | — |
| 41 | FdHxCrtdByPersonNameDPEOLastName2 | LAST_NAME | — | — |
| 42 | FdHxCrtdByPersonNameDPEOLastUpdateDate8 | LAST_UPDATE_DATE | — | — |
| 43 | FdHxCrtdByPersonNameDPEOLastUpdateLogin8 | LAST_UPDATE_LOGIN | — | — |
| 44 | FdHxCrtdByPersonNameDPEOLastUpdatedBy8 | LAST_UPDATED_BY | — | — |
| 45 | FdHxCrtdByPersonNameDPEOLegislationCode2 | LEGISLATION_CODE | — | — |
| 46 | FdHxCrtdByPersonNameDPEOListName2 | LIST_NAME | — | — |
| 47 | FdHxCrtdByPersonNameDPEOMiddleNames2 | MIDDLE_NAMES | — | — |
| 48 | FdHxCrtdByPersonNameDPEOMilitaryRank2 | MILITARY_RANK | — | — |
| 49 | FdHxCrtdByPersonNameDPEONameType2 | NAME_TYPE | — | — |
| 50 | FdHxCrtdByPersonNameDPEOObjectVersionNumber10 | OBJECT_VERSION_NUMBER | — | — |
| 51 | FdHxCrtdByPersonNameDPEOObjectVersionNumber11 | OBJECT_VERSION_NUMBER | — | — |
| 52 | FdHxCrtdByPersonNameDPEOOrderName2 | ORDER_NAME | — | — |
| 53 | FdHxCrtdByPersonNameDPEOPersonId6 | PERSON_ID | — | — |
| 54 | FdHxCrtdByPersonNameDPEOPersonNameId4 | PERSON_NAME_ID | — | — |
| 55 | FdHxCrtdByPersonNameDPEOPersonNameId5 | PERSON_NAME_ID | — | — |
| 56 | FdHxCrtdByPersonNameDPEOPreNameAdjunct2 | PRE_NAME_ADJUNCT | — | — |
| 57 | FdHxCrtdByPersonNameDPEOPreviousLastName2 | PREVIOUS_LAST_NAME | — | — |
| 58 | FdHxCrtdByPersonNameDPEOSuffix2 | SUFFIX | — | — |
| 59 | FdHxCrtdByPersonNameDPEOTitle2 | TITLE | — | — |
| 60 | FdHxLastUpdByPersonNameDPEOBusinessGroupId7 | BUSINESS_GROUP_ID | — | — |
| 61 | FdHxLastUpdByPersonNameDPEOCreatedBy9 | CREATED_BY | — | — |
| 62 | FdHxLastUpdByPersonNameDPEOCreationDate9 | CREATION_DATE | — | — |
| 63 | FdHxLastUpdByPersonNameDPEODisplayName3 | DISPLAY_NAME | — | — |
| 64 | FdHxLastUpdByPersonNameDPEOEffectiveEndDate3 | EFFECTIVE_END_DATE | — | — |
| 65 | FdHxLastUpdByPersonNameDPEOEffectiveStartDate3 | EFFECTIVE_START_DATE | — | — |
| 66 | FdHxLastUpdByPersonNameDPEOFirstName3 | FIRST_NAME | — | — |
| 67 | FdHxLastUpdByPersonNameDPEOFullName3 | FULL_NAME | — | — |
| 68 | FdHxLastUpdByPersonNameDPEOHonors3 | HONORS | — | — |
| 69 | FdHxLastUpdByPersonNameDPEOKnownAs3 | KNOWN_AS | — | — |
| 70 | FdHxLastUpdByPersonNameDPEOLastName3 | LAST_NAME | — | — |
| 71 | FdHxLastUpdByPersonNameDPEOLastUpdateDate9 | LAST_UPDATE_DATE | — | — |
| 72 | FdHxLastUpdByPersonNameDPEOLastUpdateLogin9 | LAST_UPDATE_LOGIN | — | — |
| 73 | FdHxLastUpdByPersonNameDPEOLastUpdatedBy9 | LAST_UPDATED_BY | — | — |
| 74 | FdHxLastUpdByPersonNameDPEOLegislationCode3 | LEGISLATION_CODE | — | — |
| 75 | FdHxLastUpdByPersonNameDPEOListName3 | LIST_NAME | — | — |
| 76 | FdHxLastUpdByPersonNameDPEOMiddleNames3 | MIDDLE_NAMES | — | — |
| 77 | FdHxLastUpdByPersonNameDPEOMilitaryRank3 | MILITARY_RANK | — | — |
| 78 | FdHxLastUpdByPersonNameDPEONameType3 | NAME_TYPE | — | — |
| 79 | FdHxLastUpdByPersonNameDPEOObjectVersionNumber12 | OBJECT_VERSION_NUMBER | — | — |
| 80 | FdHxLastUpdByPersonNameDPEOObjectVersionNumber13 | OBJECT_VERSION_NUMBER | — | — |
| 81 | FdHxLastUpdByPersonNameDPEOOrderName3 | ORDER_NAME | — | — |
| 82 | FdHxLastUpdByPersonNameDPEOPersonId7 | PERSON_ID | — | — |
| 83 | FdHxLastUpdByPersonNameDPEOPersonNameId6 | PERSON_NAME_ID | — | — |
| 84 | FdHxLastUpdByPersonNameDPEOPersonNameId7 | PERSON_NAME_ID | — | — |
| 85 | FdHxLastUpdByPersonNameDPEOPreNameAdjunct3 | PRE_NAME_ADJUNCT | — | — |
| 86 | FdHxLastUpdByPersonNameDPEOPreviousLastName3 | PREVIOUS_LAST_NAME | — | — |
| 87 | FdHxLastUpdByPersonNameDPEOSuffix3 | SUFFIX | — | — |
| 88 | FdHxLastUpdByPersonNameDPEOTitle3 | TITLE | — | — |
| 89 | FdLinesCrtdByPersonNameDPEOBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 90 | FdLinesCrtdByPersonNameDPEOCreatedBy4 | CREATED_BY | — | — |
| 91 | FdLinesCrtdByPersonNameDPEOCreationDate4 | CREATION_DATE | — | — |
| 92 | FdLinesCrtdByPersonNameDPEODisplayName | DISPLAY_NAME | — | — |
| 93 | FdLinesCrtdByPersonNameDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 94 | FdLinesCrtdByPersonNameDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 95 | FdLinesCrtdByPersonNameDPEOFirstName | FIRST_NAME | — | — |
| 96 | FdLinesCrtdByPersonNameDPEOFullName | FULL_NAME | — | — |
| 97 | FdLinesCrtdByPersonNameDPEOHonors | HONORS | — | — |
| 98 | FdLinesCrtdByPersonNameDPEOKnownAs | KNOWN_AS | — | — |
| 99 | FdLinesCrtdByPersonNameDPEOLastName | LAST_NAME | — | — |
| 100 | FdLinesCrtdByPersonNameDPEOLastUpdateDate4 | LAST_UPDATE_DATE | — | — |
| 101 | FdLinesCrtdByPersonNameDPEOLastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 102 | FdLinesCrtdByPersonNameDPEOLastUpdatedBy4 | LAST_UPDATED_BY | — | — |
| 103 | FdLinesCrtdByPersonNameDPEOLegislationCode | LEGISLATION_CODE | — | — |
| 104 | FdLinesCrtdByPersonNameDPEOListName | LIST_NAME | — | — |
| 105 | FdLinesCrtdByPersonNameDPEOMiddleNames | MIDDLE_NAMES | — | — |
| 106 | FdLinesCrtdByPersonNameDPEOMilitaryRank | MILITARY_RANK | — | — |
| 107 | FdLinesCrtdByPersonNameDPEONameType | NAME_TYPE | — | — |
| 108 | FdLinesCrtdByPersonNameDPEOObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 109 | FdLinesCrtdByPersonNameDPEOObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 110 | FdLinesCrtdByPersonNameDPEOOrderName | ORDER_NAME | — | — |
| 111 | FdLinesCrtdByPersonNameDPEOPersonId2 | PERSON_ID | — | — |
| 112 | FdLinesCrtdByPersonNameDPEOPersonNameId | PERSON_NAME_ID | — | — |
| 113 | FdLinesCrtdByPersonNameDPEOPersonNameId1 | PERSON_NAME_ID | — | — |
| 114 | FdLinesCrtdByPersonNameDPEOPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 115 | FdLinesCrtdByPersonNameDPEOPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 116 | FdLinesCrtdByPersonNameDPEOSuffix | SUFFIX | — | — |
| 117 | FdLinesCrtdByPersonNameDPEOTitle | TITLE | — | — |
| 118 | FdLinesLastUpdByPersonNameDPCreatedBy5 | CREATED_BY | — | — |
| 119 | FdLinesLastUpdByPersonNameDPCreationDate5 | CREATION_DATE | — | — |
| 120 | FdLinesLastUpdByPersonNameDPDisplayName1 | DISPLAY_NAME | — | — |
| 121 | FdLinesLastUpdByPersonNameDPEffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 122 | FdLinesLastUpdByPersonNameDPEffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 123 | FdLinesLastUpdByPersonNameDPFirstName1 | FIRST_NAME | — | — |
| 124 | FdLinesLastUpdByPersonNameDPFullName1 | FULL_NAME | — | — |
| 125 | FdLinesLastUpdByPersonNameDPHonors1 | HONORS | — | — |
| 126 | FdLinesLastUpdByPersonNameDPKnownAs1 | KNOWN_AS | — | — |
| 127 | FdLinesLastUpdByPersonNameDPLastName1 | LAST_NAME | — | — |
| 128 | FdLinesLastUpdByPersonNameDPLastUpdateDate5 | LAST_UPDATE_DATE | — | — |
| 129 | FdLinesLastUpdByPersonNameDPLastUpdateLogin5 | LAST_UPDATE_LOGIN | — | — |
| 130 | FdLinesLastUpdByPersonNameDPLastUpdatedBy5 | LAST_UPDATED_BY | — | — |
| 131 | FdLinesLastUpdByPersonNameDPLegislationCode1 | LEGISLATION_CODE | — | — |
| 132 | FdLinesLastUpdByPersonNameDPListName1 | LIST_NAME | — | — |
| 133 | FdLinesLastUpdByPersonNameDPMiddleNames1 | MIDDLE_NAMES | — | — |
| 134 | FdLinesLastUpdByPersonNameDPMilitaryRank1 | MILITARY_RANK | — | — |
| 135 | FdLinesLastUpdByPersonNameDPNameType1 | NAME_TYPE | — | — |
| 136 | FdLinesLastUpdByPersonNameDPObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |
| 137 | FdLinesLastUpdByPersonNameDPObjectVersionNumber7 | OBJECT_VERSION_NUMBER | — | — |
| 138 | FdLinesLastUpdByPersonNameDPOrderName1 | ORDER_NAME | — | — |
| 139 | FdLinesLastUpdByPersonNameDPPersonId3 | PERSON_ID | — | — |
| 140 | FdLinesLastUpdByPersonNameDPPersonNameId2 | PERSON_NAME_ID | — | — |
| 141 | FdLinesLastUpdByPersonNameDPPersonNameId3 | PERSON_NAME_ID | — | — |
| 142 | FdLinesLastUpdByPersonNameDPPreNameAdjunct1 | PRE_NAME_ADJUNCT | — | — |
| 143 | FdLinesLastUpdByPersonNameDPPreviousLastName1 | PREVIOUS_LAST_NAME | — | — |
| 144 | FdLinesLastUpdByPersonNameDPSuffix1 | SUFFIX | — | — |
| 145 | FdLinesLastUpdByPersonNameDPTitle1 | TITLE | — | — |
| 146 | FdTLCrtdByPersonNameDPEOBusinessGroupId10 | BUSINESS_GROUP_ID | — | — |
| 147 | FdTLCrtdByPersonNameDPEOCreatedBy12 | CREATED_BY | — | — |
| 148 | FdTLCrtdByPersonNameDPEOCreationDate12 | CREATION_DATE | — | — |
| 149 | FdTLCrtdByPersonNameDPEODisplayName4 | DISPLAY_NAME | — | — |
| 150 | FdTLCrtdByPersonNameDPEOEffectiveEndDate4 | EFFECTIVE_END_DATE | — | — |
| 151 | FdTLCrtdByPersonNameDPEOEffectiveStartDate4 | EFFECTIVE_START_DATE | — | — |
| 152 | FdTLCrtdByPersonNameDPEOFirstName4 | FIRST_NAME | — | — |
| 153 | FdTLCrtdByPersonNameDPEOFullName4 | FULL_NAME | — | — |
| 154 | FdTLCrtdByPersonNameDPEOHonors4 | HONORS | — | — |
| 155 | FdTLCrtdByPersonNameDPEOKnownAs4 | KNOWN_AS | — | — |
| 156 | FdTLCrtdByPersonNameDPEOLastName4 | LAST_NAME | — | — |
| 157 | FdTLCrtdByPersonNameDPEOLastUpdateDate12 | LAST_UPDATE_DATE | — | — |
| 158 | FdTLCrtdByPersonNameDPEOLastUpdateLogin12 | LAST_UPDATE_LOGIN | — | — |
| 159 | FdTLCrtdByPersonNameDPEOLastUpdatedBy12 | LAST_UPDATED_BY | — | — |
| 160 | FdTLCrtdByPersonNameDPEOLegislationCode4 | LEGISLATION_CODE | — | — |
| 161 | FdTLCrtdByPersonNameDPEOListName4 | LIST_NAME | — | — |
| 162 | FdTLCrtdByPersonNameDPEOMiddleNames4 | MIDDLE_NAMES | — | — |
| 163 | FdTLCrtdByPersonNameDPEOMilitaryRank4 | MILITARY_RANK | — | — |
| 164 | FdTLCrtdByPersonNameDPEONameType4 | NAME_TYPE | — | — |
| 165 | FdTLCrtdByPersonNameDPEOObjectVersionNumber16 | OBJECT_VERSION_NUMBER | — | — |
| 166 | FdTLCrtdByPersonNameDPEOObjectVersionNumber17 | OBJECT_VERSION_NUMBER | — | — |
| 167 | FdTLCrtdByPersonNameDPEOOrderName4 | ORDER_NAME | — | — |
| 168 | FdTLCrtdByPersonNameDPEOPersonId10 | PERSON_ID | — | — |
| 169 | FdTLCrtdByPersonNameDPEOPersonNameId8 | PERSON_NAME_ID | — | — |
| 170 | FdTLCrtdByPersonNameDPEOPersonNameId9 | PERSON_NAME_ID | — | — |
| 171 | FdTLCrtdByPersonNameDPEOPreNameAdjunct4 | PRE_NAME_ADJUNCT | — | — |
| 172 | FdTLCrtdByPersonNameDPEOPreviousLastName4 | PREVIOUS_LAST_NAME | — | — |
| 173 | FdTLCrtdByPersonNameDPEOSuffix4 | SUFFIX | — | — |
| 174 | FdTLCrtdByPersonNameDPEOTitle4 | TITLE | — | — |
| 175 | FdTLLastUpdByPersonNameDPEOBusinessGroupId11 | BUSINESS_GROUP_ID | — | — |
| 176 | FdTLLastUpdByPersonNameDPEOCreatedBy13 | CREATED_BY | — | — |
| 177 | FdTLLastUpdByPersonNameDPEOCreationDate13 | CREATION_DATE | — | — |
| 178 | FdTLLastUpdByPersonNameDPEODisplayName5 | DISPLAY_NAME | — | — |
| 179 | FdTLLastUpdByPersonNameDPEOEffectiveEndDate5 | EFFECTIVE_END_DATE | — | — |
| 180 | FdTLLastUpdByPersonNameDPEOEffectiveStartDate5 | EFFECTIVE_START_DATE | — | — |
| 181 | FdTLLastUpdByPersonNameDPEOFirstName5 | FIRST_NAME | — | — |
| 182 | FdTLLastUpdByPersonNameDPEOFullName5 | FULL_NAME | — | — |
| 183 | FdTLLastUpdByPersonNameDPEOHonors5 | HONORS | — | — |
| 184 | FdTLLastUpdByPersonNameDPEOKnownAs5 | KNOWN_AS | — | — |
| 185 | FdTLLastUpdByPersonNameDPEOLastName5 | LAST_NAME | — | — |
| 186 | FdTLLastUpdByPersonNameDPEOLastUpdateDate13 | LAST_UPDATE_DATE | — | — |
| 187 | FdTLLastUpdByPersonNameDPEOLastUpdateLogin13 | LAST_UPDATE_LOGIN | — | — |
| 188 | FdTLLastUpdByPersonNameDPEOLastUpdatedBy13 | LAST_UPDATED_BY | — | — |
| 189 | FdTLLastUpdByPersonNameDPEOLegislationCode5 | LEGISLATION_CODE | — | — |
| 190 | FdTLLastUpdByPersonNameDPEOListName5 | LIST_NAME | — | — |
| 191 | FdTLLastUpdByPersonNameDPEOMiddleNames5 | MIDDLE_NAMES | — | — |
| 192 | FdTLLastUpdByPersonNameDPEOMilitaryRank5 | MILITARY_RANK | — | — |
| 193 | FdTLLastUpdByPersonNameDPEONameType5 | NAME_TYPE | — | — |
| 194 | FdTLLastUpdByPersonNameDPEOObjectVersionNumber18 | OBJECT_VERSION_NUMBER | — | — |
| 195 | FdTLLastUpdByPersonNameDPEOObjectVersionNumber19 | OBJECT_VERSION_NUMBER | — | — |
| 196 | FdTLLastUpdByPersonNameDPEOOrderName5 | ORDER_NAME | — | — |
| 197 | FdTLLastUpdByPersonNameDPEOPersonId11 | PERSON_ID | — | — |
| 198 | FdTLLastUpdByPersonNameDPEOPersonNameId10 | PERSON_NAME_ID | — | — |
| 199 | FdTLLastUpdByPersonNameDPEOPersonNameId11 | PERSON_NAME_ID | — | — |
| 200 | FdTLLastUpdByPersonNameDPEOPreNameAdjunct5 | PRE_NAME_ADJUNCT | — | — |
| 201 | FdTLLastUpdByPersonNameDPEOPreviousLastName5 | PREVIOUS_LAST_NAME | — | — |
| 202 | FdTLLastUpdByPersonNameDPEOSuffix5 | SUFFIX | — | — |
| 203 | FdTLLastUpdByPersonNameDPEOTitle5 | TITLE | — | — |
| 204 | LastUpdatedByPersonNameDPEOAttributeCategory11 | ATTRIBUTE_CATEGORY | — | — |
| 205 | LastUpdatedByPersonNameDPEOBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 206 | LastUpdatedByPersonNameDPEOCreatedBy14 | CREATED_BY | — | — |
| 207 | LastUpdatedByPersonNameDPEOCreationDate14 | CREATION_DATE | — | — |
| 208 | LastUpdatedByPersonNameDPEODisplayName1 | DISPLAY_NAME | — | — |
| 209 | LastUpdatedByPersonNameDPEOEffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 210 | LastUpdatedByPersonNameDPEOEffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 211 | LastUpdatedByPersonNameDPEOFirstName1 | FIRST_NAME | — | — |
| 212 | LastUpdatedByPersonNameDPEOFullName1 | FULL_NAME | — | — |
| 213 | LastUpdatedByPersonNameDPEOHonors1 | HONORS | — | — |
| 214 | LastUpdatedByPersonNameDPEOKnownAs1 | KNOWN_AS | — | — |
| 215 | LastUpdatedByPersonNameDPEOLastName1 | LAST_NAME | — | — |
| 216 | LastUpdatedByPersonNameDPEOLastUpdateDate14 | LAST_UPDATE_DATE | — | — |
| 217 | LastUpdatedByPersonNameDPEOLastUpdateLogin14 | LAST_UPDATE_LOGIN | — | — |
| 218 | LastUpdatedByPersonNameDPEOLastUpdatedBy14 | LAST_UPDATED_BY | — | — |
| 219 | LastUpdatedByPersonNameDPEOLegislationCode1 | LEGISLATION_CODE | — | — |
| 220 | LastUpdatedByPersonNameDPEOListName1 | LIST_NAME | — | — |
| 221 | LastUpdatedByPersonNameDPEOMiddleNames1 | MIDDLE_NAMES | — | — |
| 222 | LastUpdatedByPersonNameDPEOMilitaryRank1 | MILITARY_RANK | — | — |
| 223 | LastUpdatedByPersonNameDPEONamInformationCategory1 | NAM_INFORMATION_CATEGORY | — | — |
| 224 | LastUpdatedByPersonNameDPEONameType1 | NAME_TYPE | — | — |
| 225 | LastUpdatedByPersonNameDPEOObjectVersionNumber13 | OBJECT_VERSION_NUMBER | — | — |
| 226 | LastUpdatedByPersonNameDPEOOrderName1 | ORDER_NAME | — | — |
| 227 | LastUpdatedByPersonNameDPEOPersonId3 | PERSON_ID | — | — |
| 228 | LastUpdatedByPersonNameDPEOPersonNameId1 | PERSON_NAME_ID | — | — |
| 229 | LastUpdatedByPersonNameDPEOPreNameAdjunct1 | PRE_NAME_ADJUNCT | — | — |
| 230 | LastUpdatedByPersonNameDPEOPreviousLastName1 | PREVIOUS_LAST_NAME | — | — |
| 231 | LastUpdatedByPersonNameDPEOSuffix1 | SUFFIX | — | — |
| 232 | LastUpdatedByPersonNameDPEOTitle1 | TITLE | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedByUserPEOActiveFlag1 | ACTIVE_FLAG | — | — |
| 2 | CreatedByUserPEOBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 3 | CreatedByUserPEOCreatedBy12 | CREATED_BY | — | — |
| 4 | CreatedByUserPEOCreationDate12 | CREATION_DATE | — | — |
| 5 | CreatedByUserPEOCredentialsEmailSent1 | CREDENTIALS_EMAIL_SENT | — | — |
| 6 | CreatedByUserPEOEndDate1 | END_DATE | — | — |
| 7 | CreatedByUserPEOExternalId1 | EXTERNAL_ID | — | — |
| 8 | CreatedByUserPEOHrTerminated1 | HR_TERMINATED | — | — |
| 9 | CreatedByUserPEOLastUpdateDate12 | LAST_UPDATE_DATE | — | — |
| 10 | CreatedByUserPEOLastUpdateLogin12 | LAST_UPDATE_LOGIN | — | — |
| 11 | CreatedByUserPEOLastUpdatedBy12 | LAST_UPDATED_BY | — | — |
| 12 | CreatedByUserPEOMultitenancyUsername1 | MULTITENANCY_USERNAME | — | — |
| 13 | CreatedByUserPEOObjectVersionNumber11 | OBJECT_VERSION_NUMBER | — | — |
| 14 | CreatedByUserPEOPartyId1 | PARTY_ID | — | — |
| 15 | CreatedByUserPEOPersonId1 | PERSON_ID | — | — |
| 16 | CreatedByUserPEOStartDate1 | START_DATE | — | — |
| 17 | CreatedByUserPEOSuspended1 | SUSPENDED | — | — |
| 18 | CreatedByUserPEOUserDataChecksum1 | USER_DATA_CHECKSUM | — | — |
| 19 | CreatedByUserPEOUserDistinguishedName1 | USER_DISTINGUISHED_NAME | — | — |
| 20 | CreatedByUserPEOUserGuid1 | USER_GUID | — | — |
| 21 | CreatedByUserPEOUserId1 | USER_ID | — | — |
| 22 | CreatedByUserPEOUsername1 | USERNAME | — | — |
| 23 | FdHdrExtnCrtdByUserPEOActiveFlag2 | ACTIVE_FLAG | — | — |
| 24 | FdHdrExtnCrtdByUserPEOBusinessGroupId4 | BUSINESS_GROUP_ID | — | — |
| 25 | FdHdrExtnCrtdByUserPEOCreatedBy6 | CREATED_BY | — | — |
| 26 | FdHdrExtnCrtdByUserPEOCreationDate6 | CREATION_DATE | — | — |
| 27 | FdHdrExtnCrtdByUserPEOCredentialsEmailSent2 | CREDENTIALS_EMAIL_SENT | — | — |
| 28 | FdHdrExtnCrtdByUserPEOEndDate2 | END_DATE | — | — |
| 29 | FdHdrExtnCrtdByUserPEOExternalId2 | EXTERNAL_ID | — | — |
| 30 | FdHdrExtnCrtdByUserPEOHrTerminated2 | HR_TERMINATED | — | — |
| 31 | FdHdrExtnCrtdByUserPEOLastUpdateDate6 | LAST_UPDATE_DATE | — | — |
| 32 | FdHdrExtnCrtdByUserPEOLastUpdateLogin6 | LAST_UPDATE_LOGIN | — | — |
| 33 | FdHdrExtnCrtdByUserPEOLastUpdatedBy6 | LAST_UPDATED_BY | — | — |
| 34 | FdHdrExtnCrtdByUserPEOMultitenancyUsername2 | MULTITENANCY_USERNAME | — | — |
| 35 | FdHdrExtnCrtdByUserPEOObjectVersionNumber8 | OBJECT_VERSION_NUMBER | — | — |
| 36 | FdHdrExtnCrtdByUserPEOPartyId2 | PARTY_ID | — | — |
| 37 | FdHdrExtnCrtdByUserPEOPersonId4 | PERSON_ID | — | — |
| 38 | FdHdrExtnCrtdByUserPEOStartDate2 | START_DATE | — | — |
| 39 | FdHdrExtnCrtdByUserPEOSuspended2 | SUSPENDED | — | — |
| 40 | FdHdrExtnCrtdByUserPEOUserDataChecksum2 | USER_DATA_CHECKSUM | — | — |
| 41 | FdHdrExtnCrtdByUserPEOUserDistinguishedName2 | USER_DISTINGUISHED_NAME | — | — |
| 42 | FdHdrExtnCrtdByUserPEOUserGuid2 | USER_GUID | — | — |
| 43 | FdHdrExtnCrtdByUserPEOUserId2 | USER_ID | — | — |
| 44 | FdHdrExtnCrtdByUserPEOUsername2 | USERNAME | — | — |
| 45 | FdHdrExtnLastUpdByUserPEOActiveFlag3 | ACTIVE_FLAG | — | — |
| 46 | FdHdrExtnLastUpdByUserPEOBusinessGroupId5 | BUSINESS_GROUP_ID | — | — |
| 47 | FdHdrExtnLastUpdByUserPEOCreatedBy7 | CREATED_BY | — | — |
| 48 | FdHdrExtnLastUpdByUserPEOCreationDate7 | CREATION_DATE | — | — |
| 49 | FdHdrExtnLastUpdByUserPEOCredentialsEmailSent3 | CREDENTIALS_EMAIL_SENT | — | — |
| 50 | FdHdrExtnLastUpdByUserPEOEndDate3 | END_DATE | — | — |
| 51 | FdHdrExtnLastUpdByUserPEOExternalId3 | EXTERNAL_ID | — | — |
| 52 | FdHdrExtnLastUpdByUserPEOHrTerminated3 | HR_TERMINATED | — | — |
| 53 | FdHdrExtnLastUpdByUserPEOLastUpdateDate7 | LAST_UPDATE_DATE | — | — |
| 54 | FdHdrExtnLastUpdByUserPEOLastUpdateLogin7 | LAST_UPDATE_LOGIN | — | — |
| 55 | FdHdrExtnLastUpdByUserPEOLastUpdatedBy7 | LAST_UPDATED_BY | — | — |
| 56 | FdHdrExtnLastUpdByUserPEOMultitenancyUsername3 | MULTITENANCY_USERNAME | — | — |
| 57 | FdHdrExtnLastUpdByUserPEOObjectVersionNumber9 | OBJECT_VERSION_NUMBER | — | — |
| 58 | FdHdrExtnLastUpdByUserPEOPartyId3 | PARTY_ID | — | — |
| 59 | FdHdrExtnLastUpdByUserPEOPersonId5 | PERSON_ID | — | — |
| 60 | FdHdrExtnLastUpdByUserPEOStartDate3 | START_DATE | — | — |
| 61 | FdHdrExtnLastUpdByUserPEOSuspended3 | SUSPENDED | — | — |
| 62 | FdHdrExtnLastUpdByUserPEOUserDataChecksum3 | USER_DATA_CHECKSUM | — | — |
| 63 | FdHdrExtnLastUpdByUserPEOUserDistinguishedName3 | USER_DISTINGUISHED_NAME | — | — |
| 64 | FdHdrExtnLastUpdByUserPEOUserGuid3 | USER_GUID | — | — |
| 65 | FdHdrExtnLastUpdByUserPEOUsername3 | USERNAME | — | — |
| 66 | FdLinesCrtdByUserPEOActiveFlag | ACTIVE_FLAG | — | — |
| 67 | FdLinesCrtdByUserPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 68 | FdLinesCrtdByUserPEOCreatedBy2 | CREATED_BY | — | — |
| 69 | FdLinesCrtdByUserPEOCreationDate2 | CREATION_DATE | — | — |
| 70 | FdLinesCrtdByUserPEOCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 71 | FdLinesCrtdByUserPEOEndDate | END_DATE | — | — |
| 72 | FdLinesCrtdByUserPEOExternalId | EXTERNAL_ID | — | — |
| 73 | FdLinesCrtdByUserPEOHrTerminated | HR_TERMINATED | — | — |
| 74 | FdLinesCrtdByUserPEOLastUpdateDate2 | LAST_UPDATE_DATE | — | — |
| 75 | FdLinesCrtdByUserPEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 76 | FdLinesCrtdByUserPEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 77 | FdLinesCrtdByUserPEOMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 78 | FdLinesCrtdByUserPEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 79 | FdLinesCrtdByUserPEOPartyId | PARTY_ID | — | — |
| 80 | FdLinesCrtdByUserPEOPersonId | PERSON_ID | — | — |
| 81 | FdLinesCrtdByUserPEOStartDate | START_DATE | — | — |
| 82 | FdLinesCrtdByUserPEOSuspended | SUSPENDED | — | — |
| 83 | FdLinesCrtdByUserPEOUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 84 | FdLinesCrtdByUserPEOUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 85 | FdLinesCrtdByUserPEOUserGuid | USER_GUID | — | — |
| 86 | FdLinesCrtdByUserPEOUserId | USER_ID | — | — |
| 87 | FdLinesCrtdByUserPEOUsername | USERNAME | — | — |
| 88 | FdLinesLastUpdByUserPEOActiveFlag1 | ACTIVE_FLAG | — | — |
| 89 | FdLinesLastUpdByUserPEOBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 90 | FdLinesLastUpdByUserPEOCreatedBy3 | CREATED_BY | — | — |
| 91 | FdLinesLastUpdByUserPEOCreationDate3 | CREATION_DATE | — | — |
| 92 | FdLinesLastUpdByUserPEOCredentialsEmailSent1 | CREDENTIALS_EMAIL_SENT | — | — |
| 93 | FdLinesLastUpdByUserPEOEndDate1 | END_DATE | — | — |
| 94 | FdLinesLastUpdByUserPEOExternalId1 | EXTERNAL_ID | — | — |
| 95 | FdLinesLastUpdByUserPEOHrTerminated1 | HR_TERMINATED | — | — |
| 96 | FdLinesLastUpdByUserPEOLastUpdateDate3 | LAST_UPDATE_DATE | — | — |
| 97 | FdLinesLastUpdByUserPEOLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 98 | FdLinesLastUpdByUserPEOLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 99 | FdLinesLastUpdByUserPEOMultitenancyUsername1 | MULTITENANCY_USERNAME | — | — |
| 100 | FdLinesLastUpdByUserPEOObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 101 | FdLinesLastUpdByUserPEOPartyId1 | PARTY_ID | — | — |
| 102 | FdLinesLastUpdByUserPEOPersonId1 | PERSON_ID | — | — |
| 103 | FdLinesLastUpdByUserPEOStartDate1 | START_DATE | — | — |
| 104 | FdLinesLastUpdByUserPEOSuspended1 | SUSPENDED | — | — |
| 105 | FdLinesLastUpdByUserPEOUserDataChecksum1 | USER_DATA_CHECKSUM | — | — |
| 106 | FdLinesLastUpdByUserPEOUserDistinguishedName1 | USER_DISTINGUISHED_NAME | — | — |
| 107 | FdLinesLastUpdByUserPEOUserGuid1 | USER_GUID | — | — |
| 108 | FdLinesLastUpdByUserPEOUsername1 | USERNAME | — | — |
| 109 | FdTaxLineCrtdByUserPEOActiveFlag4 | ACTIVE_FLAG | — | — |
| 110 | FdTaxLineCrtdByUserPEOBusinessGroupId8 | BUSINESS_GROUP_ID | — | — |
| 111 | FdTaxLineCrtdByUserPEOCreatedBy10 | CREATED_BY | — | — |
| 112 | FdTaxLineCrtdByUserPEOCreationDate10 | CREATION_DATE | — | — |
| 113 | FdTaxLineCrtdByUserPEOCredentialsEmailSent4 | CREDENTIALS_EMAIL_SENT | — | — |
| 114 | FdTaxLineCrtdByUserPEOEndDate4 | END_DATE | — | — |
| 115 | FdTaxLineCrtdByUserPEOExternalId4 | EXTERNAL_ID | — | — |
| 116 | FdTaxLineCrtdByUserPEOHrTerminated4 | HR_TERMINATED | — | — |
| 117 | FdTaxLineCrtdByUserPEOLastUpdateDate10 | LAST_UPDATE_DATE | — | — |
| 118 | FdTaxLineCrtdByUserPEOLastUpdateLogin10 | LAST_UPDATE_LOGIN | — | — |
| 119 | FdTaxLineCrtdByUserPEOLastUpdatedBy10 | LAST_UPDATED_BY | — | — |
| 120 | FdTaxLineCrtdByUserPEOMultitenancyUsername4 | MULTITENANCY_USERNAME | — | — |
| 121 | FdTaxLineCrtdByUserPEOObjectVersionNumber14 | OBJECT_VERSION_NUMBER | — | — |
| 122 | FdTaxLineCrtdByUserPEOPartyId4 | PARTY_ID | — | — |
| 123 | FdTaxLineCrtdByUserPEOPersonId8 | PERSON_ID | — | — |
| 124 | FdTaxLineCrtdByUserPEOStartDate4 | START_DATE | — | — |
| 125 | FdTaxLineCrtdByUserPEOSuspended4 | SUSPENDED | — | — |
| 126 | FdTaxLineCrtdByUserPEOUserDataChecksum4 | USER_DATA_CHECKSUM | — | — |
| 127 | FdTaxLineCrtdByUserPEOUserDistinguishedName4 | USER_DISTINGUISHED_NAME | — | — |
| 128 | FdTaxLineCrtdByUserPEOUserGuid4 | USER_GUID | — | — |
| 129 | FdTaxLineCrtdByUserPEOUserId4 | USER_ID | — | — |
| 130 | FdTaxLineCrtdByUserPEOUsername4 | USERNAME | — | — |
| 131 | FdTaxLineLastUpdByUserPEOActiveFlag5 | ACTIVE_FLAG | — | — |
| 132 | FdTaxLineLastUpdByUserPEOBusinessGroupId9 | BUSINESS_GROUP_ID | — | — |
| 133 | FdTaxLineLastUpdByUserPEOCreatedBy11 | CREATED_BY | — | — |
| 134 | FdTaxLineLastUpdByUserPEOCreationDate11 | CREATION_DATE | — | — |
| 135 | FdTaxLineLastUpdByUserPEOCredentialsEmailSent5 | CREDENTIALS_EMAIL_SENT | — | — |
| 136 | FdTaxLineLastUpdByUserPEOEndDate5 | END_DATE | — | — |
| 137 | FdTaxLineLastUpdByUserPEOExternalId5 | EXTERNAL_ID | — | — |
| 138 | FdTaxLineLastUpdByUserPEOHrTerminated5 | HR_TERMINATED | — | — |
| 139 | FdTaxLineLastUpdByUserPEOLastUpdateDate11 | LAST_UPDATE_DATE | — | — |
| 140 | FdTaxLineLastUpdByUserPEOLastUpdateLogin11 | LAST_UPDATE_LOGIN | — | — |
| 141 | FdTaxLineLastUpdByUserPEOLastUpdatedBy11 | LAST_UPDATED_BY | — | — |
| 142 | FdTaxLineLastUpdByUserPEOMultitenancyUsername5 | MULTITENANCY_USERNAME | — | — |
| 143 | FdTaxLineLastUpdByUserPEOObjectVersionNumber15 | OBJECT_VERSION_NUMBER | — | — |
| 144 | FdTaxLineLastUpdByUserPEOPartyId5 | PARTY_ID | — | — |
| 145 | FdTaxLineLastUpdByUserPEOPersonId9 | PERSON_ID | — | — |
| 146 | FdTaxLineLastUpdByUserPEOStartDate5 | START_DATE | — | — |
| 147 | FdTaxLineLastUpdByUserPEOSuspended5 | SUSPENDED | — | — |
| 148 | FdTaxLineLastUpdByUserPEOUserDataChecksum5 | USER_DATA_CHECKSUM | — | — |
| 149 | FdTaxLineLastUpdByUserPEOUserDistinguishedName5 | USER_DISTINGUISHED_NAME | — | — |
| 150 | FdTaxLineLastUpdByUserPEOUserGuid5 | USER_GUID | — | — |
| 151 | FdTaxLineLastUpdByUserPEOUserId5 | USER_ID | — | — |
| 152 | FdTaxLineLastUpdByUserPEOUsername5 | USERNAME | — | — |
| 153 | LastUpdatedUserPEOActiveFlag | ACTIVE_FLAG | — | — |
| 154 | LastUpdatedUserPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 155 | LastUpdatedUserPEOCreatedBy11 | CREATED_BY | — | — |
| 156 | LastUpdatedUserPEOCreationDate11 | CREATION_DATE | — | — |
| 157 | LastUpdatedUserPEOCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 158 | LastUpdatedUserPEOEndDate | END_DATE | — | — |
| 159 | LastUpdatedUserPEOExternalId | EXTERNAL_ID | — | — |
| 160 | LastUpdatedUserPEOHrTerminated | HR_TERMINATED | — | — |
| 161 | LastUpdatedUserPEOLastUpdateDate11 | LAST_UPDATE_DATE | — | — |
| 162 | LastUpdatedUserPEOLastUpdateLogin11 | LAST_UPDATE_LOGIN | — | — |
| 163 | LastUpdatedUserPEOLastUpdatedBy11 | LAST_UPDATED_BY | — | — |
| 164 | LastUpdatedUserPEOMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 165 | LastUpdatedUserPEOObjectVersionNumber10 | OBJECT_VERSION_NUMBER | — | — |
| 166 | LastUpdatedUserPEOPartyId | PARTY_ID | — | — |
| 167 | LastUpdatedUserPEOPersonId | PERSON_ID | — | — |
| 168 | LastUpdatedUserPEOStartDate | START_DATE | — | — |
| 169 | LastUpdatedUserPEOSuspended | SUSPENDED | — | — |
| 170 | LastUpdatedUserPEOUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 171 | LastUpdatedUserPEOUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 172 | LastUpdatedUserPEOUserGuid | USER_GUID | — | — |
| 173 | LastUpdatedUserPEOUserId | USER_ID | — | — |
| 174 | LastUpdatedUserPEOUsername | USERNAME | — | — |
| 175 | UserId1 | USER_ID | — | — |
| 176 | UserId3 | USER_ID | — | — |

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
| 6 | LineIntendedUsePEOName3 | NAME | — | — |

### [[zx_fc_product_categories_v|ZX_FC_PRODUCT_CATEGORIES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProductCategoriesPEOClassificationCode1 | CLASSIFICATION_CODE | — | — |
| 2 | ProductCategoriesPEOClassificationId1 | CLASSIFICATION_ID | — | — |
| 3 | ProductCategoriesPEOClassificationName1 | CLASSIFICATION_NAME | — | — |
| 4 | ProductCategoriesPEOConcatLeafCode | CONCAT_LEAF_CODE | — | — |
| 5 | ProductCategoriesPEOConcatLeafName | CONCAT_LEAF_NAME | — | — |
| 6 | ProductCategoriesPEOCountryCode3 | COUNTRY_CODE | — | — |
| 7 | ProductCategoriesPEOEffectiveFrom2 | EFFECTIVE_FROM | — | — |
| 8 | ProductCategoriesPEOEffectiveTo2 | EFFECTIVE_TO | — | — |

### [[zx_fc_product_fiscal_v|ZX_FC_PRODUCT_FISCAL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProductFiscClassificatnsPEOCategoryId | CATEGORY_ID | — | — |
| 2 | ProductFiscClassificatnsPEOCategorySetId | CATEGORY_SET_ID | — | — |
| 3 | ProductFiscClassificatnsPEOClassificationCode2 | CLASSIFICATION_CODE | — | — |
| 4 | ProductFiscClassificatnsPEOClassificationName2 | CLASSIFICATION_NAME | — | — |
| 5 | ProductFiscClassificatnsPEOCountryCode4 | COUNTRY_CODE | — | — |
| 6 | ProductFiscClassificatnsPEOEffectiveTo3 | EFFECTIVE_TO | — | — |
| 7 | ProductFiscClassificatnsPEOStructureId | STRUCTURE_ID | — | — |
| 8 | ProductFiscClassificatnsPEOStructureName | STRUCTURE_NAME | — | — |

### [[zx_fc_user_defined_v|ZX_FC_USER_DEFINED_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserDefinedFiscClassPEOClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | UserDefinedFiscClassPEOClassificationName | CLASSIFICATION_NAME | — | — |
| 3 | UserDefinedFiscClassPEOCountryCode2 | COUNTRY_CODE | — | — |
| 4 | UserDefinedFiscClassPEOEffectiveFrom1 | EFFECTIVE_FROM | — | — |
| 5 | UserDefinedFiscClassPEOEffectiveTo1 | EFFECTIVE_TO | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
