---
id: DOC-OTHER-PVO-MasterCustomAttributeValuePVO
doc_type: system-doc
title: "MasterCustomAttributeValuePVO — PVO Cross-Module"
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
  - MasterCustomAttributeValuePVO
  - mastercustomattributevaluepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MasterCustomAttributeValuePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Master Custom Attribute Value. Acessa as tabelas: HWM_TM_REP_M_CUST_ATRB_VAL_V.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeRepositoryAM.MasterCustomAttributeValuePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 1 | 1 | 6 | 21% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tm_rep_m_cust_atrb_val_v|HWM_TM_REP_M_CUST_ATRB_VAL_V]] — 29 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[hwm_tm_rep_m_cust_atrb_val_v|HWM_TM_REP_M_CUST_ATRB_VAL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllowedScope | ALLOWED_SCOPE | — | — |
| 2 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 3 | AttributeGroup | ATTRIBUTE_GROUP | — | — |
| 4 | AttributeName | ATTRIBUTE_NAME | — | ✅ |
| 5 | AttributeType | ATTRIBUTE_TYPE | — | — |
| 6 | AttributeVarcharValue | ATTRIBUTE_VARCHAR_VALUE | — | ✅ |
| 7 | Class11 | CLASS | — | — |
| 8 | ComponentDisplayCode | COMP_DISP_CODE | — | — |
| 9 | CreatedBy | CREATED_BY | — | — |
| 10 | CreationDate | CREATION_DATE | — | — |
| 11 | Description | DESCRIPTION | — | — |
| 12 | DisplayName | DISPLAY_NAME | — | — |
| 13 | EnterpriseId | ENTERPRISE_ID | — | — |
| 14 | GlobalTimeAttributeFieldId | GLOBAL_TM_ATRB_FLD_ID | — | — |
| 15 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | MandatoryForTimeConsumers | MANDATORY_FOR_TCSMRS | — | — |
| 19 | ModuleId | MODULE_ID | — | — |
| 20 | Name | NAME | — | ✅ |
| 21 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | ParentTimeAttributeFieldId | PARENT_TM_ATRB_FLD_ID | — | — |
| 23 | TimeAttributeFieldId | TM_ATRB_FLD_ID | — | ✅ |
| 24 | TimeConsumersId | TCSMRS_ID | — | — |
| 25 | TimeRecordId | TM_REC_ID | — | — |
| 26 | TimeRecordVersion | TM_REC_VERSION | — | — |
| 27 | TimeRepositoryAttributeId | TM_REP_ATRB_ID | 🔑 | ✅ |
| 28 | ValueLocation | VALUE_LOCATION | — | — |
| 29 | ValueSetId | VALUE_SET_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
