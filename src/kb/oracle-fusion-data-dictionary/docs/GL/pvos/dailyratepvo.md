---
id: DOC-GL-PVO-DailyRatePVO
doc_type: system-doc
title: "DailyRatePVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - DailyRatePVO
  - dailyratepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DailyRatePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Daily Rate. Acessa as tabelas: GL_DAILY_CONVERSION_TYPES, GL_DAILY_RATES.

**Caminho:** `FscmTopModelAM.FinGlCurrManageRateAM.DailyRatePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 31 | 2 | 4 | 16 | 52% |

---

## 🔗 Tabelas Relacionadas

- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 18 atributos (7 BICC)
- [[gl_daily_rates|GL_DAILY_RATES]] — 13 atributos (4 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlDailyConversionTypesConversionType | CONVERSION_TYPE | — | ✅ |
| 2 | GlDailyConversionTypesCreatedBy | CREATED_BY | — | ✅ |
| 3 | GlDailyConversionTypesCreationDate | CREATION_DATE | — | ✅ |
| 4 | GlDailyConversionTypesDescription | DESCRIPTION | — | ✅ |
| 5 | GlDailyConversionTypesEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 6 | GlDailyConversionTypesEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 7 | GlDailyConversionTypesFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 8 | GlDailyConversionTypesFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 9 | GlDailyConversionTypesFemScenario | FEM_SCENARIO | — | — |
| 10 | GlDailyConversionTypesFemTimeframe | FEM_TIMEFRAME | — | — |
| 11 | GlDailyConversionTypesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | GlDailyConversionTypesLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | GlDailyConversionTypesLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | GlDailyConversionTypesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | GlDailyConversionTypesPivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 16 | GlDailyConversionTypesSecurityFlag | SECURITY_FLAG | — | — |
| 17 | GlDailyConversionTypesUserConversionType | USER_CONVERSION_TYPE | — | — |
| 18 | GlDailyConversionTypesUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |

### [[gl_daily_rates|GL_DAILY_RATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConversionDate | CONVERSION_DATE | 🔑 | ✅ |
| 2 | ConversionType | CONVERSION_TYPE | 🔑 | ✅ |
| 3 | DailyRateConversionRate | CONVERSION_RATE | — | ✅ |
| 4 | DailyRateCreatedBy | CREATED_BY | — | ✅ |
| 5 | DailyRateCreationDate | CREATION_DATE | — | ✅ |
| 6 | DailyRateLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | DailyRateLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | DailyRateLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | DailyRateObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | DailyRateRateSourceCode | RATE_SOURCE_CODE | — | — |
| 11 | DailyRateStatusCode | STATUS_CODE | — | — |
| 12 | FromCurrency | FROM_CURRENCY | 🔑 | ✅ |
| 13 | ToCurrency | TO_CURRENCY | 🔑 | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
