---
id: DOC-OTHER-PVO-CustAcctSiteUseLoc
doc_type: system-doc
title: "CustAcctSiteUseLoc — PVO Cross-Module"
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
  - CustAcctSiteUseLoc
  - custacctsiteuseloc
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CustAcctSiteUseLoc

## 📌 Visão Geral

View Object para extração BICC de dados de Cust Acct Site Use Loc. Acessa as tabelas: FND_SETID_SETS_VL, HZ_CUST_ACCOUNTS, HZ_CUST_ACCT_SITES_ALL (+3).

**Caminho:** `FscmTopModelAM.PartiesAnalyticsAM.CustAcctSiteUseLoc`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 171 | 6 | 1 | 83 | 49% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_setid_sets_vl|FND_SETID_SETS_VL]] — 3 atributos (2 BICC)
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 32 atributos (1 PKs, 13 BICC)
- [[hz_cust_acct_sites_all|HZ_CUST_ACCT_SITES_ALL]] — 23 atributos (13 BICC)
- [[hz_cust_site_uses_all|HZ_CUST_SITE_USES_ALL]] — 32 atributos (15 BICC)
- [[hz_locations|HZ_LOCATIONS]] — 50 atributos (24 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 31 atributos (16 BICC)

---

## ⚙️ Atributos

### [[fnd_setid_sets_vl|FND_SETID_SETS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustomerAccountSiteSetId | SET_NAME | — | ✅ |
| 2 | SetIdSetSetCode | SET_CODE | — | — |
| 3 | SetIdSetSetId | SET_ID | — | ✅ |

### [[hz_cust_accounts|HZ_CUST_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustAccountId | CUST_ACCOUNT_ID | 🔑 | ✅ |
| 2 | CustomerAccountAccountEstablishedDate | ACCOUNT_ESTABLISHED_DATE | — | ✅ |
| 3 | CustomerAccountAccountName | ACCOUNT_NAME | — | ✅ |
| 4 | CustomerAccountAccountNumber | ACCOUNT_NUMBER | — | ✅ |
| 5 | CustomerAccountAccountTerminationDate | ACCOUNT_TERMINATION_DATE | — | ✅ |
| 6 | CustomerAccountArrivalsetsIncludeLinesFlag | ARRIVALSETS_INCLUDE_LINES_FLAG | — | — |
| 7 | CustomerAccountAutopayFlag | AUTOPAY_FLAG | — | ✅ |
| 8 | CustomerAccountComments | COMMENTS | — | — |
| 9 | CustomerAccountCoterminateDayMonth | COTERMINATE_DAY_MONTH | — | — |
| 10 | CustomerAccountCreatedBy | CREATED_BY | — | — |
| 11 | CustomerAccountCreatedByModule | CREATED_BY_MODULE | — | — |
| 12 | CustomerAccountCreationDate | CREATION_DATE | — | — |
| 13 | CustomerAccountCustomerClassCode | CUSTOMER_CLASS_CODE | — | ✅ |
| 14 | CustomerAccountCustomerType | CUSTOMER_TYPE | — | ✅ |
| 15 | CustomerAccountDateTypePreference | DATE_TYPE_PREFERENCE | — | — |
| 16 | CustomerAccountDepositRefundMethod | DEPOSIT_REFUND_METHOD | — | — |
| 17 | CustomerAccountHeldBillExpirationDate | HELD_BILL_EXPIRATION_DATE | — | — |
| 18 | CustomerAccountHoldBillFlag | HOLD_BILL_FLAG | — | — |
| 19 | CustomerAccountLastBatchId | LAST_BATCH_ID | — | — |
| 20 | CustomerAccountLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | CustomerAccountLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 22 | CustomerAccountLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 23 | CustomerAccountNpaNumber | NPA_NUMBER | — | — |
| 24 | CustomerAccountOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | ✅ |
| 25 | CustomerAccountPartyId | PARTY_ID | — | ✅ |
| 26 | CustomerAccountSellingPartyId | SELLING_PARTY_ID | — | — |
| 27 | CustomerAccountSourceCode | SOURCE_CODE | — | — |
| 28 | CustomerAccountStatus | STATUS | — | ✅ |
| 29 | CustomerAccountStatusUpdateDate | STATUS_UPDATE_DATE | — | — |
| 30 | CustomerAccountTaxCode | TAX_CODE | — | ✅ |
| 31 | CustomerAccountTaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | — |
| 32 | CustomerAccountTaxRoundingRule | TAX_ROUNDING_RULE | — | — |

### [[hz_cust_acct_sites_all|HZ_CUST_ACCT_SITES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustomerAccountSiteBillToFlag | BILL_TO_FLAG | — | — |
| 2 | CustomerAccountSiteCreatedBy | CREATED_BY | — | ✅ |
| 3 | CustomerAccountSiteCreatedByModule | CREATED_BY_MODULE | — | — |
| 4 | CustomerAccountSiteCreationDate | CREATION_DATE | — | ✅ |
| 5 | CustomerAccountSiteCustAccountId | CUST_ACCOUNT_ID | — | — |
| 6 | CustomerAccountSiteCustAcctSiteId | CUST_ACCT_SITE_ID | — | ✅ |
| 7 | CustomerAccountSiteCustomerCategoryCode | CUSTOMER_CATEGORY_CODE | — | ✅ |
| 8 | CustomerAccountSiteEceTpLocationCode | ECE_TP_LOCATION_CODE | — | — |
| 9 | CustomerAccountSiteEndDate | END_DATE | — | ✅ |
| 10 | CustomerAccountSiteKeyAccountFlag | KEY_ACCOUNT_FLAG | — | — |
| 11 | CustomerAccountSiteLanguage | ACCT_SITE_LANGUAGE | — | ✅ |
| 12 | CustomerAccountSiteLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | CustomerAccountSiteLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | CustomerAccountSiteLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | CustomerAccountSiteMarketFlag | MARKET_FLAG | — | — |
| 16 | CustomerAccountSiteOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | ✅ |
| 17 | CustomerAccountSitePartySiteId | PARTY_SITE_ID | — | — |
| 18 | CustomerAccountSiteSetIdentifier | SET_ID | — | — |
| 19 | CustomerAccountSiteShipToFlag | SHIP_TO_FLAG | — | — |
| 20 | CustomerAccountSiteStartDate | START_DATE | — | ✅ |
| 21 | CustomerAccountSiteStatus | STATUS | — | ✅ |
| 22 | CustomerAccountSiteTpHeaderId | TP_HEADER_ID | — | — |
| 23 | CustomerAccountSiteTranslatedCustomerName | TRANSLATED_CUSTOMER_NAME | — | ✅ |

### [[hz_cust_site_uses_all|HZ_CUST_SITE_USES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustomerAccountSiteUseBillToSiteUseId | BILL_TO_SITE_USE_ID | — | ✅ |
| 2 | CustomerAccountSiteUseCreatedBy | CREATED_BY | — | ✅ |
| 3 | CustomerAccountSiteUseCreatedByModule | CREATED_BY_MODULE | — | ✅ |
| 4 | CustomerAccountSiteUseCreationDate | CREATION_DATE | — | ✅ |
| 5 | CustomerAccountSiteUseCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 6 | CustomerAccountSiteUseEndDate | END_DATE | — | ✅ |
| 7 | CustomerAccountSiteUseFinchrgReceivablesTrxId | FINCHRG_RECEIVABLES_TRX_ID | — | — |
| 8 | CustomerAccountSiteUseGsaIndicator | GSA_INDICATOR | — | — |
| 9 | CustomerAccountSiteUseLastAccrueChargeDate | LAST_ACCRUE_CHARGE_DATE | — | — |
| 10 | CustomerAccountSiteUseLastUnaccrueChargeDate | LAST_UNACCRUE_CHARGE_DATE | — | — |
| 11 | CustomerAccountSiteUseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | CustomerAccountSiteUseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | CustomerAccountSiteUseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | CustomerAccountSiteUseLocation | LOCATION | — | ✅ |
| 15 | CustomerAccountSiteUseOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | ✅ |
| 16 | CustomerAccountSiteUsePaymentTermId | PAYMENT_TERM_ID | — | — |
| 17 | CustomerAccountSiteUsePrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 18 | CustomerAccountSiteUseSecondLastAccrueChargeDate | SECOND_LAST_ACCRUE_CHARGE_DATE | — | — |
| 19 | CustomerAccountSiteUseSecondLastUnaccrueChrgDate | SECOND_LAST_UNACCRUE_CHRG_DATE | — | — |
| 20 | CustomerAccountSiteUseSetId | SET_ID | — | — |
| 21 | CustomerAccountSiteUseSicCode | SIC_CODE | — | — |
| 22 | CustomerAccountSiteUseSiteUseCode | SITE_USE_CODE | — | ✅ |
| 23 | CustomerAccountSiteUseSiteUseId | SITE_USE_ID | — | ✅ |
| 24 | CustomerAccountSiteUseSortPriority | SORT_PRIORITY | — | — |
| 25 | CustomerAccountSiteUseStartDate | START_DATE | — | ✅ |
| 26 | CustomerAccountSiteUseStatus | STATUS | — | ✅ |
| 27 | CustomerAccountSiteUseTaxClassification | TAX_CLASSIFICATION | — | — |
| 28 | CustomerAccountSiteUseTaxCode | TAX_CODE | — | — |
| 29 | CustomerAccountSiteUseTaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | — |
| 30 | CustomerAccountSiteUseTaxReference | TAX_REFERENCE | — | — |
| 31 | CustomerAccountSiteUseTaxRoundingRule | TAX_ROUNDING_RULE | — | — |
| 32 | CustomerAccountSiteUseTerritoryId | TERRITORY_ID | — | — |

### [[hz_locations|HZ_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocationActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | LocationAddress1 | ADDRESS1 | — | ✅ |
| 3 | LocationAddress2 | ADDRESS2 | — | ✅ |
| 4 | LocationAddress3 | ADDRESS3 | — | ✅ |
| 5 | LocationAddress4 | ADDRESS4 | — | ✅ |
| 6 | LocationAddressEffectiveDate | ADDRESS_EFFECTIVE_DATE | — | — |
| 7 | LocationAddressExpirationDate | ADDRESS_EXPIRATION_DATE | — | — |
| 8 | LocationAddressLinesPhonetic | ADDRESS_LINES_PHONETIC | — | ✅ |
| 9 | LocationAddressStyle | ADDRESS_STYLE | — | — |
| 10 | LocationBuilding | BUILDING | — | ✅ |
| 11 | LocationCity | CITY | — | ✅ |
| 12 | LocationClliCode | CLLI_CODE | — | — |
| 13 | LocationComments | COMMENTS | — | — |
| 14 | LocationCountry | COUNTRY | — | ✅ |
| 15 | LocationCounty | COUNTY | — | ✅ |
| 16 | LocationCreatedBy | CREATED_BY | — | ✅ |
| 17 | LocationCreatedByModule | CREATED_BY_MODULE | — | ✅ |
| 18 | LocationCreationDate | CREATION_DATE | — | ✅ |
| 19 | LocationDateValidated | DATE_VALIDATED | — | — |
| 20 | LocationDescription | DESCRIPTION | — | ✅ |
| 21 | LocationDoNotValidateFlag | DO_NOT_VALIDATE_FLAG | — | — |
| 22 | LocationFaLocationId | FA_LOCATION_ID | — | — |
| 23 | LocationFloorNumber | FLOOR_NUMBER | — | ✅ |
| 24 | LocationGeometryStatusCode | GEOMETRY_STATUS_CODE | — | — |
| 25 | LocationHouseType | HOUSE_TYPE | — | ✅ |
| 26 | LocationInternalFlag | INTERNAL_FLAG | — | — |
| 27 | LocationJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 28 | LocationJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 29 | LocationLanguage | LOCATION_LANGUAGE | — | — |
| 30 | LocationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 31 | LocationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 32 | LocationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 33 | LocationLatitude | LATITUDE | — | — |
| 34 | LocationLocationDirections | LOCATION_DIRECTIONS | — | — |
| 35 | LocationLocationId | LOCATION_ID | — | — |
| 36 | LocationLongitude | LONGITUDE | — | — |
| 37 | LocationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 38 | LocationOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | ✅ |
| 39 | LocationPosition | POSITION | — | — |
| 40 | LocationPostalCode | POSTAL_CODE | — | ✅ |
| 41 | LocationPostalPlus4Code | POSTAL_PLUS4_CODE | — | — |
| 42 | LocationProvince | PROVINCE | — | ✅ |
| 43 | LocationSalesTaxGeocode | SALES_TAX_GEOCODE | — | ✅ |
| 44 | LocationSalesTaxInsideCityLimits | SALES_TAX_INSIDE_CITY_LIMITS | — | ✅ |
| 45 | LocationShortDescription | SHORT_DESCRIPTION | — | ✅ |
| 46 | LocationState | STATE | — | ✅ |
| 47 | LocationStatusFlag | STATUS_FLAG | — | — |
| 48 | LocationTimezoneCode | TIMEZONE_CODE | — | ✅ |
| 49 | LocationValidatedFlag | VALIDATED_FLAG | — | — |
| 50 | LocationValidationStatusCode | VALIDATION_STATUS_CODE | — | — |

### [[hz_party_sites|HZ_PARTY_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartySiteActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | PartySiteAddressee | ADDRESSEE | — | — |
| 3 | PartySiteComments | COMMENTS | — | — |
| 4 | PartySiteCreatedBy | CREATED_BY | — | ✅ |
| 5 | PartySiteCreatedByModule | CREATED_BY_MODULE | — | ✅ |
| 6 | PartySiteCreationDate | CREATION_DATE | — | ✅ |
| 7 | PartySiteDunsNumberC | DUNS_NUMBER_C | — | — |
| 8 | PartySiteEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 9 | PartySiteGlobalLocationNumber | GLOBAL_LOCATION_NUMBER | — | ✅ |
| 10 | PartySiteIdentifyingAddressFlag | IDENTIFYING_ADDRESS_FLAG | — | ✅ |
| 11 | PartySiteLanguage | PARTY_SITE_LANGUAGE | — | — |
| 12 | PartySiteLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | PartySiteLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | PartySiteLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | PartySiteLocationId | LOCATION_ID | — | — |
| 16 | PartySiteMailstop | MAILSTOP | — | ✅ |
| 17 | PartySiteObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | PartySiteOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | ✅ |
| 19 | PartySiteOverallPrimaryFlag | OVERALL_PRIMARY_FLAG | — | — |
| 20 | PartySitePartyId | PARTY_ID | — | — |
| 21 | PartySitePartyNameDba | PARTY_NAME_DBA | — | — |
| 22 | PartySitePartyNameDivision | PARTY_NAME_DIVISION | — | — |
| 23 | PartySitePartyNameLegal | PARTY_NAME_LEGAL | — | — |
| 24 | PartySitePartySiteId | PARTY_SITE_ID | — | — |
| 25 | PartySitePartySiteName | PARTY_SITE_NAME | — | ✅ |
| 26 | PartySitePartySiteNumber | PARTY_SITE_NUMBER | — | ✅ |
| 27 | PartySitePartySiteType | PARTY_SITE_TYPE | — | — |
| 28 | PartySitePartyUsageCode | PARTY_USAGE_CODE | — | — |
| 29 | PartySiteRelationshipId | RELATIONSHIP_ID | — | ✅ |
| 30 | PartySiteStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 31 | PartySiteStatus | STATUS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
