---
id: DOC-OTHER-PVO-ResourceRequestDetailsPVO
doc_type: system-doc
title: "ResourceRequestDetailsPVO — PVO Cross-Module"
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
  - ResourceRequestDetailsPVO
  - resourcerequestdetailspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ResourceRequestDetailsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Resource Request Details. Acessa as tabelas: HRT_CONTENT_ITEMS_VL, HRT_CONTENT_TYPES_VL, HRT_PROFILE_TYP_SECTIONS (+3).

**Caminho:** `FscmTopModelAM.PjrResourceRequestAM.ResourceRequestDetailsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 54 | 6 | 1 | 26 | 48% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_content_items_vl|HRT_CONTENT_ITEMS_VL]] — 7 atributos (3 BICC)
- [[hrt_content_types_vl|HRT_CONTENT_TYPES_VL]] — 5 atributos (4 BICC)
- [[hrt_profile_typ_sections|HRT_PROFILE_TYP_SECTIONS]] — 1 atributos
- [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]] — 1 atributos
- [[hrt_rating_levels_vl|HRT_RATING_LEVELS_VL]] — 24 atributos (12 BICC)
- [[pjr_resource_request_details|PJR_RESOURCE_REQUEST_DETAILS]] — 16 atributos (1 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[hrt_content_items_vl|HRT_CONTENT_ITEMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentItemBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ContentItemContentItemCode | CONTENT_ITEM_CODE | — | — |
| 3 | ContentItemContentItemId | CONTENT_ITEM_ID | — | — |
| 4 | ContentItemDateFrom | DATE_FROM | — | ✅ |
| 5 | ContentItemDateTo | DATE_TO | — | ✅ |
| 6 | ContentItemItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 7 | ContentItemPEOContentItemName | NAME | — | — |

### [[hrt_content_types_vl|HRT_CONTENT_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentTypeBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ContentTypeContentDescription | CONTENT_DESCRIPTION | — | ✅ |
| 3 | ContentTypeContentTypeId | CONTENT_TYPE_ID | — | ✅ |
| 4 | ContentTypeContentTypeName | CONTENT_TYPE_NAME | — | ✅ |
| 5 | ContentTypeContextName | CONTEXT_NAME | — | ✅ |

### [[hrt_profile_typ_sections|HRT_PROFILE_TYP_SECTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProfileTypeSectionPEOSectionId | SECTION_ID | — | — |

### [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProfileTypeSectionPEOName | NAME | — | — |

### [[hrt_rating_levels_vl|HRT_RATING_LEVELS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RatingLevelBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | RatingLevelRatingDescription | RATING_DESCRIPTION | — | — |
| 3 | RatingLevelRatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 4 | RatingLevelRatingLevelId | RATING_LEVEL_ID | — | — |
| 5 | RatingLevelShortDescr | RATING_SHORT_DESCR | — | ✅ |
| 6 | RatingLevelStarRating | STAR_RATING | — | ✅ |
| 7 | ReadingBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 8 | ReadingRatingDescr | RATING_DESCRIPTION | — | — |
| 9 | ReadingRatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 10 | ReadingRatingLevelId | RATING_LEVEL_ID | — | — |
| 11 | ReadingRatingShortDescr | RATING_SHORT_DESCR | — | ✅ |
| 12 | ReadingStarRating | STAR_RATING | — | ✅ |
| 13 | SpeakingBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 14 | SpeakingRatingDescr | RATING_DESCRIPTION | — | — |
| 15 | SpeakingRatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 16 | SpeakingRatingLevelId | RATING_LEVEL_ID | — | — |
| 17 | SpeakingRatingShortDescr | RATING_SHORT_DESCR | — | ✅ |
| 18 | SpeakingStarRating | STAR_RATING | — | ✅ |
| 19 | WritingBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 20 | WritingRatingDescr | RATING_DESCRIPTION | — | — |
| 21 | WritingRatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 22 | WritingRatingLevelId | RATING_LEVEL_ID | — | — |
| 23 | WritingRatingShortDescr | RATING_SHORT_DESCR | — | ✅ |
| 24 | WritingStarRating | STAR_RATING | — | ✅ |

### [[pjr_resource_request_details|PJR_RESOURCE_REQUEST_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequestDetailPEOContentItemId | CONTENT_ITEM_ID | — | ✅ |
| 2 | RequestDetailPEOCreatedBy | CREATED_BY | — | — |
| 3 | RequestDetailPEOCreationDate | CREATION_DATE | — | — |
| 4 | RequestDetailPEOKeyword | KEYWORD | — | — |
| 5 | RequestDetailPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | RequestDetailPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | RequestDetailPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | RequestDetailPEOMandatoryFlag | MANDATORY_FLAG | — | — |
| 9 | RequestDetailPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | RequestDetailPEORatingLevelId | RATING_LEVEL_ID | — | ✅ |
| 11 | RequestDetailPEOReadingRatingLevelId | READING_RATING_LEVEL_ID | — | ✅ |
| 12 | RequestDetailPEOResourceRequestId | RESOURCE_REQUEST_ID | — | — |
| 13 | RequestDetailPEOSectionId | SECTION_ID | — | — |
| 14 | RequestDetailPEOSpeakingRatingLevelId | SPEAKING_RATING_LEVEL_ID | — | ✅ |
| 15 | RequestDetailPEOWritingRatingLevelId | WRITING_RATING_LEVEL_ID | — | ✅ |
| 16 | ResourceRequestDetailId | RESOURCE_REQUEST_DETAIL_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
