---
id: DOC-PO-PVO-NegotiationLineExtractPVO
doc_type: system-doc
title: "NegotiationLineExtractPVO — PVO Purchasing"
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
  - NegotiationLineExtractPVO
  - negotiationlineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationLineExtractPVO

## 📌 Visão Geral

Extrai as linhas de negociações de sourcing para carga BICC, detalhando itens em cotação, quantidades estimadas, preços-alvo e especificações. Permite análise de escopo e complexidade de cada evento.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.NegotiationLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 152 | 1 | 2 | 68 | 45% |

---

## 🔗 Tabelas Relacionadas

- [[pon_auction_item_prices_all|PON_AUCTION_ITEM_PRICES_ALL]] — 152 atributos (2 PKs, 68 BICC)

---

## ⚙️ Atributos

### [[pon_auction_item_prices_all|PON_AUCTION_ITEM_PRICES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdditionalJobDetails | ADDITIONAL_JOB_DETAILS | — | — |
| 2 | AdvanceAmount | ADVANCE_AMOUNT | — | — |
| 3 | AllocationStatus | ALLOCATION_STATUS | — | ✅ |
| 4 | AllowAlternateLines | ALLOW_ALTERNATE_LINES | — | ✅ |
| 5 | Attribute1 | ATTRIBUTE1 | — | — |
| 6 | Attribute10 | ATTRIBUTE10 | — | — |
| 7 | Attribute11 | ATTRIBUTE11 | — | — |
| 8 | Attribute12 | ATTRIBUTE12 | — | — |
| 9 | Attribute13 | ATTRIBUTE13 | — | — |
| 10 | Attribute14 | ATTRIBUTE14 | — | — |
| 11 | Attribute15 | ATTRIBUTE15 | — | — |
| 12 | Attribute16 | ATTRIBUTE16 | — | — |
| 13 | Attribute17 | ATTRIBUTE17 | — | — |
| 14 | Attribute18 | ATTRIBUTE18 | — | — |
| 15 | Attribute19 | ATTRIBUTE19 | — | — |
| 16 | Attribute2 | ATTRIBUTE2 | — | — |
| 17 | Attribute20 | ATTRIBUTE20 | — | — |
| 18 | Attribute3 | ATTRIBUTE3 | — | — |
| 19 | Attribute4 | ATTRIBUTE4 | — | — |
| 20 | Attribute5 | ATTRIBUTE5 | — | — |
| 21 | Attribute6 | ATTRIBUTE6 | — | — |
| 22 | Attribute7 | ATTRIBUTE7 | — | — |
| 23 | Attribute8 | ATTRIBUTE8 | — | — |
| 24 | Attribute9 | ATTRIBUTE9 | — | — |
| 25 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 26 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 27 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 28 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 29 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 30 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 31 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 32 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 33 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 34 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 35 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 36 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 37 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 38 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 39 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 40 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 41 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 42 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 43 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 44 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 45 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 46 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 47 | AttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 48 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 49 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 50 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 51 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 52 | AttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 53 | AttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 54 | AttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 55 | AttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 56 | AuctionHeaderId | AUCTION_HEADER_ID | 🔑 | ✅ |
| 57 | AwardMode | AWARD_MODE | — | ✅ |
| 58 | AwardStatus | AWARD_STATUS | — | ✅ |
| 59 | AwardedQuantity | AWARDED_QUANTITY | — | ✅ |
| 60 | BestBidBidCurrencyCode | BEST_BID_BID_CURRENCY_CODE | — | — |
| 61 | BestBidBidCurrencyPrice | BEST_BID_BID_CURRENCY_PRICE | — | — |
| 62 | BestBidBidNumber | BEST_BID_BID_NUMBER | — | — |
| 63 | BestBidBidPrice | BEST_BID_BID_PRICE | — | — |
| 64 | BestBidCurrencyCode | BEST_BID_CURRENCY_CODE | — | — |
| 65 | BestBidCurrencyPrice | BEST_BID_CURRENCY_PRICE | — | — |
| 66 | BestBidFirstBidPrice | BEST_BID_FIRST_BID_PRICE | — | — |
| 67 | BestBidNumber | BEST_BID_NUMBER | — | — |
| 68 | BestBidPrice | BEST_BID_PRICE | — | — |
| 69 | BestBidPromisedDate | BEST_BID_PROMISED_DATE | — | — |
| 70 | BestBidProxyLimitPrice | BEST_BID_PROXY_LIMIT_PRICE | — | — |
| 71 | BestBidQuantity | BEST_BID_QUANTITY | — | — |
| 72 | BestBidScore | BEST_BID_SCORE | — | — |
| 73 | BidStartPrice | BID_START_PRICE | — | — |
| 74 | CarrierId | CARRIER_ID | — | ✅ |
| 75 | CategoryId | CATEGORY_ID | — | ✅ |
| 76 | CloseBiddingDate | CLOSE_BIDDING_DATE | — | ✅ |
| 77 | CreatedBy | CREATED_BY | — | ✅ |
| 78 | CreationDate | CREATION_DATE | — | ✅ |
| 79 | CurrentPrice | CURRENT_PRICE | — | ✅ |
| 80 | DifferentialResponseType | DIFFERENTIAL_RESPONSE_TYPE | — | — |
| 81 | DispLineNumber | DISP_LINE_NUMBER | — | ✅ |
| 82 | DisplayTargetPriceFlag | DISPLAY_TARGET_PRICE_FLAG | — | ✅ |
| 83 | DocumentDispLineNumber | DOCUMENT_DISP_LINE_NUMBER | — | ✅ |
| 84 | GroupType | GROUP_TYPE | — | ✅ |
| 85 | HasAttributesFlag | HAS_ATTRIBUTES_FLAG | — | ✅ |
| 86 | HasBuyerPfsFlag | HAS_BUYER_PFS_FLAG | — | ✅ |
| 87 | HasPaymentsFlag | HAS_PAYMENTS_FLAG | — | — |
| 88 | HasPriceDifferentialsFlag | HAS_PRICE_DIFFERENTIALS_FLAG | — | — |
| 89 | HasPriceElementsFlag | HAS_PRICE_ELEMENTS_FLAG | — | ✅ |
| 90 | HasQuantityTiers | HAS_QUANTITY_TIERS | — | ✅ |
| 91 | HasShipmentsFlag | HAS_SHIPMENTS_FLAG | — | ✅ |
| 92 | InvOrgId | INV_ORG_ID | — | ✅ |
| 93 | ItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 94 | ItemId | ITEM_ID | — | ✅ |
| 95 | ItemRevision | ITEM_REVISION | — | ✅ |
| 96 | JobId | JOB_ID | — | ✅ |
| 97 | LastAmendmentUpdate | LAST_AMENDMENT_UPDATE | — | ✅ |
| 98 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 99 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 100 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 101 | LineNumber | LINE_NUMBER | 🔑 | ✅ |
| 102 | LineOriginationCode | LINE_ORIGINATION_CODE | — | ✅ |
| 103 | LineTypeId | LINE_TYPE_ID | — | ✅ |
| 104 | MaxRetainageAmount | MAX_RETAINAGE_AMOUNT | — | — |
| 105 | MaxSubLineSequenceNumber | MAX_SUB_LINE_SEQUENCE_NUMBER | — | ✅ |
| 106 | ModeOfTransport | MODE_OF_TRANSPORT | — | ✅ |
| 107 | ModifiedDate | MODIFIED_DATE | — | ✅ |
| 108 | ModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 109 | NeedByDate | NEED_BY_DATE | — | ✅ |
| 110 | NoAward | NO_AWARD | — | ✅ |
| 111 | NoteToBidders | NOTE_TO_BIDDERS | — | ✅ |
| 112 | NumberOfBids | NUMBER_OF_BIDS | — | — |
| 113 | NumberOfExtensions | NUMBER_OF_EXTENSIONS | — | — |
| 114 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 115 | OrderTypeLookupCode | ORDER_TYPE_LOOKUP_CODE | — | ✅ |
| 116 | ParentLineNumber | PARENT_LINE_NUMBER | — | ✅ |
| 117 | PoAgreedAmount | PO_AGREED_AMOUNT | — | ✅ |
| 118 | PoMinRelAmount | PO_MIN_REL_AMOUNT | — | ✅ |
| 119 | PrcBuId | PRC_BU_ID | — | ✅ |
| 120 | PriceBreakNegFlag | PRICE_BREAK_NEG_FLAG | — | ✅ |
| 121 | PriceBreakType | PRICE_BREAK_TYPE | — | ✅ |
| 122 | PriceDiffShipmentNumber | PRICE_DIFF_SHIPMENT_NUMBER | — | — |
| 123 | PriceDisabledFlag | PRICE_DISABLED_FLAG | — | ✅ |
| 124 | ProgressPymtRatePercent | PROGRESS_PYMT_RATE_PERCENT | — | — |
| 125 | ProjectAwardId | PROJECT_AWARD_ID | — | — |
| 126 | ProjectExpOrganizationId | PROJECT_EXP_ORGANIZATION_ID | — | — |
| 127 | ProjectExpenditureItemDate | PROJECT_EXPENDITURE_ITEM_DATE | — | — |
| 128 | ProjectExpenditureType | PROJECT_EXPENDITURE_TYPE | — | — |
| 129 | ProjectId | PROJECT_ID | — | — |
| 130 | ProjectTaskId | PROJECT_TASK_ID | — | — |
| 131 | PurchaseBasis | PURCHASE_BASIS | — | ✅ |
| 132 | Quantity | QUANTITY | — | ✅ |
| 133 | QuantityDisabledFlag | QUANTITY_DISABLED_FLAG | — | ✅ |
| 134 | RecommendedAwardAmount | RECOMMENDED_AWARD_AMOUNT | — | ✅ |
| 135 | RecoupmentRatePercent | RECOUPMENT_RATE_PERCENT | — | — |
| 136 | ReqBuId | REQ_BU_ID | — | ✅ |
| 137 | RequestedDeliveryDate | REQUESTED_DELIVERY_DATE | — | ✅ |
| 138 | RequestedShipDate | REQUESTED_SHIP_DATE | — | ✅ |
| 139 | RequisitionNumber | REQUISITION_NUMBER | — | ✅ |
| 140 | RetainageRatePercent | RETAINAGE_RATE_PERCENT | — | — |
| 141 | ServiceLevel | SERVICE_LEVEL | — | ✅ |
| 142 | ShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 143 | SourceDocId | SOURCE_DOC_ID | — | ✅ |
| 144 | SourceDocNumber | SOURCE_DOC_NUMBER | — | ✅ |
| 145 | SourceLineId | SOURCE_LINE_ID | — | ✅ |
| 146 | SourceLineNumber | SOURCE_LINE_NUMBER | — | ✅ |
| 147 | SubLineSequenceNumber | SUB_LINE_SEQUENCE_NUMBER | — | ✅ |
| 148 | TargetPrice | TARGET_PRICE | — | ✅ |
| 149 | UnitDisplayTargetFlag | UNIT_DISPLAY_TARGET_FLAG | — | ✅ |
| 150 | UnitTargetPrice | UNIT_TARGET_PRICE | — | ✅ |
| 151 | UomCode | UOM_CODE | — | ✅ |
| 152 | WorkApproverUserId | WORK_APPROVER_USER_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
