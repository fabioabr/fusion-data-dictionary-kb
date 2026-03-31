---
id: DOC-PO-PVO-RequisitionLineExtractPVO
doc_type: system-doc
title: "RequisitionLineExtractPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - RequisitionLineExtractPVO
  - requisitionlineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RequisitionLineExtractPVO

## 📌 Visão Geral

Extrai as linhas de requisições de compra para carga BICC, detalhando itens solicitados, quantidades, estimativas de preço, fornecedores sugeridos e local de entrega. Permite análise de demanda por categoria.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PorBiccExtractAM.RequisitionLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 250 | 5 | 1 | 199 | 80% |

---

## 🔗 Tabelas Relacionadas

- [[egp_categories_vl|EGP_CATEGORIES_VL]] — 3 atributos (3 BICC)
- [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]] — 3 atributos (3 BICC)
- [[hr_locations_all_f_vl|HR_LOCATIONS_ALL_F_VL]] — 4 atributos (4 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 5 atributos (5 BICC)
- [[por_requisition_lines_all|POR_REQUISITION_LINES_ALL]] — 235 atributos (1 PKs, 184 BICC)

---

## ⚙️ Atributos

### [[egp_categories_vl|EGP_CATEGORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryId1 | CATEGORY_ID | — | ✅ |
| 2 | CategoryName | CATEGORY_NAME | — | ✅ |
| 3 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | ✅ |

### [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 2 | ItemNumber | ITEM_NUMBER | — | ✅ |
| 3 | OrganizationId | ORGANIZATION_ID | — | ✅ |

### [[hr_locations_all_f_vl|HR_LOCATIONS_ALL_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | LocationId | LOCATION_ID | — | ✅ |
| 4 | LocationName | LOCATION_NAME | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate1 | EFFECTIVE_END_DATE | — | ✅ |
| 2 | EffectiveStartDate1 | EFFECTIVE_START_DATE | — | ✅ |
| 3 | ListName | LIST_NAME | — | ✅ |
| 4 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | ✅ |
| 5 | PersonNameId | PERSON_NAME_ID | — | ✅ |

### [[por_requisition_lines_all|POR_REQUISITION_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionRequiredCode | ACTION_REQUIRED_CODE | — | ✅ |
| 2 | AdditionalContactEmail | ALT_SUPPLIER_CONTACT_EMAILS | — | ✅ |
| 3 | Amount | AMOUNT | — | ✅ |
| 4 | AssessableValue | ASSESSABLE_VALUE | — | ✅ |
| 5 | AssignedBuyerId | ASSIGNED_BUYER_ID | — | ✅ |
| 6 | AtSourcingFlag | AT_SOURCING_FLAG | — | ✅ |
| 7 | Attribute1 | ATTRIBUTE1 | — | — |
| 8 | Attribute10 | ATTRIBUTE10 | — | — |
| 9 | Attribute11 | ATTRIBUTE11 | — | — |
| 10 | Attribute12 | ATTRIBUTE12 | — | — |
| 11 | Attribute13 | ATTRIBUTE13 | — | — |
| 12 | Attribute14 | ATTRIBUTE14 | — | — |
| 13 | Attribute15 | ATTRIBUTE15 | — | — |
| 14 | Attribute16 | ATTRIBUTE16 | — | — |
| 15 | Attribute17 | ATTRIBUTE17 | — | — |
| 16 | Attribute18 | ATTRIBUTE18 | — | — |
| 17 | Attribute19 | ATTRIBUTE19 | — | — |
| 18 | Attribute2 | ATTRIBUTE2 | — | — |
| 19 | Attribute20 | ATTRIBUTE20 | — | — |
| 20 | Attribute3 | ATTRIBUTE3 | — | — |
| 21 | Attribute4 | ATTRIBUTE4 | — | — |
| 22 | Attribute5 | ATTRIBUTE5 | — | — |
| 23 | Attribute6 | ATTRIBUTE6 | — | — |
| 24 | Attribute7 | ATTRIBUTE7 | — | — |
| 25 | Attribute8 | ATTRIBUTE8 | — | — |
| 26 | Attribute9 | ATTRIBUTE9 | — | — |
| 27 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 28 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 29 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 30 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 31 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 32 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 33 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 34 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 35 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 36 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 37 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 38 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 39 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 40 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 41 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 42 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 43 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 44 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 45 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 46 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 47 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 48 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 49 | AttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 50 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 51 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 52 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 53 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 54 | AttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 55 | AttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 56 | AttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 57 | AttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 58 | AuctionDisplayNumber | AUCTION_DISPLAY_NUMBER | — | ✅ |
| 59 | AuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 60 | AuctionLineNumber | AUCTION_LINE_NUMBER | — | ✅ |
| 61 | BackToBackFlag | BACK_TO_BACK_FLAG | — | ✅ |
| 62 | BaseModelId | BASE_MODEL_ID | — | ✅ |
| 63 | BaseModelPrice | BASE_MODEL_PRICE | — | ✅ |
| 64 | BidLineNumber | BID_LINE_NUMBER | — | ✅ |
| 65 | BidNumber | BID_NUMBER | — | ✅ |
| 66 | BpaPriceUserOverrideFlag | BPA_PRICE_USER_OVERRIDE_FLAG | — | ✅ |
| 67 | BuyerProcessingFlag | BUYER_PROCESSING_FLAG | — | ✅ |
| 68 | CancelDate | CANCEL_DATE | — | ✅ |
| 69 | CancelFlag | CANCEL_FLAG | — | ✅ |
| 70 | CancelReason | CANCEL_REASON | — | ✅ |
| 71 | CarrierId | CARRIER_ID | — | ✅ |
| 72 | CategoryId | CATEGORY_ID | — | ✅ |
| 73 | ConfiguredItemFlag | CONFIGURED_ITEM_FLAG | — | ✅ |
| 74 | ContentPrcBuId | CONTENT_PRC_BU_ID | — | ✅ |
| 75 | CreatedBy | CREATED_BY | — | ✅ |
| 76 | CreationDate | CREATION_DATE | — | ✅ |
| 77 | CurrencyAmount | CURRENCY_AMOUNT | — | ✅ |
| 78 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 79 | CurrencyUnitPrice | CURRENCY_UNIT_PRICE | — | ✅ |
| 80 | CustomerItem | CUSTOMER_ITEM | — | ✅ |
| 81 | CustomerItemDesc | CUSTOMER_ITEM_DESC | — | ✅ |
| 82 | CustomerPoLineNumber | CUSTOMER_PO_LINE_NUMBER | — | ✅ |
| 83 | CustomerPoNumber | CUSTOMER_PO_NUMBER | — | ✅ |
| 84 | CustomerPoScheduleNumber | CUSTOMER_PO_SCHEDULE_NUMBER | — | ✅ |
| 85 | DaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | ✅ |
| 86 | DaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | ✅ |
| 87 | DefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | ✅ |
| 88 | DeliverToCustContactId | DELIVER_TO_CUST_CONTACT_ID | — | ✅ |
| 89 | DeliverToCustId | DELIVER_TO_CUST_ID | — | ✅ |
| 90 | DeliverToCustLocationId | DELIVER_TO_CUST_LOCATION_ID | — | ✅ |
| 91 | DeliverToLocationId | DELIVER_TO_LOCATION_ID | — | ✅ |
| 92 | DestinationOrganizationId | DESTINATION_ORGANIZATION_ID | — | ✅ |
| 93 | DestinationSubinventory | DESTINATION_SUBINVENTORY | — | ✅ |
| 94 | DestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 95 | DocumentSubType | DOCUMENT_SUB_TYPE | — | ✅ |
| 96 | ExternalCategoryValue | EXTERNAL_CATEGORY_VALUE | — | ✅ |
| 97 | ExternalUomQuantity | EXTERNAL_UOM_QUANTITY | — | ✅ |
| 98 | ExternalUomValue | EXTERNAL_UOM_VALUE | — | ✅ |
| 99 | FinalDischargeLocationId | FINAL_DISCHARGE_LOCATION_ID | — | ✅ |
| 100 | FirmFlag | FIRM_FLAG | — | ✅ |
| 101 | FirstPtyRegId | FIRST_PTY_REG_ID | — | ✅ |
| 102 | FundsStatus | FUNDS_STATUS | — | ✅ |
| 103 | HazardClassId | HAZARD_CLASS_ID | — | ✅ |
| 104 | InfoTemplateTouchedFlag | INFO_TEMPLATE_TOUCHED_FLAG | — | ✅ |
| 105 | InterfaceLineKey | INTERFACE_LINE_KEY | — | ✅ |
| 106 | ItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 107 | ItemId | ITEM_ID | — | ✅ |
| 108 | ItemRevision | ITEM_REVISION | — | ✅ |
| 109 | ItemSource | ITEM_SOURCE | — | ✅ |
| 110 | ItemUserOverrideFlag | ITEM_USER_OVERRIDE_FLAG | — | ✅ |
| 111 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 112 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 113 | LastApprovalDate | LAST_APPROVAL_DATE | — | ✅ |
| 114 | LastSubmittedDate | LAST_SUBMITTED_DATE | — | ✅ |
| 115 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 116 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 117 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 118 | LifecycleStatus | LIFECYCLE_STATUS | — | ✅ |
| 119 | LineGroup | LINE_GROUP | — | ✅ |
| 120 | LineIntendedUse | LINE_INTENDED_USE | — | ✅ |
| 121 | LineIntendedUseId | LINE_INTENDED_USE_ID | — | ✅ |
| 122 | LineLocationId | LINE_LOCATION_ID | — | ✅ |
| 123 | LineNumber | LINE_NUMBER | — | ✅ |
| 124 | LineStatus | LINE_STATUS | — | ✅ |
| 125 | LineTypeId | LINE_TYPE_ID | — | ✅ |
| 126 | ManufacturerName | MANUFACTURER_NAME | — | ✅ |
| 127 | ManufacturerPartNumber | MANUFACTURER_PART_NUMBER | — | ✅ |
| 128 | MatchingBasis | MATCHING_BASIS | — | ✅ |
| 129 | ModeOfTransport | MODE_OF_TRANSPORT | — | ✅ |
| 130 | ModifiedByBuyerFlag | MODIFIED_BY_BUYER_FLAG | — | ✅ |
| 131 | ModifiedByBuyerId | MODIFIED_BY_BUYER_ID | — | ✅ |
| 132 | NeedByDate | NEED_BY_DATE | — | ✅ |
| 133 | NegotiatedByPreparerFlag | NEGOTIATED_BY_PREPARER_FLAG | — | ✅ |
| 134 | NegotiationRequiredFlag | NEGOTIATION_REQUIRED_FLAG | — | ✅ |
| 135 | NewSupplierFlag | NEW_SUPPLIER_FLAG | — | ✅ |
| 136 | NoteToBuyer | NOTE_TO_BUYER | — | ✅ |
| 137 | NoteToReceiver | NOTE_TO_RECEIVER | — | ✅ |
| 138 | NoteToSupplier | NOTE_TO_SUPPLIER | — | ✅ |
| 139 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 140 | OnRfqFlag | ON_RFQ_FLAG | — | ✅ |
| 141 | OneTimeLocationFlag | ONE_TIME_LOCATION_FLAG | — | ✅ |
| 142 | OptionsPrice | OPTIONS_PRICE | — | ✅ |
| 143 | OrchestrationCode | ORCHESTRATION_CODE | — | ✅ |
| 144 | OrderTypeLookupCode | ORDER_TYPE_LOOKUP_CODE | — | ✅ |
| 145 | OriginalApprovalDate | ORIGINAL_APPROVAL_DATE | — | ✅ |
| 146 | OriginalSubmittedDate | ORIGINAL_SUBMITTED_DATE | — | ✅ |
| 147 | ParentReqLineId | PARENT_REQ_LINE_ID | — | ✅ |
| 148 | PcardFlag | PCARD_FLAG | — | ✅ |
| 149 | PoHeaderId | PO_HEADER_ID | — | ✅ |
| 150 | PoLineId | PO_LINE_ID | — | ✅ |
| 151 | PrcBuId | PRC_BU_ID | — | ✅ |
| 152 | PriceVarianceExceededAmt | PRICE_VARIANCE_EXCEEDED_AMT | — | ✅ |
| 153 | PriceVarianceExceededFlag | PRICE_VARIANCE_EXCEEDED_FLAG | — | ✅ |
| 154 | ProductCategory | PRODUCT_CATEGORY | — | ✅ |
| 155 | ProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | ✅ |
| 156 | ProductFiscClassificationId | PRODUCT_FISC_CLASSIFICATION_ID | — | ✅ |
| 157 | ProductType | PRODUCT_TYPE | — | ✅ |
| 158 | PublicListId | PUBLIC_LIST_ID | — | ✅ |
| 159 | PunchoutCatalogId | PUNCHOUT_CATALOG_ID | — | ✅ |
| 160 | PurchaseBasis | PURCHASE_BASIS | — | ✅ |
| 161 | QtyRcvTolerance | QTY_RCV_TOLERANCE | — | ✅ |
| 162 | Quantity | QUANTITY | — | ✅ |
| 163 | Rate | RATE | — | ✅ |
| 164 | RateDate | RATE_DATE | — | ✅ |
| 165 | RateType | RATE_TYPE | — | ✅ |
| 166 | ReceiptCloseTolerancePercent | QTY_UNDER_RCV_TOLERANCE | — | ✅ |
| 167 | ReinstateLineLocationId | REINSTATE_LINE_LOCATION_ID | — | ✅ |
| 168 | RepriceFlag | REPRICE_FLAG | — | ✅ |
| 169 | ReqBuId | REQ_BU_ID | — | ✅ |
| 170 | ReqPoInstanceId | REQ_PO_INSTANCE_ID | — | ✅ |
| 171 | ReqsInPoolFlag | REQS_IN_POOL_FLAG | — | ✅ |
| 172 | ReqtopoAutoFailedReason | REQTOPO_AUTO_FAILED_REASON | — | ✅ |
| 173 | ReqtopoAutomationFailed | REQTOPO_AUTOMATION_FAILED | — | ✅ |
| 174 | RequestId | REQUEST_ID | — | ✅ |
| 175 | RequestedShipDate | REQUESTED_SHIP_DATE | — | ✅ |
| 176 | RequesterId | REQUESTER_ID | — | ✅ |
| 177 | RequesterSupervisorLevel1 | REQUESTER_SUPERVISOR_LEVEL1 | — | ✅ |
| 178 | RequesterSupervisorLevel10 | REQUESTER_SUPERVISOR_LEVEL10 | — | ✅ |
| 179 | RequesterSupervisorLevel2 | REQUESTER_SUPERVISOR_LEVEL2 | — | ✅ |
| 180 | RequesterSupervisorLevel3 | REQUESTER_SUPERVISOR_LEVEL3 | — | ✅ |
| 181 | RequesterSupervisorLevel4 | REQUESTER_SUPERVISOR_LEVEL4 | — | ✅ |
| 182 | RequesterSupervisorLevel5 | REQUESTER_SUPERVISOR_LEVEL5 | — | ✅ |
| 183 | RequesterSupervisorLevel6 | REQUESTER_SUPERVISOR_LEVEL6 | — | ✅ |
| 184 | RequesterSupervisorLevel7 | REQUESTER_SUPERVISOR_LEVEL7 | — | ✅ |
| 185 | RequesterSupervisorLevel8 | REQUESTER_SUPERVISOR_LEVEL8 | — | ✅ |
| 186 | RequesterSupervisorLevel9 | REQUESTER_SUPERVISOR_LEVEL9 | — | ✅ |
| 187 | RequisitionHeaderId | REQUISITION_HEADER_ID | — | ✅ |
| 188 | RequisitionLineId | REQUISITION_LINE_ID | 🔑 | ✅ |
| 189 | SalesOrderLineNumber | SALES_ORDER_LINE_NUMBER | — | ✅ |
| 190 | SalesOrderNumber | SALES_ORDER_NUMBER | — | ✅ |
| 191 | SalesOrderScheduleNumber | SALES_ORDER_SCHEDULE_NUMBER | — | ✅ |
| 192 | SecondaryQuantity | SECONDARY_QUANTITY | — | ✅ |
| 193 | SecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 194 | ServiceLevel | SERVICE_LEVEL | — | ✅ |
| 195 | ShipToCustContactId | SHIP_TO_CUST_CONTACT_ID | — | ✅ |
| 196 | ShipToCustId | SHIP_TO_CUST_ID | — | ✅ |
| 197 | ShipToCustLocationId | SHIP_TO_CUST_LOCATION_ID | — | ✅ |
| 198 | SmartFormId | SMART_FORM_ID | — | ✅ |
| 199 | SourceDocHeaderId | SOURCE_DOC_HEADER_ID | — | ✅ |
| 200 | SourceDocLineId | SOURCE_DOC_LINE_ID | — | ✅ |
| 201 | SourceDocumentType | SOURCE_DOCUMENT_TYPE | — | ✅ |
| 202 | SourceOrganizationId | SOURCE_ORGANIZATION_ID | — | ✅ |
| 203 | SourceSubinventory | SOURCE_SUBINVENTORY | — | ✅ |
| 204 | SourceTypeCode | SOURCE_TYPE_CODE | — | ✅ |
| 205 | SuggestedBuyerId | SUGGESTED_BUYER_ID | — | ✅ |
| 206 | SuggestedSupplierItemNumber | SUGGESTED_SUPPLIER_ITEM_NUMBER | — | ✅ |
| 207 | SuggestedVendorContact | SUGGESTED_VENDOR_CONTACT | — | ✅ |
| 208 | SuggestedVendorContactEmail | SUGGESTED_VENDOR_CONTACT_EMAIL | — | ✅ |
| 209 | SuggestedVendorContactFax | SUGGESTED_VENDOR_CONTACT_FAX | — | ✅ |
| 210 | SuggestedVendorContactPhone | SUGGESTED_VENDOR_CONTACT_PHONE | — | ✅ |
| 211 | SuggestedVendorName | SUGGESTED_VENDOR_NAME | — | ✅ |
| 212 | SuggestedVendorSite | SUGGESTED_VENDOR_SITE | — | ✅ |
| 213 | SupplierDuns | SUPPLIER_DUNS | — | ✅ |
| 214 | SupplierRefNumber | SUPPLIER_REF_NUMBER | — | ✅ |
| 215 | TaxAttrUserOverrideFlag | TAX_ATTR_USER_OVERRIDE_FLAG | — | ✅ |
| 216 | TaxClassificationCode | TAX_CLASSIFICATION_CODE | — | ✅ |
| 217 | ThirdPtyRegId | THIRD_PTY_REG_ID | — | ✅ |
| 218 | ToHeaderId | TO_HEADER_ID | — | ✅ |
| 219 | ToLineId | TO_LINE_ID | — | ✅ |
| 220 | TrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 221 | UnNumberId | UN_NUMBER_ID | — | ✅ |
| 222 | UnitPrice | UNIT_PRICE | — | ✅ |
| 223 | UnspscCode | UNSPSC_CODE | — | ✅ |
| 224 | UomCode | UOM_CODE | — | ✅ |
| 225 | UrgentFlag | URGENT_FLAG | — | ✅ |
| 226 | UserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | ✅ |
| 227 | VendorContactId | VENDOR_CONTACT_ID | — | ✅ |
| 228 | VendorId | VENDOR_ID | — | ✅ |
| 229 | VendorSiteId | VENDOR_SITE_ID | — | ✅ |
| 230 | WorkOrderId | WORK_ORDER_ID | — | ✅ |
| 231 | WorkOrderNumber | WORK_ORDER_NUMBER | — | ✅ |
| 232 | WorkOrderOperationId | WORK_ORDER_OPERATION_ID | — | ✅ |
| 233 | WorkOrderOperationSeq | WORK_ORDER_OPERATION_SEQ | — | ✅ |
| 234 | WorkOrderProduct | WORK_ORDER_PRODUCT | — | ✅ |
| 235 | WorkOrderSubType | WORK_ORDER_SUB_TYPE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
