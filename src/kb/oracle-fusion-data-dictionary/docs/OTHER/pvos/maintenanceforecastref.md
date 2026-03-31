---
id: DOC-OTHER-PVO-MaintenanceForecastRef
doc_type: system-doc
title: "MaintenanceForecastRef — PVO Cross-Module"
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
  - MaintenanceForecastRef
  - maintenanceforecastref
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MaintenanceForecastRef

## 📌 Visão Geral

View Object para extração BICC de dados de Maintenance Forecast Ref. Acessa as tabelas: MNT_FORECASTS.

**Caminho:** `FscmTopModelAM.MaintProgramAM.MaintenanceForecastRef`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 57 | 1 | 1 | 4 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[mnt_forecasts|MNT_FORECASTS]] — 57 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[mnt_forecasts|MNT_FORECASTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ForecastPEOAssetId | ASSET_ID | — | — |
| 2 | ForecastPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 3 | ForecastPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 4 | ForecastPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 5 | ForecastPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 6 | ForecastPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 7 | ForecastPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 8 | ForecastPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 9 | ForecastPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 10 | ForecastPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 11 | ForecastPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 12 | ForecastPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 13 | ForecastPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 14 | ForecastPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 15 | ForecastPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 16 | ForecastPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 17 | ForecastPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 18 | ForecastPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 19 | ForecastPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 20 | ForecastPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 21 | ForecastPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 22 | ForecastPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 23 | ForecastPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | ForecastPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | ForecastPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | ForecastPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | ForecastPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | ForecastPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 29 | ForecastPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 30 | ForecastPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 31 | ForecastPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 32 | ForecastPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 33 | ForecastPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 34 | ForecastPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 35 | ForecastPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 36 | ForecastPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 37 | ForecastPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 38 | ForecastPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 39 | ForecastPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 40 | ForecastPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 41 | ForecastPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 42 | ForecastPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 43 | ForecastPEOCreatedBy | CREATED_BY | — | — |
| 44 | ForecastPEOCreationDate | CREATION_DATE | — | — |
| 45 | ForecastPEOForecastDate | FORECAST_DATE | — | ✅ |
| 46 | ForecastPEOForecastId | FORECAST_ID | 🔑 | ✅ |
| 47 | ForecastPEOItemId | ITEM_ID | — | — |
| 48 | ForecastPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 49 | ForecastPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 50 | ForecastPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 51 | ForecastPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 52 | ForecastPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 53 | ForecastPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 54 | ForecastPEOOrganizationId | ORGANIZATION_ID | — | — |
| 55 | ForecastPEOProgramId | PROGRAM_ID | — | — |
| 56 | ForecastPEORequestId | REQUEST_ID | — | — |
| 57 | ForecastPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
