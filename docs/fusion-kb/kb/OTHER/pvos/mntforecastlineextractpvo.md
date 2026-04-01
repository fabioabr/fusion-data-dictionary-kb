---
id: DOC-OTHER-PVO-MntForecastLineExtractPVO
doc_type: system-doc
title: "MntForecastLineExtractPVO — PVO Cross-Module"
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
  - MntForecastLineExtractPVO
  - mntforecastlineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MntForecastLineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Mnt Forecast Line Extract. Acessa as tabelas: MNT_FORECAST_LINES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.MntBiccExtractAM.MntForecastLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 1 | 1 | 28 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[mnt_forecast_lines|MNT_FORECAST_LINES]] — 28 atributos (1 PKs, 28 BICC)

---

## ⚙️ Atributos

### [[mnt_forecast_lines|MNT_FORECAST_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetId | ASSET_ID | — | ✅ |
| 2 | ConditionEventCodeId | CONDITION_EVENT_CODE_ID | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | CycleInterval | CYCLE_INTERVAL | — | ✅ |
| 6 | ForecastDate | FORECAST_DATE | — | ✅ |
| 7 | ForecastId | FORECAST_ID | — | ✅ |
| 8 | ForecastLineId | FORECAST_LINE_ID | 🔑 | ✅ |
| 9 | ForecastMtrReadingValue | FORECAST_MTR_READING_VALUE | — | ✅ |
| 10 | ForecastSequence | FORECAST_SEQUENCE | — | ✅ |
| 11 | ItemId | ITEM_ID | — | ✅ |
| 12 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 13 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 14 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 16 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | MeterDefinitionId | METER_DEFINITION_ID | — | ✅ |
| 18 | MeterId | METER_ID | — | ✅ |
| 19 | NextWorkOrderOnlyFlag | NEXT_WORK_ORDER_ONLY_FLAG | — | ✅ |
| 20 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 21 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 22 | RequestId | REQUEST_ID | — | ✅ |
| 23 | RequirementId | REQUIREMENT_ID | — | ✅ |
| 24 | RequirementWdId | REQUIREMENT_WD_ID | — | ✅ |
| 25 | SchedulePatternId | SCHEDULE_PATTERN_ID | — | ✅ |
| 26 | SuppressedFlag | SUPPRESSED_FLAG | — | ✅ |
| 27 | WorkDefinitionId | WORK_DEFINITION_ID | — | ✅ |
| 28 | WorkDefinitionVersionId | WORK_DEFINITION_VERSION_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
