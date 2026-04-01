---
id: DOC-OTHER-PVO-ScheduledCoursePVO
doc_type: system-doc
title: "ScheduledCoursePVO — PVO Cross-Module"
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
  - ScheduledCoursePVO
  - scheduledcoursepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ScheduledCoursePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Scheduled Course. Acessa as tabelas: HER_ACADEMIC_PERIOD_VL, HER_ACADEMIC_SUBJECT_VL, HER_CURRICULUM_BUILD_STATUS_VL (+9).

**Caminho:** `FscmTopModelAM.StudentEnrollmentAM.ScheduledCoursePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 556 | 12 | 2 | 40 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[her_academic_period_vl|HER_ACADEMIC_PERIOD_VL]] — 72 atributos
- [[her_academic_subject_vl|HER_ACADEMIC_SUBJECT_VL]] — 65 atributos (3 BICC)
- [[her_curriculum_build_status_vl|HER_CURRICULUM_BUILD_STATUS_VL]] — 64 atributos (2 BICC)
- [[her_curriculum_enrollment|HER_CURRICULUM_ENROLLMENT]] — 63 atributos (7 BICC)
- [[her_curriculum_offering|HER_CURRICULUM_OFFERING]] — 64 atributos (3 BICC)
- [[her_curriculum_section|HER_CURRICULUM_SECTION]] — 76 atributos (11 BICC)
- [[her_curriculum_section_periods|HER_CURRICULUM_SECTION_PERIODS]] — 58 atributos
- [[her_curric_enrollment|HER_CURRIC_ENROLLMENT]] — 1 atributos
- [[her_curric_header_vl|HER_CURRIC_HEADER_VL]] — 79 atributos (1 PKs, 11 BICC)
- [[her_curric_offering|HER_CURRIC_OFFERING]] — 1 atributos
- [[her_curric_section|HER_CURRIC_SECTION]] — 11 atributos (1 PKs, 3 BICC)
- [[her_curric_section_periods|HER_CURRIC_SECTION_PERIODS]] — 2 atributos

---

## ⚙️ Atributos

### [[her_academic_period_vl|HER_ACADEMIC_PERIOD_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcademicPeriodPEOAcademicPeriodCode | ACADEMIC_PERIOD_CODE | — | — |
| 2 | AcademicPeriodPEOAcademicPeriodEndDt | ACADEMIC_PERIOD_END_DT | — | — |
| 3 | AcademicPeriodPEOAcademicPeriodId | ACADEMIC_PERIOD_ID | — | — |
| 4 | AcademicPeriodPEOAcademicPeriodStartDt | ACADEMIC_PERIOD_START_DT | — | — |
| 5 | AcademicPeriodPEOAcademicPeriodTypeId | ACADEMIC_PERIOD_TYPE_ID | — | — |
| 6 | AcademicPeriodPEOAttribute1 | ATTRIBUTE1 | — | — |
| 7 | AcademicPeriodPEOAttribute10 | ATTRIBUTE10 | — | — |
| 8 | AcademicPeriodPEOAttribute11 | ATTRIBUTE11 | — | — |
| 9 | AcademicPeriodPEOAttribute12 | ATTRIBUTE12 | — | — |
| 10 | AcademicPeriodPEOAttribute13 | ATTRIBUTE13 | — | — |
| 11 | AcademicPeriodPEOAttribute14 | ATTRIBUTE14 | — | — |
| 12 | AcademicPeriodPEOAttribute15 | ATTRIBUTE15 | — | — |
| 13 | AcademicPeriodPEOAttribute16 | ATTRIBUTE16 | — | — |
| 14 | AcademicPeriodPEOAttribute17 | ATTRIBUTE17 | — | — |
| 15 | AcademicPeriodPEOAttribute18 | ATTRIBUTE18 | — | — |
| 16 | AcademicPeriodPEOAttribute19 | ATTRIBUTE19 | — | — |
| 17 | AcademicPeriodPEOAttribute2 | ATTRIBUTE2 | — | — |
| 18 | AcademicPeriodPEOAttribute20 | ATTRIBUTE20 | — | — |
| 19 | AcademicPeriodPEOAttribute3 | ATTRIBUTE3 | — | — |
| 20 | AcademicPeriodPEOAttribute4 | ATTRIBUTE4 | — | — |
| 21 | AcademicPeriodPEOAttribute5 | ATTRIBUTE5 | — | — |
| 22 | AcademicPeriodPEOAttribute6 | ATTRIBUTE6 | — | — |
| 23 | AcademicPeriodPEOAttribute7 | ATTRIBUTE7 | — | — |
| 24 | AcademicPeriodPEOAttribute8 | ATTRIBUTE8 | — | — |
| 25 | AcademicPeriodPEOAttribute9 | ATTRIBUTE9 | — | — |
| 26 | AcademicPeriodPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 27 | AcademicPeriodPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 28 | AcademicPeriodPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 29 | AcademicPeriodPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 30 | AcademicPeriodPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 31 | AcademicPeriodPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 32 | AcademicPeriodPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 33 | AcademicPeriodPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 34 | AcademicPeriodPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 35 | AcademicPeriodPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 36 | AcademicPeriodPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 37 | AcademicPeriodPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 38 | AcademicPeriodPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 39 | AcademicPeriodPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 40 | AcademicPeriodPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 41 | AcademicPeriodPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 42 | AcademicPeriodPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 43 | AcademicPeriodPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 44 | AcademicPeriodPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 45 | AcademicPeriodPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 46 | AcademicPeriodPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 47 | AcademicPeriodPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 48 | AcademicPeriodPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 49 | AcademicPeriodPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 50 | AcademicPeriodPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 51 | AcademicPeriodPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 52 | AcademicPeriodPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 53 | AcademicPeriodPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 54 | AcademicPeriodPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 55 | AcademicPeriodPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 56 | AcademicPeriodPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 57 | AcademicPeriodPEOCalId | CAL_ID | — | — |
| 58 | AcademicPeriodPEOCalendarDateFlag | CALENDAR_DATE_FLAG | — | — |
| 59 | AcademicPeriodPEOCalendarItemId | CALENDAR_ITEM_ID | — | — |
| 60 | AcademicPeriodPEOCreatedBy | CREATED_BY | — | — |
| 61 | AcademicPeriodPEOCreationDate | CREATION_DATE | — | — |
| 62 | AcademicPeriodPEODescription | DESCRIPTION | — | — |
| 63 | AcademicPeriodPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 64 | AcademicPeriodPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 65 | AcademicPeriodPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 66 | AcademicPeriodPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 67 | AcademicPeriodPEOPeriodCategoryCode | PERIOD_CATEGORY_CODE | — | — |
| 68 | AcademicPeriodPEOPeriodName | PERIOD_NAME | — | — |
| 69 | AcademicPeriodPEOPeriodTierCode | PERIOD_TIER_CODE | — | — |
| 70 | AcademicPeriodPEOSetId | SET_ID | — | — |
| 71 | AcademicPeriodPEOSystemGeneratedFlag | SYSTEM_GENERATED_FLAG | — | — |
| 72 | AcademicPeriodPEOWeeksOfInstruction | WEEKS_OF_INSTRUCTION | — | — |

### [[her_academic_subject_vl|HER_ACADEMIC_SUBJECT_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcademicSubjectDPEOAcademicSubjectCode | ACADEMIC_SUBJECT_CODE | — | ✅ |
| 2 | AcademicSubjectDPEOAcademicSubjectId | ACADEMIC_SUBJECT_ID | — | — |
| 3 | AcademicSubjectDPEOAcademicSubjectName | ACADEMIC_SUBJECT_NAME | — | — |
| 4 | AcademicSubjectDPEOActiveFlag | ACTIVE_FLAG | — | — |
| 5 | AcademicSubjectDPEOAttribute1 | ATTRIBUTE1 | — | — |
| 6 | AcademicSubjectDPEOAttribute10 | ATTRIBUTE10 | — | — |
| 7 | AcademicSubjectDPEOAttribute11 | ATTRIBUTE11 | — | — |
| 8 | AcademicSubjectDPEOAttribute12 | ATTRIBUTE12 | — | — |
| 9 | AcademicSubjectDPEOAttribute13 | ATTRIBUTE13 | — | — |
| 10 | AcademicSubjectDPEOAttribute14 | ATTRIBUTE14 | — | — |
| 11 | AcademicSubjectDPEOAttribute15 | ATTRIBUTE15 | — | — |
| 12 | AcademicSubjectDPEOAttribute16 | ATTRIBUTE16 | — | — |
| 13 | AcademicSubjectDPEOAttribute17 | ATTRIBUTE17 | — | — |
| 14 | AcademicSubjectDPEOAttribute18 | ATTRIBUTE18 | — | — |
| 15 | AcademicSubjectDPEOAttribute19 | ATTRIBUTE19 | — | — |
| 16 | AcademicSubjectDPEOAttribute2 | ATTRIBUTE2 | — | — |
| 17 | AcademicSubjectDPEOAttribute20 | ATTRIBUTE20 | — | — |
| 18 | AcademicSubjectDPEOAttribute3 | ATTRIBUTE3 | — | — |
| 19 | AcademicSubjectDPEOAttribute4 | ATTRIBUTE4 | — | — |
| 20 | AcademicSubjectDPEOAttribute5 | ATTRIBUTE5 | — | — |
| 21 | AcademicSubjectDPEOAttribute6 | ATTRIBUTE6 | — | — |
| 22 | AcademicSubjectDPEOAttribute7 | ATTRIBUTE7 | — | — |
| 23 | AcademicSubjectDPEOAttribute8 | ATTRIBUTE8 | — | — |
| 24 | AcademicSubjectDPEOAttribute9 | ATTRIBUTE9 | — | — |
| 25 | AcademicSubjectDPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 26 | AcademicSubjectDPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 27 | AcademicSubjectDPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 28 | AcademicSubjectDPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 29 | AcademicSubjectDPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 30 | AcademicSubjectDPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 31 | AcademicSubjectDPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 32 | AcademicSubjectDPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 33 | AcademicSubjectDPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 34 | AcademicSubjectDPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 35 | AcademicSubjectDPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 36 | AcademicSubjectDPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 37 | AcademicSubjectDPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 38 | AcademicSubjectDPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 39 | AcademicSubjectDPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 40 | AcademicSubjectDPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 41 | AcademicSubjectDPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 42 | AcademicSubjectDPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 43 | AcademicSubjectDPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 44 | AcademicSubjectDPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 45 | AcademicSubjectDPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 46 | AcademicSubjectDPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 47 | AcademicSubjectDPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 48 | AcademicSubjectDPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 49 | AcademicSubjectDPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 50 | AcademicSubjectDPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 51 | AcademicSubjectDPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 52 | AcademicSubjectDPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 53 | AcademicSubjectDPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 54 | AcademicSubjectDPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 55 | AcademicSubjectDPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 56 | AcademicSubjectDPEOCreatedBy | CREATED_BY | — | — |
| 57 | AcademicSubjectDPEOCreationDate | CREATION_DATE | — | — |
| 58 | AcademicSubjectDPEODescription | DESCRIPTION | — | — |
| 59 | AcademicSubjectDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 60 | AcademicSubjectDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 61 | AcademicSubjectDPEOInstitutionId | INSTITUTION_ID | — | — |
| 62 | AcademicSubjectDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 63 | AcademicSubjectDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 64 | AcademicSubjectDPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 65 | AcademicSubjectDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[her_curriculum_build_status_vl|HER_CURRICULUM_BUILD_STATUS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurriculumBuildStatusPEOActiveFlag | ACTIVE_FLAG | — | — |
| 2 | CurriculumBuildStatusPEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | CurriculumBuildStatusPEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | CurriculumBuildStatusPEOAttribute11 | ATTRIBUTE11 | — | — |
| 5 | CurriculumBuildStatusPEOAttribute12 | ATTRIBUTE12 | — | — |
| 6 | CurriculumBuildStatusPEOAttribute13 | ATTRIBUTE13 | — | — |
| 7 | CurriculumBuildStatusPEOAttribute14 | ATTRIBUTE14 | — | — |
| 8 | CurriculumBuildStatusPEOAttribute15 | ATTRIBUTE15 | — | — |
| 9 | CurriculumBuildStatusPEOAttribute16 | ATTRIBUTE16 | — | — |
| 10 | CurriculumBuildStatusPEOAttribute17 | ATTRIBUTE17 | — | — |
| 11 | CurriculumBuildStatusPEOAttribute18 | ATTRIBUTE18 | — | — |
| 12 | CurriculumBuildStatusPEOAttribute19 | ATTRIBUTE19 | — | — |
| 13 | CurriculumBuildStatusPEOAttribute2 | ATTRIBUTE2 | — | — |
| 14 | CurriculumBuildStatusPEOAttribute20 | ATTRIBUTE20 | — | — |
| 15 | CurriculumBuildStatusPEOAttribute3 | ATTRIBUTE3 | — | — |
| 16 | CurriculumBuildStatusPEOAttribute4 | ATTRIBUTE4 | — | — |
| 17 | CurriculumBuildStatusPEOAttribute5 | ATTRIBUTE5 | — | — |
| 18 | CurriculumBuildStatusPEOAttribute6 | ATTRIBUTE6 | — | — |
| 19 | CurriculumBuildStatusPEOAttribute7 | ATTRIBUTE7 | — | — |
| 20 | CurriculumBuildStatusPEOAttribute8 | ATTRIBUTE8 | — | — |
| 21 | CurriculumBuildStatusPEOAttribute9 | ATTRIBUTE9 | — | — |
| 22 | CurriculumBuildStatusPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 23 | CurriculumBuildStatusPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | CurriculumBuildStatusPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 25 | CurriculumBuildStatusPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 26 | CurriculumBuildStatusPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 27 | CurriculumBuildStatusPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 28 | CurriculumBuildStatusPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 29 | CurriculumBuildStatusPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 30 | CurriculumBuildStatusPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 31 | CurriculumBuildStatusPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 32 | CurriculumBuildStatusPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 33 | CurriculumBuildStatusPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 34 | CurriculumBuildStatusPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 35 | CurriculumBuildStatusPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 36 | CurriculumBuildStatusPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 37 | CurriculumBuildStatusPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 38 | CurriculumBuildStatusPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 39 | CurriculumBuildStatusPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 40 | CurriculumBuildStatusPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 41 | CurriculumBuildStatusPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 42 | CurriculumBuildStatusPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 43 | CurriculumBuildStatusPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 44 | CurriculumBuildStatusPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 45 | CurriculumBuildStatusPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 46 | CurriculumBuildStatusPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 47 | CurriculumBuildStatusPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 48 | CurriculumBuildStatusPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 49 | CurriculumBuildStatusPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 50 | CurriculumBuildStatusPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 51 | CurriculumBuildStatusPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 52 | CurriculumBuildStatusPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 53 | CurriculumBuildStatusPEOBuildStatusCode | BUILD_STATUS_CODE | — | — |
| 54 | CurriculumBuildStatusPEOBuildStatusSortNum | BUILD_STATUS_SORT_NUM | — | — |
| 55 | CurriculumBuildStatusPEOCreatedBy | CREATED_BY | — | — |
| 56 | CurriculumBuildStatusPEOCreationDate | CREATION_DATE | — | — |
| 57 | CurriculumBuildStatusPEOCurriculumBuildStatusId | CURRICULUM_BUILD_STATUS_ID | — | — |
| 58 | CurriculumBuildStatusPEODescription | DESCRIPTION | — | — |
| 59 | CurriculumBuildStatusPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 60 | CurriculumBuildStatusPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 61 | CurriculumBuildStatusPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 62 | CurriculumBuildStatusPEONameDisplay | NAME_DISPLAY | — | ✅ |
| 63 | CurriculumBuildStatusPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 64 | CurriculumBuildStatusPEOSystemStatusCode | SYSTEM_STATUS_CODE | — | — |

### [[her_curriculum_enrollment|HER_CURRICULUM_ENROLLMENT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurriculumEnrollmentPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | CurriculumEnrollmentPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | CurriculumEnrollmentPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | CurriculumEnrollmentPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | CurriculumEnrollmentPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | CurriculumEnrollmentPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | CurriculumEnrollmentPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | CurriculumEnrollmentPEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | CurriculumEnrollmentPEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | CurriculumEnrollmentPEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | CurriculumEnrollmentPEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | CurriculumEnrollmentPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | CurriculumEnrollmentPEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | CurriculumEnrollmentPEOAttribute3 | ATTRIBUTE3 | — | — |
| 15 | CurriculumEnrollmentPEOAttribute4 | ATTRIBUTE4 | — | — |
| 16 | CurriculumEnrollmentPEOAttribute5 | ATTRIBUTE5 | — | — |
| 17 | CurriculumEnrollmentPEOAttribute6 | ATTRIBUTE6 | — | — |
| 18 | CurriculumEnrollmentPEOAttribute7 | ATTRIBUTE7 | — | — |
| 19 | CurriculumEnrollmentPEOAttribute8 | ATTRIBUTE8 | — | — |
| 20 | CurriculumEnrollmentPEOAttribute9 | ATTRIBUTE9 | — | — |
| 21 | CurriculumEnrollmentPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | CurriculumEnrollmentPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | CurriculumEnrollmentPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 24 | CurriculumEnrollmentPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | CurriculumEnrollmentPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | CurriculumEnrollmentPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | CurriculumEnrollmentPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | CurriculumEnrollmentPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 29 | CurriculumEnrollmentPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 30 | CurriculumEnrollmentPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 31 | CurriculumEnrollmentPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 32 | CurriculumEnrollmentPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 33 | CurriculumEnrollmentPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 34 | CurriculumEnrollmentPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 35 | CurriculumEnrollmentPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 36 | CurriculumEnrollmentPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 37 | CurriculumEnrollmentPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 38 | CurriculumEnrollmentPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 39 | CurriculumEnrollmentPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 40 | CurriculumEnrollmentPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 41 | CurriculumEnrollmentPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 42 | CurriculumEnrollmentPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 43 | CurriculumEnrollmentPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 44 | CurriculumEnrollmentPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 45 | CurriculumEnrollmentPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 46 | CurriculumEnrollmentPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 47 | CurriculumEnrollmentPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 48 | CurriculumEnrollmentPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 49 | CurriculumEnrollmentPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 50 | CurriculumEnrollmentPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 51 | CurriculumEnrollmentPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 52 | CurriculumEnrollmentPEOCreatedBy | CREATED_BY | — | — |
| 53 | CurriculumEnrollmentPEOCreationDate | CREATION_DATE | — | — |
| 54 | CurriculumEnrollmentPEOEnrollmentCapacity | ENROLLMENT_CAPACITY | — | ✅ |
| 55 | CurriculumEnrollmentPEOEnrollmentStatusCode | ENROLLMENT_STATUS_CODE | — | ✅ |
| 56 | CurriculumEnrollmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 57 | CurriculumEnrollmentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 58 | CurriculumEnrollmentPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 59 | CurriculumEnrollmentPEOMinimumEnrollment | MINIMUM_ENROLLMENT | — | ✅ |
| 60 | CurriculumEnrollmentPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 61 | CurriculumEnrollmentPEOTotalEnrolled | TOTAL_ENROLLED | — | ✅ |
| 62 | CurriculumEnrollmentPEOTotalWaitlisted | TOTAL_WAITLISTED | — | ✅ |
| 63 | CurriculumEnrollmentPEOWaitlistCapacity | WAITLIST_CAPACITY | — | ✅ |

### [[her_curriculum_offering|HER_CURRICULUM_OFFERING]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurriculumOfferPEOAcademicLevelId | ACADEMIC_LEVEL_ID | — | — |
| 2 | CurriculumOfferPEOAcademicSubjectId | ACADEMIC_SUBJECT_ID | — | — |
| 3 | CurriculumOfferPEOAttribute1 | ATTRIBUTE1 | — | — |
| 4 | CurriculumOfferPEOAttribute10 | ATTRIBUTE10 | — | — |
| 5 | CurriculumOfferPEOAttribute11 | ATTRIBUTE11 | — | — |
| 6 | CurriculumOfferPEOAttribute12 | ATTRIBUTE12 | — | — |
| 7 | CurriculumOfferPEOAttribute13 | ATTRIBUTE13 | — | — |
| 8 | CurriculumOfferPEOAttribute14 | ATTRIBUTE14 | — | — |
| 9 | CurriculumOfferPEOAttribute15 | ATTRIBUTE15 | — | — |
| 10 | CurriculumOfferPEOAttribute16 | ATTRIBUTE16 | — | — |
| 11 | CurriculumOfferPEOAttribute17 | ATTRIBUTE17 | — | — |
| 12 | CurriculumOfferPEOAttribute18 | ATTRIBUTE18 | — | — |
| 13 | CurriculumOfferPEOAttribute19 | ATTRIBUTE19 | — | — |
| 14 | CurriculumOfferPEOAttribute2 | ATTRIBUTE2 | — | — |
| 15 | CurriculumOfferPEOAttribute20 | ATTRIBUTE20 | — | — |
| 16 | CurriculumOfferPEOAttribute3 | ATTRIBUTE3 | — | — |
| 17 | CurriculumOfferPEOAttribute4 | ATTRIBUTE4 | — | — |
| 18 | CurriculumOfferPEOAttribute5 | ATTRIBUTE5 | — | — |
| 19 | CurriculumOfferPEOAttribute6 | ATTRIBUTE6 | — | — |
| 20 | CurriculumOfferPEOAttribute7 | ATTRIBUTE7 | — | — |
| 21 | CurriculumOfferPEOAttribute8 | ATTRIBUTE8 | — | — |
| 22 | CurriculumOfferPEOAttribute9 | ATTRIBUTE9 | — | — |
| 23 | CurriculumOfferPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 24 | CurriculumOfferPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 25 | CurriculumOfferPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 26 | CurriculumOfferPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 27 | CurriculumOfferPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 28 | CurriculumOfferPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 29 | CurriculumOfferPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 30 | CurriculumOfferPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 31 | CurriculumOfferPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 32 | CurriculumOfferPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 33 | CurriculumOfferPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 34 | CurriculumOfferPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 35 | CurriculumOfferPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 36 | CurriculumOfferPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 37 | CurriculumOfferPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 38 | CurriculumOfferPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 39 | CurriculumOfferPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 40 | CurriculumOfferPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 41 | CurriculumOfferPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 42 | CurriculumOfferPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 43 | CurriculumOfferPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 44 | CurriculumOfferPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 45 | CurriculumOfferPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 46 | CurriculumOfferPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 47 | CurriculumOfferPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 48 | CurriculumOfferPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 49 | CurriculumOfferPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 50 | CurriculumOfferPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 51 | CurriculumOfferPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 52 | CurriculumOfferPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 53 | CurriculumOfferPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 54 | CurriculumOfferPEOCreatedBy | CREATED_BY | — | — |
| 55 | CurriculumOfferPEOCreationDate | CREATION_DATE | — | — |
| 56 | CurriculumOfferPEOCredentialId | CREDENTIAL_ID | — | ✅ |
| 57 | CurriculumOfferPEOCreditTypeCode | CREDIT_TYPE_CODE | — | — |
| 58 | CurriculumOfferPEOCurriculumCatalogNumber | CURRICULUM_CATALOG_NUMBER | — | ✅ |
| 59 | CurriculumOfferPEOInstitutionId | INSTITUTION_ID | — | — |
| 60 | CurriculumOfferPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 61 | CurriculumOfferPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 62 | CurriculumOfferPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 63 | CurriculumOfferPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 64 | CurriculumOfferPEOOfferSeqNum | OFFER_SEQ_NUM | — | — |

### [[her_curriculum_section|HER_CURRICULUM_SECTION]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurriculumSectionExtensionPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | CurriculumSectionExtensionPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | CurriculumSectionExtensionPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | CurriculumSectionExtensionPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | CurriculumSectionExtensionPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | CurriculumSectionExtensionPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | CurriculumSectionExtensionPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | CurriculumSectionExtensionPEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | CurriculumSectionExtensionPEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | CurriculumSectionExtensionPEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | CurriculumSectionExtensionPEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | CurriculumSectionExtensionPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | CurriculumSectionExtensionPEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | CurriculumSectionExtensionPEOAttribute3 | ATTRIBUTE3 | — | — |
| 15 | CurriculumSectionExtensionPEOAttribute4 | ATTRIBUTE4 | — | — |
| 16 | CurriculumSectionExtensionPEOAttribute5 | ATTRIBUTE5 | — | — |
| 17 | CurriculumSectionExtensionPEOAttribute6 | ATTRIBUTE6 | — | — |
| 18 | CurriculumSectionExtensionPEOAttribute7 | ATTRIBUTE7 | — | — |
| 19 | CurriculumSectionExtensionPEOAttribute8 | ATTRIBUTE8 | — | — |
| 20 | CurriculumSectionExtensionPEOAttribute9 | ATTRIBUTE9 | — | — |
| 21 | CurriculumSectionExtensionPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | CurriculumSectionExtensionPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | CurriculumSectionExtensionPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 24 | CurriculumSectionExtensionPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | CurriculumSectionExtensionPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | CurriculumSectionExtensionPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | CurriculumSectionExtensionPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | CurriculumSectionExtensionPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 29 | CurriculumSectionExtensionPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 30 | CurriculumSectionExtensionPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 31 | CurriculumSectionExtensionPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 32 | CurriculumSectionExtensionPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 33 | CurriculumSectionExtensionPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 34 | CurriculumSectionExtensionPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 35 | CurriculumSectionExtensionPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 36 | CurriculumSectionExtensionPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 37 | CurriculumSectionExtensionPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 38 | CurriculumSectionExtensionPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 39 | CurriculumSectionExtensionPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 40 | CurriculumSectionExtensionPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 41 | CurriculumSectionExtensionPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 42 | CurriculumSectionExtensionPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 43 | CurriculumSectionExtensionPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 44 | CurriculumSectionExtensionPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 45 | CurriculumSectionExtensionPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 46 | CurriculumSectionExtensionPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 47 | CurriculumSectionExtensionPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 48 | CurriculumSectionExtensionPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 49 | CurriculumSectionExtensionPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 50 | CurriculumSectionExtensionPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 51 | CurriculumSectionExtensionPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 52 | CurriculumSectionExtensionPEOClassFeesOvrdFlag | CLASS_FEES_OVRD_FLAG | — | — |
| 53 | CurriculumSectionExtensionPEOCombinedSectionFlag | COMBINED_SECTION_FLAG | — | — |
| 54 | CurriculumSectionExtensionPEOCreatedBy | CREATED_BY | — | — |
| 55 | CurriculumSectionExtensionPEOCreationDate | CREATION_DATE | — | — |
| 56 | CurriculumSectionExtensionPEODateControlCode | DATE_CONTROL_CODE | — | ✅ |
| 57 | CurriculumSectionExtensionPEOExcludeFromPeriodFeesFlag | EXCLUDE_FROM_PERIOD_FEES_FLAG | — | — |
| 58 | CurriculumSectionExtensionPEOFacilityAssignedFlag | FACILITY_ASSIGNED_FLAG | — | ✅ |
| 59 | CurriculumSectionExtensionPEOIncludeOwnerItemMsgsFlag | INCLUDE_OWNER_ITEM_MSGS_FLAG | — | — |
| 60 | CurriculumSectionExtensionPEOInstructorAssignedFlag | INSTRUCTOR_ASSIGNED_FLAG | — | ✅ |
| 61 | CurriculumSectionExtensionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 62 | CurriculumSectionExtensionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 63 | CurriculumSectionExtensionPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 64 | CurriculumSectionExtensionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 65 | CurriculumSectionExtensionPEOOwningCampusId | OWNING_CAMPUS_ID | — | — |
| 66 | CurriculumSectionExtensionPEOOwningCurriculumId | OWNING_CURRICULUM_ID | — | ✅ |
| 67 | CurriculumSectionExtensionPEOOwningOfferNum | OWNING_OFFER_NUM | — | ✅ |
| 68 | CurriculumSectionExtensionPEOOwningOrgId | OWNING_ORG_ID | — | — |
| 69 | CurriculumSectionExtensionPEOSectionCourseCode | SECTION_COURSE_CODE | — | ✅ |
| 70 | CurriculumSectionExtensionPEOSectionEndDate | SECTION_END_DATE | — | ✅ |
| 71 | CurriculumSectionExtensionPEOSectionNum | SECTION_NUM | — | — |
| 72 | CurriculumSectionExtensionPEOSectionStartDate | SECTION_START_DATE | — | ✅ |
| 73 | CurriculumSectionExtensionPEOSectionStatusCode | SECTION_STATUS_CODE | — | ✅ |
| 74 | CurriculumSectionExtensionPEOSectionTypeCode | SECTION_TYPE_CODE | — | — |
| 75 | CurriculumSectionExtensionPEOSelfPacedFlag | SELF_PACED_FLAG | — | ✅ |
| 76 | CurriculumSectionExtensionPEOTopicSeqNum | TOPIC_SEQ_NUM | — | — |

### [[her_curriculum_section_periods|HER_CURRICULUM_SECTION_PERIODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurriculumSectionPeriodPEOAcademicPeriodId | ACADEMIC_PERIOD_ID | — | — |
| 2 | CurriculumSectionPeriodPEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | CurriculumSectionPeriodPEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | CurriculumSectionPeriodPEOAttribute11 | ATTRIBUTE11 | — | — |
| 5 | CurriculumSectionPeriodPEOAttribute12 | ATTRIBUTE12 | — | — |
| 6 | CurriculumSectionPeriodPEOAttribute13 | ATTRIBUTE13 | — | — |
| 7 | CurriculumSectionPeriodPEOAttribute14 | ATTRIBUTE14 | — | — |
| 8 | CurriculumSectionPeriodPEOAttribute15 | ATTRIBUTE15 | — | — |
| 9 | CurriculumSectionPeriodPEOAttribute16 | ATTRIBUTE16 | — | — |
| 10 | CurriculumSectionPeriodPEOAttribute17 | ATTRIBUTE17 | — | — |
| 11 | CurriculumSectionPeriodPEOAttribute18 | ATTRIBUTE18 | — | — |
| 12 | CurriculumSectionPeriodPEOAttribute19 | ATTRIBUTE19 | — | — |
| 13 | CurriculumSectionPeriodPEOAttribute2 | ATTRIBUTE2 | — | — |
| 14 | CurriculumSectionPeriodPEOAttribute20 | ATTRIBUTE20 | — | — |
| 15 | CurriculumSectionPeriodPEOAttribute3 | ATTRIBUTE3 | — | — |
| 16 | CurriculumSectionPeriodPEOAttribute4 | ATTRIBUTE4 | — | — |
| 17 | CurriculumSectionPeriodPEOAttribute5 | ATTRIBUTE5 | — | — |
| 18 | CurriculumSectionPeriodPEOAttribute6 | ATTRIBUTE6 | — | — |
| 19 | CurriculumSectionPeriodPEOAttribute7 | ATTRIBUTE7 | — | — |
| 20 | CurriculumSectionPeriodPEOAttribute8 | ATTRIBUTE8 | — | — |
| 21 | CurriculumSectionPeriodPEOAttribute9 | ATTRIBUTE9 | — | — |
| 22 | CurriculumSectionPeriodPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 23 | CurriculumSectionPeriodPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | CurriculumSectionPeriodPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 25 | CurriculumSectionPeriodPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 26 | CurriculumSectionPeriodPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 27 | CurriculumSectionPeriodPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 28 | CurriculumSectionPeriodPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 29 | CurriculumSectionPeriodPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 30 | CurriculumSectionPeriodPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 31 | CurriculumSectionPeriodPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 32 | CurriculumSectionPeriodPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 33 | CurriculumSectionPeriodPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 34 | CurriculumSectionPeriodPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 35 | CurriculumSectionPeriodPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 36 | CurriculumSectionPeriodPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 37 | CurriculumSectionPeriodPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 38 | CurriculumSectionPeriodPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 39 | CurriculumSectionPeriodPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 40 | CurriculumSectionPeriodPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 41 | CurriculumSectionPeriodPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 42 | CurriculumSectionPeriodPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 43 | CurriculumSectionPeriodPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 44 | CurriculumSectionPeriodPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 45 | CurriculumSectionPeriodPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 46 | CurriculumSectionPeriodPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 47 | CurriculumSectionPeriodPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 48 | CurriculumSectionPeriodPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 49 | CurriculumSectionPeriodPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 50 | CurriculumSectionPeriodPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 51 | CurriculumSectionPeriodPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 52 | CurriculumSectionPeriodPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 53 | CurriculumSectionPeriodPEOCreatedBy | CREATED_BY | — | — |
| 54 | CurriculumSectionPeriodPEOCreationDate | CREATION_DATE | — | — |
| 55 | CurriculumSectionPeriodPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 56 | CurriculumSectionPeriodPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 57 | CurriculumSectionPeriodPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 58 | CurriculumSectionPeriodPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[her_curric_enrollment|HER_CURRIC_ENROLLMENT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurriculumSectionEnrollmentPEOCurriculumEnrollmentId | CURRICULUM_ENROLLMENT_ID | — | — |

### [[her_curric_header_vl|HER_CURRIC_HEADER_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurriculumHeaderDPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | CurriculumHeaderDPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | CurriculumHeaderDPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | CurriculumHeaderDPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | CurriculumHeaderDPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | CurriculumHeaderDPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | CurriculumHeaderDPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | CurriculumHeaderDPEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | CurriculumHeaderDPEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | CurriculumHeaderDPEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | CurriculumHeaderDPEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | CurriculumHeaderDPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | CurriculumHeaderDPEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | CurriculumHeaderDPEOAttribute3 | ATTRIBUTE3 | — | — |
| 15 | CurriculumHeaderDPEOAttribute4 | ATTRIBUTE4 | — | — |
| 16 | CurriculumHeaderDPEOAttribute5 | ATTRIBUTE5 | — | — |
| 17 | CurriculumHeaderDPEOAttribute6 | ATTRIBUTE6 | — | — |
| 18 | CurriculumHeaderDPEOAttribute7 | ATTRIBUTE7 | — | — |
| 19 | CurriculumHeaderDPEOAttribute8 | ATTRIBUTE8 | — | — |
| 20 | CurriculumHeaderDPEOAttribute9 | ATTRIBUTE9 | — | — |
| 21 | CurriculumHeaderDPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | CurriculumHeaderDPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | CurriculumHeaderDPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 24 | CurriculumHeaderDPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | CurriculumHeaderDPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | CurriculumHeaderDPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | CurriculumHeaderDPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | CurriculumHeaderDPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 29 | CurriculumHeaderDPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 30 | CurriculumHeaderDPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 31 | CurriculumHeaderDPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 32 | CurriculumHeaderDPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 33 | CurriculumHeaderDPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 34 | CurriculumHeaderDPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 35 | CurriculumHeaderDPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 36 | CurriculumHeaderDPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 37 | CurriculumHeaderDPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 38 | CurriculumHeaderDPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 39 | CurriculumHeaderDPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 40 | CurriculumHeaderDPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 41 | CurriculumHeaderDPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 42 | CurriculumHeaderDPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 43 | CurriculumHeaderDPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 44 | CurriculumHeaderDPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 45 | CurriculumHeaderDPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 46 | CurriculumHeaderDPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 47 | CurriculumHeaderDPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 48 | CurriculumHeaderDPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 49 | CurriculumHeaderDPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 50 | CurriculumHeaderDPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 51 | CurriculumHeaderDPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 52 | CurriculumHeaderDPEOCalId | CAL_ID | — | — |
| 53 | CurriculumHeaderDPEOCartEnabledFlag | CART_ENABLED_FLAG | — | — |
| 54 | CurriculumHeaderDPEOCreatedBy | CREATED_BY | — | — |
| 55 | CurriculumHeaderDPEOCreationDate | CREATION_DATE | — | — |
| 56 | CurriculumHeaderDPEOCurriculumBuildStatusId | CURRICULUM_BUILD_STATUS_ID | — | ✅ |
| 57 | CurriculumHeaderDPEOCurriculumFormatCode | CURRICULUM_FORMAT_CODE | — | ✅ |
| 58 | CurriculumHeaderDPEOCurriculumHeaderId | CURRICULUM_HEADER_ID | 🔑 | ✅ |
| 59 | CurriculumHeaderDPEOCurriculumId | CURRICULUM_ID | — | ✅ |
| 60 | CurriculumHeaderDPEOCurriculumItemLastUpdate | CURRICULUM_ITEM_LAST_UPDATE | — | — |
| 61 | CurriculumHeaderDPEOCurriculumLongDescr | CURRICULUM_LONG_DESCR | — | — |
| 62 | CurriculumHeaderDPEOCurriculumName | CURRICULUM_NAME | — | ✅ |
| 63 | CurriculumHeaderDPEOCurriculumNameCode | CURRICULUM_NAME_CODE | — | — |
| 64 | CurriculumHeaderDPEOCurriculumStatusCode | CURRICULUM_STATUS_CODE | — | ✅ |
| 65 | CurriculumHeaderDPEOCurriculumTitle | CURRICULUM_TITLE | — | ✅ |
| 66 | CurriculumHeaderDPEOCurriculumTypeId | CURRICULUM_TYPE_ID | — | — |
| 67 | CurriculumHeaderDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 68 | CurriculumHeaderDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 69 | CurriculumHeaderDPEOEnableOsnFlag | ENABLE_OSN_FLAG | — | — |
| 70 | CurriculumHeaderDPEOEndAcademicPeriodId | END_ACADEMIC_PERIOD_ID | — | — |
| 71 | CurriculumHeaderDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 72 | CurriculumHeaderDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 73 | CurriculumHeaderDPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 74 | CurriculumHeaderDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 75 | CurriculumHeaderDPEOSearchEnabledFlag | SEARCH_ENABLED_FLAG | — | — |
| 76 | CurriculumHeaderDPEOStartAcademicPeriodId | START_ACADEMIC_PERIOD_ID | — | — |
| 77 | CurriculumHeaderDPEOSystemStatusCode | SYSTEM_STATUS_CODE | — | ✅ |
| 78 | CurriculumHeaderDPEOTemplateId | TEMPLATE_ID | — | — |
| 79 | CurriculumHeaderDPEOWishlistEnabledFlag | WISHLIST_ENABLED_FLAG | — | — |

### [[her_curric_offering|HER_CURRIC_OFFERING]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurriculumOfferPEOCurriculumOfferingId | CURRICULUM_OFFERING_ID | — | — |

### [[her_curric_section|HER_CURRIC_SECTION]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurriculumSectionExtensionPEOBillingUnits | BILLING_UNITS | — | — |
| 2 | CurriculumSectionExtensionPEOContactHours | CONTACT_HOURS | — | — |
| 3 | CurriculumSectionExtensionPEOContactHoursRangeTypeCode | CONTACT_HOURS_RANGE_TYPE_CODE | — | — |
| 4 | CurriculumSectionExtensionPEOCurriculumSectionId | CURRICULUM_SECTION_ID | 🔑 | ✅ |
| 5 | CurriculumSectionExtensionPEOMaxContactHours | MAX_CONTACT_HOURS | — | — |
| 6 | CurriculumSectionExtensionPEOMaxUnits | MAX_UNITS | — | ✅ |
| 7 | CurriculumSectionExtensionPEOMinUnits | MIN_UNITS | — | ✅ |
| 8 | CurriculumSectionExtensionPEOOverridePrereqFlag | OVERRIDE_PREREQ_FLAG | — | — |
| 9 | CurriculumSectionExtensionPEOOverrideProgreqFlag | OVERRIDE_PROGREQ_FLAG | — | — |
| 10 | CurriculumSectionExtensionPEOOwningCurriculumHeaderId | OWNING_CURRICULUM_HEADER_ID | — | — |
| 11 | CurriculumSectionExtensionPEOUnitRangeTypeCode | UNIT_RANGE_TYPE_CODE | — | — |

### [[her_curric_section_periods|HER_CURRIC_SECTION_PERIODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurriculumSectionPeriodPEOCurriculumPeriodId | CURRICULUM_PERIOD_ID | — | — |
| 2 | CurriculumSectionPeriodPEOCurriculumSectionId | CURRICULUM_SECTION_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
