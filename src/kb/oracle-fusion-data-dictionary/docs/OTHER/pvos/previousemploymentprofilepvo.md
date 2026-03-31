---
id: DOC-OTHER-PVO-PreviousEmploymentProfilePVO
doc_type: system-doc
title: "PreviousEmploymentProfilePVO — PVO Cross-Module"
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
  - PreviousEmploymentProfilePVO
  - previousemploymentprofilepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PreviousEmploymentProfilePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Previous Employment Profile. Acessa as tabelas: HRT_BI_PREV_EMPLOYMENT_ITEMS_V, HRT_CONTENT_TYPES_B, HRT_CONTENT_TYPES_TL (+3).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileCoreAM.PreviousEmploymentProfilePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 140 | 6 | 1 | 45 | 32% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_bi_prev_employment_items_v|HRT_BI_PREV_EMPLOYMENT_ITEMS_V]] — 99 atributos (35 BICC)
- [[hrt_content_types_b|HRT_CONTENT_TYPES_B]] — 7 atributos (2 BICC)
- [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]] — 6 atributos (3 BICC)
- [[hrt_profiles_b|HRT_PROFILES_B]] — 14 atributos (1 PKs, 2 BICC)
- [[hrt_profiles_tl|HRT_PROFILES_TL]] — 7 atributos (1 BICC)
- [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]] — 7 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hrt_bi_prev_employment_items_v|HRT_BI_PREV_EMPLOYMENT_ITEMS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CountryCode | COUNTRY_CODE | — | — |
| 2 | CountryName | COUNTRY_NAME | — | ✅ |
| 3 | Importance | IMPORTANCE | — | — |
| 4 | InterestLevel | INTEREST_LEVEL | — | — |
| 5 | ItemClob1 | ITEM_CLOB_1 | — | — |
| 6 | ItemClob2 | ITEM_CLOB_2 | — | — |
| 7 | ItemClob3 | ITEM_CLOB_3 | — | — |
| 8 | ItemClob4 | ITEM_CLOB_4 | — | — |
| 9 | ItemClob5 | ITEM_CLOB_5 | — | — |
| 10 | ItemDate1 | ITEM_DATE_1 | — | ✅ |
| 11 | ItemDate10 | ITEM_DATE_10 | — | — |
| 12 | ItemDate2 | ITEM_DATE_2 | — | ✅ |
| 13 | ItemDate3 | ITEM_DATE_3 | — | — |
| 14 | ItemDate4 | ITEM_DATE_4 | — | — |
| 15 | ItemDate5 | ITEM_DATE_5 | — | — |
| 16 | ItemDate6 | ITEM_DATE_6 | — | — |
| 17 | ItemDate7 | ITEM_DATE_7 | — | — |
| 18 | ItemDate8 | ITEM_DATE_8 | — | — |
| 19 | ItemDate9 | ITEM_DATE_9 | — | — |
| 20 | ItemDecimal1 | ITEM_DECIMAL_1 | — | ✅ |
| 21 | ItemDecimal2 | ITEM_DECIMAL_2 | — | ✅ |
| 22 | ItemDecimal3 | ITEM_DECIMAL_3 | — | — |
| 23 | ItemDecimal4 | ITEM_DECIMAL_4 | — | — |
| 24 | ItemDecimal5 | ITEM_DECIMAL_5 | — | — |
| 25 | ItemNumber1 | ITEM_NUMBER_1 | — | ✅ |
| 26 | ItemNumber10 | ITEM_NUMBER_10 | — | — |
| 27 | ItemNumber2 | ITEM_NUMBER_2 | — | — |
| 28 | ItemNumber3 | ITEM_NUMBER_3 | — | — |
| 29 | ItemNumber4 | ITEM_NUMBER_4 | — | — |
| 30 | ItemNumber5 | ITEM_NUMBER_5 | — | — |
| 31 | ItemNumber6 | ITEM_NUMBER_6 | — | — |
| 32 | ItemNumber7 | ITEM_NUMBER_7 | — | — |
| 33 | ItemNumber8 | ITEM_NUMBER_8 | — | ✅ |
| 34 | ItemNumber9 | ITEM_NUMBER_9 | — | — |
| 35 | ItemText20001 | ITEM_TEXT2000_1 | — | ✅ |
| 36 | ItemText20002 | ITEM_TEXT2000_2 | — | ✅ |
| 37 | ItemText20003 | ITEM_TEXT2000_3 | — | — |
| 38 | ItemText20004 | ITEM_TEXT2000_4 | — | — |
| 39 | ItemText20005 | ITEM_TEXT2000_5 | — | — |
| 40 | ItemText2401 | ITEM_TEXT240_1 | — | ✅ |
| 41 | ItemText24010 | ITEM_TEXT240_10 | — | ✅ |
| 42 | ItemText24011 | ITEM_TEXT240_11 | — | ✅ |
| 43 | ItemText24012 | ITEM_TEXT240_12 | — | ✅ |
| 44 | ItemText24013 | ITEM_TEXT240_13 | — | ✅ |
| 45 | ItemText24014 | ITEM_TEXT240_14 | — | ✅ |
| 46 | ItemText24015 | ITEM_TEXT240_15 | — | — |
| 47 | ItemText2402 | ITEM_TEXT240_2 | — | ✅ |
| 48 | ItemText2403 | ITEM_TEXT240_3 | — | ✅ |
| 49 | ItemText2404 | ITEM_TEXT240_4 | — | ✅ |
| 50 | ItemText2405 | ITEM_TEXT240_5 | — | — |
| 51 | ItemText2406 | ITEM_TEXT240_6 | — | ✅ |
| 52 | ItemText2407 | ITEM_TEXT240_7 | — | ✅ |
| 53 | ItemText2408 | ITEM_TEXT240_8 | — | ✅ |
| 54 | ItemText2409 | ITEM_TEXT240_9 | — | ✅ |
| 55 | ItemText301 | ITEM_TEXT30_1 | — | ✅ |
| 56 | ItemText3010 | ITEM_TEXT30_10 | — | — |
| 57 | ItemText3011 | ITEM_TEXT30_11 | — | — |
| 58 | ItemText3012 | ITEM_TEXT30_12 | — | — |
| 59 | ItemText3013 | ITEM_TEXT30_13 | — | — |
| 60 | ItemText3014 | ITEM_TEXT30_14 | — | — |
| 61 | ItemText3015 | ITEM_TEXT30_15 | — | — |
| 62 | ItemText302 | ITEM_TEXT30_2 | — | ✅ |
| 63 | ItemText303 | ITEM_TEXT30_3 | — | — |
| 64 | ItemText304 | ITEM_TEXT30_4 | — | — |
| 65 | ItemText305 | ITEM_TEXT30_5 | — | ✅ |
| 66 | ItemText306 | ITEM_TEXT30_6 | — | — |
| 67 | ItemText307 | ITEM_TEXT30_7 | — | ✅ |
| 68 | ItemText308 | ITEM_TEXT30_8 | — | ✅ |
| 69 | ItemText309 | ITEM_TEXT30_9 | — | ✅ |
| 70 | Mandatory | MANDATORY | — | — |
| 71 | ProfileItemPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 72 | ProfileItemPEOContentItemId | CONTENT_ITEM_ID | — | — |
| 73 | ProfileItemPEOContentTypeId | CONTENT_TYPE_ID | — | ✅ |
| 74 | ProfileItemPEOCountryId | COUNTRY_ID | — | — |
| 75 | ProfileItemPEODateFrom | DATE_FROM | — | ✅ |
| 76 | ProfileItemPEODateTo | DATE_TO | — | ✅ |
| 77 | ProfileItemPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 78 | ProfileItemPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 79 | ProfileItemPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 80 | ProfileItemPEOParentProfileItemId | PARENT_PROFILE_ITEM_ID | — | — |
| 81 | ProfileItemPEOProfileId | PROFILE_ID | — | — |
| 82 | ProfileItemPEOProfileItemId | PROFILE_ITEM_ID | — | ✅ |
| 83 | ProfileItemPEORatingLevelId1 | RATING_LEVEL_ID1 | — | — |
| 84 | ProfileItemPEORatingLevelId2 | RATING_LEVEL_ID2 | — | — |
| 85 | ProfileItemPEORatingLevelId3 | RATING_LEVEL_ID3 | — | — |
| 86 | ProfileItemPEORatingModelId1 | RATING_MODEL_ID1 | — | — |
| 87 | ProfileItemPEORatingModelId2 | RATING_MODEL_ID2 | — | — |
| 88 | ProfileItemPEORatingModelId3 | RATING_MODEL_ID3 | — | — |
| 89 | ProfileItemPEOStateProvinceId | STATE_PROVINCE_ID | — | — |
| 90 | QualifierId1 | QUALIFIER_ID1 | — | — |
| 91 | QualifierId2 | QUALIFIER_ID2 | — | — |
| 92 | SectionId | SECTION_ID | — | ✅ |
| 93 | SourceId | SOURCE_ID | — | — |
| 94 | SourceKey1 | SOURCE_KEY1 | — | — |
| 95 | SourceKey2 | SOURCE_KEY2 | — | — |
| 96 | SourceKey3 | SOURCE_KEY3 | — | — |
| 97 | SourceType | SOURCE_TYPE | — | — |
| 98 | StateProvinceCode | STATE_PROVINCE_CODE | — | — |
| 99 | StateProvinceName | STATE_PROVINCE_NAME | — | ✅ |

