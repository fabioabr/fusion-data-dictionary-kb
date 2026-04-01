---
id: DOC-HCM-PVO-WorkRequirementDateCheckPVO
doc_type: system-doc
title: "WorkRequirementDateCheckPVO — PVO Human Capital Management"
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
  - WorkRequirementDateCheckPVO
  - workrequirementdatecheckpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkRequirementDateCheckPVO

## 📌 Visão Geral

Disponibiliza verificação de datas em requisitos de trabalho do perfil de talento. Valida vigência de preferências e requisitos profissionais do colaborador.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileCoreAM.WorkRequirementDateCheckPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 127 | 6 | 1 | 30 | 24% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_bi_work_preference_items_v|HRT_BI_WORK_PREFERENCE_ITEMS_V]] — 103 atributos (1 PKs, 28 BICC)
- [[hrt_content_types_b|HRT_CONTENT_TYPES_B]] — 5 atributos
- [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]] — 5 atributos
- [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]] — 5 atributos (2 BICC)
- [[hrt_sources_b|HRT_SOURCES_B]] — 4 atributos
- [[hrt_sources_tl|HRT_SOURCES_TL]] — 5 atributos

---

## ⚙️ Atributos

### [[hrt_bi_work_preference_items_v|HRT_BI_WORK_PREFERENCE_ITEMS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | Importance | IMPORTANCE | — | ✅ |
| 4 | InterestLevel | INTEREST_LEVEL | — | — |
| 5 | ItemDate1 | ITEM_DATE_1 | — | — |
| 6 | ItemDate10 | ITEM_DATE_10 | — | — |
| 7 | ItemDate2 | ITEM_DATE_2 | — | — |
| 8 | ItemDate3 | ITEM_DATE_3 | — | — |
| 9 | ItemDate4 | ITEM_DATE_4 | — | — |
| 10 | ItemDate5 | ITEM_DATE_5 | — | — |
| 11 | ItemDate6 | ITEM_DATE_6 | — | — |
| 12 | ItemDate7 | ITEM_DATE_7 | — | — |
| 13 | ItemDate8 | ITEM_DATE_8 | — | — |
| 14 | ItemDate9 | ITEM_DATE_9 | — | — |
| 15 | ItemDecimal1 | ITEM_DECIMAL_1 | — | ✅ |
| 16 | ItemDecimal2 | ITEM_DECIMAL_2 | — | — |
| 17 | ItemDecimal3 | ITEM_DECIMAL_3 | — | — |
| 18 | ItemDecimal4 | ITEM_DECIMAL_4 | — | — |
| 19 | ItemDecimal5 | ITEM_DECIMAL_5 | — | — |
| 20 | ItemNumber10 | ITEM_NUMBER_10 | — | ✅ |
| 21 | ItemNumber1_MODL | ITEM_NUMBER_1 | — | — |
| 22 | ItemNumber9 | ITEM_NUMBER_9 | — | ✅ |
| 23 | ItemText20001 | ITEM_TEXT2000_1 | — | — |
| 24 | ItemText20002 | ITEM_TEXT2000_2 | — | — |
| 25 | ItemText20003 | ITEM_TEXT2000_3 | — | — |
| 26 | ItemText20004 | ITEM_TEXT2000_4 | — | — |
| 27 | ItemText20005 | ITEM_TEXT2000_5 | — | — |
| 28 | ItemText2401 | ITEM_TEXT240_1 | — | ✅ |
| 29 | ItemText24010 | ITEM_TEXT240_10 | — | — |
| 30 | ItemText24011 | ITEM_TEXT240_11 | — | — |
| 31 | ItemText24012 | ITEM_TEXT240_12 | — | — |
| 32 | ItemText24013 | ITEM_TEXT240_13 | — | — |
| 33 | ItemText24014 | ITEM_TEXT240_14 | — | ✅ |
| 34 | ItemText24015 | ITEM_TEXT240_15 | — | ✅ |
| 35 | ItemText2402 | ITEM_TEXT240_2 | — | — |
| 36 | ItemText2403 | ITEM_TEXT240_3 | — | — |
| 37 | ItemText2404 | ITEM_TEXT240_4 | — | — |
| 38 | ItemText2405 | ITEM_TEXT240_5 | — | — |
| 39 | ItemText2406 | ITEM_TEXT240_6 | — | — |
| 40 | ItemText2407 | ITEM_TEXT240_7 | — | — |
| 41 | ItemText2408 | ITEM_TEXT240_8 | — | — |
| 42 | ItemText2409 | ITEM_TEXT240_9 | — | — |
| 43 | ItemText301 | ITEM_TEXT30_1 | — | ✅ |
| 44 | ItemText3010 | ITEM_TEXT30_10 | — | ✅ |
| 45 | ItemText3011 | ITEM_TEXT30_11 | — | ✅ |
| 46 | ItemText3012 | ITEM_TEXT30_12 | — | ✅ |
| 47 | ItemText3013 | ITEM_TEXT30_13 | — | — |
| 48 | ItemText3014 | ITEM_TEXT30_14 | — | ✅ |
| 49 | ItemText3015 | ITEM_TEXT30_15 | — | ✅ |
| 50 | ItemText301_MODL | ITEM_TEXT30_1 | — | — |
| 51 | ItemText302 | ITEM_TEXT30_2 | — | ✅ |
| 52 | ItemText302_MODL | ITEM_TEXT30_2 | — | — |
| 53 | ItemText303 | ITEM_TEXT30_3 | — | ✅ |
| 54 | ItemText303_MODL | ITEM_TEXT30_3 | — | — |
| 55 | ItemText304 | ITEM_TEXT30_4 | — | ✅ |
| 56 | ItemText304_MODL | ITEM_TEXT30_4 | — | — |
| 57 | ItemText305 | ITEM_TEXT30_5 | — | ✅ |
| 58 | ItemText306 | ITEM_TEXT30_6 | — | ✅ |
| 59 | ItemText307 | ITEM_TEXT30_7 | — | ✅ |
| 60 | ItemText308 | ITEM_TEXT30_8 | — | ✅ |
| 61 | ItemText309 | ITEM_TEXT30_9 | — | ✅ |
| 62 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 63 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 64 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 65 | Mandatory | MANDATORY | — | — |
| 66 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 67 | ParentProfileItemId | PARENT_PROFILE_ITEM_ID | — | — |
| 68 | ProfileItemPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 69 | ProfileItemPEOContentItemId | CONTENT_ITEM_ID | — | — |
| 70 | ProfileItemPEOContentTypeId | CONTENT_TYPE_ID | — | ✅ |
| 71 | ProfileItemPEOCountryId | COUNTRY_ID | — | — |
| 72 | ProfileItemPEODateFrom | DATE_FROM | — | ✅ |
| 73 | ProfileItemPEODateTo | DATE_TO | — | ✅ |
| 74 | ProfileItemPEOItemNumber1 | ITEM_NUMBER_1 | — | ✅ |
| 75 | ProfileItemPEOItemNumber2 | ITEM_NUMBER_2 | — | ✅ |
| 76 | ProfileItemPEOItemNumber3 | ITEM_NUMBER_3 | — | — |
| 77 | ProfileItemPEOItemNumber4 | ITEM_NUMBER_4 | — | — |
| 78 | ProfileItemPEOItemNumber5 | ITEM_NUMBER_5 | — | — |
| 79 | ProfileItemPEOItemNumber6 | ITEM_NUMBER_6 | — | — |
| 80 | ProfileItemPEOItemNumber7 | ITEM_NUMBER_7 | — | — |
| 81 | ProfileItemPEOItemNumber8 | ITEM_NUMBER_8 | — | — |
| 82 | ProfileItemPEOProfileId | PROFILE_ID | — | — |
| 83 | ProfileItemPEOProfileItemId | PROFILE_ITEM_ID | 🔑 | ✅ |
| 84 | ProfileItemPEORatingLevelId1 | RATING_LEVEL_ID1 | — | — |
| 85 | ProfileItemPEORatingLevelId2 | RATING_LEVEL_ID2 | — | — |
| 86 | ProfileItemPEORatingLevelId3 | RATING_LEVEL_ID3 | — | — |
| 87 | ProfileItemPEORatingModelId1 | RATING_MODEL_ID1 | — | — |
| 88 | ProfileItemPEORatingModelId2 | RATING_MODEL_ID2 | — | — |
| 89 | ProfileItemPEORatingModelId3 | RATING_MODEL_ID3 | — | — |
| 90 | ProfileItemPEOStateProvinceId | STATE_PROVINCE_ID | — | — |
| 91 | QualifierId1 | QUALIFIER_ID1 | — | — |
| 92 | QualifierId2 | QUALIFIER_ID2 | — | — |
| 93 | SourceId | SOURCE_ID | — | — |
| 94 | SourceKey1 | SOURCE_KEY1 | — | — |
| 95 | SourceKey2 | SOURCE_KEY2 | — | — |
| 96 | SourceKey3 | SOURCE_KEY3 | — | — |
| 97 | SourceType | SOURCE_TYPE | — | — |
| 98 | WorkReqPEOItemClob1 | ITEM_CLOB_1 | — | — |
| 99 | WorkReqPEOItemClob2 | ITEM_CLOB_2 | — | — |
| 100 | WorkReqPEOItemClob3 | ITEM_CLOB_3 | — | — |
| 101 | WorkReqPEOItemClob4 | ITEM_CLOB_4 | — | — |
| 102 | WorkReqPEOItemClob5 | ITEM_CLOB_5 | — | — |
| 103 | WorkReqPEOSectionId | SECTION_ID | — | — |

