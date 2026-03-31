---
id: DOC-GL-PVO-RatePVO
doc_type: system-doc
title: "RatePVO — PVO General Ledger"
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
  - RatePVO
  - ratepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RatePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Rate. Acessa as tabelas: PER_ACTION_REASONS_TL, PER_RATES_F, PER_RATES_F_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GradeAM.RatePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 37 | 3 | 2 | 26 | 70% |

---

## 🔗 Tabelas Relacionadas

- [[per_action_reasons_tl|PER_ACTION_REASONS_TL]] — 3 atributos (1 BICC)
- [[per_rates_f|PER_RATES_F]] — 22 atributos (2 PKs, 21 BICC)
- [[per_rates_f_tl|PER_RATES_F_TL]] — 12 atributos (4 BICC)

---

## ⚙️ Atributos

### [[per_action_reasons_tl|PER_ACTION_REASONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionReasonTranslationPEOActionReason | ACTION_REASON | — | ✅ |
| 2 | ActionReasonTranslationPEOActionReasonId | ACTION_REASON_ID | — | — |
| 3 | ActionReasonTranslationPEOLanguage | LANGUAGE | — | — |

### [[per_rates_f|PER_RATES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | RateId | RATE_ID | 🔑 | ✅ |
| 4 | RatePEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | ✅ |
| 5 | RatePEOActiveStatus | ACTIVE_STATUS | — | ✅ |
| 6 | RatePEOAnnualizationFactor | ANNUALIZATION_FACTOR | — | ✅ |
| 7 | RatePEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | RatePEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | RatePEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 10 | RatePEOGradeLadderId | GRADE_LADDER_ID | — | ✅ |
| 11 | RatePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | RatePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | RatePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | RatePEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 15 | RatePEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 16 | RatePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | RatePEOPayScaleId | PAY_SCALE_ID | — | ✅ |
| 18 | RatePEOProgressionRateFlag | PROGRESSION_RATE_FLAG | — | ✅ |
| 19 | RatePEORateFrequency | RATE_FREQUENCY | — | ✅ |
| 20 | RatePEORateObjectType | RATE_OBJECT_TYPE | — | ✅ |
| 21 | RatePEORateType | RATE_TYPE | — | ✅ |
| 22 | RatePEORateUom | RATE_UOM | — | ✅ |

### [[per_rates_f_tl|PER_RATES_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RateTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | RateTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | RateTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | RateTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | RateTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 6 | RateTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | RateTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | RateTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | RateTranslationPEOName | NAME | — | ✅ |
| 10 | RateTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | RateTranslationPEORateId | RATE_ID | — | — |
| 12 | RateTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
