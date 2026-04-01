---
id: DOC-OTHER-PVO-AccrualPlanBandPVO
doc_type: system-doc
title: "AccrualPlanBandPVO — PVO Cross-Module"
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
  - AccrualPlanBandPVO
  - accrualplanbandpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AccrualPlanBandPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Accrual Plan Band. Acessa as tabelas: PER_ACCRUAL_BANDS, PER_ACCRUAL_PLANS_B.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AccrualAM.AccrualPlanBandPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 54 | 2 | 1 | 3 | 6% |

---

## 🔗 Tabelas Relacionadas

- [[per_accrual_bands|PER_ACCRUAL_BANDS]] — 14 atributos (1 BICC)
- [[per_accrual_plans_b|PER_ACCRUAL_PLANS_B]] — 40 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[per_accrual_bands|PER_ACCRUAL_BANDS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccrualBandId | ACCRUAL_BAND_ID | — | — |
| 2 | AccrualBandPEOAccrualPlanId | ACCRUAL_PLAN_ID | — | — |
| 3 | AccrualBandPEOBandGroupCode | BAND_GROUP_CODE | — | — |
| 4 | AccrualBandPEOBandRangeEnd | BAND_RANGE_END | — | — |
| 5 | AccrualBandPEOBandRangeStart | BAND_RANGE_START | — | — |
| 6 | AccrualBandPEOCreatedBy | CREATED_BY | — | — |
| 7 | AccrualBandPEOCreationDate | CREATION_DATE | — | — |
| 8 | AccrualBandPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | AccrualBandPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | AccrualBandPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | AccrualBandPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | AccrualBandPEOTermAccrualRate | TERM_ACCRUAL_RATE | — | — |
| 13 | AccrualBandPEOTermCeilingValue | TERM_CEILING_VALUE | — | — |
| 14 | AccrualBandPEOTermMaxCarryOver | TERM_MAX_CARRY_OVER | — | — |

### [[per_accrual_plans_b|PER_ACCRUAL_PLANS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccrualPlanId | ACCRUAL_PLAN_ID | 🔑 | ✅ |
| 2 | AccrualPlanPEOAccrualBandGroup | ACCRUAL_BAND_GROUP | — | — |
| 3 | AccrualPlanPEOAccrualBandRange | ACCRUAL_BAND_RANGE | — | — |
| 4 | AccrualPlanPEOAccrualCategory | ACCRUAL_CATEGORY | — | — |
| 5 | AccrualPlanPEOAccrualDefinedBalanceId | ACCRUAL_DEFINED_BALANCE_ID | — | — |
| 6 | AccrualPlanPEOAccrualElementTypeId | ACCRUAL_ELEMENT_TYPE_ID | — | — |
| 7 | AccrualPlanPEOAccrualFormulaId | ACCRUAL_FORMULA_ID | — | — |
| 8 | AccrualPlanPEOAccrualFrequencyLength | ACCRUAL_FREQUENCY_LENGTH | — | — |
| 9 | AccrualPlanPEOAccrualFrequencyLengthUom | ACCRUAL_FREQUENCY_LENGTH_UOM | — | — |
| 10 | AccrualPlanPEOAccrualFrequencyType | ACCRUAL_FREQUENCY_TYPE | — | — |
| 11 | AccrualPlanPEOAccrualStartRule | ACCRUAL_START_RULE | — | — |
| 12 | AccrualPlanPEOAccrualTermEnd | ACCRUAL_TERM_END | — | — |
| 13 | AccrualPlanPEOAccrualTermLength | ACCRUAL_TERM_LENGTH | — | — |
| 14 | AccrualPlanPEOAccrualTermLengthUom | ACCRUAL_TERM_LENGTH_UOM | — | — |
| 15 | AccrualPlanPEOAccrualTermStart | ACCRUAL_TERM_START | — | — |
| 16 | AccrualPlanPEOAccrualTermType | ACCRUAL_TERM_TYPE | — | — |
| 17 | AccrualPlanPEOAccrualUnits | ACCRUAL_UNITS | — | — |
| 18 | AccrualPlanPEOCoDateInputValueId | CO_DATE_INPUT_VALUE_ID | — | — |
| 19 | AccrualPlanPEOCoExpDateInputValueId | CO_EXP_DATE_INPUT_VALUE_ID | — | — |
| 20 | AccrualPlanPEOCoExpiryLength | CO_EXPIRY_LENGTH | — | — |
| 21 | AccrualPlanPEOCoExpiryLengthUom | CO_EXPIRY_LENGTH_UOM | — | — |
| 22 | AccrualPlanPEOCoFormulaId | CO_FORMULA_ID | — | — |
| 23 | AccrualPlanPEOCoInputValueId | CO_INPUT_VALUE_ID | — | — |
| 24 | AccrualPlanPEOCreatedBy | CREATED_BY | — | — |
| 25 | AccrualPlanPEOCreationDate | CREATION_DATE | — | — |
| 26 | AccrualPlanPEOIneligibilityFormulaId | INELIGIBILITY_FORMULA_ID | — | — |
| 27 | AccrualPlanPEOIneligiblePeriodLength | INELIGIBLE_PERIOD_LENGTH | — | — |
| 28 | AccrualPlanPEOIneligiblePeriodLengthUom | INELIGIBLE_PERIOD_LENGTH_UOM | — | — |
| 29 | AccrualPlanPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | AccrualPlanPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 31 | AccrualPlanPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 32 | AccrualPlanPEOLegislationCode | LEGISLATION_CODE | — | — |
| 33 | AccrualPlanPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 34 | AccrualPlanPEOLiabilityBalanceElementId | LIABILITY_BALANCE_ELEMENT_ID | — | — |
| 35 | AccrualPlanPEOLiabilityDefinedBalanceId | LIABILITY_DEFINED_BALANCE_ID | — | — |
| 36 | AccrualPlanPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 37 | AccrualPlanPEOPayrollFormulaId | PAYROLL_FORMULA_ID | — | — |
| 38 | AccrualPlanPEOResidualDateInputValueId | RESIDUAL_DATE_INPUT_VALUE_ID | — | — |
| 39 | AccrualPlanPEOResidualInputValueId | RESIDUAL_INPUT_VALUE_ID | — | — |
| 40 | AccrualPlanPEOTaggingElementTypeId | TAGGING_ELEMENT_TYPE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
