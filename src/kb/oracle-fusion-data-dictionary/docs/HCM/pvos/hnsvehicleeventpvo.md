---
id: DOC-HCM-PVO-HNSVehicleEventPVO
doc_type: system-doc
title: "HNSVehicleEventPVO — PVO Human Capital Management"
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
  - HNSVehicleEventPVO
  - hnsvehicleeventpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HNSVehicleEventPVO

## 📌 Visão Geral

Consolida eventos de incidentes veiculares em SST, incluindo passageiros e sumário. Suporta gestão de frotas e segurança viária corporativa.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HealthandSafetyAM.HNSVehicleEventPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 393 | 4 | 3 | 110 | 28% |

---

## 🔗 Tabelas Relacionadas

- [[hns_incidents_detail|HNS_INCIDENTS_DETAIL]] — 115 atributos
- [[hns_veh_inc_event_detail|HNS_VEH_INC_EVENT_DETAIL]] — 176 atributos (1 PKs, 60 BICC)
- [[hns_veh_inc_event_passengers|HNS_VEH_INC_EVENT_PASSENGERS]] — 27 atributos (1 PKs, 26 BICC)
- [[hns_veh_inc_event_summary|HNS_VEH_INC_EVENT_SUMMARY]] — 75 atributos (1 PKs, 24 BICC)

---

## ⚙️ Atributos

