---
id: DOC-OTHER-PVO-HistoricProcessedTimeEntryPVO
doc_type: system-doc
title: "HistoricProcessedTimeEntryPVO — PVO Cross-Module"
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
  - HistoricProcessedTimeEntryPVO
  - historicprocessedtimeentrypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HistoricProcessedTimeEntryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Historic Processed Time Entry. Acessa as tabelas: HWM_TE_VERSION_STATUS_V, HWM_TM_A_XFR_STATUS_PJC_V, HWM_TM_A_XFR_STATUS_PYR_V (+15).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeRepositoryAM.HistoricProcessedTimeEntryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 148 | 18 | 2 | 79 | 53% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_te_version_status_v|HWM_TE_VERSION_STATUS_V]] — 6 atributos
- [[hwm_tm_a_xfr_status_pjc_v|HWM_TM_A_XFR_STATUS_PJC_V]] — 2 atributos (1 BICC)
- [[hwm_tm_a_xfr_status_pyr_v|HWM_TM_A_XFR_STATUS_PYR_V]] — 2 atributos (1 BICC)
- [[hwm_tm_d_xfr_status_pjc_v|HWM_TM_D_XFR_STATUS_PJC_V]] — 1 atributos
- [[hwm_tm_d_xfr_status_pyr_v|HWM_TM_D_XFR_STATUS_PYR_V]] — 1 atributos
- [[hwm_tm_rec|HWM_TM_REC]] — 35 atributos (2 PKs, 24 BICC)
- [[hwm_tm_rec_grp|HWM_TM_REC_GRP]] — 58 atributos (37 BICC)
- [[hwm_tm_rep_m_comp_toil_atrbs_v|HWM_TM_REP_M_COMP_TOIL_ATRBS_V]] — 2 atributos
- [[hwm_tm_rep_m_pjc_doc_atrbs_v|HWM_TM_REP_M_PJC_DOC_ATRBS_V]] — 2 atributos (1 BICC)
- [[hwm_tm_rep_m_pjc_exp_atrbs_v|HWM_TM_REP_M_PJC_EXP_ATRBS_V]] — 2 atributos (1 BICC)
- [[hwm_tm_rep_m_ptt_atrbs_v|HWM_TM_REP_M_PTT_ATRBS_V]] — 2 atributos (1 BICC)
- [[hwm_tm_rep_s_hxt_atrbs_v|HWM_TM_REP_S_HXT_ATRBS_V]] — 4 atributos
- [[hwm_tm_rep_s_pjc_atrbs_v|HWM_TM_REP_S_PJC_ATRBS_V]] — 7 atributos (5 BICC)
- [[hwm_tm_rep_s_sec_atrbs_v|HWM_TM_REP_S_SEC_ATRBS_V]] — 6 atributos (4 BICC)
- [[hwm_tm_statuses|HWM_TM_STATUSES]] — 8 atributos
- [[hxt_tm_header|HXT_TM_HEADER]] — 2 atributos
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 4 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 4 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hwm_te_version_status_v|HWM_TE_VERSION_STATUS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeEntryVersionStatusPEOMaxAXfrStatusPjcId | MAX_A_XFR_STATUS_PJC_ID | — | — |
| 2 | TimeEntryVersionStatusPEOMaxAXfrStatusPyrId | MAX_A_XFR_STATUS_PYR_ID | — | — |
| 3 | TimeEntryVersionStatusPEOMaxDReadyXfrStatusPjcId | MAX_D_READY_XFR_STATUS_PJC_ID | — | — |
| 4 | TimeEntryVersionStatusPEOMaxDReadyXfrStatusPyrId | MAX_D_READY_XFR_STATUS_PYR_ID | — | — |
| 5 | TimeEntryVersionStatusPEOTmBldgBlkId | TM_BLDG_BLK_ID | — | — |
| 6 | TimeEntryVersionStatusPEOTmBldgBlkVersion | TM_BLDG_BLK_VERSION | — | — |

