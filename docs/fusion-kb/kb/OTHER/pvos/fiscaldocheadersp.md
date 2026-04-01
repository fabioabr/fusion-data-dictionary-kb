---
id: DOC-OTHER-PVO-FiscalDocHeadersP
doc_type: system-doc
title: "FiscalDocHeadersP — PVO Cross-Module"
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
  - FiscalDocHeadersP
  - fiscaldocheadersp
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FiscalDocHeadersP

## 📌 Visão Geral

View Object para extração BICC de dados de Fiscal Doc Headers P. Acessa as tabelas: AP_INVOICES_ALL, AP_PAYMENT_SCHEDULES_ALL, CMF_FD_LOC_INFO_PERSIST_OTBI_V (+9).

**Caminho:** `FscmTopModelAM.FiscalDocumentAM.FiscalDocHeadersP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 768 | 12 | 1 | 74 | 10% |

---

## 🔗 Tabelas Relacionadas

- [[ap_invoices_all|AP_INVOICES_ALL]] — 163 atributos
- [[ap_payment_schedules_all|AP_PAYMENT_SCHEDULES_ALL]] — 5 atributos
- [[cmf_fd_loc_info_persist_otbi_v|CMF_FD_LOC_INFO_PERSIST_OTBI_V]] — 79 atributos (12 BICC)
- [[cmf_fiscal_doc_headers|CMF_FISCAL_DOC_HEADERS]] — 60 atributos (1 PKs, 21 BICC)
- [[cmf_fiscal_proc_options|CMF_FISCAL_PROC_OPTIONS]] — 56 atributos
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 21 atributos
- [[inv_cons_advice_headers|INV_CONS_ADVICE_HEADERS]] — 25 atributos
- [[jg_fscl_hdrs_atrb_ext_all|JG_FSCL_HDRS_ATRB_EXT_ALL]] — 56 atributos (37 BICC)
- [[jg_fscl_hdr_dtls_atrb_ext_all|JG_FSCL_HDR_DTLS_ATRB_EXT_ALL]] — 20 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 112 atributos (4 BICC)
- [[per_users|PER_USERS]] — 88 atributos
- [[rcv_shipment_headers|RCV_SHIPMENT_HEADERS]] — 83 atributos

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

### [[cmf_fiscal_doc_headers|CMF_FISCAL_DOC_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocumentHeaderId | DOCUMENT_HEADER_ID | 🔑 | ✅ |
| 2 | FiscalDocHeadersPEOAccessKeyNumber | ACCESS_KEY_NUMBER | — | ✅ |
| 3 | FiscalDocHeadersPEOAcknowledgedDate | ACKNOWLEDGED_DATE | — | ✅ |
| 4 | FiscalDocHeadersPEOBillToBusinessUnitId | BILL_TO_BUSINESS_UNIT_ID | — | — |
| 5 | FiscalDocHeadersPEOChargeAllocationStatus | CHARGE_ALLOCATION_STATUS | — | ✅ |
| 6 | FiscalDocHeadersPEOCmrInterfacedFlag | CMR_INTERFACED_FLAG | — | ✅ |
| 7 | FiscalDocHeadersPEOConversionRate | CONVERSION_RATE | — | — |
| 8 | FiscalDocHeadersPEOConverstionType | CONVERSTION_TYPE | — | — |
| 9 | FiscalDocHeadersPEOCountryCode | COUNTRY_CODE | — | ✅ |
| 10 | FiscalDocHeadersPEOCreatedBy | CREATED_BY | — | — |
| 11 | FiscalDocHeadersPEOCreationDate | CREATION_DATE | — | ✅ |
| 12 | FiscalDocHeadersPEOCurrency | CURRENCY | — | ✅ |
| 13 | FiscalDocHeadersPEODocumentNumber | DOCUMENT_NUMBER | — | ✅ |
| 14 | FiscalDocHeadersPEODocumentStatus | DOCUMENT_STATUS | — | ✅ |
| 15 | FiscalDocHeadersPEODocumentType | DOCUMENT_TYPE | — | — |
| 16 | FiscalDocHeadersPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | — |
| 17 | FiscalDocHeadersPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | — |
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
| 28 | FiscalDocHeadersPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 29 | FiscalDocHeadersPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 30 | FiscalDocHeadersPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 31 | FiscalDocHeadersPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 32 | FiscalDocHeadersPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 33 | FiscalDocHeadersPEOModel | MODEL | — | ✅ |
| 34 | FiscalDocHeadersPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 35 | FiscalDocHeadersPEOOperationType | OPERATION_TYPE | — | — |
| 36 | FiscalDocHeadersPEOParentDocumentHeaderId | PARENT_DOCUMENT_HEADER_ID | — | — |
| 37 | FiscalDocHeadersPEOReason | REASON | — | — |
| 38 | FiscalDocHeadersPEOReceiverLocationId | RECEIVER_LOCATION_ID | — | — |
| 39 | FiscalDocHeadersPEOReceiverPartyId | RECEIVER_PARTY_ID | — | — |
| 40 | FiscalDocHeadersPEOReceiverPartySiteId | RECEIVER_PARTY_SITE_ID | — | — |
| 41 | FiscalDocHeadersPEOReceiverTaxId | RECEIVER_TAX_ID | — | — |
| 42 | FiscalDocHeadersPEOReferencedStatus | REFERENCED_STATUS | — | ✅ |
| 43 | FiscalDocHeadersPEORequestId | REQUEST_ID | — | — |
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
| 55 | FiscalDocHeadersPEOSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 56 | FiscalDocHeadersPEOSourceRefDocHeaderId | SOURCE_REF_DOC_HEADER_ID | — | — |
| 57 | FiscalDocHeadersPEOSubseries | SUBSERIES | — | ✅ |
| 58 | FiscalDocHeadersPEOTaxCalculationStatus | TAX_CALCULATION_STATUS | — | ✅ |
| 59 | FiscalDocHeadersPEOTotalAmount | TOTAL_AMOUNT | — | ✅ |
| 60 | FiscalDocHeadersPEOValidationStatus | VALIDATION_STATUS | — | — |

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
| 30 | FiscalDocHdrCreatdByPerBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 31 | FiscalDocHdrCreatdByPerCreatedBy3 | CREATED_BY | — | — |
| 32 | FiscalDocHdrCreatdByPerCreationDate3 | CREATION_DATE | — | — |
| 33 | FiscalDocHdrCreatdByPerDisplayName1 | DISPLAY_NAME | — | — |
| 34 | FiscalDocHdrCreatdByPerEffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 35 | FiscalDocHdrCreatdByPerEffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 36 | FiscalDocHdrCreatdByPerFirstName1 | FIRST_NAME | — | — |
| 37 | FiscalDocHdrCreatdByPerFullName1 | FULL_NAME | — | ✅ |
| 38 | FiscalDocHdrCreatdByPerHonors1 | HONORS | — | — |
| 39 | FiscalDocHdrCreatdByPerKnownAs1 | KNOWN_AS | — | — |
| 40 | FiscalDocHdrCreatdByPerLastName1 | LAST_NAME | — | — |
| 41 | FiscalDocHdrCreatdByPerLastUpdateDate3 | LAST_UPDATE_DATE | — | — |
| 42 | FiscalDocHdrCreatdByPerLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 43 | FiscalDocHdrCreatdByPerLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 44 | FiscalDocHdrCreatdByPerLegislationCode1 | LEGISLATION_CODE | — | — |
| 45 | FiscalDocHdrCreatdByPerListName1 | LIST_NAME | — | — |
| 46 | FiscalDocHdrCreatdByPerMiddleNames1 | MIDDLE_NAMES | — | — |
| 47 | FiscalDocHdrCreatdByPerMilitaryRank1 | MILITARY_RANK | — | — |
| 48 | FiscalDocHdrCreatdByPerNameType1 | NAME_TYPE | — | — |
| 49 | FiscalDocHdrCreatdByPerObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 50 | FiscalDocHdrCreatdByPerOrderName1 | ORDER_NAME | — | — |
| 51 | FiscalDocHdrCreatdByPerPersonId3 | PERSON_ID | — | — |
| 52 | FiscalDocHdrCreatdByPerPersonNameId1 | PERSON_NAME_ID | — | — |
| 53 | FiscalDocHdrCreatdByPerPreNameAdjunct1 | PRE_NAME_ADJUNCT | — | — |
| 54 | FiscalDocHdrCreatdByPerPreviousLastName1 | PREVIOUS_LAST_NAME | — | — |
| 55 | FiscalDocHdrCreatdByPerSuffix1 | SUFFIX | — | — |
| 56 | FiscalDocHdrCreatdByPerTitle1 | TITLE | — | — |
| 57 | FiscalDocHdrLastUpPerBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 58 | FiscalDocHdrLastUpPerCreatedBy2 | CREATED_BY | — | — |
| 59 | FiscalDocHdrLastUpPerCreationDate2 | CREATION_DATE | — | — |
| 60 | FiscalDocHdrLastUpPerDisplayName | DISPLAY_NAME | — | — |
| 61 | FiscalDocHdrLastUpPerEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 62 | FiscalDocHdrLastUpPerEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 63 | FiscalDocHdrLastUpPerFirstName | FIRST_NAME | — | — |
| 64 | FiscalDocHdrLastUpPerFullName | FULL_NAME | — | ✅ |
| 65 | FiscalDocHdrLastUpPerHonors | HONORS | — | — |
| 66 | FiscalDocHdrLastUpPerKnownAs | KNOWN_AS | — | — |
| 67 | FiscalDocHdrLastUpPerLastName | LAST_NAME | — | — |
| 68 | FiscalDocHdrLastUpPerLastUpdateDate2 | LAST_UPDATE_DATE | — | — |
| 69 | FiscalDocHdrLastUpPerLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 70 | FiscalDocHdrLastUpPerLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 71 | FiscalDocHdrLastUpPerLegislationCode | LEGISLATION_CODE | — | — |
| 72 | FiscalDocHdrLastUpPerListName | LIST_NAME | — | — |
| 73 | FiscalDocHdrLastUpPerMiddleNames | MIDDLE_NAMES | — | — |
| 74 | FiscalDocHdrLastUpPerMilitaryRank | MILITARY_RANK | — | — |
| 75 | FiscalDocHdrLastUpPerNameType | NAME_TYPE | — | — |
| 76 | FiscalDocHdrLastUpPerObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 77 | FiscalDocHdrLastUpPerOrderName | ORDER_NAME | — | — |
| 78 | FiscalDocHdrLastUpPerPersonId2 | PERSON_ID | — | — |
| 79 | FiscalDocHdrLastUpPerPersonNameId | PERSON_NAME_ID | — | — |
| 80 | FiscalDocHdrLastUpPerPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 81 | FiscalDocHdrLastUpPerPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 82 | FiscalDocHdrLastUpPerSuffix | SUFFIX | — | — |
| 83 | FiscalDocHdrLastUpPerTitle | TITLE | — | — |
| 84 | LastUpdatedByPersonNameDPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 85 | LastUpdatedByPersonNameDPEOCreatedBy | CREATED_BY | — | — |
| 86 | LastUpdatedByPersonNameDPEOCreationDate | CREATION_DATE | — | — |
| 87 | LastUpdatedByPersonNameDPEODisplayName | DISPLAY_NAME | — | — |
| 88 | LastUpdatedByPersonNameDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 89 | LastUpdatedByPersonNameDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 90 | LastUpdatedByPersonNameDPEOFirstName | FIRST_NAME | — | — |
| 91 | LastUpdatedByPersonNameDPEOFullName | FULL_NAME | — | ✅ |
| 92 | LastUpdatedByPersonNameDPEOHonors | HONORS | — | — |
| 93 | LastUpdatedByPersonNameDPEOKnownAs | KNOWN_AS | — | — |
| 94 | LastUpdatedByPersonNameDPEOLastName | LAST_NAME | — | — |
| 95 | LastUpdatedByPersonNameDPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 96 | LastUpdatedByPersonNameDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 97 | LastUpdatedByPersonNameDPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 98 | LastUpdatedByPersonNameDPEOLegislationCode | LEGISLATION_CODE | — | — |
| 99 | LastUpdatedByPersonNameDPEOListName | LIST_NAME | — | — |
| 100 | LastUpdatedByPersonNameDPEOMiddleNames | MIDDLE_NAMES | — | — |
| 101 | LastUpdatedByPersonNameDPEOMilitaryRank | MILITARY_RANK | — | — |
| 102 | LastUpdatedByPersonNameDPEONameType | NAME_TYPE | — | — |
| 103 | LastUpdatedByPersonNameDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 104 | LastUpdatedByPersonNameDPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 105 | LastUpdatedByPersonNameDPEOOrderName | ORDER_NAME | — | — |
| 106 | LastUpdatedByPersonNameDPEOPersonId | PERSON_ID | — | — |
| 107 | LastUpdatedByPersonNameDPEOPersonNameId | PERSON_NAME_ID | — | — |
| 108 | LastUpdatedByPersonNameDPEOPersonNameId1 | PERSON_NAME_ID | — | — |
| 109 | LastUpdatedByPersonNameDPEOPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 110 | LastUpdatedByPersonNameDPEOPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 111 | LastUpdatedByPersonNameDPEOSuffix | SUFFIX | — | — |
| 112 | LastUpdatedByPersonNameDPEOTitle | TITLE | — | — |

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
| 23 | FiscalDocHeaderExtnCreatedByActiveFlag | ACTIVE_FLAG | — | — |
| 24 | FiscalDocHeaderExtnCreatedByBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 25 | FiscalDocHeaderExtnCreatedByCreatedBy | CREATED_BY | — | — |
| 26 | FiscalDocHeaderExtnCreatedByCreationDate | CREATION_DATE | — | — |
| 27 | FiscalDocHeaderExtnCreatedByCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 28 | FiscalDocHeaderExtnCreatedByEndDate | END_DATE | — | — |
| 29 | FiscalDocHeaderExtnCreatedByExternalId | EXTERNAL_ID | — | — |
| 30 | FiscalDocHeaderExtnCreatedByHrTerminated | HR_TERMINATED | — | — |
| 31 | FiscalDocHeaderExtnCreatedByLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 32 | FiscalDocHeaderExtnCreatedByLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | FiscalDocHeaderExtnCreatedByLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 34 | FiscalDocHeaderExtnCreatedByMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 35 | FiscalDocHeaderExtnCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 36 | FiscalDocHeaderExtnCreatedByPartyId | PARTY_ID | — | — |
| 37 | FiscalDocHeaderExtnCreatedByPersonId | PERSON_ID | — | — |
| 38 | FiscalDocHeaderExtnCreatedByStartDate | START_DATE | — | — |
| 39 | FiscalDocHeaderExtnCreatedBySuspended | SUSPENDED | — | — |
| 40 | FiscalDocHeaderExtnCreatedByUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 41 | FiscalDocHeaderExtnCreatedByUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 42 | FiscalDocHeaderExtnCreatedByUserGuid | USER_GUID | — | — |
| 43 | FiscalDocHeaderExtnCreatedByUserId | USER_ID | — | — |
| 44 | FiscalDocHeaderExtnCreatedByUsername | USERNAME | — | — |
| 45 | FiscalDocHeaderExtnLastUpdatActiveFlag1 | ACTIVE_FLAG | — | — |
| 46 | FiscalDocHeaderExtnLastUpdatBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 47 | FiscalDocHeaderExtnLastUpdatCreatedBy1 | CREATED_BY | — | — |
| 48 | FiscalDocHeaderExtnLastUpdatCreationDate1 | CREATION_DATE | — | — |
| 49 | FiscalDocHeaderExtnLastUpdatCredentialsEmailSent1 | CREDENTIALS_EMAIL_SENT | — | — |
| 50 | FiscalDocHeaderExtnLastUpdatEndDate1 | END_DATE | — | — |
| 51 | FiscalDocHeaderExtnLastUpdatExternalId1 | EXTERNAL_ID | — | — |
| 52 | FiscalDocHeaderExtnLastUpdatHrTerminated1 | HR_TERMINATED | — | — |
| 53 | FiscalDocHeaderExtnLastUpdatLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 54 | FiscalDocHeaderExtnLastUpdatLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 55 | FiscalDocHeaderExtnLastUpdatLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 56 | FiscalDocHeaderExtnLastUpdatMultitenancyUsername1 | MULTITENANCY_USERNAME | — | — |
| 57 | FiscalDocHeaderExtnLastUpdatObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 58 | FiscalDocHeaderExtnLastUpdatPartyId1 | PARTY_ID | — | — |
| 59 | FiscalDocHeaderExtnLastUpdatPersonId1 | PERSON_ID | — | — |
| 60 | FiscalDocHeaderExtnLastUpdatStartDate1 | START_DATE | — | — |
| 61 | FiscalDocHeaderExtnLastUpdatSuspended1 | SUSPENDED | — | — |
| 62 | FiscalDocHeaderExtnLastUpdatUserDataChecksum1 | USER_DATA_CHECKSUM | — | — |
| 63 | FiscalDocHeaderExtnLastUpdatUserDistinguishedName1 | USER_DISTINGUISHED_NAME | — | — |
| 64 | FiscalDocHeaderExtnLastUpdatUserGuid1 | USER_GUID | — | — |
| 65 | FiscalDocHeaderExtnLastUpdatUserId1 | USER_ID | — | — |
| 66 | FiscalDocHeaderExtnLastUpdatUsername1 | USERNAME | — | — |
| 67 | LastUpdatedUserPEOActiveFlag | ACTIVE_FLAG | — | — |
| 68 | LastUpdatedUserPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 69 | LastUpdatedUserPEOCreatedBy | CREATED_BY | — | — |
| 70 | LastUpdatedUserPEOCreationDate | CREATION_DATE | — | — |
| 71 | LastUpdatedUserPEOCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 72 | LastUpdatedUserPEOEndDate | END_DATE | — | — |
| 73 | LastUpdatedUserPEOExternalId | EXTERNAL_ID | — | — |
| 74 | LastUpdatedUserPEOHrTerminated | HR_TERMINATED | — | — |
| 75 | LastUpdatedUserPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 76 | LastUpdatedUserPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 77 | LastUpdatedUserPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 78 | LastUpdatedUserPEOMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 79 | LastUpdatedUserPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 80 | LastUpdatedUserPEOPartyId | PARTY_ID | — | — |
| 81 | LastUpdatedUserPEOPersonId | PERSON_ID | — | — |
| 82 | LastUpdatedUserPEOStartDate | START_DATE | — | — |
| 83 | LastUpdatedUserPEOSuspended | SUSPENDED | — | — |
| 84 | LastUpdatedUserPEOUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 85 | LastUpdatedUserPEOUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 86 | LastUpdatedUserPEOUserGuid | USER_GUID | — | — |
| 87 | LastUpdatedUserPEOUserId | USER_ID | — | — |
| 88 | LastUpdatedUserPEOUsername | USERNAME | — | — |

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

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
