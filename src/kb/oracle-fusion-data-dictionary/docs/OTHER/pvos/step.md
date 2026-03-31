---
id: DOC-OTHER-PVO-Step
doc_type: system-doc
title: "Step — PVO Cross-Module"
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
  - Step
  - step
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# Step

## 📌 Visão Geral

View Object para extração BICC de dados de Step. Acessa as tabelas: DOO_PROCESS_STEPS_B, DOO_PROCESS_STEPS_TL.

**Caminho:** `FscmTopModelAM.DooTopAM.Step`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 48 | 2 | 1 | 13 | 27% |

---

## 🔗 Tabelas Relacionadas

- [[doo_process_steps_b|DOO_PROCESS_STEPS_B]] — 37 atributos (1 PKs, 10 BICC)
- [[doo_process_steps_tl|DOO_PROCESS_STEPS_TL]] — 11 atributos (3 BICC)

---

## ⚙️ Atributos

### [[doo_process_steps_b|DOO_PROCESS_STEPS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurrentStepCheckWithFsBeforeChange | CHECK_WITH_FS_BEFORE_CHANGE | — | — |
| 2 | CurrentStepCompPatternRlsId | COMP_PATTERN_RLS_ID | — | — |
| 3 | CurrentStepCompPatternRlsName | COMP_PATTERN_RLS_NAME | — | — |
| 4 | CurrentStepCreatedBy | CREATED_BY | — | — |
| 5 | CurrentStepCreationDate | CREATION_DATE | — | — |
| 6 | CurrentStepDefaultBranchFlag | DEFAULT_BRANCH_FLAG | — | — |
| 7 | CurrentStepDefaultExitStatusCode | DEFAULT_EXIT_STATUS_CODE | — | — |
| 8 | CurrentStepDefaultLeadTime | DEFAULT_LEAD_TIME | — | ✅ |
| 9 | CurrentStepDefaultLeadTimeUom | DEFAULT_LEAD_TIME_UOM | — | ✅ |
| 10 | CurrentStepDooProcessId | DOO_PROCESS_ID | — | ✅ |
| 11 | CurrentStepDooProcessVersion | DOO_PROCESS_VERSION | — | — |
| 12 | CurrentStepDooSubProcessId | DOO_SUB_PROCESS_ID | — | — |
| 13 | CurrentStepExitCriteriaStatusCode | EXIT_CRITERIA_STATUS_CODE | — | — |
| 14 | CurrentStepHoldOnWait | HOLD_ON_WAIT | — | — |
| 15 | CurrentStepLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | CurrentStepLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | CurrentStepLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | CurrentStepLeadTimeRlsId | LEAD_TIME_RLS_ID | — | — |
| 19 | CurrentStepLeadTimeRlsName | LEAD_TIME_RLS_NAME | — | — |
| 20 | CurrentStepManualStepFlag | MANUAL_STEP_FLAG | — | ✅ |
| 21 | CurrentStepObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | CurrentStepOtherwiseFlag | OTHERWISE_FLAG | — | — |
| 23 | CurrentStepParentStepNumber | PARENT_STEP_NUMBER | — | — |
| 24 | CurrentStepPreviousVersionStepId | PREVIOUS_VERSION_STEP_ID | — | — |
| 25 | CurrentStepServiceId | SERVICE_ID | — | — |
| 26 | CurrentStepSplitUnitName | SPLIT_UNIT_NAME | — | ✅ |
| 27 | CurrentStepStepFilterRlsId | STEP_FILTER_RLS_ID | — | — |
| 28 | CurrentStepStepFilterRlsName | STEP_FILTER_RLS_NAME | — | — |
| 29 | CurrentStepStepId | STEP_ID | 🔑 | ✅ |
| 30 | CurrentStepStepNumber | STEP_NUMBER | — | ✅ |
| 31 | CurrentStepStepType | STEP_TYPE | — | ✅ |
| 32 | CurrentStepSubProcessVersion | SUB_PROCESS_VERSION | — | — |
| 33 | CurrentStepSwitchConditionEvalSeq | SWITCH_CONDITION_EVAL_SEQ | — | — |
| 34 | CurrentStepSwitchRlsId | SWITCH_RLS_ID | — | — |
| 35 | CurrentStepSwitchRlsName | SWITCH_RLS_NAME | — | — |
| 36 | CurrentStepTaskId | TASK_ID | — | ✅ |
| 37 | CurrentStepUseDynamicAttrInDeltaComp | USE_DYNAMIC_ATTR_IN_DELTA_COMP | — | — |

### [[doo_process_steps_tl|DOO_PROCESS_STEPS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurrentStepTranslationCreatedBy | CREATED_BY | — | — |
| 2 | CurrentStepTranslationCreationDate | CREATION_DATE | — | — |
| 3 | CurrentStepTranslationLanguage | LANGUAGE | — | ✅ |
| 4 | CurrentStepTranslationLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 5 | CurrentStepTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | CurrentStepTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | CurrentStepTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | CurrentStepTranslationSourceLang | SOURCE_LANG | — | — |
| 9 | CurrentStepTranslationSplitUnitDisplayName | SPLIT_UNIT_DISPLAY_NAME | — | ✅ |
| 10 | CurrentStepTranslationStepId | STEP_ID | — | — |
| 11 | CurrentStepTranslationStepName | STEP_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
