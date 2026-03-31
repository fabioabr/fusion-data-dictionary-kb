---
id: DOC-OTHER-PVO-MembershipPVO
doc_type: system-doc
title: "MembershipPVO — PVO Cross-Module"
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
  - MembershipPVO
  - membershippvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MembershipPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Membership. Acessa as tabelas: HRT_BI_MEMBERSHIP_ITEMS_V, HRT_CONTENT_ITEMS_B, HRT_CONTENT_ITEMS_TL (+7).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileCoreAM.MembershipPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 227 | 10 | 1 | 48 | 21% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_bi_membership_items_v|HRT_BI_MEMBERSHIP_ITEMS_V]] — 101 atributos (1 PKs, 35 BICC)
- [[hrt_content_items_b|HRT_CONTENT_ITEMS_B]] — 64 atributos (1 BICC)
- [[hrt_content_items_tl|HRT_CONTENT_ITEMS_TL]] — 29 atributos (4 BICC)
- [[hrt_content_types_b|HRT_CONTENT_TYPES_B]] — 4 atributos (1 BICC)
- [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]] — 6 atributos (1 BICC)
- [[hrt_establishments_b|HRT_ESTABLISHMENTS_B]] — 6 atributos (1 BICC)
- [[hrt_establishments_tl|HRT_ESTABLISHMENTS_TL]] — 6 atributos (2 BICC)
- [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]] — 4 atributos (2 BICC)
- [[hrt_sources_b|HRT_SOURCES_B]] — 3 atributos
- [[hrt_sources_tl|HRT_SOURCES_TL]] — 4 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hrt_bi_membership_items_v|HRT_BI_MEMBERSHIP_ITEMS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContextName | CONTEXT_NAME | — | — |
| 2 | CountryId | COUNTRY_ID | — | — |
| 3 | CreatedBy | CREATED_BY | — | — |
| 4 | CreationDate | CREATION_DATE | — | — |
| 5 | Importance | IMPORTANCE | — | ✅ |
| 6 | InterestLevel | INTEREST_LEVEL | — | — |
| 7 | ItemClob3 | ITEM_CLOB_3 | — | — |
| 8 | ItemClob4 | ITEM_CLOB_4 | — | — |
| 9 | ItemClob5 | ITEM_CLOB_5 | — | — |
| 10 | ItemDecimal1 | ITEM_DECIMAL_1 | — | — |
| 11 | ItemDecimal2 | ITEM_DECIMAL_2 | — | — |
| 12 | ItemDecimal3 | ITEM_DECIMAL_3 | — | — |
| 13 | ItemDecimal4 | ITEM_DECIMAL_4 | — | — |
| 14 | ItemDecimal5 | ITEM_DECIMAL_5 | — | — |
| 15 | ItemText20001 | ITEM_TEXT2000_1 | — | ✅ |
| 16 | ItemText20002 | ITEM_TEXT2000_2 | — | ✅ |
| 17 | ItemText20003 | ITEM_TEXT2000_3 | — | ✅ |
| 18 | ItemText20004 | ITEM_TEXT2000_4 | — | — |
| 19 | ItemText20005 | ITEM_TEXT2000_5 | — | — |
| 20 | ItemText2401 | ITEM_TEXT240_1 | — | ✅ |
| 21 | ItemText24010 | ITEM_TEXT240_10 | — | ✅ |
| 22 | ItemText24011 | ITEM_TEXT240_11 | — | ✅ |
| 23 | ItemText24012 | ITEM_TEXT240_12 | — | ✅ |
| 24 | ItemText24013 | ITEM_TEXT240_13 | — | ✅ |
| 25 | ItemText24014 | ITEM_TEXT240_14 | — | — |
| 26 | ItemText24015 | ITEM_TEXT240_15 | — | — |
| 27 | ItemText2402 | ITEM_TEXT240_2 | — | ✅ |
| 28 | ItemText2403 | ITEM_TEXT240_3 | — | ✅ |
| 29 | ItemText2404 | ITEM_TEXT240_4 | — | ✅ |
| 30 | ItemText2405 | ITEM_TEXT240_5 | — | ✅ |
| 31 | ItemText2406 | ITEM_TEXT240_6 | — | — |
| 32 | ItemText2407 | ITEM_TEXT240_7 | — | — |
| 33 | ItemText2408 | ITEM_TEXT240_8 | — | — |
| 34 | ItemText2409 | ITEM_TEXT240_9 | — | — |
| 35 | ItemText301 | ITEM_TEXT30_1 | — | ✅ |
| 36 | ItemText3010 | ITEM_TEXT30_10 | — | — |
| 37 | ItemText3011 | ITEM_TEXT30_11 | — | ✅ |
| 38 | ItemText3012 | ITEM_TEXT30_12 | — | — |
| 39 | ItemText3013 | ITEM_TEXT30_13 | — | — |
| 40 | ItemText3014 | ITEM_TEXT30_14 | — | — |
| 41 | ItemText3015 | ITEM_TEXT30_15 | — | — |
| 42 | ItemText302 | ITEM_TEXT30_2 | — | ✅ |
| 43 | ItemText303 | ITEM_TEXT30_3 | — | ✅ |
| 44 | ItemText304 | ITEM_TEXT30_4 | — | — |
| 45 | ItemText305 | ITEM_TEXT30_5 | — | — |
| 46 | ItemText306 | ITEM_TEXT30_6 | — | — |
| 47 | ItemText307 | ITEM_TEXT30_7 | — | ✅ |
| 48 | ItemText308 | ITEM_TEXT30_8 | — | — |
| 49 | ItemText309 | ITEM_TEXT30_9 | — | — |
| 50 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 51 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 52 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 53 | Mandatory | MANDATORY | — | ✅ |
| 54 | MembershipPIPEOItemClob1 | ITEM_CLOB_1 | — | — |
| 55 | MembershipPIPEOItemClob2 | ITEM_CLOB_2 | — | — |
| 56 | MembershipPIPEOItemText3010 | ITEM_TEXT30_10 | — | ✅ |
| 57 | MembershipPIPEOItemText309 | ITEM_TEXT30_9 | — | ✅ |
| 58 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 59 | ProfileItemPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 60 | ProfileItemPEOContentItemId | CONTENT_ITEM_ID | — | — |
| 61 | ProfileItemPEOContentTypeId | CONTENT_TYPE_ID | — | ✅ |
| 62 | ProfileItemPEODateFrom | DATE_FROM | — | ✅ |
| 63 | ProfileItemPEODateTo | DATE_TO | — | ✅ |
| 64 | ProfileItemPEOItemDate1 | ITEM_DATE_1 | — | — |
| 65 | ProfileItemPEOItemDate10 | ITEM_DATE_10 | — | — |
| 66 | ProfileItemPEOItemDate2 | ITEM_DATE_2 | — | ✅ |
| 67 | ProfileItemPEOItemDate3 | ITEM_DATE_3 | — | ✅ |
| 68 | ProfileItemPEOItemDate4 | ITEM_DATE_4 | — | — |
| 69 | ProfileItemPEOItemDate5 | ITEM_DATE_5 | — | ✅ |
| 70 | ProfileItemPEOItemDate6 | ITEM_DATE_6 | — | ✅ |
| 71 | ProfileItemPEOItemDate7 | ITEM_DATE_7 | — | ✅ |
| 72 | ProfileItemPEOItemDate8 | ITEM_DATE_8 | — | — |
| 73 | ProfileItemPEOItemDate9 | ITEM_DATE_9 | — | — |
| 74 | ProfileItemPEOItemNumber1 | ITEM_NUMBER_1 | — | ✅ |
| 75 | ProfileItemPEOItemNumber10 | ITEM_NUMBER_10 | — | — |
| 76 | ProfileItemPEOItemNumber2 | ITEM_NUMBER_2 | — | — |
| 77 | ProfileItemPEOItemNumber3 | ITEM_NUMBER_3 | — | — |
| 78 | ProfileItemPEOItemNumber4 | ITEM_NUMBER_4 | — | — |
| 79 | ProfileItemPEOItemNumber5 | ITEM_NUMBER_5 | — | — |
| 80 | ProfileItemPEOItemNumber6 | ITEM_NUMBER_6 | — | — |
| 81 | ProfileItemPEOItemNumber7 | ITEM_NUMBER_7 | — | — |
| 82 | ProfileItemPEOItemNumber8 | ITEM_NUMBER_8 | — | — |
| 83 | ProfileItemPEOItemNumber9 | ITEM_NUMBER_9 | — | — |
| 84 | ProfileItemPEOParentProfileItemId | PARENT_PROFILE_ITEM_ID | — | ✅ |
| 85 | ProfileItemPEOProfileId | PROFILE_ID | — | ✅ |
| 86 | ProfileItemPEOProfileItemId | PROFILE_ITEM_ID | 🔑 | ✅ |
| 87 | QualifierId1 | QUALIFIER_ID1 | — | — |
| 88 | QualifierId2 | QUALIFIER_ID2 | — | — |
| 89 | RatingLevelId1 | RATING_LEVEL_ID1 | — | — |
| 90 | RatingLevelId2 | RATING_LEVEL_ID2 | — | — |
| 91 | RatingLevelId3 | RATING_LEVEL_ID3 | — | — |
| 92 | RatingModelId1 | RATING_MODEL_ID1 | — | — |
| 93 | RatingModelId2 | RATING_MODEL_ID2 | — | — |
| 94 | RatingModelId3 | RATING_MODEL_ID3 | — | — |
| 95 | SectionId | SECTION_ID | — | ✅ |
| 96 | SourceId | SOURCE_ID | — | — |
| 97 | SourceKey1 | SOURCE_KEY1 | — | — |
| 98 | SourceKey2 | SOURCE_KEY2 | — | — |
| 99 | SourceKey3 | SOURCE_KEY3 | — | — |
| 100 | SourceType | SOURCE_TYPE | — | — |
| 101 | StateProvinceId | STATE_PROVINCE_ID | — | — |

