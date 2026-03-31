---
id: DOC-OTHER-PVO-ProgramExtract
doc_type: system-doc
title: "ProgramExtract — PVO Cross-Module"
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
  - ProgramExtract
  - programextract
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProgramExtract

## 📌 Visão Geral

View Object para extração BICC de dados de Program Extract. Acessa as tabelas: MNT_PROGRAMS_EXT.

**Caminho:** `FscmTopModelAM.MaintProgramAM.ProgramExtract`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 59 | 1 | 1 | 3 | 5% |

---

## 🔗 Tabelas Relacionadas

- [[mnt_programs_ext|MNT_PROGRAMS_EXT]] — 59 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[mnt_programs_ext|MNT_PROGRAMS_EXT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetId | ASSET_ID | — | ✅ |
| 2 | AssetItemId | ASSET_ITEM_ID | — | — |
| 3 | AssetItemNumber | ASSET_ITEM_NUMBER | — | — |
| 4 | AssetNumber | ASSET_NUMBER | — | — |
| 5 | BaseInterval | BASE_INTERVAL | — | — |
| 6 | BaseIntervalUomCode | BASE_INTERVAL_UOM_CODE | — | — |
| 7 | CalendarBasedFlag | CALENDAR_BASED_FLAG | — | — |
| 8 | CreatedBy | CREATED_BY | — | — |
| 9 | CreationDate | CREATION_DATE | — | — |
| 10 | DataRowId | DATA_ROW_ID | 🔑 | ✅ |
| 11 | DueAtCycleInterval | DUE_AT_CYCLE_INTERVAL | — | — |
| 12 | ForecastUsingCycleFlag | FORECAST_USING_CYCLE_FLAG | — | — |
| 13 | IntervalsInTheCycle | INTERVALS_IN_THE_CYCLE | — | — |
| 14 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 15 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 16 | LastForecastDate | LAST_FORECAST_DATE | — | — |
| 17 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | MaterialItemId | MATERIAL_ITEM_ID | — | — |
| 21 | MaterialItemNumber | MATERIAL_ITEM_NUMBER | — | — |
| 22 | MaterialQuantity | MATERIAL_QUANTITY | — | — |
| 23 | MaterialSeqNumber | MATERIAL_SEQ_NUMBER | — | — |
| 24 | MaterialUomCode | MATERIAL_UOM_CODE | — | — |
| 25 | MeterBasedFlag | METER_BASED_FLAG | — | — |
| 26 | MeterDefinitionId | METER_DEFINITION_ID | — | — |
| 27 | MeterId | METER_ID | — | — |
| 28 | MeterName | METER_NAME | — | — |
| 29 | NextForecastDueByCode | NEXT_FORECAST_DUE_BY_CODE | — | — |
| 30 | OrganizationCode | ORGANIZATION_CODE | — | — |
| 31 | OrganizationId | ORGANIZATION_ID | — | — |
| 32 | ProgramCode | PROGRAM_CODE | — | — |
| 33 | ProgramId | PROGRAM_ID | — | — |
| 34 | ProgramName | PROGRAM_NAME | — | — |
| 35 | ProgramOvn | PROGRAM_OVN | — | — |
| 36 | ReliabilityRate | RELIABILITY_RATE | — | — |
| 37 | RepeatsInCycleFlag | REPEATS_IN_CYCLE_FLAG | — | — |
| 38 | RequestId | REQUEST_ID | — | — |
| 39 | RequirementId | REQUIREMENT_ID | — | — |
| 40 | RequirementMeterId | REQUIREMENT_METER_ID | — | — |
| 41 | RequirementName | REQUIREMENT_NAME | — | — |
| 42 | RequirementOvn | REQUIREMENT_OVN | — | — |
| 43 | RequirementWdId | REQUIREMENT_WD_ID | — | — |
| 44 | RunId | RUN_ID | — | — |
| 45 | ScheduleDuration | SCHEDULE_DURATION | — | — |
| 46 | ScheduleDurationUomCode | SCHEDULE_DURATION_UOM_CODE | — | — |
| 47 | SchedulePatternId | SCHEDULE_PATTERN_ID | — | — |
| 48 | SchedulePatternName | SCHEDULE_PATTERN_NAME | — | — |
| 49 | UtilizationRate | UTILIZATION_RATE | — | — |
| 50 | WdOperationId | WD_OPERATION_ID | — | — |
| 51 | WdOperationMaterialId | WD_OPERATION_MATERIAL_ID | — | — |
| 52 | WdOperationName | WD_OPERATION_NAME | — | — |
| 53 | WdOperationSeqNumber | WD_OPERATION_SEQ_NUMBER | — | — |
| 54 | WorkCenterCode | WORK_CENTER_CODE | — | — |
| 55 | WorkCenterId | WORK_CENTER_ID | — | — |
| 56 | WorkCenterName | WORK_CENTER_NAME | — | — |
| 57 | WorkDefinitionCode | WORK_DEFINITION_CODE | — | — |
| 58 | WorkDefinitionId | WORK_DEFINITION_ID | — | — |
| 59 | WorkDefinitionName | WORK_DEFINITION_NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
