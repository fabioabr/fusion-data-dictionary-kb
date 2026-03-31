---
id: DOC-AP-PVO-InvoiceLinePVO
doc_type: system-doc
title: "InvoiceLinePVO — PVO Accounts Payable"
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
  - InvoiceLinePVO
  - invoicelinepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvoiceLinePVO

## 📌 Visão Geral

Extrai as linhas detalhadas das faturas de fornecedores, incluindo itens, quantidades, valores, impostos retidos, pedido de compra vinculado, projeto e distribuições contábeis. Viabiliza análise detalhada de gastos, conciliação com pedidos de compra e controle tributário linha a linha.

**Caminho:** `FscmTopModelAM.FinApInvTransactionsAM.InvoiceLinePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 395 | 55 | 2 | 203 | 51% |

---

## 🔗 Tabelas Relacionadas

- [[ap_batches_all|AP_BATCHES_ALL]] — 2 atributos (2 BICC)
- [[ap_distribution_sets_all|AP_DISTRIBUTION_SETS_ALL]] — 6 atributos (2 BICC)
- [[ap_invoices_all|AP_INVOICES_ALL]] — 90 atributos (63 BICC)
- [[ap_invoice_lines_all|AP_INVOICE_LINES_ALL]] — 88 atributos (2 PKs, 76 BICC)
- [[ap_inv_aprvl_hist_all|AP_INV_APRVL_HIST_ALL]] — 12 atributos
- [[egp_categories_vl|EGP_CATEGORIES_VL]] — 2 atributos (1 BICC)
- [[fa_book_controls|FA_BOOK_CONTROLS]] — 2 atributos (1 BICC)
- [[fnd_attached_documents|FND_ATTACHED_DOCUMENTS]] — 2 atributos
- [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]] — 2 atributos (1 BICC)
- [[fnd_doc_sequence_categories|FND_DOC_SEQUENCE_CATEGORIES]] — 4 atributos (2 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 1 atributos
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 2 atributos (1 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 2 atributos
- [[hr_all_organization_units_f_vl|HR_ALL_ORGANIZATION_UNITS_F_VL]] — 4 atributos (1 BICC)
- [[hr_locations|HR_LOCATIONS]] — 9 atributos
- [[hz_locations|HZ_LOCATIONS]] — 15 atributos
- [[hz_parties|HZ_PARTIES]] — 2 atributos (1 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 4 atributos (2 BICC)
- [[inv_cons_advice_txns_v|INV_CONS_ADVICE_TXNS_V]] — 3 atributos (2 BICC)
- [[inv_units_of_measure_b|INV_UNITS_OF_MEASURE_B]] — 2 atributos (1 BICC)
- [[inv_units_of_measure_tl|INV_UNITS_OF_MEASURE_TL]] — 4 atributos (2 BICC)
- [[per_location_details_f_vl|PER_LOCATION_DETAILS_F_VL]] — 4 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 41 atributos (7 BICC)
- [[per_users|PER_USERS]] — 7 atributos
- [[pjf_exp_types_tl|PJF_EXP_TYPES_TL]] — 3 atributos (1 BICC)
- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 2 atributos (1 BICC)
- [[pjf_projects_all_tl|PJF_PROJECTS_ALL_TL]] — 3 atributos (1 BICC)
- [[pjf_proj_elements_b|PJF_PROJ_ELEMENTS_B]] — 2 atributos (1 BICC)
- [[pjf_proj_elements_tl|PJF_PROJ_ELEMENTS_TL]] — 3 atributos (1 BICC)
- [[poz_suppliers_v|POZ_SUPPLIERS_V]] — 2 atributos (1 BICC)
- [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]] — 2 atributos (1 BICC)
- [[po_distributions_all|PO_DISTRIBUTIONS_ALL]] — 2 atributos (1 BICC)
- [[po_headers_all|PO_HEADERS_ALL]] — 7 atributos (5 BICC)
- [[po_lines_all|PO_LINES_ALL]] — 2 atributos (1 BICC)
- [[po_line_locations_all|PO_LINE_LOCATIONS_ALL]] — 2 atributos (1 BICC)
- [[po_system_parameters_all|PO_SYSTEM_PARAMETERS_ALL]] — 2 atributos
- [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]] — 2 atributos (1 BICC)
- [[rcv_shipment_headers|RCV_SHIPMENT_HEADERS]] — 2 atributos (1 BICC)
- [[rcv_shipment_lines|RCV_SHIPMENT_LINES]] — 2 atributos (1 BICC)
- [[rcv_transactions|RCV_TRANSACTIONS]] — 4 atributos (3 BICC)
- [[zx_condition_groups_b|ZX_CONDITION_GROUPS_B]] — 2 atributos
- [[zx_condition_groups_tl|ZX_CONDITION_GROUPS_TL]] — 3 atributos (1 BICC)
- [[zx_fc_codes_vl|ZX_FC_CODES_VL]] — 2 atributos (1 BICC)
- [[zx_jurisdictions_b|ZX_JURISDICTIONS_B]] — 2 atributos
- [[zx_jurisdictions_tl|ZX_JURISDICTIONS_TL]] — 3 atributos (1 BICC)
- [[zx_rates_vl|ZX_RATES_VL]] — 8 atributos (5 BICC)
- [[zx_regimes_b|ZX_REGIMES_B]] — 2 atributos
- [[zx_regimes_tl|ZX_REGIMES_TL]] — 3 atributos (1 BICC)
- [[zx_registrations|ZX_REGISTRATIONS]] — 4 atributos (2 BICC)
- [[zx_status_b|ZX_STATUS_B]] — 1 atributos
- [[zx_status_tl|ZX_STATUS_TL]] — 3 atributos
- [[zx_taxes_b|ZX_TAXES_B]] — 1 atributos
- [[zx_taxes_tl|ZX_TAXES_TL]] — 3 atributos (1 BICC)
- [[zx_tax_settlement_auths_f|ZX_TAX_SETTLEMENT_AUTHS_F]] — 3 atributos (2 BICC)
- [[zx_wht_lines_summary|ZX_WHT_LINES_SUMMARY]] — 3 atributos (2 BICC)

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
| 2 | DistributionSetDistributionSetName | DISTRIBUTION_SET_NAME | — | ✅ |
| 3 | DistributionSetLineDistributionSetId | DISTRIBUTION_SET_ID | — | — |
| 4 | DistributionSetLineDistributionSetName | DISTRIBUTION_SET_NAME | — | ✅ |
| 5 | DistributionSetLineOrgId | ORG_ID | — | — |
| 6 | DistributionSetOrgId | ORG_ID | — | — |

### [[ap_invoices_all|AP_INVOICES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvHdrCorrInvInvoiceId | INVOICE_ID | — | — |
| 2 | InvHdrCorrInvInvoiceNum | INVOICE_NUM | — | ✅ |
| 3 | InvHdrCrInvInvoiceId | INVOICE_ID | — | — |
| 4 | InvHdrCrInvInvoiceNum | INVOICE_NUM | — | ✅ |
| 5 | InvHdrPreInvInvoiceId | INVOICE_ID | — | — |
| 6 | InvHdrPreInvInvoiceNum | INVOICE_NUM | — | ✅ |
| 7 | InvHdrTaxRelInvInvoiceId | INVOICE_ID | — | — |
| 8 | InvHdrTaxRelInvInvoiceNum | INVOICE_NUM | — | ✅ |
| 9 | InvHdrTaxRelInvObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | InvLineAprvlPersonNameObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | InvoiceHdrTransactionDeadline | TRANSACTION_DEADLINE | — | ✅ |
| 12 | InvoiceHeaderAcctsPayCodeCombinationId | ACCTS_PAY_CODE_COMBINATION_ID | — | — |
| 13 | InvoiceHeaderApprovalDescription | APPROVAL_DESCRIPTION | — | ✅ |
| 14 | InvoiceHeaderApprovalIteration | APPROVAL_ITERATION | — | ✅ |
| 15 | InvoiceHeaderApprovalStatus | APPROVAL_STATUS | — | ✅ |
| 16 | InvoiceHeaderBudgetDate | BUDGET_DATE | — | ✅ |
| 17 | InvoiceHeaderCancelledBy | CANCELLED_BY | — | ✅ |
| 18 | InvoiceHeaderCancelledDate | CANCELLED_DATE | — | ✅ |
| 19 | InvoiceHeaderCorrectionPeriod | CORRECTION_PERIOD | — | ✅ |
| 20 | InvoiceHeaderCorrectionYear | CORRECTION_YEAR | — | ✅ |
| 21 | InvoiceHeaderCreatedBy | CREATED_BY | — | ✅ |
| 22 | InvoiceHeaderCreationDate | CREATION_DATE | — | ✅ |
| 23 | InvoiceHeaderDescription | DESCRIPTION | — | ✅ |
| 24 | InvoiceHeaderDocCategoryCode | DOC_CATEGORY_CODE | — | ✅ |
| 25 | InvoiceHeaderDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 26 | InvoiceHeaderDocSequenceValue | DOC_SEQUENCE_VALUE | — | ✅ |
| 27 | InvoiceHeaderEarliestSettlementDate | EARLIEST_SETTLEMENT_DATE | — | ✅ |
| 28 | InvoiceHeaderExchangeDate | EXCHANGE_DATE | — | ✅ |
| 29 | InvoiceHeaderExchangeRate | EXCHANGE_RATE | — | ✅ |
| 30 | InvoiceHeaderExcludeFreightFromDiscount | EXCLUDE_FREIGHT_FROM_DISCOUNT | — | ✅ |
| 31 | InvoiceHeaderExclusivePaymentFlag | EXCLUSIVE_PAYMENT_FLAG | — | ✅ |
| 32 | InvoiceHeaderFiscalDocAccessKey | FISCAL_DOC_ACCESS_KEY | — | — |
| 33 | InvoiceHeaderFundsStatus | FUNDS_STATUS | — | ✅ |
| 34 | InvoiceHeaderGlDate | GL_DATE | — | ✅ |
| 35 | InvoiceHeaderGoodsReceivedDate | GOODS_RECEIVED_DATE | — | ✅ |
| 36 | InvoiceHeaderIntercompanyFlag | INTERCOMPANY_FLAG | — | ✅ |
| 37 | InvoiceHeaderInvoiceAmount | INVOICE_AMOUNT | — | — |
| 38 | InvoiceHeaderInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 39 | InvoiceHeaderInvoiceDate | INVOICE_DATE | — | ✅ |
| 40 | InvoiceHeaderInvoiceId | INVOICE_ID | — | ✅ |
| 41 | InvoiceHeaderInvoiceNum | INVOICE_NUM | — | ✅ |
| 42 | InvoiceHeaderInvoiceReceivedDate | INVOICE_RECEIVED_DATE | — | ✅ |
| 43 | InvoiceHeaderInvoiceTypeLookupCode | INVOICE_TYPE_LOOKUP_CODE | — | ✅ |
| 44 | InvoiceHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 45 | InvoiceHeaderLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 46 | InvoiceHeaderLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 47 | InvoiceHeaderNetOfRetainageFlag | NET_OF_RETAINAGE_FLAG | — | ✅ |
| 48 | InvoiceHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 49 | InvoiceHeaderOrgId | ORG_ID | — | — |
| 50 | InvoiceHeaderPartyId | PARTY_ID | — | — |
| 51 | InvoiceHeaderPartySiteId | PARTY_SITE_ID | — | — |
| 52 | InvoiceHeaderPayGroupLookupCode | PAY_GROUP_LOOKUP_CODE | — | ✅ |
| 53 | InvoiceHeaderPaymentCrossRate | PAYMENT_CROSS_RATE | — | ✅ |
| 54 | InvoiceHeaderPaymentCrossRateDate | PAYMENT_CROSS_RATE_DATE | — | ✅ |
| 55 | InvoiceHeaderPaymentCrossRateType | PAYMENT_CROSS_RATE_TYPE | — | ✅ |
| 56 | InvoiceHeaderPaymentCurrencyCode | PAYMENT_CURRENCY_CODE | — | ✅ |
| 57 | InvoiceHeaderPaymentMethodCode | PAYMENT_METHOD_CODE | — | — |
| 58 | InvoiceHeaderPaymentMethodLookupCode | PAYMENT_METHOD_LOOKUP_CODE | — | — |
| 59 | InvoiceHeaderPaymentReasonComments | PAYMENT_REASON_COMMENTS | — | ✅ |
| 60 | InvoiceHeaderPaymentStatusFlag | PAYMENT_STATUS_FLAG | — | ✅ |
| 61 | InvoiceHeaderPortOfEntryCode | PORT_OF_ENTRY_CODE | — | ✅ |
| 62 | InvoiceHeaderPostingStatus | POSTING_STATUS | — | ✅ |
| 63 | InvoiceHeaderReleaseAmountNetOfTax | RELEASE_AMOUNT_NET_OF_TAX | — | — |
| 64 | InvoiceHeaderRoutingAttribute1 | ROUTING_ATTRIBUTE1 | — | ✅ |
| 65 | InvoiceHeaderRoutingAttribute2 | ROUTING_ATTRIBUTE2 | — | ✅ |
| 66 | InvoiceHeaderRoutingAttribute3 | ROUTING_ATTRIBUTE3 | — | ✅ |
| 67 | InvoiceHeaderRoutingAttribute4 | ROUTING_ATTRIBUTE4 | — | ✅ |
| 68 | InvoiceHeaderRoutingAttribute5 | ROUTING_ATTRIBUTE5 | — | — |
| 69 | InvoiceHeaderRoutingStatusLookupCode | ROUTING_STATUS_LOOKUP_CODE | — | ✅ |
| 70 | InvoiceHeaderSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 71 | InvoiceHeaderSettlementPriority | SETTLEMENT_PRIORITY | — | ✅ |
| 72 | InvoiceHeaderSource | SOURCE | — | ✅ |
| 73 | InvoiceHeaderSupplierTaxExchangeRate | SUPPLIER_TAX_EXCHANGE_RATE | — | ✅ |
| 74 | InvoiceHeaderSupplierTaxInvoiceDate | SUPPLIER_TAX_INVOICE_DATE | — | ✅ |
| 75 | InvoiceHeaderSupplierTaxInvoiceNumber | SUPPLIER_TAX_INVOICE_NUMBER | — | ✅ |
| 76 | InvoiceHeaderTaxInvoiceInternalSeq | TAX_INVOICE_INTERNAL_SEQ | — | ✅ |
| 77 | InvoiceHeaderTaxInvoiceRecordingDate | TAX_INVOICE_RECORDING_DATE | — | ✅ |
| 78 | InvoiceHeaderTaxationCountry | TAXATION_COUNTRY | — | ✅ |
| 79 | InvoiceHeaderTermsDate | TERMS_DATE | — | ✅ |
| 80 | InvoiceHeaderTermsId | TERMS_ID | — | — |
| 81 | InvoiceHeaderUniqueRemittanceIdentifier | UNIQUE_REMITTANCE_IDENTIFIER | — | ✅ |
| 82 | InvoiceHeaderUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 83 | InvoiceHeaderVendorId | VENDOR_ID | — | — |
| 84 | InvoiceHeaderVendorSiteId | VENDOR_SITE_ID | — | — |
| 85 | InvoiceHeaderVoucherNum | VOUCHER_NUM | — | ✅ |
| 86 | InvoiceHeaderWfapprovalStatus | WFAPPROVAL_STATUS | — | ✅ |
| 87 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 88 | RetainedInvoiceInvoiceId | INVOICE_ID | — | — |
| 89 | RetainedInvoiceInvoiceNum | INVOICE_NUM | — | ✅ |
| 90 | RetainedInvoiceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[ap_invoice_lines_all|AP_INVOICE_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AppliedInvoiceLineInvoiceId | INVOICE_ID | — | — |
| 2 | AppliedInvoiceLineLineNumber | LINE_NUMBER | — | — |
| 3 | AppliedInvoiceLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | InvoiceId | INVOICE_ID | 🔑 | ✅ |
| 5 | InvoiceLineAccountingDate | ACCOUNTING_DATE | — | ✅ |
| 6 | InvoiceLineAdjustmentReason | ADJUSTMENT_REASON | — | ✅ |
| 7 | InvoiceLineAmount | AMOUNT | — | ✅ |
| 8 | InvoiceLineAssessableValue | ASSESSABLE_VALUE | — | ✅ |
| 9 | InvoiceLineAssetBookTypeCode | ASSET_BOOK_TYPE_CODE | — | ✅ |
| 10 | InvoiceLineAssetsTrackingFlag | ASSETS_TRACKING_FLAG | — | ✅ |
| 11 | InvoiceLineBaseAmount | BASE_AMOUNT | — | ✅ |
| 12 | InvoiceLineBudgetDate | BUDGET_DATE | — | ✅ |
| 13 | InvoiceLineCancelledFlag | CANCELLED_FLAG | — | ✅ |
| 14 | InvoiceLineControlAmount | CONTROL_AMOUNT | — | ✅ |
| 15 | InvoiceLineCorrectedInvId | CORRECTED_INV_ID | — | — |
| 16 | InvoiceLineCorrectedLineNumber | CORRECTED_LINE_NUMBER | — | ✅ |
| 17 | InvoiceLineCreatedBy | CREATED_BY | — | ✅ |
| 18 | InvoiceLineCreationDate | CREATION_DATE | — | ✅ |
| 19 | InvoiceLineDefAcctgAclCcid | DEF_ACCTG_ACCRUAL_CCID | — | ✅ |
| 20 | InvoiceLineDefAcctgEndDate | DEF_ACCTG_END_DATE | — | ✅ |
| 21 | InvoiceLineDefAcctgNumberOfPeriods | DEF_ACCTG_NUMBER_OF_PERIODS | — | ✅ |
| 22 | InvoiceLineDefAcctgPeriodType | DEF_ACCTG_PERIOD_TYPE | — | ✅ |
| 23 | InvoiceLineDefAcctgStartDate | DEF_ACCTG_START_DATE | — | ✅ |
| 24 | InvoiceLineDefaultDistCcid | DEFAULT_DIST_CCID | — | ✅ |
| 25 | InvoiceLineDeferredAcctgFlag | DEFERRED_ACCTG_FLAG | — | ✅ |
| 26 | InvoiceLineDescription | DESCRIPTION | — | ✅ |
| 27 | InvoiceLineDiscardedFlag | DISCARDED_FLAG | — | ✅ |
| 28 | InvoiceLineExpenditureItemDate | EXPENDITURE_ITEM_DATE | — | ✅ |
| 29 | InvoiceLineFinalMatchFlag | FINAL_MATCH_FLAG | — | ✅ |
| 30 | InvoiceLineFundsStatus | FUNDS_STATUS | — | ✅ |
| 31 | InvoiceLineIncludedTaxAmount | INCLUDED_TAX_AMOUNT | — | ✅ |
| 32 | InvoiceLineIncomeTaxRegion | INCOME_TAX_REGION | — | ✅ |
| 33 | InvoiceLineInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 34 | InvoiceLineInvoiceIncludesPrepayFlag | INVOICE_INCLUDES_PREPAY_FLAG | — | ✅ |
| 35 | InvoiceLineItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 36 | InvoiceLineLCMEnabledLookupCode | LCM_ENABLED_FLAG | — | ✅ |
| 37 | InvoiceLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 38 | InvoiceLineLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 39 | InvoiceLineLineGroupNumber | LINE_GROUP_NUMBER | — | ✅ |
| 40 | InvoiceLineLineSource | LINE_SOURCE | — | — |
| 41 | InvoiceLineLineTypeLookupCode | LINE_TYPE_LOOKUP_CODE | — | ✅ |
| 42 | InvoiceLineManufacturer | MANUFACTURER | — | ✅ |
| 43 | InvoiceLineMatchType | MATCH_TYPE | — | ✅ |
| 44 | InvoiceLineModelNumber | MODEL_NUMBER | — | ✅ |
| 45 | InvoiceLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 46 | InvoiceLineOrgId | ORG_ID | — | ✅ |
| 47 | InvoiceLineOriginalAmount | ORIGINAL_AMOUNT | — | ✅ |
| 48 | InvoiceLineOriginalBaseAmount | ORIGINAL_BASE_AMOUNT | — | ✅ |
| 49 | InvoiceLineOriginalRoundingAmt | ORIGINAL_ROUNDING_AMT | — | ✅ |
| 50 | InvoiceLinePaCcArInvoiceLineNum | PA_CC_AR_INVOICE_LINE_NUM | — | ✅ |
| 51 | InvoiceLinePaCcProcessedCode | PA_CC_PROCESSED_CODE | — | ✅ |
| 52 | InvoiceLinePeriodName | PERIOD_NAME | — | ✅ |
| 53 | InvoiceLinePjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | ✅ |
| 54 | InvoiceLinePrepayInvoiceId | PREPAY_INVOICE_ID | — | — |
| 55 | InvoiceLinePrepayLineNumber | PREPAY_LINE_NUMBER | — | ✅ |
| 56 | InvoiceLineProductCategory | PRODUCT_CATEGORY | — | ✅ |
| 57 | InvoiceLineProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | ✅ |
| 58 | InvoiceLineProductType | PRODUCT_TYPE | — | ✅ |
| 59 | InvoiceLineProrateAcrossAllItems | PRORATE_ACROSS_ALL_ITEMS | — | ✅ |
| 60 | InvoiceLineQuantityInvoiced | QUANTITY_INVOICED | — | ✅ |
| 61 | InvoiceLineReferenceKey1 | REFERENCE_KEY1 | — | — |
| 62 | InvoiceLineRetainedAmount | RETAINED_AMOUNT | — | ✅ |
| 63 | InvoiceLineRetainedAmountRemaining | RETAINED_AMOUNT_REMAINING | — | ✅ |
| 64 | InvoiceLineRetainedInvoiceId | RETAINED_INVOICE_ID | — | — |
| 65 | InvoiceLineRetainedLineNumber | RETAINED_LINE_NUMBER | — | ✅ |
| 66 | InvoiceLineRoundingAmt | ROUNDING_AMT | — | ✅ |
| 67 | InvoiceLineSerialNumber | SERIAL_NUMBER | — | ✅ |
| 68 | InvoiceLineShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 69 | InvoiceLineTax | TAX | — | ✅ |
| 70 | InvoiceLineTaxAlreadyCalculatedFlag | TAX_ALREADY_CALCULATED_FLAG | — | ✅ |
| 71 | InvoiceLineTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | ✅ |
| 72 | InvoiceLineTaxJurisdictionCode | TAX_JURISDICTION_CODE | — | ✅ |
| 73 | InvoiceLineTaxRate | TAX_RATE | — | ✅ |
| 74 | InvoiceLineTaxRateCode | TAX_RATE_CODE | — | ✅ |
| 75 | InvoiceLineTaxRegimeCode | TAX_REGIME_CODE | — | ✅ |
| 76 | InvoiceLineTaxStatusCode | TAX_STATUS_CODE | — | — |
| 77 | InvoiceLineTotalNrecTaxAmount | TOTAL_NREC_TAX_AMOUNT | — | ✅ |
| 78 | InvoiceLineTotalNrecTaxAmtFunclCurr | TOTAL_NREC_TAX_AMT_FUNCL_CURR | — | ✅ |
| 79 | InvoiceLineTotalRecTaxAmount | TOTAL_REC_TAX_AMOUNT | — | ✅ |
| 80 | InvoiceLineTotalRecTaxAmtFunclCurr | TOTAL_REC_TAX_AMT_FUNCL_CURR | — | ✅ |
| 81 | InvoiceLineTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 82 | InvoiceLineType1099 | TYPE_1099 | — | ✅ |
| 83 | InvoiceLineUnitMeasLookupCode | UNIT_MEAS_LOOKUP_CODE | — | ✅ |
| 84 | InvoiceLineUnitPrice | UNIT_PRICE | — | ✅ |
| 85 | InvoiceLineUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | ✅ |
| 86 | InvoiceLineWarrantyNumber | WARRANTY_NUMBER | — | ✅ |
| 87 | InvoiceLineWfapprovalStatus | WFAPPROVAL_STATUS | — | ✅ |
| 88 | LineNumber | LINE_NUMBER | 🔑 | ✅ |

### [[ap_inv_aprvl_hist_all|AP_INV_APRVL_HIST_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApInvLineAprvlHistAllApproverId | APPROVER_ID | — | — |
| 2 | InvAprvlHistAllAmountApproved | AMOUNT_APPROVED | — | — |
| 3 | InvAprvlHistAllApprovalHistoryId | APPROVAL_HISTORY_ID | — | — |
| 4 | InvAprvlHistAllApproverId | APPROVER_ID | — | — |
| 5 | InvAprvlHistAllCreationDate | CREATION_DATE | — | — |
| 6 | InvAprvlHistAllHistoryType | HISTORY_TYPE | — | — |
| 7 | InvAprvlHistAllResponse | RESPONSE | — | — |
| 8 | InvLineAprvlHistAllAmountApproved | AMOUNT_APPROVED | — | — |
| 9 | InvLineAprvlHistAllCreationDate | CREATION_DATE | — | — |
| 10 | InvLineAprvlHistAllHistoryType | HISTORY_TYPE | — | — |
| 11 | InvLineAprvlHistAllResponse | RESPONSE | — | — |
| 12 | InvLineAprvlHistId | APPROVAL_HISTORY_ID | — | — |

### [[egp_categories_vl|EGP_CATEGORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryCategoryId | CATEGORY_ID | — | — |
| 2 | CategoryCategoryName | CATEGORY_NAME | — | ✅ |

### [[fa_book_controls|FA_BOOK_CONTROLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BookControlInvLineBookTypeCode | BOOK_TYPE_CODE | — | — |
| 2 | BookControlInvLineBookTypeName | BOOK_TYPE_NAME | — | ✅ |

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

### [[hr_all_organization_units_f_vl|HR_ALL_ORGANIZATION_UNITS_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjcBUEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PjcBUEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | PjcBUName | NAME | — | ✅ |
| 4 | PjcBUOrganizationId | ORGANIZATION_ID | — | — |

### [[hr_locations|HR_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HrLocationsAddressLine1 | ADDRESS_LINE_1 | — | — |
| 2 | HrLocationsAddressLine2 | ADDRESS_LINE_2 | — | — |
| 3 | HrLocationsAddressLine3 | ADDRESS_LINE_3 | — | — |
| 4 | HrLocationsAddressLine4 | ADDRESS_LINE_4 | — | — |
| 5 | HrLocationsGeometry | GEOMETRY | — | — |
| 6 | HrLocationsLocationId | LOCATION_ID | — | — |
| 7 | HrLocationsPostalCode | POSTAL_CODE | — | — |
| 8 | HrLocationsRegion2 | REGION_2 | — | — |
| 9 | HrLocationsTownOrCity | TOWN_OR_CITY | — | — |

### [[hz_locations|HZ_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FinalDischargeLocationAddress1 | ADDRESS1 | — | — |
| 2 | FinalDischargeLocationAddress2 | ADDRESS2 | — | — |
| 3 | FinalDischargeLocationAddress3 | ADDRESS3 | — | — |
| 4 | FinalDischargeLocationAddress4 | ADDRESS4 | — | — |
| 5 | FinalDischargeLocationCity | CITY | — | — |
| 6 | FinalDischargeLocationLocationId1 | LOCATION_ID | — | — |
| 7 | FinalDischargeLocationPostalCode | POSTAL_CODE | — | — |
| 8 | FinalDischargeLocationState | STATE | — | — |
| 9 | ShipFromLocationAddress1 | ADDRESS1 | — | — |
| 10 | ShipFromLocationAddress2 | ADDRESS2 | — | — |
| 11 | ShipFromLocationAddress3 | ADDRESS3 | — | — |
| 12 | ShipFromLocationAddress4 | ADDRESS4 | — | — |
| 13 | ShipFromLocationCity | CITY | — | — |
| 14 | ShipFromLocationLocationId | LOCATION_ID | — | — |
| 15 | ShipFromLocationPostalCode | POSTAL_CODE | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyPartyId | PARTY_ID | — | — |
| 2 | PartyPartyName | PARTY_NAME | — | ✅ |

### [[hz_party_sites|HZ_PARTY_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwtPartySitePartySiteId | PARTY_SITE_ID | — | — |
| 2 | AwtPartySitePartySiteName | PARTY_SITE_NAME | — | ✅ |
| 3 | PartySitePartySiteId | PARTY_SITE_ID | — | — |
| 4 | PartySitePartySiteName | PARTY_SITE_NAME | — | ✅ |

### [[inv_cons_advice_txns_v|INV_CONS_ADVICE_TXNS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConsumptionAdviceConsumptionLineId | CONSUMPTION_LINE_ID | — | — |
| 2 | ConsumptionAdviceConsumptionLineNumber | CONSUMPTION_LINE_NUMBER | — | ✅ |
| 3 | ConsumptionAdviceConsumptionNumber | CONSUMPTION_NUMBER | — | ✅ |

### [[inv_units_of_measure_b|INV_UNITS_OF_MEASURE_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UomUnitOfMeasureId | UNIT_OF_MEASURE_ID | — | — |
| 2 | UomUomCode | UOM_CODE | — | ✅ |

### [[inv_units_of_measure_tl|INV_UNITS_OF_MEASURE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UomDescription | DESCRIPTION | — | ✅ |
| 2 | UomTLLanguage | LANGUAGE | — | — |
| 3 | UomTLUnitOfMeasureId | UNIT_OF_MEASURE_ID | — | — |
| 4 | UomUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |

### [[per_location_details_f_vl|PER_LOCATION_DETAILS_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocDetailsEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | LocDetailsEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | LocDetailsLocationDetailsId | LOCATION_DETAILS_ID | — | — |
| 4 | LocDetailsLocationName | LOCATION_NAME | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AprvlPersonNameDisplayName1 | DISPLAY_NAME | — | — |
| 2 | AprvlPersonNameEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | AprvlPersonNameEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | AprvlPersonNamePersonNameId | PERSON_NAME_ID | — | — |
| 5 | InvLineAprvlPersonNameDisplayName | DISPLAY_NAME | — | — |
| 6 | InvLineAprvlPersonNameEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | InvLineAprvlPersonNameEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 8 | InvLineAprvlPersonNamePersonNameId | PERSON_NAME_ID | — | — |
| 9 | InvLineRequesterPersonNameDisplayName | DISPLAY_NAME | — | ✅ |
| 10 | InvPersonCreateDisplayName | DISPLAY_NAME | — | ✅ |
| 11 | InvPersonCreateEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 12 | InvPersonCreateEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 13 | InvPersonCreatePersonNameId | PERSON_NAME_ID | — | — |
| 14 | InvPersonUpdateDisplayName | DISPLAY_NAME | — | ✅ |
| 15 | InvPersonUpdateEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 16 | InvPersonUpdateEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 17 | InvPersonUpdatePersonNameId | PERSON_NAME_ID | — | — |
| 18 | PersonCancelledByDisplayName | DISPLAY_NAME | — | ✅ |
| 19 | PersonCancelledByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 20 | PersonCancelledByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 21 | PersonCancelledByPersonNameId | PERSON_NAME_ID | — | — |
| 22 | PersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 23 | PersonCreatedByEffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 24 | PersonCreatedByEffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 25 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 26 | PersonNameDisplayName | DISPLAY_NAME | — | ✅ |
| 27 | PersonNameEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 28 | PersonNameEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 29 | PersonNameLineEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 30 | PersonNameLineEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 31 | PersonNameLinePersonNameId | PERSON_NAME_ID | — | — |
| 32 | PersonNamePersonNameId | PERSON_NAME_ID | — | — |
| 33 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 34 | PersonUpdatedByEffectiveEndDate2 | EFFECTIVE_END_DATE | — | — |
| 35 | PersonUpdatedByEffectiveStartDate2 | EFFECTIVE_START_DATE | — | — |
| 36 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |
| 37 | PoHeaderInvLinePersonUpdatedByDisplayName | DISPLAY_NAME | — | — |
| 38 | PoHeaderInvLinePersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 39 | PoHeaderInvLinePersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 40 | PoHeaderInvLinePersonUpdatedByPersonId | PERSON_ID | — | — |
| 41 | PoHeaderInvLinePersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvUpdateObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | InvUpdateUserId | USER_ID | — | — |
| 3 | PoHeaderInvLineUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | PoHeaderInvLineUpdatedByPersonId | PERSON_ID | — | — |
| 5 | PoHeaderInvLineUpdatedByUserGuid | USER_GUID | — | — |
| 6 | PoHeaderInvLineUpdatedByUserId | USER_ID | — | — |
| 7 | PoHeaderInvLineUpdatedByUsername | USERNAME | — | — |

### [[pjf_exp_types_tl|PJF_EXP_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpTypeExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 2 | ExpTypeExpenditureTypeName | EXPENDITURE_TYPE_NAME | — | ✅ |
| 3 | ExpTypeLanguage | LANGUAGE | — | — |

### [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectProjectId | PROJECT_ID | — | — |
| 2 | ProjectSegment1 | SEGMENT1 | — | ✅ |

### [[pjf_projects_all_tl|PJF_PROJECTS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectName | NAME | — | ✅ |
| 2 | ProjectTLLAnguage | LANGUAGE | — | — |
| 3 | ProjectTLProjectId | PROJECT_ID | — | — |

### [[pjf_proj_elements_b|PJF_PROJ_ELEMENTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskStructureElementNumber | ELEMENT_NUMBER | — | ✅ |
| 2 | TaskStructureProjElementId | PROJ_ELEMENT_ID | — | — |

### [[pjf_proj_elements_tl|PJF_PROJ_ELEMENTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskStructureName | NAME | — | ✅ |
| 2 | TaskStructureTLLanguage | LANGUAGE | — | — |
| 3 | TaskStructureTLProjElementId | PROJ_ELEMENT_ID | — | — |

### [[poz_suppliers_v|POZ_SUPPLIERS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwtSupplierVendorId | VENDOR_ID | — | — |
| 2 | AwtSupplierVendorName | VENDOR_NAME | — | ✅ |

### [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwtSupplierSiteVendorSiteCode | VENDOR_SITE_CODE | — | ✅ |
| 2 | AwtSupplierSiteVendorSiteId | VENDOR_SITE_ID | — | — |

### [[po_distributions_all|PO_DISTRIBUTIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PoDistributionDistributionNum | DISTRIBUTION_NUM | — | ✅ |
| 2 | PoDistributionPoDistributionId | PO_DISTRIBUTION_ID | — | — |

### [[po_headers_all|PO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PoHeaderCreationDate | CREATION_DATE | — | ✅ |
| 2 | PoHeaderPoHeaderId | PO_HEADER_ID | — | — |
| 3 | PoHeaderSegment1 | SEGMENT1 | — | ✅ |
| 4 | PurchaseOrderClosedDate | CLOSED_DATE | — | ✅ |
| 5 | PurchaseOrderDocumentStatus | DOCUMENT_STATUS | — | ✅ |
| 6 | PurchaseOrderPoHeaderId | PO_HEADER_ID | — | — |
| 7 | PurchaseOrderSegment1 | SEGMENT1 | — | ✅ |

### [[po_lines_all|PO_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PoLineLineNum | LINE_NUM | — | ✅ |
| 2 | PoLinePoLineId | PO_LINE_ID | — | — |

### [[po_line_locations_all|PO_LINE_LOCATIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PoLineLocLineLocationId | LINE_LOCATION_ID | — | — |
| 2 | PoLineLocShipmentNum | SHIPMENT_NUM | — | ✅ |

### [[po_system_parameters_all|PO_SYSTEM_PARAMETERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchasingSystemParameterInventoryOrgId | INVENTORY_ORGANIZATION_ID | — | — |
| 2 | PurchasingSystemParameterPrcBuId | PRC_BU_ID | — | — |

### [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrxHeaderCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 2 | TrxHeaderTrxNumber | TRX_NUMBER | — | ✅ |

### [[rcv_shipment_headers|RCV_SHIPMENT_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RcvShipHeaderInvLineReceiptNum | RECEIPT_NUM | — | ✅ |
| 2 | RcvShipHeaderInvLineShipmentHeaderId | SHIPMENT_HEADER_ID | — | — |

### [[rcv_shipment_lines|RCV_SHIPMENT_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RcvShipLineLineNum | LINE_NUM | — | ✅ |
| 2 | RcvShipLineShipmentLineId | SHIPMENT_LINE_ID | — | — |

### [[rcv_transactions|RCV_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RcvTransInvLineComments | COMMENTS | — | ✅ |
| 2 | RcvTransInvLineTransactionDate | TRANSACTION_DATE | — | ✅ |
| 3 | RcvTransInvLineTransactionId | TRANSACTION_ID | — | — |
| 4 | RcvTransInvLineTransactionType | TRANSACTION_TYPE | — | ✅ |

### [[zx_condition_groups_b|ZX_CONDITION_GROUPS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwtTaxGroupLineConditionGroupCode | CONDITION_GROUP_CODE | — | — |
| 2 | AwtTaxGroupLineConditionGroupId | CONDITION_GROUP_ID | — | — |

### [[zx_condition_groups_tl|ZX_CONDITION_GROUPS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwtTaxGroupLineConditionGroupName | CONDITION_GROUP_NAME | — | ✅ |
| 2 | AwtTaxGroupLineTLConditionGroupId | CONDITION_GROUP_ID | — | — |
| 3 | AwtTaxGroupLineTLLanguage | LANGUAGE | — | — |

### [[zx_fc_codes_vl|ZX_FC_CODES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClassificationId | CLASSIFICATION_ID | — | — |
| 2 | InvoiceLinePrimaryIntendedUse | CLASSIFICATION_CODE | — | ✅ |

### [[zx_jurisdictions_b|ZX_JURISDICTIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxJurisTaxJurisdictionCode | TAX_JURISDICTION_CODE | — | — |
| 2 | TaxJurisTaxJurisdictionId | TAX_JURISDICTION_ID | — | — |

### [[zx_jurisdictions_tl|ZX_JURISDICTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxJurisTLLanguage | LANGUAGE | — | — |
| 2 | TaxJurisTLTaxJurisdictionId | TAX_JURISDICTION_ID | — | — |
| 3 | TaxJurisTaxJurisdictionName | TAX_JURISDICTION_NAME | — | ✅ |

### [[zx_rates_vl|ZX_RATES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxRateLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | TaxRateLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 3 | TaxRateTaxRateId | TAX_RATE_ID | — | — |
| 4 | TaxRateTaxRateName | TAX_RATE_NAME | — | ✅ |
| 5 | WhtRatesDescription | DESCRIPTION | — | ✅ |
| 6 | WhtRatesTaxRateCode | TAX_RATE_CODE | — | ✅ |
| 7 | WhtRatesTaxRateId | TAX_RATE_ID | — | — |
| 8 | WhtRatesTaxRateName | TAX_RATE_NAME | — | ✅ |

### [[zx_regimes_b|ZX_REGIMES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxRegimeTaxRegimeCode | TAX_REGIME_CODE | — | — |
| 2 | TaxRegimeTaxRegimeId | TAX_REGIME_ID | — | — |

### [[zx_regimes_tl|ZX_REGIMES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxRegimeTLLanguage | LANGUAGE | — | — |
| 2 | TaxRegimeTLTaxRegimeId | TAX_REGIME_ID | — | — |
| 3 | TaxRegimeTaxRegimeName | TAX_REGIME_NAME | — | ✅ |

### [[zx_registrations|ZX_REGISTRATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FirstPartyTaxRegistrationRegistrationId | REGISTRATION_ID | — | — |
| 2 | FirstPartyTaxRegistrationRegistrationNumber | REGISTRATION_NUMBER | — | ✅ |
| 3 | ThirdPartyTaxRegistrationRegistrationId1 | REGISTRATION_ID | — | — |
| 4 | ThirdPartyTaxRegistrationRegistrationNumber1 | REGISTRATION_NUMBER | — | ✅ |

### [[zx_status_b|ZX_STATUS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxStatusTaxStatusId | TAX_STATUS_ID | — | — |

### [[zx_status_tl|ZX_STATUS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxStatusLanguage | LANGUAGE | — | — |
| 2 | TaxStatusTLTaxStatusId | TAX_STATUS_ID | — | — |
| 3 | TaxStatusTaxStatusName | TAX_STATUS_NAME | — | — |

### [[zx_taxes_b|ZX_TAXES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WhtTaxesTaxId | TAX_ID | — | — |

### [[zx_taxes_tl|ZX_TAXES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WhtTaxesTLLanguage | LANGUAGE | — | — |
| 2 | WhtTaxesTLTaxId | TAX_ID | — | — |
| 3 | WhtTaxesTaxFullName | TAX_FULL_NAME | — | ✅ |

### [[zx_tax_settlement_auths_f|ZX_TAX_SETTLEMENT_AUTHS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxSettlementAuthorityEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | TaxSettlementAuthorityEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | TaxSettlementAuthorityTaxSettlementAuthId | TAX_SETTLEMENT_AUTH_ID | — | — |

### [[zx_wht_lines_summary|ZX_WHT_LINES_SUMMARY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WhtSummaryTaxLineExemptCertificateNumber | EXEMPT_CERTIFICATE_NUMBER | — | ✅ |
| 2 | WhtSummaryTaxLineSummaryTaxLineId | SUMMARY_TAX_LINE_ID | — | — |
| 3 | WhtSummaryTaxLineTaxRate | TAX_RATE | — | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