### [[hrt_content_items_b|HRT_CONTENT_ITEMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentItemBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ContentItemBPEOContentItemCode | CONTENT_ITEM_CODE | — | — |
| 3 | ContentItemBPEOContentItemId | CONTENT_ITEM_ID | — | — |
| 4 | ContentItemBPEOContentTypeId | CONTENT_TYPE_ID | — | — |
| 5 | ContentItemBPEODateFrom | DATE_FROM | — | — |
| 6 | ContentItemBPEODateTo | DATE_TO | — | — |
| 7 | ContentItemBPEOItemDate1 | ITEM_DATE_1 | — | — |
| 8 | ContentItemBPEOItemDate10 | ITEM_DATE_10 | — | — |
| 9 | ContentItemBPEOItemDate2 | ITEM_DATE_2 | — | — |
| 10 | ContentItemBPEOItemDate3 | ITEM_DATE_3 | — | — |
| 11 | ContentItemBPEOItemDate4 | ITEM_DATE_4 | — | — |
| 12 | ContentItemBPEOItemDate5 | ITEM_DATE_5 | — | — |
| 13 | ContentItemBPEOItemDate6 | ITEM_DATE_6 | — | — |
| 14 | ContentItemBPEOItemDate7 | ITEM_DATE_7 | — | — |
| 15 | ContentItemBPEOItemDate8 | ITEM_DATE_8 | — | — |
| 16 | ContentItemBPEOItemDate9 | ITEM_DATE_9 | — | — |
| 17 | ContentItemBPEOItemNumber1 | ITEM_NUMBER_1 | — | — |
| 18 | ContentItemBPEOItemNumber10 | ITEM_NUMBER_10 | — | — |
| 19 | ContentItemBPEOItemNumber2 | ITEM_NUMBER_2 | — | — |
| 20 | ContentItemBPEOItemNumber3 | ITEM_NUMBER_3 | — | — |
| 21 | ContentItemBPEOItemNumber4 | ITEM_NUMBER_4 | — | — |
| 22 | ContentItemBPEOItemNumber5 | ITEM_NUMBER_5 | — | — |
| 23 | ContentItemBPEOItemNumber6 | ITEM_NUMBER_6 | — | — |
| 24 | ContentItemBPEOItemNumber7 | ITEM_NUMBER_7 | — | — |
| 25 | ContentItemBPEOItemNumber8 | ITEM_NUMBER_8 | — | — |
| 26 | ContentItemBPEOItemNumber9 | ITEM_NUMBER_9 | — | — |
| 27 | ContentItemBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | ContentItemBPEORatingModelId | RATING_MODEL_ID | — | — |
| 29 | ContentKeyflexId | CONTENT_KEYFLEX_ID | — | — |
| 30 | ContentSupplierCode | CONTENT_SUPPLIER_CODE | — | — |
| 31 | EstIdBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 32 | EstIdContentItemCode | CONTENT_ITEM_CODE | — | — |
| 33 | EstIdContentItemId | CONTENT_ITEM_ID | — | — |
| 34 | EstIdRatingModelId | RATING_MODEL_ID | — | — |
| 35 | ItemText1 | ITEM_TEXT_1 | — | — |
| 36 | ItemText10 | ITEM_TEXT_10 | — | — |
| 37 | ItemText11 | ITEM_TEXT_11 | — | — |
| 38 | ItemText12 | ITEM_TEXT_12 | — | — |
| 39 | ItemText13 | ITEM_TEXT_13 | — | — |
| 40 | ItemText14 | ITEM_TEXT_14 | — | — |
| 41 | ItemText15 | ITEM_TEXT_15 | — | — |
| 42 | ItemText16 | ITEM_TEXT_16 | — | — |
| 43 | ItemText17 | ITEM_TEXT_17 | — | — |
| 44 | ItemText18 | ITEM_TEXT_18 | — | — |
| 45 | ItemText19 | ITEM_TEXT_19 | — | — |
| 46 | ItemText2 | ITEM_TEXT_2 | — | — |
| 47 | ItemText20 | ITEM_TEXT_20 | — | — |
| 48 | ItemText21 | ITEM_TEXT_21 | — | — |
| 49 | ItemText22 | ITEM_TEXT_22 | — | — |
| 50 | ItemText23 | ITEM_TEXT_23 | — | — |
| 51 | ItemText24 | ITEM_TEXT_24 | — | — |
| 52 | ItemText25 | ITEM_TEXT_25 | — | — |
| 53 | ItemText26 | ITEM_TEXT_26 | — | — |
| 54 | ItemText27 | ITEM_TEXT_27 | — | — |
| 55 | ItemText28 | ITEM_TEXT_28 | — | — |
| 56 | ItemText29 | ITEM_TEXT_29 | — | — |
| 57 | ItemText3 | ITEM_TEXT_3 | — | — |
| 58 | ItemText30 | ITEM_TEXT_30 | — | — |
| 59 | ItemText4 | ITEM_TEXT_4 | — | — |
| 60 | ItemText5 | ITEM_TEXT_5 | — | — |
| 61 | ItemText6 | ITEM_TEXT_6 | — | — |
| 62 | ItemText7 | ITEM_TEXT_7 | — | — |
| 63 | ItemText8 | ITEM_TEXT_8 | — | — |
| 64 | ItemText9 | ITEM_TEXT_9 | — | — |

