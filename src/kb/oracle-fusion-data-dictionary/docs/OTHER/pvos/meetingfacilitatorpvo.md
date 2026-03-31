---
id: DOC-OTHER-PVO-MeetingFacilitatorPVO
doc_type: system-doc
title: "MeetingFacilitatorPVO — PVO Cross-Module"
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
  - MeetingFacilitatorPVO
  - meetingfacilitatorpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MeetingFacilitatorPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Meeting Facilitator. Acessa as tabelas: HRR_MEETING_FACILITATORS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmTalentCalibMeetingsAM.MeetingFacilitatorPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 4 | 5 | 50% |

---

## 🔗 Tabelas Relacionadas

- [[hrr_meeting_facilitators|HRR_MEETING_FACILITATORS]] — 10 atributos (4 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[hrr_meeting_facilitators|HRR_MEETING_FACILITATORS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | EnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 4 | FacilitatorPersonId | FACILITATOR_PERSON_ID | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | MeetingFacilitatorId | MEETING_FACILITATOR_ID | 🔑 | ✅ |
| 9 | MeetingId | MEETING_ID | 🔑 | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
