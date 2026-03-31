---
id: DOC-AR-PVO-SiteCreditCard
doc_type: system-doc
title: "SiteCreditCard — PVO Accounts Receivable"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ar
  - data-dictionary
  - pvo
  - bicc
aliases:
  - SiteCreditCard
  - sitecreditcard
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SiteCreditCard

## 📌 Visão Geral

Extrai os cartões de crédito registrados por site de cliente, com dados de cobrança e instrumentos de pagamento. Viabiliza cobranças automáticas diferenciadas por filial do cliente.

**Caminho:** `FscmTopModelAM.FinArCustomersPublicModelAM.SiteCreditCard`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 172 | 6 | 1 | 23 | 13% |

---

## 🔗 Tabelas Relacionadas

- [[hz_locations|HZ_LOCATIONS]] — 50 atributos (5 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 28 atributos (1 BICC)
- [[hz_party_site_uses|HZ_PARTY_SITE_USES]] — 15 atributos (1 BICC)
- [[iby_creditcard|IBY_CREDITCARD]] — 46 atributos (11 BICC)
- [[iby_external_payers_all|IBY_EXTERNAL_PAYERS_ALL]] — 18 atributos (1 BICC)
- [[iby_pmt_instr_uses_all|IBY_PMT_INSTR_USES_ALL]] — 15 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

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
| 8 | LocationAddressLinesPhonetic | ADDRESS_LINES_PHONETIC | — | — |
| 9 | LocationAddressStyle | ADDRESS_STYLE | — | — |
| 10 | LocationBuilding | BUILDING | — | — |
| 11 | LocationCity | CITY | — | — |
| 12 | LocationClliCode | CLLI_CODE | — | — |
| 13 | LocationComments | COMMENTS | — | — |
| 14 | LocationCountry | COUNTRY | — | — |
| 15 | LocationCounty | COUNTY | — | — |
| 16 | LocationCreatedBy | CREATED_BY | — | — |
| 17 | LocationCreatedByModule | CREATED_BY_MODULE | — | — |
| 18 | LocationCreationDate | CREATION_DATE | — | — |
| 19 | LocationDateValidated | DATE_VALIDATED | — | — |
| 20 | LocationDescription | DESCRIPTION | — | — |
| 21 | LocationDoNotValidateFlag | DO_NOT_VALIDATE_FLAG | — | — |
| 22 | LocationFaLocationId | FA_LOCATION_ID | — | — |
| 23 | LocationFloorNumber | FLOOR_NUMBER | — | — |
| 24 | LocationGeometryStatusCode | GEOMETRY_STATUS_CODE | — | — |
| 25 | LocationHouseType | HOUSE_TYPE | — | — |
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
| 38 | LocationOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 39 | LocationPosition | POSITION | — | — |
| 40 | LocationPostalCode | POSTAL_CODE | — | — |
| 41 | LocationPostalPlus4Code | POSTAL_PLUS4_CODE | — | — |
| 42 | LocationProvince | PROVINCE | — | — |
| 43 | LocationSalesTaxGeocode | SALES_TAX_GEOCODE | — | — |
| 44 | LocationSalesTaxInsideCityLimits | SALES_TAX_INSIDE_CITY_LIMITS | — | — |
| 45 | LocationShortDescription | SHORT_DESCRIPTION | — | — |
| 46 | LocationState | STATE | — | — |
| 47 | LocationStatusFlag | STATUS_FLAG | — | — |
| 48 | LocationTimezoneCode | TIMEZONE_CODE | — | — |
| 49 | LocationValidatedFlag | VALIDATED_FLAG | — | — |
| 50 | LocationValidationStatusCode | VALIDATION_STATUS_CODE | — | — |

### [[hz_party_sites|HZ_PARTY_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartySiteCreatedBy | CREATED_BY | — | — |
| 2 | PartySiteCreatedByModule | CREATED_BY_MODULE | — | — |
| 3 | PartySiteCreationDate | CREATION_DATE | — | — |
| 4 | PartySiteDunsNumberC | DUNS_NUMBER_C | — | — |
| 5 | PartySiteEndDateActive | END_DATE_ACTIVE | — | — |
| 6 | PartySiteGlobalLocationNumber | GLOBAL_LOCATION_NUMBER | — | — |
| 7 | PartySiteIdentifyingAddressFlag | IDENTIFYING_ADDRESS_FLAG | — | — |
| 8 | PartySiteLanguage | PARTY_SITE_LANGUAGE | — | — |
| 9 | PartySiteLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | PartySiteLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | PartySiteLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | PartySiteLocationId | LOCATION_ID | — | — |
| 13 | PartySiteMailstop | MAILSTOP | — | — |
| 14 | PartySiteObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | PartySiteOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 16 | PartySiteOverallPrimaryFlag | OVERALL_PRIMARY_FLAG | — | — |
| 17 | PartySitePartyId | PARTY_ID | — | — |
| 18 | PartySitePartyNameDba | PARTY_NAME_DBA | — | — |
| 19 | PartySitePartyNameDivision | PARTY_NAME_DIVISION | — | — |
| 20 | PartySitePartyNameLegal | PARTY_NAME_LEGAL | — | — |
| 21 | PartySitePartySiteId | PARTY_SITE_ID | — | — |
| 22 | PartySitePartySiteName | PARTY_SITE_NAME | — | — |
| 23 | PartySitePartySiteNumber | PARTY_SITE_NUMBER | — | — |
| 24 | PartySitePartySiteType | PARTY_SITE_TYPE | — | — |
| 25 | PartySitePartyUsageCode | PARTY_USAGE_CODE | — | — |
| 26 | PartySiteRelationshipId | RELATIONSHIP_ID | — | — |
| 27 | PartySiteStartDateActive | START_DATE_ACTIVE | — | — |
| 28 | PartySiteStatus | STATUS | — | — |

### [[hz_party_site_uses|HZ_PARTY_SITE_USES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartySiteUseBeginDate | BEGIN_DATE | — | — |
| 2 | PartySiteUseComments | COMMENTS | — | — |
| 3 | PartySiteUseCreatedBy | CREATED_BY | — | — |
| 4 | PartySiteUseCreatedByModule | CREATED_BY_MODULE | — | — |
| 5 | PartySiteUseCreationDate | CREATION_DATE | — | — |
| 6 | PartySiteUseEndDate | END_DATE | — | — |
| 7 | PartySiteUseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PartySiteUseLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | PartySiteUseLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | PartySiteUseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | PartySiteUsePartySiteId | PARTY_SITE_ID | — | — |
| 12 | PartySiteUsePartySiteUseId | PARTY_SITE_USE_ID | — | — |
| 13 | PartySiteUsePrimaryPerType | PRIMARY_PER_TYPE | — | — |
| 14 | PartySiteUseSiteUseType | SITE_USE_TYPE | — | — |
| 15 | PartySiteUseStatus | STATUS | — | — |

### [[iby_creditcard|IBY_CREDITCARD]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreditCardAccttypeid | ACCTTYPEID | — | — |
| 2 | CreditCardAddressid | ADDRESSID | — | — |
| 3 | CreditCardBillAddrTerritoryCode | BILL_ADDR_TERRITORY_CODE | — | — |
| 4 | CreditCardBillingAddrPostalCode | BILLING_ADDR_POSTAL_CODE | — | — |
| 5 | CreditCardCardIssuerCode | CARD_ISSUER_CODE | — | ✅ |
| 6 | CreditCardCardMaskSetting | CARD_MASK_SETTING | — | — |
| 7 | CreditCardCardOwnerId | CARD_OWNER_ID | — | — |
| 8 | CreditCardCardPurpose | CARD_PURPOSE | — | ✅ |
| 9 | CreditCardCardUnmaskLength | CARD_UNMASK_LENGTH | — | — |
| 10 | CreditCardCcIssuerRangeId | CC_ISSUER_RANGE_ID | — | — |
| 11 | CreditCardCcNumSecSegmentId | CC_NUM_SEC_SEGMENT_ID | — | — |
| 12 | CreditCardCcNumberHash1 | CC_NUMBER_HASH1 | — | — |
| 13 | CreditCardCcNumberHash2 | CC_NUMBER_HASH2 | — | — |
| 14 | CreditCardCcNumberLength | CC_NUMBER_LENGTH | — | — |
| 15 | CreditCardCcnumber | CCNUMBER | — | — |
| 16 | CreditCardChname | CHNAME | — | ✅ |
| 17 | CreditCardCreatedBy | CREATED_BY | — | — |
| 18 | CreditCardCreationDate | CREATION_DATE | — | — |
| 19 | CreditCardDescription | DESCRIPTION | — | ✅ |
| 20 | CreditCardEncrypted | ENCRYPTED | — | — |
| 21 | CreditCardEndDate | END_DATE | — | ✅ |
| 22 | CreditCardExpirySecSegmentId | EXPIRY_SEC_SEGMENT_ID | — | — |
| 23 | CreditCardExpirydate | EXPIRYDATE | — | ✅ |
| 24 | CreditCardFiname | FINAME | — | ✅ |
| 25 | CreditCardInformationOnlyFlag | INFORMATION_ONLY_FLAG | — | — |
| 26 | CreditCardInstrbuf | INSTRBUF | — | — |
| 27 | CreditCardInstrid | INSTRID | — | — |
| 28 | CreditCardInstrname | INSTRNAME | — | — |
| 29 | CreditCardInstrumentType | INSTRUMENT_TYPE | — | — |
| 30 | CreditCardLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 31 | CreditCardLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 32 | CreditCardLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 33 | CreditCardMaskedCcNumber | MASKED_CC_NUMBER | — | ✅ |
| 34 | CreditCardObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 35 | CreditCardProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 36 | CreditCardProgramId | PROGRAM_ID | — | — |
| 37 | CreditCardProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 38 | CreditCardPurchasecardFlag | PURCHASECARD_FLAG | — | ✅ |
| 39 | CreditCardPurchasecardSubtype | PURCHASECARD_SUBTYPE | — | — |
| 40 | CreditCardRequestId | REQUEST_ID | — | — |
| 41 | CreditCardSecSubkeyId | SEC_SUBKEY_ID | — | — |
| 42 | CreditCardSecurityGroupId | SECURITY_GROUP_ID | — | — |
| 43 | CreditCardSingleUseFlag | SINGLE_USE_FLAG | — | — |
| 44 | CreditCardStartDate | START_DATE | — | ✅ |
| 45 | CreditCardSubtype | SUBTYPE | — | — |
| 46 | CreditCardUpgradeAddressid | UPGRADE_ADDRESSID | — | — |

### [[iby_external_payers_all|IBY_EXTERNAL_PAYERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayersAcctSiteUseId | ACCT_SITE_USE_ID | — | — |
| 2 | PayersBankChargeBearerCode | BANK_CHARGE_BEARER_CODE | — | — |
| 3 | PayersCreatedBy | CREATED_BY | — | — |
| 4 | PayersCreationDate | CREATION_DATE | — | — |
| 5 | PayersCustAccountId | CUST_ACCOUNT_ID | — | — |
| 6 | PayersDebitAdviceDeliveryMethod | DEBIT_ADVICE_DELIVERY_METHOD | — | — |
| 7 | PayersDebitAdviceEmail | DEBIT_ADVICE_EMAIL | — | — |
| 8 | PayersDebitAdviceFax | DEBIT_ADVICE_FAX | — | — |
| 9 | PayersDirdebInstructionCode | DIRDEB_INSTRUCTION_CODE | — | — |
| 10 | PayersExtPayerId | EXT_PAYER_ID | — | — |
| 11 | PayersLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | PayersLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | PayersLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | PayersObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | PayersOrgId | ORG_ID | — | — |
| 16 | PayersOrgType | ORG_TYPE | — | — |
| 17 | PayersPartyId | PARTY_ID | — | — |
| 18 | PayersPaymentFunction | PAYMENT_FUNCTION | — | — |

### [[iby_pmt_instr_uses_all|IBY_PMT_INSTR_USES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InstrumentPaymentUseId | INSTRUMENT_PAYMENT_USE_ID | 🔑 | ✅ |
| 2 | UseCreatedBy | CREATED_BY | — | — |
| 3 | UseCreationDate | CREATION_DATE | — | — |
| 4 | UseEndDate | END_DATE | — | — |
| 5 | UseExtPmtPartyId | EXT_PMT_PARTY_ID | — | — |
| 6 | UseInstrumentId | INSTRUMENT_ID | — | — |
| 7 | UseInstrumentType | INSTRUMENT_TYPE | — | — |
| 8 | UseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | UseLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | UseLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | UseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | UsePaymentFlow | PAYMENT_FLOW | — | — |
| 13 | UsePaymentFunction | PAYMENT_FUNCTION | — | — |
| 14 | UsePrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 15 | UseStartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
