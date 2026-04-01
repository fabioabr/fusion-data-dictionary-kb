---
id: DOC-HCM-PVO-PjrAssignmentPVO
doc_type: system-doc
title: "PjrAssignmentPVO — PVO Human Capital Management"
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
  - PjrAssignmentPVO
  - pjrassignmentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PjrAssignmentPVO

## 📌 Visão Geral

Extrai atribuições de recursos a projetos (Project Resource Management), com tipo de alocação, taxa de cobrança e moeda. Suporta planejamento de capacidade e staffing de projetos.

**Caminho:** `FscmTopModelAM.PjrAssignmentAM.PjrAssignmentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 41 | 1 | 1 | 28 | 68% |

---

## 🔗 Tabelas Relacionadas

- [[pjr_assignment|PJR_ASSIGNMENT]] — 41 atributos (1 PKs, 28 BICC)

---

## ⚙️ Atributos

### [[pjr_assignment|PJR_ASSIGNMENT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignId | ASSIGN_ID | 🔑 | ✅ |
| 2 | AssignmentPEOAssignmentName | ASSIGNMENT_NAME | — | — |
| 3 | PjrAssignmentPEOAdjustType | ADJUST_TYPE | — | — |
| 4 | PjrAssignmentPEOAssignDetails | ASSIGN_DETAILS | — | ✅ |
| 5 | PjrAssignmentPEOAssignmentTypeCode | ASSIGNMENT_TYPE | — | ✅ |
| 6 | PjrAssignmentPEOBillRate | BILL_RATE | — | — |
| 7 | PjrAssignmentPEOBillRateCurrCode | BILL_RATE_CURR_CODE | — | ✅ |
| 8 | PjrAssignmentPEOBillablePercent | BILLABLE_PERCENT | — | ✅ |
| 9 | PjrAssignmentPEOBillablePercentReasonCode | BILLABLE_PERCENT_REASON_CODE | — | ✅ |
| 10 | PjrAssignmentPEOCanceledByResourceId | CANCELED_BY_RESOURCE_ID | — | — |
| 11 | PjrAssignmentPEOCancellationDate | CANCELLATION_DATE | — | ✅ |
| 12 | PjrAssignmentPEOCancellationReason | CANCELLATION_REASON | — | ✅ |
| 13 | PjrAssignmentPEOCostRate | COST_RATE | — | — |
| 14 | PjrAssignmentPEOCostRateCurrCode | COST_RATE_CURR_CODE | — | ✅ |
| 15 | PjrAssignmentPEOCreatedBy | CREATED_BY | — | ✅ |
| 16 | PjrAssignmentPEOCreationDate | CREATION_DATE | — | ✅ |
| 17 | PjrAssignmentPEOEndDate | END_DATE | — | ✅ |
| 18 | PjrAssignmentPEOHoursPerDay | HOURS_PER_DAY | — | ✅ |
| 19 | PjrAssignmentPEOHoursPerDay1 | HOURS_PER_DAY1 | — | ✅ |
| 20 | PjrAssignmentPEOHoursPerDay2 | HOURS_PER_DAY2 | — | ✅ |
| 21 | PjrAssignmentPEOHoursPerDay3 | HOURS_PER_DAY3 | — | ✅ |
| 22 | PjrAssignmentPEOHoursPerDay4 | HOURS_PER_DAY4 | — | ✅ |
| 23 | PjrAssignmentPEOHoursPerDay5 | HOURS_PER_DAY5 | — | ✅ |
| 24 | PjrAssignmentPEOHoursPerDay6 | HOURS_PER_DAY6 | — | ✅ |
| 25 | PjrAssignmentPEOHoursPerDay7 | HOURS_PER_DAY7 | — | ✅ |
| 26 | PjrAssignmentPEOHoursPerInterval | HOURS_PER_INTERVAL | — | ✅ |
| 27 | PjrAssignmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | PjrAssignmentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 29 | PjrAssignmentPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 30 | PjrAssignmentPEOLocation | LOCATION | — | — |
| 31 | PjrAssignmentPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 32 | PjrAssignmentPEOProjectId | PROJECT_ID | — | — |
| 33 | PjrAssignmentPEOProjectRoleId | PROJECT_ROLE_ID | — | — |
| 34 | PjrAssignmentPEORequesterId | REQUESTER_ID | — | — |
| 35 | PjrAssignmentPEOReservationExpirationDate | RESERVATION_EXPIRATION_DATE | — | ✅ |
| 36 | PjrAssignmentPEOReservationReasonCode | RESERVATION_REASON_CODE | — | ✅ |
| 37 | PjrAssignmentPEOResourceId | RESOURCE_ID | — | — |
| 38 | PjrAssignmentPEOStaffingOwnerId | STAFFING_OWNER_ID | — | — |
| 39 | PjrAssignmentPEOStartDate | START_DATE | — | ✅ |
| 40 | PjrAssignmentPEOStatusCode | STATUS_CODE | — | ✅ |
| 41 | PjrAssignmentPEOUseProjCalendarHourFlag | USE_PROJ_CALENDAR_HOUR_FLAG | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
