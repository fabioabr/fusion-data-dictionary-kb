---
id: DOC-PO-PVO-RequisitionTemplatePVO
doc_type: system-doc
title: "RequisitionTemplatePVO — PVO Purchasing"
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
  - RequisitionTemplatePVO
  - requisitiontemplatepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RequisitionTemplatePVO

## 📌 Visão Geral

Extrai templates de requisições de contratação pré-configurados, com critérios padrão, fórmulas de elegibilidade e descrições de cargo. Agiliza a abertura de vagas e garante padronização.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecHiringRequisitionAM.RequisitionTemplatePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 177 | 3 | 1 | 18 | 10% |

---

## 🔗 Tabelas Relacionadas

- [[ff_formulas_vl|FF_FORMULAS_VL]] — 2 atributos (1 BICC)
- [[irc_requisitions_b|IRC_REQUISITIONS_B]] — 152 atributos (1 PKs, 14 BICC)
- [[irc_requisitions_tl|IRC_REQUISITIONS_TL]] — 23 atributos (3 BICC)

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
| 1 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | AttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 3 | AttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 4 | AttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 5 | AttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 6 | AttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 7 | AttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 8 | AttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 9 | AttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 10 | AttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 11 | AttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 12 | AttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 13 | AttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 14 | AttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 15 | AttributeChar21 | ATTRIBUTE_CHAR21 | — | — |
| 16 | AttributeChar22 | ATTRIBUTE_CHAR22 | — | — |
| 17 | AttributeChar23 | ATTRIBUTE_CHAR23 | — | — |
| 18 | AttributeChar24 | ATTRIBUTE_CHAR24 | — | — |
| 19 | AttributeChar25 | ATTRIBUTE_CHAR25 | — | — |
| 20 | AttributeChar26 | ATTRIBUTE_CHAR26 | — | — |
| 21 | AttributeChar27 | ATTRIBUTE_CHAR27 | — | — |
| 22 | AttributeChar28 | ATTRIBUTE_CHAR28 | — | — |
| 23 | AttributeChar29 | ATTRIBUTE_CHAR29 | — | — |
| 24 | AttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 25 | AttributeChar30 | ATTRIBUTE_CHAR30 | — | — |
| 26 | AttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 27 | AttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 28 | AttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 29 | AttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 30 | AttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 31 | AttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 32 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 33 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 34 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 35 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 36 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 37 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 38 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 39 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 40 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 41 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 42 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 43 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 44 | AttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 45 | AttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 46 | AttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 47 | AttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 48 | AttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 49 | AttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 50 | AttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 51 | AttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 52 | AttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 53 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 54 | AttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 55 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 56 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 57 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 58 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 59 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 60 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 61 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 62 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 63 | AttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 64 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 65 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 66 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 67 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 68 | AttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 69 | AttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 70 | AttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 71 | AttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 72 | BudgetCurrencyCode | BUDGET_CURRENCY_CODE | — | — |
| 73 | BusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 74 | Comments | COMMENTS | — | — |
| 75 | CreatedBy | CREATED_BY | — | ✅ |
| 76 | CreationDate | CREATION_DATE | — | ✅ |
| 77 | CurrentPhaseId | CURRENT_PHASE_ID | — | — |
| 78 | CurrentStateId | CURRENT_STATE_ID | — | — |
| 79 | DepartmentId | DEPARTMENT_ID | — | — |
| 80 | DisplayInOrgChartFlag | DISPLAY_IN_ORG_CHART_FLAG | — | — |
| 81 | EmployeeReferralBonus | EMPLOYEE_REFERRAL_BONUS | — | — |
| 82 | ExtContactEmail | EXT_CONTACT_EMAIL | — | — |
| 83 | ExtContactName | EXT_CONTACT_NAME | — | — |
| 84 | ExtEmployerDescId | EXT_EMPLOYER_DESC_ID | — | — |
| 85 | ExtOrganizationDescId | EXT_ORGANIZATION_DESC_ID | — | — |
| 86 | ExtPublishJobEndDate | EXT_PUBLISH_JOB_END_DATE | — | — |
| 87 | ExtPublishJobStartDate | EXT_PUBLISH_JOB_START_DATE | — | — |
| 88 | ExtPublishJobStatus | EXT_PUBLISH_JOB_STATUS | — | — |
| 89 | ExternalApplyFlowId | EXTERNAL_APPLY_FLOW_ID | — | — |
| 90 | FullPartTime | FULL_PART_TIME | — | — |
| 91 | GeographyId | GEOGRAPHY_ID | — | — |
| 92 | GeographyNodeId | GEOGRAPHY_NODE_ID | — | — |
| 93 | GradeId | GRADE_ID | — | — |
| 94 | HiredCount | HIRED_COUNT | — | — |
| 95 | HiringManagerId | HIRING_MANAGER_ID | — | — |
| 96 | IntContactEmail | INT_CONTACT_EMAIL | — | — |
| 97 | IntContactName | INT_CONTACT_NAME | — | — |
| 98 | IntEmployerDescId | INT_EMPLOYER_DESC_ID | — | — |
| 99 | IntOrganizationDescId | INT_ORGANIZATION_DESC_ID | — | — |
| 100 | IntPublishJobEndDate | INT_PUBLISH_JOB_END_DATE | — | — |
| 101 | IntPublishJobStartDate | INT_PUBLISH_JOB_START_DATE | — | — |
| 102 | IntPublishJobStatus | INT_PUBLISH_JOB_STATUS | — | — |
| 103 | JobFamilyId | JOB_FAMILY_ID | — | — |
| 104 | JobFunctionCode | JOB_FUNCTION_CODE | — | — |
| 105 | JobId | JOB_ID | — | — |
| 106 | JobShiftCode | JOB_SHIFT_CODE | — | — |
| 107 | JobTypeCode | JOB_TYPE_CODE | — | — |
| 108 | JustificationCode | JUSTIFICATION_CODE | — | — |
| 109 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 110 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 111 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 112 | LegalEmployerId | LEGAL_EMPLOYER_ID | — | — |
| 113 | LocationId | LOCATION_ID | — | — |
| 114 | ManagerAssignmentId | MANAGER_ASSIGNMENT_ID | — | — |
| 115 | ManagerLevel | MANAGER_LEVEL | — | — |
| 116 | MaxSalary | MAX_SALARY | — | — |
| 117 | MinSalary | MIN_SALARY | — | — |
| 118 | NumberToHire | NUMBER_TO_HIRE | — | — |
| 119 | ObjectStatus | OBJECT_STATUS | — | — |
| 120 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 121 | OrganizationId | ORGANIZATION_ID | — | — |
| 122 | ProcessId | PROCESS_ID | — | — |
| 123 | ProfileId | PROFILE_ID | — | — |
| 124 | RecruiterAssignmentId | RECRUITER_ASSIGNMENT_ID | — | — |
| 125 | RecruiterId | RECRUITER_ID | — | — |
| 126 | RecruitingTypeCode | RECRUITING_TYPE_CODE | — | ✅ |
| 127 | RegularTemporary | REGULAR_TEMPORARY | — | — |
| 128 | RelocationBudget | RELOCATION_BUDGET | — | — |
| 129 | ReqLastModifiedDate | REQ_LAST_MODIFIED_DATE | — | — |
| 130 | ReqUsageCode | REQ_USAGE_CODE | — | ✅ |
| 131 | RequisitionBPEOAutoOpenRequisition | AUTO_OPEN_REQUISITION | — | ✅ |
| 132 | RequisitionBPEOAutoUnpostRequisition | AUTO_UNPOST_REQUISITION | — | ✅ |
| 133 | RequisitionBPEOAutomaticFillFlag | AUTOMATIC_FILL_FLAG | — | — |
| 134 | RequisitionBPEOExternalDescriptionId | EXTERNAL_DESCRIPTION_ID | — | ✅ |
| 135 | RequisitionBPEOInternalDescriptionId | INTERNAL_DESCRIPTION_ID | — | ✅ |
| 136 | RequisitionBPEOPostingExpireInDays | POSTING_EXPIRE_IN_DAYS | — | ✅ |
| 137 | RequisitionBPEOReqUsageType | REQ_USAGE_TYPE | — | ✅ |
| 138 | RequisitionBPEOSalaryPeriodCode | SALARY_PERIOD_CODE | — | — |
| 139 | RequisitionBPEOUnpostFormulaId | UNPOST_FORMULA_ID | — | ✅ |
| 140 | RequisitionBPEOWorkEndDate | WORK_END_DATE | — | — |
| 141 | RequisitionBPEOWorkStartDate | WORK_START_DATE | — | — |
| 142 | RequisitionId | REQUISITION_ID | 🔑 | ✅ |
| 143 | RequisitionNumber | REQUISITION_NUMBER | — | ✅ |
| 144 | RequisitionTemplateId | REQUISITION_TEMPLATE_ID | — | — |
| 145 | SalaryCurrencyCode | SALARY_CURRENCY_CODE | — | — |
| 146 | SalaryFrequencyCode | SALARY_FREQUENCY_CODE | — | — |
| 147 | SourcingBudget | SOURCING_BUDGET | — | — |
| 148 | StudyLevelCode | STUDY_LEVEL_CODE | — | — |
| 149 | SubsProcessTemplateId | SUBS_PROCESS_TEMPLATE_ID | — | — |
| 150 | TravelBudget | TRAVEL_BUDGET | — | — |
| 151 | UnlimitedHireFlag | UNLIMITED_HIRE_FLAG | — | — |
| 152 | WorkerTypeCode | WORKER_TYPE_CODE | — | — |

