---
id: DOC-HCM-PVO-NBoxLabelPVO
doc_type: system-doc
title: "NBoxLabelPVO — PVO Human Capital Management"
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
  - NBoxLabelPVO
  - nboxlabelpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NBoxLabelPVO

## 📌 Visão Geral

Disponibiliza rótulos das células do N-Box (9-box matrix) por sequência e reunião de calibração. Permite personalização da nomenclatura dos quadrantes de desempenho/potencial.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmTalentCalibMeetingsAM.NBoxLabelPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 95 | 5 | 4 | 10 | 11% |

---

## 🔗 Tabelas Relacionadas

- [[hrr_dashboard_tmpls_b|HRR_DASHBOARD_TMPLS_B]] — 37 atributos (1 BICC)
- [[hrr_meetings|HRR_MEETINGS]] — 20 atributos (2 PKs, 3 BICC)
- [[hrr_tmpl_analytic_types_b|HRR_TMPL_ANALYTIC_TYPES_B]] — 16 atributos (1 BICC)
- [[hrr_tmpl_anlyt_box_lbls_b|HRR_TMPL_ANLYT_BOX_LBLS_B]] — 11 atributos (1 PKs, 2 BICC)
- [[hrr_tmpl_anlyt_box_lbls_tl|HRR_TMPL_ANLYT_BOX_LBLS_TL]] — 11 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[hrr_dashboard_tmpls_b|HRR_DASHBOARD_TMPLS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ColorJobroleAssgn | COLOR_JOBROLE_ASSGN | — | — |
| 2 | ColorLocation | COLOR_LOCATION | — | — |
| 3 | ColorOrgHierarchy | COLOR_ORG_HIERARCHY | — | — |
| 4 | CreateGoalsFlag | CREATE_GOALS_FLAG | — | — |
| 5 | DashTmplBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 6 | DashTmplBPEOCreatedBy | CREATED_BY | — | — |
| 7 | DashTmplBPEOCreationDate | CREATION_DATE | — | — |
| 8 | DashTmplBPEODashboardTmplId | DASHBOARD_TMPL_ID | — | — |
| 9 | DashTmplBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | DashTmplBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | DashTmplBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | DashTmplBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | DisplayAge | DISPLAY_AGE | — | — |
| 14 | DisplayEthnicity | DISPLAY_ETHNICITY | — | — |
| 15 | DisplayGender | DISPLAY_GENDER | — | — |
| 16 | DisplayImpactOfLoss | DISPLAY_IMPACT_OF_LOSS | — | — |
| 17 | DisplayMobility | DISPLAY_MOBILITY | — | — |
| 18 | DisplayReligiousAffltn | DISPLAY_RELIGIOUS_AFFLTN | — | — |
| 19 | DisplayRiskOfLoss | DISPLAY_RISK_OF_LOSS | — | — |
| 20 | FilterCompetency | FILTER_COMPETENCY | — | — |
| 21 | FilterJobroleAssgn | FILTER_JOBROLE_ASSGN | — | — |
| 22 | FilterLevel | FILTER_LEVEL | — | — |
| 23 | FilterLocation | FILTER_LOCATION | — | — |
| 24 | FilterOrgHierarchy | FILTER_ORG_HIERARCHY | — | — |
| 25 | FilterProficiency | FILTER_PROFICIENCY | — | — |
| 26 | FilterSuccessionPlan | FILTER_SUCCESSION_PLAN | — | — |
| 27 | FilterTalentPool | FILTER_TALENT_POOL | — | — |
| 28 | IncludeSuccessionPlans | INCLUDE_SUCCESSION_PLANS | — | — |
| 29 | IncludeTalentPools | INCLUDE_TALENT_POOLS | — | — |
| 30 | MaxMarkersAllowed | MAX_MARKERS_ALLOWED | — | — |
| 31 | ModuleId | MODULE_ID | — | — |
| 32 | OwnerId | OWNER_ID | — | — |
| 33 | SetId | SET_ID | — | — |
| 34 | TmplStatusCode | TMPL_STATUS_CODE | — | — |
| 35 | UseHoldingAreaFlag | USE_HOLDING_AREA_FLAG | — | — |
| 36 | UseNotesFlag | USE_NOTES_FLAG | — | — |
| 37 | UseTasksFlag | USE_TASKS_FLAG | — | — |

### [[hrr_meetings|HRR_MEETINGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | DashboardTmplId | DASHBOARD_TMPL_ID | — | — |
| 5 | DataSubmitDate | DATA_SUBMIT_DATE | — | — |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | MeetingDate | MEETING_DATE | — | — |
| 10 | MeetingFacilitatorNotes | MEETING_FACILITATOR_NOTES | — | — |
| 11 | MeetingId | MEETING_ID | 🔑 | ✅ |
| 12 | MeetingInstructions | MEETING_INSTRUCTIONS | — | — |
| 13 | MeetingLeaderId | MEETING_LEADER_ID | — | — |
| 14 | MeetingOrganizationId | MEETING_ORGANIZATION_ID | — | — |
| 15 | MeetingPurpose | MEETING_PURPOSE | — | — |
| 16 | MeetingStatusCode | MEETING_STATUS_CODE | — | — |
| 17 | MeetingSubmitStatusCode | MEETING_SUBMIT_STATUS_CODE | — | — |
| 18 | MeetingTitle | MEETING_TITLE | — | — |
| 19 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | PrefReviewQualifierId | PREF_REVIEW_QUALIFIER_ID | — | — |

### [[hrr_tmpl_analytic_types_b|HRR_TMPL_ANALYTIC_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AnalyticTypeCode | ANALYTIC_TYPE_CODE | — | — |
| 2 | AnalyticTypeId | ANALYTIC_TYPE_ID | — | — |
| 3 | AnalyticViewMode | ANALYTIC_VIEW_MODE | — | — |
| 4 | ColorSchemeCode | COLOR_SCHEME_CODE | — | — |
| 5 | HorizontalAxisCode | HORIZONTAL_AXIS_CODE | — | — |
| 6 | SubmitBoxAsgnmntFlag | SUBMIT_BOX_ASGNMNT_FLAG | — | — |
| 7 | TmplAnalyticTypeBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 8 | TmplAnalyticTypeBPEOCreatedBy | CREATED_BY | — | — |
| 9 | TmplAnalyticTypeBPEOCreationDate | CREATION_DATE | — | — |
| 10 | TmplAnalyticTypeBPEODashboardTmplId | DASHBOARD_TMPL_ID | — | — |
| 11 | TmplAnalyticTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | TmplAnalyticTypeBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | TmplAnalyticTypeBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | TmplAnalyticTypeBPEOModuleId | MODULE_ID | — | — |
| 15 | TmplAnalyticTypeBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | VerticalAxisCode | VERTICAL_AXIS_CODE | — | — |

### [[hrr_tmpl_anlyt_box_lbls_b|HRR_TMPL_ANLYT_BOX_LBLS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AnalyticBoxLabelId | ANALYTIC_BOX_LABEL_ID | — | — |
| 2 | BoxSequence | BOX_SEQUENCE | 🔑 | ✅ |
| 3 | TmplAnylBoxLblPEOAnalyticTypeId | ANALYTIC_TYPE_ID | — | — |
| 4 | TmplAnylBoxLblPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 5 | TmplAnylBoxLblPEOCreatedBy | CREATED_BY | — | — |
| 6 | TmplAnylBoxLblPEOCreationDate | CREATION_DATE | — | — |
| 7 | TmplAnylBoxLblPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | TmplAnylBoxLblPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | TmplAnylBoxLblPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | TmplAnylBoxLblPEOModuleId | MODULE_ID | — | — |
| 11 | TmplAnylBoxLblPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[hrr_tmpl_anlyt_box_lbls_tl|HRR_TMPL_ANLYT_BOX_LBLS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BoxLabel | BOX_LABEL | — | ✅ |
| 2 | TmplAnylBoxLblTLPEOAnalyticBoxLabelId | ANALYTIC_BOX_LABEL_ID | — | — |
| 3 | TmplAnylBoxLblTLPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | TmplAnylBoxLblTLPEOCreatedBy | CREATED_BY | — | — |
| 5 | TmplAnylBoxLblTLPEOCreationDate | CREATION_DATE | — | — |
| 6 | TmplAnylBoxLblTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | TmplAnylBoxLblTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | TmplAnylBoxLblTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | TmplAnylBoxLblTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | TmplAnylBoxLblTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | TmplAnylBoxLblTLPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
