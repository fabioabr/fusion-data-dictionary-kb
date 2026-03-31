---
id: DOC-OTHER-PVO-ReportedTimeEntryPVO
doc_type: system-doc
title: "ReportedTimeEntryPVO — PVO Cross-Module"
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
  - ReportedTimeEntryPVO
  - reportedtimeentrypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReportedTimeEntryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Reported Time Entry. Acessa as tabelas: HWM_RP_TM_PERIODS_VL, HWM_TM_APPROVED_TS_V, HWM_TM_A_APP_STATUS_PJC_V (+20).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeRepositoryAM.ReportedTimeEntryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 141 | 23 | 2 | 79 | 56% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_rp_tm_periods_vl|HWM_RP_TM_PERIODS_VL]] — 2 atributos (2 BICC)
- [[hwm_tm_approved_ts_v|HWM_TM_APPROVED_TS_V]] — 2 atributos (1 BICC)
- [[hwm_tm_a_app_status_pjc_v|HWM_TM_A_APP_STATUS_PJC_V]] — 2 atributos (1 BICC)
- [[hwm_tm_a_app_status_pyr_v|HWM_TM_A_APP_STATUS_PYR_V]] — 2 atributos (1 BICC)
- [[hwm_tm_a_te_completed_v|HWM_TM_A_TE_COMPLETED_V]] — 2 atributos
- [[hwm_tm_a_tr_err_status_v|HWM_TM_A_TR_ERR_STATUS_V]] — 2 atributos
- [[hwm_tm_a_user_status_v|HWM_TM_A_USER_STATUS_V]] — 2 atributos (1 BICC)
- [[hwm_tm_d_tm_ui_status_v|HWM_TM_D_TM_UI_STATUS_V]] — 2 atributos (1 BICC)
- [[hwm_tm_d_xfr_status_pjc_v|HWM_TM_D_XFR_STATUS_PJC_V]] — 1 atributos
- [[hwm_tm_d_xfr_status_pyr_v|HWM_TM_D_XFR_STATUS_PYR_V]] — 1 atributos
- [[hwm_tm_rec|HWM_TM_REC]] — 32 atributos (2 PKs, 20 BICC)
- [[hwm_tm_rec_grp|HWM_TM_REC_GRP]] — 54 atributos (33 BICC)
- [[hwm_tm_rep_m_comp_toil_atrbs_v|HWM_TM_REP_M_COMP_TOIL_ATRBS_V]] — 2 atributos
- [[hwm_tm_rep_m_pjc_doc_atrbs_v|HWM_TM_REP_M_PJC_DOC_ATRBS_V]] — 2 atributos (1 BICC)
- [[hwm_tm_rep_m_pjc_exp_atrbs_v|HWM_TM_REP_M_PJC_EXP_ATRBS_V]] — 2 atributos (1 BICC)
- [[hwm_tm_rep_m_ptt_atrbs_v|HWM_TM_REP_M_PTT_ATRBS_V]] — 2 atributos (1 BICC)
- [[hwm_tm_rep_s_hxt_atrbs_v|HWM_TM_REP_S_HXT_ATRBS_V]] — 4 atributos (2 BICC)
- [[hwm_tm_rep_s_pjc_atrbs_v|HWM_TM_REP_S_PJC_ATRBS_V]] — 7 atributos (5 BICC)
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
| 2 | RepeatingTmPeriodId | REPEATING_TM_PERIOD_ID | — | ✅ |

### [[hwm_tm_approved_ts_v|HWM_TM_APPROVED_TS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeCardApprovedStatusId | STATUS_ID | — | — |
| 2 | TimeCardApprovedTimestamp | APPROVED_TIMESTAMP | — | ✅ |

### [[hwm_tm_a_app_status_pjc_v|HWM_TM_A_APP_STATUS_PJC_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeEntryPjcAppStatusId | STATUS_ID | — | — |
| 2 | TimeEntryPjcAppStatusValue | STATUS_VALUE | — | ✅ |

### [[hwm_tm_a_app_status_pyr_v|HWM_TM_A_APP_STATUS_PYR_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeEntryPyrAppStatusId | STATUS_ID | — | — |
| 2 | TimeEntryPyrAppStatusValue | STATUS_VALUE | — | ✅ |

### [[hwm_tm_a_te_completed_v|HWM_TM_A_TE_COMPLETED_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeEntryCompletedStatusId | STATUS_ID | — | — |
| 2 | TimeEntryCompletedStatusValue | STATUS_VALUE | — | — |

### [[hwm_tm_a_tr_err_status_v|HWM_TM_A_TR_ERR_STATUS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeEntryErrorStatusId | STATUS_ID | — | — |
| 2 | TimeEntryErrorStatusValue | STATUS_VALUE | — | — |

### [[hwm_tm_a_user_status_v|HWM_TM_A_USER_STATUS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeCardUserStatusId | STATUS_ID | — | — |
| 2 | TimeCardUserStatusValue | STATUS_VALUE | — | ✅ |

