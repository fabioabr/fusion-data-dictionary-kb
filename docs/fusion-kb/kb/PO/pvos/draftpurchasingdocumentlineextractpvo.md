---
id: DOC-PO-PVO-DraftPurchasingDocumentLineExtractPVO
doc_type: system-doc
title: "DraftPurchasingDocumentLineExtractPVO — PVO Purchasing"
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
  - DraftPurchasingDocumentLineExtractPVO
  - draftpurchasingdocumentlineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DraftPurchasingDocumentLineExtractPVO

## 📌 Visão Geral

Extrai as linhas de rascunhos de documentos de compra, com itens e quantidades em fase de elaboração. Permite previsão de demanda futura baseada em pedidos ainda não finalizados.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoBiccExtractAM.DraftPurchasingDocumentLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 118 | 1 | 1 | 113 | 96% |

---

## 🔗 Tabelas Relacionadas

- [[po_lines_draft_all|PO_LINES_DRAFT_ALL]] — 118 atributos (1 PKs, 113 BICC)

---

## ⚙️ Atributos

### [[po_lines_draft_all|PO_LINES_DRAFT_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgingPeriodDays | AGING_PERIOD_DAYS | — | ✅ |
| 2 | AllowDescriptionUpdateFlag | ALLOW_DESCRIPTION_UPDATE_FLAG | — | ✅ |
| 3 | AllowPriceOverrideFlag | ALLOW_PRICE_OVERRIDE_FLAG | — | ✅ |
| 4 | Amount | AMOUNT | — | ✅ |
| 5 | AuctionDisplayNumber | AUCTION_DISPLAY_NUMBER | — | ✅ |
| 6 | AuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 7 | AuctionLineNumber | AUCTION_LINE_NUMBER | — | ✅ |
| 8 | BaseModelId | BASE_MODEL_ID | — | ✅ |
| 9 | BaseModelPrice | BASE_MODEL_PRICE | — | ✅ |
| 10 | BaseQty | BASE_QTY | — | ✅ |
| 11 | BaseUnitPrice | BASE_UNIT_PRICE | — | ✅ |
| 12 | BaseUom | BASE_UOM | — | ✅ |
| 13 | BidLineNumber | BID_LINE_NUMBER | — | ✅ |
| 14 | BidNumber | BID_NUMBER | — | ✅ |
| 15 | CancelDate | CANCEL_DATE | — | ✅ |
| 16 | CancelFlag | CANCEL_FLAG | — | ✅ |
| 17 | CancelReason | CANCEL_REASON | — | ✅ |
| 18 | CancelledBy | CANCELLED_BY | — | ✅ |
| 19 | CapitalExpenseFlag | CAPITAL_EXPENSE_FLAG | — | ✅ |
| 20 | CategoryId | CATEGORY_ID | — | ✅ |
| 21 | ChangeAcceptedFlag | CHANGE_ACCEPTED_FLAG | — | ✅ |
| 22 | CoAmountCancelled | CO_AMOUNT_CANCELLED | — | ✅ |
| 23 | CoQuantityCancelled | CO_QUANTITY_CANCELLED | — | ✅ |
| 24 | CommittedAmount | COMMITTED_AMOUNT | — | ✅ |
| 25 | ConfiguredItemFlag | CONFIGURED_ITEM_FLAG | — | ✅ |
| 26 | ConsignmentLineFlag | CONSIGNMENT_LINE_FLAG | — | ✅ |
| 27 | ContractId | CONTRACT_ID | — | ✅ |
| 28 | ContractorFirstName | CONTRACTOR_FIRST_NAME | — | ✅ |
| 29 | ContractorLastName | CONTRACTOR_LAST_NAME | — | ✅ |
| 30 | CreatedBy | CREATED_BY | — | ✅ |
| 31 | CreationDate | CREATION_DATE | — | ✅ |
| 32 | EntityChangeTypeCode | ENTITY_CHANGE_TYPE_CODE | — | ✅ |
| 33 | ExpirationDate | EXPIRATION_DATE | — | ✅ |
| 34 | ExternalChangeFlag | EXTERNAL_CHANGE_FLAG | — | ✅ |
| 35 | FromHeaderId | FROM_HEADER_ID | — | ✅ |
| 36 | FromLineId | FROM_LINE_ID | — | ✅ |
| 37 | FromLineLocationId | FROM_LINE_LOCATION_ID | — | ✅ |
| 38 | FundsStatus | FUNDS_STATUS | — | ✅ |
| 39 | HazardClassId | HAZARD_CLASS_ID | — | ✅ |
| 40 | ItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 41 | ItemId | ITEM_ID | — | ✅ |
| 42 | ItemRevision | ITEM_REVISION | — | ✅ |
| 43 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 44 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 45 | JobId | JOB_ID | — | ✅ |
| 46 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 47 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 48 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 49 | LineNum | LINE_NUM | — | ✅ |
| 50 | LineReferenceNum | LINE_REFERENCE_NUM | — | ✅ |
| 51 | LineStartDate | LINE_START_DATE | — | — |
| 52 | LineTypeId | LINE_TYPE_ID | — | ✅ |
| 53 | ListPricePerUnit | LIST_PRICE_PER_UNIT | — | ✅ |
| 54 | ManualPriceChangeFlag | MANUAL_PRICE_CHANGE_FLAG | — | ✅ |
| 55 | Manufacturer | MANUFACTURER | — | ✅ |
| 56 | ManufacturerPartNum | MANUFACTURER_PART_NUM | — | ✅ |
| 57 | MarketPrice | MARKET_PRICE | — | ✅ |
| 58 | MatchingBasis | MATCHING_BASIS | — | ✅ |
| 59 | MaxRetainageAmount | MAX_RETAINAGE_AMOUNT | — | ✅ |
| 60 | MinReleaseAmount | MIN_RELEASE_AMOUNT | — | ✅ |
| 61 | NegotiatedByPreparerFlag | NEGOTIATED_BY_PREPARER_FLAG | — | ✅ |
| 62 | NotToExceedPrice | NOT_TO_EXCEED_PRICE | — | ✅ |
| 63 | NoteToVendor | NOTE_TO_VENDOR | — | ✅ |
| 64 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 65 | OkeContractHeaderId | OKE_CONTRACT_HEADER_ID | — | ✅ |
| 66 | OkeContractVersionId | OKE_CONTRACT_VERSION_ID | — | ✅ |
| 67 | OptionsPrice | OPTIONS_PRICE | — | ✅ |
| 68 | OrderTypeLookupCode | ORDER_TYPE_LOOKUP_CODE | — | ✅ |
| 69 | OriginalInterfaceLineId | ORIGINAL_INTERFACE_LINE_ID | — | ✅ |
| 70 | OverToleranceErrorFlag | OVER_TOLERANCE_ERROR_FLAG | — | ✅ |
| 71 | ParentItemId | PARENT_ITEM_ID | — | ✅ |
| 72 | PjcContextCategory | PJC_CONTEXT_CATEGORY | — | ✅ |
| 73 | PoHeaderId | PO_HEADER_ID | — | ✅ |
| 74 | PoLineId | PO_LINE_ID | 🔑 | ✅ |
| 75 | PrcBuId | PRC_BU_ID | — | ✅ |
| 76 | PreferredGrade | PREFERRED_GRADE | — | — |
| 77 | PriceBreakLookupCode | PRICE_BREAK_LOOKUP_CODE | — | ✅ |
| 78 | PriceTypeLookupCode | PRICE_TYPE_LOOKUP_CODE | — | ✅ |
| 79 | ProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 80 | ProgramName | PROGRAM_NAME | — | ✅ |
| 81 | ProgressPaymentRate | PROGRESS_PAYMENT_RATE | — | — |
| 82 | PurchaseBasis | PURCHASE_BASIS | — | ✅ |
| 83 | QcGrade | QC_GRADE | — | ✅ |
| 84 | QtyRcvTolerance | QTY_RCV_TOLERANCE | — | ✅ |
| 85 | Quantity | QUANTITY | — | ✅ |
| 86 | QuantityCommitted | QUANTITY_COMMITTED | — | ✅ |
| 87 | ReasonForChange | REASON_FOR_CHANGE | — | ✅ |
| 88 | RecoupmentRate | RECOUPMENT_RATE | — | ✅ |
| 89 | RejectedBy | REJECTED_BY | — | ✅ |
| 90 | RejectedByRole | REJECTED_BY_ROLE | — | ✅ |
| 91 | RejectedReason | REJECTED_REASON | — | ✅ |
| 92 | ReqBuId | REQ_BU_ID | — | ✅ |
| 93 | RequestId | REQUEST_ID | — | ✅ |
| 94 | RetainageRate | RETAINAGE_RATE | — | ✅ |
| 95 | RetroactiveDate | RETROACTIVE_DATE | — | ✅ |
| 96 | SecondaryQuantity | SECONDARY_QUANTITY | — | ✅ |
| 97 | SecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 98 | ShippingUomCode | SHIPPING_UOM_CODE | — | ✅ |
| 99 | ShippingUomQuantity | SHIPPING_UOM_QUANTITY | — | ✅ |
| 100 | SourceDocRevNum | SOURCE_DOC_REV_NUM | — | ✅ |
| 101 | StartDate | START_DATE | — | ✅ |
| 102 | SupplierParentItem | SUPPLIER_PARENT_ITEM | — | ✅ |
| 103 | SupplierPartAuxid | SUPPLIER_PART_AUXID | — | ✅ |
| 104 | SupplierRefNumber | SUPPLIER_REF_NUMBER | — | ✅ |
| 105 | SupplierTopModel | SUPPLIER_TOP_MODEL | — | ✅ |
| 106 | TaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | ✅ |
| 107 | TaxCodeId | TAX_CODE_ID | — | ✅ |
| 108 | TaxExclusivePrice | TAX_EXCLUSIVE_PRICE | — | ✅ |
| 109 | TaxName | TAX_NAME | — | ✅ |
| 110 | TaxableFlag | TAXABLE_FLAG | — | ✅ |
| 111 | TopModelId | TOP_MODEL_ID | — | ✅ |
| 112 | Type1099 | TYPE_1099 | — | ✅ |
| 113 | UnNumberId | UN_NUMBER_ID | — | ✅ |
| 114 | UnitPrice | UNIT_PRICE | — | ✅ |
| 115 | UnorderedFlag | UNORDERED_FLAG | — | ✅ |
| 116 | UomCode | UOM_CODE | — | ✅ |
| 117 | VendorProductNum | VENDOR_PRODUCT_NUM | — | ✅ |
| 118 | WorkOrderProduct | WORK_ORDER_PRODUCT | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