### [[hrt_content_types_b|HRT_CONTENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CTContextName | CONTEXT_NAME | — | — |
| 3 | ContentTypeId | CONTENT_TYPE_ID | — | — |
| 4 | ContentTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 5 | ContextName | CONTEXT_NAME | — | — |

### [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CTTLBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | CT_ContentTypeId1 | CONTENT_TYPE_ID | — | — |
| 3 | ContentTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 4 | ContentTypeName | CONTENT_TYPE_NAME | — | — |
| 5 | Language | LANGUAGE | — | — |

### [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PTSBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | PTSSectionId | SECTION_ID | — | ✅ |
| 3 | PTSSectionItemReqdFlag | SECTION_ITEM_REQD_FLAG | — | — |
| 4 | ProfileTypeSectionPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 5 | ProfileTypeSectionPEOName | NAME | — | ✅ |

### [[hrt_sources_b|HRT_SOURCES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | SourceCode | SOURCE_CODE | — | — |
| 3 | SourceId1 | SOURCE_ID | — | — |
| 4 | SourcesBPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |

### [[hrt_sources_tl|HRT_SOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 2 | Language1 | LANGUAGE | — | — |
| 3 | SourceDescription | SOURCE_DESCRIPTION | — | — |
| 4 | SourceId2 | SOURCE_ID | — | — |
| 5 | SourcesTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
