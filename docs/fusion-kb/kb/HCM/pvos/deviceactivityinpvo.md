---
id: DOC-HCM-PVO-DeviceActivityInPVO
doc_type: system-doc
title: "DeviceActivityInPVO — PVO Human Capital Management"
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
  - DeviceActivityInPVO
  - deviceactivityinpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DeviceActivityInPVO

## 📌 Visão Geral

Extrai registros de entrada de atividade via dispositivo de ponto, com dados do colaborador e timestamp. Utilizado para controle de jornada e marcações de entrada.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeRepositoryAM.DeviceActivityInPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 41 | 3 | 2 | 13 | 32% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tm_rec|HWM_TM_REC]] — 33 atributos (2 PKs, 9 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 4 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 4 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hwm_tm_rec|HWM_TM_REC]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeRecordPEOActivityEventTime | ACTIVITY_EVENT_TIME | — | ✅ |
| 2 | TimeRecordPEOActivityType | ACTIVITY_TYPE | — | — |
| 3 | TimeRecordPEOCommentText | COMMENT_TEXT | — | — |
| 4 | TimeRecordPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | TimeRecordPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | TimeRecordPEODataSetId | DATA_SET_ID | — | — |
| 7 | TimeRecordPEODateFrom | DATE_FROM | — | — |
| 8 | TimeRecordPEODateTo | DATE_TO | — | — |
| 9 | TimeRecordPEODeleteFlag | DELETE_FLAG | — | — |
| 10 | TimeRecordPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 11 | TimeRecordPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | TimeRecordPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | TimeRecordPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | TimeRecordPEOLatestVersion | LATEST_VERSION | — | — |
| 15 | TimeRecordPEOLayerCode | LAYER_CODE | — | — |
| 16 | TimeRecordPEOMeasure | MEASURE | — | — |
| 17 | TimeRecordPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | TimeRecordPEOOrderEntered | ORDER_ENTERED | — | — |
| 19 | TimeRecordPEOOriginalTimeRecordId | ORIG_TM_REC_ID | — | — |
| 20 | TimeRecordPEOOriginalTimeRecordVersion | ORIG_TM_REC_VERSION | — | — |
| 21 | TimeRecordPEOResourceId | RESOURCE_ID | — | — |
| 22 | TimeRecordPEOResourceType | RESOURCE_TYPE | — | — |
| 23 | TimeRecordPEOStartTime | START_TIME | — | — |
| 24 | TimeRecordPEOStopTime | STOP_TIME | — | — |
| 25 | TimeRecordPEOSubresourceId | SUBRESOURCE_ID | — | — |
| 26 | TimeRecordPEOTimeConsumerConfigurationSetId | TCSMR_CONFIG_SET_ID | — | — |
| 27 | TimeRecordPEOTimeConsumerSetId | TCSMR_SET_ID | — | — |
| 28 | TimeRecordPEOTimeRecordId | TM_REC_ID | 🔑 | ✅ |
| 29 | TimeRecordPEOTimeRecordType | TM_REC_TYPE | — | — |
| 30 | TimeRecordPEOTimeRecordVersion | TM_REC_VERSION | 🔑 | ✅ |
| 31 | TimeRecordPEOTimeReporterId | TIME_REPORTER_ID | — | ✅ |
| 32 | TimeRecordPEOUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 33 | TimeRecordPEOUserStatus | USER_STATUS | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonDetailsPEOPersonId | PERSON_ID | — | — |
| 4 | PersonDetailsPEOPersonNumber | PERSON_NUMBER | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonNamePEOPersonName | FULL_NAME | — | ✅ |
| 4 | PersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
