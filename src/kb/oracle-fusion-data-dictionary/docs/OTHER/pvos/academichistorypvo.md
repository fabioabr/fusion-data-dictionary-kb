---
id: DOC-OTHER-PVO-AcademicHistoryPVO
doc_type: system-doc
title: "AcademicHistoryPVO — PVO Cross-Module"
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
  - AcademicHistoryPVO
  - academichistorypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AcademicHistoryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Academic History. Acessa as tabelas: HEY_ACADEMIC_HISTORY_TXNS, HEY_ACAD_HISTORY_TXN_SOURCES, HZ_PARTIES.

**Caminho:** `FscmTopModelAM.HedHeyStdExtAcademicInfoAM.AcademicHistoryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 296 | 3 | 1 | 27 | 9% |

---

## 🔗 Tabelas Relacionadas

- [[hey_academic_history_txns|HEY_ACADEMIC_HISTORY_TXNS]] — 93 atributos (1 PKs, 24 BICC)
- [[hey_acad_history_txn_sources|HEY_ACAD_HISTORY_TXN_SOURCES]] — 62 atributos (2 BICC)
- [[hz_parties|HZ_PARTIES]] — 141 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hey_academic_history_txns|HEY_ACADEMIC_HISTORY_TXNS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcademicHistoryTxnsPEOAcademicHistoryTxnId | ACADEMIC_HISTORY_TXN_ID | 🔑 | ✅ |
| 2 | AcademicHistoryTxnsPEOAcademicLevelCode | ACADEMIC_LEVEL_CODE | — | — |
| 3 | AcademicHistoryTxnsPEOAttribute1 | ATTRIBUTE1 | — | — |
| 4 | AcademicHistoryTxnsPEOAttribute10 | ATTRIBUTE10 | — | — |
| 5 | AcademicHistoryTxnsPEOAttribute11 | ATTRIBUTE11 | — | — |
| 6 | AcademicHistoryTxnsPEOAttribute12 | ATTRIBUTE12 | — | — |
| 7 | AcademicHistoryTxnsPEOAttribute13 | ATTRIBUTE13 | — | — |
| 8 | AcademicHistoryTxnsPEOAttribute14 | ATTRIBUTE14 | — | — |
| 9 | AcademicHistoryTxnsPEOAttribute15 | ATTRIBUTE15 | — | — |
| 10 | AcademicHistoryTxnsPEOAttribute16 | ATTRIBUTE16 | — | — |
| 11 | AcademicHistoryTxnsPEOAttribute17 | ATTRIBUTE17 | — | — |
| 12 | AcademicHistoryTxnsPEOAttribute18 | ATTRIBUTE18 | — | — |
| 13 | AcademicHistoryTxnsPEOAttribute19 | ATTRIBUTE19 | — | — |
| 14 | AcademicHistoryTxnsPEOAttribute2 | ATTRIBUTE2 | — | — |
| 15 | AcademicHistoryTxnsPEOAttribute20 | ATTRIBUTE20 | — | — |
| 16 | AcademicHistoryTxnsPEOAttribute3 | ATTRIBUTE3 | — | — |
| 17 | AcademicHistoryTxnsPEOAttribute4 | ATTRIBUTE4 | — | — |
| 18 | AcademicHistoryTxnsPEOAttribute5 | ATTRIBUTE5 | — | — |
| 19 | AcademicHistoryTxnsPEOAttribute6 | ATTRIBUTE6 | — | — |
| 20 | AcademicHistoryTxnsPEOAttribute7 | ATTRIBUTE7 | — | — |
| 21 | AcademicHistoryTxnsPEOAttribute8 | ATTRIBUTE8 | — | — |
| 22 | AcademicHistoryTxnsPEOAttribute9 | ATTRIBUTE9 | — | — |
| 23 | AcademicHistoryTxnsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 24 | AcademicHistoryTxnsPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 25 | AcademicHistoryTxnsPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 26 | AcademicHistoryTxnsPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 27 | AcademicHistoryTxnsPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 28 | AcademicHistoryTxnsPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 29 | AcademicHistoryTxnsPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 30 | AcademicHistoryTxnsPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 31 | AcademicHistoryTxnsPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 32 | AcademicHistoryTxnsPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 33 | AcademicHistoryTxnsPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 34 | AcademicHistoryTxnsPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 35 | AcademicHistoryTxnsPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 36 | AcademicHistoryTxnsPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 37 | AcademicHistoryTxnsPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 38 | AcademicHistoryTxnsPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 39 | AcademicHistoryTxnsPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 40 | AcademicHistoryTxnsPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 41 | AcademicHistoryTxnsPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 42 | AcademicHistoryTxnsPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 43 | AcademicHistoryTxnsPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 44 | AcademicHistoryTxnsPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 45 | AcademicHistoryTxnsPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 46 | AcademicHistoryTxnsPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 47 | AcademicHistoryTxnsPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 48 | AcademicHistoryTxnsPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 49 | AcademicHistoryTxnsPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 50 | AcademicHistoryTxnsPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 51 | AcademicHistoryTxnsPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 52 | AcademicHistoryTxnsPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 53 | AcademicHistoryTxnsPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 54 | AcademicHistoryTxnsPEOClassRankPosition | CLASS_RANK_POSITION | — | ✅ |
| 55 | AcademicHistoryTxnsPEOClassRankSize | CLASS_RANK_SIZE | — | ✅ |
| 56 | AcademicHistoryTxnsPEOContactAddress | CONTACT_ADDRESS | — | ✅ |
| 57 | AcademicHistoryTxnsPEOContactEmailAddress | CONTACT_EMAIL_ADDRESS | — | ✅ |
| 58 | AcademicHistoryTxnsPEOContactFirstName | CONTACT_FIRST_NAME | — | ✅ |
| 59 | AcademicHistoryTxnsPEOContactLastName | CONTACT_LAST_NAME | — | ✅ |
| 60 | AcademicHistoryTxnsPEOContactNameTitle | CONTACT_NAME_TITLE | — | ✅ |
| 61 | AcademicHistoryTxnsPEOContactPartyId | CONTACT_PARTY_ID | — | — |
| 62 | AcademicHistoryTxnsPEOCorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 63 | AcademicHistoryTxnsPEOCreatedBy | CREATED_BY | — | — |
| 64 | AcademicHistoryTxnsPEOCreationDate | CREATION_DATE | — | — |
| 65 | AcademicHistoryTxnsPEOCurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 66 | AcademicHistoryTxnsPEOCurrencyCode | CURRENCY_CODE | — | — |
| 67 | AcademicHistoryTxnsPEODegreeCode | DEGREE_CODE | — | ✅ |
| 68 | AcademicHistoryTxnsPEODegreeEarned | DEGREE_EARNED | — | ✅ |
| 69 | AcademicHistoryTxnsPEOEntryDate | ENTRY_DATE | — | ✅ |
| 70 | AcademicHistoryTxnsPEOGpa | GPA | — | ✅ |
| 71 | AcademicHistoryTxnsPEOGpaWeightingCode | GPA_WEIGHTING_CODE | — | ✅ |
| 72 | AcademicHistoryTxnsPEOGraduationDate | GRADUATION_DATE | — | ✅ |
| 73 | AcademicHistoryTxnsPEOGraduationFlag | GRADUATION_FLAG | — | ✅ |
| 74 | AcademicHistoryTxnsPEOHomeSchoolFlag | HOME_SCHOOL_FLAG | — | ✅ |
| 75 | AcademicHistoryTxnsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 76 | AcademicHistoryTxnsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 77 | AcademicHistoryTxnsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 78 | AcademicHistoryTxnsPEOMajorProgramCode | MAJOR_PROGRAM_CODE | — | ✅ |
| 79 | AcademicHistoryTxnsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 80 | AcademicHistoryTxnsPEOOrganizationOtherName | ORGANIZATION_OTHER_NAME | — | ✅ |
| 81 | AcademicHistoryTxnsPEOOrganizationOtherNameFlag | ORGANIZATION_OTHER_NAME_FLAG | — | — |
| 82 | AcademicHistoryTxnsPEOOrganizationPartyId | ORGANIZATION_PARTY_ID | — | — |
| 83 | AcademicHistoryTxnsPEOOrganizationTypeCode | ORGANIZATION_TYPE_CODE | — | — |
| 84 | AcademicHistoryTxnsPEOParentId | PARENT_ID | — | — |
| 85 | AcademicHistoryTxnsPEOPartyId | PARTY_ID | — | — |
| 86 | AcademicHistoryTxnsPEOPhoneAreaCode | PHONE_AREA_CODE | — | ✅ |
| 87 | AcademicHistoryTxnsPEOPhoneCountryCode | PHONE_COUNTRY_CODE | — | ✅ |
| 88 | AcademicHistoryTxnsPEOPhoneNumber | PHONE_NUMBER | — | ✅ |
| 89 | AcademicHistoryTxnsPEOReducedPriceMealFlag | REDUCED_PRICE_MEAL_FLAG | — | ✅ |
| 90 | AcademicHistoryTxnsPEOSchoolDistrictName | SCHOOL_DISTRICT_NAME | — | — |
| 91 | AcademicHistoryTxnsPEOStudentIdentifier | STUDENT_IDENTIFIER | — | ✅ |
| 92 | AcademicHistoryTxnsPEO_AliasAcademicHistoryTxnId | ACADEMIC_HISTORY_TXN_ID | — | — |
| 93 | AcademicHistoryTxnsPEO_AliasParentId | PARENT_ID | — | — |

### [[hey_acad_history_txn_sources|HEY_ACAD_HISTORY_TXN_SOURCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcadHistoryTxnSourcesPEOAcadHistoryTxnSourceId | ACAD_HISTORY_TXN_SOURCE_ID | — | — |
| 2 | AcadHistoryTxnSourcesPEOAcademicHistoryTxnId | ACADEMIC_HISTORY_TXN_ID | — | — |
| 3 | AcadHistoryTxnSourcesPEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | AcadHistoryTxnSourcesPEOAttribute11 | ATTRIBUTE11 | — | — |
| 5 | AcadHistoryTxnSourcesPEOAttribute110 | ATTRIBUTE1 | — | — |
| 6 | AcadHistoryTxnSourcesPEOAttribute12 | ATTRIBUTE12 | — | — |
| 7 | AcadHistoryTxnSourcesPEOAttribute13 | ATTRIBUTE13 | — | — |
| 8 | AcadHistoryTxnSourcesPEOAttribute14 | ATTRIBUTE14 | — | — |
| 9 | AcadHistoryTxnSourcesPEOAttribute15 | ATTRIBUTE15 | — | — |
| 10 | AcadHistoryTxnSourcesPEOAttribute16 | ATTRIBUTE16 | — | — |
| 11 | AcadHistoryTxnSourcesPEOAttribute17 | ATTRIBUTE17 | — | — |
| 12 | AcadHistoryTxnSourcesPEOAttribute18 | ATTRIBUTE18 | — | — |
| 13 | AcadHistoryTxnSourcesPEOAttribute19 | ATTRIBUTE19 | — | — |
| 14 | AcadHistoryTxnSourcesPEOAttribute2 | ATTRIBUTE2 | — | — |
| 15 | AcadHistoryTxnSourcesPEOAttribute20 | ATTRIBUTE20 | — | — |
| 16 | AcadHistoryTxnSourcesPEOAttribute3 | ATTRIBUTE3 | — | — |
| 17 | AcadHistoryTxnSourcesPEOAttribute4 | ATTRIBUTE4 | — | — |
| 18 | AcadHistoryTxnSourcesPEOAttribute5 | ATTRIBUTE5 | — | — |
| 19 | AcadHistoryTxnSourcesPEOAttribute6 | ATTRIBUTE6 | — | — |
| 20 | AcadHistoryTxnSourcesPEOAttribute7 | ATTRIBUTE7 | — | — |
| 21 | AcadHistoryTxnSourcesPEOAttribute8 | ATTRIBUTE8 | — | — |
| 22 | AcadHistoryTxnSourcesPEOAttribute9 | ATTRIBUTE9 | — | — |
| 23 | AcadHistoryTxnSourcesPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 24 | AcadHistoryTxnSourcesPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 25 | AcadHistoryTxnSourcesPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 26 | AcadHistoryTxnSourcesPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 27 | AcadHistoryTxnSourcesPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 28 | AcadHistoryTxnSourcesPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 29 | AcadHistoryTxnSourcesPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 30 | AcadHistoryTxnSourcesPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 31 | AcadHistoryTxnSourcesPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 32 | AcadHistoryTxnSourcesPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 33 | AcadHistoryTxnSourcesPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 34 | AcadHistoryTxnSourcesPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 35 | AcadHistoryTxnSourcesPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 36 | AcadHistoryTxnSourcesPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 37 | AcadHistoryTxnSourcesPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 38 | AcadHistoryTxnSourcesPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 39 | AcadHistoryTxnSourcesPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 40 | AcadHistoryTxnSourcesPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 41 | AcadHistoryTxnSourcesPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 42 | AcadHistoryTxnSourcesPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 43 | AcadHistoryTxnSourcesPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 44 | AcadHistoryTxnSourcesPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 45 | AcadHistoryTxnSourcesPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 46 | AcadHistoryTxnSourcesPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 47 | AcadHistoryTxnSourcesPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 48 | AcadHistoryTxnSourcesPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 49 | AcadHistoryTxnSourcesPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 50 | AcadHistoryTxnSourcesPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 51 | AcadHistoryTxnSourcesPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 52 | AcadHistoryTxnSourcesPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 53 | AcadHistoryTxnSourcesPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 54 | AcadHistoryTxnSourcesPEOCreatedBy | CREATED_BY | — | — |
| 55 | AcadHistoryTxnSourcesPEOCreationDate | CREATION_DATE | — | — |
| 56 | AcadHistoryTxnSourcesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 57 | AcadHistoryTxnSourcesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 58 | AcadHistoryTxnSourcesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 59 | AcadHistoryTxnSourcesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 60 | AcadHistoryTxnSourcesPEOOriginSystemCode | ORIGIN_SYSTEM_CODE | — | — |
| 61 | AcadHistoryTxnSourcesPEOOriginSystemReference | ORIGIN_SYSTEM_REFERENCE | — | — |
| 62 | AcadHistoryTxnSourcesPEOStatusCode | STATUS_CODE | — | ✅ |

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
| 94 | PartyPEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
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
