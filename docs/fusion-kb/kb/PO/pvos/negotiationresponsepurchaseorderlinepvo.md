---
id: DOC-PO-PVO-NegotiationResponsePurchaseOrderLinePVO
doc_type: system-doc
title: "NegotiationResponsePurchaseOrderLinePVO — PVO Purchasing"
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
  - NegotiationResponsePurchaseOrderLinePVO
  - negotiationresponsepurchaseorderlinepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationResponsePurchaseOrderLinePVO

## 📌 Visão Geral

Extrai a vinculação entre linhas de resposta de negociação e linhas de ordens de compra geradas. Permite rastreabilidade completa do sourcing até a execução do pedido de compra.

**Caminho:** `FscmTopModelAM.PrcPonPublicViewAM.NegotiationResponsePurchaseOrderLinePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 676 | 12 | 3 | 103 | 15% |

---

## 🔗 Tabelas Relacionadas

- [[egp_categories_vl|EGP_CATEGORIES_VL]] — 9 atributos (3 BICC)
- [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]] — 6 atributos
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 2 atributos
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 29 atributos (1 BICC)
- [[inv_units_of_measure_vl|INV_UNITS_OF_MEASURE_VL]] — 4 atributos (1 BICC)
- [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]] — 218 atributos (28 BICC)
- [[pon_auction_item_prices_all|PON_AUCTION_ITEM_PRICES_ALL]] — 96 atributos (27 BICC)
- [[pon_bid_headers|PON_BID_HEADERS]] — 74 atributos (16 BICC)
- [[pon_bid_item_prices|PON_BID_ITEM_PRICES]] — 85 atributos (20 BICC)
- [[pon_bid_po_lines|PON_BID_PO_LINES]] — 15 atributos (3 PKs, 5 BICC)
- [[pon_bid_po_numbers|PON_BID_PO_NUMBERS]] — 34 atributos (1 BICC)
- [[po_system_parameters_all|PO_SYSTEM_PARAMETERS_ALL]] — 104 atributos (1 BICC)

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
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |

### [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 2 | ItemInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 3 | ItemItemNumber | ITEM_NUMBER | — | — |
| 4 | ItemItemType | ITEM_TYPE | — | — |
| 5 | ItemOrganizationId | ORGANIZATION_ID | — | — |
| 6 | ItemPrimaryUomCode | PRIMARY_UOM_CODE | — | — |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitId | BU_ID | — | — |
| 2 | PrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |

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
| 9 | DailyConversionTypeNegoHdrLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | DailyConversionTypeNegoHdrLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | DailyConversionTypeNegoHdrLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | DailyConversionTypeNegoHdrObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | DailyConversionTypeNegoHdrPivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 14 | DailyConversionTypeNegoHdrSecurityFlag | SECURITY_FLAG | — | — |
| 15 | DailyConversionTypeNegoHdrUserConversionType | USER_CONVERSION_TYPE | — | — |
| 16 | DailyConversionTypeNegoHdrUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |
| 17 | DailyConversionTypeResHdrConversionType | CONVERSION_TYPE | — | — |
| 18 | DailyConversionTypeResHdrDescription | DESCRIPTION | — | — |
| 19 | DailyConversionTypeResHdrEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 20 | DailyConversionTypeResHdrEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 21 | DailyConversionTypeResHdrFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 22 | DailyConversionTypeResHdrFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 23 | DailyConversionTypeResHdrFemScenario | FEM_SCENARIO | — | — |
| 24 | DailyConversionTypeResHdrFemTimeframe | FEM_TIMEFRAME | — | — |
| 25 | DailyConversionTypeResHdrObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 26 | DailyConversionTypeResHdrPivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 27 | DailyConversionTypeResHdrSecurityFlag | SECURITY_FLAG | — | — |
| 28 | DailyConversionTypeResHdrUserConversionType | USER_CONVERSION_TYPE | — | — |
| 29 | DailyConversionTypeResHdrUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |

### [[inv_units_of_measure_vl|INV_UNITS_OF_MEASURE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | — |
| 2 | ObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 3 | UnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 4 | UomCode | UOM_CODE | — | ✅ |

### [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllowAlternateLines | ALLOW_ALTERNATE_LINES | — | — |
| 2 | BidRevisionType | BID_REVISION_TYPE | — | — |
| 3 | BidRevisionTypeDspFlag | BID_REVISION_TYPE_DSP_FLAG | — | — |
| 4 | BuyerTransportEnabledFlag | BUYER_TRANSPORT_ENABLED_FLAG | — | — |
| 5 | BuyerTransportFlag | BUYER_TRANSPORT_FLAG | — | ✅ |
| 6 | NegotiationHeaderAbstractDetails | ABSTRACT_DETAILS | — | — |
| 7 | NegotiationHeaderAbstractStatus | ABSTRACT_STATUS | — | — |
| 8 | NegotiationHeaderAdvanceNegotiableFlag | ADVANCE_NEGOTIABLE_FLAG | — | — |
| 9 | NegotiationHeaderAllowOtherBidCurrencyFlag | ALLOW_OTHER_BID_CURRENCY_FLAG | — | — |
| 10 | NegotiationHeaderAmendmentDescription | AMENDMENT_DESCRIPTION | — | — |
| 11 | NegotiationHeaderAmendmentNumber | AMENDMENT_NUMBER | — | — |
| 12 | NegotiationHeaderApprovalStatus | NEG_APPROVAL_STATUS | — | — |
| 13 | NegotiationHeaderAttributeLineNumber | ATTRIBUTE_LINE_NUMBER | — | — |
| 14 | NegotiationHeaderAttributesExist | ATTRIBUTES_EXIST | — | — |
| 15 | NegotiationHeaderAuctionHeaderId | AUCTION_HEADER_ID | — | — |
| 16 | NegotiationHeaderAuctionHeaderIdOrigAmend | AUCTION_HEADER_ID_ORIG_AMEND | — | — |
| 17 | NegotiationHeaderAuctionHeaderIdOrigRound | AUCTION_HEADER_ID_ORIG_ROUND | — | — |
| 18 | NegotiationHeaderAuctionHeaderIdPrevAmend | AUCTION_HEADER_ID_PREV_AMEND | — | — |
| 19 | NegotiationHeaderAuctionHeaderIdPrevRound | AUCTION_HEADER_ID_PREV_ROUND | — | — |
| 20 | NegotiationHeaderAuctionOriginationCode | AUCTION_ORIGINATION_CODE | — | — |
| 21 | NegotiationHeaderAuctionRoundNumber | AUCTION_ROUND_NUMBER | — | ✅ |
| 22 | NegotiationHeaderAuctionStatus | AUCTION_STATUS | — | ✅ |
| 23 | NegotiationHeaderAuctionTitle | AUCTION_TITLE | — | ✅ |
| 24 | NegotiationHeaderAutoExtendAllLinesFlag | AUTO_EXTEND_ALL_LINES_FLAG | — | — |
| 25 | NegotiationHeaderAutoExtendDuration | AUTO_EXTEND_DURATION | — | — |
| 26 | NegotiationHeaderAutoExtendEnabledFlag | AUTO_EXTEND_ENABLED_FLAG | — | — |
| 27 | NegotiationHeaderAutoExtendFlag | AUTO_EXTEND_FLAG | — | — |
| 28 | NegotiationHeaderAutoExtendMinTriggerRank | AUTO_EXTEND_MIN_TRIGGER_RANK | — | — |
| 29 | NegotiationHeaderAutoExtendNumber | AUTO_EXTEND_NUMBER | — | — |
| 30 | NegotiationHeaderAutoExtendTypeFlag | AUTO_EXTEND_TYPE_FLAG | — | — |
| 31 | NegotiationHeaderAutoextendChangedFlag | AUTOEXTEND_CHANGED_FLAG | — | — |
| 32 | NegotiationHeaderAwardApprAmeTransId | AWARD_APPR_AME_TRANS_ID | — | — |
| 33 | NegotiationHeaderAwardApprAmeTransPrevId | AWARD_APPR_AME_TRANS_PREV_ID | — | — |
| 34 | NegotiationHeaderAwardApprAmeTxnDate | AWARD_APPR_AME_TXN_DATE | — | — |
| 35 | NegotiationHeaderAwardApprovalFlag | AWARD_APPROVAL_FLAG | — | — |
| 36 | NegotiationHeaderAwardApprovalStatus | AWARD_APPROVAL_STATUS | — | — |
| 37 | NegotiationHeaderAwardByDate | AWARD_BY_DATE | — | — |
| 38 | NegotiationHeaderAwardCompleteDate | AWARD_COMPLETE_DATE | — | ✅ |
| 39 | NegotiationHeaderAwardDate | AWARD_DATE | — | ✅ |
| 40 | NegotiationHeaderAwardMode | AWARD_MODE | — | — |
| 41 | NegotiationHeaderAwardStatus | AWARD_STATUS | — | — |
| 42 | NegotiationHeaderBidDecrementMethod | BID_DECREMENT_METHOD | — | — |
| 43 | NegotiationHeaderBidFrequencyCode | BID_FREQUENCY_CODE | — | — |
| 44 | NegotiationHeaderBidListType | BID_LIST_TYPE | — | — |
| 45 | NegotiationHeaderBidRanking | BID_RANKING | — | ✅ |
| 46 | NegotiationHeaderBidScopeCode | BID_SCOPE_CODE | — | — |
| 47 | NegotiationHeaderBidVisibilityCode | BID_VISIBILITY_CODE | — | ✅ |
| 48 | NegotiationHeaderCancelDate | CANCEL_DATE | — | — |
| 49 | NegotiationHeaderCarrierId | CARRIER_ID | — | — |
| 50 | NegotiationHeaderCloseBiddingDate | CLOSE_BIDDING_DATE | — | ✅ |
| 51 | NegotiationHeaderCompleteFlag | COMPLETE_FLAG | — | — |
| 52 | NegotiationHeaderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 53 | NegotiationHeaderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 54 | NegotiationHeaderContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 55 | NegotiationHeaderContractTemplateId | CONTRACT_TEMPLATE_ID | — | — |
| 56 | NegotiationHeaderContractType | CONTRACT_TYPE | — | ✅ |
| 57 | NegotiationHeaderCreatedBy | CREATED_BY | — | — |
| 58 | NegotiationHeaderCreationDate | CREATION_DATE | — | — |
| 59 | NegotiationHeaderCreationDateOrigAmend | CREATION_DATE_ORIG_AMEND | — | — |
| 60 | NegotiationHeaderCurrencyCode | CURRENCY_CODE | — | ✅ |
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
| 139 | NegotiationHeaderNegTeamEnabledFlag | NEG_TEAM_ENABLED_FLAG | — | — |
| 140 | NegotiationHeaderNumberOfBids | NUMBER_OF_BIDS | — | — |
| 141 | NegotiationHeaderNumberOfExtensions | NUMBER_OF_EXTENSIONS | — | — |
| 142 | NegotiationHeaderNumberOfLines | NUMBER_OF_LINES | — | — |
| 143 | NegotiationHeaderNumberPriceDecimals | NUMBER_PRICE_DECIMALS | — | — |
| 144 | NegotiationHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 145 | NegotiationHeaderOpenAuctionNowFlag | OPEN_AUCTION_NOW_FLAG | — | ✅ |
| 146 | NegotiationHeaderOpenBiddingDate | OPEN_BIDDING_DATE | — | ✅ |
| 147 | NegotiationHeaderOriginalCloseBiddingDate | ORIGINAL_CLOSE_BIDDING_DATE | — | — |
| 148 | NegotiationHeaderOutcomeStatus | OUTCOME_STATUS | — | — |
| 149 | NegotiationHeaderPauseRemarks | PAUSE_REMARKS | — | — |
| 150 | NegotiationHeaderPaymentTermsId | PAYMENT_TERMS_ID | — | — |
| 151 | NegotiationHeaderPersonId | PERSON_ID | — | — |
| 152 | NegotiationHeaderPfTypeAllowed | PF_TYPE_ALLOWED | — | — |
| 153 | NegotiationHeaderPoAgreedAmount | PO_AGREED_AMOUNT | — | ✅ |
| 154 | NegotiationHeaderPoEndDate | PO_END_DATE | — | ✅ |
| 155 | NegotiationHeaderPoMinRelAmount | PO_MIN_REL_AMOUNT | — | ✅ |
| 156 | NegotiationHeaderPoStartDate | PO_START_DATE | — | ✅ |
| 157 | NegotiationHeaderPoStyleId | PO_STYLE_ID | — | — |
| 158 | NegotiationHeaderPowerBiddingEnabledFlag | POWER_BIDDING_ENABLED_FLAG | — | — |
| 159 | NegotiationHeaderPrcBuId | PRC_BU_ID | — | — |
| 160 | NegotiationHeaderPriceDrivenAuctionFlag | PRICE_DRIVEN_AUCTION_FLAG | — | — |
| 161 | NegotiationHeaderPriceElementEnabledFlag | PRICE_ELEMENT_ENABLED_FLAG | — | — |
| 162 | NegotiationHeaderPriceTiersIndicator | PRICE_TIERS_INDICATOR | — | ✅ |
| 163 | NegotiationHeaderProgramAppName | PROGRAM_APP_NAME | — | — |
| 164 | NegotiationHeaderProgramName | PROGRAM_NAME | — | — |
| 165 | NegotiationHeaderProgressPaymentType | PROGRESS_PAYMENT_TYPE | — | — |
| 166 | NegotiationHeaderProgressPymtNegotiableFlag | PROGRESS_PYMT_NEGOTIABLE_FLAG | — | — |
| 167 | NegotiationHeaderProjectId | PROJECT_ID | — | — |
| 168 | NegotiationHeaderProxyBiddingEnabledFlag | PROXY_BIDDING_ENABLED_FLAG | — | — |
| 169 | NegotiationHeaderPublishAuctionNowFlag | PUBLISH_AUCTION_NOW_FLAG | — | — |
| 170 | NegotiationHeaderPublishDate | PUBLISH_DATE | — | ✅ |
| 171 | NegotiationHeaderPublishDateOrigAmend | PUBLISH_DATE_ORIG_AMEND | — | — |
| 172 | NegotiationHeaderPublishRatesToBiddersFlag | PUBLISH_RATES_TO_BIDDERS_FLAG | — | — |
| 173 | NegotiationHeaderQtyPriceTiersEnabledFlag | QTY_PRICE_TIERS_ENABLED_FLAG | — | — |
| 174 | NegotiationHeaderRankIndicator | RANK_INDICATOR | — | ✅ |
| 175 | NegotiationHeaderRateDate | RATE_DATE | — | — |
| 176 | NegotiationHeaderRateType | RATE_TYPE | — | — |
| 177 | NegotiationHeaderRecoupmentNegotiableFlag | RECOUPMENT_NEGOTIABLE_FLAG | — | — |
| 178 | NegotiationHeaderReminderDate | REMINDER_DATE | — | — |
| 179 | NegotiationHeaderRequestDate | REQUEST_DATE | — | — |
| 180 | NegotiationHeaderRequestId | REQUEST_ID | — | — |
| 181 | NegotiationHeaderRequestedBy | REQUESTED_BY | — | — |
| 182 | NegotiationHeaderRetainageNegotiableFlag | RETAINAGE_NEGOTIABLE_FLAG | — | — |
| 183 | NegotiationHeaderRfiLineEnabledFlag | RFI_LINE_ENABLED_FLAG | — | — |
| 184 | NegotiationHeaderScoringLockDate | SCORING_LOCK_DATE | — | — |
| 185 | NegotiationHeaderSealedActualUnlockDate | SEALED_ACTUAL_UNLOCK_DATE | — | — |
| 186 | NegotiationHeaderSealedActualUnsealDate | SEALED_ACTUAL_UNSEAL_DATE | — | — |
| 187 | NegotiationHeaderSealedAuctionStatus | SEALED_AUCTION_STATUS | — | ✅ |
| 188 | NegotiationHeaderServiceLevel | SERVICE_LEVEL | — | — |
| 189 | NegotiationHeaderShareAwardDecision | SHARE_AWARD_DECISION | — | — |
| 190 | NegotiationHeaderShowBidderNotes | SHOW_BIDDER_NOTES | — | — |
| 191 | NegotiationHeaderShowBidderScores | SHOW_BIDDER_SCORES | — | — |
| 192 | NegotiationHeaderSourceDocId | SOURCE_DOC_ID | — | — |
| 193 | NegotiationHeaderSourceDocLineMsg | SOURCE_DOC_LINE_MSG | — | — |
| 194 | NegotiationHeaderSourceDocMsg | SOURCE_DOC_MSG | — | — |
| 195 | NegotiationHeaderSourceDocMsgApp | SOURCE_DOC_MSG_APP | — | — |
| 196 | NegotiationHeaderSourceDocNumber | SOURCE_DOC_NUMBER | — | ✅ |
| 197 | NegotiationHeaderSourceReqsFlag | SOURCE_REQS_FLAG | — | — |
| 198 | NegotiationHeaderStaggeredClosingInterval | STAGGERED_CLOSING_INTERVAL | — | — |
| 199 | NegotiationHeaderStyleId | STYLE_ID | — | — |
| 200 | NegotiationHeaderSupplierEnterablePymtFlag | SUPPLIER_ENTERABLE_PYMT_FLAG | — | — |
| 201 | NegotiationHeaderSupplierViewType | SUPPLIER_VIEW_TYPE | — | — |
| 202 | NegotiationHeaderTeamScoringEnabledFlag | TEAM_SCORING_ENABLED_FLAG | — | — |
| 203 | NegotiationHeaderTechnicalActualUnlockDate | TECHNICAL_ACTUAL_UNLOCK_DATE | — | — |
| 204 | NegotiationHeaderTechnicalActualUnsealDate | TECHNICAL_ACTUAL_UNSEAL_DATE | — | — |
| 205 | NegotiationHeaderTechnicalEvaluationStatus | TECHNICAL_EVALUATION_STATUS | — | — |
| 206 | NegotiationHeaderTechnicalLockStatus | TECHNICAL_LOCK_STATUS | — | — |
| 207 | NegotiationHeaderTemplateId | TEMPLATE_ID | — | — |
| 208 | NegotiationHeaderTemplateScope | TEMPLATE_SCOPE | — | — |
| 209 | NegotiationHeaderTemplateStatus | TEMPLATE_STATUS | — | — |
| 210 | NegotiationHeaderTwoPartFlag | TWO_PART_FLAG | — | ✅ |
| 211 | NegotiationHeaderVersionNum | VERSION_NUM | — | — |
| 212 | NegotiationHeaderViewByDate | VIEW_BY_DATE | — | ✅ |
| 213 | NegotiationHeaderWfApprovalItemKey | WF_APPROVAL_ITEM_KEY | — | — |
| 214 | NegotiationHeaderWfAwardApprovalItemKey | WF_AWARD_APPROVAL_ITEM_KEY | — | — |
| 215 | NegotiationHeaderWfItemKey | WF_ITEM_KEY | — | — |
| 216 | NegotiationHeaderWfPoncomplCurrentRound | WF_PONCOMPL_CURRENT_ROUND | — | — |
| 217 | NegotiationHeaderWfPoncomplItemKey | WF_PONCOMPL_ITEM_KEY | — | — |
| 218 | NegotiationHeaderWfRoleName | WF_ROLE_NAME | — | — |

### [[pon_auction_item_prices_all|PON_AUCTION_ITEM_PRICES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationLineAdditionalJobDetails | ADDITIONAL_JOB_DETAILS | — | — |
| 2 | NegotiationLineAdvanceAmount | ADVANCE_AMOUNT | — | — |
| 3 | NegotiationLineAllocationStatus | ALLOCATION_STATUS | — | — |
| 4 | NegotiationLineAuctionHeaderId | AUCTION_HEADER_ID | — | — |
| 5 | NegotiationLineAwardMode | AWARD_MODE | — | — |
| 6 | NegotiationLineAwardStatus | AWARD_STATUS | — | — |
| 7 | NegotiationLineAwardedQuantity | AWARDED_QUANTITY | — | — |
| 8 | NegotiationLineBestBidBidCurrencyCode | BEST_BID_BID_CURRENCY_CODE | — | — |
| 9 | NegotiationLineBestBidBidCurrencyPrice | BEST_BID_BID_CURRENCY_PRICE | — | — |
| 10 | NegotiationLineBestBidBidNumber | BEST_BID_BID_NUMBER | — | — |
| 11 | NegotiationLineBestBidBidPrice | BEST_BID_BID_PRICE | — | — |
| 12 | NegotiationLineBestBidCurrencyCode | BEST_BID_CURRENCY_CODE | — | ✅ |
| 13 | NegotiationLineBestBidCurrencyPrice | BEST_BID_CURRENCY_PRICE | — | ✅ |
| 14 | NegotiationLineBestBidFirstBidPrice | BEST_BID_FIRST_BID_PRICE | — | ✅ |
| 15 | NegotiationLineBestBidNumber | BEST_BID_NUMBER | — | ✅ |
| 16 | NegotiationLineBestBidPrice | BEST_BID_PRICE | — | ✅ |
| 17 | NegotiationLineBestBidPromisedDate | BEST_BID_PROMISED_DATE | — | — |
| 18 | NegotiationLineBestBidProxyLimitPrice | BEST_BID_PROXY_LIMIT_PRICE | — | — |
| 19 | NegotiationLineBestBidQuantity | BEST_BID_QUANTITY | — | ✅ |
| 20 | NegotiationLineBestBidScore | BEST_BID_SCORE | — | ✅ |
| 21 | NegotiationLineBidStartPrice | BID_START_PRICE | — | ✅ |
| 22 | NegotiationLineCategoryId | CATEGORY_ID | — | — |
| 23 | NegotiationLineCloseBiddingDate | CLOSE_BIDDING_DATE | — | — |
| 24 | NegotiationLineCreatedBy | CREATED_BY | — | — |
| 25 | NegotiationLineCreationDate | CREATION_DATE | — | — |
| 26 | NegotiationLineCurrentPrice | CURRENT_PRICE | — | ✅ |
| 27 | NegotiationLineDifferentialResponseType | DIFFERENTIAL_RESPONSE_TYPE | — | — |
| 28 | NegotiationLineDispLineNumber | DISP_LINE_NUMBER | — | — |
| 29 | NegotiationLineDisplayTargetPriceFlag | DISPLAY_TARGET_PRICE_FLAG | — | ✅ |
| 30 | NegotiationLineDocumentDispLineNumber | DOCUMENT_DISP_LINE_NUMBER | — | ✅ |
| 31 | NegotiationLineGroupType | GROUP_TYPE | — | ✅ |
| 32 | NegotiationLineHasAttributesFlag | HAS_ATTRIBUTES_FLAG | — | — |
| 33 | NegotiationLineHasBuyerPfsFlag | HAS_BUYER_PFS_FLAG | — | — |
| 34 | NegotiationLineHasPaymentsFlag | HAS_PAYMENTS_FLAG | — | — |
| 35 | NegotiationLineHasPriceDifferentialsFlag | HAS_PRICE_DIFFERENTIALS_FLAG | — | — |
| 36 | NegotiationLineHasPriceElementsFlag | HAS_PRICE_ELEMENTS_FLAG | — | — |
| 37 | NegotiationLineHasQuantityTiers | HAS_QUANTITY_TIERS | — | — |
| 38 | NegotiationLineHasShipmentsFlag | HAS_SHIPMENTS_FLAG | — | — |
| 39 | NegotiationLineInvOrgId | INV_ORG_ID | — | — |
| 40 | NegotiationLineItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 41 | NegotiationLineItemId | ITEM_ID | — | ✅ |
| 42 | NegotiationLineItemRevision | ITEM_REVISION | — | ✅ |
| 43 | NegotiationLineJobId | JOB_ID | — | — |
| 44 | NegotiationLineLastAmendmentUpdate | LAST_AMENDMENT_UPDATE | — | — |
| 45 | NegotiationLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 46 | NegotiationLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 47 | NegotiationLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 48 | NegotiationLineLineNumber | LINE_NUMBER | — | — |
| 49 | NegotiationLineLineOriginationCode | LINE_ORIGINATION_CODE | — | — |
| 50 | NegotiationLineLineTypeId | LINE_TYPE_ID | — | — |
| 51 | NegotiationLineMaxRetainageAmount | MAX_RETAINAGE_AMOUNT | — | — |
| 52 | NegotiationLineMaxSubLineSequenceNumber | MAX_SUB_LINE_SEQUENCE_NUMBER | — | — |
| 53 | NegotiationLineModifiedDate | MODIFIED_DATE | — | — |
| 54 | NegotiationLineModifiedFlag | MODIFIED_FLAG | — | — |
| 55 | NegotiationLineNeedByDate | NEED_BY_DATE | — | ✅ |
| 56 | NegotiationLineNoAward | NO_AWARD | — | — |
| 57 | NegotiationLineNoteToBidders | NOTE_TO_BIDDERS | — | ✅ |
| 58 | NegotiationLineNumberOfBids | NUMBER_OF_BIDS | — | — |
| 59 | NegotiationLineNumberOfExtensions | NUMBER_OF_EXTENSIONS | — | — |
| 60 | NegotiationLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 61 | NegotiationLineOrderTypeLookupCode | ORDER_TYPE_LOOKUP_CODE | — | — |
| 62 | NegotiationLineParentLineNumber | PARENT_LINE_NUMBER | — | — |
| 63 | NegotiationLinePoAgreedAmount | PO_AGREED_AMOUNT | — | ✅ |
| 64 | NegotiationLinePoMinRelAmount | PO_MIN_REL_AMOUNT | — | ✅ |
| 65 | NegotiationLinePrcBuId | PRC_BU_ID | — | — |
| 66 | NegotiationLinePriceBreakNegFlag | PRICE_BREAK_NEG_FLAG | — | — |
| 67 | NegotiationLinePriceBreakType | PRICE_BREAK_TYPE | — | — |
| 68 | NegotiationLinePriceDiffShipmentNumber | PRICE_DIFF_SHIPMENT_NUMBER | — | — |
| 69 | NegotiationLinePriceDisabledFlag | PRICE_DISABLED_FLAG | — | — |
| 70 | NegotiationLineProgressPymtRatePercent | PROGRESS_PYMT_RATE_PERCENT | — | — |
| 71 | NegotiationLineProjectAwardId | PROJECT_AWARD_ID | — | — |
| 72 | NegotiationLineProjectExpOrganizationId | PROJECT_EXP_ORGANIZATION_ID | — | — |
| 73 | NegotiationLineProjectExpenditureItemDate | PROJECT_EXPENDITURE_ITEM_DATE | — | — |
| 74 | NegotiationLineProjectExpenditureType | PROJECT_EXPENDITURE_TYPE | — | — |
| 75 | NegotiationLineProjectId | PROJECT_ID | — | — |
| 76 | NegotiationLineProjectTaskId | PROJECT_TASK_ID | — | — |
| 77 | NegotiationLinePurchaseBasis | PURCHASE_BASIS | — | — |
| 78 | NegotiationLineQuantity | QUANTITY | — | ✅ |
| 79 | NegotiationLineQuantityDisabledFlag | QUANTITY_DISABLED_FLAG | — | — |
| 80 | NegotiationLineRecoupmentRatePercent | RECOUPMENT_RATE_PERCENT | — | — |
| 81 | NegotiationLineReqBuId | REQ_BU_ID | — | — |
| 82 | NegotiationLineRequisitionNumber | REQUISITION_NUMBER | — | ✅ |
| 83 | NegotiationLineRetainageRatePercent | RETAINAGE_RATE_PERCENT | — | — |
| 84 | NegotiationLineShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 85 | NegotiationLineSourceDocId | SOURCE_DOC_ID | — | — |
| 86 | NegotiationLineSourceDocNumber | SOURCE_DOC_NUMBER | — | — |
| 87 | NegotiationLineSourceLineId | SOURCE_LINE_ID | — | — |
| 88 | NegotiationLineSourceLineNumber | SOURCE_LINE_NUMBER | — | ✅ |
| 89 | NegotiationLineSubLineSequenceNumber | SUB_LINE_SEQUENCE_NUMBER | — | — |
| 90 | NegotiationLineTargetPrice | TARGET_PRICE | — | ✅ |
| 91 | NegotiationLineUnitDisplayTargetFlag | UNIT_DISPLAY_TARGET_FLAG | — | — |
| 92 | NegotiationLineUnitTargetPrice | UNIT_TARGET_PRICE | — | — |
| 93 | NegotiationLineUomCode | UOM_CODE | — | ✅ |
| 94 | NegotiationLineWorkApproverUserId | WORK_APPROVER_USER_ID | — | — |
| 95 | RequestedDeliveryDate | REQUESTED_DELIVERY_DATE | — | ✅ |
| 96 | RequestedShipDate | REQUESTED_SHIP_DATE | — | ✅ |

### [[pon_bid_headers|PON_BID_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OriginalBidNumber | ORIGINAL_BID_NUMBER | — | — |
| 2 | ResponseHeaderAttributeLineNumber | ATTRIBUTE_LINE_NUMBER | — | — |
| 3 | ResponseHeaderAuctionHeaderId | AUCTION_HEADER_ID | — | — |
| 4 | ResponseHeaderAwardDate | AWARD_DATE | — | — |
| 5 | ResponseHeaderAwardStatus | AWARD_STATUS | — | — |
| 6 | ResponseHeaderBidCurrencyCode | BID_CURRENCY_CODE | — | ✅ |
| 7 | ResponseHeaderBidExpirationDate | BID_EXPIRATION_DATE | — | — |
| 8 | ResponseHeaderBidNumber | BID_NUMBER | — | — |
| 9 | ResponseHeaderBidStatus | BID_STATUS | — | — |
| 10 | ResponseHeaderBiddersBidNumber | BIDDERS_BID_NUMBER | — | — |
| 11 | ResponseHeaderBuyerBidTotal | BUYER_BID_TOTAL | — | — |
| 12 | ResponseHeaderCancelReason | CANCEL_REASON | — | ✅ |
| 13 | ResponseHeaderCancelledDate | CANCELLED_DATE | — | ✅ |
| 14 | ResponseHeaderColorSequenceId | COLOR_SEQUENCE_ID | — | — |
| 15 | ResponseHeaderCreatedBy | CREATED_BY | — | — |
| 16 | ResponseHeaderCreationDate | CREATION_DATE | — | — |
| 17 | ResponseHeaderCurrentRebate | CURRENT_REBATE | — | — |
| 18 | ResponseHeaderCurrentTotalSpend | CURRENT_TOTAL_SPEND | — | — |
| 19 | ResponseHeaderDisplayPriceFactorsFlag | DISPLAY_PRICE_FACTORS_FLAG | — | — |
| 20 | ResponseHeaderDisqualifyReason | DISQUALIFY_REASON | — | — |
| 21 | ResponseHeaderDraftLocked | DRAFT_LOCKED | — | ✅ |
| 22 | ResponseHeaderDraftLockedBy | DRAFT_LOCKED_BY | — | — |
| 23 | ResponseHeaderDraftLockedByContactId | DRAFT_LOCKED_BY_CONTACT_ID | — | — |
| 24 | ResponseHeaderDraftLockedDate | DRAFT_LOCKED_DATE | — | ✅ |
| 25 | ResponseHeaderDraftUnlockedBy | DRAFT_UNLOCKED_BY | — | — |
| 26 | ResponseHeaderDraftUnlockedByContactId | DRAFT_UNLOCKED_BY_CONTACT_ID | — | — |
| 27 | ResponseHeaderDraftUnlockedDate | DRAFT_UNLOCKED_DATE | — | ✅ |
| 28 | ResponseHeaderFixedIncentive | FIXED_INCENTIVE | — | — |
| 29 | ResponseHeaderHasRebateTiers | HAS_REBATE_TIERS | — | — |
| 30 | ResponseHeaderImportFileName | IMPORT_FILE_NAME | — | — |
| 31 | ResponseHeaderIncumbentFlag | INCUMBENT_FLAG | — | — |
| 32 | ResponseHeaderInternalNote | INTERNAL_NOTE | — | ✅ |
| 33 | ResponseHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 34 | ResponseHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 35 | ResponseHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 36 | ResponseHeaderMinBidChange | MIN_BID_CHANGE | — | — |
| 37 | ResponseHeaderNoteToAuctionOwner | NOTE_TO_AUCTION_OWNER | — | ✅ |
| 38 | ResponseHeaderNoteToSupplier | NOTE_TO_SUPPLIER | — | ✅ |
| 39 | ResponseHeaderNumberPriceDecimals | NUMBER_PRICE_DECIMALS | — | ✅ |
| 40 | ResponseHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 41 | ResponseHeaderOldBidExpirationDate | OLD_BID_EXPIRATION_DATE | — | — |
| 42 | ResponseHeaderOldBidNumber | OLD_BID_NUMBER | — | — |
| 43 | ResponseHeaderOldBidStatus | OLD_BID_STATUS | — | — |
| 44 | ResponseHeaderOldBiddersBidNumber | OLD_BIDDERS_BID_NUMBER | — | — |
| 45 | ResponseHeaderOldMinBidChange | OLD_MIN_BID_CHANGE | — | — |
| 46 | ResponseHeaderOldNoteToAuctionOwner | OLD_NOTE_TO_AUCTION_OWNER | — | — |
| 47 | ResponseHeaderOldSurrogBidReceiptDate | OLD_SURROG_BID_RECEIPT_DATE | — | — |
| 48 | ResponseHeaderPartialResponseFlag | PARTIAL_RESPONSE_FLAG | — | ✅ |
| 49 | ResponseHeaderPoAgreedAmount | PO_AGREED_AMOUNT | — | — |
| 50 | ResponseHeaderProgramAppName | PROGRAM_APP_NAME | — | — |
| 51 | ResponseHeaderProgramName | PROGRAM_NAME | — | — |
| 52 | ResponseHeaderProxyBidFlag | PROXY_BID_FLAG | — | — |
| 53 | ResponseHeaderPublishDate | PUBLISH_DATE | — | ✅ |
| 54 | ResponseHeaderRate | RATE | — | — |
| 55 | ResponseHeaderRateDate | RATE_DATE | — | — |
| 56 | ResponseHeaderRateDsp | RATE_DSP | — | — |
| 57 | ResponseHeaderRateType | RATE_TYPE | — | — |
| 58 | ResponseHeaderRequestDate | REQUEST_DATE | — | — |
| 59 | ResponseHeaderRequestId | REQUEST_ID | — | — |
| 60 | ResponseHeaderRequestedBy | REQUESTED_BY | — | — |
| 61 | ResponseHeaderScoreOverridenDate | SCORE_OVERRIDEN_DATE | — | — |
| 62 | ResponseHeaderScoreOverridenFlag | SCORE_OVERRIDEN_FLAG | — | — |
| 63 | ResponseHeaderShortlistFlag | SHORTLIST_FLAG | — | ✅ |
| 64 | ResponseHeaderSurrogBidCreatedPersonId | SURROG_BID_CREATED_PERSON_ID | — | — |
| 65 | ResponseHeaderSurrogBidFlag | SURROG_BID_FLAG | — | ✅ |
| 66 | ResponseHeaderSurrogBidOnlineEntryDate | SURROG_BID_ONLINE_ENTRY_DATE | — | — |
| 67 | ResponseHeaderSurrogBidReceiptDate | SURROG_BID_RECEIPT_DATE | — | — |
| 68 | ResponseHeaderTechnicalShortlistFlag | TECHNICAL_SHORTLIST_FLAG | — | ✅ |
| 69 | ResponseHeaderTotalAwardAmount | TOTAL_AWARD_AMOUNT | — | — |
| 70 | ResponseHeaderTradingPartnerContactId | TRADING_PARTNER_CONTACT_ID | — | — |
| 71 | ResponseHeaderTradingPartnerId | TRADING_PARTNER_ID | — | — |
| 72 | ResponseHeaderVendorId | VENDOR_ID | — | — |
| 73 | ResponseHeaderVendorSiteId | VENDOR_SITE_ID | — | — |
| 74 | TypeOfResponse | TYPE_OF_RESPONSE | — | — |

### [[pon_bid_item_prices|PON_BID_ITEM_PRICES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AlternateLineDescription | ALTERNATE_LINE_DESCRIPTION | — | ✅ |
| 2 | AlternateLineFlag | ALTERNATE_LINE_FLAG | — | — |
| 3 | AwardDate | AWARD_DATE | — | — |
| 4 | PromisedDeliveryDate | PROMISED_DELIVERY_DATE | — | ✅ |
| 5 | PromisedShipDate | PROMISED_SHIP_DATE | — | ✅ |
| 6 | ResponseLineAdvanceAmount | ADVANCE_AMOUNT | — | — |
| 7 | ResponseLineAuctionHeaderId | AUCTION_HEADER_ID | — | — |
| 8 | ResponseLineAwardDate | AWARD_DATE | — | — |
| 9 | ResponseLineAwardPrice | AWARD_PRICE | — | ✅ |
| 10 | ResponseLineAwardQuantity | AWARD_QUANTITY | — | — |
| 11 | ResponseLineAwardShipmentNumber | AWARD_SHIPMENT_NUMBER | — | — |
| 12 | ResponseLineAwardStatus | AWARD_STATUS | — | — |
| 13 | ResponseLineBatchId | BATCH_ID | — | — |
| 14 | ResponseLineBidCurrAdvanceAmount | BID_CURR_ADVANCE_AMOUNT | — | — |
| 15 | ResponseLineBidCurrMaxRetainageAmt | BID_CURR_MAX_RETAINAGE_AMT | — | — |
| 16 | ResponseLineBidCurrencyLimitPrice | BID_CURRENCY_LIMIT_PRICE | — | — |
| 17 | ResponseLineBidCurrencyPrice | BID_CURRENCY_PRICE | — | — |
| 18 | ResponseLineBidCurrencyTransPrice | BID_CURRENCY_TRANS_PRICE | — | — |
| 19 | ResponseLineBidCurrencyUnitPrice | BID_CURRENCY_UNIT_PRICE | — | ✅ |
| 20 | ResponseLineBidNumber | BID_NUMBER | — | — |
| 21 | ResponseLineBidStartPrice | BID_START_PRICE | — | ✅ |
| 22 | ResponseLineCancelledLimitPrice | CANCELLED_LIMIT_PRICE | — | — |
| 23 | ResponseLineCopyPriceForProxyFlag | COPY_PRICE_FOR_PROXY_FLAG | — | — |
| 24 | ResponseLineCreatedBy | CREATED_BY | — | — |
| 25 | ResponseLineCreationDate | CREATION_DATE | — | — |
| 26 | ResponseLineDisplayPriceFactorsFlag | DISPLAY_PRICE_FACTORS_FLAG | — | — |
| 27 | ResponseLineDocumentDispLineNumber | DOCUMENT_DISP_LINE_NUMBER | — | ✅ |
| 28 | ResponseLineFirstBidPrice | FIRST_BID_PRICE | — | — |
| 29 | ResponseLineFixedAmountComponent | FIXED_AMOUNT_COMPONENT | — | — |
| 30 | ResponseLineGroupAmount | GROUP_AMOUNT | — | — |
| 31 | ResponseLineHasAttributesFlag | HAS_ATTRIBUTES_FLAG | — | — |
| 32 | ResponseLineHasBidFlag | HAS_BID_FLAG | — | ✅ |
| 33 | ResponseLineHasBidPaymentsFlag | HAS_BID_PAYMENTS_FLAG | — | — |
| 34 | ResponseLineHasPriceDifferentialsFlag | HAS_PRICE_DIFFERENTIALS_FLAG | — | — |
| 35 | ResponseLineHasQuantityTiers | HAS_QUANTITY_TIERS | — | — |
| 36 | ResponseLineHasShipmentsFlag | HAS_SHIPMENTS_FLAG | — | — |
| 37 | ResponseLineInterfaceLineId | INTERFACE_LINE_ID | — | — |
| 38 | ResponseLineIsChangedLineFlag | IS_CHANGED_LINE_FLAG | — | — |
| 39 | ResponseLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 40 | ResponseLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 41 | ResponseLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 42 | ResponseLineLineNumber | LINE_NUMBER | — | — |
| 43 | ResponseLineMaxRetainageAmount | MAX_RETAINAGE_AMOUNT | — | — |
| 44 | ResponseLineNoteToAuctionOwner | NOTE_TO_AUCTION_OWNER | — | ✅ |
| 45 | ResponseLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 46 | ResponseLineOldBidCurrAdvanceAmount | OLD_BID_CURR_ADVANCE_AMOUNT | — | — |
| 47 | ResponseLineOldBidCurrMaxRetainageAmt | OLD_BID_CURR_MAX_RETAINAGE_AMT | — | — |
| 48 | ResponseLineOldBidCurrencyLimitPrice | OLD_BID_CURRENCY_LIMIT_PRICE | — | — |
| 49 | ResponseLineOldBidCurrencyPrice | OLD_BID_CURRENCY_PRICE | — | — |
| 50 | ResponseLineOldBidCurrencyUnitPrice | OLD_BID_CURRENCY_UNIT_PRICE | — | — |
| 51 | ResponseLineOldNoOfPayments | OLD_NO_OF_PAYMENTS | — | — |
| 52 | ResponseLineOldNoteToAuctionOwner | OLD_NOTE_TO_AUCTION_OWNER | — | — |
| 53 | ResponseLineOldPoBidMinRelAmount | OLD_PO_BID_MIN_REL_AMOUNT | — | — |
| 54 | ResponseLineOldPrice | OLD_PRICE | — | — |
| 55 | ResponseLineOldProgressPymtRatePercent | OLD_PROGRESS_PYMT_RATE_PERCENT | — | — |
| 56 | ResponseLineOldPromisedDate | OLD_PROMISED_DATE | — | — |
| 57 | ResponseLineOldPublishDate | OLD_PUBLISH_DATE | — | — |
| 58 | ResponseLineOldQuantity | OLD_QUANTITY | — | — |
| 59 | ResponseLineOldRecoupmentRatePercent | OLD_RECOUPMENT_RATE_PERCENT | — | — |
| 60 | ResponseLineOldRetainageRatePercent | OLD_RETAINAGE_RATE_PERCENT | — | — |
| 61 | ResponseLinePerUnitPriceComponent | PER_UNIT_PRICE_COMPONENT | — | ✅ |
| 62 | ResponseLinePoBidMinRelAmount | PO_BID_MIN_REL_AMOUNT | — | ✅ |
| 63 | ResponseLinePoMinRelAmount | PO_MIN_REL_AMOUNT | — | ✅ |
| 64 | ResponseLinePrice | PRICE | — | — |
| 65 | ResponseLinePriceBreakType | PRICE_BREAK_TYPE | — | — |
| 66 | ResponseLinePriceDiffShipmentNumber | PRICE_DIFF_SHIPMENT_NUMBER | — | — |
| 67 | ResponseLineProgramAppName | PROGRAM_APP_NAME | — | — |
| 68 | ResponseLineProgramName | PROGRAM_NAME | — | — |
| 69 | ResponseLineProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 70 | ResponseLineProgressPymtRatePercent | PROGRESS_PYMT_RATE_PERCENT | — | — |
| 71 | ResponseLinePromisedDate | PROMISED_DATE | — | ✅ |
| 72 | ResponseLineProxyBidFlag | PROXY_BID_FLAG | — | ✅ |
| 73 | ResponseLineProxyBidLimitPrice | PROXY_BID_LIMIT_PRICE | — | ✅ |
| 74 | ResponseLinePublishDate | PUBLISH_DATE | — | — |
| 75 | ResponseLineQuantity | QUANTITY | — | ✅ |
| 76 | ResponseLineRank | RANK | — | ✅ |
| 77 | ResponseLineRecoupmentRatePercent | RECOUPMENT_RATE_PERCENT | — | — |
| 78 | ResponseLineRequestId | REQUEST_ID | — | — |
| 79 | ResponseLineRetainageRatePercent | RETAINAGE_RATE_PERCENT | — | — |
| 80 | ResponseLineTotalWeightedScore | TOTAL_WEIGHTED_SCORE | — | ✅ |
| 81 | ResponseLineTriggerBidNumber | TRIGGER_BID_NUMBER | — | — |
| 82 | ResponseLineUnitPrice | UNIT_PRICE | — | ✅ |
| 83 | ResponseLineWorksheetName | WORKSHEET_NAME | — | — |
| 84 | ResponseLineWorksheetSequenceNumber | WORKSHEET_SEQUENCE_NUMBER | — | — |
| 85 | UomConversionFactor | UOM_CONVERSION_FACTOR | — | — |

### [[pon_bid_po_lines|PON_BID_PO_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AuctionLineNumber | AUCTION_LINE_NUMBER | — | — |
| 2 | BidNumber | BID_NUMBER | 🔑 | ✅ |
| 3 | ItemDescription | ITEM_DESCRIPTION | — | — |
| 4 | ItemId | ITEM_ID | — | — |
| 5 | ItemRevision | ITEM_REVISION | — | — |
| 6 | LineNumber | LINE_NUMBER | 🔑 | ✅ |
| 7 | ResponsePOLineAuctionHeaderId | AUCTION_HEADER_ID | — | — |
| 8 | ResponsePOLineCreatedBy | CREATED_BY | — | — |
| 9 | ResponsePOLineCreationDate | CREATION_DATE | — | — |
| 10 | ResponsePOLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | ResponsePOLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | ResponsePOLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | ResponsePOLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | ResponsePOLineQuantity | QUANTITY | — | ✅ |
| 15 | SequenceNumber | SEQUENCE_NUMBER | 🔑 | ✅ |

### [[pon_bid_po_numbers|PON_BID_PO_NUMBERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResponsePOAcceptanceRequiredFlag | ACCEPTANCE_REQUIRED_FLAG | — | — |
| 2 | ResponsePOAcknowledgementWithinDays | ACKNOWLEDGEMENT_WITHIN_DAYS | — | — |
| 3 | ResponsePOAgentId | AGENT_ID | — | — |
| 4 | ResponsePOAuctionHeaderId | AUCTION_HEADER_ID | — | — |
| 5 | ResponsePOAutomaticGenerateOrder | AUTOMATIC_GENERATE_ORDER | — | — |
| 6 | ResponsePOAutomaticSubmitForAppr | AUTOMATIC_SUBMIT_FOR_APPR | — | — |
| 7 | ResponsePOBidNumber | BID_NUMBER | — | — |
| 8 | ResponsePOCreatedBy | CREATED_BY | — | — |
| 9 | ResponsePOCreationDate | CREATION_DATE | — | — |
| 10 | ResponsePODefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 11 | ResponsePOForBackingRequisition | FOR_BACKING_REQUISITION | — | — |
| 12 | ResponsePOGroupRequisition | GROUP_REQUISITION | — | — |
| 13 | ResponsePOGroupRequisitionLines | GROUP_REQUISITION_LINES | — | — |
| 14 | ResponsePOInitiateApproval | INITIATE_APPROVAL | — | — |
| 15 | ResponsePOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | ResponsePOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | ResponsePOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | ResponsePONoteToSupplier | NOTE_TO_SUPPLIER | — | — |
| 19 | ResponsePOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | ResponsePOOrderNumber | ORDER_NUMBER | — | — |
| 21 | ResponsePOPoEndDate | PO_END_DATE | — | — |
| 22 | ResponsePOPoErrorCode | PO_ERROR_CODE | — | — |
| 23 | ResponsePOPoErrorMsg | PO_ERROR_MSG | — | — |
| 24 | ResponsePOPoHeaderId | PO_HEADER_ID | — | — |
| 25 | ResponsePOPoStartDate | PO_START_DATE | — | — |
| 26 | ResponsePOPoWfCreationRnd | PO_WF_CREATION_RND | — | — |
| 27 | ResponsePOReqBuId | REQ_BU_ID | — | — |
| 28 | ResponsePORetroPriceApplyUpdatesFlag | RETRO_PRICE_APPLY_UPDATES_FLAG | — | — |
| 29 | ResponsePORetroPriceCommUpdatesFlag | RETRO_PRICE_COMM_UPDATES_FLAG | — | — |
| 30 | ResponsePOSequenceNumber | SEQUENCE_NUMBER | — | — |
| 31 | ResponsePOTaxDocumentSubtype | TAX_DOCUMENT_SUBTYPE | — | — |
| 32 | ResponsePOUseNeedByDate | USE_NEED_BY_DATE | — | — |
| 33 | ResponsePOUseShipTo | USE_SHIP_TO | — | — |
| 34 | ResponsePOVendorSiteId | VENDOR_SITE_ID | — | — |

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
| 57 | InvoiceCloseCode | INVOICE_CLOSE_CODE | — | — |
| 58 | InvoiceCloseTolerance | INVOICE_CLOSE_TOLERANCE | — | — |
| 59 | LanguageCode | LANGUAGE_CODE | — | — |
| 60 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 61 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 62 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 63 | LineTypeId | LINE_TYPE_ID | — | — |
| 64 | ManualReceiptNumType | MANUAL_RECEIPT_NUM_TYPE | — | — |
| 65 | ManualReqNumType | MANUAL_REQ_NUM_TYPE | — | — |
| 66 | MatchOption | MATCH_OPTION | — | — |
| 67 | MaxAttachmentSize | MAX_ATTACHMENT_SIZE | — | — |
| 68 | MinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 69 | ModeOfTransport | MODE_OF_TRANSPORT | — | — |
| 70 | NegApprovalEnabledFlag | NEG_APPROVAL_ENABLED_FLAG | — | — |
| 71 | NextApproverLookupCode | NEXT_APPROVER_LOOKUP_CODE | — | — |
| 72 | NextNegotiationNumber | NEXT_NEGOTIATION_NUMBER | — | — |
| 73 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 74 | PrcBuId | PRC_BU_ID | — | — |
| 75 | PriceBreakLookupCode | PRICE_BREAK_LOOKUP_CODE | — | — |
| 76 | PriceChangeAmount | PRICE_CHANGE_AMOUNT | — | — |
| 77 | RankIndicator | RANK_INDICATOR | — | — |
| 78 | RankVisibleBlind | RANK_VISIBLE_BLIND | — | — |
| 79 | ReceiveCloseCode | RECEIVE_CLOSE_CODE | — | — |
| 80 | ReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | — |
| 81 | ReceivingFlag | RECEIVING_FLAG | — | — |
| 82 | RfqOnlySiteFlag | RFQ_ONLY_SITE_FLAG | — | — |
| 83 | ServiceLevel | SERVICE_LEVEL | — | — |
| 84 | StyleId | STYLE_ID | — | — |
| 85 | SupplierAuthoringAcceptance | SUPPLIER_AUTHORING_ACCEPTANCE | — | — |
| 86 | SupplierHistoryDuration | SUPPLIER_HISTORY_DURATION | — | — |
| 87 | SystemConfiguredFlag | SYSTEM_CONFIGURED_FLAG | — | — |
| 88 | TaxFromItemFlag | TAX_FROM_ITEM_FLAG | — | — |
| 89 | TaxFromShipToLocFlag | TAX_FROM_SHIP_TO_LOC_FLAG | — | — |
| 90 | TaxFromSystemFlag | TAX_FROM_SYSTEM_FLAG | — | — |
| 91 | TaxFromVendorFlag | TAX_FROM_VENDOR_FLAG | — | — |
| 92 | TaxFromVendorSiteFlag | TAX_FROM_VENDOR_SITE_FLAG | — | — |
| 93 | TaxHierItem | TAX_HIER_ITEM | — | — |
| 94 | TaxHierShipToLoc | TAX_HIER_SHIP_TO_LOC | — | — |
| 95 | TaxHierSystem | TAX_HIER_SYSTEM | — | — |
| 96 | TaxHierVendor | TAX_HIER_VENDOR | — | — |
| 97 | TaxHierVendorSite | TAX_HIER_VENDOR_SITE | — | — |
| 98 | TaxableFlag | TAXABLE_FLAG | — | — |
| 99 | TermsId | TERMS_ID | — | — |
| 100 | UseNeedByDate | USE_NEED_BY_DATE | — | — |
| 101 | UseSalesOrderNumberFlag | USE_SALES_ORDER_NUMBER_FLAG | — | — |
| 102 | UseShipTo | USE_SHIP_TO | — | — |
| 103 | UserDefinedReceiptNumCode | USER_DEFINED_RECEIPT_NUM_CODE | — | — |
| 104 | UserDefinedReqNumCode | USER_DEFINED_REQ_NUM_CODE | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
