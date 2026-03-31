---
id: DOC-OTHER-PVO-CostTransactionPVO
doc_type: system-doc
title: "CostTransactionPVO — PVO Cross-Module"
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
  - CostTransactionPVO
  - costtransactionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CostTransactionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cost Transaction. Acessa as tabelas: CST_COST_BOOKS_TL, CST_COST_DISTRIBUTIONS, CST_COST_DISTRIBUTION_LINES (+14).

**Caminho:** `FscmTopModelAM.CostTransactionAM.CostTransactionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 237 | 17 | 1 | 79 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_books_tl|CST_COST_BOOKS_TL]] — 3 atributos
- [[cst_cost_distributions|CST_COST_DISTRIBUTIONS]] — 28 atributos (13 BICC)
- [[cst_cost_distribution_lines|CST_COST_DISTRIBUTION_LINES]] — 24 atributos (1 PKs, 17 BICC)
- [[cst_cost_orgs_v|CST_COST_ORGS_V]] — 8 atributos (5 BICC)
- [[cst_cost_org_books|CST_COST_ORG_BOOKS]] — 4 atributos
- [[cst_cost_profiles_tl|CST_COST_PROFILES_TL]] — 3 atributos (1 BICC)
- [[cst_expense_pools_tl|CST_EXPENSE_POOLS_TL]] — 6 atributos (1 BICC)
- [[cst_inv_transactions|CST_INV_TRANSACTIONS]] — 3 atributos
- [[cst_layer_costs|CST_LAYER_COSTS]] — 31 atributos (3 BICC)
- [[cst_transactions|CST_TRANSACTIONS]] — 67 atributos (30 BICC)
- [[cst_transfer_costs|CST_TRANSFER_COSTS]] — 31 atributos (4 BICC)
- [[cst_val_units_tl|CST_VAL_UNITS_TL]] — 3 atributos (1 BICC)
- [[fnd_messages_vl|FND_MESSAGES_VL]] — 3 atributos
- [[gl_calendars|GL_CALENDARS]] — 6 atributos
- [[xla_event_classes_tl|XLA_EVENT_CLASSES_TL]] — 6 atributos (1 BICC)
- [[xla_event_types_tl|XLA_EVENT_TYPES_TL]] — 7 atributos
- [[xla_lookups|XLA_LOOKUPS]] — 4 atributos (3 BICC)

---

## ⚙️ Atributos

### [[cst_cost_books_tl|CST_COST_BOOKS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransferBookTLPEOCostBookDesc | COST_BOOK_DESC | — | — |
| 2 | TransferBookTLPEOCostBookId | COST_BOOK_ID | — | — |
| 3 | TransferBookTLPEOLanguage | LANGUAGE | — | — |

### [[cst_cost_distributions|CST_COST_DISTRIBUTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostDistributionsEOAccountedFlag | ACCOUNTED_FLAG | — | — |
| 2 | CostDistributionsEOAdditionalProcessingCode | ADDITIONAL_PROCESSING_CODE | — | — |
| 3 | CostDistributionsEOBaseCurrencyCode | BASE_CURRENCY_CODE | — | ✅ |
| 4 | CostDistributionsEOCostBookId | COST_BOOK_ID | — | — |
| 5 | CostDistributionsEOCostOrganizationId | COST_ORGANIZATION_ID | — | — |
| 6 | CostDistributionsEOCostTransactionType | COST_TRANSACTION_TYPE | — | — |
| 7 | CostDistributionsEOCostTransactionUom | COST_TRANSACTION_UOM | — | ✅ |
| 8 | CostDistributionsEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | CostDistributionsEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | CostDistributionsEODepTrxnId | DEP_TRXN_ID | — | — |
| 11 | CostDistributionsEODistributionId | DISTRIBUTION_ID | — | — |
| 12 | CostDistributionsEOEffDate | EFF_DATE | — | ✅ |
| 13 | CostDistributionsEOEntityCode | ENTITY_CODE | — | ✅ |
| 14 | CostDistributionsEOEventClassCode | EVENT_CLASS_CODE | — | ✅ |
| 15 | CostDistributionsEOEventId | EVENT_ID | — | ✅ |
| 16 | CostDistributionsEOEventTypeCode | EVENT_TYPE_CODE | — | — |
| 17 | CostDistributionsEOGlDate | GL_DATE | — | ✅ |
| 18 | CostDistributionsEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 19 | CostDistributionsEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 20 | CostDistributionsEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | CostDistributionsEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 22 | CostDistributionsEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 23 | CostDistributionsEOLayerQuantity | LAYER_QUANTITY | — | ✅ |
| 24 | CostDistributionsEOLedgerId | LEDGER_ID | — | — |
| 25 | CostDistributionsEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 26 | CostDistributionsEORecTrxnId | REC_TRXN_ID | — | — |
| 27 | CostDistributionsEORequestId | REQUEST_ID | — | — |
| 28 | CostDistributionsEOTransactionId | TRANSACTION_ID | — | — |

### [[cst_cost_distribution_lines|CST_COST_DISTRIBUTION_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostDistributionLinesEOAccountingDefinitionId | ACCOUNTING_DEFINITION_ID | — | — |
| 2 | CostDistributionLinesEOAccountingLineType | ACCOUNTING_LINE_TYPE | — | ✅ |
| 3 | CostDistributionLinesEOCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 4 | CostDistributionLinesEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 5 | CostDistributionLinesEOCostId | COST_ID | — | — |
| 6 | CostDistributionLinesEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | CostDistributionLinesEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | CostDistributionLinesEODistributionId | DISTRIBUTION_ID | — | — |
| 9 | CostDistributionLinesEODrCrSign | DR_CR_SIGN | — | ✅ |
| 10 | CostDistributionLinesEOEnteredCurrencyAmount | ENTERED_CURRENCY_AMOUNT | — | ✅ |
| 11 | CostDistributionLinesEOEnteredCurrencyCode | ENTERED_CURRENCY_CODE | — | ✅ |
| 12 | CostDistributionLinesEOEventId | EVENT_ID | — | — |
| 13 | CostDistributionLinesEOExchangeDate | EXCHANGE_DATE | — | ✅ |
| 14 | CostDistributionLinesEOExchangeRate | EXCHANGE_RATE | — | ✅ |
| 15 | CostDistributionLinesEOExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 16 | CostDistributionLinesEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | CostDistributionLinesEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 18 | CostDistributionLinesEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | CostDistributionLinesEOLedgerAmount | LEDGER_AMOUNT | — | ✅ |
| 20 | CostDistributionLinesEOLineNumber | LINE_NUMBER | — | — |
| 21 | CostDistributionLinesEOPjcTxnStatusCode | PJC_TXN_STATUS_CODE | — | ✅ |
| 22 | CostDistributionLinesEOSourceTable | SOURCE_TABLE | — | — |
| 23 | CostDistributionLinesEOTransactionCostId | TRANSACTION_COST_ID | — | — |
| 24 | DistributionLineId | DISTRIBUTION_LINE_ID | 🔑 | ✅ |

### [[cst_cost_orgs_v|CST_COST_ORGS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OwningCostOrgPEOCostOrgId | COST_ORG_ID | — | — |
| 2 | OwningCostOrgPEOCostOrgName | COST_ORG_NAME | — | ✅ |
| 3 | OwningCostOrgPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | OwningCostOrgPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | TransferCostOrgPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 6 | TransferCostOrgPEOCostOrgName | COST_ORG_NAME | — | ✅ |
| 7 | TransferCostOrgPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | TransferCostOrgPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |

### [[cst_cost_org_books|CST_COST_ORG_BOOKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostOrgBookPEOCalendarId | CALENDAR_ID | — | — |
| 2 | CostOrgBookPEOCostBookId | COST_BOOK_ID | — | — |
| 3 | CostOrgBookPEOCostOrgId | COST_ORG_ID | — | — |
| 4 | LedgerId | LEDGER_ID | — | — |

### [[cst_cost_profiles_tl|CST_COST_PROFILES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostProfileTLPEOCostProfileDesc | COST_PROFILE_DESC | — | ✅ |
| 2 | CostProfileTLPEOCostProfileId | COST_PROFILE_ID | — | — |
| 3 | CostProfileTLPEOLanguage | LANGUAGE | — | — |

### [[cst_expense_pools_tl|CST_EXPENSE_POOLS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LayerCostExpensePoolPEOExpensePoolDesc | EXPENSE_POOL_DESC | — | — |
| 2 | LayerCostExpensePoolPEOExpensePoolId | EXPENSE_POOL_ID | — | — |
| 3 | LayerCostExpensePoolPEOLanguage | LANGUAGE | — | — |
| 4 | TransferCostExpensePoolTLPEOExpensePoolDesc | EXPENSE_POOL_DESC | — | ✅ |
| 5 | TransferCostExpensePoolTLPEOExpensePoolId | EXPENSE_POOL_ID | — | — |
| 6 | TransferCostExpensePoolTLPEOLanguage | LANGUAGE | — | — |

### [[cst_inv_transactions|CST_INV_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstInvTransactionId | CST_INV_TRANSACTION_ID | — | — |
| 2 | CstInvTransactionsPEOLocatorId | LOCATOR_ID | — | — |
| 3 | CstInvTransactionsPEOSubinventoryCode | SUBINVENTORY_CODE | — | — |

### [[cst_layer_costs|CST_LAYER_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstLayerCostsPEOAbsorptionType | ABSORPTION_TYPE | — | — |
| 2 | CstLayerCostsPEOAdditionalProcessingCode | ADDITIONAL_PROCESSING_CODE | — | — |
| 3 | CstLayerCostsPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | — |
| 4 | CstLayerCostsPEOCostBookId | COST_BOOK_ID | — | — |
| 5 | CstLayerCostsPEOCostDate | COST_DATE | — | — |
| 6 | CstLayerCostsPEOCostElementId | COST_ELEMENT_ID | — | — |
| 7 | CstLayerCostsPEOCostOrgId | COST_ORG_ID | — | — |
| 8 | CstLayerCostsPEOCostTransactionType | COST_TRANSACTION_TYPE | — | — |
| 9 | CstLayerCostsPEOCreatedBy | CREATED_BY | — | — |
| 10 | CstLayerCostsPEOCreationDate | CREATION_DATE | — | — |
| 11 | CstLayerCostsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 12 | CstLayerCostsPEODepTrxnId | DEP_TRXN_ID | — | — |
| 13 | CstLayerCostsPEODistributionId | DISTRIBUTION_ID | — | — |
| 14 | CstLayerCostsPEOEffDate | EFF_DATE | — | — |
| 15 | CstLayerCostsPEOExpensePoolId | EXPENSE_POOL_ID | — | — |
| 16 | CstLayerCostsPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 17 | CstLayerCostsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 18 | CstLayerCostsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 19 | CstLayerCostsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | CstLayerCostsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | CstLayerCostsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 22 | CstLayerCostsPEOLayerCostId | LAYER_COST_ID | — | — |
| 23 | CstLayerCostsPEOPostedFlag | POSTED_FLAG | — | — |
| 24 | CstLayerCostsPEOQuantity | QUANTITY | — | — |
| 25 | CstLayerCostsPEORecTrxnId | REC_TRXN_ID | — | — |
| 26 | CstLayerCostsPEORequestId | REQUEST_ID | — | — |
| 27 | CstLayerCostsPEOTransactionCostId | TRANSACTION_COST_ID | — | — |
| 28 | CstLayerCostsPEOTransactionId | TRANSACTION_ID | — | — |
| 29 | CstLayerCostsPEOUnitCost | UNIT_COST | — | ✅ |
| 30 | CstLayerCostsPEOUomCode | UOM_CODE | — | — |
| 31 | CstLayerCostsPEOValUnitId | VAL_UNIT_ID | — | — |

### [[cst_transactions|CST_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionsEOAdditionalProcessingCode | ADDITIONAL_PROCESSING_CODE | — | — |
| 2 | TransactionsEOBaseTxnActionId | BASE_TXN_ACTION_ID | — | — |
| 3 | TransactionsEOBaseTxnSourceTypeId | BASE_TXN_SOURCE_TYPE_ID | — | ✅ |
| 4 | TransactionsEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | — |
| 5 | TransactionsEOBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 6 | TransactionsEOCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 7 | TransactionsEOCostBookId | COST_BOOK_ID | — | — |
| 8 | TransactionsEOCostDate | COST_DATE | — | ✅ |
| 9 | TransactionsEOCostMethodCode | COST_METHOD_CODE | — | — |
| 10 | TransactionsEOCostOrgId | COST_ORG_ID | — | — |
| 11 | TransactionsEOCostProfileId | COST_PROFILE_ID | — | — |
| 12 | TransactionsEOCostTransactionType | COST_TRANSACTION_TYPE | — | ✅ |
| 13 | TransactionsEOCreatedBy | CREATED_BY | — | ✅ |
| 14 | TransactionsEOCreationDate | CREATION_DATE | — | ✅ |
| 15 | TransactionsEOCstInvTransactionDtlId | CST_INV_TRANSACTION_DTL_ID | — | — |
| 16 | TransactionsEOCstInvTransactionId | CST_INV_TRANSACTION_ID | — | — |
| 17 | TransactionsEODooFullfillLineId | DOO_FULLFILL_LINE_ID | — | — |
| 18 | TransactionsEOErrorCode | ERROR_CODE | — | ✅ |
| 19 | TransactionsEOExpenseTransactionFlag | EXPENSE_TRANSACTION_FLAG | — | — |
| 20 | TransactionsEOFobPoint | FOB_POINT | — | ✅ |
| 21 | TransactionsEOInternalProfitTracking | INTERNAL_PROFIT_TRACKING | — | ✅ |
| 22 | TransactionsEOIntransitFlag | INTRANSIT_FLAG | — | ✅ |
| 23 | TransactionsEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 24 | TransactionsEOInventoryOrgId | INVENTORY_ORG_ID | — | — |
| 25 | TransactionsEOItemCostProfileId | ITEM_COST_PROFILE_ID | — | — |
| 26 | TransactionsEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 27 | TransactionsEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 28 | TransactionsEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 29 | TransactionsEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 30 | TransactionsEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 31 | TransactionsEOLogicalFlag | LOGICAL_FLAG | — | ✅ |
| 32 | TransactionsEOMatchedToCostFlag | MATCHED_TO_COST_FLAG | — | — |
| 33 | TransactionsEONegativeQtyCode | NEGATIVE_QTY_CODE | — | — |
| 34 | TransactionsEOOwningCostOrgId | OWNING_COST_ORG_ID | — | ✅ |
| 35 | TransactionsEOPoDistributionId | PO_DISTRIBUTION_ID | — | ✅ |
| 36 | TransactionsEOPostedFlag | POSTED_FLAG | — | ✅ |
| 37 | TransactionsEOPreprocessingStatus | PREPROCESSING_STATUS | — | ✅ |
| 38 | TransactionsEOPricingOption | PRICING_OPTION | — | ✅ |
| 39 | TransactionsEOProcessDate | PROCESS_DATE | — | ✅ |
| 40 | TransactionsEOQuantity | QUANTITY | — | ✅ |
| 41 | TransactionsEOQuantityFlowCode | QUANTITY_FLOW_CODE | — | — |
| 42 | TransactionsEORcvTransactionId | RCV_TRANSACTION_ID | — | — |
| 43 | TransactionsEORequestId | REQUEST_ID | — | — |
| 44 | TransactionsEORunMode | RUN_MODE | — | — |
| 45 | TransactionsEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 46 | TransactionsEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 47 | TransactionsEOTransactionFlowType | TRANSACTION_FLOW_TYPE | — | — |
| 48 | TransactionsEOTransactionId | TRANSACTION_ID | — | ✅ |
| 49 | TransactionsEOTransactionQty | TRANSACTION_QTY | — | ✅ |
| 50 | TransactionsEOTransactionUomCode | TRANSACTION_UOM_CODE | — | ✅ |
| 51 | TransactionsEOTransferBookId | TRANSFER_BOOK_ID | — | — |
| 52 | TransactionsEOTransferCostOrgId | TRANSFER_COST_ORG_ID | — | — |
| 53 | TransactionsEOTransferCstInvTxnId | TRANSFER_CST_INV_TXN_ID | — | — |
| 54 | TransactionsEOTransferPercentage | TRANSFER_PERCENTAGE | — | ✅ |
| 55 | TransactionsEOTransferValUnitId | TRANSFER_VAL_UNIT_ID | — | — |
| 56 | TransactionsEOTxnSourceDocNumber | TXN_SOURCE_DOC_NUMBER | — | ✅ |
| 57 | TransactionsEOTxnSourceDocType | TXN_SOURCE_DOC_TYPE | — | ✅ |
| 58 | TransactionsEOTxnSourceRefDocNumber | TXN_SOURCE_REF_DOC_NUMBER | — | ✅ |
| 59 | TransactionsEOTxnSourceRefDocType | TXN_SOURCE_REF_DOC_TYPE | — | ✅ |
| 60 | TransactionsEOUomCode | UOM_CODE | — | — |
| 61 | TransactionsEOUomConversionFactor | UOM_CONVERSION_FACTOR | — | ✅ |
| 62 | TransactionsEOUseItemCostFlag | USE_ITEM_COST_FLAG | — | — |
| 63 | TransactionsEOValStructureId | VAL_STRUCTURE_ID | — | ✅ |
| 64 | TransactionsEOValUnitCombinationId | VAL_UNIT_COMBINATION_ID | — | — |
| 65 | TransactionsEOValUnitDetailId | VAL_UNIT_DETAIL_ID | — | — |
| 66 | TransactionsEOValUnitId | VAL_UNIT_ID | — | — |
| 67 | TransactionsEOWshDeliveryDetailId | WSH_DELIVERY_DETAIL_ID | — | — |

### [[cst_transfer_costs|CST_TRANSFER_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstTransferCostsPEOAbsorptionType | ABSORPTION_TYPE | — | ✅ |
| 2 | CstTransferCostsPEOAdditionalProcessingCode | ADDITIONAL_PROCESSING_CODE | — | — |
| 3 | CstTransferCostsPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | — |
| 4 | CstTransferCostsPEOCostBookId | COST_BOOK_ID | — | — |
| 5 | CstTransferCostsPEOCostDate | COST_DATE | — | — |
| 6 | CstTransferCostsPEOCostElementId | COST_ELEMENT_ID | — | — |
| 7 | CstTransferCostsPEOCostOrgId | COST_ORG_ID | — | — |
| 8 | CstTransferCostsPEOCostTransactionType | COST_TRANSACTION_TYPE | — | — |
| 9 | CstTransferCostsPEOCreatedBy | CREATED_BY | — | — |
| 10 | CstTransferCostsPEOCreationDate | CREATION_DATE | — | — |
| 11 | CstTransferCostsPEOCurrencyCode | CURRENCY_CODE | — | — |
| 12 | CstTransferCostsPEODepTrxnId | DEP_TRXN_ID | — | — |
| 13 | CstTransferCostsPEODistributionId | DISTRIBUTION_ID | — | — |
| 14 | CstTransferCostsPEOEffDate | EFF_DATE | — | — |
| 15 | CstTransferCostsPEOExpensePoolId | EXPENSE_POOL_ID | — | ✅ |
| 16 | CstTransferCostsPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 17 | CstTransferCostsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 18 | CstTransferCostsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 19 | CstTransferCostsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | CstTransferCostsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | CstTransferCostsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 22 | CstTransferCostsPEOPostedFlag | POSTED_FLAG | — | — |
| 23 | CstTransferCostsPEOQuantity | QUANTITY | — | — |
| 24 | CstTransferCostsPEORecTrxnId | REC_TRXN_ID | — | — |
| 25 | CstTransferCostsPEORequestId | REQUEST_ID | — | — |
| 26 | CstTransferCostsPEOTransactionCostId | TRANSACTION_COST_ID | — | — |
| 27 | CstTransferCostsPEOTransactionId | TRANSACTION_ID | — | — |
| 28 | CstTransferCostsPEOTransferCostId | TRANSFER_COST_ID | — | — |
| 29 | CstTransferCostsPEOUnitCost | UNIT_COST | — | ✅ |
| 30 | CstTransferCostsPEOUomCode | UOM_CODE | — | — |
| 31 | CstTransferCostsPEOValUnitId | VAL_UNIT_ID | — | — |

### [[cst_val_units_tl|CST_VAL_UNITS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransferValUnitPEOLanguage | LANGUAGE | — | — |
| 2 | TransferValUnitPEOValUnitDesc | VAL_UNIT_DESC | — | ✅ |
| 3 | TransferValUnitPEOValUnitId | VAL_UNIT_ID | — | — |

### [[fnd_messages_vl|FND_MESSAGES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MessagePEOApplicationId | APPLICATION_ID | — | — |
| 2 | MessagePEOMessageName | MESSAGE_NAME | — | — |
| 3 | MessagePEOMessageText | MESSAGE_TEXT | — | — |

### [[gl_calendars|GL_CALENDARS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlCalendarsCalendarId | CALENDAR_ID | — | — |
| 2 | GlCalendarsPeriodSetId | PERIOD_SET_ID | — | — |
| 3 | GlCalendarsPeriodSetName | PERIOD_SET_NAME | — | — |
| 4 | GlCalendarsPeriodType | PERIOD_TYPE | — | — |
| 5 | GlCalendarsPeriodTypeId | PERIOD_TYPE_ID | — | — |
| 6 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[xla_event_classes_tl|XLA_EVENT_CLASSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventClassTranslationPEOApplicationId | APPLICATION_ID | — | ✅ |
| 2 | EventClassTranslationPEODescription | DESCRIPTION | — | — |
| 3 | EventClassTranslationPEOEntityCode | ENTITY_CODE | — | — |
| 4 | EventClassTranslationPEOEventClassCode | EVENT_CLASS_CODE | — | — |
| 5 | EventClassTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | EventClassTranslationPEOName | NAME | — | — |

### [[xla_event_types_tl|XLA_EVENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventTypeTranslationPEOApplicationId | APPLICATION_ID | — | — |
| 2 | EventTypeTranslationPEODescription | DESCRIPTION | — | — |
| 3 | EventTypeTranslationPEOEntityCode | ENTITY_CODE | — | — |
| 4 | EventTypeTranslationPEOEventClassCode | EVENT_CLASS_CODE | — | — |
| 5 | EventTypeTranslationPEOEventTypeCode | EVENT_TYPE_CODE | — | — |
| 6 | EventTypeTranslationPEOLanguage | LANGUAGE | — | — |
| 7 | EventTypeTranslationPEOName | NAME | — | — |

### [[xla_lookups|XLA_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcctLineTypeLookupPEODescription | DESCRIPTION | — | ✅ |
| 2 | AcctLineTypeLookupPEOLookupCode | LOOKUP_CODE | — | ✅ |
| 3 | AcctLineTypeLookupPEOLookupType | LOOKUP_TYPE | — | ✅ |
| 4 | AcctLineTypeLookupPEOMeaning | MEANING | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
