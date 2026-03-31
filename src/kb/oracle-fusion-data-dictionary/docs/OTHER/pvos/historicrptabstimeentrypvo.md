---
id: DOC-OTHER-PVO-HistoricRptAbsTimeEntryPVO
doc_type: system-doc
title: "HistoricRptAbsTimeEntryPVO — PVO Cross-Module"
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
  - HistoricRptAbsTimeEntryPVO
  - historicrptabstimeentrypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HistoricRptAbsTimeEntryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Historic Rpt Abs Time Entry. Acessa as tabelas: HWM_RP_TM_PERIODS_TL, HWM_TC_VERSION_STATUS_V, HWM_TE_VERSION_STATUS_V (+27).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeRepositoryAM.HistoricRptAbsTimeEntryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 182 | 30 | 2 | 105 | 58% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_rp_tm_periods_tl|HWM_RP_TM_PERIODS_TL]] — 3 atributos (2 BICC)
- [[hwm_tc_version_status_v|HWM_TC_VERSION_STATUS_V]] — 4 atributos
- [[hwm_te_version_status_v|HWM_TE_VERSION_STATUS_V]] — 6 atributos
- [[hwm_tm_approved_ts_v|HWM_TM_APPROVED_TS_V]] — 2 atributos (1 BICC)
- [[hwm_tm_a_anc_app_status_v|HWM_TM_A_ANC_APP_STATUS_V]] — 2 atributos (1 BICC)
- [[hwm_tm_a_app_status_pjc_v|HWM_TM_A_APP_STATUS_PJC_V]] — 2 atributos (1 BICC)
- [[hwm_tm_a_app_status_pyr_v|HWM_TM_A_APP_STATUS_PYR_V]] — 2 atributos (1 BICC)
- [[hwm_tm_a_te_completed_v|HWM_TM_A_TE_COMPLETED_V]] — 1 atributos
- [[hwm_tm_a_tr_err_status_v|HWM_TM_A_TR_ERR_STATUS_V]] — 1 atributos
- [[hwm_tm_a_user_status_v|HWM_TM_A_USER_STATUS_V]] — 2 atributos (1 BICC)
- [[hwm_tm_d_tm_ui_status_v|HWM_TM_D_TM_UI_STATUS_V]] — 2 atributos (1 BICC)
- [[hwm_tm_opm_meaning_v|HWM_TM_OPM_MEANING_V]] — 2 atributos (1 BICC)
- [[hwm_tm_reprocess_request|HWM_TM_REPROCESS_REQUEST]] — 3 atributos (2 BICC)
- [[hwm_tm_rep_m_anc_atrbs_v|HWM_TM_REP_M_ANC_ATRBS_V]] — 2 atributos (1 BICC)
- [[hwm_tm_rep_m_comp_toil_atrbs_v|HWM_TM_REP_M_COMP_TOIL_ATRBS_V]] — 2 atributos
- [[hwm_tm_rep_m_pjc_doc_atrbs_v|HWM_TM_REP_M_PJC_DOC_ATRBS_V]] — 2 atributos (1 BICC)
- [[hwm_tm_rep_m_pjc_exp_atrbs_v|HWM_TM_REP_M_PJC_EXP_ATRBS_V]] — 2 atributos (1 BICC)
- [[hwm_tm_rep_m_ptt_atrbs_v|HWM_TM_REP_M_PTT_ATRBS_V]] — 2 atributos (1 BICC)
- [[hwm_tm_rep_s_abs_hp_atrbs_v|HWM_TM_REP_S_ABS_HP_ATRBS_V]] — 4 atributos (2 BICC)
- [[hwm_tm_rep_s_abs_tep_atrbs_v|HWM_TM_REP_S_ABS_TEP_ATRBS_V]] — 2 atributos (1 BICC)
- [[hwm_tm_rep_s_common_atrbs_v|HWM_TM_REP_S_COMMON_ATRBS_V]] — 3 atributos (2 BICC)
- [[hwm_tm_rep_s_hxt_atrbs_v|HWM_TM_REP_S_HXT_ATRBS_V]] — 8 atributos (5 BICC)
- [[hwm_tm_rep_s_pjc_atrbs_v|HWM_TM_REP_S_PJC_ATRBS_V]] — 11 atributos (9 BICC)
- [[hwm_tm_rep_s_sec_atrbs_v|HWM_TM_REP_S_SEC_ATRBS_V]] — 6 atributos (4 BICC)
- [[hwm_tm_rpt_entry_v|HWM_TM_RPT_ENTRY_V]] — 80 atributos (2 PKs, 62 BICC)
- [[hwm_tm_statuses|HWM_TM_STATUSES]] — 14 atributos
- [[hwm_tm_submitted_ts_v|HWM_TM_SUBMITTED_TS_V]] — 2 atributos (1 BICC)
- [[hxt_tm_header|HXT_TM_HEADER]] — 2 atributos
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 4 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 4 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hwm_rp_tm_periods_tl|HWM_RP_TM_PERIODS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RepeatingTimePeriodTLDescription | DESCRIPTION | — | ✅ |
| 2 | RepeatingTimePeriodTLLanguage | LANGUAGE | — | — |
| 3 | RepeatingTimePeriodTLRepeatingTmPeriodId | REPEATING_TM_PERIOD_ID | — | ✅ |

