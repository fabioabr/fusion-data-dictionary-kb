---
id: DOC-HCM-PVO-TimeMessagePVO
doc_type: system-doc
title: "TimeMessagePVO — PVO Human Capital Management"
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
  - TimeMessagePVO
  - timemessagepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimeMessagePVO

## 📌 Visão Geral

Extrai mensagens de tempo com exceções e regras de permissão. Suporta comunicação de alertas e validações no sistema de gestão de jornada.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeRepositoryAM.TimeMessagePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 54 | 2 | 1 | 26 | 48% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_fnd_messages_vl|HWM_FND_MESSAGES_VL]] — 22 atributos (9 BICC)
- [[hwm_tm_allow_exps_v|HWM_TM_ALLOW_EXPS_V]] — 32 atributos (1 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[hwm_fnd_messages_vl|HWM_FND_MESSAGES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HwmFndMessagesVLPEOApplicationId | APPLICATION_ID | — | ✅ |
| 2 | HwmFndMessagesVLPEOApplicationShortName | APPLICATION_SHORT_NAME | — | ✅ |
| 3 | HwmFndMessagesVLPEOChangeSinceLastRefresh | CHANGE_SINCE_LAST_REFRESH | — | — |
| 4 | HwmFndMessagesVLPEOContext | CONTEXT | — | — |
| 5 | HwmFndMessagesVLPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | HwmFndMessagesVLPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | HwmFndMessagesVLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | HwmFndMessagesVLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | HwmFndMessagesVLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | HwmFndMessagesVLPEOLoggableAlertable | LOGGABLE_ALERTABLE | — | — |
| 11 | HwmFndMessagesVLPEOMessageAdminAction | MESSAGE_ADMIN_ACTION | — | — |
| 12 | HwmFndMessagesVLPEOMessageAdminDetails | MESSAGE_ADMIN_DETAILS | — | — |
| 13 | HwmFndMessagesVLPEOMessageCategory | MESSAGE_CATEGORY | — | — |
| 14 | HwmFndMessagesVLPEOMessageCause | MESSAGE_CAUSE | — | — |
| 15 | HwmFndMessagesVLPEOMessageName | MESSAGE_NAME | — | — |
| 16 | HwmFndMessagesVLPEOMessageNumber | MESSAGE_NUMBER | — | ✅ |
| 17 | HwmFndMessagesVLPEOMessageSeverity | MESSAGE_SEVERITY | — | — |
| 18 | HwmFndMessagesVLPEOMessageText | MESSAGE_TEXT | — | ✅ |
| 19 | HwmFndMessagesVLPEOMessageUserAction | MESSAGE_USER_ACTION | — | — |
| 20 | HwmFndMessagesVLPEOMessageUserDetails | MESSAGE_USER_DETAILS | — | — |
| 21 | HwmFndMessagesVLPEOModuleId | MODULE_ID | — | — |
| 22 | HwmFndMessagesVLPEOType | TYPE | — | — |

### [[hwm_tm_allow_exps_v|HWM_TM_ALLOW_EXPS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeMessagePEOAllowExCreatedBy | ALLOWEX_CREATED_BY | — | ✅ |
| 2 | TimeMessagePEOAllowExCreationDate | ALLOWEX_CREATION_DATE | — | ✅ |
| 3 | TimeMessagePEOAllowExLastUpdateDate | ALLOWEX_LAST_UPDATE_DATE | — | ✅ |
| 4 | TimeMessagePEOAllowExLastUpdateLogin | ALLOWEX_LAST_UPDATE_LOGIN | — | ✅ |
| 5 | TimeMessagePEOAllowExLastUpdatedBy | ALLOWEX_LAST_UPDATED_BY | — | ✅ |
| 6 | TimeMessagePEOAllowException | ALLOW_EXCEPTION | — | — |
| 7 | TimeMessagePEOAllowExceptionFlag | ALLOW_EXCEPTION_FLAG | — | ✅ |
| 8 | TimeMessagePEOApplicationId | APPLICATION_ID | — | — |
| 9 | TimeMessagePEOApplicationShortName | APPLICATION_SHORT_NAME | — | — |
| 10 | TimeMessagePEOCreatedBy | CREATED_BY | — | ✅ |
| 11 | TimeMessagePEOCreationDate | CREATION_DATE | — | ✅ |
| 12 | TimeMessagePEODateFrom | DATE_FROM | — | ✅ |
| 13 | TimeMessagePEODateTo | DATE_TO | — | ✅ |
| 14 | TimeMessagePEOEnterpriseId | ENTERPRISE_ID | — | — |
| 15 | TimeMessagePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | TimeMessagePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | TimeMessagePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | TimeMessagePEOMessageField | MESSAGE_FIELD | — | — |
| 19 | TimeMessagePEOMessageLevel | MESSAGE_LEVEL | — | ✅ |
| 20 | TimeMessagePEOMessageName | MESSAGE_NAME | — | ✅ |
| 21 | TimeMessagePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | TimeMessagePEOTmBldgBlkId | TM_BLDG_BLK_ID | — | — |
| 23 | TimeMessagePEOTmBldgBlkVersion | TM_BLDG_BLK_VERSION | — | — |
| 24 | TimeMessagePEOTmEventId | TM_EVENT_ID | — | — |
| 25 | TimeMessagePEOTmRecGrpId | TM_REC_GRP_ID | — | — |
| 26 | TimeMessagePEOTmRecGrpVersion | TM_REC_GRP_VERSION | — | — |
| 27 | TimeMessagePEOTmRecId | TM_REC_ID | — | — |
| 28 | TimeMessagePEOTmRecVersion | TM_REC_VERSION | — | — |
| 29 | TimeMessagePEOTmRepAllowExpsId | TM_REP_ALLOW_EXPS_ID | — | ✅ |
| 30 | TimeMessagePEOTmRepAtrbUsageId | TM_REP_ATRB_USAGE_ID | — | — |
| 31 | TimeMessagePEOTmRepMsgsId | TM_REP_MSGS_ID | 🔑 | ✅ |
| 32 | TimeMessagePEOTrnId | TRN_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
