---
id: DOC-OTHER-PVO-ProjectRefPVO
doc_type: system-doc
title: "ProjectRefPVO — PVO Cross-Module"
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
  - ProjectRefPVO
  - projectrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectRefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Ref. Acessa as tabelas: FND_CURRENCIES_VL, FND_SETID_SETS_VL, GL_DAILY_CONVERSION_TYPES (+21).

**Caminho:** `FscmTopModelAM.PjfProjectAM.ProjectRefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 322 | 24 | 1 | 149 | 46% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_currencies_vl|FND_CURRENCIES_VL]] — 6 atributos
- [[fnd_setid_sets_vl|FND_SETID_SETS_VL]] — 3 atributos
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 3 atributos
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 4 atributos (1 BICC)
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 6 atributos (2 BICC)
- [[hr_organization_v|HR_ORGANIZATION_V]] — 12 atributos (4 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 4 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 5 atributos (2 BICC)
- [[pjc_cint_rate_sch_vl|PJC_CINT_RATE_SCH_VL]] — 6 atributos (1 BICC)
- [[pjf_ind_rate_sch_vl|PJF_IND_RATE_SCH_VL]] — 6 atributos
- [[pjf_latestprojectmanager_v|PJF_LATESTPROJECTMANAGER_V]] — 4 atributos (1 BICC)
- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 92 atributos (1 PKs, 36 BICC)
- [[pjf_projects_all_tl|PJF_PROJECTS_ALL_TL]] — 12 atributos (4 BICC)
- [[pjf_projects_all_vl|PJF_PROJECTS_ALL_VL]] — 5 atributos
- [[pjf_project_statuses_vl|PJF_PROJECT_STATUSES_VL]] — 5 atributos (3 BICC)
- [[pjf_project_types_b|PJF_PROJECT_TYPES_B]] — 33 atributos (14 BICC)
- [[pjf_project_types_tl|PJF_PROJECT_TYPES_TL]] — 11 atributos (1 BICC)
- [[pjf_proj_elements_vl|PJF_PROJ_ELEMENTS_VL]] — 77 atributos (71 BICC)
- [[pjf_tp_schedules|PJF_TP_SCHEDULES]] — 6 atributos
- [[pjf_work_types_vl|PJF_WORK_TYPES_VL]] — 5 atributos (1 BICC)
- [[pjo_project_progress|PJO_PROJECT_PROGRESS]] — 6 atributos (3 BICC)
- [[pjt_primaryprojmanager_v|PJT_PRIMARYPROJMANAGER_V]] — 4 atributos (2 BICC)
- [[pjt_schedules_vl|PJT_SCHEDULES_VL]] — 4 atributos (2 BICC)
- [[xle_entity_profiles|XLE_ENTITY_PROFILES]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[fnd_currencies_vl|FND_CURRENCIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectCurrencyCodePEOCurrencyCode | CURRENCY_CODE | — | — |
| 2 | ProjectCurrencyCodePEODescription | DESCRIPTION | — | — |
| 3 | ProjectCurrencyCodePEOName | NAME | — | — |
| 4 | ProjectFunctionalCurrencyPEOCurrencyCode | CURRENCY_CODE | — | — |
| 5 | ProjectFunctionalCurrencyPEODescription | DESCRIPTION | — | — |
| 6 | ProjectFunctionalCurrencyPEOName | NAME | — | — |

### [[fnd_setid_sets_vl|FND_SETID_SETS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SetIdSetPEODescription | DESCRIPTION | — | — |
| 2 | SetIdSetPEOSetId | SET_ID | — | — |
| 3 | SetIdSetPEOSetName | SET_NAME | — | — |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlDailyConversionTypesConversionType | CONVERSION_TYPE | — | — |
| 2 | GlDailyConversionTypesDescription | DESCRIPTION | — | — |
| 3 | GlDailyConversionTypesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOPrimaryLedgerId | ORG_INFORMATION3 | — | — |
| 2 | OrganizationInformationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | OrganizationInformationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | OrganizationInformationPEOOrgInformationId | ORG_INFORMATION_ID | — | — |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOBusinessUnitId | ORGANIZATION_ID | — | — |
| 2 | BusinessUnitPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | BusinessUnitPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | BusinessUnitPEOName | NAME | — | ✅ |
| 5 | OrganizationUnitTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | OrganizationUnitTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[hr_organization_v|HR_ORGANIZATION_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectOwningOrgDPEOClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | ProjectOwningOrgDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | ProjectOwningOrgDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | ProjectOwningOrgDPEOName | NAME | — | ✅ |
| 5 | ProjectOwningOrgDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | ProjectOwningOrgDPEOOrganizationId | ORGANIZATION_ID | — | — |
| 7 | ProjectUnitDPEOClassificationCode | CLASSIFICATION_CODE | — | — |
| 8 | ProjectUnitDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 9 | ProjectUnitDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 10 | ProjectUnitDPEOName | NAME | — | ✅ |
| 11 | ProjectUnitDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ProjectUnitDPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | PersonDPEOPersonId | PERSON_ID | — | — |
| 4 | PersonDPEOPersonNumber | PERSON_NUMBER | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNameDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonNameDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonNameDPEOListName | LIST_NAME | — | ✅ |
| 4 | PersonNameDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | PersonNameDPEOPersonNameId | PERSON_NAME_ID | — | — |

### [[pjc_cint_rate_sch_vl|PJC_CINT_RATE_SCH_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CapitalInterestRateSchPEOCintRateSchId | CINT_RATE_SCH_ID | — | — |
| 2 | CapitalInterestRateSchPEODescription | DESCRIPTION | — | — |
| 3 | CapitalInterestRateSchPEORateSchName | RATE_SCH_NAME | — | — |
| 4 | ProjectTypeBaseCIntPEOCintRateSchId | CINT_RATE_SCH_ID | — | — |
| 5 | ProjectTypeBaseCIntPEODescription | DESCRIPTION | — | — |
| 6 | ProjectTypeBaseCIntPEORateSchName | RATE_SCH_NAME | — | ✅ |

### [[pjf_ind_rate_sch_vl|PJF_IND_RATE_SCH_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectBurdenSchedulePEODescription | DESCRIPTION | — | — |
| 2 | ProjectBurdenSchedulePEOIndRateSchId | IND_RATE_SCH_ID | — | — |
| 3 | ProjectBurdenSchedulePEOIndSchName | IND_SCH_NAME | — | — |
| 4 | ProjectTypeCostBurdenSchPEODescription | DESCRIPTION | — | — |
| 5 | ProjectTypeCostBurdenSchPEOIndRateSchId | IND_RATE_SCH_ID | — | — |
| 6 | ProjectTypeCostBurdenSchPEOIndSchName | IND_SCH_NAME | — | — |

### [[pjf_latestprojectmanager_v|PJF_LATESTPROJECTMANAGER_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LatesProjectManagerPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | LatesProjectManagerPEOProjectId | PROJECT_ID | — | — |
| 3 | LatesProjectManagerPEOProjectPartyId | PROJECT_PARTY_ID | — | — |
| 4 | LatesProjectManagerPEOResourceSourceId | RESOURCE_SOURCE_ID | — | — |

### [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectBaseCreatedFromPEOProjectId | PROJECT_ID | — | — |
| 2 | ProjectBaseCreatedFromPEOSegment1 | SEGMENT1 | — | ✅ |
| 3 | ProjectBasePEOActualAsOfDate | ACTUAL_AS_OF_DATE | — | — |
| 4 | ProjectBasePEOActualDuration | ACTUAL_DURATION | — | — |
| 5 | ProjectBasePEOActualFinishDate | ACTUAL_FINISH_DATE | — | — |
| 6 | ProjectBasePEOActualStartDate | ACTUAL_START_DATE | — | — |
| 7 | ProjectBasePEOAllowCrossChargeFlag | ALLOW_CROSS_CHARGE_FLAG | — | ✅ |
| 8 | ProjectBasePEOAssetAllocationMethod | ASSET_ALLOCATION_METHOD | — | ✅ |
| 9 | ProjectBasePEOBaselineAsOfDate | BASELINE_AS_OF_DATE | — | — |
| 10 | ProjectBasePEOBaselineDuration | BASELINE_DURATION | — | — |
| 11 | ProjectBasePEOBaselineFinishDate | BASELINE_FINISH_DATE | — | — |
| 12 | ProjectBasePEOBaselineStartDate | BASELINE_START_DATE | — | — |
| 13 | ProjectBasePEOBudgetaryControlFlag | BUDGETARY_CONTROL_FLAG | — | ✅ |
| 14 | ProjectBasePEOCapitalEventProcessing | CAPITAL_EVENT_PROCESSING | — | ✅ |
| 15 | ProjectBasePEOCarryingOutOrganizationId | CARRYING_OUT_ORGANIZATION_ID | — | ✅ |
| 16 | ProjectBasePEOCcProcessLaborFlag | CC_PROCESS_LABOR_FLAG | — | ✅ |
| 17 | ProjectBasePEOCcProcessNlFlag | CC_PROCESS_NL_FLAG | — | ✅ |
| 18 | ProjectBasePEOCintEligibleFlag | CINT_ELIGIBLE_FLAG | — | ✅ |
| 19 | ProjectBasePEOCintRateSchId | CINT_RATE_SCH_ID | — | — |
| 20 | ProjectBasePEOCintStopDate | CINT_STOP_DATE | — | — |
| 21 | ProjectBasePEOClinLinkedCode | CLIN_LINKED_CODE | — | ✅ |
| 22 | ProjectBasePEOClosedDate | CLOSED_DATE | — | ✅ |
| 23 | ProjectBasePEOCompletionDate | COMPLETION_DATE | — | ✅ |
| 24 | ProjectBasePEOCostIndRateSchId | COST_IND_RATE_SCH_ID | — | — |
| 25 | ProjectBasePEOCostIndSchFixedDate | COST_IND_SCH_FIXED_DATE | — | — |
| 26 | ProjectBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 27 | ProjectBasePEOCreatedFromProjectId | CREATED_FROM_PROJECT_ID | — | — |
| 28 | ProjectBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 29 | ProjectBasePEOCurrencyConvDate | CURRENCY_CONV_DATE | — | — |
| 30 | ProjectBasePEOCurrencyConvDateTypeCode | CURRENCY_CONV_DATE_TYPE_CODE | — | — |
| 31 | ProjectBasePEOCurrencyConvRateType | CURRENCY_CONV_RATE_TYPE | — | — |
| 32 | ProjectBasePEOEarlyFinishDate | EARLY_FINISH_DATE | — | — |
| 33 | ProjectBasePEOEarlyStartDate | EARLY_START_DATE | — | — |
| 34 | ProjectBasePEOEnabledFlag | ENABLED_FLAG | — | — |
| 35 | ProjectBasePEOExpectedApprovalDate | EXPECTED_APPROVAL_DATE | — | — |
| 36 | ProjectBasePEOExternalProjectId | EXTERNAL_PROJECT_ID | — | ✅ |
| 37 | ProjectBasePEOHoursPerDay | HOURS_PER_DAY | — | ✅ |
| 38 | ProjectBasePEOIcClinLinkedCode | IC_CLIN_LINKED_CODE | — | — |
| 39 | ProjectBasePEOIntegratedProductCode | INTEGRATED_PRODUCT_CODE | — | — |
| 40 | ProjectBasePEOIntegratedProjectReference | INTEGRATED_PROJECT_REFERENCE | — | — |
| 41 | ProjectBasePEOKpiNotificationEnabled | KPI_NOTIFICATION_ENABLED | — | — |
| 42 | ProjectBasePEOKpiNotificationIncludeNotes | KPI_NOTIFICATION_INCLUDE_NOTES | — | — |
| 43 | ProjectBasePEOKpiNotificationRecipients | KPI_NOTIFICATION_RECIPIENTS | — | — |
| 44 | ProjectBasePEOLaborTpFixedDate | LABOR_TP_FIXED_DATE | — | — |
| 45 | ProjectBasePEOLaborTpScheduleId | LABOR_TP_SCHEDULE_ID | — | — |
| 46 | ProjectBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 47 | ProjectBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 48 | ProjectBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 49 | ProjectBasePEOLateFinishDate | LATE_FINISH_DATE | — | — |
| 50 | ProjectBasePEOLateStartDate | LATE_START_DATE | — | — |
| 51 | ProjectBasePEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 52 | ProjectBasePEOLimitToTxnControlsFlag | LIMIT_TO_TXN_CONTROLS_FLAG | — | ✅ |
| 53 | ProjectBasePEONlTpFixedDate | NL_TP_FIXED_DATE | — | — |
| 54 | ProjectBasePEONlTpScheduleId | NL_TP_SCHEDULE_ID | — | — |
| 55 | ProjectBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 56 | ProjectBasePEOOrgId | ORG_ID | — | ✅ |
| 57 | ProjectBasePEOOutlineLevel | OUTLINE_LEVEL | — | — |
| 58 | ProjectBasePEOOvrCostIndRateSchId | OVR_COST_IND_RATE_SCH_ID | — | — |
| 59 | ProjectBasePEOPlanningProjectFlag | PLANNING_PROJECT_FLAG | — | — |
| 60 | ProjectBasePEOPmProductCode | PM_PRODUCT_CODE | — | ✅ |
| 61 | ProjectBasePEOPmProjectReference | PM_PROJECT_REFERENCE | — | ✅ |
| 62 | ProjectBasePEOPriorityCode | PRIORITY_CODE | — | ✅ |
| 63 | ProjectBasePEOProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 64 | ProjectBasePEOProgramId | PROGRAM_ID | — | — |
| 65 | ProjectBasePEOProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 66 | ProjectBasePEOProjectCalendarId | PROJECT_CALENDAR_ID | — | ✅ |
| 67 | ProjectBasePEOProjectCategory | PROJECT_CATEGORY | — | ✅ |
| 68 | ProjectBasePEOProjectCurrencyCode | PROJECT_CURRENCY_CODE | — | ✅ |
| 69 | ProjectBasePEOProjectStatusCode | PROJECT_STATUS_CODE | — | ✅ |
| 70 | ProjectBasePEOProjectTypeId | PROJECT_TYPE_ID | — | ✅ |
| 71 | ProjectBasePEOProjectUnitId | PROJECT_UNIT_ID | — | — |
| 72 | ProjectBasePEOProjectValue | PROJECT_VALUE | — | ✅ |
| 73 | ProjectBasePEOProjfuncCurrencyCode | PROJFUNC_CURRENCY_CODE | — | ✅ |
| 74 | ProjectBasePEOPublicSectorFlag | PUBLIC_SECTOR_FLAG | — | ✅ |
| 75 | ProjectBasePEORequestId | REQUEST_ID | — | — |
| 76 | ProjectBasePEOScheduledAsOfDate | SCHEDULED_AS_OF_DATE | — | — |
| 77 | ProjectBasePEOScheduledDuration | SCHEDULED_DURATION | — | — |
| 78 | ProjectBasePEOScheduledFinishDate | SCHEDULED_FINISH_DATE | — | — |
| 79 | ProjectBasePEOScheduledStartDate | SCHEDULED_START_DATE | — | — |
| 80 | ProjectBasePEOSegment1 | SEGMENT1 | — | ✅ |
| 81 | ProjectBasePEOServiceTypeCode | SERVICE_TYPE_CODE | — | ✅ |
| 82 | ProjectBasePEOStartDate | START_DATE | — | ✅ |
| 83 | ProjectBasePEOStructureSharingCode | STRUCTURE_SHARING_CODE | — | — |
| 84 | ProjectBasePEOSummaryFlag | SUMMARY_FLAG | — | — |
| 85 | ProjectBasePEOTargetFinishDate | TARGET_FINISH_DATE | — | — |
| 86 | ProjectBasePEOTargetStartDate | TARGET_START_DATE | — | — |
| 87 | ProjectBasePEOTemplateEndDateActive | TEMPLATE_END_DATE_ACTIVE | — | — |
| 88 | ProjectBasePEOTemplateFlag | TEMPLATE_FLAG | — | ✅ |
| 89 | ProjectBasePEOTemplateStartDateActive | TEMPLATE_START_DATE_ACTIVE | — | — |
| 90 | ProjectBasePEOVerificationDate | VERIFICATION_DATE | — | — |
| 91 | ProjectBasePEOWorkTypeId | WORK_TYPE_ID | — | — |
| 92 | ProjectId | PROJECT_ID | 🔑 | ✅ |

### [[pjf_projects_all_tl|PJF_PROJECTS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | ProjectTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | ProjectTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | ProjectTranslationPEOExecutionCustomerName | EXECUTION_CUSTOMER_NAME | — | ✅ |
| 5 | ProjectTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | ProjectTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ProjectTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ProjectTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ProjectTranslationPEOName | NAME | — | ✅ |
| 10 | ProjectTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ProjectTranslationPEOProjectId | PROJECT_ID | — | — |
| 12 | ProjectTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[pjf_projects_all_vl|PJF_PROJECTS_ALL_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectPEOName | NAME | — | — |
| 2 | ProjectPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | ProjectPEOProjectId | PROJECT_ID | — | — |
| 4 | ProjectTypeBurdenCostPrjPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | ProjectTypeBurdenCostPrjPEOProjectId | PROJECT_ID | — | — |

### [[pjf_project_statuses_vl|PJF_PROJECT_STATUSES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectStatusPEODescription | DESCRIPTION | — | ✅ |
| 2 | ProjectStatusPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | ProjectStatusPEOProjectStatusCode | PROJECT_STATUS_CODE | — | — |
| 4 | ProjectStatusPEOProjectStatusName | PROJECT_STATUS_NAME | — | ✅ |
| 5 | ProjectStatusPEOProjectSystemStatusCode | PROJECT_SYSTEM_STATUS_CODE | — | ✅ |

### [[pjf_project_types_b|PJF_PROJECT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectTypeBasePEOAssetAllocationMethod | ASSET_ALLOCATION_METHOD | — | ✅ |
| 2 | ProjectTypeBasePEOBurdenAccountFlag | BURDEN_ACCOUNT_FLAG | — | — |
| 3 | ProjectTypeBasePEOBurdenAmtDisplayMethod | BURDEN_AMT_DISPLAY_METHOD | — | — |
| 4 | ProjectTypeBasePEOBurdenCostFlag | BURDEN_COST_FLAG | — | ✅ |
| 5 | ProjectTypeBasePEOBurdenCostJournalFlag | BURDEN_COST_JOURNAL_FLAG | — | — |
| 6 | ProjectTypeBasePEOBurdenSumDestProjectId | BURDEN_SUM_DEST_PROJECT_ID | — | — |
| 7 | ProjectTypeBasePEOBurdenSumDestTaskId | BURDEN_SUM_DEST_TASK_ID | — | — |
| 8 | ProjectTypeBasePEOCapitalCostTypeCode | CAPITAL_COST_TYPE_CODE | — | ✅ |
| 9 | ProjectTypeBasePEOCapitalEventProcessing | CAPITAL_EVENT_PROCESSING | — | ✅ |
| 10 | ProjectTypeBasePEOCintRateSchId | CINT_RATE_SCH_ID | — | — |
| 11 | ProjectTypeBasePEOCintSchOverrideFlag | CINT_SCH_OVERRIDE_FLAG | — | ✅ |
| 12 | ProjectTypeBasePEOCipGroupingMethodCode | CIP_GROUPING_METHOD_CODE | — | ✅ |
| 13 | ProjectTypeBasePEOCostIndRateSchId | COST_IND_RATE_SCH_ID | — | — |
| 14 | ProjectTypeBasePEOCostSchOverrideFlag | COST_SCH_OVERRIDE_FLAG | — | ✅ |
| 15 | ProjectTypeBasePEOCreatedBy | CREATED_BY | — | — |
| 16 | ProjectTypeBasePEOCreationDate | CREATION_DATE | — | — |
| 17 | ProjectTypeBasePEOEnableBillingFlag | ENABLE_BILLING_FLAG | — | ✅ |
| 18 | ProjectTypeBasePEOEnableCapitalizationFlag | ENABLE_CAPITALIZATION_FLAG | — | ✅ |
| 19 | ProjectTypeBasePEOEndDateActive | END_DATE_ACTIVE | — | — |
| 20 | ProjectTypeBasePEOInterfaceAssetCostCode | INTERFACE_ASSET_COST_CODE | — | — |
| 21 | ProjectTypeBasePEOInterfaceCompleteAssetFlag | INTERFACE_COMPLETE_ASSET_FLAG | — | ✅ |
| 22 | ProjectTypeBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | ProjectTypeBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 24 | ProjectTypeBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 25 | ProjectTypeBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 26 | ProjectTypeBasePEOOverrideAssetAssignmentFlag | OVERRIDE_ASSET_ASSIGNMENT_FLAG | — | ✅ |
| 27 | ProjectTypeBasePEOProjectTypeId | PROJECT_TYPE_ID | — | — |
| 28 | ProjectTypeBasePEOSetId | SET_ID | — | — |
| 29 | ProjectTypeBasePEOSponsoredFlag | SPONSORED_FLAG | — | ✅ |
| 30 | ProjectTypeBasePEOStartDateActive | START_DATE_ACTIVE | — | — |
| 31 | ProjectTypeBasePEOTotalBurdenedJournalFlag | TOTAL_BURDENED_JOURNAL_FLAG | — | — |
| 32 | ProjectTypeBasePEOVendorInvoiceGroupingCode | VENDOR_INVOICE_GROUPING_CODE | — | ✅ |
| 33 | ProjectTypeBasePEOWorkTypeId | WORK_TYPE_ID | — | — |

### [[pjf_project_types_tl|PJF_PROJECT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectTypeTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | ProjectTypeTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | ProjectTypeTranslationPEODescription | DESCRIPTION | — | — |
| 4 | ProjectTypeTranslationPEOLanguage | LANGUAGE | — | — |
| 5 | ProjectTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ProjectTypeTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ProjectTypeTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ProjectTypeTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ProjectTypeTranslationPEOProjectType | PROJECT_TYPE | — | — |
| 10 | ProjectTypeTranslationPEOProjectTypeId | PROJECT_TYPE_ID | — | — |
| 11 | ProjectTypeTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[pjf_proj_elements_vl|PJF_PROJ_ELEMENTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectCodesPEONumberAttr01 | NUMBER_ATTR01 | — | ✅ |
| 2 | ProjectCodesPEONumberAttr02 | NUMBER_ATTR02 | — | ✅ |
| 3 | ProjectCodesPEONumberAttr03 | NUMBER_ATTR03 | — | ✅ |
| 4 | ProjectCodesPEONumberAttr04 | NUMBER_ATTR04 | — | ✅ |
| 5 | ProjectCodesPEONumberAttr05 | NUMBER_ATTR05 | — | ✅ |
| 6 | ProjectCodesPEONumberAttr06 | NUMBER_ATTR06 | — | ✅ |
| 7 | ProjectCodesPEONumberAttr07 | NUMBER_ATTR07 | — | ✅ |
| 8 | ProjectCodesPEONumberAttr08 | NUMBER_ATTR08 | — | ✅ |
| 9 | ProjectCodesPEONumberAttr09 | NUMBER_ATTR09 | — | ✅ |
| 10 | ProjectCodesPEONumberAttr10 | NUMBER_ATTR10 | — | ✅ |
| 11 | ProjectCodesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ProjectCodesPEOProjElementId | PROJ_ELEMENT_ID | — | — |
| 13 | ProjectCodesPEOTaskCode01Id | TASK_CODE01_ID | — | ✅ |
| 14 | ProjectCodesPEOTaskCode02Id | TASK_CODE02_ID | — | ✅ |
| 15 | ProjectCodesPEOTaskCode03Id | TASK_CODE03_ID | — | ✅ |
| 16 | ProjectCodesPEOTaskCode04Id | TASK_CODE04_ID | — | ✅ |
| 17 | ProjectCodesPEOTaskCode05Id | TASK_CODE05_ID | — | ✅ |
| 18 | ProjectCodesPEOTaskCode06Id | TASK_CODE06_ID | — | ✅ |
| 19 | ProjectCodesPEOTaskCode07Id | TASK_CODE07_ID | — | ✅ |
| 20 | ProjectCodesPEOTaskCode08Id | TASK_CODE08_ID | — | ✅ |
| 21 | ProjectCodesPEOTaskCode09Id | TASK_CODE09_ID | — | ✅ |
| 22 | ProjectCodesPEOTaskCode10Id | TASK_CODE10_ID | — | ✅ |
| 23 | ProjectCodesPEOTaskCode11Id | TASK_CODE11_ID | — | ✅ |
| 24 | ProjectCodesPEOTaskCode12Id | TASK_CODE12_ID | — | ✅ |
| 25 | ProjectCodesPEOTaskCode13Id | TASK_CODE13_ID | — | ✅ |
| 26 | ProjectCodesPEOTaskCode14Id | TASK_CODE14_ID | — | ✅ |
| 27 | ProjectCodesPEOTaskCode15Id | TASK_CODE15_ID | — | ✅ |
| 28 | ProjectCodesPEOTaskCode16Id | TASK_CODE16_ID | — | ✅ |
| 29 | ProjectCodesPEOTaskCode17Id | TASK_CODE17_ID | — | ✅ |
| 30 | ProjectCodesPEOTaskCode18Id | TASK_CODE18_ID | — | ✅ |
| 31 | ProjectCodesPEOTaskCode19Id | TASK_CODE19_ID | — | ✅ |
| 32 | ProjectCodesPEOTaskCode20Id | TASK_CODE20_ID | — | ✅ |
| 33 | ProjectCodesPEOTaskCode21Id | TASK_CODE21_ID | — | ✅ |
| 34 | ProjectCodesPEOTaskCode22Id | TASK_CODE22_ID | — | ✅ |
| 35 | ProjectCodesPEOTaskCode23Id | TASK_CODE23_ID | — | ✅ |
| 36 | ProjectCodesPEOTaskCode24Id | TASK_CODE24_ID | — | ✅ |
| 37 | ProjectCodesPEOTaskCode25Id | TASK_CODE25_ID | — | ✅ |
| 38 | ProjectCodesPEOTaskCode26Id | TASK_CODE26_ID | — | ✅ |
| 39 | ProjectCodesPEOTaskCode27Id | TASK_CODE27_ID | — | ✅ |
| 40 | ProjectCodesPEOTaskCode28Id | TASK_CODE28_ID | — | ✅ |
| 41 | ProjectCodesPEOTaskCode29Id | TASK_CODE29_ID | — | ✅ |
| 42 | ProjectCodesPEOTaskCode30Id | TASK_CODE30_ID | — | ✅ |
| 43 | ProjectCodesPEOTaskCode31Id | TASK_CODE31_ID | — | ✅ |
| 44 | ProjectCodesPEOTaskCode32Id | TASK_CODE32_ID | — | ✅ |
| 45 | ProjectCodesPEOTaskCode33Id | TASK_CODE33_ID | — | ✅ |
| 46 | ProjectCodesPEOTaskCode34Id | TASK_CODE34_ID | — | ✅ |
| 47 | ProjectCodesPEOTaskCode35Id | TASK_CODE35_ID | — | ✅ |
| 48 | ProjectCodesPEOTaskCode36Id | TASK_CODE36_ID | — | ✅ |
| 49 | ProjectCodesPEOTaskCode37Id | TASK_CODE37_ID | — | ✅ |
| 50 | ProjectCodesPEOTaskCode38Id | TASK_CODE38_ID | — | ✅ |
| 51 | ProjectCodesPEOTaskCode39Id | TASK_CODE39_ID | — | ✅ |
| 52 | ProjectCodesPEOTaskCode40Id | TASK_CODE40_ID | — | ✅ |
| 53 | ProjectCodesPEOTextAttr01 | TEXT_ATTR01 | — | ✅ |
| 54 | ProjectCodesPEOTextAttr02 | TEXT_ATTR02 | — | ✅ |
| 55 | ProjectCodesPEOTextAttr03 | TEXT_ATTR03 | — | ✅ |
| 56 | ProjectCodesPEOTextAttr04 | TEXT_ATTR04 | — | ✅ |
| 57 | ProjectCodesPEOTextAttr05 | TEXT_ATTR05 | — | ✅ |
| 58 | ProjectCodesPEOTextAttr06 | TEXT_ATTR06 | — | ✅ |
| 59 | ProjectCodesPEOTextAttr07 | TEXT_ATTR07 | — | ✅ |
| 60 | ProjectCodesPEOTextAttr08 | TEXT_ATTR08 | — | ✅ |
| 61 | ProjectCodesPEOTextAttr09 | TEXT_ATTR09 | — | ✅ |
| 62 | ProjectCodesPEOTextAttr10 | TEXT_ATTR10 | — | ✅ |
| 63 | ProjectCodesPEOTextAttr11 | TEXT_ATTR11 | — | ✅ |
| 64 | ProjectCodesPEOTextAttr12 | TEXT_ATTR12 | — | ✅ |
| 65 | ProjectCodesPEOTextAttr13 | TEXT_ATTR13 | — | ✅ |
| 66 | ProjectCodesPEOTextAttr14 | TEXT_ATTR14 | — | ✅ |
| 67 | ProjectCodesPEOTextAttr15 | TEXT_ATTR15 | — | ✅ |
| 68 | ProjectCodesPEOTextAttr16 | TEXT_ATTR16 | — | ✅ |
| 69 | ProjectCodesPEOTextAttr17 | TEXT_ATTR17 | — | ✅ |
| 70 | ProjectCodesPEOTextAttr18 | TEXT_ATTR18 | — | ✅ |
| 71 | ProjectCodesPEOTextAttr19 | TEXT_ATTR19 | — | ✅ |
| 72 | ProjectCodesPEOTextAttr20 | TEXT_ATTR20 | — | ✅ |
| 73 | TaskStructurePEODescription | DESCRIPTION | — | — |
| 74 | TaskStructurePEOName | NAME | — | — |
| 75 | TaskStructurePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 76 | TaskStructurePEOProjElementId | PROJ_ELEMENT_ID | — | — |
| 77 | TaskTypeCode | TASK_TYPE_CODE | — | ✅ |

### [[pjf_tp_schedules|PJF_TP_SCHEDULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LaborTransferPriceSchedPEODescription | DESCRIPTION | — | — |
| 2 | LaborTransferPriceSchedPEOTpScheduleId | TP_SCHEDULE_ID | — | — |
| 3 | LaborTransferPriceSchedPEOTpScheduleName | TP_SCHEDULE_NAME | — | — |
| 4 | NonLaborTransferPriceSchedPEODescription | DESCRIPTION | — | — |
| 5 | NonLaborTransferPriceSchedPEOTpScheduleId | TP_SCHEDULE_ID | — | — |
| 6 | NonLaborTransferPriceSchedPEOTpScheduleName | TP_SCHEDULE_NAME | — | — |

### [[pjf_work_types_vl|PJF_WORK_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectTypeWorkTypePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | ProjectTypeWorkTypePEOWorkTypeId | WORK_TYPE_ID | — | — |
| 3 | WorkTypePEOName | NAME | — | ✅ |
| 4 | WorkTypePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | WorkTypePEOWorkTypeId | WORK_TYPE_ID | — | — |

### [[pjo_project_progress|PJO_PROJECT_PROGRESS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectProgressPEOActualFinishDate | ACTUAL_FINISH_DATE | — | ✅ |
| 2 | ProjectProgressPEOActualStartDate | ACTUAL_START_DATE | — | ✅ |
| 3 | ProjectProgressPEOEstimatedFinishDate | ESTIMATED_FINISH_DATE | — | ✅ |
| 4 | ProjectProgressPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | ProjectProgressPEOProjectId | PROJECT_ID | — | — |
| 6 | ProjectProgressPEOProjectProgressId | PROJECT_PROGRESS_ID | — | — |

### [[pjt_primaryprojmanager_v|PJT_PRIMARYPROJMANAGER_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrimaryProjectManagerPEODisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PrimaryProjectManagerPEOEmail | EMAIL | — | ✅ |
| 3 | PrimaryProjectManagerPEOProjectId | PROJECT_ID | — | — |
| 4 | PrimaryProjectManagerPEOResourceId | RESOURCE_ID | — | — |

### [[pjt_schedules_vl|PJT_SCHEDULES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SchedulesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | SchedulesPEOScheduleDesc | SCHEDULE_DESC | — | ✅ |
| 3 | SchedulesPEOScheduleId | SCHEDULE_ID | — | — |
| 4 | SchedulesPEOScheduleName | SCHEDULE_NAME | — | ✅ |

### [[xle_entity_profiles|XLE_ENTITY_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LegalEntityPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 2 | LegalEntityPEOName | NAME | — | ✅ |
| 3 | LegalEntityPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
