---
id: DOC-PO-PVO-PurchasingDocumentLineExtractPVO
doc_type: system-doc
title: "PurchasingDocumentLineExtractPVO — PVO Purchasing"
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
  - PurchasingDocumentLineExtractPVO
  - purchasingdocumentlineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PurchasingDocumentLineExtractPVO

## 📌 Visão Geral

Extrai as linhas individuais de ordens de compra para carga BICC, detalhando itens, quantidades, preços unitários, categorias e datas prometidas. Permite análise granular de compras por item e comparação de preços entre fornecedores.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoBiccExtractAM.PurchasingDocumentLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 112 | 1 | 1 | 107 | 96% |

---

## 🔗 Tabelas Relacionadas

- [[po_lines_all|PO_LINES_ALL]] — 112 atributos (1 PKs, 107 BICC)

---

## ⚙️ Atributos

### [[po_lines_all|PO_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgingPeriodDays | AGING_PERIOD_DAYS | — | ✅ |
| 2 | AllowDescriptionUpdateFlag | ALLOW_DESCRIPTION_UPDATE_FLAG | — | ✅ |
| 3 | AllowPriceOverrideFlag | ALLOW_PRICE_OVERRIDE_FLAG | — | ✅ |
| 4 | Amount | AMOUNT | — | ✅ |
| 5 | AmountReleased | AMOUNT_RELEASED | — | ✅ |
| 6 | AuctionDisplayNumber | AUCTION_DISPLAY_NUMBER | — | ✅ |
| 7 | AuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 8 | AuctionLineNumber | AUCTION_LINE_NUMBER | — | ✅ |
| 9 | BaseModelId | BASE_MODEL_ID | — | ✅ |
| 10 | BaseModelPrice | BASE_MODEL_PRICE | — | ✅ |
| 11 | BaseQty | BASE_QTY | — | ✅ |
| 12 | BaseUnitPrice | BASE_UNIT_PRICE | — | ✅ |
| 13 | BaseUom | BASE_UOM | — | ✅ |
| 14 | BidLineNumber | BID_LINE_NUMBER | — | ✅ |
| 15 | BidNumber | BID_NUMBER | — | ✅ |
| 16 | CancelDate | CANCEL_DATE | — | ✅ |
| 17 | CancelFlag | CANCEL_FLAG | — | ✅ |
| 18 | CancelReason | CANCEL_REASON | — | ✅ |
| 19 | CancelledBy | CANCELLED_BY | — | ✅ |
| 20 | CapitalExpenseFlag | CAPITAL_EXPENSE_FLAG | — | ✅ |
| 21 | CategoryId | CATEGORY_ID | — | ✅ |
| 22 | ClosedBy | CLOSED_BY | — | ✅ |
| 23 | ClosedDate | CLOSED_DATE | — | ✅ |
| 24 | ClosedReason | CLOSED_REASON | — | ✅ |
| 25 | CommittedAmount | COMMITTED_AMOUNT | — | ✅ |
| 26 | ConfiguredItemFlag | CONFIGURED_ITEM_FLAG | — | ✅ |
| 27 | ConsignmentLineFlag | CONSIGNMENT_LINE_FLAG | — | ✅ |
| 28 | ContractId | CONTRACT_ID | — | ✅ |
| 29 | ContractorFirstName | CONTRACTOR_FIRST_NAME | — | ✅ |
| 30 | ContractorLastName | CONTRACTOR_LAST_NAME | — | ✅ |
| 31 | CreatedBy | CREATED_BY | — | ✅ |
| 32 | CreationDate | CREATION_DATE | — | ✅ |
| 33 | Discount | DISCOUNT | — | ✅ |
| 34 | DiscountReason | DISCOUNT_REASON | — | ✅ |
| 35 | DiscountType | DISCOUNT_TYPE | — | ✅ |
| 36 | ExpirationDate | EXPIRATION_DATE | — | ✅ |
| 37 | FromHeaderId | FROM_HEADER_ID | — | ✅ |
| 38 | FromLineId | FROM_LINE_ID | — | ✅ |
| 39 | FromLineLocationId | FROM_LINE_LOCATION_ID | — | ✅ |
| 40 | FundsStatus | FUNDS_STATUS | — | ✅ |
| 41 | HazardClassId | HAZARD_CLASS_ID | — | ✅ |
| 42 | ItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 43 | ItemId | ITEM_ID | — | ✅ |
| 44 | ItemRevision | ITEM_REVISION | — | ✅ |
| 45 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 46 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 47 | JobId | JOB_ID | — | ✅ |
| 48 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 49 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 50 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 51 | LastUpdatedProgram | LAST_UPDATED_PROGRAM | — | ✅ |
| 52 | LineNum | LINE_NUM | — | ✅ |
| 53 | LineReferenceNum | LINE_REFERENCE_NUM | — | ✅ |
| 54 | LineStartDate | LINE_START_DATE | — | — |
| 55 | LineStatus | LINE_STATUS | — | ✅ |
| 56 | LineTypeId | LINE_TYPE_ID | — | ✅ |
| 57 | ListPrice | LIST_PRICE | — | ✅ |
| 58 | ListPricePerUnit | LIST_PRICE_PER_UNIT | — | ✅ |
| 59 | ManualPriceChangeFlag | MANUAL_PRICE_CHANGE_FLAG | — | ✅ |
| 60 | Manufacturer | MANUFACTURER | — | ✅ |
| 61 | ManufacturerPartNum | MANUFACTURER_PART_NUM | — | ✅ |
| 62 | MarketPrice | MARKET_PRICE | — | ✅ |
| 63 | MatchingBasis | MATCHING_BASIS | — | ✅ |
| 64 | MaxRetainageAmount | MAX_RETAINAGE_AMOUNT | — | ✅ |
| 65 | MinReleaseAmount | MIN_RELEASE_AMOUNT | — | ✅ |
| 66 | NegotiatedByPreparerFlag | NEGOTIATED_BY_PREPARER_FLAG | — | ✅ |
| 67 | NextConsumptionAdvGenDate | NEXT_CONSUMPTION_ADV_GEN_DATE | — | ✅ |
| 68 | NotToExceedPrice | NOT_TO_EXCEED_PRICE | — | ✅ |
| 69 | NoteToVendor | NOTE_TO_VENDOR | — | ✅ |
| 70 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 71 | OkeContractHeaderId | OKE_CONTRACT_HEADER_ID | — | ✅ |
| 72 | OkeContractVersionId | OKE_CONTRACT_VERSION_ID | — | ✅ |
| 73 | OptionsPrice | OPTIONS_PRICE | — | ✅ |
| 74 | OrderTypeLookupCode | ORDER_TYPE_LOOKUP_CODE | — | ✅ |
| 75 | OverToleranceErrorFlag | OVER_TOLERANCE_ERROR_FLAG | — | ✅ |
| 76 | ParentItemId | PARENT_ITEM_ID | — | ✅ |
| 77 | PoHeaderId | PO_HEADER_ID | — | ✅ |
| 78 | PoLineId | PO_LINE_ID | 🔑 | ✅ |
| 79 | PrcBuId | PRC_BU_ID | — | ✅ |
| 80 | PreferredGrade | PREFERRED_GRADE | — | — |
| 81 | PriceBreakLookupCode | PRICE_BREAK_LOOKUP_CODE | — | ✅ |
| 82 | PriceTypeLookupCode | PRICE_TYPE_LOOKUP_CODE | — | ✅ |
| 83 | ProgressPaymentRate | PROGRESS_PAYMENT_RATE | — | — |
| 84 | PurchaseBasis | PURCHASE_BASIS | — | ✅ |
| 85 | QtyRcvTolerance | QTY_RCV_TOLERANCE | — | ✅ |
| 86 | Quantity | QUANTITY | — | ✅ |
| 87 | QuantityCommitted | QUANTITY_COMMITTED | — | ✅ |
| 88 | ReqBuId | REQ_BU_ID | — | ✅ |
| 89 | RequestId | REQUEST_ID | — | ✅ |
| 90 | RetroactiveDate | RETROACTIVE_DATE | — | ✅ |
| 91 | SecondaryQuantity | SECONDARY_QUANTITY | — | ✅ |
| 92 | SecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 93 | ShippingUomCode | SHIPPING_UOM_CODE | — | ✅ |
| 94 | ShippingUomQuantity | SHIPPING_UOM_QUANTITY | — | ✅ |
| 95 | SourceDocRevNum | SOURCE_DOC_REV_NUM | — | ✅ |
| 96 | StartDate | START_DATE | — | ✅ |
| 97 | SupplierParentItem | SUPPLIER_PARENT_ITEM | — | ✅ |
| 98 | SupplierPartAuxid | SUPPLIER_PART_AUXID | — | ✅ |
| 99 | SupplierRefNumber | SUPPLIER_REF_NUMBER | — | ✅ |
| 100 | SupplierTopModel | SUPPLIER_TOP_MODEL | — | ✅ |
| 101 | TaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | ✅ |
| 102 | TaxCodeId | TAX_CODE_ID | — | ✅ |
| 103 | TaxExclusivePrice | TAX_EXCLUSIVE_PRICE | — | ✅ |
| 104 | TaxName | TAX_NAME | — | ✅ |
| 105 | TaxableFlag | TAXABLE_FLAG | — | ✅ |
| 106 | TopModelId | TOP_MODEL_ID | — | ✅ |
| 107 | UnNumberId | UN_NUMBER_ID | — | ✅ |
| 108 | UnitPrice | UNIT_PRICE | — | ✅ |
| 109 | UnorderedFlag | UNORDERED_FLAG | — | ✅ |
| 110 | UomCode | UOM_CODE | — | ✅ |
| 111 | VendorProductNum | VENDOR_PRODUCT_NUM | — | ✅ |
| 112 | WorkOrderProduct | WORK_ORDER_PRODUCT | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
