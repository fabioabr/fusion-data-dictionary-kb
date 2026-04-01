---
id: DOC-OTHER-PVO-HNSInvestigationNotesPVO
doc_type: system-doc
title: "HNSInvestigationNotesPVO — PVO Cross-Module"
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
  - HNSInvestigationNotesPVO
  - hnsinvestigationnotespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HNSInvestigationNotesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de HNSInvestigation Notes. Acessa as tabelas: HNS_NOTES.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HealthandSafetyAM.HNSInvestigationNotesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hns_notes|HNS_NOTES]] — 13 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[hns_notes|HNS_NOTES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HNSNotesPEOAuthorId | AUTHOR_ID | — | ✅ |
| 2 | HNSNotesPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | HNSNotesPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | HNSNotesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | HNSNotesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | HNSNotesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | HNSNotesPEONotes | NOTES | — | ✅ |
| 8 | HNSNotesPEONotesId | NOTES_ID | 🔑 | ✅ |
| 9 | HNSNotesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | HNSNotesPEOTaskId | TASK_ID | — | ✅ |
| 11 | HNSNotesPEOTaskTypeCode | TASK_TYPE_CODE | — | ✅ |
| 12 | HNSNotesPEOUpdatedBy | UPDATED_BY | — | ✅ |
| 13 | HNSNotesPEOUpdatedDate | UPDATED_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