### [[hns_incidents_detail|HNS_INCIDENTS_DETAIL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute3 | ATTRIBUTE3 | — | — |
| 2 | HNSIncidentEventDetailsPEOActionRequiredFlag | ACTION_REQUIRED_FLAG | — | — |
| 3 | HNSIncidentEventDetailsPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | — |
| 4 | HNSIncidentEventDetailsPEOAirQualityTypeCode | AIR_QUALITY_TYPE_CODE | — | — |
| 5 | HNSIncidentEventDetailsPEOAmountRecovered | AMOUNT_RECOVERED | — | — |
| 6 | HNSIncidentEventDetailsPEOAmountRecoveredUnitCd | AMOUNT_RECOVERED_UNIT_CD | — | — |
| 7 | HNSIncidentEventDetailsPEOAmountSpilled | AMOUNT_SPILLED | — | — |
| 8 | HNSIncidentEventDetailsPEOAmountSpilledUnitCd | AMOUNT_SPILLED_UNIT_CD | — | — |
| 9 | HNSIncidentEventDetailsPEOAttribute1 | ATTRIBUTE1 | — | — |
| 10 | HNSIncidentEventDetailsPEOAttribute10 | ATTRIBUTE10 | — | — |
| 11 | HNSIncidentEventDetailsPEOAttribute11 | ATTRIBUTE11 | — | — |
| 12 | HNSIncidentEventDetailsPEOAttribute12 | ATTRIBUTE12 | — | — |
| 13 | HNSIncidentEventDetailsPEOAttribute13 | ATTRIBUTE13 | — | — |
| 14 | HNSIncidentEventDetailsPEOAttribute14 | ATTRIBUTE14 | — | — |
| 15 | HNSIncidentEventDetailsPEOAttribute15 | ATTRIBUTE15 | — | — |
| 16 | HNSIncidentEventDetailsPEOAttribute16 | ATTRIBUTE16 | — | — |
| 17 | HNSIncidentEventDetailsPEOAttribute17 | ATTRIBUTE17 | — | — |
| 18 | HNSIncidentEventDetailsPEOAttribute18 | ATTRIBUTE18 | — | — |
| 19 | HNSIncidentEventDetailsPEOAttribute19 | ATTRIBUTE19 | — | — |
| 20 | HNSIncidentEventDetailsPEOAttribute2 | ATTRIBUTE2 | — | — |
| 21 | HNSIncidentEventDetailsPEOAttribute20 | ATTRIBUTE20 | — | — |
| 22 | HNSIncidentEventDetailsPEOAttribute21 | ATTRIBUTE21 | — | — |
| 23 | HNSIncidentEventDetailsPEOAttribute22 | ATTRIBUTE22 | — | — |
| 24 | HNSIncidentEventDetailsPEOAttribute23 | ATTRIBUTE23 | — | — |
| 25 | HNSIncidentEventDetailsPEOAttribute24 | ATTRIBUTE24 | — | — |
| 26 | HNSIncidentEventDetailsPEOAttribute25 | ATTRIBUTE25 | — | — |
| 27 | HNSIncidentEventDetailsPEOAttribute26 | ATTRIBUTE26 | — | — |
| 28 | HNSIncidentEventDetailsPEOAttribute27 | ATTRIBUTE27 | — | — |
| 29 | HNSIncidentEventDetailsPEOAttribute28 | ATTRIBUTE28 | — | — |
| 30 | HNSIncidentEventDetailsPEOAttribute29 | ATTRIBUTE29 | — | — |
| 31 | HNSIncidentEventDetailsPEOAttribute30 | ATTRIBUTE30 | — | — |
| 32 | HNSIncidentEventDetailsPEOAttribute4 | ATTRIBUTE4 | — | — |
| 33 | HNSIncidentEventDetailsPEOAttribute5 | ATTRIBUTE5 | — | — |
| 34 | HNSIncidentEventDetailsPEOAttribute6 | ATTRIBUTE6 | — | — |
| 35 | HNSIncidentEventDetailsPEOAttribute7 | ATTRIBUTE7 | — | — |
| 36 | HNSIncidentEventDetailsPEOAttribute8 | ATTRIBUTE8 | — | — |
| 37 | HNSIncidentEventDetailsPEOAttribute9 | ATTRIBUTE9 | — | — |
| 38 | HNSIncidentEventDetailsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 39 | HNSIncidentEventDetailsPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 40 | HNSIncidentEventDetailsPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 41 | HNSIncidentEventDetailsPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 42 | HNSIncidentEventDetailsPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 43 | HNSIncidentEventDetailsPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 44 | HNSIncidentEventDetailsPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 45 | HNSIncidentEventDetailsPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 46 | HNSIncidentEventDetailsPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 47 | HNSIncidentEventDetailsPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 48 | HNSIncidentEventDetailsPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 49 | HNSIncidentEventDetailsPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 50 | HNSIncidentEventDetailsPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 51 | HNSIncidentEventDetailsPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 52 | HNSIncidentEventDetailsPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 53 | HNSIncidentEventDetailsPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 54 | HNSIncidentEventDetailsPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 55 | HNSIncidentEventDetailsPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 56 | HNSIncidentEventDetailsPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 57 | HNSIncidentEventDetailsPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 58 | HNSIncidentEventDetailsPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 59 | HNSIncidentEventDetailsPEOCitationNum | CITATION_NUM | — | — |
| 60 | HNSIncidentEventDetailsPEOCleanupTeamNotified | CLEANUP_TEAM_NOTIFIED | — | — |
| 61 | HNSIncidentEventDetailsPEOCleanupTeamNotifiedAt | CLEANUP_TEAM_NOTIFIED_AT | — | — |
| 62 | HNSIncidentEventDetailsPEOCompletedFlag | COMPLETED_FLAG | — | — |
| 63 | HNSIncidentEventDetailsPEOCreatedBy | CREATED_BY | — | — |
| 64 | HNSIncidentEventDetailsPEOCreationDate | CREATION_DATE | — | — |
| 65 | HNSIncidentEventDetailsPEODateDisclosed | DATE_DISCLOSED | — | — |
| 66 | HNSIncidentEventDetailsPEODeletedFlag | DELETED_FLAG | — | — |
| 67 | HNSIncidentEventDetailsPEODeletedFlag1 | DELETED_FLAG | — | — |
| 68 | HNSIncidentEventDetailsPEOEmployeeAssignId | EMPLOYEE_ASSIGN_ID | — | — |
| 69 | HNSIncidentEventDetailsPEOEmployeeId1 | EMPLOYEE_ID | — | — |
| 70 | HNSIncidentEventDetailsPEOErgonomicAssReqCode | ERGONOMIC_ASS_REQ_CODE | — | — |
| 71 | HNSIncidentEventDetailsPEOErgonomicTypeCode | ERGONOMIC_TYPE_CODE | — | — |
| 72 | HNSIncidentEventDetailsPEOEventCreationDate | EVENT_CREATION_DATE | — | — |
| 73 | HNSIncidentEventDetailsPEOImprovementTypeCode | IMPROVEMENT_TYPE_CODE | — | — |
| 74 | HNSIncidentEventDetailsPEOIncEventOwnerAssignId | INC_EVENT_OWNER_ASSIGN_ID | — | — |
| 75 | HNSIncidentEventDetailsPEOInciDetailDescr | INCI_DETAIL_DESCR | — | — |
| 76 | HNSIncidentEventDetailsPEOInciEventStatusCode | INCI_EVENT_STATUS_CODE | — | — |
| 77 | HNSIncidentEventDetailsPEOIncidentDetailId | INCIDENT_DETAIL_ID | — | — |
| 78 | HNSIncidentEventDetailsPEOIncidentEventCode | INCIDENT_EVENT_CODE | — | — |
| 79 | HNSIncidentEventDetailsPEOIncidentEventDate | INCIDENT_EVENT_DATE | — | — |
| 80 | HNSIncidentEventDetailsPEOIncidentEventNo | INCIDENT_EVENT_NO | — | — |
| 81 | HNSIncidentEventDetailsPEOIncidentEventOwnerId | INCIDENT_EVENT_OWNER_ID | — | — |
| 82 | HNSIncidentEventDetailsPEOIncidentEventSummary | INCIDENT_EVENT_SUMMARY | — | — |
| 83 | HNSIncidentEventDetailsPEOIncidentId | INCIDENT_ID | — | — |
| 84 | HNSIncidentEventDetailsPEOIssueTypeCode | ISSUE_TYPE_CODE | — | — |
| 85 | HNSIncidentEventDetailsPEOLessonsLearned | LESSONS_LEARNED | — | — |
| 86 | HNSIncidentEventDetailsPEOLightConditionCode | LIGHT_CONDITION_CODE | — | — |
| 87 | HNSIncidentEventDetailsPEONearMissCode | NEAR_MISS_CODE | — | — |
| 88 | HNSIncidentEventDetailsPEONoticeOfViolationCd | NOTICE_OF_VIOLATION_CD | — | — |
| 89 | HNSIncidentEventDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 90 | HNSIncidentEventDetailsPEOPoliceBadgeNum | POLICE_BADGE_NUM | — | — |
| 91 | HNSIncidentEventDetailsPEOPoliceReportFlag | POLICE_REPORT_FLAG | — | — |
| 92 | HNSIncidentEventDetailsPEOPropertyDamageCode | PROPERTY_DAMAGE_CODE | — | — |
| 93 | HNSIncidentEventDetailsPEOReplnSpillKitFlag | REPLN_SPILL_KIT_FLAG | — | — |
| 94 | HNSIncidentEventDetailsPEOResultCode | RESULT_CODE | — | — |
| 95 | HNSIncidentEventDetailsPEORoadConditionCode | ROAD_CONDITION_CODE | — | — |
| 96 | HNSIncidentEventDetailsPEOSeverityLevelCode | SEVERITY_LEVEL_CODE | — | — |
| 97 | HNSIncidentEventDetailsPEOSpillPossibleCauseCode | SPILL_POSSIBLE_CAUSE_CODE | — | — |
| 98 | HNSIncidentEventDetailsPEOSpillReleaseCode | SPILL_RELEASE_CODE | — | — |
| 99 | HNSIncidentEventDetailsPEOSpillSourceCode | SPILL_SOURCE_CODE | — | — |
| 100 | HNSIncidentEventDetailsPEOSpillkitDeployedFlag | SPILLKIT_DEPLOYED_FLAG | — | — |
| 101 | HNSIncidentEventDetailsPEOTargetCompletionDate | TARGET_COMPLETION_DATE | — | — |
| 102 | HNSIncidentEventDetailsPEOThirdPartyDetails | THIRD_PARTY_DETAILS | — | — |
| 103 | HNSIncidentEventDetailsPEOTrafficConditionCode | TRAFFIC_CONDITION_CODE | — | — |
| 104 | HNSIncidentEventDetailsPEOTrafficControlsCode | TRAFFIC_CONTROLS_CODE | — | — |
| 105 | HNSIncidentEventDetailsPEOUnsafeActTypeCode | UNSAFE_ACT_TYPE_CODE | — | — |
| 106 | HNSIncidentEventDetailsPEOUnsafeConditionCode | UNSAFE_CONDITION_CODE | — | — |
| 107 | HNSIncidentEventDetailsPEOVehicleAccCategoryCode | VEHICLE_ACC_CATEGORY_CODE | — | — |
| 108 | HNSIncidentEventDetailsPEOVehicleCollisionTypeCode | VEHICLE_COLLISION_TYPE_CODE | — | — |
| 109 | HNSIncidentEventDetailsPEOVehicleSpeedLimit | VEHICLE_SPEED_LIMIT | — | — |
| 110 | HNSIncidentEventDetailsPEOVehicleSpeedUnitCd | VEHICLE_SPEED_UNIT_CD | — | — |
| 111 | HNSIncidentEventDetailsPEOVehicleStruckByCode1 | VEHICLE_STRUCK_BY_CODE | — | — |
| 112 | HNSIncidentEventDetailsPEOVehicleStruckCode | VEHICLE_STRUCK_CODE | — | — |
| 113 | HNSIncidentEventDetailsPEOWeatherConditionCode | WEATHER_CONDITION_CODE | — | — |
| 114 | HNSIncidentEventDetailsPEOWhatWasSpilledOrReleased | WHAT_WAS_SPILLED_OR_RELEASED | — | — |
| 115 | PoliceAgencyLocation | POLICE_AGENCY_LOCATION | — | — |

