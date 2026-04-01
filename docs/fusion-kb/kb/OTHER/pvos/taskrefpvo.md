---
id: DOC-OTHER-PVO-TaskRefPVO
doc_type: system-doc
title: "TaskRefPVO — PVO Cross-Module"
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
  - TaskRefPVO
  - taskrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaskRefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Task Ref. Acessa as tabelas: HR_ORGANIZATION_V, PER_PERSON_NAMES_F_V, PJF_PROJECTS_ALL_B (+6).

**Caminho:** `FscmTopModelAM.PjfProjectDefinitionAM.TaskRefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 206 | 9 | 1 | 125 | 61% |

---

## 🔗 Tabelas Relacionadas

- [[hr_organization_v|HR_ORGANIZATION_V]] — 6 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 6 atributos (2 BICC)
- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 3 atributos (2 BICC)
- [[pjf_proj_elements_b|PJF_PROJ_ELEMENTS_B]] — 158 atributos (1 PKs, 111 BICC)
- [[pjf_proj_elements_tl|PJF_PROJ_ELEMENTS_TL]] — 8 atributos (2 BICC)
- [[pjf_proj_element_version|PJF_PROJ_ELEMENT_VERSION]] — 2 atributos
- [[pjf_work_types_vl|PJF_WORK_TYPES_VL]] — 3 atributos (1 BICC)
- [[pjo_project_progress|PJO_PROJECT_PROGRESS]] — 15 atributos (5 BICC)
- [[pjt_proj_plan_lines|PJT_PROJ_PLAN_LINES]] — 5 atributos

---

## ⚙️ Atributos

### [[hr_organization_v|HR_ORGANIZATION_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationDPEOClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | OrganizationDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | OrganizationDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | OrganizationDPEOName | NAME | — | ✅ |
| 5 | OrganizationDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | OrganizationDPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNameDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonNameDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonNameDPEOListName | LIST_NAME | — | ✅ |
| 4 | PersonNameDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | PersonNameDPEOPersonId | PERSON_ID | — | — |
| 6 | PersonNameDPEOPersonNameId | PERSON_NAME_ID | — | — |

### [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectBasePEOProjectCategory | PROJECT_CATEGORY | — | — |
| 2 | ProjectBasePEOProjectId | PROJECT_ID | — | ✅ |
| 3 | ProjectBasePEOSegment1 | SEGMENT1 | — | ✅ |

### [[pjf_proj_elements_b|PJF_PROJ_ELEMENTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClinTaskBasePEOElementNumber | ELEMENT_NUMBER | — | — |
| 2 | ClinTaskBasePEOProjElementId | PROJ_ELEMENT_ID | — | — |
| 3 | ClinTaskBasePEOProjectId | PROJECT_ID | — | — |
| 4 | IcClinTaskBasePEOElementNumber | ELEMENT_NUMBER | — | — |
| 5 | IcClinTaskBasePEOProjElementId | PROJ_ELEMENT_ID | — | — |
| 6 | IcClinTaskBasePEOProjectId | PROJECT_ID | — | — |
| 7 | ParentTaskStructureBasePEOElementNumber | ELEMENT_NUMBER | — | — |
| 8 | ParentTaskStructureBasePEOProjElementId | PROJ_ELEMENT_ID | — | — |
| 9 | ParentTaskStructureBasePEOProjectId | PROJECT_ID | — | — |
| 10 | ProjElementId | PROJ_ELEMENT_ID | 🔑 | ✅ |
| 11 | TaskStructureBasePEOAllowCrossChargeFlag | ALLOW_CROSS_CHARGE_FLAG | — | ✅ |
| 12 | TaskStructureBasePEOBaselineFinishDate | BASELINE_FINISH_DATE | — | ✅ |
| 13 | TaskStructureBasePEOBaselineStartDate | BASELINE_START_DATE | — | ✅ |
| 14 | TaskStructureBasePEOBillableFlag | BILLABLE_FLAG | — | ✅ |
| 15 | TaskStructureBasePEOCapitalizableFlag | CAPITALIZABLE_FLAG | — | ✅ |
| 16 | TaskStructureBasePEOCarryingOutOrganizationId | CARRYING_OUT_ORGANIZATION_ID | — | — |
| 17 | TaskStructureBasePEOCcProcessLaborFlag | CC_PROCESS_LABOR_FLAG | — | ✅ |
| 18 | TaskStructureBasePEOCcProcessNlFlag | CC_PROCESS_NL_FLAG | — | ✅ |
| 19 | TaskStructureBasePEOChargeableFlag | CHARGEABLE_FLAG | — | ✅ |
| 20 | TaskStructureBasePEOCintEligibleFlag | CINT_ELIGIBLE_FLAG | — | ✅ |
| 21 | TaskStructureBasePEOCintStopDate | CINT_STOP_DATE | — | ✅ |
| 22 | TaskStructureBasePEOClinElementId | CLIN_ELEMENT_ID | — | — |
| 23 | TaskStructureBasePEOCompletionDate | COMPLETION_DATE | — | ✅ |
| 24 | TaskStructureBasePEOContractEventId | CONTRACT_EVENT_ID | — | — |
| 25 | TaskStructureBasePEOCostIndRateSchId | COST_IND_RATE_SCH_ID | — | — |
| 26 | TaskStructureBasePEOCostIndSchFixedDate | COST_IND_SCH_FIXED_DATE | — | — |
| 27 | TaskStructureBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 28 | TaskStructureBasePEOCreatedFromSourceId | CREATED_FROM_SOURCE_ID | — | — |
| 29 | TaskStructureBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 30 | TaskStructureBasePEOCriticalFlag | CRITICAL_FLAG | — | ✅ |
| 31 | TaskStructureBasePEODenormDisplaySequence | DENORM_DISPLAY_SEQUENCE | — | ✅ |
| 32 | TaskStructureBasePEODenormElemVerId | DENORM_ELEM_VER_ID | — | — |
| 33 | TaskStructureBasePEODenormExecutionDispSeq | DENORM_EXECUTION_DISP_SEQ | — | — |
| 34 | TaskStructureBasePEODenormParentElemVerId | DENORM_PARENT_ELEM_VER_ID | — | — |
| 35 | TaskStructureBasePEODenormParentElementId | DENORM_PARENT_ELEMENT_ID | — | — |
| 36 | TaskStructureBasePEODenormParentObjectType | DENORM_PARENT_OBJECT_TYPE | — | — |
| 37 | TaskStructureBasePEODenormParentStructVerId | DENORM_PARENT_STRUCT_VER_ID | — | — |
| 38 | TaskStructureBasePEODenormTopElementId | DENORM_TOP_ELEMENT_ID | — | — |
| 39 | TaskStructureBasePEODenormWbsLevel | DENORM_WBS_LEVEL | — | ✅ |
| 40 | TaskStructureBasePEODenormWbsNumber | DENORM_WBS_NUMBER | — | ✅ |
| 41 | TaskStructureBasePEOElementNumber | ELEMENT_NUMBER | — | ✅ |
| 42 | TaskStructureBasePEOElementType | ELEMENT_TYPE | — | ✅ |
| 43 | TaskStructureBasePEOEtcCalcMethod | ETC_CALC_METHOD | — | ✅ |
| 44 | TaskStructureBasePEOExternalId | EXTERNAL_ID | — | — |
| 45 | TaskStructureBasePEOGateFlag | GATE_FLAG | — | — |
| 46 | TaskStructureBasePEOGenEtcSourceCode | GEN_ETC_SOURCE_CODE | — | — |
| 47 | TaskStructureBasePEOIcClinElementId | IC_CLIN_ELEMENT_ID | — | — |
| 48 | TaskStructureBasePEOIssueId | ISSUE_ID | — | — |
| 49 | TaskStructureBasePEOLaborCostMultiplierName | LABOR_COST_MULTIPLIER_NAME | — | — |
| 50 | TaskStructureBasePEOLaborTpFixedDate | LABOR_TP_FIXED_DATE | — | ✅ |
| 51 | TaskStructureBasePEOLaborTpScheduleId | LABOR_TP_SCHEDULE_ID | — | ✅ |
| 52 | TaskStructureBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 53 | TaskStructureBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 54 | TaskStructureBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 55 | TaskStructureBasePEOLastViewedDate | LAST_VIEWED_DATE | — | — |
| 56 | TaskStructureBasePEOLeafNodeFlag | LEAF_NODE_FLAG | — | — |
| 57 | TaskStructureBasePEOLimitToTxnControlsFlag | LIMIT_TO_TXN_CONTROLS_FLAG | — | ✅ |
| 58 | TaskStructureBasePEOManagerPersonId | MANAGER_PERSON_ID | — | — |
| 59 | TaskStructureBasePEOMilestoneFlag | MILESTONE_FLAG | — | ✅ |
| 60 | TaskStructureBasePEONlTpFixedDate | NL_TP_FIXED_DATE | — | ✅ |
| 61 | TaskStructureBasePEONlTpScheduleId | NL_TP_SCHEDULE_ID | — | ✅ |
| 62 | TaskStructureBasePEONumberAttr01 | NUMBER_ATTR01 | — | ✅ |
| 63 | TaskStructureBasePEONumberAttr02 | NUMBER_ATTR02 | — | ✅ |
| 64 | TaskStructureBasePEONumberAttr03 | NUMBER_ATTR03 | — | ✅ |
| 65 | TaskStructureBasePEONumberAttr04 | NUMBER_ATTR04 | — | ✅ |
| 66 | TaskStructureBasePEONumberAttr05 | NUMBER_ATTR05 | — | ✅ |
| 67 | TaskStructureBasePEONumberAttr06 | NUMBER_ATTR06 | — | ✅ |
| 68 | TaskStructureBasePEONumberAttr07 | NUMBER_ATTR07 | — | ✅ |
| 69 | TaskStructureBasePEONumberAttr08 | NUMBER_ATTR08 | — | ✅ |
| 70 | TaskStructureBasePEONumberAttr09 | NUMBER_ATTR09 | — | ✅ |
| 71 | TaskStructureBasePEONumberAttr10 | NUMBER_ATTR10 | — | ✅ |
| 72 | TaskStructureBasePEOObjectAssociationBitmap | OBJECT_ASSOCIATION_BITMAP | — | — |
| 73 | TaskStructureBasePEOObjectType | OBJECT_TYPE | — | — |
| 74 | TaskStructureBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 75 | TaskStructureBasePEOOvrCostIndRateSchId | OVR_COST_IND_RATE_SCH_ID | — | — |
| 76 | TaskStructureBasePEOParentStructureId | PARENT_STRUCTURE_ID | — | — |
| 77 | TaskStructureBasePEOPercentCompCalcMethod | PERCENT_COMP_CALC_METHOD | — | ✅ |
| 78 | TaskStructureBasePEOPlanningDatesRollupFlag | PLANNING_DATES_ROLLUP_FLAG | — | — |
| 79 | TaskStructureBasePEOPlanningEndDate | PLANNING_END_DATE | — | ✅ |
| 80 | TaskStructureBasePEOPlanningStartDate | PLANNING_START_DATE | — | ✅ |
| 81 | TaskStructureBasePEOPmSourceCode | PM_SOURCE_CODE | — | ✅ |
| 82 | TaskStructureBasePEOPmSourceReference | PM_SOURCE_REFERENCE | — | ✅ |
| 83 | TaskStructureBasePEOPrimaryResourceId | PRIMARY_RESOURCE_ID | — | — |
| 84 | TaskStructureBasePEOProjectId | PROJECT_ID | — | — |
| 85 | TaskStructureBasePEOReceiveProjectInvoiceFlag | RECEIVE_PROJECT_INVOICE_FLAG | — | ✅ |
| 86 | TaskStructureBasePEORetirementCostFlag | RETIREMENT_COST_FLAG | — | ✅ |
| 87 | TaskStructureBasePEORqmtId | RQMT_ID | — | — |
| 88 | TaskStructureBasePEOServiceTypeCode | SERVICE_TYPE_CODE | — | ✅ |
| 89 | TaskStructureBasePEOSiteUseId | SITE_USE_ID | — | ✅ |
| 90 | TaskStructureBasePEOSprintId | SPRINT_ID | — | — |
| 91 | TaskStructureBasePEOStartDate | START_DATE | — | ✅ |
| 92 | TaskStructureBasePEOStructureType | STRUCTURE_TYPE | — | ✅ |
| 93 | TaskStructureBasePEOTaskCode01Id | TASK_CODE01_ID | — | ✅ |
| 94 | TaskStructureBasePEOTaskCode02Id | TASK_CODE02_ID | — | ✅ |
| 95 | TaskStructureBasePEOTaskCode03Id | TASK_CODE03_ID | — | ✅ |
| 96 | TaskStructureBasePEOTaskCode04Id | TASK_CODE04_ID | — | ✅ |
| 97 | TaskStructureBasePEOTaskCode05Id | TASK_CODE05_ID | — | ✅ |
| 98 | TaskStructureBasePEOTaskCode06Id | TASK_CODE06_ID | — | ✅ |
| 99 | TaskStructureBasePEOTaskCode07Id | TASK_CODE07_ID | — | ✅ |
| 100 | TaskStructureBasePEOTaskCode08Id | TASK_CODE08_ID | — | ✅ |
| 101 | TaskStructureBasePEOTaskCode09Id | TASK_CODE09_ID | — | ✅ |
| 102 | TaskStructureBasePEOTaskCode10Id | TASK_CODE10_ID | — | ✅ |
| 103 | TaskStructureBasePEOTaskCode11Id | TASK_CODE11_ID | — | ✅ |
| 104 | TaskStructureBasePEOTaskCode12Id | TASK_CODE12_ID | — | ✅ |
| 105 | TaskStructureBasePEOTaskCode13Id | TASK_CODE13_ID | — | ✅ |
| 106 | TaskStructureBasePEOTaskCode14Id | TASK_CODE14_ID | — | ✅ |
| 107 | TaskStructureBasePEOTaskCode15Id | TASK_CODE15_ID | — | ✅ |
| 108 | TaskStructureBasePEOTaskCode16Id | TASK_CODE16_ID | — | ✅ |
| 109 | TaskStructureBasePEOTaskCode17Id | TASK_CODE17_ID | — | ✅ |
| 110 | TaskStructureBasePEOTaskCode18Id | TASK_CODE18_ID | — | ✅ |
| 111 | TaskStructureBasePEOTaskCode19Id | TASK_CODE19_ID | — | ✅ |
| 112 | TaskStructureBasePEOTaskCode20Id | TASK_CODE20_ID | — | ✅ |
| 113 | TaskStructureBasePEOTaskCode21Id | TASK_CODE21_ID | — | ✅ |
| 114 | TaskStructureBasePEOTaskCode22Id | TASK_CODE22_ID | — | ✅ |
| 115 | TaskStructureBasePEOTaskCode23Id | TASK_CODE23_ID | — | ✅ |
| 116 | TaskStructureBasePEOTaskCode24Id | TASK_CODE24_ID | — | ✅ |
| 117 | TaskStructureBasePEOTaskCode25Id | TASK_CODE25_ID | — | ✅ |
| 118 | TaskStructureBasePEOTaskCode26Id | TASK_CODE26_ID | — | ✅ |
| 119 | TaskStructureBasePEOTaskCode27Id | TASK_CODE27_ID | — | ✅ |
| 120 | TaskStructureBasePEOTaskCode28Id | TASK_CODE28_ID | — | ✅ |
| 121 | TaskStructureBasePEOTaskCode29Id | TASK_CODE29_ID | — | ✅ |
| 122 | TaskStructureBasePEOTaskCode30Id | TASK_CODE30_ID | — | ✅ |
| 123 | TaskStructureBasePEOTaskCode31Id | TASK_CODE31_ID | — | ✅ |
| 124 | TaskStructureBasePEOTaskCode32Id | TASK_CODE32_ID | — | ✅ |
| 125 | TaskStructureBasePEOTaskCode33Id | TASK_CODE33_ID | — | ✅ |
| 126 | TaskStructureBasePEOTaskCode34Id | TASK_CODE34_ID | — | ✅ |
| 127 | TaskStructureBasePEOTaskCode35Id | TASK_CODE35_ID | — | ✅ |
| 128 | TaskStructureBasePEOTaskCode36Id | TASK_CODE36_ID | — | ✅ |
| 129 | TaskStructureBasePEOTaskCode37Id | TASK_CODE37_ID | — | ✅ |
| 130 | TaskStructureBasePEOTaskCode38Id | TASK_CODE38_ID | — | ✅ |
| 131 | TaskStructureBasePEOTaskCode39Id | TASK_CODE39_ID | — | ✅ |
| 132 | TaskStructureBasePEOTaskCode40Id | TASK_CODE40_ID | — | ✅ |
| 133 | TaskStructureBasePEOTaskStatusCode | TASK_STATUS_CODE | — | — |
| 134 | TaskStructureBasePEOTaskTypeCode | TASK_TYPE_CODE | — | — |
| 135 | TaskStructureBasePEOTextAttr01 | TEXT_ATTR01 | — | ✅ |
| 136 | TaskStructureBasePEOTextAttr02 | TEXT_ATTR02 | — | ✅ |
| 137 | TaskStructureBasePEOTextAttr03 | TEXT_ATTR03 | — | ✅ |
| 138 | TaskStructureBasePEOTextAttr04 | TEXT_ATTR04 | — | ✅ |
| 139 | TaskStructureBasePEOTextAttr05 | TEXT_ATTR05 | — | ✅ |
| 140 | TaskStructureBasePEOTextAttr06 | TEXT_ATTR06 | — | ✅ |
| 141 | TaskStructureBasePEOTextAttr07 | TEXT_ATTR07 | — | ✅ |
| 142 | TaskStructureBasePEOTextAttr08 | TEXT_ATTR08 | — | ✅ |
| 143 | TaskStructureBasePEOTextAttr09 | TEXT_ATTR09 | — | ✅ |
| 144 | TaskStructureBasePEOTextAttr10 | TEXT_ATTR10 | — | ✅ |
| 145 | TaskStructureBasePEOTextAttr11 | TEXT_ATTR11 | — | ✅ |
| 146 | TaskStructureBasePEOTextAttr12 | TEXT_ATTR12 | — | ✅ |
| 147 | TaskStructureBasePEOTextAttr13 | TEXT_ATTR13 | — | ✅ |
| 148 | TaskStructureBasePEOTextAttr14 | TEXT_ATTR14 | — | ✅ |
| 149 | TaskStructureBasePEOTextAttr15 | TEXT_ATTR15 | — | ✅ |
| 150 | TaskStructureBasePEOTextAttr16 | TEXT_ATTR16 | — | ✅ |
| 151 | TaskStructureBasePEOTextAttr17 | TEXT_ATTR17 | — | ✅ |
| 152 | TaskStructureBasePEOTextAttr18 | TEXT_ATTR18 | — | ✅ |
| 153 | TaskStructureBasePEOTextAttr19 | TEXT_ATTR19 | — | ✅ |
| 154 | TaskStructureBasePEOTextAttr20 | TEXT_ATTR20 | — | ✅ |
| 155 | TaskStructureBasePEOWorkTypeId | WORK_TYPE_ID | — | — |
| 156 | TopTaskBasePEOElementNumber | ELEMENT_NUMBER | — | — |
| 157 | TopTaskBasePEOProjElementId | PROJ_ELEMENT_ID | — | — |
| 158 | TopTaskBasePEOProjectId | PROJECT_ID | — | — |

### [[pjf_proj_elements_tl|PJF_PROJ_ELEMENTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskStructureTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | TaskStructureTranslationPEODescription | DESCRIPTION | — | ✅ |
| 3 | TaskStructureTranslationPEOLanguage | LANGUAGE | — | — |
| 4 | TaskStructureTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 5 | TaskStructureTranslationPEOName | NAME | — | ✅ |
| 6 | TaskStructureTranslationPEOProjElementId | PROJ_ELEMENT_ID | — | — |
| 7 | TaskStructureTranslationPEOProjectId | PROJECT_ID | — | — |
| 8 | TaskStructureTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[pjf_proj_element_version|PJF_PROJ_ELEMENT_VERSION]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ElementVersionId | ELEMENT_VERSION_ID | — | — |
| 2 | TaskStructureVersionPEOExecutionLeaf | EXECUTION_LEAF | — | — |

### [[pjf_work_types_vl|PJF_WORK_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkTypePEOName | NAME | — | ✅ |
| 2 | WorkTypePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | WorkTypePEOWorkTypeId | WORK_TYPE_ID | — | — |

### [[pjo_project_progress|PJO_PROJECT_PROGRESS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectProgressPEOActualFinishDate | ACTUAL_FINISH_DATE | — | ✅ |
| 2 | ProjectProgressPEOActualStartDate | ACTUAL_START_DATE | — | ✅ |
| 3 | ProjectProgressPEOCreatedBy | CREATED_BY | — | — |
| 4 | ProjectProgressPEOCreationDate | CREATION_DATE | — | — |
| 5 | ProjectProgressPEOEstimatedFinishDate | ESTIMATED_FINISH_DATE | — | ✅ |
| 6 | ProjectProgressPEOEstimatedStartDate | ESTIMATED_START_DATE | — | ✅ |
| 7 | ProjectProgressPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ProjectProgressPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ProjectProgressPEOObjectId | OBJECT_ID | — | — |
| 10 | ProjectProgressPEOObjectType | OBJECT_TYPE | — | — |
| 11 | ProjectProgressPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ProjectProgressPEOProjElementId | PROJ_ELEMENT_ID | — | — |
| 13 | ProjectProgressPEOProjectId | PROJECT_ID | — | — |
| 14 | ProjectProgressPEOProjectProgressId | PROJECT_PROGRESS_ID | — | — |
| 15 | ProjectProgressPEOPublishedFlag | PUBLISHED_FLAG | — | — |

### [[pjt_proj_plan_lines|PJT_PROJ_PLAN_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Id | ID | — | — |
| 2 | ProjPlanLinePEOActualFinishDate | ACTUAL_FINISH_DATE | — | — |
| 3 | ProjPlanLinePEODuration | DURATION | — | — |
| 4 | ProjPlanLinePEOFinishDate | FINISH_DATE | — | — |
| 5 | ProjPlanLinePEOProgressStatusCode | PROGRESS_STATUS_CODE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
