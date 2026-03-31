---
id: DOC-OTHER-PVO-TimeRecordGroupExtractP1
doc_type: system-doc
title: "TimeRecordGroupExtractP1 — PVO Cross-Module"
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
  - TimeRecordGroupExtractP1
  - timerecordgroupextractp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimeRecordGroupExtractP1

## 📌 Visão Geral

View Object para extração BICC de dados de Time Record Group Extract P1. Acessa as tabelas: HWM_TM_REC_GRP.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.WfmBiccExtractAM.TimeRecordGroupExtractP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 36 | 1 | 2 | 36 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tm_rec_grp|HWM_TM_REC_GRP]] — 36 atributos (2 PKs, 36 BICC)

---

## ⚙️ Atributos

### [[hwm_tm_rec_grp|HWM_TM_REC_GRP]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CommentText | COMMENT_TEXT | — | ✅ |
| 2 | CommitTimestamp | COMMIT_TIMESTAMP | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | DataSetId | DATA_SET_ID | — | ✅ |
| 6 | DateFrom | DATE_FROM | — | ✅ |
| 7 | DateTo | DATE_TO | — | ✅ |
| 8 | DeleteFlag | DELETE_FLAG | — | ✅ |
| 9 | EnterpriseId | ENTERPRISE_ID | — | ✅ |
| 10 | GroupTypeId | GRP_TYPE_ID | — | ✅ |
| 11 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | LatestVersion | LATEST_VERSION | — | ✅ |
| 15 | LayerCode | LAYER_CODE | — | ✅ |
| 16 | LayerTimeRecordGroupId | LAYER_TM_REC_GRP_ID | — | ✅ |
| 17 | LayerTimeRecordGroupVersion | LAYER_TM_REC_GRP_VERSION | — | ✅ |
| 18 | Measure | MEASURE | — | ✅ |
| 19 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 20 | OrderEntered | ORDER_ENTERED | — | ✅ |
| 21 | OriginalTimeRecordGroupId | ORIG_TM_REC_GRP_ID | — | ✅ |
| 22 | OriginalTimeRecordGroupVersion | ORIG_TM_REC_GRP_VERSION | — | ✅ |
| 23 | ParentTimeRecordGroupId | PARENT_TM_REC_GRP_ID | — | ✅ |
| 24 | ParentTimeRecordGroupVersion | PARENT_TM_REC_GRP_VERSION | — | ✅ |
| 25 | ResourceId | RESOURCE_ID | — | ✅ |
| 26 | ResourceType | RESOURCE_TYPE | — | ✅ |
| 27 | StartTime | START_TIME | — | ✅ |
| 28 | StopTime | STOP_TIME | — | ✅ |
| 29 | SubresourceId | SUBRESOURCE_ID | — | ✅ |
| 30 | TimeConsumerConfigurationSetId | TCSMR_CONFIG_SET_ID | — | ✅ |
| 31 | TimeConsumerSetId | TCSMR_SET_ID | — | ✅ |
| 32 | TimeRecordGroupId | TM_REC_GRP_ID | 🔑 | ✅ |
| 33 | TimeRecordGroupVersion | TM_REC_GRP_VERSION | 🔑 | ✅ |
| 34 | TimeReporterId | TIME_REPORTER_ID | — | ✅ |
| 35 | UnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 36 | UserStatus | USER_STATUS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