### [[hns_veh_inc_event_detail|HNS_VEH_INC_EVENT_DETAIL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HNSVehicleEventPEOAirbagDeplydFlag | AIRBAG_DEPLOYED_FLAG | — | ✅ |
| 2 | HNSVehicleEventPEOAlchlTestPerfFlag | ALCOHOL_TEST_PERFORM_FLAG | — | ✅ |
| 3 | HNSVehicleEventPEOAttribute1 | ATTRIBUTE1 | — | — |
| 4 | HNSVehicleEventPEOAttribute10 | ATTRIBUTE10 | — | — |
| 5 | HNSVehicleEventPEOAttribute11 | ATTRIBUTE1 | — | — |
| 6 | HNSVehicleEventPEOAttribute111 | ATTRIBUTE11 | — | — |
| 7 | HNSVehicleEventPEOAttribute12 | ATTRIBUTE12 | — | — |
| 8 | HNSVehicleEventPEOAttribute13 | ATTRIBUTE13 | — | — |
| 9 | HNSVehicleEventPEOAttribute14 | ATTRIBUTE14 | — | — |
| 10 | HNSVehicleEventPEOAttribute15 | ATTRIBUTE15 | — | — |
| 11 | HNSVehicleEventPEOAttribute16 | ATTRIBUTE16 | — | — |
| 12 | HNSVehicleEventPEOAttribute17 | ATTRIBUTE17 | — | — |
| 13 | HNSVehicleEventPEOAttribute18 | ATTRIBUTE18 | — | — |
| 14 | HNSVehicleEventPEOAttribute19 | ATTRIBUTE19 | — | — |
| 15 | HNSVehicleEventPEOAttribute2 | ATTRIBUTE2 | — | — |
| 16 | HNSVehicleEventPEOAttribute20 | ATTRIBUTE20 | — | — |
| 17 | HNSVehicleEventPEOAttribute21 | ATTRIBUTE21 | — | — |
| 18 | HNSVehicleEventPEOAttribute22 | ATTRIBUTE22 | — | — |
| 19 | HNSVehicleEventPEOAttribute23 | ATTRIBUTE23 | — | — |
| 20 | HNSVehicleEventPEOAttribute24 | ATTRIBUTE24 | — | — |
| 21 | HNSVehicleEventPEOAttribute25 | ATTRIBUTE25 | — | — |
| 22 | HNSVehicleEventPEOAttribute26 | ATTRIBUTE26 | — | — |
| 23 | HNSVehicleEventPEOAttribute27 | ATTRIBUTE27 | — | — |
| 24 | HNSVehicleEventPEOAttribute28 | ATTRIBUTE28 | — | — |
| 25 | HNSVehicleEventPEOAttribute29 | ATTRIBUTE29 | — | — |
| 26 | HNSVehicleEventPEOAttribute3 | ATTRIBUTE3 | — | — |
| 27 | HNSVehicleEventPEOAttribute30 | ATTRIBUTE30 | — | — |
| 28 | HNSVehicleEventPEOAttribute4 | ATTRIBUTE4 | — | — |
| 29 | HNSVehicleEventPEOAttribute5 | ATTRIBUTE5 | — | — |
| 30 | HNSVehicleEventPEOAttribute6 | ATTRIBUTE6 | — | — |
| 31 | HNSVehicleEventPEOAttribute7 | ATTRIBUTE7 | — | — |
| 32 | HNSVehicleEventPEOAttribute8 | ATTRIBUTE8 | — | — |
| 33 | HNSVehicleEventPEOAttribute9 | ATTRIBUTE9 | — | — |
| 34 | HNSVehicleEventPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 35 | HNSVehicleEventPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 36 | HNSVehicleEventPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 37 | HNSVehicleEventPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 38 | HNSVehicleEventPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 39 | HNSVehicleEventPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 40 | HNSVehicleEventPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 41 | HNSVehicleEventPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 42 | HNSVehicleEventPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 43 | HNSVehicleEventPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 44 | HNSVehicleEventPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 45 | HNSVehicleEventPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 46 | HNSVehicleEventPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 47 | HNSVehicleEventPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 48 | HNSVehicleEventPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 49 | HNSVehicleEventPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 50 | HNSVehicleEventPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 51 | HNSVehicleEventPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 52 | HNSVehicleEventPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 53 | HNSVehicleEventPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 54 | HNSVehicleEventPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 55 | HNSVehicleEventPEOCaseNumber | CASE_NUMBER | — | — |
| 56 | HNSVehicleEventPEOCellPhInUseFlag | CELL_PHONE_IN_USE_FLAG | — | ✅ |
| 57 | HNSVehicleEventPEOCompInUseFlag | COMPUTER_IN_USE_FLAG | — | ✅ |
| 58 | HNSVehicleEventPEOCompVehFlag | COMPANY_VEHICLE_FLAG | — | ✅ |
| 59 | HNSVehicleEventPEOCompanyAddrCity | COMPANY_ADDR_CITY | — | — |
| 60 | HNSVehicleEventPEOCompanyAddrCountry | COMPANY_ADDR_COUNTRY | — | — |
| 61 | HNSVehicleEventPEOCompanyAddrLine1 | COMPANY_ADDR_LINE1 | — | — |
| 62 | HNSVehicleEventPEOCompanyAddrLine2 | COMPANY_ADDR_LINE2 | — | — |
| 63 | HNSVehicleEventPEOCompanyAddrState | COMPANY_ADDR_STATE | — | — |
| 64 | HNSVehicleEventPEOCompanyAddrZipCode | COMPANY_ADDR_ZIP_CODE | — | — |
| 65 | HNSVehicleEventPEOContactId | CONTACT_ID | — | — |
| 66 | HNSVehicleEventPEOCostOfRentalVehicle | COST_OF_RENTAL_VEHICLE | — | — |
| 67 | HNSVehicleEventPEOCreatedBy | CREATED_BY | — | ✅ |
| 68 | HNSVehicleEventPEOCreationDate | CREATION_DATE | — | ✅ |
| 69 | HNSVehicleEventPEODamageDescr | DAMAGE_DESCR | — | ✅ |
| 70 | HNSVehicleEventPEODeletedFlag | DELETED_FLAG | — | ✅ |
| 71 | HNSVehicleEventPEODescribeDamage | DESCRIBE_DAMAGE | — | — |
| 72 | HNSVehicleEventPEODrivLicExpDate | DRIVERS_LICENSE_EXP_DATE | — | ✅ |
| 73 | HNSVehicleEventPEODrugTestPerfFlag | DRUG_TEST_PERFORM_FLAG | — | ✅ |
| 74 | HNSVehicleEventPEOEmpAsnId | EMPLOYEE_ASSIGN_ID | — | — |
| 75 | HNSVehicleEventPEOEmployeeId | EMPLOYEE_ID | — | ✅ |
| 76 | HNSVehicleEventPEOExpiryDate | EXPIRY_DATE | — | — |
| 77 | HNSVehicleEventPEOFatalityFlag | FATALITY_FLAG | — | ✅ |
| 78 | HNSVehicleEventPEOFleetVehicleFlg | FLEET_VEHICLE_FLG | — | — |
| 79 | HNSVehicleEventPEOIncDetailId | INCIDENT_DETAIL_ID | — | ✅ |
| 80 | HNSVehicleEventPEOInjuredFlag | INJURED_FLAG | — | ✅ |
| 81 | HNSVehicleEventPEOInsEmail | INS_EMAIL | — | — |
| 82 | HNSVehicleEventPEOInsPhoneAreaCode | INS_PHONE_AREA_CODE | — | — |
| 83 | HNSVehicleEventPEOInsPhoneCountryCode | INS_PHONE_COUNTRY_CODE | — | — |
| 84 | HNSVehicleEventPEOInsPhoneNum | INS_PHONE_NUM | — | — |
| 85 | HNSVehicleEventPEOInsuranceAddFlg | INSURANCE_ADD_FLG | — | — |
| 86 | HNSVehicleEventPEOInsuranceAgent | INSURANCE_AGENT | — | — |
| 87 | HNSVehicleEventPEOInsuranceCompanyName | INSURANCE_COMPANY_NAME | — | — |
| 88 | HNSVehicleEventPEOInsuranceInformationFlg | INSURANCE_INFORMATION_FLG | — | — |
| 89 | HNSVehicleEventPEOInsurancePolicyNumber | INSURANCE_POLICY_NUMBER | — | — |
| 90 | HNSVehicleEventPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 91 | HNSVehicleEventPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 92 | HNSVehicleEventPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 93 | HNSVehicleEventPEOLocationOfPedestrian | LOCATION_OF_PEDESTRIAN | — | — |
| 94 | HNSVehicleEventPEONonComVehAddCity | NON_COM_VEH_ADD_CITY | — | — |
| 95 | HNSVehicleEventPEONonComVehAddCountry | NON_COM_VEH_ADD_COUNTRY | — | — |
| 96 | HNSVehicleEventPEONonComVehAddLine1 | NON_COM_VEH_ADD_LINE1 | — | — |
| 97 | HNSVehicleEventPEONonComVehAddLine2 | NON_COM_VEH_ADD_LINE2 | — | — |
| 98 | HNSVehicleEventPEONonComVehAddState | NON_COM_VEH_ADD_STATE | — | — |
| 99 | HNSVehicleEventPEONonComVehAddZipCode | NON_COM_VEH_ADD_ZIP_CODE | — | — |
| 100 | HNSVehicleEventPEONonComVehBodyType | NON_COM_VEH_BODY_TYPE | — | — |
| 101 | HNSVehicleEventPEONonComVehContactName | NON_COM_VEH_CONTACT_NAME | — | — |
| 102 | HNSVehicleEventPEONonComVehLicenseNum | NON_COM_VEH_LICENSE_NUM | — | — |
| 103 | HNSVehicleEventPEONonComVehMake | NON_COM_VEH_MAKE | — | — |
| 104 | HNSVehicleEventPEONonComVehModel | NON_COM_VEH_MODEL | — | — |
| 105 | HNSVehicleEventPEONonComVehOwnerName | NON_COM_VEH_OWNER_NAME | — | — |
| 106 | HNSVehicleEventPEONonComVehRegiCountry | NON_COM_VEH_REGI_COUNTRY | — | — |
| 107 | HNSVehicleEventPEONonComVehRegiNum | NON_COM_VEH_REGI_NUM | — | — |
| 108 | HNSVehicleEventPEONonComVehRegiState | NON_COM_VEH_REGI_STATE | — | — |
| 109 | HNSVehicleEventPEONonComVehRegisterFlg | NON_COM_VEH_REGISTER_FLG | — | — |
| 110 | HNSVehicleEventPEONonComVehVinNum | NON_COM_VEH_VIN_NUM | — | — |
| 111 | HNSVehicleEventPEONonComVehYear | NON_COM_VEH_YEAR | — | — |
| 112 | HNSVehicleEventPEONonEmpAddrCity | NON_EMP_ADDR_CITY | — | ✅ |
| 113 | HNSVehicleEventPEONonEmpAddrCountry | NON_EMP_ADDR_COUNTRY | — | ✅ |
| 114 | HNSVehicleEventPEONonEmpAddrLine1 | NON_EMP_ADDR_LINE1 | — | ✅ |
| 115 | HNSVehicleEventPEONonEmpAddrLine2 | NON_EMP_ADDR_LINE2 | — | ✅ |
| 116 | HNSVehicleEventPEONonEmpAddrState | NON_EMP_ADDR_STATE | — | ✅ |
| 117 | HNSVehicleEventPEONonEmpAddrZipCode | NON_EMP_ADDR_ZIP_CODE | — | ✅ |
| 118 | HNSVehicleEventPEONonEmpEmail | NON_EMP_EMAIL | — | ✅ |
| 119 | HNSVehicleEventPEONonEmpName | NON_EMP_NAME | — | ✅ |
| 120 | HNSVehicleEventPEONonRelComVehContactName | NON_REL_COM_VEH_CONTACT_NAME | — | — |
| 121 | HNSVehicleEventPEOObjVeNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 122 | HNSVehicleEventPEOOwnerName | OWNER_NAME | — | — |
| 123 | HNSVehicleEventPEOPaidByCompanyFlg | PAID_BY_COMPANY_FLG | — | — |
| 124 | HNSVehicleEventPEOPedDoingPriorToIncident | PED_DOING_PRIOR_TO_INCIDENT | — | — |
| 125 | HNSVehicleEventPEOPedSafetyEquipment | PED_SAFETY_EQUIPMENT | — | — |
| 126 | HNSVehicleEventPEOPersonTypeCode | PERSON_TYPE_CODE | — | ✅ |
| 127 | HNSVehicleEventPEOPhCountryCodeNum | PHONE_COUNTRY_CODE_NUM | — | ✅ |
| 128 | HNSVehicleEventPEOPhoneAreaCode | PHONE_AREA_CODE | — | ✅ |
| 129 | HNSVehicleEventPEOPhoneNum | PHONE_NUM | — | ✅ |
| 130 | HNSVehicleEventPEORegistrationDate | REGISTRATION_DATE | — | — |
| 131 | HNSVehicleEventPEORelatedCompanyFlg | RELATED_COMPANY_FLG | — | — |
| 132 | HNSVehicleEventPEORelatedCompanyId | RELATED_COMPNAY_ID | — | — |
| 133 | HNSVehicleEventPEORentalAgreementNumber | RENTAL_AGREEMENT_NUMBER | — | — |
| 134 | HNSVehicleEventPEORentalCompanyName | RENTAL_COMPANY_NAME | — | — |
| 135 | HNSVehicleEventPEORentalDate | RENTAL_DATE | — | — |
| 136 | HNSVehicleEventPEORentalLocation | RENTAL_LOCATION | — | — |
| 137 | HNSVehicleEventPEORentalVehReplacementFlg | RENTAL_VEH_REPLACEMENT_FLG | — | — |
| 138 | HNSVehicleEventPEORepCostOfRentalVehicle | REP_COST_OF_RENTAL_VEHICLE | — | — |
| 139 | HNSVehicleEventPEORepInsuranceAddFlg | REP_INSURANCE_ADD_FLG | — | — |
| 140 | HNSVehicleEventPEORepPaidByCompanyFlg | REP_PAID_BY_COMPANY_FLG | — | — |
| 141 | HNSVehicleEventPEORepRentalAgreementNumber | REP_RENTAL_AGREEMENT_NUMBER | — | — |
| 142 | HNSVehicleEventPEORepRentalCompanyName | REP_RENTAL_COMPANY_NAME | — | — |
| 143 | HNSVehicleEventPEORepRentalDate | REP_RENTAL_DATE | — | — |
| 144 | HNSVehicleEventPEORepRentalLocation | REP_RENTAL_LOCATION | — | — |
| 145 | HNSVehicleEventPEORepairCost | REPAIR_COST | — | — |
| 146 | HNSVehicleEventPEOSeatBeltInUseFlag | SEAT_BELT_IN_USE_FLAG | — | ✅ |
| 147 | HNSVehicleEventPEOStateIssdDrvrsLic | STATE_ISSUED_DRIVERS_LICENSE | — | ✅ |
| 148 | HNSVehicleEventPEOTakenToHospFlag | TAKEN_TO_HOSPITAL_FLAG | — | ✅ |
| 149 | HNSVehicleEventPEOTowingCompContDtl | TOWING_COMPANY_CONTACT_DETAIL | — | ✅ |
| 150 | HNSVehicleEventPEOVehAreaImpactCd | VEHICLE_AREA_IMPACT_CODE | — | ✅ |
| 151 | HNSVehicleEventPEOVehClasfctnCode | VEHICLE_CLASSIFICATION_CODE | — | ✅ |
| 152 | HNSVehicleEventPEOVehCompanyIdNum | VEHICLE_COMPANY_ID_NUM | — | ✅ |
| 153 | HNSVehicleEventPEOVehDriverLocCode | VEHICLE_DRIVER_LOCATION_CODE | — | ✅ |
| 154 | HNSVehicleEventPEOVehDriversLicNum | VEHICLE_DRIVERS_LICENSE_NUM | — | ✅ |
| 155 | HNSVehicleEventPEOVehGrossWeight | VEHICLE_GROSS_WEIGHT | — | ✅ |
| 156 | HNSVehicleEventPEOVehHasAirbagFlag | VEHICLE_HAS_AIRBAG_FLAG | — | ✅ |
| 157 | HNSVehicleEventPEOVehHasPasngrFlag | VEHICLE_HAS_PASSENGER_FLAG | — | ✅ |
| 158 | HNSVehicleEventPEOVehIncEvtDtlId | VEH_INC_EVT_DETAIL_ID | 🔑 | ✅ |
| 159 | HNSVehicleEventPEOVehLicensePltNum | VEHICLE_LICENSE_PLATE_NUM | — | ✅ |
| 160 | HNSVehicleEventPEOVehModelYear | VEHICLE_MODEL_YEAR | — | ✅ |
| 161 | HNSVehicleEventPEOVehMovementCode | VEHICLE_MOVEMENT_CODE | — | ✅ |
| 162 | HNSVehicleEventPEOVehPositionCode | VEHICLE_POSITION_CODE | — | ✅ |
| 163 | HNSVehicleEventPEOVehRegstrdFlag | VEHICLE_REGISTERED_FLAG | — | ✅ |
| 164 | HNSVehicleEventPEOVehRegstrtnCntry | VEHICLE_REGISTRATION_COUNTRY | — | ✅ |
| 165 | HNSVehicleEventPEOVehRegstrtnNum | VEHICLE_REGISTRATION_NUM | — | ✅ |
| 166 | HNSVehicleEventPEOVehRegstrtnState | VEHICLE_REGISTRATION_STATE | — | ✅ |
| 167 | HNSVehicleEventPEOVehSpeedUnitCd | VEHICLE_SPEED_UNIT_CD | — | ✅ |
| 168 | HNSVehicleEventPEOVehTowedFlag | VEHICLE_TOWED_FLAG | — | ✅ |
| 169 | HNSVehicleEventPEOVehWeightUnitCd | VEHICLE_WEIGHT_UNIT_CD | — | ✅ |
| 170 | HNSVehicleEventPEOVehicleBodyType | VEHICLE_BODY_TYPE | — | ✅ |
| 171 | HNSVehicleEventPEOVehicleDescription | VEHICLE_DESCRIPTION | — | — |
| 172 | HNSVehicleEventPEOVehicleMake | VEHICLE_MAKE | — | ✅ |
| 173 | HNSVehicleEventPEOVehicleModel | VEHICLE_MODEL | — | ✅ |
| 174 | HNSVehicleEventPEOVehicleSpeed | VEHICLE_SPEED | — | ✅ |
| 175 | HNSVehicleEventPEOVehicleVinNum | VEHICLE_VIN_NUM | — | ✅ |
| 176 | HNSVehicleEventPEOWasRentalFlag | WAS_RENTAL_FLAG | — | — |