### [[hrt_content_items_tl|HRT_CONTENT_ITEMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentItemTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ContentItemTranslationPEOContentItemId | CONTENT_ITEM_ID | — | — |
| 3 | ContentItemTranslationPEOItemDescription | ITEM_DESCRIPTION | — | — |
| 4 | ContentItemTranslationPEOItemDescrlong | ITEM_DESCRLONG | — | — |
| 5 | ContentItemTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ContentItemTranslationPEOName | NAME | — | ✅ |
| 7 | ESTCITLEduEstablishmentName | NAME | — | ✅ |
| 8 | ESTLItemDescription | ITEM_DESCRIPTION | — | — |
| 9 | ESTLItemDescrlong | ITEM_DESCRLONG | — | — |
| 10 | EstlBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 11 | EstlContentItemId | CONTENT_ITEM_ID | — | — |
| 12 | EstlLanguage1 | LANGUAGE | — | — |
| 13 | ItemTextTl1 | ITEM_TEXT_TL_1 | — | — |
| 14 | ItemTextTl10 | ITEM_TEXT_TL_10 | — | — |
| 15 | ItemTextTl11 | ITEM_TEXT_TL_11 | — | — |
| 16 | ItemTextTl12 | ITEM_TEXT_TL_12 | — | — |
| 17 | ItemTextTl13 | ITEM_TEXT_TL_13 | — | — |
| 18 | ItemTextTl14 | ITEM_TEXT_TL_14 | — | — |
| 19 | ItemTextTl15 | ITEM_TEXT_TL_15 | — | — |
| 20 | ItemTextTl2 | ITEM_TEXT_TL_2 | — | — |
| 21 | ItemTextTl3 | ITEM_TEXT_TL_3 | — | — |
| 22 | ItemTextTl4 | ITEM_TEXT_TL_4 | — | — |
| 23 | ItemTextTl5 | ITEM_TEXT_TL_5 | — | — |
| 24 | ItemTextTl6 | ITEM_TEXT_TL_6 | — | — |
| 25 | ItemTextTl7 | ITEM_TEXT_TL_7 | — | — |
| 26 | ItemTextTl8 | ITEM_TEXT_TL_8 | — | — |
| 27 | ItemTextTl9 | ITEM_TEXT_TL_9 | — | — |
| 28 | Language | LANGUAGE | — | ✅ |
| 29 | SourceLang | SOURCE_LANG | — | — |

