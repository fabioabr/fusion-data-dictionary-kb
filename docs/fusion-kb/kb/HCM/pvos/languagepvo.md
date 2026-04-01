---
id: DOC-HCM-PVO-LanguagePVO
doc_type: system-doc
title: "LanguagePVO — PVO Human Capital Management"
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
  - LanguagePVO
  - languagepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LanguagePVO

## 📌 Visão Geral

Consolida competências linguísticas no perfil do colaborador com ratings e tipos de conteúdo. Suporta gestão de idiomas e alocação internacional.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileCoreAM.LanguagePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 225 | 10 | 4 | 54 | 24% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_bi_language_items_v|HRT_BI_LANGUAGE_ITEMS_V]] — 99 atributos (2 PKs, 15 BICC)
- [[hrt_content_types_b|HRT_CONTENT_TYPES_B]] — 9 atributos (2 PKs, 4 BICC)
- [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]] — 5 atributos (3 BICC)
- [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]] — 4 atributos (3 BICC)
- [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]] — 42 atributos (6 BICC)
- [[hrt_rating_levels_tl|HRT_RATING_LEVELS_TL]] — 22 atributos (10 BICC)
- [[hrt_rating_models_b|HRT_RATING_MODELS_B]] — 18 atributos (6 BICC)
- [[hrt_rating_models_tl|HRT_RATING_MODELS_TL]] — 19 atributos (6 BICC)
- [[hrt_sources_b|HRT_SOURCES_B]] — 3 atributos
- [[hrt_sources_tl|HRT_SOURCES_TL]] — 4 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hrt_bi_language_items_v|HRT_BI_LANGUAGE_ITEMS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | Importance | IMPORTANCE | — | ✅ |
| 4 | InterestLevel | INTEREST_LEVEL | — | — |
| 5 | ItemClob2 | ITEM_CLOB_2 | — | — |
| 6 | ItemClob3 | ITEM_CLOB_3 | — | — |
| 7 | ItemClob4 | ITEM_CLOB_4 | — | — |
| 8 | ItemClob5 | ITEM_CLOB_5 | — | — |
| 9 | ItemDate1 | ITEM_DATE_1 | — | ✅ |
| 10 | ItemDate10 | ITEM_DATE_10 | — | — |
| 11 | ItemDate2 | ITEM_DATE_2 | — | — |
| 12 | ItemDate3 | ITEM_DATE_3 | — | — |
| 13 | ItemDate4 | ITEM_DATE_4 | — | — |
| 14 | ItemDate5 | ITEM_DATE_5 | — | — |
| 15 | ItemDate6 | ITEM_DATE_6 | — | — |
| 16 | ItemDate7 | ITEM_DATE_7 | — | — |
| 17 | ItemDate8 | ITEM_DATE_8 | — | — |
| 18 | ItemDate9 | ITEM_DATE_9 | — | — |
| 19 | ItemDecimal1 | ITEM_DECIMAL_1 | — | — |
| 20 | ItemDecimal2 | ITEM_DECIMAL_2 | — | — |
| 21 | ItemDecimal3 | ITEM_DECIMAL_3 | — | — |
| 22 | ItemDecimal4 | ITEM_DECIMAL_4 | — | — |
| 23 | ItemDecimal5 | ITEM_DECIMAL_5 | — | — |
| 24 | ItemNumber1 | ITEM_NUMBER_1 | — | — |
| 25 | ItemNumber10 | ITEM_NUMBER_10 | — | — |
| 26 | ItemNumber2 | ITEM_NUMBER_2 | — | — |
| 27 | ItemNumber3 | ITEM_NUMBER_3 | — | — |
| 28 | ItemNumber4 | ITEM_NUMBER_4 | — | — |
| 29 | ItemNumber5 | ITEM_NUMBER_5 | — | — |
| 30 | ItemNumber6 | ITEM_NUMBER_6 | — | — |
| 31 | ItemNumber7 | ITEM_NUMBER_7 | — | — |
| 32 | ItemNumber8 | ITEM_NUMBER_8 | — | — |
| 33 | ItemNumber9 | ITEM_NUMBER_9 | — | — |
| 34 | ItemText20001 | ITEM_TEXT2000_1 | — | — |
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
| 46 | ItemText2402 | ITEM_TEXT240_2 | — | ✅ |
| 47 | ItemText2403 | ITEM_TEXT240_3 | — | — |
| 48 | ItemText2404 | ITEM_TEXT240_4 | — | — |
| 49 | ItemText2405 | ITEM_TEXT240_5 | — | — |
| 50 | ItemText2406 | ITEM_TEXT240_6 | — | — |
| 51 | ItemText2407 | ITEM_TEXT240_7 | — | — |
| 52 | ItemText2408 | ITEM_TEXT240_8 | — | — |
| 53 | ItemText2409 | ITEM_TEXT240_9 | — | — |
| 54 | ItemText301 | ITEM_TEXT30_1 | — | ✅ |
| 55 | ItemText3010 | ITEM_TEXT30_10 | — | — |
| 56 | ItemText3011 | ITEM_TEXT30_11 | — | — |
| 57 | ItemText3012 | ITEM_TEXT30_12 | — | — |
| 58 | ItemText3013 | ITEM_TEXT30_13 | — | — |
| 59 | ItemText3014 | ITEM_TEXT30_14 | — | — |
| 60 | ItemText3015 | ITEM_TEXT30_15 | — | — |
| 61 | ItemText302 | ITEM_TEXT30_2 | — | ✅ |
| 62 | ItemText303 | ITEM_TEXT30_3 | — | ✅ |
| 63 | ItemText304 | ITEM_TEXT30_4 | — | ✅ |
| 64 | ItemText305 | ITEM_TEXT30_5 | — | — |
| 65 | ItemText306 | ITEM_TEXT30_6 | — | — |
| 66 | ItemText307 | ITEM_TEXT30_7 | — | — |
| 67 | ItemText308 | ITEM_TEXT30_8 | — | — |
| 68 | ItemText309 | ITEM_TEXT30_9 | — | — |
| 69 | LanguagePIPEOContextName | CONTEXT_NAME | — | — |
| 70 | LanguagePIPEOItemClob1 | ITEM_CLOB_1 | — | — |
| 71 | LanguageProfileItemPEOSectionId | SECTION_ID | — | — |
| 72 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 73 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 74 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 75 | Mandatory | MANDATORY | — | ✅ |
| 76 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 77 | ProfileItemPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 78 | ProfileItemPEOContentItemId | CONTENT_ITEM_ID | — | — |
| 79 | ProfileItemPEOContentTypeId | CONTENT_TYPE_ID | — | — |
| 80 | ProfileItemPEOCountryId | COUNTRY_ID | — | — |
| 81 | ProfileItemPEODateFrom | DATE_FROM | — | ✅ |
| 82 | ProfileItemPEODateTo | DATE_TO | — | ✅ |
| 83 | ProfileItemPEOParentProfileItemId | PARENT_PROFILE_ITEM_ID | — | — |
| 84 | ProfileItemPEOProfileId | PROFILE_ID | — | ✅ |
| 85 | ProfileItemPEOProfileItemId | PROFILE_ITEM_ID | 🔑 | ✅ |
| 86 | ProfileItemPEORatingLevelId1 | RATING_LEVEL_ID1 | — | — |
| 87 | ProfileItemPEORatingLevelId2 | RATING_LEVEL_ID2 | — | — |
| 88 | ProfileItemPEORatingLevelId3 | RATING_LEVEL_ID3 | — | — |
| 89 | ProfileItemPEORatingModelId1 | RATING_MODEL_ID1 | — | — |
| 90 | ProfileItemPEORatingModelId2 | RATING_MODEL_ID2 | — | — |
| 91 | ProfileItemPEORatingModelId3 | RATING_MODEL_ID3 | — | — |
| 92 | ProfileItemPEOStateProvinceId | STATE_PROVINCE_ID | — | — |
| 93 | QualifierId1 | QUALIFIER_ID1 | — | — |
| 94 | QualifierId2 | QUALIFIER_ID2 | — | — |
| 95 | SourceId | SOURCE_ID | — | — |
| 96 | SourceKey1 | SOURCE_KEY1 | — | — |
| 97 | SourceKey2 | SOURCE_KEY2 | — | — |
| 98 | SourceKey3 | SOURCE_KEY3 | — | — |
| 99 | SourceType | SOURCE_TYPE | — | — |

