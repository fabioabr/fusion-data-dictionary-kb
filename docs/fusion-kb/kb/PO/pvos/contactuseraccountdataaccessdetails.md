---
id: DOC-PO-PVO-ContactUserAccountDataAccessDetails
doc_type: system-doc
title: "ContactUserAccountDataAccessDetails — PVO Purchasing"
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
  - ContactUserAccountDataAccessDetails
  - contactuseraccountdataaccessdetails
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContactUserAccountDataAccessDetails

## 📌 Visão Geral

Extrai detalhes de acesso de contas de usuários-contato de fornecedores, incluindo unidades de negócio e sites acessíveis. Essencial para auditoria de segurança e gestão de permissões no portal de fornecedores.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.ContactUserAccountDataAccessDetails`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 163 | 4 | 3 | 10 | 6% |

---

## 🔗 Tabelas Relacionadas

- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 20 atributos (2 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 30 atributos (1 BICC)
- [[poz_contact_act_data_access_v|POZ_CONTACT_ACT_DATA_ACCESS_V]] — 9 atributos (3 PKs, 5 BICC)
- [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]] — 104 atributos (2 BICC)

---

## ⚙️ Atributos

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrcBUBusinessUnitId | BU_ID | — | — |
| 2 | PrcBUCreatedBy | CREATED_BY | — | — |
| 3 | PrcBUCreationDate | CREATION_DATE | — | — |
| 4 | PrcBUDateFrom | DATE_FROM | — | — |
| 5 | PrcBUDateTo | DATE_TO | — | — |
| 6 | PrcBUDefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | — |
| 7 | PrcBUDefaultSetId | DEFAULT_SET_ID | — | — |
| 8 | PrcBUEnabledForHrFlag | ENABLED_FOR_HR_FLAG | — | — |
| 9 | PrcBUEnterpriseId | BUSINESS_GROUP_ID | — | — |
| 10 | PrcBUFinancialsBusinessUnitId | FIN_BUSINESS_UNIT_ID | — | — |
| 11 | PrcBULastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | PrcBULastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | PrcBULastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | PrcBULegalEntityId | LEGAL_ENTITY_ID | — | — |
| 15 | PrcBULocationId | LOCATION_ID | — | — |
| 16 | PrcBUManagerId | MANAGER_ID | — | — |
| 17 | PrcBUName | BU_NAME | — | ✅ |
| 18 | PrcBUPrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |
| 19 | PrcBUShortCode | SHORT_CODE | — | — |
| 20 | PrcBUStatus | STATUS | — | — |

### [[hz_party_sites|HZ_PARTY_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartySiteActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | PartySiteAddressee | ADDRESSEE | — | — |
| 3 | PartySiteComments | COMMENTS | — | — |
| 4 | PartySiteCreatedBy | CREATED_BY | — | — |
| 5 | PartySiteCreatedByModule | CREATED_BY_MODULE | — | — |
| 6 | PartySiteCreationDate | CREATION_DATE | — | — |
| 7 | PartySiteDunsNumberC | DUNS_NUMBER_C | — | — |
| 8 | PartySiteEndDateActive | END_DATE_ACTIVE | — | — |
| 9 | PartySiteGlobalLocationNumber | GLOBAL_LOCATION_NUMBER | — | — |
| 10 | PartySiteIdentifyingAddressFlag | IDENTIFYING_ADDRESS_FLAG | — | — |
| 11 | PartySiteLanguage | PARTY_SITE_LANGUAGE | — | — |
| 12 | PartySiteLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | PartySiteLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | PartySiteLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | PartySiteLocationId | LOCATION_ID | — | — |
| 16 | PartySiteMailstop | MAILSTOP | — | — |
| 17 | PartySiteObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | PartySiteOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 19 | PartySitePartyId | PARTY_ID | — | — |
| 20 | PartySitePartyNameDba | PARTY_NAME_DBA | — | — |
| 21 | PartySitePartyNameDivision | PARTY_NAME_DIVISION | — | — |
| 22 | PartySitePartyNameLegal | PARTY_NAME_LEGAL | — | — |
| 23 | PartySitePartySiteId | PARTY_SITE_ID | — | — |
| 24 | PartySitePartySiteName | PARTY_SITE_NAME | — | — |
| 25 | PartySitePartySiteNumber | PARTY_SITE_NUMBER | — | — |
| 26 | PartySitePartySiteType | PARTY_SITE_TYPE | — | — |
| 27 | PartySitePartyUsageCode | PARTY_USAGE_CODE | — | — |
| 28 | PartySiteRelationshipId | RELATIONSHIP_ID | — | — |
| 29 | PartySiteStartDateActive | START_DATE_ACTIVE | — | — |
| 30 | PartySiteStatus | STATUS | — | — |

### [[poz_contact_act_data_access_v|POZ_CONTACT_ACT_DATA_ACCESS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccessCode | ACCESS_CODE | 🔑 | ✅ |
| 2 | AccessValue | ACCESS_VALUE | 🔑 | ✅ |
| 3 | ContactUserAccountDataAccessAccessLevel | ACCESS_LEVEL | — | ✅ |
| 4 | ContactUserAccountDataAccessPartySiteName | PARTY_SITE_NAME | — | — |
| 5 | ContactUserAccountDataAccessPrcBuId | PRC_BU_ID | — | — |
| 6 | ContactUserAccountDataAccessVendorId | VENDOR_ID | — | — |
| 7 | ContactUserAccountDataAccessVendorSiteCode | VENDOR_SITE_CODE | — | ✅ |
| 8 | ContactUserAccountDataAccessVendorSiteId | VENDOR_SITE_ID | — | — |
| 9 | PerPartyId | PER_PARTY_ID | 🔑 | ✅ |

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
| 11 | SuppSiteB2bSiteCode | B2B_SITE_CODE | — | — |
| 12 | SuppSiteBankChargeBearer | BANK_CHARGE_BEARER | — | — |
| 13 | SuppSiteCarrierId | CARRIER_ID | — | — |
| 14 | SuppSiteCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | — |
| 15 | SuppSiteCreateDebitMemoFlag | CREATE_DEBIT_MEMO_FLAG | — | — |
| 16 | SuppSiteCreatedBy | CREATED_BY | — | — |
| 17 | SuppSiteCreationDate | CREATION_DATE | — | — |
| 18 | SuppSiteCustomerNum | CUSTOMER_NUM | — | — |
| 19 | SuppSiteDaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | — |
| 20 | SuppSiteDaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | — |
| 21 | SuppSiteDefaultPaySiteId | DEFAULT_PAY_SITE_ID | — | — |
| 22 | SuppSiteEceTpLocationCode | ECE_TP_LOCATION_CODE | — | — |
| 23 | SuppSiteEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 24 | SuppSiteEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 25 | SuppSiteEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 26 | SuppSiteEmailAddress | EMAIL_ADDRESS | — | — |
| 27 | SuppSiteEnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | — |
| 28 | SuppSiteExcludeFreightFromDiscount | EXCLUDE_FREIGHT_FROM_DISCOUNT | — | — |
| 29 | SuppSiteExcludeTaxFromDiscount | EXCLUDE_TAX_FROM_DISCOUNT | — | — |
| 30 | SuppSiteFax | FAX | — | — |
| 31 | SuppSiteFaxAreaCode | FAX_AREA_CODE | — | — |
| 32 | SuppSiteFaxCountryCode | FAX_COUNTRY_CODE | — | — |
| 33 | SuppSiteFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 34 | SuppSiteFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 35 | SuppSiteGaplessInvNumFlag | GAPLESS_INV_NUM_FLAG | — | — |
| 36 | SuppSiteHoldAllPaymentsFlag | HOLD_ALL_PAYMENTS_FLAG | — | — |
| 37 | SuppSiteHoldBy | HOLD_BY | — | — |
| 38 | SuppSiteHoldDate | HOLD_DATE | — | — |
| 39 | SuppSiteHoldFlag | HOLD_FLAG | — | — |
| 40 | SuppSiteHoldFuturePaymentsFlag | HOLD_FUTURE_PAYMENTS_FLAG | — | — |
| 41 | SuppSiteHoldReason | HOLD_REASON | — | — |
| 42 | SuppSiteHoldUnmatchedInvoicesFlag | HOLD_UNMATCHED_INVOICES_FLAG | — | — |
| 43 | SuppSiteInactiveDate | INACTIVE_DATE | — | — |
| 44 | SuppSiteInspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | — |
| 45 | SuppSiteInvoiceAmountLimit | INVOICE_AMOUNT_LIMIT | — | — |
| 46 | SuppSiteInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 47 | SuppSiteJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 48 | SuppSiteJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 49 | SuppSiteLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 50 | SuppSiteLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 51 | SuppSiteLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 52 | SuppSiteLocationId | LOCATION_ID | — | — |
| 53 | SuppSiteMatchOption | MATCH_OPTION | — | — |
| 54 | SuppSiteObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 55 | SuppSiteOffsetTaxFlag | OFFSET_TAX_FLAG | — | — |
| 56 | SuppSiteOffsetVatCode | OFFSET_VAT_CODE | — | — |
| 57 | SuppSitePartySiteId | PARTY_SITE_ID | — | — |
| 58 | SuppSitePayDateBasisLookupCode | PAY_DATE_BASIS_LOOKUP_CODE | — | — |
| 59 | SuppSitePayGroupLookupCode | PAY_GROUP_LOOKUP_CODE | — | — |
| 60 | SuppSitePayOnCode | PAY_ON_CODE | — | — |
| 61 | SuppSitePayOnReceiptSummaryCode | PAY_ON_RECEIPT_SUMMARY_CODE | — | — |
| 62 | SuppSitePaySiteFlag | PAY_SITE_FLAG | — | — |
| 63 | SuppSitePaymentCurrencyCode | PAYMENT_CURRENCY_CODE | — | — |
| 64 | SuppSitePaymentHoldDate | PAYMENT_HOLD_DATE | — | — |
| 65 | SuppSitePaymentPriority | PAYMENT_PRIORITY | — | — |
| 66 | SuppSitePcardSiteFlag | PCARD_SITE_FLAG | — | — |
| 67 | SuppSitePhone | PHONE | — | — |
| 68 | SuppSitePhoneCountryCode | PHONE_COUNTRY_CODE | — | — |
| 69 | SuppSitePhoneExtension | PHONE_EXTENSION | — | — |
| 70 | SuppSitePrcBuId | PRC_BU_ID | — | — |
| 71 | SuppSitePrimaryPaySiteFlag | PRIMARY_PAY_SITE_FLAG | — | — |
| 72 | SuppSiteProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 73 | SuppSiteProgramId | PROGRAM_ID | — | — |
| 74 | SuppSiteProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 75 | SuppSitePurchasingHoldReason | PURCHASING_HOLD_REASON | — | — |
| 76 | SuppSitePurchasingSiteFlag | PURCHASING_SITE_FLAG | — | — |
| 77 | SuppSiteQtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | — |
| 78 | SuppSiteQtyRcvTolerance | QTY_RCV_TOLERANCE | — | — |
| 79 | SuppSiteReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | — |
| 80 | SuppSiteReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 81 | SuppSiteReceivingRoutingId | RECEIVING_ROUTING_ID | — | — |
| 82 | SuppSiteRequestId | REQUEST_ID | — | — |
| 83 | SuppSiteRetainageRate | RETAINAGE_RATE | — | — |
| 84 | SuppSiteRfqOnlySiteFlag | RFQ_ONLY_SITE_FLAG | — | — |
| 85 | SuppSiteSellingCompanyIdentifier | SELLING_COMPANY_IDENTIFIER | — | — |
| 86 | SuppSiteServicesToleranceId | SERVICES_TOLERANCE_ID | — | — |
| 87 | SuppSiteShipViaLookupCode | SHIP_VIA_LOOKUP_CODE | — | — |
| 88 | SuppSiteShippingControl | SHIPPING_CONTROL | — | — |
| 89 | SuppSiteShippingNetworkLocation | SHIPPING_NETWORK_LOCATION | — | — |
| 90 | SuppSiteSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | — |
| 91 | SuppSiteTaxCountryCode | TAX_COUNTRY_CODE | — | — |
| 92 | SuppSiteTaxReportingSiteFlag | TAX_REPORTING_SITE_FLAG | — | — |
| 93 | SuppSiteTelex | TELEX | — | — |
| 94 | SuppSiteTermsDateBasis | TERMS_DATE_BASIS | — | — |
| 95 | SuppSiteTermsId | TERMS_ID | — | — |
| 96 | SuppSiteToleranceId | TOLERANCE_ID | — | — |
| 97 | SuppSiteTpHeaderId | TP_HEADER_ID | — | — |
| 98 | SuppSiteVatCode | VAT_CODE | — | — |
| 99 | SuppSiteVatRegistrationNum | VAT_REGISTRATION_NUM | — | — |
| 100 | SuppSiteVendorId | VENDOR_ID | — | — |
| 101 | SuppSiteVendorSiteCode | VENDOR_SITE_CODE | — | — |
| 102 | SuppSiteVendorSiteCodeAlt | VENDOR_SITE_CODE_ALT | — | — |
| 103 | SuppSiteVendorSiteId | VENDOR_SITE_ID | — | — |
| 104 | SuppSiteVendorSiteSpkId | VENDOR_SITE_SPK_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
