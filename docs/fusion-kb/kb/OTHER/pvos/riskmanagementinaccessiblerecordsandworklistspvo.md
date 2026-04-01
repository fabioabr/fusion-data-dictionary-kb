---
id: DOC-OTHER-PVO-RiskManagementInAccessibleRecordsandWorklistsPVO
doc_type: system-doc
title: "RiskManagementInAccessibleRecordsandWorklistsPVO — PVO Cross-Module"
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
  - RiskManagementInAccessibleRecordsandWorklistsPVO
  - riskmanagementinaccessiblerecordsandworklistspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RiskManagementInAccessibleRecordsandWorklistsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Risk Management In Accessible Recordsand Worklists. Acessa as tabelas: GRC_OTBI_INACCESS_REC_RPT.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.RiskManagementInAccessibleRecordsandWorklistsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 3 | 17 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[grc_otbi_inaccess_rec_rpt|GRC_OTBI_INACCESS_REC_RPT]] — 17 atributos (3 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[grc_otbi_inaccess_rec_rpt|GRC_OTBI_INACCESS_REC_RPT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InAccessibleRecsnWrkListPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | InAccessibleRecsnWrkListPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | InAccessibleRecsnWrkListPEODueDate | DUE_DATE | — | ✅ |
| 4 | InAccessibleRecsnWrkListPEOEntityId | ENTITY_ID | 🔑 | ✅ |
| 5 | InAccessibleRecsnWrkListPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | InAccessibleRecsnWrkListPEOLastUpdtDt | LAST_UPDATE_DATE | — | ✅ |
| 7 | InAccessibleRecsnWrkListPEOLastUpdtLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | InAccessibleRecsnWrkListPEOModuleId | MODULE_ID | — | ✅ |
| 9 | InAccessibleRecsnWrkListPEOObjCreationDt | OBJ_CREATION_DATE | — | ✅ |
| 10 | InAccessibleRecsnWrkListPEOObjectId | OBJECT_ID | — | ✅ |
| 11 | InAccessibleRecsnWrkListPEOObjectName | OBJECT_NAME | — | ✅ |
| 12 | InAccessibleRecsnWrkListPEOObjectType | OBJECT_TYPE | 🔑 | ✅ |
| 13 | InAccessibleRecsnWrkListPEOPerspItemId | PERSPECTIVE_ITEM_ID | 🔑 | ✅ |
| 14 | InAccessibleRecsnWrkListPEOPerspName | PERSPECTIVE_NAME | — | ✅ |
| 15 | InAccessibleRecsnWrkListPEOPerspTreeId | PERSPECTIVE_TREE_ID | — | ✅ |
| 16 | InAccessibleRecsnWrkListPEOPerspValue | PERSPECTIVE_VALUE | — | ✅ |
| 17 | InAccessibleRecsnWrkListPEOStateCode | STATE_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
