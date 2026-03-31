---
id: DOC-OTHER-PVO-SourceSystemBase
doc_type: system-doc
title: "SourceSystemBase — PVO Cross-Module"
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
  - SourceSystemBase
  - sourcesystembase
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SourceSystemBase

## 📌 Visão Geral

View Object para extração BICC de dados de Source System Base. Acessa as tabelas: HZ_ORIG_SYSTEMS_B.

**Caminho:** `FscmTopModelAM.EgiBatchesPublicModelAnalyticsAM.SourceSystemBase`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 1 | 7 | 41% |

---

## 🔗 Tabelas Relacionadas

- [[hz_orig_systems_b|HZ_ORIG_SYSTEMS_B]] — 17 atributos (1 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[hz_orig_systems_b|HZ_ORIG_SYSTEMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreatedByModule | CREATED_BY_MODULE | — | — |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | EnableForItemsFlag | ENABLE_FOR_ITEMS_FLAG | — | — |
| 5 | EnableForPlanningFlag | ENABLE_FOR_PLANNING_FLAG | — | — |
| 6 | EnableForTcaFlag | ENABLE_FOR_TCA_FLAG | — | — |
| 7 | EndDateActive | END_DATE_ACTIVE | — | — |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | OrigSystem | ORIG_SYSTEM | — | ✅ |
| 13 | OrigSystemId | ORIG_SYSTEM_ID | 🔑 | ✅ |
| 14 | OrigSystemType | ORIG_SYSTEM_TYPE | — | — |
| 15 | SstFlag | SST_FLAG | — | — |
| 16 | StartDateActive | START_DATE_ACTIVE | — | — |
| 17 | Status | STATUS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