### [[hwm_tc_version_status_v|HWM_TC_VERSION_STATUS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeCardVersionStatusPEOMaxAUserStatusId | MAX_A_USER_STATUS_ID | — | — |
| 2 | TimeCardVersionStatusPEOMaxDUiStatusId | MAX_D_UI_STATUS_ID | — | — |
| 3 | TimeCardVersionStatusPEOTmBldgBlkId | TM_BLDG_BLK_ID | — | — |
| 4 | TimeCardVersionStatusPEOTmBldgBlkVersion | TM_BLDG_BLK_VERSION | — | — |

### [[hwm_te_version_status_v|HWM_TE_VERSION_STATUS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeEntryVersionStatusPEOMaxAAppStatusPjcId | MAX_A_APP_STATUS_PJC_ID | — | — |
| 2 | TimeEntryVersionStatusPEOMaxAAppStatusPyrId | MAX_A_APP_STATUS_PYR_ID | — | — |
| 3 | TimeEntryVersionStatusPEOMaxATeCompletedId | MAX_A_TE_COMPLETED_ID | — | — |
| 4 | TimeEntryVersionStatusPEOMaxATrErrStatusId | MAX_A_TR_ERR_STATUS_ID | — | — |
| 5 | TimeEntryVersionStatusPEOTmBldgBlkId | TM_BLDG_BLK_ID | — | — |
| 6 | TimeEntryVersionStatusPEOTmBldgBlkVersion | TM_BLDG_BLK_VERSION | — | — |

### [[hwm_tm_approved_ts_v|HWM_TM_APPROVED_TS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeCardApprovedTimestampPEOApprovedTimestamp | APPROVED_TIMESTAMP | — | ✅ |
| 2 | TimeCardApprovedTimestampPEOStatusId | STATUS_ID | — | — |

### [[hwm_tm_a_anc_app_status_v|HWM_TM_A_ANC_APP_STATUS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TmAtomicAbsApprovalStatusPEOStatusId | STATUS_ID | — | — |
| 2 | TmAtomicAbsApprovalStatusPEOStatusValue | STATUS_VALUE | — | ✅ |

### [[hwm_tm_a_app_status_pjc_v|HWM_TM_A_APP_STATUS_PJC_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TmAtomicPjcApprovalStatusPEOStatusId | STATUS_ID | — | — |
| 2 | TmAtomicPjcApprovalStatusPEOStatusValue | STATUS_VALUE | — | ✅ |

### [[hwm_tm_a_app_status_pyr_v|HWM_TM_A_APP_STATUS_PYR_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TmAtomicPyrApprovalStatusPEOStatusId | STATUS_ID | — | — |
| 2 | TmAtomicPyrApprovalStatusPEOStatusValue | STATUS_VALUE | — | ✅ |

### [[hwm_tm_a_te_completed_v|HWM_TM_A_TE_COMPLETED_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeAtomicCompletedStatusPEOStatusId | STATUS_ID | — | — |

