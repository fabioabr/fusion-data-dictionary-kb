---
id: DOC-OTHER-PVO-EventAdjustmentAuditExtractPVO
doc_type: system-doc
title: "EventAdjustmentAuditExtractPVO — PVO Cross-Module"
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
  - EventAdjustmentAuditExtractPVO
  - eventadjustmentauditextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EventAdjustmentAuditExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Event Adjustment Audit Extract. Acessa as tabelas: PJB_EVENT_ADJ_ACTIVITIES.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjbBiccExtractAM.EventAdjustmentAuditExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 3 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjb_event_adj_activities|PJB_EVENT_ADJ_ACTIVITIES]] — 14 atributos (3 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[pjb_event_adj_activities|PJB_EVENT_ADJ_ACTIVITIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventAdjustmentAuditPEOActivityDate | ACTIVITY_DATE | 🔑 | ✅ |
| 2 | EventAdjustmentAuditPEOAdjOrigin | ADJ_ORIGIN | — | ✅ |
| 3 | EventAdjustmentAuditPEOAdjustmentType | ADJUSTMENT_TYPE | 🔑 | ✅ |
| 4 | EventAdjustmentAuditPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | EventAdjustmentAuditPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | EventAdjustmentAuditPEOEventId | EVENT_ID | 🔑 | ✅ |
| 7 | EventAdjustmentAuditPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 8 | EventAdjustmentAuditPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 9 | EventAdjustmentAuditPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | EventAdjustmentAuditPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | EventAdjustmentAuditPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | EventAdjustmentAuditPEOModuleCode | MODULE_CODE | — | ✅ |
| 13 | EventAdjustmentAuditPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | EventAdjustmentAuditPEORequestId | REQUEST_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
