---
id: DOC-OTHER-PVO-CseMeterExtractPVO
doc_type: system-doc
title: "CseMeterExtractPVO — PVO Cross-Module"
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
  - CseMeterExtractPVO
  - csemeterextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CseMeterExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cse Meter Extract. Acessa as tabelas: CSE_METERS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.CseMeterExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 1 | 1 | 26 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_meters|CSE_METERS]] — 26 atributos (1 PKs, 26 BICC)

---

## ⚙️ Atributos

### [[cse_meters|CSE_METERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | ActiveStartDate | ACTIVE_START_DATE | — | ✅ |
| 3 | AllowInMaintProgramFlag | ALLOW_IN_MAINT_PROGRAM_FLAG | — | ✅ |
| 4 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 5 | AvgDailyUtilizationRate | AVG_DAILY_UTILIZATION_RATE | — | ✅ |
| 6 | CorpCurrencyCode | CORP_CURRENCY_CODE | — | ✅ |
| 7 | CreatedBy | CREATED_BY | — | ✅ |
| 8 | CreationDate | CREATION_DATE | — | ✅ |
| 9 | CurcyConvRateType | CURCY_CONV_RATE_TYPE | — | ✅ |
| 10 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 11 | DailyUtilizationRate | DAILY_UTILIZATION_RATE | — | ✅ |
| 12 | InitialReadingValue | INITIAL_READING_VALUE | — | ✅ |
| 13 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 14 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 15 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | MeterDefinitionId | METER_DEFINITION_ID | — | ✅ |
| 19 | MeterId | METER_ID | 🔑 | ✅ |
| 20 | MeterObjectId | METER_OBJECT_ID | — | ✅ |
| 21 | MeterUsageCode | METER_USAGE_CODE | — | ✅ |
| 22 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 23 | ReadingLockDate | READING_LOCK_DATE | — | ✅ |
| 24 | RecordAtWoComplCode | RECORD_AT_WO_COMPL_CODE | — | ✅ |
| 25 | RequestId | REQUEST_ID | — | ✅ |
| 26 | UtilizationRateComputedAt | UTILIZATION_RATE_COMPUTED_AT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