### [[hwm_tm_a_tr_err_status_v|HWM_TM_A_TR_ERR_STATUS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeAtomicErrorStatusPEOStatusId | STATUS_ID | — | — |

### [[hwm_tm_a_user_status_v|HWM_TM_A_USER_STATUS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeAtomicUserStatusPEOStatusId | STATUS_ID | — | — |
| 2 | TimeAtomicUserStatusPEOStatusValue | STATUS_VALUE | — | ✅ |

### [[hwm_tm_d_tm_ui_status_v|HWM_TM_D_TM_UI_STATUS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeDerivedUIStatusPEOStatusId | STATUS_ID | — | — |
| 2 | TimeDerivedUIStatusPEOStatusValue | STATUS_VALUE | — | ✅ |

### [[hwm_tm_opm_meaning_v|HWM_TM_OPM_MEANING_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OverridePaymentMethodCode | CODE | — | — |
| 2 | OverridePaymentMethodCodeMeaning | MEANING | — | ✅ |

### [[hwm_tm_reprocess_request|HWM_TM_REPROCESS_REQUEST]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReprocessRequestPEOReprocessReason | REPROCESS_REASON | — | ✅ |
| 2 | ReprocessRequestPEOReprocessStatus | REPROCESS_STATUS | — | ✅ |
| 3 | ReprocessRequestPEOTmReprocessRequestId | TM_REPROCESS_REQUEST_ID | — | — |

### [[hwm_tm_rep_m_anc_atrbs_v|HWM_TM_REP_M_ANC_ATRBS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MasterAbsTypeAttributePEOAncAbsenceType | ANC_ABSENCE_TYPE | — | ✅ |
| 2 | MasterAbsTypeAttributePEOAncMasterTimeRepositoryAttributeId | ANC_MASTER_TIME_REPOS_ATRB_ID | — | — |

### [[hwm_tm_rep_m_comp_toil_atrbs_v|HWM_TM_REP_M_COMP_TOIL_ATRBS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ToilReposAtrbId | TOIL_REPOS_ATRB_ID | — | — |
| 2 | ToilTimeType | TOIL_TIME_TYPE | — | — |

### [[hwm_tm_rep_m_pjc_doc_atrbs_v|HWM_TM_REP_M_PJC_DOC_ATRBS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MasterDocTypeAttributePEOPjcDocTypeTimeRepositoryAttributeId | PJC_DOC_TIME_REPOS_ATRB_ID | — | — |
| 2 | MasterDocTypeAttributePEOPjcDocumentType | PJC_DOCUMENT_TYPE | — | ✅ |

### [[hwm_tm_rep_m_pjc_exp_atrbs_v|HWM_TM_REP_M_PJC_EXP_ATRBS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MasterExpendTypeAttributePEOPjcExpTypeTimeRepositoryAttributeId | PJC_EXP_TIME_REPOS_ATRB_ID | — | — |
| 2 | MasterExpendTypeAttributePEOPjcExpenditureType | PJC_EXPENDITURE_TYPE | — | ✅ |

### [[hwm_tm_rep_m_ptt_atrbs_v|HWM_TM_REP_M_PTT_ATRBS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MasterPyrTimeTypeAtrbPEOPayPayrollTimeType | PAY_PAYROLL_TIME_TYPE | — | ✅ |
| 2 | MasterPyrTimeTypeAtrbPEOPttTimeRepositoryAttributeId | PTT_TIME_REPOS_ATRB_ID | — | — |

### [[hwm_tm_rep_s_abs_hp_atrbs_v|HWM_TM_REP_S_ABS_HP_ATRBS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SimpleAbsHeaderParamsAtrbPEOAncAbsenceEntryId | ANC_ABSENCE_ENTRY_ID | — | ✅ |
| 2 | SimpleAbsHeaderParamsAtrbPEOAncAttributeCategory | ANC_ATTRIBUTE_CATEGORY | — | — |
| 3 | SimpleAbsHeaderParamsAtrbPEOAncEndOfBreakdown | ANC_END_OF_BREAKDOWN | — | ✅ |
| 4 | SimpleAbsHeaderParamsAtrbPEOAncTimeRepositoryAttributeId | ANC_TIME_REPOS_ATRB_ID | — | — |

