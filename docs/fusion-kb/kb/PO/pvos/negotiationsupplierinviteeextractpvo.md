---
id: DOC-PO-PVO-NegotiationSupplierInviteeExtractPVO
doc_type: system-doc
title: "NegotiationSupplierInviteeExtractPVO — PVO Purchasing"
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
  - NegotiationSupplierInviteeExtractPVO
  - negotiationsupplierinviteeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationSupplierInviteeExtractPVO

## 📌 Visão Geral

Extrai os fornecedores convidados para negociações, incluindo dados de registro e status de convite. Permite análise de abrangência de mercado e rastreabilidade de convites em processos competitivos.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.NegotiationSupplierInviteeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 87 | 2 | 3 | 83 | 95% |

---

## 🔗 Tabelas Relacionadas

- [[pon_bidding_parties|PON_BIDDING_PARTIES]] — 34 atributos (3 PKs, 30 BICC)
- [[poz_supplier_registrations|POZ_SUPPLIER_REGISTRATIONS]] — 53 atributos (53 BICC)

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
| 14 | ListId | LIST_ID | 🔑 | — |
| 15 | ModifiedFlag | MODIFIED_FLAG | — | — |
| 16 | NumberPriceDecimals | NUMBER_PRICE_DECIMALS | — | ✅ |
| 17 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | Rate | RATE | — | ✅ |
| 19 | RateDsp | RATE_DSP | — | ✅ |
| 20 | RegistrationId | REGISTRATION_ID | — | ✅ |
| 21 | RequestedSuppContactName | REQUESTED_SUPP_CONTACT_NAME | — | ✅ |
| 22 | RequestedSupplierContactId | REQUESTED_SUPPLIER_CONTACT_ID | — | ✅ |
| 23 | RequestedSupplierId | REQUESTED_SUPPLIER_ID | — | ✅ |
| 24 | RequestedSupplierName | REQUESTED_SUPPLIER_NAME | — | ✅ |
| 25 | RoundNumber | ROUND_NUMBER | — | ✅ |
| 26 | Sequence | SEQUENCE | 🔑 | ✅ |
| 27 | SuppAcknowledgement | SUPP_ACKNOWLEDGEMENT | — | ✅ |
| 28 | SurrogBidAckFlag | SURROG_BID_ACK_FLAG | — | ✅ |
| 29 | SurrogBidAckPersonId | SURROG_BID_ACK_PERSON_ID | — | ✅ |
| 30 | TradingPartnerContactId | TRADING_PARTNER_CONTACT_ID | — | ✅ |
| 31 | TradingPartnerId | TRADING_PARTNER_ID | — | ✅ |
| 32 | VendorSiteId | VENDOR_SITE_ID | — | ✅ |
| 33 | WfItemKey | WF_ITEM_KEY | — | — |
| 34 | WfUserName | WF_USER_NAME | — | — |

### [[poz_supplier_registrations|POZ_SUPPLIER_REGISTRATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddressLine1 | ADDRESS_LINE1 | — | ✅ |
| 2 | AddressLine2 | ADDRESS_LINE2 | — | ✅ |
| 3 | AddressLine3 | ADDRESS_LINE3 | — | ✅ |
| 4 | AddressLine4 | ADDRESS_LINE4 | — | ✅ |
| 5 | AddressNickname | ADDRESS_NICKNAME | — | ✅ |
| 6 | ApprovedDate | APPROVED_DATE | — | ✅ |
| 7 | BusinessRelationshipCode | BUSINESS_RELATIONSHIP_CODE | — | ✅ |
| 8 | City | CITY | — | ✅ |
| 9 | CorporateWebsite | CORPORATE_WEBSITE | — | ✅ |
| 10 | Country | COUNTRY | — | ✅ |
| 11 | County | COUNTY | — | ✅ |
| 12 | CreatedBy1 | CREATED_BY | — | ✅ |
| 13 | CreationDate1 | CREATION_DATE | — | ✅ |
| 14 | DunsNumber | DUNS_NUMBER | — | ✅ |
| 15 | IncomeTaxIdFlag | INCOME_TAX_ID_FLAG | — | ✅ |
| 16 | Justification | JUSTIFICATION | — | ✅ |
| 17 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 18 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 19 | LastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 20 | NoteFromSupplier | NOTE_FROM_SUPPLIER | — | ✅ |
| 21 | NoteToApprover | NOTE_TO_APPROVER | — | ✅ |
| 22 | NoteToSupplier | NOTE_TO_SUPPLIER | — | ✅ |
| 23 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | ✅ |
| 24 | OrganizationType | ORGANIZATION_TYPE | — | ✅ |
| 25 | PostalCode | POSTAL_CODE | — | ✅ |
| 26 | PrcBuId | PRC_BU_ID | — | ✅ |
| 27 | Province | PROVINCE | — | ✅ |
| 28 | RegKey | REG_KEY | — | ✅ |
| 29 | RegistrationStatus | REGISTRATION_STATUS | — | ✅ |
| 30 | RegistrationType | REGISTRATION_TYPE | — | ✅ |
| 31 | RejectionCode | REJECTION_CODE | — | ✅ |
| 32 | RequestNumber | REQUEST_NUMBER | — | ✅ |
| 33 | RequestReasonCode | REQUEST_REASON_CODE | — | ✅ |
| 34 | RequestedDate | REQUESTED_DATE | — | ✅ |
| 35 | RequesterEmailAddress | REQUESTER_EMAIL_ADDRESS | — | ✅ |
| 36 | RequesterFirstName | REQUESTER_FIRST_NAME | — | ✅ |
| 37 | RequesterLanguage | REQUESTER_LANGUAGE | — | ✅ |
| 38 | RequesterLastName | REQUESTER_LAST_NAME | — | ✅ |
| 39 | RequesterPersonId | REQUESTER_PERSON_ID | — | ✅ |
| 40 | State | STATE | — | ✅ |
| 41 | SupplierCreationStatus | SUPPLIER_CREATION_STATUS | — | ✅ |
| 42 | SupplierName | SUPPLIER_NAME | — | ✅ |
| 43 | SupplierNumber | SUPPLIER_NUMBER | — | ✅ |
| 44 | SupplierRegId | SUPPLIER_REG_ID | — | ✅ |
| 45 | TaxRegCountryCode | TAX_REG_COUNTRY_CODE | — | ✅ |
| 46 | TaxRegNumberFlag | TAX_REG_NUMBER_FLAG | — | ✅ |
| 47 | TaxRegType | TAX_REG_TYPE | — | ✅ |
| 48 | TaxRegistrationNumber | TAX_REGISTRATION_NUMBER | — | ✅ |
| 49 | TaxpayerId | TAXPAYER_ID | — | ✅ |
| 50 | UserRegId | USER_REG_ID | — | ✅ |
| 51 | VendorId | VENDOR_ID | — | ✅ |
| 52 | VendorPartyId | VENDOR_PARTY_ID | — | ✅ |
| 53 | VendorTypeLookupCode | VENDOR_TYPE_LOOKUP_CODE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
