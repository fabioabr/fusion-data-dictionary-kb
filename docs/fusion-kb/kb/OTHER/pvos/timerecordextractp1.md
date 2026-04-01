---
id: DOC-OTHER-PVO-TimeRecordExtractP1
doc_type: system-doc
title: "TimeRecordExtractP1 — PVO Cross-Module"
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
  - TimeRecordExtractP1
  - timerecordextractp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimeRecordExtractP1

## 📌 Visão Geral

View Object para extração BICC de dados de Time Record Extract P1. Acessa as tabelas: HWM_TM_REC.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.WfmBiccExtractAM.TimeRecordExtractP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 45 | 1 | 2 | 45 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tm_rec|HWM_TM_REC]] — 45 atributos (2 PKs, 45 BICC)

---

## ⚙️ Atributos

### [[hwm_tm_rec|HWM_TM_REC]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActivityEventTime | ACTIVITY_EVENT_TIME | — | ✅ |
| 2 | ActivityInId | ACTIVITY_IN_ID | — | ✅ |
| 3 | ActivityOutId | ACTIVITY_OUT_ID | — | ✅ |
| 4 | ActivityType | ACTIVITY_TYPE | — | ✅ |
| 5 | ActualDate | ACTUAL_DATE | — | ✅ |
| 6 | CommentText | COMMENT_TEXT | — | ✅ |
| 7 | CreatedBy | CREATED_BY | — | ✅ |
| 8 | CreationDate | CREATION_DATE | — | ✅ |
| 9 | DataSetId | DATA_SET_ID | — | ✅ |
| 10 | DateFrom | DATE_FROM | — | ✅ |
| 11 | DateTo | DATE_TO | — | ✅ |
| 12 | DeleteFlag | DELETE_FLAG | — | ✅ |
| 13 | EnterpriseId | ENTERPRISE_ID | — | ✅ |
| 14 | GrpTypeId | GRP_TYPE_ID | — | ✅ |
| 15 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | LatestVersion | LATEST_VERSION | — | ✅ |
| 19 | LayerCode | LAYER_CODE | — | ✅ |
| 20 | Measure | MEASURE | — | ✅ |
| 21 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 22 | OrderEntered | ORDER_ENTERED | — | ✅ |
| 23 | OriginalTimeRecordId | ORIG_TM_REC_ID | — | ✅ |
| 24 | OriginalTimeRecordVersion | ORIG_TM_REC_VERSION | — | ✅ |
| 25 | PartDate | PART_DATE | — | ✅ |
| 26 | RefDate | REF_DATE | — | ✅ |
| 27 | ResourceId | RESOURCE_ID | — | ✅ |
| 28 | ResourceType | RESOURCE_TYPE | — | ✅ |
| 29 | StartGmtOffset | START_GMT_OFFSET | — | ✅ |
| 30 | StartTime | START_TIME | — | ✅ |
| 31 | StartTimezoneCode | START_TIMEZONE_CODE | — | ✅ |
| 32 | StopGmtOffset | STOP_GMT_OFFSET | — | ✅ |
| 33 | StopTime | STOP_TIME | — | ✅ |
| 34 | StopTimezoneCode | STOP_TIMEZONE_CODE | — | ✅ |
| 35 | SubresourceId | SUBRESOURCE_ID | — | ✅ |
| 36 | TimeConsumerConfigurationSetId | TCSMR_CONFIG_SET_ID | — | ✅ |
| 37 | TimeConsumerSetId | TCSMR_SET_ID | — | ✅ |
| 38 | TimeRecordId | TM_REC_ID | 🔑 | ✅ |
| 39 | TimeRecordType | TM_REC_TYPE | — | ✅ |
| 40 | TimeRecordVersion | TM_REC_VERSION | 🔑 | ✅ |
| 41 | TimeReporterId | TIME_REPORTER_ID | — | ✅ |
| 42 | TmRecRowId | TM_REC_ROW_ID | — | ✅ |
| 43 | UnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 44 | UserStatus | USER_STATUS | — | ✅ |
| 45 | ZoneType | ZONE_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
