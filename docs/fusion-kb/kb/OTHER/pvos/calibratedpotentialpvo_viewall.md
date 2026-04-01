---
id: DOC-OTHER-PVO-CalibratedPotentialPVO_Viewall
doc_type: system-doc
title: "CalibratedPotentialPVO_Viewall — PVO Cross-Module"
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
  - CalibratedPotentialPVO_Viewall
  - calibratedpotentialpvo_viewall
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CalibratedPotentialPVO_Viewall

## 📌 Visão Geral

View Object para extração BICC de dados de Calibrated Potential_Viewall. Acessa as tabelas: HRT_CONTENT_TYPES_B, HRT_PROFILES_B, HRT_PROFILE_ITEMS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileCoreAM.CalibratedPotentialPVO_Viewall`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 117 | 3 | 3 | 6 | 5% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_content_types_b|HRT_CONTENT_TYPES_B]] — 11 atributos (1 PKs, 2 BICC)
- [[hrt_profiles_b|HRT_PROFILES_B]] — 14 atributos (1 PKs, 2 BICC)
- [[hrt_profile_items|HRT_PROFILE_ITEMS]] — 92 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[hrt_content_types_b|HRT_CONTENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CTypeBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CTypeBPEOContentTypeId | CONTENT_TYPE_ID | 🔑 | ✅ |
| 3 | CTypeBPEOContextName | CONTEXT_NAME | — | — |
| 4 | CTypeBPEOCreatedBy | CREATED_BY | — | — |
| 5 | CTypeBPEOCreationDate | CREATION_DATE | — | — |
| 6 | CTypeBPEOFreeFormFlag | FREE_FORM_FLAG | — | — |
| 7 | CTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | CTypeBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | CTypeBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | CTypeBPEOModuleId | MODULE_ID | — | — |
| 11 | CTypeBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[hrt_profiles_b|HRT_PROFILES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProfileBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ProfileBPEOCreatedBy | CREATED_BY | — | — |
| 3 | ProfileBPEOCreationDate | CREATION_DATE | — | — |
| 4 | ProfileBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ProfileBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ProfileBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ProfileBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | ProfileBPEOOwnerPersonId | OWNER_PERSON_ID | — | — |
| 9 | ProfileBPEOPartyId | PARTY_ID | — | — |
| 10 | ProfileBPEOPersonId | PERSON_ID | — | — |
| 11 | ProfileBPEOProfileCode | PROFILE_CODE | — | — |
| 12 | ProfileBPEOProfileId | PROFILE_ID | 🔑 | ✅ |
| 13 | ProfileBPEOProfileTypeId | PROFILE_TYPE_ID | — | — |
| 14 | ProfileBPEOProfileUsageCode | PROFILE_USAGE_CODE | — | — |

### [[hrt_profile_items|HRT_PROFILE_ITEMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemDate1 | ITEM_DATE_1 | — | — |
| 2 | ItemDate10 | ITEM_DATE_10 | — | — |
| 3 | ItemDate2 | ITEM_DATE_2 | — | — |
| 4 | ItemDate3 | ITEM_DATE_3 | — | — |
| 5 | ItemDate4 | ITEM_DATE_4 | — | — |
| 6 | ItemDate5 | ITEM_DATE_5 | — | — |
| 7 | ItemDate6 | ITEM_DATE_6 | — | — |
| 8 | ItemDate7 | ITEM_DATE_7 | — | — |
| 9 | ItemDate8 | ITEM_DATE_8 | — | — |
| 10 | ItemDate9 | ITEM_DATE_9 | — | — |
| 11 | ItemDecimal1 | ITEM_DECIMAL_1 | — | — |
| 12 | ItemDecimal2 | ITEM_DECIMAL_2 | — | — |
| 13 | ItemDecimal3 | ITEM_DECIMAL_3 | — | — |
| 14 | ItemDecimal4 | ITEM_DECIMAL_4 | — | — |
| 15 | ItemDecimal5 | ITEM_DECIMAL_5 | — | — |
| 16 | ItemNumber1 | ITEM_NUMBER_1 | — | — |
| 17 | ItemNumber10 | ITEM_NUMBER_10 | — | — |
| 18 | ItemNumber2 | ITEM_NUMBER_2 | — | — |
| 19 | ItemNumber3 | ITEM_NUMBER_3 | — | — |
| 20 | ItemNumber4 | ITEM_NUMBER_4 | — | — |
| 21 | ItemNumber5 | ITEM_NUMBER_5 | — | — |
| 22 | ItemNumber6 | ITEM_NUMBER_6 | — | — |
| 23 | ItemNumber7 | ITEM_NUMBER_7 | — | — |
| 24 | ItemNumber8 | ITEM_NUMBER_8 | — | — |
| 25 | ItemNumber9 | ITEM_NUMBER_9 | — | — |
| 26 | ItemText20001 | ITEM_TEXT2000_1 | — | — |
| 27 | ItemText20002 | ITEM_TEXT2000_2 | — | — |
| 28 | ItemText20003 | ITEM_TEXT2000_3 | — | — |
| 29 | ItemText20004 | ITEM_TEXT2000_4 | — | — |
| 30 | ItemText20005 | ITEM_TEXT2000_5 | — | — |
| 31 | ItemText2401 | ITEM_TEXT240_1 | — | — |
| 32 | ItemText24010 | ITEM_TEXT240_10 | — | — |
| 33 | ItemText24011 | ITEM_TEXT240_11 | — | — |
| 34 | ItemText24012 | ITEM_TEXT240_12 | — | — |
| 35 | ItemText24013 | ITEM_TEXT240_13 | — | — |
| 36 | ItemText24014 | ITEM_TEXT240_14 | — | — |
| 37 | ItemText24015 | ITEM_TEXT240_15 | — | — |
| 38 | ItemText2402 | ITEM_TEXT240_2 | — | — |
| 39 | ItemText2403 | ITEM_TEXT240_3 | — | — |
| 40 | ItemText2404 | ITEM_TEXT240_4 | — | — |
| 41 | ItemText2405 | ITEM_TEXT240_5 | — | — |
| 42 | ItemText2406 | ITEM_TEXT240_6 | — | — |
| 43 | ItemText2407 | ITEM_TEXT240_7 | — | — |
| 44 | ItemText2408 | ITEM_TEXT240_8 | — | — |
| 45 | ItemText2409 | ITEM_TEXT240_9 | — | — |
| 46 | ItemText301 | ITEM_TEXT30_1 | — | — |
| 47 | ItemText3010 | ITEM_TEXT30_10 | — | — |
| 48 | ItemText3011 | ITEM_TEXT30_11 | — | — |
| 49 | ItemText3012 | ITEM_TEXT30_12 | — | — |
| 50 | ItemText3013 | ITEM_TEXT30_13 | — | — |
| 51 | ItemText3014 | ITEM_TEXT30_14 | — | — |
| 52 | ItemText3015 | ITEM_TEXT30_15 | — | — |
| 53 | ItemText302 | ITEM_TEXT30_2 | — | — |
| 54 | ItemText303 | ITEM_TEXT30_3 | — | — |
| 55 | ItemText304 | ITEM_TEXT30_4 | — | — |
| 56 | ItemText305 | ITEM_TEXT30_5 | — | — |
| 57 | ItemText306 | ITEM_TEXT30_6 | — | — |
| 58 | ItemText307 | ITEM_TEXT30_7 | — | — |
| 59 | ItemText308 | ITEM_TEXT30_8 | — | — |
| 60 | ItemText309 | ITEM_TEXT30_9 | — | — |
| 61 | ParentProfileItemId | PARENT_PROFILE_ITEM_ID | — | — |
| 62 | ProfileItemPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 63 | ProfileItemPEOContentItemId | CONTENT_ITEM_ID | — | — |
| 64 | ProfileItemPEOContentTypeId | CONTENT_TYPE_ID | — | — |
| 65 | ProfileItemPEOCountryId | COUNTRY_ID | — | — |
| 66 | ProfileItemPEOCreatedBy | CREATED_BY | — | — |
| 67 | ProfileItemPEOCreationDate | CREATION_DATE | — | — |
| 68 | ProfileItemPEODateFrom | DATE_FROM | — | — |
| 69 | ProfileItemPEODateTo | DATE_TO | — | — |
| 70 | ProfileItemPEOImportance | IMPORTANCE | — | — |
| 71 | ProfileItemPEOInterestLevel | INTEREST_LEVEL | — | — |
| 72 | ProfileItemPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 73 | ProfileItemPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 74 | ProfileItemPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 75 | ProfileItemPEOMandatory | MANDATORY | — | — |
| 76 | ProfileItemPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 77 | ProfileItemPEOProfileId | PROFILE_ID | — | — |
| 78 | ProfileItemPEOProfileItemId | PROFILE_ITEM_ID | 🔑 | ✅ |
| 79 | ProfileItemPEOQualifierId1 | QUALIFIER_ID1 | — | — |
| 80 | ProfileItemPEOQualifierId2 | QUALIFIER_ID2 | — | — |
| 81 | ProfileItemPEORatingLevelId1 | RATING_LEVEL_ID1 | — | — |
| 82 | ProfileItemPEORatingLevelId2 | RATING_LEVEL_ID2 | — | — |
| 83 | ProfileItemPEORatingLevelId3 | RATING_LEVEL_ID3 | — | — |
| 84 | ProfileItemPEORatingModelId1 | RATING_MODEL_ID1 | — | — |
| 85 | ProfileItemPEORatingModelId2 | RATING_MODEL_ID2 | — | — |
| 86 | ProfileItemPEORatingModelId3 | RATING_MODEL_ID3 | — | — |
| 87 | ProfileItemPEOSourceId | SOURCE_ID | — | — |
| 88 | ProfileItemPEOSourceKey1 | SOURCE_KEY1 | — | — |
| 89 | ProfileItemPEOSourceKey2 | SOURCE_KEY2 | — | — |
| 90 | ProfileItemPEOSourceKey3 | SOURCE_KEY3 | — | — |
| 91 | ProfileItemPEOSourceType | SOURCE_TYPE | — | — |
| 92 | ProfileItemPEOStateProvinceId | STATE_PROVINCE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
