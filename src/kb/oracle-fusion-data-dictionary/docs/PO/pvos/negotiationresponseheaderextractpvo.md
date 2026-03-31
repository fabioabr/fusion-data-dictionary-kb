---
id: DOC-PO-PVO-NegotiationResponseHeaderExtractPVO
doc_type: system-doc
title: "NegotiationResponseHeaderExtractPVO — PVO Purchasing"
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
  - NegotiationResponseHeaderExtractPVO
  - negotiationresponseheaderextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationResponseHeaderExtractPVO

## 📌 Visão Geral

Extrai os cabeçalhos de respostas (propostas/lances) de fornecedores em negociações para carga BICC. Permite análise de competitividade, taxa de participação e valores totais por proposta.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.NegotiationResponseHeaderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 94 | 1 | 1 | 77 | 82% |

---

## 🔗 Tabelas Relacionadas

- [[pon_bid_headers|PON_BID_HEADERS]] — 94 atributos (1 PKs, 77 BICC)

---

## ⚙️ Atributos

### [[pon_bid_headers|PON_BID_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AttributeLineNumber | ATTRIBUTE_LINE_NUMBER | — | ✅ |
| 2 | AuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 3 | AwardDate | AWARD_DATE | — | ✅ |
| 4 | AwardStatus | AWARD_STATUS | — | ✅ |
| 5 | BidCurrencyCode | BID_CURRENCY_CODE | — | ✅ |
| 6 | BidCurrencyMinBidChange | BID_CURRENCY_MIN_BID_CHANGE | — | ✅ |
| 7 | BidExpirationDate | BID_EXPIRATION_DATE | — | ✅ |
| 8 | BidNumber | BID_NUMBER | 🔑 | ✅ |
| 9 | BidStatus | BID_STATUS | — | ✅ |
| 10 | BiddersBidNumber | BIDDERS_BID_NUMBER | — | ✅ |
| 11 | BuyerBidTotal | BUYER_BID_TOTAL | — | ✅ |
| 12 | BuyerBidTransformedTotal | BUYER_BID_TRANSFORMED_TOTAL | — | ✅ |
| 13 | CancelReason | CANCEL_REASON | — | ✅ |
| 14 | CancelledDate | CANCELLED_DATE | — | ✅ |
| 15 | ColorSequenceId | COLOR_SEQUENCE_ID | — | — |
| 16 | ContractErrorMsg | CONTRACT_ERROR_MSG | — | — |
| 17 | ContractId | CONTRACT_ID | — | — |
| 18 | ContractLinesFlag | CONTRACT_LINES_FLAG | — | — |
| 19 | CreatedBy | CREATED_BY | — | ✅ |
| 20 | CreationDate | CREATION_DATE | — | ✅ |
| 21 | CurrentRebate | CURRENT_REBATE | — | — |
| 22 | CurrentTotalSpend | CURRENT_TOTAL_SPEND | — | — |
| 23 | DisplayPriceFactorsFlag | DISPLAY_PRICE_FACTORS_FLAG | — | ✅ |
| 24 | DisqualifyReason | DISQUALIFY_REASON | — | ✅ |
| 25 | DraftLocked | DRAFT_LOCKED | — | ✅ |
| 26 | DraftLockedBy | DRAFT_LOCKED_BY | — | ✅ |
| 27 | DraftLockedByContactId | DRAFT_LOCKED_BY_CONTACT_ID | — | ✅ |
| 28 | DraftLockedDate | DRAFT_LOCKED_DATE | — | ✅ |
| 29 | DraftUnlockedBy | DRAFT_UNLOCKED_BY | — | ✅ |
| 30 | DraftUnlockedByContactId | DRAFT_UNLOCKED_BY_CONTACT_ID | — | ✅ |
| 31 | DraftUnlockedDate | DRAFT_UNLOCKED_DATE | — | ✅ |
| 32 | FixedIncentive | FIXED_INCENTIVE | — | — |
| 33 | HasRebateTiers | HAS_REBATE_TIERS | — | — |
| 34 | ImportFileName | IMPORT_FILE_NAME | — | — |
| 35 | IncumbentFlag | INCUMBENT_FLAG | — | — |
| 36 | InternalNote | INTERNAL_NOTE | — | ✅ |
| 37 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 38 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 39 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 40 | MaxInternalLineNum | MAX_INTERNAL_LINE_NUM | — | ✅ |
| 41 | MinBidChange | MIN_BID_CHANGE | — | ✅ |
| 42 | NoteToAuctionOwner | NOTE_TO_AUCTION_OWNER | — | ✅ |
| 43 | NoteToSupplier | NOTE_TO_SUPPLIER | — | ✅ |
| 44 | NumberPriceDecimals | NUMBER_PRICE_DECIMALS | — | ✅ |
| 45 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 46 | OldBidCurrMinBidChange | OLD_BID_CURR_MIN_BID_CHANGE | — | ✅ |
| 47 | OldBidExpirationDate | OLD_BID_EXPIRATION_DATE | — | ✅ |
| 48 | OldBidNumber | OLD_BID_NUMBER | — | ✅ |
| 49 | OldBidStatus | OLD_BID_STATUS | — | ✅ |
| 50 | OldBiddersBidNumber | OLD_BIDDERS_BID_NUMBER | — | ✅ |
| 51 | OldMinBidChange | OLD_MIN_BID_CHANGE | — | ✅ |
| 52 | OldNoteToAuctionOwner | OLD_NOTE_TO_AUCTION_OWNER | — | ✅ |
| 53 | OldSurrogBidReceiptDate | OLD_SURROG_BID_RECEIPT_DATE | — | ✅ |
| 54 | OriginalBidNumber | ORIGINAL_BID_NUMBER | — | ✅ |
| 55 | OverridenScore | OVERRIDEN_SCORE | — | ✅ |
| 56 | PartialResponseFlag | PARTIAL_RESPONSE_FLAG | — | ✅ |
| 57 | PoAgreedAmount | PO_AGREED_AMOUNT | — | ✅ |
| 58 | PoqTransferStatus | POQ_TRANSFER_STATUS | — | ✅ |
| 59 | ProgramAppName | PROGRAM_APP_NAME | — | — |
| 60 | ProgramName | PROGRAM_NAME | — | — |
| 61 | ProxyBidFlag | PROXY_BID_FLAG | — | ✅ |
| 62 | PublishDate | PUBLISH_DATE | — | ✅ |
| 63 | Rate | RATE | — | ✅ |
| 64 | RateDate | RATE_DATE | — | ✅ |
| 65 | RateDsp | RATE_DSP | — | ✅ |
| 66 | RateType | RATE_TYPE | — | ✅ |
| 67 | RequestDate | REQUEST_DATE | — | — |
| 68 | RequestId | REQUEST_ID | — | — |
| 69 | RequestedBy | REQUESTED_BY | — | — |
| 70 | ScoreOverridePersonId | SCORE_OVERRIDE_PERSON_ID | — | ✅ |
| 71 | ScoreOverrideReason | SCORE_OVERRIDE_REASON | — | ✅ |
| 72 | ScoreOverridenDate | SCORE_OVERRIDEN_DATE | — | ✅ |
| 73 | ScoreOverridenFlag | SCORE_OVERRIDEN_FLAG | — | ✅ |
| 74 | ScoringStatus | SCORING_STATUS | — | ✅ |
| 75 | ShortlistBuyerId | SHORTLIST_BUYER_ID | — | ✅ |
| 76 | ShortlistFlag | SHORTLIST_FLAG | — | ✅ |
| 77 | SubmitStage | SUBMIT_STAGE | — | — |
| 78 | SurrogBidCreatedPersonId | SURROG_BID_CREATED_PERSON_ID | — | ✅ |
| 79 | SurrogBidFlag | SURROG_BID_FLAG | — | ✅ |
| 80 | SurrogBidOnlineEntryDate | SURROG_BID_ONLINE_ENTRY_DATE | — | ✅ |
| 81 | SurrogBidReceiptDate | SURROG_BID_RECEIPT_DATE | — | ✅ |
| 82 | SurrogDraftLockPersonId | SURROG_DRAFT_LOCK_PERSON_ID | — | ✅ |
| 83 | SurrogDraftUnlockPersonId | SURROG_DRAFT_UNLOCK_PERSON_ID | — | ✅ |
| 84 | SurrogMethodOfResponse | SURROG_METHOD_OF_RESPONSE | — | ✅ |
| 85 | TechnicalScoringStatus | TECHNICAL_SCORING_STATUS | — | ✅ |
| 86 | TechnicalShortlistFlag | TECHNICAL_SHORTLIST_FLAG | — | — |
| 87 | TotalAwardAmount | TOTAL_AWARD_AMOUNT | — | ✅ |
| 88 | TradingPartnerContactId | TRADING_PARTNER_CONTACT_ID | — | ✅ |
| 89 | TradingPartnerId | TRADING_PARTNER_ID | — | ✅ |
| 90 | TransformedRank | TRANSFORMED_RANK | — | ✅ |
| 91 | TypeOfResponse | TYPE_OF_RESPONSE | — | ✅ |
| 92 | VendorId | VENDOR_ID | — | ✅ |
| 93 | VendorSiteCode | VENDOR_SITE_CODE | — | ✅ |
| 94 | VendorSiteId | VENDOR_SITE_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
