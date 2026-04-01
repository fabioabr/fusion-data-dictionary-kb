---
id: DOC-GL-PVO-AccrualCalculationRuleInputValuePVO
doc_type: system-doc
title: "AccrualCalculationRuleInputValuePVO — PVO General Ledger"
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
  - AccrualCalculationRuleInputValuePVO
  - accrualcalculationruleinputvaluepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AccrualCalculationRuleInputValuePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Accrual Calculation Rule Input Value. Acessa as tabelas: PAY_INPUT_VALUES_F, PER_ACCRUAL_CALC_RULES.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AccrualAM.AccrualCalculationRuleInputValuePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 43 | 2 | 1 | 4 | 9% |

---

## 🔗 Tabelas Relacionadas

- [[pay_input_values_f|PAY_INPUT_VALUES_F]] — 30 atributos (2 BICC)
- [[per_accrual_calc_rules|PER_ACCRUAL_CALC_RULES]] — 13 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[pay_input_values_f|PAY_INPUT_VALUES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InputValueDPEOBaseName | BASE_NAME | — | — |
| 2 | InputValueDPEOContextId | CONTEXT_ID | — | — |
| 3 | InputValueDPEOCreatedBy | CREATED_BY | — | — |
| 4 | InputValueDPEOCreationDate | CREATION_DATE | — | — |
| 5 | InputValueDPEODefaultValue | DEFAULT_VALUE | — | — |
| 6 | InputValueDPEODisplaySequence | DISPLAY_SEQUENCE | — | — |
| 7 | InputValueDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | InputValueDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 9 | InputValueDPEOElementTypeId | ELEMENT_TYPE_ID | — | — |
| 10 | InputValueDPEOForceRrvMode | FORCE_RRV_MODE | — | — |
| 11 | InputValueDPEOFormulaId | FORMULA_ID | — | — |
| 12 | InputValueDPEOGenerateDbItemsFlag | GENERATE_DB_ITEMS_FLAG | — | — |
| 13 | InputValueDPEOHotDefaultFlag | HOT_DEFAULT_FLAG | — | — |
| 14 | InputValueDPEOInputValueId | INPUT_VALUE_ID | — | — |
| 15 | InputValueDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | InputValueDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | InputValueDPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | InputValueDPEOLookupType | LOOKUP_TYPE | — | — |
| 19 | InputValueDPEOMandatoryFlag | MANDATORY_FLAG | — | — |
| 20 | InputValueDPEOMaxValue | MAX_VALUE | — | — |
| 21 | InputValueDPEOMinValue | MIN_VALUE | — | — |
| 22 | InputValueDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | InputValueDPEOReservedInputValue | RESERVED_INPUT_VALUE | — | — |
| 24 | InputValueDPEORetroStaticFlag | RETRO_STATIC_FLAG | — | — |
| 25 | InputValueDPEOUom | UOM | — | — |
| 26 | InputValueDPEOUserDisplayFlag | USER_DISPLAY_FLAG | — | — |
| 27 | InputValueDPEOUserEnterableFlag | USER_ENTERABLE_FLAG | — | — |
| 28 | InputValueDPEOValidationOverrideMessage | VALIDATION_OVERRIDE_MESSAGE | — | — |
| 29 | InputValueDPEOVoName | VO_NAME | — | — |
| 30 | InputValueDPEOWarningOrError | WARNING_OR_ERROR | — | — |

### [[per_accrual_calc_rules|PER_ACCRUAL_CALC_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccrualCalcRuleId | ACCRUAL_CALC_RULE_ID | 🔑 | ✅ |
| 2 | AccrualCalculationRulePEOAbsenceAttendanceTypeId | ABSENCE_ATTENDANCE_TYPE_ID | — | — |
| 3 | AccrualCalculationRulePEOAccrualPlanId | ACCRUAL_PLAN_ID | — | — |
| 4 | AccrualCalculationRulePEOAddOrSubtract | ADD_OR_SUBTRACT | — | — |
| 5 | AccrualCalculationRulePEOCreatedBy | CREATED_BY | — | — |
| 6 | AccrualCalculationRulePEOCreationDate | CREATION_DATE | — | — |
| 7 | AccrualCalculationRulePEODateInputValueId | DATE_INPUT_VALUE_ID | — | — |
| 8 | AccrualCalculationRulePEOInputValueId | INPUT_VALUE_ID | — | — |
| 9 | AccrualCalculationRulePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | AccrualCalculationRulePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | AccrualCalculationRulePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | AccrualCalculationRulePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | AccrualCalculationRulePEOUseElementLink | USE_ELEMENT_LINK | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
