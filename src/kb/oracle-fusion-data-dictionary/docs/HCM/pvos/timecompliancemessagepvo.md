---
id: DOC-HCM-PVO-TimeComplianceMessagePVO
doc_type: system-doc
title: "TimeComplianceMessagePVO — PVO Human Capital Management"
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
  - TimeComplianceMessagePVO
  - timecompliancemessagepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimeComplianceMessagePVO

## 📌 Visão Geral

Extrai mensagens de conformidade de tempo com regras de validação e timestamps. Suporta auditoria de compliance em registros de jornada de trabalho.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeRepositoryAM.TimeComplianceMessagePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 39 | 1 | 4 | 22 | 56% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tm_comp_msgs_v|HWM_TM_COMP_MSGS_V]] — 39 atributos (4 PKs, 22 BICC)

---

## ⚙️ Atributos

### [[hwm_tm_comp_msgs_v|HWM_TM_COMP_MSGS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeComplianceMessagePEOApplicationShortName | APPLICATION_SHORT_NAME | — | ✅ |
| 2 | TimeComplianceMessagePEOComplianceCommitTimestamp | COMPLIANCE_COMMIT_TIMESTAMP | — | ✅ |
| 3 | TimeComplianceMessagePEOComplianceCreatedBy | COMPLIANCE_CREATED_BY | — | ✅ |
| 4 | TimeComplianceMessagePEOComplianceCreationDate | COMPLIANCE_CREATION_DATE | — | ✅ |
| 5 | TimeComplianceMessagePEOComplianceDeleteFlag | COMPLIANCE_DELETE_FLAG | — | — |
| 6 | TimeComplianceMessagePEOComplianceGrpTypeId | COMPLIANCE_GRP_TYPE_ID | — | — |
| 7 | TimeComplianceMessagePEOComplianceId | COMPLIANCE_ID | 🔑 | ✅ |
| 8 | TimeComplianceMessagePEOComplianceLastUpdateDate | COMPLIANCE_LAST_UPDATE_DATE | — | ✅ |
| 9 | TimeComplianceMessagePEOComplianceLastUpdateLogin | COMPLIANCE_LAST_UPDATE_LOGIN | — | ✅ |
| 10 | TimeComplianceMessagePEOComplianceLastUpdatedBy | COMPLIANCE_LAST_UPDATED_BY | — | ✅ |
| 11 | TimeComplianceMessagePEOComplianceLatestVersion | COMPLIANCE_LATEST_VERSION | — | — |
| 12 | TimeComplianceMessagePEOComplianceStartTime | COMPLIANCE_START_TIME | — | ✅ |
| 13 | TimeComplianceMessagePEOComplianceStopTime | COMPLIANCE_STOP_TIME | — | ✅ |
| 14 | TimeComplianceMessagePEOComplianceSubresourceId | COMPLIANCE_SUBRESOURCE_ID | — | — |
| 15 | TimeComplianceMessagePEOCreatedBy | CREATED_BY | — | ✅ |
| 16 | TimeComplianceMessagePEOCreationDate | CREATION_DATE | — | ✅ |
| 17 | TimeComplianceMessagePEODateFrom | DATE_FROM | — | ✅ |
| 18 | TimeComplianceMessagePEODateTo | DATE_TO | — | ✅ |
| 19 | TimeComplianceMessagePEODayDeleteFlag | DAY_DELETE_FLAG | — | — |
| 20 | TimeComplianceMessagePEODayLatestVersion | DAY_LATEST_VERSION | — | — |
| 21 | TimeComplianceMessagePEODayTmRecGrpId | DAY_TM_REC_GRP_ID | — | — |
| 22 | TimeComplianceMessagePEODayTmRecGrpVersion | DAY_TM_REC_GRP_VERSION | — | — |
| 23 | TimeComplianceMessagePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | TimeComplianceMessagePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 25 | TimeComplianceMessagePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 26 | TimeComplianceMessagePEOMessageLevel | MESSAGE_LEVEL | — | ✅ |
| 27 | TimeComplianceMessagePEOMessageName | MESSAGE_NAME | — | ✅ |
| 28 | TimeComplianceMessagePEOResourceId | RESOURCE_ID | — | — |
| 29 | TimeComplianceMessagePEOTcDeleteFlag | TC_DELETE_FLAG | — | — |
| 30 | TimeComplianceMessagePEOTcLatestVersion | TC_LATEST_VERSION | — | — |
| 31 | TimeComplianceMessagePEOTcTmRecGrpId | TC_TM_REC_GRP_ID | — | — |
| 32 | TimeComplianceMessagePEOTcTmRecGrpVersion | TC_TM_REC_GRP_VERSION | — | — |
| 33 | TimeComplianceMessagePEOTeDeleteFlag | TE_DELETE_FLAG | — | — |
| 34 | TimeComplianceMessagePEOTeLatestVersion | TE_LATEST_VERSION | — | — |
| 35 | TimeComplianceMessagePEOTeTmRecId | TE_TM_REC_ID | 🔑 | ✅ |
| 36 | TimeComplianceMessagePEOTeTmRecVersion | TE_TM_REC_VERSION | 🔑 | ✅ |
| 37 | TimeComplianceMessagePEOTmBldgBlkId | TM_BLDG_BLK_ID | — | — |
| 38 | TimeComplianceMessagePEOTmBldgBlkVersion | TM_BLDG_BLK_VERSION | — | — |
| 39 | TimeComplianceMessagePEOTmRepMsgsId | TM_REP_MSGS_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
