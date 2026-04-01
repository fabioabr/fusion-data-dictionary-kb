---
id: DOC-PO-PVO-NegotiationResponsePriceTierPVO
doc_type: system-doc
title: "NegotiationResponsePriceTierPVO — PVO Purchasing"
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
  - NegotiationResponsePriceTierPVO
  - negotiationresponsepricetierpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationResponsePriceTierPVO

## 📌 Visão Geral

Disponibiliza faixas de preço de respostas de fornecedores para consulta, facilitando comparação de descontos por volume entre propostas concorrentes.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.NegotiationResponsePriceTierPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 638 | 7 | 3 | 638 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[egp_categories_vl|EGP_CATEGORIES_VL]] — 8 atributos (8 BICC)
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 26 atributos (26 BICC)
- [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]] — 215 atributos (215 BICC)
- [[pon_auction_item_prices_all|PON_AUCTION_ITEM_PRICES_ALL]] — 190 atributos (190 BICC)
- [[pon_bid_headers|PON_BID_HEADERS]] — 74 atributos (74 BICC)
- [[pon_bid_item_prices|PON_BID_ITEM_PRICES]] — 88 atributos (88 BICC)
- [[pon_bid_shipments|PON_BID_SHIPMENTS]] — 37 atributos (3 PKs, 37 BICC)

---

## ⚙️ Atributos

### [[egp_categories_vl|EGP_CATEGORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryCategoryId | CATEGORY_ID | — | ✅ |
| 2 | CategoryCategoryName | CATEGORY_NAME | — | ✅ |
| 3 | CategoryDescription | DESCRIPTION | — | ✅ |
| 4 | CategoryEnabledFlag | ENABLED_FLAG | — | ✅ |
| 5 | CategoryJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 6 | CategoryJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 7 | CategoryStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | ✅ |
| 8 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | ✅ |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DailyConversionTypeNegoHdrConversionType | CONVERSION_TYPE | — | ✅ |
| 2 | DailyConversionTypeNegoHdrDescription | DESCRIPTION | — | ✅ |
| 3 | DailyConversionTypeNegoHdrEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | ✅ |
| 4 | DailyConversionTypeNegoHdrEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | ✅ |
| 5 | DailyConversionTypeNegoHdrFemEnabledFlag | FEM_ENABLED_FLAG | — | ✅ |
| 6 | DailyConversionTypeNegoHdrFemRateTypeCode | FEM_RATE_TYPE_CODE | — | ✅ |
| 7 | DailyConversionTypeNegoHdrFemScenario | FEM_SCENARIO | — | ✅ |
| 8 | DailyConversionTypeNegoHdrFemTimeframe | FEM_TIMEFRAME | — | ✅ |
| 9 | DailyConversionTypeNegoHdrPivotCurrencyCode | PIVOT_CURRENCY_CODE | — | ✅ |
| 10 | DailyConversionTypeNegoHdrSecurityFlag | SECURITY_FLAG | — | ✅ |
| 11 | DailyConversionTypeNegoHdrUserConversionType | USER_CONVERSION_TYPE | — | ✅ |
| 12 | DailyConversionTypeNegoHdrUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | ✅ |
| 13 | DailyConversionTypeResHdrConversionType | CONVERSION_TYPE | — | ✅ |
| 14 | DailyConversionTypeResHdrDescription | DESCRIPTION | — | ✅ |
| 15 | DailyConversionTypeResHdrEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | ✅ |
| 16 | DailyConversionTypeResHdrEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | ✅ |
| 17 | DailyConversionTypeResHdrFemEnabledFlag | FEM_ENABLED_FLAG | — | ✅ |
| 18 | DailyConversionTypeResHdrFemRateTypeCode | FEM_RATE_TYPE_CODE | — | ✅ |
| 19 | DailyConversionTypeResHdrFemScenario | FEM_SCENARIO | — | ✅ |
| 20 | DailyConversionTypeResHdrFemTimeframe | FEM_TIMEFRAME | — | ✅ |
| 21 | DailyConversionTypeResHdrPivotCurrencyCode | PIVOT_CURRENCY_CODE | — | ✅ |
| 22 | DailyConversionTypeResHdrSecurityFlag | SECURITY_FLAG | — | ✅ |
| 23 | DailyConversionTypeResHdrUserConversionType | USER_CONVERSION_TYPE | — | ✅ |
| 24 | DailyConversionTypeResHdrUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | ✅ |
| 25 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 26 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | ✅ |

