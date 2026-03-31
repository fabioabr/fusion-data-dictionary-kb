---
id: DOC-HCM-PVO-TimeRecordPVO
doc_type: system-doc
title: "TimeRecordPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - TimeRecordPVO
  - timerecordpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimeRecordPVO

## 📌 Visão Geral

Extrai registros individuais de tempo com atividades, eventos e comentários. Base operacional para gestão de ponto e controle de jornada de trabalho.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeRepositoryAM.TimeRecordPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 33 | 1 | 2 | 33 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tm_rec|HWM_TM_REC]] — 33 atributos (2 PKs, 33 BICC)

---

## ⚙️ Atributos

### [[hwm_tm_rec|HWM_TM_REC]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActivityEventTime | ACTIVITY_EVENT_TIME | — | ✅ |
| 2 | ActivityType | ACTIVITY_TYPE | — | ✅ |
| 3 | CommentText | COMMENT_TEXT | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | DataSetId | DATA_SET_ID | — | ✅ |
| 7 | DateFrom | DATE_FROM | — | ✅ |
| 8 | DateTo | DATE_TO | — | ✅ |
| 9 | DeleteFlag | DELETE_FLAG | — | ✅ |
| 10 | EnterpriseId | ENTERPRISE_ID | — | ✅ |
| 11 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | LatestVersion | LATEST_VERSION | — | ✅ |
| 15 | LayerCode | LAYER_CODE | — | ✅ |
| 16 | Measure | MEASURE | — | ✅ |
| 17 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | OrderEntered | ORDER_ENTERED | — | ✅ |
| 19 | OriginalTimeRecordId | ORIG_TM_REC_ID | — | ✅ |
| 20 | OriginalTimeRecordVersion | ORIG_TM_REC_VERSION | — | ✅ |
| 21 | ResourceId | RESOURCE_ID | — | ✅ |
| 22 | ResourceType | RESOURCE_TYPE | — | ✅ |
| 23 | StartTime | START_TIME | — | ✅ |
| 24 | StopTime | STOP_TIME | — | ✅ |
| 25 | SubresourceId | SUBRESOURCE_ID | — | ✅ |
| 26 | TimeConsumerConfigurationSetId | TCSMR_CONFIG_SET_ID | — | ✅ |
| 27 | TimeConsumerSetId | TCSMR_SET_ID | — | ✅ |
| 28 | TimeRecordId | TM_REC_ID | 🔑 | ✅ |
| 29 | TimeRecordType | TM_REC_TYPE | — | ✅ |
| 30 | TimeRecordVersion | TM_REC_VERSION | 🔑 | ✅ |
| 31 | TimeReporterId | TIME_REPORTER_ID | — | ✅ |
| 32 | UnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 33 | UserStatus | USER_STATUS | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
