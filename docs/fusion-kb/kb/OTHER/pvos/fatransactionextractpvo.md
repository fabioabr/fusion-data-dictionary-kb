---
id: DOC-OTHER-PVO-FaTransactionExtractPVO
doc_type: system-doc
title: "FaTransactionExtractPVO — PVO Cross-Module"
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
  - FaTransactionExtractPVO
  - fatransactionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FaTransactionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fa Transaction Extract. Acessa as tabelas: FA_ADDITIONS_B, FA_BOOKS, FA_BOOK_CONTROLS (+3).

**Caminho:** `FscmTopModelAM.FinFaSharedUtilAM.FaTransactionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 348 | 6 | 1 | 33 | 9% |

---

## 🔗 Tabelas Relacionadas

- [[fa_additions_b|FA_ADDITIONS_B]] — 28 atributos (1 BICC)
- [[fa_books|FA_BOOKS]] — 137 atributos (1 BICC)
- [[fa_book_controls|FA_BOOK_CONTROLS]] — 4 atributos
- [[fa_trx_extract|FA_TRX_EXTRACT]] — 63 atributos (1 PKs, 30 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 3 atributos
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 113 atributos (1 BICC)

---

## ⚙️ Atributos

### [[fa_additions_b|FA_ADDITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ParentAdditionBaseAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 2 | ParentAdditionBaseAssetId | ASSET_ID | — | — |
| 3 | ParentAdditionBaseAssetKeyCcid | ASSET_KEY_CCID | — | — |
| 4 | ParentAdditionBaseAssetNumber | ASSET_NUMBER | — | — |
| 5 | ParentAdditionBaseAssetType | ASSET_TYPE | — | — |
| 6 | ParentAdditionBaseCommitment | COMMITMENT | — | — |
| 7 | ParentAdditionBaseContext | CONTEXT | — | — |
| 8 | ParentAdditionBaseCreatedBy | CREATED_BY | — | — |
| 9 | ParentAdditionBaseCreationDate | CREATION_DATE | — | — |
| 10 | ParentAdditionBaseCurrentUnits | CURRENT_UNITS | — | — |
| 11 | ParentAdditionBaseDistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | — |
| 12 | ParentAdditionBaseInUseFlag | IN_USE_FLAG | — | — |
| 13 | ParentAdditionBaseInventorial | INVENTORIAL | — | — |
| 14 | ParentAdditionBaseInvestmentLaw | INVESTMENT_LAW | — | — |
| 15 | ParentAdditionBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | ParentAdditionBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | ParentAdditionBaseLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | ParentAdditionBaseLeaseId | LEASE_ID | — | — |
| 19 | ParentAdditionBaseManufacturerName | MANUFACTURER_NAME | — | — |
| 20 | ParentAdditionBaseModelNumber | MODEL_NUMBER | — | — |
| 21 | ParentAdditionBaseNewUsed | NEW_USED | — | — |
| 22 | ParentAdditionBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | ParentAdditionBaseOwnedLeased | OWNED_LEASED | — | — |
| 24 | ParentAdditionBaseParentAssetId | PARENT_ASSET_ID | — | — |
| 25 | ParentAdditionBaseProperty12451250Code | PROPERTY_1245_1250_CODE | — | — |
| 26 | ParentAdditionBasePropertyTypeCode | PROPERTY_TYPE_CODE | — | — |
| 27 | ParentAdditionBaseSerialNumber | SERIAL_NUMBER | — | — |
| 28 | ParentAdditionBaseTagNumber | TAG_NUMBER | — | — |

### [[fa_books|FA_BOOKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GroupAssetBookAdjustedCapacity | ADJUSTED_CAPACITY | — | — |
| 2 | GroupAssetBookAdjustedCost | ADJUSTED_COST | — | — |
| 3 | GroupAssetBookAdjustedRecoverableCost | ADJUSTED_RECOVERABLE_COST | — | — |
| 4 | GroupAssetBookAllocateToFullyRetFlag | ALLOCATE_TO_FULLY_RET_FLAG | — | — |
| 5 | GroupAssetBookAllocateToFullyRsvFlag | ALLOCATE_TO_FULLY_RSV_FLAG | — | — |
| 6 | GroupAssetBookAllowedDeprnLimit | ALLOWED_DEPRN_LIMIT | — | — |
| 7 | GroupAssetBookAllowedDeprnLimitAmount | ALLOWED_DEPRN_LIMIT_AMOUNT | — | — |
| 8 | GroupAssetBookAnnualDeprnRoundingFlag | ANNUAL_DEPRN_ROUNDING_FLAG | — | — |
| 9 | GroupAssetBookAssetId | ASSET_ID | — | — |
| 10 | GroupAssetBookBonusRuleId | BONUS_RULE_ID | — | — |
| 11 | GroupAssetBookBookTypeCode | BOOK_TYPE_CODE | — | — |
| 12 | GroupAssetBookCapitalizeFlag | CAPITALIZE_FLAG | — | — |
| 13 | GroupAssetBookCashGeneratingUnitId | CASH_GENERATING_UNIT_ID | — | — |
| 14 | GroupAssetBookCeilingTypeId | CEILING_TYPE_ID | — | — |
| 15 | GroupAssetBookCipCost | CIP_COST | — | — |
| 16 | GroupAssetBookContractId | CONTRACT_ID | — | — |
| 17 | GroupAssetBookConventionTypeId | CONVENTION_TYPE_ID | — | — |
| 18 | GroupAssetBookConversionDate | CONVERSION_DATE | — | — |
| 19 | GroupAssetBookCost | COST | — | — |
| 20 | GroupAssetBookCreatedBy | CREATED_BY | — | — |
| 21 | GroupAssetBookCreationDate | CREATION_DATE | — | — |
| 22 | GroupAssetBookDateEffective | DATE_EFFECTIVE | — | — |
| 23 | GroupAssetBookDateIneffective | DATE_INEFFECTIVE | — | — |
| 24 | GroupAssetBookDatePlacedInService | DATE_PLACED_IN_SERVICE | — | — |
| 25 | GroupAssetBookDepreciateFlag | DEPRECIATE_FLAG | — | — |
| 26 | GroupAssetBookDepreciationOption | DEPRECIATION_OPTION | — | — |
| 27 | GroupAssetBookDeprnLimitType | DEPRN_LIMIT_TYPE | — | — |
| 28 | GroupAssetBookDeprnStartDate | DEPRN_START_DATE | — | — |
| 29 | GroupAssetBookDisabledFlag | DISABLED_FLAG | — | — |
| 30 | GroupAssetBookDryHoleFlag | DRY_HOLE_FLAG | — | — |
| 31 | GroupAssetBookEofyAdjCost | EOFY_ADJ_COST | — | — |
| 32 | GroupAssetBookEofyFormulaFactor | EOFY_FORMULA_FACTOR | — | — |
| 33 | GroupAssetBookEofyReserve | EOFY_RESERVE | — | — |
| 34 | GroupAssetBookEopAdjCost | EOP_ADJ_COST | — | — |
| 35 | GroupAssetBookEopFormulaFactor | EOP_FORMULA_FACTOR | — | — |
| 36 | GroupAssetBookExcessAllocationOption | EXCESS_ALLOCATION_OPTION | — | — |
| 37 | GroupAssetBookExcludeFullyRsvFlag | EXCLUDE_FULLY_RSV_FLAG | — | — |
| 38 | GroupAssetBookExcludeProceedsFromBasis | EXCLUDE_PROCEEDS_FROM_BASIS | — | — |
| 39 | GroupAssetBookExtendedDepreciationPeriod | EXTENDED_DEPRECIATION_PERIOD | — | — |
| 40 | GroupAssetBookExtendedDeprnFlag | EXTENDED_DEPRN_FLAG | — | — |
| 41 | GroupAssetBookFairMarketValue | FAIR_MARKET_VALUE | — | — |
| 42 | GroupAssetBookFlatRateId | FLAT_RATE_ID | — | — |
| 43 | GroupAssetBookFormulaFactor | FORMULA_FACTOR | — | — |
| 44 | GroupAssetBookFullyRsvdRevalsCounter | FULLY_RSVD_REVALS_COUNTER | — | — |
| 45 | GroupAssetBookGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 46 | GroupAssetBookGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 47 | GroupAssetBookGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 48 | GroupAssetBookGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 49 | GroupAssetBookGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 50 | GroupAssetBookGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 51 | GroupAssetBookGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 52 | GroupAssetBookGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 53 | GroupAssetBookGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 54 | GroupAssetBookGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 55 | GroupAssetBookGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 56 | GroupAssetBookGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 57 | GroupAssetBookGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 58 | GroupAssetBookGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 59 | GroupAssetBookGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 60 | GroupAssetBookGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 61 | GroupAssetBookGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 62 | GroupAssetBookGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 63 | GroupAssetBookGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 64 | GroupAssetBookGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 65 | GroupAssetBookGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 66 | GroupAssetBookGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 67 | GroupAssetBookGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 68 | GroupAssetBookGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 69 | GroupAssetBookGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 70 | GroupAssetBookGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 71 | GroupAssetBookGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 72 | GroupAssetBookGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 73 | GroupAssetBookGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 74 | GroupAssetBookGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 75 | GroupAssetBookGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 76 | GroupAssetBookGroupAssetId | GROUP_ASSET_ID | — | — |
| 77 | GroupAssetBookItcAmount | ITC_AMOUNT | — | — |
| 78 | GroupAssetBookItcAmountId | ITC_AMOUNT_ID | — | — |
| 79 | GroupAssetBookItcBasis | ITC_BASIS | — | — |
| 80 | GroupAssetBookLastPriceIndexValue | LAST_PRICE_INDEX_VALUE | — | — |
| 81 | GroupAssetBookLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 82 | GroupAssetBookLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 83 | GroupAssetBookLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 84 | GroupAssetBookLimitProceedsFlag | LIMIT_PROCEEDS_FLAG | — | — |
| 85 | GroupAssetBookLtdCostOfRemoval | LTD_COST_OF_REMOVAL | — | — |
| 86 | GroupAssetBookLtdProceeds | LTD_PROCEEDS | — | — |
| 87 | GroupAssetBookMemberRollupFlag | MEMBER_ROLLUP_FLAG | — | — |
| 88 | GroupAssetBookMethodId | METHOD_ID | — | — |
| 89 | GroupAssetBookNbvAtSwitch | NBV_AT_SWITCH | — | — |
| 90 | GroupAssetBookObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 91 | GroupAssetBookOldAdjustedCapacity | OLD_ADJUSTED_CAPACITY | — | — |
| 92 | GroupAssetBookOldAdjustedCost | OLD_ADJUSTED_COST | — | — |
| 93 | GroupAssetBookOriginalCost | ORIGINAL_COST | — | — |
| 94 | GroupAssetBookOriginalDeprnStartDate | ORIGINAL_DEPRN_START_DATE | — | — |
| 95 | GroupAssetBookOverDepreciateOption | OVER_DEPRECIATE_OPTION | — | — |
| 96 | GroupAssetBookPercentSalvageValue | PERCENT_SALVAGE_VALUE | — | — |
| 97 | GroupAssetBookPeriodCounterCapitalized | PERIOD_COUNTER_CAPITALIZED | — | — |
| 98 | GroupAssetBookPeriodCounterExtended | PERIOD_COUNTER_EXTENDED | — | — |
| 99 | GroupAssetBookPeriodCounterFullyExtended | PERIOD_COUNTER_FULLY_EXTENDED | — | — |
| 100 | GroupAssetBookPeriodCounterFullyReserved | PERIOD_COUNTER_FULLY_RESERVED | — | — |
| 101 | GroupAssetBookPeriodCounterFullyRetired | PERIOD_COUNTER_FULLY_RETIRED | — | — |
| 102 | GroupAssetBookPeriodCounterLifeComplete | PERIOD_COUNTER_LIFE_COMPLETE | — | — |
| 103 | GroupAssetBookPriorDeprnLimit | PRIOR_DEPRN_LIMIT | — | — |
| 104 | GroupAssetBookPriorDeprnLimitAmount | PRIOR_DEPRN_LIMIT_AMOUNT | — | — |
| 105 | GroupAssetBookPriorDeprnLimitType | PRIOR_DEPRN_LIMIT_TYPE | — | — |
| 106 | GroupAssetBookPriorEofyReserve | PRIOR_EOFY_RESERVE | — | — |
| 107 | GroupAssetBookPriorFlatRateId | PRIOR_FLAT_RATE_ID | — | — |
| 108 | GroupAssetBookPriorMethodId | PRIOR_METHOD_ID | — | — |
| 109 | GroupAssetBookProductionCapacity | PRODUCTION_CAPACITY | — | — |
| 110 | GroupAssetBookProrateDate | PRORATE_DATE | — | — |
| 111 | GroupAssetBookRateAdjustmentFactor | RATE_ADJUSTMENT_FACTOR | — | — |
| 112 | GroupAssetBookRateInUse | RATE_IN_USE | — | — |
| 113 | GroupAssetBookRecaptureReserveFlag | RECAPTURE_RESERVE_FLAG | — | — |
| 114 | GroupAssetBookRecognizeGainLoss | RECOGNIZE_GAIN_LOSS | — | — |
| 115 | GroupAssetBookRecoverableCost | RECOVERABLE_COST | — | — |
| 116 | GroupAssetBookReduceAdditionFlag | REDUCE_ADDITION_FLAG | — | — |
| 117 | GroupAssetBookReduceAdjustmentFlag | REDUCE_ADJUSTMENT_FLAG | — | — |
| 118 | GroupAssetBookReduceRetirementFlag | REDUCE_RETIREMENT_FLAG | — | — |
| 119 | GroupAssetBookReductionRate | REDUCTION_RATE | — | — |
| 120 | GroupAssetBookRemainingLife1 | REMAINING_LIFE1 | — | — |
| 121 | GroupAssetBookRemainingLife2 | REMAINING_LIFE2 | — | — |
| 122 | GroupAssetBookRetirementDeprnOption | RETIREMENT_DEPRN_OPTION | — | — |
| 123 | GroupAssetBookRetirementId | RETIREMENT_ID | — | — |
| 124 | GroupAssetBookRevalAmortizationBasis | REVAL_AMORTIZATION_BASIS | — | — |
| 125 | GroupAssetBookRevalCeiling | REVAL_CEILING | — | — |
| 126 | GroupAssetBookSalvageType | SALVAGE_TYPE | — | — |
| 127 | GroupAssetBookSalvageValue | SALVAGE_VALUE | — | — |
| 128 | GroupAssetBookShortFiscalYearFlag | SHORT_FISCAL_YEAR_FLAG | — | — |
| 129 | GroupAssetBookTerminalGainLoss | TERMINAL_GAIN_LOSS | — | — |
| 130 | GroupAssetBookTerminalGainLossAmount | TERMINAL_GAIN_LOSS_AMOUNT | — | — |
| 131 | GroupAssetBookTerminalGainLossFlag | TERMINAL_GAIN_LOSS_FLAG | — | — |
| 132 | GroupAssetBookTrackingMethod | TRACKING_METHOD | — | — |
| 133 | GroupAssetBookTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | — |
| 134 | GroupAssetBookTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | — |
| 135 | GroupAssetBookUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 136 | GroupAssetBookUnrevaluedCost | UNREVALUED_COST | — | — |
| 137 | GroupAssetBookYtdProceeds | YTD_PROCEEDS | — | — |

### [[fa_book_controls|FA_BOOK_CONTROLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BookControlBookControlId | BOOK_CONTROL_ID | — | — |
| 2 | BookControlBookTypeCode | BOOK_TYPE_CODE | — | — |
| 3 | BookControlObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 4 | BookTypeName | BOOK_TYPE_NAME | — | — |

### [[fa_trx_extract|FA_TRX_EXTRACT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AHTransactionHeaderId | AH_TRANSACTION_HEADER_ID | — | — |
| 2 | FaTransactionExtractAdjustmentLineId | ADJUSTMENT_LINE_ID | — | — |
| 3 | FaTransactionExtractAdjustmentType | ADJUSTMENT_TYPE | — | ✅ |
| 4 | FaTransactionExtractAssetId | ASSET_ID | — | — |
| 5 | FaTransactionExtractAssetType | ASSET_TYPE | — | — |
| 6 | FaTransactionExtractBonusExpense | BONUS_EXPENSE | — | ✅ |
| 7 | FaTransactionExtractBonusReserve | BONUS_RESERVE | — | ✅ |
| 8 | FaTransactionExtractBookTypeCode | BOOK_TYPE_CODE | — | — |
| 9 | FaTransactionExtractBooksTransactionHeaderId | BOOKS_TRANSACTION_HEADER_ID | — | — |
| 10 | FaTransactionExtractCapitalizationFlag | CAPITALIZATION_FLAG | — | — |
| 11 | FaTransactionExtractCategoryBookDefaultId | CATEGORY_BOOK_DEFAULT_ID | — | — |
| 12 | FaTransactionExtractCategoryId | CATEGORY_ID | — | — |
| 13 | FaTransactionExtractCipCost | CIP_COST | — | ✅ |
| 14 | FaTransactionExtractCipCostClearing | CIP_COST_CLEARING | — | ✅ |
| 15 | FaTransactionExtractCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 16 | FaTransactionExtractCost | COST | — | ✅ |
| 17 | FaTransactionExtractCostClearing | COST_CLEARING | — | ✅ |
| 18 | FaTransactionExtractCostOfRemoval | COST_OF_REMOVAL | — | ✅ |
| 19 | FaTransactionExtractCreatedBy | CREATED_BY | — | — |
| 20 | FaTransactionExtractCreationDate | CREATION_DATE | — | — |
| 21 | FaTransactionExtractCurrencyCode | CURRENCY_CODE | — | ✅ |
| 22 | FaTransactionExtractDeprnOverrideFlag | DEPRN_OVERRIDE_FLAG | — | ✅ |
| 23 | FaTransactionExtractDistributionId | DISTRIBUTION_ID | — | ✅ |
| 24 | FaTransactionExtractEmployeeId | EMPLOYEE_ID | — | — |
| 25 | FaTransactionExtractExpense | EXPENSE | — | ✅ |
| 26 | FaTransactionExtractImpairmentExpense | IMPAIRMENT_EXPENSE | — | ✅ |
| 27 | FaTransactionExtractImpairmentId | IMPAIRMENT_ID | — | — |
| 28 | FaTransactionExtractImpairmentReserve | IMPAIRMENT_RESERVE | — | ✅ |
| 29 | FaTransactionExtractInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 30 | FaTransactionExtractInvoiceTransactionType | INVOICE_TRANSACTION_TYPE | — | — |
| 31 | FaTransactionExtractLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | FaTransactionExtractLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | FaTransactionExtractLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 34 | FaTransactionExtractLedgerId | LEDGER_ID | — | — |
| 35 | FaTransactionExtractLedgerSetId | LEDGER_SET_ID | — | — |
| 36 | FaTransactionExtractLocationId | LOCATION_ID | — | — |
| 37 | FaTransactionExtractNbvRetired | NBV_RETIRED | — | ✅ |
| 38 | FaTransactionExtractNewBooksTrxIdIn | NEW_BOOKS_TRX_ID_IN | — | — |
| 39 | FaTransactionExtractOldBooksTrxIdIn | OLD_BOOKS_TRX_ID_IN | — | — |
| 40 | FaTransactionExtractOriginalCost | ORIGINAL_COST | — | ✅ |
| 41 | FaTransactionExtractPeriodCounter | PERIOD_COUNTER | — | — |
| 42 | FaTransactionExtractPeriodName | PERIOD_NAME | — | — |
| 43 | FaTransactionExtractProceedsOfSale | PROCEEDS_OF_SALE | — | ✅ |
| 44 | FaTransactionExtractRecoverableCost | RECOVERABLE_COST | — | ✅ |
| 45 | FaTransactionExtractReserve | RESERVE | — | ✅ |
| 46 | FaTransactionExtractRetirementId | RETIREMENT_ID | — | — |
| 47 | FaTransactionExtractRetirementTrxId | RETIREMENT_TRX_ID | — | — |
| 48 | FaTransactionExtractRevalReserve | REVAL_RESERVE | — | ✅ |
| 49 | FaTransactionExtractSalvageValue | SALVAGE_VALUE | — | ✅ |
| 50 | FaTransactionExtractSourceDestCode | SOURCE_DEST_CODE | — | ✅ |
| 51 | FaTransactionExtractSourceDistributionType | SOURCE_DISTRIBUTION_TYPE | — | ✅ |
| 52 | FaTransactionExtractSourceLineId | SOURCE_LINE_ID | — | — |
| 53 | FaTransactionExtractSourceTable | SOURCE_TABLE | — | — |
| 54 | FaTransactionExtractSourceTypeCode | SOURCE_TYPE_CODE | — | ✅ |
| 55 | FaTransactionExtractTotalUnits | TOTAL_UNITS | — | — |
| 56 | FaTransactionExtractTrackMemberFlag | TRACK_MEMBER_FLAG | — | ✅ |
| 57 | FaTransactionExtractTransactionHeaderId | TRANSACTION_HEADER_ID | — | — |
| 58 | FaTransactionExtractTransactionKey | TRANSACTION_KEY | — | ✅ |
| 59 | FaTransactionExtractTransactionTypeCode | TRANSACTION_TYPE_CODE | — | ✅ |
| 60 | FaTransactionExtractUnitRatio | UNIT_RATIO | — | — |
| 61 | FaTransactionExtractUnitsAssigned | UNITS_ASSIGNED | — | ✅ |
| 62 | FaTransactionExtractUnplannedTrxId | UNPLANNED_TRX_ID | — | — |
| 63 | TrxExtractId | TRX_EXTRACT_ID | 🔑 | ✅ |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgerId | LEDGER_ID | — | — |
| 2 | LedgerPEOChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 3 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentPEOActionCode | ACTION_CODE | — | — |
| 2 | AssignmentPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 3 | AssignmentPEOAllowAsgOverrideFlag | ALLOW_ASG_OVERRIDE_FLAG | — | — |
| 4 | AssignmentPEOApplicantRank | APPLICANT_RANK | — | — |
| 5 | AssignmentPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 6 | AssignmentPEOAssignmentName | ASSIGNMENT_NAME | — | — |
| 7 | AssignmentPEOAssignmentNumber | ASSIGNMENT_NUMBER | — | — |
| 8 | AssignmentPEOAssignmentSequence | ASSIGNMENT_SEQUENCE | — | — |
| 9 | AssignmentPEOAssignmentStatusType | ASSIGNMENT_STATUS_TYPE | — | — |
| 10 | AssignmentPEOAssignmentStatusTypeId | ASSIGNMENT_STATUS_TYPE_ID | — | — |
| 11 | AssignmentPEOAssignmentType | ASSIGNMENT_TYPE | — | — |
| 12 | AssignmentPEOAutoEndFlag | AUTO_END_FLAG | — | — |
| 13 | AssignmentPEOBargainingUnitCode | BARGAINING_UNIT_CODE | — | — |
| 14 | AssignmentPEOBillingTitle | BILLING_TITLE | — | — |
| 15 | AssignmentPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 16 | AssignmentPEOBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 17 | AssignmentPEOCagrGradeDefId | CAGR_GRADE_DEF_ID | — | — |
| 18 | AssignmentPEOCagrIdFlexNum | CAGR_ID_FLEX_NUM | — | — |
| 19 | AssignmentPEOCollectiveAgreementId | COLLECTIVE_AGREEMENT_ID | — | — |
| 20 | AssignmentPEOContractId | CONTRACT_ID | — | — |
| 21 | AssignmentPEOCreatedBy | CREATED_BY | — | — |
| 22 | AssignmentPEOCreationDate | CREATION_DATE | — | — |
| 23 | AssignmentPEODateProbationEnd | DATE_PROBATION_END | — | — |
| 24 | AssignmentPEODefaultCodeCombId | DEFAULT_CODE_COMB_ID | — | — |
| 25 | AssignmentPEODutiesType | DUTIES_TYPE | — | — |
| 26 | AssignmentPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 27 | AssignmentPEOEffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 28 | AssignmentPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 29 | AssignmentPEOEffectiveLatestChange1 | EFFECTIVE_LATEST_CHANGE | — | — |
| 30 | AssignmentPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 31 | AssignmentPEOEffectiveSequence1 | EFFECTIVE_SEQUENCE | — | — |
| 32 | AssignmentPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 33 | AssignmentPEOEffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 34 | AssignmentPEOEmployeeCategory | EMPLOYEE_CATEGORY | — | — |
| 35 | AssignmentPEOEmploymentCategory | EMPLOYMENT_CATEGORY | — | — |
| 36 | AssignmentPEOEstablishmentId | ESTABLISHMENT_ID | — | — |
| 37 | AssignmentPEOExpenseCheckAddress | EXPENSE_CHECK_ADDRESS | — | — |
| 38 | AssignmentPEOFreezeStartDate | FREEZE_START_DATE | — | — |
| 39 | AssignmentPEOFreezeUntilDate | FREEZE_UNTIL_DATE | — | — |
| 40 | AssignmentPEOFrequency | FREQUENCY | — | — |
| 41 | AssignmentPEOFullPartTime | FULL_PART_TIME | — | — |
| 42 | AssignmentPEOGradeId | GRADE_ID | — | — |
| 43 | AssignmentPEOGradeLadderPgmId | GRADE_LADDER_PGM_ID | — | — |
| 44 | AssignmentPEOHourlySalariedCode | HOURLY_SALARIED_CODE | — | — |
| 45 | AssignmentPEOIdFlexNum | ID_FLEX_NUM | — | — |
| 46 | AssignmentPEOInternalBuilding | INTERNAL_BUILDING | — | — |
| 47 | AssignmentPEOInternalFloor | INTERNAL_FLOOR | — | — |
| 48 | AssignmentPEOInternalLocation | INTERNAL_LOCATION | — | — |
| 49 | AssignmentPEOInternalMailstop | INTERNAL_MAILSTOP | — | — |
| 50 | AssignmentPEOInternalOfficeNumber | INTERNAL_OFFICE_NUMBER | — | — |
| 51 | AssignmentPEOJobId | JOB_ID | — | — |
| 52 | AssignmentPEOJobPostSourceName | JOB_POST_SOURCE_NAME | — | — |
| 53 | AssignmentPEOLabourUnionMemberFlag | LABOUR_UNION_MEMBER_FLAG | — | — |
| 54 | AssignmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 55 | AssignmentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 56 | AssignmentPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 57 | AssignmentPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 58 | AssignmentPEOLegislationCode | LEGISLATION_CODE | — | — |
| 59 | AssignmentPEOLinkageType | LINKAGE_TYPE | — | — |
| 60 | AssignmentPEOLocationId | LOCATION_ID | — | — |
| 61 | AssignmentPEOManagerFlag | MANAGER_FLAG | — | — |
| 62 | AssignmentPEONormalHours | NORMAL_HOURS | — | — |
| 63 | AssignmentPEONoticePeriod | NOTICE_PERIOD | — | — |
| 64 | AssignmentPEONoticePeriodUom | NOTICE_PERIOD_UOM | — | — |
| 65 | AssignmentPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 66 | AssignmentPEOOrganizationId | ORGANIZATION_ID | — | — |
| 67 | AssignmentPEOParentAssignmentId | PARENT_ASSIGNMENT_ID | — | — |
| 68 | AssignmentPEOPeopleGroupId | PEOPLE_GROUP_ID | — | — |
| 69 | AssignmentPEOPeriodOfServiceId | PERIOD_OF_SERVICE_ID | — | — |
| 70 | AssignmentPEOPermanentTemporaryFlag | PERMANENT_TEMPORARY_FLAG | — | — |
| 71 | AssignmentPEOPersonId | PERSON_ID | — | — |
| 72 | AssignmentPEOPersonReferredById | PERSON_REFERRED_BY_ID | — | — |
| 73 | AssignmentPEOPersonTypeId | PERSON_TYPE_ID | — | — |
| 74 | AssignmentPEOPoHeaderId | PO_HEADER_ID | — | — |
| 75 | AssignmentPEOPoLineId | PO_LINE_ID | — | — |
| 76 | AssignmentPEOPositionId | POSITION_ID | — | — |
| 77 | AssignmentPEOPositionOverrideFlag | POSITION_OVERRIDE_FLAG | — | — |
| 78 | AssignmentPEOPostingContentId | POSTING_CONTENT_ID | — | — |
| 79 | AssignmentPEOPrimaryAssignmentFlag | PRIMARY_ASSIGNMENT_FLAG | — | — |
| 80 | AssignmentPEOPrimaryFlag | PRIMARY_FLAG | — | — |
| 81 | AssignmentPEOPrimaryWorkRelationFlag | PRIMARY_WORK_RELATION_FLAG | — | — |
| 82 | AssignmentPEOPrimaryWorkTermsFlag | PRIMARY_WORK_TERMS_FLAG | — | — |
| 83 | AssignmentPEOProbationPeriod | PROBATION_PERIOD | — | — |
| 84 | AssignmentPEOProbationUnit | PROBATION_UNIT | — | — |
| 85 | AssignmentPEOProjectTitle | PROJECT_TITLE | — | — |
| 86 | AssignmentPEOProjectedAssignmentEnd | PROJECTED_ASSIGNMENT_END | — | — |
| 87 | AssignmentPEOProjectedStartDate | PROJECTED_START_DATE | — | — |
| 88 | AssignmentPEOProposedWorkerType | PROPOSED_WORKER_TYPE | — | — |
| 89 | AssignmentPEOReasonCode | REASON_CODE | — | — |
| 90 | AssignmentPEORecordCreator | RECORD_CREATOR | — | — |
| 91 | AssignmentPEORecruiterId | RECRUITER_ID | — | — |
| 92 | AssignmentPEORecruitmentActivityId | RECRUITMENT_ACTIVITY_ID | — | — |
| 93 | AssignmentPEORetirementAge | RETIREMENT_AGE | — | — |
| 94 | AssignmentPEORetirementDate | RETIREMENT_DATE | — | — |
| 95 | AssignmentPEOSalReviewPeriod | SAL_REVIEW_PERIOD | — | — |
| 96 | AssignmentPEOSalReviewPeriodFrequency | SAL_REVIEW_PERIOD_FREQUENCY | — | — |
| 97 | AssignmentPEOSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 98 | AssignmentPEOSoftCodingKeyflexId | SOFT_CODING_KEYFLEX_ID | — | — |
| 99 | AssignmentPEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 100 | AssignmentPEOSourceType | SOURCE_TYPE | — | — |
| 101 | AssignmentPEOSpecialCeilingStepId | SPECIAL_CEILING_STEP_ID | — | — |
| 102 | AssignmentPEOStepEntryDate | STEP_ENTRY_DATE | — | — |
| 103 | AssignmentPEOSystemPersonType | SYSTEM_PERSON_TYPE | — | — |
| 104 | AssignmentPEOTaxAddressId | TAX_ADDRESS_ID | — | — |
| 105 | AssignmentPEOTimeNormalFinish | TIME_NORMAL_FINISH | — | — |
| 106 | AssignmentPEOTimeNormalStart | TIME_NORMAL_START | — | — |
| 107 | AssignmentPEOVacancyId | VACANCY_ID | — | — |
| 108 | AssignmentPEOVendorAssignmentNumber | VENDOR_ASSIGNMENT_NUMBER | — | — |
| 109 | AssignmentPEOVendorEmployeeNumber | VENDOR_EMPLOYEE_NUMBER | — | — |
| 110 | AssignmentPEOVendorId | VENDOR_ID | — | — |
| 111 | AssignmentPEOVendorSiteId | VENDOR_SITE_ID | — | — |
| 112 | AssignmentPEOWorkAtHome | WORK_AT_HOME | — | — |
| 113 | AssignmentPEOWorkTermsAssignmentId | WORK_TERMS_ASSIGNMENT_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