### [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllowAlternateLines | ALLOW_ALTERNATE_LINES | — | ✅ |
| 2 | BidRevisionType | BID_REVISION_TYPE | — | ✅ |
| 3 | BidRevisionTypeDspFlag | BID_REVISION_TYPE_DSP_FLAG | — | ✅ |
| 4 | NegotiationHeaderAbstractDetails | ABSTRACT_DETAILS | — | ✅ |
| 5 | NegotiationHeaderAbstractStatus | ABSTRACT_STATUS | — | ✅ |
| 6 | NegotiationHeaderAdvanceNegotiableFlag | ADVANCE_NEGOTIABLE_FLAG | — | ✅ |
| 7 | NegotiationHeaderAllowOtherBidCurrencyFlag | ALLOW_OTHER_BID_CURRENCY_FLAG | — | ✅ |
| 8 | NegotiationHeaderAmendmentDescription | AMENDMENT_DESCRIPTION | — | ✅ |
| 9 | NegotiationHeaderAmendmentNumber | AMENDMENT_NUMBER | — | ✅ |
| 10 | NegotiationHeaderApprovalStatus | NEG_APPROVAL_STATUS | — | ✅ |
| 11 | NegotiationHeaderAttributeLineNumber | ATTRIBUTE_LINE_NUMBER | — | ✅ |
| 12 | NegotiationHeaderAttributesExist | ATTRIBUTES_EXIST | — | ✅ |
| 13 | NegotiationHeaderAuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 14 | NegotiationHeaderAuctionHeaderIdOrigAmend | AUCTION_HEADER_ID_ORIG_AMEND | — | ✅ |
| 15 | NegotiationHeaderAuctionHeaderIdOrigRound | AUCTION_HEADER_ID_ORIG_ROUND | — | ✅ |
| 16 | NegotiationHeaderAuctionHeaderIdPrevAmend | AUCTION_HEADER_ID_PREV_AMEND | — | ✅ |
| 17 | NegotiationHeaderAuctionHeaderIdPrevRound | AUCTION_HEADER_ID_PREV_ROUND | — | ✅ |
| 18 | NegotiationHeaderAuctionOriginationCode | AUCTION_ORIGINATION_CODE | — | ✅ |
| 19 | NegotiationHeaderAuctionRoundNumber | AUCTION_ROUND_NUMBER | — | ✅ |
| 20 | NegotiationHeaderAuctionStatus | AUCTION_STATUS | — | ✅ |
| 21 | NegotiationHeaderAuctionTitle | AUCTION_TITLE | — | ✅ |
| 22 | NegotiationHeaderAutoExtendAllLinesFlag | AUTO_EXTEND_ALL_LINES_FLAG | — | ✅ |
| 23 | NegotiationHeaderAutoExtendDuration | AUTO_EXTEND_DURATION | — | ✅ |
| 24 | NegotiationHeaderAutoExtendEnabledFlag | AUTO_EXTEND_ENABLED_FLAG | — | ✅ |
| 25 | NegotiationHeaderAutoExtendFlag | AUTO_EXTEND_FLAG | — | ✅ |
| 26 | NegotiationHeaderAutoExtendMinTriggerRank | AUTO_EXTEND_MIN_TRIGGER_RANK | — | ✅ |
| 27 | NegotiationHeaderAutoExtendNumber | AUTO_EXTEND_NUMBER | — | ✅ |
| 28 | NegotiationHeaderAutoExtendTypeFlag | AUTO_EXTEND_TYPE_FLAG | — | ✅ |
| 29 | NegotiationHeaderAutoextendChangedFlag | AUTOEXTEND_CHANGED_FLAG | — | ✅ |
| 30 | NegotiationHeaderAwardApprAmeTransId | AWARD_APPR_AME_TRANS_ID | — | ✅ |
| 31 | NegotiationHeaderAwardApprAmeTransPrevId | AWARD_APPR_AME_TRANS_PREV_ID | — | ✅ |
| 32 | NegotiationHeaderAwardApprAmeTxnDate | AWARD_APPR_AME_TXN_DATE | — | ✅ |
| 33 | NegotiationHeaderAwardApprovalFlag | AWARD_APPROVAL_FLAG | — | ✅ |
| 34 | NegotiationHeaderAwardApprovalStatus | AWARD_APPROVAL_STATUS | — | ✅ |
| 35 | NegotiationHeaderAwardByDate | AWARD_BY_DATE | — | ✅ |
| 36 | NegotiationHeaderAwardCompleteDate | AWARD_COMPLETE_DATE | — | ✅ |
| 37 | NegotiationHeaderAwardDate | AWARD_DATE | — | ✅ |
| 38 | NegotiationHeaderAwardMode | AWARD_MODE | — | ✅ |
| 39 | NegotiationHeaderAwardStatus | AWARD_STATUS | — | ✅ |
| 40 | NegotiationHeaderBidDecrementMethod | BID_DECREMENT_METHOD | — | ✅ |
| 41 | NegotiationHeaderBidFrequencyCode | BID_FREQUENCY_CODE | — | ✅ |
| 42 | NegotiationHeaderBidListType | BID_LIST_TYPE | — | ✅ |
| 43 | NegotiationHeaderBidRanking | BID_RANKING | — | ✅ |
| 44 | NegotiationHeaderBidScopeCode | BID_SCOPE_CODE | — | ✅ |
| 45 | NegotiationHeaderBidVisibilityCode | BID_VISIBILITY_CODE | — | ✅ |
| 46 | NegotiationHeaderBuyerTransportEnabledFlag | BUYER_TRANSPORT_ENABLED_FLAG | — | ✅ |
| 47 | NegotiationHeaderBuyerTransportFlag | BUYER_TRANSPORT_FLAG | — | ✅ |
| 48 | NegotiationHeaderCancelDate | CANCEL_DATE | — | ✅ |
| 49 | NegotiationHeaderCarrierId | CARRIER_ID | — | ✅ |
| 50 | NegotiationHeaderCloseBiddingDate | CLOSE_BIDDING_DATE | — | ✅ |
| 51 | NegotiationHeaderCompleteFlag | COMPLETE_FLAG | — | ✅ |
| 52 | NegotiationHeaderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | ✅ |
| 53 | NegotiationHeaderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | ✅ |
| 54 | NegotiationHeaderContermsExistFlag | CONTERMS_EXIST_FLAG | — | ✅ |
| 55 | NegotiationHeaderContractTemplateId | CONTRACT_TEMPLATE_ID | — | ✅ |
| 56 | NegotiationHeaderContractType | CONTRACT_TYPE | — | ✅ |
| 57 | NegotiationHeaderCreatedBy | CREATED_BY | — | ✅ |
| 58 | NegotiationHeaderCreationDate | CREATION_DATE | — | ✅ |
| 59 | NegotiationHeaderCreationDateOrigAmend | CREATION_DATE_ORIG_AMEND | — | ✅ |
| 60 | NegotiationHeaderCurrencyCode | CURRENCY_CODE | — | ✅ |
| 61 | NegotiationHeaderDescription | DESCRIPTION | — | ✅ |
| 62 | NegotiationHeaderDisplayBestPriceBlindFlag | DISPLAY_BEST_PRICE_BLIND_FLAG | — | ✅ |
| 63 | NegotiationHeaderDoctypeId | DOCTYPE_ID | — | ✅ |
| 64 | NegotiationHeaderDocumentNumber | DOCUMENT_NUMBER | — | ✅ |
| 65 | NegotiationHeaderDraftLocked | DRAFT_LOCKED | — | ✅ |
| 66 | NegotiationHeaderDraftLockedDate | DRAFT_LOCKED_DATE | — | ✅ |
| 67 | NegotiationHeaderDraftUnlockedDate | DRAFT_UNLOCKED_DATE | — | ✅ |
| 68 | NegotiationHeaderEnforcePrevrndBidPriceFlag | ENFORCE_PREVRND_BID_PRICE_FLAG | — | ✅ |
| 69 | NegotiationHeaderEventId | EVENT_ID | — | ✅ |
| 70 | NegotiationHeaderEventTitle | EVENT_TITLE | — | ✅ |
| 71 | NegotiationHeaderExtAttribute1 | EXT_ATTRIBUTE1 | — | ✅ |
| 72 | NegotiationHeaderExtAttribute10 | EXT_ATTRIBUTE10 | — | ✅ |
| 73 | NegotiationHeaderExtAttribute11 | EXT_ATTRIBUTE11 | — | ✅ |
| 74 | NegotiationHeaderExtAttribute12 | EXT_ATTRIBUTE12 | — | ✅ |
| 75 | NegotiationHeaderExtAttribute13 | EXT_ATTRIBUTE13 | — | ✅ |
| 76 | NegotiationHeaderExtAttribute14 | EXT_ATTRIBUTE14 | — | ✅ |
| 77 | NegotiationHeaderExtAttribute15 | EXT_ATTRIBUTE15 | — | ✅ |
| 78 | NegotiationHeaderExtAttribute2 | EXT_ATTRIBUTE2 | — | ✅ |
| 79 | NegotiationHeaderExtAttribute3 | EXT_ATTRIBUTE3 | — | ✅ |
| 80 | NegotiationHeaderExtAttribute4 | EXT_ATTRIBUTE4 | — | ✅ |
| 81 | NegotiationHeaderExtAttribute5 | EXT_ATTRIBUTE5 | — | ✅ |
| 82 | NegotiationHeaderExtAttribute6 | EXT_ATTRIBUTE6 | — | ✅ |
| 83 | NegotiationHeaderExtAttribute7 | EXT_ATTRIBUTE7 | — | ✅ |
| 84 | NegotiationHeaderExtAttribute8 | EXT_ATTRIBUTE8 | — | ✅ |
| 85 | NegotiationHeaderExtAttribute9 | EXT_ATTRIBUTE9 | — | ✅ |
| 86 | NegotiationHeaderExtAttributeCategory | EXT_ATTRIBUTE_CATEGORY | — | ✅ |
| 87 | NegotiationHeaderFirstLineCloseDate | FIRST_LINE_CLOSE_DATE | — | ✅ |
| 88 | NegotiationHeaderFobCode | FOB_CODE | — | ✅ |
| 89 | NegotiationHeaderFreightTermsCode | FREIGHT_TERMS_CODE | — | ✅ |
| 90 | NegotiationHeaderFullQuantityBidCode | FULL_QUANTITY_BID_CODE | — | ✅ |
| 91 | NegotiationHeaderGlobalTemplateFlag | GLOBAL_TEMPLATE_FLAG | — | ✅ |
| 92 | NegotiationHeaderGroupEnabledFlag | GROUP_ENABLED_FLAG | — | ✅ |
| 93 | NegotiationHeaderHasHdrAttrFlag | HAS_HDR_ATTR_FLAG | — | ✅ |
| 94 | NegotiationHeaderHasItemsFlag | HAS_ITEMS_FLAG | — | ✅ |
| 95 | NegotiationHeaderHasPeForAllItems | HAS_PE_FOR_ALL_ITEMS | — | ✅ |
| 96 | NegotiationHeaderHasPriceElements | HAS_PRICE_ELEMENTS | — | ✅ |
| 97 | NegotiationHeaderHasScoringTeamsFlag | HAS_SCORING_TEAMS_FLAG | — | ✅ |
| 98 | NegotiationHeaderHdrAttrDisplayScore | HDR_ATTR_DISPLAY_SCORE | — | ✅ |
| 99 | NegotiationHeaderHdrAttrEnableWeights | HDR_ATTR_ENABLE_WEIGHTS | — | ✅ |
| 100 | NegotiationHeaderHdrAttrMaximumScore | HDR_ATTR_MAXIMUM_SCORE | — | ✅ |
| 101 | NegotiationHeaderHdrAttributeEnabledFlag | HDR_ATTRIBUTE_ENABLED_FLAG | — | ✅ |
| 102 | NegotiationHeaderImportFileName | IMPORT_FILE_NAME | — | ✅ |
| 103 | NegotiationHeaderIncludePdfInExternalPage | INCLUDE_PDF_IN_EXTERNAL_PAGE | — | ✅ |
| 104 | NegotiationHeaderIntAttribute1 | INT_ATTRIBUTE1 | — | ✅ |
| 105 | NegotiationHeaderIntAttribute10 | INT_ATTRIBUTE10 | — | ✅ |
| 106 | NegotiationHeaderIntAttribute11 | INT_ATTRIBUTE11 | — | ✅ |
| 107 | NegotiationHeaderIntAttribute12 | INT_ATTRIBUTE12 | — | ✅ |
| 108 | NegotiationHeaderIntAttribute13 | INT_ATTRIBUTE13 | — | ✅ |
| 109 | NegotiationHeaderIntAttribute14 | INT_ATTRIBUTE14 | — | ✅ |
| 110 | NegotiationHeaderIntAttribute15 | INT_ATTRIBUTE15 | — | ✅ |
| 111 | NegotiationHeaderIntAttribute2 | INT_ATTRIBUTE2 | — | ✅ |
| 112 | NegotiationHeaderIntAttribute3 | INT_ATTRIBUTE3 | — | ✅ |
| 113 | NegotiationHeaderIntAttribute4 | INT_ATTRIBUTE4 | — | ✅ |
| 114 | NegotiationHeaderIntAttribute5 | INT_ATTRIBUTE5 | — | ✅ |
| 115 | NegotiationHeaderIntAttribute6 | INT_ATTRIBUTE6 | — | ✅ |
| 116 | NegotiationHeaderIntAttribute7 | INT_ATTRIBUTE7 | — | ✅ |
| 117 | NegotiationHeaderIntAttribute8 | INT_ATTRIBUTE8 | — | ✅ |
| 118 | NegotiationHeaderIntAttribute9 | INT_ATTRIBUTE9 | — | ✅ |
| 119 | NegotiationHeaderIntAttributeCategory | INT_ATTRIBUTE_CATEGORY | — | ✅ |
| 120 | NegotiationHeaderIsPaused | IS_PAUSED | — | ✅ |
| 121 | NegotiationHeaderIsTemplateFlag | IS_TEMPLATE_FLAG | — | ✅ |
| 122 | NegotiationHeaderLanguageCode | LANGUAGE_CODE | — | ✅ |
| 123 | NegotiationHeaderLargeNegEnabledFlag | LARGE_NEG_ENABLED_FLAG | — | ✅ |
| 124 | NegotiationHeaderLastLineNumber | LAST_LINE_NUMBER | — | ✅ |
| 125 | NegotiationHeaderLastPauseDate | LAST_PAUSE_DATE | — | ✅ |
| 126 | NegotiationHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 127 | NegotiationHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 128 | NegotiationHeaderLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 129 | NegotiationHeaderLineAttributeEnabledFlag | LINE_ATTRIBUTE_ENABLED_FLAG | — | ✅ |
| 130 | NegotiationHeaderLineMasEnabledFlag | LINE_MAS_ENABLED_FLAG | — | ✅ |
| 131 | NegotiationHeaderLotEnabledFlag | LOT_ENABLED_FLAG | — | ✅ |
| 132 | NegotiationHeaderMaxBidColorSequenceId | MAX_BID_COLOR_SEQUENCE_ID | — | ✅ |
| 133 | NegotiationHeaderMaxDocumentLineNum | MAX_DOCUMENT_LINE_NUM | — | ✅ |
| 134 | NegotiationHeaderMaxInternalLineNum | MAX_INTERNAL_LINE_NUM | — | ✅ |
| 135 | NegotiationHeaderMaxRetainageNegotiableFlag | MAX_RETAINAGE_NEGOTIABLE_FLAG | — | ✅ |
| 136 | NegotiationHeaderMinBidChangeType | MIN_BID_CHANGE_TYPE | — | ✅ |
| 137 | NegotiationHeaderMinBidDecrement | MIN_BID_DECREMENT | — | ✅ |
| 138 | NegotiationHeaderNegTeamEnabledFlag | NEG_TEAM_ENABLED_FLAG | — | ✅ |
| 139 | NegotiationHeaderNumberOfBids | NUMBER_OF_BIDS | — | ✅ |
| 140 | NegotiationHeaderNumberOfExtensions | NUMBER_OF_EXTENSIONS | — | ✅ |
| 141 | NegotiationHeaderNumberOfLines | NUMBER_OF_LINES | — | ✅ |
| 142 | NegotiationHeaderNumberPriceDecimals | NUMBER_PRICE_DECIMALS | — | ✅ |
| 143 | NegotiationHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 144 | NegotiationHeaderOpenAuctionNowFlag | OPEN_AUCTION_NOW_FLAG | — | ✅ |
| 145 | NegotiationHeaderOpenBiddingDate | OPEN_BIDDING_DATE | — | ✅ |
| 146 | NegotiationHeaderOriginalCloseBiddingDate | ORIGINAL_CLOSE_BIDDING_DATE | — | ✅ |
| 147 | NegotiationHeaderOutcomeStatus | OUTCOME_STATUS | — | ✅ |
| 148 | NegotiationHeaderPauseRemarks | PAUSE_REMARKS | — | ✅ |
| 149 | NegotiationHeaderPaymentTermsId | PAYMENT_TERMS_ID | — | ✅ |
| 150 | NegotiationHeaderPfTypeAllowed | PF_TYPE_ALLOWED | — | ✅ |
| 151 | NegotiationHeaderPoAgreedAmount | PO_AGREED_AMOUNT | — | ✅ |
| 152 | NegotiationHeaderPoEndDate | PO_END_DATE | — | ✅ |
| 153 | NegotiationHeaderPoMinRelAmount | PO_MIN_REL_AMOUNT | — | ✅ |
| 154 | NegotiationHeaderPoStartDate | PO_START_DATE | — | ✅ |
| 155 | NegotiationHeaderPoStyleId | PO_STYLE_ID | — | ✅ |
| 156 | NegotiationHeaderPowerBiddingEnabledFlag | POWER_BIDDING_ENABLED_FLAG | — | ✅ |
| 157 | NegotiationHeaderPrcBuId | PRC_BU_ID | — | ✅ |
| 158 | NegotiationHeaderPriceDrivenAuctionFlag | PRICE_DRIVEN_AUCTION_FLAG | — | ✅ |
| 159 | NegotiationHeaderPriceElementEnabledFlag | PRICE_ELEMENT_ENABLED_FLAG | — | ✅ |
| 160 | NegotiationHeaderPriceTiersIndicator | PRICE_TIERS_INDICATOR | — | ✅ |
| 161 | NegotiationHeaderProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 162 | NegotiationHeaderProgramName | PROGRAM_NAME | — | ✅ |
| 163 | NegotiationHeaderProgressPaymentType | PROGRESS_PAYMENT_TYPE | — | ✅ |
| 164 | NegotiationHeaderProgressPymtNegotiableFlag | PROGRESS_PYMT_NEGOTIABLE_FLAG | — | ✅ |
| 165 | NegotiationHeaderProjectId | PROJECT_ID | — | ✅ |
| 166 | NegotiationHeaderProxyBiddingEnabledFlag | PROXY_BIDDING_ENABLED_FLAG | — | ✅ |
| 167 | NegotiationHeaderPublishAuctionNowFlag | PUBLISH_AUCTION_NOW_FLAG | — | ✅ |
| 168 | NegotiationHeaderPublishDate | PUBLISH_DATE | — | ✅ |
| 169 | NegotiationHeaderPublishDateOrigAmend | PUBLISH_DATE_ORIG_AMEND | — | ✅ |
| 170 | NegotiationHeaderPublishRatesToBiddersFlag | PUBLISH_RATES_TO_BIDDERS_FLAG | — | ✅ |
| 171 | NegotiationHeaderQtyPriceTiersEnabledFlag | QTY_PRICE_TIERS_ENABLED_FLAG | — | ✅ |
| 172 | NegotiationHeaderRankIndicator | RANK_INDICATOR | — | ✅ |
| 173 | NegotiationHeaderRateDate | RATE_DATE | — | ✅ |
| 174 | NegotiationHeaderRateType | RATE_TYPE | — | ✅ |
| 175 | NegotiationHeaderRecoupmentNegotiableFlag | RECOUPMENT_NEGOTIABLE_FLAG | — | ✅ |
| 176 | NegotiationHeaderReminderDate | REMINDER_DATE | — | ✅ |
| 177 | NegotiationHeaderRequestDate | REQUEST_DATE | — | ✅ |
| 178 | NegotiationHeaderRequestId | REQUEST_ID | — | ✅ |
| 179 | NegotiationHeaderRequestedBy | REQUESTED_BY | — | ✅ |
| 180 | NegotiationHeaderRetainageNegotiableFlag | RETAINAGE_NEGOTIABLE_FLAG | — | ✅ |
| 181 | NegotiationHeaderRfiLineEnabledFlag | RFI_LINE_ENABLED_FLAG | — | ✅ |
| 182 | NegotiationHeaderScoringLockDate | SCORING_LOCK_DATE | — | ✅ |
| 183 | NegotiationHeaderSealedActualUnlockDate | SEALED_ACTUAL_UNLOCK_DATE | — | ✅ |
| 184 | NegotiationHeaderSealedActualUnsealDate | SEALED_ACTUAL_UNSEAL_DATE | — | ✅ |
| 185 | NegotiationHeaderSealedAuctionStatus | SEALED_AUCTION_STATUS | — | ✅ |
| 186 | NegotiationHeaderShareAwardDecision | SHARE_AWARD_DECISION | — | ✅ |
| 187 | NegotiationHeaderShowBidderNotes | SHOW_BIDDER_NOTES | — | ✅ |
| 188 | NegotiationHeaderShowBidderScores | SHOW_BIDDER_SCORES | — | ✅ |
| 189 | NegotiationHeaderSourceDocId | SOURCE_DOC_ID | — | ✅ |
| 190 | NegotiationHeaderSourceDocLineMsg | SOURCE_DOC_LINE_MSG | — | ✅ |
| 191 | NegotiationHeaderSourceDocMsg | SOURCE_DOC_MSG | — | ✅ |
| 192 | NegotiationHeaderSourceDocMsgApp | SOURCE_DOC_MSG_APP | — | ✅ |
| 193 | NegotiationHeaderSourceDocNumber | SOURCE_DOC_NUMBER | — | ✅ |
| 194 | NegotiationHeaderSourceReqsFlag | SOURCE_REQS_FLAG | — | ✅ |
| 195 | NegotiationHeaderStaggeredClosingInterval | STAGGERED_CLOSING_INTERVAL | — | ✅ |
| 196 | NegotiationHeaderStyleId | STYLE_ID | — | ✅ |
| 197 | NegotiationHeaderSupplierEnterablePymtFlag | SUPPLIER_ENTERABLE_PYMT_FLAG | — | ✅ |
| 198 | NegotiationHeaderSupplierViewType | SUPPLIER_VIEW_TYPE | — | ✅ |
| 199 | NegotiationHeaderTeamScoringEnabledFlag | TEAM_SCORING_ENABLED_FLAG | — | ✅ |
| 200 | NegotiationHeaderTechnicalActualUnlockDate | TECHNICAL_ACTUAL_UNLOCK_DATE | — | ✅ |
| 201 | NegotiationHeaderTechnicalActualUnsealDate | TECHNICAL_ACTUAL_UNSEAL_DATE | — | ✅ |
| 202 | NegotiationHeaderTechnicalEvaluationStatus | TECHNICAL_EVALUATION_STATUS | — | ✅ |
| 203 | NegotiationHeaderTechnicalLockStatus | TECHNICAL_LOCK_STATUS | — | ✅ |
| 204 | NegotiationHeaderTemplateId | TEMPLATE_ID | — | ✅ |
| 205 | NegotiationHeaderTemplateScope | TEMPLATE_SCOPE | — | ✅ |
| 206 | NegotiationHeaderTemplateStatus | TEMPLATE_STATUS | — | ✅ |
| 207 | NegotiationHeaderTwoPartFlag | TWO_PART_FLAG | — | ✅ |
| 208 | NegotiationHeaderVersionNum | VERSION_NUM | — | ✅ |
| 209 | NegotiationHeaderViewByDate | VIEW_BY_DATE | — | ✅ |
| 210 | NegotiationHeaderWfApprovalItemKey | WF_APPROVAL_ITEM_KEY | — | ✅ |
| 211 | NegotiationHeaderWfAwardApprovalItemKey | WF_AWARD_APPROVAL_ITEM_KEY | — | ✅ |
| 212 | NegotiationHeaderWfItemKey | WF_ITEM_KEY | — | ✅ |
| 213 | NegotiationHeaderWfPoncomplCurrentRound | WF_PONCOMPL_CURRENT_ROUND | — | ✅ |
| 214 | NegotiationHeaderWfPoncomplItemKey | WF_PONCOMPL_ITEM_KEY | — | ✅ |
| 215 | NegotiationHeaderWfRoleName | WF_ROLE_NAME | — | ✅ |

