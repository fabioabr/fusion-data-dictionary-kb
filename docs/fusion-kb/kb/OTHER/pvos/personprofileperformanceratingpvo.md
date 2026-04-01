---
id: DOC-OTHER-PVO-PersonProfilePerformanceRatingPVO
doc_type: system-doc
title: "PersonProfilePerformanceRatingPVO — PVO Cross-Module"
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
  - PersonProfilePerformanceRatingPVO
  - personprofileperformanceratingpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonProfilePerformanceRatingPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Person Profile Performance Rating. Acessa as tabelas: HRT_BI_PERF_RATING_ITEMS_V, HRT_CONTENT_TYPES_B, HRT_CONTENT_TYPES_TL (+11).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileCoreAM.PersonProfilePerformanceRatingPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 195 | 14 | 2 | 37 | 19% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_bi_perf_rating_items_v|HRT_BI_PERF_RATING_ITEMS_V]] — 96 atributos (1 PKs, 16 BICC)
- [[hrt_content_types_b|HRT_CONTENT_TYPES_B]] — 6 atributos (2 BICC)
- [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]] — 6 atributos (3 BICC)
- [[hrt_profiles_b|HRT_PROFILES_B]] — 14 atributos (1 PKs, 2 BICC)
- [[hrt_profiles_tl|HRT_PROFILES_TL]] — 7 atributos (1 BICC)
- [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]] — 4 atributos (2 BICC)
- [[hrt_rating_categories_b|HRT_RATING_CATEGORIES_B]] — 6 atributos (1 BICC)
- [[hrt_rating_categories_tl|HRT_RATING_CATEGORIES_TL]] — 7 atributos (2 BICC)
- [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]] — 20 atributos (1 BICC)
- [[hrt_rating_levels_tl|HRT_RATING_LEVELS_TL]] — 7 atributos (1 BICC)
- [[hrt_rating_models_b|HRT_RATING_MODELS_B]] — 7 atributos (1 BICC)
- [[hrt_rating_models_tl|HRT_RATING_MODELS_TL]] — 6 atributos (1 BICC)
- [[hrt_sources_b|HRT_SOURCES_B]] — 4 atributos (2 BICC)
- [[hrt_sources_tl|HRT_SOURCES_TL]] — 5 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hrt_bi_perf_rating_items_v|HRT_BI_PERF_RATING_ITEMS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContextName | CONTEXT_NAME | — | — |
| 2 | Importance | IMPORTANCE | — | — |
| 3 | InterestLevel | INTEREST_LEVEL | — | — |
| 4 | ItemClob1 | ITEM_CLOB_1 | — | — |
| 5 | ItemClob2 | ITEM_CLOB_2 | — | — |
| 6 | ItemClob3 | ITEM_CLOB_3 | — | — |
| 7 | ItemClob4 | ITEM_CLOB_4 | — | — |
| 8 | ItemClob5 | ITEM_CLOB_5 | — | — |
| 9 | ItemDate1 | ITEM_DATE_1 | — | — |
| 10 | ItemDate10 | ITEM_DATE_10 | — | — |
| 11 | ItemDate2 | ITEM_DATE_2 | — | — |
| 12 | ItemDate3 | ITEM_DATE_3 | — | — |
| 13 | ItemDate4 | ITEM_DATE_4 | — | — |
| 14 | ItemDate5 | ITEM_DATE_5 | — | — |
| 15 | ItemDate6 | ITEM_DATE_6 | — | — |
| 16 | ItemDate7 | ITEM_DATE_7 | — | — |
| 17 | ItemDate8 | ITEM_DATE_8 | — | — |
| 18 | ItemDate9 | ITEM_DATE_9 | — | — |
| 19 | ItemDecimal1 | ITEM_DECIMAL_1 | — | ✅ |
| 20 | ItemDecimal2 | ITEM_DECIMAL_2 | — | — |
| 21 | ItemDecimal3 | ITEM_DECIMAL_3 | — | — |
| 22 | ItemDecimal4 | ITEM_DECIMAL_4 | — | — |
| 23 | ItemDecimal5 | ITEM_DECIMAL_5 | — | — |
| 24 | ItemNumber1 | ITEM_NUMBER_1 | — | ✅ |
| 25 | ItemNumber10 | ITEM_NUMBER_10 | — | — |
| 26 | ItemNumber2 | ITEM_NUMBER_2 | — | ✅ |
| 27 | ItemNumber3 | ITEM_NUMBER_3 | — | — |
| 28 | ItemNumber4 | ITEM_NUMBER_4 | — | — |
| 29 | ItemNumber5 | ITEM_NUMBER_5 | — | — |
| 30 | ItemNumber6 | ITEM_NUMBER_6 | — | — |
| 31 | ItemNumber7 | ITEM_NUMBER_7 | — | — |
| 32 | ItemNumber8 | ITEM_NUMBER_8 | — | — |
| 33 | ItemNumber9 | ITEM_NUMBER_9 | — | — |
| 34 | ItemText20001 | ITEM_TEXT2000_1 | — | ✅ |
| 35 | ItemText20002 | ITEM_TEXT2000_2 | — | — |
| 36 | ItemText20003 | ITEM_TEXT2000_3 | — | — |
| 37 | ItemText20004 | ITEM_TEXT2000_4 | — | — |
| 38 | ItemText20005 | ITEM_TEXT2000_5 | — | — |
| 39 | ItemText2401 | ITEM_TEXT240_1 | — | ✅ |
| 40 | ItemText24010 | ITEM_TEXT240_10 | — | — |
| 41 | ItemText24011 | ITEM_TEXT240_11 | — | — |
| 42 | ItemText24012 | ITEM_TEXT240_12 | — | — |
| 43 | ItemText24013 | ITEM_TEXT240_13 | — | — |
| 44 | ItemText24014 | ITEM_TEXT240_14 | — | — |
| 45 | ItemText24015 | ITEM_TEXT240_15 | — | — |
| 46 | ItemText2402 | ITEM_TEXT240_2 | — | — |
| 47 | ItemText2403 | ITEM_TEXT240_3 | — | — |
| 48 | ItemText2404 | ITEM_TEXT240_4 | — | — |
| 49 | ItemText2405 | ITEM_TEXT240_5 | — | — |
| 50 | ItemText2406 | ITEM_TEXT240_6 | — | — |
| 51 | ItemText2407 | ITEM_TEXT240_7 | — | — |
| 52 | ItemText2408 | ITEM_TEXT240_8 | — | — |
| 53 | ItemText2409 | ITEM_TEXT240_9 | — | — |
| 54 | ItemText301 | ITEM_TEXT30_1 | — | — |
| 55 | ItemText3010 | ITEM_TEXT30_10 | — | — |
| 56 | ItemText3011 | ITEM_TEXT30_11 | — | — |
| 57 | ItemText3012 | ITEM_TEXT30_12 | — | — |
| 58 | ItemText3013 | ITEM_TEXT30_13 | — | — |
| 59 | ItemText3014 | ITEM_TEXT30_14 | — | — |
| 60 | ItemText3015 | ITEM_TEXT30_15 | — | — |
| 61 | ItemText302 | ITEM_TEXT30_2 | — | — |
| 62 | ItemText303 | ITEM_TEXT30_3 | — | — |
| 63 | ItemText304 | ITEM_TEXT30_4 | — | — |
| 64 | ItemText305 | ITEM_TEXT30_5 | — | — |
| 65 | ItemText306 | ITEM_TEXT30_6 | — | — |
| 66 | ItemText307 | ITEM_TEXT30_7 | — | — |
| 67 | ItemText308 | ITEM_TEXT30_8 | — | — |
| 68 | ItemText309 | ITEM_TEXT30_9 | — | — |
| 69 | Mandatory | MANDATORY | — | — |
| 70 | ProfileItemPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 71 | ProfileItemPEOContentItemId | CONTENT_ITEM_ID | — | — |
| 72 | ProfileItemPEOContentTypeId | CONTENT_TYPE_ID | — | ✅ |
| 73 | ProfileItemPEOCountryId | COUNTRY_ID | — | — |
| 74 | ProfileItemPEODateFrom | DATE_FROM | — | ✅ |
| 75 | ProfileItemPEODateTo | DATE_TO | — | ✅ |
| 76 | ProfileItemPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 77 | ProfileItemPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 78 | ProfileItemPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 79 | ProfileItemPEOParentProfileItemId | PARENT_PROFILE_ITEM_ID | — | — |
| 80 | ProfileItemPEOProfileId | PROFILE_ID | — | — |
| 81 | ProfileItemPEOProfileItemId | PROFILE_ITEM_ID | 🔑 | ✅ |
| 82 | ProfileItemPEORatingLevelId1 | RATING_LEVEL_ID1 | — | ✅ |
| 83 | ProfileItemPEORatingLevelId2 | RATING_LEVEL_ID2 | — | — |
| 84 | ProfileItemPEORatingLevelId3 | RATING_LEVEL_ID3 | — | — |
| 85 | ProfileItemPEORatingModelId1 | RATING_MODEL_ID1 | — | ✅ |
| 86 | ProfileItemPEORatingModelId2 | RATING_MODEL_ID2 | — | — |
| 87 | ProfileItemPEORatingModelId3 | RATING_MODEL_ID3 | — | — |
| 88 | ProfileItemPEOStateProvinceId | STATE_PROVINCE_ID | — | — |
| 89 | QualifierId1 | QUALIFIER_ID1 | — | — |
| 90 | QualifierId2 | QUALIFIER_ID2 | — | — |
| 91 | SectionId | SECTION_ID | — | ✅ |
| 92 | SourceId | SOURCE_ID | — | ✅ |
| 93 | SourceKey1 | SOURCE_KEY1 | — | ✅ |
| 94 | SourceKey2 | SOURCE_KEY2 | — | — |
| 95 | SourceKey3 | SOURCE_KEY3 | — | — |
| 96 | SourceType | SOURCE_TYPE | — | ✅ |

