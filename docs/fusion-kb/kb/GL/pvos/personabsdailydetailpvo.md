---
id: DOC-GL-PVO-PersonAbsDailyDetailPVO
doc_type: system-doc
title: "PersonAbsDailyDetailPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PersonAbsDailyDetailPVO
  - personabsdailydetailpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonAbsDailyDetailPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Person Abs Daily Detail. Acessa as tabelas: ANC_PER_ABS_DAILY_DTLS, PER_ALL_ASSIGNMENTS_M, PER_ALL_PEOPLE_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GlobalAbsencesAM.PersonAbsDailyDetailPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 3 | 2 | 10 | 37% |

---

## 🔗 Tabelas Relacionadas

- [[anc_per_abs_daily_dtls|ANC_PER_ABS_DAILY_DTLS]] — 19 atributos (2 PKs, 10 BICC)
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 5 atributos
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 3 atributos

---

## ⚙️ Atributos

### [[anc_per_abs_daily_dtls|ANC_PER_ABS_DAILY_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsDate | ABS_DATE | — | — |
| 2 | AbsDays | ABS_DAYS | — | ✅ |
| 3 | AbsHours | ABS_HOURS | — | ✅ |
| 4 | AbsencePlanId | ABSENCE_PLAN_ID | — | — |
| 5 | AbsenceTypeId | ABSENCE_TYPE_ID | — | — |
| 6 | AbsenceTypeReasonId | ABSENCE_TYPE_REASON_ID | — | — |
| 7 | AssignmentId | ASSIGNMENT_ID | — | — |
| 8 | CreatedBy | CREATED_BY | — | ✅ |
| 9 | CreationDate | CREATION_DATE | — | ✅ |
| 10 | EnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 11 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | PerAbsDailyDtlId | PER_ABS_DAILY_DTL_ID | 🔑 | ✅ |
| 16 | PerAbsenceEntryId | PER_ABSENCE_ENTRY_ID | — | ✅ |
| 17 | PersonId | PERSON_ID | — | — |
| 18 | ScheduledUnits | SCHEDULED_UNITS | — | — |
| 19 | Uom | UOM | — | ✅ |

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 2 | AssignmentPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | AssignmentPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 4 | AssignmentPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 5 | AssignmentPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | PersonId1 | PERSON_ID | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
