---
id: DOC-PO-PVO-NegotiationCollaborationTeamPVO
doc_type: system-doc
title: "NegotiationCollaborationTeamPVO — PVO Purchasing"
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
  - NegotiationCollaborationTeamPVO
  - negotiationcollaborationteampvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationCollaborationTeamPVO

## 📌 Visão Geral

Disponibiliza equipes de colaboração de negociações para consulta, identificando membros, funções e nível de acesso em cada processo de sourcing.

**Caminho:** `FscmTopModelAM.PrcPonPublicViewAM.NegotiationCollaborationTeamPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 254 | 3 | 2 | 35 | 14% |

---

## 🔗 Tabelas Relacionadas

- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 13 atributos
- [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]] — 222 atributos (27 BICC)
- [[pon_neg_team_members|PON_NEG_TEAM_MEMBERS]] — 19 atributos (2 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DailyConversionTypeNegoHdrConversionType | CONVERSION_TYPE | — | — |
| 2 | DailyConversionTypeNegoHdrDescription | DESCRIPTION | — | — |
| 3 | DailyConversionTypeNegoHdrEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 4 | DailyConversionTypeNegoHdrEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 5 | DailyConversionTypeNegoHdrFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 6 | DailyConversionTypeNegoHdrFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 7 | DailyConversionTypeNegoHdrFemScenario | FEM_SCENARIO | — | — |
| 8 | DailyConversionTypeNegoHdrFemTimeframe | FEM_TIMEFRAME | — | — |
| 9 | DailyConversionTypeNegoHdrObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | DailyConversionTypeNegoHdrPivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 11 | DailyConversionTypeNegoHdrSecurityFlag | SECURITY_FLAG | — | — |
| 12 | DailyConversionTypeNegoHdrUserConversionType | USER_CONVERSION_TYPE | — | — |
| 13 | DailyConversionTypeNegoHdrUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |

### [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationHeaderAbstractDetails | ABSTRACT_DETAILS | — | — |
| 2 | NegotiationHeaderAbstractStatus | ABSTRACT_STATUS | — | — |
| 3 | NegotiationHeaderAdvanceNegotiableFlag | ADVANCE_NEGOTIABLE_FLAG | — | — |
| 4 | NegotiationHeaderAllowOtherBidCurrencyFlag | ALLOW_OTHER_BID_CURRENCY_FLAG | — | — |
| 5 | NegotiationHeaderAmendmentDescription | AMENDMENT_DESCRIPTION | — | — |
| 6 | NegotiationHeaderAmendmentNumber | AMENDMENT_NUMBER | — | — |
| 7 | NegotiationHeaderApprovalAmount | APPROVAL_AMOUNT | — | — |
| 8 | NegotiationHeaderApprovalStatus | NEG_APPROVAL_STATUS | — | — |
| 9 | NegotiationHeaderAttributeLineNumber | ATTRIBUTE_LINE_NUMBER | — | — |
| 10 | NegotiationHeaderAttributesExist | ATTRIBUTES_EXIST | — | — |
| 11 | NegotiationHeaderAuctionHeaderId | AUCTION_HEADER_ID | — | — |
| 12 | NegotiationHeaderAuctionHeaderIdOrigAmend | AUCTION_HEADER_ID_ORIG_AMEND | — | — |
| 13 | NegotiationHeaderAuctionHeaderIdOrigRound | AUCTION_HEADER_ID_ORIG_ROUND | — | — |
| 14 | NegotiationHeaderAuctionHeaderIdPrevAmend | AUCTION_HEADER_ID_PREV_AMEND | — | — |
| 15 | NegotiationHeaderAuctionHeaderIdPrevRound | AUCTION_HEADER_ID_PREV_ROUND | — | — |
| 16 | NegotiationHeaderAuctionOriginationCode | AUCTION_ORIGINATION_CODE | — | — |
| 17 | NegotiationHeaderAuctionRoundNumber | AUCTION_ROUND_NUMBER | — | ✅ |
| 18 | NegotiationHeaderAuctionStatus | AUCTION_STATUS | — | ✅ |
| 19 | NegotiationHeaderAuctionTitle | AUCTION_TITLE | — | ✅ |
| 20 | NegotiationHeaderAutoExtendAllLinesFlag | AUTO_EXTEND_ALL_LINES_FLAG | — | — |
| 21 | NegotiationHeaderAutoExtendDuration | AUTO_EXTEND_DURATION | — | — |
| 22 | NegotiationHeaderAutoExtendEnabledFlag | AUTO_EXTEND_ENABLED_FLAG | — | — |
| 23 | NegotiationHeaderAutoExtendFlag | AUTO_EXTEND_FLAG | — | — |
| 24 | NegotiationHeaderAutoExtendMinTriggerRank | AUTO_EXTEND_MIN_TRIGGER_RANK | — | — |
| 25 | NegotiationHeaderAutoExtendNumber | AUTO_EXTEND_NUMBER | — | — |
| 26 | NegotiationHeaderAutoExtendTypeFlag | AUTO_EXTEND_TYPE_FLAG | — | — |
| 27 | NegotiationHeaderAutoextendChangedFlag | AUTOEXTEND_CHANGED_FLAG | — | — |
| 28 | NegotiationHeaderAwardApprAmeTransId | AWARD_APPR_AME_TRANS_ID | — | — |
| 29 | NegotiationHeaderAwardApprAmeTransPrevId | AWARD_APPR_AME_TRANS_PREV_ID | — | — |
| 30 | NegotiationHeaderAwardApprAmeTxnDate | AWARD_APPR_AME_TXN_DATE | — | — |
| 31 | NegotiationHeaderAwardApprovalFlag | AWARD_APPROVAL_FLAG | — | — |
| 32 | NegotiationHeaderAwardApprovalStatus | AWARD_APPROVAL_STATUS | — | — |
| 33 | NegotiationHeaderAwardByDate | AWARD_BY_DATE | — | — |
| 34 | NegotiationHeaderAwardCompleteDate | AWARD_COMPLETE_DATE | — | ✅ |
| 35 | NegotiationHeaderAwardDate | AWARD_DATE | — | ✅ |
| 36 | NegotiationHeaderAwardMode | AWARD_MODE | — | — |
| 37 | NegotiationHeaderAwardStatus | AWARD_STATUS | — | ✅ |
| 38 | NegotiationHeaderBidDecrementMethod | BID_DECREMENT_METHOD | — | — |
| 39 | NegotiationHeaderBidFrequencyCode | BID_FREQUENCY_CODE | — | — |
| 40 | NegotiationHeaderBidListType | BID_LIST_TYPE | — | — |
| 41 | NegotiationHeaderBidRanking | BID_RANKING | — | ✅ |
| 42 | NegotiationHeaderBidScopeCode | BID_SCOPE_CODE | — | — |
| 43 | NegotiationHeaderBidVisibilityCode | BID_VISIBILITY_CODE | — | ✅ |
| 44 | NegotiationHeaderBuyerTransportEnabledFlag | BUYER_TRANSPORT_ENABLED_FLAG | — | — |
| 45 | NegotiationHeaderBuyerTransportFlag | BUYER_TRANSPORT_FLAG | — | ✅ |
| 46 | NegotiationHeaderCancelDate | CANCEL_DATE | — | — |
| 47 | NegotiationHeaderCarrierId | CARRIER_ID | — | — |
| 48 | NegotiationHeaderCloseBiddingDate | CLOSE_BIDDING_DATE | — | ✅ |
| 49 | NegotiationHeaderCloseDateType | CLOSE_DATE_TYPE | — | — |
| 50 | NegotiationHeaderCompleteFlag | COMPLETE_FLAG | — | — |
| 51 | NegotiationHeaderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 52 | NegotiationHeaderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 53 | NegotiationHeaderContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 54 | NegotiationHeaderContractTemplateId | CONTRACT_TEMPLATE_ID | — | — |
| 55 | NegotiationHeaderContractType | CONTRACT_TYPE | — | — |
| 56 | NegotiationHeaderCreatedBy | CREATED_BY | — | — |
| 57 | NegotiationHeaderCreationDate | CREATION_DATE | — | — |
| 58 | NegotiationHeaderCreationDateOrigAmend | CREATION_DATE_ORIG_AMEND | — | — |
| 59 | NegotiationHeaderCurrencyCode | CURRENCY_CODE | — | ✅ |
| 60 | NegotiationHeaderDaysAfterOpenDate | DAYS_AFTER_OPEN_DATE | — | — |
| 61 | NegotiationHeaderDescription | DESCRIPTION | — | — |
| 62 | NegotiationHeaderDisplayBestPriceBlindFlag | DISPLAY_BEST_PRICE_BLIND_FLAG | — | — |
| 63 | NegotiationHeaderDoctypeId | DOCTYPE_ID | — | — |
| 64 | NegotiationHeaderDocumentNumber | DOCUMENT_NUMBER | — | ✅ |
| 65 | NegotiationHeaderDraftLocked | DRAFT_LOCKED | — | — |
| 66 | NegotiationHeaderDraftLockedDate | DRAFT_LOCKED_DATE | — | — |
| 67 | NegotiationHeaderDraftUnlockedDate | DRAFT_UNLOCKED_DATE | — | — |
| 68 | NegotiationHeaderEnforcePrevrndBidPriceFlag | ENFORCE_PREVRND_BID_PRICE_FLAG | — | — |
| 69 | NegotiationHeaderEventId | EVENT_ID | — | — |
| 70 | NegotiationHeaderEventTitle | EVENT_TITLE | — | — |
| 71 | NegotiationHeaderExtAttribute1 | EXT_ATTRIBUTE1 | — | — |
| 72 | NegotiationHeaderExtAttribute10 | EXT_ATTRIBUTE10 | — | — |
| 73 | NegotiationHeaderExtAttribute11 | EXT_ATTRIBUTE11 | — | — |
| 74 | NegotiationHeaderExtAttribute12 | EXT_ATTRIBUTE12 | — | — |
| 75 | NegotiationHeaderExtAttribute13 | EXT_ATTRIBUTE13 | — | — |
| 76 | NegotiationHeaderExtAttribute14 | EXT_ATTRIBUTE14 | — | — |
| 77 | NegotiationHeaderExtAttribute15 | EXT_ATTRIBUTE15 | — | — |
| 78 | NegotiationHeaderExtAttribute2 | EXT_ATTRIBUTE2 | — | — |
| 79 | NegotiationHeaderExtAttribute3 | EXT_ATTRIBUTE3 | — | — |
| 80 | NegotiationHeaderExtAttribute4 | EXT_ATTRIBUTE4 | — | — |
| 81 | NegotiationHeaderExtAttribute5 | EXT_ATTRIBUTE5 | — | — |
| 82 | NegotiationHeaderExtAttribute6 | EXT_ATTRIBUTE6 | — | — |
| 83 | NegotiationHeaderExtAttribute7 | EXT_ATTRIBUTE7 | — | — |
| 84 | NegotiationHeaderExtAttribute8 | EXT_ATTRIBUTE8 | — | — |
| 85 | NegotiationHeaderExtAttribute9 | EXT_ATTRIBUTE9 | — | — |
| 86 | NegotiationHeaderExtAttributeCategory | EXT_ATTRIBUTE_CATEGORY | — | — |
| 87 | NegotiationHeaderFirstLineCloseDate | FIRST_LINE_CLOSE_DATE | — | — |
| 88 | NegotiationHeaderFobCode | FOB_CODE | — | — |
| 89 | NegotiationHeaderFreightTermsCode | FREIGHT_TERMS_CODE | — | — |
| 90 | NegotiationHeaderFullQuantityBidCode | FULL_QUANTITY_BID_CODE | — | — |
| 91 | NegotiationHeaderGlobalTemplateFlag | GLOBAL_TEMPLATE_FLAG | — | — |
| 92 | NegotiationHeaderGroupEnabledFlag | GROUP_ENABLED_FLAG | — | — |
| 93 | NegotiationHeaderHasHdrAttrFlag | HAS_HDR_ATTR_FLAG | — | — |
| 94 | NegotiationHeaderHasItemsFlag | HAS_ITEMS_FLAG | — | — |
| 95 | NegotiationHeaderHasPeForAllItems | HAS_PE_FOR_ALL_ITEMS | — | — |
| 96 | NegotiationHeaderHasPriceElements | HAS_PRICE_ELEMENTS | — | — |
| 97 | NegotiationHeaderHasScoringTeamsFlag | HAS_SCORING_TEAMS_FLAG | — | — |
| 98 | NegotiationHeaderHdrAttrDisplayScore | HDR_ATTR_DISPLAY_SCORE | — | ✅ |
| 99 | NegotiationHeaderHdrAttrEnableWeights | HDR_ATTR_ENABLE_WEIGHTS | — | ✅ |
| 100 | NegotiationHeaderHdrAttrMaximumScore | HDR_ATTR_MAXIMUM_SCORE | — | — |
| 101 | NegotiationHeaderHdrAttributeEnabledFlag | HDR_ATTRIBUTE_ENABLED_FLAG | — | — |
| 102 | NegotiationHeaderImportFileName | IMPORT_FILE_NAME | — | — |
| 103 | NegotiationHeaderIncludePdfInExternalPage | INCLUDE_PDF_IN_EXTERNAL_PAGE | — | — |
| 104 | NegotiationHeaderIntAttribute1 | INT_ATTRIBUTE1 | — | — |
| 105 | NegotiationHeaderIntAttribute10 | INT_ATTRIBUTE10 | — | — |
| 106 | NegotiationHeaderIntAttribute11 | INT_ATTRIBUTE11 | — | — |
| 107 | NegotiationHeaderIntAttribute12 | INT_ATTRIBUTE12 | — | — |
| 108 | NegotiationHeaderIntAttribute13 | INT_ATTRIBUTE13 | — | — |
| 109 | NegotiationHeaderIntAttribute14 | INT_ATTRIBUTE14 | — | — |
| 110 | NegotiationHeaderIntAttribute15 | INT_ATTRIBUTE15 | — | — |
| 111 | NegotiationHeaderIntAttribute2 | INT_ATTRIBUTE2 | — | — |
| 112 | NegotiationHeaderIntAttribute3 | INT_ATTRIBUTE3 | — | — |
| 113 | NegotiationHeaderIntAttribute4 | INT_ATTRIBUTE4 | — | — |
| 114 | NegotiationHeaderIntAttribute5 | INT_ATTRIBUTE5 | — | — |
| 115 | NegotiationHeaderIntAttribute6 | INT_ATTRIBUTE6 | — | — |
| 116 | NegotiationHeaderIntAttribute7 | INT_ATTRIBUTE7 | — | — |
| 117 | NegotiationHeaderIntAttribute8 | INT_ATTRIBUTE8 | — | — |
| 118 | NegotiationHeaderIntAttribute9 | INT_ATTRIBUTE9 | — | — |
| 119 | NegotiationHeaderIntAttributeCategory | INT_ATTRIBUTE_CATEGORY | — | — |
| 120 | NegotiationHeaderIsPaused | IS_PAUSED | — | — |
| 121 | NegotiationHeaderIsTemplateFlag | IS_TEMPLATE_FLAG | — | — |
| 122 | NegotiationHeaderLanguageCode | LANGUAGE_CODE | — | — |
| 123 | NegotiationHeaderLargeNegEnabledFlag | LARGE_NEG_ENABLED_FLAG | — | — |
| 124 | NegotiationHeaderLastLineNumber | LAST_LINE_NUMBER | — | — |
| 125 | NegotiationHeaderLastPauseDate | LAST_PAUSE_DATE | — | — |
| 126 | NegotiationHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 127 | NegotiationHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 128 | NegotiationHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 129 | NegotiationHeaderLineAttributeEnabledFlag | LINE_ATTRIBUTE_ENABLED_FLAG | — | — |
| 130 | NegotiationHeaderLineMasEnabledFlag | LINE_MAS_ENABLED_FLAG | — | — |
| 131 | NegotiationHeaderLotEnabledFlag | LOT_ENABLED_FLAG | — | — |
| 132 | NegotiationHeaderMaxBidColorSequenceId | MAX_BID_COLOR_SEQUENCE_ID | — | — |
| 133 | NegotiationHeaderMaxDocumentLineNum | MAX_DOCUMENT_LINE_NUM | — | — |
| 134 | NegotiationHeaderMaxInternalLineNum | MAX_INTERNAL_LINE_NUM | — | — |
| 135 | NegotiationHeaderMaxRetainageNegotiableFlag | MAX_RETAINAGE_NEGOTIABLE_FLAG | — | — |
| 136 | NegotiationHeaderMinBidChangeType | MIN_BID_CHANGE_TYPE | — | — |
| 137 | NegotiationHeaderMinBidDecrement | MIN_BID_DECREMENT | — | — |
| 138 | NegotiationHeaderModeOfTransport | MODE_OF_TRANSPORT | — | — |
| 139 | NegotiationHeaderNegApprovalDate | NEG_APPROVAL_DATE | — | — |
| 140 | NegotiationHeaderNegApprovalEnabledFlag | NEG_APPROVAL_ENABLED_FLAG | — | — |
| 141 | NegotiationHeaderNegTeamEnabledFlag | NEG_TEAM_ENABLED_FLAG | — | — |
| 142 | NegotiationHeaderNumberOfBids | NUMBER_OF_BIDS | — | — |
| 143 | NegotiationHeaderNumberOfExtensions | NUMBER_OF_EXTENSIONS | — | — |
| 144 | NegotiationHeaderNumberOfLines | NUMBER_OF_LINES | — | — |
| 145 | NegotiationHeaderNumberPriceDecimals | NUMBER_PRICE_DECIMALS | — | ✅ |
| 146 | NegotiationHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 147 | NegotiationHeaderOpenAuctionNowFlag | OPEN_AUCTION_NOW_FLAG | — | ✅ |
| 148 | NegotiationHeaderOpenBiddingDate | OPEN_BIDDING_DATE | — | ✅ |
| 149 | NegotiationHeaderOriginalCloseBiddingDate | ORIGINAL_CLOSE_BIDDING_DATE | — | — |
| 150 | NegotiationHeaderOutcomeStatus | OUTCOME_STATUS | — | — |
| 151 | NegotiationHeaderPauseRemarks | PAUSE_REMARKS | — | — |
| 152 | NegotiationHeaderPaymentTermsId | PAYMENT_TERMS_ID | — | — |
| 153 | NegotiationHeaderPersonId | PERSON_ID | — | — |
| 154 | NegotiationHeaderPfTypeAllowed | PF_TYPE_ALLOWED | — | — |
| 155 | NegotiationHeaderPoAgreedAmount | PO_AGREED_AMOUNT | — | ✅ |
| 156 | NegotiationHeaderPoEndDate | PO_END_DATE | — | ✅ |
| 157 | NegotiationHeaderPoMinRelAmount | PO_MIN_REL_AMOUNT | — | ✅ |
| 158 | NegotiationHeaderPoStartDate | PO_START_DATE | — | ✅ |
| 159 | NegotiationHeaderPoStyleId | PO_STYLE_ID | — | — |
| 160 | NegotiationHeaderPowerBiddingEnabledFlag | POWER_BIDDING_ENABLED_FLAG | — | — |
| 161 | NegotiationHeaderPrcBuId | PRC_BU_ID | — | — |
| 162 | NegotiationHeaderPriceDrivenAuctionFlag | PRICE_DRIVEN_AUCTION_FLAG | — | — |
| 163 | NegotiationHeaderPriceElementEnabledFlag | PRICE_ELEMENT_ENABLED_FLAG | — | — |
| 164 | NegotiationHeaderPriceTiersIndicator | PRICE_TIERS_INDICATOR | — | ✅ |
| 165 | NegotiationHeaderProgramAppName | PROGRAM_APP_NAME | — | — |
| 166 | NegotiationHeaderProgramName | PROGRAM_NAME | — | — |
| 167 | NegotiationHeaderProgressPaymentType | PROGRESS_PAYMENT_TYPE | — | — |
| 168 | NegotiationHeaderProgressPymtNegotiableFlag | PROGRESS_PYMT_NEGOTIABLE_FLAG | — | — |
| 169 | NegotiationHeaderProjectId | PROJECT_ID | — | — |
| 170 | NegotiationHeaderProxyBiddingEnabledFlag | PROXY_BIDDING_ENABLED_FLAG | — | — |
| 171 | NegotiationHeaderPublishAuctionNowFlag | PUBLISH_AUCTION_NOW_FLAG | — | — |
| 172 | NegotiationHeaderPublishDate | PUBLISH_DATE | — | ✅ |
| 173 | NegotiationHeaderPublishDateOrigAmend | PUBLISH_DATE_ORIG_AMEND | — | — |
| 174 | NegotiationHeaderPublishRatesToBiddersFlag | PUBLISH_RATES_TO_BIDDERS_FLAG | — | — |
| 175 | NegotiationHeaderQtyPriceTiersEnabledFlag | QTY_PRICE_TIERS_ENABLED_FLAG | — | — |
| 176 | NegotiationHeaderRankIndicator | RANK_INDICATOR | — | ✅ |
| 177 | NegotiationHeaderRateDate | RATE_DATE | — | — |
| 178 | NegotiationHeaderRateType | RATE_TYPE | — | — |
| 179 | NegotiationHeaderRecoupmentNegotiableFlag | RECOUPMENT_NEGOTIABLE_FLAG | — | — |
| 180 | NegotiationHeaderReminderDate | REMINDER_DATE | — | — |
| 181 | NegotiationHeaderReqBuId | REQ_BU_ID | — | — |
| 182 | NegotiationHeaderRequestDate | REQUEST_DATE | — | — |
| 183 | NegotiationHeaderRequestId | REQUEST_ID | — | — |
| 184 | NegotiationHeaderRequestedBy | REQUESTED_BY | — | — |
| 185 | NegotiationHeaderRetainageNegotiableFlag | RETAINAGE_NEGOTIABLE_FLAG | — | — |
| 186 | NegotiationHeaderRfiLineEnabledFlag | RFI_LINE_ENABLED_FLAG | — | — |
| 187 | NegotiationHeaderScoringLockDate | SCORING_LOCK_DATE | — | — |
| 188 | NegotiationHeaderSealedActualUnlockDate | SEALED_ACTUAL_UNLOCK_DATE | — | — |
| 189 | NegotiationHeaderSealedActualUnsealDate | SEALED_ACTUAL_UNSEAL_DATE | — | — |
| 190 | NegotiationHeaderSealedAuctionStatus | SEALED_AUCTION_STATUS | — | — |
| 191 | NegotiationHeaderServiceLevel | SERVICE_LEVEL | — | — |
| 192 | NegotiationHeaderShareAwardDecision | SHARE_AWARD_DECISION | — | — |
| 193 | NegotiationHeaderShowBidderNotes | SHOW_BIDDER_NOTES | — | — |
| 194 | NegotiationHeaderShowBidderScores | SHOW_BIDDER_SCORES | — | — |
| 195 | NegotiationHeaderSourceDocId | SOURCE_DOC_ID | — | — |
| 196 | NegotiationHeaderSourceDocLineMsg | SOURCE_DOC_LINE_MSG | — | — |
| 197 | NegotiationHeaderSourceDocMsg | SOURCE_DOC_MSG | — | — |
| 198 | NegotiationHeaderSourceDocMsgApp | SOURCE_DOC_MSG_APP | — | — |
| 199 | NegotiationHeaderSourceDocNumber | SOURCE_DOC_NUMBER | — | ✅ |
| 200 | NegotiationHeaderSourceReqsFlag | SOURCE_REQS_FLAG | — | — |
| 201 | NegotiationHeaderStaggeredClosingInterval | STAGGERED_CLOSING_INTERVAL | — | — |
| 202 | NegotiationHeaderStyleId | STYLE_ID | — | — |
| 203 | NegotiationHeaderSupplierEnterablePymtFlag | SUPPLIER_ENTERABLE_PYMT_FLAG | — | — |
| 204 | NegotiationHeaderSupplierViewType | SUPPLIER_VIEW_TYPE | — | — |
| 205 | NegotiationHeaderTeamScoringEnabledFlag | TEAM_SCORING_ENABLED_FLAG | — | — |
| 206 | NegotiationHeaderTechnicalActualUnlockDate | TECHNICAL_ACTUAL_UNLOCK_DATE | — | — |
| 207 | NegotiationHeaderTechnicalActualUnsealDate | TECHNICAL_ACTUAL_UNSEAL_DATE | — | — |
| 208 | NegotiationHeaderTechnicalEvaluationStatus | TECHNICAL_EVALUATION_STATUS | — | — |
| 209 | NegotiationHeaderTechnicalLockStatus | TECHNICAL_LOCK_STATUS | — | — |
| 210 | NegotiationHeaderTemplateId | TEMPLATE_ID | — | — |
| 211 | NegotiationHeaderTemplateScope | TEMPLATE_SCOPE | — | — |
| 212 | NegotiationHeaderTemplateStatus | TEMPLATE_STATUS | — | — |
| 213 | NegotiationHeaderTwoPartFlag | TWO_PART_FLAG | — | — |
| 214 | NegotiationHeaderTwostageEvalEnabledFlag | TWOSTAGE_EVAL_ENABLED_FLAG | — | — |
| 215 | NegotiationHeaderVersionNum | VERSION_NUM | — | — |
| 216 | NegotiationHeaderViewByDate | VIEW_BY_DATE | — | ✅ |
| 217 | NegotiationHeaderWfApprovalItemKey | WF_APPROVAL_ITEM_KEY | — | — |
| 218 | NegotiationHeaderWfAwardApprovalItemKey | WF_AWARD_APPROVAL_ITEM_KEY | — | — |
| 219 | NegotiationHeaderWfItemKey | WF_ITEM_KEY | — | — |
| 220 | NegotiationHeaderWfPoncomplCurrentRound | WF_PONCOMPL_CURRENT_ROUND | — | — |
| 221 | NegotiationHeaderWfPoncomplItemKey | WF_PONCOMPL_ITEM_KEY | — | — |
| 222 | NegotiationHeaderWfRoleName | WF_ROLE_NAME | — | — |

### [[pon_neg_team_members|PON_NEG_TEAM_MEMBERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccessType | ACCESS_TYPE | — | ✅ |
| 2 | AuctionHeaderId | AUCTION_HEADER_ID | 🔑 | ✅ |
| 3 | NegotiationCollaborationApprovalStatus | APPROVAL_STATUS | — | — |
| 4 | NegotiationCollaborationApproverFlag | APPROVER_FLAG | — | — |
| 5 | NegotiationCollaborationCompletionDate | COMPLETION_DATE | — | ✅ |
| 6 | NegotiationCollaborationCreatedBy | CREATED_BY | — | — |
| 7 | NegotiationCollaborationCreationDate | CREATION_DATE | — | ✅ |
| 8 | NegotiationCollaborationLastAmendmentUpdate | LAST_AMENDMENT_UPDATE | — | — |
| 9 | NegotiationCollaborationLastNotifiedDate | LAST_NOTIFIED_DATE | — | — |
| 10 | NegotiationCollaborationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | NegotiationCollaborationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | NegotiationCollaborationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | NegotiationCollaborationMemberType | MEMBER_TYPE | — | — |
| 14 | NegotiationCollaborationModifiedFlag | MODIFIED_FLAG | — | — |
| 15 | NegotiationCollaborationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | NegotiationCollaborationPersonId | PERSON_ID | — | — |
| 17 | NegotiationCollaborationTargetDate | TARGET_DATE | — | ✅ |
| 18 | NegotiationCollaborationTaskName | TASK_NAME | — | ✅ |
| 19 | SequenceNumber | SEQUENCE_NUMBER | 🔑 | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
