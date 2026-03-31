---
id: DOC-OTHER-PVO-DistributionHistoryPVO
doc_type: system-doc
title: "DistributionHistoryPVO — PVO Cross-Module"
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
  - DistributionHistoryPVO
  - distributionhistorypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DistributionHistoryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Distribution History. Acessa as tabelas: FA_ADDITIONS_B, FA_BOOK_CONTROLS, FA_DISTRIBUTION_HISTORY (+2).

**Caminho:** `FscmTopModelAM.FinFaSharedUtilAM.DistributionHistoryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 154 | 5 | 1 | 15 | 10% |

---

## 🔗 Tabelas Relacionadas

- [[fa_additions_b|FA_ADDITIONS_B]] — 50 atributos (1 BICC)
- [[fa_book_controls|FA_BOOK_CONTROLS]] — 4 atributos
- [[fa_distribution_history|FA_DISTRIBUTION_HISTORY]] — 19 atributos (1 PKs, 8 BICC)
- [[fa_retirements|FA_RETIREMENTS]] — 33 atributos
- [[fa_transaction_headers|FA_TRANSACTION_HEADERS]] — 48 atributos (6 BICC)

---

## ⚙️ Atributos

### [[fa_additions_b|FA_ADDITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdditionAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 2 | AdditionAssetId | ASSET_ID | — | — |
| 3 | AdditionAssetKeyCcid | ASSET_KEY_CCID | — | — |
| 4 | AdditionAssetNumber | ASSET_NUMBER | — | — |
| 5 | AdditionAssetType | ASSET_TYPE | — | — |
| 6 | AdditionCommitment | COMMITMENT | — | — |
| 7 | AdditionContext | CONTEXT | — | — |
| 8 | AdditionCreatedBy | CREATED_BY | — | — |
| 9 | AdditionCreationDate | CREATION_DATE | — | — |
| 10 | AdditionCurrentUnits | CURRENT_UNITS | — | — |
| 11 | AdditionDistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | — |
| 12 | AdditionInUseFlag | IN_USE_FLAG | — | — |
| 13 | AdditionInventorial | INVENTORIAL | — | — |
| 14 | AdditionInvestmentLaw | INVESTMENT_LAW | — | — |
| 15 | AdditionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | AdditionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | AdditionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | AdditionLeaseId | LEASE_ID | — | — |
| 19 | AdditionManufacturerName | MANUFACTURER_NAME | — | — |
| 20 | AdditionModelNumber | MODEL_NUMBER | — | — |
| 21 | AdditionNewUsed | NEW_USED | — | — |
| 22 | AdditionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | AdditionOwnedLeased | OWNED_LEASED | — | — |
| 24 | AdditionParentAssetId | PARENT_ASSET_ID | — | — |
| 25 | AdditionPrntAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 26 | AdditionPrntAssetId | ASSET_ID | — | — |
| 27 | AdditionPrntAssetKeyCcid | ASSET_KEY_CCID | — | — |
| 28 | AdditionPrntAssetNumber | ASSET_NUMBER | — | — |
| 29 | AdditionPrntAssetType | ASSET_TYPE | — | — |
| 30 | AdditionPrntCommitment | COMMITMENT | — | — |
| 31 | AdditionPrntContext | CONTEXT | — | — |
| 32 | AdditionPrntCurrentUnits | CURRENT_UNITS | — | — |
| 33 | AdditionPrntDistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | — |
| 34 | AdditionPrntInUseFlag | IN_USE_FLAG | — | — |
| 35 | AdditionPrntInventorial | INVENTORIAL | — | — |
| 36 | AdditionPrntInvestmentLaw | INVESTMENT_LAW | — | — |
| 37 | AdditionPrntLeaseId | LEASE_ID | — | — |
| 38 | AdditionPrntManufacturerName | MANUFACTURER_NAME | — | — |
| 39 | AdditionPrntModelNumber | MODEL_NUMBER | — | — |
| 40 | AdditionPrntNewUsed | NEW_USED | — | — |
| 41 | AdditionPrntOwnedLeased | OWNED_LEASED | — | — |
| 42 | AdditionPrntParentAssetId | PARENT_ASSET_ID | — | — |
| 43 | AdditionPrntProperty12451250Code | PROPERTY_1245_1250_CODE | — | — |
| 44 | AdditionPrntPropertyTypeCode | PROPERTY_TYPE_CODE | — | — |
| 45 | AdditionPrntSerialNumber | SERIAL_NUMBER | — | — |
| 46 | AdditionPrntTagNumber | TAG_NUMBER | — | — |
| 47 | AdditionProperty12451250Code | PROPERTY_1245_1250_CODE | — | — |
| 48 | AdditionPropertyTypeCode | PROPERTY_TYPE_CODE | — | — |
| 49 | AdditionSerialNumber | SERIAL_NUMBER | — | — |
| 50 | AdditionTagNumber | TAG_NUMBER | — | — |

### [[fa_book_controls|FA_BOOK_CONTROLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BookControlAccountingFlexStructure | ACCOUNTING_FLEX_STRUCTURE | — | — |
| 2 | BookControlBookControlId | BOOK_CONTROL_ID | — | — |
| 3 | BookControlBookTypeCode | BOOK_TYPE_CODE | — | — |
| 4 | BookControlSetOfBooksId | SET_OF_BOOKS_ID | — | — |

### [[fa_distribution_history|FA_DISTRIBUTION_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistHistAssetId | ASSET_ID | — | ✅ |
| 2 | DistHistAssignedTo | ASSIGNED_TO | — | — |
| 3 | DistHistBookTypeCode | BOOK_TYPE_CODE | — | — |
| 4 | DistHistCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 5 | DistHistCreatedBy | CREATED_BY | — | — |
| 6 | DistHistCreationDate | CREATION_DATE | — | — |
| 7 | DistHistDateEffective | DATE_EFFECTIVE | — | — |
| 8 | DistHistDateIneffective | DATE_INEFFECTIVE | — | ✅ |
| 9 | DistHistLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | DistHistLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | DistHistLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | DistHistLocationId | LOCATION_ID | — | — |
| 13 | DistHistObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | DistHistRetirementId | RETIREMENT_ID | — | — |
| 15 | DistHistTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | ✅ |
| 16 | DistHistTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | ✅ |
| 17 | DistHistTransactionUnits | TRANSACTION_UNITS | — | ✅ |
| 18 | DistHistUnitsAssigned | UNITS_ASSIGNED | — | ✅ |
| 19 | DistributionId | DISTRIBUTION_ID | 🔑 | ✅ |

### [[fa_retirements|FA_RETIREMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RetirementInAssetId | ASSET_ID | — | — |
| 2 | RetirementInBonusReserveRetired | BONUS_RESERVE_RETIRED | — | — |
| 3 | RetirementInBookTypeCode | BOOK_TYPE_CODE | — | — |
| 4 | RetirementInCostOfRemoval | COST_OF_REMOVAL | — | — |
| 5 | RetirementInCostRetired | COST_RETIRED | — | — |
| 6 | RetirementInDateEffective | DATE_EFFECTIVE | — | — |
| 7 | RetirementInDateRetired | DATE_RETIRED | — | — |
| 8 | RetirementInEofyReserve | EOFY_RESERVE | — | — |
| 9 | RetirementInGainLossAmount | GAIN_LOSS_AMOUNT | — | — |
| 10 | RetirementInGainLossTypeCode | GAIN_LOSS_TYPE_CODE | — | — |
| 11 | RetirementInLimitProceedsFlag | LIMIT_PROCEEDS_FLAG | — | — |
| 12 | RetirementInNbvRetired | NBV_RETIRED | — | — |
| 13 | RetirementInProceedsOfSale | PROCEEDS_OF_SALE | — | — |
| 14 | RetirementInRecaptureAmount | RECAPTURE_AMOUNT | — | — |
| 15 | RetirementInRecaptureReserveFlag | RECAPTURE_RESERVE_FLAG | — | — |
| 16 | RetirementInRecognizeGainLoss | RECOGNIZE_GAIN_LOSS | — | — |
| 17 | RetirementInReductionRate | REDUCTION_RATE | — | — |
| 18 | RetirementInReferenceNum | REFERENCE_NUM | — | — |
| 19 | RetirementInReserveRetired | RESERVE_RETIRED | — | — |
| 20 | RetirementInRetirementConventionTypeId | RETIREMENT_CONVENTION_TYPE_ID | — | — |
| 21 | RetirementInRetirementId | RETIREMENT_ID | — | — |
| 22 | RetirementInRetirementTypeCode | RETIREMENT_TYPE_CODE | — | — |
| 23 | RetirementInRevalReserveRetired | REVAL_RESERVE_RETIRED | — | — |
| 24 | RetirementInSoldTo | SOLD_TO | — | — |
| 25 | RetirementInStatus | STATUS | — | — |
| 26 | RetirementInStlDeprnAmount | STL_DEPRN_AMOUNT | — | — |
| 27 | RetirementInStlMethodId | STL_METHOD_ID | — | — |
| 28 | RetirementInTerminalGainLoss | TERMINAL_GAIN_LOSS | — | — |
| 29 | RetirementInTradeInAssetId | TRADE_IN_ASSET_ID | — | — |
| 30 | RetirementInTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | — |
| 31 | RetirementInTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | — |
| 32 | RetirementInUnits | UNITS | — | — |
| 33 | RetirementInUnrevaluedCostRetired | UNREVALUED_COST_RETIRED | — | — |

### [[fa_transaction_headers|FA_TRANSACTION_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InTrxHdrAmortizationStartDate | AMORTIZATION_START_DATE | — | — |
| 2 | InTrxHdrAssetId | ASSET_ID | — | — |
| 3 | InTrxHdrBookTypeCode | BOOK_TYPE_CODE | — | — |
| 4 | InTrxHdrCallingInterface | CALLING_INTERFACE | — | — |
| 5 | InTrxHdrCreatedBy | CREATED_BY | — | — |
| 6 | InTrxHdrCreationDate | CREATION_DATE | — | — |
| 7 | InTrxHdrDateEffective | DATE_EFFECTIVE | — | — |
| 8 | InTrxHdrEventId | EVENT_ID | — | — |
| 9 | InTrxHdrInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 10 | InTrxHdrLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | InTrxHdrLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | InTrxHdrLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | InTrxHdrMassReferenceId | MASS_REFERENCE_ID | — | — |
| 14 | InTrxHdrMassTransactionId | MASS_TRANSACTION_ID | — | — |
| 15 | InTrxHdrMemberTransactionHeaderId | MEMBER_TRANSACTION_HEADER_ID | — | — |
| 16 | InTrxHdrObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | InTrxHdrSourceTransactionHeaderId | SOURCE_TRANSACTION_HEADER_ID | — | — |
| 18 | InTrxHdrTransactionDateEntered | TRANSACTION_DATE_ENTERED | — | — |
| 19 | InTrxHdrTransactionHeaderId | TRANSACTION_HEADER_ID | — | — |
| 20 | InTrxHdrTransactionKey | TRANSACTION_KEY | — | ✅ |
| 21 | InTrxHdrTransactionName | TRANSACTION_NAME | — | ✅ |
| 22 | InTrxHdrTransactionSubtype | TRANSACTION_SUBTYPE | — | ✅ |
| 23 | InTrxHdrTransactionTypeCode | TRANSACTION_TYPE_CODE | — | — |
| 24 | InTrxHdrTrxReferenceId | TRX_REFERENCE_ID | — | — |
| 25 | OutTrxHdrAmortizationStartDate | AMORTIZATION_START_DATE | — | — |
| 26 | OutTrxHdrAssetId | ASSET_ID | — | — |
| 27 | OutTrxHdrBookTypeCode | BOOK_TYPE_CODE | — | — |
| 28 | OutTrxHdrCallingInterface | CALLING_INTERFACE | — | — |
| 29 | OutTrxHdrCreatedBy | CREATED_BY | — | — |
| 30 | OutTrxHdrCreationDate | CREATION_DATE | — | — |
| 31 | OutTrxHdrDateEffective | DATE_EFFECTIVE | — | — |
| 32 | OutTrxHdrEventId | EVENT_ID | — | — |
| 33 | OutTrxHdrInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 34 | OutTrxHdrLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 35 | OutTrxHdrLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 36 | OutTrxHdrLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 37 | OutTrxHdrMassReferenceId | MASS_REFERENCE_ID | — | — |
| 38 | OutTrxHdrMassTransactionId | MASS_TRANSACTION_ID | — | — |
| 39 | OutTrxHdrMemberTransactionHeaderId | MEMBER_TRANSACTION_HEADER_ID | — | — |
| 40 | OutTrxHdrObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 41 | OutTrxHdrSourceTransactionHeaderId | SOURCE_TRANSACTION_HEADER_ID | — | — |
| 42 | OutTrxHdrTransactionDateEntered | TRANSACTION_DATE_ENTERED | — | — |
| 43 | OutTrxHdrTransactionHeaderId | TRANSACTION_HEADER_ID | — | — |
| 44 | OutTrxHdrTransactionKey | TRANSACTION_KEY | — | — |
| 45 | OutTrxHdrTransactionName | TRANSACTION_NAME | — | — |
| 46 | OutTrxHdrTransactionSubtype | TRANSACTION_SUBTYPE | — | — |
| 47 | OutTrxHdrTransactionTypeCode | TRANSACTION_TYPE_CODE | — | ✅ |
| 48 | OutTrxHdrTrxReferenceId | TRX_REFERENCE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
