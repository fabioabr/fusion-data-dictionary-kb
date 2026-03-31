---
id: DOC-OTHER-PVO-PjeIssueAction
doc_type: system-doc
title: "PjeIssueAction — PVO Cross-Module"
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
  - PjeIssueAction
  - pjeissueaction
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PjeIssueAction

## 📌 Visão Geral

View Object para extração BICC de dados de Pje Issue Action. Acessa as tabelas: PJE_ISSUES_B, PJE_ISSUES_TL, PJE_ISSUE_ACTIONS (+4).

**Caminho:** `FscmTopModelAM.PjeIssuesAM.PjeIssueAction`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 62 | 7 | 3 | 19 | 31% |

---

## 🔗 Tabelas Relacionadas

- [[pje_issues_b|PJE_ISSUES_B]] — 20 atributos (1 PKs, 2 BICC)
- [[pje_issues_tl|PJE_ISSUES_TL]] — 13 atributos (5 BICC)
- [[pje_issue_actions|PJE_ISSUE_ACTIONS]] — 10 atributos (2 PKs, 8 BICC)
- [[pjf_proj_elements_vl|PJF_PROJ_ELEMENTS_VL]] — 6 atributos (3 BICC)
- [[pjt_lookups|PJT_LOOKUPS]] — 4 atributos
- [[pjt_prj_enterprise_resource_vl|PJT_PRJ_ENTERPRISE_RESOURCE_VL]] — 3 atributos
- [[pjt_proj_plan_lines|PJT_PROJ_PLAN_LINES]] — 6 atributos (1 BICC)

---

## ⚙️ Atributos

### [[pje_issues_b|PJE_ISSUES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IssueBasePEOClosedReason | CLOSED_REASON | — | — |
| 2 | IssueBasePEOCreatedBy | CREATED_BY | — | — |
| 3 | IssueBasePEOCreatedById | CREATED_BY_ID | — | — |
| 4 | IssueBasePEOCreationDate | CREATION_DATE | — | — |
| 5 | IssueBasePEODateClosed | DATE_CLOSED | — | — |
| 6 | IssueBasePEODateCreated | DATE_CREATED | — | — |
| 7 | IssueBasePEOEnterpriseId | ENTERPRISE_ID | — | — |
| 8 | IssueBasePEOIssueId | ISSUE_ID | 🔑 | ✅ |
| 9 | IssueBasePEOIssueNumber | ISSUE_NUMBER | — | — |
| 10 | IssueBasePEOIssueTypeId | ISSUE_TYPE_ID | — | — |
| 11 | IssueBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | IssueBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | IssueBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | IssueBasePEONeedByDate | NEED_BY_DATE | — | — |
| 15 | IssueBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | IssueBasePEOOwnerId | OWNER_ID | — | — |
| 17 | IssueBasePEOPriorityCode | PRIORITY_CODE | — | — |
| 18 | IssueBasePEOProjectId | PROJECT_ID | — | — |
| 19 | IssueBasePEOStatusCode | STATUS_CODE | — | — |
| 20 | IssueBasePEOTaskId | TASK_ID | — | — |

### [[pje_issues_tl|PJE_ISSUES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IssueTranslationPEOCreatedBy2 | CREATED_BY | — | — |
| 2 | IssueTranslationPEOCreationDate2 | CREATION_DATE | — | — |
| 3 | IssueTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | IssueTranslationPEOEnterpriseId2 | ENTERPRISE_ID | — | — |
| 5 | IssueTranslationPEOIssueId2 | ISSUE_ID | — | — |
| 6 | IssueTranslationPEOLanguage | LANGUAGE | — | — |
| 7 | IssueTranslationPEOLastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 8 | IssueTranslationPEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 9 | IssueTranslationPEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 10 | IssueTranslationPEOReopenSummary | REOPEN_SUMMARY | — | ✅ |
| 11 | IssueTranslationPEOResolution | RESOLUTION | — | ✅ |
| 12 | IssueTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 13 | IssueTranslationPEOSummary | SUMMARY | — | ✅ |

### [[pje_issue_actions|PJE_ISSUE_ACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EnterpriseId1 | ENTERPRISE_ID | 🔑 | ✅ |
| 2 | IssueActionId | ISSUE_ACTION_ID | 🔑 | ✅ |
| 3 | IssueActionPEOActionId | ACTION_ID | — | ✅ |
| 4 | IssueActionPEOActionId1 | ACTION_ID | — | ✅ |
| 5 | IssueActionPEOCreatedBy1 | CREATED_BY | — | ✅ |
| 6 | IssueActionPEOCreationDate1 | CREATION_DATE | — | ✅ |
| 7 | IssueActionPEOIssueId1 | ISSUE_ID | — | — |
| 8 | IssueActionPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 9 | IssueActionPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 10 | IssueActionPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |

### [[pjf_proj_elements_vl|PJF_PROJ_ELEMENTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjtProjElementPEODescription | DESCRIPTION | — | ✅ |
| 2 | PjtProjElementPEOName | NAME | — | ✅ |
| 3 | PjtProjElementPEOPlanningEndDate | PLANNING_END_DATE | — | ✅ |
| 4 | PjtProjElementPEOPlanningStartDate | PLANNING_START_DATE | — | — |
| 5 | PjtProjElementPEOPrimaryResourceId | PRIMARY_RESOURCE_ID | — | — |
| 6 | PjtProjElementPEOProjElementId | PROJ_ELEMENT_ID | — | — |

### [[pjt_lookups|PJT_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjtLookupPEOMeaning | MEANING | — | — |
| 2 | PjtLookupsPEODescription | DESCRIPTION | — | — |
| 3 | PjtLookupsPEOLookupCode | LOOKUP_CODE | — | — |
| 4 | PjtLookupsPEOLookupType | LOOKUP_TYPE | — | — |

### [[pjt_prj_enterprise_resource_vl|PJT_PRJ_ENTERPRISE_RESOURCE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrjEnterpriseResourcePEODisplayName | DISPLAY_NAME | — | — |
| 2 | PrjEnterpriseResourcePEOLanguage1 | LANGUAGE | — | — |
| 3 | PrjEnterpriseResourcePEOResourceId | RESOURCE_ID | — | — |

### [[pjt_proj_plan_lines|PJT_PROJ_PLAN_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjPlanLinePEOCreatedBy | CREATED_BY | — | — |
| 2 | ProjPlanLinePEOId | ID | — | — |
| 3 | ProjPlanLinePEOPlanLineId | PLAN_LINE_ID | — | — |
| 4 | ProjPlanLinePEOProgressStatusCode | PROGRESS_STATUS_CODE | — | ✅ |
| 5 | ProjPlanLinePEORollupFlag | ROLLUP_FLAG | — | — |
| 6 | ProjPlanLinePEORollupPlanLine | ROLLUP_PLAN_LINE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
