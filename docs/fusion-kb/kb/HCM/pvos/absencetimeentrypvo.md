---
id: DOC-HCM-PVO-AbsenceTimeEntryPVO
doc_type: system-doc
title: "AbsenceTimeEntryPVO — PVO Human Capital Management"
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
  - AbsenceTimeEntryPVO
  - absencetimeentrypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AbsenceTimeEntryPVO

## 📌 Visão Geral

Integra lancamentos de tempo com registros de ausencia, incluindo periodos, status de aprovacao e duracao paga. Essencial para conciliacao entre time tracking e ausencias.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeRepositoryAM.AbsenceTimeEntryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 127 | 16 | 2 | 77 | 61% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_rp_tm_periods_vl|HWM_RP_TM_PERIODS_VL]] — 2 atributos (2 BICC)
- [[hwm_tm_abs_entry_v|HWM_TM_ABS_ENTRY_V]] — 84 atributos (2 PKs, 53 BICC)
- [[hwm_tm_approved_ts_v|HWM_TM_APPROVED_TS_V]] — 2 atributos (1 BICC)
- [[hwm_tm_a_anc_app_status_v|HWM_TM_A_ANC_APP_STATUS_V]] — 2 atributos (1 BICC)
- [[hwm_tm_a_user_status_v|HWM_TM_A_USER_STATUS_V]] — 2 atributos (1 BICC)
- [[hwm_tm_d_tm_ui_status_v|HWM_TM_D_TM_UI_STATUS_V]] — 2 atributos (1 BICC)
- [[hwm_tm_rec_grp|HWM_TM_REC_GRP]] — 3 atributos (3 BICC)
- [[hwm_tm_rep_m_anc_atrbs_v|HWM_TM_REP_M_ANC_ATRBS_V]] — 2 atributos (1 BICC)
- [[hwm_tm_rep_s_abs_hp_atrbs_v|HWM_TM_REP_S_ABS_HP_ATRBS_V]] — 4 atributos (2 BICC)
- [[hwm_tm_rep_s_abs_tep_atrbs_v|HWM_TM_REP_S_ABS_TEP_ATRBS_V]] — 2 atributos (1 BICC)
- [[hwm_tm_rep_s_hxt_atrbs_v|HWM_TM_REP_S_HXT_ATRBS_V]] — 4 atributos (2 BICC)
- [[hwm_tm_rep_s_sec_atrbs_v|HWM_TM_REP_S_SEC_ATRBS_V]] — 6 atributos (4 BICC)
- [[hwm_tm_submitted_ts_v|HWM_TM_SUBMITTED_TS_V]] — 2 atributos (1 BICC)
- [[hxt_tm_header|HXT_TM_HEADER]] — 2 atributos
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 4 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 4 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hwm_rp_tm_periods_vl|HWM_RP_TM_PERIODS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HxtResolvedPeriodMeaning | DESCRIPTION | — | ✅ |
| 2 | RepeatingTimePeriodId | REPEATING_TM_PERIOD_ID | — | ✅ |

