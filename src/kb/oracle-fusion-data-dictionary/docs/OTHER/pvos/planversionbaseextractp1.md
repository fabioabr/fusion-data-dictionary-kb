---
id: DOC-OTHER-PVO-PlanVersionBaseExtractP1
doc_type: system-doc
title: "PlanVersionBaseExtractP1 — PVO Cross-Module"
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
  - PlanVersionBaseExtractP1
  - planversionbaseextractp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlanVersionBaseExtractP1

## 📌 Visão Geral

View Object para extração BICC de dados de Plan Version Base Extract P1. Acessa as tabelas: PJO_PLAN_VERSIONS_B, PJO_PLAN_VERSIONS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjoBiccExtractAM.PlanVersionBaseExtractP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 59 | 2 | 1 | 59 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjo_plan_versions_b|PJO_PLAN_VERSIONS_B]] — 48 atributos (1 PKs, 48 BICC)
- [[pjo_plan_versions_tl|PJO_PLAN_VERSIONS_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[pjo_plan_versions_b|PJO_PLAN_VERSIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlanVersionBasePEOActualAmtsThruPeriod | ACTUAL_AMTS_THRU_PERIOD | — | ✅ |
| 2 | PlanVersionBasePEOBaselinedByPersonId | BASELINED_BY_PERSON_ID | — | ✅ |
| 3 | PlanVersionBasePEOBaselinedDate | BASELINED_DATE | — | ✅ |
| 4 | PlanVersionBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | PlanVersionBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | PlanVersionBasePEOCurrentPlanStatusFlag | CURRENT_PLAN_STATUS_FLAG | — | ✅ |
| 7 | PlanVersionBasePEOEquipmentQuantity | EQUIPMENT_QUANTITY | — | ✅ |
| 8 | PlanVersionBasePEOEtcStartDate | ETC_START_DATE | — | ✅ |
| 9 | PlanVersionBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 10 | PlanVersionBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 11 | PlanVersionBasePEOLastAmtGenDate | LAST_AMT_GEN_DATE | — | ✅ |
| 12 | PlanVersionBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | PlanVersionBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | PlanVersionBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | PlanVersionBasePEOLockedByPersonId | LOCKED_BY_PERSON_ID | — | ✅ |
| 16 | PlanVersionBasePEOMultiErrorFlag | MULTI_ERROR_FLAG | — | ✅ |
| 17 | PlanVersionBasePEOObjectId1 | OBJECT_ID1 | — | ✅ |
| 18 | PlanVersionBasePEOObjectTypeCode | OBJECT_TYPE_CODE | — | ✅ |
| 19 | PlanVersionBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 20 | PlanVersionBasePEOOriginalFlag | ORIGINAL_FLAG | — | ✅ |
| 21 | PlanVersionBasePEOPeopleQuantity | PEOPLE_QUANTITY | — | ✅ |
| 22 | PlanVersionBasePEOPfcBrdndCost | PFC_BRDND_COST | — | ✅ |
| 23 | PlanVersionBasePEOPfcRawCost | PFC_RAW_COST | — | ✅ |
| 24 | PlanVersionBasePEOPfcRevenue | PFC_REVENUE | — | ✅ |
| 25 | PlanVersionBasePEOPjiSummarizedFlag | PJI_SUMMARIZED_FLAG | — | ✅ |
| 26 | PlanVersionBasePEOPjsSummaryId | PJS_SUMMARY_ID | — | ✅ |
| 27 | PlanVersionBasePEOPlanClassCode | PLAN_CLASS_CODE | — | ✅ |
| 28 | PlanVersionBasePEOPlanProcessStatusCode | PLAN_PROCESS_STATUS_CODE | — | ✅ |
| 29 | PlanVersionBasePEOPlanProcessingCode | PLAN_PROCESSING_CODE | — | ✅ |
| 30 | PlanVersionBasePEOPlanRunDate | PLAN_RUN_DATE | — | ✅ |
| 31 | PlanVersionBasePEOPlanStatusCode | PLAN_STATUS_CODE | — | ✅ |
| 32 | PlanVersionBasePEOPlanTypeId | PLAN_TYPE_ID | — | ✅ |
| 33 | PlanVersionBasePEOPlanVersionId | PLAN_VERSION_ID | 🔑 | ✅ |
| 34 | PlanVersionBasePEOPlannedForCode | PLANNED_FOR_CODE | — | ✅ |
| 35 | PlanVersionBasePEOPmBudgetReference | PM_BUDGET_REFERENCE | — | ✅ |
| 36 | PlanVersionBasePEOPmProductCode | PM_PRODUCT_CODE | — | ✅ |
| 37 | PlanVersionBasePEOProjectId | PROJECT_ID | — | ✅ |
| 38 | PlanVersionBasePEORejectedBy | REJECTED_BY | — | ✅ |
| 39 | PlanVersionBasePEORejectionDate | REJECTION_DATE | — | ✅ |
| 40 | PlanVersionBasePEORequestId | REQUEST_ID | — | ✅ |
| 41 | PlanVersionBasePEOStructureVersionId | STRUCTURE_VERSION_ID | — | ✅ |
| 42 | PlanVersionBasePEOSubmittedBy | SUBMITTED_BY | — | ✅ |
| 43 | PlanVersionBasePEOSubmittedDate | SUBMITTED_DATE | — | ✅ |
| 44 | PlanVersionBasePEOTotalPcBrdndCost | TOTAL_PC_BRDND_COST | — | ✅ |
| 45 | PlanVersionBasePEOTotalPcRawCost | TOTAL_PC_RAW_COST | — | ✅ |
| 46 | PlanVersionBasePEOTotalPcRevenue | TOTAL_PC_REVENUE | — | ✅ |
| 47 | PlanVersionBasePEOVersionNumber | VERSION_NUMBER | — | ✅ |
| 48 | PlanVersionBasePEOWfStatusCode | WF_STATUS_CODE | — | ✅ |

### [[pjo_plan_versions_tl|PJO_PLAN_VERSIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlanVersionTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PlanVersionTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PlanVersionTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | PlanVersionTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 5 | PlanVersionTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PlanVersionTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | PlanVersionTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | PlanVersionTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | PlanVersionTranslationPEOPlanVersionId | PLAN_VERSION_ID | — | ✅ |
| 10 | PlanVersionTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |
| 11 | PlanVersionTranslationPEOVersionName | VERSION_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