### [[pon_auction_item_prices_all|PON_AUCTION_ITEM_PRICES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationLineAdditionalJobDetails | ADDITIONAL_JOB_DETAILS | — | ✅ |
| 2 | NegotiationLineAdvanceAmount | ADVANCE_AMOUNT | — | ✅ |
| 3 | NegotiationLineAllocationStatus | ALLOCATION_STATUS | — | ✅ |
| 4 | NegotiationLineAuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 5 | NegotiationLineAwardMode | AWARD_MODE | — | ✅ |
| 6 | NegotiationLineAwardStatus | AWARD_STATUS | — | ✅ |
| 7 | NegotiationLineAwardedQuantity | AWARDED_QUANTITY | — | ✅ |
| 8 | NegotiationLineBestBidBidCurrencyCode | BEST_BID_BID_CURRENCY_CODE | — | ✅ |
| 9 | NegotiationLineBestBidBidCurrencyPrice | BEST_BID_BID_CURRENCY_PRICE | — | ✅ |
| 10 | NegotiationLineBestBidBidNumber | BEST_BID_BID_NUMBER | — | ✅ |
| 11 | NegotiationLineBestBidBidPrice | BEST_BID_BID_PRICE | — | ✅ |
| 12 | NegotiationLineBestBidCurrencyCode | BEST_BID_CURRENCY_CODE | — | ✅ |
| 13 | NegotiationLineBestBidCurrencyPrice | BEST_BID_CURRENCY_PRICE | — | ✅ |
| 14 | NegotiationLineBestBidFirstBidPrice | BEST_BID_FIRST_BID_PRICE | — | ✅ |
| 15 | NegotiationLineBestBidNumber | BEST_BID_NUMBER | — | ✅ |
| 16 | NegotiationLineBestBidPrice | BEST_BID_PRICE | — | ✅ |
| 17 | NegotiationLineBestBidPromisedDate | BEST_BID_PROMISED_DATE | — | ✅ |
| 18 | NegotiationLineBestBidProxyLimitPrice | BEST_BID_PROXY_LIMIT_PRICE | — | ✅ |
| 19 | NegotiationLineBestBidQuantity | BEST_BID_QUANTITY | — | ✅ |
| 20 | NegotiationLineBestBidScore | BEST_BID_SCORE | — | ✅ |
| 21 | NegotiationLineBidStartPrice | BID_START_PRICE | — | ✅ |
| 22 | NegotiationLineCategoryId | CATEGORY_ID | — | ✅ |
| 23 | NegotiationLineCloseBiddingDate | CLOSE_BIDDING_DATE | — | ✅ |
| 24 | NegotiationLineCreatedBy | CREATED_BY | — | ✅ |
| 25 | NegotiationLineCreationDate | CREATION_DATE | — | ✅ |
| 26 | NegotiationLineCurrentPrice | CURRENT_PRICE | — | ✅ |
| 27 | NegotiationLineDifferentialResponseType | DIFFERENTIAL_RESPONSE_TYPE | — | ✅ |
| 28 | NegotiationLineDispLineNumber | DISP_LINE_NUMBER | — | ✅ |
| 29 | NegotiationLineDisplayTargetPriceFlag | DISPLAY_TARGET_PRICE_FLAG | — | ✅ |
| 30 | NegotiationLineDocumentDispLineNumber | DOCUMENT_DISP_LINE_NUMBER | — | ✅ |
| 31 | NegotiationLineGroupType | GROUP_TYPE | — | ✅ |
| 32 | NegotiationLineHasAttributesFlag | HAS_ATTRIBUTES_FLAG | — | ✅ |
| 33 | NegotiationLineHasBuyerPfsFlag | HAS_BUYER_PFS_FLAG | — | ✅ |
| 34 | NegotiationLineHasPaymentsFlag | HAS_PAYMENTS_FLAG | — | ✅ |
| 35 | NegotiationLineHasPriceDifferentialsFlag | HAS_PRICE_DIFFERENTIALS_FLAG | — | ✅ |
| 36 | NegotiationLineHasPriceElementsFlag | HAS_PRICE_ELEMENTS_FLAG | — | ✅ |
| 37 | NegotiationLineHasQuantityTiers | HAS_QUANTITY_TIERS | — | ✅ |
| 38 | NegotiationLineHasShipmentsFlag | HAS_SHIPMENTS_FLAG | — | ✅ |
| 39 | NegotiationLineInvOrgId | INV_ORG_ID | — | ✅ |
| 40 | NegotiationLineItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 41 | NegotiationLineItemId | ITEM_ID | — | ✅ |
| 42 | NegotiationLineItemRevision | ITEM_REVISION | — | ✅ |
| 43 | NegotiationLineJobId | JOB_ID | — | ✅ |
| 44 | NegotiationLineLastAmendmentUpdate | LAST_AMENDMENT_UPDATE | — | ✅ |
| 45 | NegotiationLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 46 | NegotiationLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 47 | NegotiationLineLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 48 | NegotiationLineLineNumber | LINE_NUMBER | — | ✅ |
| 49 | NegotiationLineLineOriginationCode | LINE_ORIGINATION_CODE | — | ✅ |
| 50 | NegotiationLineLineTypeId | LINE_TYPE_ID | — | ✅ |
| 51 | NegotiationLineMaxRetainageAmount | MAX_RETAINAGE_AMOUNT | — | ✅ |
| 52 | NegotiationLineMaxSubLineSequenceNumber | MAX_SUB_LINE_SEQUENCE_NUMBER | — | ✅ |
| 53 | NegotiationLineModifiedDate | MODIFIED_DATE | — | ✅ |
| 54 | NegotiationLineModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 55 | NegotiationLineNeedByDate | NEED_BY_DATE | — | ✅ |
| 56 | NegotiationLineNoAward | NO_AWARD | — | ✅ |
| 57 | NegotiationLineNoteToBidders | NOTE_TO_BIDDERS | — | ✅ |
| 58 | NegotiationLineNumberOfBids | NUMBER_OF_BIDS | — | ✅ |
| 59 | NegotiationLineNumberOfExtensions | NUMBER_OF_EXTENSIONS | — | ✅ |
| 60 | NegotiationLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 61 | NegotiationLineOrderTypeLookupCode | ORDER_TYPE_LOOKUP_CODE | — | ✅ |
| 62 | NegotiationLineParentLineNumber | PARENT_LINE_NUMBER | — | ✅ |
| 63 | NegotiationLinePoAgreedAmount | PO_AGREED_AMOUNT | — | ✅ |
| 64 | NegotiationLinePoMinRelAmount | PO_MIN_REL_AMOUNT | — | ✅ |
| 65 | NegotiationLinePrcBuId | PRC_BU_ID | — | ✅ |
| 66 | NegotiationLinePriceBreakNegFlag | PRICE_BREAK_NEG_FLAG | — | ✅ |
| 67 | NegotiationLinePriceBreakType | PRICE_BREAK_TYPE | — | ✅ |
| 68 | NegotiationLinePriceDiffShipmentNumber | PRICE_DIFF_SHIPMENT_NUMBER | — | ✅ |
| 69 | NegotiationLinePriceDisabledFlag | PRICE_DISABLED_FLAG | — | ✅ |
| 70 | NegotiationLineProgressPymtRatePercent | PROGRESS_PYMT_RATE_PERCENT | — | ✅ |
| 71 | NegotiationLineProjectAwardId | PROJECT_AWARD_ID | — | ✅ |
| 72 | NegotiationLineProjectExpOrganizationId | PROJECT_EXP_ORGANIZATION_ID | — | ✅ |
| 73 | NegotiationLineProjectExpenditureItemDate | PROJECT_EXPENDITURE_ITEM_DATE | — | ✅ |
| 74 | NegotiationLineProjectExpenditureType | PROJECT_EXPENDITURE_TYPE | — | ✅ |
| 75 | NegotiationLineProjectId | PROJECT_ID | — | ✅ |
| 76 | NegotiationLineProjectTaskId | PROJECT_TASK_ID | — | ✅ |
| 77 | NegotiationLinePurchaseBasis | PURCHASE_BASIS | — | ✅ |
| 78 | NegotiationLineQuantity | QUANTITY | — | ✅ |
| 79 | NegotiationLineQuantityDisabledFlag | QUANTITY_DISABLED_FLAG | — | ✅ |
| 80 | NegotiationLineRecoupmentRatePercent | RECOUPMENT_RATE_PERCENT | — | ✅ |
| 81 | NegotiationLineReqBuId | REQ_BU_ID | — | ✅ |
| 82 | NegotiationLineRequestedDeliveryDate | REQUESTED_DELIVERY_DATE | — | ✅ |
| 83 | NegotiationLineRequestedShipDate | REQUESTED_SHIP_DATE | — | ✅ |
| 84 | NegotiationLineRequisitionNumber | REQUISITION_NUMBER | — | ✅ |
| 85 | NegotiationLineRetainageRatePercent | RETAINAGE_RATE_PERCENT | — | ✅ |
| 86 | NegotiationLineShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 87 | NegotiationLineSourceDocId | SOURCE_DOC_ID | — | ✅ |
| 88 | NegotiationLineSourceDocNumber | SOURCE_DOC_NUMBER | — | ✅ |
| 89 | NegotiationLineSourceLineId | SOURCE_LINE_ID | — | ✅ |
| 90 | NegotiationLineSourceLineNumber | SOURCE_LINE_NUMBER | — | ✅ |
| 91 | NegotiationLineSubLineSequenceNumber | SUB_LINE_SEQUENCE_NUMBER | — | ✅ |
| 92 | NegotiationLineTargetPrice | TARGET_PRICE | — | ✅ |
| 93 | NegotiationLineUnitDisplayTargetFlag | UNIT_DISPLAY_TARGET_FLAG | — | ✅ |
| 94 | NegotiationLineUnitTargetPrice | UNIT_TARGET_PRICE | — | ✅ |
| 95 | NegotiationLineUomCode | UOM_CODE | — | ✅ |
| 96 | NegotiationLineWorkApproverUserId | WORK_APPROVER_USER_ID | — | ✅ |
| 97 | NegotiationParentLineAdditionalJobDetails | ADDITIONAL_JOB_DETAILS | — | ✅ |
| 98 | NegotiationParentLineAdvanceAmount | ADVANCE_AMOUNT | — | ✅ |
| 99 | NegotiationParentLineAllocationStatus | ALLOCATION_STATUS | — | ✅ |
| 100 | NegotiationParentLineAuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 101 | NegotiationParentLineAwardMode | AWARD_MODE | — | ✅ |
| 102 | NegotiationParentLineAwardStatus | AWARD_STATUS | — | ✅ |
| 103 | NegotiationParentLineAwardedQuantity | AWARDED_QUANTITY | — | ✅ |
| 104 | NegotiationParentLineBestBidBidCurrencyCode | BEST_BID_BID_CURRENCY_CODE | — | ✅ |
| 105 | NegotiationParentLineBestBidBidCurrencyPrice | BEST_BID_BID_CURRENCY_PRICE | — | ✅ |
| 106 | NegotiationParentLineBestBidBidNumber | BEST_BID_BID_NUMBER | — | ✅ |
| 107 | NegotiationParentLineBestBidBidPrice | BEST_BID_BID_PRICE | — | ✅ |
| 108 | NegotiationParentLineBestBidCurrencyCode | BEST_BID_CURRENCY_CODE | — | ✅ |
| 109 | NegotiationParentLineBestBidCurrencyPrice | BEST_BID_CURRENCY_PRICE | — | ✅ |
| 110 | NegotiationParentLineBestBidFirstBidPrice | BEST_BID_FIRST_BID_PRICE | — | ✅ |
| 111 | NegotiationParentLineBestBidNumber | BEST_BID_NUMBER | — | ✅ |
| 112 | NegotiationParentLineBestBidPrice | BEST_BID_PRICE | — | ✅ |
| 113 | NegotiationParentLineBestBidPromisedDate | BEST_BID_PROMISED_DATE | — | ✅ |
| 114 | NegotiationParentLineBestBidProxyLimitPrice | BEST_BID_PROXY_LIMIT_PRICE | — | ✅ |
| 115 | NegotiationParentLineBestBidQuantity | BEST_BID_QUANTITY | — | ✅ |
| 116 | NegotiationParentLineBestBidScore | BEST_BID_SCORE | — | ✅ |
| 117 | NegotiationParentLineBidStartPrice | BID_START_PRICE | — | ✅ |
| 118 | NegotiationParentLineCategoryId | CATEGORY_ID | — | ✅ |
| 119 | NegotiationParentLineCloseBiddingDate | CLOSE_BIDDING_DATE | — | ✅ |
| 120 | NegotiationParentLineCreatedBy | CREATED_BY | — | ✅ |
| 121 | NegotiationParentLineCreationDate | CREATION_DATE | — | ✅ |
| 122 | NegotiationParentLineCurrentPrice | CURRENT_PRICE | — | ✅ |
| 123 | NegotiationParentLineDifferentialResponseType | DIFFERENTIAL_RESPONSE_TYPE | — | ✅ |
| 124 | NegotiationParentLineDispLineNumber | DISP_LINE_NUMBER | — | ✅ |
| 125 | NegotiationParentLineDisplayTargetPriceFlag | DISPLAY_TARGET_PRICE_FLAG | — | ✅ |
| 126 | NegotiationParentLineDocumentDispLineNumber | DOCUMENT_DISP_LINE_NUMBER | — | ✅ |
| 127 | NegotiationParentLineGroupType | GROUP_TYPE | — | ✅ |
| 128 | NegotiationParentLineHasAttributesFlag | HAS_ATTRIBUTES_FLAG | — | ✅ |
| 129 | NegotiationParentLineHasBuyerPfsFlag | HAS_BUYER_PFS_FLAG | — | ✅ |
| 130 | NegotiationParentLineHasPaymentsFlag | HAS_PAYMENTS_FLAG | — | ✅ |
| 131 | NegotiationParentLineHasPriceDifferentialsFlag | HAS_PRICE_DIFFERENTIALS_FLAG | — | ✅ |
| 132 | NegotiationParentLineHasPriceElementsFlag | HAS_PRICE_ELEMENTS_FLAG | — | ✅ |
| 133 | NegotiationParentLineHasQuantityTiers | HAS_QUANTITY_TIERS | — | ✅ |
| 134 | NegotiationParentLineHasShipmentsFlag | HAS_SHIPMENTS_FLAG | — | ✅ |
| 135 | NegotiationParentLineInvOrgId | INV_ORG_ID | — | ✅ |
| 136 | NegotiationParentLineItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 137 | NegotiationParentLineItemId | ITEM_ID | — | ✅ |
| 138 | NegotiationParentLineItemRevision | ITEM_REVISION | — | ✅ |
| 139 | NegotiationParentLineJobId | JOB_ID | — | ✅ |
| 140 | NegotiationParentLineLastAmendmentUpdate | LAST_AMENDMENT_UPDATE | — | ✅ |
| 141 | NegotiationParentLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 142 | NegotiationParentLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 143 | NegotiationParentLineLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 144 | NegotiationParentLineLineNumber | LINE_NUMBER | — | ✅ |
| 145 | NegotiationParentLineLineOriginationCode | LINE_ORIGINATION_CODE | — | ✅ |
| 146 | NegotiationParentLineLineTypeId | LINE_TYPE_ID | — | ✅ |
| 147 | NegotiationParentLineMaxRetainageAmount | MAX_RETAINAGE_AMOUNT | — | ✅ |
| 148 | NegotiationParentLineMaxSubLineSequenceNumber | MAX_SUB_LINE_SEQUENCE_NUMBER | — | ✅ |
| 149 | NegotiationParentLineModifiedDate | MODIFIED_DATE | — | ✅ |
| 150 | NegotiationParentLineModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 151 | NegotiationParentLineNeedByDate | NEED_BY_DATE | — | ✅ |
| 152 | NegotiationParentLineNoAward | NO_AWARD | — | ✅ |
| 153 | NegotiationParentLineNoteToBidders | NOTE_TO_BIDDERS | — | ✅ |
| 154 | NegotiationParentLineNumberOfBids | NUMBER_OF_BIDS | — | ✅ |
| 155 | NegotiationParentLineNumberOfExtensions | NUMBER_OF_EXTENSIONS | — | ✅ |
| 156 | NegotiationParentLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 157 | NegotiationParentLineOrderTypeLookupCode | ORDER_TYPE_LOOKUP_CODE | — | ✅ |
| 158 | NegotiationParentLineParentLineNumber | PARENT_LINE_NUMBER | — | ✅ |
| 159 | NegotiationParentLinePoAgreedAmount | PO_AGREED_AMOUNT | — | ✅ |
| 160 | NegotiationParentLinePoMinRelAmount | PO_MIN_REL_AMOUNT | — | ✅ |
| 161 | NegotiationParentLinePrcBuId | PRC_BU_ID | — | ✅ |
| 162 | NegotiationParentLinePriceBreakNegFlag | PRICE_BREAK_NEG_FLAG | — | ✅ |
| 163 | NegotiationParentLinePriceBreakType | PRICE_BREAK_TYPE | — | ✅ |
| 164 | NegotiationParentLinePriceDiffShipmentNumber | PRICE_DIFF_SHIPMENT_NUMBER | — | ✅ |
| 165 | NegotiationParentLinePriceDisabledFlag | PRICE_DISABLED_FLAG | — | ✅ |
| 166 | NegotiationParentLineProgressPymtRatePercent | PROGRESS_PYMT_RATE_PERCENT | — | ✅ |
| 167 | NegotiationParentLineProjectAwardId | PROJECT_AWARD_ID | — | ✅ |
| 168 | NegotiationParentLineProjectExpOrganizationId | PROJECT_EXP_ORGANIZATION_ID | — | ✅ |
| 169 | NegotiationParentLineProjectExpenditureItemDate | PROJECT_EXPENDITURE_ITEM_DATE | — | ✅ |
| 170 | NegotiationParentLineProjectExpenditureType | PROJECT_EXPENDITURE_TYPE | — | ✅ |
| 171 | NegotiationParentLineProjectId | PROJECT_ID | — | ✅ |
| 172 | NegotiationParentLineProjectTaskId | PROJECT_TASK_ID | — | ✅ |
| 173 | NegotiationParentLinePurchaseBasis | PURCHASE_BASIS | — | ✅ |
| 174 | NegotiationParentLineQuantity | QUANTITY | — | ✅ |
| 175 | NegotiationParentLineQuantityDisabledFlag | QUANTITY_DISABLED_FLAG | — | ✅ |
| 176 | NegotiationParentLineRecoupmentRatePercent | RECOUPMENT_RATE_PERCENT | — | ✅ |
| 177 | NegotiationParentLineReqBuId | REQ_BU_ID | — | ✅ |
| 178 | NegotiationParentLineRequisitionNumber | REQUISITION_NUMBER | — | ✅ |
| 179 | NegotiationParentLineRetainageRatePercent | RETAINAGE_RATE_PERCENT | — | ✅ |
| 180 | NegotiationParentLineShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 181 | NegotiationParentLineSourceDocId | SOURCE_DOC_ID | — | ✅ |
| 182 | NegotiationParentLineSourceDocNumber | SOURCE_DOC_NUMBER | — | ✅ |
| 183 | NegotiationParentLineSourceLineId | SOURCE_LINE_ID | — | ✅ |
| 184 | NegotiationParentLineSourceLineNumber | SOURCE_LINE_NUMBER | — | ✅ |
| 185 | NegotiationParentLineSubLineSequenceNumber | SUB_LINE_SEQUENCE_NUMBER | — | ✅ |
| 186 | NegotiationParentLineTargetPrice | TARGET_PRICE | — | ✅ |
| 187 | NegotiationParentLineUnitDisplayTargetFlag | UNIT_DISPLAY_TARGET_FLAG | — | ✅ |
| 188 | NegotiationParentLineUnitTargetPrice | UNIT_TARGET_PRICE | — | ✅ |
| 189 | NegotiationParentLineUomCode | UOM_CODE | — | ✅ |
| 190 | NegotiationParentLineWorkApproverUserId | WORK_APPROVER_USER_ID | — | ✅ |

