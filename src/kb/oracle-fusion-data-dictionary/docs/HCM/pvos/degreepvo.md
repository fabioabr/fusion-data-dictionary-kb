---
id: DOC-HCM-PVO-DegreePVO
doc_type: system-doc
title: "DegreePVO — PVO Human Capital Management"
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
  - DegreePVO
  - degreepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DegreePVO

## 📌 Visão Geral

Extrai graus academicos de perfis de colaboradores com instituicao, conteudo e secoes. Suporta gestao de formacao educacional e requisitos de cargo.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileCoreAM.DegreePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 246 | 10 | 1 | 70 | 28% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_bi_education_items_v|HRT_BI_EDUCATION_ITEMS_V]] — 120 atributos (1 PKs, 51 BICC)
- [[hrt_content_items_b|HRT_CONTENT_ITEMS_B]] — 62 atributos (3 BICC)
- [[hrt_content_items_tl|HRT_CONTENT_ITEMS_TL]] — 29 atributos (5 BICC)
- [[hrt_content_types_b|HRT_CONTENT_TYPES_B]] — 3 atributos (1 BICC)
- [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]] — 6 atributos (3 BICC)
- [[hrt_establishments_b|HRT_ESTABLISHMENTS_B]] — 7 atributos (1 BICC)
- [[hrt_establishments_tl|HRT_ESTABLISHMENTS_TL]] — 6 atributos (2 BICC)
- [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]] — 4 atributos (2 BICC)
- [[hrt_sources_b|HRT_SOURCES_B]] — 4 atributos (1 BICC)
- [[hrt_sources_tl|HRT_SOURCES_TL]] — 5 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hrt_bi_education_items_v|HRT_BI_EDUCATION_ITEMS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContextName | CONTEXT_NAME | — | — |
| 2 | CountryCode | COUNTRY_CODE | — | — |
| 3 | CountryName | COUNTRY_NAME | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | — |
| 5 | CreationDate | CREATION_DATE | — | — |
| 6 | DegreePIItemText2408 | ITEM_TEXT240_8 | — | ✅ |
| 7 | DegreePIPEOItemClob1 | ITEM_CLOB_1 | — | — |
| 8 | DegreePIPEOItemClob3 | ITEM_CLOB_3 | — | — |
| 9 | DegreePIPEOItemClob4 | ITEM_CLOB_4 | — | — |
| 10 | DegreePIPEOItemText20002 | ITEM_TEXT2000_2 | — | ✅ |
| 11 | DegreePIPEOItemText24010 | ITEM_TEXT240_10 | — | ✅ |
| 12 | DegreePIPEOItemText24011 | ITEM_TEXT240_11 | — | ✅ |
| 13 | DegreePIPEOItemText2403 | ITEM_TEXT240_3 | — | ✅ |
| 14 | DegreePIPEOItemText2409 | ITEM_TEXT240_9 | — | ✅ |
| 15 | DegreePIPEOItemText3010 | ITEM_TEXT30_10 | — | ✅ |
| 16 | DegreePIPEOItemText3012 | ITEM_TEXT30_12 | — | ✅ |
| 17 | DegreePIPEOItemText3013 | ITEM_TEXT30_13 | — | ✅ |
| 18 | DegreePIPEOItemText304 | ITEM_TEXT30_4 | — | ✅ |
| 19 | DegreePIPEOItemText305 | ITEM_TEXT30_5 | — | ✅ |
| 20 | DegreePIPEOItemText306 | ITEM_TEXT30_6 | — | ✅ |
| 21 | DegreePIPEOItemText308 | ITEM_TEXT30_8 | — | ✅ |
| 22 | DegreePIPEOItemText309 | ITEM_TEXT30_9 | — | — |
| 23 | DegreePIPEOText2402 | ITEM_TEXT240_2 | — | ✅ |
| 24 | DegreeProfileItemPEOItemClob2 | ITEM_CLOB_2 | — | — |
| 25 | InterestLevel | INTEREST_LEVEL | — | ✅ |
| 26 | ItemDecimal1 | ITEM_DECIMAL_1 | — | ✅ |
| 27 | ItemDecimal1_MODL | ITEM_DECIMAL_1 | — | — |
| 28 | ItemDecimal2 | ITEM_DECIMAL_2 | — | — |
| 29 | ItemDecimal3 | ITEM_DECIMAL_3 | — | — |
| 30 | ItemDecimal4 | ITEM_DECIMAL_4 | — | — |
| 31 | ItemDecimal5 | ITEM_DECIMAL_5 | — | — |
| 32 | ItemText20001 | ITEM_TEXT2000_1 | — | ✅ |
| 33 | ItemText20002 | ITEM_TEXT2000_2 | — | — |
| 34 | ItemText20003 | ITEM_TEXT2000_3 | — | ✅ |
| 35 | ItemText20004 | ITEM_TEXT2000_4 | — | — |
| 36 | ItemText20005 | ITEM_TEXT2000_5 | — | ✅ |
| 37 | ItemText2401 | ITEM_TEXT240_1 | — | ✅ |
| 38 | ItemText24010 | ITEM_TEXT240_10 | — | — |
| 39 | ItemText24011 | ITEM_TEXT240_11 | — | — |
| 40 | ItemText24012 | ITEM_TEXT240_12 | — | ✅ |
| 41 | ItemText24013 | ITEM_TEXT240_13 | — | — |
| 42 | ItemText24014 | ITEM_TEXT240_14 | — | — |
| 43 | ItemText24015 | ITEM_TEXT240_15 | — | — |
| 44 | ItemText2402 | ITEM_TEXT240_2 | — | — |
| 45 | ItemText2403 | ITEM_TEXT240_3 | — | — |
| 46 | ItemText2404 | ITEM_TEXT240_4 | — | ✅ |
| 47 | ItemText2405 | ITEM_TEXT240_5 | — | ✅ |
| 48 | ItemText2406 | ITEM_TEXT240_6 | — | ✅ |
| 49 | ItemText2407 | ITEM_TEXT240_7 | — | ✅ |
| 50 | ItemText2408 | ITEM_TEXT240_8 | — | — |
| 51 | ItemText2409 | ITEM_TEXT240_9 | — | — |
| 52 | ItemText301 | ITEM_TEXT30_1 | — | ✅ |
| 53 | ItemText3010 | ITEM_TEXT30_10 | — | — |
| 54 | ItemText3011 | ITEM_TEXT30_11 | — | ✅ |
| 55 | ItemText3012 | ITEM_TEXT30_12 | — | — |
| 56 | ItemText3013 | ITEM_TEXT30_13 | — | — |
| 57 | ItemText3014 | ITEM_TEXT30_14 | — | — |
| 58 | ItemText3015 | ITEM_TEXT30_15 | — | — |
| 59 | ItemText301_MODL | ITEM_TEXT30_1 | — | — |
| 60 | ItemText302 | ITEM_TEXT30_2 | — | ✅ |
| 61 | ItemText303 | ITEM_TEXT30_3 | — | ✅ |
| 62 | ItemText304 | ITEM_TEXT30_4 | — | — |
| 63 | ItemText305 | ITEM_TEXT30_5 | — | — |
| 64 | ItemText306 | ITEM_TEXT30_6 | — | — |
| 65 | ItemText307 | ITEM_TEXT30_7 | — | ✅ |
| 66 | ItemText308 | ITEM_TEXT30_8 | — | — |
| 67 | ItemText309 | ITEM_TEXT30_9 | — | — |
| 68 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 69 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 70 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 71 | Mandatory | MANDATORY | — | ✅ |
| 72 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 73 | PIPEOParentProfileItemId | PARENT_PROFILE_ITEM_ID | — | — |
| 74 | ParentProfileItemId | PARENT_PROFILE_ITEM_ID | — | — |
| 75 | ProfileItemPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 76 | ProfileItemPEOContentItemId | CONTENT_ITEM_ID | — | — |
| 77 | ProfileItemPEOContentTypeId | CONTENT_TYPE_ID | — | ✅ |
| 78 | ProfileItemPEOCountryId | COUNTRY_ID | — | ✅ |
| 79 | ProfileItemPEODateFrom | DATE_FROM | — | ✅ |
| 80 | ProfileItemPEODateTo | DATE_TO | — | ✅ |
| 81 | ProfileItemPEOImportance | IMPORTANCE | — | ✅ |
| 82 | ProfileItemPEOItemDate1 | ITEM_DATE_1 | — | — |
| 83 | ProfileItemPEOItemDate10 | ITEM_DATE_10 | — | — |
| 84 | ProfileItemPEOItemDate2 | ITEM_DATE_2 | — | — |
| 85 | ProfileItemPEOItemDate3 | ITEM_DATE_3 | — | — |
| 86 | ProfileItemPEOItemDate4 | ITEM_DATE_4 | — | ✅ |
| 87 | ProfileItemPEOItemDate5 | ITEM_DATE_5 | — | — |
| 88 | ProfileItemPEOItemDate6 | ITEM_DATE_6 | — | ✅ |
| 89 | ProfileItemPEOItemDate7 | ITEM_DATE_7 | — | ✅ |
| 90 | ProfileItemPEOItemDate8 | ITEM_DATE_8 | — | ✅ |
| 91 | ProfileItemPEOItemDate9 | ITEM_DATE_9 | — | — |
| 92 | ProfileItemPEOItemNumber1 | ITEM_NUMBER_1 | — | ✅ |
| 93 | ProfileItemPEOItemNumber10 | ITEM_NUMBER_10 | — | — |
| 94 | ProfileItemPEOItemNumber2 | ITEM_NUMBER_2 | — | ✅ |
| 95 | ProfileItemPEOItemNumber3 | ITEM_NUMBER_3 | — | ✅ |
| 96 | ProfileItemPEOItemNumber4 | ITEM_NUMBER_4 | — | — |
| 97 | ProfileItemPEOItemNumber5 | ITEM_NUMBER_5 | — | — |
| 98 | ProfileItemPEOItemNumber6 | ITEM_NUMBER_6 | — | — |
| 99 | ProfileItemPEOItemNumber7 | ITEM_NUMBER_7 | — | — |
| 100 | ProfileItemPEOItemNumber8 | ITEM_NUMBER_8 | — | ✅ |
| 101 | ProfileItemPEOItemNumber9 | ITEM_NUMBER_9 | — | — |
| 102 | ProfileItemPEOProfileId | PROFILE_ID | — | ✅ |
| 103 | ProfileItemPEOProfileItemId | PROFILE_ITEM_ID | 🔑 | ✅ |
| 104 | ProfileItemPEORatingLevelId1 | RATING_LEVEL_ID1 | — | — |
| 105 | ProfileItemPEORatingLevelId2 | RATING_LEVEL_ID2 | — | — |
| 106 | ProfileItemPEORatingLevelId3 | RATING_LEVEL_ID3 | — | — |
| 107 | ProfileItemPEORatingModelId1 | RATING_MODEL_ID1 | — | — |
| 108 | ProfileItemPEORatingModelId2 | RATING_MODEL_ID2 | — | — |
| 109 | ProfileItemPEORatingModelId3 | RATING_MODEL_ID3 | — | — |
| 110 | ProfileItemPEOStateProvinceId | STATE_PROVINCE_ID | — | ✅ |
| 111 | QualifierId1 | QUALIFIER_ID1 | — | — |
| 112 | QualifierId2 | QUALIFIER_ID2 | — | — |
| 113 | SectionId | SECTION_ID | — | ✅ |
| 114 | SourceId | SOURCE_ID | — | — |
| 115 | SourceKey1 | SOURCE_KEY1 | — | — |
| 116 | SourceKey2 | SOURCE_KEY2 | — | — |
| 117 | SourceKey3 | SOURCE_KEY3 | — | — |
| 118 | SourceType | SOURCE_TYPE | — | — |
| 119 | StateProvinceCode | STATE_PROVINCE_CODE | — | — |
| 120 | StateProvinceName | STATE_PROVINCE_NAME | — | ✅ |

