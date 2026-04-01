---
id: DOC-OTHER-PVO-ResourceRequestLinesPVO
doc_type: system-doc
title: "ResourceRequestLinesPVO — PVO Cross-Module"
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
  - ResourceRequestLinesPVO
  - resourcerequestlinespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ResourceRequestLinesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Resource Request Lines. Acessa as tabelas: PJR_ASSIGNMENT, PJR_RESOURCE_REQUESTS, PJR_RESOURCE_REQUEST_LINES.

**Caminho:** `FscmTopModelAM.PjrResourceRequestAM.ResourceRequestLinesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 113 | 3 | 1 | 18 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[pjr_assignment|PJR_ASSIGNMENT]] — 31 atributos
- [[pjr_resource_requests|PJR_RESOURCE_REQUESTS]] — 47 atributos
- [[pjr_resource_request_lines|PJR_RESOURCE_REQUEST_LINES]] — 35 atributos (1 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[pjr_assignment|PJR_ASSIGNMENT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentPEOAdjustType | ADJUST_TYPE | — | — |
| 2 | AssignmentPEOAssignDetails | ASSIGN_DETAILS | — | — |
| 3 | AssignmentPEOAssignId | ASSIGN_ID | — | — |
| 4 | AssignmentPEOBillRate | BILL_RATE | — | — |
| 5 | AssignmentPEOBillRateCurrCode | BILL_RATE_CURR_CODE | — | — |
| 6 | AssignmentPEOCanceledByResourceId | CANCELED_BY_RESOURCE_ID | — | — |
| 7 | AssignmentPEOCancellationDate | CANCELLATION_DATE | — | — |
| 8 | AssignmentPEOCancellationReason | CANCELLATION_REASON | — | — |
| 9 | AssignmentPEOCostRate | COST_RATE | — | — |
| 10 | AssignmentPEOCostRateCurrCode | COST_RATE_CURR_CODE | — | — |
| 11 | AssignmentPEOEndDate | END_DATE | — | — |
| 12 | AssignmentPEOHoursPerDay | HOURS_PER_DAY | — | — |
| 13 | AssignmentPEOHoursPerDay1 | HOURS_PER_DAY1 | — | — |
| 14 | AssignmentPEOHoursPerDay2 | HOURS_PER_DAY2 | — | — |
| 15 | AssignmentPEOHoursPerDay3 | HOURS_PER_DAY3 | — | — |
| 16 | AssignmentPEOHoursPerDay4 | HOURS_PER_DAY4 | — | — |
| 17 | AssignmentPEOHoursPerDay5 | HOURS_PER_DAY5 | — | — |
| 18 | AssignmentPEOHoursPerDay6 | HOURS_PER_DAY6 | — | — |
| 19 | AssignmentPEOHoursPerDay7 | HOURS_PER_DAY7 | — | — |
| 20 | AssignmentPEOLocation | LOCATION | — | — |
| 21 | AssignmentPEOProjectId | PROJECT_ID | — | — |
| 22 | AssignmentPEOProjectRoleId | PROJECT_ROLE_ID | — | — |
| 23 | AssignmentPEORequesterId | REQUESTER_ID | — | — |
| 24 | AssignmentPEOReservation | RESERVATION | — | — |
| 25 | AssignmentPEOReservationExpirationDate | RESERVATION_EXPIRATION_DATE | — | — |
| 26 | AssignmentPEOReservationReasonCode | RESERVATION_REASON_CODE | — | — |
| 27 | AssignmentPEOResourceId | RESOURCE_ID | — | — |
| 28 | AssignmentPEOStaffingOwnerId | STAFFING_OWNER_ID | — | — |
| 29 | AssignmentPEOStartDate | START_DATE | — | — |
| 30 | AssignmentPEOStatusCode | STATUS_CODE | — | — |
| 31 | AssignmentPEOUseProjCalendarHourFlag | USE_PROJ_CALENDAR_HOUR_FLAG | — | — |

### [[pjr_resource_requests|PJR_RESOURCE_REQUESTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequestPEOAdjustmentComment | ADJUSTMENT_COMMENT | — | — |
| 2 | RequestPEOAdjustmentReason | ADJUSTMENT_REASON | — | — |
| 3 | RequestPEOCanceledByResourceId | CANCELED_BY_RESOURCE_ID | — | — |
| 4 | RequestPEOCancellationDate | CANCELLATION_DATE | — | — |
| 5 | RequestPEOCancellationReason | CANCELLATION_REASON | — | — |
| 6 | RequestPEOCreatedBy | CREATED_BY | — | — |
| 7 | RequestPEOCreationDate | CREATION_DATE | — | — |
| 8 | RequestPEOFinishDate | FINISH_DATE | — | — |
| 9 | RequestPEOFulfilledDate | FULFILLED_DATE | — | — |
| 10 | RequestPEOHoursPerDay | HOURS_PER_DAY | — | — |
| 11 | RequestPEOHoursPerDay1 | HOURS_PER_DAY1 | — | — |
| 12 | RequestPEOHoursPerDay2 | HOURS_PER_DAY2 | — | — |
| 13 | RequestPEOHoursPerDay3 | HOURS_PER_DAY3 | — | — |
| 14 | RequestPEOHoursPerDay4 | HOURS_PER_DAY4 | — | — |
| 15 | RequestPEOHoursPerDay5 | HOURS_PER_DAY5 | — | — |
| 16 | RequestPEOHoursPerDay6 | HOURS_PER_DAY6 | — | — |
| 17 | RequestPEOHoursPerDay7 | HOURS_PER_DAY7 | — | — |
| 18 | RequestPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 19 | RequestPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | RequestPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 21 | RequestPEOLocation | LOCATION | — | — |
| 22 | RequestPEOName | NAME | — | — |
| 23 | RequestPEONumberOfWorkingDays | NUMBER_OF_WORKING_DAYS | — | — |
| 24 | RequestPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 25 | RequestPEOOrigRequestedResourceId | ORIG_REQUESTED_RESOURCEID | — | — |
| 26 | RequestPEOProjectId | PROJECT_ID | — | — |
| 27 | RequestPEOProjectRoleId | PROJECT_ROLE_ID | — | — |
| 28 | RequestPEOProposedQuantity | PROPOSED_QUANTITY | — | — |
| 29 | RequestPEORemainingQuantity | REMAINING_QUANTITY | — | — |
| 30 | RequestPEORequestSource | REQUEST_SOURCE | — | — |
| 31 | RequestPEORequestedQuantity | REQUESTED_QUANTITY | — | — |
| 32 | RequestPEORequesterId | REQUESTER_ID | — | — |
| 33 | RequestPEOResourceRequestId | RESOURCE_REQUEST_ID | — | — |
| 34 | RequestPEOSpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 35 | RequestPEOStaffingOwnerId | STAFFING_OWNER_ID | — | — |
| 36 | RequestPEOStaffingRemarks | STAFFING_REMARKS | — | — |
| 37 | RequestPEOStartDate | START_DATE | — | — |
| 38 | RequestPEOStatusCode | STATUS_CODE | — | — |
| 39 | RequestPEOSubmittedDate | SUBMITTED_DATE | — | — |
| 40 | RequestPEOTargetBillRate | TARGET_BILL_RATE | — | — |
| 41 | RequestPEOTargetBillRateCurrCode | TARGET_BILL_RATE_CURR_CODE | — | — |
| 42 | RequestPEOTargetCostRate | TARGET_COST_RATE | — | — |
| 43 | RequestPEOTargetCostRateCurrCode | TARGET_COST_RATE_CURR_CODE | — | — |
| 44 | RequestPEOTotalHours | TOTAL_HOURS | — | — |
| 45 | RequestPEOTypeCode | TYPE_CODE | — | — |
| 46 | RequestPEOUseProjCalendarHourFlag | USE_PROJ_CALENDAR_HOUR_FLAG | — | — |
| 47 | ResourceProposedDate | RESOURCE_PROPOSED_DATE | — | — |

### [[pjr_resource_request_lines|PJR_RESOURCE_REQUEST_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrigAssignHoursPerInterval | ORIG_ASSIGN_HOURS_PER_INTERVAL | — | ✅ |
| 2 | RLinePEOOrigAssignHoursPerDay1 | ORIG_ASSIGN_HOURS_PER_DAY1 | — | ✅ |
| 3 | RLinePEOOrigAssignHoursPerDay2 | ORIG_ASSIGN_HOURS_PER_DAY2 | — | ✅ |
| 4 | RLinePEOOrigAssignHoursPerDay3 | ORIG_ASSIGN_HOURS_PER_DAY3 | — | ✅ |
| 5 | RLinePEOOrigAssignHoursPerDay4 | ORIG_ASSIGN_HOURS_PER_DAY4 | — | ✅ |
| 6 | RLinePEOOrigAssignHoursPerDay5 | ORIG_ASSIGN_HOURS_PER_DAY5 | — | ✅ |
| 7 | RLinePEOOrigAssignHoursPerDay6 | ORIG_ASSIGN_HOURS_PER_DAY6 | — | ✅ |
| 8 | RLinePEOOrigAssignHoursPerDay7 | ORIG_ASSIGN_HOURS_PER_DAY7 | — | ✅ |
| 9 | RequestLinePEOAssignmentStatus | ASSIGNMENT_STATUS | — | — |
| 10 | RequestLinePEORejectReasonCode | RESOURCE_REJECT_REASON_CODE | — | ✅ |
| 11 | RequestLinesPEOAssignId | ASSIGN_ID | — | — |
| 12 | RequestLinesPEOBillRate | RESOURCE_BILL_RATE | — | — |
| 13 | RequestLinesPEOBillRateCurrCd | RESOURCE_BILL_RATE_CURR_CODE | — | — |
| 14 | RequestLinesPEOCostRate | RESOURCE_COST_RATE | — | — |
| 15 | RequestLinesPEOCostRateCurrCd | RESOURCE_COST_RATE_CURR_CODE | — | — |
| 16 | RequestLinesPEOCreatedBy | CREATED_BY | — | — |
| 17 | RequestLinesPEOCurrentFlag | CURRENT_FLAG | — | — |
| 18 | RequestLinesPEOFulfilledDate | FULFILLED_DATE | — | ✅ |
| 19 | RequestLinesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | RequestLinesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | RequestLinesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 22 | RequestLinesPEONumWkingDays | NUMBER_OF_WORKING_DAYS | — | — |
| 23 | RequestLinesPEOObjectVerNum | OBJECT_VERSION_NUMBER | — | — |
| 24 | RequestLinesPEOOrigAssgnStrtDt | ORIG_ASSIGN_START_DATE | — | ✅ |
| 25 | RequestLinesPEOOrigAssignFinDt | ORIG_ASSIGN_FINISH_DATE | — | ✅ |
| 26 | RequestLinesPEOOrigAssignHrsDy | ORIG_ASSIGN_HOURS_PER_DAY | — | ✅ |
| 27 | RequestLinesPEOOrigAssnCalFlg | ORIG_ASSIGN_USE_CAL_FLAG | — | ✅ |
| 28 | RequestLinesPEOPmRquestedResId | PM_REQUESTED_RESOURCE_ID | — | — |
| 29 | RequestLinesPEORequestId | RESOURCE_REQUEST_ID | — | — |
| 30 | RequestLinesPEOResProposedDt | RESOURCE_PROPOSED_DATE | — | ✅ |
| 31 | RequestLinesPEOResourceId | RESOURCE_ID | — | — |
| 32 | RequestLinesPEOResourceStatus | RESOURCE_STATUS | — | ✅ |
| 33 | RequestLinesPEOStaffingOwnerId | STAFFING_OWNER_ID | — | — |
| 34 | RequestLinesPEOTotalHours | TOTAL_HOURS | — | — |
| 35 | ResourceRequestSeqNumber | RESOURCE_REQUEST_SEQ_NUMBER | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
