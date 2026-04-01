---
id: DOC-OTHER-PVO-PerformanceDocSectionPVO
doc_type: system-doc
title: "PerformanceDocSectionPVO — PVO Cross-Module"
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
  - PerformanceDocSectionPVO
  - performancedocsectionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PerformanceDocSectionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Performance Doc Section. Acessa as tabelas: HRA_EVAL_SECTIONS, HRA_SECTION_DEFNS_B, HRA_SECTION_DEFNS_TL (+2).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPerformanceSetupAM.PerformanceDocSectionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 302 | 5 | 7 | 51 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[hra_eval_sections|HRA_EVAL_SECTIONS]] — 50 atributos (1 PKs, 3 BICC)
- [[hra_section_defns_b|HRA_SECTION_DEFNS_B]] — 114 atributos (2 PKs, 5 BICC)
- [[hra_section_defns_tl|HRA_SECTION_DEFNS_TL]] — 13 atributos (2 PKs, 4 BICC)
- [[hra_tmpl_sections|HRA_TMPL_SECTIONS]] — 117 atributos (2 PKs, 37 BICC)
- [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]] — 8 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hra_eval_sections|HRA_EVAL_SECTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EvalSectionPEOAddItemsConfirmCritFlag | ADD_ITEMS_CONFIRM_CRIT_FLAG | — | — |
| 2 | EvalSectionPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | EvalSectionPEOCalculationRuleCode | CALCULATION_RULE_CODE | — | — |
| 4 | EvalSectionPEOCommentText | COMMENT_TEXT | — | ✅ |
| 5 | EvalSectionPEOComments | COMMENTS | — | — |
| 6 | EvalSectionPEOContentTypeId | CONTENT_TYPE_ID | — | — |
| 7 | EvalSectionPEOCreatedBy | CREATED_BY | — | — |
| 8 | EvalSectionPEOCreationDate | CREATION_DATE | — | — |
| 9 | EvalSectionPEOEnableItems | ENABLE_ITEMS | — | — |
| 10 | EvalSectionPEOEvalSectionId | EVAL_SECTION_ID | 🔑 | ✅ |
| 11 | EvalSectionPEOEvaluationId | EVALUATION_ID | — | — |
| 12 | EvalSectionPEOFastFormulaId | FAST_FORMULA_ID | — | — |
| 13 | EvalSectionPEOFreeFormAllowedFlag | FREE_FORM_ALLOWED_FLAG | — | — |
| 14 | EvalSectionPEOItemCalculationCode | ITEM_CALCULATION_CODE | — | — |
| 15 | EvalSectionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | EvalSectionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | EvalSectionPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | EvalSectionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | EvalSectionPEOPerfRatingModelId | PERF_RATING_MODEL_ID | — | — |
| 20 | EvalSectionPEOProfileId | PROFILE_ID | — | — |
| 21 | EvalSectionPEOProfileTypeId | PROFILE_TYPE_ID | — | — |
| 22 | EvalSectionPEORateItemFlag | RATE_ITEM_FLAG | — | — |
| 23 | EvalSectionPEORateSectionFlag | RATE_SECTION_FLAG | — | — |
| 24 | EvalSectionPEORatingOverideFlag | RATING_OVERIDE_FLAG | — | — |
| 25 | EvalSectionPEORatingTypeCode | RATING_TYPE_CODE | — | — |
| 26 | EvalSectionPEOSectionMinWeight | SECTION_MIN_WEIGHT | — | — |
| 27 | EvalSectionPEOSectionMinWeightFlag | SECTION_MIN_WEIGHT_FLAG | — | — |
| 28 | EvalSectionPEOSectionRatingModelId | SECTION_RATING_MODEL_ID | — | — |
| 29 | EvalSectionPEOSectionTypeCode | SECTION_TYPE_CODE | — | — |
| 30 | EvalSectionPEOSectionWeight | SECTION_WEIGHT | — | — |
| 31 | EvalSectionPEOSectionWeightFlag | SECTION_WEIGHT_FLAG | — | — |
| 32 | EvalSectionPEOSequenceNumber | SEQUENCE_NUMBER | — | — |
| 33 | EvalSectionPEOShowCritical | SHOW_CRITICAL | — | — |
| 34 | EvalSectionPEOShowDescription | SHOW_DESCRIPTION | — | — |
| 35 | EvalSectionPEOShowDueDate | SHOW_DUE_DATE | — | — |
| 36 | EvalSectionPEOShowMandatory | SHOW_MANDATORY | — | — |
| 37 | EvalSectionPEOShowMeasurement | SHOW_MEASUREMENT | — | — |
| 38 | EvalSectionPEOShowOwnedBy | SHOW_OWNED_BY | — | — |
| 39 | EvalSectionPEOShowPercentComplete | SHOW_PERCENT_COMPLETE | — | — |
| 40 | EvalSectionPEOShowReminderDate | SHOW_REMINDER_DATE | — | — |
| 41 | EvalSectionPEOShowStatus | SHOW_STATUS | — | — |
| 42 | EvalSectionPEOShowTargetPerfRtg | SHOW_TARGET_PERF_RTG | — | — |
| 43 | EvalSectionPEOShowTargetProfLevel | SHOW_TARGET_PROF_LEVEL | — | — |
| 44 | EvalSectionPEOTmplSectionId | TMPL_SECTION_ID | — | — |
| 45 | EvalSectionPEOUseProfileFlag | USE_PROFILE_FLAG | — | — |
| 46 | EvalSectionPEOUseSecrtgForPerfrtgFlag | USE_SECRTG_FOR_PERFRTG_FLAG | — | — |
| 47 | EvalSectionPEOUseSpecContentItemFlag | USE_SPEC_CONTENT_ITEM_FLAG | — | — |
| 48 | EvalSectionPEOUseSpecProfileFlag | USE_SPEC_PROFILE_FLAG | — | — |
| 49 | EvalSectionPEOUseWorkerGoalsFlag | USE_WORKER_GOALS_FLAG | — | — |
| 50 | EvalSectionPEOWeightSectionFlag | WEIGHT_SECTION_FLAG | — | — |

