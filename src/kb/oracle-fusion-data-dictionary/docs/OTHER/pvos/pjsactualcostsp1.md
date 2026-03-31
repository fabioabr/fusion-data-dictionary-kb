---
id: DOC-OTHER-PVO-PjsActualCostsP1
doc_type: system-doc
title: "PjsActualCostsP1 — PVO Cross-Module"
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
  - PjsActualCostsP1
  - pjsactualcostsp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PjsActualCostsP1

## 📌 Visão Geral

View Object para extração BICC de dados de Pjs Actual Costs P1. Acessa as tabelas: GL_LEDGERS, HR_ORGANIZATION_INFORMATION_F, PJF_BU_IMPL_ALL (+2).

**Caminho:** `FscmTopModelAM.PjsProjectPerformanceAM.PjsActualCostsP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 38 | 5 | 8 | 19 | 50% |

---

## 🔗 Tabelas Relacionadas

- [[gl_ledgers|GL_LEDGERS]] — 4 atributos
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 5 atributos
- [[pjf_bu_impl_all|PJF_BU_IMPL_ALL]] — 2 atributos
- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 3 atributos
- [[pjs_fp_base_fin|PJS_FP_BASE_FIN]] — 24 atributos (8 PKs, 19 BICC)

---

## ⚙️ Atributos

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlLedgersPEOAccPeriodType | ACCOUNTED_PERIOD_TYPE | — | — |
| 2 | GlLedgersPEOLedgerId | LEDGER_ID | — | — |
| 3 | GlLedgersPEOObjVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | GlLedgersPEOPeriodSetName | PERIOD_SET_NAME | — | — |

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BIImplOrgPEOPrimaryLedgerId | ORG_INFORMATION3 | — | — |
| 2 | OrgInfoPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | OrgInfoPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | OrgInfoPEOOrgInfoContext | ORG_INFORMATION_CONTEXT | — | — |
| 5 | OrgInfoPEOOrgInformationId | ORG_INFORMATION_ID | — | — |

### [[pjf_bu_impl_all|PJF_BU_IMPL_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BIImplOrgPEOObjVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | BIImplOrgPEOOrgId | ORG_ID | — | — |

### [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectPEOCarryingOutOrgId | CARRYING_OUT_ORGANIZATION_ID | — | — |
| 2 | ProjectPEOOrgId | ORG_ID | — | — |
| 3 | ProjectPEOProjectId | PROJECT_ID | — | — |

### [[pjs_fp_base_fin|PJS_FP_BASE_FIN]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActualCostPEOBillBrdnCost | BILL_BRDN_COST | — | ✅ |
| 2 | ActualCostPEOBillQuantity | BILL_QUANTITY | — | ✅ |
| 3 | ActualCostPEOBillRawCost | BILL_RAW_COST | — | ✅ |
| 4 | ActualCostPEOBrdnCost | BRDN_COST | — | ✅ |
| 5 | ActualCostPEOCalendarId | CALENDAR_ID | — | — |
| 6 | ActualCostPEOCapBrdnCost | CAP_BRDN_COST | — | ✅ |
| 7 | ActualCostPEOCapQuantity | CAP_QUANTITY | — | — |
| 8 | ActualCostPEOCapRawCost | CAP_RAW_COST | — | ✅ |
| 9 | ActualCostPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 10 | ActualCostPEOExpenseBrdnCost | EXPENSE_BRDN_COST | — | — |
| 11 | ActualCostPEOExpenseQuantity | EXPENSE_QUANTITY | — | — |
| 12 | ActualCostPEOExpenseRawCost | EXPENSE_RAW_COST | — | — |
| 13 | ActualCostPEOPeriodEndDate | END_DATE | — | ✅ |
| 14 | ActualCostPEOPeriodStartDate | START_DATE | — | ✅ |
| 15 | ActualCostPEOQuantity | QUANTITY | — | ✅ |
| 16 | ActualCostPEORawCost | RAW_COST | — | ✅ |
| 17 | CalendarType | CALENDAR_TYPE | 🔑 | ✅ |
| 18 | CurrencyType | CURRENCY_TYPE | 🔑 | ✅ |
| 19 | PeriodName | PERIOD_NAME | 🔑 | ✅ |
| 20 | ProjectId | PROJECT_ID | 🔑 | ✅ |
| 21 | ResourceClassId | RESOURCE_CLASS_ID | 🔑 | ✅ |
| 22 | TaskId | TASK_ID | 🔑 | ✅ |
| 23 | TxnAccumHeaderId | TXN_ACCUM_HEADER_ID | 🔑 | ✅ |
| 24 | UomCode | UOM_CODE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
