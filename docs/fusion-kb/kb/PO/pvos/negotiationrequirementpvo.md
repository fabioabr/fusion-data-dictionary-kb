---
id: DOC-PO-PVO-NegotiationRequirementPVO
doc_type: system-doc
title: "NegotiationRequirementPVO — PVO Purchasing"
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
  - NegotiationRequirementPVO
  - negotiationrequirementpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationRequirementPVO

## 📌 Visão Geral

Disponibiliza requisitos de negociações para consulta operacional, com critérios, seções e scores. Permite revisão detalhada das exigências estabelecidas em cada processo competitivo.

**Caminho:** `FscmTopModelAM.PrcPonPublicViewAM.NegotiationRequirementPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 301 | 4 | 1 | 62 | 21% |

---

## 🔗 Tabelas Relacionadas

- [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]] — 214 atributos (28 BICC)
- [[pon_requirements|PON_REQUIREMENTS]] — 45 atributos (1 PKs, 26 BICC)
- [[pon_requirement_scores|PON_REQUIREMENT_SCORES]] — 25 atributos (2 BICC)
- [[pon_requirement_sections|PON_REQUIREMENT_SECTIONS]] — 17 atributos (6 BICC)

---

## ⚙️ Atributos

### [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationHeaderAbstractDetails | ABSTRACT_DETAILS | — | — |
| 2 | NegotiationHeaderAbstractStatus | ABSTRACT_STATUS | — | — |
| 3 | NegotiationHeaderAdvanceNegotiableFlag | ADVANCE_NEGOTIABLE_FLAG | — | — |
| 4 | NegotiationHeaderAllowAlternateLines | ALLOW_ALTERNATE_LINES | — | — |
| 5 | NegotiationHeaderAllowOtherBidCurrencyFlag | ALLOW_OTHER_BID_CURRENCY_FLAG | — | — |
| 6 | NegotiationHeaderAlternateLinesEnabledFlag | ALTERNATE_LINES_ENABLED_FLAG | — | — |
| 7 | NegotiationHeaderAmendmentDescription | AMENDMENT_DESCRIPTION | — | — |
| 8 | NegotiationHeaderAmendmentNumber | AMENDMENT_NUMBER | — | — |
| 9 | NegotiationHeaderApprovalAmount | APPROVAL_AMOUNT | — | — |
| 10 | NegotiationHeaderAttributeLineNumber | ATTRIBUTE_LINE_NUMBER | — | — |
| 11 | NegotiationHeaderAttributesExist | ATTRIBUTES_EXIST | — | — |
| 12 | NegotiationHeaderAuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 13 | NegotiationHeaderAuctionHeaderIdOrigAmend | AUCTION_HEADER_ID_ORIG_AMEND | — | — |
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
| 32 | NegotiationHeaderAwardApprIdentificationKey | AWARD_APPR_IDENTIFICATION_KEY | — | — |
| 33 | NegotiationHeaderAwardApprovalDate | AWARD_APPROVAL_DATE | — | — |
| 34 | NegotiationHeaderAwardApprovalFlag | AWARD_APPROVAL_FLAG | — | — |
| 35 | NegotiationHeaderAwardApprovalNote | AWARD_APPROVAL_NOTE | — | — |
| 36 | NegotiationHeaderAwardApprovalStatus | AWARD_APPROVAL_STATUS | — | — |
| 37 | NegotiationHeaderAwardByDate | AWARD_BY_DATE | — | — |
| 38 | NegotiationHeaderAwardCompleteDate | AWARD_COMPLETE_DATE | — | ✅ |
| 39 | NegotiationHeaderAwardDate | AWARD_DATE | — | ✅ |
| 40 | NegotiationHeaderAwardMode | AWARD_MODE | — | — |
| 41 | NegotiationHeaderAwardStatus | AWARD_STATUS | — | ✅ |
| 42 | NegotiationHeaderBidDecrementMethod | BID_DECREMENT_METHOD | — | — |
| 43 | NegotiationHeaderBidFrequencyCode | BID_FREQUENCY_CODE | — | — |
| 44 | NegotiationHeaderBidFrequencyCodeDspFlag | BID_FREQUENCY_CODE_DSP_FLAG | — | — |
| 45 | NegotiationHeaderBidListType | BID_LIST_TYPE | — | — |
| 46 | NegotiationHeaderBidListTypeDspFlag | BID_LIST_TYPE_DSP_FLAG | — | — |
| 47 | NegotiationHeaderBidRanking | BID_RANKING | — | ✅ |
| 48 | NegotiationHeaderBidRevisionType | BID_REVISION_TYPE | — | — |
| 49 | NegotiationHeaderBidRevisionTypeDspFlag | BID_REVISION_TYPE_DSP_FLAG | — | — |
| 50 | NegotiationHeaderBidScopeCode | BID_SCOPE_CODE | — | — |
| 51 | NegotiationHeaderBidScopeCodeDspFlag | BID_SCOPE_CODE_DSP_FLAG | — | — |
| 52 | NegotiationHeaderBidVisibilityCode | BID_VISIBILITY_CODE | — | ✅ |
| 53 | NegotiationHeaderBuyerTransportEnabledFlag | BUYER_TRANSPORT_ENABLED_FLAG | — | — |
| 54 | NegotiationHeaderBuyerTransportFlag | BUYER_TRANSPORT_FLAG | — | ✅ |
| 55 | NegotiationHeaderCancelDate | CANCEL_DATE | — | — |
| 56 | NegotiationHeaderCarrierId | CARRIER_ID | — | — |
| 57 | NegotiationHeaderCloseBiddingDate | CLOSE_BIDDING_DATE | — | ✅ |
| 58 | NegotiationHeaderCloseDateType | CLOSE_DATE_TYPE | — | — |
| 59 | NegotiationHeaderCompleteFlag | COMPLETE_FLAG | — | — |
| 60 | NegotiationHeaderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 61 | NegotiationHeaderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 62 | NegotiationHeaderContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 63 | NegotiationHeaderContractTemplateId | CONTRACT_TEMPLATE_ID | — | — |
| 64 | NegotiationHeaderContractType | CONTRACT_TYPE | — | — |
| 65 | NegotiationHeaderCreatedBy | CREATED_BY | — | — |
| 66 | NegotiationHeaderCreationDate | CREATION_DATE | — | — |
| 67 | NegotiationHeaderCreationDateOrigAmend | CREATION_DATE_ORIG_AMEND | — | — |
| 68 | NegotiationHeaderCurrencyCode | CURRENCY_CODE | — | ✅ |
| 69 | NegotiationHeaderDaysAfterOpenDate | DAYS_AFTER_OPEN_DATE | — | — |
| 70 | NegotiationHeaderDescription | DESCRIPTION | — | — |
| 71 | NegotiationHeaderDisplayBestPriceBlindFlag | DISPLAY_BEST_PRICE_BLIND_FLAG | — | — |
| 72 | NegotiationHeaderDisplayBestPriceDspFlag | DISPLAY_BEST_PRICE_DSP_FLAG | — | — |
| 73 | NegotiationHeaderDoctypeId | DOCTYPE_ID | — | — |
| 74 | NegotiationHeaderDocumentNumber | DOCUMENT_NUMBER | — | ✅ |
| 75 | NegotiationHeaderDraftLocked | DRAFT_LOCKED | — | — |
| 76 | NegotiationHeaderDraftLockedByPersonId | DRAFT_LOCKED_BY_PERSON_ID | — | — |
| 77 | NegotiationHeaderDraftLockedDate | DRAFT_LOCKED_DATE | — | — |
| 78 | NegotiationHeaderDraftUnlockedByPersonId | DRAFT_UNLOCKED_BY_PERSON_ID | — | — |
| 79 | NegotiationHeaderDraftUnlockedDate | DRAFT_UNLOCKED_DATE | — | — |
| 80 | NegotiationHeaderEnforcePrevrndBidPriceFlag | ENFORCE_PREVRND_BID_PRICE_FLAG | — | — |
| 81 | NegotiationHeaderEventId | EVENT_ID | — | — |
| 82 | NegotiationHeaderEventTitle | EVENT_TITLE | — | — |
| 83 | NegotiationHeaderExternalPoCreationStatus | EXTERNAL_PO_CREATION_STATUS | — | — |
| 84 | NegotiationHeaderFirstLineCloseDate | FIRST_LINE_CLOSE_DATE | — | — |
| 85 | NegotiationHeaderFobCode | FOB_CODE | — | — |
| 86 | NegotiationHeaderFreightTermsCode | FREIGHT_TERMS_CODE | — | — |
| 87 | NegotiationHeaderFullQuantityBidCode | FULL_QUANTITY_BID_CODE | — | — |
| 88 | NegotiationHeaderGlobalTemplateFlag | GLOBAL_TEMPLATE_FLAG | — | — |
| 89 | NegotiationHeaderGroupEnabledFlag | GROUP_ENABLED_FLAG | — | — |
| 90 | NegotiationHeaderHasHdrAttrFlag | HAS_HDR_ATTR_FLAG | — | — |
| 91 | NegotiationHeaderHasItemsFlag | HAS_ITEMS_FLAG | — | — |
| 92 | NegotiationHeaderHasPeForAllItems | HAS_PE_FOR_ALL_ITEMS | — | — |
| 93 | NegotiationHeaderHasPriceElements | HAS_PRICE_ELEMENTS | — | — |
| 94 | NegotiationHeaderHasScoringTeamsFlag | HAS_SCORING_TEAMS_FLAG | — | — |
| 95 | NegotiationHeaderHdrAttrDisplayScore | HDR_ATTR_DISPLAY_SCORE | — | ✅ |
| 96 | NegotiationHeaderHdrAttrEnableWeights | HDR_ATTR_ENABLE_WEIGHTS | — | ✅ |
| 97 | NegotiationHeaderHdrAttrMaximumScore | HDR_ATTR_MAXIMUM_SCORE | — | — |
| 98 | NegotiationHeaderHdrAttributeEnabledFlag | HDR_ATTRIBUTE_ENABLED_FLAG | — | — |
| 99 | NegotiationHeaderImportFileName | IMPORT_FILE_NAME | — | — |
| 100 | NegotiationHeaderIncludePdfInExternalPage | INCLUDE_PDF_IN_EXTERNAL_PAGE | — | — |
| 101 | NegotiationHeaderIsPaused | IS_PAUSED | — | — |
| 102 | NegotiationHeaderIsTemplateFlag | IS_TEMPLATE_FLAG | — | — |
| 103 | NegotiationHeaderLanguageCode | LANGUAGE_CODE | — | — |
| 104 | NegotiationHeaderLargeNegEnabledFlag | LARGE_NEG_ENABLED_FLAG | — | — |
| 105 | NegotiationHeaderLastLineNumber | LAST_LINE_NUMBER | — | — |
| 106 | NegotiationHeaderLastPauseDate | LAST_PAUSE_DATE | — | — |
| 107 | NegotiationHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 108 | NegotiationHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 109 | NegotiationHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 110 | NegotiationHeaderLineAttributeEnabledFlag | LINE_ATTRIBUTE_ENABLED_FLAG | — | — |
| 111 | NegotiationHeaderLineMasEnabledFlag | LINE_MAS_ENABLED_FLAG | — | — |
| 112 | NegotiationHeaderLotEnabledFlag | LOT_ENABLED_FLAG | — | — |
| 113 | NegotiationHeaderMaxBidColorSequenceId | MAX_BID_COLOR_SEQUENCE_ID | — | — |
| 114 | NegotiationHeaderMaxDocumentLineNum | MAX_DOCUMENT_LINE_NUM | — | — |
| 115 | NegotiationHeaderMaxInternalLineNum | MAX_INTERNAL_LINE_NUM | — | — |
| 116 | NegotiationHeaderMaxRetainageNegotiableFlag | MAX_RETAINAGE_NEGOTIABLE_FLAG | — | — |
| 117 | NegotiationHeaderMinBidChangeType | MIN_BID_CHANGE_TYPE | — | — |
| 118 | NegotiationHeaderMinBidDecrement | MIN_BID_DECREMENT | — | — |
| 119 | NegotiationHeaderModeOfTransport | MODE_OF_TRANSPORT | — | — |
| 120 | NegotiationHeaderNegApprIdentificationKey | NEG_APPR_IDENTIFICATION_KEY | — | — |
| 121 | NegotiationHeaderNegApprovalDate | NEG_APPROVAL_DATE | — | — |
| 122 | NegotiationHeaderNegApprovalEnabledFlag | NEG_APPROVAL_ENABLED_FLAG | — | — |
| 123 | NegotiationHeaderNegApprovalNote | NEG_APPROVAL_NOTE | — | — |
| 124 | NegotiationHeaderNegApprovalStatus | NEG_APPROVAL_STATUS | — | — |
| 125 | NegotiationHeaderNegTeamEnabledFlag | NEG_TEAM_ENABLED_FLAG | — | — |
| 126 | NegotiationHeaderNumberOfBids | NUMBER_OF_BIDS | — | — |
| 127 | NegotiationHeaderNumberOfExtensions | NUMBER_OF_EXTENSIONS | — | — |
| 128 | NegotiationHeaderNumberOfLines | NUMBER_OF_LINES | — | — |
| 129 | NegotiationHeaderNumberPriceDecimals | NUMBER_PRICE_DECIMALS | — | ✅ |
| 130 | NegotiationHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 131 | NegotiationHeaderOpenAuctionNowFlag | OPEN_AUCTION_NOW_FLAG | — | ✅ |
| 132 | NegotiationHeaderOpenBiddingDate | OPEN_BIDDING_DATE | — | ✅ |
| 133 | NegotiationHeaderOriginalCloseBiddingDate | ORIGINAL_CLOSE_BIDDING_DATE | — | — |
| 134 | NegotiationHeaderOutcomeStatus | OUTCOME_STATUS | — | — |
| 135 | NegotiationHeaderPauseRemarks | PAUSE_REMARKS | — | — |
| 136 | NegotiationHeaderPaymentTermsId | PAYMENT_TERMS_ID | — | — |
| 137 | NegotiationHeaderPersonId | PERSON_ID | — | — |
| 138 | NegotiationHeaderPfTypeAllowed | PF_TYPE_ALLOWED | — | — |
| 139 | NegotiationHeaderPoAgreedAmount | PO_AGREED_AMOUNT | — | ✅ |
| 140 | NegotiationHeaderPoCreationProcess | PO_CREATION_PROCESS | — | — |
| 141 | NegotiationHeaderPoEndDate | PO_END_DATE | — | ✅ |
| 142 | NegotiationHeaderPoMinRelAmount | PO_MIN_REL_AMOUNT | — | ✅ |
| 143 | NegotiationHeaderPoStartDate | PO_START_DATE | — | ✅ |
| 144 | NegotiationHeaderPoStyleId | PO_STYLE_ID | — | — |
| 145 | NegotiationHeaderPowerBiddingEnabledFlag | POWER_BIDDING_ENABLED_FLAG | — | — |
| 146 | NegotiationHeaderPrcBuId | PRC_BU_ID | — | — |
| 147 | NegotiationHeaderPriceDrivenAuctionFlag | PRICE_DRIVEN_AUCTION_FLAG | — | — |
| 148 | NegotiationHeaderPriceElementEnabledFlag | PRICE_ELEMENT_ENABLED_FLAG | — | — |
| 149 | NegotiationHeaderPriceTiersIndicator | PRICE_TIERS_INDICATOR | — | ✅ |
| 150 | NegotiationHeaderProgramAppName | PROGRAM_APP_NAME | — | — |
| 151 | NegotiationHeaderProgramName | PROGRAM_NAME | — | — |
| 152 | NegotiationHeaderProgressPaymentType | PROGRESS_PAYMENT_TYPE | — | — |
| 153 | NegotiationHeaderProgressPymtNegotiableFlag | PROGRESS_PYMT_NEGOTIABLE_FLAG | — | — |
| 154 | NegotiationHeaderProjectId | PROJECT_ID | — | — |
| 155 | NegotiationHeaderProjectsEnabledFlag | PROJECTS_ENABLED_FLAG | — | — |
| 156 | NegotiationHeaderProxyBiddingEnabledFlag | PROXY_BIDDING_ENABLED_FLAG | — | — |
| 157 | NegotiationHeaderPublishAuctionNowFlag | PUBLISH_AUCTION_NOW_FLAG | — | — |
| 158 | NegotiationHeaderPublishDate | PUBLISH_DATE | — | ✅ |
| 159 | NegotiationHeaderPublishDateOrigAmend | PUBLISH_DATE_ORIG_AMEND | — | — |
| 160 | NegotiationHeaderPublishRatesToBiddersFlag | PUBLISH_RATES_TO_BIDDERS_FLAG | — | — |
| 161 | NegotiationHeaderQtyPriceTiersEnabledFlag | QTY_PRICE_TIERS_ENABLED_FLAG | — | — |
| 162 | NegotiationHeaderRankIndicator | RANK_INDICATOR | — | ✅ |
| 163 | NegotiationHeaderRateDate | RATE_DATE | — | — |
| 164 | NegotiationHeaderRateType | RATE_TYPE | — | — |
| 165 | NegotiationHeaderRecoupmentNegotiableFlag | RECOUPMENT_NEGOTIABLE_FLAG | — | — |
| 166 | NegotiationHeaderReminderDate | REMINDER_DATE | — | — |
| 167 | NegotiationHeaderReqBuId | REQ_BU_ID | — | — |
| 168 | NegotiationHeaderRequestDate | REQUEST_DATE | — | — |
| 169 | NegotiationHeaderRequestId | REQUEST_ID | — | — |
| 170 | NegotiationHeaderRequestedBy | REQUESTED_BY | — | — |
| 171 | NegotiationHeaderRetainageNegotiableFlag | RETAINAGE_NEGOTIABLE_FLAG | — | — |
| 172 | NegotiationHeaderRfiLineEnabledFlag | RFI_LINE_ENABLED_FLAG | — | — |
| 173 | NegotiationHeaderScoringLockDate | SCORING_LOCK_DATE | — | — |
| 174 | NegotiationHeaderScoringLockPersonId | SCORING_LOCK_PERSON_ID | — | — |
| 175 | NegotiationHeaderSealedActualUnlockDate | SEALED_ACTUAL_UNLOCK_DATE | — | — |
| 176 | NegotiationHeaderSealedActualUnsealDate | SEALED_ACTUAL_UNSEAL_DATE | — | — |
| 177 | NegotiationHeaderSealedAuctionStatus | SEALED_AUCTION_STATUS | — | — |
| 178 | NegotiationHeaderSealedUnlockPersonId | SEALED_UNLOCK_PERSON_ID | — | — |
| 179 | NegotiationHeaderSealedUnsealPersonId | SEALED_UNSEAL_PERSON_ID | — | — |
| 180 | NegotiationHeaderServiceLevel | SERVICE_LEVEL | — | — |
| 181 | NegotiationHeaderShareAwardDecision | SHARE_AWARD_DECISION | — | — |
| 182 | NegotiationHeaderShowBidderNotes | SHOW_BIDDER_NOTES | — | — |
| 183 | NegotiationHeaderShowBidderScores | SHOW_BIDDER_SCORES | — | — |
| 184 | NegotiationHeaderSourceDocId | SOURCE_DOC_ID | — | — |
| 185 | NegotiationHeaderSourceDocLineMsg | SOURCE_DOC_LINE_MSG | — | — |
| 186 | NegotiationHeaderSourceDocMsg | SOURCE_DOC_MSG | — | — |
| 187 | NegotiationHeaderSourceDocMsgApp | SOURCE_DOC_MSG_APP | — | — |
| 188 | NegotiationHeaderSourceDocNumber | SOURCE_DOC_NUMBER | — | ✅ |
| 189 | NegotiationHeaderSourceReqsFlag | SOURCE_REQS_FLAG | — | — |
| 190 | NegotiationHeaderStaggeredClosingInterval | STAGGERED_CLOSING_INTERVAL | — | — |
| 191 | NegotiationHeaderStyleId | STYLE_ID | — | — |
| 192 | NegotiationHeaderSupplierEnterablePymtFlag | SUPPLIER_ENTERABLE_PYMT_FLAG | — | — |
| 193 | NegotiationHeaderSupplierViewType | SUPPLIER_VIEW_TYPE | — | — |
| 194 | NegotiationHeaderSynopsis | SYNOPSIS | — | — |
| 195 | NegotiationHeaderTeamScoringEnabledFlag | TEAM_SCORING_ENABLED_FLAG | — | — |
| 196 | NegotiationHeaderTechnicalActualUnlockDate | TECHNICAL_ACTUAL_UNLOCK_DATE | — | — |
| 197 | NegotiationHeaderTechnicalActualUnsealDate | TECHNICAL_ACTUAL_UNSEAL_DATE | — | — |
| 198 | NegotiationHeaderTechnicalEvaluationStatus | TECHNICAL_EVALUATION_STATUS | — | — |
| 199 | NegotiationHeaderTechnicalLockStatus | TECHNICAL_LOCK_STATUS | — | — |
| 200 | NegotiationHeaderTechnicalUnlockPersonId | TECHNICAL_UNLOCK_PERSON_ID | — | — |
| 201 | NegotiationHeaderTechnicalUnsealPersonId | TECHNICAL_UNSEAL_PERSON_ID | — | — |
| 202 | NegotiationHeaderTemplateId | TEMPLATE_ID | — | — |
| 203 | NegotiationHeaderTemplateScope | TEMPLATE_SCOPE | — | — |
| 204 | NegotiationHeaderTemplateStatus | TEMPLATE_STATUS | — | — |
| 205 | NegotiationHeaderTwoPartFlag | TWO_PART_FLAG | — | — |
| 206 | NegotiationHeaderTwostageEvalEnabledFlag | TWOSTAGE_EVAL_ENABLED_FLAG | — | — |
| 207 | NegotiationHeaderVersionNum | VERSION_NUM | — | — |
| 208 | NegotiationHeaderViewByDate | VIEW_BY_DATE | — | ✅ |
| 209 | NegotiationHeaderWfApprovalItemKey | WF_APPROVAL_ITEM_KEY | — | — |
| 210 | NegotiationHeaderWfAwardApprovalItemKey | WF_AWARD_APPROVAL_ITEM_KEY | — | — |
| 211 | NegotiationHeaderWfItemKey | WF_ITEM_KEY | — | — |
| 212 | NegotiationHeaderWfPoncomplCurrentRound | WF_PONCOMPL_CURRENT_ROUND | — | — |
| 213 | NegotiationHeaderWfPoncomplItemKey | WF_PONCOMPL_ITEM_KEY | — | — |
| 214 | NegotiationHeaderWfRoleName | WF_ROLE_NAME | — | — |

### [[pon_requirements|PON_REQUIREMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationRequirementAbsoluteSectionSequence | ABSOLUTE_SECTION_SEQUENCE | — | ✅ |
| 2 | NegotiationRequirementAllowAttachmentCode | ALLOW_ATTACHMENT_CODE | — | ✅ |
| 3 | NegotiationRequirementAllowComments | ALLOW_COMMENTS | — | ✅ |
| 4 | NegotiationRequirementAuctionHeaderId | AUCTION_HEADER_ID | — | — |
| 5 | NegotiationRequirementCategoryCode | CATEGORY_CODE | — | — |
| 6 | NegotiationRequirementCreatedBy | CREATED_BY | — | ✅ |
| 7 | NegotiationRequirementCreationDate | CREATION_DATE | — | ✅ |
| 8 | NegotiationRequirementDatatype | DATATYPE | — | ✅ |
| 9 | NegotiationRequirementDateValue | DATE_VALUE | — | ✅ |
| 10 | NegotiationRequirementDatetimeValue | DATETIME_VALUE | — | ✅ |
| 11 | NegotiationRequirementDispSeqNumber | DISP_SEQ_NUMBER | — | — |
| 12 | NegotiationRequirementDisplayTargetFlag | DISPLAY_TARGET_FLAG | — | ✅ |
| 13 | NegotiationRequirementHint | HINT | — | ✅ |
| 14 | NegotiationRequirementIsQuestionBranch | IS_QUESTION_BRANCH | — | — |
| 15 | NegotiationRequirementKnockoutScore | KNOCKOUT_SCORE | — | ✅ |
| 16 | NegotiationRequirementLastAmendmentUpdate | LAST_AMENDMENT_UPDATE | — | — |
| 17 | NegotiationRequirementLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | NegotiationRequirementLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | NegotiationRequirementLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | NegotiationRequirementMaxScore | MAX_SCORE | — | ✅ |
| 21 | NegotiationRequirementModifiedDate | MODIFIED_DATE | — | — |
| 22 | NegotiationRequirementModifiedFlag | MODIFIED_FLAG | — | — |
| 23 | NegotiationRequirementNumberValue | NUMBER_VALUE | — | ✅ |
| 24 | NegotiationRequirementObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 25 | NegotiationRequirementParentLevel | PARENT_LEVEL | — | — |
| 26 | NegotiationRequirementParentRequirementId | PARENT_REQUIREMENT_ID | — | — |
| 27 | NegotiationRequirementPreviousRequirementId | PREVIOUS_REQUIREMENT_ID | — | — |
| 28 | NegotiationRequirementQuestionId | QUESTION_ID | — | ✅ |
| 29 | NegotiationRequirementReqDisplayNumber | REQ_DISPLAY_NUMBER | — | ✅ |
| 30 | NegotiationRequirementRequirementName | REQUIREMENT_NAME | — | ✅ |
| 31 | NegotiationRequirementRequirementText | REQUIREMENT_TEXT | — | ✅ |
| 32 | NegotiationRequirementRequirementTreeLevel | REQUIREMENT_TREE_LEVEL | — | — |
| 33 | NegotiationRequirementRequirementType | REQUIREMENT_TYPE | — | ✅ |
| 34 | NegotiationRequirementResponseType | RESPONSE_TYPE | — | ✅ |
| 35 | NegotiationRequirementRevisionNumber | REVISION_NUMBER | — | ✅ |
| 36 | NegotiationRequirementRootRequirementId | ROOT_REQUIREMENT_ID | — | — |
| 37 | NegotiationRequirementScoreId | SCORE_ID | — | — |
| 38 | NegotiationRequirementScoringMethod | SCORING_METHOD | — | ✅ |
| 39 | NegotiationRequirementScoringType | SCORING_TYPE | — | — |
| 40 | NegotiationRequirementSectionId | SECTION_ID | — | — |
| 41 | NegotiationRequirementSequenceNumber | SEQUENCE_NUMBER | — | — |
| 42 | NegotiationRequirementSupplierLevel | SUPPLIER_LEVEL | — | ✅ |
| 43 | NegotiationRequirementTextValue | TEXT_VALUE | — | ✅ |
| 44 | NegotiationRequirementWeight | WEIGHT | — | ✅ |
| 45 | RequirementId | REQUIREMENT_ID | 🔑 | ✅ |

### [[pon_requirement_scores|PON_REQUIREMENT_SCORES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ParentRequirementScoreAccResponseId | ACC_RESPONSE_ID | — | — |
| 2 | ParentRequirementScoreAllowAttachmentCode | ALLOW_ATTACHMENT_CODE | — | — |
| 3 | ParentRequirementScoreAuctionHeaderId | AUCTION_HEADER_ID | — | — |
| 4 | ParentRequirementScoreCreatedBy | CREATED_BY | — | — |
| 5 | ParentRequirementScoreCreationDate | CREATION_DATE | — | — |
| 6 | ParentRequirementScoreDateFromRange | DATE_FROM_RANGE | — | — |
| 7 | ParentRequirementScoreDateToRange | DATE_TO_RANGE | — | — |
| 8 | ParentRequirementScoreDatetimeFromRange | DATETIME_FROM_RANGE | — | — |
| 9 | ParentRequirementScoreDatetimeToRange | DATETIME_TO_RANGE | — | — |
| 10 | ParentRequirementScoreDispSeqNumber | DISP_SEQ_NUMBER | — | ✅ |
| 11 | ParentRequirementScoreIsDefaultScoreRow | IS_DEFAULT_SCORE_ROW | — | — |
| 12 | ParentRequirementScoreLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | ParentRequirementScoreLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | ParentRequirementScoreLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | ParentRequirementScoreNumberFromRange | NUMBER_FROM_RANGE | — | — |
| 16 | ParentRequirementScoreNumberToRange | NUMBER_TO_RANGE | — | — |
| 17 | ParentRequirementScoreObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | ParentRequirementScorePreviousScoreId | PREVIOUS_SCORE_ID | — | — |
| 19 | ParentRequirementScoreRequirementId | REQUIREMENT_ID | — | — |
| 20 | ParentRequirementScoreScore | SCORE | — | — |
| 21 | ParentRequirementScoreScoreDisplayNumber | SCORE_DISPLAY_NUMBER | — | — |
| 22 | ParentRequirementScoreScoreId | SCORE_ID | — | — |
| 23 | ParentRequirementScoreScoreLevel | SCORE_LEVEL | — | — |
| 24 | ParentRequirementScoreTargetFlag | TARGET_FLAG | — | — |
| 25 | ParentRequirementScoreTextValue | TEXT_VALUE | — | — |

### [[pon_requirement_sections|PON_REQUIREMENT_SECTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationSectionAuctionHeaderId | AUCTION_HEADER_ID | — | — |
| 2 | NegotiationSectionCreatedBy | CREATED_BY | — | — |
| 3 | NegotiationSectionCreationDate | CREATION_DATE | — | — |
| 4 | NegotiationSectionDispSeqNumber | DISP_SEQ_NUMBER | — | ✅ |
| 5 | NegotiationSectionIsInternal | IS_INTERNAL | — | — |
| 6 | NegotiationSectionLastAmendmentUpdate | LAST_AMENDMENT_UPDATE | — | — |
| 7 | NegotiationSectionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | NegotiationSectionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | NegotiationSectionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | NegotiationSectionModifiedFlag | MODIFIED_FLAG | — | — |
| 11 | NegotiationSectionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | NegotiationSectionPreviousSectionId | PREVIOUS_SECTION_ID | — | — |
| 13 | NegotiationSectionSectionDisplayNumber | SECTION_DISPLAY_NUMBER | — | ✅ |
| 14 | NegotiationSectionSectionId | SECTION_ID | — | ✅ |
| 15 | NegotiationSectionSectionLevel | SECTION_LEVEL | — | — |
| 16 | NegotiationSectionSectionName | SECTION_NAME | — | ✅ |
| 17 | NegotiationSectionTwoPartSectionType | TWO_PART_SECTION_TYPE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
