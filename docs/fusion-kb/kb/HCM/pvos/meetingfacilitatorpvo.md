---
id: DOC-HCM-PVO-MeetingFacilitatorPVO
doc_type: system-doc
title: "MeetingFacilitatorPVO — PVO Human Capital Management"
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

Extrai facilitadores de reuniões de calibração de talentos (Talent Review). Identifica os responsáveis por conduzir sessões de avaliação coletiva de desempenho e potencial.

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

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
