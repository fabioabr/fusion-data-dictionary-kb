---
id: DOC-PO-PVO-NegotiationRespRequirementAndValuesPVO
doc_type: system-doc
title: "NegotiationRespRequirementAndValuesPVO — PVO Purchasing"
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
  - NegotiationRespRequirementAndValuesPVO
  - negotiationresprequirementandvaluespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationRespRequirementAndValuesPVO

## 📌 Visão Geral

Extrai requisitos e seus valores preenchidos nas respostas de fornecedores, com detalhes de seção e pontuação. Permite análise comparativa de atendimento a especificações técnicas.

**Caminho:** `FscmTopModelAM.PrcPonPublicViewAM.NegotiationRespRequirementAndValuesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 553 | 8 | 4 | 87 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]] — 332 atributos (1 PKs, 30 BICC)
- [[pon_bid_headers|PON_BID_HEADERS]] — 83 atributos (17 BICC)
- [[pon_bid_requirements|PON_BID_REQUIREMENTS]] — 20 atributos (7 BICC)
- [[pon_bid_requirement_values|PON_BID_REQUIREMENT_VALUES]] — 21 atributos (1 PKs, 10 BICC)
- [[pon_bid_sections|PON_BID_SECTIONS]] — 10 atributos (1 BICC)
- [[pon_requirements|PON_REQUIREMENTS]] — 45 atributos (13 BICC)
- [[pon_requirement_scores|PON_REQUIREMENT_SCORES]] — 25 atributos (1 PKs, 3 BICC)
- [[pon_requirement_sections|PON_REQUIREMENT_SECTIONS]] — 17 atributos (1 PKs, 6 BICC)

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
| 10 | NegotiationHeaderAttribute1 | ATTRIBUTE1 | — | — |
| 11 | NegotiationHeaderAttribute10 | ATTRIBUTE10 | — | — |
| 12 | NegotiationHeaderAttribute11 | ATTRIBUTE11 | — | — |
| 13 | NegotiationHeaderAttribute12 | ATTRIBUTE12 | — | — |
| 14 | NegotiationHeaderAttribute13 | ATTRIBUTE13 | — | — |
| 15 | NegotiationHeaderAttribute14 | ATTRIBUTE14 | — | — |
| 16 | NegotiationHeaderAttribute15 | ATTRIBUTE15 | — | — |
| 17 | NegotiationHeaderAttribute16 | ATTRIBUTE16 | — | — |
| 18 | NegotiationHeaderAttribute17 | ATTRIBUTE17 | — | — |
| 19 | NegotiationHeaderAttribute18 | ATTRIBUTE18 | — | — |
| 20 | NegotiationHeaderAttribute19 | ATTRIBUTE19 | — | — |
| 21 | NegotiationHeaderAttribute2 | ATTRIBUTE2 | — | — |
| 22 | NegotiationHeaderAttribute20 | ATTRIBUTE20 | — | — |
| 23 | NegotiationHeaderAttribute3 | ATTRIBUTE3 | — | — |
| 24 | NegotiationHeaderAttribute4 | ATTRIBUTE4 | — | — |
| 25 | NegotiationHeaderAttribute5 | ATTRIBUTE5 | — | — |
| 26 | NegotiationHeaderAttribute6 | ATTRIBUTE6 | — | — |
| 27 | NegotiationHeaderAttribute7 | ATTRIBUTE7 | — | — |
| 28 | NegotiationHeaderAttribute8 | ATTRIBUTE8 | — | — |
| 29 | NegotiationHeaderAttribute9 | ATTRIBUTE9 | — | — |
| 30 | NegotiationHeaderAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 31 | NegotiationHeaderAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 32 | NegotiationHeaderAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 33 | NegotiationHeaderAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 34 | NegotiationHeaderAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 35 | NegotiationHeaderAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 36 | NegotiationHeaderAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 37 | NegotiationHeaderAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 38 | NegotiationHeaderAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 39 | NegotiationHeaderAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 40 | NegotiationHeaderAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 41 | NegotiationHeaderAttributeLineNumber | ATTRIBUTE_LINE_NUMBER | — | — |
| 42 | NegotiationHeaderAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 43 | NegotiationHeaderAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 44 | NegotiationHeaderAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 45 | NegotiationHeaderAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 46 | NegotiationHeaderAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 47 | NegotiationHeaderAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 48 | NegotiationHeaderAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 49 | NegotiationHeaderAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 50 | NegotiationHeaderAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 51 | NegotiationHeaderAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 52 | NegotiationHeaderAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 53 | NegotiationHeaderAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 54 | NegotiationHeaderAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 55 | NegotiationHeaderAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 56 | NegotiationHeaderAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 57 | NegotiationHeaderAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 58 | NegotiationHeaderAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 59 | NegotiationHeaderAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 60 | NegotiationHeaderAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 61 | NegotiationHeaderAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 62 | NegotiationHeaderAttributesExist | ATTRIBUTES_EXIST | — | — |
| 63 | NegotiationHeaderAuctionHeaderId4 | AUCTION_HEADER_ID | 🔑 | ✅ |
| 64 | NegotiationHeaderAuctionHeaderIdOrigAmend | AUCTION_HEADER_ID_ORIG_AMEND | — | — |
| 65 | NegotiationHeaderAuctionHeaderIdOrigRound | AUCTION_HEADER_ID_ORIG_ROUND | — | — |
| 66 | NegotiationHeaderAuctionHeaderIdPrevAmend | AUCTION_HEADER_ID_PREV_AMEND | — | — |
| 67 | NegotiationHeaderAuctionHeaderIdPrevRound | AUCTION_HEADER_ID_PREV_ROUND | — | — |
| 68 | NegotiationHeaderAuctionOriginationCode | AUCTION_ORIGINATION_CODE | — | — |
| 69 | NegotiationHeaderAuctionRoundNumber | AUCTION_ROUND_NUMBER | — | ✅ |
| 70 | NegotiationHeaderAuctionStatus | AUCTION_STATUS | — | ✅ |
| 71 | NegotiationHeaderAuctionTitle | AUCTION_TITLE | — | ✅ |
| 72 | NegotiationHeaderAutoExtendAllLinesFlag | AUTO_EXTEND_ALL_LINES_FLAG | — | — |
| 73 | NegotiationHeaderAutoExtendDuration | AUTO_EXTEND_DURATION | — | — |
| 74 | NegotiationHeaderAutoExtendEnabledFlag | AUTO_EXTEND_ENABLED_FLAG | — | — |
| 75 | NegotiationHeaderAutoExtendFlag | AUTO_EXTEND_FLAG | — | — |
| 76 | NegotiationHeaderAutoExtendMinTriggerRank | AUTO_EXTEND_MIN_TRIGGER_RANK | — | — |
| 77 | NegotiationHeaderAutoExtendNumber | AUTO_EXTEND_NUMBER | — | — |
| 78 | NegotiationHeaderAutoExtendTypeFlag | AUTO_EXTEND_TYPE_FLAG | — | — |
| 79 | NegotiationHeaderAutoextendChangedFlag | AUTOEXTEND_CHANGED_FLAG | — | — |
| 80 | NegotiationHeaderAwardApprAmeTransId | AWARD_APPR_AME_TRANS_ID | — | — |
| 81 | NegotiationHeaderAwardApprAmeTransPrevId | AWARD_APPR_AME_TRANS_PREV_ID | — | — |
| 82 | NegotiationHeaderAwardApprAmeTxnDate | AWARD_APPR_AME_TXN_DATE | — | — |
| 83 | NegotiationHeaderAwardApprIdentificationKey | AWARD_APPR_IDENTIFICATION_KEY | — | — |
| 84 | NegotiationHeaderAwardApprovalDate | AWARD_APPROVAL_DATE | — | — |
| 85 | NegotiationHeaderAwardApprovalFlag | AWARD_APPROVAL_FLAG | — | — |
| 86 | NegotiationHeaderAwardApprovalNote | AWARD_APPROVAL_NOTE | — | — |
| 87 | NegotiationHeaderAwardApprovalStatus | AWARD_APPROVAL_STATUS | — | — |
| 88 | NegotiationHeaderAwardByDate | AWARD_BY_DATE | — | — |
| 89 | NegotiationHeaderAwardCompleteDate | AWARD_COMPLETE_DATE | — | ✅ |
| 90 | NegotiationHeaderAwardDate | AWARD_DATE | — | ✅ |
| 91 | NegotiationHeaderAwardMode | AWARD_MODE | — | — |
| 92 | NegotiationHeaderAwardStatus | AWARD_STATUS | — | — |
| 93 | NegotiationHeaderBidDecrementMethod | BID_DECREMENT_METHOD | — | — |
| 94 | NegotiationHeaderBidFrequencyCode | BID_FREQUENCY_CODE | — | — |
| 95 | NegotiationHeaderBidFrequencyCodeDspFlag | BID_FREQUENCY_CODE_DSP_FLAG | — | — |
| 96 | NegotiationHeaderBidListType | BID_LIST_TYPE | — | — |
| 97 | NegotiationHeaderBidListTypeDspFlag | BID_LIST_TYPE_DSP_FLAG | — | — |
| 98 | NegotiationHeaderBidRanking | BID_RANKING | — | ✅ |
| 99 | NegotiationHeaderBidRevisionType | BID_REVISION_TYPE | — | — |
| 100 | NegotiationHeaderBidRevisionTypeDspFlag | BID_REVISION_TYPE_DSP_FLAG | — | — |
| 101 | NegotiationHeaderBidScopeCode | BID_SCOPE_CODE | — | — |
| 102 | NegotiationHeaderBidScopeCodeDspFlag | BID_SCOPE_CODE_DSP_FLAG | — | — |
| 103 | NegotiationHeaderBidVisibilityCode | BID_VISIBILITY_CODE | — | ✅ |
| 104 | NegotiationHeaderBuyerTransportEnabledFlag | BUYER_TRANSPORT_ENABLED_FLAG | — | — |
| 105 | NegotiationHeaderBuyerTransportFlag | BUYER_TRANSPORT_FLAG | — | ✅ |
| 106 | NegotiationHeaderCancelDate | CANCEL_DATE | — | — |
| 107 | NegotiationHeaderCarrierId | CARRIER_ID | — | — |
| 108 | NegotiationHeaderCloseBiddingDate | CLOSE_BIDDING_DATE | — | ✅ |
| 109 | NegotiationHeaderCloseDateType | CLOSE_DATE_TYPE | — | — |
| 110 | NegotiationHeaderCompleteFlag | COMPLETE_FLAG | — | — |
| 111 | NegotiationHeaderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 112 | NegotiationHeaderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 113 | NegotiationHeaderContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 114 | NegotiationHeaderContractTemplateId | CONTRACT_TEMPLATE_ID | — | — |
| 115 | NegotiationHeaderContractType | CONTRACT_TYPE | — | — |
| 116 | NegotiationHeaderCreatedBy4 | CREATED_BY | — | — |
| 117 | NegotiationHeaderCreationDate4 | CREATION_DATE | — | — |
| 118 | NegotiationHeaderCreationDateOrigAmend | CREATION_DATE_ORIG_AMEND | — | — |
| 119 | NegotiationHeaderCurrencyCode | CURRENCY_CODE | — | ✅ |
| 120 | NegotiationHeaderDaysAfterOpenDate | DAYS_AFTER_OPEN_DATE | — | — |
| 121 | NegotiationHeaderDescription | DESCRIPTION | — | — |
| 122 | NegotiationHeaderDisplayBestPriceBlindFlag | DISPLAY_BEST_PRICE_BLIND_FLAG | — | — |
| 123 | NegotiationHeaderDisplayBestPriceDspFlag | DISPLAY_BEST_PRICE_DSP_FLAG | — | — |
| 124 | NegotiationHeaderDoctypeId | DOCTYPE_ID | — | — |
| 125 | NegotiationHeaderDocumentNumber | DOCUMENT_NUMBER | — | ✅ |
| 126 | NegotiationHeaderDraftLocked | DRAFT_LOCKED | — | — |
| 127 | NegotiationHeaderDraftLockedByPersonId | DRAFT_LOCKED_BY_PERSON_ID | — | — |
| 128 | NegotiationHeaderDraftLockedDate | DRAFT_LOCKED_DATE | — | — |
| 129 | NegotiationHeaderDraftUnlockedByPersonId | DRAFT_UNLOCKED_BY_PERSON_ID | — | — |
| 130 | NegotiationHeaderDraftUnlockedDate | DRAFT_UNLOCKED_DATE | — | — |
| 131 | NegotiationHeaderEnforcePrevrndBidPriceFlag | ENFORCE_PREVRND_BID_PRICE_FLAG | — | — |
| 132 | NegotiationHeaderEventId | EVENT_ID | — | — |
| 133 | NegotiationHeaderEventTitle | EVENT_TITLE | — | — |
| 134 | NegotiationHeaderExtAttribute1 | EXT_ATTRIBUTE1 | — | — |
| 135 | NegotiationHeaderExtAttribute10 | EXT_ATTRIBUTE10 | — | — |
| 136 | NegotiationHeaderExtAttribute11 | EXT_ATTRIBUTE11 | — | — |
| 137 | NegotiationHeaderExtAttribute12 | EXT_ATTRIBUTE12 | — | — |
| 138 | NegotiationHeaderExtAttribute13 | EXT_ATTRIBUTE13 | — | — |
| 139 | NegotiationHeaderExtAttribute14 | EXT_ATTRIBUTE14 | — | — |
| 140 | NegotiationHeaderExtAttribute15 | EXT_ATTRIBUTE15 | — | — |
| 141 | NegotiationHeaderExtAttribute16 | EXT_ATTRIBUTE16 | — | — |
| 142 | NegotiationHeaderExtAttribute17 | EXT_ATTRIBUTE17 | — | — |
| 143 | NegotiationHeaderExtAttribute18 | EXT_ATTRIBUTE18 | — | — |
| 144 | NegotiationHeaderExtAttribute19 | EXT_ATTRIBUTE19 | — | — |
| 145 | NegotiationHeaderExtAttribute2 | EXT_ATTRIBUTE2 | — | — |
| 146 | NegotiationHeaderExtAttribute20 | EXT_ATTRIBUTE20 | — | — |
| 147 | NegotiationHeaderExtAttribute3 | EXT_ATTRIBUTE3 | — | — |
| 148 | NegotiationHeaderExtAttribute4 | EXT_ATTRIBUTE4 | — | — |
| 149 | NegotiationHeaderExtAttribute5 | EXT_ATTRIBUTE5 | — | — |
| 150 | NegotiationHeaderExtAttribute6 | EXT_ATTRIBUTE6 | — | — |
| 151 | NegotiationHeaderExtAttribute7 | EXT_ATTRIBUTE7 | — | — |
| 152 | NegotiationHeaderExtAttribute8 | EXT_ATTRIBUTE8 | — | — |
| 153 | NegotiationHeaderExtAttribute9 | EXT_ATTRIBUTE9 | — | — |
| 154 | NegotiationHeaderExtAttributeCategory | EXT_ATTRIBUTE_CATEGORY | — | — |
| 155 | NegotiationHeaderExtAttributeDate1 | EXT_ATTRIBUTE_DATE1 | — | — |
| 156 | NegotiationHeaderExtAttributeDate10 | EXT_ATTRIBUTE_DATE10 | — | — |
| 157 | NegotiationHeaderExtAttributeDate2 | EXT_ATTRIBUTE_DATE2 | — | — |
| 158 | NegotiationHeaderExtAttributeDate3 | EXT_ATTRIBUTE_DATE3 | — | — |
| 159 | NegotiationHeaderExtAttributeDate4 | EXT_ATTRIBUTE_DATE4 | — | — |
| 160 | NegotiationHeaderExtAttributeDate5 | EXT_ATTRIBUTE_DATE5 | — | — |
| 161 | NegotiationHeaderExtAttributeDate6 | EXT_ATTRIBUTE_DATE6 | — | — |
| 162 | NegotiationHeaderExtAttributeDate7 | EXT_ATTRIBUTE_DATE7 | — | — |
| 163 | NegotiationHeaderExtAttributeDate8 | EXT_ATTRIBUTE_DATE8 | — | — |
| 164 | NegotiationHeaderExtAttributeDate9 | EXT_ATTRIBUTE_DATE9 | — | — |
| 165 | NegotiationHeaderExtAttributeNumber1 | EXT_ATTRIBUTE_NUMBER1 | — | — |
| 166 | NegotiationHeaderExtAttributeNumber10 | EXT_ATTRIBUTE_NUMBER10 | — | — |
| 167 | NegotiationHeaderExtAttributeNumber2 | EXT_ATTRIBUTE_NUMBER2 | — | — |
| 168 | NegotiationHeaderExtAttributeNumber3 | EXT_ATTRIBUTE_NUMBER3 | — | — |
| 169 | NegotiationHeaderExtAttributeNumber4 | EXT_ATTRIBUTE_NUMBER4 | — | — |
| 170 | NegotiationHeaderExtAttributeNumber5 | EXT_ATTRIBUTE_NUMBER5 | — | — |
| 171 | NegotiationHeaderExtAttributeNumber6 | EXT_ATTRIBUTE_NUMBER6 | — | — |
| 172 | NegotiationHeaderExtAttributeNumber7 | EXT_ATTRIBUTE_NUMBER7 | — | — |
| 173 | NegotiationHeaderExtAttributeNumber8 | EXT_ATTRIBUTE_NUMBER8 | — | — |
| 174 | NegotiationHeaderExtAttributeNumber9 | EXT_ATTRIBUTE_NUMBER9 | — | — |
| 175 | NegotiationHeaderExtAttributeTimestamp1 | EXT_ATTRIBUTE_TIMESTAMP1 | — | — |
| 176 | NegotiationHeaderExtAttributeTimestamp10 | EXT_ATTRIBUTE_TIMESTAMP10 | — | — |
| 177 | NegotiationHeaderExtAttributeTimestamp2 | EXT_ATTRIBUTE_TIMESTAMP2 | — | — |
| 178 | NegotiationHeaderExtAttributeTimestamp3 | EXT_ATTRIBUTE_TIMESTAMP3 | — | — |
| 179 | NegotiationHeaderExtAttributeTimestamp4 | EXT_ATTRIBUTE_TIMESTAMP4 | — | — |
| 180 | NegotiationHeaderExtAttributeTimestamp5 | EXT_ATTRIBUTE_TIMESTAMP5 | — | — |
| 181 | NegotiationHeaderExtAttributeTimestamp6 | EXT_ATTRIBUTE_TIMESTAMP6 | — | — |
| 182 | NegotiationHeaderExtAttributeTimestamp7 | EXT_ATTRIBUTE_TIMESTAMP7 | — | — |
| 183 | NegotiationHeaderExtAttributeTimestamp8 | EXT_ATTRIBUTE_TIMESTAMP8 | — | — |
| 184 | NegotiationHeaderExtAttributeTimestamp9 | EXT_ATTRIBUTE_TIMESTAMP9 | — | — |
| 185 | NegotiationHeaderExternalPoCreationStatus | EXTERNAL_PO_CREATION_STATUS | — | — |
| 186 | NegotiationHeaderFirstLineCloseDate | FIRST_LINE_CLOSE_DATE | — | — |
| 187 | NegotiationHeaderFobCode | FOB_CODE | — | — |
| 188 | NegotiationHeaderFreightTermsCode | FREIGHT_TERMS_CODE | — | — |
| 189 | NegotiationHeaderFullQuantityBidCode | FULL_QUANTITY_BID_CODE | — | — |
| 190 | NegotiationHeaderGlobalTemplateFlag | GLOBAL_TEMPLATE_FLAG | — | — |
| 191 | NegotiationHeaderGroupEnabledFlag | GROUP_ENABLED_FLAG | — | — |
| 192 | NegotiationHeaderHasHdrAttrFlag | HAS_HDR_ATTR_FLAG | — | — |
| 193 | NegotiationHeaderHasItemsFlag | HAS_ITEMS_FLAG | — | — |
| 194 | NegotiationHeaderHasPeForAllItems | HAS_PE_FOR_ALL_ITEMS | — | — |
| 195 | NegotiationHeaderHasPriceElements | HAS_PRICE_ELEMENTS | — | — |
| 196 | NegotiationHeaderHasScoringTeamsFlag | HAS_SCORING_TEAMS_FLAG | — | — |
| 197 | NegotiationHeaderHdrAttrDisplayScore | HDR_ATTR_DISPLAY_SCORE | — | ✅ |
| 198 | NegotiationHeaderHdrAttrEnableWeights | HDR_ATTR_ENABLE_WEIGHTS | — | ✅ |
| 199 | NegotiationHeaderHdrAttrMaximumScore | HDR_ATTR_MAXIMUM_SCORE | — | — |
| 200 | NegotiationHeaderHdrAttributeEnabledFlag | HDR_ATTRIBUTE_ENABLED_FLAG | — | — |
| 201 | NegotiationHeaderImportFileName | IMPORT_FILE_NAME | — | — |
| 202 | NegotiationHeaderIncludePdfInExternalPage | INCLUDE_PDF_IN_EXTERNAL_PAGE | — | — |
| 203 | NegotiationHeaderIntAttribute1 | INT_ATTRIBUTE1 | — | — |
| 204 | NegotiationHeaderIntAttribute10 | INT_ATTRIBUTE10 | — | — |
| 205 | NegotiationHeaderIntAttribute11 | INT_ATTRIBUTE11 | — | — |
| 206 | NegotiationHeaderIntAttribute12 | INT_ATTRIBUTE12 | — | — |
| 207 | NegotiationHeaderIntAttribute13 | INT_ATTRIBUTE13 | — | — |
| 208 | NegotiationHeaderIntAttribute14 | INT_ATTRIBUTE14 | — | — |
| 209 | NegotiationHeaderIntAttribute15 | INT_ATTRIBUTE15 | — | — |
| 210 | NegotiationHeaderIntAttribute2 | INT_ATTRIBUTE2 | — | — |
| 211 | NegotiationHeaderIntAttribute3 | INT_ATTRIBUTE3 | — | — |
| 212 | NegotiationHeaderIntAttribute4 | INT_ATTRIBUTE4 | — | — |
| 213 | NegotiationHeaderIntAttribute5 | INT_ATTRIBUTE5 | — | — |
| 214 | NegotiationHeaderIntAttribute6 | INT_ATTRIBUTE6 | — | — |
| 215 | NegotiationHeaderIntAttribute7 | INT_ATTRIBUTE7 | — | — |
| 216 | NegotiationHeaderIntAttribute8 | INT_ATTRIBUTE8 | — | — |
| 217 | NegotiationHeaderIntAttribute9 | INT_ATTRIBUTE9 | — | — |
| 218 | NegotiationHeaderIntAttributeCategory | INT_ATTRIBUTE_CATEGORY | — | — |
| 219 | NegotiationHeaderIsPaused | IS_PAUSED | — | — |
| 220 | NegotiationHeaderIsTemplateFlag | IS_TEMPLATE_FLAG | — | — |
| 221 | NegotiationHeaderLanguageCode | LANGUAGE_CODE | — | — |
| 222 | NegotiationHeaderLargeNegEnabledFlag | LARGE_NEG_ENABLED_FLAG | — | — |
| 223 | NegotiationHeaderLastLineNumber | LAST_LINE_NUMBER | — | — |
| 224 | NegotiationHeaderLastPauseDate | LAST_PAUSE_DATE | — | — |
| 225 | NegotiationHeaderLastUpdateDate4 | LAST_UPDATE_DATE | — | ✅ |
| 226 | NegotiationHeaderLastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 227 | NegotiationHeaderLastUpdatedBy4 | LAST_UPDATED_BY | — | — |
| 228 | NegotiationHeaderLineAttributeEnabledFlag | LINE_ATTRIBUTE_ENABLED_FLAG | — | — |
| 229 | NegotiationHeaderLineMasEnabledFlag | LINE_MAS_ENABLED_FLAG | — | — |
| 230 | NegotiationHeaderLotEnabledFlag | LOT_ENABLED_FLAG | — | — |
| 231 | NegotiationHeaderMaxBidColorSequenceId | MAX_BID_COLOR_SEQUENCE_ID | — | — |
| 232 | NegotiationHeaderMaxDocumentLineNum | MAX_DOCUMENT_LINE_NUM | — | — |
| 233 | NegotiationHeaderMaxInternalLineNum | MAX_INTERNAL_LINE_NUM | — | — |
| 234 | NegotiationHeaderMaxRetainageNegotiableFlag | MAX_RETAINAGE_NEGOTIABLE_FLAG | — | — |
| 235 | NegotiationHeaderMinBidChangeType | MIN_BID_CHANGE_TYPE | — | — |
| 236 | NegotiationHeaderMinBidDecrement | MIN_BID_DECREMENT | — | — |
| 237 | NegotiationHeaderModeOfTransport | MODE_OF_TRANSPORT | — | — |
| 238 | NegotiationHeaderNegApprIdentificationKey | NEG_APPR_IDENTIFICATION_KEY | — | — |
| 239 | NegotiationHeaderNegApprovalDate | NEG_APPROVAL_DATE | — | — |
| 240 | NegotiationHeaderNegApprovalEnabledFlag | NEG_APPROVAL_ENABLED_FLAG | — | — |
| 241 | NegotiationHeaderNegApprovalNote | NEG_APPROVAL_NOTE | — | — |
| 242 | NegotiationHeaderNegApprovalStatus | NEG_APPROVAL_STATUS | — | — |
| 243 | NegotiationHeaderNegTeamEnabledFlag | NEG_TEAM_ENABLED_FLAG | — | — |
| 244 | NegotiationHeaderNumberOfBids | NUMBER_OF_BIDS | — | — |
| 245 | NegotiationHeaderNumberOfExtensions | NUMBER_OF_EXTENSIONS | — | — |
| 246 | NegotiationHeaderNumberOfLines | NUMBER_OF_LINES | — | — |
| 247 | NegotiationHeaderNumberPriceDecimals | NUMBER_PRICE_DECIMALS | — | ✅ |
| 248 | NegotiationHeaderObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 249 | NegotiationHeaderOpenAuctionNowFlag | OPEN_AUCTION_NOW_FLAG | — | ✅ |
| 250 | NegotiationHeaderOpenBiddingDate | OPEN_BIDDING_DATE | — | ✅ |
| 251 | NegotiationHeaderOriginalCloseBiddingDate | ORIGINAL_CLOSE_BIDDING_DATE | — | — |
| 252 | NegotiationHeaderOutcomeStatus | OUTCOME_STATUS | — | — |
| 253 | NegotiationHeaderPauseRemarks | PAUSE_REMARKS | — | — |
| 254 | NegotiationHeaderPaymentTermsId | PAYMENT_TERMS_ID | — | — |
| 255 | NegotiationHeaderPersonId | PERSON_ID | — | — |
| 256 | NegotiationHeaderPfTypeAllowed | PF_TYPE_ALLOWED | — | — |
| 257 | NegotiationHeaderPoAgreedAmount | PO_AGREED_AMOUNT | — | ✅ |
| 258 | NegotiationHeaderPoCreationProcess | PO_CREATION_PROCESS | — | — |
| 259 | NegotiationHeaderPoEndDate | PO_END_DATE | — | ✅ |
| 260 | NegotiationHeaderPoMinRelAmount | PO_MIN_REL_AMOUNT | — | ✅ |
| 261 | NegotiationHeaderPoStartDate | PO_START_DATE | — | ✅ |
| 262 | NegotiationHeaderPoStyleId | PO_STYLE_ID | — | — |
| 263 | NegotiationHeaderPowerBiddingEnabledFlag | POWER_BIDDING_ENABLED_FLAG | — | — |
| 264 | NegotiationHeaderPrcBuId | PRC_BU_ID | — | — |
| 265 | NegotiationHeaderPriceDrivenAuctionFlag | PRICE_DRIVEN_AUCTION_FLAG | — | — |
| 266 | NegotiationHeaderPriceElementEnabledFlag | PRICE_ELEMENT_ENABLED_FLAG | — | — |
| 267 | NegotiationHeaderPriceTiersIndicator | PRICE_TIERS_INDICATOR | — | ✅ |
| 268 | NegotiationHeaderProgramAppName | PROGRAM_APP_NAME | — | — |
| 269 | NegotiationHeaderProgramName | PROGRAM_NAME | — | — |
| 270 | NegotiationHeaderProgressPaymentType | PROGRESS_PAYMENT_TYPE | — | — |
| 271 | NegotiationHeaderProgressPymtNegotiableFlag | PROGRESS_PYMT_NEGOTIABLE_FLAG | — | — |
| 272 | NegotiationHeaderProjectId | PROJECT_ID | — | — |
| 273 | NegotiationHeaderProjectsEnabledFlag | PROJECTS_ENABLED_FLAG | — | — |
| 274 | NegotiationHeaderProxyBiddingEnabledFlag | PROXY_BIDDING_ENABLED_FLAG | — | — |
| 275 | NegotiationHeaderPublishAuctionNowFlag | PUBLISH_AUCTION_NOW_FLAG | — | — |
| 276 | NegotiationHeaderPublishDate | PUBLISH_DATE | — | ✅ |
| 277 | NegotiationHeaderPublishDateOrigAmend | PUBLISH_DATE_ORIG_AMEND | — | — |
| 278 | NegotiationHeaderPublishRatesToBiddersFlag | PUBLISH_RATES_TO_BIDDERS_FLAG | — | — |
| 279 | NegotiationHeaderQtyPriceTiersEnabledFlag | QTY_PRICE_TIERS_ENABLED_FLAG | — | — |
| 280 | NegotiationHeaderRankIndicator | RANK_INDICATOR | — | ✅ |
| 281 | NegotiationHeaderRateDate | RATE_DATE | — | — |
| 282 | NegotiationHeaderRateType | RATE_TYPE | — | — |
| 283 | NegotiationHeaderRecoupmentNegotiableFlag | RECOUPMENT_NEGOTIABLE_FLAG | — | — |
| 284 | NegotiationHeaderReminderDate | REMINDER_DATE | — | — |
| 285 | NegotiationHeaderReqBuId | REQ_BU_ID | — | — |
| 286 | NegotiationHeaderRequestDate | REQUEST_DATE | — | — |
| 287 | NegotiationHeaderRequestId | REQUEST_ID | — | — |
| 288 | NegotiationHeaderRequestedBy | REQUESTED_BY | — | — |
| 289 | NegotiationHeaderRetainageNegotiableFlag | RETAINAGE_NEGOTIABLE_FLAG | — | — |
| 290 | NegotiationHeaderRfiLineEnabledFlag | RFI_LINE_ENABLED_FLAG | — | — |
| 291 | NegotiationHeaderScoringLockDate | SCORING_LOCK_DATE | — | — |
| 292 | NegotiationHeaderScoringLockPersonId | SCORING_LOCK_PERSON_ID | — | — |
| 293 | NegotiationHeaderSealedActualUnlockDate | SEALED_ACTUAL_UNLOCK_DATE | — | — |
| 294 | NegotiationHeaderSealedActualUnsealDate | SEALED_ACTUAL_UNSEAL_DATE | — | — |
| 295 | NegotiationHeaderSealedAuctionStatus | SEALED_AUCTION_STATUS | — | ✅ |
| 296 | NegotiationHeaderSealedUnlockPersonId | SEALED_UNLOCK_PERSON_ID | — | — |
| 297 | NegotiationHeaderSealedUnsealPersonId | SEALED_UNSEAL_PERSON_ID | — | — |
| 298 | NegotiationHeaderServiceLevel | SERVICE_LEVEL | — | — |
| 299 | NegotiationHeaderShareAwardDecision | SHARE_AWARD_DECISION | — | — |
| 300 | NegotiationHeaderShowBidderNotes | SHOW_BIDDER_NOTES | — | — |
| 301 | NegotiationHeaderShowBidderScores | SHOW_BIDDER_SCORES | — | — |
| 302 | NegotiationHeaderSourceDocId | SOURCE_DOC_ID | — | — |
| 303 | NegotiationHeaderSourceDocLineMsg | SOURCE_DOC_LINE_MSG | — | — |
| 304 | NegotiationHeaderSourceDocMsg | SOURCE_DOC_MSG | — | — |
| 305 | NegotiationHeaderSourceDocMsgApp | SOURCE_DOC_MSG_APP | — | — |
| 306 | NegotiationHeaderSourceDocNumber | SOURCE_DOC_NUMBER | — | ✅ |
| 307 | NegotiationHeaderSourceReqsFlag | SOURCE_REQS_FLAG | — | — |
| 308 | NegotiationHeaderStaggeredClosingInterval | STAGGERED_CLOSING_INTERVAL | — | — |
| 309 | NegotiationHeaderStyleId | STYLE_ID | — | — |
| 310 | NegotiationHeaderSupplierEnterablePymtFlag | SUPPLIER_ENTERABLE_PYMT_FLAG | — | — |
| 311 | NegotiationHeaderSupplierViewType | SUPPLIER_VIEW_TYPE | — | — |
| 312 | NegotiationHeaderSynopsis | SYNOPSIS | — | — |
| 313 | NegotiationHeaderTeamScoringEnabledFlag | TEAM_SCORING_ENABLED_FLAG | — | — |
| 314 | NegotiationHeaderTechnicalActualUnlockDate | TECHNICAL_ACTUAL_UNLOCK_DATE | — | — |
| 315 | NegotiationHeaderTechnicalActualUnsealDate | TECHNICAL_ACTUAL_UNSEAL_DATE | — | — |
| 316 | NegotiationHeaderTechnicalEvaluationStatus | TECHNICAL_EVALUATION_STATUS | — | — |
| 317 | NegotiationHeaderTechnicalLockStatus | TECHNICAL_LOCK_STATUS | — | ✅ |
| 318 | NegotiationHeaderTechnicalUnlockPersonId | TECHNICAL_UNLOCK_PERSON_ID | — | — |
| 319 | NegotiationHeaderTechnicalUnsealPersonId | TECHNICAL_UNSEAL_PERSON_ID | — | — |
| 320 | NegotiationHeaderTemplateId | TEMPLATE_ID | — | — |
| 321 | NegotiationHeaderTemplateScope | TEMPLATE_SCOPE | — | — |
| 322 | NegotiationHeaderTemplateStatus | TEMPLATE_STATUS | — | — |
| 323 | NegotiationHeaderTwoPartFlag | TWO_PART_FLAG | — | ✅ |
| 324 | NegotiationHeaderTwostageEvalEnabledFlag | TWOSTAGE_EVAL_ENABLED_FLAG | — | — |
| 325 | NegotiationHeaderVersionNum | VERSION_NUM | — | — |
| 326 | NegotiationHeaderViewByDate | VIEW_BY_DATE | — | ✅ |
| 327 | NegotiationHeaderWfApprovalItemKey | WF_APPROVAL_ITEM_KEY | — | — |
| 328 | NegotiationHeaderWfAwardApprovalItemKey | WF_AWARD_APPROVAL_ITEM_KEY | — | — |
| 329 | NegotiationHeaderWfItemKey | WF_ITEM_KEY | — | — |
| 330 | NegotiationHeaderWfPoncomplCurrentRound | WF_PONCOMPL_CURRENT_ROUND | — | — |
| 331 | NegotiationHeaderWfPoncomplItemKey | WF_PONCOMPL_ITEM_KEY | — | — |
| 332 | NegotiationHeaderWfRoleName | WF_ROLE_NAME | — | — |

### [[pon_bid_headers|PON_BID_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResponseHeaderAttributeLineNumber1 | ATTRIBUTE_LINE_NUMBER | — | — |
| 2 | ResponseHeaderAuctionHeaderId7 | AUCTION_HEADER_ID | — | — |
| 3 | ResponseHeaderAwardDate1 | AWARD_DATE | — | — |
| 4 | ResponseHeaderAwardStatus1 | AWARD_STATUS | — | — |
| 5 | ResponseHeaderBidCurrencyCode | BID_CURRENCY_CODE | — | ✅ |
| 6 | ResponseHeaderBidCurrencyMinBidChange | BID_CURRENCY_MIN_BID_CHANGE | — | — |
| 7 | ResponseHeaderBidExpirationDate | BID_EXPIRATION_DATE | — | — |
| 8 | ResponseHeaderBidNumber3 | BID_NUMBER | — | ✅ |
| 9 | ResponseHeaderBidStatus | BID_STATUS | — | — |
| 10 | ResponseHeaderBiddersBidNumber | BIDDERS_BID_NUMBER | — | — |
| 11 | ResponseHeaderBuyerBidTotal | BUYER_BID_TOTAL | — | — |
| 12 | ResponseHeaderCancelReason | CANCEL_REASON | — | ✅ |
| 13 | ResponseHeaderCancelledDate | CANCELLED_DATE | — | ✅ |
| 14 | ResponseHeaderColorSequenceId | COLOR_SEQUENCE_ID | — | — |
| 15 | ResponseHeaderCreatedBy7 | CREATED_BY | — | — |
| 16 | ResponseHeaderCreationDate7 | CREATION_DATE | — | — |
| 17 | ResponseHeaderCurrentRebate | CURRENT_REBATE | — | — |
| 18 | ResponseHeaderCurrentTotalSpend | CURRENT_TOTAL_SPEND | — | — |
| 19 | ResponseHeaderDisplayPriceFactorsFlag | DISPLAY_PRICE_FACTORS_FLAG | — | — |
| 20 | ResponseHeaderDisqualifyReason | DISQUALIFY_REASON | — | — |
| 21 | ResponseHeaderDraftLocked1 | DRAFT_LOCKED | — | ✅ |
| 22 | ResponseHeaderDraftLockedBy | DRAFT_LOCKED_BY | — | — |
| 23 | ResponseHeaderDraftLockedByContactId | DRAFT_LOCKED_BY_CONTACT_ID | — | — |
| 24 | ResponseHeaderDraftLockedDate1 | DRAFT_LOCKED_DATE | — | ✅ |
| 25 | ResponseHeaderDraftUnlockedBy | DRAFT_UNLOCKED_BY | — | — |
| 26 | ResponseHeaderDraftUnlockedByContactId | DRAFT_UNLOCKED_BY_CONTACT_ID | — | — |
| 27 | ResponseHeaderDraftUnlockedDate1 | DRAFT_UNLOCKED_DATE | — | ✅ |
| 28 | ResponseHeaderFixedIncentive | FIXED_INCENTIVE | — | — |
| 29 | ResponseHeaderHasRebateTiers | HAS_REBATE_TIERS | — | — |
| 30 | ResponseHeaderImportFileName1 | IMPORT_FILE_NAME | — | — |
| 31 | ResponseHeaderIncumbentFlag | INCUMBENT_FLAG | — | — |
| 32 | ResponseHeaderInternalNote1 | INTERNAL_NOTE | — | ✅ |
| 33 | ResponseHeaderLastUpdateDate7 | LAST_UPDATE_DATE | — | ✅ |
| 34 | ResponseHeaderLastUpdateLogin7 | LAST_UPDATE_LOGIN | — | — |
| 35 | ResponseHeaderLastUpdatedBy7 | LAST_UPDATED_BY | — | — |
| 36 | ResponseHeaderMaxInternalLineNum1 | MAX_INTERNAL_LINE_NUM | — | — |
| 37 | ResponseHeaderMinBidChange | MIN_BID_CHANGE | — | — |
| 38 | ResponseHeaderNoteToAuctionOwner | NOTE_TO_AUCTION_OWNER | — | ✅ |
| 39 | ResponseHeaderNoteToSupplier | NOTE_TO_SUPPLIER | — | ✅ |
| 40 | ResponseHeaderNumberPriceDecimals1 | NUMBER_PRICE_DECIMALS | — | ✅ |
| 41 | ResponseHeaderObjectVersionNumber7 | OBJECT_VERSION_NUMBER | — | — |
| 42 | ResponseHeaderOldBidCurrMinBidChange | OLD_BID_CURR_MIN_BID_CHANGE | — | — |
| 43 | ResponseHeaderOldBidExpirationDate | OLD_BID_EXPIRATION_DATE | — | — |
| 44 | ResponseHeaderOldBidNumber | OLD_BID_NUMBER | — | — |
| 45 | ResponseHeaderOldBidStatus | OLD_BID_STATUS | — | — |
| 46 | ResponseHeaderOldBiddersBidNumber | OLD_BIDDERS_BID_NUMBER | — | — |
| 47 | ResponseHeaderOldMinBidChange | OLD_MIN_BID_CHANGE | — | — |
| 48 | ResponseHeaderOldNoteToAuctionOwner | OLD_NOTE_TO_AUCTION_OWNER | — | — |
| 49 | ResponseHeaderOldSurrogBidReceiptDate | OLD_SURROG_BID_RECEIPT_DATE | — | — |
| 50 | ResponseHeaderOriginalBidNumber | ORIGINAL_BID_NUMBER | — | — |
| 51 | ResponseHeaderPartialResponseFlag | PARTIAL_RESPONSE_FLAG | — | ✅ |
| 52 | ResponseHeaderPoAgreedAmount1 | PO_AGREED_AMOUNT | — | — |
| 53 | ResponseHeaderPoqTransferStatus | POQ_TRANSFER_STATUS | — | — |
| 54 | ResponseHeaderProgramAppName1 | PROGRAM_APP_NAME | — | — |
| 55 | ResponseHeaderProgramName1 | PROGRAM_NAME | — | — |
| 56 | ResponseHeaderProxyBidFlag | PROXY_BID_FLAG | — | — |
| 57 | ResponseHeaderPublishDate1 | PUBLISH_DATE | — | ✅ |
| 58 | ResponseHeaderRate | RATE | — | — |
| 59 | ResponseHeaderRateDate1 | RATE_DATE | — | — |
| 60 | ResponseHeaderRateDsp | RATE_DSP | — | — |
| 61 | ResponseHeaderRateType1 | RATE_TYPE | — | — |
| 62 | ResponseHeaderRequestDate1 | REQUEST_DATE | — | — |
| 63 | ResponseHeaderRequestId1 | REQUEST_ID | — | — |
| 64 | ResponseHeaderRequestedBy1 | REQUESTED_BY | — | — |
| 65 | ResponseHeaderScoreOverridenDate | SCORE_OVERRIDEN_DATE | — | — |
| 66 | ResponseHeaderScoreOverridenFlag | SCORE_OVERRIDEN_FLAG | — | — |
| 67 | ResponseHeaderShortlistBuyerId | SHORTLIST_BUYER_ID | — | — |
| 68 | ResponseHeaderShortlistFlag | SHORTLIST_FLAG | — | ✅ |
| 69 | ResponseHeaderSubmitStage | SUBMIT_STAGE | — | — |
| 70 | ResponseHeaderSurrogBidCreatedPersonId | SURROG_BID_CREATED_PERSON_ID | — | — |
| 71 | ResponseHeaderSurrogBidFlag | SURROG_BID_FLAG | — | ✅ |
| 72 | ResponseHeaderSurrogBidOnlineEntryDate | SURROG_BID_ONLINE_ENTRY_DATE | — | — |
| 73 | ResponseHeaderSurrogBidReceiptDate | SURROG_BID_RECEIPT_DATE | — | — |
| 74 | ResponseHeaderSurrogDraftLockPersonId | SURROG_DRAFT_LOCK_PERSON_ID | — | — |
| 75 | ResponseHeaderSurrogDraftUnlockPersonId | SURROG_DRAFT_UNLOCK_PERSON_ID | — | — |
| 76 | ResponseHeaderSurrogMethodOfResponse | SURROG_METHOD_OF_RESPONSE | — | — |
| 77 | ResponseHeaderTechnicalShortlistFlag | TECHNICAL_SHORTLIST_FLAG | — | ✅ |
| 78 | ResponseHeaderTotalAwardAmount | TOTAL_AWARD_AMOUNT | — | — |
| 79 | ResponseHeaderTradingPartnerContactId | TRADING_PARTNER_CONTACT_ID | — | — |
| 80 | ResponseHeaderTradingPartnerId | TRADING_PARTNER_ID | — | — |
| 81 | ResponseHeaderTypeOfResponse | TYPE_OF_RESPONSE | — | — |
| 82 | ResponseHeaderVendorId | VENDOR_ID | — | — |
| 83 | ResponseHeaderVendorSiteId | VENDOR_SITE_ID | — | — |

### [[pon_bid_requirements|PON_BID_REQUIREMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegRespRequirementsAuctionHeaderId5 | AUCTION_HEADER_ID | — | — |
| 2 | NegRespRequirementsBidNumber1 | BID_NUMBER | — | — |
| 3 | NegRespRequirementsComments | COMMENTS | — | ✅ |
| 4 | NegRespRequirementsCreatedBy5 | CREATED_BY | — | ✅ |
| 5 | NegRespRequirementsCreationDate5 | CREATION_DATE | — | ✅ |
| 6 | NegRespRequirementsHasBidFlag | HAS_BID_FLAG | — | — |
| 7 | NegRespRequirementsInterfaceLineId | INTERFACE_LINE_ID | — | — |
| 8 | NegRespRequirementsInternalNote | INTERNAL_NOTE | — | ✅ |
| 9 | NegRespRequirementsLastUpdateDate5 | LAST_UPDATE_DATE | — | ✅ |
| 10 | NegRespRequirementsLastUpdateLogin5 | LAST_UPDATE_LOGIN | — | — |
| 11 | NegRespRequirementsLastUpdatedBy5 | LAST_UPDATED_BY | — | — |
| 12 | NegRespRequirementsObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 13 | NegRespRequirementsOldComments | OLD_COMMENTS | — | — |
| 14 | NegRespRequirementsRequirementId3 | REQUIREMENT_ID | — | — |
| 15 | NegRespRequirementsScore1 | SCORE | — | ✅ |
| 16 | NegRespRequirementsSectionId2 | SECTION_ID | — | — |
| 17 | NegRespRequirementsSequenceNumber1 | SEQUENCE_NUMBER | — | — |
| 18 | NegRespRequirementsWeightedScore | WEIGHTED_SCORE | — | ✅ |
| 19 | NegRespRequirementsWorksheetName | WORKSHEET_NAME | — | — |
| 20 | NegRespRequirementsWorksheetSequenceNumber | WORKSHEET_SEQUENCE_NUMBER | — | — |

### [[pon_bid_requirement_values|PON_BID_REQUIREMENT_VALUES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RespReqtValuesAuctionHeaderId | AUCTION_HEADER_ID | — | — |
| 2 | RespReqtValuesBidNumber | BID_NUMBER | — | ✅ |
| 3 | RespReqtValuesCreatedBy | CREATED_BY | — | — |
| 4 | RespReqtValuesCreationDate | CREATION_DATE | — | — |
| 5 | RespReqtValuesDateValue | DATE_VALUE | — | ✅ |
| 6 | RespReqtValuesDatetimeValue | DATETIME_VALUE | — | ✅ |
| 7 | RespReqtValuesIsSelectedFlag | IS_SELECTED_FLAG | — | ✅ |
| 8 | RespReqtValuesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | RespReqtValuesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | RespReqtValuesLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | RespReqtValuesNumberValue | NUMBER_VALUE | — | ✅ |
| 12 | RespReqtValuesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | RespReqtValuesOldDateValue | OLD_DATE_VALUE | — | — |
| 14 | RespReqtValuesOldDatetimeValue | OLD_DATETIME_VALUE | — | — |
| 15 | RespReqtValuesOldIsSelectedFlag | OLD_IS_SELECTED_FLAG | — | — |
| 16 | RespReqtValuesOldNumberValue | OLD_NUMBER_VALUE | — | — |
| 17 | RespReqtValuesOldTextValue | OLD_TEXT_VALUE | — | — |
| 18 | RespReqtValuesRequirementId | REQUIREMENT_ID | — | ✅ |
| 19 | RespReqtValuesRequirementValueId | REQUIREMENT_VALUE_ID | 🔑 | ✅ |
| 20 | RespReqtValuesScoreId | SCORE_ID | — | ✅ |
| 21 | RespReqtValuesTextValue | TEXT_VALUE | — | ✅ |

### [[pon_bid_sections|PON_BID_SECTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegRespSectionsAuctionHeaderId6 | AUCTION_HEADER_ID | — | — |
| 2 | NegRespSectionsBidNumber2 | BID_NUMBER | — | — |
| 3 | NegRespSectionsCreatedBy6 | CREATED_BY | — | — |
| 4 | NegRespSectionsCreationDate6 | CREATION_DATE | — | — |
| 5 | NegRespSectionsLastUpdateDate6 | LAST_UPDATE_DATE | — | ✅ |
| 6 | NegRespSectionsLastUpdateLogin6 | LAST_UPDATE_LOGIN | — | — |
| 7 | NegRespSectionsLastUpdatedBy6 | LAST_UPDATED_BY | — | — |
| 8 | NegRespSectionsObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |
| 9 | NegRespSectionsSectionId3 | SECTION_ID | — | — |
| 10 | NegRespSectionsSectionVisitedFlag | SECTION_VISITED_FLAG | — | — |

### [[pon_requirements|PON_REQUIREMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationRequirementAbsoluteSectionSequence | ABSOLUTE_SECTION_SEQUENCE | — | ✅ |
| 2 | NegotiationRequirementAllowAttachmentCode | ALLOW_ATTACHMENT_CODE | — | — |
| 3 | NegotiationRequirementAllowComments | ALLOW_COMMENTS | — | — |
| 4 | NegotiationRequirementAuctionHeaderId2 | AUCTION_HEADER_ID | — | — |
| 5 | NegotiationRequirementCategoryCode | CATEGORY_CODE | — | — |
| 6 | NegotiationRequirementCreatedBy2 | CREATED_BY | — | — |
| 7 | NegotiationRequirementCreationDate2 | CREATION_DATE | — | — |
| 8 | NegotiationRequirementDatatype | DATATYPE | — | ✅ |
| 9 | NegotiationRequirementDateValue1 | DATE_VALUE | — | — |
| 10 | NegotiationRequirementDatetimeValue1 | DATETIME_VALUE | — | — |
| 11 | NegotiationRequirementDispSeqNumber1 | DISP_SEQ_NUMBER | — | — |
| 12 | NegotiationRequirementDisplayTargetFlag | DISPLAY_TARGET_FLAG | — | — |
| 13 | NegotiationRequirementHint | HINT | — | — |
| 14 | NegotiationRequirementIsQuestionBranch | IS_QUESTION_BRANCH | — | — |
| 15 | NegotiationRequirementKnockoutScore | KNOCKOUT_SCORE | — | — |
| 16 | NegotiationRequirementLastAmendmentUpdate1 | LAST_AMENDMENT_UPDATE | — | — |
| 17 | NegotiationRequirementLastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 18 | NegotiationRequirementLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 19 | NegotiationRequirementLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 20 | NegotiationRequirementMaxScore | MAX_SCORE | — | — |
| 21 | NegotiationRequirementModifiedDate | MODIFIED_DATE | — | — |
| 22 | NegotiationRequirementModifiedFlag1 | MODIFIED_FLAG | — | — |
| 23 | NegotiationRequirementNumberValue1 | NUMBER_VALUE | — | — |
| 24 | NegotiationRequirementObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 25 | NegotiationRequirementParentLevel | PARENT_LEVEL | — | — |
| 26 | NegotiationRequirementParentRequirementId | PARENT_REQUIREMENT_ID | — | — |
| 27 | NegotiationRequirementPreviousRequirementId | PREVIOUS_REQUIREMENT_ID | — | — |
| 28 | NegotiationRequirementQuestionId | QUESTION_ID | — | ✅ |
| 29 | NegotiationRequirementReqDisplayNumber | REQ_DISPLAY_NUMBER | — | ✅ |
| 30 | NegotiationRequirementRequirementId1 | REQUIREMENT_ID | — | ✅ |
| 31 | NegotiationRequirementRequirementName | REQUIREMENT_NAME | — | ✅ |
| 32 | NegotiationRequirementRequirementText | REQUIREMENT_TEXT | — | ✅ |
| 33 | NegotiationRequirementRequirementTreeLevel | REQUIREMENT_TREE_LEVEL | — | — |
| 34 | NegotiationRequirementRequirementType | REQUIREMENT_TYPE | — | ✅ |
| 35 | NegotiationRequirementResponseType | RESPONSE_TYPE | — | ✅ |
| 36 | NegotiationRequirementRevisionNumber | REVISION_NUMBER | — | ✅ |
| 37 | NegotiationRequirementRootRequirementId | ROOT_REQUIREMENT_ID | — | — |
| 38 | NegotiationRequirementScoreId1 | SCORE_ID | — | — |
| 39 | NegotiationRequirementScoringMethod | SCORING_METHOD | — | ✅ |
| 40 | NegotiationRequirementScoringType | SCORING_TYPE | — | — |
| 41 | NegotiationRequirementSectionId1 | SECTION_ID | — | — |
| 42 | NegotiationRequirementSequenceNumber | SEQUENCE_NUMBER | — | — |
| 43 | NegotiationRequirementSupplierLevel | SUPPLIER_LEVEL | — | ✅ |
| 44 | NegotiationRequirementTextValue1 | TEXT_VALUE | — | — |
| 45 | NegotiationRequirementWeight | WEIGHT | — | — |

### [[pon_requirement_scores|PON_REQUIREMENT_SCORES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationScoresAccResponseId | ACC_RESPONSE_ID | — | — |
| 2 | NegotiationScoresAllowAttachmentCode1 | ALLOW_ATTACHMENT_CODE | — | — |
| 3 | NegotiationScoresAuctionHeaderId3 | AUCTION_HEADER_ID | — | — |
| 4 | NegotiationScoresCreatedBy3 | CREATED_BY | — | — |
| 5 | NegotiationScoresCreationDate3 | CREATION_DATE | — | — |
| 6 | NegotiationScoresDateFromRange | DATE_FROM_RANGE | — | — |
| 7 | NegotiationScoresDateToRange | DATE_TO_RANGE | — | — |
| 8 | NegotiationScoresDatetimeFromRange | DATETIME_FROM_RANGE | — | — |
| 9 | NegotiationScoresDatetimeToRange | DATETIME_TO_RANGE | — | — |
| 10 | NegotiationScoresDispSeqNumber2 | DISP_SEQ_NUMBER | — | — |
| 11 | NegotiationScoresIsDefaultScoreRow | IS_DEFAULT_SCORE_ROW | — | — |
| 12 | NegotiationScoresLastUpdateDate3 | LAST_UPDATE_DATE | — | ✅ |
| 13 | NegotiationScoresLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 14 | NegotiationScoresLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 15 | NegotiationScoresNumberFromRange | NUMBER_FROM_RANGE | — | — |
| 16 | NegotiationScoresNumberToRange | NUMBER_TO_RANGE | — | — |
| 17 | NegotiationScoresObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 18 | NegotiationScoresPreviousScoreId | PREVIOUS_SCORE_ID | — | — |
| 19 | NegotiationScoresRequirementId2 | REQUIREMENT_ID | — | — |
| 20 | NegotiationScoresScore | SCORE | — | — |
| 21 | NegotiationScoresScoreDisplayNumber | SCORE_DISPLAY_NUMBER | — | — |
| 22 | NegotiationScoresScoreId2 | SCORE_ID | 🔑 | ✅ |
| 23 | NegotiationScoresScoreLevel | SCORE_LEVEL | — | — |
| 24 | NegotiationScoresTargetFlag | TARGET_FLAG | — | — |
| 25 | NegotiationScoresTextValue2 | TEXT_VALUE | — | ✅ |

### [[pon_requirement_sections|PON_REQUIREMENT_SECTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationSectionsAuctionHeaderId1 | AUCTION_HEADER_ID | — | — |
| 2 | NegotiationSectionsCreatedBy1 | CREATED_BY | — | — |
| 3 | NegotiationSectionsCreationDate1 | CREATION_DATE | — | — |
| 4 | NegotiationSectionsDispSeqNumber | DISP_SEQ_NUMBER | — | ✅ |
| 5 | NegotiationSectionsIsInternal | IS_INTERNAL | — | — |
| 6 | NegotiationSectionsLastAmendmentUpdate | LAST_AMENDMENT_UPDATE | — | — |
| 7 | NegotiationSectionsLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 8 | NegotiationSectionsLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 9 | NegotiationSectionsLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 10 | NegotiationSectionsModifiedFlag | MODIFIED_FLAG | — | — |
| 11 | NegotiationSectionsObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 12 | NegotiationSectionsPreviousSectionId | PREVIOUS_SECTION_ID | — | — |
| 13 | NegotiationSectionsSectionDisplayNumber | SECTION_DISPLAY_NUMBER | — | ✅ |
| 14 | NegotiationSectionsSectionId | SECTION_ID | 🔑 | ✅ |
| 15 | NegotiationSectionsSectionLevel | SECTION_LEVEL | — | — |
| 16 | NegotiationSectionsSectionName | SECTION_NAME | — | ✅ |
| 17 | NegotiationSectionsTwoPartSectionType | TWO_PART_SECTION_TYPE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
