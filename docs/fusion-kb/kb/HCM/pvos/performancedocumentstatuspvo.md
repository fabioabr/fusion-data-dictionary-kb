---
id: DOC-HCM-PVO-PerformanceDocumentStatusPVO
doc_type: system-doc
title: "PerformanceDocumentStatusPVO — PVO Human Capital Management"
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
  - PerformanceDocumentStatusPVO
  - performancedocumentstatuspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PerformanceDocumentStatusPVO

## 📌 Visão Geral

Disponibiliza o status de documentos de avaliação de desempenho com template e período associados. Permite acompanhamento do progresso (rascunho, em revisão, finalizado) das avaliações.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPerformanceDocsAM.PerformanceDocumentStatusPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 56 | 3 | 5 | 25 | 45% |

---

## 🔗 Tabelas Relacionadas

- [[hra_evaluations|HRA_EVALUATIONS]] — 28 atributos (1 PKs, 19 BICC)
- [[hra_tmpl_defns_b|HRA_TMPL_DEFNS_B]] — 16 atributos (2 PKs, 3 BICC)
- [[hra_tmpl_periods_b|HRA_TMPL_PERIODS_B]] — 12 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[hra_evaluations|HRA_EVALUATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | EvaluationId | EVALUATION_ID | 🔑 | ✅ |
| 4 | EvaluationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 5 | EvaluationPEOCalculationRatingsFlag | CALCULATION_RATINGS_FLAG | — | ✅ |
| 6 | EvaluationPEODecimalPlaces | DECIMAL_PLACES | — | — |
| 7 | EvaluationPEOEndDate | END_DATE | — | ✅ |
| 8 | EvaluationPEOEvaluationDate | EVALUATION_DATE | — | ✅ |
| 9 | EvaluationPEOLanguageCode | LANGUAGE_CODE | — | — |
| 10 | EvaluationPEOLockedByUserId | LOCKED_BY_USER_ID | — | — |
| 11 | EvaluationPEOManagerComments | MANAGER_COMMENTS | — | ✅ |
| 12 | EvaluationPEOManagerId | MANAGER_ID | — | ✅ |
| 13 | EvaluationPEOMappingMethodCode | MAPPING_METHOD_CODE | — | ✅ |
| 14 | EvaluationPEOMeetingHeldDate | MEETING_HELD_DATE | — | ✅ |
| 15 | EvaluationPEOPrevStatusCode | PREV_STATUS_CODE | — | ✅ |
| 16 | EvaluationPEORoundingRuleCode | ROUNDING_RULE_CODE | — | ✅ |
| 17 | EvaluationPEOSelectManagerAllowedFlag | SELECT_MANAGER_ALLOWED_FLAG | — | ✅ |
| 18 | EvaluationPEOStarRatingEnabledFlag | STAR_RATING_ENABLED_FLAG | — | ✅ |
| 19 | EvaluationPEOStartDate | START_DATE | — | ✅ |
| 20 | EvaluationPEOStatusCode | STATUS_CODE | — | ✅ |
| 21 | EvaluationPEOTemplateDefnId | TEMPLATE_DEFN_ID | — | — |
| 22 | EvaluationPEOTmplPeriodId | TMPL_PERIOD_ID | — | — |
| 23 | EvaluationPEOWorkerComments | WORKER_COMMENTS | — | ✅ |
| 24 | EvaluationPEOWorkerId | WORKER_ID | — | — |
| 25 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 27 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 28 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[hra_tmpl_defns_b|HRA_TMPL_DEFNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TemplateDefnBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | TemplateDefnBPEOCalculateRatingsFlag | CALCULATE_RATINGS_FLAG | — | — |
| 3 | TemplateDefnBPEODateFrom | DATE_FROM | — | — |
| 4 | TemplateDefnBPEODateTo | DATE_TO | — | — |
| 5 | TemplateDefnBPEODecimalPlaces | DECIMAL_PLACES | — | — |
| 6 | TemplateDefnBPEODocTypeId | DOC_TYPE_ID | — | — |
| 7 | TemplateDefnBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | TemplateDefnBPEOMappingMethodCode | MAPPING_METHOD_CODE | — | — |
| 9 | TemplateDefnBPEOProcessFlowId | PROCESS_FLOW_ID | — | — |
| 10 | TemplateDefnBPEORoundingRuleCode | ROUNDING_RULE_CODE | — | — |
| 11 | TemplateDefnBPEOSelectMgrAllowedFlag | SELECT_MGR_ALLOWED_FLAG | — | — |
| 12 | TemplateDefnBPEOSetId | SET_ID | — | — |
| 13 | TemplateDefnBPEOShowParticipantNames | SHOW_PARTICIPANT_NAMES | — | — |
| 14 | TemplateDefnBPEOStarRatingEnabledFlag | STAR_RATING_ENABLED_FLAG | — | — |
| 15 | TemplateDefnBPEOStatusCode | STATUS_CODE | — | — |
| 16 | TemplateDefnBPEOTemplateDefnId | TEMPLATE_DEFN_ID | 🔑 | ✅ |

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
