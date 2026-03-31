---
id: DOC-OTHER-PVO-ScheduleDetailExtractPVO
doc_type: system-doc
title: "ScheduleDetailExtractPVO — PVO Cross-Module"
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
  - ScheduleDetailExtractPVO
  - scheduledetailextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ScheduleDetailExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Schedule Detail Extract. Acessa as tabelas: ZMM_SR_SCHEDULE_DTLS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.ScheduleDetailExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[zmm_sr_schedule_dtls|ZMM_SR_SCHEDULE_DTLS]] — 13 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[zmm_sr_schedule_dtls|ZMM_SR_SCHEDULE_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AvlExceptionId | AVL_EXCEPTION_ID | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | EndDateTime | END_DATE_TIME | — | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | RequestId | REQUEST_ID | — | ✅ |
| 10 | ScheduleDetailId | SCHEDULE_DETAIL_ID | 🔑 | ✅ |
| 11 | ScheduleId | SCHEDULE_ID | — | ✅ |
| 12 | ShiftId | SHIFT_ID | — | ✅ |
| 13 | StartDateTime | START_DATE_TIME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
