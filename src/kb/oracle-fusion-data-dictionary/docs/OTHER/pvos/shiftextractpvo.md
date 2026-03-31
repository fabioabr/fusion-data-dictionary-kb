---
id: DOC-OTHER-PVO-ShiftExtractPVO
doc_type: system-doc
title: "ShiftExtractPVO — PVO Cross-Module"
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
  - ShiftExtractPVO
  - shiftextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ShiftExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Shift Extract. Acessa as tabelas: ZMM_SR_SHIFTS_B, ZMM_SR_SHIFTS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.ShiftExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 50 | 2 | 1 | 49 | 98% |

---

## 🔗 Tabelas Relacionadas

- [[zmm_sr_shifts_b|ZMM_SR_SHIFTS_B]] — 47 atributos (1 PKs, 47 BICC)
- [[zmm_sr_shifts_tl|ZMM_SR_SHIFTS_TL]] — 3 atributos (2 BICC)

---

## ⚙️ Atributos

### [[zmm_sr_shifts_b|ZMM_SR_SHIFTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ShiftId | SHIFT_ID | 🔑 | ✅ |
| 2 | ShiftPEOAttribute1 | ATTRIBUTE1 | — | ✅ |
| 3 | ShiftPEOAttribute10 | ATTRIBUTE10 | — | ✅ |
| 4 | ShiftPEOAttribute11 | ATTRIBUTE11 | — | ✅ |
| 5 | ShiftPEOAttribute12 | ATTRIBUTE12 | — | ✅ |
| 6 | ShiftPEOAttribute13 | ATTRIBUTE13 | — | ✅ |
| 7 | ShiftPEOAttribute14 | ATTRIBUTE14 | — | ✅ |
| 8 | ShiftPEOAttribute15 | ATTRIBUTE15 | — | ✅ |
| 9 | ShiftPEOAttribute16 | ATTRIBUTE16 | — | ✅ |
| 10 | ShiftPEOAttribute17 | ATTRIBUTE17 | — | ✅ |
| 11 | ShiftPEOAttribute18 | ATTRIBUTE18 | — | ✅ |
| 12 | ShiftPEOAttribute19 | ATTRIBUTE19 | — | ✅ |
| 13 | ShiftPEOAttribute2 | ATTRIBUTE2 | — | ✅ |
| 14 | ShiftPEOAttribute20 | ATTRIBUTE20 | — | ✅ |
| 15 | ShiftPEOAttribute21 | ATTRIBUTE21 | — | ✅ |
| 16 | ShiftPEOAttribute22 | ATTRIBUTE22 | — | ✅ |
| 17 | ShiftPEOAttribute23 | ATTRIBUTE23 | — | ✅ |
| 18 | ShiftPEOAttribute24 | ATTRIBUTE24 | — | ✅ |
| 19 | ShiftPEOAttribute25 | ATTRIBUTE25 | — | ✅ |
| 20 | ShiftPEOAttribute26 | ATTRIBUTE26 | — | ✅ |
| 21 | ShiftPEOAttribute27 | ATTRIBUTE27 | — | ✅ |
| 22 | ShiftPEOAttribute28 | ATTRIBUTE28 | — | ✅ |
| 23 | ShiftPEOAttribute29 | ATTRIBUTE29 | — | ✅ |
| 24 | ShiftPEOAttribute3 | ATTRIBUTE3 | — | ✅ |
| 25 | ShiftPEOAttribute30 | ATTRIBUTE30 | — | ✅ |
| 26 | ShiftPEOAttribute4 | ATTRIBUTE4 | — | ✅ |
| 27 | ShiftPEOAttribute5 | ATTRIBUTE5 | — | ✅ |
| 28 | ShiftPEOAttribute6 | ATTRIBUTE6 | — | ✅ |
| 29 | ShiftPEOAttribute7 | ATTRIBUTE7 | — | ✅ |
| 30 | ShiftPEOAttribute8 | ATTRIBUTE8 | — | ✅ |
| 31 | ShiftPEOAttribute9 | ATTRIBUTE9 | — | ✅ |
| 32 | ShiftPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 33 | ShiftPEOAvailabilityCode | AVAILABILITY_CODE | — | ✅ |
| 34 | ShiftPEOCategoryCode | CATEGORY_CODE | — | ✅ |
| 35 | ShiftPEOCreatedBy | CREATED_BY | — | ✅ |
| 36 | ShiftPEOCreationDate | CREATION_DATE | — | ✅ |
| 37 | ShiftPEODurationMsNum | DURATION_MS_NUM | — | ✅ |
| 38 | ShiftPEODurationUomCode | DURATION_UOM_CODE | — | ✅ |
| 39 | ShiftPEOEndTimeMsNum | END_TIME_MS_NUM | — | ✅ |
| 40 | ShiftPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 41 | ShiftPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 42 | ShiftPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 43 | ShiftPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 44 | ShiftPEOShiftDtlTypeCode | SHIFT_DTL_TYPE_CODE | — | ✅ |
| 45 | ShiftPEOShiftTypeCode | SHIFT_TYPE_CODE | — | ✅ |
| 46 | ShiftPEOShortTxt | SHORT_TXT | — | ✅ |
| 47 | ShiftPEOStartTimeMsNum | START_TIME_MS_NUM | — | ✅ |

### [[zmm_sr_shifts_tl|ZMM_SR_SHIFTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ShiftTranslationPEOLanguage | LANGUAGE | — | — |
| 2 | ShiftTranslationPEOShiftDesc | SHIFT_DESC | — | ✅ |
| 3 | ShiftTranslationPEOShiftName | SHIFT_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
