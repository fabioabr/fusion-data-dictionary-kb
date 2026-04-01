---
id: DOC-OTHER-PVO-EgoChangeStatusesPVO
doc_type: system-doc
title: "EgoChangeStatusesPVO — PVO Cross-Module"
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
  - EgoChangeStatusesPVO
  - egochangestatusespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EgoChangeStatusesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Ego Change Statuses. Acessa as tabelas: EGO_CHANGE_STATUSES_B, EGO_CHANGE_STATUSES_TL.

**Caminho:** `FscmTopModelAM.ChangeTypesAM.EgoChangeStatusesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 2 | 1 | 9 | 50% |

---

## 🔗 Tabelas Relacionadas

- [[ego_change_statuses_b|EGO_CHANGE_STATUSES_B]] — 13 atributos (1 PKs, 6 BICC)
- [[ego_change_statuses_tl|EGO_CHANGE_STATUSES_TL]] — 5 atributos (3 BICC)

---

## ⚙️ Atributos

### [[ego_change_statuses_b|EGO_CHANGE_STATUSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EgoChangeStatusesBasePEOApplicationId | APPLICATION_ID | — | — |
| 2 | EgoChangeStatusesBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | EgoChangeStatusesBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | EgoChangeStatusesBasePEODisableDate | DISABLE_DATE | — | — |
| 5 | EgoChangeStatusesBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | EgoChangeStatusesBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | EgoChangeStatusesBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | EgoChangeStatusesBasePEOObjectName | OBJECT_NAME | — | — |
| 9 | EgoChangeStatusesBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | EgoChangeStatusesBasePEOSeededFlag | SEEDED_FLAG | — | — |
| 11 | EgoChangeStatusesBasePEOSortSequenceNum | SORT_SEQUENCE_NUM | — | — |
| 12 | EgoChangeStatusesBasePEOStatusType | STATUS_TYPE | — | ✅ |
| 13 | StatusCode | STATUS_CODE | 🔑 | ✅ |

### [[ego_change_statuses_tl|EGO_CHANGE_STATUSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EgoChangeStatusesTLPEODescription | DESCRIPTION | — | ✅ |
| 2 | EgoChangeStatusesTLPEOLanguage | LANGUAGE | — | ✅ |
| 3 | EgoChangeStatusesTLPEOSourceLang | SOURCE_LANG | — | — |
| 4 | EgoChangeStatusesTLPEOStatusCode | STATUS_CODE | — | — |
| 5 | EgoChangeStatusesTLPEOStatusName | STATUS_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
