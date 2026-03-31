---
id: DOC-PO-PVO-PurchasingAgreementBuAccessPVO
doc_type: system-doc
title: "PurchasingAgreementBuAccessPVO — PVO Purchasing"
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
  - PurchasingAgreementBuAccessPVO
  - purchasingagreementbuaccesspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PurchasingAgreementBuAccessPVO

## 📌 Visão Geral

Extrai os acessos de unidades de negócio a contratos de compra, determinando quais entidades podem referenciar cada acordo. Fundamental para governança de acordos corporativos compartilhados.

**Caminho:** `FscmTopModelAM.PrcPoPublicViewAM.PurchasingAgreementBuAccessPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 361 | 6 | 1 | 39 | 11% |

---

## 🔗 Tabelas Relacionadas

- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 41 atributos (18 BICC)
- [[hz_locations|HZ_LOCATIONS]] — 53 atributos (9 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 30 atributos (1 BICC)
- [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]] — 105 atributos (4 BICC)
- [[po_ga_org_assignments|PO_GA_ORG_ASSIGNMENTS]] — 16 atributos (1 PKs, 5 BICC)
- [[po_headers_all|PO_HEADERS_ALL]] — 116 atributos (2 BICC)

---

## ⚙️ Atributos

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgreementBuAccessBilltoBuBusinessUnitId | BU_ID | — | ✅ |
| 2 | AgreementBuAccessBilltoBuCreatedBy | CREATED_BY | — | ✅ |
| 3 | AgreementBuAccessBilltoBuCreationDate | CREATION_DATE | — | ✅ |
| 4 | AgreementBuAccessBilltoBuDateFrom | DATE_FROM | — | ✅ |
| 5 | AgreementBuAccessBilltoBuDateTo | DATE_TO | — | ✅ |
| 6 | AgreementBuAccessBilltoBuDefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | ✅ |
| 7 | AgreementBuAccessBilltoBuDefaultSetId | DEFAULT_SET_ID | — | — |
| 8 | AgreementBuAccessBilltoBuEnabledForHrFlag | ENABLED_FOR_HR_FLAG | — | — |
| 9 | AgreementBuAccessBilltoBuEnterpriseId | BUSINESS_GROUP_ID | — | — |
| 10 | AgreementBuAccessBilltoBuFinancialsBusinessUnitId | FIN_BUSINESS_UNIT_ID | — | — |
| 11 | AgreementBuAccessBilltoBuLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | AgreementBuAccessBilltoBuLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | AgreementBuAccessBilltoBuLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | AgreementBuAccessBilltoBuLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 15 | AgreementBuAccessBilltoBuLocationId | LOCATION_ID | — | — |
| 16 | AgreementBuAccessBilltoBuManagerId | MANAGER_ID | — | — |
| 17 | AgreementBuAccessBilltoBuName | BU_NAME | — | ✅ |
| 18 | AgreementBuAccessBilltoBuPrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |
| 19 | AgreementBuAccessBilltoBuProfitCenterFlag | PROFIT_CENTER_FLAG | — | — |
| 20 | AgreementBuAccessBilltoBuShortCode | SHORT_CODE | — | — |
| 21 | AgreementBuAccessBilltoBuStatus | STATUS | — | ✅ |
| 22 | AgreementBuAccessReqBuBusinessUnitId | BU_ID | — | ✅ |
| 23 | AgreementBuAccessReqBuCreatedBy | CREATED_BY | — | ✅ |
| 24 | AgreementBuAccessReqBuCreationDate | CREATION_DATE | — | ✅ |
| 25 | AgreementBuAccessReqBuDateFrom | DATE_FROM | — | ✅ |
| 26 | AgreementBuAccessReqBuDateTo | DATE_TO | — | ✅ |
| 27 | AgreementBuAccessReqBuDefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | ✅ |
| 28 | AgreementBuAccessReqBuDefaultSetId | DEFAULT_SET_ID | — | — |
| 29 | AgreementBuAccessReqBuEnabledForHrFlag | ENABLED_FOR_HR_FLAG | — | — |
| 30 | AgreementBuAccessReqBuEnterpriseId | BUSINESS_GROUP_ID | — | — |
| 31 | AgreementBuAccessReqBuFinancialsBusinessUnitId | FIN_BUSINESS_UNIT_ID | — | — |
| 32 | AgreementBuAccessReqBuLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 33 | AgreementBuAccessReqBuLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 34 | AgreementBuAccessReqBuLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 35 | AgreementBuAccessReqBuLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 36 | AgreementBuAccessReqBuLocationId | LOCATION_ID | — | — |
| 37 | AgreementBuAccessReqBuManagerId | MANAGER_ID | — | — |
| 38 | AgreementBuAccessReqBuName | BU_NAME | — | ✅ |
| 39 | AgreementBuAccessReqBuPrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |
| 40 | AgreementBuAccessReqBuShortCode | SHORT_CODE | — | — |
| 41 | AgreementBuAccessReqBuStatus | STATUS | — | ✅ |

### [[hz_locations|HZ_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BuAccessSiteLocationActualContentSource1 | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | BuAccessSiteLocationAddrElementAttribute1 | ADDR_ELEMENT_ATTRIBUTE1 | — | — |
| 3 | BuAccessSiteLocationAddrElementAttribute2 | ADDR_ELEMENT_ATTRIBUTE2 | — | — |
| 4 | BuAccessSiteLocationAddrElementAttribute3 | ADDR_ELEMENT_ATTRIBUTE3 | — | — |
| 5 | BuAccessSiteLocationAddrElementAttribute4 | ADDR_ELEMENT_ATTRIBUTE4 | — | — |
| 6 | BuAccessSiteLocationAddrElementAttribute5 | ADDR_ELEMENT_ATTRIBUTE5 | — | — |
| 7 | BuAccessSiteLocationAddress1 | ADDRESS1 | — | ✅ |
| 8 | BuAccessSiteLocationAddress2 | ADDRESS2 | — | ✅ |
| 9 | BuAccessSiteLocationAddress3 | ADDRESS3 | — | ✅ |
| 10 | BuAccessSiteLocationAddress4 | ADDRESS4 | — | ✅ |
| 11 | BuAccessSiteLocationAddressEffectiveDate | ADDRESS_EFFECTIVE_DATE | — | — |
| 12 | BuAccessSiteLocationAddressExpirationDate | ADDRESS_EXPIRATION_DATE | — | — |
| 13 | BuAccessSiteLocationAddressLinesPhonetic | ADDRESS_LINES_PHONETIC | — | — |
| 14 | BuAccessSiteLocationAddressStyle | ADDRESS_STYLE | — | — |
| 15 | BuAccessSiteLocationAttributeCategory1 | ATTRIBUTE_CATEGORY | — | — |
| 16 | BuAccessSiteLocationBuilding | BUILDING | — | — |
| 17 | BuAccessSiteLocationCity | CITY | — | ✅ |
| 18 | BuAccessSiteLocationClliCode | CLLI_CODE | — | — |
| 19 | BuAccessSiteLocationComments1 | COMMENTS | — | — |
| 20 | BuAccessSiteLocationCountry | COUNTRY | — | ✅ |
| 21 | BuAccessSiteLocationCounty | COUNTY | — | — |
| 22 | BuAccessSiteLocationCreatedBy1 | CREATED_BY | — | — |
| 23 | BuAccessSiteLocationCreatedByModule1 | CREATED_BY_MODULE | — | — |
| 24 | BuAccessSiteLocationCreationDate1 | CREATION_DATE | — | — |
| 25 | BuAccessSiteLocationDateValidated | DATE_VALIDATED | — | — |
| 26 | BuAccessSiteLocationDescription | DESCRIPTION | — | — |
| 27 | BuAccessSiteLocationDoNotValidateFlag | DO_NOT_VALIDATE_FLAG | — | — |
| 28 | BuAccessSiteLocationFaLocationId | FA_LOCATION_ID | — | — |
| 29 | BuAccessSiteLocationFloorNumber | FLOOR_NUMBER | — | — |
| 30 | BuAccessSiteLocationGeometryStatusCode | GEOMETRY_STATUS_CODE | — | — |
| 31 | BuAccessSiteLocationHouseType | HOUSE_TYPE | — | — |
| 32 | BuAccessSiteLocationInternalFlag | INTERNAL_FLAG | — | — |
| 33 | BuAccessSiteLocationJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 34 | BuAccessSiteLocationJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 35 | BuAccessSiteLocationLanguage1 | LOCATION_LANGUAGE | — | — |
| 36 | BuAccessSiteLocationLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 37 | BuAccessSiteLocationLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 38 | BuAccessSiteLocationLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 39 | BuAccessSiteLocationLocationDirections | LOCATION_DIRECTIONS | — | — |
| 40 | BuAccessSiteLocationLocationId1 | LOCATION_ID | — | — |
| 41 | BuAccessSiteLocationOrigSystemReference1 | ORIG_SYSTEM_REFERENCE | — | — |
| 42 | BuAccessSiteLocationPosition | POSITION | — | — |
| 43 | BuAccessSiteLocationPostalCode | POSTAL_CODE | — | ✅ |
| 44 | BuAccessSiteLocationPostalPlus4Code | POSTAL_PLUS4_CODE | — | — |
| 45 | BuAccessSiteLocationProvince | PROVINCE | — | — |
| 46 | BuAccessSiteLocationSalesTaxGeocode | SALES_TAX_GEOCODE | — | — |
| 47 | BuAccessSiteLocationSalesTaxInsideCityLimits | SALES_TAX_INSIDE_CITY_LIMITS | — | — |
| 48 | BuAccessSiteLocationShortDescription | SHORT_DESCRIPTION | — | — |
| 49 | BuAccessSiteLocationState | STATE | — | ✅ |
| 50 | BuAccessSiteLocationStatusFlag | STATUS_FLAG | — | — |
| 51 | BuAccessSiteLocationTimezoneCode | TIMEZONE_CODE | — | — |
| 52 | BuAccessSiteLocationValidatedFlag | VALIDATED_FLAG | — | — |
| 53 | BuAccessSiteLocationValidationStatusCode | VALIDATION_STATUS_CODE | — | — |

### [[hz_party_sites|HZ_PARTY_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BuAccessPartySiteActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | BuAccessPartySiteAddressee | ADDRESSEE | — | — |
| 3 | BuAccessPartySiteAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | BuAccessPartySiteComments | COMMENTS | — | — |
| 5 | BuAccessPartySiteCreatedBy | CREATED_BY | — | — |
| 6 | BuAccessPartySiteCreatedByModule | CREATED_BY_MODULE | — | — |
| 7 | BuAccessPartySiteCreationDate | CREATION_DATE | — | — |
| 8 | BuAccessPartySiteDunsNumberC | DUNS_NUMBER_C | — | — |
| 9 | BuAccessPartySiteEndDateActive | END_DATE_ACTIVE | — | — |
| 10 | BuAccessPartySiteGlobalLocationNumber | GLOBAL_LOCATION_NUMBER | — | — |
| 11 | BuAccessPartySiteIdentifyingAddressFlag | IDENTIFYING_ADDRESS_FLAG | — | — |
| 12 | BuAccessPartySiteLanguage | PARTY_SITE_LANGUAGE | — | — |
| 13 | BuAccessPartySiteLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | BuAccessPartySiteLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | BuAccessPartySiteLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | BuAccessPartySiteLocationId | LOCATION_ID | — | — |
| 17 | BuAccessPartySiteMailstop | MAILSTOP | — | — |
| 18 | BuAccessPartySiteOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 19 | BuAccessPartySitePartyId | PARTY_ID | — | — |
| 20 | BuAccessPartySitePartyNameDba | PARTY_NAME_DBA | — | — |
| 21 | BuAccessPartySitePartyNameDivision | PARTY_NAME_DIVISION | — | — |
| 22 | BuAccessPartySitePartyNameLegal | PARTY_NAME_LEGAL | — | — |
| 23 | BuAccessPartySitePartySiteId | PARTY_SITE_ID | — | — |
| 24 | BuAccessPartySitePartySiteName | PARTY_SITE_NAME | — | — |
| 25 | BuAccessPartySitePartySiteNumber | PARTY_SITE_NUMBER | — | — |
| 26 | BuAccessPartySitePartySiteType | PARTY_SITE_TYPE | — | — |
| 27 | BuAccessPartySitePartyUsageCode | PARTY_USAGE_CODE | — | — |
| 28 | BuAccessPartySiteRelationshipId | RELATIONSHIP_ID | — | — |
| 29 | BuAccessPartySiteStartDateActive | START_DATE_ACTIVE | — | — |
| 30 | BuAccessPartySiteStatus | STATUS | — | — |

### [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BuAccessPurchasingSiteAllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | — |
| 2 | BuAccessPurchasingSiteAllowUnorderedReceiptsFlag | ALLOW_UNORDERED_RECEIPTS_FLAG | — | — |
| 3 | BuAccessPurchasingSiteAlwaysTakeDiscFlag | ALWAYS_TAKE_DISC_FLAG | — | — |
| 4 | BuAccessPurchasingSiteAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 5 | BuAccessPurchasingSiteApTaxRoundingRule | AP_TAX_ROUNDING_RULE | — | — |
| 6 | BuAccessPurchasingSiteAreaCode | AREA_CODE | — | — |
| 7 | BuAccessPurchasingSiteAttentionArFlag | ATTENTION_AR_FLAG | — | — |
| 8 | BuAccessPurchasingSiteAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 9 | BuAccessPurchasingSiteAutoTaxCalcFlag | AUTO_TAX_CALC_FLAG | — | — |
| 10 | BuAccessPurchasingSiteAutoTaxCalcOverride | AUTO_TAX_CALC_OVERRIDE | — | — |
| 11 | BuAccessPurchasingSiteB2bSiteCode | B2B_SITE_CODE | — | — |
| 12 | BuAccessPurchasingSiteBankChargeBearer | BANK_CHARGE_BEARER | — | — |
| 13 | BuAccessPurchasingSiteCarrierId | CARRIER_ID | — | — |
| 14 | BuAccessPurchasingSiteCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | ✅ |
| 15 | BuAccessPurchasingSiteCreateDebitMemoFlag | CREATE_DEBIT_MEMO_FLAG | — | — |
| 16 | BuAccessPurchasingSiteCreatedBy | CREATED_BY | — | — |
| 17 | BuAccessPurchasingSiteCreationDate | CREATION_DATE | — | — |
| 18 | BuAccessPurchasingSiteCustomerNum | CUSTOMER_NUM | — | — |
| 19 | BuAccessPurchasingSiteDaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | — |
| 20 | BuAccessPurchasingSiteDaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | — |
| 21 | BuAccessPurchasingSiteDefaultPaySiteId | DEFAULT_PAY_SITE_ID | — | — |
| 22 | BuAccessPurchasingSiteEceTpLocationCode | ECE_TP_LOCATION_CODE | — | — |
| 23 | BuAccessPurchasingSiteEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 24 | BuAccessPurchasingSiteEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 25 | BuAccessPurchasingSiteEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 26 | BuAccessPurchasingSiteEmailAddress | EMAIL_ADDRESS | — | — |
| 27 | BuAccessPurchasingSiteEnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | — |
| 28 | BuAccessPurchasingSiteExcludeFreightFromDiscount | EXCLUDE_FREIGHT_FROM_DISCOUNT | — | — |
| 29 | BuAccessPurchasingSiteExcludeTaxFromDiscount | EXCLUDE_TAX_FROM_DISCOUNT | — | — |
| 30 | BuAccessPurchasingSiteFax | FAX | — | — |
| 31 | BuAccessPurchasingSiteFaxAreaCode | FAX_AREA_CODE | — | — |
| 32 | BuAccessPurchasingSiteFaxCountryCode | FAX_COUNTRY_CODE | — | — |
| 33 | BuAccessPurchasingSiteFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 34 | BuAccessPurchasingSiteFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 35 | BuAccessPurchasingSiteGaplessInvNumFlag | GAPLESS_INV_NUM_FLAG | — | — |
| 36 | BuAccessPurchasingSiteGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 37 | BuAccessPurchasingSiteHoldAllPaymentsFlag | HOLD_ALL_PAYMENTS_FLAG | — | — |
| 38 | BuAccessPurchasingSiteHoldBy | HOLD_BY | — | — |
| 39 | BuAccessPurchasingSiteHoldDate | HOLD_DATE | — | — |
| 40 | BuAccessPurchasingSiteHoldFlag | HOLD_FLAG | — | — |
| 41 | BuAccessPurchasingSiteHoldFuturePaymentsFlag | HOLD_FUTURE_PAYMENTS_FLAG | — | — |
| 42 | BuAccessPurchasingSiteHoldReason | HOLD_REASON | — | — |
| 43 | BuAccessPurchasingSiteHoldUnmatchedInvoicesFlag | HOLD_UNMATCHED_INVOICES_FLAG | — | — |
| 44 | BuAccessPurchasingSiteInactiveDate | INACTIVE_DATE | — | — |
| 45 | BuAccessPurchasingSiteInspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | — |
| 46 | BuAccessPurchasingSiteInvoiceAmountLimit | INVOICE_AMOUNT_LIMIT | — | — |
| 47 | BuAccessPurchasingSiteInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 48 | BuAccessPurchasingSiteJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 49 | BuAccessPurchasingSiteJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 50 | BuAccessPurchasingSiteLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 51 | BuAccessPurchasingSiteLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 52 | BuAccessPurchasingSiteLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 53 | BuAccessPurchasingSiteLocationId | LOCATION_ID | — | — |
| 54 | BuAccessPurchasingSiteMatchOption | MATCH_OPTION | — | — |
| 55 | BuAccessPurchasingSiteObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 56 | BuAccessPurchasingSiteOffsetTaxFlag | OFFSET_TAX_FLAG | — | — |
| 57 | BuAccessPurchasingSiteOffsetVatCode | OFFSET_VAT_CODE | — | — |
| 58 | BuAccessPurchasingSitePartySiteId | PARTY_SITE_ID | — | — |
| 59 | BuAccessPurchasingSitePayDateBasisLookupCode | PAY_DATE_BASIS_LOOKUP_CODE | — | — |
| 60 | BuAccessPurchasingSitePayGroupLookupCode | PAY_GROUP_LOOKUP_CODE | — | — |
| 61 | BuAccessPurchasingSitePayOnCode | PAY_ON_CODE | — | — |
| 62 | BuAccessPurchasingSitePayOnReceiptSummaryCode | PAY_ON_RECEIPT_SUMMARY_CODE | — | — |
| 63 | BuAccessPurchasingSitePaySiteFlag | PAY_SITE_FLAG | — | — |
| 64 | BuAccessPurchasingSitePaymentCurrencyCode | PAYMENT_CURRENCY_CODE | — | — |
| 65 | BuAccessPurchasingSitePaymentHoldDate | PAYMENT_HOLD_DATE | — | — |
| 66 | BuAccessPurchasingSitePaymentPriority | PAYMENT_PRIORITY | — | — |
| 67 | BuAccessPurchasingSitePcardSiteFlag | PCARD_SITE_FLAG | — | — |
| 68 | BuAccessPurchasingSitePhone | PHONE | — | — |
| 69 | BuAccessPurchasingSitePhoneCountryCode | PHONE_COUNTRY_CODE | — | — |
| 70 | BuAccessPurchasingSitePhoneExtension | PHONE_EXTENSION | — | — |
| 71 | BuAccessPurchasingSitePrcBuId | PRC_BU_ID | — | — |
| 72 | BuAccessPurchasingSitePrimaryPaySiteFlag | PRIMARY_PAY_SITE_FLAG | — | — |
| 73 | BuAccessPurchasingSiteProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 74 | BuAccessPurchasingSiteProgramId | PROGRAM_ID | — | — |
| 75 | BuAccessPurchasingSiteProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 76 | BuAccessPurchasingSitePurchasingHoldReason | PURCHASING_HOLD_REASON | — | — |
| 77 | BuAccessPurchasingSitePurchasingSiteFlag | PURCHASING_SITE_FLAG | — | — |
| 78 | BuAccessPurchasingSiteQtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | — |
| 79 | BuAccessPurchasingSiteQtyRcvTolerance | QTY_RCV_TOLERANCE | — | — |
| 80 | BuAccessPurchasingSiteReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | — |
| 81 | BuAccessPurchasingSiteReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 82 | BuAccessPurchasingSiteReceivingRoutingId | RECEIVING_ROUTING_ID | — | — |
| 83 | BuAccessPurchasingSiteRequestId | REQUEST_ID | — | — |
| 84 | BuAccessPurchasingSiteRetainageRate | RETAINAGE_RATE | — | — |
| 85 | BuAccessPurchasingSiteRfqOnlySiteFlag | RFQ_ONLY_SITE_FLAG | — | — |
| 86 | BuAccessPurchasingSiteSellingCompanyIdentifier | SELLING_COMPANY_IDENTIFIER | — | — |
| 87 | BuAccessPurchasingSiteServicesToleranceId | SERVICES_TOLERANCE_ID | — | — |
| 88 | BuAccessPurchasingSiteShipViaLookupCode | SHIP_VIA_LOOKUP_CODE | — | — |
| 89 | BuAccessPurchasingSiteShippingControl | SHIPPING_CONTROL | — | — |
| 90 | BuAccessPurchasingSiteShippingNetworkLocation | SHIPPING_NETWORK_LOCATION | — | — |
| 91 | BuAccessPurchasingSiteSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | — |
| 92 | BuAccessPurchasingSiteTaxCountryCode | TAX_COUNTRY_CODE | — | — |
| 93 | BuAccessPurchasingSiteTaxReportingSiteFlag | TAX_REPORTING_SITE_FLAG | — | — |
| 94 | BuAccessPurchasingSiteTelex | TELEX | — | — |
| 95 | BuAccessPurchasingSiteTermsDateBasis | TERMS_DATE_BASIS | — | — |
| 96 | BuAccessPurchasingSiteTermsId | TERMS_ID | — | — |
| 97 | BuAccessPurchasingSiteToleranceId | TOLERANCE_ID | — | — |
| 98 | BuAccessPurchasingSiteTpHeaderId | TP_HEADER_ID | — | — |
| 99 | BuAccessPurchasingSiteVatCode | VAT_CODE | — | — |
| 100 | BuAccessPurchasingSiteVatRegistrationNum | VAT_REGISTRATION_NUM | — | — |
| 101 | BuAccessPurchasingSiteVendorId | VENDOR_ID | — | — |
| 102 | BuAccessPurchasingSiteVendorSiteCode | VENDOR_SITE_CODE | — | ✅ |
| 103 | BuAccessPurchasingSiteVendorSiteCodeAlt | VENDOR_SITE_CODE_ALT | — | — |
| 104 | BuAccessPurchasingSiteVendorSiteId | VENDOR_SITE_ID | — | — |
| 105 | BuAccessPurchasingSiteVendorSiteSpkId | VENDOR_SITE_SPK_ID | — | — |

### [[po_ga_org_assignments|PO_GA_ORG_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillToLocationId | BILL_TO_LOCATION_ID | — | ✅ |
| 2 | BilltoBuId | BILLTO_BU_ID | — | — |
| 3 | CreatedBy | CREATED_BY | — | — |
| 4 | CreationDate | CREATION_DATE | — | — |
| 5 | EnabledFlag | ENABLED_FLAG | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | OrgAssignmentId | ORG_ASSIGNMENT_ID | 🔑 | ✅ |
| 11 | PoHeaderId | PO_HEADER_ID | — | — |
| 12 | PrcBuId | PRC_BU_ID | — | — |
| 13 | PurchasingAgreementBuAccessOrderedLocallyFlag | ORDERED_LOCALLY_FLAG | — | ✅ |
| 14 | ReqBuId | REQ_BU_ID | — | — |
| 15 | ShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 16 | VendorSiteId | VENDOR_SITE_ID | — | — |

### [[po_headers_all|PO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchasingDocumentHeaderAcceptanceDueDate | ACCEPTANCE_DUE_DATE | — | — |
| 2 | PurchasingDocumentHeaderAcceptanceRequiredFlag | ACCEPTANCE_REQUIRED_FLAG | — | — |
| 3 | PurchasingDocumentHeaderAcceptanceWithinDays | ACCEPTANCE_WITHIN_DAYS | — | — |
| 4 | PurchasingDocumentHeaderActiveVersionFlag | ACTIVE_VERSION_FLAG | — | — |
| 5 | PurchasingDocumentHeaderAgentId | AGENT_ID | — | — |
| 6 | PurchasingDocumentHeaderAmountLimit | AMOUNT_LIMIT | — | — |
| 7 | PurchasingDocumentHeaderAmountReleased | AMOUNT_RELEASED | — | — |
| 8 | PurchasingDocumentHeaderApprovedDate | APPROVED_DATE | — | — |
| 9 | PurchasingDocumentHeaderApprovedFlag | APPROVED_FLAG | — | — |
| 10 | PurchasingDocumentHeaderAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 11 | PurchasingDocumentHeaderAutoSourcingFlag | AUTO_SOURCING_FLAG | — | — |
| 12 | PurchasingDocumentHeaderBillToLocationId1 | BILL_TO_LOCATION_ID | — | — |
| 13 | PurchasingDocumentHeaderBlanketTotalAmount | BLANKET_TOTAL_AMOUNT | — | — |
| 14 | PurchasingDocumentHeaderCancelFlag | CANCEL_FLAG | — | — |
| 15 | PurchasingDocumentHeaderCarrierId | CARRIER_ID | — | — |
| 16 | PurchasingDocumentHeaderCatAdminAuthEnabledFlag | CAT_ADMIN_AUTH_ENABLED_FLAG | — | — |
| 17 | PurchasingDocumentHeaderCbcAccountingDate | CBC_ACCOUNTING_DATE | — | — |
| 18 | PurchasingDocumentHeaderChangeRequestedBy | CHANGE_REQUESTED_BY | — | — |
| 19 | PurchasingDocumentHeaderChangeSummary | CHANGE_SUMMARY | — | — |
| 20 | PurchasingDocumentHeaderClosedDate | CLOSED_DATE | — | — |
| 21 | PurchasingDocumentHeaderClosedDateTime | CLOSED_DATE | — | — |
| 22 | PurchasingDocumentHeaderComments | COMMENTS | — | — |
| 23 | PurchasingDocumentHeaderConfirmingOrderFlag | CONFIRMING_ORDER_FLAG | — | — |
| 24 | PurchasingDocumentHeaderConsignedConsumptionFlag | CONSIGNED_CONSUMPTION_FLAG | — | — |
| 25 | PurchasingDocumentHeaderConsumeReqDemandFlag | CONSUME_REQ_DEMAND_FLAG | — | — |
| 26 | PurchasingDocumentHeaderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 27 | PurchasingDocumentHeaderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 28 | PurchasingDocumentHeaderContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 29 | PurchasingDocumentHeaderCpaReference | CPA_REFERENCE | — | — |
| 30 | PurchasingDocumentHeaderCreatedBy1 | CREATED_BY | — | — |
| 31 | PurchasingDocumentHeaderCreatedLanguage | CREATED_LANGUAGE | — | — |
| 32 | PurchasingDocumentHeaderCreationDate1 | CREATION_DATE | — | — |
| 33 | PurchasingDocumentHeaderCurrencyCode | CURRENCY_CODE | — | — |
| 34 | PurchasingDocumentHeaderCurrentVersionId | CURRENT_VERSION_ID | — | — |
| 35 | PurchasingDocumentHeaderDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 36 | PurchasingDocumentHeaderDocumentCreationMethod | DOCUMENT_CREATION_METHOD | — | — |
| 37 | PurchasingDocumentHeaderDocumentStatus | DOCUMENT_STATUS | — | — |
| 38 | PurchasingDocumentHeaderEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 39 | PurchasingDocumentHeaderEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 40 | PurchasingDocumentHeaderEmailAddress | EMAIL_ADDRESS | — | — |
| 41 | PurchasingDocumentHeaderEnabledFlag | ENABLED_FLAG | — | — |
| 42 | PurchasingDocumentHeaderEncumbranceRequiredFlag | ENCUMBRANCE_REQUIRED_FLAG | — | — |
| 43 | PurchasingDocumentHeaderEndDate | END_DATE | — | — |
| 44 | PurchasingDocumentHeaderFax | FAX | — | — |
| 45 | PurchasingDocumentHeaderFirmDate | FIRM_DATE | — | — |
| 46 | PurchasingDocumentHeaderFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 47 | PurchasingDocumentHeaderFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 48 | PurchasingDocumentHeaderFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 49 | PurchasingDocumentHeaderFromHeaderId | FROM_HEADER_ID | — | — |
| 50 | PurchasingDocumentHeaderFromTypeLookupCode | FROM_TYPE_LOOKUP_CODE | — | — |
| 51 | PurchasingDocumentHeaderFrozenFlag | FROZEN_FLAG | — | — |
| 52 | PurchasingDocumentHeaderGenerateOrdersAutomatic | GENERATE_ORDERS_AUTOMATIC | — | — |
| 53 | PurchasingDocumentHeaderGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 54 | PurchasingDocumentHeaderGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 55 | PurchasingDocumentHeaderGroupRequisitionLines | GROUP_REQUISITION_LINES | — | — |
| 56 | PurchasingDocumentHeaderGroupRequisitions | GROUP_REQUISITIONS | — | — |
| 57 | PurchasingDocumentHeaderInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 58 | PurchasingDocumentHeaderJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 59 | PurchasingDocumentHeaderJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 60 | PurchasingDocumentHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 61 | PurchasingDocumentHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 62 | PurchasingDocumentHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 63 | PurchasingDocumentHeaderLastUpdatedProgram | LAST_UPDATED_PROGRAM | — | — |
| 64 | PurchasingDocumentHeaderMergeRequestId | MERGE_REQUEST_ID | — | — |
| 65 | PurchasingDocumentHeaderMinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 66 | PurchasingDocumentHeaderNoteToAuthorizer | NOTE_TO_AUTHORIZER | — | — |
| 67 | PurchasingDocumentHeaderNoteToReceiver | NOTE_TO_RECEIVER | — | — |
| 68 | PurchasingDocumentHeaderNoteToVendor | NOTE_TO_VENDOR | — | — |
| 69 | PurchasingDocumentHeaderObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 70 | PurchasingDocumentHeaderPayOnCode | PAY_ON_CODE | — | — |
| 71 | PurchasingDocumentHeaderPcardId | PCARD_ID | — | — |
| 72 | PurchasingDocumentHeaderPendingSignatureFlag | PENDING_SIGNATURE_FLAG | — | — |
| 73 | PurchasingDocumentHeaderPoHeaderId | PO_HEADER_ID | — | — |
| 74 | PurchasingDocumentHeaderPrcBuId | PRC_BU_ID | — | — |
| 75 | PurchasingDocumentHeaderPriceUpdateTolerance | PRICE_UPDATE_TOLERANCE | — | — |
| 76 | PurchasingDocumentHeaderProgramAppName | PROGRAM_APP_NAME | — | — |
| 77 | PurchasingDocumentHeaderProgramName | PROGRAM_NAME | — | — |
| 78 | PurchasingDocumentHeaderRate | RATE | — | — |
| 79 | PurchasingDocumentHeaderRateDate | RATE_DATE | — | — |
| 80 | PurchasingDocumentHeaderRateType | RATE_TYPE | — | — |
| 81 | PurchasingDocumentHeaderReferenceNum | REFERENCE_NUM | — | — |
| 82 | PurchasingDocumentHeaderReleaseMethod | RELEASE_METHOD | — | — |
| 83 | PurchasingDocumentHeaderReqBuId | REQ_BU_ID | — | — |
| 84 | PurchasingDocumentHeaderRequestId | REQUEST_ID | — | — |
| 85 | PurchasingDocumentHeaderRetroPriceApplyUpdatesFlag | RETRO_PRICE_APPLY_UPDATES_FLAG | — | — |
| 86 | PurchasingDocumentHeaderRetroPriceCommUpdatesFlag | RETRO_PRICE_COMM_UPDATES_FLAG | — | — |
| 87 | PurchasingDocumentHeaderReviewAutogeneratedReleases | REVIEW_AUTOGENERATED_RELEASES | — | — |
| 88 | PurchasingDocumentHeaderRevisedDate | REVISED_DATE | — | — |
| 89 | PurchasingDocumentHeaderRevisionNum | REVISION_NUM | — | — |
| 90 | PurchasingDocumentHeaderSegment1 | SEGMENT1 | — | — |
| 91 | PurchasingDocumentHeaderSegment2 | SEGMENT2 | — | — |
| 92 | PurchasingDocumentHeaderSegment3 | SEGMENT3 | — | — |
| 93 | PurchasingDocumentHeaderSegment4 | SEGMENT4 | — | — |
| 94 | PurchasingDocumentHeaderSegment5 | SEGMENT5 | — | — |
| 95 | PurchasingDocumentHeaderShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 96 | PurchasingDocumentHeaderShippingControl | SHIPPING_CONTROL | — | — |
| 97 | PurchasingDocumentHeaderStartDate | START_DATE | — | — |
| 98 | PurchasingDocumentHeaderStyleId | STYLE_ID | — | — |
| 99 | PurchasingDocumentHeaderSubmitApprovalAutomatic | SUBMIT_APPROVAL_AUTOMATIC | — | — |
| 100 | PurchasingDocumentHeaderSubmitDate | SUBMIT_DATE | — | — |
| 101 | PurchasingDocumentHeaderSummaryFlag | SUMMARY_FLAG | — | — |
| 102 | PurchasingDocumentHeaderSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | — |
| 103 | PurchasingDocumentHeaderTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 104 | PurchasingDocumentHeaderTaxDocumentSubtype | TAX_DOCUMENT_SUBTYPE | — | — |
| 105 | PurchasingDocumentHeaderTermsId | TERMS_ID | — | — |
| 106 | PurchasingDocumentHeaderTypeLookupCode | TYPE_LOOKUP_CODE | — | ✅ |
| 107 | PurchasingDocumentHeaderUpdateSourcingRulesFlag | UPDATE_SOURCING_RULES_FLAG | — | — |
| 108 | PurchasingDocumentHeaderUseNeedByDate | USE_NEED_BY_DATE | — | — |
| 109 | PurchasingDocumentHeaderUseShipTo | USE_SHIP_TO | — | — |
| 110 | PurchasingDocumentHeaderVendorContactId | VENDOR_CONTACT_ID | — | — |
| 111 | PurchasingDocumentHeaderVendorId | VENDOR_ID | — | — |
| 112 | PurchasingDocumentHeaderVendorOrderNum | VENDOR_ORDER_NUM | — | — |
| 113 | PurchasingDocumentHeaderVendorSiteId | VENDOR_SITE_ID | — | — |
| 114 | PurchasingDocumentHeaderXmlChangeSendDate | XML_CHANGE_SEND_DATE | — | — |
| 115 | PurchasingDocumentHeaderXmlFlag | XML_FLAG | — | — |
| 116 | PurchasingDocumentHeaderXmlSendDate | XML_SEND_DATE | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
