---
id: DOC-OTHER-PVO-PersonProfileItemPVO
doc_type: system-doc
title: "PersonProfileItemPVO — PVO Cross-Module"
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
  - PersonProfileItemPVO
  - personprofileitempvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonProfileItemPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Person Profile Item. Acessa as tabelas: HRT_CONTENT_TYPES_B, HRT_CONTENT_TYPES_TL, HRT_PROFILES_B (+4).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileCoreAM.PersonProfileItemPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 146 | 7 | 3 | 19 | 13% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_content_types_b|HRT_CONTENT_TYPES_B]] — 5 atributos (1 BICC)
- [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]] — 6 atributos (1 BICC)
- [[hrt_profiles_b|HRT_PROFILES_B]] — 14 atributos (1 PKs, 7 BICC)
- [[hrt_profiles_tl|HRT_PROFILES_TL]] — 7 atributos (3 BICC)
- [[hrt_profile_items|HRT_PROFILE_ITEMS]] — 93 atributos (1 PKs, 3 BICC)
- [[hrt_profile_types_b|HRT_PROFILE_TYPES_B]] — 10 atributos (1 PKs, 3 BICC)
- [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]] — 11 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hrt_content_types_b|HRT_CONTENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CTBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CTBPEOContentTypeId | CONTENT_TYPE_ID | — | — |
| 3 | CTBPEOContextName | CONTEXT_NAME | — | — |
| 4 | CTBPEOFreeFormFlag | FREE_FORM_FLAG | — | — |
| 5 | ContentTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CTTLBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CTTLContentDescription | CONTENT_DESCRIPTION | — | — |
| 3 | CTTLContentTypeId | CONTENT_TYPE_ID | — | — |
| 4 | CTTLContentTypeName | CONTENT_TYPE_NAME | — | — |
| 5 | CTTLLanguage1 | LANGUAGE | — | — |
| 6 | CntTypeTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_profiles_b|HRT_PROFILES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | ProfileBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 8 | ProfileBPEOOwnerPersonId | OWNER_PERSON_ID | — | — |
| 9 | ProfileBPEOPartyId | PARTY_ID | — | ✅ |
| 10 | ProfileBPEOPersonId | PERSON_ID | — | ✅ |
| 11 | ProfileBPEOProfileCode | PROFILE_CODE | — | ✅ |
| 12 | ProfileBPEOProfileId | PROFILE_ID | 🔑 | ✅ |
| 13 | ProfileBPEOProfileTypeId | PROFILE_TYPE_ID | — | — |
| 14 | ProfileBPEOProfileUsageCode | PROFILE_USAGE_CODE | — | ✅ |

### [[hrt_profiles_tl|HRT_PROFILES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | — | ✅ |
| 2 | ProfileTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | ProfileTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | ProfileTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ProfileTranslationPEOProfileId | PROFILE_ID | — | — |
| 6 | ProfileTranslationPEOSummary | SUMMARY | — | — |
| 7 | SourceLang | SOURCE_LANG | — | — |

