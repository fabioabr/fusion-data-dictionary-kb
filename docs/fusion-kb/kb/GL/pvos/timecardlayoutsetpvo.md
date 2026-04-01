---
id: DOC-GL-PVO-TimecardLayoutSetPVO
doc_type: system-doc
title: "TimecardLayoutSetPVO — PVO General Ledger"
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
  - TimecardLayoutSetPVO
  - timecardlayoutsetpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimecardLayoutSetPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Timecard Layout Set. Acessa as tabelas: HXT_TCLAYST_B, HXT_TCLAYST_PROP, HXT_TCLAYST_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.LayoutSetAM.TimecardLayoutSetPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 34 | 3 | 2 | 33 | 97% |

---

## 🔗 Tabelas Relacionadas

- [[hxt_tclayst_b|HXT_TCLAYST_B]] — 16 atributos (1 PKs, 16 BICC)
- [[hxt_tclayst_prop|HXT_TCLAYST_PROP]] — 6 atributos (5 BICC)
- [[hxt_tclayst_tl|HXT_TCLAYST_TL]] — 12 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[hxt_tclayst_b|HXT_TCLAYST_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TclaystPEOAnswerSetId | ANS_SET_ID | — | ✅ |
| 2 | TclaystPEOAuditUsageFlag | AUDIT_USAGE_FLAG | — | ✅ |
| 3 | TclaystPEOCompletionStatus | COMPLETION_STATUS | — | ✅ |
| 4 | TclaystPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | TclaystPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | TclaystPEODefaultAuditConfigFlag | DEFAULT_AUDIT_CONFIG_FLAG | — | ✅ |
| 7 | TclaystPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 8 | TclaystPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | TclaystPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | TclaystPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | TclaystPEOModuleId | MODULE_ID | — | ✅ |
| 12 | TclaystPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | TclaystPEOOwner | OWNER | — | ✅ |
| 14 | TclaystPEOShortCode | SHORT_CODE | — | ✅ |
| 15 | TclaystPEOTimeConsumerSetId | TCSMR_SET_ID | — | ✅ |
| 16 | TclaystPEOTimecardLayoutSetId | TCLAYST_ID | 🔑 | ✅ |

### [[hxt_tclayst_prop|HXT_TCLAYST_PROP]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TclaystPropPEOAnsSetId | ANS_SET_ID | — | — |
| 2 | TclaystPropPEOIndMgrFlag | IND_MGR_FLAG | — | ✅ |
| 3 | TclaystPropPEOIndTcsmrsCode | IND_TCSMRS_CODE | — | ✅ |
| 4 | TclaystPropPEOMembershipFlag | MEMBERSHIP_FLAG | — | ✅ |
| 5 | TclaystPropPEOTclaystPropCd | TCLAYST_PROP_CD | — | ✅ |
| 6 | TclaystPropPEOTclaystPropId | TCLAYST_PROP_ID | — | ✅ |

### [[hxt_tclayst_tl|HXT_TCLAYST_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TclaystTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | TclaystTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | TclaystTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | TclaystTLPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 5 | TclaystTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | TclaystTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | TclaystTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | TclaystTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | TclaystTLPEOName | NAME | — | ✅ |
| 10 | TclaystTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | TclaystTLPEOSourceLang | SOURCE_LANG | — | ✅ |
| 12 | TclaystTLPEOTimecardLayoutSetId | TCLAYST_ID | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
