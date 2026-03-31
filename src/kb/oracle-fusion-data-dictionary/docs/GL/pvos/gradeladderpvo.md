---
id: DOC-GL-PVO-GradeLadderPVO
doc_type: system-doc
title: "GradeLadderPVO — PVO General Ledger"
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
  - GradeLadderPVO
  - gradeladderpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GradeLadderPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Grade Ladder. Acessa as tabelas: FF_FORMULAS_VL, FND_SETID_SETS_VL, PER_ACTIONS_B (+6).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GradeAM.GradeLadderPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 175 | 9 | 3 | 46 | 26% |

---

## 🔗 Tabelas Relacionadas

- [[ff_formulas_vl|FF_FORMULAS_VL]] — 20 atributos (12 BICC)
- [[fnd_setid_sets_vl|FND_SETID_SETS_VL]] — 5 atributos (2 BICC)
- [[per_actions_b|PER_ACTIONS_B]] — 2 atributos (1 BICC)
- [[per_actions_tl|PER_ACTIONS_TL]] — 4 atributos (2 BICC)
- [[per_action_reasons_b|PER_ACTION_REASONS_B]] — 2 atributos (1 BICC)
- [[per_action_reasons_tl|PER_ACTION_REASONS_TL]] — 4 atributos (2 BICC)
- [[per_grade_ladders_f|PER_GRADE_LADDERS_F]] — 109 atributos (3 PKs, 20 BICC)
- [[per_grade_ladders_f_tl|PER_GRADE_LADDERS_F_TL]] — 13 atributos (3 BICC)
- [[per_rates_f|PER_RATES_F]] — 16 atributos (3 BICC)

---

## ⚙️ Atributos

