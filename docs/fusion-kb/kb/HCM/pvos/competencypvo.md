---
id: DOC-HCM-PVO-CompetencyPVO
doc_type: system-doc
title: "CompetencyPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - CompetencyPVO
  - competencypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CompetencyPVO

## 📌 Visão Geral

Consolida competencias de perfis de talento com qualificadores, tipos de conteudo e secoes. View Object principal para gestao de competencias de colaboradores.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileCoreAM.CompetencyPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 244 | 12 | 1 | 69 | 28% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_bi_competency_items_v|HRT_BI_COMPETENCY_ITEMS_V]] — 101 atributos (1 PKs, 33 BICC)
- [[hrt_content_types_b|HRT_CONTENT_TYPES_B]] — 5 atributos (1 BICC)
- [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]] — 6 atributos (2 BICC)
- [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]] — 4 atributos (2 BICC)
- [[hrt_qualifiers_b|HRT_QUALIFIERS_B]] — 6 atributos (3 BICC)
- [[hrt_qualifiers_tl|HRT_QUALIFIERS_TL]] — 6 atributos (3 BICC)
- [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]] — 46 atributos (6 BICC)
- [[hrt_rating_levels_tl|HRT_RATING_LEVELS_TL]] — 29 atributos (8 BICC)
- [[hrt_rating_models_b|HRT_RATING_MODELS_B]] — 13 atributos (3 BICC)
- [[hrt_rating_models_tl|HRT_RATING_MODELS_TL]] — 21 atributos (7 BICC)
- [[hrt_sources_b|HRT_SOURCES_B]] — 3 atributos
- [[hrt_sources_tl|HRT_SOURCES_TL]] — 4 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hrt_bi_competency_items_v|HRT_BI_COMPETENCY_ITEMS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContextName | CONTEXT_NAME | — | — |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | Importance | IMPORTANCE | — | ✅ |
| 5 | InterestLevel | INTEREST_LEVEL | — | ✅ |
| 6 | ItemClob1 | ITEM_CLOB_1 | — | — |
| 7 | ItemClob2 | ITEM_CLOB_2 | — | — |
| 8 | ItemClob3 | ITEM_CLOB_3 | — | — |
| 9 | ItemClob4 | ITEM_CLOB_4 | — | — |
| 10 | ItemClob5 | ITEM_CLOB_5 | — | — |
| 11 | ItemDate1 | ITEM_DATE_1 | — | — |
| 12 | ItemDate10 | ITEM_DATE_10 | — | — |
| 13 | ItemDate2 | ITEM_DATE_2 | — | — |
| 14 | ItemDate5 | ITEM_DATE_5 | — | — |
| 15 | ItemDate6 | ITEM_DATE_6 | — | ✅ |
| 16 | ItemDate7 | ITEM_DATE_7 | — | — |
| 17 | ItemDate8 | ITEM_DATE_8 | — | — |
| 18 | ItemDate9 | ITEM_DATE_9 | — | — |
| 19 | ItemDecimal1 | ITEM_DECIMAL_1 | — | — |
| 20 | ItemDecimal2 | ITEM_DECIMAL_2 | — | ✅ |
| 21 | ItemDecimal3 | ITEM_DECIMAL_3 | — | — |
| 22 | ItemDecimal4 | ITEM_DECIMAL_4 | — | ✅ |
| 23 | ItemDecimal5 | ITEM_DECIMAL_5 | — | — |
| 24 | ItemNumber1 | ITEM_NUMBER_1 | — | ✅ |
| 25 | ItemNumber10 | ITEM_NUMBER_10 | — | — |
| 26 | ItemNumber1_Modl | ITEM_NUMBER_1 | — | — |
| 27 | ItemNumber2 | ITEM_NUMBER_2 | — | ✅ |
| 28 | ItemNumber2_Modl | ITEM_NUMBER_2 | — | — |
| 29 | ItemNumber3 | ITEM_NUMBER_3 | — | — |
| 30 | ItemNumber4 | ITEM_NUMBER_4 | — | — |
| 31 | ItemNumber5 | ITEM_NUMBER_5 | — | ✅ |
| 32 | ItemNumber6 | ITEM_NUMBER_6 | — | — |
| 33 | ItemNumber7 | ITEM_NUMBER_7 | — | — |
| 34 | ItemNumber8 | ITEM_NUMBER_8 | — | — |
| 35 | ItemNumber9 | ITEM_NUMBER_9 | — | — |
| 36 | ItemText20001 | ITEM_TEXT2000_1 | — | ✅ |
| 37 | ItemText20002 | ITEM_TEXT2000_2 | — | — |
| 38 | ItemText20003 | ITEM_TEXT2000_3 | — | — |
| 39 | ItemText20004 | ITEM_TEXT2000_4 | — | — |
| 40 | ItemText20005 | ITEM_TEXT2000_5 | — | — |
| 41 | ItemText2401 | ITEM_TEXT240_1 | — | ✅ |
| 42 | ItemText24010 | ITEM_TEXT240_10 | — | — |
| 43 | ItemText24011 | ITEM_TEXT240_11 | — | — |
| 44 | ItemText24012 | ITEM_TEXT240_12 | — | — |
| 45 | ItemText24013 | ITEM_TEXT240_13 | — | — |
| 46 | ItemText24014 | ITEM_TEXT240_14 | — | — |
| 47 | ItemText24015 | ITEM_TEXT240_15 | — | — |
| 48 | ItemText2402 | ITEM_TEXT240_2 | — | ✅ |
| 49 | ItemText2403 | ITEM_TEXT240_3 | — | — |
| 50 | ItemText2404 | ITEM_TEXT240_4 | — | ✅ |
| 51 | ItemText2405 | ITEM_TEXT240_5 | — | ✅ |
| 52 | ItemText2406 | ITEM_TEXT240_6 | — | — |
| 53 | ItemText2407 | ITEM_TEXT240_7 | — | — |
| 54 | ItemText2408 | ITEM_TEXT240_8 | — | — |
| 55 | ItemText2409 | ITEM_TEXT240_9 | — | — |
| 56 | ItemText301 | ITEM_TEXT30_1 | — | ✅ |
| 57 | ItemText3010 | ITEM_TEXT30_10 | — | — |
| 58 | ItemText3011 | ITEM_TEXT30_11 | — | — |
| 59 | ItemText3012 | ITEM_TEXT30_12 | — | — |
| 60 | ItemText3013 | ITEM_TEXT30_13 | — | — |
| 61 | ItemText3014 | ITEM_TEXT30_14 | — | — |
| 62 | ItemText3015 | ITEM_TEXT30_15 | — | — |
| 63 | ItemText302 | ITEM_TEXT30_2 | — | ✅ |
| 64 | ItemText303 | ITEM_TEXT30_3 | — | ✅ |
| 65 | ItemText304 | ITEM_TEXT30_4 | — | — |
| 66 | ItemText305 | ITEM_TEXT30_5 | — | — |
| 67 | ItemText306 | ITEM_TEXT30_6 | — | — |
| 68 | ItemText307 | ITEM_TEXT30_7 | — | — |
| 69 | ItemText308 | ITEM_TEXT30_8 | — | — |
| 70 | ItemText309 | ITEM_TEXT30_9 | — | — |
| 71 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 72 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 73 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 74 | Mandatory | MANDATORY | — | ✅ |
| 75 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 76 | ParentProfileItemId | PARENT_PROFILE_ITEM_ID | — | — |
| 77 | ProfileItemPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 78 | ProfileItemPEOContentItemId | CONTENT_ITEM_ID | — | — |
| 79 | ProfileItemPEOContentTypeId | CONTENT_TYPE_ID | — | ✅ |
| 80 | ProfileItemPEOCountryId | COUNTRY_ID | — | ✅ |
| 81 | ProfileItemPEODateFrom | DATE_FROM | — | ✅ |
| 82 | ProfileItemPEODateTo | DATE_TO | — | ✅ |
| 83 | ProfileItemPEOItemDate3 | ITEM_DATE_3 | — | ✅ |
| 84 | ProfileItemPEOItemDate4 | ITEM_DATE_4 | — | ✅ |
| 85 | ProfileItemPEOProfileId | PROFILE_ID | — | — |
| 86 | ProfileItemPEOProfileItemId | PROFILE_ITEM_ID | 🔑 | ✅ |
| 87 | ProfileItemPEORatingLevelId1 | RATING_LEVEL_ID1 | — | ✅ |
| 88 | ProfileItemPEORatingLevelId2 | RATING_LEVEL_ID2 | — | ✅ |
| 89 | ProfileItemPEORatingLevelId3 | RATING_LEVEL_ID3 | — | — |
| 90 | ProfileItemPEORatingModelId1 | RATING_MODEL_ID1 | — | ✅ |
| 91 | ProfileItemPEORatingModelId2 | RATING_MODEL_ID2 | — | ✅ |
| 92 | ProfileItemPEORatingModelId3 | RATING_MODEL_ID3 | — | — |
| 93 | ProfileItemPEOStateProvinceId | STATE_PROVINCE_ID | — | — |
| 94 | QualifierId1 | QUALIFIER_ID1 | — | ✅ |
| 95 | QualifierId2 | QUALIFIER_ID2 | — | ✅ |
| 96 | SectionId | SECTION_ID | — | ✅ |
| 97 | SourceId | SOURCE_ID | — | — |
| 98 | SourceKey1 | SOURCE_KEY1 | — | — |
| 99 | SourceKey2 | SOURCE_KEY2 | — | — |
| 100 | SourceKey3 | SOURCE_KEY3 | — | — |
| 101 | SourceType | SOURCE_TYPE | — | — |

