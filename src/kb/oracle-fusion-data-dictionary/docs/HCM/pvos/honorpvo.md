---
id: DOC-HCM-PVO-HonorPVO
doc_type: system-doc
title: "HonorPVO — PVO Human Capital Management"
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
  - HonorPVO
  - honorpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HonorPVO

## 📌 Visão Geral

Consolida honrarias e premiações no perfil do colaborador com tipos de conteúdo e ratings. Suporta gestão de reconhecimento e meritocracia.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileCoreAM.HonorPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 235 | 10 | 1 | 38 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_bi_honor_items_v|HRT_BI_HONOR_ITEMS_V]] — 101 atributos (1 PKs, 24 BICC)
- [[hrt_content_items_b|HRT_CONTENT_ITEMS_B]] — 64 atributos (1 BICC)
- [[hrt_content_items_tl|HRT_CONTENT_ITEMS_TL]] — 30 atributos (3 BICC)
- [[hrt_content_types_b|HRT_CONTENT_TYPES_B]] — 6 atributos (2 BICC)
- [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]] — 7 atributos (2 BICC)
- [[hrt_establishments_b|HRT_ESTABLISHMENTS_B]] — 5 atributos (1 BICC)
- [[hrt_establishments_tl|HRT_ESTABLISHMENTS_TL]] — 7 atributos (2 BICC)
- [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]] — 8 atributos (2 BICC)
- [[hrt_sources_b|HRT_SOURCES_B]] — 3 atributos
- [[hrt_sources_tl|HRT_SOURCES_TL]] — 4 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hrt_bi_honor_items_v|HRT_BI_HONOR_ITEMS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContextName | CONTEXT_NAME | — | — |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | HonorPIItemClob1 | ITEM_CLOB_1 | — | — |
| 5 | HonorPIItemClob2 | ITEM_CLOB_2 | — | — |
| 6 | HonorPIItemText20001 | ITEM_TEXT2000_1 | — | ✅ |
| 7 | InterestLevel | INTEREST_LEVEL | — | ✅ |
| 8 | ItemClob3 | ITEM_CLOB_3 | — | — |
| 9 | ItemClob4 | ITEM_CLOB_4 | — | — |
| 10 | ItemClob5 | ITEM_CLOB_5 | — | — |
| 11 | ItemDate3 | ITEM_DATE_3 | — | — |
| 12 | ItemDecimal1 | ITEM_DECIMAL_1 | — | — |
| 13 | ItemDecimal2 | ITEM_DECIMAL_2 | — | — |
| 14 | ItemDecimal3 | ITEM_DECIMAL_3 | — | — |
| 15 | ItemDecimal4 | ITEM_DECIMAL_4 | — | — |
| 16 | ItemDecimal5 | ITEM_DECIMAL_5 | — | — |
| 17 | ItemText20001 | ITEM_TEXT2000_1 | — | — |
| 18 | ItemText20002 | ITEM_TEXT2000_2 | — | ✅ |
| 19 | ItemText20003 | ITEM_TEXT2000_3 | — | ✅ |
| 20 | ItemText20004 | ITEM_TEXT2000_4 | — | — |
| 21 | ItemText20005 | ITEM_TEXT2000_5 | — | — |
| 22 | ItemText2401 | ITEM_TEXT240_1 | — | ✅ |
| 23 | ItemText24010 | ITEM_TEXT240_10 | — | — |
| 24 | ItemText24011 | ITEM_TEXT240_11 | — | — |
| 25 | ItemText24012 | ITEM_TEXT240_12 | — | — |
| 26 | ItemText24013 | ITEM_TEXT240_13 | — | — |
| 27 | ItemText24014 | ITEM_TEXT240_14 | — | — |
| 28 | ItemText24015 | ITEM_TEXT240_15 | — | — |
| 29 | ItemText2402 | ITEM_TEXT240_2 | — | — |
| 30 | ItemText2403 | ITEM_TEXT240_3 | — | — |
| 31 | ItemText2404 | ITEM_TEXT240_4 | — | ✅ |
| 32 | ItemText2405 | ITEM_TEXT240_5 | — | ✅ |
| 33 | ItemText2406 | ITEM_TEXT240_6 | — | ✅ |
| 34 | ItemText2407 | ITEM_TEXT240_7 | — | — |
| 35 | ItemText2408 | ITEM_TEXT240_8 | — | — |
| 36 | ItemText2409 | ITEM_TEXT240_9 | — | — |
| 37 | ItemText301 | ITEM_TEXT30_1 | — | ✅ |
| 38 | ItemText3010 | ITEM_TEXT30_10 | — | — |
| 39 | ItemText3011 | ITEM_TEXT30_11 | — | — |
| 40 | ItemText3012 | ITEM_TEXT30_12 | — | — |
| 41 | ItemText3013 | ITEM_TEXT30_13 | — | — |
| 42 | ItemText3014 | ITEM_TEXT30_14 | — | — |
| 43 | ItemText3015 | ITEM_TEXT30_15 | — | — |
| 44 | ItemText302 | ITEM_TEXT30_2 | — | — |
| 45 | ItemText303 | ITEM_TEXT30_3 | — | — |
| 46 | ItemText304 | ITEM_TEXT30_4 | — | — |
| 47 | ItemText305 | ITEM_TEXT30_5 | — | — |
| 48 | ItemText306 | ITEM_TEXT30_6 | — | — |
| 49 | ItemText307 | ITEM_TEXT30_7 | — | — |
| 50 | ItemText308 | ITEM_TEXT30_8 | — | — |
| 51 | ItemText309 | ITEM_TEXT30_9 | — | — |
| 52 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 53 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 54 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 55 | Mandatory | MANDATORY | — | ✅ |
| 56 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 57 | ProfileItemPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 58 | ProfileItemPEOContentItemId | CONTENT_ITEM_ID | — | — |
| 59 | ProfileItemPEOContentTypeId | CONTENT_TYPE_ID | — | ✅ |
| 60 | ProfileItemPEOCountryId | COUNTRY_ID | — | ✅ |
| 61 | ProfileItemPEODateFrom | DATE_FROM | — | ✅ |
| 62 | ProfileItemPEODateTo | DATE_TO | — | ✅ |
| 63 | ProfileItemPEOImportance | IMPORTANCE | — | ✅ |
| 64 | ProfileItemPEOItemDate1 | ITEM_DATE_1 | — | ✅ |
| 65 | ProfileItemPEOItemDate10 | ITEM_DATE_10 | — | — |
| 66 | ProfileItemPEOItemDate2 | ITEM_DATE_2 | — | ✅ |
| 67 | ProfileItemPEOItemDate3 | ITEM_DATE_3 | — | ✅ |
| 68 | ProfileItemPEOItemDate4 | ITEM_DATE_4 | — | — |
| 69 | ProfileItemPEOItemDate5 | ITEM_DATE_5 | — | — |
| 70 | ProfileItemPEOItemDate6 | ITEM_DATE_6 | — | ✅ |
| 71 | ProfileItemPEOItemDate7 | ITEM_DATE_7 | — | — |
| 72 | ProfileItemPEOItemDate8 | ITEM_DATE_8 | — | — |
| 73 | ProfileItemPEOItemDate9 | ITEM_DATE_9 | — | — |
| 74 | ProfileItemPEOItemNumber1 | ITEM_NUMBER_1 | — | — |
| 75 | ProfileItemPEOItemNumber10 | ITEM_NUMBER_10 | — | — |
| 76 | ProfileItemPEOItemNumber2 | ITEM_NUMBER_2 | — | — |
| 77 | ProfileItemPEOItemNumber3 | ITEM_NUMBER_3 | — | — |
| 78 | ProfileItemPEOItemNumber4 | ITEM_NUMBER_4 | — | ✅ |
| 79 | ProfileItemPEOItemNumber5 | ITEM_NUMBER_5 | — | — |
| 80 | ProfileItemPEOItemNumber6 | ITEM_NUMBER_6 | — | — |
| 81 | ProfileItemPEOItemNumber7 | ITEM_NUMBER_7 | — | — |
| 82 | ProfileItemPEOItemNumber8 | ITEM_NUMBER_8 | — | — |
| 83 | ProfileItemPEOItemNumber9 | ITEM_NUMBER_9 | — | — |
| 84 | ProfileItemPEOParentProfileItemId | PARENT_PROFILE_ITEM_ID | — | — |
| 85 | ProfileItemPEOProfileId | PROFILE_ID | — | ✅ |
| 86 | ProfileItemPEOProfileItemId | PROFILE_ITEM_ID | 🔑 | ✅ |
| 87 | ProfileItemPEORatingLevelId1 | RATING_LEVEL_ID1 | — | — |
| 88 | ProfileItemPEORatingLevelId2 | RATING_LEVEL_ID2 | — | — |
| 89 | ProfileItemPEORatingLevelId3 | RATING_LEVEL_ID3 | — | — |
| 90 | ProfileItemPEORatingModelId1 | RATING_MODEL_ID1 | — | — |
| 91 | ProfileItemPEORatingModelId2 | RATING_MODEL_ID2 | — | — |
| 92 | ProfileItemPEORatingModelId3 | RATING_MODEL_ID3 | — | — |
| 93 | ProfileItemPEOStateProvinceId | STATE_PROVINCE_ID | — | — |
| 94 | QualifierId1 | QUALIFIER_ID1 | — | — |
| 95 | QualifierId2 | QUALIFIER_ID2 | — | — |
| 96 | SectionId | SECTION_ID | — | ✅ |
| 97 | SourceId | SOURCE_ID | — | — |
| 98 | SourceKey1 | SOURCE_KEY1 | — | — |
| 99 | SourceKey2 | SOURCE_KEY2 | — | — |
| 100 | SourceKey3 | SOURCE_KEY3 | — | — |
| 101 | SourceType | SOURCE_TYPE | — | — |

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
| 1 | CITLPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ContentItemTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | ContentItemTranslationPEOContentItemId | CONTENT_ITEM_ID | — | — |
| 4 | ContentItemTranslationPEOItemDescription | ITEM_DESCRIPTION | — | — |
| 5 | ContentItemTranslationPEOItemDescrlong | ITEM_DESCRLONG | — | — |
| 6 | ContentItemTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ContentItemTranslationPEOName | NAME | — | — |
| 8 | ESTCITLEduEstablishmentName | NAME | — | ✅ |
| 9 | ESTLItemDescription | ITEM_DESCRIPTION | — | — |
| 10 | ESTLItemDescrlong | ITEM_DESCRLONG | — | — |
| 11 | EstlBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 12 | EstlContentItemId | CONTENT_ITEM_ID | — | — |
| 13 | EstlLanguage1 | LANGUAGE | — | — |
| 14 | ItemTextTl1 | ITEM_TEXT_TL_1 | — | — |
| 15 | ItemTextTl10 | ITEM_TEXT_TL_10 | — | — |
| 16 | ItemTextTl11 | ITEM_TEXT_TL_11 | — | — |
| 17 | ItemTextTl12 | ITEM_TEXT_TL_12 | — | — |
| 18 | ItemTextTl13 | ITEM_TEXT_TL_13 | — | — |
| 19 | ItemTextTl14 | ITEM_TEXT_TL_14 | — | — |
| 20 | ItemTextTl15 | ITEM_TEXT_TL_15 | — | — |
| 21 | ItemTextTl2 | ITEM_TEXT_TL_2 | — | — |
| 22 | ItemTextTl3 | ITEM_TEXT_TL_3 | — | — |
| 23 | ItemTextTl4 | ITEM_TEXT_TL_4 | — | — |
| 24 | ItemTextTl5 | ITEM_TEXT_TL_5 | — | — |
| 25 | ItemTextTl6 | ITEM_TEXT_TL_6 | — | — |
| 26 | ItemTextTl7 | ITEM_TEXT_TL_7 | — | — |
| 27 | ItemTextTl8 | ITEM_TEXT_TL_8 | — | — |
| 28 | ItemTextTl9 | ITEM_TEXT_TL_9 | — | — |
| 29 | Language | LANGUAGE | — | ✅ |
| 30 | SourceLang | SOURCE_LANG | — | — |

