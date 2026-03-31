---
id: DOC-HCM-PVO-ComplianceMessagePVO
doc_type: system-doc
title: "ComplianceMessagePVO — PVO Human Capital Management"
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
  - ComplianceMessagePVO
  - compliancemessagepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ComplianceMessagePVO

## 📌 Visão Geral

Extrai mensagens de compliance do repositorio de tempo com grupos de registro. Suporta alertas e validacoes de conformidade em time tracking.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeRepositoryAM.ComplianceMessagePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 58 | 2 | 1 | 20 | 34% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tm_rec_grp|HWM_TM_REC_GRP]] — 36 atributos (9 BICC)
- [[hwm_tm_rep_msgs|HWM_TM_REP_MSGS]] — 22 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[hwm_tm_rec_grp|HWM_TM_REC_GRP]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeRecordGroupPEOCommentText | COMMENT_TEXT | — | — |
| 2 | TimeRecordGroupPEOCommitTimestamp | COMMIT_TIMESTAMP | — | ✅ |
| 3 | TimeRecordGroupPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | TimeRecordGroupPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | TimeRecordGroupPEODataSetId | DATA_SET_ID | — | — |
| 6 | TimeRecordGroupPEODateFrom | DATE_FROM | — | — |
| 7 | TimeRecordGroupPEODateTo | DATE_TO | — | — |
| 8 | TimeRecordGroupPEODeleteFlag | DELETE_FLAG | — | — |
| 9 | TimeRecordGroupPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 10 | TimeRecordGroupPEOGroupTypeId | GRP_TYPE_ID | — | — |
| 11 | TimeRecordGroupPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | TimeRecordGroupPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | TimeRecordGroupPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | TimeRecordGroupPEOLatestVersion | LATEST_VERSION | — | — |
| 15 | TimeRecordGroupPEOLayerCode | LAYER_CODE | — | — |
| 16 | TimeRecordGroupPEOLayerTimeRecordGroupId | LAYER_TM_REC_GRP_ID | — | — |
| 17 | TimeRecordGroupPEOLayerTimeRecordGroupVersion | LAYER_TM_REC_GRP_VERSION | — | — |
| 18 | TimeRecordGroupPEOMeasure | MEASURE | — | — |
| 19 | TimeRecordGroupPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | TimeRecordGroupPEOOrderEntered | ORDER_ENTERED | — | — |
| 21 | TimeRecordGroupPEOOriginalTimeRecordGroupId | ORIG_TM_REC_GRP_ID | — | — |
| 22 | TimeRecordGroupPEOOriginalTimeRecordGroupVersion | ORIG_TM_REC_GRP_VERSION | — | — |
| 23 | TimeRecordGroupPEOParentTimeRecordGroupId | PARENT_TM_REC_GRP_ID | — | — |
| 24 | TimeRecordGroupPEOParentTimeRecordGroupVersion | PARENT_TM_REC_GRP_VERSION | — | — |
| 25 | TimeRecordGroupPEOResourceId | RESOURCE_ID | — | — |
| 26 | TimeRecordGroupPEOResourceType | RESOURCE_TYPE | — | — |
| 27 | TimeRecordGroupPEOStartTime | START_TIME | — | ✅ |
| 28 | TimeRecordGroupPEOStopTime | STOP_TIME | — | ✅ |
| 29 | TimeRecordGroupPEOSubresourceId | SUBRESOURCE_ID | — | — |
| 30 | TimeRecordGroupPEOTimeConsumerConfigurationSetId | TCSMR_CONFIG_SET_ID | — | — |
| 31 | TimeRecordGroupPEOTimeConsumerSetId | TCSMR_SET_ID | — | — |
| 32 | TimeRecordGroupPEOTimeRecordGroupId | TM_REC_GRP_ID | — | ✅ |
| 33 | TimeRecordGroupPEOTimeRecordGroupVersion | TM_REC_GRP_VERSION | — | — |
| 34 | TimeRecordGroupPEOTimeReporterId | TIME_REPORTER_ID | — | — |
| 35 | TimeRecordGroupPEOUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 36 | TimeRecordGroupPEOUserStatus | USER_STATUS | — | — |

### [[hwm_tm_rep_msgs|HWM_TM_REP_MSGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeRepositoryMessageId | TM_REP_MSGS_ID | 🔑 | ✅ |
| 2 | TimeRepositoryMessagePEOApplicationId | APPLICATION_ID | — | — |
| 3 | TimeRepositoryMessagePEOApplicationShortName | APPLICATION_SHORT_NAME | — | ✅ |
| 4 | TimeRepositoryMessagePEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | TimeRepositoryMessagePEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | TimeRepositoryMessagePEODateFrom | DATE_FROM | — | ✅ |
| 7 | TimeRepositoryMessagePEODateTo | DATE_TO | — | ✅ |
| 8 | TimeRepositoryMessagePEOEnterpriseId | ENTERPRISE_ID | — | — |
| 9 | TimeRepositoryMessagePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | TimeRepositoryMessagePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | TimeRepositoryMessagePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | TimeRepositoryMessagePEOMessageField | MESSAGE_FIELD | — | — |
| 13 | TimeRepositoryMessagePEOMessageLevel | MESSAGE_LEVEL | — | ✅ |
| 14 | TimeRepositoryMessagePEOMessageName | MESSAGE_NAME | — | ✅ |
| 15 | TimeRepositoryMessagePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | TimeRepositoryMessagePEOTimeEventId | TM_EVENT_ID | — | — |
| 17 | TimeRepositoryMessagePEOTimeRecordGroupId | TM_REC_GRP_ID | — | — |
| 18 | TimeRepositoryMessagePEOTimeRecordGroupVersion | TM_REC_GRP_VERSION | — | — |
| 19 | TimeRepositoryMessagePEOTimeRecordId | TM_REC_ID | — | — |
| 20 | TimeRepositoryMessagePEOTimeRecordVersion | TM_REC_VERSION | — | — |
| 21 | TimeRepositoryMessagePEOTimeRepositoryAttributeUsageId | TM_REP_ATRB_USAGE_ID | — | — |
| 22 | TimeRepositoryMessagePEOTransactionId | TRN_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
