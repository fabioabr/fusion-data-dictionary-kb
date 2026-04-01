---
id: DOC-PO-PVO-NegotiationPriceTierPVO
doc_type: system-doc
title: "NegotiationPriceTierPVO — PVO Purchasing"
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
  - NegotiationPriceTierPVO
  - negotiationpricetierpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationPriceTierPVO

## 📌 Visão Geral

Disponibiliza faixas de preço de negociações para consulta operacional, com detalhes de volume e preço por faixa. Suporta análise comparativa de propostas por quantidade.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.NegotiationPriceTierPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 444 | 5 | 3 | 444 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[egp_categories_vl|EGP_CATEGORIES_VL]] — 7 atributos (7 BICC)
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 12 atributos (12 BICC)
- [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]] — 217 atributos (217 BICC)
- [[pon_auction_item_prices_all|PON_AUCTION_ITEM_PRICES_ALL]] — 188 atributos (188 BICC)
- [[pon_auction_shipments_all|PON_AUCTION_SHIPMENTS_ALL]] — 20 atributos (3 PKs, 20 BICC)

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

### [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationHeaderAbstractDetails | ABSTRACT_DETAILS | — | ✅ |
| 2 | NegotiationHeaderAbstractStatus | ABSTRACT_STATUS | — | ✅ |
| 3 | NegotiationHeaderAdvanceNegotiableFlag | ADVANCE_NEGOTIABLE_FLAG | — | ✅ |
| 4 | NegotiationHeaderAllowOtherBidCurrencyFlag | ALLOW_OTHER_BID_CURRENCY_FLAG | — | ✅ |
| 5 | NegotiationHeaderAmendmentDescription | AMENDMENT_DESCRIPTION | — | ✅ |
| 6 | NegotiationHeaderAmendmentNumber | AMENDMENT_NUMBER | — | ✅ |
| 7 | NegotiationHeaderApprovalAmount | APPROVAL_AMOUNT | — | ✅ |
| 8 | NegotiationHeaderApprovalStatus | NEG_APPROVAL_STATUS | — | ✅ |
| 9 | NegotiationHeaderAttributeLineNumber | ATTRIBUTE_LINE_NUMBER | — | ✅ |
| 10 | NegotiationHeaderAttributesExist | ATTRIBUTES_EXIST | — | ✅ |
| 11 | NegotiationHeaderAuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 12 | NegotiationHeaderAuctionHeaderIdOrigAmend | AUCTION_HEADER_ID_ORIG_AMEND | — | ✅ |
| 13 | NegotiationHeaderAuctionHeaderIdOrigRound | AUCTION_HEADER_ID_ORIG_ROUND | — | ✅ |
| 14 | NegotiationHeaderAuctionHeaderIdPrevAmend | AUCTION_HEADER_ID_PREV_AMEND | — | ✅ |
| 15 | NegotiationHeaderAuctionHeaderIdPrevRound | AUCTION_HEADER_ID_PREV_ROUND | — | ✅ |
| 16 | NegotiationHeaderAuctionOriginationCode | AUCTION_ORIGINATION_CODE | — | ✅ |
| 17 | NegotiationHeaderAuctionRoundNumber | AUCTION_ROUND_NUMBER | — | ✅ |
| 18 | NegotiationHeaderAuctionStatus | AUCTION_STATUS | — | ✅ |
| 19 | NegotiationHeaderAuctionTitle | AUCTION_TITLE | — | ✅ |
| 20 | NegotiationHeaderAutoExtendAllLinesFlag | AUTO_EXTEND_ALL_LINES_FLAG | — | ✅ |
| 21 | NegotiationHeaderAutoExtendDuration | AUTO_EXTEND_DURATION | — | ✅ |
| 22 | NegotiationHeaderAutoExtendEnabledFlag | AUTO_EXTEND_ENABLED_FLAG | — | ✅ |
| 23 | NegotiationHeaderAutoExtendFlag | AUTO_EXTEND_FLAG | — | ✅ |
| 24 | NegotiationHeaderAutoExtendMinTriggerRank | AUTO_EXTEND_MIN_TRIGGER_RANK | — | ✅ |
| 25 | NegotiationHeaderAutoExtendNumber | AUTO_EXTEND_NUMBER | — | ✅ |
| 26 | NegotiationHeaderAutoExtendTypeFlag | AUTO_EXTEND_TYPE_FLAG | — | ✅ |
| 27 | NegotiationHeaderAutoextendChangedFlag | AUTOEXTEND_CHANGED_FLAG | — | ✅ |
| 28 | NegotiationHeaderAwardApprAmeTransId | AWARD_APPR_AME_TRANS_ID | — | ✅ |
| 29 | NegotiationHeaderAwardApprAmeTransPrevId | AWARD_APPR_AME_TRANS_PREV_ID | — | ✅ |
| 30 | NegotiationHeaderAwardApprAmeTxnDate | AWARD_APPR_AME_TXN_DATE | — | ✅ |
| 31 | NegotiationHeaderAwardApprovalFlag | AWARD_APPROVAL_FLAG | — | ✅ |
| 32 | NegotiationHeaderAwardApprovalStatus | AWARD_APPROVAL_STATUS | — | ✅ |
| 33 | NegotiationHeaderAwardByDate | AWARD_BY_DATE | — | ✅ |
| 34 | NegotiationHeaderAwardCompleteDate | AWARD_COMPLETE_DATE | — | ✅ |
| 35 | NegotiationHeaderAwardDate | AWARD_DATE | — | ✅ |
| 36 | NegotiationHeaderAwardMode | AWARD_MODE | — | ✅ |
| 37 | NegotiationHeaderAwardStatus | AWARD_STATUS | — | ✅ |
| 38 | NegotiationHeaderBidDecrementMethod | BID_DECREMENT_METHOD | — | ✅ |
| 39 | NegotiationHeaderBidFrequencyCode | BID_FREQUENCY_CODE | — | ✅ |
| 40 | NegotiationHeaderBidListType | BID_LIST_TYPE | — | ✅ |
| 41 | NegotiationHeaderBidRanking | BID_RANKING | — | ✅ |
| 42 | NegotiationHeaderBidScopeCode | BID_SCOPE_CODE | — | ✅ |
| 43 | NegotiationHeaderBidVisibilityCode | BID_VISIBILITY_CODE | — | ✅ |
| 44 | NegotiationHeaderCancelDate | CANCEL_DATE | — | ✅ |
| 45 | NegotiationHeaderCarrierId | CARRIER_ID | — | ✅ |
| 46 | NegotiationHeaderCloseBiddingDate | CLOSE_BIDDING_DATE | — | ✅ |
| 47 | NegotiationHeaderCloseDateType | CLOSE_DATE_TYPE | — | ✅ |
| 48 | NegotiationHeaderCompleteFlag | COMPLETE_FLAG | — | ✅ |
| 49 | NegotiationHeaderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | ✅ |
| 50 | NegotiationHeaderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | ✅ |
| 51 | NegotiationHeaderContermsExistFlag | CONTERMS_EXIST_FLAG | — | ✅ |
| 52 | NegotiationHeaderContractTemplateId | CONTRACT_TEMPLATE_ID | — | ✅ |
| 53 | NegotiationHeaderContractType | CONTRACT_TYPE | — | ✅ |
| 54 | NegotiationHeaderCreatedBy | CREATED_BY | — | ✅ |
| 55 | NegotiationHeaderCreationDate | CREATION_DATE | — | ✅ |
| 56 | NegotiationHeaderCreationDateOrigAmend | CREATION_DATE_ORIG_AMEND | — | ✅ |
| 57 | NegotiationHeaderCurrencyCode | CURRENCY_CODE | — | ✅ |
| 58 | NegotiationHeaderDaysAfterOpenDate | DAYS_AFTER_OPEN_DATE | — | ✅ |
| 59 | NegotiationHeaderDescription | DESCRIPTION | — | ✅ |
| 60 | NegotiationHeaderDisplayBestPriceBlindFlag | DISPLAY_BEST_PRICE_BLIND_FLAG | — | ✅ |
| 61 | NegotiationHeaderDoctypeId | DOCTYPE_ID | — | ✅ |
| 62 | NegotiationHeaderDocumentNumber | DOCUMENT_NUMBER | — | ✅ |
| 63 | NegotiationHeaderDraftLocked | DRAFT_LOCKED | — | ✅ |
| 64 | NegotiationHeaderDraftLockedDate | DRAFT_LOCKED_DATE | — | ✅ |
| 65 | NegotiationHeaderDraftUnlockedDate | DRAFT_UNLOCKED_DATE | — | ✅ |
| 66 | NegotiationHeaderEnforcePrevrndBidPriceFlag | ENFORCE_PREVRND_BID_PRICE_FLAG | — | ✅ |
| 67 | NegotiationHeaderEventId | EVENT_ID | — | ✅ |
| 68 | NegotiationHeaderEventTitle | EVENT_TITLE | — | ✅ |
| 69 | NegotiationHeaderExtAttribute1 | EXT_ATTRIBUTE1 | — | ✅ |
| 70 | NegotiationHeaderExtAttribute10 | EXT_ATTRIBUTE10 | — | ✅ |
| 71 | NegotiationHeaderExtAttribute11 | EXT_ATTRIBUTE11 | — | ✅ |
| 72 | NegotiationHeaderExtAttribute12 | EXT_ATTRIBUTE12 | — | ✅ |
| 73 | NegotiationHeaderExtAttribute13 | EXT_ATTRIBUTE13 | — | ✅ |
| 74 | NegotiationHeaderExtAttribute14 | EXT_ATTRIBUTE14 | — | ✅ |
| 75 | NegotiationHeaderExtAttribute15 | EXT_ATTRIBUTE15 | — | ✅ |
| 76 | NegotiationHeaderExtAttribute2 | EXT_ATTRIBUTE2 | — | ✅ |
| 77 | NegotiationHeaderExtAttribute3 | EXT_ATTRIBUTE3 | — | ✅ |
| 78 | NegotiationHeaderExtAttribute4 | EXT_ATTRIBUTE4 | — | ✅ |
| 79 | NegotiationHeaderExtAttribute5 | EXT_ATTRIBUTE5 | — | ✅ |
| 80 | NegotiationHeaderExtAttribute6 | EXT_ATTRIBUTE6 | — | ✅ |
| 81 | NegotiationHeaderExtAttribute7 | EXT_ATTRIBUTE7 | — | ✅ |
| 82 | NegotiationHeaderExtAttribute8 | EXT_ATTRIBUTE8 | — | ✅ |
| 83 | NegotiationHeaderExtAttribute9 | EXT_ATTRIBUTE9 | — | ✅ |
| 84 | NegotiationHeaderExtAttributeCategory | EXT_ATTRIBUTE_CATEGORY | — | ✅ |
| 85 | NegotiationHeaderFirstLineCloseDate | FIRST_LINE_CLOSE_DATE | — | ✅ |
| 86 | NegotiationHeaderFobCode | FOB_CODE | — | ✅ |
| 87 | NegotiationHeaderFreightTermsCode | FREIGHT_TERMS_CODE | — | ✅ |
| 88 | NegotiationHeaderFullQuantityBidCode | FULL_QUANTITY_BID_CODE | — | ✅ |
| 89 | NegotiationHeaderGlobalTemplateFlag | GLOBAL_TEMPLATE_FLAG | — | ✅ |
| 90 | NegotiationHeaderGroupEnabledFlag | GROUP_ENABLED_FLAG | — | ✅ |
| 91 | NegotiationHeaderHasHdrAttrFlag | HAS_HDR_ATTR_FLAG | — | ✅ |
| 92 | NegotiationHeaderHasItemsFlag | HAS_ITEMS_FLAG | — | ✅ |
| 93 | NegotiationHeaderHasPeForAllItems | HAS_PE_FOR_ALL_ITEMS | — | ✅ |
| 94 | NegotiationHeaderHasPriceElements | HAS_PRICE_ELEMENTS | — | ✅ |
| 95 | NegotiationHeaderHasScoringTeamsFlag | HAS_SCORING_TEAMS_FLAG | — | ✅ |
| 96 | NegotiationHeaderHdrAttrDisplayScore | HDR_ATTR_DISPLAY_SCORE | — | ✅ |
| 97 | NegotiationHeaderHdrAttrEnableWeights | HDR_ATTR_ENABLE_WEIGHTS | — | ✅ |
| 98 | NegotiationHeaderHdrAttrMaximumScore | HDR_ATTR_MAXIMUM_SCORE | — | ✅ |
| 99 | NegotiationHeaderHdrAttributeEnabledFlag | HDR_ATTRIBUTE_ENABLED_FLAG | — | ✅ |
| 100 | NegotiationHeaderImportFileName | IMPORT_FILE_NAME | — | ✅ |
| 101 | NegotiationHeaderIncludePdfInExternalPage | INCLUDE_PDF_IN_EXTERNAL_PAGE | — | ✅ |
| 102 | NegotiationHeaderIntAttribute1 | INT_ATTRIBUTE1 | — | ✅ |
| 103 | NegotiationHeaderIntAttribute10 | INT_ATTRIBUTE10 | — | ✅ |
| 104 | NegotiationHeaderIntAttribute11 | INT_ATTRIBUTE11 | — | ✅ |
| 105 | NegotiationHeaderIntAttribute12 | INT_ATTRIBUTE12 | — | ✅ |
| 106 | NegotiationHeaderIntAttribute13 | INT_ATTRIBUTE13 | — | ✅ |
| 107 | NegotiationHeaderIntAttribute14 | INT_ATTRIBUTE14 | — | ✅ |
| 108 | NegotiationHeaderIntAttribute15 | INT_ATTRIBUTE15 | — | ✅ |
| 109 | NegotiationHeaderIntAttribute2 | INT_ATTRIBUTE2 | — | ✅ |
| 110 | NegotiationHeaderIntAttribute3 | INT_ATTRIBUTE3 | — | ✅ |
| 111 | NegotiationHeaderIntAttribute4 | INT_ATTRIBUTE4 | — | ✅ |
| 112 | NegotiationHeaderIntAttribute5 | INT_ATTRIBUTE5 | — | ✅ |
| 113 | NegotiationHeaderIntAttribute6 | INT_ATTRIBUTE6 | — | ✅ |
| 114 | NegotiationHeaderIntAttribute7 | INT_ATTRIBUTE7 | — | ✅ |
| 115 | NegotiationHeaderIntAttribute8 | INT_ATTRIBUTE8 | — | ✅ |
| 116 | NegotiationHeaderIntAttribute9 | INT_ATTRIBUTE9 | — | ✅ |
| 117 | NegotiationHeaderIntAttributeCategory | INT_ATTRIBUTE_CATEGORY | — | ✅ |
| 118 | NegotiationHeaderIsPaused | IS_PAUSED | — | ✅ |
| 119 | NegotiationHeaderIsTemplateFlag | IS_TEMPLATE_FLAG | — | ✅ |
| 120 | NegotiationHeaderLanguageCode | LANGUAGE_CODE | — | ✅ |
| 121 | NegotiationHeaderLargeNegEnabledFlag | LARGE_NEG_ENABLED_FLAG | — | ✅ |
| 122 | NegotiationHeaderLastLineNumber | LAST_LINE_NUMBER | — | ✅ |
| 123 | NegotiationHeaderLastPauseDate | LAST_PAUSE_DATE | — | ✅ |
| 124 | NegotiationHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 125 | NegotiationHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 126 | NegotiationHeaderLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 127 | NegotiationHeaderLineAttributeEnabledFlag | LINE_ATTRIBUTE_ENABLED_FLAG | — | ✅ |
| 128 | NegotiationHeaderLineMasEnabledFlag | LINE_MAS_ENABLED_FLAG | — | ✅ |
| 129 | NegotiationHeaderLotEnabledFlag | LOT_ENABLED_FLAG | — | ✅ |
| 130 | NegotiationHeaderMaxBidColorSequenceId | MAX_BID_COLOR_SEQUENCE_ID | — | ✅ |
| 131 | NegotiationHeaderMaxDocumentLineNum | MAX_DOCUMENT_LINE_NUM | — | ✅ |
| 132 | NegotiationHeaderMaxInternalLineNum | MAX_INTERNAL_LINE_NUM | — | ✅ |
| 133 | NegotiationHeaderMaxRetainageNegotiableFlag | MAX_RETAINAGE_NEGOTIABLE_FLAG | — | ✅ |
| 134 | NegotiationHeaderMinBidChangeType | MIN_BID_CHANGE_TYPE | — | ✅ |
| 135 | NegotiationHeaderMinBidDecrement | MIN_BID_DECREMENT | — | ✅ |
| 136 | NegotiationHeaderNegApprovalDate | NEG_APPROVAL_DATE | — | ✅ |
| 137 | NegotiationHeaderNegApprovalEnabledFlag | NEG_APPROVAL_ENABLED_FLAG | — | ✅ |
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
| 150 | NegotiationHeaderPersonId | PERSON_ID | — | ✅ |
| 151 | NegotiationHeaderPfTypeAllowed | PF_TYPE_ALLOWED | — | ✅ |
| 152 | NegotiationHeaderPoAgreedAmount | PO_AGREED_AMOUNT | — | ✅ |
| 153 | NegotiationHeaderPoEndDate | PO_END_DATE | — | ✅ |
| 154 | NegotiationHeaderPoMinRelAmount | PO_MIN_REL_AMOUNT | — | ✅ |
| 155 | NegotiationHeaderPoStartDate | PO_START_DATE | — | ✅ |
| 156 | NegotiationHeaderPoStyleId | PO_STYLE_ID | — | ✅ |
| 157 | NegotiationHeaderPowerBiddingEnabledFlag | POWER_BIDDING_ENABLED_FLAG | — | ✅ |
| 158 | NegotiationHeaderPrcBuId | PRC_BU_ID | — | ✅ |
| 159 | NegotiationHeaderPriceDrivenAuctionFlag | PRICE_DRIVEN_AUCTION_FLAG | — | ✅ |
| 160 | NegotiationHeaderPriceElementEnabledFlag | PRICE_ELEMENT_ENABLED_FLAG | — | ✅ |
| 161 | NegotiationHeaderPriceTiersIndicator | PRICE_TIERS_INDICATOR | — | ✅ |
| 162 | NegotiationHeaderProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 163 | NegotiationHeaderProgramName | PROGRAM_NAME | — | ✅ |
| 164 | NegotiationHeaderProgressPaymentType | PROGRESS_PAYMENT_TYPE | — | ✅ |
| 165 | NegotiationHeaderProgressPymtNegotiableFlag | PROGRESS_PYMT_NEGOTIABLE_FLAG | — | ✅ |
| 166 | NegotiationHeaderProjectId | PROJECT_ID | — | ✅ |
| 167 | NegotiationHeaderProxyBiddingEnabledFlag | PROXY_BIDDING_ENABLED_FLAG | — | ✅ |
| 168 | NegotiationHeaderPublishAuctionNowFlag | PUBLISH_AUCTION_NOW_FLAG | — | ✅ |
| 169 | NegotiationHeaderPublishDate | PUBLISH_DATE | — | ✅ |
| 170 | NegotiationHeaderPublishDateOrigAmend | PUBLISH_DATE_ORIG_AMEND | — | ✅ |
| 171 | NegotiationHeaderPublishRatesToBiddersFlag | PUBLISH_RATES_TO_BIDDERS_FLAG | — | ✅ |
| 172 | NegotiationHeaderQtyPriceTiersEnabledFlag | QTY_PRICE_TIERS_ENABLED_FLAG | — | ✅ |
| 173 | NegotiationHeaderRankIndicator | RANK_INDICATOR | — | ✅ |
| 174 | NegotiationHeaderRateDate | RATE_DATE | — | ✅ |
| 175 | NegotiationHeaderRateType | RATE_TYPE | — | ✅ |
| 176 | NegotiationHeaderRecoupmentNegotiableFlag | RECOUPMENT_NEGOTIABLE_FLAG | — | ✅ |
| 177 | NegotiationHeaderReminderDate | REMINDER_DATE | — | ✅ |
| 178 | NegotiationHeaderReqBuId | REQ_BU_ID | — | ✅ |
| 179 | NegotiationHeaderRequestDate | REQUEST_DATE | — | ✅ |
| 180 | NegotiationHeaderRequestId | REQUEST_ID | — | ✅ |
| 181 | NegotiationHeaderRequestedBy | REQUESTED_BY | — | ✅ |
| 182 | NegotiationHeaderRetainageNegotiableFlag | RETAINAGE_NEGOTIABLE_FLAG | — | ✅ |
| 183 | NegotiationHeaderRfiLineEnabledFlag | RFI_LINE_ENABLED_FLAG | — | ✅ |
| 184 | NegotiationHeaderScoringLockDate | SCORING_LOCK_DATE | — | ✅ |
| 185 | NegotiationHeaderSealedActualUnlockDate | SEALED_ACTUAL_UNLOCK_DATE | — | ✅ |
| 186 | NegotiationHeaderSealedActualUnsealDate | SEALED_ACTUAL_UNSEAL_DATE | — | ✅ |
| 187 | NegotiationHeaderSealedAuctionStatus | SEALED_AUCTION_STATUS | — | ✅ |
| 188 | NegotiationHeaderShareAwardDecision | SHARE_AWARD_DECISION | — | ✅ |
| 189 | NegotiationHeaderShowBidderNotes | SHOW_BIDDER_NOTES | — | ✅ |
| 190 | NegotiationHeaderShowBidderScores | SHOW_BIDDER_SCORES | — | ✅ |
| 191 | NegotiationHeaderSourceDocId | SOURCE_DOC_ID | — | ✅ |
| 192 | NegotiationHeaderSourceDocLineMsg | SOURCE_DOC_LINE_MSG | — | ✅ |
| 193 | NegotiationHeaderSourceDocMsg | SOURCE_DOC_MSG | — | ✅ |
| 194 | NegotiationHeaderSourceDocMsgApp | SOURCE_DOC_MSG_APP | — | ✅ |
| 195 | NegotiationHeaderSourceDocNumber | SOURCE_DOC_NUMBER | — | ✅ |
| 196 | NegotiationHeaderSourceReqsFlag | SOURCE_REQS_FLAG | — | ✅ |
| 197 | NegotiationHeaderStaggeredClosingInterval | STAGGERED_CLOSING_INTERVAL | — | ✅ |
| 198 | NegotiationHeaderStyleId | STYLE_ID | — | ✅ |
| 199 | NegotiationHeaderSupplierEnterablePymtFlag | SUPPLIER_ENTERABLE_PYMT_FLAG | — | ✅ |
| 200 | NegotiationHeaderSupplierViewType | SUPPLIER_VIEW_TYPE | — | ✅ |
| 201 | NegotiationHeaderTeamScoringEnabledFlag | TEAM_SCORING_ENABLED_FLAG | — | ✅ |
| 202 | NegotiationHeaderTechnicalActualUnlockDate | TECHNICAL_ACTUAL_UNLOCK_DATE | — | ✅ |
| 203 | NegotiationHeaderTechnicalActualUnsealDate | TECHNICAL_ACTUAL_UNSEAL_DATE | — | ✅ |
| 204 | NegotiationHeaderTechnicalEvaluationStatus | TECHNICAL_EVALUATION_STATUS | — | ✅ |
| 205 | NegotiationHeaderTechnicalLockStatus | TECHNICAL_LOCK_STATUS | — | ✅ |
| 206 | NegotiationHeaderTemplateId | TEMPLATE_ID | — | ✅ |
| 207 | NegotiationHeaderTemplateScope | TEMPLATE_SCOPE | — | ✅ |
| 208 | NegotiationHeaderTemplateStatus | TEMPLATE_STATUS | — | ✅ |
| 209 | NegotiationHeaderTwoPartFlag | TWO_PART_FLAG | — | ✅ |
| 210 | NegotiationHeaderVersionNum | VERSION_NUM | — | ✅ |
| 211 | NegotiationHeaderViewByDate | VIEW_BY_DATE | — | ✅ |
| 212 | NegotiationHeaderWfApprovalItemKey | WF_APPROVAL_ITEM_KEY | — | ✅ |
| 213 | NegotiationHeaderWfAwardApprovalItemKey | WF_AWARD_APPROVAL_ITEM_KEY | — | ✅ |
| 214 | NegotiationHeaderWfItemKey | WF_ITEM_KEY | — | ✅ |
| 215 | NegotiationHeaderWfPoncomplCurrentRound | WF_PONCOMPL_CURRENT_ROUND | — | ✅ |
| 216 | NegotiationHeaderWfPoncomplItemKey | WF_PONCOMPL_ITEM_KEY | — | ✅ |
| 217 | NegotiationHeaderWfRoleName | WF_ROLE_NAME | — | ✅ |

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
| 95 | NegotiationParentLineAdditionalJobDetails | ADDITIONAL_JOB_DETAILS | — | ✅ |
| 96 | NegotiationParentLineAdvanceAmount | ADVANCE_AMOUNT | — | ✅ |
| 97 | NegotiationParentLineAllocationStatus | ALLOCATION_STATUS | — | ✅ |
| 98 | NegotiationParentLineAuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 99 | NegotiationParentLineAwardMode | AWARD_MODE | — | ✅ |
| 100 | NegotiationParentLineAwardStatus | AWARD_STATUS | — | ✅ |
| 101 | NegotiationParentLineAwardedQuantity | AWARDED_QUANTITY | — | ✅ |
| 102 | NegotiationParentLineBestBidBidCurrencyCode | BEST_BID_BID_CURRENCY_CODE | — | ✅ |
| 103 | NegotiationParentLineBestBidBidCurrencyPrice | BEST_BID_BID_CURRENCY_PRICE | — | ✅ |
| 104 | NegotiationParentLineBestBidBidNumber | BEST_BID_BID_NUMBER | — | ✅ |
| 105 | NegotiationParentLineBestBidBidPrice | BEST_BID_BID_PRICE | — | ✅ |
| 106 | NegotiationParentLineBestBidCurrencyCode | BEST_BID_CURRENCY_CODE | — | ✅ |
| 107 | NegotiationParentLineBestBidCurrencyPrice | BEST_BID_CURRENCY_PRICE | — | ✅ |
| 108 | NegotiationParentLineBestBidFirstBidPrice | BEST_BID_FIRST_BID_PRICE | — | ✅ |
| 109 | NegotiationParentLineBestBidNumber | BEST_BID_NUMBER | — | ✅ |
| 110 | NegotiationParentLineBestBidPrice | BEST_BID_PRICE | — | ✅ |
| 111 | NegotiationParentLineBestBidPromisedDate | BEST_BID_PROMISED_DATE | — | ✅ |
| 112 | NegotiationParentLineBestBidProxyLimitPrice | BEST_BID_PROXY_LIMIT_PRICE | — | ✅ |
| 113 | NegotiationParentLineBestBidQuantity | BEST_BID_QUANTITY | — | ✅ |
| 114 | NegotiationParentLineBestBidScore | BEST_BID_SCORE | — | ✅ |
| 115 | NegotiationParentLineBidStartPrice | BID_START_PRICE | — | ✅ |
| 116 | NegotiationParentLineCategoryId | CATEGORY_ID | — | ✅ |
| 117 | NegotiationParentLineCloseBiddingDate | CLOSE_BIDDING_DATE | — | ✅ |
| 118 | NegotiationParentLineCreatedBy | CREATED_BY | — | ✅ |
| 119 | NegotiationParentLineCreationDate | CREATION_DATE | — | ✅ |
| 120 | NegotiationParentLineCurrentPrice | CURRENT_PRICE | — | ✅ |
| 121 | NegotiationParentLineDifferentialResponseType | DIFFERENTIAL_RESPONSE_TYPE | — | ✅ |
| 122 | NegotiationParentLineDispLineNumber | DISP_LINE_NUMBER | — | ✅ |
| 123 | NegotiationParentLineDisplayTargetPriceFlag | DISPLAY_TARGET_PRICE_FLAG | — | ✅ |
| 124 | NegotiationParentLineDocumentDispLineNumber | DOCUMENT_DISP_LINE_NUMBER | — | ✅ |
| 125 | NegotiationParentLineGroupType | GROUP_TYPE | — | ✅ |
| 126 | NegotiationParentLineHasAttributesFlag | HAS_ATTRIBUTES_FLAG | — | ✅ |
| 127 | NegotiationParentLineHasBuyerPfsFlag | HAS_BUYER_PFS_FLAG | — | ✅ |
| 128 | NegotiationParentLineHasPaymentsFlag | HAS_PAYMENTS_FLAG | — | ✅ |
| 129 | NegotiationParentLineHasPriceDifferentialsFlag | HAS_PRICE_DIFFERENTIALS_FLAG | — | ✅ |
| 130 | NegotiationParentLineHasPriceElementsFlag | HAS_PRICE_ELEMENTS_FLAG | — | ✅ |
| 131 | NegotiationParentLineHasQuantityTiers | HAS_QUANTITY_TIERS | — | ✅ |
| 132 | NegotiationParentLineHasShipmentsFlag | HAS_SHIPMENTS_FLAG | — | ✅ |
| 133 | NegotiationParentLineInvOrgId | INV_ORG_ID | — | ✅ |
| 134 | NegotiationParentLineItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 135 | NegotiationParentLineItemId | ITEM_ID | — | ✅ |
| 136 | NegotiationParentLineItemRevision | ITEM_REVISION | — | ✅ |
| 137 | NegotiationParentLineJobId | JOB_ID | — | ✅ |
| 138 | NegotiationParentLineLastAmendmentUpdate | LAST_AMENDMENT_UPDATE | — | ✅ |
| 139 | NegotiationParentLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 140 | NegotiationParentLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 141 | NegotiationParentLineLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 142 | NegotiationParentLineLineNumber | LINE_NUMBER | — | ✅ |
| 143 | NegotiationParentLineLineOriginationCode | LINE_ORIGINATION_CODE | — | ✅ |
| 144 | NegotiationParentLineLineTypeId | LINE_TYPE_ID | — | ✅ |
| 145 | NegotiationParentLineMaxRetainageAmount | MAX_RETAINAGE_AMOUNT | — | ✅ |
| 146 | NegotiationParentLineMaxSubLineSequenceNumber | MAX_SUB_LINE_SEQUENCE_NUMBER | — | ✅ |
| 147 | NegotiationParentLineModifiedDate | MODIFIED_DATE | — | ✅ |
| 148 | NegotiationParentLineModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 149 | NegotiationParentLineNeedByDate | NEED_BY_DATE | — | ✅ |
| 150 | NegotiationParentLineNoAward | NO_AWARD | — | ✅ |
| 151 | NegotiationParentLineNoteToBidders | NOTE_TO_BIDDERS | — | ✅ |
| 152 | NegotiationParentLineNumberOfBids | NUMBER_OF_BIDS | — | ✅ |
| 153 | NegotiationParentLineNumberOfExtensions | NUMBER_OF_EXTENSIONS | — | ✅ |
| 154 | NegotiationParentLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 155 | NegotiationParentLineOrderTypeLookupCode | ORDER_TYPE_LOOKUP_CODE | — | ✅ |
| 156 | NegotiationParentLineParentLineNumber | PARENT_LINE_NUMBER | — | ✅ |
| 157 | NegotiationParentLinePoAgreedAmount | PO_AGREED_AMOUNT | — | ✅ |
| 158 | NegotiationParentLinePoMinRelAmount | PO_MIN_REL_AMOUNT | — | ✅ |
| 159 | NegotiationParentLinePrcBuId | PRC_BU_ID | — | ✅ |
| 160 | NegotiationParentLinePriceBreakNegFlag | PRICE_BREAK_NEG_FLAG | — | ✅ |
| 161 | NegotiationParentLinePriceBreakType | PRICE_BREAK_TYPE | — | ✅ |
| 162 | NegotiationParentLinePriceDiffShipmentNumber | PRICE_DIFF_SHIPMENT_NUMBER | — | ✅ |
| 163 | NegotiationParentLinePriceDisabledFlag | PRICE_DISABLED_FLAG | — | ✅ |
| 164 | NegotiationParentLineProgressPymtRatePercent | PROGRESS_PYMT_RATE_PERCENT | — | ✅ |
| 165 | NegotiationParentLineProjectAwardId | PROJECT_AWARD_ID | — | ✅ |
| 166 | NegotiationParentLineProjectExpOrganizationId | PROJECT_EXP_ORGANIZATION_ID | — | ✅ |
| 167 | NegotiationParentLineProjectExpenditureItemDate | PROJECT_EXPENDITURE_ITEM_DATE | — | ✅ |
| 168 | NegotiationParentLineProjectExpenditureType | PROJECT_EXPENDITURE_TYPE | — | ✅ |
| 169 | NegotiationParentLineProjectId | PROJECT_ID | — | ✅ |
| 170 | NegotiationParentLineProjectTaskId | PROJECT_TASK_ID | — | ✅ |
| 171 | NegotiationParentLinePurchaseBasis | PURCHASE_BASIS | — | ✅ |
| 172 | NegotiationParentLineQuantity | QUANTITY | — | ✅ |
| 173 | NegotiationParentLineQuantityDisabledFlag | QUANTITY_DISABLED_FLAG | — | ✅ |
| 174 | NegotiationParentLineRecoupmentRatePercent | RECOUPMENT_RATE_PERCENT | — | ✅ |
| 175 | NegotiationParentLineReqBuId | REQ_BU_ID | — | ✅ |
| 176 | NegotiationParentLineRequisitionNumber | REQUISITION_NUMBER | — | ✅ |
| 177 | NegotiationParentLineRetainageRatePercent | RETAINAGE_RATE_PERCENT | — | ✅ |
| 178 | NegotiationParentLineShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 179 | NegotiationParentLineSourceDocId | SOURCE_DOC_ID | — | ✅ |
| 180 | NegotiationParentLineSourceDocNumber | SOURCE_DOC_NUMBER | — | ✅ |
| 181 | NegotiationParentLineSourceLineId | SOURCE_LINE_ID | — | ✅ |
| 182 | NegotiationParentLineSourceLineNumber | SOURCE_LINE_NUMBER | — | ✅ |
| 183 | NegotiationParentLineSubLineSequenceNumber | SUB_LINE_SEQUENCE_NUMBER | — | ✅ |
| 184 | NegotiationParentLineTargetPrice | TARGET_PRICE | — | ✅ |
| 185 | NegotiationParentLineUnitDisplayTargetFlag | UNIT_DISPLAY_TARGET_FLAG | — | ✅ |
| 186 | NegotiationParentLineUnitTargetPrice | UNIT_TARGET_PRICE | — | ✅ |
| 187 | NegotiationParentLineUomCode | UOM_CODE | — | ✅ |
| 188 | NegotiationParentLineWorkApproverUserId | WORK_APPROVER_USER_ID | — | ✅ |

