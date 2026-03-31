---
id: DOC-PO-PVO-SupplierContactsPVO
doc_type: system-doc
title: "SupplierContactsPVO — PVO Purchasing"
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
  - SupplierContactsPVO
  - suppliercontactspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierContactsPVO

## 📌 Visão Geral

Extrai os contatos dos fornecedores, incluindo nome, cargo, telefone, e-mail e site associado. Suporta gestão de relacionamento e comunicação eficiente com a base de fornecedores.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.SupplierContactsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 205 | 4 | 1 | 19 | 9% |

---

## 🔗 Tabelas Relacionadas

- [[hz_org_contacts|HZ_ORG_CONTACTS]] — 18 atributos (2 BICC)
- [[hz_parties|HZ_PARTIES]] — 75 atributos (8 BICC)
- [[poz_supplier_contacts|POZ_SUPPLIER_CONTACTS]] — 17 atributos (1 PKs, 5 BICC)
- [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]] — 95 atributos (4 BICC)

---

## ⚙️ Atributos

### [[hz_org_contacts|HZ_ORG_CONTACTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgComments | COMMENTS | — | — |
| 2 | OrgContactNumber | CONTACT_NUMBER | — | — |
| 3 | OrgCreatedByModule | CREATED_BY_MODULE | — | — |
| 4 | OrgDecisionMakerFlag | DECISION_MAKER_FLAG | — | — |
| 5 | OrgDepartment | DEPARTMENT | — | — |
| 6 | OrgDepartmentCode | DEPARTMENT_CODE | — | — |
| 7 | OrgJobTitle | JOB_TITLE | — | ✅ |
| 8 | OrgJobTitleCode | JOB_TITLE_CODE | — | — |
| 9 | OrgOrgContactId | ORG_CONTACT_ID | — | ✅ |
| 10 | OrgOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 11 | OrgPartyRelationshipId | PARTY_RELATIONSHIP_ID | — | — |
| 12 | OrgPartySiteId | PARTY_SITE_ID | — | — |
| 13 | OrgRank | RANK | — | — |
| 14 | OrgReferenceUseFlag | REFERENCE_USE_FLAG | — | — |
| 15 | OrgSalesAffinityCode | SALES_AFFINITY_CODE | — | — |
| 16 | OrgSalesAffinityComments | SALES_AFFINITY_COMMENTS | — | — |
| 17 | OrgSalesBuyingRoleCode | SALES_BUYING_ROLE_CODE | — | — |
| 18 | OrgSalesInfluenceLevelCode | SALES_INFLUENCE_LEVEL_CODE | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyAddress1 | ADDRESS1 | — | — |
| 2 | PartyAddress2 | ADDRESS2 | — | — |
| 3 | PartyAddress3 | ADDRESS3 | — | — |
| 4 | PartyAddress4 | ADDRESS4 | — | — |
| 5 | PartyAnalysisFy | ANALYSIS_FY | — | — |
| 6 | PartyCategoryCode | CATEGORY_CODE | — | — |
| 7 | PartyCeoName | CEO_NAME | — | — |
| 8 | PartyCertReasonCode | CERT_REASON_CODE | — | — |
| 9 | PartyCertificationLevel | CERTIFICATION_LEVEL | — | — |
| 10 | PartyCity | CITY | — | — |
| 11 | PartyComments | COMMENTS | — | — |
| 12 | PartyCountry | COUNTRY | — | — |
| 13 | PartyCounty | COUNTY | — | — |
| 14 | PartyCreatedByModule | CREATED_BY_MODULE | — | — |
| 15 | PartyCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 16 | PartyDateOfBirth | DATE_OF_BIRTH | — | — |
| 17 | PartyDunsNumberC | DUNS_NUMBER_C | — | — |
| 18 | PartyEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 19 | PartyEmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 20 | PartyFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 21 | PartyGender | GENDER | — | — |
| 22 | PartyGroupType | GROUP_TYPE | — | — |
| 23 | PartyGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | — |
| 24 | PartyHomeCountry | HOME_COUNTRY | — | — |
| 25 | PartyHqBranchInd | HQ_BRANCH_IND | — | — |
| 26 | PartyIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 27 | PartyIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | — |
| 28 | PartyInternalFlag | INTERNAL_FLAG | — | — |
| 29 | PartyJgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 30 | PartyLanguageName | LANGUAGE_NAME | — | — |
| 31 | PartyMaritalStatus | MARITAL_STATUS | — | — |
| 32 | PartyMissionStatement | MISSION_STATEMENT | — | — |
| 33 | PartyNextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 34 | PartyOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 35 | PartyPartyId | PARTY_ID | — | ✅ |
| 36 | PartyPartyName | PARTY_NAME | — | ✅ |
| 37 | PartyPartyNumber | PARTY_NUMBER | — | — |
| 38 | PartyPartyType | PARTY_TYPE | — | — |
| 39 | PartyPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 40 | PartyPersonFirstName | PERSON_FIRST_NAME | — | ✅ |
| 41 | PartyPersonLastName | PERSON_LAST_NAME | — | ✅ |
| 42 | PartyPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 43 | PartyPersonMiddleName | PERSON_MIDDLE_NAME | — | ✅ |
| 44 | PartyPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 45 | PartyPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 46 | PartyPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 47 | PartyPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 48 | PartyPersonTitle | PERSON_TITLE | — | ✅ |
| 49 | PartyPostalCode | POSTAL_CODE | — | — |
| 50 | PartyPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 51 | PartyPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 52 | PartyPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 53 | PartyPreferredName | PREFERRED_NAME | — | — |
| 54 | PartyPreferredNameId | PREFERRED_NAME_ID | — | — |
| 55 | PartyPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | — |
| 56 | PartyPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 57 | PartyPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 58 | PartyPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 59 | PartyPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 60 | PartyPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 61 | PartyPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | ✅ |
| 62 | PartyPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 63 | PartyPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 64 | PartyProvince | PROVINCE | — | — |
| 65 | PartySalutation | SALUTATION | — | — |
| 66 | PartySicCode | SIC_CODE | — | — |
| 67 | PartySicCodeType | SIC_CODE_TYPE | — | — |
| 68 | PartyState | STATE | — | — |
| 69 | PartyStatus | STATUS | — | — |
| 70 | PartyThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 71 | PartyTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 72 | PartyUrl | URL | — | — |
| 73 | PartyUserGuid | USER_GUID | — | — |
| 74 | PartyValidatedFlag | VALIDATED_FLAG | — | — |
| 75 | PartyYearEstablished | YEAR_ESTABLISHED | — | — |

