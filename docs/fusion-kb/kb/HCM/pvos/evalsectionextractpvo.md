---
id: DOC-HCM-PVO-EvalSectionExtractPVO
doc_type: system-doc
title: "EvalSectionExtractPVO — PVO Human Capital Management"
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
  - EvalSectionExtractPVO
  - evalsectionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EvalSectionExtractPVO

## 📌 Visão Geral

Extrai seções de avaliação de desempenho com regras de cálculo e configurações. Suporta estruturação de templates de performance review.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.PerformanceBiccExtractAM.EvalSectionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 51 | 1 | 1 | 51 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hra_eval_sections|HRA_EVAL_SECTIONS]] — 51 atributos (1 PKs, 51 BICC)

---

## ⚙️ Atributos

### [[hra_eval_sections|HRA_EVAL_SECTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddItemsConfirmCritFlag | ADD_ITEMS_CONFIRM_CRIT_FLAG | — | ✅ |
| 2 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 3 | CalculationRuleCode | CALCULATION_RULE_CODE | — | ✅ |
| 4 | CommentText | COMMENT_TEXT | — | ✅ |
| 5 | Comments | COMMENTS | — | ✅ |
| 6 | ContentTypeId | CONTENT_TYPE_ID | — | ✅ |
| 7 | CreatedBy | CREATED_BY | — | ✅ |
| 8 | CreationDate | CREATION_DATE | — | ✅ |
| 9 | EnableItems | ENABLE_ITEMS | — | ✅ |
| 10 | EvalSectionId | EVAL_SECTION_ID | 🔑 | ✅ |
| 11 | EvaluationId | EVALUATION_ID | — | ✅ |
| 12 | FastFormulaId | FAST_FORMULA_ID | — | ✅ |
| 13 | FreeFormAllowedFlag | FREE_FORM_ALLOWED_FLAG | — | ✅ |
| 14 | ItemCalculationCode | ITEM_CALCULATION_CODE | — | ✅ |
| 15 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 19 | PerfRatingModelId | PERF_RATING_MODEL_ID | — | ✅ |
| 20 | ProfileId | PROFILE_ID | — | ✅ |
| 21 | ProfileTypeId | PROFILE_TYPE_ID | — | ✅ |
| 22 | RateItemFlag | RATE_ITEM_FLAG | — | ✅ |
| 23 | RateSectionFlag | RATE_SECTION_FLAG | — | ✅ |
| 24 | RatingOverideFlag | RATING_OVERIDE_FLAG | — | ✅ |
| 25 | RatingTypeCode | RATING_TYPE_CODE | — | ✅ |
| 26 | ReferenceSectionId | REFERENCE_SECTION_ID | — | ✅ |
| 27 | SectionMinWeight | SECTION_MIN_WEIGHT | — | ✅ |
| 28 | SectionMinWeightFlag | SECTION_MIN_WEIGHT_FLAG | — | ✅ |
| 29 | SectionRatingModelId | SECTION_RATING_MODEL_ID | — | ✅ |
| 30 | SectionTypeCode | SECTION_TYPE_CODE | — | ✅ |
| 31 | SectionWeight | SECTION_WEIGHT | — | ✅ |
| 32 | SectionWeightFlag | SECTION_WEIGHT_FLAG | — | ✅ |
| 33 | SequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 34 | ShowCritical | SHOW_CRITICAL | — | ✅ |
| 35 | ShowDescription | SHOW_DESCRIPTION | — | ✅ |
| 36 | ShowDueDate | SHOW_DUE_DATE | — | ✅ |
| 37 | ShowMandatory | SHOW_MANDATORY | — | ✅ |
| 38 | ShowMeasurement | SHOW_MEASUREMENT | — | ✅ |
| 39 | ShowOwnedBy | SHOW_OWNED_BY | — | ✅ |
| 40 | ShowPercentComplete | SHOW_PERCENT_COMPLETE | — | ✅ |
| 41 | ShowReminderDate | SHOW_REMINDER_DATE | — | ✅ |
| 42 | ShowStatus | SHOW_STATUS | — | ✅ |
| 43 | ShowTargetPerfRtg | SHOW_TARGET_PERF_RTG | — | ✅ |
| 44 | ShowTargetProfLevel | SHOW_TARGET_PROF_LEVEL | — | ✅ |
| 45 | TmplSectionId | TMPL_SECTION_ID | — | ✅ |
| 46 | UseProfileFlag | USE_PROFILE_FLAG | — | ✅ |
| 47 | UseSecrtgForPerfrtgFlag | USE_SECRTG_FOR_PERFRTG_FLAG | — | ✅ |
| 48 | UseSpecContentItemFlag | USE_SPEC_CONTENT_ITEM_FLAG | — | ✅ |
| 49 | UseSpecProfileFlag | USE_SPEC_PROFILE_FLAG | — | ✅ |
| 50 | UseWorkerGoalsFlag | USE_WORKER_GOALS_FLAG | — | ✅ |
| 51 | WeightSectionFlag | WEIGHT_SECTION_FLAG | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
