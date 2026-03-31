---
id: DOC-OTHER-PVO-ProjRoleQualificationsPVO
doc_type: system-doc
title: "ProjRoleQualificationsPVO — PVO Cross-Module"
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
  - ProjRoleQualificationsPVO
  - projrolequalificationspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjRoleQualificationsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Proj Role Qualifications. Acessa as tabelas: HRT_CONTENT_ITEMS_VL, HRT_CONTENT_TYPES_VL, HRT_PROFILE_TYP_SECTIONS (+3).

**Caminho:** `FscmTopModelAM.PjrSetupAM.ProjRoleQualificationsPVO`

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
- [[pjr_proj_role_qualifications|PJR_PROJ_ROLE_QUALIFICATIONS]] — 16 atributos (1 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[hrt_content_items_vl|HRT_CONTENT_ITEMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentItemPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ContentItemPEOContentItemCode | CONTENT_ITEM_CODE | — | — |
| 3 | ContentItemPEOContentItemId | CONTENT_ITEM_ID | — | — |
| 4 | ContentItemPEODateFrom | DATE_FROM | — | ✅ |
| 5 | ContentItemPEODateTo | DATE_TO | — | ✅ |
| 6 | ContentItemPEOItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 7 | ContentItemPEOName | NAME | — | — |

### [[hrt_content_types_vl|HRT_CONTENT_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentDescription | CONTENT_DESCRIPTION | — | ✅ |
| 2 | ContentTypeContentTypeName | CONTENT_TYPE_NAME | — | ✅ |
| 3 | ContentTypePEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | ContentTypePEOContentTypeId | CONTENT_TYPE_ID | — | ✅ |
| 5 | ContentTypePEOContextName | CONTEXT_NAME | — | ✅ |

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
| 1 | RatingDescription | RATING_DESCRIPTION | — | — |
| 2 | RatingLevelBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | RatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 4 | RatingLevelId | RATING_LEVEL_ID | — | — |
| 5 | RatingShortDescr | RATING_SHORT_DESCR | — | ✅ |
| 6 | RatingStarRating | STAR_RATING | — | ✅ |
| 7 | ReadingBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 8 | ReadingRatingDescription | RATING_DESCRIPTION | — | — |
| 9 | ReadingRatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 10 | ReadingRatingLevelId | RATING_LEVEL_ID | — | — |
| 11 | ReadingRatingShortDescr | RATING_SHORT_DESCR | — | ✅ |
| 12 | ReadingStarRating | STAR_RATING | — | ✅ |
| 13 | SpeakingBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 14 | SpeakingRatingDescription | RATING_DESCRIPTION | — | — |
| 15 | SpeakingRatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 16 | SpeakingRatingLevelId | RATING_LEVEL_ID | — | — |
| 17 | SpeakingRatingShortDescr | RATING_SHORT_DESCR | — | ✅ |
| 18 | SpeakingStarRating | STAR_RATING | — | ✅ |
| 19 | WritingBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 20 | WritingRatingDescription | RATING_DESCRIPTION | — | — |
| 21 | WritingRatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 22 | WritingRatingLevelId | RATING_LEVEL_ID | — | — |
| 23 | WritingRatingShortDescr | RATING_SHORT_DESCR | — | ✅ |
| 24 | WritingStarRating | STAR_RATING | — | ✅ |

### [[pjr_proj_role_qualifications|PJR_PROJ_ROLE_QUALIFICATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjRoleQualificationPEOContentItemId | CONTENT_ITEM_ID | — | ✅ |
| 2 | ProjRoleQualificationPEOCreatedBy | CREATED_BY | — | — |
| 3 | ProjRoleQualificationPEOCreationDate | CREATION_DATE | — | — |
| 4 | ProjRoleQualificationPEOKeyword | KEYWORD | — | — |
| 5 | ProjRoleQualificationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ProjRoleQualificationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ProjRoleQualificationPEOMandatoryFlag | MANDATORY_FLAG | — | — |
| 8 | ProjRoleQualificationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ProjRoleQualificationPEOProjectRoleId | PROJECT_ROLE_ID | — | — |
| 10 | ProjRoleQualificationPEORatingLevelId | RATING_LEVEL_ID | — | ✅ |
| 11 | ProjRoleQualificationPEOReadingRatingLevelId | READING_RATING_LEVEL_ID | — | ✅ |
| 12 | ProjRoleQualificationPEOSectionId | SECTION_ID | — | — |
| 13 | ProjRoleQualificationPEOSpeakingRatingLevelId | SPEAKING_RATING_LEVEL_ID | — | ✅ |
| 14 | ProjRoleQualificationPEOUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | ProjRoleQualificationPEOWritingRatingLevelId | WRITING_RATING_LEVEL_ID | — | ✅ |
| 16 | ProjectRoleQualificationId | PROJECT_ROLE_QUALIFICATION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
