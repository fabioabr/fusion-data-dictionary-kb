---
id: DOC-HCM-PVO-CustomContentProfilePVO
doc_type: system-doc
title: "CustomContentProfilePVO — PVO Human Capital Management"
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
  - CustomContentProfilePVO
  - customcontentprofilepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CustomContentProfilePVO

## 📌 Visão Geral

Extrai conteudo customizado de perfis de talento com tipos e secoes definidos pelo cliente. Suporta extensibilidade do modelo de perfil de competencias.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileCoreAM.CustomContentProfilePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 137 | 6 | 2 | 99 | 72% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_content_types_b|HRT_CONTENT_TYPES_B]] — 8 atributos (1 BICC)
- [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]] — 6 atributos (1 BICC)
- [[hrt_profiles_b|HRT_PROFILES_B]] — 14 atributos (1 PKs, 7 BICC)
- [[hrt_profiles_tl|HRT_PROFILES_TL]] — 7 atributos (1 BICC)
- [[hrt_profile_items|HRT_PROFILE_ITEMS]] — 95 atributos (1 PKs, 86 BICC)
- [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]] — 7 atributos (3 BICC)

---

## ⚙️ Atributos

### [[hrt_content_types_b|HRT_CONTENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CTBPEOFreeFormFlag | FREE_FORM_FLAG | — | — |
| 2 | ContentTypeBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | ContentTypeBPEOContentTypeId | CONTENT_TYPE_ID | — | — |
| 4 | ContentTypeBPEOContextName | CONTEXT_NAME | — | — |
| 5 | ContentTypeBPEOFreeFormFlag | FREE_FORM_FLAG | — | — |
| 6 | ContentTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ContentTypeBPEOModuleId | MODULE_ID | — | — |
| 8 | ContextName | CONTEXT_NAME | — | — |

### [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CTLBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CTLContentTypeId | CONTENT_TYPE_ID | — | — |
| 3 | CTLContentTypeName | CONTENT_TYPE_NAME | — | — |
| 4 | CTLLanguage1 | LANGUAGE | — | — |
| 5 | CTTLContentDescription | CONTENT_DESCRIPTION | — | — |
| 6 | CntTypeTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_profiles_b|HRT_PROFILES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | ProfileBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 8 | ProfileBPEOOwnerPersonId | OWNER_PERSON_ID | — | — |
| 9 | ProfileBPEOPartyId | PARTY_ID | — | — |
| 10 | ProfileBPEOPersonId | PERSON_ID | — | — |
| 11 | ProfileBPEOProfileCode | PROFILE_CODE | — | ✅ |
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