### [[hwm_tm_rep_s_abs_tep_atrbs_v|HWM_TM_REP_S_ABS_TEP_ATRBS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SimpleAbsTeParamsAtrbPEOAncDurationPaid | ANC_DURATION_PAID | — | ✅ |
| 2 | SimpleAbsTeParamsAtrbPEOAncTimeRepositoryAttributeId | ANC_TIME_REPOS_ATRB_ID | — | — |

### [[hwm_tm_rep_s_common_atrbs_v|HWM_TM_REP_S_COMMON_ATRBS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CommonInternalSource | COMMON_INTERNAL_SOURCE | — | ✅ |
| 2 | CommonOwner | COMMON_OWNER | — | ✅ |
| 3 | CommonTimeReposAtrbId1 | COMMON_TIME_REPOS_ATRB_ID | — | — |

### [[hwm_tm_rep_s_hxt_atrbs_v|HWM_TM_REP_S_HXT_ATRBS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Expedite | EXPEDITE | — | ✅ |
| 2 | HxtTimeRepositoryAttributeId | HXT_TIME_REPOS_ATRB_ID | — | — |
| 3 | OverrideCheckPrinter | OVERRIDE_CHECK_PRINTER | — | ✅ |
| 4 | OverridePayMethod | OVERRIDE_PAY_METHOD | — | ✅ |
| 5 | SimpleHxtAttributePEOHxtAttributeCategory | HXT_ATTRIBUTE_CATEGORY | — | — |
| 6 | SimpleHxtAttributePEOHxtDay | HXT_DAY | — | ✅ |
| 7 | SimpleHxtAttributePEOHxtResolvedPeriodId | HXT_RESOLVED_PERIOD_ID | — | ✅ |
| 8 | SimpleHxtAttributePEOHxtTmReposAtrbId | HXT_TIME_REPOS_ATRB_ID | — | — |

### [[hwm_tm_rep_s_pjc_atrbs_v|HWM_TM_REP_S_PJC_ATRBS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SimpleProjectsAttributePEOPjcAttributeCategory | PJC_ATTRIBUTE_CATEGORY | — | — |
| 2 | SimpleProjectsAttributePEOPjcBillableFlag | PJC_BILLABLE_FLAG | — | ✅ |
| 3 | SimpleProjectsAttributePEOPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | ✅ |
| 4 | SimpleProjectsAttributePEOPjcContractId | PJC_CONTRACT_ID | — | ✅ |
| 5 | SimpleProjectsAttributePEOPjcExpOrganizationId | PJC_EXP_ORGANIZATION_ID | — | ✅ |
| 6 | SimpleProjectsAttributePEOPjcFundingSourceId | PJC_FUNDING_SOURCE_ID | — | ✅ |
| 7 | SimpleProjectsAttributePEOPjcProjectId | PJC_PROJECT_ID | — | ✅ |
| 8 | SimpleProjectsAttributePEOPjcProjectUnit | PJC_PROJECT_UNIT | — | ✅ |
| 9 | SimpleProjectsAttributePEOPjcTaskId | PJC_TASK_ID | — | ✅ |
| 10 | SimpleProjectsAttributePEOPjcTimeRepositoryAttributeId | PJC_TIME_REPOS_ATRB_ID | — | — |
| 11 | SimpleProjectsAttributePEOPjcWorkType | PJC_WORK_TYPE | — | ✅ |

### [[hwm_tm_rep_s_sec_atrbs_v|HWM_TM_REP_S_SEC_ATRBS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SimpleSecurityAttributePEOSecAttributeCategory | SEC_ATTRIBUTE_CATEGORY | — | — |
| 2 | SimpleSecurityAttributePEOSecurityBusinessUnit | SECURITY_BUSINESS_UNIT | — | ✅ |
| 3 | SimpleSecurityAttributePEOSecurityEnterpriseId | SECURITY_ENTERPRISE_ID | — | ✅ |
| 4 | SimpleSecurityAttributePEOSecurityLegislativeDataGroup | SECURITY_LEG_DATA_GROUP | — | ✅ |
| 5 | SimpleSecurityAttributePEOSecurityOrganizationId | SECURITY_ORGANIZATION_ID | — | ✅ |
| 6 | SimpleSecurityAttributePEOSecurityTimeRepositoryAttributeId | SEC_TIME_REPOS_ATRB_ID | — | — |

