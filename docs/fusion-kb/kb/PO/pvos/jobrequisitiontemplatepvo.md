---
id: DOC-PO-PVO-JobRequisitionTemplatePVO
doc_type: system-doc
title: "JobRequisitionTemplatePVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - JobRequisitionTemplatePVO
  - jobrequisitiontemplatepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JobRequisitionTemplatePVO

## 📌 Visão Geral

Extrai templates de requisições de contratação pré-configurados, com critérios padrão e descrições de cargo. Agiliza a abertura de vagas e garante padronização no processo de hiring.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecHiringRequisitionAM.JobRequisitionTemplatePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 195 | 3 | 1 | 43 | 22% |

---

## 🔗 Tabelas Relacionadas

- [[ff_formulas_vl|FF_FORMULAS_VL]] — 2 atributos (1 BICC)
- [[irc_requisitions_b|IRC_REQUISITIONS_B]] — 167 atributos (1 PKs, 34 BICC)
- [[irc_requisitions_tl|IRC_REQUISITIONS_TL]] — 26 atributos (8 BICC)

---

## ⚙️ Atributos

### [[ff_formulas_vl|FF_FORMULAS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequisitionFastFormulaPEOFormulaId | FORMULA_ID | — | — |
| 2 | RequisitionFastFormulaPEOFormulaName | FORMULA_NAME | — | ✅ |

