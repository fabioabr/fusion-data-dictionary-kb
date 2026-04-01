---
id: DOC-OTHER-PVO-EPSFactPVO
doc_type: system-doc
title: "EPSFactPVO — PVO Cross-Module"
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
  - EPSFactPVO
  - epsfactpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EPSFactPVO

## 📌 Visão Geral

View Object para extração BICC de dados de EPSFact. Acessa as tabelas: PJF_PROJECTS_ALL_B, PJF_PROJ_ELEMENT_VERSION, PJT_PROJ_PLAN_LINES (+1).

**Caminho:** `FscmTopModelAM.PjtProjectPlanAM.EPSFactPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 83 | 4 | 1 | 31 | 37% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 3 atributos
- [[pjf_proj_element_version|PJF_PROJ_ELEMENT_VERSION]] — 3 atributos
- [[pjt_proj_plan_lines|PJT_PROJ_PLAN_LINES]] — 62 atributos (1 PKs, 31 BICC)
- [[pjt_proj_ref_object_vl|PJT_PROJ_REF_OBJECT_VL]] — 15 atributos

---

## ⚙️ Atributos

### [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CarryingOutOrganizationId | CARRYING_OUT_ORGANIZATION_ID | — | — |
| 2 | OrgId | ORG_ID | — | — |
| 3 | ProjectId | PROJECT_ID | — | — |

### [[pjf_proj_element_version|PJF_PROJ_ELEMENT_VERSION]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjtProjElementVersionPEOElementVersionId | ELEMENT_VERSION_ID | — | — |
| 2 | PjtProjElementVersionPEOExecutionLeaf | EXECUTION_LEAF | — | — |
| 3 | PjtProjElementVersionPEOObjectType | OBJECT_TYPE | — | — |

### [[pjt_proj_plan_lines|PJT_PROJ_PLAN_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostPercentComplete | COST_PERCENT_COMPLETE | — | ✅ |
| 2 | Id | ID | 🔑 | ✅ |
| 3 | ProjPlanLinePEOActualExpenseCostAmount | ACTUAL_EXPENSE_COST_AMOUNT | — | ✅ |
| 4 | ProjPlanLinePEOActualFinishDate | ACTUAL_FINISH_DATE | — | ✅ |
| 5 | ProjPlanLinePEOActualLaborBilledAmount | ACTUAL_LABOR_BILLED_AMOUNT | — | ✅ |
| 6 | ProjPlanLinePEOActualLaborCostAmount | ACTUAL_LABOR_COST_AMOUNT | — | ✅ |
| 7 | ProjPlanLinePEOActualQuantity | ACTUAL_QUANTITY | — | — |
| 8 | ProjPlanLinePEOActualStartDate | ACTUAL_START_DATE | — | ✅ |
| 9 | ProjPlanLinePEOApprovedDate | APPROVED_DATE | — | — |
| 10 | ProjPlanLinePEOBaselineAllocation | BASELINE_ALLOCATION | — | — |
| 11 | ProjPlanLinePEOBaselineDuration | BASELINE_DURATION | — | — |
| 12 | ProjPlanLinePEOBaselineFinishDate | BASELINE_FINISH_DATE | — | — |
| 13 | ProjPlanLinePEOBaselineQuantity | BASELINE_QUANTITY | — | — |
| 14 | ProjPlanLinePEOBaselineStartDate | BASELINE_START_DATE | — | — |
| 15 | ProjPlanLinePEOCreatedBy | CREATED_BY | — | — |
| 16 | ProjPlanLinePEOCreationDate | CREATION_DATE | — | — |
| 17 | ProjPlanLinePEODuration | DURATION | — | ✅ |
| 18 | ProjPlanLinePEOElementVersionId | ELEMENT_VERSION_ID | — | — |
| 19 | ProjPlanLinePEOExpenseCostAmount | EXPENSE_COST_AMOUNT | — | ✅ |
| 20 | ProjPlanLinePEOFinishDate | FINISH_DATE | — | ✅ |
| 21 | ProjPlanLinePEOHealthStsCode | HEALTH_STS_CODE | — | — |
| 22 | ProjPlanLinePEOInitiatedDate | INITIATED_DATE | — | — |
| 23 | ProjPlanLinePEOItdQuantity | ITD_QUANTITY | — | ✅ |
| 24 | ProjPlanLinePEOLaborBilledAmount | LABOR_BILLED_AMOUNT | — | ✅ |
| 25 | ProjPlanLinePEOLaborCostAmount | LABOR_COST_AMOUNT | — | ✅ |
| 26 | ProjPlanLinePEOLastCommentDate | LAST_COMMENT_DATE | — | — |
| 27 | ProjPlanLinePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | ProjPlanLinePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 29 | ProjPlanLinePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 30 | ProjPlanLinePEONumberOfExceptions | NUMBER_OF_EXCEPTIONS | — | — |
| 31 | ProjPlanLinePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 32 | ProjPlanLinePEOPercentComplete | PERCENT_COMPLETE | — | ✅ |
| 33 | ProjPlanLinePEOPersonId | PERSON_ID | — | — |
| 34 | ProjPlanLinePEOPhysicalPercentComplete | PHYSICAL_PERCENT_COMPLETE | — | ✅ |
| 35 | ProjPlanLinePEOPlanLineId | PLAN_LINE_ID | — | — |
| 36 | ProjPlanLinePEOPlanLineTypeCode | PLAN_LINE_TYPE_CODE | — | ✅ |
| 37 | ProjPlanLinePEOPlanVersionId | PLAN_VERSION_ID | — | — |
| 38 | ProjPlanLinePEOPmPlanProgressRef | PM_PLAN_PROGRESS_REF | — | — |
| 39 | ProjPlanLinePEOPmProductCode | PM_PRODUCT_CODE | — | — |
| 40 | ProjPlanLinePEOPriority | PRIORITY | — | ✅ |
| 41 | ProjPlanLinePEOProgressEnteredDate | PROGRESS_ENTERED_DATE | — | — |
| 42 | ProjPlanLinePEOProgressStatusCode | PROGRESS_STATUS_CODE | — | ✅ |
| 43 | ProjPlanLinePEOProjElementId | PROJ_ELEMENT_ID | — | ✅ |
| 44 | ProjPlanLinePEOProjectId | PROJECT_ID | — | ✅ |
| 45 | ProjPlanLinePEOProposedDuration | PROPOSED_DURATION | — | — |
| 46 | ProjPlanLinePEOProposedFinishDate | PROPOSED_FINISH_DATE | — | — |
| 47 | ProjPlanLinePEOProposedQuantity | PROPOSED_QUANTITY | — | — |
| 48 | ProjPlanLinePEOProposedResAllocation | PROPOSED_RES_ALLOCATION | — | — |
| 49 | ProjPlanLinePEOProposedStartDate | PROPOSED_START_DATE | — | — |
| 50 | ProjPlanLinePEOQuantity | QUANTITY | — | ✅ |
| 51 | ProjPlanLinePEORemainingExpenseCostAmount | REMAINING_EXPENSE_COST_AMOUNT | — | ✅ |
| 52 | ProjPlanLinePEORemainingLaborBilledAmount | REMAINING_LABOR_BILLED_AMOUNT | — | ✅ |
| 53 | ProjPlanLinePEORemainingLaborCostAmount | REMAINING_LABOR_COST_AMOUNT | — | ✅ |
| 54 | ProjPlanLinePEORemainingQuantity | REMAINING_QUANTITY | — | ✅ |
| 55 | ProjPlanLinePEOResourceAllocationPercent | RESOURCE_ALLOCATION_PERCENT | — | ✅ |
| 56 | ProjPlanLinePEOResourceId | RESOURCE_ID | — | — |
| 57 | ProjPlanLinePEORollupFlag | ROLLUP_FLAG | — | — |
| 58 | ProjPlanLinePEORollupPlanLine | ROLLUP_PLAN_LINE | — | — |
| 59 | ProjPlanLinePEOStartDate | START_DATE | — | ✅ |
| 60 | ProjPlanLinePEOTotalActualCostAmount | TOTAL_ACTUAL_COST_AMOUNT | — | ✅ |
| 61 | ProjPlanLinePEOTotalCostAmount | TOTAL_COST_AMOUNT | — | ✅ |
| 62 | ProjPlanLinePEOTotalRemainingCostAmount | TOTAL_REMAINING_COST_AMOUNT | — | ✅ |

### [[pjt_proj_ref_object_vl|PJT_PROJ_REF_OBJECT_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OpportunityAltNumber | OPPORTUNITY_ALT_NUMBER | — | — |
| 2 | OpportunityAmount | OPPORTUNITY_AMOUNT | — | — |
| 3 | OpportunityCurrencyCode | OPPORTUNITY_CURRENCY_CODE | — | — |
| 4 | OpportunityCustomerId | OPPORTUNITY_CUSTOMER_ID | — | — |
| 5 | OpportunityCustomerName | OPPORTUNITY_CUSTOMER_NAME | — | — |
| 6 | OpportunityCustomerNumber | OPPORTUNITY_CUSTOMER_NUMBER | — | — |
| 7 | OpportunityDescription | OPPORTUNITY_DESCRIPTION | — | — |
| 8 | OpportunityId | OPPORTUNITY_ID | — | — |
| 9 | OpportunityName | OPPORTUNITY_NAME | — | — |
| 10 | OpportunityNumber | OPPORTUNITY_NUMBER | — | — |
| 11 | OpportunityStatus | OPPORTUNITY_STATUS | — | — |
| 12 | OpportunityWinConfPercent | OPPORTUNITY_WIN_CONF_PERCENT | — | — |
| 13 | RefObjectId | REF_OBJECT_ID | — | — |
| 14 | RefObjectType | REF_OBJECT_TYPE | — | — |
| 15 | RefProjectId | REF_PROJECT_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
