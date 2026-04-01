---
id: DOC-OTHER-PVO-CategoryBookDefaultPVO
doc_type: system-doc
title: "CategoryBookDefaultPVO — PVO Cross-Module"
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
  - CategoryBookDefaultPVO
  - categorybookdefaultpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CategoryBookDefaultPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Category Book Default. Acessa as tabelas: FA_ADDITIONS_VL, FA_BONUS_RULES, FA_CATEGORY_BOOK_DEFAULTS (+6).

**Caminho:** `FscmTopModelAM.FinFaDeprnSetupCategoriesAM.CategoryBookDefaultPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 112 | 9 | 1 | 35 | 31% |

---

## 🔗 Tabelas Relacionadas

- [[fa_additions_vl|FA_ADDITIONS_VL]] — 3 atributos (2 BICC)
- [[fa_bonus_rules|FA_BONUS_RULES]] — 2 atributos (1 BICC)
- [[fa_category_book_defaults|FA_CATEGORY_BOOK_DEFAULTS]] — 68 atributos (1 PKs, 21 BICC)
- [[fa_ceiling_types|FA_CEILING_TYPES]] — 2 atributos
- [[fa_convention_types|FA_CONVENTION_TYPES]] — 3 atributos (1 BICC)
- [[fa_flat_rates|FA_FLAT_RATES]] — 8 atributos (4 BICC)
- [[fa_methods|FA_METHODS]] — 6 atributos (4 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (2 BICC)
- [[per_users|PER_USERS]] — 10 atributos

---

## ⚙️ Atributos

### [[fa_additions_vl|FA_ADDITIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DefaultAssetId | ASSET_ID | — | — |
| 2 | DefaultAssetNumber | ASSET_NUMBER | — | ✅ |
| 3 | DefaultDescription | DESCRIPTION | — | ✅ |

### [[fa_bonus_rules|FA_BONUS_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BonusRulePEOBonusRule | BONUS_RULE | — | ✅ |
| 2 | BonusRulePEOBonusRuleId | BONUS_RULE_ID | — | — |

### [[fa_category_book_defaults|FA_CATEGORY_BOOK_DEFAULTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryBookDefaultPEOAllocateToFullyRetFlag | ALLOCATE_TO_FULLY_RET_FLAG | — | — |
| 2 | CategoryBookDefaultPEOAllocateToFullyRsvFlag | ALLOCATE_TO_FULLY_RSV_FLAG | — | — |
| 3 | CategoryBookDefaultPEOAllowedDeprnLimit | ALLOWED_DEPRN_LIMIT | — | ✅ |
| 4 | CategoryBookDefaultPEOAttribute1 | ATTRIBUTE1 | — | — |
| 5 | CategoryBookDefaultPEOAttribute10 | ATTRIBUTE10 | — | — |
| 6 | CategoryBookDefaultPEOAttribute11 | ATTRIBUTE11 | — | — |
| 7 | CategoryBookDefaultPEOAttribute12 | ATTRIBUTE12 | — | — |
| 8 | CategoryBookDefaultPEOAttribute13 | ATTRIBUTE13 | — | — |
| 9 | CategoryBookDefaultPEOAttribute14 | ATTRIBUTE14 | — | — |
| 10 | CategoryBookDefaultPEOAttribute15 | ATTRIBUTE15 | — | — |
| 11 | CategoryBookDefaultPEOAttribute2 | ATTRIBUTE2 | — | — |
| 12 | CategoryBookDefaultPEOAttribute3 | ATTRIBUTE3 | — | — |
| 13 | CategoryBookDefaultPEOAttribute4 | ATTRIBUTE4 | — | — |
| 14 | CategoryBookDefaultPEOAttribute5 | ATTRIBUTE5 | — | — |
| 15 | CategoryBookDefaultPEOAttribute6 | ATTRIBUTE6 | — | — |
| 16 | CategoryBookDefaultPEOAttribute7 | ATTRIBUTE7 | — | — |
| 17 | CategoryBookDefaultPEOAttribute8 | ATTRIBUTE8 | — | — |
| 18 | CategoryBookDefaultPEOAttribute9 | ATTRIBUTE9 | — | — |
| 19 | CategoryBookDefaultPEOAttributeCategoryCode | ATTRIBUTE_CATEGORY_CODE | — | — |
| 20 | CategoryBookDefaultPEOBonusRuleId | BONUS_RULE_ID | — | — |
| 21 | CategoryBookDefaultPEOBookTypeCode | BOOK_TYPE_CODE | — | — |
| 22 | CategoryBookDefaultPEOCapThresholdAmount | CAP_THRESHOLD_AMOUNT | — | ✅ |
| 23 | CategoryBookDefaultPEOCapitalGainThreshold | CAPITAL_GAIN_THRESHOLD | — | — |
| 24 | CategoryBookDefaultPEOCategoryBookDefaultId | CATEGORY_BOOK_DEFAULT_ID | 🔑 | ✅ |
| 25 | CategoryBookDefaultPEOCategoryId | CATEGORY_ID | — | — |
| 26 | CategoryBookDefaultPEOCeilingTypeId | CEILING_TYPE_ID | — | ✅ |
| 27 | CategoryBookDefaultPEOConventionTypeId | CONVENTION_TYPE_ID | — | — |
| 28 | CategoryBookDefaultPEOCreatedBy | CREATED_BY | — | ✅ |
| 29 | CategoryBookDefaultPEOCreationDate | CREATION_DATE | — | ✅ |
| 30 | CategoryBookDefaultPEODepreciateFlag | DEPRECIATE_FLAG | — | ✅ |
| 31 | CategoryBookDefaultPEODepreciationOption | DEPRECIATION_OPTION | — | — |
| 32 | CategoryBookDefaultPEODeprnLimitType | DEPRN_LIMIT_TYPE | — | ✅ |
| 33 | CategoryBookDefaultPEOEndDpis | END_DPIS | — | ✅ |
| 34 | CategoryBookDefaultPEOExcessAllocationOption | EXCESS_ALLOCATION_OPTION | — | — |
| 35 | CategoryBookDefaultPEOExcludeFullyRsvFlag | EXCLUDE_FULLY_RSV_FLAG | — | — |
| 36 | CategoryBookDefaultPEOFlatRateId | FLAT_RATE_ID | — | — |
| 37 | CategoryBookDefaultPEOGroupAssetId | GROUP_ASSET_ID | — | — |
| 38 | CategoryBookDefaultPEOItcEligibleFlag | ITC_ELIGIBLE_FLAG | — | — |
| 39 | CategoryBookDefaultPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 40 | CategoryBookDefaultPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 41 | CategoryBookDefaultPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 42 | CategoryBookDefaultPEOLimitProceedsFlag | LIMIT_PROCEEDS_FLAG | — | — |
| 43 | CategoryBookDefaultPEOLowValueThresholdAmount | LOW_VALUE_THRESHOLD_AMOUNT | — | ✅ |
| 44 | CategoryBookDefaultPEOLvaConventionTypeId | LVA_CONVENTION_TYPE_ID | — | — |
| 45 | CategoryBookDefaultPEOLvaFlatRateId | LVA_FLAT_RATE_ID | — | — |
| 46 | CategoryBookDefaultPEOLvaMethodId | LVA_METHOD_ID | — | — |
| 47 | CategoryBookDefaultPEOMassPropertyFlag | MASS_PROPERTY_FLAG | — | ✅ |
| 48 | CategoryBookDefaultPEOMemberRollupFlag | MEMBER_ROLLUP_FLAG | — | — |
| 49 | CategoryBookDefaultPEOMethodId | METHOD_ID | — | — |
| 50 | CategoryBookDefaultPEOMinimumLifeInMonths | MINIMUM_LIFE_IN_MONTHS | — | ✅ |
| 51 | CategoryBookDefaultPEOMinimumLifeInPeriods | MINIMUM_LIFE_IN_PERIODS | — | — |
| 52 | CategoryBookDefaultPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 53 | CategoryBookDefaultPEOPercentSalvageValue | PERCENT_SALVAGE_VALUE | — | ✅ |
| 54 | CategoryBookDefaultPEOPriceIndexId | PRICE_INDEX_ID | — | ✅ |
| 55 | CategoryBookDefaultPEOProductionCapacity | PRODUCTION_CAPACITY | — | ✅ |
| 56 | CategoryBookDefaultPEORecaptureReserveFlag | RECAPTURE_RESERVE_FLAG | — | — |
| 57 | CategoryBookDefaultPEORecognizeGainLoss | RECOGNIZE_GAIN_LOSS | — | — |
| 58 | CategoryBookDefaultPEORetirementConventionTypeId | RETIREMENT_CONVENTION_TYPE_ID | — | — |
| 59 | CategoryBookDefaultPEOSpecialDeprnLimitAmount | SPECIAL_DEPRN_LIMIT_AMOUNT | — | ✅ |
| 60 | CategoryBookDefaultPEOStartDpis | START_DPIS | — | ✅ |
| 61 | CategoryBookDefaultPEOStlMethodId | STL_METHOD_ID | — | — |
| 62 | CategoryBookDefaultPEOSubcomponentLifeRule | SUBCOMPONENT_LIFE_RULE | — | ✅ |
| 63 | CategoryBookDefaultPEOTerminalGainLoss | TERMINAL_GAIN_LOSS | — | — |
| 64 | CategoryBookDefaultPEOTrackingMethod | TRACKING_METHOD | — | — |
| 65 | CategoryBookDefaultPEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 66 | CategoryBookDefaultPEOUseAddConvForAdjtfrFlag | USE_ADD_CONV_FOR_ADJTFR_FLAG | — | — |
| 67 | CategoryBookDefaultPEOUseItcCeilingsFlag | USE_ITC_CEILINGS_FLAG | — | — |
| 68 | CategoryBookDefaultPEOUseStlRetirementsFlag | USE_STL_RETIREMENTS_FLAG | — | — |

### [[fa_ceiling_types|FA_CEILING_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CeilingTypeId | CEILING_TYPE_ID | — | — |
| 2 | CeilingTypePEOCeilingName | CEILING_NAME | — | — |

### [[fa_convention_types|FA_CONVENTION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConventionTypeId | CONVENTION_TYPE_ID | — | — |
| 2 | ProrateLVAConventionTypePEODescription | DESCRIPTION | — | ✅ |
| 3 | ProrateLVAConventionTypePEOProrateConventionCode | PRORATE_CONVENTION_CODE | — | — |

### [[fa_flat_rates|FA_FLAT_RATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DepreciationFlatRateAdjustedRate | ADJUSTED_RATE | — | ✅ |
| 2 | DepreciationFlatRateBasicRate | BASIC_RATE | — | ✅ |
| 3 | DepreciationFlatRateMethodId | METHOD_ID | — | — |
| 4 | DepreciationLVAFlatRatePEOAdjustedRate | ADJUSTED_RATE | — | ✅ |
| 5 | DepreciationLVAFlatRatePEOBasicRate | BASIC_RATE | — | ✅ |
| 6 | FlatRateId | FLAT_RATE_ID | — | — |
| 7 | FlatRatePEOFlatRateId | FLAT_RATE_ID | — | — |
| 8 | MethodId | METHOD_ID | — | — |

### [[fa_methods|FA_METHODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DepreciationLVAMethodPEOLifeInMonths | LIFE_IN_MONTHS | — | ✅ |
| 2 | DepreciationLVAMethodPEOMethodId | METHOD_ID | — | — |
| 3 | DepreciationLVAMethodPEOName | NAME | — | ✅ |
| 4 | DepreciationMethodPEOLifeInMonths | LIFE_IN_MONTHS | — | ✅ |
| 5 | DepreciationMethodPEOMethodId | METHOD_ID | — | — |
| 6 | DepreciationMethodPEOName | NAME | — | ✅ |

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

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
