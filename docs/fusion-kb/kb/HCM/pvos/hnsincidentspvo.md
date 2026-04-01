---
id: DOC-HCM-PVO-HNSIncidentsPVO
doc_type: system-doc
title: "HNSIncidentsPVO — PVO Human Capital Management"
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
  - HNSIncidentsPVO
  - hnsincidentspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HNSIncidentsPVO

## 📌 Visão Geral

Disponibiliza o sumário de incidentes de saúde e segurança com status, ações requeridas e datas. Fundamental para gestão e KPIs de SST.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HealthandSafetyAM.HNSIncidentsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 104 | 1 | 1 | 63 | 61% |

---

## 🔗 Tabelas Relacionadas

- [[hns_incidents_summary|HNS_INCIDENTS_SUMMARY]] — 104 atributos (1 PKs, 63 BICC)

---

## ⚙️ Atributos

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
| 66 | HNSIncidentsPEOIncidentApproverEmailFlag | INCIDENT_APPROVER_EMAIL_FLAG | — | ✅ |
| 67 | HNSIncidentsPEOIncidentCreateDate | INCIDENT_CREATE_DATE | — | ✅ |
| 68 | HNSIncidentsPEOIncidentDate | INCIDENT_DATE | — | ✅ |
| 69 | HNSIncidentsPEOIncidentDescription | INCIDENT_DESCRIPTION | — | ✅ |
| 70 | HNSIncidentsPEOIncidentId | INCIDENT_ID | 🔑 | ✅ |
| 71 | HNSIncidentsPEOIncidentImmeActDescr | INCIDENT_IMME_ACT_DESCR | — | ✅ |
| 72 | HNSIncidentsPEOIncidentNo | INCIDENT_NO | — | ✅ |
| 73 | HNSIncidentsPEOIncidentOwnerId | INCIDENT_OWNER_ID | — | ✅ |
| 74 | HNSIncidentsPEOIncidentReviewerEmailFlag | INCIDENT_REVIEWER_EMAIL_FLAG | — | ✅ |
| 75 | HNSIncidentsPEOIncidentSrcCode | INCIDENT_SOURCE_CODE | — | ✅ |
| 76 | HNSIncidentsPEOIncidentStatusCode | INCIDENT_STATUS_CODE | — | ✅ |
| 77 | HNSIncidentsPEOIncidentSummary | INCIDENT_SUMMARY | — | ✅ |
| 78 | HNSIncidentsPEOIncidentTypCode | INCIDENT_TYPE_CODE | — | ✅ |
| 79 | HNSIncidentsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 80 | HNSIncidentsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 81 | HNSIncidentsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 82 | HNSIncidentsPEOLessonsLearned | LESSONS_LEARNED | — | ✅ |
| 83 | HNSIncidentsPEOLocationId | LOCATION_ID | — | ✅ |
| 84 | HNSIncidentsPEOLocationTypeCode | LOCATION_TYPE_CODE | — | ✅ |
| 85 | HNSIncidentsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 86 | HNSIncidentsPEOOffsiteLocTypeCode | OFFSITE_LOC_TYPE_CODE | — | ✅ |
| 87 | HNSIncidentsPEORadius | RADIUS | — | ✅ |
| 88 | HNSIncidentsPEORadiusUnitCd | RADIUS_UNIT_CD | — | ✅ |
| 89 | HNSIncidentsPEOReporterTypeCode | REPORTER_TYPE_CODE | — | ✅ |
| 90 | HNSIncidentsPEOReptrAddrLine1 | REPTR_ADDR_LINE1 | — | ✅ |
| 91 | HNSIncidentsPEOReptrAddrLine2 | REPTR_ADDR_LINE2 | — | ✅ |
| 92 | HNSIncidentsPEOReptrAreaCode | REPTR_AREA_CODE | — | ✅ |
| 93 | HNSIncidentsPEOReptrCity | REPTR_CITY | — | ✅ |
| 94 | HNSIncidentsPEOReptrCountry | REPTR_COUNTRY | — | ✅ |
| 95 | HNSIncidentsPEOReptrCountryCodeNum | REPTR_COUNTRY_CODE_NUM | — | ✅ |
| 96 | HNSIncidentsPEOReptrEmail | REPTR_EMAIL | — | ✅ |
| 97 | HNSIncidentsPEOReptrName | REPTR_NAME | — | ✅ |
| 98 | HNSIncidentsPEOReptrNonempTypeCode | REPTR_NONEMP_TYPE_CODE | — | ✅ |
| 99 | HNSIncidentsPEOReptrPhoneNo | REPTR_PHONE_NO | — | ✅ |
| 100 | HNSIncidentsPEOReptrSpecificLocation | REPTR_SPECIFIC_LOCATION | — | ✅ |
| 101 | HNSIncidentsPEOReptrState | REPTR_STATE | — | ✅ |
| 102 | HNSIncidentsPEOReptrZipCode | REPTR_ZIP_CODE | — | ✅ |
| 103 | HNSIncidentsPEOSeverityLevelCode | SEVERITY_LEVEL_CODE | — | ✅ |
| 104 | HNSIncidentsPEOTargetCompletionDate | TARGET_COMPLETION_DATE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
