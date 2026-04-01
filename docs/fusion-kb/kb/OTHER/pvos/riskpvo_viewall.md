---
id: DOC-OTHER-PVO-RiskPVO_Viewall
doc_type: system-doc
title: "RiskPVO_Viewall — PVO Cross-Module"
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
  - RiskPVO_Viewall
  - riskpvo_viewall
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RiskPVO_Viewall

## 📌 Visão Geral

View Object para extração BICC de dados de Risk_Viewall. Acessa as tabelas: HRT_BI_RISK_ITEMS_V, HRT_CONTENT_TYPES_B, HRT_CONTENT_TYPES_TL (+8).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileCoreAM.RiskPVO_Viewall`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 195 | 11 | 1 | 41 | 21% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_bi_risk_items_v|HRT_BI_RISK_ITEMS_V]] — 100 atributos (1 PKs, 14 BICC)
- [[hrt_content_types_b|HRT_CONTENT_TYPES_B]] — 3 atributos (1 BICC)
- [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]] — 6 atributos (2 BICC)
- [[hrt_profiles_b|HRT_PROFILES_B]] — 9 atributos (1 BICC)
- [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]] — 4 atributos (2 BICC)
- [[hrt_qualifiers_b|HRT_QUALIFIERS_B]] — 4 atributos (1 BICC)
- [[hrt_qualifiers_tl|HRT_QUALIFIERS_TL]] — 5 atributos (2 BICC)
- [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]] — 27 atributos (4 BICC)
- [[hrt_rating_levels_tl|HRT_RATING_LEVELS_TL]] — 14 atributos (6 BICC)
- [[hrt_rating_models_b|HRT_RATING_MODELS_B]] — 12 atributos (4 BICC)
- [[hrt_rating_models_tl|HRT_RATING_MODELS_TL]] — 11 atributos (4 BICC)

---

## ⚙️ Atributos

### [[hrt_bi_risk_items_v|HRT_BI_RISK_ITEMS_V]]

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
| 34 | ItemText20001 | ITEM_TEXT2000_1 | — | ✅ |
| 35 | ItemText20002 | ITEM_TEXT2000_2 | — | ✅ |
| 36 | ItemText20003 | ITEM_TEXT2000_3 | — | — |
| 37 | ItemText20004 | ITEM_TEXT2000_4 | — | — |
| 38 | ItemText20005 | ITEM_TEXT2000_5 | — | — |
| 39 | ItemText2401 | ITEM_TEXT240_1 | — | — |
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
| 54 | ItemText301 | ITEM_TEXT30_1 | — | ✅ |
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
| 65 | ItemText306 | ITEM_TEXT30_6 | — | ✅ |
| 66 | ItemText307 | ITEM_TEXT30_7 | — | ✅ |
| 67 | ItemText308 | ITEM_TEXT30_8 | — | — |
| 68 | ItemText309 | ITEM_TEXT30_9 | — | — |
| 69 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 70 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 71 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 72 | Mandatory | MANDATORY | — | — |
| 73 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 74 | ParentProfileItemId | PARENT_PROFILE_ITEM_ID | — | — |
| 75 | ProfileItemPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 76 | ProfileItemPEOContentItemId | CONTENT_ITEM_ID | — | — |
| 77 | ProfileItemPEOContentTypeId | CONTENT_TYPE_ID | — | ✅ |
| 78 | ProfileItemPEOCountryId | COUNTRY_ID | — | — |
| 79 | ProfileItemPEODateFrom | DATE_FROM | — | ✅ |
| 80 | ProfileItemPEODateTo | DATE_TO | — | ✅ |
| 81 | ProfileItemPEOProfileId | PROFILE_ID | — | — |
| 82 | ProfileItemPEOProfileItemId | PROFILE_ITEM_ID | 🔑 | ✅ |
| 83 | ProfileItemPEORatingLevelId1 | RATING_LEVEL_ID1 | — | — |
| 84 | ProfileItemPEORatingLevelId2 | RATING_LEVEL_ID2 | — | — |
| 85 | ProfileItemPEORatingLevelId3 | RATING_LEVEL_ID3 | — | — |
| 86 | ProfileItemPEORatingModelId1 | RATING_MODEL_ID1 | — | ✅ |
| 87 | ProfileItemPEORatingModelId2 | RATING_MODEL_ID2 | — | ✅ |
| 88 | ProfileItemPEORatingModelId3 | RATING_MODEL_ID3 | — | — |
| 89 | ProfileItemPEOStateProvinceId | STATE_PROVINCE_ID | — | — |
| 90 | QualifierId1 | QUALIFIER_ID1 | — | — |
| 91 | QualifierId2 | QUALIFIER_ID2 | — | — |
| 92 | RiskPIItemClob1 | ITEM_CLOB_1 | — | — |
| 93 | RiskPIItemClob2 | ITEM_CLOB_2 | — | — |
| 94 | RiskPIItemText2401 | ITEM_TEXT240_1 | — | — |
| 95 | SectionId | SECTION_ID | — | ✅ |
| 96 | SourceId | SOURCE_ID | — | — |
| 97 | SourceKey1 | SOURCE_KEY1 | — | — |
| 98 | SourceKey2 | SOURCE_KEY2 | — | — |
| 99 | SourceKey3 | SOURCE_KEY3 | — | — |
| 100 | SourceType | SOURCE_TYPE | — | — |

### [[hrt_content_types_b|HRT_CONTENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ContentTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | ContentTypeId | CONTENT_TYPE_ID | — | — |

### [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CTTLBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CTTLContentDescription | CONTENT_DESCRIPTION | — | — |
| 3 | CTTLContentTypeId | CONTENT_TYPE_ID | — | — |
| 4 | CTTLContentTypeName | CONTENT_TYPE_NAME | — | ✅ |
| 5 | CTTLLanguage | LANGUAGE | — | — |
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
| 1 | PTSPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | PTSectionPEOSectionId1 | SECTION_ID | — | — |
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
| 1 | RLIMPACTBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | RLIMPACTCareerStrDev | CAREER_STR_DEV | — | — |
| 3 | RLIMPACTDateFrom | DATE_FROM | — | — |
| 4 | RLIMPACTDateTo | DATE_TO | — | — |
| 5 | RLIMPACTFromPoints | FROM_POINTS | — | — |
| 6 | RLIMPACTMaxRatingDistrib | MAX_RATING_DISTRIBUTION | — | — |
| 7 | RLIMPACTMinRatingDistrib | MIN_RATING_DISTRIBUTION | — | — |
| 8 | RLIMPACTNumericRating | NUMERIC_RATING | — | — |
| 9 | RLIMPACTRatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 10 | RLIMPACTRatingLevelId | RATING_LEVEL_ID | — | — |
| 11 | RLIMPACTReviewPoints | REVIEW_POINTS | — | — |
| 12 | RLIMPACTStarRating | STAR_RATING | — | — |
| 13 | RLIMPACTToPoints | TO_POINTS | — | — |
| 14 | RLRISKBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 15 | RLRISKDateFrom | DATE_FROM | — | — |
| 16 | RLRISKDateTo | DATE_TO | — | — |
| 17 | RLRISKFromPoints | FROM_POINTS | — | — |
| 18 | RLRISKMaxRatingDistribution | MAX_RATING_DISTRIBUTION | — | — |
| 19 | RLRISKMinRatingDistribution | MIN_RATING_DISTRIBUTION | — | — |
| 20 | RLRISKRatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 21 | RLRISKRatingLevelId | RATING_LEVEL_ID | — | — |
| 22 | RLRISKRatingModelId | RATING_MODEL_ID | — | — |
| 23 | RLRISKReviewPoints | REVIEW_POINTS | — | — |
| 24 | RLRISKStarRating | STAR_RATING | — | — |
| 25 | RLRISKToPoints | TO_POINTS | — | — |
| 26 | RatingLevelImpactBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 27 | RatingLevelRiskBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_rating_levels_tl|HRT_RATING_LEVELS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RLTLImpactBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | RLTLImpactLanguage | LANGUAGE | — | — |
| 3 | RLTLImpactRatingDescription | RATING_DESCRIPTION | — | ✅ |
| 4 | RLTLImpactRatingLevelId | RATING_LEVEL_ID | — | — |
| 5 | RLTLImpactRatingShortDescr | RATING_SHORT_DESCR | — | ✅ |
| 6 | RLTLImpactReviewRatingDescr | REVIEW_RATING_DESCR | — | — |
| 7 | RLTLRISKBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 8 | RLTLRISKLanguage | LANGUAGE | — | — |
| 9 | RLTLRISKRatingDescription | RATING_DESCRIPTION | — | ✅ |
| 10 | RLTLRISKRatingLevelId | RATING_LEVEL_ID | — | — |
| 11 | RLTLRISKRatingShortDescr | RATING_SHORT_DESCR | — | ✅ |
| 12 | RLTLRISKReviewRatingDescr | REVIEW_RATING_DESCR | — | — |
| 13 | RtgLvlImpactTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | RtgLvlRiskTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_rating_models_b|HRT_RATING_MODELS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RMdlImpactBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | RMdlImpactDateFrom | DATE_FROM | — | — |
| 3 | RMdlImpactDateTo | DATE_TO | — | — |
| 4 | RMdlImpactRatingModelCode | RATING_MODEL_CODE | — | ✅ |
| 5 | RMdlImpactRatingModelId | RATING_MODEL_ID | — | — |
| 6 | RMdlRiskRatingModelCode | RATING_MODEL_CODE | — | ✅ |
| 7 | RiskRtgMdlBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 8 | RiskRtgMdlDateFrom | DATE_FROM | — | — |
| 9 | RiskRtgMdlDateTo | DATE_TO | — | — |
| 10 | RiskRtgMdlRatingModelId | RATING_MODEL_ID | — | — |
| 11 | RtgMdlImpactBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | RtgMdlRiskBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_rating_models_tl|HRT_RATING_MODELS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RtgMdlImpactTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | RtgMdlRiskBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | RtgMdlRiskLanguage | LANGUAGE | — | — |
| 4 | RtgMdlRiskRatingModelId | RATING_MODEL_ID | — | — |
| 5 | RtgMdlRiskTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | RtgMdlTLImpactBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 7 | RtgMdlTLImpactLanguage | LANGUAGE | — | — |
| 8 | RtgMdlTLImpactRatingDescrip | RATING_DESCRIPTION | — | — |
| 9 | RtgMdlTLImpactRatingModelId | RATING_MODEL_ID | — | — |
| 10 | RtgMdlTLImpactRatingName | RATING_NAME | — | ✅ |
| 11 | RtgMdlTLRiskRatingName | RATING_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
