---
id: DOC-OTHER-PVO-ProjectView
doc_type: system-doc
title: "ProjectView — PVO Cross-Module"
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
  - ProjectView
  - projectview
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectView

## 📌 Visão Geral

View Object para extração BICC de dados de Project View. Acessa as tabelas: FND_CURRENCIES_VL, FND_SETID_SETS_VL, GL_DAILY_CONVERSION_TYPES (+19).

**Caminho:** `FscmTopModelAM.PjfProjectAM.ProjectView`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 301 | 22 | 1 | 149 | 50% |

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
- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 2 atributos (1 BICC)
- [[pjf_projects_all_vl|PJF_PROJECTS_ALL_VL]] — 95 atributos (1 PKs, 37 BICC)
- [[pjf_project_statuses_vl|PJF_PROJECT_STATUSES_VL]] — 5 atributos (3 BICC)
- [[pjf_project_types_vl|PJF_PROJECT_TYPES_VL]] — 35 atributos (17 BICC)
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
| 4 | ProjectTypeCIntPEOCintRateSchId | CINT_RATE_SCH_ID | — | — |
| 5 | ProjectTypeCIntPEODescription | DESCRIPTION | — | — |
| 6 | ProjectTypeCIntPEORateSchName | RATE_SCH_NAME | — | ✅ |

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