### [[hwm_tm_d_tm_ui_status_v|HWM_TM_D_TM_UI_STATUS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeCardUIStatusId | STATUS_ID | — | — |
| 2 | TimeCardUIStatusValue | STATUS_VALUE | — | ✅ |

### [[hwm_tm_d_xfr_status_pjc_v|HWM_TM_D_XFR_STATUS_PJC_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeEntryReadyXfrPjcStatusId | STATUS_ID | — | — |

### [[hwm_tm_d_xfr_status_pyr_v|HWM_TM_D_XFR_STATUS_PYR_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeEntryReadyXfrPyrStatusId | STATUS_ID | — | — |

### [[hwm_tm_rec|HWM_TM_REC]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeEntryActivityEventTime | ACTIVITY_EVENT_TIME | — | — |
| 2 | TimeEntryActivityInId | ACTIVITY_IN_ID | — | — |
| 3 | TimeEntryActivityOutId | ACTIVITY_OUT_ID | — | — |
| 4 | TimeEntryActivityType | ACTIVITY_TYPE | — | — |
| 5 | TimeEntryCommentText | COMMENT_TEXT | — | ✅ |
| 6 | TimeEntryCreatedBy | CREATED_BY | — | ✅ |
| 7 | TimeEntryCreationDate | CREATION_DATE | — | ✅ |
| 8 | TimeEntryDataSetId | DATA_SET_ID | — | — |
| 9 | TimeEntryDateFrom | DATE_FROM | — | ✅ |
| 10 | TimeEntryDateTo | DATE_TO | — | ✅ |
| 11 | TimeEntryDeleteFlag | DELETE_FLAG | — | ✅ |
| 12 | TimeEntryEnterpriseId | ENTERPRISE_ID | — | — |
| 13 | TimeEntryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | TimeEntryLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | TimeEntryLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | TimeEntryLatestVersion | LATEST_VERSION | — | ✅ |
| 17 | TimeEntryLayerCode | LAYER_CODE | — | ✅ |
| 18 | TimeEntryMeasure | MEASURE | — | ✅ |
| 19 | TimeEntryOrderEntered | ORDER_ENTERED | — | — |
| 20 | TimeEntryResourceId | RESOURCE_ID | — | — |
| 21 | TimeEntryResourceType | RESOURCE_TYPE | — | — |
| 22 | TimeEntryStartTime | START_TIME | — | ✅ |
| 23 | TimeEntryStopTime | STOP_TIME | — | ✅ |
| 24 | TimeEntrySubresourceId | SUBRESOURCE_ID | — | — |
| 25 | TimeEntryTimeConsumerConfigurationSetId | TCSMR_CONFIG_SET_ID | — | — |
| 26 | TimeEntryTimeConsumerSetId | TCSMR_SET_ID | — | ✅ |
| 27 | TimeEntryTimeRecordId | TM_REC_ID | 🔑 | ✅ |
| 28 | TimeEntryTimeRecordType | TM_REC_TYPE | — | ✅ |
| 29 | TimeEntryTimeRecordVersion | TM_REC_VERSION | 🔑 | ✅ |
| 30 | TimeEntryTimeReporterId | TIME_REPORTER_ID | — | ✅ |
| 31 | TimeEntryUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 32 | TimeEntryUserStatus | USER_STATUS | — | — |

