---
id: DOC-GL-PVO-ScheduleAssignmentPVO
doc_type: system-doc
title: "ScheduleAssignmentPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ScheduleAssignmentPVO
  - scheduleassignmentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ScheduleAssignmentPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Schedule Assignment. Acessa as tabelas: PER_ALL_ASSIGNMENTS_M, PER_SCHEDULE_ASSIGNMENTS, ZMM_SR_PATTERNS_B (+4).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.WorkScheduleAM.ScheduleAssignmentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 246 | 7 | 1 | 18 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 109 atributos (2 BICC)
- [[per_schedule_assignments|PER_SCHEDULE_ASSIGNMENTS]] — 15 atributos (1 PKs, 9 BICC)
- [[zmm_sr_patterns_b|ZMM_SR_PATTERNS_B]] — 42 atributos (1 BICC)
- [[zmm_sr_patterns_tl|ZMM_SR_PATTERNS_TL]] — 11 atributos (2 BICC)
- [[zmm_sr_pattern_dtls|ZMM_SR_PATTERN_DTLS]] — 44 atributos (1 BICC)
- [[zmm_sr_schedules_b|ZMM_SR_SCHEDULES_B]] — 14 atributos (1 BICC)
- [[zmm_sr_schedules_tl|ZMM_SR_SCHEDULES_TL]] — 11 atributos (2 BICC)

---

