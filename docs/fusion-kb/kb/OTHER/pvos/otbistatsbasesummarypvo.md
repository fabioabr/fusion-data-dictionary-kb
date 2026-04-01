---
id: DOC-OTHER-PVO-OtbiStatsBaseSummaryPVO
doc_type: system-doc
title: "OtbiStatsBaseSummaryPVO — PVO Cross-Module"
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
  - OtbiStatsBaseSummaryPVO
  - otbistatsbasesummarypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OtbiStatsBaseSummaryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Otbi Stats Base Summary. Acessa as tabelas: EXM_EXPENSE_TYPES, EXM_OTBI_STATS_BASE_SUMMARY, FUN_BU_PERF_V (+1).

**Caminho:** `FscmTopModelAM.FinExmEntrySharedAM.OtbiStatsBaseSummaryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 85 | 4 | 2 | 27 | 32% |

---

## 🔗 Tabelas Relacionadas

- [[exm_expense_types|EXM_EXPENSE_TYPES]] — 27 atributos (1 BICC)
- [[exm_otbi_stats_base_summary|EXM_OTBI_STATS_BASE_SUMMARY]] — 43 atributos (1 PKs, 24 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 11 atributos (1 PKs, 2 BICC)
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 4 atributos

---

## ⚙️ Atributos

### [[exm_expense_types|EXM_EXPENSE_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenseTypePEOCategoryCode | CATEGORY_CODE | — | — |
| 2 | ExpenseTypePEOCcReceiptRequiredFlag | CC_RECEIPT_REQUIRED_FLAG | — | — |
| 3 | ExpenseTypePEOCcReceiptThreshold | CC_RECEIPT_THRESHOLD | — | — |
| 4 | ExpenseTypePEOCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 5 | ExpenseTypePEOCreatedBy | CREATED_BY | — | — |
| 6 | ExpenseTypePEOCreationDate | CREATION_DATE | — | — |
| 7 | ExpenseTypePEODefaultProjExpendType | DEFAULT_PROJ_EXPEND_TYPE | — | — |
| 8 | ExpenseTypePEODescription | DESCRIPTION | — | — |
| 9 | ExpenseTypePEODispRcptViolationFlag | DISP_RCPT_VIOLATION_FLAG | — | — |
| 10 | ExpenseTypePEOEnableProjectsFlag | ENABLE_PROJECTS_FLAG | — | — |
| 11 | ExpenseTypePEOEndDate | END_DATE | — | — |
| 12 | ExpenseTypePEOExpenseTemplateId | EXPENSE_TEMPLATE_ID | — | — |
| 13 | ExpenseTypePEOExpenseTypeId | EXPENSE_TYPE_ID | — | — |
| 14 | ExpenseTypePEOItemizationBehaviourCode | ITEMIZATION_BEHAVIOUR_CODE | — | — |
| 15 | ExpenseTypePEOItemizationOnlyFlag | ITEMIZATION_ONLY_FLAG | — | — |
| 16 | ExpenseTypePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 17 | ExpenseTypePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | ExpenseTypePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | ExpenseTypePEOName | NAME | — | ✅ |
| 20 | ExpenseTypePEONegativeRcptReqCode | NEGATIVE_RCPT_REQ_CODE | — | — |
| 21 | ExpenseTypePEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 22 | ExpenseTypePEOOrgId1 | ORG_ID | — | — |
| 23 | ExpenseTypePEORcptRequiredProjFlag | RCPT_REQUIRED_PROJ_FLAG | — | — |
| 24 | ExpenseTypePEOReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 25 | ExpenseTypePEOReceiptThreshold | RECEIPT_THRESHOLD | — | — |
| 26 | ExpenseTypePEOStartDate | START_DATE | — | — |
| 27 | ExpenseTypePEOTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |

### [[exm_otbi_stats_base_summary|EXM_OTBI_STATS_BASE_SUMMARY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentId | ASSIGNMENT_ID | — | — |
| 2 | CalMonth | CAL_MONTH | — | — |
| 3 | Company | COMPANY | — | ✅ |
| 4 | CostCenter | COST_CENTER | — | ✅ |
| 5 | CostCenterOwnerId | COST_CENTER_OWNER_ID | — | — |
| 6 | CreatedBy | CREATED_BY | — | — |
| 7 | CreationDate | CREATION_DATE | — | — |
| 8 | ExpenseCategoryCode | EXPENSE_CATEGORY_CODE | — | ✅ |
| 9 | ExpenseLocationCity | EXPENSE_LOCATION_CITY | — | ✅ |
| 10 | ExpenseLocationCountry | EXPENSE_LOCATION_COUNTRY | — | ✅ |
| 11 | ExpenseLocationState | EXPENSE_LOCATION_STATE | — | ✅ |
| 12 | ExpenseReportTotal | EXPENSE_REPORT_TOTAL | — | — |
| 13 | ExpenseStatusCode | EXPENSE_STATUS_CODE | — | ✅ |
| 14 | ExpenseTotal | EXPENSE_TOTAL | — | ✅ |
| 15 | ExpenseTypeCategoryCode | EXPENSE_TYPE_CATEGORY_CODE | — | ✅ |
| 16 | ExpenseTypeId | EXPENSE_TYPE_ID | — | ✅ |
| 17 | ExpenseViolationTotal | EXPENSE_VIOLATION_TOTAL | — | ✅ |
| 18 | FunctionalCurrencyCode | FUNCTIONAL_CURRENCY_CODE | — | — |
| 19 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 22 | LegalEntityId | LEGAL_ENTITY_ID | — | — |
| 23 | MerchantName | MERCHANT_NAME | — | ✅ |
| 24 | MonthNum | MONTH_NUM | — | — |
| 25 | NumAgingBucket1 | NUM_AGING_BUCKET_1 | — | ✅ |
| 26 | NumAgingBucket2 | NUM_AGING_BUCKET_2 | — | ✅ |
| 27 | NumAgingBucket3 | NUM_AGING_BUCKET_3 | — | ✅ |
| 28 | NumExpenseReports | NUM_EXPENSE_REPORTS | — | ✅ |
| 29 | NumExpenseViolations | NUM_EXPENSE_VIOLATIONS | — | ✅ |
| 30 | NumExpenses | NUM_EXPENSES | — | ✅ |
| 31 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 32 | OrgId | ORG_ID | — | — |
| 33 | OtbiStatsBaseSummaryId | OTBI_STATS_BASE_SUMMARY_ID | 🔑 | ✅ |
| 34 | PersonId | PERSON_ID | — | — |
| 35 | PersonLocationId | PERSON_LOCATION_ID | — | — |
| 36 | PjcProjectId | PJC_PROJECT_ID | — | — |
| 37 | PjcTaskId | PJC_TASK_ID | — | — |
| 38 | SupervisorId | SUPERVISOR_ID | — | — |
| 39 | TotalAgingBucket1 | TOTAL_AGING_BUCKET_1 | — | ✅ |
| 40 | TotalAgingBucket2 | TOTAL_AGING_BUCKET_2 | — | ✅ |
| 41 | TotalAgingBucket3 | TOTAL_AGING_BUCKET_3 | — | ✅ |
| 42 | ViolationTypeCode | VIOLATION_TYPE_CODE | — | ✅ |
| 43 | YearNum | YEAR_NUM | — | — |

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUBusinessUnitId | BU_ID | 🔑 | ✅ |
| 2 | BUCreatedBy | CREATED_BY | — | — |
| 3 | BUCreationDate | CREATION_DATE | — | — |
| 4 | BUDateFrom | DATE_FROM | — | — |
| 5 | BUDateTo | DATE_TO | — | — |
| 6 | BUEnterpriseId | BUSINESS_GROUP_ID | — | — |
| 7 | BULastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | BULastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | BULastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | BUName | BU_NAME | — | — |
| 11 | BUStatus | STATUS | — | — |

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUPrimaryLedgerId | ORG_INFORMATION3 | — | — |
| 2 | OrgInfoEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | OrgInfoEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | OrgInfoOrgInformationId | ORG_INFORMATION_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
