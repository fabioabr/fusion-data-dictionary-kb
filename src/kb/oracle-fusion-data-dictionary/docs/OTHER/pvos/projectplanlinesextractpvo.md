---
id: DOC-OTHER-PVO-ProjectPlanLinesExtractPVO
doc_type: system-doc
title: "ProjectPlanLinesExtractPVO — PVO Cross-Module"
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
  - ProjectPlanLinesExtractPVO
  - projectplanlinesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectPlanLinesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Plan Lines Extract. Acessa as tabelas: PJT_PROJ_PLAN_LINES.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjtBiccExtractAM.ProjectPlanLinesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 105 | 1 | 1 | 105 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjt_proj_plan_lines|PJT_PROJ_PLAN_LINES]] — 105 atributos (1 PKs, 105 BICC)

---

## ⚙️ Atributos

### [[pjt_proj_plan_lines|PJT_PROJ_PLAN_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PhysicalPercentComplete | PHYSICAL_PERCENT_COMPLETE | — | ✅ |
| 2 | ProjPlanLineEOActualExpenseCostAmount | ACTUAL_EXPENSE_COST_AMOUNT | — | ✅ |
| 3 | ProjPlanLineEOActualFinishDate | ACTUAL_FINISH_DATE | — | ✅ |
| 4 | ProjPlanLineEOActualFinishDateTime | ACTUAL_FINISH_DATE | — | ✅ |
| 5 | ProjPlanLineEOActualLaborBilledAmount | ACTUAL_LABOR_BILLED_AMOUNT | — | ✅ |
| 6 | ProjPlanLineEOActualLaborCostAmount | ACTUAL_LABOR_COST_AMOUNT | — | ✅ |
| 7 | ProjPlanLineEOActualQuantity | ACTUAL_QUANTITY | — | ✅ |
| 8 | ProjPlanLineEOActualStartDate | ACTUAL_START_DATE | — | ✅ |
| 9 | ProjPlanLineEOActualStartDateTime | ACTUAL_START_DATE | — | ✅ |
| 10 | ProjPlanLineEOApprovedDate | APPROVED_DATE | — | ✅ |
| 11 | ProjPlanLineEOAtCompletionDuration | AT_COMPLETION_DURATION | — | ✅ |
| 12 | ProjPlanLineEOAtCompletionExpenseCost | AT_COMPLETION_EXPENSE_COST | — | ✅ |
| 13 | ProjPlanLineEOAtCompletionFinishDate | AT_COMPLETION_FINISH_DATE | — | ✅ |
| 14 | ProjPlanLineEOAtCompletionFinishTime | AT_COMPLETION_FINISH_TIME | — | ✅ |
| 15 | ProjPlanLineEOAtCompletionLaborBill | AT_COMPLETION_LABOR_BILL | — | ✅ |
| 16 | ProjPlanLineEOAtCompletionLaborCost | AT_COMPLETION_LABOR_COST | — | ✅ |
| 17 | ProjPlanLineEOAtCompletionStartDate | AT_COMPLETION_START_DATE | — | ✅ |
| 18 | ProjPlanLineEOAtCompletionStartTime | AT_COMPLETION_START_TIME | — | ✅ |
| 19 | ProjPlanLineEOAtCompletionTotalCost | AT_COMPLETION_TOTAL_COST | — | ✅ |
| 20 | ProjPlanLineEOBaselineAllocation | BASELINE_ALLOCATION | — | ✅ |
| 21 | ProjPlanLineEOBaselineDuration | BASELINE_DURATION | — | ✅ |
| 22 | ProjPlanLineEOBaselineExpenseCostAmount | BASELINE_EXPENSE_COST_AMOUNT | — | ✅ |
| 23 | ProjPlanLineEOBaselineFinishDate | BASELINE_FINISH_DATE | — | ✅ |
| 24 | ProjPlanLineEOBaselineFinishDateTime | BASELINE_FINISH_DATE | — | ✅ |
| 25 | ProjPlanLineEOBaselineLaborBilledAmount | BASELINE_LABOR_BILLED_AMOUNT | — | ✅ |
| 26 | ProjPlanLineEOBaselineLaborCostAmount | BASELINE_LABOR_COST_AMOUNT | — | ✅ |
| 27 | ProjPlanLineEOBaselineQuantity | BASELINE_QUANTITY | — | ✅ |
| 28 | ProjPlanLineEOBaselineStartDate | BASELINE_START_DATE | — | ✅ |
| 29 | ProjPlanLineEOBaselineStartDateTime | BASELINE_START_DATE | — | ✅ |
| 30 | ProjPlanLineEOCostPercentComplete | COST_PERCENT_COMPLETE | — | ✅ |
| 31 | ProjPlanLineEOCreatedBy | CREATED_BY | — | ✅ |
| 32 | ProjPlanLineEOCreationDate | CREATION_DATE | — | ✅ |
| 33 | ProjPlanLineEOCreationSource | CREATION_SOURCE | — | ✅ |
| 34 | ProjPlanLineEOCurrentActualQuantity | AT_COMPLETION_QUANTITY | — | ✅ |
| 35 | ProjPlanLineEODenormResourceClass | DENORM_RESOURCE_CLASS | — | ✅ |
| 36 | ProjPlanLineEODuration | DURATION | — | ✅ |
| 37 | ProjPlanLineEOEarlyFinishDate | EARLY_FINISH_DATE | — | ✅ |
| 38 | ProjPlanLineEOEarlyFinishDateTime | EARLY_FINISH_DATE | — | ✅ |
| 39 | ProjPlanLineEOEarlyStartDate | EARLY_START_DATE | — | ✅ |
| 40 | ProjPlanLineEOEarlyStartDateTime | EARLY_START_DATE | — | ✅ |
| 41 | ProjPlanLineEOEffectiveBillRate | EFFECTIVE_BILL_RATE | — | ✅ |
| 42 | ProjPlanLineEOEffectiveCostRate | EFFECTIVE_COST_RATE | — | ✅ |
| 43 | ProjPlanLineEOElementVersionId | ELEMENT_VERSION_ID | — | ✅ |
| 44 | ProjPlanLineEOExpenseCostAmount | EXPENSE_COST_AMOUNT | — | ✅ |
| 45 | ProjPlanLineEOFinishDate | FINISH_DATE | — | ✅ |
| 46 | ProjPlanLineEOFreeFloat | FREE_FLOAT | — | ✅ |
| 47 | ProjPlanLineEOGateStatusCode | GATE_STATUS_CODE | — | ✅ |
| 48 | ProjPlanLineEOHealthStsCode | HEALTH_STS_CODE | — | ✅ |
| 49 | ProjPlanLineEOId | ID | 🔑 | ✅ |
| 50 | ProjPlanLineEOInitiatedDate | INITIATED_DATE | — | ✅ |
| 51 | ProjPlanLineEOItdQuantity | ITD_QUANTITY | — | ✅ |
| 52 | ProjPlanLineEOLaborBilledAmount | LABOR_BILLED_AMOUNT | — | ✅ |
| 53 | ProjPlanLineEOLaborCostAmount | LABOR_COST_AMOUNT | — | ✅ |
| 54 | ProjPlanLineEOLastCommentDate | LAST_COMMENT_DATE | — | ✅ |
| 55 | ProjPlanLineEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 56 | ProjPlanLineEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 57 | ProjPlanLineEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 58 | ProjPlanLineEOLateFinishDate | LATE_FINISH_DATE | — | ✅ |
| 59 | ProjPlanLineEOLateFinishDateTime | LATE_FINISH_DATE | — | ✅ |
| 60 | ProjPlanLineEOLateStartDate | LATE_START_DATE | — | ✅ |
| 61 | ProjPlanLineEOLateStartDateTime | LATE_START_DATE | — | ✅ |
| 62 | ProjPlanLineEONumberOfExceptions | NUMBER_OF_EXCEPTIONS | — | ✅ |
| 63 | ProjPlanLineEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 64 | ProjPlanLineEOPercentComplete | PERCENT_COMPLETE | — | ✅ |
| 65 | ProjPlanLineEOPersonId | PERSON_ID | — | ✅ |
| 66 | ProjPlanLineEOPlanLineId | PLAN_LINE_ID | — | ✅ |
| 67 | ProjPlanLineEOPlanLineTypeCode | PLAN_LINE_TYPE_CODE | — | ✅ |
| 68 | ProjPlanLineEOPlanVersionId | PLAN_VERSION_ID | — | ✅ |
| 69 | ProjPlanLineEOPlannedFinishDateTime | FINISH_DATE | — | ✅ |
| 70 | ProjPlanLineEOPlannedStartDateTime | START_DATE | — | ✅ |
| 71 | ProjPlanLineEOPmPlanProgressRef | PM_PLAN_PROGRESS_REF | — | ✅ |
| 72 | ProjPlanLineEOPmProductCode | PM_PRODUCT_CODE | — | ✅ |
| 73 | ProjPlanLineEOPriority | PRIORITY | — | ✅ |
| 74 | ProjPlanLineEOPrjResourceAssignId | PRJ_RESOURCE_ASSIGN_ID | — | ✅ |
| 75 | ProjPlanLineEOProgressEnteredDate | PROGRESS_ENTERED_DATE | — | ✅ |
| 76 | ProjPlanLineEOProgressStatusCode | PROGRESS_STATUS_CODE | — | ✅ |
| 77 | ProjPlanLineEOProjElementId | PROJ_ELEMENT_ID | — | ✅ |
| 78 | ProjPlanLineEOProjectId | PROJECT_ID | — | ✅ |
| 79 | ProjPlanLineEOProposedDuration | PROPOSED_DURATION | — | ✅ |
| 80 | ProjPlanLineEOProposedFinishDate | PROPOSED_FINISH_DATE | — | ✅ |
| 81 | ProjPlanLineEOProposedFinishDateTime | PROPOSED_FINISH_DATE | — | ✅ |
| 82 | ProjPlanLineEOProposedQuantity | PROPOSED_QUANTITY | — | ✅ |
| 83 | ProjPlanLineEOProposedResAllocation | PROPOSED_RES_ALLOCATION | — | ✅ |
| 84 | ProjPlanLineEOProposedStartDate | PROPOSED_START_DATE | — | ✅ |
| 85 | ProjPlanLineEOProposedStartDateTime | PROPOSED_START_DATE | — | ✅ |
| 86 | ProjPlanLineEOQuantity | QUANTITY | — | ✅ |
| 87 | ProjPlanLineEORemainingExpenseCostAmount | REMAINING_EXPENSE_COST_AMOUNT | — | ✅ |
| 88 | ProjPlanLineEORemainingLaborBilledAmount | REMAINING_LABOR_BILLED_AMOUNT | — | ✅ |
| 89 | ProjPlanLineEORemainingLaborCostAmount | REMAINING_LABOR_COST_AMOUNT | — | ✅ |
| 90 | ProjPlanLineEORemainingQuantity | REMAINING_QUANTITY | — | ✅ |
| 91 | ProjPlanLineEOResourceAllocationPercent | RESOURCE_ALLOCATION_PERCENT | — | ✅ |
| 92 | ProjPlanLineEOResourceId | RESOURCE_ID | — | ✅ |
| 93 | ProjPlanLineEORollupFlag | ROLLUP_FLAG | — | ✅ |
| 94 | ProjPlanLineEORollupPlanLine | ROLLUP_PLAN_LINE | — | ✅ |
| 95 | ProjPlanLineEOShowInTimelineFlag | SHOW_IN_TIMELINE_FLAG | — | ✅ |
| 96 | ProjPlanLineEOStartDate | START_DATE | — | ✅ |
| 97 | ProjPlanLineEOTaskAssignedDate | TASK_ASSIGNED_DATE | — | ✅ |
| 98 | ProjPlanLineEOTaskDeadline | TASK_DEADLINE | — | ✅ |
| 99 | ProjPlanLineEOTaskDeadlineDateTime | TASK_DEADLINE | — | ✅ |
| 100 | ProjPlanLineEOTotalActualCostAmount | TOTAL_ACTUAL_COST_AMOUNT | — | ✅ |
| 101 | ProjPlanLineEOTotalCostAmount | TOTAL_COST_AMOUNT | — | ✅ |
| 102 | ProjPlanLineEOTotalFloat | TOTAL_FLOAT | — | ✅ |
| 103 | ProjPlanLineEOTotalRemainingCostAmount | TOTAL_REMAINING_COST_AMOUNT | — | ✅ |
| 104 | ProjPlanLineEOUpdateSource | UPDATE_SOURCE | — | ✅ |
| 105 | ProjPlanLineEOWorkitemsCompleteFlag | WORKITEMS_COMPLETE_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