### [[hwm_tm_abs_entry_v|HWM_TM_ABS_ENTRY_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DayCommentText | DAY_COMMENT_TEXT | — | ✅ |
| 2 | DayCommitTimestamp | DAY_COMMIT_TIMESTAMP | — | — |
| 3 | DayCreatedBy | DAY_CREATED_BY | — | ✅ |
| 4 | DayCreationDate | DAY_CREATION_DATE | — | ✅ |
| 5 | DayDataSetId | DAY_DATA_SET_ID | — | — |
| 6 | DayDateFrom | DAY_DATE_FROM | — | ✅ |
| 7 | DayDateTo | DAY_DATE_TO | — | ✅ |
| 8 | DayDeleteFlag | DAY_DELETE_FLAG | — | ✅ |
| 9 | DayEnterpriseId | DAY_ENTERPRISE_ID | — | — |
| 10 | DayGroupTypeId | DAY_GRP_TYPE_ID | — | ✅ |
| 11 | DayLastUpdateDate | DAY_LAST_UPDATE_DATE | — | ✅ |
| 12 | DayLastUpdateLogin | DAY_LAST_UPDATE_LOGIN | — | ✅ |
| 13 | DayLastUpdatedBy | DAY_LAST_UPDATED_BY | — | ✅ |
| 14 | DayLatestVersion | DAY_LATEST_VERSION | — | ✅ |
| 15 | DayLayerCode | DAY_LAYER_CODE | — | ✅ |
| 16 | DayOrderEntered | DAY_ORDER_ENTERED | — | — |
| 17 | DayResourceId | DAY_RESOURCE_ID | — | — |
| 18 | DayResourceType | DAY_RESOURCE_TYPE | — | — |
| 19 | DayStartTime | DAY_START_TIME | — | ✅ |
| 20 | DayStopTime | DAY_STOP_TIME | — | ✅ |
| 21 | DaySubresourceId | DAY_SUBRESOURCE_ID | — | — |
| 22 | DayTimeConsumerConfigurationSetId | DAY_TCSMR_CONFIG_SET_ID | — | — |
| 23 | DayTimeConsumerSetId | DAY_TCSMR_SET_ID | — | — |
| 24 | DayTimeRecordGroupId | DAY_TM_REC_GRP_ID | — | ✅ |
| 25 | DayTimeRecordGroupVersion | DAY_TM_REC_GRP_VERSION | — | ✅ |
| 26 | DayTimeReporterId | DAY_TIME_REPORTER_ID | — | — |
| 27 | DayUserStatus | DAY_USER_STATUS | — | — |
| 28 | TimeCardCommentText | TIME_CARD_COMMENT_TEXT | — | ✅ |
| 29 | TimeCardCommitTimestamp | TIME_CARD_COMMIT_TIMESTAMP | — | ✅ |
| 30 | TimeCardCreatedBy | TIME_CARD_CREATED_BY | — | ✅ |
| 31 | TimeCardCreationDate | TIME_CARD_CREATION_DATE | — | ✅ |
| 32 | TimeCardDataSetId | TIME_CARD_DATA_SET_ID | — | — |
| 33 | TimeCardDateFrom | TIME_CARD_DATE_FROM | — | ✅ |
| 34 | TimeCardDateTo | TIME_CARD_DATE_TO | — | ✅ |
| 35 | TimeCardDeleteFlag | TIME_CARD_DELETE_FLAG | — | ✅ |
| 36 | TimeCardEnterpriseId | TIME_CARD_ENTERPRISE_ID | — | — |
| 37 | TimeCardGroupTypeId | TIME_CARD_GRP_TYPE_ID | — | ✅ |
| 38 | TimeCardLastUpdateDate | TIME_CARD_LAST_UPDATE_DATE | — | ✅ |
| 39 | TimeCardLastUpdateLogin | TIME_CARD_LAST_UPDATE_LOGIN | — | ✅ |
| 40 | TimeCardLastUpdatedBy | TIME_CARD_LAST_UPDATED_BY | — | ✅ |
| 41 | TimeCardLatestVersion | TIME_CARD_LATEST_VERSION | — | ✅ |
| 42 | TimeCardLayerCode | TIME_CARD_LAYER_CODE | — | ✅ |
| 43 | TimeCardOrderEntered | TIME_CARD_ORDER_ENTERED | — | — |
| 44 | TimeCardResourceId | TIME_CARD_RESOURCE_ID | — | — |
| 45 | TimeCardResourceType | TIME_CARD_RESOURCE_TYPE | — | — |
| 46 | TimeCardStartTime | TIME_CARD_START_TIME | — | ✅ |
| 47 | TimeCardStopTime | TIME_CARD_STOP_TIME | — | ✅ |
| 48 | TimeCardSubresourceId | TIME_CARD_SUBRESOURCE_ID | — | — |
| 49 | TimeCardTimeConsumerConfigurationSetId | TIME_CARD_TCSMR_CONFIG_SET_ID | — | — |
| 50 | TimeCardTimeConsumerSetId | TIME_CARD_TCSMR_SET_ID | — | — |
| 51 | TimeCardTimeRecordGroupId | TIME_CARD_TM_REC_GRP_ID | — | ✅ |
| 52 | TimeCardTimeRecordGroupVersion | TIME_CARD_TM_REC_GRP_VERSION | — | ✅ |
| 53 | TimeCardTimeReporterId | TIME_CARD_TIME_REPORTER_ID | — | — |
| 54 | TimeCardUserStatus | TIME_CARD_USER_STATUS | — | — |
| 55 | TimeEntryActivityEventTime | TIME_ENTRY_ACTIVITY_EVENT_TIME | — | — |
| 56 | TimeEntryActivityType | TIME_ENTRY_ACTIVITY_TYPE | — | — |
| 57 | TimeEntryCommentText | TIME_ENTRY_COMMENT_TEXT | — | ✅ |
| 58 | TimeEntryCreatedBy | TIME_ENTRY_CREATED_BY | — | ✅ |
| 59 | TimeEntryCreationDate | TIME_ENTRY_CREATION_DATE | — | ✅ |
| 60 | TimeEntryDataSetId | TIME_ENTRY_DATA_SET_ID | — | — |
| 61 | TimeEntryDateFrom | TIME_ENTRY_DATE_FROM | — | ✅ |
| 62 | TimeEntryDateTo | TIME_ENTRY_DATE_TO | — | ✅ |
| 63 | TimeEntryDeleteFlag | TIME_ENTRY_DELETE_FLAG | — | ✅ |
| 64 | TimeEntryEnterpriseId | TIME_ENTRY_ENTERPRISE_ID | — | — |
| 65 | TimeEntryLastUpdateDate | TIME_ENTRY_LAST_UPDATE_DATE | — | ✅ |
| 66 | TimeEntryLastUpdateLogin | TIME_ENTRY_LAST_UPDATE_LOGIN | — | ✅ |
| 67 | TimeEntryLastUpdatedBy | TIME_ENTRY_LAST_UPDATED_BY | — | ✅ |
| 68 | TimeEntryLatestVersion | TIME_ENTRY_LATEST_VERSION | — | ✅ |
| 69 | TimeEntryLayerCode | TIME_ENTRY_LAYER_CODE | — | ✅ |
| 70 | TimeEntryMeasure | TIME_ENTRY_MEASURE | — | ✅ |
| 71 | TimeEntryOrderEntered | TIME_ENTRY_ORDER_ENTERED | — | — |
| 72 | TimeEntryResourceId | RESOURCE_ID | — | — |
| 73 | TimeEntryResourceType | TIME_ENTRY_RESOURCE_TYPE | — | — |
| 74 | TimeEntryStartTime | TIME_ENTRY_START_TIME | — | ✅ |
| 75 | TimeEntryStopTime | TIME_ENTRY_STOP_TIME | — | ✅ |
| 76 | TimeEntrySubresourceId | TIME_ENTRY_SUBRESOURCE_ID | — | — |
| 77 | TimeEntryTimeConsumerConfigurationSetId | TIME_ENTRY_TCSMR_CONFIG_SET_ID | — | — |
| 78 | TimeEntryTimeConsumerSetId | TIME_ENTRY_TCSMR_SET_ID | — | ✅ |
| 79 | TimeEntryTimeRecordId | TIME_ENTRY_TM_REC_ID | 🔑 | ✅ |
| 80 | TimeEntryTimeRecordType | TIME_ENTRY_TM_REC_TYPE | — | ✅ |
| 81 | TimeEntryTimeRecordVersion | TIME_ENTRY_TM_REC_VERSION | 🔑 | ✅ |
| 82 | TimeEntryTimeReporterId | TIME_ENTRY_TIME_REPORTER_ID | — | ✅ |
| 83 | TimeEntryUnitOfMeasure | TIME_ENTRY_UNIT_OF_MEASURE | — | ✅ |
| 84 | TimeEntryUserStatus | TIME_ENTRY_USER_STATUS | — | — |

