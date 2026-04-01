---
id: DOC-OTHER-PVO-Relationship
doc_type: system-doc
title: "Relationship — PVO Cross-Module"
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
  - Relationship
  - relationship
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# Relationship

## 📌 Visão Geral

View Object para extração BICC de dados de Relationship. Acessa as tabelas: HZ_PARTIES, HZ_RELATIONSHIPS, HZ_RELATIONSHIP_TYPES.

**Caminho:** `FscmTopModelAM.DooTopAM.Relationship`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 201 | 3 | 1 | 60 | 30% |

---

## 🔗 Tabelas Relacionadas

- [[hz_parties|HZ_PARTIES]] — 78 atributos (47 BICC)
- [[hz_relationships|HZ_RELATIONSHIPS]] — 115 atributos (1 PKs, 12 BICC)
- [[hz_relationship_types|HZ_RELATIONSHIP_TYPES]] — 8 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectPartyPEOAnalysisFy | ANALYSIS_FY | — | — |
| 2 | ObjectPartyPEOCategoryCode | CATEGORY_CODE | — | — |
| 3 | ObjectPartyPEOCertReasonCode | CERT_REASON_CODE | — | — |
| 4 | ObjectPartyPEOCertificationLevel | CERTIFICATION_LEVEL | — | — |
| 5 | ObjectPartyPEOCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 6 | ObjectPartyPEODunsNumberC | DUNS_NUMBER_C | — | — |
| 7 | ObjectPartyPEOEmailAddress | EMAIL_ADDRESS | — | — |
| 8 | ObjectPartyPEOEmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 9 | ObjectPartyPEOHomeCountry | HOME_COUNTRY | — | — |
| 10 | ObjectPartyPEOHqBranchInd | HQ_BRANCH_IND | — | — |
| 11 | ObjectPartyPEOJgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 12 | ObjectPartyPEOLanguageName | LANGUAGE_NAME | — | — |
| 13 | ObjectPartyPEONextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 14 | ObjectPartyPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | ObjectPartyPEOOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 16 | ObjectPartyPEOPartyId | PARTY_ID | — | — |
| 17 | ObjectPartyPEOPartyName | PARTY_NAME | — | — |
| 18 | ObjectPartyPEOPartyNumber | PARTY_NUMBER | — | — |
| 19 | ObjectPartyPEOPartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 20 | ObjectPartyPEOPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 21 | ObjectPartyPEOPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 22 | ObjectPartyPEOSicCode | SIC_CODE | — | — |
| 23 | ObjectPartyPEOSicCodeType | SIC_CODE_TYPE | — | — |
| 24 | ObjectPartyPEOThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 25 | ObjectPartyPEOUrl | URL | — | — |
| 26 | ObjectPartyPEOValidatedFlag | VALIDATED_FLAG | — | — |
| 27 | ObjectPartyPEOYearEstablished | YEAR_ESTABLISHED | — | — |
| 28 | SubjectPartyPEOAddress1 | ADDRESS1 | — | ✅ |
| 29 | SubjectPartyPEOAddress2 | ADDRESS2 | — | ✅ |
| 30 | SubjectPartyPEOAddress3 | ADDRESS3 | — | ✅ |
| 31 | SubjectPartyPEOAddress4 | ADDRESS4 | — | ✅ |
| 32 | SubjectPartyPEOCategoryCode | CATEGORY_CODE | — | ✅ |
| 33 | SubjectPartyPEOCertReasonCode | CERT_REASON_CODE | — | ✅ |
| 34 | SubjectPartyPEOCertificationLevel | CERTIFICATION_LEVEL | — | ✅ |
| 35 | SubjectPartyPEOCity | CITY | — | ✅ |
| 36 | SubjectPartyPEOCountry | COUNTRY | — | ✅ |
| 37 | SubjectPartyPEOCounty | COUNTY | — | ✅ |
| 38 | SubjectPartyPEOCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | ✅ |
| 39 | SubjectPartyPEODunsNumberC | DUNS_NUMBER_C | — | ✅ |
| 40 | SubjectPartyPEOEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 41 | SubjectPartyPEOEmployeesTotal | EMPLOYEES_TOTAL | — | ✅ |
| 42 | SubjectPartyPEOHqBranchInd | HQ_BRANCH_IND | — | ✅ |
| 43 | SubjectPartyPEOJgzzFiscalCode | JGZZ_FISCAL_CODE | — | ✅ |
| 44 | SubjectPartyPEOLanguageName | LANGUAGE_NAME | — | ✅ |
| 45 | SubjectPartyPEONextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | ✅ |
| 46 | SubjectPartyPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 47 | SubjectPartyPEOOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 48 | SubjectPartyPEOPartyName | PARTY_NAME | — | ✅ |
| 49 | SubjectPartyPEOPartyNumber | PARTY_NUMBER | — | ✅ |
| 50 | SubjectPartyPEOPartyType | PARTY_TYPE | — | ✅ |
| 51 | SubjectPartyPEOPartyUniqueName | PARTY_UNIQUE_NAME | — | ✅ |
| 52 | SubjectPartyPEOPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | ✅ |
| 53 | SubjectPartyPEOPersonFirstName | PERSON_FIRST_NAME | — | ✅ |
| 54 | SubjectPartyPEOPersonLastName | PERSON_LAST_NAME | — | ✅ |
| 55 | SubjectPartyPEOPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | ✅ |
| 56 | SubjectPartyPEOPersonMiddleName | PERSON_MIDDLE_NAME | — | ✅ |
| 57 | SubjectPartyPEOPersonNameSuffix | PERSON_NAME_SUFFIX | — | ✅ |
| 58 | SubjectPartyPEOPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | ✅ |
| 59 | SubjectPartyPEOPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | ✅ |
| 60 | SubjectPartyPEOPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | ✅ |
| 61 | SubjectPartyPEOPersonTitle | PERSON_TITLE | — | ✅ |
| 62 | SubjectPartyPEOPostalCode | POSTAL_CODE | — | ✅ |
| 63 | SubjectPartyPEOPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | ✅ |
| 64 | SubjectPartyPEOPreferredName | PREFERRED_NAME | — | ✅ |
| 65 | SubjectPartyPEOPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | ✅ |
| 66 | SubjectPartyPEOPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | ✅ |
| 67 | SubjectPartyPEOPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | ✅ |
| 68 | SubjectPartyPEOPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | ✅ |
| 69 | SubjectPartyPEOPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | ✅ |
| 70 | SubjectPartyPEOProvince | PROVINCE | — | ✅ |
| 71 | SubjectPartyPEOSalutation | SALUTATION | — | ✅ |
| 72 | SubjectPartyPEOSicCode | SIC_CODE | — | ✅ |
| 73 | SubjectPartyPEOSicCodeType | SIC_CODE_TYPE | — | ✅ |
| 74 | SubjectPartyPEOState | STATE | — | ✅ |
| 75 | SubjectPartyPEOSubAnalysisFy | ANALYSIS_FY | — | — |
| 76 | SubjectPartyPEOSubjectPartyId | PARTY_ID | — | ✅ |
| 77 | SubjectPartyPEOUrl | URL | — | — |
| 78 | SubjectPartyPEOValidatedFlag | VALIDATED_FLAG | — | ✅ |