### [[hns_veh_inc_event_passengers|HNS_VEH_INC_EVENT_PASSENGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HNSVehEventPasngrsPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | HNSVehEventPasngrsPEOCreationDt | CREATION_DATE | — | ✅ |
| 3 | HNSVehEventPasngrsPEODelFlag | DELETED_FLAG | — | ✅ |
| 4 | HNSVehEventPasngrsPEOEmpAsnId | EMPLOYEE_ASSIGN_ID | — | — |
| 5 | HNSVehEventPasngrsPEOEmpId | EMPLOYEE_ID | — | ✅ |
| 6 | HNSVehEventPasngrsPEOLastUpdtdBy | LAST_UPDATED_BY | — | ✅ |
| 7 | HNSVehEventPasngrsPEOLstUpdtDt | LAST_UPDATE_DATE | — | ✅ |
| 8 | HNSVehEventPasngrsPEOLstUpdtLgn | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | HNSVehEventPasngrsPEOObjVerNum | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | HNSVehEventPasngrsPEOPasAddrCity | PASSENGER_ADDR_CITY | — | ✅ |
| 11 | HNSVehEventPasngrsPEOPasAddrLine1 | PASSENGER_ADDR_LINE1 | — | ✅ |
| 12 | HNSVehEventPasngrsPEOPasAddrLine2 | PASSENGER_ADDR_LINE2 | — | ✅ |
| 13 | HNSVehEventPasngrsPEOPasAddrState | PASSENGER_ADDR_STATE | — | ✅ |
| 14 | HNSVehEventPasngrsPEOPasAreaCode | PASSENGER_AREA_CODE | — | ✅ |
| 15 | HNSVehEventPasngrsPEOPasCntCdNum | PASSENGER_COUNTRY_CODE_NUM | — | ✅ |
| 16 | HNSVehEventPasngrsPEOPasCountry | PASSENGER_COUNTRY | — | ✅ |
| 17 | HNSVehEventPasngrsPEOPasEmail | PASSENGER_EMAIL | — | ✅ |
| 18 | HNSVehEventPasngrsPEOPasFtltyFlag | PASSENGER_FATALITY_FLAG | — | ✅ |
| 19 | HNSVehEventPasngrsPEOPasInjrdFlag | PASSENGER_INJURED_FLAG | — | ✅ |
| 20 | HNSVehEventPasngrsPEOPasPerTypCd | PASSENGER_PER_TYPE_CODE | — | ✅ |
| 21 | HNSVehEventPasngrsPEOPasPhoneNum | PASSENGER_PHONE_NUM | — | ✅ |
| 22 | HNSVehEventPasngrsPEOPasZipCode | PASSENGER_ZIP_CODE | — | ✅ |
| 23 | HNSVehEventPasngrsPEOPassengerId | PASSENGER_ID | — | ✅ |
| 24 | HNSVehEventPasngrsPEOPassengerName | PASSENGER_NAME | 🔑 | ✅ |
| 25 | HNSVehEventPasngrsPEOTakenToHospFlg | TAKEN_TO_HOSPITAL_FLAG | — | ✅ |
| 26 | HNSVehEventPasngrsPEOVehIncEvtDtlId | VEH_INC_EVT_DETAIL_ID | — | ✅ |
| 27 | HNSVehEventPasngrsPEOWearSeatBltFlg | WEARING_SEAT_BELT_FLAG | — | ✅ |

