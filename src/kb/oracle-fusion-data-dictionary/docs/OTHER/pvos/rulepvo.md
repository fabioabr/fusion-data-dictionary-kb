---
id: DOC-OTHER-PVO-RulePVO
doc_type: system-doc
title: "RulePVO — PVO Cross-Module"
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
  - RulePVO
  - rulepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RulePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Rule. Acessa as tabelas: FF_FORMULAS_VL, HWM_ALLOCATIONS_HDR_VL, HWM_RULES.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.RulesCoreAM.RulePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 38 | 3 | 1 | 28 | 74% |

---

## 🔗 Tabelas Relacionadas

- [[ff_formulas_vl|FF_FORMULAS_VL]] — 5 atributos (2 BICC)
- [[hwm_allocations_hdr_vl|HWM_ALLOCATIONS_HDR_VL]] — 4 atributos (2 BICC)
- [[hwm_rules|HWM_RULES]] — 29 atributos (1 PKs, 24 BICC)

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
| 18 | RulePEORuleId | RULE_ID | 🔑 | ✅ |
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

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
