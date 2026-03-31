---
id: DOC-OTHER-PVO-AdvancementReadinessPVO_Viewall
doc_type: system-doc
title: "AdvancementReadinessPVO_Viewall — PVO Cross-Module"
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
  - AdvancementReadinessPVO_Viewall
  - advancementreadinesspvo_viewall
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AdvancementReadinessPVO_Viewall

## 📌 Visão Geral

View Object para extração BICC de dados de Advancement Readiness_Viewall. Acessa as tabelas: HRT_BI_ADV_READINESS_ITEMS_V, HRT_CONTENT_TYPES_B, HRT_CONTENT_TYPES_TL (+4).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileCoreAM.AdvancementReadinessPVO_Viewall`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 131 | 7 | 3 | 21 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_bi_adv_readiness_items_v|HRT_BI_ADV_READINESS_ITEMS_V]] — 95 atributos (2 PKs, 12 BICC)
- [[hrt_content_types_b|HRT_CONTENT_TYPES_B]] — 9 atributos (1 PKs, 2 BICC)
- [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]] — 5 atributos (1 BICC)
- [[hrt_profiles_b|HRT_PROFILES_B]] — 9 atributos (1 BICC)
- [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]] — 4 atributos (2 BICC)
- [[hrt_sources_b|HRT_SOURCES_B]] — 4 atributos (1 BICC)
- [[hrt_sources_tl|HRT_SOURCES_TL]] — 5 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hrt_bi_adv_readiness_items_v|HRT_BI_ADV_READINESS_ITEMS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdvReadinessPIPEOContextName | CONTEXT_NAME | — | — |
| 2 | AdvReadinessPIPEOItemClob1 | ITEM_CLOB_1 | — | — |
| 3 | AdvReadinessPIPEOSectionId | SECTION_ID | — | ✅ |
| 4 | CountryId | COUNTRY_ID | — | — |
| 5 | CreatedBy | CREATED_BY | — | — |
| 6 | CreationDate | CREATION_DATE | — | — |
| 7 | DateFrom | DATE_FROM | — | ✅ |
| 8 | DateTo | DATE_TO | — | ✅ |
| 9 | Importance | IMPORTANCE | — | — |
| 10 | InterestLevel | INTEREST_LEVEL | — | — |
| 11 | ItemDate1 | ITEM_DATE_1 | — | ✅ |
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
| 26 | ItemNumber1 | ITEM_NUMBER_1 | — | ✅ |
| 27 | ItemNumber10 | ITEM_NUMBER_10 | — | — |
| 28 | ItemNumber2 | ITEM_NUMBER_2 | — | ✅ |
| 29 | ItemNumber3 | ITEM_NUMBER_3 | — | — |
| 30 | ItemNumber4 | ITEM_NUMBER_4 | — | — |
| 31 | ItemNumber5 | ITEM_NUMBER_5 | — | — |
| 32 | ItemNumber6 | ITEM_NUMBER_6 | — | — |
| 33 | ItemNumber7 | ITEM_NUMBER_7 | — | — |
| 34 | ItemNumber8 | ITEM_NUMBER_8 | — | — |
| 35 | ItemNumber9 | ITEM_NUMBER_9 | — | — |
| 36 | ItemText20001 | ITEM_TEXT2000_1 | — | ✅ |
| 37 | ItemText20002 | ITEM_TEXT2000_2 | — | — |
| 38 | ItemText20003 | ITEM_TEXT2000_3 | — | — |
| 39 | ItemText20004 | ITEM_TEXT2000_4 | — | — |
| 40 | ItemText20005 | ITEM_TEXT2000_5 | — | — |
| 41 | ItemText2401 | ITEM_TEXT240_1 | — | — |
| 42 | ItemText24010 | ITEM_TEXT240_10 | — | — |
| 43 | ItemText24011 | ITEM_TEXT240_11 | — | — |
| 44 | ItemText24012 | ITEM_TEXT240_12 | — | — |
| 45 | ItemText24013 | ITEM_TEXT240_13 | — | — |
| 46 | ItemText24014 | ITEM_TEXT240_14 | — | — |
| 47 | ItemText24015 | ITEM_TEXT240_15 | — | — |
| 48 | ItemText2402 | ITEM_TEXT240_2 | — | — |
| 49 | ItemText2403 | ITEM_TEXT240_3 | — | — |
| 50 | ItemText2404 | ITEM_TEXT240_4 | — | — |
| 51 | ItemText2405 | ITEM_TEXT240_5 | — | — |
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
| 63 | ItemText302 | ITEM_TEXT30_2 | — | — |
| 64 | ItemText303 | ITEM_TEXT30_3 | — | — |
| 65 | ItemText304 | ITEM_TEXT30_4 | — | — |
| 66 | ItemText305 | ITEM_TEXT30_5 | — | — |
| 67 | ItemText306 | ITEM_TEXT30_6 | — | — |
| 68 | ItemText307 | ITEM_TEXT30_7 | — | — |
| 69 | ItemText308 | ITEM_TEXT30_8 | — | — |
| 70 | ItemText309 | ITEM_TEXT30_9 | — | — |
| 71 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 72 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 73 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 74 | Mandatory | MANDATORY | — | — |
| 75 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 76 | ProfileItemPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 77 | ProfileItemPEOContentItemId | CONTENT_ITEM_ID | — | — |
| 78 | ProfileItemPEOContentTypeId | CONTENT_TYPE_ID | — | ✅ |
| 79 | ProfileItemPEOParentProfileItemId | PARENT_PROFILE_ITEM_ID | — | — |
| 80 | ProfileItemPEOProfileId | PROFILE_ID | 🔑 | ✅ |
| 81 | ProfileItemPEOProfileItemId | PROFILE_ITEM_ID | 🔑 | ✅ |
| 82 | QualifierId1 | QUALIFIER_ID1 | — | — |
| 83 | QualifierId2 | QUALIFIER_ID2 | — | — |
| 84 | RatingLevelId1 | RATING_LEVEL_ID1 | — | — |
| 85 | RatingLevelId2 | RATING_LEVEL_ID2 | — | — |
| 86 | RatingLevelId3 | RATING_LEVEL_ID3 | — | — |
| 87 | RatingModelId1 | RATING_MODEL_ID1 | — | — |
| 88 | RatingModelId2 | RATING_MODEL_ID2 | — | — |
| 89 | RatingModelId3 | RATING_MODEL_ID3 | — | — |
| 90 | SourceId | SOURCE_ID | — | — |
| 91 | SourceKey1 | SOURCE_KEY1 | — | — |
| 92 | SourceKey2 | SOURCE_KEY2 | — | — |
| 93 | SourceKey3 | SOURCE_KEY3 | — | — |
| 94 | SourceType | SOURCE_TYPE | — | — |
| 95 | StateProvinceId | STATE_PROVINCE_ID | — | — |

### [[hrt_content_types_b|HRT_CONTENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ContentTypeBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | ContentTypeBPEOContentTypeId | CONTENT_TYPE_ID | 🔑 | ✅ |
| 4 | ContentTypeBPEOContextName | CONTEXT_NAME | — | — |
| 5 | ContentTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ContentTypeBPEOModuleId | MODULE_ID | — | — |
| 7 | ContentTypeId | CONTENT_TYPE_ID | — | — |
| 8 | FreeFormFlag | FREE_FORM_FLAG | — | — |
| 9 | ModuleId | MODULE_ID | — | — |

### [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CTTLBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CTTLContentTypeId | CONTENT_TYPE_ID | — | — |
| 3 | CTTLContentTypeName | CONTENT_TYPE_NAME | — | — |
| 4 | CTTLLanguage | LANGUAGE | — | — |
| 5 | ContentTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

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
| 2 | PTSSectionId | SECTION_ID | — | — |
| 3 | ProfileTypeSectionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | ProfileTypeSectionPEOName | NAME | — | ✅ |

### [[hrt_sources_b|HRT_SOURCES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | SBPEOSourceCode | SOURCE_CODE | — | — |
| 3 | SBPEOSourceId1 | SOURCE_ID | — | — |
| 4 | SourcesBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_sources_tl|HRT_SOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | STLBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | STLLanguage | LANGUAGE | — | — |
| 3 | STLSourceDescription | SOURCE_DESCRIPTION | — | ✅ |
| 4 | STLSourceId1 | SOURCE_ID | — | — |
| 5 | SourcesTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
