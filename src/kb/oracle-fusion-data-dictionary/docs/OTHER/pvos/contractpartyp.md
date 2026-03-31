---
id: DOC-OTHER-PVO-ContractPartyP
doc_type: system-doc
title: "ContractPartyP — PVO Cross-Module"
system: Oracle Fusion Cloud ERP
module: Cross-Module
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - other
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ContractPartyP
  - contractpartyp
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContractPartyP

## 📌 Visão Geral

View Object para extração BICC de dados de Contract Party P. Acessa as tabelas: FUN_ALL_BUSINESS_UNITS_V, HZ_PARTIES, OKC_K_HEADERS_ALL_B (+1).

**Caminho:** `FscmTopModelAM.ContractsCoreAM.ContractPartyP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 226 | 4 | 6 | 114 | 50% |

---

## 🔗 Tabelas Relacionadas

- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 21 atributos (1 PKs, 4 BICC)
- [[hz_parties|HZ_PARTIES]] — 82 atributos (1 PKs, 82 BICC)
- [[okc_k_headers_all_b|OKC_K_HEADERS_ALL_B]] — 98 atributos (2 PKs, 3 BICC)
- [[okc_k_party_roles_vl|OKC_K_PARTY_ROLES_VL]] — 25 atributos (2 PKs, 25 BICC)

---

## ⚙️ Atributos

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitBusinessUnitId | BU_ID | 🔑 | ✅ |
| 2 | BusinessUnitCreatedBy | CREATED_BY | — | — |
| 3 | BusinessUnitCreationDate | CREATION_DATE | — | — |
| 4 | BusinessUnitDateFrom | DATE_FROM | — | — |
| 5 | BusinessUnitDateTo | DATE_TO | — | — |
| 6 | BusinessUnitDefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | — |
| 7 | BusinessUnitDefaultSetId | DEFAULT_SET_ID | — | — |
| 8 | BusinessUnitEnabledForHrFlag | ENABLED_FOR_HR_FLAG | — | — |
| 9 | BusinessUnitEnterpriseId | BUSINESS_GROUP_ID | — | — |
| 10 | BusinessUnitFinancialsBusinessUnitId | FIN_BUSINESS_UNIT_ID | — | — |
| 11 | BusinessUnitLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | BusinessUnitLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | BusinessUnitLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | BusinessUnitLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 15 | BusinessUnitLocationId | LOCATION_ID | — | — |
| 16 | BusinessUnitManagerId | MANAGER_ID | — | — |
| 17 | BusinessUnitPrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |
| 18 | BusinessUnitProfitCenterFlag | PROFIT_CENTER_FLAG | — | — |
| 19 | BusinessUnitStatus | STATUS | — | — |
| 20 | Name | BU_NAME | — | ✅ |
| 21 | ShortCode | SHORT_CODE | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyAddress1 | ADDRESS1 | — | ✅ |
| 2 | PartyAddress2 | ADDRESS2 | — | ✅ |
| 3 | PartyAddress3 | ADDRESS3 | — | ✅ |
| 4 | PartyAddress4 | ADDRESS4 | — | ✅ |
| 5 | PartyAnalysisFy | ANALYSIS_FY | — | ✅ |
| 6 | PartyCategoryCode | CATEGORY_CODE | — | ✅ |
| 7 | PartyCeoName | CEO_NAME | — | ✅ |
| 8 | PartyCertReasonCode | CERT_REASON_CODE | — | ✅ |
| 9 | PartyCertificationLevel | CERTIFICATION_LEVEL | — | ✅ |
| 10 | PartyCity | CITY | — | ✅ |
| 11 | PartyComments | COMMENTS | — | ✅ |
| 12 | PartyCountry | COUNTRY | — | ✅ |
| 13 | PartyCounty | COUNTY | — | ✅ |
| 14 | PartyCreatedBy | CREATED_BY | — | ✅ |
| 15 | PartyCreatedByModule | CREATED_BY_MODULE | — | ✅ |
| 16 | PartyCreationDate | CREATION_DATE | — | ✅ |
| 17 | PartyCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | ✅ |
| 18 | PartyDateOfBirth | DATE_OF_BIRTH | — | ✅ |
| 19 | PartyDunsNumberC | DUNS_NUMBER_C | — | ✅ |
| 20 | PartyEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 21 | PartyEmployeesTotal | EMPLOYEES_TOTAL | — | ✅ |
| 22 | PartyFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | ✅ |
| 23 | PartyGender | GENDER | — | ✅ |
| 24 | PartyGroupType | GROUP_TYPE | — | ✅ |
| 25 | PartyGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | ✅ |
| 26 | PartyHomeCountry | HOME_COUNTRY | — | ✅ |
| 27 | PartyHqBranchInd | HQ_BRANCH_IND | — | ✅ |
| 28 | PartyIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | ✅ |
| 29 | PartyIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | ✅ |
| 30 | PartyInternalFlag | INTERNAL_FLAG | — | ✅ |
| 31 | PartyJgzzFiscalCode | JGZZ_FISCAL_CODE | — | ✅ |
| 32 | PartyLanguageName | LANGUAGE_NAME | — | ✅ |
| 33 | PartyLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 34 | PartyLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 35 | PartyLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 36 | PartyMaritalStatus | MARITAL_STATUS | — | ✅ |
| 37 | PartyMissionStatement | MISSION_STATEMENT | — | ✅ |
| 38 | PartyNextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | ✅ |
| 39 | PartyObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 40 | PartyOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | ✅ |
| 41 | PartyPartyId | PARTY_ID | 🔑 | ✅ |
| 42 | PartyPartyName | PARTY_NAME | — | ✅ |
| 43 | PartyPartyNumber | PARTY_NUMBER | — | ✅ |
| 44 | PartyPartyType | PARTY_TYPE | — | ✅ |
| 45 | PartyPartyUniqueName | PARTY_UNIQUE_NAME | — | ✅ |
| 46 | PartyPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | ✅ |
| 47 | PartyPersonFirstName | PERSON_FIRST_NAME | — | ✅ |
| 48 | PartyPersonLastName | PERSON_LAST_NAME | — | ✅ |
| 49 | PartyPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | ✅ |
| 50 | PartyPersonMiddleName | PERSON_MIDDLE_NAME | — | ✅ |
| 51 | PartyPersonNameSuffix | PERSON_NAME_SUFFIX | — | ✅ |
| 52 | PartyPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | ✅ |
| 53 | PartyPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | ✅ |
| 54 | PartyPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | ✅ |
| 55 | PartyPersonTitle | PERSON_TITLE | — | ✅ |
| 56 | PartyPostalCode | POSTAL_CODE | — | ✅ |
| 57 | PartyPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | ✅ |
| 58 | PartyPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | ✅ |
| 59 | PartyPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | ✅ |
| 60 | PartyPreferredName | PREFERRED_NAME | — | ✅ |
| 61 | PartyPreferredNameId | PREFERRED_NAME_ID | — | ✅ |
| 62 | PartyPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | ✅ |
| 63 | PartyPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | ✅ |
| 64 | PartyPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | ✅ |
| 65 | PartyPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | ✅ |
| 66 | PartyPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | ✅ |
| 67 | PartyPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | ✅ |
| 68 | PartyPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | ✅ |
| 69 | PartyPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | ✅ |
| 70 | PartyPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | ✅ |
| 71 | PartyProvince | PROVINCE | — | ✅ |
| 72 | PartySalutation | SALUTATION | — | ✅ |
| 73 | PartySicCode | SIC_CODE | — | ✅ |
| 74 | PartySicCodeType | SIC_CODE_TYPE | — | ✅ |
| 75 | PartyState | STATE | — | ✅ |
| 76 | PartyStatus | STATUS | — | ✅ |
| 77 | PartyThirdPartyFlag | THIRD_PARTY_FLAG | — | ✅ |
| 78 | PartyTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | ✅ |
| 79 | PartyUrl | URL | — | ✅ |
| 80 | PartyUserGuid | USER_GUID | — | ✅ |
| 81 | PartyValidatedFlag | VALIDATED_FLAG | — | ✅ |
| 82 | PartyYearEstablished | YEAR_ESTABLISHED | — | ✅ |

### [[okc_k_headers_all_b|OKC_K_HEADERS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractHeaderAcctRuleId | ACCT_RULE_ID | — | — |
| 2 | ContractHeaderAgreedAmount | AGREED_AMOUNT | — | — |
| 3 | ContractHeaderAmendmentEffectiveDate | AMENDMENT_EFFECTIVE_DATE | — | — |
| 4 | ContractHeaderApTermsId | AP_TERMS_ID | — | — |
| 5 | ContractHeaderArInterfaceYn | AR_INTERFACE_YN | — | — |
| 6 | ContractHeaderAutoReleaseInvoice | AUTO_RELEASE_INVOICE | — | — |
| 7 | ContractHeaderBaseContractYn | BASE_CONTRACT_YN | — | — |
| 8 | ContractHeaderBillSequence | BILL_SEQUENCE | — | — |
| 9 | ContractHeaderBillToAcctId | BILL_TO_ACCT_ID | — | — |
| 10 | ContractHeaderBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 11 | ContractHeaderBilledAtSource | BILLED_AT_SOURCE | — | — |
| 12 | ContractHeaderBilltoLocationId | BILLTO_LOCATION_ID | — | — |
| 13 | ContractHeaderBuyOrSell | BUY_OR_SELL | — | — |
| 14 | ContractHeaderCancelledAmount | CANCELLED_AMOUNT | — | — |
| 15 | ContractHeaderCommitmentId | COMMITMENT_ID | — | — |
| 16 | ContractHeaderContractNumber | CONTRACT_NUMBER | — | — |
| 17 | ContractHeaderContractNumberModifier | CONTRACT_NUMBER_MODIFIER | — | — |
| 18 | ContractHeaderContractTypeId | CONTRACT_TYPE_ID | — | — |
| 19 | ContractHeaderContributionPercent | CONTRIBUTION_PERCENT | — | — |
| 20 | ContractHeaderCreatedBy | CREATED_BY | — | — |
| 21 | ContractHeaderCreationDate | CREATION_DATE | — | — |
| 22 | ContractHeaderCurrencyCode | CURRENCY_CODE | — | — |
| 23 | ContractHeaderCustPoNumber | CUST_PO_NUMBER | — | — |
| 24 | ContractHeaderCustPoNumberReqYn | CUST_PO_NUMBER_REQ_YN | — | — |
| 25 | ContractHeaderDateApproved | DATE_APPROVED | — | — |
| 26 | ContractHeaderDateNotified | DATE_NOTIFIED | — | — |
| 27 | ContractHeaderDateSigned | DATE_SIGNED | — | — |
| 28 | ContractHeaderDateTerminated | DATE_TERMINATED | — | — |
| 29 | ContractHeaderDatetimeCancelled | DATETIME_CANCELLED | — | — |
| 30 | ContractHeaderEndDate | END_DATE | — | — |
| 31 | ContractHeaderEstimatedAmount | ESTIMATED_AMOUNT | — | — |
| 32 | ContractHeaderExemptCertificateNumber | EXEMPT_CERTIFICATE_NUMBER | — | — |
| 33 | ContractHeaderExemptReasonCode | EXEMPT_REASON_CODE | — | — |
| 34 | ContractHeaderFob | FOB | — | — |
| 35 | ContractHeaderFreightTerms | FREIGHT_TERMS | — | — |
| 36 | ContractHeaderHoldBilling | HOLD_BILLING | — | — |
| 37 | ContractHeaderHoldReasonCode | HOLD_REASON_CODE | — | — |
| 38 | ContractHeaderHoldUntilDate | HOLD_UNTIL_DATE | — | — |
| 39 | ContractHeaderId | ID | 🔑 | ✅ |
| 40 | ContractHeaderInvConvRateDate | INV_CONV_RATE_DATE | — | — |
| 41 | ContractHeaderInvConvRateDateType | INV_CONV_RATE_DATE_TYPE | — | — |
| 42 | ContractHeaderInvConvRateType | INV_CONV_RATE_TYPE | — | — |
| 43 | ContractHeaderInvOrganizationId | INV_ORGANIZATION_ID | — | — |
| 44 | ContractHeaderInvPrepayTrxTypeId | INV_PREPAY_TRX_TYPE_ID | — | — |
| 45 | ContractHeaderInvPrintProfile | INV_PRINT_PROFILE | — | — |
| 46 | ContractHeaderInvRuleId | INV_RULE_ID | — | — |
| 47 | ContractHeaderInvTrxTypeId | INV_TRX_TYPE_ID | — | — |
| 48 | ContractHeaderLastRevRecogDate | LAST_REV_RECOG_DATE | — | — |
| 49 | ContractHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 50 | ContractHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 51 | ContractHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 52 | ContractHeaderLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 53 | ContractHeaderLineAutonumberEnabledFlag | LINE_AUTONUMBER_ENABLED_FLAG | — | — |
| 54 | ContractHeaderMajorVersion | MAJOR_VERSION | 🔑 | ✅ |
| 55 | ContractHeaderNetInvoiceFlag | NET_INVOICE_FLAG | — | — |
| 56 | ContractHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 57 | ContractHeaderOrderId | ORDER_ID | — | — |
| 58 | ContractHeaderOrderNumber | ORDER_NUMBER | — | — |
| 59 | ContractHeaderOrgId | ORG_ID | — | — |
| 60 | ContractHeaderOrigSystemId1 | ORIG_SYSTEM_ID1 | — | — |
| 61 | ContractHeaderOrigSystemReference1 | ORIG_SYSTEM_REFERENCE1 | — | — |
| 62 | ContractHeaderOrigSystemSourceCode | ORIG_SYSTEM_SOURCE_CODE | — | — |
| 63 | ContractHeaderOutputTaxClassificationCode | OUTPUT_TAX_CLASSIFICATION_CODE | — | — |
| 64 | ContractHeaderOverallRiskCode | OVERALL_RISK_CODE | — | — |
| 65 | ContractHeaderOwningOrgId | OWNING_ORG_ID | — | — |
| 66 | ContractHeaderPaymentInstructionType | PAYMENT_INSTRUCTION_TYPE | — | — |
| 67 | ContractHeaderPaymentTermId | PAYMENT_TERM_ID | — | — |
| 68 | ContractHeaderPaymentType | PAYMENT_TYPE | — | — |
| 69 | ContractHeaderPriceListId | PRICE_LIST_ID | — | — |
| 70 | ContractHeaderPrimaryEntPartyId | PRIMARY_ENT_PARTY_ID | — | — |
| 71 | ContractHeaderProgramAppName | PROGRAM_APP_NAME | — | — |
| 72 | ContractHeaderProgramName | PROGRAM_NAME | — | — |
| 73 | ContractHeaderQclId | QCL_ID | — | — |
| 74 | ContractHeaderRecvInvOrgId | RECV_INV_ORG_ID | — | — |
| 75 | ContractHeaderRequestId | REQUEST_ID | — | — |
| 76 | ContractHeaderRevConvRateType | REV_CONV_RATE_TYPE | — | — |
| 77 | ContractHeaderShipInvOrgId | SHIP_INV_ORG_ID | — | — |
| 78 | ContractHeaderShipToAcctId | SHIP_TO_ACCT_ID | — | — |
| 79 | ContractHeaderShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 80 | ContractHeaderShiptoLocationId | SHIPTO_LOCATION_ID | — | — |
| 81 | ContractHeaderSoldToAcctId | SOLD_TO_ACCT_ID | — | — |
| 82 | ContractHeaderSoldToSiteId | SOLD_TO_SITE_ID | — | — |
| 83 | ContractHeaderStartDate | START_DATE | — | — |
| 84 | ContractHeaderStateTransitionFlowName | STATE_TRANSITION_FLOW_NAME | — | — |
| 85 | ContractHeaderStateTransitionFlowState | STATE_TRANSITION_FLOW_STATE | — | — |
| 86 | ContractHeaderStsCode | STS_CODE | — | — |
| 87 | ContractHeaderSummaryTrxYn | SUMMARY_TRX_YN | — | — |
| 88 | ContractHeaderSupplierId | SUPPLIER_ID | — | — |
| 89 | ContractHeaderSupplierSiteId | SUPPLIER_SITE_ID | — | — |
| 90 | ContractHeaderTaskId | TASK_ID | — | — |
| 91 | ContractHeaderTaxAmount | TAX_AMOUNT | — | — |
| 92 | ContractHeaderTaxExemptionControl | TAX_EXEMPTION_CONTROL | — | — |
| 93 | ContractHeaderTemplateUsed | TEMPLATE_USED | — | — |
| 94 | ContractHeaderTemplateYn | TEMPLATE_YN | — | — |
| 95 | ContractHeaderTermCancelSource | TERM_CANCEL_SOURCE | — | — |
| 96 | ContractHeaderTrnCode | TRN_CODE | — | — |
| 97 | ContractHeaderUserStatusCode | USER_STATUS_CODE | — | — |
| 98 | ContractHeaderVersionType | VERSION_TYPE | — | — |

### [[okc_k_party_roles_vl|OKC_K_PARTY_ROLES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractPartyAlias | ALIAS | — | ✅ |
| 2 | ContractPartyChrId | CHR_ID | — | ✅ |
| 3 | ContractPartyCleId | CLE_ID | — | ✅ |
| 4 | ContractPartyCognomen | COGNOMEN | — | ✅ |
| 5 | ContractPartyCreatedBy | CREATED_BY | — | ✅ |
| 6 | ContractPartyCreationDate | CREATION_DATE | — | ✅ |
| 7 | ContractPartyDnzChrId | DNZ_CHR_ID | — | ✅ |
| 8 | ContractPartyId | ID | 🔑 | ✅ |
| 9 | ContractPartyJtotObject1Code | JTOT_OBJECT1_CODE | — | ✅ |
| 10 | ContractPartyLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | ContractPartyLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | ContractPartyLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | ContractPartyMajorVersion | MAJOR_VERSION | 🔑 | ✅ |
| 14 | ContractPartyObject1Id1 | OBJECT1_ID1 | — | ✅ |
| 15 | ContractPartyObject1Id2 | OBJECT1_ID2 | — | ✅ |
| 16 | ContractPartyObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | ContractPartyOrigSystemId1 | ORIG_SYSTEM_ID1 | — | ✅ |
| 18 | ContractPartyOrigSystemReference1 | ORIG_SYSTEM_REFERENCE1 | — | ✅ |
| 19 | ContractPartyOrigSystemSourceCode | ORIG_SYSTEM_SOURCE_CODE | — | ✅ |
| 20 | ContractPartyPrimaryYn | PRIMARY_YN | — | ✅ |
| 21 | ContractPartyRleCode | RLE_CODE | — | ✅ |
| 22 | ContractPartySignedBy | SIGNED_BY | — | ✅ |
| 23 | ContractPartySignedDate | SIGNED_DATE | — | ✅ |
| 24 | ContractPartySignerRole | SIGNER_ROLE | — | ✅ |
| 25 | ContractPartyVersionType | VERSION_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