### [[hra_section_defns_b|HRA_SECTION_DEFNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ASectionDefnBPEOttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 2 | SectionDefId | SECTION_DEF_ID | 🔑 | ✅ |
| 3 | SectionDefnBPEOAddItemsConfirmCritFlag | ADD_ITEMS_CONFIRM_CRIT_FLAG | — | — |
| 4 | SectionDefnBPEOAttribute1 | ATTRIBUTE1 | — | — |
| 5 | SectionDefnBPEOAttribute10 | ATTRIBUTE10 | — | — |
| 6 | SectionDefnBPEOAttribute11 | ATTRIBUTE11 | — | — |
| 7 | SectionDefnBPEOAttribute12 | ATTRIBUTE12 | — | — |
| 8 | SectionDefnBPEOAttribute13 | ATTRIBUTE13 | — | — |
| 9 | SectionDefnBPEOAttribute14 | ATTRIBUTE14 | — | — |
| 10 | SectionDefnBPEOAttribute15 | ATTRIBUTE15 | — | — |
| 11 | SectionDefnBPEOAttribute16 | ATTRIBUTE16 | — | — |
| 12 | SectionDefnBPEOAttribute17 | ATTRIBUTE17 | — | — |
| 13 | SectionDefnBPEOAttribute18 | ATTRIBUTE18 | — | — |
| 14 | SectionDefnBPEOAttribute19 | ATTRIBUTE19 | — | — |
| 15 | SectionDefnBPEOAttribute2 | ATTRIBUTE2 | — | — |
| 16 | SectionDefnBPEOAttribute20 | ATTRIBUTE20 | — | — |
| 17 | SectionDefnBPEOAttribute21 | ATTRIBUTE21 | — | — |
| 18 | SectionDefnBPEOAttribute22 | ATTRIBUTE22 | — | — |
| 19 | SectionDefnBPEOAttribute23 | ATTRIBUTE23 | — | — |
| 20 | SectionDefnBPEOAttribute24 | ATTRIBUTE24 | — | — |
| 21 | SectionDefnBPEOAttribute25 | ATTRIBUTE25 | — | — |
| 22 | SectionDefnBPEOAttribute26 | ATTRIBUTE26 | — | — |
| 23 | SectionDefnBPEOAttribute27 | ATTRIBUTE27 | — | — |
| 24 | SectionDefnBPEOAttribute28 | ATTRIBUTE28 | — | — |
| 25 | SectionDefnBPEOAttribute29 | ATTRIBUTE29 | — | — |
| 26 | SectionDefnBPEOAttribute3 | ATTRIBUTE3 | — | — |
| 27 | SectionDefnBPEOAttribute30 | ATTRIBUTE30 | — | — |
| 28 | SectionDefnBPEOAttribute4 | ATTRIBUTE4 | — | — |
| 29 | SectionDefnBPEOAttribute5 | ATTRIBUTE5 | — | — |
| 30 | SectionDefnBPEOAttribute6 | ATTRIBUTE6 | — | — |
| 31 | SectionDefnBPEOAttribute7 | ATTRIBUTE7 | — | — |
| 32 | SectionDefnBPEOAttribute8 | ATTRIBUTE8 | — | — |
| 33 | SectionDefnBPEOAttribute9 | ATTRIBUTE9 | — | — |
| 34 | SectionDefnBPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 35 | SectionDefnBPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 36 | SectionDefnBPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 37 | SectionDefnBPEOAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 38 | SectionDefnBPEOAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 39 | SectionDefnBPEOAttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 40 | SectionDefnBPEOAttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 41 | SectionDefnBPEOAttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 42 | SectionDefnBPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 43 | SectionDefnBPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 44 | SectionDefnBPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 45 | SectionDefnBPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 46 | SectionDefnBPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 47 | SectionDefnBPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 48 | SectionDefnBPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 49 | SectionDefnBPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 50 | SectionDefnBPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 51 | SectionDefnBPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 52 | SectionDefnBPEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 53 | SectionDefnBPEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 54 | SectionDefnBPEOAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 55 | SectionDefnBPEOAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 56 | SectionDefnBPEOAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 57 | SectionDefnBPEOAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 58 | SectionDefnBPEOAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 59 | SectionDefnBPEOAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 60 | SectionDefnBPEOAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 61 | SectionDefnBPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 62 | SectionDefnBPEOAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 63 | SectionDefnBPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 64 | SectionDefnBPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 65 | SectionDefnBPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 66 | SectionDefnBPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 67 | SectionDefnBPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 68 | SectionDefnBPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 69 | SectionDefnBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 70 | SectionDefnBPEOCalculationRuleCode | CALCULATION_RULE_CODE | — | — |
| 71 | SectionDefnBPEOContentProfileFlag | CONTENT_PROFILE_FLAG | — | — |
| 72 | SectionDefnBPEOContentTypeId | CONTENT_TYPE_ID | — | — |
| 73 | SectionDefnBPEOCreatedBy | CREATED_BY | — | — |
| 74 | SectionDefnBPEOCreationDate | CREATION_DATE | — | — |
| 75 | SectionDefnBPEODateFrom | DATE_FROM | — | — |
| 76 | SectionDefnBPEODateTo | DATE_TO | — | — |
| 77 | SectionDefnBPEOEnableItemsFlag | ENABLE_ITEMS_FLAG | — | — |
| 78 | SectionDefnBPEOFastFormulaId | FAST_FORMULA_ID | — | — |
| 79 | SectionDefnBPEOFreeFormAllowedFlag | FREE_FORM_ALLOWED_FLAG | — | — |
| 80 | SectionDefnBPEOItemCalculationCode | ITEM_CALCULATION_CODE | — | — |
| 81 | SectionDefnBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 82 | SectionDefnBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 83 | SectionDefnBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 84 | SectionDefnBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 85 | SectionDefnBPEOPerfRatingModelId | PERF_RATING_MODEL_ID | — | ✅ |
| 86 | SectionDefnBPEOProfileId | PROFILE_ID | — | — |
| 87 | SectionDefnBPEOProfileTypeId | PROFILE_TYPE_ID | — | — |
| 88 | SectionDefnBPEORateItemFlag | RATE_ITEM_FLAG | — | — |
| 89 | SectionDefnBPEORateSectionFlag | RATE_SECTION_FLAG | — | — |
| 90 | SectionDefnBPEORatingTypeCode | RATING_TYPE_CODE | — | — |
| 91 | SectionDefnBPEOSectionMinWeight | SECTION_MIN_WEIGHT | — | — |
| 92 | SectionDefnBPEOSectionRatingModelId | SECTION_RATING_MODEL_ID | — | ✅ |
| 93 | SectionDefnBPEOSectionTypeCode | SECTION_TYPE_CODE | — | — |
| 94 | SectionDefnBPEOSectionWeight | SECTION_WEIGHT | — | — |
| 95 | SectionDefnBPEOShowCritical | SHOW_CRITICAL | — | — |
| 96 | SectionDefnBPEOShowDescription | SHOW_DESCRIPTION | — | — |
| 97 | SectionDefnBPEOShowDueDate | SHOW_DUE_DATE | — | — |
| 98 | SectionDefnBPEOShowMandatory | SHOW_MANDATORY | — | — |
| 99 | SectionDefnBPEOShowMeasurement | SHOW_MEASUREMENT | — | — |
| 100 | SectionDefnBPEOShowOwnedBy | SHOW_OWNED_BY | — | — |
| 101 | SectionDefnBPEOShowPercentComplete | SHOW_PERCENT_COMPLETE | — | — |
| 102 | SectionDefnBPEOShowReminderDate | SHOW_REMINDER_DATE | — | — |
| 103 | SectionDefnBPEOShowSectionMinWeight | SHOW_SECTION_MIN_WEIGHT | — | — |
| 104 | SectionDefnBPEOShowSectionWeight | SHOW_SECTION_WEIGHT | — | — |
| 105 | SectionDefnBPEOShowStatus | SHOW_STATUS | — | — |
| 106 | SectionDefnBPEOShowTargetPerfRtg | SHOW_TARGET_PERF_RTG | — | — |
| 107 | SectionDefnBPEOShowTargetProfLevel | SHOW_TARGET_PROF_LEVEL | — | — |
| 108 | SectionDefnBPEOStatusCode | STATUS_CODE | — | — |
| 109 | SectionDefnBPEOUseProfileFlag | USE_PROFILE_FLAG | — | — |
| 110 | SectionDefnBPEOUseSecrtgForPerfrtgFlag | USE_SECRTG_FOR_PERFRTG_FLAG | — | — |
| 111 | SectionDefnBPEOUseSpecContentItemFlag | USE_SPEC_CONTENT_ITEM_FLAG | — | — |
| 112 | SectionDefnBPEOUseSpecProfileFlag | USE_SPEC_PROFILE_FLAG | — | — |
| 113 | SectionDefnBPEOUseWorkerGoalsFlag | USE_WORKER_GOALS_FLAG | — | — |
| 114 | SectionDefnBPEOWeightSectionFlag | WEIGHT_SECTION_FLAG | — | — |

