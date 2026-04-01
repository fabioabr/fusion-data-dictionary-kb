---
id: DOC-PO-PVO-NegotiationAndTemplateExtractPVO
doc_type: system-doc
title: "NegotiationAndTemplateExtractPVO — PVO Purchasing"
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
  - NegotiationAndTemplateExtractPVO
  - negotiationandtemplateextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationAndTemplateExtractPVO

## 📌 Visão Geral

Extrai cabeçalhos de negociações de sourcing e templates para carga BICC, com regras, prazos, moeda e critérios de adjudicação. Alimenta análises de desempenho e eficácia do processo de sourcing.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.NegotiationAndTemplateExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 382 | 1 | 1 | 171 | 45% |

---

## 🔗 Tabelas Relacionadas

- [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]] — 382 atributos (1 PKs, 171 BICC)

---

## ⚙️ Atributos

### [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbstractDetails | ABSTRACT_DETAILS | — | — |
| 2 | AbstractEnabledFlag | ABSTRACT_ENABLED_FLAG | — | ✅ |
| 3 | AbstractStatus | ABSTRACT_STATUS | — | — |
| 4 | AcceptTermsBeforeNegFlag | ACCEPT_TERMS_BEFORE_NEG_FLAG | — | ✅ |
| 5 | AdvanceNegotiableFlag | ADVANCE_NEGOTIABLE_FLAG | — | — |
| 6 | AllowAlternateLines | ALLOW_ALTERNATE_LINES | — | ✅ |
| 7 | AllowContractCrtFlag | ALLOW_CONTRACT_CRT_FLAG | — | ✅ |
| 8 | AllowOtherBidCurrencyFlag | ALLOW_OTHER_BID_CURRENCY_FLAG | — | ✅ |
| 9 | AlternateLinesEnabledFlag | ALTERNATE_LINES_ENABLED_FLAG | — | ✅ |
| 10 | AmendmentDescription | AMENDMENT_DESCRIPTION | — | ✅ |
| 11 | AmendmentNumber | AMENDMENT_NUMBER | — | ✅ |
| 12 | ApprovalAmount | APPROVAL_AMOUNT | — | ✅ |
| 13 | ApprovalStatus1 | APPROVAL_STATUS | — | ✅ |
| 14 | Attribute1 | ATTRIBUTE1 | — | — |
| 15 | Attribute10 | ATTRIBUTE10 | — | — |
| 16 | Attribute11 | ATTRIBUTE11 | — | — |
| 17 | Attribute12 | ATTRIBUTE12 | — | — |
| 18 | Attribute13 | ATTRIBUTE13 | — | — |
| 19 | Attribute14 | ATTRIBUTE14 | — | — |
| 20 | Attribute15 | ATTRIBUTE15 | — | — |
| 21 | Attribute16 | ATTRIBUTE16 | — | — |
| 22 | Attribute17 | ATTRIBUTE17 | — | — |
| 23 | Attribute18 | ATTRIBUTE18 | — | — |
| 24 | Attribute19 | ATTRIBUTE19 | — | — |
| 25 | Attribute2 | ATTRIBUTE2 | — | — |
| 26 | Attribute20 | ATTRIBUTE20 | — | — |
| 27 | Attribute3 | ATTRIBUTE3 | — | — |
| 28 | Attribute4 | ATTRIBUTE4 | — | — |
| 29 | Attribute5 | ATTRIBUTE5 | — | — |
| 30 | Attribute6 | ATTRIBUTE6 | — | — |
| 31 | Attribute7 | ATTRIBUTE7 | — | — |
| 32 | Attribute8 | ATTRIBUTE8 | — | — |
| 33 | Attribute9 | ATTRIBUTE9 | — | — |
| 34 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 35 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 36 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 37 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 38 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 39 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 40 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 41 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 42 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 43 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 44 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 45 | AttributeLineNumber | ATTRIBUTE_LINE_NUMBER | — | — |
| 46 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 47 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 48 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 49 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 50 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 51 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 52 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 53 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 54 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 55 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 56 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 57 | AttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 58 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 59 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 60 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 61 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 62 | AttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 63 | AttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 64 | AttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 65 | AttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 66 | AttributesExist | ATTRIBUTES_EXIST | — | — |
| 67 | AuctionHeaderId | AUCTION_HEADER_ID | 🔑 | ✅ |
| 68 | AuctionHeaderIdOrigAmend | AUCTION_HEADER_ID_ORIG_AMEND | — | ✅ |
| 69 | AuctionHeaderIdOrigRound | AUCTION_HEADER_ID_ORIG_ROUND | — | ✅ |
| 70 | AuctionHeaderIdPrevAmend | AUCTION_HEADER_ID_PREV_AMEND | — | ✅ |
| 71 | AuctionHeaderIdPrevRound | AUCTION_HEADER_ID_PREV_ROUND | — | ✅ |
| 72 | AuctionOriginationCode | AUCTION_ORIGINATION_CODE | — | ✅ |
| 73 | AuctionRoundNumber | AUCTION_ROUND_NUMBER | — | ✅ |
| 74 | AuctionStatus | AUCTION_STATUS | — | ✅ |
| 75 | AuctionTitle | AUCTION_TITLE | — | ✅ |
| 76 | AutoExtendAllLinesFlag | AUTO_EXTEND_ALL_LINES_FLAG | — | ✅ |
| 77 | AutoExtendDuration | AUTO_EXTEND_DURATION | — | ✅ |
| 78 | AutoExtendEnabledFlag | AUTO_EXTEND_ENABLED_FLAG | — | ✅ |
| 79 | AutoExtendFlag | AUTO_EXTEND_FLAG | — | ✅ |
| 80 | AutoExtendMinTriggerRank | AUTO_EXTEND_MIN_TRIGGER_RANK | — | ✅ |
| 81 | AutoExtendNumber | AUTO_EXTEND_NUMBER | — | ✅ |
| 82 | AutoExtendTriggerPeriod | AUTO_EXTEND_TRIGGER_PERIOD | — | ✅ |
| 83 | AutoExtendTypeFlag | AUTO_EXTEND_TYPE_FLAG | — | ✅ |
| 84 | AutoextendChangedFlag | AUTOEXTEND_CHANGED_FLAG | — | — |
| 85 | AwardApprAmeTransId | AWARD_APPR_AME_TRANS_ID | — | — |
| 86 | AwardApprAmeTransPrevId | AWARD_APPR_AME_TRANS_PREV_ID | — | — |
| 87 | AwardApprAmeTxnDate | AWARD_APPR_AME_TXN_DATE | — | — |
| 88 | AwardApprIdentificationKey | AWARD_APPR_IDENTIFICATION_KEY | — | — |
| 89 | AwardApprovalDate | AWARD_APPROVAL_DATE | — | ✅ |
| 90 | AwardApprovalFlag | AWARD_APPROVAL_FLAG | — | ✅ |
| 91 | AwardApprovalNote | AWARD_APPROVAL_NOTE | — | ✅ |
| 92 | AwardApprovalStatus | AWARD_APPROVAL_STATUS | — | ✅ |
| 93 | AwardByDate | AWARD_BY_DATE | — | ✅ |
| 94 | AwardCompleteDate | AWARD_COMPLETE_DATE | — | ✅ |
| 95 | AwardDate | AWARD_DATE | — | ✅ |
| 96 | AwardMode | AWARD_MODE | — | — |
| 97 | AwardNoticeLayoutName | AWARD_NOTICE_LAYOUT_NAME | — | ✅ |
| 98 | AwardStatus | AWARD_STATUS | — | ✅ |
| 99 | BidDecrementMethod | BID_DECREMENT_METHOD | — | ✅ |
| 100 | BidFrequencyCode | BID_FREQUENCY_CODE | — | ✅ |
| 101 | BidFrequencyCodeDspFlag | BID_FREQUENCY_CODE_DSP_FLAG | — | ✅ |
| 102 | BidListType | BID_LIST_TYPE | — | ✅ |
| 103 | BidListTypeDspFlag | BID_LIST_TYPE_DSP_FLAG | — | ✅ |
| 104 | BidRanking | BID_RANKING | — | ✅ |
| 105 | BidRevisionType | BID_REVISION_TYPE | — | ✅ |
| 106 | BidRevisionTypeDspFlag | BID_REVISION_TYPE_DSP_FLAG | — | ✅ |
| 107 | BidScopeCode | BID_SCOPE_CODE | — | ✅ |
| 108 | BidScopeCodeDspFlag | BID_SCOPE_CODE_DSP_FLAG | — | ✅ |
| 109 | BidVisibilityCode | BID_VISIBILITY_CODE | — | ✅ |
| 110 | BuyerTransportEnabledFlag | BUYER_TRANSPORT_ENABLED_FLAG | — | ✅ |
| 111 | BuyerTransportFlag | BUYER_TRANSPORT_FLAG | — | ✅ |
| 112 | CancelDate | CANCEL_DATE | — | ✅ |
| 113 | CarrierId | CARRIER_ID | — | ✅ |
| 114 | CloseBiddingDate | CLOSE_BIDDING_DATE | — | ✅ |
| 115 | CloseDatePauseAdjusted | CLOSE_DATE_PAUSE_ADJUSTED | — | — |
| 116 | CloseDateType | CLOSE_DATE_TYPE | — | ✅ |
| 117 | CompleteFlag | COMPLETE_FLAG | — | — |
| 118 | ContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 119 | ContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 120 | ContermsEnabledFlag | CONTERMS_ENABLED_FLAG | — | — |
| 121 | ContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 122 | ContractErrorMsg | CONTRACT_ERROR_MSG | — | — |
| 123 | ContractId | CONTRACT_ID | — | — |
| 124 | ContractLayoutId | CONTRACT_LAYOUT_ID | — | — |
| 125 | ContractLayoutName | CONTRACT_LAYOUT_NAME | — | — |
| 126 | ContractTemplateId | CONTRACT_TEMPLATE_ID | — | — |
| 127 | ContractType | CONTRACT_TYPE | — | — |
| 128 | CoverPageEnabledFlag | COVER_PAGE_ENABLED_FLAG | — | ✅ |
| 129 | CoverPageText | COVER_PAGE_TEXT | — | ✅ |
| 130 | CreatedBy | CREATED_BY | — | ✅ |
| 131 | CreationDate | CREATION_DATE | — | ✅ |
| 132 | CreationDateOrigAmend | CREATION_DATE_ORIG_AMEND | — | ✅ |
| 133 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 134 | DaysAfterOpenDate | DAYS_AFTER_OPEN_DATE | — | ✅ |
| 135 | Description | DESCRIPTION | — | — |
| 136 | DisplayBestPriceBlindFlag | DISPLAY_BEST_PRICE_BLIND_FLAG | — | ✅ |
| 137 | DisplayBestPriceDspFlag | DISPLAY_BEST_PRICE_DSP_FLAG | — | ✅ |
| 138 | DisplayBidRankToSuppFlag | DISPLAY_BID_RANK_TO_SUPP_FLAG | — | ✅ |
| 139 | DisplayTransAmountSuppFlag | DISPLAY_TRANS_AMOUNT_SUPP_FLAG | — | ✅ |
| 140 | DoctypeId | DOCTYPE_ID | — | ✅ |
| 141 | DocumentNumber | DOCUMENT_NUMBER | — | ✅ |
| 142 | DraftLocked | DRAFT_LOCKED | — | ✅ |
| 143 | DraftLockedByPersonId | DRAFT_LOCKED_BY_PERSON_ID | — | ✅ |
| 144 | DraftLockedDate | DRAFT_LOCKED_DATE | — | ✅ |
| 145 | DraftUnlockedByPersonId | DRAFT_UNLOCKED_BY_PERSON_ID | — | ✅ |
| 146 | DraftUnlockedDate | DRAFT_UNLOCKED_DATE | — | ✅ |
| 147 | EnforcePrevrndBidDspFlag | ENFORCE_PREVRND_BID_DSP_FLAG | — | ✅ |
| 148 | EnforcePrevrndBidPriceFlag | ENFORCE_PREVRND_BID_PRICE_FLAG | — | ✅ |
| 149 | EventId | EVENT_ID | — | — |
| 150 | EventTitle | EVENT_TITLE | — | — |
| 151 | ExtAttribute1 | EXT_ATTRIBUTE1 | — | — |
| 152 | ExtAttribute10 | EXT_ATTRIBUTE10 | — | — |
| 153 | ExtAttribute11 | EXT_ATTRIBUTE11 | — | — |
| 154 | ExtAttribute12 | EXT_ATTRIBUTE12 | — | — |
| 155 | ExtAttribute13 | EXT_ATTRIBUTE13 | — | — |
| 156 | ExtAttribute14 | EXT_ATTRIBUTE14 | — | — |
| 157 | ExtAttribute15 | EXT_ATTRIBUTE15 | — | — |
| 158 | ExtAttribute16 | EXT_ATTRIBUTE16 | — | — |
| 159 | ExtAttribute17 | EXT_ATTRIBUTE17 | — | — |
| 160 | ExtAttribute18 | EXT_ATTRIBUTE18 | — | — |
| 161 | ExtAttribute19 | EXT_ATTRIBUTE19 | — | — |
| 162 | ExtAttribute2 | EXT_ATTRIBUTE2 | — | — |
| 163 | ExtAttribute20 | EXT_ATTRIBUTE20 | — | — |
| 164 | ExtAttribute3 | EXT_ATTRIBUTE3 | — | — |
| 165 | ExtAttribute4 | EXT_ATTRIBUTE4 | — | — |
| 166 | ExtAttribute5 | EXT_ATTRIBUTE5 | — | — |
| 167 | ExtAttribute6 | EXT_ATTRIBUTE6 | — | — |
| 168 | ExtAttribute7 | EXT_ATTRIBUTE7 | — | — |
| 169 | ExtAttribute8 | EXT_ATTRIBUTE8 | — | — |
| 170 | ExtAttribute9 | EXT_ATTRIBUTE9 | — | — |
| 171 | ExtAttributeCategory | EXT_ATTRIBUTE_CATEGORY | — | — |
| 172 | ExtAttributeDate1 | EXT_ATTRIBUTE_DATE1 | — | — |
| 173 | ExtAttributeDate10 | EXT_ATTRIBUTE_DATE10 | — | — |
| 174 | ExtAttributeDate2 | EXT_ATTRIBUTE_DATE2 | — | — |
| 175 | ExtAttributeDate3 | EXT_ATTRIBUTE_DATE3 | — | — |
| 176 | ExtAttributeDate4 | EXT_ATTRIBUTE_DATE4 | — | — |
| 177 | ExtAttributeDate5 | EXT_ATTRIBUTE_DATE5 | — | — |
| 178 | ExtAttributeDate6 | EXT_ATTRIBUTE_DATE6 | — | — |
| 179 | ExtAttributeDate7 | EXT_ATTRIBUTE_DATE7 | — | — |
| 180 | ExtAttributeDate8 | EXT_ATTRIBUTE_DATE8 | — | — |
| 181 | ExtAttributeDate9 | EXT_ATTRIBUTE_DATE9 | — | — |
| 182 | ExtAttributeNumber1 | EXT_ATTRIBUTE_NUMBER1 | — | — |
| 183 | ExtAttributeNumber10 | EXT_ATTRIBUTE_NUMBER10 | — | — |
| 184 | ExtAttributeNumber2 | EXT_ATTRIBUTE_NUMBER2 | — | — |
| 185 | ExtAttributeNumber3 | EXT_ATTRIBUTE_NUMBER3 | — | — |
| 186 | ExtAttributeNumber4 | EXT_ATTRIBUTE_NUMBER4 | — | — |
| 187 | ExtAttributeNumber5 | EXT_ATTRIBUTE_NUMBER5 | — | — |
| 188 | ExtAttributeNumber6 | EXT_ATTRIBUTE_NUMBER6 | — | — |
| 189 | ExtAttributeNumber7 | EXT_ATTRIBUTE_NUMBER7 | — | — |
| 190 | ExtAttributeNumber8 | EXT_ATTRIBUTE_NUMBER8 | — | — |
| 191 | ExtAttributeNumber9 | EXT_ATTRIBUTE_NUMBER9 | — | — |
| 192 | ExtAttributeTimestamp1 | EXT_ATTRIBUTE_TIMESTAMP1 | — | — |
| 193 | ExtAttributeTimestamp10 | EXT_ATTRIBUTE_TIMESTAMP10 | — | — |
| 194 | ExtAttributeTimestamp2 | EXT_ATTRIBUTE_TIMESTAMP2 | — | — |
| 195 | ExtAttributeTimestamp3 | EXT_ATTRIBUTE_TIMESTAMP3 | — | — |
| 196 | ExtAttributeTimestamp4 | EXT_ATTRIBUTE_TIMESTAMP4 | — | — |
| 197 | ExtAttributeTimestamp5 | EXT_ATTRIBUTE_TIMESTAMP5 | — | — |
| 198 | ExtAttributeTimestamp6 | EXT_ATTRIBUTE_TIMESTAMP6 | — | — |
| 199 | ExtAttributeTimestamp7 | EXT_ATTRIBUTE_TIMESTAMP7 | — | — |
| 200 | ExtAttributeTimestamp8 | EXT_ATTRIBUTE_TIMESTAMP8 | — | — |
| 201 | ExtAttributeTimestamp9 | EXT_ATTRIBUTE_TIMESTAMP9 | — | — |
| 202 | ExternalPoCreationStatus | EXTERNAL_PO_CREATION_STATUS | — | — |
| 203 | FirstLineCloseDate | FIRST_LINE_CLOSE_DATE | — | ✅ |
| 204 | FobCode | FOB_CODE | — | ✅ |
| 205 | FreightTermsCode | FREIGHT_TERMS_CODE | — | ✅ |
| 206 | FullQuantityBidCode | FULL_QUANTITY_BID_CODE | — | ✅ |
| 207 | FullQuantityBidDspFlag | FULL_QUANTITY_BID_DSP_FLAG | — | ✅ |
| 208 | GeneralIntroEnabledFlag | GENERAL_INTRO_ENABLED_FLAG | — | — |
| 209 | GeneralIntroText | GENERAL_INTRO_TEXT | — | — |
| 210 | GlobalTemplateFlag | GLOBAL_TEMPLATE_FLAG | — | — |
| 211 | GroupEnabledFlag | GROUP_ENABLED_FLAG | — | — |
| 212 | HasHdrAttrFlag | HAS_HDR_ATTR_FLAG | — | — |
| 213 | HasItemsFlag | HAS_ITEMS_FLAG | — | — |
| 214 | HasLineCurrentPrice | HAS_LINE_CURRENT_PRICE | — | — |
| 215 | HasPeForAllItems | HAS_PE_FOR_ALL_ITEMS | — | — |
| 216 | HasPriceElements | HAS_PRICE_ELEMENTS | — | — |
| 217 | HasScoringTeamsFlag | HAS_SCORING_TEAMS_FLAG | — | ✅ |
| 218 | HdrAttrDisplayScore | HDR_ATTR_DISPLAY_SCORE | — | ✅ |
| 219 | HdrAttrEnableWeights | HDR_ATTR_ENABLE_WEIGHTS | — | ✅ |
| 220 | HdrAttrMaximumScore | HDR_ATTR_MAXIMUM_SCORE | — | ✅ |
| 221 | HdrAttributeEnabledFlag | HDR_ATTRIBUTE_ENABLED_FLAG | — | ✅ |
| 222 | ImportFileName | IMPORT_FILE_NAME | — | — |
| 223 | IncludePdfInExternalPage | INCLUDE_PDF_IN_EXTERNAL_PAGE | — | — |
| 224 | IntAttribute1 | INT_ATTRIBUTE1 | — | — |
| 225 | IntAttribute10 | INT_ATTRIBUTE10 | — | — |
| 226 | IntAttribute11 | INT_ATTRIBUTE11 | — | — |
| 227 | IntAttribute12 | INT_ATTRIBUTE12 | — | — |
| 228 | IntAttribute13 | INT_ATTRIBUTE13 | — | — |
| 229 | IntAttribute14 | INT_ATTRIBUTE14 | — | — |
| 230 | IntAttribute15 | INT_ATTRIBUTE15 | — | — |
| 231 | IntAttribute2 | INT_ATTRIBUTE2 | — | — |
| 232 | IntAttribute3 | INT_ATTRIBUTE3 | — | — |
| 233 | IntAttribute4 | INT_ATTRIBUTE4 | — | — |
| 234 | IntAttribute5 | INT_ATTRIBUTE5 | — | — |
| 235 | IntAttribute6 | INT_ATTRIBUTE6 | — | — |
| 236 | IntAttribute7 | INT_ATTRIBUTE7 | — | — |
| 237 | IntAttribute8 | INT_ATTRIBUTE8 | — | — |
| 238 | IntAttribute9 | INT_ATTRIBUTE9 | — | — |
| 239 | IntAttributeCategory | INT_ATTRIBUTE_CATEGORY | — | — |
| 240 | InternalCfEnabledFlag | INTERNAL_CF_ENABLED_FLAG | — | — |
| 241 | IsCreatedFromRest | IS_CREATED_FROM_REST | — | — |
| 242 | IsPaused | IS_PAUSED | — | ✅ |
| 243 | IsTemplateFlag | IS_TEMPLATE_FLAG | — | — |
| 244 | LanguageCode | LANGUAGE_CODE | — | ✅ |
| 245 | LargeNegEnabledFlag | LARGE_NEG_ENABLED_FLAG | — | — |
| 246 | LastLineNumber | LAST_LINE_NUMBER | — | — |
| 247 | LastPauseDate | LAST_PAUSE_DATE | — | ✅ |
| 248 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 249 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 250 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 251 | LineAttributeEnabledFlag | LINE_ATTRIBUTE_ENABLED_FLAG | — | ✅ |
| 252 | LineDefaultsEnabledFlag | LINE_DEFAULTS_ENABLED_FLAG | — | ✅ |
| 253 | LineDefaultsExistFlag | LINE_DEFAULTS_EXIST_FLAG | — | ✅ |
| 254 | LineMasEnabledFlag | LINE_MAS_ENABLED_FLAG | — | ✅ |
| 255 | LinesInstrEnabledFlag | LINES_INSTR_ENABLED_FLAG | — | — |
| 256 | LinesInstrText | LINES_INSTR_TEXT | — | — |
| 257 | LotEnabledFlag | LOT_ENABLED_FLAG | — | — |
| 258 | MaxBidColorSequenceId | MAX_BID_COLOR_SEQUENCE_ID | — | — |
| 259 | MaxDocumentLineNum | MAX_DOCUMENT_LINE_NUM | — | — |
| 260 | MaxInternalLineNum | MAX_INTERNAL_LINE_NUM | — | — |
| 261 | MaxRetainageNegotiableFlag | MAX_RETAINAGE_NEGOTIABLE_FLAG | — | — |
| 262 | MinBidChangeType | MIN_BID_CHANGE_TYPE | — | ✅ |
| 263 | MinBidDecrement | MIN_BID_DECREMENT | — | ✅ |
| 264 | ModeOfTransport | MODE_OF_TRANSPORT | — | ✅ |
| 265 | NegApprIdentificationKey | NEG_APPR_IDENTIFICATION_KEY | — | — |
| 266 | NegApprovalDate | NEG_APPROVAL_DATE | — | ✅ |
| 267 | NegApprovalEnabledFlag | NEG_APPROVAL_ENABLED_FLAG | — | — |
| 268 | NegApprovalNote | NEG_APPROVAL_NOTE | — | — |
| 269 | NegApprovalStatus | NEG_APPROVAL_STATUS | — | ✅ |
| 270 | NegTeamEnabledFlag | NEG_TEAM_ENABLED_FLAG | — | ✅ |
| 271 | NegotiationLayoutId | NEGOTIATION_LAYOUT_ID | — | ✅ |
| 272 | NegotiationLayoutName | NEGOTIATION_LAYOUT_NAME | — | ✅ |
| 273 | NumberOfBids | NUMBER_OF_BIDS | — | ✅ |
| 274 | NumberOfExtensions | NUMBER_OF_EXTENSIONS | — | ✅ |
| 275 | NumberOfLines | NUMBER_OF_LINES | — | ✅ |
| 276 | NumberPriceDecimals | NUMBER_PRICE_DECIMALS | — | ✅ |
| 277 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 278 | OpenAuctionNowFlag | OPEN_AUCTION_NOW_FLAG | — | ✅ |
| 279 | OpenBiddingDate | OPEN_BIDDING_DATE | — | ✅ |
| 280 | OriginalCloseBiddingDate | ORIGINAL_CLOSE_BIDDING_DATE | — | ✅ |
| 281 | OutcomeStatus | OUTCOME_STATUS | — | ✅ |
| 282 | OverallRespRankEnabledFlag | OVERALL_RESP_RANK_ENABLED_FLAG | — | ✅ |
| 283 | PauseRemarks | PAUSE_REMARKS | — | ✅ |
| 284 | PaymentTermsId | PAYMENT_TERMS_ID | — | ✅ |
| 285 | PersonId | PERSON_ID | — | ✅ |
| 286 | PfTypeAllowed | PF_TYPE_ALLOWED | — | — |
| 287 | PoAgreedAmount | PO_AGREED_AMOUNT | — | ✅ |
| 288 | PoCreationProcess | PO_CREATION_PROCESS | — | — |
| 289 | PoEndDate | PO_END_DATE | — | ✅ |
| 290 | PoMinRelAmount | PO_MIN_REL_AMOUNT | — | ✅ |
| 291 | PoStartDate | PO_START_DATE | — | ✅ |
| 292 | PoStyleId | PO_STYLE_ID | — | ✅ |
| 293 | PowerBiddingEnabledFlag | POWER_BIDDING_ENABLED_FLAG | — | ✅ |
| 294 | PrcBuId | PRC_BU_ID | — | ✅ |
| 295 | PriceDrivenAuctionFlag | PRICE_DRIVEN_AUCTION_FLAG | — | — |
| 296 | PriceElementEnabledFlag | PRICE_ELEMENT_ENABLED_FLAG | — | — |
| 297 | PriceTiersIndicator | PRICE_TIERS_INDICATOR | — | ✅ |
| 298 | ProgramAppName | PROGRAM_APP_NAME | — | — |
| 299 | ProgramName | PROGRAM_NAME | — | — |
| 300 | ProgressPaymentType | PROGRESS_PAYMENT_TYPE | — | — |
| 301 | ProgressPymtNegotiableFlag | PROGRESS_PYMT_NEGOTIABLE_FLAG | — | — |
| 302 | ProjectId | PROJECT_ID | — | ✅ |
| 303 | ProjectsEnabledFlag | PROJECTS_ENABLED_FLAG | — | ✅ |
| 304 | ProxyBiddingEnabledFlag | PROXY_BIDDING_ENABLED_FLAG | — | ✅ |
| 305 | PublishAuctionNowFlag | PUBLISH_AUCTION_NOW_FLAG | — | ✅ |
| 306 | PublishDate | PUBLISH_DATE | — | ✅ |
| 307 | PublishDateOrigAmend | PUBLISH_DATE_ORIG_AMEND | — | ✅ |
| 308 | PublishRatesToBiddersFlag | PUBLISH_RATES_TO_BIDDERS_FLAG | — | ✅ |
| 309 | QtyPriceTiersEnabledFlag | QTY_PRICE_TIERS_ENABLED_FLAG | — | ✅ |
| 310 | RankIndicator | RANK_INDICATOR | — | ✅ |
| 311 | RateDate | RATE_DATE | — | ✅ |
| 312 | RateType | RATE_TYPE | — | ✅ |
| 313 | RebuildIndex | REBUILD_INDEX | — | — |
| 314 | RecoupmentNegotiableFlag | RECOUPMENT_NEGOTIABLE_FLAG | — | — |
| 315 | ReminderDate | REMINDER_DATE | — | ✅ |
| 316 | ReqBuId | REQ_BU_ID | — | ✅ |
| 317 | ReqmntsInstrEnabledFlag | REQMNTS_INSTR_ENABLED_FLAG | — | — |
| 318 | ReqmntsInstrText | REQMNTS_INSTR_TEXT | — | — |
| 319 | RequestDate | REQUEST_DATE | — | — |
| 320 | RequestId | REQUEST_ID | — | — |
| 321 | RequestedBy | REQUESTED_BY | — | — |
| 322 | RespLinesSpshetEnabledFlag | RESP_LINES_SPSHET_ENABLED_FLAG | — | — |
| 323 | RespReqtSpshetEnabledFlag | RESP_REQT_SPSHET_ENABLED_FLAG | — | — |
| 324 | RespSpshetEnabledFlag | RESP_SPSHET_ENABLED_FLAG | — | — |
| 325 | RespTabulationLayoutName | RESP_TABULATION_LAYOUT_NAME | — | ✅ |
| 326 | RespXmlSpshetEnabledFlag | RESP_XML_SPSHET_ENABLED_FLAG | — | — |
| 327 | ResponseLayoutId | RESPONSE_LAYOUT_ID | — | ✅ |
| 328 | ResponseLayoutName | RESPONSE_LAYOUT_NAME | — | ✅ |
| 329 | RetainageNegotiableFlag | RETAINAGE_NEGOTIABLE_FLAG | — | — |
| 330 | RfiLineEnabledFlag | RFI_LINE_ENABLED_FLAG | — | ✅ |
| 331 | ScoringLockDate | SCORING_LOCK_DATE | — | ✅ |
| 332 | ScoringLockPersonId | SCORING_LOCK_PERSON_ID | — | ✅ |
| 333 | ScoringOpenDate | SCORING_OPEN_DATE | — | ✅ |
| 334 | ScoringOpenPersonId | SCORING_OPEN_PERSON_ID | — | ✅ |
| 335 | ScoringStatus | SCORING_STATUS | — | ✅ |
| 336 | SealedActualUnlockDate | SEALED_ACTUAL_UNLOCK_DATE | — | ✅ |
| 337 | SealedActualUnsealDate | SEALED_ACTUAL_UNSEAL_DATE | — | ✅ |
| 338 | SealedAuctionStatus | SEALED_AUCTION_STATUS | — | ✅ |
| 339 | SealedUnlockPersonId | SEALED_UNLOCK_PERSON_ID | — | ✅ |
| 340 | SealedUnsealPersonId | SEALED_UNSEAL_PERSON_ID | — | ✅ |
| 341 | ServiceLevel | SERVICE_LEVEL | — | ✅ |
| 342 | ShareAwardDecision | SHARE_AWARD_DECISION | — | ✅ |
| 343 | ShareAwdDecisionDate | SHARE_AWD_DECISION_DATE | — | ✅ |
| 344 | ShowBidderNotes | SHOW_BIDDER_NOTES | — | ✅ |
| 345 | ShowBidderNotesDspFlag | SHOW_BIDDER_NOTES_DSP_FLAG | — | ✅ |
| 346 | ShowBidderScores | SHOW_BIDDER_SCORES | — | ✅ |
| 347 | SourceDocId | SOURCE_DOC_ID | — | — |
| 348 | SourceDocLineMsg | SOURCE_DOC_LINE_MSG | — | — |
| 349 | SourceDocMsg | SOURCE_DOC_MSG | — | — |
| 350 | SourceDocMsgApp | SOURCE_DOC_MSG_APP | — | — |
| 351 | SourceDocNumber | SOURCE_DOC_NUMBER | — | — |
| 352 | SourceReqsFlag | SOURCE_REQS_FLAG | — | — |
| 353 | StagCloseEnabledFlag | STAG_CLOSE_ENABLED_FLAG | — | ✅ |
| 354 | StaggeredClosingFlag | STAGGERED_CLOSING_FLAG | — | ✅ |
| 355 | StaggeredClosingInterval | STAGGERED_CLOSING_INTERVAL | — | ✅ |
| 356 | StyleId | STYLE_ID | — | ✅ |
| 357 | SupplierEnterablePymtFlag | SUPPLIER_ENTERABLE_PYMT_FLAG | — | — |
| 358 | SupplierViewType | SUPPLIER_VIEW_TYPE | — | ✅ |
| 359 | Synopsis | SYNOPSIS | — | ✅ |
| 360 | TeamScoringEnabledFlag | TEAM_SCORING_ENABLED_FLAG | — | ✅ |
| 361 | TechnicalActualUnlockDate | TECHNICAL_ACTUAL_UNLOCK_DATE | — | ✅ |
| 362 | TechnicalActualUnsealDate | TECHNICAL_ACTUAL_UNSEAL_DATE | — | ✅ |
| 363 | TechnicalEvaluationStatus | TECHNICAL_EVALUATION_STATUS | — | ✅ |
| 364 | TechnicalLockStatus | TECHNICAL_LOCK_STATUS | — | ✅ |
| 365 | TechnicalScoringStatus | TECHNICAL_SCORING_STATUS | — | ✅ |
| 366 | TechnicalUnlockPersonId | TECHNICAL_UNLOCK_PERSON_ID | — | ✅ |
| 367 | TechnicalUnsealPersonId | TECHNICAL_UNSEAL_PERSON_ID | — | ✅ |
| 368 | TemplateId | TEMPLATE_ID | — | — |
| 369 | TemplateScope | TEMPLATE_SCOPE | — | — |
| 370 | TemplateStatus | TEMPLATE_STATUS | — | — |
| 371 | TermsInstrEnabledFlag | TERMS_INSTR_ENABLED_FLAG | — | — |
| 372 | TermsInstrText | TERMS_INSTR_TEXT | — | — |
| 373 | TwoPartFlag | TWO_PART_FLAG | — | ✅ |
| 374 | TwostageEvalEnabledFlag | TWOSTAGE_EVAL_ENABLED_FLAG | — | ✅ |
| 375 | VersionNum | VERSION_NUM | — | — |
| 376 | ViewByDate | VIEW_BY_DATE | — | ✅ |
| 377 | WfApprovalItemKey | WF_APPROVAL_ITEM_KEY | — | — |
| 378 | WfAwardApprovalItemKey | WF_AWARD_APPROVAL_ITEM_KEY | — | — |
| 379 | WfItemKey | WF_ITEM_KEY | — | — |
| 380 | WfPoncomplCurrentRound | WF_PONCOMPL_CURRENT_ROUND | — | — |
| 381 | WfPoncomplItemKey | WF_PONCOMPL_ITEM_KEY | — | — |
| 382 | WfRoleName | WF_ROLE_NAME | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
