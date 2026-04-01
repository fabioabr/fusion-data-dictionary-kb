---
id: DOC-GL-PVO-RuleInputPVO
doc_type: system-doc
title: "RuleInputPVO — PVO General Ledger"
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
  - RuleInputPVO
  - ruleinputpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RuleInputPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Rule Input. Acessa as tabelas: FF_FORMULAS_VL, FND_VS_VALUE_SETS, HWM_ALLOCATIONS_HDR_VL (+3).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.RulesCoreAM.RuleInputPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 66 | 6 | 1 | 52 | 79% |

---

## 🔗 Tabelas Relacionadas

- [[ff_formulas_vl|FF_FORMULAS_VL]] — 5 atributos (2 BICC)
- [[fnd_vs_value_sets|FND_VS_VALUE_SETS]] — 3 atributos (1 BICC)
- [[hwm_allocations_hdr_vl|HWM_ALLOCATIONS_HDR_VL]] — 4 atributos (2 BICC)
- [[hwm_rules|HWM_RULES]] — 29 atributos (24 BICC)
- [[hwm_rule_inputs|HWM_RULE_INPUTS]] — 22 atributos (1 PKs, 20 BICC)
- [[hwm_tcats_vl|HWM_TCATS_VL]] — 3 atributos (3 BICC)

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

### [[hwm_rule_inputs|HWM_RULE_INPUTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RuleInputPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | RuleInputPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | RuleInputPEODisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 4 | RuleInputPEODisplayType | DISPLAY_TYPE | — | ✅ |
| 5 | RuleInputPEODisplayValue | DISPLAY_VALUE | — | ✅ |
| 6 | RuleInputPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 7 | RuleInputPEOInputName | INPUT_NAME | — | ✅ |
| 8 | RuleInputPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | RuleInputPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | RuleInputPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | RuleInputPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | RuleInputPEOParmValueRequired | PARM_VALUE_REQUIRED | — | ✅ |
| 13 | RuleInputPEORuleId | RULE_ID | — | ✅ |
| 14 | RuleInputPEORuleInputId | RULE_INPUT_ID | 🔑 | ✅ |
| 15 | RuleInputPEORuleParameterType | RULE_PARAMETER_TYPE | — | ✅ |
| 16 | RuleInputPEORuleTmpltInputId | RULE_TMPLT_INPUT_ID | — | ✅ |
| 17 | RuleInputPEOTcatId | TCAT_ID | — | ✅ |
| 18 | RuleInputPEOUserDefinedName | USER_DEFINED_NAME | — | ✅ |
| 19 | RuleInputPEOValueDate | VALUE_DATE | — | ✅ |
| 20 | RuleInputPEOValueNumber | VALUE_NUMBER | — | ✅ |
| 21 | RuleInputPEOValueSetId | VALUE_SET_ID | — | ✅ |
| 22 | RuleInputPEOValueText | VALUE_TEXT | — | ✅ |

### [[hwm_tcats_vl|HWM_TCATS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeCategoryVLPEOTcatCd | TCAT_CD | — | ✅ |
| 2 | TimeCategoryVLPEOTcatId | TCAT_ID | — | ✅ |
| 3 | TimeCategoryVLPEOTcatName | TCAT_NAME | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
