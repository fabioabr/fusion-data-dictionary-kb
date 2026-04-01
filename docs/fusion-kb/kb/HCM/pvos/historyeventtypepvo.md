---
id: DOC-HCM-PVO-HistoryEventTypePVO
doc_type: system-doc
title: "HistoryEventTypePVO — PVO Human Capital Management"
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
  - HistoryEventTypePVO
  - historyeventtypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HistoryEventTypePVO

## 📌 Visão Geral

Disponibiliza tipos de eventos históricos de recrutamento (candidatura, entrevista, oferta). Tabela de referência para rastreamento de etapas seletivas.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecruitingCommonAM.HistoryEventTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 2 | 1 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[irc_hist_event_b|IRC_HIST_EVENT_B]] — 11 atributos (1 PKs, 11 BICC)
- [[irc_hist_event_tl|IRC_HIST_EVENT_TL]] — 10 atributos (10 BICC)

---

## ⚙️ Atributos

### [[irc_hist_event_b|IRC_HIST_EVENT_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventTypeId | EVENT_TYPE_ID | 🔑 | ✅ |
| 2 | HistoryEventTypeBPEOCode | CODE | — | ✅ |
| 3 | HistoryEventTypeBPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | HistoryEventTypeBPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | HistoryEventTypeBPEOIsBackward | IS_BACKWARD | — | ✅ |
| 6 | HistoryEventTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | HistoryEventTypeBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | HistoryEventTypeBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | HistoryEventTypeBPEOModuleId | MODULE_ID | — | ✅ |
| 10 | HistoryEventTypeBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | HistoryEventTypeBPEOShowInUi | SHOW_IN_UI | — | ✅ |

### [[irc_hist_event_tl|IRC_HIST_EVENT_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HistoryEventTypeTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | HistoryEventTypeTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | HistoryEventTypeTranslationPEOEventTypeId | EVENT_TYPE_ID | — | ✅ |
| 4 | HistoryEventTypeTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 5 | HistoryEventTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | HistoryEventTypeTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | HistoryEventTypeTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | HistoryEventTypeTranslationPEOName | NAME | — | ✅ |
| 9 | HistoryEventTypeTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | HistoryEventTypeTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
