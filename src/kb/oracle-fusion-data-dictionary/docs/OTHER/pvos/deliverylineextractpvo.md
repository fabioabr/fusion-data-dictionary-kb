---
id: DOC-OTHER-PVO-DeliveryLineExtractPVO
doc_type: system-doc
title: "DeliveryLineExtractPVO — PVO Cross-Module"
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
  - DeliveryLineExtractPVO
  - deliverylineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DeliveryLineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Delivery Line Extract. Acessa as tabelas: WSH_DELIVERY_DETAILS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.WshBiccExtractAM.DeliveryLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 168 | 1 | 1 | 168 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wsh_delivery_details|WSH_DELIVERY_DETAILS]] — 168 atributos (1 PKs, 168 BICC)

---

## ⚙️ Atributos

### [[wsh_delivery_details|WSH_DELIVERY_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeliveryLinePEOAllowItemSubstitutionFlag | ALLOW_ITEM_SUBSTITUTION_FLAG | — | ✅ |
| 2 | DeliveryLinePEOAssessableValue | ASSESSABLE_VALUE | — | ✅ |
| 3 | DeliveryLinePEOBaseItemId | BASE_ITEM_ID | — | ✅ |
| 4 | DeliveryLinePEOBatchId | BATCH_ID | — | ✅ |
| 5 | DeliveryLinePEOBillToContactId | BILL_TO_CONTACT_ID | — | ✅ |
| 6 | DeliveryLinePEOBillToLocationId | BILL_TO_LOCATION_ID | — | ✅ |
| 7 | DeliveryLinePEOBillToPartyId | BILL_TO_PARTY_ID | — | ✅ |
| 8 | DeliveryLinePEOBillToPartySiteId | BILL_TO_PARTY_SITE_ID | — | ✅ |
| 9 | DeliveryLinePEOCalcWndWddDate | CALC_WND_WDD_DATE | — | ✅ |
| 10 | DeliveryLinePEOCancelledQuantity | CANCELLED_QUANTITY | — | ✅ |
| 11 | DeliveryLinePEOCancelledQuantity2 | CANCELLED_QUANTITY2 | — | ✅ |
| 12 | DeliveryLinePEOCarrierId | CARRIER_ID | — | ✅ |
| 13 | DeliveryLinePEOCategoryId | CATEGORY_ID | — | ✅ |
| 14 | DeliveryLinePEOConversionDate | CONVERSION_DATE | — | ✅ |
| 15 | DeliveryLinePEOConversionRate | CONVERSION_RATE | — | ✅ |
| 16 | DeliveryLinePEOConversionType | CONVERSION_TYPE | — | ✅ |
| 17 | DeliveryLinePEOConvertedQuantity | CONVERTED_QUANTITY | — | ✅ |
| 18 | DeliveryLinePEOConvertedQuantity2 | CONVERTED_QUANTITY2 | — | ✅ |
| 19 | DeliveryLinePEOConvertedRequestedQuantity | CONVERTED_REQUESTED_QUANTITY | — | ✅ |
| 20 | DeliveryLinePEOCreatedBy | CREATED_BY | — | ✅ |
| 21 | DeliveryLinePEOCreationDate | CREATION_DATE | — | ✅ |
| 22 | DeliveryLinePEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 23 | DeliveryLinePEOCustPoNumber | CUST_PO_NUMBER | — | ✅ |
| 24 | DeliveryLinePEOCustomerItemId | CUSTOMER_ITEM_ID | — | ✅ |
| 25 | DeliveryLinePEOCycleCountQuantity | CYCLE_COUNT_QUANTITY | — | ✅ |
| 26 | DeliveryLinePEOCycleCountQuantity2 | CYCLE_COUNT_QUANTITY2 | — | ✅ |
| 27 | DeliveryLinePEODateRequested | DATE_REQUESTED | — | ✅ |
| 28 | DeliveryLinePEODateScheduled | DATE_SCHEDULED | — | ✅ |
| 29 | DeliveryLinePEODefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | ✅ |
| 30 | DeliveryLinePEODeliveredQuantity | DELIVERED_QUANTITY | — | ✅ |
| 31 | DeliveryLinePEODeliveredQuantity2 | DELIVERED_QUANTITY2 | — | ✅ |
| 32 | DeliveryLinePEODeliveryDetailId | DELIVERY_DETAIL_ID | 🔑 | ✅ |
| 33 | DeliveryLinePEODetailContainerItemId | DETAIL_CONTAINER_ITEM_ID | — | ✅ |
| 34 | DeliveryLinePEODoNotShipAfterDate | DO_NOT_SHIP_AFTER_DATE | — | ✅ |
| 35 | DeliveryLinePEODoNotShipBeforeDate | DO_NOT_SHIP_BEFORE_DATE | — | ✅ |
| 36 | DeliveryLinePEODocumentSubType | DOCUMENT_SUB_TYPE | — | ✅ |
| 37 | DeliveryLinePEOEarliestDropoffDate | EARLIEST_DROPOFF_DATE | — | ✅ |
| 38 | DeliveryLinePEOEarliestPickupDate | EARLIEST_PICKUP_DATE | — | ✅ |
| 39 | DeliveryLinePEOEndAssemblyItemNumber | END_ASSEMBLY_ITEM_NUMBER | — | ✅ |
| 40 | DeliveryLinePEOExemptCertificateNumber | EXEMPT_CERTIFICATE_NUMBER | — | ✅ |
| 41 | DeliveryLinePEOExemptReasonCode | EXEMPT_REASON_CODE | — | ✅ |
| 42 | DeliveryLinePEOFinalDischargeLocationId | FINAL_DISCHARGE_LOCATION_ID | — | ✅ |
| 43 | DeliveryLinePEOFirstPtyRegId | FIRST_PTY_REG_ID | — | ✅ |
| 44 | DeliveryLinePEOFiscalDocHeaderId | FISCAL_DOC_HEADER_ID | — | ✅ |
| 45 | DeliveryLinePEOFiscalDocLineId | FISCAL_DOC_LINE_ID | — | ✅ |
| 46 | DeliveryLinePEOFobCode | FOB_CODE | — | ✅ |
| 47 | DeliveryLinePEOFreightTermsCode | FREIGHT_TERMS_CODE | — | ✅ |
| 48 | DeliveryLinePEOGrossWeight | GROSS_WEIGHT | — | ✅ |
| 49 | DeliveryLinePEOIntendedUseClassifId | INTENDED_USE_CLASSIF_ID | — | ✅ |
| 50 | DeliveryLinePEOInvInterfacedFlag | INV_INTERFACED_FLAG | — | ✅ |
| 51 | DeliveryLinePEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 52 | DeliveryLinePEOItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 53 | DeliveryLinePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 54 | DeliveryLinePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 55 | DeliveryLinePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 56 | DeliveryLinePEOLatestDropoffDate | LATEST_DROPOFF_DATE | — | ✅ |
| 57 | DeliveryLinePEOLatestPickupDate | LATEST_PICKUP_DATE | — | ✅ |
| 58 | DeliveryLinePEOLoadSeqNumber | LOAD_SEQ_NUMBER | — | ✅ |
| 59 | DeliveryLinePEOLocatorId | LOCATOR_ID | — | ✅ |
| 60 | DeliveryLinePEOLotNumber | LOT_NUMBER | — | ✅ |
| 61 | DeliveryLinePEOModeOfTransport | MODE_OF_TRANSPORT | — | ✅ |
| 62 | DeliveryLinePEOMoveOrderLineId | MOVE_ORDER_LINE_ID | — | ✅ |
| 63 | DeliveryLinePEOMovementId | MOVEMENT_ID | — | ✅ |
| 64 | DeliveryLinePEOMvtStatStatus | MVT_STAT_STATUS | — | ✅ |
| 65 | DeliveryLinePEONetWeight | NET_WEIGHT | — | ✅ |
| 66 | DeliveryLinePEONewSourceShipmentId | NEW_SOURCE_SHIPMENT_ID | — | ✅ |
| 67 | DeliveryLinePEONewSourceShipmentNumber | NEW_SOURCE_SHIPMENT_NUMBER | — | ✅ |
| 68 | DeliveryLinePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 69 | DeliveryLinePEOOrgId | ORG_ID | — | ✅ |
| 70 | DeliveryLinePEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 71 | DeliveryLinePEOOriginalDeliveryDetailId | ORIGINAL_DELIVERY_DETAIL_ID | — | ✅ |
| 72 | DeliveryLinePEOOriginalItemConvertedQty | ORIGINAL_ITEM_CONVERTED_QTY | — | ✅ |
| 73 | DeliveryLinePEOOriginalItemId | ORIGINAL_ITEM_ID | — | ✅ |
| 74 | DeliveryLinePEOOriginalSubinventory | ORIGINAL_SUBINVENTORY | — | ✅ |
| 75 | DeliveryLinePEOPackingInstructions | PACKING_INSTRUCTIONS | — | ✅ |
| 76 | DeliveryLinePEOParentInventoryItemId | PARENT_INVENTORY_ITEM_ID | — | ✅ |
| 77 | DeliveryLinePEOParentLpnId | PARENT_LPN_ID | — | ✅ |
| 78 | DeliveryLinePEOParentSourceShipmentId | PARENT_SOURCE_SHIPMENT_ID | — | ✅ |
| 79 | DeliveryLinePEOPickableFlag | PICKABLE_FLAG | — | ✅ |
| 80 | DeliveryLinePEOPickedFromSubinventory | PICKED_FROM_SUBINVENTORY | — | ✅ |
| 81 | DeliveryLinePEOPickedQuantity | PICKED_QUANTITY | — | ✅ |
| 82 | DeliveryLinePEOPickedQuantity2 | PICKED_QUANTITY2 | — | ✅ |
| 83 | DeliveryLinePEOPjcProjectId | PJC_PROJECT_ID | — | ✅ |
| 84 | DeliveryLinePEOPjcTaskId | PJC_TASK_ID | — | ✅ |
| 85 | DeliveryLinePEOPreferredGrade | PREFERRED_GRADE | — | ✅ |
| 86 | DeliveryLinePEOProductCategory | PRODUCT_CATEGORY | — | ✅ |
| 87 | DeliveryLinePEOProductType | PRODUCT_TYPE | — | ✅ |
| 88 | DeliveryLinePEOProjectExpenseFlag | PROJECT_EXPENSE_FLAG | — | ✅ |
| 89 | DeliveryLinePEOQuickShipStatus | QUICK_SHIP_STATUS | — | ✅ |
| 90 | DeliveryLinePEORcvShipmentLineId | RCV_SHIPMENT_LINE_ID | — | ✅ |
| 91 | DeliveryLinePEOReleasedStatus | RELEASED_STATUS | — | ✅ |
| 92 | DeliveryLinePEORequestDateTypeCode | REQUEST_DATE_TYPE_CODE | — | ✅ |
| 93 | DeliveryLinePEORequestId | REQUEST_ID | — | ✅ |
| 94 | DeliveryLinePEORequestedQuantity | REQUESTED_QUANTITY | — | ✅ |
| 95 | DeliveryLinePEORequestedQuantity2 | REQUESTED_QUANTITY2 | — | ✅ |
| 96 | DeliveryLinePEORequestedQuantityUom | REQUESTED_QUANTITY_UOM | — | ✅ |
| 97 | DeliveryLinePEORequestedQuantityUom2 | REQUESTED_QUANTITY_UOM2 | — | ✅ |
| 98 | DeliveryLinePEORequisitionHeaderId | REQUISITION_HEADER_ID | — | ✅ |
| 99 | DeliveryLinePEORequisitionLineId | REQUISITION_LINE_ID | — | ✅ |
| 100 | DeliveryLinePEORevision | REVISION | — | ✅ |
| 101 | DeliveryLinePEOSalesOrderLineNumber | SALES_ORDER_LINE_NUMBER | — | ✅ |
| 102 | DeliveryLinePEOSalesOrderNumber | SALES_ORDER_NUMBER | — | ✅ |
| 103 | DeliveryLinePEOSalesOrderShipmentNumber | SALES_ORDER_SHIPMENT_NUMBER | — | ✅ |
| 104 | DeliveryLinePEOSealCode | SEAL_CODE | — | ✅ |
| 105 | DeliveryLinePEOSellingPrice | SELLING_PRICE | — | ✅ |
| 106 | DeliveryLinePEOServiceLevel | SERVICE_LEVEL | — | ✅ |
| 107 | DeliveryLinePEOShipFromLocationId | SHIP_FROM_LOCATION_ID | — | ✅ |
| 108 | DeliveryLinePEOShipMethodCode | SHIP_METHOD_CODE | — | ✅ |
| 109 | DeliveryLinePEOShipSetName | SHIP_SET_NAME | — | ✅ |
| 110 | DeliveryLinePEOShipToContactId | SHIP_TO_CONTACT_ID | — | ✅ |
| 111 | DeliveryLinePEOShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 112 | DeliveryLinePEOShipToLocationType | SHIP_TO_LOCATION_TYPE | — | ✅ |
| 113 | DeliveryLinePEOShipToPartyId | SHIP_TO_PARTY_ID | — | ✅ |
| 114 | DeliveryLinePEOShipToPartySiteId | SHIP_TO_PARTY_SITE_ID | — | ✅ |
| 115 | DeliveryLinePEOShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | ✅ |
| 116 | DeliveryLinePEOShipToleranceAbove | SHIP_TOLERANCE_ABOVE | — | ✅ |
| 117 | DeliveryLinePEOShipToleranceBelow | SHIP_TOLERANCE_BELOW | — | ✅ |
| 118 | DeliveryLinePEOShipmentAdviceStatus | SHIPMENT_ADVICE_STATUS | — | ✅ |
| 119 | DeliveryLinePEOShipmentPriorityCode | SHIPMENT_PRIORITY_CODE | — | ✅ |
| 120 | DeliveryLinePEOShippedQuantity | SHIPPED_QUANTITY | — | ✅ |
| 121 | DeliveryLinePEOShippedQuantity2 | SHIPPED_QUANTITY2 | — | ✅ |
| 122 | DeliveryLinePEOShippingInstructions | SHIPPING_INSTRUCTIONS | — | ✅ |
| 123 | DeliveryLinePEOSoldToContactId | SOLD_TO_CONTACT_ID | — | ✅ |
| 124 | DeliveryLinePEOSoldToPartyId | SOLD_TO_PARTY_ID | — | ✅ |
| 125 | DeliveryLinePEOSourceDocumentTypeId | SOURCE_DOCUMENT_TYPE_ID | — | ✅ |
| 126 | DeliveryLinePEOSourceHeaderId | SOURCE_HEADER_ID | — | ✅ |
| 127 | DeliveryLinePEOSourceHeaderNumber | SOURCE_HEADER_NUMBER | — | ✅ |
| 128 | DeliveryLinePEOSourceLineId | SOURCE_LINE_ID | — | ✅ |
| 129 | DeliveryLinePEOSourceLineNumber | SOURCE_LINE_NUMBER | — | ✅ |
| 130 | DeliveryLinePEOSourceLineType | SOURCE_LINE_TYPE | — | ✅ |
| 131 | DeliveryLinePEOSourceLineUpdateDate | SOURCE_LINE_UPDATE_DATE | — | ✅ |
| 132 | DeliveryLinePEOSourceShipmentId | SOURCE_SHIPMENT_ID | — | ✅ |
| 133 | DeliveryLinePEOSourceShipmentNumber | SOURCE_SHIPMENT_NUMBER | — | ✅ |
| 134 | DeliveryLinePEOSourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 135 | DeliveryLinePEOSplitFromDeliveryDetailId | SPLIT_FROM_DELIVERY_DETAIL_ID | — | ✅ |
| 136 | DeliveryLinePEOSrcRequestedQuantity | SRC_REQUESTED_QUANTITY | — | ✅ |
| 137 | DeliveryLinePEOSrcRequestedQuantity2 | SRC_REQUESTED_QUANTITY2 | — | ✅ |
| 138 | DeliveryLinePEOSrcRequestedQuantityUom | SRC_REQUESTED_QUANTITY_UOM | — | ✅ |
| 139 | DeliveryLinePEOSrcRequestedQuantityUom2 | SRC_REQUESTED_QUANTITY_UOM2 | — | ✅ |
| 140 | DeliveryLinePEOSubinventory | SUBINVENTORY | — | ✅ |
| 141 | DeliveryLinePEOTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | ✅ |
| 142 | DeliveryLinePEOTaxInvoiceDate | TAX_INVOICE_DATE | — | ✅ |
| 143 | DeliveryLinePEOTaxInvoiceNumber | TAX_INVOICE_NUMBER | — | ✅ |
| 144 | DeliveryLinePEOThirdPtyRegId | THIRD_PTY_REG_ID | — | ✅ |
| 145 | DeliveryLinePEOTpInitialLegDestLocId | TP_INITIAL_LEG_DEST_LOC_ID | — | ✅ |
| 146 | DeliveryLinePEOTpReceivedDate | TP_RECEIVED_DATE | — | ✅ |
| 147 | DeliveryLinePEOTpShipmentLine | TP_SHIPMENT_LINE | — | ✅ |
| 148 | DeliveryLinePEOTpShipmentNumber | TP_SHIPMENT_NUMBER | — | ✅ |
| 149 | DeliveryLinePEOTpStatusCode | TP_STATUS_CODE | — | ✅ |
| 150 | DeliveryLinePEOTrackingNumber | TRACKING_NUMBER | — | ✅ |
| 151 | DeliveryLinePEOTradeComplianceDate | TRADE_COMPLIANCE_DATE | — | ✅ |
| 152 | DeliveryLinePEOTradeComplianceMethod | TRADE_COMPLIANCE_METHOD | — | ✅ |
| 153 | DeliveryLinePEOTradeComplianceReason | TRADE_COMPLIANCE_REASON | — | ✅ |
| 154 | DeliveryLinePEOTradeComplianceStatus | TRADE_COMPLIANCE_STATUS | — | ✅ |
| 155 | DeliveryLinePEOTransactionId | TRANSACTION_ID | — | ✅ |
| 156 | DeliveryLinePEOTransactionTempId | TRANSACTION_TEMP_ID | — | ✅ |
| 157 | DeliveryLinePEOTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 158 | DeliveryLinePEOUnitPrice | UNIT_PRICE | — | ✅ |
| 159 | DeliveryLinePEOUnitVolume | UNIT_VOLUME | — | ✅ |
| 160 | DeliveryLinePEOUnitWeight | UNIT_WEIGHT | — | ✅ |
| 161 | DeliveryLinePEOUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | ✅ |
| 162 | DeliveryLinePEOVolume | VOLUME | — | ✅ |
| 163 | DeliveryLinePEOVolumeUomCode | VOLUME_UOM_CODE | — | ✅ |
| 164 | DeliveryLinePEOWeightUomCode | WEIGHT_UOM_CODE | — | ✅ |
| 165 | DeliveryLinePEOWmsInterfacedFlag | WMS_INTERFACED_FLAG | — | ✅ |
| 166 | DeliveryLinePEOWmsShipToleranceAbove | WMS_SHIP_TOLERANCE_ABOVE | — | ✅ |
| 167 | DeliveryLinePEOWmsShipToleranceBelow | WMS_SHIP_TOLERANCE_BELOW | — | ✅ |
| 168 | DeliveryLinePEOWvFrozenFlag | WV_FROZEN_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
