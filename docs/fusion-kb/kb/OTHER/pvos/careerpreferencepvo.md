---
id: DOC-OTHER-PVO-CareerPreferencePVO
doc_type: system-doc
title: "CareerPreferencePVO — PVO Cross-Module"
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
  - CareerPreferencePVO
  - careerpreferencepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CareerPreferencePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Career Preference. Acessa as tabelas: HRT_BI_CAREER_PRF_ITEMS_V, HRT_CONTENT_TYPES_B, HRT_CONTENT_TYPES_TL (+3).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileCoreAM.CareerPreferencePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 131 | 6 | 5 | 30 | 23% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_bi_career_prf_items_v|HRT_BI_CAREER_PRF_ITEMS_V]] — 98 atributos (3 PKs, 14 BICC)
- [[hrt_content_types_b|HRT_CONTENT_TYPES_B]] — 9 atributos (2 PKs, 3 BICC)
- [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]] — 6 atributos (2 BICC)
- [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]] — 4 atributos (3 BICC)
- [[per_job_family_f|PER_JOB_FAMILY_F]] — 7 atributos (3 BICC)
- [[per_job_family_f_tl|PER_JOB_FAMILY_F_TL]] — 7 atributos (5 BICC)

---

## ⚙️ Atributos

### [[hrt_bi_career_prf_items_v|HRT_BI_CAREER_PRF_ITEMS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CareerPrefPIPEOItemClob1 | ITEM_CLOB_1 | — | — |
| 2 | CareerPrefPIPEOItemClob2 | ITEM_CLOB_2 | — | — |
| 3 | CareerPrefPIPEOItemText20003 | ITEM_TEXT2000_3 | — | ✅ |
| 4 | CareerPrefPIPEOItemText20004 | ITEM_TEXT2000_4 | — | ✅ |
| 5 | CareerPrefPIPEOSectionId | SECTION_ID | — | — |
| 6 | CareerPrefProfileItemPEOContextName | CONTEXT_NAME | — | — |
| 7 | CreatedBy | CREATED_BY | — | — |
| 8 | CreationDate | CREATION_DATE | — | — |
| 9 | Importance | IMPORTANCE | — | — |
| 10 | InterestLevel | INTEREST_LEVEL | — | — |
| 11 | ItemDate1 | ITEM_DATE_1 | — | — |
| 12 | ItemDate10 | ITEM_DATE_10 | — | — |
| 13 | ItemDate2 | ITEM_DATE_2 | — | — |
| 14 | ItemDate3 | ITEM_DATE_3 | — | — |
| 15 | ItemDate4 | ITEM_DATE_4 | — | — |
| 16 | ItemDate5 | ITEM_DATE_5 | — | — |
| 17 | ItemDate6 | ITEM_DATE_6 | — | — |
| 18 | ItemDate7 | ITEM_DATE_7 | — | — |
| 19 | ItemDate8 | ITEM_DATE_8 | — | — |
| 20 | ItemDate9 | ITEM_DATE_9 | — | — |
| 21 | ItemDecimal1 | ITEM_DECIMAL_1 | — | — |
| 22 | ItemDecimal2 | ITEM_DECIMAL_2 | — | — |
| 23 | ItemDecimal3 | ITEM_DECIMAL_3 | — | — |
| 24 | ItemDecimal4 | ITEM_DECIMAL_4 | — | — |
| 25 | ItemDecimal5 | ITEM_DECIMAL_5 | — | — |
| 26 | ItemNumber10 | ITEM_NUMBER_10 | — | — |
| 27 | ItemNumber2 | ITEM_NUMBER_2 | — | — |
| 28 | ItemNumber4 | ITEM_NUMBER_4 | — | ✅ |
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
| 61 | ItemText302 | ITEM_TEXT30_2 | — | ✅ |
| 62 | ItemText303 | ITEM_TEXT30_3 | — | ✅ |
| 63 | ItemText304 | ITEM_TEXT30_4 | — | — |
| 64 | ItemText305 | ITEM_TEXT30_5 | — | — |
| 65 | ItemText306 | ITEM_TEXT30_6 | — | — |
| 66 | ItemText307 | ITEM_TEXT30_7 | — | — |
| 67 | ItemText308 | ITEM_TEXT30_8 | — | — |
| 68 | ItemText309 | ITEM_TEXT30_9 | — | — |
| 69 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 70 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 71 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 72 | Mandatory | MANDATORY | — | — |
| 73 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 74 | ProfileItemPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 75 | ProfileItemPEOContentItemId | CONTENT_ITEM_ID | — | — |
| 76 | ProfileItemPEOContentTypeId | CONTENT_TYPE_ID | 🔑 | ✅ |
| 77 | ProfileItemPEOCountryId | COUNTRY_ID | — | — |
| 78 | ProfileItemPEODateFrom | DATE_FROM | — | ✅ |
| 79 | ProfileItemPEODateTo | DATE_TO | — | ✅ |
| 80 | ProfileItemPEOItemNumber1 | ITEM_NUMBER_1 | — | — |
| 81 | ProfileItemPEOItemNumber3 | ITEM_NUMBER_3 | — | — |
| 82 | ProfileItemPEOParentProfileItemId | PARENT_PROFILE_ITEM_ID | — | — |
| 83 | ProfileItemPEOProfileId | PROFILE_ID | — | — |
| 84 | ProfileItemPEOProfileItemId | PROFILE_ITEM_ID | 🔑 | ✅ |
| 85 | ProfileItemPEOStateProvinceId | STATE_PROVINCE_ID | — | — |
| 86 | QualifierId1 | QUALIFIER_ID1 | — | — |
| 87 | QualifierId2 | QUALIFIER_ID2 | — | — |
| 88 | RatingLevelId1 | RATING_LEVEL_ID1 | — | — |
| 89 | RatingLevelId2 | RATING_LEVEL_ID2 | — | — |
| 90 | RatingLevelId3 | RATING_LEVEL_ID3 | — | — |
| 91 | RatingModelId1 | RATING_MODEL_ID1 | — | — |
| 92 | RatingModelId2 | RATING_MODEL_ID2 | — | — |
| 93 | RatingModelId3 | RATING_MODEL_ID3 | — | — |
| 94 | SourceId | SOURCE_ID | — | — |
| 95 | SourceKey1 | SOURCE_KEY1 | — | — |
| 96 | SourceKey2 | SOURCE_KEY2 | — | — |
| 97 | SourceKey3 | SOURCE_KEY3 | — | — |
| 98 | SourceType | SOURCE_TYPE | — | — |

