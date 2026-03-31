---
id: DOC-OTHER-PVO-ChangeStatusesExtractPVO
doc_type: system-doc
title: "ChangeStatusesExtractPVO — PVO Cross-Module"
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
  - ChangeStatusesExtractPVO
  - changestatusesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ChangeStatusesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Change Statuses Extract. Acessa as tabelas: EGO_CHANGE_STATUSES_B, EGO_CHANGE_STATUSES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgoBiccExtractAM.ChangeStatusesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 2 | 1 | 14 | 78% |

---

## 🔗 Tabelas Relacionadas

- [[ego_change_statuses_b|EGO_CHANGE_STATUSES_B]] — 14 atributos (1 PKs, 14 BICC)
- [[ego_change_statuses_tl|EGO_CHANGE_STATUSES_TL]] — 4 atributos

---

## ⚙️ Atributos

### [[ego_change_statuses_b|EGO_CHANGE_STATUSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EgoChangeStatusesBasePEOApplicationId | APPLICATION_ID | — | ✅ |
| 2 | EgoChangeStatusesBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | EgoChangeStatusesBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | EgoChangeStatusesBasePEODisableDate | DISABLE_DATE | — | ✅ |
| 5 | EgoChangeStatusesBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | EgoChangeStatusesBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | EgoChangeStatusesBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | EgoChangeStatusesBasePEOObjectName | OBJECT_NAME | — | ✅ |
| 9 | EgoChangeStatusesBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | EgoChangeStatusesBasePEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 11 | EgoChangeStatusesBasePEOSeededFlag | SEEDED_FLAG | — | ✅ |
| 12 | EgoChangeStatusesBasePEOStatusCode | STATUS_CODE | 🔑 | ✅ |
| 13 | EgoChangeStatusesBasePEOStatusInternalName | STATUS_INTERNAL_NAME | — | ✅ |
| 14 | EgoChangeStatusesBasePEOStatusType | STATUS_TYPE | — | ✅ |

### [[ego_change_statuses_tl|EGO_CHANGE_STATUSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EgoChangeStatusesTLPEODescription | DESCRIPTION | — | — |
| 2 | EgoChangeStatusesTLPEOLanguage | LANGUAGE | — | — |
| 3 | EgoChangeStatusesTLPEOStatusCode | STATUS_CODE | — | — |
| 4 | EgoChangeStatusesTLPEOStatusName | STATUS_NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
