---
id: DOC-OTHER-PVO-CompetenciesCalbRatingPVO
doc_type: system-doc
title: "CompetenciesCalbRatingPVO — PVO Cross-Module"
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
  - CompetenciesCalbRatingPVO
  - competenciescalbratingpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CompetenciesCalbRatingPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Competencies Calb Rating. Acessa as tabelas: HRR_DASHBOARDS, HRR_MEETINGS, HRR_TMPL_METRIC_CONFIG (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmTalentCalibMeetingsAM.CompetenciesCalbRatingPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 147 | 4 | 4 | 8 | 5% |

---

## 🔗 Tabelas Relacionadas

- [[hrr_dashboards|HRR_DASHBOARDS]] — 29 atributos (1 PKs, 2 BICC)
- [[hrr_meetings|HRR_MEETINGS]] — 88 atributos (1 PKs, 2 BICC)
- [[hrr_tmpl_metric_config|HRR_TMPL_METRIC_CONFIG]] — 16 atributos (1 PKs, 2 BICC)
- [[hrt_profiles_b|HRT_PROFILES_B]] — 14 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[hrr_dashboards|HRR_DASHBOARDS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DashboardPEOAgeGroupValue | AGE_GROUP_VALUE | — | — |
| 2 | DashboardPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 3 | DashboardPEOBuLeaderDirectId | BU_LEADER_DIRECT_ID | — | — |
| 4 | DashboardPEOBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 5 | DashboardPEOCreatedBy1 | CREATED_BY | — | — |
| 6 | DashboardPEOCreationDate1 | CREATION_DATE | — | — |
| 7 | DashboardPEODashboardId | DASHBOARD_ID | 🔑 | ✅ |
| 8 | DashboardPEOExtnMetricCalibValue1 | EXTN_METRIC_CALIB_VALUE1 | — | — |
| 9 | DashboardPEOExtnMetricCalibValue2 | EXTN_METRIC_CALIB_VALUE2 | — | — |
| 10 | DashboardPEOExtnMetricValue1 | EXTN_METRIC_VALUE1 | — | — |
| 11 | DashboardPEOExtnMetricValue2 | EXTN_METRIC_VALUE2 | — | — |
| 12 | DashboardPEOImpactLossCalbRtLvlId | IMPACT_LOSS_CALB_RT_LVL_ID | — | — |
| 13 | DashboardPEOImpactLossRtLvlId | IMPACT_LOSS_RT_LVL_ID | — | — |
| 14 | DashboardPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 15 | DashboardPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 16 | DashboardPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 17 | DashboardPEOMeetingId | MEETING_ID | — | — |
| 18 | DashboardPEOMobilityCalibValue | MOBILITY_CALIB_VALUE | — | — |
| 19 | DashboardPEOMobilityValue | MOBILITY_VALUE | — | — |
| 20 | DashboardPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 21 | DashboardPEOPerfCalibRtLvlId | PERF_CALIB_RT_LVL_ID | — | — |
| 22 | DashboardPEOPerfRtLvlId | PERF_RT_LVL_ID | — | — |
| 23 | DashboardPEOPersonId1 | PERSON_ID | — | — |
| 24 | DashboardPEOPotCalibRtLvlId | POT_CALIB_RT_LVL_ID | — | — |
| 25 | DashboardPEOPotRtLvlId | POT_RT_LVL_ID | — | — |
| 26 | DashboardPEORiskLossCalibRtLvlId | RISK_LOSS_CALIB_RT_LVL_ID | — | — |
| 27 | DashboardPEORiskLossRtLvlId | RISK_LOSS_RT_LVL_ID | — | — |
| 28 | DashboardPEOTalentScorCalbRtLvlId | TALENT_SCOR_CALB_RT_LVL_ID | — | — |
| 29 | DashboardPEOTalentScoreRtLvlId | TALENT_SCORE_RT_LVL_ID | — | — |

### [[hrr_meetings|HRR_MEETINGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MeetingPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | MeetingPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | MeetingPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | MeetingPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | MeetingPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | MeetingPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | MeetingPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | MeetingPEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | MeetingPEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | MeetingPEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | MeetingPEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | MeetingPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | MeetingPEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | MeetingPEOAttribute21 | ATTRIBUTE21 | — | — |
| 15 | MeetingPEOAttribute22 | ATTRIBUTE22 | — | — |
| 16 | MeetingPEOAttribute23 | ATTRIBUTE23 | — | — |
| 17 | MeetingPEOAttribute24 | ATTRIBUTE24 | — | — |
| 18 | MeetingPEOAttribute25 | ATTRIBUTE25 | — | — |
| 19 | MeetingPEOAttribute26 | ATTRIBUTE26 | — | — |
| 20 | MeetingPEOAttribute27 | ATTRIBUTE27 | — | — |
| 21 | MeetingPEOAttribute28 | ATTRIBUTE28 | — | — |
| 22 | MeetingPEOAttribute29 | ATTRIBUTE29 | — | — |
| 23 | MeetingPEOAttribute3 | ATTRIBUTE3 | — | — |
| 24 | MeetingPEOAttribute30 | ATTRIBUTE30 | — | — |
| 25 | MeetingPEOAttribute4 | ATTRIBUTE4 | — | — |
| 26 | MeetingPEOAttribute5 | ATTRIBUTE5 | — | — |
| 27 | MeetingPEOAttribute6 | ATTRIBUTE6 | — | — |
| 28 | MeetingPEOAttribute7 | ATTRIBUTE7 | — | — |
| 29 | MeetingPEOAttribute8 | ATTRIBUTE8 | — | — |
| 30 | MeetingPEOAttribute9 | ATTRIBUTE9 | — | — |
| 31 | MeetingPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 32 | MeetingPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 33 | MeetingPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 34 | MeetingPEOAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 35 | MeetingPEOAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 36 | MeetingPEOAttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 37 | MeetingPEOAttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 38 | MeetingPEOAttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 39 | MeetingPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 40 | MeetingPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 41 | MeetingPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 42 | MeetingPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 43 | MeetingPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 44 | MeetingPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 45 | MeetingPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 46 | MeetingPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 47 | MeetingPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 48 | MeetingPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 49 | MeetingPEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 50 | MeetingPEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 51 | MeetingPEOAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 52 | MeetingPEOAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 53 | MeetingPEOAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 54 | MeetingPEOAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 55 | MeetingPEOAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 56 | MeetingPEOAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 57 | MeetingPEOAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 58 | MeetingPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 59 | MeetingPEOAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 60 | MeetingPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 61 | MeetingPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 62 | MeetingPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 63 | MeetingPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 64 | MeetingPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 65 | MeetingPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 66 | MeetingPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 67 | MeetingPEOBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 68 | MeetingPEOCreatedBy2 | CREATED_BY | — | — |
| 69 | MeetingPEOCreationDate2 | CREATION_DATE | — | — |
| 70 | MeetingPEODashboardTmplId | DASHBOARD_TMPL_ID | — | — |
| 71 | MeetingPEODataSubmitDate | DATA_SUBMIT_DATE | — | — |
| 72 | MeetingPEODataValidityCode | DATA_VALIDITY_CODE | — | — |
| 73 | MeetingPEOLastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 74 | MeetingPEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 75 | MeetingPEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 76 | MeetingPEOMeetingDate | MEETING_DATE | — | — |
| 77 | MeetingPEOMeetingFacilitatorNotes | MEETING_FACILITATOR_NOTES | — | — |
| 78 | MeetingPEOMeetingId1 | MEETING_ID | 🔑 | ✅ |
| 79 | MeetingPEOMeetingInstructions | MEETING_INSTRUCTIONS | — | — |
| 80 | MeetingPEOMeetingLeaderId | MEETING_LEADER_ID | — | — |
| 81 | MeetingPEOMeetingOrganizationId | MEETING_ORGANIZATION_ID | — | — |
| 82 | MeetingPEOMeetingPurpose | MEETING_PURPOSE | — | — |
| 83 | MeetingPEOMeetingStatusCode | MEETING_STATUS_CODE | — | — |
| 84 | MeetingPEOMeetingSubmissionDate | MEETING_SUBMISSION_DATE | — | — |
| 85 | MeetingPEOMeetingSubmitStatusCode | MEETING_SUBMIT_STATUS_CODE | — | — |
| 86 | MeetingPEOMeetingTitle | MEETING_TITLE | — | — |
| 87 | MeetingPEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 88 | MeetingPEOPrefReviewQualifierId | PREF_REVIEW_QUALIFIER_ID | — | — |

### [[hrr_tmpl_metric_config|HRR_TMPL_METRIC_CONFIG]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DasTmplConfigEOContentTypeId | CONTENT_TYPE_ID | — | — |
| 2 | DasTmplConfigEOCreatedBy3 | CREATED_BY | — | — |
| 3 | DasTmplConfigEOCreationDate3 | CREATION_DATE | — | — |
| 4 | DasTmplConfigEODashboardColumnName | DASHBOARD_COLUMN_NAME | — | — |
| 5 | DasTmplConfigEODashboardTmplId1 | DASHBOARD_TMPL_ID | 🔑 | ✅ |
| 6 | DasTmplConfigEOEnterpriseId | ENTERPRISE_ID | — | — |
| 7 | DasTmplConfigEOLastUpdateDate3 | LAST_UPDATE_DATE | — | ✅ |
| 8 | DasTmplConfigEOLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 9 | DasTmplConfigEOLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 10 | DasTmplConfigEOMetricCode | METRIC_CODE | — | — |
| 11 | DasTmplConfigEOMetricId | METRIC_ID | — | — |
| 12 | DasTmplConfigEOObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 13 | DasTmplConfigEORatingModelId | RATING_MODEL_ID | — | — |
| 14 | DasTmplConfigEOReadOnlyFlag | READ_ONLY_FLAG | — | — |
| 15 | DasTmplConfigEOUseAsAxisFlag | USE_AS_AXIS_FLAG | — | — |
| 16 | DasTmplConfigEOUseAsUnderlayFlag | USE_AS_UNDERLAY_FLAG | — | — |

### [[hrt_profiles_b|HRT_PROFILES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProfileBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ProfileBPEOCreatedBy | CREATED_BY | — | — |
| 3 | ProfileBPEOCreationDate | CREATION_DATE | — | — |
| 4 | ProfileBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ProfileBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ProfileBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ProfileBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | ProfileBPEOOwnerPersonId | OWNER_PERSON_ID | — | — |
| 9 | ProfileBPEOPartyId | PARTY_ID | — | — |
| 10 | ProfileBPEOPersonId | PERSON_ID | — | — |
| 11 | ProfileBPEOProfileCode | PROFILE_CODE | — | — |
| 12 | ProfileBPEOProfileId | PROFILE_ID | 🔑 | ✅ |
| 13 | ProfileBPEOProfileTypeId | PROFILE_TYPE_ID | — | — |
| 14 | ProfileBPEOProfileUsageCode | PROFILE_USAGE_CODE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