### [[hwm_tm_approved_ts_v|HWM_TM_APPROVED_TS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeCardApprovedStatusId | STATUS_ID | — | — |
| 2 | TimeCardApprovedTimestamp | APPROVED_TIMESTAMP | — | ✅ |

### [[hwm_tm_a_anc_app_status_v|HWM_TM_A_ANC_APP_STATUS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimEntryAtomicAncAppStatusId | STATUS_ID | — | — |
| 2 | TimEntryAtomicAncAppStatusValue | STATUS_VALUE | — | ✅ |

### [[hwm_tm_a_user_status_v|HWM_TM_A_USER_STATUS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeCardAtomicUserStatusId | STATUS_ID | — | — |
| 2 | TimeCardAtomicUserStatusValue | STATUS_VALUE | — | ✅ |

### [[hwm_tm_d_tm_ui_status_v|HWM_TM_D_TM_UI_STATUS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeCardDerivedUIStatusId | STATUS_ID | — | — |
| 2 | TimeCardDerivedUIStatusValue | STATUS_VALUE | — | ✅ |

### [[hwm_tm_rec_grp|HWM_TM_REC_GRP]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AncHeaderGroupTypeId | GRP_TYPE_ID | — | ✅ |
| 2 | AncHeaderTimeRecordGroupId | TM_REC_GRP_ID | — | ✅ |
| 3 | AncHeaderTimeRecordGroupVersion | TM_REC_GRP_VERSION | — | ✅ |