### [[hrt_content_types_b|HRT_CONTENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CTBPContentTypeContextName | CONTEXT_NAME | — | ✅ |
| 2 | ContentTypeBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | ContentTypeBPEOContentTypeId | CONTENT_TYPE_ID | — | — |
| 4 | ContentTypeBPEOContextName | CONTEXT_NAME | — | — |
| 5 | ContentTypeBPEOFreeFormFlag | FREE_FORM_FLAG | — | — |
| 6 | ContentTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ContentTypeBPEOModuleId | MODULE_ID | — | — |

### [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CTLContentTypeId | CONTENT_TYPE_ID | — | — |
| 2 | CTTLContentDescription | CONTENT_DESCRIPTION | — | ✅ |
| 3 | CTTLContentTypeName | CONTENT_TYPE_NAME | — | ✅ |
| 4 | ContentTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | Language1 | LANGUAGE | — | — |
| 6 | TLBusinessGroupId | BUSINESS_GROUP_ID | — | — |

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
| 1 | PTSBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | PTSParentSectionId | PARENT_SECTION_ID | — | — |
| 3 | PTSQualifierSetId1 | QUALIFIER_SET_ID1 | — | — |
| 4 | PTSQualifierSetId2 | QUALIFIER_SET_ID2 | — | — |
| 5 | PTS_SectionId1 | SECTION_ID | — | — |
| 6 | ProfileTypeSectionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ProfileTypeSectionPEOName | NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
