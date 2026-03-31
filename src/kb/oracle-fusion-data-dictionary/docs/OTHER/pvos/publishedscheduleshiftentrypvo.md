---
id: DOC-OTHER-PVO-PublishedScheduleShiftEntryPVO
doc_type: system-doc
title: "PublishedScheduleShiftEntryPVO — PVO Cross-Module"
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
  - PublishedScheduleShiftEntryPVO
  - publishedscheduleshiftentrypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PublishedScheduleShiftEntryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Published Schedule Shift Entry. Acessa as tabelas: HTS_SCHEDULES_ATRBS_VIEW, HTS_SCHEDULES_DAY_SHIFT_VIEW, HWM_TM_REC (+4).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeRepositoryAM.PublishedScheduleShiftEntryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 166 | 7 | 7 | 66 | 40% |

---

## 🔗 Tabelas Relacionadas

- [[hts_schedules_atrbs_view|HTS_SCHEDULES_ATRBS_VIEW]] — 9 atributos (4 BICC)
- [[hts_schedules_day_shift_view|HTS_SCHEDULES_DAY_SHIFT_VIEW]] — 39 atributos (15 BICC)
- [[hwm_tm_rec|HWM_TM_REC]] — 24 atributos (2 PKs, 11 BICC)
- [[hwm_tm_rec_grp|HWM_TM_REC_GRP]] — 75 atributos (28 BICC)
- [[hwm_tm_rep_s_common_atrbs_v|HWM_TM_REP_S_COMMON_ATRBS_V]] — 3 atributos (1 BICC)
- [[hxt_sch_prof_default_view|HXT_SCH_PROF_DEFAULT_VIEW]] — 10 atributos (5 PKs, 5 BICC)
- [[per_assignment_supervisors_f|PER_ASSIGNMENT_SUPERVISORS_F]] — 6 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hts_schedules_atrbs_view|HTS_SCHEDULES_ATRBS_VIEW]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | — | — |
| 2 | ShiftColour | SHIFT_COLOUR | — | — |
| 3 | ShiftId | SHIFT_ID | — | — |
| 4 | ShiftName | SHIFT_NAME | — | ✅ |
| 5 | ShiftShortName | SHIFT_SHORT_NAME | — | ✅ |
| 6 | ShiftTimeNotWorked | TIME_NOT_WORKED | — | ✅ |
| 7 | ShiftTypeCode | SHIFT_TYPE_CODE | — | ✅ |
| 8 | ShortTxt | SHORT_TXT | — | — |
| 9 | UsagesSourceId | USAGES_SOURCE_ID | — | — |

