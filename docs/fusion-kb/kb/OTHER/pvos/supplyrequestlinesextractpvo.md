---
id: DOC-OTHER-PVO-SupplyRequestLinesExtractPVO
doc_type: system-doc
title: "SupplyRequestLinesExtractPVO — PVO Cross-Module"
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
  - SupplyRequestLinesExtractPVO
  - supplyrequestlinesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplyRequestLinesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Supply Request Lines Extract. Acessa as tabelas: DOS_SUPPLY_LINES_INT.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DosBiccExtractAM.SupplyRequestLinesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 208 | 1 | 1 | 208 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[dos_supply_lines_int|DOS_SUPPLY_LINES_INT]] — 208 atributos (1 PKs, 208 BICC)

---

## ⚙️ Atributos

### [[dos_supply_lines_int|DOS_SUPPLY_LINES_INT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DosSupplyLinesIntPEOAccountingClassCode | ACCOUNTING_CLASS_CODE | — | ✅ |
| 2 | DosSupplyLinesIntPEOAgreementId | AGREEMENT_ID | — | ✅ |
| 3 | DosSupplyLinesIntPEOAllowExplosionFlag | ALLOW_EXPLOSION_FLAG | — | ✅ |
| 4 | DosSupplyLinesIntPEOAltBomDesignator | ALT_BOM_DESIGNATOR | — | ✅ |
| 5 | DosSupplyLinesIntPEOAltRoutingDesignator | ALT_ROUTING_DESIGNATOR | — | ✅ |
| 6 | DosSupplyLinesIntPEOAuthorizationStatus | AUTHORIZATION_STATUS | — | ✅ |
| 7 | DosSupplyLinesIntPEOAutosourceFlag | AUTOSOURCE_FLAG | — | ✅ |
| 8 | DosSupplyLinesIntPEOBackToBackFlag | BACK_TO_BACK_FLAG | — | ✅ |
| 9 | DosSupplyLinesIntPEOBatchId | BATCH_ID | — | ✅ |
| 10 | DosSupplyLinesIntPEOBomRevisionDate | BOM_REVISION_DATE | — | ✅ |
| 11 | DosSupplyLinesIntPEOBudgetControlEnabledFlag | BUDGET_CONTROL_ENABLED_FLAG | — | ✅ |
| 12 | DosSupplyLinesIntPEOBudgetDate | BUDGET_DATE | — | ✅ |
| 13 | DosSupplyLinesIntPEOBuildSequence | BUILD_SEQUENCE | — | ✅ |
| 14 | DosSupplyLinesIntPEOBuyerId | BUYER_ID | — | ✅ |
| 15 | DosSupplyLinesIntPEOCancelComments | CANCEL_COMMENTS | — | ✅ |
| 16 | DosSupplyLinesIntPEOCancelReasonCode | CANCEL_REASON_CODE | — | ✅ |
| 17 | DosSupplyLinesIntPEOCarrierId | CARRIER_ID | — | ✅ |
| 18 | DosSupplyLinesIntPEOCategoryId | CATEGORY_ID | — | ✅ |
| 19 | DosSupplyLinesIntPEOChargeAcctId | CHARGE_ACCT_ID | — | ✅ |
| 20 | DosSupplyLinesIntPEOComments | COMMENTS | — | ✅ |
| 21 | DosSupplyLinesIntPEOCreatedBy | CREATED_BY | — | ✅ |
| 22 | DosSupplyLinesIntPEOCreationDate | CREATION_DATE | — | ✅ |
| 23 | DosSupplyLinesIntPEOCustomerContactId | CUSTOMER_CONTACT_ID | — | ✅ |
| 24 | DosSupplyLinesIntPEOCustomerId | CUSTOMER_ID | — | ✅ |
| 25 | DosSupplyLinesIntPEOCustomerOrderLineNumber | CUSTOMER_ORDER_LINE_NUMBER | — | ✅ |
| 26 | DosSupplyLinesIntPEOCustomerOrderNumber | CUSTOMER_ORDER_NUMBER | — | ✅ |
| 27 | DosSupplyLinesIntPEOCustomerOrderScheduleNumber | CUSTOMER_ORDER_SCHEDULE_NUMBER | — | ✅ |
| 28 | DosSupplyLinesIntPEOCustomerOrderSourceSystem | CUSTOMER_ORDER_SOURCE_SYSTEM | — | ✅ |
| 29 | DosSupplyLinesIntPEOCustomerShipToId | CUSTOMER_SHIP_TO_ID | — | ✅ |
| 30 | DosSupplyLinesIntPEODeliverToLocationId | DELIVER_TO_LOCATION_ID | — | ✅ |
| 31 | DosSupplyLinesIntPEODeliverToRequestorId | DELIVER_TO_REQUESTOR_ID | — | ✅ |
| 32 | DosSupplyLinesIntPEODeliverToSubinventory | DELIVER_TO_SUBINVENTORY | — | ✅ |
| 33 | DosSupplyLinesIntPEODeliveryLeadTime | DELIVERY_LEAD_TIME | — | ✅ |
| 34 | DosSupplyLinesIntPEODemandClass | DEMAND_CLASS | — | ✅ |
| 35 | DosSupplyLinesIntPEODestinationBuId | DESTINATION_BU_ID | — | ✅ |
| 36 | DosSupplyLinesIntPEODestinationLocationId | DESTINATION_LOCATION_ID | — | ✅ |
| 37 | DosSupplyLinesIntPEODestinationOrganizationCode | DESTINATION_ORGANIZATION_CODE | — | ✅ |
| 38 | DosSupplyLinesIntPEODestinationOrganizationId | DESTINATION_ORGANIZATION_ID | — | ✅ |
| 39 | DosSupplyLinesIntPEODestinationSubinventoryCode | DESTINATION_SUBINVENTORY_CODE | — | ✅ |
| 40 | DosSupplyLinesIntPEODestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 41 | DosSupplyLinesIntPEODistributionId | DISTRIBUTION_ID | — | ✅ |
| 42 | DosSupplyLinesIntPEODooShipmentFlag | DOO_SHIPMENT_FLAG | — | ✅ |
| 43 | DosSupplyLinesIntPEOEarliestShipDate | EARLIEST_SHIP_DATE | — | ✅ |
| 44 | DosSupplyLinesIntPEOEndInventoryItemId | END_INVENTORY_ITEM_ID | — | ✅ |
| 45 | DosSupplyLinesIntPEOEndItemName | END_ITEM_NAME | — | ✅ |
| 46 | DosSupplyLinesIntPEOExecSystemDeliverToSubinv | EXEC_SYSTEM_DELIVER_TO_SUBINV | — | ✅ |
| 47 | DosSupplyLinesIntPEOExecSystemDelvrToLocName | EXEC_SYSTEM_DELVR_TO_LOC_NAME | — | ✅ |
| 48 | DosSupplyLinesIntPEOExecSystemDelvrToRequestor | EXEC_SYSTEM_DELVR_TO_REQUESTOR | — | ✅ |
| 49 | DosSupplyLinesIntPEOExecSystemItemNumber | EXEC_SYSTEM_ITEM_NUMBER | — | ✅ |
| 50 | DosSupplyLinesIntPEOExecSystemProjectId | EXEC_SYSTEM_PROJECT_ID | — | ✅ |
| 51 | DosSupplyLinesIntPEOExecSystemProjectName | EXEC_SYSTEM_PROJECT_NAME | — | ✅ |
| 52 | DosSupplyLinesIntPEOExecSystemSourceLoctrCode | EXEC_SYSTEM_SOURCE_LOCTR_CODE | — | ✅ |
| 53 | DosSupplyLinesIntPEOExecSystemSourceOrgCode | EXEC_SYSTEM_SOURCE_ORG_CODE | — | ✅ |
| 54 | DosSupplyLinesIntPEOExecSystemSuggestedVendor | EXEC_SYSTEM_SUGGESTED_VENDOR | — | ✅ |
| 55 | DosSupplyLinesIntPEOExecSystemSugstdVendorSite | EXEC_SYSTEM_SUGSTD_VENDOR_SITE | — | ✅ |
| 56 | DosSupplyLinesIntPEOExecSystemTaskId | EXEC_SYSTEM_TASK_ID | — | ✅ |
| 57 | DosSupplyLinesIntPEOExecSystemTaskName | EXEC_SYSTEM_TASK_NAME | — | ✅ |
| 58 | DosSupplyLinesIntPEOFirmDemandFlag | FIRM_DEMAND_FLAG | — | ✅ |
| 59 | DosSupplyLinesIntPEOFirmPlannedFlag | FIRM_PLANNED_FLAG | — | ✅ |
| 60 | DosSupplyLinesIntPEOFundsStatus | FUNDS_STATUS | — | ✅ |
| 61 | DosSupplyLinesIntPEOGopSplitReferenceId | GOP_SPLIT_REFERENCE_ID | — | ✅ |
| 62 | DosSupplyLinesIntPEOGroupCode | GROUP_CODE | — | ✅ |
| 63 | DosSupplyLinesIntPEOGroupId | GROUP_ID | — | ✅ |
| 64 | DosSupplyLinesIntPEOHeaderInterfaceId | HEADER_INTERFACE_ID | — | ✅ |
| 65 | DosSupplyLinesIntPEOHeaderNumber | HEADER_NUMBER | — | ✅ |
| 66 | DosSupplyLinesIntPEOInterfaceBatchNumber | INTERFACE_BATCH_NUMBER | — | ✅ |
| 67 | DosSupplyLinesIntPEOInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | ✅ |
| 68 | DosSupplyLinesIntPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 69 | DosSupplyLinesIntPEOItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 70 | DosSupplyLinesIntPEOItemNumber | ITEM_NUMBER | — | ✅ |
| 71 | DosSupplyLinesIntPEOItemRevision | ITEM_REVISION | — | ✅ |
| 72 | DosSupplyLinesIntPEOItemType | ITEM_TYPE | — | ✅ |
| 73 | DosSupplyLinesIntPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 74 | DosSupplyLinesIntPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 75 | DosSupplyLinesIntPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 76 | DosSupplyLinesIntPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 77 | DosSupplyLinesIntPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 78 | DosSupplyLinesIntPEOLineInterfaceId | LINE_INTERFACE_ID | 🔑 | ✅ |
| 79 | DosSupplyLinesIntPEOLineLocationId | LINE_LOCATION_ID | — | ✅ |
| 80 | DosSupplyLinesIntPEOLineNumber | LINE_NUMBER | — | ✅ |
| 81 | DosSupplyLinesIntPEOLineTypeId | LINE_TYPE_ID | — | ✅ |
| 82 | DosSupplyLinesIntPEOLoadRequestId | LOAD_REQUEST_ID | — | ✅ |
| 83 | DosSupplyLinesIntPEOLoadType | LOAD_TYPE | — | ✅ |
| 84 | DosSupplyLinesIntPEOMovementRequestFlag | MOVEMENT_REQUEST_FLAG | — | ✅ |
| 85 | DosSupplyLinesIntPEONeedByDate | NEED_BY_DATE | — | ✅ |
| 86 | DosSupplyLinesIntPEONetQuantity | NET_QUANTITY | — | ✅ |
| 87 | DosSupplyLinesIntPEONetQuantityUomCode | NET_QUANTITY_UOM_CODE | — | ✅ |
| 88 | DosSupplyLinesIntPEONoteToReceiver | NOTE_TO_RECEIVER | — | ✅ |
| 89 | DosSupplyLinesIntPEONoteToSupplier | NOTE_TO_SUPPLIER | — | ✅ |
| 90 | DosSupplyLinesIntPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 91 | DosSupplyLinesIntPEOOnHoldReasonCode | ON_HOLD_REASON_CODE | — | ✅ |
| 92 | DosSupplyLinesIntPEOOutsideProcessingFlag | OUTSIDE_PROCESSING_FLAG | — | ✅ |
| 93 | DosSupplyLinesIntPEOParentItemId | PARENT_ITEM_ID | — | ✅ |
| 94 | DosSupplyLinesIntPEOParentLineId | PARENT_LINE_ID | — | ✅ |
| 95 | DosSupplyLinesIntPEOParentLineNumber | PARENT_LINE_NUMBER | — | ✅ |
| 96 | DosSupplyLinesIntPEOPreparerId | PREPARER_ID | — | ✅ |
| 97 | DosSupplyLinesIntPEOProcessStatus | PROCESS_STATUS | — | ✅ |
| 98 | DosSupplyLinesIntPEOPurchaseOrderHeaderId | PURCHASE_ORDER_HEADER_ID | — | ✅ |
| 99 | DosSupplyLinesIntPEOPurchaseOrderLineId | PURCHASE_ORDER_LINE_ID | — | ✅ |
| 100 | DosSupplyLinesIntPEOPurchaseOrderLineNumber | PURCHASE_ORDER_LINE_NUMBER | — | ✅ |
| 101 | DosSupplyLinesIntPEOPurchaseOrderNumber | PURCHASE_ORDER_NUMBER | — | ✅ |
| 102 | DosSupplyLinesIntPEOPurchaseOrderScheduleNumber | PURCHASE_ORDER_SCHEDULE_NUMBER | — | ✅ |
| 103 | DosSupplyLinesIntPEOQuantity | QUANTITY | — | ✅ |
| 104 | DosSupplyLinesIntPEOReferenceTrackingLineId | REFERENCE_TRACKING_LINE_ID | — | ✅ |
| 105 | DosSupplyLinesIntPEORepriceFlag | REPRICE_FLAG | — | ✅ |
| 106 | DosSupplyLinesIntPEORequestId | REQUEST_ID | — | ✅ |
| 107 | DosSupplyLinesIntPEORequestedShipDate | REQUESTED_SHIP_DATE | — | ✅ |
| 108 | DosSupplyLinesIntPEORequisitionLineId | REQUISITION_LINE_ID | — | ✅ |
| 109 | DosSupplyLinesIntPEORequisitionLineNumber | REQUISITION_LINE_NUMBER | — | ✅ |
| 110 | DosSupplyLinesIntPEORequisitionNumber | REQUISITION_NUMBER | — | ✅ |
| 111 | DosSupplyLinesIntPEORequisitionSourceTypeCode | REQUISITION_SOURCE_TYPE_CODE | — | ✅ |
| 112 | DosSupplyLinesIntPEORequisitioningBuId | REQUISITIONING_BU_ID | — | ✅ |
| 113 | DosSupplyLinesIntPEOResubmitCount | RESUBMIT_COUNT | — | ✅ |
| 114 | DosSupplyLinesIntPEORoutingRevisionDate | ROUTING_REVISION_DATE | — | ✅ |
| 115 | DosSupplyLinesIntPEOSalesOrderHeaderId | SALES_ORDER_HEADER_ID | — | ✅ |
| 116 | DosSupplyLinesIntPEOSalesOrderHeaderNumber | SALES_ORDER_HEADER_NUMBER | — | ✅ |
| 117 | DosSupplyLinesIntPEOSalesOrderLineId | SALES_ORDER_LINE_ID | — | ✅ |
| 118 | DosSupplyLinesIntPEOSalesOrderLineNumber | SALES_ORDER_LINE_NUMBER | — | ✅ |
| 119 | DosSupplyLinesIntPEOScheduleGrpId | SCHEDULE_GRP_ID | — | ✅ |
| 120 | DosSupplyLinesIntPEOScheduledShipDate | SCHEDULED_SHIP_DATE | — | ✅ |
| 121 | DosSupplyLinesIntPEOSchedulingMethod | SCHEDULING_METHOD | — | ✅ |
| 122 | DosSupplyLinesIntPEOSecondaryQuantity | SECONDARY_QUANTITY | — | ✅ |
| 123 | DosSupplyLinesIntPEOSecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 124 | DosSupplyLinesIntPEOShipClassOfService | SHIP_CLASS_OF_SERVICE | — | ✅ |
| 125 | DosSupplyLinesIntPEOShipModeOfTransport | SHIP_MODE_OF_TRANSPORT | — | ✅ |
| 126 | DosSupplyLinesIntPEOShipToPartyId | SHIP_TO_PARTY_ID | — | ✅ |
| 127 | DosSupplyLinesIntPEOShipToPartySiteId | SHIP_TO_PARTY_SITE_ID | — | ✅ |
| 128 | DosSupplyLinesIntPEOShipmentFlag | SHIPMENT_FLAG | — | ✅ |
| 129 | DosSupplyLinesIntPEOShipmentPriorityCode | SHIPMENT_PRIORITY_CODE | — | ✅ |
| 130 | DosSupplyLinesIntPEOShippingMethod | SHIPPING_METHOD | — | ✅ |
| 131 | DosSupplyLinesIntPEOSourceBuId | SOURCE_BU_ID | — | ✅ |
| 132 | DosSupplyLinesIntPEOSourceLocationId | SOURCE_LOCATION_ID | — | ✅ |
| 133 | DosSupplyLinesIntPEOSourceOrganizationCode | SOURCE_ORGANIZATION_CODE | — | ✅ |
| 134 | DosSupplyLinesIntPEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | ✅ |
| 135 | DosSupplyLinesIntPEOSourceSubinventoryCode | SOURCE_SUBINVENTORY_CODE | — | ✅ |
| 136 | DosSupplyLinesIntPEOSourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 137 | DosSupplyLinesIntPEOSourceSystemType | SOURCE_SYSTEM_TYPE | — | ✅ |
| 138 | DosSupplyLinesIntPEOSplitLineReferenceId | SPLIT_LINE_REFERENCE_ID | — | ✅ |
| 139 | DosSupplyLinesIntPEOSuggestedVendorId | SUGGESTED_VENDOR_ID | — | ✅ |
| 140 | DosSupplyLinesIntPEOSuggestedVendorSiteId | SUGGESTED_VENDOR_SITE_ID | — | ✅ |
| 141 | DosSupplyLinesIntPEOSupplyOperation | SUPPLY_OPERATION | — | ✅ |
| 142 | DosSupplyLinesIntPEOSupplyOrderHeaderId | SUPPLY_ORDER_HEADER_ID | — | ✅ |
| 143 | DosSupplyLinesIntPEOSupplyOrderRefLineNumber | SUPPLY_ORDER_REF_LINE_NUMBER | — | ✅ |
| 144 | DosSupplyLinesIntPEOSupplyOrderReferenceLineId | SUPPLY_ORDER_REFERENCE_LINE_ID | — | ✅ |
| 145 | DosSupplyLinesIntPEOSupplyOrderSource | SUPPLY_ORDER_SOURCE | — | ✅ |
| 146 | DosSupplyLinesIntPEOSupplySourceSystem | SUPPLY_SOURCE_SYSTEM | — | ✅ |
| 147 | DosSupplyLinesIntPEOSupplyType | SUPPLY_TYPE | — | ✅ |
| 148 | DosSupplyLinesIntPEOTransferOrderHeaderId | TRANSFER_ORDER_HEADER_ID | — | ✅ |
| 149 | DosSupplyLinesIntPEOTransferOrderHeaderNumber | TRANSFER_ORDER_HEADER_NUMBER | — | ✅ |
| 150 | DosSupplyLinesIntPEOTransferOrderLineId | TRANSFER_ORDER_LINE_ID | — | ✅ |
| 151 | DosSupplyLinesIntPEOTransferOrderLineNumber | TRANSFER_ORDER_LINE_NUMBER | — | ✅ |
| 152 | DosSupplyLinesIntPEOTransferPrice | TRANSFER_PRICE | — | ✅ |
| 153 | DosSupplyLinesIntPEOTransferPriceCurrencyCode | TRANSFER_PRICE_CURRENCY_CODE | — | ✅ |
| 154 | DosSupplyLinesIntPEOUomCode | UOM_CODE | — | ✅ |
| 155 | DosSupplyLinesIntPEOWorkDefinitionAsOfDate | WORK_DEFINITION_AS_OF_DATE | — | ✅ |
| 156 | DosSupplyLinesIntPEOWorkDefinitionId | WORK_DEFINITION_ID | — | ✅ |
| 157 | DosSupplyLinesIntPEOWorkDefinitionName | WORK_DEFINITION_NAME | — | ✅ |
| 158 | DosSupplyLinesIntPEOWorkMethodCode | WORK_METHOD_CODE | — | ✅ |
| 159 | DosSupplyLinesIntPEOWorkOrderCompletionDate | WORK_ORDER_COMPLETION_DATE | — | ✅ |
| 160 | DosSupplyLinesIntPEOWorkOrderDescription | WORK_ORDER_DESCRIPTION | — | ✅ |
| 161 | DosSupplyLinesIntPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |
| 162 | DosSupplyLinesIntPEOWorkOrderNumber | WORK_ORDER_NUMBER | — | ✅ |
| 163 | DosSupplyLinesIntPEOWorkOrderStartDate | WORK_ORDER_START_DATE | — | ✅ |
| 164 | DosSupplyLinesIntPEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | ✅ |
| 165 | DosSupplyLinesIntPEOWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | ✅ |
| 166 | DosSupplyLinesIntPEOWorkOrderType | WORK_ORDER_TYPE | — | ✅ |
| 167 | DosSupplyLinesIntPEOWorkProcessName | WORK_PROCESS_NAME | — | ✅ |
| 168 | DosSupplyLinesIntPEOXferAttributeCategory | XFER_ATTRIBUTE_CATEGORY | — | ✅ |
| 169 | DosSupplyLinesIntPEOXferAttributeChar1 | XFER_ATTRIBUTE_CHAR1 | — | ✅ |
| 170 | DosSupplyLinesIntPEOXferAttributeChar10 | XFER_ATTRIBUTE_CHAR10 | — | ✅ |
| 171 | DosSupplyLinesIntPEOXferAttributeChar11 | XFER_ATTRIBUTE_CHAR11 | — | ✅ |
| 172 | DosSupplyLinesIntPEOXferAttributeChar12 | XFER_ATTRIBUTE_CHAR12 | — | ✅ |
| 173 | DosSupplyLinesIntPEOXferAttributeChar13 | XFER_ATTRIBUTE_CHAR13 | — | ✅ |
| 174 | DosSupplyLinesIntPEOXferAttributeChar14 | XFER_ATTRIBUTE_CHAR14 | — | ✅ |
| 175 | DosSupplyLinesIntPEOXferAttributeChar15 | XFER_ATTRIBUTE_CHAR15 | — | ✅ |
| 176 | DosSupplyLinesIntPEOXferAttributeChar16 | XFER_ATTRIBUTE_CHAR16 | — | ✅ |
| 177 | DosSupplyLinesIntPEOXferAttributeChar17 | XFER_ATTRIBUTE_CHAR17 | — | ✅ |
| 178 | DosSupplyLinesIntPEOXferAttributeChar18 | XFER_ATTRIBUTE_CHAR18 | — | ✅ |
| 179 | DosSupplyLinesIntPEOXferAttributeChar19 | XFER_ATTRIBUTE_CHAR19 | — | ✅ |
| 180 | DosSupplyLinesIntPEOXferAttributeChar2 | XFER_ATTRIBUTE_CHAR2 | — | ✅ |
| 181 | DosSupplyLinesIntPEOXferAttributeChar20 | XFER_ATTRIBUTE_CHAR20 | — | ✅ |
| 182 | DosSupplyLinesIntPEOXferAttributeChar3 | XFER_ATTRIBUTE_CHAR3 | — | ✅ |
| 183 | DosSupplyLinesIntPEOXferAttributeChar4 | XFER_ATTRIBUTE_CHAR4 | — | ✅ |
| 184 | DosSupplyLinesIntPEOXferAttributeChar5 | XFER_ATTRIBUTE_CHAR5 | — | ✅ |
| 185 | DosSupplyLinesIntPEOXferAttributeChar6 | XFER_ATTRIBUTE_CHAR6 | — | ✅ |
| 186 | DosSupplyLinesIntPEOXferAttributeChar7 | XFER_ATTRIBUTE_CHAR7 | — | ✅ |
| 187 | DosSupplyLinesIntPEOXferAttributeChar8 | XFER_ATTRIBUTE_CHAR8 | — | ✅ |
| 188 | DosSupplyLinesIntPEOXferAttributeChar9 | XFER_ATTRIBUTE_CHAR9 | — | ✅ |
| 189 | DosSupplyLinesIntPEOXferAttributeDate1 | XFER_ATTRIBUTE_DATE1 | — | ✅ |
| 190 | DosSupplyLinesIntPEOXferAttributeDate2 | XFER_ATTRIBUTE_DATE2 | — | ✅ |
| 191 | DosSupplyLinesIntPEOXferAttributeDate3 | XFER_ATTRIBUTE_DATE3 | — | ✅ |
| 192 | DosSupplyLinesIntPEOXferAttributeDate4 | XFER_ATTRIBUTE_DATE4 | — | ✅ |
| 193 | DosSupplyLinesIntPEOXferAttributeDate5 | XFER_ATTRIBUTE_DATE5 | — | ✅ |
| 194 | DosSupplyLinesIntPEOXferAttributeNumber1 | XFER_ATTRIBUTE_NUMBER1 | — | ✅ |
| 195 | DosSupplyLinesIntPEOXferAttributeNumber10 | XFER_ATTRIBUTE_NUMBER10 | — | ✅ |
| 196 | DosSupplyLinesIntPEOXferAttributeNumber2 | XFER_ATTRIBUTE_NUMBER2 | — | ✅ |
| 197 | DosSupplyLinesIntPEOXferAttributeNumber3 | XFER_ATTRIBUTE_NUMBER3 | — | ✅ |
| 198 | DosSupplyLinesIntPEOXferAttributeNumber4 | XFER_ATTRIBUTE_NUMBER4 | — | ✅ |
| 199 | DosSupplyLinesIntPEOXferAttributeNumber5 | XFER_ATTRIBUTE_NUMBER5 | — | ✅ |
| 200 | DosSupplyLinesIntPEOXferAttributeNumber6 | XFER_ATTRIBUTE_NUMBER6 | — | ✅ |
| 201 | DosSupplyLinesIntPEOXferAttributeNumber7 | XFER_ATTRIBUTE_NUMBER7 | — | ✅ |
| 202 | DosSupplyLinesIntPEOXferAttributeNumber8 | XFER_ATTRIBUTE_NUMBER8 | — | ✅ |
| 203 | DosSupplyLinesIntPEOXferAttributeNumber9 | XFER_ATTRIBUTE_NUMBER9 | — | ✅ |
| 204 | DosSupplyLinesIntPEOXferAttributeTimestamp1 | XFER_ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 205 | DosSupplyLinesIntPEOXferAttributeTimestamp2 | XFER_ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 206 | DosSupplyLinesIntPEOXferAttributeTimestamp3 | XFER_ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 207 | DosSupplyLinesIntPEOXferAttributeTimestamp4 | XFER_ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 208 | DosSupplyLinesIntPEOXferAttributeTimestamp5 | XFER_ATTRIBUTE_TIMESTAMP5 | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
