---
id: DOC-OTHER-PVO-PeriodStartDateExtractPVO
doc_type: system-doc
title: "PeriodStartDateExtractPVO — PVO Cross-Module"
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
  - PeriodStartDateExtractPVO
  - periodstartdateextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PeriodStartDateExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Period Start Date Extract. Acessa as tabelas: ZMM_SR_PRD_START_DATES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.PeriodStartDateExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[zmm_sr_prd_start_dates|ZMM_SR_PRD_START_DATES]] — 13 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[zmm_sr_prd_start_dates|ZMM_SR_PRD_START_DATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | NextDate | NEXT_DATE | — | ✅ |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | PrdStartDate | PRD_START_DATE | — | ✅ |
| 9 | PrdStartDateId | PRD_START_DATE_ID | 🔑 | ✅ |
| 10 | PriorDate | PRIOR_DATE | — | ✅ |
| 11 | RequestId | REQUEST_ID | — | ✅ |
| 12 | ScheduleId | SCHEDULE_ID | — | ✅ |
| 13 | SeqNum | SEQ_NUM | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
