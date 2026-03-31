---
id: DOC-HCM-PVO-TalentScorePVO
doc_type: system-doc
title: "TalentScorePVO — PVO Human Capital Management"
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
  - TalentScorePVO
  - talentscorepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TalentScorePVO

## 📌 Visão Geral

Disponibiliza scores de talento com múltiplos tipos de conteúdo e itens de perfil. Base para classificação multidimensional de talentos na organização.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileCoreAM.TalentScorePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 252 | 11 | 4 | 23 | 9% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_bi_talent_rating_items_v|HRT_BI_TALENT_RATING_ITEMS_V]] — 165 atributos (1 PKs, 7 BICC)
- [[hrt_content_types_b|HRT_CONTENT_TYPES_B]] — 12 atributos (2 PKs, 3 BICC)
- [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]] — 5 atributos
- [[hrt_profiles_b|HRT_PROFILES_B]] — 14 atributos (1 PKs, 2 BICC)
- [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]] — 8 atributos (1 BICC)
- [[hrt_qualifiers_b|HRT_QUALIFIERS_B]] — 13 atributos (1 BICC)
- [[hrt_qualifiers_tl|HRT_QUALIFIERS_TL]] — 9 atributos (2 BICC)
- [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]] — 9 atributos (2 BICC)
- [[hrt_rating_levels_tl|HRT_RATING_LEVELS_TL]] — 6 atributos (2 BICC)
- [[hrt_rating_models_b|HRT_RATING_MODELS_B]] — 6 atributos (1 BICC)
- [[hrt_rating_models_tl|HRT_RATING_MODELS_TL]] — 5 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hrt_bi_talent_rating_items_v|HRT_BI_TALENT_RATING_ITEMS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContextName | CONTEXT_NAME | — | — |
| 2 | PiAttribute1 | ATTRIBUTE1 | — | — |
| 3 | PiAttribute10 | ATTRIBUTE10 | — | — |
| 4 | PiAttribute11 | ATTRIBUTE11 | — | — |
| 5 | PiAttribute12 | ATTRIBUTE12 | — | — |
| 6 | PiAttribute13 | ATTRIBUTE13 | — | — |
| 7 | PiAttribute14 | ATTRIBUTE14 | — | — |
| 8 | PiAttribute15 | ATTRIBUTE15 | — | — |
| 9 | PiAttribute16 | ATTRIBUTE16 | — | — |
| 10 | PiAttribute17 | ATTRIBUTE17 | — | — |
| 11 | PiAttribute18 | ATTRIBUTE18 | — | — |
| 12 | PiAttribute19 | ATTRIBUTE19 | — | — |
| 13 | PiAttribute2 | ATTRIBUTE2 | — | — |
| 14 | PiAttribute20 | ATTRIBUTE20 | — | — |
| 15 | PiAttribute21 | ATTRIBUTE21 | — | — |
| 16 | PiAttribute22 | ATTRIBUTE22 | — | — |
| 17 | PiAttribute23 | ATTRIBUTE23 | — | — |
| 18 | PiAttribute24 | ATTRIBUTE24 | — | — |
| 19 | PiAttribute25 | ATTRIBUTE25 | — | — |
| 20 | PiAttribute26 | ATTRIBUTE26 | — | — |
| 21 | PiAttribute27 | ATTRIBUTE27 | — | — |
| 22 | PiAttribute28 | ATTRIBUTE28 | — | — |
| 23 | PiAttribute29 | ATTRIBUTE29 | — | — |
| 24 | PiAttribute3 | ATTRIBUTE3 | — | — |
| 25 | PiAttribute30 | ATTRIBUTE30 | — | — |
| 26 | PiAttribute4 | ATTRIBUTE4 | — | — |
| 27 | PiAttribute5 | ATTRIBUTE5 | — | — |
| 28 | PiAttribute6 | ATTRIBUTE6 | — | — |
| 29 | PiAttribute7 | ATTRIBUTE7 | — | — |
| 30 | PiAttribute8 | ATTRIBUTE8 | — | — |
| 31 | PiAttribute9 | ATTRIBUTE9 | — | — |
| 32 | PiAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 33 | PiAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 34 | PiAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 35 | PiAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 36 | PiAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 37 | PiAttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 38 | PiAttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 39 | PiAttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 40 | PiAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 41 | PiAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 42 | PiAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 43 | PiAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 44 | PiAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 45 | PiAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 46 | PiAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 47 | PiAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 48 | PiAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 49 | PiAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 50 | PiAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 51 | PiAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 52 | PiAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 53 | PiAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 54 | PiAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 55 | PiAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 56 | PiAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 57 | PiAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 58 | PiAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 59 | PiAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 60 | PiAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 61 | PiAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 62 | PiAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 63 | PiAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 64 | PiAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 65 | PiAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 66 | PiAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 67 | PiAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 68 | PiBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 69 | PiContentItemId | CONTENT_ITEM_ID | — | — |
| 70 | PiContentTypeId | CONTENT_TYPE_ID | — | ✅ |
| 71 | PiCountryId | COUNTRY_ID | — | — |
| 72 | PiCreatedBy1 | CREATED_BY | — | — |
| 73 | PiCreationDate1 | CREATION_DATE | — | — |
| 74 | PiDateFrom | DATE_FROM | — | ✅ |
| 75 | PiDateTo | DATE_TO | — | ✅ |
| 76 | PiImportance | IMPORTANCE | — | — |
| 77 | PiInterestLevel | INTEREST_LEVEL | — | — |
| 78 | PiItemDate1 | ITEM_DATE_1 | — | — |
| 79 | PiItemDate10 | ITEM_DATE_10 | — | — |
| 80 | PiItemDate2 | ITEM_DATE_2 | — | — |
| 81 | PiItemDate3 | ITEM_DATE_3 | — | — |
| 82 | PiItemDate4 | ITEM_DATE_4 | — | — |
| 83 | PiItemDate5 | ITEM_DATE_5 | — | — |
| 84 | PiItemDate6 | ITEM_DATE_6 | — | — |
| 85 | PiItemDate7 | ITEM_DATE_7 | — | — |
| 86 | PiItemDate8 | ITEM_DATE_8 | — | — |
| 87 | PiItemDate9 | ITEM_DATE_9 | — | — |
| 88 | PiItemDecimal1 | ITEM_DECIMAL_1 | — | — |
| 89 | PiItemDecimal2 | ITEM_DECIMAL_2 | — | — |
| 90 | PiItemDecimal3 | ITEM_DECIMAL_3 | — | — |
| 91 | PiItemDecimal4 | ITEM_DECIMAL_4 | — | — |
| 92 | PiItemDecimal5 | ITEM_DECIMAL_5 | — | — |
| 93 | PiItemNumber1 | ITEM_NUMBER_1 | — | — |
| 94 | PiItemNumber10 | ITEM_NUMBER_10 | — | — |
| 95 | PiItemNumber2 | ITEM_NUMBER_2 | — | — |
| 96 | PiItemNumber3 | ITEM_NUMBER_3 | — | — |
| 97 | PiItemNumber4 | ITEM_NUMBER_4 | — | — |
| 98 | PiItemNumber5 | ITEM_NUMBER_5 | — | — |
| 99 | PiItemNumber6 | ITEM_NUMBER_6 | — | — |
| 100 | PiItemNumber7 | ITEM_NUMBER_7 | — | — |
| 101 | PiItemNumber8 | ITEM_NUMBER_8 | — | — |
| 102 | PiItemNumber9 | ITEM_NUMBER_9 | — | — |
| 103 | PiItemText20001 | ITEM_TEXT2000_1 | — | ✅ |
| 104 | PiItemText20002 | ITEM_TEXT2000_2 | — | — |
| 105 | PiItemText20003 | ITEM_TEXT2000_3 | — | — |
| 106 | PiItemText20004 | ITEM_TEXT2000_4 | — | — |
| 107 | PiItemText20005 | ITEM_TEXT2000_5 | — | — |
| 108 | PiItemText2401 | ITEM_TEXT240_1 | — | — |
| 109 | PiItemText24010 | ITEM_TEXT240_10 | — | — |
| 110 | PiItemText24011 | ITEM_TEXT240_11 | — | — |
| 111 | PiItemText24012 | ITEM_TEXT240_12 | — | — |
| 112 | PiItemText24013 | ITEM_TEXT240_13 | — | — |
| 113 | PiItemText24014 | ITEM_TEXT240_14 | — | — |
| 114 | PiItemText24015 | ITEM_TEXT240_15 | — | — |
| 115 | PiItemText2402 | ITEM_TEXT240_2 | — | — |
| 116 | PiItemText2403 | ITEM_TEXT240_3 | — | — |
| 117 | PiItemText2404 | ITEM_TEXT240_4 | — | — |
| 118 | PiItemText2405 | ITEM_TEXT240_5 | — | — |
| 119 | PiItemText2406 | ITEM_TEXT240_6 | — | — |
| 120 | PiItemText2407 | ITEM_TEXT240_7 | — | — |
| 121 | PiItemText2408 | ITEM_TEXT240_8 | — | — |
| 122 | PiItemText2409 | ITEM_TEXT240_9 | — | — |
| 123 | PiItemText301 | ITEM_TEXT30_1 | — | — |
| 124 | PiItemText3010 | ITEM_TEXT30_10 | — | — |
| 125 | PiItemText3011 | ITEM_TEXT30_11 | — | — |
| 126 | PiItemText3012 | ITEM_TEXT30_12 | — | — |
| 127 | PiItemText3013 | ITEM_TEXT30_13 | — | — |
| 128 | PiItemText3014 | ITEM_TEXT30_14 | — | — |
| 129 | PiItemText3015 | ITEM_TEXT30_15 | — | — |
| 130 | PiItemText302 | ITEM_TEXT30_2 | — | — |
| 131 | PiItemText303 | ITEM_TEXT30_3 | — | — |
| 132 | PiItemText304 | ITEM_TEXT30_4 | — | — |
| 133 | PiItemText305 | ITEM_TEXT30_5 | — | — |
| 134 | PiItemText306 | ITEM_TEXT30_6 | — | — |
| 135 | PiItemText307 | ITEM_TEXT30_7 | — | — |
| 136 | PiItemText308 | ITEM_TEXT30_8 | — | — |
| 137 | PiItemText309 | ITEM_TEXT30_9 | — | — |
| 138 | PiLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 139 | PiLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 140 | PiLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 141 | PiMandatory | MANDATORY | — | — |
| 142 | PiObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 143 | PiParentProfileItemId | PARENT_PROFILE_ITEM_ID | — | — |
| 144 | PiProfileId1 | PROFILE_ID | — | — |
| 145 | PiProfileItemId | PROFILE_ITEM_ID | 🔑 | ✅ |
| 146 | PiQualifierId1 | QUALIFIER_ID1 | — | — |
| 147 | PiQualifierId2 | QUALIFIER_ID2 | — | — |
| 148 | PiRatingLevelId1 | RATING_LEVEL_ID1 | — | — |
| 149 | PiRatingLevelId2 | RATING_LEVEL_ID2 | — | — |
| 150 | PiRatingLevelId3 | RATING_LEVEL_ID3 | — | — |
| 151 | PiRatingModelId1 | RATING_MODEL_ID1 | — | — |
| 152 | PiRatingModelId2 | RATING_MODEL_ID2 | — | — |
| 153 | PiRatingModelId3 | RATING_MODEL_ID3 | — | — |
| 154 | PiSourceId | SOURCE_ID | — | — |
| 155 | PiSourceKey1 | SOURCE_KEY1 | — | — |
| 156 | PiSourceKey2 | SOURCE_KEY2 | — | — |
| 157 | PiSourceKey3 | SOURCE_KEY3 | — | — |
| 158 | PiSourceType | SOURCE_TYPE | — | — |
| 159 | PiStateProvinceId | STATE_PROVINCE_ID | — | — |
| 160 | SectionId | SECTION_ID | — | ✅ |
| 161 | TSPIItemClob1 | ITEM_CLOB_1 | — | — |
| 162 | TSPIItemClob2 | ITEM_CLOB_2 | — | — |
| 163 | TSPIItemClob3 | ITEM_CLOB_3 | — | — |
| 164 | TSPIItemClob4 | ITEM_CLOB_4 | — | — |
| 165 | TSPIItemClob5 | ITEM_CLOB_5 | — | — |

