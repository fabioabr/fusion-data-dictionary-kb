---
id: DOC-PO-PVO-NegotiationSupplierActivityPVO
doc_type: system-doc
title: "NegotiationSupplierActivityPVO — PVO Purchasing"
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
  - NegotiationSupplierActivityPVO
  - negotiationsupplieractivitypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationSupplierActivityPVO

## 📌 Visão Geral

Disponibiliza atividades de fornecedores em negociações para consulta operacional, permitindo monitoramento em tempo real da participação e interação no evento de sourcing.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.NegotiationSupplierActivityPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 523 | 4 | 6 | 523 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hz_parties|HZ_PARTIES]] — 141 atributos (141 BICC)
- [[pon_supplier_activities|PON_SUPPLIER_ACTIVITIES]] — 17 atributos (6 PKs, 17 BICC)
- [[poz_suppliers_v|POZ_SUPPLIERS_V]] — 148 atributos (148 BICC)
- [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]] — 217 atributos (217 BICC)

---

## ⚙️ Atributos

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PPEOAddress1 | ADDRESS1 | — | ✅ |
| 2 | PPEOAddress2 | ADDRESS2 | — | ✅ |
| 3 | PPEOAddress3 | ADDRESS3 | — | ✅ |
| 4 | PPEOAddress4 | ADDRESS4 | — | ✅ |
| 5 | PPEOAnalysisFy | ANALYSIS_FY | — | ✅ |
| 6 | PPEOAttribute1 | ATTRIBUTE1 | — | ✅ |
| 7 | PPEOAttribute10 | ATTRIBUTE10 | — | ✅ |
| 8 | PPEOAttribute11 | ATTRIBUTE11 | — | ✅ |
| 9 | PPEOAttribute12 | ATTRIBUTE12 | — | ✅ |
| 10 | PPEOAttribute13 | ATTRIBUTE13 | — | ✅ |
| 11 | PPEOAttribute14 | ATTRIBUTE14 | — | ✅ |
| 12 | PPEOAttribute15 | ATTRIBUTE15 | — | ✅ |
| 13 | PPEOAttribute16 | ATTRIBUTE16 | — | ✅ |
| 14 | PPEOAttribute17 | ATTRIBUTE17 | — | ✅ |
| 15 | PPEOAttribute18 | ATTRIBUTE18 | — | ✅ |
| 16 | PPEOAttribute19 | ATTRIBUTE19 | — | ✅ |
| 17 | PPEOAttribute2 | ATTRIBUTE2 | — | ✅ |
| 18 | PPEOAttribute20 | ATTRIBUTE20 | — | ✅ |
| 19 | PPEOAttribute21 | ATTRIBUTE21 | — | ✅ |
| 20 | PPEOAttribute22 | ATTRIBUTE22 | — | ✅ |
| 21 | PPEOAttribute23 | ATTRIBUTE23 | — | ✅ |
| 22 | PPEOAttribute24 | ATTRIBUTE24 | — | ✅ |
| 23 | PPEOAttribute25 | ATTRIBUTE25 | — | ✅ |
| 24 | PPEOAttribute26 | ATTRIBUTE26 | — | ✅ |
| 25 | PPEOAttribute27 | ATTRIBUTE27 | — | ✅ |
| 26 | PPEOAttribute28 | ATTRIBUTE28 | — | ✅ |
| 27 | PPEOAttribute29 | ATTRIBUTE29 | — | ✅ |
| 28 | PPEOAttribute3 | ATTRIBUTE3 | — | ✅ |
| 29 | PPEOAttribute30 | ATTRIBUTE30 | — | ✅ |
| 30 | PPEOAttribute4 | ATTRIBUTE4 | — | ✅ |
| 31 | PPEOAttribute5 | ATTRIBUTE5 | — | ✅ |
| 32 | PPEOAttribute6 | ATTRIBUTE6 | — | ✅ |
| 33 | PPEOAttribute7 | ATTRIBUTE7 | — | ✅ |
| 34 | PPEOAttribute8 | ATTRIBUTE8 | — | ✅ |
| 35 | PPEOAttribute9 | ATTRIBUTE9 | — | ✅ |
| 36 | PPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 37 | PPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 38 | PPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | ✅ |
| 39 | PPEOAttributeDate11 | ATTRIBUTE_DATE11 | — | ✅ |
| 40 | PPEOAttributeDate12 | ATTRIBUTE_DATE12 | — | ✅ |
| 41 | PPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 42 | PPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 43 | PPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 44 | PPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 45 | PPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | ✅ |
| 46 | PPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | ✅ |
| 47 | PPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | ✅ |
| 48 | PPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | ✅ |
| 49 | PPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 50 | PPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 51 | PPEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | ✅ |
| 52 | PPEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | ✅ |
| 53 | PPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 54 | PPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 55 | PPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 56 | PPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 57 | PPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 58 | PPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 59 | PPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 60 | PPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 61 | PPEOCategoryCode | CATEGORY_CODE | — | ✅ |
| 62 | PPEOCeoName | CEO_NAME | — | ✅ |
| 63 | PPEOCertReasonCode | CERT_REASON_CODE | — | ✅ |
| 64 | PPEOCertificationLevel | CERTIFICATION_LEVEL | — | ✅ |
| 65 | PPEOCity | CITY | — | ✅ |
| 66 | PPEOComments | COMMENTS | — | ✅ |
| 67 | PPEOCountry | COUNTRY | — | ✅ |
| 68 | PPEOCounty | COUNTY | — | ✅ |
| 69 | PPEOCreatedBy1 | CREATED_BY | — | ✅ |
| 70 | PPEOCreatedByModule | CREATED_BY_MODULE | — | ✅ |
| 71 | PPEOCreationDate1 | CREATION_DATE | — | ✅ |
| 72 | PPEOCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | ✅ |
| 73 | PPEODateOfBirth | DATE_OF_BIRTH | — | ✅ |
| 74 | PPEODunsNumberC | DUNS_NUMBER_C | — | ✅ |
| 75 | PPEOEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 76 | PPEOEmployeesTotal | EMPLOYEES_TOTAL | — | ✅ |
| 77 | PPEOFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | ✅ |
| 78 | PPEOGender | GENDER | — | ✅ |
| 79 | PPEOGroupType | GROUP_TYPE | — | ✅ |
| 80 | PPEOGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | ✅ |
| 81 | PPEOHomeCountry | HOME_COUNTRY | — | ✅ |
| 82 | PPEOHqBranchInd | HQ_BRANCH_IND | — | ✅ |
| 83 | PPEOIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | ✅ |
| 84 | PPEOIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | ✅ |
| 85 | PPEOInternalFlag | INTERNAL_FLAG | — | ✅ |
| 86 | PPEOJgzzFiscalCode | JGZZ_FISCAL_CODE | — | ✅ |
| 87 | PPEOLanguageName | LANGUAGE_NAME | — | ✅ |
| 88 | PPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 89 | PPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 90 | PPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 91 | PPEOMaritalStatus | MARITAL_STATUS | — | ✅ |
| 92 | PPEOMissionStatement | MISSION_STATEMENT | — | ✅ |
| 93 | PPEONextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | ✅ |
| 94 | PPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | ✅ |
| 95 | PPEOOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | ✅ |
| 96 | PPEOPartyId | PARTY_ID | — | ✅ |
| 97 | PPEOPartyName | PARTY_NAME | — | ✅ |
| 98 | PPEOPartyNumber | PARTY_NUMBER | — | ✅ |
| 99 | PPEOPartyType | PARTY_TYPE | — | ✅ |
| 100 | PPEOPartyUniqueName | PARTY_UNIQUE_NAME | — | ✅ |
| 101 | PPEOPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | ✅ |
| 102 | PPEOPersonFirstName | PERSON_FIRST_NAME | — | ✅ |
| 103 | PPEOPersonLastName | PERSON_LAST_NAME | — | ✅ |
| 104 | PPEOPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | ✅ |
| 105 | PPEOPersonMiddleName | PERSON_MIDDLE_NAME | — | ✅ |
| 106 | PPEOPersonNameSuffix | PERSON_NAME_SUFFIX | — | ✅ |
| 107 | PPEOPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | ✅ |
| 108 | PPEOPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | ✅ |
| 109 | PPEOPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | ✅ |
| 110 | PPEOPersonTitle | PERSON_TITLE | — | ✅ |
| 111 | PPEOPersonalAddressFlag | PERSONAL_ADDRESS_FLAG | — | ✅ |
| 112 | PPEOPersonalEmailFlag | PERSONAL_EMAIL_FLAG | — | ✅ |
| 113 | PPEOPersonalPhoneFlag | PERSONAL_PHONE_FLAG | — | ✅ |
| 114 | PPEOPostalCode | POSTAL_CODE | — | ✅ |
| 115 | PPEOPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | ✅ |
| 116 | PPEOPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | ✅ |
| 117 | PPEOPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | ✅ |
| 118 | PPEOPreferredName | PREFERRED_NAME | — | ✅ |
| 119 | PPEOPreferredNameId | PREFERRED_NAME_ID | — | ✅ |
| 120 | PPEOPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | ✅ |
| 121 | PPEOPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | ✅ |
| 122 | PPEOPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | ✅ |
| 123 | PPEOPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | ✅ |
| 124 | PPEOPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | ✅ |
| 125 | PPEOPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | ✅ |
| 126 | PPEOPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | ✅ |
| 127 | PPEOPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | ✅ |
| 128 | PPEOPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | ✅ |
| 129 | PPEOProvince | PROVINCE | — | ✅ |
| 130 | PPEORequestId | REQUEST_ID | — | ✅ |
| 131 | PPEOSalutation | SALUTATION | — | ✅ |
| 132 | PPEOSicCode | SIC_CODE | — | ✅ |
| 133 | PPEOSicCodeType | SIC_CODE_TYPE | — | ✅ |
| 134 | PPEOState | STATE | — | ✅ |
| 135 | PPEOStatus | STATUS | — | ✅ |
| 136 | PPEOThirdPartyFlag | THIRD_PARTY_FLAG | — | ✅ |
| 137 | PPEOTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | ✅ |
| 138 | PPEOUrl | URL | — | ✅ |
| 139 | PPEOUserGuid | USER_GUID | — | ✅ |
| 140 | PPEOValidatedFlag | VALIDATED_FLAG | — | ✅ |
| 141 | PPEOYearEstablished | YEAR_ESTABLISHED | — | ✅ |

