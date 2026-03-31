---
id: DOC-GL-PVO-RuleTemplateInputPVO
doc_type: system-doc
title: "RuleTemplateInputPVO — PVO General Ledger"
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
  - RuleTemplateInputPVO
  - ruletemplateinputpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RuleTemplateInputPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Rule Template Input. Acessa as tabelas: FF_FORMULAS_VL, FND_VS_VALUE_SETS, HWM_ALLOCATIONS_HDR_VL (+4).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.RulesTemplatesAM.RuleTemplateInputPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 67 | 7 | 1 | 45 | 67% |

---

## 🔗 Tabelas Relacionadas

- [[ff_formulas_vl|FF_FORMULAS_VL]] — 5 atributos (2 BICC)
- [[fnd_vs_value_sets|FND_VS_VALUE_SETS]] — 3 atributos (1 BICC)
- [[hwm_allocations_hdr_vl|HWM_ALLOCATIONS_HDR_VL]] — 4 atributos (2 BICC)
- [[hwm_rule_tmplts|HWM_RULE_TMPLTS]] — 30 atributos (24 BICC)
- [[hwm_rule_tmplts_tl|HWM_RULE_TMPLTS_TL]] — 4 atributos (2 BICC)
- [[hwm_rule_tmplt_inputs|HWM_RULE_TMPLT_INPUTS]] — 17 atributos (1 PKs, 12 BICC)
- [[hwm_rule_tmplt_inputs_tl|HWM_RULE_TMPLT_INPUTS_TL]] — 4 atributos (2 BICC)

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

### [[hwm_rule_tmplts|HWM_RULE_TMPLTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RuleTemplateBPEOClassification | CLASSIFICATION | — | ✅ |
| 2 | RuleTemplateBPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | RuleTemplateBPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | RuleTemplateBPEODfltAllocationId | DFLT_ALLOCATION_ID | — | ✅ |
| 5 | RuleTemplateBPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 6 | RuleTemplateBPEOFastFormulaExecType | FAST_FORMULA_EXEC_TYPE | — | — |
| 7 | RuleTemplateBPEOIncludeEmptyTc | INCLUDE_EMPTY_TC | — | ✅ |
| 8 | RuleTemplateBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | RuleTemplateBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | RuleTemplateBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | RuleTemplateBPEOModuleId | MODULE_ID | — | — |
| 12 | RuleTemplateBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | RuleTemplateBPEOProcessName | PROCESS_NAME | — | ✅ |
| 14 | RuleTemplateBPEOProcessType | PROCESS_TYPE | — | ✅ |
| 15 | RuleTemplateBPEOPrsFormulaId | PRS_FORMULA_ID | — | ✅ |
| 16 | RuleTemplateBPEOPrsScriptId | PRS_SCRIPT_ID | — | — |
| 17 | RuleTemplateBPEORuleExecType | RULE_EXEC_TYPE | — | ✅ |
| 18 | RuleTemplateBPEORuleSubType | RULE_SUB_TYPE | — | ✅ |
| 19 | RuleTemplateBPEORuleTmpltsId | RULE_TMPLTS_ID | — | ✅ |
| 20 | RuleTemplateBPEORunEventDelete | RUN_EVENT_DELETE | — | ✅ |
| 21 | RuleTemplateBPEORunEventResub | RUN_EVENT_RESUB | — | ✅ |
| 22 | RuleTemplateBPEORunEventSave | RUN_EVENT_SAVE | — | ✅ |
| 23 | RuleTemplateBPEORunEventSub | RUN_EVENT_SUB | — | ✅ |
| 24 | RuleTemplateBPEORunSummationLevel | RUN_SUMMATION_LEVEL | — | ✅ |
| 25 | RuleTemplateBPEORunTbbLevel | RUN_TBB_LEVEL | — | ✅ |
| 26 | RuleTemplateBPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 27 | RuleTemplateBPEOSeededFlag | SEEDED_FLAG | — | ✅ |
| 28 | RuleTemplateBPEOSuppressDupMsgs | SUPPRESS_DUP_MSGS | — | ✅ |
| 29 | RuleTemplateBPEOTemplateName | TEMPLATE_NAME | — | ✅ |
| 30 | RuleTemplateBPEOTemplateType | TEMPLATE_TYPE | — | ✅ |

### [[hwm_rule_tmplts_tl|HWM_RULE_TMPLTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RuleTemplateTLPEODescription | DESCRIPTION | — | ✅ |
| 2 | RuleTemplateTLPEOLanguage | LANGUAGE | — | — |
| 3 | RuleTemplateTLPEORtExplanation | RT_EXPLANATION | — | ✅ |
| 4 | RuleTemplateTLPEORuleTmpltsId | RULE_TMPLTS_ID | — | — |

### [[hwm_rule_tmplt_inputs|HWM_RULE_TMPLT_INPUTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RuleTemplateInputBPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | RuleTemplateInputBPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | RuleTemplateInputBPEODisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 4 | RuleTemplateInputBPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 5 | RuleTemplateInputBPEOInputName | INPUT_NAME | — | ✅ |
| 6 | RuleTemplateInputBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | RuleTemplateInputBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | RuleTemplateInputBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | RuleTemplateInputBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | RuleTemplateInputBPEOParmValueRequired | PARM_VALUE_REQUIRED | — | ✅ |
| 11 | RuleTemplateInputBPEORuleParameterType | RULE_PARAMETER_TYPE | — | ✅ |
| 12 | RuleTemplateInputBPEORuleTmpltInputId | RULE_TMPLT_INPUT_ID | 🔑 | ✅ |
| 13 | RuleTemplateInputBPEORuleTmpltsId | RULE_TMPLTS_ID | — | ✅ |
| 14 | RuleTemplateInputBPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 15 | RuleTemplateInputBPEOSguid | SGUID | — | — |
| 16 | RuleTemplateInputBPEOUserDefinedName | USER_DEFINED_NAME | — | — |
| 17 | RuleTemplateInputBPEOValueSetId | VALUE_SET_ID | — | ✅ |

### [[hwm_rule_tmplt_inputs_tl|HWM_RULE_TMPLT_INPUTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RuleTemplateInputTLPEOInNameDescription | IN_NAME_DESCRIPTION | — | ✅ |
| 2 | RuleTemplateInputTLPEOLanguage | LANGUAGE | — | — |
| 3 | RuleTemplateInputTLPEORuleTmpltInputId | RULE_TMPLT_INPUT_ID | — | — |
| 4 | RuleTemplateInputTLPEOUserDefinedInName | USER_DEFINED_IN_NAME | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
