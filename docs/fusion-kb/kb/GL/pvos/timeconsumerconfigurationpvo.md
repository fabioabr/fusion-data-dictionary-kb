---
id: DOC-GL-PVO-TimeConsumerConfigurationPVO
doc_type: system-doc
title: "TimeConsumerConfigurationPVO — PVO General Ledger"
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
  - TimeConsumerConfigurationPVO
  - timeconsumerconfigurationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimeConsumerConfigurationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Time Consumer Configuration. Acessa as tabelas: HWM_TCATS_VL, HWM_TCSMRS_VL, HWM_TCSMR_CONFIGS (+4).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeConsumerAM.TimeConsumerConfigurationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 58 | 7 | 1 | 44 | 76% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tcats_vl|HWM_TCATS_VL]] — 3 atributos (1 BICC)
- [[hwm_tcsmrs_vl|HWM_TCSMRS_VL]] — 3 atributos (3 BICC)
- [[hwm_tcsmr_configs|HWM_TCSMR_CONFIGS]] — 16 atributos (1 PKs, 16 BICC)
- [[hwm_tcsmr_config_sets_b|HWM_TCSMR_CONFIG_SETS_B]] — 13 atributos (10 BICC)
- [[hwm_tcsmr_config_sets_tl|HWM_TCSMR_CONFIG_SETS_TL]] — 4 atributos (2 BICC)
- [[hwm_tcsmr_xfr_configs|HWM_TCSMR_XFR_CONFIGS]] — 16 atributos (9 BICC)
- [[hwm_tcsmr_xfr_processes_vl|HWM_TCSMR_XFR_PROCESSES_VL]] — 3 atributos (3 BICC)

---

## ⚙️ Atributos

### [[hwm_tcats_vl|HWM_TCATS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeCategoryVLPEOTcatCd | TCAT_CD | — | ✅ |
| 2 | TimeCategoryVLPEOTcatId | TCAT_ID | — | — |
| 3 | TimeCategoryVLPEOTcatName | TCAT_NAME | — | — |

### [[hwm_tcsmrs_vl|HWM_TCSMRS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeConsumerVLPEOName | NAME | — | ✅ |
| 2 | TimeConsumerVLPEOTcsmrsCode | TCSMRS_CODE | — | ✅ |
| 3 | TimeConsumerVLPEOTcsmrsId | TCSMRS_ID | — | ✅ |

### [[hwm_tcsmr_configs|HWM_TCSMR_CONFIGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApprovalPeriodId | APPROVAL_PERIOD_ID | — | ✅ |
| 2 | AprvlRecGrpTypCd | APRVL_REC_GRP_TYP_CD | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | EnterpriseId | ENTERPRISE_ID | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | TcatId | TCAT_ID | — | ✅ |
| 11 | TcsmrConfigId | TCSMR_CONFIG_ID | 🔑 | ✅ |
| 12 | TcsmrConfigSetId | TCSMR_CONFIG_SET_ID | — | ✅ |
| 13 | TcsmrsId | TCSMRS_ID | — | ✅ |
| 14 | TimeConsumerConfigurationPEOEnableEntryLevelAprvl | ENABLE_ENTRY_LEVEL_APRVL | — | ✅ |
| 15 | TimeRequired | TIME_REQUIRED | — | ✅ |
| 16 | ValidateOnSave | VALIDATE_ON_SAVE | — | ✅ |

### [[hwm_tcsmr_config_sets_b|HWM_TCSMR_CONFIG_SETS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TcsmrConfigSetPEOAbsApprovalUsageCd | ABS_APPROVAL_USAGE_CD | — | ✅ |
| 2 | TcsmrConfigSetPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | TcsmrConfigSetPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | TcsmrConfigSetPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 5 | TcsmrConfigSetPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | TcsmrConfigSetPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | TcsmrConfigSetPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | TcsmrConfigSetPEOModuleId | MODULE_ID | — | — |
| 9 | TcsmrConfigSetPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | TcsmrConfigSetPEOTimeConsumerConfigurationSetCode | TCSMR_CONFIG_SET_CODE | — | ✅ |
| 11 | TcsmrConfigSetPEOTimeConsumerConfigurationSetId | TCSMR_CONFIG_SET_ID | — | ✅ |
| 12 | TcsmrConfigSetPEOWrkApprovalEnabled | WRK_APPROVAL_ENABLED | — | ✅ |
| 13 | TcsmrConfigSetPEOWrkflwNtfnEnabled | WRKFLW_NTFN_ENABLED | — | ✅ |

### [[hwm_tcsmr_config_sets_tl|HWM_TCSMR_CONFIG_SETS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TcsmrConfigSetTLPEODescription | DESCRIPTION | — | ✅ |
| 2 | TcsmrConfigSetTLPEOLanguage | LANGUAGE | — | — |
| 3 | TcsmrConfigSetTLPEOName | NAME | — | ✅ |
| 4 | TcsmrConfigSetTLPEOTimeConsumerConfigurationSetId | TCSMR_CONFIG_SET_ID | — | — |

### [[hwm_tcsmr_xfr_configs|HWM_TCSMR_XFR_CONFIGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TcsmrXfrConfigPEOApprovalReqd | APPROVAL_REQD | — | ✅ |
| 2 | TcsmrXfrConfigPEOApprovalReqdTcsmrId | APPROVAL_REQD_TCSMR_ID | — | — |
| 3 | TcsmrXfrConfigPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | TcsmrXfrConfigPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | TcsmrXfrConfigPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 6 | TcsmrXfrConfigPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | TcsmrXfrConfigPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | TcsmrXfrConfigPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | TcsmrXfrConfigPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | TcsmrXfrConfigPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 11 | TcsmrXfrConfigPEOSguid | SGUID | — | — |
| 12 | TcsmrXfrConfigPEOTcmsrXfrConfigId | TCMSR_XFR_CONFIG_ID | — | ✅ |
| 13 | TcsmrXfrConfigPEOTcsmrConfigId | TCSMR_CONFIG_ID | — | — |
| 14 | TcsmrXfrConfigPEOTcsmrXfrProcessId | TCSMR_XFR_PROCESS_ID | — | — |
| 15 | TcsmrXfrConfigPEOXfrOnSave | XFR_ON_SAVE | — | ✅ |
| 16 | TcsmrXfrConfigPEOXfrOnSubmit | XFR_ON_SUBMIT | — | ✅ |

### [[hwm_tcsmr_xfr_processes_vl|HWM_TCSMR_XFR_PROCESSES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TcsmrXfrProcessVLPEOName | NAME | — | ✅ |
| 2 | TcsmrXfrProcessVLPEOPendingEntriesThreshold | PENDING_ENTRIES_THRESHOLD | — | ✅ |
| 3 | TcsmrXfrProcessVLPEOTcsmrXfrProcessId | TCSMR_XFR_PROCESS_ID | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
