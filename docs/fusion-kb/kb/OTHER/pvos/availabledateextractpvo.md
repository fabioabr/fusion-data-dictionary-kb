---
id: DOC-OTHER-PVO-AvailableDateExtractPVO
doc_type: system-doc
title: "AvailableDateExtractPVO — PVO Cross-Module"
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
  - AvailableDateExtractPVO
  - availabledateextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AvailableDateExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Available Date Extract. Acessa as tabelas: ZMM_SR_AVAILABLE_DATES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.AvailableDateExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[zmm_sr_available_dates|ZMM_SR_AVAILABLE_DATES]] — 15 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[zmm_sr_available_dates|ZMM_SR_AVAILABLE_DATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AvlDateId | AVL_DATE_ID | 🔑 | ✅ |
| 2 | CalendarDate | CALENDAR_DATE | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | NextDate | NEXT_DATE | — | ✅ |
| 9 | NextSeqNum | NEXT_SEQ_NUM | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | PriorDate | PRIOR_DATE | — | ✅ |
| 12 | PriorSeqNum | PRIOR_SEQ_NUM | — | ✅ |
| 13 | RequestId | REQUEST_ID | — | ✅ |
| 14 | ScheduleId | SCHEDULE_ID | — | ✅ |
| 15 | SeqNum | SEQ_NUM | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