### [[hra_section_defns_tl|HRA_SECTION_DEFNS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | SectionDefnTlPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | SectionDefnTlPEOComments | COMMENTS | — | — |
| 4 | SectionDefnTlPEOCreatedBy | CREATED_BY | — | — |
| 5 | SectionDefnTlPEOCreationDate | CREATION_DATE | — | — |
| 6 | SectionDefnTlPEODescription | DESCRIPTION | — | — |
| 7 | SectionDefnTlPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | SectionDefnTlPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | SectionDefnTlPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | SectionDefnTlPEOName | NAME | — | ✅ |
| 11 | SectionDefnTlPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | SectionDefnTlPEOSectionDefId | SECTION_DEF_ID | 🔑 | ✅ |
| 13 | SectionDefnTlPEOSourceLang | SOURCE_LANG | — | — |

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
| 10 | TemplateSectionPEOAddItemsConfirmCritFlag | ADD_ITEMS_CONFIRM_CRIT_FLAG | — | ✅ |
| 11 | TemplateSectionPEOAttribute1 | ATTRIBUTE1 | — | — |
| 12 | TemplateSectionPEOAttribute10 | ATTRIBUTE10 | — | — |
| 13 | TemplateSectionPEOAttribute11 | ATTRIBUTE11 | — | — |
| 14 | TemplateSectionPEOAttribute12 | ATTRIBUTE12 | — | — |
| 15 | TemplateSectionPEOAttribute13 | ATTRIBUTE13 | — | — |
| 16 | TemplateSectionPEOAttribute14 | ATTRIBUTE14 | — | — |
| 17 | TemplateSectionPEOAttribute15 | ATTRIBUTE15 | — | — |
| 18 | TemplateSectionPEOAttribute16 | ATTRIBUTE16 | — | — |
| 19 | TemplateSectionPEOAttribute17 | ATTRIBUTE17 | — | — |
| 20 | TemplateSectionPEOAttribute18 | ATTRIBUTE18 | — | — |
| 21 | TemplateSectionPEOAttribute19 | ATTRIBUTE19 | — | — |
| 22 | TemplateSectionPEOAttribute2 | ATTRIBUTE2 | — | — |
| 23 | TemplateSectionPEOAttribute20 | ATTRIBUTE20 | — | — |
| 24 | TemplateSectionPEOAttribute21 | ATTRIBUTE21 | — | — |
| 25 | TemplateSectionPEOAttribute22 | ATTRIBUTE22 | — | — |
| 26 | TemplateSectionPEOAttribute23 | ATTRIBUTE23 | — | — |
| 27 | TemplateSectionPEOAttribute24 | ATTRIBUTE24 | — | — |
| 28 | TemplateSectionPEOAttribute25 | ATTRIBUTE25 | — | — |
| 29 | TemplateSectionPEOAttribute26 | ATTRIBUTE26 | — | — |
| 30 | TemplateSectionPEOAttribute27 | ATTRIBUTE27 | — | — |
| 31 | TemplateSectionPEOAttribute28 | ATTRIBUTE28 | — | — |
| 32 | TemplateSectionPEOAttribute29 | ATTRIBUTE29 | — | — |
| 33 | TemplateSectionPEOAttribute3 | ATTRIBUTE3 | — | — |
| 34 | TemplateSectionPEOAttribute30 | ATTRIBUTE30 | — | — |
| 35 | TemplateSectionPEOAttribute4 | ATTRIBUTE4 | — | — |
| 36 | TemplateSectionPEOAttribute5 | ATTRIBUTE5 | — | — |
| 37 | TemplateSectionPEOAttribute6 | ATTRIBUTE6 | — | — |
| 38 | TemplateSectionPEOAttribute7 | ATTRIBUTE7 | — | — |
| 39 | TemplateSectionPEOAttribute8 | ATTRIBUTE8 | — | — |
| 40 | TemplateSectionPEOAttribute9 | ATTRIBUTE9 | — | — |
| 41 | TemplateSectionPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 42 | TemplateSectionPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 43 | TemplateSectionPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 44 | TemplateSectionPEOAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 45 | TemplateSectionPEOAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 46 | TemplateSectionPEOAttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 47 | TemplateSectionPEOAttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 48 | TemplateSectionPEOAttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 49 | TemplateSectionPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 50 | TemplateSectionPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 51 | TemplateSectionPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 52 | TemplateSectionPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 53 | TemplateSectionPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 54 | TemplateSectionPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 55 | TemplateSectionPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 56 | TemplateSectionPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 57 | TemplateSectionPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 58 | TemplateSectionPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 59 | TemplateSectionPEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 60 | TemplateSectionPEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 61 | TemplateSectionPEOAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 62 | TemplateSectionPEOAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 63 | TemplateSectionPEOAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 64 | TemplateSectionPEOAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 65 | TemplateSectionPEOAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 66 | TemplateSectionPEOAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 67 | TemplateSectionPEOAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 68 | TemplateSectionPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 69 | TemplateSectionPEOAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 70 | TemplateSectionPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 71 | TemplateSectionPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 72 | TemplateSectionPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 73 | TemplateSectionPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 74 | TemplateSectionPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 75 | TemplateSectionPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 76 | TemplateSectionPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 77 | TemplateSectionPEOCalculationRuleCode | CALCULATION_RULE_CODE | — | ✅ |
| 78 | TemplateSectionPEOContentProfileFlag | CONTENT_PROFILE_FLAG | — | ✅ |
| 79 | TemplateSectionPEOContentTypeId | CONTENT_TYPE_ID | — | — |
| 80 | TemplateSectionPEODescription | DESCRIPTION | — | ✅ |
| 81 | TemplateSectionPEOEnableItemCommentsFlag | ENABLE_ITEM_COMMENTS_FLAG | — | ✅ |
| 82 | TemplateSectionPEOEnableItemsFlag | ENABLE_ITEMS_FLAG | — | ✅ |
| 83 | TemplateSectionPEOFastFormulaId | FAST_FORMULA_ID | — | — |
| 84 | TemplateSectionPEOFreeFormAllowedFlag | FREE_FORM_ALLOWED_FLAG | — | ✅ |
| 85 | TemplateSectionPEOItemCalculationCode | ITEM_CALCULATION_CODE | — | ✅ |
| 86 | TemplateSectionPEOPerfRatingModelId | PERF_RATING_MODEL_ID | — | — |
| 87 | TemplateSectionPEOProfileId | PROFILE_ID | — | — |
| 88 | TemplateSectionPEOProfileTypeId | PROFILE_TYPE_ID | — | — |
| 89 | TemplateSectionPEORateItemFlag | RATE_ITEM_FLAG | — | ✅ |
| 90 | TemplateSectionPEORateSectionFlag | RATE_SECTION_FLAG | — | ✅ |
| 91 | TemplateSectionPEORatingTypeCode | RATING_TYPE_CODE | — | ✅ |
| 92 | TemplateSectionPEOSectionDefId | SECTION_DEF_ID | — | — |
| 93 | TemplateSectionPEOSectionMinWeight | SECTION_MIN_WEIGHT | — | ✅ |
| 94 | TemplateSectionPEOSectionRatingModelId | SECTION_RATING_MODEL_ID | — | — |
| 95 | TemplateSectionPEOSectionTypeCode | SECTION_TYPE_CODE | — | ✅ |
| 96 | TemplateSectionPEOSectionWeight | SECTION_WEIGHT | — | ✅ |
| 97 | TemplateSectionPEOSequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 98 | TemplateSectionPEOShowCritical | SHOW_CRITICAL | — | ✅ |
| 99 | TemplateSectionPEOShowDescription | SHOW_DESCRIPTION | — | ✅ |
| 100 | TemplateSectionPEOShowDueDate | SHOW_DUE_DATE | — | ✅ |
| 101 | TemplateSectionPEOShowMandatory | SHOW_MANDATORY | — | ✅ |
| 102 | TemplateSectionPEOShowMeasurement | SHOW_MEASUREMENT | — | ✅ |
| 103 | TemplateSectionPEOShowOwnedBy | SHOW_OWNED_BY | — | ✅ |
| 104 | TemplateSectionPEOShowPercentComplete | SHOW_PERCENT_COMPLETE | — | ✅ |
| 105 | TemplateSectionPEOShowReminderDate | SHOW_REMINDER_DATE | — | ✅ |
| 106 | TemplateSectionPEOShowSectionMinWeight | SHOW_SECTION_MIN_WEIGHT | — | ✅ |
| 107 | TemplateSectionPEOShowSectionWeight | SHOW_SECTION_WEIGHT | — | ✅ |
| 108 | TemplateSectionPEOShowStatus | SHOW_STATUS | — | ✅ |
| 109 | TemplateSectionPEOShowTargetPerfRtg | SHOW_TARGET_PERF_RTG | — | ✅ |
| 110 | TemplateSectionPEOShowTargetProfLevel | SHOW_TARGET_PROF_LEVEL | — | ✅ |
| 111 | TemplateSectionPEOTemplateDefnId | TEMPLATE_DEFN_ID | — | — |
| 112 | TemplateSectionPEOUseProfileFlag | USE_PROFILE_FLAG | — | ✅ |
| 113 | TemplateSectionPEOUseSecrtgForPerfrtgFlag | USE_SECRTG_FOR_PERFRTG_FLAG | — | ✅ |
| 114 | TemplateSectionPEOUseSpecContentItemFlag | USE_SPEC_CONTENT_ITEM_FLAG | — | ✅ |
| 115 | TemplateSectionPEOUseSpecProfileFlag | USE_SPEC_PROFILE_FLAG | — | ✅ |
| 116 | TemplateSectionPEOUseWorkerGoalsFlag | USE_WORKER_GOALS_FLAG | — | ✅ |
| 117 | TemplateSectionPEOWeightSectionFlag | WEIGHT_SECTION_FLAG | — | ✅ |

### [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProfileTypeSectionPEOApprovalRequiredFlag | APPROVAL_REQUIRED_FLAG | — | — |
| 2 | ProfileTypeSectionPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | ProfileTypeSectionPEOContentTypeId | CONTENT_TYPE_ID | — | — |
| 4 | ProfileTypeSectionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ProfileTypeSectionPEOName | NAME | — | ✅ |
| 6 | ProfileTypeSectionPEOProfileTypeId | PROFILE_TYPE_ID | — | — |
| 7 | ProfileTypeSectionPEOSectionId | SECTION_ID | — | — |
| 8 | ProfileTypeSectionPEOSectionItemReqdFlag | SECTION_ITEM_REQD_FLAG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
