---
id: DOC-OTHER-PVO-ProjectCommitmentPVO
doc_type: system-doc
title: "ProjectCommitmentPVO — PVO Cross-Module"
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
  - ProjectCommitmentPVO
  - projectcommitmentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectCommitmentPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Commitment. Acessa as tabelas: FND_CURRENCIES_VL, HR_ORGANIZATION_INFORMATION_F, HR_ORGANIZATION_V (+9).

**Caminho:** `FscmTopModelAM.PjcTransactionsAM.ProjectCommitmentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 146 | 12 | 1 | 98 | 67% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_currencies_vl|FND_CURRENCIES_VL]] — 2 atributos
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 10 atributos (2 BICC)
- [[hr_organization_v|HR_ORGANIZATION_V]] — 5 atributos (2 BICC)
- [[pjc_commitment_txns|PJC_COMMITMENT_TXNS]] — 105 atributos (1 PKs, 83 BICC)
- [[pjc_lookups|PJC_LOOKUPS]] — 3 atributos (1 BICC)
- [[pjf_exp_types_b|PJF_EXP_TYPES_B]] — 3 atributos
- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 8 atributos (1 BICC)
- [[pjf_txn_document_vl|PJF_TXN_DOCUMENT_VL]] — 2 atributos (2 BICC)
- [[pjf_txn_doc_entry_vl|PJF_TXN_DOC_ENTRY_VL]] — 2 atributos (2 BICC)
- [[pjf_txn_sources_vl|PJF_TXN_SOURCES_VL]] — 2 atributos (2 BICC)
- [[pjf_units_of_measure_v|PJF_UNITS_OF_MEASURE_V]] — 2 atributos (1 BICC)
- [[pjf_work_types_vl|PJF_WORK_TYPES_VL]] — 2 atributos (2 BICC)

---

## ⚙️ Atributos

### [[fnd_currencies_vl|FND_CURRENCIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurrencyPEOCurrencyCode | CURRENCY_CODE | — | — |
| 2 | CurrencyPEOCurrencyName | NAME | — | — |

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgInfomationPEOPrvdrPrimaryLedgerID | ORG_INFORMATION3 | — | — |
| 2 | OrgInformationPEOLegalEntityId | ORG_INFORMATION2 | — | — |
| 3 | OrganizationInformationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | OrganizationInformationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | OrganizationInformationPEOOrgInformationId | ORG_INFORMATION_ID | — | — |
| 6 | RcvrOrgInfomationPEOBusinessUnitId | ORGANIZATION_ID | — | — |
| 7 | RcvrOrgInfomationPEOPrimaryLedgerID | ORG_INFORMATION3 | — | — |
| 8 | RcvrOrganizationInformationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 9 | RcvrOrganizationInformationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 10 | RcvrOrganizationInformationPEOOrgInformationId | ORG_INFORMATION_ID | — | — |

### [[hr_organization_v|HR_ORGANIZATION_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationDPEOClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | OrganizationDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | OrganizationDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | OrganizationDPEOName | NAME | — | ✅ |
| 5 | OrganizationDPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[pjc_commitment_txns|PJC_COMMITMENT_TXNS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CommitmentTxnId | COMMITMENT_TXN_ID | 🔑 | ✅ |
| 2 | ProjectCommitmentPEOAcctBrdndCost | ACCT_BRDND_COST | — | ✅ |
| 3 | ProjectCommitmentPEOAcctCurrencyCode | ACCT_CURRENCY_CODE | — | ✅ |
| 4 | ProjectCommitmentPEOAcctExchangeRate | ACCT_EXCHANGE_RATE | — | ✅ |
| 5 | ProjectCommitmentPEOAcctRateDate | ACCT_RATE_DATE | — | — |
| 6 | ProjectCommitmentPEOAcctRateType | ACCT_RATE_TYPE | — | — |
| 7 | ProjectCommitmentPEOAcctRawCost | ACCT_RAW_COST | — | ✅ |
| 8 | ProjectCommitmentPEOAdditionalInfo1 | ADDITIONAL_INFO1 | — | ✅ |
| 9 | ProjectCommitmentPEOAdditionalInfo2 | ADDITIONAL_INFO2 | — | ✅ |
| 10 | ProjectCommitmentPEOAdditionalInfo3 | ADDITIONAL_INFO3 | — | ✅ |
| 11 | ProjectCommitmentPEOAmountCancelled | AMOUNT_CANCELLED | — | ✅ |
| 12 | ProjectCommitmentPEOAmountDelivered | AMOUNT_DELIVERED | — | ✅ |
| 13 | ProjectCommitmentPEOAmountInvoiced | AMOUNT_INVOICED | — | ✅ |
| 14 | ProjectCommitmentPEOAmountOrdered | AMOUNT_ORDERED | — | ✅ |
| 15 | ProjectCommitmentPEOAmountOutstandingDelivery | AMOUNT_OUTSTANDING_DELIVERY | — | ✅ |
| 16 | ProjectCommitmentPEOAmountOutstandingInvoice | AMOUNT_OUTSTANDING_INVOICE | — | ✅ |
| 17 | ProjectCommitmentPEOAmountOverbilled | AMOUNT_OVERBILLED | — | ✅ |
| 18 | ProjectCommitmentPEOBillableFlag | BILLABLE_FLAG | — | ✅ |
| 19 | ProjectCommitmentPEOBuId | BU_ID | — | ✅ |
| 20 | ProjectCommitmentPEOBudgetPeriodId | BUDGET_PERIOD_ID | — | — |
| 21 | ProjectCommitmentPEOBurdenSumDestRunId | BURDEN_SUM_DEST_RUN_ID | — | — |
| 22 | ProjectCommitmentPEOBurdenSumRejectionCode | BURDEN_SUM_REJECTION_CODE | — | — |
| 23 | ProjectCommitmentPEOBurdenSumSourceRunId | BURDEN_SUM_SOURCE_RUN_ID | — | — |
| 24 | ProjectCommitmentPEOCapitalizableFlag | CAPITALIZABLE_FLAG | — | ✅ |
| 25 | ProjectCommitmentPEOCmtApprovedDate | CMT_APPROVED_DATE | — | — |
| 26 | ProjectCommitmentPEOCmtApprovedStatus | CMT_APPROVED_STATUS | — | ✅ |
| 27 | ProjectCommitmentPEOCmtBuyerName | CMT_BUYER_NAME | — | ✅ |
| 28 | ProjectCommitmentPEOCmtCreationDate | CMT_CREATION_DATE | — | ✅ |
| 29 | ProjectCommitmentPEOCmtDistNum | CMT_DIST_NUM | — | ✅ |
| 30 | ProjectCommitmentPEOCmtDistributionId | CMT_DISTRIBUTION_ID | — | ✅ |
| 31 | ProjectCommitmentPEOCmtHeaderId | CMT_HEADER_ID | — | ✅ |
| 32 | ProjectCommitmentPEOCmtIndCompiledSetId | CMT_IND_COMPILED_SET_ID | — | — |
| 33 | ProjectCommitmentPEOCmtLineId | CMT_LINE_ID | — | ✅ |
| 34 | ProjectCommitmentPEOCmtLineNumber | CMT_LINE_NUMBER | — | ✅ |
| 35 | ProjectCommitmentPEOCmtNeedByDate | CMT_NEED_BY_DATE | — | ✅ |
| 36 | ProjectCommitmentPEOCmtNumber | CMT_NUMBER | — | ✅ |
| 37 | ProjectCommitmentPEOCmtPromisedDate | CMT_PROMISED_DATE | — | ✅ |
| 38 | ProjectCommitmentPEOCmtRequestorName | CMT_REQUESTOR_NAME | — | ✅ |
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
| 49 | ProjectCommitmentPEOExpTypeCostRateFlag | EXP_TYPE_COST_RATE_FLAG | — | — |
| 50 | ProjectCommitmentPEOExpenditureCategory | EXPENDITURE_CATEGORY | — | — |
| 51 | ProjectCommitmentPEOExpenditureItemDate | EXPENDITURE_ITEM_DATE | — | ✅ |
| 52 | ProjectCommitmentPEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | ✅ |
| 53 | ProjectCommitmentPEOGlDate | GL_DATE | — | ✅ |
| 54 | ProjectCommitmentPEOGlPeriod | GL_PERIOD | — | — |
| 55 | ProjectCommitmentPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 56 | ProjectCommitmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 57 | ProjectCommitmentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 58 | ProjectCommitmentPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 59 | ProjectCommitmentPEOLineType | LINE_TYPE | — | ✅ |
| 60 | ProjectCommitmentPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 61 | ProjectCommitmentPEOOriginalAmountOrdered | ORIGINAL_AMOUNT_ORDERED | — | ✅ |
| 62 | ProjectCommitmentPEOOriginalQuantityOrdered | ORIGINAL_QUANTITY_ORDERED | — | ✅ |
| 63 | ProjectCommitmentPEOOriginalTxnReference | ORIGINAL_TXN_REFERENCE | — | ✅ |
| 64 | ProjectCommitmentPEOPaDate | PA_DATE | — | ✅ |
| 65 | ProjectCommitmentPEOPaPeriod | PA_PERIOD | — | — |
| 66 | ProjectCommitmentPEOPrjBrdndCost | PRJ_BRDND_COST | — | ✅ |
| 67 | ProjectCommitmentPEOPrjCurrencyCode | PRJ_CURRENCY_CODE | — | ✅ |
| 68 | ProjectCommitmentPEOPrjExchangeRate | PRJ_EXCHANGE_RATE | — | ✅ |
| 69 | ProjectCommitmentPEOPrjRateDate | PRJ_RATE_DATE | — | — |
| 70 | ProjectCommitmentPEOPrjRateType | PRJ_RATE_TYPE | — | — |
| 71 | ProjectCommitmentPEOPrjRawCost | PRJ_RAW_COST | — | ✅ |
| 72 | ProjectCommitmentPEOProjectId | PROJECT_ID | — | ✅ |
| 73 | ProjectCommitmentPEOProjectTypeId | PROJECT_TYPE_ID | — | — |
| 74 | ProjectCommitmentPEOProjfuncBrdndCost | PROJFUNC_BRDND_COST | — | ✅ |
| 75 | ProjectCommitmentPEOProjfuncCurrencyCode | PROJFUNC_CURRENCY_CODE | — | ✅ |
| 76 | ProjectCommitmentPEOProjfuncExchangeRate | PROJFUNC_EXCHANGE_RATE | — | ✅ |
| 77 | ProjectCommitmentPEOProjfuncRateDate | PROJFUNC_RATE_DATE | — | — |
| 78 | ProjectCommitmentPEOProjfuncRateType | PROJFUNC_RATE_TYPE | — | — |
| 79 | ProjectCommitmentPEOProjfuncRawCost | PROJFUNC_RAW_COST | — | ✅ |
| 80 | ProjectCommitmentPEOQuantityCancelled | QUANTITY_CANCELLED | — | ✅ |
| 81 | ProjectCommitmentPEOQuantityDelivered | QUANTITY_DELIVERED | — | ✅ |
| 82 | ProjectCommitmentPEOQuantityInvoiced | QUANTITY_INVOICED | — | ✅ |
| 83 | ProjectCommitmentPEOQuantityOrdered | QUANTITY_ORDERED | — | ✅ |
| 84 | ProjectCommitmentPEOQuantityOutstandingDelivery | QUANTITY_OUTSTANDING_DELIVERY | — | ✅ |
| 85 | ProjectCommitmentPEOQuantityOutstandingInvoice | QUANTITY_OUTSTANDING_INVOICE | — | ✅ |
| 86 | ProjectCommitmentPEOQuantityOverbilled | QUANTITY_OVERBILLED | — | ✅ |
| 87 | ProjectCommitmentPEORawCostRate | RAW_COST_RATE | — | — |
| 88 | ProjectCommitmentPEORecvrGlDate | RECVR_GL_DATE | — | ✅ |
| 89 | ProjectCommitmentPEORecvrGlPeriodName | RECVR_GL_PERIOD_NAME | — | ✅ |
| 90 | ProjectCommitmentPEORecvrOrgId | RECVR_ORG_ID | — | ✅ |
| 91 | ProjectCommitmentPEORecvrPaDate | RECVR_PA_DATE | — | ✅ |
| 92 | ProjectCommitmentPEORecvrPaPeriodName | RECVR_PA_PERIOD_NAME | — | ✅ |
| 93 | ProjectCommitmentPEOReservedAttribute1 | RESERVED_ATTRIBUTE1 | — | — |
| 94 | ProjectCommitmentPEOResourceClass | RESOURCE_CLASS | — | ✅ |
| 95 | ProjectCommitmentPEORevenueCategory | REVENUE_CATEGORY | — | — |
| 96 | ProjectCommitmentPEOSrcSystemLinkageFunction | SRC_SYSTEM_LINKAGE_FUNCTION | — | — |
| 97 | ProjectCommitmentPEOSystemLinkageFunction | SYSTEM_LINKAGE_FUNCTION | — | ✅ |
| 98 | ProjectCommitmentPEOTaskId | TASK_ID | — | ✅ |
| 99 | ProjectCommitmentPEOTotCmtQuantity | TOT_CMT_QUANTITY | — | ✅ |
| 100 | ProjectCommitmentPEOTransactionSourceId | TRANSACTION_SOURCE_ID | — | ✅ |
| 101 | ProjectCommitmentPEOTransactionStatusCode | TRANSACTION_STATUS_CODE | — | ✅ |
| 102 | ProjectCommitmentPEOUnitPrice | UNIT_PRICE | — | — |
| 103 | ProjectCommitmentPEOUomCode | UOM_CODE | — | ✅ |
| 104 | ProjectCommitmentPEOVendorId | VENDOR_ID | — | ✅ |
| 105 | ProjectCommitmentPEOWorkTypeId | WORK_TYPE_ID | — | ✅ |

### [[pjc_lookups|PJC_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjcLookupPEOLookupCode | LOOKUP_CODE | — | — |
| 2 | PjcLookupPEOLookupType | LOOKUP_TYPE | — | — |
| 3 | PjcLookupPEOMeaning | MEANING | — | ✅ |

### [[pjf_exp_types_b|PJF_EXP_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureTypeBasePEOExpenditureCategoryId | EXPENDITURE_CATEGORY_ID | — | — |
| 2 | ExpenditureTypeBasePEORevenueCategoryCode | REVENUE_CATEGORY_CODE | — | — |
| 3 | ExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |

### [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectBasePEOCarryingOutOrganizationId | CARRYING_OUT_ORGANIZATION_ID | — | — |
| 2 | ProjectBasePEOCreatedBy | CREATED_BY | — | — |
| 3 | ProjectBasePEOCreationDate | CREATION_DATE | — | — |
| 4 | ProjectBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ProjectBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ProjectBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ProjectBasePEOOrgId | ORG_ID | — | — |
| 8 | ProjectBasePEOProjectId | PROJECT_ID | — | — |

### [[pjf_txn_document_vl|PJF_TXN_DOCUMENT_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionDocumentPEODocumentId | DOCUMENT_ID | — | ✅ |
| 2 | TransactionDocumentPEODocumentName | DOCUMENT_NAME | — | ✅ |

### [[pjf_txn_doc_entry_vl|PJF_TXN_DOC_ENTRY_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionDocEntryPEODocEntryId | DOC_ENTRY_ID | — | ✅ |
| 2 | TransactionDocEntryPEODocEntryName | DOC_ENTRY_NAME | — | ✅ |

### [[pjf_txn_sources_vl|PJF_TXN_SOURCES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionSourcePEOTransactionSourceId | TRANSACTION_SOURCE_ID | — | ✅ |
| 2 | TransactionSourcePEOUserTransactionSource | USER_TRANSACTION_SOURCE | — | ✅ |

### [[pjf_units_of_measure_v|PJF_UNITS_OF_MEASURE_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UnitOfMeasurePEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 2 | UnitOfMeasurePEOUomCode | UOM_CODE | — | — |

### [[pjf_work_types_vl|PJF_WORK_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkTypePEOName | NAME | — | ✅ |
| 2 | WorkTypePEOWorkTypeId | WORK_TYPE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
