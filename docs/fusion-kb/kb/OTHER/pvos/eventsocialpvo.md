---
id: DOC-OTHER-PVO-EventSocialPVO
doc_type: system-doc
title: "EventSocialPVO — PVO Cross-Module"
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
  - EventSocialPVO
  - eventsocialpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EventSocialPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Event Social. Acessa as tabelas: WLF_EVENT_SOCIAL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ContentAM.EventSocialPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 1 | 6 | 35% |

---

## 🔗 Tabelas Relacionadas

- [[wlf_event_social|WLF_EVENT_SOCIAL]] — 17 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[wlf_event_social|WLF_EVENT_SOCIAL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventSocialPEOComments | COMMENTS | — | ✅ |
| 2 | EventSocialPEOCreatedBy | CREATED_BY | — | — |
| 3 | EventSocialPEOCreationDate | CREATION_DATE | — | — |
| 4 | EventSocialPEOData | DATA | — | — |
| 5 | EventSocialPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 6 | EventSocialPEOEventId | EVENT_ID | — | — |
| 7 | EventSocialPEOEventSocialId | EVENT_SOCIAL_ID | 🔑 | ✅ |
| 8 | EventSocialPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | EventSocialPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | EventSocialPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | EventSocialPEOLatestSocialInteractionId | LATEST_SOCIAL_INTERACTION_ID | — | — |
| 12 | EventSocialPEOObjectId | OBJECT_ID | — | — |
| 13 | EventSocialPEOObjectType | OBJECT_TYPE | — | — |
| 14 | EventSocialPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | EventSocialPEORating | RATING | — | ✅ |
| 16 | EventSocialPEORatingDate | RATING_DATE | — | ✅ |
| 17 | EventSocialPEOStatus | STATUS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