## ⚙️ Atributos

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentPEOActionCode | ACTION_CODE | — | — |
| 2 | AssignmentPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 3 | AssignmentPEOAllowAsgOverrideFlag | ALLOW_ASG_OVERRIDE_FLAG | — | — |
| 4 | AssignmentPEOApplicantRank | APPLICANT_RANK | — | — |
| 5 | AssignmentPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 6 | AssignmentPEOAssignmentName | ASSIGNMENT_NAME | — | — |
| 7 | AssignmentPEOAssignmentNumber | ASSIGNMENT_NUMBER | — | — |
| 8 | AssignmentPEOAssignmentSequence | ASSIGNMENT_SEQUENCE | — | — |
| 9 | AssignmentPEOAssignmentStatusType | ASSIGNMENT_STATUS_TYPE | — | — |
| 10 | AssignmentPEOAssignmentStatusTypeId | ASSIGNMENT_STATUS_TYPE_ID | — | — |
| 11 | AssignmentPEOAssignmentType | ASSIGNMENT_TYPE | — | — |
| 12 | AssignmentPEOAutoEndFlag | AUTO_END_FLAG | — | — |
| 13 | AssignmentPEOBargainingUnitCode | BARGAINING_UNIT_CODE | — | — |
| 14 | AssignmentPEOBillingTitle | BILLING_TITLE | — | — |
| 15 | AssignmentPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 16 | AssignmentPEOBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 17 | AssignmentPEOCagrGradeDefId | CAGR_GRADE_DEF_ID | — | — |
| 18 | AssignmentPEOCagrIdFlexNum | CAGR_ID_FLEX_NUM | — | — |
| 19 | AssignmentPEOCollectiveAgreementId | COLLECTIVE_AGREEMENT_ID | — | — |
| 20 | AssignmentPEOContractId | CONTRACT_ID | — | — |
| 21 | AssignmentPEOCreatedBy | CREATED_BY | — | — |
| 22 | AssignmentPEOCreationDate | CREATION_DATE | — | — |
| 23 | AssignmentPEODateProbationEnd | DATE_PROBATION_END | — | — |
| 24 | AssignmentPEODefaultCodeCombId | DEFAULT_CODE_COMB_ID | — | — |
| 25 | AssignmentPEODutiesType | DUTIES_TYPE | — | — |
| 26 | AssignmentPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 27 | AssignmentPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 28 | AssignmentPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 29 | AssignmentPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 30 | AssignmentPEOEmployeeCategory | EMPLOYEE_CATEGORY | — | — |
| 31 | AssignmentPEOEmploymentCategory | EMPLOYMENT_CATEGORY | — | — |
| 32 | AssignmentPEOEstablishmentId | ESTABLISHMENT_ID | — | — |
| 33 | AssignmentPEOExpenseCheckAddress | EXPENSE_CHECK_ADDRESS | — | — |
| 34 | AssignmentPEOFreezeStartDate | FREEZE_START_DATE | — | — |
| 35 | AssignmentPEOFreezeUntilDate | FREEZE_UNTIL_DATE | — | — |
| 36 | AssignmentPEOFrequency | FREQUENCY | — | — |
| 37 | AssignmentPEOFullPartTime | FULL_PART_TIME | — | — |
| 38 | AssignmentPEOGradeId | GRADE_ID | — | — |
| 39 | AssignmentPEOGradeLadderPgmId | GRADE_LADDER_PGM_ID | — | — |
| 40 | AssignmentPEOHourlySalariedCode | HOURLY_SALARIED_CODE | — | — |
| 41 | AssignmentPEOIdFlexNum | ID_FLEX_NUM | — | — |
| 42 | AssignmentPEOInternalBuilding | INTERNAL_BUILDING | — | — |
| 43 | AssignmentPEOInternalFloor | INTERNAL_FLOOR | — | — |
| 44 | AssignmentPEOInternalLocation | INTERNAL_LOCATION | — | — |
| 45 | AssignmentPEOInternalMailstop | INTERNAL_MAILSTOP | — | — |
| 46 | AssignmentPEOInternalOfficeNumber | INTERNAL_OFFICE_NUMBER | — | — |
| 47 | AssignmentPEOJobId | JOB_ID | — | — |
| 48 | AssignmentPEOJobPostSourceName | JOB_POST_SOURCE_NAME | — | — |
| 49 | AssignmentPEOLabourUnionMemberFlag | LABOUR_UNION_MEMBER_FLAG | — | — |
| 50 | AssignmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 51 | AssignmentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 52 | AssignmentPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 53 | AssignmentPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 54 | AssignmentPEOLegislationCode | LEGISLATION_CODE | — | — |
| 55 | AssignmentPEOLinkageType | LINKAGE_TYPE | — | — |
| 56 | AssignmentPEOLocationId | LOCATION_ID | — | — |
| 57 | AssignmentPEOManagerFlag | MANAGER_FLAG | — | — |
| 58 | AssignmentPEONormalHours | NORMAL_HOURS | — | — |
| 59 | AssignmentPEONoticePeriod | NOTICE_PERIOD | — | — |
| 60 | AssignmentPEONoticePeriodUom | NOTICE_PERIOD_UOM | — | — |
| 61 | AssignmentPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 62 | AssignmentPEOOrganizationId | ORGANIZATION_ID | — | — |
| 63 | AssignmentPEOParentAssignmentId | PARENT_ASSIGNMENT_ID | — | — |
| 64 | AssignmentPEOPeopleGroupId | PEOPLE_GROUP_ID | — | — |
| 65 | AssignmentPEOPeriodOfServiceId | PERIOD_OF_SERVICE_ID | — | — |
| 66 | AssignmentPEOPermanentTemporaryFlag | PERMANENT_TEMPORARY_FLAG | — | — |
| 67 | AssignmentPEOPersonId | PERSON_ID | — | — |
| 68 | AssignmentPEOPersonReferredById | PERSON_REFERRED_BY_ID | — | — |
| 69 | AssignmentPEOPersonTypeId | PERSON_TYPE_ID | — | — |
| 70 | AssignmentPEOPoHeaderId | PO_HEADER_ID | — | — |
| 71 | AssignmentPEOPoLineId | PO_LINE_ID | — | — |
| 72 | AssignmentPEOPositionId | POSITION_ID | — | — |
| 73 | AssignmentPEOPositionOverrideFlag | POSITION_OVERRIDE_FLAG | — | — |
| 74 | AssignmentPEOPostingContentId | POSTING_CONTENT_ID | — | — |
| 75 | AssignmentPEOPrimaryAssignmentFlag | PRIMARY_ASSIGNMENT_FLAG | — | — |
| 76 | AssignmentPEOPrimaryFlag | PRIMARY_FLAG | — | — |
| 77 | AssignmentPEOPrimaryWorkRelationFlag | PRIMARY_WORK_RELATION_FLAG | — | — |
| 78 | AssignmentPEOPrimaryWorkTermsFlag | PRIMARY_WORK_TERMS_FLAG | — | — |
| 79 | AssignmentPEOProbationPeriod | PROBATION_PERIOD | — | — |
| 80 | AssignmentPEOProbationUnit | PROBATION_UNIT | — | — |
| 81 | AssignmentPEOProjectTitle | PROJECT_TITLE | — | — |
| 82 | AssignmentPEOProjectedAssignmentEnd | PROJECTED_ASSIGNMENT_END | — | — |
| 83 | AssignmentPEOProjectedStartDate | PROJECTED_START_DATE | — | — |
| 84 | AssignmentPEOProposedWorkerType | PROPOSED_WORKER_TYPE | — | — |
| 85 | AssignmentPEOReasonCode | REASON_CODE | — | — |
| 86 | AssignmentPEORecordCreator | RECORD_CREATOR | — | — |
| 87 | AssignmentPEORecruiterId | RECRUITER_ID | — | — |
| 88 | AssignmentPEORecruitmentActivityId | RECRUITMENT_ACTIVITY_ID | — | — |
| 89 | AssignmentPEORetirementAge | RETIREMENT_AGE | — | — |
| 90 | AssignmentPEORetirementDate | RETIREMENT_DATE | — | — |
| 91 | AssignmentPEOSalReviewPeriod | SAL_REVIEW_PERIOD | — | — |
| 92 | AssignmentPEOSalReviewPeriodFrequency | SAL_REVIEW_PERIOD_FREQUENCY | — | — |
| 93 | AssignmentPEOSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 94 | AssignmentPEOSoftCodingKeyflexId | SOFT_CODING_KEYFLEX_ID | — | — |
| 95 | AssignmentPEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 96 | AssignmentPEOSourceType | SOURCE_TYPE | — | — |
| 97 | AssignmentPEOSpecialCeilingStepId | SPECIAL_CEILING_STEP_ID | — | — |
| 98 | AssignmentPEOStepEntryDate | STEP_ENTRY_DATE | — | — |
| 99 | AssignmentPEOSystemPersonType | SYSTEM_PERSON_TYPE | — | — |
| 100 | AssignmentPEOTaxAddressId | TAX_ADDRESS_ID | — | — |
| 101 | AssignmentPEOTimeNormalFinish | TIME_NORMAL_FINISH | — | — |
| 102 | AssignmentPEOTimeNormalStart | TIME_NORMAL_START | — | — |
| 103 | AssignmentPEOVacancyId | VACANCY_ID | — | — |
| 104 | AssignmentPEOVendorAssignmentNumber | VENDOR_ASSIGNMENT_NUMBER | — | — |
| 105 | AssignmentPEOVendorEmployeeNumber | VENDOR_EMPLOYEE_NUMBER | — | — |
| 106 | AssignmentPEOVendorId | VENDOR_ID | — | — |
| 107 | AssignmentPEOVendorSiteId | VENDOR_SITE_ID | — | — |
| 108 | AssignmentPEOWorkAtHome | WORK_AT_HOME | — | — |
| 109 | AssignmentPEOWorkTermsAssignmentId | WORK_TERMS_ASSIGNMENT_ID | — | — |

