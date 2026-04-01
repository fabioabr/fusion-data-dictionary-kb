---
id: DOC-OTHER-PVO-TimeConsumerConfigurationSetPVO
doc_type: system-doc
title: "TimeConsumerConfigurationSetPVO — PVO Cross-Module"
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
  - TimeConsumerConfigurationSetPVO
  - timeconsumerconfigurationsetpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimeConsumerConfigurationSetPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Time Consumer Configuration Set. Acessa as tabelas: HWM_TCSMR_CONFIG_SETS_B, HWM_TCSMR_CONFIG_SETS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeConsumerAM.TimeConsumerConfigurationSetPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 2 | 2 | 25 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tcsmr_config_sets_b|HWM_TCSMR_CONFIG_SETS_B]] — 13 atributos (1 PKs, 13 BICC)
- [[hwm_tcsmr_config_sets_tl|HWM_TCSMR_CONFIG_SETS_TL]] — 12 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[hwm_tcsmr_config_sets_b|HWM_TCSMR_CONFIG_SETS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TcsmrConfigSetPEOAbsApprovalUsageCd | ABS_APPROVAL_USAGE_CD | — | ✅ |
| 2 | TcsmrConfigSetPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | TcsmrConfigSetPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | TcsmrConfigSetPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 5 | TcsmrConfigSetPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | TcsmrConfigSetPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | TcsmrConfigSetPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | TcsmrConfigSetPEOModuleId | MODULE_ID | — | ✅ |
| 9 | TcsmrConfigSetPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | TcsmrConfigSetPEOTimeConsumerConfigurationSetCode | TCSMR_CONFIG_SET_CODE | — | ✅ |
| 11 | TcsmrConfigSetPEOTimeConsumerConfigurationSetId | TCSMR_CONFIG_SET_ID | 🔑 | ✅ |
| 12 | TcsmrConfigSetPEOWrkApprovalEnabled | WRK_APPROVAL_ENABLED | — | ✅ |
| 13 | TcsmrConfigSetPEOWrkflwNtfnEnabled | WRKFLW_NTFN_ENABLED | — | ✅ |

### [[hwm_tcsmr_config_sets_tl|HWM_TCSMR_CONFIG_SETS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TcsmrConfigSetTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | TcsmrConfigSetTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | TcsmrConfigSetTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | TcsmrConfigSetTLPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 5 | TcsmrConfigSetTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | TcsmrConfigSetTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | TcsmrConfigSetTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | TcsmrConfigSetTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | TcsmrConfigSetTLPEOName | NAME | — | ✅ |
| 10 | TcsmrConfigSetTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | TcsmrConfigSetTLPEOSourceLang | SOURCE_LANG | — | ✅ |
| 12 | TcsmrConfigSetTLPEOTimeConsumerConfigurationSetId | TCSMR_CONFIG_SET_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
