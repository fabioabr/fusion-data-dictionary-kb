---
id: DOC-OTHER-PVO-ProjectPlanLineForecastPVO
doc_type: system-doc
title: "ProjectPlanLineForecastPVO — PVO Cross-Module"
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
  - ProjectPlanLineForecastPVO
  - projectplanlineforecastpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectPlanLineForecastPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Plan Line Forecast. Acessa as tabelas: CST_COST_BOOKS_B, EGP_CATEGORIES_VL, EGP_SYSTEM_ITEMS_VL (+37).

**Caminho:** `FscmTopModelAM.PjoBudgetsAndForecastsAnalyticsAM.ProjectPlanLineForecastPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 554 | 40 | 1 | 61 | 11% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_books_b|CST_COST_BOOKS_B]] — 2 atributos (1 BICC)
- [[egp_categories_vl|EGP_CATEGORIES_VL]] — 2 atributos
- [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]] — 4 atributos
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 12 atributos
- [[hr_organization_v|HR_ORGANIZATION_V]] — 5 atributos (2 BICC)
- [[per_jobs_f_vl|PER_JOBS_F_VL]] — 4 atributos (2 BICC)
- [[per_persons|PER_PERSONS]] — 8 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 25 atributos (5 BICC)
- [[per_person_types_vl|PER_PERSON_TYPES_VL]] — 4 atributos (1 BICC)
- [[per_roles_dn_vl|PER_ROLES_DN_VL]] — 2 atributos
- [[pjf_event_types_vl|PJF_EVENT_TYPES_VL]] — 2 atributos (1 BICC)
- [[pjf_exp_categories_vl|PJF_EXP_CATEGORIES_VL]] — 2 atributos (1 BICC)
- [[pjf_exp_types_vl|PJF_EXP_TYPES_VL]] — 6 atributos (1 BICC)
- [[pjf_non_labor_res_vl|PJF_NON_LABOR_RES_VL]] — 2 atributos (1 BICC)
- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 8 atributos
- [[pjf_projects_all_tl|PJF_PROJECTS_ALL_TL]] — 11 atributos (1 BICC)
- [[pjf_proj_elements_vl|PJF_PROJ_ELEMENTS_VL]] — 4 atributos
- [[pjf_proj_role_types_vl|PJF_PROJ_ROLE_TYPES_VL]] — 3 atributos
- [[pjf_rate_schedules_vl|PJF_RATE_SCHEDULES_VL]] — 27 atributos
- [[pjf_rbs_elements_vl|PJF_RBS_ELEMENTS_VL]] — 50 atributos (2 BICC)
- [[pjf_rbs_element_map|PJF_RBS_ELEMENT_MAP]] — 2 atributos (1 BICC)
- [[pjf_rbs_element_names_vl|PJF_RBS_ELEMENT_NAMES_VL]] — 2 atributos (1 BICC)
- [[pjf_rbs_versions_vl|PJF_RBS_VERSIONS_VL]] — 5 atributos
- [[pjf_resource_classes_vl|PJF_RESOURCE_CLASSES_VL]] — 2 atributos
- [[pjf_res_formats_vl|PJF_RES_FORMATS_VL]] — 2 atributos
- [[pjf_res_types_vl|PJF_RES_TYPES_VL]] — 2 atributos
- [[pjf_units_of_measure_v|PJF_UNITS_OF_MEASURE_V]] — 6 atributos
- [[pjo_fin_plan_amt_sets|PJO_FIN_PLAN_AMT_SETS]] — 10 atributos
- [[pjo_period_profiles_vl|PJO_PERIOD_PROFILES_VL]] — 2 atributos
- [[pjo_planning_elements|PJO_PLANNING_ELEMENTS]] — 55 atributos (5 BICC)
- [[pjo_planning_options|PJO_PLANNING_OPTIONS]] — 90 atributos (1 BICC)
- [[pjo_plan_lines|PJO_PLAN_LINES]] — 83 atributos (1 PKs, 28 BICC)
- [[pjo_plan_types_b|PJO_PLAN_TYPES_B]] — 22 atributos (1 BICC)
- [[pjo_plan_types_tl|PJO_PLAN_TYPES_TL]] — 11 atributos (1 BICC)
- [[pjo_plan_types_vl|PJO_PLAN_TYPES_VL]] — 4 atributos
- [[pjo_plan_versions_b|PJO_PLAN_VERSIONS_B]] — 48 atributos (2 BICC)
- [[pjo_plan_versions_tl|PJO_PLAN_VERSIONS_TL]] — 11 atributos (1 BICC)
- [[pjo_plan_versions_vl|PJO_PLAN_VERSIONS_VL]] — 6 atributos
- [[pjo_spread_curves_vl|PJO_SPREAD_CURVES_VL]] — 5 atributos (1 BICC)
- [[poz_suppliers|POZ_SUPPLIERS]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[cst_cost_books_b|CST_COST_BOOKS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostBookForRbsElementCostBookCode | COST_BOOK_CODE | — | ✅ |
| 2 | CostBookForRbsElementCostBookId | COST_BOOK_ID | — | — |

### [[egp_categories_vl|EGP_CATEGORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemCategoryForRbsElementCategoryId | CATEGORY_ID | — | — |
| 2 | ItemCategoryForRbsElementCategoryName | CATEGORY_NAME | — | — |

### [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvItemForRbsElementInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 2 | InvItemForRbsElementOrganizationId | ORGANIZATION_ID | — | — |
| 3 | ItemForPlanElemInventoryItemInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 4 | ItemForPlanElemInventoryItemOrganizationId | ORGANIZATION_ID | — | — |

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

### [[hr_organization_v|HR_ORGANIZATION_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgForRbsElementClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | OrgForRbsElementEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | OrgForRbsElementEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | OrgForRbsElementName | NAME | — | ✅ |
| 5 | OrgForRbsElementOrganizationId | ORGANIZATION_ID | — | — |

### [[per_jobs_f_vl|PER_JOBS_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JobForRbsElementEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | JobForRbsElementEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | JobForRbsElementJobId | JOB_ID | — | — |
| 4 | JobForRbsElementName | NAME | — | ✅ |

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
| 1 | PersonForRbsElementEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonForRbsElementEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonForRbsElementFullName | FULL_NAME | — | — |
| 4 | PersonForRbsElementPersonId | PERSON_ID | — | — |
| 5 | PersonForRbsElementPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonNameForBaselinedIdEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | PersonNameForBaselinedIdEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 8 | PersonNameForBaselinedIdFullName | FULL_NAME | — | — |
| 9 | PersonNameForBaselinedIdPersonId | PERSON_ID | — | — |
| 10 | PersonNameForBaselinedIdPersonNameId | PERSON_NAME_ID | — | — |
| 11 | PersonNameForLockedIdEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 12 | PersonNameForLockedIdEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 13 | PersonNameForLockedIdFullName | FULL_NAME | — | — |
| 14 | PersonNameForLockedIdPersonId | PERSON_ID | — | — |
| 15 | PersonNameForLockedIdPersonNameId | PERSON_NAME_ID | — | — |
| 16 | PersonNameForRejectedIdEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 17 | PersonNameForRejectedIdEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 18 | PersonNameForRejectedIdFullName | FULL_NAME | — | — |
| 19 | PersonNameForRejectedIdPersonId | PERSON_ID | — | — |
| 20 | PersonNameForRejectedIdPersonNameId | PERSON_NAME_ID | — | — |
| 21 | PersonNameForSubmittedIdEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 22 | PersonNameForSubmittedIdEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 23 | PersonNameForSubmittedIdFullName | FULL_NAME | — | — |
| 24 | PersonNameForSubmittedIdPersonId | PERSON_ID | — | — |
| 25 | PersonNameForSubmittedIdPersonNameId | PERSON_NAME_ID | — | — |

### [[per_person_types_vl|PER_PERSON_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonTypeForRbsElementPersonTypeId | PERSON_TYPE_ID | — | — |
| 2 | PersonTypeForRbsElementSeededPersonTypeKey | SEEDED_PERSON_TYPE_KEY | — | — |
| 3 | PersonTypeForRbsElementSystemPersonType | SYSTEM_PERSON_TYPE | — | — |
| 4 | PersonTypeForRbsElementUserPersonType | USER_PERSON_TYPE | — | ✅ |

### [[per_roles_dn_vl|PER_ROLES_DN_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RoleForRbsElementRoleId | ROLE_ID | — | — |
| 2 | RoleForRbsElementRoleName | ROLE_NAME | — | — |

### [[pjf_event_types_vl|PJF_EVENT_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EvtTypeForRbsElementEventTypeId | EVENT_TYPE_ID | — | — |
| 2 | EvtTypeForRbsElementEventTypeName | EVENT_TYPE_NAME | — | ✅ |

### [[pjf_exp_categories_vl|PJF_EXP_CATEGORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpCatForRbsElementExpenditureCategoryId | EXPENDITURE_CATEGORY_ID | — | — |
| 2 | ExpCatForRbsElementExpenditureCategoryName | EXPENDITURE_CATEGORY_NAME | — | ✅ |

### [[pjf_exp_types_vl|PJF_EXP_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpTypeForRbsElementExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 2 | ExpTypeForRbsElementExpenditureTypeName | EXPENDITURE_TYPE_NAME | — | ✅ |
| 3 | RateExpTypeForPlanElementDescription | DESCRIPTION | — | — |
| 4 | RateExpTypeForPlanElementExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 5 | RateExpTypeForPlanElementExpenditureTypeName | EXPENDITURE_TYPE_NAME | — | — |
| 6 | RateExpTypeForPlanElementObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[pjf_non_labor_res_vl|PJF_NON_LABOR_RES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NonLbrResForRbsElementNlrName | NLR_NAME | — | ✅ |
| 2 | NonLbrResForRbsElementNonLaborResourceId | NON_LABOR_RESOURCE_ID | — | — |

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
| 8 | ProjectBasePEOSegment1 | SEGMENT1 | — | — |

### [[pjf_projects_all_tl|PJF_PROJECTS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | ProjectTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | ProjectTranslationPEODescription | DESCRIPTION | — | — |
| 4 | ProjectTranslationPEOLanguage | LANGUAGE | — | — |
| 5 | ProjectTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ProjectTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ProjectTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ProjectTranslationPEOName | NAME | — | — |
| 9 | ProjectTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ProjectTranslationPEOProjectId | PROJECT_ID | — | — |
| 11 | ProjectTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[pjf_proj_elements_vl|PJF_PROJ_ELEMENTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskStructureForPlanElementDescription | DESCRIPTION | — | — |
| 2 | TaskStructureForPlanElementName | NAME | — | — |
| 3 | TaskStructureForPlanElementProjElementId | PROJ_ELEMENT_ID | — | — |
| 4 | TaskStructureForPlanElementType | ELEMENT_TYPE | — | — |

### [[pjf_proj_role_types_vl|PJF_PROJ_ROLE_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RoleTypeForPlanElementDescription | DESCRIPTION | — | — |
| 2 | RoleTypeForPlanElementProjectRoleId | PROJECT_ROLE_ID | — | — |
| 3 | RoleTypeForPlanElementProjectRoleName | PROJECT_ROLE_NAME | — | — |

### [[pjf_rate_schedules_vl|PJF_RATE_SCHEDULES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillRateSchedulesForPlanLineDescription | DESCRIPTION | — | — |
| 2 | BillRateSchedulesForPlanLineRateScheduleId | RATE_SCHEDULE_ID | — | — |
| 3 | BillRateSchedulesForPlanLineRateScheduleName | RATE_SCHEDULE_NAME | — | — |
| 4 | CostBrdnRateSchForPlanOptionRateScheduleId | RATE_SCHEDULE_ID | — | — |
| 5 | CostBrdnRateSchForPlanOptionRateScheduleName | RATE_SCHEDULE_NAME | — | — |
| 6 | CostEmpRateSchForPlanOptionRateScheduleId | RATE_SCHEDULE_ID | — | — |
| 7 | CostEmpRateSchForPlanOptionRateScheduleName | RATE_SCHEDULE_NAME | — | — |
| 8 | CostJobRateSchForPlanOptionRateScheduleId | RATE_SCHEDULE_ID | — | — |
| 9 | CostJobRateSchForPlanOptionRateScheduleName | RATE_SCHEDULE_NAME | — | — |
| 10 | CostNonLbrRateSchForPlanOptnRateScheduleId | RATE_SCHEDULE_ID | — | — |
| 11 | CostNonLbrRateSchForPlanOptnRateScheduleName | RATE_SCHEDULE_NAME | — | — |
| 12 | CostRateSchedulesForPlanLineDescription | DESCRIPTION | — | — |
| 13 | CostRateSchedulesForPlanLineRateScheduleId | RATE_SCHEDULE_ID | — | — |
| 14 | CostRateSchedulesForPlanLineRateScheduleName | RATE_SCHEDULE_NAME | — | — |
| 15 | IndRateSchedulesForPlanLineDescription | DESCRIPTION | — | — |
| 16 | IndRateSchedulesForPlanLineRateScheduleId | RATE_SCHEDULE_ID | — | — |
| 17 | IndRateSchedulesForPlanLineRateScheduleName | RATE_SCHEDULE_NAME | — | — |
| 18 | ResClassRawCostForPlanOptnRateScheduleId | RATE_SCHEDULE_ID | — | — |
| 19 | ResClassRawCostForPlanOptnRateScheduleName | RATE_SCHEDULE_NAME | — | — |
| 20 | ResClsBillRateSchForPlanOptnRateScheduleId | RATE_SCHEDULE_ID | — | — |
| 21 | ResClsBillRateSchForPlanOptnRateScheduleName | RATE_SCHEDULE_NAME | — | — |
| 22 | RevEmpRateSchForPlanOptionRateScheduleId | RATE_SCHEDULE_ID | — | — |
| 23 | RevEmpRateSchForPlanOptionRateScheduleName | RATE_SCHEDULE_NAME | — | — |
| 24 | RevJobRateSchForPlanOptionRateScheduleId | RATE_SCHEDULE_ID | — | — |
| 25 | RevJobRateSchForPlanOptionRateScheduleName | RATE_SCHEDULE_NAME | — | — |
| 26 | RevNonLbrResSchForPlanOptionRateScheduleId | RATE_SCHEDULE_ID | — | — |
| 27 | RevNonLbrResSchForPlanOptionRateScheduleName | RATE_SCHEDULE_NAME | — | — |

### [[pjf_rbs_elements_vl|PJF_RBS_ELEMENTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ParentElementForRbsElementAlias | ALIAS | — | — |
| 2 | ParentElementForRbsElementRbsElementId | RBS_ELEMENT_ID | — | — |
| 3 | RbsElementPEOAlias | ALIAS | — | — |
| 4 | RbsElementPEOBomEquipmentId | BOM_EQUIPMENT_ID | — | — |
| 5 | RbsElementPEOBomLaborId | BOM_LABOR_ID | — | — |
| 6 | RbsElementPEOCreatedBy | CREATED_BY | — | — |
| 7 | RbsElementPEOCreationDate | CREATION_DATE | — | — |
| 8 | RbsElementPEOElementIdentifier | ELEMENT_IDENTIFIER | — | — |
| 9 | RbsElementPEOEnabledFlag | ENABLED_FLAG | — | — |
| 10 | RbsElementPEOEventTypeId | EVENT_TYPE_ID | — | — |
| 11 | RbsElementPEOExpenditureCategoryId | EXPENDITURE_CATEGORY_ID | — | — |
| 12 | RbsElementPEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 13 | RbsElementPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 14 | RbsElementPEOItemCategoryId | ITEM_CATEGORY_ID | — | — |
| 15 | RbsElementPEOJobId | JOB_ID | — | — |
| 16 | RbsElementPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | RbsElementPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | RbsElementPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | RbsElementPEOLeafNodeFlag | LEAF_NODE_FLAG | — | — |
| 20 | RbsElementPEOMarkedFor | MARKED_FOR | — | — |
| 21 | RbsElementPEOMfcCostTypeId | MFC_COST_TYPE_ID | — | — |
| 22 | RbsElementPEONonLaborResourceId | NON_LABOR_RESOURCE_ID | — | — |
| 23 | RbsElementPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 24 | RbsElementPEOOrderNumber | ORDER_NUMBER | — | — |
| 25 | RbsElementPEOOrganizationId | ORGANIZATION_ID | — | — |
| 26 | RbsElementPEOOutlineNumber | OUTLINE_NUMBER | — | — |
| 27 | RbsElementPEOParentElementId | PARENT_ELEMENT_ID | — | — |
| 28 | RbsElementPEOPersonId | PERSON_ID | — | — |
| 29 | RbsElementPEOPersonTypeId | PERSON_TYPE_ID | — | — |
| 30 | RbsElementPEORbsElementId | RBS_ELEMENT_ID | — | — |
| 31 | RbsElementPEORbsElementNameId | RBS_ELEMENT_NAME_ID | — | — |
| 32 | RbsElementPEORbsLevel | RBS_LEVEL | — | — |
| 33 | RbsElementPEORbsVersionId | RBS_VERSION_ID | — | — |
| 34 | RbsElementPEOResFormatId | RES_FORMAT_ID | — | — |
| 35 | RbsElementPEOResourceClassCode | RESOURCE_CLASS_CODE | — | — |
| 36 | RbsElementPEOResourceClassId | RESOURCE_CLASS_ID | — | — |
| 37 | RbsElementPEOResourceSourceId | RESOURCE_SOURCE_ID | — | — |
| 38 | RbsElementPEOResourceTypeId | RESOURCE_TYPE_ID | — | — |
| 39 | RbsElementPEORevenueCategoryId | REVENUE_CATEGORY_ID | — | — |
| 40 | RbsElementPEORoleId | ROLE_ID | — | — |
| 41 | RbsElementPEORuleFlag | RULE_FLAG | — | — |
| 42 | RbsElementPEOSpreadCurveId | SPREAD_CURVE_ID | — | — |
| 43 | RbsElementPEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 44 | RbsElementPEOUserCreatedFlag | USER_CREATED_FLAG | — | — |
| 45 | RbsElementPEOUserDefinedCustom1Id | USER_DEFINED_CUSTOM1_ID | — | — |
| 46 | RbsElementPEOUserDefinedCustom2Id | USER_DEFINED_CUSTOM2_ID | — | — |
| 47 | RbsElementPEOUserDefinedCustom3Id | USER_DEFINED_CUSTOM3_ID | — | — |
| 48 | RbsElementPEOUserDefinedCustom4Id | USER_DEFINED_CUSTOM4_ID | — | — |
| 49 | RbsElementPEOUserDefinedCustom5Id | USER_DEFINED_CUSTOM5_ID | — | — |
| 50 | RbsElementPEOVendorId | VENDOR_ID | — | — |

### [[pjf_rbs_element_map|PJF_RBS_ELEMENT_MAP]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RevCategoryForRbsElementResourceId | RESOURCE_ID | — | — |
| 2 | RevCategoryForRbsElementResourceName | RESOURCE_NAME | — | ✅ |

### [[pjf_rbs_element_names_vl|PJF_RBS_ELEMENT_NAMES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RbsNameForRbsElementName | NAME | — | ✅ |
| 2 | RbsNameForRbsElementRbsElementNameId | RBS_ELEMENT_NAME_ID | — | — |

### [[pjf_rbs_versions_vl|PJF_RBS_VERSIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RbsVersionForPlanOptionDescription | DESCRIPTION | — | — |
| 2 | RbsVersionForPlanOptionName | NAME | — | — |
| 3 | RbsVersionForPlanOptionRbsVersionId | RBS_VERSION_ID | — | — |
| 4 | RbsVersionForRbsElementName | NAME | — | — |
| 5 | RbsVersionForRbsElementRbsVersionId | RBS_VERSION_ID | — | — |

### [[pjf_resource_classes_vl|PJF_RESOURCE_CLASSES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResourceClassForRbsElementName | NAME | — | — |
| 2 | ResourceClassForRbsElementResourceClassId | RESOURCE_CLASS_ID | — | — |

### [[pjf_res_formats_vl|PJF_RES_FORMATS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResourceFormatForRbsElementName | NAME | — | — |
| 2 | ResourceFormatForRbsElementResFormatId | RES_FORMAT_ID | — | — |

### [[pjf_res_types_vl|PJF_RES_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResourceTypeForRbsElementName | NAME | — | — |
| 2 | ResourceTypeForRbsElementResTypeId | RES_TYPE_ID | — | — |

### [[pjf_units_of_measure_v|PJF_UNITS_OF_MEASURE_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UnitOfMeasureForPlanElemDescription | DESCRIPTION | — | — |
| 2 | UnitOfMeasureForPlanElemUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 3 | UnitOfMeasureForPlanElemUomCode | UOM_CODE | — | — |
| 4 | UnitOfMeasureForRbsElementDescription | DESCRIPTION | — | — |
| 5 | UnitOfMeasureForRbsElementUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 6 | UnitOfMeasureForRbsElementUomCode | UOM_CODE | — | — |

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

### [[pjo_period_profiles_vl|PJO_PERIOD_PROFILES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PeriodProfileForPlanOptionName | NAME | — | — |
| 2 | PeriodProfileForPlanOptionPeriodProfileId | PERIOD_PROFILE_ID | — | — |

### [[pjo_planning_elements|PJO_PLANNING_ELEMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlanningElementPEOAssignmentDescription | ASSIGNMENT_DESCRIPTION | — | — |
| 2 | PlanningElementPEOCreatedBy | CREATED_BY | — | — |
| 3 | PlanningElementPEOCreationDate | CREATION_DATE | — | — |
| 4 | PlanningElementPEOEtcMethodCode | ETC_METHOD_CODE | — | — |
| 5 | PlanningElementPEOEventTypeId | EVENT_TYPE_ID | — | — |
| 6 | PlanningElementPEOExpenditureCategoryId | EXPENDITURE_CATEGORY_ID | — | — |
| 7 | PlanningElementPEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 8 | PlanningElementPEOFcResTypeCode | FC_RES_TYPE_CODE | — | — |
| 9 | PlanningElementPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 10 | PlanningElementPEOItemCategoryId | ITEM_CATEGORY_ID | — | — |
| 11 | PlanningElementPEOJobId | JOB_ID | — | — |
| 12 | PlanningElementPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | PlanningElementPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | PlanningElementPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | PlanningElementPEOMfcCostTypeId | MFC_COST_TYPE_ID | — | — |
| 16 | PlanningElementPEONonLaborResourceId | NON_LABOR_RESOURCE_ID | — | — |
| 17 | PlanningElementPEOObjectChildId1 | OBJECT_CHILD_ID1 | — | — |
| 18 | PlanningElementPEOObjectChildId2 | OBJECT_CHILD_ID2 | — | — |
| 19 | PlanningElementPEOObjectChildId3 | OBJECT_CHILD_ID3 | — | — |
| 20 | PlanningElementPEOObjectId1 | OBJECT_ID1 | — | — |
| 21 | PlanningElementPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | PlanningElementPEOOrganizationId | ORGANIZATION_ID | — | — |
| 23 | PlanningElementPEOParentElementId | PARENT_ELEMENT_ID | — | — |
| 24 | PlanningElementPEOPersonId | PERSON_ID | — | — |
| 25 | PlanningElementPEOPersonTypeId | PERSON_TYPE_ID | — | — |
| 26 | PlanningElementPEOPlanVersionId | PLAN_VERSION_ID | — | — |
| 27 | PlanningElementPEOPlanningElementId | PLANNING_ELEMENT_ID | — | — |
| 28 | PlanningElementPEOPlanningEndDate | PLANNING_END_DATE | — | ✅ |
| 29 | PlanningElementPEOPlanningStartDate | PLANNING_START_DATE | — | ✅ |
| 30 | PlanningElementPEOPmProductCode | PM_PRODUCT_CODE | — | — |
| 31 | PlanningElementPEOPmResAsgnReference | PM_RES_ASGN_REFERENCE | — | — |
| 32 | PlanningElementPEOProcureResourceFlag | PROCURE_RESOURCE_FLAG | — | — |
| 33 | PlanningElementPEOProgressEtcMethodCode | PROGRESS_ETC_METHOD_CODE | — | — |
| 34 | PlanningElementPEOProjElementVersionId | PROJ_ELEMENT_VERSION_ID | — | — |
| 35 | PlanningElementPEOProjectId | PROJECT_ID | — | — |
| 36 | PlanningElementPEOProjectRoleId | PROJECT_ROLE_ID | — | — |
| 37 | PlanningElementPEORaTaskDatesSame | RA_TASK_DATES_SAME | — | — |
| 38 | PlanningElementPEORateBasedFlag | RATE_BASED_FLAG | — | ✅ |
| 39 | PlanningElementPEORateExpFuncCurrCode | RATE_EXP_FUNC_CURR_CODE | — | — |
| 40 | PlanningElementPEORateExpenditureOrgId | RATE_EXPENDITURE_ORG_ID | — | — |
| 41 | PlanningElementPEORateExpenditureTypeId | RATE_EXPENDITURE_TYPE_ID | — | — |
| 42 | PlanningElementPEORbsElementId | RBS_ELEMENT_ID | — | — |
| 43 | PlanningElementPEOResTypeCode | RES_TYPE_CODE | — | — |
| 44 | PlanningElementPEOResourceClassCode | RESOURCE_CLASS_CODE | — | — |
| 45 | PlanningElementPEOResourceClassFlag | RESOURCE_CLASS_FLAG | — | — |
| 46 | PlanningElementPEORevenueCategoryId | REVENUE_CATEGORY_ID | — | — |
| 47 | PlanningElementPEOScheduledDelay | SCHEDULED_DELAY | — | — |
| 48 | PlanningElementPEOSpFixedDate | SP_FIXED_DATE | — | — |
| 49 | PlanningElementPEOSpreadCurveId | SPREAD_CURVE_ID | — | — |
| 50 | PlanningElementPEOSupplierId | SUPPLIER_ID | — | — |
| 51 | PlanningElementPEOTaskId | TASK_ID | — | — |
| 52 | PlanningElementPEOTransactionSourceCode | TRANSACTION_SOURCE_CODE | — | — |
| 53 | PlanningElementPEOTxnAccumHeaderId | TXN_ACCUM_HEADER_ID | — | — |
| 54 | PlanningElementPEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 55 | PlanningElementPEOUnplannedFlag | UNPLANNED_FLAG | — | — |

### [[pjo_planning_options|PJO_PLANNING_OPTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlanningOptionPEOAllowFcstAmtCarryFlag | ALLOW_FCST_AMT_CARRY_FLAG | — | — |
| 2 | PlanningOptionPEOAllowNegEtcFlag | ALLOW_NEG_ETC_FLAG | — | — |
| 3 | PlanningOptionPEOAmountSetId | AMOUNT_SET_ID | — | — |
| 4 | PlanningOptionPEOAmountType | AMOUNT_TYPE | — | — |
| 5 | PlanningOptionPEOApprovedCostPlanTypeFlag | APPROVED_COST_PLAN_TYPE_FLAG | — | — |
| 6 | PlanningOptionPEOApprovedRevPlanTypeFlag | APPROVED_REV_PLAN_TYPE_FLAG | — | — |
| 7 | PlanningOptionPEOAutoApproveFlag | AUTO_APPROVE_FLAG | — | — |
| 8 | PlanningOptionPEOAutoBdgtBaseline | AUTO_BDGT_BASELINE | — | — |
| 9 | PlanningOptionPEOAutoRollupTaskDate | AUTO_ROLLUP_TASK_DATE | — | — |
| 10 | PlanningOptionPEOBudgetCreationMethod | BUDGET_CREATION_METHOD | — | — |
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
| 22 | PlanningOptionPEOCurrentPlanningPeriod | CURRENT_PLANNING_PERIOD | — | — |
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
| 41 | PlanningOptionPEOMarginDerivedFromCode | MARGIN_DERIVED_FROM_CODE | — | — |
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
| 62 | PlanningOptionPEOPlanInMultiCurrFlag | PLAN_IN_MULTI_CURR_FLAG | — | — |
| 63 | PlanningOptionPEOPlanLevelCode | PLAN_LEVEL_CODE | — | — |
| 64 | PlanningOptionPEOPlanOptionLevelCode | PLAN_OPTION_LEVEL_CODE | — | — |
| 65 | PlanningOptionPEOPlanTypeCode | PLAN_TYPE_CODE | — | — |
| 66 | PlanningOptionPEOPlanTypeId | PLAN_TYPE_ID | — | — |
| 67 | PlanningOptionPEOPlanVersionId | PLAN_VERSION_ID | — | — |
| 68 | PlanningOptionPEOPlannedForCode | PLANNED_FOR_CODE | — | — |
| 69 | PlanningOptionPEOPlanningOptionId | PLANNING_OPTION_ID | — | — |
| 70 | PlanningOptionPEOPrimaryCostForecastFlag | PRIMARY_COST_FORECAST_FLAG | — | — |
| 71 | PlanningOptionPEOPrimaryRevForecastFlag | PRIMARY_REV_FORECAST_FLAG | — | — |
| 72 | PlanningOptionPEOProjectId | PROJECT_ID | — | — |
| 73 | PlanningOptionPEORaPlanTypeId | RA_PLAN_TYPE_ID | — | — |
| 74 | PlanningOptionPEORaTaskDatesSame | RA_TASK_DATES_SAME | — | — |
| 75 | PlanningOptionPEORbsVersionId | RBS_VERSION_ID | — | — |
| 76 | PlanningOptionPEOResClassBillRateSchId | RES_CLASS_BILL_RATE_SCH_ID | — | — |
| 77 | PlanningOptionPEOResClassRawCostSchId | RES_CLASS_RAW_COST_SCH_ID | — | — |
| 78 | PlanningOptionPEORevClassificationMethod | REV_CLASSIFICATION_METHOD | — | — |
| 79 | PlanningOptionPEORevEmpRateSchId | REV_EMP_RATE_SCH_ID | — | — |
| 80 | PlanningOptionPEORevJobRateSchId | REV_JOB_RATE_SCH_ID | — | — |
| 81 | PlanningOptionPEORevNonLbrResRateSchId | REV_NON_LBR_RES_RATE_SCH_ID | — | — |
| 82 | PlanningOptionPEOSpecPcCostAtProjLevel | SPEC_PC_COST_AT_PROJ_LEVEL | — | — |
| 83 | PlanningOptionPEOSpecPcRevAtProjLevel | SPEC_PC_REV_AT_PROJ_LEVEL | — | — |
| 84 | PlanningOptionPEOSpecPfcCostAtProjLevel | SPEC_PFC_COST_AT_PROJ_LEVEL | — | — |
| 85 | PlanningOptionPEOSpecPfcRevAtProjLevel | SPEC_PFC_REV_AT_PROJ_LEVEL | — | — |
| 86 | PlanningOptionPEOSyncTaskTxnPlanDates | SYNC_TASK_TXN_PLAN_DATES | — | — |
| 87 | PlanningOptionPEOSyncTxnDateBuffer | SYNC_TXN_DATE_BUFFER | — | — |
| 88 | PlanningOptionPEOTimePhasedCode | TIME_PHASED_CODE | — | — |
| 89 | PlanningOptionPEOUsePlanningRatesFlag | USE_PLANNING_RATES_FLAG | — | — |
| 90 | PlanningOptionPEOUseThirdPartySoftware | USE_THIRD_PARTY_SOFTWARE | — | — |

### [[pjo_plan_lines|PJO_PLAN_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlanLineId | PLAN_LINE_ID | 🔑 | ✅ |
| 2 | PlanLinePEOBillRateScheduleId | BILL_RATE_SCHEDULE_ID | — | — |
| 3 | PlanLinePEOCostRateScheduleId | COST_RATE_SCHEDULE_ID | — | — |
| 4 | PlanLinePEOCreatedBy | CREATED_BY | — | — |
| 5 | PlanLinePEOCreationDate | CREATION_DATE | — | — |
| 6 | PlanLinePEOIndRateScheduleId | IND_RATE_SCHEDULE_ID | — | — |
| 7 | PlanLinePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PlanLinePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | PlanLinePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | PlanLinePEOMultiErrorFlag | MULTI_ERROR_FLAG | — | — |
| 11 | PlanLinePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | PlanLinePEOPlanVersionId | PLAN_VERSION_ID | — | — |
| 13 | PlanLinePEOPlanningElementId | PLANNING_ELEMENT_ID | — | — |
| 14 | PlanLinePEOTcAverageBillRate | TC_AVERAGE_BILL_RATE | — | — |
| 15 | PlanLinePEOTcAverageBrdndCostRate | TC_AVERAGE_BRDND_COST_RATE | — | — |
| 16 | PlanLinePEOTcAverageRawCostRate | TC_AVERAGE_RAW_COST_RATE | — | — |
| 17 | PlanLinePEOTcAvgStdBillRate | TC_AVG_STD_BILL_RATE | — | ✅ |
| 18 | PlanLinePEOTcAvgStdBrdndCostRate | TC_AVG_STD_BRDND_COST_RATE | — | ✅ |
| 19 | PlanLinePEOTcAvgStdBrdndMultiplier | TC_AVG_STD_BRDND_MULTIPLIER | — | — |
| 20 | PlanLinePEOTcAvgStdRawCostRate | TC_AVG_STD_RAW_COST_RATE | — | ✅ |
| 21 | PlanLinePEOTcBillRateOverride | TC_BILL_RATE_OVERRIDE | — | ✅ |
| 22 | PlanLinePEOTcBrdndCostRateOverride | TC_BRDND_COST_RATE_OVERRIDE | — | ✅ |
| 23 | PlanLinePEOTcEtcBillRate | TC_ETC_BILL_RATE | — | — |
| 24 | PlanLinePEOTcEtcBrdndCostRate | TC_ETC_BRDND_COST_RATE | — | — |
| 25 | PlanLinePEOTcEtcRawCostRate | TC_ETC_RAW_COST_RATE | — | — |
| 26 | PlanLinePEOTcMarkupPercent | TC_MARKUP_PERCENT | — | — |
| 27 | PlanLinePEOTcRawCostRateOverride | TC_RAW_COST_RATE_OVERRIDE | — | ✅ |
| 28 | PlanLinePEOTotalActQuantity | TOTAL_ACT_QUANTITY | — | ✅ |
| 29 | PlanLinePEOTotalExtQuantity | TOTAL_EXT_QUANTITY | — | — |
| 30 | PlanLinePEOTotalPcActBrdndCost | TOTAL_PC_ACT_BRDND_COST | — | ✅ |
| 31 | PlanLinePEOTotalPcActRawCost | TOTAL_PC_ACT_RAW_COST | — | ✅ |
| 32 | PlanLinePEOTotalPcActRevenue | TOTAL_PC_ACT_REVENUE | — | ✅ |
| 33 | PlanLinePEOTotalPcBrdndCost | TOTAL_PC_BRDND_COST | — | ✅ |
| 34 | PlanLinePEOTotalPcExtBrdndCost | TOTAL_PC_EXT_BRDND_COST | — | — |
| 35 | PlanLinePEOTotalPcExtRawCost | TOTAL_PC_EXT_RAW_COST | — | — |
| 36 | PlanLinePEOTotalPcPoBrdndCost | TOTAL_PC_PO_BRDND_COST | — | — |
| 37 | PlanLinePEOTotalPcPoRawCost | TOTAL_PC_PO_RAW_COST | — | — |
| 38 | PlanLinePEOTotalPcRawCost | TOTAL_PC_RAW_COST | — | ✅ |
| 39 | PlanLinePEOTotalPcReqBrdndCost | TOTAL_PC_REQ_BRDND_COST | — | — |
| 40 | PlanLinePEOTotalPcReqRawCost | TOTAL_PC_REQ_RAW_COST | — | — |
| 41 | PlanLinePEOTotalPcRevenue | TOTAL_PC_REVENUE | — | ✅ |
| 42 | PlanLinePEOTotalPcSiBrdndCost | TOTAL_PC_SI_BRDND_COST | — | — |
| 43 | PlanLinePEOTotalPcSiRawCost | TOTAL_PC_SI_RAW_COST | — | — |
| 44 | PlanLinePEOTotalPcToBrdndCost | TOTAL_PC_TO_BRDND_COST | — | — |
| 45 | PlanLinePEOTotalPcToRawCost | TOTAL_PC_TO_RAW_COST | — | — |
| 46 | PlanLinePEOTotalPfcActBrdndCost | TOTAL_PFC_ACT_BRDND_COST | — | ✅ |
| 47 | PlanLinePEOTotalPfcActRawCost | TOTAL_PFC_ACT_RAW_COST | — | ✅ |
| 48 | PlanLinePEOTotalPfcActRevenue | TOTAL_PFC_ACT_REVENUE | — | ✅ |
| 49 | PlanLinePEOTotalPfcBrdndCost | TOTAL_PFC_BRDND_COST | — | ✅ |
| 50 | PlanLinePEOTotalPfcExtBrdndCost | TOTAL_PFC_EXT_BRDND_COST | — | — |
| 51 | PlanLinePEOTotalPfcExtRawCost | TOTAL_PFC_EXT_RAW_COST | — | — |
| 52 | PlanLinePEOTotalPfcPoBrdndCost | TOTAL_PFC_PO_BRDND_COST | — | — |
| 53 | PlanLinePEOTotalPfcPoRawCost | TOTAL_PFC_PO_RAW_COST | — | — |
| 54 | PlanLinePEOTotalPfcRawCost | TOTAL_PFC_RAW_COST | — | ✅ |
| 55 | PlanLinePEOTotalPfcReqBrdndCost | TOTAL_PFC_REQ_BRDND_COST | — | — |
| 56 | PlanLinePEOTotalPfcReqRawCost | TOTAL_PFC_REQ_RAW_COST | — | — |
| 57 | PlanLinePEOTotalPfcRevenue | TOTAL_PFC_REVENUE | — | ✅ |
| 58 | PlanLinePEOTotalPfcSiBrdndCost | TOTAL_PFC_SI_BRDND_COST | — | — |
| 59 | PlanLinePEOTotalPfcSiRawCost | TOTAL_PFC_SI_RAW_COST | — | — |
| 60 | PlanLinePEOTotalPfcToBrdndCost | TOTAL_PFC_TO_BRDND_COST | — | — |
| 61 | PlanLinePEOTotalPfcToRawCost | TOTAL_PFC_TO_RAW_COST | — | — |
| 62 | PlanLinePEOTotalPoQuantity | TOTAL_PO_QUANTITY | — | — |
| 63 | PlanLinePEOTotalQuantity | TOTAL_QUANTITY | — | ✅ |
| 64 | PlanLinePEOTotalReqQuantity | TOTAL_REQ_QUANTITY | — | — |
| 65 | PlanLinePEOTotalSiQuantity | TOTAL_SI_QUANTITY | — | — |
| 66 | PlanLinePEOTotalTcActBrdndCost | TOTAL_TC_ACT_BRDND_COST | — | ✅ |
| 67 | PlanLinePEOTotalTcActRawCost | TOTAL_TC_ACT_RAW_COST | — | ✅ |
| 68 | PlanLinePEOTotalTcActRevenue | TOTAL_TC_ACT_REVENUE | — | ✅ |
| 69 | PlanLinePEOTotalTcBrdndCost | TOTAL_TC_BRDND_COST | — | ✅ |
| 70 | PlanLinePEOTotalTcExtBrdndCost | TOTAL_TC_EXT_BRDND_COST | — | — |
| 71 | PlanLinePEOTotalTcExtRawCost | TOTAL_TC_EXT_RAW_COST | — | — |
| 72 | PlanLinePEOTotalTcPoBrdndCost | TOTAL_TC_PO_BRDND_COST | — | — |
| 73 | PlanLinePEOTotalTcPoRawCost | TOTAL_TC_PO_RAW_COST | — | — |
| 74 | PlanLinePEOTotalTcRawCost | TOTAL_TC_RAW_COST | — | ✅ |
| 75 | PlanLinePEOTotalTcReqBrdndCost | TOTAL_TC_REQ_BRDND_COST | — | — |
| 76 | PlanLinePEOTotalTcReqRawCost | TOTAL_TC_REQ_RAW_COST | — | — |
| 77 | PlanLinePEOTotalTcRevenue | TOTAL_TC_REVENUE | — | ✅ |
| 78 | PlanLinePEOTotalTcSiBrdndCost | TOTAL_TC_SI_BRDND_COST | — | — |
| 79 | PlanLinePEOTotalTcSiRawCost | TOTAL_TC_SI_RAW_COST | — | — |
| 80 | PlanLinePEOTotalTcToBrdndCost | TOTAL_TC_TO_BRDND_COST | — | — |
| 81 | PlanLinePEOTotalTcToRawCost | TOTAL_TC_TO_RAW_COST | — | — |
| 82 | PlanLinePEOTotalToQuantity | TOTAL_TO_QUANTITY | — | — |
| 83 | PlanLinePEOTxnCurrencyCode | TXN_CURRENCY_CODE | — | — |

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
| 9 | PlanTypeBasePEOEndDate | END_DATE | — | — |
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
| 22 | PlanTypeBasePEOStartDate | START_DATE | — | — |

### [[pjo_plan_types_tl|PJO_PLAN_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlanTypeTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | PlanTypeTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | PlanTypeTranslationPEODescription | DESCRIPTION | — | — |
| 4 | PlanTypeTranslationPEOLanguage | LANGUAGE | — | — |
| 5 | PlanTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PlanTypeTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | PlanTypeTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | PlanTypeTranslationPEOName | NAME | — | — |
| 9 | PlanTypeTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | PlanTypeTranslationPEOPlanTypeId | PLAN_TYPE_ID | — | — |
| 11 | PlanTypeTranslationPEOSourceLang | SOURCE_LANG | — | — |

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
| 3 | PlanVersionBasePEOBaselinedDate | BASELINED_DATE | — | — |
| 4 | PlanVersionBasePEOCreatedBy | CREATED_BY | — | — |
| 5 | PlanVersionBasePEOCreationDate | CREATION_DATE | — | — |
| 6 | PlanVersionBasePEOCurrentPlanStatusFlag | CURRENT_PLAN_STATUS_FLAG | — | — |
| 7 | PlanVersionBasePEOEquipmentQuantity | EQUIPMENT_QUANTITY | — | — |
| 8 | PlanVersionBasePEOEtcStartDate | ETC_START_DATE | — | — |
| 9 | PlanVersionBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 10 | PlanVersionBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 11 | PlanVersionBasePEOLastAmtGenDate | LAST_AMT_GEN_DATE | — | — |
| 12 | PlanVersionBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | PlanVersionBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | PlanVersionBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | PlanVersionBasePEOLockedByPersonId | LOCKED_BY_PERSON_ID | — | — |
| 16 | PlanVersionBasePEOMultiErrorFlag | MULTI_ERROR_FLAG | — | — |
| 17 | PlanVersionBasePEOObjectId1 | OBJECT_ID1 | — | — |
| 18 | PlanVersionBasePEOObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 19 | PlanVersionBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | PlanVersionBasePEOOriginalFlag | ORIGINAL_FLAG | — | — |
| 21 | PlanVersionBasePEOPeopleQuantity | PEOPLE_QUANTITY | — | — |
| 22 | PlanVersionBasePEOPfcBrdndCost | PFC_BRDND_COST | — | — |
| 23 | PlanVersionBasePEOPfcRawCost | PFC_RAW_COST | — | — |
| 24 | PlanVersionBasePEOPfcRevenue | PFC_REVENUE | — | — |
| 25 | PlanVersionBasePEOPjiSummarizedFlag | PJI_SUMMARIZED_FLAG | — | — |
| 26 | PlanVersionBasePEOPjsSummaryId | PJS_SUMMARY_ID | — | — |
| 27 | PlanVersionBasePEOPlanClassCode | PLAN_CLASS_CODE | — | — |
| 28 | PlanVersionBasePEOPlanProcessStatusCode | PLAN_PROCESS_STATUS_CODE | — | — |
| 29 | PlanVersionBasePEOPlanProcessingCode | PLAN_PROCESSING_CODE | — | — |
| 30 | PlanVersionBasePEOPlanRunDate | PLAN_RUN_DATE | — | — |
| 31 | PlanVersionBasePEOPlanStatusCode | PLAN_STATUS_CODE | — | — |
| 32 | PlanVersionBasePEOPlanTypeId | PLAN_TYPE_ID | — | — |
| 33 | PlanVersionBasePEOPlanVersionId | PLAN_VERSION_ID | — | ✅ |
| 34 | PlanVersionBasePEOPlannedForCode | PLANNED_FOR_CODE | — | — |
| 35 | PlanVersionBasePEOPmBudgetReference | PM_BUDGET_REFERENCE | — | — |
| 36 | PlanVersionBasePEOPmProductCode | PM_PRODUCT_CODE | — | — |
| 37 | PlanVersionBasePEOProjectId | PROJECT_ID | — | — |
| 38 | PlanVersionBasePEORejectedBy | REJECTED_BY | — | — |
| 39 | PlanVersionBasePEORejectionDate | REJECTION_DATE | — | — |
| 40 | PlanVersionBasePEORequestId | REQUEST_ID | — | — |
| 41 | PlanVersionBasePEOStructureVersionId | STRUCTURE_VERSION_ID | — | — |
| 42 | PlanVersionBasePEOSubmittedBy | SUBMITTED_BY | — | — |
| 43 | PlanVersionBasePEOSubmittedDate | SUBMITTED_DATE | — | — |
| 44 | PlanVersionBasePEOTotalPcBrdndCost | TOTAL_PC_BRDND_COST | — | — |
| 45 | PlanVersionBasePEOTotalPcRawCost | TOTAL_PC_RAW_COST | — | — |
| 46 | PlanVersionBasePEOTotalPcRevenue | TOTAL_PC_REVENUE | — | — |
| 47 | PlanVersionBasePEOVersionNumber | VERSION_NUMBER | — | — |
| 48 | PlanVersionBasePEOWfStatusCode | WF_STATUS_CODE | — | — |

### [[pjo_plan_versions_tl|PJO_PLAN_VERSIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlanVersionTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | PlanVersionTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | PlanVersionTranslationPEODescription | DESCRIPTION | — | — |
| 4 | PlanVersionTranslationPEOLanguage | LANGUAGE | — | — |
| 5 | PlanVersionTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PlanVersionTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | PlanVersionTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | PlanVersionTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | PlanVersionTranslationPEOPlanVersionId | PLAN_VERSION_ID | — | — |
| 10 | PlanVersionTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 11 | PlanVersionTranslationPEOVersionName | VERSION_NAME | — | — |

### [[pjo_plan_versions_vl|PJO_PLAN_VERSIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CopySrcPlanVersForPlanOptionPlanVersionId | PLAN_VERSION_ID | — | — |
| 2 | CopySrcPlanVersForPlanOptionVersionName | VERSION_NAME | — | — |
| 3 | CopySrcPlanVersForPlanOptionVersionNumber | VERSION_NUMBER | — | — |
| 4 | GenSrcPlanVersForPlanOptionPlanVersionId | PLAN_VERSION_ID | — | — |
| 5 | GenSrcPlanVersForPlanOptionVersionName | VERSION_NAME | — | — |
| 6 | GenSrcPlanVersForPlanOptionVersionNumber | VERSION_NUMBER | — | — |

### [[pjo_spread_curves_vl|PJO_SPREAD_CURVES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SpreadCurveForPlanElementDescription | DESCRIPTION | — | — |
| 2 | SpreadCurveForPlanElementName | NAME | — | ✅ |
| 3 | SpreadCurveForPlanElementSpreadCurveId | SPREAD_CURVE_ID | — | — |
| 4 | SpreadCurveForRbsElementName | NAME | — | — |
| 5 | SpreadCurveForRbsElementSpreadCurveId | SPREAD_CURVE_ID | — | — |

### [[poz_suppliers|POZ_SUPPLIERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupplierForRbsElementVendorSegment1 | SEGMENT1 | — | ✅ |
| 2 | SupplierForRbsElementVendorTaxReportingName | TAX_REPORTING_NAME | — | — |
| 3 | SupplierForRbsElementVendorVendorId | VENDOR_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
