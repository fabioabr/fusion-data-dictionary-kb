---
id: DOC-OTHER-PVO-SysParameterExtractPVO
doc_type: system-doc
title: "SysParameterExtractPVO — PVO Cross-Module"
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
  - SysParameterExtractPVO
  - sysparameterextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SysParameterExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Sys Parameter Extract. Acessa as tabelas: AR_SYSTEM_PARAMETERS_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.SysParameterExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 203 | 1 | 1 | 151 | 74% |

---

## 🔗 Tabelas Relacionadas

- [[ar_system_parameters_all|AR_SYSTEM_PARAMETERS_ALL]] — 203 atributos (1 PKs, 151 BICC)

---

## ⚙️ Atributos

### [[ar_system_parameters_all|AR_SYSTEM_PARAMETERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArSystemParameterAccountingMethod | ACCOUNTING_METHOD | — | ✅ |
| 2 | ArSystemParameterAccrueInterest | ACCRUE_INTEREST | — | ✅ |
| 3 | ArSystemParameterAcctDatesOutOfOrder | ACCT_DATES_OUT_OF_ORDER | — | ✅ |
| 4 | ArSystemParameterAddressValidation | ADDRESS_VALIDATION | — | ✅ |
| 5 | ArSystemParameterAiAcctFlexKeyLeftPrompt | AI_ACCT_FLEX_KEY_LEFT_PROMPT | — | ✅ |
| 6 | ArSystemParameterAiActivateSqlTraceFlag | AI_ACTIVATE_SQL_TRACE_FLAG | — | ✅ |
| 7 | ArSystemParameterAiLogFileMessageLevel | AI_LOG_FILE_MESSAGE_LEVEL | — | ✅ |
| 8 | ArSystemParameterAiMaxMemoryInBytes | AI_MAX_MEMORY_IN_BYTES | — | ✅ |
| 9 | ArSystemParameterAiMtlItemsKeyLeftPrompt | AI_MTL_ITEMS_KEY_LEFT_PROMPT | — | ✅ |
| 10 | ArSystemParameterAiPurgeInterfaceTablesFlag | AI_PURGE_INTERFACE_TABLES_FLAG | — | ✅ |
| 11 | ArSystemParameterAiTerritoryKeyLeftPrompt | AI_TERRITORY_KEY_LEFT_PROMPT | — | ✅ |
| 12 | ArSystemParameterAllowLateCharges | ALLOW_LATE_CHARGES | — | ✅ |
| 13 | ArSystemParameterAllowPaymentDeletionFlag | ALLOW_PAYMENT_DELETION_FLAG | — | ✅ |
| 14 | ArSystemParameterAttribute1 | ATTRIBUTE1 | — | — |
| 15 | ArSystemParameterAttribute10 | ATTRIBUTE10 | — | — |
| 16 | ArSystemParameterAttribute11 | ATTRIBUTE11 | — | — |
| 17 | ArSystemParameterAttribute12 | ATTRIBUTE12 | — | — |
| 18 | ArSystemParameterAttribute13 | ATTRIBUTE13 | — | — |
| 19 | ArSystemParameterAttribute14 | ATTRIBUTE14 | — | — |
| 20 | ArSystemParameterAttribute15 | ATTRIBUTE15 | — | — |
| 21 | ArSystemParameterAttribute2 | ATTRIBUTE2 | — | — |
| 22 | ArSystemParameterAttribute3 | ATTRIBUTE3 | — | — |
| 23 | ArSystemParameterAttribute4 | ATTRIBUTE4 | — | — |
| 24 | ArSystemParameterAttribute5 | ATTRIBUTE5 | — | — |
| 25 | ArSystemParameterAttribute6 | ATTRIBUTE6 | — | — |
| 26 | ArSystemParameterAttribute7 | ATTRIBUTE7 | — | — |
| 27 | ArSystemParameterAttribute8 | ATTRIBUTE8 | — | — |
| 28 | ArSystemParameterAttribute9 | ATTRIBUTE9 | — | — |
| 29 | ArSystemParameterAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 30 | ArSystemParameterAutoRecInvoicesPerCommit | AUTO_REC_INVOICES_PER_COMMIT | — | ✅ |
| 31 | ArSystemParameterAutoRecReceiptsPerCommit | AUTO_REC_RECEIPTS_PER_COMMIT | — | ✅ |
| 32 | ArSystemParameterAutoSiteNumbering | AUTO_SITE_NUMBERING | — | ✅ |
| 33 | ArSystemParameterAutoapplyFlag | AUTOAPPLY_FLAG | — | ✅ |
| 34 | ArSystemParameterAutocashHierarchyId | AUTOCASH_HIERARCHY_ID | — | ✅ |
| 35 | ArSystemParameterAutomatchRerunDays | AUTOMATCH_RERUN_DAYS | — | ✅ |
| 36 | ArSystemParameterAutomatchRuleId | AUTOMATCH_RULE_ID | — | ✅ |
| 37 | ArSystemParameterBaRemitBankAcctUseId | BA_REMIT_BANK_ACCT_USE_ID | — | ✅ |
| 38 | ArSystemParameterBillsReceivableEnabledFlag | BILLS_RECEIVABLE_ENABLED_FLAG | — | ✅ |
| 39 | ArSystemParameterBrDefaultBatchsourceSeqId | BR_DEFAULT_BATCHSOURCE_SEQ_ID | — | ✅ |
| 40 | ArSystemParameterBrRemitWithoutRecourseFlag | BR_REMIT_WITHOUT_RECOURSE_FLAG | — | ✅ |
| 41 | ArSystemParameterCalcDiscountOnLinesFlag | CALC_DISCOUNT_ON_LINES_FLAG | — | ✅ |
| 42 | ArSystemParameterCalcTaxOnCreditMemoFlag | CALC_TAX_ON_CREDIT_MEMO_FLAG | — | ✅ |
| 43 | ArSystemParameterCashBasisSetOfBooksId | CASH_BASIS_SET_OF_BOOKS_ID | — | ✅ |
| 44 | ArSystemParameterCcRemitBankAcctUseId | CC_REMIT_BANK_ACCT_USE_ID | — | ✅ |
| 45 | ArSystemParameterCerDsoDays | CER_DSO_DAYS | — | ✅ |
| 46 | ArSystemParameterCerSplitAmount | CER_SPLIT_AMOUNT | — | ✅ |
| 47 | ArSystemParameterChangePrintedInvoiceFlag | CHANGE_PRINTED_INVOICE_FLAG | — | ✅ |
| 48 | ArSystemParameterCodeCombinationIdGain | CODE_COMBINATION_ID_GAIN | — | ✅ |
| 49 | ArSystemParameterCodeCombinationIdLoss | CODE_COMBINATION_ID_LOSS | — | ✅ |
| 50 | ArSystemParameterCodeCombinationIdRound | CODE_COMBINATION_ID_ROUND | — | ✅ |
| 51 | ArSystemParameterConfirmThresholdAmt | CONFIRM_THRESHOLD_AMT | — | ✅ |
| 52 | ArSystemParameterCreateDetailedDist | CREATE_DETAILED_DIST | — | ✅ |
| 53 | ArSystemParameterCreateReciprocalFlag | CREATE_RECIPROCAL_FLAG | — | ✅ |
| 54 | ArSystemParameterCreatedBy | CREATED_BY | — | ✅ |
| 55 | ArSystemParameterCreationDate | CREATION_DATE | — | ✅ |
| 56 | ArSystemParameterCreditClassification1 | CREDIT_CLASSIFICATION1 | — | ✅ |
| 57 | ArSystemParameterCreditClassification2 | CREDIT_CLASSIFICATION2 | — | ✅ |
| 58 | ArSystemParameterCreditClassification3 | CREDIT_CLASSIFICATION3 | — | ✅ |
| 59 | ArSystemParameterCrossCurrencyRateType | CROSS_CURRENCY_RATE_TYPE | — | ✅ |
| 60 | ArSystemParameterDefaultCbDueDate | DEFAULT_CB_DUE_DATE | — | ✅ |
| 61 | ArSystemParameterDefaultCountry | DEFAULT_COUNTRY | — | ✅ |
| 62 | ArSystemParameterDefaultGroupingRuleId | DEFAULT_GROUPING_RULE_ID | — | ✅ |
| 63 | ArSystemParameterDefaultTerritory | DEFAULT_TERRITORY | — | ✅ |
| 64 | ArSystemParameterDocumentSeqGenLevel | DOCUMENT_SEQ_GEN_LEVEL | — | ✅ |
| 65 | ArSystemParameterEmailBody | EMAIL_BODY | — | ✅ |
| 66 | ArSystemParameterEmailSubject | EMAIL_SUBJECT | — | ✅ |
| 67 | ArSystemParameterEnableRecurringBillingFlag | ENABLE_RECURRING_BILLING_FLAG | — | ✅ |
| 68 | ArSystemParameterExceptionAdjReasonCode | EXCEPTION_ADJ_REASON_CODE | — | ✅ |
| 69 | ArSystemParameterExceptionAdjRecTrxId | EXCEPTION_ADJ_REC_TRX_ID | — | ✅ |
| 70 | ArSystemParameterExceptionPmtMethodCode | EXCEPTION_PMT_METHOD_CODE | — | ✅ |
| 71 | ArSystemParameterExceptionRuleId | EXCEPTION_RULE_ID | — | ✅ |
| 72 | ArSystemParameterExceptionWrtoffRecTrxId | EXCEPTION_WRTOFF_REC_TRX_ID | — | ✅ |
| 73 | ArSystemParameterFinchrgReceivablesTrxId | FINCHRG_RECEIVABLES_TRX_ID | — | ✅ |
| 74 | ArSystemParameterFromEmailAddress | FROM_EMAIL_ADDRESS | — | ✅ |
| 75 | ArSystemParameterFromEmailName | FROM_EMAIL_NAME | — | ✅ |
| 76 | ArSystemParameterFromPostalCode | FROM_POSTAL_CODE | — | ✅ |
| 77 | ArSystemParameterGenerateCustomerNumber | GENERATE_CUSTOMER_NUMBER | — | ✅ |
| 78 | ArSystemParameterGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 79 | ArSystemParameterGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 80 | ArSystemParameterGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 81 | ArSystemParameterGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 82 | ArSystemParameterGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 83 | ArSystemParameterGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 84 | ArSystemParameterGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 85 | ArSystemParameterGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 86 | ArSystemParameterGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 87 | ArSystemParameterGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 88 | ArSystemParameterGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 89 | ArSystemParameterGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 90 | ArSystemParameterGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 91 | ArSystemParameterGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 92 | ArSystemParameterGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 93 | ArSystemParameterGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 94 | ArSystemParameterGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 95 | ArSystemParameterGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 96 | ArSystemParameterGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 97 | ArSystemParameterGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 98 | ArSystemParameterGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 99 | ArSystemParameterGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 100 | ArSystemParameterGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 101 | ArSystemParameterGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 102 | ArSystemParameterGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 103 | ArSystemParameterGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 104 | ArSystemParameterGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 105 | ArSystemParameterGlobalAttributeNumber10 | GLOBAL_ATTRIBUTE_NUMBER10 | — | — |
| 106 | ArSystemParameterGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 107 | ArSystemParameterGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 108 | ArSystemParameterGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 109 | ArSystemParameterGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 110 | ArSystemParameterGlobalAttributeNumber6 | GLOBAL_ATTRIBUTE_NUMBER6 | — | — |
| 111 | ArSystemParameterGlobalAttributeNumber7 | GLOBAL_ATTRIBUTE_NUMBER7 | — | — |
| 112 | ArSystemParameterGlobalAttributeNumber8 | GLOBAL_ATTRIBUTE_NUMBER8 | — | — |
| 113 | ArSystemParameterGlobalAttributeNumber9 | GLOBAL_ATTRIBUTE_NUMBER9 | — | — |
| 114 | ArSystemParameterIncludeBuSubjectCode | INCLUDE_BU_SUBJECT_CODE | — | ✅ |
| 115 | ArSystemParameterIncludeStmtBuSubCode | INCLUDE_STMT_BU_SUB_CODE | — | ✅ |
| 116 | ArSystemParameterIncludeStmtDateSubCode | INCLUDE_STMT_DATE_SUB_CODE | — | ✅ |
| 117 | ArSystemParameterIncludeTrxnumSubjectCode | INCLUDE_TRXNUM_SUBJECT_CODE | — | ✅ |
| 118 | ArSystemParameterInclusiveTaxUsed | INCLUSIVE_TAX_USED | — | ✅ |
| 119 | ArSystemParameterInvoiceDeletionFlag | INVOICE_DELETION_FLAG | — | ✅ |
| 120 | ArSystemParameterIrecBaReceiptMethodId | IREC_BA_RECEIPT_METHOD_ID | — | ✅ |
| 121 | ArSystemParameterIrecCcReceiptMethodId | IREC_CC_RECEIPT_METHOD_ID | — | ✅ |
| 122 | ArSystemParameterIrecServiceChargeRecTrxId | IREC_SERVICE_CHARGE_REC_TRX_ID | — | ✅ |
| 123 | ArSystemParameterItemValidationOrgId | ITEM_VALIDATION_ORG_ID | — | ✅ |
| 124 | ArSystemParameterLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 125 | ArSystemParameterLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 126 | ArSystemParameterLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 127 | ArSystemParameterLateChargeBatSourceSeqId | LATE_CHARGE_BAT_SOURCE_SEQ_ID | — | ✅ |
| 128 | ArSystemParameterLateChargeBillingCalcMode | LATE_CHARGE_BILLING_CALC_MODE | — | ✅ |
| 129 | ArSystemParameterLateChargeDmTypeSeqId | LATE_CHARGE_DM_TYPE_SEQ_ID | — | ✅ |
| 130 | ArSystemParameterLateChargeInvTypeSeqId | LATE_CHARGE_INV_TYPE_SEQ_ID | — | ✅ |
| 131 | ArSystemParameterLocationStructureId | LOCATION_STRUCTURE_ID | — | ✅ |
| 132 | ArSystemParameterLocationTaxAccount | LOCATION_TAX_ACCOUNT | — | ✅ |
| 133 | ArSystemParameterLockboxMatchingOption1 | LOCKBOX_MATCHING_OPTION1 | — | ✅ |
| 134 | ArSystemParameterLockboxMatchingOption2 | LOCKBOX_MATCHING_OPTION2 | — | ✅ |
| 135 | ArSystemParameterLockboxMatchingOption3 | LOCKBOX_MATCHING_OPTION3 | — | ✅ |
| 136 | ArSystemParameterLockboxMatchingOption4 | LOCKBOX_MATCHING_OPTION4 | — | ✅ |
| 137 | ArSystemParameterMatchedClaimCreationFlag | MATCHED_CLAIM_CREATION_FLAG | — | ✅ |
| 138 | ArSystemParameterMatchedClaimExclCmFlag | MATCHED_CLAIM_EXCL_CM_FLAG | — | ✅ |
| 139 | ArSystemParameterMaxWrtoffAmount | MAX_WRTOFF_AMOUNT | — | ✅ |
| 140 | ArSystemParameterMinRefundAmount | MIN_REFUND_AMOUNT | — | ✅ |
| 141 | ArSystemParameterMinWrtoffAmount | MIN_WRTOFF_AMOUNT | — | ✅ |
| 142 | ArSystemParameterObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 143 | ArSystemParameterOrgId | ORG_ID | 🔑 | ✅ |
| 144 | ArSystemParameterPartialDiscountFlag | PARTIAL_DISCOUNT_FLAG | — | ✅ |
| 145 | ArSystemParameterPayUnrelatedInvoicesFlag | PAY_UNRELATED_INVOICES_FLAG | — | ✅ |
| 146 | ArSystemParameterPaymentApplicationRule | PAYMENT_APPLICATION_RULE | — | ✅ |
| 147 | ArSystemParameterPaymentThreshold | PAYMENT_THRESHOLD | — | ✅ |
| 148 | ArSystemParameterPenaltyRecTrxId | PENALTY_REC_TRX_ID | — | ✅ |
| 149 | ArSystemParameterPopulateGlSegmentsFlag | POPULATE_GL_SEGMENTS_FLAG | — | ✅ |
| 150 | ArSystemParameterPostBillingItemInclusion | POST_BILLING_ITEM_INCLUSION | — | ✅ |
| 151 | ArSystemParameterPostingDaysPerCycle | POSTING_DAYS_PER_CYCLE | — | ✅ |
| 152 | ArSystemParameterPrintHomeCountryFlag | PRINT_HOME_COUNTRY_FLAG | — | ✅ |
| 153 | ArSystemParameterPrintRemitTo | PRINT_REMIT_TO | — | ✅ |
| 154 | ArSystemParameterReplyToEmailAddress | REPLY_TO_EMAIL_ADDRESS | — | ✅ |
| 155 | ArSystemParameterRevTransferClearCcid | REV_TRANSFER_CLEAR_CCID | — | ✅ |
| 156 | ArSystemParameterRuleSetId | RULE_SET_ID | — | ✅ |
| 157 | ArSystemParameterRunGlJournalImportFlag | RUN_GL_JOURNAL_IMPORT_FLAG | — | ✅ |
| 158 | ArSystemParameterSalesCreditPctLimit | SALES_CREDIT_PCT_LIMIT | — | ✅ |
| 159 | ArSystemParameterSalesTaxGeocode | SALES_TAX_GEOCODE | — | ✅ |
| 160 | ArSystemParameterSalesrepRequiredFlag | SALESREP_REQUIRED_FLAG | — | ✅ |
| 161 | ArSystemParameterServicedByAnyBuFlag | SERVICED_BY_ANY_BU_FLAG | — | ✅ |
| 162 | ArSystemParameterSetOfBooksId | SET_OF_BOOKS_ID | — | ✅ |
| 163 | ArSystemParameterShowBillingNumberFlag | SHOW_BILLING_NUMBER_FLAG | — | ✅ |
| 164 | ArSystemParameterSiteRequiredFlag | SITE_REQUIRED_FLAG | — | ✅ |
| 165 | ArSystemParameterStandardRefund | STANDARD_REFUND | — | ✅ |
| 166 | ArSystemParameterStmtEmailBody | STMT_EMAIL_BODY | — | ✅ |
| 167 | ArSystemParameterStmtEmailSubject | STMT_EMAIL_SUBJECT | — | ✅ |
| 168 | ArSystemParameterStmtFromEmailAddress | STMT_FROM_EMAIL_ADDRESS | — | ✅ |
| 169 | ArSystemParameterStmtFromEmailName | STMT_FROM_EMAIL_NAME | — | ✅ |
| 170 | ArSystemParameterStmtReplyToEmailAddress | STMT_REPLY_TO_EMAIL_ADDRESS | — | ✅ |
| 171 | ArSystemParameterTaInstalledFlag | TA_INSTALLED_FLAG | — | ✅ |
| 172 | ArSystemParameterTaxAllowCompoundFlag | TAX_ALLOW_COMPOUND_FLAG | — | ✅ |
| 173 | ArSystemParameterTaxCache | TAX_CACHE | — | ✅ |
| 174 | ArSystemParameterTaxCode | TAX_CODE | — | ✅ |
| 175 | ArSystemParameterTaxCurrencyCode | TAX_CURRENCY_CODE | — | ✅ |
| 176 | ArSystemParameterTaxDatabaseViewSet | TAX_DATABASE_VIEW_SET | — | ✅ |
| 177 | ArSystemParameterTaxEnforceAccountFlag | TAX_ENFORCE_ACCOUNT_FLAG | — | ✅ |
| 178 | ArSystemParameterTaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | ✅ |
| 179 | ArSystemParameterTaxHierAccountExcRate | TAX_HIER_ACCOUNT_EXC_RATE | — | ✅ |
| 180 | ArSystemParameterTaxHierCustExcRate | TAX_HIER_CUST_EXC_RATE | — | ✅ |
| 181 | ArSystemParameterTaxHierProdExcRate | TAX_HIER_PROD_EXC_RATE | — | ✅ |
| 182 | ArSystemParameterTaxHierSiteExcRate | TAX_HIER_SITE_EXC_RATE | — | ✅ |
| 183 | ArSystemParameterTaxHierSystemExcRate | TAX_HIER_SYSTEM_EXC_RATE | — | ✅ |
| 184 | ArSystemParameterTaxInvoicePrint | TAX_INVOICE_PRINT | — | ✅ |
| 185 | ArSystemParameterTaxMethod | TAX_METHOD | — | ✅ |
| 186 | ArSystemParameterTaxMinimumAccountableUnit | TAX_MINIMUM_ACCOUNTABLE_UNIT | — | ✅ |
| 187 | ArSystemParameterTaxPrecision | TAX_PRECISION | — | ✅ |
| 188 | ArSystemParameterTaxRegistrationNumber | TAX_REGISTRATION_NUMBER | — | ✅ |
| 189 | ArSystemParameterTaxRoundingAllowOverride | TAX_ROUNDING_ALLOW_OVERRIDE | — | ✅ |
| 190 | ArSystemParameterTaxRoundingRule | TAX_ROUNDING_RULE | — | ✅ |
| 191 | ArSystemParameterTaxUseAccountExcRateFlag | TAX_USE_ACCOUNT_EXC_RATE_FLAG | — | ✅ |
| 192 | ArSystemParameterTaxUseCustExcRateFlag | TAX_USE_CUST_EXC_RATE_FLAG | — | ✅ |
| 193 | ArSystemParameterTaxUseCustomerExemptFlag | TAX_USE_CUSTOMER_EXEMPT_FLAG | — | ✅ |
| 194 | ArSystemParameterTaxUseLocExcRateFlag | TAX_USE_LOC_EXC_RATE_FLAG | — | ✅ |
| 195 | ArSystemParameterTaxUseProdExcRateFlag | TAX_USE_PROD_EXC_RATE_FLAG | — | ✅ |
| 196 | ArSystemParameterTaxUseProductExemptFlag | TAX_USE_PRODUCT_EXEMPT_FLAG | — | ✅ |
| 197 | ArSystemParameterTaxUseSiteExcRateFlag | TAX_USE_SITE_EXC_RATE_FLAG | — | ✅ |
| 198 | ArSystemParameterTaxUseSystemExcRateFlag | TAX_USE_SYSTEM_EXC_RATE_FLAG | — | ✅ |
| 199 | ArSystemParameterToPostalCode | TO_POSTAL_CODE | — | ✅ |
| 200 | ArSystemParameterTrxHeaderLevelRounding | TRX_HEADER_LEVEL_ROUNDING | — | ✅ |
| 201 | ArSystemParameterTrxHeaderRoundCcid | TRX_HEADER_ROUND_CCID | — | ✅ |
| 202 | ArSystemParameterUnallocatedRevenueCcid | UNALLOCATED_REVENUE_CCID | — | ✅ |
| 203 | ArSystemParameterUnearnedDiscount | UNEARNED_DISCOUNT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
