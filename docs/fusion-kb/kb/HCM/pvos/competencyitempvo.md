---
id: DOC-HCM-PVO-CompetencyItemPVO
doc_type: system-doc
title: "CompetencyItemPVO — PVO Human Capital Management"
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
  - CompetencyItemPVO
  - competencyitempvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CompetencyItemPVO

## 📌 Visão Geral

Extrai itens de competencia em documentos de avaliacao de performance com secoes. Suporta avaliacao de competencias em ciclos de performance review.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPerformanceDocsAM.CompetencyItemPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 160 | 4 | 8 | 34 | 21% |

---

## 🔗 Tabelas Relacionadas

- [[hra_eval_items|HRA_EVAL_ITEMS]] — 31 atributos (2 PKs, 22 BICC)
- [[hra_eval_sections|HRA_EVAL_SECTIONS]] — 46 atributos (1 PKs, 2 BICC)
- [[hrt_content_items_b|HRT_CONTENT_ITEMS_B]] — 60 atributos (2 PKs, 5 BICC)
- [[hrt_content_items_tl|HRT_CONTENT_ITEMS_TL]] — 23 atributos (3 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[hra_eval_items|HRA_EVAL_ITEMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | EvalItemId | EVAL_ITEM_ID | 🔑 | ✅ |
| 4 | EvalItemPEOAchievementDate | ACHIEVEMENT_DATE | — | ✅ |
| 5 | EvalItemPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 6 | EvalItemPEOCriticalFlag | CRITICAL_FLAG | — | ✅ |
| 7 | EvalItemPEODescription | DESCRIPTION | — | ✅ |
| 8 | EvalItemPEODueDate | DUE_DATE | — | ✅ |
| 9 | EvalItemPEOEvalSectionId | EVAL_SECTION_ID | — | — |
| 10 | EvalItemPEOEvaluationId | EVALUATION_ID | — | — |
| 11 | EvalItemPEOItemName | ITEM_NAME | — | ✅ |
| 12 | EvalItemPEOMandatoryFlag | MANDATORY_FLAG | — | ✅ |
| 13 | EvalItemPEOMeasurement | MEASUREMENT | — | ✅ |
| 14 | EvalItemPEOMinWeight | MIN_WEIGHT | — | ✅ |
| 15 | EvalItemPEOOwnedBy | OWNED_BY | — | ✅ |
| 16 | EvalItemPEOParentItemId | PARENT_ITEM_ID | — | — |
| 17 | EvalItemPEOPercentCompleted | PERCENT_COMPLETED | — | ✅ |
| 18 | EvalItemPEOPerfRatingModelId | PERF_RATING_MODEL_ID | — | ✅ |
| 19 | EvalItemPEOProfRatingModelId | PROF_RATING_MODEL_ID | — | ✅ |
| 20 | EvalItemPEORatingOverideFlag | RATING_OVERIDE_FLAG | — | ✅ |
| 21 | EvalItemPEOReminderDate | REMINDER_DATE | — | ✅ |
| 22 | EvalItemPEOStartDate | START_DATE | — | ✅ |
| 23 | EvalItemPEOTargetDate | TARGET_DATE | — | ✅ |
| 24 | EvalItemPEOTargetPerfRevRatingId | TARGET_PERF_REV_RATING_ID | — | ✅ |
| 25 | EvalItemPEOTargetProfRevRatingId | TARGET_PROF_REV_RATING_ID | — | ✅ |
| 26 | EvalItemPEOWeight | WEIGHT | — | ✅ |
| 27 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 29 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 30 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 31 | ReferenceItemId | REFERENCE_ITEM_ID | 🔑 | ✅ |

### [[hra_eval_sections|HRA_EVAL_SECTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EvalSectionId | EVAL_SECTION_ID | 🔑 | ✅ |
| 2 | EvalSectionPEOAddItemsConfirmCritFlag | ADD_ITEMS_CONFIRM_CRIT_FLAG | — | — |
| 3 | EvalSectionPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | EvalSectionPEOCalculationRuleCode | CALCULATION_RULE_CODE | — | — |
| 5 | EvalSectionPEOCommentText | COMMENT_TEXT | — | — |
| 6 | EvalSectionPEOComments | COMMENTS | — | — |
| 7 | EvalSectionPEOContentTypeId | CONTENT_TYPE_ID | — | — |
| 8 | EvalSectionPEOEnableItems | ENABLE_ITEMS | — | — |
| 9 | EvalSectionPEOEvaluationId | EVALUATION_ID | — | — |
| 10 | EvalSectionPEOFastFormulaId | FAST_FORMULA_ID | — | — |
| 11 | EvalSectionPEOFreeFormAllowedFlag | FREE_FORM_ALLOWED_FLAG | — | — |
| 12 | EvalSectionPEOItemCalculationCode | ITEM_CALCULATION_CODE | — | — |
| 13 | EvalSectionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | EvalSectionPEOPerfRatingModelId | PERF_RATING_MODEL_ID | — | — |
| 15 | EvalSectionPEOProfileId | PROFILE_ID | — | — |
| 16 | EvalSectionPEOProfileTypeId | PROFILE_TYPE_ID | — | — |
| 17 | EvalSectionPEORateItemFlag | RATE_ITEM_FLAG | — | — |
| 18 | EvalSectionPEORateSectionFlag | RATE_SECTION_FLAG | — | — |
| 19 | EvalSectionPEORatingOverideFlag | RATING_OVERIDE_FLAG | — | — |
| 20 | EvalSectionPEORatingTypeCode | RATING_TYPE_CODE | — | — |
| 21 | EvalSectionPEOSectionMinWeight | SECTION_MIN_WEIGHT | — | — |
| 22 | EvalSectionPEOSectionMinWeightFlag | SECTION_MIN_WEIGHT_FLAG | — | — |
| 23 | EvalSectionPEOSectionRatingModelId | SECTION_RATING_MODEL_ID | — | — |
| 24 | EvalSectionPEOSectionTypeCode | SECTION_TYPE_CODE | — | — |
| 25 | EvalSectionPEOSectionWeight | SECTION_WEIGHT | — | — |
| 26 | EvalSectionPEOSectionWeightFlag | SECTION_WEIGHT_FLAG | — | — |
| 27 | EvalSectionPEOSequenceNumber | SEQUENCE_NUMBER | — | — |
| 28 | EvalSectionPEOShowCritical | SHOW_CRITICAL | — | — |
| 29 | EvalSectionPEOShowDescription | SHOW_DESCRIPTION | — | — |
| 30 | EvalSectionPEOShowDueDate | SHOW_DUE_DATE | — | — |
| 31 | EvalSectionPEOShowMandatory | SHOW_MANDATORY | — | — |
| 32 | EvalSectionPEOShowMeasurement | SHOW_MEASUREMENT | — | — |
| 33 | EvalSectionPEOShowOwnedBy | SHOW_OWNED_BY | — | — |
| 34 | EvalSectionPEOShowPercentComplete | SHOW_PERCENT_COMPLETE | — | — |
| 35 | EvalSectionPEOShowReminderDate | SHOW_REMINDER_DATE | — | — |
| 36 | EvalSectionPEOShowStatus | SHOW_STATUS | — | — |
| 37 | EvalSectionPEOShowTargetPerfRtg | SHOW_TARGET_PERF_RTG | — | — |
| 38 | EvalSectionPEOShowTargetProfLevel | SHOW_TARGET_PROF_LEVEL | — | — |
| 39 | EvalSectionPEOTmplSectionId | TMPL_SECTION_ID | — | — |
| 40 | EvalSectionPEOUseProfileFlag | USE_PROFILE_FLAG | — | — |
| 41 | EvalSectionPEOUseSecrtgForPerfrtgFlag | USE_SECRTG_FOR_PERFRTG_FLAG | — | — |
| 42 | EvalSectionPEOUseSpecContentItemFlag | USE_SPEC_CONTENT_ITEM_FLAG | — | — |
| 43 | EvalSectionPEOUseSpecProfileFlag | USE_SPEC_PROFILE_FLAG | — | — |
| 44 | EvalSectionPEOUseWorkerGoalsFlag | USE_WORKER_GOALS_FLAG | — | — |
| 45 | EvalSectionPEOWeightSectionFlag | WEIGHT_SECTION_FLAG | — | — |
| 46 | ReferenceSectionId | REFERENCE_SECTION_ID | — | — |

### [[hrt_content_items_b|HRT_CONTENT_ITEMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | ContentItemBPEOContentItemCode | CONTENT_ITEM_CODE | — | — |
| 3 | ContentItemBPEOContentKeyflexId | CONTENT_KEYFLEX_ID | — | — |
| 4 | ContentItemBPEOContentSupplierCode | CONTENT_SUPPLIER_CODE | — | — |
| 5 | ContentItemBPEOContentTypeId | CONTENT_TYPE_ID | — | — |
| 6 | ContentItemBPEODateFrom | DATE_FROM | — | ✅ |
| 7 | ContentItemBPEODateTo | DATE_TO | — | ✅ |
| 8 | ContentItemBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ContentItemBPEORatingModelId | RATING_MODEL_ID | — | — |
| 10 | ContentItemId | CONTENT_ITEM_ID | 🔑 | ✅ |
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
| 1 | ContentItemTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | ContentItemTranslationPEOContentItemId | CONTENT_ITEM_ID | 🔑 | ✅ |
| 3 | ContentItemTranslationPEOItemDescription | ITEM_DESCRIPTION | — | — |
| 4 | ContentItemTranslationPEOItemDescrlong | ITEM_DESCRLONG | — | — |
| 5 | ContentItemTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ContentItemTranslationPEOName | NAME | — | ✅ |
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
| 22 | Language | LANGUAGE | 🔑 | ✅ |
| 23 | SourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
