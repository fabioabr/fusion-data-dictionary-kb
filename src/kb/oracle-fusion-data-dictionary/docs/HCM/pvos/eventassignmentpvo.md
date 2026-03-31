---
id: DOC-HCM-PVO-EventAssignmentPVO
doc_type: system-doc
title: "EventAssignmentPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - EventAssignmentPVO
  - eventassignmentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EventAssignmentPVO

## 📌 Visão Geral

Disponibiliza atribuições de eventos de aprendizagem com vigência e status. Utilizado para rastrear designações de treinamentos obrigatórios e opcionais.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ContentAM.EventAssignmentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 3 | 5 | 28% |

---

## 🔗 Tabelas Relacionadas

- [[wlf_event_assignments_f|WLF_EVENT_ASSIGNMENTS_F]] — 18 atributos (3 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[wlf_event_assignments_f|WLF_EVENT_ASSIGNMENTS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventAssignmentDEOAssignmentProfileNumber | ASSIGNMENT_PROFILE_NUMBER | — | — |
| 2 | EventAssignmentDEOAssignmentRuleId | ASSIGNMENT_RULE_ID | — | — |
| 3 | EventAssignmentDEOAssignmentStartDate | ASSIGNMENT_START_DATE | — | — |
| 4 | EventAssignmentDEOComments | COMMENTS | — | — |
| 5 | EventAssignmentDEOCreatedBy | CREATED_BY | — | — |
| 6 | EventAssignmentDEOCreationDate | CREATION_DATE | — | — |
| 7 | EventAssignmentDEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 8 | EventAssignmentDEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 9 | EventAssignmentDEOEnterpriseId | ENTERPRISE_ID | — | — |
| 10 | EventAssignmentDEOEventAssignmentId | EVENT_ASSIGNMENT_ID | 🔑 | ✅ |
| 11 | EventAssignmentDEOEventId | EVENT_ID | — | — |
| 12 | EventAssignmentDEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | EventAssignmentDEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | EventAssignmentDEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | EventAssignmentDEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | EventAssignmentDEOProcessedDate | PROCESSED_DATE | — | — |
| 17 | EventAssignmentDEORequestDetailId | REQUEST_DETAIL_ID | — | — |
| 18 | EventAssignmentDEOStatus | STATUS | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
