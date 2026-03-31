---
id: DOC-PO-PVO-NegDocumentSourcingNegotiationAndTemplatePVO
doc_type: system-doc
title: "NegDocumentSourcingNegotiationAndTemplatePVO — PVO Purchasing"
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
  - NegDocumentSourcingNegotiationAndTemplatePVO
  - negdocumentsourcingnegotiationandtemplatepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegDocumentSourcingNegotiationAndTemplatePVO

## 📌 Visão Geral

Extrai o vínculo entre documentos de sourcing, negociações e templates utilizados. Permite análise de reutilização de templates e eficiência na configuração de eventos de sourcing.

**Caminho:** `FscmTopModelAM.PrcPonPublicViewAM.NegDocumentSourcingNegotiationAndTemplatePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 202 | 3 | 6 | 77 | 38% |

---

## 🔗 Tabelas Relacionadas

- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 13 atributos
- [[pon_action_history|PON_ACTION_HISTORY]] — 7 atributos (5 PKs, 6 BICC)
- [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]] — 182 atributos (1 PKs, 71 BICC)

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

### [[pon_action_history|PON_ACTION_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationActionHistoryActionType | ACTION_TYPE | 🔑 | ✅ |
| 2 | NegotiationActionHistoryApprovalIdentificationKey | APPROVAL_IDENTIFICATION_KEY | — | — |
| 3 | NegotiationActionHistoryCreationDate | CREATION_DATE | — | ✅ |
| 4 | NegotiationActionHistoryObjectId | OBJECT_ID | 🔑 | ✅ |
| 5 | NegotiationActionHistoryObjectId2 | OBJECT_ID2 | 🔑 | ✅ |
| 6 | NegotiationActionHistoryObjectTypeCode | OBJECT_TYPE_CODE | 🔑 | ✅ |
| 7 | NegotiationActionHistorySequenceNum | SEQUENCE_NUM | 🔑 | ✅ |

### [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AuctionHeaderId | AUCTION_HEADER_ID | 🔑 | ✅ |
| 2 | NegotiationHeaderAbstractDetails | ABSTRACT_DETAILS | — | — |
| 3 | NegotiationHeaderAbstractStatus | ABSTRACT_STATUS | — | — |
| 4 | NegotiationHeaderAdvanceNegotiableFlag | ADVANCE_NEGOTIABLE_FLAG | — | — |
| 5 | NegotiationHeaderAllowAlternateLines | ALLOW_ALTERNATE_LINES | — | ✅ |
| 6 | NegotiationHeaderAllowOtherBidCurrencyFlag | ALLOW_OTHER_BID_CURRENCY_FLAG | — | — |
| 7 | NegotiationHeaderAmendmentDescription | AMENDMENT_DESCRIPTION | — | — |
| 8 | NegotiationHeaderAmendmentNumber | AMENDMENT_NUMBER | — | ✅ |
| 9 | NegotiationHeaderApprIdentificationKey | NEG_APPR_IDENTIFICATION_KEY | — | — |
| 10 | NegotiationHeaderApprovalAmount | APPROVAL_AMOUNT | — | ✅ |
| 11 | NegotiationHeaderApprovalStatus | NEG_APPROVAL_STATUS | — | ✅ |
| 12 | NegotiationHeaderAttributeLineNumber | ATTRIBUTE_LINE_NUMBER | — | — |
| 13 | NegotiationHeaderAttributesExist | ATTRIBUTES_EXIST | — | — |
| 14 | NegotiationHeaderAuctionHeaderIdOrigAmend | AUCTION_HEADER_ID_ORIG_AMEND | — | ✅ |
| 15 | NegotiationHeaderAuctionHeaderIdOrigRound | AUCTION_HEADER_ID_ORIG_ROUND | — | — |
| 16 | NegotiationHeaderAuctionHeaderIdPrevAmend | AUCTION_HEADER_ID_PREV_AMEND | — | — |
| 17 | NegotiationHeaderAuctionHeaderIdPrevRound | AUCTION_HEADER_ID_PREV_ROUND | — | — |
| 18 | NegotiationHeaderAuctionOriginationCode | AUCTION_ORIGINATION_CODE | — | ✅ |
| 19 | NegotiationHeaderAuctionRoundNumber | AUCTION_ROUND_NUMBER | — | ✅ |
| 20 | NegotiationHeaderAuctionStatus | AUCTION_STATUS | — | ✅ |
| 21 | NegotiationHeaderAuctionTitle | AUCTION_TITLE | — | ✅ |
| 22 | NegotiationHeaderAutoExtendAllLinesFlag | AUTO_EXTEND_ALL_LINES_FLAG | — | — |
| 23 | NegotiationHeaderAutoExtendDuration | AUTO_EXTEND_DURATION | — | — |
| 24 | NegotiationHeaderAutoExtendEnabledFlag | AUTO_EXTEND_ENABLED_FLAG | — | — |
| 25 | NegotiationHeaderAutoExtendFlag | AUTO_EXTEND_FLAG | — | — |
| 26 | NegotiationHeaderAutoExtendMinTriggerRank | AUTO_EXTEND_MIN_TRIGGER_RANK | — | — |
| 27 | NegotiationHeaderAutoExtendNumber | AUTO_EXTEND_NUMBER | — | — |
| 28 | NegotiationHeaderAutoExtendTypeFlag | AUTO_EXTEND_TYPE_FLAG | — | — |
| 29 | NegotiationHeaderAutoextendChangedFlag | AUTOEXTEND_CHANGED_FLAG | — | — |
| 30 | NegotiationHeaderAwardApprovalDate | AWARD_APPROVAL_DATE | — | ✅ |
| 31 | NegotiationHeaderAwardApprovalFlag | AWARD_APPROVAL_FLAG | — | ✅ |
| 32 | NegotiationHeaderAwardApprovalStatus | AWARD_APPROVAL_STATUS | — | ✅ |
| 33 | NegotiationHeaderAwardByDate | AWARD_BY_DATE | — | ✅ |
| 34 | NegotiationHeaderAwardCompleteDate | AWARD_COMPLETE_DATE | — | ✅ |
| 35 | NegotiationHeaderAwardDate | AWARD_DATE | — | — |
| 36 | NegotiationHeaderAwardMode | AWARD_MODE | — | — |
| 37 | NegotiationHeaderAwardStatus | AWARD_STATUS | — | ✅ |
| 38 | NegotiationHeaderBidDecrementMethod | BID_DECREMENT_METHOD | — | — |
| 39 | NegotiationHeaderBidFrequencyCode | BID_FREQUENCY_CODE | — | — |
| 40 | NegotiationHeaderBidFrequencyCodeDspFlag | BID_FREQUENCY_CODE_DSP_FLAG | — | ✅ |
| 41 | NegotiationHeaderBidListType | BID_LIST_TYPE | — | — |
| 42 | NegotiationHeaderBidListTypeDspFlag | BID_LIST_TYPE_DSP_FLAG | — | ✅ |
| 43 | NegotiationHeaderBidRanking | BID_RANKING | — | ✅ |
| 44 | NegotiationHeaderBidRevisionType | BID_REVISION_TYPE | — | ✅ |
| 45 | NegotiationHeaderBidRevisionTypeDspFlag | BID_REVISION_TYPE_DSP_FLAG | — | ✅ |
| 46 | NegotiationHeaderBidScopeCode | BID_SCOPE_CODE | — | — |
| 47 | NegotiationHeaderBidScopeCodeDspFlag | BID_SCOPE_CODE_DSP_FLAG | — | ✅ |
| 48 | NegotiationHeaderBidVisibilityCode | BID_VISIBILITY_CODE | — | ✅ |
| 49 | NegotiationHeaderBuyerTransportEnabledFlag | BUYER_TRANSPORT_ENABLED_FLAG | — | ✅ |
| 50 | NegotiationHeaderBuyerTransportFlag | BUYER_TRANSPORT_FLAG | — | ✅ |
| 51 | NegotiationHeaderCancelDate | CANCEL_DATE | — | — |
| 52 | NegotiationHeaderCarrierId | CARRIER_ID | — | — |
| 53 | NegotiationHeaderCloseBiddingDate | CLOSE_BIDDING_DATE | — | ✅ |
| 54 | NegotiationHeaderCloseDateType | CLOSE_DATE_TYPE | — | — |
| 55 | NegotiationHeaderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 56 | NegotiationHeaderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 57 | NegotiationHeaderContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 58 | NegotiationHeaderContractTemplateId | CONTRACT_TEMPLATE_ID | — | — |
| 59 | NegotiationHeaderContractType | CONTRACT_TYPE | — | ✅ |
| 60 | NegotiationHeaderCreatedBy | CREATED_BY | — | ✅ |
| 61 | NegotiationHeaderCreationDate | CREATION_DATE | — | ✅ |
| 62 | NegotiationHeaderCreationDateOrigAmend | CREATION_DATE_ORIG_AMEND | — | ✅ |
| 63 | NegotiationHeaderCurrencyCode | CURRENCY_CODE | — | ✅ |
| 64 | NegotiationHeaderDaysAfterOpenDate | DAYS_AFTER_OPEN_DATE | — | — |
| 65 | NegotiationHeaderDescription | DESCRIPTION | — | — |
| 66 | NegotiationHeaderDisplayBestPriceBlindFlag | DISPLAY_BEST_PRICE_BLIND_FLAG | — | — |
| 67 | NegotiationHeaderDisplayBestPriceDspFlag | DISPLAY_BEST_PRICE_DSP_FLAG | — | ✅ |
| 68 | NegotiationHeaderDoctypeId | DOCTYPE_ID | — | ✅ |
| 69 | NegotiationHeaderDocumentNumber | DOCUMENT_NUMBER | — | ✅ |
| 70 | NegotiationHeaderDraftLocked | DRAFT_LOCKED | — | — |
| 71 | NegotiationHeaderDraftLockedDate | DRAFT_LOCKED_DATE | — | — |
| 72 | NegotiationHeaderDraftUnlockedDate | DRAFT_UNLOCKED_DATE | — | — |
| 73 | NegotiationHeaderEnforcePrevrndBidPriceFlag | ENFORCE_PREVRND_BID_PRICE_FLAG | — | — |
| 74 | NegotiationHeaderFirstLineCloseDate | FIRST_LINE_CLOSE_DATE | — | — |
| 75 | NegotiationHeaderFobCode | FOB_CODE | — | — |
| 76 | NegotiationHeaderFreightTermsCode | FREIGHT_TERMS_CODE | — | — |
| 77 | NegotiationHeaderFullQuantityBidCode | FULL_QUANTITY_BID_CODE | — | — |
| 78 | NegotiationHeaderGlobalTemplateFlag | GLOBAL_TEMPLATE_FLAG | — | — |
| 79 | NegotiationHeaderGroupEnabledFlag | GROUP_ENABLED_FLAG | — | — |
| 80 | NegotiationHeaderHasHdrAttrFlag | HAS_HDR_ATTR_FLAG | — | — |
| 81 | NegotiationHeaderHasItemsFlag | HAS_ITEMS_FLAG | — | ✅ |
| 82 | NegotiationHeaderHasPeForAllItems | HAS_PE_FOR_ALL_ITEMS | — | — |
| 83 | NegotiationHeaderHasPriceElements | HAS_PRICE_ELEMENTS | — | — |
| 84 | NegotiationHeaderHasScoringTeamsFlag | HAS_SCORING_TEAMS_FLAG | — | — |
| 85 | NegotiationHeaderHdrAttrDisplayScore | HDR_ATTR_DISPLAY_SCORE | — | ✅ |
| 86 | NegotiationHeaderHdrAttrEnableWeights | HDR_ATTR_ENABLE_WEIGHTS | — | ✅ |
| 87 | NegotiationHeaderHdrAttrMaximumScore | HDR_ATTR_MAXIMUM_SCORE | — | — |
| 88 | NegotiationHeaderHdrAttributeEnabledFlag | HDR_ATTRIBUTE_ENABLED_FLAG | — | — |
| 89 | NegotiationHeaderImportFileName | IMPORT_FILE_NAME | — | — |
| 90 | NegotiationHeaderIncludePdfInExternalPage | INCLUDE_PDF_IN_EXTERNAL_PAGE | — | — |
| 91 | NegotiationHeaderIsPaused | IS_PAUSED | — | — |
| 92 | NegotiationHeaderIsTemplateFlag | IS_TEMPLATE_FLAG | — | — |
| 93 | NegotiationHeaderLanguageCode | LANGUAGE_CODE | — | — |
| 94 | NegotiationHeaderLargeNegEnabledFlag | LARGE_NEG_ENABLED_FLAG | — | — |
| 95 | NegotiationHeaderLastLineNumber | LAST_LINE_NUMBER | — | — |
| 96 | NegotiationHeaderLastPauseDate | LAST_PAUSE_DATE | — | — |
| 97 | NegotiationHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 98 | NegotiationHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 99 | NegotiationHeaderLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 100 | NegotiationHeaderLineAttributeEnabledFlag | LINE_ATTRIBUTE_ENABLED_FLAG | — | — |
| 101 | NegotiationHeaderLineMasEnabledFlag | LINE_MAS_ENABLED_FLAG | — | — |
| 102 | NegotiationHeaderLotEnabledFlag | LOT_ENABLED_FLAG | — | — |
| 103 | NegotiationHeaderMaxBidColorSequenceId | MAX_BID_COLOR_SEQUENCE_ID | — | — |
| 104 | NegotiationHeaderMaxDocumentLineNum | MAX_DOCUMENT_LINE_NUM | — | — |
| 105 | NegotiationHeaderMaxInternalLineNum | MAX_INTERNAL_LINE_NUM | — | — |
| 106 | NegotiationHeaderMinBidChangeType | MIN_BID_CHANGE_TYPE | — | — |
| 107 | NegotiationHeaderMinBidDecrement | MIN_BID_DECREMENT | — | — |
| 108 | NegotiationHeaderModeOfTransport | MODE_OF_TRANSPORT | — | ✅ |
| 109 | NegotiationHeaderNegApprovalDate | NEG_APPROVAL_DATE | — | ✅ |
| 110 | NegotiationHeaderNegApprovalEnabledFlag | NEG_APPROVAL_ENABLED_FLAG | — | ✅ |
| 111 | NegotiationHeaderNegTeamEnabledFlag | NEG_TEAM_ENABLED_FLAG | — | — |
| 112 | NegotiationHeaderNumberOfBids | NUMBER_OF_BIDS | — | — |
| 113 | NegotiationHeaderNumberOfExtensions | NUMBER_OF_EXTENSIONS | — | — |
| 114 | NegotiationHeaderNumberOfLines | NUMBER_OF_LINES | — | — |
| 115 | NegotiationHeaderNumberPriceDecimals | NUMBER_PRICE_DECIMALS | — | ✅ |
| 116 | NegotiationHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 117 | NegotiationHeaderOpenAuctionNowFlag | OPEN_AUCTION_NOW_FLAG | — | ✅ |
| 118 | NegotiationHeaderOpenBiddingDate | OPEN_BIDDING_DATE | — | ✅ |
| 119 | NegotiationHeaderOriginalCloseBiddingDate | ORIGINAL_CLOSE_BIDDING_DATE | — | ✅ |
| 120 | NegotiationHeaderOutcomeStatus | OUTCOME_STATUS | — | — |
| 121 | NegotiationHeaderPauseRemarks | PAUSE_REMARKS | — | — |
| 122 | NegotiationHeaderPaymentTermsId | PAYMENT_TERMS_ID | — | — |
| 123 | NegotiationHeaderPersonId | PERSON_ID | — | ✅ |
| 124 | NegotiationHeaderPfTypeAllowed | PF_TYPE_ALLOWED | — | — |
| 125 | NegotiationHeaderPoAgreedAmount | PO_AGREED_AMOUNT | — | ✅ |
| 126 | NegotiationHeaderPoEndDate | PO_END_DATE | — | ✅ |
| 127 | NegotiationHeaderPoMinRelAmount | PO_MIN_REL_AMOUNT | — | ✅ |
| 128 | NegotiationHeaderPoStartDate | PO_START_DATE | — | ✅ |
| 129 | NegotiationHeaderPoStyleId | PO_STYLE_ID | — | — |
| 130 | NegotiationHeaderPowerBiddingEnabledFlag | POWER_BIDDING_ENABLED_FLAG | — | — |
| 131 | NegotiationHeaderPrcBuId | PRC_BU_ID | — | ✅ |
| 132 | NegotiationHeaderPriceDrivenAuctionFlag | PRICE_DRIVEN_AUCTION_FLAG | — | — |
| 133 | NegotiationHeaderPriceElementEnabledFlag | PRICE_ELEMENT_ENABLED_FLAG | — | — |
| 134 | NegotiationHeaderPriceTiersIndicator | PRICE_TIERS_INDICATOR | — | ✅ |
| 135 | NegotiationHeaderProgramAppName | PROGRAM_APP_NAME | — | — |
| 136 | NegotiationHeaderProgramName | PROGRAM_NAME | — | — |
| 137 | NegotiationHeaderProjectId | PROJECT_ID | — | — |
| 138 | NegotiationHeaderProxyBiddingEnabledFlag | PROXY_BIDDING_ENABLED_FLAG | — | — |
| 139 | NegotiationHeaderPublishAuctionNowFlag | PUBLISH_AUCTION_NOW_FLAG | — | — |
| 140 | NegotiationHeaderPublishDate | PUBLISH_DATE | — | ✅ |
| 141 | NegotiationHeaderPublishDateOrigAmend | PUBLISH_DATE_ORIG_AMEND | — | ✅ |
| 142 | NegotiationHeaderPublishRatesToBiddersFlag | PUBLISH_RATES_TO_BIDDERS_FLAG | — | — |
| 143 | NegotiationHeaderQtyPriceTiersEnabledFlag | QTY_PRICE_TIERS_ENABLED_FLAG | — | — |
| 144 | NegotiationHeaderRankIndicator | RANK_INDICATOR | — | ✅ |
| 145 | NegotiationHeaderRateDate | RATE_DATE | — | ✅ |
| 146 | NegotiationHeaderRateType | RATE_TYPE | — | ✅ |
| 147 | NegotiationHeaderReminderDate | REMINDER_DATE | — | — |
| 148 | NegotiationHeaderReqBuId | REQ_BU_ID | — | ✅ |
| 149 | NegotiationHeaderRequestDate | REQUEST_DATE | — | — |
| 150 | NegotiationHeaderRequestId | REQUEST_ID | — | — |
| 151 | NegotiationHeaderRequestedBy | REQUESTED_BY | — | — |
| 152 | NegotiationHeaderRfiLineEnabledFlag | RFI_LINE_ENABLED_FLAG | — | — |
| 153 | NegotiationHeaderScoringLockDate | SCORING_LOCK_DATE | — | — |
| 154 | NegotiationHeaderSealedActualUnlockDate | SEALED_ACTUAL_UNLOCK_DATE | — | ✅ |
| 155 | NegotiationHeaderSealedActualUnsealDate | SEALED_ACTUAL_UNSEAL_DATE | — | — |
| 156 | NegotiationHeaderSealedAuctionStatus | SEALED_AUCTION_STATUS | — | ✅ |
| 157 | NegotiationHeaderServiceLevel | SERVICE_LEVEL | — | ✅ |
| 158 | NegotiationHeaderShareAwardDecision | SHARE_AWARD_DECISION | — | — |
| 159 | NegotiationHeaderShowBidderNotes | SHOW_BIDDER_NOTES | — | — |
| 160 | NegotiationHeaderShowBidderScores | SHOW_BIDDER_SCORES | — | — |
| 161 | NegotiationHeaderSourceDocId | SOURCE_DOC_ID | — | ✅ |
| 162 | NegotiationHeaderSourceDocLineMsg | SOURCE_DOC_LINE_MSG | — | — |
| 163 | NegotiationHeaderSourceDocMsg | SOURCE_DOC_MSG | — | — |
| 164 | NegotiationHeaderSourceDocMsgApp | SOURCE_DOC_MSG_APP | — | — |
| 165 | NegotiationHeaderSourceDocNumber | SOURCE_DOC_NUMBER | — | ✅ |
| 166 | NegotiationHeaderSourceReqsFlag | SOURCE_REQS_FLAG | — | — |
| 167 | NegotiationHeaderStaggeredClosingInterval | STAGGERED_CLOSING_INTERVAL | — | — |
| 168 | NegotiationHeaderStyleId | STYLE_ID | — | ✅ |
| 169 | NegotiationHeaderSupplierViewType | SUPPLIER_VIEW_TYPE | — | — |
| 170 | NegotiationHeaderSynopsis | SYNOPSIS | — | ✅ |
| 171 | NegotiationHeaderTeamScoringEnabledFlag | TEAM_SCORING_ENABLED_FLAG | — | — |
| 172 | NegotiationHeaderTechnicalActualUnlockDate | TECHNICAL_ACTUAL_UNLOCK_DATE | — | ✅ |
| 173 | NegotiationHeaderTechnicalActualUnsealDate | TECHNICAL_ACTUAL_UNSEAL_DATE | — | — |
| 174 | NegotiationHeaderTechnicalEvaluationStatus | TECHNICAL_EVALUATION_STATUS | — | — |
| 175 | NegotiationHeaderTechnicalLockStatus | TECHNICAL_LOCK_STATUS | — | ✅ |
| 176 | NegotiationHeaderTemplateId | TEMPLATE_ID | — | — |
| 177 | NegotiationHeaderTemplateScope | TEMPLATE_SCOPE | — | — |
| 178 | NegotiationHeaderTemplateStatus | TEMPLATE_STATUS | — | — |
| 179 | NegotiationHeaderTwoPartFlag | TWO_PART_FLAG | — | ✅ |
| 180 | NegotiationHeaderTwostageEvalEnabledFlag | TWOSTAGE_EVAL_ENABLED_FLAG | — | ✅ |
| 181 | NegotiationHeaderVersionNum | VERSION_NUM | — | — |
| 182 | NegotiationHeaderViewByDate | VIEW_BY_DATE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
