---
id: DOC-OTHER-PVO-ProjectPlanIntegrationPVO
doc_type: system-doc
title: "ProjectPlanIntegrationPVO — PVO Cross-Module"
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
  - ProjectPlanIntegrationPVO
  - projectplanintegrationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectPlanIntegrationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Plan Integration. Acessa as tabelas: PJE_DELIVERABLE_TYPES_B, PJE_OBJECT_ASSOCIATIONS, PJF_PROJ_ELEMENTS_B (+1).

**Caminho:** `FscmTopModelAM.PjtProjectPlanAM.ProjectPlanIntegrationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 323 | 4 | 1 | 20 | 6% |

---

## 🔗 Tabelas Relacionadas

- [[pje_deliverable_types_b|PJE_DELIVERABLE_TYPES_B]] — 12 atributos
- [[pje_object_associations|PJE_OBJECT_ASSOCIATIONS]] — 14 atributos (1 PKs, 3 BICC)
- [[pjf_proj_elements_b|PJF_PROJ_ELEMENTS_B]] — 226 atributos (3 BICC)
- [[pjt_proj_plan_lines|PJT_PROJ_PLAN_LINES]] — 71 atributos (14 BICC)

---

## ⚙️ Atributos

### [[pje_deliverable_types_b|PJE_DELIVERABLE_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeliverableTypesBPEOCreatedBy | CREATED_BY | — | — |
| 2 | DeliverableTypesBPEOCreationDate | CREATION_DATE | — | — |
| 3 | DeliverableTypesBPEODeliverableTypeClass | DELIVERABLE_TYPE_CLASS | — | — |
| 4 | DeliverableTypesBPEODeliverableTypeId | DELIVERABLE_TYPE_ID | — | — |
| 5 | DeliverableTypesBPEODisabled | DISABLED | — | — |
| 6 | DeliverableTypesBPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 7 | DeliverableTypesBPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 8 | DeliverableTypesBPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 9 | DeliverableTypesBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | DeliverableTypesBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | DeliverableTypesBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | DeliverableTypesBPEOStartDateActive | START_DATE_ACTIVE | — | — |

### [[pje_object_associations|PJE_OBJECT_ASSOCIATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectAssociationPEOAssociatedObjectId | ASSOCIATED_OBJECT_ID | — | — |
| 2 | ObjectAssociationPEOAssociatedObjectSubTypeId | ASSOCIATED_OBJECT_SUB_TYPE_ID | — | — |
| 3 | ObjectAssociationPEOCompletionCriteria | COMPLETION_CRITERIA | — | — |
| 4 | ObjectAssociationPEOCompletionStatus | COMPLETION_STATUS | — | ✅ |
| 5 | ObjectAssociationPEOCreatedBy | CREATED_BY | — | — |
| 6 | ObjectAssociationPEOCreationDate | CREATION_DATE | — | — |
| 7 | ObjectAssociationPEODescription | DESCRIPTION | — | — |
| 8 | ObjectAssociationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ObjectAssociationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | ObjectAssociationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | ObjectAssociationPEOObjectAssociationId | OBJECT_ASSOCIATION_ID | 🔑 | ✅ |
| 12 | ObjectAssociationPEOObjectId | OBJECT_ID | — | — |
| 13 | ObjectAssociationPEOObjectType | OBJECT_TYPE | — | — |
| 14 | ObjectAssociationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[pjf_proj_elements_b|PJF_PROJ_ELEMENTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskStructureBasePEOAllowCrossChargeFlag | ALLOW_CROSS_CHARGE_FLAG | — | — |
| 2 | TaskStructureBasePEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | TaskStructureBasePEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | TaskStructureBasePEOAttribute10Date | ATTRIBUTE10_DATE | — | — |
| 5 | TaskStructureBasePEOAttribute10Number | ATTRIBUTE10_NUMBER | — | — |
| 6 | TaskStructureBasePEOAttribute11 | ATTRIBUTE11 | — | — |
| 7 | TaskStructureBasePEOAttribute11Date | ATTRIBUTE11_DATE | — | — |
| 8 | TaskStructureBasePEOAttribute11Number | ATTRIBUTE11_NUMBER | — | — |
| 9 | TaskStructureBasePEOAttribute12 | ATTRIBUTE12 | — | — |
| 10 | TaskStructureBasePEOAttribute12Date | ATTRIBUTE12_DATE | — | — |
| 11 | TaskStructureBasePEOAttribute12Number | ATTRIBUTE12_NUMBER | — | — |
| 12 | TaskStructureBasePEOAttribute13 | ATTRIBUTE13 | — | — |
| 13 | TaskStructureBasePEOAttribute13Date | ATTRIBUTE13_DATE | — | — |
| 14 | TaskStructureBasePEOAttribute13Number | ATTRIBUTE13_NUMBER | — | — |
| 15 | TaskStructureBasePEOAttribute14 | ATTRIBUTE14 | — | — |
| 16 | TaskStructureBasePEOAttribute14Date | ATTRIBUTE14_DATE | — | — |
| 17 | TaskStructureBasePEOAttribute14Number | ATTRIBUTE14_NUMBER | — | — |
| 18 | TaskStructureBasePEOAttribute15 | ATTRIBUTE15 | — | — |
| 19 | TaskStructureBasePEOAttribute15Date | ATTRIBUTE15_DATE | — | — |
| 20 | TaskStructureBasePEOAttribute15Number | ATTRIBUTE15_NUMBER | — | — |
| 21 | TaskStructureBasePEOAttribute16 | ATTRIBUTE16 | — | — |
| 22 | TaskStructureBasePEOAttribute17 | ATTRIBUTE17 | — | — |
| 23 | TaskStructureBasePEOAttribute18 | ATTRIBUTE18 | — | — |
| 24 | TaskStructureBasePEOAttribute19 | ATTRIBUTE19 | — | — |
| 25 | TaskStructureBasePEOAttribute1Date | ATTRIBUTE1_DATE | — | — |
| 26 | TaskStructureBasePEOAttribute1Number | ATTRIBUTE1_NUMBER | — | — |
| 27 | TaskStructureBasePEOAttribute2 | ATTRIBUTE2 | — | — |
| 28 | TaskStructureBasePEOAttribute20 | ATTRIBUTE20 | — | — |
| 29 | TaskStructureBasePEOAttribute21 | ATTRIBUTE21 | — | — |
| 30 | TaskStructureBasePEOAttribute22 | ATTRIBUTE22 | — | — |
| 31 | TaskStructureBasePEOAttribute23 | ATTRIBUTE23 | — | — |
| 32 | TaskStructureBasePEOAttribute24 | ATTRIBUTE24 | — | — |
| 33 | TaskStructureBasePEOAttribute25 | ATTRIBUTE25 | — | — |
| 34 | TaskStructureBasePEOAttribute26 | ATTRIBUTE26 | — | — |
| 35 | TaskStructureBasePEOAttribute27 | ATTRIBUTE27 | — | — |
| 36 | TaskStructureBasePEOAttribute28 | ATTRIBUTE28 | — | — |
| 37 | TaskStructureBasePEOAttribute29 | ATTRIBUTE29 | — | — |
| 38 | TaskStructureBasePEOAttribute2Date | ATTRIBUTE2_DATE | — | — |
| 39 | TaskStructureBasePEOAttribute2Number | ATTRIBUTE2_NUMBER | — | — |
| 40 | TaskStructureBasePEOAttribute3 | ATTRIBUTE3 | — | — |
| 41 | TaskStructureBasePEOAttribute30 | ATTRIBUTE30 | — | — |
| 42 | TaskStructureBasePEOAttribute31 | ATTRIBUTE31 | — | — |
| 43 | TaskStructureBasePEOAttribute32 | ATTRIBUTE32 | — | — |
| 44 | TaskStructureBasePEOAttribute33 | ATTRIBUTE33 | — | — |
| 45 | TaskStructureBasePEOAttribute34 | ATTRIBUTE34 | — | — |
| 46 | TaskStructureBasePEOAttribute35 | ATTRIBUTE35 | — | — |
| 47 | TaskStructureBasePEOAttribute36 | ATTRIBUTE36 | — | — |
| 48 | TaskStructureBasePEOAttribute37 | ATTRIBUTE37 | — | — |
| 49 | TaskStructureBasePEOAttribute38 | ATTRIBUTE38 | — | — |
| 50 | TaskStructureBasePEOAttribute39 | ATTRIBUTE39 | — | — |
| 51 | TaskStructureBasePEOAttribute3Date | ATTRIBUTE3_DATE | — | — |
| 52 | TaskStructureBasePEOAttribute3Number | ATTRIBUTE3_NUMBER | — | — |
| 53 | TaskStructureBasePEOAttribute4 | ATTRIBUTE4 | — | — |
| 54 | TaskStructureBasePEOAttribute40 | ATTRIBUTE40 | — | — |
| 55 | TaskStructureBasePEOAttribute41 | ATTRIBUTE41 | — | — |
| 56 | TaskStructureBasePEOAttribute42 | ATTRIBUTE42 | — | — |
| 57 | TaskStructureBasePEOAttribute43 | ATTRIBUTE43 | — | — |
| 58 | TaskStructureBasePEOAttribute44 | ATTRIBUTE44 | — | — |
| 59 | TaskStructureBasePEOAttribute45 | ATTRIBUTE45 | — | — |
| 60 | TaskStructureBasePEOAttribute46 | ATTRIBUTE46 | — | — |
| 61 | TaskStructureBasePEOAttribute47 | ATTRIBUTE47 | — | — |
| 62 | TaskStructureBasePEOAttribute48 | ATTRIBUTE48 | — | — |
| 63 | TaskStructureBasePEOAttribute49 | ATTRIBUTE49 | — | — |
| 64 | TaskStructureBasePEOAttribute4Date | ATTRIBUTE4_DATE | — | — |
| 65 | TaskStructureBasePEOAttribute4Number | ATTRIBUTE4_NUMBER | — | — |
| 66 | TaskStructureBasePEOAttribute5 | ATTRIBUTE5 | — | — |
| 67 | TaskStructureBasePEOAttribute50 | ATTRIBUTE50 | — | — |
| 68 | TaskStructureBasePEOAttribute5Date | ATTRIBUTE5_DATE | — | — |
| 69 | TaskStructureBasePEOAttribute5Number | ATTRIBUTE5_NUMBER | — | — |
| 70 | TaskStructureBasePEOAttribute6 | ATTRIBUTE6 | — | — |
| 71 | TaskStructureBasePEOAttribute6Date | ATTRIBUTE6_DATE | — | — |
| 72 | TaskStructureBasePEOAttribute6Number | ATTRIBUTE6_NUMBER | — | — |
| 73 | TaskStructureBasePEOAttribute7 | ATTRIBUTE7 | — | — |
| 74 | TaskStructureBasePEOAttribute7Date | ATTRIBUTE7_DATE | — | — |
| 75 | TaskStructureBasePEOAttribute7Number | ATTRIBUTE7_NUMBER | — | — |
| 76 | TaskStructureBasePEOAttribute8 | ATTRIBUTE8 | — | — |
| 77 | TaskStructureBasePEOAttribute8Date | ATTRIBUTE8_DATE | — | — |
| 78 | TaskStructureBasePEOAttribute8Number | ATTRIBUTE8_NUMBER | — | — |
| 79 | TaskStructureBasePEOAttribute9 | ATTRIBUTE9 | — | — |
| 80 | TaskStructureBasePEOAttribute9Date | ATTRIBUTE9_DATE | — | — |
| 81 | TaskStructureBasePEOAttribute9Number | ATTRIBUTE9_NUMBER | — | — |
| 82 | TaskStructureBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 83 | TaskStructureBasePEOBaselineFinishDate | BASELINE_FINISH_DATE | — | — |
| 84 | TaskStructureBasePEOBaselineStartDate | BASELINE_START_DATE | — | — |
| 85 | TaskStructureBasePEOBillableFlag | BILLABLE_FLAG | — | — |
| 86 | TaskStructureBasePEOCapitalizableFlag | CAPITALIZABLE_FLAG | — | — |
| 87 | TaskStructureBasePEOCarryingOutOrganizationId | CARRYING_OUT_ORGANIZATION_ID | — | — |
| 88 | TaskStructureBasePEOCcProcessLaborFlag | CC_PROCESS_LABOR_FLAG | — | — |
| 89 | TaskStructureBasePEOCcProcessNlFlag | CC_PROCESS_NL_FLAG | — | — |
| 90 | TaskStructureBasePEOChargeableFlag | CHARGEABLE_FLAG | — | — |
| 91 | TaskStructureBasePEOCintEligibleFlag | CINT_ELIGIBLE_FLAG | — | — |
| 92 | TaskStructureBasePEOCintStopDate | CINT_STOP_DATE | — | — |
| 93 | TaskStructureBasePEOClinElementId | CLIN_ELEMENT_ID | — | — |
| 94 | TaskStructureBasePEOCompletionDate | COMPLETION_DATE | — | — |
| 95 | TaskStructureBasePEOCostIndRateSchId | COST_IND_RATE_SCH_ID | — | — |
| 96 | TaskStructureBasePEOCostIndSchFixedDate | COST_IND_SCH_FIXED_DATE | — | — |
| 97 | TaskStructureBasePEOCreatedBy | CREATED_BY | — | — |
| 98 | TaskStructureBasePEOCreatedFromSourceId | CREATED_FROM_SOURCE_ID | — | — |
| 99 | TaskStructureBasePEOCreationDate | CREATION_DATE | — | — |
| 100 | TaskStructureBasePEOCriticalFlag | CRITICAL_FLAG | — | — |
| 101 | TaskStructureBasePEODenormDisplaySequence | DENORM_DISPLAY_SEQUENCE | — | — |
| 102 | TaskStructureBasePEODenormElemVerId | DENORM_ELEM_VER_ID | — | — |
| 103 | TaskStructureBasePEODenormExecutionDispSeq | DENORM_EXECUTION_DISP_SEQ | — | — |
| 104 | TaskStructureBasePEODenormParentElemVerId | DENORM_PARENT_ELEM_VER_ID | — | — |
| 105 | TaskStructureBasePEODenormParentElementId | DENORM_PARENT_ELEMENT_ID | — | — |
| 106 | TaskStructureBasePEODenormParentObjectType | DENORM_PARENT_OBJECT_TYPE | — | — |
| 107 | TaskStructureBasePEODenormParentStructVerId | DENORM_PARENT_STRUCT_VER_ID | — | — |
| 108 | TaskStructureBasePEODenormTopElementId | DENORM_TOP_ELEMENT_ID | — | — |
| 109 | TaskStructureBasePEODenormWbsLevel | DENORM_WBS_LEVEL | — | — |
| 110 | TaskStructureBasePEODenormWbsNumber | DENORM_WBS_NUMBER | — | — |
| 111 | TaskStructureBasePEOElementNumber | ELEMENT_NUMBER | — | — |
| 112 | TaskStructureBasePEOElementType | ELEMENT_TYPE | — | — |
| 113 | TaskStructureBasePEOEtcCalcMethod | ETC_CALC_METHOD | — | — |
| 114 | TaskStructureBasePEOExternalId | EXTERNAL_ID | — | — |
| 115 | TaskStructureBasePEOGateFlag | GATE_FLAG | — | — |
| 116 | TaskStructureBasePEOGenEtcSourceCode | GEN_ETC_SOURCE_CODE | — | — |
| 117 | TaskStructureBasePEOIcClinElementId | IC_CLIN_ELEMENT_ID | — | — |
| 118 | TaskStructureBasePEOIssueId | ISSUE_ID | — | — |
| 119 | TaskStructureBasePEOLaborCostMultiplierName | LABOR_COST_MULTIPLIER_NAME | — | — |
| 120 | TaskStructureBasePEOLaborTpFixedDate | LABOR_TP_FIXED_DATE | — | — |
| 121 | TaskStructureBasePEOLaborTpScheduleId | LABOR_TP_SCHEDULE_ID | — | — |
| 122 | TaskStructureBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 123 | TaskStructureBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 124 | TaskStructureBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 125 | TaskStructureBasePEOLastViewedDate | LAST_VIEWED_DATE | — | — |
| 126 | TaskStructureBasePEOLeafNodeFlag | LEAF_NODE_FLAG | — | — |
| 127 | TaskStructureBasePEOLimitToTxnControlsFlag | LIMIT_TO_TXN_CONTROLS_FLAG | — | — |
| 128 | TaskStructureBasePEOManagerPersonId | MANAGER_PERSON_ID | — | — |
| 129 | TaskStructureBasePEOMilestoneFlag | MILESTONE_FLAG | — | — |
| 130 | TaskStructureBasePEONlTpFixedDate | NL_TP_FIXED_DATE | — | — |
| 131 | TaskStructureBasePEONlTpScheduleId | NL_TP_SCHEDULE_ID | — | — |
| 132 | TaskStructureBasePEONumberAttr01 | NUMBER_ATTR01 | — | — |
| 133 | TaskStructureBasePEONumberAttr02 | NUMBER_ATTR02 | — | — |
| 134 | TaskStructureBasePEONumberAttr03 | NUMBER_ATTR03 | — | — |
| 135 | TaskStructureBasePEONumberAttr04 | NUMBER_ATTR04 | — | — |
| 136 | TaskStructureBasePEONumberAttr05 | NUMBER_ATTR05 | — | — |
| 137 | TaskStructureBasePEONumberAttr06 | NUMBER_ATTR06 | — | — |
| 138 | TaskStructureBasePEONumberAttr07 | NUMBER_ATTR07 | — | — |
| 139 | TaskStructureBasePEONumberAttr08 | NUMBER_ATTR08 | — | — |
| 140 | TaskStructureBasePEONumberAttr09 | NUMBER_ATTR09 | — | — |
| 141 | TaskStructureBasePEONumberAttr10 | NUMBER_ATTR10 | — | — |
| 142 | TaskStructureBasePEOObjectAssociationBitmap | OBJECT_ASSOCIATION_BITMAP | — | — |
| 143 | TaskStructureBasePEOObjectType | OBJECT_TYPE | — | — |
| 144 | TaskStructureBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 145 | TaskStructureBasePEOOvrCostIndRateSchId | OVR_COST_IND_RATE_SCH_ID | — | — |
| 146 | TaskStructureBasePEOParentStructureId | PARENT_STRUCTURE_ID | — | — |
| 147 | TaskStructureBasePEOPercentCompCalcMethod | PERCENT_COMP_CALC_METHOD | — | — |
| 148 | TaskStructureBasePEOPlanningDatesRollupFlag | PLANNING_DATES_ROLLUP_FLAG | — | — |
| 149 | TaskStructureBasePEOPlanningEndDate | PLANNING_END_DATE | — | — |
| 150 | TaskStructureBasePEOPlanningStartDate | PLANNING_START_DATE | — | — |
| 151 | TaskStructureBasePEOPmSourceCode | PM_SOURCE_CODE | — | — |
| 152 | TaskStructureBasePEOPmSourceReference | PM_SOURCE_REFERENCE | — | — |
| 153 | TaskStructureBasePEOPrimaryResourceId | PRIMARY_RESOURCE_ID | — | ✅ |
| 154 | TaskStructureBasePEOProjElementId | PROJ_ELEMENT_ID | — | ✅ |
| 155 | TaskStructureBasePEOProjectId | PROJECT_ID | — | — |
| 156 | TaskStructureBasePEOReceiveProjectInvoiceFlag | RECEIVE_PROJECT_INVOICE_FLAG | — | — |
| 157 | TaskStructureBasePEORetirementCostFlag | RETIREMENT_COST_FLAG | — | — |
| 158 | TaskStructureBasePEORqmtId | RQMT_ID | — | — |
| 159 | TaskStructureBasePEOServiceTypeCode | SERVICE_TYPE_CODE | — | — |
| 160 | TaskStructureBasePEOSiteUseId | SITE_USE_ID | — | — |
| 161 | TaskStructureBasePEOSprintId | SPRINT_ID | — | — |
| 162 | TaskStructureBasePEOStartDate | START_DATE | — | — |
| 163 | TaskStructureBasePEOStructureType | STRUCTURE_TYPE | — | — |
| 164 | TaskStructureBasePEOTaskCode01Id | TASK_CODE01_ID | — | — |
| 165 | TaskStructureBasePEOTaskCode02Id | TASK_CODE02_ID | — | — |
| 166 | TaskStructureBasePEOTaskCode03Id | TASK_CODE03_ID | — | — |
| 167 | TaskStructureBasePEOTaskCode04Id | TASK_CODE04_ID | — | — |
| 168 | TaskStructureBasePEOTaskCode05Id | TASK_CODE05_ID | — | — |
| 169 | TaskStructureBasePEOTaskCode06Id | TASK_CODE06_ID | — | — |
| 170 | TaskStructureBasePEOTaskCode07Id | TASK_CODE07_ID | — | — |
| 171 | TaskStructureBasePEOTaskCode08Id | TASK_CODE08_ID | — | — |
| 172 | TaskStructureBasePEOTaskCode09Id | TASK_CODE09_ID | — | — |
| 173 | TaskStructureBasePEOTaskCode10Id | TASK_CODE10_ID | — | — |
| 174 | TaskStructureBasePEOTaskCode11Id | TASK_CODE11_ID | — | — |
| 175 | TaskStructureBasePEOTaskCode12Id | TASK_CODE12_ID | — | — |
| 176 | TaskStructureBasePEOTaskCode13Id | TASK_CODE13_ID | — | — |
| 177 | TaskStructureBasePEOTaskCode14Id | TASK_CODE14_ID | — | — |
| 178 | TaskStructureBasePEOTaskCode15Id | TASK_CODE15_ID | — | — |
| 179 | TaskStructureBasePEOTaskCode16Id | TASK_CODE16_ID | — | — |
| 180 | TaskStructureBasePEOTaskCode17Id | TASK_CODE17_ID | — | — |
| 181 | TaskStructureBasePEOTaskCode18Id | TASK_CODE18_ID | — | — |
| 182 | TaskStructureBasePEOTaskCode19Id | TASK_CODE19_ID | — | — |
| 183 | TaskStructureBasePEOTaskCode20Id | TASK_CODE20_ID | — | — |
| 184 | TaskStructureBasePEOTaskCode21Id | TASK_CODE21_ID | — | — |
| 185 | TaskStructureBasePEOTaskCode22Id | TASK_CODE22_ID | — | — |
| 186 | TaskStructureBasePEOTaskCode23Id | TASK_CODE23_ID | — | — |
| 187 | TaskStructureBasePEOTaskCode24Id | TASK_CODE24_ID | — | — |
| 188 | TaskStructureBasePEOTaskCode25Id | TASK_CODE25_ID | — | — |
| 189 | TaskStructureBasePEOTaskCode26Id | TASK_CODE26_ID | — | — |
| 190 | TaskStructureBasePEOTaskCode27Id | TASK_CODE27_ID | — | — |
| 191 | TaskStructureBasePEOTaskCode28Id | TASK_CODE28_ID | — | — |
| 192 | TaskStructureBasePEOTaskCode29Id | TASK_CODE29_ID | — | — |
| 193 | TaskStructureBasePEOTaskCode30Id | TASK_CODE30_ID | — | — |
| 194 | TaskStructureBasePEOTaskCode31Id | TASK_CODE31_ID | — | — |
| 195 | TaskStructureBasePEOTaskCode32Id | TASK_CODE32_ID | — | — |
| 196 | TaskStructureBasePEOTaskCode33Id | TASK_CODE33_ID | — | — |
| 197 | TaskStructureBasePEOTaskCode34Id | TASK_CODE34_ID | — | — |
| 198 | TaskStructureBasePEOTaskCode35Id | TASK_CODE35_ID | — | — |
| 199 | TaskStructureBasePEOTaskCode36Id | TASK_CODE36_ID | — | — |
| 200 | TaskStructureBasePEOTaskCode37Id | TASK_CODE37_ID | — | — |
| 201 | TaskStructureBasePEOTaskCode38Id | TASK_CODE38_ID | — | — |
| 202 | TaskStructureBasePEOTaskCode39Id | TASK_CODE39_ID | — | — |
| 203 | TaskStructureBasePEOTaskCode40Id | TASK_CODE40_ID | — | — |
| 204 | TaskStructureBasePEOTaskStatusCode | TASK_STATUS_CODE | — | — |
| 205 | TaskStructureBasePEOTaskTypeCode | TASK_TYPE_CODE | — | — |
| 206 | TaskStructureBasePEOTextAttr01 | TEXT_ATTR01 | — | — |
| 207 | TaskStructureBasePEOTextAttr02 | TEXT_ATTR02 | — | — |
| 208 | TaskStructureBasePEOTextAttr03 | TEXT_ATTR03 | — | — |
| 209 | TaskStructureBasePEOTextAttr04 | TEXT_ATTR04 | — | — |
| 210 | TaskStructureBasePEOTextAttr05 | TEXT_ATTR05 | — | — |
| 211 | TaskStructureBasePEOTextAttr06 | TEXT_ATTR06 | — | — |
| 212 | TaskStructureBasePEOTextAttr07 | TEXT_ATTR07 | — | — |
| 213 | TaskStructureBasePEOTextAttr08 | TEXT_ATTR08 | — | — |
| 214 | TaskStructureBasePEOTextAttr09 | TEXT_ATTR09 | — | — |
| 215 | TaskStructureBasePEOTextAttr10 | TEXT_ATTR10 | — | — |
| 216 | TaskStructureBasePEOTextAttr11 | TEXT_ATTR11 | — | — |
| 217 | TaskStructureBasePEOTextAttr12 | TEXT_ATTR12 | — | — |
| 218 | TaskStructureBasePEOTextAttr13 | TEXT_ATTR13 | — | — |
| 219 | TaskStructureBasePEOTextAttr14 | TEXT_ATTR14 | — | — |
| 220 | TaskStructureBasePEOTextAttr15 | TEXT_ATTR15 | — | — |
| 221 | TaskStructureBasePEOTextAttr16 | TEXT_ATTR16 | — | — |
| 222 | TaskStructureBasePEOTextAttr17 | TEXT_ATTR17 | — | — |
| 223 | TaskStructureBasePEOTextAttr18 | TEXT_ATTR18 | — | — |
| 224 | TaskStructureBasePEOTextAttr19 | TEXT_ATTR19 | — | — |
| 225 | TaskStructureBasePEOTextAttr20 | TEXT_ATTR20 | — | — |
| 226 | TaskStructureBasePEOWorkTypeId | WORK_TYPE_ID | — | — |

### [[pjt_proj_plan_lines|PJT_PROJ_PLAN_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjPlanLinePEOActualExpenseCostAmount | ACTUAL_EXPENSE_COST_AMOUNT | — | — |
| 2 | ProjPlanLinePEOActualFinishDate | ACTUAL_FINISH_DATE | — | ✅ |
| 3 | ProjPlanLinePEOActualLaborBilledAmount | ACTUAL_LABOR_BILLED_AMOUNT | — | — |
| 4 | ProjPlanLinePEOActualLaborCostAmount | ACTUAL_LABOR_COST_AMOUNT | — | — |
| 5 | ProjPlanLinePEOActualQuantity | ACTUAL_QUANTITY | — | — |
| 6 | ProjPlanLinePEOActualStartDate | ACTUAL_START_DATE | — | ✅ |
| 7 | ProjPlanLinePEOApprovedDate | APPROVED_DATE | — | — |
| 8 | ProjPlanLinePEOAtCompletionFinishDate | AT_COMPLETION_FINISH_DATE | — | — |
| 9 | ProjPlanLinePEOAtCompletionLaborCost | AT_COMPLETION_LABOR_COST | — | — |
| 10 | ProjPlanLinePEOAtCompletionQuantity | AT_COMPLETION_QUANTITY | — | — |
| 11 | ProjPlanLinePEOAtCompletionStartDate | AT_COMPLETION_START_DATE | — | — |
| 12 | ProjPlanLinePEOBaselineAllocation | BASELINE_ALLOCATION | — | — |
| 13 | ProjPlanLinePEOBaselineDuration | BASELINE_DURATION | — | — |
| 14 | ProjPlanLinePEOBaselineExpenseCostAmount | BASELINE_EXPENSE_COST_AMOUNT | — | — |
| 15 | ProjPlanLinePEOBaselineFinishDate | BASELINE_FINISH_DATE | — | — |
| 16 | ProjPlanLinePEOBaselineLaborBilledAmount | BASELINE_LABOR_BILLED_AMOUNT | — | — |
| 17 | ProjPlanLinePEOBaselineLaborCostAmount | BASELINE_LABOR_COST_AMOUNT | — | — |
| 18 | ProjPlanLinePEOBaselineQuantity | BASELINE_QUANTITY | — | — |
| 19 | ProjPlanLinePEOBaselineStartDate | BASELINE_START_DATE | — | — |
| 20 | ProjPlanLinePEOCostPercentComplete | COST_PERCENT_COMPLETE | — | — |
| 21 | ProjPlanLinePEOCreatedBy | CREATED_BY | — | — |
| 22 | ProjPlanLinePEOCreationDate | CREATION_DATE | — | — |
| 23 | ProjPlanLinePEODenormResourceClass | DENORM_RESOURCE_CLASS | — | — |
| 24 | ProjPlanLinePEODuration | DURATION | — | — |
| 25 | ProjPlanLinePEOElementVersionId | ELEMENT_VERSION_ID | — | — |
| 26 | ProjPlanLinePEOExpenseCostAmount | EXPENSE_COST_AMOUNT | — | — |
| 27 | ProjPlanLinePEOFinishDate | FINISH_DATE | — | ✅ |
| 28 | ProjPlanLinePEOGateStatusCode | GATE_STATUS_CODE | — | — |
| 29 | ProjPlanLinePEOHealthStsCode | HEALTH_STS_CODE | — | — |
| 30 | ProjPlanLinePEOId | ID | — | — |
| 31 | ProjPlanLinePEOInitiatedDate | INITIATED_DATE | — | — |
| 32 | ProjPlanLinePEOItdQuantity | ITD_QUANTITY | — | ✅ |
| 33 | ProjPlanLinePEOLaborBilledAmount | LABOR_BILLED_AMOUNT | — | — |
| 34 | ProjPlanLinePEOLaborCostAmount | LABOR_COST_AMOUNT | — | — |
| 35 | ProjPlanLinePEOLastCommentDate | LAST_COMMENT_DATE | — | — |
| 36 | ProjPlanLinePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 37 | ProjPlanLinePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 38 | ProjPlanLinePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 39 | ProjPlanLinePEONumberOfExceptions | NUMBER_OF_EXCEPTIONS | — | — |
| 40 | ProjPlanLinePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 41 | ProjPlanLinePEOPercentComplete | PERCENT_COMPLETE | — | ✅ |
| 42 | ProjPlanLinePEOPersonId | PERSON_ID | — | — |
| 43 | ProjPlanLinePEOPhysicalPercentComplete | PHYSICAL_PERCENT_COMPLETE | — | — |
| 44 | ProjPlanLinePEOPlanLineId | PLAN_LINE_ID | — | — |
| 45 | ProjPlanLinePEOPlanLineTypeCode | PLAN_LINE_TYPE_CODE | — | — |
| 46 | ProjPlanLinePEOPlanVersionId | PLAN_VERSION_ID | — | — |
| 47 | ProjPlanLinePEOPmPlanProgressRef | PM_PLAN_PROGRESS_REF | — | — |
| 48 | ProjPlanLinePEOPmProductCode | PM_PRODUCT_CODE | — | — |
| 49 | ProjPlanLinePEOPriority | PRIORITY | — | — |
| 50 | ProjPlanLinePEOProgressEnteredDate | PROGRESS_ENTERED_DATE | — | — |
| 51 | ProjPlanLinePEOProgressStatusCode | PROGRESS_STATUS_CODE | — | ✅ |
| 52 | ProjPlanLinePEOProjElementId | PROJ_ELEMENT_ID | — | — |
| 53 | ProjPlanLinePEOProjectId | PROJECT_ID | — | ✅ |
| 54 | ProjPlanLinePEOProposedDuration | PROPOSED_DURATION | — | — |
| 55 | ProjPlanLinePEOProposedFinishDate | PROPOSED_FINISH_DATE | — | — |
| 56 | ProjPlanLinePEOProposedQuantity | PROPOSED_QUANTITY | — | ✅ |
| 57 | ProjPlanLinePEOProposedResAllocation | PROPOSED_RES_ALLOCATION | — | — |
| 58 | ProjPlanLinePEOProposedStartDate | PROPOSED_START_DATE | — | — |
| 59 | ProjPlanLinePEOQuantity | QUANTITY | — | ✅ |
| 60 | ProjPlanLinePEORemainingExpenseCostAmount | REMAINING_EXPENSE_COST_AMOUNT | — | — |
| 61 | ProjPlanLinePEORemainingLaborBilledAmount | REMAINING_LABOR_BILLED_AMOUNT | — | — |
| 62 | ProjPlanLinePEORemainingLaborCostAmount | REMAINING_LABOR_COST_AMOUNT | — | — |
| 63 | ProjPlanLinePEORemainingQuantity | REMAINING_QUANTITY | — | ✅ |
| 64 | ProjPlanLinePEOResourceAllocationPercent | RESOURCE_ALLOCATION_PERCENT | — | — |
| 65 | ProjPlanLinePEOResourceId | RESOURCE_ID | — | — |
| 66 | ProjPlanLinePEORollupFlag | ROLLUP_FLAG | — | — |
| 67 | ProjPlanLinePEORollupPlanLine | ROLLUP_PLAN_LINE | — | — |
| 68 | ProjPlanLinePEOStartDate | START_DATE | — | ✅ |
| 69 | ProjPlanLinePEOTotalActualCostAmount | TOTAL_ACTUAL_COST_AMOUNT | — | ✅ |
| 70 | ProjPlanLinePEOTotalCostAmount | TOTAL_COST_AMOUNT | — | ✅ |
| 71 | ProjPlanLinePEOTotalRemainingCostAmount | TOTAL_REMAINING_COST_AMOUNT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
