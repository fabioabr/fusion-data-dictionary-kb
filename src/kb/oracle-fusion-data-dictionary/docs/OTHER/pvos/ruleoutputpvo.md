---
id: DOC-OTHER-PVO-RuleOutputPVO
doc_type: system-doc
title: "RuleOutputPVO — PVO Cross-Module"
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
  - RuleOutputPVO
  - ruleoutputpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RuleOutputPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Rule Output. Acessa as tabelas: FF_FORMULAS_VL, FND_VS_VALUE_SETS, HWM_ALLOCATIONS_HDR_VL (+2).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.RulesCoreAM.RuleOutputPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 69 | 5 | 1 | 52 | 75% |

---

## 🔗 Tabelas Relacionadas

- [[ff_formulas_vl|FF_FORMULAS_VL]] — 5 atributos (2 BICC)
- [[fnd_vs_value_sets|FND_VS_VALUE_SETS]] — 3 atributos (1 BICC)
- [[hwm_allocations_hdr_vl|HWM_ALLOCATIONS_HDR_VL]] — 4 atributos (2 BICC)
- [[hwm_rules|HWM_RULES]] — 29 atributos (24 BICC)
- [[hwm_rule_outputs|HWM_RULE_OUTPUTS]] — 28 atributos (1 PKs, 23 BICC)

---

## ⚙️ Atributos

### [[ff_formulas_vl|FF_FORMULAS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FormulaDPEOBaseFormulaName | BASE_FORMULA_NAME | — | — |
| 2 | FormulaDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | FormulaDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | FormulaDPEOFormulaId | FORMULA_ID | — | — |
| 5 | FormulaDPEOFormulaName | FORMULA_NAME | — | ✅ |

### [[fnd_vs_value_sets|FND_VS_VALUE_SETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ValueSetsBPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 2 | ValueSetsBPEOValueSetCode | VALUE_SET_CODE | — | ✅ |
| 3 | ValueSetsBPEOValueSetId | VALUE_SET_ID | — | — |

### [[hwm_allocations_hdr_vl|HWM_ALLOCATIONS_HDR_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllocationsHdrVLPEOAllocationId | ALLOCATION_ID | — | — |
| 2 | AllocationsHdrVLPEOAllocationName | ALLOCATION_NAME | — | ✅ |
| 3 | AllocationsHdrVLPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | AllocationsHdrVLPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |

### [[hwm_rules|HWM_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RulePEOClassification | CLASSIFICATION | — | ✅ |
| 2 | RulePEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | RulePEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | RulePEODescription | DESCRIPTION | — | ✅ |
| 5 | RulePEODfltAllocationId | DFLT_ALLOCATION_ID | — | ✅ |
| 6 | RulePEOEnterpriseId | ENTERPRISE_ID | — | — |
| 7 | RulePEOFastFormulaExecType | FAST_FORMULA_EXEC_TYPE | — | — |
| 8 | RulePEOIncludeEmptyTc | INCLUDE_EMPTY_TC | — | ✅ |
| 9 | RulePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | RulePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | RulePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | RulePEOModuleId | MODULE_ID | — | — |
| 13 | RulePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | RulePEOProcessType | PROCESS_TYPE | — | ✅ |
| 15 | RulePEOPrsFormulaId | PRS_FORMULA_ID | — | ✅ |
| 16 | RulePEOPrsScriptId | PRS_SCRIPT_ID | — | — |
| 17 | RulePEORuleExecType | RULE_EXEC_TYPE | — | ✅ |
| 18 | RulePEORuleId | RULE_ID | — | ✅ |
| 19 | RulePEORuleName | RULE_NAME | — | ✅ |
| 20 | RulePEORuleSubType | RULE_SUB_TYPE | — | ✅ |
| 21 | RulePEORuleTmpltsId | RULE_TMPLTS_ID | — | ✅ |
| 22 | RulePEORuleType | RULE_TYPE | — | ✅ |
| 23 | RulePEORunEventDelete | RUN_EVENT_DELETE | — | ✅ |
| 24 | RulePEORunEventResub | RUN_EVENT_RESUB | — | ✅ |
| 25 | RulePEORunEventSave | RUN_EVENT_SAVE | — | ✅ |
| 26 | RulePEORunEventSub | RUN_EVENT_SUB | — | ✅ |
| 27 | RulePEORunSummationLevel | RUN_SUMMATION_LEVEL | — | ✅ |
| 28 | RulePEORunTbbLevel | RUN_TBB_LEVEL | — | ✅ |
| 29 | RulePEOSuppressDupMsgs | SUPPRESS_DUP_MSGS | — | ✅ |

### [[hwm_rule_outputs|HWM_RULE_OUTPUTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RuleOutputPEOAtrbFldName | ATRB_FLD_NAME | — | ✅ |
| 2 | RuleOutputPEOAtrbFldSetId | ATRB_FLD_SET_ID | — | — |
| 3 | RuleOutputPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | RuleOutputPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | RuleOutputPEODisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 6 | RuleOutputPEODisplayType | DISPLAY_TYPE | — | ✅ |
| 7 | RuleOutputPEODisplayValue | DISPLAY_VALUE | — | ✅ |
| 8 | RuleOutputPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 9 | RuleOutputPEOHideFlag | HIDE_FLAG | — | ✅ |
| 10 | RuleOutputPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | RuleOutputPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | RuleOutputPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | RuleOutputPEOMsgSeverity | MSG_SEVERITY | — | ✅ |
| 14 | RuleOutputPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | RuleOutputPEOOutputName | OUTPUT_NAME | — | ✅ |
| 16 | RuleOutputPEOOutputSource | OUTPUT_SOURCE | — | ✅ |
| 17 | RuleOutputPEOOutputValueType | OUTPUT_VALUE_TYPE | — | ✅ |
| 18 | RuleOutputPEORecursive | RECURSIVE | — | — |
| 19 | RuleOutputPEORelatedInputName | RELATED_INPUT_NAME | — | — |
| 20 | RuleOutputPEORuleId | RULE_ID | — | ✅ |
| 21 | RuleOutputPEORuleOutputId | RULE_OUTPUT_ID | 🔑 | ✅ |
| 22 | RuleOutputPEORuleTmpltUsagesId | RULE_TMPLT_USAGES_ID | — | ✅ |
| 23 | RuleOutputPEOTbbGroupNumber | TBB_GROUP_NUMBER | — | ✅ |
| 24 | RuleOutputPEOTmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 25 | RuleOutputPEOValueDate | VALUE_DATE | — | ✅ |
| 26 | RuleOutputPEOValueNumber | VALUE_NUMBER | — | ✅ |
| 27 | RuleOutputPEOValueSetId | VALUE_SET_ID | — | ✅ |
| 28 | RuleOutputPEOValueText | VALUE_TEXT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