### [[hts_schedules_day_shift_view|HTS_SCHEDULES_DAY_SHIFT_VIEW]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ScheduleDayShift1PEOParentTmRecGrpId | PARENT_TM_REC_GRP_ID | — | — |
| 2 | ScheduleDayShift1PEOParentTmRecGrpVersion | PARENT_TM_REC_GRP_VERSION | — | — |
| 3 | ScheduleDayShift1PEOShiftDateFrom | SHIFT_DATE_FROM | — | — |
| 4 | ScheduleDayShift1PEOShiftDateTo | SHIFT_DATE_TO | — | — |
| 5 | ScheduleDayShift1PEOShiftId1 | SHIFT_ID | — | — |
| 6 | ScheduleDayShift1PEOShiftName1 | SHIFT_NAME | — | ✅ |
| 7 | ScheduleDayShift1PEOShiftSequence | SHIFT_SEQUENCE | — | — |
| 8 | ScheduleDayShift1PEOShiftShortName1 | SHIFT_SHORT_NAME | — | ✅ |
| 9 | ScheduleDayShift1PEOShiftStartTime | SHIFT_START_TIME | — | ✅ |
| 10 | ScheduleDayShift1PEOShiftStopTime | SHIFT_STOP_TIME | — | ✅ |
| 11 | ScheduleDayShift1PEOShiftTmRecGrpId | SHIFT_TM_REC_GRP_ID | — | — |
| 12 | ScheduleDayShift1PEOShiftTmRecGrpVersion | SHIFT_TM_REC_GRP_VERSION | — | — |
| 13 | ScheduleDayShift1PEOShiftTypeCode1 | SHIFT_TYPE_CODE | — | ✅ |
| 14 | ScheduleDayShift2PEOParentTmRecGrpId | PARENT_TM_REC_GRP_ID | — | — |
| 15 | ScheduleDayShift2PEOParentTmRecGrpVersion | PARENT_TM_REC_GRP_VERSION | — | — |
| 16 | ScheduleDayShift2PEOShiftDateFrom | SHIFT_DATE_FROM | — | — |
| 17 | ScheduleDayShift2PEOShiftDateTo | SHIFT_DATE_TO | — | — |
| 18 | ScheduleDayShift2PEOShiftId1 | SHIFT_ID | — | — |
| 19 | ScheduleDayShift2PEOShiftName1 | SHIFT_NAME | — | ✅ |
| 20 | ScheduleDayShift2PEOShiftSequence | SHIFT_SEQUENCE | — | — |
| 21 | ScheduleDayShift2PEOShiftShortName1 | SHIFT_SHORT_NAME | — | ✅ |
| 22 | ScheduleDayShift2PEOShiftStartTime | SHIFT_START_TIME | — | ✅ |
| 23 | ScheduleDayShift2PEOShiftStopTime | SHIFT_STOP_TIME | — | ✅ |
| 24 | ScheduleDayShift2PEOShiftTmRecGrpId | SHIFT_TM_REC_GRP_ID | — | — |
| 25 | ScheduleDayShift2PEOShiftTmRecGrpVersion | SHIFT_TM_REC_GRP_VERSION | — | — |
| 26 | ScheduleDayShift2PEOShiftTypeCode1 | SHIFT_TYPE_CODE | — | ✅ |
| 27 | ScheduleDayShift3PEOParentTmRecGrpId | PARENT_TM_REC_GRP_ID | — | — |
| 28 | ScheduleDayShift3PEOParentTmRecGrpVersion | PARENT_TM_REC_GRP_VERSION | — | — |
| 29 | ScheduleDayShift3PEOShiftDateFrom | SHIFT_DATE_FROM | — | — |
| 30 | ScheduleDayShift3PEOShiftDateTo | SHIFT_DATE_TO | — | — |
| 31 | ScheduleDayShift3PEOShiftId1 | SHIFT_ID | — | — |
| 32 | ScheduleDayShift3PEOShiftName1 | SHIFT_NAME | — | ✅ |
| 33 | ScheduleDayShift3PEOShiftSequence | SHIFT_SEQUENCE | — | — |
| 34 | ScheduleDayShift3PEOShiftShortName1 | SHIFT_SHORT_NAME | — | ✅ |
| 35 | ScheduleDayShift3PEOShiftStartTime | SHIFT_START_TIME | — | ✅ |
| 36 | ScheduleDayShift3PEOShiftStopTime | SHIFT_STOP_TIME | — | ✅ |
| 37 | ScheduleDayShift3PEOShiftTmRecGrpId | SHIFT_TM_REC_GRP_ID | — | — |
| 38 | ScheduleDayShift3PEOShiftTmRecGrpVersion | SHIFT_TM_REC_GRP_VERSION | — | — |
| 39 | ScheduleDayShift3PEOShiftTypeCode1 | SHIFT_TYPE_CODE | — | ✅ |

