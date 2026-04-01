---
id: DOC-PO-PVO-NegotiationResponseLineExtractPVO
doc_type: system-doc
title: "NegotiationResponseLineExtractPVO — PVO Purchasing"
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
  - NegotiationResponseLineExtractPVO
  - negotiationresponselineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationResponseLineExtractPVO

## 📌 Visão Geral

Extrai as linhas de respostas de fornecedores para carga BICC, com preços unitários, quantidades ofertadas e condições. Alimenta comparações detalhadas de propostas e análise de savings.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.NegotiationResponseLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 96 | 1 | 2 | 63 | 66% |

---

## 🔗 Tabelas Relacionadas

- [[pon_bid_item_prices|PON_BID_ITEM_PRICES]] — 96 atributos (2 PKs, 63 BICC)

---

## ⚙️ Atributos

### [[pon_bid_item_prices|PON_BID_ITEM_PRICES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdvanceAmount | ADVANCE_AMOUNT | — | — |
| 2 | AlternateDispLineNumber | ALTERNATE_DISP_LINE_NUMBER | — | ✅ |
| 3 | AlternateLineDescription | ALTERNATE_LINE_DESCRIPTION | — | ✅ |
| 4 | AlternateLineFlag | ALTERNATE_LINE_FLAG | — | ✅ |
| 5 | AuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 6 | AuctionLineNumber | AUCTION_LINE_NUMBER | — | ✅ |
| 7 | AwardDate | AWARD_DATE | — | ✅ |
| 8 | AwardPrice | AWARD_PRICE | — | ✅ |
| 9 | AwardQuantity | AWARD_QUANTITY | — | ✅ |
| 10 | AwardShipmentNumber | AWARD_SHIPMENT_NUMBER | — | ✅ |
| 11 | AwardStatus | AWARD_STATUS | — | ✅ |
| 12 | BatchId | BATCH_ID | — | — |
| 13 | BidCurrAdvanceAmount | BID_CURR_ADVANCE_AMOUNT | — | — |
| 14 | BidCurrMaxRetainageAmt | BID_CURR_MAX_RETAINAGE_AMT | — | — |
| 15 | BidCurrencyLimitPrice | BID_CURRENCY_LIMIT_PRICE | — | ✅ |
| 16 | BidCurrencyPrice | BID_CURRENCY_PRICE | — | ✅ |
| 17 | BidCurrencyTransPrice | BID_CURRENCY_TRANS_PRICE | — | ✅ |
| 18 | BidCurrencyUnitPrice | BID_CURRENCY_UNIT_PRICE | — | ✅ |
| 19 | BidNumber | BID_NUMBER | 🔑 | ✅ |
| 20 | BidStartPrice | BID_START_PRICE | — | ✅ |
| 21 | CancelledLimitPrice | CANCELLED_LIMIT_PRICE | — | ✅ |
| 22 | CopyPriceForProxyFlag | COPY_PRICE_FOR_PROXY_FLAG | — | — |
| 23 | CreatedBy | CREATED_BY | — | ✅ |
| 24 | CreationDate | CREATION_DATE | — | ✅ |
| 25 | DisplayPriceFactorsFlag | DISPLAY_PRICE_FACTORS_FLAG | — | — |
| 26 | DocumentDispLineNumber | DOCUMENT_DISP_LINE_NUMBER | — | ✅ |
| 27 | FirstBidPrice | FIRST_BID_PRICE | — | — |
| 28 | FixedAmountComponent | FIXED_AMOUNT_COMPONENT | — | — |
| 29 | GroupAmount | GROUP_AMOUNT | — | ✅ |
| 30 | HasAttributesFlag | HAS_ATTRIBUTES_FLAG | — | — |
| 31 | HasBidFlag | HAS_BID_FLAG | — | — |
| 32 | HasBidPaymentsFlag | HAS_BID_PAYMENTS_FLAG | — | — |
| 33 | HasPriceDifferentialsFlag | HAS_PRICE_DIFFERENTIALS_FLAG | — | — |
| 34 | HasQuantityTiers | HAS_QUANTITY_TIERS | — | — |
| 35 | HasShipmentsFlag | HAS_SHIPMENTS_FLAG | — | — |
| 36 | InterfaceLineId | INTERFACE_LINE_ID | — | — |
| 37 | IsChangedLineFlag | IS_CHANGED_LINE_FLAG | — | — |
| 38 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 39 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 40 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 41 | LineNumber | LINE_NUMBER | 🔑 | ✅ |
| 42 | MaxAlternateDispLineNumber | MAX_ALTERNATE_DISP_LINE_NUMBER | — | ✅ |
| 43 | MaxRetainageAmount | MAX_RETAINAGE_AMOUNT | — | — |
| 44 | NoteToAuctionOwner | NOTE_TO_AUCTION_OWNER | — | ✅ |
| 45 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 46 | OldAlternateLineDescription | OLD_ALTERNATE_LINE_DESCRIPTION | — | ✅ |
| 47 | OldBidCurrAdvanceAmount | OLD_BID_CURR_ADVANCE_AMOUNT | — | — |
| 48 | OldBidCurrMaxRetainageAmt | OLD_BID_CURR_MAX_RETAINAGE_AMT | — | — |
| 49 | OldBidCurrencyLimitPrice | OLD_BID_CURRENCY_LIMIT_PRICE | — | ✅ |
| 50 | OldBidCurrencyPrice | OLD_BID_CURRENCY_PRICE | — | ✅ |
| 51 | OldBidCurrencyUnitPrice | OLD_BID_CURRENCY_UNIT_PRICE | — | ✅ |
| 52 | OldNoOfPayments | OLD_NO_OF_PAYMENTS | — | — |
| 53 | OldNoteToAuctionOwner | OLD_NOTE_TO_AUCTION_OWNER | — | ✅ |
| 54 | OldPoBidMinRelAmount | OLD_PO_BID_MIN_REL_AMOUNT | — | ✅ |
| 55 | OldPrice | OLD_PRICE | — | ✅ |
| 56 | OldProgressPymtRatePercent | OLD_PROGRESS_PYMT_RATE_PERCENT | — | — |
| 57 | OldPromisedDate | OLD_PROMISED_DATE | — | ✅ |
| 58 | OldPromisedDeliveryDate | OLD_PROMISED_DELIVERY_DATE | — | ✅ |
| 59 | OldPromisedShipDate | OLD_PROMISED_SHIP_DATE | — | ✅ |
| 60 | OldPublishDate | OLD_PUBLISH_DATE | — | ✅ |
| 61 | OldQuantity | OLD_QUANTITY | — | ✅ |
| 62 | OldRecoupmentRatePercent | OLD_RECOUPMENT_RATE_PERCENT | — | — |
| 63 | OldRetainageRatePercent | OLD_RETAINAGE_RATE_PERCENT | — | — |
| 64 | OldUomCode | OLD_UOM_CODE | — | ✅ |
| 65 | ParentLineNumber | PARENT_LINE_NUMBER | — | ✅ |
| 66 | PerUnitPriceComponent | PER_UNIT_PRICE_COMPONENT | — | ✅ |
| 67 | PoBidMinRelAmount | PO_BID_MIN_REL_AMOUNT | — | ✅ |
| 68 | PoMinRelAmount | PO_MIN_REL_AMOUNT | — | ✅ |
| 69 | Price | PRICE | — | ✅ |
| 70 | PriceBreakType | PRICE_BREAK_TYPE | — | ✅ |
| 71 | PriceDiffShipmentNumber | PRICE_DIFF_SHIPMENT_NUMBER | — | — |
| 72 | ProgramAppName | PROGRAM_APP_NAME | — | — |
| 73 | ProgramName | PROGRAM_NAME | — | — |
| 74 | ProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 75 | ProgressPymtRatePercent | PROGRESS_PYMT_RATE_PERCENT | — | — |
| 76 | PromisedDate | PROMISED_DATE | — | ✅ |
| 77 | PromisedDeliveryDate | PROMISED_DELIVERY_DATE | — | ✅ |
| 78 | PromisedShipDate | PROMISED_SHIP_DATE | — | ✅ |
| 79 | ProxyBidFlag | PROXY_BID_FLAG | — | ✅ |
| 80 | ProxyBidLimitPrice | PROXY_BID_LIMIT_PRICE | — | ✅ |
| 81 | PublishDate | PUBLISH_DATE | — | ✅ |
| 82 | PurchasingItemDesc | PURCHASING_ITEM_DESC | — | ✅ |
| 83 | PurchasingItemId | PURCHASING_ITEM_ID | — | ✅ |
| 84 | PurchasingItemRevision | PURCHASING_ITEM_REVISION | — | ✅ |
| 85 | Quantity | QUANTITY | — | ✅ |
| 86 | Rank | RANK | — | ✅ |
| 87 | RecoupmentRatePercent | RECOUPMENT_RATE_PERCENT | — | — |
| 88 | RequestId | REQUEST_ID | — | — |
| 89 | RetainageRatePercent | RETAINAGE_RATE_PERCENT | — | — |
| 90 | TotalWeightedScore | TOTAL_WEIGHTED_SCORE | — | ✅ |
| 91 | TriggerBidNumber | TRIGGER_BID_NUMBER | — | ✅ |
| 92 | UnitPrice | UNIT_PRICE | — | ✅ |
| 93 | UomCode | UOM_CODE | — | ✅ |
| 94 | UomConversionFactor | UOM_CONVERSION_FACTOR | — | ✅ |
| 95 | WorksheetName | WORKSHEET_NAME | — | — |
| 96 | WorksheetSequenceNumber | WORKSHEET_SEQUENCE_NUMBER | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
