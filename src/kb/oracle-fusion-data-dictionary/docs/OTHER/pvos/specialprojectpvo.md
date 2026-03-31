---
id: DOC-OTHER-PVO-SpecialProjectPVO
doc_type: system-doc
title: "SpecialProjectPVO — PVO Cross-Module"
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
  - SpecialProjectPVO
  - specialprojectpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SpecialProjectPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Special Project. Acessa as tabelas: HRT_BI_SPECIAL_PRJ_ITEMS_V, HRT_CONTENT_ITEMS_B, HRT_CONTENT_ITEMS_TL (+4).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileCoreAM.SpecialProjectPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 159 | 7 | 2 | 25 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_bi_special_prj_items_v|HRT_BI_SPECIAL_PRJ_ITEMS_V]] — 106 atributos (1 PKs, 18 BICC)
- [[hrt_content_items_b|HRT_CONTENT_ITEMS_B]] — 9 atributos
- [[hrt_content_items_tl|HRT_CONTENT_ITEMS_TL]] — 5 atributos (2 BICC)
- [[hrt_content_types_b|HRT_CONTENT_TYPES_B]] — 9 atributos (1 PKs, 1 BICC)
- [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]] — 5 atributos (1 BICC)
- [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]] — 3 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 22 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hrt_bi_special_prj_items_v|HRT_BI_SPECIAL_PRJ_ITEMS_V]]

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
| 9 | ItemDate1 | ITEM_DATE_1 | — | ✅ |
| 10 | ItemDate10 | ITEM_DATE_10 | — | — |
| 11 | ItemDate2 | ITEM_DATE_2 | — | — |
| 12 | ItemDate3 | ITEM_DATE_3 | — | — |
| 13 | ItemDate4 | ITEM_DATE_4 | — | — |
| 14 | ItemDate5 | ITEM_DATE_5 | — | — |
| 15 | ItemDate6 | ITEM_DATE_6 | — | ✅ |
| 16 | ItemDate7 | ITEM_DATE_7 | — | — |
| 17 | ItemDate8 | ITEM_DATE_8 | — | — |
| 18 | ItemDate9 | ITEM_DATE_9 | — | — |
| 19 | ItemDecimal1 | ITEM_DECIMAL_1 | — | — |
| 20 | ItemDecimal2 | ITEM_DECIMAL_2 | — | — |
| 21 | ItemDecimal3 | ITEM_DECIMAL_3 | — | — |
| 22 | ItemDecimal4 | ITEM_DECIMAL_4 | — | — |
| 23 | ItemDecimal5 | ITEM_DECIMAL_5 | — | — |
| 24 | ItemNumber1 | ITEM_NUMBER_1 | — | — |
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
| 49 | ItemText2406 | ITEM_TEXT240_6 | — | ✅ |
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
| 73 | ProfileItemPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 74 | ProfileItemPEOContentItemId | CONTENT_ITEM_ID | — | — |
| 75 | ProfileItemPEOContentTypeId | CONTENT_TYPE_ID | — | ✅ |
| 76 | ProfileItemPEOCountryId | COUNTRY_ID | — | — |
| 77 | ProfileItemPEODateFrom | DATE_FROM | — | ✅ |
| 78 | ProfileItemPEODateTo | DATE_TO | — | ✅ |
| 79 | ProfileItemPEOItemNumber10 | ITEM_NUMBER_10 | — | — |
| 80 | ProfileItemPEOParentProfileItemId | PARENT_PROFILE_ITEM_ID | — | — |
| 81 | ProfileItemPEOProfileId | PROFILE_ID | — | — |
| 82 | ProfileItemPEOProfileItemId | PROFILE_ITEM_ID | 🔑 | ✅ |
| 83 | ProfileItemPEOStateProvinceId | STATE_PROVINCE_ID | — | — |
| 84 | QualifierId1 | QUALIFIER_ID1 | — | — |
| 85 | QualifierId2 | QUALIFIER_ID2 | — | — |
| 86 | RatingLevelId1 | RATING_LEVEL_ID1 | — | — |
| 87 | RatingLevelId2 | RATING_LEVEL_ID2 | — | — |
| 88 | RatingLevelId3 | RATING_LEVEL_ID3 | — | — |
| 89 | RatingModelId1 | RATING_MODEL_ID1 | — | — |
| 90 | RatingModelId2 | RATING_MODEL_ID2 | — | — |
| 91 | RatingModelId3 | RATING_MODEL_ID3 | — | — |
| 92 | SectionId | SECTION_ID | — | ✅ |
| 93 | SourceId | SOURCE_ID | — | — |
| 94 | SourceKey1 | SOURCE_KEY1 | — | — |
| 95 | SourceKey2 | SOURCE_KEY2 | — | — |
| 96 | SourceKey3 | SOURCE_KEY3 | — | — |
| 97 | SourceType | SOURCE_TYPE | — | — |
| 98 | SpecialPrjPEOPEOItemText20002 | ITEM_TEXT2000_2 | — | ✅ |
| 99 | SpecialPrjPIPEOItemClob1 | ITEM_CLOB_1 | — | — |
| 100 | SpecialPrjPIPEOItemClob2 | ITEM_CLOB_2 | — | — |
| 101 | SpecialPrjPIPEOItemText24010 | ITEM_TEXT240_10 | — | ✅ |
| 102 | SpecialPrjPIPEOItemText2402 | ITEM_TEXT240_2 | — | ✅ |
| 103 | SpecialPrjPIPEOItemText2403 | ITEM_TEXT240_3 | — | ✅ |
| 104 | SpecialPrjPIPEOItemText2404 | ITEM_TEXT240_4 | — | ✅ |
| 105 | SpecialPrjPIPEOItemText2407 | ITEM_TEXT240_7 | — | ✅ |
| 106 | SpecialPrjPIPEOItemText302 | ITEM_TEXT30_2 | — | ✅ |

