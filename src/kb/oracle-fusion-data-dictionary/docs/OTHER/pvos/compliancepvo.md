---
id: DOC-OTHER-PVO-CompliancePVO
doc_type: system-doc
title: "CompliancePVO — PVO Cross-Module"
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
  - CompliancePVO
  - compliancepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CompliancePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Compliance. Acessa as tabelas: HWM_TM_REC_GRP.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeRepositoryAM.CompliancePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 36 | 1 | 2 | 10 | 28% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tm_rec_grp|HWM_TM_REC_GRP]] — 36 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[hwm_tm_rec_grp|HWM_TM_REC_GRP]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeRecordGroupPEOCommitTimestamp | COMMIT_TIMESTAMP | — | ✅ |
| 2 | TimeRecordGroupPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | TimeRecordGroupPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | TimeRecordGroupPEODataSetId | DATA_SET_ID | — | — |
| 5 | TimeRecordGroupPEODateFrom | DATE_FROM | — | — |
| 6 | TimeRecordGroupPEODateTo | DATE_TO | — | — |
| 7 | TimeRecordGroupPEODeleteFlag | DELETE_FLAG | — | — |
| 8 | TimeRecordGroupPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 9 | TimeRecordGroupPEOGroupTypeId | GRP_TYPE_ID | — | — |
| 10 | TimeRecordGroupPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | TimeRecordGroupPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | TimeRecordGroupPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | TimeRecordGroupPEOLatestVersion | LATEST_VERSION | — | — |
| 14 | TimeRecordGroupPEOLayerCode | LAYER_CODE | — | — |
| 15 | TimeRecordGroupPEOLayerTimeRecordGroupId | LAYER_TM_REC_GRP_ID | — | — |
| 16 | TimeRecordGroupPEOLayerTimeRecordGroupVersion | LAYER_TM_REC_GRP_VERSION | — | — |
| 17 | TimeRecordGroupPEOMeasure | MEASURE | — | — |
| 18 | TimeRecordGroupPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | TimeRecordGroupPEOOrderEntered | ORDER_ENTERED | — | — |
| 20 | TimeRecordGroupPEOOriginalTimeRecordGroupId | ORIG_TM_REC_GRP_ID | — | — |
| 21 | TimeRecordGroupPEOOriginalTimeRecordGroupVersion | ORIG_TM_REC_GRP_VERSION | — | — |
| 22 | TimeRecordGroupPEOParentTimeRecordGroupId | PARENT_TM_REC_GRP_ID | — | — |
| 23 | TimeRecordGroupPEOParentTimeRecordGroupVersion | PARENT_TM_REC_GRP_VERSION | — | — |
| 24 | TimeRecordGroupPEOResourceId | RESOURCE_ID | — | — |
| 25 | TimeRecordGroupPEOResourceType | RESOURCE_TYPE | — | — |
| 26 | TimeRecordGroupPEOStartTime | START_TIME | — | ✅ |
| 27 | TimeRecordGroupPEOStopTime | STOP_TIME | — | ✅ |
| 28 | TimeRecordGroupPEOSubresourceId | SUBRESOURCE_ID | — | — |
| 29 | TimeRecordGroupPEOTimeConsumerConfigurationSetId | TCSMR_CONFIG_SET_ID | — | — |
| 30 | TimeRecordGroupPEOTimeConsumerSetId | TCSMR_SET_ID | — | — |
| 31 | TimeRecordGroupPEOTimeRecordGroupId | TM_REC_GRP_ID | 🔑 | ✅ |
| 32 | TimeRecordGroupPEOTimeRecordGroupVersion | TM_REC_GRP_VERSION | 🔑 | ✅ |
| 33 | TimeRecordGroupPEOTimeReporterId | TIME_REPORTER_ID | — | — |
| 34 | TimeRecordGroupPEOUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 35 | TimeRecordGroupPEOUserStatus | USER_STATUS | — | — |
| 36 | TimeRecrodGroupPEOCommentText | COMMENT_TEXT | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
