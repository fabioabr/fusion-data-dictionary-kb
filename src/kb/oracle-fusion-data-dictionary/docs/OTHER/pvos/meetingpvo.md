---
id: DOC-OTHER-PVO-MeetingPVO
doc_type: system-doc
title: "MeetingPVO — PVO Cross-Module"
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
  - MeetingPVO
  - meetingpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MeetingPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Meeting. Acessa as tabelas: HRR_MEETINGS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmTalentCalibMeetingsAM.MeetingPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 1 | 2 | 21 | 91% |

---

## 🔗 Tabelas Relacionadas

- [[hrr_meetings|HRR_MEETINGS]] — 23 atributos (2 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[hrr_meetings|HRR_MEETINGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | DashboardTmplId | DASHBOARD_TMPL_ID | — | ✅ |
| 5 | DataSubmitDate | DATA_SUBMIT_DATE | — | ✅ |
| 6 | DataValidityCode | DATA_VALIDITY_CODE | — | — |
| 7 | IncludeMatrixMgmt | INCLUDE_MATRIX_MGMT | — | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | MeetingDate | MEETING_DATE | — | ✅ |
| 12 | MeetingFacilitatorNotes | MEETING_FACILITATOR_NOTES | — | ✅ |
| 13 | MeetingId | MEETING_ID | 🔑 | ✅ |
| 14 | MeetingInstructions | MEETING_INSTRUCTIONS | — | ✅ |
| 15 | MeetingLeaderId | MEETING_LEADER_ID | — | ✅ |
| 16 | MeetingOrganizationId | MEETING_ORGANIZATION_ID | — | ✅ |
| 17 | MeetingPurpose | MEETING_PURPOSE | — | ✅ |
| 18 | MeetingStatusCode | MEETING_STATUS_CODE | — | ✅ |
| 19 | MeetingSubmissionDate | MEETING_SUBMISSION_DATE | — | ✅ |
| 20 | MeetingSubmitStatusCode | MEETING_SUBMIT_STATUS_CODE | — | ✅ |
| 21 | MeetingTitle | MEETING_TITLE | — | ✅ |
| 22 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 23 | PrefReviewQualifierId | PREF_REVIEW_QUALIFIER_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
