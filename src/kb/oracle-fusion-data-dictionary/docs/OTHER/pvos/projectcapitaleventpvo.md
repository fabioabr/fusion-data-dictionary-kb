---
id: DOC-OTHER-PVO-ProjectCapitalEventPVO
doc_type: system-doc
title: "ProjectCapitalEventPVO — PVO Cross-Module"
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
  - ProjectCapitalEventPVO
  - projectcapitaleventpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectCapitalEventPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Capital Event. Acessa as tabelas: PJC_CAPITAL_EVENTS.

**Caminho:** `FscmTopModelAM.PjcCapitalAM.ProjectCapitalEventPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 10 | 62% |

---

## 🔗 Tabelas Relacionadas

- [[pjc_capital_events|PJC_CAPITAL_EVENTS]] — 16 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[pjc_capital_events|PJC_CAPITAL_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CapitalEventId | CAPITAL_EVENT_ID | 🔑 | ✅ |
| 2 | ProjectCapitalEventPEOAssetAllocationMethod | ASSET_ALLOCATION_METHOD | — | ✅ |
| 3 | ProjectCapitalEventPEOCapitalEventNumber | CAPITAL_EVENT_NUMBER | — | ✅ |
| 4 | ProjectCapitalEventPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | ProjectCapitalEventPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | ProjectCapitalEventPEOEventName | EVENT_NAME | — | ✅ |
| 7 | ProjectCapitalEventPEOEventPeriod | EVENT_PERIOD | — | ✅ |
| 8 | ProjectCapitalEventPEOEventType | EVENT_TYPE | — | ✅ |
| 9 | ProjectCapitalEventPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 10 | ProjectCapitalEventPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 11 | ProjectCapitalEventPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | ProjectCapitalEventPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | ProjectCapitalEventPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | ProjectCapitalEventPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | ProjectCapitalEventPEOProjectId | PROJECT_ID | — | — |
| 16 | ProjectCapitalEventPEORequestId | REQUEST_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
