---
id: DOC-OTHER-PVO-MaintenanceWorkRequirementRef
doc_type: system-doc
title: "MaintenanceWorkRequirementRef — PVO Cross-Module"
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
  - MaintenanceWorkRequirementRef
  - maintenanceworkrequirementref
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MaintenanceWorkRequirementRef

## 📌 Visão Geral

View Object para extração BICC de dados de Maintenance Work Requirement Ref. Acessa as tabelas: MNT_WORK_REQUIREMENTS_B, MNT_WORK_REQUIREMENTS_TL, WIE_WO_STATUSES_TL.

**Caminho:** `FscmTopModelAM.MaintProgramAM.MaintenanceWorkRequirementRef`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 56 | 3 | 1 | 18 | 32% |

---

## 🔗 Tabelas Relacionadas

- [[mnt_work_requirements_b|MNT_WORK_REQUIREMENTS_B]] — 42 atributos (1 PKs, 16 BICC)
- [[mnt_work_requirements_tl|MNT_WORK_REQUIREMENTS_TL]] — 10 atributos (2 BICC)
- [[wie_wo_statuses_tl|WIE_WO_STATUSES_TL]] — 4 atributos

---

## ⚙️ Atributos

### [[mnt_work_requirements_b|MNT_WORK_REQUIREMENTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BasePEOActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | BasePEOActiveStartDate | ACTIVE_START_DATE | — | ✅ |
| 3 | BasePEOAssetHistoryServiceDate | ASSET_HISTORY_SERVICE_DATE | — | — |
| 4 | BasePEOAssetHistoryServiceInterval | ASSET_HISTORY_SERVICE_INTERVAL | — | — |
| 5 | BasePEOAssetId | ASSET_ID | — | — |
| 6 | BasePEOAssetInclusionTypeCode | ASSET_INCLUSION_TYPE_CODE | — | — |
| 7 | BasePEOCalendarBasedFlag | CALENDAR_BASED_FLAG | — | ✅ |
| 8 | BasePEOConditionBasedFlag | CONDITION_BASED_FLAG | — | ✅ |
| 9 | BasePEOCreateWorkOrderOptionCode | CREATE_WORK_ORDER_OPTION_CODE | — | — |
| 10 | BasePEOCreatedBy | CREATED_BY | — | — |
| 11 | BasePEOCreationDate | CREATION_DATE | — | — |
| 12 | BasePEODayBasedFlag | DAY_BASED_FLAG | — | — |
| 13 | BasePEOFirmPlannedFlag | FIRM_PLANNED_FLAG | — | — |
| 14 | BasePEOForecastUsingCycleFlag | FORECAST_USING_CYCLE_FLAG | — | ✅ |
| 15 | BasePEOForecastWindowInDays | FORECAST_WINDOW_IN_DAYS | — | — |
| 16 | BasePEOIntervalsInTheCycle | INTERVALS_IN_THE_CYCLE | — | ✅ |
| 17 | BasePEOItemId | ITEM_ID | — | — |
| 18 | BasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 19 | BasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 20 | BasePEOLastForecastDate | LAST_FORECAST_DATE | — | ✅ |
| 21 | BasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | BasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 23 | BasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 24 | BasePEOMeterBasedFlag | METER_BASED_FLAG | — | ✅ |
| 25 | BasePEOModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 26 | BasePEONextForecastDueByCode | NEXT_FORECAST_DUE_BY_CODE | — | — |
| 27 | BasePEONextWorkOrderOnlyFlag | NEXT_WORK_ORDER_ONLY_FLAG | — | ✅ |
| 28 | BasePEONumberOfDays | NUMBER_OF_DAYS | — | — |
| 29 | BasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 30 | BasePEOOrganizationId | ORGANIZATION_ID | — | — |
| 31 | BasePEOProgramId | PROGRAM_ID | — | — |
| 32 | BasePEORequestId | REQUEST_ID | — | — |
| 33 | BasePEORequirementId | REQUIREMENT_ID | 🔑 | ✅ |
| 34 | BasePEORequirementReference | REQUIREMENT_REFERENCE | — | — |
| 35 | BasePEORequirementTypeCode | REQUIREMENT_TYPE_CODE | — | ✅ |
| 36 | BasePEOSchedulePatternId | SCHEDULE_PATTERN_ID | — | — |
| 37 | BasePEOStatusCode | STATUS_CODE | — | ✅ |
| 38 | BasePEOSuppressMergeCode | SUPPRESS_MERGE_CODE | — | ✅ |
| 39 | BasePEOSuppressMergeOverrideFlag | SUPPRESS_MERGE_OVERRIDE_FLAG | — | ✅ |
| 40 | BasePEOWorkOrderPriority | WORK_ORDER_PRIORITY | — | — |
| 41 | BasePEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | — |
| 42 | BasePEOWorkOrderWindowInDays | WORK_ORDER_WINDOW_IN_DAYS | — | — |

### [[mnt_work_requirements_tl|MNT_WORK_REQUIREMENTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TLPEOCreatedBy | CREATED_BY | — | — |
| 2 | TLPEOCreationDate | CREATION_DATE | — | — |
| 3 | TLPEOLanguage | LANGUAGE | — | — |
| 4 | TLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | TLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | TLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | TLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | TLPEORequirementId | REQUIREMENT_ID | — | — |
| 9 | TLPEORequirementName | REQUIREMENT_NAME | — | ✅ |
| 10 | TLPEOSourceLang | SOURCE_LANG | — | — |

### [[wie_wo_statuses_tl|WIE_WO_STATUSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WOStatusTLPEOLanguage | LANGUAGE | — | — |
| 2 | WOStatusTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | WOStatusTLPEOWoStatusId | WO_STATUS_ID | — | — |
| 4 | WOStatusTLPEOWoStatusName | WO_STATUS_NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
