---
id: DOC-PO-PVO-NegotiationAwardAcceptancePVO
doc_type: system-doc
title: "NegotiationAwardAcceptancePVO — PVO Purchasing"
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
  - NegotiationAwardAcceptancePVO
  - negotiationawardacceptancepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationAwardAcceptancePVO

## 📌 Visão Geral

Extrai as aceitações de adjudicação por fornecedores em negociações, com status, datas e valores. Permite monitorar se fornecedores vencedores aceitaram os termos e rastrear pendências de formalização.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.NegotiationAwardAcceptancePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 495 | 7 | 1 | 495 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[egp_categories_vl|EGP_CATEGORIES_VL]] — 3 atributos (3 BICC)
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 25 atributos (25 BICC)
- [[pon_acceptances|PON_ACCEPTANCES]] — 13 atributos (1 PKs, 13 BICC)
- [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]] — 210 atributos (210 BICC)
- [[pon_auction_item_prices_all|PON_AUCTION_ITEM_PRICES_ALL]] — 94 atributos (94 BICC)
- [[pon_bid_headers|PON_BID_HEADERS]] — 72 atributos (72 BICC)
- [[pon_bid_item_prices|PON_BID_ITEM_PRICES]] — 78 atributos (78 BICC)

---

## ⚙️ Atributos

### [[egp_categories_vl|EGP_CATEGORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryCategoryId | CATEGORY_ID | — | ✅ |
| 2 | CategoryCategoryName | CATEGORY_NAME | — | ✅ |
| 3 | CategoryDescription | DESCRIPTION | — | ✅ |

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
| 9 | DailyConversionTypeNegoHdrObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | DailyConversionTypeNegoHdrPivotCurrencyCode | PIVOT_CURRENCY_CODE | — | ✅ |
| 11 | DailyConversionTypeNegoHdrSecurityFlag | SECURITY_FLAG | — | ✅ |
| 12 | DailyConversionTypeNegoHdrUserConversionType | USER_CONVERSION_TYPE | — | ✅ |
| 13 | DailyConversionTypeNegoHdrUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | ✅ |
| 14 | DailyConversionTypeResHdrConversionType | CONVERSION_TYPE | — | ✅ |
| 15 | DailyConversionTypeResHdrDescription | DESCRIPTION | — | ✅ |
| 16 | DailyConversionTypeResHdrEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | ✅ |
| 17 | DailyConversionTypeResHdrEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | ✅ |
| 18 | DailyConversionTypeResHdrFemEnabledFlag | FEM_ENABLED_FLAG | — | ✅ |
| 19 | DailyConversionTypeResHdrFemRateTypeCode | FEM_RATE_TYPE_CODE | — | ✅ |
| 20 | DailyConversionTypeResHdrFemScenario | FEM_SCENARIO | — | ✅ |
| 21 | DailyConversionTypeResHdrFemTimeframe | FEM_TIMEFRAME | — | ✅ |
| 22 | DailyConversionTypeResHdrPivotCurrencyCode | PIVOT_CURRENCY_CODE | — | ✅ |
| 23 | DailyConversionTypeResHdrSecurityFlag | SECURITY_FLAG | — | ✅ |
| 24 | DailyConversionTypeResHdrUserConversionType | USER_CONVERSION_TYPE | — | ✅ |
| 25 | DailyConversionTypeResHdrUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | ✅ |

### [[pon_acceptances|PON_ACCEPTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcceptanceId | ACCEPTANCE_ID | 🔑 | ✅ |
| 2 | AwardsAcceptanceDate | ACCEPTANCE_DATE | — | ✅ |
| 3 | AwardsAcceptanceType | ACCEPTANCE_TYPE | — | ✅ |
| 4 | AwardsAuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 5 | AwardsBidNumber | BID_NUMBER | — | ✅ |
| 6 | AwardsCreatedBy | CREATED_BY | — | ✅ |
| 7 | AwardsCreationDate | CREATION_DATE | — | ✅ |
| 8 | AwardsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | AwardsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | AwardsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | AwardsLineNumber | LINE_NUMBER | — | ✅ |
| 12 | AwardsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | AwardsReason | REASON | — | ✅ |

