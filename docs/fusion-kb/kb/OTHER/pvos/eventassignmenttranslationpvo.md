---
id: DOC-OTHER-PVO-EventAssignmentTranslationPVO
doc_type: system-doc
title: "EventAssignmentTranslationPVO — PVO Cross-Module"
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
  - EventAssignmentTranslationPVO
  - eventassignmenttranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EventAssignmentTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Event Assignment Translation. Acessa as tabelas: WLF_EVENT_ASSIGNMENTS_F_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ContentAM.EventAssignmentTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 4 | 7 | 47% |

---

## 🔗 Tabelas Relacionadas

- [[wlf_event_assignments_f_tl|WLF_EVENT_ASSIGNMENTS_F_TL]] — 15 atributos (4 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[wlf_event_assignments_f_tl|WLF_EVENT_ASSIGNMENTS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventAssignmentTranslationDEOComments | COMMENTS | — | — |
| 2 | EventAssignmentTranslationDEOCreatedBy | CREATED_BY | — | — |
| 3 | EventAssignmentTranslationDEOCreationDate | CREATION_DATE | — | — |
| 4 | EventAssignmentTranslationDEODescription | DESCRIPTION | — | ✅ |
| 5 | EventAssignmentTranslationDEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 6 | EventAssignmentTranslationDEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 7 | EventAssignmentTranslationDEOEnterpriseId | ENTERPRISE_ID | — | — |
| 8 | EventAssignmentTranslationDEOEventAssignmentId | EVENT_ASSIGNMENT_ID | 🔑 | ✅ |
| 9 | EventAssignmentTranslationDEOLanguage | LANGUAGE | 🔑 | ✅ |
| 10 | EventAssignmentTranslationDEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | EventAssignmentTranslationDEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | EventAssignmentTranslationDEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | EventAssignmentTranslationDEOName | NAME | — | ✅ |
| 14 | EventAssignmentTranslationDEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | EventAssignmentTranslationDEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
