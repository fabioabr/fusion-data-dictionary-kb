---
id: DOC-PO-PVO-SupplierProductsServicesPVO
doc_type: system-doc
title: "SupplierProductsServicesPVO — PVO Purchasing"
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
  - SupplierProductsServicesPVO
  - supplierproductsservicespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierProductsServicesPVO

## 📌 Visão Geral

Disponibiliza o catálogo de produtos e serviços dos fornecedores para consulta, com categorias, atributos e status. Facilita a busca por fontes de fornecimento por categoria de item.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.SupplierProductsServicesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 151 | 4 | 3 | 13 | 9% |

---

## 🔗 Tabelas Relacionadas

- [[hz_parties|HZ_PARTIES]] — 82 atributos (2 BICC)
- [[poz_suppliers|POZ_SUPPLIERS]] — 49 atributos (2 BICC)
- [[poz_supp_prod_services_attr_v|POZ_SUPP_PROD_SERVICES_ATTR_V]] — 9 atributos (2 PKs, 7 BICC)
- [[poz_sup_products_services|POZ_SUP_PRODUCTS_SERVICES]] — 11 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 2 | PartyAddress1 | ADDRESS1 | — | — |
| 3 | PartyAddress2 | ADDRESS2 | — | — |
| 4 | PartyAddress3 | ADDRESS3 | — | — |
| 5 | PartyAddress4 | ADDRESS4 | — | — |
| 6 | PartyAnalysisFy | ANALYSIS_FY | — | — |
| 7 | PartyCategoryCode | CATEGORY_CODE | — | — |
| 8 | PartyCeoName | CEO_NAME | — | — |
| 9 | PartyCertReasonCode | CERT_REASON_CODE | — | — |
| 10 | PartyCertificationLevel | CERTIFICATION_LEVEL | — | — |
| 11 | PartyCity | CITY | — | — |
| 12 | PartyComments | COMMENTS | — | — |
| 13 | PartyCountry | COUNTRY | — | — |
| 14 | PartyCounty | COUNTY | — | — |
| 15 | PartyCreatedBy | CREATED_BY | — | — |
| 16 | PartyCreatedByModule | CREATED_BY_MODULE | — | — |
| 17 | PartyCreationDate | CREATION_DATE | — | — |
| 18 | PartyCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 19 | PartyDateOfBirth | DATE_OF_BIRTH | — | — |
| 20 | PartyDunsNumberC | DUNS_NUMBER_C | — | — |
| 21 | PartyEmailAddress | EMAIL_ADDRESS | — | — |
| 22 | PartyEmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 23 | PartyFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 24 | PartyGender | GENDER | — | — |
| 25 | PartyGroupType | GROUP_TYPE | — | — |
| 26 | PartyGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | — |
| 27 | PartyHomeCountry | HOME_COUNTRY | — | — |
| 28 | PartyHqBranchInd | HQ_BRANCH_IND | — | — |
| 29 | PartyIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 30 | PartyIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | — |
| 31 | PartyInternalFlag | INTERNAL_FLAG | — | — |
| 32 | PartyJgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 33 | PartyLanguageName | LANGUAGE_NAME | — | — |
| 34 | PartyLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 35 | PartyLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 36 | PartyMaritalStatus | MARITAL_STATUS | — | — |
| 37 | PartyMissionStatement | MISSION_STATEMENT | — | — |
| 38 | PartyNextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 39 | PartyObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 40 | PartyOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 41 | PartyPartyId | PARTY_ID | — | — |
| 42 | PartyPartyName | PARTY_NAME | — | ✅ |
| 43 | PartyPartyNumber | PARTY_NUMBER | — | — |
| 44 | PartyPartyType | PARTY_TYPE | — | — |
| 45 | PartyPartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 46 | PartyPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 47 | PartyPersonFirstName | PERSON_FIRST_NAME | — | — |
| 48 | PartyPersonLastName | PERSON_LAST_NAME | — | — |
| 49 | PartyPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 50 | PartyPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 51 | PartyPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 52 | PartyPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 53 | PartyPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 54 | PartyPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 55 | PartyPersonTitle | PERSON_TITLE | — | — |
| 56 | PartyPostalCode | POSTAL_CODE | — | — |
| 57 | PartyPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 58 | PartyPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 59 | PartyPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 60 | PartyPreferredName | PREFERRED_NAME | — | — |
| 61 | PartyPreferredNameId | PREFERRED_NAME_ID | — | — |
| 62 | PartyPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | — |
| 63 | PartyPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 64 | PartyPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 65 | PartyPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 66 | PartyPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 67 | PartyPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 68 | PartyPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | — |
| 69 | PartyPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 70 | PartyPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 71 | PartyProvince | PROVINCE | — | — |
| 72 | PartySalutation | SALUTATION | — | — |
| 73 | PartySicCode | SIC_CODE | — | — |
| 74 | PartySicCodeType | SIC_CODE_TYPE | — | — |
| 75 | PartyState | STATE | — | — |
| 76 | PartyStatus | STATUS | — | — |
| 77 | PartyThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 78 | PartyTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 79 | PartyUrl | URL | — | — |
| 80 | PartyUserGuid | USER_GUID | — | — |
| 81 | PartyValidatedFlag | VALIDATED_FLAG | — | — |
| 82 | PartyYearEstablished | YEAR_ESTABLISHED | — | — |

