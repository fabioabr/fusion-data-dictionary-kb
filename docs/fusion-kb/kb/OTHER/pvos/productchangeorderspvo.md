---
id: DOC-OTHER-PVO-ProductChangeOrdersPVO
doc_type: system-doc
title: "ProductChangeOrdersPVO — PVO Cross-Module"
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
  - ProductChangeOrdersPVO
  - productchangeorderspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProductChangeOrdersPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Product Change Orders. Acessa as tabelas: EGO_CHANGE_STATUSES_VL, EGO_ENGINEERING_CHANGES_B, EGO_ENGINEERING_CHANGES_TL.

**Caminho:** `FscmTopModelAM.CommonAnalyticsAM.ProductChangeOrdersPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 3 | 1 | 12 | 48% |

---

## 🔗 Tabelas Relacionadas

- [[ego_change_statuses_vl|EGO_CHANGE_STATUSES_VL]] — 4 atributos (4 BICC)
- [[ego_engineering_changes_b|EGO_ENGINEERING_CHANGES_B]] — 11 atributos (1 PKs, 5 BICC)
- [[ego_engineering_changes_tl|EGO_ENGINEERING_CHANGES_TL]] — 10 atributos (3 BICC)

---

## ⚙️ Atributos

### [[ego_change_statuses_vl|EGO_CHANGE_STATUSES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeStatusesDescription | DESCRIPTION | — | ✅ |
| 2 | ChangeStatusesStatusCode | STATUS_CODE | — | ✅ |
| 3 | ChangeStatusesStatusName | STATUS_NAME | — | ✅ |
| 4 | ChangeStatusesStatusType | STATUS_TYPE | — | ✅ |

### [[ego_engineering_changes_b|EGO_ENGINEERING_CHANGES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeAssigneeId | ASSIGNEE_ID | — | — |
| 2 | ChangeChangeId | CHANGE_ID | 🔑 | ✅ |
| 3 | ChangeCreatedBy | CREATED_BY | — | — |
| 4 | ChangeCreationDate | CREATION_DATE | — | ✅ |
| 5 | ChangeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ChangeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ChangeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ChangePriorityCode | PRIORITY_CODE | — | ✅ |
| 9 | ChangeStatusCode | STATUS_CODE | — | — |
| 10 | Creator | CREATED_BY | — | — |
| 11 | NeedByDate | NEED_BY_DATE | — | ✅ |

### [[ego_engineering_changes_tl|EGO_ENGINEERING_CHANGES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeTranslationChangeId | CHANGE_ID | — | — |
| 2 | ChangeTranslationChangeName | CHANGE_NAME | — | ✅ |
| 3 | ChangeTranslationCreatedBy | CREATED_BY | — | — |
| 4 | ChangeTranslationCreationDate | CREATION_DATE | — | — |
| 5 | ChangeTranslationDescription | DESCRIPTION | — | ✅ |
| 6 | ChangeTranslationDisplayName | CHANGE_NAME | — | — |
| 7 | ChangeTranslationLanguage | LANGUAGE | — | — |
| 8 | ChangeTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ChangeTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | ChangeTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
