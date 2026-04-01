---
id: DOC-OTHER-PVO-PartsProfitabilityCostPVO
doc_type: system-doc
title: "PartsProfitabilityCostPVO — PVO Cross-Module"
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
  - PartsProfitabilityCostPVO
  - partsprofitabilitycostpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PartsProfitabilityCostPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Parts Profitability Cost. Acessa as tabelas: DOO_FULFILL_LINES_ALL, DOO_LINES_ALL, HZ_PARTY_SITES (+10).

**Caminho:** `FscmTopModelAM.PartsAnalyticsAM.PartsProfitabilityCostPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 515 | 13 | 1 | 44 | 9% |

---

## 🔗 Tabelas Relacionadas

- [[doo_fulfill_lines_all|DOO_FULFILL_LINES_ALL]] — 192 atributos (5 BICC)
- [[doo_lines_all|DOO_LINES_ALL]] — 49 atributos (2 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 34 atributos (1 BICC)
- [[qp_charge_definitions_vl|QP_CHARGE_DEFINITIONS_VL]] — 22 atributos (2 BICC)
- [[qp_price_elements_vl|QP_PRICE_ELEMENTS_VL]] — 13 atributos (2 BICC)
- [[qp_pricing_strategies_vl|QP_PRICING_STRATEGIES_VL]] — 20 atributos (2 BICC)
- [[rcl_inv_transfer_orders_v|RCL_INV_TRANSFER_ORDERS_V]] — 9 atributos
- [[rcl_parts_req_lines|RCL_PARTS_REQ_LINES]] — 22 atributos (10 BICC)
- [[rcl_parts_req_line_details|RCL_PARTS_REQ_LINE_DETAILS]] — 17 atributos (1 PKs, 5 BICC)
- [[rcl_pricing_headers|RCL_PRICING_HEADERS]] — 19 atributos (4 BICC)
- [[rcl_service_charges|RCL_SERVICE_CHARGES]] — 28 atributos (3 BICC)
- [[rcl_service_charge_components|RCL_SERVICE_CHARGE_COMPONENTS]] — 35 atributos (6 BICC)
- [[svc_service_requests|SVC_SERVICE_REQUESTS]] — 55 atributos (2 BICC)

---

## ⚙️ Atributos

### [[doo_fulfill_lines_all|DOO_FULFILL_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FulfillLinePEOAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 2 | FulfillLinePEOActionTypeCode | ACTION_TYPE_CODE | — | — |
| 3 | FulfillLinePEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | — |
| 4 | FulfillLinePEOActualShipDate2 | ACTUAL_SHIP_DATE | — | — |
| 5 | FulfillLinePEOAgreementHeaderId | AGREEMENT_HEADER_ID | — | — |
| 6 | FulfillLinePEOAgreementLineId | AGREEMENT_LINE_ID | — | — |
| 7 | FulfillLinePEOAgreementVersionNumber | AGREEMENT_VERSION_NUMBER | — | — |
| 8 | FulfillLinePEOAppliedPriceListId | APPLIED_PRICE_LIST_ID | — | — |
| 9 | FulfillLinePEOAssessableValue | ASSESSABLE_VALUE | — | — |
| 10 | FulfillLinePEOAssetGroupNumber | ASSET_GROUP_NUMBER | — | — |
| 11 | FulfillLinePEOAssetTrackedFlag | ASSET_TRACKED_FLAG | — | — |
| 12 | FulfillLinePEOBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 13 | FulfillLinePEOBillToContactPointId | BILL_TO_CONTACT_POINT_ID | — | — |
| 14 | FulfillLinePEOBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 15 | FulfillLinePEOBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 16 | FulfillLinePEOBillingTrxTypeId | BILLING_TRX_TYPE_ID | — | — |
| 17 | FulfillLinePEOBuyerId | BUYER_ID | — | — |
| 18 | FulfillLinePEOCancelReasonCode | CANCEL_REASON_CODE | — | — |
| 19 | FulfillLinePEOCanceledFlag1 | CANCELED_FLAG | — | — |
| 20 | FulfillLinePEOCanceledQty1 | CANCELED_QTY | — | ✅ |
| 21 | FulfillLinePEOCarrierId | CARRIER_ID | — | — |
| 22 | FulfillLinePEOCategoryCode1 | CATEGORY_CODE | — | — |
| 23 | FulfillLinePEOComments | COMMENTS | — | — |
| 24 | FulfillLinePEOCompSeqPath1 | COMP_SEQ_PATH | — | — |
| 25 | FulfillLinePEOComponentIdPath | COMPONENT_ID_PATH | — | — |
| 26 | FulfillLinePEOConfigCreationDate | CONFIG_CREATION_DATE | — | — |
| 27 | FulfillLinePEOConfigHeaderId | CONFIG_HEADER_ID | — | — |
| 28 | FulfillLinePEOConfigInventoryItemId | CONFIG_INVENTORY_ITEM_ID | — | — |
| 29 | FulfillLinePEOConfigItemReference | CONFIG_ITEM_REFERENCE | — | — |
| 30 | FulfillLinePEOConfigRevisionNumber | CONFIG_REVISION_NUMBER | — | — |
| 31 | FulfillLinePEOConfigTradeComplResultCode | CONFIG_TRADE_COMPL_RESULT_CODE | — | — |
| 32 | FulfillLinePEOConfiguratorPath | CONFIGURATOR_PATH | — | — |
| 33 | FulfillLinePEOContractEndDate | CONTRACT_END_DATE | — | — |
| 34 | FulfillLinePEOContractStartDate | CONTRACT_START_DATE | — | — |
| 35 | FulfillLinePEOCreatedBy4 | CREATED_BY | — | — |
| 36 | FulfillLinePEOCreatedInRelease | CREATED_IN_RELEASE | — | — |
| 37 | FulfillLinePEOCreationDate4 | CREATION_DATE | — | — |
| 38 | FulfillLinePEOCreditChkAuthExpDate | CREDIT_CHK_AUTH_EXP_DATE | — | — |
| 39 | FulfillLinePEOCreditChkAuthNum | CREDIT_CHK_AUTH_NUM | — | — |
| 40 | FulfillLinePEOCustomerItemId | CUSTOMER_ITEM_ID | — | — |
| 41 | FulfillLinePEOCustomerPoLineNumber | CUSTOMER_PO_LINE_NUMBER | — | — |
| 42 | FulfillLinePEOCustomerPoNumber | CUSTOMER_PO_NUMBER | — | — |
| 43 | FulfillLinePEOCustomerPoScheduleNumber | CUSTOMER_PO_SCHEDULE_NUMBER | — | — |
| 44 | FulfillLinePEODefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 45 | FulfillLinePEODeltaType1 | DELTA_TYPE | — | — |
| 46 | FulfillLinePEODemandClassCode | DEMAND_CLASS_CODE | — | — |
| 47 | FulfillLinePEODestinationLocationId | DESTINATION_LOCATION_ID | — | — |
| 48 | FulfillLinePEODestinationOrgId | DESTINATION_ORG_ID | — | — |
| 49 | FulfillLinePEODocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 50 | FulfillLinePEOEarliestAcceptableShipDate | EARLIEST_ACCEPTABLE_SHIP_DATE | — | — |
| 51 | FulfillLinePEOEstimateFulfillmentCost | ESTIMATE_FULFILLMENT_COST | — | — |
| 52 | FulfillLinePEOEstimateMargin | ESTIMATE_MARGIN | — | — |
| 53 | FulfillLinePEOExemptionCertificateNumber | EXEMPTION_CERTIFICATE_NUMBER | — | — |
| 54 | FulfillLinePEOExtendedAmount1 | EXTENDED_AMOUNT | — | — |
| 55 | FulfillLinePEOFinalDischargeLocationId | FINAL_DISCHARGE_LOCATION_ID | — | — |
| 56 | FulfillLinePEOFirstPtyRegId | FIRST_PTY_REG_ID | — | — |
| 57 | FulfillLinePEOFobPointCode | FOB_POINT_CODE | — | — |
| 58 | FulfillLinePEOFreightTermsCode | FREIGHT_TERMS_CODE | — | — |
| 59 | FulfillLinePEOFulfillInstanceId | FULFILL_INSTANCE_ID | — | — |
| 60 | FulfillLinePEOFulfillLineId | FULFILL_LINE_ID | — | — |
| 61 | FulfillLinePEOFulfillLineNumber | FULFILL_LINE_NUMBER | — | — |
| 62 | FulfillLinePEOFulfillOrgId | FULFILL_ORG_ID | — | — |
| 63 | FulfillLinePEOFulfillToleranceAbove | FULFILL_TOLERANCE_ABOVE | — | — |
| 64 | FulfillLinePEOFulfillToleranceBelow | FULFILL_TOLERANCE_BELOW | — | — |
| 65 | FulfillLinePEOFulfilledQty1 | FULFILLED_QTY | — | ✅ |
| 66 | FulfillLinePEOFulfillmentDate1 | FULFILLMENT_DATE | — | — |
| 67 | FulfillLinePEOFulfillmentMode | FULFILLMENT_MODE | — | — |
| 68 | FulfillLinePEOFulfillmentSplitRefId | FULFILLMENT_SPLIT_REF_ID | — | — |
| 69 | FulfillLinePEOGopReferenceId | GOP_REFERENCE_ID | — | — |
| 70 | FulfillLinePEOGopRequestRegion | GOP_REQUEST_REGION | — | — |
| 71 | FulfillLinePEOHeaderId1 | HEADER_ID | — | — |
| 72 | FulfillLinePEOIntendedUseClassifId | INTENDED_USE_CLASSIF_ID | — | — |
| 73 | FulfillLinePEOInventoryItemId3 | INVENTORY_ITEM_ID | — | — |
| 74 | FulfillLinePEOInventoryOrganizationId1 | INVENTORY_ORGANIZATION_ID | — | — |
| 75 | FulfillLinePEOInvoiceEnabledFlag | INVOICE_ENABLED_FLAG | — | — |
| 76 | FulfillLinePEOInvoiceInterfacedFlag | INVOICE_INTERFACED_FLAG | — | — |
| 77 | FulfillLinePEOInvoiceableItemFlag | INVOICEABLE_ITEM_FLAG | — | — |
| 78 | FulfillLinePEOInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 79 | FulfillLinePEOItemSubTypeCode | ITEM_SUB_TYPE_CODE | — | — |
| 80 | FulfillLinePEOItemTypeCode1 | ITEM_TYPE_CODE | — | — |
| 81 | FulfillLinePEOLastUpdateDate4 | LAST_UPDATE_DATE | — | ✅ |
| 82 | FulfillLinePEOLastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 83 | FulfillLinePEOLastUpdatedBy4 | LAST_UPDATED_BY | — | — |
| 84 | FulfillLinePEOLatestAcceptableArrivalDate | LATEST_ACCEPTABLE_ARRIVAL_DATE | — | — |
| 85 | FulfillLinePEOLatestAcceptableShipDate | LATEST_ACCEPTABLE_SHIP_DATE | — | — |
| 86 | FulfillLinePEOLineId2 | LINE_ID | — | — |
| 87 | FulfillLinePEOLineTypeCode1 | LINE_TYPE_CODE | — | — |
| 88 | FulfillLinePEOObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 89 | FulfillLinePEOOnHold1 | ON_HOLD | — | — |
| 90 | FulfillLinePEOOpenFlag1 | OPEN_FLAG | — | — |
| 91 | FulfillLinePEOOrderedQty1 | ORDERED_QTY | — | ✅ |
| 92 | FulfillLinePEOOrderedUom1 | ORDERED_UOM | — | — |
| 93 | FulfillLinePEOOrgId1 | ORG_ID | — | — |
| 94 | FulfillLinePEOOrigSysDocumentLineRef1 | ORIG_SYS_DOCUMENT_LINE_REF | — | — |
| 95 | FulfillLinePEOOrigSysDocumentRef1 | ORIG_SYS_DOCUMENT_REF | — | — |
| 96 | FulfillLinePEOOriginalInventoryItemId | ORIGINAL_INVENTORY_ITEM_ID | — | — |
| 97 | FulfillLinePEOOverrideScheduleDateFlag | OVERRIDE_SCHEDULE_DATE_FLAG | — | — |
| 98 | FulfillLinePEOOwnerId1 | OWNER_ID | — | — |
| 99 | FulfillLinePEOPackingInstructions | PACKING_INSTRUCTIONS | — | — |
| 100 | FulfillLinePEOParentFulfillLineId | PARENT_FULFILL_LINE_ID | — | — |
| 101 | FulfillLinePEOPartialShipAllowedFlag | PARTIAL_SHIP_ALLOWED_FLAG | — | — |
| 102 | FulfillLinePEOPaymentTermId | PAYMENT_TERM_ID | — | — |
| 103 | FulfillLinePEOPoStatusCode | PO_STATUS_CODE | — | — |
| 104 | FulfillLinePEOPricedOn | PRICED_ON | — | — |
| 105 | FulfillLinePEOProcessInstanceId | PROCESS_INSTANCE_ID | — | — |
| 106 | FulfillLinePEOProcessNumber | PROCESS_NUMBER | — | — |
| 107 | FulfillLinePEOProcessSet | PROCESS_SET | — | — |
| 108 | FulfillLinePEOProdFcCategId | PROD_FC_CATEG_ID | — | — |
| 109 | FulfillLinePEOProductCategory | PRODUCT_CATEGORY | — | — |
| 110 | FulfillLinePEOProductType | PRODUCT_TYPE | — | — |
| 111 | FulfillLinePEOPromiseArrivalDate | PROMISE_ARRIVAL_DATE | — | — |
| 112 | FulfillLinePEOPromiseShipDate | PROMISE_SHIP_DATE | — | — |
| 113 | FulfillLinePEOPurchasingEnabledFlag | PURCHASING_ENABLED_FLAG | — | — |
| 114 | FulfillLinePEOPurchasingUom | PURCHASING_UOM | — | — |
| 115 | FulfillLinePEOQuantityPerModel | QUANTITY_PER_MODEL | — | — |
| 116 | FulfillLinePEOReceivablesOrgId | RECEIVABLES_ORG_ID | — | — |
| 117 | FulfillLinePEOReferenceFlineId | REFERENCE_FLINE_ID | — | — |
| 118 | FulfillLinePEORemnantFlag | REMNANT_FLAG | — | — |
| 119 | FulfillLinePEORequestArrivalDate | REQUEST_ARRIVAL_DATE | — | — |
| 120 | FulfillLinePEORequestCancelDate | REQUEST_CANCEL_DATE | — | — |
| 121 | FulfillLinePEORequestShipDate | REQUEST_SHIP_DATE | — | — |
| 122 | FulfillLinePEORequestType | REQUEST_TYPE | — | — |
| 123 | FulfillLinePEORequiredFulfillmentDate | REQUIRED_FULFILLMENT_DATE | — | — |
| 124 | FulfillLinePEORequisitionBuId | REQUISITION_BU_ID | — | — |
| 125 | FulfillLinePEORequisitionInventoryOrgId | REQUISITION_INVENTORY_ORG_ID | — | — |
| 126 | FulfillLinePEOReservableFlag | RESERVABLE_FLAG | — | — |
| 127 | FulfillLinePEOReservationId | RESERVATION_ID | — | — |
| 128 | FulfillLinePEOReservedQty | RESERVED_QTY | — | — |
| 129 | FulfillLinePEOReturnReasonCode1 | RETURN_REASON_CODE | — | — |
| 130 | FulfillLinePEOReturnableFlag | RETURNABLE_FLAG | — | — |
| 131 | FulfillLinePEORmaDeliveredQty1 | RMA_DELIVERED_QTY | — | — |
| 132 | FulfillLinePEORootParentFulfillLineId | ROOT_PARENT_FULFILL_LINE_ID | — | — |
| 133 | FulfillLinePEOSalesProductTypeCode | SALES_PRODUCT_TYPE_CODE | — | — |
| 134 | FulfillLinePEOSalespersonId | SALESPERSON_ID | — | — |
| 135 | FulfillLinePEOScheduleArrivalDate | SCHEDULE_ARRIVAL_DATE | — | — |
| 136 | FulfillLinePEOScheduleShipDate1 | SCHEDULE_SHIP_DATE | — | — |
| 137 | FulfillLinePEOSchedulingReasonCode | SCHEDULING_REASON_CODE | — | — |
| 138 | FulfillLinePEOServiceCancelDate | SERVICE_CANCEL_DATE | — | — |
| 139 | FulfillLinePEOServiceDuration | SERVICE_DURATION | — | — |
| 140 | FulfillLinePEOServiceDurationPeriodCode | SERVICE_DURATION_PERIOD_CODE | — | — |
| 141 | FulfillLinePEOShipClassOfService | SHIP_CLASS_OF_SERVICE | — | — |
| 142 | FulfillLinePEOShipModeOfTransport | SHIP_MODE_OF_TRANSPORT | — | — |
| 143 | FulfillLinePEOShipSetName | SHIP_SET_NAME | — | — |
| 144 | FulfillLinePEOShipToContactId1 | SHIP_TO_CONTACT_ID | — | — |
| 145 | FulfillLinePEOShipToContactPointId | SHIP_TO_CONTACT_POINT_ID | — | — |
| 146 | FulfillLinePEOShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 147 | FulfillLinePEOShipToPartyContactId | SHIP_TO_PARTY_CONTACT_ID | — | — |
| 148 | FulfillLinePEOShipToPartyId | SHIP_TO_PARTY_ID | — | — |
| 149 | FulfillLinePEOShipToPartySiteId | SHIP_TO_PARTY_SITE_ID | — | — |
| 150 | FulfillLinePEOShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 151 | FulfillLinePEOShipmentPriorityCode | SHIPMENT_PRIORITY_CODE | — | — |
| 152 | FulfillLinePEOShippableFlag | SHIPPABLE_FLAG | — | — |
| 153 | FulfillLinePEOShippedQty1 | SHIPPED_QTY | — | ✅ |
| 154 | FulfillLinePEOShippedUom | SHIPPED_UOM | — | — |
| 155 | FulfillLinePEOShippingInstructions | SHIPPING_INSTRUCTIONS | — | — |
| 156 | FulfillLinePEOShowInSales | SHOW_IN_SALES | — | — |
| 157 | FulfillLinePEOSourceLineId1 | SOURCE_LINE_ID | — | — |
| 158 | FulfillLinePEOSourceLineNumber1 | SOURCE_LINE_NUMBER | — | — |
| 159 | FulfillLinePEOSourceOrderId1 | SOURCE_ORDER_ID | — | — |
| 160 | FulfillLinePEOSourceOrderNumber1 | SOURCE_ORDER_NUMBER | — | — |
| 161 | FulfillLinePEOSourceOrderSystem1 | SOURCE_ORDER_SYSTEM | — | — |
| 162 | FulfillLinePEOSourceOrgId1 | SOURCE_ORG_ID | — | — |
| 163 | FulfillLinePEOSourceRevisionNumber | SOURCE_REVISION_NUMBER | — | — |
| 164 | FulfillLinePEOSourceScheduleId1 | SOURCE_SCHEDULE_ID | — | — |
| 165 | FulfillLinePEOSourceScheduleNumber1 | SOURCE_SCHEDULE_NUMBER | — | — |
| 166 | FulfillLinePEOSplitFromFlineId | SPLIT_FROM_FLINE_ID | — | — |
| 167 | FulfillLinePEOStatusCode1 | STATUS_CODE | — | — |
| 168 | FulfillLinePEOStatusRulesetId | STATUS_RULESET_ID | — | — |
| 169 | FulfillLinePEOSubinventory | SUBINVENTORY | — | — |
| 170 | FulfillLinePEOSubstituteAllowedFlag | SUBSTITUTE_ALLOWED_FLAG | — | — |
| 171 | FulfillLinePEOSubstituteReasonCode | SUBSTITUTE_REASON_CODE | — | — |
| 172 | FulfillLinePEOSupplierId | SUPPLIER_ID | — | — |
| 173 | FulfillLinePEOSupplierSiteId | SUPPLIER_SITE_ID | — | — |
| 174 | FulfillLinePEOSupplyStatusCode | SUPPLY_STATUS_CODE | — | — |
| 175 | FulfillLinePEOTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 176 | FulfillLinePEOTaxExemptFlag | TAX_EXEMPT_FLAG | — | — |
| 177 | FulfillLinePEOTaxExemptionReasonCode | TAX_EXEMPTION_REASON_CODE | — | — |
| 178 | FulfillLinePEOTaxInvoiceDate | TAX_INVOICE_DATE | — | — |
| 179 | FulfillLinePEOTaxInvoiceNumber | TAX_INVOICE_NUMBER | — | — |
| 180 | FulfillLinePEOThirdPtyRegId | THIRD_PTY_REG_ID | — | — |
| 181 | FulfillLinePEOTotalContractAmount | TOTAL_CONTRACT_AMOUNT | — | — |
| 182 | FulfillLinePEOTotalContractQuantity | TOTAL_CONTRACT_QUANTITY | — | — |
| 183 | FulfillLinePEOTradeComplianceDate | TRADE_COMPLIANCE_DATE | — | — |
| 184 | FulfillLinePEOTradeComplianceResultCode | TRADE_COMPLIANCE_RESULT_CODE | — | — |
| 185 | FulfillLinePEOTransportationPlannedFlag | TRANSPORTATION_PLANNED_FLAG | — | — |
| 186 | FulfillLinePEOTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 187 | FulfillLinePEOUnitListPrice1 | UNIT_LIST_PRICE | — | — |
| 188 | FulfillLinePEOUnitQuantity | UNIT_QUANTITY | — | — |
| 189 | FulfillLinePEOUnitSellingPrice1 | UNIT_SELLING_PRICE | — | — |
| 190 | FulfillLinePEOUnreferencedReturnFlag | UNREFERENCED_RETURN_FLAG | — | — |
| 191 | FulfillLinePEOUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 192 | FulfillLinePEOValidConfigurationFlag | VALID_CONFIGURATION_FLAG | — | — |

### [[doo_lines_all|DOO_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LinePEOActualShipDate1 | ACTUAL_SHIP_DATE | — | — |
| 2 | LinePEOCanceledFlag | CANCELED_FLAG | — | — |
| 3 | LinePEOCanceledQty | CANCELED_QTY | — | — |
| 4 | LinePEOCategoryCode | CATEGORY_CODE | — | — |
| 5 | LinePEOCompSeqPath | COMP_SEQ_PATH | — | — |
| 6 | LinePEOCreatedBy3 | CREATED_BY | — | — |
| 7 | LinePEOCreationDate3 | CREATION_DATE | — | — |
| 8 | LinePEODeltaType | DELTA_TYPE | — | — |
| 9 | LinePEODisplayLineNumber | DISPLAY_LINE_NUMBER | — | — |
| 10 | LinePEOExtendedAmount | EXTENDED_AMOUNT | — | — |
| 11 | LinePEOFulfilledQty | FULFILLED_QTY | — | — |
| 12 | LinePEOFulfillmentDate | FULFILLMENT_DATE | — | — |
| 13 | LinePEOHeaderId | HEADER_ID | — | — |
| 14 | LinePEOInventoryItemId2 | INVENTORY_ITEM_ID | — | — |
| 15 | LinePEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 16 | LinePEOItemTypeCode | ITEM_TYPE_CODE | — | — |
| 17 | LinePEOLastUpdateDate3 | LAST_UPDATE_DATE | — | ✅ |
| 18 | LinePEOLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 19 | LinePEOLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 20 | LinePEOLineId1 | LINE_ID | — | ✅ |
| 21 | LinePEOLineNumber | LINE_NUMBER | — | — |
| 22 | LinePEOLineTypeCode | LINE_TYPE_CODE | — | — |
| 23 | LinePEOObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 24 | LinePEOOnHold | ON_HOLD | — | — |
| 25 | LinePEOOpenFlag | OPEN_FLAG | — | — |
| 26 | LinePEOOrderedQty | ORDERED_QTY | — | — |
| 27 | LinePEOOrderedUom | ORDERED_UOM | — | — |
| 28 | LinePEOOrgId | ORG_ID | — | — |
| 29 | LinePEOOrigSysDocumentLineRef | ORIG_SYS_DOCUMENT_LINE_REF | — | — |
| 30 | LinePEOOrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | — |
| 31 | LinePEOOwnerId | OWNER_ID | — | — |
| 32 | LinePEOParentLineId | PARENT_LINE_ID | — | — |
| 33 | LinePEOReferenceLineId | REFERENCE_LINE_ID | — | — |
| 34 | LinePEORmaDeliveredQty | RMA_DELIVERED_QTY | — | — |
| 35 | LinePEORootParentLineId | ROOT_PARENT_LINE_ID | — | — |
| 36 | LinePEOScheduleShipDate | SCHEDULE_SHIP_DATE | — | — |
| 37 | LinePEOShippedQty | SHIPPED_QTY | — | — |
| 38 | LinePEOSourceLineId | SOURCE_LINE_ID | — | — |
| 39 | LinePEOSourceLineNumber | SOURCE_LINE_NUMBER | — | — |
| 40 | LinePEOSourceOrderId | SOURCE_ORDER_ID | — | — |
| 41 | LinePEOSourceOrderNumber | SOURCE_ORDER_NUMBER | — | — |
| 42 | LinePEOSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | — |
| 43 | LinePEOSourceOrgId | SOURCE_ORG_ID | — | — |
| 44 | LinePEOSourceScheduleId | SOURCE_SCHEDULE_ID | — | — |
| 45 | LinePEOSourceScheduleNumber | SOURCE_SCHEDULE_NUMBER | — | — |
| 46 | LinePEOStatusCode | STATUS_CODE | — | — |
| 47 | LinePEOTransformFromLineId | TRANSFORM_FROM_LINE_ID | — | — |
| 48 | LinePEOUnitListPrice | UNIT_LIST_PRICE | — | — |
| 49 | LinePEOUnitSellingPrice | UNIT_SELLING_PRICE | — | — |

### [[hz_party_sites|HZ_PARTY_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartySitePEOActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | PartySitePEOAddressee | ADDRESSEE | — | — |
| 3 | PartySitePEOComments | COMMENTS | — | — |
| 4 | PartySitePEOCorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 5 | PartySitePEOCreatedBy | CREATED_BY | — | — |
| 6 | PartySitePEOCreatedByModule | CREATED_BY_MODULE | — | — |
| 7 | PartySitePEOCreationDate | CREATION_DATE | — | — |
| 8 | PartySitePEOCurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 9 | PartySitePEOCurrencyCode | CURRENCY_CODE | — | — |
| 10 | PartySitePEODunsNumberC | DUNS_NUMBER_C | — | — |
| 11 | PartySitePEOEndDateActive | END_DATE_ACTIVE | — | — |
| 12 | PartySitePEOGlobalLocationNumber | GLOBAL_LOCATION_NUMBER | — | — |
| 13 | PartySitePEOIdentifyingAddressFlag | IDENTIFYING_ADDRESS_FLAG | — | — |
| 14 | PartySitePEOLanguage | PARTY_SITE_LANGUAGE | — | — |
| 15 | PartySitePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | PartySitePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | PartySitePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | PartySitePEOLocationId | LOCATION_ID | — | — |
| 19 | PartySitePEOMailstop | MAILSTOP | — | — |
| 20 | PartySitePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | PartySitePEOOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 22 | PartySitePEOOverallPrimaryFlag | OVERALL_PRIMARY_FLAG | — | — |
| 23 | PartySitePEOPartyId | PARTY_ID | — | — |
| 24 | PartySitePEOPartyNameDba | PARTY_NAME_DBA | — | — |
| 25 | PartySitePEOPartyNameDivision | PARTY_NAME_DIVISION | — | — |
| 26 | PartySitePEOPartyNameLegal | PARTY_NAME_LEGAL | — | — |
| 27 | PartySitePEOPartySiteId | PARTY_SITE_ID | — | — |
| 28 | PartySitePEOPartySiteName | PARTY_SITE_NAME | — | — |
| 29 | PartySitePEOPartySiteNumber | PARTY_SITE_NUMBER | — | — |
| 30 | PartySitePEOPartySiteType | PARTY_SITE_TYPE | — | — |
| 31 | PartySitePEOPartyUsageCode | PARTY_USAGE_CODE | — | — |
| 32 | PartySitePEORelationshipId | RELATIONSHIP_ID | — | — |
| 33 | PartySitePEOStartDateActive | START_DATE_ACTIVE | — | — |
| 34 | PartySitePEOStatus | STATUS | — | — |

### [[qp_charge_definitions_vl|QP_CHARGE_DEFINITIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChargeDefinitionPEOActiveFlag | ACTIVE_FLAG | — | — |
| 2 | ChargeDefinitionPEOAppliesToCode | APPLIES_TO_CODE | — | — |
| 3 | ChargeDefinitionPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | ChargeDefinitionPEOCalculateMarginFlag | CALCULATE_MARGIN_FLAG | — | — |
| 5 | ChargeDefinitionPEOChargeDefinitionCode1 | CHARGE_DEFINITION_CODE | — | — |
| 6 | ChargeDefinitionPEOChargeDefinitionId | CHARGE_DEFINITION_ID | — | — |
| 7 | ChargeDefinitionPEOChargeDefinitionId1 | CHARGE_DEFINITION_ID | — | — |
| 8 | ChargeDefinitionPEOChargeSubtypeCode1 | CHARGE_SUBTYPE_CODE | — | — |
| 9 | ChargeDefinitionPEOChargeTypeCode1 | CHARGE_TYPE_CODE | — | — |
| 10 | ChargeDefinitionPEOCreatedBy5 | CREATED_BY | — | — |
| 11 | ChargeDefinitionPEOCreationDate5 | CREATION_DATE | — | — |
| 12 | ChargeDefinitionPEODescription | DESCRIPTION | — | — |
| 13 | ChargeDefinitionPEOLastUpdateDate5 | LAST_UPDATE_DATE | — | ✅ |
| 14 | ChargeDefinitionPEOLastUpdateLogin5 | LAST_UPDATE_LOGIN | — | — |
| 15 | ChargeDefinitionPEOLastUpdatedBy5 | LAST_UPDATED_BY | — | — |
| 16 | ChargeDefinitionPEOName | NAME | — | ✅ |
| 17 | ChargeDefinitionPEOObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |
| 18 | ChargeDefinitionPEOPricePeriodicityUomClass | PRICE_PERIODICITY_UOM_CLASS | — | — |
| 19 | ChargeDefinitionPEOPriceTypeCode1 | PRICE_TYPE_CODE | — | — |
| 20 | ChargeDefinitionPEORefundableFlag | REFUNDABLE_FLAG | — | — |
| 21 | ChargeDefinitionPEOSetupEnabledFlag | SETUP_ENABLED_FLAG | — | — |
| 22 | ChargeDefinitionPEOUsageUomClass | USAGE_UOM_CLASS | — | — |

### [[qp_price_elements_vl|QP_PRICE_ELEMENTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PriceElementPEOActiveFlag | ACTIVE_FLAG | — | — |
| 2 | PriceElementPEOCreatedBy | CREATED_BY | — | — |
| 3 | PriceElementPEOCreationDate | CREATION_DATE | — | — |
| 4 | PriceElementPEOElementCode | ELEMENT_CODE | — | — |
| 5 | PriceElementPEOElementTypeCode | ELEMENT_TYPE_CODE | — | — |
| 6 | PriceElementPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PriceElementPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | PriceElementPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | PriceElementPEOName | NAME | — | ✅ |
| 10 | PriceElementPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | PriceElementPEOPriceElementId | PRICE_ELEMENT_ID | — | — |
| 12 | PriceElementPEOPricingGuidelineEnabledFlag | PRICING_GUIDELINE_ENABLED_FLAG | — | — |
| 13 | PriceElementPEOSeededFlag | SEEDED_FLAG | — | — |

### [[qp_pricing_strategies_vl|QP_PRICING_STRATEGIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PricingStrategyPEOAllowCurrencyOverrideFlag | ALLOW_CURRENCY_OVERRIDE_FLAG | — | — |
| 2 | PricingStrategyPEOAllowPriceListOverrideFlag | ALLOW_PRICE_LIST_OVERRIDE_FLAG | — | — |
| 3 | PricingStrategyPEOAttributeCategory1 | ATTRIBUTE_CATEGORY | — | — |
| 4 | PricingStrategyPEOCreatedBy8 | CREATED_BY | — | — |
| 5 | PricingStrategyPEOCreationDate8 | CREATION_DATE | — | — |
| 6 | PricingStrategyPEODefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | — |
| 7 | PricingStrategyPEODefaultGlConvTypeCode | DEFAULT_GL_CONV_TYPE_CODE | — | — |
| 8 | PricingStrategyPEODescription1 | DESCRIPTION | — | — |
| 9 | PricingStrategyPEOEndDate | END_DATE | — | — |
| 10 | PricingStrategyPEOLastUpdateDate8 | LAST_UPDATE_DATE | — | ✅ |
| 11 | PricingStrategyPEOLastUpdateLogin8 | LAST_UPDATE_LOGIN | — | — |
| 12 | PricingStrategyPEOLastUpdatedBy8 | LAST_UPDATED_BY | — | — |
| 13 | PricingStrategyPEOName1 | NAME | — | ✅ |
| 14 | PricingStrategyPEOObjectVersionNumber9 | OBJECT_VERSION_NUMBER | — | — |
| 15 | PricingStrategyPEOObjectiveCode | OBJECTIVE_CODE | — | — |
| 16 | PricingStrategyPEOOrgId3 | ORG_ID | — | — |
| 17 | PricingStrategyPEOPricingStrategyId1 | PRICING_STRATEGY_ID | — | — |
| 18 | PricingStrategyPEOPricingStrategyId2 | PRICING_STRATEGY_ID | — | — |
| 19 | PricingStrategyPEOStartDate | START_DATE | — | — |
| 20 | PricingStrategyPEOStatusCode2 | STATUS_CODE | — | — |

### [[rcl_inv_transfer_orders_v|RCL_INV_TRANSFER_ORDERS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InventoryTransferOrderPEOActualShipDate | ACTUAL_SHIP_DATE | — | — |
| 2 | InventoryTransferOrderPEODeliveryDetailId | DELIVERY_DETAIL_ID | — | — |
| 3 | InventoryTransferOrderPEOLineId | LINE_ID | — | — |
| 4 | InventoryTransferOrderPEOReceiptDate | RECEIPT_DATE | — | — |
| 5 | InventoryTransferOrderPEOReceiptNum | RECEIPT_NUM | — | — |
| 6 | InventoryTransferOrderPEOShipmentHeaderId | SHIPMENT_HEADER_ID | — | — |
| 7 | InventoryTransferOrderPEOShipmentLineId | SHIPMENT_LINE_ID | — | — |
| 8 | InventoryTransferOrderPEOShipmentNum | SHIPMENT_NUM | — | — |
| 9 | InventoryTransferOrderPEOShippedQuantity | SHIPPED_QUANTITY | — | — |

### [[rcl_parts_req_lines|RCL_PARTS_REQ_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartsReqLinesPEOCreatedBy1 | CREATED_BY | — | — |
| 2 | PartsReqLinesPEOCreationDate1 | CREATION_DATE | — | — |
| 3 | PartsReqLinesPEODestinationOrganizationId | DESTINATION_ORGANIZATION_ID | — | — |
| 4 | PartsReqLinesPEODestinationSubinventory | DESTINATION_SUBINVENTORY | — | ✅ |
| 5 | PartsReqLinesPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 6 | PartsReqLinesPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 7 | PartsReqLinesPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 8 | PartsReqLinesPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 9 | PartsReqLinesPEONeedByDate | NEED_BY_DATE | — | ✅ |
| 10 | PartsReqLinesPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 11 | PartsReqLinesPEOParentEntityCode | PARENT_ENTITY_CODE | — | ✅ |
| 12 | PartsReqLinesPEOParentEntityId | PARENT_ENTITY_ID | — | ✅ |
| 13 | PartsReqLinesPEOQuantity | QUANTITY | — | ✅ |
| 14 | PartsReqLinesPEORequirementHeaderId | REQUIREMENT_HEADER_ID | — | — |
| 15 | PartsReqLinesPEORequirementLineId1 | REQUIREMENT_LINE_ID | — | ✅ |
| 16 | PartsReqLinesPEOReturnReasonCode | RETURN_REASON_CODE | — | — |
| 17 | PartsReqLinesPEORevision | REVISION | — | ✅ |
| 18 | PartsReqLinesPEOServiceActivityId | SERVICE_ACTIVITY_ID | — | — |
| 19 | PartsReqLinesPEOShipToAddressType | SHIP_TO_ADDRESS_TYPE | — | ✅ |
| 20 | PartsReqLinesPEOShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 21 | PartsReqLinesPEOShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 22 | PartsReqLinesPEOUomCode | UOM_CODE | — | ✅ |

### [[rcl_parts_req_line_details|RCL_PARTS_REQ_LINE_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartsReqLineDetailsPEOCreatedBy | CREATED_BY | — | — |
| 2 | PartsReqLineDetailsPEOCreationDate | CREATION_DATE | — | — |
| 3 | PartsReqLineDetailsPEOExpectedArrivalDate | EXPECTED_ARRIVAL_DATE | — | — |
| 4 | PartsReqLineDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PartsReqLineDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | PartsReqLineDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | PartsReqLineDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | PartsReqLineDetailsPEOReqLineDetailId | REQ_LINE_DETAIL_ID | 🔑 | ✅ |
| 9 | PartsReqLineDetailsPEORequirementLineId | REQUIREMENT_LINE_ID | — | — |
| 10 | PartsReqLineDetailsPEOSourceCarrierId | SOURCE_CARRIER_ID | — | — |
| 11 | PartsReqLineDetailsPEOSourceId | SOURCE_ID | — | ✅ |
| 12 | PartsReqLineDetailsPEOSourceModeOfTransport | SOURCE_MODE_OF_TRANSPORT | — | — |
| 13 | PartsReqLineDetailsPEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 14 | PartsReqLineDetailsPEOSourceRequestDate | SOURCE_REQUEST_DATE | — | — |
| 15 | PartsReqLineDetailsPEOSourceServiceLevels | SOURCE_SERVICE_LEVELS | — | — |
| 16 | PartsReqLineDetailsPEOSourceSubinventory | SOURCE_SUBINVENTORY | — | ✅ |
| 17 | PartsReqLineDetailsPEOSourceType | SOURCE_TYPE | — | ✅ |

### [[rcl_pricing_headers|RCL_PRICING_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PricingHeadersPEOAppliedCurrencyCode | APPLIED_CURRENCY_CODE | — | ✅ |
| 2 | PricingHeadersPEOCreatedBy7 | CREATED_BY | — | — |
| 3 | PricingHeadersPEOCreationDate7 | CREATION_DATE | — | — |
| 4 | PricingHeadersPEOLastUpdateDate7 | LAST_UPDATE_DATE | — | ✅ |
| 5 | PricingHeadersPEOLastUpdateLogin7 | LAST_UPDATE_LOGIN | — | — |
| 6 | PricingHeadersPEOLastUpdatedBy7 | LAST_UPDATED_BY | — | — |
| 7 | PricingHeadersPEOObjectVersionNumber8 | OBJECT_VERSION_NUMBER | — | — |
| 8 | PricingHeadersPEOOrgId2 | ORG_ID | — | — |
| 9 | PricingHeadersPEOPricedOn1 | PRICED_ON | — | — |
| 10 | PricingHeadersPEOPricingSegmentCode | PRICING_SEGMENT_CODE | — | ✅ |
| 11 | PricingHeadersPEOPricingSegmentExplanation | PRICING_SEGMENT_EXPLANATION | — | — |
| 12 | PricingHeadersPEOPricingStrategyExplanation | PRICING_STRATEGY_EXPLANATION | — | — |
| 13 | PricingHeadersPEOPricingStrategyId | PRICING_STRATEGY_ID | — | — |
| 14 | PricingHeadersPEORclPricingHeaderId | RCL_PRICING_HEADER_ID | — | ✅ |
| 15 | PricingHeadersPEOSegmentExplanationMsgName | SEGMENT_EXPLANATION_MSG_NAME | — | — |
| 16 | PricingHeadersPEOSoldToPartyId | SOLD_TO_PARTY_ID | — | — |
| 17 | PricingHeadersPEOSourceId1 | SOURCE_ID | — | — |
| 18 | PricingHeadersPEOSourceType1 | SOURCE_TYPE | — | — |
| 19 | PricingHeadersPEOStrategyExplanationMsgName | STRATEGY_EXPLANATION_MSG_NAME | — | — |

### [[rcl_service_charges|RCL_SERVICE_CHARGES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ServiceChargesPEOAvgUnitSellingPrice | AVG_UNIT_SELLING_PRICE | — | — |
| 2 | ServiceChargesPEOCanAdjustFlag | CAN_ADJUST_FLAG | — | — |
| 3 | ServiceChargesPEOChargeAppliesTo | CHARGE_APPLIES_TO | — | — |
| 4 | ServiceChargesPEOChargeCurrencyCode | CHARGE_CURRENCY_CODE | — | — |
| 5 | ServiceChargesPEOChargeDefinitionCode | CHARGE_DEFINITION_CODE | — | — |
| 6 | ServiceChargesPEOChargeSubtypeCode | CHARGE_SUBTYPE_CODE | — | — |
| 7 | ServiceChargesPEOChargeTypeCode | CHARGE_TYPE_CODE | — | — |
| 8 | ServiceChargesPEOCreatedBy6 | CREATED_BY | — | — |
| 9 | ServiceChargesPEOCreationDate6 | CREATION_DATE | — | — |
| 10 | ServiceChargesPEODeltaType2 | DELTA_TYPE | — | — |
| 11 | ServiceChargesPEOGsaUnitPrice | GSA_UNIT_PRICE | — | — |
| 12 | ServiceChargesPEOLastUpdateDate6 | LAST_UPDATE_DATE | — | ✅ |
| 13 | ServiceChargesPEOLastUpdateLogin6 | LAST_UPDATE_LOGIN | — | — |
| 14 | ServiceChargesPEOLastUpdatedBy6 | LAST_UPDATED_BY | — | — |
| 15 | ServiceChargesPEOModifiedFlag | MODIFIED_FLAG | — | — |
| 16 | ServiceChargesPEOObjectVersionNumber7 | OBJECT_VERSION_NUMBER | — | — |
| 17 | ServiceChargesPEOParentEntityCode1 | PARENT_ENTITY_CODE | — | ✅ |
| 18 | ServiceChargesPEOParentEntityId1 | PARENT_ENTITY_ID | — | ✅ |
| 19 | ServiceChargesPEOPricePeriodicityCode | PRICE_PERIODICITY_CODE | — | — |
| 20 | ServiceChargesPEOPriceTypeCode | PRICE_TYPE_CODE | — | — |
| 21 | ServiceChargesPEOPricedQuantity | PRICED_QUANTITY | — | — |
| 22 | ServiceChargesPEOPricedQuantityUomCode | PRICED_QUANTITY_UOM_CODE | — | — |
| 23 | ServiceChargesPEOPrimaryFlag | PRIMARY_FLAG | — | — |
| 24 | ServiceChargesPEOReferenceOrderChargeId | REFERENCE_ORDER_CHARGE_ID | — | — |
| 25 | ServiceChargesPEORollupFlag | ROLLUP_FLAG | — | — |
| 26 | ServiceChargesPEOSequenceNumber | SEQUENCE_NUMBER | — | — |
| 27 | ServiceChargesPEOServiceChargeId | SERVICE_CHARGE_ID | — | — |
| 28 | ServiceChargesPEOSourceChargeId | SOURCE_CHARGE_ID | — | — |

### [[rcl_service_charge_components|RCL_SERVICE_CHARGE_COMPONENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ServiceChargeComponentsPEOChargeCurrDurationExtAmt | CHARGE_CURR_DURATION_EXT_AMT | — | — |
| 2 | ServiceChargeComponentsPEOChargeCurrencyCode1 | CHARGE_CURRENCY_CODE | — | — |
| 3 | ServiceChargeComponentsPEOChargeCurrencyExtAmount | CHARGE_CURRENCY_EXT_AMOUNT | — | — |
| 4 | ServiceChargeComponentsPEOChargeCurrencyUnitPrice | CHARGE_CURRENCY_UNIT_PRICE | — | ✅ |
| 5 | ServiceChargeComponentsPEOCoverageProductId | COVERAGE_PRODUCT_ID | — | — |
| 6 | ServiceChargeComponentsPEOCreatedBy9 | CREATED_BY | — | — |
| 7 | ServiceChargeComponentsPEOCreationDate9 | CREATION_DATE | — | — |
| 8 | ServiceChargeComponentsPEODeltaType3 | DELTA_TYPE | — | — |
| 9 | ServiceChargeComponentsPEOExplanation | EXPLANATION | — | — |
| 10 | ServiceChargeComponentsPEOExplanationMessageName | EXPLANATION_MESSAGE_NAME | — | — |
| 11 | ServiceChargeComponentsPEOHeaderCurrDurationExtAmt | HEADER_CURR_DURATION_EXT_AMT | — | — |
| 12 | ServiceChargeComponentsPEOHeaderCurrencyCode | HEADER_CURRENCY_CODE | — | — |
| 13 | ServiceChargeComponentsPEOHeaderCurrencyExtAmount | HEADER_CURRENCY_EXT_AMOUNT | — | ✅ |
| 14 | ServiceChargeComponentsPEOHeaderCurrencyUnitPrice | HEADER_CURRENCY_UNIT_PRICE | — | ✅ |
| 15 | ServiceChargeComponentsPEOLastUpdateDate9 | LAST_UPDATE_DATE | — | ✅ |
| 16 | ServiceChargeComponentsPEOLastUpdateLogin9 | LAST_UPDATE_LOGIN | — | — |
| 17 | ServiceChargeComponentsPEOLastUpdatedBy9 | LAST_UPDATED_BY | — | — |
| 18 | ServiceChargeComponentsPEOModifiedFlag1 | MODIFIED_FLAG | — | — |
| 19 | ServiceChargeComponentsPEOObjectVersionNumber10 | OBJECT_VERSION_NUMBER | — | — |
| 20 | ServiceChargeComponentsPEOParentChargeComponentId | PARENT_CHARGE_COMPONENT_ID | — | — |
| 21 | ServiceChargeComponentsPEOPercentOfComparisonElement | PERCENT_OF_COMPARISON_ELEMENT | — | — |
| 22 | ServiceChargeComponentsPEOPriceElementCode | PRICE_ELEMENT_CODE | — | ✅ |
| 23 | ServiceChargeComponentsPEOPriceElementUsageCode | PRICE_ELEMENT_USAGE_CODE | — | — |
| 24 | ServiceChargeComponentsPEOPricingSourceId | PRICING_SOURCE_ID | — | — |
| 25 | ServiceChargeComponentsPEOPricingSourceTypeCode | PRICING_SOURCE_TYPE_CODE | — | — |
| 26 | ServiceChargeComponentsPEOReferenceSrvChargeCompId | REFERENCE_SRV_CHARGE_COMP_ID | — | — |
| 27 | ServiceChargeComponentsPEORollupFlag1 | ROLLUP_FLAG | — | — |
| 28 | ServiceChargeComponentsPEOSequenceNumber1 | SEQUENCE_NUMBER | — | — |
| 29 | ServiceChargeComponentsPEOServiceChargeComponentId | SERVICE_CHARGE_COMPONENT_ID | — | ✅ |
| 30 | ServiceChargeComponentsPEOServiceChargeId1 | SERVICE_CHARGE_ID | — | — |
| 31 | ServiceChargeComponentsPEOSourceChargeComponentId | SOURCE_CHARGE_COMPONENT_ID | — | — |
| 32 | ServiceChargeComponentsPEOSourceChargeId1 | SOURCE_CHARGE_ID | — | — |
| 33 | ServiceChargeComponentsPEOSourceMpaId | SOURCE_MPA_ID | — | — |
| 34 | ServiceChargeComponentsPEOSourceParentChargeCompId | SOURCE_PARENT_CHARGE_COMP_ID | — | — |
| 35 | ServiceChargeComponentsPEOTaxIncludedFlag | TAX_INCLUDED_FLAG | — | — |

### [[svc_service_requests|SVC_SERVICE_REQUESTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ServiceRequestUnsecuredPEOAccountPartyId | ACCOUNT_PARTY_ID | — | — |
| 2 | ServiceRequestUnsecuredPEOAssetId | ASSET_ID | — | — |
| 3 | ServiceRequestUnsecuredPEOAssigneeResourceId | ASSIGNEE_RESOURCE_ID | — | — |
| 4 | ServiceRequestUnsecuredPEOBUOrgId | BU_ORG_ID | — | — |
| 5 | ServiceRequestUnsecuredPEOCatalogId | CATALOG_ID | — | — |
| 6 | ServiceRequestUnsecuredPEOCategoryId | CATEGORY_ID | — | — |
| 7 | ServiceRequestUnsecuredPEOChannelTypeCd | CHANNEL_TYPE_CD | — | — |
| 8 | ServiceRequestUnsecuredPEOClosedDate | CLOSED_DATE | — | — |
| 9 | ServiceRequestUnsecuredPEOCorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 10 | ServiceRequestUnsecuredPEOCreatedBy2 | CREATED_BY | — | — |
| 11 | ServiceRequestUnsecuredPEOCreatedByPartyId | CREATED_BY_PARTY_ID | — | — |
| 12 | ServiceRequestUnsecuredPEOCreationDate2 | CREATION_DATE | — | — |
| 13 | ServiceRequestUnsecuredPEOCriticalFlag | CRITICAL_FLAG | — | — |
| 14 | ServiceRequestUnsecuredPEOCurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 15 | ServiceRequestUnsecuredPEOCurrencyCode | CURRENCY_CODE | — | — |
| 16 | ServiceRequestUnsecuredPEODeletedFlag | DELETED_FLAG | — | — |
| 17 | ServiceRequestUnsecuredPEOIBAssetId | IB_ASSET_ID | — | — |
| 18 | ServiceRequestUnsecuredPEOInternalPriorityCd | INTERNAL_PRIORITY_CD | — | — |
| 19 | ServiceRequestUnsecuredPEOInventoryItemId1 | INVENTORY_ITEM_ID | — | — |
| 20 | ServiceRequestUnsecuredPEOInventoryOrgId | INVENTORY_ORG_ID | — | — |
| 21 | ServiceRequestUnsecuredPEOLanguageCd | LANGUAGE_CD | — | — |
| 22 | ServiceRequestUnsecuredPEOLastReopenDate | LAST_REOPEN_DATE | — | — |
| 23 | ServiceRequestUnsecuredPEOLastResolvedDate | LAST_RESOLVED_DATE | — | — |
| 24 | ServiceRequestUnsecuredPEOLastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 25 | ServiceRequestUnsecuredPEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 26 | ServiceRequestUnsecuredPEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 27 | ServiceRequestUnsecuredPEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 28 | ServiceRequestUnsecuredPEOObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 29 | ServiceRequestUnsecuredPEOOpenDate | OPEN_DATE | — | — |
| 30 | ServiceRequestUnsecuredPEOOriginalSystemReference | ORIGINAL_SYSTEM_REFERENCE | — | — |
| 31 | ServiceRequestUnsecuredPEOOwnerTypeCd | OWNER_TYPE_CD | — | — |
| 32 | ServiceRequestUnsecuredPEOPartnerAccountPartyId | PARTNER_ACCOUNT_PARTY_ID | — | — |
| 33 | ServiceRequestUnsecuredPEOPrimaryContactPartyId | PRIMARY_CONTACT_PARTY_ID | — | — |
| 34 | ServiceRequestUnsecuredPEOProblemCd | PROBLEM_CD | — | — |
| 35 | ServiceRequestUnsecuredPEOProblemDesc | PROBLEM_DESC | — | — |
| 36 | ServiceRequestUnsecuredPEOProdGroupId | PROD_GROUP_ID | — | — |
| 37 | ServiceRequestUnsecuredPEOQueueId | QUEUE_ID | — | — |
| 38 | ServiceRequestUnsecuredPEOReportedByPartyId | REPORTED_BY_PARTY_ID | — | — |
| 39 | ServiceRequestUnsecuredPEOResolutionCd | RESOLUTION_CD | — | — |
| 40 | ServiceRequestUnsecuredPEOResolveDescription | RESOLVE_DESC | — | — |
| 41 | ServiceRequestUnsecuredPEOResolveOutcomeCd | RESOLVE_OUTCOME_CD | — | — |
| 42 | ServiceRequestUnsecuredPEOResolvedBy | RESOLVED_BY | — | — |
| 43 | ServiceRequestUnsecuredPEOSeverityCd | SEVERITY_CD | — | — |
| 44 | ServiceRequestUnsecuredPEOSourceCd | SOURCE_CD | — | — |
| 45 | ServiceRequestUnsecuredPEOSrCreatedBy | SR_CREATED_BY | — | — |
| 46 | ServiceRequestUnsecuredPEOSrId | SR_ID | — | — |
| 47 | ServiceRequestUnsecuredPEOSrId1 | SR_ID | — | — |
| 48 | ServiceRequestUnsecuredPEOSrLastUpdateDate | SR_LAST_UPDATE_DATE | — | ✅ |
| 49 | ServiceRequestUnsecuredPEOSrLastUpdateLogin | SR_LAST_UPDATE_LOGIN | — | — |
| 50 | ServiceRequestUnsecuredPEOSrLastUpdatedBy | SR_LAST_UPDATED_BY | — | — |
| 51 | ServiceRequestUnsecuredPEOSrNumber | SR_NUMBER | — | — |
| 52 | ServiceRequestUnsecuredPEOStatusCd | STATUS_CD | — | — |
| 53 | ServiceRequestUnsecuredPEOStatusTypeCd | STATUS_TYPE_CD | — | — |
| 54 | ServiceRequestUnsecuredPEOStripeCd | STRIPE_CD | — | — |
| 55 | ServiceRequestUnsecuredPEOTitle | TITLE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
