---
id: DOC-OTHER-PVO-HNSIncidentEventPVO
doc_type: system-doc
title: "HNSIncidentEventPVO — PVO Cross-Module"
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
  - HNSIncidentEventPVO
  - hnsincidenteventpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HNSIncidentEventPVO

## 📌 Visão Geral

View Object para extração BICC de dados de HNSIncident Event. Acessa as tabelas: HNS_INCIDENTS_DETAIL, HNS_INCIDENTS_SUMMARY.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HealthandSafetyAM.HNSIncidentEventPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 138 | 2 | 3 | 92 | 67% |

---

## 🔗 Tabelas Relacionadas

- [[hns_incidents_detail|HNS_INCIDENTS_DETAIL]] — 29 atributos (2 PKs, 27 BICC)
- [[hns_incidents_summary|HNS_INCIDENTS_SUMMARY]] — 109 atributos (1 PKs, 65 BICC)

---

## ⚙️ Atributos

### [[hns_incidents_detail|HNS_INCIDENTS_DETAIL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HNSIncidentEventDetailsPEOActionRqrdFlag | ACTION_REQUIRED_FLAG | — | ✅ |
| 2 | HNSIncidentEventDetailsPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 3 | HNSIncidentEventDetailsPEOCompletedFlag | COMPLETED_FLAG | — | ✅ |
| 4 | HNSIncidentEventDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | HNSIncidentEventDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | HNSIncidentEventDetailsPEODateDisclsd | DATE_DISCLOSED | — | ✅ |
| 7 | HNSIncidentEventDetailsPEODeletedFlag | DELETED_FLAG | — | ✅ |
| 8 | HNSIncidentEventDetailsPEOEmpAsnId | EMPLOYEE_ASSIGN_ID | — | — |
| 9 | HNSIncidentEventDetailsPEOEmployeeId | EMPLOYEE_ID | — | ✅ |
| 10 | HNSIncidentEventDetailsPEOEvntCreationDt | EVENT_CREATION_DATE | — | ✅ |
| 11 | HNSIncidentEventDetailsPEOIncEvOwnAsnId | INC_EVENT_OWNER_ASSIGN_ID | — | — |
| 12 | HNSIncidentEventDetailsPEOInciDetailDescr | INCI_DETAIL_DESCR | — | ✅ |
| 13 | HNSIncidentEventDetailsPEOInciEventStatusCode | INCI_EVENT_STATUS_CODE | — | ✅ |
| 14 | HNSIncidentEventDetailsPEOIncidentDetailId | INCIDENT_DETAIL_ID | 🔑 | ✅ |
| 15 | HNSIncidentEventDetailsPEOIncidentEventCode | INCIDENT_EVENT_CODE | — | ✅ |
| 16 | HNSIncidentEventDetailsPEOIncidentEventDate | INCIDENT_EVENT_DATE | — | ✅ |
| 17 | HNSIncidentEventDetailsPEOIncidentEventNo | INCIDENT_EVENT_NO | — | ✅ |
| 18 | HNSIncidentEventDetailsPEOIncidentEventOwnerId | INCIDENT_EVENT_OWNER_ID | — | ✅ |
| 19 | HNSIncidentEventDetailsPEOIncidentEventSummary | INCIDENT_EVENT_SUMMARY | — | ✅ |
| 20 | HNSIncidentEventDetailsPEOIncidentId | INCIDENT_ID | 🔑 | ✅ |
| 21 | HNSIncidentEventDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | HNSIncidentEventDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 23 | HNSIncidentEventDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | HNSIncidentEventDetailsPEOLessonsLearned | LESSONS_LEARNED | — | ✅ |
| 25 | HNSIncidentEventDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 26 | HNSIncidentEventDetailsPEOResultCode | RESULT_CODE | — | ✅ |
| 27 | HNSIncidentEventDetailsPEOSeverityLevelCode | SEVERITY_LEVEL_CODE | — | ✅ |
| 28 | HNSIncidentEventDetailsPEOTargetCompletionDate | TARGET_COMPLETION_DATE | — | ✅ |
| 29 | HNSIncidentEventDetailsPEOThirdPartyDetails | THIRD_PARTY_DETAILS | — | ✅ |

