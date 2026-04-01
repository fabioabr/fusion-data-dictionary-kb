---
id: DOC-OTHER-PVO-ProjectCommitmentExtractPVO
doc_type: system-doc
title: "ProjectCommitmentExtractPVO — PVO Cross-Module"
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
  - ProjectCommitmentExtractPVO
  - projectcommitmentextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectCommitmentExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Commitment Extract. Acessa as tabelas: PJC_COMMITMENT_TXNS, PJF_UNITS_OF_MEASURE_V.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjcBiccExtractAM.ProjectCommitmentExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 109 | 2 | 1 | 108 | 99% |

---

## 🔗 Tabelas Relacionadas

- [[pjc_commitment_txns|PJC_COMMITMENT_TXNS]] — 107 atributos (1 PKs, 106 BICC)
- [[pjf_units_of_measure_v|PJF_UNITS_OF_MEASURE_V]] — 2 atributos (2 BICC)

---

## ⚙️ Atributos

### [[pjc_commitment_txns|PJC_COMMITMENT_TXNS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectCommitmentPEOAcctBrdndCost | ACCT_BRDND_COST | — | ✅ |
| 2 | ProjectCommitmentPEOAcctCurrencyCode | ACCT_CURRENCY_CODE | — | ✅ |
| 3 | ProjectCommitmentPEOAcctExchangeRate | ACCT_EXCHANGE_RATE | — | ✅ |
| 4 | ProjectCommitmentPEOAcctRateDate | ACCT_RATE_DATE | — | ✅ |
| 5 | ProjectCommitmentPEOAcctRateType | ACCT_RATE_TYPE | — | ✅ |
| 6 | ProjectCommitmentPEOAcctRawCost | ACCT_RAW_COST | — | ✅ |
| 7 | ProjectCommitmentPEOAdditionalInfo1 | ADDITIONAL_INFO1 | — | ✅ |
| 8 | ProjectCommitmentPEOAdditionalInfo2 | ADDITIONAL_INFO2 | — | ✅ |
| 9 | ProjectCommitmentPEOAdditionalInfo3 | ADDITIONAL_INFO3 | — | ✅ |
| 10 | ProjectCommitmentPEOAmountCancelled | AMOUNT_CANCELLED | — | ✅ |
| 11 | ProjectCommitmentPEOAmountDelivered | AMOUNT_DELIVERED | — | ✅ |
| 12 | ProjectCommitmentPEOAmountInvoiced | AMOUNT_INVOICED | — | ✅ |
| 13 | ProjectCommitmentPEOAmountOrdered | AMOUNT_ORDERED | — | ✅ |
| 14 | ProjectCommitmentPEOAmountOutstandingDelivery | AMOUNT_OUTSTANDING_DELIVERY | — | ✅ |
| 15 | ProjectCommitmentPEOAmountOutstandingInvoice | AMOUNT_OUTSTANDING_INVOICE | — | ✅ |
| 16 | ProjectCommitmentPEOAmountOverbilled | AMOUNT_OVERBILLED | — | ✅ |
| 17 | ProjectCommitmentPEOBillableFlag | BILLABLE_FLAG | — | ✅ |
| 18 | ProjectCommitmentPEOBuId | BU_ID | — | ✅ |
| 19 | ProjectCommitmentPEOBudgetPeriodId | BUDGET_PERIOD_ID | — | ✅ |
| 20 | ProjectCommitmentPEOBurdenSumDestRunId | BURDEN_SUM_DEST_RUN_ID | — | ✅ |
| 21 | ProjectCommitmentPEOBurdenSumRejectionCode | BURDEN_SUM_REJECTION_CODE | — | ✅ |
| 22 | ProjectCommitmentPEOBurdenSumSourceRunId | BURDEN_SUM_SOURCE_RUN_ID | — | ✅ |
| 23 | ProjectCommitmentPEOCapitalizableFlag | CAPITALIZABLE_FLAG | — | ✅ |
| 24 | ProjectCommitmentPEOCmtApprovedDate | CMT_APPROVED_DATE | — | ✅ |
| 25 | ProjectCommitmentPEOCmtApprovedStatus | CMT_APPROVED_STATUS | — | ✅ |
| 26 | ProjectCommitmentPEOCmtBuyerName | CMT_BUYER_NAME | — | ✅ |
| 27 | ProjectCommitmentPEOCmtCreationDate | CMT_CREATION_DATE | — | ✅ |
| 28 | ProjectCommitmentPEOCmtDistNum | CMT_DIST_NUM | — | ✅ |
| 29 | ProjectCommitmentPEOCmtDistributionId | CMT_DISTRIBUTION_ID | — | ✅ |
| 30 | ProjectCommitmentPEOCmtHeaderId | CMT_HEADER_ID | — | ✅ |
| 31 | ProjectCommitmentPEOCmtIndCompiledSetId | CMT_IND_COMPILED_SET_ID | — | ✅ |
| 32 | ProjectCommitmentPEOCmtLineId | CMT_LINE_ID | — | ✅ |
| 33 | ProjectCommitmentPEOCmtLineNumber | CMT_LINE_NUMBER | — | ✅ |
| 34 | ProjectCommitmentPEOCmtNeedByDate | CMT_NEED_BY_DATE | — | ✅ |
| 35 | ProjectCommitmentPEOCmtNumber | CMT_NUMBER | — | ✅ |
| 36 | ProjectCommitmentPEOCmtPromisedDate | CMT_PROMISED_DATE | — | ✅ |
| 37 | ProjectCommitmentPEOCmtRequestorName | CMT_REQUESTOR_NAME | — | ✅ |
| 38 | ProjectCommitmentPEOCommitmentTxnId | COMMITMENT_TXN_ID | 🔑 | ✅ |
| 39 | ProjectCommitmentPEOCommitmentType | COMMITMENT_TYPE | — | ✅ |
| 40 | ProjectCommitmentPEOContractId | CONTRACT_ID | — | ✅ |
| 41 | ProjectCommitmentPEOCreatedBy | CREATED_BY | — | ✅ |
| 42 | ProjectCommitmentPEOCreationDate | CREATION_DATE | — | ✅ |
| 43 | ProjectCommitmentPEODenomBrdndCost | DENOM_BRDND_COST | — | ✅ |
| 44 | ProjectCommitmentPEODenomCurrencyCode | DENOM_CURRENCY_CODE | — | ✅ |
| 45 | ProjectCommitmentPEODenomRawCost | DENOM_RAW_COST | — | ✅ |
| 46 | ProjectCommitmentPEODescription | DESCRIPTION | — | ✅ |
| 47 | ProjectCommitmentPEODocEntryId | DOC_ENTRY_ID | — | ✅ |
| 48 | ProjectCommitmentPEODocumentId | DOCUMENT_ID | — | ✅ |
| 49 | ProjectCommitmentPEOExpTypeCostRateFlag | EXP_TYPE_COST_RATE_FLAG | — | ✅ |
| 50 | ProjectCommitmentPEOExpenditureCategory | EXPENDITURE_CATEGORY | — | ✅ |
| 51 | ProjectCommitmentPEOExpenditureCategoryId | EXPENDITURE_CATEGORY_ID | — | ✅ |
| 52 | ProjectCommitmentPEOExpenditureItemDate | EXPENDITURE_ITEM_DATE | — | ✅ |
| 53 | ProjectCommitmentPEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | ✅ |
| 54 | ProjectCommitmentPEOGlDate | GL_DATE | — | ✅ |
| 55 | ProjectCommitmentPEOGlPeriod | GL_PERIOD | — | ✅ |
| 56 | ProjectCommitmentPEOInterfaceId | INTERFACE_ID | — | ✅ |
| 57 | ProjectCommitmentPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 58 | ProjectCommitmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 59 | ProjectCommitmentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 60 | ProjectCommitmentPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 61 | ProjectCommitmentPEOLineType | LINE_TYPE | — | ✅ |
| 62 | ProjectCommitmentPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 63 | ProjectCommitmentPEOOriginalAmountOrdered | ORIGINAL_AMOUNT_ORDERED | — | ✅ |
| 64 | ProjectCommitmentPEOOriginalQuantityOrdered | ORIGINAL_QUANTITY_ORDERED | — | ✅ |
| 65 | ProjectCommitmentPEOOriginalTxnReference | ORIGINAL_TXN_REFERENCE | — | ✅ |
| 66 | ProjectCommitmentPEOPaDate | PA_DATE | — | ✅ |
| 67 | ProjectCommitmentPEOPaPeriod | PA_PERIOD | — | ✅ |
| 68 | ProjectCommitmentPEOPrjBrdndCost | PRJ_BRDND_COST | — | ✅ |
| 69 | ProjectCommitmentPEOPrjCurrencyCode | PRJ_CURRENCY_CODE | — | ✅ |
| 70 | ProjectCommitmentPEOPrjExchangeRate | PRJ_EXCHANGE_RATE | — | ✅ |
| 71 | ProjectCommitmentPEOPrjRateDate | PRJ_RATE_DATE | — | ✅ |
| 72 | ProjectCommitmentPEOPrjRateType | PRJ_RATE_TYPE | — | ✅ |
| 73 | ProjectCommitmentPEOPrjRawCost | PRJ_RAW_COST | — | ✅ |
| 74 | ProjectCommitmentPEOProjectId | PROJECT_ID | — | ✅ |
| 75 | ProjectCommitmentPEOProjectTypeId | PROJECT_TYPE_ID | — | ✅ |
| 76 | ProjectCommitmentPEOProjfuncBrdndCost | PROJFUNC_BRDND_COST | — | ✅ |
| 77 | ProjectCommitmentPEOProjfuncCurrencyCode | PROJFUNC_CURRENCY_CODE | — | ✅ |
| 78 | ProjectCommitmentPEOProjfuncExchangeRate | PROJFUNC_EXCHANGE_RATE | — | ✅ |
| 79 | ProjectCommitmentPEOProjfuncRateDate | PROJFUNC_RATE_DATE | — | ✅ |
| 80 | ProjectCommitmentPEOProjfuncRateType | PROJFUNC_RATE_TYPE | — | ✅ |
| 81 | ProjectCommitmentPEOProjfuncRawCost | PROJFUNC_RAW_COST | — | ✅ |
| 82 | ProjectCommitmentPEOQuantityCancelled | QUANTITY_CANCELLED | — | ✅ |
| 83 | ProjectCommitmentPEOQuantityDelivered | QUANTITY_DELIVERED | — | ✅ |
| 84 | ProjectCommitmentPEOQuantityInvoiced | QUANTITY_INVOICED | — | ✅ |
| 85 | ProjectCommitmentPEOQuantityOrdered | QUANTITY_ORDERED | — | ✅ |
| 86 | ProjectCommitmentPEOQuantityOutstandingDelivery | QUANTITY_OUTSTANDING_DELIVERY | — | ✅ |
| 87 | ProjectCommitmentPEOQuantityOutstandingInvoice | QUANTITY_OUTSTANDING_INVOICE | — | ✅ |
| 88 | ProjectCommitmentPEOQuantityOverbilled | QUANTITY_OVERBILLED | — | ✅ |
| 89 | ProjectCommitmentPEORawCostRate | RAW_COST_RATE | — | ✅ |
| 90 | ProjectCommitmentPEORecvrGlDate | RECVR_GL_DATE | — | ✅ |
| 91 | ProjectCommitmentPEORecvrGlPeriodName | RECVR_GL_PERIOD_NAME | — | ✅ |
| 92 | ProjectCommitmentPEORecvrOrgId | RECVR_ORG_ID | — | ✅ |
| 93 | ProjectCommitmentPEORecvrPaDate | RECVR_PA_DATE | — | ✅ |
| 94 | ProjectCommitmentPEORecvrPaPeriodName | RECVR_PA_PERIOD_NAME | — | ✅ |
| 95 | ProjectCommitmentPEOReservedAttribute1 | RESERVED_ATTRIBUTE1 | — | — |
| 96 | ProjectCommitmentPEOResourceClass | RESOURCE_CLASS | — | ✅ |
| 97 | ProjectCommitmentPEORevenueCategory | REVENUE_CATEGORY | — | ✅ |
| 98 | ProjectCommitmentPEOSrcSystemLinkageFunction | SRC_SYSTEM_LINKAGE_FUNCTION | — | ✅ |
| 99 | ProjectCommitmentPEOSystemLinkageFunction | SYSTEM_LINKAGE_FUNCTION | — | ✅ |
| 100 | ProjectCommitmentPEOTaskId | TASK_ID | — | ✅ |
| 101 | ProjectCommitmentPEOTotCmtQuantity | TOT_CMT_QUANTITY | — | ✅ |
| 102 | ProjectCommitmentPEOTransactionSourceId | TRANSACTION_SOURCE_ID | — | ✅ |
| 103 | ProjectCommitmentPEOTransactionStatusCode | TRANSACTION_STATUS_CODE | — | ✅ |
| 104 | ProjectCommitmentPEOUnitPrice | UNIT_PRICE | — | ✅ |
| 105 | ProjectCommitmentPEOUomCode | UOM_CODE | — | ✅ |
| 106 | ProjectCommitmentPEOVendorId | VENDOR_ID | — | ✅ |
| 107 | ProjectCommitmentPEOWorkTypeId | WORK_TYPE_ID | — | ✅ |

### [[pjf_units_of_measure_v|PJF_UNITS_OF_MEASURE_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UnitOfMeasurePEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 2 | UnitOfMeasurePEOUomCode | UOM_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
