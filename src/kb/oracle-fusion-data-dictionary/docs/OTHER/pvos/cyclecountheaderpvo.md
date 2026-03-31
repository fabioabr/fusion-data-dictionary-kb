---
id: DOC-OTHER-PVO-CycleCountHeaderPVO
doc_type: system-doc
title: "CycleCountHeaderPVO — PVO Cross-Module"
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
  - CycleCountHeaderPVO
  - cyclecountheaderpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CycleCountHeaderPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cycle Count Header. Acessa as tabelas: INV_ABC_ASSIGNMENT_GROUPS, INV_CYCLE_COUNT_HEADERS, ZMM_SR_SCHEDULES_VL.

**Caminho:** `FscmTopModelAM.InventoryAM.CycleCountHeaderPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 53 | 3 | 1 | 31 | 58% |

---

## 🔗 Tabelas Relacionadas

- [[inv_abc_assignment_groups|INV_ABC_ASSIGNMENT_GROUPS]] — 3 atributos (1 BICC)
- [[inv_cycle_count_headers|INV_CYCLE_COUNT_HEADERS]] — 47 atributos (1 PKs, 29 BICC)
- [[zmm_sr_schedules_vl|ZMM_SR_SCHEDULES_VL]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[inv_abc_assignment_groups|INV_ABC_ASSIGNMENT_GROUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbcAssignmentGroupPEOAssignmentGroupId | ASSIGNMENT_GROUP_ID | — | — |
| 2 | AbcAssignmentGroupPEOAssignmentGroupName | ASSIGNMENT_GROUP_NAME | — | ✅ |
| 3 | AbcAssignmentGroupPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[inv_cycle_count_headers|INV_CYCLE_COUNT_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbcAssignmentGroupId | ABC_ASSIGNMENT_GROUP_ID | — | — |
| 2 | AbcInitializationStatus | ABC_INITIALIZATION_STATUS | — | — |
| 3 | AllowSerialItems | ALLOW_SERIAL_ITEMS | — | ✅ |
| 4 | ApprovalOptionCode | APPROVAL_OPTION_CODE | — | — |
| 5 | ApprovalRequired | APPROVAL_REQUIRED | — | ✅ |
| 6 | ApprovalToleranceNegative | APPROVAL_TOLERANCE_NEGATIVE | — | ✅ |
| 7 | ApprovalTolerancePositive | APPROVAL_TOLERANCE_POSITIVE | — | ✅ |
| 8 | AutoscheduleEnabledFlag | AUTOSCHEDULE_ENABLED_FLAG | — | ✅ |
| 9 | ContainerAdjustmentOption | CONTAINER_ADJUSTMENT_OPTION | — | — |
| 10 | ContainerDiscrepancyOption | CONTAINER_DISCREPANCY_OPTION | — | — |
| 11 | ContainerEnabledFlag | CONTAINER_ENABLED_FLAG | — | — |
| 12 | CostToleranceNegative | COST_TOLERANCE_NEGATIVE | — | ✅ |
| 13 | CostTolerancePositive | COST_TOLERANCE_POSITIVE | — | ✅ |
| 14 | CreatedBy | CREATED_BY | — | ✅ |
| 15 | CreationDate | CREATION_DATE | — | ✅ |
| 16 | CycleCountHeaderId | CYCLE_COUNT_HEADER_ID | 🔑 | ✅ |
| 17 | CycleCountHeaderName | CYCLE_COUNT_HEADER_NAME | — | ✅ |
| 18 | DaysUntilLate | DAYS_UNTIL_LATE | — | ✅ |
| 19 | DefaultApprover | DEFAULT_APPROVER | — | — |
| 20 | Description | DESCRIPTION | — | ✅ |
| 21 | EndDate | END_DATE | — | — |
| 22 | HeaderLastScheduleDate | HEADER_LAST_SCHEDULE_DATE | — | — |
| 23 | HeaderNextScheduleDate | HEADER_NEXT_SCHEDULE_DATE | — | — |
| 24 | HitMissToleranceNegative | HIT_MISS_TOLERANCE_NEGATIVE | — | ✅ |
| 25 | HitMissTolerancePositive | HIT_MISS_TOLERANCE_POSITIVE | — | ✅ |
| 26 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 27 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 28 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 29 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 30 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 31 | MaximumAutoRecounts | MAXIMUM_AUTO_RECOUNTS | — | ✅ |
| 32 | NextUserCountSequence | NEXT_USER_COUNT_SEQUENCE | — | ✅ |
| 33 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 34 | OnhandVisibleFlag | ONHAND_VISIBLE_FLAG | — | ✅ |
| 35 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 36 | OverrideDefaultApprover | OVERRIDE_DEFAULT_APPROVER | — | — |
| 37 | RequestId | REQUEST_ID | — | — |
| 38 | ScheduleIntervalTime | SCHEDULE_INTERVAL_TIME | — | ✅ |
| 39 | SerialAdjustmentOption | SERIAL_ADJUSTMENT_OPTION | — | ✅ |
| 40 | SerialCountOption | SERIAL_COUNT_OPTION | — | ✅ |
| 41 | SerialDetailOption | SERIAL_DETAIL_OPTION | — | ✅ |
| 42 | SerialDiscrepancyOption | SERIAL_DISCREPANCY_OPTION | — | ✅ |
| 43 | StartDate | START_DATE | — | — |
| 44 | StartManualCountsPrefix | START_MANUAL_COUNTS_PREFIX | — | ✅ |
| 45 | UnscheduledCountEntry | UNSCHEDULED_COUNT_ENTRY | — | ✅ |
| 46 | WorkdaySchedule | WORKDAY_SCHEDULE | — | — |
| 47 | ZeroCountFlag | ZERO_COUNT_FLAG | — | ✅ |

### [[zmm_sr_schedules_vl|ZMM_SR_SCHEDULES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ScheduleEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | ScheduleEOScheduleId | SCHEDULE_ID | — | — |
| 3 | ScheduleEOScheduleName | SCHEDULE_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
