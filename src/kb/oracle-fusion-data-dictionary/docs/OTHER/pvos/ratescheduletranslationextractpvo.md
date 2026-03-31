---
id: DOC-OTHER-PVO-RateScheduleTranslationExtractPVO
doc_type: system-doc
title: "RateScheduleTranslationExtractPVO — PVO Cross-Module"
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
  - RateScheduleTranslationExtractPVO
  - ratescheduletranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RateScheduleTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Rate Schedule Translation Extract. Acessa as tabelas: PJF_RATE_SCHEDULES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.RateScheduleTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_rate_schedules_tl|PJF_RATE_SCHEDULES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[pjf_rate_schedules_tl|PJF_RATE_SCHEDULES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RateScheduleTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | RateScheduleTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | RateScheduleTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | RateScheduleTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | RateScheduleTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | RateScheduleTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | RateScheduleTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | RateScheduleTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | RateScheduleTranslationPEORateScheduleId | RATE_SCHEDULE_ID | 🔑 | ✅ |
| 10 | RateScheduleTranslationPEORateScheduleName | RATE_SCHEDULE_NAME | — | ✅ |
| 11 | RateScheduleTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
