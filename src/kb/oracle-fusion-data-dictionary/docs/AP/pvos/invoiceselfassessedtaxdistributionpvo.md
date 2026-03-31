---
id: DOC-AP-PVO-InvoiceSelfAssessedTaxDistributionPVO
doc_type: system-doc
title: "InvoiceSelfAssessedTaxDistributionPVO — PVO Accounts Payable"
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
  - InvoiceSelfAssessedTaxDistributionPVO
  - invoiceselfassessedtaxdistributionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvoiceSelfAssessedTaxDistributionPVO

## 📌 Visão Geral

Extrai as distribuições de impostos auto-avaliados (self-assessed) em faturas, incluindo regime fiscal, alíquota e valores. Necessário para conformidade com obrigações tributárias de autolancamento, como reverse charge em operações internacionais.

**Caminho:** `FscmTopModelAM.FinApInvTransactionsAM.InvoiceSelfAssessedTaxDistributionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 149 | 4 | 1 | 14 | 9% |

---

## 🔗 Tabelas Relacionadas

- [[ap_self_assessed_tax_dist_all|AP_SELF_ASSESSED_TAX_DIST_ALL]] — 126 atributos (1 PKs, 14 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 1 atributos
- [[gl_ledgers|GL_LEDGERS]] — 4 atributos
- [[zx_lines|ZX_LINES]] — 18 atributos

---

## ⚙️ Atributos

### [[ap_self_assessed_tax_dist_all|AP_SELF_ASSESSED_TAX_DIST_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceDistributionId | INVOICE_DISTRIBUTION_ID | 🔑 | ✅ |
| 2 | InvoiceSelfAssessedTaxChargeApplicableToDistId | CHARGE_APPLICABLE_TO_DIST_ID | — | — |
| 3 | InvoiceSelfAssessedTaxDistAccountingDate | ACCOUNTING_DATE | — | ✅ |
| 4 | InvoiceSelfAssessedTaxDistAccountingEventId | ACCOUNTING_EVENT_ID | — | — |
| 5 | InvoiceSelfAssessedTaxDistAdjustmentReason | ADJUSTMENT_REASON | — | ✅ |
| 6 | InvoiceSelfAssessedTaxDistAmount | AMOUNT | — | ✅ |
| 7 | InvoiceSelfAssessedTaxDistAmountVariance | AMOUNT_VARIANCE | — | — |
| 8 | InvoiceSelfAssessedTaxDistAssetBookTypeCode | ASSET_BOOK_TYPE_CODE | — | — |
| 9 | InvoiceSelfAssessedTaxDistAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 10 | InvoiceSelfAssessedTaxDistAssetsAdditionFlag | ASSETS_ADDITION_FLAG | — | — |
| 11 | InvoiceSelfAssessedTaxDistAssetsTrackingFlag | ASSETS_TRACKING_FLAG | — | — |
| 12 | InvoiceSelfAssessedTaxDistAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 13 | InvoiceSelfAssessedTaxDistAwardId | AWARD_ID | — | — |
| 14 | InvoiceSelfAssessedTaxDistAwtFlag | AWT_FLAG | — | — |
| 15 | InvoiceSelfAssessedTaxDistAwtGrossAmount | AWT_GROSS_AMOUNT | — | — |
| 16 | InvoiceSelfAssessedTaxDistAwtGroupId | AWT_GROUP_ID | — | — |
| 17 | InvoiceSelfAssessedTaxDistAwtInvoiceId | AWT_INVOICE_ID | — | — |
| 18 | InvoiceSelfAssessedTaxDistAwtInvoicePaymentId | AWT_INVOICE_PAYMENT_ID | — | — |
| 19 | InvoiceSelfAssessedTaxDistAwtOriginGroupId | AWT_ORIGIN_GROUP_ID | — | — |
| 20 | InvoiceSelfAssessedTaxDistAwtTaxRateId | AWT_TAX_RATE_ID | — | — |
| 21 | InvoiceSelfAssessedTaxDistAwtWithheldAmt | AWT_WITHHELD_AMT | — | — |
| 22 | InvoiceSelfAssessedTaxDistBaseAmount | BASE_AMOUNT | — | ✅ |
| 23 | InvoiceSelfAssessedTaxDistBaseAmountVariance | BASE_AMOUNT_VARIANCE | — | — |
| 24 | InvoiceSelfAssessedTaxDistBaseQuantityVariance | BASE_QUANTITY_VARIANCE | — | — |
| 25 | InvoiceSelfAssessedTaxDistBatchId | BATCH_ID | — | — |
| 26 | InvoiceSelfAssessedTaxDistBcEventId | BC_EVENT_ID | — | — |
| 27 | InvoiceSelfAssessedTaxDistCancellationFlag | CANCELLATION_FLAG | — | ✅ |
| 28 | InvoiceSelfAssessedTaxDistCcReversalFlag | CC_REVERSAL_FLAG | — | — |
| 29 | InvoiceSelfAssessedTaxDistCompanyPrepaidInvoiceId | COMPANY_PREPAID_INVOICE_ID | — | — |
| 30 | InvoiceSelfAssessedTaxDistCorrectedInvoiceDistId | CORRECTED_INVOICE_DIST_ID | — | — |
| 31 | InvoiceSelfAssessedTaxDistCorrectedQuantity | CORRECTED_QUANTITY | — | — |
| 32 | InvoiceSelfAssessedTaxDistCountryOfSupply | COUNTRY_OF_SUPPLY | — | — |
| 33 | InvoiceSelfAssessedTaxDistCreatedBy | CREATED_BY | — | — |
| 34 | InvoiceSelfAssessedTaxDistCreationDate | CREATION_DATE | — | — |
| 35 | InvoiceSelfAssessedTaxDistCreditCardTrxId | CREDIT_CARD_TRX_ID | — | — |
| 36 | InvoiceSelfAssessedTaxDistCurrencyCode | RECEIPT_CURRENCY_CODE | — | — |
| 37 | InvoiceSelfAssessedTaxDistDailyAmount | DAILY_AMOUNT | — | — |
| 38 | InvoiceSelfAssessedTaxDistDescription | DESCRIPTION | — | — |
| 39 | InvoiceSelfAssessedTaxDistDetailTaxDistId | DETAIL_TAX_DIST_ID | — | — |
| 40 | InvoiceSelfAssessedTaxDistDistCodeCombinationId | DIST_CODE_COMBINATION_ID | — | — |
| 41 | InvoiceSelfAssessedTaxDistDistMatchType | DIST_MATCH_TYPE | — | — |
| 42 | InvoiceSelfAssessedTaxDistDistributionClass | DISTRIBUTION_CLASS | — | — |
| 43 | InvoiceSelfAssessedTaxDistDistributionLineNumber | DISTRIBUTION_LINE_NUMBER | — | ✅ |
| 44 | InvoiceSelfAssessedTaxDistEncumberedFlag | ENCUMBERED_FLAG | — | — |
| 45 | InvoiceSelfAssessedTaxDistEndExpenseDate | END_EXPENSE_DATE | — | — |
| 46 | InvoiceSelfAssessedTaxDistExpenditureItemDate | EXPENDITURE_ITEM_DATE | — | — |
| 47 | InvoiceSelfAssessedTaxDistExpenditureOrganizationId | EXPENDITURE_ORGANIZATION_ID | — | — |
| 48 | InvoiceSelfAssessedTaxDistExpenditureType | EXPENDITURE_TYPE | — | — |
| 49 | InvoiceSelfAssessedTaxDistExpenseGroup | EXPENSE_GROUP | — | — |
| 50 | InvoiceSelfAssessedTaxDistExtraPoErv | EXTRA_PO_ERV | — | — |
| 51 | InvoiceSelfAssessedTaxDistFinalMatchFlag | FINAL_MATCH_FLAG | — | — |
| 52 | InvoiceSelfAssessedTaxDistGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 53 | InvoiceSelfAssessedTaxDistGmsBurdenableRawCost | GMS_BURDENABLE_RAW_COST | — | — |
| 54 | InvoiceSelfAssessedTaxDistIncomeTaxRegion | INCOME_TAX_REGION | — | — |
| 55 | InvoiceSelfAssessedTaxDistIntendedUse | INTENDED_USE | — | — |
| 56 | InvoiceSelfAssessedTaxDistInventoryTransferStatus | INVENTORY_TRANSFER_STATUS | — | — |
| 57 | InvoiceSelfAssessedTaxDistInvoiceLineNumber | INVOICE_LINE_NUMBER | — | — |
| 58 | InvoiceSelfAssessedTaxDistInvoiceSelfAssessedTaxDistParentReversalId | PARENT_REVERSAL_ID | — | — |
| 59 | InvoiceSelfAssessedTaxDistJustification | JUSTIFICATION | — | — |
| 60 | InvoiceSelfAssessedTaxDistLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 61 | InvoiceSelfAssessedTaxDistLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 62 | InvoiceSelfAssessedTaxDistLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 63 | InvoiceSelfAssessedTaxDistLineTypeLookupCode | LINE_TYPE_LOOKUP_CODE | — | ✅ |
| 64 | InvoiceSelfAssessedTaxDistMatchStatusFlag | MATCH_STATUS_FLAG | — | ✅ |
| 65 | InvoiceSelfAssessedTaxDistMatchedUomLookupCode | MATCHED_UOM_LOOKUP_CODE | — | — |
| 66 | InvoiceSelfAssessedTaxDistMerchantDocumentNumber | MERCHANT_DOCUMENT_NUMBER | — | — |
| 67 | InvoiceSelfAssessedTaxDistMerchantName | MERCHANT_NAME | — | — |
| 68 | InvoiceSelfAssessedTaxDistMerchantReference | MERCHANT_REFERENCE | — | — |
| 69 | InvoiceSelfAssessedTaxDistMerchantTaxRegNumber | MERCHANT_TAX_REG_NUMBER | — | — |
| 70 | InvoiceSelfAssessedTaxDistMerchantTaxpayerId | MERCHANT_TAXPAYER_ID | — | — |
| 71 | InvoiceSelfAssessedTaxDistObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 72 | InvoiceSelfAssessedTaxDistOrgId | ORG_ID | — | — |
| 73 | InvoiceSelfAssessedTaxDistPaAdditionFlag | PA_ADDITION_FLAG | — | — |
| 74 | InvoiceSelfAssessedTaxDistPaCmtXfaceFlag | PA_CMT_XFACE_FLAG | — | — |
| 75 | InvoiceSelfAssessedTaxDistPaQuantity | PA_QUANTITY | — | — |
| 76 | InvoiceSelfAssessedTaxDistPacketId | PACKET_ID | — | — |
| 77 | InvoiceSelfAssessedTaxDistParentInvoiceId | PARENT_INVOICE_ID | — | — |
| 78 | InvoiceSelfAssessedTaxDistPeriodName | PERIOD_NAME | — | ✅ |
| 79 | InvoiceSelfAssessedTaxDistPoDistributionId | PO_DISTRIBUTION_ID | — | — |
| 80 | InvoiceSelfAssessedTaxDistPostedFlag | POSTED_FLAG | — | ✅ |
| 81 | InvoiceSelfAssessedTaxDistPrepayAmountRemaining | PREPAY_AMOUNT_REMAINING | — | — |
| 82 | InvoiceSelfAssessedTaxDistPrepayDistributionId | PREPAY_DISTRIBUTION_ID | — | — |
| 83 | InvoiceSelfAssessedTaxDistPrepayTaxDiffAmount | PREPAY_TAX_DIFF_AMOUNT | — | — |
| 84 | InvoiceSelfAssessedTaxDistProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 85 | InvoiceSelfAssessedTaxDistProgramId | PROGRAM_ID | — | — |
| 86 | InvoiceSelfAssessedTaxDistProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 87 | InvoiceSelfAssessedTaxDistProjectId | PROJECT_ID | — | — |
| 88 | InvoiceSelfAssessedTaxDistQuantityInvoiced | QUANTITY_INVOICED | — | — |
| 89 | InvoiceSelfAssessedTaxDistQuantityVariance | QUANTITY_VARIANCE | — | — |
| 90 | InvoiceSelfAssessedTaxDistRcvChargeAdditionFlag | RCV_CHARGE_ADDITION_FLAG | — | — |
| 91 | InvoiceSelfAssessedTaxDistRcvTransactionId | RCV_TRANSACTION_ID | — | — |
| 92 | InvoiceSelfAssessedTaxDistRecNrecRate | REC_NREC_RATE | — | — |
| 93 | InvoiceSelfAssessedTaxDistReceiptConversionRate | RECEIPT_CONVERSION_RATE | — | — |
| 94 | InvoiceSelfAssessedTaxDistReceiptCurrencyAmount | RECEIPT_CURRENCY_AMOUNT | — | — |
| 95 | InvoiceSelfAssessedTaxDistReceiptMissingFlag | RECEIPT_MISSING_FLAG | — | — |
| 96 | InvoiceSelfAssessedTaxDistReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 97 | InvoiceSelfAssessedTaxDistReceiptVerifiedFlag | RECEIPT_VERIFIED_FLAG | — | — |
| 98 | InvoiceSelfAssessedTaxDistRecoveryRateId | RECOVERY_RATE_ID | — | — |
| 99 | InvoiceSelfAssessedTaxDistRecoveryRateName | RECOVERY_RATE_NAME | — | — |
| 100 | InvoiceSelfAssessedTaxDistRecoveryTypeCode | RECOVERY_TYPE_CODE | — | ✅ |
| 101 | InvoiceSelfAssessedTaxDistReference1 | REFERENCE_1 | — | — |
| 102 | InvoiceSelfAssessedTaxDistReference2 | REFERENCE_2 | — | — |
| 103 | InvoiceSelfAssessedTaxDistRelatedId | RELATED_ID | — | — |
| 104 | InvoiceSelfAssessedTaxDistRequestId | REQUEST_ID | — | — |
| 105 | InvoiceSelfAssessedTaxDistReversalFlag | REVERSAL_FLAG | — | ✅ |
| 106 | InvoiceSelfAssessedTaxDistRoundingAmt | ROUNDING_AMT | — | — |
| 107 | InvoiceSelfAssessedTaxDistSelfAssessedFlag | SELF_ASSESSED_FLAG | — | — |
| 108 | InvoiceSelfAssessedTaxDistSelfAssessedTaxLiabCcid | SELF_ASSESSED_TAX_LIAB_CCID | — | — |
| 109 | InvoiceSelfAssessedTaxDistSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 110 | InvoiceSelfAssessedTaxDistStartExpenseDate | START_EXPENSE_DATE | — | — |
| 111 | InvoiceSelfAssessedTaxDistStatAmount | STAT_AMOUNT | — | — |
| 112 | InvoiceSelfAssessedTaxDistSummaryTaxLineId | SUMMARY_TAX_LINE_ID | — | — |
| 113 | InvoiceSelfAssessedTaxDistTaskId | TASK_ID | — | — |
| 114 | InvoiceSelfAssessedTaxDistTaxAlreadyDistributedFlag | TAX_ALREADY_DISTRIBUTED_FLAG | — | — |
| 115 | InvoiceSelfAssessedTaxDistTaxCodeId | TAX_CODE_ID | — | — |
| 116 | InvoiceSelfAssessedTaxDistTaxRecoverableFlag | TAX_RECOVERABLE_FLAG | — | — |
| 117 | InvoiceSelfAssessedTaxDistTaxableAmount | TAXABLE_AMOUNT | — | — |
| 118 | InvoiceSelfAssessedTaxDistTaxableBaseAmount | TAXABLE_BASE_AMOUNT | — | — |
| 119 | InvoiceSelfAssessedTaxDistType1099 | TYPE_1099 | — | — |
| 120 | InvoiceSelfAssessedTaxDistUnitPrice | UNIT_PRICE | — | — |
| 121 | InvoiceSelfAssessedTaxDistUpgradeBasePostedAmt | UPGRADE_BASE_POSTED_AMT | — | — |
| 122 | InvoiceSelfAssessedTaxDistUpgradePostedAmt | UPGRADE_POSTED_AMT | — | — |
| 123 | InvoiceSelfAssessedTaxDistUssglTransactionCode | USSGL_TRANSACTION_CODE | — | — |
| 124 | InvoiceSelfAssessedTaxDistUssglTrxCodeContext | USSGL_TRX_CODE_CONTEXT | — | — |
| 125 | InvoiceSelfAssessedTaxDistWebParameterId | WEB_PARAMETER_ID | — | — |
| 126 | InvoiceSelfAssessedTaxDistWithholdingTaxCodeId | WITHHOLDING_TAX_CODE_ID | — | — |

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitBusinessUnitId | BU_ID | — | — |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 2 | LedgersCurrencyCode | CURRENCY_CODE | — | — |
| 3 | LedgersLedgerId | LEDGER_ID | — | — |
| 4 | LedgersObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[zx_lines|ZX_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DetailTaxLinePEOCancelFlag | CANCEL_FLAG | — | — |
| 2 | DetailTaxLinePEOIncludedFlag | TAX_ONLY_LINE_FLAG | — | — |
| 3 | DetailTaxLinePEOJurisdictionCode | TAX_JURISDICTION_CODE | — | — |
| 4 | DetailTaxLinePEOJurisdictionId | TAX_JURISDICTION_ID | — | — |
| 5 | DetailTaxLinePEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 6 | DetailTaxLinePEOReportingCurrencyCode | REPORTING_CURRENCY_CODE | — | — |
| 7 | DetailTaxLinePEOSelfAssessedFlag | SELF_ASSESSED_FLAG | — | — |
| 8 | DetailTaxLinePEOTaxAmtFunclCurr | TAX_AMT_FUNCL_CURR | — | — |
| 9 | DetailTaxLinePEOTaxCurrencyCode | TAX_CURRENCY_CODE | — | — |
| 10 | DetailTaxLinePEOTaxId | TAX_ID | — | — |
| 11 | DetailTaxLinePEOTaxLineId | TAX_LINE_ID | — | — |
| 12 | DetailTaxLinePEOTaxRate | TAX_RATE | — | — |
| 13 | DetailTaxLinePEOTaxRateCode | TAX_RATE_CODE | — | — |
| 14 | DetailTaxLinePEOTaxRateId | TAX_RATE_ID | — | — |
| 15 | DetailTaxLinePEOTaxRegimeCode | TAX_REGIME_CODE | — | — |
| 16 | DetailTaxLinePEOTaxRegimeId | TAX_REGIME_ID | — | — |
| 17 | DetailTaxLinePEOTaxStatusId | TAX_STATUS_ID | — | — |
| 18 | DetailTaxLinePEOTaxonlyLineFlag | TAX_ONLY_LINE_FLAG | — | — |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
