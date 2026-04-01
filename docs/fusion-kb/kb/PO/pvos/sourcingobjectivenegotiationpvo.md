---
id: DOC-PO-PVO-SourcingObjectiveNegotiationPVO
doc_type: system-doc
title: "SourcingObjectiveNegotiationPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - SourcingObjectiveNegotiationPVO
  - sourcingobjectivenegotiationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SourcingObjectiveNegotiationPVO

## 📌 Visão Geral

Extrai os objetivos definidos para negociações de sourcing (melhor preço, melhor valor, savings target), com métricas e resultados. Permite análise de alinhamento entre estratégia e execução.

**Caminho:** `FscmTopModelAM.PrcPonPublicViewAM.SourcingObjectiveNegotiationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 228 | 12 | 3 | 39 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[egp_categories_vl|EGP_CATEGORIES_VL]] — 24 atributos
- [[fnd_lookups|FND_LOOKUPS]] — 52 atributos (3 BICC)
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 4 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 24 atributos (3 BICC)
- [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]] — 21 atributos (6 BICC)
- [[pon_neg_agg_to_obj_otbi_v|PON_NEG_AGG_TO_OBJ_OTBI_V]] — 6 atributos
- [[pon_neg_agg_to_prog_otbi_v|PON_NEG_AGG_TO_PROG_OTBI_V]] — 5 atributos
- [[pon_objective_negotiations|PON_OBJECTIVE_NEGOTIATIONS]] — 17 atributos (1 PKs, 4 BICC)
- [[pon_obj_agg_to_prog_otbi_v|PON_OBJ_AGG_TO_PROG_OTBI_V]] — 4 atributos
- [[pon_program_headers|PON_PROGRAM_HEADERS]] — 26 atributos (1 PKs, 12 BICC)
- [[pon_program_objectives|PON_PROGRAM_OBJECTIVES]] — 23 atributos (1 PKs, 10 BICC)
- [[por_browse_categories_vl|POR_BROWSE_CATEGORIES_VL]] — 22 atributos

---

## ⚙️ Atributos

### [[egp_categories_vl|EGP_CATEGORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectiveCategoryPEOCategoryCode | CATEGORY_CODE | — | — |
| 2 | ObjectiveCategoryPEOCategoryContentCode | CATEGORY_CONTENT_CODE | — | — |
| 3 | ObjectiveCategoryPEOCategoryId | CATEGORY_ID | — | — |
| 4 | ObjectiveCategoryPEOCategoryName | CATEGORY_NAME | — | — |
| 5 | ObjectiveCategoryPEODescription | DESCRIPTION | — | — |
| 6 | ObjectiveCategoryPEOEnabledFlag | ENABLED_FLAG | — | — |
| 7 | ObjectiveCategoryPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 8 | ObjectiveCategoryPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ObjectiveCategoryPEOStartDateActive | START_DATE_ACTIVE | — | — |
| 10 | ObjectiveCategoryPEOSummaryFlag | SUMMARY_FLAG | — | — |
| 11 | ObjectiveCategoryPEOSupplierEnabledFlag | SUPPLIER_ENABLED_FLAG | — | — |
| 12 | ObjectiveCategoryPEOWebStatus | WEB_STATUS | — | — |
| 13 | ProgramCategoryPEOCategoryCode | CATEGORY_CODE | — | — |
| 14 | ProgramCategoryPEOCategoryContentCode | CATEGORY_CONTENT_CODE | — | — |
| 15 | ProgramCategoryPEOCategoryId | CATEGORY_ID | — | — |
| 16 | ProgramCategoryPEOCategoryName | CATEGORY_NAME | — | — |
| 17 | ProgramCategoryPEODescription | DESCRIPTION | — | — |
| 18 | ProgramCategoryPEOEnabledFlag | ENABLED_FLAG | — | — |
| 19 | ProgramCategoryPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 20 | ProgramCategoryPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | ProgramCategoryPEOStartDateActive | START_DATE_ACTIVE | — | — |
| 22 | ProgramCategoryPEOSummaryFlag | SUMMARY_FLAG | — | — |
| 23 | ProgramCategoryPEOSupplierEnabledFlag | SUPPLIER_ENABLED_FLAG | — | — |
| 24 | ProgramCategoryPEOWebStatus | WEB_STATUS | — | — |

### [[fnd_lookups|FND_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectiveStatusLookupPEOCreatedBy | CREATED_BY | — | — |
| 2 | ObjectiveStatusLookupPEOCreationDate | CREATION_DATE | — | — |
| 3 | ObjectiveStatusLookupPEODescription | DESCRIPTION | — | — |
| 4 | ObjectiveStatusLookupPEODisplaySequence | DISPLAY_SEQUENCE | — | — |
| 5 | ObjectiveStatusLookupPEOEnabledFlag | ENABLED_FLAG | — | — |
| 6 | ObjectiveStatusLookupPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 7 | ObjectiveStatusLookupPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | ObjectiveStatusLookupPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ObjectiveStatusLookupPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ObjectiveStatusLookupPEOLookupCode | LOOKUP_CODE | — | — |
| 11 | ObjectiveStatusLookupPEOLookupType | LOOKUP_TYPE | — | — |
| 12 | ObjectiveStatusLookupPEOMeaning | MEANING | — | ✅ |
| 13 | ObjectiveStatusLookupPEOStartDateActive | START_DATE_ACTIVE | — | — |
| 14 | ObjectiveTypeLookupPEOCreatedBy | CREATED_BY | — | — |
| 15 | ObjectiveTypeLookupPEOCreationDate | CREATION_DATE | — | — |
| 16 | ObjectiveTypeLookupPEODescription | DESCRIPTION | — | — |
| 17 | ObjectiveTypeLookupPEODisplaySequence | DISPLAY_SEQUENCE | — | — |
| 18 | ObjectiveTypeLookupPEOEnabledFlag | ENABLED_FLAG | — | — |
| 19 | ObjectiveTypeLookupPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 20 | ObjectiveTypeLookupPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 21 | ObjectiveTypeLookupPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 22 | ObjectiveTypeLookupPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 23 | ObjectiveTypeLookupPEOLookupCode | LOOKUP_CODE | — | — |
| 24 | ObjectiveTypeLookupPEOLookupType | LOOKUP_TYPE | — | — |
| 25 | ObjectiveTypeLookupPEOMeaning | MEANING | — | ✅ |
| 26 | ObjectiveTypeLookupPEOStartDateActive | START_DATE_ACTIVE | — | — |
| 27 | ProgramPhaseLookupPEOCreatedBy | CREATED_BY | — | — |
| 28 | ProgramPhaseLookupPEOCreationDate | CREATION_DATE | — | — |
| 29 | ProgramPhaseLookupPEODescription | DESCRIPTION | — | — |
| 30 | ProgramPhaseLookupPEODisplaySequence | DISPLAY_SEQUENCE | — | — |
| 31 | ProgramPhaseLookupPEOEnabledFlag | ENABLED_FLAG | — | — |
| 32 | ProgramPhaseLookupPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 33 | ProgramPhaseLookupPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 34 | ProgramPhaseLookupPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 35 | ProgramPhaseLookupPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 36 | ProgramPhaseLookupPEOLookupCode | LOOKUP_CODE | — | — |
| 37 | ProgramPhaseLookupPEOLookupType | LOOKUP_TYPE | — | — |
| 38 | ProgramPhaseLookupPEOMeaning | MEANING | — | ✅ |
| 39 | ProgramPhaseLookupPEOStartDateActive | START_DATE_ACTIVE | — | — |
| 40 | ProgramStatusLookupPEOCreatedBy | CREATED_BY | — | — |
| 41 | ProgramStatusLookupPEOCreationDate | CREATION_DATE | — | — |
| 42 | ProgramStatusLookupPEODescription | DESCRIPTION | — | — |
| 43 | ProgramStatusLookupPEODisplaySequence | DISPLAY_SEQUENCE | — | — |
| 44 | ProgramStatusLookupPEOEnabledFlag | ENABLED_FLAG | — | — |
| 45 | ProgramStatusLookupPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 46 | ProgramStatusLookupPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 47 | ProgramStatusLookupPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 48 | ProgramStatusLookupPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 49 | ProgramStatusLookupPEOLookupCode | LOOKUP_CODE | — | — |
| 50 | ProgramStatusLookupPEOLookupType | LOOKUP_TYPE | — | — |
| 51 | ProgramStatusLookupPEOMeaning | MEANING | — | — |
| 52 | ProgramStatusLookupPEOStartDateActive | START_DATE_ACTIVE | — | — |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProgramDailyConversionTypePEOConversionType | CONVERSION_TYPE | — | — |
| 2 | ProgramDailyConversionTypePEODescription | DESCRIPTION | — | — |
| 3 | ProgramDailyConversionTypePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | ProgramDailyConversionTypePEOUserConversionType | USER_CONVERSION_TYPE | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegHeaderPersonNamePEODisplayName | DISPLAY_NAME | — | ✅ |
| 2 | NegHeaderPersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | NegHeaderPersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | NegHeaderPersonNamePEOFullName | FULL_NAME | — | — |
| 5 | NegHeaderPersonNamePEOListName | LIST_NAME | — | — |
| 6 | NegHeaderPersonNamePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | NegHeaderPersonNamePEOPersonId | PERSON_ID | — | — |
| 8 | NegHeaderPersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |
| 9 | ObjectivePersonNamePEODisplayName | DISPLAY_NAME | — | ✅ |
| 10 | ObjectivePersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 11 | ObjectivePersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 12 | ObjectivePersonNamePEOFullName | FULL_NAME | — | — |
| 13 | ObjectivePersonNamePEOListName | LIST_NAME | — | — |
| 14 | ObjectivePersonNamePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | ObjectivePersonNamePEOPersonId | PERSON_ID | — | — |
| 16 | ObjectivePersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |
| 17 | ProgramPersonNamePEODisplayName | DISPLAY_NAME | — | ✅ |
| 18 | ProgramPersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 19 | ProgramPersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 20 | ProgramPersonNamePEOFullName | FULL_NAME | — | — |
| 21 | ProgramPersonNamePEOListName | LIST_NAME | — | — |
| 22 | ProgramPersonNamePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | ProgramPersonNamePEOPersonId | PERSON_ID | — | — |
| 24 | ProgramPersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |

### [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationHeaderPEOAuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 2 | NegotiationHeaderPEOAuctionStatus | AUCTION_STATUS | — | — |
| 3 | NegotiationHeaderPEOAuctionTitle | AUCTION_TITLE | — | ✅ |
| 4 | NegotiationHeaderPEOAwardCompleteDate | AWARD_COMPLETE_DATE | — | — |
| 5 | NegotiationHeaderPEOAwardDate | AWARD_DATE | — | — |
| 6 | NegotiationHeaderPEOAwardStatus | AWARD_STATUS | — | — |
| 7 | NegotiationHeaderPEOCancelDate | CANCEL_DATE | — | — |
| 8 | NegotiationHeaderPEOCreatedBy | CREATED_BY | — | — |
| 9 | NegotiationHeaderPEOCreationDate | CREATION_DATE | — | — |
| 10 | NegotiationHeaderPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 11 | NegotiationHeaderPEODescription | DESCRIPTION | — | — |
| 12 | NegotiationHeaderPEODoctypeId | DOCTYPE_ID | — | ✅ |
| 13 | NegotiationHeaderPEODocumentNumber | DOCUMENT_NUMBER | — | ✅ |
| 14 | NegotiationHeaderPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 15 | NegotiationHeaderPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | NegotiationHeaderPEONegApprovalStatus | NEG_APPROVAL_STATUS | — | — |
| 17 | NegotiationHeaderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | NegotiationHeaderPEOPersonId | PERSON_ID | — | — |
| 19 | NegotiationHeaderPEOPrcBuId | PRC_BU_ID | — | — |
| 20 | NegotiationHeaderPEOSealedAuctionStatus | SEALED_AUCTION_STATUS | — | — |
| 21 | NegotiationHeaderPEOStyleId | STYLE_ID | — | ✅ |

### [[pon_neg_agg_to_obj_otbi_v|PON_NEG_AGG_TO_OBJ_OTBI_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationAggToObjPEOAwardAmountByObj | AWARD_AMOUNT_BY_OBJ | — | — |
| 2 | NegotiationAggToObjPEOObjectiveHeaderId | OBJECTIVE_HEADER_ID | — | — |
| 3 | NegotiationAggToObjPEOPlannedCurrentSpendByObj | PLANNED_CURRENT_SPEND_BY_OBJ | — | — |
| 4 | NegotiationAggToObjPEOPlannedSavingGoalsByObj | PLANNED_SAVING_GOALS_BY_OBJ | — | — |
| 5 | NegotiationAggToObjPEOPlannedTargetSpendByObj | PLANNED_TARGET_SPEND_BY_OBJ | — | — |
| 6 | NegotiationAggToObjPEOProgramHeaderId | PROGRAM_HEADER_ID | — | — |

### [[pon_neg_agg_to_prog_otbi_v|PON_NEG_AGG_TO_PROG_OTBI_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationAggToProgPEOAwardAmountByProg | AWARD_AMOUNT_BY_PROG | — | — |
| 2 | NegotiationAggToProgPEOPlannedCurrentSpendByProg | PLANNED_CURRENT_SPEND_BY_PROG | — | — |
| 3 | NegotiationAggToProgPEOPlannedSavingGoalsByProg | PLANNED_SAVING_GOALS_BY_PROG | — | — |
| 4 | NegotiationAggToProgPEOPlannedTargetSpendByProg | PLANNED_TARGET_SPEND_BY_PROG | — | — |
| 5 | NegotiationAggToProgPEOProgramHeaderId | PROGRAM_HEADER_ID | — | — |

### [[pon_objective_negotiations|PON_OBJECTIVE_NEGOTIATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectiveNegotiationPEOAuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 2 | ObjectiveNegotiationPEOAwardAmount | AWARD_AMOUNT | — | ✅ |
| 3 | ObjectiveNegotiationPEOCreatedBy | CREATED_BY | — | — |
| 4 | ObjectiveNegotiationPEOCreationDate | CREATION_DATE | — | — |
| 5 | ObjectiveNegotiationPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 6 | ObjectiveNegotiationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ObjectiveNegotiationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ObjectiveNegotiationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ObjectiveNegotiationPEOObjectiveHeaderId | OBJECTIVE_HEADER_ID | — | — |
| 10 | ObjectiveNegotiationPEOObjectiveNegotiationId | OBJECTIVE_NEGOTIATION_ID | 🔑 | ✅ |
| 11 | ObjectiveNegotiationPEOOverrideFlag | OVERRIDE_FLAG | — | — |
| 12 | ObjectiveNegotiationPEOPlannedCurrentSpend | PLANNED_CURRENT_SPEND | — | — |
| 13 | ObjectiveNegotiationPEOPlannedSavings | PLANNED_SAVINGS | — | — |
| 14 | ObjectiveNegotiationPEOPlannedSavingsPercent | PLANNED_SAVINGS_PERCENT | — | — |
| 15 | ObjectiveNegotiationPEOPlannedTargetSpend | PLANNED_TARGET_SPEND | — | — |
| 16 | ObjectiveNegotiationPEOPlannedTitle | PLANNED_TITLE | — | ✅ |
| 17 | ObjectiveNegotiationPEOProgramHeaderId | PROGRAM_HEADER_ID | — | — |

### [[pon_obj_agg_to_prog_otbi_v|PON_OBJ_AGG_TO_PROG_OTBI_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectiveAggToProgPEOObjBsCurrentSpendByProg | OBJ_BS_CURRENT_SPEND_BY_PROG | — | — |
| 2 | ObjectiveAggToProgPEOObjBsSavingsGoalByProg | OBJ_BS_SAVINGS_GOAL_BY_PROG | — | — |
| 3 | ObjectiveAggToProgPEOObjBsTargetSpendByProg | OBJ_BS_TARGET_SPEND_BY_PROG | — | — |
| 4 | ObjectiveAggToProgPEOProgramHeaderId | PROGRAM_HEADER_ID | — | — |

### [[pon_program_headers|PON_PROGRAM_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProgramHeaderPEOCategoryId | CATEGORY_ID | — | — |
| 2 | ProgramHeaderPEOComments | COMMENTS | — | ✅ |
| 3 | ProgramHeaderPEOCreatedBy | CREATED_BY | — | — |
| 4 | ProgramHeaderPEOCreationDate | CREATION_DATE | — | — |
| 5 | ProgramHeaderPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 6 | ProgramHeaderPEOCurrentSpend | CURRENT_SPEND | — | ✅ |
| 7 | ProgramHeaderPEOEndDate | END_DATE | — | ✅ |
| 8 | ProgramHeaderPEOGlobalProgramFlag | GLOBAL_PROGRAM_FLAG | — | ✅ |
| 9 | ProgramHeaderPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 10 | ProgramHeaderPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | ProgramHeaderPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | ProgramHeaderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | ProgramHeaderPEOPersonId | PERSON_ID | — | — |
| 14 | ProgramHeaderPEOPrcBuId | PRC_BU_ID | — | — |
| 15 | ProgramHeaderPEOProgramHeaderId | PROGRAM_HEADER_ID | 🔑 | ✅ |
| 16 | ProgramHeaderPEOProgramPhase | PROGRAM_PHASE | — | — |
| 17 | ProgramHeaderPEOProgramStatus | PROGRAM_STATUS | — | — |
| 18 | ProgramHeaderPEOPurchasingCatFlag | PURCHASING_CAT_FLAG | — | — |
| 19 | ProgramHeaderPEORateDate | RATE_DATE | — | ✅ |
| 20 | ProgramHeaderPEORateType | RATE_TYPE | — | — |
| 21 | ProgramHeaderPEOSavings | SAVINGS | — | ✅ |
| 22 | ProgramHeaderPEOSavingsPercent | SAVINGS_PERCENT | — | — |
| 23 | ProgramHeaderPEOStartDate | START_DATE | — | ✅ |
| 24 | ProgramHeaderPEOSynopsis | SYNOPSIS | — | ✅ |
| 25 | ProgramHeaderPEOTargetSpend | TARGET_SPEND | — | ✅ |
| 26 | ProgramHeaderPEOTitle | TITLE | — | ✅ |

### [[pon_program_objectives|PON_PROGRAM_OBJECTIVES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProgramObjectivePEOCategoryId | CATEGORY_ID | — | — |
| 2 | ProgramObjectivePEOComments | COMMENTS | — | ✅ |
| 3 | ProgramObjectivePEOCreatedBy | CREATED_BY | — | — |
| 4 | ProgramObjectivePEOCreationDate | CREATION_DATE | — | — |
| 5 | ProgramObjectivePEOCurrentSpend | CURRENT_SPEND | — | ✅ |
| 6 | ProgramObjectivePEODescription | DESCRIPTION | — | ✅ |
| 7 | ProgramObjectivePEOEndDate | END_DATE | — | ✅ |
| 8 | ProgramObjectivePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 9 | ProgramObjectivePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | ProgramObjectivePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | ProgramObjectivePEOName | NAME | — | ✅ |
| 12 | ProgramObjectivePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | ProgramObjectivePEOObjectiveHeaderId | OBJECTIVE_HEADER_ID | 🔑 | ✅ |
| 14 | ProgramObjectivePEOObjectiveType | OBJECTIVE_TYPE | — | — |
| 15 | ProgramObjectivePEOPersonId | PERSON_ID | — | — |
| 16 | ProgramObjectivePEOProgramHeaderId | PROGRAM_HEADER_ID | — | — |
| 17 | ProgramObjectivePEOPurchasingCatFlag | PURCHASING_CAT_FLAG | — | — |
| 18 | ProgramObjectivePEORollUpFlag | ROLL_UP_FLAG | — | ✅ |
| 19 | ProgramObjectivePEOSavings | SAVINGS | — | ✅ |
| 20 | ProgramObjectivePEOSavingsPercent | SAVINGS_PERCENT | — | — |
| 21 | ProgramObjectivePEOStartDate | START_DATE | — | ✅ |
| 22 | ProgramObjectivePEOStatus | STATUS | — | — |
| 23 | ProgramObjectivePEOTargetSpend | TARGET_SPEND | — | ✅ |

### [[por_browse_categories_vl|POR_BROWSE_CATEGORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectiveBrowseCategoryPEOCategoryDescription | CATEGORY_DESCRIPTION | — | — |
| 2 | ObjectiveBrowseCategoryPEOCategoryId | CATEGORY_ID | — | — |
| 3 | ObjectiveBrowseCategoryPEOCategoryName | CATEGORY_NAME | — | — |
| 4 | ObjectiveBrowseCategoryPEOCreatedBy | CREATED_BY | — | — |
| 5 | ObjectiveBrowseCategoryPEOCreationDate | CREATION_DATE | — | — |
| 6 | ObjectiveBrowseCategoryPEOImageUrl | IMAGE_URL | — | — |
| 7 | ObjectiveBrowseCategoryPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | ObjectiveBrowseCategoryPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ObjectiveBrowseCategoryPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ObjectiveBrowseCategoryPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ObjectiveBrowseCategoryPEOType | TYPE | — | — |
| 12 | ProgramBrowseCategoryPEOCategoryDescription | CATEGORY_DESCRIPTION | — | — |
| 13 | ProgramBrowseCategoryPEOCategoryId | CATEGORY_ID | — | — |
| 14 | ProgramBrowseCategoryPEOCategoryName | CATEGORY_NAME | — | — |
| 15 | ProgramBrowseCategoryPEOCreatedBy | CREATED_BY | — | — |
| 16 | ProgramBrowseCategoryPEOCreationDate | CREATION_DATE | — | — |
| 17 | ProgramBrowseCategoryPEOImageUrl | IMAGE_URL | — | — |
| 18 | ProgramBrowseCategoryPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 19 | ProgramBrowseCategoryPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | ProgramBrowseCategoryPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 21 | ProgramBrowseCategoryPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | ProgramBrowseCategoryPEOType | TYPE | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
