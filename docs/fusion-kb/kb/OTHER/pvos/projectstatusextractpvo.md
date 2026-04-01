---
id: DOC-OTHER-PVO-ProjectStatusExtractPVO
doc_type: system-doc
title: "ProjectStatusExtractPVO — PVO Cross-Module"
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
  - ProjectStatusExtractPVO
  - projectstatusextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectStatusExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Status Extract. Acessa as tabelas: PJF_PROJECT_STATUSES_B, PJF_PROJECT_STATUSES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ProjectStatusExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 50 | 2 | 1 | 34 | 68% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_project_statuses_b|PJF_PROJECT_STATUSES_B]] — 39 atributos (1 PKs, 23 BICC)
- [[pjf_project_statuses_tl|PJF_PROJECT_STATUSES_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[pjf_project_statuses_b|PJF_PROJECT_STATUSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectStatusBasePEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | ProjectStatusBasePEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | ProjectStatusBasePEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | ProjectStatusBasePEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | ProjectStatusBasePEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | ProjectStatusBasePEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | ProjectStatusBasePEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | ProjectStatusBasePEOAttribute2 | ATTRIBUTE2 | — | — |
| 9 | ProjectStatusBasePEOAttribute3 | ATTRIBUTE3 | — | — |
| 10 | ProjectStatusBasePEOAttribute4 | ATTRIBUTE4 | — | — |
| 11 | ProjectStatusBasePEOAttribute5 | ATTRIBUTE5 | — | — |
| 12 | ProjectStatusBasePEOAttribute6 | ATTRIBUTE6 | — | — |
| 13 | ProjectStatusBasePEOAttribute7 | ATTRIBUTE7 | — | — |
| 14 | ProjectStatusBasePEOAttribute8 | ATTRIBUTE8 | — | — |
| 15 | ProjectStatusBasePEOAttribute9 | ATTRIBUTE9 | — | — |
| 16 | ProjectStatusBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | ProjectStatusBasePEOBpFailureStatusCode | BP_FAILURE_STATUS_CODE | — | ✅ |
| 18 | ProjectStatusBasePEOBpSuccessStatusCode | BP_SUCCESS_STATUS_CODE | — | ✅ |
| 19 | ProjectStatusBasePEOBpelItemType | BPEL_ITEM_TYPE | — | ✅ |
| 20 | ProjectStatusBasePEOBpelProcess | BPEL_PROCESS | — | ✅ |
| 21 | ProjectStatusBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 22 | ProjectStatusBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 23 | ProjectStatusBasePEOEnableBpFlag | ENABLE_BP_FLAG | — | ✅ |
| 24 | ProjectStatusBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 25 | ProjectStatusBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | ProjectStatusBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 27 | ProjectStatusBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 28 | ProjectStatusBasePEONextAllowableStatusFlag | NEXT_ALLOWABLE_STATUS_FLAG | — | ✅ |
| 29 | ProjectStatusBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 30 | ProjectStatusBasePEOPredefinedFlag | PREDEFINED_FLAG | — | ✅ |
| 31 | ProjectStatusBasePEOProjectStatusCode | PROJECT_STATUS_CODE | 🔑 | ✅ |
| 32 | ProjectStatusBasePEOProjectStatusWeight | PROJECT_STATUS_WEIGHT | — | ✅ |
| 33 | ProjectStatusBasePEOProjectSystemStatusCode | PROJECT_SYSTEM_STATUS_CODE | — | ✅ |
| 34 | ProjectStatusBasePEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 35 | ProjectStatusBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 36 | ProjectStatusBasePEOStartingStatusFlag | STARTING_STATUS_FLAG | — | ✅ |
| 37 | ProjectStatusBasePEOStatusIconActiveInd | STATUS_ICON_ACTIVE_IND | — | ✅ |
| 38 | ProjectStatusBasePEOStatusIconInd | STATUS_ICON_IND | — | ✅ |
| 39 | ProjectStatusBasePEOStatusType | STATUS_TYPE | — | ✅ |

### [[pjf_project_statuses_tl|PJF_PROJECT_STATUSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectStatusTransLangPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProjectStatusTransLangPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProjectStatusTransLangPEODescription | DESCRIPTION | — | ✅ |
| 4 | ProjectStatusTransLangPEOLanguage | LANGUAGE | — | ✅ |
| 5 | ProjectStatusTransLangPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ProjectStatusTransLangPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ProjectStatusTransLangPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ProjectStatusTransLangPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | ProjectStatusTransLangPEOProjectStatusCode | PROJECT_STATUS_CODE | — | ✅ |
| 10 | ProjectStatusTransLangPEOProjectStatusName | PROJECT_STATUS_NAME | — | ✅ |
| 11 | ProjectStatusTransLangPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