### [[pon_auction_shipments_all|PON_AUCTION_SHIPMENTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AuctionHeaderId | AUCTION_HEADER_ID | 🔑 | ✅ |
| 2 | LineNumber | LINE_NUMBER | 🔑 | ✅ |
| 3 | NegotiationShipmentCreatedBy | CREATED_BY | — | ✅ |
| 4 | NegotiationShipmentCreationDate | CREATION_DATE | — | ✅ |
| 5 | NegotiationShipmentDifferentialResponseType | DIFFERENTIAL_RESPONSE_TYPE | — | ✅ |
| 6 | NegotiationShipmentEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 7 | NegotiationShipmentEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 8 | NegotiationShipmentHasPriceDifferentialsFlag | HAS_PRICE_DIFFERENTIALS_FLAG | — | ✅ |
| 9 | NegotiationShipmentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | NegotiationShipmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | NegotiationShipmentLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | NegotiationShipmentMaxQuantity | MAX_QUANTITY | — | ✅ |
| 13 | NegotiationShipmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | NegotiationShipmentPrcBuId | PRC_BU_ID | — | ✅ |
| 15 | NegotiationShipmentPrice | PRICE | — | ✅ |
| 16 | NegotiationShipmentQuantity | QUANTITY | — | ✅ |
| 17 | NegotiationShipmentShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 18 | NegotiationShipmentShipToOrganizationId | SHIP_TO_ORGANIZATION_ID | — | ✅ |
| 19 | NegotiationShipmentShipmentType | SHIPMENT_TYPE | — | ✅ |
| 20 | ShipmentNumber | SHIPMENT_NUMBER | 🔑 | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
