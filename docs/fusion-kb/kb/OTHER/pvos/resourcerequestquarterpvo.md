---
id: DOC-OTHER-PVO-ResourceRequestQuarterPVO
doc_type: system-doc
title: "ResourceRequestQuarterPVO — PVO Cross-Module"
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
  - ResourceRequestQuarterPVO
  - resourcerequestquarterpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ResourceRequestQuarterPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Resource Request Quarter. Acessa as tabelas: FND_CAL_QUARTER, PJF_PROJECTS_ALL_VL, PJR_RESOURCE_REQUESTS (+1).

**Caminho:** `FscmTopModelAM.PjrResourceRequestAM.ResourceRequestQuarterPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 65 | 4 | 2 | 34 | 52% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_cal_quarter|FND_CAL_QUARTER]] — 3 atributos (1 PKs, 1 BICC)
- [[pjf_projects_all_vl|PJF_PROJECTS_ALL_VL]] — 4 atributos
- [[pjr_resource_requests|PJR_RESOURCE_REQUESTS]] — 48 atributos (1 PKs, 33 BICC)
- [[pjr_resource_request_schedules|PJR_RESOURCE_REQUEST_SCHEDULES]] — 10 atributos

---

## ⚙️ Atributos

### [[fnd_cal_quarter|FND_CAL_QUARTER]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CalQtrEndDate | CAL_QTR_END_DATE | — | — |
| 2 | CalQtrStartDate | CAL_QTR_START_DATE | — | — |
| 3 | CalQuarter | CAL_QUARTER | 🔑 | ✅ |

### [[pjf_projects_all_vl|PJF_PROJECTS_ALL_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 2 | ProjectPEOCarryingOutOrganizationId | CARRYING_OUT_ORGANIZATION_ID | — | — |
| 3 | ProjectPEOOrgId | ORG_ID | — | — |
| 4 | ProjectPEOProjectId1_1_1 | PROJECT_ID | — | — |

### [[pjr_resource_requests|PJR_RESOURCE_REQUESTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustmentComment | ADJUSTMENT_COMMENT | — | — |
| 2 | AdjustmentReason | ADJUSTMENT_REASON | — | — |
| 3 | AssignedQuantity | ASSIGNED_QUANTITY | — | ✅ |
| 4 | AssignmentTypeCode | ASSIGNMENT_TYPE | — | ✅ |
| 5 | BillablePercent | BILLABLE_PERCENT | — | ✅ |
| 6 | BillablePercentReasonCode | BILLABLE_PERCENT_REASON_CODE | — | ✅ |
| 7 | CanceledByResourceId | CANCELED_BY_RESOURCE_ID | — | — |
| 8 | CancellationDate | CANCELLATION_DATE | — | ✅ |
| 9 | CancellationReason | CANCELLATION_REASON | — | ✅ |
| 10 | CreatedBy | CREATED_BY | — | — |
| 11 | CreationDate | CREATION_DATE | — | — |
| 12 | FulfilledDate | FULFILLED_DATE | — | ✅ |
| 13 | HoursPerDay | HOURS_PER_DAY | — | ✅ |
| 14 | HoursPerDay1 | HOURS_PER_DAY1 | — | ✅ |
| 15 | HoursPerDay2 | HOURS_PER_DAY2 | — | ✅ |
| 16 | HoursPerDay3 | HOURS_PER_DAY3 | — | ✅ |
| 17 | HoursPerDay4 | HOURS_PER_DAY4 | — | ✅ |
| 18 | HoursPerDay5 | HOURS_PER_DAY5 | — | ✅ |
| 19 | HoursPerDay6 | HOURS_PER_DAY6 | — | ✅ |
| 20 | HoursPerDay7 | HOURS_PER_DAY7 | — | ✅ |
| 21 | HoursPerInterval | HOURS_PER_INTERVAL | — | ✅ |
| 22 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 24 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 25 | Location | LOCATION | — | ✅ |
| 26 | Name | NAME | — | ✅ |
| 27 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 28 | OrigRequestedResourceId | ORIG_REQUESTED_RESOURCEID | — | — |
| 29 | ProjectId | PROJECT_ID | — | — |
| 30 | ProjectRoleId | PROJECT_ROLE_ID | — | — |
| 31 | ProposedQuantity | PROPOSED_QUANTITY | — | ✅ |
| 32 | RemainingQuantity | REMAINING_QUANTITY | — | ✅ |
| 33 | RequestSource | REQUEST_SOURCE | — | — |
| 34 | RequestedQuantity | REQUESTED_QUANTITY | — | ✅ |
| 35 | RequesterId | REQUESTER_ID | — | — |
| 36 | ResourceProposedDate | RESOURCE_PROPOSED_DATE | — | — |
| 37 | ResourceRequestId | RESOURCE_REQUEST_ID | 🔑 | ✅ |
| 38 | SpecialInstructions | SPECIAL_INSTRUCTIONS | — | ✅ |
| 39 | StaffingOwnerId | STAFFING_OWNER_ID | — | — |
| 40 | StaffingRemarks | STAFFING_REMARKS | — | ✅ |
| 41 | StatusCode | STATUS_CODE | — | ✅ |
| 42 | SubmittedDate | SUBMITTED_DATE | — | ✅ |
| 43 | TargetBillRate | TARGET_BILL_RATE | — | ✅ |
| 44 | TargetBillRateCurrCode | TARGET_BILL_RATE_CURR_CODE | — | ✅ |
| 45 | TargetCostRate | TARGET_COST_RATE | — | ✅ |
| 46 | TargetCostRateCurrCode | TARGET_COST_RATE_CURR_CODE | — | ✅ |
| 47 | TypeCode | TYPE_CODE | — | ✅ |
| 48 | UseProjCalendarHourFlag | USE_PROJ_CALENDAR_HOUR_FLAG | — | ✅ |

### [[pjr_resource_request_schedules|PJR_RESOURCE_REQUEST_SCHEDULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequestSchedulesPEOCreatedBy | CREATED_BY | — | — |
| 2 | RequestSchedulesPEOCreationDate | CREATION_DATE | — | — |
| 3 | RequestSchedulesPEOIntervalName | INTERVAL_NAME | — | — |
| 4 | RequestSchedulesPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 5 | RequestSchedulesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | RequestSchedulesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | RequestSchedulesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | RequestSchedulesPEOResourceRequestId | RESOURCE_REQUEST_ID | — | — |
| 9 | RequestSchedulesPEOResourceRequestScheduleId | RESOURCE_REQUEST_SCHEDULE_ID | — | — |
| 10 | RequestSchedulesPEOUseProjCalendarHourFlag | USE_PROJ_CALENDAR_HOUR_FLAG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