### [[hwm_tm_rec|HWM_TM_REC]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | entryCommentText | COMMENT_TEXT | — | — |
| 2 | entryCreatedBy | CREATED_BY | — | ✅ |
| 3 | entryCreationDate | CREATION_DATE | — | ✅ |
| 4 | entryDateFrom | DATE_FROM | — | — |
| 5 | entryDateTo | DATE_TO | — | — |
| 6 | entryDeleteFlag | DELETE_FLAG | — | — |
| 7 | entryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | entryLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | entryLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | entryLatestVersion | LATEST_VERSION | — | — |
| 11 | entryLayerCode | LAYER_CODE | — | — |
| 12 | entryMeasure | MEASURE | — | ✅ |
| 13 | entryResourceId | RESOURCE_ID | — | ✅ |
| 14 | entryResourceType | RESOURCE_TYPE | — | — |
| 15 | entryStartTime | START_TIME | — | ✅ |
| 16 | entryStopTime | STOP_TIME | — | ✅ |
| 17 | entrySubresourceId | SUBRESOURCE_ID | — | — |
| 18 | entryTcsmrConfigSetId | TCSMR_CONFIG_SET_ID | — | — |
| 19 | entryTcsmrSetId | TCSMR_SET_ID | — | — |
| 20 | entryTimeReporterId | TIME_REPORTER_ID | — | — |
| 21 | entryTmRecId | TM_REC_ID | 🔑 | ✅ |
| 22 | entryTmRecType | TM_REC_TYPE | — | — |
| 23 | entryTmRecVersion | TM_REC_VERSION | 🔑 | ✅ |
| 24 | entryUnitOfMeasure | UNIT_OF_MEASURE | — | — |

### [[hwm_tm_rec_grp|HWM_TM_REC_GRP]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | dayCommentText | COMMENT_TEXT | — | — |
| 2 | dayCommitTimestamp | COMMIT_TIMESTAMP | — | — |
| 3 | dayCreatedBy | CREATED_BY | — | ✅ |
| 4 | dayCreationDate | CREATION_DATE | — | ✅ |
| 5 | dayDateFrom | DATE_FROM | — | — |
| 6 | dayDateTo | DATE_TO | — | — |
| 7 | dayDeleteFlag | DELETE_FLAG | — | — |
| 8 | dayGroupTypeId | GRP_TYPE_ID | — | — |
| 9 | dayLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | dayLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | dayLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | dayLatestVersion | LATEST_VERSION | — | — |
| 13 | dayLayerCode | LAYER_CODE | — | — |
| 14 | dayParentTmRecGrpId | PARENT_TM_REC_GRP_ID | — | — |
| 15 | dayParentTmRecGrpVersion | PARENT_TM_REC_GRP_VERSION | — | — |
| 16 | dayResourceId | RESOURCE_ID | — | — |
| 17 | dayResourceType | RESOURCE_TYPE | — | — |
| 18 | dayStartTime | START_TIME | — | ✅ |
| 19 | dayStopTime | STOP_TIME | — | ✅ |
| 20 | daySubresourceId | SUBRESOURCE_ID | — | — |
| 21 | dayTcsmrConfigSetId | TCSMR_CONFIG_SET_ID | — | — |
| 22 | dayTcsmrSetId | TCSMR_SET_ID | — | — |
| 23 | dayTimeReporterId | TIME_REPORTER_ID | — | — |
| 24 | dayTmRecGrpId | TM_REC_GRP_ID | — | ✅ |
| 25 | dayTmRecGrpVersion | TM_REC_GRP_VERSION | — | ✅ |
| 26 | periodCommentText | COMMENT_TEXT | — | — |
| 27 | periodCommitTimestamp | COMMIT_TIMESTAMP | — | ✅ |
| 28 | periodCreatedBy | CREATED_BY | — | ✅ |
| 29 | periodCreationDate | CREATION_DATE | — | ✅ |
| 30 | periodDateFrom | DATE_FROM | — | — |
| 31 | periodDateTo | DATE_TO | — | — |
| 32 | periodDeleteFlag | DELETE_FLAG | — | — |
| 33 | periodGroupTypeId | GRP_TYPE_ID | — | — |
| 34 | periodLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 35 | periodLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 36 | periodLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 37 | periodLatestVersion | LATEST_VERSION | — | — |
| 38 | periodLayerCode | LAYER_CODE | — | — |
| 39 | periodParentTmRecGrpId | PARENT_TM_REC_GRP_ID | — | — |
| 40 | periodParentTmRecGrpVersion | PARENT_TM_REC_GRP_VERSION | — | — |
| 41 | periodResourceId | RESOURCE_ID | — | — |
| 42 | periodResourceType | RESOURCE_TYPE | — | — |
| 43 | periodStartTime | START_TIME | — | ✅ |
| 44 | periodStopTime | STOP_TIME | — | ✅ |
| 45 | periodSubresourceId | SUBRESOURCE_ID | — | — |
| 46 | periodTcsmrConfigSetId | TCSMR_CONFIG_SET_ID | — | — |
| 47 | periodTcsmrSetId | TCSMR_SET_ID | — | — |
| 48 | periodTimeReporterId | TIME_REPORTER_ID | — | — |
| 49 | periodTmRecGrpId | TM_REC_GRP_ID | — | ✅ |
| 50 | periodTmRecGrpVersion | TM_REC_GRP_VERSION | — | ✅ |
| 51 | shiftCommentText | COMMENT_TEXT | — | — |
| 52 | shiftCommitTimestamp | COMMIT_TIMESTAMP | — | — |
| 53 | shiftCreatedBy | CREATED_BY | — | ✅ |
| 54 | shiftCreationDate | CREATION_DATE | — | ✅ |
| 55 | shiftDateFrom | DATE_FROM | — | — |
| 56 | shiftDateTo | DATE_TO | — | — |
| 57 | shiftDeleteFlag | DELETE_FLAG | — | — |
| 58 | shiftGroupTypeId | GRP_TYPE_ID | — | — |
| 59 | shiftLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 60 | shiftLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 61 | shiftLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 62 | shiftLatestVersion | LATEST_VERSION | — | — |
| 63 | shiftLayerCode | LAYER_CODE | — | — |
| 64 | shiftParentTmRecGrpId | PARENT_TM_REC_GRP_ID | — | — |
| 65 | shiftParentTmRecGrpVersion | PARENT_TM_REC_GRP_VERSION | — | — |
| 66 | shiftResourceId | RESOURCE_ID | — | — |
| 67 | shiftResourceType | RESOURCE_TYPE | — | — |
| 68 | shiftStartTime | START_TIME | — | ✅ |
| 69 | shiftStopTime | STOP_TIME | — | ✅ |
| 70 | shiftSubresourceId | SUBRESOURCE_ID | — | — |
| 71 | shiftTcsmrConfigSetId | TCSMR_CONFIG_SET_ID | — | — |
| 72 | shiftTcsmrSetId | TCSMR_SET_ID | — | — |
| 73 | shiftTimeReporterId | TIME_REPORTER_ID | — | — |
| 74 | shiftTmRecGrpId | TM_REC_GRP_ID | — | ✅ |
| 75 | shiftTmRecGrpVersion | TM_REC_GRP_VERSION | — | ✅ |