### [[per_schedule_assignments|PER_SCHEDULE_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ScheduleAssignmentPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ScheduleAssignmentPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ScheduleAssignmentPEOEndDate | END_DATE | — | ✅ |
| 4 | ScheduleAssignmentPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 5 | ScheduleAssignmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ScheduleAssignmentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ScheduleAssignmentPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ScheduleAssignmentPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ScheduleAssignmentPEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 10 | ScheduleAssignmentPEOResourceId | RESOURCE_ID | — | — |
| 11 | ScheduleAssignmentPEOResourceType | RESOURCE_TYPE | — | ✅ |
| 12 | ScheduleAssignmentPEOScheduleAssignmentId | SCHEDULE_ASSIGNMENT_ID | 🔑 | ✅ |
| 13 | ScheduleAssignmentPEOScheduleId | SCHEDULE_ID | — | — |
| 14 | ScheduleAssignmentPEOStartDate | START_DATE | — | ✅ |
| 15 | ScheduleAssignmentPEOStartPatternDtlId | START_PATTERN_DTL_ID | — | — |

### [[zmm_sr_patterns_b|ZMM_SR_PATTERNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PatternsPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | PatternsPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | PatternsPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | PatternsPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | PatternsPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | PatternsPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | PatternsPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | PatternsPEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | PatternsPEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | PatternsPEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | PatternsPEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | PatternsPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | PatternsPEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | PatternsPEOAttribute21 | ATTRIBUTE21 | — | — |
| 15 | PatternsPEOAttribute22 | ATTRIBUTE22 | — | — |
| 16 | PatternsPEOAttribute23 | ATTRIBUTE23 | — | — |
| 17 | PatternsPEOAttribute24 | ATTRIBUTE24 | — | — |
| 18 | PatternsPEOAttribute25 | ATTRIBUTE25 | — | — |
| 19 | PatternsPEOAttribute26 | ATTRIBUTE26 | — | — |
| 20 | PatternsPEOAttribute27 | ATTRIBUTE27 | — | — |
| 21 | PatternsPEOAttribute28 | ATTRIBUTE28 | — | — |
| 22 | PatternsPEOAttribute29 | ATTRIBUTE29 | — | — |
| 23 | PatternsPEOAttribute3 | ATTRIBUTE3 | — | — |
| 24 | PatternsPEOAttribute30 | ATTRIBUTE30 | — | — |
| 25 | PatternsPEOAttribute4 | ATTRIBUTE4 | — | — |
| 26 | PatternsPEOAttribute5 | ATTRIBUTE5 | — | — |
| 27 | PatternsPEOAttribute6 | ATTRIBUTE6 | — | — |
| 28 | PatternsPEOAttribute7 | ATTRIBUTE7 | — | — |
| 29 | PatternsPEOAttribute8 | ATTRIBUTE8 | — | — |
| 30 | PatternsPEOAttribute9 | ATTRIBUTE9 | — | — |
| 31 | PatternsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 32 | PatternsPEOCreatedBy | CREATED_BY | — | — |
| 33 | PatternsPEOCreationDate | CREATION_DATE | — | — |
| 34 | PatternsPEODeletedFlag | DELETED_FLAG | — | — |
| 35 | PatternsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 36 | PatternsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 37 | PatternsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 38 | PatternsPEOLengthDaysNum | LENGTH_DAYS_NUM | — | — |
| 39 | PatternsPEONumericDayFlag | NUMERIC_DAY_FLAG | — | — |
| 40 | PatternsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 41 | PatternsPEOPatternId | PATTERN_ID | — | — |
| 42 | PatternsPEOPatternTypeCode | PATTERN_TYPE_CODE | — | — |

