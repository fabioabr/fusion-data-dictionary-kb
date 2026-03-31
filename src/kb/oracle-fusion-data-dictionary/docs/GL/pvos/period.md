---
id: DOC-GL-PVO-Period
doc_type: system-doc
title: "Period — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - Period
  - period
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# Period

## 📌 Visão Geral

View Object para extração BICC de dados de Period. Acessa as tabelas: CN_PERIOD_DIMS_ALL_TL.

**Caminho:** `FscmTopModelAM.CalendarAM.Period`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 60 | 1 | 5 | 25 | 42% |

---

## 🔗 Tabelas Relacionadas

- [[cn_period_dims_all_tl|CN_PERIOD_DIMS_ALL_TL]] — 60 atributos (5 PKs, 25 BICC)

---

## ⚙️ Atributos

### [[cn_period_dims_all_tl|CN_PERIOD_DIMS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitId | ORG_ID | — | — |
| 2 | CalPerIntTypeId | CAL_PER_INT_TYPE_ID | — | ✅ |
| 3 | CalPerIntTypeId1 | CAL_PER_INT_TYPE_ID1 | — | — |
| 4 | CalendarId | CALENDAR_ID | 🔑 | ✅ |
| 5 | CalendarId1 | CALENDAR_ID | — | — |
| 6 | CalendarId2 | CALENDAR_ID | — | — |
| 7 | CalendarId3 | CALENDAR_ID | — | — |
| 8 | CalendarId4 | CALENDAR_ID | — | — |
| 9 | CalendarName | CALENDAR_NAME | — | ✅ |
| 10 | CreatedBy | CREATED_BY | — | — |
| 11 | CreationDate | CREATION_DATE | — | — |
| 12 | Description | DESCRIPTION | — | ✅ |
| 13 | EndDate | END_DATE | — | ✅ |
| 14 | ForecastFlag | FORECAST_FLAG | — | ✅ |
| 15 | FreezeFlag | FREEZE_FLAG | — | — |
| 16 | HalfyearTypeId | HALFYEAR_TYPE_ID | — | — |
| 17 | IntervalName | INTERVAL_NAME | — | ✅ |
| 18 | IntervalNumber | QUARTER_NUMBER | — | ✅ |
| 19 | IntervalNumber1 | HALFYEAR_NUMBER | — | ✅ |
| 20 | IntervalTypeId | INTERVAL_TYPE_ID | — | — |
| 21 | IntervalTypeId1 | INTERVAL_TYPE_ID | — | — |
| 22 | IntervalTypeId2 | INTERVAL_TYPE_ID | — | — |
| 23 | Language | TARGET_LANGUAGE | — | ✅ |
| 24 | Language1 | TARGET_LANGUAGE | — | — |
| 25 | Language2 | TARGET_LANGUAGE | — | — |
| 26 | Language3 | TARGET_LANGUAGE | — | — |
| 27 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 29 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 30 | Name | BU_NAME | — | ✅ |
| 31 | NumberPerFiscalYear | NUMBER_PER_FISCAL_YEAR | — | ✅ |
| 32 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 33 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 34 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 35 | ObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 36 | ObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 37 | ObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 38 | ObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |
| 39 | ObjectVersionNumber7 | OBJECT_VERSION_NUMBER | — | — |
| 40 | ObjectVersionNumber8 | OBJECT_VERSION_NUMBER | — | — |
| 41 | ObjectVersionNumber9 | OBJECT_VERSION_NUMBER | — | — |
| 42 | OrgId | ORG_ID | 🔑 | ✅ |
| 43 | OrgId1 | ORG_ID | — | — |
| 44 | OrgId2 | ORG_ID | — | — |
| 45 | PeriodDimId | PERIOD_DIM_ID | — | — |
| 46 | PeriodId | PERIOD_ID | 🔑 | ✅ |
| 47 | PeriodId1 | PERIOD_ID | — | — |
| 48 | PeriodId2 | PERIOD_ID | — | — |
| 49 | PeriodName | PERIOD_NAME | — | ✅ |
| 50 | PeriodNumber | PERIOD_NUMBER | — | ✅ |
| 51 | PeriodStatus | PERIOD_STATUS | — | ✅ |
| 52 | PeriodType | PERIOD_TYPE | — | ✅ |
| 53 | PeriodTypeId | PERIOD_TYPE_ID | 🔑 | ✅ |
| 54 | PeriodTypeId1 | PERIOD_TYPE_ID | 🔑 | ✅ |
| 55 | PeriodYear | PERIOD_YEAR | — | ✅ |
| 56 | ProcessingStatusCode | PROCESSING_STATUS_CODE | — | ✅ |
| 57 | QuarterTypeId | QUARTER_TYPE_ID | — | — |
| 58 | RequestId | REQUEST_ID | — | — |
| 59 | SourceLang | SOURCE_LANGUAGE | — | ✅ |
| 60 | StartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