### [[hrt_profile_items|HRT_PROFILE_ITEMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Importance | IMPORTANCE | — | — |
| 2 | InterestLevel | INTEREST_LEVEL | — | — |
| 3 | ItemClob1 | ITEM_CLOB_1 | — | — |
| 4 | ItemClob2 | ITEM_CLOB_2 | — | — |
| 5 | ItemClob3 | ITEM_CLOB_3 | — | — |
| 6 | ItemClob4 | ITEM_CLOB_4 | — | — |
| 7 | ItemClob5 | ITEM_CLOB_5 | — | — |
| 8 | ItemDate1 | ITEM_DATE_1 | — | — |
| 9 | ItemDate10 | ITEM_DATE_10 | — | — |
| 10 | ItemDate2 | ITEM_DATE_2 | — | — |
| 11 | ItemDate3 | ITEM_DATE_3 | — | — |
| 12 | ItemDate4 | ITEM_DATE_4 | — | — |
| 13 | ItemDate5 | ITEM_DATE_5 | — | — |
| 14 | ItemDate6 | ITEM_DATE_6 | — | — |
| 15 | ItemDate7 | ITEM_DATE_7 | — | — |
| 16 | ItemDate8 | ITEM_DATE_8 | — | — |
| 17 | ItemDate9 | ITEM_DATE_9 | — | — |
| 18 | ItemDecimal1 | ITEM_DECIMAL_1 | — | — |
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
| 33 | ItemText20001 | ITEM_TEXT2000_1 | — | — |
| 34 | ItemText20002 | ITEM_TEXT2000_2 | — | — |
| 35 | ItemText20003 | ITEM_TEXT2000_3 | — | — |
| 36 | ItemText20004 | ITEM_TEXT2000_4 | — | — |
| 37 | ItemText20005 | ITEM_TEXT2000_5 | — | — |
| 38 | ItemText2401 | ITEM_TEXT240_1 | — | — |
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
| 68 | Mandatory | MANDATORY | — | — |
| 69 | ProfileItemPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 70 | ProfileItemPEOContentItemId | CONTENT_ITEM_ID | — | — |
| 71 | ProfileItemPEOContentTypeId | CONTENT_TYPE_ID | — | — |
| 72 | ProfileItemPEOCountryId | COUNTRY_ID | — | — |
| 73 | ProfileItemPEODateFrom | DATE_FROM | — | — |
| 74 | ProfileItemPEODateTo | DATE_TO | — | — |
| 75 | ProfileItemPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 76 | ProfileItemPEOParentProfileItemId | PARENT_PROFILE_ITEM_ID | — | — |
| 77 | ProfileItemPEOProfileId | PROFILE_ID | — | ✅ |
| 78 | ProfileItemPEOProfileItemId | PROFILE_ITEM_ID | 🔑 | ✅ |
| 79 | ProfileItemPEORatingLevelId1 | RATING_LEVEL_ID1 | — | — |
| 80 | ProfileItemPEORatingLevelId2 | RATING_LEVEL_ID2 | — | — |
| 81 | ProfileItemPEORatingLevelId3 | RATING_LEVEL_ID3 | — | — |
| 82 | ProfileItemPEORatingModelId1 | RATING_MODEL_ID1 | — | — |
| 83 | ProfileItemPEORatingModelId2 | RATING_MODEL_ID2 | — | — |
| 84 | ProfileItemPEORatingModelId3 | RATING_MODEL_ID3 | — | — |
| 85 | ProfileItemPEOStateProvinceId | STATE_PROVINCE_ID | — | — |
| 86 | QualifierId1 | QUALIFIER_ID1 | — | — |
| 87 | QualifierId2 | QUALIFIER_ID2 | — | — |
| 88 | SectionId | SECTION_ID | — | — |
| 89 | SourceId | SOURCE_ID | — | — |
| 90 | SourceKey1 | SOURCE_KEY1 | — | — |
| 91 | SourceKey2 | SOURCE_KEY2 | — | — |
| 92 | SourceKey3 | SOURCE_KEY3 | — | — |
| 93 | SourceType | SOURCE_TYPE | — | — |

### [[hrt_profile_types_b|HRT_PROFILE_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProfileTypeBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ProfileTypeBPEODateFrom | DATE_FROM | — | — |
| 3 | ProfileTypeBPEODateTo | DATE_TO | — | — |
| 4 | ProfileTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ProfileTypeBPEOModuleId | MODULE_ID | — | — |
| 6 | ProfileTypeBPEOPidApprovalFlag | PID_APPROVAL_FLAG | — | ✅ |
| 7 | ProfileTypeBPEOProfileStatusCode | PROFILE_STATUS_CODE | — | — |
| 8 | ProfileTypeBPEOProfileTypeCode | PROFILE_TYPE_CODE | — | — |
| 9 | ProfileTypeBPEOProfileTypeId | PROFILE_TYPE_ID | 🔑 | ✅ |
| 10 | ProfileTypeBPEOProfileUsageCode | PROFILE_USAGE_CODE | — | — |

### [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApprovalRequiredFlag | APPROVAL_REQUIRED_FLAG | — | — |
| 2 | PTSBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | PTSCreatedBy1 | CREATED_BY | — | — |
| 4 | PTSCreationDate1 | CREATION_DATE | — | — |
| 5 | PTSLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 6 | PTSLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 7 | PTSProfileTypeId | PROFILE_TYPE_ID | — | — |
| 8 | PTSSectionContext | SECTION_CONTEXT | — | — |
| 9 | ParentSectionId | PARENT_SECTION_ID | — | — |
| 10 | ProfileTypeSectionPEOName | NAME | — | — |
| 11 | SectionId1 | SECTION_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
