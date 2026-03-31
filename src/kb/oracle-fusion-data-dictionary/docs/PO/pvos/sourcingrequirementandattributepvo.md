---
id: DOC-PO-PVO-SourcingRequirementAndAttributePVO
doc_type: system-doc
title: "SourcingRequirementAndAttributePVO — PVO Purchasing"
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
  - SourcingRequirementAndAttributePVO
  - sourcingrequirementandattributepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SourcingRequirementAndAttributePVO

## 📌 Visão Geral

Extrai requisitos e atributos configurados para processos de sourcing, definindo critérios técnicos e comerciais de avaliação. Suporta análise de complexidade e padronização de processos competitivos.

**Caminho:** `FscmTopModelAM.PrcPonPublicViewAM.SourcingRequirementAndAttributePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 489 | 8 | 4 | 85 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[egp_categories_vl|EGP_CATEGORIES_VL]] — 8 atributos (3 BICC)
- [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]] — 6 atributos
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 16 atributos (1 BICC)
- [[pon_auction_attributes|PON_AUCTION_ATTRIBUTES]] — 34 atributos (4 PKs, 25 BICC)
- [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]] — 222 atributos (34 BICC)
- [[pon_auction_item_prices_all|PON_AUCTION_ITEM_PRICES_ALL]] — 96 atributos (21 BICC)
- [[pon_auction_sections|PON_AUCTION_SECTIONS]] — 3 atributos (1 BICC)
- [[po_system_parameters_all|PO_SYSTEM_PARAMETERS_ALL]] — 104 atributos

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
| 1 | ItemInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 2 | ItemInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 3 | ItemItemNumber | ITEM_NUMBER | — | — |
| 4 | ItemItemType | ITEM_TYPE | — | — |
| 5 | ItemOrganizationId | ORGANIZATION_ID | — | — |
| 6 | ItemPrimaryUomCode | PRIMARY_UOM_CODE | — | — |

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

### [[pon_auction_attributes|PON_AUCTION_ATTRIBUTES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AttributeListId | ATTRIBUTE_LIST_ID | 🔑 | ✅ |
| 2 | AuctionHeaderId | AUCTION_HEADER_ID | 🔑 | ✅ |
| 3 | LineNumber | LINE_NUMBER | 🔑 | ✅ |
| 4 | SequenceNumber | SEQUENCE_NUMBER | 🔑 | ✅ |
| 5 | SourcingReqAttAttrDispSeqNumber | ATTR_DISP_SEQ_NUMBER | — | ✅ |
| 6 | SourcingReqAttAttrGroupSeqNumber | ATTR_GROUP_SEQ_NUMBER | — | ✅ |
| 7 | SourcingReqAttAttrLevel | ATTR_LEVEL | — | ✅ |
| 8 | SourcingReqAttAttrMaxScore | ATTR_MAX_SCORE | — | ✅ |
| 9 | SourcingReqAttAttributeName | ATTRIBUTE_NAME | — | ✅ |
| 10 | SourcingReqAttCreatedBy | CREATED_BY | — | ✅ |
| 11 | SourcingReqAttCreationDate | CREATION_DATE | — | ✅ |
| 12 | SourcingReqAttDatatype | DATATYPE | — | ✅ |
| 13 | SourcingReqAttDateValue | DATE_VALUE | — | ✅ |
| 14 | SourcingReqAttDisplayTargetFlag | DISPLAY_TARGET_FLAG | — | ✅ |
| 15 | SourcingReqAttIpCategoryId | IP_CATEGORY_ID | — | ✅ |
| 16 | SourcingReqAttIpDescriptorId | IP_DESCRIPTOR_ID | — | ✅ |
| 17 | SourcingReqAttKnockoutScore | KNOCKOUT_SCORE | — | ✅ |
| 18 | SourcingReqAttLastAmendmentUpdate | LAST_AMENDMENT_UPDATE | — | — |
| 19 | SourcingReqAttLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | SourcingReqAttLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | SourcingReqAttLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 22 | SourcingReqAttModifiedDate | MODIFIED_DATE | — | — |
| 23 | SourcingReqAttModifiedFlag | MODIFIED_FLAG | — | — |
| 24 | SourcingReqAttNumberValue | NUMBER_VALUE | — | ✅ |
| 25 | SourcingReqAttObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 26 | SourcingReqAttProgramAppName | PROGRAM_APP_NAME | — | — |
| 27 | SourcingReqAttProgramName | PROGRAM_NAME | — | — |
| 28 | SourcingReqAttRequestId | REQUEST_ID | — | — |
| 29 | SourcingReqAttResponseType | RESPONSE_TYPE | — | ✅ |
| 30 | SourcingReqAttScoringMethod | SCORING_METHOD | — | ✅ |
| 31 | SourcingReqAttScoringType | SCORING_TYPE | — | ✅ |
| 32 | SourcingReqAttSectionName | SECTION_NAME | — | ✅ |
| 33 | SourcingReqAttTextValue | TEXT_VALUE | — | ✅ |
| 34 | SourcingReqAttWeight | WEIGHT | — | ✅ |

### [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationHeaderAbstractDetails | ABSTRACT_DETAILS | — | — |
| 2 | NegotiationHeaderAbstractStatus | ABSTRACT_STATUS | — | — |
| 3 | NegotiationHeaderAdvanceNegotiableFlag | ADVANCE_NEGOTIABLE_FLAG | — | — |
| 4 | NegotiationHeaderAllowAlternateLines | ALLOW_ALTERNATE_LINES | — | ✅ |
| 5 | NegotiationHeaderAllowOtherBidCurrencyFlag | ALLOW_OTHER_BID_CURRENCY_FLAG | — | — |
| 6 | NegotiationHeaderAmendmentDescription | AMENDMENT_DESCRIPTION | — | — |
| 7 | NegotiationHeaderAmendmentNumber | AMENDMENT_NUMBER | — | — |
| 8 | NegotiationHeaderApprovalAmount | APPROVAL_AMOUNT | — | ✅ |
| 9 | NegotiationHeaderApprovalStatus | NEG_APPROVAL_STATUS | — | — |
| 10 | NegotiationHeaderAttributeLineNumber | ATTRIBUTE_LINE_NUMBER | — | — |
| 11 | NegotiationHeaderAttributesExist | ATTRIBUTES_EXIST | — | — |
| 12 | NegotiationHeaderAuctionHeaderId | AUCTION_HEADER_ID | — | — |
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
| 32 | NegotiationHeaderAwardApprovalFlag | AWARD_APPROVAL_FLAG | — | — |
| 33 | NegotiationHeaderAwardApprovalStatus | AWARD_APPROVAL_STATUS | — | — |
| 34 | NegotiationHeaderAwardByDate | AWARD_BY_DATE | — | ✅ |
| 35 | NegotiationHeaderAwardCompleteDate | AWARD_COMPLETE_DATE | — | ✅ |
| 36 | NegotiationHeaderAwardDate | AWARD_DATE | — | ✅ |
| 37 | NegotiationHeaderAwardMode | AWARD_MODE | — | — |
| 38 | NegotiationHeaderAwardStatus | AWARD_STATUS | — | ✅ |
| 39 | NegotiationHeaderBidDecrementMethod | BID_DECREMENT_METHOD | — | — |
| 40 | NegotiationHeaderBidFrequencyCode | BID_FREQUENCY_CODE | — | — |
| 41 | NegotiationHeaderBidListType | BID_LIST_TYPE | — | — |
| 42 | NegotiationHeaderBidRanking | BID_RANKING | — | ✅ |
| 43 | NegotiationHeaderBidScopeCode | BID_SCOPE_CODE | — | — |
| 44 | NegotiationHeaderBidVisibilityCode | BID_VISIBILITY_CODE | — | ✅ |
| 45 | NegotiationHeaderBuyerTransportEnabledFlag | BUYER_TRANSPORT_ENABLED_FLAG | — | — |
| 46 | NegotiationHeaderBuyerTransportFlag | BUYER_TRANSPORT_FLAG | — | ✅ |
| 47 | NegotiationHeaderCancelDate | CANCEL_DATE | — | — |
| 48 | NegotiationHeaderCarrierId | CARRIER_ID | — | — |
| 49 | NegotiationHeaderCloseBiddingDate | CLOSE_BIDDING_DATE | — | ✅ |
| 50 | NegotiationHeaderCloseDateType | CLOSE_DATE_TYPE | — | — |
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
| 61 | NegotiationHeaderDaysAfterOpenDate | DAYS_AFTER_OPEN_DATE | — | — |
| 62 | NegotiationHeaderDescription | DESCRIPTION | — | — |
| 63 | NegotiationHeaderDisplayBestPriceBlindFlag | DISPLAY_BEST_PRICE_BLIND_FLAG | — | — |
| 64 | NegotiationHeaderDoctypeId | DOCTYPE_ID | — | — |
| 65 | NegotiationHeaderDocumentNumber | DOCUMENT_NUMBER | — | ✅ |
| 66 | NegotiationHeaderDraftLocked | DRAFT_LOCKED | — | — |
| 67 | NegotiationHeaderDraftLockedDate | DRAFT_LOCKED_DATE | — | — |
| 68 | NegotiationHeaderDraftUnlockedDate | DRAFT_UNLOCKED_DATE | — | — |
| 69 | NegotiationHeaderEnforcePrevrndBidPriceFlag | ENFORCE_PREVRND_BID_PRICE_FLAG | — | — |
| 70 | NegotiationHeaderEventId | EVENT_ID | — | — |
| 71 | NegotiationHeaderEventTitle | EVENT_TITLE | — | — |
| 72 | NegotiationHeaderExtAttribute1 | EXT_ATTRIBUTE1 | — | — |
| 73 | NegotiationHeaderExtAttribute10 | EXT_ATTRIBUTE10 | — | — |
| 74 | NegotiationHeaderExtAttribute11 | EXT_ATTRIBUTE11 | — | — |
| 75 | NegotiationHeaderExtAttribute12 | EXT_ATTRIBUTE12 | — | — |
| 76 | NegotiationHeaderExtAttribute13 | EXT_ATTRIBUTE13 | — | — |
| 77 | NegotiationHeaderExtAttribute14 | EXT_ATTRIBUTE14 | — | — |
| 78 | NegotiationHeaderExtAttribute15 | EXT_ATTRIBUTE15 | — | — |
| 79 | NegotiationHeaderExtAttribute2 | EXT_ATTRIBUTE2 | — | — |
| 80 | NegotiationHeaderExtAttribute3 | EXT_ATTRIBUTE3 | — | — |
| 81 | NegotiationHeaderExtAttribute4 | EXT_ATTRIBUTE4 | — | — |
| 82 | NegotiationHeaderExtAttribute5 | EXT_ATTRIBUTE5 | — | — |
| 83 | NegotiationHeaderExtAttribute6 | EXT_ATTRIBUTE6 | — | — |
| 84 | NegotiationHeaderExtAttribute7 | EXT_ATTRIBUTE7 | — | — |
| 85 | NegotiationHeaderExtAttribute8 | EXT_ATTRIBUTE8 | — | — |
| 86 | NegotiationHeaderExtAttribute9 | EXT_ATTRIBUTE9 | — | — |
| 87 | NegotiationHeaderExtAttributeCategory | EXT_ATTRIBUTE_CATEGORY | — | — |
| 88 | NegotiationHeaderFirstLineCloseDate | FIRST_LINE_CLOSE_DATE | — | — |
| 89 | NegotiationHeaderFobCode | FOB_CODE | — | — |
| 90 | NegotiationHeaderFreightTermsCode | FREIGHT_TERMS_CODE | — | — |
| 91 | NegotiationHeaderFullQuantityBidCode | FULL_QUANTITY_BID_CODE | — | — |
| 92 | NegotiationHeaderGlobalTemplateFlag | GLOBAL_TEMPLATE_FLAG | — | — |
| 93 | NegotiationHeaderGroupEnabledFlag | GROUP_ENABLED_FLAG | — | — |
| 94 | NegotiationHeaderHasHdrAttrFlag | HAS_HDR_ATTR_FLAG | — | — |
| 95 | NegotiationHeaderHasItemsFlag | HAS_ITEMS_FLAG | — | — |
| 96 | NegotiationHeaderHasPeForAllItems | HAS_PE_FOR_ALL_ITEMS | — | — |
| 97 | NegotiationHeaderHasPriceElements | HAS_PRICE_ELEMENTS | — | — |
| 98 | NegotiationHeaderHasScoringTeamsFlag | HAS_SCORING_TEAMS_FLAG | — | — |
| 99 | NegotiationHeaderHdrAttrDisplayScore | HDR_ATTR_DISPLAY_SCORE | — | ✅ |
| 100 | NegotiationHeaderHdrAttrEnableWeights | HDR_ATTR_ENABLE_WEIGHTS | — | ✅ |
| 101 | NegotiationHeaderHdrAttrMaximumScore | HDR_ATTR_MAXIMUM_SCORE | — | — |
| 102 | NegotiationHeaderHdrAttributeEnabledFlag | HDR_ATTRIBUTE_ENABLED_FLAG | — | — |
| 103 | NegotiationHeaderImportFileName | IMPORT_FILE_NAME | — | — |
| 104 | NegotiationHeaderIncludePdfInExternalPage | INCLUDE_PDF_IN_EXTERNAL_PAGE | — | — |
| 105 | NegotiationHeaderIntAttribute1 | INT_ATTRIBUTE1 | — | — |
| 106 | NegotiationHeaderIntAttribute10 | INT_ATTRIBUTE10 | — | — |
| 107 | NegotiationHeaderIntAttribute11 | INT_ATTRIBUTE11 | — | — |
| 108 | NegotiationHeaderIntAttribute12 | INT_ATTRIBUTE12 | — | — |
| 109 | NegotiationHeaderIntAttribute13 | INT_ATTRIBUTE13 | — | — |
| 110 | NegotiationHeaderIntAttribute14 | INT_ATTRIBUTE14 | — | — |
| 111 | NegotiationHeaderIntAttribute15 | INT_ATTRIBUTE15 | — | — |
| 112 | NegotiationHeaderIntAttribute2 | INT_ATTRIBUTE2 | — | — |
| 113 | NegotiationHeaderIntAttribute3 | INT_ATTRIBUTE3 | — | — |
| 114 | NegotiationHeaderIntAttribute4 | INT_ATTRIBUTE4 | — | — |
| 115 | NegotiationHeaderIntAttribute5 | INT_ATTRIBUTE5 | — | — |
| 116 | NegotiationHeaderIntAttribute6 | INT_ATTRIBUTE6 | — | — |
| 117 | NegotiationHeaderIntAttribute7 | INT_ATTRIBUTE7 | — | — |
| 118 | NegotiationHeaderIntAttribute8 | INT_ATTRIBUTE8 | — | — |
| 119 | NegotiationHeaderIntAttribute9 | INT_ATTRIBUTE9 | — | — |
| 120 | NegotiationHeaderIntAttributeCategory | INT_ATTRIBUTE_CATEGORY | — | — |
| 121 | NegotiationHeaderIsPaused | IS_PAUSED | — | — |
| 122 | NegotiationHeaderIsTemplateFlag | IS_TEMPLATE_FLAG | — | — |
| 123 | NegotiationHeaderLanguageCode | LANGUAGE_CODE | — | — |
| 124 | NegotiationHeaderLargeNegEnabledFlag | LARGE_NEG_ENABLED_FLAG | — | — |
| 125 | NegotiationHeaderLastLineNumber | LAST_LINE_NUMBER | — | — |
| 126 | NegotiationHeaderLastPauseDate | LAST_PAUSE_DATE | — | — |
| 127 | NegotiationHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 128 | NegotiationHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 129 | NegotiationHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 130 | NegotiationHeaderLineAttributeEnabledFlag | LINE_ATTRIBUTE_ENABLED_FLAG | — | — |
| 131 | NegotiationHeaderLineMasEnabledFlag | LINE_MAS_ENABLED_FLAG | — | — |
| 132 | NegotiationHeaderLotEnabledFlag | LOT_ENABLED_FLAG | — | — |
| 133 | NegotiationHeaderMaxBidColorSequenceId | MAX_BID_COLOR_SEQUENCE_ID | — | — |
| 134 | NegotiationHeaderMaxDocumentLineNum | MAX_DOCUMENT_LINE_NUM | — | — |
| 135 | NegotiationHeaderMaxInternalLineNum | MAX_INTERNAL_LINE_NUM | — | — |
| 136 | NegotiationHeaderMaxRetainageNegotiableFlag | MAX_RETAINAGE_NEGOTIABLE_FLAG | — | — |
| 137 | NegotiationHeaderMinBidChangeType | MIN_BID_CHANGE_TYPE | — | — |
| 138 | NegotiationHeaderMinBidDecrement | MIN_BID_DECREMENT | — | — |
| 139 | NegotiationHeaderModeOfTransport | MODE_OF_TRANSPORT | — | ✅ |
| 140 | NegotiationHeaderNegApprovalDate | NEG_APPROVAL_DATE | — | — |
| 141 | NegotiationHeaderNegApprovalEnabledFlag | NEG_APPROVAL_ENABLED_FLAG | — | — |
| 142 | NegotiationHeaderNegTeamEnabledFlag | NEG_TEAM_ENABLED_FLAG | — | — |
| 143 | NegotiationHeaderNumberOfBids | NUMBER_OF_BIDS | — | — |
| 144 | NegotiationHeaderNumberOfExtensions | NUMBER_OF_EXTENSIONS | — | — |
| 145 | NegotiationHeaderNumberOfLines | NUMBER_OF_LINES | — | — |
| 146 | NegotiationHeaderNumberPriceDecimals | NUMBER_PRICE_DECIMALS | — | ✅ |
| 147 | NegotiationHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 148 | NegotiationHeaderOpenAuctionNowFlag | OPEN_AUCTION_NOW_FLAG | — | ✅ |
| 149 | NegotiationHeaderOpenBiddingDate | OPEN_BIDDING_DATE | — | ✅ |
| 150 | NegotiationHeaderOriginalCloseBiddingDate | ORIGINAL_CLOSE_BIDDING_DATE | — | — |
| 151 | NegotiationHeaderOutcomeStatus | OUTCOME_STATUS | — | — |
| 152 | NegotiationHeaderPauseRemarks | PAUSE_REMARKS | — | — |
| 153 | NegotiationHeaderPaymentTermsId | PAYMENT_TERMS_ID | — | — |
| 154 | NegotiationHeaderPersonId | PERSON_ID | — | — |
| 155 | NegotiationHeaderPfTypeAllowed | PF_TYPE_ALLOWED | — | — |
| 156 | NegotiationHeaderPoAgreedAmount | PO_AGREED_AMOUNT | — | ✅ |
| 157 | NegotiationHeaderPoEndDate | PO_END_DATE | — | ✅ |
| 158 | NegotiationHeaderPoMinRelAmount | PO_MIN_REL_AMOUNT | — | ✅ |
| 159 | NegotiationHeaderPoStartDate | PO_START_DATE | — | ✅ |
| 160 | NegotiationHeaderPoStyleId | PO_STYLE_ID | — | — |
| 161 | NegotiationHeaderPowerBiddingEnabledFlag | POWER_BIDDING_ENABLED_FLAG | — | — |
| 162 | NegotiationHeaderPrcBuId | PRC_BU_ID | — | — |
| 163 | NegotiationHeaderPriceDrivenAuctionFlag | PRICE_DRIVEN_AUCTION_FLAG | — | — |
| 164 | NegotiationHeaderPriceElementEnabledFlag | PRICE_ELEMENT_ENABLED_FLAG | — | — |
| 165 | NegotiationHeaderPriceTiersIndicator | PRICE_TIERS_INDICATOR | — | ✅ |
| 166 | NegotiationHeaderProgramAppName | PROGRAM_APP_NAME | — | — |
| 167 | NegotiationHeaderProgramName | PROGRAM_NAME | — | — |
| 168 | NegotiationHeaderProgressPaymentType | PROGRESS_PAYMENT_TYPE | — | — |
| 169 | NegotiationHeaderProgressPymtNegotiableFlag | PROGRESS_PYMT_NEGOTIABLE_FLAG | — | — |
| 170 | NegotiationHeaderProjectId | PROJECT_ID | — | — |
| 171 | NegotiationHeaderProxyBiddingEnabledFlag | PROXY_BIDDING_ENABLED_FLAG | — | — |
| 172 | NegotiationHeaderPublishAuctionNowFlag | PUBLISH_AUCTION_NOW_FLAG | — | — |
| 173 | NegotiationHeaderPublishDate | PUBLISH_DATE | — | ✅ |
| 174 | NegotiationHeaderPublishDateOrigAmend | PUBLISH_DATE_ORIG_AMEND | — | — |
| 175 | NegotiationHeaderPublishRatesToBiddersFlag | PUBLISH_RATES_TO_BIDDERS_FLAG | — | — |
| 176 | NegotiationHeaderQtyPriceTiersEnabledFlag | QTY_PRICE_TIERS_ENABLED_FLAG | — | — |
| 177 | NegotiationHeaderRankIndicator | RANK_INDICATOR | — | ✅ |
| 178 | NegotiationHeaderRateDate | RATE_DATE | — | — |
| 179 | NegotiationHeaderRateType | RATE_TYPE | — | — |
| 180 | NegotiationHeaderRecoupmentNegotiableFlag | RECOUPMENT_NEGOTIABLE_FLAG | — | — |
| 181 | NegotiationHeaderReminderDate | REMINDER_DATE | — | — |
| 182 | NegotiationHeaderRequestDate | REQUEST_DATE | — | — |
| 183 | NegotiationHeaderRequestId | REQUEST_ID | — | — |
| 184 | NegotiationHeaderRequestedBy | REQUESTED_BY | — | — |
| 185 | NegotiationHeaderRetainageNegotiableFlag | RETAINAGE_NEGOTIABLE_FLAG | — | — |
| 186 | NegotiationHeaderRfiLineEnabledFlag | RFI_LINE_ENABLED_FLAG | — | — |
| 187 | NegotiationHeaderScoringLockDate | SCORING_LOCK_DATE | — | — |
| 188 | NegotiationHeaderSealedActualUnlockDate | SEALED_ACTUAL_UNLOCK_DATE | — | — |
| 189 | NegotiationHeaderSealedActualUnsealDate | SEALED_ACTUAL_UNSEAL_DATE | — | — |
| 190 | NegotiationHeaderSealedAuctionStatus | SEALED_AUCTION_STATUS | — | — |
| 191 | NegotiationHeaderServiceLevel | SERVICE_LEVEL | — | ✅ |
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
| 213 | NegotiationHeaderTwoPartFlag | TWO_PART_FLAG | — | ✅ |
| 214 | NegotiationHeaderTwostageEvalEnabledFlag | TWOSTAGE_EVAL_ENABLED_FLAG | — | — |
| 215 | NegotiationHeaderVersionNum | VERSION_NUM | — | — |
| 216 | NegotiationHeaderViewByDate | VIEW_BY_DATE | — | ✅ |
| 217 | NegotiationHeaderWfApprovalItemKey | WF_APPROVAL_ITEM_KEY | — | — |
| 218 | NegotiationHeaderWfAwardApprovalItemKey | WF_AWARD_APPROVAL_ITEM_KEY | — | — |
| 219 | NegotiationHeaderWfItemKey | WF_ITEM_KEY | — | — |
| 220 | NegotiationHeaderWfPoncomplCurrentRound | WF_PONCOMPL_CURRENT_ROUND | — | — |
| 221 | NegotiationHeaderWfPoncomplItemKey | WF_PONCOMPL_ITEM_KEY | — | — |
| 222 | NegotiationHeaderWfRoleName | WF_ROLE_NAME | — | — |

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
| 12 | NegotiationLineBestBidCurrencyCode | BEST_BID_CURRENCY_CODE | — | — |
| 13 | NegotiationLineBestBidCurrencyPrice | BEST_BID_CURRENCY_PRICE | — | — |
| 14 | NegotiationLineBestBidFirstBidPrice | BEST_BID_FIRST_BID_PRICE | — | — |
| 15 | NegotiationLineBestBidNumber | BEST_BID_NUMBER | — | — |
| 16 | NegotiationLineBestBidPrice | BEST_BID_PRICE | — | — |
| 17 | NegotiationLineBestBidPromisedDate | BEST_BID_PROMISED_DATE | — | — |
| 18 | NegotiationLineBestBidProxyLimitPrice | BEST_BID_PROXY_LIMIT_PRICE | — | — |
| 19 | NegotiationLineBestBidQuantity | BEST_BID_QUANTITY | — | — |
| 20 | NegotiationLineBestBidScore | BEST_BID_SCORE | — | — |
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
| 82 | NegotiationLineRequestedDeliveryDate | REQUESTED_DELIVERY_DATE | — | ✅ |
| 83 | NegotiationLineRequestedShipDate | REQUESTED_SHIP_DATE | — | ✅ |
| 84 | NegotiationLineRequisitionNumber | REQUISITION_NUMBER | — | ✅ |
| 85 | NegotiationLineRetainageRatePercent | RETAINAGE_RATE_PERCENT | — | — |
| 86 | NegotiationLineShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 87 | NegotiationLineSourceDocId | SOURCE_DOC_ID | — | — |
| 88 | NegotiationLineSourceDocNumber | SOURCE_DOC_NUMBER | — | ✅ |
| 89 | NegotiationLineSourceLineId | SOURCE_LINE_ID | — | — |
| 90 | NegotiationLineSourceLineNumber | SOURCE_LINE_NUMBER | — | ✅ |
| 91 | NegotiationLineSubLineSequenceNumber | SUB_LINE_SEQUENCE_NUMBER | — | — |
| 92 | NegotiationLineTargetPrice | TARGET_PRICE | — | ✅ |
| 93 | NegotiationLineUnitDisplayTargetFlag | UNIT_DISPLAY_TARGET_FLAG | — | — |
| 94 | NegotiationLineUnitTargetPrice | UNIT_TARGET_PRICE | — | — |
| 95 | NegotiationLineUomCode | UOM_CODE | — | ✅ |
| 96 | NegotiationLineWorkApproverUserId | WORK_APPROVER_USER_ID | — | — |

### [[pon_auction_sections|PON_AUCTION_SECTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SourcingRequirementSectionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | SourcingRequirementSectionSectionId | SECTION_ID | — | — |
| 3 | SourcingRequirementSectionTwoPartSectionType | TWO_PART_SECTION_TYPE | — | ✅ |

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
| 60 | LastUpdateDate | LAST_UPDATE_DATE | — | — |
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
| 73 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
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