### [[hwm_tm_a_xfr_status_pjc_v|HWM_TM_A_XFR_STATUS_PJC_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeEnryPjcXfrStatusId | STATUS_ID | — | — |
| 2 | TimeEnryPjcXfrStatusValue | STATUS_VALUE | — | ✅ |

### [[hwm_tm_a_xfr_status_pyr_v|HWM_TM_A_XFR_STATUS_PYR_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeEntryPyrXfrStatusId | STATUS_ID | — | — |
| 2 | TimeEntryPyrXfrStatusValue | STATUS_VALUE | — | ✅ |

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
| 2 | TimeEntryActivityType | ACTIVITY_TYPE | — | — |
| 3 | TimeEntryCommentText | COMMENT_TEXT | — | ✅ |
| 4 | TimeEntryCreatedBy | CREATED_BY | — | ✅ |
| 5 | TimeEntryCreationDate | CREATION_DATE | — | ✅ |
| 6 | TimeEntryDataSetId | DATA_SET_ID | — | — |
| 7 | TimeEntryDateFrom | DATE_FROM | — | ✅ |
| 8 | TimeEntryDateTo | DATE_TO | — | ✅ |
| 9 | TimeEntryDeleteFlag | DELETE_FLAG | — | ✅ |
| 10 | TimeEntryEnterpriseId | ENTERPRISE_ID | — | — |
| 11 | TimeEntryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | TimeEntryLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | TimeEntryLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | TimeEntryLatestVersion | LATEST_VERSION | — | ✅ |
| 15 | TimeEntryLayerCode | LAYER_CODE | — | ✅ |
| 16 | TimeEntryMeasure | MEASURE | — | ✅ |
| 17 | TimeEntryOrderEntered | ORDER_ENTERED | — | — |
| 18 | TimeEntryOriginalTimeRecordId | ORIG_TM_REC_ID | — | ✅ |
| 19 | TimeEntryOriginalTimeRecordVersion | ORIG_TM_REC_VERSION | — | ✅ |
| 20 | TimeEntryResourceId | RESOURCE_ID | — | — |
| 21 | TimeEntryResourceType | RESOURCE_TYPE | — | — |
| 22 | TimeEntryStartTime | START_TIME | — | ✅ |
| 23 | TimeEntryStopTime | STOP_TIME | — | ✅ |
| 24 | TimeEntrySubresourceId | SUBRESOURCE_ID | — | — |
| 25 | TimeEntryTimeConsumerConfigurationSetId | TCSMR_CONFIG_SET_ID | — | — |
| 26 | TimeEntryTimeConsumerSetId | TCSMR_SET_ID | — | ✅ |
| 27 | TimeEntryTimeRecordId | TM_REC_ID | 🔑 | ✅ |
| 28 | TimeEntryTimeRecordPEOActualDate | ACTUAL_DATE | — | ✅ |
| 29 | TimeEntryTimeRecordPEORefDate | REF_DATE | — | ✅ |
| 30 | TimeEntryTimeRecordRowId | TM_REC_ROW_ID | — | — |
| 31 | TimeEntryTimeRecordType | TM_REC_TYPE | — | ✅ |
| 32 | TimeEntryTimeRecordVersion | TM_REC_VERSION | 🔑 | ✅ |
| 33 | TimeEntryTimeReporterId | TIME_REPORTER_ID | — | ✅ |
| 34 | TimeEntryUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 35 | TimeEntryUserStatus | USER_STATUS | — | — |

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
| 17 | DayOriginalTimeRecordGroupId | ORIG_TM_REC_GRP_ID | — | ✅ |
| 18 | DayOriginalTimeRecordGroupVersion | ORIG_TM_REC_GRP_VERSION | — | ✅ |
| 19 | DayResourceId | RESOURCE_ID | — | — |
| 20 | DayResourceType | RESOURCE_TYPE | — | — |
| 21 | DayStartTime | START_TIME | — | ✅ |
| 22 | DayStopTime | STOP_TIME | — | ✅ |
| 23 | DaySubresourceId | SUBRESOURCE_ID | — | — |
| 24 | DayTimeConsumerConfigurationSetId | TCSMR_CONFIG_SET_ID | — | — |
| 25 | DayTimeConsumerSetId | TCSMR_SET_ID | — | — |
| 26 | DayTimeRecordGroupId | TM_REC_GRP_ID | — | ✅ |
| 27 | DayTimeRecordGroupVersion | TM_REC_GRP_VERSION | — | ✅ |
| 28 | DayTimeReporterId | TIME_REPORTER_ID | — | — |
| 29 | DayUserStatus | USER_STATUS | — | — |
| 30 | TimeCardCommentText | COMMENT_TEXT | — | ✅ |
| 31 | TimeCardCommitTimestamp | COMMIT_TIMESTAMP | — | ✅ |
| 32 | TimeCardCreatedBy | CREATED_BY | — | ✅ |
| 33 | TimeCardCreationDate | CREATION_DATE | — | ✅ |
| 34 | TimeCardDataSetId | DATA_SET_ID | — | — |
| 35 | TimeCardDateFrom | DATE_FROM | — | ✅ |
| 36 | TimeCardDateTo | DATE_TO | — | ✅ |
| 37 | TimeCardDeleteFlag | DELETE_FLAG | — | ✅ |
| 38 | TimeCardEnterpriseId | ENTERPRISE_ID | — | — |
| 39 | TimeCardGroupTypeId | GRP_TYPE_ID | — | ✅ |
| 40 | TimeCardLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 41 | TimeCardLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 42 | TimeCardLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 43 | TimeCardLatestVersion | LATEST_VERSION | — | ✅ |
| 44 | TimeCardLayerCode | LAYER_CODE | — | ✅ |
| 45 | TimeCardOrderEntered | ORDER_ENTERED | — | — |
| 46 | TimeCardOriginalTimeRecordGroupId | ORIG_TM_REC_GRP_ID | — | ✅ |
| 47 | TimeCardOriginalTimeRecordGroupVersion | ORIG_TM_REC_GRP_VERSION | — | ✅ |
| 48 | TimeCardResourceId | RESOURCE_ID | — | — |
| 49 | TimeCardResourceType | RESOURCE_TYPE | — | — |
| 50 | TimeCardStartTime | START_TIME | — | ✅ |
| 51 | TimeCardStopTime | STOP_TIME | — | ✅ |
| 52 | TimeCardSubresourceId | SUBRESOURCE_ID | — | — |
| 53 | TimeCardTimeConsumerConfigurationSetId | TCSMR_CONFIG_SET_ID | — | — |
| 54 | TimeCardTimeConsumerSetId | TCSMR_SET_ID | — | — |
| 55 | TimeCardTimeRecordGroupId | TM_REC_GRP_ID | — | ✅ |
| 56 | TimeCardTimeRecordGroupVersion | TM_REC_GRP_VERSION | — | ✅ |
| 57 | TimeCardTimeReporterId | TIME_REPORTER_ID | — | — |
| 58 | TimeCardUserStatus | USER_STATUS | — | — |

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
| 2 | HxtDay | HXT_DAY | — | — |
| 3 | HxtResolvedPeriodId | HXT_RESOLVED_PERIOD_ID | — | — |
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

### [[hwm_tm_statuses|HWM_TM_STATUSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TeRdyXfrPjcTimeStatusPEOStatusId | STATUS_ID | — | — |
| 2 | TeRdyXfrPjcTimeStatusPEOStatusValue | STATUS_VALUE | — | — |
| 3 | TeRdyXfrPyrTimeStatusPEOStatusId | STATUS_ID | — | — |
| 4 | TeRdyXfrPyrTimeStatusPEOStatusValue | STATUS_VALUE | — | — |
| 5 | TeXfrPjcTimeStatusPEOStatusId | STATUS_ID | — | — |
| 6 | TeXfrPjcTimeStatusPEOStatusValue | STATUS_VALUE | — | — |
| 7 | TeXfrPyrTimeStatusPEOStatusId | STATUS_ID | — | — |
| 8 | TeXfrPyrTimeStatusPEOStatusValue | STATUS_VALUE | — | — |

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
