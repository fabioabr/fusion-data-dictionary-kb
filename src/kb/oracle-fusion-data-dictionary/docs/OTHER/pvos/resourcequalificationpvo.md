---
id: DOC-OTHER-PVO-ResourceQualificationPVO
doc_type: system-doc
title: "ResourceQualificationPVO — PVO Cross-Module"
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
  - ResourceQualificationPVO
  - resourcequalificationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ResourceQualificationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Resource Qualification. Acessa as tabelas: HRT_CONTENT_ITEMS_VL, HRT_CONTENT_TYPES_VL, HRT_PROFILES_VL (+6).

**Caminho:** `FscmTopModelAM.PjrResourceAM.ResourceQualificationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 60 | 9 | 1 | 24 | 40% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_content_items_vl|HRT_CONTENT_ITEMS_VL]] — 8 atributos (4 BICC)
- [[hrt_content_types_vl|HRT_CONTENT_TYPES_VL]] — 5 atributos (3 BICC)
- [[hrt_profiles_vl|HRT_PROFILES_VL]] — 10 atributos (1 PKs, 1 BICC)
- [[hrt_profile_items|HRT_PROFILE_ITEMS]] — 11 atributos (2 BICC)
- [[hrt_profile_typ_sections|HRT_PROFILE_TYP_SECTIONS]] — 1 atributos
- [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]] — 1 atributos
- [[hrt_rating_levels_vl|HRT_RATING_LEVELS_VL]] — 18 atributos (12 BICC)
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 5 atributos (1 BICC)
- [[pjt_prj_enterprise_resource_b|PJT_PRJ_ENTERPRISE_RESOURCE_B]] — 1 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hrt_content_items_vl|HRT_CONTENT_ITEMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentItemId | CONTENT_ITEM_ID | — | — |
| 2 | ContentItemItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 3 | ContentItemPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | ContentItemPEOContentItemCode | CONTENT_ITEM_CODE | — | — |
| 5 | ContentItemPEOContentTypeId | CONTENT_TYPE_ID | — | — |
| 6 | ContentItemPEODateFrom | DATE_FROM | — | ✅ |
| 7 | ContentItemPEODateTo | DATE_TO | — | ✅ |
| 8 | ContentItemPEOName | NAME | — | ✅ |

### [[hrt_content_types_vl|HRT_CONTENT_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentTypeBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ContentTypeContentDescription | CONTENT_DESCRIPTION | — | ✅ |
| 3 | ContentTypeContentTypeName | CONTENT_TYPE_NAME | — | ✅ |
| 4 | ContentTypeContextName | CONTEXT_NAME | — | ✅ |
| 5 | ContentTypeId | CONTENT_TYPE_ID | — | — |

### [[hrt_profiles_vl|HRT_PROFILES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProfileId | PROFILE_ID | 🔑 | ✅ |
| 2 | ProfilePEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | ProfilePEODescription | DESCRIPTION | — | — |
| 4 | ProfilePEOOwnerPersonId | OWNER_PERSON_ID | — | — |
| 5 | ProfilePEOPartyId | PARTY_ID | — | — |
| 6 | ProfilePEOPersonId | PERSON_ID | — | — |
| 7 | ProfilePEOProfileCode | PROFILE_CODE | — | — |
| 8 | ProfilePEOProfileTypeId | PROFILE_TYPE_ID | — | — |
| 9 | ProfilePEOProfileUsageCode | PROFILE_USAGE_CODE | — | — |
| 10 | ProfilePEOSummary | SUMMARY | — | — |

### [[hrt_profile_items|HRT_PROFILE_ITEMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DateFrom | DATE_FROM | — | — |
| 2 | DateTo | DATE_TO | — | — |
| 3 | ProfileItemId | PROFILE_ITEM_ID | — | — |
| 4 | ProfileItemPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 5 | ProfileItemPEOContentItemId | CONTENT_ITEM_ID | — | ✅ |
| 6 | ProfileItemPEOContentTypeId | CONTENT_TYPE_ID | — | ✅ |
| 7 | ProfileItemPEOProfileId | PROFILE_ID | — | — |
| 8 | ProfileItemPEOSectionId | SECTION_ID | — | — |
| 9 | ProfileItemReadingRatingLevelId | RATING_LEVEL_ID2 | — | — |
| 10 | ProfileItemSpeakingRatingLevelId | RATING_LEVEL_ID1 | — | — |
| 11 | ProfileItemWritingRatingLevelId | RATING_LEVEL_ID3 | — | — |

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
| 1 | ReadingBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ReadingRatingDescription | RATING_DESCRIPTION | — | — |
| 3 | ReadingRatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 4 | ReadingRatingLevelId | RATING_LEVEL_ID | — | ✅ |
| 5 | ReadingRatingShortDescr | RATING_SHORT_DESCR | — | ✅ |
| 6 | ReadingStarRating | STAR_RATING | — | ✅ |
| 7 | SpeakingBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 8 | SpeakingRatingDescription | RATING_DESCRIPTION | — | — |
| 9 | SpeakingRatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 10 | SpeakingRatingLevelId | RATING_LEVEL_ID | — | ✅ |
| 11 | SpeakingRatingShortDescr | RATING_SHORT_DESCR | — | ✅ |
| 12 | SpeakingStarRating | STAR_RATING | — | ✅ |
| 13 | WritingBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 14 | WritingRatingDescription | RATING_DESCRIPTION | — | — |
| 15 | WritingRatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 16 | WritingRatingLevelId | RATING_LEVEL_ID | — | ✅ |
| 17 | WritingRatingShortDescr | RATING_SHORT_DESCR | — | ✅ |
| 18 | WritingStarRating | STAR_RATING | — | ✅ |

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | AssignmentDPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 3 | AssignmentDPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 4 | AssignmentDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | AssignmentId | ASSIGNMENT_ID | — | — |

### [[pjt_prj_enterprise_resource_b|PJT_PRJ_ENTERPRISE_RESOURCE_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResourceId | RESOURCE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
