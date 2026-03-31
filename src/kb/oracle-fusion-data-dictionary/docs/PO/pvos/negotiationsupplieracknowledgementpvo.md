---
id: DOC-PO-PVO-NegotiationSupplierAcknowledgementPVO
doc_type: system-doc
title: "NegotiationSupplierAcknowledgementPVO — PVO Purchasing"
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
  - NegotiationSupplierAcknowledgementPVO
  - negotiationsupplieracknowledgementpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationSupplierAcknowledgementPVO

## 📌 Visão Geral

Extrai as confirmações de recebimento (acknowledgements) de fornecedores para convites de negociação. Permite monitorar engajamento e identificar fornecedores que não responderam ao convite.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.NegotiationSupplierAcknowledgementPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 387 | 4 | 2 | 387 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 12 atributos (12 BICC)
- [[hz_parties|HZ_PARTIES]] — 150 atributos (150 BICC)
- [[pon_acknowledgements|PON_ACKNOWLEDGEMENTS]] — 13 atributos (2 PKs, 13 BICC)
- [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]] — 212 atributos (212 BICC)

---

## ⚙️ Atributos

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

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TradingPartnerAddress1 | ADDRESS1 | — | ✅ |
| 2 | TradingPartnerAddress2 | ADDRESS2 | — | ✅ |
| 3 | TradingPartnerAddress3 | ADDRESS3 | — | ✅ |
| 4 | TradingPartnerAddress4 | ADDRESS4 | — | ✅ |
| 5 | TradingPartnerAnalysisFy | ANALYSIS_FY | — | ✅ |
| 6 | TradingPartnerCategoryCode | CATEGORY_CODE | — | ✅ |
| 7 | TradingPartnerCeoName | CEO_NAME | — | ✅ |
| 8 | TradingPartnerCertReasonCode | CERT_REASON_CODE | — | ✅ |
| 9 | TradingPartnerCertificationLevel | CERTIFICATION_LEVEL | — | ✅ |
| 10 | TradingPartnerCity | CITY | — | ✅ |
| 11 | TradingPartnerComments | COMMENTS | — | ✅ |
| 12 | TradingPartnerContactAddress1 | ADDRESS1 | — | ✅ |
| 13 | TradingPartnerContactAddress2 | ADDRESS2 | — | ✅ |
| 14 | TradingPartnerContactAddress3 | ADDRESS3 | — | ✅ |
| 15 | TradingPartnerContactAddress4 | ADDRESS4 | — | ✅ |
| 16 | TradingPartnerContactAnalysisFy | ANALYSIS_FY | — | ✅ |
| 17 | TradingPartnerContactCategoryCode | CATEGORY_CODE | — | ✅ |
| 18 | TradingPartnerContactCeoName | CEO_NAME | — | ✅ |
| 19 | TradingPartnerContactCertReasonCode | CERT_REASON_CODE | — | ✅ |
| 20 | TradingPartnerContactCertificationLevel | CERTIFICATION_LEVEL | — | ✅ |
| 21 | TradingPartnerContactCity | CITY | — | ✅ |
| 22 | TradingPartnerContactComments | COMMENTS | — | ✅ |
| 23 | TradingPartnerContactCountry | COUNTRY | — | ✅ |
| 24 | TradingPartnerContactCounty | COUNTY | — | ✅ |
| 25 | TradingPartnerContactCreatedByModule | CREATED_BY_MODULE | — | ✅ |
| 26 | TradingPartnerContactCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | ✅ |
| 27 | TradingPartnerContactDateOfBirth | DATE_OF_BIRTH | — | ✅ |
| 28 | TradingPartnerContactDunsNumberC | DUNS_NUMBER_C | — | ✅ |
| 29 | TradingPartnerContactEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 30 | TradingPartnerContactEmployeesTotal | EMPLOYEES_TOTAL | — | ✅ |
| 31 | TradingPartnerContactFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | ✅ |
| 32 | TradingPartnerContactGender | GENDER | — | ✅ |
| 33 | TradingPartnerContactGroupType | GROUP_TYPE | — | ✅ |
| 34 | TradingPartnerContactGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | ✅ |
| 35 | TradingPartnerContactHomeCountry | HOME_COUNTRY | — | ✅ |
| 36 | TradingPartnerContactHqBranchInd | HQ_BRANCH_IND | — | ✅ |
| 37 | TradingPartnerContactIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | ✅ |
| 38 | TradingPartnerContactIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | ✅ |
| 39 | TradingPartnerContactInternalFlag | INTERNAL_FLAG | — | ✅ |
| 40 | TradingPartnerContactJgzzFiscalCode | JGZZ_FISCAL_CODE | — | ✅ |
| 41 | TradingPartnerContactLanguageName | LANGUAGE_NAME | — | ✅ |
| 42 | TradingPartnerContactMaritalStatus | MARITAL_STATUS | — | ✅ |
| 43 | TradingPartnerContactMissionStatement | MISSION_STATEMENT | — | ✅ |
| 44 | TradingPartnerContactNextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | ✅ |
| 45 | TradingPartnerContactOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | ✅ |
| 46 | TradingPartnerContactPartyId | PARTY_ID | — | ✅ |
| 47 | TradingPartnerContactPartyName | PARTY_NAME | — | ✅ |
| 48 | TradingPartnerContactPartyNumber | PARTY_NUMBER | — | ✅ |
| 49 | TradingPartnerContactPartyType | PARTY_TYPE | — | ✅ |
| 50 | TradingPartnerContactPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | ✅ |
| 51 | TradingPartnerContactPersonFirstName | PERSON_FIRST_NAME | — | ✅ |
| 52 | TradingPartnerContactPersonLastName | PERSON_LAST_NAME | — | ✅ |
| 53 | TradingPartnerContactPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | ✅ |
| 54 | TradingPartnerContactPersonMiddleName | PERSON_MIDDLE_NAME | — | ✅ |
| 55 | TradingPartnerContactPersonNameSuffix | PERSON_NAME_SUFFIX | — | ✅ |
| 56 | TradingPartnerContactPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | ✅ |
| 57 | TradingPartnerContactPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | ✅ |
| 58 | TradingPartnerContactPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | ✅ |
| 59 | TradingPartnerContactPersonTitle | PERSON_TITLE | — | ✅ |
| 60 | TradingPartnerContactPostalCode | POSTAL_CODE | — | ✅ |
| 61 | TradingPartnerContactPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | ✅ |
| 62 | TradingPartnerContactPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | ✅ |
| 63 | TradingPartnerContactPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | ✅ |
| 64 | TradingPartnerContactPreferredName | PREFERRED_NAME | — | ✅ |
| 65 | TradingPartnerContactPreferredNameId | PREFERRED_NAME_ID | — | ✅ |
| 66 | TradingPartnerContactPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | ✅ |
| 67 | TradingPartnerContactPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | ✅ |
| 68 | TradingPartnerContactPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | ✅ |
| 69 | TradingPartnerContactPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | ✅ |
| 70 | TradingPartnerContactPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | ✅ |
| 71 | TradingPartnerContactPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | ✅ |
| 72 | TradingPartnerContactPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | ✅ |
| 73 | TradingPartnerContactPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | ✅ |
| 74 | TradingPartnerContactPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | ✅ |
| 75 | TradingPartnerContactProvince | PROVINCE | — | ✅ |
| 76 | TradingPartnerContactSalutation | SALUTATION | — | ✅ |
| 77 | TradingPartnerContactSicCode | SIC_CODE | — | ✅ |
| 78 | TradingPartnerContactSicCodeType | SIC_CODE_TYPE | — | ✅ |
| 79 | TradingPartnerContactState | STATE | — | ✅ |
| 80 | TradingPartnerContactStatus | STATUS | — | ✅ |
| 81 | TradingPartnerContactThirdPartyFlag | THIRD_PARTY_FLAG | — | ✅ |
| 82 | TradingPartnerContactTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | ✅ |
| 83 | TradingPartnerContactUrl | URL | — | ✅ |
| 84 | TradingPartnerContactUserGuid | USER_GUID | — | ✅ |
| 85 | TradingPartnerContactValidatedFlag | VALIDATED_FLAG | — | ✅ |
| 86 | TradingPartnerContactYearEstablished | YEAR_ESTABLISHED | — | ✅ |
| 87 | TradingPartnerCountry | COUNTRY | — | ✅ |
| 88 | TradingPartnerCounty | COUNTY | — | ✅ |
| 89 | TradingPartnerCreatedByModule | CREATED_BY_MODULE | — | ✅ |
| 90 | TradingPartnerCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | ✅ |
| 91 | TradingPartnerDateOfBirth | DATE_OF_BIRTH | — | ✅ |
| 92 | TradingPartnerDunsNumberC | DUNS_NUMBER_C | — | ✅ |
| 93 | TradingPartnerEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 94 | TradingPartnerEmployeesTotal | EMPLOYEES_TOTAL | — | ✅ |
| 95 | TradingPartnerFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | ✅ |
| 96 | TradingPartnerGender | GENDER | — | ✅ |
| 97 | TradingPartnerGroupType | GROUP_TYPE | — | ✅ |
| 98 | TradingPartnerGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | ✅ |
| 99 | TradingPartnerHomeCountry | HOME_COUNTRY | — | ✅ |
| 100 | TradingPartnerHqBranchInd | HQ_BRANCH_IND | — | ✅ |
| 101 | TradingPartnerIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | ✅ |
| 102 | TradingPartnerIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | ✅ |
| 103 | TradingPartnerInternalFlag | INTERNAL_FLAG | — | ✅ |
| 104 | TradingPartnerJgzzFiscalCode | JGZZ_FISCAL_CODE | — | ✅ |
| 105 | TradingPartnerLanguageName | LANGUAGE_NAME | — | ✅ |
| 106 | TradingPartnerMaritalStatus | MARITAL_STATUS | — | ✅ |
| 107 | TradingPartnerMissionStatement | MISSION_STATEMENT | — | ✅ |
| 108 | TradingPartnerNextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | ✅ |
| 109 | TradingPartnerOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | ✅ |
| 110 | TradingPartnerPartyId | PARTY_ID | — | ✅ |
| 111 | TradingPartnerPartyName | PARTY_NAME | — | ✅ |
| 112 | TradingPartnerPartyNumber | PARTY_NUMBER | — | ✅ |
| 113 | TradingPartnerPartyType | PARTY_TYPE | — | ✅ |
| 114 | TradingPartnerPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | ✅ |
| 115 | TradingPartnerPersonFirstName | PERSON_FIRST_NAME | — | ✅ |
| 116 | TradingPartnerPersonLastName | PERSON_LAST_NAME | — | ✅ |
| 117 | TradingPartnerPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | ✅ |
| 118 | TradingPartnerPersonMiddleName | PERSON_MIDDLE_NAME | — | ✅ |
| 119 | TradingPartnerPersonNameSuffix | PERSON_NAME_SUFFIX | — | ✅ |
| 120 | TradingPartnerPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | ✅ |
| 121 | TradingPartnerPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | ✅ |
| 122 | TradingPartnerPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | ✅ |
| 123 | TradingPartnerPersonTitle | PERSON_TITLE | — | ✅ |
| 124 | TradingPartnerPostalCode | POSTAL_CODE | — | ✅ |
| 125 | TradingPartnerPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | ✅ |
| 126 | TradingPartnerPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | ✅ |
| 127 | TradingPartnerPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | ✅ |
| 128 | TradingPartnerPreferredName | PREFERRED_NAME | — | ✅ |
| 129 | TradingPartnerPreferredNameId | PREFERRED_NAME_ID | — | ✅ |
| 130 | TradingPartnerPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | ✅ |
| 131 | TradingPartnerPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | ✅ |
| 132 | TradingPartnerPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | ✅ |
| 133 | TradingPartnerPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | ✅ |
| 134 | TradingPartnerPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | ✅ |
| 135 | TradingPartnerPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | ✅ |
| 136 | TradingPartnerPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | ✅ |
| 137 | TradingPartnerPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | ✅ |
| 138 | TradingPartnerPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | ✅ |
| 139 | TradingPartnerProvince | PROVINCE | — | ✅ |
| 140 | TradingPartnerSalutation | SALUTATION | — | ✅ |
| 141 | TradingPartnerSicCode | SIC_CODE | — | ✅ |
| 142 | TradingPartnerSicCodeType | SIC_CODE_TYPE | — | ✅ |
| 143 | TradingPartnerState | STATE | — | ✅ |
| 144 | TradingPartnerStatus | STATUS | — | ✅ |
| 145 | TradingPartnerThirdPartyFlag | THIRD_PARTY_FLAG | — | ✅ |
| 146 | TradingPartnerTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | ✅ |
| 147 | TradingPartnerUrl | URL | — | ✅ |
| 148 | TradingPartnerUserGuid | USER_GUID | — | ✅ |
| 149 | TradingPartnerValidatedFlag | VALIDATED_FLAG | — | ✅ |
| 150 | TradingPartnerYearEstablished | YEAR_ESTABLISHED | — | ✅ |

