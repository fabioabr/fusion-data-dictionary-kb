---
id: DOC-OTHER-PVO-RuleTemplatePVO
doc_type: system-doc
title: "RuleTemplatePVO — PVO Cross-Module"
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
  - RuleTemplatePVO
  - ruletemplatepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RuleTemplatePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Rule Template. Acessa as tabelas: FF_FORMULAS_VL, HWM_ALLOCATIONS_HDR_VL, HWM_RULE_TMPLTS (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.RulesTemplatesAM.RuleTemplatePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 43 | 4 | 1 | 32 | 74% |

---

## 🔗 Tabelas Relacionadas

- [[ff_formulas_vl|FF_FORMULAS_VL]] — 5 atributos (3 BICC)
- [[hwm_allocations_hdr_vl|HWM_ALLOCATIONS_HDR_VL]] — 4 atributos (3 BICC)
- [[hwm_rule_tmplts|HWM_RULE_TMPLTS]] — 30 atributos (1 PKs, 24 BICC)
- [[hwm_rule_tmplts_tl|HWM_RULE_TMPLTS_TL]] — 4 atributos (2 BICC)

---

## ⚙️ Atributos

### [[ff_formulas_vl|FF_FORMULAS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FormulaDPEOBaseFormulaName | BASE_FORMULA_NAME | — | ✅ |
| 2 | FormulaDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | FormulaDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | FormulaDPEOFormulaId | FORMULA_ID | — | — |
| 5 | FormulaDPEOFormulaName | FORMULA_NAME | — | ✅ |

### [[hwm_allocations_hdr_vl|HWM_ALLOCATIONS_HDR_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllocationsHdrVLPEOAllocationId | ALLOCATION_ID | — | ✅ |
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
| 19 | RuleTemplateBPEORuleTmpltsId | RULE_TMPLTS_ID | 🔑 | ✅ |
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

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
