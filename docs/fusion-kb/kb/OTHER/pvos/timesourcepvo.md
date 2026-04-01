---
id: DOC-OTHER-PVO-TimeSourcePVO
doc_type: system-doc
title: "TimeSourcePVO — PVO Cross-Module"
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
  - TimeSourcePVO
  - timesourcepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimeSourcePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Time Source. Acessa as tabelas: HWM_TM_SOURCES.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeSourceAM.TimeSourcePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 1 | 2 | 20% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tm_sources|HWM_TM_SOURCES]] — 10 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[hwm_tm_sources|HWM_TM_SOURCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | EnterpriseId | ENTERPRISE_ID | — | — |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ModuleId | MODULE_ID | — | — |
| 8 | Name | NAME | — | — |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | TimeSourceId | TM_SOURCE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