### [[hwm_tm_rep_m_anc_atrbs_v|HWM_TM_REP_M_ANC_ATRBS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AncAbsenceType | ANC_ABSENCE_TYPE | — | ✅ |
| 2 | AncMasterTimeRepositoryAttributeId | ANC_MASTER_TIME_REPOS_ATRB_ID | — | — |

### [[hwm_tm_rep_s_abs_hp_atrbs_v|HWM_TM_REP_S_ABS_HP_ATRBS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AncAbsenceEntryId | ANC_ABSENCE_ENTRY_ID | — | ✅ |
| 2 | AncAttributeCategory | ANC_ATTRIBUTE_CATEGORY | — | — |
| 3 | AncEndOfBreakdown | ANC_END_OF_BREAKDOWN | — | ✅ |
| 4 | AncTimeRepositoryAttributeId | ANC_TIME_REPOS_ATRB_ID | — | — |

### [[hwm_tm_rep_s_abs_tep_atrbs_v|HWM_TM_REP_S_ABS_TEP_ATRBS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AncDurationPaid | ANC_DURATION_PAID | — | ✅ |
| 2 | AncSimpleTEPTimeRepositoryAttributeId | ANC_TIME_REPOS_ATRB_ID | — | — |

### [[hwm_tm_rep_s_hxt_atrbs_v|HWM_TM_REP_S_HXT_ATRBS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HxtAttributeCategory | HXT_ATTRIBUTE_CATEGORY | — | — |
| 2 | HxtDay | HXT_DAY | — | ✅ |
| 3 | HxtResolvedPeriodId | HXT_RESOLVED_PERIOD_ID | — | ✅ |
| 4 | HxtTimeRepositoryAttributeId | HXT_TIME_REPOS_ATRB_ID | — | — |

### [[hwm_tm_rep_s_sec_atrbs_v|HWM_TM_REP_S_SEC_ATRBS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SecAttributeCategory | SEC_ATTRIBUTE_CATEGORY | — | — |
| 2 | SecurityBusinessUnit | SECURITY_BUSINESS_UNIT | — | ✅ |
| 3 | SecurityEnterpriseId | SECURITY_ENTERPRISE_ID | — | ✅ |
| 4 | SecurityLegislativeDataGroup | SECURITY_LEG_DATA_GROUP | — | ✅ |
| 5 | SecurityOrganizationId | SECURITY_ORGANIZATION_ID | — | ✅ |
| 6 | SecurityTimeRepositoryAttributeId | SEC_TIME_REPOS_ATRB_ID | — | — |

### [[hwm_tm_submitted_ts_v|HWM_TM_SUBMITTED_TS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeCardSubmittedStatusId | STATUS_ID | — | — |
| 2 | TimeCardSubmittedTimestamp | SUBMITTED_TIMESTAMP | — | ✅ |

### [[hxt_tm_header|HXT_TM_HEADER]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimecardHeaderId | TM_HEADER_ID | — | — |
| 2 | TimecardLayoutSetId | TCLAYST_ID | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonDetailsPEOPersonId | PERSON_ID | — | — |
| 4 | PersonNumber | PERSON_NUMBER | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonName | FULL_NAME | — | ✅ |
| 2 | PersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | PersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
