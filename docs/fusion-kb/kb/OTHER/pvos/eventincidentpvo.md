---
id: DOC-OTHER-PVO-EventIncidentPVO
doc_type: system-doc
title: "EventIncidentPVO — PVO Cross-Module"
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
  - EventIncidentPVO
  - eventincidentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EventIncidentPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Event Incident. Acessa as tabelas: WLF_EVENT_INCIDENTS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ContentAM.EventIncidentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 4 | 29% |

---

## 🔗 Tabelas Relacionadas

- [[wlf_event_incidents|WLF_EVENT_INCIDENTS]] — 14 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[wlf_event_incidents|WLF_EVENT_INCIDENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventIncidentPEOComments | COMMENTS | — | — |
| 2 | EventIncidentPEOCreatedBy | CREATED_BY | — | — |
| 3 | EventIncidentPEOCreationDate | CREATION_DATE | — | — |
| 4 | EventIncidentPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 5 | EventIncidentPEOEventDispositionId | EVENT_DISPOSITION_ID | — | — |
| 6 | EventIncidentPEOEventId | EVENT_ID | — | — |
| 7 | EventIncidentPEOEventIncidentId | EVENT_INCIDENT_ID | 🔑 | ✅ |
| 8 | EventIncidentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | EventIncidentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | EventIncidentPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | EventIncidentPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | EventIncidentPEOReasonCode | REASON_CODE | — | ✅ |
| 13 | EventIncidentPEOStatus | STATUS | — | ✅ |
| 14 | EventIncidentPEOStatusLastModified | STATUS_LAST_MODIFIED | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
