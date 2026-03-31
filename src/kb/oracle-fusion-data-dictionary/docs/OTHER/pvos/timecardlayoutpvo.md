---
id: DOC-OTHER-PVO-TimecardLayoutPVO
doc_type: system-doc
title: "TimecardLayoutPVO — PVO Cross-Module"
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
  - TimecardLayoutPVO
  - timecardlayoutpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimecardLayoutPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Timecard Layout. Acessa as tabelas: HXT_TCLAYST_B, HXT_TCLAYST_PROP, HXT_TCLAYST_TL (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.LayoutSetAM.TimecardLayoutPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 41 | 4 | 1 | 26 | 63% |

---

## 🔗 Tabelas Relacionadas

- [[hxt_tclayst_b|HXT_TCLAYST_B]] — 16 atributos (8 BICC)
- [[hxt_tclayst_prop|HXT_TCLAYST_PROP]] — 7 atributos (5 BICC)
- [[hxt_tclayst_tl|HXT_TCLAYST_TL]] — 4 atributos (2 BICC)
- [[hxt_tclay_v|HXT_TCLAY_V]] — 14 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[hxt_tclayst_b|HXT_TCLAYST_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TclaystPEOAnswerSetId | ANS_SET_ID | — | — |
| 2 | TclaystPEOAuditUsageFlag | AUDIT_USAGE_FLAG | — | — |
| 3 | TclaystPEOCompletionStatus | COMPLETION_STATUS | — | — |
| 4 | TclaystPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | TclaystPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | TclaystPEODefaultAuditConfigFlag | DEFAULT_AUDIT_CONFIG_FLAG | — | — |
| 7 | TclaystPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 8 | TclaystPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | TclaystPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | TclaystPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | TclaystPEOModuleId | MODULE_ID | — | — |
| 12 | TclaystPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | TclaystPEOOwner | OWNER | — | — |
| 14 | TclaystPEOShortCode | SHORT_CODE | — | ✅ |
| 15 | TclaystPEOTimeConsumerSetId | TCSMR_SET_ID | — | ✅ |
| 16 | TclaystPEOTimecardLayoutSetId | TCLAYST_ID | — | ✅ |

### [[hxt_tclayst_prop|HXT_TCLAYST_PROP]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TclaystPropPEOAnsSetId | ANS_SET_ID | — | — |
| 2 | TclaystPropPEOIndMgrFlag | IND_MGR_FLAG | — | ✅ |
| 3 | TclaystPropPEOIndTcsmrsCode | IND_TCSMRS_CODE | — | ✅ |
| 4 | TclaystPropPEOMembershipFlag | MEMBERSHIP_FLAG | — | ✅ |
| 5 | TclaystPropPEOTclaystPropCd | TCLAYST_PROP_CD | — | ✅ |
| 6 | TclaystPropPEOTclaystPropId | TCLAYST_PROP_ID | — | ✅ |
| 7 | TclaystPropPEOTclaystTeType | TCLAYST_TE_TYPE | — | — |

### [[hxt_tclayst_tl|HXT_TCLAYST_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TclaystTLPEODescription | DESCRIPTION | — | ✅ |
| 2 | TclaystTLPEOLanguage | LANGUAGE | — | — |
| 3 | TclaystTLPEOName | NAME | — | ✅ |
| 4 | TclaystTLPEOTimecardLayoutSetId | TCLAYST_ID | — | — |

### [[hxt_tclay_v|HXT_TCLAY_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TclayVPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | TclayVPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | TclayVPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | TclayVPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | TclayVPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | TclayVPEOTaskName | TASK_NAME | — | ✅ |
| 7 | TclayVPEOTaskShortName | TASK_SHORT_NAME | — | — |
| 8 | TclayVPEOTclayCd | TCLAY_CD | — | ✅ |
| 9 | TclayVPEOTclayId | TCLAY_ID | 🔑 | ✅ |
| 10 | TclayVPEOTclayTaskShortName | TCLAY_TASK_SHORT_NAME | — | ✅ |
| 11 | TclayVPEOTclayType | TCLAY_TYPE | — | ✅ |
| 12 | TclayVPEOTclaystId | TCLAYST_ID | — | ✅ |
| 13 | TclayVPEOTlTaskFeaturesId | TL_TASK_FEATURES_ID | — | — |
| 14 | TclayVPEOTlTaskResultsId | TL_TASK_RESULTS_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
