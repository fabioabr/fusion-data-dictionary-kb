---
id: DOC-OTHER-PVO-AttributeNumericValuePVO
doc_type: system-doc
title: "AttributeNumericValuePVO — PVO Cross-Module"
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
  - AttributeNumericValuePVO
  - attributenumericvaluepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AttributeNumericValuePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Attribute Numeric Value. Acessa as tabelas: HWM_TM_REP_ATRB_NUM_VAL_V.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeRepositoryAM.AttributeNumericValuePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 1 | 1 | 6 | 21% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tm_rep_atrb_num_val_v|HWM_TM_REP_ATRB_NUM_VAL_V]] — 28 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[hwm_tm_rep_atrb_num_val_v|HWM_TM_REP_ATRB_NUM_VAL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllowedScope | ALLOWED_SCOPE | — | — |
| 2 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 3 | AttributeGroup | ATTRIBUTE_GROUP | — | — |
| 4 | AttributeName | ATTRIBUTE_NAME | — | ✅ |
| 5 | AttributeNumericValue | ATTRIBUTE_NUMERIC_VALUE | — | ✅ |
| 6 | AttributeType | ATTRIBUTE_TYPE | — | — |
| 7 | Class11 | CLASS | — | — |
| 8 | ComponentDisplayCode | COMP_DISP_CODE | — | — |
| 9 | CreatedBy | CREATED_BY | — | — |
| 10 | CreationDate | CREATION_DATE | — | — |
| 11 | Description | DESCRIPTION | — | — |
| 12 | EnterpriseId | ENTERPRISE_ID | — | — |
| 13 | GlobalTimeAttributeFieldId | GLOBAL_TM_ATRB_FLD_ID | — | — |
| 14 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | MandatoryForTimeConsumers | MANDATORY_FOR_TCSMRS | — | — |
| 18 | ModuleId | MODULE_ID | — | — |
| 19 | Name | NAME | — | ✅ |
| 20 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | ParentTimeAttributeFieldId | PARENT_TM_ATRB_FLD_ID | — | — |
| 22 | TimeAttributeFieldId | TM_ATRB_FLD_ID | — | ✅ |
| 23 | TimeConsumersId | TCSMRS_ID | — | — |
| 24 | TimeRecordId | TM_REC_ID | — | — |
| 25 | TimeRecordVersion | TM_REC_VERSION | — | — |
| 26 | TimeRepositoryAttributeId | TM_REP_ATRB_ID | 🔑 | ✅ |
| 27 | ValueLocation | VALUE_LOCATION | — | — |
| 28 | ValueSetId | VALUE_SET_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
