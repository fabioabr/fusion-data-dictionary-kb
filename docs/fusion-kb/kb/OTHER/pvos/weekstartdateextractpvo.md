---
id: DOC-OTHER-PVO-WeekStartDateExtractPVO
doc_type: system-doc
title: "WeekStartDateExtractPVO — PVO Cross-Module"
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
  - WeekStartDateExtractPVO
  - weekstartdateextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WeekStartDateExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Week Start Date Extract. Acessa as tabelas: ZMM_SR_WEEK_START_DATES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.WeekStartDateExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[zmm_sr_week_start_dates|ZMM_SR_WEEK_START_DATES]] — 13 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[zmm_sr_week_start_dates|ZMM_SR_WEEK_START_DATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | NextDate | NEXT_DATE | — | ✅ |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | PriorDate | PRIOR_DATE | — | ✅ |
| 9 | RequestId | REQUEST_ID | — | ✅ |
| 10 | ScheduleId | SCHEDULE_ID | — | ✅ |
| 11 | SeqNum | SEQ_NUM | — | ✅ |
| 12 | WeekStartDate | WEEK_START_DATE | — | ✅ |
| 13 | WeekStartDateId | WEEK_START_DATE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
