---
id: DOC-OTHER-PVO-YearStartDateExtractPVO
doc_type: system-doc
title: "YearStartDateExtractPVO — PVO Cross-Module"
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
  - YearStartDateExtractPVO
  - yearstartdateextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# YearStartDateExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Year Start Date Extract. Acessa as tabelas: ZMM_SR_YEAR_START_DATES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.YearStartDateExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 1 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[zmm_sr_year_start_dates|ZMM_SR_YEAR_START_DATES]] — 10 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[zmm_sr_year_start_dates|ZMM_SR_YEAR_START_DATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | RequestId | REQUEST_ID | — | ✅ |
| 8 | ScheduleId | SCHEDULE_ID | — | ✅ |
| 9 | YearStartDate | YEAR_START_DATE | — | ✅ |
| 10 | YearStartDateId | YEAR_START_DATE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
