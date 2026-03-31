---
id: DOC-OTHER-PVO-ProjectProgressPVO
doc_type: system-doc
title: "ProjectProgressPVO — PVO Cross-Module"
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
  - ProjectProgressPVO
  - projectprogresspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectProgressPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Progress. Acessa as tabelas: HR_ORGANIZATION_INFORMATION_F, PJF_PROJECTS_ALL_B, PJF_PROJ_ELEMENTS_B (+2).

**Caminho:** `FscmTopModelAM.PjoBudgetsAndForecastsAnalyticsAM.ProjectProgressPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 103 | 5 | 1 | 45 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 6 atributos
- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 6 atributos
- [[pjf_proj_elements_b|PJF_PROJ_ELEMENTS_B]] — 5 atributos (4 BICC)
- [[pjo_project_progress|PJO_PROJECT_PROGRESS]] — 84 atributos (1 PKs, 40 BICC)
- [[pjs_project_extr_status|PJS_PROJECT_EXTR_STATUS]] — 2 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOBusinessUnitId | ORGANIZATION_ID | — | — |
| 2 | BusinessUnitPEOPrimaryLedgerId | ORG_INFORMATION3 | — | — |
| 3 | OrganizationInformationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | OrganizationInformationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 5 | OrganizationInformationPEOOrgInformationContext | ORG_INFORMATION_CONTEXT | — | — |
| 6 | OrganizationInformationPEOOrgInformationId | ORG_INFORMATION_ID | — | — |

### [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectBasePEOCarryingOutOrganizationId | CARRYING_OUT_ORGANIZATION_ID | — | — |
| 2 | ProjectBasePEOOrgId | ORG_ID | — | — |
| 3 | ProjectBasePEOProjectCurrencyCode | PROJECT_CURRENCY_CODE | — | — |
| 4 | ProjectBasePEOProjectId | PROJECT_ID | — | — |
| 5 | ProjectBasePEOProjectUnitId | PROJECT_UNIT_ID | — | — |
| 6 | ProjectBasePEOProjfuncCurrencyCode | PROJFUNC_CURRENCY_CODE | — | — |

### [[pjf_proj_elements_b|PJF_PROJ_ELEMENTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskStructureBasePEOBaselineFinishDate | BASELINE_FINISH_DATE | — | ✅ |
| 2 | TaskStructureBasePEOBaselineStartDate | BASELINE_START_DATE | — | ✅ |
| 3 | TaskStructureBasePEOPlanningEndDate | PLANNING_END_DATE | — | ✅ |
| 4 | TaskStructureBasePEOPlanningStartDate | PLANNING_START_DATE | — | ✅ |
| 5 | TaskStructureBasePEOProjElementId | PROJ_ELEMENT_ID | — | — |

### [[pjo_project_progress|PJO_PROJECT_PROGRESS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | ProjectProgressPEOActualCostThruPeriodFc | ACTUAL_COST_THRU_PERIOD_FC | — | ✅ |
| 3 | ProjectProgressPEOActualCostThruPeriodPc | ACTUAL_COST_THRU_PERIOD_PC | — | ✅ |
| 4 | ProjectProgressPEOActualCostThruPeriodTc | ACTUAL_COST_THRU_PERIOD_TC | — | — |
| 5 | ProjectProgressPEOActualEffortThruPeriod | ACTUAL_EFFORT_THRU_PERIOD | — | ✅ |
| 6 | ProjectProgressPEOActualFinishDate | ACTUAL_FINISH_DATE | — | ✅ |
| 7 | ProjectProgressPEOActualQuantityThruPeriod | ACTUAL_QUANTITY_THRU_PERIOD | — | — |
| 8 | ProjectProgressPEOActualRawCostThruPeriodFc | ACTUAL_RAW_COST_THRU_PRD_FC | — | ✅ |
| 9 | ProjectProgressPEOActualRawCostThruPeriodPc | ACTUAL_RAW_COST_THRU_PRD_PC | — | ✅ |
| 10 | ProjectProgressPEOActualRawCostThruPeriodTc | ACTUAL_RAW_COST_THRU_PRD_TC | — | — |
| 11 | ProjectProgressPEOActualStartDate | ACTUAL_START_DATE | — | ✅ |
| 12 | ProjectProgressPEOActualsThruPeriod | ACTUALS_THRU_PERIOD | — | ✅ |
| 13 | ProjectProgressPEOAsOfDate | AS_OF_DATE | — | ✅ |
| 14 | ProjectProgressPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 15 | ProjectProgressPEOBaselinePlanCostFc | BASELINE_PLAN_COST_FC | — | ✅ |
| 16 | ProjectProgressPEOBaselinePlanCostPc | BASELINE_PLAN_COST_PC | — | ✅ |
| 17 | ProjectProgressPEOBaselinePlanCostTc | BASELINE_PLAN_COST_TC | — | — |
| 18 | ProjectProgressPEOBaselinePlanEffort | BASELINE_PLAN_EFFORT | — | ✅ |
| 19 | ProjectProgressPEOBaselinePlanQuantity | BASELINE_PLAN_QUANTITY | — | — |
| 20 | ProjectProgressPEOBaselinePlanRawCostFc | BASELINE_PLAN_RAW_COST_FC | — | ✅ |
| 21 | ProjectProgressPEOBaselinePlanRawCostPc | BASELINE_PLAN_RAW_COST_PC | — | ✅ |
| 22 | ProjectProgressPEOBaselinePlanRawCostTc | BASELINE_PLAN_RAW_COST_TC | — | — |
| 23 | ProjectProgressPEOCreatedBy | CREATED_BY | — | ✅ |
| 24 | ProjectProgressPEOCreationDate | CREATION_DATE | — | ✅ |
| 25 | ProjectProgressPEOCurrentFlag | CURRENT_FLAG | — | — |
| 26 | ProjectProgressPEODataFlag | DATA_FLAG | — | — |
| 27 | ProjectProgressPEOEarnedValueCostFc | EARNED_VALUE_COST_FC | — | ✅ |
| 28 | ProjectProgressPEOEarnedValueCostPc | EARNED_VALUE_COST_PC | — | ✅ |
| 29 | ProjectProgressPEOEarnedValueEffort | EARNED_VALUE_EFFORT | — | ✅ |
| 30 | ProjectProgressPEOElementVersionId | ELEMENT_VERSION_ID | — | — |
| 31 | ProjectProgressPEOEstimatedFinishDate | ESTIMATED_FINISH_DATE | — | ✅ |
| 32 | ProjectProgressPEOEstimatedStartDate | ESTIMATED_START_DATE | — | ✅ |
| 33 | ProjectProgressPEOEtcCalcMethod | ETC_CALC_METHOD | — | ✅ |
| 34 | ProjectProgressPEOEtcCostFc | ETC_COST_FC | — | ✅ |
| 35 | ProjectProgressPEOEtcCostPc | ETC_COST_PC | — | ✅ |
| 36 | ProjectProgressPEOEtcCostTc | ETC_COST_TC | — | — |
| 37 | ProjectProgressPEOEtcEffort | ETC_EFFORT | — | ✅ |
| 38 | ProjectProgressPEOEtcQuantity | ETC_QUANTITY | — | — |
| 39 | ProjectProgressPEOEtcRawCostFc | ETC_RAW_COST_FC | — | — |
| 40 | ProjectProgressPEOEtcRawCostPc | ETC_RAW_COST_PC | — | — |
| 41 | ProjectProgressPEOEtcRawCostTc | ETC_RAW_COST_TC | — | — |
| 42 | ProjectProgressPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 43 | ProjectProgressPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 44 | ProjectProgressPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 45 | ProjectProgressPEOObjectId | OBJECT_ID | — | — |
| 46 | ProjectProgressPEOObjectType | OBJECT_TYPE | — | — |
| 47 | ProjectProgressPEOOriginalPercentComplete | ORIGINAL_PERCENT_COMPLETE | — | ✅ |
| 48 | ProjectProgressPEOPercentCompCalcMethod | PERCENT_COMP_CALC_METHOD | — | ✅ |
| 49 | ProjectProgressPEOPercentComplete | PERCENT_COMPLETE | — | ✅ |
| 50 | ProjectProgressPEOPlanVersionId | PLAN_VERSION_ID | — | — |
| 51 | ProjectProgressPEOPriorProjectProgressId | PRIOR_PROJECT_PROGRESS_ID | — | — |
| 52 | ProjectProgressPEOProgressPeriod | PROGRESS_PERIOD | — | ✅ |
| 53 | ProjectProgressPEOProgressStatusCode | PROGRESS_STATUS_CODE | — | — |
| 54 | ProjectProgressPEOProgressStatusWeight | PROGRESS_STATUS_WEIGHT | — | — |
| 55 | ProjectProgressPEOProjElementId | PROJ_ELEMENT_ID | — | — |
| 56 | ProjectProgressPEOProjectId | PROJECT_ID | — | — |
| 57 | ProjectProgressPEOProjectProgressId | PROJECT_PROGRESS_ID | 🔑 | ✅ |
| 58 | ProjectProgressPEOPublishedFlag | PUBLISHED_FLAG | — | ✅ |
| 59 | ProjectProgressPEOResActCostThruPrdFc | RES_ACT_COST_THRU_PRD_FC | — | — |
| 60 | ProjectProgressPEOResActCostThruPrdPc | RES_ACT_COST_THRU_PRD_PC | — | — |
| 61 | ProjectProgressPEOResActEffThruPrd | RES_ACT_EFF_THRU_PRD | — | — |
| 62 | ProjectProgressPEOResActQtyThruPrd | RES_ACT_QTY_THRU_PRD | — | — |
| 63 | ProjectProgressPEOResActRawcostThruPrdFc | RES_ACT_RAWCOST_THRU_PRD_FC | — | — |
| 64 | ProjectProgressPEOResActRawcostThruPrdPc | RES_ACT_RAWCOST_THRU_PRD_PC | — | — |
| 65 | ProjectProgressPEOResEtcCostFc | RES_ETC_COST_FC | — | — |
| 66 | ProjectProgressPEOResEtcCostPc | RES_ETC_COST_PC | — | — |
| 67 | ProjectProgressPEOResEtcEffort | RES_ETC_EFFORT | — | — |
| 68 | ProjectProgressPEOResEtcQuantity | RES_ETC_QUANTITY | — | — |
| 69 | ProjectProgressPEOResEtcRawCostFc | RES_ETC_RAW_COST_FC | — | — |
| 70 | ProjectProgressPEOResEtcRawCostPc | RES_ETC_RAW_COST_PC | — | — |
| 71 | ProjectProgressPEORollupFlag | ROLLUP_FLAG | — | — |
| 72 | ProjectProgressPEOStructureType | STRUCTURE_TYPE | — | — |
| 73 | ProjectProgressPEOStructureVersionId | STRUCTURE_VERSION_ID | — | — |
| 74 | ProjectProgressPEOSummarizationDate | SUMMARIZATION_DATE | — | ✅ |
| 75 | ProjectProgressPEOTotalPlanCostFc | TOTAL_PLAN_COST_FC | — | ✅ |
| 76 | ProjectProgressPEOTotalPlanCostPc | TOTAL_PLAN_COST_PC | — | ✅ |
| 77 | ProjectProgressPEOTotalPlanCostTc | TOTAL_PLAN_COST_TC | — | — |
| 78 | ProjectProgressPEOTotalPlanEffort | TOTAL_PLAN_EFFORT | — | ✅ |
| 79 | ProjectProgressPEOTotalPlanQuantity | TOTAL_PLAN_QUANTITY | — | — |
| 80 | ProjectProgressPEOTotalPlanRawCostFc | TOTAL_PLAN_RAW_COST_FC | — | ✅ |
| 81 | ProjectProgressPEOTotalPlanRawCostPc | TOTAL_PLAN_RAW_COST_PC | — | ✅ |
| 82 | ProjectProgressPEOTotalPlanRawCostTc | TOTAL_PLAN_RAW_COST_TC | — | — |
| 83 | ProjectProgressPEOTransactionCurrencyCode | TRANSACTION_CURRENCY_CODE | — | — |
| 84 | ProjectProgressPEOUnitOfMeasure | UNIT_OF_MEASURE | — | — |

### [[pjs_project_extr_status|PJS_PROJECT_EXTR_STATUS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectSummarizationStatusPEOLastSumCostDate | LAST_SUM_COST_DATE | — | ✅ |
| 2 | ProjectSummarizationStatusPEOProjectId | PROJECT_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