### [[hrt_content_types_b|HRT_CONTENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CTBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | CTContentTypeId | CONTENT_TYPE_ID | — | — |
| 3 | CTContextName1 | CONTEXT_NAME | — | — |
| 4 | ContentTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | ContentDescription | CONTENT_DESCRIPTION | — | — |
| 3 | ContentTypeId | CONTENT_TYPE_ID | — | — |
| 4 | ContentTypeName | CONTENT_TYPE_NAME | — | — |
| 5 | ContentTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | Language1 | LANGUAGE | — | — |

### [[hrt_establishments_b|HRT_ESTABLISHMENTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ESTCountryId1 | COUNTRY_ID | — | — |
| 2 | ESTEstablishmentId | ESTABLISHMENT_ID | — | — |
| 3 | ESTObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 4 | ESTSchoolCode | SCHOOL_CODE | — | — |
| 5 | ESTStateProvinceId1 | STATE_PROVINCE_ID | — | — |
| 6 | EstablishmentBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_establishments_tl|HRT_ESTABLISHMENTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ESTTLDescription | DESCRIPTION | — | ✅ |
| 2 | ESTTLEstablishmentId | ESTABLISHMENT_ID | — | — |
| 3 | ESTTLLanguage1 | LANGUAGE | — | — |
| 4 | ESTTLName | NAME | — | — |
| 5 | ESTTLObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 6 | EstablishmentTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ProfileTypeSectionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | ProfileTypeSectionPEOName | NAME | — | ✅ |
| 4 | SectionId1 | SECTION_ID | — | — |

### [[hrt_sources_b|HRT_SOURCES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 2 | SourceCode | SOURCE_CODE | — | — |
| 3 | SourceId1 | SOURCE_ID | — | — |

### [[hrt_sources_tl|HRT_SOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 2 | Language2 | LANGUAGE | — | — |
| 3 | SourceDescription | SOURCE_DESCRIPTION | — | ✅ |
| 4 | SourceId2 | SOURCE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
