---
id: DOC-PO-PVO-NegotiationResponsePriceTierExtractPVO
doc_type: system-doc
title: "NegotiationResponsePriceTierExtractPVO — PVO Purchasing"
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
  - NegotiationResponsePriceTierExtractPVO
  - negotiationresponsepricetierextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationResponsePriceTierExtractPVO

## 📌 Visão Geral

Extrai faixas de preço das respostas de fornecedores em negociações para carga BICC. Permite identificar descontos por volume oferecidos e oportunidades de consolidação.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.NegotiationResponsePriceTierExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 38 | 1 | 3 | 38 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pon_bid_shipments|PON_BID_SHIPMENTS]] — 38 atributos (3 PKs, 38 BICC)

---

## ⚙️ Atributos

### [[pon_bid_shipments|PON_BID_SHIPMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 2 | AuctionLineNumber | AUCTION_LINE_NUMBER | — | ✅ |
| 3 | AuctionShipmentNumber | AUCTION_SHIPMENT_NUMBER | — | ✅ |
| 4 | BidCurrencyPrice | BID_CURRENCY_PRICE | — | ✅ |
| 5 | BidCurrencyUnitPrice | BID_CURRENCY_UNIT_PRICE | — | ✅ |
| 6 | BidNumber | BID_NUMBER | 🔑 | ✅ |
| 7 | CreatedBy | CREATED_BY | — | ✅ |
| 8 | CreationDate | CREATION_DATE | — | ✅ |
| 9 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 10 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 11 | HasPriceDifferentialsFlag | HAS_PRICE_DIFFERENTIALS_FLAG | — | ✅ |
| 12 | InterfaceLineId | INTERFACE_LINE_ID | — | ✅ |
| 13 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | LineNumber | LINE_NUMBER | 🔑 | ✅ |
| 17 | MaxQuantity | MAX_QUANTITY | — | ✅ |
| 18 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 19 | OldBidCurrencyPrice | OLD_BID_CURRENCY_PRICE | — | ✅ |
| 20 | OldBidCurrencyUnitPrice | OLD_BID_CURRENCY_UNIT_PRICE | — | ✅ |
| 21 | OldEffectiveEndDate | OLD_EFFECTIVE_END_DATE | — | ✅ |
| 22 | OldEffectiveStartDate | OLD_EFFECTIVE_START_DATE | — | ✅ |
| 23 | OldMaxQuantity | OLD_MAX_QUANTITY | — | ✅ |
| 24 | OldPriceDiscount | OLD_PRICE_DISCOUNT | — | ✅ |
| 25 | OldPriceType | OLD_PRICE_TYPE | — | ✅ |
| 26 | OldQuantity | OLD_QUANTITY | — | ✅ |
| 27 | OldShipToLocId | OLD_SHIP_TO_LOC_ID | — | ✅ |
| 28 | OldShipToOrgId | OLD_SHIP_TO_ORG_ID | — | ✅ |
| 29 | PerUnitPriceComponent | PER_UNIT_PRICE_COMPONENT | — | ✅ |
| 30 | Price | PRICE | — | ✅ |
| 31 | PriceDiscount | PRICE_DISCOUNT | — | ✅ |
| 32 | PriceType | PRICE_TYPE | — | ✅ |
| 33 | Quantity | QUANTITY | — | ✅ |
| 34 | ShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 35 | ShipToOrganizationId | SHIP_TO_ORGANIZATION_ID | — | ✅ |
| 36 | ShipmentNumber | SHIPMENT_NUMBER | 🔑 | ✅ |
| 37 | ShipmentType | SHIPMENT_TYPE | — | ✅ |
| 38 | UnitPrice | UNIT_PRICE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
