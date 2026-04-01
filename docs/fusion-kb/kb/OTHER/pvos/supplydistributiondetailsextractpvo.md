---
id: DOC-OTHER-PVO-SupplyDistributionDetailsExtractPVO
doc_type: system-doc
title: "SupplyDistributionDetailsExtractPVO — PVO Cross-Module"
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
  - SupplyDistributionDetailsExtractPVO
  - supplydistributiondetailsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplyDistributionDetailsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Supply Distribution Details Extract. Acessa as tabelas: DOS_DISTRIBUTION_DETAILS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DosBiccExtractAM.SupplyDistributionDetailsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 78 | 1 | 1 | 78 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[dos_distribution_details|DOS_DISTRIBUTION_DETAILS]] — 78 atributos (1 PKs, 78 BICC)

---

## ⚙️ Atributos

### [[dos_distribution_details|DOS_DISTRIBUTION_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DosDistributionDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | DosDistributionDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | DosDistributionDetailsPEODetailType | DETAIL_TYPE | — | ✅ |
| 4 | DosDistributionDetailsPEODistrbAmount | DISTRB_AMOUNT | — | ✅ |
| 5 | DosDistributionDetailsPEODistrbAmountCurrencyCode | DISTRB_AMOUNT_CURRENCY_CODE | — | ✅ |
| 6 | DosDistributionDetailsPEODistrbBudgetDate | DISTRB_BUDGET_DATE | — | ✅ |
| 7 | DosDistributionDetailsPEODistrbChargeAccountId | DISTRB_CHARGE_ACCOUNT_ID | — | ✅ |
| 8 | DosDistributionDetailsPEODistrbCurramtCurrencyCode | DISTRB_CURRAMT_CURRENCY_CODE | — | ✅ |
| 9 | DosDistributionDetailsPEODistrbCurrencyAmount | DISTRB_CURRENCY_AMOUNT | — | ✅ |
| 10 | DosDistributionDetailsPEODistrbDeliveredQuantity | DISTRB_DELIVERED_QUANTITY | — | ✅ |
| 11 | DosDistributionDetailsPEODistrbDelvrdQuantityUom | DISTRB_DELVRD_QUANTITY_UOM | — | ✅ |
| 12 | DosDistributionDetailsPEODistrbFundsStatus | DISTRB_FUNDS_STATUS | — | ✅ |
| 13 | DosDistributionDetailsPEODistrbNonrcvrblCrncyTax | DISTRB_NONRCVRBL_CRNCY_TAX | — | ✅ |
| 14 | DosDistributionDetailsPEODistrbNonrecoverableTax | DISTRB_NONRECOVERABLE_TAX | — | ✅ |
| 15 | DosDistributionDetailsPEODistrbPercent | DISTRB_PERCENT | — | ✅ |
| 16 | DosDistributionDetailsPEODistrbPrimaryLedgerId | DISTRB_PRIMARY_LEDGER_ID | — | ✅ |
| 17 | DosDistributionDetailsPEODistrbPropamtCurrencyCode | DISTRB_PROPAMT_CURRENCY_CODE | — | ✅ |
| 18 | DosDistributionDetailsPEODistrbProposedAmount | DISTRB_PROPOSED_AMOUNT | — | ✅ |
| 19 | DosDistributionDetailsPEODistrbProposedChrgAccntId | DISTRB_PROPOSED_CHRG_ACCNT_ID | — | ✅ |
| 20 | DosDistributionDetailsPEODistrbProposedPercent | DISTRB_PROPOSED_PERCENT | — | ✅ |
| 21 | DosDistributionDetailsPEODistrbProposedProjectId | DISTRB_PROPOSED_PROJECT_ID | — | ✅ |
| 22 | DosDistributionDetailsPEODistrbProposedQuantity | DISTRB_PROPOSED_QUANTITY | — | ✅ |
| 23 | DosDistributionDetailsPEODistrbProposedQuantityUom | DISTRB_PROPOSED_QUANTITY_UOM | — | ✅ |
| 24 | DosDistributionDetailsPEODistrbProposedTaskId | DISTRB_PROPOSED_TASK_ID | — | ✅ |
| 25 | DosDistributionDetailsPEODistrbQuantity | DISTRB_QUANTITY | — | ✅ |
| 26 | DosDistributionDetailsPEODistrbQuantityUom | DISTRB_QUANTITY_UOM | — | ✅ |
| 27 | DosDistributionDetailsPEODistrbRecoverableCrncyTax | DISTRB_RECOVERABLE_CRNCY_TAX | — | ✅ |
| 28 | DosDistributionDetailsPEODistrbRecoverableTax | DISTRB_RECOVERABLE_TAX | — | ✅ |
| 29 | DosDistributionDetailsPEODistrbRequestingBuId | DISTRB_REQUESTING_BU_ID | — | ✅ |
| 30 | DosDistributionDetailsPEODistrbRequisitionLineId | DISTRB_REQUISITION_LINE_ID | — | ✅ |
| 31 | DosDistributionDetailsPEODistributionDetailsId | DISTRIBUTION_DETAILS_ID | 🔑 | ✅ |
| 32 | DosDistributionDetailsPEODistributionId | DISTRIBUTION_ID | — | ✅ |
| 33 | DosDistributionDetailsPEODistributionNumber | DISTRIBUTION_NUMBER | — | ✅ |
| 34 | DosDistributionDetailsPEODistributionOperation | DISTRIBUTION_OPERATION | — | ✅ |
| 35 | DosDistributionDetailsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 36 | DosDistributionDetailsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 37 | DosDistributionDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 38 | DosDistributionDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 39 | DosDistributionDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 40 | DosDistributionDetailsPEOLineId | LINE_ID | — | ✅ |
| 41 | DosDistributionDetailsPEOLoadRequestId | LOAD_REQUEST_ID | — | ✅ |
| 42 | DosDistributionDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 43 | DosDistributionDetailsPEOPjcBillableFlag | PJC_BILLABLE_FLAG | — | ✅ |
| 44 | DosDistributionDetailsPEOPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | ✅ |
| 45 | DosDistributionDetailsPEOPjcContextCategory | PJC_CONTEXT_CATEGORY | — | ✅ |
| 46 | DosDistributionDetailsPEOPjcContractId | PJC_CONTRACT_ID | — | ✅ |
| 47 | DosDistributionDetailsPEOPjcContractLineId | PJC_CONTRACT_LINE_ID | — | ✅ |
| 48 | DosDistributionDetailsPEOPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | ✅ |
| 49 | DosDistributionDetailsPEOPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | ✅ |
| 50 | DosDistributionDetailsPEOPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | ✅ |
| 51 | DosDistributionDetailsPEOPjcOrganizationId | PJC_ORGANIZATION_ID | — | ✅ |
| 52 | DosDistributionDetailsPEOPjcProjectId | PJC_PROJECT_ID | — | ✅ |
| 53 | DosDistributionDetailsPEOPjcProjectNumber | PJC_PROJECT_NUMBER | — | ✅ |
| 54 | DosDistributionDetailsPEOPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | ✅ |
| 55 | DosDistributionDetailsPEOPjcReservedAttribute10 | PJC_RESERVED_ATTRIBUTE10 | — | ✅ |
| 56 | DosDistributionDetailsPEOPjcReservedAttribute2 | PJC_RESERVED_ATTRIBUTE2 | — | ✅ |
| 57 | DosDistributionDetailsPEOPjcReservedAttribute3 | PJC_RESERVED_ATTRIBUTE3 | — | ✅ |
| 58 | DosDistributionDetailsPEOPjcReservedAttribute4 | PJC_RESERVED_ATTRIBUTE4 | — | ✅ |
| 59 | DosDistributionDetailsPEOPjcReservedAttribute5 | PJC_RESERVED_ATTRIBUTE5 | — | ✅ |
| 60 | DosDistributionDetailsPEOPjcReservedAttribute6 | PJC_RESERVED_ATTRIBUTE6 | — | ✅ |
| 61 | DosDistributionDetailsPEOPjcReservedAttribute7 | PJC_RESERVED_ATTRIBUTE7 | — | ✅ |
| 62 | DosDistributionDetailsPEOPjcReservedAttribute8 | PJC_RESERVED_ATTRIBUTE8 | — | ✅ |
| 63 | DosDistributionDetailsPEOPjcReservedAttribute9 | PJC_RESERVED_ATTRIBUTE9 | — | ✅ |
| 64 | DosDistributionDetailsPEOPjcTaskId | PJC_TASK_ID | — | ✅ |
| 65 | DosDistributionDetailsPEOPjcTaskNumber | PJC_TASK_NUMBER | — | ✅ |
| 66 | DosDistributionDetailsPEOPjcUserDefAttribute1 | PJC_USER_DEF_ATTRIBUTE1 | — | ✅ |
| 67 | DosDistributionDetailsPEOPjcUserDefAttribute10 | PJC_USER_DEF_ATTRIBUTE10 | — | ✅ |
| 68 | DosDistributionDetailsPEOPjcUserDefAttribute2 | PJC_USER_DEF_ATTRIBUTE2 | — | ✅ |
| 69 | DosDistributionDetailsPEOPjcUserDefAttribute3 | PJC_USER_DEF_ATTRIBUTE3 | — | ✅ |
| 70 | DosDistributionDetailsPEOPjcUserDefAttribute4 | PJC_USER_DEF_ATTRIBUTE4 | — | ✅ |
| 71 | DosDistributionDetailsPEOPjcUserDefAttribute5 | PJC_USER_DEF_ATTRIBUTE5 | — | ✅ |
| 72 | DosDistributionDetailsPEOPjcUserDefAttribute6 | PJC_USER_DEF_ATTRIBUTE6 | — | ✅ |
| 73 | DosDistributionDetailsPEOPjcUserDefAttribute7 | PJC_USER_DEF_ATTRIBUTE7 | — | ✅ |
| 74 | DosDistributionDetailsPEOPjcUserDefAttribute8 | PJC_USER_DEF_ATTRIBUTE8 | — | ✅ |
| 75 | DosDistributionDetailsPEOPjcUserDefAttribute9 | PJC_USER_DEF_ATTRIBUTE9 | — | ✅ |
| 76 | DosDistributionDetailsPEOPjcWorkTypeId | PJC_WORK_TYPE_ID | — | ✅ |
| 77 | DosDistributionDetailsPEORequestId | REQUEST_ID | — | ✅ |
| 78 | DosDistributionDetailsPEOTrackingLineId | TRACKING_LINE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
