---
id: DOC-OTHER-PVO-PatternDetailExtractPVO
doc_type: system-doc
title: "PatternDetailExtractPVO — PVO Cross-Module"
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
  - PatternDetailExtractPVO
  - patterndetailextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PatternDetailExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Pattern Detail Extract. Acessa as tabelas: ZMM_SR_PATTERN_DTLS, ZMM_SR_SHIFTS_B.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.PatternDetailExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 43 | 2 | 1 | 43 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[zmm_sr_pattern_dtls|ZMM_SR_PATTERN_DTLS]] — 42 atributos (1 PKs, 42 BICC)
- [[zmm_sr_shifts_b|ZMM_SR_SHIFTS_B]] — 1 atributos (1 BICC)

---

## ⚙️ Atributos

### [[zmm_sr_pattern_dtls|ZMM_SR_PATTERN_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PatternDetailPEOAttribute1 | ATTRIBUTE1 | — | ✅ |
| 2 | PatternDetailPEOAttribute10 | ATTRIBUTE10 | — | ✅ |
| 3 | PatternDetailPEOAttribute11 | ATTRIBUTE11 | — | ✅ |
| 4 | PatternDetailPEOAttribute12 | ATTRIBUTE12 | — | ✅ |
| 5 | PatternDetailPEOAttribute13 | ATTRIBUTE13 | — | ✅ |
| 6 | PatternDetailPEOAttribute14 | ATTRIBUTE14 | — | ✅ |
| 7 | PatternDetailPEOAttribute15 | ATTRIBUTE15 | — | ✅ |
| 8 | PatternDetailPEOAttribute16 | ATTRIBUTE16 | — | ✅ |
| 9 | PatternDetailPEOAttribute17 | ATTRIBUTE17 | — | ✅ |
| 10 | PatternDetailPEOAttribute18 | ATTRIBUTE18 | — | ✅ |
| 11 | PatternDetailPEOAttribute19 | ATTRIBUTE19 | — | ✅ |
| 12 | PatternDetailPEOAttribute2 | ATTRIBUTE2 | — | ✅ |
| 13 | PatternDetailPEOAttribute20 | ATTRIBUTE20 | — | ✅ |
| 14 | PatternDetailPEOAttribute21 | ATTRIBUTE21 | — | ✅ |
| 15 | PatternDetailPEOAttribute22 | ATTRIBUTE22 | — | ✅ |
| 16 | PatternDetailPEOAttribute23 | ATTRIBUTE23 | — | ✅ |
| 17 | PatternDetailPEOAttribute24 | ATTRIBUTE24 | — | ✅ |
| 18 | PatternDetailPEOAttribute25 | ATTRIBUTE25 | — | ✅ |
| 19 | PatternDetailPEOAttribute26 | ATTRIBUTE26 | — | ✅ |
| 20 | PatternDetailPEOAttribute27 | ATTRIBUTE27 | — | ✅ |
| 21 | PatternDetailPEOAttribute28 | ATTRIBUTE28 | — | ✅ |
| 22 | PatternDetailPEOAttribute29 | ATTRIBUTE29 | — | ✅ |
| 23 | PatternDetailPEOAttribute3 | ATTRIBUTE3 | — | ✅ |
| 24 | PatternDetailPEOAttribute30 | ATTRIBUTE30 | — | ✅ |
| 25 | PatternDetailPEOAttribute4 | ATTRIBUTE4 | — | ✅ |
| 26 | PatternDetailPEOAttribute5 | ATTRIBUTE5 | — | ✅ |
| 27 | PatternDetailPEOAttribute6 | ATTRIBUTE6 | — | ✅ |
| 28 | PatternDetailPEOAttribute7 | ATTRIBUTE7 | — | ✅ |
| 29 | PatternDetailPEOAttribute8 | ATTRIBUTE8 | — | ✅ |
| 30 | PatternDetailPEOAttribute9 | ATTRIBUTE9 | — | ✅ |
| 31 | PatternDetailPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 32 | PatternDetailPEOCreatedBy | CREATED_BY | — | ✅ |
| 33 | PatternDetailPEOCreationDate | CREATION_DATE | — | ✅ |
| 34 | PatternDetailPEODayStartNum | DAY_START_NUM | — | ✅ |
| 35 | PatternDetailPEODayStopNum | DAY_STOP_NUM | — | ✅ |
| 36 | PatternDetailPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 37 | PatternDetailPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 38 | PatternDetailPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 39 | PatternDetailPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 40 | PatternDetailPEOPatternDtlSeqNum | PATTERN_DTL_SEQ_NUM | — | ✅ |
| 41 | PatternDetailPEOPatternId | PATTERN_ID | — | ✅ |
| 42 | PatternDtlId | PATTERN_DTL_ID | 🔑 | ✅ |

### [[zmm_sr_shifts_b|ZMM_SR_SHIFTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ShiftPEOShiftId | SHIFT_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
