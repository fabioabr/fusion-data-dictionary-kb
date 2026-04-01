---
id: DOC-PO-PVO-SourcingProgramHeaderPVO
doc_type: system-doc
title: "SourcingProgramHeaderPVO — PVO Purchasing"
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
  - SourcingProgramHeaderPVO
  - sourcingprogramheaderpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SourcingProgramHeaderPVO

## 📌 Visão Geral

Extrai os cabeçalhos de programas de sourcing, com objetivos estratégicos, categorias-alvo, responsáveis e status. Permite gestão de portfólio de iniciativas de sourcing e acompanhamento de savings.

**Caminho:** `FscmTopModelAM.PrcPonPublicViewAM.SourcingProgramHeaderPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 96 | 8 | 1 | 15 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[egp_categories_vl|EGP_CATEGORIES_VL]] — 12 atributos
- [[fnd_lookups|FND_LOOKUPS]] — 26 atributos (1 BICC)
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 4 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 8 atributos (1 BICC)
- [[pon_neg_agg_to_prog_otbi_v|PON_NEG_AGG_TO_PROG_OTBI_V]] — 5 atributos
- [[pon_obj_agg_to_prog_otbi_v|PON_OBJ_AGG_TO_PROG_OTBI_V]] — 4 atributos
- [[pon_program_headers|PON_PROGRAM_HEADERS]] — 26 atributos (1 PKs, 12 BICC)
- [[por_browse_categories_vl|POR_BROWSE_CATEGORIES_VL]] — 11 atributos

---

## ⚙️ Atributos

### [[egp_categories_vl|EGP_CATEGORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProgramCategoryPEOCategoryCode | CATEGORY_CODE | — | — |
| 2 | ProgramCategoryPEOCategoryContentCode | CATEGORY_CONTENT_CODE | — | — |
| 3 | ProgramCategoryPEOCategoryId | CATEGORY_ID | — | — |
| 4 | ProgramCategoryPEOCategoryName | CATEGORY_NAME | — | — |
| 5 | ProgramCategoryPEODescription | DESCRIPTION | — | — |
| 6 | ProgramCategoryPEOEnabledFlag | ENABLED_FLAG | — | — |
| 7 | ProgramCategoryPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 8 | ProgramCategoryPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ProgramCategoryPEOStartDateActive | START_DATE_ACTIVE | — | — |
| 10 | ProgramCategoryPEOSummaryFlag | SUMMARY_FLAG | — | — |
| 11 | ProgramCategoryPEOSupplierEnabledFlag | SUPPLIER_ENABLED_FLAG | — | — |
| 12 | ProgramCategoryPEOWebStatus | WEB_STATUS | — | — |

### [[fnd_lookups|FND_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProgramPhaseLookupPEOCreatedBy | CREATED_BY | — | — |
| 2 | ProgramPhaseLookupPEOCreationDate | CREATION_DATE | — | — |
| 3 | ProgramPhaseLookupPEODescription | DESCRIPTION | — | — |
| 4 | ProgramPhaseLookupPEODisplaySequence | DISPLAY_SEQUENCE | — | — |
| 5 | ProgramPhaseLookupPEOEnabledFlag | ENABLED_FLAG | — | — |
| 6 | ProgramPhaseLookupPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 7 | ProgramPhaseLookupPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | ProgramPhaseLookupPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ProgramPhaseLookupPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ProgramPhaseLookupPEOLookupCode | LOOKUP_CODE | — | — |
| 11 | ProgramPhaseLookupPEOLookupType | LOOKUP_TYPE | — | — |
| 12 | ProgramPhaseLookupPEOMeaning | MEANING | — | ✅ |
| 13 | ProgramPhaseLookupPEOStartDateActive | START_DATE_ACTIVE | — | — |
| 14 | ProgramStatusLookupPEOCreatedBy | CREATED_BY | — | — |
| 15 | ProgramStatusLookupPEOCreationDate | CREATION_DATE | — | — |
| 16 | ProgramStatusLookupPEODescription | DESCRIPTION | — | — |
| 17 | ProgramStatusLookupPEODisplaySequence | DISPLAY_SEQUENCE | — | — |
| 18 | ProgramStatusLookupPEOEnabledFlag | ENABLED_FLAG | — | — |
| 19 | ProgramStatusLookupPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 20 | ProgramStatusLookupPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 21 | ProgramStatusLookupPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 22 | ProgramStatusLookupPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 23 | ProgramStatusLookupPEOLookupCode | LOOKUP_CODE | — | — |
| 24 | ProgramStatusLookupPEOLookupType | LOOKUP_TYPE | — | — |
| 25 | ProgramStatusLookupPEOMeaning | MEANING | — | — |
| 26 | ProgramStatusLookupPEOStartDateActive | START_DATE_ACTIVE | — | — |

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
| 1 | ProgramPersonNamePEODisplayName | DISPLAY_NAME | — | ✅ |
| 2 | ProgramPersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | ProgramPersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | ProgramPersonNamePEOFullName | FULL_NAME | — | — |
| 5 | ProgramPersonNamePEOListName | LIST_NAME | — | — |
| 6 | ProgramPersonNamePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | ProgramPersonNamePEOPersonId | PERSON_ID | — | — |
| 8 | ProgramPersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |

### [[pon_neg_agg_to_prog_otbi_v|PON_NEG_AGG_TO_PROG_OTBI_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationAggToProgPEOAwardAmountByProg | AWARD_AMOUNT_BY_PROG | — | — |
| 2 | NegotiationAggToProgPEOPlannedCurrentSpendByProg | PLANNED_CURRENT_SPEND_BY_PROG | — | — |
| 3 | NegotiationAggToProgPEOPlannedSavingGoalsByProg | PLANNED_SAVING_GOALS_BY_PROG | — | — |
| 4 | NegotiationAggToProgPEOPlannedTargetSpendByProg | PLANNED_TARGET_SPEND_BY_PROG | — | — |
| 5 | NegotiationAggToProgPEOProgramHeaderId | PROGRAM_HEADER_ID | — | — |

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

### [[por_browse_categories_vl|POR_BROWSE_CATEGORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProgramBrowseCategoryPEOCategoryDescription | CATEGORY_DESCRIPTION | — | — |
| 2 | ProgramBrowseCategoryPEOCategoryId | CATEGORY_ID | — | — |
| 3 | ProgramBrowseCategoryPEOCategoryName | CATEGORY_NAME | — | — |
| 4 | ProgramBrowseCategoryPEOCreatedBy | CREATED_BY | — | — |
| 5 | ProgramBrowseCategoryPEOCreationDate | CREATION_DATE | — | — |
| 6 | ProgramBrowseCategoryPEOImageUrl | IMAGE_URL | — | — |
| 7 | ProgramBrowseCategoryPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | ProgramBrowseCategoryPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ProgramBrowseCategoryPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ProgramBrowseCategoryPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ProgramBrowseCategoryPEOType | TYPE | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