### [[hns_veh_inc_event_summary|HNS_VEH_INC_EVENT_SUMMARY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HnsVehIncEventSummaryPEOAttrCat | ATTRIBUTE_CATEGORY | — | — |
| 2 | HnsVehIncEventSummaryPEOAttrNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 3 | HnsVehIncEventSummaryPEOAttrNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 4 | HnsVehIncEventSummaryPEOAttrNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 5 | HnsVehIncEventSummaryPEOAttrNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 6 | HnsVehIncEventSummaryPEOAttrNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 7 | HnsVehIncEventSummaryPEOAttrNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 8 | HnsVehIncEventSummaryPEOAttrNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 9 | HnsVehIncEventSummaryPEOAttrNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 10 | HnsVehIncEventSummaryPEOAttrNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 11 | HnsVehIncEventSummaryPEOAttrNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 12 | HnsVehIncEventSummaryPEOAttrTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 13 | HnsVehIncEventSummaryPEOAttrTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 14 | HnsVehIncEventSummaryPEOAttrTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 15 | HnsVehIncEventSummaryPEOAttrTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 16 | HnsVehIncEventSummaryPEOAttrTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 17 | HnsVehIncEventSummaryPEOAttrTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 18 | HnsVehIncEventSummaryPEOAttrTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 19 | HnsVehIncEventSummaryPEOAttrTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 20 | HnsVehIncEventSummaryPEOAttrTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 21 | HnsVehIncEventSummaryPEOAttrTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 22 | HnsVehIncEventSummaryPEOAttribute1 | ATTRIBUTE1 | — | — |
| 23 | HnsVehIncEventSummaryPEOAttribute10 | ATTRIBUTE10 | — | — |
| 24 | HnsVehIncEventSummaryPEOAttribute11 | ATTRIBUTE11 | — | — |
| 25 | HnsVehIncEventSummaryPEOAttribute12 | ATTRIBUTE12 | — | — |
| 26 | HnsVehIncEventSummaryPEOAttribute13 | ATTRIBUTE13 | — | — |
| 27 | HnsVehIncEventSummaryPEOAttribute14 | ATTRIBUTE14 | — | — |
| 28 | HnsVehIncEventSummaryPEOAttribute15 | ATTRIBUTE15 | — | — |
| 29 | HnsVehIncEventSummaryPEOAttribute16 | ATTRIBUTE16 | — | — |
| 30 | HnsVehIncEventSummaryPEOAttribute17 | ATTRIBUTE17 | — | — |
| 31 | HnsVehIncEventSummaryPEOAttribute18 | ATTRIBUTE18 | — | — |
| 32 | HnsVehIncEventSummaryPEOAttribute19 | ATTRIBUTE19 | — | — |
| 33 | HnsVehIncEventSummaryPEOAttribute2 | ATTRIBUTE2 | — | — |
| 34 | HnsVehIncEventSummaryPEOAttribute20 | ATTRIBUTE20 | — | — |
| 35 | HnsVehIncEventSummaryPEOAttribute21 | ATTRIBUTE21 | — | — |
| 36 | HnsVehIncEventSummaryPEOAttribute22 | ATTRIBUTE22 | — | — |
| 37 | HnsVehIncEventSummaryPEOAttribute23 | ATTRIBUTE23 | — | — |
| 38 | HnsVehIncEventSummaryPEOAttribute24 | ATTRIBUTE24 | — | — |
| 39 | HnsVehIncEventSummaryPEOAttribute25 | ATTRIBUTE25 | — | — |
| 40 | HnsVehIncEventSummaryPEOAttribute26 | ATTRIBUTE26 | — | — |
| 41 | HnsVehIncEventSummaryPEOAttribute27 | ATTRIBUTE27 | — | — |
| 42 | HnsVehIncEventSummaryPEOAttribute28 | ATTRIBUTE28 | — | — |
| 43 | HnsVehIncEventSummaryPEOAttribute29 | ATTRIBUTE29 | — | — |
| 44 | HnsVehIncEventSummaryPEOAttribute3 | ATTRIBUTE3 | — | — |
| 45 | HnsVehIncEventSummaryPEOAttribute30 | ATTRIBUTE30 | — | — |
| 46 | HnsVehIncEventSummaryPEOAttribute4 | ATTRIBUTE4 | — | — |
| 47 | HnsVehIncEventSummaryPEOAttribute5 | ATTRIBUTE5 | — | — |
| 48 | HnsVehIncEventSummaryPEOAttribute6 | ATTRIBUTE6 | — | — |
| 49 | HnsVehIncEventSummaryPEOAttribute7 | ATTRIBUTE7 | — | — |
| 50 | HnsVehIncEventSummaryPEOAttribute8 | ATTRIBUTE8 | — | — |
| 51 | HnsVehIncEventSummaryPEOAttribute9 | ATTRIBUTE9 | — | — |
| 52 | HnsVehIncEventSummaryPEOCitationNum | CITATION_NUM | — | ✅ |
| 53 | HnsVehIncEventSummaryPEOCreatedBy | CREATED_BY | — | ✅ |
| 54 | HnsVehIncEventSummaryPEOCreationDate | CREATION_DATE | — | ✅ |
| 55 | HnsVehIncEventSummaryPEODeletedFlag | DELETED_FLAG | — | ✅ |
| 56 | HnsVehIncEventSummaryPEOIncDetailId | INCIDENT_DETAIL_ID | — | ✅ |
| 57 | HnsVehIncEventSummaryPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 58 | HnsVehIncEventSummaryPEOLatUpdtLgn | LAST_UPDATE_LOGIN | — | ✅ |
| 59 | HnsVehIncEventSummaryPEOLightCondCd | LIGHT_CONDITION_CODE | — | ✅ |
| 60 | HnsVehIncEventSummaryPEOLstUpdtDt | LAST_UPDATE_DATE | — | ✅ |
| 61 | HnsVehIncEventSummaryPEOObjVerNum | OBJECT_VERSION_NUMBER | — | ✅ |
| 62 | HnsVehIncEventSummaryPEOPoliceAgncLoc | POLICE_AGENCY_LOCATION | — | ✅ |
| 63 | HnsVehIncEventSummaryPEOPoliceBadgeNum | POLICE_BADGE_NUM | — | ✅ |
| 64 | HnsVehIncEventSummaryPEOPoliceReportFlag | POLICE_REPORT_FLAG | — | ✅ |
| 65 | HnsVehIncEventSummaryPEORoadCondCd | ROAD_CONDITION_CODE | — | ✅ |
| 66 | HnsVehIncEventSummaryPEOTrafCondCd | TRAFFIC_CONDITION_CODE | — | ✅ |
| 67 | HnsVehIncEventSummaryPEOTrafCtrlsCd | TRAFFIC_CONTROLS_CODE | — | ✅ |
| 68 | HnsVehIncEventSummaryPEOVehClsnTypCd | VEHICLE_COLLISION_TYPE_CODE | — | ✅ |
| 69 | HnsVehIncEventSummaryPEOVehIncEvtSumId | VEH_INC_EVT_SUMMARY_ID | 🔑 | ✅ |
| 70 | HnsVehIncEventSummaryPEOVehSpeedLmt | VEHICLE_SPEED_LIMIT | — | ✅ |
| 71 | HnsVehIncEventSummaryPEOVehSpeedUntCd | VEHICLE_SPEED_UNIT_CD | — | ✅ |
| 72 | HnsVehIncEventSummaryPEOVehStruckCode | VEHICLE_STRUCK_CODE | — | ✅ |
| 73 | HnsVehIncEventSummaryPEOWeatherCondCd | WEATHER_CONDITION_CODE | — | ✅ |
| 74 | VehicleAccCategoryCode | VEHICLE_ACC_CATEGORY_CODE | — | ✅ |
| 75 | VehicleStruckByCode | VEHICLE_STRUCK_BY_CODE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
