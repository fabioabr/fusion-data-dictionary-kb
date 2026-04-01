---
id: DOC-OTHER-PVO-CustAccountSiteUse
doc_type: system-doc
title: "CustAccountSiteUse — PVO Cross-Module"
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
  - CustAccountSiteUse
  - custaccountsiteuse
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CustAccountSiteUse

## 📌 Visão Geral

View Object para extração BICC de dados de Cust Account Site Use. Acessa as tabelas: HZ_CUST_ACCOUNTS, HZ_CUST_ACCT_SITES_ALL, HZ_CUST_SITE_USES_ALL (+2).

**Caminho:** `FscmTopModelAM.PartiesAnalyticsAM.CustAccountSiteUse`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 112 | 5 | 3 | 28 | 25% |

---

## 🔗 Tabelas Relacionadas

- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 1 atributos
- [[hz_cust_acct_sites_all|HZ_CUST_ACCT_SITES_ALL]] — 15 atributos
- [[hz_cust_site_uses_all|HZ_CUST_SITE_USES_ALL]] — 29 atributos (1 PKs, 5 BICC)
- [[hz_locations|HZ_LOCATIONS]] — 45 atributos (1 PKs, 16 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 22 atributos (1 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[hz_cust_accounts|HZ_CUST_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustomerAccountPEOCustAccountId | CUST_ACCOUNT_ID | — | — |

### [[hz_cust_acct_sites_all|HZ_CUST_ACCT_SITES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccountSiteEndDate | END_DATE | — | — |
| 2 | AccountSitePartySiteId | PARTY_SITE_ID | — | — |
| 3 | AccountSiteSetId | SET_ID | — | — |
| 4 | AccountSiteStartDate | START_DATE | — | — |
| 5 | AccountSiteStatus | STATUS | — | — |
| 6 | BillToFlag | BILL_TO_FLAG | — | — |
| 7 | CustAccountSiteId | CUST_ACCT_SITE_ID | — | — |
| 8 | CustomerCategoryCode | CUSTOMER_CATEGORY_CODE | — | — |
| 9 | EceTpLocationCode | ECE_TP_LOCATION_CODE | — | — |
| 10 | KeyAccountFlag | KEY_ACCOUNT_FLAG | — | — |
| 11 | Language | ACCT_SITE_LANGUAGE | — | — |
| 12 | MarketFlag | MARKET_FLAG | — | — |
| 13 | ShipToFlag | SHIP_TO_FLAG | — | — |
| 14 | TpHeaderId | TP_HEADER_ID | — | — |
| 15 | TranslatedCustomerName | TRANSLATED_CUSTOMER_NAME | — | — |

### [[hz_cust_site_uses_all|HZ_CUST_SITE_USES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreationDate | CREATION_DATE | — | — |
| 2 | CustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 3 | EndDate | END_DATE | — | — |
| 4 | FinchrgReceivablesTrxId | FINCHRG_RECEIVABLES_TRX_ID | — | — |
| 5 | GsaIndicator | GSA_INDICATOR | — | — |
| 6 | LastAccrueChargeDate | LAST_ACCRUE_CHARGE_DATE | — | — |
| 7 | LastUnaccrueChargeDate | LAST_UNACCRUE_CHARGE_DATE | — | — |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | Location | LOCATION | — | ✅ |
| 12 | OrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 13 | PaymentTermId | PAYMENT_TERM_ID | — | — |
| 14 | PrimaryFlag | PRIMARY_FLAG | — | — |
| 15 | SecondLastAccrueChargeDate | SECOND_LAST_ACCRUE_CHARGE_DATE | — | — |
| 16 | SecondLastUnaccrueChrgDate | SECOND_LAST_UNACCRUE_CHRG_DATE | — | — |
| 17 | SetId | SET_ID | — | — |
| 18 | SicCode | SIC_CODE | — | — |
| 19 | SiteUseCode | SITE_USE_CODE | — | ✅ |
| 20 | SiteUseId | SITE_USE_ID | 🔑 | ✅ |
| 21 | SortPriority | SORT_PRIORITY | — | — |
| 22 | StartDate | START_DATE | — | — |
| 23 | Status | STATUS | — | ✅ |
| 24 | TaxClassification | TAX_CLASSIFICATION | — | — |
| 25 | TaxCode | TAX_CODE | — | — |
| 26 | TaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | — |
| 27 | TaxReference | TAX_REFERENCE | — | — |
| 28 | TaxRoundingRule | TAX_ROUNDING_RULE | — | — |
| 29 | TerritoryId | TERRITORY_ID | — | — |

### [[hz_locations|HZ_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddrElementAttribute1 | ADDR_ELEMENT_ATTRIBUTE1 | — | — |
| 2 | AddrElementAttribute2 | ADDR_ELEMENT_ATTRIBUTE2 | — | — |
| 3 | AddrElementAttribute3 | ADDR_ELEMENT_ATTRIBUTE3 | — | — |
| 4 | AddrElementAttribute4 | ADDR_ELEMENT_ATTRIBUTE4 | — | — |
| 5 | AddrElementAttribute5 | ADDR_ELEMENT_ATTRIBUTE5 | — | — |
| 6 | Address1 | ADDRESS1 | — | ✅ |
| 7 | Address2 | ADDRESS2 | — | ✅ |
| 8 | Address3 | ADDRESS3 | — | ✅ |
| 9 | Address4 | ADDRESS4 | — | ✅ |
| 10 | AddressEffectiveDate | ADDRESS_EFFECTIVE_DATE | — | — |
| 11 | AddressExpirationDate | ADDRESS_EXPIRATION_DATE | — | — |
| 12 | AddressLinesPhonetic | ADDRESS_LINES_PHONETIC | — | — |
| 13 | AddressStyle | ADDRESS_STYLE | — | — |
| 14 | Building | BUILDING | — | — |
| 15 | City | CITY | — | ✅ |
| 16 | ClliCode | CLLI_CODE | — | — |
| 17 | Country | COUNTRY | — | ✅ |
| 18 | County | COUNTY | — | ✅ |
| 19 | DateValidated | DATE_VALIDATED | — | — |
| 20 | Description | DESCRIPTION | — | ✅ |
| 21 | DoNotValidateFlag | DO_NOT_VALIDATE_FLAG | — | — |
| 22 | FaLocationId | FA_LOCATION_ID | — | — |
| 23 | FloorNumber | FLOOR_NUMBER | — | — |
| 24 | GeometryStatusCode | GEOMETRY_STATUS_CODE | — | — |
| 25 | HouseType | HOUSE_TYPE | — | — |
| 26 | InternalFlag | INTERNAL_FLAG | — | — |
| 27 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 28 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 29 | LocationComments | COMMENTS | — | — |
| 30 | LocationDirections | LOCATION_DIRECTIONS | — | — |
| 31 | LocationId | LOCATION_ID | 🔑 | ✅ |
| 32 | LocationLanguage | LOCATION_LANGUAGE | — | — |
| 33 | OrigSystemReference1 | ORIG_SYSTEM_REFERENCE | — | — |
| 34 | Position | POSITION | — | — |
| 35 | PostalCode | POSTAL_CODE | — | ✅ |
| 36 | PostalPlus4Code | POSTAL_PLUS4_CODE | — | — |
| 37 | Province | PROVINCE | — | ✅ |
| 38 | SalesTaxGeocode | SALES_TAX_GEOCODE | — | ✅ |
| 39 | SalesTaxInsideCityLimits | SALES_TAX_INSIDE_CITY_LIMITS | — | ✅ |
| 40 | ShortDescription | SHORT_DESCRIPTION | — | ✅ |
| 41 | State | STATE | — | ✅ |
| 42 | StatusFlag | STATUS_FLAG | — | — |
| 43 | TimezoneCode | TIMEZONE_CODE | — | ✅ |
| 44 | ValidatedFlag | VALIDATED_FLAG | — | — |
| 45 | ValidationStatusCode | VALIDATION_STATUS_CODE | — | — |

### [[hz_party_sites|HZ_PARTY_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | Addressee | ADDRESSEE | — | — |
| 3 | Comments | COMMENTS | — | — |
| 4 | DunsNumberC | DUNS_NUMBER_C | — | — |
| 5 | EndDateActive | END_DATE_ACTIVE | — | ✅ |
| 6 | GlobalLocationNumber | GLOBAL_LOCATION_NUMBER | — | ✅ |
| 7 | IdentifyingAddressFlag | IDENTIFYING_ADDRESS_FLAG | — | ✅ |
| 8 | Mailstop | MAILSTOP | — | — |
| 9 | PartyId | PARTY_ID | — | — |
| 10 | PartyNameDba | PARTY_NAME_DBA | — | — |
| 11 | PartyNameDivision | PARTY_NAME_DIVISION | — | — |
| 12 | PartyNameLegal | PARTY_NAME_LEGAL | — | — |
| 13 | PartySiteId | PARTY_SITE_ID | 🔑 | ✅ |
| 14 | PartySiteLanguage | PARTY_SITE_LANGUAGE | — | — |
| 15 | PartySiteLocationId | LOCATION_ID | — | — |
| 16 | PartySiteName | PARTY_SITE_NAME | — | ✅ |
| 17 | PartySiteNumber | PARTY_SITE_NUMBER | — | ✅ |
| 18 | PartySiteStatus | STATUS | — | — |
| 19 | PartySiteType | PARTY_SITE_TYPE | — | — |
| 20 | PartyUsageCode | PARTY_USAGE_CODE | — | — |
| 21 | RelationshipId | RELATIONSHIP_ID | — | — |
| 22 | StartDateActive | START_DATE_ACTIVE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