### [[pon_supplier_activities|PON_SUPPLIER_ACTIVITIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 2 | AuctionHeaderIdOrigAmend | AUCTION_HEADER_ID_ORIG_AMEND | 🔑 | ✅ |
| 3 | BidNumber | BID_NUMBER | — | ✅ |
| 4 | BidStatus | BID_STATUS | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | LastActionFlag | LAST_ACTION_FLAG | — | ✅ |
| 8 | LastActivityCode | LAST_ACTIVITY_CODE | 🔑 | ✅ |
| 9 | LastActivityTime | LAST_ACTIVITY_TIME | 🔑 | ✅ |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | SessionId | SESSION_ID | 🔑 | ✅ |
| 15 | TradingPartnerContactId | TRADING_PARTNER_CONTACT_ID | 🔑 | ✅ |
| 16 | TradingPartnerId | TRADING_PARTNER_ID | 🔑 | ✅ |
| 17 | VendorSiteId | VENDOR_SITE_ID | — | ✅ |

### [[poz_suppliers_v|POZ_SUPPLIERS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SVEOAllowAwtFlag | ALLOW_AWT_FLAG | — | ✅ |
| 2 | SVEOAttribute101 | ATTRIBUTE10 | — | ✅ |
| 3 | SVEOAttribute110 | ATTRIBUTE1 | — | ✅ |
| 4 | SVEOAttribute111 | ATTRIBUTE11 | — | ✅ |
| 5 | SVEOAttribute121 | ATTRIBUTE12 | — | ✅ |
| 6 | SVEOAttribute131 | ATTRIBUTE13 | — | ✅ |
| 7 | SVEOAttribute141 | ATTRIBUTE14 | — | ✅ |
| 8 | SVEOAttribute151 | ATTRIBUTE15 | — | ✅ |
| 9 | SVEOAttribute161 | ATTRIBUTE16 | — | ✅ |
| 10 | SVEOAttribute171 | ATTRIBUTE17 | — | ✅ |
| 11 | SVEOAttribute181 | ATTRIBUTE18 | — | ✅ |
| 12 | SVEOAttribute191 | ATTRIBUTE19 | — | ✅ |
| 13 | SVEOAttribute201 | ATTRIBUTE20 | — | ✅ |
| 14 | SVEOAttribute210 | ATTRIBUTE2 | — | ✅ |
| 15 | SVEOAttribute31 | ATTRIBUTE3 | — | ✅ |
| 16 | SVEOAttribute41 | ATTRIBUTE4 | — | ✅ |
| 17 | SVEOAttribute51 | ATTRIBUTE5 | — | ✅ |
| 18 | SVEOAttribute61 | ATTRIBUTE6 | — | ✅ |
| 19 | SVEOAttribute71 | ATTRIBUTE7 | — | ✅ |
| 20 | SVEOAttribute81 | ATTRIBUTE8 | — | ✅ |
| 21 | SVEOAttribute91 | ATTRIBUTE9 | — | ✅ |
| 22 | SVEOAttributeCategory1 | ATTRIBUTE_CATEGORY | — | ✅ |
| 23 | SVEOAttributeDate101 | ATTRIBUTE_DATE10 | — | ✅ |
| 24 | SVEOAttributeDate13 | ATTRIBUTE_DATE1 | — | ✅ |
| 25 | SVEOAttributeDate21 | ATTRIBUTE_DATE2 | — | ✅ |
| 26 | SVEOAttributeDate31 | ATTRIBUTE_DATE3 | — | ✅ |
| 27 | SVEOAttributeDate41 | ATTRIBUTE_DATE4 | — | ✅ |
| 28 | SVEOAttributeDate51 | ATTRIBUTE_DATE5 | — | ✅ |
| 29 | SVEOAttributeDate61 | ATTRIBUTE_DATE6 | — | ✅ |
| 30 | SVEOAttributeDate71 | ATTRIBUTE_DATE7 | — | ✅ |
| 31 | SVEOAttributeDate81 | ATTRIBUTE_DATE8 | — | ✅ |
| 32 | SVEOAttributeDate91 | ATTRIBUTE_DATE9 | — | ✅ |
| 33 | SVEOAttributeNumber101 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 34 | SVEOAttributeNumber13 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 35 | SVEOAttributeNumber21 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 36 | SVEOAttributeNumber31 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 37 | SVEOAttributeNumber41 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 38 | SVEOAttributeNumber51 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 39 | SVEOAttributeNumber61 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 40 | SVEOAttributeNumber71 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 41 | SVEOAttributeNumber81 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 42 | SVEOAttributeNumber91 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 43 | SVEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 44 | SVEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | ✅ |
| 45 | SVEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 46 | SVEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 47 | SVEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 48 | SVEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 49 | SVEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | ✅ |
| 50 | SVEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | ✅ |
| 51 | SVEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | ✅ |
| 52 | SVEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | ✅ |
| 53 | SVEOAwtGroupId | AWT_GROUP_ID | — | ✅ |
| 54 | SVEOBankChargeBearer | BANK_CHARGE_BEARER | — | ✅ |
| 55 | SVEOBusinessRelationship | BUSINESS_RELATIONSHIP | — | ✅ |
| 56 | SVEOCorporateWebsite | CORPORATE_WEBSITE | — | ✅ |
| 57 | SVEOCreatedBy2 | CREATED_BY | — | ✅ |
| 58 | SVEOCreationDate2 | CREATION_DATE | — | ✅ |
| 59 | SVEOCustomerNum | CUSTOMER_NUM | — | ✅ |
| 60 | SVEODunsNumberC1 | DUNS_NUMBER_C | — | ✅ |
| 61 | SVEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 62 | SVEOFederalReportableFlag | FEDERAL_REPORTABLE_FLAG | — | ✅ |
| 63 | SVEOGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | ✅ |
| 64 | SVEOGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | ✅ |
| 65 | SVEOGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | ✅ |
| 66 | SVEOGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | ✅ |
| 67 | SVEOGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | ✅ |
| 68 | SVEOGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | ✅ |
| 69 | SVEOGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | ✅ |
| 70 | SVEOGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | ✅ |
| 71 | SVEOGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | ✅ |
| 72 | SVEOGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | ✅ |
| 73 | SVEOGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | ✅ |
| 74 | SVEOGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | ✅ |
| 75 | SVEOGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | ✅ |
| 76 | SVEOGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | ✅ |
| 77 | SVEOGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | ✅ |
| 78 | SVEOGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | ✅ |
| 79 | SVEOGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | ✅ |
| 80 | SVEOGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | ✅ |
| 81 | SVEOGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | ✅ |
| 82 | SVEOGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | ✅ |
| 83 | SVEOGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | ✅ |
| 84 | SVEOGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | ✅ |
| 85 | SVEOGlobalAttributeDate10 | GLOBAL_ATTRIBUTE_DATE10 | — | ✅ |
| 86 | SVEOGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | ✅ |
| 87 | SVEOGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | ✅ |
| 88 | SVEOGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | ✅ |
| 89 | SVEOGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | ✅ |
| 90 | SVEOGlobalAttributeDate6 | GLOBAL_ATTRIBUTE_DATE6 | — | ✅ |
| 91 | SVEOGlobalAttributeDate7 | GLOBAL_ATTRIBUTE_DATE7 | — | ✅ |
| 92 | SVEOGlobalAttributeDate8 | GLOBAL_ATTRIBUTE_DATE8 | — | ✅ |
| 93 | SVEOGlobalAttributeDate9 | GLOBAL_ATTRIBUTE_DATE9 | — | ✅ |
| 94 | SVEOGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | ✅ |
| 95 | SVEOGlobalAttributeNumber10 | GLOBAL_ATTRIBUTE_NUMBER10 | — | ✅ |
| 96 | SVEOGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | ✅ |
| 97 | SVEOGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | ✅ |
| 98 | SVEOGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | ✅ |
| 99 | SVEOGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | ✅ |
| 100 | SVEOGlobalAttributeNumber6 | GLOBAL_ATTRIBUTE_NUMBER6 | — | ✅ |
| 101 | SVEOGlobalAttributeNumber7 | GLOBAL_ATTRIBUTE_NUMBER7 | — | ✅ |
| 102 | SVEOGlobalAttributeNumber8 | GLOBAL_ATTRIBUTE_NUMBER8 | — | ✅ |
| 103 | SVEOGlobalAttributeNumber9 | GLOBAL_ATTRIBUTE_NUMBER9 | — | ✅ |
| 104 | SVEOGlobalAttributeTimestamp1 | GLOBAL_ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 105 | SVEOGlobalAttributeTimestamp10 | GLOBAL_ATTRIBUTE_TIMESTAMP10 | — | ✅ |
| 106 | SVEOGlobalAttributeTimestamp2 | GLOBAL_ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 107 | SVEOGlobalAttributeTimestamp3 | GLOBAL_ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 108 | SVEOGlobalAttributeTimestamp4 | GLOBAL_ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 109 | SVEOGlobalAttributeTimestamp5 | GLOBAL_ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 110 | SVEOGlobalAttributeTimestamp6 | GLOBAL_ATTRIBUTE_TIMESTAMP6 | — | ✅ |
| 111 | SVEOGlobalAttributeTimestamp7 | GLOBAL_ATTRIBUTE_TIMESTAMP7 | — | ✅ |
| 112 | SVEOGlobalAttributeTimestamp8 | GLOBAL_ATTRIBUTE_TIMESTAMP8 | — | ✅ |
| 113 | SVEOGlobalAttributeTimestamp9 | GLOBAL_ATTRIBUTE_TIMESTAMP9 | — | ✅ |
| 114 | SVEOLastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 115 | SVEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | ✅ |
| 116 | SVEOLastUpdatedBy2 | LAST_UPDATED_BY | — | ✅ |
| 117 | SVEOMinOrderAmount | MIN_ORDER_AMOUNT | — | ✅ |
| 118 | SVEOMinorityGroupLookupCode | MINORITY_GROUP_LOOKUP_CODE | — | ✅ |
| 119 | SVEONameControl | NAME_CONTROL | — | ✅ |
| 120 | SVEONiNumber | NI_NUMBER | — | ✅ |
| 121 | SVEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | ✅ |
| 122 | SVEOOneTimeFlag | ONE_TIME_FLAG | — | ✅ |
| 123 | SVEOOrganizationTypeLookupCode | ORGANIZATION_TYPE_LOOKUP_CODE | — | ✅ |
| 124 | SVEOParentPartyId | PARENT_PARTY_ID | — | ✅ |
| 125 | SVEOParentVendorId | PARENT_VENDOR_ID | — | ✅ |
| 126 | SVEOPartyId1 | PARTY_ID | — | ✅ |
| 127 | SVEOProgramApplicationId | PROGRAM_APPLICATION_ID | — | ✅ |
| 128 | SVEOProgramId | PROGRAM_ID | — | ✅ |
| 129 | SVEOProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 130 | SVEORequestId1 | REQUEST_ID | — | ✅ |
| 131 | SVEOSegment1 | SEGMENT1 | — | ✅ |
| 132 | SVEOSetOfBooksId | SET_OF_BOOKS_ID | — | ✅ |
| 133 | SVEOSmallBusinessFlag | SMALL_BUSINESS_FLAG | — | ✅ |
| 134 | SVEOSpendAuthReviewStatus | SPEND_AUTH_REVIEW_STATUS | — | ✅ |
| 135 | SVEOStandardIndustryClass | STANDARD_INDUSTRY_CLASS | — | ✅ |
| 136 | SVEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 137 | SVEOStateReportableFlag | STATE_REPORTABLE_FLAG | — | ✅ |
| 138 | SVEOSummaryFlag | SUMMARY_FLAG | — | ✅ |
| 139 | SVEOTaxReportingName | TAX_REPORTING_NAME | — | ✅ |
| 140 | SVEOTaxVerificationDate | TAX_VERIFICATION_DATE | — | ✅ |
| 141 | SVEOType1099 | TYPE_1099 | — | ✅ |
| 142 | SVEOVendorId | VENDOR_ID | — | ✅ |
| 143 | SVEOVendorName | VENDOR_NAME | — | ✅ |
| 144 | SVEOVendorNameAlt | VENDOR_NAME_ALT | — | ✅ |
| 145 | SVEOVendorTypeLookupCode | VENDOR_TYPE_LOOKUP_CODE | — | ✅ |
| 146 | SVEOWithholdingStartDate | WITHHOLDING_START_DATE | — | ✅ |
| 147 | SVEOWithholdingStatusLookupCode | WITHHOLDING_STATUS_LOOKUP_CODE | — | ✅ |
| 148 | SVEOWomenOwnedFlag | WOMEN_OWNED_FLAG | — | ✅ |