### [[pon_bid_headers|PON_BID_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OriginalBidNumber | ORIGINAL_BID_NUMBER | — | ✅ |
| 2 | ResponseHeaderAttributeLineNumber | ATTRIBUTE_LINE_NUMBER | — | ✅ |
| 3 | ResponseHeaderAuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 4 | ResponseHeaderAwardDate | AWARD_DATE | — | ✅ |
| 5 | ResponseHeaderAwardStatus | AWARD_STATUS | — | ✅ |
| 6 | ResponseHeaderBidCurrencyCode | BID_CURRENCY_CODE | — | ✅ |
| 7 | ResponseHeaderBidExpirationDate | BID_EXPIRATION_DATE | — | ✅ |
| 8 | ResponseHeaderBidNumber | BID_NUMBER | — | ✅ |
| 9 | ResponseHeaderBidStatus | BID_STATUS | — | ✅ |
| 10 | ResponseHeaderBiddersBidNumber | BIDDERS_BID_NUMBER | — | ✅ |
| 11 | ResponseHeaderBuyerBidTotal | BUYER_BID_TOTAL | — | ✅ |
| 12 | ResponseHeaderCancelReason | CANCEL_REASON | — | ✅ |
| 13 | ResponseHeaderCancelledDate | CANCELLED_DATE | — | ✅ |
| 14 | ResponseHeaderColorSequenceId | COLOR_SEQUENCE_ID | — | ✅ |
| 15 | ResponseHeaderCreatedBy | CREATED_BY | — | ✅ |
| 16 | ResponseHeaderCreationDate | CREATION_DATE | — | ✅ |
| 17 | ResponseHeaderCurrentRebate | CURRENT_REBATE | — | ✅ |
| 18 | ResponseHeaderCurrentTotalSpend | CURRENT_TOTAL_SPEND | — | ✅ |
| 19 | ResponseHeaderDisplayPriceFactorsFlag | DISPLAY_PRICE_FACTORS_FLAG | — | ✅ |
| 20 | ResponseHeaderDisqualifyReason | DISQUALIFY_REASON | — | ✅ |
| 21 | ResponseHeaderDraftLocked | DRAFT_LOCKED | — | ✅ |
| 22 | ResponseHeaderDraftLockedBy | DRAFT_LOCKED_BY | — | ✅ |
| 23 | ResponseHeaderDraftLockedByContactId | DRAFT_LOCKED_BY_CONTACT_ID | — | ✅ |
| 24 | ResponseHeaderDraftLockedDate | DRAFT_LOCKED_DATE | — | ✅ |
| 25 | ResponseHeaderDraftUnlockedBy | DRAFT_UNLOCKED_BY | — | ✅ |
| 26 | ResponseHeaderDraftUnlockedByContactId | DRAFT_UNLOCKED_BY_CONTACT_ID | — | ✅ |
| 27 | ResponseHeaderDraftUnlockedDate | DRAFT_UNLOCKED_DATE | — | ✅ |
| 28 | ResponseHeaderFixedIncentive | FIXED_INCENTIVE | — | ✅ |
| 29 | ResponseHeaderHasRebateTiers | HAS_REBATE_TIERS | — | ✅ |
| 30 | ResponseHeaderImportFileName | IMPORT_FILE_NAME | — | ✅ |
| 31 | ResponseHeaderIncumbentFlag | INCUMBENT_FLAG | — | ✅ |
| 32 | ResponseHeaderInternalNote | INTERNAL_NOTE | — | ✅ |
| 33 | ResponseHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 34 | ResponseHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 35 | ResponseHeaderLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 36 | ResponseHeaderMinBidChange | MIN_BID_CHANGE | — | ✅ |
| 37 | ResponseHeaderNoteToAuctionOwner | NOTE_TO_AUCTION_OWNER | — | ✅ |
| 38 | ResponseHeaderNoteToSupplier | NOTE_TO_SUPPLIER | — | ✅ |
| 39 | ResponseHeaderNumberPriceDecimals | NUMBER_PRICE_DECIMALS | — | ✅ |
| 40 | ResponseHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 41 | ResponseHeaderOldBidExpirationDate | OLD_BID_EXPIRATION_DATE | — | ✅ |
| 42 | ResponseHeaderOldBidNumber | OLD_BID_NUMBER | — | ✅ |
| 43 | ResponseHeaderOldBidStatus | OLD_BID_STATUS | — | ✅ |
| 44 | ResponseHeaderOldBiddersBidNumber | OLD_BIDDERS_BID_NUMBER | — | ✅ |
| 45 | ResponseHeaderOldMinBidChange | OLD_MIN_BID_CHANGE | — | ✅ |
| 46 | ResponseHeaderOldNoteToAuctionOwner | OLD_NOTE_TO_AUCTION_OWNER | — | ✅ |
| 47 | ResponseHeaderOldSurrogBidReceiptDate | OLD_SURROG_BID_RECEIPT_DATE | — | ✅ |
| 48 | ResponseHeaderPartialResponseFlag | PARTIAL_RESPONSE_FLAG | — | ✅ |
| 49 | ResponseHeaderPoAgreedAmount | PO_AGREED_AMOUNT | — | ✅ |
| 50 | ResponseHeaderProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 51 | ResponseHeaderProgramName | PROGRAM_NAME | — | ✅ |
| 52 | ResponseHeaderProxyBidFlag | PROXY_BID_FLAG | — | ✅ |
| 53 | ResponseHeaderPublishDate | PUBLISH_DATE | — | ✅ |
| 54 | ResponseHeaderRate | RATE | — | ✅ |
| 55 | ResponseHeaderRateDate | RATE_DATE | — | ✅ |
| 56 | ResponseHeaderRateDsp | RATE_DSP | — | ✅ |
| 57 | ResponseHeaderRateType | RATE_TYPE | — | ✅ |
| 58 | ResponseHeaderRequestDate | REQUEST_DATE | — | ✅ |
| 59 | ResponseHeaderRequestId | REQUEST_ID | — | ✅ |
| 60 | ResponseHeaderRequestedBy | REQUESTED_BY | — | ✅ |
| 61 | ResponseHeaderScoreOverridenDate | SCORE_OVERRIDEN_DATE | — | ✅ |
| 62 | ResponseHeaderScoreOverridenFlag | SCORE_OVERRIDEN_FLAG | — | ✅ |
| 63 | ResponseHeaderShortlistFlag | SHORTLIST_FLAG | — | ✅ |
| 64 | ResponseHeaderSurrogBidCreatedPersonId | SURROG_BID_CREATED_PERSON_ID | — | ✅ |
| 65 | ResponseHeaderSurrogBidFlag | SURROG_BID_FLAG | — | ✅ |
| 66 | ResponseHeaderSurrogBidOnlineEntryDate | SURROG_BID_ONLINE_ENTRY_DATE | — | ✅ |
| 67 | ResponseHeaderSurrogBidReceiptDate | SURROG_BID_RECEIPT_DATE | — | ✅ |
| 68 | ResponseHeaderTechnicalShortlistFlag | TECHNICAL_SHORTLIST_FLAG | — | ✅ |
| 69 | ResponseHeaderTotalAwardAmount | TOTAL_AWARD_AMOUNT | — | ✅ |
| 70 | ResponseHeaderTradingPartnerContactId | TRADING_PARTNER_CONTACT_ID | — | ✅ |
| 71 | ResponseHeaderTradingPartnerId | TRADING_PARTNER_ID | — | ✅ |
| 72 | ResponseHeaderVendorId | VENDOR_ID | — | ✅ |
| 73 | ResponseHeaderVendorSiteId | VENDOR_SITE_ID | — | ✅ |
| 74 | TypeOfResponse | TYPE_OF_RESPONSE | — | ✅ |

