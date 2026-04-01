---
id: DOC-OTHER-PVO-RelationshipsPVO
doc_type: system-doc
title: "RelationshipsPVO — PVO Cross-Module"
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
  - RelationshipsPVO
  - relationshipspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RelationshipsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Relationships. Acessa as tabelas: HEY_RELATIONSHIP_TXNS, HEY_RELATIONSHIP_TXN_SOURCES, HZ_PARTIES.

**Caminho:** `FscmTopModelAM.HedHeyStdExtAcademicInfoAM.RelationshipsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 528 | 3 | 1 | 31 | 6% |

---

## 🔗 Tabelas Relacionadas

- [[hey_relationship_txns|HEY_RELATIONSHIP_TXNS]] — 184 atributos (1 PKs, 27 BICC)
- [[hey_relationship_txn_sources|HEY_RELATIONSHIP_TXN_SOURCES]] — 62 atributos (2 BICC)
- [[hz_parties|HZ_PARTIES]] — 282 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hey_relationship_txns|HEY_RELATIONSHIP_TXNS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelationshipTxnsPEOAttendedInstDegreeRecCode | ATTENDED_INST_DEGREE_REC_CODE | — | ✅ |
| 2 | RelationshipTxnsPEOAttendedInstitutionDate | ATTENDED_INSTITUTION_DATE | — | ✅ |
| 3 | RelationshipTxnsPEOAttendedInstitutionFlag | ATTENDED_INSTITUTION_FLAG | — | ✅ |
| 4 | RelationshipTxnsPEOAttribute1 | ATTRIBUTE1 | — | — |
| 5 | RelationshipTxnsPEOAttribute10 | ATTRIBUTE10 | — | — |
| 6 | RelationshipTxnsPEOAttribute11 | ATTRIBUTE11 | — | — |
| 7 | RelationshipTxnsPEOAttribute12 | ATTRIBUTE12 | — | — |
| 8 | RelationshipTxnsPEOAttribute13 | ATTRIBUTE13 | — | — |
| 9 | RelationshipTxnsPEOAttribute14 | ATTRIBUTE14 | — | — |
| 10 | RelationshipTxnsPEOAttribute15 | ATTRIBUTE15 | — | — |
| 11 | RelationshipTxnsPEOAttribute16 | ATTRIBUTE16 | — | — |
| 12 | RelationshipTxnsPEOAttribute17 | ATTRIBUTE17 | — | — |
| 13 | RelationshipTxnsPEOAttribute18 | ATTRIBUTE18 | — | — |
| 14 | RelationshipTxnsPEOAttribute19 | ATTRIBUTE19 | — | — |
| 15 | RelationshipTxnsPEOAttribute2 | ATTRIBUTE2 | — | — |
| 16 | RelationshipTxnsPEOAttribute20 | ATTRIBUTE20 | — | — |
| 17 | RelationshipTxnsPEOAttribute3 | ATTRIBUTE3 | — | — |
| 18 | RelationshipTxnsPEOAttribute4 | ATTRIBUTE4 | — | — |
| 19 | RelationshipTxnsPEOAttribute5 | ATTRIBUTE5 | — | — |
| 20 | RelationshipTxnsPEOAttribute6 | ATTRIBUTE6 | — | — |
| 21 | RelationshipTxnsPEOAttribute7 | ATTRIBUTE7 | — | — |
| 22 | RelationshipTxnsPEOAttribute8 | ATTRIBUTE8 | — | — |
| 23 | RelationshipTxnsPEOAttribute9 | ATTRIBUTE9 | — | — |
| 24 | RelationshipTxnsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 25 | RelationshipTxnsPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 26 | RelationshipTxnsPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 27 | RelationshipTxnsPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 28 | RelationshipTxnsPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 29 | RelationshipTxnsPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 30 | RelationshipTxnsPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 31 | RelationshipTxnsPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 32 | RelationshipTxnsPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 33 | RelationshipTxnsPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 34 | RelationshipTxnsPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 35 | RelationshipTxnsPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 36 | RelationshipTxnsPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 37 | RelationshipTxnsPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 38 | RelationshipTxnsPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 39 | RelationshipTxnsPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 40 | RelationshipTxnsPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 41 | RelationshipTxnsPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 42 | RelationshipTxnsPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 43 | RelationshipTxnsPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 44 | RelationshipTxnsPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 45 | RelationshipTxnsPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 46 | RelationshipTxnsPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 47 | RelationshipTxnsPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 48 | RelationshipTxnsPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 49 | RelationshipTxnsPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 50 | RelationshipTxnsPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 51 | RelationshipTxnsPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 52 | RelationshipTxnsPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 53 | RelationshipTxnsPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 54 | RelationshipTxnsPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 55 | RelationshipTxnsPEOCorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 56 | RelationshipTxnsPEOCreatedBy | CREATED_BY | — | — |
| 57 | RelationshipTxnsPEOCreationDate | CREATION_DATE | — | — |
| 58 | RelationshipTxnsPEOCurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 59 | RelationshipTxnsPEOCurrencyCode | CURRENCY_CODE | — | — |
| 60 | RelationshipTxnsPEOHighestDegreeEarnedCode | HIGHEST_DEGREE_EARNED_CODE | — | ✅ |
| 61 | RelationshipTxnsPEOHighestDegreeEarnedDate | HIGHEST_DEGREE_EARNED_DATE | — | ✅ |
| 62 | RelationshipTxnsPEOHighestDegreeOrgPartyId | HIGHEST_DEGREE_ORG_PARTY_ID | — | — |
| 63 | RelationshipTxnsPEOHighestOrgOtherName | HIGHEST_ORG_OTHER_NAME | — | — |
| 64 | RelationshipTxnsPEOHighestOrgOtherNameFlag | HIGHEST_ORG_OTHER_NAME_FLAG | — | — |
| 65 | RelationshipTxnsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 66 | RelationshipTxnsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 67 | RelationshipTxnsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 68 | RelationshipTxnsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 69 | RelationshipTxnsPEOParentId | PARENT_ID | — | — |
| 70 | RelationshipTxnsPEOPartyId | PARTY_ID | — | — |
| 71 | RelationshipTxnsPEOPhoneAreaCode | PHONE_AREA_CODE | — | ✅ |
| 72 | RelationshipTxnsPEOPhoneCountryCode | PHONE_COUNTRY_CODE | — | ✅ |
| 73 | RelationshipTxnsPEOPhoneNumber | PHONE_NUMBER | — | ✅ |
| 74 | RelationshipTxnsPEORelationshipEmployedIn | RELATIONSHIP_EMPLOYED_IN | — | ✅ |
| 75 | RelationshipTxnsPEORelationshipFirstName | RELATIONSHIP_FIRST_NAME | — | ✅ |
| 76 | RelationshipTxnsPEORelationshipGenderCode | RELATIONSHIP_GENDER_CODE | — | ✅ |
| 77 | RelationshipTxnsPEORelationshipLastName | RELATIONSHIP_LAST_NAME | — | ✅ |
| 78 | RelationshipTxnsPEORelationshipLivingFlag | RELATIONSHIP_LIVING_FLAG | — | ✅ |
| 79 | RelationshipTxnsPEORelationshipMailingAddr | RELATIONSHIP_MAILING_ADDR | — | ✅ |
| 80 | RelationshipTxnsPEORelationshipMiddleName | RELATIONSHIP_MIDDLE_NAME | — | ✅ |
| 81 | RelationshipTxnsPEORelationshipOccupation | RELATIONSHIP_OCCUPATION | — | ✅ |
| 82 | RelationshipTxnsPEORelationshipPersonalEmail | RELATIONSHIP_PERSONAL_EMAIL | — | ✅ |
| 83 | RelationshipTxnsPEORelationshipPrefix | RELATIONSHIP_PREFIX | — | ✅ |
| 84 | RelationshipTxnsPEORelationshipSuffix | RELATIONSHIP_SUFFIX | — | ✅ |
| 85 | RelationshipTxnsPEORelationshipTxnId | RELATIONSHIP_TXN_ID | 🔑 | ✅ |
| 86 | RelationshipTxnsPEORelationshipTypeCode | RELATIONSHIP_TYPE_CODE | — | ✅ |
| 87 | RelationshipTxnsPEORelativesBirthCountryCode | RELATIVES_BIRTH_COUNTRY_CODE | — | ✅ |
| 88 | RelationshipTxnsPEOUndergradDegreeDate | UNDERGRAD_DEGREE_DATE | — | ✅ |
| 89 | RelationshipTxnsPEOUndergradDegreeEarnFlag | UNDERGRAD_DEGREE_EARN_FLAG | — | ✅ |
| 90 | RelationshipTxnsPEOUndergradOrgOtherName | UNDERGRAD_ORG_OTHER_NAME | — | ✅ |
| 91 | RelationshipTxnsPEOUndergradOrgOtherNameFlag | UNDERGRAD_ORG_OTHER_NAME_FLAG | — | — |
| 92 | RelationshipTxnsPEOUndergradOrgPartyId | UNDERGRAD_ORG_PARTY_ID | — | — |
| 93 | RelationshipTxnsPEO_AliasAttendedInstDegreeRecCode | ATTENDED_INST_DEGREE_REC_CODE | — | — |
| 94 | RelationshipTxnsPEO_AliasAttendedInstitutionDate | ATTENDED_INSTITUTION_DATE | — | — |
| 95 | RelationshipTxnsPEO_AliasAttendedInstitutionFlag | ATTENDED_INSTITUTION_FLAG | — | — |
| 96 | RelationshipTxnsPEO_AliasAttribute1 | ATTRIBUTE1 | — | — |
| 97 | RelationshipTxnsPEO_AliasAttribute10 | ATTRIBUTE10 | — | — |
| 98 | RelationshipTxnsPEO_AliasAttribute11 | ATTRIBUTE11 | — | — |
| 99 | RelationshipTxnsPEO_AliasAttribute12 | ATTRIBUTE12 | — | — |
| 100 | RelationshipTxnsPEO_AliasAttribute13 | ATTRIBUTE13 | — | — |
| 101 | RelationshipTxnsPEO_AliasAttribute14 | ATTRIBUTE14 | — | — |
| 102 | RelationshipTxnsPEO_AliasAttribute15 | ATTRIBUTE15 | — | — |
| 103 | RelationshipTxnsPEO_AliasAttribute16 | ATTRIBUTE16 | — | — |
| 104 | RelationshipTxnsPEO_AliasAttribute17 | ATTRIBUTE17 | — | — |
| 105 | RelationshipTxnsPEO_AliasAttribute18 | ATTRIBUTE18 | — | — |
| 106 | RelationshipTxnsPEO_AliasAttribute19 | ATTRIBUTE19 | — | — |
| 107 | RelationshipTxnsPEO_AliasAttribute2 | ATTRIBUTE2 | — | — |
| 108 | RelationshipTxnsPEO_AliasAttribute20 | ATTRIBUTE20 | — | — |
| 109 | RelationshipTxnsPEO_AliasAttribute3 | ATTRIBUTE3 | — | — |
| 110 | RelationshipTxnsPEO_AliasAttribute4 | ATTRIBUTE4 | — | — |
| 111 | RelationshipTxnsPEO_AliasAttribute5 | ATTRIBUTE5 | — | — |
| 112 | RelationshipTxnsPEO_AliasAttribute6 | ATTRIBUTE6 | — | — |
| 113 | RelationshipTxnsPEO_AliasAttribute7 | ATTRIBUTE7 | — | — |
| 114 | RelationshipTxnsPEO_AliasAttribute8 | ATTRIBUTE8 | — | — |
| 115 | RelationshipTxnsPEO_AliasAttribute9 | ATTRIBUTE9 | — | — |
| 116 | RelationshipTxnsPEO_AliasAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 117 | RelationshipTxnsPEO_AliasAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 118 | RelationshipTxnsPEO_AliasAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 119 | RelationshipTxnsPEO_AliasAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 120 | RelationshipTxnsPEO_AliasAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 121 | RelationshipTxnsPEO_AliasAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 122 | RelationshipTxnsPEO_AliasAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 123 | RelationshipTxnsPEO_AliasAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 124 | RelationshipTxnsPEO_AliasAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 125 | RelationshipTxnsPEO_AliasAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 126 | RelationshipTxnsPEO_AliasAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 127 | RelationshipTxnsPEO_AliasAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 128 | RelationshipTxnsPEO_AliasAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 129 | RelationshipTxnsPEO_AliasAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 130 | RelationshipTxnsPEO_AliasAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 131 | RelationshipTxnsPEO_AliasAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 132 | RelationshipTxnsPEO_AliasAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 133 | RelationshipTxnsPEO_AliasAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 134 | RelationshipTxnsPEO_AliasAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 135 | RelationshipTxnsPEO_AliasAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 136 | RelationshipTxnsPEO_AliasAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 137 | RelationshipTxnsPEO_AliasAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 138 | RelationshipTxnsPEO_AliasAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 139 | RelationshipTxnsPEO_AliasAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 140 | RelationshipTxnsPEO_AliasAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 141 | RelationshipTxnsPEO_AliasAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 142 | RelationshipTxnsPEO_AliasAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 143 | RelationshipTxnsPEO_AliasAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 144 | RelationshipTxnsPEO_AliasAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 145 | RelationshipTxnsPEO_AliasAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 146 | RelationshipTxnsPEO_AliasAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 147 | RelationshipTxnsPEO_AliasCorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 148 | RelationshipTxnsPEO_AliasCreatedBy | CREATED_BY | — | — |
| 149 | RelationshipTxnsPEO_AliasCreationDate | CREATION_DATE | — | — |
| 150 | RelationshipTxnsPEO_AliasCurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 151 | RelationshipTxnsPEO_AliasCurrencyCode | CURRENCY_CODE | — | — |
| 152 | RelationshipTxnsPEO_AliasHighestDegreeEarnedCode | HIGHEST_DEGREE_EARNED_CODE | — | — |
| 153 | RelationshipTxnsPEO_AliasHighestDegreeEarnedDate | HIGHEST_DEGREE_EARNED_DATE | — | — |
| 154 | RelationshipTxnsPEO_AliasHighestDegreeOrgPartyId | HIGHEST_DEGREE_ORG_PARTY_ID | — | — |
| 155 | RelationshipTxnsPEO_AliasHighestOrgOtherName | HIGHEST_ORG_OTHER_NAME | — | — |
| 156 | RelationshipTxnsPEO_AliasHighestOrgOtherNameFlag | HIGHEST_ORG_OTHER_NAME_FLAG | — | — |
| 157 | RelationshipTxnsPEO_AliasLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 158 | RelationshipTxnsPEO_AliasLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 159 | RelationshipTxnsPEO_AliasLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 160 | RelationshipTxnsPEO_AliasObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 161 | RelationshipTxnsPEO_AliasParentId | PARENT_ID | — | — |
| 162 | RelationshipTxnsPEO_AliasPartyId | PARTY_ID | — | — |
| 163 | RelationshipTxnsPEO_AliasPhoneAreaCode | PHONE_AREA_CODE | — | — |
| 164 | RelationshipTxnsPEO_AliasPhoneCountryCode | PHONE_COUNTRY_CODE | — | — |
| 165 | RelationshipTxnsPEO_AliasPhoneNumber | PHONE_NUMBER | — | — |
| 166 | RelationshipTxnsPEO_AliasRelationshipEmployedIn | RELATIONSHIP_EMPLOYED_IN | — | — |
| 167 | RelationshipTxnsPEO_AliasRelationshipFirstName | RELATIONSHIP_FIRST_NAME | — | — |
| 168 | RelationshipTxnsPEO_AliasRelationshipGenderCode | RELATIONSHIP_GENDER_CODE | — | — |
| 169 | RelationshipTxnsPEO_AliasRelationshipLastName | RELATIONSHIP_LAST_NAME | — | — |
| 170 | RelationshipTxnsPEO_AliasRelationshipLivingFlag | RELATIONSHIP_LIVING_FLAG | — | — |
| 171 | RelationshipTxnsPEO_AliasRelationshipMailingAddr | RELATIONSHIP_MAILING_ADDR | — | — |
| 172 | RelationshipTxnsPEO_AliasRelationshipMiddleName | RELATIONSHIP_MIDDLE_NAME | — | — |
| 173 | RelationshipTxnsPEO_AliasRelationshipOccupation | RELATIONSHIP_OCCUPATION | — | — |
| 174 | RelationshipTxnsPEO_AliasRelationshipPersonalEmail | RELATIONSHIP_PERSONAL_EMAIL | — | — |
| 175 | RelationshipTxnsPEO_AliasRelationshipPrefix | RELATIONSHIP_PREFIX | — | — |
| 176 | RelationshipTxnsPEO_AliasRelationshipSuffix | RELATIONSHIP_SUFFIX | — | — |
| 177 | RelationshipTxnsPEO_AliasRelationshipTxnId | RELATIONSHIP_TXN_ID | — | — |
| 178 | RelationshipTxnsPEO_AliasRelationshipTypeCode | RELATIONSHIP_TYPE_CODE | — | — |
| 179 | RelationshipTxnsPEO_AliasRelativesBirthCountryCode | RELATIVES_BIRTH_COUNTRY_CODE | — | — |
| 180 | RelationshipTxnsPEO_AliasUndergradDegreeDate | UNDERGRAD_DEGREE_DATE | — | — |
| 181 | RelationshipTxnsPEO_AliasUndergradDegreeEarnFlag | UNDERGRAD_DEGREE_EARN_FLAG | — | — |
| 182 | RelationshipTxnsPEO_AliasUndergradOrgOtherName | UNDERGRAD_ORG_OTHER_NAME | — | — |
| 183 | RelationshipTxnsPEO_AliasUndergradOrgOtherNameFlag | UNDERGRAD_ORG_OTHER_NAME_FLAG | — | — |
| 184 | RelationshipTxnsPEO_AliasUndergradOrgPartyId1 | UNDERGRAD_ORG_PARTY_ID | — | — |

### [[hey_relationship_txn_sources|HEY_RELATIONSHIP_TXN_SOURCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelationshipTxnSourcesPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | RelationshipTxnSourcesPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | RelationshipTxnSourcesPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | RelationshipTxnSourcesPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | RelationshipTxnSourcesPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | RelationshipTxnSourcesPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | RelationshipTxnSourcesPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | RelationshipTxnSourcesPEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | RelationshipTxnSourcesPEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | RelationshipTxnSourcesPEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | RelationshipTxnSourcesPEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | RelationshipTxnSourcesPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | RelationshipTxnSourcesPEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | RelationshipTxnSourcesPEOAttribute3 | ATTRIBUTE3 | — | — |
| 15 | RelationshipTxnSourcesPEOAttribute4 | ATTRIBUTE4 | — | — |
| 16 | RelationshipTxnSourcesPEOAttribute5 | ATTRIBUTE5 | — | — |
| 17 | RelationshipTxnSourcesPEOAttribute6 | ATTRIBUTE6 | — | — |
| 18 | RelationshipTxnSourcesPEOAttribute7 | ATTRIBUTE7 | — | — |
| 19 | RelationshipTxnSourcesPEOAttribute8 | ATTRIBUTE8 | — | — |
| 20 | RelationshipTxnSourcesPEOAttribute91 | ATTRIBUTE9 | — | — |
| 21 | RelationshipTxnSourcesPEOAttributeCategory1 | ATTRIBUTE_CATEGORY | — | — |
| 22 | RelationshipTxnSourcesPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | RelationshipTxnSourcesPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 24 | RelationshipTxnSourcesPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | RelationshipTxnSourcesPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | RelationshipTxnSourcesPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | RelationshipTxnSourcesPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | RelationshipTxnSourcesPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 29 | RelationshipTxnSourcesPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 30 | RelationshipTxnSourcesPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 31 | RelationshipTxnSourcesPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 32 | RelationshipTxnSourcesPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 33 | RelationshipTxnSourcesPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 34 | RelationshipTxnSourcesPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 35 | RelationshipTxnSourcesPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 36 | RelationshipTxnSourcesPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 37 | RelationshipTxnSourcesPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 38 | RelationshipTxnSourcesPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 39 | RelationshipTxnSourcesPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 40 | RelationshipTxnSourcesPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 41 | RelationshipTxnSourcesPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 42 | RelationshipTxnSourcesPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 43 | RelationshipTxnSourcesPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 44 | RelationshipTxnSourcesPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 45 | RelationshipTxnSourcesPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 46 | RelationshipTxnSourcesPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 47 | RelationshipTxnSourcesPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 48 | RelationshipTxnSourcesPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 49 | RelationshipTxnSourcesPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 50 | RelationshipTxnSourcesPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 51 | RelationshipTxnSourcesPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 52 | RelationshipTxnSourcesPEOCreatedBy | CREATED_BY | — | — |
| 53 | RelationshipTxnSourcesPEOCreationDate | CREATION_DATE | — | — |
| 54 | RelationshipTxnSourcesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 55 | RelationshipTxnSourcesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 56 | RelationshipTxnSourcesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 57 | RelationshipTxnSourcesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 58 | RelationshipTxnSourcesPEOOriginSystemCode | ORIGIN_SYSTEM_CODE | — | — |
| 59 | RelationshipTxnSourcesPEOOriginSystemReference | ORIGIN_SYSTEM_REFERENCE | — | — |
| 60 | RelationshipTxnSourcesPEORelationshipTxnId | RELATIONSHIP_TXN_ID | — | — |
| 61 | RelationshipTxnSourcesPEORelationshipTxnSourceId | RELATIONSHIP_TXN_SOURCE_ID | — | ✅ |
| 62 | RelationshipTxnSourcesPEOStatusCode | STATUS_CODE | — | — |

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
| 142 | PartyPEO_AliasAddress1 | ADDRESS1 | — | — |
| 143 | PartyPEO_AliasAddress2 | ADDRESS2 | — | — |
| 144 | PartyPEO_AliasAddress3 | ADDRESS3 | — | — |
| 145 | PartyPEO_AliasAddress4 | ADDRESS4 | — | — |
| 146 | PartyPEO_AliasAnalysisFy | ANALYSIS_FY | — | — |
| 147 | PartyPEO_AliasAttribute1 | ATTRIBUTE1 | — | — |
| 148 | PartyPEO_AliasAttribute10 | ATTRIBUTE10 | — | — |
| 149 | PartyPEO_AliasAttribute11 | ATTRIBUTE11 | — | — |
| 150 | PartyPEO_AliasAttribute12 | ATTRIBUTE12 | — | — |
| 151 | PartyPEO_AliasAttribute13 | ATTRIBUTE13 | — | — |
| 152 | PartyPEO_AliasAttribute14 | ATTRIBUTE14 | — | — |
| 153 | PartyPEO_AliasAttribute15 | ATTRIBUTE15 | — | — |
| 154 | PartyPEO_AliasAttribute16 | ATTRIBUTE16 | — | — |
| 155 | PartyPEO_AliasAttribute17 | ATTRIBUTE17 | — | — |
| 156 | PartyPEO_AliasAttribute18 | ATTRIBUTE18 | — | — |
| 157 | PartyPEO_AliasAttribute19 | ATTRIBUTE19 | — | — |
| 158 | PartyPEO_AliasAttribute2 | ATTRIBUTE2 | — | — |
| 159 | PartyPEO_AliasAttribute20 | ATTRIBUTE20 | — | — |
| 160 | PartyPEO_AliasAttribute21 | ATTRIBUTE21 | — | — |
| 161 | PartyPEO_AliasAttribute22 | ATTRIBUTE22 | — | — |
| 162 | PartyPEO_AliasAttribute23 | ATTRIBUTE23 | — | — |
| 163 | PartyPEO_AliasAttribute24 | ATTRIBUTE24 | — | — |
| 164 | PartyPEO_AliasAttribute25 | ATTRIBUTE25 | — | — |
| 165 | PartyPEO_AliasAttribute26 | ATTRIBUTE26 | — | — |
| 166 | PartyPEO_AliasAttribute27 | ATTRIBUTE27 | — | — |
| 167 | PartyPEO_AliasAttribute28 | ATTRIBUTE28 | — | — |
| 168 | PartyPEO_AliasAttribute29 | ATTRIBUTE29 | — | — |
| 169 | PartyPEO_AliasAttribute3 | ATTRIBUTE3 | — | — |
| 170 | PartyPEO_AliasAttribute30 | ATTRIBUTE30 | — | — |
| 171 | PartyPEO_AliasAttribute4 | ATTRIBUTE4 | — | — |
| 172 | PartyPEO_AliasAttribute5 | ATTRIBUTE5 | — | — |
| 173 | PartyPEO_AliasAttribute6 | ATTRIBUTE6 | — | — |
| 174 | PartyPEO_AliasAttribute7 | ATTRIBUTE7 | — | — |
| 175 | PartyPEO_AliasAttribute8 | ATTRIBUTE8 | — | — |
| 176 | PartyPEO_AliasAttribute9 | ATTRIBUTE9 | — | — |
| 177 | PartyPEO_AliasAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 178 | PartyPEO_AliasAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 179 | PartyPEO_AliasAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 180 | PartyPEO_AliasAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 181 | PartyPEO_AliasAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 182 | PartyPEO_AliasAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 183 | PartyPEO_AliasAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 184 | PartyPEO_AliasAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 185 | PartyPEO_AliasAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 186 | PartyPEO_AliasAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 187 | PartyPEO_AliasAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 188 | PartyPEO_AliasAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 189 | PartyPEO_AliasAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 190 | PartyPEO_AliasAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 191 | PartyPEO_AliasAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 192 | PartyPEO_AliasAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 193 | PartyPEO_AliasAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 194 | PartyPEO_AliasAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 195 | PartyPEO_AliasAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 196 | PartyPEO_AliasAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 197 | PartyPEO_AliasAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 198 | PartyPEO_AliasAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 199 | PartyPEO_AliasAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 200 | PartyPEO_AliasAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 201 | PartyPEO_AliasAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 202 | PartyPEO_AliasCategoryCode | CATEGORY_CODE | — | — |
| 203 | PartyPEO_AliasCeoName | CEO_NAME | — | — |
| 204 | PartyPEO_AliasCertReasonCode | CERT_REASON_CODE | — | — |
| 205 | PartyPEO_AliasCertificationLevel | CERTIFICATION_LEVEL | — | — |
| 206 | PartyPEO_AliasCity | CITY | — | — |
| 207 | PartyPEO_AliasComments | COMMENTS | — | — |
| 208 | PartyPEO_AliasCountry | COUNTRY | — | — |
| 209 | PartyPEO_AliasCounty | COUNTY | — | — |
| 210 | PartyPEO_AliasCreatedBy | CREATED_BY | — | — |
| 211 | PartyPEO_AliasCreatedByModule | CREATED_BY_MODULE | — | — |
| 212 | PartyPEO_AliasCreationDate | CREATION_DATE | — | — |
| 213 | PartyPEO_AliasCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 214 | PartyPEO_AliasDateOfBirth | DATE_OF_BIRTH | — | — |
| 215 | PartyPEO_AliasDunsNumberC | DUNS_NUMBER_C | — | — |
| 216 | PartyPEO_AliasEmailAddress | EMAIL_ADDRESS | — | — |
| 217 | PartyPEO_AliasEmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 218 | PartyPEO_AliasFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 219 | PartyPEO_AliasGender | GENDER | — | — |
| 220 | PartyPEO_AliasGroupType | GROUP_TYPE | — | — |
| 221 | PartyPEO_AliasGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | — |
| 222 | PartyPEO_AliasHomeCountry | HOME_COUNTRY | — | — |
| 223 | PartyPEO_AliasHqBranchInd | HQ_BRANCH_IND | — | — |
| 224 | PartyPEO_AliasIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 225 | PartyPEO_AliasIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | — |
| 226 | PartyPEO_AliasInternalFlag | INTERNAL_FLAG | — | — |
| 227 | PartyPEO_AliasJgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 228 | PartyPEO_AliasLanguageName | LANGUAGE_NAME | — | — |
| 229 | PartyPEO_AliasLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 230 | PartyPEO_AliasLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 231 | PartyPEO_AliasLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 232 | PartyPEO_AliasMaritalStatus | MARITAL_STATUS | — | — |
| 233 | PartyPEO_AliasMissionStatement | MISSION_STATEMENT | — | — |
| 234 | PartyPEO_AliasNextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 235 | PartyPEO_AliasObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 236 | PartyPEO_AliasOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 237 | PartyPEO_AliasPartyId | PARTY_ID | — | — |
| 238 | PartyPEO_AliasPartyName | PARTY_NAME | — | — |
| 239 | PartyPEO_AliasPartyNumber | PARTY_NUMBER | — | — |
| 240 | PartyPEO_AliasPartyType | PARTY_TYPE | — | — |
| 241 | PartyPEO_AliasPartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 242 | PartyPEO_AliasPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 243 | PartyPEO_AliasPersonFirstName | PERSON_FIRST_NAME | — | — |
| 244 | PartyPEO_AliasPersonLastName | PERSON_LAST_NAME | — | — |
| 245 | PartyPEO_AliasPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 246 | PartyPEO_AliasPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 247 | PartyPEO_AliasPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 248 | PartyPEO_AliasPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 249 | PartyPEO_AliasPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 250 | PartyPEO_AliasPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 251 | PartyPEO_AliasPersonTitle | PERSON_TITLE | — | — |
| 252 | PartyPEO_AliasPersonalAddressFlag | PERSONAL_ADDRESS_FLAG | — | — |
| 253 | PartyPEO_AliasPersonalEmailFlag | PERSONAL_EMAIL_FLAG | — | — |
| 254 | PartyPEO_AliasPersonalPhoneFlag | PERSONAL_PHONE_FLAG | — | — |
| 255 | PartyPEO_AliasPostalCode | POSTAL_CODE | — | — |
| 256 | PartyPEO_AliasPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 257 | PartyPEO_AliasPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 258 | PartyPEO_AliasPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 259 | PartyPEO_AliasPreferredName | PREFERRED_NAME | — | — |
| 260 | PartyPEO_AliasPreferredNameId | PREFERRED_NAME_ID | — | — |
| 261 | PartyPEO_AliasPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | — |
| 262 | PartyPEO_AliasPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 263 | PartyPEO_AliasPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 264 | PartyPEO_AliasPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 265 | PartyPEO_AliasPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 266 | PartyPEO_AliasPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 267 | PartyPEO_AliasPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | — |
| 268 | PartyPEO_AliasPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 269 | PartyPEO_AliasPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 270 | PartyPEO_AliasProvince | PROVINCE | — | — |
| 271 | PartyPEO_AliasRequestId | REQUEST_ID | — | — |
| 272 | PartyPEO_AliasSalutation | SALUTATION | — | — |
| 273 | PartyPEO_AliasSicCode | SIC_CODE | — | — |
| 274 | PartyPEO_AliasSicCodeType | SIC_CODE_TYPE | — | — |
| 275 | PartyPEO_AliasState | STATE | — | — |
| 276 | PartyPEO_AliasStatus | STATUS | — | — |
| 277 | PartyPEO_AliasThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 278 | PartyPEO_AliasTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 279 | PartyPEO_AliasUrl | URL | — | — |
| 280 | PartyPEO_AliasUserGuid | USER_GUID | — | — |
| 281 | PartyPEO_AliasValidatedFlag | VALIDATED_FLAG | — | — |
| 282 | PartyPEO_AliasYearEstablished | YEAR_ESTABLISHED | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