### [[pjf_projects_all_vl|PJF_PROJECTS_ALL_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectId | PROJECT_ID | 🔑 | ✅ |
| 2 | ProjectPEOActualAsOfDate | ACTUAL_AS_OF_DATE | — | — |
| 3 | ProjectPEOActualDuration | ACTUAL_DURATION | — | — |
| 4 | ProjectPEOActualFinishDate | ACTUAL_FINISH_DATE | — | — |
| 5 | ProjectPEOActualStartDate | ACTUAL_START_DATE | — | — |
| 6 | ProjectPEOAllowCrossChargeFlag | ALLOW_CROSS_CHARGE_FLAG | — | ✅ |
| 7 | ProjectPEOAssetAllocationMethod | ASSET_ALLOCATION_METHOD | — | ✅ |
| 8 | ProjectPEOBaselineAsOfDate | BASELINE_AS_OF_DATE | — | — |
| 9 | ProjectPEOBaselineDuration | BASELINE_DURATION | — | — |
| 10 | ProjectPEOBaselineFinishDate | BASELINE_FINISH_DATE | — | — |
| 11 | ProjectPEOBaselineStartDate | BASELINE_START_DATE | — | — |
| 12 | ProjectPEOBudgetaryControlFlag | BUDGETARY_CONTROL_FLAG | — | ✅ |
| 13 | ProjectPEOCapitalEventProcessing | CAPITAL_EVENT_PROCESSING | — | ✅ |
| 14 | ProjectPEOCarryingOutOrganizationId | CARRYING_OUT_ORGANIZATION_ID | — | ✅ |
| 15 | ProjectPEOCcProcessLaborFlag | CC_PROCESS_LABOR_FLAG | — | ✅ |
| 16 | ProjectPEOCcProcessNlFlag | CC_PROCESS_NL_FLAG | — | ✅ |
| 17 | ProjectPEOCintEligibleFlag | CINT_ELIGIBLE_FLAG | — | ✅ |
| 18 | ProjectPEOCintRateSchId | CINT_RATE_SCH_ID | — | — |
| 19 | ProjectPEOCintStopDate | CINT_STOP_DATE | — | — |
| 20 | ProjectPEOClinLinkedCode | CLIN_LINKED_CODE | — | ✅ |
| 21 | ProjectPEOClosedDate | CLOSED_DATE | — | ✅ |
| 22 | ProjectPEOCompletionDate | COMPLETION_DATE | — | ✅ |
| 23 | ProjectPEOCostIndRateSchId | COST_IND_RATE_SCH_ID | — | — |
| 24 | ProjectPEOCostIndSchFixedDate | COST_IND_SCH_FIXED_DATE | — | — |
| 25 | ProjectPEOCreatedBy | CREATED_BY | — | ✅ |
| 26 | ProjectPEOCreatedFromProjectId | CREATED_FROM_PROJECT_ID | — | — |
| 27 | ProjectPEOCreationDate | CREATION_DATE | — | ✅ |
| 28 | ProjectPEOCurrencyConvDate | CURRENCY_CONV_DATE | — | — |
| 29 | ProjectPEOCurrencyConvDateTypeCode | CURRENCY_CONV_DATE_TYPE_CODE | — | — |
| 30 | ProjectPEOCurrencyConvRateType | CURRENCY_CONV_RATE_TYPE | — | — |
| 31 | ProjectPEODescription | DESCRIPTION | — | ✅ |
| 32 | ProjectPEOEarlyFinishDate | EARLY_FINISH_DATE | — | — |
| 33 | ProjectPEOEarlyStartDate | EARLY_START_DATE | — | — |
| 34 | ProjectPEOEnabledFlag | ENABLED_FLAG | — | — |
| 35 | ProjectPEOExecutionCustomerName | EXECUTION_CUSTOMER_NAME | — | ✅ |
| 36 | ProjectPEOExpectedApprovalDate | EXPECTED_APPROVAL_DATE | — | — |
| 37 | ProjectPEOExternalProjectId | EXTERNAL_PROJECT_ID | — | ✅ |
| 38 | ProjectPEOHoursPerDay | HOURS_PER_DAY | — | ✅ |
| 39 | ProjectPEOIcClinLinkedCode | IC_CLIN_LINKED_CODE | — | — |
| 40 | ProjectPEOIntegratedProductCode | INTEGRATED_PRODUCT_CODE | — | — |
| 41 | ProjectPEOIntegratedProjectReference | INTEGRATED_PROJECT_REFERENCE | — | — |
| 42 | ProjectPEOKpiNotificationEnabled | KPI_NOTIFICATION_ENABLED | — | — |
| 43 | ProjectPEOKpiNotificationIncludeNotes | KPI_NOTIFICATION_INCLUDE_NOTES | — | — |
| 44 | ProjectPEOKpiNotificationRecipients | KPI_NOTIFICATION_RECIPIENTS | — | — |
| 45 | ProjectPEOLaborTpFixedDate | LABOR_TP_FIXED_DATE | — | — |
| 46 | ProjectPEOLaborTpScheduleId | LABOR_TP_SCHEDULE_ID | — | — |
| 47 | ProjectPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 48 | ProjectPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 49 | ProjectPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 50 | ProjectPEOLateFinishDate | LATE_FINISH_DATE | — | — |
| 51 | ProjectPEOLateStartDate | LATE_START_DATE | — | — |
| 52 | ProjectPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 53 | ProjectPEOLimitToTxnControlsFlag | LIMIT_TO_TXN_CONTROLS_FLAG | — | ✅ |
| 54 | ProjectPEOName | NAME | — | ✅ |
| 55 | ProjectPEONlTpFixedDate | NL_TP_FIXED_DATE | — | — |
| 56 | ProjectPEONlTpScheduleId | NL_TP_SCHEDULE_ID | — | — |
| 57 | ProjectPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 58 | ProjectPEOOrgId | ORG_ID | — | ✅ |
| 59 | ProjectPEOOutlineLevel | OUTLINE_LEVEL | — | — |
| 60 | ProjectPEOOvrCostIndRateSchId | OVR_COST_IND_RATE_SCH_ID | — | — |
| 61 | ProjectPEOPlanningProjectFlag | PLANNING_PROJECT_FLAG | — | — |
| 62 | ProjectPEOPmProductCode | PM_PRODUCT_CODE | — | ✅ |
| 63 | ProjectPEOPmProjectReference | PM_PROJECT_REFERENCE | — | ✅ |
| 64 | ProjectPEOPriorityCode | PRIORITY_CODE | — | ✅ |
| 65 | ProjectPEOProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 66 | ProjectPEOProgramId | PROGRAM_ID | — | — |
| 67 | ProjectPEOProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 68 | ProjectPEOProjectCalendarId | PROJECT_CALENDAR_ID | — | ✅ |
| 69 | ProjectPEOProjectCategory | PROJECT_CATEGORY | — | ✅ |
| 70 | ProjectPEOProjectCurrencyCode | PROJECT_CURRENCY_CODE | — | ✅ |
| 71 | ProjectPEOProjectStatusCode | PROJECT_STATUS_CODE | — | ✅ |
| 72 | ProjectPEOProjectTypeId | PROJECT_TYPE_ID | — | — |
| 73 | ProjectPEOProjectUnitId | PROJECT_UNIT_ID | — | — |
| 74 | ProjectPEOProjectValue | PROJECT_VALUE | — | ✅ |
| 75 | ProjectPEOProjfuncCurrencyCode | PROJFUNC_CURRENCY_CODE | — | ✅ |
| 76 | ProjectPEOPublicSectorFlag | PUBLIC_SECTOR_FLAG | — | ✅ |
| 77 | ProjectPEORequestId | REQUEST_ID | — | — |
| 78 | ProjectPEOScheduledAsOfDate | SCHEDULED_AS_OF_DATE | — | — |
| 79 | ProjectPEOScheduledDuration | SCHEDULED_DURATION | — | — |
| 80 | ProjectPEOScheduledFinishDate | SCHEDULED_FINISH_DATE | — | — |
| 81 | ProjectPEOScheduledStartDate | SCHEDULED_START_DATE | — | — |
| 82 | ProjectPEOSegment1 | SEGMENT1 | — | ✅ |
| 83 | ProjectPEOServiceTypeCode | SERVICE_TYPE_CODE | — | ✅ |
| 84 | ProjectPEOStartDate | START_DATE | — | ✅ |
| 85 | ProjectPEOStructureSharingCode | STRUCTURE_SHARING_CODE | — | — |
| 86 | ProjectPEOSummaryFlag | SUMMARY_FLAG | — | — |
| 87 | ProjectPEOTargetFinishDate | TARGET_FINISH_DATE | — | — |
| 88 | ProjectPEOTargetStartDate | TARGET_START_DATE | — | — |
| 89 | ProjectPEOTemplateEndDateActive | TEMPLATE_END_DATE_ACTIVE | — | — |
| 90 | ProjectPEOTemplateFlag | TEMPLATE_FLAG | — | ✅ |
| 91 | ProjectPEOTemplateStartDateActive | TEMPLATE_START_DATE_ACTIVE | — | — |
| 92 | ProjectPEOVerificationDate | VERIFICATION_DATE | — | — |
| 93 | ProjectPEOWorkTypeId | WORK_TYPE_ID | — | — |
| 94 | ProjectTypeBurdenCostPrjPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 95 | ProjectTypeBurdenCostPrjPEOProjectId | PROJECT_ID | — | — |