### [[hwm_tm_rpt_entry_v|HWM_TM_RPT_ENTRY_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AncDeleteFlag | ANC_DELETE_FLAG | — | — |
| 2 | AncLatestVersion | ANC_LATEST_VERSION | — | — |
| 3 | RptAbsTimeEntryPEOAncGrpTypeId | ANC_GRP_TYPE_ID | — | ✅ |
| 4 | RptAbsTimeEntryPEOAncTmRecGrpId | ANC_TM_REC_GRP_ID | — | ✅ |
| 5 | RptAbsTimeEntryPEOAncTmRecGrpVersion | ANC_TM_REC_GRP_VERSION | — | ✅ |
| 6 | RptAbsTimeEntryPEODayCommentText | DAY_COMMENT_TEXT | — | ✅ |
| 7 | RptAbsTimeEntryPEODayCreatedBy | DAY_CREATED_BY | — | ✅ |
| 8 | RptAbsTimeEntryPEODayCreationDate | DAY_CREATION_DATE | — | ✅ |
| 9 | RptAbsTimeEntryPEODayDateFrom | DAY_DATE_FROM | — | ✅ |
| 10 | RptAbsTimeEntryPEODayDateTo | DAY_DATE_TO | — | ✅ |
| 11 | RptAbsTimeEntryPEODayDeleteFlag | DAY_DELETE_FLAG | — | ✅ |
| 12 | RptAbsTimeEntryPEODayGrpTypeId | DAY_GRP_TYPE_ID | — | ✅ |
| 13 | RptAbsTimeEntryPEODayLastUpdateDate | DAY_LAST_UPDATE_DATE | — | ✅ |
| 14 | RptAbsTimeEntryPEODayLastUpdateLogin | DAY_LAST_UPDATE_LOGIN | — | ✅ |
| 15 | RptAbsTimeEntryPEODayLastUpdatedBy | DAY_LAST_UPDATED_BY | — | ✅ |
| 16 | RptAbsTimeEntryPEODayLatestVersion | DAY_LATEST_VERSION | — | ✅ |
| 17 | RptAbsTimeEntryPEODayLayerCode | DAY_LAYER_CODE | — | ✅ |
| 18 | RptAbsTimeEntryPEODayStartGmtOffset | DAY_START_GMT_OFFSET | — | — |
| 19 | RptAbsTimeEntryPEODayStartTime | DAY_START_TIME | — | ✅ |
| 20 | RptAbsTimeEntryPEODayStartTimezoneCode | DAY_START_TIMEZONE_CODE | — | ✅ |
| 21 | RptAbsTimeEntryPEODayStopGmtOffset | DAY_STOP_GMT_OFFSET | — | — |
| 22 | RptAbsTimeEntryPEODayStopTime | DAY_STOP_TIME | — | ✅ |
| 23 | RptAbsTimeEntryPEODayStopTimezoneCode | DAY_STOP_TIMEZONE_CODE | — | ✅ |
| 24 | RptAbsTimeEntryPEODayTmRecGrpId | DAY_TM_REC_GRP_ID | — | ✅ |
| 25 | RptAbsTimeEntryPEODayTmRecGrpVersion | DAY_TM_REC_GRP_VERSION | — | ✅ |
| 26 | RptAbsTimeEntryPEOTcCommentText | TC_COMMENT_TEXT | — | ✅ |
| 27 | RptAbsTimeEntryPEOTcCommitTimestamp | TC_COMMIT_TIMESTAMP | — | ✅ |
| 28 | RptAbsTimeEntryPEOTcCreatedBy | TC_CREATED_BY | — | ✅ |
| 29 | RptAbsTimeEntryPEOTcCreationDate | TC_CREATION_DATE | — | ✅ |
| 30 | RptAbsTimeEntryPEOTcDateFrom | TC_DATE_FROM | — | ✅ |
| 31 | RptAbsTimeEntryPEOTcDateTo | TC_DATE_TO | — | ✅ |
| 32 | RptAbsTimeEntryPEOTcDeleteFlag | TC_DELETE_FLAG | — | ✅ |
| 33 | RptAbsTimeEntryPEOTcGrpTypeId | TC_GRP_TYPE_ID | — | ✅ |
| 34 | RptAbsTimeEntryPEOTcLastUpdateDate | TC_LAST_UPDATE_DATE | — | ✅ |
| 35 | RptAbsTimeEntryPEOTcLastUpdateLogin | TC_LAST_UPDATE_LOGIN | — | ✅ |
| 36 | RptAbsTimeEntryPEOTcLastUpdatedBy | TC_LAST_UPDATED_BY | — | ✅ |
| 37 | RptAbsTimeEntryPEOTcLatestVersion | TC_LATEST_VERSION | — | ✅ |
| 38 | RptAbsTimeEntryPEOTcLayerCode | TC_LAYER_CODE | — | ✅ |
| 39 | RptAbsTimeEntryPEOTcStartDate | TC_START_DATE | — | — |
| 40 | RptAbsTimeEntryPEOTcStartGmtOffset | TC_START_GMT_OFFSET | — | — |
| 41 | RptAbsTimeEntryPEOTcStartTime | TC_START_TIME | — | ✅ |
| 42 | RptAbsTimeEntryPEOTcStartTimezoneCode | TC_START_TIMEZONE_CODE | — | — |
| 43 | RptAbsTimeEntryPEOTcStopDate | TC_STOP_DATE | — | — |
| 44 | RptAbsTimeEntryPEOTcStopGmtOffset | TC_STOP_GMT_OFFSET | — | — |
| 45 | RptAbsTimeEntryPEOTcStopTime | TC_STOP_TIME | — | ✅ |
| 46 | RptAbsTimeEntryPEOTcStopTimezoneCode | TC_STOP_TIMEZONE_CODE | — | — |
| 47 | RptAbsTimeEntryPEOTcTmRecGrpId | TC_TM_REC_GRP_ID | — | ✅ |
| 48 | RptAbsTimeEntryPEOTcTmRecGrpVersion | TC_TM_REC_GRP_VERSION | — | ✅ |
| 49 | RptAbsTimeEntryPEOTeActivityInId | TE_ACTIVITY_IN_ID | — | — |
| 50 | RptAbsTimeEntryPEOTeActivityOutId | TE_ACTIVITY_OUT_ID | — | — |
| 51 | RptAbsTimeEntryPEOTeCommentText | TE_COMMENT_TEXT | — | ✅ |
| 52 | RptAbsTimeEntryPEOTeCreatedBy | TE_CREATED_BY | — | ✅ |
| 53 | RptAbsTimeEntryPEOTeCreationDate | TE_CREATION_DATE | — | ✅ |
| 54 | RptAbsTimeEntryPEOTeDateFrom | TE_DATE_FROM | — | ✅ |
| 55 | RptAbsTimeEntryPEOTeDateTo | TE_DATE_TO | — | ✅ |
| 56 | RptAbsTimeEntryPEOTeDeleteFlag | TE_DELETE_FLAG | — | ✅ |
| 57 | RptAbsTimeEntryPEOTeLastUpdateDate | TE_LAST_UPDATE_DATE | — | ✅ |
| 58 | RptAbsTimeEntryPEOTeLastUpdateLogin | TE_LAST_UPDATE_LOGIN | — | ✅ |
| 59 | RptAbsTimeEntryPEOTeLastUpdatedBy | TE_LAST_UPDATED_BY | — | ✅ |
| 60 | RptAbsTimeEntryPEOTeLatestVersion | TE_LATEST_VERSION | — | ✅ |
| 61 | RptAbsTimeEntryPEOTeLayerCode | TE_LAYER_CODE | — | ✅ |
| 62 | RptAbsTimeEntryPEOTeMeasure | TE_MEASURE | — | ✅ |
| 63 | RptAbsTimeEntryPEOTeMeasureAbsence | TE_MEASURE_ABSENCE | — | ✅ |
| 64 | RptAbsTimeEntryPEOTeMeasureAbsenceDay | TE_MEASURE_ABSENCE_DAY | — | — |
| 65 | RptAbsTimeEntryPEOTeMeasureLabor | TE_MEASURE_LABOR | — | ✅ |
| 66 | RptAbsTimeEntryPEOTeResourceId | RESOURCE_ID | — | — |
| 67 | RptAbsTimeEntryPEOTeStartGmtOffset | TE_START_GMT_OFFSET | — | — |
| 68 | RptAbsTimeEntryPEOTeStartTime | TE_START_TIME | — | ✅ |
| 69 | RptAbsTimeEntryPEOTeStartTimezoneCode | TE_START_TIMEZONE_CODE | — | ✅ |
| 70 | RptAbsTimeEntryPEOTeStopGmtOffset | TE_STOP_GMT_OFFSET | — | — |
| 71 | RptAbsTimeEntryPEOTeStopTime | TE_STOP_TIME | — | ✅ |
| 72 | RptAbsTimeEntryPEOTeStopTimezoneCode | TE_STOP_TIMEZONE_CODE | — | ✅ |
| 73 | RptAbsTimeEntryPEOTeSubresourceId | TE_SUBRESOURCE_ID | — | — |
| 74 | RptAbsTimeEntryPEOTeTcsmrConfigSetId | TE_TCSMR_CONFIG_SET_ID | — | — |
| 75 | RptAbsTimeEntryPEOTeTcsmrSetId | TE_TCSMR_SET_ID | — | ✅ |
| 76 | RptAbsTimeEntryPEOTeTimeReporterId | TE_TIME_REPORTER_ID | — | ✅ |
| 77 | RptAbsTimeEntryPEOTeTmRecId | TE_TM_REC_ID | 🔑 | ✅ |
| 78 | RptAbsTimeEntryPEOTeTmRecType | TE_TM_REC_TYPE | — | ✅ |
| 79 | RptAbsTimeEntryPEOTeTmRecVersion | TE_TM_REC_VERSION | 🔑 | ✅ |
| 80 | RptAbsTimeEntryPEOTeUnitOfMeasure | TE_UNIT_OF_MEASURE | — | ✅ |

