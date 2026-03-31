---
id: DOC-OTHER-PVO-ScheduleDayPVO
doc_type: system-doc
title: "ScheduleDayPVO — PVO Cross-Module"
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
  - ScheduleDayPVO
  - scheduledaypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ScheduleDayPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Schedule Day. Acessa as tabelas: HTS_SCHEDULES_DAY_SHIFT_VIEW, HWM_TM_REC_GRP, HXT_SCH_PROF_DEFAULT_VIEW (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeRepositoryAM.ScheduleDayPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 84 | 4 | 2 | 26 | 31% |

---

## 🔗 Tabelas Relacionadas

- [[hts_schedules_day_shift_view|HTS_SCHEDULES_DAY_SHIFT_VIEW]] — 39 atributos (15 BICC)
- [[hwm_tm_rec_grp|HWM_TM_REC_GRP]] — 36 atributos (2 PKs, 9 BICC)
- [[hxt_sch_prof_default_view|HXT_SCH_PROF_DEFAULT_VIEW]] — 6 atributos (1 BICC)
- [[per_assignment_supervisors_f|PER_ASSIGNMENT_SUPERVISORS_F]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hts_schedules_day_shift_view|HTS_SCHEDULES_DAY_SHIFT_VIEW]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ScheduleDayShift1PEOParentTmRecGrpId | PARENT_TM_REC_GRP_ID | — | — |
| 2 | ScheduleDayShift1PEOParentTmRecGrpVersion | PARENT_TM_REC_GRP_VERSION | — | — |
| 3 | ScheduleDayShift1PEOShiftDateFrom | SHIFT_DATE_FROM | — | — |
| 4 | ScheduleDayShift1PEOShiftDateTo | SHIFT_DATE_TO | — | — |
| 5 | ScheduleDayShift1PEOShiftId | SHIFT_ID | — | — |
| 6 | ScheduleDayShift1PEOShiftName | SHIFT_NAME | — | ✅ |
| 7 | ScheduleDayShift1PEOShiftSequence | SHIFT_SEQUENCE | — | — |
| 8 | ScheduleDayShift1PEOShiftShortName | SHIFT_SHORT_NAME | — | ✅ |
| 9 | ScheduleDayShift1PEOShiftStartTime | SHIFT_START_TIME | — | ✅ |
| 10 | ScheduleDayShift1PEOShiftStopTime | SHIFT_STOP_TIME | — | ✅ |
| 11 | ScheduleDayShift1PEOShiftTmRecGrpId | SHIFT_TM_REC_GRP_ID | — | — |
| 12 | ScheduleDayShift1PEOShiftTmRecGrpVersion | SHIFT_TM_REC_GRP_VERSION | — | — |
| 13 | ScheduleDayShift1PEOShiftTypeCode | SHIFT_TYPE_CODE | — | ✅ |
| 14 | ScheduleDayShift2PEOParentTmRecGrpId | PARENT_TM_REC_GRP_ID | — | — |
| 15 | ScheduleDayShift2PEOParentTmRecGrpVersion | PARENT_TM_REC_GRP_VERSION | — | — |
| 16 | ScheduleDayShift2PEOShiftDateFrom | SHIFT_DATE_FROM | — | — |
| 17 | ScheduleDayShift2PEOShiftDateTo | SHIFT_DATE_TO | — | — |
| 18 | ScheduleDayShift2PEOShiftId | SHIFT_ID | — | — |
| 19 | ScheduleDayShift2PEOShiftName | SHIFT_NAME | — | ✅ |
| 20 | ScheduleDayShift2PEOShiftSequence | SHIFT_SEQUENCE | — | — |
| 21 | ScheduleDayShift2PEOShiftShortName | SHIFT_SHORT_NAME | — | ✅ |
| 22 | ScheduleDayShift2PEOShiftStartTime | SHIFT_START_TIME | — | ✅ |
| 23 | ScheduleDayShift2PEOShiftStopTime | SHIFT_STOP_TIME | — | ✅ |
| 24 | ScheduleDayShift2PEOShiftTmRecGrpId | SHIFT_TM_REC_GRP_ID | — | — |
| 25 | ScheduleDayShift2PEOShiftTmRecGrpVersion | SHIFT_TM_REC_GRP_VERSION | — | — |
| 26 | ScheduleDayShift2PEOShiftTypeCode | SHIFT_TYPE_CODE | — | ✅ |
| 27 | ScheduleDayShift3PEOParentTmRecGrpId | PARENT_TM_REC_GRP_ID | — | — |
| 28 | ScheduleDayShift3PEOParentTmRecGrpVersion | PARENT_TM_REC_GRP_VERSION | — | — |
| 29 | ScheduleDayShift3PEOShiftDateFrom | SHIFT_DATE_FROM | — | — |
| 30 | ScheduleDayShift3PEOShiftDateTo | SHIFT_DATE_TO | — | — |
| 31 | ScheduleDayShift3PEOShiftId | SHIFT_ID | — | — |
| 32 | ScheduleDayShift3PEOShiftName | SHIFT_NAME | — | ✅ |
| 33 | ScheduleDayShift3PEOShiftSequence | SHIFT_SEQUENCE | — | — |
| 34 | ScheduleDayShift3PEOShiftShortName | SHIFT_SHORT_NAME | — | ✅ |
| 35 | ScheduleDayShift3PEOShiftStartTime | SHIFT_START_TIME | — | ✅ |
| 36 | ScheduleDayShift3PEOShiftStopTime | SHIFT_STOP_TIME | — | ✅ |
| 37 | ScheduleDayShift3PEOShiftTmRecGrpId | SHIFT_TM_REC_GRP_ID | — | — |
| 38 | ScheduleDayShift3PEOShiftTmRecGrpVersion | SHIFT_TM_REC_GRP_VERSION | — | — |
| 39 | ScheduleDayShift3PEOShiftTypeCode | SHIFT_TYPE_CODE | — | ✅ |

### [[hwm_tm_rec_grp|HWM_TM_REC_GRP]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DayTimeRecordGroupPEOCommentText | COMMENT_TEXT | — | — |
| 2 | DayTimeRecordGroupPEOCommitTimestamp | COMMIT_TIMESTAMP | — | — |
| 3 | DayTimeRecordGroupPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | DayTimeRecordGroupPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | DayTimeRecordGroupPEODataSetId | DATA_SET_ID | — | — |
| 6 | DayTimeRecordGroupPEODateFrom | DATE_FROM | — | — |
| 7 | DayTimeRecordGroupPEODateTo | DATE_TO | — | — |
| 8 | DayTimeRecordGroupPEODeleteFlag | DELETE_FLAG | — | — |
| 9 | DayTimeRecordGroupPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 10 | DayTimeRecordGroupPEOGroupTypeId | GRP_TYPE_ID | — | — |
| 11 | DayTimeRecordGroupPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | DayTimeRecordGroupPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | DayTimeRecordGroupPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | DayTimeRecordGroupPEOLatestVersion | LATEST_VERSION | — | — |
| 15 | DayTimeRecordGroupPEOLayerCode | LAYER_CODE | — | — |
| 16 | DayTimeRecordGroupPEOLayerTimeRecordGroupId | LAYER_TM_REC_GRP_ID | — | — |
| 17 | DayTimeRecordGroupPEOLayerTimeRecordGroupVersion | LAYER_TM_REC_GRP_VERSION | — | — |
| 18 | DayTimeRecordGroupPEOMeasure | MEASURE | — | — |
| 19 | DayTimeRecordGroupPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | DayTimeRecordGroupPEOOrderEntered | ORDER_ENTERED | — | — |
| 21 | DayTimeRecordGroupPEOOriginalTimeRecordGroupId | ORIG_TM_REC_GRP_ID | — | — |
| 22 | DayTimeRecordGroupPEOOriginalTimeRecordGroupVersion | ORIG_TM_REC_GRP_VERSION | — | — |
| 23 | DayTimeRecordGroupPEOParentTimeRecordGroupId | PARENT_TM_REC_GRP_ID | — | — |
| 24 | DayTimeRecordGroupPEOParentTimeRecordGroupVersion | PARENT_TM_REC_GRP_VERSION | — | — |
| 25 | DayTimeRecordGroupPEOResourceId | RESOURCE_ID | — | — |
| 26 | DayTimeRecordGroupPEOResourceType | RESOURCE_TYPE | — | — |
| 27 | DayTimeRecordGroupPEOStartTime | START_TIME | — | ✅ |
| 28 | DayTimeRecordGroupPEOStopTime | STOP_TIME | — | ✅ |
| 29 | DayTimeRecordGroupPEOSubresourceId | SUBRESOURCE_ID | — | — |
| 30 | DayTimeRecordGroupPEOTimeConsumerConfigurationSetId | TCSMR_CONFIG_SET_ID | — | — |
| 31 | DayTimeRecordGroupPEOTimeConsumerSetId | TCSMR_SET_ID | — | — |
| 32 | DayTimeRecordGroupPEOTimeRecordGroupId | TM_REC_GRP_ID | 🔑 | ✅ |
| 33 | DayTimeRecordGroupPEOTimeRecordGroupVersion | TM_REC_GRP_VERSION | 🔑 | ✅ |
| 34 | DayTimeRecordGroupPEOTimeReporterId | TIME_REPORTER_ID | — | — |
| 35 | DayTimeRecordGroupPEOUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 36 | DayTimeRecordGroupPEOUserStatus | USER_STATUS | — | — |

### [[hxt_sch_prof_default_view|HXT_SCH_PROF_DEFAULT_VIEW]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BISchedulerProfileOptionPEOCreationDate1 | CREATION_DATE1 | — | — |
| 2 | BISchedulerProfileOptionPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | BISchedulerProfileOptionPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | BISchedulerProfileOptionPEOInclMemberId | INCL_MEMBER_ID | — | — |
| 5 | BISchedulerProfileOptionPEOSetupOptionValId | SETUP_OPTION_VAL_ID | — | — |
| 6 | BISchedulerProfileOptionPEOSetupProfileAsgId | SETUP_PROFILE_ASG_ID | — | — |

### [[per_assignment_supervisors_f|PER_ASSIGNMENT_SUPERVISORS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentSupervisorId | ASSIGNMENT_SUPERVISOR_ID | — | — |
| 2 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