### [[hrt_content_types_b|HRT_CONTENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | CTTLContentTypeId | CONTENT_TYPE_ID | — | — |
| 3 | CTTLContextName | CONTEXT_NAME | — | — |
| 4 | ContentTypeBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 5 | ContentTypeBPEOContentTypeId | CONTENT_TYPE_ID | 🔑 | ✅ |
| 6 | ContentTypeBPEOContextName | CONTEXT_NAME | — | — |
| 7 | ContentTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ContentTypeBPEOModuleId | MODULE_ID | — | — |
| 9 | FreeFormFlag | FREE_FORM_FLAG | — | — |

### [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CTTLBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 2 | CTTLContentDescription | CONTENT_DESCRIPTION | — | — |
| 3 | CTTLContentTypeId1 | CONTENT_TYPE_ID | — | — |
| 4 | CTTLContentTypeName | CONTENT_TYPE_NAME | — | ✅ |
| 5 | CTTLLanguage1 | LANGUAGE | — | — |
| 6 | ContentTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ProfileTypeSectionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | ProfileTypeSectionPEOName | NAME | — | ✅ |
| 4 | SectionId | SECTION_ID | — | ✅ |

### [[per_job_family_f|PER_JOB_FAMILY_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | ActiveStatus | ACTIVE_STATUS | — | — |
| 3 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | JobFamilyId | JOB_FAMILY_ID | — | — |
| 6 | JobFamilyPEOEffectiveStartDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | JobFamilyPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[per_job_family_f_tl|PER_JOB_FAMILY_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate1 | EFFECTIVE_START_DATE | — | ✅ |
| 3 | JobFamilyId1 | JOB_FAMILY_ID | — | — |
| 4 | JobFamilyName | JOB_FAMILY_NAME | — | ✅ |
| 5 | JobFamilyTranslationPEOEffectiveStartDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | JobFamilyTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | Language | LANGUAGE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