### [[irc_requisitions_tl|IRC_REQUISITIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy1 | CREATED_BY | — | — |
| 2 | CreationDate1 | CREATION_DATE | — | — |
| 3 | ExternalDesc | EXTERNAL_DESC | — | — |
| 4 | ExternalDescHtml | EXTERNAL_DESC_HTML | — | — |
| 5 | ExternalShortDesc | EXTERNAL_SHORT_DESC | — | — |
| 6 | InternalDesc | INTERNAL_DESC | — | — |
| 7 | InternalDescHtml | INTERNAL_DESC_HTML | — | — |
| 8 | InternalShortDesc | INTERNAL_SHORT_DESC | — | — |
| 9 | Language1 | LANGUAGE | — | — |
| 10 | LastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 11 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 12 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 13 | ManagerTitle | MANAGER_TITLE | — | ✅ |
| 14 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 15 | RequisitionId1 | REQUISITION_ID | — | — |
| 16 | RequisitionTranslationPEOCustomExtPostDescFlag | CUSTOM_EXT_POST_DESC_FLAG | — | — |
| 17 | RequisitionTranslationPEOExternalQual | EXTERNAL_QUAL | — | — |
| 18 | RequisitionTranslationPEOExternalResp | EXTERNAL_RESP | — | — |
| 19 | RequisitionTranslationPEOInternalQual | INTERNAL_QUAL | — | — |
| 20 | RequisitionTranslationPEOInternalResp | INTERNAL_RESP | — | — |
| 21 | RequisitionTranslationPEOName | NAME | — | ✅ |
| 22 | SourceLang | SOURCE_LANG | — | — |
| 23 | Title | TITLE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
