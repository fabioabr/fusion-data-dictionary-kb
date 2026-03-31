---
id: DOC-OTHER-PVO-MeetingRevwContentPVO
doc_type: system-doc
title: "MeetingRevwContentPVO — PVO Cross-Module"
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
  - MeetingRevwContentPVO
  - meetingrevwcontentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MeetingRevwContentPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Meeting Revw Content. Acessa as tabelas: HRR_MEETING_REVW_CONTENT.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmTalentCalibMeetingsAM.MeetingRevwContentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 3 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hrr_meeting_revw_content|HRR_MEETING_REVW_CONTENT]] — 12 atributos (3 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[hrr_meeting_revw_content|HRR_MEETING_REVW_CONTENT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | MeetingId | MEETING_ID | 🔑 | ✅ |
| 8 | MetricId | METRIC_ID | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | ReviewContentId | REVIEW_CONTENT_ID | 🔑 | ✅ |
| 11 | UseAsAxisFlag | USE_AS_AXIS_FLAG | — | ✅ |
| 12 | UseAsUnderlayFlag | USE_AS_UNDERLAY_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