### [[poz_suppliers|POZ_SUPPLIERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupplierAllowAwtFlag | ALLOW_AWT_FLAG | — | — |
| 2 | SupplierAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 3 | SupplierApTaxRoundingRule | AP_TAX_ROUNDING_RULE | — | — |
| 4 | SupplierAutoTaxCalcFlag | AUTO_TAX_CALC_FLAG | — | — |
| 5 | SupplierAutoTaxCalcOverride | AUTO_TAX_CALC_OVERRIDE | — | — |
| 6 | SupplierAwtGroupId | AWT_GROUP_ID | — | — |
| 7 | SupplierBusinessRelationship | BUSINESS_RELATIONSHIP | — | — |
| 8 | SupplierCorporateWebsite | CORPORATE_WEBSITE | — | — |
| 9 | SupplierCreatedBy | CREATED_BY | — | — |
| 10 | SupplierCreationDate | CREATION_DATE | — | — |
| 11 | SupplierCreationSource | CREATION_SOURCE | — | — |
| 12 | SupplierCustomerNum | CUSTOMER_NUM | — | — |
| 13 | SupplierEmployeeId | EMPLOYEE_ID | — | — |
| 14 | SupplierEndDateActive | END_DATE_ACTIVE | — | — |
| 15 | SupplierFederalReportableFlag | FEDERAL_REPORTABLE_FLAG | — | — |
| 16 | SupplierIncomeTaxIdFlag | INCOME_TAX_ID_FLAG | — | — |
| 17 | SupplierLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | SupplierLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | SupplierLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | SupplierMinOrderAmount | MIN_ORDER_AMOUNT | — | — |
| 21 | SupplierNameControl | NAME_CONTROL | — | — |
| 22 | SupplierNiNumber | NI_NUMBER | — | — |
| 23 | SupplierObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 24 | SupplierOffsetTaxFlag | OFFSET_TAX_FLAG | — | — |
| 25 | SupplierOffsetVatCode | OFFSET_VAT_CODE | — | — |
| 26 | SupplierOneTimeFlag | ONE_TIME_FLAG | — | — |
| 27 | SupplierOrganizationTypeLookupCode | ORGANIZATION_TYPE_LOOKUP_CODE | — | — |
| 28 | SupplierParentPartyId | PARENT_PARTY_ID | — | — |
| 29 | SupplierParentVendorId | PARENT_VENDOR_ID | — | — |
| 30 | SupplierPartyId | PARTY_ID | — | — |
| 31 | SupplierProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 32 | SupplierProgramId | PROGRAM_ID | — | — |
| 33 | SupplierProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 34 | SupplierRequestId | REQUEST_ID | — | — |
| 35 | SupplierReviewType | REVIEW_TYPE | — | — |
| 36 | SupplierSegment1 | SEGMENT1 | — | ✅ |
| 37 | SupplierSpendAuthReviewStatus | SPEND_AUTH_REVIEW_STATUS | — | — |
| 38 | SupplierStandardIndustryClass | STANDARD_INDUSTRY_CLASS | — | — |
| 39 | SupplierStartDateActive | START_DATE_ACTIVE | — | — |
| 40 | SupplierStateReportableFlag | STATE_REPORTABLE_FLAG | — | — |
| 41 | SupplierTaxReportingName | TAX_REPORTING_NAME | — | — |
| 42 | SupplierTaxVerificationDate | TAX_VERIFICATION_DATE | — | — |
| 43 | SupplierTaxpayerCountry | TAXPAYER_COUNTRY | — | — |
| 44 | SupplierType1099 | TYPE_1099 | — | — |
| 45 | SupplierVatCode | VAT_CODE | — | — |
| 46 | SupplierVendorId | VENDOR_ID | — | — |
| 47 | SupplierVendorTypeLookupCode | VENDOR_TYPE_LOOKUP_CODE | — | — |
| 48 | SupplierWithholdingStartDate | WITHHOLDING_START_DATE | — | — |
| 49 | SupplierWithholdingStatusLookupCode | WITHHOLDING_STATUS_LOOKUP_CODE | — | — |

### [[poz_supp_prod_services_attr_v|POZ_SUPP_PROD_SERVICES_ATTR_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AncestorCategoryId | ANCESTOR_CATEGORY_ID | 🔑 | ✅ |
| 2 | CategoryId | CATEGORY_ID | 🔑 | ✅ |
| 3 | CategoryTreeAttrAncestorCategoryDescription | ANCESTOR_CATEGORY_DESCRIPTION | — | ✅ |
| 4 | CategoryTreeAttrAncestorCategoryName | ANCESTOR_CATEGORY_NAME | — | ✅ |
| 5 | CategoryTreeAttrCalculatedPath | CALCULATED_PATH | — | ✅ |
| 6 | CategoryTreeAttrCategoryDescription | CATEGORY_DESCRIPTION | — | ✅ |
| 7 | CategoryTreeAttrCategoryName | CATEGORY_NAME | — | ✅ |
| 8 | CategoryTreeAttrDistance | DISTANCE | — | — |
| 9 | CategoryTreeAttrIsleaf | ISLEAF | — | — |

### [[poz_sup_products_services|POZ_SUP_PRODUCTS_SERVICES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClassificationId | CLASSIFICATION_ID | 🔑 | ✅ |
| 2 | SupplierProductsServicesCategoryId | CATEGORY_ID | — | — |
| 3 | SupplierProductsServicesCreatedBy | CREATED_BY | — | — |
| 4 | SupplierProductsServicesCreationDate | CREATION_DATE | — | — |
| 5 | SupplierProductsServicesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | SupplierProductsServicesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | SupplierProductsServicesLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | SupplierProductsServicesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | SupplierProductsServicesPurchasingCatFlag | PURCHASING_CAT_FLAG | — | — |
| 10 | SupplierProductsServicesStatus | STATUS | — | — |
| 11 | SupplierProductsServicesVendorId | VENDOR_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