### [[pjf_project_statuses_vl|PJF_PROJECT_STATUSES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectStatusPEODescription | DESCRIPTION | — | ✅ |
| 2 | ProjectStatusPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | ProjectStatusPEOProjectStatusCode | PROJECT_STATUS_CODE | — | — |
| 4 | ProjectStatusPEOProjectStatusName | PROJECT_STATUS_NAME | — | ✅ |
| 5 | ProjectStatusPEOProjectSystemStatusCode | PROJECT_SYSTEM_STATUS_CODE | — | ✅ |

### [[pjf_project_types_vl|PJF_PROJECT_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectTypePEOAssetAllocationMethod | ASSET_ALLOCATION_METHOD | — | ✅ |
| 2 | ProjectTypePEOBurdenAccountFlag | BURDEN_ACCOUNT_FLAG | — | — |
| 3 | ProjectTypePEOBurdenAmtDisplayMethod | BURDEN_AMT_DISPLAY_METHOD | — | — |
| 4 | ProjectTypePEOBurdenCostFlag | BURDEN_COST_FLAG | — | ✅ |
| 5 | ProjectTypePEOBurdenCostJournalFlag | BURDEN_COST_JOURNAL_FLAG | — | — |
| 6 | ProjectTypePEOBurdenSumDestProjectId | BURDEN_SUM_DEST_PROJECT_ID | — | — |
| 7 | ProjectTypePEOBurdenSumDestTaskId | BURDEN_SUM_DEST_TASK_ID | — | — |
| 8 | ProjectTypePEOCapitalCostTypeCode | CAPITAL_COST_TYPE_CODE | — | ✅ |
| 9 | ProjectTypePEOCapitalEventProcessing | CAPITAL_EVENT_PROCESSING | — | ✅ |
| 10 | ProjectTypePEOCintRateSchId | CINT_RATE_SCH_ID | — | — |
| 11 | ProjectTypePEOCintSchOverrideFlag | CINT_SCH_OVERRIDE_FLAG | — | ✅ |
| 12 | ProjectTypePEOCipGroupingMethodCode | CIP_GROUPING_METHOD_CODE | — | ✅ |
| 13 | ProjectTypePEOCostIndRateSchId | COST_IND_RATE_SCH_ID | — | — |
| 14 | ProjectTypePEOCostSchOverrideFlag | COST_SCH_OVERRIDE_FLAG | — | ✅ |
| 15 | ProjectTypePEOCreatedBy | CREATED_BY | — | — |
| 16 | ProjectTypePEOCreationDate | CREATION_DATE | — | — |
| 17 | ProjectTypePEODescription | DESCRIPTION | — | ✅ |
| 18 | ProjectTypePEOEnableBillingFlag | ENABLE_BILLING_FLAG | — | ✅ |
| 19 | ProjectTypePEOEnableCapitalizationFlag | ENABLE_CAPITALIZATION_FLAG | — | ✅ |
| 20 | ProjectTypePEOEndDateActive | END_DATE_ACTIVE | — | — |
| 21 | ProjectTypePEOInterfaceAssetCostCode | INTERFACE_ASSET_COST_CODE | — | — |
| 22 | ProjectTypePEOInterfaceCompleteAssetFlag | INTERFACE_COMPLETE_ASSET_FLAG | — | ✅ |
| 23 | ProjectTypePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | ProjectTypePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 25 | ProjectTypePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 26 | ProjectTypePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 27 | ProjectTypePEOOverrideAssetAssignmentFlag | OVERRIDE_ASSET_ASSIGNMENT_FLAG | — | ✅ |
| 28 | ProjectTypePEOProjectType | PROJECT_TYPE | — | ✅ |
| 29 | ProjectTypePEOProjectTypeId | PROJECT_TYPE_ID | — | ✅ |
| 30 | ProjectTypePEOSetId | SET_ID | — | — |
| 31 | ProjectTypePEOSponsoredFlag | SPONSORED_FLAG | — | ✅ |
| 32 | ProjectTypePEOStartDateActive | START_DATE_ACTIVE | — | — |
| 33 | ProjectTypePEOTotalBurdenedJournalFlag | TOTAL_BURDENED_JOURNAL_FLAG | — | — |
| 34 | ProjectTypePEOVendorInvoiceGroupingCode | VENDOR_INVOICE_GROUPING_CODE | — | ✅ |
| 35 | ProjectTypePEOWorkTypeId | WORK_TYPE_ID | — | — |

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
