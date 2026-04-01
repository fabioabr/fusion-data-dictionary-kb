---
id: DOC-OTHER-PVO-DashboardTemplatePVO
doc_type: system-doc
title: "DashboardTemplatePVO — PVO Cross-Module"
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
  - DashboardTemplatePVO
  - dashboardtemplatepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DashboardTemplatePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Dashboard Template. Acessa as tabelas: HRR_DASHBOARD_TMPLS_B, HRR_DASHBOARD_TMPLS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmTalentCalibSetupAM.DashboardTemplatePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 48 | 2 | 2 | 35 | 73% |

---

## 🔗 Tabelas Relacionadas

- [[hrr_dashboard_tmpls_b|HRR_DASHBOARD_TMPLS_B]] — 37 atributos (2 PKs, 34 BICC)
- [[hrr_dashboard_tmpls_tl|HRR_DASHBOARD_TMPLS_TL]] — 11 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hrr_dashboard_tmpls_b|HRR_DASHBOARD_TMPLS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | ColorJobroleAssgn | COLOR_JOBROLE_ASSGN | — | — |
| 3 | ColorLocation | COLOR_LOCATION | — | — |
| 4 | ColorOrgHierarchy | COLOR_ORG_HIERARCHY | — | — |
| 5 | CreateGoalsFlag | CREATE_GOALS_FLAG | — | ✅ |
| 6 | CreatedBy | CREATED_BY | — | ✅ |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | DashboardTmplId | DASHBOARD_TMPL_ID | 🔑 | ✅ |
| 9 | DisplayAge | DISPLAY_AGE | — | ✅ |
| 10 | DisplayEthnicity | DISPLAY_ETHNICITY | — | ✅ |
| 11 | DisplayGender | DISPLAY_GENDER | — | ✅ |
| 12 | DisplayImpactOfLoss | DISPLAY_IMPACT_OF_LOSS | — | ✅ |
| 13 | DisplayMobility | DISPLAY_MOBILITY | — | ✅ |
| 14 | DisplayReligiousAffltn | DISPLAY_RELIGIOUS_AFFLTN | — | ✅ |
| 15 | DisplayRiskOfLoss | DISPLAY_RISK_OF_LOSS | — | ✅ |
| 16 | FilterCompetency | FILTER_COMPETENCY | — | ✅ |
| 17 | FilterJobroleAssgn | FILTER_JOBROLE_ASSGN | — | ✅ |
| 18 | FilterLevel | FILTER_LEVEL | — | ✅ |
| 19 | FilterLocation | FILTER_LOCATION | — | ✅ |
| 20 | FilterOrgHierarchy | FILTER_ORG_HIERARCHY | — | ✅ |
| 21 | FilterProficiency | FILTER_PROFICIENCY | — | ✅ |
| 22 | FilterSuccessionPlan | FILTER_SUCCESSION_PLAN | — | ✅ |
| 23 | FilterTalentPool | FILTER_TALENT_POOL | — | ✅ |
| 24 | IncludeSuccessionPlans | INCLUDE_SUCCESSION_PLANS | — | ✅ |
| 25 | IncludeTalentPools | INCLUDE_TALENT_POOLS | — | ✅ |
| 26 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 27 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 28 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 29 | MaxMarkersAllowed | MAX_MARKERS_ALLOWED | — | ✅ |
| 30 | ModuleId | MODULE_ID | — | ✅ |
| 31 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 32 | OwnerId | OWNER_ID | — | ✅ |
| 33 | SetId | SET_ID | — | ✅ |
| 34 | TmplStatusCode | TMPL_STATUS_CODE | — | ✅ |
| 35 | UseHoldingAreaFlag | USE_HOLDING_AREA_FLAG | — | ✅ |
| 36 | UseNotesFlag | USE_NOTES_FLAG | — | ✅ |
| 37 | UseTasksFlag | USE_TASKS_FLAG | — | ✅ |

### [[hrr_dashboard_tmpls_tl|HRR_DASHBOARD_TMPLS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DashTmpltTLPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | DashTmpltTLPEOCreatedBy | CREATED_BY | — | — |
| 3 | DashTmpltTLPEOCreationDate | CREATION_DATE | — | — |
| 4 | DashTmpltTLPEODashboardTmplId | DASHBOARD_TMPL_ID | — | — |
| 5 | DashTmpltTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 6 | DashTmpltTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | DashTmpltTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | DashTmpltTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | Language | LANGUAGE | — | — |
| 10 | Name | NAME | — | — |
| 11 | SourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