### [[hrt_content_types_b|HRT_CONTENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentTypeBPEOBusinessGroup | BUSINESS_GROUP_ID | — | — |
| 2 | ContentTypeBPEOContentTypeId | CONTENT_TYPE_ID | — | — |
| 3 | ContentTypeBPEOContentTypeId1 | CONTENT_TYPE_ID | — | — |
| 4 | ContentTypeBPEOContextName1 | CONTEXT_NAME | — | — |
| 5 | ContentTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CntTypeTLPEOBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 2 | CntTypeTLPEOContentDescrip | CONTENT_DESCRIPTION | — | — |
| 3 | CntTypeTLPEOContentTypeId2 | CONTENT_TYPE_ID | — | — |
| 4 | CntTypeTLPEOContentTypeName | CONTENT_TYPE_NAME | — | ✅ |
| 5 | CntTypeTLPEOLanguage2 | LANGUAGE | — | — |
| 6 | CntTypeTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ProfileTypeSectionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | ProfileTypeSectionPEOName | NAME | — | ✅ |
| 4 | SectionId1 | SECTION_ID | — | — |

### [[hrt_qualifiers_b|HRT_QUALIFIERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 2 | QualifierSetId | QUALIFIER_SET_ID | — | — |
| 3 | QualifiersBEOBusinessGroupId9 | BUSINESS_GROUP_ID | — | — |
| 4 | QualifiersBEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | QualifiersBEOQualifierCode | QUALIFIER_CODE | — | ✅ |
| 6 | QualifiersBEOQualifierId | QUALIFIER_ID | — | ✅ |

