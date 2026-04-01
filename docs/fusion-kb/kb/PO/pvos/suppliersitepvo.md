---
id: DOC-PO-PVO-SupplierSitePVO
doc_type: system-doc
title: "SupplierSitePVO — PVO Purchasing"
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
  - SupplierSitePVO
  - suppliersitepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierSitePVO

## 📌 Visão Geral

Disponibiliza os sites de fornecedores para consulta operacional, incluindo condições de pagamento, tolerâncias, moeda e status. Suporta a seleção do site correto ao emitir ordens de compra.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.SupplierSitePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 398 | 10 | 1 | 228 | 57% |

---

## 🔗 Tabelas Relacionadas

- [[ap_tolerance_templates|AP_TOLERANCE_TEMPLATES]] — 20 atributos (13 BICC)
- [[fnd_territories_vl|FND_TERRITORIES_VL]] — 20 atributos (1 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 20 atributos (3 BICC)
- [[hz_locations|HZ_LOCATIONS]] — 47 atributos (10 BICC)
- [[hz_parties|HZ_PARTIES]] — 2 atributos (1 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 24 atributos (2 BICC)
- [[poz_bi_sup_sites_ap_inv_dist_v|POZ_BI_SUP_SITES_AP_INV_DIST_V]] — 2 atributos (1 BICC)
- [[poz_suppliers|POZ_SUPPLIERS]] — 47 atributos (6 BICC)
- [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]] — 214 atributos (1 PKs, 191 BICC)
- [[poz_supplier_sites_pii|POZ_SUPPLIER_SITES_PII]] — 2 atributos

---

## ⚙️ Atributos

### [[ap_tolerance_templates|AP_TOLERANCE_TEMPLATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApAmtToleranceToleranceId | TOLERANCE_ID | — | — |
| 2 | ApAmtToleranceToleranceName | TOLERANCE_NAME | — | ✅ |
| 3 | ApToleranceCreatedBy | CREATED_BY | — | — |
| 4 | ApToleranceCreationDate | CREATION_DATE | — | — |
| 5 | ApToleranceDescription | DESCRIPTION | — | ✅ |
| 6 | ApToleranceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ApToleranceLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ApToleranceLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ApToleranceMaxQtyOrdTolerance | MAX_QTY_ORD_TOLERANCE | — | ✅ |
| 10 | ApToleranceMaxQtyRecTolerance | MAX_QTY_REC_TOLERANCE | — | ✅ |
| 11 | ApToleranceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ApTolerancePriceTolerance | PRICE_TOLERANCE | — | ✅ |
| 13 | ApToleranceQtyReceivedTolerance | QTY_RECEIVED_TOLERANCE | — | ✅ |
| 14 | ApToleranceQuantityTolerance | QUANTITY_TOLERANCE | — | ✅ |
| 15 | ApToleranceRateAmtTolerance | RATE_AMT_TOLERANCE | — | ✅ |
| 16 | ApToleranceShipAmtTolerance | SHIP_AMT_TOLERANCE | — | ✅ |
| 17 | ApToleranceToleranceId | TOLERANCE_ID | — | — |
| 18 | ApToleranceToleranceName | TOLERANCE_NAME | — | ✅ |
| 19 | ApToleranceToleranceType | TOLERANCE_TYPE | — | ✅ |
| 20 | ApToleranceTotalAmtTolerance | TOTAL_AMT_TOLERANCE | — | ✅ |

### [[fnd_territories_vl|FND_TERRITORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TerritoryAddressStyle | ADDRESS_STYLE | — | — |
| 2 | TerritoryAddressValidation | ADDRESS_VALIDATION | — | — |
| 3 | TerritoryAlternateTerritoryCode | ALTERNATE_TERRITORY_CODE | — | — |
| 4 | TerritoryBankInfoStyle | BANK_INFO_STYLE | — | — |
| 5 | TerritoryBankInfoValidation | BANK_INFO_VALIDATION | — | — |
| 6 | TerritoryCreatedBy | CREATED_BY | — | — |
| 7 | TerritoryCreationDate | CREATION_DATE | — | — |
| 8 | TerritoryCurrencyCode | CURRENCY_CODE | — | — |
| 9 | TerritoryDescription | DESCRIPTION | — | — |
| 10 | TerritoryEnabledFlag | ENABLED_FLAG | — | — |
| 11 | TerritoryEuCode | EU_CODE | — | — |
| 12 | TerritoryIsoNumericCode | ISO_NUMERIC_CODE | — | — |
| 13 | TerritoryIsoTerritoryCode | ISO_TERRITORY_CODE | — | — |
| 14 | TerritoryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | TerritoryLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | TerritoryLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | TerritoryNlsTerritory | NLS_TERRITORY | — | — |
| 18 | TerritoryObsoleteFlag | OBSOLETE_FLAG | — | — |
| 19 | TerritoryShortName | TERRITORY_SHORT_NAME | — | — |
| 20 | TerritoryTerritoryCode | TERRITORY_CODE | — | — |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUCreatedBy | CREATED_BY | — | — |
| 2 | BUCreationDate | CREATION_DATE | — | — |
| 3 | BUDateFrom | DATE_FROM | — | — |
| 4 | BUDateTo | DATE_TO | — | — |
| 5 | BUDefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | — |
| 6 | BUDefaultSetId | DEFAULT_SET_ID | — | — |
| 7 | BUEnabledForHrFlag | ENABLED_FOR_HR_FLAG | — | — |
| 8 | BUEnterpriseId | BUSINESS_GROUP_ID | — | — |
| 9 | BUFinancialsBusinessUnitId | FIN_BUSINESS_UNIT_ID | — | — |
| 10 | BULastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | BULastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | BULastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | BULegalEntityId | LEGAL_ENTITY_ID | — | — |
| 14 | BULocationId | LOCATION_ID | — | — |
| 15 | BUManagerId | MANAGER_ID | — | — |
| 16 | BUName | BU_NAME | — | ✅ |
| 17 | BUPrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |
| 18 | BUShortCode | SHORT_CODE | — | ✅ |
| 19 | BUStatus | STATUS | — | — |
| 20 | BusinessUnitId | BU_ID | — | — |

### [[hz_locations|HZ_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocationActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | LocationAddrElementAttribute1 | ADDR_ELEMENT_ATTRIBUTE1 | — | — |
| 3 | LocationAddrElementAttribute2 | ADDR_ELEMENT_ATTRIBUTE2 | — | — |
| 4 | LocationAddrElementAttribute3 | ADDR_ELEMENT_ATTRIBUTE3 | — | — |
| 5 | LocationAddrElementAttribute4 | ADDR_ELEMENT_ATTRIBUTE4 | — | — |
| 6 | LocationAddrElementAttribute5 | ADDR_ELEMENT_ATTRIBUTE5 | — | — |
| 7 | LocationAddress1 | ADDRESS1 | — | ✅ |
| 8 | LocationAddress2 | ADDRESS2 | — | ✅ |
| 9 | LocationAddress3 | ADDRESS3 | — | ✅ |
| 10 | LocationAddress4 | ADDRESS4 | — | ✅ |
| 11 | LocationAddressEffectiveDate | ADDRESS_EFFECTIVE_DATE | — | — |
| 12 | LocationAddressExpirationDate | ADDRESS_EXPIRATION_DATE | — | — |
| 13 | LocationAddressLinesPhonetic | ADDRESS_LINES_PHONETIC | — | — |
| 14 | LocationAddressStyle | ADDRESS_STYLE | — | — |
| 15 | LocationBuilding | BUILDING | — | — |
| 16 | LocationCity | CITY | — | ✅ |
| 17 | LocationClliCode | CLLI_CODE | — | — |
| 18 | LocationComments | COMMENTS | — | — |
| 19 | LocationCountry | COUNTRY | — | ✅ |
| 20 | LocationCounty | COUNTY | — | ✅ |
| 21 | LocationCreatedByModule | CREATED_BY_MODULE | — | — |
| 22 | LocationDateValidated | DATE_VALIDATED | — | — |
| 23 | LocationDescription | DESCRIPTION | — | — |
| 24 | LocationDoNotValidateFlag | DO_NOT_VALIDATE_FLAG | — | — |
| 25 | LocationFaLocationId | FA_LOCATION_ID | — | — |
| 26 | LocationFloorNumber | FLOOR_NUMBER | — | — |
| 27 | LocationGeometryStatusCode | GEOMETRY_STATUS_CODE | — | — |
| 28 | LocationHouseType | HOUSE_TYPE | — | — |
| 29 | LocationInternalFlag | INTERNAL_FLAG | — | — |
| 30 | LocationJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 31 | LocationJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 32 | LocationLanguage | LOCATION_LANGUAGE | — | — |
| 33 | LocationLocationDirections | LOCATION_DIRECTIONS | — | — |
| 34 | LocationLocationId | LOCATION_ID | — | — |
| 35 | LocationOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 36 | LocationPosition | POSITION | — | — |
| 37 | LocationPostalCode | POSTAL_CODE | — | ✅ |
| 38 | LocationPostalPlus4Code | POSTAL_PLUS4_CODE | — | — |
| 39 | LocationProvince | PROVINCE | — | ✅ |
| 40 | LocationSalesTaxGeocode | SALES_TAX_GEOCODE | — | — |
| 41 | LocationSalesTaxInsideCityLimits | SALES_TAX_INSIDE_CITY_LIMITS | — | — |
| 42 | LocationShortDescription | SHORT_DESCRIPTION | — | — |
| 43 | LocationState | STATE | — | ✅ |
| 44 | LocationStatusFlag | STATUS_FLAG | — | — |
| 45 | LocationTimezoneCode | TIMEZONE_CODE | — | — |
| 46 | LocationValidatedFlag | VALIDATED_FLAG | — | — |
| 47 | LocationValidationStatusCode | VALIDATION_STATUS_CODE | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SuppPartyPartyId | PARTY_ID | — | — |
| 2 | SuppPartyPartyName | PARTY_NAME | — | ✅ |

### [[hz_party_sites|HZ_PARTY_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartySiteActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | PartySiteAddressee | ADDRESSEE | — | — |
| 3 | PartySiteComments | COMMENTS | — | — |
| 4 | PartySiteCreatedByModule | CREATED_BY_MODULE | — | — |
| 5 | PartySiteDunsNumberC | DUNS_NUMBER_C | — | ✅ |
| 6 | PartySiteEndDateActive | END_DATE_ACTIVE | — | — |
| 7 | PartySiteGlobalLocationNumber | GLOBAL_LOCATION_NUMBER | — | — |
| 8 | PartySiteIdentifyingAddressFlag | IDENTIFYING_ADDRESS_FLAG | — | — |
| 9 | PartySiteLanguage | PARTY_SITE_LANGUAGE | — | — |
| 10 | PartySiteLocationId | LOCATION_ID | — | — |
| 11 | PartySiteMailstop | MAILSTOP | — | — |
| 12 | PartySiteOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 13 | PartySitePartyId | PARTY_ID | — | — |
| 14 | PartySitePartyNameDba | PARTY_NAME_DBA | — | — |
| 15 | PartySitePartyNameDivision | PARTY_NAME_DIVISION | — | — |
| 16 | PartySitePartyNameLegal | PARTY_NAME_LEGAL | — | — |
| 17 | PartySitePartySiteId | PARTY_SITE_ID | — | — |
| 18 | PartySitePartySiteName | PARTY_SITE_NAME | — | ✅ |
| 19 | PartySitePartySiteNumber | PARTY_SITE_NUMBER | — | — |
| 20 | PartySitePartySiteType | PARTY_SITE_TYPE | — | — |
| 21 | PartySitePartyUsageCode | PARTY_USAGE_CODE | — | — |
| 22 | PartySiteRelationshipId | RELATIONSHIP_ID | — | — |
| 23 | PartySiteStartDateActive | START_DATE_ACTIVE | — | — |
| 24 | PartySiteStatus | STATUS | — | — |

### [[poz_bi_sup_sites_ap_inv_dist_v|POZ_BI_SUP_SITES_AP_INV_DIST_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SuppSiteInvDistAmount | AMOUNT | — | ✅ |
| 2 | SuppSiteInvDistVendorSiteId | VENDOR_SITE_ID | — | — |

### [[poz_suppliers|POZ_SUPPLIERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupplierAllowAwtFlag | ALLOW_AWT_FLAG | — | ✅ |
| 2 | SupplierAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 3 | SupplierApTaxRoundingRule | AP_TAX_ROUNDING_RULE | — | — |
| 4 | SupplierAutoTaxCalcFlag | AUTO_TAX_CALC_FLAG | — | — |
| 5 | SupplierAutoTaxCalcOverride | AUTO_TAX_CALC_OVERRIDE | — | — |
| 6 | SupplierAwtGroupId | AWT_GROUP_ID | — | — |
| 7 | SupplierBusinessRelationship | BUSINESS_RELATIONSHIP | — | — |
| 8 | SupplierCorporateWebsite | CORPORATE_WEBSITE | — | — |
| 9 | SupplierCreatedBy | CREATED_BY | — | — |
| 10 | SupplierCreationDate | CREATION_DATE | — | — |
| 11 | SupplierCustomerNum | CUSTOMER_NUM | — | — |
| 12 | SupplierEmployeeId | EMPLOYEE_ID | — | — |
| 13 | SupplierEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 14 | SupplierFederalReportableFlag | FEDERAL_REPORTABLE_FLAG | — | — |
| 15 | SupplierIncomeTaxIdFlag | INCOME_TAX_ID_FLAG | — | — |
| 16 | SupplierLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | SupplierLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | SupplierLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | SupplierMinOrderAmount | MIN_ORDER_AMOUNT | — | — |
| 20 | SupplierNameControl | NAME_CONTROL | — | — |
| 21 | SupplierNiNumber | NI_NUMBER | — | — |
| 22 | SupplierObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | SupplierOffsetTaxFlag | OFFSET_TAX_FLAG | — | — |
| 24 | SupplierOffsetVatCode | OFFSET_VAT_CODE | — | — |
| 25 | SupplierOneTimeFlag | ONE_TIME_FLAG | — | — |
| 26 | SupplierOrganizationTypeLookupCode | ORGANIZATION_TYPE_LOOKUP_CODE | — | — |
| 27 | SupplierParentPartyId | PARENT_PARTY_ID | — | — |
| 28 | SupplierParentVendorId | PARENT_VENDOR_ID | — | — |
| 29 | SupplierPartyId | PARTY_ID | — | ✅ |
| 30 | SupplierProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 31 | SupplierProgramId | PROGRAM_ID | — | — |
| 32 | SupplierProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 33 | SupplierRequestId | REQUEST_ID | — | — |
| 34 | SupplierSegment1 | SEGMENT1 | — | ✅ |
| 35 | SupplierSpendAuthReviewStatus | SPEND_AUTH_REVIEW_STATUS | — | — |
| 36 | SupplierStandardIndustryClass | STANDARD_INDUSTRY_CLASS | — | — |
| 37 | SupplierStartDateActive | START_DATE_ACTIVE | — | — |
| 38 | SupplierStateReportableFlag | STATE_REPORTABLE_FLAG | — | — |
| 39 | SupplierTaxReportingName | TAX_REPORTING_NAME | — | — |
| 40 | SupplierTaxVerificationDate | TAX_VERIFICATION_DATE | — | — |
| 41 | SupplierTaxpayerCountry | TAXPAYER_COUNTRY | — | — |
| 42 | SupplierType1099 | TYPE_1099 | — | — |
| 43 | SupplierVatCode | VAT_CODE | — | — |
| 44 | SupplierVendorId | VENDOR_ID | — | ✅ |
| 45 | SupplierVendorTypeLookupCode | VENDOR_TYPE_LOOKUP_CODE | — | — |
| 46 | SupplierWithholdingStartDate | WITHHOLDING_START_DATE | — | — |
| 47 | SupplierWithholdingStatusLookupCode | WITHHOLDING_STATUS_LOOKUP_CODE | — | — |

### [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AltPaySiteVendorSiteCode | VENDOR_SITE_CODE | — | ✅ |
| 2 | AltPaySiteVendorSiteId | VENDOR_SITE_ID | — | — |
| 3 | B2bCommMethodCode | B2B_COMM_METHOD_CODE | — | ✅ |
| 4 | BuyerManagedTransportFlag | BUYER_MANAGED_TRANSPORT_FLAG | — | ✅ |
| 5 | InvoiceChannel | INVOICE_CHANNEL | — | ✅ |
| 6 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | PoAckReqdCode | PO_ACK_REQD_CODE | — | ✅ |
| 8 | PoAckReqdDays | PO_ACK_REQD_DAYS | — | ✅ |
| 9 | SupplierSiteAgingOnsetPoint | AGING_ONSET_POINT | — | ✅ |
| 10 | SupplierSiteAgingPeriodDays | AGING_PERIOD_DAYS | — | ✅ |
| 11 | SupplierSiteAllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | ✅ |
| 12 | SupplierSiteAllowUnorderedReceiptsFlag | ALLOW_UNORDERED_RECEIPTS_FLAG | — | ✅ |
| 13 | SupplierSiteAlwaysTakeDiscFlag | ALWAYS_TAKE_DISC_FLAG | — | ✅ |
| 14 | SupplierSiteAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 15 | SupplierSiteApTaxRoundingRule | AP_TAX_ROUNDING_RULE | — | — |
| 16 | SupplierSiteAreaCode | AREA_CODE | — | ✅ |
| 17 | SupplierSiteAttentionArFlag | ATTENTION_AR_FLAG | — | — |
| 18 | SupplierSiteAttribute1 | ATTRIBUTE1 | — | ✅ |
| 19 | SupplierSiteAttribute10 | ATTRIBUTE10 | — | ✅ |
| 20 | SupplierSiteAttribute11 | ATTRIBUTE11 | — | ✅ |
| 21 | SupplierSiteAttribute12 | ATTRIBUTE12 | — | ✅ |
| 22 | SupplierSiteAttribute13 | ATTRIBUTE13 | — | ✅ |
| 23 | SupplierSiteAttribute14 | ATTRIBUTE14 | — | ✅ |
| 24 | SupplierSiteAttribute15 | ATTRIBUTE15 | — | ✅ |
| 25 | SupplierSiteAttribute16 | ATTRIBUTE16 | — | ✅ |
| 26 | SupplierSiteAttribute17 | ATTRIBUTE17 | — | ✅ |
| 27 | SupplierSiteAttribute18 | ATTRIBUTE18 | — | ✅ |
| 28 | SupplierSiteAttribute19 | ATTRIBUTE19 | — | ✅ |
| 29 | SupplierSiteAttribute2 | ATTRIBUTE2 | — | ✅ |
| 30 | SupplierSiteAttribute20 | ATTRIBUTE20 | — | ✅ |
| 31 | SupplierSiteAttribute3 | ATTRIBUTE3 | — | ✅ |
| 32 | SupplierSiteAttribute4 | ATTRIBUTE4 | — | ✅ |
| 33 | SupplierSiteAttribute5 | ATTRIBUTE5 | — | ✅ |
| 34 | SupplierSiteAttribute6 | ATTRIBUTE6 | — | ✅ |
| 35 | SupplierSiteAttribute7 | ATTRIBUTE7 | — | ✅ |
| 36 | SupplierSiteAttribute8 | ATTRIBUTE8 | — | ✅ |
| 37 | SupplierSiteAttribute9 | ATTRIBUTE9 | — | ✅ |
| 38 | SupplierSiteAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 39 | SupplierSiteAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 40 | SupplierSiteAttributeDate10 | ATTRIBUTE_DATE10 | — | ✅ |
| 41 | SupplierSiteAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 42 | SupplierSiteAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 43 | SupplierSiteAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 44 | SupplierSiteAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 45 | SupplierSiteAttributeDate6 | ATTRIBUTE_DATE6 | — | ✅ |
| 46 | SupplierSiteAttributeDate7 | ATTRIBUTE_DATE7 | — | ✅ |
| 47 | SupplierSiteAttributeDate8 | ATTRIBUTE_DATE8 | — | ✅ |
| 48 | SupplierSiteAttributeDate9 | ATTRIBUTE_DATE9 | — | ✅ |
| 49 | SupplierSiteAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 50 | SupplierSiteAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 51 | SupplierSiteAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 52 | SupplierSiteAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 53 | SupplierSiteAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 54 | SupplierSiteAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 55 | SupplierSiteAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 56 | SupplierSiteAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 57 | SupplierSiteAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 58 | SupplierSiteAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 59 | SupplierSiteAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 60 | SupplierSiteAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | ✅ |
| 61 | SupplierSiteAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 62 | SupplierSiteAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 63 | SupplierSiteAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 64 | SupplierSiteAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 65 | SupplierSiteAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | ✅ |
| 66 | SupplierSiteAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | ✅ |
| 67 | SupplierSiteAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | ✅ |
| 68 | SupplierSiteAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | ✅ |
| 69 | SupplierSiteAutoCalculateInterestFlag | AUTO_CALCULATE_INTEREST_FLAG | — | ✅ |
| 70 | SupplierSiteAutoTaxCalcFlag | AUTO_TAX_CALC_FLAG | — | — |
| 71 | SupplierSiteAutoTaxCalcOverride | AUTO_TAX_CALC_OVERRIDE | — | — |
| 72 | SupplierSiteB2bSiteCode | B2B_SITE_CODE | — | ✅ |
| 73 | SupplierSiteBankChargeDeductionType | BANK_CHARGE_DEDUCTION_TYPE | — | ✅ |
| 74 | SupplierSiteCarrierId | CARRIER_ID | — | — |
| 75 | SupplierSiteConsumptionAdviceFrequency | CONSUMPTION_ADVICE_FREQUENCY | — | ✅ |
| 76 | SupplierSiteConsumptionAdviceSummary | CONSUMPTION_ADVICE_SUMMARY | — | ✅ |
| 77 | SupplierSiteCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | ✅ |
| 78 | SupplierSiteCreateDebitMemoFlag | CREATE_DEBIT_MEMO_FLAG | — | ✅ |
| 79 | SupplierSiteCreatedBy | CREATED_BY | — | ✅ |
| 80 | SupplierSiteCreationDate | CREATION_DATE | — | ✅ |
| 81 | SupplierSiteCustomerNum | CUSTOMER_NUM | — | ✅ |
| 82 | SupplierSiteDaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | ✅ |
| 83 | SupplierSiteDaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | ✅ |
| 84 | SupplierSiteDefaultPaySiteId | DEFAULT_PAY_SITE_ID | — | ✅ |
| 85 | SupplierSiteEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 86 | SupplierSiteEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 87 | SupplierSiteEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 88 | SupplierSiteEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 89 | SupplierSiteEnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | ✅ |
| 90 | SupplierSiteExcludeFreightFromDiscount | EXCLUDE_FREIGHT_FROM_DISCOUNT | — | ✅ |
| 91 | SupplierSiteExcludeTaxFromDiscount | EXCLUDE_TAX_FROM_DISCOUNT | — | ✅ |
| 92 | SupplierSiteFax | FAX | — | ✅ |
| 93 | SupplierSiteFaxAreaCode | FAX_AREA_CODE | — | ✅ |
| 94 | SupplierSiteFaxCountryCode | FAX_COUNTRY_CODE | — | ✅ |
| 95 | SupplierSiteFobLookupCode | FOB_LOOKUP_CODE | — | ✅ |
| 96 | SupplierSiteFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | ✅ |
| 97 | SupplierSiteGaplessInvNumFlag | GAPLESS_INV_NUM_FLAG | — | ✅ |
| 98 | SupplierSiteGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | ✅ |
| 99 | SupplierSiteGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | ✅ |
| 100 | SupplierSiteGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | ✅ |
| 101 | SupplierSiteGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | ✅ |
| 102 | SupplierSiteGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | ✅ |
| 103 | SupplierSiteGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | ✅ |
| 104 | SupplierSiteGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | ✅ |
| 105 | SupplierSiteGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | ✅ |
| 106 | SupplierSiteGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | ✅ |
| 107 | SupplierSiteGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | ✅ |
| 108 | SupplierSiteGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | ✅ |
| 109 | SupplierSiteGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | ✅ |
| 110 | SupplierSiteGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | ✅ |
| 111 | SupplierSiteGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | ✅ |
| 112 | SupplierSiteGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | ✅ |
| 113 | SupplierSiteGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | ✅ |
| 114 | SupplierSiteGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | ✅ |
| 115 | SupplierSiteGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | ✅ |
| 116 | SupplierSiteGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | ✅ |
| 117 | SupplierSiteGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | ✅ |
| 118 | SupplierSiteGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | ✅ |
| 119 | SupplierSiteGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | ✅ |
| 120 | SupplierSiteGlobalAttributeDate10 | GLOBAL_ATTRIBUTE_DATE10 | — | ✅ |
| 121 | SupplierSiteGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | ✅ |
| 122 | SupplierSiteGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | ✅ |
| 123 | SupplierSiteGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | ✅ |
| 124 | SupplierSiteGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | ✅ |
| 125 | SupplierSiteGlobalAttributeDate6 | GLOBAL_ATTRIBUTE_DATE6 | — | ✅ |
| 126 | SupplierSiteGlobalAttributeDate7 | GLOBAL_ATTRIBUTE_DATE7 | — | ✅ |
| 127 | SupplierSiteGlobalAttributeDate8 | GLOBAL_ATTRIBUTE_DATE8 | — | ✅ |
| 128 | SupplierSiteGlobalAttributeDate9 | GLOBAL_ATTRIBUTE_DATE9 | — | ✅ |
| 129 | SupplierSiteGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | ✅ |
| 130 | SupplierSiteGlobalAttributeNumber10 | GLOBAL_ATTRIBUTE_NUMBER10 | — | ✅ |
| 131 | SupplierSiteGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | ✅ |
| 132 | SupplierSiteGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | ✅ |
| 133 | SupplierSiteGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | ✅ |
| 134 | SupplierSiteGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | ✅ |
| 135 | SupplierSiteGlobalAttributeNumber6 | GLOBAL_ATTRIBUTE_NUMBER6 | — | ✅ |
| 136 | SupplierSiteGlobalAttributeNumber7 | GLOBAL_ATTRIBUTE_NUMBER7 | — | ✅ |
| 137 | SupplierSiteGlobalAttributeNumber8 | GLOBAL_ATTRIBUTE_NUMBER8 | — | ✅ |
| 138 | SupplierSiteGlobalAttributeNumber9 | GLOBAL_ATTRIBUTE_NUMBER9 | — | ✅ |
| 139 | SupplierSiteGlobalAttributeTimestamp1 | GLOBAL_ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 140 | SupplierSiteGlobalAttributeTimestamp10 | GLOBAL_ATTRIBUTE_TIMESTAMP10 | — | ✅ |
| 141 | SupplierSiteGlobalAttributeTimestamp2 | GLOBAL_ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 142 | SupplierSiteGlobalAttributeTimestamp3 | GLOBAL_ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 143 | SupplierSiteGlobalAttributeTimestamp4 | GLOBAL_ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 144 | SupplierSiteGlobalAttributeTimestamp5 | GLOBAL_ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 145 | SupplierSiteGlobalAttributeTimestamp6 | GLOBAL_ATTRIBUTE_TIMESTAMP6 | — | ✅ |
| 146 | SupplierSiteGlobalAttributeTimestamp7 | GLOBAL_ATTRIBUTE_TIMESTAMP7 | — | ✅ |
| 147 | SupplierSiteGlobalAttributeTimestamp8 | GLOBAL_ATTRIBUTE_TIMESTAMP8 | — | ✅ |
| 148 | SupplierSiteGlobalAttributeTimestamp9 | GLOBAL_ATTRIBUTE_TIMESTAMP9 | — | ✅ |
| 149 | SupplierSiteHoldAllPaymentsFlag | HOLD_ALL_PAYMENTS_FLAG | — | ✅ |
| 150 | SupplierSiteHoldBy | HOLD_BY | — | ✅ |
| 151 | SupplierSiteHoldDate | HOLD_DATE | — | ✅ |
| 152 | SupplierSiteHoldFlag | HOLD_FLAG | — | ✅ |
| 153 | SupplierSiteHoldFuturePaymentsFlag | HOLD_FUTURE_PAYMENTS_FLAG | — | ✅ |
| 154 | SupplierSiteHoldReason | HOLD_REASON | — | ✅ |
| 155 | SupplierSiteHoldUnmatchedInvoicesFlag | HOLD_UNMATCHED_INVOICES_FLAG | — | ✅ |
| 156 | SupplierSiteInactiveDate | INACTIVE_DATE | — | ✅ |
| 157 | SupplierSiteInspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | ✅ |
| 158 | SupplierSiteInvoiceAmountLimit | INVOICE_AMOUNT_LIMIT | — | ✅ |
| 159 | SupplierSiteInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 160 | SupplierSiteLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 161 | SupplierSiteLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 162 | SupplierSiteLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 163 | SupplierSiteLocationId | LOCATION_ID | — | ✅ |
| 164 | SupplierSiteMatchOption | MATCH_OPTION | — | ✅ |
| 165 | SupplierSiteModeOfTransport | MODE_OF_TRANSPORT | — | ✅ |
| 166 | SupplierSiteObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 167 | SupplierSiteOffsetTaxFlag | OFFSET_TAX_FLAG | — | — |
| 168 | SupplierSiteOffsetVatCode | OFFSET_VAT_CODE | — | — |
| 169 | SupplierSitePartySiteId | PARTY_SITE_ID | — | ✅ |
| 170 | SupplierSitePayDateBasisLookupCode | PAY_DATE_BASIS_LOOKUP_CODE | — | ✅ |
| 171 | SupplierSitePayGroupLookupCode | PAY_GROUP_LOOKUP_CODE | — | ✅ |
| 172 | SupplierSitePayOnCode | PAY_ON_CODE | — | ✅ |
| 173 | SupplierSitePayOnReceiptSummaryCode | PAY_ON_RECEIPT_SUMMARY_CODE | — | ✅ |
| 174 | SupplierSitePayOnUseFlag | PAY_ON_USE_FLAG | — | ✅ |
| 175 | SupplierSitePaySiteFlag | PAY_SITE_FLAG | — | ✅ |
| 176 | SupplierSitePaymentCurrencyCode | PAYMENT_CURRENCY_CODE | — | ✅ |
| 177 | SupplierSitePaymentPriority | PAYMENT_PRIORITY | — | ✅ |
| 178 | SupplierSitePcardSiteFlag | PCARD_SITE_FLAG | — | ✅ |
| 179 | SupplierSitePhone | PHONE | — | ✅ |
| 180 | SupplierSitePhoneCountryCode | PHONE_COUNTRY_CODE | — | ✅ |
| 181 | SupplierSitePhoneExtension | PHONE_EXTENSION | — | ✅ |
| 182 | SupplierSitePrcBuId | PRC_BU_ID | — | ✅ |
| 183 | SupplierSitePrimaryPaySiteFlag | PRIMARY_PAY_SITE_FLAG | — | ✅ |
| 184 | SupplierSiteProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 185 | SupplierSiteProgramId | PROGRAM_ID | — | — |
| 186 | SupplierSiteProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 187 | SupplierSitePurchasingHoldReason | PURCHASING_HOLD_REASON | — | ✅ |
| 188 | SupplierSitePurchasingSiteFlag | PURCHASING_SITE_FLAG | — | ✅ |
| 189 | SupplierSiteQtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | ✅ |
| 190 | SupplierSiteQtyRcvTolerance | QTY_RCV_TOLERANCE | — | ✅ |
| 191 | SupplierSiteReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | ✅ |
| 192 | SupplierSiteReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | ✅ |
| 193 | SupplierSiteReceivingRoutingId | RECEIVING_ROUTING_ID | — | ✅ |
| 194 | SupplierSiteRequestId | REQUEST_ID | — | — |
| 195 | SupplierSiteRetainageRate | RETAINAGE_RATE | — | — |
| 196 | SupplierSiteRfqOnlySiteFlag | RFQ_ONLY_SITE_FLAG | — | ✅ |
| 197 | SupplierSiteSellingCompanyIdentifier | SELLING_COMPANY_IDENTIFIER | — | ✅ |
| 198 | SupplierSiteServiceLevel | SERVICE_LEVEL | — | ✅ |
| 199 | SupplierSiteServicesToleranceId | SERVICES_TOLERANCE_ID | — | — |
| 200 | SupplierSiteShippingControl | SHIPPING_CONTROL | — | — |
| 201 | SupplierSiteShippingNetworkLocation | SHIPPING_NETWORK_LOCATION | — | — |
| 202 | SupplierSiteSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | ✅ |
| 203 | SupplierSiteTaxCountryCode | TAX_COUNTRY_CODE | — | — |
| 204 | SupplierSiteTaxReportingSiteFlag | TAX_REPORTING_SITE_FLAG | — | ✅ |
| 205 | SupplierSiteTermsDateBasis | TERMS_DATE_BASIS | — | ✅ |
| 206 | SupplierSiteTermsId | TERMS_ID | — | ✅ |
| 207 | SupplierSiteToleranceId | TOLERANCE_ID | — | ✅ |
| 208 | SupplierSiteVatCode | VAT_CODE | — | ✅ |
| 209 | SupplierSiteVatRegistrationNum | VAT_REGISTRATION_NUM | — | ✅ |
| 210 | SupplierSiteVendorId | VENDOR_ID | — | ✅ |
| 211 | SupplierSiteVendorSiteCode | VENDOR_SITE_CODE | — | ✅ |
| 212 | SupplierSiteVendorSiteCodeAlt | VENDOR_SITE_CODE_ALT | — | ✅ |
| 213 | SupplierSiteVendorSiteSpkId | VENDOR_SITE_SPK_ID | — | — |
| 214 | VendorSiteId | VENDOR_SITE_ID | 🔑 | ✅ |

### [[poz_supplier_sites_pii|POZ_SUPPLIER_SITES_PII]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupplierSitePiiVatRegistrationNum | VAT_REGISTRATION_NUM | — | — |
| 2 | SupplierSitePiiVendorSiteId | VENDOR_SITE_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
