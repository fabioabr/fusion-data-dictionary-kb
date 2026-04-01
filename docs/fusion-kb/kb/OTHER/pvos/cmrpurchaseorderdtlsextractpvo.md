---
id: DOC-OTHER-PVO-CmrPurchaseOrderDtlsExtractPVO
doc_type: system-doc
title: "CmrPurchaseOrderDtlsExtractPVO — PVO Cross-Module"
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
  - CmrPurchaseOrderDtlsExtractPVO
  - cmrpurchaseorderdtlsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrPurchaseOrderDtlsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cmr Purchase Order Dtls Extract. Acessa as tabelas: CMR_PURCHASE_ORDER_DTLS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CmrBiccExtractAM.CmrPurchaseOrderDtlsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 94 | 1 | 3 | 94 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_purchase_order_dtls|CMR_PURCHASE_ORDER_DTLS]] — 94 atributos (3 PKs, 94 BICC)

---

## ⚙️ Atributos

### [[cmr_purchase_order_dtls|CMR_PURCHASE_ORDER_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrPurchaseOrderDtlsPEOAccrualAccountId | ACCRUAL_ACCOUNT_ID | — | ✅ |
| 2 | CmrPurchaseOrderDtlsPEOAccrueOnReceiptFlag | ACCRUE_ON_RECEIPT_FLAG | — | ✅ |
| 3 | CmrPurchaseOrderDtlsPEOActiveFlag | ACTIVE_FLAG | — | ✅ |
| 4 | CmrPurchaseOrderDtlsPEOActiveForCaFlag | ACTIVE_FOR_CA_FLAG | — | ✅ |
| 5 | CmrPurchaseOrderDtlsPEOAgentId | AGENT_ID | — | ✅ |
| 6 | CmrPurchaseOrderDtlsPEOAmountCancelled | AMOUNT_CANCELLED | — | ✅ |
| 7 | CmrPurchaseOrderDtlsPEOAmountOrdered | AMOUNT_ORDERED | — | ✅ |
| 8 | CmrPurchaseOrderDtlsPEOBillToBusinessUnitId | BILL_TO_BUSINESS_UNIT_ID | — | ✅ |
| 9 | CmrPurchaseOrderDtlsPEOBillToLocationId | BILL_TO_LOCATION_ID | — | ✅ |
| 10 | CmrPurchaseOrderDtlsPEOCategoryId | CATEGORY_ID | — | ✅ |
| 11 | CmrPurchaseOrderDtlsPEOChargeAccountId | CHARGE_ACCOUNT_ID | — | ✅ |
| 12 | CmrPurchaseOrderDtlsPEOCmrPoDistributionId | CMR_PO_DISTRIBUTION_ID | — | ✅ |
| 13 | CmrPurchaseOrderDtlsPEOCmrPoLineLocationId | CMR_PO_LINE_LOCATION_ID | — | ✅ |
| 14 | CmrPurchaseOrderDtlsPEOConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 15 | CmrPurchaseOrderDtlsPEOConvFactorToPrimaryUom | CONV_FACTOR_TO_PRIMARY_UOM | — | ✅ |
| 16 | CmrPurchaseOrderDtlsPEOCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | ✅ |
| 17 | CmrPurchaseOrderDtlsPEOCreatedBy | CREATED_BY | — | ✅ |
| 18 | CmrPurchaseOrderDtlsPEOCreationDate | CREATION_DATE | — | ✅ |
| 19 | CmrPurchaseOrderDtlsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 20 | CmrPurchaseOrderDtlsPEOCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 21 | CmrPurchaseOrderDtlsPEOCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 22 | CmrPurchaseOrderDtlsPEOCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 23 | CmrPurchaseOrderDtlsPEODefaultInventoryOrgId | DEFAULT_INVENTORY_ORG_ID | — | ✅ |
| 24 | CmrPurchaseOrderDtlsPEODeliverToBuFuncCurrCode | DELIVER_TO_BU_FUNC_CURR_CODE | — | ✅ |
| 25 | CmrPurchaseOrderDtlsPEODeliverToBusinessUnitId | DELIVER_TO_BUSINESS_UNIT_ID | — | ✅ |
| 26 | CmrPurchaseOrderDtlsPEODeliverToInventoryOrgId | DELIVER_TO_INVENTORY_ORG_ID | — | ✅ |
| 27 | CmrPurchaseOrderDtlsPEODestinationChargeAccountId | DESTINATION_CHARGE_ACCOUNT_ID | — | ✅ |
| 28 | CmrPurchaseOrderDtlsPEODestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 29 | CmrPurchaseOrderDtlsPEODestinationVarianceAcctId | DESTINATION_VARIANCE_ACCT_ID | — | ✅ |
| 30 | CmrPurchaseOrderDtlsPEODistributionNumber | DISTRIBUTION_NUMBER | — | ✅ |
| 31 | CmrPurchaseOrderDtlsPEOEventDate | EVENT_DATE | 🔑 | ✅ |
| 32 | CmrPurchaseOrderDtlsPEOEventType | EVENT_TYPE | — | ✅ |
| 33 | CmrPurchaseOrderDtlsPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | 🔑 | ✅ |
| 34 | CmrPurchaseOrderDtlsPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | 🔑 | ✅ |
| 35 | CmrPurchaseOrderDtlsPEOFobLookupCode | FOB_LOOKUP_CODE | — | ✅ |
| 36 | CmrPurchaseOrderDtlsPEOIntendedUse | INTENDED_USE | — | ✅ |
| 37 | CmrPurchaseOrderDtlsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 38 | CmrPurchaseOrderDtlsPEOItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 39 | CmrPurchaseOrderDtlsPEOLastRunPeriodId | LAST_RUN_PERIOD_ID | — | ✅ |
| 40 | CmrPurchaseOrderDtlsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 41 | CmrPurchaseOrderDtlsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 42 | CmrPurchaseOrderDtlsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 43 | CmrPurchaseOrderDtlsPEOLeTimezoneCode | LE_TIMEZONE_CODE | — | ✅ |
| 44 | CmrPurchaseOrderDtlsPEOLineNumber | LINE_NUMBER | — | ✅ |
| 45 | CmrPurchaseOrderDtlsPEOMatchOption | MATCH_OPTION | — | ✅ |
| 46 | CmrPurchaseOrderDtlsPEONeedByDate | NEED_BY_DATE | — | ✅ |
| 47 | CmrPurchaseOrderDtlsPEONonrecoverableInclusiveTax | NONRECOVERABLE_INCLUSIVE_TAX | — | ✅ |
| 48 | CmrPurchaseOrderDtlsPEONonrecoverableTax | NONRECOVERABLE_TAX | — | ✅ |
| 49 | CmrPurchaseOrderDtlsPEONrTaxInPrimaryUom | NR_TAX_IN_PRIMARY_UOM | — | ✅ |
| 50 | CmrPurchaseOrderDtlsPEOOrchestrationOrderFlag | ORCHESTRATION_ORDER_FLAG | — | ✅ |
| 51 | CmrPurchaseOrderDtlsPEOPaymentType | PAYMENT_TYPE | — | ✅ |
| 52 | CmrPurchaseOrderDtlsPEOPeriodEndAccruedFlag | PERIOD_END_ACCRUED_FLAG | — | ✅ |
| 53 | CmrPurchaseOrderDtlsPEOPoHeaderId | PO_HEADER_ID | — | ✅ |
| 54 | CmrPurchaseOrderDtlsPEOPoLineId | PO_LINE_ID | — | ✅ |
| 55 | CmrPurchaseOrderDtlsPEOPoLineLocationId | PO_LINE_LOCATION_ID | — | ✅ |
| 56 | CmrPurchaseOrderDtlsPEOPoNumber | PO_NUMBER | — | ✅ |
| 57 | CmrPurchaseOrderDtlsPEOPoPurchaseBasis | PO_PURCHASE_BASIS | — | ✅ |
| 58 | CmrPurchaseOrderDtlsPEOPrice | PRICE | — | ✅ |
| 59 | CmrPurchaseOrderDtlsPEOPriceInPrimaryUom | PRICE_IN_PRIMARY_UOM | — | ✅ |
| 60 | CmrPurchaseOrderDtlsPEOProcessedByCaFlag | PROCESSED_BY_CA_FLAG | — | ✅ |
| 61 | CmrPurchaseOrderDtlsPEOProcessedByRaFlag | PROCESSED_BY_RA_FLAG | — | ✅ |
| 62 | CmrPurchaseOrderDtlsPEOProcurementBusinessUnitId | PROCUREMENT_BUSINESS_UNIT_ID | — | ✅ |
| 63 | CmrPurchaseOrderDtlsPEOProductFiscalClassification | PRODUCT_FISCAL_CLASSIFICATION | — | ✅ |
| 64 | CmrPurchaseOrderDtlsPEOPromisedDate | PROMISED_DATE | — | ✅ |
| 65 | CmrPurchaseOrderDtlsPEOPurchaseBasis | PURCHASE_BASIS | — | ✅ |
| 66 | CmrPurchaseOrderDtlsPEOQuantityCancelled | QUANTITY_CANCELLED | — | ✅ |
| 67 | CmrPurchaseOrderDtlsPEOQuantityOrdered | QUANTITY_ORDERED | — | ✅ |
| 68 | CmrPurchaseOrderDtlsPEORecoverableInclusiveTax | RECOVERABLE_INCLUSIVE_TAX | — | ✅ |
| 69 | CmrPurchaseOrderDtlsPEORecoverableTax | RECOVERABLE_TAX | — | ✅ |
| 70 | CmrPurchaseOrderDtlsPEORequisitioningBuId | REQUISITIONING_BU_ID | — | ✅ |
| 71 | CmrPurchaseOrderDtlsPEOScheduleStatus | SCHEDULE_STATUS | — | ✅ |
| 72 | CmrPurchaseOrderDtlsPEOSecondaryQtyCancelled | SECONDARY_QTY_CANCELLED | — | ✅ |
| 73 | CmrPurchaseOrderDtlsPEOSecondaryQuantity | SECONDARY_QUANTITY | — | ✅ |
| 74 | CmrPurchaseOrderDtlsPEOSecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 75 | CmrPurchaseOrderDtlsPEOSfoPrimaryTradeRelationId | SFO_PRIMARY_TRADE_RELATION_ID | — | ✅ |
| 76 | CmrPurchaseOrderDtlsPEOShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 77 | CmrPurchaseOrderDtlsPEOShipmentNumber | SHIPMENT_NUMBER | — | ✅ |
| 78 | CmrPurchaseOrderDtlsPEOSoldToLegalEntityId | SOLD_TO_LEGAL_ENTITY_ID | — | ✅ |
| 79 | CmrPurchaseOrderDtlsPEOStatusUpdateDate | STATUS_UPDATE_DATE | — | ✅ |
| 80 | CmrPurchaseOrderDtlsPEOSupplierItem | SUPPLIER_ITEM | — | ✅ |
| 81 | CmrPurchaseOrderDtlsPEOTaxExclusivePrice | TAX_EXCLUSIVE_PRICE | — | ✅ |
| 82 | CmrPurchaseOrderDtlsPEOTradeOrgBuFuncCurrCode | TRADE_ORG_BU_FUNC_CURR_CODE | — | ✅ |
| 83 | CmrPurchaseOrderDtlsPEOTradeOrgProfitCenterBuId | TRADE_ORG_PROFIT_CENTER_BU_ID | — | ✅ |
| 84 | CmrPurchaseOrderDtlsPEOTradeOrganizationId | TRADE_ORGANIZATION_ID | — | ✅ |
| 85 | CmrPurchaseOrderDtlsPEOUomCode | UOM_CODE | — | ✅ |
| 86 | CmrPurchaseOrderDtlsPEOUseForGpFlag | USE_FOR_GP_FLAG | — | ✅ |
| 87 | CmrPurchaseOrderDtlsPEOVarianceAccountId | VARIANCE_ACCOUNT_ID | — | ✅ |
| 88 | CmrPurchaseOrderDtlsPEOVendorId | VENDOR_ID | — | ✅ |
| 89 | CmrPurchaseOrderDtlsPEOVendorSiteId | VENDOR_SITE_ID | — | ✅ |
| 90 | CmrPurchaseOrderDtlsPEOWoOperationSeqNumber | WO_OPERATION_SEQ_NUMBER | — | ✅ |
| 91 | CmrPurchaseOrderDtlsPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |
| 92 | CmrPurchaseOrderDtlsPEOWorkOrderNumber | WORK_ORDER_NUMBER | — | ✅ |
| 93 | CmrPurchaseOrderDtlsPEOWorkOrderOperationId | WORK_ORDER_OPERATION_ID | — | ✅ |
| 94 | CmrPurchaseOrderDtlsPEOWorkOrderProduct | WORK_ORDER_PRODUCT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
