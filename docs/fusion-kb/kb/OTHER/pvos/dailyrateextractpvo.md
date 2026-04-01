---
id: DOC-OTHER-PVO-DailyRateExtractPVO
doc_type: system-doc
title: "DailyRateExtractPVO — PVO Cross-Module"
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
  - DailyRateExtractPVO
  - dailyrateextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DailyRateExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Daily Rate Extract. Acessa as tabelas: GL_DAILY_RATES.

**Caminho:** `FscmTopModelAM.FinExtractAM.GlBiccExtractAM.DailyRateExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 38 | 1 | 4 | 12 | 32% |

---

## 🔗 Tabelas Relacionadas

- [[gl_daily_rates|GL_DAILY_RATES]] — 38 atributos (4 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[gl_daily_rates|GL_DAILY_RATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DailyRateAttribute1 | ATTRIBUTE1 | — | — |
| 2 | DailyRateAttribute10 | ATTRIBUTE10 | — | — |
| 3 | DailyRateAttribute11 | ATTRIBUTE11 | — | — |
| 4 | DailyRateAttribute12 | ATTRIBUTE12 | — | — |
| 5 | DailyRateAttribute13 | ATTRIBUTE13 | — | — |
| 6 | DailyRateAttribute14 | ATTRIBUTE14 | — | — |
| 7 | DailyRateAttribute15 | ATTRIBUTE15 | — | — |
| 8 | DailyRateAttribute2 | ATTRIBUTE2 | — | — |
| 9 | DailyRateAttribute3 | ATTRIBUTE3 | — | — |
| 10 | DailyRateAttribute4 | ATTRIBUTE4 | — | — |
| 11 | DailyRateAttribute5 | ATTRIBUTE5 | — | — |
| 12 | DailyRateAttribute6 | ATTRIBUTE6 | — | — |
| 13 | DailyRateAttribute7 | ATTRIBUTE7 | — | — |
| 14 | DailyRateAttribute8 | ATTRIBUTE8 | — | — |
| 15 | DailyRateAttribute9 | ATTRIBUTE9 | — | — |
| 16 | DailyRateAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | DailyRateAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 18 | DailyRateAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 19 | DailyRateAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 20 | DailyRateAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 21 | DailyRateAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 22 | DailyRateAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 23 | DailyRateAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 24 | DailyRateAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 25 | DailyRateAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 26 | DailyRateAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 27 | DailyRateConversionDate | CONVERSION_DATE | 🔑 | ✅ |
| 28 | DailyRateConversionRate | CONVERSION_RATE | — | ✅ |
| 29 | DailyRateConversionType | CONVERSION_TYPE | 🔑 | ✅ |
| 30 | DailyRateCreatedBy | CREATED_BY | — | ✅ |
| 31 | DailyRateCreationDate | CREATION_DATE | — | ✅ |
| 32 | DailyRateFromCurrency | FROM_CURRENCY | 🔑 | ✅ |
| 33 | DailyRateLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 34 | DailyRateLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 35 | DailyRateLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 36 | DailyRateObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 37 | DailyRateStatusCode | STATUS_CODE | — | ✅ |
| 38 | DailyRateToCurrency | TO_CURRENCY | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