### [[hrt_content_items_b|HRT_CONTENT_ITEMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CIBPEOBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | CIBPEOContentItemCode | CONTENT_ITEM_CODE | — | — |
| 3 | CIBPEOContentItemId | CONTENT_ITEM_ID | — | — |
| 4 | ContentKeyflexId | CONTENT_KEYFLEX_ID | — | — |
| 5 | ContentSupplierCode | CONTENT_SUPPLIER_CODE | — | — |
| 6 | ContentTypeId | CONTENT_TYPE_ID | — | — |
| 7 | CreatedBy1 | CREATED_BY | — | — |
| 8 | DateFrom | DATE_FROM | — | — |
| 9 | DateTo | DATE_TO | — | — |

### [[hrt_content_items_tl|HRT_CONTENT_ITEMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CTL_BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | CTL_ContentItemId | CONTENT_ITEM_ID | — | — |
| 3 | CTL_Language | LANGUAGE | — | — |
| 4 | CTL_LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 5 | ContentItemTranslationPEOName | NAME | — | ✅ |

### [[hrt_content_types_b|HRT_CONTENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CTBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | CTContentTypeId | CONTENT_TYPE_ID | — | — |
| 3 | CTContextName1 | CONTEXT_NAME | — | — |
| 4 | CTFreeFormFlag | FREE_FORM_FLAG | — | — |
| 5 | ContentTypeBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 6 | ContentTypeBPEOContentTypeId | CONTENT_TYPE_ID | 🔑 | ✅ |
| 7 | ContentTypeBPEOContextName | CONTEXT_NAME | — | — |
| 8 | ContentTypeBPEOFreeFormFlag | FREE_FORM_FLAG | — | — |
| 9 | ContentTypeBPEOModuleId | MODULE_ID | — | — |

### [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CTTLBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 2 | CTTLContentDescription | CONTENT_DESCRIPTION | — | — |
| 3 | CTTLContentTypeId1 | CONTENT_TYPE_ID | — | — |
| 4 | CTTLContentTypeName | CONTENT_TYPE_NAME | — | ✅ |
| 5 | CTTLLanguage | LANGUAGE | — | — |

### [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ProfileTypeSectionPEOName | NAME | — | ✅ |
| 3 | SectionId1 | SECTION_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 2 | Honors | HONORS | — | — |
| 3 | LegislationCode | LEGISLATION_CODE | — | — |
| 4 | ListName | LIST_NAME | — | — |
| 5 | MilitaryRank | MILITARY_RANK | — | — |
| 6 | OrderName | ORDER_NAME | — | — |
| 7 | PersonNameId | PERSON_NAME_ID | — | — |
| 8 | PersonNamePEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 9 | PersonNamePEODisplayName | DISPLAY_NAME | — | — |
| 10 | PersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 11 | PersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 12 | PersonNamePEOFirstName | FIRST_NAME | — | — |
| 13 | PersonNamePEOFullName | FULL_NAME | — | — |
| 14 | PersonNamePEOKnownAs | KNOWN_AS | — | — |
| 15 | PersonNamePEOLastName | LAST_NAME | — | — |
| 16 | PersonNamePEOMiddleNames | MIDDLE_NAMES | — | — |
| 17 | PersonNamePEOPersonId | PERSON_ID | — | — |
| 18 | PersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |
| 19 | PersonNamePEOSuffix | SUFFIX | — | — |
| 20 | PersonNamePEOTitle | TITLE | — | — |
| 21 | PreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 22 | PreviousLastName | PREVIOUS_LAST_NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
