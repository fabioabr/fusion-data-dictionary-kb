---
id: DOC-OTHER-PVO-ReadingRatingLevelPVO
doc_type: system-doc
title: "ReadingRatingLevelPVO — PVO Cross-Module"
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
  - ReadingRatingLevelPVO
  - readingratinglevelpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReadingRatingLevelPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Reading Rating Level. Acessa as tabelas: HRT_CONTENT_ITEMS_B, HRT_CONTENT_ITEMS_TL, HRT_CONTENT_TYPES_B (+3).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileSetupAM.ReadingRatingLevelPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 137 | 6 | 3 | 11 | 8% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_content_items_b|HRT_CONTENT_ITEMS_B]] — 60 atributos (1 PKs, 2 BICC)
- [[hrt_content_items_tl|HRT_CONTENT_ITEMS_TL]] — 23 atributos (1 BICC)
- [[hrt_content_types_b|HRT_CONTENT_TYPES_B]] — 6 atributos (1 BICC)
- [[hrt_profile_tp_sc_prp_b|HRT_PROFILE_TP_SC_PRP_B]] — 14 atributos (1 BICC)
- [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]] — 13 atributos (1 BICC)
- [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]] — 21 atributos (2 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[hrt_content_items_b|HRT_CONTENT_ITEMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentItemBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ContentItemBPEOContentItemCode | CONTENT_ITEM_CODE | — | — |
| 3 | ContentItemBPEOContentItemId | CONTENT_ITEM_ID | 🔑 | ✅ |
| 4 | ContentItemBPEOContentTypeId | CONTENT_TYPE_ID | — | — |
| 5 | ContentItemBPEODateFrom | DATE_FROM | — | — |
| 6 | ContentItemBPEODateTo | DATE_TO | — | — |
| 7 | ContentItemBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ContentItemBPEORatingModelId | RATING_MODEL_ID | — | — |
| 9 | ContentKeyflexId | CONTENT_KEYFLEX_ID | — | — |
| 10 | ContentSupplierCode | CONTENT_SUPPLIER_CODE | — | — |
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
| 21 | ItemNumber1 | ITEM_NUMBER_1 | — | — |
| 22 | ItemNumber10 | ITEM_NUMBER_10 | — | — |
| 23 | ItemNumber2 | ITEM_NUMBER_2 | — | — |
| 24 | ItemNumber3 | ITEM_NUMBER_3 | — | — |
| 25 | ItemNumber4 | ITEM_NUMBER_4 | — | — |
| 26 | ItemNumber5 | ITEM_NUMBER_5 | — | — |
| 27 | ItemNumber6 | ITEM_NUMBER_6 | — | — |
| 28 | ItemNumber7 | ITEM_NUMBER_7 | — | — |
| 29 | ItemNumber8 | ITEM_NUMBER_8 | — | — |
| 30 | ItemNumber9 | ITEM_NUMBER_9 | — | — |
| 31 | ItemText1 | ITEM_TEXT_1 | — | — |
| 32 | ItemText10 | ITEM_TEXT_10 | — | — |
| 33 | ItemText11 | ITEM_TEXT_11 | — | — |
| 34 | ItemText12 | ITEM_TEXT_12 | — | — |
| 35 | ItemText13 | ITEM_TEXT_13 | — | — |
| 36 | ItemText14 | ITEM_TEXT_14 | — | — |
| 37 | ItemText15 | ITEM_TEXT_15 | — | — |
| 38 | ItemText16 | ITEM_TEXT_16 | — | — |
| 39 | ItemText17 | ITEM_TEXT_17 | — | — |
| 40 | ItemText18 | ITEM_TEXT_18 | — | — |
| 41 | ItemText19 | ITEM_TEXT_19 | — | — |
| 42 | ItemText2 | ITEM_TEXT_2 | — | — |
| 43 | ItemText20 | ITEM_TEXT_20 | — | — |
| 44 | ItemText21 | ITEM_TEXT_21 | — | — |
| 45 | ItemText22 | ITEM_TEXT_22 | — | — |
| 46 | ItemText23 | ITEM_TEXT_23 | — | — |
| 47 | ItemText24 | ITEM_TEXT_24 | — | — |
| 48 | ItemText25 | ITEM_TEXT_25 | — | — |
| 49 | ItemText26 | ITEM_TEXT_26 | — | — |
| 50 | ItemText27 | ITEM_TEXT_27 | — | — |
| 51 | ItemText28 | ITEM_TEXT_28 | — | — |
| 52 | ItemText29 | ITEM_TEXT_29 | — | — |
| 53 | ItemText3 | ITEM_TEXT_3 | — | — |
| 54 | ItemText30 | ITEM_TEXT_30 | — | — |
| 55 | ItemText4 | ITEM_TEXT_4 | — | — |
| 56 | ItemText5 | ITEM_TEXT_5 | — | — |
| 57 | ItemText6 | ITEM_TEXT_6 | — | — |
| 58 | ItemText7 | ITEM_TEXT_7 | — | — |
| 59 | ItemText8 | ITEM_TEXT_8 | — | — |
| 60 | ItemText9 | ITEM_TEXT_9 | — | — |

### [[hrt_content_items_tl|HRT_CONTENT_ITEMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentItemTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ContentItemTranslationPEOContentItemId | CONTENT_ITEM_ID | — | — |
| 3 | ContentItemTranslationPEOItemDescription | ITEM_DESCRIPTION | — | — |
| 4 | ContentItemTranslationPEOItemDescrlong | ITEM_DESCRLONG | — | — |
| 5 | ContentItemTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ContentItemTranslationPEOName | NAME | — | — |
| 7 | ItemTextTl1 | ITEM_TEXT_TL_1 | — | — |
| 8 | ItemTextTl10 | ITEM_TEXT_TL_10 | — | — |
| 9 | ItemTextTl11 | ITEM_TEXT_TL_11 | — | — |
| 10 | ItemTextTl12 | ITEM_TEXT_TL_12 | — | — |
| 11 | ItemTextTl13 | ITEM_TEXT_TL_13 | — | — |
| 12 | ItemTextTl14 | ITEM_TEXT_TL_14 | — | — |
| 13 | ItemTextTl15 | ITEM_TEXT_TL_15 | — | — |
| 14 | ItemTextTl2 | ITEM_TEXT_TL_2 | — | — |
| 15 | ItemTextTl3 | ITEM_TEXT_TL_3 | — | — |
| 16 | ItemTextTl4 | ITEM_TEXT_TL_4 | — | — |
| 17 | ItemTextTl5 | ITEM_TEXT_TL_5 | — | — |
| 18 | ItemTextTl6 | ITEM_TEXT_TL_6 | — | — |
| 19 | ItemTextTl7 | ITEM_TEXT_TL_7 | — | — |
| 20 | ItemTextTl8 | ITEM_TEXT_TL_8 | — | — |
| 21 | ItemTextTl9 | ITEM_TEXT_TL_9 | — | — |
| 22 | Language | LANGUAGE | — | — |
| 23 | SourceLang | SOURCE_LANG | — | — |

### [[hrt_content_types_b|HRT_CONTENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentTypeBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ContentTypeBPEOContentTypeId | CONTENT_TYPE_ID | — | — |
| 3 | ContentTypeBPEOContextName | CONTEXT_NAME | — | — |
| 4 | ContentTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ContentTypeBPEOModuleId | MODULE_ID | — | — |
| 6 | FreeFormFlag | FREE_FORM_FLAG | — | — |

### [[hrt_profile_tp_sc_prp_b|HRT_PROFILE_TP_SC_PRP_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DisplayFlag | DISPLAY_FLAG | — | — |
| 2 | FieldName | FIELD_NAME | — | — |
| 3 | ProfileTpScPrpBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | ProfileTpScPrpBPEOColumnName | COLUMN_NAME | — | — |
| 5 | ProfileTpScPrpBPEODefaultValue | DEFAULT_VALUE | — | — |
| 6 | ProfileTpScPrpBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ProfileTpScPrpBPEOModuleId | MODULE_ID | — | — |
| 8 | ProfileTpScPrpBPEOSectionId | SECTION_ID | — | — |
| 9 | ProfileTpScPrpBPEOSectionPropId | SECTION_PROP_ID | — | — |
| 10 | PropertySource | PROPERTY_SOURCE | — | — |
| 11 | RequiredFlag | REQUIRED_FLAG | — | — |
| 12 | SearchFlag | SEARCH_FLAG | — | — |
| 13 | ValueSetName | VALUE_SET_NAME | — | — |
| 14 | ViewAttrbName | VIEW_ATTRB_NAME | — | — |

### [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApprovalRequiredFlag | APPROVAL_REQUIRED_FLAG | — | — |
| 2 | ProfileTypeSectionPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | ProfileTypeSectionPEOContentTypeId | CONTENT_TYPE_ID | — | — |
| 4 | ProfileTypeSectionPEOContentTypeRelationId | CONTENT_TYPE_RELATION_ID | — | — |
| 5 | ProfileTypeSectionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ProfileTypeSectionPEOModuleId | MODULE_ID | — | — |
| 7 | ProfileTypeSectionPEOParentSectionId | PARENT_SECTION_ID | — | — |
| 8 | ProfileTypeSectionPEOProfileTypeId | PROFILE_TYPE_ID | — | — |
| 9 | ProfileTypeSectionPEOSectionContext | SECTION_CONTEXT | — | — |
| 10 | ProfileTypeSectionPEOSectionId | SECTION_ID | — | — |
| 11 | QualifierSetId1 | QUALIFIER_SET_ID1 | — | — |
| 12 | QualifierSetId2 | QUALIFIER_SET_ID2 | — | — |
| 13 | SectionItemReqdFlag | SECTION_ITEM_REQD_FLAG | — | — |

### [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CareerStrDev | CAREER_STR_DEV | — | — |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | FromPoints | FROM_POINTS | — | — |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | NumericRating | NUMERIC_RATING | — | — |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | RatingLevelBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 11 | RatingLevelBPEODateFrom | DATE_FROM | — | — |
| 12 | RatingLevelBPEODateTo | DATE_TO | — | — |
| 13 | RatingLevelBPEOMaxRatingDistribution | MAX_RATING_DISTRIBUTION | — | — |
| 14 | RatingLevelBPEOMinRatingDistribution | MIN_RATING_DISTRIBUTION | — | — |
| 15 | RatingLevelBPEOModuleId | MODULE_ID | — | — |
| 16 | RatingLevelBPEORatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 17 | RatingLevelBPEORatingLevelId | RATING_LEVEL_ID | 🔑 | ✅ |
| 18 | RatingLevelBPEORatingModelId | RATING_MODEL_ID | — | ✅ |
| 19 | RatingLevelBPEOStarRating | STAR_RATING | — | — |
| 20 | ReviewPoints | REVIEW_POINTS | — | — |
| 21 | ToPoints | TO_POINTS | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