### [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationHeaderAbstractDetails | ABSTRACT_DETAILS | — | ✅ |
| 2 | NegotiationHeaderAbstractStatus | ABSTRACT_STATUS | — | ✅ |
| 3 | NegotiationHeaderAdvanceNegotiableFlag | ADVANCE_NEGOTIABLE_FLAG | — | ✅ |
| 4 | NegotiationHeaderAllowOtherBidCurrencyFlag | ALLOW_OTHER_BID_CURRENCY_FLAG | — | ✅ |
| 5 | NegotiationHeaderAmendmentDescription | AMENDMENT_DESCRIPTION | — | ✅ |
| 6 | NegotiationHeaderAmendmentNumber | AMENDMENT_NUMBER | — | ✅ |
| 7 | NegotiationHeaderApprovalStatus | NEG_APPROVAL_STATUS | — | ✅ |
| 8 | NegotiationHeaderAttributeLineNumber | ATTRIBUTE_LINE_NUMBER | — | ✅ |
| 9 | NegotiationHeaderAttributesExist | ATTRIBUTES_EXIST | — | ✅ |
| 10 | NegotiationHeaderAuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 11 | NegotiationHeaderAuctionHeaderIdOrigAmend | AUCTION_HEADER_ID_ORIG_AMEND | — | ✅ |
| 12 | NegotiationHeaderAuctionHeaderIdOrigRound | AUCTION_HEADER_ID_ORIG_ROUND | — | ✅ |
| 13 | NegotiationHeaderAuctionHeaderIdPrevAmend | AUCTION_HEADER_ID_PREV_AMEND | — | ✅ |
| 14 | NegotiationHeaderAuctionHeaderIdPrevRound | AUCTION_HEADER_ID_PREV_ROUND | — | ✅ |
| 15 | NegotiationHeaderAuctionOriginationCode | AUCTION_ORIGINATION_CODE | — | ✅ |
| 16 | NegotiationHeaderAuctionRoundNumber | AUCTION_ROUND_NUMBER | — | ✅ |
| 17 | NegotiationHeaderAuctionStatus | AUCTION_STATUS | — | ✅ |
| 18 | NegotiationHeaderAuctionTitle | AUCTION_TITLE | — | ✅ |
| 19 | NegotiationHeaderAutoExtendAllLinesFlag | AUTO_EXTEND_ALL_LINES_FLAG | — | ✅ |
| 20 | NegotiationHeaderAutoExtendDuration | AUTO_EXTEND_DURATION | — | ✅ |
| 21 | NegotiationHeaderAutoExtendEnabledFlag | AUTO_EXTEND_ENABLED_FLAG | — | ✅ |
| 22 | NegotiationHeaderAutoExtendFlag | AUTO_EXTEND_FLAG | — | ✅ |
| 23 | NegotiationHeaderAutoExtendMinTriggerRank | AUTO_EXTEND_MIN_TRIGGER_RANK | — | ✅ |
| 24 | NegotiationHeaderAutoExtendNumber | AUTO_EXTEND_NUMBER | — | ✅ |
| 25 | NegotiationHeaderAutoExtendTypeFlag | AUTO_EXTEND_TYPE_FLAG | — | ✅ |
| 26 | NegotiationHeaderAutoextendChangedFlag | AUTOEXTEND_CHANGED_FLAG | — | ✅ |
| 27 | NegotiationHeaderAwardApprAmeTransId | AWARD_APPR_AME_TRANS_ID | — | ✅ |
| 28 | NegotiationHeaderAwardApprAmeTransPrevId | AWARD_APPR_AME_TRANS_PREV_ID | — | ✅ |
| 29 | NegotiationHeaderAwardApprAmeTxnDate | AWARD_APPR_AME_TXN_DATE | — | ✅ |
| 30 | NegotiationHeaderAwardApprovalFlag | AWARD_APPROVAL_FLAG | — | ✅ |
| 31 | NegotiationHeaderAwardApprovalStatus | AWARD_APPROVAL_STATUS | — | ✅ |
| 32 | NegotiationHeaderAwardByDate | AWARD_BY_DATE | — | ✅ |
| 33 | NegotiationHeaderAwardCompleteDate | AWARD_COMPLETE_DATE | — | ✅ |
| 34 | NegotiationHeaderAwardDate | AWARD_DATE | — | ✅ |
| 35 | NegotiationHeaderAwardMode | AWARD_MODE | — | ✅ |
| 36 | NegotiationHeaderAwardStatus | AWARD_STATUS | — | ✅ |
| 37 | NegotiationHeaderBidDecrementMethod | BID_DECREMENT_METHOD | — | ✅ |
| 38 | NegotiationHeaderBidFrequencyCode | BID_FREQUENCY_CODE | — | ✅ |
| 39 | NegotiationHeaderBidListType | BID_LIST_TYPE | — | ✅ |
| 40 | NegotiationHeaderBidRanking | BID_RANKING | — | ✅ |
| 41 | NegotiationHeaderBidScopeCode | BID_SCOPE_CODE | — | ✅ |
| 42 | NegotiationHeaderBidVisibilityCode | BID_VISIBILITY_CODE | — | ✅ |
| 43 | NegotiationHeaderCancelDate | CANCEL_DATE | — | ✅ |
| 44 | NegotiationHeaderCarrierId | CARRIER_ID | — | ✅ |
| 45 | NegotiationHeaderCloseBiddingDate | CLOSE_BIDDING_DATE | — | ✅ |
| 46 | NegotiationHeaderCompleteFlag | COMPLETE_FLAG | — | ✅ |
| 47 | NegotiationHeaderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | ✅ |
| 48 | NegotiationHeaderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | ✅ |
| 49 | NegotiationHeaderContermsExistFlag | CONTERMS_EXIST_FLAG | — | ✅ |
| 50 | NegotiationHeaderContractTemplateId | CONTRACT_TEMPLATE_ID | — | ✅ |
| 51 | NegotiationHeaderContractType | CONTRACT_TYPE | — | ✅ |
| 52 | NegotiationHeaderCreatedBy | CREATED_BY | — | ✅ |
| 53 | NegotiationHeaderCreationDate | CREATION_DATE | — | ✅ |
| 54 | NegotiationHeaderCreationDateOrigAmend | CREATION_DATE_ORIG_AMEND | — | ✅ |
| 55 | NegotiationHeaderCurrencyCode | CURRENCY_CODE | — | ✅ |
| 56 | NegotiationHeaderDescription | DESCRIPTION | — | ✅ |
| 57 | NegotiationHeaderDisplayBestPriceBlindFlag | DISPLAY_BEST_PRICE_BLIND_FLAG | — | ✅ |
| 58 | NegotiationHeaderDoctypeId | DOCTYPE_ID | — | ✅ |
| 59 | NegotiationHeaderDocumentNumber | DOCUMENT_NUMBER | — | ✅ |
| 60 | NegotiationHeaderDraftLocked | DRAFT_LOCKED | — | ✅ |
| 61 | NegotiationHeaderDraftLockedDate | DRAFT_LOCKED_DATE | — | ✅ |
| 62 | NegotiationHeaderDraftUnlockedDate | DRAFT_UNLOCKED_DATE | — | ✅ |
| 63 | NegotiationHeaderEnforcePrevrndBidPriceFlag | ENFORCE_PREVRND_BID_PRICE_FLAG | — | ✅ |
| 64 | NegotiationHeaderEventId | EVENT_ID | — | ✅ |
| 65 | NegotiationHeaderEventTitle | EVENT_TITLE | — | ✅ |
| 66 | NegotiationHeaderExtAttribute1 | EXT_ATTRIBUTE1 | — | ✅ |
| 67 | NegotiationHeaderExtAttribute10 | EXT_ATTRIBUTE10 | — | ✅ |
| 68 | NegotiationHeaderExtAttribute11 | EXT_ATTRIBUTE11 | — | ✅ |
| 69 | NegotiationHeaderExtAttribute12 | EXT_ATTRIBUTE12 | — | ✅ |
| 70 | NegotiationHeaderExtAttribute13 | EXT_ATTRIBUTE13 | — | ✅ |
| 71 | NegotiationHeaderExtAttribute14 | EXT_ATTRIBUTE14 | — | ✅ |
| 72 | NegotiationHeaderExtAttribute15 | EXT_ATTRIBUTE15 | — | ✅ |
| 73 | NegotiationHeaderExtAttribute2 | EXT_ATTRIBUTE2 | — | ✅ |
| 74 | NegotiationHeaderExtAttribute3 | EXT_ATTRIBUTE3 | — | ✅ |
| 75 | NegotiationHeaderExtAttribute4 | EXT_ATTRIBUTE4 | — | ✅ |
| 76 | NegotiationHeaderExtAttribute5 | EXT_ATTRIBUTE5 | — | ✅ |
| 77 | NegotiationHeaderExtAttribute6 | EXT_ATTRIBUTE6 | — | ✅ |
| 78 | NegotiationHeaderExtAttribute7 | EXT_ATTRIBUTE7 | — | ✅ |
| 79 | NegotiationHeaderExtAttribute8 | EXT_ATTRIBUTE8 | — | ✅ |
| 80 | NegotiationHeaderExtAttribute9 | EXT_ATTRIBUTE9 | — | ✅ |
| 81 | NegotiationHeaderExtAttributeCategory | EXT_ATTRIBUTE_CATEGORY | — | ✅ |
| 82 | NegotiationHeaderFirstLineCloseDate | FIRST_LINE_CLOSE_DATE | — | ✅ |
| 83 | NegotiationHeaderFobCode | FOB_CODE | — | ✅ |
| 84 | NegotiationHeaderFreightTermsCode | FREIGHT_TERMS_CODE | — | ✅ |
| 85 | NegotiationHeaderFullQuantityBidCode | FULL_QUANTITY_BID_CODE | — | ✅ |
| 86 | NegotiationHeaderGlobalTemplateFlag | GLOBAL_TEMPLATE_FLAG | — | ✅ |
| 87 | NegotiationHeaderGroupEnabledFlag | GROUP_ENABLED_FLAG | — | ✅ |
| 88 | NegotiationHeaderHasHdrAttrFlag | HAS_HDR_ATTR_FLAG | — | ✅ |
| 89 | NegotiationHeaderHasItemsFlag | HAS_ITEMS_FLAG | — | ✅ |
| 90 | NegotiationHeaderHasPeForAllItems | HAS_PE_FOR_ALL_ITEMS | — | ✅ |
| 91 | NegotiationHeaderHasPriceElements | HAS_PRICE_ELEMENTS | — | ✅ |
| 92 | NegotiationHeaderHasScoringTeamsFlag | HAS_SCORING_TEAMS_FLAG | — | ✅ |
| 93 | NegotiationHeaderHdrAttrDisplayScore | HDR_ATTR_DISPLAY_SCORE | — | ✅ |
| 94 | NegotiationHeaderHdrAttrEnableWeights | HDR_ATTR_ENABLE_WEIGHTS | — | ✅ |
| 95 | NegotiationHeaderHdrAttrMaximumScore | HDR_ATTR_MAXIMUM_SCORE | — | ✅ |
| 96 | NegotiationHeaderHdrAttributeEnabledFlag | HDR_ATTRIBUTE_ENABLED_FLAG | — | ✅ |
| 97 | NegotiationHeaderImportFileName | IMPORT_FILE_NAME | — | ✅ |
| 98 | NegotiationHeaderIncludePdfInExternalPage | INCLUDE_PDF_IN_EXTERNAL_PAGE | — | ✅ |
| 99 | NegotiationHeaderIntAttribute1 | INT_ATTRIBUTE1 | — | ✅ |
| 100 | NegotiationHeaderIntAttribute10 | INT_ATTRIBUTE10 | — | ✅ |
| 101 | NegotiationHeaderIntAttribute11 | INT_ATTRIBUTE11 | — | ✅ |
| 102 | NegotiationHeaderIntAttribute12 | INT_ATTRIBUTE12 | — | ✅ |
| 103 | NegotiationHeaderIntAttribute13 | INT_ATTRIBUTE13 | — | ✅ |
| 104 | NegotiationHeaderIntAttribute14 | INT_ATTRIBUTE14 | — | ✅ |
| 105 | NegotiationHeaderIntAttribute15 | INT_ATTRIBUTE15 | — | ✅ |
| 106 | NegotiationHeaderIntAttribute2 | INT_ATTRIBUTE2 | — | ✅ |
| 107 | NegotiationHeaderIntAttribute3 | INT_ATTRIBUTE3 | — | ✅ |
| 108 | NegotiationHeaderIntAttribute4 | INT_ATTRIBUTE4 | — | ✅ |
| 109 | NegotiationHeaderIntAttribute5 | INT_ATTRIBUTE5 | — | ✅ |
| 110 | NegotiationHeaderIntAttribute6 | INT_ATTRIBUTE6 | — | ✅ |
| 111 | NegotiationHeaderIntAttribute7 | INT_ATTRIBUTE7 | — | ✅ |
| 112 | NegotiationHeaderIntAttribute8 | INT_ATTRIBUTE8 | — | ✅ |
| 113 | NegotiationHeaderIntAttribute9 | INT_ATTRIBUTE9 | — | ✅ |
| 114 | NegotiationHeaderIntAttributeCategory | INT_ATTRIBUTE_CATEGORY | — | ✅ |
| 115 | NegotiationHeaderIsPaused | IS_PAUSED | — | ✅ |
| 116 | NegotiationHeaderIsTemplateFlag | IS_TEMPLATE_FLAG | — | ✅ |
| 117 | NegotiationHeaderLanguageCode | LANGUAGE_CODE | — | ✅ |
| 118 | NegotiationHeaderLargeNegEnabledFlag | LARGE_NEG_ENABLED_FLAG | — | ✅ |
| 119 | NegotiationHeaderLastLineNumber | LAST_LINE_NUMBER | — | ✅ |
| 120 | NegotiationHeaderLastPauseDate | LAST_PAUSE_DATE | — | ✅ |
| 121 | NegotiationHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 122 | NegotiationHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 123 | NegotiationHeaderLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 124 | NegotiationHeaderLineAttributeEnabledFlag | LINE_ATTRIBUTE_ENABLED_FLAG | — | ✅ |
| 125 | NegotiationHeaderLineMasEnabledFlag | LINE_MAS_ENABLED_FLAG | — | ✅ |
| 126 | NegotiationHeaderLotEnabledFlag | LOT_ENABLED_FLAG | — | ✅ |
| 127 | NegotiationHeaderMaxBidColorSequenceId | MAX_BID_COLOR_SEQUENCE_ID | — | ✅ |
| 128 | NegotiationHeaderMaxDocumentLineNum | MAX_DOCUMENT_LINE_NUM | — | ✅ |
| 129 | NegotiationHeaderMaxInternalLineNum | MAX_INTERNAL_LINE_NUM | — | ✅ |
| 130 | NegotiationHeaderMaxRetainageNegotiableFlag | MAX_RETAINAGE_NEGOTIABLE_FLAG | — | ✅ |
| 131 | NegotiationHeaderMinBidChangeType | MIN_BID_CHANGE_TYPE | — | ✅ |
| 132 | NegotiationHeaderMinBidDecrement | MIN_BID_DECREMENT | — | ✅ |
| 133 | NegotiationHeaderNegTeamEnabledFlag | NEG_TEAM_ENABLED_FLAG | — | ✅ |
| 134 | NegotiationHeaderNumberOfBids | NUMBER_OF_BIDS | — | ✅ |
| 135 | NegotiationHeaderNumberOfExtensions | NUMBER_OF_EXTENSIONS | — | ✅ |
| 136 | NegotiationHeaderNumberOfLines | NUMBER_OF_LINES | — | ✅ |
| 137 | NegotiationHeaderNumberPriceDecimals | NUMBER_PRICE_DECIMALS | — | ✅ |
| 138 | NegotiationHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 139 | NegotiationHeaderOpenAuctionNowFlag | OPEN_AUCTION_NOW_FLAG | — | ✅ |
| 140 | NegotiationHeaderOpenBiddingDate | OPEN_BIDDING_DATE | — | ✅ |
| 141 | NegotiationHeaderOriginalCloseBiddingDate | ORIGINAL_CLOSE_BIDDING_DATE | — | ✅ |
| 142 | NegotiationHeaderOutcomeStatus | OUTCOME_STATUS | — | ✅ |
| 143 | NegotiationHeaderPauseRemarks | PAUSE_REMARKS | — | ✅ |
| 144 | NegotiationHeaderPaymentTermsId | PAYMENT_TERMS_ID | — | ✅ |
| 145 | NegotiationHeaderPfTypeAllowed | PF_TYPE_ALLOWED | — | ✅ |
| 146 | NegotiationHeaderPoAgreedAmount | PO_AGREED_AMOUNT | — | ✅ |
| 147 | NegotiationHeaderPoEndDate | PO_END_DATE | — | ✅ |
| 148 | NegotiationHeaderPoMinRelAmount | PO_MIN_REL_AMOUNT | — | ✅ |
| 149 | NegotiationHeaderPoStartDate | PO_START_DATE | — | ✅ |
| 150 | NegotiationHeaderPoStyleId | PO_STYLE_ID | — | ✅ |
| 151 | NegotiationHeaderPowerBiddingEnabledFlag | POWER_BIDDING_ENABLED_FLAG | — | ✅ |
| 152 | NegotiationHeaderPrcBuId | PRC_BU_ID | — | ✅ |
| 153 | NegotiationHeaderPriceDrivenAuctionFlag | PRICE_DRIVEN_AUCTION_FLAG | — | ✅ |
| 154 | NegotiationHeaderPriceElementEnabledFlag | PRICE_ELEMENT_ENABLED_FLAG | — | ✅ |
| 155 | NegotiationHeaderPriceTiersIndicator | PRICE_TIERS_INDICATOR | — | ✅ |
| 156 | NegotiationHeaderProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 157 | NegotiationHeaderProgramName | PROGRAM_NAME | — | ✅ |
| 158 | NegotiationHeaderProgressPaymentType | PROGRESS_PAYMENT_TYPE | — | ✅ |
| 159 | NegotiationHeaderProgressPymtNegotiableFlag | PROGRESS_PYMT_NEGOTIABLE_FLAG | — | ✅ |
| 160 | NegotiationHeaderProjectId | PROJECT_ID | — | ✅ |
| 161 | NegotiationHeaderProxyBiddingEnabledFlag | PROXY_BIDDING_ENABLED_FLAG | — | ✅ |
| 162 | NegotiationHeaderPublishAuctionNowFlag | PUBLISH_AUCTION_NOW_FLAG | — | ✅ |
| 163 | NegotiationHeaderPublishDate | PUBLISH_DATE | — | ✅ |
| 164 | NegotiationHeaderPublishDateOrigAmend | PUBLISH_DATE_ORIG_AMEND | — | ✅ |
| 165 | NegotiationHeaderPublishRatesToBiddersFlag | PUBLISH_RATES_TO_BIDDERS_FLAG | — | ✅ |
| 166 | NegotiationHeaderQtyPriceTiersEnabledFlag | QTY_PRICE_TIERS_ENABLED_FLAG | — | ✅ |
| 167 | NegotiationHeaderRankIndicator | RANK_INDICATOR | — | ✅ |
| 168 | NegotiationHeaderRateDate | RATE_DATE | — | ✅ |
| 169 | NegotiationHeaderRateType | RATE_TYPE | — | ✅ |
| 170 | NegotiationHeaderRecoupmentNegotiableFlag | RECOUPMENT_NEGOTIABLE_FLAG | — | ✅ |
| 171 | NegotiationHeaderReminderDate | REMINDER_DATE | — | ✅ |
| 172 | NegotiationHeaderRequestDate | REQUEST_DATE | — | ✅ |
| 173 | NegotiationHeaderRequestId | REQUEST_ID | — | ✅ |
| 174 | NegotiationHeaderRequestedBy | REQUESTED_BY | — | ✅ |
| 175 | NegotiationHeaderRetainageNegotiableFlag | RETAINAGE_NEGOTIABLE_FLAG | — | ✅ |
| 176 | NegotiationHeaderRfiLineEnabledFlag | RFI_LINE_ENABLED_FLAG | — | ✅ |
| 177 | NegotiationHeaderScoringLockDate | SCORING_LOCK_DATE | — | ✅ |
| 178 | NegotiationHeaderSealedActualUnlockDate | SEALED_ACTUAL_UNLOCK_DATE | — | ✅ |
| 179 | NegotiationHeaderSealedActualUnsealDate | SEALED_ACTUAL_UNSEAL_DATE | — | ✅ |
| 180 | NegotiationHeaderSealedAuctionStatus | SEALED_AUCTION_STATUS | — | ✅ |
| 181 | NegotiationHeaderShareAwardDecision | SHARE_AWARD_DECISION | — | ✅ |
| 182 | NegotiationHeaderShowBidderNotes | SHOW_BIDDER_NOTES | — | ✅ |
| 183 | NegotiationHeaderShowBidderScores | SHOW_BIDDER_SCORES | — | ✅ |
| 184 | NegotiationHeaderSourceDocId | SOURCE_DOC_ID | — | ✅ |
| 185 | NegotiationHeaderSourceDocLineMsg | SOURCE_DOC_LINE_MSG | — | ✅ |
| 186 | NegotiationHeaderSourceDocMsg | SOURCE_DOC_MSG | — | ✅ |
| 187 | NegotiationHeaderSourceDocMsgApp | SOURCE_DOC_MSG_APP | — | ✅ |
| 188 | NegotiationHeaderSourceDocNumber | SOURCE_DOC_NUMBER | — | ✅ |
| 189 | NegotiationHeaderSourceReqsFlag | SOURCE_REQS_FLAG | — | ✅ |
| 190 | NegotiationHeaderStaggeredClosingInterval | STAGGERED_CLOSING_INTERVAL | — | ✅ |
| 191 | NegotiationHeaderStyleId | STYLE_ID | — | ✅ |
| 192 | NegotiationHeaderSupplierEnterablePymtFlag | SUPPLIER_ENTERABLE_PYMT_FLAG | — | ✅ |
| 193 | NegotiationHeaderSupplierViewType | SUPPLIER_VIEW_TYPE | — | ✅ |
| 194 | NegotiationHeaderTeamScoringEnabledFlag | TEAM_SCORING_ENABLED_FLAG | — | ✅ |
| 195 | NegotiationHeaderTechnicalActualUnlockDate | TECHNICAL_ACTUAL_UNLOCK_DATE | — | ✅ |
| 196 | NegotiationHeaderTechnicalActualUnsealDate | TECHNICAL_ACTUAL_UNSEAL_DATE | — | ✅ |
| 197 | NegotiationHeaderTechnicalEvaluationStatus | TECHNICAL_EVALUATION_STATUS | — | ✅ |
| 198 | NegotiationHeaderTechnicalLockStatus | TECHNICAL_LOCK_STATUS | — | ✅ |
| 199 | NegotiationHeaderTemplateId | TEMPLATE_ID | — | ✅ |
| 200 | NegotiationHeaderTemplateScope | TEMPLATE_SCOPE | — | ✅ |
| 201 | NegotiationHeaderTemplateStatus | TEMPLATE_STATUS | — | ✅ |
| 202 | NegotiationHeaderTwoPartFlag | TWO_PART_FLAG | — | ✅ |
| 203 | NegotiationHeaderVersionNum | VERSION_NUM | — | ✅ |
| 204 | NegotiationHeaderViewByDate | VIEW_BY_DATE | — | ✅ |
| 205 | NegotiationHeaderWfApprovalItemKey | WF_APPROVAL_ITEM_KEY | — | ✅ |
| 206 | NegotiationHeaderWfAwardApprovalItemKey | WF_AWARD_APPROVAL_ITEM_KEY | — | ✅ |
| 207 | NegotiationHeaderWfItemKey | WF_ITEM_KEY | — | ✅ |
| 208 | NegotiationHeaderWfPoncomplCurrentRound | WF_PONCOMPL_CURRENT_ROUND | — | ✅ |
| 209 | NegotiationHeaderWfPoncomplItemKey | WF_PONCOMPL_ITEM_KEY | — | ✅ |
| 210 | NegotiationHeaderWfRoleName | WF_ROLE_NAME | — | ✅ |

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
| 82 | NegotiationLineRequisitionNumber | REQUISITION_NUMBER | — | ✅ |
| 83 | NegotiationLineRetainageRatePercent | RETAINAGE_RATE_PERCENT | — | ✅ |
| 84 | NegotiationLineShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 85 | NegotiationLineSourceDocId | SOURCE_DOC_ID | — | ✅ |
| 86 | NegotiationLineSourceDocNumber | SOURCE_DOC_NUMBER | — | ✅ |
| 87 | NegotiationLineSourceLineId | SOURCE_LINE_ID | — | ✅ |
| 88 | NegotiationLineSourceLineNumber | SOURCE_LINE_NUMBER | — | ✅ |
| 89 | NegotiationLineSubLineSequenceNumber | SUB_LINE_SEQUENCE_NUMBER | — | ✅ |
| 90 | NegotiationLineTargetPrice | TARGET_PRICE | — | ✅ |
| 91 | NegotiationLineUnitDisplayTargetFlag | UNIT_DISPLAY_TARGET_FLAG | — | ✅ |
| 92 | NegotiationLineUnitTargetPrice | UNIT_TARGET_PRICE | — | ✅ |
| 93 | NegotiationLineUomCode | UOM_CODE | — | ✅ |
| 94 | NegotiationLineWorkApproverUserId | WORK_APPROVER_USER_ID | — | ✅ |

