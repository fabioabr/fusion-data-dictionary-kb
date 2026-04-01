---
id: DOC-OTHER-PVO-ProjectPlanLinesHistoryExtractPVO
doc_type: system-doc
title: "ProjectPlanLinesHistoryExtractPVO — PVO Cross-Module"
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
  - ProjectPlanLinesHistoryExtractPVO
  - projectplanlineshistoryextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectPlanLinesHistoryExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Plan Lines History Extract. Acessa as tabelas: PJT_PROJ_PLAN_LINES_H.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjtBiccExtractAM.ProjectPlanLinesHistoryExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 67 | 1 | 1 | 67 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjt_proj_plan_lines_h|PJT_PROJ_PLAN_LINES_H]] — 67 atributos (1 PKs, 67 BICC)

---

## ⚙️ Atributos

### [[pjt_proj_plan_lines_h|PJT_PROJ_PLAN_LINES_H]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjPlanLinesHistoryEOActualExpenseCostAmount | ACTUAL_EXPENSE_COST_AMOUNT | — | ✅ |
| 2 | ProjPlanLinesHistoryEOActualFinishDate | ACTUAL_FINISH_DATE | — | ✅ |
| 3 | ProjPlanLinesHistoryEOActualLaborBilledAmount | ACTUAL_LABOR_BILLED_AMOUNT | — | ✅ |
| 4 | ProjPlanLinesHistoryEOActualLaborCostAmount | ACTUAL_LABOR_COST_AMOUNT | — | ✅ |
| 5 | ProjPlanLinesHistoryEOActualQuantity | ACTUAL_QUANTITY | — | ✅ |
| 6 | ProjPlanLinesHistoryEOActualStartDate | ACTUAL_START_DATE | — | ✅ |
| 7 | ProjPlanLinesHistoryEOApprovedDate | APPROVED_DATE | — | ✅ |
| 8 | ProjPlanLinesHistoryEOBaselineAllocation | BASELINE_ALLOCATION | — | ✅ |
| 9 | ProjPlanLinesHistoryEOBaselineDuration | BASELINE_DURATION | — | ✅ |
| 10 | ProjPlanLinesHistoryEOBaselineExpenseCostAmount | BASELINE_EXPENSE_COST_AMOUNT | — | ✅ |
| 11 | ProjPlanLinesHistoryEOBaselineFinishDate | BASELINE_FINISH_DATE | — | ✅ |
| 12 | ProjPlanLinesHistoryEOBaselineLaborBilledAmount | BASELINE_LABOR_BILLED_AMOUNT | — | ✅ |
| 13 | ProjPlanLinesHistoryEOBaselineLaborCostAmount | BASELINE_LABOR_COST_AMOUNT | — | ✅ |
| 14 | ProjPlanLinesHistoryEOBaselineQuantity | BASELINE_QUANTITY | — | ✅ |
| 15 | ProjPlanLinesHistoryEOBaselineStartDate | BASELINE_START_DATE | — | ✅ |
| 16 | ProjPlanLinesHistoryEOCostPercentComplete | COST_PERCENT_COMPLETE | — | ✅ |
| 17 | ProjPlanLinesHistoryEOCreatedBy | CREATED_BY | — | ✅ |
| 18 | ProjPlanLinesHistoryEOCreationDate | CREATION_DATE | — | ✅ |
| 19 | ProjPlanLinesHistoryEODenormResourceClass | DENORM_RESOURCE_CLASS | — | ✅ |
| 20 | ProjPlanLinesHistoryEODuration | DURATION | — | ✅ |
| 21 | ProjPlanLinesHistoryEOElementVersionId | ELEMENT_VERSION_ID | — | ✅ |
| 22 | ProjPlanLinesHistoryEOExpenseCostAmount | EXPENSE_COST_AMOUNT | — | ✅ |
| 23 | ProjPlanLinesHistoryEOFinishDate | FINISH_DATE | — | ✅ |
| 24 | ProjPlanLinesHistoryEOHealthStsCode | HEALTH_STS_CODE | — | ✅ |
| 25 | ProjPlanLinesHistoryEOId | ID | 🔑 | ✅ |
| 26 | ProjPlanLinesHistoryEOInitiatedDate | INITIATED_DATE | — | ✅ |
| 27 | ProjPlanLinesHistoryEOItdQuantity | ITD_QUANTITY | — | ✅ |
| 28 | ProjPlanLinesHistoryEOLaborBilledAmount | LABOR_BILLED_AMOUNT | — | ✅ |
| 29 | ProjPlanLinesHistoryEOLaborCostAmount | LABOR_COST_AMOUNT | — | ✅ |
| 30 | ProjPlanLinesHistoryEOLastCommentDate | LAST_COMMENT_DATE | — | ✅ |
| 31 | ProjPlanLinesHistoryEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | ProjPlanLinesHistoryEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 33 | ProjPlanLinesHistoryEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 34 | ProjPlanLinesHistoryEONumberOfExceptions | NUMBER_OF_EXCEPTIONS | — | ✅ |
| 35 | ProjPlanLinesHistoryEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 36 | ProjPlanLinesHistoryEOPercentComplete | PERCENT_COMPLETE | — | ✅ |
| 37 | ProjPlanLinesHistoryEOPersonId | PERSON_ID | — | ✅ |
| 38 | ProjPlanLinesHistoryEOPhysicalPercentComplete | PHYSICAL_PERCENT_COMPLETE | — | ✅ |
| 39 | ProjPlanLinesHistoryEOPlanLineId | PLAN_LINE_ID | — | ✅ |
| 40 | ProjPlanLinesHistoryEOPlanLineTypeCode | PLAN_LINE_TYPE_CODE | — | ✅ |
| 41 | ProjPlanLinesHistoryEOPlanVersionId | PLAN_VERSION_ID | — | ✅ |
| 42 | ProjPlanLinesHistoryEOPmPlanProgressRef | PM_PLAN_PROGRESS_REF | — | ✅ |
| 43 | ProjPlanLinesHistoryEOPmProductCode | PM_PRODUCT_CODE | — | ✅ |
| 44 | ProjPlanLinesHistoryEOPriority | PRIORITY | — | ✅ |
| 45 | ProjPlanLinesHistoryEOProgressEnteredDate | PROGRESS_ENTERED_DATE | — | ✅ |
| 46 | ProjPlanLinesHistoryEOProgressStatusCode | PROGRESS_STATUS_CODE | — | ✅ |
| 47 | ProjPlanLinesHistoryEOProjElementId | PROJ_ELEMENT_ID | — | ✅ |
| 48 | ProjPlanLinesHistoryEOProjectId | PROJECT_ID | — | ✅ |
| 49 | ProjPlanLinesHistoryEOProposedDuration | PROPOSED_DURATION | — | ✅ |
| 50 | ProjPlanLinesHistoryEOProposedFinishDate | PROPOSED_FINISH_DATE | — | ✅ |
| 51 | ProjPlanLinesHistoryEOProposedQuantity | PROPOSED_QUANTITY | — | ✅ |
| 52 | ProjPlanLinesHistoryEOProposedResAllocation | PROPOSED_RES_ALLOCATION | — | ✅ |
| 53 | ProjPlanLinesHistoryEOProposedStartDate | PROPOSED_START_DATE | — | ✅ |
| 54 | ProjPlanLinesHistoryEOQuantity | QUANTITY | — | ✅ |
| 55 | ProjPlanLinesHistoryEORemainingExpenseCostAmount | REMAINING_EXPENSE_COST_AMOUNT | — | ✅ |
| 56 | ProjPlanLinesHistoryEORemainingLaborBilledAmount | REMAINING_LABOR_BILLED_AMOUNT | — | ✅ |
| 57 | ProjPlanLinesHistoryEORemainingLaborCostAmount | REMAINING_LABOR_COST_AMOUNT | — | ✅ |
| 58 | ProjPlanLinesHistoryEORemainingQuantity | REMAINING_QUANTITY | — | ✅ |
| 59 | ProjPlanLinesHistoryEOResourceAllocationPercent | RESOURCE_ALLOCATION_PERCENT | — | ✅ |
| 60 | ProjPlanLinesHistoryEOResourceId | RESOURCE_ID | — | ✅ |
| 61 | ProjPlanLinesHistoryEORollupFlag | ROLLUP_FLAG | — | ✅ |
| 62 | ProjPlanLinesHistoryEORollupPlanLine | ROLLUP_PLAN_LINE | — | ✅ |
| 63 | ProjPlanLinesHistoryEOStartDate | START_DATE | — | ✅ |
| 64 | ProjPlanLinesHistoryEOTaskAssignedDate | TASK_ASSIGNED_DATE | — | ✅ |
| 65 | ProjPlanLinesHistoryEOTotalActualCostAmount | TOTAL_ACTUAL_COST_AMOUNT | — | ✅ |
| 66 | ProjPlanLinesHistoryEOTotalCostAmount | TOTAL_COST_AMOUNT | — | ✅ |
| 67 | ProjPlanLinesHistoryEOTotalRemainingCostAmount | TOTAL_REMAINING_COST_AMOUNT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
