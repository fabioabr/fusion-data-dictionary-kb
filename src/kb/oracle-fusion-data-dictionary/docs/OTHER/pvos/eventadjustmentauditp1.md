---
id: DOC-OTHER-PVO-EventAdjustmentAuditP1
doc_type: system-doc
title: "EventAdjustmentAuditP1 — PVO Cross-Module"
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
  - EventAdjustmentAuditP1
  - eventadjustmentauditp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EventAdjustmentAuditP1

## 📌 Visão Geral

View Object para extração BICC de dados de Event Adjustment Audit P1. Acessa as tabelas: PJB_EVENT_ADJ_ACTIVITIES.

**Caminho:** `FscmTopModelAM.BillingEventAM.EventAdjustmentAuditP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 3 | 5 | 36% |

---

## 🔗 Tabelas Relacionadas

- [[pjb_event_adj_activities|PJB_EVENT_ADJ_ACTIVITIES]] — 14 atributos (3 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[pjb_event_adj_activities|PJB_EVENT_ADJ_ACTIVITIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActivityDate | ACTIVITY_DATE | 🔑 | ✅ |
| 2 | AdjustmentType | ADJUSTMENT_TYPE | 🔑 | ✅ |
| 3 | EventId | EVENT_ID | 🔑 | ✅ |
| 4 | EvtAdjAuditPEOAdjOrigin | ADJ_ORIGIN | — | — |
| 5 | EvtAdjAuditPEOCreatedBy | CREATED_BY | — | — |
| 6 | EvtAdjAuditPEOCreationDate | CREATION_DATE | — | — |
| 7 | EvtAdjAuditPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 8 | EvtAdjAuditPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 9 | EvtAdjAuditPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | EvtAdjAuditPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | EvtAdjAuditPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | EvtAdjAuditPEOModuleCode | MODULE_CODE | — | ✅ |
| 13 | EvtAdjAuditPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | EvtAdjAuditPEORequestId | REQUEST_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