### [[hrt_content_items_b|HRT_CONTENT_ITEMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentItemBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ContentItemBPEOContentItemCode | CONTENT_ITEM_CODE | — | — |
| 3 | ContentItemBPEOContentItemId | CONTENT_ITEM_ID | — | ✅ |
| 4 | ContentItemBPEOContentTypeId | CONTENT_TYPE_ID | — | ✅ |
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
| 31 | ESTBusinessGroupId4 | BUSINESS_GROUP_ID | — | — |
| 32 | ESTContentItemId | CONTENT_ITEM_ID | — | — |
| 33 | ItemText1 | ITEM_TEXT_1 | — | — |
| 34 | ItemText10 | ITEM_TEXT_10 | — | — |
| 35 | ItemText11 | ITEM_TEXT_11 | — | — |
| 36 | ItemText12 | ITEM_TEXT_12 | — | — |
| 37 | ItemText13 | ITEM_TEXT_13 | — | — |
| 38 | ItemText14 | ITEM_TEXT_14 | — | — |
| 39 | ItemText15 | ITEM_TEXT_15 | — | — |
| 40 | ItemText16 | ITEM_TEXT_16 | — | — |
| 41 | ItemText17 | ITEM_TEXT_17 | — | — |
| 42 | ItemText18 | ITEM_TEXT_18 | — | — |
| 43 | ItemText19 | ITEM_TEXT_19 | — | — |
| 44 | ItemText2 | ITEM_TEXT_2 | — | — |
| 45 | ItemText20 | ITEM_TEXT_20 | — | — |
| 46 | ItemText21 | ITEM_TEXT_21 | — | — |
| 47 | ItemText22 | ITEM_TEXT_22 | — | — |
| 48 | ItemText23 | ITEM_TEXT_23 | — | — |
| 49 | ItemText24 | ITEM_TEXT_24 | — | — |
| 50 | ItemText25 | ITEM_TEXT_25 | — | — |
| 51 | ItemText26 | ITEM_TEXT_26 | — | — |
| 52 | ItemText27 | ITEM_TEXT_27 | — | — |
| 53 | ItemText28 | ITEM_TEXT_28 | — | — |
| 54 | ItemText29 | ITEM_TEXT_29 | — | — |
| 55 | ItemText3 | ITEM_TEXT_3 | — | — |
| 56 | ItemText30 | ITEM_TEXT_30 | — | — |
| 57 | ItemText4 | ITEM_TEXT_4 | — | — |
| 58 | ItemText5 | ITEM_TEXT_5 | — | — |
| 59 | ItemText6 | ITEM_TEXT_6 | — | — |
| 60 | ItemText7 | ITEM_TEXT_7 | — | — |
| 61 | ItemText8 | ITEM_TEXT_8 | — | — |
| 62 | ItemText9 | ITEM_TEXT_9 | — | — |