### [[hrt_content_types_b|HRT_CONTENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentTypeBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ContentTypeBPEOContentTypeId | CONTENT_TYPE_ID | — | ✅ |
| 3 | ContentTypeBPEOContextName | CONTEXT_NAME | — | — |
| 4 | ContentTypeBPEOFreeFormFlag | FREE_FORM_FLAG | — | — |
| 5 | ContentTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ContentTypeBPEOModuleId | MODULE_ID | — | — |

### [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ContentDescription | CONTENT_DESCRIPTION | — | ✅ |
| 3 | ContentTypeId | CONTENT_TYPE_ID | — | — |
| 4 | ContentTypeName | CONTENT_TYPE_NAME | — | ✅ |
| 5 | ContentTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | Language1 | LANGUAGE | — | — |

### [[hrt_profiles_b|HRT_PROFILES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | ProfileBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 8 | ProfileBPEOOwnerPersonId | OWNER_PERSON_ID | — | — |
| 9 | ProfileBPEOPartyId | PARTY_ID | — | — |
| 10 | ProfileBPEOPersonId | PERSON_ID | — | — |
| 11 | ProfileBPEOProfileCode | PROFILE_CODE | — | — |
| 12 | ProfileBPEOProfileId | PROFILE_ID | 🔑 | ✅ |
| 13 | ProfileBPEOProfileTypeId | PROFILE_TYPE_ID | — | — |
| 14 | ProfileBPEOProfileUsageCode | PROFILE_USAGE_CODE | — | — |

