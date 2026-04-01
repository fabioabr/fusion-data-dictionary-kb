---
id: DOC-OTHER-PVO-DailyConversionTypeExtractPVO
doc_type: system-doc
title: "DailyConversionTypeExtractPVO — PVO Cross-Module"
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
  - DailyConversionTypeExtractPVO
  - dailyconversiontypeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DailyConversionTypeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Daily Conversion Type Extract. Acessa as tabelas: GL_DAILY_CONVERSION_TYPES.

**Caminho:** `FscmTopModelAM.FinExtractAM.GlBiccExtractAM.DailyConversionTypeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 1 | 1 | 13 | 45% |

---

## 🔗 Tabelas Relacionadas

- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 29 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DailyConversionTypeAttribute1 | ATTRIBUTE1 | — | — |
| 2 | DailyConversionTypeAttribute10 | ATTRIBUTE10 | — | — |
| 3 | DailyConversionTypeAttribute11 | ATTRIBUTE11 | — | — |
| 4 | DailyConversionTypeAttribute12 | ATTRIBUTE12 | — | — |
| 5 | DailyConversionTypeAttribute13 | ATTRIBUTE13 | — | — |
| 6 | DailyConversionTypeAttribute14 | ATTRIBUTE14 | — | — |
| 7 | DailyConversionTypeAttribute15 | ATTRIBUTE15 | — | — |
| 8 | DailyConversionTypeAttribute2 | ATTRIBUTE2 | — | — |
| 9 | DailyConversionTypeAttribute3 | ATTRIBUTE3 | — | — |
| 10 | DailyConversionTypeAttribute4 | ATTRIBUTE4 | — | — |
| 11 | DailyConversionTypeAttribute5 | ATTRIBUTE5 | — | — |
| 12 | DailyConversionTypeAttribute6 | ATTRIBUTE6 | — | — |
| 13 | DailyConversionTypeAttribute7 | ATTRIBUTE7 | — | — |
| 14 | DailyConversionTypeAttribute8 | ATTRIBUTE8 | — | — |
| 15 | DailyConversionTypeAttribute9 | ATTRIBUTE9 | — | — |
| 16 | DailyConversionTypeAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | DailyConversionTypeConversionType | CONVERSION_TYPE | 🔑 | ✅ |
| 18 | DailyConversionTypeCreatedBy | CREATED_BY | — | ✅ |
| 19 | DailyConversionTypeCreationDate | CREATION_DATE | — | ✅ |
| 20 | DailyConversionTypeDescription | DESCRIPTION | — | ✅ |
| 21 | DailyConversionTypeEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | ✅ |
| 22 | DailyConversionTypeEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | ✅ |
| 23 | DailyConversionTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | DailyConversionTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 25 | DailyConversionTypeLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 26 | DailyConversionTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 27 | DailyConversionTypePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | ✅ |
| 28 | DailyConversionTypeUserConversionType | USER_CONVERSION_TYPE | — | ✅ |
| 29 | DailyConversionTypeUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
