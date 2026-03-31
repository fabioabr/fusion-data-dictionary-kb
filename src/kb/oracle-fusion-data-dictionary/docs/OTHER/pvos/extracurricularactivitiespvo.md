---
id: DOC-OTHER-PVO-ExtracurricularActivitiesPVO
doc_type: system-doc
title: "ExtracurricularActivitiesPVO — PVO Cross-Module"
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
  - ExtracurricularActivitiesPVO
  - extracurricularactivitiespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExtracurricularActivitiesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Extracurricular Activities. Acessa as tabelas: HEY_EXTRACURRICULAR_TXNS, HEY_EXTRACURRICULAR_TXN_SRCS, HZ_PARTIES.

**Caminho:** `FscmTopModelAM.HedHeyStdExtAcademicInfoAM.ExtracurricularActivitiesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 288 | 3 | 1 | 23 | 8% |

---

## 🔗 Tabelas Relacionadas

- [[hey_extracurricular_txns|HEY_EXTRACURRICULAR_TXNS]] — 85 atributos (1 PKs, 20 BICC)
- [[hey_extracurricular_txn_srcs|HEY_EXTRACURRICULAR_TXN_SRCS]] — 62 atributos (2 BICC)
- [[hz_parties|HZ_PARTIES]] — 141 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hey_extracurricular_txns|HEY_EXTRACURRICULAR_TXNS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExtracurricularTxnsPEOAcademicLevelCode | ACADEMIC_LEVEL_CODE | — | ✅ |
| 2 | ExtracurricularTxnsPEOActivityDescription | ACTIVITY_DESCRIPTION | — | ✅ |
| 3 | ExtracurricularTxnsPEOActivityTypeCode | ACTIVITY_TYPE_CODE | — | ✅ |
| 4 | ExtracurricularTxnsPEOAttribute1 | ATTRIBUTE1 | — | — |
| 5 | ExtracurricularTxnsPEOAttribute10 | ATTRIBUTE10 | — | — |
| 6 | ExtracurricularTxnsPEOAttribute11 | ATTRIBUTE11 | — | — |
| 7 | ExtracurricularTxnsPEOAttribute12 | ATTRIBUTE12 | — | — |
| 8 | ExtracurricularTxnsPEOAttribute13 | ATTRIBUTE13 | — | — |
| 9 | ExtracurricularTxnsPEOAttribute14 | ATTRIBUTE14 | — | — |
| 10 | ExtracurricularTxnsPEOAttribute15 | ATTRIBUTE15 | — | — |
| 11 | ExtracurricularTxnsPEOAttribute16 | ATTRIBUTE16 | — | — |
| 12 | ExtracurricularTxnsPEOAttribute17 | ATTRIBUTE17 | — | — |
| 13 | ExtracurricularTxnsPEOAttribute18 | ATTRIBUTE18 | — | — |
| 14 | ExtracurricularTxnsPEOAttribute19 | ATTRIBUTE19 | — | — |
| 15 | ExtracurricularTxnsPEOAttribute2 | ATTRIBUTE2 | — | — |
| 16 | ExtracurricularTxnsPEOAttribute20 | ATTRIBUTE20 | — | — |
| 17 | ExtracurricularTxnsPEOAttribute3 | ATTRIBUTE3 | — | — |
| 18 | ExtracurricularTxnsPEOAttribute4 | ATTRIBUTE4 | — | — |
| 19 | ExtracurricularTxnsPEOAttribute5 | ATTRIBUTE5 | — | — |
| 20 | ExtracurricularTxnsPEOAttribute6 | ATTRIBUTE6 | — | — |
| 21 | ExtracurricularTxnsPEOAttribute7 | ATTRIBUTE7 | — | — |
| 22 | ExtracurricularTxnsPEOAttribute8 | ATTRIBUTE8 | — | — |
| 23 | ExtracurricularTxnsPEOAttribute9 | ATTRIBUTE9 | — | — |
| 24 | ExtracurricularTxnsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 25 | ExtracurricularTxnsPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 26 | ExtracurricularTxnsPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 27 | ExtracurricularTxnsPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 28 | ExtracurricularTxnsPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 29 | ExtracurricularTxnsPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 30 | ExtracurricularTxnsPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 31 | ExtracurricularTxnsPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 32 | ExtracurricularTxnsPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 33 | ExtracurricularTxnsPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 34 | ExtracurricularTxnsPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 35 | ExtracurricularTxnsPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 36 | ExtracurricularTxnsPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 37 | ExtracurricularTxnsPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 38 | ExtracurricularTxnsPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 39 | ExtracurricularTxnsPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 40 | ExtracurricularTxnsPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 41 | ExtracurricularTxnsPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 42 | ExtracurricularTxnsPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 43 | ExtracurricularTxnsPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 44 | ExtracurricularTxnsPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 45 | ExtracurricularTxnsPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 46 | ExtracurricularTxnsPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 47 | ExtracurricularTxnsPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 48 | ExtracurricularTxnsPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 49 | ExtracurricularTxnsPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 50 | ExtracurricularTxnsPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 51 | ExtracurricularTxnsPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 52 | ExtracurricularTxnsPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 53 | ExtracurricularTxnsPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 54 | ExtracurricularTxnsPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 55 | ExtracurricularTxnsPEOContactAddress | CONTACT_ADDRESS | — | ✅ |
| 56 | ExtracurricularTxnsPEOContactEmailAddress | CONTACT_EMAIL_ADDRESS | — | ✅ |
| 57 | ExtracurricularTxnsPEOContactFirstName | CONTACT_FIRST_NAME | — | ✅ |
| 58 | ExtracurricularTxnsPEOContactLastName | CONTACT_LAST_NAME | — | ✅ |
| 59 | ExtracurricularTxnsPEOContactNameTitle | CONTACT_NAME_TITLE | — | ✅ |
| 60 | ExtracurricularTxnsPEOCorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 61 | ExtracurricularTxnsPEOCreatedBy | CREATED_BY | — | — |
| 62 | ExtracurricularTxnsPEOCreationDate | CREATION_DATE | — | — |
| 63 | ExtracurricularTxnsPEOCurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 64 | ExtracurricularTxnsPEOCurrencyCode | CURRENCY_CODE | — | — |
| 65 | ExtracurricularTxnsPEOEndDate | END_DATE | — | ✅ |
| 66 | ExtracurricularTxnsPEOExtracurricularTxnId | EXTRACURRICULAR_TXN_ID | 🔑 | ✅ |
| 67 | ExtracurricularTxnsPEOHoursPerWeek | HOURS_PER_WEEK | — | ✅ |
| 68 | ExtracurricularTxnsPEOInterestedInPursuingCode | INTERESTED_IN_PURSUING_CODE | — | ✅ |
| 69 | ExtracurricularTxnsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 70 | ExtracurricularTxnsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 71 | ExtracurricularTxnsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 72 | ExtracurricularTxnsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 73 | ExtracurricularTxnsPEOOrganizationOtherName | ORGANIZATION_OTHER_NAME | — | ✅ |
| 74 | ExtracurricularTxnsPEOOrganizationOtherNameFlag | ORGANIZATION_OTHER_NAME_FLAG | — | — |
| 75 | ExtracurricularTxnsPEOOrganizationPartyId | ORGANIZATION_PARTY_ID | — | — |
| 76 | ExtracurricularTxnsPEOParentId | PARENT_ID | — | — |
| 77 | ExtracurricularTxnsPEOPartyId | PARTY_ID | — | — |
| 78 | ExtracurricularTxnsPEOPhoneAreaCode | PHONE_AREA_CODE | — | ✅ |
| 79 | ExtracurricularTxnsPEOPhoneCountryCode | PHONE_COUNTRY_CODE | — | ✅ |
| 80 | ExtracurricularTxnsPEOPhoneNumber | PHONE_NUMBER | — | ✅ |
| 81 | ExtracurricularTxnsPEOPositionHeld | POSITION_HELD | — | ✅ |
| 82 | ExtracurricularTxnsPEOStartDate | START_DATE | — | ✅ |
| 83 | ExtracurricularTxnsPEOWeeksPerYear | WEEKS_PER_YEAR | — | ✅ |
| 84 | ExtracurricularTxnsPEO_AliasExtracurricularTxnId | EXTRACURRICULAR_TXN_ID | — | — |
| 85 | ExtracurricularTxnsPEO_AliasParentId | PARENT_ID | — | — |

### [[hey_extracurricular_txn_srcs|HEY_EXTRACURRICULAR_TXN_SRCS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExtracurricularTxnSrcsPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | ExtracurricularTxnSrcsPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | ExtracurricularTxnSrcsPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | ExtracurricularTxnSrcsPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | ExtracurricularTxnSrcsPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | ExtracurricularTxnSrcsPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | ExtracurricularTxnSrcsPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | ExtracurricularTxnSrcsPEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | ExtracurricularTxnSrcsPEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | ExtracurricularTxnSrcsPEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | ExtracurricularTxnSrcsPEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | ExtracurricularTxnSrcsPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | ExtracurricularTxnSrcsPEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | ExtracurricularTxnSrcsPEOAttribute3 | ATTRIBUTE3 | — | — |
| 15 | ExtracurricularTxnSrcsPEOAttribute4 | ATTRIBUTE4 | — | — |
| 16 | ExtracurricularTxnSrcsPEOAttribute5 | ATTRIBUTE5 | — | — |
| 17 | ExtracurricularTxnSrcsPEOAttribute6 | ATTRIBUTE6 | — | — |
| 18 | ExtracurricularTxnSrcsPEOAttribute7 | ATTRIBUTE7 | — | — |
| 19 | ExtracurricularTxnSrcsPEOAttribute8 | ATTRIBUTE8 | — | — |
| 20 | ExtracurricularTxnSrcsPEOAttribute9 | ATTRIBUTE9 | — | — |
| 21 | ExtracurricularTxnSrcsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | ExtracurricularTxnSrcsPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | ExtracurricularTxnSrcsPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 24 | ExtracurricularTxnSrcsPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | ExtracurricularTxnSrcsPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | ExtracurricularTxnSrcsPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | ExtracurricularTxnSrcsPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | ExtracurricularTxnSrcsPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 29 | ExtracurricularTxnSrcsPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 30 | ExtracurricularTxnSrcsPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 31 | ExtracurricularTxnSrcsPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 32 | ExtracurricularTxnSrcsPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 33 | ExtracurricularTxnSrcsPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 34 | ExtracurricularTxnSrcsPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 35 | ExtracurricularTxnSrcsPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 36 | ExtracurricularTxnSrcsPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 37 | ExtracurricularTxnSrcsPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 38 | ExtracurricularTxnSrcsPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 39 | ExtracurricularTxnSrcsPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 40 | ExtracurricularTxnSrcsPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 41 | ExtracurricularTxnSrcsPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 42 | ExtracurricularTxnSrcsPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 43 | ExtracurricularTxnSrcsPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 44 | ExtracurricularTxnSrcsPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 45 | ExtracurricularTxnSrcsPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 46 | ExtracurricularTxnSrcsPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 47 | ExtracurricularTxnSrcsPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 48 | ExtracurricularTxnSrcsPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 49 | ExtracurricularTxnSrcsPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 50 | ExtracurricularTxnSrcsPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 51 | ExtracurricularTxnSrcsPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 52 | ExtracurricularTxnSrcsPEOCreatedBy | CREATED_BY | — | — |
| 53 | ExtracurricularTxnSrcsPEOCreationDate | CREATION_DATE | — | — |
| 54 | ExtracurricularTxnSrcsPEOExtracurricularTxnId | EXTRACURRICULAR_TXN_ID | — | — |
| 55 | ExtracurricularTxnSrcsPEOExtracurricularTxnSrcId | EXTRACURRICULAR_TXN_SRC_ID | — | — |
| 56 | ExtracurricularTxnSrcsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 57 | ExtracurricularTxnSrcsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 58 | ExtracurricularTxnSrcsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 59 | ExtracurricularTxnSrcsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 60 | ExtracurricularTxnSrcsPEOOriginSystemCode | ORIGIN_SYSTEM_CODE | — | — |
| 61 | ExtracurricularTxnSrcsPEOOriginSystemReference | ORIGIN_SYSTEM_REFERENCE | — | — |
| 62 | ExtracurricularTxnSrcsPEOStatusCode | STATUS_CODE | — | ✅ |

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
| 96 | PartyPEOPartyId | PARTY_ID | — | — |
| 97 | PartyPEOPartyName | PARTY_NAME | — | — |
| 98 | PartyPEOPartyNumber | PARTY_NUMBER | — | — |
| 99 | PartyPEOPartyType | PARTY_TYPE | — | — |
| 100 | PartyPEOPartyUniqueName | PARTY_UNIQUE_NAME | — | — |
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