### [[hrt_qualifiers_tl|HRT_QUALIFIERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QualifierTLPEOBusinessGroup | BUSINESS_GROUP_ID | — | — |
| 2 | QualifiersTLPEODescription | DESCRIPTION | — | ✅ |
| 3 | QualifiersTLPEOLanguage1 | LANGUAGE | — | ✅ |
| 4 | QualifiersTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | QualifiersTLPEOQualifierId | QUALIFIER_ID | — | — |
| 6 | QualifiersTLPEOSourceLang | SOURCE_LANG | — | — |

### [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId5 | BUSINESS_GROUP_ID | — | — |
| 2 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 3 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 4 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 5 | RLvlBPEOInterestBusinessGroup | BUSINESS_GROUP_ID | — | — |
| 6 | RLvlBPEOInterestCareerStrDev | CAREER_STR_DEV | — | — |
| 7 | RLvlBPEOInterestDateFrom | DATE_FROM | — | — |
| 8 | RLvlBPEOInterestDateTo | DATE_TO | — | — |
| 9 | RLvlBPEOInterestFromPoints | FROM_POINTS | — | — |
| 10 | RLvlBPEOInterestMaxRtgDistri | MAX_RATING_DISTRIBUTION | — | — |
| 11 | RLvlBPEOInterestMinRtgDistri | MIN_RATING_DISTRIBUTION | — | — |
| 12 | RLvlBPEOInterestModuleId | MODULE_ID | — | — |
| 13 | RLvlBPEOInterestNumericRating | NUMERIC_RATING | — | — |
| 14 | RLvlBPEOInterestRLCode | RATING_LEVEL_CODE | — | ✅ |
| 15 | RLvlBPEOInterestRatingLevelId | RATING_LEVEL_ID | — | — |
| 16 | RLvlBPEOInterestReviewPoints | REVIEW_POINTS | — | — |
| 17 | RLvlBPEOInterestStarRating | STAR_RATING | — | — |
| 18 | RLvlBPEOInterestToPoints | TO_POINTS | — | — |
| 19 | RLvlBPEOPerfRtgCareerStrDev | CAREER_STR_DEV | — | — |
| 20 | RLvlBPEOPerfRtgDateFrom | DATE_FROM | — | — |
| 21 | RLvlBPEOPerfRtgDateTo | DATE_TO | — | — |
| 22 | RLvlBPEOPerfRtgFromPoints | FROM_POINTS | — | — |
| 23 | RLvlBPEOPerfRtgLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | RLvlBPEOPerfRtgLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 25 | RLvlBPEOPerfRtgMaxRtgDistribu | MAX_RATING_DISTRIBUTION | — | — |
| 26 | RLvlBPEOPerfRtgMinRtgDistribu | MIN_RATING_DISTRIBUTION | — | — |
| 27 | RLvlBPEOPerfRtgModuleId | MODULE_ID | — | — |
| 28 | RLvlBPEOPerfRtgNumericRating | NUMERIC_RATING | — | — |
| 29 | RLvlBPEOPerfRtgRatingLevelId2 | RATING_LEVEL_ID | — | — |
| 30 | RLvlBPEOPerfRtgRatingModelId3 | RATING_MODEL_ID | — | — |
| 31 | RLvlBPEOPerfRtgReviewPoints | REVIEW_POINTS | — | — |
| 32 | RLvlBPEOPerfRtgStarRating | STAR_RATING | — | — |
| 33 | RLvlBPEOPerfRtgToPoints | TO_POINTS | — | — |
| 34 | RLvlBPEOProfBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 35 | RLvlBPEOProfDateFrom | DATE_FROM | — | — |
| 36 | RLvlBPEOProfDateTo | DATE_TO | — | — |
| 37 | RLvlBPEOProfLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 38 | RLvlBPEOProfMaxRtgDistributio | MAX_RATING_DISTRIBUTION | — | — |
| 39 | RLvlBPEOProfMinRtgDistributio | MIN_RATING_DISTRIBUTION | — | — |
| 40 | RLvlBPEOProfNumericRating | NUMERIC_RATING | — | — |
| 41 | RLvlBPEOProfRatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 42 | RLvlBPEOProfRatingLevelId | RATING_LEVEL_ID | — | — |
| 43 | RLvlBPEOProfRatingMdlId | RATING_MODEL_ID | — | — |
| 44 | RLvlBPEOProfReviewPoints | REVIEW_POINTS | — | — |
| 45 | RLvlBPEOProfStarRating | STAR_RATING | — | — |
| 46 | RLvlBPEOProfToPoints | TO_POINTS | — | — |

