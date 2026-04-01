---
id: DOC-OTHER-PVO-AllocateChecklistTaskTranslation
doc_type: system-doc
title: "AllocateChecklistTaskTranslation — PVO Cross-Module"
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
  - AllocateChecklistTaskTranslation
  - allocatechecklisttasktranslation
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AllocateChecklistTaskTranslation

## 📌 Visão Geral

View Object para extração BICC de dados de Allocate Checklist Task Translation. Acessa as tabelas: PER_ALLOCATED_TASKS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.HcmChecklistBiccExtractAM.AllocateChecklistTaskTranslation`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 1 | 2 | 26 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[per_allocated_tasks_tl|PER_ALLOCATED_TASKS_TL]] — 26 atributos (2 PKs, 26 BICC)

---

## ⚙️ Atributos

### [[per_allocated_tasks_tl|PER_ALLOCATED_TASKS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionUrl | ACTION_URL | — | ✅ |
| 2 | ActivityAction1Label | ACTIVITY_ACTION1_LABEL | — | ✅ |
| 3 | ActivityAction2Label | ACTIVITY_ACTION2_LABEL | — | ✅ |
| 4 | ActivityAction3Label | ACTIVITY_ACTION3_LABEL | — | ✅ |
| 5 | ActivityAction4Label | ACTIVITY_ACTION4_LABEL | — | ✅ |
| 6 | ActivityAction5Label | ACTIVITY_ACTION5_LABEL | — | ✅ |
| 7 | AllocatedTaskId | ALLOCATED_TASK_ID | 🔑 | ✅ |
| 8 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 9 | CalendarActionLabel | CALENDAR_ACTION_LABEL | — | ✅ |
| 10 | CompleteActionLabel | COMPLETE_ACTION_LABEL | — | ✅ |
| 11 | CreatedBy | CREATED_BY | — | ✅ |
| 12 | CreationDate | CREATION_DATE | — | ✅ |
| 13 | Description | DESCRIPTION | — | ✅ |
| 14 | Language | LANGUAGE | 🔑 | ✅ |
| 15 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | MeetingLocation | MEETING_LOCATION | — | ✅ |
| 19 | NoteTitle | NOTE_TITLE | — | ✅ |
| 20 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 21 | RejectActionLabel | REJECT_ACTION_LABEL | — | ✅ |
| 22 | SaveActionLabel | SAVE_ACTION_LABEL | — | ✅ |
| 23 | SourceLang | SOURCE_LANG | — | ✅ |
| 24 | TaskDetails | TASK_DETAILS | — | ✅ |
| 25 | TaskName | TASK_NAME | — | ✅ |
| 26 | UserDisplayName | USER_DISPLAY_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
