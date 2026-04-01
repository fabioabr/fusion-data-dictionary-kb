---
id: DOC-OTHER-PVO-StudentResultPVO
doc_type: system-doc
title: "StudentResultPVO — PVO Cross-Module"
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
  - StudentResultPVO
  - studentresultpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# StudentResultPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Student Result. Acessa as tabelas: HER_SCT_CUR_RESULT_VL, HER_SCT_ITEM, HER_SCT_SECTION.

**Caminho:** `FscmTopModelAM.StudentEnrollmentAM.StudentResultPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 224 | 3 | 1 | 16 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[her_sct_cur_result_vl|HER_SCT_CUR_RESULT_VL]] — 77 atributos (1 PKs, 13 BICC)
- [[her_sct_item|HER_SCT_ITEM]] — 71 atributos (1 BICC)
- [[her_sct_section|HER_SCT_SECTION]] — 76 atributos (2 BICC)

---

## ⚙️ Atributos

### [[her_sct_cur_result_vl|HER_SCT_CUR_RESULT_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SctResultPEOAcademicLevelId | ACADEMIC_LEVEL_ID | — | — |
| 2 | SctResultPEOAcademicPeriodId | ACADEMIC_PERIOD_ID | — | — |
| 3 | SctResultPEOAdministrationNotes | ADMINISTRATION_NOTES | — | ✅ |
| 4 | SctResultPEOAttribute1 | ATTRIBUTE1 | — | — |
| 5 | SctResultPEOAttribute10 | ATTRIBUTE10 | — | — |
| 6 | SctResultPEOAttribute11 | ATTRIBUTE11 | — | — |
| 7 | SctResultPEOAttribute12 | ATTRIBUTE12 | — | — |
| 8 | SctResultPEOAttribute13 | ATTRIBUTE13 | — | — |
| 9 | SctResultPEOAttribute14 | ATTRIBUTE14 | — | — |
| 10 | SctResultPEOAttribute15 | ATTRIBUTE15 | — | — |
| 11 | SctResultPEOAttribute16 | ATTRIBUTE16 | — | — |
| 12 | SctResultPEOAttribute17 | ATTRIBUTE17 | — | — |
| 13 | SctResultPEOAttribute18 | ATTRIBUTE18 | — | — |
| 14 | SctResultPEOAttribute19 | ATTRIBUTE19 | — | — |
| 15 | SctResultPEOAttribute2 | ATTRIBUTE2 | — | — |
| 16 | SctResultPEOAttribute20 | ATTRIBUTE20 | — | — |
| 17 | SctResultPEOAttribute3 | ATTRIBUTE3 | — | — |
| 18 | SctResultPEOAttribute4 | ATTRIBUTE4 | — | — |
| 19 | SctResultPEOAttribute5 | ATTRIBUTE5 | — | — |
| 20 | SctResultPEOAttribute6 | ATTRIBUTE6 | — | — |
| 21 | SctResultPEOAttribute7 | ATTRIBUTE7 | — | — |
| 22 | SctResultPEOAttribute8 | ATTRIBUTE8 | — | — |
| 23 | SctResultPEOAttribute9 | ATTRIBUTE9 | — | — |
| 24 | SctResultPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 25 | SctResultPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 26 | SctResultPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 27 | SctResultPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 28 | SctResultPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 29 | SctResultPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 30 | SctResultPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 31 | SctResultPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 32 | SctResultPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 33 | SctResultPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 34 | SctResultPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 35 | SctResultPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 36 | SctResultPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 37 | SctResultPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 38 | SctResultPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 39 | SctResultPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 40 | SctResultPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 41 | SctResultPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 42 | SctResultPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 43 | SctResultPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 44 | SctResultPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 45 | SctResultPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 46 | SctResultPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 47 | SctResultPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 48 | SctResultPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 49 | SctResultPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 50 | SctResultPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 51 | SctResultPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 52 | SctResultPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 53 | SctResultPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 54 | SctResultPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 55 | SctResultPEOCreatedBy | CREATED_BY | — | — |
| 56 | SctResultPEOCreationDate | CREATION_DATE | — | ✅ |
| 57 | SctResultPEODerivedResultId | DERIVED_RESULT_ID | — | — |
| 58 | SctResultPEODerivedResultType | DERIVED_RESULT_TYPE | — | — |
| 59 | SctResultPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 60 | SctResultPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 61 | SctResultPEOLastActionId | LAST_ACTION_ID | — | — |
| 62 | SctResultPEOLastActionType | LAST_ACTION_TYPE | — | — |
| 63 | SctResultPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 64 | SctResultPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 65 | SctResultPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 66 | SctResultPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 67 | SctResultPEORequestId | REQUEST_ID | — | — |
| 68 | SctResultPEOResultGradepoints | RESULT_GRADEPOINTS | — | ✅ |
| 69 | SctResultPEOResultNumericValue | RESULT_NUMERIC_VALUE | — | ✅ |
| 70 | SctResultPEOResultOutcomeCode | RESULT_OUTCOME_CODE | — | ✅ |
| 71 | SctResultPEOResultSetId | RESULT_SET_ID | — | ✅ |
| 72 | SctResultPEOResultStatus | RESULT_STATUS | — | ✅ |
| 73 | SctResultPEOResultTextValue | RESULT_TEXT_VALUE | — | ✅ |
| 74 | SctResultPEOResultTypeId | RESULT_TYPE_ID | — | ✅ |
| 75 | SctResultPEOSctItemId | SCT_ITEM_ID | — | ✅ |
| 76 | SctResultPEOSctResultId | SCT_RESULT_ID | 🔑 | ✅ |
| 77 | SctResultPEOShowStudentFlag | SHOW_STUDENT_FLAG | — | ✅ |

### [[her_sct_item|HER_SCT_ITEM]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SctItemPEOAcademicLevelId | ACADEMIC_LEVEL_ID | — | — |
| 2 | SctItemPEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | SctItemPEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | SctItemPEOAttribute11 | ATTRIBUTE11 | — | — |
| 5 | SctItemPEOAttribute12 | ATTRIBUTE12 | — | — |
| 6 | SctItemPEOAttribute13 | ATTRIBUTE13 | — | — |
| 7 | SctItemPEOAttribute14 | ATTRIBUTE14 | — | — |
| 8 | SctItemPEOAttribute15 | ATTRIBUTE15 | — | — |
| 9 | SctItemPEOAttribute16 | ATTRIBUTE16 | — | — |
| 10 | SctItemPEOAttribute17 | ATTRIBUTE17 | — | — |
| 11 | SctItemPEOAttribute18 | ATTRIBUTE18 | — | — |
| 12 | SctItemPEOAttribute19 | ATTRIBUTE19 | — | — |
| 13 | SctItemPEOAttribute2 | ATTRIBUTE2 | — | — |
| 14 | SctItemPEOAttribute20 | ATTRIBUTE20 | — | — |
| 15 | SctItemPEOAttribute3 | ATTRIBUTE3 | — | — |
| 16 | SctItemPEOAttribute4 | ATTRIBUTE4 | — | — |
| 17 | SctItemPEOAttribute5 | ATTRIBUTE5 | — | — |
| 18 | SctItemPEOAttribute6 | ATTRIBUTE6 | — | — |
| 19 | SctItemPEOAttribute7 | ATTRIBUTE7 | — | — |
| 20 | SctItemPEOAttribute8 | ATTRIBUTE8 | — | — |
| 21 | SctItemPEOAttribute9 | ATTRIBUTE9 | — | — |
| 22 | SctItemPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 23 | SctItemPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | SctItemPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 25 | SctItemPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 26 | SctItemPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 27 | SctItemPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 28 | SctItemPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 29 | SctItemPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 30 | SctItemPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 31 | SctItemPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 32 | SctItemPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 33 | SctItemPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 34 | SctItemPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 35 | SctItemPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 36 | SctItemPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 37 | SctItemPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 38 | SctItemPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 39 | SctItemPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 40 | SctItemPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 41 | SctItemPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 42 | SctItemPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 43 | SctItemPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 44 | SctItemPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 45 | SctItemPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 46 | SctItemPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 47 | SctItemPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 48 | SctItemPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 49 | SctItemPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 50 | SctItemPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 51 | SctItemPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 52 | SctItemPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 53 | SctItemPEOCampusId | CAMPUS_ID | — | — |
| 54 | SctItemPEOCreatedBy | CREATED_BY | — | — |
| 55 | SctItemPEOCreationDate | CREATION_DATE | — | — |
| 56 | SctItemPEOCurriculumId | CURRICULUM_ID | — | — |
| 57 | SctItemPEOCurriculumTypeId | CURRICULUM_TYPE_ID | — | — |
| 58 | SctItemPEOInstitutionId | INSTITUTION_ID | — | — |
| 59 | SctItemPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 60 | SctItemPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 61 | SctItemPEOLastActionId | LAST_ACTION_ID | — | — |
| 62 | SctItemPEOLastActionReasonId | LAST_ACTION_REASON_ID | — | — |
| 63 | SctItemPEOLastActionType | LAST_ACTION_TYPE | — | — |
| 64 | SctItemPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 65 | SctItemPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 66 | SctItemPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 67 | SctItemPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 68 | SctItemPEORecordStatus | RECORD_STATUS | — | — |
| 69 | SctItemPEORequestId | REQUEST_ID | — | — |
| 70 | SctItemPEOSctItemId | SCT_ITEM_ID | — | — |
| 71 | SctItemPEOStudentPartyId | STUDENT_PARTY_ID | — | — |

### [[her_sct_section|HER_SCT_SECTION]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SctSectionPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | SctSectionPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | SctSectionPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | SctSectionPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | SctSectionPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | SctSectionPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | SctSectionPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | SctSectionPEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | SctSectionPEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | SctSectionPEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | SctSectionPEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | SctSectionPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | SctSectionPEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | SctSectionPEOAttribute3 | ATTRIBUTE3 | — | — |
| 15 | SctSectionPEOAttribute4 | ATTRIBUTE4 | — | — |
| 16 | SctSectionPEOAttribute5 | ATTRIBUTE5 | — | — |
| 17 | SctSectionPEOAttribute6 | ATTRIBUTE6 | — | — |
| 18 | SctSectionPEOAttribute7 | ATTRIBUTE7 | — | — |
| 19 | SctSectionPEOAttribute8 | ATTRIBUTE8 | — | — |
| 20 | SctSectionPEOAttribute9 | ATTRIBUTE9 | — | — |
| 21 | SctSectionPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | SctSectionPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | SctSectionPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 24 | SctSectionPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | SctSectionPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | SctSectionPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | SctSectionPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | SctSectionPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 29 | SctSectionPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 30 | SctSectionPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 31 | SctSectionPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 32 | SctSectionPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 33 | SctSectionPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 34 | SctSectionPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 35 | SctSectionPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 36 | SctSectionPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 37 | SctSectionPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 38 | SctSectionPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 39 | SctSectionPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 40 | SctSectionPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 41 | SctSectionPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 42 | SctSectionPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 43 | SctSectionPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 44 | SctSectionPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 45 | SctSectionPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 46 | SctSectionPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 47 | SctSectionPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 48 | SctSectionPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 49 | SctSectionPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 50 | SctSectionPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 51 | SctSectionPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 52 | SctSectionPEOBillingUnits | BILLING_UNITS | — | — |
| 53 | SctSectionPEOClassEndDate | CLASS_END_DATE | — | — |
| 54 | SctSectionPEOClassStartDate | CLASS_START_DATE | — | — |
| 55 | SctSectionPEOCreatedBy | CREATED_BY | — | — |
| 56 | SctSectionPEOCreationDate | CREATION_DATE | — | — |
| 57 | SctSectionPEOCreditOptionFlag | CREDIT_OPTION_FLAG | — | — |
| 58 | SctSectionPEODropDate | DROP_DATE | — | — |
| 59 | SctSectionPEOEnrolledCredits | ENROLLED_CREDITS | — | ✅ |
| 60 | SctSectionPEOEnrollmentDate | ENROLLMENT_DATE | — | — |
| 61 | SctSectionPEOEnrollmentStatus | ENROLLMENT_STATUS | — | — |
| 62 | SctSectionPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 63 | SctSectionPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 64 | SctSectionPEOLastAttendanceDate | LAST_ATTENDANCE_DATE | — | — |
| 65 | SctSectionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 66 | SctSectionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 67 | SctSectionPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 68 | SctSectionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 69 | SctSectionPEOOwningCurriculumId | OWNING_CURRICULUM_ID | — | — |
| 70 | SctSectionPEORequestId | REQUEST_ID | — | — |
| 71 | SctSectionPEORequisiteStatusCode | REQUISITE_STATUS_CODE | — | — |
| 72 | SctSectionPEOResultSetId | RESULT_SET_ID | — | — |
| 73 | SctSectionPEOSctItemId | SCT_ITEM_ID | — | — |
| 74 | SctSectionPEOSelfPacedFlag | SELF_PACED_FLAG | — | — |
| 75 | SctSectionPEOStudentAttendedFlag | STUDENT_ATTENDED_FLAG | — | — |
| 76 | SctSectionPEOWaitlistPosition | WAITLIST_POSITION | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