### [[hrt_rating_levels_tl|HRT_RATING_LEVELS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | BusinessGroupId6 | BUSINESS_GROUP_ID | — | — |
| 3 | Language | LANGUAGE | — | — |
| 4 | RLvlTLPEOInterLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | RLvlTLPEOInterRatingLevelId | RATING_LEVEL_ID | — | — |
| 6 | RLvlTLPEOInterReviewRtgDescr | REVIEW_RATING_DESCR | — | — |
| 7 | RLvlTLPEOInterRtgDescription | RATING_DESCRIPTION | — | — |
| 8 | RLvlTLPEOInterRtgShortDescr | RATING_SHORT_DESCR | — | ✅ |
| 9 | RLvlTLPEOInterSourceLang | SOURCE_LANG | — | — |
| 10 | RLvlTLPEOprofBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 11 | RLvlTLPEOprofLanguage | LANGUAGE | — | — |
| 12 | RLvlTLPEOprofLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | RLvlTLPEOprofRatingLevelId1 | RATING_LEVEL_ID | — | — |
| 14 | RLvlTLPEOprofRatingShortDescM | RATING_SHORT_DESCR | — | — |
| 15 | RLvlTLPEOprofRatingShortDescr | RATING_SHORT_DESCR | — | — |
| 16 | RLvlTLPEOprofReviewRtgDescr | REVIEW_RATING_DESCR | — | — |
| 17 | RLvlTLPEOprofReviewRtgDescrM | REVIEW_RATING_DESCR | — | — |
| 18 | RLvlTLPEOprofRtgDescription | RATING_DESCRIPTION | — | ✅ |
| 19 | RLvlTLPEOprofRtgDescriptionM | RATING_DESCRIPTION | — | ✅ |
| 20 | RLvlTLPEOprofSourceLang | SOURCE_LANG | — | — |
| 21 | RtgLvlTLPEOPerfLanguage2 | LANGUAGE | — | — |
| 22 | RtgLvlTLPEOPerfLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | RtgLvlTLPEOPerfRatingLevelId3 | RATING_LEVEL_ID | — | — |
| 24 | RtgLvlTLPEOPerfReviewRtgDescM | REVIEW_RATING_DESCR | — | — |
| 25 | RtgLvlTLPEOPerfReviewRtgDescr | REVIEW_RATING_DESCR | — | — |
| 26 | RtgLvlTLPEOPerfRtgDescriptioM | RATING_DESCRIPTION | — | ✅ |
| 27 | RtgLvlTLPEOPerfRtgDescription | RATING_DESCRIPTION | — | ✅ |
| 28 | RtgLvlTLPEOPerfRtgShortDesc | RATING_SHORT_DESCR | — | — |
| 29 | RtgLvlTLPEOPerfRtgShortDescrM | RATING_SHORT_DESCR | — | — |

