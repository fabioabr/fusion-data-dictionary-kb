---
id: DOC-OTHER-PVO-RateScheduleExtractPVO
doc_type: system-doc
title: "RateScheduleExtractPVO — PVO Cross-Module"
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
  - RateScheduleExtractPVO
  - ratescheduleextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RateScheduleExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Rate Schedule Extract. Acessa as tabelas: PJF_RATE_SCHEDULES_B, PJF_RATE_SCHEDULES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.RateScheduleExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 38 | 2 | 1 | 22 | 58% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_rate_schedules_b|PJF_RATE_SCHEDULES_B]] — 27 atributos (1 PKs, 11 BICC)
- [[pjf_rate_schedules_tl|PJF_RATE_SCHEDULES_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[pjf_rate_schedules_b|PJF_RATE_SCHEDULES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RateScheduleBasePEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | RateScheduleBasePEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | RateScheduleBasePEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | RateScheduleBasePEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | RateScheduleBasePEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | RateScheduleBasePEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | RateScheduleBasePEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | RateScheduleBasePEOAttribute2 | ATTRIBUTE2 | — | — |
| 9 | RateScheduleBasePEOAttribute3 | ATTRIBUTE3 | — | — |
| 10 | RateScheduleBasePEOAttribute4 | ATTRIBUTE4 | — | — |
| 11 | RateScheduleBasePEOAttribute5 | ATTRIBUTE5 | — | — |
| 12 | RateScheduleBasePEOAttribute6 | ATTRIBUTE6 | — | — |
| 13 | RateScheduleBasePEOAttribute7 | ATTRIBUTE7 | — | — |
| 14 | RateScheduleBasePEOAttribute8 | ATTRIBUTE8 | — | — |
| 15 | RateScheduleBasePEOAttribute9 | ATTRIBUTE9 | — | — |
| 16 | RateScheduleBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | RateScheduleBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 18 | RateScheduleBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 19 | RateScheduleBasePEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 20 | RateScheduleBasePEOJobSetId | JOB_SET_ID | — | ✅ |
| 21 | RateScheduleBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | RateScheduleBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 23 | RateScheduleBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | RateScheduleBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 25 | RateScheduleBasePEORateScheduleId | RATE_SCHEDULE_ID | 🔑 | ✅ |
| 26 | RateScheduleBasePEOScheduleType | SCHEDULE_TYPE | — | ✅ |
| 27 | RateScheduleBasePEOSetId | SET_ID | — | ✅ |

### [[pjf_rate_schedules_tl|PJF_RATE_SCHEDULES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RateScheduleTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | RateScheduleTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | RateScheduleTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | RateScheduleTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 5 | RateScheduleTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | RateScheduleTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | RateScheduleTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | RateScheduleTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | RateScheduleTranslationPEORateScheduleId | RATE_SCHEDULE_ID | — | ✅ |
| 10 | RateScheduleTranslationPEORateScheduleName | RATE_SCHEDULE_NAME | — | ✅ |
| 11 | RateScheduleTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