### [[ff_formulas_vl|FF_FORMULAS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProgressionFormulaDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | ProgressionFormulaDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | ProgressionFormulaDPEOFormulaId | FORMULA_ID | — | — |
| 4 | ProgressionFormulaDPEOFormulaName | FORMULA_NAME | — | ✅ |
| 5 | ProgressionFormulaDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | RateFormulaDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | RateFormulaDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 8 | RateFormulaDPEOFormulaId | FORMULA_ID | — | — |
| 9 | RateFormulaDPEOFormulaName | FORMULA_NAME | — | ✅ |
| 10 | RateFormulaDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | SalaryCalcFormulaDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 12 | SalaryCalcFormulaDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 13 | SalaryCalcFormulaDPEOFormulaId | FORMULA_ID | — | — |
| 14 | SalaryCalcFormulaDPEOFormulaName | FORMULA_NAME | — | ✅ |
| 15 | SalaryCalcFormulaDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | SalaryFormulaDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 17 | SalaryFormulaDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 18 | SalaryFormulaDPEOFormulaId | FORMULA_ID | — | — |
| 19 | SalaryFormulaDPEOFormulaName | FORMULA_NAME | — | ✅ |
| 20 | SalaryFormulaDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[fnd_setid_sets_vl|FND_SETID_SETS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SetIdSetPEODescription | DESCRIPTION | — | — |
| 2 | SetIdSetPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | SetIdSetPEOSetCode | SET_CODE | — | — |
| 4 | SetIdSetPEOSetId | SET_ID | — | — |
| 5 | SetIdSetPEOSetName | SET_NAME | — | ✅ |

### [[per_actions_b|PER_ACTIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProgressionActionsPEOActionId | ACTION_ID | — | — |
| 2 | ProgressionActionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[per_actions_tl|PER_ACTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProgressionActionTranslationPEOActionId | ACTION_ID | — | — |
| 2 | ProgressionActionTranslationPEOActionName | ACTION_NAME | — | ✅ |
| 3 | ProgressionActionTranslationPEOLanguage | LANGUAGE | — | — |
| 4 | ProgressionActionTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[per_action_reasons_b|PER_ACTION_REASONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProgressionActionReasonsPEOActionReasonId | ACTION_REASON_ID | — | — |
| 2 | ProgressionActionReasonsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[per_action_reasons_tl|PER_ACTION_REASONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProgressionActionReasonsTranslationPEOActionReason | ACTION_REASON | — | ✅ |
| 2 | ProgressionActionReasonsTranslationPEOActionReasonId | ACTION_REASON_ID | — | — |
| 3 | ProgressionActionReasonsTranslationPEOLanguage | LANGUAGE | — | — |
| 4 | ProgressionActionReasonsTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[per_grade_ladders_f|PER_GRADE_LADDERS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | ActiveStatus | ACTIVE_STATUS | — | ✅ |
| 3 | AllowProgOverrideFlag | ALLOW_PROG_OVERRIDE_FLAG | — | — |
| 4 | AllowSalaryOverrideFlag | ALLOW_SALARY_OVERRIDE_FLAG | — | — |
| 5 | Attribute1 | ATTRIBUTE1 | — | — |
| 6 | Attribute10 | ATTRIBUTE10 | — | — |
| 7 | Attribute11 | ATTRIBUTE11 | — | — |
| 8 | Attribute12 | ATTRIBUTE12 | — | — |
| 9 | Attribute13 | ATTRIBUTE13 | — | — |
| 10 | Attribute14 | ATTRIBUTE14 | — | — |
| 11 | Attribute15 | ATTRIBUTE15 | — | — |
| 12 | Attribute16 | ATTRIBUTE16 | — | — |
| 13 | Attribute17 | ATTRIBUTE17 | — | — |
| 14 | Attribute18 | ATTRIBUTE18 | — | — |
| 15 | Attribute19 | ATTRIBUTE19 | — | — |
| 16 | Attribute2 | ATTRIBUTE2 | — | — |
| 17 | Attribute20 | ATTRIBUTE20 | — | — |
| 18 | Attribute21 | ATTRIBUTE21 | — | — |
| 19 | Attribute22 | ATTRIBUTE22 | — | — |
| 20 | Attribute23 | ATTRIBUTE23 | — | — |
| 21 | Attribute24 | ATTRIBUTE24 | — | — |
| 22 | Attribute25 | ATTRIBUTE25 | — | — |
| 23 | Attribute26 | ATTRIBUTE26 | — | — |
| 24 | Attribute27 | ATTRIBUTE27 | — | — |
| 25 | Attribute28 | ATTRIBUTE28 | — | — |
| 26 | Attribute29 | ATTRIBUTE29 | — | — |
| 27 | Attribute3 | ATTRIBUTE3 | — | — |
| 28 | Attribute30 | ATTRIBUTE30 | — | — |
| 29 | Attribute4 | ATTRIBUTE4 | — | — |
| 30 | Attribute5 | ATTRIBUTE5 | — | — |
| 31 | Attribute6 | ATTRIBUTE6 | — | — |
| 32 | Attribute7 | ATTRIBUTE7 | — | — |
| 33 | Attribute8 | ATTRIBUTE8 | — | — |
| 34 | Attribute9 | ATTRIBUTE9 | — | — |
| 35 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 36 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 37 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 38 | AttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 39 | AttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 40 | AttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 41 | AttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 42 | AttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 43 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 44 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 45 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 46 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 47 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 48 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 49 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 50 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 51 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 52 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 53 | AttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 54 | AttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 55 | AttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 56 | AttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 57 | AttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 58 | AttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 59 | AttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 60 | AttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 61 | AttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 62 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 63 | AttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 64 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 65 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 66 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 67 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 68 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 69 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 70 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 71 | AutoProgressionCode | AUTO_PROGRESSION_CODE | — | ✅ |
| 72 | AutoSalChangeCode | AUTO_SAL_CHANGE_CODE | — | ✅ |
| 73 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 74 | CreatedBy | CREATED_BY | — | ✅ |
| 75 | CreationDate | CREATION_DATE | — | ✅ |
| 76 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 77 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 78 | GradeLadderGrpCode | GRADE_LADDER_GRP_CODE | — | ✅ |
| 79 | GradeLadderId | GRADE_LADDER_ID | 🔑 | ✅ |
| 80 | GradeSetId | GRADE_SET_ID | — | — |
| 81 | GradeType | GRADE_TYPE | — | ✅ |
| 82 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 83 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 84 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 85 | LegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 86 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 87 | ProgActionId | PROG_ACTION_ID | — | — |
| 88 | ProgActionOccurrenceId | PROG_ACTION_OCCURRENCE_ID | — | — |
| 89 | ProgActionReasonId | PROG_ACTION_REASON_ID | — | — |
| 90 | ProgressionDateCode | PROGRESSION_DATE_CODE | — | ✅ |
| 91 | ProgressionDateRuleId | PROGRESSION_DATE_RULE_ID | — | — |
| 92 | ProgressionStyleCode | PROGRESSION_STYLE_CODE | — | ✅ |
| 93 | RateChangeDateCode | RATE_CHANGE_DATE_CODE | — | ✅ |
| 94 | RateChangeDateRuleId | RATE_CHANGE_DATE_RULE_ID | — | — |
| 95 | RateSyncActionId | RATE_SYNC_ACTION_ID | — | — |
| 96 | RateSyncActionReasonId | RATE_SYNC_ACTION_REASON_ID | — | — |
| 97 | SalaryActionId | SALARY_ACTION_ID | — | — |
| 98 | SalaryActionOccurrenceId | SALARY_ACTION_OCCURRENCE_ID | — | — |
| 99 | SalaryActionReasonId | SALARY_ACTION_REASON_ID | — | — |
| 100 | SalaryAdjustmentTypeCode | SALARY_ADJUSTMENT_TYPE_CODE | — | ✅ |
| 101 | SalaryCalcMethodCode | SALARY_CALC_METHOD_CODE | — | ✅ |
| 102 | SalaryCalcRuleId | SALARY_CALC_RULE_ID | — | — |
| 103 | SalaryChangeDateCode | SALARY_CHANGE_DATE_CODE | — | ✅ |
| 104 | SalaryChangeDateRuleId | SALARY_CHANGE_DATE_RULE_ID | — | — |
| 105 | SalaryElementTypeId | SALARY_ELEMENT_TYPE_ID | — | — |
| 106 | SalaryInputValueId | SALARY_INPUT_VALUE_ID | — | — |
| 107 | SalaryUpdMethodCode | SALARY_UPD_METHOD_CODE | — | — |
| 108 | StepDeterminationCode | STEP_DETERMINATION_CODE | — | — |
| 109 | UpdateSalaryFlag | UPDATE_SALARY_FLAG | — | ✅ |

### [[per_grade_ladders_f_tl|PER_GRADE_LADDERS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GradeLadderTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | GradeLadderTranslationPEOCreatedBy | CREATED_BY | — | — |
| 3 | GradeLadderTranslationPEOCreationDate | CREATION_DATE | — | — |
| 4 | GradeLadderTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 5 | GradeLadderTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 6 | GradeLadderTranslationPEOGradeLadderId | GRADE_LADDER_ID | — | — |
| 7 | GradeLadderTranslationPEOLanguage | LANGUAGE | — | — |
| 8 | GradeLadderTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | GradeLadderTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | GradeLadderTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | GradeLadderTranslationPEOName | NAME | — | ✅ |
| 12 | GradeLadderTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | GradeLadderTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[per_rates_f|PER_RATES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SalaryUpdateRatePEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | SalaryUpdateRatePEOActiveStatus | ACTIVE_STATUS | — | — |
| 3 | SalaryUpdateRatePEOAnnualizationFactor | ANNUALIZATION_FACTOR | — | ✅ |
| 4 | SalaryUpdateRatePEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 5 | SalaryUpdateRatePEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 6 | SalaryUpdateRatePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | SalaryUpdateRatePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 8 | SalaryUpdateRatePEOGradeLadderId | GRADE_LADDER_ID | — | — |
| 9 | SalaryUpdateRatePEOLegislationCode | LEGISLATION_CODE | — | — |
| 10 | SalaryUpdateRatePEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 11 | SalaryUpdateRatePEOProgressionRateFlag | PROGRESSION_RATE_FLAG | — | — |
| 12 | SalaryUpdateRatePEORateFrequency | RATE_FREQUENCY | — | ✅ |
| 13 | SalaryUpdateRatePEORateId | RATE_ID | — | — |
| 14 | SalaryUpdateRatePEORateObjectType | RATE_OBJECT_TYPE | — | — |
| 15 | SalaryUpdateRatePEORateType | RATE_TYPE | — | — |
| 16 | SalaryUpdateRatePEORateUom | RATE_UOM | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
