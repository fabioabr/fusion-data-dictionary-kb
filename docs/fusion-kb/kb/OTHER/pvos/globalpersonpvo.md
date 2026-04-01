---
id: DOC-OTHER-PVO-GlobalPersonPVO
doc_type: system-doc
title: "GlobalPersonPVO — PVO Cross-Module"
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
  - GlobalPersonPVO
  - globalpersonpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GlobalPersonPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Global Person. Acessa as tabelas: HR_ALL_ORGANIZATION_UNITS_F, HR_ALL_POSITIONS_F, HR_ALL_POSITIONS_F_TL (+23).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.GlobalPersonPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 729 | 26 | 1 | 687 | 94% |

---

## 🔗 Tabelas Relacionadas

- [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]] — 22 atributos (22 BICC)
- [[hr_all_positions_f|HR_ALL_POSITIONS_F]] — 149 atributos (149 BICC)
- [[hr_all_positions_f_tl|HR_ALL_POSITIONS_F_TL]] — 12 atributos (12 BICC)
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 18 atributos (18 BICC)
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 6 atributos (6 BICC)
- [[per_addresses_f|PER_ADDRESSES_F]] — 24 atributos (24 BICC)
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 128 atributos (119 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 24 atributos (24 BICC)
- [[per_assignment_status_types|PER_ASSIGNMENT_STATUS_TYPES]] — 9 atributos
- [[per_assignment_status_types_tl|PER_ASSIGNMENT_STATUS_TYPES_TL]] — 5 atributos
- [[per_assignment_supervisors_f|PER_ASSIGNMENT_SUPERVISORS_F]] — 19 atributos (19 BICC)
- [[per_email_addresses|PER_EMAIL_ADDRESSES]] — 21 atributos (17 BICC)
- [[per_grade_ladders_f|PER_GRADE_LADDERS_F]] — 4 atributos (4 BICC)
- [[per_grade_ladders_f_tl|PER_GRADE_LADDERS_F_TL]] — 6 atributos (6 BICC)
- [[per_jobs_f|PER_JOBS_F]] — 29 atributos (27 BICC)
- [[per_jobs_f_tl|PER_JOBS_F_TL]] — 6 atributos (6 BICC)
- [[per_location_details_f|PER_LOCATION_DETAILS_F]] — 5 atributos
- [[per_location_details_f_vl|PER_LOCATION_DETAILS_F_VL]] — 5 atributos (5 BICC)
- [[per_national_identifiers|PER_NATIONAL_IDENTIFIERS]] — 3 atributos (3 BICC)
- [[per_periods_of_service|PER_PERIODS_OF_SERVICE]] — 9 atributos (8 BICC)
- [[per_persons|PER_PERSONS]] — 18 atributos (1 PKs, 18 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 53 atributos (53 BICC)
- [[per_person_types_tl|PER_PERSON_TYPES_TL]] — 4 atributos (4 BICC)
- [[per_phones|PER_PHONES]] — 26 atributos (19 BICC)
- [[per_users|PER_USERS]] — 42 atributos (42 BICC)
- [[per_working_hour_patterns_f|PER_WORKING_HOUR_PATTERNS_F]] — 82 atributos (82 BICC)

---

## ⚙️ Atributos

### [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationUnitMgrPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | OrganizationUnitMgrPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | OrganizationUnitMgrPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | OrganizationUnitMgrPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 5 | OrganizationUnitPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | ✅ |
| 6 | OrganizationUnitPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 7 | OrganizationUnitPEOCostAllocationKeyflexId | COST_ALLOCATION_KEYFLEX_ID | — | ✅ |
| 8 | OrganizationUnitPEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | OrganizationUnitPEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | OrganizationUnitPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 11 | OrganizationUnitPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 12 | OrganizationUnitPEOEstablishmentId | ESTABLISHMENT_ID | — | ✅ |
| 13 | OrganizationUnitPEOInternalAddressLine | INTERNAL_ADDRESS_LINE | — | ✅ |
| 14 | OrganizationUnitPEOInternalExternalFlag | INTERNAL_EXTERNAL_FLAG | — | ✅ |
| 15 | OrganizationUnitPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | OrganizationUnitPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | OrganizationUnitPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | OrganizationUnitPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 19 | OrganizationUnitPEOLocationId | LOCATION_ID | — | ✅ |
| 20 | OrganizationUnitPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 21 | OrganizationUnitPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 22 | OrganizationUnitPEOOrganizationUnitPEOType | TYPE | — | ✅ |

### [[hr_all_positions_f|HR_ALL_POSITIONS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PositionMgrPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | ✅ |
| 2 | PositionMgrPEOActiveStatus | ACTIVE_STATUS | — | ✅ |
| 3 | PositionMgrPEOAttribute1 | ATTRIBUTE1 | — | ✅ |
| 4 | PositionMgrPEOAttribute10 | ATTRIBUTE10 | — | ✅ |
| 5 | PositionMgrPEOAttribute11 | ATTRIBUTE11 | — | ✅ |
| 6 | PositionMgrPEOAttribute12 | ATTRIBUTE12 | — | ✅ |
| 7 | PositionMgrPEOAttribute13 | ATTRIBUTE13 | — | ✅ |
| 8 | PositionMgrPEOAttribute14 | ATTRIBUTE14 | — | ✅ |
| 9 | PositionMgrPEOAttribute15 | ATTRIBUTE15 | — | ✅ |
| 10 | PositionMgrPEOAttribute16 | ATTRIBUTE16 | — | ✅ |
| 11 | PositionMgrPEOAttribute17 | ATTRIBUTE17 | — | ✅ |
| 12 | PositionMgrPEOAttribute18 | ATTRIBUTE18 | — | ✅ |
| 13 | PositionMgrPEOAttribute19 | ATTRIBUTE19 | — | ✅ |
| 14 | PositionMgrPEOAttribute2 | ATTRIBUTE2 | — | ✅ |
| 15 | PositionMgrPEOAttribute20 | ATTRIBUTE20 | — | ✅ |
| 16 | PositionMgrPEOAttribute21 | ATTRIBUTE21 | — | ✅ |
| 17 | PositionMgrPEOAttribute22 | ATTRIBUTE22 | — | ✅ |
| 18 | PositionMgrPEOAttribute23 | ATTRIBUTE23 | — | ✅ |
| 19 | PositionMgrPEOAttribute24 | ATTRIBUTE24 | — | ✅ |
| 20 | PositionMgrPEOAttribute25 | ATTRIBUTE25 | — | ✅ |
| 21 | PositionMgrPEOAttribute26 | ATTRIBUTE26 | — | ✅ |
| 22 | PositionMgrPEOAttribute27 | ATTRIBUTE27 | — | ✅ |
| 23 | PositionMgrPEOAttribute28 | ATTRIBUTE28 | — | ✅ |
| 24 | PositionMgrPEOAttribute29 | ATTRIBUTE29 | — | ✅ |
| 25 | PositionMgrPEOAttribute3 | ATTRIBUTE3 | — | ✅ |
| 26 | PositionMgrPEOAttribute30 | ATTRIBUTE30 | — | ✅ |
| 27 | PositionMgrPEOAttribute4 | ATTRIBUTE4 | — | ✅ |
| 28 | PositionMgrPEOAttribute5 | ATTRIBUTE5 | — | ✅ |
| 29 | PositionMgrPEOAttribute6 | ATTRIBUTE6 | — | ✅ |
| 30 | PositionMgrPEOAttribute7 | ATTRIBUTE7 | — | ✅ |
| 31 | PositionMgrPEOAttribute8 | ATTRIBUTE8 | — | ✅ |
| 32 | PositionMgrPEOAttribute9 | ATTRIBUTE9 | — | ✅ |
| 33 | PositionMgrPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 34 | PositionMgrPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 35 | PositionMgrPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | ✅ |
| 36 | PositionMgrPEOAttributeDate11 | ATTRIBUTE_DATE11 | — | ✅ |
| 37 | PositionMgrPEOAttributeDate12 | ATTRIBUTE_DATE12 | — | ✅ |
| 38 | PositionMgrPEOAttributeDate13 | ATTRIBUTE_DATE13 | — | ✅ |
| 39 | PositionMgrPEOAttributeDate14 | ATTRIBUTE_DATE14 | — | ✅ |
| 40 | PositionMgrPEOAttributeDate15 | ATTRIBUTE_DATE15 | — | ✅ |
| 41 | PositionMgrPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 42 | PositionMgrPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 43 | PositionMgrPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 44 | PositionMgrPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 45 | PositionMgrPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | ✅ |
| 46 | PositionMgrPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | ✅ |
| 47 | PositionMgrPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | ✅ |
| 48 | PositionMgrPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | ✅ |
| 49 | PositionMgrPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 50 | PositionMgrPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 51 | PositionMgrPEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | ✅ |
| 52 | PositionMgrPEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | ✅ |
| 53 | PositionMgrPEOAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | ✅ |
| 54 | PositionMgrPEOAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | ✅ |
| 55 | PositionMgrPEOAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | ✅ |
| 56 | PositionMgrPEOAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | ✅ |
| 57 | PositionMgrPEOAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | ✅ |
| 58 | PositionMgrPEOAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | ✅ |
| 59 | PositionMgrPEOAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | ✅ |
| 60 | PositionMgrPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 61 | PositionMgrPEOAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | ✅ |
| 62 | PositionMgrPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 63 | PositionMgrPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 64 | PositionMgrPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 65 | PositionMgrPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 66 | PositionMgrPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 67 | PositionMgrPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 68 | PositionMgrPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 69 | PositionMgrPEOBargainingUnitCd | BARGAINING_UNIT_CD | — | ✅ |
| 70 | PositionMgrPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 71 | PositionMgrPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 72 | PositionMgrPEOCreatedBy | CREATED_BY | — | ✅ |
| 73 | PositionMgrPEOCreationDate | CREATION_DATE | — | ✅ |
| 74 | PositionMgrPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 75 | PositionMgrPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 76 | PositionMgrPEOEntryGradeId | ENTRY_GRADE_ID | — | ✅ |
| 77 | PositionMgrPEOEntryStepId | ENTRY_STEP_ID | — | ✅ |
| 78 | PositionMgrPEOFrequency | FREQUENCY | — | ✅ |
| 79 | PositionMgrPEOFte | FTE | — | ✅ |
| 80 | PositionMgrPEOFullPartTime | FULL_PART_TIME | — | ✅ |
| 81 | PositionMgrPEOHiringStatus | HIRING_STATUS | — | ✅ |
| 82 | PositionMgrPEOJobId | JOB_ID | — | ✅ |
| 83 | PositionMgrPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 84 | PositionMgrPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 85 | PositionMgrPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 86 | PositionMgrPEOLocationId | LOCATION_ID | — | ✅ |
| 87 | PositionMgrPEOMaxPersons | MAX_PERSONS | — | ✅ |
| 88 | PositionMgrPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 89 | PositionMgrPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 90 | PositionMgrPEOOverlapAllowed | OVERLAP_ALLOWED | — | ✅ |
| 91 | PositionMgrPEOPermanentTemporaryFlag | PERMANENT_TEMPORARY_FLAG | — | ✅ |
| 92 | PositionMgrPEOPositionCode | POSITION_CODE | — | ✅ |
| 93 | PositionMgrPEOPositionId | POSITION_ID | — | ✅ |
| 94 | PositionMgrPEOPositionSynchronizationFlag | POSITION_SYNCHRONIZATION_FLAG | — | ✅ |
| 95 | PositionMgrPEOPositionType | POSITION_TYPE | — | ✅ |
| 96 | PositionMgrPEOProbationPeriod | PROBATION_PERIOD | — | ✅ |
| 97 | PositionMgrPEOProbationPeriodUnitCd | PROBATION_PERIOD_UNIT_CD | — | ✅ |
| 98 | PositionMgrPEOSeasonalEndDate | SEASONAL_END_DATE | — | ✅ |
| 99 | PositionMgrPEOSeasonalFlag | SEASONAL_FLAG | — | ✅ |
| 100 | PositionMgrPEOSeasonalStartDate | SEASONAL_START_DATE | — | ✅ |
| 101 | PositionMgrPEOSecurityClearance | SECURITY_CLEARANCE | — | ✅ |
| 102 | PositionMgrPEOSupervisorAssignmentId | SUPERVISOR_ASSIGNMENT_ID | — | ✅ |
| 103 | PositionMgrPEOSupervisorId | SUPERVISOR_ID | — | ✅ |
| 104 | PositionMgrPEOTimeNormalFinish | TIME_NORMAL_FINISH | — | ✅ |
| 105 | PositionMgrPEOTimeNormalStart | TIME_NORMAL_START | — | ✅ |
| 106 | PositionMgrPEOWorkingHours | WORKING_HOURS | — | ✅ |
| 107 | PositionPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | ✅ |
| 108 | PositionPEOActiveStatus | ACTIVE_STATUS | — | ✅ |
| 109 | PositionPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 110 | PositionPEOBargainingUnitCd | BARGAINING_UNIT_CD | — | ✅ |
| 111 | PositionPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 112 | PositionPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 113 | PositionPEOCreatedBy | CREATED_BY | — | ✅ |
| 114 | PositionPEOCreationDate | CREATION_DATE | — | ✅ |
| 115 | PositionPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 116 | PositionPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 117 | PositionPEOEntryGradeId | ENTRY_GRADE_ID | — | ✅ |
| 118 | PositionPEOEntryStepId | ENTRY_STEP_ID | — | ✅ |
| 119 | PositionPEOFrequency | FREQUENCY | — | ✅ |
| 120 | PositionPEOFte | FTE | — | ✅ |
| 121 | PositionPEOFullPartTime | FULL_PART_TIME | — | ✅ |
| 122 | PositionPEOHiringStatus | HIRING_STATUS | — | ✅ |
| 123 | PositionPEOJobId | JOB_ID | — | ✅ |
| 124 | PositionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 125 | PositionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 126 | PositionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 127 | PositionPEOLocationId | LOCATION_ID | — | ✅ |
| 128 | PositionPEOMaxPersons | MAX_PERSONS | — | ✅ |
| 129 | PositionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 130 | PositionPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 131 | PositionPEOOverlapAllowed | OVERLAP_ALLOWED | — | ✅ |
| 132 | PositionPEOPermanentTemporaryFlag | PERMANENT_TEMPORARY_FLAG | — | ✅ |
| 133 | PositionPEOPositionCode | POSITION_CODE | — | ✅ |
| 134 | PositionPEOPositionId | POSITION_ID | — | ✅ |
| 135 | PositionPEOPositionSynchronizationFlag | POSITION_SYNCHRONIZATION_FLAG | — | ✅ |
| 136 | PositionPEOPositionType | POSITION_TYPE | — | ✅ |
| 137 | PositionPEOProbationPeriod | PROBATION_PERIOD | — | ✅ |
| 138 | PositionPEOProbationPeriodUnitCd | PROBATION_PERIOD_UNIT_CD | — | ✅ |
| 139 | PositionPEOSeasonalEndDate | SEASONAL_END_DATE | — | ✅ |
| 140 | PositionPEOSeasonalFlag | SEASONAL_FLAG | — | ✅ |
| 141 | PositionPEOSeasonalStartDate | SEASONAL_START_DATE | — | ✅ |
| 142 | PositionPEOSecurityClearance | SECURITY_CLEARANCE | — | ✅ |
| 143 | PositionPEOStandardWorkingFrequency | STANDARD_WORKING_FREQUENCY | — | ✅ |
| 144 | PositionPEOStandardWorkingHours | STANDARD_WORKING_HOURS | — | ✅ |
| 145 | PositionPEOSupervisorAssignmentId | SUPERVISOR_ASSIGNMENT_ID | — | ✅ |
| 146 | PositionPEOSupervisorId | SUPERVISOR_ID | — | ✅ |
| 147 | PositionPEOTimeNormalFinish | TIME_NORMAL_FINISH | — | ✅ |
| 148 | PositionPEOTimeNormalStart | TIME_NORMAL_START | — | ✅ |
| 149 | PositionPEOWorkingHours | WORKING_HOURS | — | ✅ |

### [[hr_all_positions_f_tl|HR_ALL_POSITIONS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PositionTranslationMgrPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PositionTranslationMgrPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PositionTranslationMgrPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 4 | PositionTranslationMgrPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | PositionTranslationMgrPEOLanguage1 | LANGUAGE | — | ✅ |
| 6 | PositionTranslationMgrPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PositionTranslationMgrPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | PositionTranslationMgrPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | PositionTranslationMgrPEOName | NAME | — | ✅ |
| 10 | PositionTranslationMgrPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | PositionTranslationMgrPEOPositionId | POSITION_ID | — | ✅ |
| 12 | PositionTranslationMgrPEOSourceLang | SOURCE_LANG | — | ✅ |

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DepartmentWorkDayInfoPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | DepartmentWorkDayInfoPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | DepartmentWorkDayInfoPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | DepartmentWorkDayInfoPEOOrgInformationId | ORG_INFORMATION_ID | — | ✅ |
| 5 | DepartmentWorkDayInfoPEOWorkingHours | ORG_INFORMATION_NUMBER1 | — | ✅ |
| 6 | DepartmentWorkDayInfoPEOWorkingHoursFrequency | ORG_INFORMATION4 | — | ✅ |
| 7 | EnterpriseWorkDayInfoPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 8 | EnterpriseWorkDayInfoPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 9 | EnterpriseWorkDayInfoPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | EnterpriseWorkDayInfoPEOOrgInformationId | ORG_INFORMATION_ID | — | ✅ |
| 11 | EnterpriseWorkDayInfoPEOWorkingHours | ORG_INFORMATION_NUMBER1 | — | ✅ |
| 12 | EnterpriseWorkDayInfoPEOWorkingHoursFrequency | ORG_INFORMATION4 | — | ✅ |
| 13 | LegalEntityWorkDayInfoPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 14 | LegalEntityWorkDayInfoPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 15 | LegalEntityWorkDayInfoPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | LegalEntityWorkDayInfoPEOOrgInformationId | ORG_INFORMATION_ID | — | ✅ |
| 17 | LegalEntityWorkDayInfoPEOWorkingHours | ORG_INFORMATION_NUMBER1 | — | ✅ |
| 18 | LegalEntityWorkDayInfoPEOWorkingHoursFrequencey | ORG_INFORMATION4 | — | ✅ |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgUnitTranslationMgrPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | OrgUnitTranslationMgrPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | OrgUnitTranslationMgrPEOLanguage | LANGUAGE | — | ✅ |
| 4 | OrgUnitTranslationMgrPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | OrgUnitTranslationMgrPEOName | NAME | — | ✅ |
| 6 | OrgUnitTranslationMgrPEOOrganizationId | ORGANIZATION_ID | — | ✅ |

### [[per_addresses_f|PER_ADDRESSES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddressesPEOAddressId | ADDRESS_ID | — | ✅ |
| 2 | AddressesPEOAddressLine1 | ADDRESS_LINE_1 | — | ✅ |
| 3 | AddressesPEOAddressLine2 | ADDRESS_LINE_2 | — | ✅ |
| 4 | AddressesPEOAddressLine3 | ADDRESS_LINE_3 | — | ✅ |
| 5 | AddressesPEOAddressLine4 | ADDRESS_LINE_4 | — | ✅ |
| 6 | AddressesPEOBuilding | BUILDING | — | ✅ |
| 7 | AddressesPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 8 | AddressesPEOCountry | COUNTRY | — | ✅ |
| 9 | AddressesPEOCreatedBy | CREATED_BY | — | ✅ |
| 10 | AddressesPEOCreationDate | CREATION_DATE | — | ✅ |
| 11 | AddressesPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 12 | AddressesPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 13 | AddressesPEOFloorNumber | FLOOR_NUMBER | — | ✅ |
| 14 | AddressesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | AddressesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 16 | AddressesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | AddressesPEOLongPostalCode | LONG_POSTAL_CODE | — | ✅ |
| 18 | AddressesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 19 | AddressesPEOPostalCode | POSTAL_CODE | — | ✅ |
| 20 | AddressesPEORegion1 | REGION_1 | — | ✅ |
| 21 | AddressesPEORegion2 | REGION_2 | — | ✅ |
| 22 | AddressesPEORegion3 | REGION_3 | — | ✅ |
| 23 | AddressesPEOTimezoneCode | TIMEZONE_CODE | — | ✅ |
| 24 | AddressesPEOTownOrCity | TOWN_OR_CITY | — | ✅ |

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentMgrPEOAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 2 | AssignmentMgrPEOAssignmentNumber | ASSIGNMENT_NUMBER | — | ✅ |
| 3 | AssignmentMgrPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 4 | AssignmentMgrPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | ✅ |
| 5 | AssignmentMgrPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | ✅ |
| 6 | AssignmentMgrPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | AssignmentMgrPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | AssignmentMgrPEOLegislativeCode | LEGISLATION_CODE | — | ✅ |
| 9 | AssignmentPEOActionCode | ACTION_CODE | — | ✅ |
| 10 | AssignmentPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | ✅ |
| 11 | AssignmentPEOAdjustedFte | ADJUSTED_FTE | — | — |
| 12 | AssignmentPEOAllowAsgOverrideFlag | ALLOW_ASG_OVERRIDE_FLAG | — | ✅ |
| 13 | AssignmentPEOAnnualWorkingDuration | ANNUAL_WORKING_DURATION | — | — |
| 14 | AssignmentPEOAnnualWorkingDurationUnits | ANNUAL_WORKING_DURATION_UNITS | — | — |
| 15 | AssignmentPEOAnnualWorkingRatio | ANNUAL_WORKING_RATIO | — | — |
| 16 | AssignmentPEOApplicantRank | APPLICANT_RANK | — | ✅ |
| 17 | AssignmentPEOAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 18 | AssignmentPEOAssignmentName | ASSIGNMENT_NAME | — | ✅ |
| 19 | AssignmentPEOAssignmentNumber | ASSIGNMENT_NUMBER | — | ✅ |
| 20 | AssignmentPEOAssignmentSequence | ASSIGNMENT_SEQUENCE | — | ✅ |
| 21 | AssignmentPEOAssignmentStatusType | ASSIGNMENT_STATUS_TYPE | — | ✅ |
| 22 | AssignmentPEOAssignmentStatusTypeId | ASSIGNMENT_STATUS_TYPE_ID | — | ✅ |
| 23 | AssignmentPEOAssignmentType | ASSIGNMENT_TYPE | — | ✅ |
| 24 | AssignmentPEOAutoEndFlag | AUTO_END_FLAG | — | ✅ |
| 25 | AssignmentPEOBargainingUnitCode | BARGAINING_UNIT_CODE | — | ✅ |
| 26 | AssignmentPEOBillingTitle | BILLING_TITLE | — | ✅ |
| 27 | AssignmentPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 28 | AssignmentPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 29 | AssignmentPEOCagrGradeDefId | CAGR_GRADE_DEF_ID | — | ✅ |
| 30 | AssignmentPEOCagrIdFlexNum | CAGR_ID_FLEX_NUM | — | ✅ |
| 31 | AssignmentPEOCollectiveAgreementId | COLLECTIVE_AGREEMENT_ID | — | ✅ |
| 32 | AssignmentPEOContractId | CONTRACT_ID | — | ✅ |
| 33 | AssignmentPEOCreatedBy | CREATED_BY | — | ✅ |
| 34 | AssignmentPEOCreationDate | CREATION_DATE | — | ✅ |
| 35 | AssignmentPEODateProbationEnd | DATE_PROBATION_END | — | ✅ |
| 36 | AssignmentPEODefaultCodeCombId | DEFAULT_CODE_COMB_ID | — | ✅ |
| 37 | AssignmentPEODutiesType | DUTIES_TYPE | — | ✅ |
| 38 | AssignmentPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 39 | AssignmentPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | ✅ |
| 40 | AssignmentPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | ✅ |
| 41 | AssignmentPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 42 | AssignmentPEOEmployeeCategory | EMPLOYEE_CATEGORY | — | ✅ |
| 43 | AssignmentPEOEmploymentCategory | EMPLOYMENT_CATEGORY | — | ✅ |
| 44 | AssignmentPEOEstablishmentId | ESTABLISHMENT_ID | — | ✅ |
| 45 | AssignmentPEOExpenseCheckAddress | EXPENSE_CHECK_ADDRESS | — | ✅ |
| 46 | AssignmentPEOFreezeStartDate | FREEZE_START_DATE | — | ✅ |
| 47 | AssignmentPEOFreezeUntilDate | FREEZE_UNTIL_DATE | — | ✅ |
| 48 | AssignmentPEOFrequency | FREQUENCY | — | ✅ |
| 49 | AssignmentPEOFullPartTime | FULL_PART_TIME | — | ✅ |
| 50 | AssignmentPEOGradeId | GRADE_ID | — | ✅ |
| 51 | AssignmentPEOGradeLadderPgmId | GRADE_LADDER_PGM_ID | — | ✅ |
| 52 | AssignmentPEOGspEligibilityFlag | GSP_ELIGIBILITY_FLAG | — | ✅ |
| 53 | AssignmentPEOHourlySalariedCode | HOURLY_SALARIED_CODE | — | ✅ |
| 54 | AssignmentPEOIdFlexNum | ID_FLEX_NUM | — | ✅ |
| 55 | AssignmentPEOInternalBuilding | INTERNAL_BUILDING | — | ✅ |
| 56 | AssignmentPEOInternalFloor | INTERNAL_FLOOR | — | ✅ |
| 57 | AssignmentPEOInternalLocation | INTERNAL_LOCATION | — | ✅ |
| 58 | AssignmentPEOInternalMailstop | INTERNAL_MAILSTOP | — | ✅ |
| 59 | AssignmentPEOInternalOfficeNumber | INTERNAL_OFFICE_NUMBER | — | ✅ |
| 60 | AssignmentPEOJobId | JOB_ID | — | ✅ |
| 61 | AssignmentPEOJobPostSourceName | JOB_POST_SOURCE_NAME | — | ✅ |
| 62 | AssignmentPEOLabourUnionMemberFlag | LABOUR_UNION_MEMBER_FLAG | — | ✅ |
| 63 | AssignmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 64 | AssignmentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 65 | AssignmentPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 66 | AssignmentPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 67 | AssignmentPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 68 | AssignmentPEOLinkageType | LINKAGE_TYPE | — | ✅ |
| 69 | AssignmentPEOLocationId | LOCATION_ID | — | ✅ |
| 70 | AssignmentPEOManagerFlag | MANAGER_FLAG | — | ✅ |
| 71 | AssignmentPEONormalHours | NORMAL_HOURS | — | ✅ |
| 72 | AssignmentPEONoticePeriod | NOTICE_PERIOD | — | ✅ |
| 73 | AssignmentPEONoticePeriodUom | NOTICE_PERIOD_UOM | — | ✅ |
| 74 | AssignmentPEONotificationDate | NOTIFICATION_DATE | — | — |
| 75 | AssignmentPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 76 | AssignmentPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 77 | AssignmentPEOParentAssignmentId | PARENT_ASSIGNMENT_ID | — | ✅ |
| 78 | AssignmentPEOPeopleGroupId | PEOPLE_GROUP_ID | — | ✅ |
| 79 | AssignmentPEOPeriodOfServiceId | PERIOD_OF_SERVICE_ID | — | ✅ |
| 80 | AssignmentPEOPermanentTemporaryFlag | PERMANENT_TEMPORARY_FLAG | — | ✅ |
| 81 | AssignmentPEOPersonId | PERSON_ID | — | ✅ |
| 82 | AssignmentPEOPersonReferredById | PERSON_REFERRED_BY_ID | — | ✅ |
| 83 | AssignmentPEOPersonTypeId | PERSON_TYPE_ID | — | ✅ |
| 84 | AssignmentPEOPoHeaderId | PO_HEADER_ID | — | ✅ |
| 85 | AssignmentPEOPoLineId | PO_LINE_ID | — | ✅ |
| 86 | AssignmentPEOPositionId | POSITION_ID | — | ✅ |
| 87 | AssignmentPEOPositionOverrideFlag | POSITION_OVERRIDE_FLAG | — | ✅ |
| 88 | AssignmentPEOPostingContentId | POSTING_CONTENT_ID | — | ✅ |
| 89 | AssignmentPEOPrimaryAssignmentFlag | PRIMARY_ASSIGNMENT_FLAG | — | ✅ |
| 90 | AssignmentPEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 91 | AssignmentPEOPrimaryWorkRelationFlag | PRIMARY_WORK_RELATION_FLAG | — | ✅ |
| 92 | AssignmentPEOPrimaryWorkTermsFlag | PRIMARY_WORK_TERMS_FLAG | — | ✅ |
| 93 | AssignmentPEOProbationPeriod | PROBATION_PERIOD | — | ✅ |
| 94 | AssignmentPEOProbationUnit | PROBATION_UNIT | — | ✅ |
| 95 | AssignmentPEOProjectTitle | PROJECT_TITLE | — | ✅ |
| 96 | AssignmentPEOProjectedAssignmentEnd | PROJECTED_ASSIGNMENT_END | — | ✅ |
| 97 | AssignmentPEOProjectedStartDate | PROJECTED_START_DATE | — | ✅ |
| 98 | AssignmentPEOProposedWorkerType | PROPOSED_WORKER_TYPE | — | ✅ |
| 99 | AssignmentPEOReasonCode | REASON_CODE | — | ✅ |
| 100 | AssignmentPEORecordCreator | RECORD_CREATOR | — | ✅ |
| 101 | AssignmentPEORecruiterId | RECRUITER_ID | — | ✅ |
| 102 | AssignmentPEORecruitmentActivityId | RECRUITMENT_ACTIVITY_ID | — | ✅ |
| 103 | AssignmentPEORetirementAge | RETIREMENT_AGE | — | ✅ |
| 104 | AssignmentPEORetirementDate | RETIREMENT_DATE | — | ✅ |
| 105 | AssignmentPEOSalReviewPeriod | SAL_REVIEW_PERIOD | — | ✅ |
| 106 | AssignmentPEOSalReviewPeriodFrequency | SAL_REVIEW_PERIOD_FREQUENCY | — | ✅ |
| 107 | AssignmentPEOSeniorityBasis | SENIORITY_BASIS | — | ✅ |
| 108 | AssignmentPEOSetOfBooksId | SET_OF_BOOKS_ID | — | ✅ |
| 109 | AssignmentPEOSoftCodingKeyflexId | SOFT_CODING_KEYFLEX_ID | — | ✅ |
| 110 | AssignmentPEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | ✅ |
| 111 | AssignmentPEOSourceType | SOURCE_TYPE | — | ✅ |
| 112 | AssignmentPEOSpecialCeilingStepId | SPECIAL_CEILING_STEP_ID | — | ✅ |
| 113 | AssignmentPEOStandardFrequency | STANDARD_FREQUENCY | — | — |
| 114 | AssignmentPEOStandardHours | STANDARD_HOURS | — | — |
| 115 | AssignmentPEOStdAnnualWorkingDuration | STD_ANNUAL_WORKING_DURATION | — | — |
| 116 | AssignmentPEOStepEntryDate | STEP_ENTRY_DATE | — | ✅ |
| 117 | AssignmentPEOSystemPersonType | SYSTEM_PERSON_TYPE | — | ✅ |
| 118 | AssignmentPEOTaxAddressId | TAX_ADDRESS_ID | — | ✅ |
| 119 | AssignmentPEOTerminationDate | TERMINATION_DATE | — | — |
| 120 | AssignmentPEOTimeNormalFinish | TIME_NORMAL_FINISH | — | ✅ |
| 121 | AssignmentPEOTimeNormalStart | TIME_NORMAL_START | — | ✅ |
| 122 | AssignmentPEOVacancyId | VACANCY_ID | — | ✅ |
| 123 | AssignmentPEOVendorAssignmentNumber | VENDOR_ASSIGNMENT_NUMBER | — | ✅ |
| 124 | AssignmentPEOVendorEmployeeNumber | VENDOR_EMPLOYEE_NUMBER | — | ✅ |
| 125 | AssignmentPEOVendorId | VENDOR_ID | — | ✅ |
| 126 | AssignmentPEOVendorSiteId | VENDOR_SITE_ID | — | ✅ |
| 127 | AssignmentPEOWorkAtHome | WORK_AT_HOME | — | ✅ |
| 128 | AssignmentPEOWorkTermsAssignmentId | WORK_TERMS_ASSIGNMENT_ID | — | ✅ |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonDetailsPEO1EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | PersonDetailsPEO1EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonDetailsPEO1LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | PersonDetailsPEO1PersonId1 | PERSON_ID | — | ✅ |
| 5 | PersonDetailsPEO1PersonNumber | PERSON_NUMBER | — | ✅ |
| 6 | PersonDetailsPEO1PrimaryEmailId | PRIMARY_EMAIL_ID | — | ✅ |
| 7 | PersonDetailsPEOApplicantNumber | APPLICANT_NUMBER | — | ✅ |
| 8 | PersonDetailsPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 9 | PersonDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 10 | PersonDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 11 | PersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 12 | PersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 13 | PersonDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | PersonDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | PersonDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | PersonDetailsPEOMailingAddressId | MAILING_ADDRESS_ID | — | ✅ |
| 17 | PersonDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | PersonDetailsPEOPersonId | PERSON_ID | — | ✅ |
| 19 | PersonDetailsPEOPersonNumber | PERSON_NUMBER | — | ✅ |
| 20 | PersonDetailsPEOPrimaryEmailId | PRIMARY_EMAIL_ID | — | ✅ |
| 21 | PersonDetailsPEOPrimaryNidNumber | PRIMARY_NID_NUMBER | — | ✅ |
| 22 | PersonDetailsPEOPrimaryPhoneId | PRIMARY_PHONE_ID | — | ✅ |
| 23 | PersonDetailsPEOStartDate | START_DATE | — | ✅ |
| 24 | PersonDetailsPEOWaiveDataProtect | WAIVE_DATA_PROTECT | — | ✅ |

### [[per_assignment_status_types|PER_ASSIGNMENT_STATUS_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentStatusTypesPEOActiveFlag | ACTIVE_FLAG | — | — |
| 2 | AssignmentStatusTypesPEOAssignmentStatusCode | ASSIGNMENT_STATUS_CODE | — | — |
| 3 | AssignmentStatusTypesPEOAssignmentStatusTypeId | ASSIGNMENT_STATUS_TYPE_ID | — | — |
| 4 | AssignmentStatusTypesPEOEndDate | END_DATE | — | — |
| 5 | AssignmentStatusTypesPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 6 | AssignmentStatusTypesPEOPaySystemStatus | PAY_SYSTEM_STATUS | — | — |
| 7 | AssignmentStatusTypesPEOPerSystemStatus | PER_SYSTEM_STATUS | — | — |
| 8 | AssignmentStatusTypesPEOPrimaryFlag | PRIMARY_FLAG | — | — |
| 9 | AssignmentStatusTypesPEOStartDate | START_DATE | — | — |

### [[per_assignment_status_types_tl|PER_ASSIGNMENT_STATUS_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssginmentStatusTypesTLPEOAssignmentStatusTypeId | ASSIGNMENT_STATUS_TYPE_ID | — | — |
| 2 | AssginmentStatusTypesTLPEOLanguage | LANGUAGE | — | — |
| 3 | AssginmentStatusTypesTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 4 | AssginmentStatusTypesTLPEOSourceLang | SOURCE_LANG | — | — |
| 5 | AssginmentStatusTypesTLPEOUserStatus | USER_STATUS | — | — |

### [[per_assignment_supervisors_f|PER_ASSIGNMENT_SUPERVISORS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentSupervisorPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | ✅ |
| 2 | AssignmentSupervisorPEOAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 3 | AssignmentSupervisorPEOAssignmentSupervisorId | ASSIGNMENT_SUPERVISOR_ID | — | ✅ |
| 4 | AssignmentSupervisorPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 5 | AssignmentSupervisorPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | AssignmentSupervisorPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | AssignmentSupervisorPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 8 | AssignmentSupervisorPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 9 | AssignmentSupervisorPEOFreezeStartDate | FREEZE_START_DATE | — | ✅ |
| 10 | AssignmentSupervisorPEOFreezeUntilDate | FREEZE_UNTIL_DATE | — | ✅ |
| 11 | AssignmentSupervisorPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | AssignmentSupervisorPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | AssignmentSupervisorPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | AssignmentSupervisorPEOManagerAssignmentId | MANAGER_ASSIGNMENT_ID | — | ✅ |
| 15 | AssignmentSupervisorPEOManagerId | MANAGER_ID | — | ✅ |
| 16 | AssignmentSupervisorPEOManagerType | MANAGER_TYPE | — | ✅ |
| 17 | AssignmentSupervisorPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | AssignmentSupervisorPEOPersonId | PERSON_ID | — | ✅ |
| 19 | AssignmentSupervisorPEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |

### [[per_email_addresses|PER_EMAIL_ADDRESSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EmailAddressesPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 2 | EmailAddressesPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | EmailAddressesPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | EmailAddressesPEODateFrom | DATE_FROM | — | ✅ |
| 5 | EmailAddressesPEODateTo | DATE_TO | — | ✅ |
| 6 | EmailAddressesPEOEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 7 | EmailAddressesPEOEmailAddressId | EMAIL_ADDRESS_ID | — | ✅ |
| 8 | EmailAddressesPEOEmailType | EMAIL_TYPE | — | ✅ |
| 9 | EmailAddressesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | EmailAddressesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | EmailAddressesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | EmailAddressesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | EmailAddressesPEOPersonId | PERSON_ID | — | ✅ |
| 14 | SupervisorEmailAddressPEOEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 15 | SupervisorEmailAddressPEOEmailAddressId | EMAIL_ADDRESS_ID | — | ✅ |
| 16 | SupervisorEmailAddressPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | WorkEmailAddressesPEOEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 18 | WorkEmailAddressesPEOEmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 19 | WorkEmailAddressesPEOEmailType | EMAIL_TYPE | — | — |
| 20 | WorkEmailAddressesPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 21 | WorkEmailAddressesPEOPersonId | PERSON_ID | — | — |

### [[per_grade_ladders_f|PER_GRADE_LADDERS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GradeLadderPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | GradeLadderPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | GradeLadderPEOGradeLadderId | GRADE_LADDER_ID | — | ✅ |
| 4 | GradeLadderPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[per_grade_ladders_f_tl|PER_GRADE_LADDERS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GradeLadderTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | GradeLadderTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | GradeLadderTranslationPEOGradeLadderId | GRADE_LADDER_ID | — | ✅ |
| 4 | GradeLadderTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 5 | GradeLadderTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | GradeLadderTranslationPEOName | NAME | — | ✅ |

### [[per_jobs_f|PER_JOBS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JobMgrPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | JobMgrPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | JobMgrPEOJobId | JOB_ID | — | ✅ |
| 4 | JobMgrPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | JobPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | ✅ |
| 6 | JobPEOActiveStatus | ACTIVE_STATUS | — | ✅ |
| 7 | JobPEOApprovalAuthority | APPROVAL_AUTHORITY | — | ✅ |
| 8 | JobPEOBenchmarkJobFlag | BENCHMARK_JOB_FLAG | — | ✅ |
| 9 | JobPEOBenchmarkJobId | BENCHMARK_JOB_ID | — | ✅ |
| 10 | JobPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 11 | JobPEOCreatedBy | CREATED_BY | — | ✅ |
| 12 | JobPEOCreationDate | CREATION_DATE | — | ✅ |
| 13 | JobPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 14 | JobPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 15 | JobPEOFullPartTime | FULL_PART_TIME | — | ✅ |
| 16 | JobPEOJobCode | JOB_CODE | — | ✅ |
| 17 | JobPEOJobFamilyId | JOB_FAMILY_ID | — | ✅ |
| 18 | JobPEOJobFunctionCode | JOB_FUNCTION_CODE | — | ✅ |
| 19 | JobPEOJobId | JOB_ID | — | ✅ |
| 20 | JobPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | JobPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 22 | JobPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 23 | JobPEOManagerLevel | MANAGER_LEVEL | — | ✅ |
| 24 | JobPEOMedCheckupReq | MED_CHECKUP_REQ | — | ✅ |
| 25 | JobPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 26 | JobPEORegularTemporary | REGULAR_TEMPORARY | — | ✅ |
| 27 | JobPEOSetId | SET_ID | — | ✅ |
| 28 | JobPEOStandardWorkingFrequency | STANDARD_WORKING_FREQUENCY | — | — |
| 29 | JobPEOStandardWorkingHours | STANDARD_WORKING_HOURS | — | — |

### [[per_jobs_f_tl|PER_JOBS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JobMgrTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | JobMgrTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | JobMgrTranslationPEOJobId | JOB_ID | — | ✅ |
| 4 | JobMgrTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 5 | JobMgrTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | JobMgrTranslationPEOName | NAME | — | ✅ |

### [[per_location_details_f|PER_LOCATION_DETAILS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocBasePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | LocBasePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | LocBasePEOLocationDetailsId | LOCATION_DETAILS_ID | — | — |
| 4 | LocBasePEOStandardWorkingFrequency | STANDARD_WORKING_FREQUENCY | — | — |
| 5 | LocBasePEOStandardWorkingHours | STANDARD_WORKING_HOURS | — | — |

### [[per_location_details_f_vl|PER_LOCATION_DETAILS_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocationDetailsMgrPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | LocationDetailsMgrPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | LocationDetailsMgrPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | LocationDetailsMgrPEOLocationDetailsId | LOCATION_DETAILS_ID | — | ✅ |
| 5 | LocationDetailsMgrPEOLocationName | LOCATION_NAME | — | ✅ |

### [[per_national_identifiers|PER_NATIONAL_IDENTIFIERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NationalIdentifierPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | NationalIdentifierPEONationalIdentifierId | NATIONAL_IDENTIFIER_ID | — | ✅ |
| 3 | NationalIdentifierPEONationalIdentifierNumber | NATIONAL_IDENTIFIER_NUMBER | — | ✅ |

### [[per_periods_of_service|PER_PERIODS_OF_SERVICE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PeriodOfServicePEOActualTerminationDate | ACTUAL_TERMINATION_DATE | — | ✅ |
| 2 | PeriodOfServicePEOAdjustedSvcDate | ADJUSTED_SVC_DATE | — | — |
| 3 | PeriodOfServicePEODateStart | DATE_START | — | ✅ |
| 4 | PeriodOfServicePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PeriodOfServicePEONotifiedTerminationDate | NOTIFIED_TERMINATION_DATE | — | ✅ |
| 6 | PeriodOfServicePEOOriginalDateOfHire | ORIGINAL_DATE_OF_HIRE | — | ✅ |
| 7 | PeriodOfServicePEOPeriodOfServiceId | PERIOD_OF_SERVICE_ID | — | ✅ |
| 8 | PeriodOfServicePEOReadyToConvert | READY_TO_CONVERT | — | ✅ |
| 9 | PeriodOfServicePEORevokeUserAccess | REVOKE_USER_ACCESS | — | ✅ |

### [[per_persons|PER_PERSONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonId | PERSON_ID | 🔑 | ✅ |
| 2 | PersonPEOBloodType | BLOOD_TYPE | — | ✅ |
| 3 | PersonPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 4 | PersonPEOCorrespondenceLanguage | CORRESPONDENCE_LANGUAGE | — | ✅ |
| 5 | PersonPEOCountryOfBirth | COUNTRY_OF_BIRTH | — | ✅ |
| 6 | PersonPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | PersonPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | PersonPEODateOfBirth | DATE_OF_BIRTH | — | ✅ |
| 9 | PersonPEODateOfDeath | DATE_OF_DEATH | — | ✅ |
| 10 | PersonPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | PersonPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | PersonPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | PersonPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | PersonPEOPartyId | PARTY_ID | — | ✅ |
| 15 | PersonPEORegionOfBirth | REGION_OF_BIRTH | — | ✅ |
| 16 | PersonPEOStartDate | START_DATE | — | ✅ |
| 17 | PersonPEOTownOfBirth | TOWN_OF_BIRTH | — | ✅ |
| 18 | PersonPEOUserGuid | USER_GUID | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNamePEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 2 | PersonNamePEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | PersonNamePEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | PersonNamePEODisplayName | DISPLAY_NAME | — | ✅ |
| 5 | PersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 6 | PersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | PersonNamePEOFirstName | FIRST_NAME | — | ✅ |
| 8 | PersonNamePEOFullName | FULL_NAME | — | ✅ |
| 9 | PersonNamePEOHonors | HONORS | — | ✅ |
| 10 | PersonNamePEOKnownAs | KNOWN_AS | — | ✅ |
| 11 | PersonNamePEOLastName | LAST_NAME | — | ✅ |
| 12 | PersonNamePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | PersonNamePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | PersonNamePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | PersonNamePEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 16 | PersonNamePEOListName | LIST_NAME | — | ✅ |
| 17 | PersonNamePEOMiddleNames | MIDDLE_NAMES | — | ✅ |
| 18 | PersonNamePEOMilitaryRank | MILITARY_RANK | — | ✅ |
| 19 | PersonNamePEONameType | NAME_TYPE | — | ✅ |
| 20 | PersonNamePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 21 | PersonNamePEOPersonId | PERSON_ID | — | ✅ |
| 22 | PersonNamePEOPersonNameId | PERSON_NAME_ID | — | ✅ |
| 23 | PersonNamePEOPreNameAdjunct | PRE_NAME_ADJUNCT | — | ✅ |
| 24 | PersonNamePEOPreviousLastName | PREVIOUS_LAST_NAME | — | ✅ |
| 25 | PersonNamePEOSuffix | SUFFIX | — | ✅ |
| 26 | PersonNamePEOTitle | TITLE | — | ✅ |
| 27 | SupervisorNamePEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 28 | SupervisorNamePEOCreatedBy | CREATED_BY | — | ✅ |
| 29 | SupervisorNamePEOCreationDate | CREATION_DATE | — | ✅ |
| 30 | SupervisorNamePEODisplayName | DISPLAY_NAME | — | ✅ |
| 31 | SupervisorNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 32 | SupervisorNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 33 | SupervisorNamePEOFirstName | FIRST_NAME | — | ✅ |
| 34 | SupervisorNamePEOFullName | FULL_NAME | — | ✅ |
| 35 | SupervisorNamePEOHonors | HONORS | — | ✅ |
| 36 | SupervisorNamePEOKnownAs | KNOWN_AS | — | ✅ |
| 37 | SupervisorNamePEOLastName | LAST_NAME | — | ✅ |
| 38 | SupervisorNamePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 39 | SupervisorNamePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 40 | SupervisorNamePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 41 | SupervisorNamePEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 42 | SupervisorNamePEOListName | LIST_NAME | — | ✅ |
| 43 | SupervisorNamePEOMiddleNames | MIDDLE_NAMES | — | ✅ |
| 44 | SupervisorNamePEOMilitaryRank | MILITARY_RANK | — | ✅ |
| 45 | SupervisorNamePEONameType | NAME_TYPE | — | ✅ |
| 46 | SupervisorNamePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 47 | SupervisorNamePEOOrderName | ORDER_NAME | — | ✅ |
| 48 | SupervisorNamePEOPersonId | PERSON_ID | — | ✅ |
| 49 | SupervisorNamePEOPersonNameId | PERSON_NAME_ID | — | ✅ |
| 50 | SupervisorNamePEOPreNameAdjunct | PRE_NAME_ADJUNCT | — | ✅ |
| 51 | SupervisorNamePEOPreviousLastName | PREVIOUS_LAST_NAME | — | ✅ |
| 52 | SupervisorNamePEOSuffix | SUFFIX | — | ✅ |
| 53 | SupervisorNamePEOTitle | TITLE | — | ✅ |

### [[per_person_types_tl|PER_PERSON_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonTypesTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 2 | PersonTypesTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | PersonTypesTranslationPEOPersonTypeId | PERSON_TYPE_ID | — | ✅ |
| 4 | PersonTypesTranslationPEOUserPersonType | USER_PERSON_TYPE | — | ✅ |

### [[per_phones|PER_PHONES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PhonesEOAreaCode | AREA_CODE | — | ✅ |
| 2 | PhonesEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 3 | PhonesEOCountryCodeNumber | COUNTRY_CODE_NUMBER | — | ✅ |
| 4 | PhonesEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | PhonesEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | PhonesEODateFrom | DATE_FROM | — | ✅ |
| 7 | PhonesEODateTo | DATE_TO | — | ✅ |
| 8 | PhonesEOExtension | EXTENSION | — | ✅ |
| 9 | PhonesEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | PhonesEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | PhonesEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | PhonesEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 13 | PhonesEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | PhonesEOPersonId | PERSON_ID | — | ✅ |
| 15 | PhonesEOPhoneId | PHONE_ID | — | ✅ |
| 16 | PhonesEOPhoneNumber | PHONE_NUMBER | — | ✅ |
| 17 | PhonesEOPhoneType | PHONE_TYPE | — | ✅ |
| 18 | PhonesEOSpeedDialNumber | SPEED_DIAL_NUMBER | — | ✅ |
| 19 | PhonesEOValidity | VALIDITY | — | ✅ |
| 20 | WorkPhonePEOCountryCodeNumber | COUNTRY_CODE_NUMBER | — | — |
| 21 | WorkPhonePEOExtension | EXTENSION | — | — |
| 22 | WorkPhonePEOLegislationCode | LEGISLATION_CODE | — | — |
| 23 | WorkPhonePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 24 | WorkPhonePEOPersonId | PERSON_ID | — | — |
| 25 | WorkPhonePEOPhoneId | PHONE_ID | — | — |
| 26 | WorkPhonePEOPhoneNumber | PHONE_NUMBER | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupervisorUserPEOActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | SupervisorUserPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 3 | SupervisorUserPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | SupervisorUserPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | SupervisorUserPEOCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | ✅ |
| 6 | SupervisorUserPEOEndDate | END_DATE | — | ✅ |
| 7 | SupervisorUserPEOHrTerminated | HR_TERMINATED | — | ✅ |
| 8 | SupervisorUserPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | SupervisorUserPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | SupervisorUserPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | SupervisorUserPEOMultitenancyUsername | MULTITENANCY_USERNAME | — | ✅ |
| 12 | SupervisorUserPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | SupervisorUserPEOPartyId | PARTY_ID | — | ✅ |
| 14 | SupervisorUserPEOPersonId | PERSON_ID | — | ✅ |
| 15 | SupervisorUserPEOStartDate | START_DATE | — | ✅ |
| 16 | SupervisorUserPEOSuspended | SUSPENDED | — | ✅ |
| 17 | SupervisorUserPEOUserDataChecksum | USER_DATA_CHECKSUM | — | ✅ |
| 18 | SupervisorUserPEOUserDistinguishedName | USER_DISTINGUISHED_NAME | — | ✅ |
| 19 | SupervisorUserPEOUserGuid | USER_GUID | — | ✅ |
| 20 | SupervisorUserPEOUserId | USER_ID | — | ✅ |
| 21 | SupervisorUserPEOUsername | USERNAME | — | ✅ |
| 22 | UserPEOActiveFlag | ACTIVE_FLAG | — | ✅ |
| 23 | UserPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 24 | UserPEOCreatedBy | CREATED_BY | — | ✅ |
| 25 | UserPEOCreationDate | CREATION_DATE | — | ✅ |
| 26 | UserPEOCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | ✅ |
| 27 | UserPEOEndDate | END_DATE | — | ✅ |
| 28 | UserPEOHrTerminated | HR_TERMINATED | — | ✅ |
| 29 | UserPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | UserPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 31 | UserPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 32 | UserPEOMultitenancyUsername | MULTITENANCY_USERNAME | — | ✅ |
| 33 | UserPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 34 | UserPEOPartyId | PARTY_ID | — | ✅ |
| 35 | UserPEOPersonId | PERSON_ID | — | ✅ |
| 36 | UserPEOStartDate | START_DATE | — | ✅ |
| 37 | UserPEOSuspended | SUSPENDED | — | ✅ |
| 38 | UserPEOUserDataChecksum | USER_DATA_CHECKSUM | — | ✅ |
| 39 | UserPEOUserDistinguishedName | USER_DISTINGUISHED_NAME | — | ✅ |
| 40 | UserPEOUserGuid | USER_GUID | — | ✅ |
| 41 | UserPEOUserId | USER_ID | — | ✅ |
| 42 | UserPEOUsername | USERNAME | — | ✅ |

### [[per_working_hour_patterns_f|PER_WORKING_HOUR_PATTERNS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkingHourPatternsPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | WorkingHourPatternsPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | WorkingHourPatternsPEODefaultStartDay | DEFAULT_START_DAY | — | ✅ |
| 4 | WorkingHourPatternsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 5 | WorkingHourPatternsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 6 | WorkingHourPatternsPEOFriEndTime | FRI_END_TIME | — | ✅ |
| 7 | WorkingHourPatternsPEOFriHours | FRI_HOURS | — | ✅ |
| 8 | WorkingHourPatternsPEOFriStartTime | FRI_START_TIME | — | ✅ |
| 9 | WorkingHourPatternsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | WorkingHourPatternsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | WorkingHourPatternsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | WorkingHourPatternsPEOMonEndTime | MON_END_TIME | — | ✅ |
| 13 | WorkingHourPatternsPEOMonHours | MON_HOURS | — | ✅ |
| 14 | WorkingHourPatternsPEOMonStartTime | MON_START_TIME | — | ✅ |
| 15 | WorkingHourPatternsPEOObject | OBJECT | — | ✅ |
| 16 | WorkingHourPatternsPEOObjectId | OBJECT_ID | — | ✅ |
| 17 | WorkingHourPatternsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | WorkingHourPatternsPEOPersonId1 | PERSON_ID | — | ✅ |
| 19 | WorkingHourPatternsPEOSatEndTime | SAT_END_TIME | — | ✅ |
| 20 | WorkingHourPatternsPEOSatHours | SAT_HOURS | — | ✅ |
| 21 | WorkingHourPatternsPEOSatStartTime | SAT_START_TIME | — | ✅ |
| 22 | WorkingHourPatternsPEOSunEndTime | SUN_END_TIME | — | ✅ |
| 23 | WorkingHourPatternsPEOSunHours | SUN_HOURS | — | ✅ |
| 24 | WorkingHourPatternsPEOSunStartTime | SUN_START_TIME | — | ✅ |
| 25 | WorkingHourPatternsPEOThuEndTime | THU_END_TIME | — | ✅ |
| 26 | WorkingHourPatternsPEOThuHours | THU_HOURS | — | ✅ |
| 27 | WorkingHourPatternsPEOThuStartTime | THU_START_TIME | — | ✅ |
| 28 | WorkingHourPatternsPEOTotalHours | TOTAL_HOURS | — | ✅ |
| 29 | WorkingHourPatternsPEOTueEndTime | TUE_END_TIME | — | ✅ |
| 30 | WorkingHourPatternsPEOTueHours | TUE_HOURS | — | ✅ |
| 31 | WorkingHourPatternsPEOTueStartTime | TUE_START_TIME | — | ✅ |
| 32 | WorkingHourPatternsPEOWedEndTime | WED_END_TIME | — | ✅ |
| 33 | WorkingHourPatternsPEOWedHours | WED_HOURS | — | ✅ |
| 34 | WorkingHourPatternsPEOWedStartTime | WED_START_TIME | — | ✅ |
| 35 | WorkingHourPatternsPEOWhpAttribute1 | WHP_ATTRIBUTE1 | — | ✅ |
| 36 | WorkingHourPatternsPEOWhpAttribute10 | WHP_ATTRIBUTE10 | — | ✅ |
| 37 | WorkingHourPatternsPEOWhpAttribute11 | WHP_ATTRIBUTE11 | — | ✅ |
| 38 | WorkingHourPatternsPEOWhpAttribute12 | WHP_ATTRIBUTE12 | — | ✅ |
| 39 | WorkingHourPatternsPEOWhpAttribute13 | WHP_ATTRIBUTE13 | — | ✅ |
| 40 | WorkingHourPatternsPEOWhpAttribute14 | WHP_ATTRIBUTE14 | — | ✅ |
| 41 | WorkingHourPatternsPEOWhpAttribute15 | WHP_ATTRIBUTE15 | — | ✅ |
| 42 | WorkingHourPatternsPEOWhpAttribute16 | WHP_ATTRIBUTE16 | — | ✅ |
| 43 | WorkingHourPatternsPEOWhpAttribute17 | WHP_ATTRIBUTE17 | — | ✅ |
| 44 | WorkingHourPatternsPEOWhpAttribute18 | WHP_ATTRIBUTE18 | — | ✅ |
| 45 | WorkingHourPatternsPEOWhpAttribute19 | WHP_ATTRIBUTE19 | — | ✅ |
| 46 | WorkingHourPatternsPEOWhpAttribute2 | WHP_ATTRIBUTE2 | — | ✅ |
| 47 | WorkingHourPatternsPEOWhpAttribute20 | WHP_ATTRIBUTE20 | — | ✅ |
| 48 | WorkingHourPatternsPEOWhpAttribute3 | WHP_ATTRIBUTE3 | — | ✅ |
| 49 | WorkingHourPatternsPEOWhpAttribute4 | WHP_ATTRIBUTE4 | — | ✅ |
| 50 | WorkingHourPatternsPEOWhpAttribute5 | WHP_ATTRIBUTE5 | — | ✅ |
| 51 | WorkingHourPatternsPEOWhpAttribute6 | WHP_ATTRIBUTE6 | — | ✅ |
| 52 | WorkingHourPatternsPEOWhpAttribute7 | WHP_ATTRIBUTE7 | — | ✅ |
| 53 | WorkingHourPatternsPEOWhpAttribute8 | WHP_ATTRIBUTE8 | — | ✅ |
| 54 | WorkingHourPatternsPEOWhpAttribute9 | WHP_ATTRIBUTE9 | — | ✅ |
| 55 | WorkingHourPatternsPEOWhpAttributeCategory | WHP_ATTRIBUTE_CATEGORY | — | ✅ |
| 56 | WorkingHourPatternsPEOWhpAttributeDate1 | WHP_ATTRIBUTE_DATE1 | — | ✅ |
| 57 | WorkingHourPatternsPEOWhpAttributeDate10 | WHP_ATTRIBUTE_DATE10 | — | ✅ |
| 58 | WorkingHourPatternsPEOWhpAttributeDate11 | WHP_ATTRIBUTE_DATE11 | — | ✅ |
| 59 | WorkingHourPatternsPEOWhpAttributeDate12 | WHP_ATTRIBUTE_DATE12 | — | ✅ |
| 60 | WorkingHourPatternsPEOWhpAttributeDate13 | WHP_ATTRIBUTE_DATE13 | — | ✅ |
| 61 | WorkingHourPatternsPEOWhpAttributeDate14 | WHP_ATTRIBUTE_DATE14 | — | ✅ |
| 62 | WorkingHourPatternsPEOWhpAttributeDate15 | WHP_ATTRIBUTE_DATE15 | — | ✅ |
| 63 | WorkingHourPatternsPEOWhpAttributeDate2 | WHP_ATTRIBUTE_DATE2 | — | ✅ |
| 64 | WorkingHourPatternsPEOWhpAttributeDate3 | WHP_ATTRIBUTE_DATE3 | — | ✅ |
| 65 | WorkingHourPatternsPEOWhpAttributeDate4 | WHP_ATTRIBUTE_DATE4 | — | ✅ |
| 66 | WorkingHourPatternsPEOWhpAttributeDate5 | WHP_ATTRIBUTE_DATE5 | — | ✅ |
| 67 | WorkingHourPatternsPEOWhpAttributeDate6 | WHP_ATTRIBUTE_DATE6 | — | ✅ |
| 68 | WorkingHourPatternsPEOWhpAttributeDate7 | WHP_ATTRIBUTE_DATE7 | — | ✅ |
| 69 | WorkingHourPatternsPEOWhpAttributeDate8 | WHP_ATTRIBUTE_DATE8 | — | ✅ |
| 70 | WorkingHourPatternsPEOWhpAttributeDate9 | WHP_ATTRIBUTE_DATE9 | — | ✅ |
| 71 | WorkingHourPatternsPEOWhpAttributeNumber1 | WHP_ATTRIBUTE_NUMBER1 | — | ✅ |
| 72 | WorkingHourPatternsPEOWhpAttributeNumber10 | WHP_ATTRIBUTE_NUMBER10 | — | ✅ |
| 73 | WorkingHourPatternsPEOWhpAttributeNumber2 | WHP_ATTRIBUTE_NUMBER2 | — | ✅ |
| 74 | WorkingHourPatternsPEOWhpAttributeNumber3 | WHP_ATTRIBUTE_NUMBER3 | — | ✅ |
| 75 | WorkingHourPatternsPEOWhpAttributeNumber4 | WHP_ATTRIBUTE_NUMBER4 | — | ✅ |
| 76 | WorkingHourPatternsPEOWhpAttributeNumber5 | WHP_ATTRIBUTE_NUMBER5 | — | ✅ |
| 77 | WorkingHourPatternsPEOWhpAttributeNumber6 | WHP_ATTRIBUTE_NUMBER6 | — | ✅ |
| 78 | WorkingHourPatternsPEOWhpAttributeNumber7 | WHP_ATTRIBUTE_NUMBER7 | — | ✅ |
| 79 | WorkingHourPatternsPEOWhpAttributeNumber8 | WHP_ATTRIBUTE_NUMBER8 | — | ✅ |
| 80 | WorkingHourPatternsPEOWhpAttributeNumber9 | WHP_ATTRIBUTE_NUMBER9 | — | ✅ |
| 81 | WorkingHourPatternsPEOWorkingHourPatternId | WORKING_HOUR_PATTERN_ID | — | ✅ |
| 82 | WorkingHourPatternsPEOWorkingHoursType | WORKING_HOURS_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
