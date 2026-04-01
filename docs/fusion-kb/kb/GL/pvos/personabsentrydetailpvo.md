---
id: DOC-GL-PVO-PersonAbsEntryDetailPVO
doc_type: system-doc
title: "PersonAbsEntryDetailPVO — PVO General Ledger"
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
  - PersonAbsEntryDetailPVO
  - personabsentrydetailpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonAbsEntryDetailPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Person Abs Entry Detail. Acessa as tabelas: ANC_PER_ABS_ENTRY_DTLS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GlobalAbsencesAM.PersonAbsEntryDetailPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 2 | 13 | 76% |

---

## 🔗 Tabelas Relacionadas

- [[anc_per_abs_entry_dtls|ANC_PER_ABS_ENTRY_DTLS]] — 17 atributos (2 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[anc_per_abs_entry_dtls|ANC_PER_ABS_ENTRY_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsenceDate | ABSENCE_DATE | — | ✅ |
| 2 | AbsenceDatetime | ABSENCE_DATETIME | — | ✅ |
| 3 | AbsenceEndDatetime | ABSENCE_END_DATETIME | — | — |
| 4 | AssignmentId | ASSIGNMENT_ID | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | Duration | DURATION | — | ✅ |
| 8 | EndTime | END_TIME | — | ✅ |
| 9 | EnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | PerAbsEntryDtlId | PER_ABS_ENTRY_DTL_ID | 🔑 | ✅ |
| 15 | PerAbsenceEntryId | PER_ABSENCE_ENTRY_ID | — | ✅ |
| 16 | PersonAbsEntryDetailPEODurPrefCd | DUR_PREF_CD | — | — |
| 17 | StartTime | START_TIME | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
