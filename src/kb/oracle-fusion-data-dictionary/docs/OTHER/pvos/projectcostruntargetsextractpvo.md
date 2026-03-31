---
id: DOC-OTHER-PVO-ProjectCostRunTargetsExtractPVO
doc_type: system-doc
title: "ProjectCostRunTargetsExtractPVO — PVO Cross-Module"
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
  - ProjectCostRunTargetsExtractPVO
  - projectcostruntargetsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectCostRunTargetsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Cost Run Targets Extract. Acessa as tabelas: PJC_ALLOC_RUN_TARGETS.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjcBiccExtractAM.ProjectCostRunTargetsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 50 | 1 | 1 | 32 | 64% |

---

## 🔗 Tabelas Relacionadas

- [[pjc_alloc_run_targets|PJC_ALLOC_RUN_TARGETS]] — 50 atributos (1 PKs, 32 BICC)

---

## ⚙️ Atributos

### [[pjc_alloc_run_targets|PJC_ALLOC_RUN_TARGETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LaborDistRunTargetsPEOBasisFactor | BASIS_FACTOR | — | ✅ |
| 2 | LaborDistRunTargetsPEOBillableFlag | BILLABLE_FLAG | — | ✅ |
| 3 | LaborDistRunTargetsPEOBudgetaryControlValStatus | BUDGETARY_CONTROL_VAL_STATUS | — | ✅ |
| 4 | LaborDistRunTargetsPEOCapitalizableFlag | CAPITALIZABLE_FLAG | — | ✅ |
| 5 | LaborDistRunTargetsPEOContextCategory | CONTEXT_CATEGORY | — | ✅ |
| 6 | LaborDistRunTargetsPEOContractId | CONTRACT_ID | — | ✅ |
| 7 | LaborDistRunTargetsPEOContractLineId | CONTRACT_LINE_ID | — | ✅ |
| 8 | LaborDistRunTargetsPEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | LaborDistRunTargetsPEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | LaborDistRunTargetsPEOExcludeFlag | EXCLUDE_FLAG | — | ✅ |
| 11 | LaborDistRunTargetsPEOExpenditureItemDate | EXPENDITURE_ITEM_DATE | — | ✅ |
| 12 | LaborDistRunTargetsPEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | ✅ |
| 13 | LaborDistRunTargetsPEOFundingAllocationId | FUNDING_ALLOCATION_ID | — | ✅ |
| 14 | LaborDistRunTargetsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | LaborDistRunTargetsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 16 | LaborDistRunTargetsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | LaborDistRunTargetsPEOLdSuspenseAcctFlag | LD_SUSPENSE_ACCT_FLAG | — | ✅ |
| 18 | LaborDistRunTargetsPEOLdTargetCcid | LD_TARGET_CCID | — | ✅ |
| 19 | LaborDistRunTargetsPEOLineNum | LINE_NUM | — | ✅ |
| 20 | LaborDistRunTargetsPEOLinePercent | LINE_PERCENT | — | ✅ |
| 21 | LaborDistRunTargetsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 22 | LaborDistRunTargetsPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 23 | LaborDistRunTargetsPEOPlanVersionId | PLAN_VERSION_ID | — | ✅ |
| 24 | LaborDistRunTargetsPEOProjectId | PROJECT_ID | — | ✅ |
| 25 | LaborDistRunTargetsPEOReservedAttribute1 | RESERVED_ATTRIBUTE1 | — | ✅ |
| 26 | LaborDistRunTargetsPEOReservedAttribute10 | RESERVED_ATTRIBUTE10 | — | ✅ |
| 27 | LaborDistRunTargetsPEOReservedAttribute2 | RESERVED_ATTRIBUTE2 | — | — |
| 28 | LaborDistRunTargetsPEOReservedAttribute3 | RESERVED_ATTRIBUTE3 | — | — |
| 29 | LaborDistRunTargetsPEOReservedAttribute4 | RESERVED_ATTRIBUTE4 | — | — |
| 30 | LaborDistRunTargetsPEOReservedAttribute5 | RESERVED_ATTRIBUTE5 | — | — |
| 31 | LaborDistRunTargetsPEOReservedAttribute6 | RESERVED_ATTRIBUTE6 | — | — |
| 32 | LaborDistRunTargetsPEOReservedAttribute7 | RESERVED_ATTRIBUTE7 | — | — |
| 33 | LaborDistRunTargetsPEOReservedAttribute8 | RESERVED_ATTRIBUTE8 | — | — |
| 34 | LaborDistRunTargetsPEOReservedAttribute9 | RESERVED_ATTRIBUTE9 | — | — |
| 35 | LaborDistRunTargetsPEOReversalRunTargetId | REVERSAL_RUN_TARGET_ID | — | ✅ |
| 36 | LaborDistRunTargetsPEORuleId | RULE_ID | — | ✅ |
| 37 | LaborDistRunTargetsPEORunId | RUN_ID | — | ✅ |
| 38 | LaborDistRunTargetsPEORunTargetId | RUN_TARGET_ID | 🔑 | ✅ |
| 39 | LaborDistRunTargetsPEOTaskId | TASK_ID | — | ✅ |
| 40 | LaborDistRunTargetsPEOUserDefAttribute1 | USER_DEF_ATTRIBUTE1 | — | — |
| 41 | LaborDistRunTargetsPEOUserDefAttribute10 | USER_DEF_ATTRIBUTE10 | — | — |
| 42 | LaborDistRunTargetsPEOUserDefAttribute2 | USER_DEF_ATTRIBUTE2 | — | — |
| 43 | LaborDistRunTargetsPEOUserDefAttribute3 | USER_DEF_ATTRIBUTE3 | — | — |
| 44 | LaborDistRunTargetsPEOUserDefAttribute4 | USER_DEF_ATTRIBUTE4 | — | — |
| 45 | LaborDistRunTargetsPEOUserDefAttribute5 | USER_DEF_ATTRIBUTE5 | — | — |
| 46 | LaborDistRunTargetsPEOUserDefAttribute6 | USER_DEF_ATTRIBUTE6 | — | — |
| 47 | LaborDistRunTargetsPEOUserDefAttribute7 | USER_DEF_ATTRIBUTE7 | — | — |
| 48 | LaborDistRunTargetsPEOUserDefAttribute8 | USER_DEF_ATTRIBUTE8 | — | — |
| 49 | LaborDistRunTargetsPEOUserDefAttribute9 | USER_DEF_ATTRIBUTE9 | — | — |
| 50 | LaborDistRunTargetsPEOWorkTypeId | WORK_TYPE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