### [[hns_incidents_summary|HNS_INCIDENTS_SUMMARY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HNSIncidentsPEOActionReqrdFlag | ACTION_REQUIRED_FLAG | — | ✅ |
| 2 | HNSIncidentsPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 3 | HNSIncidentsPEOAttrCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | HNSIncidentsPEOAttrNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 5 | HNSIncidentsPEOAttrNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 6 | HNSIncidentsPEOAttrNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 7 | HNSIncidentsPEOAttrNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 8 | HNSIncidentsPEOAttrNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 9 | HNSIncidentsPEOAttrNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 10 | HNSIncidentsPEOAttrNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 11 | HNSIncidentsPEOAttrNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 12 | HNSIncidentsPEOAttrNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 13 | HNSIncidentsPEOAttrNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 14 | HNSIncidentsPEOAttrTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 15 | HNSIncidentsPEOAttrTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 16 | HNSIncidentsPEOAttrTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 17 | HNSIncidentsPEOAttrTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 18 | HNSIncidentsPEOAttrTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 19 | HNSIncidentsPEOAttrTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 20 | HNSIncidentsPEOAttrTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 21 | HNSIncidentsPEOAttrTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 22 | HNSIncidentsPEOAttrTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 23 | HNSIncidentsPEOAttrTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 24 | HNSIncidentsPEOAttribute1 | ATTRIBUTE1 | — | — |
| 25 | HNSIncidentsPEOAttribute10 | ATTRIBUTE10 | — | — |
| 26 | HNSIncidentsPEOAttribute11 | ATTRIBUTE11 | — | — |
| 27 | HNSIncidentsPEOAttribute12 | ATTRIBUTE12 | — | — |
| 28 | HNSIncidentsPEOAttribute13 | ATTRIBUTE13 | — | — |
| 29 | HNSIncidentsPEOAttribute14 | ATTRIBUTE14 | — | — |
| 30 | HNSIncidentsPEOAttribute15 | ATTRIBUTE15 | — | — |
| 31 | HNSIncidentsPEOAttribute16 | ATTRIBUTE16 | — | — |
| 32 | HNSIncidentsPEOAttribute17 | ATTRIBUTE17 | — | — |
| 33 | HNSIncidentsPEOAttribute18 | ATTRIBUTE18 | — | — |
| 34 | HNSIncidentsPEOAttribute19 | ATTRIBUTE19 | — | — |
| 35 | HNSIncidentsPEOAttribute2 | ATTRIBUTE2 | — | — |
| 36 | HNSIncidentsPEOAttribute20 | ATTRIBUTE20 | — | — |
| 37 | HNSIncidentsPEOAttribute3 | ATTRIBUTE3 | — | — |
| 38 | HNSIncidentsPEOAttribute4 | ATTRIBUTE4 | — | — |
| 39 | HNSIncidentsPEOAttribute5 | ATTRIBUTE5 | — | — |
| 40 | HNSIncidentsPEOAttribute6 | ATTRIBUTE6 | — | — |
| 41 | HNSIncidentsPEOAttribute7 | ATTRIBUTE7 | — | — |
| 42 | HNSIncidentsPEOAttribute8 | ATTRIBUTE8 | — | — |
| 43 | HNSIncidentsPEOAttribute9 | ATTRIBUTE9 | — | — |
| 44 | HNSIncidentsPEOBizConPlnAcEmid | BIZ_CONT_PLAN_ACT_BY_EMPID | — | ✅ |
| 45 | HNSIncidentsPEOBizConPlnActdFl | BIZ_CONT_PLAN_ACTIVATED_FLAG | — | ✅ |
| 46 | HNSIncidentsPEOBizContPlnActAt | BIZ_CONT_PLAN_ACTIVATED_AT | — | ✅ |
| 47 | HNSIncidentsPEOCompletedFlag | COMPLETED_FLAG | — | ✅ |
| 48 | HNSIncidentsPEOConfidentialFlag | CONFIDENTIAL_FLAG | — | ✅ |
| 49 | HNSIncidentsPEOCreatedBy | CREATED_BY | — | ✅ |
| 50 | HNSIncidentsPEOCreationDate | CREATION_DATE | — | ✅ |
| 51 | HNSIncidentsPEODeletedFlag | DELETED_FLAG | — | ✅ |
| 52 | HNSIncidentsPEOEmergAcPlnAcFlg | EMERG_ACTION_PLAN_ACT_FLAG | — | ✅ |
| 53 | HNSIncidentsPEOEmergActPlanActvtdAt | EMERG_ACTION_PLAN_ACTIVATED_AT | — | ✅ |
| 54 | HNSIncidentsPEOEmergencyFlag | EMERGENCY_FLAG | — | ✅ |
| 55 | HNSIncidentsPEOEmployeeId | EMPLOYEE_ID | — | ✅ |
| 56 | HNSIncidentsPEOEmrAcPlnAcByEmid | EMERG_ACTION_PLAN_ACT_BY_EMPID | — | ✅ |
| 57 | HNSIncidentsPEOEvacLengthOfTim | EVACUATION_LENGTH_OF_TIME | — | ✅ |
| 58 | HNSIncidentsPEOEvacOrderedAt | EVACUATION_ORDERED_AT | — | ✅ |
| 59 | HNSIncidentsPEOEvacOrdrByEmpId | EVACUATION_ORDERED_BY_EMP_ID | — | ✅ |
| 60 | HNSIncidentsPEOEvacTypeCode | EVACUATION_TYPE_CODE | — | ✅ |
| 61 | HNSIncidentsPEOEvacuationFlag | EVACUATION_FLAG | — | ✅ |
| 62 | HNSIncidentsPEOFacClsdByEmpId | FACILITY_CLOSED_BY_EMP_ID | — | ✅ |
| 63 | HNSIncidentsPEOFacClsdFlag | FACILITY_CLOSED_FLAG | — | ✅ |
| 64 | HNSIncidentsPEOFacClsdLngOfTim | FACILITY_CLOSED_LENGTH_OF_TIME | — | ✅ |
| 65 | HNSIncidentsPEOFacilityClsdAt | FACILITY_CLOSED_AT | — | ✅ |
| 66 | HNSIncidentsPEOIncOwnAsnId | INCIDENT_OWNER_ASSIGN_ID | — | — |
| 67 | HNSIncidentsPEOIncRprtdDt | INCIDENT_REPORTED_DATE | — | ✅ |
| 68 | HNSIncidentsPEOIncidentApproverEmailFlag | INCIDENT_APPROVER_EMAIL_FLAG | — | ✅ |
| 69 | HNSIncidentsPEOIncidentCreateDate | INCIDENT_CREATE_DATE | — | ✅ |
| 70 | HNSIncidentsPEOIncidentDate | INCIDENT_DATE | — | ✅ |
| 71 | HNSIncidentsPEOIncidentDescription | INCIDENT_DESCRIPTION | — | ✅ |
| 72 | HNSIncidentsPEOIncidentId | INCIDENT_ID | 🔑 | ✅ |
| 73 | HNSIncidentsPEOIncidentImmeActDescr | INCIDENT_IMME_ACT_DESCR | — | ✅ |
| 74 | HNSIncidentsPEOIncidentNo | INCIDENT_NO | — | ✅ |
| 75 | HNSIncidentsPEOIncidentOwnerId | INCIDENT_OWNER_ID | — | ✅ |
| 76 | HNSIncidentsPEOIncidentReviewerEmailFlag | INCIDENT_REVIEWER_EMAIL_FLAG | — | ✅ |
| 77 | HNSIncidentsPEOIncidentSrcCode | INCIDENT_SOURCE_CODE | — | ✅ |
| 78 | HNSIncidentsPEOIncidentStatusCode | INCIDENT_STATUS_CODE | — | ✅ |
| 79 | HNSIncidentsPEOIncidentSummary | INCIDENT_SUMMARY | — | ✅ |
| 80 | HNSIncidentsPEOIncidentTypCode | INCIDENT_TYPE_CODE | — | ✅ |
| 81 | HNSIncidentsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 82 | HNSIncidentsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 83 | HNSIncidentsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 84 | HNSIncidentsPEOLessonsLearned | LESSONS_LEARNED | — | ✅ |
| 85 | HNSIncidentsPEOLocationId | LOCATION_ID | — | ✅ |
| 86 | HNSIncidentsPEOLocationTypeCode | LOCATION_TYPE_CODE | — | ✅ |
| 87 | HNSIncidentsPEONtfdPerAsnId | NOTIFIED_PER_ASSIGN_ID | — | — |
| 88 | HNSIncidentsPEONtfdPerId | NOTIFIED_PERSON_ID | — | ✅ |
| 89 | HNSIncidentsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 90 | HNSIncidentsPEOOffsiteLocTypeCode | OFFSITE_LOC_TYPE_CODE | — | ✅ |
| 91 | HNSIncidentsPEORadius | RADIUS | — | ✅ |
| 92 | HNSIncidentsPEORadiusUnitCd | RADIUS_UNIT_CD | — | ✅ |
| 93 | HNSIncidentsPEOReporterTypeCode | REPORTER_TYPE_CODE | — | ✅ |
| 94 | HNSIncidentsPEOReptrAddrLine1 | REPTR_ADDR_LINE1 | — | ✅ |
| 95 | HNSIncidentsPEOReptrAddrLine2 | REPTR_ADDR_LINE2 | — | ✅ |
| 96 | HNSIncidentsPEOReptrAreaCode | REPTR_AREA_CODE | — | ✅ |
| 97 | HNSIncidentsPEOReptrCity | REPTR_CITY | — | ✅ |
| 98 | HNSIncidentsPEOReptrCountry | REPTR_COUNTRY | — | ✅ |
| 99 | HNSIncidentsPEOReptrCountryCodeNum | REPTR_COUNTRY_CODE_NUM | — | ✅ |
| 100 | HNSIncidentsPEOReptrEmail | REPTR_EMAIL | — | ✅ |
| 101 | HNSIncidentsPEOReptrName | REPTR_NAME | — | ✅ |
| 102 | HNSIncidentsPEOReptrNonempTypeCode | REPTR_NONEMP_TYPE_CODE | — | ✅ |
| 103 | HNSIncidentsPEOReptrPhoneNo | REPTR_PHONE_NO | — | ✅ |
| 104 | HNSIncidentsPEOReptrSpecificLocation | REPTR_SPECIFIC_LOCATION | — | ✅ |
| 105 | HNSIncidentsPEOReptrState | REPTR_STATE | — | ✅ |
| 106 | HNSIncidentsPEOReptrZipCode | REPTR_ZIP_CODE | — | ✅ |
| 107 | HNSIncidentsPEORptrAsntId | REPORTER_ASSIGNMENT_ID | — | — |
| 108 | HNSIncidentsPEOSeverityLevelCode | SEVERITY_LEVEL_CODE | — | ✅ |
| 109 | HNSIncidentsPEOTargetCompletionDate | TARGET_COMPLETION_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
