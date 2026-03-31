---
id: DOC-OTHER-PVO-FulfillLineExtractPVO
doc_type: system-doc
title: "FulfillLineExtractPVO — PVO Cross-Module"
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
  - FulfillLineExtractPVO
  - fulfilllineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FulfillLineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fulfill Line Extract. Acessa as tabelas: DOO_FULFILL_LINES_ALL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.FulfillLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 229 | 1 | 1 | 228 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_fulfill_lines_all|DOO_FULFILL_LINES_ALL]] — 229 atributos (1 PKs, 228 BICC)

---

## ⚙️ Atributos

### [[doo_fulfill_lines_all|DOO_FULFILL_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FulfillLineAccountingRuleId | ACCOUNTING_RULE_ID | — | ✅ |
| 2 | FulfillLineActionTypeCode | ACTION_TYPE_CODE | — | ✅ |
| 3 | FulfillLineActualCompletionDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 4 | FulfillLineActualShipDate | ACTUAL_SHIP_DATE | — | ✅ |
| 5 | FulfillLineAgreementHeaderId | AGREEMENT_HEADER_ID | — | ✅ |
| 6 | FulfillLineAgreementLineId | AGREEMENT_LINE_ID | — | ✅ |
| 7 | FulfillLineAgreementVersionNumber | AGREEMENT_VERSION_NUMBER | — | ✅ |
| 8 | FulfillLineAppliedPriceListId | APPLIED_PRICE_LIST_ID | — | ✅ |
| 9 | FulfillLineAssessableValue | ASSESSABLE_VALUE | — | ✅ |
| 10 | FulfillLineAssetGroupNumber | ASSET_GROUP_NUMBER | — | ✅ |
| 11 | FulfillLineAssetTrackedFlag | ASSET_TRACKED_FLAG | — | ✅ |
| 12 | FulfillLineBatchId | BATCH_ID | — | ✅ |
| 13 | FulfillLineBillToContactId | BILL_TO_CONTACT_ID | — | ✅ |
| 14 | FulfillLineBillToContactPointId | BILL_TO_CONTACT_POINT_ID | — | ✅ |
| 15 | FulfillLineBillToCustomerId | BILL_TO_CUSTOMER_ID | — | ✅ |
| 16 | FulfillLineBillToSiteUseId | BILL_TO_SITE_USE_ID | — | ✅ |
| 17 | FulfillLineBillingTrxTypeId | BILLING_TRX_TYPE_ID | — | ✅ |
| 18 | FulfillLineBuyerId | BUYER_ID | — | ✅ |
| 19 | FulfillLineCancelBackordersFlag | CANCEL_BACKORDERS_FLAG | — | ✅ |
| 20 | FulfillLineCancelReasonCode | CANCEL_REASON_CODE | — | ✅ |
| 21 | FulfillLineCanceledFlag | CANCELED_FLAG | — | ✅ |
| 22 | FulfillLineCanceledQty | CANCELED_QTY | — | ✅ |
| 23 | FulfillLineCarrierId | CARRIER_ID | — | ✅ |
| 24 | FulfillLineCategoryCode | CATEGORY_CODE | — | ✅ |
| 25 | FulfillLineChangeEligibleFlag | CHANGE_ELIGIBLE_FLAG | — | ✅ |
| 26 | FulfillLineComments | COMMENTS | — | ✅ |
| 27 | FulfillLineCompSeqPath | COMP_SEQ_PATH | — | ✅ |
| 28 | FulfillLineComponentIdPath | COMPONENT_ID_PATH | — | ✅ |
| 29 | FulfillLineConfigCreationDate | CONFIG_CREATION_DATE | — | ✅ |
| 30 | FulfillLineConfigHeaderId | CONFIG_HEADER_ID | — | ✅ |
| 31 | FulfillLineConfigInventoryItemId | CONFIG_INVENTORY_ITEM_ID | — | ✅ |
| 32 | FulfillLineConfigItemReference | CONFIG_ITEM_REFERENCE | — | ✅ |
| 33 | FulfillLineConfigItemVersion | CONFIG_ITEM_VERSION | — | ✅ |
| 34 | FulfillLineConfigRevisionNumber | CONFIG_REVISION_NUMBER | — | ✅ |
| 35 | FulfillLineConfigTradeComplResultCode | CONFIG_TRADE_COMPL_RESULT_CODE | — | ✅ |
| 36 | FulfillLineConfiguratorPath | CONFIGURATOR_PATH | — | ✅ |
| 37 | FulfillLineContractEndDate | CONTRACT_END_DATE | — | ✅ |
| 38 | FulfillLineContractStartDate | CONTRACT_START_DATE | — | ✅ |
| 39 | FulfillLineCreatedBy | CREATED_BY | — | ✅ |
| 40 | FulfillLineCreatedInRelease | CREATED_IN_RELEASE | — | ✅ |
| 41 | FulfillLineCreationDate | CREATION_DATE | — | ✅ |
| 42 | FulfillLineCreationMode | CREATION_MODE | — | ✅ |
| 43 | FulfillLineCreditChkAuthExpDate | CREDIT_CHK_AUTH_EXP_DATE | — | ✅ |
| 44 | FulfillLineCreditChkAuthNum | CREDIT_CHK_AUTH_NUM | — | ✅ |
| 45 | FulfillLineCustomerItemId | CUSTOMER_ITEM_ID | — | ✅ |
| 46 | FulfillLineCustomerPoLineNumber | CUSTOMER_PO_LINE_NUMBER | — | ✅ |
| 47 | FulfillLineCustomerPoNumber | CUSTOMER_PO_NUMBER | — | ✅ |
| 48 | FulfillLineCustomerPoScheduleNumber | CUSTOMER_PO_SCHEDULE_NUMBER | — | ✅ |
| 49 | FulfillLineDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | ✅ |
| 50 | FulfillLineDeltaType | DELTA_TYPE | — | ✅ |
| 51 | FulfillLineDemandClassCode | DEMAND_CLASS_CODE | — | ✅ |
| 52 | FulfillLineDemandSourceLineReference | DEMAND_SOURCE_LINE_REFERENCE | — | ✅ |
| 53 | FulfillLineDemandSourceScheduledFlag | DEMAND_SOURCE_SCHEDULED_FLAG | — | ✅ |
| 54 | FulfillLineDestinationLocationId | DESTINATION_LOCATION_ID | — | ✅ |
| 55 | FulfillLineDestinationOrgId | DESTINATION_ORG_ID | — | ✅ |
| 56 | FulfillLineDocumentSubType | DOCUMENT_SUB_TYPE | — | ✅ |
| 57 | FulfillLineEarliestAcceptableShipDate | EARLIEST_ACCEPTABLE_SHIP_DATE | — | ✅ |
| 58 | FulfillLineEndCreditMethodCode | END_CREDIT_METHOD_CODE | — | ✅ |
| 59 | FulfillLineEndDate | END_DATE | — | ✅ |
| 60 | FulfillLineEndReasonCode | END_REASON_CODE | — | ✅ |
| 61 | FulfillLineEnforceSingleShipmentFlag | ENFORCE_SINGLE_SHIPMENT_FLAG | — | ✅ |
| 62 | FulfillLineEstimateFulfillmentCost | ESTIMATE_FULFILLMENT_COST | — | ✅ |
| 63 | FulfillLineEstimateMargin | ESTIMATE_MARGIN | — | ✅ |
| 64 | FulfillLineExemptionCertificateNumber | EXEMPTION_CERTIFICATE_NUMBER | — | ✅ |
| 65 | FulfillLineExtendedAmount | EXTENDED_AMOUNT | — | ✅ |
| 66 | FulfillLineExternalPriceBookName | EXTERNAL_PRICE_BOOK_NAME | — | ✅ |
| 67 | FulfillLineFinalDischargeLocationId | FINAL_DISCHARGE_LOCATION_ID | — | ✅ |
| 68 | FulfillLineFirstPtyRegId | FIRST_PTY_REG_ID | — | ✅ |
| 69 | FulfillLineFobPointCode | FOB_POINT_CODE | — | ✅ |
| 70 | FulfillLineFreightTermsCode | FREIGHT_TERMS_CODE | — | ✅ |
| 71 | FulfillLineFulfillInstanceId | FULFILL_INSTANCE_ID | — | ✅ |
| 72 | FulfillLineFulfillLineNumber | FULFILL_LINE_NUMBER | — | ✅ |
| 73 | FulfillLineFulfillOrgId | FULFILL_ORG_ID | — | ✅ |
| 74 | FulfillLineFulfillToleranceAbove | FULFILL_TOLERANCE_ABOVE | — | ✅ |
| 75 | FulfillLineFulfillToleranceBelow | FULFILL_TOLERANCE_BELOW | — | ✅ |
| 76 | FulfillLineFulfilledQty | FULFILLED_QTY | — | ✅ |
| 77 | FulfillLineFulfillmentDate | FULFILLMENT_DATE | — | ✅ |
| 78 | FulfillLineFulfillmentGroupId | FULFILLMENT_GROUP_ID | — | ✅ |
| 79 | FulfillLineFulfillmentMode | FULFILLMENT_MODE | — | ✅ |
| 80 | FulfillLineFulfillmentSplitRefId | FULFILLMENT_SPLIT_REF_ID | — | ✅ |
| 81 | FulfillLineGopReferenceId | GOP_REFERENCE_ID | — | ✅ |
| 82 | FulfillLineGopRequestRegion | GOP_REQUEST_REGION | — | ✅ |
| 83 | FulfillLineHeaderId | HEADER_ID | — | ✅ |
| 84 | FulfillLineId | FULFILL_LINE_ID | 🔑 | ✅ |
| 85 | FulfillLineIntendedUseClassifId | INTENDED_USE_CLASSIF_ID | — | ✅ |
| 86 | FulfillLineInternalComments | INTERNAL_COMMENTS | — | ✅ |
| 87 | FulfillLineInventoryInterfacedFlag | INVENTORY_INTERFACED_FLAG | — | ✅ |
| 88 | FulfillLineInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 89 | FulfillLineInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | ✅ |
| 90 | FulfillLineInventoryTransactionFlag | INVENTORY_TRANSACTION_FLAG | — | ✅ |
| 91 | FulfillLineInvoiceEnabledFlag | INVOICE_ENABLED_FLAG | — | ✅ |
| 92 | FulfillLineInvoiceInterfacedFlag | INVOICE_INTERFACED_FLAG | — | ✅ |
| 93 | FulfillLineInvoiceableItemFlag | INVOICEABLE_ITEM_FLAG | — | ✅ |
| 94 | FulfillLineInvoicingRuleId | INVOICING_RULE_ID | — | ✅ |
| 95 | FulfillLineItemSubTypeCode | ITEM_SUB_TYPE_CODE | — | ✅ |
| 96 | FulfillLineItemTypeCode | ITEM_TYPE_CODE | — | ✅ |
| 97 | FulfillLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 98 | FulfillLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 99 | FulfillLineLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 100 | FulfillLineLatestAcceptableArrivalDate | LATEST_ACCEPTABLE_ARRIVAL_DATE | — | ✅ |
| 101 | FulfillLineLatestAcceptableShipDate | LATEST_ACCEPTABLE_SHIP_DATE | — | ✅ |
| 102 | FulfillLineLatestExtFulfillLineNumber | LATEST_EXT_FULFILL_LINE_NUMBER | — | ✅ |
| 103 | FulfillLineLineId | LINE_ID | — | ✅ |
| 104 | FulfillLineLineTypeCode | LINE_TYPE_CODE | — | ✅ |
| 105 | FulfillLineMdoFlag | MDO_FLAG | — | ✅ |
| 106 | FulfillLineModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 107 | FulfillLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 108 | FulfillLineOnHold | ON_HOLD | — | ✅ |
| 109 | FulfillLineOneTimeConfigFlag | ONE_TIME_CONFIG_FLAG | — | ✅ |
| 110 | FulfillLineOpenFlag | OPEN_FLAG | — | ✅ |
| 111 | FulfillLineOrderedQty | ORDERED_QTY | — | ✅ |
| 112 | FulfillLineOrderedUom | ORDERED_UOM | — | ✅ |
| 113 | FulfillLineOrgId | ORG_ID | — | ✅ |
| 114 | FulfillLineOrigSysDocumentLineRef | ORIG_SYS_DOCUMENT_LINE_REF | — | ✅ |
| 115 | FulfillLineOrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | ✅ |
| 116 | FulfillLineOriginalInventoryItemId | ORIGINAL_INVENTORY_ITEM_ID | — | ✅ |
| 117 | FulfillLineOverrideScheduleDateFlag | OVERRIDE_SCHEDULE_DATE_FLAG | — | ✅ |
| 118 | FulfillLineOwnerId | OWNER_ID | — | ✅ |
| 119 | FulfillLinePackingInstructions | PACKING_INSTRUCTIONS | — | ✅ |
| 120 | FulfillLineParentFulfillLineId | PARENT_FULFILL_LINE_ID | — | ✅ |
| 121 | FulfillLinePartialShipAllowedFlag | PARTIAL_SHIP_ALLOWED_FLAG | — | ✅ |
| 122 | FulfillLinePaymentTermId | PAYMENT_TERM_ID | — | ✅ |
| 123 | FulfillLinePoStatusCode | PO_STATUS_CODE | — | ✅ |
| 124 | FulfillLinePrefOverriddenBitset | PREF_OVERRIDDEN_BITSET | — | ✅ |
| 125 | FulfillLinePriceUsingSecUomFlag | PRICE_USING_SEC_UOM_FLAG | — | ✅ |
| 126 | FulfillLinePricedOn | PRICED_ON | — | ✅ |
| 127 | FulfillLinePrjRecIndicator | PRJ_REC_INDICATOR | — | ✅ |
| 128 | FulfillLineProcessId | PROCESS_ID | — | ✅ |
| 129 | FulfillLineProcessInstanceId | PROCESS_INSTANCE_ID | — | ✅ |
| 130 | FulfillLineProcessNumber | PROCESS_NUMBER | — | ✅ |
| 131 | FulfillLineProcessSet | PROCESS_SET | — | ✅ |
| 132 | FulfillLineProdFcCategId | PROD_FC_CATEG_ID | — | ✅ |
| 133 | FulfillLineProductCategory | PRODUCT_CATEGORY | — | ✅ |
| 134 | FulfillLineProductType | PRODUCT_TYPE | — | ✅ |
| 135 | FulfillLinePromiseArrivalDate | PROMISE_ARRIVAL_DATE | — | ✅ |
| 136 | FulfillLinePromiseShipDate | PROMISE_SHIP_DATE | — | ✅ |
| 137 | FulfillLinePromotionItemFlag | PROMOTION_ITEM_FLAG | — | — |
| 138 | FulfillLinePurchasingEnabledFlag | PURCHASING_ENABLED_FLAG | — | ✅ |
| 139 | FulfillLinePurchasingUom | PURCHASING_UOM | — | ✅ |
| 140 | FulfillLineQuantityPerModel | QUANTITY_PER_MODEL | — | ✅ |
| 141 | FulfillLineRatePlanDocumentId | RATE_PLAN_DOCUMENT_ID | — | ✅ |
| 142 | FulfillLineRatePlanId | RATE_PLAN_ID | — | ✅ |
| 143 | FulfillLineReceivablesOrgId | RECEIVABLES_ORG_ID | — | ✅ |
| 144 | FulfillLineReferenceFlineId | REFERENCE_FLINE_ID | — | ✅ |
| 145 | FulfillLineRemnantFlag | REMNANT_FLAG | — | ✅ |
| 146 | FulfillLineRequestArrivalDate | REQUEST_ARRIVAL_DATE | — | ✅ |
| 147 | FulfillLineRequestCancelDate | REQUEST_CANCEL_DATE | — | ✅ |
| 148 | FulfillLineRequestShipDate | REQUEST_SHIP_DATE | — | ✅ |
| 149 | FulfillLineRequestType | REQUEST_TYPE | — | ✅ |
| 150 | FulfillLineRequestedRatePlanId | REQUESTED_RATE_PLAN_ID | — | ✅ |
| 151 | FulfillLineRequiredFulfillmentDate | REQUIRED_FULFILLMENT_DATE | — | ✅ |
| 152 | FulfillLineRequisitionBuId | REQUISITION_BU_ID | — | ✅ |
| 153 | FulfillLineRequisitionInventoryOrgId | REQUISITION_INVENTORY_ORG_ID | — | ✅ |
| 154 | FulfillLineReservableFlag | RESERVABLE_FLAG | — | ✅ |
| 155 | FulfillLineReservationId | RESERVATION_ID | — | ✅ |
| 156 | FulfillLineReservedQty | RESERVED_QTY | — | ✅ |
| 157 | FulfillLineReturnReasonCode | RETURN_REASON_CODE | — | ✅ |
| 158 | FulfillLineReturnableFlag | RETURNABLE_FLAG | — | ✅ |
| 159 | FulfillLineRmaDeliveredQty | RMA_DELIVERED_QTY | — | ✅ |
| 160 | FulfillLineRootParentFulfillLineId | ROOT_PARENT_FULFILL_LINE_ID | — | ✅ |
| 161 | FulfillLineSalesProductTypeCode | SALES_PRODUCT_TYPE_CODE | — | ✅ |
| 162 | FulfillLineSalespersonId | SALESPERSON_ID | — | ✅ |
| 163 | FulfillLineScheduleArrivalDate | SCHEDULE_ARRIVAL_DATE | — | ✅ |
| 164 | FulfillLineScheduleShipDate | SCHEDULE_SHIP_DATE | — | ✅ |
| 165 | FulfillLineSchedulingReasonCode | SCHEDULING_REASON_CODE | — | ✅ |
| 166 | FulfillLineSecondaryFulfilledQty | SECONDARY_FULFILLED_QTY | — | ✅ |
| 167 | FulfillLineSecondaryOrderedQty | SECONDARY_ORDERED_QTY | — | ✅ |
| 168 | FulfillLineSecondaryRmaDeliveredQty | SECONDARY_RMA_DELIVERED_QTY | — | ✅ |
| 169 | FulfillLineSecondaryShippedQty | SECONDARY_SHIPPED_QTY | — | ✅ |
| 170 | FulfillLineSecondaryUom | SECONDARY_UOM | — | ✅ |
| 171 | FulfillLineSellingProfitCenterBUId | SELLING_PROFIT_CENTER_BU_ID | — | ✅ |
| 172 | FulfillLineServiceCancelDate | SERVICE_CANCEL_DATE | — | ✅ |
| 173 | FulfillLineServiceDuration | SERVICE_DURATION | — | ✅ |
| 174 | FulfillLineServiceDurationPeriodCode | SERVICE_DURATION_PERIOD_CODE | — | ✅ |
| 175 | FulfillLineShipClassOfService | SHIP_CLASS_OF_SERVICE | — | ✅ |
| 176 | FulfillLineShipModeOfTransport | SHIP_MODE_OF_TRANSPORT | — | ✅ |
| 177 | FulfillLineShipSetName | SHIP_SET_NAME | — | ✅ |
| 178 | FulfillLineShipToContactId | SHIP_TO_CONTACT_ID | — | ✅ |
| 179 | FulfillLineShipToContactPointId | SHIP_TO_CONTACT_POINT_ID | — | ✅ |
| 180 | FulfillLineShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | ✅ |
| 181 | FulfillLineShipToPartyContactId | SHIP_TO_PARTY_CONTACT_ID | — | ✅ |
| 182 | FulfillLineShipToPartyId | SHIP_TO_PARTY_ID | — | ✅ |
| 183 | FulfillLineShipToPartySiteId | SHIP_TO_PARTY_SITE_ID | — | ✅ |
| 184 | FulfillLineShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | ✅ |
| 185 | FulfillLineShipmentPriorityCode | SHIPMENT_PRIORITY_CODE | — | ✅ |
| 186 | FulfillLineShippableFlag | SHIPPABLE_FLAG | — | ✅ |
| 187 | FulfillLineShippedQty | SHIPPED_QTY | — | ✅ |
| 188 | FulfillLineShippedUom | SHIPPED_UOM | — | ✅ |
| 189 | FulfillLineShippingInstructions | SHIPPING_INSTRUCTIONS | — | ✅ |
| 190 | FulfillLineShowInSales | SHOW_IN_SALES | — | ✅ |
| 191 | FulfillLineSourceLineId | SOURCE_LINE_ID | — | ✅ |
| 192 | FulfillLineSourceLineNumber | SOURCE_LINE_NUMBER | — | ✅ |
| 193 | FulfillLineSourceOrderId | SOURCE_ORDER_ID | — | ✅ |
| 194 | FulfillLineSourceOrderNumber | SOURCE_ORDER_NUMBER | — | ✅ |
| 195 | FulfillLineSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | ✅ |
| 196 | FulfillLineSourceOrgId | SOURCE_ORG_ID | — | ✅ |
| 197 | FulfillLineSourceRevisionNumber | SOURCE_REVISION_NUMBER | — | ✅ |
| 198 | FulfillLineSourceScheduleId | SOURCE_SCHEDULE_ID | — | ✅ |
| 199 | FulfillLineSourceScheduleNumber | SOURCE_SCHEDULE_NUMBER | — | ✅ |
| 200 | FulfillLineSplitFromFlineId | SPLIT_FROM_FLINE_ID | — | ✅ |
| 201 | FulfillLineStatusCode | STATUS_CODE | — | ✅ |
| 202 | FulfillLineStatusRulesetId | STATUS_RULESET_ID | — | ✅ |
| 203 | FulfillLineSubinventory | SUBINVENTORY | — | ✅ |
| 204 | FulfillLineSubscriptionInterfacedFlag | SUBSCRIPTION_INTERFACED_FLAG | — | ✅ |
| 205 | FulfillLineSubscriptionProfileId | SUBSCRIPTION_PROFILE_ID | — | ✅ |
| 206 | FulfillLineSubstituteAllowedFlag | SUBSTITUTE_ALLOWED_FLAG | — | ✅ |
| 207 | FulfillLineSubstituteReasonCode | SUBSTITUTE_REASON_CODE | — | ✅ |
| 208 | FulfillLineSupplierId | SUPPLIER_ID | — | ✅ |
| 209 | FulfillLineSupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 210 | FulfillLineSupplyStatusCode | SUPPLY_STATUS_CODE | — | ✅ |
| 211 | FulfillLineTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | ✅ |
| 212 | FulfillLineTaxExemptFlag | TAX_EXEMPT_FLAG | — | ✅ |
| 213 | FulfillLineTaxExemptionReasonCode | TAX_EXEMPTION_REASON_CODE | — | ✅ |
| 214 | FulfillLineTaxInvoiceDate | TAX_INVOICE_DATE | — | ✅ |
| 215 | FulfillLineTaxInvoiceNumber | TAX_INVOICE_NUMBER | — | ✅ |
| 216 | FulfillLineThirdPtyRegId | THIRD_PTY_REG_ID | — | ✅ |
| 217 | FulfillLineTotalContractAmount | TOTAL_CONTRACT_AMOUNT | — | ✅ |
| 218 | FulfillLineTotalContractQuantity | TOTAL_CONTRACT_QUANTITY | — | ✅ |
| 219 | FulfillLineTradeComplianceDate | TRADE_COMPLIANCE_DATE | — | ✅ |
| 220 | FulfillLineTradeComplianceResultCode | TRADE_COMPLIANCE_RESULT_CODE | — | ✅ |
| 221 | FulfillLineTransportationPlannedFlag | TRANSPORTATION_PLANNED_FLAG | — | ✅ |
| 222 | FulfillLineTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 223 | FulfillLineUnitListPrice | UNIT_LIST_PRICE | — | ✅ |
| 224 | FulfillLineUnitQuantity | UNIT_QUANTITY | — | ✅ |
| 225 | FulfillLineUnitSellingPrice | UNIT_SELLING_PRICE | — | ✅ |
| 226 | FulfillLineUnreferencedReturnFlag | UNREFERENCED_RETURN_FLAG | — | ✅ |
| 227 | FulfillLineUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | ✅ |
| 228 | FulfillLineUserUpdateIndicatorBitset | USER_UPDATE_INDICATOR_BITSET | — | ✅ |
| 229 | FulfillLineValidConfigurationFlag | VALID_CONFIGURATION_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
