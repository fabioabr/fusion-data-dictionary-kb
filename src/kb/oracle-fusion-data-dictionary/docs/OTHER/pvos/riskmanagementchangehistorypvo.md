---
id: DOC-OTHER-PVO-RiskManagementChangeHistoryPVO
doc_type: system-doc
title: "RiskManagementChangeHistoryPVO — PVO Cross-Module"
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
  - RiskManagementChangeHistoryPVO
  - riskmanagementchangehistorypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RiskManagementChangeHistoryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Risk Management Change History. Acessa as tabelas: GRC_OTBI_CHG_H_RPT, PER_PERSON_NAMES_F_V, PER_USERS.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.RiskManagementChangeHistoryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 3 | 5 | 21 | 70% |

---

## 🔗 Tabelas Relacionadas

- [[grc_otbi_chg_h_rpt|GRC_OTBI_CHG_H_RPT]] — 20 atributos (5 PKs, 20 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 5 atributos (1 BICC)
- [[per_users|PER_USERS]] — 5 atributos

---

## ⚙️ Atributos

### [[grc_otbi_chg_h_rpt|GRC_OTBI_CHG_H_RPT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeHistoryPEOApprover | APPROVER | — | ✅ |
| 2 | ChangeHistoryPEOAttribute | ATTRIBUTE | 🔑 | ✅ |
| 3 | ChangeHistoryPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | ChangeHistoryPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | ChangeHistoryPEOEntityId | ENTITY_ID | 🔑 | ✅ |
| 6 | ChangeHistoryPEOEventType | EVENT_TYPE | — | ✅ |
| 7 | ChangeHistoryPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ChangeHistoryPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | ChangeHistoryPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ChangeHistoryPEOMdlId | MDL_ID | 🔑 | ✅ |
| 11 | ChangeHistoryPEOModuleId | MODULE_ID | — | ✅ |
| 12 | ChangeHistoryPEONewValue | NEW_VALUE | — | ✅ |
| 13 | ChangeHistoryPEOObjLastUpdatedBy | OBJ_LAST_UPDATED_BY | — | ✅ |
| 14 | ChangeHistoryPEOObjectId | OBJECT_ID | — | ✅ |
| 15 | ChangeHistoryPEOObjectName | OBJECT_NAME | — | ✅ |
| 16 | ChangeHistoryPEOObjectType | OBJECT_TYPE | 🔑 | ✅ |
| 17 | ChangeHistoryPEOOldValue | OLD_VALUE | — | ✅ |
| 18 | ChangeHistoryPEOReviewer | REVIEWER | — | ✅ |
| 19 | ChangeHistoryPEORevision | REVISION | 🔑 | ✅ |
| 20 | ChangeHistoryPEORevisionDate | REVISION_DATE | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CHPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | CHPersonUpdatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | CHPersonUpdatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | CHPersonUpdatedByPersonId | PERSON_ID | — | — |
| 5 | CHPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CHUpdatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | CHUpdatedByPersonId | PERSON_ID | — | — |
| 3 | CHUpdatedByUserGuid | USER_GUID | — | — |
| 4 | CHUpdatedByUserId | USER_ID | — | — |
| 5 | CHUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