### [[hrt_content_items_tl|HRT_CONTENT_ITEMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentItemTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ContentItemTranslationPEOContentItemId | CONTENT_ITEM_ID | — | — |
| 3 | ContentItemTranslationPEOItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 4 | ContentItemTranslationPEOItemDescrlong | ITEM_DESCRLONG | — | — |
| 5 | ContentItemTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ContentItemTranslationPEOName | NAME | — | ✅ |
| 7 | ESTCITLSchoolName | NAME | — | ✅ |
| 8 | ESTLItemDescription | ITEM_DESCRIPTION | — | — |
| 9 | ESTTLBusinessGroupId5 | BUSINESS_GROUP_ID | — | — |
| 10 | ESTTLContentItemId1 | CONTENT_ITEM_ID | — | — |
| 11 | ESTTLItemDescrlong | ITEM_DESCRLONG | — | — |
| 12 | ESTTLLanguage4 | LANGUAGE | — | — |
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
| 1 | BusinessGroupId4 | BUSINESS_GROUP_ID | — | — |
| 2 | ContentTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | ContentTypeId1 | CONTENT_TYPE_ID | — | — |

### [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | ContentDescription | CONTENT_DESCRIPTION | — | — |
| 3 | ContentTypeId | CONTENT_TYPE_ID | — | ✅ |
| 4 | ContentTypeName | CONTENT_TYPE_NAME | — | ✅ |
| 5 | ContentTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | Language1 | LANGUAGE | — | — |

### [[hrt_establishments_b|HRT_ESTABLISHMENTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CountryId | COUNTRY_ID | — | — |
| 2 | EstablishmentBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | EstablishmentId1 | ESTABLISHMENT_ID | — | — |
| 4 | EstablishmentId2 | ESTABLISHMENT_ID | — | — |
| 5 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 6 | PartyId | PARTY_ID | — | — |
| 7 | SchoolCode | SCHOOL_CODE | — | — |

### [[hrt_establishments_tl|HRT_ESTABLISHMENTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | — |
| 2 | EstablishmentId | ESTABLISHMENT_ID | — | — |
| 3 | EstablishmentTLName | NAME | — | ✅ |
| 4 | EstablishmentTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | Language3 | LANGUAGE | — | — |
| 6 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |

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
| 1 | BusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 2 | SourceCode | SOURCE_CODE | — | — |
| 3 | SourceId2 | SOURCE_ID | — | — |
| 4 | SourcesBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_sources_tl|HRT_SOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 2 | Language2 | LANGUAGE | — | — |
| 3 | SourceDescription | SOURCE_DESCRIPTION | — | — |
| 4 | SourceId1 | SOURCE_ID | — | — |
| 5 | SourcesTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
