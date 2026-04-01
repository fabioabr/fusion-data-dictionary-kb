---
id: DOC-OTHER-PVO-DeliveryLinePVO
doc_type: system-doc
title: "DeliveryLinePVO — PVO Cross-Module"
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
  - DeliveryLinePVO
  - deliverylinepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DeliveryLinePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Delivery Line. Acessa as tabelas: DOO_FULFILL_LINES_ALL, DOO_PROJECTS, HZ_PARTIES (+6).

**Caminho:** `FscmTopModelAM.WshDeliveriesAM.DeliveryLinePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 296 | 9 | 1 | 103 | 35% |

---

## 🔗 Tabelas Relacionadas

- [[doo_fulfill_lines_all|DOO_FULFILL_LINES_ALL]] — 2 atributos
- [[doo_projects|DOO_PROJECTS]] — 24 atributos
- [[hz_parties|HZ_PARTIES]] — 4 atributos (4 BICC)
- [[hz_relationships|HZ_RELATIONSHIPS]] — 4 atributos (4 BICC)
- [[inv_org_parameters_v|INV_ORG_PARAMETERS_V]] — 2 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 8 atributos
- [[wsh_delivery_assignments|WSH_DELIVERY_ASSIGNMENTS]] — 4 atributos (2 BICC)
- [[wsh_delivery_details|WSH_DELIVERY_DETAILS]] — 161 atributos (1 PKs, 76 BICC)
- [[wsh_new_deliveries|WSH_NEW_DELIVERIES]] — 87 atributos (16 BICC)

---

## ⚙️ Atributos

### [[doo_fulfill_lines_all|DOO_FULFILL_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FulfillLineId | FULFILL_LINE_ID | — | — |
| 2 | FulfillLinePEOPrjRecIndicator | PRJ_REC_INDICATOR | — | — |

### [[doo_projects|DOO_PROJECTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectPEOCreatedBy | CREATED_BY | — | — |
| 2 | ProjectPEOCreationDate | CREATION_DATE | — | — |
| 3 | ProjectPEODooOrderPrjId | DOO_ORDER_PRJ_ID | — | — |
| 4 | ProjectPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 5 | ProjectPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ProjectPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ProjectPEOModifiedFlag | MODIFIED_FLAG | — | — |
| 8 | ProjectPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ProjectPEOPJC_BILLABLE_FLAG | PJC_BILLABLE_FLAG | — | — |
| 10 | ProjectPEOPJC_CAPITALIZABLE_FLAG | PJC_CAPITALIZABLE_FLAG | — | — |
| 11 | ProjectPEOPJC_CONTEXT_CATEGORY | PJC_CONTEXT_CATEGORY | — | — |
| 12 | ProjectPEOPJC_CONTRACT_ID | PJC_CONTRACT_ID | — | — |
| 13 | ProjectPEOPJC_CONTRACT_LINE_ID | PJC_CONTRACT_LINE_ID | — | — |
| 14 | ProjectPEOPJC_EXPENDITURE_ITEM_DATE | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 15 | ProjectPEOPJC_EXPENDITURE_TYPE_ID | PJC_EXPENDITURE_TYPE_ID | — | — |
| 16 | ProjectPEOPJC_FUNDING_ALLOCATION_ID | PJC_FUNDING_ALLOCATION_ID | — | — |
| 17 | ProjectPEOPJC_ORGANIZATION_ID | PJC_ORGANIZATION_ID | — | — |
| 18 | ProjectPEOPJC_PROJECT_ID | PJC_PROJECT_ID | — | — |
| 19 | ProjectPEOPJC_RESERVED_ATTRIBUTE1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 20 | ProjectPEOPJC_TASK_ID | PJC_TASK_ID | — | — |
| 21 | ProjectPEOPJC_WORK_TYPE_ID | PJC_WORK_TYPE_ID | — | — |
| 22 | ProjectPEOParentEntityCode | PARENT_ENTITY_CODE | — | — |
| 23 | ProjectPEOParentEntityId | PARENT_ENTITY_ID | — | — |
| 24 | ProjectPEORefDooOrderPrjId | REF_DOO_ORDER_PRJ_ID | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ShipToRelPartyPEOPartyId | PARTY_ID | — | ✅ |
| 2 | ShipToRelPartyPEOPartyName | PARTY_NAME | — | ✅ |
| 3 | SoldToRelPartyPEOPartyId | PARTY_ID | — | ✅ |
| 4 | SoldToRelPartyPEOPartyName | PARTY_NAME | — | ✅ |

### [[hz_relationships|HZ_RELATIONSHIPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ShipToRelationshipPEORelationshipRecId1 | RELATIONSHIP_REC_ID | — | ✅ |
| 2 | ShipToRelationshipPEOSubjectId | SUBJECT_ID | — | ✅ |
| 3 | SoldToRelationshipPEORelationshipRecId | RELATIONSHIP_REC_ID | — | ✅ |
| 4 | SoldToRelationshipPEOSubjectId | SUBJECT_ID | — | ✅ |

### [[inv_org_parameters_v|INV_ORG_PARAMETERS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationParameterPEOOrganizationCode | ORGANIZATION_CODE | — | ✅ |
| 2 | OrganizationParameterPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedByPersonNamePEODisplayName | DISPLAY_NAME | — | — |
| 2 | CreatedByPersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | CreatedByPersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | CreatedByPersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |
| 5 | LastUpdatedByPersonNamePEODisplayName | DISPLAY_NAME | — | — |
| 6 | LastUpdatedByPersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | LastUpdatedByPersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 8 | LastUpdatedByPersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |

### [[wsh_delivery_assignments|WSH_DELIVERY_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeliveryLineAssignmentPEODeliveryAssignmentId | DELIVERY_ASSIGNMENT_ID | — | — |
| 2 | DeliveryLineAssignmentPEODeliveryDetailId | DELIVERY_DETAIL_ID | — | — |
| 3 | DeliveryLineAssignmentPEODeliveryId | DELIVERY_ID | — | ✅ |
| 4 | DeliveryLineAssignmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[wsh_delivery_details|WSH_DELIVERY_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllowItemSubstitutionFlag | ALLOW_ITEM_SUBSTITUTION_FLAG | — | ✅ |
| 2 | DeliveryDetailId | DELIVERY_DETAIL_ID | 🔑 | ✅ |
| 3 | DeliveryLInePEOTradeComplianceDate | TRADE_COMPLIANCE_DATE | — | — |
| 4 | DeliveryLinePEOArrivalSetName | ARRIVAL_SET_NAME | — | — |
| 5 | DeliveryLinePEOAssessableValue | ASSESSABLE_VALUE | — | ✅ |
| 6 | DeliveryLinePEOBatchId | BATCH_ID | — | — |
| 7 | DeliveryLinePEOBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 8 | DeliveryLinePEOBillToLocationId | BILL_TO_LOCATION_ID | — | ✅ |
| 9 | DeliveryLinePEOBillToPartyId | BILL_TO_PARTY_ID | — | — |
| 10 | DeliveryLinePEOBillToPartySiteId | BILL_TO_PARTY_SITE_ID | — | — |
| 11 | DeliveryLinePEOCancelledQuantity | CANCELLED_QUANTITY | — | — |
| 12 | DeliveryLinePEOCancelledQuantity2 | CANCELLED_QUANTITY2 | — | — |
| 13 | DeliveryLinePEOCarrierId | CARRIER_ID | — | — |
| 14 | DeliveryLinePEOCategoryId | CATEGORY_ID | — | ✅ |
| 15 | DeliveryLinePEOConvertedQuantity | CONVERTED_QUANTITY | — | — |
| 16 | DeliveryLinePEOCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | — |
| 17 | DeliveryLinePEOCreatedBy | CREATED_BY | — | ✅ |
| 18 | DeliveryLinePEOCreationDate | CREATION_DATE | — | ✅ |
| 19 | DeliveryLinePEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 20 | DeliveryLinePEOCustPoNumber | CUST_PO_NUMBER | — | ✅ |
| 21 | DeliveryLinePEOCustomerItemId | CUSTOMER_ITEM_ID | — | — |
| 22 | DeliveryLinePEOCycleCountQuantity | CYCLE_COUNT_QUANTITY | — | — |
| 23 | DeliveryLinePEOCycleCountQuantity2 | CYCLE_COUNT_QUANTITY2 | — | — |
| 24 | DeliveryLinePEODateRequested | DATE_REQUESTED | — | ✅ |
| 25 | DeliveryLinePEODateScheduled | DATE_SCHEDULED | — | ✅ |
| 26 | DeliveryLinePEODefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | ✅ |
| 27 | DeliveryLinePEODeliveredQuantity | DELIVERED_QUANTITY | — | — |
| 28 | DeliveryLinePEODeliveredQuantity2 | DELIVERED_QUANTITY2 | — | — |
| 29 | DeliveryLinePEODetailContainerItemId | DETAIL_CONTAINER_ITEM_ID | — | — |
| 30 | DeliveryLinePEODocumentSubType | DOCUMENT_SUB_TYPE | — | ✅ |
| 31 | DeliveryLinePEOEarliestDropoffDate | EARLIEST_DROPOFF_DATE | — | — |
| 32 | DeliveryLinePEOEarliestPickupDate | EARLIEST_PICKUP_DATE | — | — |
| 33 | DeliveryLinePEOEndAssemblyItemNumber | END_ASSEMBLY_ITEM_NUMBER | — | — |
| 34 | DeliveryLinePEOExemptCertificateNumber | EXEMPT_CERTIFICATE_NUMBER | — | ✅ |
| 35 | DeliveryLinePEOExemptReasonCode | EXEMPT_REASON_CODE | — | ✅ |
| 36 | DeliveryLinePEOFinalDischargeLocationId | FINAL_DISCHARGE_LOCATION_ID | — | ✅ |
| 37 | DeliveryLinePEOFirstPtyRegId | FIRST_PTY_REG_ID | — | ✅ |
| 38 | DeliveryLinePEOFobCode | FOB_CODE | — | ✅ |
| 39 | DeliveryLinePEOFreightTermsCode | FREIGHT_TERMS_CODE | — | ✅ |
| 40 | DeliveryLinePEOGrossWeight | GROSS_WEIGHT | — | ✅ |
| 41 | DeliveryLinePEOInspectionFlag | INSPECTION_FLAG | — | — |
| 42 | DeliveryLinePEOIntendedUseClassifId | INTENDED_USE_CLASSIF_ID | — | ✅ |
| 43 | DeliveryLinePEOInvInterfacedFlag | INV_INTERFACED_FLAG | — | — |
| 44 | DeliveryLinePEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 45 | DeliveryLinePEOItemDescription | ITEM_DESCRIPTION | — | — |
| 46 | DeliveryLinePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 47 | DeliveryLinePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 48 | DeliveryLinePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 49 | DeliveryLinePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 50 | DeliveryLinePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 51 | DeliveryLinePEOLatestDropoffDate | LATEST_DROPOFF_DATE | — | — |
| 52 | DeliveryLinePEOLatestPickupDate | LATEST_PICKUP_DATE | — | — |
| 53 | DeliveryLinePEOLoadSeqNumber | LOAD_SEQ_NUMBER | — | ✅ |
| 54 | DeliveryLinePEOLocatorId | LOCATOR_ID | — | ✅ |
| 55 | DeliveryLinePEOLotNumber | LOT_NUMBER | — | ✅ |
| 56 | DeliveryLinePEOLpnContentId | LPN_CONTENT_ID | — | — |
| 57 | DeliveryLinePEOMasterContainerItemId | MASTER_CONTAINER_ITEM_ID | — | — |
| 58 | DeliveryLinePEOModeOfTransport | MODE_OF_TRANSPORT | — | — |
| 59 | DeliveryLinePEOMoveOrderLineId | MOVE_ORDER_LINE_ID | — | — |
| 60 | DeliveryLinePEOMovementId | MOVEMENT_ID | — | — |
| 61 | DeliveryLinePEOMvtStatStatus | MVT_STAT_STATUS | — | — |
| 62 | DeliveryLinePEONetWeight | NET_WEIGHT | — | ✅ |
| 63 | DeliveryLinePEONewSourceShipmentId | NEW_SOURCE_SHIPMENT_ID | — | — |
| 64 | DeliveryLinePEONewSourceShipmentNumber | NEW_SOURCE_SHIPMENT_NUMBER | — | — |
| 65 | DeliveryLinePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 66 | DeliveryLinePEOOrgId | ORG_ID | — | ✅ |
| 67 | DeliveryLinePEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 68 | DeliveryLinePEOOriginalSubinventory | ORIGINAL_SUBINVENTORY | — | — |
| 69 | DeliveryLinePEOOutsourcerPartyId | OUTSOURCER_PARTY_ID | — | — |
| 70 | DeliveryLinePEOPackingInstructions | PACKING_INSTRUCTIONS | — | — |
| 71 | DeliveryLinePEOParentLpnId | PARENT_LPN_ID | — | — |
| 72 | DeliveryLinePEOPickableFlag | PICKABLE_FLAG | — | ✅ |
| 73 | DeliveryLinePEOPickedQuantity | PICKED_QUANTITY | — | ✅ |
| 74 | DeliveryLinePEOPickedQuantity2 | PICKED_QUANTITY2 | — | — |
| 75 | DeliveryLinePEOPjcProjectId | PJC_PROJECT_ID | — | — |
| 76 | DeliveryLinePEOPjcTaskId | PJC_TASK_ID | — | — |
| 77 | DeliveryLinePEOPreferredGrade | PREFERRED_GRADE | — | — |
| 78 | DeliveryLinePEOProductCategory | PRODUCT_CATEGORY | — | ✅ |
| 79 | DeliveryLinePEOProductType | PRODUCT_TYPE | — | ✅ |
| 80 | DeliveryLinePEOProjectId | PROJECT_ID | — | — |
| 81 | DeliveryLinePEOQuickShipStatus | QUICK_SHIP_STATUS | — | — |
| 82 | DeliveryLinePEOReleasedStatus | RELEASED_STATUS | — | ✅ |
| 83 | DeliveryLinePEORequestDateTypeCode | REQUEST_DATE_TYPE_CODE | — | — |
| 84 | DeliveryLinePEORequestId | REQUEST_ID | — | — |
| 85 | DeliveryLinePEORequestedQuantity | REQUESTED_QUANTITY | — | ✅ |
| 86 | DeliveryLinePEORequestedQuantity2 | REQUESTED_QUANTITY2 | — | — |
| 87 | DeliveryLinePEORequestedQuantityUom | REQUESTED_QUANTITY_UOM | — | ✅ |
| 88 | DeliveryLinePEORequestedQuantityUom2 | REQUESTED_QUANTITY_UOM2 | — | — |
| 89 | DeliveryLinePEORequisitionHeaderId | REQUISITION_HEADER_ID | — | — |
| 90 | DeliveryLinePEORequisitionLineId | REQUISITION_LINE_ID | — | — |
| 91 | DeliveryLinePEORevision | REVISION | — | ✅ |
| 92 | DeliveryLinePEOSalesOrderLineNumber | SALES_ORDER_LINE_NUMBER | — | ✅ |
| 93 | DeliveryLinePEOSalesOrderNumber | SALES_ORDER_NUMBER | — | ✅ |
| 94 | DeliveryLinePEOSalesOrderShipmentNumber | SALES_ORDER_SHIPMENT_NUMBER | — | — |
| 95 | DeliveryLinePEOSealCode | SEAL_CODE | — | ✅ |
| 96 | DeliveryLinePEOSellingPrice | SELLING_PRICE | — | — |
| 97 | DeliveryLinePEOSerialNumber | SERIAL_NUMBER | — | — |
| 98 | DeliveryLinePEOServiceLevel | SERVICE_LEVEL | — | — |
| 99 | DeliveryLinePEOShipFromLocationId | SHIP_FROM_LOCATION_ID | — | — |
| 100 | DeliveryLinePEOShipMethodCode | SHIP_METHOD_CODE | — | — |
| 101 | DeliveryLinePEOShipSetName | SHIP_SET_NAME | — | ✅ |
| 102 | DeliveryLinePEOShipToContactId | SHIP_TO_CONTACT_ID | — | ✅ |
| 103 | DeliveryLinePEOShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 104 | DeliveryLinePEOShipToPartyId | SHIP_TO_PARTY_ID | — | ✅ |
| 105 | DeliveryLinePEOShipToPartySiteId | SHIP_TO_PARTY_SITE_ID | — | — |
| 106 | DeliveryLinePEOShipToleranceAbove | SHIP_TOLERANCE_ABOVE | — | — |
| 107 | DeliveryLinePEOShipToleranceBelow | SHIP_TOLERANCE_BELOW | — | — |
| 108 | DeliveryLinePEOShipmentAdviceStatus | SHIPMENT_ADVICE_STATUS | — | — |
| 109 | DeliveryLinePEOShipmentPriorityCode | SHIPMENT_PRIORITY_CODE | — | — |
| 110 | DeliveryLinePEOShippedQuantity | SHIPPED_QUANTITY | — | ✅ |
| 111 | DeliveryLinePEOShippedQuantity2 | SHIPPED_QUANTITY2 | — | — |
| 112 | DeliveryLinePEOShippingInstructions | SHIPPING_INSTRUCTIONS | — | — |
| 113 | DeliveryLinePEOSoldToContactId | SOLD_TO_CONTACT_ID | — | ✅ |
| 114 | DeliveryLinePEOSoldToPartyId | SOLD_TO_PARTY_ID | — | ✅ |
| 115 | DeliveryLinePEOSourceDocumentTypeId | SOURCE_DOCUMENT_TYPE_ID | — | — |
| 116 | DeliveryLinePEOSourceHeaderId | SOURCE_HEADER_ID | — | ✅ |
| 117 | DeliveryLinePEOSourceHeaderNumber | SOURCE_HEADER_NUMBER | — | ✅ |
| 118 | DeliveryLinePEOSourceLineId | SOURCE_LINE_ID | — | ✅ |
| 119 | DeliveryLinePEOSourceLineNumber | SOURCE_LINE_NUMBER | — | ✅ |
| 120 | DeliveryLinePEOSourceLineType | SOURCE_LINE_TYPE | — | ✅ |
| 121 | DeliveryLinePEOSourceLineUpdateDate | SOURCE_LINE_UPDATE_DATE | — | — |
| 122 | DeliveryLinePEOSourceShipmentId | SOURCE_SHIPMENT_ID | — | ✅ |
| 123 | DeliveryLinePEOSourceShipmentNumber | SOURCE_SHIPMENT_NUMBER | — | ✅ |
| 124 | DeliveryLinePEOSourceSystemId | SOURCE_SYSTEM_ID | — | — |
| 125 | DeliveryLinePEOSplitFromDeliveryDetailId | SPLIT_FROM_DELIVERY_DETAIL_ID | — | — |
| 126 | DeliveryLinePEOSrcRequestedQuantity | SRC_REQUESTED_QUANTITY | — | ✅ |
| 127 | DeliveryLinePEOSrcRequestedQuantity2 | SRC_REQUESTED_QUANTITY2 | — | — |
| 128 | DeliveryLinePEOSrcRequestedQuantityUom | SRC_REQUESTED_QUANTITY_UOM | — | ✅ |
| 129 | DeliveryLinePEOSrcRequestedQuantityUom2 | SRC_REQUESTED_QUANTITY_UOM2 | — | — |
| 130 | DeliveryLinePEOSubinventory | SUBINVENTORY | — | ✅ |
| 131 | DeliveryLinePEOTaskId | TASK_ID | — | — |
| 132 | DeliveryLinePEOTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | ✅ |
| 133 | DeliveryLinePEOTaxInvoiceDate | TAX_INVOICE_DATE | — | ✅ |
| 134 | DeliveryLinePEOTaxInvoiceNumber | TAX_INVOICE_NUMBER | — | ✅ |
| 135 | DeliveryLinePEOThirdPtyRegId | THIRD_PTY_REG_ID | — | ✅ |
| 136 | DeliveryLinePEOTpInitialLegDestLocId | TP_INITIAL_LEG_DEST_LOC_ID | — | ✅ |
| 137 | DeliveryLinePEOTpReceivedDate | TP_RECEIVED_DATE | — | ✅ |
| 138 | DeliveryLinePEOTpShipmentLine | TP_SHIPMENT_LINE | — | ✅ |
| 139 | DeliveryLinePEOTpShipmentNumber | TP_SHIPMENT_NUMBER | — | ✅ |
| 140 | DeliveryLinePEOTpStatusCode | TP_STATUS_CODE | — | ✅ |
| 141 | DeliveryLinePEOTrackingNumber | TRACKING_NUMBER | — | ✅ |
| 142 | DeliveryLinePEOTradeComplianceMethod | TRADE_COMPLIANCE_METHOD | — | — |
| 143 | DeliveryLinePEOTradeComplianceReason | TRADE_COMPLIANCE_REASON | — | — |
| 144 | DeliveryLinePEOTradeComplianceStatus | TRADE_COMPLIANCE_STATUS | — | — |
| 145 | DeliveryLinePEOTransactionId | TRANSACTION_ID | — | — |
| 146 | DeliveryLinePEOTransactionTempId | TRANSACTION_TEMP_ID | — | — |
| 147 | DeliveryLinePEOTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 148 | DeliveryLinePEOUnitPrice | UNIT_PRICE | — | — |
| 149 | DeliveryLinePEOUnitVolume | UNIT_VOLUME | — | — |
| 150 | DeliveryLinePEOUnitWeight | UNIT_WEIGHT | — | — |
| 151 | DeliveryLinePEOUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | ✅ |
| 152 | DeliveryLinePEOVolume | VOLUME | — | ✅ |
| 153 | DeliveryLinePEOVolumeUomCode | VOLUME_UOM_CODE | — | ✅ |
| 154 | DeliveryLinePEOWeightUomCode | WEIGHT_UOM_CODE | — | ✅ |
| 155 | DeliveryLinePEOWmsShipToleranceAbove | WMS_SHIP_TOLERANCE_ABOVE | — | — |
| 156 | DeliveryLinePEOWmsShipToleranceBelow | WMS_SHIP_TOLERANCE_BELOW | — | — |
| 157 | DeliveryLinePEOWvFrozenFlag | WV_FROZEN_FLAG | — | — |
| 158 | OriginalDeliveryDetailId | ORIGINAL_DELIVERY_DETAIL_ID | — | ✅ |
| 159 | OriginalItemConvertedQty | ORIGINAL_ITEM_CONVERTED_QTY | — | ✅ |
| 160 | OriginalItemId | ORIGINAL_ITEM_ID | — | ✅ |
| 161 | ProjectExpenseFlag | PROJECT_EXPENSE_FLAG | — | — |

### [[wsh_new_deliveries|WSH_NEW_DELIVERIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeliveryPEOAcceptanceFlag | ACCEPTANCE_FLAG | — | — |
| 2 | DeliveryPEOAcceptedBy | ACCEPTED_BY | — | — |
| 3 | DeliveryPEOAcceptedDate | ACCEPTED_DATE | — | — |
| 4 | DeliveryPEOAcknowledgedBy | ACKNOWLEDGED_BY | — | — |
| 5 | DeliveryPEOActualShipDate | ACTUAL_SHIP_DATE | — | ✅ |
| 6 | DeliveryPEOActualShipDateTime | ACTUAL_SHIP_DATE | — | — |
| 7 | DeliveryPEOAdditionalShipmentInfo | ADDITIONAL_SHIPMENT_INFO | — | — |
| 8 | DeliveryPEOApBatchId | AP_BATCH_ID | — | — |
| 9 | DeliveryPEOAsnDateSent | ASN_DATE_SENT | — | — |
| 10 | DeliveryPEOAsnSeqNumber | ASN_SEQ_NUMBER | — | — |
| 11 | DeliveryPEOAsnStatusCode | ASN_STATUS_CODE | — | — |
| 12 | DeliveryPEOAutoApExcludeFlag | AUTO_AP_EXCLUDE_FLAG | — | — |
| 13 | DeliveryPEOAutoScExcludeFlag | AUTO_SC_EXCLUDE_FLAG | — | — |
| 14 | DeliveryPEOBatchId | BATCH_ID | — | — |
| 15 | DeliveryPEOBillFreightTo | BILL_FREIGHT_TO | — | — |
| 16 | DeliveryPEOBillOfLadingNumber | BILL_OF_LADING_NUMBER | — | ✅ |
| 17 | DeliveryPEOBookingNumber | BOOKING_NUMBER | — | — |
| 18 | DeliveryPEOCarriedBy | CARRIED_BY | — | — |
| 19 | DeliveryPEOCarrierId | CARRIER_ID | — | — |
| 20 | DeliveryPEOCodAmount | COD_AMOUNT | — | — |
| 21 | DeliveryPEOCodChargePaidBy | COD_CHARGE_PAID_BY | — | — |
| 22 | DeliveryPEOCodCurrencyCode | COD_CURRENCY_CODE | — | — |
| 23 | DeliveryPEOCodRemitTo | COD_REMIT_TO | — | — |
| 24 | DeliveryPEOConfirmDate | CONFIRM_DATE | — | ✅ |
| 25 | DeliveryPEOConfirmedBy | CONFIRMED_BY | — | — |
| 26 | DeliveryPEOCreatedBy | CREATED_BY | — | — |
| 27 | DeliveryPEOCreationDate | CREATION_DATE | — | — |
| 28 | DeliveryPEOCurrencyCode | CURRENCY_CODE | — | — |
| 29 | DeliveryPEODeliveredDate | DELIVERED_DATE | — | ✅ |
| 30 | DeliveryPEODeliveryId | DELIVERY_ID | — | ✅ |
| 31 | DeliveryPEODeliveryName | DELIVERY_NAME | — | ✅ |
| 32 | DeliveryPEODeliveryType | DELIVERY_TYPE | — | — |
| 33 | DeliveryPEODescription | DESCRIPTION | — | — |
| 34 | DeliveryPEODockCode | DOCK_CODE | — | — |
| 35 | DeliveryPEOEarliestDropoffDate | EARLIEST_DROPOFF_DATE | — | — |
| 36 | DeliveryPEOEarliestPickupDate | EARLIEST_PICKUP_DATE | — | — |
| 37 | DeliveryPEOEntryNumber | ENTRY_NUMBER | — | — |
| 38 | DeliveryPEOFobCode | FOB_CODE | — | — |
| 39 | DeliveryPEOFobLocationId | FOB_LOCATION_ID | — | — |
| 40 | DeliveryPEOFreightTermsCode | FREIGHT_TERMS_CODE | — | ✅ |
| 41 | DeliveryPEOFtzNumber | FTZ_NUMBER | — | — |
| 42 | DeliveryPEOGrossWeight | GROSS_WEIGHT | — | ✅ |
| 43 | DeliveryPEOHashString | HASH_STRING | — | — |
| 44 | DeliveryPEOHashValue | HASH_VALUE | — | — |
| 45 | DeliveryPEOInBondCode | IN_BOND_CODE | — | — |
| 46 | DeliveryPEOInitialPickupDate | INITIAL_PICKUP_DATE | — | ✅ |
| 47 | DeliveryPEOInitialPickupLocationId | INITIAL_PICKUP_LOCATION_ID | — | — |
| 48 | DeliveryPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 49 | DeliveryPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 50 | DeliveryPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 51 | DeliveryPEOLatestDropoffDate | LATEST_DROPOFF_DATE | — | — |
| 52 | DeliveryPEOLatestPickupDate | LATEST_PICKUP_DATE | — | — |
| 53 | DeliveryPEOLoadingOrderFlag | LOADING_ORDER_FLAG | — | — |
| 54 | DeliveryPEOLoadingSequence | LOADING_SEQUENCE | — | — |
| 55 | DeliveryPEOModeOfTransport | MODE_OF_TRANSPORT | — | — |
| 56 | DeliveryPEONetWeight | NET_WEIGHT | — | — |
| 57 | DeliveryPEONumberOfLpn | NUMBER_OF_LPN | — | — |
| 58 | DeliveryPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 59 | DeliveryPEOOrganizationId | ORGANIZATION_ID | — | — |
| 60 | DeliveryPEOOutsourcerPartyId | OUTSOURCER_PARTY_ID | — | — |
| 61 | DeliveryPEOPackingSlipNumber | PACKING_SLIP_NUMBER | — | ✅ |
| 62 | DeliveryPEOPackingSlipStatus | PACKING_SLIP_STATUS | — | — |
| 63 | DeliveryPEOPlannedFlag | PLANNED_FLAG | — | — |
| 64 | DeliveryPEOPortOfDischarge | PORT_OF_DISCHARGE | — | — |
| 65 | DeliveryPEOPortOfLoading | PORT_OF_LOADING | — | — |
| 66 | DeliveryPEOProblemContactReference | PROBLEM_CONTACT_REFERENCE | — | — |
| 67 | DeliveryPEOReasonOfTransport | REASON_OF_TRANSPORT | — | — |
| 68 | DeliveryPEORequestId | REQUEST_ID | — | — |
| 69 | DeliveryPEORoutingInstructions | ROUTING_INSTRUCTIONS | — | — |
| 70 | DeliveryPEOSealCode | SEAL_CODE | — | — |
| 71 | DeliveryPEOServiceContract | SERVICE_CONTRACT | — | — |
| 72 | DeliveryPEOServiceLevel | SERVICE_LEVEL | — | — |
| 73 | DeliveryPEOShipMethodCode | SHIP_METHOD_CODE | — | — |
| 74 | DeliveryPEOShipToPartyId | SHIP_TO_PARTY_ID | — | — |
| 75 | DeliveryPEOShippingMarks | SHIPPING_MARKS | — | — |
| 76 | DeliveryPEOSoldToPartyId | SOLD_TO_PARTY_ID | — | — |
| 77 | DeliveryPEOSourceHeaderId | SOURCE_HEADER_ID | — | — |
| 78 | DeliveryPEOStatusCode | STATUS_CODE | — | ✅ |
| 79 | DeliveryPEOUltimateDropoffDate | ULTIMATE_DROPOFF_DATE | — | — |
| 80 | DeliveryPEOUltimateDropoffLocationId | ULTIMATE_DROPOFF_LOCATION_ID | — | — |
| 81 | DeliveryPEOVehicleItemId | VEHICLE_ITEM_ID | — | — |
| 82 | DeliveryPEOVehicleNumber | VEHICLE_NUMBER | — | ✅ |
| 83 | DeliveryPEOVolume | VOLUME | — | — |
| 84 | DeliveryPEOVolumeUomCode | VOLUME_UOM_CODE | — | ✅ |
| 85 | DeliveryPEOWaybill | WAYBILL | — | ✅ |
| 86 | DeliveryPEOWeightUomCode | WEIGHT_UOM_CODE | — | ✅ |
| 87 | DeliveryPEOWvFrozenFlag | WV_FROZEN_FLAG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
