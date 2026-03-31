---
id: DOC-OTHER-PVO-AvailAssignPVO
doc_type: system-doc
title: "AvailAssignPVO — PVO Cross-Module"
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
  - AvailAssignPVO
  - availassignpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AvailAssignPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Avail Assign. Acessa as tabelas: PJF_PROJECTS_ALL_B, PJR_ASSIGNMENT, PJR_AVAIL_ASSIGN.

**Caminho:** `FscmTopModelAM.PjrAssignmentAM.AvailAssignPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 46 | 3 | 1 | 10 | 22% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 4 atributos
- [[pjr_assignment|PJR_ASSIGNMENT]] — 30 atributos (6 BICC)
- [[pjr_avail_assign|PJR_AVAIL_ASSIGN]] — 12 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectBasePEOCarryingOutOrganizationId | CARRYING_OUT_ORGANIZATION_ID | — | — |
| 2 | ProjectBasePEOOrgId | ORG_ID | — | — |
| 3 | ProjectBasePEOProjectId | PROJECT_ID | — | — |
| 4 | ProjectBasePEOProjectUnitId | PROJECT_UNIT_ID | — | — |

### [[pjr_assignment|PJR_ASSIGNMENT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignId | ASSIGN_ID | — | — |
| 2 | AssignmentPEOAssignmentType | ASSIGNMENT_TYPE | — | ✅ |
| 3 | AssignmentPEOBillablePercent | BILLABLE_PERCENT | — | ✅ |
| 4 | AssignmentPEOBillablePercentReasonCode | BILLABLE_PERCENT_REASON_CODE | — | — |
| 5 | PjrAssignmentPEOAdjustType | ADJUST_TYPE | — | — |
| 6 | PjrAssignmentPEOAssignDetails | ASSIGN_DETAILS | — | — |
| 7 | PjrAssignmentPEOBillRate | BILL_RATE | — | ✅ |
| 8 | PjrAssignmentPEOBillRateCurrCode | BILL_RATE_CURR_CODE | — | — |
| 9 | PjrAssignmentPEOCanceledByResourceId | CANCELED_BY_RESOURCE_ID | — | — |
| 10 | PjrAssignmentPEOCancellationDate | CANCELLATION_DATE | — | — |
| 11 | PjrAssignmentPEOCancellationReason | CANCELLATION_REASON | — | — |
| 12 | PjrAssignmentPEOCostRate | COST_RATE | — | ✅ |
| 13 | PjrAssignmentPEOCostRateCurrCode | COST_RATE_CURR_CODE | — | — |
| 14 | PjrAssignmentPEOCreatedBy | CREATED_BY | — | — |
| 15 | PjrAssignmentPEOCreationDate | CREATION_DATE | — | — |
| 16 | PjrAssignmentPEOEndDate | END_DATE | — | ✅ |
| 17 | PjrAssignmentPEOHoursPerDay | HOURS_PER_DAY | — | — |
| 18 | PjrAssignmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | PjrAssignmentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | PjrAssignmentPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 21 | PjrAssignmentPEOLocation | LOCATION | — | — |
| 22 | PjrAssignmentPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | PjrAssignmentPEOProjectId | PROJECT_ID | — | — |
| 24 | PjrAssignmentPEOProjectRoleId | PROJECT_ROLE_ID | — | — |
| 25 | PjrAssignmentPEORequesterId | REQUESTER_ID | — | — |
| 26 | PjrAssignmentPEOResourceId | RESOURCE_ID | — | — |
| 27 | PjrAssignmentPEOStaffingOwnerId | STAFFING_OWNER_ID | — | — |
| 28 | PjrAssignmentPEOStartDate | START_DATE | — | — |
| 29 | PjrAssignmentPEOStatusCode | STATUS_CODE | — | — |
| 30 | UseProjCalendarHourFlag | USE_PROJ_CALENDAR_HOUR_FLAG | — | — |

### [[pjr_avail_assign|PJR_AVAIL_ASSIGN]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AvailAssignId | AVAIL_ASSIGN_ID | 🔑 | ✅ |
| 2 | PjrAvailAssignPEOAssignId | ASSIGN_ID | — | ✅ |
| 3 | PjrAvailAssignPEOAvailabilityCacheId | AVAILABILITY_CACHE_ID | — | — |
| 4 | PjrAvailAssignPEOCreatedBy | CREATED_BY | — | — |
| 5 | PjrAvailAssignPEOCreationDate | CREATION_DATE | — | — |
| 6 | PjrAvailAssignPEOEntryDay | ENTRY_DAY | — | — |
| 7 | PjrAvailAssignPEOEntryDurationHrs | ENTRY_DURATION_HRS | — | ✅ |
| 8 | PjrAvailAssignPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | PjrAvailAssignPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | PjrAvailAssignPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | PjrAvailAssignPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | PjrAvailAssignPEOResourceId | RESOURCE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
