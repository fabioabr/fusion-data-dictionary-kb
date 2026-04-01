---
id: DOC-OTHER-PVO-PotentialRatingLevelPVO
doc_type: system-doc
title: "PotentialRatingLevelPVO — PVO Cross-Module"
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
  - PotentialRatingLevelPVO
  - potentialratinglevelpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PotentialRatingLevelPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Potential Rating Level. Acessa as tabelas: HRT_CONTENT_TYPES_B, HRT_PROFILE_TP_SC_PRP_B, HRT_PROFILE_TYP_SECTIONS_VL (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileSetupAM.PotentialRatingLevelPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 54 | 4 | 8 | 13 | 24% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_content_types_b|HRT_CONTENT_TYPES_B]] — 6 atributos (2 PKs, 3 BICC)
- [[hrt_profile_tp_sc_prp_b|HRT_PROFILE_TP_SC_PRP_B]] — 14 atributos (2 PKs, 3 BICC)
- [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]] — 13 atributos (2 PKs, 3 BICC)
- [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]] — 21 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[hrt_content_types_b|HRT_CONTENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentTypeBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | ContentTypeBPEOContentTypeId | CONTENT_TYPE_ID | 🔑 | ✅ |
| 3 | ContentTypeBPEOContextName | CONTEXT_NAME | — | — |
| 4 | ContentTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ContentTypeBPEOModuleId | MODULE_ID | — | — |
| 6 | FreeFormFlag | FREE_FORM_FLAG | — | — |

### [[hrt_profile_tp_sc_prp_b|HRT_PROFILE_TP_SC_PRP_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DisplayFlag | DISPLAY_FLAG | — | — |
| 2 | FieldName | FIELD_NAME | — | — |
| 3 | ProfileTpScPrpBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 4 | ProfileTpScPrpBPEOColumnName | COLUMN_NAME | — | — |
| 5 | ProfileTpScPrpBPEODefaultValue | DEFAULT_VALUE | — | — |
| 6 | ProfileTpScPrpBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ProfileTpScPrpBPEOModuleId | MODULE_ID | — | — |
| 8 | ProfileTpScPrpBPEOSectionId | SECTION_ID | — | — |
| 9 | ProfileTpScPrpBPEOSectionPropId | SECTION_PROP_ID | 🔑 | ✅ |
| 10 | PropertySource | PROPERTY_SOURCE | — | — |
| 11 | RequiredFlag | REQUIRED_FLAG | — | — |
| 12 | SearchFlag | SEARCH_FLAG | — | — |
| 13 | ValueSetName | VALUE_SET_NAME | — | — |
| 14 | ViewAttrbName | VIEW_ATTRB_NAME | — | — |

### [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApprovalRequiredFlag | APPROVAL_REQUIRED_FLAG | — | — |
| 2 | ProfileTypeSectionPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 3 | ProfileTypeSectionPEOContentTypeId | CONTENT_TYPE_ID | — | — |
| 4 | ProfileTypeSectionPEOContentTypeRelationId | CONTENT_TYPE_RELATION_ID | — | — |
| 5 | ProfileTypeSectionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ProfileTypeSectionPEOModuleId | MODULE_ID | — | — |
| 7 | ProfileTypeSectionPEOParentSectionId | PARENT_SECTION_ID | — | — |
| 8 | ProfileTypeSectionPEOProfileTypeId | PROFILE_TYPE_ID | — | — |
| 9 | ProfileTypeSectionPEOSectionContext | SECTION_CONTEXT | — | — |
| 10 | ProfileTypeSectionPEOSectionId | SECTION_ID | 🔑 | ✅ |
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
| 18 | RatingLevelBPEORatingModelId | RATING_MODEL_ID | — | — |
| 19 | RatingLevelBPEOStarRating | STAR_RATING | — | — |
| 20 | ReviewPoints | REVIEW_POINTS | — | — |
| 21 | ToPoints | TO_POINTS | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
