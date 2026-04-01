---
id: DOC-PO-PVO-NegotiationPriceTierExtractPVO
doc_type: system-doc
title: "NegotiationPriceTierExtractPVO — PVO Purchasing"
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
  - NegotiationPriceTierExtractPVO
  - negotiationpricetierextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationPriceTierExtractPVO

## 📌 Visão Geral

Extrai as faixas de preço (price tiers) configuradas em negociações para carga BICC, com quebras por volume. Alimenta análises de estratégia de precificação e economia por escala.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.NegotiationPriceTierExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 1 | 3 | 20 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pon_auction_shipments_all|PON_AUCTION_SHIPMENTS_ALL]] — 20 atributos (3 PKs, 20 BICC)

---

## ⚙️ Atributos

### [[pon_auction_shipments_all|PON_AUCTION_SHIPMENTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AuctionHeaderId | AUCTION_HEADER_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | DifferentialResponseType | DIFFERENTIAL_RESPONSE_TYPE | — | ✅ |
| 5 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 6 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | HasPriceDifferentialsFlag | HAS_PRICE_DIFFERENTIALS_FLAG | — | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | LineNumber | LINE_NUMBER | 🔑 | ✅ |
| 12 | MaxQuantity | MAX_QUANTITY | — | ✅ |
| 13 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | PrcBuId | PRC_BU_ID | — | ✅ |
| 15 | Price | PRICE | — | ✅ |
| 16 | Quantity | QUANTITY | — | ✅ |
| 17 | ShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 18 | ShipToOrganizationId | SHIP_TO_ORGANIZATION_ID | — | ✅ |
| 19 | ShipmentNumber | SHIPMENT_NUMBER | 🔑 | ✅ |
| 20 | ShipmentType | SHIPMENT_TYPE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