### [[hrt_profile_items|HRT_PROFILE_ITEMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Importance | IMPORTANCE | — | ✅ |
| 2 | InterestLevel | INTEREST_LEVEL | — | ✅ |
| 3 | ItemClob1 | ITEM_CLOB_1 | — | — |
| 4 | ItemClob2 | ITEM_CLOB_2 | — | — |
| 5 | ItemClob3 | ITEM_CLOB_3 | — | — |
| 6 | ItemClob4 | ITEM_CLOB_4 | — | — |
| 7 | ItemClob5 | ITEM_CLOB_5 | — | — |
| 8 | ItemDate1 | ITEM_DATE_1 | — | ✅ |
| 9 | ItemDate10 | ITEM_DATE_10 | — | ✅ |
| 10 | ItemDate2 | ITEM_DATE_2 | — | ✅ |
| 11 | ItemDate3 | ITEM_DATE_3 | — | ✅ |
| 12 | ItemDate4 | ITEM_DATE_4 | — | ✅ |
| 13 | ItemDate5 | ITEM_DATE_5 | — | ✅ |
| 14 | ItemDate6 | ITEM_DATE_6 | — | ✅ |
| 15 | ItemDate7 | ITEM_DATE_7 | — | ✅ |
| 16 | ItemDate8 | ITEM_DATE_8 | — | ✅ |
| 17 | ItemDate9 | ITEM_DATE_9 | — | ✅ |
| 18 | ItemDecimal1 | ITEM_DECIMAL_1 | — | ✅ |
| 19 | ItemDecimal2 | ITEM_DECIMAL_2 | — | ✅ |
| 20 | ItemDecimal3 | ITEM_DECIMAL_3 | — | ✅ |
| 21 | ItemDecimal4 | ITEM_DECIMAL_4 | — | ✅ |
| 22 | ItemDecimal5 | ITEM_DECIMAL_5 | — | ✅ |
| 23 | ItemNumber1 | ITEM_NUMBER_1 | — | ✅ |
| 24 | ItemNumber10 | ITEM_NUMBER_10 | — | ✅ |
| 25 | ItemNumber2 | ITEM_NUMBER_2 | — | ✅ |
| 26 | ItemNumber3 | ITEM_NUMBER_3 | — | ✅ |
| 27 | ItemNumber4 | ITEM_NUMBER_4 | — | ✅ |
| 28 | ItemNumber5 | ITEM_NUMBER_5 | — | ✅ |
| 29 | ItemNumber6 | ITEM_NUMBER_6 | — | ✅ |
| 30 | ItemNumber7 | ITEM_NUMBER_7 | — | ✅ |
| 31 | ItemNumber8 | ITEM_NUMBER_8 | — | ✅ |
| 32 | ItemNumber9 | ITEM_NUMBER_9 | — | ✅ |
| 33 | ItemText20001 | ITEM_TEXT2000_1 | — | ✅ |
| 34 | ItemText20002 | ITEM_TEXT2000_2 | — | ✅ |
| 35 | ItemText20003 | ITEM_TEXT2000_3 | — | ✅ |
| 36 | ItemText20004 | ITEM_TEXT2000_4 | — | ✅ |
| 37 | ItemText20005 | ITEM_TEXT2000_5 | — | ✅ |
| 38 | ItemText2401 | ITEM_TEXT240_1 | — | ✅ |
| 39 | ItemText24010 | ITEM_TEXT240_10 | — | ✅ |
| 40 | ItemText24011 | ITEM_TEXT240_11 | — | ✅ |
| 41 | ItemText24012 | ITEM_TEXT240_12 | — | ✅ |
| 42 | ItemText24013 | ITEM_TEXT240_13 | — | ✅ |
| 43 | ItemText24014 | ITEM_TEXT240_14 | — | ✅ |
| 44 | ItemText24015 | ITEM_TEXT240_15 | — | ✅ |
| 45 | ItemText2402 | ITEM_TEXT240_2 | — | ✅ |
| 46 | ItemText2403 | ITEM_TEXT240_3 | — | ✅ |
| 47 | ItemText2404 | ITEM_TEXT240_4 | — | ✅ |
| 48 | ItemText2405 | ITEM_TEXT240_5 | — | ✅ |
| 49 | ItemText2406 | ITEM_TEXT240_6 | — | ✅ |
| 50 | ItemText2407 | ITEM_TEXT240_7 | — | ✅ |
| 51 | ItemText2408 | ITEM_TEXT240_8 | — | ✅ |
| 52 | ItemText2409 | ITEM_TEXT240_9 | — | ✅ |
| 53 | ItemText301 | ITEM_TEXT30_1 | — | ✅ |
| 54 | ItemText3010 | ITEM_TEXT30_10 | — | ✅ |
| 55 | ItemText3011 | ITEM_TEXT30_11 | — | ✅ |
| 56 | ItemText3012 | ITEM_TEXT30_12 | — | ✅ |
| 57 | ItemText3013 | ITEM_TEXT30_13 | — | ✅ |
| 58 | ItemText3014 | ITEM_TEXT30_14 | — | ✅ |
| 59 | ItemText3015 | ITEM_TEXT30_15 | — | ✅ |
| 60 | ItemText302 | ITEM_TEXT30_2 | — | ✅ |
| 61 | ItemText303 | ITEM_TEXT30_3 | — | ✅ |
| 62 | ItemText304 | ITEM_TEXT30_4 | — | ✅ |
| 63 | ItemText305 | ITEM_TEXT30_5 | — | ✅ |
| 64 | ItemText306 | ITEM_TEXT30_6 | — | ✅ |
| 65 | ItemText307 | ITEM_TEXT30_7 | — | ✅ |
| 66 | ItemText308 | ITEM_TEXT30_8 | — | ✅ |
| 67 | ItemText309 | ITEM_TEXT30_9 | — | ✅ |
| 68 | Mandatory | MANDATORY | — | ✅ |
| 69 | ProfileItemPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 70 | ProfileItemPEOContentItemId | CONTENT_ITEM_ID | — | — |
| 71 | ProfileItemPEOContentTypeId | CONTENT_TYPE_ID | — | ✅ |
| 72 | ProfileItemPEOCountryId | COUNTRY_ID | — | ✅ |
| 73 | ProfileItemPEODateFrom | DATE_FROM | — | ✅ |
| 74 | ProfileItemPEODateTo | DATE_TO | — | ✅ |
| 75 | ProfileItemPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 76 | ProfileItemPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 77 | ProfileItemPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 78 | ProfileItemPEOParentProfileItemId | PARENT_PROFILE_ITEM_ID | — | — |
| 79 | ProfileItemPEOProfileId | PROFILE_ID | — | ✅ |
| 80 | ProfileItemPEOProfileItemId | PROFILE_ITEM_ID | 🔑 | ✅ |
| 81 | ProfileItemPEORatingLevelId1 | RATING_LEVEL_ID1 | — | ✅ |
| 82 | ProfileItemPEORatingLevelId2 | RATING_LEVEL_ID2 | — | ✅ |
| 83 | ProfileItemPEORatingLevelId3 | RATING_LEVEL_ID3 | — | ✅ |
| 84 | ProfileItemPEORatingModelId1 | RATING_MODEL_ID1 | — | ✅ |
| 85 | ProfileItemPEORatingModelId2 | RATING_MODEL_ID2 | — | ✅ |
| 86 | ProfileItemPEORatingModelId3 | RATING_MODEL_ID3 | — | ✅ |
| 87 | ProfileItemPEOStateProvinceId | STATE_PROVINCE_ID | — | ✅ |
| 88 | QualifierId1 | QUALIFIER_ID1 | — | ✅ |
| 89 | QualifierId2 | QUALIFIER_ID2 | — | ✅ |
| 90 | SectionId | SECTION_ID | — | — |
| 91 | SourceId | SOURCE_ID | — | ✅ |
| 92 | SourceKey1 | SOURCE_KEY1 | — | ✅ |
| 93 | SourceKey2 | SOURCE_KEY2 | — | ✅ |
| 94 | SourceKey3 | SOURCE_KEY3 | — | ✅ |
| 95 | SourceType | SOURCE_TYPE | — | ✅ |

### [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PTSBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | PTSCreatedBy1 | CREATED_BY | — | — |
| 3 | PTSCreationDate1 | CREATION_DATE | — | — |
| 4 | PTSSectionId1 | SECTION_ID | — | ✅ |
| 5 | ProfileTypeSectionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ProfileTypeSectionPEOName | NAME | — | ✅ |
| 7 | SectionContext | SECTION_CONTEXT | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
