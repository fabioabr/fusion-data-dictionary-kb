---
id: DOC-GL-PVO-GroupCriteriaPVO
doc_type: system-doc
title: "GroupCriteriaPVO — PVO General Ledger"
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
  - GroupCriteriaPVO
  - groupcriteriapvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GroupCriteriaPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Group Criteria. Acessa as tabelas: HWM_GRP_CRITERIA.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GroupsAM.GroupCriteriaPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 34 | 1 | 1 | 17 | 50% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_grp_criteria|HWM_GRP_CRITERIA]] — 34 atributos (1 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[hwm_grp_criteria|HWM_GRP_CRITERIA]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GroupCriteriaPEOAddlAttrCategory | ADDL_ATTR_CATEGORY | — | — |
| 2 | GroupCriteriaPEOAddlAttrChar1 | ADDL_ATTR_CHAR1 | — | — |
| 3 | GroupCriteriaPEOAddlAttrChar2 | ADDL_ATTR_CHAR2 | — | — |
| 4 | GroupCriteriaPEOAddlAttrChar3 | ADDL_ATTR_CHAR3 | — | — |
| 5 | GroupCriteriaPEOAddlAttrChar4 | ADDL_ATTR_CHAR4 | — | — |
| 6 | GroupCriteriaPEOAddlAttrChar5 | ADDL_ATTR_CHAR5 | — | — |
| 7 | GroupCriteriaPEOAddlAttrNumber1 | ADDL_ATTR_NUMBER1 | — | — |
| 8 | GroupCriteriaPEOAddlAttrNumber2 | ADDL_ATTR_NUMBER2 | — | — |
| 9 | GroupCriteriaPEOAddlAttrNumber3 | ADDL_ATTR_NUMBER3 | — | — |
| 10 | GroupCriteriaPEOAddlAttrNumber4 | ADDL_ATTR_NUMBER4 | — | — |
| 11 | GroupCriteriaPEOAddlAttrNumber5 | ADDL_ATTR_NUMBER5 | — | — |
| 12 | GroupCriteriaPEOBoolOperCd | BOOL_OPER_CD | — | ✅ |
| 13 | GroupCriteriaPEOCreatedBy | CREATED_BY | — | ✅ |
| 14 | GroupCriteriaPEOCreationDate | CREATION_DATE | — | ✅ |
| 15 | GroupCriteriaPEOCriteriaDisplayName | CRITERIA_DISPLAY_NAME | — | ✅ |
| 16 | GroupCriteriaPEOCriteriaId | CRITERIA_ID | — | — |
| 17 | GroupCriteriaPEOCriteriaName | CRITERIA_NAME | — | ✅ |
| 18 | GroupCriteriaPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 19 | GroupCriteriaPEOGrpCriteriaId | GRP_CRITERIA_ID | 🔑 | ✅ |
| 20 | GroupCriteriaPEOGrpId | GRP_ID | — | — |
| 21 | GroupCriteriaPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | GroupCriteriaPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 23 | GroupCriteriaPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | GroupCriteriaPEOLeftParamNum | LEFT_PARAM_NUM | — | ✅ |
| 25 | GroupCriteriaPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 26 | GroupCriteriaPEOOperatorId | OPERATOR_ID | — | — |
| 27 | GroupCriteriaPEOOperatorName | OPERATOR_NAME | — | ✅ |
| 28 | GroupCriteriaPEOOrdrNum | ORDR_NUM | — | ✅ |
| 29 | GroupCriteriaPEORightParamNum | RIGHT_PARAM_NUM | — | ✅ |
| 30 | GroupCriteriaPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 31 | GroupCriteriaPEOValueChar | VALUE_CHAR | — | ✅ |
| 32 | GroupCriteriaPEOValueDate | VALUE_DATE | — | ✅ |
| 33 | GroupCriteriaPEOValueNumber | VALUE_NUMBER | — | ✅ |
| 34 | GroupCriteriaPEOValueTs | VALUE_TS | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
