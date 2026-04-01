---
id: DOC-OTHER-PVO-SupplyRequestDistrbDtlsExtractPVO
doc_type: system-doc
title: "SupplyRequestDistrbDtlsExtractPVO — PVO Cross-Module"
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
  - SupplyRequestDistrbDtlsExtractPVO
  - supplyrequestdistrbdtlsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplyRequestDistrbDtlsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Supply Request Distrb Dtls Extract. Acessa as tabelas: DOS_DISTRIBUTION_DETAILS_INT.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DosBiccExtractAM.SupplyRequestDistrbDtlsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 111 | 1 | 1 | 111 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[dos_distribution_details_int|DOS_DISTRIBUTION_DETAILS_INT]] — 111 atributos (1 PKs, 111 BICC)

---

## ⚙️ Atributos

### [[dos_distribution_details_int|DOS_DISTRIBUTION_DETAILS_INT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DosDistributionDetailsIntPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | DosDistributionDetailsIntPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | DosDistributionDetailsIntPEODetailType | DETAIL_TYPE | — | ✅ |
| 4 | DosDistributionDetailsIntPEODistrbAmount | DISTRB_AMOUNT | — | ✅ |
| 5 | DosDistributionDetailsIntPEODistrbAmountCurrencyCode | DISTRB_AMOUNT_CURRENCY_CODE | — | ✅ |
| 6 | DosDistributionDetailsIntPEODistrbBudgetDate | DISTRB_BUDGET_DATE | — | ✅ |
| 7 | DosDistributionDetailsIntPEODistrbChargeAccountId | DISTRB_CHARGE_ACCOUNT_ID | — | ✅ |
| 8 | DosDistributionDetailsIntPEODistrbCurramtCurrencyCode | DISTRB_CURRAMT_CURRENCY_CODE | — | ✅ |
| 9 | DosDistributionDetailsIntPEODistrbCurrencyAmount | DISTRB_CURRENCY_AMOUNT | — | ✅ |
| 10 | DosDistributionDetailsIntPEODistrbDeliveredQuantity | DISTRB_DELIVERED_QUANTITY | — | ✅ |
| 11 | DosDistributionDetailsIntPEODistrbDelvrdQuantityUom | DISTRB_DELVRD_QUANTITY_UOM | — | ✅ |
| 12 | DosDistributionDetailsIntPEODistrbExpenditureDate | DISTRB_EXPENDITURE_DATE | — | ✅ |
| 13 | DosDistributionDetailsIntPEODistrbExpenditureOrgId | DISTRB_EXPENDITURE_ORG_ID | — | ✅ |
| 14 | DosDistributionDetailsIntPEODistrbExpenditureTypeId | DISTRB_EXPENDITURE_TYPE_ID | — | ✅ |
| 15 | DosDistributionDetailsIntPEODistrbFundsStatus | DISTRB_FUNDS_STATUS | — | ✅ |
| 16 | DosDistributionDetailsIntPEODistrbNonrcvrblCrncyTax | DISTRB_NONRCVRBL_CRNCY_TAX | — | ✅ |
| 17 | DosDistributionDetailsIntPEODistrbNonrecoverableTax | DISTRB_NONRECOVERABLE_TAX | — | ✅ |
| 18 | DosDistributionDetailsIntPEODistrbPercent | DISTRB_PERCENT | — | ✅ |
| 19 | DosDistributionDetailsIntPEODistrbPjcBillableFlag | DISTRB_PJC_BILLABLE_FLAG | — | ✅ |
| 20 | DosDistributionDetailsIntPEODistrbPjcCapitalizableFlag | DISTRB_PJC_CAPITALIZABLE_FLAG | — | ✅ |
| 21 | DosDistributionDetailsIntPEODistrbPjcContextCategory | DISTRB_PJC_CONTEXT_CATEGORY | — | ✅ |
| 22 | DosDistributionDetailsIntPEODistrbPjcContractId | DISTRB_PJC_CONTRACT_ID | — | ✅ |
| 23 | DosDistributionDetailsIntPEODistrbPjcContractLineId | DISTRB_PJC_CONTRACT_LINE_ID | — | ✅ |
| 24 | DosDistributionDetailsIntPEODistrbPjcFndingAllctnId | DISTRB_PJC_FNDING_ALLCTN_ID | — | ✅ |
| 25 | DosDistributionDetailsIntPEODistrbPjcRsrvdAttribute1 | DISTRB_PJC_RSRVD_ATTRIBUTE1 | — | ✅ |
| 26 | DosDistributionDetailsIntPEODistrbPjcRsrvdAttribute10 | DISTRB_PJC_RSRVD_ATTRIBUTE10 | — | ✅ |
| 27 | DosDistributionDetailsIntPEODistrbPjcRsrvdAttribute2 | DISTRB_PJC_RSRVD_ATTRIBUTE2 | — | ✅ |
| 28 | DosDistributionDetailsIntPEODistrbPjcRsrvdAttribute3 | DISTRB_PJC_RSRVD_ATTRIBUTE3 | — | ✅ |
| 29 | DosDistributionDetailsIntPEODistrbPjcRsrvdAttribute4 | DISTRB_PJC_RSRVD_ATTRIBUTE4 | — | ✅ |
| 30 | DosDistributionDetailsIntPEODistrbPjcRsrvdAttribute5 | DISTRB_PJC_RSRVD_ATTRIBUTE5 | — | ✅ |
| 31 | DosDistributionDetailsIntPEODistrbPjcRsrvdAttribute6 | DISTRB_PJC_RSRVD_ATTRIBUTE6 | — | ✅ |
| 32 | DosDistributionDetailsIntPEODistrbPjcRsrvdAttribute7 | DISTRB_PJC_RSRVD_ATTRIBUTE7 | — | ✅ |
| 33 | DosDistributionDetailsIntPEODistrbPjcRsrvdAttribute8 | DISTRB_PJC_RSRVD_ATTRIBUTE8 | — | ✅ |
| 34 | DosDistributionDetailsIntPEODistrbPjcRsrvdAttribute9 | DISTRB_PJC_RSRVD_ATTRIBUTE9 | — | ✅ |
| 35 | DosDistributionDetailsIntPEODistrbPjcUsrDefAttribute1 | DISTRB_PJC_USR_DEF_ATTRIBUTE1 | — | ✅ |
| 36 | DosDistributionDetailsIntPEODistrbPjcUsrDefAttribute10 | DISTRB_PJC_USR_DEF_ATTRIBUTE10 | — | ✅ |
| 37 | DosDistributionDetailsIntPEODistrbPjcUsrDefAttribute2 | DISTRB_PJC_USR_DEF_ATTRIBUTE2 | — | ✅ |
| 38 | DosDistributionDetailsIntPEODistrbPjcUsrDefAttribute3 | DISTRB_PJC_USR_DEF_ATTRIBUTE3 | — | ✅ |
| 39 | DosDistributionDetailsIntPEODistrbPjcUsrDefAttribute4 | DISTRB_PJC_USR_DEF_ATTRIBUTE4 | — | ✅ |
| 40 | DosDistributionDetailsIntPEODistrbPjcUsrDefAttribute5 | DISTRB_PJC_USR_DEF_ATTRIBUTE5 | — | ✅ |
| 41 | DosDistributionDetailsIntPEODistrbPjcUsrDefAttribute6 | DISTRB_PJC_USR_DEF_ATTRIBUTE6 | — | ✅ |
| 42 | DosDistributionDetailsIntPEODistrbPjcUsrDefAttribute7 | DISTRB_PJC_USR_DEF_ATTRIBUTE7 | — | ✅ |
| 43 | DosDistributionDetailsIntPEODistrbPjcUsrDefAttribute8 | DISTRB_PJC_USR_DEF_ATTRIBUTE8 | — | ✅ |
| 44 | DosDistributionDetailsIntPEODistrbPjcUsrDefAttribute9 | DISTRB_PJC_USR_DEF_ATTRIBUTE9 | — | ✅ |
| 45 | DosDistributionDetailsIntPEODistrbPjcWorkTypeId | DISTRB_PJC_WORK_TYPE_ID | — | ✅ |
| 46 | DosDistributionDetailsIntPEODistrbPrimaryLedgerId | DISTRB_PRIMARY_LEDGER_ID | — | ✅ |
| 47 | DosDistributionDetailsIntPEODistrbProjectId | DISTRB_PROJECT_ID | — | ✅ |
| 48 | DosDistributionDetailsIntPEODistrbPropamtCurrencyCode | DISTRB_PROPAMT_CURRENCY_CODE | — | ✅ |
| 49 | DosDistributionDetailsIntPEODistrbProposedAmount | DISTRB_PROPOSED_AMOUNT | — | ✅ |
| 50 | DosDistributionDetailsIntPEODistrbProposedChrgAccntId | DISTRB_PROPOSED_CHRG_ACCNT_ID | — | ✅ |
| 51 | DosDistributionDetailsIntPEODistrbProposedPercent | DISTRB_PROPOSED_PERCENT | — | ✅ |
| 52 | DosDistributionDetailsIntPEODistrbProposedProjectId | DISTRB_PROPOSED_PROJECT_ID | — | ✅ |
| 53 | DosDistributionDetailsIntPEODistrbProposedQuantity | DISTRB_PROPOSED_QUANTITY | — | ✅ |
| 54 | DosDistributionDetailsIntPEODistrbProposedQuantityUom | DISTRB_PROPOSED_QUANTITY_UOM | — | ✅ |
| 55 | DosDistributionDetailsIntPEODistrbProposedTaskId | DISTRB_PROPOSED_TASK_ID | — | ✅ |
| 56 | DosDistributionDetailsIntPEODistrbQuantity | DISTRB_QUANTITY | — | ✅ |
| 57 | DosDistributionDetailsIntPEODistrbQuantityUom | DISTRB_QUANTITY_UOM | — | ✅ |
| 58 | DosDistributionDetailsIntPEODistrbRecoverableCrncyTax | DISTRB_RECOVERABLE_CRNCY_TAX | — | ✅ |
| 59 | DosDistributionDetailsIntPEODistrbRecoverableTax | DISTRB_RECOVERABLE_TAX | — | ✅ |
| 60 | DosDistributionDetailsIntPEODistrbRequestingBuId | DISTRB_REQUESTING_BU_ID | — | ✅ |
| 61 | DosDistributionDetailsIntPEODistrbRequisitionLineId | DISTRB_REQUISITION_LINE_ID | — | ✅ |
| 62 | DosDistributionDetailsIntPEODistrbTaskId | DISTRB_TASK_ID | — | ✅ |
| 63 | DosDistributionDetailsIntPEODistributionDetailsIntfId | DISTRIBUTION_DETAILS_INTF_ID | 🔑 | ✅ |
| 64 | DosDistributionDetailsIntPEODistributionId | DISTRIBUTION_ID | — | ✅ |
| 65 | DosDistributionDetailsIntPEODistributionNumber | DISTRIBUTION_NUMBER | — | ✅ |
| 66 | DosDistributionDetailsIntPEODistributionOperation | DISTRIBUTION_OPERATION | — | ✅ |
| 67 | DosDistributionDetailsIntPEOHeaderInterfaceId | HEADER_INTERFACE_ID | — | ✅ |
| 68 | DosDistributionDetailsIntPEOInterfaceBatchNumber | INTERFACE_BATCH_NUMBER | — | ✅ |
| 69 | DosDistributionDetailsIntPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 70 | DosDistributionDetailsIntPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 71 | DosDistributionDetailsIntPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 72 | DosDistributionDetailsIntPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 73 | DosDistributionDetailsIntPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 74 | DosDistributionDetailsIntPEOLineInterfaceId | LINE_INTERFACE_ID | — | ✅ |
| 75 | DosDistributionDetailsIntPEOLoadRequestId | LOAD_REQUEST_ID | — | ✅ |
| 76 | DosDistributionDetailsIntPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 77 | DosDistributionDetailsIntPEOPjcBillableFlag | PJC_BILLABLE_FLAG | — | ✅ |
| 78 | DosDistributionDetailsIntPEOPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | ✅ |
| 79 | DosDistributionDetailsIntPEOPjcContextCategory | PJC_CONTEXT_CATEGORY | — | ✅ |
| 80 | DosDistributionDetailsIntPEOPjcContractId | PJC_CONTRACT_ID | — | ✅ |
| 81 | DosDistributionDetailsIntPEOPjcContractLineId | PJC_CONTRACT_LINE_ID | — | ✅ |
| 82 | DosDistributionDetailsIntPEOPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | ✅ |
| 83 | DosDistributionDetailsIntPEOPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | ✅ |
| 84 | DosDistributionDetailsIntPEOPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | ✅ |
| 85 | DosDistributionDetailsIntPEOPjcOrganizationId | PJC_ORGANIZATION_ID | — | ✅ |
| 86 | DosDistributionDetailsIntPEOPjcProjectId | PJC_PROJECT_ID | — | ✅ |
| 87 | DosDistributionDetailsIntPEOPjcProjectNumber | PJC_PROJECT_NUMBER | — | ✅ |
| 88 | DosDistributionDetailsIntPEOPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | ✅ |
| 89 | DosDistributionDetailsIntPEOPjcReservedAttribute10 | PJC_RESERVED_ATTRIBUTE10 | — | ✅ |
| 90 | DosDistributionDetailsIntPEOPjcReservedAttribute2 | PJC_RESERVED_ATTRIBUTE2 | — | ✅ |
| 91 | DosDistributionDetailsIntPEOPjcReservedAttribute3 | PJC_RESERVED_ATTRIBUTE3 | — | ✅ |
| 92 | DosDistributionDetailsIntPEOPjcReservedAttribute4 | PJC_RESERVED_ATTRIBUTE4 | — | ✅ |
| 93 | DosDistributionDetailsIntPEOPjcReservedAttribute5 | PJC_RESERVED_ATTRIBUTE5 | — | ✅ |
| 94 | DosDistributionDetailsIntPEOPjcReservedAttribute6 | PJC_RESERVED_ATTRIBUTE6 | — | ✅ |
| 95 | DosDistributionDetailsIntPEOPjcReservedAttribute7 | PJC_RESERVED_ATTRIBUTE7 | — | ✅ |
| 96 | DosDistributionDetailsIntPEOPjcReservedAttribute8 | PJC_RESERVED_ATTRIBUTE8 | — | ✅ |
| 97 | DosDistributionDetailsIntPEOPjcReservedAttribute9 | PJC_RESERVED_ATTRIBUTE9 | — | ✅ |
| 98 | DosDistributionDetailsIntPEOPjcTaskId | PJC_TASK_ID | — | ✅ |
| 99 | DosDistributionDetailsIntPEOPjcTaskNumber | PJC_TASK_NUMBER | — | ✅ |
| 100 | DosDistributionDetailsIntPEOPjcUserDefAttribute1 | PJC_USER_DEF_ATTRIBUTE1 | — | ✅ |
| 101 | DosDistributionDetailsIntPEOPjcUserDefAttribute10 | PJC_USER_DEF_ATTRIBUTE10 | — | ✅ |
| 102 | DosDistributionDetailsIntPEOPjcUserDefAttribute2 | PJC_USER_DEF_ATTRIBUTE2 | — | ✅ |
| 103 | DosDistributionDetailsIntPEOPjcUserDefAttribute3 | PJC_USER_DEF_ATTRIBUTE3 | — | ✅ |
| 104 | DosDistributionDetailsIntPEOPjcUserDefAttribute4 | PJC_USER_DEF_ATTRIBUTE4 | — | ✅ |
| 105 | DosDistributionDetailsIntPEOPjcUserDefAttribute5 | PJC_USER_DEF_ATTRIBUTE5 | — | ✅ |
| 106 | DosDistributionDetailsIntPEOPjcUserDefAttribute6 | PJC_USER_DEF_ATTRIBUTE6 | — | ✅ |
| 107 | DosDistributionDetailsIntPEOPjcUserDefAttribute7 | PJC_USER_DEF_ATTRIBUTE7 | — | ✅ |
| 108 | DosDistributionDetailsIntPEOPjcUserDefAttribute8 | PJC_USER_DEF_ATTRIBUTE8 | — | ✅ |
| 109 | DosDistributionDetailsIntPEOPjcUserDefAttribute9 | PJC_USER_DEF_ATTRIBUTE9 | — | ✅ |
| 110 | DosDistributionDetailsIntPEOPjcWorkTypeId | PJC_WORK_TYPE_ID | — | ✅ |
| 111 | DosDistributionDetailsIntPEORequestId | REQUEST_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
