---
id: DOC-OTHER-PVO-ExternalOrganizationPVO
doc_type: system-doc
title: "ExternalOrganizationPVO — PVO Cross-Module"
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
  - ExternalOrganizationPVO
  - externalorganizationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExternalOrganizationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de External Organization. Acessa as tabelas: HEY_ORGANIZATION, HZ_PARTIES.

**Caminho:** `FscmTopModelAM.HedHeyOrganizationInfoAM.ExternalOrganizationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 201 | 2 | 1 | 7 | 3% |

---

## 🔗 Tabelas Relacionadas

- [[hey_organization|HEY_ORGANIZATION]] — 60 atributos (1 PKs, 3 BICC)
- [[hz_parties|HZ_PARTIES]] — 141 atributos (4 BICC)

---

## ⚙️ Atributos

### [[hey_organization|HEY_ORGANIZATION]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | OrganizationPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | OrganizationPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | OrganizationPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | OrganizationPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | OrganizationPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | OrganizationPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | OrganizationPEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | OrganizationPEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | OrganizationPEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | OrganizationPEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | OrganizationPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | OrganizationPEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | OrganizationPEOAttribute3 | ATTRIBUTE3 | — | — |
| 15 | OrganizationPEOAttribute4 | ATTRIBUTE4 | — | — |
| 16 | OrganizationPEOAttribute5 | ATTRIBUTE5 | — | — |
| 17 | OrganizationPEOAttribute6 | ATTRIBUTE6 | — | — |
| 18 | OrganizationPEOAttribute7 | ATTRIBUTE7 | — | — |
| 19 | OrganizationPEOAttribute8 | ATTRIBUTE8 | — | — |
| 20 | OrganizationPEOAttribute9 | ATTRIBUTE9 | — | — |
| 21 | OrganizationPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | OrganizationPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | OrganizationPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 24 | OrganizationPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | OrganizationPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | OrganizationPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | OrganizationPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | OrganizationPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 29 | OrganizationPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 30 | OrganizationPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 31 | OrganizationPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 32 | OrganizationPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 33 | OrganizationPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 34 | OrganizationPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 35 | OrganizationPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 36 | OrganizationPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 37 | OrganizationPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 38 | OrganizationPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 39 | OrganizationPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 40 | OrganizationPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 41 | OrganizationPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 42 | OrganizationPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 43 | OrganizationPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 44 | OrganizationPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 45 | OrganizationPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 46 | OrganizationPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 47 | OrganizationPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 48 | OrganizationPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 49 | OrganizationPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 50 | OrganizationPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 51 | OrganizationPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 52 | OrganizationPEOCreatedBy | CREATED_BY | — | — |
| 53 | OrganizationPEOCreationDate | CREATION_DATE | — | — |
| 54 | OrganizationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 55 | OrganizationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 56 | OrganizationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 57 | OrganizationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 58 | OrganizationPEOOrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 59 | OrganizationPEOOrganizationTypeCode | ORGANIZATION_TYPE_CODE | — | ✅ |
| 60 | OrganizationPEOPartyId | PARTY_ID | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyPEOAddress1 | ADDRESS1 | — | — |
| 2 | PartyPEOAddress2 | ADDRESS2 | — | — |
| 3 | PartyPEOAddress3 | ADDRESS3 | — | — |
| 4 | PartyPEOAddress4 | ADDRESS4 | — | — |
| 5 | PartyPEOAnalysisFy | ANALYSIS_FY | — | — |
| 6 | PartyPEOAttribute1 | ATTRIBUTE1 | — | — |
| 7 | PartyPEOAttribute10 | ATTRIBUTE10 | — | — |
| 8 | PartyPEOAttribute11 | ATTRIBUTE11 | — | — |
| 9 | PartyPEOAttribute12 | ATTRIBUTE12 | — | — |
| 10 | PartyPEOAttribute13 | ATTRIBUTE13 | — | — |
| 11 | PartyPEOAttribute14 | ATTRIBUTE14 | — | — |
| 12 | PartyPEOAttribute15 | ATTRIBUTE15 | — | — |
| 13 | PartyPEOAttribute16 | ATTRIBUTE16 | — | — |
| 14 | PartyPEOAttribute17 | ATTRIBUTE17 | — | — |
| 15 | PartyPEOAttribute18 | ATTRIBUTE18 | — | — |
| 16 | PartyPEOAttribute19 | ATTRIBUTE19 | — | — |
| 17 | PartyPEOAttribute2 | ATTRIBUTE2 | — | — |
| 18 | PartyPEOAttribute20 | ATTRIBUTE20 | — | — |
| 19 | PartyPEOAttribute21 | ATTRIBUTE21 | — | — |
| 20 | PartyPEOAttribute22 | ATTRIBUTE22 | — | — |
| 21 | PartyPEOAttribute23 | ATTRIBUTE23 | — | — |
| 22 | PartyPEOAttribute24 | ATTRIBUTE24 | — | — |
| 23 | PartyPEOAttribute25 | ATTRIBUTE25 | — | — |
| 24 | PartyPEOAttribute26 | ATTRIBUTE26 | — | — |
| 25 | PartyPEOAttribute27 | ATTRIBUTE27 | — | — |
| 26 | PartyPEOAttribute28 | ATTRIBUTE28 | — | — |
| 27 | PartyPEOAttribute29 | ATTRIBUTE29 | — | — |
| 28 | PartyPEOAttribute3 | ATTRIBUTE3 | — | — |
| 29 | PartyPEOAttribute30 | ATTRIBUTE30 | — | — |
| 30 | PartyPEOAttribute4 | ATTRIBUTE4 | — | — |
| 31 | PartyPEOAttribute5 | ATTRIBUTE5 | — | — |
| 32 | PartyPEOAttribute6 | ATTRIBUTE6 | — | — |
| 33 | PartyPEOAttribute7 | ATTRIBUTE7 | — | — |
| 34 | PartyPEOAttribute8 | ATTRIBUTE8 | — | — |
| 35 | PartyPEOAttribute9 | ATTRIBUTE9 | — | — |
| 36 | PartyPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 37 | PartyPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 38 | PartyPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 39 | PartyPEOAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 40 | PartyPEOAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 41 | PartyPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 42 | PartyPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 43 | PartyPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 44 | PartyPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 45 | PartyPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 46 | PartyPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 47 | PartyPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 48 | PartyPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 49 | PartyPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 50 | PartyPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 51 | PartyPEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 52 | PartyPEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 53 | PartyPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 54 | PartyPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 55 | PartyPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 56 | PartyPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 57 | PartyPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 58 | PartyPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 59 | PartyPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 60 | PartyPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 61 | PartyPEOCategoryCode | CATEGORY_CODE | — | — |
| 62 | PartyPEOCeoName | CEO_NAME | — | — |
| 63 | PartyPEOCertReasonCode | CERT_REASON_CODE | — | — |
| 64 | PartyPEOCertificationLevel | CERTIFICATION_LEVEL | — | — |
| 65 | PartyPEOCity | CITY | — | — |
| 66 | PartyPEOComments | COMMENTS | — | — |
| 67 | PartyPEOCountry | COUNTRY | — | — |
| 68 | PartyPEOCounty | COUNTY | — | — |
| 69 | PartyPEOCreatedBy | CREATED_BY | — | — |
| 70 | PartyPEOCreatedByModule | CREATED_BY_MODULE | — | — |
| 71 | PartyPEOCreationDate | CREATION_DATE | — | — |
| 72 | PartyPEOCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 73 | PartyPEODateOfBirth | DATE_OF_BIRTH | — | — |
| 74 | PartyPEODunsNumberC | DUNS_NUMBER_C | — | — |
| 75 | PartyPEOEmailAddress | EMAIL_ADDRESS | — | — |
| 76 | PartyPEOEmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 77 | PartyPEOFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 78 | PartyPEOGender | GENDER | — | — |
| 79 | PartyPEOGroupType | GROUP_TYPE | — | — |
| 80 | PartyPEOGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | — |
| 81 | PartyPEOHomeCountry | HOME_COUNTRY | — | — |
| 82 | PartyPEOHqBranchInd | HQ_BRANCH_IND | — | — |
| 83 | PartyPEOIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 84 | PartyPEOIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | — |
| 85 | PartyPEOInternalFlag | INTERNAL_FLAG | — | — |
| 86 | PartyPEOJgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 87 | PartyPEOLanguageName | LANGUAGE_NAME | — | — |
| 88 | PartyPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 89 | PartyPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 90 | PartyPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 91 | PartyPEOMaritalStatus | MARITAL_STATUS | — | — |
| 92 | PartyPEOMissionStatement | MISSION_STATEMENT | — | — |
| 93 | PartyPEONextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 94 | PartyPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 95 | PartyPEOOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 96 | PartyPEOPartyId | PARTY_ID | — | ✅ |
| 97 | PartyPEOPartyName | PARTY_NAME | — | ✅ |
| 98 | PartyPEOPartyNumber | PARTY_NUMBER | — | — |
| 99 | PartyPEOPartyType | PARTY_TYPE | — | — |
| 100 | PartyPEOPartyUniqueName | PARTY_UNIQUE_NAME | — | ✅ |
| 101 | PartyPEOPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 102 | PartyPEOPersonFirstName | PERSON_FIRST_NAME | — | — |
| 103 | PartyPEOPersonLastName | PERSON_LAST_NAME | — | — |
| 104 | PartyPEOPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 105 | PartyPEOPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 106 | PartyPEOPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 107 | PartyPEOPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 108 | PartyPEOPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 109 | PartyPEOPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 110 | PartyPEOPersonTitle | PERSON_TITLE | — | — |
| 111 | PartyPEOPersonalAddressFlag | PERSONAL_ADDRESS_FLAG | — | — |
| 112 | PartyPEOPersonalEmailFlag | PERSONAL_EMAIL_FLAG | — | — |
| 113 | PartyPEOPersonalPhoneFlag | PERSONAL_PHONE_FLAG | — | — |
| 114 | PartyPEOPostalCode | POSTAL_CODE | — | — |
| 115 | PartyPEOPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 116 | PartyPEOPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 117 | PartyPEOPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 118 | PartyPEOPreferredName | PREFERRED_NAME | — | — |
| 119 | PartyPEOPreferredNameId | PREFERRED_NAME_ID | — | — |
| 120 | PartyPEOPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | — |
| 121 | PartyPEOPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 122 | PartyPEOPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 123 | PartyPEOPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 124 | PartyPEOPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 125 | PartyPEOPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 126 | PartyPEOPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | — |
| 127 | PartyPEOPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 128 | PartyPEOPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 129 | PartyPEOProvince | PROVINCE | — | — |
| 130 | PartyPEORequestId | REQUEST_ID | — | — |
| 131 | PartyPEOSalutation | SALUTATION | — | — |
| 132 | PartyPEOSicCode | SIC_CODE | — | — |
| 133 | PartyPEOSicCodeType | SIC_CODE_TYPE | — | — |
| 134 | PartyPEOState | STATE | — | — |
| 135 | PartyPEOStatus | STATUS | — | — |
| 136 | PartyPEOThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 137 | PartyPEOTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 138 | PartyPEOUrl | URL | — | — |
| 139 | PartyPEOUserGuid | USER_GUID | — | — |
| 140 | PartyPEOValidatedFlag | VALIDATED_FLAG | — | — |
| 141 | PartyPEOYearEstablished | YEAR_ESTABLISHED | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
