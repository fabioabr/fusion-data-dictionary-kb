---
id: DOC-PO-PVO-NegotiationSupplierInviteesExtractPVO
doc_type: system-doc
title: "NegotiationSupplierInviteesExtractPVO — PVO Purchasing"
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
  - NegotiationSupplierInviteesExtractPVO
  - negotiationsupplierinviteesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationSupplierInviteesExtractPVO

## 📌 Visão Geral

Extrai lista expandida de fornecedores convidados para negociações para carga BICC, com detalhes de comunicação e participação. Alimenta análises de engajamento e cobertura de fornecedores.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.NegotiationSupplierInviteesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 35 | 1 | 3 | 35 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pon_bidding_parties|PON_BIDDING_PARTIES]] — 35 atributos (3 PKs, 35 BICC)

---

## ⚙️ Atributos

### [[pon_bidding_parties|PON_BIDDING_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccessType | ACCESS_TYPE | — | ✅ |
| 2 | AckNoteToAuctioneer | ACK_NOTE_TO_AUCTIONEER | — | ✅ |
| 3 | AckPartnerContactId | ACK_PARTNER_CONTACT_ID | — | ✅ |
| 4 | AcknowledgementTime | ACKNOWLEDGEMENT_TIME | — | ✅ |
| 5 | AdditionalContactEmail | ADDITIONAL_CONTACT_EMAIL | — | ✅ |
| 6 | AuctionHeaderId | AUCTION_HEADER_ID | 🔑 | ✅ |
| 7 | BidCurrencyCode | BID_CURRENCY_CODE | — | ✅ |
| 8 | CreatedBy | CREATED_BY | — | ✅ |
| 9 | CreationDate | CREATION_DATE | — | ✅ |
| 10 | LastAmendmentUpdate | LAST_AMENDMENT_UPDATE | — | ✅ |
| 11 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | ListId | LIST_ID | 🔑 | ✅ |
| 15 | ModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 16 | NotifyContactsFlag | NOTIFY_CONTACTS_FLAG | — | ✅ |
| 17 | NumberPriceDecimals | NUMBER_PRICE_DECIMALS | — | ✅ |
| 18 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 19 | Rate | RATE | — | ✅ |
| 20 | RateDsp | RATE_DSP | — | ✅ |
| 21 | RegistrationId | REGISTRATION_ID | — | ✅ |
| 22 | RequestedSuppContactName | REQUESTED_SUPP_CONTACT_NAME | — | ✅ |
| 23 | RequestedSupplierContactId | REQUESTED_SUPPLIER_CONTACT_ID | — | ✅ |
| 24 | RequestedSupplierId | REQUESTED_SUPPLIER_ID | — | ✅ |
| 25 | RequestedSupplierName | REQUESTED_SUPPLIER_NAME | — | ✅ |
| 26 | RoundNumber | ROUND_NUMBER | — | ✅ |
| 27 | Sequence | SEQUENCE | 🔑 | ✅ |
| 28 | SuppAcknowledgement | SUPP_ACKNOWLEDGEMENT | — | ✅ |
| 29 | SurrogBidAckFlag | SURROG_BID_ACK_FLAG | — | ✅ |
| 30 | SurrogBidAckPersonId | SURROG_BID_ACK_PERSON_ID | — | ✅ |
| 31 | TradingPartnerContactId | TRADING_PARTNER_CONTACT_ID | — | ✅ |
| 32 | TradingPartnerId | TRADING_PARTNER_ID | — | ✅ |
| 33 | VendorSiteId | VENDOR_SITE_ID | — | ✅ |
| 34 | WfItemKey | WF_ITEM_KEY | — | ✅ |
| 35 | WfUserName | WF_USER_NAME | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