### [[pon_bid_item_prices|PON_BID_ITEM_PRICES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AlternateLineDescription | ALTERNATE_LINE_DESCRIPTION | — | ✅ |
| 2 | AlternateLineFlag | ALTERNATE_LINE_FLAG | — | ✅ |
| 3 | AuctionLineNumber | AUCTION_LINE_NUMBER | — | ✅ |
| 4 | PurchasingItemDesc | PURCHASING_ITEM_DESC | — | ✅ |
| 5 | PurchasingItemId | PURCHASING_ITEM_ID | — | ✅ |
| 6 | PurchasingItemRevision | PURCHASING_ITEM_REVISION | — | ✅ |
| 7 | ResponseLineAdvanceAmount | ADVANCE_AMOUNT | — | ✅ |
| 8 | ResponseLineAuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 9 | ResponseLineAwardDate | AWARD_DATE | — | ✅ |
| 10 | ResponseLineAwardPrice | AWARD_PRICE | — | ✅ |
| 11 | ResponseLineAwardQuantity | AWARD_QUANTITY | — | ✅ |
| 12 | ResponseLineAwardShipmentNumber | AWARD_SHIPMENT_NUMBER | — | ✅ |
| 13 | ResponseLineAwardStatus | AWARD_STATUS | — | ✅ |
| 14 | ResponseLineBatchId | BATCH_ID | — | ✅ |
| 15 | ResponseLineBidCurrAdvanceAmount | BID_CURR_ADVANCE_AMOUNT | — | ✅ |
| 16 | ResponseLineBidCurrMaxRetainageAmt | BID_CURR_MAX_RETAINAGE_AMT | — | ✅ |
| 17 | ResponseLineBidCurrencyLimitPrice | BID_CURRENCY_LIMIT_PRICE | — | ✅ |
| 18 | ResponseLineBidCurrencyPrice | BID_CURRENCY_PRICE | — | ✅ |
| 19 | ResponseLineBidCurrencyTransPrice | BID_CURRENCY_TRANS_PRICE | — | ✅ |
| 20 | ResponseLineBidCurrencyUnitPrice | BID_CURRENCY_UNIT_PRICE | — | ✅ |
| 21 | ResponseLineBidNumber | BID_NUMBER | — | ✅ |
| 22 | ResponseLineBidStartPrice | BID_START_PRICE | — | ✅ |
| 23 | ResponseLineCancelledLimitPrice | CANCELLED_LIMIT_PRICE | — | ✅ |
| 24 | ResponseLineCopyPriceForProxyFlag | COPY_PRICE_FOR_PROXY_FLAG | — | ✅ |
| 25 | ResponseLineCreatedBy | CREATED_BY | — | ✅ |
| 26 | ResponseLineCreationDate | CREATION_DATE | — | ✅ |
| 27 | ResponseLineDisplayPriceFactorsFlag | DISPLAY_PRICE_FACTORS_FLAG | — | ✅ |
| 28 | ResponseLineFirstBidPrice | FIRST_BID_PRICE | — | ✅ |
| 29 | ResponseLineFixedAmountComponent | FIXED_AMOUNT_COMPONENT | — | ✅ |
| 30 | ResponseLineGroupAmount | GROUP_AMOUNT | — | ✅ |
| 31 | ResponseLineHasAttributesFlag | HAS_ATTRIBUTES_FLAG | — | ✅ |
| 32 | ResponseLineHasBidFlag | HAS_BID_FLAG | — | ✅ |
| 33 | ResponseLineHasBidPaymentsFlag | HAS_BID_PAYMENTS_FLAG | — | ✅ |
| 34 | ResponseLineHasPriceDifferentialsFlag | HAS_PRICE_DIFFERENTIALS_FLAG | — | ✅ |
| 35 | ResponseLineHasQuantityTiers | HAS_QUANTITY_TIERS | — | ✅ |
| 36 | ResponseLineHasShipmentsFlag | HAS_SHIPMENTS_FLAG | — | ✅ |
| 37 | ResponseLineInterfaceLineId | INTERFACE_LINE_ID | — | ✅ |
| 38 | ResponseLineIsChangedLineFlag | IS_CHANGED_LINE_FLAG | — | ✅ |
| 39 | ResponseLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 40 | ResponseLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 41 | ResponseLineLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 42 | ResponseLineLineNumber | LINE_NUMBER | — | ✅ |
| 43 | ResponseLineMaxRetainageAmount | MAX_RETAINAGE_AMOUNT | — | ✅ |
| 44 | ResponseLineNoteToAuctionOwner | NOTE_TO_AUCTION_OWNER | — | ✅ |
| 45 | ResponseLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 46 | ResponseLineOldBidCurrAdvanceAmount | OLD_BID_CURR_ADVANCE_AMOUNT | — | ✅ |
| 47 | ResponseLineOldBidCurrMaxRetainageAmt | OLD_BID_CURR_MAX_RETAINAGE_AMT | — | ✅ |
| 48 | ResponseLineOldBidCurrencyLimitPrice | OLD_BID_CURRENCY_LIMIT_PRICE | — | ✅ |
| 49 | ResponseLineOldBidCurrencyPrice | OLD_BID_CURRENCY_PRICE | — | ✅ |
| 50 | ResponseLineOldBidCurrencyUnitPrice | OLD_BID_CURRENCY_UNIT_PRICE | — | ✅ |
| 51 | ResponseLineOldNoOfPayments | OLD_NO_OF_PAYMENTS | — | ✅ |
| 52 | ResponseLineOldNoteToAuctionOwner | OLD_NOTE_TO_AUCTION_OWNER | — | ✅ |
| 53 | ResponseLineOldPoBidMinRelAmount | OLD_PO_BID_MIN_REL_AMOUNT | — | ✅ |
| 54 | ResponseLineOldPrice | OLD_PRICE | — | ✅ |
| 55 | ResponseLineOldProgressPymtRatePercent | OLD_PROGRESS_PYMT_RATE_PERCENT | — | ✅ |
| 56 | ResponseLineOldPromisedDate | OLD_PROMISED_DATE | — | ✅ |
| 57 | ResponseLineOldPublishDate | OLD_PUBLISH_DATE | — | ✅ |
| 58 | ResponseLineOldQuantity | OLD_QUANTITY | — | ✅ |
| 59 | ResponseLineOldRecoupmentRatePercent | OLD_RECOUPMENT_RATE_PERCENT | — | ✅ |
| 60 | ResponseLineOldRetainageRatePercent | OLD_RETAINAGE_RATE_PERCENT | — | ✅ |
| 61 | ResponseLinePerUnitPriceComponent | PER_UNIT_PRICE_COMPONENT | — | ✅ |
| 62 | ResponseLinePoBidMinRelAmount | PO_BID_MIN_REL_AMOUNT | — | ✅ |
| 63 | ResponseLinePoMinRelAmount | PO_MIN_REL_AMOUNT | — | ✅ |
| 64 | ResponseLinePrice | PRICE | — | ✅ |
| 65 | ResponseLinePriceBreakType | PRICE_BREAK_TYPE | — | ✅ |
| 66 | ResponseLinePriceDiffShipmentNumber | PRICE_DIFF_SHIPMENT_NUMBER | — | ✅ |
| 67 | ResponseLineProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 68 | ResponseLineProgramName | PROGRAM_NAME | — | ✅ |
| 69 | ResponseLineProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 70 | ResponseLineProgressPymtRatePercent | PROGRESS_PYMT_RATE_PERCENT | — | ✅ |
| 71 | ResponseLinePromisedDate | PROMISED_DATE | — | ✅ |
| 72 | ResponseLinePromisedDeliveryDate | PROMISED_DELIVERY_DATE | — | ✅ |
| 73 | ResponseLinePromisedShipDate | PROMISED_SHIP_DATE | — | ✅ |
| 74 | ResponseLineProxyBidFlag | PROXY_BID_FLAG | — | ✅ |
| 75 | ResponseLineProxyBidLimitPrice | PROXY_BID_LIMIT_PRICE | — | ✅ |
| 76 | ResponseLinePublishDate | PUBLISH_DATE | — | ✅ |
| 77 | ResponseLineQuantity | QUANTITY | — | ✅ |
| 78 | ResponseLineRank | RANK | — | ✅ |
| 79 | ResponseLineRecoupmentRatePercent | RECOUPMENT_RATE_PERCENT | — | ✅ |
| 80 | ResponseLineRequestId | REQUEST_ID | — | ✅ |
| 81 | ResponseLineRetainageRatePercent | RETAINAGE_RATE_PERCENT | — | ✅ |
| 82 | ResponseLineTotalWeightedScore | TOTAL_WEIGHTED_SCORE | — | ✅ |
| 83 | ResponseLineTriggerBidNumber | TRIGGER_BID_NUMBER | — | ✅ |
| 84 | ResponseLineUnitPrice | UNIT_PRICE | — | ✅ |
| 85 | ResponseLineWorksheetName | WORKSHEET_NAME | — | ✅ |
| 86 | ResponseLineWorksheetSequenceNumber | WORKSHEET_SEQUENCE_NUMBER | — | ✅ |
| 87 | UomCode | UOM_CODE | — | ✅ |
| 88 | UomConversionFactor | UOM_CONVERSION_FACTOR | — | ✅ |

