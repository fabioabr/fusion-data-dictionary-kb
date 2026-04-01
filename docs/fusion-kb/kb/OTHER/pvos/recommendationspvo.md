---
id: DOC-OTHER-PVO-RecommendationsPVO
doc_type: system-doc
title: "RecommendationsPVO — PVO Cross-Module"
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
  - RecommendationsPVO
  - recommendationspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RecommendationsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Recommendations. Acessa as tabelas: HEY_RECOMMENDATION_TXNS, HEY_RECOMMENDATION_TXN_SOURCES, HZ_PARTIES.

**Caminho:** `FscmTopModelAM.HedHeyStdExtAcademicInfoAM.RecommendationsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 281 | 3 | 1 | 19 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[hey_recommendation_txns|HEY_RECOMMENDATION_TXNS]] — 83 atributos (1 PKs, 16 BICC)
- [[hey_recommendation_txn_sources|HEY_RECOMMENDATION_TXN_SOURCES]] — 57 atributos (2 BICC)
- [[hz_parties|HZ_PARTIES]] — 141 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hey_recommendation_txns|HEY_RECOMMENDATION_TXNS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RecommendationTxnsPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | RecommendationTxnsPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | RecommendationTxnsPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | RecommendationTxnsPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | RecommendationTxnsPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | RecommendationTxnsPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | RecommendationTxnsPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | RecommendationTxnsPEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | RecommendationTxnsPEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | RecommendationTxnsPEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | RecommendationTxnsPEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | RecommendationTxnsPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | RecommendationTxnsPEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | RecommendationTxnsPEOAttribute3 | ATTRIBUTE3 | — | — |
| 15 | RecommendationTxnsPEOAttribute4 | ATTRIBUTE4 | — | — |
| 16 | RecommendationTxnsPEOAttribute5 | ATTRIBUTE5 | — | — |
| 17 | RecommendationTxnsPEOAttribute6 | ATTRIBUTE6 | — | — |
| 18 | RecommendationTxnsPEOAttribute7 | ATTRIBUTE7 | — | — |
| 19 | RecommendationTxnsPEOAttribute8 | ATTRIBUTE8 | — | — |
| 20 | RecommendationTxnsPEOAttribute9 | ATTRIBUTE9 | — | — |
| 21 | RecommendationTxnsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | RecommendationTxnsPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | RecommendationTxnsPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 24 | RecommendationTxnsPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | RecommendationTxnsPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | RecommendationTxnsPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | RecommendationTxnsPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | RecommendationTxnsPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 29 | RecommendationTxnsPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 30 | RecommendationTxnsPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 31 | RecommendationTxnsPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 32 | RecommendationTxnsPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 33 | RecommendationTxnsPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 34 | RecommendationTxnsPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 35 | RecommendationTxnsPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 36 | RecommendationTxnsPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 37 | RecommendationTxnsPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 38 | RecommendationTxnsPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 39 | RecommendationTxnsPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 40 | RecommendationTxnsPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 41 | RecommendationTxnsPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 42 | RecommendationTxnsPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 43 | RecommendationTxnsPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 44 | RecommendationTxnsPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 45 | RecommendationTxnsPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 46 | RecommendationTxnsPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 47 | RecommendationTxnsPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 48 | RecommendationTxnsPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 49 | RecommendationTxnsPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 50 | RecommendationTxnsPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 51 | RecommendationTxnsPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 52 | RecommendationTxnsPEOCorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 53 | RecommendationTxnsPEOCreatedBy | CREATED_BY | — | — |
| 54 | RecommendationTxnsPEOCreationDate | CREATION_DATE | — | — |
| 55 | RecommendationTxnsPEOCurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 56 | RecommendationTxnsPEOCurrencyCode | CURRENCY_CODE | — | — |
| 57 | RecommendationTxnsPEOLastInviteSentDate | LAST_INVITE_SENT_DATE | — | ✅ |
| 58 | RecommendationTxnsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 59 | RecommendationTxnsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 60 | RecommendationTxnsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 61 | RecommendationTxnsPEOLengthOfRelationship | LENGTH_OF_RELATIONSHIP | — | ✅ |
| 62 | RecommendationTxnsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 63 | RecommendationTxnsPEOOrganizationAddress | ORGANIZATION_ADDRESS | — | — |
| 64 | RecommendationTxnsPEOOrganizationOtherName | ORGANIZATION_OTHER_NAME | — | ✅ |
| 65 | RecommendationTxnsPEOOrganizationOtherNameFlag | ORGANIZATION_OTHER_NAME_FLAG | — | — |
| 66 | RecommendationTxnsPEOOrganizationPartyId | ORGANIZATION_PARTY_ID | — | — |
| 67 | RecommendationTxnsPEOParentId | PARENT_ID | — | — |
| 68 | RecommendationTxnsPEOPartyId | PARTY_ID | — | — |
| 69 | RecommendationTxnsPEOPhoneAreaCode | PHONE_AREA_CODE | — | ✅ |
| 70 | RecommendationTxnsPEOPhoneCountryCode | PHONE_COUNTRY_CODE | — | ✅ |
| 71 | RecommendationTxnsPEOPhoneNumber | PHONE_NUMBER | — | ✅ |
| 72 | RecommendationTxnsPEORecommendationTxnId | RECOMMENDATION_TXN_ID | 🔑 | ✅ |
| 73 | RecommendationTxnsPEORecommendationTypeCode | RECOMMENDATION_TYPE_CODE | — | ✅ |
| 74 | RecommendationTxnsPEORecommenderAddress | RECOMMENDER_ADDRESS | — | ✅ |
| 75 | RecommendationTxnsPEORecommenderDescription | RECOMMENDER_DESCRIPTION | — | ✅ |
| 76 | RecommendationTxnsPEORecommenderEmailAddress | RECOMMENDER_EMAIL_ADDRESS | — | ✅ |
| 77 | RecommendationTxnsPEORecommenderFirstName | RECOMMENDER_FIRST_NAME | — | ✅ |
| 78 | RecommendationTxnsPEORecommenderLastName | RECOMMENDER_LAST_NAME | — | ✅ |
| 79 | RecommendationTxnsPEORecommenderNameTitle | RECOMMENDER_NAME_TITLE | — | ✅ |
| 80 | RecommendationTxnsPEORecommenderPartyId | RECOMMENDER_PARTY_ID | — | — |
| 81 | RecommendationTxnsPEORelationshipToStudent | RELATIONSHIP_TO_STUDENT | — | ✅ |
| 82 | RecommendationTxnsPEO_AliasParentId | PARENT_ID | — | — |
| 83 | RecommendationTxnsPEO_AliasRecommendationTxnId | RECOMMENDATION_TXN_ID | — | — |

### [[hey_recommendation_txn_sources|HEY_RECOMMENDATION_TXN_SOURCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RecommendationTxnSourcesPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | RecommendationTxnSourcesPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | RecommendationTxnSourcesPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | RecommendationTxnSourcesPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | RecommendationTxnSourcesPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | RecommendationTxnSourcesPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | RecommendationTxnSourcesPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | RecommendationTxnSourcesPEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | RecommendationTxnSourcesPEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | RecommendationTxnSourcesPEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | RecommendationTxnSourcesPEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | RecommendationTxnSourcesPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | RecommendationTxnSourcesPEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | RecommendationTxnSourcesPEOAttribute3 | ATTRIBUTE3 | — | — |
| 15 | RecommendationTxnSourcesPEOAttribute4 | ATTRIBUTE4 | — | — |
| 16 | RecommendationTxnSourcesPEOAttribute5 | ATTRIBUTE5 | — | — |
| 17 | RecommendationTxnSourcesPEOAttribute6 | ATTRIBUTE6 | — | — |
| 18 | RecommendationTxnSourcesPEOAttribute7 | ATTRIBUTE7 | — | — |
| 19 | RecommendationTxnSourcesPEOAttribute8 | ATTRIBUTE8 | — | — |
| 20 | RecommendationTxnSourcesPEOAttribute9 | ATTRIBUTE9 | — | — |
| 21 | RecommendationTxnSourcesPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | RecommendationTxnSourcesPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | RecommendationTxnSourcesPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 24 | RecommendationTxnSourcesPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | RecommendationTxnSourcesPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | RecommendationTxnSourcesPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | RecommendationTxnSourcesPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | RecommendationTxnSourcesPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 29 | RecommendationTxnSourcesPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 30 | RecommendationTxnSourcesPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 31 | RecommendationTxnSourcesPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 32 | RecommendationTxnSourcesPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 33 | RecommendationTxnSourcesPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 34 | RecommendationTxnSourcesPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 35 | RecommendationTxnSourcesPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 36 | RecommendationTxnSourcesPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 37 | RecommendationTxnSourcesPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 38 | RecommendationTxnSourcesPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 39 | RecommendationTxnSourcesPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 40 | RecommendationTxnSourcesPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 41 | RecommendationTxnSourcesPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 42 | RecommendationTxnSourcesPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 43 | RecommendationTxnSourcesPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 44 | RecommendationTxnSourcesPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 45 | RecommendationTxnSourcesPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 46 | RecommendationTxnSourcesPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 47 | RecommendationTxnSourcesPEOCreatedBy | CREATED_BY | — | — |
| 48 | RecommendationTxnSourcesPEOCreationDate | CREATION_DATE | — | — |
| 49 | RecommendationTxnSourcesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 50 | RecommendationTxnSourcesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 51 | RecommendationTxnSourcesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 52 | RecommendationTxnSourcesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 53 | RecommendationTxnSourcesPEOOriginSystemCode | ORIGIN_SYSTEM_CODE | — | — |
| 54 | RecommendationTxnSourcesPEOOriginSystemReference | ORIGIN_SYSTEM_REFERENCE | — | — |
| 55 | RecommendationTxnSourcesPEORecommendationTxnId | RECOMMENDATION_TXN_ID | — | — |
| 56 | RecommendationTxnSourcesPEORecommendationTxnSourceId | RECOMMENDATION_TXN_SOURCE_ID | — | — |
| 57 | RecommendationTxnSourcesPEOStatusCode | STATUS_CODE | — | ✅ |

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
