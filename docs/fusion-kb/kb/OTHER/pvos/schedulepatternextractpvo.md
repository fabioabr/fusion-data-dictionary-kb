---
id: DOC-OTHER-PVO-SchedulePatternExtractPVO
doc_type: system-doc
title: "SchedulePatternExtractPVO — PVO Cross-Module"
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
  - SchedulePatternExtractPVO
  - schedulepatternextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SchedulePatternExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Schedule Pattern Extract. Acessa as tabelas: ZMM_SR_SCHEDULE_PATTERNS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.SchedulePatternExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 1 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[zmm_sr_schedule_patterns|ZMM_SR_SCHEDULE_PATTERNS]] — 10 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[zmm_sr_schedule_patterns|ZMM_SR_SCHEDULE_PATTERNS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SchedulePatternId | SCHEDULE_PATTERN_ID | 🔑 | ✅ |
| 2 | SchedulePatternPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | SchedulePatternPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | SchedulePatternPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | SchedulePatternPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | SchedulePatternPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | SchedulePatternPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | SchedulePatternPEOPatternId | PATTERN_ID | — | ✅ |
| 9 | SchedulePatternPEOPatternSeqNum | PATTERN_SEQ_NUM | — | ✅ |
| 10 | SchedulePatternPEOScheduleId | SCHEDULE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
