---
id: DOC-AR-PVO-ReceivingReceiptsPVO
doc_type: system-doc
title: "ReceivingReceiptsPVO — PVO Accounts Receivable"
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
  - ReceivingReceiptsPVO
  - receivingreceiptspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReceivingReceiptsPVO

## 📌 Visão Geral

Extrai os recebimentos de materiais/serviços vinculados a ordens de compra, com dados de remessa, fornecedor e categoria. Permite acompanhar o fluxo de recebimento físico para matching com faturas e controle de accruals.

**Caminho:** `FscmTopModelAM.RcvReceiptsAM.ReceivingReceiptsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 614 | 8 | 2 | 39 | 6% |

---

## 🔗 Tabelas Relacionadas

- [[egp_categories_vl|EGP_CATEGORIES_VL]] — 10 atributos
- [[inv_org_parameters_v|INV_ORG_PARAMETERS_V]] — 1 atributos (1 PKs, 1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 16 atributos
- [[po_headers_all|PO_HEADERS_ALL]] — 115 atributos
- [[po_lines_all|PO_LINES_ALL]] — 108 atributos (2 BICC)
- [[po_line_locations_all|PO_LINE_LOCATIONS_ALL]] — 144 atributos (2 BICC)
- [[rcv_shipment_headers|RCV_SHIPMENT_HEADERS]] — 81 atributos (15 BICC)
- [[rcv_shipment_lines|RCV_SHIPMENT_LINES]] — 139 atributos (1 PKs, 19 BICC)

---

## ⚙️ Atributos

### [[egp_categories_vl|EGP_CATEGORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryPEOCategoryCode | CATEGORY_CODE | — | — |
| 2 | CategoryPEOCategoryContentCode | CATEGORY_CONTENT_CODE | — | — |
| 3 | CategoryPEOCategoryId | CATEGORY_ID | — | — |
| 4 | CategoryPEOCategoryName | CATEGORY_NAME | — | — |
| 5 | CategoryPEOCreatedBy | CREATED_BY | — | — |
| 6 | CategoryPEOCreationDate | CREATION_DATE | — | — |
| 7 | CategoryPEODescription | DESCRIPTION | — | — |
| 8 | CategoryPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 9 | CategoryPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | CategoryPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[inv_org_parameters_v|INV_ORG_PARAMETERS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNamePEORSHCrtByDisplayName | DISPLAY_NAME | — | — |
| 2 | PersonNamePEORSHCrtByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonNamePEORSHCrtByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PersonNamePEORSHCrtByPersonNameId | PERSON_NAME_ID | — | — |
| 5 | PersonNamePEORSHLUpdByDisplayName | DISPLAY_NAME | — | — |
| 6 | PersonNamePEORSHLUpdByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | PersonNamePEORSHLUpdByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 8 | PersonNamePEORSHLUpdByPersonNameId | PERSON_NAME_ID | — | — |
| 9 | PersonNamePEORSLCrtByDisplayName | DISPLAY_NAME | — | — |
| 10 | PersonNamePEORSLCrtByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 11 | PersonNamePEORSLCrtByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 12 | PersonNamePEORSLCrtByPersonNameId | PERSON_NAME_ID | — | — |
| 13 | PersonNamePEORSLLUpdByDisplayName | DISPLAY_NAME | — | — |
| 14 | PersonNamePEORSLLUpdByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 15 | PersonNamePEORSLLUpdByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 16 | PersonNamePEORSLLUpdByPersonNameId | PERSON_NAME_ID | — | — |

### [[po_headers_all|PO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PoHeadersAllPEOAcceptanceDueDate | ACCEPTANCE_DUE_DATE | — | — |
| 2 | PoHeadersAllPEOAcceptanceRequiredFlag | ACCEPTANCE_REQUIRED_FLAG | — | — |
| 3 | PoHeadersAllPEOAcceptanceWithinDays | ACCEPTANCE_WITHIN_DAYS | — | — |
| 4 | PoHeadersAllPEOAgentId | AGENT_ID | — | — |
| 5 | PoHeadersAllPEOAmountLimit | AMOUNT_LIMIT | — | — |
| 6 | PoHeadersAllPEOAmountReleased | AMOUNT_RELEASED | — | — |
| 7 | PoHeadersAllPEOApprovedDate | APPROVED_DATE | — | — |
| 8 | PoHeadersAllPEOApprovedFlag | APPROVED_FLAG | — | — |
| 9 | PoHeadersAllPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 10 | PoHeadersAllPEOAutoSourcingFlag | AUTO_SOURCING_FLAG | — | — |
| 11 | PoHeadersAllPEOBillToLocationId | BILL_TO_LOCATION_ID | — | — |
| 12 | PoHeadersAllPEOBilltoBuId | BILLTO_BU_ID | — | — |
| 13 | PoHeadersAllPEOBlanketTotalAmount | BLANKET_TOTAL_AMOUNT | — | — |
| 14 | PoHeadersAllPEOCancelFlag | CANCEL_FLAG | — | — |
| 15 | PoHeadersAllPEOCarrierId | CARRIER_ID | — | — |
| 16 | PoHeadersAllPEOCatAdminAuthEnabledFlag | CAT_ADMIN_AUTH_ENABLED_FLAG | — | — |
| 17 | PoHeadersAllPEOCbcAccountingDate | CBC_ACCOUNTING_DATE | — | — |
| 18 | PoHeadersAllPEOChangeRequestedBy | CHANGE_REQUESTED_BY | — | — |
| 19 | PoHeadersAllPEOChangeSummary | CHANGE_SUMMARY | — | — |
| 20 | PoHeadersAllPEOClosedDate | CLOSED_DATE | — | — |
| 21 | PoHeadersAllPEOComments | COMMENTS | — | — |
| 22 | PoHeadersAllPEOConfirmingOrderFlag | CONFIRMING_ORDER_FLAG | — | — |
| 23 | PoHeadersAllPEOConsignedConsumptionFlag | CONSIGNED_CONSUMPTION_FLAG | — | — |
| 24 | PoHeadersAllPEOConsumeReqDemandFlag | CONSUME_REQ_DEMAND_FLAG | — | — |
| 25 | PoHeadersAllPEOContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 26 | PoHeadersAllPEOContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 27 | PoHeadersAllPEOContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 28 | PoHeadersAllPEOCpaReference | CPA_REFERENCE | — | — |
| 29 | PoHeadersAllPEOCreatedBy | CREATED_BY | — | — |
| 30 | PoHeadersAllPEOCreatedLanguage | CREATED_LANGUAGE | — | — |
| 31 | PoHeadersAllPEOCreationDate | CREATION_DATE | — | — |
| 32 | PoHeadersAllPEOCurrencyCode | CURRENCY_CODE | — | — |
| 33 | PoHeadersAllPEOCurrentVersionId | CURRENT_VERSION_ID | — | — |
| 34 | PoHeadersAllPEODefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 35 | PoHeadersAllPEODocumentCreationMethod | DOCUMENT_CREATION_METHOD | — | — |
| 36 | PoHeadersAllPEODocumentStatus | DOCUMENT_STATUS | — | — |
| 37 | PoHeadersAllPEOEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 38 | PoHeadersAllPEOEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 39 | PoHeadersAllPEOEmailAddress | EMAIL_ADDRESS | — | — |
| 40 | PoHeadersAllPEOEnabledFlag | ENABLED_FLAG | — | — |
| 41 | PoHeadersAllPEOEncumbranceRequiredFlag | ENCUMBRANCE_REQUIRED_FLAG | — | — |
| 42 | PoHeadersAllPEOEndDate | END_DATE | — | — |
| 43 | PoHeadersAllPEOFax | FAX | — | — |
| 44 | PoHeadersAllPEOFirmDate | FIRM_DATE | — | — |
| 45 | PoHeadersAllPEOFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 46 | PoHeadersAllPEOFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 47 | PoHeadersAllPEOFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 48 | PoHeadersAllPEOFromHeaderId | FROM_HEADER_ID | — | — |
| 49 | PoHeadersAllPEOFromTypeLookupCode | FROM_TYPE_LOOKUP_CODE | — | — |
| 50 | PoHeadersAllPEOFrozenFlag | FROZEN_FLAG | — | — |
| 51 | PoHeadersAllPEOGenerateOrdersAutomatic | GENERATE_ORDERS_AUTOMATIC | — | — |
| 52 | PoHeadersAllPEOGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 53 | PoHeadersAllPEOGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 54 | PoHeadersAllPEOGroupRequisitionLines | GROUP_REQUISITION_LINES | — | — |
| 55 | PoHeadersAllPEOGroupRequisitions | GROUP_REQUISITIONS | — | — |
| 56 | PoHeadersAllPEOInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 57 | PoHeadersAllPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 58 | PoHeadersAllPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 59 | PoHeadersAllPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 60 | PoHeadersAllPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 61 | PoHeadersAllPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 62 | PoHeadersAllPEOLastUpdatedProgram | LAST_UPDATED_PROGRAM | — | — |
| 63 | PoHeadersAllPEOMinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 64 | PoHeadersAllPEONoteToAuthorizer | NOTE_TO_AUTHORIZER | — | — |
| 65 | PoHeadersAllPEONoteToReceiver | NOTE_TO_RECEIVER | — | — |
| 66 | PoHeadersAllPEONoteToVendor | NOTE_TO_VENDOR | — | — |
| 67 | PoHeadersAllPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 68 | PoHeadersAllPEOPayOnCode | PAY_ON_CODE | — | — |
| 69 | PoHeadersAllPEOPcardId | PCARD_ID | — | — |
| 70 | PoHeadersAllPEOPendingSignatureFlag | PENDING_SIGNATURE_FLAG | — | — |
| 71 | PoHeadersAllPEOPoHeaderId | PO_HEADER_ID | — | — |
| 72 | PoHeadersAllPEOPrcBuId | PRC_BU_ID | — | — |
| 73 | PoHeadersAllPEOPriceUpdateTolerance | PRICE_UPDATE_TOLERANCE | — | — |
| 74 | PoHeadersAllPEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 75 | PoHeadersAllPEOProgramName | PROGRAM_NAME | — | — |
| 76 | PoHeadersAllPEORate | RATE | — | — |
| 77 | PoHeadersAllPEORateDate | RATE_DATE | — | — |
| 78 | PoHeadersAllPEORateType | RATE_TYPE | — | — |
| 79 | PoHeadersAllPEOReferenceNum | REFERENCE_NUM | — | — |
| 80 | PoHeadersAllPEOReleaseMethod | RELEASE_METHOD | — | — |
| 81 | PoHeadersAllPEOReqBuId | REQ_BU_ID | — | — |
| 82 | PoHeadersAllPEORequestId | REQUEST_ID | — | — |
| 83 | PoHeadersAllPEORetroPriceApplyUpdatesFlag | RETRO_PRICE_APPLY_UPDATES_FLAG | — | — |
| 84 | PoHeadersAllPEORetroPriceCommUpdatesFlag | RETRO_PRICE_COMM_UPDATES_FLAG | — | — |
| 85 | PoHeadersAllPEOReviewAutogeneratedReleases | REVIEW_AUTOGENERATED_RELEASES | — | — |
| 86 | PoHeadersAllPEORevisedDate | REVISED_DATE | — | — |
| 87 | PoHeadersAllPEORevisionNum | REVISION_NUM | — | — |
| 88 | PoHeadersAllPEOSegment1 | SEGMENT1 | — | — |
| 89 | PoHeadersAllPEOSegment2 | SEGMENT2 | — | — |
| 90 | PoHeadersAllPEOSegment3 | SEGMENT3 | — | — |
| 91 | PoHeadersAllPEOSegment4 | SEGMENT4 | — | — |
| 92 | PoHeadersAllPEOSegment5 | SEGMENT5 | — | — |
| 93 | PoHeadersAllPEOShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 94 | PoHeadersAllPEOShippingControl | SHIPPING_CONTROL | — | — |
| 95 | PoHeadersAllPEOSoldtoLeId | SOLDTO_LE_ID | — | — |
| 96 | PoHeadersAllPEOStartDate | START_DATE | — | — |
| 97 | PoHeadersAllPEOStyleId | STYLE_ID | — | — |
| 98 | PoHeadersAllPEOSubmitApprovalAutomatic | SUBMIT_APPROVAL_AUTOMATIC | — | — |
| 99 | PoHeadersAllPEOSubmitDate | SUBMIT_DATE | — | — |
| 100 | PoHeadersAllPEOSummaryFlag | SUMMARY_FLAG | — | — |
| 101 | PoHeadersAllPEOSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | — |
| 102 | PoHeadersAllPEOTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 103 | PoHeadersAllPEOTaxDocumentSubtype | TAX_DOCUMENT_SUBTYPE | — | — |
| 104 | PoHeadersAllPEOTermsId | TERMS_ID | — | — |
| 105 | PoHeadersAllPEOTypeLookupCode | TYPE_LOOKUP_CODE | — | — |
| 106 | PoHeadersAllPEOUpdateSourcingRulesFlag | UPDATE_SOURCING_RULES_FLAG | — | — |
| 107 | PoHeadersAllPEOUseNeedByDate | USE_NEED_BY_DATE | — | — |
| 108 | PoHeadersAllPEOUseShipTo | USE_SHIP_TO | — | — |
| 109 | PoHeadersAllPEOVendorContactId | VENDOR_CONTACT_ID | — | — |
| 110 | PoHeadersAllPEOVendorId | VENDOR_ID | — | — |
| 111 | PoHeadersAllPEOVendorOrderNum | VENDOR_ORDER_NUM | — | — |
| 112 | PoHeadersAllPEOVendorSiteId | VENDOR_SITE_ID | — | — |
| 113 | PoHeadersAllPEOXmlChangeSendDate | XML_CHANGE_SEND_DATE | — | — |
| 114 | PoHeadersAllPEOXmlFlag | XML_FLAG | — | — |
| 115 | PoHeadersAllPEOXmlSendDate | XML_SEND_DATE | — | — |

### [[po_lines_all|PO_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PoLinesAllPEOAllowDescriptionUpdateFlag | ALLOW_DESCRIPTION_UPDATE_FLAG | — | — |
| 2 | PoLinesAllPEOAllowPriceOverrideFlag | ALLOW_PRICE_OVERRIDE_FLAG | — | — |
| 3 | PoLinesAllPEOAmount | AMOUNT | — | — |
| 4 | PoLinesAllPEOAmountReleased | AMOUNT_RELEASED | — | — |
| 5 | PoLinesAllPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 6 | PoLinesAllPEOAuctionDisplayNumber | AUCTION_DISPLAY_NUMBER | — | — |
| 7 | PoLinesAllPEOAuctionHeaderId | AUCTION_HEADER_ID | — | — |
| 8 | PoLinesAllPEOAuctionLineNumber | AUCTION_LINE_NUMBER | — | — |
| 9 | PoLinesAllPEOBaseQty | BASE_QTY | — | — |
| 10 | PoLinesAllPEOBaseUnitPrice | BASE_UNIT_PRICE | — | — |
| 11 | PoLinesAllPEOBaseUom | BASE_UOM | — | — |
| 12 | PoLinesAllPEOBidLineNumber | BID_LINE_NUMBER | — | — |
| 13 | PoLinesAllPEOBidNumber | BID_NUMBER | — | — |
| 14 | PoLinesAllPEOCancelDate | CANCEL_DATE | — | — |
| 15 | PoLinesAllPEOCancelFlag | CANCEL_FLAG | — | — |
| 16 | PoLinesAllPEOCancelReason | CANCEL_REASON | — | — |
| 17 | PoLinesAllPEOCancelledBy | CANCELLED_BY | — | — |
| 18 | PoLinesAllPEOCapitalExpenseFlag | CAPITAL_EXPENSE_FLAG | — | — |
| 19 | PoLinesAllPEOCategoryId | CATEGORY_ID | — | — |
| 20 | PoLinesAllPEOClosedBy | CLOSED_BY | — | — |
| 21 | PoLinesAllPEOClosedDate | CLOSED_DATE | — | — |
| 22 | PoLinesAllPEOClosedReason | CLOSED_REASON | — | — |
| 23 | PoLinesAllPEOCommittedAmount | COMMITTED_AMOUNT | — | — |
| 24 | PoLinesAllPEOContractId | CONTRACT_ID | — | — |
| 25 | PoLinesAllPEOContractorFirstName | CONTRACTOR_FIRST_NAME | — | — |
| 26 | PoLinesAllPEOContractorLastName | CONTRACTOR_LAST_NAME | — | — |
| 27 | PoLinesAllPEOCreatedBy | CREATED_BY | — | — |
| 28 | PoLinesAllPEOCreationDate | CREATION_DATE | — | — |
| 29 | PoLinesAllPEOExpirationDate | EXPIRATION_DATE | — | — |
| 30 | PoLinesAllPEOFirmDate | FIRM_DATE | — | — |
| 31 | PoLinesAllPEOFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 32 | PoLinesAllPEOFromHeaderId | FROM_HEADER_ID | — | — |
| 33 | PoLinesAllPEOFromLineId | FROM_LINE_ID | — | — |
| 34 | PoLinesAllPEOFromLineLocationId | FROM_LINE_LOCATION_ID | — | — |
| 35 | PoLinesAllPEOGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 36 | PoLinesAllPEOGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 37 | PoLinesAllPEOHazardClassId | HAZARD_CLASS_ID | — | — |
| 38 | PoLinesAllPEOItemDescription | ITEM_DESCRIPTION | — | — |
| 39 | PoLinesAllPEOItemId | ITEM_ID | — | — |
| 40 | PoLinesAllPEOItemRevision | ITEM_REVISION | — | — |
| 41 | PoLinesAllPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 42 | PoLinesAllPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 43 | PoLinesAllPEOJobId | JOB_ID | — | — |
| 44 | PoLinesAllPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 45 | PoLinesAllPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 46 | PoLinesAllPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 47 | PoLinesAllPEOLastUpdatedProgram | LAST_UPDATED_PROGRAM | — | — |
| 48 | PoLinesAllPEOLineNum | LINE_NUM | — | — |
| 49 | PoLinesAllPEOLineReferenceNum | LINE_REFERENCE_NUM | — | — |
| 50 | PoLinesAllPEOLineStatus | LINE_STATUS | — | — |
| 51 | PoLinesAllPEOLineTypeId | LINE_TYPE_ID | — | — |
| 52 | PoLinesAllPEOListPricePerUnit | LIST_PRICE_PER_UNIT | — | — |
| 53 | PoLinesAllPEOManualPriceChangeFlag | MANUAL_PRICE_CHANGE_FLAG | — | — |
| 54 | PoLinesAllPEOManufacturer | MANUFACTURER | — | — |
| 55 | PoLinesAllPEOManufacturerPartNum | MANUFACTURER_PART_NUM | — | — |
| 56 | PoLinesAllPEOMarketPrice | MARKET_PRICE | — | — |
| 57 | PoLinesAllPEOMatchingBasis | MATCHING_BASIS | — | — |
| 58 | PoLinesAllPEOMaxRetainageAmount | MAX_RETAINAGE_AMOUNT | — | — |
| 59 | PoLinesAllPEOMinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 60 | PoLinesAllPEONegotiatedByPreparerFlag | NEGOTIATED_BY_PREPARER_FLAG | — | — |
| 61 | PoLinesAllPEONotToExceedPrice | NOT_TO_EXCEED_PRICE | — | — |
| 62 | PoLinesAllPEONoteToVendor | NOTE_TO_VENDOR | — | — |
| 63 | PoLinesAllPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 64 | PoLinesAllPEOOkeContractHeaderId | OKE_CONTRACT_HEADER_ID | — | — |
| 65 | PoLinesAllPEOOkeContractVersionId | OKE_CONTRACT_VERSION_ID | — | — |
| 66 | PoLinesAllPEOOrderTypeLookupCode | ORDER_TYPE_LOOKUP_CODE | — | — |
| 67 | PoLinesAllPEOOverToleranceErrorFlag | OVER_TOLERANCE_ERROR_FLAG | — | — |
| 68 | PoLinesAllPEOPJC_CONTEXT_CATEGORY | PJC_CONTEXT_CATEGORY | — | — |
| 69 | PoLinesAllPEOPoHeaderId | PO_HEADER_ID | — | — |
| 70 | PoLinesAllPEOPoLineId | PO_LINE_ID | — | — |
| 71 | PoLinesAllPEOPrcBuId | PRC_BU_ID | — | — |
| 72 | PoLinesAllPEOPreferredGrade | PREFERRED_GRADE | — | — |
| 73 | PoLinesAllPEOPriceBreakLookupCode | PRICE_BREAK_LOOKUP_CODE | — | — |
| 74 | PoLinesAllPEOPriceTypeLookupCode | PRICE_TYPE_LOOKUP_CODE | — | — |
| 75 | PoLinesAllPEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 76 | PoLinesAllPEOProgramName | PROGRAM_NAME | — | — |
| 77 | PoLinesAllPEOProgressPaymentRate | PROGRESS_PAYMENT_RATE | — | — |
| 78 | PoLinesAllPEOPurchaseBasis | PURCHASE_BASIS | — | — |
| 79 | PoLinesAllPEOQcGrade | QC_GRADE | — | — |
| 80 | PoLinesAllPEOQtyRcvTolerance | QTY_RCV_TOLERANCE | — | — |
| 81 | PoLinesAllPEOQuantity | QUANTITY | — | — |
| 82 | PoLinesAllPEOQuantityCommitted | QUANTITY_COMMITTED | — | — |
| 83 | PoLinesAllPEORecoupmentRate | RECOUPMENT_RATE | — | — |
| 84 | PoLinesAllPEOReferenceNum | REFERENCE_NUM | — | — |
| 85 | PoLinesAllPEOReqBuId | REQ_BU_ID | — | — |
| 86 | PoLinesAllPEORequestId | REQUEST_ID | — | — |
| 87 | PoLinesAllPEORetainageRate | RETAINAGE_RATE | — | — |
| 88 | PoLinesAllPEORetroactiveDate | RETROACTIVE_DATE | — | — |
| 89 | PoLinesAllPEOSecondaryQuantity | SECONDARY_QUANTITY | — | — |
| 90 | PoLinesAllPEOSecondaryUomCode | SECONDARY_UOM_CODE | — | — |
| 91 | PoLinesAllPEOShippingUomCode | SHIPPING_UOM_CODE | — | ✅ |
| 92 | PoLinesAllPEOShippingUomQuantity | SHIPPING_UOM_QUANTITY | — | ✅ |
| 93 | PoLinesAllPEOSourceDocRevNum | SOURCE_DOC_REV_NUM | — | — |
| 94 | PoLinesAllPEOStartDate | START_DATE | — | — |
| 95 | PoLinesAllPEOSupplierPartAuxid | SUPPLIER_PART_AUXID | — | — |
| 96 | PoLinesAllPEOSupplierRefNumber | SUPPLIER_REF_NUMBER | — | — |
| 97 | PoLinesAllPEOSvcAmountNotifSent | SVC_AMOUNT_NOTIF_SENT | — | — |
| 98 | PoLinesAllPEOSvcCompletionNotifSent | SVC_COMPLETION_NOTIF_SENT | — | — |
| 99 | PoLinesAllPEOTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 100 | PoLinesAllPEOTaxCodeId | TAX_CODE_ID | — | — |
| 101 | PoLinesAllPEOTaxName | TAX_NAME | — | — |
| 102 | PoLinesAllPEOTaxableFlag | TAXABLE_FLAG | — | — |
| 103 | PoLinesAllPEOType1099 | TYPE_1099 | — | — |
| 104 | PoLinesAllPEOUnNumberId | UN_NUMBER_ID | — | — |
| 105 | PoLinesAllPEOUnitPrice | UNIT_PRICE | — | — |
| 106 | PoLinesAllPEOUnorderedFlag | UNORDERED_FLAG | — | — |
| 107 | PoLinesAllPEOUomCode | UOM_CODE | — | — |
| 108 | PoLinesAllPEOVendorProductNum | VENDOR_PRODUCT_NUM | — | — |

### [[po_line_locations_all|PO_LINE_LOCATIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PoLineLocationsAllPEOAccrueOnReceiptFlag | ACCRUE_ON_RECEIPT_FLAG | — | — |
| 2 | PoLineLocationsAllPEOAllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | — |
| 3 | PoLineLocationsAllPEOAmount | AMOUNT | — | — |
| 4 | PoLineLocationsAllPEOAmountAccepted | AMOUNT_ACCEPTED | — | — |
| 5 | PoLineLocationsAllPEOAmountBilled | AMOUNT_BILLED | — | — |
| 6 | PoLineLocationsAllPEOAmountCancelled | AMOUNT_CANCELLED | — | — |
| 7 | PoLineLocationsAllPEOAmountFinanced | AMOUNT_FINANCED | — | — |
| 8 | PoLineLocationsAllPEOAmountReceived | AMOUNT_RECEIVED | — | — |
| 9 | PoLineLocationsAllPEOAmountRecouped | AMOUNT_RECOUPED | — | — |
| 10 | PoLineLocationsAllPEOAmountRejected | AMOUNT_REJECTED | — | — |
| 11 | PoLineLocationsAllPEOAmountShipped | AMOUNT_SHIPPED | — | — |
| 12 | PoLineLocationsAllPEOAssessableValue | ASSESSABLE_VALUE | — | — |
| 13 | PoLineLocationsAllPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 14 | PoLineLocationsAllPEOAutoClosureMode | AUTO_CLOSURE_MODE | — | — |
| 15 | PoLineLocationsAllPEOBidPaymentId | BID_PAYMENT_ID | — | — |
| 16 | PoLineLocationsAllPEOCalculateTaxFlag | CALCULATE_TAX_FLAG | — | — |
| 17 | PoLineLocationsAllPEOCancelDate | CANCEL_DATE | — | — |
| 18 | PoLineLocationsAllPEOCancelFlag | CANCEL_FLAG | — | — |
| 19 | PoLineLocationsAllPEOCancelReason | CANCEL_REASON | — | — |
| 20 | PoLineLocationsAllPEOCancelledBy | CANCELLED_BY | — | — |
| 21 | PoLineLocationsAllPEOCarrierId | CARRIER_ID | — | — |
| 22 | PoLineLocationsAllPEOChangePromisedDateReason | CHANGE_PROMISED_DATE_REASON | — | — |
| 23 | PoLineLocationsAllPEOClosedBy | CLOSED_BY | — | — |
| 24 | PoLineLocationsAllPEOClosedDate | CLOSED_DATE | — | — |
| 25 | PoLineLocationsAllPEOClosedForInvoiceDate | CLOSED_FOR_INVOICE_DATE | — | — |
| 26 | PoLineLocationsAllPEOClosedForReceivingDate | CLOSED_FOR_RECEIVING_DATE | — | — |
| 27 | PoLineLocationsAllPEOClosedReason | CLOSED_REASON | — | — |
| 28 | PoLineLocationsAllPEOConsignedFlag | CONSIGNED_FLAG | — | — |
| 29 | PoLineLocationsAllPEOCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | — |
| 30 | PoLineLocationsAllPEOCreatedBy | CREATED_BY | — | — |
| 31 | PoLineLocationsAllPEOCreationDate | CREATION_DATE | — | — |
| 32 | PoLineLocationsAllPEODaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | — |
| 33 | PoLineLocationsAllPEODaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | — |
| 34 | PoLineLocationsAllPEODescription | DESCRIPTION | — | — |
| 35 | PoLineLocationsAllPEODestinationTypeCode | DESTINATION_TYPE_CODE | — | — |
| 36 | PoLineLocationsAllPEODropShipFlag | DROP_SHIP_FLAG | — | — |
| 37 | PoLineLocationsAllPEOEncumberNow | ENCUMBER_NOW | — | — |
| 38 | PoLineLocationsAllPEOEncumberedDate | ENCUMBERED_DATE | — | — |
| 39 | PoLineLocationsAllPEOEncumberedFlag | ENCUMBERED_FLAG | — | — |
| 40 | PoLineLocationsAllPEOEndDate | END_DATE | — | — |
| 41 | PoLineLocationsAllPEOEnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | — |
| 42 | PoLineLocationsAllPEOEstimatedTaxAmount | ESTIMATED_TAX_AMOUNT | — | — |
| 43 | PoLineLocationsAllPEOFinalMatchFlag | FINAL_MATCH_FLAG | — | — |
| 44 | PoLineLocationsAllPEOFirmDate | FIRM_DATE | — | — |
| 45 | PoLineLocationsAllPEOFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 46 | PoLineLocationsAllPEOFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 47 | PoLineLocationsAllPEOFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 48 | PoLineLocationsAllPEOFromHeaderId | FROM_HEADER_ID | — | — |
| 49 | PoLineLocationsAllPEOFromLineId | FROM_LINE_ID | — | — |
| 50 | PoLineLocationsAllPEOFromLineLocationId | FROM_LINE_LOCATION_ID | — | — |
| 51 | PoLineLocationsAllPEOGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 52 | PoLineLocationsAllPEOGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 53 | PoLineLocationsAllPEOGroupName | GROUP_NAME | — | — |
| 54 | PoLineLocationsAllPEOInputTaxClassificationCode | INPUT_TAX_CLASSIFICATION_CODE | — | — |
| 55 | PoLineLocationsAllPEOInspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | — |
| 56 | PoLineLocationsAllPEOInvoiceCloseTolerance | INVOICE_CLOSE_TOLERANCE | — | — |
| 57 | PoLineLocationsAllPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 58 | PoLineLocationsAllPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 59 | PoLineLocationsAllPEOLastAcceptDate | LAST_ACCEPT_DATE | — | — |
| 60 | PoLineLocationsAllPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 61 | PoLineLocationsAllPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 62 | PoLineLocationsAllPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 63 | PoLineLocationsAllPEOLeadTime | LEAD_TIME | — | — |
| 64 | PoLineLocationsAllPEOLeadTimeUnit | LEAD_TIME_UNIT | — | — |
| 65 | PoLineLocationsAllPEOLineIntendedUse | LINE_INTENDED_USE | — | — |
| 66 | PoLineLocationsAllPEOLineLocationId | LINE_LOCATION_ID | — | — |
| 67 | PoLineLocationsAllPEOManualPriceChangeFlag | MANUAL_PRICE_CHANGE_FLAG | — | — |
| 68 | PoLineLocationsAllPEOMatchOption | MATCH_OPTION | — | — |
| 69 | PoLineLocationsAllPEOMatchingBasis | MATCHING_BASIS | — | — |
| 70 | PoLineLocationsAllPEONeedByDate | NEED_BY_DATE | — | — |
| 71 | PoLineLocationsAllPEONoteToReceiver | NOTE_TO_RECEIVER | — | — |
| 72 | PoLineLocationsAllPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 73 | PoLineLocationsAllPEOOriginalShipmentId | ORIGINAL_SHIPMENT_ID | — | — |
| 74 | PoLineLocationsAllPEOOutsourcedAssembly | OUTSOURCED_ASSEMBLY | — | — |
| 75 | PoLineLocationsAllPEOPJC_CONTEXT_CATEGORY | PJC_CONTEXT_CATEGORY | — | — |
| 76 | PoLineLocationsAllPEOPaymentType | PAYMENT_TYPE | — | — |
| 77 | PoLineLocationsAllPEOPoHeaderId | PO_HEADER_ID | — | — |
| 78 | PoLineLocationsAllPEOPoLineId | PO_LINE_ID | — | — |
| 79 | PoLineLocationsAllPEOPoTradingOrganizationId | PO_TRADING_ORGANIZATION_ID | — | — |
| 80 | PoLineLocationsAllPEOPrcBuId | PRC_BU_ID | — | — |
| 81 | PoLineLocationsAllPEOPreferredGrade | PREFERRED_GRADE | — | — |
| 82 | PoLineLocationsAllPEOPriceDiscount | PRICE_DISCOUNT | — | — |
| 83 | PoLineLocationsAllPEOPriceOverride | PRICE_OVERRIDE | — | — |
| 84 | PoLineLocationsAllPEOProductCategory | PRODUCT_CATEGORY | — | — |
| 85 | PoLineLocationsAllPEOProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | — |
| 86 | PoLineLocationsAllPEOProductType | PRODUCT_TYPE | — | — |
| 87 | PoLineLocationsAllPEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 88 | PoLineLocationsAllPEOProgramName | PROGRAM_NAME | — | — |
| 89 | PoLineLocationsAllPEOPromisedDate | PROMISED_DATE | — | — |
| 90 | PoLineLocationsAllPEOQtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | — |
| 91 | PoLineLocationsAllPEOQtyRcvTolerance | QTY_RCV_TOLERANCE | — | — |
| 92 | PoLineLocationsAllPEOQuantity | QUANTITY | — | — |
| 93 | PoLineLocationsAllPEOQuantityAccepted | QUANTITY_ACCEPTED | — | — |
| 94 | PoLineLocationsAllPEOQuantityBilled | QUANTITY_BILLED | — | — |
| 95 | PoLineLocationsAllPEOQuantityCancelled | QUANTITY_CANCELLED | — | — |
| 96 | PoLineLocationsAllPEOQuantityFinanced | QUANTITY_FINANCED | — | — |
| 97 | PoLineLocationsAllPEOQuantityReceived | QUANTITY_RECEIVED | — | — |
| 98 | PoLineLocationsAllPEOQuantityRecouped | QUANTITY_RECOUPED | — | — |
| 99 | PoLineLocationsAllPEOQuantityRejected | QUANTITY_REJECTED | — | — |
| 100 | PoLineLocationsAllPEOQuantityShipped | QUANTITY_SHIPPED | — | — |
| 101 | PoLineLocationsAllPEOReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | — |
| 102 | PoLineLocationsAllPEOReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 103 | PoLineLocationsAllPEOReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | — |
| 104 | PoLineLocationsAllPEOReceivingRoutingId | RECEIVING_ROUTING_ID | — | — |
| 105 | PoLineLocationsAllPEOReqBuId | REQ_BU_ID | — | — |
| 106 | PoLineLocationsAllPEORequestId | REQUEST_ID | — | — |
| 107 | PoLineLocationsAllPEORetainageReleasedAmount | RETAINAGE_RELEASED_AMOUNT | — | — |
| 108 | PoLineLocationsAllPEORetainageWithheldAmount | RETAINAGE_WITHHELD_AMOUNT | — | — |
| 109 | PoLineLocationsAllPEORetroactiveDate | RETROACTIVE_DATE | — | — |
| 110 | PoLineLocationsAllPEOSalesOrderUpdateDate | SALES_ORDER_UPDATE_DATE | — | — |
| 111 | PoLineLocationsAllPEOScheduleStatus | SCHEDULE_STATUS | — | — |
| 112 | PoLineLocationsAllPEOSecondaryQuantity | SECONDARY_QUANTITY | — | — |
| 113 | PoLineLocationsAllPEOSecondaryQuantityAccepted | SECONDARY_QUANTITY_ACCEPTED | — | — |
| 114 | PoLineLocationsAllPEOSecondaryQuantityCancelled | SECONDARY_QUANTITY_CANCELLED | — | — |
| 115 | PoLineLocationsAllPEOSecondaryQuantityReceived | SECONDARY_QUANTITY_RECEIVED | — | — |
| 116 | PoLineLocationsAllPEOSecondaryQuantityRejected | SECONDARY_QUANTITY_REJECTED | — | — |
| 117 | PoLineLocationsAllPEOSecondaryQuantityShipped | SECONDARY_QUANTITY_SHIPPED | — | — |
| 118 | PoLineLocationsAllPEOSecondaryUomCode | SECONDARY_UOM_CODE | — | — |
| 119 | PoLineLocationsAllPEOShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 120 | PoLineLocationsAllPEOShipToOrganizationId | SHIP_TO_ORGANIZATION_ID | — | — |
| 121 | PoLineLocationsAllPEOShipmentClosedDate | SHIPMENT_CLOSED_DATE | — | — |
| 122 | PoLineLocationsAllPEOShipmentNum | SHIPMENT_NUM | — | — |
| 123 | PoLineLocationsAllPEOShipmentType | SHIPMENT_TYPE | — | — |
| 124 | PoLineLocationsAllPEOShippingUomCode | SHIPPING_UOM_CODE | — | ✅ |
| 125 | PoLineLocationsAllPEOShippingUomQuantity | SHIPPING_UOM_QUANTITY | — | ✅ |
| 126 | PoLineLocationsAllPEOShippingUomQuantityReceived | SHIPPING_UOM_QUANTITY_RECEIVED | — | — |
| 127 | PoLineLocationsAllPEOSourceShipmentId | SOURCE_SHIPMENT_ID | — | — |
| 128 | PoLineLocationsAllPEOStartDate | START_DATE | — | — |
| 129 | PoLineLocationsAllPEOSupplierOrderLineNumber | SUPPLIER_ORDER_LINE_NUMBER | — | — |
| 130 | PoLineLocationsAllPEOTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 131 | PoLineLocationsAllPEOTaxCodeId | TAX_CODE_ID | — | — |
| 132 | PoLineLocationsAllPEOTaxName | TAX_NAME | — | — |
| 133 | PoLineLocationsAllPEOTaxUserOverrideFlag | TAX_USER_OVERRIDE_FLAG | — | — |
| 134 | PoLineLocationsAllPEOTaxableFlag | TAXABLE_FLAG | — | — |
| 135 | PoLineLocationsAllPEOTermsId | TERMS_ID | — | — |
| 136 | PoLineLocationsAllPEOTransactionFlowHeaderId | TRANSACTION_FLOW_HEADER_ID | — | — |
| 137 | PoLineLocationsAllPEOTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 138 | PoLineLocationsAllPEOUnencumberedQuantity | UNENCUMBERED_QUANTITY | — | — |
| 139 | PoLineLocationsAllPEOUnitOfMeasureClass | UNIT_OF_MEASURE_CLASS | — | — |
| 140 | PoLineLocationsAllPEOUomCode | UOM_CODE | — | — |
| 141 | PoLineLocationsAllPEOUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 142 | PoLineLocationsAllPEOValueBasis | VALUE_BASIS | — | — |
| 143 | PoLineLocationsAllPEOVmiFlag | VMI_FLAG | — | — |
| 144 | PoLineLocationsAllPEOWorkApproverId | WORK_APPROVER_ID | — | — |

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
| 8 | RcvShipmentHeadersPEOComments | COMMENTS | — | ✅ |
| 9 | RcvShipmentHeadersPEOConversionDate | CONVERSION_DATE | — | — |
| 10 | RcvShipmentHeadersPEOConversionRate | CONVERSION_RATE | — | — |
| 11 | RcvShipmentHeadersPEOConversionRateType | CONVERSION_RATE_TYPE | — | — |
| 12 | RcvShipmentHeadersPEOCreatedBy | CREATED_BY | — | — |
| 13 | RcvShipmentHeadersPEOCreationDate | CREATION_DATE | — | ✅ |
| 14 | RcvShipmentHeadersPEOCurrencyCode | CURRENCY_CODE | — | — |
| 15 | RcvShipmentHeadersPEOCustomerId | CUSTOMER_ID | — | — |
| 16 | RcvShipmentHeadersPEOCustomerSiteId | CUSTOMER_SITE_ID | — | — |
| 17 | RcvShipmentHeadersPEOEdiControlNum | EDI_CONTROL_NUM | — | — |
| 18 | RcvShipmentHeadersPEOEmployeeId | EMPLOYEE_ID | — | — |
| 19 | RcvShipmentHeadersPEOExpectedReceiptDate | EXPECTED_RECEIPT_DATE | — | — |
| 20 | RcvShipmentHeadersPEOFreightAmount | FREIGHT_AMOUNT | — | — |
| 21 | RcvShipmentHeadersPEOFreightBillNumber | FREIGHT_BILL_NUMBER | — | — |
| 22 | RcvShipmentHeadersPEOFreightCarrierId | FREIGHT_CARRIER_ID | — | — |
| 23 | RcvShipmentHeadersPEOFreightTerms | FREIGHT_TERMS | — | — |
| 24 | RcvShipmentHeadersPEOGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 25 | RcvShipmentHeadersPEOGrossWeight | GROSS_WEIGHT | — | — |
| 26 | RcvShipmentHeadersPEOGrossWeightUomCode | GROSS_WEIGHT_UOM_CODE | — | — |
| 27 | RcvShipmentHeadersPEOHazardClass | HAZARD_CLASS | — | — |
| 28 | RcvShipmentHeadersPEOHazardCode | HAZARD_CODE | — | — |
| 29 | RcvShipmentHeadersPEOHazardDescription | HAZARD_DESCRIPTION | — | — |
| 30 | RcvShipmentHeadersPEOInvoiceAmount | INVOICE_AMOUNT | — | — |
| 31 | RcvShipmentHeadersPEOInvoiceDate | INVOICE_DATE | — | — |
| 32 | RcvShipmentHeadersPEOInvoiceNum | INVOICE_NUM | — | — |
| 33 | RcvShipmentHeadersPEOInvoiceStatusCode | INVOICE_STATUS_CODE | — | — |
| 34 | RcvShipmentHeadersPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 35 | RcvShipmentHeadersPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 36 | RcvShipmentHeadersPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 37 | RcvShipmentHeadersPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 38 | RcvShipmentHeadersPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 39 | RcvShipmentHeadersPEOLspFlag | LSP_FLAG | — | — |
| 40 | RcvShipmentHeadersPEONetWeight | NET_WEIGHT | — | ✅ |
| 41 | RcvShipmentHeadersPEONetWeightUomCode | NET_WEIGHT_UOM_CODE | — | ✅ |
| 42 | RcvShipmentHeadersPEONoticeCreationDate | NOTICE_CREATION_DATE | — | — |
| 43 | RcvShipmentHeadersPEONumOfContainers | NUM_OF_CONTAINERS | — | — |
| 44 | RcvShipmentHeadersPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 45 | RcvShipmentHeadersPEOOrganizationId | ORGANIZATION_ID | — | — |
| 46 | RcvShipmentHeadersPEOPackagingCode | PACKAGING_CODE | — | — |
| 47 | RcvShipmentHeadersPEOPackingSlip | PACKING_SLIP | — | ✅ |
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
| 63 | RcvShipmentHeadersPEOReceiptSourceCode | RECEIPT_SOURCE_CODE | — | — |
| 64 | RcvShipmentHeadersPEORemitToSiteId | REMIT_TO_SITE_ID | — | — |
| 65 | RcvShipmentHeadersPEORequestDate | REQUEST_DATE | — | — |
| 66 | RcvShipmentHeadersPEORequestId | REQUEST_ID | — | — |
| 67 | RcvShipmentHeadersPEORmaBuId | RMA_BU_ID | — | — |
| 68 | RcvShipmentHeadersPEOShipFromLocationId | SHIP_FROM_LOCATION_ID | — | — |
| 69 | RcvShipmentHeadersPEOShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 70 | RcvShipmentHeadersPEOShipToOrgId | SHIP_TO_ORG_ID | — | — |
| 71 | RcvShipmentHeadersPEOShipmentHeaderId | SHIPMENT_HEADER_ID | — | ✅ |
| 72 | RcvShipmentHeadersPEOShipmentNum | SHIPMENT_NUM | — | ✅ |
| 73 | RcvShipmentHeadersPEOShippedDate | SHIPPED_DATE | — | ✅ |
| 74 | RcvShipmentHeadersPEOSpecialHandlingCode | SPECIAL_HANDLING_CODE | — | — |
| 75 | RcvShipmentHeadersPEOTarWeight | TAR_WEIGHT | — | ✅ |
| 76 | RcvShipmentHeadersPEOTarWeightUomCode | TAR_WEIGHT_UOM_CODE | — | ✅ |
| 77 | RcvShipmentHeadersPEOTaxAmount | TAX_AMOUNT | — | — |
| 78 | RcvShipmentHeadersPEOTaxName | TAX_NAME | — | — |
| 79 | RcvShipmentHeadersPEOVendorId | VENDOR_ID | — | — |
| 80 | RcvShipmentHeadersPEOVendorSiteId | VENDOR_SITE_ID | — | — |
| 81 | RcvShipmentHeadersPEOWaybillAirbillNum | WAYBILL_AIRBILL_NUM | — | ✅ |

### [[rcv_shipment_lines|RCV_SHIPMENT_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RcvShipmentLinesPEOAmount | AMOUNT | — | — |
| 2 | RcvShipmentLinesPEOAmountReceived | AMOUNT_RECEIVED | — | ✅ |
| 3 | RcvShipmentLinesPEOAmountShipped | AMOUNT_SHIPPED | — | — |
| 4 | RcvShipmentLinesPEOApprovalStatus | APPROVAL_STATUS | — | — |
| 5 | RcvShipmentLinesPEOAsnLineFlag | ASN_LINE_FLAG | — | — |
| 6 | RcvShipmentLinesPEOAsnLpnId | ASN_LPN_ID | — | — |
| 7 | RcvShipmentLinesPEOAssessableValue | ASSESSABLE_VALUE | — | — |
| 8 | RcvShipmentLinesPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 9 | RcvShipmentLinesPEOBarCodeLabel | BAR_CODE_LABEL | — | — |
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
| 26 | RcvShipmentLinesPEODestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
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
| 37 | RcvShipmentLinesPEOItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 38 | RcvShipmentLinesPEOItemId | ITEM_ID | — | ✅ |
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
| 56 | RcvShipmentLinesPEOPoDistributionId | PO_DISTRIBUTION_ID | — | — |
| 57 | RcvShipmentLinesPEOPoHeaderId | PO_HEADER_ID | — | — |
| 58 | RcvShipmentLinesPEOPoLineId | PO_LINE_ID | — | — |
| 59 | RcvShipmentLinesPEOPoLineLocationId | PO_LINE_LOCATION_ID | — | — |
| 60 | RcvShipmentLinesPEOPrimaryUomCode | PRIMARY_UOM_CODE | — | — |
| 61 | RcvShipmentLinesPEOProductCategory | PRODUCT_CATEGORY | — | — |
| 62 | RcvShipmentLinesPEOProductType | PRODUCT_TYPE | — | — |
| 63 | RcvShipmentLinesPEOQcGrade | QC_GRADE | — | — |
| 64 | RcvShipmentLinesPEOQuantityAccepted | QUANTITY_ACCEPTED | — | ✅ |
| 65 | RcvShipmentLinesPEOQuantityDelivered | QUANTITY_DELIVERED | — | ✅ |
| 66 | RcvShipmentLinesPEOQuantityReceived | QUANTITY_RECEIVED | — | ✅ |
| 67 | RcvShipmentLinesPEOQuantityRejected | QUANTITY_REJECTED | — | ✅ |
| 68 | RcvShipmentLinesPEOQuantityReturned | QUANTITY_RETURNED | — | ✅ |
| 69 | RcvShipmentLinesPEOQuantityShipped | QUANTITY_SHIPPED | — | ✅ |
| 70 | RcvShipmentLinesPEORaAllowSubstituteReceipt | RA_ALLOW_SUBSTITUTE_RECEIPT | — | — |
| 71 | RcvShipmentLinesPEORaDaysEarlyReceiptAllowed | RA_DAYS_EARLY_RECEIPT_ALLOWED | — | — |
| 72 | RcvShipmentLinesPEORaDaysLateReceiptAllowed | RA_DAYS_LATE_RECEIPT_ALLOWED | — | — |
| 73 | RcvShipmentLinesPEORaDocLineCreationDate | RA_DOC_LINE_CREATION_DATE | — | — |
| 74 | RcvShipmentLinesPEORaDocLineLastUpdateDate | RA_DOC_LINE_LAST_UPDATE_DATE | — | — |
| 75 | RcvShipmentLinesPEORaDocScheduleNumber | RA_DOC_SCHEDULE_NUMBER | — | — |
| 76 | RcvShipmentLinesPEORaDocumentLineNumber | RA_DOCUMENT_LINE_NUMBER | — | — |
| 77 | RcvShipmentLinesPEORaDooFulfillmentLineNumber | RA_DOO_FULFILLMENT_LINE_NUMBER | — | — |
| 78 | RcvShipmentLinesPEORaDooHeaderNumber | RA_DOO_HEADER_NUMBER | — | — |
| 79 | RcvShipmentLinesPEORaDooLineNumber | RA_DOO_LINE_NUMBER | — | — |
| 80 | RcvShipmentLinesPEORaEnforceShipToLocCode | RA_ENFORCE_SHIP_TO_LOC_CODE | — | — |
| 81 | RcvShipmentLinesPEORaExpectedReceiptDate | RA_EXPECTED_RECEIPT_DATE | — | — |
| 82 | RcvShipmentLinesPEORaLastActionCode | RA_LAST_ACTION_CODE | — | — |
| 83 | RcvShipmentLinesPEORaNoteToReceiver | RA_NOTE_TO_RECEIVER | — | — |
| 84 | RcvShipmentLinesPEORaOrigDooFulfilLineNum | RA_ORIG_DOO_FULFIL_LINE_NUM | — | — |
| 85 | RcvShipmentLinesPEORaOrigDooHeaderNumber | RA_ORIG_DOO_HEADER_NUMBER | — | — |
| 86 | RcvShipmentLinesPEORaOrigDooLineNumber | RA_ORIG_DOO_LINE_NUMBER | — | — |
| 87 | RcvShipmentLinesPEORaOrigOcHeaderNumber | RA_ORIG_OC_HEADER_NUMBER | — | — |
| 88 | RcvShipmentLinesPEORaOrigOcLineNumber | RA_ORIG_OC_LINE_NUMBER | — | — |
| 89 | RcvShipmentLinesPEORaQtyRcvExceptionCode | RA_QTY_RCV_EXCEPTION_CODE | — | — |
| 90 | RcvShipmentLinesPEORaQtyRcvTolerance | RA_QTY_RCV_TOLERANCE | — | — |
| 91 | RcvShipmentLinesPEORaQuantityExpected | RA_QUANTITY_EXPECTED | — | — |
| 92 | RcvShipmentLinesPEORaReceiptDaysExceptionCode | RA_RECEIPT_DAYS_EXCEPTION_CODE | — | — |
| 93 | RcvShipmentLinesPEORaSecondaryQuantityExpected | RA_SECONDARY_QUANTITY_EXPECTED | — | — |
| 94 | RcvShipmentLinesPEORaUnitPrice | RA_UNIT_PRICE | — | — |
| 95 | RcvShipmentLinesPEOReasonId | REASON_ID | — | — |
| 96 | RcvShipmentLinesPEOReceiptAdviceHeaderId | RECEIPT_ADVICE_HEADER_ID | — | — |
| 97 | RcvShipmentLinesPEOReceiptAdviceLineId | RECEIPT_ADVICE_LINE_ID | — | — |
| 98 | RcvShipmentLinesPEOReceiptAdviceLineNumber | RECEIPT_ADVICE_LINE_NUMBER | — | — |
| 99 | RcvShipmentLinesPEOReqDistributionId | REQ_DISTRIBUTION_ID | — | — |
| 100 | RcvShipmentLinesPEORequestId | REQUEST_ID | — | — |
| 101 | RcvShipmentLinesPEORequestedAmount | REQUESTED_AMOUNT | — | — |
| 102 | RcvShipmentLinesPEORequisitionLineId | REQUISITION_LINE_ID | — | — |
| 103 | RcvShipmentLinesPEORoutingHeaderId | ROUTING_HEADER_ID | — | ✅ |
| 104 | RcvShipmentLinesPEOSecondaryQtyAccepted | SECONDARY_QTY_ACCEPTED | — | — |
| 105 | RcvShipmentLinesPEOSecondaryQtyDelivered | SECONDARY_QTY_DELIVERED | — | — |
| 106 | RcvShipmentLinesPEOSecondaryQtyRejected | SECONDARY_QTY_REJECTED | — | — |
| 107 | RcvShipmentLinesPEOSecondaryQtyReturned | SECONDARY_QTY_RETURNED | — | — |
| 108 | RcvShipmentLinesPEOSecondaryQuantityReceived | SECONDARY_QUANTITY_RECEIVED | — | — |
| 109 | RcvShipmentLinesPEOSecondaryQuantityShipped | SECONDARY_QUANTITY_SHIPPED | — | — |
| 110 | RcvShipmentLinesPEOSecondaryUomCode | SECONDARY_UOM_CODE | — | — |
| 111 | RcvShipmentLinesPEOShipFromLocationId | SHIP_FROM_LOCATION_ID | — | — |
| 112 | RcvShipmentLinesPEOShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 113 | RcvShipmentLinesPEOShipmentHeaderId | SHIPMENT_HEADER_ID | — | — |
| 114 | RcvShipmentLinesPEOShipmentLineStatusCode | SHIPMENT_LINE_STATUS_CODE | — | — |
| 115 | RcvShipmentLinesPEOShipmentUnitPrice | SHIPMENT_UNIT_PRICE | — | — |
| 116 | RcvShipmentLinesPEOSourceDocumentCode | SOURCE_DOCUMENT_CODE | — | — |
| 117 | RcvShipmentLinesPEOSpGroupId | SP_GROUP_ID | — | — |
| 118 | RcvShipmentLinesPEOSpQuantity | SP_QUANTITY | — | — |
| 119 | RcvShipmentLinesPEOSpUomCode | SP_UOM_CODE | — | — |
| 120 | RcvShipmentLinesPEOTaxAmount | TAX_AMOUNT | — | — |
| 121 | RcvShipmentLinesPEOTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 122 | RcvShipmentLinesPEOTaxName | TAX_NAME | — | — |
| 123 | RcvShipmentLinesPEOThirdPtyRegId | THIRD_PTY_REG_ID | — | — |
| 124 | RcvShipmentLinesPEOTimecardId | TIMECARD_ID | — | — |
| 125 | RcvShipmentLinesPEOTimecardOvn | TIMECARD_OVN | — | — |
| 126 | RcvShipmentLinesPEOToOrganizationId | TO_ORGANIZATION_ID | — | — |
| 127 | RcvShipmentLinesPEOToSubinventory | TO_SUBINVENTORY | — | — |
| 128 | RcvShipmentLinesPEOTransferCost | TRANSFER_COST | — | — |
| 129 | RcvShipmentLinesPEOTransferPercentage | TRANSFER_PERCENTAGE | — | — |
| 130 | RcvShipmentLinesPEOTransportationCost | TRANSPORTATION_COST | — | — |
| 131 | RcvShipmentLinesPEOTruckNum | TRUCK_NUM | — | — |
| 132 | RcvShipmentLinesPEOTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 133 | RcvShipmentLinesPEOUomCode | UOM_CODE | — | ✅ |
| 134 | RcvShipmentLinesPEOUomConversionRate | UOM_CONVERSION_RATE | — | — |
| 135 | RcvShipmentLinesPEOUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 136 | RcvShipmentLinesPEOVendorCumShippedQuantity | VENDOR_CUM_SHIPPED_QUANTITY | — | — |
| 137 | RcvShipmentLinesPEOVendorItemNum | VENDOR_ITEM_NUM | — | — |
| 138 | RcvShipmentLinesPEOVendorLotNum | VENDOR_LOT_NUM | — | — |
| 139 | ShipmentLineId | SHIPMENT_LINE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