### [[hrt_content_types_b|HRT_CONTENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CTBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CTContentTypeId | CONTENT_TYPE_ID | — | ✅ |
| 3 | CTContextName1 | CONTEXT_NAME | — | — |
| 4 | CTFreeFormFlag | FREE_FORM_FLAG | — | — |
| 5 | ContentTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ContentTypeId | CONTENT_TYPE_ID | — | — |

### [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CTLBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | CTLContentDescription | CONTENT_DESCRIPTION | — | — |
| 4 | CTLContentTypeId | CONTENT_TYPE_ID | — | — |
| 5 | CTLContentTypeName | CONTENT_TYPE_NAME | — | ✅ |
| 6 | CTLLanguage1 | LANGUAGE | — | — |
| 7 | ContentTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_establishments_b|HRT_ESTABLISHMENTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EstablishmentBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | EstablishmentId | ESTABLISHMENT_ID | — | — |
| 3 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 4 | SchoolCode | SCHOOL_CODE | — | — |
| 5 | StateProvinceId | STATE_PROVINCE_ID | — | — |

### [[hrt_establishments_tl|HRT_ESTABLISHMENTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | — |
| 2 | EstablishmentId1 | ESTABLISHMENT_ID | — | — |
| 3 | EstablishmentTLName | NAME | — | ✅ |
| 4 | EstablishmentTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | Language1 | LANGUAGE | — | — |
| 6 | Location | LOCATION | — | — |
| 7 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |

### [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PTPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | PTPEOSectionId1 | SECTION_ID | — | — |
| 3 | PTPEOSectionItemReqdFlag | SECTION_ITEM_REQD_FLAG | — | — |
| 4 | ProfileTypeSectionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ProfileTypeSectionPEOName | NAME | — | ✅ |
| 6 | QualifierSetId1 | QUALIFIER_SET_ID1 | — | — |
| 7 | QualifierSetId2 | QUALIFIER_SET_ID2 | — | — |
| 8 | SectionContext | SECTION_CONTEXT | — | — |

### [[hrt_sources_b|HRT_SOURCES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | SourceCode | SOURCE_CODE | — | — |
| 3 | SourceId1 | SOURCE_ID | — | — |

### [[hrt_sources_tl|HRT_SOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 2 | Language2 | LANGUAGE | — | — |
| 3 | SourceDescription | SOURCE_DESCRIPTION | — | ✅ |
| 4 | SourceId2 | SOURCE_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
