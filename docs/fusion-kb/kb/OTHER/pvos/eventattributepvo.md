---
id: DOC-OTHER-PVO-EventAttributePVO
doc_type: system-doc
title: "EventAttributePVO — PVO Cross-Module"
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
  - EventAttributePVO
  - eventattributepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EventAttributePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Event Attribute. Acessa as tabelas: HWM_TM_ATRB_FLDS_VL, HWM_TM_EVENT_ATRBS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeEventsAM.EventAttributePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 35 | 2 | 1 | 8 | 23% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tm_atrb_flds_vl|HWM_TM_ATRB_FLDS_VL]] — 24 atributos (4 BICC)
- [[hwm_tm_event_atrbs|HWM_TM_EVENT_ATRBS]] — 11 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[hwm_tm_atrb_flds_vl|HWM_TM_ATRB_FLDS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeAttributeFieldVLPEOAllowedScope | ALLOWED_SCOPE | — | — |
| 2 | TimeAttributeFieldVLPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 3 | TimeAttributeFieldVLPEOAttributeGroup | ATTRIBUTE_GROUP | — | — |
| 4 | TimeAttributeFieldVLPEOAttributeType | ATTRIBUTE_TYPE | — | — |
| 5 | TimeAttributeFieldVLPEOClass11 | CLASS | — | — |
| 6 | TimeAttributeFieldVLPEOComponentDisplayCode | COMP_DISP_CODE | — | — |
| 7 | TimeAttributeFieldVLPEOCreatedBy | CREATED_BY | — | — |
| 8 | TimeAttributeFieldVLPEOCreationDate | CREATION_DATE | — | — |
| 9 | TimeAttributeFieldVLPEODescription | DESCRIPTION | — | — |
| 10 | TimeAttributeFieldVLPEODisplayName | DISPLAY_NAME | — | ✅ |
| 11 | TimeAttributeFieldVLPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 12 | TimeAttributeFieldVLPEOGlobalTimeAttributeFieldId | GLOBAL_TM_ATRB_FLD_ID | — | — |
| 13 | TimeAttributeFieldVLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | TimeAttributeFieldVLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | TimeAttributeFieldVLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | TimeAttributeFieldVLPEOMandatoryForTimeConsumers | MANDATORY_FOR_TCSMRS | — | — |
| 17 | TimeAttributeFieldVLPEOModuleId | MODULE_ID | — | — |
| 18 | TimeAttributeFieldVLPEOName | NAME | — | ✅ |
| 19 | TimeAttributeFieldVLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | TimeAttributeFieldVLPEOParentTimeAttributeFieldId | PARENT_TM_ATRB_FLD_ID | — | — |
| 21 | TimeAttributeFieldVLPEOTimeAttributeFieldId | TM_ATRB_FLD_ID | — | ✅ |
| 22 | TimeAttributeFieldVLPEOTimeConsumersId | TCSMRS_ID | — | — |
| 23 | TimeAttributeFieldVLPEOValueLocation | VALUE_LOCATION | — | — |
| 24 | TimeAttributeFieldVLPEOValueSetId | VALUE_SET_ID | — | — |

### [[hwm_tm_event_atrbs|HWM_TM_EVENT_ATRBS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventAttributePEOCreatedBy | CREATED_BY | — | — |
| 2 | EventAttributePEOCreationDate | CREATION_DATE | — | — |
| 3 | EventAttributePEOEnterpriseId | ENTERPRISE_ID | — | — |
| 4 | EventAttributePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | EventAttributePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | EventAttributePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | EventAttributePEOName | NAME | — | ✅ |
| 8 | EventAttributePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | EventAttributePEOTmEventAtrbId | TM_EVENT_ATRB_ID | 🔑 | ✅ |
| 10 | EventAttributePEOTmEventId | TM_EVENT_ID | — | — |
| 11 | EventAttributePEOValue | VALUE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