### [[pon_bid_headers|PON_BID_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResponseHeaderAttributeLineNumber | ATTRIBUTE_LINE_NUMBER | — | ✅ |
| 2 | ResponseHeaderAuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 3 | ResponseHeaderAwardDate | AWARD_DATE | — | ✅ |
| 4 | ResponseHeaderAwardStatus | AWARD_STATUS | — | ✅ |
| 5 | ResponseHeaderBidCurrencyCode | BID_CURRENCY_CODE | — | ✅ |
| 6 | ResponseHeaderBidExpirationDate | BID_EXPIRATION_DATE | — | ✅ |
| 7 | ResponseHeaderBidNumber | BID_NUMBER | — | ✅ |
| 8 | ResponseHeaderBidStatus | BID_STATUS | — | ✅ |
| 9 | ResponseHeaderBiddersBidNumber | BIDDERS_BID_NUMBER | — | ✅ |
| 10 | ResponseHeaderBuyerBidTotal | BUYER_BID_TOTAL | — | ✅ |
| 11 | ResponseHeaderCancelReason | CANCEL_REASON | — | ✅ |
| 12 | ResponseHeaderCancelledDate | CANCELLED_DATE | — | ✅ |
| 13 | ResponseHeaderColorSequenceId | COLOR_SEQUENCE_ID | — | ✅ |
| 14 | ResponseHeaderCreatedBy | CREATED_BY | — | ✅ |
| 15 | ResponseHeaderCreationDate | CREATION_DATE | — | ✅ |
| 16 | ResponseHeaderCurrentRebate | CURRENT_REBATE | — | ✅ |
| 17 | ResponseHeaderCurrentTotalSpend | CURRENT_TOTAL_SPEND | — | ✅ |
| 18 | ResponseHeaderDisplayPriceFactorsFlag | DISPLAY_PRICE_FACTORS_FLAG | — | ✅ |
| 19 | ResponseHeaderDisqualifyReason | DISQUALIFY_REASON | — | ✅ |
| 20 | ResponseHeaderDraftLocked | DRAFT_LOCKED | — | ✅ |
| 21 | ResponseHeaderDraftLockedBy | DRAFT_LOCKED_BY | — | ✅ |
| 22 | ResponseHeaderDraftLockedByContactId | DRAFT_LOCKED_BY_CONTACT_ID | — | ✅ |
| 23 | ResponseHeaderDraftLockedDate | DRAFT_LOCKED_DATE | — | ✅ |
| 24 | ResponseHeaderDraftUnlockedBy | DRAFT_UNLOCKED_BY | — | ✅ |
| 25 | ResponseHeaderDraftUnlockedByContactId | DRAFT_UNLOCKED_BY_CONTACT_ID | — | ✅ |
| 26 | ResponseHeaderDraftUnlockedDate | DRAFT_UNLOCKED_DATE | — | ✅ |
| 27 | ResponseHeaderFixedIncentive | FIXED_INCENTIVE | — | ✅ |
| 28 | ResponseHeaderHasRebateTiers | HAS_REBATE_TIERS | — | ✅ |
| 29 | ResponseHeaderImportFileName | IMPORT_FILE_NAME | — | ✅ |
| 30 | ResponseHeaderIncumbentFlag | INCUMBENT_FLAG | — | ✅ |
| 31 | ResponseHeaderInternalNote | INTERNAL_NOTE | — | ✅ |
| 32 | ResponseHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 33 | ResponseHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 34 | ResponseHeaderLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 35 | ResponseHeaderMinBidChange | MIN_BID_CHANGE | — | ✅ |
| 36 | ResponseHeaderNoteToAuctionOwner | NOTE_TO_AUCTION_OWNER | — | ✅ |
| 37 | ResponseHeaderNoteToSupplier | NOTE_TO_SUPPLIER | — | ✅ |
| 38 | ResponseHeaderNumberPriceDecimals | NUMBER_PRICE_DECIMALS | — | ✅ |
| 39 | ResponseHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 40 | ResponseHeaderOldBidExpirationDate | OLD_BID_EXPIRATION_DATE | — | ✅ |
| 41 | ResponseHeaderOldBidNumber | OLD_BID_NUMBER | — | ✅ |
| 42 | ResponseHeaderOldBidStatus | OLD_BID_STATUS | — | ✅ |
| 43 | ResponseHeaderOldBiddersBidNumber | OLD_BIDDERS_BID_NUMBER | — | ✅ |
| 44 | ResponseHeaderOldMinBidChange | OLD_MIN_BID_CHANGE | — | ✅ |
| 45 | ResponseHeaderOldNoteToAuctionOwner | OLD_NOTE_TO_AUCTION_OWNER | — | ✅ |
| 46 | ResponseHeaderOldSurrogBidReceiptDate | OLD_SURROG_BID_RECEIPT_DATE | — | ✅ |
| 47 | ResponseHeaderPartialResponseFlag | PARTIAL_RESPONSE_FLAG | — | ✅ |
| 48 | ResponseHeaderPoAgreedAmount | PO_AGREED_AMOUNT | — | ✅ |
| 49 | ResponseHeaderProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 50 | ResponseHeaderProgramName | PROGRAM_NAME | — | ✅ |
| 51 | ResponseHeaderProxyBidFlag | PROXY_BID_FLAG | — | ✅ |
| 52 | ResponseHeaderPublishDate | PUBLISH_DATE | — | ✅ |
| 53 | ResponseHeaderRate | RATE | — | ✅ |
| 54 | ResponseHeaderRateDate | RATE_DATE | — | ✅ |
| 55 | ResponseHeaderRateDsp | RATE_DSP | — | ✅ |
| 56 | ResponseHeaderRateType | RATE_TYPE | — | ✅ |
| 57 | ResponseHeaderRequestDate | REQUEST_DATE | — | ✅ |
| 58 | ResponseHeaderRequestId | REQUEST_ID | — | ✅ |
| 59 | ResponseHeaderRequestedBy | REQUESTED_BY | — | ✅ |
| 60 | ResponseHeaderScoreOverridenDate | SCORE_OVERRIDEN_DATE | — | ✅ |
| 61 | ResponseHeaderScoreOverridenFlag | SCORE_OVERRIDEN_FLAG | — | ✅ |
| 62 | ResponseHeaderShortlistFlag | SHORTLIST_FLAG | — | ✅ |
| 63 | ResponseHeaderSurrogBidCreatedPersonId | SURROG_BID_CREATED_PERSON_ID | — | ✅ |
| 64 | ResponseHeaderSurrogBidFlag | SURROG_BID_FLAG | — | ✅ |
| 65 | ResponseHeaderSurrogBidOnlineEntryDate | SURROG_BID_ONLINE_ENTRY_DATE | — | ✅ |
| 66 | ResponseHeaderSurrogBidReceiptDate | SURROG_BID_RECEIPT_DATE | — | ✅ |
| 67 | ResponseHeaderTechnicalShortlistFlag | TECHNICAL_SHORTLIST_FLAG | — | ✅ |
| 68 | ResponseHeaderTotalAwardAmount | TOTAL_AWARD_AMOUNT | — | ✅ |
| 69 | ResponseHeaderTradingPartnerContactId | TRADING_PARTNER_CONTACT_ID | — | ✅ |
| 70 | ResponseHeaderTradingPartnerId | TRADING_PARTNER_ID | — | ✅ |
| 71 | ResponseHeaderVendorId | VENDOR_ID | — | ✅ |
| 72 | ResponseHeaderVendorSiteId | VENDOR_SITE_ID | — | ✅ |