### [[hz_relationships|HZ_RELATIONSHIPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdditionalInformation1 | ADDITIONAL_INFORMATION1 | — | — |
| 2 | AdditionalInformation10 | ADDITIONAL_INFORMATION10 | — | — |
| 3 | AdditionalInformation11 | ADDITIONAL_INFORMATION11 | — | — |
| 4 | AdditionalInformation12 | ADDITIONAL_INFORMATION12 | — | — |
| 5 | AdditionalInformation13 | ADDITIONAL_INFORMATION13 | — | — |
| 6 | AdditionalInformation14 | ADDITIONAL_INFORMATION14 | — | — |
| 7 | AdditionalInformation15 | ADDITIONAL_INFORMATION15 | — | — |
| 8 | AdditionalInformation16 | ADDITIONAL_INFORMATION16 | — | — |
| 9 | AdditionalInformation17 | ADDITIONAL_INFORMATION17 | — | — |
| 10 | AdditionalInformation18 | ADDITIONAL_INFORMATION18 | — | — |
| 11 | AdditionalInformation19 | ADDITIONAL_INFORMATION19 | — | — |
| 12 | AdditionalInformation2 | ADDITIONAL_INFORMATION2 | — | — |
| 13 | AdditionalInformation20 | ADDITIONAL_INFORMATION20 | — | — |
| 14 | AdditionalInformation21 | ADDITIONAL_INFORMATION21 | — | — |
| 15 | AdditionalInformation22 | ADDITIONAL_INFORMATION22 | — | — |
| 16 | AdditionalInformation23 | ADDITIONAL_INFORMATION23 | — | — |
| 17 | AdditionalInformation24 | ADDITIONAL_INFORMATION24 | — | — |
| 18 | AdditionalInformation25 | ADDITIONAL_INFORMATION25 | — | — |
| 19 | AdditionalInformation26 | ADDITIONAL_INFORMATION26 | — | — |
| 20 | AdditionalInformation27 | ADDITIONAL_INFORMATION27 | — | — |
| 21 | AdditionalInformation28 | ADDITIONAL_INFORMATION28 | — | — |
| 22 | AdditionalInformation29 | ADDITIONAL_INFORMATION29 | — | — |
| 23 | AdditionalInformation3 | ADDITIONAL_INFORMATION3 | — | — |
| 24 | AdditionalInformation30 | ADDITIONAL_INFORMATION30 | — | — |
| 25 | AdditionalInformation4 | ADDITIONAL_INFORMATION4 | — | — |
| 26 | AdditionalInformation5 | ADDITIONAL_INFORMATION5 | — | — |
| 27 | AdditionalInformation6 | ADDITIONAL_INFORMATION6 | — | — |
| 28 | AdditionalInformation7 | ADDITIONAL_INFORMATION7 | — | — |
| 29 | AdditionalInformation8 | ADDITIONAL_INFORMATION8 | — | — |
| 30 | AdditionalInformation9 | ADDITIONAL_INFORMATION9 | — | — |
| 31 | Attribute1 | ATTRIBUTE1 | — | — |
| 32 | Attribute10 | ATTRIBUTE10 | — | — |
| 33 | Attribute11 | ATTRIBUTE11 | — | — |
| 34 | Attribute12 | ATTRIBUTE12 | — | — |
| 35 | Attribute13 | ATTRIBUTE13 | — | — |
| 36 | Attribute14 | ATTRIBUTE14 | — | — |
| 37 | Attribute15 | ATTRIBUTE15 | — | — |
| 38 | Attribute16 | ATTRIBUTE16 | — | — |
| 39 | Attribute17 | ATTRIBUTE17 | — | — |
| 40 | Attribute18 | ATTRIBUTE18 | — | — |
| 41 | Attribute19 | ATTRIBUTE19 | — | — |
| 42 | Attribute2 | ATTRIBUTE2 | — | — |
| 43 | Attribute20 | ATTRIBUTE20 | — | — |
| 44 | Attribute21 | ATTRIBUTE21 | — | — |
| 45 | Attribute22 | ATTRIBUTE22 | — | — |
| 46 | Attribute23 | ATTRIBUTE23 | — | — |
| 47 | Attribute24 | ATTRIBUTE24 | — | — |
| 48 | Attribute25 | ATTRIBUTE25 | — | — |
| 49 | Attribute26 | ATTRIBUTE26 | — | — |
| 50 | Attribute27 | ATTRIBUTE27 | — | — |
| 51 | Attribute28 | ATTRIBUTE28 | — | — |
| 52 | Attribute29 | ATTRIBUTE29 | — | — |
| 53 | Attribute3 | ATTRIBUTE3 | — | — |
| 54 | Attribute30 | ATTRIBUTE30 | — | — |
| 55 | Attribute4 | ATTRIBUTE4 | — | — |
| 56 | Attribute5 | ATTRIBUTE5 | — | — |
| 57 | Attribute6 | ATTRIBUTE6 | — | — |
| 58 | Attribute7 | ATTRIBUTE7 | — | — |
| 59 | Attribute8 | ATTRIBUTE8 | — | — |
| 60 | Attribute9 | ATTRIBUTE9 | — | — |
| 61 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 62 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 63 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 64 | AttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 65 | AttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 66 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 67 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 68 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 69 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 70 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 71 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 72 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 73 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 74 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 75 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 76 | AttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 77 | AttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 78 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 79 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 80 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 81 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 82 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 83 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 84 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 85 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 86 | RelationshipActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 87 | RelationshipCode | RELATIONSHIP_CODE | — | ✅ |
| 88 | RelationshipComments | COMMENTS | — | ✅ |
| 89 | RelationshipCreatedBy | CREATED_BY | — | ✅ |
| 90 | RelationshipCreatedByModule | CREATED_BY_MODULE | — | — |
| 91 | RelationshipCreationDate | CREATION_DATE | — | ✅ |
| 92 | RelationshipDependentFlag | DEPENDENT_FLAG | — | — |
| 93 | RelationshipDirectionCode | DIRECTION_CODE | — | — |
| 94 | RelationshipDirectionalFlag | DIRECTIONAL_FLAG | — | — |
| 95 | RelationshipEndDate | END_DATE | — | ✅ |
| 96 | RelationshipHeadOfHouseholdFlag | HEAD_OF_HOUSEHOLD_FLAG | — | — |
| 97 | RelationshipId | RELATIONSHIP_ID | — | ✅ |
| 98 | RelationshipLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 99 | RelationshipLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 100 | RelationshipLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 101 | RelationshipObjectId | OBJECT_ID | — | — |
| 102 | RelationshipObjectTableName | OBJECT_TABLE_NAME | — | — |
| 103 | RelationshipObjectType | OBJECT_TYPE | — | — |
| 104 | RelationshipObjectUsageCode | OBJECT_USAGE_CODE | — | — |
| 105 | RelationshipObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 106 | RelationshipPercentageOwnership | PERCENTAGE_OWNERSHIP | — | — |
| 107 | RelationshipRecId | RELATIONSHIP_REC_ID | 🔑 | ✅ |
| 108 | RelationshipRequestId | REQUEST_ID | — | — |
| 109 | RelationshipStartDate | START_DATE | — | ✅ |
| 110 | RelationshipStatus | STATUS | — | ✅ |
| 111 | RelationshipSubjectId | SUBJECT_ID | — | — |
| 112 | RelationshipSubjectTableName | SUBJECT_TABLE_NAME | — | — |
| 113 | RelationshipSubjectType | SUBJECT_TYPE | — | — |
| 114 | RelationshipSubjectUsageCode | SUBJECT_USAGE_CODE | — | — |
| 115 | RelationshipType | RELATIONSHIP_TYPE | — | ✅ |

### [[hz_relationship_types|HZ_RELATIONSHIP_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelTypeBackwardRelCode | BACKWARD_REL_CODE | — | — |
| 2 | RelTypeDirectionCode | DIRECTION_CODE | — | — |
| 3 | RelTypeForwardRelCode | FORWARD_REL_CODE | — | — |
| 4 | RelTypeObjectType | OBJECT_TYPE | — | — |
| 5 | RelTypeRelationshipTypeId | RELATIONSHIP_TYPE_ID | — | — |
| 6 | RelTypeRole | ROLE | — | ✅ |
| 7 | RelTypeStatus | STATUS | — | — |
| 8 | RelTypeSubjectType | SUBJECT_TYPE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