### [[hrt_content_types_b|HRT_CONTENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CTBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CTFreeFormFlag | FREE_FORM_FLAG | — | — |
| 3 | CtBusinessGroupId2 | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 4 | CtContentTypeId1 | CONTENT_TYPE_ID | 🔑 | ✅ |
| 5 | CtContextName | CONTEXT_NAME | — | — |
| 6 | CtCreatedBy2 | CREATED_BY | — | — |
| 7 | CtCreationDate2 | CREATION_DATE | — | — |
| 8 | CtLastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 9 | CtLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 10 | CtLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 11 | CtModuleId | MODULE_ID | — | — |
| 12 | CtObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |

### [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CTBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | CTLanguage | LANGUAGE | — | — |
| 3 | CTTLContentDescription | CONTENT_DESCRIPTION | — | — |
| 4 | CTTLContentTypeId | CONTENT_TYPE_ID | — | — |
| 5 | CTTLContentTypeName | CONTENT_TYPE_NAME | — | — |

### [[hrt_profiles_b|HRT_PROFILES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrfBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | PrfCreatedBy | CREATED_BY | — | — |
| 3 | PrfCreationDate | CREATION_DATE | — | — |
| 4 | PrfLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PrfLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | PrfLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | PrfObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | PrfOwnerPersonId | OWNER_PERSON_ID | — | — |
| 9 | PrfPartyId | PARTY_ID | — | — |
| 10 | PrfPersonId | PERSON_ID | — | — |
| 11 | PrfProfileCode | PROFILE_CODE | — | — |
| 12 | PrfProfileId | PROFILE_ID | 🔑 | ✅ |
| 13 | PrfProfileTypeId | PROFILE_TYPE_ID | — | — |
| 14 | PrfProfileUsageCode | PROFILE_USAGE_CODE | — | — |

