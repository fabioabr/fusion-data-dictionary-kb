---
id: DOC-AR-PVO-ReceiptAccountingPVO
doc_type: system-doc
title: "ReceiptAccountingPVO — PVO Accounts Receivable"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ar
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ReceiptAccountingPVO
  - receiptaccountingpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReceiptAccountingPVO

## 📌 Visão Geral

Extrai a contabilização de recebimentos de compras (receipt accounting), com eventos contábeis, distribuições e custos associados a ordens de compra. Permite reconciliar o recebimento físico de materiais com os lançamentos contábeis correspondentes.

**Caminho:** `FscmTopModelAM.ReceiptAccountingAM.ReceiptAccountingPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 241 | 20 | 1 | 89 | 37% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_purchase_order_dtls|CMR_PURCHASE_ORDER_DTLS]] — 11 atributos (3 BICC)
- [[cmr_rcv_distributions|CMR_RCV_DISTRIBUTIONS]] — 20 atributos (1 PKs, 11 BICC)
- [[cmr_rcv_events|CMR_RCV_EVENTS]] — 61 atributos (27 BICC)
- [[cmr_rcv_event_costs|CMR_RCV_EVENT_COSTS]] — 11 atributos (3 BICC)
- [[cmr_rcv_event_types|CMR_RCV_EVENT_TYPES]] — 1 atributos (1 BICC)
- [[cmr_r_rcv_transactions_v|CMR_R_RCV_TRANSACTIONS_V]] — 54 atributos (2 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 4 atributos
- [[inv_org_parameters_v|INV_ORG_PARAMETERS_V]] — 2 atributos
- [[inv_units_of_measure_vl|INV_UNITS_OF_MEASURE_VL]] — 4 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 12 atributos (8 BICC)
- [[por_requisition_headers_all|POR_REQUISITION_HEADERS_ALL]] — 2 atributos (1 BICC)
- [[por_requisition_lines_all|POR_REQUISITION_LINES_ALL]] — 2 atributos (1 BICC)
- [[po_distributions_all|PO_DISTRIBUTIONS_ALL]] — 8 atributos (6 BICC)
- [[po_headers_all|PO_HEADERS_ALL]] — 14 atributos (8 BICC)
- [[po_lines_all|PO_LINES_ALL]] — 12 atributos (10 BICC)
- [[po_line_locations_all|PO_LINE_LOCATIONS_ALL]] — 3 atributos (1 BICC)
- [[xla_event_classes_tl|XLA_EVENT_CLASSES_TL]] — 6 atributos
- [[xla_event_types_tl|XLA_EVENT_TYPES_TL]] — 7 atributos (4 BICC)
- [[xla_lookups|XLA_LOOKUPS]] — 4 atributos (1 BICC)
- [[xle_entity_profiles|XLE_ENTITY_PROFILES]] — 3 atributos

---

## ⚙️ Atributos

### [[cmr_purchase_order_dtls|CMR_PURCHASE_ORDER_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchaseOrderDtlsPEOAccrueOnReceiptFlag | ACCRUE_ON_RECEIPT_FLAG | — | — |
| 2 | PurchaseOrderDtlsPEOActiveFlag | ACTIVE_FLAG | — | — |
| 3 | PurchaseOrderDtlsPEOCmrPoDistributionId | CMR_PO_DISTRIBUTION_ID | — | — |
| 4 | PurchaseOrderDtlsPEODestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 5 | PurchaseOrderDtlsPEODistributionNumber | DISTRIBUTION_NUMBER | — | ✅ |
| 6 | PurchaseOrderDtlsPEOEventDate | EVENT_DATE | — | — |
| 7 | PurchaseOrderDtlsPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | — |
| 8 | PurchaseOrderDtlsPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 9 | PurchaseOrderDtlsPEOPoNumber | PO_NUMBER | — | ✅ |
| 10 | PurchaseOrderDtlsPEOVendorId | VENDOR_ID | — | — |
| 11 | PurchaseOrderDtlsPEOVendorSiteId | VENDOR_SITE_ID | — | — |

### [[cmr_rcv_distributions|CMR_RCV_DISTRIBUTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrSubLedgerId | CMR_SUB_LEDGER_ID | 🔑 | ✅ |
| 2 | ReceivingDistributionsEOAccountedQty | ACCOUNTED_QTY | — | ✅ |
| 3 | ReceivingDistributionsEOAccountingEventId | ACCOUNTING_EVENT_ID | — | — |
| 4 | ReceivingDistributionsEOAccountingLineType | ACCOUNTING_LINE_TYPE | — | ✅ |
| 5 | ReceivingDistributionsEOCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 6 | ReceivingDistributionsEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | ReceivingDistributionsEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | ReceivingDistributionsEOEnteredCurrencyAmount | ENTERED_CURRENCY_AMOUNT | — | ✅ |
| 9 | ReceivingDistributionsEOEnteredCurrencyCode | ENTERED_CURRENCY_CODE | — | ✅ |
| 10 | ReceivingDistributionsEOEventId | EVENT_ID | — | — |
| 11 | ReceivingDistributionsEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 12 | ReceivingDistributionsEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 13 | ReceivingDistributionsEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | ReceivingDistributionsEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | ReceivingDistributionsEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | ReceivingDistributionsEOLedgerAmount | LEDGER_AMOUNT | — | ✅ |
| 17 | ReceivingDistributionsEOLedgerCurrencyCode | LEDGER_CURRENCY_CODE | — | ✅ |
| 18 | ReceivingDistributionsEOLineNumber | LINE_NUMBER | — | — |
| 19 | ReceivingDistributionsEOPjcTxnStatusCode | PJC_TXN_STATUS_CODE | — | — |
| 20 | ReceivingDistributionsEORequestId | REQUEST_ID | — | — |

### [[cmr_rcv_events|CMR_RCV_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReceivingAccountingEventsEOAccountedFlag | ACCOUNTED_FLAG | — | ✅ |
| 2 | ReceivingAccountingEventsEOAccountingEventId | ACCOUNTING_EVENT_ID | — | — |
| 3 | ReceivingAccountingEventsEOBillToBusinessUnitId | BILL_TO_BUSINESS_UNIT_ID | — | — |
| 4 | ReceivingAccountingEventsEOBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 5 | ReceivingAccountingEventsEOCmrPoDistributionId | CMR_PO_DISTRIBUTION_ID | — | — |
| 6 | ReceivingAccountingEventsEOCmrRcvTransactionId | CMR_RCV_TRANSACTION_ID | — | — |
| 7 | ReceivingAccountingEventsEOConsignedFlag | CONSIGNED_FLAG | — | — |
| 8 | ReceivingAccountingEventsEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | ReceivingAccountingEventsEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | ReceivingAccountingEventsEODeliverToBusinessUnitId | DELIVER_TO_BUSINESS_UNIT_ID | — | — |
| 11 | ReceivingAccountingEventsEODeliverToInventoryOrgId | DELIVER_TO_INVENTORY_ORG_ID | — | — |
| 12 | ReceivingAccountingEventsEODestinationTypeCode | DESTINATION_TYPE_CODE | — | — |
| 13 | ReceivingAccountingEventsEODooFullfillLineId | DOO_FULLFILL_LINE_ID | — | — |
| 14 | ReceivingAccountingEventsEOEnteredCurrencyCode | ENTERED_CURRENCY_CODE | — | ✅ |
| 15 | ReceivingAccountingEventsEOEntityCode | ENTITY_CODE | — | — |
| 16 | ReceivingAccountingEventsEOEventClassCode | EVENT_CLASS_CODE | — | ✅ |
| 17 | ReceivingAccountingEventsEOEventId | EVENT_ID | — | — |
| 18 | ReceivingAccountingEventsEOEventSource | EVENT_SOURCE | — | — |
| 19 | ReceivingAccountingEventsEOEventSourceId | EVENT_SOURCE_ID | — | — |
| 20 | ReceivingAccountingEventsEOEventTypeCode | EVENT_TYPE_CODE | — | ✅ |
| 21 | ReceivingAccountingEventsEOExchangeDate | EXCHANGE_DATE | — | — |
| 22 | ReceivingAccountingEventsEOExchangeRate | EXCHANGE_RATE | — | — |
| 23 | ReceivingAccountingEventsEOExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 24 | ReceivingAccountingEventsEOGlDate | GL_DATE | — | ✅ |
| 25 | ReceivingAccountingEventsEOInvShippingTransactionId | INV_SHIPPING_TRANSACTION_ID | — | — |
| 26 | ReceivingAccountingEventsEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 27 | ReceivingAccountingEventsEOInventoryOrgId | INVENTORY_ORG_ID | — | — |
| 28 | ReceivingAccountingEventsEOInvoicedFlag | INVOICED_FLAG | — | — |
| 29 | ReceivingAccountingEventsEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 30 | ReceivingAccountingEventsEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 31 | ReceivingAccountingEventsEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | ReceivingAccountingEventsEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 33 | ReceivingAccountingEventsEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 34 | ReceivingAccountingEventsEOLedgerId | LEDGER_ID | — | — |
| 35 | ReceivingAccountingEventsEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 36 | ReceivingAccountingEventsEOMultiBuFlag | MULTI_BU_FLAG | — | — |
| 37 | ReceivingAccountingEventsEONonrecoverableTax | NONRECOVERABLE_TAX | — | ✅ |
| 38 | ReceivingAccountingEventsEOPoUnitPrice | PO_UNIT_PRICE | — | ✅ |
| 39 | ReceivingAccountingEventsEOPostedFlag | POSTED_FLAG | — | — |
| 40 | ReceivingAccountingEventsEOPrimaryQty | PRIMARY_QTY | — | ✅ |
| 41 | ReceivingAccountingEventsEOPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 42 | ReceivingAccountingEventsEOPriorBusinessUnitId | PRIOR_BUSINESS_UNIT_ID | — | — |
| 43 | ReceivingAccountingEventsEOPriorInventoryOrgId | PRIOR_INVENTORY_ORG_ID | — | — |
| 44 | ReceivingAccountingEventsEOProcessingGroupId | PROCESSING_GROUP_ID | — | — |
| 45 | ReceivingAccountingEventsEOProcurementOrgFlag | PROCUREMENT_ORG_FLAG | — | — |
| 46 | ReceivingAccountingEventsEORequestId | REQUEST_ID | — | — |
| 47 | ReceivingAccountingEventsEOSlaTransactionNumber | SLA_TRANSACTION_NUMBER | — | ✅ |
| 48 | ReceivingAccountingEventsEOSourceDocNumber | SOURCE_DOC_NUMBER | — | ✅ |
| 49 | ReceivingAccountingEventsEOSourceDocQty | SOURCE_DOC_QTY | — | ✅ |
| 50 | ReceivingAccountingEventsEOSourceDocUomCode | SOURCE_DOC_UOM_CODE | — | ✅ |
| 51 | ReceivingAccountingEventsEOTradeEventId | TRADE_EVENT_ID | — | — |
| 52 | ReceivingAccountingEventsEOTransactionAmt | TRANSACTION_AMT | — | ✅ |
| 53 | ReceivingAccountingEventsEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 54 | ReceivingAccountingEventsEOTransactionQty | TRANSACTION_QTY | — | ✅ |
| 55 | ReceivingAccountingEventsEOTransactionUomCode | TRANSACTION_UOM_CODE | — | ✅ |
| 56 | ReceivingAccountingEventsEOTransferPrice | TRANSFER_PRICE | — | ✅ |
| 57 | ReceivingAccountingEventsEOTropChargeLineId | TROP_CHARGE_LINE_ID | — | — |
| 58 | ReceivingAccountingEventsEOTxnFlowHeaderId | TXN_FLOW_HEADER_ID | — | — |
| 59 | ReceivingAccountingEventsPEOBudgetaryControlFlag | BUDGETARY_CONTROL_FLAG | — | ✅ |
| 60 | ReceivingAccountingEventsPEOEncumbranceAccountingFlag | ENCUMBRANCE_ACCOUNTING_FLAG | — | ✅ |
| 61 | ReceivingAccountingEventsPEOFundReservationStatus | FUND_RESERVATION_STATUS | — | ✅ |

### [[cmr_rcv_event_costs|CMR_RCV_EVENT_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrRcvEventCostsPEOCrossBuFlag | CROSS_BU_FLAG | — | — |
| 2 | CmrRcvEventCostsPEOCurrencyCode | CURRENCY_CODE | — | — |
| 3 | CmrRcvEventCostsPEOCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | — |
| 4 | CmrRcvEventCostsPEOCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | — |
| 5 | CmrRcvEventCostsPEOCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | — |
| 6 | CmrRcvEventCostsPEODestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 7 | CmrRcvEventCostsPEOEventCostId | EVENT_COST_ID | — | — |
| 8 | CmrRcvEventCostsPEOEventCostSource | EVENT_COST_SOURCE | — | — |
| 9 | CmrRcvEventCostsPEOEventCostSourceType | EVENT_COST_SOURCE_TYPE | — | ✅ |
| 10 | CmrRcvEventCostsPEOEventUnitCost | EVENT_UNIT_COST | — | ✅ |
| 11 | CmrRcvEventCostsPEOProcurementBuFlag | PROCUREMENT_BU_FLAG | — | — |

### [[cmr_rcv_event_types|CMR_RCV_EVENT_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RcvEventTypesPEOTransactionType | TRANSACTION_TYPE | — | ✅ |

### [[cmr_r_rcv_transactions_v|CMR_R_RCV_TRANSACTIONS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrRcvTransactionRptPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | CmrRcvTransactionRptPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | CmrRcvTransactionRptPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | CmrRcvTransactionRptPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | CmrRcvTransactionRptPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | CmrRcvTransactionRptPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | CmrRcvTransactionRptPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | CmrRcvTransactionRptPEOAttribute2 | ATTRIBUTE2 | — | — |
| 9 | CmrRcvTransactionRptPEOAttribute3 | ATTRIBUTE3 | — | — |
| 10 | CmrRcvTransactionRptPEOAttribute4 | ATTRIBUTE4 | — | — |
| 11 | CmrRcvTransactionRptPEOAttribute5 | ATTRIBUTE5 | — | — |
| 12 | CmrRcvTransactionRptPEOAttribute6 | ATTRIBUTE6 | — | — |
| 13 | CmrRcvTransactionRptPEOAttribute7 | ATTRIBUTE7 | — | — |
| 14 | CmrRcvTransactionRptPEOAttribute8 | ATTRIBUTE8 | — | — |
| 15 | CmrRcvTransactionRptPEOAttribute9 | ATTRIBUTE9 | — | — |
| 16 | CmrRcvTransactionRptPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | CmrRcvTransactionRptPEOCmrSubLedgerId1 | CMR_SUB_LEDGER_ID | — | — |
| 18 | CmrRcvTransactionRptPEOPjcBillableFlag | PJC_BILLABLE_FLAG | — | — |
| 19 | CmrRcvTransactionRptPEOPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | — |
| 20 | CmrRcvTransactionRptPEOPjcContextCategory | PJC_CONTEXT_CATEGORY | — | — |
| 21 | CmrRcvTransactionRptPEOPjcContractId | PJC_CONTRACT_ID | — | — |
| 22 | CmrRcvTransactionRptPEOPjcContractLineId | PJC_CONTRACT_LINE_ID | — | — |
| 23 | CmrRcvTransactionRptPEOPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 24 | CmrRcvTransactionRptPEOPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | — |
| 25 | CmrRcvTransactionRptPEOPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | — |
| 26 | CmrRcvTransactionRptPEOPjcInterfacedStatus | PJC_INTERFACED_STATUS | — | — |
| 27 | CmrRcvTransactionRptPEOPjcOrganizationId | PJC_ORGANIZATION_ID | — | — |
| 28 | CmrRcvTransactionRptPEOPjcProjectId | PJC_PROJECT_ID | — | — |
| 29 | CmrRcvTransactionRptPEOPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 30 | CmrRcvTransactionRptPEOPjcReservedAttribute10 | PJC_RESERVED_ATTRIBUTE10 | — | — |
| 31 | CmrRcvTransactionRptPEOPjcReservedAttribute2 | PJC_RESERVED_ATTRIBUTE2 | — | — |
| 32 | CmrRcvTransactionRptPEOPjcReservedAttribute3 | PJC_RESERVED_ATTRIBUTE3 | — | — |
| 33 | CmrRcvTransactionRptPEOPjcReservedAttribute4 | PJC_RESERVED_ATTRIBUTE4 | — | — |
| 34 | CmrRcvTransactionRptPEOPjcReservedAttribute5 | PJC_RESERVED_ATTRIBUTE5 | — | — |
| 35 | CmrRcvTransactionRptPEOPjcReservedAttribute6 | PJC_RESERVED_ATTRIBUTE6 | — | — |
| 36 | CmrRcvTransactionRptPEOPjcReservedAttribute7 | PJC_RESERVED_ATTRIBUTE7 | — | — |
| 37 | CmrRcvTransactionRptPEOPjcReservedAttribute8 | PJC_RESERVED_ATTRIBUTE8 | — | — |
| 38 | CmrRcvTransactionRptPEOPjcReservedAttribute9 | PJC_RESERVED_ATTRIBUTE9 | — | — |
| 39 | CmrRcvTransactionRptPEOPjcTaskId | PJC_TASK_ID | — | — |
| 40 | CmrRcvTransactionRptPEOPjcTxnStatusCode | PJC_TXN_STATUS_CODE | — | — |
| 41 | CmrRcvTransactionRptPEOPjcUserDefAttribute1 | PJC_USER_DEF_ATTRIBUTE1 | — | — |
| 42 | CmrRcvTransactionRptPEOPjcUserDefAttribute10 | PJC_USER_DEF_ATTRIBUTE10 | — | — |
| 43 | CmrRcvTransactionRptPEOPjcUserDefAttribute2 | PJC_USER_DEF_ATTRIBUTE2 | — | — |
| 44 | CmrRcvTransactionRptPEOPjcUserDefAttribute3 | PJC_USER_DEF_ATTRIBUTE3 | — | — |
| 45 | CmrRcvTransactionRptPEOPjcUserDefAttribute4 | PJC_USER_DEF_ATTRIBUTE4 | — | — |
| 46 | CmrRcvTransactionRptPEOPjcUserDefAttribute5 | PJC_USER_DEF_ATTRIBUTE5 | — | — |
| 47 | CmrRcvTransactionRptPEOPjcUserDefAttribute6 | PJC_USER_DEF_ATTRIBUTE6 | — | — |
| 48 | CmrRcvTransactionRptPEOPjcUserDefAttribute7 | PJC_USER_DEF_ATTRIBUTE7 | — | — |
| 49 | CmrRcvTransactionRptPEOPjcUserDefAttribute8 | PJC_USER_DEF_ATTRIBUTE8 | — | — |
| 50 | CmrRcvTransactionRptPEOPjcUserDefAttribute9 | PJC_USER_DEF_ATTRIBUTE9 | — | — |
| 51 | CmrRcvTransactionRptPEOPjcWorkTypeId | PJC_WORK_TYPE_ID | — | — |
| 52 | CmrRcvTransactionRptPEOReceiptLineNumber | RECEIPT_LINE_NUMBER | — | — |
| 53 | CmrRcvTransactionRptPEOReceiptNumber | RECEIPT_NUMBER | — | ✅ |
| 54 | CmrRcvTransactionRptPEOTransactionDate | TRANSACTION_DATE | — | ✅ |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillToBusinessUnitPEOBusinessUnitId | BU_ID | — | — |
| 2 | BillToBusinessUnitPEOName | BU_NAME | — | — |
| 3 | BusinessUnitPEOBusinessUnitId | BU_ID | — | — |
| 4 | BusinessUnitPEOName | BU_NAME | — | — |

### [[inv_org_parameters_v|INV_ORG_PARAMETERS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MtlParametersAllOrganizationCode | ORGANIZATION_CODE | — | — |
| 2 | MtlParametersAllOrganizationId | ORGANIZATION_ID | — | — |

### [[inv_units_of_measure_vl|INV_UNITS_OF_MEASURE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 2 | UnitOfMeasurePEOUomCode | UOM_CODE | — | — |
| 3 | UomDescription | DESCRIPTION | — | ✅ |
| 4 | UomUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonNameId | PERSON_NAME_ID | — | — |
| 4 | PersonNamePEODisplayName | DISPLAY_NAME | — | ✅ |
| 5 | PersonNamePEOFirstName | FIRST_NAME | — | ✅ |
| 6 | PersonNamePEOFullName | FULL_NAME | — | ✅ |
| 7 | PersonNamePEOLastName | LAST_NAME | — | ✅ |
| 8 | PersonNamePEOTitle | TITLE | — | ✅ |
| 9 | SupervisorNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 10 | SupervisorNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 11 | SupervisorNamePEOFullName | FULL_NAME | — | ✅ |
| 12 | SupervisorNamePEOPersonNameId | PERSON_NAME_ID | — | — |

### [[por_requisition_headers_all|POR_REQUISITION_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequisitionHeaderPEORequisitionHeaderId | REQUISITION_HEADER_ID | — | — |
| 2 | RequisitionHeaderPEORequisitionNumber | REQUISITION_NUMBER | — | ✅ |

### [[por_requisition_lines_all|POR_REQUISITION_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequisitionLinePEOLineNumber | LINE_NUMBER | — | ✅ |
| 2 | RequisitionLinePEORequisitionLineId | REQUISITION_LINE_ID | — | — |

### [[po_distributions_all|PO_DISTRIBUTIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 2 | PoDistributionId | PO_DISTRIBUTION_ID | — | — |
| 3 | PurchaseOrderDistributionDistributionNum | DISTRIBUTION_NUM | — | ✅ |
| 4 | PurchaseOrderDistributionRate | RATE | — | ✅ |
| 5 | PurchaseOrderDistributionRateDate | RATE_DATE | — | ✅ |
| 6 | PurchaseOrderDistributionReqDistributionId | REQ_DISTRIBUTION_ID | — | ✅ |
| 7 | PurchaseOrderDistributionReqHeaderReferenceNum | REQ_HEADER_REFERENCE_NUM | — | ✅ |
| 8 | PurchaseOrderDistributionReqLineReferenceNum | REQ_LINE_REFERENCE_NUM | — | ✅ |

### [[po_headers_all|PO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BlanketHeaderPEOPoHeaderId | PO_HEADER_ID | — | — |
| 2 | ContractHeaderPEOPoHeaderId | PO_HEADER_ID | — | — |
| 3 | ContractHeaderSegment1 | SEGMENT1 | — | ✅ |
| 4 | FromBlanketHeaderSegment1 | SEGMENT1 | — | ✅ |
| 5 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | ObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 7 | ObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |
| 8 | PoHeaderId | PO_HEADER_ID | — | — |
| 9 | PurchasingDocumentHeaderComments | COMMENTS | — | ✅ |
| 10 | PurchasingDocumentHeaderConfirmingOrderFlag | CONFIRMING_ORDER_FLAG | — | ✅ |
| 11 | PurchasingDocumentHeaderCurrencyCode | CURRENCY_CODE | — | ✅ |
| 12 | PurchasingDocumentHeaderReferenceNum | REFERENCE_NUM | — | ✅ |
| 13 | PurchasingDocumentHeaderSegment1 | SEGMENT1 | — | ✅ |
| 14 | PurchasingDocumentHeaderVendorOrderNum | VENDOR_ORDER_NUM | — | ✅ |

### [[po_lines_all|PO_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 2 | PoLineId | PO_LINE_ID | — | — |
| 3 | PurchasingDocumentLineCancelDate | CANCEL_DATE | — | ✅ |
| 4 | PurchasingDocumentLineCancelReason | CANCEL_REASON | — | ✅ |
| 5 | PurchasingDocumentLineCancelledBy | CANCELLED_BY | — | ✅ |
| 6 | PurchasingDocumentLineContractId | CONTRACT_ID | — | ✅ |
| 7 | PurchasingDocumentLineFromHeaderId | FROM_HEADER_ID | — | ✅ |
| 8 | PurchasingDocumentLineItemRevision | ITEM_REVISION | — | ✅ |
| 9 | PurchasingDocumentLineLineNum | LINE_NUM | — | ✅ |
| 10 | PurchasingDocumentLineLineReferenceNum | LINE_REFERENCE_NUM | — | ✅ |
| 11 | PurchasingDocumentLineLineStatus | LINE_STATUS | — | ✅ |
| 12 | PurchasingDocumentLineUomCode | UOM_CODE | — | ✅ |

### [[po_line_locations_all|PO_LINE_LOCATIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LineLocationId | LINE_LOCATION_ID | — | — |
| 2 | ObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 3 | PurchasingDocumentShipmentShipmentNum | SHIPMENT_NUM | — | ✅ |

### [[xla_event_classes_tl|XLA_EVENT_CLASSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventClassTranslationPEOApplicationId | APPLICATION_ID | — | — |
| 2 | EventClassTranslationPEODescription | DESCRIPTION | — | — |
| 3 | EventClassTranslationPEOEntityCode | ENTITY_CODE | — | — |
| 4 | EventClassTranslationPEOEventClassCode | EVENT_CLASS_CODE | — | — |
| 5 | EventClassTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | EventClassTranslationPEOName | NAME | — | — |

### [[xla_event_types_tl|XLA_EVENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventTypeTranslationPEOApplicationId | APPLICATION_ID | — | — |
| 2 | EventTypeTranslationPEODescription | DESCRIPTION | — | ✅ |
| 3 | EventTypeTranslationPEOEntityCode | ENTITY_CODE | — | — |
| 4 | EventTypeTranslationPEOEventClassCode | EVENT_CLASS_CODE | — | ✅ |
| 5 | EventTypeTranslationPEOEventTypeCode | EVENT_TYPE_CODE | — | ✅ |
| 6 | EventTypeTranslationPEOLanguage | LANGUAGE | — | — |
| 7 | EventTypeTranslationPEOName | NAME | — | ✅ |

### [[xla_lookups|XLA_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcctLineTypeLookupPEODescription | DESCRIPTION | — | — |
| 2 | AcctLineTypeLookupPEOLookupCode | LOOKUP_CODE | — | — |
| 3 | AcctLineTypeLookupPEOLookupType | LOOKUP_TYPE | — | — |
| 4 | AcctLineTypeLookupPEOMeaning | MEANING | — | ✅ |

### [[xle_entity_profiles|XLE_ENTITY_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | XleEntityProfilesLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 2 | XleEntityProfilesName | NAME | — | — |
| 3 | XleEntityProfilesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
