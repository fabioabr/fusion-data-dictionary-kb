---
id: DOC-HCM-PVO-PersonRefPVO
doc_type: system-doc
title: "PersonRefPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PersonRefPVO
  - personrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonRefPVO

## 📌 Visão Geral

Extrai visão consolidada de referência da pessoa, combinando nome, endereço, assignment e organização (16 tabelas, 250 atributos). View ampla para relatórios gerenciais e people analytics.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.PersonRefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 250 | 16 | 3 | 65 | 26% |

---

## 🔗 Tabelas Relacionadas

- [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]] — 3 atributos (1 BICC)
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 5 atributos (2 BICC)
- [[per_addresses_f|PER_ADDRESSES_F]] — 17 atributos
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 113 atributos (27 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 10 atributos (4 BICC)
- [[per_assignment_supervisors_f|PER_ASSIGNMENT_SUPERVISORS_F]] — 6 atributos (2 BICC)
- [[per_email_addresses|PER_EMAIL_ADDRESSES]] — 2 atributos
- [[per_jobs_f|PER_JOBS_F]] — 3 atributos (1 BICC)
- [[per_jobs_f_tl|PER_JOBS_F_TL]] — 5 atributos (2 BICC)
- [[per_location_details_f_vl|PER_LOCATION_DETAILS_F_VL]] — 4 atributos (2 BICC)
- [[per_periods_of_service|PER_PERIODS_OF_SERVICE]] — 2 atributos (1 BICC)
- [[per_persons|PER_PERSONS]] — 9 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 39 atributos (3 PKs, 19 BICC)
- [[per_person_types_tl|PER_PERSON_TYPES_TL]] — 3 atributos (1 BICC)
- [[per_phones|PER_PHONES]] — 8 atributos
- [[per_users|PER_USERS]] — 21 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationUnitMgrPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | OrganizationUnitMgrPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | OrganizationUnitMgrPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgUnitTranslationMgrPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | OrgUnitTranslationMgrPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | OrgUnitTranslationMgrPEOLanguage | LANGUAGE | — | ✅ |
| 4 | OrgUnitTranslationMgrPEOName | NAME | — | — |
| 5 | OrgUnitTranslationMgrPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[per_addresses_f|PER_ADDRESSES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddressesPEOAddressId | ADDRESS_ID | — | — |
| 2 | AddressesPEOAddressLine1 | ADDRESS_LINE_1 | — | — |
| 3 | AddressesPEOAddressLine2 | ADDRESS_LINE_2 | — | — |
| 4 | AddressesPEOAddressLine3 | ADDRESS_LINE_3 | — | — |
| 5 | AddressesPEOAddressLine4 | ADDRESS_LINE_4 | — | — |
| 6 | AddressesPEOBuilding | BUILDING | — | — |
| 7 | AddressesPEOCountry | COUNTRY | — | — |
| 8 | AddressesPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 9 | AddressesPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 10 | AddressesPEOFloorNumber | FLOOR_NUMBER | — | — |
| 11 | AddressesPEOLongPostalCode | LONG_POSTAL_CODE | — | — |
| 12 | AddressesPEOPostalCode | POSTAL_CODE | — | — |
| 13 | AddressesPEORegion1 | REGION_1 | — | — |
| 14 | AddressesPEORegion2 | REGION_2 | — | — |
| 15 | AddressesPEORegion3 | REGION_3 | — | — |
| 16 | AddressesPEOTimezoneCode | TIMEZONE_CODE | — | — |
| 17 | AddressesPEOTownOrCity | TOWN_OR_CITY | — | — |

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentMgrPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 2 | AssignmentMgrPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | AssignmentMgrPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 4 | AssignmentMgrPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 5 | AssignmentMgrPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 6 | AssignmentMgrPEOLegislationCode | LEGISLATION_CODE | — | — |
| 7 | AssignmentPEOActionCode | ACTION_CODE | — | ✅ |
| 8 | AssignmentPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 9 | AssignmentPEOAllowAsgOverrideFlag | ALLOW_ASG_OVERRIDE_FLAG | — | — |
| 10 | AssignmentPEOApplicantRank | APPLICANT_RANK | — | ✅ |
| 11 | AssignmentPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 12 | AssignmentPEOAssignmentName | ASSIGNMENT_NAME | — | ✅ |
| 13 | AssignmentPEOAssignmentNumber | ASSIGNMENT_NUMBER | — | ✅ |
| 14 | AssignmentPEOAssignmentSequence | ASSIGNMENT_SEQUENCE | — | — |
| 15 | AssignmentPEOAssignmentStatusType | ASSIGNMENT_STATUS_TYPE | — | ✅ |
| 16 | AssignmentPEOAssignmentStatusTypeId | ASSIGNMENT_STATUS_TYPE_ID | — | ✅ |
| 17 | AssignmentPEOAssignmentType | ASSIGNMENT_TYPE | — | ✅ |
| 18 | AssignmentPEOAutoEndFlag | AUTO_END_FLAG | — | — |
| 19 | AssignmentPEOBargainingUnitCode | BARGAINING_UNIT_CODE | — | — |
| 20 | AssignmentPEOBillingTitle | BILLING_TITLE | — | ✅ |
| 21 | AssignmentPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 22 | AssignmentPEOBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 23 | AssignmentPEOCagrGradeDefId | CAGR_GRADE_DEF_ID | — | — |
| 24 | AssignmentPEOCagrIdFlexNum | CAGR_ID_FLEX_NUM | — | — |
| 25 | AssignmentPEOCollectiveAgreementId | COLLECTIVE_AGREEMENT_ID | — | — |
| 26 | AssignmentPEOContractId | CONTRACT_ID | — | — |
| 27 | AssignmentPEOCreatedBy | CREATED_BY | — | — |
| 28 | AssignmentPEOCreationDate | CREATION_DATE | — | — |
| 29 | AssignmentPEODateProbationEnd | DATE_PROBATION_END | — | — |
| 30 | AssignmentPEODefaultCodeCombId | DEFAULT_CODE_COMB_ID | — | — |
| 31 | AssignmentPEODutiesType | DUTIES_TYPE | — | — |
| 32 | AssignmentPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 33 | AssignmentPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | ✅ |
| 34 | AssignmentPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | ✅ |
| 35 | AssignmentPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 36 | AssignmentPEOEmployeeCategory | EMPLOYEE_CATEGORY | — | ✅ |
| 37 | AssignmentPEOEmploymentCategory | EMPLOYMENT_CATEGORY | — | ✅ |
| 38 | AssignmentPEOEstablishmentId | ESTABLISHMENT_ID | — | — |
| 39 | AssignmentPEOExpenseCheckAddress | EXPENSE_CHECK_ADDRESS | — | — |
| 40 | AssignmentPEOFreezeStartDate | FREEZE_START_DATE | — | — |
| 41 | AssignmentPEOFreezeUntilDate | FREEZE_UNTIL_DATE | — | — |
| 42 | AssignmentPEOFrequency | FREQUENCY | — | — |
| 43 | AssignmentPEOGradeId | GRADE_ID | — | — |
| 44 | AssignmentPEOGradeLadderPgmId | GRADE_LADDER_PGM_ID | — | — |
| 45 | AssignmentPEOHourlySalariedCode | HOURLY_SALARIED_CODE | — | — |
| 46 | AssignmentPEOIdFlexNum | ID_FLEX_NUM | — | — |
| 47 | AssignmentPEOInternalBuilding | INTERNAL_BUILDING | — | — |
| 48 | AssignmentPEOInternalFloor | INTERNAL_FLOOR | — | — |
| 49 | AssignmentPEOInternalLocation | INTERNAL_LOCATION | — | — |
| 50 | AssignmentPEOInternalMailstop | INTERNAL_MAILSTOP | — | ✅ |
| 51 | AssignmentPEOInternalOfficeNumber | INTERNAL_OFFICE_NUMBER | — | — |
| 52 | AssignmentPEOJobId | JOB_ID | — | — |
| 53 | AssignmentPEOJobPostSourceName | JOB_POST_SOURCE_NAME | — | — |
| 54 | AssignmentPEOLabourUnionMemberFlag | LABOUR_UNION_MEMBER_FLAG | — | — |
| 55 | AssignmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 56 | AssignmentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 57 | AssignmentPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 58 | AssignmentPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 59 | AssignmentPEOLegislationCode | LEGISLATION_CODE | — | — |
| 60 | AssignmentPEOLinkageType | LINKAGE_TYPE | — | — |
| 61 | AssignmentPEOLocationId | LOCATION_ID | — | — |
| 62 | AssignmentPEOManagerFlag | MANAGER_FLAG | — | — |
| 63 | AssignmentPEONormalHours | NORMAL_HOURS | — | — |
| 64 | AssignmentPEONoticePeriod | NOTICE_PERIOD | — | — |
| 65 | AssignmentPEONoticePeriodUom | NOTICE_PERIOD_UOM | — | — |
| 66 | AssignmentPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 67 | AssignmentPEOOrganizationId | ORGANIZATION_ID | — | — |
| 68 | AssignmentPEOParentAssignmentId | PARENT_ASSIGNMENT_ID | — | — |
| 69 | AssignmentPEOPeopleGroupId | PEOPLE_GROUP_ID | — | — |
| 70 | AssignmentPEOPeriodOfServiceId | PERIOD_OF_SERVICE_ID | — | — |
| 71 | AssignmentPEOPersonId | PERSON_ID | — | — |
| 72 | AssignmentPEOPersonReferredById | PERSON_REFERRED_BY_ID | — | — |
| 73 | AssignmentPEOPersonTypeId | PERSON_TYPE_ID | — | ✅ |
| 74 | AssignmentPEOPoHeaderId | PO_HEADER_ID | — | — |
| 75 | AssignmentPEOPoLineId | PO_LINE_ID | — | — |
| 76 | AssignmentPEOPositionId | POSITION_ID | — | — |
| 77 | AssignmentPEOPositionOverrideFlag | POSITION_OVERRIDE_FLAG | — | — |
| 78 | AssignmentPEOPostingContentId | POSTING_CONTENT_ID | — | — |
| 79 | AssignmentPEOPrimaryAssignmentFlag | PRIMARY_ASSIGNMENT_FLAG | — | ✅ |
| 80 | AssignmentPEOPrimaryFlag | PRIMARY_FLAG | — | — |
| 81 | AssignmentPEOPrimaryWorkRelationFlag | PRIMARY_WORK_RELATION_FLAG | — | ✅ |
| 82 | AssignmentPEOPrimaryWorkTermsFlag | PRIMARY_WORK_TERMS_FLAG | — | — |
| 83 | AssignmentPEOProbationPeriod | PROBATION_PERIOD | — | — |
| 84 | AssignmentPEOProbationUnit | PROBATION_UNIT | — | — |
| 85 | AssignmentPEOProjectTitle | PROJECT_TITLE | — | — |
| 86 | AssignmentPEOProjectedAssignmentEnd | PROJECTED_ASSIGNMENT_END | — | — |
| 87 | AssignmentPEOProjectedStartDate | PROJECTED_START_DATE | — | — |
| 88 | AssignmentPEOProposedWorkerType | PROPOSED_WORKER_TYPE | — | — |
| 89 | AssignmentPEOReasonCode | REASON_CODE | — | ✅ |
| 90 | AssignmentPEORecordCreator | RECORD_CREATOR | — | — |
| 91 | AssignmentPEORecruiterId | RECRUITER_ID | — | — |
| 92 | AssignmentPEORecruitmentActivityId | RECRUITMENT_ACTIVITY_ID | — | — |
| 93 | AssignmentPEORetirementAge | RETIREMENT_AGE | — | ✅ |
| 94 | AssignmentPEORetirementDate | RETIREMENT_DATE | — | ✅ |
| 95 | AssignmentPEOSalReviewPeriod | SAL_REVIEW_PERIOD | — | — |
| 96 | AssignmentPEOSalReviewPeriodFrequency | SAL_REVIEW_PERIOD_FREQUENCY | — | — |
| 97 | AssignmentPEOSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 98 | AssignmentPEOSoftCodingKeyflexId | SOFT_CODING_KEYFLEX_ID | — | — |
| 99 | AssignmentPEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 100 | AssignmentPEOSourceType | SOURCE_TYPE | — | — |
| 101 | AssignmentPEOSpecialCeilingStepId | SPECIAL_CEILING_STEP_ID | — | — |
| 102 | AssignmentPEOStepEntryDate | STEP_ENTRY_DATE | — | — |
| 103 | AssignmentPEOSystemPersonType | SYSTEM_PERSON_TYPE | — | ✅ |
| 104 | AssignmentPEOTaxAddressId | TAX_ADDRESS_ID | — | — |
| 105 | AssignmentPEOTimeNormalFinish | TIME_NORMAL_FINISH | — | ✅ |
| 106 | AssignmentPEOTimeNormalStart | TIME_NORMAL_START | — | ✅ |
| 107 | AssignmentPEOVacancyId | VACANCY_ID | — | — |
| 108 | AssignmentPEOVendorAssignmentNumber | VENDOR_ASSIGNMENT_NUMBER | — | — |
| 109 | AssignmentPEOVendorEmployeeNumber | VENDOR_EMPLOYEE_NUMBER | — | — |
| 110 | AssignmentPEOVendorId | VENDOR_ID | — | — |
| 111 | AssignmentPEOVendorSiteId | VENDOR_SITE_ID | — | — |
| 112 | AssignmentPEOWorkAtHome | WORK_AT_HOME | — | ✅ |
| 113 | AssignmentPEOWorkTermsAssignmentId | WORK_TERMS_ASSIGNMENT_ID | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonDetailsPEO1EffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 2 | PersonDetailsPEO1EffectiveStartDate1 | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonDetailsPEO1PersonId | PERSON_ID | — | — |
| 4 | PersonDetailsPEO1PersonNumber | PERSON_NUMBER | — | ✅ |
| 5 | PersonDetailsPEOApplicantNumber | APPLICANT_NUMBER | — | — |
| 6 | PersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | PersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 8 | PersonDetailsPEOPersonId | PERSON_ID | — | — |
| 9 | PersonDetailsPEOPersonNumber | PERSON_NUMBER | — | ✅ |
| 10 | PersonDetailsPEOWaiveDataProtect | WAIVE_DATA_PROTECT | — | — |

### [[per_assignment_supervisors_f|PER_ASSIGNMENT_SUPERVISORS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentSupervisorPEOAssignmentSupervisorId | ASSIGNMENT_SUPERVISOR_ID | — | — |
| 2 | AssignmentSupervisorPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | AssignmentSupervisorPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | AssignmentSupervisorPEOManagerAssignmentId | MANAGER_ASSIGNMENT_ID | — | — |
| 5 | AssignmentSupervisorPEOManagerId | MANAGER_ID | — | ✅ |
| 6 | AssignmentSupervisorPEOManagerType | MANAGER_TYPE | — | — |

### [[per_email_addresses|PER_EMAIL_ADDRESSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EmailAddressesPEOEmailAddress | EMAIL_ADDRESS | — | — |
| 2 | EmailAddressesPEOEmailAddressId | EMAIL_ADDRESS_ID | — | — |

### [[per_jobs_f|PER_JOBS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JobMgrPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | JobMgrPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | JobMgrPEOJobId | JOB_ID | — | — |

### [[per_jobs_f_tl|PER_JOBS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JobTranslationMgrPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | JobTranslationMgrPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | JobTranslationMgrPEOJobId | JOB_ID | — | — |
| 4 | JobTranslationMgrPEOLanguage | LANGUAGE | — | — |
| 5 | JobTranslationMgrPEOName | NAME | — | ✅ |

### [[per_location_details_f_vl|PER_LOCATION_DETAILS_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocationDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | LocationDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | LocationDetailsPEOLocationDetailsId | LOCATION_DETAILS_ID | — | — |
| 4 | LocationDetailsPEOLocationName | LOCATION_NAME | — | ✅ |

### [[per_periods_of_service|PER_PERIODS_OF_SERVICE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PeriodOfServicePEODateStart | DATE_START | — | ✅ |
| 2 | PeriodOfServicePEOPeriodOfServiceId | PERIOD_OF_SERVICE_ID | — | — |

### [[per_persons|PER_PERSONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonPEOBloodType | BLOOD_TYPE | — | — |
| 2 | PersonPEOCorrespondenceLanguage | CORRESPONDENCE_LANGUAGE | — | — |
| 3 | PersonPEOCountryOfBirth | COUNTRY_OF_BIRTH | — | — |
| 4 | PersonPEODateOfBirth | DATE_OF_BIRTH | — | ✅ |
| 5 | PersonPEODateOfDeath | DATE_OF_DEATH | — | — |
| 6 | PersonPEOPersonId | PERSON_ID | — | — |
| 7 | PersonPEORegionOfBirth | REGION_OF_BIRTH | — | — |
| 8 | PersonPEOTownOfBirth | TOWN_OF_BIRTH | — | — |
| 9 | PersonPEOUserGuid | USER_GUID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | PersonNameId | PERSON_NAME_ID | 🔑 | ✅ |
| 4 | PersonNamePEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 5 | PersonNamePEOCreatedBy | CREATED_BY | — | — |
| 6 | PersonNamePEOCreationDate | CREATION_DATE | — | — |
| 7 | PersonNamePEODisplayName | DISPLAY_NAME | — | ✅ |
| 8 | PersonNamePEOFirstName | FIRST_NAME | — | ✅ |
| 9 | PersonNamePEOFullName | FULL_NAME | — | ✅ |
| 10 | PersonNamePEOHonors | HONORS | — | — |
| 11 | PersonNamePEOKnownAs | KNOWN_AS | — | — |
| 12 | PersonNamePEOLastName | LAST_NAME | — | ✅ |
| 13 | PersonNamePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | PersonNamePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | PersonNamePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | PersonNamePEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 17 | PersonNamePEOListName | LIST_NAME | — | ✅ |
| 18 | PersonNamePEOMiddleNames | MIDDLE_NAMES | — | ✅ |
| 19 | PersonNamePEOMilitaryRank | MILITARY_RANK | — | ✅ |
| 20 | PersonNamePEONameType | NAME_TYPE | — | ✅ |
| 21 | PersonNamePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | PersonNamePEOPersonId | PERSON_ID | — | ✅ |
| 23 | PersonNamePEOPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 24 | PersonNamePEOPreviousLastName | PREVIOUS_LAST_NAME | — | ✅ |
| 25 | PersonNamePEOSuffix | SUFFIX | — | ✅ |
| 26 | PersonNamePEOTitle | TITLE | — | ✅ |
| 27 | SupervisorNamePEODisplayName | DISPLAY_NAME | — | — |
| 28 | SupervisorNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 29 | SupervisorNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 30 | SupervisorNamePEOFirstName | FIRST_NAME | — | — |
| 31 | SupervisorNamePEOFullName | FULL_NAME | — | ✅ |
| 32 | SupervisorNamePEOHonors | HONORS | — | — |
| 33 | SupervisorNamePEOKnownAs | KNOWN_AS | — | — |
| 34 | SupervisorNamePEOLastName | LAST_NAME | — | — |
| 35 | SupervisorNamePEOListName | LIST_NAME | — | — |
| 36 | SupervisorNamePEOMiddleNames | MIDDLE_NAMES | — | — |
| 37 | SupervisorNamePEOMilitaryRank | MILITARY_RANK | — | — |
| 38 | SupervisorNamePEONameType | NAME_TYPE | — | — |
| 39 | SupervisorNamePEOPersonNameId | PERSON_NAME_ID | — | — |

### [[per_person_types_tl|PER_PERSON_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonTypesTranslationPEOLanguage | LANGUAGE | — | — |
| 2 | PersonTypesTranslationPEOPersonTypeId | PERSON_TYPE_ID | — | — |
| 3 | PersonTypesTranslationPEOUserPersonType | USER_PERSON_TYPE | — | ✅ |

### [[per_phones|PER_PHONES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PhonesEOCountryCodeNumber | COUNTRY_CODE_NUMBER | — | — |
| 2 | PhonesEOExtension | EXTENSION | — | — |
| 3 | PhonesEOPhoneId | PHONE_ID | — | — |
| 4 | PhonesEOPhoneNumber | PHONE_NUMBER | — | — |
| 5 | PhonesEOPhoneType | PHONE_TYPE | — | — |
| 6 | PhonesEOSearchPhoneNumber | SEARCH_PHONE_NUMBER | — | — |
| 7 | PhonesEOSpeedDialNumber | SPEED_DIAL_NUMBER | — | — |
| 8 | PhonesEOValidity | VALIDITY | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupervisorUserPEOActiveFlag | ACTIVE_FLAG | — | — |
| 2 | SupervisorUserPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | SupervisorUserPEOCreatedBy | CREATED_BY | — | — |
| 4 | SupervisorUserPEOCreationDate | CREATION_DATE | — | — |
| 5 | SupervisorUserPEOCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 6 | SupervisorUserPEOEndDate | END_DATE | — | — |
| 7 | SupervisorUserPEOHrTerminated | HR_TERMINATED | — | — |
| 8 | SupervisorUserPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | SupervisorUserPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | SupervisorUserPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | SupervisorUserPEOMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 12 | SupervisorUserPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | SupervisorUserPEOPartyId | PARTY_ID | — | — |
| 14 | SupervisorUserPEOPersonId | PERSON_ID | — | — |
| 15 | SupervisorUserPEOStartDate | START_DATE | — | — |
| 16 | SupervisorUserPEOSuspended | SUSPENDED | — | — |
| 17 | SupervisorUserPEOUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 18 | SupervisorUserPEOUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 19 | SupervisorUserPEOUserGuid | USER_GUID | — | — |
| 20 | SupervisorUserPEOUserId | USER_ID | — | — |
| 21 | SupervisorUserPEOUsername | USERNAME | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
