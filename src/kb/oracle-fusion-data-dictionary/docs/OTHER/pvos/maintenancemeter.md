---
id: DOC-OTHER-PVO-MaintenanceMeter
doc_type: system-doc
title: "MaintenanceMeter — PVO Cross-Module"
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
  - MaintenanceMeter
  - maintenancemeter
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MaintenanceMeter

## 📌 Visão Geral

View Object para extração BICC de dados de Maintenance Meter. Acessa as tabelas: CSE_METERS, CSE_METER_DEFINITIONS_B, CSE_METER_DEFINITIONS_TL (+2).

**Caminho:** `FscmTopModelAM.MaintProgramAM.MaintenanceMeter`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 116 | 5 | 1 | 33 | 28% |

---

## 🔗 Tabelas Relacionadas

- [[cse_meters|CSE_METERS]] — 25 atributos (7 BICC)
- [[cse_meter_definitions_b|CSE_METER_DEFINITIONS_B]] — 32 atributos (16 BICC)
- [[cse_meter_definitions_tl|CSE_METER_DEFINITIONS_TL]] — 11 atributos (3 BICC)
- [[cse_meter_readings|CSE_METER_READINGS]] — 28 atributos (1 BICC)
- [[mnt_wr_meters_fact_v|MNT_WR_METERS_FACT_V]] — 20 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[cse_meters|CSE_METERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MeterInstancePEOActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | MeterInstancePEOActiveStartDate | ACTIVE_START_DATE | — | ✅ |
| 3 | MeterInstancePEOAllowInMaintProgramFlag | ALLOW_IN_MAINT_PROGRAM_FLAG | — | — |
| 4 | MeterInstancePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 5 | MeterInstancePEOAvgDailyUtilizationRate | AVG_DAILY_UTILIZATION_RATE | — | ✅ |
| 6 | MeterInstancePEOCorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 7 | MeterInstancePEOCreatedBy | CREATED_BY | — | — |
| 8 | MeterInstancePEOCreationDate | CREATION_DATE | — | — |
| 9 | MeterInstancePEOCurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 10 | MeterInstancePEOCurrencyCode | CURRENCY_CODE | — | — |
| 11 | MeterInstancePEODailyUtilizationRate | DAILY_UTILIZATION_RATE | — | ✅ |
| 12 | MeterInstancePEOInitialReadingValue | INITIAL_READING_VALUE | — | ✅ |
| 13 | MeterInstancePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 14 | MeterInstancePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 15 | MeterInstancePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | MeterInstancePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | MeterInstancePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | MeterInstancePEOMeterDefinitionId | METER_DEFINITION_ID | — | — |
| 19 | MeterInstancePEOMeterId | METER_ID | — | — |
| 20 | MeterInstancePEOMeterObjectId | METER_OBJECT_ID | — | — |
| 21 | MeterInstancePEOMeterUsageCode | METER_USAGE_CODE | — | ✅ |
| 22 | MeterInstancePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | MeterInstancePEORecordAtWoComplCode | RECORD_AT_WO_COMPL_CODE | — | — |
| 24 | MeterInstancePEORequestId | REQUEST_ID | — | — |
| 25 | MeterInstancePEOUtilizationRateComputedAt | UTILIZATION_RATE_COMPUTED_AT | — | — |

### [[cse_meter_definitions_b|CSE_METER_DEFINITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DefinitionBasePEOActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | DefinitionBasePEOActiveStartDate | ACTIVE_START_DATE | — | ✅ |
| 3 | DefinitionBasePEOAllowInMaintProgramFlag | ALLOW_IN_MAINT_PROGRAM_FLAG | — | — |
| 4 | DefinitionBasePEOCorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 5 | DefinitionBasePEOCreatedBy | CREATED_BY | — | — |
| 6 | DefinitionBasePEOCreationDate | CREATION_DATE | — | — |
| 7 | DefinitionBasePEOCurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 8 | DefinitionBasePEOCurrencyCode | CURRENCY_CODE | — | — |
| 9 | DefinitionBasePEODailyUtilizationRate | DAILY_UTILIZATION_RATE | — | — |
| 10 | DefinitionBasePEOInitialReadingValue | INITIAL_READING_VALUE | — | — |
| 11 | DefinitionBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 12 | DefinitionBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 13 | DefinitionBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | DefinitionBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | DefinitionBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | DefinitionBasePEOMeterCode | METER_CODE | — | ✅ |
| 17 | DefinitionBasePEOMeterDefinitionId | METER_DEFINITION_ID | — | — |
| 18 | DefinitionBasePEOMeterTypeCode | METER_TYPE_CODE | — | ✅ |
| 19 | DefinitionBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | DefinitionBasePEOReadingDirection | READING_DIRECTION | — | ✅ |
| 21 | DefinitionBasePEOReadingMaxValue | READING_MAX_VALUE | — | ✅ |
| 22 | DefinitionBasePEOReadingMinValue | READING_MIN_VALUE | — | ✅ |
| 23 | DefinitionBasePEOReadingTypeCode | READING_TYPE_CODE | — | ✅ |
| 24 | DefinitionBasePEORecordAtWoComplCode | RECORD_AT_WO_COMPL_CODE | — | — |
| 25 | DefinitionBasePEORequestId | REQUEST_ID | — | — |
| 26 | DefinitionBasePEOResetAllowedFlag | RESET_ALLOWED_FLAG | — | ✅ |
| 27 | DefinitionBasePEOResetValue | RESET_VALUE | — | ✅ |
| 28 | DefinitionBasePEORolloverAllowedFlag | ROLLOVER_ALLOWED_FLAG | — | ✅ |
| 29 | DefinitionBasePEORolloverMaxValue | ROLLOVER_MAX_VALUE | — | ✅ |
| 30 | DefinitionBasePEORolloverResetValue | ROLLOVER_RESET_VALUE | — | ✅ |
| 31 | DefinitionBasePEOUomCode | UOM_CODE | — | ✅ |
| 32 | DefinitionBasePEOUtilizationRateComputedAt | UTILIZATION_RATE_COMPUTED_AT | — | ✅ |

### [[cse_meter_definitions_tl|CSE_METER_DEFINITIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DefinitionTLPEOCreatedBy | CREATED_BY | — | — |
| 2 | DefinitionTLPEOCreationDate | CREATION_DATE | — | — |
| 3 | DefinitionTLPEOLanguage | LANGUAGE | — | — |
| 4 | DefinitionTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | DefinitionTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | DefinitionTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | DefinitionTLPEOMeterDefinitionId | METER_DEFINITION_ID | — | — |
| 8 | DefinitionTLPEOMeterDescription | METER_DESCRIPTION | — | ✅ |
| 9 | DefinitionTLPEOMeterName | METER_NAME | — | ✅ |
| 10 | DefinitionTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | DefinitionTLPEOSourceLang | SOURCE_LANG | — | — |

### [[cse_meter_readings|CSE_METER_READINGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReadingPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | ReadingPEOComments | COMMENTS | — | — |
| 3 | ReadingPEOCorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 4 | ReadingPEOCreatedBy | CREATED_BY | — | — |
| 5 | ReadingPEOCreationDate | CREATION_DATE | — | — |
| 6 | ReadingPEOCurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 7 | ReadingPEOCurrencyCode | CURRENCY_CODE | — | — |
| 8 | ReadingPEODisabledFlag | DISABLED_FLAG | — | — |
| 9 | ReadingPEODisplayedValue | DISPLAYED_VALUE | — | — |
| 10 | ReadingPEOInitialFlag | INITIAL_FLAG | — | — |
| 11 | ReadingPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 12 | ReadingPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 13 | ReadingPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | ReadingPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | ReadingPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | ReadingPEOMeterId | METER_ID | — | — |
| 17 | ReadingPEOMeterReadingId | METER_READING_ID | — | — |
| 18 | ReadingPEOModifiedFlag | MODIFIED_FLAG | — | — |
| 19 | ReadingPEONetValue | NET_VALUE | — | — |
| 20 | ReadingPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | ReadingPEOReadingDate | READING_DATE | — | — |
| 22 | ReadingPEOReadingNetChange | READING_NET_CHANGE | — | — |
| 23 | ReadingPEOReadingTypeCode | READING_TYPE_CODE | — | — |
| 24 | ReadingPEOReadingValue | READING_VALUE | — | — |
| 25 | ReadingPEORequestId | REQUEST_ID | — | — |
| 26 | ReadingPEOResetFlag | RESET_FLAG | — | — |
| 27 | ReadingPEORolloverFlag | ROLLOVER_FLAG | — | — |
| 28 | ReadingPEOWorkOrderId | WORK_ORDER_ID | — | — |

### [[mnt_wr_meters_fact_v|MNT_WR_METERS_FACT_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MntMeterPEOAssetId | ASSET_ID | — | ✅ |
| 2 | MntMeterPEOBaseInterval | BASE_INTERVAL | — | — |
| 3 | MntMeterPEOCreatedBy | CREATED_BY | — | — |
| 4 | MntMeterPEOCreationDate | CREATION_DATE | — | — |
| 5 | MntMeterPEODisabledFlag | DISABLED_FLAG | — | — |
| 6 | MntMeterPEOItemId | ITEM_ID | — | — |
| 7 | MntMeterPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 8 | MntMeterPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 9 | MntMeterPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | MntMeterPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | MntMeterPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | MntMeterPEOMeterDefinitionId | METER_DEFINITION_ID | — | ✅ |
| 13 | MntMeterPEOMeterId | METER_ID | — | ✅ |
| 14 | MntMeterPEONextForecastDueByCode | NEXT_FORECAST_DUE_BY_CODE | — | ✅ |
| 15 | MntMeterPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | MntMeterPEOOrganizationId | ORGANIZATION_ID | — | — |
| 17 | MntMeterPEORequestId | REQUEST_ID | — | — |
| 18 | MntMeterPEORequirementId | REQUIREMENT_ID | — | — |
| 19 | MntMeterPEORequirementMeterId | REQUIREMENT_METER_ID | 🔑 | ✅ |
| 20 | MntMeterPEORequirementTypeCode | REQUIREMENT_TYPE_CODE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
