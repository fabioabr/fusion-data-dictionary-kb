---
id: DOC-PO-PVO-NegDocumentSourcingSupplierInviteePVO
doc_type: system-doc
title: "NegDocumentSourcingSupplierInviteePVO — PVO Purchasing"
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
  - NegDocumentSourcingSupplierInviteePVO
  - negdocumentsourcingsupplierinviteepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegDocumentSourcingSupplierInviteePVO

## 📌 Visão Geral

Extrai fornecedores convidados vinculados a documentos de sourcing, com dados de participação e status de proposta. Suporta auditoria de processo e análise de alcance de mercado.

**Caminho:** `FscmTopModelAM.PrcPonPublicViewAM.NegDocumentSourcingSupplierInviteePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 326 | 7 | 3 | 84 | 26% |

---

## 🔗 Tabelas Relacionadas

- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 12 atributos
- [[hz_parties|HZ_PARTIES]] — 8 atributos (2 BICC)
- [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]] — 230 atributos (55 BICC)
- [[pon_bidding_parties|PON_BIDDING_PARTIES]] — 32 atributos (3 PKs, 18 BICC)
- [[poz_contact_requests|POZ_CONTACT_REQUESTS]] — 5 atributos
- [[poz_supplier_registrations|POZ_SUPPLIER_REGISTRATIONS]] — 37 atributos (9 BICC)
- [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]] — 2 atributos

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
| 9 | DailyConversionTypeNegoHdrPivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 10 | DailyConversionTypeNegoHdrSecurityFlag | SECURITY_FLAG | — | — |
| 11 | DailyConversionTypeNegoHdrUserConversionType | USER_CONVERSION_TYPE | — | — |
| 12 | DailyConversionTypeNegoHdrUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupplierContactPartyId | PARTY_ID | — | — |
| 2 | SupplierContactPartyName | PARTY_NAME | — | ✅ |
| 3 | SupplierContactPersonFirstName | PERSON_FIRST_NAME | — | — |
| 4 | SupplierContactPersonLastName | PERSON_LAST_NAME | — | — |
| 5 | SupplierContactPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 6 | SupplierContactPersonTitle | PERSON_TITLE | — | — |
| 7 | SupplierPartyId | PARTY_ID | — | — |
| 8 | SupplierPartyName | PARTY_NAME | — | ✅ |

### [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationHeaderAbstractDetails | ABSTRACT_DETAILS | — | — |
| 2 | NegotiationHeaderAbstractStatus | ABSTRACT_STATUS | — | — |
| 3 | NegotiationHeaderAdvanceNegotiableFlag | ADVANCE_NEGOTIABLE_FLAG | — | — |
| 4 | NegotiationHeaderAllowAlternateLines | ALLOW_ALTERNATE_LINES | — | ✅ |
| 5 | NegotiationHeaderAllowOtherBidCurrencyFlag | ALLOW_OTHER_BID_CURRENCY_FLAG | — | — |
| 6 | NegotiationHeaderAmendmentDescription | AMENDMENT_DESCRIPTION | — | — |
| 7 | NegotiationHeaderAmendmentNumber | AMENDMENT_NUMBER | — | ✅ |
| 8 | NegotiationHeaderApprovalAmount | APPROVAL_AMOUNT | — | ✅ |
| 9 | NegotiationHeaderApprovalStatus | NEG_APPROVAL_STATUS | — | ✅ |
| 10 | NegotiationHeaderAttributeLineNumber | ATTRIBUTE_LINE_NUMBER | — | — |
| 11 | NegotiationHeaderAttributesExist | ATTRIBUTES_EXIST | — | — |
| 12 | NegotiationHeaderAuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 13 | NegotiationHeaderAuctionHeaderIdOrigAmend | AUCTION_HEADER_ID_ORIG_AMEND | — | ✅ |
| 14 | NegotiationHeaderAuctionHeaderIdOrigRound | AUCTION_HEADER_ID_ORIG_ROUND | — | — |
| 15 | NegotiationHeaderAuctionHeaderIdPrevAmend | AUCTION_HEADER_ID_PREV_AMEND | — | — |
| 16 | NegotiationHeaderAuctionHeaderIdPrevRound | AUCTION_HEADER_ID_PREV_ROUND | — | — |
| 17 | NegotiationHeaderAuctionOriginationCode | AUCTION_ORIGINATION_CODE | — | — |
| 18 | NegotiationHeaderAuctionRoundNumber | AUCTION_ROUND_NUMBER | — | ✅ |
| 19 | NegotiationHeaderAuctionStatus | AUCTION_STATUS | — | ✅ |
| 20 | NegotiationHeaderAuctionTitle | AUCTION_TITLE | — | ✅ |
| 21 | NegotiationHeaderAutoExtendAllLinesFlag | AUTO_EXTEND_ALL_LINES_FLAG | — | — |
| 22 | NegotiationHeaderAutoExtendDuration | AUTO_EXTEND_DURATION | — | — |
| 23 | NegotiationHeaderAutoExtendEnabledFlag | AUTO_EXTEND_ENABLED_FLAG | — | — |
| 24 | NegotiationHeaderAutoExtendFlag | AUTO_EXTEND_FLAG | — | — |
| 25 | NegotiationHeaderAutoExtendMinTriggerRank | AUTO_EXTEND_MIN_TRIGGER_RANK | — | — |
| 26 | NegotiationHeaderAutoExtendNumber | AUTO_EXTEND_NUMBER | — | — |
| 27 | NegotiationHeaderAutoExtendTypeFlag | AUTO_EXTEND_TYPE_FLAG | — | — |
| 28 | NegotiationHeaderAutoextendChangedFlag | AUTOEXTEND_CHANGED_FLAG | — | — |
| 29 | NegotiationHeaderAwardApprAmeTransId | AWARD_APPR_AME_TRANS_ID | — | — |
| 30 | NegotiationHeaderAwardApprAmeTransPrevId | AWARD_APPR_AME_TRANS_PREV_ID | — | — |
| 31 | NegotiationHeaderAwardApprAmeTxnDate | AWARD_APPR_AME_TXN_DATE | — | — |
| 32 | NegotiationHeaderAwardApprovalFlag | AWARD_APPROVAL_FLAG | — | — |
| 33 | NegotiationHeaderAwardApprovalStatus | AWARD_APPROVAL_STATUS | — | — |
| 34 | NegotiationHeaderAwardByDate | AWARD_BY_DATE | — | — |
| 35 | NegotiationHeaderAwardCompleteDate | AWARD_COMPLETE_DATE | — | — |
| 36 | NegotiationHeaderAwardDate | AWARD_DATE | — | ✅ |
| 37 | NegotiationHeaderAwardMode | AWARD_MODE | — | — |
| 38 | NegotiationHeaderAwardStatus | AWARD_STATUS | — | ✅ |
| 39 | NegotiationHeaderBidDecrementMethod | BID_DECREMENT_METHOD | — | — |
| 40 | NegotiationHeaderBidFrequencyCode | BID_FREQUENCY_CODE | — | — |
| 41 | NegotiationHeaderBidFrequencyCodeDspFlag | BID_FREQUENCY_CODE_DSP_FLAG | — | ✅ |
| 42 | NegotiationHeaderBidListType | BID_LIST_TYPE | — | — |
| 43 | NegotiationHeaderBidListTypeDspFlag | BID_LIST_TYPE_DSP_FLAG | — | ✅ |
| 44 | NegotiationHeaderBidRanking | BID_RANKING | — | ✅ |
| 45 | NegotiationHeaderBidRevisionType | BID_REVISION_TYPE | — | ✅ |
| 46 | NegotiationHeaderBidRevisionTypeDspFlag | BID_REVISION_TYPE_DSP_FLAG | — | ✅ |
| 47 | NegotiationHeaderBidScopeCode | BID_SCOPE_CODE | — | — |
| 48 | NegotiationHeaderBidScopeCodeDspFlag | BID_SCOPE_CODE_DSP_FLAG | — | ✅ |
| 49 | NegotiationHeaderBidVisibilityCode | BID_VISIBILITY_CODE | — | ✅ |
| 50 | NegotiationHeaderBuyerTransportEnabledFlag | BUYER_TRANSPORT_ENABLED_FLAG | — | ✅ |
| 51 | NegotiationHeaderBuyerTransportFlag | BUYER_TRANSPORT_FLAG | — | ✅ |
| 52 | NegotiationHeaderCancelDate | CANCEL_DATE | — | — |
| 53 | NegotiationHeaderCarrierId | CARRIER_ID | — | — |
| 54 | NegotiationHeaderCloseBiddingDate | CLOSE_BIDDING_DATE | — | — |
| 55 | NegotiationHeaderCloseDateType | CLOSE_DATE_TYPE | — | — |
| 56 | NegotiationHeaderCompleteFlag | COMPLETE_FLAG | — | — |
| 57 | NegotiationHeaderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 58 | NegotiationHeaderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 59 | NegotiationHeaderContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 60 | NegotiationHeaderContractTemplateId | CONTRACT_TEMPLATE_ID | — | — |
| 61 | NegotiationHeaderContractType | CONTRACT_TYPE | — | ✅ |
| 62 | NegotiationHeaderCreatedBy | CREATED_BY | — | ✅ |
| 63 | NegotiationHeaderCreationDate | CREATION_DATE | — | ✅ |
| 64 | NegotiationHeaderCreationDateOrigAmend | CREATION_DATE_ORIG_AMEND | — | — |
| 65 | NegotiationHeaderCurrencyCode | CURRENCY_CODE | — | ✅ |
| 66 | NegotiationHeaderDaysAfterOpenDate | DAYS_AFTER_OPEN_DATE | — | — |
| 67 | NegotiationHeaderDescription | DESCRIPTION | — | — |
| 68 | NegotiationHeaderDisplayBestPriceBlindFlag | DISPLAY_BEST_PRICE_BLIND_FLAG | — | — |
| 69 | NegotiationHeaderDisplayBestPriceDspFlag | DISPLAY_BEST_PRICE_DSP_FLAG | — | ✅ |
| 70 | NegotiationHeaderDoctypeId | DOCTYPE_ID | — | ✅ |
| 71 | NegotiationHeaderDocumentNumber | DOCUMENT_NUMBER | — | ✅ |
| 72 | NegotiationHeaderDraftLocked | DRAFT_LOCKED | — | — |
| 73 | NegotiationHeaderDraftLockedDate | DRAFT_LOCKED_DATE | — | — |
| 74 | NegotiationHeaderDraftUnlockedDate | DRAFT_UNLOCKED_DATE | — | — |
| 75 | NegotiationHeaderEnforcePrevrndBidPriceFlag | ENFORCE_PREVRND_BID_PRICE_FLAG | — | — |
| 76 | NegotiationHeaderEventId | EVENT_ID | — | — |
| 77 | NegotiationHeaderEventTitle | EVENT_TITLE | — | — |
| 78 | NegotiationHeaderExtAttribute1 | EXT_ATTRIBUTE1 | — | — |
| 79 | NegotiationHeaderExtAttribute10 | EXT_ATTRIBUTE10 | — | — |
| 80 | NegotiationHeaderExtAttribute11 | EXT_ATTRIBUTE11 | — | — |
| 81 | NegotiationHeaderExtAttribute12 | EXT_ATTRIBUTE12 | — | — |
| 82 | NegotiationHeaderExtAttribute13 | EXT_ATTRIBUTE13 | — | — |
| 83 | NegotiationHeaderExtAttribute14 | EXT_ATTRIBUTE14 | — | — |
| 84 | NegotiationHeaderExtAttribute15 | EXT_ATTRIBUTE15 | — | — |
| 85 | NegotiationHeaderExtAttribute2 | EXT_ATTRIBUTE2 | — | — |
| 86 | NegotiationHeaderExtAttribute3 | EXT_ATTRIBUTE3 | — | — |
| 87 | NegotiationHeaderExtAttribute4 | EXT_ATTRIBUTE4 | — | — |
| 88 | NegotiationHeaderExtAttribute5 | EXT_ATTRIBUTE5 | — | — |
| 89 | NegotiationHeaderExtAttribute6 | EXT_ATTRIBUTE6 | — | — |
| 90 | NegotiationHeaderExtAttribute7 | EXT_ATTRIBUTE7 | — | — |
| 91 | NegotiationHeaderExtAttribute8 | EXT_ATTRIBUTE8 | — | — |
| 92 | NegotiationHeaderExtAttribute9 | EXT_ATTRIBUTE9 | — | — |
| 93 | NegotiationHeaderExtAttributeCategory | EXT_ATTRIBUTE_CATEGORY | — | — |
| 94 | NegotiationHeaderFirstLineCloseDate | FIRST_LINE_CLOSE_DATE | — | — |
| 95 | NegotiationHeaderFobCode | FOB_CODE | — | — |
| 96 | NegotiationHeaderFreightTermsCode | FREIGHT_TERMS_CODE | — | — |
| 97 | NegotiationHeaderFullQuantityBidCode | FULL_QUANTITY_BID_CODE | — | — |
| 98 | NegotiationHeaderGlobalTemplateFlag | GLOBAL_TEMPLATE_FLAG | — | — |
| 99 | NegotiationHeaderGroupEnabledFlag | GROUP_ENABLED_FLAG | — | — |
| 100 | NegotiationHeaderHasHdrAttrFlag | HAS_HDR_ATTR_FLAG | — | — |
| 101 | NegotiationHeaderHasItemsFlag | HAS_ITEMS_FLAG | — | ✅ |
| 102 | NegotiationHeaderHasPeForAllItems | HAS_PE_FOR_ALL_ITEMS | — | — |
| 103 | NegotiationHeaderHasPriceElements | HAS_PRICE_ELEMENTS | — | — |
| 104 | NegotiationHeaderHasScoringTeamsFlag | HAS_SCORING_TEAMS_FLAG | — | — |
| 105 | NegotiationHeaderHdrAttrDisplayScore | HDR_ATTR_DISPLAY_SCORE | — | ✅ |
| 106 | NegotiationHeaderHdrAttrEnableWeights | HDR_ATTR_ENABLE_WEIGHTS | — | ✅ |
| 107 | NegotiationHeaderHdrAttrMaximumScore | HDR_ATTR_MAXIMUM_SCORE | — | — |
| 108 | NegotiationHeaderHdrAttributeEnabledFlag | HDR_ATTRIBUTE_ENABLED_FLAG | — | — |
| 109 | NegotiationHeaderImportFileName | IMPORT_FILE_NAME | — | — |
| 110 | NegotiationHeaderIncludePdfInExternalPage | INCLUDE_PDF_IN_EXTERNAL_PAGE | — | — |
| 111 | NegotiationHeaderIntAttribute1 | INT_ATTRIBUTE1 | — | — |
| 112 | NegotiationHeaderIntAttribute10 | INT_ATTRIBUTE10 | — | — |
| 113 | NegotiationHeaderIntAttribute11 | INT_ATTRIBUTE11 | — | — |
| 114 | NegotiationHeaderIntAttribute12 | INT_ATTRIBUTE12 | — | — |
| 115 | NegotiationHeaderIntAttribute13 | INT_ATTRIBUTE13 | — | — |
| 116 | NegotiationHeaderIntAttribute14 | INT_ATTRIBUTE14 | — | — |
| 117 | NegotiationHeaderIntAttribute15 | INT_ATTRIBUTE15 | — | — |
| 118 | NegotiationHeaderIntAttribute2 | INT_ATTRIBUTE2 | — | — |
| 119 | NegotiationHeaderIntAttribute3 | INT_ATTRIBUTE3 | — | — |
| 120 | NegotiationHeaderIntAttribute4 | INT_ATTRIBUTE4 | — | — |
| 121 | NegotiationHeaderIntAttribute5 | INT_ATTRIBUTE5 | — | — |
| 122 | NegotiationHeaderIntAttribute6 | INT_ATTRIBUTE6 | — | — |
| 123 | NegotiationHeaderIntAttribute7 | INT_ATTRIBUTE7 | — | — |
| 124 | NegotiationHeaderIntAttribute8 | INT_ATTRIBUTE8 | — | — |
| 125 | NegotiationHeaderIntAttribute9 | INT_ATTRIBUTE9 | — | — |
| 126 | NegotiationHeaderIntAttributeCategory | INT_ATTRIBUTE_CATEGORY | — | — |
| 127 | NegotiationHeaderIsPaused | IS_PAUSED | — | — |
| 128 | NegotiationHeaderIsTemplateFlag | IS_TEMPLATE_FLAG | — | ✅ |
| 129 | NegotiationHeaderLanguageCode | LANGUAGE_CODE | — | — |
| 130 | NegotiationHeaderLargeNegEnabledFlag | LARGE_NEG_ENABLED_FLAG | — | — |
| 131 | NegotiationHeaderLastLineNumber | LAST_LINE_NUMBER | — | — |
| 132 | NegotiationHeaderLastPauseDate | LAST_PAUSE_DATE | — | — |
| 133 | NegotiationHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 134 | NegotiationHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 135 | NegotiationHeaderLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 136 | NegotiationHeaderLineAttributeEnabledFlag | LINE_ATTRIBUTE_ENABLED_FLAG | — | — |
| 137 | NegotiationHeaderLineMasEnabledFlag | LINE_MAS_ENABLED_FLAG | — | — |
| 138 | NegotiationHeaderLotEnabledFlag | LOT_ENABLED_FLAG | — | — |
| 139 | NegotiationHeaderMaxBidColorSequenceId | MAX_BID_COLOR_SEQUENCE_ID | — | — |
| 140 | NegotiationHeaderMaxDocumentLineNum | MAX_DOCUMENT_LINE_NUM | — | — |
| 141 | NegotiationHeaderMaxInternalLineNum | MAX_INTERNAL_LINE_NUM | — | — |
| 142 | NegotiationHeaderMaxRetainageNegotiableFlag | MAX_RETAINAGE_NEGOTIABLE_FLAG | — | — |
| 143 | NegotiationHeaderMinBidChangeType | MIN_BID_CHANGE_TYPE | — | — |
| 144 | NegotiationHeaderMinBidDecrement | MIN_BID_DECREMENT | — | — |
| 145 | NegotiationHeaderModeOfTransport | MODE_OF_TRANSPORT | — | ✅ |
| 146 | NegotiationHeaderNegApprovalDate | NEG_APPROVAL_DATE | — | ✅ |
| 147 | NegotiationHeaderNegApprovalEnabledFlag | NEG_APPROVAL_ENABLED_FLAG | — | ✅ |
| 148 | NegotiationHeaderNegTeamEnabledFlag | NEG_TEAM_ENABLED_FLAG | — | — |
| 149 | NegotiationHeaderNumberOfBids | NUMBER_OF_BIDS | — | — |
| 150 | NegotiationHeaderNumberOfExtensions | NUMBER_OF_EXTENSIONS | — | — |
| 151 | NegotiationHeaderNumberOfLines | NUMBER_OF_LINES | — | — |
| 152 | NegotiationHeaderNumberPriceDecimals | NUMBER_PRICE_DECIMALS | — | ✅ |
| 153 | NegotiationHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 154 | NegotiationHeaderOpenAuctionNowFlag | OPEN_AUCTION_NOW_FLAG | — | ✅ |
| 155 | NegotiationHeaderOpenBiddingDate | OPEN_BIDDING_DATE | — | — |
| 156 | NegotiationHeaderOriginalCloseBiddingDate | ORIGINAL_CLOSE_BIDDING_DATE | — | — |
| 157 | NegotiationHeaderOutcomeStatus | OUTCOME_STATUS | — | — |
| 158 | NegotiationHeaderPauseRemarks | PAUSE_REMARKS | — | — |
| 159 | NegotiationHeaderPaymentTermsId | PAYMENT_TERMS_ID | — | — |
| 160 | NegotiationHeaderPersonId | PERSON_ID | — | ✅ |
| 161 | NegotiationHeaderPfTypeAllowed | PF_TYPE_ALLOWED | — | — |
| 162 | NegotiationHeaderPoAgreedAmount | PO_AGREED_AMOUNT | — | ✅ |
| 163 | NegotiationHeaderPoEndDate | PO_END_DATE | — | ✅ |
| 164 | NegotiationHeaderPoMinRelAmount | PO_MIN_REL_AMOUNT | — | ✅ |
| 165 | NegotiationHeaderPoStartDate | PO_START_DATE | — | ✅ |
| 166 | NegotiationHeaderPoStyleId | PO_STYLE_ID | — | — |
| 167 | NegotiationHeaderPowerBiddingEnabledFlag | POWER_BIDDING_ENABLED_FLAG | — | — |
| 168 | NegotiationHeaderPrcBuId | PRC_BU_ID | — | ✅ |
| 169 | NegotiationHeaderPriceDrivenAuctionFlag | PRICE_DRIVEN_AUCTION_FLAG | — | — |
| 170 | NegotiationHeaderPriceElementEnabledFlag | PRICE_ELEMENT_ENABLED_FLAG | — | — |
| 171 | NegotiationHeaderPriceTiersIndicator | PRICE_TIERS_INDICATOR | — | ✅ |
| 172 | NegotiationHeaderProgramAppName | PROGRAM_APP_NAME | — | — |
| 173 | NegotiationHeaderProgramName | PROGRAM_NAME | — | — |
| 174 | NegotiationHeaderProgressPaymentType | PROGRESS_PAYMENT_TYPE | — | — |
| 175 | NegotiationHeaderProgressPymtNegotiableFlag | PROGRESS_PYMT_NEGOTIABLE_FLAG | — | — |
| 176 | NegotiationHeaderProjectId | PROJECT_ID | — | — |
| 177 | NegotiationHeaderProxyBiddingEnabledFlag | PROXY_BIDDING_ENABLED_FLAG | — | — |
| 178 | NegotiationHeaderPublishAuctionNowFlag | PUBLISH_AUCTION_NOW_FLAG | — | — |
| 179 | NegotiationHeaderPublishDate | PUBLISH_DATE | — | ✅ |
| 180 | NegotiationHeaderPublishDateOrigAmend | PUBLISH_DATE_ORIG_AMEND | — | ✅ |
| 181 | NegotiationHeaderPublishRatesToBiddersFlag | PUBLISH_RATES_TO_BIDDERS_FLAG | — | — |
| 182 | NegotiationHeaderQtyPriceTiersEnabledFlag | QTY_PRICE_TIERS_ENABLED_FLAG | — | — |
| 183 | NegotiationHeaderRankIndicator | RANK_INDICATOR | — | ✅ |
| 184 | NegotiationHeaderRateDate | RATE_DATE | — | — |
| 185 | NegotiationHeaderRateType | RATE_TYPE | — | — |
| 186 | NegotiationHeaderRecoupmentNegotiableFlag | RECOUPMENT_NEGOTIABLE_FLAG | — | — |
| 187 | NegotiationHeaderReminderDate | REMINDER_DATE | — | — |
| 188 | NegotiationHeaderReqBuId | REQ_BU_ID | — | ✅ |
| 189 | NegotiationHeaderRequestDate | REQUEST_DATE | — | — |
| 190 | NegotiationHeaderRequestId | REQUEST_ID | — | — |
| 191 | NegotiationHeaderRequestedBy | REQUESTED_BY | — | — |
| 192 | NegotiationHeaderRetainageNegotiableFlag | RETAINAGE_NEGOTIABLE_FLAG | — | — |
| 193 | NegotiationHeaderRfiLineEnabledFlag | RFI_LINE_ENABLED_FLAG | — | — |
| 194 | NegotiationHeaderScoringLockDate | SCORING_LOCK_DATE | — | — |
| 195 | NegotiationHeaderSealedActualUnlockDate | SEALED_ACTUAL_UNLOCK_DATE | — | — |
| 196 | NegotiationHeaderSealedActualUnsealDate | SEALED_ACTUAL_UNSEAL_DATE | — | — |
| 197 | NegotiationHeaderSealedAuctionStatus | SEALED_AUCTION_STATUS | — | ✅ |
| 198 | NegotiationHeaderServiceLevel | SERVICE_LEVEL | — | — |
| 199 | NegotiationHeaderShareAwardDecision | SHARE_AWARD_DECISION | — | — |
| 200 | NegotiationHeaderShowBidderNotes | SHOW_BIDDER_NOTES | — | — |
| 201 | NegotiationHeaderShowBidderScores | SHOW_BIDDER_SCORES | — | — |
| 202 | NegotiationHeaderSourceDocId | SOURCE_DOC_ID | — | — |
| 203 | NegotiationHeaderSourceDocLineMsg | SOURCE_DOC_LINE_MSG | — | — |
| 204 | NegotiationHeaderSourceDocMsg | SOURCE_DOC_MSG | — | — |
| 205 | NegotiationHeaderSourceDocMsgApp | SOURCE_DOC_MSG_APP | — | — |
| 206 | NegotiationHeaderSourceDocNumber | SOURCE_DOC_NUMBER | — | ✅ |
| 207 | NegotiationHeaderSourceReqsFlag | SOURCE_REQS_FLAG | — | — |
| 208 | NegotiationHeaderStaggeredClosingInterval | STAGGERED_CLOSING_INTERVAL | — | — |
| 209 | NegotiationHeaderStyleId | STYLE_ID | — | ✅ |
| 210 | NegotiationHeaderSupplierEnterablePymtFlag | SUPPLIER_ENTERABLE_PYMT_FLAG | — | — |
| 211 | NegotiationHeaderSupplierViewType | SUPPLIER_VIEW_TYPE | — | — |
| 212 | NegotiationHeaderSynopsis | SYNOPSIS | — | — |
| 213 | NegotiationHeaderTeamScoringEnabledFlag | TEAM_SCORING_ENABLED_FLAG | — | — |
| 214 | NegotiationHeaderTechnicalActualUnlockDate | TECHNICAL_ACTUAL_UNLOCK_DATE | — | — |
| 215 | NegotiationHeaderTechnicalActualUnsealDate | TECHNICAL_ACTUAL_UNSEAL_DATE | — | — |
| 216 | NegotiationHeaderTechnicalEvaluationStatus | TECHNICAL_EVALUATION_STATUS | — | — |
| 217 | NegotiationHeaderTechnicalLockStatus | TECHNICAL_LOCK_STATUS | — | — |
| 218 | NegotiationHeaderTemplateId | TEMPLATE_ID | — | — |
| 219 | NegotiationHeaderTemplateScope | TEMPLATE_SCOPE | — | — |
| 220 | NegotiationHeaderTemplateStatus | TEMPLATE_STATUS | — | — |
| 221 | NegotiationHeaderTwoPartFlag | TWO_PART_FLAG | — | ✅ |
| 222 | NegotiationHeaderTwostageEvalEnabledFlag | TWOSTAGE_EVAL_ENABLED_FLAG | — | ✅ |
| 223 | NegotiationHeaderVersionNum | VERSION_NUM | — | — |
| 224 | NegotiationHeaderViewByDate | VIEW_BY_DATE | — | ✅ |
| 225 | NegotiationHeaderWfApprovalItemKey | WF_APPROVAL_ITEM_KEY | — | — |
| 226 | NegotiationHeaderWfAwardApprovalItemKey | WF_AWARD_APPROVAL_ITEM_KEY | — | — |
| 227 | NegotiationHeaderWfItemKey | WF_ITEM_KEY | — | — |
| 228 | NegotiationHeaderWfPoncomplCurrentRound | WF_PONCOMPL_CURRENT_ROUND | — | — |
| 229 | NegotiationHeaderWfPoncomplItemKey | WF_PONCOMPL_ITEM_KEY | — | — |
| 230 | NegotiationHeaderWfRoleName | WF_ROLE_NAME | — | — |

### [[pon_bidding_parties|PON_BIDDING_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AuctionHeaderId | AUCTION_HEADER_ID | 🔑 | ✅ |
| 2 | ListId | LIST_ID | 🔑 | ✅ |
| 3 | NegBiddPartiesAccessType | ACCESS_TYPE | — | — |
| 4 | NegBiddPartiesAckNoteToAuctioneer | ACK_NOTE_TO_AUCTIONEER | — | — |
| 5 | NegBiddPartiesAckPartnerContactId | ACK_PARTNER_CONTACT_ID | — | — |
| 6 | NegBiddPartiesAcknowledgementTime | ACKNOWLEDGEMENT_TIME | — | — |
| 7 | NegBiddPartiesAdditionalContactEmail | ADDITIONAL_CONTACT_EMAIL | — | ✅ |
| 8 | NegBiddPartiesBidCurrencyCode | BID_CURRENCY_CODE | — | — |
| 9 | NegBiddPartiesCreatedBy | CREATED_BY | — | ✅ |
| 10 | NegBiddPartiesCreationDate | CREATION_DATE | — | ✅ |
| 11 | NegBiddPartiesLastAmendmentUpdate | LAST_AMENDMENT_UPDATE | — | — |
| 12 | NegBiddPartiesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | NegBiddPartiesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | NegBiddPartiesLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | NegBiddPartiesModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 16 | NegBiddPartiesNumberPriceDecimals | NUMBER_PRICE_DECIMALS | — | — |
| 17 | NegBiddPartiesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | NegBiddPartiesRate | RATE | — | — |
| 19 | NegBiddPartiesRateDsp | RATE_DSP | — | — |
| 20 | NegBiddPartiesRegistrationId | REGISTRATION_ID | — | ✅ |
| 21 | NegBiddPartiesRequestedSuppContactName | REQUESTED_SUPP_CONTACT_NAME | — | ✅ |
| 22 | NegBiddPartiesRequestedSupplierContactId | REQUESTED_SUPPLIER_CONTACT_ID | — | ✅ |
| 23 | NegBiddPartiesRequestedSupplierId | REQUESTED_SUPPLIER_ID | — | ✅ |
| 24 | NegBiddPartiesRequestedSupplierName | REQUESTED_SUPPLIER_NAME | — | ✅ |
| 25 | NegBiddPartiesRoundNumber | ROUND_NUMBER | — | — |
| 26 | NegBiddPartiesSuppAcknowledgement | SUPP_ACKNOWLEDGEMENT | — | ✅ |
| 27 | NegBiddPartiesTradingPartnerContactId | TRADING_PARTNER_CONTACT_ID | — | ✅ |
| 28 | NegBiddPartiesTradingPartnerId | TRADING_PARTNER_ID | — | ✅ |
| 29 | NegBiddPartiesVendorSiteId | VENDOR_SITE_ID | — | ✅ |
| 30 | NegBiddPartiesWfItemKey | WF_ITEM_KEY | — | — |
| 31 | NegBiddPartiesWfUserName | WF_USER_NAME | — | — |
| 32 | Sequence | SEQUENCE | 🔑 | ✅ |

### [[poz_contact_requests|POZ_CONTACT_REQUESTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContactRequestContactRequestId | CONTACT_REQUEST_ID | — | — |
| 2 | ContactRequestContactTitle | CONTACT_TITLE | — | — |
| 3 | ContactRequestFirstName | FIRST_NAME | — | — |
| 4 | ContactRequestLastName | LAST_NAME | — | — |
| 5 | ContactRequestMiddleName | MIDDLE_NAME | — | — |

### [[poz_supplier_registrations|POZ_SUPPLIER_REGISTRATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupplierRegisAddressLine1 | ADDRESS_LINE1 | — | — |
| 2 | SupplierRegisAddressLine2 | ADDRESS_LINE2 | — | — |
| 3 | SupplierRegisAddressLine3 | ADDRESS_LINE3 | — | — |
| 4 | SupplierRegisAddressLine4 | ADDRESS_LINE4 | — | — |
| 5 | SupplierRegisAddressNickname | ADDRESS_NICKNAME | — | — |
| 6 | SupplierRegisCity | CITY | — | — |
| 7 | SupplierRegisCorporateWebsite | CORPORATE_WEBSITE | — | — |
| 8 | SupplierRegisCountry | COUNTRY | — | — |
| 9 | SupplierRegisCounty | COUNTY | — | — |
| 10 | SupplierRegisCreatedBy | CREATED_BY | — | — |
| 11 | SupplierRegisCreationDate | CREATION_DATE | — | ✅ |
| 12 | SupplierRegisDunsNumber | DUNS_NUMBER | — | — |
| 13 | SupplierRegisLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | SupplierRegisLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | SupplierRegisLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | SupplierRegisNoteFromSupplier | NOTE_FROM_SUPPLIER | — | — |
| 17 | SupplierRegisNoteToSupplier | NOTE_TO_SUPPLIER | — | — |
| 18 | SupplierRegisObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | SupplierRegisPostalCode | POSTAL_CODE | — | — |
| 20 | SupplierRegisPrcBuId | PRC_BU_ID | — | — |
| 21 | SupplierRegisProvince | PROVINCE | — | — |
| 22 | SupplierRegisRegKey | REG_KEY | — | — |
| 23 | SupplierRegisRegistrationStatus | REGISTRATION_STATUS | — | — |
| 24 | SupplierRegisRegistrationType | REGISTRATION_TYPE | — | — |
| 25 | SupplierRegisRejectionCode | REJECTION_CODE | — | — |
| 26 | SupplierRegisRequestNumber | REQUEST_NUMBER | — | — |
| 27 | SupplierRegisState | STATE | — | — |
| 28 | SupplierRegisSupplierName | SUPPLIER_NAME | — | ✅ |
| 29 | SupplierRegisSupplierNumber | SUPPLIER_NUMBER | — | ✅ |
| 30 | SupplierRegisSupplierRegId | SUPPLIER_REG_ID | — | ✅ |
| 31 | SupplierRegisTaxRegCountryCode | TAX_REG_COUNTRY_CODE | — | — |
| 32 | SupplierRegisTaxRegType | TAX_REG_TYPE | — | — |
| 33 | SupplierRegisTaxRegistrationNumber | TAX_REGISTRATION_NUMBER | — | — |
| 34 | SupplierRegisTaxpayerId | TAXPAYER_ID | — | — |
| 35 | SupplierRegisUserRegId | USER_REG_ID | — | ✅ |
| 36 | SupplierRegisVendorId | VENDOR_ID | — | ✅ |
| 37 | SupplierRegisVendorPartyId | VENDOR_PARTY_ID | — | ✅ |

### [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupplierSiteObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | SupplierSiteVendorSiteId | VENDOR_SITE_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
