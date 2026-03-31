---
id: DOC-OTHER-PVO-EventAssignmentDestinationPVO
doc_type: system-doc
title: "EventAssignmentDestinationPVO — PVO Cross-Module"
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
  - EventAssignmentDestinationPVO
  - eventassignmentdestinationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EventAssignmentDestinationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Event Assignment Destination. Acessa as tabelas: WLF_ASSIGNMENT_DESTINATIONS_F, WLF_BI_ANALYSIS_DESTINATIONS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ContentAM.EventAssignmentDestinationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 2 | 3 | 8 | 47% |

---

## 🔗 Tabelas Relacionadas

- [[wlf_assignment_destinations_f|WLF_ASSIGNMENT_DESTINATIONS_F]] — 14 atributos (3 PKs, 6 BICC)
- [[wlf_bi_analysis_destinations|WLF_BI_ANALYSIS_DESTINATIONS]] — 3 atributos (2 BICC)

---

## ⚙️ Atributos

### [[wlf_assignment_destinations_f|WLF_ASSIGNMENT_DESTINATIONS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventAssignmentDestinationDEOAssignedToId | ASSIGNED_TO_ID | — | — |
| 2 | EventAssignmentDestinationDEOAssignedToType | ASSIGNED_TO_TYPE | — | ✅ |
| 3 | EventAssignmentDestinationDEOAssignmentDestinationId | ASSIGNMENT_DESTINATION_ID | 🔑 | ✅ |
| 4 | EventAssignmentDestinationDEOCreatedBy | CREATED_BY | — | — |
| 5 | EventAssignmentDestinationDEOCreationDate | CREATION_DATE | — | — |
| 6 | EventAssignmentDestinationDEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 7 | EventAssignmentDestinationDEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 8 | EventAssignmentDestinationDEOEnterpriseId | ENTERPRISE_ID | — | — |
| 9 | EventAssignmentDestinationDEOEventAssignmentId | EVENT_ASSIGNMENT_ID | — | — |
| 10 | EventAssignmentDestinationDEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | EventAssignmentDestinationDEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | EventAssignmentDestinationDEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | EventAssignmentDestinationDEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | EventAssignmentDestinationDEOOperation | OPERATION | — | ✅ |

### [[wlf_bi_analysis_destinations|WLF_BI_ANALYSIS_DESTINATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BIAnalysisDestinationsPEOAnalysisReportId | ANALYSIS_REPORT_ID | — | — |
| 2 | BIAnalysisDestinationsPEOReportName | REPORT_NAME | — | ✅ |
| 3 | BIAnalysisDestinationsPEOReportPath | REPORT_PATH | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
