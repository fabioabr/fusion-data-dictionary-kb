---
id: DOC-OTHER-PVO-MeetingParticipantPVO
doc_type: system-doc
title: "MeetingParticipantPVO — PVO Cross-Module"
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
  - MeetingParticipantPVO
  - meetingparticipantpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MeetingParticipantPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Meeting Participant. Acessa as tabelas: HRR_MEETING_PARTICIPANTS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmTalentCalibMeetingsAM.MeetingParticipantPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 4 | 6 | 50% |

---

## 🔗 Tabelas Relacionadas

- [[hrr_meeting_participants|HRR_MEETING_PARTICIPANTS]] — 12 atributos (4 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[hrr_meeting_participants|HRR_MEETING_PARTICIPANTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | DataSubmissionStatusCode | DATA_SUBMISSION_STATUS_CODE | — | — |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | MeetingId | MEETING_ID | 🔑 | ✅ |
| 9 | MeetingParticipantId | MEETING_PARTICIPANT_ID | 🔑 | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ParticipantPersonId | PARTICIPANT_PERSON_ID | 🔑 | ✅ |
| 12 | ParticipantTypeCode | PARTICIPANT_TYPE_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
