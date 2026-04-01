---
id: DOC-OTHER-PVO-MeterDefinitionExtractPVO
doc_type: system-doc
title: "MeterDefinitionExtractPVO — PVO Cross-Module"
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
  - MeterDefinitionExtractPVO
  - meterdefinitionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MeterDefinitionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Meter Definition Extract. Acessa as tabelas: CSE_METER_DEFINITIONS_B, CSE_METER_DEFINITIONS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.MeterDefinitionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 46 | 2 | 3 | 46 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_meter_definitions_b|CSE_METER_DEFINITIONS_B]] — 35 atributos (1 PKs, 35 BICC)
- [[cse_meter_definitions_tl|CSE_METER_DEFINITIONS_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[cse_meter_definitions_b|CSE_METER_DEFINITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | ActiveStartDate | ACTIVE_START_DATE | — | ✅ |
| 3 | AllowInMaintProgramFlag | ALLOW_IN_MAINT_PROGRAM_FLAG | — | ✅ |
| 4 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 5 | CorpCurrencyCode | CORP_CURRENCY_CODE | — | ✅ |
| 6 | CreatedBy | CREATED_BY | — | ✅ |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | CurcyConvRateType | CURCY_CONV_RATE_TYPE | — | ✅ |
| 9 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 10 | DailyUtilizationRate | DAILY_UTILIZATION_RATE | — | ✅ |
| 11 | ForecastUsingDailyRateFlag | FORECAST_USING_DAILY_RATE_FLAG | — | ✅ |
| 12 | InitialReadingValue | INITIAL_READING_VALUE | — | ✅ |
| 13 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 14 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 15 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | MeterCode | METER_CODE | — | ✅ |
| 19 | MeterDefinitionId | METER_DEFINITION_ID | 🔑 | ✅ |
| 20 | MeterTypeCode | METER_TYPE_CODE | — | ✅ |
| 21 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 22 | ReadingDirection | READING_DIRECTION | — | ✅ |
| 23 | ReadingMaxValue | READING_MAX_VALUE | — | ✅ |
| 24 | ReadingMinValue | READING_MIN_VALUE | — | ✅ |
| 25 | ReadingTypeCode | READING_TYPE_CODE | — | ✅ |
| 26 | RecordAtWoComplCode | RECORD_AT_WO_COMPL_CODE | — | ✅ |
| 27 | RequestId | REQUEST_ID | — | ✅ |
| 28 | ResetAllowedFlag | RESET_ALLOWED_FLAG | — | ✅ |
| 29 | ResetValue | RESET_VALUE | — | ✅ |
| 30 | RolloverAllowedFlag | ROLLOVER_ALLOWED_FLAG | — | ✅ |
| 31 | RolloverMaxValue | ROLLOVER_MAX_VALUE | — | ✅ |
| 32 | RolloverResetValue | ROLLOVER_RESET_VALUE | — | ✅ |
| 33 | TemplateUsageCode | TEMPLATE_USAGE_CODE | — | ✅ |
| 34 | UomCode | UOM_CODE | — | ✅ |
| 35 | UtilizationRateComputedAt | UTILIZATION_RATE_COMPUTED_AT | — | ✅ |

### [[cse_meter_definitions_tl|CSE_METER_DEFINITIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MeterDefinitionTranslationCreatedBy | CREATED_BY | — | ✅ |
| 2 | MeterDefinitionTranslationCreationDate | CREATION_DATE | — | ✅ |
| 3 | MeterDefinitionTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 4 | MeterDefinitionTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | MeterDefinitionTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | MeterDefinitionTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | MeterDefinitionTranslationMeterDefinitionId | METER_DEFINITION_ID | 🔑 | ✅ |
| 8 | MeterDefinitionTranslationMeterDescription | METER_DESCRIPTION | — | ✅ |
| 9 | MeterDefinitionTranslationMeterName | METER_NAME | — | ✅ |
| 10 | MeterDefinitionTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | MeterDefinitionTranslationSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