### [[pon_acknowledgements|PON_ACKNOWLEDGEMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AuctionHeaderId | AUCTION_HEADER_ID | 🔑 | ✅ |
| 2 | NegSuppAckAcknowledgementDate | ACKNOWLEDGEMENT_DATE | — | ✅ |
| 3 | NegSuppAckAcknowledgementResponse | ACKNOWLEDGEMENT_RESPONSE | — | ✅ |
| 4 | NegSuppAckCreatedBy | CREATED_BY | — | ✅ |
| 5 | NegSuppAckCreationDate | CREATION_DATE | — | ✅ |
| 6 | NegSuppAckLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | NegSuppAckLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | NegSuppAckLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | NegSuppAckObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | NegSuppAckSurrogBidAckFlag | SURROG_BID_ACK_FLAG | — | ✅ |
| 11 | NegSuppAckSurrogBidAckPersonId | SURROG_BID_ACK_PERSON_ID | — | ✅ |
| 12 | NegSuppAckTradingPartnerId | TRADING_PARTNER_ID | — | ✅ |
| 13 | TradingPartnerContactId | TRADING_PARTNER_CONTACT_ID | 🔑 | ✅ |

### [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationHeaderAbstractDetails | ABSTRACT_DETAILS | — | ✅ |
| 2 | NegotiationHeaderAbstractStatus | ABSTRACT_STATUS | — | ✅ |
| 3 | NegotiationHeaderAdvanceNegotiableFlag | ADVANCE_NEGOTIABLE_FLAG | — | ✅ |
| 4 | NegotiationHeaderAllowOtherBidCurrencyFlag | ALLOW_OTHER_BID_CURRENCY_FLAG | — | ✅ |
| 5 | NegotiationHeaderAmendmentDescription | AMENDMENT_DESCRIPTION | — | ✅ |
| 6 | NegotiationHeaderAmendmentNumber | AMENDMENT_NUMBER | — | ✅ |
| 7 | NegotiationHeaderApprovalStatus | NEG_APPROVAL_STATUS | — | ✅ |
| 8 | NegotiationHeaderAttributeLineNumber | ATTRIBUTE_LINE_NUMBER | — | ✅ |
| 9 | NegotiationHeaderAttributesExist | ATTRIBUTES_EXIST | — | ✅ |
| 10 | NegotiationHeaderAuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 11 | NegotiationHeaderAuctionHeaderIdOrigAmend | AUCTION_HEADER_ID_ORIG_AMEND | — | ✅ |
| 12 | NegotiationHeaderAuctionHeaderIdOrigRound | AUCTION_HEADER_ID_ORIG_ROUND | — | ✅ |
| 13 | NegotiationHeaderAuctionHeaderIdPrevAmend | AUCTION_HEADER_ID_PREV_AMEND | — | ✅ |
| 14 | NegotiationHeaderAuctionHeaderIdPrevRound | AUCTION_HEADER_ID_PREV_ROUND | — | ✅ |
| 15 | NegotiationHeaderAuctionOriginationCode | AUCTION_ORIGINATION_CODE | — | ✅ |
| 16 | NegotiationHeaderAuctionRoundNumber | AUCTION_ROUND_NUMBER | — | ✅ |
| 17 | NegotiationHeaderAuctionStatus | AUCTION_STATUS | — | ✅ |
| 18 | NegotiationHeaderAuctionTitle | AUCTION_TITLE | — | ✅ |
| 19 | NegotiationHeaderAutoExtendAllLinesFlag | AUTO_EXTEND_ALL_LINES_FLAG | — | ✅ |
| 20 | NegotiationHeaderAutoExtendDuration | AUTO_EXTEND_DURATION | — | ✅ |
| 21 | NegotiationHeaderAutoExtendEnabledFlag | AUTO_EXTEND_ENABLED_FLAG | — | ✅ |
| 22 | NegotiationHeaderAutoExtendFlag | AUTO_EXTEND_FLAG | — | ✅ |
| 23 | NegotiationHeaderAutoExtendMinTriggerRank | AUTO_EXTEND_MIN_TRIGGER_RANK | — | ✅ |
| 24 | NegotiationHeaderAutoExtendNumber | AUTO_EXTEND_NUMBER | — | ✅ |
| 25 | NegotiationHeaderAutoExtendTypeFlag | AUTO_EXTEND_TYPE_FLAG | — | ✅ |
| 26 | NegotiationHeaderAutoextendChangedFlag | AUTOEXTEND_CHANGED_FLAG | — | ✅ |
| 27 | NegotiationHeaderAwardApprAmeTransId | AWARD_APPR_AME_TRANS_ID | — | ✅ |
| 28 | NegotiationHeaderAwardApprAmeTransPrevId | AWARD_APPR_AME_TRANS_PREV_ID | — | ✅ |
| 29 | NegotiationHeaderAwardApprAmeTxnDate | AWARD_APPR_AME_TXN_DATE | — | ✅ |
| 30 | NegotiationHeaderAwardApprovalFlag | AWARD_APPROVAL_FLAG | — | ✅ |
| 31 | NegotiationHeaderAwardApprovalStatus | AWARD_APPROVAL_STATUS | — | ✅ |
| 32 | NegotiationHeaderAwardByDate | AWARD_BY_DATE | — | ✅ |
| 33 | NegotiationHeaderAwardCompleteDate | AWARD_COMPLETE_DATE | — | ✅ |
| 34 | NegotiationHeaderAwardDate | AWARD_DATE | — | ✅ |
| 35 | NegotiationHeaderAwardMode | AWARD_MODE | — | ✅ |
| 36 | NegotiationHeaderAwardStatus | AWARD_STATUS | — | ✅ |
| 37 | NegotiationHeaderBidDecrementMethod | BID_DECREMENT_METHOD | — | ✅ |
| 38 | NegotiationHeaderBidFrequencyCode | BID_FREQUENCY_CODE | — | ✅ |
| 39 | NegotiationHeaderBidListType | BID_LIST_TYPE | — | ✅ |
| 40 | NegotiationHeaderBidRanking | BID_RANKING | — | ✅ |
| 41 | NegotiationHeaderBidScopeCode | BID_SCOPE_CODE | — | ✅ |
| 42 | NegotiationHeaderBidVisibilityCode | BID_VISIBILITY_CODE | — | ✅ |
| 43 | NegotiationHeaderCancelDate | CANCEL_DATE | — | ✅ |
| 44 | NegotiationHeaderCarrierId | CARRIER_ID | — | ✅ |
| 45 | NegotiationHeaderCloseBiddingDate | CLOSE_BIDDING_DATE | — | ✅ |
| 46 | NegotiationHeaderCompleteFlag | COMPLETE_FLAG | — | ✅ |
| 47 | NegotiationHeaderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | ✅ |
| 48 | NegotiationHeaderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | ✅ |
| 49 | NegotiationHeaderContermsExistFlag | CONTERMS_EXIST_FLAG | — | ✅ |
| 50 | NegotiationHeaderContractTemplateId | CONTRACT_TEMPLATE_ID | — | ✅ |
| 51 | NegotiationHeaderContractType | CONTRACT_TYPE | — | ✅ |
| 52 | NegotiationHeaderCreatedBy | CREATED_BY | — | ✅ |
| 53 | NegotiationHeaderCreationDate | CREATION_DATE | — | ✅ |
| 54 | NegotiationHeaderCreationDateOrigAmend | CREATION_DATE_ORIG_AMEND | — | ✅ |
| 55 | NegotiationHeaderCurrencyCode | CURRENCY_CODE | — | ✅ |
| 56 | NegotiationHeaderDescription | DESCRIPTION | — | ✅ |
| 57 | NegotiationHeaderDisplayBestPriceBlindFlag | DISPLAY_BEST_PRICE_BLIND_FLAG | — | ✅ |
| 58 | NegotiationHeaderDoctypeId | DOCTYPE_ID | — | ✅ |
| 59 | NegotiationHeaderDocumentNumber | DOCUMENT_NUMBER | — | ✅ |
| 60 | NegotiationHeaderDraftLocked | DRAFT_LOCKED | — | ✅ |
| 61 | NegotiationHeaderDraftLockedDate | DRAFT_LOCKED_DATE | — | ✅ |
| 62 | NegotiationHeaderDraftUnlockedDate | DRAFT_UNLOCKED_DATE | — | ✅ |
| 63 | NegotiationHeaderEnforcePrevrndBidPriceFlag | ENFORCE_PREVRND_BID_PRICE_FLAG | — | ✅ |
| 64 | NegotiationHeaderEventId | EVENT_ID | — | ✅ |
| 65 | NegotiationHeaderEventTitle | EVENT_TITLE | — | ✅ |
| 66 | NegotiationHeaderExtAttribute1 | EXT_ATTRIBUTE1 | — | ✅ |
| 67 | NegotiationHeaderExtAttribute10 | EXT_ATTRIBUTE10 | — | ✅ |
| 68 | NegotiationHeaderExtAttribute11 | EXT_ATTRIBUTE11 | — | ✅ |
| 69 | NegotiationHeaderExtAttribute12 | EXT_ATTRIBUTE12 | — | ✅ |
| 70 | NegotiationHeaderExtAttribute13 | EXT_ATTRIBUTE13 | — | ✅ |
| 71 | NegotiationHeaderExtAttribute14 | EXT_ATTRIBUTE14 | — | ✅ |
| 72 | NegotiationHeaderExtAttribute15 | EXT_ATTRIBUTE15 | — | ✅ |
| 73 | NegotiationHeaderExtAttribute2 | EXT_ATTRIBUTE2 | — | ✅ |
| 74 | NegotiationHeaderExtAttribute3 | EXT_ATTRIBUTE3 | — | ✅ |
| 75 | NegotiationHeaderExtAttribute4 | EXT_ATTRIBUTE4 | — | ✅ |
| 76 | NegotiationHeaderExtAttribute5 | EXT_ATTRIBUTE5 | — | ✅ |
| 77 | NegotiationHeaderExtAttribute6 | EXT_ATTRIBUTE6 | — | ✅ |
| 78 | NegotiationHeaderExtAttribute7 | EXT_ATTRIBUTE7 | — | ✅ |
| 79 | NegotiationHeaderExtAttribute8 | EXT_ATTRIBUTE8 | — | ✅ |
| 80 | NegotiationHeaderExtAttribute9 | EXT_ATTRIBUTE9 | — | ✅ |
| 81 | NegotiationHeaderExtAttributeCategory | EXT_ATTRIBUTE_CATEGORY | — | ✅ |
| 82 | NegotiationHeaderFirstLineCloseDate | FIRST_LINE_CLOSE_DATE | — | ✅ |
| 83 | NegotiationHeaderFobCode | FOB_CODE | — | ✅ |
| 84 | NegotiationHeaderFreightTermsCode | FREIGHT_TERMS_CODE | — | ✅ |
| 85 | NegotiationHeaderFullQuantityBidCode | FULL_QUANTITY_BID_CODE | — | ✅ |
| 86 | NegotiationHeaderGlobalTemplateFlag | GLOBAL_TEMPLATE_FLAG | — | ✅ |
| 87 | NegotiationHeaderGroupEnabledFlag | GROUP_ENABLED_FLAG | — | ✅ |
| 88 | NegotiationHeaderHasHdrAttrFlag | HAS_HDR_ATTR_FLAG | — | ✅ |
| 89 | NegotiationHeaderHasItemsFlag | HAS_ITEMS_FLAG | — | ✅ |
| 90 | NegotiationHeaderHasPeForAllItems | HAS_PE_FOR_ALL_ITEMS | — | ✅ |
| 91 | NegotiationHeaderHasPriceElements | HAS_PRICE_ELEMENTS | — | ✅ |
| 92 | NegotiationHeaderHasScoringTeamsFlag | HAS_SCORING_TEAMS_FLAG | — | ✅ |
| 93 | NegotiationHeaderHdrAttrDisplayScore | HDR_ATTR_DISPLAY_SCORE | — | ✅ |
| 94 | NegotiationHeaderHdrAttrEnableWeights | HDR_ATTR_ENABLE_WEIGHTS | — | ✅ |
| 95 | NegotiationHeaderHdrAttrMaximumScore | HDR_ATTR_MAXIMUM_SCORE | — | ✅ |
| 96 | NegotiationHeaderHdrAttributeEnabledFlag | HDR_ATTRIBUTE_ENABLED_FLAG | — | ✅ |
| 97 | NegotiationHeaderImportFileName | IMPORT_FILE_NAME | — | ✅ |
| 98 | NegotiationHeaderIncludePdfInExternalPage | INCLUDE_PDF_IN_EXTERNAL_PAGE | — | ✅ |
| 99 | NegotiationHeaderIntAttribute1 | INT_ATTRIBUTE1 | — | ✅ |
| 100 | NegotiationHeaderIntAttribute10 | INT_ATTRIBUTE10 | — | ✅ |
| 101 | NegotiationHeaderIntAttribute11 | INT_ATTRIBUTE11 | — | ✅ |
| 102 | NegotiationHeaderIntAttribute12 | INT_ATTRIBUTE12 | — | ✅ |
| 103 | NegotiationHeaderIntAttribute13 | INT_ATTRIBUTE13 | — | ✅ |
| 104 | NegotiationHeaderIntAttribute14 | INT_ATTRIBUTE14 | — | ✅ |
| 105 | NegotiationHeaderIntAttribute15 | INT_ATTRIBUTE15 | — | ✅ |
| 106 | NegotiationHeaderIntAttribute2 | INT_ATTRIBUTE2 | — | ✅ |
| 107 | NegotiationHeaderIntAttribute3 | INT_ATTRIBUTE3 | — | ✅ |
| 108 | NegotiationHeaderIntAttribute4 | INT_ATTRIBUTE4 | — | ✅ |
| 109 | NegotiationHeaderIntAttribute5 | INT_ATTRIBUTE5 | — | ✅ |
| 110 | NegotiationHeaderIntAttribute6 | INT_ATTRIBUTE6 | — | ✅ |
| 111 | NegotiationHeaderIntAttribute7 | INT_ATTRIBUTE7 | — | ✅ |
| 112 | NegotiationHeaderIntAttribute8 | INT_ATTRIBUTE8 | — | ✅ |
| 113 | NegotiationHeaderIntAttribute9 | INT_ATTRIBUTE9 | — | ✅ |
| 114 | NegotiationHeaderIntAttributeCategory | INT_ATTRIBUTE_CATEGORY | — | ✅ |
| 115 | NegotiationHeaderIsPaused | IS_PAUSED | — | ✅ |
| 116 | NegotiationHeaderIsTemplateFlag | IS_TEMPLATE_FLAG | — | ✅ |
| 117 | NegotiationHeaderLanguageCode | LANGUAGE_CODE | — | ✅ |
| 118 | NegotiationHeaderLargeNegEnabledFlag | LARGE_NEG_ENABLED_FLAG | — | ✅ |
| 119 | NegotiationHeaderLastLineNumber | LAST_LINE_NUMBER | — | ✅ |
| 120 | NegotiationHeaderLastPauseDate | LAST_PAUSE_DATE | — | ✅ |
| 121 | NegotiationHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 122 | NegotiationHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 123 | NegotiationHeaderLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 124 | NegotiationHeaderLineAttributeEnabledFlag | LINE_ATTRIBUTE_ENABLED_FLAG | — | ✅ |
| 125 | NegotiationHeaderLineMasEnabledFlag | LINE_MAS_ENABLED_FLAG | — | ✅ |
| 126 | NegotiationHeaderLotEnabledFlag | LOT_ENABLED_FLAG | — | ✅ |
| 127 | NegotiationHeaderMaxBidColorSequenceId | MAX_BID_COLOR_SEQUENCE_ID | — | ✅ |
| 128 | NegotiationHeaderMaxDocumentLineNum | MAX_DOCUMENT_LINE_NUM | — | ✅ |
| 129 | NegotiationHeaderMaxInternalLineNum | MAX_INTERNAL_LINE_NUM | — | ✅ |
| 130 | NegotiationHeaderMaxRetainageNegotiableFlag | MAX_RETAINAGE_NEGOTIABLE_FLAG | — | ✅ |
| 131 | NegotiationHeaderMinBidChangeType | MIN_BID_CHANGE_TYPE | — | ✅ |
| 132 | NegotiationHeaderMinBidDecrement | MIN_BID_DECREMENT | — | ✅ |
| 133 | NegotiationHeaderNegTeamEnabledFlag | NEG_TEAM_ENABLED_FLAG | — | ✅ |
| 134 | NegotiationHeaderNumberOfBids | NUMBER_OF_BIDS | — | ✅ |
| 135 | NegotiationHeaderNumberOfExtensions | NUMBER_OF_EXTENSIONS | — | ✅ |
| 136 | NegotiationHeaderNumberOfLines | NUMBER_OF_LINES | — | ✅ |
| 137 | NegotiationHeaderNumberPriceDecimals | NUMBER_PRICE_DECIMALS | — | ✅ |
| 138 | NegotiationHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 139 | NegotiationHeaderOpenAuctionNowFlag | OPEN_AUCTION_NOW_FLAG | — | ✅ |
| 140 | NegotiationHeaderOpenBiddingDate | OPEN_BIDDING_DATE | — | ✅ |
| 141 | NegotiationHeaderOriginalCloseBiddingDate | ORIGINAL_CLOSE_BIDDING_DATE | — | ✅ |
| 142 | NegotiationHeaderOutcomeStatus | OUTCOME_STATUS | — | ✅ |
| 143 | NegotiationHeaderPauseRemarks | PAUSE_REMARKS | — | ✅ |
| 144 | NegotiationHeaderPaymentTermsId | PAYMENT_TERMS_ID | — | ✅ |
| 145 | NegotiationHeaderPersonId | PERSON_ID | — | ✅ |
| 146 | NegotiationHeaderPfTypeAllowed | PF_TYPE_ALLOWED | — | ✅ |
| 147 | NegotiationHeaderPoAgreedAmount | PO_AGREED_AMOUNT | — | ✅ |
| 148 | NegotiationHeaderPoEndDate | PO_END_DATE | — | ✅ |
| 149 | NegotiationHeaderPoMinRelAmount | PO_MIN_REL_AMOUNT | — | ✅ |
| 150 | NegotiationHeaderPoStartDate | PO_START_DATE | — | ✅ |
| 151 | NegotiationHeaderPoStyleId | PO_STYLE_ID | — | ✅ |
| 152 | NegotiationHeaderPowerBiddingEnabledFlag | POWER_BIDDING_ENABLED_FLAG | — | ✅ |
| 153 | NegotiationHeaderPrcBuId | PRC_BU_ID | — | ✅ |
| 154 | NegotiationHeaderPriceDrivenAuctionFlag | PRICE_DRIVEN_AUCTION_FLAG | — | ✅ |
| 155 | NegotiationHeaderPriceElementEnabledFlag | PRICE_ELEMENT_ENABLED_FLAG | — | ✅ |
| 156 | NegotiationHeaderPriceTiersIndicator | PRICE_TIERS_INDICATOR | — | ✅ |
| 157 | NegotiationHeaderProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 158 | NegotiationHeaderProgramName | PROGRAM_NAME | — | ✅ |
| 159 | NegotiationHeaderProgressPaymentType | PROGRESS_PAYMENT_TYPE | — | ✅ |
| 160 | NegotiationHeaderProgressPymtNegotiableFlag | PROGRESS_PYMT_NEGOTIABLE_FLAG | — | ✅ |
| 161 | NegotiationHeaderProjectId | PROJECT_ID | — | ✅ |
| 162 | NegotiationHeaderProxyBiddingEnabledFlag | PROXY_BIDDING_ENABLED_FLAG | — | ✅ |
| 163 | NegotiationHeaderPublishAuctionNowFlag | PUBLISH_AUCTION_NOW_FLAG | — | ✅ |
| 164 | NegotiationHeaderPublishDate | PUBLISH_DATE | — | ✅ |
| 165 | NegotiationHeaderPublishDateOrigAmend | PUBLISH_DATE_ORIG_AMEND | — | ✅ |
| 166 | NegotiationHeaderPublishRatesToBiddersFlag | PUBLISH_RATES_TO_BIDDERS_FLAG | — | ✅ |
| 167 | NegotiationHeaderQtyPriceTiersEnabledFlag | QTY_PRICE_TIERS_ENABLED_FLAG | — | ✅ |
| 168 | NegotiationHeaderRankIndicator | RANK_INDICATOR | — | ✅ |
| 169 | NegotiationHeaderRateDate | RATE_DATE | — | ✅ |
| 170 | NegotiationHeaderRateType | RATE_TYPE | — | ✅ |
| 171 | NegotiationHeaderRecoupmentNegotiableFlag | RECOUPMENT_NEGOTIABLE_FLAG | — | ✅ |
| 172 | NegotiationHeaderReminderDate | REMINDER_DATE | — | ✅ |
| 173 | NegotiationHeaderReqBuId | REQ_BU_ID | — | ✅ |
| 174 | NegotiationHeaderRequestDate | REQUEST_DATE | — | ✅ |
| 175 | NegotiationHeaderRequestId | REQUEST_ID | — | ✅ |
| 176 | NegotiationHeaderRequestedBy | REQUESTED_BY | — | ✅ |
| 177 | NegotiationHeaderRetainageNegotiableFlag | RETAINAGE_NEGOTIABLE_FLAG | — | ✅ |
| 178 | NegotiationHeaderRfiLineEnabledFlag | RFI_LINE_ENABLED_FLAG | — | ✅ |
| 179 | NegotiationHeaderScoringLockDate | SCORING_LOCK_DATE | — | ✅ |
| 180 | NegotiationHeaderSealedActualUnlockDate | SEALED_ACTUAL_UNLOCK_DATE | — | ✅ |
| 181 | NegotiationHeaderSealedActualUnsealDate | SEALED_ACTUAL_UNSEAL_DATE | — | ✅ |
| 182 | NegotiationHeaderSealedAuctionStatus | SEALED_AUCTION_STATUS | — | ✅ |
| 183 | NegotiationHeaderShareAwardDecision | SHARE_AWARD_DECISION | — | ✅ |
| 184 | NegotiationHeaderShowBidderNotes | SHOW_BIDDER_NOTES | — | ✅ |
| 185 | NegotiationHeaderShowBidderScores | SHOW_BIDDER_SCORES | — | ✅ |
| 186 | NegotiationHeaderSourceDocId | SOURCE_DOC_ID | — | ✅ |
| 187 | NegotiationHeaderSourceDocLineMsg | SOURCE_DOC_LINE_MSG | — | ✅ |
| 188 | NegotiationHeaderSourceDocMsg | SOURCE_DOC_MSG | — | ✅ |
| 189 | NegotiationHeaderSourceDocMsgApp | SOURCE_DOC_MSG_APP | — | ✅ |
| 190 | NegotiationHeaderSourceDocNumber | SOURCE_DOC_NUMBER | — | ✅ |
| 191 | NegotiationHeaderSourceReqsFlag | SOURCE_REQS_FLAG | — | ✅ |
| 192 | NegotiationHeaderStaggeredClosingInterval | STAGGERED_CLOSING_INTERVAL | — | ✅ |
| 193 | NegotiationHeaderStyleId | STYLE_ID | — | ✅ |
| 194 | NegotiationHeaderSupplierEnterablePymtFlag | SUPPLIER_ENTERABLE_PYMT_FLAG | — | ✅ |
| 195 | NegotiationHeaderSupplierViewType | SUPPLIER_VIEW_TYPE | — | ✅ |
| 196 | NegotiationHeaderTeamScoringEnabledFlag | TEAM_SCORING_ENABLED_FLAG | — | ✅ |
| 197 | NegotiationHeaderTechnicalActualUnlockDate | TECHNICAL_ACTUAL_UNLOCK_DATE | — | ✅ |
| 198 | NegotiationHeaderTechnicalActualUnsealDate | TECHNICAL_ACTUAL_UNSEAL_DATE | — | ✅ |
| 199 | NegotiationHeaderTechnicalEvaluationStatus | TECHNICAL_EVALUATION_STATUS | — | ✅ |
| 200 | NegotiationHeaderTechnicalLockStatus | TECHNICAL_LOCK_STATUS | — | ✅ |
| 201 | NegotiationHeaderTemplateId | TEMPLATE_ID | — | ✅ |
| 202 | NegotiationHeaderTemplateScope | TEMPLATE_SCOPE | — | ✅ |
| 203 | NegotiationHeaderTemplateStatus | TEMPLATE_STATUS | — | ✅ |
| 204 | NegotiationHeaderTwoPartFlag | TWO_PART_FLAG | — | ✅ |
| 205 | NegotiationHeaderVersionNum | VERSION_NUM | — | ✅ |
| 206 | NegotiationHeaderViewByDate | VIEW_BY_DATE | — | ✅ |
| 207 | NegotiationHeaderWfApprovalItemKey | WF_APPROVAL_ITEM_KEY | — | ✅ |
| 208 | NegotiationHeaderWfAwardApprovalItemKey | WF_AWARD_APPROVAL_ITEM_KEY | — | ✅ |
| 209 | NegotiationHeaderWfItemKey | WF_ITEM_KEY | — | ✅ |
| 210 | NegotiationHeaderWfPoncomplCurrentRound | WF_PONCOMPL_CURRENT_ROUND | — | ✅ |
| 211 | NegotiationHeaderWfPoncomplItemKey | WF_PONCOMPL_ITEM_KEY | — | ✅ |
| 212 | NegotiationHeaderWfRoleName | WF_ROLE_NAME | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