### [[pon_bid_shipments|PON_BID_SHIPMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BidNumber | BID_NUMBER | 🔑 | ✅ |
| 2 | LineNumber | LINE_NUMBER | 🔑 | ✅ |
| 3 | ResponsePriceTierAuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 4 | ResponsePriceTierAuctionShipmentNumber | AUCTION_SHIPMENT_NUMBER | — | ✅ |
| 5 | ResponsePriceTierBidCurrencyPrice | BID_CURRENCY_PRICE | — | ✅ |
| 6 | ResponsePriceTierBidCurrencyUnitPrice | BID_CURRENCY_UNIT_PRICE | — | ✅ |
| 7 | ResponsePriceTierCreatedBy | CREATED_BY | — | ✅ |
| 8 | ResponsePriceTierCreationDate | CREATION_DATE | — | ✅ |
| 9 | ResponsePriceTierEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 10 | ResponsePriceTierEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 11 | ResponsePriceTierHasPriceDifferentialsFlag | HAS_PRICE_DIFFERENTIALS_FLAG | — | ✅ |
| 12 | ResponsePriceTierInterfaceLineId | INTERFACE_LINE_ID | — | ✅ |
| 13 | ResponsePriceTierLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | ResponsePriceTierLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | ResponsePriceTierLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | ResponsePriceTierMaxQuantity | MAX_QUANTITY | — | ✅ |
| 17 | ResponsePriceTierObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | ResponsePriceTierOldBidCurrencyPrice | OLD_BID_CURRENCY_PRICE | — | ✅ |
| 19 | ResponsePriceTierOldBidCurrencyUnitPrice | OLD_BID_CURRENCY_UNIT_PRICE | — | ✅ |
| 20 | ResponsePriceTierOldEffectiveEndDate | OLD_EFFECTIVE_END_DATE | — | ✅ |
| 21 | ResponsePriceTierOldEffectiveStartDate | OLD_EFFECTIVE_START_DATE | — | ✅ |
| 22 | ResponsePriceTierOldMaxQuantity | OLD_MAX_QUANTITY | — | ✅ |
| 23 | ResponsePriceTierOldPriceDiscount | OLD_PRICE_DISCOUNT | — | ✅ |
| 24 | ResponsePriceTierOldPriceType | OLD_PRICE_TYPE | — | ✅ |
| 25 | ResponsePriceTierOldQuantity | OLD_QUANTITY | — | ✅ |
| 26 | ResponsePriceTierOldShipToLocId | OLD_SHIP_TO_LOC_ID | — | ✅ |
| 27 | ResponsePriceTierOldShipToOrgId | OLD_SHIP_TO_ORG_ID | — | ✅ |
| 28 | ResponsePriceTierPerUnitPriceComponent | PER_UNIT_PRICE_COMPONENT | — | ✅ |
| 29 | ResponsePriceTierPrice | PRICE | — | ✅ |
| 30 | ResponsePriceTierPriceDiscount | PRICE_DISCOUNT | — | ✅ |
| 31 | ResponsePriceTierPriceType | PRICE_TYPE | — | ✅ |
| 32 | ResponsePriceTierQuantity | QUANTITY | — | ✅ |
| 33 | ResponsePriceTierShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 34 | ResponsePriceTierShipToOrganizationId | SHIP_TO_ORGANIZATION_ID | — | ✅ |
| 35 | ResponsePriceTierShipmentType | SHIPMENT_TYPE | — | ✅ |
| 36 | ResponsePriceTierUnitPrice | UNIT_PRICE | — | ✅ |
| 37 | ShipmentNumber | SHIPMENT_NUMBER | 🔑 | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
