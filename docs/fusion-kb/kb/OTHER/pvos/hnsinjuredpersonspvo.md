---
id: DOC-OTHER-PVO-HNSInjuredPersonsPVO
doc_type: system-doc
title: "HNSInjuredPersonsPVO — PVO Cross-Module"
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
  - HNSInjuredPersonsPVO
  - hnsinjuredpersonspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HNSInjuredPersonsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de HNSInjured Persons. Acessa as tabelas: HNS_INCIDENTS_DETAIL, HNS_INJURED_PERSONS, HNS_INJURED_PERSONS_SUMMARY.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HealthandSafetyAM.HNSInjuredPersonsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 85 | 3 | 2 | 74 | 87% |

---

## 🔗 Tabelas Relacionadas

- [[hns_incidents_detail|HNS_INCIDENTS_DETAIL]] — 2 atributos
- [[hns_injured_persons|HNS_INJURED_PERSONS]] — 72 atributos (1 PKs, 70 BICC)
- [[hns_injured_persons_summary|HNS_INJURED_PERSONS_SUMMARY]] — 11 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[hns_incidents_detail|HNS_INCIDENTS_DETAIL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DerivedEventDate | INCIDENT_EVENT_DATE | — | — |
| 2 | HNSIncidentEventDetailsPEOIncidentDetailId | INCIDENT_DETAIL_ID | — | — |

### [[hns_injured_persons|HNS_INJURED_PERSONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HNSInjuredPersonsPEOCaseNum | CASE_NUMBER | — | ✅ |
| 2 | HNSInjuredPersonsPEOClassificationCode | CLASSIFICATION_CODE | — | ✅ |
| 3 | HNSInjuredPersonsPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | HNSInjuredPersonsPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | HNSInjuredPersonsPEODeletedFlag | DELETED_FLAG | — | ✅ |
| 6 | HNSInjuredPersonsPEODescrOfTrtmnt | DESCRIPTION_OF_TREATMENT | — | ✅ |
| 7 | HNSInjuredPersonsPEODsbDysAwyFrmWrkDt | DISAB_DAYS_AWY_FRM_WRK_DT | — | ✅ |
| 8 | HNSInjuredPersonsPEODysAwyFrmWrk | DAYS_AWAY_FROM_WRK | — | ✅ |
| 9 | HNSInjuredPersonsPEOEmpRtnToWrkFlag | EMP_RTN_TO_WRK_FLAG | — | ✅ |
| 10 | HNSInjuredPersonsPEOFacilityAddressLine1 | FACILITY_ADDRESS_LINE1 | — | ✅ |
| 11 | HNSInjuredPersonsPEOFacilityAddressLine2 | FACILITY_ADDRESS_LINE2 | — | ✅ |
| 12 | HNSInjuredPersonsPEOFacilityCity | FACILITY_CITY | — | ✅ |
| 13 | HNSInjuredPersonsPEOFacilityCountry | FACILITY_COUNTRY | — | ✅ |
| 14 | HNSInjuredPersonsPEOFacilityName | FACILITY_NAME | — | ✅ |
| 15 | HNSInjuredPersonsPEOFacilityState | FACILITY_STATE | — | ✅ |
| 16 | HNSInjuredPersonsPEOFacilityZipCode | FACILITY_ZIP_CODE | — | ✅ |
| 17 | HNSInjuredPersonsPEOFatalityDate | FATALITY_DATE | — | ✅ |
| 18 | HNSInjuredPersonsPEOHrsAtWrkBfrInjIll | HRS_AT_WRK_BEFORE_INJ_ILL | — | ✅ |
| 19 | HNSInjuredPersonsPEOIllnessNatureCode | ILLNESS_NATURE_CODE | — | ✅ |
| 20 | HNSInjuredPersonsPEOInciInjPerAsnId | INCI_INJ_PERSON_ASSIGN_ID | — | — |
| 21 | HNSInjuredPersonsPEOInciInjPersonId | INCI_INJ_PERSON_ID | — | ✅ |
| 22 | HNSInjuredPersonsPEOIncidentDetailId | INCIDENT_DETAIL_ID | — | — |
| 23 | HNSInjuredPersonsPEOInjIllDevOvrTmFlg | INJ_ILL_DEV_OVER_TIME_FLAG | — | ✅ |
| 24 | HNSInjuredPersonsPEOInjIllInfrmdByPerNm | INJ_ILL_INFRMD_BY_PER_NAME | — | ✅ |
| 25 | HNSInjuredPersonsPEOInjIllOccuredDate | INJ_ILL_OCCURED_DATE | — | ✅ |
| 26 | HNSInjuredPersonsPEOInjPerNonempTypeCd | INJ_PER_NONEMP_TYPE_CD | — | ✅ |
| 27 | HNSInjuredPersonsPEOInjPersonTypeCode | INJ_PERSON_TYPE_CODE | — | ✅ |
| 28 | HNSInjuredPersonsPEOInjurdCountryCodNum | INJURED_COUNTRY_CODE_NUM | — | ✅ |
| 29 | HNSInjuredPersonsPEOInjuredAreaCode | INJURED_AREA_CODE | — | ✅ |
| 30 | HNSInjuredPersonsPEOInjuredEmail | INJURED_EMAIL | — | ✅ |
| 31 | HNSInjuredPersonsPEOInjuredName | INJURED_NAME | — | ✅ |
| 32 | HNSInjuredPersonsPEOInjuredPersonId | INJURED_PERSON_ID | 🔑 | ✅ |
| 33 | HNSInjuredPersonsPEOInjuredPhoneno | INJURED_PHONENO | — | ✅ |
| 34 | HNSInjuredPersonsPEOInjuryMcnsmLvl2Cd | INJURY_MECHANISM_LVL2_CODE | — | ✅ |
| 35 | HNSInjuredPersonsPEOInjuryMcnsmLvl3Cd | INJURY_MECHANISM_LVL3_CODE | — | ✅ |
| 36 | HNSInjuredPersonsPEOInjuryMcnsmLvl4Cd | INJURY_MECHANISM_LVL4_CODE | — | ✅ |
| 37 | HNSInjuredPersonsPEOInjuryMechCode | INJURY_MECHANISM_CODE | — | ✅ |
| 38 | HNSInjuredPersonsPEOJobTransferFlag | JOB_TRANSFER_FLAG | — | ✅ |
| 39 | HNSInjuredPersonsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 40 | HNSInjuredPersonsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 41 | HNSInjuredPersonsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 42 | HNSInjuredPersonsPEOLostTimeInHrs | LOST_TIME_IN_HRS | — | ✅ |
| 43 | HNSInjuredPersonsPEOLosttimeFlag | LOSTTIME_FLAG | — | ✅ |
| 44 | HNSInjuredPersonsPEOMedProfName | MED_PROF_NAME | — | ✅ |
| 45 | HNSInjuredPersonsPEOModDtsRstrctnDescr | MOD_DUTIES_RESTRICTN_DESCR | — | ✅ |
| 46 | HNSInjuredPersonsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 47 | HNSInjuredPersonsPEOPerInfrmdInjIllDt | PER_INFORMED_INJ_ILL_DATE | — | ✅ |
| 48 | HNSInjuredPersonsPEOPerUnblToWrkFlag | PER_UNABLE_TO_WRK_FLAG | — | ✅ |
| 49 | HNSInjuredPersonsPEOPersonActivityDescr | PERSON_ACTIVITY_DESCR | — | ✅ |
| 50 | HNSInjuredPersonsPEOPrevInjIllDate | PREV_INJ_ILL_DATE | — | ✅ |
| 51 | HNSInjuredPersonsPEORcrdblTypeCd | RECORDABLE_TYPE_CD | — | ✅ |
| 52 | HNSInjuredPersonsPEORecordableFlag | RECORDABLE_FLAG | — | ✅ |
| 53 | HNSInjuredPersonsPEORecurringFlag | RECURRING_FLAG | — | ✅ |
| 54 | HNSInjuredPersonsPEOReportableFlag | REPORTABLE_FLAG | — | ✅ |
| 55 | HNSInjuredPersonsPEORgltrNtfdBy | REGULATOR_NOTIFIED_BY | — | ✅ |
| 56 | HNSInjuredPersonsPEORgltrNtfdDt | REGULATOR_NOTIFIED_DATE | — | ✅ |
| 57 | HNSInjuredPersonsPEORgltrNtfdFlg | REGULATOR_NOTIFIED_FLAG | — | ✅ |
| 58 | HNSInjuredPersonsPEORgltrNtfdMdmCd | REGULATR_NOTIFIED_MEDIUM_CD | — | ✅ |
| 59 | HNSInjuredPersonsPEORtnToWrkDt | RTN_TO_WRK_DATE | — | ✅ |
| 60 | HNSInjuredPersonsPEORtnToWrkTypCd | RTN_TO_WRK_TYPE_CD | — | ✅ |
| 61 | HNSInjuredPersonsPEOSrcOfInjryLvl2Cd | SOURCE_OF_INJURY_LVL2_CODE | — | ✅ |
| 62 | HNSInjuredPersonsPEOSrcOfInjryLvl3Cd | SOURCE_OF_INJURY_LVL3_CODE | — | ✅ |
| 63 | HNSInjuredPersonsPEOSrcOfInjryLvl4Cd | SOURCE_OF_INJURY_LVL4_CODE | — | ✅ |
| 64 | HNSInjuredPersonsPEOSrcOfInjuryCode | SOURCE_OF_INJURY_CODE | — | ✅ |
| 65 | HNSInjuredPersonsPEOSymFrstNtcdDt | SYM_FIRST_NOTICED_DATE | — | ✅ |
| 66 | HNSInjuredPersonsPEOTimeFnshdWrk | TIME_FINISHED_WORK | — | ✅ |
| 67 | HNSInjuredPersonsPEOTimeStartedWork | TIME_STARTED_WORK | — | ✅ |
| 68 | HNSInjuredPersonsPEOTreatmentFlag | TREATMENT_FLAG | — | ✅ |
| 69 | HNSInjuredPersonsPEOTreatmentTypeCode | TREATMENT_TYPE_CODE | — | ✅ |
| 70 | HNSInjuredPersonsPEOTxFacZipCd | TX_FACILITY_ZIP_CODE | — | ✅ |
| 71 | HNSInjuredPersonsPEOWorkrelatedFlag | WORKRELATED_FLAG | — | ✅ |
| 72 | HNSInjuredPersonsPEOXfrRestrctnDays | XFR_RESTRICTN_DAYS | — | ✅ |

### [[hns_injured_persons_summary|HNS_INJURED_PERSONS_SUMMARY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HNSInjuredPersonSummaryPEOCreatedBy | CREATED_BY | — | — |
| 2 | HNSInjuredPersonSummaryPEOCreationDate | CREATION_DATE | — | — |
| 3 | HNSInjuredPersonSummaryPEODeletedFlag | DELETED_FLAG | — | ✅ |
| 4 | HNSInjuredPersonSummaryPEODtTmNtfd | DATE_TIME_NOTIFIED | — | ✅ |
| 5 | HNSInjuredPersonSummaryPEOHrNtfdFlg | HR_NOTIFIED_FLAG | — | ✅ |
| 6 | HNSInjuredPersonSummaryPEOIncDtlId | INCIDENT_DETAIL_ID | — | — |
| 7 | HNSInjuredPersonSummaryPEOInjPerSumId | INJ_PERSON_SUMMARY_ID | 🔑 | ✅ |
| 8 | HNSInjuredPersonSummaryPEOLstUpdtDt | LAST_UPDATE_DATE | — | — |
| 9 | HNSInjuredPersonSummaryPEOLstUpdtLgn | LAST_UPDATE_LOGIN | — | — |
| 10 | HNSInjuredPersonSummaryPEOLstUpdtdBy | LAST_UPDATED_BY | — | — |
| 11 | HNSInjuredPersonSummaryPEOObjVersNum | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