### [[hwm_tm_statuses|HWM_TM_STATUSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TcUiTimeStatusPEODateFrom | DATE_FROM | — | — |
| 2 | TcUiTimeStatusPEOStatusId | STATUS_ID | — | — |
| 3 | TcUiTimeStatusPEOStatusValue | STATUS_VALUE | — | — |
| 4 | TcUserTimeStatusPEODateFrom | DATE_FROM | — | — |
| 5 | TcUserTimeStatusPEOStatusId | STATUS_ID | — | — |
| 6 | TcUserTimeStatusPEOStatusValue | STATUS_VALUE | — | — |
| 7 | TeAppPjcTimeStatusPEOStatusId | STATUS_ID | — | — |
| 8 | TeAppPjcTimeStatusPEOStatusValue | STATUS_VALUE | — | — |
| 9 | TeAppPyrTimeStatusPEOStatusId | STATUS_ID | — | — |
| 10 | TeAppPyrTimeStatusPEOStatusValue | STATUS_VALUE | — | — |
| 11 | TeCmpTimeStatusPEOStatusId | STATUS_ID | — | — |
| 12 | TeCmpTimeStatusPEOStatusValue | STATUS_VALUE | — | — |
| 13 | TeErrTimeStatusPEOStatusId | STATUS_ID | — | — |
| 14 | TeErrTimeStatusPEOStatusValue | STATUS_VALUE | — | — |

### [[hwm_tm_submitted_ts_v|HWM_TM_SUBMITTED_TS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TcSubmittedTimestampPEOStatusId | STATUS_ID | — | — |
| 2 | TcSubmittedTimestampPEOSubmittedTimestamp | SUBMITTED_TIMESTAMP | — | ✅ |

### [[hxt_tm_header|HXT_TM_HEADER]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimecardHeaderPEOTclaystId | TCLAYST_ID | — | — |
| 2 | TimecardHeaderPEOTimecardHeaderId | TM_HEADER_ID | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonDetailsPEOPersonId | PERSON_ID | — | — |
| 4 | PersonDetailsPEOPersonNumber | PERSON_NUMBER | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonNamePEOFullName | FULL_NAME | — | ✅ |
| 4 | PersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
