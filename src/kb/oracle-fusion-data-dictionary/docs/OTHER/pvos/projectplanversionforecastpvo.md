---
id: DOC-OTHER-PVO-ProjectPlanVersionForecastPVO
doc_type: system-doc
title: "ProjectPlanVersionForecastPVO — PVO Cross-Module"
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
  - ProjectPlanVersionForecastPVO
  - projectplanversionforecastpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectPlanVersionForecastPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Plan Version Forecast. Acessa as tabelas: GL_DAILY_CONVERSION_TYPES, PER_PERSONS, PER_PERSON_NAMES_F_V (+14).

**Caminho:** `FscmTopModelAM.PjoBudgetsAndForecastsAnalyticsAM.ProjectPlanVersionForecastPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 266 | 17 | 1 | 61 | 23% |

---

## 🔗 Tabelas Relacionadas

- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 12 atributos
- [[per_persons|PER_PERSONS]] — 8 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 20 atributos (6 BICC)
- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 8 atributos (1 BICC)
- [[pjf_projects_all_tl|PJF_PROJECTS_ALL_TL]] — 3 atributos (1 BICC)
- [[pjf_rate_schedules_vl|PJF_RATE_SCHEDULES_VL]] — 18 atributos (9 BICC)
- [[pjf_rbs_versions_vl|PJF_RBS_VERSIONS_VL]] — 3 atributos (1 BICC)
- [[pjo_fin_plan_amt_sets|PJO_FIN_PLAN_AMT_SETS]] — 10 atributos
- [[pjo_lookups|PJO_LOOKUPS]] — 3 atributos (1 BICC)
- [[pjo_period_profiles_vl|PJO_PERIOD_PROFILES_VL]] — 2 atributos
- [[pjo_planning_options|PJO_PLANNING_OPTIONS]] — 91 atributos (14 BICC)
- [[pjo_plan_types_b|PJO_PLAN_TYPES_B]] — 22 atributos (3 BICC)
- [[pjo_plan_types_tl|PJO_PLAN_TYPES_TL]] — 4 atributos (2 BICC)
- [[pjo_plan_types_vl|PJO_PLAN_TYPES_VL]] — 4 atributos
- [[pjo_plan_versions_b|PJO_PLAN_VERSIONS_B]] — 48 atributos (1 PKs, 21 BICC)
- [[pjo_plan_versions_tl|PJO_PLAN_VERSIONS_TL]] — 4 atributos (2 BICC)
- [[pjo_plan_versions_vl|PJO_PLAN_VERSIONS_VL]] — 6 atributos

---

## ⚙️ Atributos

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PcCostRateTypeForPlanOptnConversionType | CONVERSION_TYPE | — | — |
| 2 | PcCostRateTypeForPlanOptnDescription | DESCRIPTION | — | — |
| 3 | PcCostRateTypeForPlanOptnUserConversionType | USER_CONVERSION_TYPE | — | — |
| 4 | PcRevRateTypeForPlanOptnConversionType | CONVERSION_TYPE | — | — |
| 5 | PcRevRateTypeForPlanOptnDescription | DESCRIPTION | — | — |
| 6 | PcRevRateTypeForPlanOptnUserConversionType | USER_CONVERSION_TYPE | — | — |
| 7 | PfcCostRateTypeForPlanOptnConversionType | CONVERSION_TYPE | — | — |
| 8 | PfcCostRateTypeForPlanOptnDescription | DESCRIPTION | — | — |
| 9 | PfcCostRateTypeForPlanOptnUserConversionType | USER_CONVERSION_TYPE | — | — |
| 10 | PfcRevRateTypeForPlanOptnConversionType | CONVERSION_TYPE | — | — |
| 11 | PfcRevRateTypeForPlanOptnDescription | DESCRIPTION | — | — |
| 12 | PfcRevRateTypeForPlanOptnUserConversionType | USER_CONVERSION_TYPE | — | — |

### [[per_persons|PER_PERSONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BaselineIdForPlanVersionPersonId | PERSON_ID | — | — |
| 2 | BaselineIdForPlanVersionUserGuid | USER_GUID | — | — |
| 3 | LockedIdForPlanVersionPersonId | PERSON_ID | — | — |
| 4 | LockedIdForPlanVersionUserGuid | USER_GUID | — | — |
| 5 | RejectedIdForPlanVersionPersonId | PERSON_ID | — | — |
| 6 | RejectedIdForPlanVersionUserGuid | USER_GUID | — | — |
| 7 | SubmittedIdForPlanVersionPersonId | PERSON_ID | — | — |
| 8 | SubmittedIdForPlanVersionUserGuid | USER_GUID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNameForBaselinedIdEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonNameForBaselinedIdEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonNameForBaselinedIdFullName | FULL_NAME | — | ✅ |
| 4 | PersonNameForBaselinedIdPersonId | PERSON_ID | — | — |
| 5 | PersonNameForBaselinedIdPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonNameForLockedIdEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | PersonNameForLockedIdEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 8 | PersonNameForLockedIdFullName | FULL_NAME | — | ✅ |
| 9 | PersonNameForLockedIdPersonId | PERSON_ID | — | — |
| 10 | PersonNameForLockedIdPersonNameId | PERSON_NAME_ID | — | — |
| 11 | PersonNameForRejectedIdEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 12 | PersonNameForRejectedIdEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 13 | PersonNameForRejectedIdFullName | FULL_NAME | — | — |
| 14 | PersonNameForRejectedIdPersonId | PERSON_ID | — | — |
| 15 | PersonNameForRejectedIdPersonNameId | PERSON_NAME_ID | — | — |
| 16 | PersonNameForSubmittedIdEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 17 | PersonNameForSubmittedIdEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 18 | PersonNameForSubmittedIdFullName | FULL_NAME | — | — |
| 19 | PersonNameForSubmittedIdPersonId | PERSON_ID | — | — |
| 20 | PersonNameForSubmittedIdPersonNameId | PERSON_NAME_ID | — | — |

### [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectBasePEOCarryingOutOrganizationId | CARRYING_OUT_ORGANIZATION_ID | — | — |
| 2 | ProjectBasePEOOrgId | ORG_ID | — | — |
| 3 | ProjectBasePEOProjectCategory | PROJECT_CATEGORY | — | — |
| 4 | ProjectBasePEOProjectCurrencyCode | PROJECT_CURRENCY_CODE | — | — |
| 5 | ProjectBasePEOProjectId | PROJECT_ID | — | — |
| 6 | ProjectBasePEOProjectUnitId | PROJECT_UNIT_ID | — | — |
| 7 | ProjectBasePEOProjfuncCurrencyCode | PROJFUNC_CURRENCY_CODE | — | — |
| 8 | ProjectBasePEOSegment1 | SEGMENT1 | — | ✅ |

### [[pjf_projects_all_tl|PJF_PROJECTS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectTranslationPEOLanguage | LANGUAGE | — | — |
| 2 | ProjectTranslationPEOName | NAME | — | ✅ |
| 3 | ProjectTranslationPEOProjectId | PROJECT_ID | — | — |

### [[pjf_rate_schedules_vl|PJF_RATE_SCHEDULES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostBrdnRateSchForPlanOptionRateScheduleId | RATE_SCHEDULE_ID | — | — |
| 2 | CostBrdnRateSchForPlanOptionRateScheduleName | RATE_SCHEDULE_NAME | — | ✅ |
| 3 | CostEmpRateSchForPlanOptionRateScheduleId | RATE_SCHEDULE_ID | — | — |
| 4 | CostEmpRateSchForPlanOptionRateScheduleName | RATE_SCHEDULE_NAME | — | ✅ |
| 5 | CostJobRateSchForPlanOptionRateScheduleId | RATE_SCHEDULE_ID | — | — |
| 6 | CostJobRateSchForPlanOptionRateScheduleName | RATE_SCHEDULE_NAME | — | ✅ |
| 7 | CostNonLbrRateSchForPlanOptnRateScheduleId | RATE_SCHEDULE_ID | — | — |
| 8 | CostNonLbrRateSchForPlanOptnRateScheduleName | RATE_SCHEDULE_NAME | — | ✅ |
| 9 | ResClsBillRateSchForPlanOptnRateScheduleId | RATE_SCHEDULE_ID | — | — |
| 10 | ResClsBillRateSchForPlanOptnRateScheduleName | RATE_SCHEDULE_NAME | — | ✅ |
| 11 | ResClsRawCostSchForPlanOptnRateScheduleId | RATE_SCHEDULE_ID | — | — |
| 12 | ResClsRawCostSchForPlanOptnRateScheduleName | RATE_SCHEDULE_NAME | — | ✅ |
| 13 | RevEmpRateSchForPlanOptionRateScheduleId | RATE_SCHEDULE_ID | — | — |
| 14 | RevEmpRateSchForPlanOptionRateScheduleName | RATE_SCHEDULE_NAME | — | ✅ |
| 15 | RevJobRateSchForPlanOptionRateScheduleId | RATE_SCHEDULE_ID | — | — |
| 16 | RevJobRateSchForPlanOptionRateScheduleName | RATE_SCHEDULE_NAME | — | ✅ |
| 17 | RevNonLbrRateSchForPlanOptnRateScheduleId | RATE_SCHEDULE_ID | — | — |
| 18 | RevNonLbrRateSchForPlanOptnRateScheduleName | RATE_SCHEDULE_NAME | — | ✅ |

### [[pjf_rbs_versions_vl|PJF_RBS_VERSIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RbsVersionForPlanOptionDescription | DESCRIPTION | — | — |
| 2 | RbsVersionForPlanOptionName | NAME | — | ✅ |
| 3 | RbsVersionForPlanOptionRbsVersionId | RBS_VERSION_ID | — | — |

### [[pjo_fin_plan_amt_sets|PJO_FIN_PLAN_AMT_SETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AmountSetForPlanOptionAllQtyFlag | ALL_QTY_FLAG | — | — |
| 2 | AmountSetForPlanOptionBillRateFlag | BILL_RATE_FLAG | — | — |
| 3 | AmountSetForPlanOptionBrdndCostFlag | BRDND_COST_FLAG | — | — |
| 4 | AmountSetForPlanOptionBrdndRateFlag | BRDND_RATE_FLAG | — | — |
| 5 | AmountSetForPlanOptionCostQtyFlag | COST_QTY_FLAG | — | — |
| 6 | AmountSetForPlanOptionCostRateFlag | COST_RATE_FLAG | — | — |
| 7 | AmountSetForPlanOptionFinPlanAmtSetId | FIN_PLAN_AMT_SET_ID | — | — |
| 8 | AmountSetForPlanOptionRawCostFlag | RAW_COST_FLAG | — | — |
| 9 | AmountSetForPlanOptionRevenueFlag | REVENUE_FLAG | — | — |
| 10 | AmountSetForPlanOptionRevenueQtyFlag | REVENUE_QTY_FLAG | — | — |

### [[pjo_lookups|PJO_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LookupCode | LOOKUP_CODE | — | — |
| 2 | LookupType | LOOKUP_TYPE | — | — |
| 3 | PjoLookupPEOMeaning | MEANING | — | ✅ |

### [[pjo_period_profiles_vl|PJO_PERIOD_PROFILES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PeriodProfileForPlanOptionName | NAME | — | — |
| 2 | PeriodProfileForPlanOptionPeriodProfileId | PERIOD_PROFILE_ID | — | — |

### [[pjo_planning_options|PJO_PLANNING_OPTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlanningOptionPEOAllowFcstAmtCarryFlag | ALLOW_FCST_AMT_CARRY_FLAG | — | — |
| 2 | PlanningOptionPEOAllowNegEtcFlag | ALLOW_NEG_ETC_FLAG | — | — |
| 3 | PlanningOptionPEOAmountSetId | AMOUNT_SET_ID | — | — |
| 4 | PlanningOptionPEOAmountType | AMOUNT_TYPE | — | — |
| 5 | PlanningOptionPEOApprovedCostPlanTypeFlag | APPROVED_COST_PLAN_TYPE_FLAG | — | ✅ |
| 6 | PlanningOptionPEOApprovedRevPlanTypeFlag | APPROVED_REV_PLAN_TYPE_FLAG | — | ✅ |
| 7 | PlanningOptionPEOAutoApproveFlag | AUTO_APPROVE_FLAG | — | — |
| 8 | PlanningOptionPEOAutoBdgtBaseline | AUTO_BDGT_BASELINE | — | — |
| 9 | PlanningOptionPEOAutoRollupTaskDate | AUTO_ROLLUP_TASK_DATE | — | — |
| 10 | PlanningOptionPEOBudgetCreationMethod | BUDGET_CREATION_METHOD | — | ✅ |
| 11 | PlanningOptionPEOCommitmentControlFlag | COMMITMENT_CONTROL_FLAG | — | — |
| 12 | PlanningOptionPEOCopySrcPlanTypeId | COPY_SRC_PLAN_TYPE_ID | — | — |
| 13 | PlanningOptionPEOCopySrcPlanVersionId | COPY_SRC_PLAN_VERSION_ID | — | — |
| 14 | PlanningOptionPEOCostBrdndRateSchId | COST_BRDND_RATE_SCH_ID | — | — |
| 15 | PlanningOptionPEOCostEmpRateSchId | COST_EMP_RATE_SCH_ID | — | — |
| 16 | PlanningOptionPEOCostJobRateSchId | COST_JOB_RATE_SCH_ID | — | — |
| 17 | PlanningOptionPEOCostNonLbrResRateSchId | COST_NON_LBR_RES_RATE_SCH_ID | — | — |
| 18 | PlanningOptionPEOCreatedBy | CREATED_BY | — | — |
| 19 | PlanningOptionPEOCreationDate | CREATION_DATE | — | — |
| 20 | PlanningOptionPEOCumulativeBudgetOption | CUMULATIVE_BUDGET_OPTION | — | — |
| 21 | PlanningOptionPEOCurrencyType | CURRENCY_TYPE | — | — |
| 22 | PlanningOptionPEOCurrentPlanningPeriod | CURRENT_PLANNING_PERIOD | — | ✅ |
| 23 | PlanningOptionPEOEnableCostsForProjPlan | ENABLE_COSTS_FOR_PROJ_PLAN | — | — |
| 24 | PlanningOptionPEOEtcMethodCode | ETC_METHOD_CODE | — | — |
| 25 | PlanningOptionPEOEtcMethodFlag | ETC_METHOD_FLAG | — | — |
| 26 | PlanningOptionPEOFactorByCode | FACTOR_BY_CODE | — | — |
| 27 | PlanningOptionPEOForecastPeriodName | FORECAST_PERIOD_NAME | — | — |
| 28 | PlanningOptionPEOGenActAmtsThruCode | GEN_ACT_AMTS_THRU_CODE | — | — |
| 29 | PlanningOptionPEOGenBdgtDuringBaseline | GEN_BDGT_DURING_BASELINE | — | — |
| 30 | PlanningOptionPEOGenInclBillEventFlag | GEN_INCL_BILL_EVENT_FLAG | — | — |
| 31 | PlanningOptionPEOGenInclOpencommFlag | GEN_INCL_OPENCOMM_FLAG | — | — |
| 32 | PlanningOptionPEOGenRetManLineFlag | GEN_RET_MAN_LINE_FLAG | — | — |
| 33 | PlanningOptionPEOGenSrcCode | GEN_SRC_CODE | — | — |
| 34 | PlanningOptionPEOGenSrcPlanTypeId | GEN_SRC_PLAN_TYPE_ID | — | — |
| 35 | PlanningOptionPEOGenSrcPlanVerCode | GEN_SRC_PLAN_VER_CODE | — | — |
| 36 | PlanningOptionPEOGenSrcPlanVersionId | GEN_SRC_PLAN_VERSION_ID | — | — |
| 37 | PlanningOptionPEOIntegrationType | INTEGRATION_TYPE | — | — |
| 38 | PlanningOptionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 39 | PlanningOptionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 40 | PlanningOptionPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 41 | PlanningOptionPEOMarginDerivedFromCode | MARGIN_DERIVED_FROM_CODE | — | ✅ |
| 42 | PlanningOptionPEONtpRateDate | NTP_RATE_DATE | — | — |
| 43 | PlanningOptionPEONtpRateDateType | NTP_RATE_DATE_TYPE | — | — |
| 44 | PlanningOptionPEOObjectId1 | OBJECT_ID1 | — | — |
| 45 | PlanningOptionPEOObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 46 | PlanningOptionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 47 | PlanningOptionPEOPcCostRateDate | PC_COST_RATE_DATE | — | — |
| 48 | PlanningOptionPEOPcCostRateDateType | PC_COST_RATE_DATE_TYPE | — | — |
| 49 | PlanningOptionPEOPcCostRateType | PC_COST_RATE_TYPE | — | — |
| 50 | PlanningOptionPEOPcRevRateDate | PC_REV_RATE_DATE | — | — |
| 51 | PlanningOptionPEOPcRevRateDateType | PC_REV_RATE_DATE_TYPE | — | — |
| 52 | PlanningOptionPEOPcRevRateType | PC_REV_RATE_TYPE | — | — |
| 53 | PlanningOptionPEOPercentCompCalcMethod | PERCENT_COMP_CALC_METHOD | — | — |
| 54 | PlanningOptionPEOPercentCompRollupMethod | PERCENT_COMP_ROLLUP_METHOD | — | — |
| 55 | PlanningOptionPEOPeriodProfileId | PERIOD_PROFILE_ID | — | — |
| 56 | PlanningOptionPEOPfcCostRateDate | PFC_COST_RATE_DATE | — | — |
| 57 | PlanningOptionPEOPfcCostRateDateType | PFC_COST_RATE_DATE_TYPE | — | — |
| 58 | PlanningOptionPEOPfcCostRateType | PFC_COST_RATE_TYPE | — | — |
| 59 | PlanningOptionPEOPfcRevRateDate | PFC_REV_RATE_DATE | — | — |
| 60 | PlanningOptionPEOPfcRevRateDateType | PFC_REV_RATE_DATE_TYPE | — | — |
| 61 | PlanningOptionPEOPfcRevRateType | PFC_REV_RATE_TYPE | — | — |
| 62 | PlanningOptionPEOPlanInMultiCurrFlag | PLAN_IN_MULTI_CURR_FLAG | — | ✅ |
| 63 | PlanningOptionPEOPlanLevelCode | PLAN_LEVEL_CODE | — | ✅ |
| 64 | PlanningOptionPEOPlanOptionLevelCode | PLAN_OPTION_LEVEL_CODE | — | — |
| 65 | PlanningOptionPEOPlanTypeCode | PLAN_TYPE_CODE | — | — |
| 66 | PlanningOptionPEOPlanTypeId | PLAN_TYPE_ID | — | — |
| 67 | PlanningOptionPEOPlanVersionId | PLAN_VERSION_ID | — | — |
| 68 | PlanningOptionPEOPlannedForCode | PLANNED_FOR_CODE | — | ✅ |
| 69 | PlanningOptionPEOPlanningOptionId | PLANNING_OPTION_ID | — | — |
| 70 | PlanningOptionPEOPrimaryCostForecastFlag | PRIMARY_COST_FORECAST_FLAG | — | ✅ |
| 71 | PlanningOptionPEOPrimaryRevForecastFlag | PRIMARY_REV_FORECAST_FLAG | — | ✅ |
| 72 | PlanningOptionPEOProjectId | PROJECT_ID | — | — |
| 73 | PlanningOptionPEORaPlanTypeId | RA_PLAN_TYPE_ID | — | — |
| 74 | PlanningOptionPEORaTaskDatesSame | RA_TASK_DATES_SAME | — | — |
| 75 | PlanningOptionPEORbsVersionId | RBS_VERSION_ID | — | — |
| 76 | PlanningOptionPEOResClassBillRateSchId | RES_CLASS_BILL_RATE_SCH_ID | — | — |
| 77 | PlanningOptionPEOResClassRawCostSchId | RES_CLASS_RAW_COST_SCH_ID | — | — |
| 78 | PlanningOptionPEORetainSourceSpreadFlag | RETAIN_SOURCE_SPREAD_FLAG | — | — |
| 79 | PlanningOptionPEORevClassificationMethod | REV_CLASSIFICATION_METHOD | — | ✅ |
| 80 | PlanningOptionPEORevEmpRateSchId | REV_EMP_RATE_SCH_ID | — | — |
| 81 | PlanningOptionPEORevJobRateSchId | REV_JOB_RATE_SCH_ID | — | — |
| 82 | PlanningOptionPEORevNonLbrResRateSchId | REV_NON_LBR_RES_RATE_SCH_ID | — | — |
| 83 | PlanningOptionPEOSpecPcCostAtProjLevel | SPEC_PC_COST_AT_PROJ_LEVEL | — | — |
| 84 | PlanningOptionPEOSpecPcRevAtProjLevel | SPEC_PC_REV_AT_PROJ_LEVEL | — | — |
| 85 | PlanningOptionPEOSpecPfcCostAtProjLevel | SPEC_PFC_COST_AT_PROJ_LEVEL | — | — |
| 86 | PlanningOptionPEOSpecPfcRevAtProjLevel | SPEC_PFC_REV_AT_PROJ_LEVEL | — | — |
| 87 | PlanningOptionPEOSyncTaskTxnPlanDates | SYNC_TASK_TXN_PLAN_DATES | — | — |
| 88 | PlanningOptionPEOSyncTxnDateBuffer | SYNC_TXN_DATE_BUFFER | — | — |
| 89 | PlanningOptionPEOTimePhasedCode | TIME_PHASED_CODE | — | ✅ |
| 90 | PlanningOptionPEOUsePlanningRatesFlag | USE_PLANNING_RATES_FLAG | — | ✅ |
| 91 | PlanningOptionPEOUseThirdPartySoftware | USE_THIRD_PARTY_SOFTWARE | — | — |

### [[pjo_plan_types_b|PJO_PLAN_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlanTypeBasePEOApprovedCostPlanTypeFlag | APPROVED_COST_PLAN_TYPE_FLAG | — | — |
| 2 | PlanTypeBasePEOApprovedRevPlanTypeFlag | APPROVED_REV_PLAN_TYPE_FLAG | — | — |
| 3 | PlanTypeBasePEOAutoApproveFlag | AUTO_APPROVE_FLAG | — | — |
| 4 | PlanTypeBasePEOAutoSubmitForAppr | AUTO_SUBMIT_FOR_APPR | — | — |
| 5 | PlanTypeBasePEOCreatedBy | CREATED_BY | — | — |
| 6 | PlanTypeBasePEOCreationDate | CREATION_DATE | — | — |
| 7 | PlanTypeBasePEODefaultFinPlanTypeFlag | DEFAULT_FIN_PLAN_TYPE_FLAG | — | — |
| 8 | PlanTypeBasePEOEnableWfFlag | ENABLE_WF_FLAG | — | — |
| 9 | PlanTypeBasePEOEndDate | END_DATE | — | ✅ |
| 10 | PlanTypeBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | PlanTypeBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | PlanTypeBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | PlanTypeBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | PlanTypeBasePEOPlanClassCode | PLAN_CLASS_CODE | — | — |
| 15 | PlanTypeBasePEOPlanInMultiCurrFlag | PLAN_IN_MULTI_CURR_FLAG | — | — |
| 16 | PlanTypeBasePEOPlanOptionCode | PLAN_OPTION_CODE | — | — |
| 17 | PlanTypeBasePEOPlanTypeCode | PLAN_TYPE_CODE | — | — |
| 18 | PlanTypeBasePEOPlanTypeId | PLAN_TYPE_ID | — | — |
| 19 | PlanTypeBasePEOPrimaryCostForecastFlag | PRIMARY_COST_FORECAST_FLAG | — | — |
| 20 | PlanTypeBasePEOPrimaryRevForecastFlag | PRIMARY_REV_FORECAST_FLAG | — | — |
| 21 | PlanTypeBasePEOReportQuantityFromCode | REPORT_QUANTITY_FROM_CODE | — | — |
| 22 | PlanTypeBasePEOStartDate | START_DATE | — | ✅ |

### [[pjo_plan_types_tl|PJO_PLAN_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlanTypeTranslationPEODescription | DESCRIPTION | — | ✅ |
| 2 | PlanTypeTranslationPEOLanguage | LANGUAGE | — | — |
| 3 | PlanTypeTranslationPEOName | NAME | — | ✅ |
| 4 | PlanTypeTranslationPEOPlanTypeId | PLAN_TYPE_ID | — | — |

### [[pjo_plan_types_vl|PJO_PLAN_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CopySrcPlanTypeForPlanOptionName | NAME | — | — |
| 2 | CopySrcPlanTypeForPlanOptionPlanTypeId | PLAN_TYPE_ID | — | — |
| 3 | GenSrcPlanTypeForPlanOptionName | NAME | — | — |
| 4 | GenSrcPlanTypeForPlanOptionPlanTypeId | PLAN_TYPE_ID | — | — |

### [[pjo_plan_versions_b|PJO_PLAN_VERSIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlanVersionBasePEOActualAmtsThruPeriod | ACTUAL_AMTS_THRU_PERIOD | — | — |
| 2 | PlanVersionBasePEOBaselinedByPersonId | BASELINED_BY_PERSON_ID | — | — |
| 3 | PlanVersionBasePEOBaselinedDate | BASELINED_DATE | — | ✅ |
| 4 | PlanVersionBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | PlanVersionBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | PlanVersionBasePEOCurrentPlanStatusFlag | CURRENT_PLAN_STATUS_FLAG | — | ✅ |
| 7 | PlanVersionBasePEOEquipmentQuantity | EQUIPMENT_QUANTITY | — | — |
| 8 | PlanVersionBasePEOEtcStartDate | ETC_START_DATE | — | ✅ |
| 9 | PlanVersionBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 10 | PlanVersionBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 11 | PlanVersionBasePEOLastAmtGenDate | LAST_AMT_GEN_DATE | — | ✅ |
| 12 | PlanVersionBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | PlanVersionBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | PlanVersionBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | PlanVersionBasePEOLockedByPersonId | LOCKED_BY_PERSON_ID | — | — |
| 16 | PlanVersionBasePEOMultiErrorFlag | MULTI_ERROR_FLAG | — | — |
| 17 | PlanVersionBasePEOObjectId1 | OBJECT_ID1 | — | — |
| 18 | PlanVersionBasePEOObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 19 | PlanVersionBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | PlanVersionBasePEOOriginalFlag | ORIGINAL_FLAG | — | ✅ |
| 21 | PlanVersionBasePEOPeopleQuantity | PEOPLE_QUANTITY | — | — |
| 22 | PlanVersionBasePEOPfcBrdndCost | PFC_BRDND_COST | — | — |
| 23 | PlanVersionBasePEOPfcRawCost | PFC_RAW_COST | — | — |
| 24 | PlanVersionBasePEOPfcRevenue | PFC_REVENUE | — | — |
| 25 | PlanVersionBasePEOPjiSummarizedFlag | PJI_SUMMARIZED_FLAG | — | — |
| 26 | PlanVersionBasePEOPjsSummaryId | PJS_SUMMARY_ID | — | — |
| 27 | PlanVersionBasePEOPlanClassCode | PLAN_CLASS_CODE | — | ✅ |
| 28 | PlanVersionBasePEOPlanProcessStatusCode | PLAN_PROCESS_STATUS_CODE | — | — |
| 29 | PlanVersionBasePEOPlanProcessingCode | PLAN_PROCESSING_CODE | — | — |
| 30 | PlanVersionBasePEOPlanRunDate | PLAN_RUN_DATE | — | ✅ |
| 31 | PlanVersionBasePEOPlanStatusCode | PLAN_STATUS_CODE | — | ✅ |
| 32 | PlanVersionBasePEOPlanTypeId | PLAN_TYPE_ID | — | ✅ |
| 33 | PlanVersionBasePEOPlannedForCode | PLANNED_FOR_CODE | — | ✅ |
| 34 | PlanVersionBasePEOPmBudgetReference | PM_BUDGET_REFERENCE | — | — |
| 35 | PlanVersionBasePEOPmProductCode | PM_PRODUCT_CODE | — | — |
| 36 | PlanVersionBasePEOProjectId | PROJECT_ID | — | ✅ |
| 37 | PlanVersionBasePEORejectedBy | REJECTED_BY | — | ✅ |
| 38 | PlanVersionBasePEORejectionDate | REJECTION_DATE | — | ✅ |
| 39 | PlanVersionBasePEORequestId | REQUEST_ID | — | — |
| 40 | PlanVersionBasePEOStructureVersionId | STRUCTURE_VERSION_ID | — | — |
| 41 | PlanVersionBasePEOSubmittedBy | SUBMITTED_BY | — | ✅ |
| 42 | PlanVersionBasePEOSubmittedDate | SUBMITTED_DATE | — | — |
| 43 | PlanVersionBasePEOTotalPcBrdndCost | TOTAL_PC_BRDND_COST | — | — |
| 44 | PlanVersionBasePEOTotalPcRawCost | TOTAL_PC_RAW_COST | — | — |
| 45 | PlanVersionBasePEOTotalPcRevenue | TOTAL_PC_REVENUE | — | — |
| 46 | PlanVersionBasePEOVersionNumber | VERSION_NUMBER | — | ✅ |
| 47 | PlanVersionBasePEOWfStatusCode | WF_STATUS_CODE | — | — |
| 48 | PlanVersionId | PLAN_VERSION_ID | 🔑 | ✅ |

### [[pjo_plan_versions_tl|PJO_PLAN_VERSIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlanVersionTranslationPEODescription | DESCRIPTION | — | ✅ |
| 2 | PlanVersionTranslationPEOLanguage | LANGUAGE | — | — |
| 3 | PlanVersionTranslationPEOPlanVersionId | PLAN_VERSION_ID | — | — |
| 4 | PlanVersionTranslationPEOVersionName | VERSION_NAME | — | ✅ |

### [[pjo_plan_versions_vl|PJO_PLAN_VERSIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CopySrcPlanVersForPlanOptionPlanVersionId | PLAN_VERSION_ID | — | — |
| 2 | CopySrcPlanVersForPlanOptionVersionName | VERSION_NAME | — | — |
| 3 | CopySrcPlanVersForPlanOptionVersionNumber | VERSION_NUMBER | — | — |
| 4 | GenSrcPlanVersForPlanOptionPlanVersionId | PLAN_VERSION_ID | — | — |
| 5 | GenSrcPlanVersForPlanOptionVersionName | VERSION_NAME | — | — |
| 6 | GenSrcPlanVersForPlanOptionVersionNumber | VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
