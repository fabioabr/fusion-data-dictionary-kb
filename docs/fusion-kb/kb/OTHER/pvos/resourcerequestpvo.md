---
id: DOC-OTHER-PVO-ResourceRequestPVO
doc_type: system-doc
title: "ResourceRequestPVO — PVO Cross-Module"
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
  - ResourceRequestPVO
  - resourcerequestpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ResourceRequestPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Resource Request. Acessa as tabelas: PJF_PROJECTS_ALL_B, PJR_RESOURCE_REQUESTS.

**Caminho:** `FscmTopModelAM.PjrResourceRequestAM.ResourceRequestPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 56 | 2 | 1 | 39 | 70% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 4 atributos
- [[pjr_resource_requests|PJR_RESOURCE_REQUESTS]] — 52 atributos (1 PKs, 39 BICC)

---

## ⚙️ Atributos

### [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectBasePEOCarryingOutOrganizationId | CARRYING_OUT_ORGANIZATION_ID | — | — |
| 2 | ProjectBasePEOOrgId | ORG_ID | — | — |
| 3 | ProjectBasePEOProjectId | PROJECT_ID | — | — |
| 4 | ProjectBasePEOProjectUnitId | PROJECT_UNIT_ID | — | — |

### [[pjr_resource_requests|PJR_RESOURCE_REQUESTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequestPEOAdjustmentComment | ADJUSTMENT_COMMENT | — | — |
| 2 | RequestPEOAdjustmentReason | ADJUSTMENT_REASON | — | — |
| 3 | RequestPEOAssignedQuantity | ASSIGNED_QUANTITY | — | ✅ |
| 4 | RequestPEOAssignmentTypeCode | ASSIGNMENT_TYPE | — | ✅ |
| 5 | RequestPEOBillablePercent | BILLABLE_PERCENT | — | ✅ |
| 6 | RequestPEOBillablePercentReasonCode | BILLABLE_PERCENT_REASON_CODE | — | ✅ |
| 7 | RequestPEOCanceledByResourceId | CANCELED_BY_RESOURCE_ID | — | — |
| 8 | RequestPEOCancellationDate | CANCELLATION_DATE | — | ✅ |
| 9 | RequestPEOCancellationReason | CANCELLATION_REASON | — | ✅ |
| 10 | RequestPEOCreatedBy | CREATED_BY | — | ✅ |
| 11 | RequestPEOCreationDate | CREATION_DATE | — | ✅ |
| 12 | RequestPEOFinishDate | FINISH_DATE | — | ✅ |
| 13 | RequestPEOFulfilledDate | FULFILLED_DATE | — | ✅ |
| 14 | RequestPEOHoursPerDay | HOURS_PER_DAY | — | ✅ |
| 15 | RequestPEOHoursPerDay1 | HOURS_PER_DAY1 | — | ✅ |
| 16 | RequestPEOHoursPerDay2 | HOURS_PER_DAY2 | — | ✅ |
| 17 | RequestPEOHoursPerDay3 | HOURS_PER_DAY3 | — | ✅ |
| 18 | RequestPEOHoursPerDay4 | HOURS_PER_DAY4 | — | ✅ |
| 19 | RequestPEOHoursPerDay5 | HOURS_PER_DAY5 | — | ✅ |
| 20 | RequestPEOHoursPerDay6 | HOURS_PER_DAY6 | — | ✅ |
| 21 | RequestPEOHoursPerDay7 | HOURS_PER_DAY7 | — | ✅ |
| 22 | RequestPEOHoursPerInterval | HOURS_PER_INTERVAL | — | ✅ |
| 23 | RequestPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | RequestPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 25 | RequestPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 26 | RequestPEOLocation | LOCATION | — | ✅ |
| 27 | RequestPEOName | NAME | — | ✅ |
| 28 | RequestPEONumberOfWorkingDays | NUMBER_OF_WORKING_DAYS | — | — |
| 29 | RequestPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 30 | RequestPEOOrigRequestedResourceId | ORIG_REQUESTED_RESOURCEID | — | — |
| 31 | RequestPEOProjectId | PROJECT_ID | — | — |
| 32 | RequestPEOProjectRoleId | PROJECT_ROLE_ID | — | — |
| 33 | RequestPEOProposedQuantity | PROPOSED_QUANTITY | — | ✅ |
| 34 | RequestPEORemainingQuantity | REMAINING_QUANTITY | — | ✅ |
| 35 | RequestPEORequestSource | REQUEST_SOURCE | — | — |
| 36 | RequestPEORequestedQuantity | REQUESTED_QUANTITY | — | ✅ |
| 37 | RequestPEORequesterId | REQUESTER_ID | — | — |
| 38 | RequestPEOResourceProposedDate | RESOURCE_PROPOSED_DATE | — | — |
| 39 | RequestPEOSpecialInstructions | SPECIAL_INSTRUCTIONS | — | ✅ |
| 40 | RequestPEOStaffingOwnerId | STAFFING_OWNER_ID | — | — |
| 41 | RequestPEOStaffingRemarks | STAFFING_REMARKS | — | ✅ |
| 42 | RequestPEOStartDate | START_DATE | — | ✅ |
| 43 | RequestPEOStatusCode | STATUS_CODE | — | ✅ |
| 44 | RequestPEOSubmittedDate | SUBMITTED_DATE | — | ✅ |
| 45 | RequestPEOTargetBillRate | TARGET_BILL_RATE | — | ✅ |
| 46 | RequestPEOTargetBillRateCurrCode | TARGET_BILL_RATE_CURR_CODE | — | ✅ |
| 47 | RequestPEOTargetCostRate | TARGET_COST_RATE | — | ✅ |
| 48 | RequestPEOTargetCostRateCurrCode | TARGET_COST_RATE_CURR_CODE | — | ✅ |
| 49 | RequestPEOTotalHours | TOTAL_HOURS | — | ✅ |
| 50 | RequestPEOTypeCode | TYPE_CODE | — | ✅ |
| 51 | RequestPEOUseProjCalendarHourFlag | USE_PROJ_CALENDAR_HOUR_FLAG | — | ✅ |
| 52 | ResourceRequestId | RESOURCE_REQUEST_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
