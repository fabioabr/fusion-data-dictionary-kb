---
id: DOC-HCM-PVO-PerformanceSubTaskStatusPVO
doc_type: system-doc
title: "PerformanceSubTaskStatusPVO — PVO Human Capital Management"
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
  - PerformanceSubTaskStatusPVO
  - performancesubtaskstatuspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PerformanceSubTaskStatusPVO

## 📌 Visão Geral

Extrai o status das subtarefas do ciclo de avaliação de desempenho, com ações realizadas, datas e motivos. Permite acompanhamento granular do fluxo de aprovação de performance.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPerformanceDocsAM.PerformanceSubTaskStatusPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 89 | 4 | 4 | 13 | 15% |

---

## 🔗 Tabelas Relacionadas

- [[hra_evaluations|HRA_EVALUATIONS]] — 22 atributos
- [[hra_eval_steps|HRA_EVAL_STEPS]] — 40 atributos (2 PKs, 10 BICC)
- [[hra_tmpl_defns_b|HRA_TMPL_DEFNS_B]] — 15 atributos
- [[hra_tmpl_periods_b|HRA_TMPL_PERIODS_B]] — 12 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[hra_evaluations|HRA_EVALUATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EvaluationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | EvaluationPEOCalculationRatingsFlag | CALCULATION_RATINGS_FLAG | — | — |
| 3 | EvaluationPEODecimalPlaces | DECIMAL_PLACES | — | — |
| 4 | EvaluationPEOEndDate | END_DATE | — | — |
| 5 | EvaluationPEOEvaluationDate | EVALUATION_DATE | — | — |
| 6 | EvaluationPEOEvaluationId | EVALUATION_ID | — | — |
| 7 | EvaluationPEOLanguageCode | LANGUAGE_CODE | — | — |
| 8 | EvaluationPEOLockedByUserId | LOCKED_BY_USER_ID | — | — |
| 9 | EvaluationPEOManagerComments | MANAGER_COMMENTS | — | — |
| 10 | EvaluationPEOManagerId | MANAGER_ID | — | — |
| 11 | EvaluationPEOMappingMethodCode | MAPPING_METHOD_CODE | — | — |
| 12 | EvaluationPEOMeetingHeldDate | MEETING_HELD_DATE | — | — |
| 13 | EvaluationPEOPrevStatusCode | PREV_STATUS_CODE | — | — |
| 14 | EvaluationPEORoundingRuleCode | ROUNDING_RULE_CODE | — | — |
| 15 | EvaluationPEOSelectManagerAllowedFlag | SELECT_MANAGER_ALLOWED_FLAG | — | — |
| 16 | EvaluationPEOStarRatingEnabledFlag | STAR_RATING_ENABLED_FLAG | — | — |
| 17 | EvaluationPEOStartDate | START_DATE | — | — |
| 18 | EvaluationPEOStatusCode | STATUS_CODE | — | — |
| 19 | EvaluationPEOTemplateDefnId | TEMPLATE_DEFN_ID | — | — |
| 20 | EvaluationPEOTmplPeriodId | TMPL_PERIOD_ID | — | — |
| 21 | EvaluationPEOWorkerComments | WORKER_COMMENTS | — | — |
| 22 | EvaluationPEOWorkerId | WORKER_ID | — | — |

### [[hra_eval_steps|HRA_EVAL_STEPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionPerformedBy | ACTION_PERFORMED_BY | — | ✅ |
| 2 | ActionPerformedDate | ACTION_PERFORMED_DATE | — | ✅ |
| 3 | ActionReason | ACTION_REASON | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | — |
| 5 | CreationDate | CREATION_DATE | — | — |
| 6 | EvalStepId | EVAL_STEP_ID | 🔑 | ✅ |
| 7 | EvalStepPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 8 | EvalStepPEOCriticalAlertDays | CRITICAL_ALERT_DAYS | — | — |
| 9 | EvalStepPEODueDate | DUE_DATE | — | — |
| 10 | EvalStepPEOEvalParticipantId | EVAL_PARTICIPANT_ID | — | ✅ |
| 11 | EvalStepPEOEvaluationId | EVALUATION_ID | — | — |
| 12 | EvalStepPEOParentStepId | PARENT_STEP_ID | — | ✅ |
| 13 | EvalStepPEOSequenceNumber | SEQUENCE_NUMBER | — | — |
| 14 | EvalStepPEOStandardAlertDays | STANDARD_ALERT_DAYS | — | — |
| 15 | EvalStepPEOStepCode | STEP_CODE | — | — |
| 16 | EvalStepPEOStepCompletedBy | STEP_COMPLETED_BY | — | — |
| 17 | EvalStepPEOStepCompletionDate | STEP_COMPLETION_DATE | — | — |
| 18 | EvalStepPEOStepStatus | STEP_STATUS | — | — |
| 19 | EvalStepSubPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 20 | EvalStepSubPEOCriticalAlertDays | CRITICAL_ALERT_DAYS | — | — |
| 21 | EvalStepSubPEODueDate | DUE_DATE | — | — |
| 22 | EvalStepSubPEOEvalParticipantId | EVAL_PARTICIPANT_ID | — | — |
| 23 | EvalStepSubPEOEvalStepId | EVAL_STEP_ID | 🔑 | ✅ |
| 24 | EvalStepSubPEOEvaluationId | EVALUATION_ID | — | — |
| 25 | EvalStepSubPEOParentStepId | PARENT_STEP_ID | — | — |
| 26 | EvalStepSubPEOSequenceNumber | SEQUENCE_NUMBER | — | — |
| 27 | EvalStepSubPEOStandardAlertDays | STANDARD_ALERT_DAYS | — | — |
| 28 | EvalStepSubPEOStepCode | STEP_CODE | — | — |
| 29 | EvalStepSubPEOStepCompletedBy | STEP_COMPLETED_BY | — | — |
| 30 | EvalStepSubPEOStepCompletionDate | STEP_COMPLETION_DATE | — | — |
| 31 | EvalStepSubPEOStepStatus | STEP_STATUS | — | ✅ |
| 32 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 33 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 34 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 35 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 36 | StepSubStatus | STEP_SUB_STATUS | — | ✅ |
| 37 | StepUpdActionCode | STEP_UPD_ACTION_CODE | — | — |
| 38 | StepUpdActionPerformedBy | STEP_UPD_ACTION_PERFORMED_BY | — | — |
| 39 | StepUpdActionPerformedDate | STEP_UPD_ACTION_PERFORMED_DATE | — | — |
| 40 | StepUpdActionReason | STEP_UPD_ACTION_REASON | — | — |

### [[hra_tmpl_defns_b|HRA_TMPL_DEFNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TemplateDefnBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | TemplateDefnBPEOCalculateRatingsFlag | CALCULATE_RATINGS_FLAG | — | — |
| 3 | TemplateDefnBPEODateFrom | DATE_FROM | — | — |
| 4 | TemplateDefnBPEODateTo | DATE_TO | — | — |
| 5 | TemplateDefnBPEODecimalPlaces | DECIMAL_PLACES | — | — |
| 6 | TemplateDefnBPEODocTypeId | DOC_TYPE_ID | — | — |
| 7 | TemplateDefnBPEOMappingMethodCode | MAPPING_METHOD_CODE | — | — |
| 8 | TemplateDefnBPEOProcessFlowId | PROCESS_FLOW_ID | — | — |
| 9 | TemplateDefnBPEORoundingRuleCode | ROUNDING_RULE_CODE | — | — |
| 10 | TemplateDefnBPEOSelectMgrAllowedFlag | SELECT_MGR_ALLOWED_FLAG | — | — |
| 11 | TemplateDefnBPEOSetId | SET_ID | — | — |
| 12 | TemplateDefnBPEOShowParticipantNames | SHOW_PARTICIPANT_NAMES | — | — |
| 13 | TemplateDefnBPEOStarRatingEnabledFlag | STAR_RATING_ENABLED_FLAG | — | — |
| 14 | TemplateDefnBPEOStatusCode | STATUS_CODE | — | — |
| 15 | TemplateDefnBPEOTemplateDefnId | TEMPLATE_DEFN_ID | — | — |

### [[hra_tmpl_periods_b|HRA_TMPL_PERIODS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TemplatePeriodBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | TemplatePeriodBPEOCreatedBy | CREATED_BY | — | — |
| 3 | TemplatePeriodBPEOCreationDate | CREATION_DATE | — | — |
| 4 | TemplatePeriodBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | TemplatePeriodBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | TemplatePeriodBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | TemplatePeriodBPEONominalFromDate | NOMINAL_FROM_DATE | — | — |
| 8 | TemplatePeriodBPEONominalToDate | NOMINAL_TO_DATE | — | — |
| 9 | TemplatePeriodBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | TemplatePeriodBPEOReviewPeriodId | REVIEW_PERIOD_ID | — | — |
| 11 | TemplatePeriodBPEOTemplateDefnId | TEMPLATE_DEFN_ID | — | — |
| 12 | TemplatePeriodBPEOTmplPeriodId | TMPL_PERIOD_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