### [[hrt_profiles_tl|HRT_PROFILES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | — | — |
| 2 | ProfileTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | ProfileTranslationPEODescription | DESCRIPTION | — | — |
| 4 | ProfileTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ProfileTranslationPEOProfileId | PROFILE_ID | — | — |
| 6 | ProfileTranslationPEOSummary | SUMMARY | — | — |
| 7 | SourceLang | SOURCE_LANG | — | — |

### [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PTSBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | PTSSectionId1 | SECTION_ID | — | — |
| 3 | ProfileTypeSectionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | ProfileTypeSectionPEOName | NAME | — | ✅ |

### [[hrt_rating_categories_b|HRT_RATING_CATEGORIES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerfRtgCatBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 2 | PerfRtgCatCategoryId | CATEGORY_ID | — | — |
| 3 | PerfRtgCatLowerBoundary | LOWER_BOUNDARY | — | — |
| 4 | PerfRtgCatRatingModelId1 | RATING_MODEL_ID | — | — |
| 5 | PerfRtgCatUpperBoundary | UPPER_BOUNDARY | — | — |
| 6 | RatingCategoriesBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_rating_categories_tl|HRT_RATING_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerfRtgBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 2 | PerfRtgCategoryDescription | CATEGORY_DESCRIPTION | — | — |
| 3 | PerfRtgCategoryId | CATEGORY_ID | — | — |
| 4 | PerfRtgCategoryName | CATEGORY_NAME | — | — |
| 5 | PerfRtgLanguage3 | LANGUAGE | — | — |
| 6 | RtgCategoriesTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | RtgCategoriesTransltionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RtgLvlBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | RtgLvlCareerStrDev | CAREER_STR_DEV | — | — |
| 3 | RtgLvlCreatedBy1 | CREATED_BY | — | — |
| 4 | RtgLvlCreationDate1 | CREATION_DATE | — | — |
| 5 | RtgLvlDateFrom | DATE_FROM | — | — |
| 6 | RtgLvlDateTo | DATE_TO | — | — |
| 7 | RtgLvlFromPoints | FROM_POINTS | — | — |
| 8 | RtgLvlLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 9 | RtgLvlLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 10 | RtgLvlLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 11 | RtgLvlMaxRatingDistribution | MAX_RATING_DISTRIBUTION | — | — |
| 12 | RtgLvlMinRatingDistribution | MIN_RATING_DISTRIBUTION | — | — |
| 13 | RtgLvlModuleId | MODULE_ID | — | — |
| 14 | RtgLvlNumericRating | NUMERIC_RATING | — | — |
| 15 | RtgLvlObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 16 | RtgLvlRatingLevelCode | RATING_LEVEL_CODE | — | — |
| 17 | RtgLvlRatingLevelId | RATING_LEVEL_ID | — | — |
| 18 | RtgLvlReviewPoints | REVIEW_POINTS | — | — |
| 19 | RtgLvlStarRating | STAR_RATING | — | — |
| 20 | RtgLvlToPoints | TO_POINTS | — | — |

