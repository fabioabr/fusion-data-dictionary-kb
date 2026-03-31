---
id: DOC-OTHER-PVO-CategoryBookDefaultExtractPVO
doc_type: system-doc
title: "CategoryBookDefaultExtractPVO — PVO Cross-Module"
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
  - CategoryBookDefaultExtractPVO
  - categorybookdefaultextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CategoryBookDefaultExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Category Book Default Extract. Acessa as tabelas: FA_CATEGORY_BOOK_DEFAULTS.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.CategoryBookDefaultExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 96 | 1 | 1 | 70 | 73% |

---

## 🔗 Tabelas Relacionadas

- [[fa_category_book_defaults|FA_CATEGORY_BOOK_DEFAULTS]] — 96 atributos (1 PKs, 70 BICC)

---

## ⚙️ Atributos

### [[fa_category_book_defaults|FA_CATEGORY_BOOK_DEFAULTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryBookDefaultAdjustmentConventionTypeId | ADJUSTMENT_CONVENTION_TYPE_ID | — | ✅ |
| 2 | CategoryBookDefaultAdvancePaymentCostFlag | ADVANCE_PAYMENT_COST_FLAG | — | ✅ |
| 3 | CategoryBookDefaultAdvancePaymentLiabFlag | ADVANCE_PAYMENT_LIAB_FLAG | — | ✅ |
| 4 | CategoryBookDefaultAllocateToFullyRetFlag | ALLOCATE_TO_FULLY_RET_FLAG | — | ✅ |
| 5 | CategoryBookDefaultAllocateToFullyRsvFlag | ALLOCATE_TO_FULLY_RSV_FLAG | — | ✅ |
| 6 | CategoryBookDefaultAllowedDeprnLimit | ALLOWED_DEPRN_LIMIT | — | ✅ |
| 7 | CategoryBookDefaultAttribute1 | ATTRIBUTE1 | — | — |
| 8 | CategoryBookDefaultAttribute10 | ATTRIBUTE10 | — | — |
| 9 | CategoryBookDefaultAttribute11 | ATTRIBUTE11 | — | — |
| 10 | CategoryBookDefaultAttribute12 | ATTRIBUTE12 | — | — |
| 11 | CategoryBookDefaultAttribute13 | ATTRIBUTE13 | — | — |
| 12 | CategoryBookDefaultAttribute14 | ATTRIBUTE14 | — | — |
| 13 | CategoryBookDefaultAttribute15 | ATTRIBUTE15 | — | — |
| 14 | CategoryBookDefaultAttribute2 | ATTRIBUTE2 | — | — |
| 15 | CategoryBookDefaultAttribute3 | ATTRIBUTE3 | — | — |
| 16 | CategoryBookDefaultAttribute4 | ATTRIBUTE4 | — | — |
| 17 | CategoryBookDefaultAttribute5 | ATTRIBUTE5 | — | — |
| 18 | CategoryBookDefaultAttribute6 | ATTRIBUTE6 | — | — |
| 19 | CategoryBookDefaultAttribute7 | ATTRIBUTE7 | — | — |
| 20 | CategoryBookDefaultAttribute8 | ATTRIBUTE8 | — | — |
| 21 | CategoryBookDefaultAttribute9 | ATTRIBUTE9 | — | — |
| 22 | CategoryBookDefaultAttributeCategoryCode | ATTRIBUTE_CATEGORY_CODE | — | — |
| 23 | CategoryBookDefaultAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | CategoryBookDefaultAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | CategoryBookDefaultAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | CategoryBookDefaultAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | CategoryBookDefaultAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | CategoryBookDefaultAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 29 | CategoryBookDefaultAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 30 | CategoryBookDefaultAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 31 | CategoryBookDefaultAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 32 | CategoryBookDefaultAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 33 | CategoryBookDefaultBonusRuleId | BONUS_RULE_ID | — | ✅ |
| 34 | CategoryBookDefaultBookTypeCode | BOOK_TYPE_CODE | — | ✅ |
| 35 | CategoryBookDefaultCapThresholdAmount | CAP_THRESHOLD_AMOUNT | — | ✅ |
| 36 | CategoryBookDefaultCapitalGainThreshold | CAPITAL_GAIN_THRESHOLD | — | ✅ |
| 37 | CategoryBookDefaultCategoryBookDefaultId | CATEGORY_BOOK_DEFAULT_ID | 🔑 | ✅ |
| 38 | CategoryBookDefaultCategoryId | CATEGORY_ID | — | ✅ |
| 39 | CategoryBookDefaultCeilingTypeId | CEILING_TYPE_ID | — | ✅ |
| 40 | CategoryBookDefaultConventionTypeId | CONVENTION_TYPE_ID | — | ✅ |
| 41 | CategoryBookDefaultCreatedBy | CREATED_BY | — | ✅ |
| 42 | CategoryBookDefaultCreationDate | CREATION_DATE | — | ✅ |
| 43 | CategoryBookDefaultDepreciateFlag | DEPRECIATE_FLAG | — | ✅ |
| 44 | CategoryBookDefaultDepreciationOption | DEPRECIATION_OPTION | — | ✅ |
| 45 | CategoryBookDefaultDeprnLimitType | DEPRN_LIMIT_TYPE | — | ✅ |
| 46 | CategoryBookDefaultEndDpis | END_DPIS | — | ✅ |
| 47 | CategoryBookDefaultExcessAllocationOption | EXCESS_ALLOCATION_OPTION | — | ✅ |
| 48 | CategoryBookDefaultExcludeFullyRsvFlag | EXCLUDE_FULLY_RSV_FLAG | — | ✅ |
| 49 | CategoryBookDefaultFlatRateId | FLAT_RATE_ID | — | ✅ |
| 50 | CategoryBookDefaultGroupAssetId | GROUP_ASSET_ID | — | ✅ |
| 51 | CategoryBookDefaultInitialPaymentCostFlag | INITIAL_PAYMENT_COST_FLAG | — | ✅ |
| 52 | CategoryBookDefaultInitialPaymentLiabFlag | INITIAL_PAYMENT_LIAB_FLAG | — | ✅ |
| 53 | CategoryBookDefaultItcEligibleFlag | ITC_ELIGIBLE_FLAG | — | ✅ |
| 54 | CategoryBookDefaultLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 55 | CategoryBookDefaultLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 56 | CategoryBookDefaultLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 57 | CategoryBookDefaultLimitProceedsFlag | LIMIT_PROCEEDS_FLAG | — | ✅ |
| 58 | CategoryBookDefaultLowValueThresholdAmount | LOW_VALUE_THRESHOLD_AMOUNT | — | ✅ |
| 59 | CategoryBookDefaultLvaConventionTypeId | LVA_CONVENTION_TYPE_ID | — | ✅ |
| 60 | CategoryBookDefaultLvaFlatRateId | LVA_FLAT_RATE_ID | — | ✅ |
| 61 | CategoryBookDefaultLvaMethodId | LVA_METHOD_ID | — | ✅ |
| 62 | CategoryBookDefaultMassPropertyFlag | MASS_PROPERTY_FLAG | — | ✅ |
| 63 | CategoryBookDefaultMemberRollupFlag | MEMBER_ROLLUP_FLAG | — | ✅ |
| 64 | CategoryBookDefaultMethodId | METHOD_ID | — | ✅ |
| 65 | CategoryBookDefaultMinimumLifeInMonths | MINIMUM_LIFE_IN_MONTHS | — | ✅ |
| 66 | CategoryBookDefaultMinimumLifeInPeriods | MINIMUM_LIFE_IN_PERIODS | — | ✅ |
| 67 | CategoryBookDefaultObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 68 | CategoryBookDefaultOtherPaymentCostFlag | OTHER_PAYMENT_COST_FLAG | — | ✅ |
| 69 | CategoryBookDefaultOtherPaymentLiabFlag | OTHER_PAYMENT_LIAB_FLAG | — | ✅ |
| 70 | CategoryBookDefaultPercentSalvageValue | PERCENT_SALVAGE_VALUE | — | ✅ |
| 71 | CategoryBookDefaultPeriodPaymentCostFlag | PERIOD_PAYMENT_COST_FLAG | — | ✅ |
| 72 | CategoryBookDefaultPeriodPaymentLiabFlag | PERIOD_PAYMENT_LIAB_FLAG | — | ✅ |
| 73 | CategoryBookDefaultPriceIndexId | PRICE_INDEX_ID | — | ✅ |
| 74 | CategoryBookDefaultProductionCapacity | PRODUCTION_CAPACITY | — | ✅ |
| 75 | CategoryBookDefaultPurchasePaymentCostFlag | PURCHASE_PAYMENT_COST_FLAG | — | ✅ |
| 76 | CategoryBookDefaultPurchasePaymentLiabFlag | PURCHASE_PAYMENT_LIAB_FLAG | — | ✅ |
| 77 | CategoryBookDefaultReassessLiabilityFlag | REASSESS_LIABILITY_FLAG | — | ✅ |
| 78 | CategoryBookDefaultRecaptureReserveFlag | RECAPTURE_RESERVE_FLAG | — | ✅ |
| 79 | CategoryBookDefaultRecognizeGainLoss | RECOGNIZE_GAIN_LOSS | — | ✅ |
| 80 | CategoryBookDefaultResidualPaymentCostFlag | RESIDUAL_PAYMENT_COST_FLAG | — | ✅ |
| 81 | CategoryBookDefaultResidualPaymentLiabFlag | RESIDUAL_PAYMENT_LIAB_FLAG | — | ✅ |
| 82 | CategoryBookDefaultRetirementConventionTypeId | RETIREMENT_CONVENTION_TYPE_ID | — | ✅ |
| 83 | CategoryBookDefaultSpecialDeprnLimitAmount | SPECIAL_DEPRN_LIMIT_AMOUNT | — | ✅ |
| 84 | CategoryBookDefaultStartDpis | START_DPIS | — | ✅ |
| 85 | CategoryBookDefaultStlMethodId | STL_METHOD_ID | — | ✅ |
| 86 | CategoryBookDefaultSubcomponentLifeRule | SUBCOMPONENT_LIFE_RULE | — | ✅ |
| 87 | CategoryBookDefaultTerminalGainLoss | TERMINAL_GAIN_LOSS | — | ✅ |
| 88 | CategoryBookDefaultTerminalPaymentCostFlag | TERMINAL_PAYMENT_COST_FLAG | — | ✅ |
| 89 | CategoryBookDefaultTerminalPaymentLiabFlag | TERMINAL_PAYMENT_LIAB_FLAG | — | ✅ |
| 90 | CategoryBookDefaultTrackingMethod | TRACKING_METHOD | — | ✅ |
| 91 | CategoryBookDefaultUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 92 | CategoryBookDefaultUseAddConvForAdjtfrFlag | USE_ADD_CONV_FOR_ADJTFR_FLAG | — | ✅ |
| 93 | CategoryBookDefaultUseItcCeilingsFlag | USE_ITC_CEILINGS_FLAG | — | ✅ |
| 94 | CategoryBookDefaultUseStlRetirementsFlag | USE_STL_RETIREMENTS_FLAG | — | ✅ |
| 95 | CategoryBookDefaultVariablePaymentCostFlag | VARIABLE_PAYMENT_COST_FLAG | — | ✅ |
| 96 | CategoryBookDefaultVariablePaymentLiabFlag | VARIABLE_PAYMENT_LIAB_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
