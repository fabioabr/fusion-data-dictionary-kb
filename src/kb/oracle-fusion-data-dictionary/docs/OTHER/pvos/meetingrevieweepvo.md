---
id: DOC-OTHER-PVO-MeetingRevieweePVO
doc_type: system-doc
title: "MeetingRevieweePVO — PVO Cross-Module"
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
  - MeetingRevieweePVO
  - meetingrevieweepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MeetingRevieweePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Meeting Reviewee. Acessa as tabelas: HRR_MEETING_REVIEWEES.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmTalentCalibMeetingsAM.MeetingRevieweePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 4 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hrr_meeting_reviewees|HRR_MEETING_REVIEWEES]] — 12 atributos (4 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[hrr_meeting_reviewees|HRR_MEETING_REVIEWEES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | MeetingId | MEETING_ID | 🔑 | ✅ |
| 8 | MeetingRevieweeId | MEETING_REVIEWEE_ID | 🔑 | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | RevieweeAssignmentId | REVIEWEE_ASSIGNMENT_ID | — | ✅ |
| 11 | RevieweePersonId | REVIEWEE_PERSON_ID | 🔑 | ✅ |
| 12 | ReviewerPersonId | REVIEWER_PERSON_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
