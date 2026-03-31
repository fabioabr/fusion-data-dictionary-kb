---
id: DOC-GL-PVO-PersonAbsMaternityPVO
doc_type: system-doc
title: "PersonAbsMaternityPVO — PVO General Ledger"
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
  - PersonAbsMaternityPVO
  - personabsmaternitypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonAbsMaternityPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Person Abs Maternity. Acessa as tabelas: ANC_PER_ABS_MATERNITY.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GlobalAbsencesAM.PersonAbsMaternityPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 1 | 2 | 14 | 64% |

---

## 🔗 Tabelas Relacionadas

- [[anc_per_abs_maternity|ANC_PER_ABS_MATERNITY]] — 22 atributos (2 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[anc_per_abs_maternity|ANC_PER_ABS_MATERNITY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActualChildBirthDt | ACTUAL_CHILD_BIRTH_DT | — | ✅ |
| 2 | ActualDuration | ACTUAL_DURATION | — | ✅ |
| 3 | ActualReturnDt | ACTUAL_RETURN_DT | — | ✅ |
| 4 | ActualStDt | ACTUAL_ST_DT | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | — |
| 6 | CreationDate | CREATION_DATE | — | — |
| 7 | EnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 8 | ExpectedDtChildBirth | EXPECTED_DT_CHILD_BIRTH | — | ✅ |
| 9 | ExpectedEndDate | EXPECTED_END_DATE | — | ✅ |
| 10 | ExpectedWkChildBirth | EXPECTED_WK_CHILD_BIRTH | — | — |
| 11 | IntendToWork | INTEND_TO_WORK | — | ✅ |
| 12 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | LeaveDuration | LEAVE_DURATION | — | ✅ |
| 16 | MatchingDate | MATCHING_DATE | — | — |
| 17 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | OpenEndedFlag | OPEN_ENDED_FLAG | — | ✅ |
| 19 | PerAbsMatId | PER_ABS_MAT_ID | 🔑 | ✅ |
| 20 | PerAbsenceEntryId | PER_ABSENCE_ENTRY_ID | — | — |
| 21 | PlannedReturnDt | PLANNED_RETURN_DT | — | ✅ |
| 22 | PlannedStDt | PLANNED_ST_DT | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
