---
id: DOC-AR-PVO-ReceivingIntransitShipmentsPVO
doc_type: system-doc
title: "ReceivingIntransitShipmentsPVO — PVO Accounts Receivable"
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
  - ReceivingIntransitShipmentsPVO
  - receivingintransitshipmentspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReceivingIntransitShipmentsPVO

## 📌 Visão Geral

Extrai as remessas em trânsito no processo de recebimento, com dados de ordem de compra, linhas e lotes. Permite rastrear materiais enviados mas ainda não recebidos, impactando provisões contábeis e gestão de estoque em trânsito.

**Caminho:** `FscmTopModelAM.RcvReceiptsAM.ReceivingIntransitShipmentsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 673 | 7 | 2 | 31 | 5% |

---

## 🔗 Tabelas Relacionadas

- [[inv_org_parameters_v|INV_ORG_PARAMETERS_V]] — 1 atributos (1 PKs, 1 BICC)
- [[po_lines_all|PO_LINES_ALL]] — 194 atributos
- [[po_line_locations_all|PO_LINE_LOCATIONS_ALL]] — 247 atributos
- [[rcv_lots_supply|RCV_LOTS_SUPPLY]] — 8 atributos
- [[rcv_serials_supply|RCV_SERIALS_SUPPLY]] — 5 atributos
- [[rcv_shipment_headers|RCV_SHIPMENT_HEADERS]] — 81 atributos (11 BICC)
- [[rcv_shipment_lines|RCV_SHIPMENT_LINES]] — 137 atributos (1 PKs, 19 BICC)

---

## ⚙️ Atributos

### [[inv_org_parameters_v|INV_ORG_PARAMETERS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |

### [[po_lines_all|PO_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgingPeriodDays | AGING_PERIOD_DAYS | — | — |
| 2 | AllowDescriptionUpdateFlag | ALLOW_DESCRIPTION_UPDATE_FLAG | — | — |
| 3 | AllowPriceOverrideFlag | ALLOW_PRICE_OVERRIDE_FLAG | — | — |
| 4 | Amount | AMOUNT | — | — |
| 5 | AmountReleased | AMOUNT_RELEASED | — | — |
| 6 | Attribute1 | ATTRIBUTE1 | — | — |
| 7 | Attribute10 | ATTRIBUTE10 | — | — |
| 8 | Attribute11 | ATTRIBUTE11 | — | — |
| 9 | Attribute12 | ATTRIBUTE12 | — | — |
| 10 | Attribute13 | ATTRIBUTE13 | — | — |
| 11 | Attribute14 | ATTRIBUTE14 | — | — |
| 12 | Attribute15 | ATTRIBUTE15 | — | — |
| 13 | Attribute16 | ATTRIBUTE16 | — | — |
| 14 | Attribute17 | ATTRIBUTE17 | — | — |
| 15 | Attribute18 | ATTRIBUTE18 | — | — |
| 16 | Attribute19 | ATTRIBUTE19 | — | — |
| 17 | Attribute2 | ATTRIBUTE2 | — | — |
| 18 | Attribute20 | ATTRIBUTE20 | — | — |
| 19 | Attribute3 | ATTRIBUTE3 | — | — |
| 20 | Attribute4 | ATTRIBUTE4 | — | — |
| 21 | Attribute5 | ATTRIBUTE5 | — | — |
| 22 | Attribute6 | ATTRIBUTE6 | — | — |
| 23 | Attribute7 | ATTRIBUTE7 | — | — |
| 24 | Attribute8 | ATTRIBUTE8 | — | — |
| 25 | Attribute9 | ATTRIBUTE9 | — | — |
| 26 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 27 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 28 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 29 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 30 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 31 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 32 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 33 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 34 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 35 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 36 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 37 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 38 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 39 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 40 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 41 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 42 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 43 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 44 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 45 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 46 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 47 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 48 | AttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 49 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 50 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 51 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 52 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 53 | AttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 54 | AttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 55 | AttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 56 | AttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 57 | AuctionDisplayNumber | AUCTION_DISPLAY_NUMBER | — | — |
| 58 | AuctionHeaderId | AUCTION_HEADER_ID | — | — |
| 59 | AuctionLineNumber | AUCTION_LINE_NUMBER | — | — |
| 60 | BaseModelId | BASE_MODEL_ID | — | — |
| 61 | BaseModelPrice | BASE_MODEL_PRICE | — | — |
| 62 | BaseQty | BASE_QTY | — | — |
| 63 | BaseUnitPrice | BASE_UNIT_PRICE | — | — |
| 64 | BaseUom | BASE_UOM | — | — |
| 65 | BidLineNumber | BID_LINE_NUMBER | — | — |
| 66 | BidNumber | BID_NUMBER | — | — |
| 67 | CancelDate | CANCEL_DATE | — | — |
| 68 | CancelFlag | CANCEL_FLAG | — | — |
| 69 | CancelReason | CANCEL_REASON | — | — |
| 70 | CancelledBy | CANCELLED_BY | — | — |
| 71 | CapitalExpenseFlag | CAPITAL_EXPENSE_FLAG | — | — |
| 72 | CategoryId | CATEGORY_ID | — | — |
| 73 | ClosedBy | CLOSED_BY | — | — |
| 74 | ClosedDate | CLOSED_DATE | — | — |
| 75 | ClosedReason | CLOSED_REASON | — | — |
| 76 | CommittedAmount | COMMITTED_AMOUNT | — | — |
| 77 | ConfiguredItemFlag | CONFIGURED_ITEM_FLAG | — | — |
| 78 | ConsignmentLineFlag | CONSIGNMENT_LINE_FLAG | — | — |
| 79 | ContractId | CONTRACT_ID | — | — |
| 80 | ContractorFirstName | CONTRACTOR_FIRST_NAME | — | — |
| 81 | ContractorLastName | CONTRACTOR_LAST_NAME | — | — |
| 82 | CreatedBy | CREATED_BY | — | — |
| 83 | CreationDate | CREATION_DATE | — | — |
| 84 | Discount | DISCOUNT | — | — |
| 85 | DiscountReason | DISCOUNT_REASON | — | — |
| 86 | DiscountType | DISCOUNT_TYPE | — | — |
| 87 | ExpirationDate | EXPIRATION_DATE | — | — |
| 88 | FirmDate | FIRM_DATE | — | — |
| 89 | FirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 90 | FromHeaderId | FROM_HEADER_ID | — | — |
| 91 | FromLineId | FROM_LINE_ID | — | — |
| 92 | FromLineLocationId | FROM_LINE_LOCATION_ID | — | — |
| 93 | FundsStatus | FUNDS_STATUS | — | — |
| 94 | GlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 95 | GlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 96 | GlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 97 | GlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 98 | GlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 99 | GlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 100 | GlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 101 | GlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 102 | GlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 103 | GlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 104 | GlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 105 | GlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 106 | GlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 107 | GlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 108 | GlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 109 | GlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 110 | GlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 111 | GlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 112 | GlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 113 | GlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 114 | GlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 115 | GovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 116 | HazardClassId | HAZARD_CLASS_ID | — | — |
| 117 | ItemDescription | ITEM_DESCRIPTION | — | — |
| 118 | ItemId | ITEM_ID | — | — |
| 119 | ItemRevision | ITEM_REVISION | — | — |
| 120 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 121 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 122 | JobId | JOB_ID | — | — |
| 123 | LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 124 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 125 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 126 | LastUpdatedProgram | LAST_UPDATED_PROGRAM | — | — |
| 127 | LineNum | LINE_NUM | — | — |
| 128 | LineReferenceNum | LINE_REFERENCE_NUM | — | — |
| 129 | LineStatus | LINE_STATUS | — | — |
| 130 | LineTypeId | LINE_TYPE_ID | — | — |
| 131 | ListPrice | LIST_PRICE | — | — |
| 132 | ListPricePerUnit | LIST_PRICE_PER_UNIT | — | — |
| 133 | ManualPriceChangeFlag | MANUAL_PRICE_CHANGE_FLAG | — | — |
| 134 | Manufacturer | MANUFACTURER | — | — |
| 135 | ManufacturerPartNum | MANUFACTURER_PART_NUM | — | — |
| 136 | MarketPrice | MARKET_PRICE | — | — |
| 137 | MatchingBasis | MATCHING_BASIS | — | — |
| 138 | MaxRetainageAmount | MAX_RETAINAGE_AMOUNT | — | — |
| 139 | MinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 140 | NegotiatedByPreparerFlag | NEGOTIATED_BY_PREPARER_FLAG | — | — |
| 141 | NextConsumptionAdvGenDate | NEXT_CONSUMPTION_ADV_GEN_DATE | — | — |
| 142 | NotToExceedPrice | NOT_TO_EXCEED_PRICE | — | — |
| 143 | NoteToVendor | NOTE_TO_VENDOR | — | — |
| 144 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 145 | OkeContractHeaderId | OKE_CONTRACT_HEADER_ID | — | — |
| 146 | OkeContractVersionId | OKE_CONTRACT_VERSION_ID | — | — |
| 147 | OptionsPrice | OPTIONS_PRICE | — | — |
| 148 | OrderTypeLookupCode | ORDER_TYPE_LOOKUP_CODE | — | — |
| 149 | OverToleranceErrorFlag | OVER_TOLERANCE_ERROR_FLAG | — | — |
| 150 | PJC_CONTEXT_CATEGORY | PJC_CONTEXT_CATEGORY | — | — |
| 151 | ParentItemId | PARENT_ITEM_ID | — | — |
| 152 | PoHeaderId | PO_HEADER_ID | — | — |
| 153 | PoLineId | PO_LINE_ID | — | — |
| 154 | PrcBuId | PRC_BU_ID | — | — |
| 155 | PreferredGrade | PREFERRED_GRADE | — | — |
| 156 | PriceBreakLookupCode | PRICE_BREAK_LOOKUP_CODE | — | — |
| 157 | PriceTypeLookupCode | PRICE_TYPE_LOOKUP_CODE | — | — |
| 158 | ProgramAppName | PROGRAM_APP_NAME | — | — |
| 159 | ProgramName | PROGRAM_NAME | — | — |
| 160 | ProgressPaymentRate | PROGRESS_PAYMENT_RATE | — | — |
| 161 | PurchaseBasis | PURCHASE_BASIS | — | — |
| 162 | QcGrade | QC_GRADE | — | — |
| 163 | QtyRcvTolerance | QTY_RCV_TOLERANCE | — | — |
| 164 | Quantity | QUANTITY | — | — |
| 165 | QuantityCommitted | QUANTITY_COMMITTED | — | — |
| 166 | RecoupmentRate | RECOUPMENT_RATE | — | — |
| 167 | ReferenceNum | REFERENCE_NUM | — | — |
| 168 | ReqBuId | REQ_BU_ID | — | — |
| 169 | RequestId | REQUEST_ID | — | — |
| 170 | RetainageRate | RETAINAGE_RATE | — | — |
| 171 | RetroactiveDate | RETROACTIVE_DATE | — | — |
| 172 | SecondaryQuantity | SECONDARY_QUANTITY | — | — |
| 173 | SecondaryUomCode | SECONDARY_UOM_CODE | — | — |
| 174 | SourceDocRevNum | SOURCE_DOC_REV_NUM | — | — |
| 175 | StartDate | START_DATE | — | — |
| 176 | SupplierParentItem | SUPPLIER_PARENT_ITEM | — | — |
| 177 | SupplierPartAuxid | SUPPLIER_PART_AUXID | — | — |
| 178 | SupplierRefNumber | SUPPLIER_REF_NUMBER | — | — |
| 179 | SupplierTopModel | SUPPLIER_TOP_MODEL | — | — |
| 180 | SvcAmountNotifSent | SVC_AMOUNT_NOTIF_SENT | — | — |
| 181 | SvcCompletionNotifSent | SVC_COMPLETION_NOTIF_SENT | — | — |
| 182 | TaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 183 | TaxCodeId | TAX_CODE_ID | — | — |
| 184 | TaxExclusivePrice | TAX_EXCLUSIVE_PRICE | — | — |
| 185 | TaxName | TAX_NAME | — | — |
| 186 | TaxableFlag | TAXABLE_FLAG | — | — |
| 187 | TopModelId | TOP_MODEL_ID | — | — |
| 188 | Type1099 | TYPE_1099 | — | — |
| 189 | UnNumberId | UN_NUMBER_ID | — | — |
| 190 | UnitPrice | UNIT_PRICE | — | — |
| 191 | UnorderedFlag | UNORDERED_FLAG | — | — |
| 192 | UomCode | UOM_CODE | — | — |
| 193 | VendorProductNum | VENDOR_PRODUCT_NUM | — | — |
| 194 | WorkOrderProduct | WORK_ORDER_PRODUCT | — | — |

### [[po_line_locations_all|PO_LINE_LOCATIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccrueOnReceiptFlag | ACCRUE_ON_RECEIPT_FLAG | — | — |
| 2 | AllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | — |
| 3 | Amount1 | AMOUNT | — | — |
| 4 | AmountAccepted | AMOUNT_ACCEPTED | — | — |
| 5 | AmountBilled | AMOUNT_BILLED | — | — |
| 6 | AmountCancelled | AMOUNT_CANCELLED | — | — |
| 7 | AmountFinanced | AMOUNT_FINANCED | — | — |
| 8 | AmountReceived | AMOUNT_RECEIVED | — | — |
| 9 | AmountRecouped | AMOUNT_RECOUPED | — | — |
| 10 | AmountRejected | AMOUNT_REJECTED | — | — |
| 11 | AmountShipped | AMOUNT_SHIPPED | — | — |
| 12 | AnticipatedArrivalDate | ANTICIPATED_ARRIVAL_DATE | — | — |
| 13 | AssessableValue | ASSESSABLE_VALUE | — | — |
| 14 | Attribute101 | ATTRIBUTE10 | — | — |
| 15 | Attribute110 | ATTRIBUTE1 | — | — |
| 16 | Attribute111 | ATTRIBUTE11 | — | — |
| 17 | Attribute121 | ATTRIBUTE12 | — | — |
| 18 | Attribute131 | ATTRIBUTE13 | — | — |
| 19 | Attribute141 | ATTRIBUTE14 | — | — |
| 20 | Attribute151 | ATTRIBUTE15 | — | — |
| 21 | Attribute161 | ATTRIBUTE16 | — | — |
| 22 | Attribute171 | ATTRIBUTE17 | — | — |
| 23 | Attribute181 | ATTRIBUTE18 | — | — |
| 24 | Attribute191 | ATTRIBUTE19 | — | — |
| 25 | Attribute201 | ATTRIBUTE20 | — | — |
| 26 | Attribute21 | ATTRIBUTE2 | — | — |
| 27 | Attribute31 | ATTRIBUTE3 | — | — |
| 28 | Attribute41 | ATTRIBUTE4 | — | — |
| 29 | Attribute51 | ATTRIBUTE5 | — | — |
| 30 | Attribute61 | ATTRIBUTE6 | — | — |
| 31 | Attribute71 | ATTRIBUTE7 | — | — |
| 32 | Attribute81 | ATTRIBUTE8 | — | — |
| 33 | Attribute91 | ATTRIBUTE9 | — | — |
| 34 | AttributeCategory1 | ATTRIBUTE_CATEGORY | — | — |
| 35 | AttributeDate101 | ATTRIBUTE_DATE10 | — | — |
| 36 | AttributeDate11 | ATTRIBUTE_DATE1 | — | — |
| 37 | AttributeDate21 | ATTRIBUTE_DATE2 | — | — |
| 38 | AttributeDate31 | ATTRIBUTE_DATE3 | — | — |
| 39 | AttributeDate41 | ATTRIBUTE_DATE4 | — | — |
| 40 | AttributeDate51 | ATTRIBUTE_DATE5 | — | — |
| 41 | AttributeDate61 | ATTRIBUTE_DATE6 | — | — |
| 42 | AttributeDate71 | ATTRIBUTE_DATE7 | — | — |
| 43 | AttributeDate81 | ATTRIBUTE_DATE8 | — | — |
| 44 | AttributeDate91 | ATTRIBUTE_DATE9 | — | — |
| 45 | AttributeNumber101 | ATTRIBUTE_NUMBER10 | — | — |
| 46 | AttributeNumber11 | ATTRIBUTE_NUMBER1 | — | — |
| 47 | AttributeNumber21 | ATTRIBUTE_NUMBER2 | — | — |
| 48 | AttributeNumber31 | ATTRIBUTE_NUMBER3 | — | — |
| 49 | AttributeNumber41 | ATTRIBUTE_NUMBER4 | — | — |
| 50 | AttributeNumber51 | ATTRIBUTE_NUMBER5 | — | — |
| 51 | AttributeNumber61 | ATTRIBUTE_NUMBER6 | — | — |
| 52 | AttributeNumber71 | ATTRIBUTE_NUMBER7 | — | — |
| 53 | AttributeNumber81 | ATTRIBUTE_NUMBER8 | — | — |
| 54 | AttributeNumber91 | ATTRIBUTE_NUMBER9 | — | — |
| 55 | AttributeTimestamp101 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 56 | AttributeTimestamp11 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 57 | AttributeTimestamp21 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 58 | AttributeTimestamp31 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 59 | AttributeTimestamp41 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 60 | AttributeTimestamp51 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 61 | AttributeTimestamp61 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 62 | AttributeTimestamp71 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 63 | AttributeTimestamp81 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 64 | AttributeTimestamp91 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 65 | AutoClosureMode | AUTO_CLOSURE_MODE | — | — |
| 66 | BackToBackFlag | BACK_TO_BACK_FLAG | — | — |
| 67 | BidPaymentId | BID_PAYMENT_ID | — | — |
| 68 | CalculateTaxFlag | CALCULATE_TAX_FLAG | — | — |
| 69 | CancelBudgetDate | CANCEL_BUDGET_DATE | — | — |
| 70 | CancelDate1 | CANCEL_DATE | — | — |
| 71 | CancelFlag1 | CANCEL_FLAG | — | — |
| 72 | CancelReason1 | CANCEL_REASON | — | — |
| 73 | CancelledBy1 | CANCELLED_BY | — | — |
| 74 | CarrierId | CARRIER_ID | — | — |
| 75 | ChangePromisedDateReason | CHANGE_PROMISED_DATE_REASON | — | — |
| 76 | ClosedBy1 | CLOSED_BY | — | — |
| 77 | ClosedDate1 | CLOSED_DATE | — | — |
| 78 | ClosedDateTime | CLOSED_DATE | — | — |
| 79 | ClosedForInvoiceDate | CLOSED_FOR_INVOICE_DATE | — | — |
| 80 | ClosedForReceivingDate | CLOSED_FOR_RECEIVING_DATE | — | — |
| 81 | ClosedReason1 | CLOSED_REASON | — | — |
| 82 | ConsignedFlag | CONSIGNED_FLAG | — | — |
| 83 | CountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | — |
| 84 | CreatedBy1 | CREATED_BY | — | — |
| 85 | CreationDate1 | CREATION_DATE | — | — |
| 86 | CustomerItem | CUSTOMER_ITEM | — | — |
| 87 | CustomerItemDesc | CUSTOMER_ITEM_DESC | — | — |
| 88 | CustomerPoLineNumber | CUSTOMER_PO_LINE_NUMBER | — | — |
| 89 | CustomerPoNumber | CUSTOMER_PO_NUMBER | — | — |
| 90 | CustomerPoScheduleNumber | CUSTOMER_PO_SCHEDULE_NUMBER | — | — |
| 91 | DaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | — |
| 92 | DaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | — |
| 93 | Description | DESCRIPTION | — | — |
| 94 | DestinationTypeCode | DESTINATION_TYPE_CODE | — | — |
| 95 | DropShipFlag | DROP_SHIP_FLAG | — | — |
| 96 | EncumberNow | ENCUMBER_NOW | — | — |
| 97 | EncumberedDate | ENCUMBERED_DATE | — | — |
| 98 | EncumberedFlag | ENCUMBERED_FLAG | — | — |
| 99 | EndDate | END_DATE | — | — |
| 100 | EnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | — |
| 101 | EstimatedTaxAmount | ESTIMATED_TAX_AMOUNT | — | — |
| 102 | FinalDischargeLocationId | FINAL_DISCHARGE_LOCATION_ID | — | — |
| 103 | FinalMatchFlag | FINAL_MATCH_FLAG | — | — |
| 104 | FirmDate1 | FIRM_DATE | — | — |
| 105 | FirmFlag | FIRM_FLAG | — | — |
| 106 | FirmReason | FIRM_REASON | — | — |
| 107 | FirmStatusLookupCode1 | FIRM_STATUS_LOOKUP_CODE | — | — |
| 108 | FirmedBy | FIRMED_BY | — | — |
| 109 | FobLookupCode | FOB_LOOKUP_CODE | — | — |
| 110 | FreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 111 | FromHeaderId1 | FROM_HEADER_ID | — | — |
| 112 | FromLineId1 | FROM_LINE_ID | — | — |
| 113 | FromLineLocationId1 | FROM_LINE_LOCATION_ID | — | — |
| 114 | FundsStatus1 | FUNDS_STATUS | — | — |
| 115 | GlobalAttribute101 | GLOBAL_ATTRIBUTE10 | — | — |
| 116 | GlobalAttribute110 | GLOBAL_ATTRIBUTE1 | — | — |
| 117 | GlobalAttribute111 | GLOBAL_ATTRIBUTE11 | — | — |
| 118 | GlobalAttribute121 | GLOBAL_ATTRIBUTE12 | — | — |
| 119 | GlobalAttribute131 | GLOBAL_ATTRIBUTE13 | — | — |
| 120 | GlobalAttribute141 | GLOBAL_ATTRIBUTE14 | — | — |
| 121 | GlobalAttribute151 | GLOBAL_ATTRIBUTE15 | — | — |
| 122 | GlobalAttribute161 | GLOBAL_ATTRIBUTE16 | — | — |
| 123 | GlobalAttribute171 | GLOBAL_ATTRIBUTE17 | — | — |
| 124 | GlobalAttribute181 | GLOBAL_ATTRIBUTE18 | — | — |
| 125 | GlobalAttribute191 | GLOBAL_ATTRIBUTE19 | — | — |
| 126 | GlobalAttribute201 | GLOBAL_ATTRIBUTE20 | — | — |
| 127 | GlobalAttribute21 | GLOBAL_ATTRIBUTE2 | — | — |
| 128 | GlobalAttribute31 | GLOBAL_ATTRIBUTE3 | — | — |
| 129 | GlobalAttribute41 | GLOBAL_ATTRIBUTE4 | — | — |
| 130 | GlobalAttribute51 | GLOBAL_ATTRIBUTE5 | — | — |
| 131 | GlobalAttribute61 | GLOBAL_ATTRIBUTE6 | — | — |
| 132 | GlobalAttribute71 | GLOBAL_ATTRIBUTE7 | — | — |
| 133 | GlobalAttribute81 | GLOBAL_ATTRIBUTE8 | — | — |
| 134 | GlobalAttribute91 | GLOBAL_ATTRIBUTE9 | — | — |
| 135 | GlobalAttributeCategory1 | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 136 | GovernmentContext1 | GOVERNMENT_CONTEXT | — | — |
| 137 | GroupName | GROUP_NAME | — | — |
| 138 | InputTaxClassificationCode | INPUT_TAX_CLASSIFICATION_CODE | — | — |
| 139 | InspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | — |
| 140 | InvoiceCloseTolerance | INVOICE_CLOSE_TOLERANCE | — | — |
| 141 | JobDefinitionName1 | JOB_DEFINITION_NAME | — | — |
| 142 | JobDefinitionPackage1 | JOB_DEFINITION_PACKAGE | — | — |
| 143 | LastAcceptDate | LAST_ACCEPT_DATE | — | — |
| 144 | LastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 145 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 146 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 147 | LeadTime | LEAD_TIME | — | — |
| 148 | LeadTimeUnit | LEAD_TIME_UNIT | — | — |
| 149 | LineIntendedUse | LINE_INTENDED_USE | — | — |
| 150 | LineIntendedUseId | LINE_INTENDED_USE_ID | — | — |
| 151 | LineLocationId | LINE_LOCATION_ID | — | — |
| 152 | ManualPriceChangeFlag1 | MANUAL_PRICE_CHANGE_FLAG | — | — |
| 153 | MatchOption | MATCH_OPTION | — | — |
| 154 | MatchingBasis1 | MATCHING_BASIS | — | — |
| 155 | ModeOfTransport | MODE_OF_TRANSPORT | — | — |
| 156 | NeedByDate | NEED_BY_DATE | — | — |
| 157 | NoteToReceiver | NOTE_TO_RECEIVER | — | — |
| 158 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 159 | OrchestrationCode | ORCHESTRATION_CODE | — | — |
| 160 | OriginalShipmentId | ORIGINAL_SHIPMENT_ID | — | — |
| 161 | OutsourcedAssembly | OUTSOURCED_ASSEMBLY | — | — |
| 162 | PJC_CONTEXT_CATEGORY1 | PJC_CONTEXT_CATEGORY | — | — |
| 163 | PaymentType | PAYMENT_TYPE | — | — |
| 164 | PoHeaderId1 | PO_HEADER_ID | — | — |
| 165 | PoLineId1 | PO_LINE_ID | — | — |
| 166 | PoTradingOrganizationId | PO_TRADING_ORGANIZATION_ID | — | — |
| 167 | PrcBuId1 | PRC_BU_ID | — | — |
| 168 | PreferredGrade1 | PREFERRED_GRADE | — | — |
| 169 | PriceDiscount | PRICE_DISCOUNT | — | — |
| 170 | PriceOverride | PRICE_OVERRIDE | — | — |
| 171 | ProductCategory | PRODUCT_CATEGORY | — | — |
| 172 | ProductFiscClassId | PRODUCT_FISC_CLASS_ID | — | — |
| 173 | ProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | — |
| 174 | ProductType | PRODUCT_TYPE | — | — |
| 175 | ProgramAppName1 | PROGRAM_APP_NAME | — | — |
| 176 | ProgramName1 | PROGRAM_NAME | — | — |
| 177 | PromisedDate | PROMISED_DATE | — | — |
| 178 | PromisedShipDate | PROMISED_SHIP_DATE | — | — |
| 179 | QtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | — |
| 180 | QtyRcvTolerance1 | QTY_RCV_TOLERANCE | — | — |
| 181 | Quantity1 | QUANTITY | — | — |
| 182 | QuantityAccepted | QUANTITY_ACCEPTED | — | — |
| 183 | QuantityBilled | QUANTITY_BILLED | — | — |
| 184 | QuantityCancelled | QUANTITY_CANCELLED | — | — |
| 185 | QuantityFinanced | QUANTITY_FINANCED | — | — |
| 186 | QuantityReceived | QUANTITY_RECEIVED | — | — |
| 187 | QuantityRecouped | QUANTITY_RECOUPED | — | — |
| 188 | QuantityRejected | QUANTITY_REJECTED | — | — |
| 189 | QuantityShipped | QUANTITY_SHIPPED | — | — |
| 190 | ReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | — |
| 191 | ReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 192 | ReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | — |
| 193 | ReceivingRoutingId | RECEIVING_ROUTING_ID | — | — |
| 194 | ReopenFinalCloseDate | REOPEN_FINAL_CLOSE_DATE | — | — |
| 195 | ReqBuId1 | REQ_BU_ID | — | — |
| 196 | RequestId1 | REQUEST_ID | — | — |
| 197 | RequestedShipDate | REQUESTED_SHIP_DATE | — | — |
| 198 | RetainageReleasedAmount | RETAINAGE_RELEASED_AMOUNT | — | — |
| 199 | RetainageWithheldAmount | RETAINAGE_WITHHELD_AMOUNT | — | — |
| 200 | RetroactiveDate1 | RETROACTIVE_DATE | — | — |
| 201 | SalesOrderLineNumber | SALES_ORDER_LINE_NUMBER | — | — |
| 202 | SalesOrderNumber | SALES_ORDER_NUMBER | — | — |
| 203 | SalesOrderScheduleNumber | SALES_ORDER_SCHEDULE_NUMBER | — | — |
| 204 | SalesOrderUpdateDate | SALES_ORDER_UPDATE_DATE | — | — |
| 205 | ScheduleStatus | SCHEDULE_STATUS | — | — |
| 206 | SecondaryQuantity1 | SECONDARY_QUANTITY | — | — |
| 207 | SecondaryQuantityAccepted | SECONDARY_QUANTITY_ACCEPTED | — | — |
| 208 | SecondaryQuantityCancelled | SECONDARY_QUANTITY_CANCELLED | — | — |
| 209 | SecondaryQuantityReceived | SECONDARY_QUANTITY_RECEIVED | — | — |
| 210 | SecondaryQuantityRejected | SECONDARY_QUANTITY_REJECTED | — | — |
| 211 | SecondaryQuantityShipped | SECONDARY_QUANTITY_SHIPPED | — | — |
| 212 | SecondaryUomCode1 | SECONDARY_UOM_CODE | — | — |
| 213 | ServiceLevel | SERVICE_LEVEL | — | — |
| 214 | SfoAgreementLineNumber | SFO_AGREEMENT_LINE_NUMBER | — | — |
| 215 | SfoAgreementNumber | SFO_AGREEMENT_NUMBER | — | — |
| 216 | SfoPtrId | SFO_PTR_ID | — | — |
| 217 | ShipToCustContactId | SHIP_TO_CUST_CONTACT_ID | — | — |
| 218 | ShipToCustId | SHIP_TO_CUST_ID | — | — |
| 219 | ShipToCustLocationId | SHIP_TO_CUST_LOCATION_ID | — | — |
| 220 | ShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 221 | ShipToOrganizationId | SHIP_TO_ORGANIZATION_ID | — | — |
| 222 | ShipmentClosedDate | SHIPMENT_CLOSED_DATE | — | — |
| 223 | ShipmentNum | SHIPMENT_NUM | — | — |
| 224 | ShipmentType | SHIPMENT_TYPE | — | — |
| 225 | SourceShipmentId | SOURCE_SHIPMENT_ID | — | — |
| 226 | StartDate1 | START_DATE | — | — |
| 227 | SupplierOrderLineNumber | SUPPLIER_ORDER_LINE_NUMBER | — | — |
| 228 | TaxAttributeUpdateCode1 | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 229 | TaxCodeId1 | TAX_CODE_ID | — | — |
| 230 | TaxName1 | TAX_NAME | — | — |
| 231 | TaxUserOverrideFlag | TAX_USER_OVERRIDE_FLAG | — | — |
| 232 | TaxableFlag1 | TAXABLE_FLAG | — | — |
| 233 | TermsId | TERMS_ID | — | — |
| 234 | TransactionFlowHeaderId | TRANSACTION_FLOW_HEADER_ID | — | — |
| 235 | TrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 236 | UnencumberedQuantity | UNENCUMBERED_QUANTITY | — | — |
| 237 | UnitOfMeasureClass | UNIT_OF_MEASURE_CLASS | — | — |
| 238 | UomCode1 | UOM_CODE | — | — |
| 239 | UserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 240 | ValueBasis | VALUE_BASIS | — | — |
| 241 | VmiFlag | VMI_FLAG | — | — |
| 242 | WorkApproverId | WORK_APPROVER_ID | — | — |
| 243 | WorkOrderId | WORK_ORDER_ID | — | — |
| 244 | WorkOrderNumber | WORK_ORDER_NUMBER | — | — |
| 245 | WorkOrderOperationId | WORK_ORDER_OPERATION_ID | — | — |
| 246 | WorkOrderOperationSeq | WORK_ORDER_OPERATION_SEQ | — | — |
| 247 | WorkOrderSubType | WORK_ORDER_SUB_TYPE | — | — |

### [[rcv_lots_supply|RCV_LOTS_SUPPLY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LotExpirationDate | EXPIRATION_DATE | — | — |
| 2 | LotNum | LOT_NUM | — | — |
| 3 | LotQuantity | QUANTITY | — | — |
| 4 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 5 | ReceivingLotsSupplyPEOPrimaryQuantity | PRIMARY_QUANTITY | — | — |
| 6 | ReceivingLotsSupplyPEOSecondaryQuantity | SECONDARY_QUANTITY | — | — |
| 7 | ShipmentLineIdLot | SHIPMENT_LINE_ID | — | — |
| 8 | SupplyTypeCodeLot | SUPPLY_TYPE_CODE | — | — |

### [[rcv_serials_supply|RCV_SERIALS_SUPPLY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LotNumOfSerial | LOT_NUM | — | — |
| 2 | ObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 3 | SerialNum | SERIAL_NUM | — | — |
| 4 | ShipmentLineIdSerial | SHIPMENT_LINE_ID | — | — |
| 5 | SupplyTypeCodeSerial | SUPPLY_TYPE_CODE | — | — |

### [[rcv_shipment_headers|RCV_SHIPMENT_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RcvShipmentHeadersPEOApprovalStatus | APPROVAL_STATUS | — | — |
| 2 | RcvShipmentHeadersPEOAsnStatus | ASN_STATUS | — | — |
| 3 | RcvShipmentHeadersPEOAsnType | ASN_TYPE | — | — |
| 4 | RcvShipmentHeadersPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 5 | RcvShipmentHeadersPEOBillOfLading | BILL_OF_LADING | — | ✅ |
| 6 | RcvShipmentHeadersPEOCarrierEquipment | CARRIER_EQUIPMENT | — | — |
| 7 | RcvShipmentHeadersPEOCarrierMethod | CARRIER_METHOD | — | — |
| 8 | RcvShipmentHeadersPEOComments | COMMENTS | — | — |
| 9 | RcvShipmentHeadersPEOConversionDate | CONVERSION_DATE | — | — |
| 10 | RcvShipmentHeadersPEOConversionRate | CONVERSION_RATE | — | — |
| 11 | RcvShipmentHeadersPEOConversionRateType | CONVERSION_RATE_TYPE | — | — |
| 12 | RcvShipmentHeadersPEOCreatedBy | CREATED_BY | — | — |
| 13 | RcvShipmentHeadersPEOCreationDate | CREATION_DATE | — | — |
| 14 | RcvShipmentHeadersPEOCurrencyCode | CURRENCY_CODE | — | — |
| 15 | RcvShipmentHeadersPEOCustomerId | CUSTOMER_ID | — | — |
| 16 | RcvShipmentHeadersPEOCustomerSiteId | CUSTOMER_SITE_ID | — | — |
| 17 | RcvShipmentHeadersPEOEdiControlNum | EDI_CONTROL_NUM | — | — |
| 18 | RcvShipmentHeadersPEOEmployeeId | EMPLOYEE_ID | — | — |
| 19 | RcvShipmentHeadersPEOExpectedReceiptDate | EXPECTED_RECEIPT_DATE | — | ✅ |
| 20 | RcvShipmentHeadersPEOFreightAmount | FREIGHT_AMOUNT | — | — |
| 21 | RcvShipmentHeadersPEOFreightBillNumber | FREIGHT_BILL_NUMBER | — | — |
| 22 | RcvShipmentHeadersPEOFreightCarrierId | FREIGHT_CARRIER_ID | — | — |
| 23 | RcvShipmentHeadersPEOFreightTerms | FREIGHT_TERMS | — | — |
| 24 | RcvShipmentHeadersPEOGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 25 | RcvShipmentHeadersPEOGrossWeight | GROSS_WEIGHT | — | — |
| 26 | RcvShipmentHeadersPEOGrossWeightUomCode | GROSS_WEIGHT_UOM_CODE | — | — |
| 27 | RcvShipmentHeadersPEOHazardClass | HAZARD_CLASS | — | ✅ |
| 28 | RcvShipmentHeadersPEOHazardCode | HAZARD_CODE | — | — |
| 29 | RcvShipmentHeadersPEOHazardDescription | HAZARD_DESCRIPTION | — | — |
| 30 | RcvShipmentHeadersPEOInvoiceAmount | INVOICE_AMOUNT | — | — |
| 31 | RcvShipmentHeadersPEOInvoiceDate | INVOICE_DATE | — | — |
| 32 | RcvShipmentHeadersPEOInvoiceNum | INVOICE_NUM | — | — |
| 33 | RcvShipmentHeadersPEOInvoiceStatusCode | INVOICE_STATUS_CODE | — | ✅ |
| 34 | RcvShipmentHeadersPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 35 | RcvShipmentHeadersPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 36 | RcvShipmentHeadersPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 37 | RcvShipmentHeadersPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 38 | RcvShipmentHeadersPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 39 | RcvShipmentHeadersPEOLspFlag | LSP_FLAG | — | — |
| 40 | RcvShipmentHeadersPEONetWeight | NET_WEIGHT | — | — |
| 41 | RcvShipmentHeadersPEONetWeightUomCode | NET_WEIGHT_UOM_CODE | — | — |
| 42 | RcvShipmentHeadersPEONoticeCreationDate | NOTICE_CREATION_DATE | — | — |
| 43 | RcvShipmentHeadersPEONumOfContainers | NUM_OF_CONTAINERS | — | — |
| 44 | RcvShipmentHeadersPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 45 | RcvShipmentHeadersPEOOrganizationId | ORGANIZATION_ID | — | — |
| 46 | RcvShipmentHeadersPEOPackagingCode | PACKAGING_CODE | — | — |
| 47 | RcvShipmentHeadersPEOPackingSlip | PACKING_SLIP | — | — |
| 48 | RcvShipmentHeadersPEOPaymentTermsId | PAYMENT_TERMS_ID | — | — |
| 49 | RcvShipmentHeadersPEOPerformancePeriodFrom | PERFORMANCE_PERIOD_FROM | — | — |
| 50 | RcvShipmentHeadersPEOPerformancePeriodTo | PERFORMANCE_PERIOD_TO | — | — |
| 51 | RcvShipmentHeadersPEORaDocCreationDate | RA_DOC_CREATION_DATE | — | — |
| 52 | RcvShipmentHeadersPEORaDocLastUpdateDate | RA_DOC_LAST_UPDATE_DATE | — | ✅ |
| 53 | RcvShipmentHeadersPEORaDocRevisionDate | RA_DOC_REVISION_DATE | — | — |
| 54 | RcvShipmentHeadersPEORaDocRevisionNumber | RA_DOC_REVISION_NUMBER | — | — |
| 55 | RcvShipmentHeadersPEORaDocumentCode | RA_DOCUMENT_CODE | — | — |
| 56 | RcvShipmentHeadersPEORaDocumentNumber | RA_DOCUMENT_NUMBER | — | — |
| 57 | RcvShipmentHeadersPEORaDooSourceSystemId | RA_DOO_SOURCE_SYSTEM_ID | — | — |
| 58 | RcvShipmentHeadersPEORaNoteToReceiver | RA_NOTE_TO_RECEIVER | — | — |
| 59 | RcvShipmentHeadersPEORaOutsourcerContactId | RA_OUTSOURCER_CONTACT_ID | — | — |
| 60 | RcvShipmentHeadersPEORaOutsourcerPartyId | RA_OUTSOURCER_PARTY_ID | — | — |
| 61 | RcvShipmentHeadersPEOReceiptAdviceNumber | RECEIPT_ADVICE_NUMBER | — | — |
| 62 | RcvShipmentHeadersPEOReceiptNum | RECEIPT_NUM | — | ✅ |
| 63 | RcvShipmentHeadersPEOReceiptSourceCode | RECEIPT_SOURCE_CODE | — | ✅ |
| 64 | RcvShipmentHeadersPEORemitToSiteId | REMIT_TO_SITE_ID | — | — |
| 65 | RcvShipmentHeadersPEORequestDate | REQUEST_DATE | — | — |
| 66 | RcvShipmentHeadersPEORequestId | REQUEST_ID | — | — |
| 67 | RcvShipmentHeadersPEORmaBuId | RMA_BU_ID | — | — |
| 68 | RcvShipmentHeadersPEOShipFromLocationId | SHIP_FROM_LOCATION_ID | — | — |
| 69 | RcvShipmentHeadersPEOShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 70 | RcvShipmentHeadersPEOShipToOrgId | SHIP_TO_ORG_ID | — | — |
| 71 | RcvShipmentHeadersPEOShipmentHeaderId | SHIPMENT_HEADER_ID | — | — |
| 72 | RcvShipmentHeadersPEOShipmentNum | SHIPMENT_NUM | — | ✅ |
| 73 | RcvShipmentHeadersPEOShippedDate | SHIPPED_DATE | — | ✅ |
| 74 | RcvShipmentHeadersPEOSpecialHandlingCode | SPECIAL_HANDLING_CODE | — | — |
| 75 | RcvShipmentHeadersPEOTarWeight | TAR_WEIGHT | — | — |
| 76 | RcvShipmentHeadersPEOTarWeightUomCode | TAR_WEIGHT_UOM_CODE | — | — |
| 77 | RcvShipmentHeadersPEOTaxAmount | TAX_AMOUNT | — | — |
| 78 | RcvShipmentHeadersPEOTaxName | TAX_NAME | — | — |
| 79 | RcvShipmentHeadersPEOVendorId | VENDOR_ID | — | — |
| 80 | RcvShipmentHeadersPEOVendorSiteId | VENDOR_SITE_ID | — | — |
| 81 | RcvShipmentHeadersPEOWaybillAirbillNum | WAYBILL_AIRBILL_NUM | — | ✅ |

### [[rcv_shipment_lines|RCV_SHIPMENT_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RcvShipmentLinesPEOAmount | AMOUNT | — | — |
| 2 | RcvShipmentLinesPEOAmountReceived | AMOUNT_RECEIVED | — | — |
| 3 | RcvShipmentLinesPEOAmountShipped | AMOUNT_SHIPPED | — | — |
| 4 | RcvShipmentLinesPEOApprovalStatus | APPROVAL_STATUS | — | — |
| 5 | RcvShipmentLinesPEOAsnLineFlag | ASN_LINE_FLAG | — | ✅ |
| 6 | RcvShipmentLinesPEOAsnLpnId | ASN_LPN_ID | — | — |
| 7 | RcvShipmentLinesPEOAssessableValue | ASSESSABLE_VALUE | — | — |
| 8 | RcvShipmentLinesPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 9 | RcvShipmentLinesPEOBarCodeLabel | BAR_CODE_LABEL | — | ✅ |
| 10 | RcvShipmentLinesPEOCategoryId | CATEGORY_ID | — | — |
| 11 | RcvShipmentLinesPEOComments | COMMENTS | — | ✅ |
| 12 | RcvShipmentLinesPEOConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 13 | RcvShipmentLinesPEOConsumedQuantity | CONSUMED_QUANTITY | — | ✅ |
| 14 | RcvShipmentLinesPEOContainerNum | CONTAINER_NUM | — | — |
| 15 | RcvShipmentLinesPEOCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | — |
| 16 | RcvShipmentLinesPEOCreatedBy | CREATED_BY | — | — |
| 17 | RcvShipmentLinesPEOCreationDate | CREATION_DATE | — | ✅ |
| 18 | RcvShipmentLinesPEOCumComparisonFlag | CUM_COMPARISON_FLAG | — | — |
| 19 | RcvShipmentLinesPEOCustomerId | CUSTOMER_ID | — | — |
| 20 | RcvShipmentLinesPEOCustomerItemNum | CUSTOMER_ITEM_NUM | — | — |
| 21 | RcvShipmentLinesPEOCustomerSiteId | CUSTOMER_SITE_ID | — | — |
| 22 | RcvShipmentLinesPEODefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 23 | RcvShipmentLinesPEODeliverToLocationId | DELIVER_TO_LOCATION_ID | — | — |
| 24 | RcvShipmentLinesPEODeliverToPersonId | DELIVER_TO_PERSON_ID | — | — |
| 25 | RcvShipmentLinesPEODestinationContext | DESTINATION_CONTEXT | — | — |
| 26 | RcvShipmentLinesPEODestinationTypeCode | DESTINATION_TYPE_CODE | — | — |
| 27 | RcvShipmentLinesPEODocumentFiscalClassification | DOCUMENT_FISCAL_CLASSIFICATION | — | — |
| 28 | RcvShipmentLinesPEOEmployeeId | EMPLOYEE_ID | — | — |
| 29 | RcvShipmentLinesPEOExcessTransportAuthNum | EXCESS_TRANSPORT_AUTH_NUM | — | — |
| 30 | RcvShipmentLinesPEOExcessTransportReason | EXCESS_TRANSPORT_REASON | — | — |
| 31 | RcvShipmentLinesPEOExcessTransportResponsible | EXCESS_TRANSPORT_RESPONSIBLE | — | — |
| 32 | RcvShipmentLinesPEOFinalDischargeLocationId | FINAL_DISCHARGE_LOCATION_ID | — | — |
| 33 | RcvShipmentLinesPEOFirstPtyRegId | FIRST_PTY_REG_ID | — | — |
| 34 | RcvShipmentLinesPEOFromOrganizationId | FROM_ORGANIZATION_ID | — | — |
| 35 | RcvShipmentLinesPEOGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 36 | RcvShipmentLinesPEOInvoiceStatusCode | INVOICE_STATUS_CODE | — | — |
| 37 | RcvShipmentLinesPEOItemDescription | ITEM_DESCRIPTION | — | — |
| 38 | RcvShipmentLinesPEOItemId | ITEM_ID | — | — |
| 39 | RcvShipmentLinesPEOItemRevision | ITEM_REVISION | — | — |
| 40 | RcvShipmentLinesPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 41 | RcvShipmentLinesPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 42 | RcvShipmentLinesPEOJobId | JOB_ID | — | — |
| 43 | RcvShipmentLinesPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 44 | RcvShipmentLinesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 45 | RcvShipmentLinesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 46 | RcvShipmentLinesPEOLineNum | LINE_NUM | — | ✅ |
| 47 | RcvShipmentLinesPEOLocatorId | LOCATOR_ID | — | — |
| 48 | RcvShipmentLinesPEOMaterialStoredAmount | MATERIAL_STORED_AMOUNT | — | — |
| 49 | RcvShipmentLinesPEOMmtTransactionId | MMT_TRANSACTION_ID | — | — |
| 50 | RcvShipmentLinesPEONoticeUnitPrice | NOTICE_UNIT_PRICE | — | — |
| 51 | RcvShipmentLinesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 52 | RcvShipmentLinesPEOOriginalAsnLineFlag | ORIGINAL_ASN_LINE_FLAG | — | — |
| 53 | RcvShipmentLinesPEOOriginalAsnParentLineId | ORIGINAL_ASN_PARENT_LINE_ID | — | — |
| 54 | RcvShipmentLinesPEOOsaFlag | OSA_FLAG | — | — |
| 55 | RcvShipmentLinesPEOPackingSlip | PACKING_SLIP | — | ✅ |
| 56 | RcvShipmentLinesPEOPoDistributionId | PO_DISTRIBUTION_ID | — | ✅ |
| 57 | RcvShipmentLinesPEOPoHeaderId | PO_HEADER_ID | — | ✅ |
| 58 | RcvShipmentLinesPEOPoLineId | PO_LINE_ID | — | ✅ |
| 59 | RcvShipmentLinesPEOPoLineLocationId | PO_LINE_LOCATION_ID | — | ✅ |
| 60 | RcvShipmentLinesPEOPrimaryUomCode | PRIMARY_UOM_CODE | — | — |
| 61 | RcvShipmentLinesPEOProductCategory | PRODUCT_CATEGORY | — | — |
| 62 | RcvShipmentLinesPEOProductType | PRODUCT_TYPE | — | — |
| 63 | RcvShipmentLinesPEOProjectId | PROJECT_ID | — | — |
| 64 | RcvShipmentLinesPEOQcGrade | QC_GRADE | — | — |
| 65 | RcvShipmentLinesPEOQuantityAccepted | QUANTITY_ACCEPTED | — | — |
| 66 | RcvShipmentLinesPEOQuantityDelivered | QUANTITY_DELIVERED | — | — |
| 67 | RcvShipmentLinesPEOQuantityReceived | QUANTITY_RECEIVED | — | — |
| 68 | RcvShipmentLinesPEOQuantityRejected | QUANTITY_REJECTED | — | — |
| 69 | RcvShipmentLinesPEOQuantityReturned | QUANTITY_RETURNED | — | — |
| 70 | RcvShipmentLinesPEOQuantityShipped | QUANTITY_SHIPPED | — | ✅ |
| 71 | RcvShipmentLinesPEORaAllowSubstituteReceipt | RA_ALLOW_SUBSTITUTE_RECEIPT | — | — |
| 72 | RcvShipmentLinesPEORaDaysEarlyReceiptAllowed | RA_DAYS_EARLY_RECEIPT_ALLOWED | — | — |
| 73 | RcvShipmentLinesPEORaDaysLateReceiptAllowed | RA_DAYS_LATE_RECEIPT_ALLOWED | — | — |
| 74 | RcvShipmentLinesPEORaDocLineCreationDate | RA_DOC_LINE_CREATION_DATE | — | — |
| 75 | RcvShipmentLinesPEORaDocLineLastUpdateDate | RA_DOC_LINE_LAST_UPDATE_DATE | — | — |
| 76 | RcvShipmentLinesPEORaDocScheduleNumber | RA_DOC_SCHEDULE_NUMBER | — | — |
| 77 | RcvShipmentLinesPEORaDocumentLineNumber | RA_DOCUMENT_LINE_NUMBER | — | — |
| 78 | RcvShipmentLinesPEORaDooFulfillmentLineNumber | RA_DOO_FULFILLMENT_LINE_NUMBER | — | — |
| 79 | RcvShipmentLinesPEORaDooHeaderNumber | RA_DOO_HEADER_NUMBER | — | — |
| 80 | RcvShipmentLinesPEORaDooLineNumber | RA_DOO_LINE_NUMBER | — | — |
| 81 | RcvShipmentLinesPEORaEnforceShipToLocCode | RA_ENFORCE_SHIP_TO_LOC_CODE | — | — |
| 82 | RcvShipmentLinesPEORaExpectedReceiptDate | RA_EXPECTED_RECEIPT_DATE | — | ✅ |
| 83 | RcvShipmentLinesPEORaLastActionCode | RA_LAST_ACTION_CODE | — | — |
| 84 | RcvShipmentLinesPEORaNoteToReceiver | RA_NOTE_TO_RECEIVER | — | ✅ |
| 85 | RcvShipmentLinesPEORaOrigDooFulfilLineNum | RA_ORIG_DOO_FULFIL_LINE_NUM | — | — |
| 86 | RcvShipmentLinesPEORaOrigDooHeaderNumber | RA_ORIG_DOO_HEADER_NUMBER | — | — |
| 87 | RcvShipmentLinesPEORaOrigDooLineNumber | RA_ORIG_DOO_LINE_NUMBER | — | — |
| 88 | RcvShipmentLinesPEORaOrigOcHeaderNumber | RA_ORIG_OC_HEADER_NUMBER | — | — |
| 89 | RcvShipmentLinesPEORaOrigOcLineNumber | RA_ORIG_OC_LINE_NUMBER | — | — |
| 90 | RcvShipmentLinesPEORaQtyRcvExceptionCode | RA_QTY_RCV_EXCEPTION_CODE | — | — |
| 91 | RcvShipmentLinesPEORaQtyRcvTolerance | RA_QTY_RCV_TOLERANCE | — | — |
| 92 | RcvShipmentLinesPEORaQuantityExpected | RA_QUANTITY_EXPECTED | — | — |
| 93 | RcvShipmentLinesPEORaReceiptDaysExceptionCode | RA_RECEIPT_DAYS_EXCEPTION_CODE | — | — |
| 94 | RcvShipmentLinesPEORaSecondaryQuantityExpected | RA_SECONDARY_QUANTITY_EXPECTED | — | — |
| 95 | RcvShipmentLinesPEORaUnitPrice | RA_UNIT_PRICE | — | — |
| 96 | RcvShipmentLinesPEOReasonId | REASON_ID | — | — |
| 97 | RcvShipmentLinesPEOReceiptAdviceHeaderId | RECEIPT_ADVICE_HEADER_ID | — | — |
| 98 | RcvShipmentLinesPEOReceiptAdviceLineId | RECEIPT_ADVICE_LINE_ID | — | — |
| 99 | RcvShipmentLinesPEOReceiptAdviceLineNumber | RECEIPT_ADVICE_LINE_NUMBER | — | — |
| 100 | RcvShipmentLinesPEOReqDistributionId | REQ_DISTRIBUTION_ID | — | — |
| 101 | RcvShipmentLinesPEORequestId | REQUEST_ID | — | — |
| 102 | RcvShipmentLinesPEORequestedAmount | REQUESTED_AMOUNT | — | — |
| 103 | RcvShipmentLinesPEORequisitionLineId | REQUISITION_LINE_ID | — | — |
| 104 | RcvShipmentLinesPEORoutingHeaderId | ROUTING_HEADER_ID | — | — |
| 105 | RcvShipmentLinesPEOSecondaryQuantityReceived | SECONDARY_QUANTITY_RECEIVED | — | — |
| 106 | RcvShipmentLinesPEOSecondaryQuantityShipped | SECONDARY_QUANTITY_SHIPPED | — | — |
| 107 | RcvShipmentLinesPEOSecondaryUomCode | SECONDARY_UOM_CODE | — | — |
| 108 | RcvShipmentLinesPEOShipFromLocationId | SHIP_FROM_LOCATION_ID | — | — |
| 109 | RcvShipmentLinesPEOShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 110 | RcvShipmentLinesPEOShipmentHeaderId | SHIPMENT_HEADER_ID | — | ✅ |
| 111 | RcvShipmentLinesPEOShipmentLineStatusCode | SHIPMENT_LINE_STATUS_CODE | — | ✅ |
| 112 | RcvShipmentLinesPEOShipmentUnitPrice | SHIPMENT_UNIT_PRICE | — | — |
| 113 | RcvShipmentLinesPEOSourceDocumentCode | SOURCE_DOCUMENT_CODE | — | — |
| 114 | RcvShipmentLinesPEOSpGroupId | SP_GROUP_ID | — | — |
| 115 | RcvShipmentLinesPEOSpQuantity | SP_QUANTITY | — | — |
| 116 | RcvShipmentLinesPEOSpUomCode | SP_UOM_CODE | — | — |
| 117 | RcvShipmentLinesPEOTaskId | TASK_ID | — | — |
| 118 | RcvShipmentLinesPEOTaxAmount | TAX_AMOUNT | — | — |
| 119 | RcvShipmentLinesPEOTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 120 | RcvShipmentLinesPEOTaxName | TAX_NAME | — | — |
| 121 | RcvShipmentLinesPEOThirdPtyRegId | THIRD_PTY_REG_ID | — | — |
| 122 | RcvShipmentLinesPEOTimecardId | TIMECARD_ID | — | — |
| 123 | RcvShipmentLinesPEOTimecardOvn | TIMECARD_OVN | — | — |
| 124 | RcvShipmentLinesPEOToOrganizationId | TO_ORGANIZATION_ID | — | — |
| 125 | RcvShipmentLinesPEOToSubinventory | TO_SUBINVENTORY | — | — |
| 126 | RcvShipmentLinesPEOTransferCost | TRANSFER_COST | — | — |
| 127 | RcvShipmentLinesPEOTransferPercentage | TRANSFER_PERCENTAGE | — | — |
| 128 | RcvShipmentLinesPEOTransportationCost | TRANSPORTATION_COST | — | — |
| 129 | RcvShipmentLinesPEOTruckNum | TRUCK_NUM | — | — |
| 130 | RcvShipmentLinesPEOTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 131 | RcvShipmentLinesPEOUomCode | UOM_CODE | — | ✅ |
| 132 | RcvShipmentLinesPEOUomConversionRate | UOM_CONVERSION_RATE | — | — |
| 133 | RcvShipmentLinesPEOUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 134 | RcvShipmentLinesPEOVendorCumShippedQuantity | VENDOR_CUM_SHIPPED_QUANTITY | — | — |
| 135 | RcvShipmentLinesPEOVendorItemNum | VENDOR_ITEM_NUM | — | — |
| 136 | RcvShipmentLinesPEOVendorLotNum | VENDOR_LOT_NUM | — | — |
| 137 | ShipmentLineId | SHIPMENT_LINE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
