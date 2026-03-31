---
id: DOC-OTHER-PVO-AssetInvoicePVO
doc_type: system-doc
title: "AssetInvoicePVO — PVO Cross-Module"
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
  - AssetInvoicePVO
  - assetinvoicepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssetInvoicePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Asset Invoice. Acessa as tabelas: AP_INVOICE_DISTRIBUTIONS_ALL, AP_INVOICE_PAYMENTS_ALL, FA_ASSET_INVOICES (+12).

**Caminho:** `FscmTopModelAM.FinFaSharedUtilAM.AssetInvoicePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 637 | 15 | 1 | 45 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[ap_invoice_distributions_all|AP_INVOICE_DISTRIBUTIONS_ALL]] — 176 atributos (2 BICC)
- [[ap_invoice_payments_all|AP_INVOICE_PAYMENTS_ALL]] — 60 atributos (1 BICC)
- [[fa_asset_invoices|FA_ASSET_INVOICES]] — 55 atributos (1 PKs, 25 BICC)
- [[fa_book_controls|FA_BOOK_CONTROLS]] — 5 atributos
- [[fa_invoice_transactions|FA_INVOICE_TRANSACTIONS]] — 16 atributos
- [[hr_all_organization_units_f_vl|HR_ALL_ORGANIZATION_UNITS_F_VL]] — 15 atributos (3 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (2 BICC)
- [[per_users|PER_USERS]] — 10 atributos
- [[pjc_prj_asset_lns_all|PJC_PRJ_ASSET_LNS_ALL]] — 46 atributos (2 BICC)
- [[pjf_exp_types_tl|PJF_EXP_TYPES_TL]] — 10 atributos (1 BICC)
- [[pjf_projects_all_vl|PJF_PROJECTS_ALL_VL]] — 5 atributos (3 BICC)
- [[pjf_proj_elements_vl|PJF_PROJ_ELEMENTS_VL]] — 75 atributos (2 BICC)
- [[pjf_txn_doc_entry_vl|PJF_TXN_DOC_ENTRY_VL]] — 5 atributos (1 BICC)
- [[poz_suppliers_v|POZ_SUPPLIERS_V]] — 31 atributos (1 BICC)
- [[po_distributions_all|PO_DISTRIBUTIONS_ALL]] — 118 atributos (2 BICC)

---

## ⚙️ Atributos

### [[ap_invoice_distributions_all|AP_INVOICE_DISTRIBUTIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvDistAccountingDate | ACCOUNTING_DATE | — | — |
| 2 | InvDistAccountingEventId | ACCOUNTING_EVENT_ID | — | — |
| 3 | InvDistAdjustmentReason | ADJUSTMENT_REASON | — | — |
| 4 | InvDistAmount | AMOUNT | — | — |
| 5 | InvDistAmountAtPrepayPayXrate | AMOUNT_AT_PREPAY_PAY_XRATE | — | — |
| 6 | InvDistAmountAtPrepayXrate | AMOUNT_AT_PREPAY_XRATE | — | — |
| 7 | InvDistAmountVariance | AMOUNT_VARIANCE | — | — |
| 8 | InvDistAssetBookTypeCode | ASSET_BOOK_TYPE_CODE | — | — |
| 9 | InvDistAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 10 | InvDistAssetsAdditionFlag | ASSETS_ADDITION_FLAG | — | — |
| 11 | InvDistAssetsTrackingFlag | ASSETS_TRACKING_FLAG | — | — |
| 12 | InvDistAwardId | AWARD_ID | — | — |
| 13 | InvDistAwtFlag | AWT_FLAG | — | — |
| 14 | InvDistAwtGrossAmount | AWT_GROSS_AMOUNT | — | — |
| 15 | InvDistAwtGroupId | AWT_GROUP_ID | — | — |
| 16 | InvDistAwtInvoiceId | AWT_INVOICE_ID | — | — |
| 17 | InvDistAwtInvoicePaymentId | AWT_INVOICE_PAYMENT_ID | — | — |
| 18 | InvDistAwtOriginGroupId | AWT_ORIGIN_GROUP_ID | — | — |
| 19 | InvDistAwtRelatedId | AWT_RELATED_ID | — | — |
| 20 | InvDistAwtTaxRateId | AWT_TAX_RATE_ID | — | — |
| 21 | InvDistBaseAmount | BASE_AMOUNT | — | — |
| 22 | InvDistBaseAmountVariance | BASE_AMOUNT_VARIANCE | — | — |
| 23 | InvDistBaseQuantityVariance | BASE_QUANTITY_VARIANCE | — | — |
| 24 | InvDistBatchId | BATCH_ID | — | — |
| 25 | InvDistBcEventId | BC_EVENT_ID | — | — |
| 26 | InvDistCancellationFlag | CANCELLATION_FLAG | — | — |
| 27 | InvDistCashBasisFinalAppRounding | CASH_BASIS_FINAL_APP_ROUNDING | — | — |
| 28 | InvDistCcReversalFlag | CC_REVERSAL_FLAG | — | — |
| 29 | InvDistChargeApplicableToDistId | CHARGE_APPLICABLE_TO_DIST_ID | — | — |
| 30 | InvDistCompanyPrepaidInvoiceId | COMPANY_PREPAID_INVOICE_ID | — | — |
| 31 | InvDistCorrectedInvoiceDistId | CORRECTED_INVOICE_DIST_ID | — | — |
| 32 | InvDistCorrectedQuantity | CORRECTED_QUANTITY | — | — |
| 33 | InvDistCountryOfSupply | COUNTRY_OF_SUPPLY | — | — |
| 34 | InvDistCreatedBy | CREATED_BY | — | — |
| 35 | InvDistCreationDate | CREATION_DATE | — | — |
| 36 | InvDistCreditCardTrxId | CREDIT_CARD_TRX_ID | — | — |
| 37 | InvDistDailyAmount | DAILY_AMOUNT | — | — |
| 38 | InvDistDescription | DESCRIPTION | — | — |
| 39 | InvDistDetailTaxDistId | DETAIL_TAX_DIST_ID | — | — |
| 40 | InvDistDistCodeCombinationId | DIST_CODE_COMBINATION_ID | — | — |
| 41 | InvDistDistMatchType | DIST_MATCH_TYPE | — | — |
| 42 | InvDistDistributionClass | DISTRIBUTION_CLASS | — | — |
| 43 | InvDistDistributionLineNumber | DISTRIBUTION_LINE_NUMBER | — | ✅ |
| 44 | InvDistEncumberedFlag | ENCUMBERED_FLAG | — | — |
| 45 | InvDistEndExpenseDate | END_EXPENSE_DATE | — | — |
| 46 | InvDistExchangeDate | EXCHANGE_DATE | — | — |
| 47 | InvDistExchangeRate | EXCHANGE_RATE | — | — |
| 48 | InvDistExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 49 | InvDistExpenditureItemDate | EXPENDITURE_ITEM_DATE | — | — |
| 50 | InvDistExpenditureOrganizationId | EXPENDITURE_ORGANIZATION_ID | — | — |
| 51 | InvDistExpenditureType | EXPENDITURE_TYPE | — | — |
| 52 | InvDistExpenseGroup | EXPENSE_GROUP | — | — |
| 53 | InvDistExtraPoErv | EXTRA_PO_ERV | — | — |
| 54 | InvDistFinalApplicationRounding | FINAL_APPLICATION_ROUNDING | — | — |
| 55 | InvDistFinalMatchFlag | FINAL_MATCH_FLAG | — | — |
| 56 | InvDistFinalPaymentRounding | FINAL_PAYMENT_ROUNDING | — | — |
| 57 | InvDistFinalReleaseRounding | FINAL_RELEASE_ROUNDING | — | — |
| 58 | InvDistFullyPaidAcctdFlag | FULLY_PAID_ACCTD_FLAG | — | — |
| 59 | InvDistGmsBurdenableRawCost | GMS_BURDENABLE_RAW_COST | — | — |
| 60 | InvDistHistoricalFlag | HISTORICAL_FLAG | — | — |
| 61 | InvDistIncomeTaxRegion | INCOME_TAX_REGION | — | — |
| 62 | InvDistIntendedUse | INTENDED_USE | — | — |
| 63 | InvDistInventoryTransferStatus | INVENTORY_TRANSFER_STATUS | — | — |
| 64 | InvDistInvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | — |
| 65 | InvDistInvoiceId | INVOICE_ID | — | — |
| 66 | InvDistInvoiceIncludesPrepayFlag | INVOICE_INCLUDES_PREPAY_FLAG | — | — |
| 67 | InvDistInvoiceLineNumber | INVOICE_LINE_NUMBER | — | — |
| 68 | InvDistJustification | JUSTIFICATION | — | — |
| 69 | InvDistLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 70 | InvDistLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 71 | InvDistLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 72 | InvDistLineTypeLookupCode | LINE_TYPE_LOOKUP_CODE | — | — |
| 73 | InvDistMatchStatusFlag | MATCH_STATUS_FLAG | — | — |
| 74 | InvDistMatchedUomLookupCode | MATCHED_UOM_LOOKUP_CODE | — | — |
| 75 | InvDistMerchantDocumentNumber | MERCHANT_DOCUMENT_NUMBER | — | — |
| 76 | InvDistMerchantName | MERCHANT_NAME | — | — |
| 77 | InvDistMerchantReference | MERCHANT_REFERENCE | — | — |
| 78 | InvDistMerchantTaxRegNumber | MERCHANT_TAX_REG_NUMBER | — | — |
| 79 | InvDistMerchantTaxpayerId | MERCHANT_TAXPAYER_ID | — | — |
| 80 | InvDistObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 81 | InvDistOldDistLineNumber | OLD_DIST_LINE_NUMBER | — | — |
| 82 | InvDistOldDistributionId | OLD_DISTRIBUTION_ID | — | — |
| 83 | InvDistOrgId | ORG_ID | — | — |
| 84 | InvDistPJC_BILLABLE_FLAG | PJC_BILLABLE_FLAG | — | — |
| 85 | InvDistPJC_CAPITALIZABLE_FLAG | PJC_CAPITALIZABLE_FLAG | — | — |
| 86 | InvDistPJC_CONTEXT_CATEGORY | PJC_CONTEXT_CATEGORY | — | — |
| 87 | InvDistPJC_CONTRACT_ID | PJC_CONTRACT_ID | — | — |
| 88 | InvDistPJC_CONTRACT_LINE_ID | PJC_CONTRACT_LINE_ID | — | — |
| 89 | InvDistPJC_EXPENDITURE_ITEM_DATE | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 90 | InvDistPJC_EXPENDITURE_TYPE_ID | PJC_EXPENDITURE_TYPE_ID | — | — |
| 91 | InvDistPJC_FUNDING_ALLOCATION_ID | PJC_FUNDING_ALLOCATION_ID | — | — |
| 92 | InvDistPJC_ORGANIZATION_ID | PJC_ORGANIZATION_ID | — | — |
| 93 | InvDistPJC_PROJECT_ID | PJC_PROJECT_ID | — | — |
| 94 | InvDistPJC_RESERVED_ATTRIBUTE1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 95 | InvDistPJC_RESERVED_ATTRIBUTE10 | PJC_RESERVED_ATTRIBUTE10 | — | — |
| 96 | InvDistPJC_RESERVED_ATTRIBUTE2 | PJC_RESERVED_ATTRIBUTE2 | — | — |
| 97 | InvDistPJC_RESERVED_ATTRIBUTE3 | PJC_RESERVED_ATTRIBUTE3 | — | — |
| 98 | InvDistPJC_RESERVED_ATTRIBUTE4 | PJC_RESERVED_ATTRIBUTE4 | — | — |
| 99 | InvDistPJC_RESERVED_ATTRIBUTE5 | PJC_RESERVED_ATTRIBUTE5 | — | — |
| 100 | InvDistPJC_RESERVED_ATTRIBUTE6 | PJC_RESERVED_ATTRIBUTE6 | — | — |
| 101 | InvDistPJC_RESERVED_ATTRIBUTE7 | PJC_RESERVED_ATTRIBUTE7 | — | — |
| 102 | InvDistPJC_RESERVED_ATTRIBUTE8 | PJC_RESERVED_ATTRIBUTE8 | — | — |
| 103 | InvDistPJC_RESERVED_ATTRIBUTE9 | PJC_RESERVED_ATTRIBUTE9 | — | — |
| 104 | InvDistPJC_TASK_ID | PJC_TASK_ID | — | — |
| 105 | InvDistPJC_USER_DEF_ATTRIBUTE1 | PJC_USER_DEF_ATTRIBUTE1 | — | — |
| 106 | InvDistPJC_USER_DEF_ATTRIBUTE10 | PJC_USER_DEF_ATTRIBUTE10 | — | — |
| 107 | InvDistPJC_USER_DEF_ATTRIBUTE2 | PJC_USER_DEF_ATTRIBUTE2 | — | — |
| 108 | InvDistPJC_USER_DEF_ATTRIBUTE3 | PJC_USER_DEF_ATTRIBUTE3 | — | — |
| 109 | InvDistPJC_USER_DEF_ATTRIBUTE4 | PJC_USER_DEF_ATTRIBUTE4 | — | — |
| 110 | InvDistPJC_USER_DEF_ATTRIBUTE5 | PJC_USER_DEF_ATTRIBUTE5 | — | — |
| 111 | InvDistPJC_USER_DEF_ATTRIBUTE6 | PJC_USER_DEF_ATTRIBUTE6 | — | — |
| 112 | InvDistPJC_USER_DEF_ATTRIBUTE7 | PJC_USER_DEF_ATTRIBUTE7 | — | — |
| 113 | InvDistPJC_USER_DEF_ATTRIBUTE8 | PJC_USER_DEF_ATTRIBUTE8 | — | — |
| 114 | InvDistPJC_USER_DEF_ATTRIBUTE9 | PJC_USER_DEF_ATTRIBUTE9 | — | — |
| 115 | InvDistPJC_WORK_TYPE_ID | PJC_WORK_TYPE_ID | — | — |
| 116 | InvDistPaAdditionFlag | PA_ADDITION_FLAG | — | — |
| 117 | InvDistPaCmtXfaceFlag | PA_CMT_XFACE_FLAG | — | — |
| 118 | InvDistPaQuantity | PA_QUANTITY | — | — |
| 119 | InvDistParentInvoiceId | PARENT_INVOICE_ID | — | — |
| 120 | InvDistParentReversalId | PARENT_REVERSAL_ID | — | — |
| 121 | InvDistPeriodName | PERIOD_NAME | — | — |
| 122 | InvDistPoDistributionId | PO_DISTRIBUTION_ID | — | — |
| 123 | InvDistPostedFlag | POSTED_FLAG | — | — |
| 124 | InvDistPrepayAmountRemaining | PREPAY_AMOUNT_REMAINING | — | — |
| 125 | InvDistPrepayDistributionId | PREPAY_DISTRIBUTION_ID | — | — |
| 126 | InvDistPrepayTaxDiffAmount | PREPAY_TAX_DIFF_AMOUNT | — | — |
| 127 | InvDistProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 128 | InvDistProgramId | PROGRAM_ID | — | — |
| 129 | InvDistProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 130 | InvDistProjectId | PROJECT_ID | — | — |
| 131 | InvDistQuantityInvoiced | QUANTITY_INVOICED | — | — |
| 132 | InvDistQuantityVariance | QUANTITY_VARIANCE | — | — |
| 133 | InvDistRcvChargeAdditionFlag | RCV_CHARGE_ADDITION_FLAG | — | — |
| 134 | InvDistRcvTransactionId | RCV_TRANSACTION_ID | — | — |
| 135 | InvDistRecNrecRate | REC_NREC_RATE | — | — |
| 136 | InvDistReceiptConversionRate | RECEIPT_CONVERSION_RATE | — | — |
| 137 | InvDistReceiptCurrencyAmount | RECEIPT_CURRENCY_AMOUNT | — | — |
| 138 | InvDistReceiptCurrencyCode | RECEIPT_CURRENCY_CODE | — | — |
| 139 | InvDistReceiptMissingFlag | RECEIPT_MISSING_FLAG | — | — |
| 140 | InvDistReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 141 | InvDistReceiptVerifiedFlag | RECEIPT_VERIFIED_FLAG | — | — |
| 142 | InvDistRecoveryRateCode | RECOVERY_RATE_CODE | — | — |
| 143 | InvDistRecoveryRateId | RECOVERY_RATE_ID | — | — |
| 144 | InvDistRecoveryRateName | RECOVERY_RATE_NAME | — | — |
| 145 | InvDistRecoveryTypeCode | RECOVERY_TYPE_CODE | — | — |
| 146 | InvDistRecurringPaymentId | RECURRING_PAYMENT_ID | — | — |
| 147 | InvDistReference1 | REFERENCE_1 | — | — |
| 148 | InvDistReference2 | REFERENCE_2 | — | — |
| 149 | InvDistRelatedId | RELATED_ID | — | — |
| 150 | InvDistRelatedRetainageDistId | RELATED_RETAINAGE_DIST_ID | — | — |
| 151 | InvDistReleaseInvDistDerivedFrom | RELEASE_INV_DIST_DERIVED_FROM | — | — |
| 152 | InvDistRequestId | REQUEST_ID | — | — |
| 153 | InvDistRetainedAmountRemaining | RETAINED_AMOUNT_REMAINING | — | — |
| 154 | InvDistRetainedInvoiceDistId | RETAINED_INVOICE_DIST_ID | — | — |
| 155 | InvDistReversalFlag | REVERSAL_FLAG | — | — |
| 156 | InvDistRootDistributionId | ROOT_DISTRIBUTION_ID | — | — |
| 157 | InvDistRoundingAmt | ROUNDING_AMT | — | — |
| 158 | InvDistSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 159 | InvDistStartExpenseDate | START_EXPENSE_DATE | — | — |
| 160 | InvDistStatAmount | STAT_AMOUNT | — | — |
| 161 | InvDistSummaryTaxLineId | SUMMARY_TAX_LINE_ID | — | — |
| 162 | InvDistTaskId | TASK_ID | — | — |
| 163 | InvDistTaxAlreadyDistributedFlag | TAX_ALREADY_DISTRIBUTED_FLAG | — | — |
| 164 | InvDistTaxCodeId | TAX_CODE_ID | — | — |
| 165 | InvDistTaxRecoverableFlag | TAX_RECOVERABLE_FLAG | — | — |
| 166 | InvDistTaxableAmount | TAXABLE_AMOUNT | — | — |
| 167 | InvDistTaxableBaseAmount | TAXABLE_BASE_AMOUNT | — | — |
| 168 | InvDistTotalDistAmount | TOTAL_DIST_AMOUNT | — | — |
| 169 | InvDistTotalDistBaseAmount | TOTAL_DIST_BASE_AMOUNT | — | — |
| 170 | InvDistType1099 | TYPE_1099 | — | — |
| 171 | InvDistUnitPrice | UNIT_PRICE | — | — |
| 172 | InvDistUpgradeBasePostedAmt | UPGRADE_BASE_POSTED_AMT | — | — |
| 173 | InvDistUpgradePostedAmt | UPGRADE_POSTED_AMT | — | — |
| 174 | InvDistWebParameterId | WEB_PARAMETER_ID | — | — |
| 175 | InvDistWithholdingTaxCodeId | WITHHOLDING_TAX_CODE_ID | — | — |
| 176 | InvDistXinvParentReversalId | XINV_PARENT_REVERSAL_ID | — | — |

### [[ap_invoice_payments_all|AP_INVOICE_PAYMENTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApInvoicePaymentsAllAccountingDate | ACCOUNTING_DATE | — | — |
| 2 | ApInvoicePaymentsAllAccountingEventId | ACCOUNTING_EVENT_ID | — | — |
| 3 | ApInvoicePaymentsAllAcctsPayCodeCombinationId | ACCTS_PAY_CODE_COMBINATION_ID | — | — |
| 4 | ApInvoicePaymentsAllAmount | AMOUNT | — | — |
| 5 | ApInvoicePaymentsAllAmountInvCurr | AMOUNT_INV_CURR | — | — |
| 6 | ApInvoicePaymentsAllAssetCodeCombinationId | ASSET_CODE_COMBINATION_ID | — | — |
| 7 | ApInvoicePaymentsAllAssetsAdditionFlag | ASSETS_ADDITION_FLAG | — | — |
| 8 | ApInvoicePaymentsAllBankAccountNum | BANK_ACCOUNT_NUM | — | — |
| 9 | ApInvoicePaymentsAllBankAccountType | BANK_ACCOUNT_TYPE | — | — |
| 10 | ApInvoicePaymentsAllBankNum | BANK_NUM | — | — |
| 11 | ApInvoicePaymentsAllCheckId | CHECK_ID | — | — |
| 12 | ApInvoicePaymentsAllCreatedBy | CREATED_BY | — | — |
| 13 | ApInvoicePaymentsAllCreationDate | CREATION_DATE | — | — |
| 14 | ApInvoicePaymentsAllDiscountLost | DISCOUNT_LOST | — | — |
| 15 | ApInvoicePaymentsAllDiscountLostInvCurr | DISCOUNT_LOST_INV_CURR | — | — |
| 16 | ApInvoicePaymentsAllDiscountTaken | DISCOUNT_TAKEN | — | — |
| 17 | ApInvoicePaymentsAllDiscountTakenInvCurr | DISCOUNT_TAKEN_INV_CURR | — | — |
| 18 | ApInvoicePaymentsAllExchangeDate | EXCHANGE_DATE | — | — |
| 19 | ApInvoicePaymentsAllExchangeRate | EXCHANGE_RATE | — | — |
| 20 | ApInvoicePaymentsAllExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 21 | ApInvoicePaymentsAllExternalBankAccountId | EXTERNAL_BANK_ACCOUNT_ID | — | — |
| 22 | ApInvoicePaymentsAllGainCodeCombinationId | GAIN_CODE_COMBINATION_ID | — | — |
| 23 | ApInvoicePaymentsAllIbanNumber | IBAN_NUMBER | — | — |
| 24 | ApInvoicePaymentsAllInvOrgId | INV_ORG_ID | — | — |
| 25 | ApInvoicePaymentsAllInvoiceBaseAmount | INVOICE_BASE_AMOUNT | — | — |
| 26 | ApInvoicePaymentsAllInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 27 | ApInvoicePaymentsAllInvoiceId | INVOICE_ID | — | — |
| 28 | ApInvoicePaymentsAllInvoicePaymentId | INVOICE_PAYMENT_ID | — | — |
| 29 | ApInvoicePaymentsAllInvoicePaymentId1 | INVOICE_PAYMENT_ID | — | — |
| 30 | ApInvoicePaymentsAllInvoicePaymentType | INVOICE_PAYMENT_TYPE | — | — |
| 31 | ApInvoicePaymentsAllInvoicingPartyId | INVOICING_PARTY_ID | — | — |
| 32 | ApInvoicePaymentsAllInvoicingPartySiteId | INVOICING_PARTY_SITE_ID | — | — |
| 33 | ApInvoicePaymentsAllInvoicingVendorSiteId | INVOICING_VENDOR_SITE_ID | — | — |
| 34 | ApInvoicePaymentsAllLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 35 | ApInvoicePaymentsAllLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 36 | ApInvoicePaymentsAllLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 37 | ApInvoicePaymentsAllLossCodeCombinationId | LOSS_CODE_COMBINATION_ID | — | — |
| 38 | ApInvoicePaymentsAllMrcExchangeDate | MRC_EXCHANGE_DATE | — | — |
| 39 | ApInvoicePaymentsAllMrcExchangeRateType | MRC_EXCHANGE_RATE_TYPE | — | — |
| 40 | ApInvoicePaymentsAllMrcFuturePayPostedFlag | MRC_FUTURE_PAY_POSTED_FLAG | — | — |
| 41 | ApInvoicePaymentsAllMrcGainCodeCombinationId | MRC_GAIN_CODE_COMBINATION_ID | — | — |
| 42 | ApInvoicePaymentsAllMrcInvoiceBaseAmount | MRC_INVOICE_BASE_AMOUNT | — | — |
| 43 | ApInvoicePaymentsAllMrcLossCodeCombinationId | MRC_LOSS_CODE_COMBINATION_ID | — | — |
| 44 | ApInvoicePaymentsAllMrcPaymentBaseAmount | MRC_PAYMENT_BASE_AMOUNT | — | — |
| 45 | ApInvoicePaymentsAllObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 46 | ApInvoicePaymentsAllObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 47 | ApInvoicePaymentsAllOrgId | ORG_ID | — | — |
| 48 | ApInvoicePaymentsAllPaymentBaseAmount | PAYMENT_BASE_AMOUNT | — | — |
| 49 | ApInvoicePaymentsAllPaymentCurrencyCode | PAYMENT_CURRENCY_CODE | — | — |
| 50 | ApInvoicePaymentsAllPaymentNum | PAYMENT_NUM | — | ✅ |
| 51 | ApInvoicePaymentsAllPeriodName | PERIOD_NAME | — | — |
| 52 | ApInvoicePaymentsAllPostedFlag | POSTED_FLAG | — | — |
| 53 | ApInvoicePaymentsAllRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 54 | ApInvoicePaymentsAllRemitToAddressName | REMIT_TO_ADDRESS_NAME | — | — |
| 55 | ApInvoicePaymentsAllRemitToSupplierId | REMIT_TO_SUPPLIER_ID | — | — |
| 56 | ApInvoicePaymentsAllRemitToSupplierName | REMIT_TO_SUPPLIER_NAME | — | — |
| 57 | ApInvoicePaymentsAllReversalFlag | REVERSAL_FLAG | — | — |
| 58 | ApInvoicePaymentsAllReversalInvPmtId | REVERSAL_INV_PMT_ID | — | — |
| 59 | ApInvoicePaymentsAllSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 60 | ApInvoicePaymentsAllXCurrRate | X_CURR_RATE | — | — |

### [[fa_asset_invoices|FA_ASSET_INVOICES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetInvoiceApDistributionLineNumber | AP_DISTRIBUTION_LINE_NUMBER | — | ✅ |
| 2 | AssetInvoiceAssetId | ASSET_ID | — | — |
| 3 | AssetInvoiceAssetInvoiceId | ASSET_INVOICE_ID | — | — |
| 4 | AssetInvoiceCreateBatchDate | CREATE_BATCH_DATE | — | — |
| 5 | AssetInvoiceCreateBatchId | CREATE_BATCH_ID | — | — |
| 6 | AssetInvoiceCreatedBy | CREATED_BY | — | ✅ |
| 7 | AssetInvoiceCreationDate | CREATION_DATE | — | ✅ |
| 8 | AssetInvoiceDateEffective | DATE_EFFECTIVE | — | ✅ |
| 9 | AssetInvoiceDateIneffective | DATE_INEFFECTIVE | — | ✅ |
| 10 | AssetInvoiceDeletedFlag | DELETED_FLAG | — | ✅ |
| 11 | AssetInvoiceDepreciateInGroupFlag | DEPRECIATE_IN_GROUP_FLAG | — | ✅ |
| 12 | AssetInvoiceDescription | DESCRIPTION | — | ✅ |
| 13 | AssetInvoiceExpenditureOrganizationId | EXPENDITURE_ORGANIZATION_ID | — | — |
| 14 | AssetInvoiceExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 15 | AssetInvoiceFeederSystemName | FEEDER_SYSTEM_NAME | — | ✅ |
| 16 | AssetInvoiceFixedAssetsCost | FIXED_ASSETS_COST | — | ✅ |
| 17 | AssetInvoiceInvoiceDate | INVOICE_DATE | — | ✅ |
| 18 | AssetInvoiceInvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | — |
| 19 | AssetInvoiceInvoiceId | INVOICE_ID | — | — |
| 20 | AssetInvoiceInvoiceLineDescription | INVOICE_LINE_DESCRIPTION | — | ✅ |
| 21 | AssetInvoiceInvoiceLineNumber | INVOICE_LINE_NUMBER | — | ✅ |
| 22 | AssetInvoiceInvoiceLineType | INVOICE_LINE_TYPE | — | ✅ |
| 23 | AssetInvoiceInvoiceNumber | INVOICE_NUMBER | — | ✅ |
| 24 | AssetInvoiceInvoiceTransactionIdIn | INVOICE_TRANSACTION_ID_IN | — | — |
| 25 | AssetInvoiceInvoiceTransactionIdOut | INVOICE_TRANSACTION_ID_OUT | — | — |
| 26 | AssetInvoiceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 27 | AssetInvoiceLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 28 | AssetInvoiceLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 29 | AssetInvoiceMaterialIndicatorFlag | MATERIAL_INDICATOR_FLAG | — | ✅ |
| 30 | AssetInvoiceMergeParentMassAdditionsId | MERGE_PARENT_MASS_ADDITIONS_ID | — | — |
| 31 | AssetInvoiceMergedCode | MERGED_CODE | — | — |
| 32 | AssetInvoiceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 33 | AssetInvoiceParentMassAdditionId | PARENT_MASS_ADDITION_ID | — | — |
| 34 | AssetInvoicePayablesBatchName | PAYABLES_BATCH_NAME | — | ✅ |
| 35 | AssetInvoicePayablesCodeCombinationId | PAYABLES_CODE_COMBINATION_ID | — | — |
| 36 | AssetInvoicePayablesCost | PAYABLES_COST | — | ✅ |
| 37 | AssetInvoicePayablesUnits | PAYABLES_UNITS | — | ✅ |
| 38 | AssetInvoicePoDistributionId | PO_DISTRIBUTION_ID | — | — |
| 39 | AssetInvoicePoNumber | PO_NUMBER | — | ✅ |
| 40 | AssetInvoicePoVendorId | PO_VENDOR_ID | — | — |
| 41 | AssetInvoicePostBatchId | POST_BATCH_ID | — | — |
| 42 | AssetInvoicePriorSourceLineId | PRIOR_SOURCE_LINE_ID | — | — |
| 43 | AssetInvoiceProjectAssetLineId | PROJECT_ASSET_LINE_ID | — | — |
| 44 | AssetInvoiceProjectId | PROJECT_ID | — | — |
| 45 | AssetInvoiceProjectOrganizationId | PROJECT_ORGANIZATION_ID | — | — |
| 46 | AssetInvoiceProjectTxnDocEntryId | PROJECT_TXN_DOC_ENTRY_ID | — | — |
| 47 | AssetInvoiceSplitCode | SPLIT_CODE | — | — |
| 48 | AssetInvoiceSplitMergedCode | SPLIT_MERGED_CODE | — | ✅ |
| 49 | AssetInvoiceSplitParentMassAdditionsId | SPLIT_PARENT_MASS_ADDITIONS_ID | — | — |
| 50 | AssetInvoiceTaskId | TASK_ID | — | — |
| 51 | AssetInvoiceTaskOrganizationId | TASK_ORGANIZATION_ID | — | — |
| 52 | AssetInvoiceUnrevaluedCost | UNREVALUED_COST | — | ✅ |
| 53 | ProjectNumber | PROJECT_NUMBER | — | — |
| 54 | ProjectTaskNumber | PROJECT_TASK_NUMBER | — | — |
| 55 | SourceLineId | SOURCE_LINE_ID | 🔑 | ✅ |

### [[fa_book_controls|FA_BOOK_CONTROLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BookControlAccountingFlexStructure | ACCOUNTING_FLEX_STRUCTURE | — | — |
| 2 | BookControlBookControlId | BOOK_CONTROL_ID | — | — |
| 3 | BookControlBookTypeCode | BOOK_TYPE_CODE | — | — |
| 4 | BookControlSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 5 | TaskStructureObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[fa_invoice_transactions|FA_INVOICE_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvTrxnBookTypeCode | BOOK_TYPE_CODE | — | — |
| 2 | InvTrxnCreatedBy | CREATED_BY | — | — |
| 3 | InvTrxnDateEffective | DATE_EFFECTIVE | — | — |
| 4 | InvTrxnInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 5 | InvTrxnLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | InvTrxnLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | InvTrxnObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | InvTrxnOutBookTypeCode | BOOK_TYPE_CODE | — | — |
| 9 | InvTrxnOutCreatedBy | CREATED_BY | — | — |
| 10 | InvTrxnOutDateEffective | DATE_EFFECTIVE | — | — |
| 11 | InvTrxnOutInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 12 | InvTrxnOutLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | InvTrxnOutLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | InvTrxnOutObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | InvTrxnOutTransactionType | TRANSACTION_TYPE | — | — |
| 16 | InvTrxnTransactionType | TRANSACTION_TYPE | — | — |

### [[hr_all_organization_units_f_vl|HR_ALL_ORGANIZATION_UNITS_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpOrganizationUnitEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | ExpOrganizationUnitEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | ExpOrganizationUnitName | NAME | — | ✅ |
| 4 | ExpOrganizationUnitObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | ExpOrganizationUnitOrganizationId | ORGANIZATION_ID | — | — |
| 6 | PrjOrganizationUnitEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | PrjOrganizationUnitEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 8 | PrjOrganizationUnitName | NAME | — | ✅ |
| 9 | PrjOrganizationUnitObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | PrjOrganizationUnitOrganizationId | ORGANIZATION_ID | — | — |
| 11 | TaskOrganizationUnitEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 12 | TaskOrganizationUnitEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 13 | TaskOrganizationUnitName | NAME | — | ✅ |
| 14 | TaskOrganizationUnitObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | TaskOrganizationUnitOrganizationId | ORGANIZATION_ID | — | — |

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
| 1 | UserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | UserCreatedByPersonId | PERSON_ID | — | — |
| 3 | UserCreatedByUserGuid | USER_GUID | — | — |
| 4 | UserCreatedByUserId | USER_ID | — | — |
| 5 | UserCreatedByUsername | USERNAME | — | — |
| 6 | UserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 8 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 9 | UserUpdatedByUserId | USER_ID | — | — |
| 10 | UserUpdatedByUsername | USERNAME | — | — |

### [[pjc_prj_asset_lns_all|PJC_PRJ_ASSET_LNS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrjAssetLineAmortizeFlag | AMORTIZE_FLAG | — | — |
| 2 | PrjAssetLineApDistributionLineNumber | AP_DISTRIBUTION_LINE_NUMBER | — | — |
| 3 | PrjAssetLineAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 4 | PrjAssetLineAssetCostCcid | ASSET_COST_CCID | — | — |
| 5 | PrjAssetLineCapitalEventId | CAPITAL_EVENT_ID | — | — |
| 6 | PrjAssetLineCipCcid | CIP_CCID | — | — |
| 7 | PrjAssetLineCreatedBy | CREATED_BY | — | — |
| 8 | PrjAssetLineCreationDate | CREATION_DATE | — | — |
| 9 | PrjAssetLineCurrentAssetCost | CURRENT_ASSET_COST | — | — |
| 10 | PrjAssetLineDescription | DESCRIPTION | — | ✅ |
| 11 | PrjAssetLineFaPeriodName | FA_PERIOD_NAME | — | — |
| 12 | PrjAssetLineGlDate | GL_DATE | — | — |
| 13 | PrjAssetLineInvoiceCreatedBy | INVOICE_CREATED_BY | — | — |
| 14 | PrjAssetLineInvoiceDate | INVOICE_DATE | — | — |
| 15 | PrjAssetLineInvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | — |
| 16 | PrjAssetLineInvoiceId | INVOICE_ID | — | — |
| 17 | PrjAssetLineInvoiceLineNumber | INVOICE_LINE_NUMBER | — | — |
| 18 | PrjAssetLineInvoiceNumber | INVOICE_NUMBER | — | — |
| 19 | PrjAssetLineInvoiceUpdatedBy | INVOICE_UPDATED_BY | — | — |
| 20 | PrjAssetLineJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 21 | PrjAssetLineJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 22 | PrjAssetLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | PrjAssetLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 24 | PrjAssetLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 25 | PrjAssetLineLineType | LINE_TYPE | — | — |
| 26 | PrjAssetLineNewMasterFlag | NEW_MASTER_FLAG | — | — |
| 27 | PrjAssetLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 28 | PrjAssetLineOrgId | ORG_ID | — | — |
| 29 | PrjAssetLineOriginalAssetCost | ORIGINAL_ASSET_COST | — | — |
| 30 | PrjAssetLineOriginalAssetId | ORIGINAL_ASSET_ID | — | — |
| 31 | PrjAssetLinePayablesBatchName | PAYABLES_BATCH_NAME | — | — |
| 32 | PrjAssetLinePoNumber | PO_NUMBER | — | — |
| 33 | PrjAssetLinePoVendorId | PO_VENDOR_ID | — | — |
| 34 | PrjAssetLineProjectAssetId | PROJECT_ASSET_ID | — | — |
| 35 | PrjAssetLineProjectAssetLineDetailId | PROJECT_ASSET_LINE_DETAIL_ID | — | — |
| 36 | PrjAssetLineProjectAssetLineId | PROJECT_ASSET_LINE_ID | — | — |
| 37 | PrjAssetLineProjectId | PROJECT_ID | — | — |
| 38 | PrjAssetLineRequestId | REQUEST_ID | — | — |
| 39 | PrjAssetLineRetAdjustmentTxnId | RET_ADJUSTMENT_TXN_ID | — | — |
| 40 | PrjAssetLineRetirementCostType | RETIREMENT_COST_TYPE | — | — |
| 41 | PrjAssetLineRevFromProjAssetLineId | REV_FROM_PROJ_ASSET_LINE_ID | — | — |
| 42 | PrjAssetLineRevProjAssetLineId | REV_PROJ_ASSET_LINE_ID | — | — |
| 43 | PrjAssetLineTaskId | TASK_ID | — | — |
| 44 | PrjAssetLineTransferRejectionReason | TRANSFER_REJECTION_REASON | — | — |
| 45 | PrjAssetLineTransferStatusCode | TRANSFER_STATUS_CODE | — | — |
| 46 | PrjAssetLineVendorNumber | VENDOR_NUMBER | — | — |

### [[pjf_exp_types_tl|PJF_EXP_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureTypeCreatedBy | CREATED_BY | — | — |
| 2 | ExpenditureTypeCreationDate | CREATION_DATE | — | — |
| 3 | ExpenditureTypeDescription | DESCRIPTION | — | — |
| 4 | ExpenditureTypeExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 5 | ExpenditureTypeExpenditureTypeName | EXPENDITURE_TYPE_NAME | — | ✅ |
| 6 | ExpenditureTypeLanguage | LANGUAGE | — | — |
| 7 | ExpenditureTypeLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | ExpenditureTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ExpenditureTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ExpenditureTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[pjf_projects_all_vl|PJF_PROJECTS_ALL_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectDescription | DESCRIPTION | — | ✅ |
| 2 | ProjectName | NAME | — | ✅ |
| 3 | ProjectProjectId | PROJECT_ID | — | — |
| 4 | ProjectSegment1 | SEGMENT1 | — | ✅ |
| 5 | TaskStructureObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |

### [[pjf_proj_elements_vl|PJF_PROJ_ELEMENTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskStructureAllowCrossChargeFlag | ALLOW_CROSS_CHARGE_FLAG | — | — |
| 2 | TaskStructureBaselineFinishDate | BASELINE_FINISH_DATE | — | — |
| 3 | TaskStructureBaselineStartDate | BASELINE_START_DATE | — | — |
| 4 | TaskStructureBillableFlag | BILLABLE_FLAG | — | — |
| 5 | TaskStructureCapitalizableFlag | CAPITALIZABLE_FLAG | — | — |
| 6 | TaskStructureCarryingOutOrganizationId | CARRYING_OUT_ORGANIZATION_ID | — | — |
| 7 | TaskStructureCcProcessLaborFlag | CC_PROCESS_LABOR_FLAG | — | — |
| 8 | TaskStructureCcProcessNlFlag | CC_PROCESS_NL_FLAG | — | — |
| 9 | TaskStructureChargeableFlag | CHARGEABLE_FLAG | — | — |
| 10 | TaskStructureCintEligibleFlag | CINT_ELIGIBLE_FLAG | — | — |
| 11 | TaskStructureCintStopDate | CINT_STOP_DATE | — | — |
| 12 | TaskStructureClinElementId | CLIN_ELEMENT_ID | — | — |
| 13 | TaskStructureCompletionDate | COMPLETION_DATE | — | — |
| 14 | TaskStructureCostIndRateSchId | COST_IND_RATE_SCH_ID | — | — |
| 15 | TaskStructureCostIndSchFixedDate | COST_IND_SCH_FIXED_DATE | — | — |
| 16 | TaskStructureCreatedBy | CREATED_BY | — | — |
| 17 | TaskStructureCreatedFromSourceId | CREATED_FROM_SOURCE_ID | — | — |
| 18 | TaskStructureCreationDate | CREATION_DATE | — | — |
| 19 | TaskStructureCriticalFlag | CRITICAL_FLAG | — | — |
| 20 | TaskStructureDenormDisplaySequence | DENORM_DISPLAY_SEQUENCE | — | — |
| 21 | TaskStructureDenormElemVerId | DENORM_ELEM_VER_ID | — | — |
| 22 | TaskStructureDenormExecutionDispSeq | DENORM_EXECUTION_DISP_SEQ | — | — |
| 23 | TaskStructureDenormParentElemVerId | DENORM_PARENT_ELEM_VER_ID | — | — |
| 24 | TaskStructureDenormParentElementId | DENORM_PARENT_ELEMENT_ID | — | — |
| 25 | TaskStructureDenormParentObjectType | DENORM_PARENT_OBJECT_TYPE | — | — |
| 26 | TaskStructureDenormParentStructVerId | DENORM_PARENT_STRUCT_VER_ID | — | — |
| 27 | TaskStructureDenormTopElementId | DENORM_TOP_ELEMENT_ID | — | — |
| 28 | TaskStructureDenormWbsLevel | DENORM_WBS_LEVEL | — | — |
| 29 | TaskStructureDenormWbsNumber | DENORM_WBS_NUMBER | — | — |
| 30 | TaskStructureDescription | DESCRIPTION | — | — |
| 31 | TaskStructureElementNumber | ELEMENT_NUMBER | — | ✅ |
| 32 | TaskStructureElementType | ELEMENT_TYPE | — | — |
| 33 | TaskStructureEtcCalcMethod | ETC_CALC_METHOD | — | — |
| 34 | TaskStructureExternalId | EXTERNAL_ID | — | — |
| 35 | TaskStructureGenEtcSourceCode | GEN_ETC_SOURCE_CODE | — | — |
| 36 | TaskStructureIcClinElementId | IC_CLIN_ELEMENT_ID | — | — |
| 37 | TaskStructureIssueId | ISSUE_ID | — | — |
| 38 | TaskStructureLaborCostMultiplierName | LABOR_COST_MULTIPLIER_NAME | — | — |
| 39 | TaskStructureLaborTpFixedDate | LABOR_TP_FIXED_DATE | — | — |
| 40 | TaskStructureLaborTpScheduleId | LABOR_TP_SCHEDULE_ID | — | — |
| 41 | TaskStructureLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 42 | TaskStructureLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 43 | TaskStructureLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 44 | TaskStructureLastViewedDate | LAST_VIEWED_DATE | — | — |
| 45 | TaskStructureLeafNodeFlag | LEAF_NODE_FLAG | — | — |
| 46 | TaskStructureLimitToTxnControlsFlag | LIMIT_TO_TXN_CONTROLS_FLAG | — | — |
| 47 | TaskStructureManagerPersonId | MANAGER_PERSON_ID | — | — |
| 48 | TaskStructureMilestoneFlag | MILESTONE_FLAG | — | — |
| 49 | TaskStructureName | NAME | — | ✅ |
| 50 | TaskStructureNlTpFixedDate | NL_TP_FIXED_DATE | — | — |
| 51 | TaskStructureNlTpScheduleId | NL_TP_SCHEDULE_ID | — | — |
| 52 | TaskStructureObjectAssociationBitmap | OBJECT_ASSOCIATION_BITMAP | — | — |
| 53 | TaskStructureObjectType | OBJECT_TYPE | — | — |
| 54 | TaskStructureObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 55 | TaskStructureOvrCostIndRateSchId | OVR_COST_IND_RATE_SCH_ID | — | — |
| 56 | TaskStructureParentStructureId | PARENT_STRUCTURE_ID | — | — |
| 57 | TaskStructurePercentCompCalcMethod | PERCENT_COMP_CALC_METHOD | — | — |
| 58 | TaskStructurePlanningDatesRollupFlag | PLANNING_DATES_ROLLUP_FLAG | — | — |
| 59 | TaskStructurePlanningEndDate | PLANNING_END_DATE | — | — |
| 60 | TaskStructurePlanningStartDate | PLANNING_START_DATE | — | — |
| 61 | TaskStructurePmSourceCode | PM_SOURCE_CODE | — | — |
| 62 | TaskStructurePmSourceReference | PM_SOURCE_REFERENCE | — | — |
| 63 | TaskStructurePrimaryResourceId | PRIMARY_RESOURCE_ID | — | — |
| 64 | TaskStructureProjElementId | PROJ_ELEMENT_ID | — | — |
| 65 | TaskStructureProjElementId1 | PROJ_ELEMENT_ID | — | — |
| 66 | TaskStructureProjectId | PROJECT_ID | — | — |
| 67 | TaskStructureReceiveProjectInvoiceFlag | RECEIVE_PROJECT_INVOICE_FLAG | — | — |
| 68 | TaskStructureRetirementCostFlag | RETIREMENT_COST_FLAG | — | — |
| 69 | TaskStructureRqmtId | RQMT_ID | — | — |
| 70 | TaskStructureServiceTypeCode | SERVICE_TYPE_CODE | — | — |
| 71 | TaskStructureSiteUseId | SITE_USE_ID | — | — |
| 72 | TaskStructureSprintId | SPRINT_ID | — | — |
| 73 | TaskStructureStartDate | START_DATE | — | — |
| 74 | TaskStructureStructureType | STRUCTURE_TYPE | — | — |
| 75 | TaskStructureWorkTypeId | WORK_TYPE_ID | — | — |

### [[pjf_txn_doc_entry_vl|PJF_TXN_DOC_ENTRY_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionDocEntryDescription | DESCRIPTION | — | — |
| 2 | TransactionDocEntryDocEntryCode | DOC_ENTRY_CODE | — | — |
| 3 | TransactionDocEntryDocEntryId | DOC_ENTRY_ID | — | — |
| 4 | TransactionDocEntryDocEntryName | DOC_ENTRY_NAME | — | ✅ |
| 5 | TransactionDocEntryDocumentId | DOCUMENT_ID | — | — |

### [[poz_suppliers_v|POZ_SUPPLIERS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupplierNameAllowAwtFlag | ALLOW_AWT_FLAG | — | — |
| 2 | SupplierNameAwtGroupId | AWT_GROUP_ID | — | — |
| 3 | SupplierNameCorporateWebsite | CORPORATE_WEBSITE | — | — |
| 4 | SupplierNameCustomerNum | CUSTOMER_NUM | — | — |
| 5 | SupplierNameEndDateActive | END_DATE_ACTIVE | — | — |
| 6 | SupplierNameFederalReportableFlag | FEDERAL_REPORTABLE_FLAG | — | — |
| 7 | SupplierNameMinOrderAmount | MIN_ORDER_AMOUNT | — | — |
| 8 | SupplierNameNameControl | NAME_CONTROL | — | — |
| 9 | SupplierNameNiNumber | NI_NUMBER | — | — |
| 10 | SupplierNameOneTimeFlag | ONE_TIME_FLAG | — | — |
| 11 | SupplierNameOrganizationTypeLookupCode | ORGANIZATION_TYPE_LOOKUP_CODE | — | — |
| 12 | SupplierNameParentPartyId | PARENT_PARTY_ID | — | — |
| 13 | SupplierNameParentVendorId | PARENT_VENDOR_ID | — | — |
| 14 | SupplierNamePartyId | PARTY_ID | — | — |
| 15 | SupplierNameProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 16 | SupplierNameProgramId | PROGRAM_ID | — | — |
| 17 | SupplierNameProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 18 | SupplierNameRequestId | REQUEST_ID | — | — |
| 19 | SupplierNameSegment1 | SEGMENT1 | — | — |
| 20 | SupplierNameStandardIndustryClass | STANDARD_INDUSTRY_CLASS | — | — |
| 21 | SupplierNameStartDateActive | START_DATE_ACTIVE | — | — |
| 22 | SupplierNameStateReportableFlag | STATE_REPORTABLE_FLAG | — | — |
| 23 | SupplierNameTaxReportingName | TAX_REPORTING_NAME | — | — |
| 24 | SupplierNameTaxVerificationDate | TAX_VERIFICATION_DATE | — | — |
| 25 | SupplierNameType1099 | TYPE_1099 | — | — |
| 26 | SupplierNameVendorId | VENDOR_ID | — | — |
| 27 | SupplierNameVendorName | VENDOR_NAME | — | ✅ |
| 28 | SupplierNameVendorNameAlt | VENDOR_NAME_ALT | — | — |
| 29 | SupplierNameVendorTypeLookupCode | VENDOR_TYPE_LOOKUP_CODE | — | — |
| 30 | SupplierNameWithholdingStartDate | WITHHOLDING_START_DATE | — | — |
| 31 | SupplierNameWithholdingStatusLookupCode | WITHHOLDING_STATUS_LOOKUP_CODE | — | — |

### [[po_distributions_all|PO_DISTRIBUTIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PODistributionAccrualAccountId | ACCRUAL_ACCOUNT_ID | — | — |
| 2 | PODistributionAccrueOnReceiptFlag | ACCRUE_ON_RECEIPT_FLAG | — | — |
| 3 | PODistributionAccruedFlag | ACCRUED_FLAG | — | — |
| 4 | PODistributionAmountBilled | AMOUNT_BILLED | — | — |
| 5 | PODistributionAmountCancelled | AMOUNT_CANCELLED | — | — |
| 6 | PODistributionAmountDelivered | AMOUNT_DELIVERED | — | — |
| 7 | PODistributionAmountFinanced | AMOUNT_FINANCED | — | — |
| 8 | PODistributionAmountOrdered | AMOUNT_ORDERED | — | — |
| 9 | PODistributionAmountRecouped | AMOUNT_RECOUPED | — | — |
| 10 | PODistributionAmountToEncumber | AMOUNT_TO_ENCUMBER | — | — |
| 11 | PODistributionAwardId | AWARD_ID | — | — |
| 12 | PODistributionBomResourceId | BOM_RESOURCE_ID | — | — |
| 13 | PODistributionBudgetAccountId | BUDGET_ACCOUNT_ID | — | — |
| 14 | PODistributionCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 15 | PODistributionCreatedBy | CREATED_BY | — | — |
| 16 | PODistributionCreationDate | CREATION_DATE | — | — |
| 17 | PODistributionDeliverToLocationId | DELIVER_TO_LOCATION_ID | — | — |
| 18 | PODistributionDeliverToPersonId | DELIVER_TO_PERSON_ID | — | — |
| 19 | PODistributionDestChargeAccountId | DEST_CHARGE_ACCOUNT_ID | — | — |
| 20 | PODistributionDestVarianceAccountId | DEST_VARIANCE_ACCOUNT_ID | — | — |
| 21 | PODistributionDestinationContext | DESTINATION_CONTEXT | — | — |
| 22 | PODistributionDestinationOrganizationId | DESTINATION_ORGANIZATION_ID | — | — |
| 23 | PODistributionDestinationSubinventory | DESTINATION_SUBINVENTORY | — | — |
| 24 | PODistributionDestinationTypeCode | DESTINATION_TYPE_CODE | — | — |
| 25 | PODistributionDistIntendedUse | DIST_INTENDED_USE | — | — |
| 26 | PODistributionDistributionNum | DISTRIBUTION_NUM | — | ✅ |
| 27 | PODistributionDistributionType | DISTRIBUTION_TYPE | — | — |
| 28 | PODistributionEncumberedAmount | ENCUMBERED_AMOUNT | — | — |
| 29 | PODistributionEncumberedFlag | ENCUMBERED_FLAG | — | — |
| 30 | PODistributionEndItemUnitNumber | END_ITEM_UNIT_NUMBER | — | — |
| 31 | PODistributionFailedFundsLookupCode | FAILED_FUNDS_LOOKUP_CODE | — | — |
| 32 | PODistributionGlCancelledDate | GL_CANCELLED_DATE | — | — |
| 33 | PODistributionGlClosedDate | GL_CLOSED_DATE | — | — |
| 34 | PODistributionGlEncumberedDate | GL_ENCUMBERED_DATE | — | — |
| 35 | PODistributionGlEncumberedPeriodName | GL_ENCUMBERED_PERIOD_NAME | — | — |
| 36 | PODistributionGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 37 | PODistributionInterfaceDistributionRef | INTERFACE_DISTRIBUTION_REF | — | — |
| 38 | PODistributionInvoiceAdjustmentFlag | INVOICE_ADJUSTMENT_FLAG | — | — |
| 39 | PODistributionInvoicedValInNtfn | INVOICED_VAL_IN_NTFN | — | — |
| 40 | PODistributionJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 41 | PODistributionJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 42 | PODistributionKanbanCardId | KANBAN_CARD_ID | — | — |
| 43 | PODistributionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 44 | PODistributionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 45 | PODistributionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 46 | PODistributionLineLocationId | LINE_LOCATION_ID | — | — |
| 47 | PODistributionNonrecoverableTax | NONRECOVERABLE_TAX | — | — |
| 48 | PODistributionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 49 | PODistributionOkeContractDeliverableId | OKE_CONTRACT_DELIVERABLE_ID | — | — |
| 50 | PODistributionOkeContractLineId | OKE_CONTRACT_LINE_ID | — | — |
| 51 | PODistributionPJC_BILLABLE_FLAG | PJC_BILLABLE_FLAG | — | — |
| 52 | PODistributionPJC_CAPITALIZABLE_FLAG | PJC_CAPITALIZABLE_FLAG | — | — |
| 53 | PODistributionPJC_CONTEXT_CATEGORY | PJC_CONTEXT_CATEGORY | — | — |
| 54 | PODistributionPJC_CONTRACT_ID | PJC_CONTRACT_ID | — | — |
| 55 | PODistributionPJC_CONTRACT_LINE_ID | PJC_CONTRACT_LINE_ID | — | — |
| 56 | PODistributionPJC_EXPENDITURE_ITEM_DATE | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 57 | PODistributionPJC_EXPENDITURE_TYPE_ID | PJC_EXPENDITURE_TYPE_ID | — | — |
| 58 | PODistributionPJC_FUNDING_ALLOCATION_ID | PJC_FUNDING_ALLOCATION_ID | — | — |
| 59 | PODistributionPJC_ORGANIZATION_ID | PJC_ORGANIZATION_ID | — | — |
| 60 | PODistributionPJC_PROJECT_ID | PJC_PROJECT_ID | — | — |
| 61 | PODistributionPJC_RESERVED_ATTRIBUTE1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 62 | PODistributionPJC_RESERVED_ATTRIBUTE10 | PJC_RESERVED_ATTRIBUTE10 | — | — |
| 63 | PODistributionPJC_RESERVED_ATTRIBUTE2 | PJC_RESERVED_ATTRIBUTE2 | — | — |
| 64 | PODistributionPJC_RESERVED_ATTRIBUTE3 | PJC_RESERVED_ATTRIBUTE3 | — | — |
| 65 | PODistributionPJC_RESERVED_ATTRIBUTE4 | PJC_RESERVED_ATTRIBUTE4 | — | — |
| 66 | PODistributionPJC_RESERVED_ATTRIBUTE5 | PJC_RESERVED_ATTRIBUTE5 | — | — |
| 67 | PODistributionPJC_RESERVED_ATTRIBUTE6 | PJC_RESERVED_ATTRIBUTE6 | — | — |
| 68 | PODistributionPJC_RESERVED_ATTRIBUTE7 | PJC_RESERVED_ATTRIBUTE7 | — | — |
| 69 | PODistributionPJC_RESERVED_ATTRIBUTE8 | PJC_RESERVED_ATTRIBUTE8 | — | — |
| 70 | PODistributionPJC_RESERVED_ATTRIBUTE9 | PJC_RESERVED_ATTRIBUTE9 | — | — |
| 71 | PODistributionPJC_TASK_ID | PJC_TASK_ID | — | — |
| 72 | PODistributionPJC_USER_DEF_ATTRIBUTE1 | PJC_USER_DEF_ATTRIBUTE1 | — | — |
| 73 | PODistributionPJC_USER_DEF_ATTRIBUTE10 | PJC_USER_DEF_ATTRIBUTE10 | — | — |
| 74 | PODistributionPJC_USER_DEF_ATTRIBUTE2 | PJC_USER_DEF_ATTRIBUTE2 | — | — |
| 75 | PODistributionPJC_USER_DEF_ATTRIBUTE3 | PJC_USER_DEF_ATTRIBUTE3 | — | — |
| 76 | PODistributionPJC_USER_DEF_ATTRIBUTE4 | PJC_USER_DEF_ATTRIBUTE4 | — | — |
| 77 | PODistributionPJC_USER_DEF_ATTRIBUTE5 | PJC_USER_DEF_ATTRIBUTE5 | — | — |
| 78 | PODistributionPJC_USER_DEF_ATTRIBUTE6 | PJC_USER_DEF_ATTRIBUTE6 | — | — |
| 79 | PODistributionPJC_USER_DEF_ATTRIBUTE7 | PJC_USER_DEF_ATTRIBUTE7 | — | — |
| 80 | PODistributionPJC_USER_DEF_ATTRIBUTE8 | PJC_USER_DEF_ATTRIBUTE8 | — | — |
| 81 | PODistributionPJC_USER_DEF_ATTRIBUTE9 | PJC_USER_DEF_ATTRIBUTE9 | — | — |
| 82 | PODistributionPJC_WORK_TYPE_ID | PJC_WORK_TYPE_ID | — | — |
| 83 | PODistributionPoDistributionId | PO_DISTRIBUTION_ID | — | — |
| 84 | PODistributionPoHeaderId | PO_HEADER_ID | — | — |
| 85 | PODistributionPoLineId | PO_LINE_ID | — | — |
| 86 | PODistributionPrcBuId | PRC_BU_ID | — | — |
| 87 | PODistributionPreventEncumbranceFlag | PREVENT_ENCUMBRANCE_FLAG | — | — |
| 88 | PODistributionProgramAppName | PROGRAM_APP_NAME | — | — |
| 89 | PODistributionProgramName | PROGRAM_NAME | — | — |
| 90 | PODistributionQuantityBilled | QUANTITY_BILLED | — | — |
| 91 | PODistributionQuantityCancelled | QUANTITY_CANCELLED | — | — |
| 92 | PODistributionQuantityDelivered | QUANTITY_DELIVERED | — | — |
| 93 | PODistributionQuantityFinanced | QUANTITY_FINANCED | — | — |
| 94 | PODistributionQuantityOrdered | QUANTITY_ORDERED | — | — |
| 95 | PODistributionQuantityRecouped | QUANTITY_RECOUPED | — | — |
| 96 | PODistributionRate | RATE | — | — |
| 97 | PODistributionRateDate | RATE_DATE | — | — |
| 98 | PODistributionRecoverableTax | RECOVERABLE_TAX | — | — |
| 99 | PODistributionRecoveryRate | RECOVERY_RATE | — | — |
| 100 | PODistributionReqBuId | REQ_BU_ID | — | — |
| 101 | PODistributionReqDistributionId | REQ_DISTRIBUTION_ID | — | — |
| 102 | PODistributionReqHeaderReferenceNum | REQ_HEADER_REFERENCE_NUM | — | — |
| 103 | PODistributionReqLineReferenceNum | REQ_LINE_REFERENCE_NUM | — | — |
| 104 | PODistributionRequestId | REQUEST_ID | — | — |
| 105 | PODistributionRetainageReleasedAmount | RETAINAGE_RELEASED_AMOUNT | — | — |
| 106 | PODistributionRetainageWithheldAmount | RETAINAGE_WITHHELD_AMOUNT | — | — |
| 107 | PODistributionSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 108 | PODistributionSourceDistributionId | SOURCE_DISTRIBUTION_ID | — | — |
| 109 | PODistributionTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 110 | PODistributionTaxRecoveryOverrideFlag | TAX_RECOVERY_OVERRIDE_FLAG | — | — |
| 111 | PODistributionUnencumberedAmount | UNENCUMBERED_AMOUNT | — | — |
| 112 | PODistributionUnencumberedQuantity | UNENCUMBERED_QUANTITY | — | — |
| 113 | PODistributionVarianceAccountId | VARIANCE_ACCOUNT_ID | — | — |
| 114 | PODistributionWipEntityId | WIP_ENTITY_ID | — | — |
| 115 | PODistributionWipLineId | WIP_LINE_ID | — | — |
| 116 | PODistributionWipOperationSeqNum | WIP_OPERATION_SEQ_NUM | — | — |
| 117 | PODistributionWipRepetitiveScheduleId | WIP_REPETITIVE_SCHEDULE_ID | — | — |
| 118 | PODistributionWipResourceSeqNum | WIP_RESOURCE_SEQ_NUM | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
