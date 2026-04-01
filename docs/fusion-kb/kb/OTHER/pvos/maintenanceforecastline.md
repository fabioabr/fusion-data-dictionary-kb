---
id: DOC-OTHER-PVO-MaintenanceForecastLine
doc_type: system-doc
title: "MaintenanceForecastLine — PVO Cross-Module"
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
  - MaintenanceForecastLine
  - maintenanceforecastline
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MaintenanceForecastLine

## 📌 Visão Geral

View Object para extração BICC de dados de Maintenance Forecast Line. Acessa as tabelas: MNT_FORECAST_LINES.

**Caminho:** `FscmTopModelAM.MaintProgramAM.MaintenanceForecastLine`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 1 | 1 | 19 | 63% |

---

## 🔗 Tabelas Relacionadas

- [[mnt_forecast_lines|MNT_FORECAST_LINES]] — 30 atributos (1 PKs, 19 BICC)

---

## ⚙️ Atributos

### [[mnt_forecast_lines|MNT_FORECAST_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ForecastLinePEOAssetId | ASSET_ID | — | ✅ |
| 2 | ForecastLinePEOConditionEventCodeId | CONDITION_EVENT_CODE_ID | — | ✅ |
| 3 | ForecastLinePEOCreatedBy | CREATED_BY | — | — |
| 4 | ForecastLinePEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | ForecastLinePEOCycleInterval | CYCLE_INTERVAL | — | ✅ |
| 6 | ForecastLinePEOForecastDate | FORECAST_DATE | — | ✅ |
| 7 | ForecastLinePEOForecastId | FORECAST_ID | — | ✅ |
| 8 | ForecastLinePEOForecastLineId | FORECAST_LINE_ID | 🔑 | ✅ |
| 9 | ForecastLinePEOForecastMtrReadingValue | FORECAST_MTR_READING_VALUE | — | ✅ |
| 10 | ForecastLinePEOForecastSequence | FORECAST_SEQUENCE | — | ✅ |
| 11 | ForecastLinePEOItemId | ITEM_ID | — | — |
| 12 | ForecastLinePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 13 | ForecastLinePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 14 | ForecastLinePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | ForecastLinePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | ForecastLinePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | ForecastLinePEOMeterDefinitionId | METER_DEFINITION_ID | — | ✅ |
| 18 | ForecastLinePEOMeterId | METER_ID | — | ✅ |
| 19 | ForecastLinePEONextWorkOrderOnlyFlag | NEXT_WORK_ORDER_ONLY_FLAG | — | ✅ |
| 20 | ForecastLinePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | ForecastLinePEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 22 | ForecastLinePEORequestId | REQUEST_ID | — | — |
| 23 | ForecastLinePEORequirementId | REQUIREMENT_ID | — | ✅ |
| 24 | ForecastLinePEORequirementWdId | REQUIREMENT_WD_ID | — | — |
| 25 | ForecastLinePEOSchedulePatternId | SCHEDULE_PATTERN_ID | — | ✅ |
| 26 | ForecastLinePEOSuppressedFlag | SUPPRESSED_FLAG | — | ✅ |
| 27 | ForecastLinePEOWorkDefinitionId | WORK_DEFINITION_ID | — | ✅ |
| 28 | ForecastLinePEOWorkDefinitionVersionId | WORK_DEFINITION_VERSION_ID | — | ✅ |
| 29 | MaintenanceForecastLinePEODayIntervalValue | DAY_INTERVAL_VALUE | — | — |
| 30 | MaintenanceForecastLinePEOMeterUtilizationRate | METER_UTILIZATION_RATE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