### [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PTSBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | PTSSectionId1 | SECTION_ID | — | — |
| 3 | PTSSectionItemReqdFlag | SECTION_ITEM_REQD_FLAG | — | — |
| 4 | ParentSectionId | PARENT_SECTION_ID | — | — |
| 5 | ProfileTypeSectionPEOName | NAME | — | ✅ |
| 6 | QualifierSetId1 | QUALIFIER_SET_ID1 | — | — |
| 7 | QualifierSetId2 | QUALIFIER_SET_ID2 | — | — |
| 8 | SectionContext | SECTION_CONTEXT | — | — |

### [[hrt_qualifiers_b|HRT_QUALIFIERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | EmpDefFlag | EMP_DEF_FLAG | — | — |
| 3 | EmpViewFlag | EMP_VIEW_FLAG | — | — |
| 4 | MgrDefFlag | MGR_DEF_FLAG | — | — |
| 5 | MgrViewFlag | MGR_VIEW_FLAG | — | — |
| 6 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | QualifierCode | QUALIFIER_CODE | — | — |
| 8 | QualifierId | QUALIFIER_ID | — | — |
| 9 | QualifierSeqNumber | QUALIFIER_SEQ_NUMBER | — | — |
| 10 | QualifierSetId | QUALIFIER_SET_ID | — | — |
| 11 | SBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 12 | SourcesBPEOSourceCode | QUALIFIER_CODE | — | ✅ |
| 13 | SourcesBPEOSourceId | QUALIFIER_ID | — | — |

