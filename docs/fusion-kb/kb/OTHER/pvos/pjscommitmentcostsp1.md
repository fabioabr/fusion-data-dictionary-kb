---
id: DOC-OTHER-PVO-PjsCommitmentCostsP1
doc_type: system-doc
title: "PjsCommitmentCostsP1 — PVO Cross-Module"
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
  - PjsCommitmentCostsP1
  - pjscommitmentcostsp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PjsCommitmentCostsP1

## 📌 Visão Geral

View Object para extração BICC de dados de Pjs Commitment Costs P1. Acessa as tabelas: GL_LEDGERS, HR_ORGANIZATION_INFORMATION_F, PJF_BU_IMPL_ALL (+2).

**Caminho:** `FscmTopModelAM.PjsProjectPerformanceAM.PjsCommitmentCostsP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 44 | 5 | 8 | 21 | 48% |

---

## 🔗 Tabelas Relacionadas

- [[gl_ledgers|GL_LEDGERS]] — 4 atributos
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 5 atributos
- [[pjf_bu_impl_all|PJF_BU_IMPL_ALL]] — 2 atributos
- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 3 atributos
- [[pjs_fp_base_cmt|PJS_FP_BASE_CMT]] — 30 atributos (8 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlLedgerPEOAccPeriodType | ACCOUNTED_PERIOD_TYPE | — | — |
| 2 | GlLedgerPEOLedgerId | LEDGER_ID | — | — |
| 3 | GlLedgerPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | GlLedgerPEOPeriodSetName | PERIOD_SET_NAME | — | — |

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUImplOrgPEOPrimaryLedgerId | ORG_INFORMATION3 | — | — |
| 2 | OrgInfoPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | OrgInfoPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | OrgInfoPEOOrgInfoContext | ORG_INFORMATION_CONTEXT | — | — |
| 5 | OrgInfoPEOOrgInformationId | ORG_INFORMATION_ID | — | — |

### [[pjf_bu_impl_all|PJF_BU_IMPL_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUImplOrgPEOObjVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | BUImplOrgPEOOrgId | ORG_ID | — | — |

### [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectBasePEOCarryingOutOrgId | CARRYING_OUT_ORGANIZATION_ID | — | — |
| 2 | ProjectBasePEOOrgId | ORG_ID | — | — |
| 3 | ProjectBasePEOProjectId | PROJECT_ID | — | — |

### [[pjs_fp_base_cmt|PJS_FP_BASE_CMT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CalendarType | CALENDAR_TYPE | 🔑 | ✅ |
| 2 | CmtCostPEOCalendarId | CALENDAR_ID | — | — |
| 3 | CmtCostPEOCmtOthQuantity | CMT_OTH_QUANTITY | — | — |
| 4 | CmtCostPEOCmtPoQuantity | CMT_PO_QUANTITY | — | — |
| 5 | CmtCostPEOCmtPrQuantity | CMT_PR_QUANTITY | — | — |
| 6 | CmtCostPEOCmtSIQuantity | CMT_SUP_INV_QUANTITY | — | — |
| 7 | CmtCostPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 8 | CmtCostPEOOthCmtBrdnCost | OTH_CMT_BRDN_COST | — | ✅ |
| 9 | CmtCostPEOOthCmtRawCost | OTH_CMT_RAW_COST | — | ✅ |
| 10 | CmtCostPEOPeriodEndDate | END_DATE | — | ✅ |
| 11 | CmtCostPEOPeriodStartDate | START_DATE | — | ✅ |
| 12 | CmtCostPEOPoCmtBrdnCost | PO_CMT_BRDN_COST | — | ✅ |
| 13 | CmtCostPEOPoCmtRawCost | PO_CMT_RAW_COST | — | ✅ |
| 14 | CmtCostPEOPrCmtBrdnCost | PR_CMT_BRDN_COST | — | ✅ |
| 15 | CmtCostPEOPrCmtRawCost | PR_CMT_RAW_COST | — | ✅ |
| 16 | CmtCostPEOSICmtBrdnCost | SUP_INV_CMT_BRDN_COST | — | ✅ |
| 17 | CmtCostPEOSICmtRawCost | SUP_INV_CMT_RAW_COST | — | ✅ |
| 18 | CmtCostPEOToCmtBrdnCost | TO_CMT_BRDN_COST | — | ✅ |
| 19 | CmtCostPEOToCmtQuantity | TO_CMT_QUANTITY | — | — |
| 20 | CmtCostPEOToCmtRawCost | TO_CMT_RAW_COST | — | ✅ |
| 21 | CmtCostPEOTtlCmtBrdnCost | TTL_CMT_BRDN_COST | — | — |
| 22 | CmtCostPEOTtlCmtQuantity | TTL_CMT_QUANTITY | — | — |
| 23 | CmtCostPEOTtlCmtRawCost | TTL_CMT_RAW_COST | — | — |
| 24 | CurrencyType | CURRENCY_TYPE | 🔑 | ✅ |
| 25 | PeriodName | PERIOD_NAME | 🔑 | ✅ |
| 26 | ProjectId | PROJECT_ID | 🔑 | ✅ |
| 27 | ResourceClassId | RESOURCE_CLASS_ID | 🔑 | ✅ |
| 28 | TaskId | TASK_ID | 🔑 | ✅ |
| 29 | TxnAccumHeaderId | TXN_ACCUM_HEADER_ID | 🔑 | ✅ |
| 30 | UomCode | UOM_CODE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