### [[hrt_rating_levels_tl|HRT_RATING_LEVELS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RTgLvlTLRatingDescription | RATING_DESCRIPTION | — | — |
| 2 | RtgLvlTLBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 3 | RtgLvlTLLanguage2 | LANGUAGE | — | — |
| 4 | RtgLvlTLRatingLevelId | RATING_LEVEL_ID | — | — |
| 5 | RtgLvlTLRatingShortDescr | RATING_SHORT_DESCR | — | — |
| 6 | RtgLvlTLReviewRatingDescr | REVIEW_RATING_DESCR | — | — |
| 7 | RtgLvlTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_rating_models_b|HRT_RATING_MODELS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerfRtgBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | PerfRtgDateFrom | DATE_FROM | — | — |
| 3 | PerfRtgDateTo | DATE_TO | — | — |
| 4 | PerfRtgModuleId | MODULE_ID | — | — |
| 5 | PerfRtgRatingModelCode | RATING_MODEL_CODE | — | — |
| 6 | PerfRtgRatingModelId | RATING_MODEL_ID | — | — |
| 7 | RatingModelBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_rating_models_tl|HRT_RATING_MODELS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | Language2 | LANGUAGE | — | — |
| 3 | RatingDescription | RATING_DESCRIPTION | — | — |
| 4 | RatingModelId | RATING_MODEL_ID | — | — |
| 5 | RatingName | RATING_NAME | — | — |
| 6 | RtgMdlTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_sources_b|HRT_SOURCES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SBPOBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | SBPOSourceCode | SOURCE_CODE | — | ✅ |
| 3 | SBPOSourceId1 | SOURCE_ID | — | — |
| 4 | SourcesBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_sources_tl|HRT_SOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | STLBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | STLLanguage2 | LANGUAGE | — | — |
| 3 | STLSourceDescription | SOURCE_DESCRIPTION | — | ✅ |
| 4 | STLSourceId1 | SOURCE_ID | — | — |
| 5 | SourcesTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