### [[zmm_sr_patterns_tl|ZMM_SR_PATTERNS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PatternsTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | PatternsTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | PatternsTranslationPEOLanguage | LANGUAGE | — | — |
| 4 | PatternsTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PatternsTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | PatternsTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | PatternsTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | PatternsTranslationPEOPatternDesc | PATTERN_DESC | — | — |
| 9 | PatternsTranslationPEOPatternId | PATTERN_ID | — | — |
| 10 | PatternsTranslationPEOPatternName | PATTERN_NAME | — | ✅ |
| 11 | PatternsTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[zmm_sr_pattern_dtls|ZMM_SR_PATTERN_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PatternDetailsPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | PatternDetailsPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | PatternDetailsPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | PatternDetailsPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | PatternDetailsPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | PatternDetailsPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | PatternDetailsPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | PatternDetailsPEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | PatternDetailsPEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | PatternDetailsPEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | PatternDetailsPEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | PatternDetailsPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | PatternDetailsPEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | PatternDetailsPEOAttribute21 | ATTRIBUTE21 | — | — |
| 15 | PatternDetailsPEOAttribute22 | ATTRIBUTE22 | — | — |
| 16 | PatternDetailsPEOAttribute23 | ATTRIBUTE23 | — | — |
| 17 | PatternDetailsPEOAttribute24 | ATTRIBUTE24 | — | — |
| 18 | PatternDetailsPEOAttribute25 | ATTRIBUTE25 | — | — |
| 19 | PatternDetailsPEOAttribute26 | ATTRIBUTE26 | — | — |
| 20 | PatternDetailsPEOAttribute27 | ATTRIBUTE27 | — | — |
| 21 | PatternDetailsPEOAttribute28 | ATTRIBUTE28 | — | — |
| 22 | PatternDetailsPEOAttribute29 | ATTRIBUTE29 | — | — |
| 23 | PatternDetailsPEOAttribute3 | ATTRIBUTE3 | — | — |
| 24 | PatternDetailsPEOAttribute30 | ATTRIBUTE30 | — | — |
| 25 | PatternDetailsPEOAttribute4 | ATTRIBUTE4 | — | — |
| 26 | PatternDetailsPEOAttribute5 | ATTRIBUTE5 | — | — |
| 27 | PatternDetailsPEOAttribute6 | ATTRIBUTE6 | — | — |
| 28 | PatternDetailsPEOAttribute7 | ATTRIBUTE7 | — | — |
| 29 | PatternDetailsPEOAttribute8 | ATTRIBUTE8 | — | — |
| 30 | PatternDetailsPEOAttribute9 | ATTRIBUTE9 | — | — |
| 31 | PatternDetailsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 32 | PatternDetailsPEOChildPatternId | CHILD_PATTERN_ID | — | — |
| 33 | PatternDetailsPEOChildShiftId | CHILD_SHIFT_ID | — | — |
| 34 | PatternDetailsPEOCreatedBy | CREATED_BY | — | — |
| 35 | PatternDetailsPEOCreationDate | CREATION_DATE | — | — |
| 36 | PatternDetailsPEODayStartNum | DAY_START_NUM | — | — |
| 37 | PatternDetailsPEODayStopNum | DAY_STOP_NUM | — | — |
| 38 | PatternDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 39 | PatternDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 40 | PatternDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 41 | PatternDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 42 | PatternDetailsPEOPatternDtlId | PATTERN_DTL_ID | — | — |
| 43 | PatternDetailsPEOPatternDtlSeqNum | PATTERN_DTL_SEQ_NUM | — | — |
| 44 | PatternDetailsPEOPatternId | PATTERN_ID | — | — |

### [[zmm_sr_schedules_b|ZMM_SR_SCHEDULES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SchedulePEOAssignmentNum | ASSIGNMENT_NUM | — | — |
| 2 | SchedulePEOCategoryCode | CATEGORY_CODE | — | — |
| 3 | SchedulePEOCreatedBy | CREATED_BY | — | — |
| 4 | SchedulePEOCreationDate | CREATION_DATE | — | — |
| 5 | SchedulePEODeletedFlag | DELETED_FLAG | — | — |
| 6 | SchedulePEOEffectiveFromDate | EFFECTIVE_FROM_DATE | — | — |
| 7 | SchedulePEOEffectiveToDate | EFFECTIVE_TO_DATE | — | — |
| 8 | SchedulePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | SchedulePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | SchedulePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | SchedulePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | SchedulePEOQtrlyTypeCode | QTRLY_TYPE_CODE | — | — |
| 13 | SchedulePEOScheduleId | SCHEDULE_ID | — | — |
| 14 | SchedulePEOScheduleTypeCode | SCHEDULE_TYPE_CODE | — | — |

### [[zmm_sr_schedules_tl|ZMM_SR_SCHEDULES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ScheduleTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | ScheduleTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | ScheduleTranslationPEOLanguage | LANGUAGE | — | — |
| 4 | ScheduleTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ScheduleTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ScheduleTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ScheduleTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | ScheduleTranslationPEOScheduleDesc | SCHEDULE_DESC | — | — |
| 9 | ScheduleTranslationPEOScheduleId | SCHEDULE_ID | — | — |
| 10 | ScheduleTranslationPEOScheduleName | SCHEDULE_NAME | — | ✅ |
| 11 | ScheduleTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