### [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SSDPEOAgingOnsetPoint | AGING_ONSET_POINT | — | ✅ |
| 2 | SSDPEOAgingPeriodDays | AGING_PERIOD_DAYS | — | ✅ |
| 3 | SSDPEOAllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | ✅ |
| 4 | SSDPEOAllowUnorderedReceiptsFlag | ALLOW_UNORDERED_RECEIPTS_FLAG | — | ✅ |
| 5 | SSDPEOAlwaysTakeDiscFlag | ALWAYS_TAKE_DISC_FLAG | — | ✅ |
| 6 | SSDPEOAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | ✅ |
| 7 | SSDPEOApTaxRoundingRule | AP_TAX_ROUNDING_RULE | — | ✅ |
| 8 | SSDPEOAreaCode | AREA_CODE | — | ✅ |
| 9 | SSDPEOAttentionArFlag | ATTENTION_AR_FLAG | — | ✅ |
| 10 | SSDPEOAttribute102 | ATTRIBUTE10 | — | ✅ |
| 11 | SSDPEOAttribute112 | ATTRIBUTE1 | — | ✅ |
| 12 | SSDPEOAttribute113 | ATTRIBUTE11 | — | ✅ |
| 13 | SSDPEOAttribute122 | ATTRIBUTE12 | — | ✅ |
| 14 | SSDPEOAttribute132 | ATTRIBUTE13 | — | ✅ |
| 15 | SSDPEOAttribute142 | ATTRIBUTE14 | — | ✅ |
| 16 | SSDPEOAttribute152 | ATTRIBUTE15 | — | ✅ |
| 17 | SSDPEOAttribute162 | ATTRIBUTE16 | — | ✅ |
| 18 | SSDPEOAttribute172 | ATTRIBUTE17 | — | ✅ |
| 19 | SSDPEOAttribute182 | ATTRIBUTE18 | — | ✅ |
| 20 | SSDPEOAttribute192 | ATTRIBUTE19 | — | ✅ |
| 21 | SSDPEOAttribute202 | ATTRIBUTE20 | — | ✅ |
| 22 | SSDPEOAttribute211 | ATTRIBUTE2 | — | ✅ |
| 23 | SSDPEOAttribute32 | ATTRIBUTE3 | — | ✅ |
| 24 | SSDPEOAttribute42 | ATTRIBUTE4 | — | ✅ |
| 25 | SSDPEOAttribute52 | ATTRIBUTE5 | — | ✅ |
| 26 | SSDPEOAttribute62 | ATTRIBUTE6 | — | ✅ |
| 27 | SSDPEOAttribute72 | ATTRIBUTE7 | — | ✅ |
| 28 | SSDPEOAttribute82 | ATTRIBUTE8 | — | ✅ |
| 29 | SSDPEOAttribute92 | ATTRIBUTE9 | — | ✅ |
| 30 | SSDPEOAttributeCategory2 | ATTRIBUTE_CATEGORY | — | ✅ |
| 31 | SSDPEOAttributeDate102 | ATTRIBUTE_DATE10 | — | ✅ |
| 32 | SSDPEOAttributeDate14 | ATTRIBUTE_DATE1 | — | ✅ |
| 33 | SSDPEOAttributeDate22 | ATTRIBUTE_DATE2 | — | ✅ |
| 34 | SSDPEOAttributeDate32 | ATTRIBUTE_DATE3 | — | ✅ |
| 35 | SSDPEOAttributeDate42 | ATTRIBUTE_DATE4 | — | ✅ |
| 36 | SSDPEOAttributeDate52 | ATTRIBUTE_DATE5 | — | ✅ |
| 37 | SSDPEOAttributeDate62 | ATTRIBUTE_DATE6 | — | ✅ |
| 38 | SSDPEOAttributeDate72 | ATTRIBUTE_DATE7 | — | ✅ |
| 39 | SSDPEOAttributeDate82 | ATTRIBUTE_DATE8 | — | ✅ |
| 40 | SSDPEOAttributeDate92 | ATTRIBUTE_DATE9 | — | ✅ |
| 41 | SSDPEOAttributeNumber102 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 42 | SSDPEOAttributeNumber14 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 43 | SSDPEOAttributeNumber22 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 44 | SSDPEOAttributeNumber32 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 45 | SSDPEOAttributeNumber42 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 46 | SSDPEOAttributeNumber52 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 47 | SSDPEOAttributeNumber62 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 48 | SSDPEOAttributeNumber72 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 49 | SSDPEOAttributeNumber82 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 50 | SSDPEOAttributeNumber92 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 51 | SSDPEOAttributeTimestamp101 | ATTRIBUTE_TIMESTAMP10 | — | ✅ |
| 52 | SSDPEOAttributeTimestamp11 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 53 | SSDPEOAttributeTimestamp21 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 54 | SSDPEOAttributeTimestamp31 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 55 | SSDPEOAttributeTimestamp41 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 56 | SSDPEOAttributeTimestamp51 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 57 | SSDPEOAttributeTimestamp61 | ATTRIBUTE_TIMESTAMP6 | — | ✅ |
| 58 | SSDPEOAttributeTimestamp71 | ATTRIBUTE_TIMESTAMP7 | — | ✅ |
| 59 | SSDPEOAttributeTimestamp81 | ATTRIBUTE_TIMESTAMP8 | — | ✅ |
| 60 | SSDPEOAttributeTimestamp91 | ATTRIBUTE_TIMESTAMP9 | — | ✅ |
| 61 | SSDPEOAutoCalculateInterestFlag | AUTO_CALCULATE_INTEREST_FLAG | — | ✅ |
| 62 | SSDPEOAutoTaxCalcFlag | AUTO_TAX_CALC_FLAG | — | ✅ |
| 63 | SSDPEOAutoTaxCalcOverride | AUTO_TAX_CALC_OVERRIDE | — | ✅ |
| 64 | SSDPEOB2bCommMethodCode | B2B_COMM_METHOD_CODE | — | ✅ |
| 65 | SSDPEOB2bSiteCode | B2B_SITE_CODE | — | ✅ |
| 66 | SSDPEOBankChargeBearer1 | BANK_CHARGE_BEARER | — | ✅ |
| 67 | SSDPEOBankChargeDeductionType | BANK_CHARGE_DEDUCTION_TYPE | — | ✅ |
| 68 | SSDPEOBuyerManagedTransportFlag | BUYER_MANAGED_TRANSPORT_FLAG | — | ✅ |
| 69 | SSDPEOCarrierId | CARRIER_ID | — | ✅ |
| 70 | SSDPEOConsumptionAdviceFrequency | CONSUMPTION_ADVICE_FREQUENCY | — | ✅ |
| 71 | SSDPEOConsumptionAdviceSummary | CONSUMPTION_ADVICE_SUMMARY | — | ✅ |
| 72 | SSDPEOCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | ✅ |
| 73 | SSDPEOCreateDebitMemoFlag | CREATE_DEBIT_MEMO_FLAG | — | ✅ |
| 74 | SSDPEOCreatedBy3 | CREATED_BY | — | ✅ |
| 75 | SSDPEOCreationDate3 | CREATION_DATE | — | ✅ |
| 76 | SSDPEOCustomerNum1 | CUSTOMER_NUM | — | ✅ |
| 77 | SSDPEODaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | ✅ |
| 78 | SSDPEODaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | ✅ |
| 79 | SSDPEODefaultPaySiteId | DEFAULT_PAY_SITE_ID | — | ✅ |
| 80 | SSDPEOEceTpLocationCode | ECE_TP_LOCATION_CODE | — | ✅ |
| 81 | SSDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 82 | SSDPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | ✅ |
| 83 | SSDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 84 | SSDPEOEmailAddress1 | EMAIL_ADDRESS | — | ✅ |
| 85 | SSDPEOEnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | ✅ |
| 86 | SSDPEOExcludeFreightFromDiscount | EXCLUDE_FREIGHT_FROM_DISCOUNT | — | ✅ |
| 87 | SSDPEOExcludeTaxFromDiscount | EXCLUDE_TAX_FROM_DISCOUNT | — | ✅ |
| 88 | SSDPEOFax | FAX | — | ✅ |
| 89 | SSDPEOFaxAreaCode | FAX_AREA_CODE | — | ✅ |
| 90 | SSDPEOFaxCountryCode | FAX_COUNTRY_CODE | — | ✅ |
| 91 | SSDPEOFobLookupCode | FOB_LOOKUP_CODE | — | ✅ |
| 92 | SSDPEOFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | ✅ |
| 93 | SSDPEOGaplessInvNumFlag | GAPLESS_INV_NUM_FLAG | — | ✅ |
| 94 | SSDPEOGlobalAttribute101 | GLOBAL_ATTRIBUTE10 | — | ✅ |
| 95 | SSDPEOGlobalAttribute110 | GLOBAL_ATTRIBUTE1 | — | ✅ |
| 96 | SSDPEOGlobalAttribute111 | GLOBAL_ATTRIBUTE11 | — | ✅ |
| 97 | SSDPEOGlobalAttribute121 | GLOBAL_ATTRIBUTE12 | — | ✅ |
| 98 | SSDPEOGlobalAttribute131 | GLOBAL_ATTRIBUTE13 | — | ✅ |
| 99 | SSDPEOGlobalAttribute141 | GLOBAL_ATTRIBUTE14 | — | ✅ |
| 100 | SSDPEOGlobalAttribute151 | GLOBAL_ATTRIBUTE15 | — | ✅ |
| 101 | SSDPEOGlobalAttribute161 | GLOBAL_ATTRIBUTE16 | — | ✅ |
| 102 | SSDPEOGlobalAttribute171 | GLOBAL_ATTRIBUTE17 | — | ✅ |
| 103 | SSDPEOGlobalAttribute181 | GLOBAL_ATTRIBUTE18 | — | ✅ |
| 104 | SSDPEOGlobalAttribute191 | GLOBAL_ATTRIBUTE19 | — | ✅ |
| 105 | SSDPEOGlobalAttribute201 | GLOBAL_ATTRIBUTE20 | — | ✅ |
| 106 | SSDPEOGlobalAttribute21 | GLOBAL_ATTRIBUTE2 | — | ✅ |
| 107 | SSDPEOGlobalAttribute31 | GLOBAL_ATTRIBUTE3 | — | ✅ |
| 108 | SSDPEOGlobalAttribute41 | GLOBAL_ATTRIBUTE4 | — | ✅ |
| 109 | SSDPEOGlobalAttribute51 | GLOBAL_ATTRIBUTE5 | — | ✅ |
| 110 | SSDPEOGlobalAttribute61 | GLOBAL_ATTRIBUTE6 | — | ✅ |
| 111 | SSDPEOGlobalAttribute71 | GLOBAL_ATTRIBUTE7 | — | ✅ |
| 112 | SSDPEOGlobalAttribute81 | GLOBAL_ATTRIBUTE8 | — | ✅ |
| 113 | SSDPEOGlobalAttribute91 | GLOBAL_ATTRIBUTE9 | — | ✅ |
| 114 | SSDPEOGlobalAttributeCategory1 | GLOBAL_ATTRIBUTE_CATEGORY | — | ✅ |
| 115 | SSDPEOGlobalAttributeDate101 | GLOBAL_ATTRIBUTE_DATE10 | — | ✅ |
| 116 | SSDPEOGlobalAttributeDate11 | GLOBAL_ATTRIBUTE_DATE1 | — | ✅ |
| 117 | SSDPEOGlobalAttributeDate21 | GLOBAL_ATTRIBUTE_DATE2 | — | ✅ |
| 118 | SSDPEOGlobalAttributeDate31 | GLOBAL_ATTRIBUTE_DATE3 | — | ✅ |
| 119 | SSDPEOGlobalAttributeDate41 | GLOBAL_ATTRIBUTE_DATE4 | — | ✅ |
| 120 | SSDPEOGlobalAttributeDate51 | GLOBAL_ATTRIBUTE_DATE5 | — | ✅ |
| 121 | SSDPEOGlobalAttributeDate61 | GLOBAL_ATTRIBUTE_DATE6 | — | ✅ |
| 122 | SSDPEOGlobalAttributeDate71 | GLOBAL_ATTRIBUTE_DATE7 | — | ✅ |
| 123 | SSDPEOGlobalAttributeDate81 | GLOBAL_ATTRIBUTE_DATE8 | — | ✅ |
| 124 | SSDPEOGlobalAttributeDate91 | GLOBAL_ATTRIBUTE_DATE9 | — | ✅ |
| 125 | SSDPEOGlobalAttributeNumber101 | GLOBAL_ATTRIBUTE_NUMBER10 | — | ✅ |
| 126 | SSDPEOGlobalAttributeNumber11 | GLOBAL_ATTRIBUTE_NUMBER1 | — | ✅ |
| 127 | SSDPEOGlobalAttributeNumber21 | GLOBAL_ATTRIBUTE_NUMBER2 | — | ✅ |
| 128 | SSDPEOGlobalAttributeNumber31 | GLOBAL_ATTRIBUTE_NUMBER3 | — | ✅ |
| 129 | SSDPEOGlobalAttributeNumber41 | GLOBAL_ATTRIBUTE_NUMBER4 | — | ✅ |
| 130 | SSDPEOGlobalAttributeNumber51 | GLOBAL_ATTRIBUTE_NUMBER5 | — | ✅ |
| 131 | SSDPEOGlobalAttributeNumber61 | GLOBAL_ATTRIBUTE_NUMBER6 | — | ✅ |
| 132 | SSDPEOGlobalAttributeNumber71 | GLOBAL_ATTRIBUTE_NUMBER7 | — | ✅ |
| 133 | SSDPEOGlobalAttributeNumber81 | GLOBAL_ATTRIBUTE_NUMBER8 | — | ✅ |
| 134 | SSDPEOGlobalAttributeNumber91 | GLOBAL_ATTRIBUTE_NUMBER9 | — | ✅ |
| 135 | SSDPEOGlobalAttributeTimestamp101 | GLOBAL_ATTRIBUTE_TIMESTAMP10 | — | ✅ |
| 136 | SSDPEOGlobalAttributeTimestamp11 | GLOBAL_ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 137 | SSDPEOGlobalAttributeTimestamp21 | GLOBAL_ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 138 | SSDPEOGlobalAttributeTimestamp31 | GLOBAL_ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 139 | SSDPEOGlobalAttributeTimestamp41 | GLOBAL_ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 140 | SSDPEOGlobalAttributeTimestamp51 | GLOBAL_ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 141 | SSDPEOGlobalAttributeTimestamp61 | GLOBAL_ATTRIBUTE_TIMESTAMP6 | — | ✅ |
| 142 | SSDPEOGlobalAttributeTimestamp71 | GLOBAL_ATTRIBUTE_TIMESTAMP7 | — | ✅ |
| 143 | SSDPEOGlobalAttributeTimestamp81 | GLOBAL_ATTRIBUTE_TIMESTAMP8 | — | ✅ |
| 144 | SSDPEOGlobalAttributeTimestamp91 | GLOBAL_ATTRIBUTE_TIMESTAMP9 | — | ✅ |
| 145 | SSDPEOHoldAllPaymentsFlag | HOLD_ALL_PAYMENTS_FLAG | — | ✅ |
| 146 | SSDPEOHoldBy | HOLD_BY | — | ✅ |
| 147 | SSDPEOHoldDate | HOLD_DATE | — | ✅ |
| 148 | SSDPEOHoldFlag | HOLD_FLAG | — | ✅ |
| 149 | SSDPEOHoldFuturePaymentsFlag | HOLD_FUTURE_PAYMENTS_FLAG | — | ✅ |
| 150 | SSDPEOHoldReason | HOLD_REASON | — | ✅ |
| 151 | SSDPEOHoldUnmatchedInvoicesFlag | HOLD_UNMATCHED_INVOICES_FLAG | — | ✅ |
| 152 | SSDPEOInactiveDate | INACTIVE_DATE | — | ✅ |
| 153 | SSDPEOInspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | ✅ |
| 154 | SSDPEOInvoiceAmountLimit | INVOICE_AMOUNT_LIMIT | — | ✅ |
| 155 | SSDPEOInvoiceChannel | INVOICE_CHANNEL | — | ✅ |
| 156 | SSDPEOInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 157 | SSDPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 158 | SSDPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 159 | SSDPEOLastUpdateDate3 | LAST_UPDATE_DATE | — | ✅ |
| 160 | SSDPEOLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | ✅ |
| 161 | SSDPEOLastUpdatedBy3 | LAST_UPDATED_BY | — | ✅ |
| 162 | SSDPEOLocationId | LOCATION_ID | — | ✅ |
| 163 | SSDPEOMatchOption | MATCH_OPTION | — | ✅ |
| 164 | SSDPEOModeOfTransport | MODE_OF_TRANSPORT | — | ✅ |
| 165 | SSDPEOObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | ✅ |
| 166 | SSDPEOOffsetTaxFlag | OFFSET_TAX_FLAG | — | ✅ |
| 167 | SSDPEOOffsetVatCode | OFFSET_VAT_CODE | — | ✅ |
| 168 | SSDPEOPartySiteId | PARTY_SITE_ID | — | ✅ |
| 169 | SSDPEOPayDateBasisLookupCode | PAY_DATE_BASIS_LOOKUP_CODE | — | ✅ |
| 170 | SSDPEOPayGroupLookupCode | PAY_GROUP_LOOKUP_CODE | — | ✅ |
| 171 | SSDPEOPayOnCode | PAY_ON_CODE | — | ✅ |
| 172 | SSDPEOPayOnReceiptSummaryCode | PAY_ON_RECEIPT_SUMMARY_CODE | — | ✅ |
| 173 | SSDPEOPayOnUseFlag | PAY_ON_USE_FLAG | — | ✅ |
| 174 | SSDPEOPaySiteFlag | PAY_SITE_FLAG | — | ✅ |
| 175 | SSDPEOPaymentCurrencyCode | PAYMENT_CURRENCY_CODE | — | ✅ |
| 176 | SSDPEOPaymentHoldDate | PAYMENT_HOLD_DATE | — | ✅ |
| 177 | SSDPEOPaymentPriority | PAYMENT_PRIORITY | — | ✅ |
| 178 | SSDPEOPcardSiteFlag | PCARD_SITE_FLAG | — | ✅ |
| 179 | SSDPEOPhone | PHONE | — | ✅ |
| 180 | SSDPEOPhoneCountryCode | PHONE_COUNTRY_CODE | — | ✅ |
| 181 | SSDPEOPhoneExtension | PHONE_EXTENSION | — | ✅ |
| 182 | SSDPEOPrcBuId | PRC_BU_ID | — | ✅ |
| 183 | SSDPEOPrimaryPaySiteFlag | PRIMARY_PAY_SITE_FLAG | — | ✅ |
| 184 | SSDPEOProgramApplicationId1 | PROGRAM_APPLICATION_ID | — | ✅ |
| 185 | SSDPEOProgramId1 | PROGRAM_ID | — | ✅ |
| 186 | SSDPEOProgramUpdateDate1 | PROGRAM_UPDATE_DATE | — | ✅ |
| 187 | SSDPEOPurchasingHoldReason | PURCHASING_HOLD_REASON | — | ✅ |
| 188 | SSDPEOPurchasingSiteFlag | PURCHASING_SITE_FLAG | — | ✅ |
| 189 | SSDPEOQtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | ✅ |
| 190 | SSDPEOQtyRcvTolerance | QTY_RCV_TOLERANCE | — | ✅ |
| 191 | SSDPEOReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | ✅ |
| 192 | SSDPEOReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | ✅ |
| 193 | SSDPEOReceivingRoutingId | RECEIVING_ROUTING_ID | — | ✅ |
| 194 | SSDPEORequestId2 | REQUEST_ID | — | ✅ |
| 195 | SSDPEORetainageRate | RETAINAGE_RATE | — | ✅ |
| 196 | SSDPEORfqOnlySiteFlag | RFQ_ONLY_SITE_FLAG | — | ✅ |
| 197 | SSDPEOSellingCompanyIdentifier | SELLING_COMPANY_IDENTIFIER | — | ✅ |
| 198 | SSDPEOServiceLevel | SERVICE_LEVEL | — | ✅ |
| 199 | SSDPEOServicesToleranceId | SERVICES_TOLERANCE_ID | — | ✅ |
| 200 | SSDPEOShipViaLookupCode | SHIP_VIA_LOOKUP_CODE | — | ✅ |
| 201 | SSDPEOShippingControl | SHIPPING_CONTROL | — | ✅ |
| 202 | SSDPEOShippingNetworkLocation | SHIPPING_NETWORK_LOCATION | — | ✅ |
| 203 | SSDPEOSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | ✅ |
| 204 | SSDPEOTaxCountryCode | TAX_COUNTRY_CODE | — | ✅ |
| 205 | SSDPEOTaxReportingSiteFlag | TAX_REPORTING_SITE_FLAG | — | ✅ |
| 206 | SSDPEOTelex | TELEX | — | ✅ |
| 207 | SSDPEOTermsDateBasis | TERMS_DATE_BASIS | — | ✅ |
| 208 | SSDPEOTermsId | TERMS_ID | — | ✅ |
| 209 | SSDPEOToleranceId | TOLERANCE_ID | — | ✅ |
| 210 | SSDPEOTpHeaderId | TP_HEADER_ID | — | ✅ |
| 211 | SSDPEOVatCode | VAT_CODE | — | ✅ |
| 212 | SSDPEOVatRegistrationNum | VAT_REGISTRATION_NUM | — | ✅ |
| 213 | SSDPEOVendorId1 | VENDOR_ID | — | ✅ |
| 214 | SSDPEOVendorSiteCode | VENDOR_SITE_CODE | — | ✅ |
| 215 | SSDPEOVendorSiteCodeAlt | VENDOR_SITE_CODE_ALT | — | ✅ |
| 216 | SSDPEOVendorSiteId1 | VENDOR_SITE_ID | — | ✅ |
| 217 | SSDPEOVendorSiteSpkId | VENDOR_SITE_SPK_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
