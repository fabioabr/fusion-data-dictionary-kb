---
id: DOC-OTHER-PVO-ActualHoursPVO
doc_type: system-doc
title: "ActualHoursPVO — PVO Cross-Module"
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
  - ActualHoursPVO
  - actualhourspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ActualHoursPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Actual Hours. Acessa as tabelas: PJF_PROJECTS_ALL_B, PJR_ACTUAL_HOURS.

**Caminho:** `FscmTopModelAM.PjrReportingAM.ActualHoursPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 2 | 1 | 11 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 4 atributos
- [[pjr_actual_hours|PJR_ACTUAL_HOURS]] — 21 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectBasePEOCarryingOutOrganizationId | CARRYING_OUT_ORGANIZATION_ID | — | — |
| 2 | ProjectBasePEOOrgId | ORG_ID | — | — |
| 3 | ProjectBasePEOProjectId | PROJECT_ID | — | — |
| 4 | ProjectBasePEOProjectUnitId | PROJECT_UNIT_ID | — | — |

### [[pjr_actual_hours|PJR_ACTUAL_HOURS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActualHoursPEOActualHoursWkCategoryCode | ACTUAL_HOURS_WK_CATEGORY_CODE | — | — |
| 2 | ActualHoursPEOAdjustedTransactionRef | ADJUSTED_TRANSACTION_REF | — | ✅ |
| 3 | ActualHoursPEOAdjustmentFlag | ADJUSTMENT_FLAG | — | ✅ |
| 4 | ActualHoursPEOBillingFlag | BILLING_FLAG | — | ✅ |
| 5 | ActualHoursPEOComments | COMMENTS | — | ✅ |
| 6 | ActualHoursPEOCreatedBy | CREATED_BY | — | — |
| 7 | ActualHoursPEOCreationDate | CREATION_DATE | — | — |
| 8 | ActualHoursPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 9 | ActualHoursPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | ActualHoursPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | ActualHoursPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | ActualHoursPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | ActualHoursPEOOrgnalTransactionRef | ORGNAL_TRANSACTION_REF | — | ✅ |
| 14 | ActualHoursPEOProjectId | PROJECT_ID | — | — |
| 15 | ActualHoursPEOQuantity | QUANTITY | — | ✅ |
| 16 | ActualHoursPEOResourceId | RESOURCE_ID | — | — |
| 17 | ActualHoursPEOTaskId | TASK_ID | — | — |
| 18 | ActualHoursPEOUtilizationDate | UTILIZATION_DATE | — | ✅ |
| 19 | ActualHoursPEOUtilizationFlag | UTILIZATION_FLAG | — | ✅ |
| 20 | ActualHoursPEOWorkDate | WORK_DATE | — | ✅ |
| 21 | TransactionId | TRANSACTION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
