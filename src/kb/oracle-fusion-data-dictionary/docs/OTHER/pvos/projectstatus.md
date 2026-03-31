---
id: DOC-OTHER-PVO-ProjectStatus
doc_type: system-doc
title: "ProjectStatus — PVO Cross-Module"
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
  - ProjectStatus
  - projectstatus
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectStatus

## 📌 Visão Geral

View Object para extração BICC de dados de Project Status. Acessa as tabelas: PJF_PROJECT_STATUSES_VL.

**Caminho:** `FscmTopModelAM.PjfSetupStatusesAnalyticsAM.ProjectStatus`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 40 | 1 | 1 | 9 | 22% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_project_statuses_vl|PJF_PROJECT_STATUSES_VL]] — 40 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[pjf_project_statuses_vl|PJF_PROJECT_STATUSES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute1 | ATTRIBUTE1 | — | — |
| 2 | Attribute10 | ATTRIBUTE10 | — | — |
| 3 | Attribute11 | ATTRIBUTE11 | — | — |
| 4 | Attribute12 | ATTRIBUTE12 | — | — |
| 5 | Attribute13 | ATTRIBUTE13 | — | — |
| 6 | Attribute14 | ATTRIBUTE14 | — | — |
| 7 | Attribute15 | ATTRIBUTE15 | — | — |
| 8 | Attribute2 | ATTRIBUTE2 | — | — |
| 9 | Attribute3 | ATTRIBUTE3 | — | — |
| 10 | Attribute4 | ATTRIBUTE4 | — | — |
| 11 | Attribute5 | ATTRIBUTE5 | — | — |
| 12 | Attribute6 | ATTRIBUTE6 | — | — |
| 13 | Attribute7 | ATTRIBUTE7 | — | — |
| 14 | Attribute8 | ATTRIBUTE8 | — | — |
| 15 | Attribute9 | ATTRIBUTE9 | — | — |
| 16 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | BpFailureStatusCode | BP_FAILURE_STATUS_CODE | — | — |
| 18 | BpSuccessStatusCode | BP_SUCCESS_STATUS_CODE | — | — |
| 19 | BpelItemType | BPEL_ITEM_TYPE | — | — |
| 20 | BpelProcess | BPEL_PROCESS | — | — |
| 21 | CreatedBy | CREATED_BY | — | ✅ |
| 22 | CreationDate | CREATION_DATE | — | ✅ |
| 23 | Description | DESCRIPTION | — | ✅ |
| 24 | EnableBpFlag | ENABLE_BP_FLAG | — | — |
| 25 | EndDateActive | END_DATE_ACTIVE | — | ✅ |
| 26 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 27 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 28 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 29 | NextAllowableStatusFlag | NEXT_ALLOWABLE_STATUS_FLAG | — | — |
| 30 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 31 | PredefinedFlag | PREDEFINED_FLAG | — | — |
| 32 | ProjectStatusCode | PROJECT_STATUS_CODE | 🔑 | ✅ |
| 33 | ProjectStatusName | PROJECT_STATUS_NAME | — | ✅ |
| 34 | ProjectStatusWeight | PROJECT_STATUS_WEIGHT | — | — |
| 35 | ProjectSystemStatusCode | PROJECT_SYSTEM_STATUS_CODE | — | — |
| 36 | StartDateActive | START_DATE_ACTIVE | — | ✅ |
| 37 | StartingStatusFlag | STARTING_STATUS_FLAG | — | — |
| 38 | StatusIconActiveInd | STATUS_ICON_ACTIVE_IND | — | — |
| 39 | StatusIconInd | STATUS_ICON_IND | — | — |
| 40 | StatusType | STATUS_TYPE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