### [[hrt_qualifiers_tl|HRT_QUALIFIERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QTLBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | QTLLanguage | LANGUAGE | — | — |
| 3 | QTLQualifierId1 | QUALIFIER_ID | — | — |
| 4 | QualifiersTLPEODescription | DESCRIPTION | — | ✅ |
| 5 | STLBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 6 | STLLanguage | LANGUAGE | — | — |
| 7 | STLSourceDescription | DESCRIPTION | — | ✅ |
| 8 | STLSourceId | QUALIFIER_ID | — | — |
| 9 | STLSourceLang | SOURCE_LANG | — | — |

### [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RatingLevelBPEONumericRatin | NUMERIC_RATING | — | ✅ |
| 2 | RtgLvlBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | RtgLvlCareerStrDev | CAREER_STR_DEV | — | — |
| 4 | RtgLvlDateFrom | DATE_FROM | — | — |
| 5 | RtgLvlDateTo | DATE_TO | — | — |
| 6 | RtgLvlRatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 7 | RtgLvlRatingLevelId | RATING_LEVEL_ID | — | — |
| 8 | RtgLvlStarRating | STAR_RATING | — | — |
| 9 | RtgLvlToPoints | TO_POINTS | — | — |

### [[hrt_rating_levels_tl|HRT_RATING_LEVELS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TSBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | TSLanguage | LANGUAGE | — | — |
| 3 | TSRatingDescription | RATING_DESCRIPTION | — | ✅ |
| 4 | TSRatingLevelId | RATING_LEVEL_ID | — | — |
| 5 | TSRatingShortDescr | RATING_SHORT_DESCR | — | ✅ |
| 6 | TSReviewRatingDescr | REVIEW_RATING_DESCR | — | — |

### [[hrt_rating_models_b|HRT_RATING_MODELS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RMdlBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | RMdlDateFrom | DATE_FROM | — | — |
| 3 | RMdlDateTo | DATE_TO | — | — |
| 4 | RMdlModuleId | MODULE_ID | — | — |
| 5 | RMdlRatingModelCode | RATING_MODEL_CODE | — | ✅ |
| 6 | RMdlRatingModelId | RATING_MODEL_ID | — | — |

### [[hrt_rating_models_tl|HRT_RATING_MODELS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RMTLBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | RMTLLanguage | LANGUAGE | — | — |
| 3 | RMTLRatingDescription | RATING_DESCRIPTION | — | ✅ |
| 4 | RMTLRatingModelId | RATING_MODEL_ID | — | — |
| 5 | RMTLRatingName | RATING_NAME | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
