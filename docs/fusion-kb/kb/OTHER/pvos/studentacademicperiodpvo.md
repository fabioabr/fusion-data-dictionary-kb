---
id: DOC-OTHER-PVO-StudentAcademicPeriodPVO
doc_type: system-doc
title: "StudentAcademicPeriodPVO — PVO Cross-Module"
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
  - StudentAcademicPeriodPVO
  - studentacademicperiodpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# StudentAcademicPeriodPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Student Academic Period. Acessa as tabelas: HER_SCT_ITEM, HES_STUDENT_ACADEMIC_PERIOD, HEY_ESTABLISHMENT_V (+1).

**Caminho:** `FscmTopModelAM.HedHesTuitionSetupAM.StudentAcademicPeriodPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 258 | 4 | 1 | 12 | 5% |

---

## 🔗 Tabelas Relacionadas

- [[her_sct_item|HER_SCT_ITEM]] — 71 atributos
- [[hes_student_academic_period|HES_STUDENT_ACADEMIC_PERIOD]] — 68 atributos (1 PKs, 12 BICC)
- [[hey_establishment_v|HEY_ESTABLISHMENT_V]] — 5 atributos
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 114 atributos

---

## ⚙️ Atributos

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
| 64 | SctItemPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 65 | SctItemPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 66 | SctItemPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 67 | SctItemPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 68 | SctItemPEORecordStatus | RECORD_STATUS | — | — |
| 69 | SctItemPEORequestId | REQUEST_ID | — | — |
| 70 | SctItemPEOSctItemId | SCT_ITEM_ID | — | — |
| 71 | SctItemPEOStudentPartyId | STUDENT_PARTY_ID | — | — |

### [[hes_student_academic_period|HES_STUDENT_ACADEMIC_PERIOD]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StudentAcadPeriodPEOAcademicGroupId | ACADEMIC_GROUP_ID | — | ✅ |
| 2 | StudentAcadPeriodPEOAcademicLevelId | ACADEMIC_LEVEL_ID | — | ✅ |
| 3 | StudentAcadPeriodPEOAcademicProgramId | ACADEMIC_PROGRAM_ID | — | — |
| 4 | StudentAcadPeriodPEOAcademicReportingPeriodId | ACADEMIC_REPORTING_PERIOD_ID | — | ✅ |
| 5 | StudentAcadPeriodPEOAssignedFeeGroupId | ASSIGNED_FEE_GROUP_ID | — | ✅ |
| 6 | StudentAcadPeriodPEOAttribute1 | ATTRIBUTE1 | — | — |
| 7 | StudentAcadPeriodPEOAttribute10 | ATTRIBUTE10 | — | — |
| 8 | StudentAcadPeriodPEOAttribute11 | ATTRIBUTE11 | — | — |
| 9 | StudentAcadPeriodPEOAttribute12 | ATTRIBUTE12 | — | — |
| 10 | StudentAcadPeriodPEOAttribute13 | ATTRIBUTE13 | — | — |
| 11 | StudentAcadPeriodPEOAttribute14 | ATTRIBUTE14 | — | — |
| 12 | StudentAcadPeriodPEOAttribute15 | ATTRIBUTE15 | — | — |
| 13 | StudentAcadPeriodPEOAttribute16 | ATTRIBUTE16 | — | — |
| 14 | StudentAcadPeriodPEOAttribute17 | ATTRIBUTE17 | — | — |
| 15 | StudentAcadPeriodPEOAttribute18 | ATTRIBUTE18 | — | — |
| 16 | StudentAcadPeriodPEOAttribute19 | ATTRIBUTE19 | — | — |
| 17 | StudentAcadPeriodPEOAttribute2 | ATTRIBUTE2 | — | — |
| 18 | StudentAcadPeriodPEOAttribute20 | ATTRIBUTE20 | — | — |
| 19 | StudentAcadPeriodPEOAttribute3 | ATTRIBUTE3 | — | — |
| 20 | StudentAcadPeriodPEOAttribute4 | ATTRIBUTE4 | — | — |
| 21 | StudentAcadPeriodPEOAttribute5 | ATTRIBUTE5 | — | — |
| 22 | StudentAcadPeriodPEOAttribute6 | ATTRIBUTE6 | — | — |
| 23 | StudentAcadPeriodPEOAttribute7 | ATTRIBUTE7 | — | — |
| 24 | StudentAcadPeriodPEOAttribute8 | ATTRIBUTE8 | — | — |
| 25 | StudentAcadPeriodPEOAttribute9 | ATTRIBUTE9 | — | — |
| 26 | StudentAcadPeriodPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 27 | StudentAcadPeriodPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 28 | StudentAcadPeriodPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 29 | StudentAcadPeriodPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 30 | StudentAcadPeriodPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 31 | StudentAcadPeriodPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 32 | StudentAcadPeriodPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 33 | StudentAcadPeriodPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 34 | StudentAcadPeriodPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 35 | StudentAcadPeriodPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 36 | StudentAcadPeriodPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 37 | StudentAcadPeriodPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 38 | StudentAcadPeriodPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 39 | StudentAcadPeriodPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 40 | StudentAcadPeriodPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 41 | StudentAcadPeriodPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 42 | StudentAcadPeriodPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 43 | StudentAcadPeriodPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 44 | StudentAcadPeriodPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 45 | StudentAcadPeriodPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 46 | StudentAcadPeriodPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 47 | StudentAcadPeriodPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 48 | StudentAcadPeriodPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 49 | StudentAcadPeriodPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 50 | StudentAcadPeriodPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 51 | StudentAcadPeriodPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 52 | StudentAcadPeriodPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 53 | StudentAcadPeriodPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 54 | StudentAcadPeriodPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 55 | StudentAcadPeriodPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 56 | StudentAcadPeriodPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 57 | StudentAcadPeriodPEOCreatedBy | CREATED_BY | — | — |
| 58 | StudentAcadPeriodPEOCreationDate | CREATION_DATE | — | — |
| 59 | StudentAcadPeriodPEOFeeCalcRequiredFlag | FEE_CALC_REQUIRED_FLAG | — | ✅ |
| 60 | StudentAcadPeriodPEOHoldCalculationFlag | HOLD_CALCULATION_FLAG | — | ✅ |
| 61 | StudentAcadPeriodPEOInstitutionId | INSTITUTION_ID | — | ✅ |
| 62 | StudentAcadPeriodPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 63 | StudentAcadPeriodPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 64 | StudentAcadPeriodPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 65 | StudentAcadPeriodPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 66 | StudentAcadPeriodPEOOverrideFeeGroupId | OVERRIDE_FEE_GROUP_ID | — | ✅ |
| 67 | StudentAcadPeriodPEOStudentAcademicPeriodId | STUDENT_ACADEMIC_PERIOD_ID | 🔑 | ✅ |
| 68 | StudentAcadPeriodPEOStudentPartyId | STUDENT_PARTY_ID | — | ✅ |

### [[hey_establishment_v|HEY_ESTABLISHMENT_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EstablishmentPEOAffiliationType | AFFILIATION_TYPE_CODE | — | — |
| 2 | EstablishmentPEOConstituentId | CONSTITUENT_IDENTIFIER | — | — |
| 3 | EstablishmentPEOEndDate | END_DATE | — | — |
| 4 | EstablishmentPEOPartyId | PARTY_ID | — | — |
| 5 | EstablishmentPEOStartDate | START_DATE | — | — |

### [[hz_cust_accounts|HZ_CUST_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustAccountPEOAccountEstablishedDate | ACCOUNT_ESTABLISHED_DATE | — | — |
| 2 | CustAccountPEOAccountName | ACCOUNT_NAME | — | — |
| 3 | CustAccountPEOAccountNumber | ACCOUNT_NUMBER | — | — |
| 4 | CustAccountPEOAccountTerminationDate | ACCOUNT_TERMINATION_DATE | — | — |
| 5 | CustAccountPEOArrivalsetsIncludeLinesFlag | ARRIVALSETS_INCLUDE_LINES_FLAG | — | — |
| 6 | CustAccountPEOAttribute1 | ATTRIBUTE1 | — | — |
| 7 | CustAccountPEOAttribute10 | ATTRIBUTE10 | — | — |
| 8 | CustAccountPEOAttribute11 | ATTRIBUTE11 | — | — |
| 9 | CustAccountPEOAttribute12 | ATTRIBUTE12 | — | — |
| 10 | CustAccountPEOAttribute13 | ATTRIBUTE13 | — | — |
| 11 | CustAccountPEOAttribute14 | ATTRIBUTE14 | — | — |
| 12 | CustAccountPEOAttribute15 | ATTRIBUTE15 | — | — |
| 13 | CustAccountPEOAttribute16 | ATTRIBUTE16 | — | — |
| 14 | CustAccountPEOAttribute17 | ATTRIBUTE17 | — | — |
| 15 | CustAccountPEOAttribute18 | ATTRIBUTE18 | — | — |
| 16 | CustAccountPEOAttribute19 | ATTRIBUTE19 | — | — |
| 17 | CustAccountPEOAttribute2 | ATTRIBUTE2 | — | — |
| 18 | CustAccountPEOAttribute20 | ATTRIBUTE20 | — | — |
| 19 | CustAccountPEOAttribute21 | ATTRIBUTE21 | — | — |
| 20 | CustAccountPEOAttribute22 | ATTRIBUTE22 | — | — |
| 21 | CustAccountPEOAttribute23 | ATTRIBUTE23 | — | — |
| 22 | CustAccountPEOAttribute24 | ATTRIBUTE24 | — | — |
| 23 | CustAccountPEOAttribute25 | ATTRIBUTE25 | — | — |
| 24 | CustAccountPEOAttribute26 | ATTRIBUTE26 | — | — |
| 25 | CustAccountPEOAttribute27 | ATTRIBUTE27 | — | — |
| 26 | CustAccountPEOAttribute28 | ATTRIBUTE28 | — | — |
| 27 | CustAccountPEOAttribute29 | ATTRIBUTE29 | — | — |
| 28 | CustAccountPEOAttribute3 | ATTRIBUTE3 | — | — |
| 29 | CustAccountPEOAttribute30 | ATTRIBUTE30 | — | — |
| 30 | CustAccountPEOAttribute4 | ATTRIBUTE4 | — | — |
| 31 | CustAccountPEOAttribute5 | ATTRIBUTE5 | — | — |
| 32 | CustAccountPEOAttribute6 | ATTRIBUTE6 | — | — |
| 33 | CustAccountPEOAttribute7 | ATTRIBUTE7 | — | — |
| 34 | CustAccountPEOAttribute8 | ATTRIBUTE8 | — | — |
| 35 | CustAccountPEOAttribute9 | ATTRIBUTE9 | — | — |
| 36 | CustAccountPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 37 | CustAccountPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 38 | CustAccountPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 39 | CustAccountPEOAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 40 | CustAccountPEOAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 41 | CustAccountPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 42 | CustAccountPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 43 | CustAccountPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 44 | CustAccountPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 45 | CustAccountPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 46 | CustAccountPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 47 | CustAccountPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 48 | CustAccountPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 49 | CustAccountPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 50 | CustAccountPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 51 | CustAccountPEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 52 | CustAccountPEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 53 | CustAccountPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 54 | CustAccountPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 55 | CustAccountPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 56 | CustAccountPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 57 | CustAccountPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 58 | CustAccountPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 59 | CustAccountPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 60 | CustAccountPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 61 | CustAccountPEOAutopayFlag | AUTOPAY_FLAG | — | — |
| 62 | CustAccountPEOComments | COMMENTS | — | — |
| 63 | CustAccountPEOCoterminateDayMonth | COTERMINATE_DAY_MONTH | — | — |
| 64 | CustAccountPEOCreatedBy | CREATED_BY | — | — |
| 65 | CustAccountPEOCreatedByModule | CREATED_BY_MODULE | — | — |
| 66 | CustAccountPEOCreationDate | CREATION_DATE | — | — |
| 67 | CustAccountPEOCustAccountId | CUST_ACCOUNT_ID | — | — |
| 68 | CustAccountPEOCustomerClassCode | CUSTOMER_CLASS_CODE | — | — |
| 69 | CustAccountPEOCustomerType | CUSTOMER_TYPE | — | — |
| 70 | CustAccountPEODateTypePreference | DATE_TYPE_PREFERENCE | — | — |
| 71 | CustAccountPEODepositRefundMethod | DEPOSIT_REFUND_METHOD | — | — |
| 72 | CustAccountPEOGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 73 | CustAccountPEOGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 74 | CustAccountPEOGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 75 | CustAccountPEOGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 76 | CustAccountPEOGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 77 | CustAccountPEOGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 78 | CustAccountPEOGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 79 | CustAccountPEOGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 80 | CustAccountPEOGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 81 | CustAccountPEOGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 82 | CustAccountPEOGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 83 | CustAccountPEOGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 84 | CustAccountPEOGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 85 | CustAccountPEOGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 86 | CustAccountPEOGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 87 | CustAccountPEOGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 88 | CustAccountPEOGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 89 | CustAccountPEOGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 90 | CustAccountPEOGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 91 | CustAccountPEOGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 92 | CustAccountPEOGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 93 | CustAccountPEOGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 94 | CustAccountPEOGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 95 | CustAccountPEOGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 96 | CustAccountPEOGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 97 | CustAccountPEOGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 98 | CustAccountPEOHeldBillExpirationDate | HELD_BILL_EXPIRATION_DATE | — | — |
| 99 | CustAccountPEOHoldBillFlag | HOLD_BILL_FLAG | — | — |
| 100 | CustAccountPEOLastBatchId | LAST_BATCH_ID | — | — |
| 101 | CustAccountPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 102 | CustAccountPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 103 | CustAccountPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 104 | CustAccountPEONpaNumber | NPA_NUMBER | — | — |
| 105 | CustAccountPEOOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 106 | CustAccountPEOPartyId | PARTY_ID | — | — |
| 107 | CustAccountPEOSellingPartyId | SELLING_PARTY_ID | — | — |
| 108 | CustAccountPEOSourceCode | SOURCE_CODE | — | — |
| 109 | CustAccountPEOStatus | STATUS | — | — |
| 110 | CustAccountPEOStatusUpdateDate | STATUS_UPDATE_DATE | — | — |
| 111 | CustAccountPEOTaxCode | TAX_CODE | — | — |
| 112 | CustAccountPEOTaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | — |
| 113 | CustAccountPEOTaxRoundingRule | TAX_ROUNDING_RULE | — | — |
| 114 | CustAccountPEOUserLastUpdateDate | USER_LAST_UPDATE_DATE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
