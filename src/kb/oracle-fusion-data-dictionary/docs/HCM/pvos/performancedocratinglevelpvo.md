---
id: DOC-HCM-PVO-PerformanceDocRatingLevelPVO
doc_type: system-doc
title: "PerformanceDocRatingLevelPVO — PVO Human Capital Management"
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
  - PerformanceDocRatingLevelPVO
  - performancedocratinglevelpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PerformanceDocRatingLevelPVO

## 📌 Visão Geral

Disponibiliza níveis de rating (escala de avaliação) configurados para seções de documentos de desempenho. Define a escala de notas utilizada nas avaliações de performance.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPerformanceSetupAM.PerformanceDocRatingLevelPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 72 | 3 | 4 | 17 | 24% |

---

## 🔗 Tabelas Relacionadas

- [[hra_tmpl_sections|HRA_TMPL_SECTIONS]] — 50 atributos (2 PKs, 3 BICC)
- [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]] — 15 atributos (1 PKs, 10 BICC)
- [[hrt_rating_levels_tl|HRT_RATING_LEVELS_TL]] — 7 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[hra_tmpl_sections|HRA_TMPL_SECTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | ReferenceSectionId | REFERENCE_SECTION_ID | — | — |
| 9 | SectionId | SECTION_ID | 🔑 | ✅ |
| 10 | TemplateSectionPEOAddItemsConfirmCritFlag | ADD_ITEMS_CONFIRM_CRIT_FLAG | — | — |
| 11 | TemplateSectionPEOCalculationRuleCode | CALCULATION_RULE_CODE | — | — |
| 12 | TemplateSectionPEOContentProfileFlag | CONTENT_PROFILE_FLAG | — | — |
| 13 | TemplateSectionPEOContentTypeId | CONTENT_TYPE_ID | — | — |
| 14 | TemplateSectionPEODescription | DESCRIPTION | — | — |
| 15 | TemplateSectionPEOEnableItemsFlag | ENABLE_ITEMS_FLAG | — | — |
| 16 | TemplateSectionPEOFastFormulaId | FAST_FORMULA_ID | — | — |
| 17 | TemplateSectionPEOFreeFormAllowedFlag | FREE_FORM_ALLOWED_FLAG | — | — |
| 18 | TemplateSectionPEOItemCalculationCode | ITEM_CALCULATION_CODE | — | — |
| 19 | TemplateSectionPEOPerfRatingModelId | PERF_RATING_MODEL_ID | — | — |
| 20 | TemplateSectionPEOProfileId | PROFILE_ID | — | — |
| 21 | TemplateSectionPEOProfileTypeId | PROFILE_TYPE_ID | — | — |
| 22 | TemplateSectionPEORateItemFlag | RATE_ITEM_FLAG | — | — |
| 23 | TemplateSectionPEORateSectionFlag | RATE_SECTION_FLAG | — | — |
| 24 | TemplateSectionPEORatingTypeCode | RATING_TYPE_CODE | — | — |
| 25 | TemplateSectionPEOSectionDefId | SECTION_DEF_ID | — | — |
| 26 | TemplateSectionPEOSectionMinWeight | SECTION_MIN_WEIGHT | — | — |
| 27 | TemplateSectionPEOSectionRatingModelId | SECTION_RATING_MODEL_ID | — | — |
| 28 | TemplateSectionPEOSectionTypeCode | SECTION_TYPE_CODE | — | — |
| 29 | TemplateSectionPEOSectionWeight | SECTION_WEIGHT | — | — |
| 30 | TemplateSectionPEOSequenceNumber | SEQUENCE_NUMBER | — | — |
| 31 | TemplateSectionPEOShowCritical | SHOW_CRITICAL | — | — |
| 32 | TemplateSectionPEOShowDescription | SHOW_DESCRIPTION | — | — |
| 33 | TemplateSectionPEOShowDueDate | SHOW_DUE_DATE | — | — |
| 34 | TemplateSectionPEOShowMandatory | SHOW_MANDATORY | — | — |
| 35 | TemplateSectionPEOShowMeasurement | SHOW_MEASUREMENT | — | — |
| 36 | TemplateSectionPEOShowOwnedBy | SHOW_OWNED_BY | — | — |
| 37 | TemplateSectionPEOShowPercentComplete | SHOW_PERCENT_COMPLETE | — | — |
| 38 | TemplateSectionPEOShowReminderDate | SHOW_REMINDER_DATE | — | — |
| 39 | TemplateSectionPEOShowSectionMinWeight | SHOW_SECTION_MIN_WEIGHT | — | — |
| 40 | TemplateSectionPEOShowSectionWeight | SHOW_SECTION_WEIGHT | — | — |
| 41 | TemplateSectionPEOShowStatus | SHOW_STATUS | — | — |
| 42 | TemplateSectionPEOShowTargetPerfRtg | SHOW_TARGET_PERF_RTG | — | — |
| 43 | TemplateSectionPEOShowTargetProfLevel | SHOW_TARGET_PROF_LEVEL | — | — |
| 44 | TemplateSectionPEOTemplateDefnId | TEMPLATE_DEFN_ID | — | — |
| 45 | TemplateSectionPEOUseProfileFlag | USE_PROFILE_FLAG | — | — |
| 46 | TemplateSectionPEOUseSecrtgForPerfrtgFlag | USE_SECRTG_FOR_PERFRTG_FLAG | — | — |
| 47 | TemplateSectionPEOUseSpecContentItemFlag | USE_SPEC_CONTENT_ITEM_FLAG | — | — |
| 48 | TemplateSectionPEOUseSpecProfileFlag | USE_SPEC_PROFILE_FLAG | — | — |
| 49 | TemplateSectionPEOUseWorkerGoalsFlag | USE_WORKER_GOALS_FLAG | — | — |
| 50 | TemplateSectionPEOWeightSectionFlag | WEIGHT_SECTION_FLAG | — | — |

### [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RatingLevelBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | RatingLevelBPEOCareerStrDev | CAREER_STR_DEV | — | ✅ |
| 3 | RatingLevelBPEODateFrom | DATE_FROM | — | ✅ |
| 4 | RatingLevelBPEODateTo | DATE_TO | — | ✅ |
| 5 | RatingLevelBPEOFromPoints | FROM_POINTS | — | — |
| 6 | RatingLevelBPEOMaxRatingDistribution | MAX_RATING_DISTRIBUTION | — | ✅ |
| 7 | RatingLevelBPEOMinRatingDistribution | MIN_RATING_DISTRIBUTION | — | ✅ |
| 8 | RatingLevelBPEOModuleId | MODULE_ID | — | — |
| 9 | RatingLevelBPEONumericRating | NUMERIC_RATING | — | ✅ |
| 10 | RatingLevelBPEORatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 11 | RatingLevelBPEORatingModelId | RATING_MODEL_ID | — | ✅ |
| 12 | RatingLevelBPEOReviewPoints | REVIEW_POINTS | — | — |
| 13 | RatingLevelBPEOStarRating | STAR_RATING | — | ✅ |
| 14 | RatingLevelBPEOToPoints | TO_POINTS | — | — |
| 15 | RatingLevelId | RATING_LEVEL_ID | 🔑 | ✅ |

### [[hrt_rating_levels_tl|HRT_RATING_LEVELS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | RatingLevelTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | RatingLevelTranslationPEORatingDescription | RATING_DESCRIPTION | — | ✅ |
| 4 | RatingLevelTranslationPEORatingLevelId | RATING_LEVEL_ID | — | — |
| 5 | RatingLevelTranslationPEORatingShortDescr | RATING_SHORT_DESCR | — | ✅ |
| 6 | RatingLevelTranslationPEOReviewRatingDescr | REVIEW_RATING_DESCR | — | ✅ |
| 7 | SourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