### [[irc_requisitions_b|IRC_REQUISITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApprovedDate | APPROVED_DATE | — | — |
| 2 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 3 | AttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 4 | AttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 5 | AttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 6 | AttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 7 | AttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 8 | AttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 9 | AttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 10 | AttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 11 | AttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 12 | AttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 13 | AttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 14 | AttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 15 | AttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 16 | AttributeChar21 | ATTRIBUTE_CHAR21 | — | — |
| 17 | AttributeChar22 | ATTRIBUTE_CHAR22 | — | — |
| 18 | AttributeChar23 | ATTRIBUTE_CHAR23 | — | — |
| 19 | AttributeChar24 | ATTRIBUTE_CHAR24 | — | — |
| 20 | AttributeChar25 | ATTRIBUTE_CHAR25 | — | — |
| 21 | AttributeChar26 | ATTRIBUTE_CHAR26 | — | — |
| 22 | AttributeChar27 | ATTRIBUTE_CHAR27 | — | — |
| 23 | AttributeChar28 | ATTRIBUTE_CHAR28 | — | — |
| 24 | AttributeChar29 | ATTRIBUTE_CHAR29 | — | — |
| 25 | AttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 26 | AttributeChar30 | ATTRIBUTE_CHAR30 | — | — |
| 27 | AttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 28 | AttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 29 | AttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 30 | AttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 31 | AttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 32 | AttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 33 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 34 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 35 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 36 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 37 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 38 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 39 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 40 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 41 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 42 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 43 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 44 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 45 | AttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 46 | AttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 47 | AttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 48 | AttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 49 | AttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 50 | AttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 51 | AttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 52 | AttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 53 | AttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 54 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 55 | AttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 56 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 57 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 58 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 59 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 60 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 61 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 62 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 63 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 64 | AttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 65 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 66 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 67 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 68 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 69 | AttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 70 | AttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 71 | AttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 72 | AttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 73 | BudgetCurrencyCode | BUDGET_CURRENCY_CODE | — | ✅ |
| 74 | BusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 75 | Comments | COMMENTS | — | — |
| 76 | CreatedBy | CREATED_BY | — | ✅ |
| 77 | CreationDate | CREATION_DATE | — | ✅ |
| 78 | CurrentPhaseId | CURRENT_PHASE_ID | — | — |
| 79 | CurrentStateId | CURRENT_STATE_ID | — | — |
| 80 | DepartmentId | DEPARTMENT_ID | — | — |
| 81 | DisplayInOrgChartFlag | DISPLAY_IN_ORG_CHART_FLAG | — | — |
| 82 | EmployeeReferralBonus | EMPLOYEE_REFERRAL_BONUS | — | ✅ |
| 83 | ExtContactEmail | EXT_CONTACT_EMAIL | — | ✅ |
| 84 | ExtContactName | EXT_CONTACT_NAME | — | ✅ |
| 85 | ExtEmployerDescId | EXT_EMPLOYER_DESC_ID | — | — |
| 86 | ExtFirstPostedDate | EXT_FIRST_POSTED_DATE | — | — |
| 87 | ExtOrganizationDescId | EXT_ORGANIZATION_DESC_ID | — | — |
| 88 | ExtPublishJobEndDate | EXT_PUBLISH_JOB_END_DATE | — | — |
| 89 | ExtPublishJobStartDate | EXT_PUBLISH_JOB_START_DATE | — | — |
| 90 | ExtPublishJobStatus | EXT_PUBLISH_JOB_STATUS | — | — |
| 91 | FilledDate | FILLED_DATE | — | — |
| 92 | FullPartTime | FULL_PART_TIME | — | ✅ |
| 93 | GeographyId | GEOGRAPHY_ID | — | — |
| 94 | GeographyNodeId | GEOGRAPHY_NODE_ID | — | — |
| 95 | GradeId | GRADE_ID | — | — |
| 96 | HiredCount | HIRED_COUNT | — | — |
| 97 | HiringManagerId | HIRING_MANAGER_ID | — | — |
| 98 | IntContactEmail | INT_CONTACT_EMAIL | — | ✅ |
| 99 | IntContactName | INT_CONTACT_NAME | — | ✅ |
| 100 | IntEmployerDescId | INT_EMPLOYER_DESC_ID | — | — |
| 101 | IntFirstPostedDate | INT_FIRST_POSTED_DATE | — | — |
| 102 | IntOrganizationDescId | INT_ORGANIZATION_DESC_ID | — | — |
| 103 | IntPublishJobEndDate | INT_PUBLISH_JOB_END_DATE | — | — |
| 104 | IntPublishJobStartDate | INT_PUBLISH_JOB_START_DATE | — | — |
| 105 | IntPublishJobStatus | INT_PUBLISH_JOB_STATUS | — | — |
| 106 | JobFamilyId | JOB_FAMILY_ID | — | — |
| 107 | JobFunctionCode | JOB_FUNCTION_CODE | — | ✅ |
| 108 | JobId | JOB_ID | — | — |
| 109 | JobShiftCode | JOB_SHIFT_CODE | — | ✅ |
| 110 | JobTypeCode | JOB_TYPE_CODE | — | ✅ |
| 111 | JustificationCode | JUSTIFICATION_CODE | — | — |
| 112 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 113 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 114 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 115 | LegalEmployerId | LEGAL_EMPLOYER_ID | — | — |
| 116 | LocationId | LOCATION_ID | — | — |
| 117 | ManagerAssignmentId | MANAGER_ASSIGNMENT_ID | — | — |
| 118 | ManagerLevel | MANAGER_LEVEL | — | ✅ |
| 119 | MaxSalary | MAX_SALARY | — | ✅ |
| 120 | MinSalary | MIN_SALARY | — | ✅ |
| 121 | NumberToHire | NUMBER_TO_HIRE | — | — |
| 122 | ObjectStatus | OBJECT_STATUS | — | ✅ |
| 123 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 124 | OrganizationId | ORGANIZATION_ID | — | — |
| 125 | PipelineRequisitionBPEORequisitionId | REQUISITION_ID | — | — |
| 126 | PipelineRequisitionBPEORequisitionNumber | REQUISITION_NUMBER | — | — |
| 127 | ProfileId | PROFILE_ID | — | — |
| 128 | RecruiterAssignmentId | RECRUITER_ASSIGNMENT_ID | — | — |
| 129 | RecruiterId | RECRUITER_ID | — | — |
| 130 | RecruitingTypeCode | RECRUITING_TYPE_CODE | — | ✅ |
| 131 | RegularTemporary | REGULAR_TEMPORARY | — | ✅ |
| 132 | RelocationBudget | RELOCATION_BUDGET | — | — |
| 133 | ReqLastModifiedDate | REQ_LAST_MODIFIED_DATE | — | — |
| 134 | ReqUsageCode | REQ_USAGE_CODE | — | ✅ |
| 135 | RequisitionBPEOApplyWhenNotPostedIndicator | APPLY_WHEN_NOT_POSTED_FLAG | — | — |
| 136 | RequisitionBPEOAutoOpenRequisition | AUTO_OPEN_REQUISITION | — | ✅ |
| 137 | RequisitionBPEOAutoUnpostRequisition | AUTO_UNPOST_REQUISITION | — | ✅ |
| 138 | RequisitionBPEOAutomaticFillFlag | AUTOMATIC_FILL_FLAG | — | ✅ |
| 139 | RequisitionBPEOExternalApplyFlowId | EXTERNAL_APPLY_FLOW_ID | — | — |
| 140 | RequisitionBPEOExternalDescriptionId | EXTERNAL_DESCRIPTION_ID | — | ✅ |
| 141 | RequisitionBPEOHotJobFlag | HOT_JOB_FLAG | — | — |
| 142 | RequisitionBPEOInternalDescriptionId | INTERNAL_DESCRIPTION_ID | — | ✅ |
| 143 | RequisitionBPEOOpenDate | OPEN_DATE | — | — |
| 144 | RequisitionBPEOPipelineRequisitionFlag | PIPELINE_REQUISITION_FLAG | — | — |
| 145 | RequisitionBPEOPipelineRequisitionId | PIPELINE_REQUISITION_ID | — | — |
| 146 | RequisitionBPEOPositionId | POSITION_ID | — | — |
| 147 | RequisitionBPEOPostingExpireInDays | POSTING_EXPIRE_IN_DAYS | — | ✅ |
| 148 | RequisitionBPEOProcessId | PROCESS_ID | — | — |
| 149 | RequisitionBPEOReqSourceType | REQ_SOURCE_TYPE | — | — |
| 150 | RequisitionBPEOReqUsageType | REQ_USAGE_TYPE | — | ✅ |
| 151 | RequisitionBPEOSalaryPeriodCode | SALARY_PERIOD_CODE | — | — |
| 152 | RequisitionBPEOSubsProcessTemplateId | SUBS_PROCESS_TEMPLATE_ID | — | — |
| 153 | RequisitionBPEOUnpostFormulaId | UNPOST_FORMULA_ID | — | ✅ |
| 154 | RequisitionBPEOWorkEndDate | WORK_END_DATE | — | — |
| 155 | RequisitionBPEOWorkStartDate | WORK_START_DATE | — | — |
| 156 | RequisitionBPEOWorkplaceTypeCode | WORKPLACE_TYPE_CODE | — | — |
| 157 | RequisitionId | REQUISITION_ID | 🔑 | ✅ |
| 158 | RequisitionNumber | REQUISITION_NUMBER | — | ✅ |
| 159 | RequisitionTemplateId | REQUISITION_TEMPLATE_ID | — | — |
| 160 | SalaryCurrencyCode | SALARY_CURRENCY_CODE | — | ✅ |
| 161 | SalaryFrequencyCode | SALARY_FREQUENCY_CODE | — | ✅ |
| 162 | SourcingBudget | SOURCING_BUDGET | — | — |
| 163 | StudyLevelCode | STUDY_LEVEL_CODE | — | ✅ |
| 164 | SuspendedDuration | SUSPENDED_DURATION | — | — |
| 165 | TravelBudget | TRAVEL_BUDGET | — | — |
| 166 | UnlimitedHireFlag | UNLIMITED_HIRE_FLAG | — | — |
| 167 | WorkerTypeCode | WORKER_TYPE_CODE | — | ✅ |

