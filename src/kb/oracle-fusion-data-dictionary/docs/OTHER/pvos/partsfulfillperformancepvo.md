---
id: DOC-OTHER-PVO-PartsFulfillPerformancePVO
doc_type: system-doc
title: "PartsFulfillPerformancePVO — PVO Cross-Module"
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
  - PartsFulfillPerformancePVO
  - partsfulfillperformancepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PartsFulfillPerformancePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Parts Fulfill Performance. Acessa as tabelas: DOO_FULFILL_LINES_ALL, DOO_HEADERS_ALL, DOO_LINES_ALL (+6).

**Caminho:** `FscmTopModelAM.PartsAnalyticsAM.PartsFulfillPerformancePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 530 | 9 | 1 | 37 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[doo_fulfill_lines_all|DOO_FULFILL_LINES_ALL]] — 192 atributos (7 BICC)
- [[doo_headers_all|DOO_HEADERS_ALL]] — 85 atributos (2 BICC)
- [[doo_lines_all|DOO_LINES_ALL]] — 49 atributos (2 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 34 atributos (1 BICC)
- [[rcl_inv_transfer_orders_v|RCL_INV_TRANSFER_ORDERS_V]] — 10 atributos (6 BICC)
- [[rcl_parts_req_lines|RCL_PARTS_REQ_LINES]] — 22 atributos (10 BICC)
- [[rcl_parts_req_line_details|RCL_PARTS_REQ_LINE_DETAILS]] — 17 atributos (1 PKs, 6 BICC)
- [[svc_service_requests|SVC_SERVICE_REQUESTS]] — 53 atributos (2 BICC)
- [[svc_work_orders|SVC_WORK_ORDERS]] — 68 atributos (1 BICC)

---

## ⚙️ Atributos

### [[doo_fulfill_lines_all|DOO_FULFILL_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FulfillLinePEOAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 2 | FulfillLinePEOActionTypeCode | ACTION_TYPE_CODE | — | — |
| 3 | FulfillLinePEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | — |
| 4 | FulfillLinePEOActualShipDate1 | ACTUAL_SHIP_DATE | — | ✅ |
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
| 20 | FulfillLinePEOCarrierId | CARRIER_ID | — | — |
| 21 | FulfillLinePEOCategoryCode1 | CATEGORY_CODE | — | — |
| 22 | FulfillLinePEOComments | COMMENTS | — | — |
| 23 | FulfillLinePEOCompSeqPath1 | COMP_SEQ_PATH | — | — |
| 24 | FulfillLinePEOComponentIdPath | COMPONENT_ID_PATH | — | — |
| 25 | FulfillLinePEOConfigCreationDate | CONFIG_CREATION_DATE | — | — |
| 26 | FulfillLinePEOConfigHeaderId | CONFIG_HEADER_ID | — | — |
| 27 | FulfillLinePEOConfigInventoryItemId | CONFIG_INVENTORY_ITEM_ID | — | — |
| 28 | FulfillLinePEOConfigItemReference | CONFIG_ITEM_REFERENCE | — | — |
| 29 | FulfillLinePEOConfigRevisionNumber | CONFIG_REVISION_NUMBER | — | — |
| 30 | FulfillLinePEOConfigTradeComplResultCode | CONFIG_TRADE_COMPL_RESULT_CODE | — | — |
| 31 | FulfillLinePEOConfiguratorPath | CONFIGURATOR_PATH | — | — |
| 32 | FulfillLinePEOContractEndDate | CONTRACT_END_DATE | — | — |
| 33 | FulfillLinePEOContractStartDate | CONTRACT_START_DATE | — | — |
| 34 | FulfillLinePEOCreatedBy5 | CREATED_BY | — | — |
| 35 | FulfillLinePEOCreatedInRelease | CREATED_IN_RELEASE | — | — |
| 36 | FulfillLinePEOCreationDate5 | CREATION_DATE | — | — |
| 37 | FulfillLinePEOCreditChkAuthExpDate | CREDIT_CHK_AUTH_EXP_DATE | — | — |
| 38 | FulfillLinePEOCreditChkAuthNum | CREDIT_CHK_AUTH_NUM | — | — |
| 39 | FulfillLinePEOCustomerItemId | CUSTOMER_ITEM_ID | — | — |
| 40 | FulfillLinePEOCustomerPoLineNumber | CUSTOMER_PO_LINE_NUMBER | — | — |
| 41 | FulfillLinePEOCustomerPoNumber | CUSTOMER_PO_NUMBER | — | — |
| 42 | FulfillLinePEOCustomerPoScheduleNumber | CUSTOMER_PO_SCHEDULE_NUMBER | — | — |
| 43 | FulfillLinePEODefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 44 | FulfillLinePEODeltaType1 | DELTA_TYPE | — | — |
| 45 | FulfillLinePEODemandClassCode | DEMAND_CLASS_CODE | — | — |
| 46 | FulfillLinePEODestinationLocationId | DESTINATION_LOCATION_ID | — | — |
| 47 | FulfillLinePEODestinationOrgId | DESTINATION_ORG_ID | — | — |
| 48 | FulfillLinePEODocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 49 | FulfillLinePEOEarliestAcceptableShipDate | EARLIEST_ACCEPTABLE_SHIP_DATE | — | — |
| 50 | FulfillLinePEOEstimateFulfillmentCost | ESTIMATE_FULFILLMENT_COST | — | — |
| 51 | FulfillLinePEOEstimateMargin | ESTIMATE_MARGIN | — | — |
| 52 | FulfillLinePEOExemptionCertificateNumber | EXEMPTION_CERTIFICATE_NUMBER | — | — |
| 53 | FulfillLinePEOExtendedAmount1 | EXTENDED_AMOUNT | — | — |
| 54 | FulfillLinePEOFinalDischargeLocationId | FINAL_DISCHARGE_LOCATION_ID | — | — |
| 55 | FulfillLinePEOFirstPtyRegId | FIRST_PTY_REG_ID | — | — |
| 56 | FulfillLinePEOFobPointCode | FOB_POINT_CODE | — | — |
| 57 | FulfillLinePEOFreightTermsCode | FREIGHT_TERMS_CODE | — | — |
| 58 | FulfillLinePEOFulfillInstanceId | FULFILL_INSTANCE_ID | — | — |
| 59 | FulfillLinePEOFulfillLineId | FULFILL_LINE_ID | — | ✅ |
| 60 | FulfillLinePEOFulfillLineNumber | FULFILL_LINE_NUMBER | — | — |
| 61 | FulfillLinePEOFulfillLinePEOCanceledQty1 | CANCELED_QTY | — | — |
| 62 | FulfillLinePEOFulfillOrgId | FULFILL_ORG_ID | — | — |
| 63 | FulfillLinePEOFulfillToleranceAbove | FULFILL_TOLERANCE_ABOVE | — | — |
| 64 | FulfillLinePEOFulfillToleranceBelow | FULFILL_TOLERANCE_BELOW | — | — |
| 65 | FulfillLinePEOFulfilledQty1 | FULFILLED_QTY | — | — |
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
| 81 | FulfillLinePEOLastUpdateDate5 | LAST_UPDATE_DATE | — | ✅ |
| 82 | FulfillLinePEOLastUpdateLogin5 | LAST_UPDATE_LOGIN | — | — |
| 83 | FulfillLinePEOLastUpdatedBy5 | LAST_UPDATED_BY | — | — |
| 84 | FulfillLinePEOLatestAcceptableArrivalDate | LATEST_ACCEPTABLE_ARRIVAL_DATE | — | — |
| 85 | FulfillLinePEOLatestAcceptableShipDate | LATEST_ACCEPTABLE_SHIP_DATE | — | — |
| 86 | FulfillLinePEOLineId1 | LINE_ID | — | — |
| 87 | FulfillLinePEOLineTypeCode1 | LINE_TYPE_CODE | — | — |
| 88 | FulfillLinePEOObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 89 | FulfillLinePEOOnHold1 | ON_HOLD | — | — |
| 90 | FulfillLinePEOOpenFlag1 | OPEN_FLAG | — | — |
| 91 | FulfillLinePEOOrderedQty1 | ORDERED_QTY | — | ✅ |
| 92 | FulfillLinePEOOrderedUom1 | ORDERED_UOM | — | ✅ |
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
| 167 | FulfillLinePEOStatusCode1 | STATUS_CODE | — | ✅ |
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

### [[doo_headers_all|DOO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HeaderPEOAgreementHeaderId | AGREEMENT_HEADER_ID | — | — |
| 2 | HeaderPEOAgreementVersionNumber | AGREEMENT_VERSION_NUMBER | — | — |
| 3 | HeaderPEOAllowCurrencyOverrideFlag | ALLOW_CURRENCY_OVERRIDE_FLAG | — | — |
| 4 | HeaderPEOAppliedCurrencyCode | APPLIED_CURRENCY_CODE | — | — |
| 5 | HeaderPEOApprovalSequenceNumber | APPROVAL_SEQUENCE_NUMBER | — | — |
| 6 | HeaderPEOCancelReasonCode | CANCEL_REASON_CODE | — | — |
| 7 | HeaderPEOCanceledFlag | CANCELED_FLAG | — | — |
| 8 | HeaderPEOCarrierId | CARRIER_ID | — | — |
| 9 | HeaderPEOChangeVersionNumber | CHANGE_VERSION_NUMBER | — | — |
| 10 | HeaderPEOComments | COMMENTS | — | — |
| 11 | HeaderPEOConversionDate | CONVERSION_DATE | — | — |
| 12 | HeaderPEOConversionRate | CONVERSION_RATE | — | — |
| 13 | HeaderPEOConversionTypeCode | CONVERSION_TYPE_CODE | — | — |
| 14 | HeaderPEOCreatedBy | CREATED_BY | — | — |
| 15 | HeaderPEOCreatedInRelease | CREATED_IN_RELEASE | — | — |
| 16 | HeaderPEOCreationDate | CREATION_DATE | — | — |
| 17 | HeaderPEOCustomerPoNumber | CUSTOMER_PO_NUMBER | — | — |
| 18 | HeaderPEODemandClassCode | DEMAND_CLASS_CODE | — | — |
| 19 | HeaderPEOEarliestAcceptArrivalDate | EARLIEST_ACCEPT_ARRIVAL_DATE | — | — |
| 20 | HeaderPEOEarliestAcceptableShipDate | EARLIEST_ACCEPTABLE_SHIP_DATE | — | — |
| 21 | HeaderPEOFobPointCode | FOB_POINT_CODE | — | — |
| 22 | HeaderPEOFreezePriceFlag | FREEZE_PRICE_FLAG | — | — |
| 23 | HeaderPEOFreezeShippingChargeFlag | FREEZE_SHIPPING_CHARGE_FLAG | — | — |
| 24 | HeaderPEOFreezeTaxFlag | FREEZE_TAX_FLAG | — | — |
| 25 | HeaderPEOFreightTermsCode | FREIGHT_TERMS_CODE | — | — |
| 26 | HeaderPEOFulfillOrgId | FULFILL_ORG_ID | — | — |
| 27 | HeaderPEOHeaderId | HEADER_ID | — | — |
| 28 | HeaderPEOIsEditable | IS_EDITABLE | — | — |
| 29 | HeaderPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | HeaderPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 31 | HeaderPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 32 | HeaderPEOLatestAcceptArrivalDate | LATEST_ACCEPT_ARRIVAL_DATE | — | — |
| 33 | HeaderPEOLatestAcceptableShipDate | LATEST_ACCEPTABLE_SHIP_DATE | — | — |
| 34 | HeaderPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 35 | HeaderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 36 | HeaderPEOOnHold | ON_HOLD | — | — |
| 37 | HeaderPEOOpenFlag | OPEN_FLAG | — | — |
| 38 | HeaderPEOOrderNumber | ORDER_NUMBER | — | ✅ |
| 39 | HeaderPEOOrderTypeCode | ORDER_TYPE_CODE | — | — |
| 40 | HeaderPEOOrderedDate | ORDERED_DATE | — | — |
| 41 | HeaderPEOOrgId | ORG_ID | — | — |
| 42 | HeaderPEOOrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | — |
| 43 | HeaderPEOOwnerId | OWNER_ID | — | — |
| 44 | HeaderPEOPackingInstructions | PACKING_INSTRUCTIONS | — | — |
| 45 | HeaderPEOPartialShipAllowedFlag | PARTIAL_SHIP_ALLOWED_FLAG | — | — |
| 46 | HeaderPEOPaymentTermId | PAYMENT_TERM_ID | — | — |
| 47 | HeaderPEOPreCreditCheckedFlag | PRE_CREDIT_CHECKED_FLAG | — | — |
| 48 | HeaderPEOPricedOn | PRICED_ON | — | — |
| 49 | HeaderPEOPricingSegmentCode | PRICING_SEGMENT_CODE | — | — |
| 50 | HeaderPEOPricingSegmentExplanation | PRICING_SEGMENT_EXPLANATION | — | — |
| 51 | HeaderPEOPricingStrategyExplanation | PRICING_STRATEGY_EXPLANATION | — | — |
| 52 | HeaderPEOPricingStrategyId | PRICING_STRATEGY_ID | — | — |
| 53 | HeaderPEORequestArrivalDate | REQUEST_ARRIVAL_DATE | — | — |
| 54 | HeaderPEORequestCancelDate | REQUEST_CANCEL_DATE | — | — |
| 55 | HeaderPEORequestShipDate | REQUEST_SHIP_DATE | — | — |
| 56 | HeaderPEORevisionSourceOrderSystem | REVISION_SOURCE_ORDER_SYSTEM | — | — |
| 57 | HeaderPEOSalesChannelCode | SALES_CHANNEL_CODE | — | — |
| 58 | HeaderPEOSalespersonId | SALESPERSON_ID | — | — |
| 59 | HeaderPEOSegmentExplanationMsgName | SEGMENT_EXPLANATION_MSG_NAME | — | — |
| 60 | HeaderPEOShipClassOfService | SHIP_CLASS_OF_SERVICE | — | — |
| 61 | HeaderPEOShipModeOfTransport | SHIP_MODE_OF_TRANSPORT | — | — |
| 62 | HeaderPEOShipmentPriorityCode | SHIPMENT_PRIORITY_CODE | — | — |
| 63 | HeaderPEOShippingInstructions | SHIPPING_INSTRUCTIONS | — | — |
| 64 | HeaderPEOShipsetFlag | SHIPSET_FLAG | — | — |
| 65 | HeaderPEOSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 66 | HeaderPEOSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 67 | HeaderPEOSoldToPartyContactId | SOLD_TO_PARTY_CONTACT_ID | — | — |
| 68 | HeaderPEOSoldToPartyContactPointId | SOLD_TO_PARTY_CONTACT_POINT_ID | — | — |
| 69 | HeaderPEOSoldToPartyId | SOLD_TO_PARTY_ID | — | — |
| 70 | HeaderPEOSourceDocumentTypeCode | SOURCE_DOCUMENT_TYPE_CODE | — | — |
| 71 | HeaderPEOSourceOrderId | SOURCE_ORDER_ID | — | — |
| 72 | HeaderPEOSourceOrderNumber | SOURCE_ORDER_NUMBER | — | — |
| 73 | HeaderPEOSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | — |
| 74 | HeaderPEOSourceOrgId | SOURCE_ORG_ID | — | — |
| 75 | HeaderPEOSourceRevisionNumber | SOURCE_REVISION_NUMBER | — | — |
| 76 | HeaderPEOStatusCode | STATUS_CODE | — | — |
| 77 | HeaderPEOStrategyExplanationMsgName | STRATEGY_EXPLANATION_MSG_NAME | — | — |
| 78 | HeaderPEOSubmittedBy | SUBMITTED_BY | — | — |
| 79 | HeaderPEOSubmittedDate | SUBMITTED_DATE | — | — |
| 80 | HeaderPEOSubmittedFlag | SUBMITTED_FLAG | — | — |
| 81 | HeaderPEOSubstituteAllowedFlag | SUBSTITUTE_ALLOWED_FLAG | — | — |
| 82 | HeaderPEOSupplierId | SUPPLIER_ID | — | — |
| 83 | HeaderPEOSupplierSiteId | SUPPLIER_SITE_ID | — | — |
| 84 | HeaderPEOTradeComplianceResultCode | TRADE_COMPLIANCE_RESULT_CODE | — | — |
| 85 | HeaderPEOTransactionalCurrencyCode | TRANSACTIONAL_CURRENCY_CODE | — | — |

### [[doo_lines_all|DOO_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LinePEOActualShipDate | ACTUAL_SHIP_DATE | — | — |
| 2 | LinePEOCanceledFlag | CANCELED_FLAG | — | — |
| 3 | LinePEOCanceledQty | CANCELED_QTY | — | — |
| 4 | LinePEOCategoryCode | CATEGORY_CODE | — | — |
| 5 | LinePEOCompSeqPath | COMP_SEQ_PATH | — | — |
| 6 | LinePEOCreatedBy4 | CREATED_BY | — | — |
| 7 | LinePEOCreationDate4 | CREATION_DATE | — | — |
| 8 | LinePEODeltaType | DELTA_TYPE | — | — |
| 9 | LinePEODisplayLineNumber | DISPLAY_LINE_NUMBER | — | — |
| 10 | LinePEOExtendedAmount | EXTENDED_AMOUNT | — | — |
| 11 | LinePEOFulfilledQty | FULFILLED_QTY | — | — |
| 12 | LinePEOFulfillmentDate | FULFILLMENT_DATE | — | — |
| 13 | LinePEOHeaderId | HEADER_ID | — | — |
| 14 | LinePEOInventoryItemId2 | INVENTORY_ITEM_ID | — | — |
| 15 | LinePEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 16 | LinePEOItemTypeCode | ITEM_TYPE_CODE | — | — |
| 17 | LinePEOLastUpdateDate4 | LAST_UPDATE_DATE | — | ✅ |
| 18 | LinePEOLastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 19 | LinePEOLastUpdatedBy4 | LAST_UPDATED_BY | — | — |
| 20 | LinePEOLineId | LINE_ID | — | ✅ |
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

### [[rcl_inv_transfer_orders_v|RCL_INV_TRANSFER_ORDERS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InventoryTransferOrderPEOActualShipDate | ACTUAL_SHIP_DATE | — | ✅ |
| 2 | InventoryTransferOrderPEODeliveryDetailId | DELIVERY_DETAIL_ID | — | ✅ |
| 3 | InventoryTransferOrderPEOHeaderNumber | HEADER_NUMBER | — | ✅ |
| 4 | InventoryTransferOrderPEOLineId | LINE_ID | — | ✅ |
| 5 | InventoryTransferOrderPEOReceiptDate | RECEIPT_DATE | — | ✅ |
| 6 | InventoryTransferOrderPEOReceiptNum | RECEIPT_NUM | — | — |
| 7 | InventoryTransferOrderPEOShipmentHeaderId | SHIPMENT_HEADER_ID | — | — |
| 8 | InventoryTransferOrderPEOShipmentLineId | SHIPMENT_LINE_ID | — | — |
| 9 | InventoryTransferOrderPEOShipmentNum | SHIPMENT_NUM | — | — |
| 10 | InventoryTransferOrderPEOShippedQuantity | SHIPPED_QUANTITY | — | ✅ |

### [[rcl_parts_req_lines|RCL_PARTS_REQ_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartsReqLinesPEOCreatedBy | CREATED_BY | — | — |
| 2 | PartsReqLinesPEOCreationDate | CREATION_DATE | — | — |
| 3 | PartsReqLinesPEODestinationOrganizationId | DESTINATION_ORGANIZATION_ID | — | — |
| 4 | PartsReqLinesPEODestinationSubinventory | DESTINATION_SUBINVENTORY | — | ✅ |
| 5 | PartsReqLinesPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 6 | PartsReqLinesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PartsReqLinesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | PartsReqLinesPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 9 | PartsReqLinesPEONeedByDate | NEED_BY_DATE | — | ✅ |
| 10 | PartsReqLinesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | PartsReqLinesPEOParentEntityCode | PARENT_ENTITY_CODE | — | ✅ |
| 12 | PartsReqLinesPEOParentEntityId | PARENT_ENTITY_ID | — | ✅ |
| 13 | PartsReqLinesPEOQuantity | QUANTITY | — | ✅ |
| 14 | PartsReqLinesPEORequirementHeaderId | REQUIREMENT_HEADER_ID | — | — |
| 15 | PartsReqLinesPEORequirementLineId | REQUIREMENT_LINE_ID | — | ✅ |
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
| 1 | PartsReqLineDetailsPEOCreatedBy1 | CREATED_BY | — | — |
| 2 | PartsReqLineDetailsPEOCreationDate1 | CREATION_DATE | — | — |
| 3 | PartsReqLineDetailsPEOExpectedArrivalDate | EXPECTED_ARRIVAL_DATE | — | ✅ |
| 4 | PartsReqLineDetailsPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 5 | PartsReqLineDetailsPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 6 | PartsReqLineDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | PartsReqLineDetailsPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 8 | PartsReqLineDetailsPEOReqLineDetailId | REQ_LINE_DETAIL_ID | 🔑 | ✅ |
| 9 | PartsReqLineDetailsPEORequirementLineId1 | REQUIREMENT_LINE_ID | — | — |
| 10 | PartsReqLineDetailsPEOSourceCarrierId | SOURCE_CARRIER_ID | — | — |
| 11 | PartsReqLineDetailsPEOSourceId | SOURCE_ID | — | ✅ |
| 12 | PartsReqLineDetailsPEOSourceModeOfTransport | SOURCE_MODE_OF_TRANSPORT | — | — |
| 13 | PartsReqLineDetailsPEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 14 | PartsReqLineDetailsPEOSourceRequestDate | SOURCE_REQUEST_DATE | — | — |
| 15 | PartsReqLineDetailsPEOSourceServiceLevels | SOURCE_SERVICE_LEVELS | — | — |
| 16 | PartsReqLineDetailsPEOSourceSubinventory | SOURCE_SUBINVENTORY | — | ✅ |
| 17 | PartsReqLineDetailsPEOSourceType | SOURCE_TYPE | — | ✅ |

### [[svc_service_requests|SVC_SERVICE_REQUESTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ServiceRequestUnsecuredPEOAccountPartyId1 | ACCOUNT_PARTY_ID | — | — |
| 2 | ServiceRequestUnsecuredPEOAssetId | ASSET_ID | — | — |
| 3 | ServiceRequestUnsecuredPEOAssigneeResourceId1 | ASSIGNEE_RESOURCE_ID | — | — |
| 4 | ServiceRequestUnsecuredPEOBUOrgId | BU_ORG_ID | — | — |
| 5 | ServiceRequestUnsecuredPEOCatalogId | CATALOG_ID | — | — |
| 6 | ServiceRequestUnsecuredPEOCategoryId | CATEGORY_ID | — | — |
| 7 | ServiceRequestUnsecuredPEOChannelTypeCd | CHANNEL_TYPE_CD | — | — |
| 8 | ServiceRequestUnsecuredPEOClosedDate | CLOSED_DATE | — | — |
| 9 | ServiceRequestUnsecuredPEOCorpCurrencyCode1 | CORP_CURRENCY_CODE | — | — |
| 10 | ServiceRequestUnsecuredPEOCreatedBy3 | CREATED_BY | — | — |
| 11 | ServiceRequestUnsecuredPEOCreatedByPartyId | CREATED_BY_PARTY_ID | — | — |
| 12 | ServiceRequestUnsecuredPEOCreationDate3 | CREATION_DATE | — | — |
| 13 | ServiceRequestUnsecuredPEOCriticalFlag | CRITICAL_FLAG | — | — |
| 14 | ServiceRequestUnsecuredPEOCurcyConvRateType1 | CURCY_CONV_RATE_TYPE | — | — |
| 15 | ServiceRequestUnsecuredPEOCurrencyCode1 | CURRENCY_CODE | — | — |
| 16 | ServiceRequestUnsecuredPEODeletedFlag1 | DELETED_FLAG | — | — |
| 17 | ServiceRequestUnsecuredPEOIBAssetId | IB_ASSET_ID | — | — |
| 18 | ServiceRequestUnsecuredPEOInternalPriorityCd | INTERNAL_PRIORITY_CD | — | — |
| 19 | ServiceRequestUnsecuredPEOInventoryItemId1 | INVENTORY_ITEM_ID | — | — |
| 20 | ServiceRequestUnsecuredPEOInventoryOrgId | INVENTORY_ORG_ID | — | — |
| 21 | ServiceRequestUnsecuredPEOLanguageCd | LANGUAGE_CD | — | — |
| 22 | ServiceRequestUnsecuredPEOLastReopenDate | LAST_REOPEN_DATE | — | — |
| 23 | ServiceRequestUnsecuredPEOLastResolvedDate | LAST_RESOLVED_DATE | — | — |
| 24 | ServiceRequestUnsecuredPEOLastUpdateDate3 | LAST_UPDATE_DATE | — | ✅ |
| 25 | ServiceRequestUnsecuredPEOLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 26 | ServiceRequestUnsecuredPEOLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 27 | ServiceRequestUnsecuredPEOObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 28 | ServiceRequestUnsecuredPEOOpenDate | OPEN_DATE | — | — |
| 29 | ServiceRequestUnsecuredPEOOriginalSystemReference | ORIGINAL_SYSTEM_REFERENCE | — | — |
| 30 | ServiceRequestUnsecuredPEOOwnerTypeCd | OWNER_TYPE_CD | — | — |
| 31 | ServiceRequestUnsecuredPEOPartnerAccountPartyId | PARTNER_ACCOUNT_PARTY_ID | — | — |
| 32 | ServiceRequestUnsecuredPEOPrimaryContactPartyId | PRIMARY_CONTACT_PARTY_ID | — | — |
| 33 | ServiceRequestUnsecuredPEOProblemCd | PROBLEM_CD | — | — |
| 34 | ServiceRequestUnsecuredPEOProblemDesc | PROBLEM_DESC | — | — |
| 35 | ServiceRequestUnsecuredPEOProdGroupId | PROD_GROUP_ID | — | — |
| 36 | ServiceRequestUnsecuredPEOQueueId | QUEUE_ID | — | — |
| 37 | ServiceRequestUnsecuredPEOReportedByPartyId | REPORTED_BY_PARTY_ID | — | — |
| 38 | ServiceRequestUnsecuredPEOResolutionCd | RESOLUTION_CD | — | — |
| 39 | ServiceRequestUnsecuredPEOResolveDescription | RESOLVE_DESC | — | — |
| 40 | ServiceRequestUnsecuredPEOResolveOutcomeCd | RESOLVE_OUTCOME_CD | — | — |
| 41 | ServiceRequestUnsecuredPEOResolvedBy | RESOLVED_BY | — | — |
| 42 | ServiceRequestUnsecuredPEOSeverityCd | SEVERITY_CD | — | — |
| 43 | ServiceRequestUnsecuredPEOSourceCd1 | SOURCE_CD | — | — |
| 44 | ServiceRequestUnsecuredPEOSrCreatedBy | SR_CREATED_BY | — | — |
| 45 | ServiceRequestUnsecuredPEOSrId1 | SR_ID | — | — |
| 46 | ServiceRequestUnsecuredPEOSrLastUpdateDate | SR_LAST_UPDATE_DATE | — | ✅ |
| 47 | ServiceRequestUnsecuredPEOSrLastUpdateLogin | SR_LAST_UPDATE_LOGIN | — | — |
| 48 | ServiceRequestUnsecuredPEOSrLastUpdatedBy | SR_LAST_UPDATED_BY | — | — |
| 49 | ServiceRequestUnsecuredPEOSrNumber | SR_NUMBER | — | — |
| 50 | ServiceRequestUnsecuredPEOStatusCd | STATUS_CD | — | — |
| 51 | ServiceRequestUnsecuredPEOStatusTypeCd | STATUS_TYPE_CD | — | — |
| 52 | ServiceRequestUnsecuredPEOStripeCd1 | STRIPE_CD | — | — |
| 53 | ServiceRequestUnsecuredPEOTitle | TITLE | — | — |

### [[svc_work_orders|SVC_WORK_ORDERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderBIPEOAccountPartyId | ACCOUNT_PARTY_ID | — | — |
| 2 | WorkOrderBIPEOActualEndDate | ACTUAL_END_DATE | — | — |
| 3 | WorkOrderBIPEOActualStartDate | ACTUAL_START_DATE | — | — |
| 4 | WorkOrderBIPEOAddress1 | ADDRESS1 | — | — |
| 5 | WorkOrderBIPEOAddress2 | ADDRESS2 | — | — |
| 6 | WorkOrderBIPEOAddress3 | ADDRESS3 | — | — |
| 7 | WorkOrderBIPEOAddress4 | ADDRESS4 | — | — |
| 8 | WorkOrderBIPEOAssigneeResourceId | ASSIGNEE_RESOURCE_ID | — | — |
| 9 | WorkOrderBIPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 10 | WorkOrderBIPEOBookedDate | BOOKED_DATE | — | — |
| 11 | WorkOrderBIPEOCancelReason | CANCEL_REASON | — | — |
| 12 | WorkOrderBIPEOCaseNote | CASE_NOTE | — | — |
| 13 | WorkOrderBIPEOCity | CITY | — | — |
| 14 | WorkOrderBIPEOContactAltPhoneNumber | CONTACT_ALT_PHONE_NUMBER | — | — |
| 15 | WorkOrderBIPEOContactEmail | CONTACT_EMAIL | — | — |
| 16 | WorkOrderBIPEOContactLanguageCode | CONTACT_LANGUAGE_CODE | — | — |
| 17 | WorkOrderBIPEOContactName | CONTACT_NAME | — | — |
| 18 | WorkOrderBIPEOContactPartyId | CONTACT_PARTY_ID | — | — |
| 19 | WorkOrderBIPEOContactPhoneNumber | CONTACT_PHONE_NUMBER | — | — |
| 20 | WorkOrderBIPEOCorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 21 | WorkOrderBIPEOCountry | COUNTRY | — | — |
| 22 | WorkOrderBIPEOCounty | COUNTY | — | — |
| 23 | WorkOrderBIPEOCreatedBy2 | CREATED_BY | — | — |
| 24 | WorkOrderBIPEOCreationDate2 | CREATION_DATE | — | — |
| 25 | WorkOrderBIPEOCurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 26 | WorkOrderBIPEOCurrencyCode | CURRENCY_CODE | — | — |
| 27 | WorkOrderBIPEODeletedFlag | DELETED_FLAG | — | — |
| 28 | WorkOrderBIPEODeliveryWinEndDate | DELIVERY_WIN_END_DATE | — | — |
| 29 | WorkOrderBIPEODeliveryWinStartDate | DELIVERY_WIN_START_DATE | — | — |
| 30 | WorkOrderBIPEODuration | DURATION | — | — |
| 31 | WorkOrderBIPEOEstimatedStartDate | ESTIMATED_START_DATE | — | — |
| 32 | WorkOrderBIPEOFsActivityId | FS_ACTIVITY_ID | — | — |
| 33 | WorkOrderBIPEOFsContactFlag | FS_CONTACT_FLAG | — | — |
| 34 | WorkOrderBIPEOFsErrorDetail | FS_ERROR_DETAIL | — | — |
| 35 | WorkOrderBIPEOFsNote | FS_NOTE | — | — |
| 36 | WorkOrderBIPEOFsResource | FS_RESOURCE | — | — |
| 37 | WorkOrderBIPEOLastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 38 | WorkOrderBIPEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 39 | WorkOrderBIPEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 40 | WorkOrderBIPEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 41 | WorkOrderBIPEOOpportunityId | OPPORTUNITY_ID | — | — |
| 42 | WorkOrderBIPEOOverridePartyId | OVERRIDE_PARTY_ID | — | — |
| 43 | WorkOrderBIPEOOverrideReason | OVERRIDE_REASON | — | — |
| 44 | WorkOrderBIPEOOverrideStatusCd | OVERRIDE_STATUS_CD | — | — |
| 45 | WorkOrderBIPEOPostalCode | POSTAL_CODE | — | — |
| 46 | WorkOrderBIPEOPrimaryAssetId | PRIMARY_ASSET_ID | — | — |
| 47 | WorkOrderBIPEOProvince | PROVINCE | — | — |
| 48 | WorkOrderBIPEOReminderTime | REMINDER_TIME | — | — |
| 49 | WorkOrderBIPEORequestedByPartyId | REQUESTED_BY_PARTY_ID | — | — |
| 50 | WorkOrderBIPEORequestedDate | REQUESTED_DATE | — | — |
| 51 | WorkOrderBIPEORequestedTimeSlot | REQUESTED_TIME_SLOT | — | — |
| 52 | WorkOrderBIPEORescheduleReason | RESCHEDULE_REASON | — | — |
| 53 | WorkOrderBIPEOResolutionDueDate | RESOLUTION_DUE_DATE | — | — |
| 54 | WorkOrderBIPEOScheduledDate | SCHEDULED_DATE | — | — |
| 55 | WorkOrderBIPEOScheduledTimeSlot | SCHEDULED_TIME_SLOT | — | — |
| 56 | WorkOrderBIPEOSourceCd | SOURCE_CD | — | — |
| 57 | WorkOrderBIPEOSrId | SR_ID | — | — |
| 58 | WorkOrderBIPEOState | STATE | — | — |
| 59 | WorkOrderBIPEOStripeCd | STRIPE_CD | — | — |
| 60 | WorkOrderBIPEOTimezoneCode | TIMEZONE_CODE | — | — |
| 61 | WorkOrderBIPEOTravelTime | TRAVEL_TIME | — | — |
| 62 | WorkOrderBIPEOWoArea | WO_AREA | — | — |
| 63 | WorkOrderBIPEOWoId | WO_ID | — | — |
| 64 | WorkOrderBIPEOWoIntegrationMsgCd | WO_INTEGRATION_MSG_CD | — | — |
| 65 | WorkOrderBIPEOWoIntegrationStatusCd | WO_INTEGRATION_STATUS_CD | — | — |
| 66 | WorkOrderBIPEOWoNumber | WO_NUMBER | — | — |
| 67 | WorkOrderBIPEOWoStatusCd | WO_STATUS_CD | — | — |
| 68 | WorkOrderBIPEOWoTypeId | WO_TYPE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