### [[hwm_tm_rec_grp|HWM_TM_REC_GRP]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DayCommentText | COMMENT_TEXT | — | ✅ |
| 2 | DayCommitTimestamp | COMMIT_TIMESTAMP | — | — |
| 3 | DayCreatedBy | CREATED_BY | — | ✅ |
| 4 | DayCreationDate | CREATION_DATE | — | ✅ |
| 5 | DayDataSetId | DATA_SET_ID | — | — |
| 6 | DayDateFrom | DATE_FROM | — | ✅ |
| 7 | DayDateTo | DATE_TO | — | ✅ |
| 8 | DayDeleteFlag | DELETE_FLAG | — | ✅ |
| 9 | DayEnterpriseId | ENTERPRISE_ID | — | — |
| 10 | DayGroupTypeId | GRP_TYPE_ID | — | ✅ |
| 11 | DayLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | DayLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | DayLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | DayLatestVersion | LATEST_VERSION | — | ✅ |
| 15 | DayLayerCode | LAYER_CODE | — | ✅ |
| 16 | DayOrderEntered | ORDER_ENTERED | — | — |
| 17 | DayResourceId | RESOURCE_ID | — | — |
| 18 | DayResourceType | RESOURCE_TYPE | — | — |
| 19 | DayStartTime | START_TIME | — | ✅ |
| 20 | DayStopTime | STOP_TIME | — | ✅ |
| 21 | DaySubresourceId | SUBRESOURCE_ID | — | — |
| 22 | DayTimeConsumerConfigurationSetId | TCSMR_CONFIG_SET_ID | — | — |
| 23 | DayTimeConsumerSetId | TCSMR_SET_ID | — | — |
| 24 | DayTimeRecordGroupId | TM_REC_GRP_ID | — | ✅ |
| 25 | DayTimeRecordGroupVersion | TM_REC_GRP_VERSION | — | ✅ |
| 26 | DayTimeReporterId | TIME_REPORTER_ID | — | — |
| 27 | DayUserStatus | USER_STATUS | — | — |
| 28 | TimeCardCommentText | COMMENT_TEXT | — | ✅ |
| 29 | TimeCardCommitTimestamp | COMMIT_TIMESTAMP | — | ✅ |
| 30 | TimeCardCreatedBy | CREATED_BY | — | ✅ |
| 31 | TimeCardCreationDate | CREATION_DATE | — | ✅ |
| 32 | TimeCardDataSetId | DATA_SET_ID | — | — |
| 33 | TimeCardDateFrom | DATE_FROM | — | ✅ |
| 34 | TimeCardDateTo | DATE_TO | — | ✅ |
| 35 | TimeCardDeleteFlag | DELETE_FLAG | — | ✅ |
| 36 | TimeCardEnterpriseId | ENTERPRISE_ID | — | — |
| 37 | TimeCardGroupTypeId | GRP_TYPE_ID | — | ✅ |
| 38 | TimeCardLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 39 | TimeCardLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 40 | TimeCardLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 41 | TimeCardLatestVersion | LATEST_VERSION | — | ✅ |
| 42 | TimeCardLayerCode | LAYER_CODE | — | ✅ |
| 43 | TimeCardOrderEntered | ORDER_ENTERED | — | — |
| 44 | TimeCardResourceId | RESOURCE_ID | — | — |
| 45 | TimeCardResourceType | RESOURCE_TYPE | — | — |
| 46 | TimeCardStartTime | START_TIME | — | ✅ |
| 47 | TimeCardStopTime | STOP_TIME | — | ✅ |
| 48 | TimeCardSubresourceId | SUBRESOURCE_ID | — | — |
| 49 | TimeCardTimeConsumerConfigurationSetId | TCSMR_CONFIG_SET_ID | — | — |
| 50 | TimeCardTimeConsumerSetId | TCSMR_SET_ID | — | — |
| 51 | TimeCardTimeRecordGroupId | TM_REC_GRP_ID | — | ✅ |
| 52 | TimeCardTimeRecordGroupVersion | TM_REC_GRP_VERSION | — | ✅ |
| 53 | TimeCardTimeReporterId | TIME_REPORTER_ID | — | — |
| 54 | TimeCardUserStatus | USER_STATUS | — | — |

### [[hwm_tm_rep_m_comp_toil_atrbs_v|HWM_TM_REP_M_COMP_TOIL_ATRBS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ToilReposAtrbId | TOIL_REPOS_ATRB_ID | — | — |
| 2 | ToilTimeType | TOIL_TIME_TYPE | — | — |

### [[hwm_tm_rep_m_pjc_doc_atrbs_v|HWM_TM_REP_M_PJC_DOC_ATRBS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjcDocTypeTimeRepositoryAttributeId | PJC_DOC_TIME_REPOS_ATRB_ID | — | — |
| 2 | PjcDocumentType | PJC_DOCUMENT_TYPE | — | ✅ |

### [[hwm_tm_rep_m_pjc_exp_atrbs_v|HWM_TM_REP_M_PJC_EXP_ATRBS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjcExpTypeTimeRepositoryAttributeId | PJC_EXP_TIME_REPOS_ATRB_ID | — | — |
| 2 | PjcExpenditureType | PJC_EXPENDITURE_TYPE | — | ✅ |

### [[hwm_tm_rep_m_ptt_atrbs_v|HWM_TM_REP_M_PTT_ATRBS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayPayrollTimeType | PAY_PAYROLL_TIME_TYPE | — | ✅ |
| 2 | PttTimeRepositoryAttributeId | PTT_TIME_REPOS_ATRB_ID | — | — |

### [[hwm_tm_rep_s_hxt_atrbs_v|HWM_TM_REP_S_HXT_ATRBS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HxtAttributeCategory | HXT_ATTRIBUTE_CATEGORY | — | — |
| 2 | HxtDay | HXT_DAY | — | ✅ |
| 3 | HxtResolvedPeriodId | HXT_RESOLVED_PERIOD_ID | — | ✅ |
| 4 | HxtTimeRepositoryAttributeId | HXT_TIME_REPOS_ATRB_ID | — | — |

### [[hwm_tm_rep_s_pjc_atrbs_v|HWM_TM_REP_S_PJC_ATRBS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjcAttributeCategory | PJC_ATTRIBUTE_CATEGORY | — | — |
| 2 | PjcBillableFlag | PJC_BILLABLE_FLAG | — | ✅ |
| 3 | PjcProjectId | PJC_PROJECT_ID | — | ✅ |
| 4 | PjcProjectUnit | PJC_PROJECT_UNIT | — | ✅ |
| 5 | PjcTaskId | PJC_TASK_ID | — | ✅ |
| 6 | PjcTimeRepositoryAttributeId | PJC_TIME_REPOS_ATRB_ID | — | — |
| 7 | PjcWorkType | PJC_WORK_TYPE | — | ✅ |

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

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
