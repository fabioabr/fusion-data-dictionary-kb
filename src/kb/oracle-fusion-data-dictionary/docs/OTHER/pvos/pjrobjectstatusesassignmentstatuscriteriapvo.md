---
id: DOC-OTHER-PVO-PjrObjectStatusesAssignmentStatusCriteriaPVO
doc_type: system-doc
title: "PjrObjectStatusesAssignmentStatusCriteriaPVO — PVO Cross-Module"
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
  - PjrObjectStatusesAssignmentStatusCriteriaPVO
  - pjrobjectstatusesassignmentstatuscriteriapvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PjrObjectStatusesAssignmentStatusCriteriaPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Pjr Object Statuses Assignment Status Criteria. Acessa as tabelas: PJR_OBJECT_STATUSES_B, PJR_OBJECT_STATUSES_TL.

**Caminho:** `FscmTopModelAM.PjrSetupAM.PjrObjectStatusesAssignmentStatusCriteriaPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 2 | 2 | 6 | 24% |

---

## 🔗 Tabelas Relacionadas

- [[pjr_object_statuses_b|PJR_OBJECT_STATUSES_B]] — 19 atributos (2 PKs, 4 BICC)
- [[pjr_object_statuses_tl|PJR_OBJECT_STATUSES_TL]] — 6 atributos (2 BICC)

---

## ⚙️ Atributos

### [[pjr_object_statuses_b|PJR_OBJECT_STATUSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectStatusesBasePEOActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | ObjectStatusesBasePEOCreatedBy | CREATED_BY | — | — |
| 3 | ObjectStatusesBasePEOCreationDate | CREATION_DATE | — | — |
| 4 | ObjectStatusesBasePEOEnableWfFlag | ENABLE_WF_FLAG | — | — |
| 5 | ObjectStatusesBasePEOInitialStatusFlag | INITIAL_STATUS_FLAG | — | — |
| 6 | ObjectStatusesBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ObjectStatusesBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ObjectStatusesBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ObjectStatusesBasePEONextAllowableStatusFlag | NEXT_ALLOWABLE_STATUS_FLAG | — | — |
| 10 | ObjectStatusesBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ObjectStatusesBasePEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 12 | ObjectStatusesBasePEOSeededFlag | SEEDED_FLAG | — | — |
| 13 | ObjectStatusesBasePEOSystemFlow | SYSTEM_FLOW | — | — |
| 14 | ObjectStatusesBasePEOSystemStatusCode | SYSTEM_STATUS_CODE | — | — |
| 15 | ObjectStatusesBasePEOUsedBy | USED_BY | — | — |
| 16 | ObjectStatusesBasePEOWfFailureStatusCode | WF_FAILURE_STATUS_CODE | — | — |
| 17 | ObjectStatusesBasePEOWfSuccessStatusCode | WF_SUCCESS_STATUS_CODE | — | — |
| 18 | ObjectType | OBJECT_TYPE | 🔑 | ✅ |
| 19 | StatusCode | STATUS_CODE | 🔑 | ✅ |

### [[pjr_object_statuses_tl|PJR_OBJECT_STATUSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectStatusesTranslationPEODescription | DESCRIPTION | — | ✅ |
| 2 | ObjectStatusesTranslationPEOLanguage | LANGUAGE | — | — |
| 3 | ObjectStatusesTranslationPEOObjectType | OBJECT_TYPE | — | — |
| 4 | ObjectStatusesTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 5 | ObjectStatusesTranslationPEOStatusCode | STATUS_CODE | — | — |
| 6 | ObjectStatusesTranslationPEOStatusName | STATUS_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
