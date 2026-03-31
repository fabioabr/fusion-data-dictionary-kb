---
id: DOC-OTHER-PVO-PotentialPVO_Viewall
doc_type: system-doc
title: "PotentialPVO_Viewall — PVO Cross-Module"
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
  - PotentialPVO_Viewall
  - potentialpvo_viewall
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PotentialPVO_Viewall

## 📌 Visão Geral

View Object para extração BICC de dados de Potential_Viewall. Acessa as tabelas: HRT_BI_CAREER_POTN_ITEMS_V, HRT_CONTENT_TYPES_B, HRT_CONTENT_TYPES_TL (+8).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileCoreAM.PotentialPVO_Viewall`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 169 | 11 | 2 | 31 | 18% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_bi_career_potn_items_v|HRT_BI_CAREER_POTN_ITEMS_V]] — 98 atributos (1 PKs, 11 BICC)
- [[hrt_content_types_b|HRT_CONTENT_TYPES_B]] — 9 atributos (1 PKs, 2 BICC)
- [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]] — 6 atributos (2 BICC)
- [[hrt_profiles_b|HRT_PROFILES_B]] — 9 atributos (1 BICC)
- [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]] — 4 atributos (2 BICC)
- [[hrt_qualifiers_b|HRT_QUALIFIERS_B]] — 4 atributos (1 BICC)
- [[hrt_qualifiers_tl|HRT_QUALIFIERS_TL]] — 5 atributos (2 BICC)
- [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]] — 15 atributos (3 BICC)
- [[hrt_rating_levels_tl|HRT_RATING_LEVELS_TL]] — 7 atributos (3 BICC)
- [[hrt_rating_models_b|HRT_RATING_MODELS_B]] — 6 atributos (2 BICC)
- [[hrt_rating_models_tl|HRT_RATING_MODELS_TL]] — 6 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hrt_bi_career_potn_items_v|HRT_BI_CAREER_POTN_ITEMS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContextName | CONTEXT_NAME | — | — |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | Importance | IMPORTANCE | — | — |
| 5 | InterestLevel | INTEREST_LEVEL | — | — |
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
| 19 | ItemDecimal2 | ITEM_DECIMAL_2 | — | — |
| 20 | ItemDecimal3 | ITEM_DECIMAL_3 | — | — |
| 21 | ItemDecimal4 | ITEM_DECIMAL_4 | — | — |
| 22 | ItemDecimal5 | ITEM_DECIMAL_5 | — | — |
| 23 | ItemNumber1 | ITEM_NUMBER_1 | — | — |
| 24 | ItemNumber10 | ITEM_NUMBER_10 | — | — |
| 25 | ItemNumber2 | ITEM_NUMBER_2 | — | — |
| 26 | ItemNumber3 | ITEM_NUMBER_3 | — | — |
| 27 | ItemNumber4 | ITEM_NUMBER_4 | — | — |
| 28 | ItemNumber5 | ITEM_NUMBER_5 | — | — |
| 29 | ItemNumber6 | ITEM_NUMBER_6 | — | — |
| 30 | ItemNumber7 | ITEM_NUMBER_7 | — | — |
| 31 | ItemNumber8 | ITEM_NUMBER_8 | — | — |
| 32 | ItemNumber9 | ITEM_NUMBER_9 | — | — |
| 33 | ItemText20001 | ITEM_TEXT2000_1 | — | ✅ |
| 34 | ItemText20002 | ITEM_TEXT2000_2 | — | — |
| 35 | ItemText20003 | ITEM_TEXT2000_3 | — | — |
| 36 | ItemText20004 | ITEM_TEXT2000_4 | — | — |
| 37 | ItemText20005 | ITEM_TEXT2000_5 | — | — |
| 38 | ItemText2401 | ITEM_TEXT240_1 | — | ✅ |
| 39 | ItemText24010 | ITEM_TEXT240_10 | — | — |
| 40 | ItemText24011 | ITEM_TEXT240_11 | — | — |
| 41 | ItemText24012 | ITEM_TEXT240_12 | — | — |
| 42 | ItemText24013 | ITEM_TEXT240_13 | — | — |
| 43 | ItemText24014 | ITEM_TEXT240_14 | — | — |
| 44 | ItemText24015 | ITEM_TEXT240_15 | — | — |
| 45 | ItemText2402 | ITEM_TEXT240_2 | — | — |
| 46 | ItemText2403 | ITEM_TEXT240_3 | — | — |
| 47 | ItemText2404 | ITEM_TEXT240_4 | — | — |
| 48 | ItemText2405 | ITEM_TEXT240_5 | — | — |
| 49 | ItemText2406 | ITEM_TEXT240_6 | — | — |
| 50 | ItemText2407 | ITEM_TEXT240_7 | — | — |
| 51 | ItemText2408 | ITEM_TEXT240_8 | — | — |
| 52 | ItemText2409 | ITEM_TEXT240_9 | — | — |
| 53 | ItemText301 | ITEM_TEXT30_1 | — | — |
| 54 | ItemText3010 | ITEM_TEXT30_10 | — | — |
| 55 | ItemText3011 | ITEM_TEXT30_11 | — | — |
| 56 | ItemText3012 | ITEM_TEXT30_12 | — | — |
| 57 | ItemText3013 | ITEM_TEXT30_13 | — | — |
| 58 | ItemText3014 | ITEM_TEXT30_14 | — | — |
| 59 | ItemText3015 | ITEM_TEXT30_15 | — | — |
| 60 | ItemText302 | ITEM_TEXT30_2 | — | — |
| 61 | ItemText303 | ITEM_TEXT30_3 | — | — |
| 62 | ItemText304 | ITEM_TEXT30_4 | — | — |
| 63 | ItemText305 | ITEM_TEXT30_5 | — | — |
| 64 | ItemText306 | ITEM_TEXT30_6 | — | — |
| 65 | ItemText307 | ITEM_TEXT30_7 | — | — |
| 66 | ItemText308 | ITEM_TEXT30_8 | — | — |
| 67 | ItemText309 | ITEM_TEXT30_9 | — | — |
| 68 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 69 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 70 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 71 | Mandatory | MANDATORY | — | — |
| 72 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 73 | ParentProfileItemId | PARENT_PROFILE_ITEM_ID | — | — |
| 74 | PotentialPIPEOItemClob1 | ITEM_CLOB_1 | — | — |
| 75 | PotentialProfileItemPEOItemClob2 | ITEM_CLOB_2 | — | — |
| 76 | ProfileItemPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 77 | ProfileItemPEOContentItemId | CONTENT_ITEM_ID | — | — |
| 78 | ProfileItemPEOContentTypeId | CONTENT_TYPE_ID | — | ✅ |
| 79 | ProfileItemPEOCountryId | COUNTRY_ID | — | — |
| 80 | ProfileItemPEODateFrom | DATE_FROM | — | ✅ |
| 81 | ProfileItemPEODateTo | DATE_TO | — | ✅ |
| 82 | ProfileItemPEOProfileId | PROFILE_ID | — | — |
| 83 | ProfileItemPEOProfileItemId | PROFILE_ITEM_ID | 🔑 | ✅ |
| 84 | ProfileItemPEORatingLevelId1 | RATING_LEVEL_ID1 | — | ✅ |
| 85 | ProfileItemPEORatingLevelId2 | RATING_LEVEL_ID2 | — | — |
| 86 | ProfileItemPEORatingLevelId3 | RATING_LEVEL_ID3 | — | — |
| 87 | ProfileItemPEORatingModelId1 | RATING_MODEL_ID1 | — | ✅ |
| 88 | ProfileItemPEORatingModelId2 | RATING_MODEL_ID2 | — | — |
| 89 | ProfileItemPEORatingModelId3 | RATING_MODEL_ID3 | — | — |
| 90 | ProfileItemPEOStateProvinceId | STATE_PROVINCE_ID | — | — |
| 91 | QualifierId1 | QUALIFIER_ID1 | — | — |
| 92 | QualifierId2 | QUALIFIER_ID2 | — | — |
| 93 | SectionId | SECTION_ID | — | ✅ |
| 94 | SourceId | SOURCE_ID | — | — |
| 95 | SourceKey1 | SOURCE_KEY1 | — | — |
| 96 | SourceKey2 | SOURCE_KEY2 | — | — |
| 97 | SourceKey3 | SOURCE_KEY3 | — | — |
| 98 | SourceType | SOURCE_TYPE | — | — |

### [[hrt_content_types_b|HRT_CONTENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CTBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CTContentTypeId | CONTENT_TYPE_ID | — | — |
| 3 | CTContextName | CONTEXT_NAME | — | — |
| 4 | ContentTypeBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 5 | ContentTypeBPEOContentTypeId | CONTENT_TYPE_ID | 🔑 | ✅ |
| 6 | ContentTypeBPEOContextName | CONTEXT_NAME | — | — |
| 7 | ContentTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ContentTypeBPEOModuleId | MODULE_ID | — | — |
| 9 | FreeFormFlag | FREE_FORM_FLAG | — | — |

### [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CTLBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CTLContentDescription | CONTENT_DESCRIPTION | — | — |
| 3 | CTLContentTypeId | CONTENT_TYPE_ID | — | — |
| 4 | CTLContentTypeName | CONTENT_TYPE_NAME | — | ✅ |
| 5 | CTLLanguage | LANGUAGE | — | — |
| 6 | ContentTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_profiles_b|HRT_PROFILES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProfileBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ProfileBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | ProfileBPEOOwnerPersonId | OWNER_PERSON_ID | — | — |
| 4 | ProfileBPEOPartyId | PARTY_ID | — | — |
| 5 | ProfileBPEOPersonId | PERSON_ID | — | — |
| 6 | ProfileBPEOProfileCode | PROFILE_CODE | — | — |
| 7 | ProfileBPEOProfileId | PROFILE_ID | — | — |
| 8 | ProfileBPEOProfileTypeId | PROFILE_TYPE_ID | — | — |
| 9 | ProfileBPEOProfileUsageCode | PROFILE_USAGE_CODE | — | — |

### [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PTSBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | PTSSectionId1 | SECTION_ID | — | — |
| 3 | ProfileTypeSectionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | ProfileTypeSectionPEOName | NAME | — | ✅ |

### [[hrt_qualifiers_b|HRT_QUALIFIERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | SourceCode | QUALIFIER_CODE | — | — |
| 3 | SourceId1 | QUALIFIER_ID | — | — |
| 4 | SourcesBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_qualifiers_tl|HRT_QUALIFIERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | STLBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | STLLanguage | LANGUAGE | — | — |
| 3 | STLSourceDescription | DESCRIPTION | — | ✅ |
| 4 | STLSourceId2 | QUALIFIER_ID | — | — |
| 5 | SourcesTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemDecimal1 | NUMERIC_RATING | — | ✅ |
| 2 | RatingLevelBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | RtgLvlPotBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | RtgLvlPotCareerStrDev | CAREER_STR_DEV | — | — |
| 5 | RtgLvlPotDateFrom | DATE_FROM | — | — |
| 6 | RtgLvlPotDateTo | DATE_TO | — | — |
| 7 | RtgLvlPotFromPoints | FROM_POINTS | — | — |
| 8 | RtgLvlPotMaxRatingDistrib | MAX_RATING_DISTRIBUTION | — | — |
| 9 | RtgLvlPotMinRatingDistrib | MIN_RATING_DISTRIBUTION | — | — |
| 10 | RtgLvlPotNumericRating | NUMERIC_RATING | — | — |
| 11 | RtgLvlPotRatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 12 | RtgLvlPotRatingLevelId | RATING_LEVEL_ID | — | — |
| 13 | RtgLvlPotReviewPoints | REVIEW_POINTS | — | — |
| 14 | RtgLvlPotStarRating | STAR_RATING | — | — |
| 15 | RtgLvlPotToPoints | TO_POINTS | — | — |

### [[hrt_rating_levels_tl|HRT_RATING_LEVELS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RtgLvlTLPotBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | RtgLvlTLPotLanguage | LANGUAGE | — | — |
| 3 | RtgLvlTLPotRatingDescription | RATING_DESCRIPTION | — | ✅ |
| 4 | RtgLvlTLPotRatingLevelId | RATING_LEVEL_ID | — | — |
| 5 | RtgLvlTLPotRatingShortDescr | RATING_SHORT_DESCR | — | ✅ |
| 6 | RtgLvlTLPotReviewRatingDescr | REVIEW_RATING_DESCR | — | — |
| 7 | RtgLvlTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_rating_models_b|HRT_RATING_MODELS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RatingModelBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | RtgMdlBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | RtgMdlDateFrom | DATE_FROM | — | — |
| 4 | RtgMdlDateTo | DATE_TO | — | — |
| 5 | RtgMdlRatingModelCode | RATING_MODEL_CODE | — | ✅ |
| 6 | RtgMdlRatingModelId | RATING_MODEL_ID | — | — |

### [[hrt_rating_models_tl|HRT_RATING_MODELS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RMTLPotBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | RMTLPotLanguage | LANGUAGE | — | — |
| 3 | RMTLPotRatingDescription | RATING_DESCRIPTION | — | — |
| 4 | RMTLPotRatingModelId | RATING_MODEL_ID | — | — |
| 5 | RMdlTLPotRatingName | RATING_NAME | — | ✅ |
| 6 | RtgMdlTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
