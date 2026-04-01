---
id: DOC-OTHER-PVO-TaskMSVLPVO
doc_type: system-doc
title: "TaskMSVLPVO — PVO Cross-Module"
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
  - TaskMSVLPVO
  - taskmsvlpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaskMSVLPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Task MSVL. Acessa as tabelas: HR_ORGANIZATION_V, PER_PERSON_NAMES_F_V, PJF_PROJECTS_ALL_B (+4).

**Caminho:** `FscmTopModelAM.PjfProjectDefinitionAM.TaskMSVLPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 186 | 7 | 1 | 10 | 5% |

---

## 🔗 Tabelas Relacionadas

- [[hr_organization_v|HR_ORGANIZATION_V]] — 6 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 6 atributos (1 BICC)
- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 3 atributos
- [[pjf_proj_elements_b|PJF_PROJ_ELEMENTS_B]] — 12 atributos
- [[pjf_proj_elements_vl|PJF_PROJ_ELEMENTS_VL]] — 147 atributos (1 PKs, 8 BICC)
- [[pjf_work_types_vl|PJF_WORK_TYPES_VL]] — 3 atributos
- [[pjo_project_progress|PJO_PROJECT_PROGRESS]] — 9 atributos

---

## ⚙️ Atributos

### [[hr_organization_v|HR_ORGANIZATION_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationDPEOClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | OrganizationDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | OrganizationDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | OrganizationDPEOName | NAME | — | — |
| 5 | OrganizationDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | OrganizationDPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNameDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonNameDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonNameDPEOListName | LIST_NAME | — | — |
| 4 | PersonNameDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | PersonNameDPEOPersonId | PERSON_ID | — | — |
| 6 | PersonNameDPEOPersonNameId | PERSON_NAME_ID | — | — |

### [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectBasePEOProjectCategory | PROJECT_CATEGORY | — | — |
| 2 | ProjectBasePEOProjectId | PROJECT_ID | — | — |
| 3 | ProjectBasePEOSegment1 | SEGMENT1 | — | — |

### [[pjf_proj_elements_b|PJF_PROJ_ELEMENTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClinTaskBasePEOElementNumber | ELEMENT_NUMBER | — | — |
| 2 | ClinTaskBasePEOProjElementId | PROJ_ELEMENT_ID | — | — |
| 3 | ClinTaskBasePEOProjectId3 | PROJECT_ID | — | — |
| 4 | IcClinTaskBasePEOElementNumber | ELEMENT_NUMBER | — | — |
| 5 | IcClinTaskBasePEOProjElementId | PROJ_ELEMENT_ID | — | — |
| 6 | IcClinTaskBasePEOProjectId2 | PROJECT_ID | — | — |
| 7 | ParentTaskBasePEOElementNumber | ELEMENT_NUMBER | — | — |
| 8 | ParentTaskBasePEOProjElementId | PROJ_ELEMENT_ID | — | — |
| 9 | ParentTaskBasePEOProjectId | PROJECT_ID | — | — |
| 10 | TopTaskBasePEOElementNumber | ELEMENT_NUMBER | — | — |
| 11 | TopTaskBasePEOProjElementId | PROJ_ELEMENT_ID | — | — |
| 12 | TopTaskBasePEOProjectId1 | PROJECT_ID | — | — |

### [[pjf_proj_elements_vl|PJF_PROJ_ELEMENTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjElementId | PROJ_ELEMENT_ID | 🔑 | ✅ |
| 2 | TaskStructurePEOAllowCrossChargeFlag | ALLOW_CROSS_CHARGE_FLAG | — | — |
| 3 | TaskStructurePEOBaselineFinishDate | BASELINE_FINISH_DATE | — | — |
| 4 | TaskStructurePEOBaselineStartDate | BASELINE_START_DATE | — | — |
| 5 | TaskStructurePEOBillableFlag | BILLABLE_FLAG | — | — |
| 6 | TaskStructurePEOCapitalizableFlag | CAPITALIZABLE_FLAG | — | — |
| 7 | TaskStructurePEOCarryingOutOrganizationId | CARRYING_OUT_ORGANIZATION_ID | — | — |
| 8 | TaskStructurePEOCcProcessLaborFlag | CC_PROCESS_LABOR_FLAG | — | — |
| 9 | TaskStructurePEOCcProcessNlFlag | CC_PROCESS_NL_FLAG | — | — |
| 10 | TaskStructurePEOChargeableFlag | CHARGEABLE_FLAG | — | — |
| 11 | TaskStructurePEOCintEligibleFlag | CINT_ELIGIBLE_FLAG | — | — |
| 12 | TaskStructurePEOCintStopDate | CINT_STOP_DATE | — | — |
| 13 | TaskStructurePEOClinElementId | CLIN_ELEMENT_ID | — | — |
| 14 | TaskStructurePEOCompletionDate | COMPLETION_DATE | — | — |
| 15 | TaskStructurePEOCostIndRateSchId | COST_IND_RATE_SCH_ID | — | — |
| 16 | TaskStructurePEOCostIndSchFixedDate | COST_IND_SCH_FIXED_DATE | — | — |
| 17 | TaskStructurePEOCreatedBy | CREATED_BY | — | ✅ |
| 18 | TaskStructurePEOCreatedFromSourceId | CREATED_FROM_SOURCE_ID | — | — |
| 19 | TaskStructurePEOCreationDate | CREATION_DATE | — | ✅ |
| 20 | TaskStructurePEOCriticalFlag | CRITICAL_FLAG | — | — |
| 21 | TaskStructurePEODenormDisplaySequence | DENORM_DISPLAY_SEQUENCE | — | — |
| 22 | TaskStructurePEODenormElemVerId | DENORM_ELEM_VER_ID | — | — |
| 23 | TaskStructurePEODenormExecutionDispSeq | DENORM_EXECUTION_DISP_SEQ | — | — |
| 24 | TaskStructurePEODenormParentElemVerId | DENORM_PARENT_ELEM_VER_ID | — | — |
| 25 | TaskStructurePEODenormParentElementId | DENORM_PARENT_ELEMENT_ID | — | — |
| 26 | TaskStructurePEODenormParentObjectType | DENORM_PARENT_OBJECT_TYPE | — | — |
| 27 | TaskStructurePEODenormParentStructVerId | DENORM_PARENT_STRUCT_VER_ID | — | — |
| 28 | TaskStructurePEODenormTopElementId | DENORM_TOP_ELEMENT_ID | — | — |
| 29 | TaskStructurePEODenormWbsLevel | DENORM_WBS_LEVEL | — | — |
| 30 | TaskStructurePEODenormWbsNumber | DENORM_WBS_NUMBER | — | — |
| 31 | TaskStructurePEODescription | DESCRIPTION | — | ✅ |
| 32 | TaskStructurePEOElementNumber | ELEMENT_NUMBER | — | ✅ |
| 33 | TaskStructurePEOElementType | ELEMENT_TYPE | — | — |
| 34 | TaskStructurePEOEtcCalcMethod | ETC_CALC_METHOD | — | — |
| 35 | TaskStructurePEOExternalId | EXTERNAL_ID | — | — |
| 36 | TaskStructurePEOGateFlag | GATE_FLAG | — | — |
| 37 | TaskStructurePEOGenEtcSourceCode | GEN_ETC_SOURCE_CODE | — | — |
| 38 | TaskStructurePEOIcClinElementId | IC_CLIN_ELEMENT_ID | — | — |
| 39 | TaskStructurePEOIssueId | ISSUE_ID | — | — |
| 40 | TaskStructurePEOLaborCostMultiplierName | LABOR_COST_MULTIPLIER_NAME | — | — |
| 41 | TaskStructurePEOLaborTpFixedDate | LABOR_TP_FIXED_DATE | — | — |
| 42 | TaskStructurePEOLaborTpScheduleId | LABOR_TP_SCHEDULE_ID | — | — |
| 43 | TaskStructurePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 44 | TaskStructurePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 45 | TaskStructurePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 46 | TaskStructurePEOLastViewedDate | LAST_VIEWED_DATE | — | — |
| 47 | TaskStructurePEOLeafNodeFlag | LEAF_NODE_FLAG | — | — |
| 48 | TaskStructurePEOLimitToTxnControlsFlag | LIMIT_TO_TXN_CONTROLS_FLAG | — | — |
| 49 | TaskStructurePEOManagerPersonId | MANAGER_PERSON_ID | — | — |
| 50 | TaskStructurePEOMilestoneFlag | MILESTONE_FLAG | — | — |
| 51 | TaskStructurePEOName | NAME | — | ✅ |
| 52 | TaskStructurePEONlTpFixedDate | NL_TP_FIXED_DATE | — | — |
| 53 | TaskStructurePEONlTpScheduleId | NL_TP_SCHEDULE_ID | — | — |
| 54 | TaskStructurePEONumberAttr01 | NUMBER_ATTR01 | — | — |
| 55 | TaskStructurePEONumberAttr02 | NUMBER_ATTR02 | — | — |
| 56 | TaskStructurePEONumberAttr03 | NUMBER_ATTR03 | — | — |
| 57 | TaskStructurePEONumberAttr04 | NUMBER_ATTR04 | — | — |
| 58 | TaskStructurePEONumberAttr05 | NUMBER_ATTR05 | — | — |
| 59 | TaskStructurePEONumberAttr06 | NUMBER_ATTR06 | — | — |
| 60 | TaskStructurePEONumberAttr07 | NUMBER_ATTR07 | — | — |
| 61 | TaskStructurePEONumberAttr08 | NUMBER_ATTR08 | — | — |
| 62 | TaskStructurePEONumberAttr09 | NUMBER_ATTR09 | — | — |
| 63 | TaskStructurePEONumberAttr10 | NUMBER_ATTR10 | — | — |
| 64 | TaskStructurePEOObjectAssociationBitmap | OBJECT_ASSOCIATION_BITMAP | — | — |
| 65 | TaskStructurePEOObjectType | OBJECT_TYPE | — | — |
| 66 | TaskStructurePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 67 | TaskStructurePEOOvrCostIndRateSchId | OVR_COST_IND_RATE_SCH_ID | — | — |
| 68 | TaskStructurePEOParentStructureId | PARENT_STRUCTURE_ID | — | — |
| 69 | TaskStructurePEOPercentCompCalcMethod | PERCENT_COMP_CALC_METHOD | — | — |
| 70 | TaskStructurePEOPlanningDatesRollupFlag | PLANNING_DATES_ROLLUP_FLAG | — | — |
| 71 | TaskStructurePEOPlanningEndDate | PLANNING_END_DATE | — | — |
| 72 | TaskStructurePEOPlanningStartDate | PLANNING_START_DATE | — | — |
| 73 | TaskStructurePEOPmSourceCode | PM_SOURCE_CODE | — | — |
| 74 | TaskStructurePEOPmSourceReference | PM_SOURCE_REFERENCE | — | — |
| 75 | TaskStructurePEOPrimaryResourceId | PRIMARY_RESOURCE_ID | — | — |
| 76 | TaskStructurePEOProjectId | PROJECT_ID | — | — |
| 77 | TaskStructurePEOReceiveProjectInvoiceFlag | RECEIVE_PROJECT_INVOICE_FLAG | — | — |
| 78 | TaskStructurePEORetirementCostFlag | RETIREMENT_COST_FLAG | — | — |
| 79 | TaskStructurePEORqmtId | RQMT_ID | — | — |
| 80 | TaskStructurePEOServiceTypeCode | SERVICE_TYPE_CODE | — | — |
| 81 | TaskStructurePEOSiteUseId | SITE_USE_ID | — | — |
| 82 | TaskStructurePEOSprintId | SPRINT_ID | — | — |
| 83 | TaskStructurePEOStartDate | START_DATE | — | — |
| 84 | TaskStructurePEOStructureType | STRUCTURE_TYPE | — | — |
| 85 | TaskStructurePEOTaskCode01Id | TASK_CODE01_ID | — | — |
| 86 | TaskStructurePEOTaskCode02Id | TASK_CODE02_ID | — | — |
| 87 | TaskStructurePEOTaskCode03Id | TASK_CODE03_ID | — | — |
| 88 | TaskStructurePEOTaskCode04Id | TASK_CODE04_ID | — | — |
| 89 | TaskStructurePEOTaskCode05Id | TASK_CODE05_ID | — | — |
| 90 | TaskStructurePEOTaskCode06Id | TASK_CODE06_ID | — | — |
| 91 | TaskStructurePEOTaskCode07Id | TASK_CODE07_ID | — | — |
| 92 | TaskStructurePEOTaskCode08Id | TASK_CODE08_ID | — | — |
| 93 | TaskStructurePEOTaskCode09Id | TASK_CODE09_ID | — | — |
| 94 | TaskStructurePEOTaskCode10Id | TASK_CODE10_ID | — | — |
| 95 | TaskStructurePEOTaskCode11Id | TASK_CODE11_ID | — | — |
| 96 | TaskStructurePEOTaskCode12Id | TASK_CODE12_ID | — | — |
| 97 | TaskStructurePEOTaskCode13Id | TASK_CODE13_ID | — | — |
| 98 | TaskStructurePEOTaskCode14Id | TASK_CODE14_ID | — | — |
| 99 | TaskStructurePEOTaskCode15Id | TASK_CODE15_ID | — | — |
| 100 | TaskStructurePEOTaskCode16Id | TASK_CODE16_ID | — | — |
| 101 | TaskStructurePEOTaskCode17Id | TASK_CODE17_ID | — | — |
| 102 | TaskStructurePEOTaskCode18Id | TASK_CODE18_ID | — | — |
| 103 | TaskStructurePEOTaskCode19Id | TASK_CODE19_ID | — | — |
| 104 | TaskStructurePEOTaskCode20Id | TASK_CODE20_ID | — | — |
| 105 | TaskStructurePEOTaskCode21Id | TASK_CODE21_ID | — | — |
| 106 | TaskStructurePEOTaskCode22Id | TASK_CODE22_ID | — | — |
| 107 | TaskStructurePEOTaskCode23Id | TASK_CODE23_ID | — | — |
| 108 | TaskStructurePEOTaskCode24Id | TASK_CODE24_ID | — | — |
| 109 | TaskStructurePEOTaskCode25Id | TASK_CODE25_ID | — | — |
| 110 | TaskStructurePEOTaskCode26Id | TASK_CODE26_ID | — | — |
| 111 | TaskStructurePEOTaskCode27Id | TASK_CODE27_ID | — | — |
| 112 | TaskStructurePEOTaskCode28Id | TASK_CODE28_ID | — | — |
| 113 | TaskStructurePEOTaskCode29Id | TASK_CODE29_ID | — | — |
| 114 | TaskStructurePEOTaskCode30Id | TASK_CODE30_ID | — | — |
| 115 | TaskStructurePEOTaskCode31Id | TASK_CODE31_ID | — | — |
| 116 | TaskStructurePEOTaskCode32Id | TASK_CODE32_ID | — | — |
| 117 | TaskStructurePEOTaskCode33Id | TASK_CODE33_ID | — | — |
| 118 | TaskStructurePEOTaskCode34Id | TASK_CODE34_ID | — | — |
| 119 | TaskStructurePEOTaskCode35Id | TASK_CODE35_ID | — | — |
| 120 | TaskStructurePEOTaskCode36Id | TASK_CODE36_ID | — | — |
| 121 | TaskStructurePEOTaskCode37Id | TASK_CODE37_ID | — | — |
| 122 | TaskStructurePEOTaskCode38Id | TASK_CODE38_ID | — | — |
| 123 | TaskStructurePEOTaskCode39Id | TASK_CODE39_ID | — | — |
| 124 | TaskStructurePEOTaskCode40Id | TASK_CODE40_ID | — | — |
| 125 | TaskStructurePEOTaskStatusCode | TASK_STATUS_CODE | — | — |
| 126 | TaskStructurePEOTaskTypeCode | TASK_TYPE_CODE | — | — |
| 127 | TaskStructurePEOTextAttr01 | TEXT_ATTR01 | — | — |
| 128 | TaskStructurePEOTextAttr02 | TEXT_ATTR02 | — | — |
| 129 | TaskStructurePEOTextAttr03 | TEXT_ATTR03 | — | — |
| 130 | TaskStructurePEOTextAttr04 | TEXT_ATTR04 | — | — |
| 131 | TaskStructurePEOTextAttr05 | TEXT_ATTR05 | — | — |
| 132 | TaskStructurePEOTextAttr06 | TEXT_ATTR06 | — | — |
| 133 | TaskStructurePEOTextAttr07 | TEXT_ATTR07 | — | — |
| 134 | TaskStructurePEOTextAttr08 | TEXT_ATTR08 | — | — |
| 135 | TaskStructurePEOTextAttr09 | TEXT_ATTR09 | — | — |
| 136 | TaskStructurePEOTextAttr10 | TEXT_ATTR10 | — | — |
| 137 | TaskStructurePEOTextAttr11 | TEXT_ATTR11 | — | — |
| 138 | TaskStructurePEOTextAttr12 | TEXT_ATTR12 | — | — |
| 139 | TaskStructurePEOTextAttr13 | TEXT_ATTR13 | — | — |
| 140 | TaskStructurePEOTextAttr14 | TEXT_ATTR14 | — | — |
| 141 | TaskStructurePEOTextAttr15 | TEXT_ATTR15 | — | — |
| 142 | TaskStructurePEOTextAttr16 | TEXT_ATTR16 | — | — |
| 143 | TaskStructurePEOTextAttr17 | TEXT_ATTR17 | — | — |
| 144 | TaskStructurePEOTextAttr18 | TEXT_ATTR18 | — | — |
| 145 | TaskStructurePEOTextAttr19 | TEXT_ATTR19 | — | — |
| 146 | TaskStructurePEOTextAttr20 | TEXT_ATTR20 | — | — |
| 147 | TaskStructurePEOWorkTypeId | WORK_TYPE_ID | — | — |

### [[pjf_work_types_vl|PJF_WORK_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkTypePEOName | NAME | — | — |
| 2 | WorkTypePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | WorkTypePEOWorkTypeId | WORK_TYPE_ID | — | — |

### [[pjo_project_progress|PJO_PROJECT_PROGRESS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectProgressPEOActualFinishDate | ACTUAL_FINISH_DATE | — | — |
| 2 | ProjectProgressPEOActualStartDate | ACTUAL_START_DATE | — | — |
| 3 | ProjectProgressPEOEstimatedFinishDate | ESTIMATED_FINISH_DATE | — | — |
| 4 | ProjectProgressPEOEstimatedStartDate | ESTIMATED_START_DATE | — | — |
| 5 | ProjectProgressPEOObjectId | OBJECT_ID | — | — |
| 6 | ProjectProgressPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | ProjectProgressPEOProjElementId1 | PROJ_ELEMENT_ID | — | — |
| 8 | ProjectProgressPEOProjectProgressId | PROJECT_PROGRESS_ID | — | — |
| 9 | ProjectProgressPEOPublishedFlag | PUBLISHED_FLAG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
