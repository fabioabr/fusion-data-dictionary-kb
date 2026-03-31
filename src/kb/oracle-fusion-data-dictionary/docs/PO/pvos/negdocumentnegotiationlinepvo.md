---
id: DOC-PO-PVO-NegDocumentNegotiationLinePVO
doc_type: system-doc
title: "NegDocumentNegotiationLinePVO — PVO Purchasing"
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
  - NegDocumentNegotiationLinePVO
  - negdocumentnegotiationlinepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegDocumentNegotiationLinePVO

## 📌 Visão Geral

Extrai linhas de negociação vinculadas a documentos de compra, mapeando itens cotados a linhas de pedido resultantes. Suporta rastreabilidade completa do processo de sourcing até a execução da compra.

**Caminho:** `FscmTopModelAM.PrcPonPublicViewAM.NegDocumentNegotiationLinePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 530 | 8 | 3 | 125 | 24% |

---

## 🔗 Tabelas Relacionadas

- [[egp_categories_vl|EGP_CATEGORIES_VL]] — 8 atributos (3 BICC)
- [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]] — 6 atributos (6 BICC)
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 13 atributos
- [[inv_units_of_measure_vl|INV_UNITS_OF_MEASURE_VL]] — 4 atributos
- [[pon_action_history|PON_ACTION_HISTORY]] — 7 atributos
- [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]] — 231 atributos (1 PKs, 68 BICC)
- [[pon_auction_item_prices_all|PON_AUCTION_ITEM_PRICES_ALL]] — 155 atributos (2 PKs, 47 BICC)
- [[po_system_parameters_all|PO_SYSTEM_PARAMETERS_ALL]] — 106 atributos (1 BICC)

---

## ⚙️ Atributos

### [[egp_categories_vl|EGP_CATEGORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryCategoryId | CATEGORY_ID | — | ✅ |
| 2 | CategoryCategoryName | CATEGORY_NAME | — | ✅ |
| 3 | CategoryDescription | DESCRIPTION | — | ✅ |
| 4 | CategoryEnabledFlag | ENABLED_FLAG | — | — |
| 5 | CategoryJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 6 | CategoryJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 7 | CategoryStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 8 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |

### [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 2 | ItemInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | ✅ |
| 3 | ItemItemNumber | ITEM_NUMBER | — | ✅ |
| 4 | ItemItemType | ITEM_TYPE | — | ✅ |
| 5 | ItemOrganizationId | ORGANIZATION_ID | — | ✅ |
| 6 | ItemPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |

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
| 13 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[inv_units_of_measure_vl|INV_UNITS_OF_MEASURE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | — |
| 2 | ObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 3 | UnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 4 | UomCode | UOM_CODE | — | — |

### [[pon_action_history|PON_ACTION_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationActionHistoryActionType | ACTION_TYPE | — | — |
| 2 | NegotiationActionHistoryApprovalIdentificationKey | APPROVAL_IDENTIFICATION_KEY | — | — |
| 3 | NegotiationActionHistoryCreationDate | CREATION_DATE | — | — |
| 4 | NegotiationActionHistoryObjectId | OBJECT_ID | — | — |
| 5 | NegotiationActionHistoryObjectId2 | OBJECT_ID2 | — | — |
| 6 | NegotiationActionHistoryObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 7 | NegotiationActionHistorySequenceNum | SEQUENCE_NUM | — | — |

### [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationHeaderAbstractDetails | ABSTRACT_DETAILS | — | — |
| 2 | NegotiationHeaderAbstractStatus | ABSTRACT_STATUS | — | — |
| 3 | NegotiationHeaderAdvanceNegotiableFlag | ADVANCE_NEGOTIABLE_FLAG | — | — |
| 4 | NegotiationHeaderAllowOtherBidCurrencyFlag | ALLOW_OTHER_BID_CURRENCY_FLAG | — | — |
| 5 | NegotiationHeaderAmendmentDescription | AMENDMENT_DESCRIPTION | — | — |
| 6 | NegotiationHeaderAmendmentNumber | AMENDMENT_NUMBER | — | ✅ |
| 7 | NegotiationHeaderApprovalAmount | APPROVAL_AMOUNT | — | ✅ |
| 8 | NegotiationHeaderApprovalStatus | NEG_APPROVAL_STATUS | — | ✅ |
| 9 | NegotiationHeaderAttributeLineNumber | ATTRIBUTE_LINE_NUMBER | — | — |
| 10 | NegotiationHeaderAttributesExist | ATTRIBUTES_EXIST | — | — |
| 11 | NegotiationHeaderAuctionHeaderId | AUCTION_HEADER_ID | 🔑 | ✅ |
| 12 | NegotiationHeaderAuctionHeaderIdOrigAmend | AUCTION_HEADER_ID_ORIG_AMEND | — | ✅ |
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
| 31 | NegotiationHeaderAwardApprovalDate | AWARD_APPROVAL_DATE | — | ✅ |
| 32 | NegotiationHeaderAwardApprovalFlag | AWARD_APPROVAL_FLAG | — | ✅ |
| 33 | NegotiationHeaderAwardApprovalStatus | AWARD_APPROVAL_STATUS | — | ✅ |
| 34 | NegotiationHeaderAwardByDate | AWARD_BY_DATE | — | ✅ |
| 35 | NegotiationHeaderAwardCompleteDate | AWARD_COMPLETE_DATE | — | ✅ |
| 36 | NegotiationHeaderAwardDate | AWARD_DATE | — | — |
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
| 54 | NegotiationHeaderCloseBiddingDate | CLOSE_BIDDING_DATE | — | ✅ |
| 55 | NegotiationHeaderCloseDateType | CLOSE_DATE_TYPE | — | — |
| 56 | NegotiationHeaderCompleteFlag | COMPLETE_FLAG | — | — |
| 57 | NegotiationHeaderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 58 | NegotiationHeaderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 59 | NegotiationHeaderContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 60 | NegotiationHeaderContractTemplateId | CONTRACT_TEMPLATE_ID | — | — |
| 61 | NegotiationHeaderContractType | CONTRACT_TYPE | — | ✅ |
| 62 | NegotiationHeaderCreatedBy | CREATED_BY | — | — |
| 63 | NegotiationHeaderCreationDate | CREATION_DATE | — | ✅ |
| 64 | NegotiationHeaderCreationDateOrigAmend | CREATION_DATE_ORIG_AMEND | — | ✅ |
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
| 128 | NegotiationHeaderIsTemplateFlag | IS_TEMPLATE_FLAG | — | — |
| 129 | NegotiationHeaderLanguageCode | LANGUAGE_CODE | — | — |
| 130 | NegotiationHeaderLargeNegEnabledFlag | LARGE_NEG_ENABLED_FLAG | — | — |
| 131 | NegotiationHeaderLastLineNumber | LAST_LINE_NUMBER | — | — |
| 132 | NegotiationHeaderLastPauseDate | LAST_PAUSE_DATE | — | — |
| 133 | NegotiationHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 134 | NegotiationHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 135 | NegotiationHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
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
| 146 | NegotiationHeaderNegApprIdentificationKey | NEG_APPR_IDENTIFICATION_KEY | — | — |
| 147 | NegotiationHeaderNegApprovalDate | NEG_APPROVAL_DATE | — | ✅ |
| 148 | NegotiationHeaderNegApprovalEnabledFlag | NEG_APPROVAL_ENABLED_FLAG | — | ✅ |
| 149 | NegotiationHeaderNegTeamEnabledFlag | NEG_TEAM_ENABLED_FLAG | — | — |
| 150 | NegotiationHeaderNumberOfBids | NUMBER_OF_BIDS | — | — |
| 151 | NegotiationHeaderNumberOfExtensions | NUMBER_OF_EXTENSIONS | — | — |
| 152 | NegotiationHeaderNumberOfLines | NUMBER_OF_LINES | — | — |
| 153 | NegotiationHeaderNumberPriceDecimals | NUMBER_PRICE_DECIMALS | — | ✅ |
| 154 | NegotiationHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 155 | NegotiationHeaderOpenAuctionNowFlag | OPEN_AUCTION_NOW_FLAG | — | ✅ |
| 156 | NegotiationHeaderOpenBiddingDate | OPEN_BIDDING_DATE | — | ✅ |
| 157 | NegotiationHeaderOriginalCloseBiddingDate | ORIGINAL_CLOSE_BIDDING_DATE | — | ✅ |
| 158 | NegotiationHeaderOutcomeStatus | OUTCOME_STATUS | — | — |
| 159 | NegotiationHeaderPauseRemarks | PAUSE_REMARKS | — | — |
| 160 | NegotiationHeaderPaymentTermsId | PAYMENT_TERMS_ID | — | — |
| 161 | NegotiationHeaderPersonId | PERSON_ID | — | ✅ |
| 162 | NegotiationHeaderPfTypeAllowed | PF_TYPE_ALLOWED | — | — |
| 163 | NegotiationHeaderPoAgreedAmount | PO_AGREED_AMOUNT | — | ✅ |
| 164 | NegotiationHeaderPoEndDate | PO_END_DATE | — | ✅ |
| 165 | NegotiationHeaderPoMinRelAmount | PO_MIN_REL_AMOUNT | — | ✅ |
| 166 | NegotiationHeaderPoStartDate | PO_START_DATE | — | ✅ |
| 167 | NegotiationHeaderPoStyleId | PO_STYLE_ID | — | — |
| 168 | NegotiationHeaderPowerBiddingEnabledFlag | POWER_BIDDING_ENABLED_FLAG | — | — |
| 169 | NegotiationHeaderPrcBuId | PRC_BU_ID | — | ✅ |
| 170 | NegotiationHeaderPriceDrivenAuctionFlag | PRICE_DRIVEN_AUCTION_FLAG | — | — |
| 171 | NegotiationHeaderPriceElementEnabledFlag | PRICE_ELEMENT_ENABLED_FLAG | — | — |
| 172 | NegotiationHeaderPriceTiersIndicator | PRICE_TIERS_INDICATOR | — | ✅ |
| 173 | NegotiationHeaderProgramAppName | PROGRAM_APP_NAME | — | — |
| 174 | NegotiationHeaderProgramName | PROGRAM_NAME | — | — |
| 175 | NegotiationHeaderProgressPaymentType | PROGRESS_PAYMENT_TYPE | — | — |
| 176 | NegotiationHeaderProgressPymtNegotiableFlag | PROGRESS_PYMT_NEGOTIABLE_FLAG | — | — |
| 177 | NegotiationHeaderProjectId | PROJECT_ID | — | ✅ |
| 178 | NegotiationHeaderProxyBiddingEnabledFlag | PROXY_BIDDING_ENABLED_FLAG | — | — |
| 179 | NegotiationHeaderPublishAuctionNowFlag | PUBLISH_AUCTION_NOW_FLAG | — | — |
| 180 | NegotiationHeaderPublishDate | PUBLISH_DATE | — | ✅ |
| 181 | NegotiationHeaderPublishDateOrigAmend | PUBLISH_DATE_ORIG_AMEND | — | ✅ |
| 182 | NegotiationHeaderPublishRatesToBiddersFlag | PUBLISH_RATES_TO_BIDDERS_FLAG | — | — |
| 183 | NegotiationHeaderQtyPriceTiersEnabledFlag | QTY_PRICE_TIERS_ENABLED_FLAG | — | — |
| 184 | NegotiationHeaderRankIndicator | RANK_INDICATOR | — | ✅ |
| 185 | NegotiationHeaderRateDate | RATE_DATE | — | ✅ |
| 186 | NegotiationHeaderRateType | RATE_TYPE | — | ✅ |
| 187 | NegotiationHeaderRecoupmentNegotiableFlag | RECOUPMENT_NEGOTIABLE_FLAG | — | — |
| 188 | NegotiationHeaderReminderDate | REMINDER_DATE | — | — |
| 189 | NegotiationHeaderReqBuId | REQ_BU_ID | — | ✅ |
| 190 | NegotiationHeaderRequestDate | REQUEST_DATE | — | — |
| 191 | NegotiationHeaderRequestId | REQUEST_ID | — | — |
| 192 | NegotiationHeaderRequestedBy | REQUESTED_BY | — | — |
| 193 | NegotiationHeaderRetainageNegotiableFlag | RETAINAGE_NEGOTIABLE_FLAG | — | — |
| 194 | NegotiationHeaderRfiLineEnabledFlag | RFI_LINE_ENABLED_FLAG | — | — |
| 195 | NegotiationHeaderScoringLockDate | SCORING_LOCK_DATE | — | — |
| 196 | NegotiationHeaderSealedActualUnlockDate | SEALED_ACTUAL_UNLOCK_DATE | — | ✅ |
| 197 | NegotiationHeaderSealedActualUnsealDate | SEALED_ACTUAL_UNSEAL_DATE | — | — |
| 198 | NegotiationHeaderSealedAuctionStatus | SEALED_AUCTION_STATUS | — | ✅ |
| 199 | NegotiationHeaderServiceLevel | SERVICE_LEVEL | — | ✅ |
| 200 | NegotiationHeaderShareAwardDecision | SHARE_AWARD_DECISION | — | — |
| 201 | NegotiationHeaderShowBidderNotes | SHOW_BIDDER_NOTES | — | — |
| 202 | NegotiationHeaderShowBidderScores | SHOW_BIDDER_SCORES | — | — |
| 203 | NegotiationHeaderSourceDocId | SOURCE_DOC_ID | — | ✅ |
| 204 | NegotiationHeaderSourceDocLineMsg | SOURCE_DOC_LINE_MSG | — | — |
| 205 | NegotiationHeaderSourceDocMsg | SOURCE_DOC_MSG | — | — |
| 206 | NegotiationHeaderSourceDocMsgApp | SOURCE_DOC_MSG_APP | — | — |
| 207 | NegotiationHeaderSourceDocNumber | SOURCE_DOC_NUMBER | — | ✅ |
| 208 | NegotiationHeaderSourceReqsFlag | SOURCE_REQS_FLAG | — | — |
| 209 | NegotiationHeaderStaggeredClosingInterval | STAGGERED_CLOSING_INTERVAL | — | — |
| 210 | NegotiationHeaderStyleId | STYLE_ID | — | ✅ |
| 211 | NegotiationHeaderSupplierEnterablePymtFlag | SUPPLIER_ENTERABLE_PYMT_FLAG | — | — |
| 212 | NegotiationHeaderSupplierViewType | SUPPLIER_VIEW_TYPE | — | — |
| 213 | NegotiationHeaderSynopsis | SYNOPSIS | — | ✅ |
| 214 | NegotiationHeaderTeamScoringEnabledFlag | TEAM_SCORING_ENABLED_FLAG | — | — |
| 215 | NegotiationHeaderTechnicalActualUnlockDate | TECHNICAL_ACTUAL_UNLOCK_DATE | — | ✅ |
| 216 | NegotiationHeaderTechnicalActualUnsealDate | TECHNICAL_ACTUAL_UNSEAL_DATE | — | — |
| 217 | NegotiationHeaderTechnicalEvaluationStatus | TECHNICAL_EVALUATION_STATUS | — | — |
| 218 | NegotiationHeaderTechnicalLockStatus | TECHNICAL_LOCK_STATUS | — | ✅ |
| 219 | NegotiationHeaderTemplateId | TEMPLATE_ID | — | — |
| 220 | NegotiationHeaderTemplateScope | TEMPLATE_SCOPE | — | — |
| 221 | NegotiationHeaderTemplateStatus | TEMPLATE_STATUS | — | — |
| 222 | NegotiationHeaderTwoPartFlag | TWO_PART_FLAG | — | ✅ |
| 223 | NegotiationHeaderTwostageEvalEnabledFlag | TWOSTAGE_EVAL_ENABLED_FLAG | — | ✅ |
| 224 | NegotiationHeaderVersionNum | VERSION_NUM | — | — |
| 225 | NegotiationHeaderViewByDate | VIEW_BY_DATE | — | ✅ |
| 226 | NegotiationHeaderWfApprovalItemKey | WF_APPROVAL_ITEM_KEY | — | — |
| 227 | NegotiationHeaderWfAwardApprovalItemKey | WF_AWARD_APPROVAL_ITEM_KEY | — | — |
| 228 | NegotiationHeaderWfItemKey | WF_ITEM_KEY | — | — |
| 229 | NegotiationHeaderWfPoncomplCurrentRound | WF_PONCOMPL_CURRENT_ROUND | — | — |
| 230 | NegotiationHeaderWfPoncomplItemKey | WF_PONCOMPL_ITEM_KEY | — | — |
| 231 | NegotiationHeaderWfRoleName | WF_ROLE_NAME | — | — |

### [[pon_auction_item_prices_all|PON_AUCTION_ITEM_PRICES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AuctionHeaderId | AUCTION_HEADER_ID | 🔑 | ✅ |
| 2 | LineNumber | LINE_NUMBER | 🔑 | ✅ |
| 3 | NegotiationLineAllocationStatus | ALLOCATION_STATUS | — | — |
| 4 | NegotiationLineAllowAlternateLines | ALLOW_ALTERNATE_LINES | — | ✅ |
| 5 | NegotiationLineAwardMode | AWARD_MODE | — | — |
| 6 | NegotiationLineAwardStatus | AWARD_STATUS | — | ✅ |
| 7 | NegotiationLineAwardedQuantity | AWARDED_QUANTITY | — | — |
| 8 | NegotiationLineBestBidBidCurrencyCode | BEST_BID_BID_CURRENCY_CODE | — | — |
| 9 | NegotiationLineBestBidBidCurrencyPrice | BEST_BID_BID_CURRENCY_PRICE | — | — |
| 10 | NegotiationLineBestBidBidNumber | BEST_BID_BID_NUMBER | — | — |
| 11 | NegotiationLineBestBidBidPrice | BEST_BID_BID_PRICE | — | ✅ |
| 12 | NegotiationLineBestBidCurrencyCode | BEST_BID_CURRENCY_CODE | — | ✅ |
| 13 | NegotiationLineBestBidCurrencyPrice | BEST_BID_CURRENCY_PRICE | — | — |
| 14 | NegotiationLineBestBidFirstBidPrice | BEST_BID_FIRST_BID_PRICE | — | — |
| 15 | NegotiationLineBestBidNumber | BEST_BID_NUMBER | — | — |
| 16 | NegotiationLineBestBidPrice | BEST_BID_PRICE | — | ✅ |
| 17 | NegotiationLineBestBidPromisedDate | BEST_BID_PROMISED_DATE | — | — |
| 18 | NegotiationLineBestBidProxyLimitPrice | BEST_BID_PROXY_LIMIT_PRICE | — | — |
| 19 | NegotiationLineBestBidQuantity | BEST_BID_QUANTITY | — | — |
| 20 | NegotiationLineBestBidScore | BEST_BID_SCORE | — | — |
| 21 | NegotiationLineBidStartPrice | BID_START_PRICE | — | ✅ |
| 22 | NegotiationLineCategoryId | CATEGORY_ID | — | ✅ |
| 23 | NegotiationLineCloseBiddingDate | CLOSE_BIDDING_DATE | — | ✅ |
| 24 | NegotiationLineCreatedBy | CREATED_BY | — | ✅ |
| 25 | NegotiationLineCreationDate | CREATION_DATE | — | ✅ |
| 26 | NegotiationLineCurrentPrice | CURRENT_PRICE | — | ✅ |
| 27 | NegotiationLineDispLineNumber | DISP_LINE_NUMBER | — | ✅ |
| 28 | NegotiationLineDisplayTargetPriceFlag | DISPLAY_TARGET_PRICE_FLAG | — | ✅ |
| 29 | NegotiationLineDocumentDispLineNumber | DOCUMENT_DISP_LINE_NUMBER | — | ✅ |
| 30 | NegotiationLineGroupType | GROUP_TYPE | — | ✅ |
| 31 | NegotiationLineHasAttributesFlag | HAS_ATTRIBUTES_FLAG | — | — |
| 32 | NegotiationLineHasBuyerPfsFlag | HAS_BUYER_PFS_FLAG | — | — |
| 33 | NegotiationLineHasPriceElementsFlag | HAS_PRICE_ELEMENTS_FLAG | — | — |
| 34 | NegotiationLineHasQuantityTiers | HAS_QUANTITY_TIERS | — | — |
| 35 | NegotiationLineHasShipmentsFlag | HAS_SHIPMENTS_FLAG | — | — |
| 36 | NegotiationLineInvOrgId | INV_ORG_ID | — | ✅ |
| 37 | NegotiationLineItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 38 | NegotiationLineItemId | ITEM_ID | — | ✅ |
| 39 | NegotiationLineItemRevision | ITEM_REVISION | — | ✅ |
| 40 | NegotiationLineLastAmendmentUpdate | LAST_AMENDMENT_UPDATE | — | — |
| 41 | NegotiationLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 42 | NegotiationLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 43 | NegotiationLineLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 44 | NegotiationLineLineOriginationCode | LINE_ORIGINATION_CODE | — | ✅ |
| 45 | NegotiationLineLineTypeId | LINE_TYPE_ID | — | ✅ |
| 46 | NegotiationLineMaxSubLineSequenceNumber | MAX_SUB_LINE_SEQUENCE_NUMBER | — | — |
| 47 | NegotiationLineModifiedDate | MODIFIED_DATE | — | — |
| 48 | NegotiationLineModifiedFlag | MODIFIED_FLAG | — | — |
| 49 | NegotiationLineNeedByDate | NEED_BY_DATE | — | ✅ |
| 50 | NegotiationLineNoAward | NO_AWARD | — | — |
| 51 | NegotiationLineNoteToBidders | NOTE_TO_BIDDERS | — | ✅ |
| 52 | NegotiationLineNumberOfBids | NUMBER_OF_BIDS | — | — |
| 53 | NegotiationLineNumberOfExtensions | NUMBER_OF_EXTENSIONS | — | — |
| 54 | NegotiationLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 55 | NegotiationLineOrderTypeLookupCode | ORDER_TYPE_LOOKUP_CODE | — | ✅ |
| 56 | NegotiationLineParentLineNumber | PARENT_LINE_NUMBER | — | ✅ |
| 57 | NegotiationLinePoAgreedAmount | PO_AGREED_AMOUNT | — | ✅ |
| 58 | NegotiationLinePoMinRelAmount | PO_MIN_REL_AMOUNT | — | ✅ |
| 59 | NegotiationLinePrcBuId | PRC_BU_ID | — | ✅ |
| 60 | NegotiationLinePriceBreakNegFlag | PRICE_BREAK_NEG_FLAG | — | — |
| 61 | NegotiationLinePriceBreakType | PRICE_BREAK_TYPE | — | — |
| 62 | NegotiationLinePriceDisabledFlag | PRICE_DISABLED_FLAG | — | — |
| 63 | NegotiationLinePurchaseBasis | PURCHASE_BASIS | — | — |
| 64 | NegotiationLineQuantity | QUANTITY | — | ✅ |
| 65 | NegotiationLineQuantityDisabledFlag | QUANTITY_DISABLED_FLAG | — | — |
| 66 | NegotiationLineReqBuId | REQ_BU_ID | — | ✅ |
| 67 | NegotiationLineRequestedDeliveryDate | REQUESTED_DELIVERY_DATE | — | ✅ |
| 68 | NegotiationLineRequestedShipDate | REQUESTED_SHIP_DATE | — | ✅ |
| 69 | NegotiationLineRequisitionNumber | REQUISITION_NUMBER | — | ✅ |
| 70 | NegotiationLineShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 71 | NegotiationLineSourceDocId | SOURCE_DOC_ID | — | ✅ |
| 72 | NegotiationLineSourceDocNumber | SOURCE_DOC_NUMBER | — | ✅ |
| 73 | NegotiationLineSourceLineId | SOURCE_LINE_ID | — | ✅ |
| 74 | NegotiationLineSourceLineNumber | SOURCE_LINE_NUMBER | — | ✅ |
| 75 | NegotiationLineSubLineSequenceNumber | SUB_LINE_SEQUENCE_NUMBER | — | — |
| 76 | NegotiationLineTargetPrice | TARGET_PRICE | — | ✅ |
| 77 | NegotiationLineUnitDisplayTargetFlag | UNIT_DISPLAY_TARGET_FLAG | — | — |
| 78 | NegotiationLineUnitTargetPrice | UNIT_TARGET_PRICE | — | ✅ |
| 79 | NegotiationLineUomCode | UOM_CODE | — | ✅ |
| 80 | NegotiationParentLineAllocationStatus | ALLOCATION_STATUS | — | — |
| 81 | NegotiationParentLineAuctionHeaderId | AUCTION_HEADER_ID | — | — |
| 82 | NegotiationParentLineAwardMode | AWARD_MODE | — | — |
| 83 | NegotiationParentLineAwardStatus | AWARD_STATUS | — | — |
| 84 | NegotiationParentLineAwardedQuantity | AWARDED_QUANTITY | — | — |
| 85 | NegotiationParentLineBestBidBidCurrencyCode | BEST_BID_BID_CURRENCY_CODE | — | — |
| 86 | NegotiationParentLineBestBidBidCurrencyPrice | BEST_BID_BID_CURRENCY_PRICE | — | — |
| 87 | NegotiationParentLineBestBidBidNumber | BEST_BID_BID_NUMBER | — | — |
| 88 | NegotiationParentLineBestBidBidPrice | BEST_BID_BID_PRICE | — | — |
| 89 | NegotiationParentLineBestBidCurrencyCode | BEST_BID_CURRENCY_CODE | — | — |
| 90 | NegotiationParentLineBestBidCurrencyPrice | BEST_BID_CURRENCY_PRICE | — | — |
| 91 | NegotiationParentLineBestBidFirstBidPrice | BEST_BID_FIRST_BID_PRICE | — | — |
| 92 | NegotiationParentLineBestBidNumber | BEST_BID_NUMBER | — | — |
| 93 | NegotiationParentLineBestBidPrice | BEST_BID_PRICE | — | — |
| 94 | NegotiationParentLineBestBidPromisedDate | BEST_BID_PROMISED_DATE | — | — |
| 95 | NegotiationParentLineBestBidProxyLimitPrice | BEST_BID_PROXY_LIMIT_PRICE | — | — |
| 96 | NegotiationParentLineBestBidQuantity | BEST_BID_QUANTITY | — | — |
| 97 | NegotiationParentLineBestBidScore | BEST_BID_SCORE | — | — |
| 98 | NegotiationParentLineBidStartPrice | BID_START_PRICE | — | — |
| 99 | NegotiationParentLineCategoryId | CATEGORY_ID | — | — |
| 100 | NegotiationParentLineCloseBiddingDate | CLOSE_BIDDING_DATE | — | — |
| 101 | NegotiationParentLineCreatedBy | CREATED_BY | — | — |
| 102 | NegotiationParentLineCreationDate | CREATION_DATE | — | — |
| 103 | NegotiationParentLineCurrentPrice | CURRENT_PRICE | — | — |
| 104 | NegotiationParentLineDispLineNumber | DISP_LINE_NUMBER | — | — |
| 105 | NegotiationParentLineDisplayTargetPriceFlag | DISPLAY_TARGET_PRICE_FLAG | — | — |
| 106 | NegotiationParentLineDocumentDispLineNumber | DOCUMENT_DISP_LINE_NUMBER | — | — |
| 107 | NegotiationParentLineGroupType | GROUP_TYPE | — | — |
| 108 | NegotiationParentLineHasAttributesFlag | HAS_ATTRIBUTES_FLAG | — | — |
| 109 | NegotiationParentLineHasBuyerPfsFlag | HAS_BUYER_PFS_FLAG | — | — |
| 110 | NegotiationParentLineHasPriceElementsFlag | HAS_PRICE_ELEMENTS_FLAG | — | — |
| 111 | NegotiationParentLineHasQuantityTiers | HAS_QUANTITY_TIERS | — | — |
| 112 | NegotiationParentLineHasShipmentsFlag | HAS_SHIPMENTS_FLAG | — | — |
| 113 | NegotiationParentLineInvOrgId | INV_ORG_ID | — | — |
| 114 | NegotiationParentLineItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 115 | NegotiationParentLineItemId | ITEM_ID | — | — |
| 116 | NegotiationParentLineItemRevision | ITEM_REVISION | — | — |
| 117 | NegotiationParentLineLastAmendmentUpdate | LAST_AMENDMENT_UPDATE | — | — |
| 118 | NegotiationParentLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 119 | NegotiationParentLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 120 | NegotiationParentLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 121 | NegotiationParentLineLineNumber | LINE_NUMBER | — | — |
| 122 | NegotiationParentLineLineOriginationCode | LINE_ORIGINATION_CODE | — | — |
| 123 | NegotiationParentLineLineTypeId | LINE_TYPE_ID | — | — |
| 124 | NegotiationParentLineMaxSubLineSequenceNumber | MAX_SUB_LINE_SEQUENCE_NUMBER | — | — |
| 125 | NegotiationParentLineModifiedDate | MODIFIED_DATE | — | — |
| 126 | NegotiationParentLineModifiedFlag | MODIFIED_FLAG | — | — |
| 127 | NegotiationParentLineNeedByDate | NEED_BY_DATE | — | — |
| 128 | NegotiationParentLineNoAward | NO_AWARD | — | — |
| 129 | NegotiationParentLineNoteToBidders | NOTE_TO_BIDDERS | — | — |
| 130 | NegotiationParentLineNumberOfBids | NUMBER_OF_BIDS | — | — |
| 131 | NegotiationParentLineNumberOfExtensions | NUMBER_OF_EXTENSIONS | — | — |
| 132 | NegotiationParentLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 133 | NegotiationParentLineOrderTypeLookupCode | ORDER_TYPE_LOOKUP_CODE | — | — |
| 134 | NegotiationParentLineParentLineNumber | PARENT_LINE_NUMBER | — | — |
| 135 | NegotiationParentLinePoAgreedAmount | PO_AGREED_AMOUNT | — | — |
| 136 | NegotiationParentLinePoMinRelAmount | PO_MIN_REL_AMOUNT | — | — |
| 137 | NegotiationParentLinePrcBuId | PRC_BU_ID | — | — |
| 138 | NegotiationParentLinePriceBreakNegFlag | PRICE_BREAK_NEG_FLAG | — | — |
| 139 | NegotiationParentLinePriceBreakType | PRICE_BREAK_TYPE | — | — |
| 140 | NegotiationParentLinePriceDisabledFlag | PRICE_DISABLED_FLAG | — | — |
| 141 | NegotiationParentLinePurchaseBasis | PURCHASE_BASIS | — | — |
| 142 | NegotiationParentLineQuantity | QUANTITY | — | — |
| 143 | NegotiationParentLineQuantityDisabledFlag | QUANTITY_DISABLED_FLAG | — | — |
| 144 | NegotiationParentLineReqBuId | REQ_BU_ID | — | — |
| 145 | NegotiationParentLineRequisitionNumber | REQUISITION_NUMBER | — | — |
| 146 | NegotiationParentLineShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 147 | NegotiationParentLineSourceDocId | SOURCE_DOC_ID | — | — |
| 148 | NegotiationParentLineSourceDocNumber | SOURCE_DOC_NUMBER | — | — |
| 149 | NegotiationParentLineSourceLineId | SOURCE_LINE_ID | — | — |
| 150 | NegotiationParentLineSourceLineNumber | SOURCE_LINE_NUMBER | — | — |
| 151 | NegotiationParentLineSubLineSequenceNumber | SUB_LINE_SEQUENCE_NUMBER | — | — |
| 152 | NegotiationParentLineTargetPrice | TARGET_PRICE | — | — |
| 153 | NegotiationParentLineUnitDisplayTargetFlag | UNIT_DISPLAY_TARGET_FLAG | — | — |
| 154 | NegotiationParentLineUnitTargetPrice | UNIT_TARGET_PRICE | — | — |
| 155 | NegotiationParentLineUomCode | UOM_CODE | — | — |

### [[po_system_parameters_all|PO_SYSTEM_PARAMETERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgingOnsetPoint | AGING_ONSET_POINT | — | — |
| 2 | AgingPeriodDays | AGING_PERIOD_DAYS | — | — |
| 3 | AllowItemDescUpdateFlag | ALLOW_ITEM_DESC_UPDATE_FLAG | — | — |
| 4 | AllowManulPriceUpdateOrder | ALLOW_MANUL_PRICE_UPDATE_ORDER | — | — |
| 5 | AllowRetroPricing | ALLOW_RETRO_PRICING | — | — |
| 6 | AwardApprovalEnabledFlag | AWARD_APPROVAL_ENABLED_FLAG | — | — |
| 7 | BestPriceVisibleBlind | BEST_PRICE_VISIBLE_BLIND | — | — |
| 8 | BuyerManagedTransportFlag | BUYER_MANAGED_TRANSPORT_FLAG | — | — |
| 9 | CarrierId | CARRIER_ID | — | — |
| 10 | CatAdminAuthoringAcceptance | CAT_ADMIN_AUTHORING_ACCEPTANCE | — | — |
| 11 | CollabSecurityProfileId | COLLAB_SECURITY_PROFILE_ID | — | — |
| 12 | ConsumptionAdviceFrequency | CONSUMPTION_ADVICE_FREQUENCY | — | — |
| 13 | ConsumptionAdviceSummary | CONSUMPTION_ADVICE_SUMMARY | — | — |
| 14 | CreateDebitMemoFlag | CREATE_DEBIT_MEMO_FLAG | — | — |
| 15 | CreatedBy | CREATED_BY | — | — |
| 16 | CreationDate | CREATION_DATE | — | — |
| 17 | CurrencyCode | CURRENCY_CODE | — | — |
| 18 | DefaultBuyerId | DEFAULT_BUYER_ID | — | — |
| 19 | DefaultPromiseDate | DEFAULT_PROMISE_DATE | — | — |
| 20 | DefaultRateType | DEFAULT_RATE_TYPE | — | — |
| 21 | DoctypeId | DOCTYPE_ID | — | — |
| 22 | EmailAttachmentFilename | EMAIL_ATTACHMENT_FILENAME | — | — |
| 23 | EnforceBuyerAuthorityFlag | ENFORCE_BUYER_AUTHORITY_FLAG | — | — |
| 24 | EnforceMinBidPrice | ENFORCE_MIN_BID_PRICE | — | — |
| 25 | EnforceVendorHoldFlag | ENFORCE_VENDOR_HOLD_FLAG | — | — |
| 26 | FobLookupCode | FOB_LOOKUP_CODE | — | — |
| 27 | FreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 28 | GenOrderForNegReqsFlag | GEN_ORDER_FOR_NEG_REQS_FLAG | — | — |
| 29 | GlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 30 | GlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 31 | GlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 32 | GlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 33 | GlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 34 | GlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 35 | GlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 36 | GlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 37 | GlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 38 | GlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 39 | GlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 40 | GlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 41 | GlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 42 | GlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 43 | GlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 44 | GlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 45 | GlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 46 | GlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 47 | GlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 48 | GlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 49 | GlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 50 | GroupRequisitionLines | GROUP_REQUISITION_LINES | — | — |
| 51 | GroupRequisitions | GROUP_REQUISITIONS | — | — |
| 52 | HdrAttrDefaultMaxScore | HDR_ATTR_DEFAULT_MAX_SCORE | — | — |
| 53 | HdrAttrDispScoreCriteria | HDR_ATTR_DISP_SCORE_CRITERIA | — | — |
| 54 | HdrAttrEnableWeights | HDR_ATTR_ENABLE_WEIGHTS | — | — |
| 55 | InspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | — |
| 56 | InventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 57 | InventoryOrganizationId1 | INVENTORY_ORGANIZATION_ID | — | — |
| 58 | InvoiceCloseCode | INVOICE_CLOSE_CODE | — | — |
| 59 | InvoiceCloseTolerance | INVOICE_CLOSE_TOLERANCE | — | — |
| 60 | LanguageCode | LANGUAGE_CODE | — | — |
| 61 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 62 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 63 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 64 | LineTypeId | LINE_TYPE_ID | — | — |
| 65 | ManualReceiptNumType | MANUAL_RECEIPT_NUM_TYPE | — | — |
| 66 | ManualReqNumType | MANUAL_REQ_NUM_TYPE | — | — |
| 67 | MatchOption | MATCH_OPTION | — | — |
| 68 | MaxAttachmentSize | MAX_ATTACHMENT_SIZE | — | — |
| 69 | MinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 70 | ModeOfTransport | MODE_OF_TRANSPORT | — | — |
| 71 | NegApprovalEnabledFlag | NEG_APPROVAL_ENABLED_FLAG | — | — |
| 72 | NextApproverLookupCode | NEXT_APPROVER_LOOKUP_CODE | — | — |
| 73 | NextNegotiationNumber | NEXT_NEGOTIATION_NUMBER | — | — |
| 74 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 75 | PrcBuId | PRC_BU_ID | — | — |
| 76 | PrcBuId1 | PRC_BU_ID | — | — |
| 77 | PriceBreakLookupCode | PRICE_BREAK_LOOKUP_CODE | — | — |
| 78 | PriceChangeAmount | PRICE_CHANGE_AMOUNT | — | — |
| 79 | RankIndicator | RANK_INDICATOR | — | — |
| 80 | RankVisibleBlind | RANK_VISIBLE_BLIND | — | — |
| 81 | ReceiveCloseCode | RECEIVE_CLOSE_CODE | — | — |
| 82 | ReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | — |
| 83 | ReceivingFlag | RECEIVING_FLAG | — | — |
| 84 | RfqOnlySiteFlag | RFQ_ONLY_SITE_FLAG | — | — |
| 85 | ServiceLevel | SERVICE_LEVEL | — | — |
| 86 | StyleId | STYLE_ID | — | — |
| 87 | SupplierAuthoringAcceptance | SUPPLIER_AUTHORING_ACCEPTANCE | — | — |
| 88 | SupplierHistoryDuration | SUPPLIER_HISTORY_DURATION | — | — |
| 89 | SystemConfiguredFlag | SYSTEM_CONFIGURED_FLAG | — | — |
| 90 | TaxFromItemFlag | TAX_FROM_ITEM_FLAG | — | — |
| 91 | TaxFromShipToLocFlag | TAX_FROM_SHIP_TO_LOC_FLAG | — | — |
| 92 | TaxFromSystemFlag | TAX_FROM_SYSTEM_FLAG | — | — |
| 93 | TaxFromVendorFlag | TAX_FROM_VENDOR_FLAG | — | — |
| 94 | TaxFromVendorSiteFlag | TAX_FROM_VENDOR_SITE_FLAG | — | — |
| 95 | TaxHierItem | TAX_HIER_ITEM | — | — |
| 96 | TaxHierShipToLoc | TAX_HIER_SHIP_TO_LOC | — | — |
| 97 | TaxHierSystem | TAX_HIER_SYSTEM | — | — |
| 98 | TaxHierVendor | TAX_HIER_VENDOR | — | — |
| 99 | TaxHierVendorSite | TAX_HIER_VENDOR_SITE | — | — |
| 100 | TaxableFlag | TAXABLE_FLAG | — | — |
| 101 | TermsId | TERMS_ID | — | — |
| 102 | UseNeedByDate | USE_NEED_BY_DATE | — | — |
| 103 | UseSalesOrderNumberFlag | USE_SALES_ORDER_NUMBER_FLAG | — | — |
| 104 | UseShipTo | USE_SHIP_TO | — | — |
| 105 | UserDefinedReceiptNumCode | USER_DEFINED_RECEIPT_NUM_CODE | — | — |
| 106 | UserDefinedReqNumCode | USER_DEFINED_REQ_NUM_CODE | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