### [[hrt_rating_models_b|HRT_RATING_MODELS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 2 | RMdlBPEOInterestLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | RMdlBPEOProfBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 4 | RMdlBPEOProfDateFrom | DATE_FROM | — | — |
| 5 | RMdlBPEOProfDateTo | DATE_TO | — | — |
| 6 | RMdlBPEOProfLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | RMdlBPEOProfRatingModelCode | RATING_MODEL_CODE | — | — |
| 8 | RMdlBPEOProfRatingModelId1 | RATING_MODEL_ID | — | — |
| 9 | RMdllBPEOPerfBusinessGroupId7 | BUSINESS_GROUP_ID | — | — |
| 10 | RMdllBPEOPerfLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | RMdllBPEOPerfRatingModelCode | RATING_MODEL_CODE | — | — |
| 12 | RMdllBPEOPerfRatingModelId4 | RATING_MODEL_ID | — | — |
| 13 | RatingModelId | RATING_MODEL_ID | — | — |

### [[hrt_rating_models_tl|HRT_RATING_MODELS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId4 | BUSINESS_GROUP_ID | — | — |
| 2 | BusinessGroupId8 | BUSINESS_GROUP_ID | — | — |
| 3 | Language1 | LANGUAGE | — | — |
| 4 | Language3 | LANGUAGE | — | — |
| 5 | RMdlTLBPEOProfLanguage1 | LANGUAGE | — | — |
| 6 | RMdlTLBPEOProfLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | RMdlTLBPEOProfRatingModelId2 | RATING_MODEL_ID | — | — |
| 8 | RMdlTLBPEOProfRatingNameM | RATING_NAME | — | ✅ |
| 9 | RMdlTLBPEOProfRtgDescription | RATING_DESCRIPTION | — | — |
| 10 | RMdlTLBPEOProfRtgName | RATING_NAME | — | ✅ |
| 11 | RMdlTLPEOInterBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 12 | RMdlTLPEOInterLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | RMdlTLPEOInterRatingModelId | RATING_MODEL_ID | — | — |
| 14 | RMdlTLPEOInterRatingName | RATING_NAME | — | — |
| 15 | RMdlTLPEOInterRtgDescription | RATING_DESCRIPTION | — | — |
| 16 | RMdlTLPEOInterSourceLang | SOURCE_LANG | — | — |
| 17 | RMdlTLPEOPerfLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | RMdlTLPEOPerfRatingModelId5 | RATING_MODEL_ID | — | — |
| 19 | RMdlTLPEOPerfRatingName1 | RATING_NAME | — | ✅ |
| 20 | RMdlTLPEOPerfRatingName1M | RATING_NAME | — | ✅ |
| 21 | RMdlTLPEOPerfRtgDescription | RATING_DESCRIPTION | — | — |

### [[hrt_sources_b|HRT_SOURCES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 2 | SourceCode | SOURCE_CODE | — | — |
| 3 | SourceId1 | SOURCE_ID | — | — |

### [[hrt_sources_tl|HRT_SOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId7 | BUSINESS_GROUP_ID | — | — |
| 2 | Language2 | LANGUAGE | — | — |
| 3 | SourceDescription | SOURCE_DESCRIPTION | — | ✅ |
| 4 | SourceId2 | SOURCE_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