### [[hrt_content_types_b|HRT_CONTENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | ContentTypeBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 3 | ContentTypeBPEOContentTypeId | CONTENT_TYPE_ID | 🔑 | ✅ |
| 4 | ContentTypeBPEOContextName | CONTEXT_NAME | — | — |
| 5 | ContentTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ContentTypeBPEOModuleId | MODULE_ID | — | — |
| 7 | ContentTypeId | CONTENT_TYPE_ID | — | ✅ |
| 8 | ContextName | CONTEXT_NAME | — | — |
| 9 | FreeFormFlag | FREE_FORM_FLAG | — | — |

### [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 2 | ContentTypeId1 | CONTENT_TYPE_ID | — | — |
| 3 | ContentTypeName | CONTENT_TYPE_NAME | — | ✅ |
| 4 | ContentTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | Language | LANGUAGE | — | ✅ |

### [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ProfileTypeSectionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | ProfileTypeSectionPEOName | NAME | — | ✅ |
| 4 | SectionId | SECTION_ID | — | ✅ |

### [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RLReadMaxRatingDistribution | MAX_RATING_DISTRIBUTION | — | — |
| 2 | RLReadMinRatingDistribution | MIN_RATING_DISTRIBUTION | — | — |
| 3 | RLReadingBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 4 | RLReadingCareerStrDev | CAREER_STR_DEV | — | — |
| 5 | RLReadingDateFrom | DATE_FROM | — | — |
| 6 | RLReadingDateTo | DATE_TO | — | — |
| 7 | RLReadingFromPoints | FROM_POINTS | — | — |
| 8 | RLReadingNumericRating | NUMERIC_RATING | — | — |
| 9 | RLReadingRatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 10 | RLReadingRatingLevelId | RATING_LEVEL_ID | — | — |
| 11 | RLReadingReviewPoints | REVIEW_POINTS | — | — |
| 12 | RLReadingStarRating | STAR_RATING | — | — |
| 13 | RLReadingToPoints | TO_POINTS | — | — |
| 14 | RLSpeakBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 15 | RLSpeakCareerStrDev | CAREER_STR_DEV | — | — |
| 16 | RLSpeakDateFrom | DATE_FROM | — | — |
| 17 | RLSpeakDateTo | DATE_TO | — | — |
| 18 | RLSpeakFromPoints | FROM_POINTS | — | — |
| 19 | RLSpeakMaxRatingDistribution | MAX_RATING_DISTRIBUTION | — | — |
| 20 | RLSpeakMinRatingDistribution | MIN_RATING_DISTRIBUTION | — | — |
| 21 | RLSpeakNumericRating | NUMERIC_RATING | — | — |
| 22 | RLSpeakRatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 23 | RLSpeakRatingLevelId | RATING_LEVEL_ID | — | — |
| 24 | RLSpeakReviewPoints | REVIEW_POINTS | — | — |
| 25 | RLSpeakStarRating | STAR_RATING | — | — |
| 26 | RLSpeakToPoints | TO_POINTS | — | — |
| 27 | RLWriteBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 28 | RLWriteCareerStrDev | CAREER_STR_DEV | — | — |
| 29 | RLWriteDateFrom | DATE_FROM | — | — |
| 30 | RLWriteDateTo | DATE_TO | — | — |
| 31 | RLWriteFromPoints | FROM_POINTS | — | — |
| 32 | RLWriteMaxRatingDistribution | MAX_RATING_DISTRIBUTION | — | — |
| 33 | RLWriteMinRatingDistribution | MIN_RATING_DISTRIBUTION | — | — |
| 34 | RLWriteNumericRating | NUMERIC_RATING | — | — |
| 35 | RLWriteRatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 36 | RLWriteRatingLevelId | RATING_LEVEL_ID | — | — |
| 37 | RLWriteReviewPoints | REVIEW_POINTS | — | — |
| 38 | RLWriteStarRating | STAR_RATING | — | — |
| 39 | RLWriteToPoints | TO_POINTS | — | — |
| 40 | RtgLvlReadingLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 41 | RtgLvlSpeakingLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 42 | RtgLvlWritingLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_rating_levels_tl|HRT_RATING_LEVELS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RLTLReadBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 2 | RLTLReadLanguage1 | LANGUAGE | — | — |
| 3 | RLTLReadRatingDescription | RATING_DESCRIPTION | — | ✅ |
| 4 | RLTLReadRatingLevelId | RATING_LEVEL_ID | — | — |
| 5 | RLTLReadRatingShortDescr | RATING_SHORT_DESCR | — | ✅ |
| 6 | RLTLReadReviewRatingDescr | REVIEW_RATING_DESCR | — | — |
| 7 | RLTLReadSourceLang | SOURCE_LANG | — | — |
| 8 | RLTLSpeakBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 9 | RLTLSpeakLanguage1 | LANGUAGE | — | — |
| 10 | RLTLSpeakRatingDescription | RATING_DESCRIPTION | — | ✅ |
| 11 | RLTLSpeakRatingLevelId | RATING_LEVEL_ID | — | — |
| 12 | RLTLSpeakRatingShortDescr | RATING_SHORT_DESCR | — | ✅ |
| 13 | RLTLSpeakReviewRatingDescr | REVIEW_RATING_DESCR | — | ✅ |
| 14 | RLTLWriteBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 15 | RLTLWriteLanguage1 | LANGUAGE | — | — |
| 16 | RLTLWriteRatingDescription | RATING_DESCRIPTION | — | ✅ |
| 17 | RLTLWriteRatingLevelId | RATING_LEVEL_ID | — | — |
| 18 | RLTLWriteRatingShortDescr | RATING_SHORT_DESCR | — | ✅ |
| 19 | RLTLWriteReviewRatingDescr | REVIEW_RATING_DESCR | — | — |
| 20 | RtgLvlTLReadingLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | RtgLvlTLSpeakingLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | RtgLvlTLWritingLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_rating_models_b|HRT_RATING_MODELS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RMReadBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 2 | RMReadDateFrom | DATE_FROM | — | — |
| 3 | RMReadDateTo | DATE_TO | — | — |
| 4 | RMReadObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 5 | RMReadRatingModelCode | RATING_MODEL_CODE | — | ✅ |
| 6 | RMReadRatingModelId | RATING_MODEL_ID | — | — |
| 7 | RMSpeakBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 8 | RMSpeakDateFrom | DATE_FROM | — | — |
| 9 | RMSpeakRatingModelCode | RATING_MODEL_CODE | — | ✅ |
| 10 | RMSpeakRatingModelId | RATING_MODEL_ID | — | — |
| 11 | RMWriteBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 12 | RMWriteDateFrom | DATE_FROM | — | — |
| 13 | RMWriteDateTo | DATE_TO | — | — |
| 14 | RMWriteRatingModelCode | RATING_MODEL_CODE | — | ✅ |
| 15 | RMWriteRatingModelId | RATING_MODEL_ID | — | — |
| 16 | RtgMdlReadingBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | RtgMdlSpeakingLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | RtgMdlWritingLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_rating_models_tl|HRT_RATING_MODELS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RMTLReadBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 2 | RMTLReadLanguage1 | LANGUAGE | — | — |
| 3 | RMTLReadRatingDescription | RATING_DESCRIPTION | — | — |
| 4 | RMTLReadRatingModelId | RATING_MODEL_ID | — | — |
| 5 | RMTLReadRatingName | RATING_NAME | — | ✅ |
| 6 | RMTLReadSourceLang | SOURCE_LANG | — | — |
| 7 | RMTLSpeakBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 8 | RMTLSpeakLanguage1 | LANGUAGE | — | — |
| 9 | RMTLSpeakRatingDescription | RATING_DESCRIPTION | — | — |
| 10 | RMTLSpeakRatingModelId | RATING_MODEL_ID | — | — |
| 11 | RMTLSpeakRatingName | RATING_NAME | — | ✅ |
| 12 | RMTLWriteBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 13 | RMTLWriteLanguage1 | LANGUAGE | — | — |
| 14 | RMTLWriteRatingDescription | RATING_DESCRIPTION | — | — |
| 15 | RMTLWriteRatingModelId | RATING_MODEL_ID | — | — |
| 16 | RMTLWriteRatingName | RATING_NAME | — | ✅ |
| 17 | RtgMdlTLReadingLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | RtgMdlTLSpeakingLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | RtgMdlTLWritingLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_sources_b|HRT_SOURCES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 2 | SourceCode | SOURCE_CODE | — | — |
| 3 | SourceId1 | SOURCE_ID | — | — |

### [[hrt_sources_tl|HRT_SOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId4 | BUSINESS_GROUP_ID | — | — |
| 2 | Language1 | LANGUAGE | — | — |
| 3 | SourceDescription | SOURCE_DESCRIPTION | — | ✅ |
| 4 | SourceId2 | SOURCE_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