### [[hwm_tm_rep_s_common_atrbs_v|HWM_TM_REP_S_COMMON_ATRBS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CommonTimeReposAtrbId | COMMON_TIME_REPOS_ATRB_ID | — | — |
| 2 | SimpleCommonAttributePEOCommonInternalSource | COMMON_INTERNAL_SOURCE | — | — |
| 3 | SimpleCommonAttributePEOCommonOwner | COMMON_OWNER | — | ✅ |

### [[hxt_sch_prof_default_view|HXT_SCH_PROF_DEFAULT_VIEW]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GrpInclMemberId | GRP_INCL_MEMBER_ID | — | — |
| 2 | InclMemberId | INCL_MEMBER_ID | — | — |
| 3 | ProductArea | PRODUCT_AREA | — | — |
| 4 | SetupOptionCreationDate | CREATION_DATE1 | — | — |
| 5 | SetupOptionEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 6 | SetupOptionEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 7 | SetupOptionValId | SETUP_OPTION_VAL_ID | 🔑 | ✅ |
| 8 | SetupProfileAsgAssignTo | ASSIGN_TO | — | — |
| 9 | SetupProfileAsgId | SETUP_PROFILE_ASG_ID | 🔑 | ✅ |
| 10 | SetupProfileId | SETUP_PROFILE_ID | 🔑 | ✅ |

### [[per_assignment_supervisors_f|PER_ASSIGNMENT_SUPERVISORS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentSupervisorId | ASSIGNMENT_SUPERVISOR_ID | — | — |
| 2 | ManagerId | MANAGER_ID | — | ✅ |
| 3 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | PersonId | PERSON_ID | — | — |
| 5 | mgrEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | mgrEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