### [[irc_requisitions_tl|IRC_REQUISITIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy1 | CREATED_BY | — | — |
| 2 | CreationDate1 | CREATION_DATE | — | — |
| 3 | ExternalDesc | EXTERNAL_DESC | — | ✅ |
| 4 | ExternalDescHtml | EXTERNAL_DESC_HTML | — | — |
| 5 | ExternalShortDesc | EXTERNAL_SHORT_DESC | — | ✅ |
| 6 | InternalDesc | INTERNAL_DESC | — | ✅ |
| 7 | InternalDescHtml | INTERNAL_DESC_HTML | — | — |
| 8 | InternalShortDesc | INTERNAL_SHORT_DESC | — | ✅ |
| 9 | Language | LANGUAGE | — | — |
| 10 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 12 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 13 | ManagerTitle | MANAGER_TITLE | — | ✅ |
| 14 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 15 | PipelineRequisitionTLPEOLanguage | LANGUAGE | — | — |
| 16 | PipelineRequisitionTLPEORequisitionId | REQUISITION_ID | — | — |
| 17 | PipelineRequisitionTLPEOTitle | TITLE | — | — |
| 18 | RequisitionId1 | REQUISITION_ID | — | — |
| 19 | RequisitionTranslationPEOCustomExtPostDescFlag | CUSTOM_EXT_POST_DESC_FLAG | — | — |
| 20 | RequisitionTranslationPEOExternalQual | EXTERNAL_QUAL | — | — |
| 21 | RequisitionTranslationPEOExternalResp | EXTERNAL_RESP | — | — |
| 22 | RequisitionTranslationPEOInternalQual | INTERNAL_QUAL | — | — |
| 23 | RequisitionTranslationPEOInternalResp | INTERNAL_RESP | — | — |
| 24 | RequisitionTranslationPEOName | NAME | — | ✅ |
| 25 | SourceLang | SOURCE_LANG | — | — |
| 26 | Title | TITLE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
