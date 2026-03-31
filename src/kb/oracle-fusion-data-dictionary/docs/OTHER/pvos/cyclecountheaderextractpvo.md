---
id: DOC-OTHER-PVO-CycleCountHeaderExtractPVO
doc_type: system-doc
title: "CycleCountHeaderExtractPVO — PVO Cross-Module"
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
  - CycleCountHeaderExtractPVO
  - cyclecountheaderextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CycleCountHeaderExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cycle Count Header Extract. Acessa as tabelas: INV_CYCLE_COUNT_HEADERS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.InvBiccExtractAM.CycleCountHeaderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 46 | 1 | 1 | 46 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[inv_cycle_count_headers|INV_CYCLE_COUNT_HEADERS]] — 46 atributos (1 PKs, 46 BICC)

---

## ⚙️ Atributos

### [[inv_cycle_count_headers|INV_CYCLE_COUNT_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvCycleCountHeaderPEOAbcAssignmentGroupId | ABC_ASSIGNMENT_GROUP_ID | — | ✅ |
| 2 | InvCycleCountHeaderPEOAbcInitializationStatus | ABC_INITIALIZATION_STATUS | — | ✅ |
| 3 | InvCycleCountHeaderPEOAllowSerialItems | ALLOW_SERIAL_ITEMS | — | ✅ |
| 4 | InvCycleCountHeaderPEOApprovalOptionCode | APPROVAL_OPTION_CODE | — | ✅ |
| 5 | InvCycleCountHeaderPEOApprovalRequired | APPROVAL_REQUIRED | — | ✅ |
| 6 | InvCycleCountHeaderPEOApprovalToleranceNegative | APPROVAL_TOLERANCE_NEGATIVE | — | ✅ |
| 7 | InvCycleCountHeaderPEOApprovalTolerancePositive | APPROVAL_TOLERANCE_POSITIVE | — | ✅ |
| 8 | InvCycleCountHeaderPEOAutoscheduleEnabledFlag | AUTOSCHEDULE_ENABLED_FLAG | — | ✅ |
| 9 | InvCycleCountHeaderPEOContainerAdjustmentOption | CONTAINER_ADJUSTMENT_OPTION | — | ✅ |
| 10 | InvCycleCountHeaderPEOContainerDiscrepancyOption | CONTAINER_DISCREPANCY_OPTION | — | ✅ |
| 11 | InvCycleCountHeaderPEOContainerEnabledFlag | CONTAINER_ENABLED_FLAG | — | ✅ |
| 12 | InvCycleCountHeaderPEOCostToleranceNegative | COST_TOLERANCE_NEGATIVE | — | ✅ |
| 13 | InvCycleCountHeaderPEOCostTolerancePositive | COST_TOLERANCE_POSITIVE | — | ✅ |
| 14 | InvCycleCountHeaderPEOCreatedBy | CREATED_BY | — | ✅ |
| 15 | InvCycleCountHeaderPEOCreationDate | CREATION_DATE | — | ✅ |
| 16 | InvCycleCountHeaderPEOCycleCountHeaderId | CYCLE_COUNT_HEADER_ID | 🔑 | ✅ |
| 17 | InvCycleCountHeaderPEOCycleCountHeaderName | CYCLE_COUNT_HEADER_NAME | — | ✅ |
| 18 | InvCycleCountHeaderPEODaysUntilLate | DAYS_UNTIL_LATE | — | ✅ |
| 19 | InvCycleCountHeaderPEODefaultApprover | DEFAULT_APPROVER | — | ✅ |
| 20 | InvCycleCountHeaderPEODescription | DESCRIPTION | — | ✅ |
| 21 | InvCycleCountHeaderPEOEndDate | END_DATE | — | ✅ |
| 22 | InvCycleCountHeaderPEOHeaderLastScheduleDate | HEADER_LAST_SCHEDULE_DATE | — | ✅ |
| 23 | InvCycleCountHeaderPEOHeaderNextScheduleDate | HEADER_NEXT_SCHEDULE_DATE | — | ✅ |
| 24 | InvCycleCountHeaderPEOHitMissToleranceNegative | HIT_MISS_TOLERANCE_NEGATIVE | — | ✅ |
| 25 | InvCycleCountHeaderPEOHitMissTolerancePositive | HIT_MISS_TOLERANCE_POSITIVE | — | ✅ |
| 26 | InvCycleCountHeaderPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 27 | InvCycleCountHeaderPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 28 | InvCycleCountHeaderPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 29 | InvCycleCountHeaderPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 30 | InvCycleCountHeaderPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 31 | InvCycleCountHeaderPEOMaximumAutoRecounts | MAXIMUM_AUTO_RECOUNTS | — | ✅ |
| 32 | InvCycleCountHeaderPEONextUserCountSequence | NEXT_USER_COUNT_SEQUENCE | — | ✅ |
| 33 | InvCycleCountHeaderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 34 | InvCycleCountHeaderPEOOnhandVisibleFlag | ONHAND_VISIBLE_FLAG | — | ✅ |
| 35 | InvCycleCountHeaderPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 36 | InvCycleCountHeaderPEOOverrideDefaultApprover | OVERRIDE_DEFAULT_APPROVER | — | ✅ |
| 37 | InvCycleCountHeaderPEORequestId | REQUEST_ID | — | ✅ |
| 38 | InvCycleCountHeaderPEOScheduleIntervalTime | SCHEDULE_INTERVAL_TIME | — | ✅ |
| 39 | InvCycleCountHeaderPEOSerialAdjustmentOption | SERIAL_ADJUSTMENT_OPTION | — | ✅ |
| 40 | InvCycleCountHeaderPEOSerialCountOption | SERIAL_COUNT_OPTION | — | ✅ |
| 41 | InvCycleCountHeaderPEOSerialDetailOption | SERIAL_DETAIL_OPTION | — | ✅ |
| 42 | InvCycleCountHeaderPEOSerialDiscrepancyOption | SERIAL_DISCREPANCY_OPTION | — | ✅ |
| 43 | InvCycleCountHeaderPEOStartDate | START_DATE | — | ✅ |
| 44 | InvCycleCountHeaderPEOUnscheduledCountEntry | UNSCHEDULED_COUNT_ENTRY | — | ✅ |
| 45 | InvCycleCountHeaderPEOWorkdaySchedule | WORKDAY_SCHEDULE | — | ✅ |
| 46 | InvCycleCountHeaderPEOZeroCountFlag | ZERO_COUNT_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
