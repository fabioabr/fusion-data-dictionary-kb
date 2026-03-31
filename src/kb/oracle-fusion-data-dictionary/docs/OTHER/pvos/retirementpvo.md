---
id: DOC-OTHER-PVO-RetirementPVO
doc_type: system-doc
title: "RetirementPVO — PVO Cross-Module"
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
  - RetirementPVO
  - retirementpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RetirementPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Retirement. Acessa as tabelas: FA_ADDITIONS_B, FA_CONVENTION_TYPES, FA_METHODS (+1).

**Caminho:** `FscmTopModelAM.FinFaSharedUtilAM.RetirementPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 125 | 4 | 1 | 30 | 24% |

---

## 🔗 Tabelas Relacionadas

- [[fa_additions_b|FA_ADDITIONS_B]] — 28 atributos (2 BICC)
- [[fa_convention_types|FA_CONVENTION_TYPES]] — 12 atributos (2 BICC)
- [[fa_methods|FA_METHODS]] — 20 atributos (2 BICC)
- [[fa_retirements|FA_RETIREMENTS]] — 65 atributos (1 PKs, 24 BICC)

---

## ⚙️ Atributos

### [[fa_additions_b|FA_ADDITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdditionBaseAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 2 | AdditionBaseAssetId | ASSET_ID | — | — |
| 3 | AdditionBaseAssetKeyCcid | ASSET_KEY_CCID | — | — |
| 4 | AdditionBaseAssetNumber | ASSET_NUMBER | — | ✅ |
| 5 | AdditionBaseAssetType | ASSET_TYPE | — | — |
| 6 | AdditionBaseCommitment | COMMITMENT | — | — |
| 7 | AdditionBaseContext | CONTEXT | — | — |
| 8 | AdditionBaseCreatedBy | CREATED_BY | — | — |
| 9 | AdditionBaseCreationDate | CREATION_DATE | — | — |
| 10 | AdditionBaseCurrentUnits | CURRENT_UNITS | — | — |
| 11 | AdditionBaseDistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | — |
| 12 | AdditionBaseInUseFlag | IN_USE_FLAG | — | — |
| 13 | AdditionBaseInventorial | INVENTORIAL | — | — |
| 14 | AdditionBaseInvestmentLaw | INVESTMENT_LAW | — | — |
| 15 | AdditionBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | AdditionBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | AdditionBaseLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | AdditionBaseLeaseId | LEASE_ID | — | — |
| 19 | AdditionBaseManufacturerName | MANUFACTURER_NAME | — | — |
| 20 | AdditionBaseModelNumber | MODEL_NUMBER | — | — |
| 21 | AdditionBaseNewUsed | NEW_USED | — | — |
| 22 | AdditionBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | AdditionBaseOwnedLeased | OWNED_LEASED | — | — |
| 24 | AdditionBaseParentAssetId | PARENT_ASSET_ID | — | — |
| 25 | AdditionBaseProperty12451250Code | PROPERTY_1245_1250_CODE | — | — |
| 26 | AdditionBasePropertyTypeCode | PROPERTY_TYPE_CODE | — | — |
| 27 | AdditionBaseSerialNumber | SERIAL_NUMBER | — | — |
| 28 | AdditionBaseTagNumber | TAG_NUMBER | — | — |

### [[fa_convention_types|FA_CONVENTION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProrateConventionTypeConventionTypeId | CONVENTION_TYPE_ID | — | — |
| 2 | ProrateConventionTypeCreatedBy | CREATED_BY | — | — |
| 3 | ProrateConventionTypeCreationDate | CREATION_DATE | — | — |
| 4 | ProrateConventionTypeDeprWhenAcquiredFlag | DEPR_WHEN_ACQUIRED_FLAG | — | — |
| 5 | ProrateConventionTypeDescription | DESCRIPTION | — | — |
| 6 | ProrateConventionTypeFiscalYearName | FISCAL_YEAR_NAME | — | — |
| 7 | ProrateConventionTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ProrateConventionTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ProrateConventionTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ProrateConventionTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ProrateConventionTypeProrateConventionCode | PRORATE_CONVENTION_CODE | — | ✅ |
| 12 | ProrateConventionTypeSetId | SET_ID | — | — |

### [[fa_methods|FA_METHODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DepreciationMethodCreatedBy | CREATED_BY | — | — |
| 2 | DepreciationMethodCreationDate | CREATION_DATE | — | — |
| 3 | DepreciationMethodDepreciateLastyearFlag | DEPRECIATE_LASTYEAR_FLAG | — | — |
| 4 | DepreciationMethodDeprnBasisRule | DEPRN_BASIS_RULE | — | — |
| 5 | DepreciationMethodDeprnBasisRuleId | DEPRN_BASIS_RULE_ID | — | — |
| 6 | DepreciationMethodExcludeSalvageValueFlag | EXCLUDE_SALVAGE_VALUE_FLAG | — | — |
| 7 | DepreciationMethodLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | DepreciationMethodLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | DepreciationMethodLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | DepreciationMethodLifeInMonths | LIFE_IN_MONTHS | — | — |
| 11 | DepreciationMethodMethodCode | METHOD_CODE | — | ✅ |
| 12 | DepreciationMethodMethodId | METHOD_ID | — | — |
| 13 | DepreciationMethodName | NAME | — | — |
| 14 | DepreciationMethodObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | DepreciationMethodPolishAdjCalcBasisFlag | POLISH_ADJ_CALC_BASIS_FLAG | — | — |
| 16 | DepreciationMethodProratePeriodsPerYear | PRORATE_PERIODS_PER_YEAR | — | — |
| 17 | DepreciationMethodRateSourceRule | RATE_SOURCE_RULE | — | — |
| 18 | DepreciationMethodSetId | SET_ID | — | — |
| 19 | DepreciationMethodStlMethodFlag | STL_METHOD_FLAG | — | — |
| 20 | DepreciationMethodUseLifeInPeriodsFlag | USE_LIFE_IN_PERIODS_FLAG | — | — |

### [[fa_retirements|FA_RETIREMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RetirementAssetId | ASSET_ID | — | — |
| 2 | RetirementAttribute1 | ATTRIBUTE1 | — | — |
| 3 | RetirementAttribute10 | ATTRIBUTE10 | — | — |
| 4 | RetirementAttribute11 | ATTRIBUTE11 | — | — |
| 5 | RetirementAttribute12 | ATTRIBUTE12 | — | — |
| 6 | RetirementAttribute13 | ATTRIBUTE13 | — | — |
| 7 | RetirementAttribute14 | ATTRIBUTE14 | — | — |
| 8 | RetirementAttribute15 | ATTRIBUTE15 | — | — |
| 9 | RetirementAttribute2 | ATTRIBUTE2 | — | — |
| 10 | RetirementAttribute3 | ATTRIBUTE3 | — | — |
| 11 | RetirementAttribute4 | ATTRIBUTE4 | — | — |
| 12 | RetirementAttribute5 | ATTRIBUTE5 | — | — |
| 13 | RetirementAttribute6 | ATTRIBUTE6 | — | — |
| 14 | RetirementAttribute7 | ATTRIBUTE7 | — | — |
| 15 | RetirementAttribute8 | ATTRIBUTE8 | — | — |
| 16 | RetirementAttribute9 | ATTRIBUTE9 | — | — |
| 17 | RetirementAttributeCategoryCode | ATTRIBUTE_CATEGORY_CODE | — | — |
| 18 | RetirementAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 19 | RetirementAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 20 | RetirementAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 21 | RetirementAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 22 | RetirementAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 23 | RetirementAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 24 | RetirementAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 25 | RetirementAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 26 | RetirementAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 27 | RetirementAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 28 | RetirementBonusReserveRetired | BONUS_RESERVE_RETIRED | — | ✅ |
| 29 | RetirementBookTypeCode | BOOK_TYPE_CODE | — | — |
| 30 | RetirementCostOfRemoval | COST_OF_REMOVAL | — | ✅ |
| 31 | RetirementCostRetired | COST_RETIRED | — | ✅ |
| 32 | RetirementCreatedBy | CREATED_BY | — | — |
| 33 | RetirementCreationDate | CREATION_DATE | — | — |
| 34 | RetirementDateEffective | DATE_EFFECTIVE | — | ✅ |
| 35 | RetirementDateRetired | DATE_RETIRED | — | ✅ |
| 36 | RetirementEofyReserve | EOFY_RESERVE | — | — |
| 37 | RetirementGainLossAmount | GAIN_LOSS_AMOUNT | — | ✅ |
| 38 | RetirementGainLossTypeCode | GAIN_LOSS_TYPE_CODE | — | ✅ |
| 39 | RetirementId | RETIREMENT_ID | 🔑 | ✅ |
| 40 | RetirementLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 41 | RetirementLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 42 | RetirementLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 43 | RetirementLimitProceedsFlag | LIMIT_PROCEEDS_FLAG | — | ✅ |
| 44 | RetirementNbvRetired | NBV_RETIRED | — | ✅ |
| 45 | RetirementObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 46 | RetirementProceedsOfSale | PROCEEDS_OF_SALE | — | ✅ |
| 47 | RetirementRecaptureAmount | RECAPTURE_AMOUNT | — | ✅ |
| 48 | RetirementRecaptureReserveFlag | RECAPTURE_RESERVE_FLAG | — | ✅ |
| 49 | RetirementRecognizeGainLoss | RECOGNIZE_GAIN_LOSS | — | ✅ |
| 50 | RetirementReductionRate | REDUCTION_RATE | — | ✅ |
| 51 | RetirementReferenceNum | REFERENCE_NUM | — | — |
| 52 | RetirementReserveRetired | RESERVE_RETIRED | — | ✅ |
| 53 | RetirementRetirementConventionTypeId | RETIREMENT_CONVENTION_TYPE_ID | — | — |
| 54 | RetirementRetirementTypeCode | RETIREMENT_TYPE_CODE | — | ✅ |
| 55 | RetirementRevalReserveRetired | REVAL_RESERVE_RETIRED | — | — |
| 56 | RetirementSoldTo | SOLD_TO | — | ✅ |
| 57 | RetirementStatus | STATUS | — | ✅ |
| 58 | RetirementStlDeprnAmount | STL_DEPRN_AMOUNT | — | ✅ |
| 59 | RetirementStlMethodId | STL_METHOD_ID | — | — |
| 60 | RetirementTerminalGainLoss | TERMINAL_GAIN_LOSS | — | ✅ |
| 61 | RetirementTradeInAssetId | TRADE_IN_ASSET_ID | — | — |
| 62 | RetirementTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | — |
| 63 | RetirementTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | — |
| 64 | RetirementUnits | UNITS | — | ✅ |
| 65 | RetirementUnrevaluedCostRetired | UNREVALUED_COST_RETIRED | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
