---
id: DOC-PO-PVO-NegotiationResponseCostFactorExtractPVO
doc_type: system-doc
title: "NegotiationResponseCostFactorExtractPVO — PVO Purchasing"
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
  - NegotiationResponseCostFactorExtractPVO
  - negotiationresponsecostfactorextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationResponseCostFactorExtractPVO

## 📌 Visão Geral

Extrai os fatores de custo das respostas de fornecedores (frete, impostos, seguros) para carga BICC. Permite análise de custo total de propriedade (TCO) além do preço unitário.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.NegotiationResponseCostFactorExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 1 | 3 | 23 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pon_bid_price_elements|PON_BID_PRICE_ELEMENTS]] — 23 atributos (3 PKs, 23 BICC)

---

## ⚙️ Atributos

### [[pon_bid_price_elements|PON_BID_PRICE_ELEMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AuctionCurrencyValue | AUCTION_CURRENCY_VALUE | — | ✅ |
| 2 | AuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 3 | AuctionLineNumber | AUCTION_LINE_NUMBER | — | ✅ |
| 4 | BatchId | BATCH_ID | — | ✅ |
| 5 | BidCurrencyValue | BID_CURRENCY_VALUE | — | ✅ |
| 6 | BidNumber | BID_NUMBER | 🔑 | ✅ |
| 7 | CreatedBy | CREATED_BY | — | ✅ |
| 8 | CreationDate | CREATION_DATE | — | ✅ |
| 9 | InterfaceLineId | INTERFACE_LINE_ID | — | ✅ |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | LineNumber | LINE_NUMBER | 🔑 | ✅ |
| 14 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | OldBidCurrencyValue | OLD_BID_CURRENCY_VALUE | — | ✅ |
| 16 | PfType | PF_TYPE | — | ✅ |
| 17 | PriceElementTypeId | PRICE_ELEMENT_TYPE_ID | — | ✅ |
| 18 | PricingBasis | PRICING_BASIS | — | ✅ |
| 19 | ProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 20 | ProgramName | PROGRAM_NAME | — | ✅ |
| 21 | ProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 22 | RequestId | REQUEST_ID | — | ✅ |
| 23 | SequenceNumber | SEQUENCE_NUMBER | 🔑 | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
