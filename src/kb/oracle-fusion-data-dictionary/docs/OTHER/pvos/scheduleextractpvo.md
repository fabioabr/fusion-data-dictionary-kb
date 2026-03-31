---
id: DOC-OTHER-PVO-ScheduleExtractPVO
doc_type: system-doc
title: "ScheduleExtractPVO — PVO Cross-Module"
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
  - ScheduleExtractPVO
  - scheduleextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ScheduleExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Schedule Extract. Acessa as tabelas: ZMM_SR_SCHEDULES_B, ZMM_SR_SCHEDULES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.ScheduleExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 49 | 2 | 1 | 48 | 98% |

---

## 🔗 Tabelas Relacionadas

- [[zmm_sr_schedules_b|ZMM_SR_SCHEDULES_B]] — 46 atributos (1 PKs, 46 BICC)
- [[zmm_sr_schedules_tl|ZMM_SR_SCHEDULES_TL]] — 3 atributos (2 BICC)

---

## ⚙️ Atributos

### [[zmm_sr_schedules_b|ZMM_SR_SCHEDULES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ScheduleId | SCHEDULE_ID | 🔑 | ✅ |
| 2 | SchedulePEOAssignmentNum | ASSIGNMENT_NUM | — | ✅ |
| 3 | SchedulePEOAttribute1 | ATTRIBUTE1 | — | ✅ |
| 4 | SchedulePEOAttribute10 | ATTRIBUTE10 | — | ✅ |
| 5 | SchedulePEOAttribute11 | ATTRIBUTE11 | — | ✅ |
| 6 | SchedulePEOAttribute12 | ATTRIBUTE12 | — | ✅ |
| 7 | SchedulePEOAttribute13 | ATTRIBUTE13 | — | ✅ |
| 8 | SchedulePEOAttribute14 | ATTRIBUTE14 | — | ✅ |
| 9 | SchedulePEOAttribute15 | ATTRIBUTE15 | — | ✅ |
| 10 | SchedulePEOAttribute16 | ATTRIBUTE16 | — | ✅ |
| 11 | SchedulePEOAttribute17 | ATTRIBUTE17 | — | ✅ |
| 12 | SchedulePEOAttribute18 | ATTRIBUTE18 | — | ✅ |
| 13 | SchedulePEOAttribute19 | ATTRIBUTE19 | — | ✅ |
| 14 | SchedulePEOAttribute2 | ATTRIBUTE2 | — | ✅ |
| 15 | SchedulePEOAttribute20 | ATTRIBUTE20 | — | ✅ |
| 16 | SchedulePEOAttribute21 | ATTRIBUTE21 | — | ✅ |
| 17 | SchedulePEOAttribute22 | ATTRIBUTE22 | — | ✅ |
| 18 | SchedulePEOAttribute23 | ATTRIBUTE23 | — | ✅ |
| 19 | SchedulePEOAttribute24 | ATTRIBUTE24 | — | ✅ |
| 20 | SchedulePEOAttribute25 | ATTRIBUTE25 | — | ✅ |
| 21 | SchedulePEOAttribute26 | ATTRIBUTE26 | — | ✅ |
| 22 | SchedulePEOAttribute27 | ATTRIBUTE27 | — | ✅ |
| 23 | SchedulePEOAttribute28 | ATTRIBUTE28 | — | ✅ |
| 24 | SchedulePEOAttribute29 | ATTRIBUTE29 | — | ✅ |
| 25 | SchedulePEOAttribute3 | ATTRIBUTE3 | — | ✅ |
| 26 | SchedulePEOAttribute30 | ATTRIBUTE30 | — | ✅ |
| 27 | SchedulePEOAttribute4 | ATTRIBUTE4 | — | ✅ |
| 28 | SchedulePEOAttribute5 | ATTRIBUTE5 | — | ✅ |
| 29 | SchedulePEOAttribute6 | ATTRIBUTE6 | — | ✅ |
| 30 | SchedulePEOAttribute7 | ATTRIBUTE7 | — | ✅ |
| 31 | SchedulePEOAttribute8 | ATTRIBUTE8 | — | ✅ |
| 32 | SchedulePEOAttribute9 | ATTRIBUTE9 | — | ✅ |
| 33 | SchedulePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 34 | SchedulePEOCategoryCode | CATEGORY_CODE | — | ✅ |
| 35 | SchedulePEOCreatedBy | CREATED_BY | — | ✅ |
| 36 | SchedulePEOCreationDate | CREATION_DATE | — | ✅ |
| 37 | SchedulePEODeletedFlag | DELETED_FLAG | — | ✅ |
| 38 | SchedulePEOEffectiveFromDate | EFFECTIVE_FROM_DATE | — | ✅ |
| 39 | SchedulePEOEffectiveToDate | EFFECTIVE_TO_DATE | — | ✅ |
| 40 | SchedulePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 41 | SchedulePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 42 | SchedulePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 43 | SchedulePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 44 | SchedulePEOQtrlyTypeCode | QTRLY_TYPE_CODE | — | ✅ |
| 45 | SchedulePEOScheduleTypeCode | SCHEDULE_TYPE_CODE | — | ✅ |
| 46 | SchedulePEOWeekStartCode | WEEK_START_CODE | — | ✅ |

### [[zmm_sr_schedules_tl|ZMM_SR_SCHEDULES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ScheduleTranslationPEOLanguage | LANGUAGE | — | — |
| 2 | ScheduleTranslationPEOScheduleDesc | SCHEDULE_DESC | — | ✅ |
| 3 | ScheduleTranslationPEOScheduleName | SCHEDULE_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