### [[poz_supplier_contacts|POZ_SUPPLIER_CONTACTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupplierContactCreatedBy | CREATED_BY | — | ✅ |
| 2 | SupplierContactCreationDate | CREATION_DATE | — | ✅ |
| 3 | SupplierContactInactiveDate | INACTIVE_DATE | — | — |
| 4 | SupplierContactLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | SupplierContactLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | SupplierContactLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | SupplierContactObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | SupplierContactOrgContactId | ORG_CONTACT_ID | — | — |
| 9 | SupplierContactOrgPartySiteId | ORG_PARTY_SITE_ID | — | — |
| 10 | SupplierContactPartySiteId | PARTY_SITE_ID | — | — |
| 11 | SupplierContactPerPartyId | PER_PARTY_ID | — | — |
| 12 | SupplierContactProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 13 | SupplierContactProgramId | PROGRAM_ID | — | — |
| 14 | SupplierContactProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 15 | SupplierContactRelationshipId | RELATIONSHIP_ID | — | — |
| 16 | SupplierContactRequestId | REQUEST_ID | — | — |
| 17 | VendorContactId | VENDOR_CONTACT_ID | 🔑 | ✅ |

### [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SuppSiteAllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | — |
| 2 | SuppSiteAllowUnorderedReceiptsFlag | ALLOW_UNORDERED_RECEIPTS_FLAG | — | — |
| 3 | SuppSiteAlwaysTakeDiscFlag | ALWAYS_TAKE_DISC_FLAG | — | — |
| 4 | SuppSiteAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 5 | SuppSiteApTaxRoundingRule | AP_TAX_ROUNDING_RULE | — | — |
| 6 | SuppSiteAreaCode | AREA_CODE | — | — |
| 7 | SuppSiteAttentionArFlag | ATTENTION_AR_FLAG | — | — |
| 8 | SuppSiteAutoCalculateInterestFlag | AUTO_CALCULATE_INTEREST_FLAG | — | — |
| 9 | SuppSiteAutoTaxCalcFlag | AUTO_TAX_CALC_FLAG | — | — |
| 10 | SuppSiteAutoTaxCalcOverride | AUTO_TAX_CALC_OVERRIDE | — | — |
| 11 | SuppSiteCarrierId | CARRIER_ID | — | — |
| 12 | SuppSiteCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | — |
| 13 | SuppSiteCreateDebitMemoFlag | CREATE_DEBIT_MEMO_FLAG | — | — |
| 14 | SuppSiteCreatedBy | CREATED_BY | — | — |
| 15 | SuppSiteCreationDate | CREATION_DATE | — | — |
| 16 | SuppSiteCustomerNum | CUSTOMER_NUM | — | — |
| 17 | SuppSiteDaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | — |
| 18 | SuppSiteDaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | — |
| 19 | SuppSiteDefaultPaySiteId | DEFAULT_PAY_SITE_ID | — | — |
| 20 | SuppSiteEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 21 | SuppSiteEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 22 | SuppSiteEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 23 | SuppSiteEmailAddress | EMAIL_ADDRESS | — | — |
| 24 | SuppSiteEnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | — |
| 25 | SuppSiteExcludeFreightFromDiscount | EXCLUDE_FREIGHT_FROM_DISCOUNT | — | — |
| 26 | SuppSiteExcludeTaxFromDiscount | EXCLUDE_TAX_FROM_DISCOUNT | — | — |
| 27 | SuppSiteFax | FAX | — | — |
| 28 | SuppSiteFaxAreaCode | FAX_AREA_CODE | — | — |
| 29 | SuppSiteFaxCountryCode | FAX_COUNTRY_CODE | — | — |
| 30 | SuppSiteFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 31 | SuppSiteFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 32 | SuppSiteGaplessInvNumFlag | GAPLESS_INV_NUM_FLAG | — | — |
| 33 | SuppSiteHoldAllPaymentsFlag | HOLD_ALL_PAYMENTS_FLAG | — | — |
| 34 | SuppSiteHoldBy | HOLD_BY | — | — |
| 35 | SuppSiteHoldDate | HOLD_DATE | — | — |
| 36 | SuppSiteHoldFlag | HOLD_FLAG | — | — |
| 37 | SuppSiteHoldFuturePaymentsFlag | HOLD_FUTURE_PAYMENTS_FLAG | — | — |
| 38 | SuppSiteHoldReason | HOLD_REASON | — | — |
| 39 | SuppSiteHoldUnmatchedInvoicesFlag | HOLD_UNMATCHED_INVOICES_FLAG | — | — |
| 40 | SuppSiteInactiveDate | INACTIVE_DATE | — | — |
| 41 | SuppSiteInspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | — |
| 42 | SuppSiteInvoiceAmountLimit | INVOICE_AMOUNT_LIMIT | — | — |
| 43 | SuppSiteInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 44 | SuppSiteLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 45 | SuppSiteLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 46 | SuppSiteLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 47 | SuppSiteLocationId | LOCATION_ID | — | — |
| 48 | SuppSiteMatchOption | MATCH_OPTION | — | — |
| 49 | SuppSiteObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 50 | SuppSiteOffsetTaxFlag | OFFSET_TAX_FLAG | — | — |
| 51 | SuppSiteOffsetVatCode | OFFSET_VAT_CODE | — | — |
| 52 | SuppSitePartySiteId | PARTY_SITE_ID | — | — |
| 53 | SuppSitePayDateBasisLookupCode | PAY_DATE_BASIS_LOOKUP_CODE | — | — |
| 54 | SuppSitePayGroupLookupCode | PAY_GROUP_LOOKUP_CODE | — | — |
| 55 | SuppSitePayOnCode | PAY_ON_CODE | — | — |
| 56 | SuppSitePayOnReceiptSummaryCode | PAY_ON_RECEIPT_SUMMARY_CODE | — | — |
| 57 | SuppSitePaySiteFlag | PAY_SITE_FLAG | — | — |
| 58 | SuppSitePaymentCurrencyCode | PAYMENT_CURRENCY_CODE | — | — |
| 59 | SuppSitePaymentPriority | PAYMENT_PRIORITY | — | — |
| 60 | SuppSitePcardSiteFlag | PCARD_SITE_FLAG | — | — |
| 61 | SuppSitePhone | PHONE | — | — |
| 62 | SuppSitePhoneCountryCode | PHONE_COUNTRY_CODE | — | — |
| 63 | SuppSitePhoneExtension | PHONE_EXTENSION | — | — |
| 64 | SuppSitePrcBuId | PRC_BU_ID | — | — |
| 65 | SuppSitePrimaryPaySiteFlag | PRIMARY_PAY_SITE_FLAG | — | — |
| 66 | SuppSiteProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 67 | SuppSiteProgramId | PROGRAM_ID | — | — |
| 68 | SuppSiteProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 69 | SuppSitePurchasingHoldReason | PURCHASING_HOLD_REASON | — | — |
| 70 | SuppSitePurchasingSiteFlag | PURCHASING_SITE_FLAG | — | — |
| 71 | SuppSiteQtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | — |
| 72 | SuppSiteQtyRcvTolerance | QTY_RCV_TOLERANCE | — | — |
| 73 | SuppSiteReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | — |
| 74 | SuppSiteReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 75 | SuppSiteReceivingRoutingId | RECEIVING_ROUTING_ID | — | — |
| 76 | SuppSiteRequestId | REQUEST_ID | — | — |
| 77 | SuppSiteRetainageRate | RETAINAGE_RATE | — | — |
| 78 | SuppSiteRfqOnlySiteFlag | RFQ_ONLY_SITE_FLAG | — | — |
| 79 | SuppSiteSellingCompanyIdentifier | SELLING_COMPANY_IDENTIFIER | — | — |
| 80 | SuppSiteServicesToleranceId | SERVICES_TOLERANCE_ID | — | — |
| 81 | SuppSiteShippingControl | SHIPPING_CONTROL | — | — |
| 82 | SuppSiteShippingNetworkLocation | SHIPPING_NETWORK_LOCATION | — | — |
| 83 | SuppSiteSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | — |
| 84 | SuppSiteTaxCountryCode | TAX_COUNTRY_CODE | — | — |
| 85 | SuppSiteTaxReportingSiteFlag | TAX_REPORTING_SITE_FLAG | — | — |
| 86 | SuppSiteTermsDateBasis | TERMS_DATE_BASIS | — | — |
| 87 | SuppSiteTermsId | TERMS_ID | — | — |
| 88 | SuppSiteToleranceId | TOLERANCE_ID | — | — |
| 89 | SuppSiteVatCode | VAT_CODE | — | — |
| 90 | SuppSiteVatRegistrationNum | VAT_REGISTRATION_NUM | — | — |
| 91 | SuppSiteVendorId | VENDOR_ID | — | ✅ |
| 92 | SuppSiteVendorSiteCode | VENDOR_SITE_CODE | — | — |
| 93 | SuppSiteVendorSiteCodeAlt | VENDOR_SITE_CODE_ALT | — | — |
| 94 | SuppSiteVendorSiteId | VENDOR_SITE_ID | — | ✅ |
| 95 | SuppSiteVendorSiteSpkId | VENDOR_SITE_SPK_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