### [[pon_bid_item_prices|PON_BID_ITEM_PRICES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResponseLineAdvanceAmount | ADVANCE_AMOUNT | — | ✅ |
| 2 | ResponseLineAuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 3 | ResponseLineAwardDate | AWARD_DATE | — | ✅ |
| 4 | ResponseLineAwardPrice | AWARD_PRICE | — | ✅ |
| 5 | ResponseLineAwardQuantity | AWARD_QUANTITY | — | ✅ |
| 6 | ResponseLineAwardShipmentNumber | AWARD_SHIPMENT_NUMBER | — | ✅ |
| 7 | ResponseLineAwardStatus | AWARD_STATUS | — | ✅ |
| 8 | ResponseLineBatchId | BATCH_ID | — | ✅ |
| 9 | ResponseLineBidCurrAdvanceAmount | BID_CURR_ADVANCE_AMOUNT | — | ✅ |
| 10 | ResponseLineBidCurrMaxRetainageAmt | BID_CURR_MAX_RETAINAGE_AMT | — | ✅ |
| 11 | ResponseLineBidCurrencyLimitPrice | BID_CURRENCY_LIMIT_PRICE | — | ✅ |
| 12 | ResponseLineBidCurrencyPrice | BID_CURRENCY_PRICE | — | ✅ |
| 13 | ResponseLineBidCurrencyTransPrice | BID_CURRENCY_TRANS_PRICE | — | ✅ |
| 14 | ResponseLineBidCurrencyUnitPrice | BID_CURRENCY_UNIT_PRICE | — | ✅ |
| 15 | ResponseLineBidNumber | BID_NUMBER | — | ✅ |
| 16 | ResponseLineBidStartPrice | BID_START_PRICE | — | ✅ |
| 17 | ResponseLineCancelledLimitPrice | CANCELLED_LIMIT_PRICE | — | ✅ |
| 18 | ResponseLineCopyPriceForProxyFlag | COPY_PRICE_FOR_PROXY_FLAG | — | ✅ |
| 19 | ResponseLineCreatedBy | CREATED_BY | — | ✅ |
| 20 | ResponseLineCreationDate | CREATION_DATE | — | ✅ |
| 21 | ResponseLineDisplayPriceFactorsFlag | DISPLAY_PRICE_FACTORS_FLAG | — | ✅ |
| 22 | ResponseLineFirstBidPrice | FIRST_BID_PRICE | — | ✅ |
| 23 | ResponseLineFixedAmountComponent | FIXED_AMOUNT_COMPONENT | — | ✅ |
| 24 | ResponseLineGroupAmount | GROUP_AMOUNT | — | ✅ |
| 25 | ResponseLineHasAttributesFlag | HAS_ATTRIBUTES_FLAG | — | ✅ |
| 26 | ResponseLineHasBidFlag | HAS_BID_FLAG | — | ✅ |
| 27 | ResponseLineHasBidPaymentsFlag | HAS_BID_PAYMENTS_FLAG | — | ✅ |
| 28 | ResponseLineHasPriceDifferentialsFlag | HAS_PRICE_DIFFERENTIALS_FLAG | — | ✅ |
| 29 | ResponseLineHasQuantityTiers | HAS_QUANTITY_TIERS | — | ✅ |
| 30 | ResponseLineHasShipmentsFlag | HAS_SHIPMENTS_FLAG | — | ✅ |
| 31 | ResponseLineInterfaceLineId | INTERFACE_LINE_ID | — | ✅ |
| 32 | ResponseLineIsChangedLineFlag | IS_CHANGED_LINE_FLAG | — | ✅ |
| 33 | ResponseLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 34 | ResponseLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 35 | ResponseLineLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 36 | ResponseLineLineNumber | LINE_NUMBER | — | ✅ |
| 37 | ResponseLineMaxRetainageAmount | MAX_RETAINAGE_AMOUNT | — | ✅ |
| 38 | ResponseLineNoteToAuctionOwner | NOTE_TO_AUCTION_OWNER | — | ✅ |
| 39 | ResponseLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 40 | ResponseLineOldBidCurrAdvanceAmount | OLD_BID_CURR_ADVANCE_AMOUNT | — | ✅ |
| 41 | ResponseLineOldBidCurrMaxRetainageAmt | OLD_BID_CURR_MAX_RETAINAGE_AMT | — | ✅ |
| 42 | ResponseLineOldBidCurrencyLimitPrice | OLD_BID_CURRENCY_LIMIT_PRICE | — | ✅ |
| 43 | ResponseLineOldBidCurrencyPrice | OLD_BID_CURRENCY_PRICE | — | ✅ |
| 44 | ResponseLineOldBidCurrencyUnitPrice | OLD_BID_CURRENCY_UNIT_PRICE | — | ✅ |
| 45 | ResponseLineOldNoOfPayments | OLD_NO_OF_PAYMENTS | — | ✅ |
| 46 | ResponseLineOldNoteToAuctionOwner | OLD_NOTE_TO_AUCTION_OWNER | — | ✅ |
| 47 | ResponseLineOldPoBidMinRelAmount | OLD_PO_BID_MIN_REL_AMOUNT | — | ✅ |
| 48 | ResponseLineOldPrice | OLD_PRICE | — | ✅ |
| 49 | ResponseLineOldProgressPymtRatePercent | OLD_PROGRESS_PYMT_RATE_PERCENT | — | ✅ |
| 50 | ResponseLineOldPromisedDate | OLD_PROMISED_DATE | — | ✅ |
| 51 | ResponseLineOldPublishDate | OLD_PUBLISH_DATE | — | ✅ |
| 52 | ResponseLineOldQuantity | OLD_QUANTITY | — | ✅ |
| 53 | ResponseLineOldRecoupmentRatePercent | OLD_RECOUPMENT_RATE_PERCENT | — | ✅ |
| 54 | ResponseLineOldRetainageRatePercent | OLD_RETAINAGE_RATE_PERCENT | — | ✅ |
| 55 | ResponseLinePerUnitPriceComponent | PER_UNIT_PRICE_COMPONENT | — | ✅ |
| 56 | ResponseLinePoBidMinRelAmount | PO_BID_MIN_REL_AMOUNT | — | ✅ |
| 57 | ResponseLinePoMinRelAmount | PO_MIN_REL_AMOUNT | — | ✅ |
| 58 | ResponseLinePrice | PRICE | — | ✅ |
| 59 | ResponseLinePriceBreakType | PRICE_BREAK_TYPE | — | ✅ |
| 60 | ResponseLinePriceDiffShipmentNumber | PRICE_DIFF_SHIPMENT_NUMBER | — | ✅ |
| 61 | ResponseLineProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 62 | ResponseLineProgramName | PROGRAM_NAME | — | ✅ |
| 63 | ResponseLineProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 64 | ResponseLineProgressPymtRatePercent | PROGRESS_PYMT_RATE_PERCENT | — | ✅ |
| 65 | ResponseLinePromisedDate | PROMISED_DATE | — | ✅ |
| 66 | ResponseLineProxyBidFlag | PROXY_BID_FLAG | — | ✅ |
| 67 | ResponseLineProxyBidLimitPrice | PROXY_BID_LIMIT_PRICE | — | ✅ |
| 68 | ResponseLinePublishDate | PUBLISH_DATE | — | ✅ |
| 69 | ResponseLineQuantity | QUANTITY | — | ✅ |
| 70 | ResponseLineRank | RANK | — | ✅ |
| 71 | ResponseLineRecoupmentRatePercent | RECOUPMENT_RATE_PERCENT | — | ✅ |
| 72 | ResponseLineRequestId | REQUEST_ID | — | ✅ |
| 73 | ResponseLineRetainageRatePercent | RETAINAGE_RATE_PERCENT | — | ✅ |
| 74 | ResponseLineTotalWeightedScore | TOTAL_WEIGHTED_SCORE | — | ✅ |
| 75 | ResponseLineTriggerBidNumber | TRIGGER_BID_NUMBER | — | ✅ |
| 76 | ResponseLineUnitPrice | UNIT_PRICE | — | ✅ |
| 77 | ResponseLineWorksheetName | WORKSHEET_NAME | — | ✅ |
| 78 | ResponseLineWorksheetSequenceNumber | WORKSHEET_SEQUENCE_NUMBER | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
