---
id: DOC-OTHER-PVO-PSCInspectionPVO
doc_type: system-doc
title: "PSCInspectionPVO — PVO Cross-Module"
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
  - PSCInspectionPVO
  - pscinspectionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PSCInspectionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de PSCInspection. Acessa as tabelas: PER_PERSON_NAMES_F, PSC_BNP_BILL_TYPE_TL, PSC_INS_INSPECTION (+3).

**Caminho:** `FscmTopModelAM.PscPermitsReportingAM.PSCInspectionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 322 | 6 | 1 | 36 | 11% |

---

## 🔗 Tabelas Relacionadas

- [[per_person_names_f|PER_PERSON_NAMES_F]] — 160 atributos (1 BICC)
- [[psc_bnp_bill_type_tl|PSC_BNP_BILL_TYPE_TL]] — 11 atributos
- [[psc_ins_inspection|PSC_INS_INSPECTION]] — 91 atributos (1 PKs, 33 BICC)
- [[psc_ins_inspection_type_b|PSC_INS_INSPECTION_TYPE_B]] — 30 atributos
- [[psc_ins_inspect_status_b|PSC_INS_INSPECT_STATUS_B]] — 18 atributos (1 BICC)
- [[psc_ins_inspect_status_tl|PSC_INS_INSPECT_STATUS_TL]] — 12 atributos (1 BICC)

---

## ⚙️ Atributos

### [[per_person_names_f|PER_PERSON_NAMES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonProfileDPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | PersonProfileDPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | PersonProfileDPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | PersonProfileDPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | PersonProfileDPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | PersonProfileDPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | PersonProfileDPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | PersonProfileDPEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | PersonProfileDPEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | PersonProfileDPEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | PersonProfileDPEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | PersonProfileDPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | PersonProfileDPEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | PersonProfileDPEOAttribute21 | ATTRIBUTE21 | — | — |
| 15 | PersonProfileDPEOAttribute22 | ATTRIBUTE22 | — | — |
| 16 | PersonProfileDPEOAttribute23 | ATTRIBUTE23 | — | — |
| 17 | PersonProfileDPEOAttribute24 | ATTRIBUTE24 | — | — |
| 18 | PersonProfileDPEOAttribute25 | ATTRIBUTE25 | — | — |
| 19 | PersonProfileDPEOAttribute26 | ATTRIBUTE26 | — | — |
| 20 | PersonProfileDPEOAttribute27 | ATTRIBUTE27 | — | — |
| 21 | PersonProfileDPEOAttribute28 | ATTRIBUTE28 | — | — |
| 22 | PersonProfileDPEOAttribute29 | ATTRIBUTE29 | — | — |
| 23 | PersonProfileDPEOAttribute3 | ATTRIBUTE3 | — | — |
| 24 | PersonProfileDPEOAttribute30 | ATTRIBUTE30 | — | — |
| 25 | PersonProfileDPEOAttribute4 | ATTRIBUTE4 | — | — |
| 26 | PersonProfileDPEOAttribute5 | ATTRIBUTE5 | — | — |
| 27 | PersonProfileDPEOAttribute6 | ATTRIBUTE6 | — | — |
| 28 | PersonProfileDPEOAttribute7 | ATTRIBUTE7 | — | — |
| 29 | PersonProfileDPEOAttribute8 | ATTRIBUTE8 | — | — |
| 30 | PersonProfileDPEOAttribute9 | ATTRIBUTE9 | — | — |
| 31 | PersonProfileDPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 32 | PersonProfileDPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 33 | PersonProfileDPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 34 | PersonProfileDPEOAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 35 | PersonProfileDPEOAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 36 | PersonProfileDPEOAttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 37 | PersonProfileDPEOAttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 38 | PersonProfileDPEOAttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 39 | PersonProfileDPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 40 | PersonProfileDPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 41 | PersonProfileDPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 42 | PersonProfileDPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 43 | PersonProfileDPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 44 | PersonProfileDPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 45 | PersonProfileDPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 46 | PersonProfileDPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 47 | PersonProfileDPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 48 | PersonProfileDPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 49 | PersonProfileDPEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 50 | PersonProfileDPEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 51 | PersonProfileDPEOAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 52 | PersonProfileDPEOAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 53 | PersonProfileDPEOAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 54 | PersonProfileDPEOAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 55 | PersonProfileDPEOAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 56 | PersonProfileDPEOAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 57 | PersonProfileDPEOAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 58 | PersonProfileDPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 59 | PersonProfileDPEOAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 60 | PersonProfileDPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 61 | PersonProfileDPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 62 | PersonProfileDPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 63 | PersonProfileDPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 64 | PersonProfileDPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 65 | PersonProfileDPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 66 | PersonProfileDPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 67 | PersonProfileDPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 68 | PersonProfileDPEOCharSetContext | CHAR_SET_CONTEXT | — | — |
| 69 | PersonProfileDPEOCreatedBy | CREATED_BY | — | — |
| 70 | PersonProfileDPEOCreationDate | CREATION_DATE | — | — |
| 71 | PersonProfileDPEODisplayName | DISPLAY_NAME | — | ✅ |
| 72 | PersonProfileDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 73 | PersonProfileDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 74 | PersonProfileDPEOFirstName | FIRST_NAME | — | — |
| 75 | PersonProfileDPEOFullName | FULL_NAME | — | — |
| 76 | PersonProfileDPEOHonors | HONORS | — | — |
| 77 | PersonProfileDPEOKnownAs | KNOWN_AS | — | — |
| 78 | PersonProfileDPEOLastName | LAST_NAME | — | — |
| 79 | PersonProfileDPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 80 | PersonProfileDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 81 | PersonProfileDPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 82 | PersonProfileDPEOLegislationCode | LEGISLATION_CODE | — | — |
| 83 | PersonProfileDPEOListName | LIST_NAME | — | — |
| 84 | PersonProfileDPEOMiddleNames | MIDDLE_NAMES | — | — |
| 85 | PersonProfileDPEOMilitaryRank | MILITARY_RANK | — | — |
| 86 | PersonProfileDPEONamInformation1 | NAM_INFORMATION1 | — | — |
| 87 | PersonProfileDPEONamInformation10 | NAM_INFORMATION10 | — | — |
| 88 | PersonProfileDPEONamInformation11 | NAM_INFORMATION11 | — | — |
| 89 | PersonProfileDPEONamInformation12 | NAM_INFORMATION12 | — | — |
| 90 | PersonProfileDPEONamInformation13 | NAM_INFORMATION13 | — | — |
| 91 | PersonProfileDPEONamInformation14 | NAM_INFORMATION14 | — | — |
| 92 | PersonProfileDPEONamInformation15 | NAM_INFORMATION15 | — | — |
| 93 | PersonProfileDPEONamInformation16 | NAM_INFORMATION16 | — | — |
| 94 | PersonProfileDPEONamInformation17 | NAM_INFORMATION17 | — | — |
| 95 | PersonProfileDPEONamInformation18 | NAM_INFORMATION18 | — | — |
| 96 | PersonProfileDPEONamInformation19 | NAM_INFORMATION19 | — | — |
| 97 | PersonProfileDPEONamInformation2 | NAM_INFORMATION2 | — | — |
| 98 | PersonProfileDPEONamInformation20 | NAM_INFORMATION20 | — | — |
| 99 | PersonProfileDPEONamInformation21 | NAM_INFORMATION21 | — | — |
| 100 | PersonProfileDPEONamInformation22 | NAM_INFORMATION22 | — | — |
| 101 | PersonProfileDPEONamInformation23 | NAM_INFORMATION23 | — | — |
| 102 | PersonProfileDPEONamInformation24 | NAM_INFORMATION24 | — | — |
| 103 | PersonProfileDPEONamInformation25 | NAM_INFORMATION25 | — | — |
| 104 | PersonProfileDPEONamInformation26 | NAM_INFORMATION26 | — | — |
| 105 | PersonProfileDPEONamInformation27 | NAM_INFORMATION27 | — | — |
| 106 | PersonProfileDPEONamInformation28 | NAM_INFORMATION28 | — | — |
| 107 | PersonProfileDPEONamInformation29 | NAM_INFORMATION29 | — | — |
| 108 | PersonProfileDPEONamInformation3 | NAM_INFORMATION3 | — | — |
| 109 | PersonProfileDPEONamInformation30 | NAM_INFORMATION30 | — | — |
| 110 | PersonProfileDPEONamInformation4 | NAM_INFORMATION4 | — | — |
| 111 | PersonProfileDPEONamInformation5 | NAM_INFORMATION5 | — | — |
| 112 | PersonProfileDPEONamInformation6 | NAM_INFORMATION6 | — | — |
| 113 | PersonProfileDPEONamInformation7 | NAM_INFORMATION7 | — | — |
| 114 | PersonProfileDPEONamInformation8 | NAM_INFORMATION8 | — | — |
| 115 | PersonProfileDPEONamInformation9 | NAM_INFORMATION9 | — | — |
| 116 | PersonProfileDPEONamInformationCategory | NAM_INFORMATION_CATEGORY | — | — |
| 117 | PersonProfileDPEONamInformationDate1 | NAM_INFORMATION_DATE1 | — | — |
| 118 | PersonProfileDPEONamInformationDate10 | NAM_INFORMATION_DATE10 | — | — |
| 119 | PersonProfileDPEONamInformationDate11 | NAM_INFORMATION_DATE11 | — | — |
| 120 | PersonProfileDPEONamInformationDate12 | NAM_INFORMATION_DATE12 | — | — |
| 121 | PersonProfileDPEONamInformationDate13 | NAM_INFORMATION_DATE13 | — | — |
| 122 | PersonProfileDPEONamInformationDate14 | NAM_INFORMATION_DATE14 | — | — |
| 123 | PersonProfileDPEONamInformationDate15 | NAM_INFORMATION_DATE15 | — | — |
| 124 | PersonProfileDPEONamInformationDate2 | NAM_INFORMATION_DATE2 | — | — |
| 125 | PersonProfileDPEONamInformationDate3 | NAM_INFORMATION_DATE3 | — | — |
| 126 | PersonProfileDPEONamInformationDate4 | NAM_INFORMATION_DATE4 | — | — |
| 127 | PersonProfileDPEONamInformationDate5 | NAM_INFORMATION_DATE5 | — | — |
| 128 | PersonProfileDPEONamInformationDate6 | NAM_INFORMATION_DATE6 | — | — |
| 129 | PersonProfileDPEONamInformationDate7 | NAM_INFORMATION_DATE7 | — | — |
| 130 | PersonProfileDPEONamInformationDate8 | NAM_INFORMATION_DATE8 | — | — |
| 131 | PersonProfileDPEONamInformationDate9 | NAM_INFORMATION_DATE9 | — | — |
| 132 | PersonProfileDPEONamInformationNumber1 | NAM_INFORMATION_NUMBER1 | — | — |
| 133 | PersonProfileDPEONamInformationNumber10 | NAM_INFORMATION_NUMBER10 | — | — |
| 134 | PersonProfileDPEONamInformationNumber11 | NAM_INFORMATION_NUMBER11 | — | — |
| 135 | PersonProfileDPEONamInformationNumber12 | NAM_INFORMATION_NUMBER12 | — | — |
| 136 | PersonProfileDPEONamInformationNumber13 | NAM_INFORMATION_NUMBER13 | — | — |
| 137 | PersonProfileDPEONamInformationNumber14 | NAM_INFORMATION_NUMBER14 | — | — |
| 138 | PersonProfileDPEONamInformationNumber15 | NAM_INFORMATION_NUMBER15 | — | — |
| 139 | PersonProfileDPEONamInformationNumber16 | NAM_INFORMATION_NUMBER16 | — | — |
| 140 | PersonProfileDPEONamInformationNumber17 | NAM_INFORMATION_NUMBER17 | — | — |
| 141 | PersonProfileDPEONamInformationNumber18 | NAM_INFORMATION_NUMBER18 | — | — |
| 142 | PersonProfileDPEONamInformationNumber19 | NAM_INFORMATION_NUMBER19 | — | — |
| 143 | PersonProfileDPEONamInformationNumber2 | NAM_INFORMATION_NUMBER2 | — | — |
| 144 | PersonProfileDPEONamInformationNumber20 | NAM_INFORMATION_NUMBER20 | — | — |
| 145 | PersonProfileDPEONamInformationNumber3 | NAM_INFORMATION_NUMBER3 | — | — |
| 146 | PersonProfileDPEONamInformationNumber4 | NAM_INFORMATION_NUMBER4 | — | — |
| 147 | PersonProfileDPEONamInformationNumber5 | NAM_INFORMATION_NUMBER5 | — | — |
| 148 | PersonProfileDPEONamInformationNumber6 | NAM_INFORMATION_NUMBER6 | — | — |
| 149 | PersonProfileDPEONamInformationNumber7 | NAM_INFORMATION_NUMBER7 | — | — |
| 150 | PersonProfileDPEONamInformationNumber8 | NAM_INFORMATION_NUMBER8 | — | — |
| 151 | PersonProfileDPEONamInformationNumber9 | NAM_INFORMATION_NUMBER9 | — | — |
| 152 | PersonProfileDPEONameType | NAME_TYPE | — | — |
| 153 | PersonProfileDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 154 | PersonProfileDPEOOrderName | ORDER_NAME | — | — |
| 155 | PersonProfileDPEOPersonId | PERSON_ID | — | — |
| 156 | PersonProfileDPEOPersonNameId | PERSON_NAME_ID | — | — |
| 157 | PersonProfileDPEOPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 158 | PersonProfileDPEOPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 159 | PersonProfileDPEOSuffix | SUFFIX | — | — |
| 160 | PersonProfileDPEOTitle | TITLE | — | — |

### [[psc_bnp_bill_type_tl|PSC_BNP_BILL_TYPE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillTypeTLPEOAgencyId | AGENCY_ID | — | — |
| 2 | BillTypeTLPEOBillType | BILL_TYPE | — | — |
| 3 | BillTypeTLPEOCreatedBy | CREATED_BY | — | — |
| 4 | BillTypeTLPEOCreationDate | CREATION_DATE | — | — |
| 5 | BillTypeTLPEODescription | DESCRIPTION | — | — |
| 6 | BillTypeTLPEOLanguage | LANGUAGE | — | — |
| 7 | BillTypeTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | BillTypeTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | BillTypeTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | BillTypeTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | BillTypeTLPEOSourceLang | SOURCE_LANG | — | — |

### [[psc_ins_inspection|PSC_INS_INSPECTION]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InspectionPEOActlTravelTimeFromHrs | ACTL_TRAVEL_TIME_FROM_HRS | — | — |
| 2 | InspectionPEOActlTravelTimeToHrs | ACTL_TRAVEL_TIME_TO_HRS | — | — |
| 3 | InspectionPEOActualDurationHrs | ACTUAL_DURATION_HRS | — | — |
| 4 | InspectionPEOActualEndDttm | ACTUAL_END_DTTM | — | — |
| 5 | InspectionPEOActualStartDttm | ACTUAL_START_DTTM | — | — |
| 6 | InspectionPEOAddress1 | ADDRESS1 | — | ✅ |
| 7 | InspectionPEOAddress2 | ADDRESS2 | — | ✅ |
| 8 | InspectionPEOAddress3 | ADDRESS3 | — | — |
| 9 | InspectionPEOAddress4 | ADDRESS4 | — | — |
| 10 | InspectionPEOAddressId | ADDRESS_ID | — | — |
| 11 | InspectionPEOAgencyId | AGENCY_ID | — | — |
| 12 | InspectionPEOAssessFeeFlag | ASSESS_FEE_FLAG | — | — |
| 13 | InspectionPEOBillType | BILL_TYPE | — | — |
| 14 | InspectionPEOBillableFlag | BILLABLE_FLAG | — | — |
| 15 | InspectionPEOCancellationReason | CANCELLATION_REASON | — | — |
| 16 | InspectionPEOCity | CITY | — | ✅ |
| 17 | InspectionPEOContactEmail | CONTACT_EMAIL | — | ✅ |
| 18 | InspectionPEOContactName | CONTACT_NAME | — | ✅ |
| 19 | InspectionPEOContractorName | CONTRACTOR_NAME | — | — |
| 20 | InspectionPEOContractorSignature | CONTRACTOR_SIGNATURE | — | — |
| 21 | InspectionPEOContractorSignatureDttm | CONTRACTOR_SIGNATURE_DTTM | — | — |
| 22 | InspectionPEOCoordinateX | COORDINATE_X | — | — |
| 23 | InspectionPEOCoordinateY | COORDINATE_Y | — | — |
| 24 | InspectionPEOCountry | COUNTRY | — | ✅ |
| 25 | InspectionPEOCounty | COUNTY | — | ✅ |
| 26 | InspectionPEOCreatedBy | CREATED_BY | — | ✅ |
| 27 | InspectionPEOCreationDate | CREATION_DATE | — | ✅ |
| 28 | InspectionPEODescription | DESCRIPTION | — | ✅ |
| 29 | InspectionPEODistanceUom | DISTANCE_UOM | — | — |
| 30 | InspectionPEOEstimatedDurationHrs | ESTIMATED_DURATION_HRS | — | — |
| 31 | InspectionPEOEstimatedTimeArrival | ESTIMATED_TIME_ARRIVAL | — | — |
| 32 | InspectionPEOEstimatedTimeArrivalEnd | ESTIMATED_TIME_ARRIVAL_END | — | — |
| 33 | InspectionPEOFinalInspectionFlag | FINAL_INSPECTION_FLAG | — | ✅ |
| 34 | InspectionPEOHideInspectorComment | HIDE_INSPECTOR_COMMENT | — | — |
| 35 | InspectionPEOInspectionCompleteDttm | INSPECTION_COMPLETE_DTTM | — | — |
| 36 | InspectionPEOInspectionDistrictId | INSPECTION_DISTRICT_ID | — | — |
| 37 | InspectionPEOInspectionId | INSPECTION_ID | 🔑 | ✅ |
| 38 | InspectionPEOInspectionKey | INSPECTION_KEY | — | ✅ |
| 39 | InspectionPEOInspectionLocation | INSPECTION_LOCATION | — | ✅ |
| 40 | InspectionPEOInspectionRating | INSPECTION_RATING | — | ✅ |
| 41 | InspectionPEOInspectionResult | INSPECTION_RESULT | — | ✅ |
| 42 | InspectionPEOInspectionScore | INSPECTION_SCORE | — | ✅ |
| 43 | InspectionPEOInspectionSource | INSPECTION_SOURCE | — | — |
| 44 | InspectionPEOInspectionStatus | INSPECTION_STATUS | — | — |
| 45 | InspectionPEOInspectionType | INSPECTION_TYPE | — | — |
| 46 | InspectionPEOInspectorId | INSPECTOR_ID | — | — |
| 47 | InspectionPEOInspectorInitials | INSPECTOR_INITIALS | — | — |
| 48 | InspectionPEOInspectorName | INSPECTOR_NAME | — | — |
| 49 | InspectionPEOInspectorSignature | INSPECTOR_SIGNATURE | — | — |
| 50 | InspectionPEOInspectorSignatureDttm | INSPECTOR_SIGNATURE_DTTM | — | — |
| 51 | InspectionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 52 | InspectionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 53 | InspectionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 54 | InspectionPEOLnpRecordId | LNP_RECORD_ID | — | — |
| 55 | InspectionPEOLnpRecordKey | LNP_RECORD_KEY | — | ✅ |
| 56 | InspectionPEOLocationLatitude | LOCATION_LATITUDE | — | — |
| 57 | InspectionPEOLocationLongitude | LOCATION_LONGITUDE | — | — |
| 58 | InspectionPEOMigratedDataFlag | MIGRATED_DATA_FLAG | — | — |
| 59 | InspectionPEONumMajorViolations | NUM_MAJOR_VIOLATIONS | — | ✅ |
| 60 | InspectionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 61 | InspectionPEOOwnerName | OWNER_NAME | — | — |
| 62 | InspectionPEOOwnerSignature | OWNER_SIGNATURE | — | — |
| 63 | InspectionPEOOwnerSignatureDttm | OWNER_SIGNATURE_DTTM | — | — |
| 64 | InspectionPEOParcelId | PARCEL_ID | — | — |
| 65 | InspectionPEOPhoneAreaCode | PHONE_AREA_CODE | — | ✅ |
| 66 | InspectionPEOPhoneCountryCode | PHONE_COUNTRY_CODE | — | ✅ |
| 67 | InspectionPEOPhoneExtension | PHONE_EXTENSION | — | ✅ |
| 68 | InspectionPEOPhoneNumber | PHONE_NUMBER | — | ✅ |
| 69 | InspectionPEOPostalCode | POSTAL_CODE | — | ✅ |
| 70 | InspectionPEOPostalPlus4Code | POSTAL_PLUS4_CODE | — | — |
| 71 | InspectionPEOPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 72 | InspectionPEOPreferredDate | PREFERRED_DATE | — | ✅ |
| 73 | InspectionPEOPreferredTime | PREFERRED_TIME | — | ✅ |
| 74 | InspectionPEOProvince | PROVINCE | — | — |
| 75 | InspectionPEOReadyByDttm | READY_BY_DTTM | — | ✅ |
| 76 | InspectionPEOReinspectionFlag | REINSPECTION_FLAG | — | — |
| 77 | InspectionPEORequestorComment | REQUESTOR_COMMENT | — | — |
| 78 | InspectionPEORequiredFlag | REQUIRED_FLAG | — | — |
| 79 | InspectionPEOScheduledEndDttm | SCHEDULED_END_DTTM | — | ✅ |
| 80 | InspectionPEOScheduledStartDttm | SCHEDULED_START_DTTM | — | ✅ |
| 81 | InspectionPEOShape | SHAPE | — | — |
| 82 | InspectionPEOSrid | SRID | — | — |
| 83 | InspectionPEOState | STATE | — | ✅ |
| 84 | InspectionPEOSystemResult | SYSTEM_RESULT | — | — |
| 85 | InspectionPEOSystemStatus | SYSTEM_STATUS | — | ✅ |
| 86 | InspectionPEOTravelFromActualDistance | TRAVEL_FROM_ACTUAL_DISTANCE | — | — |
| 87 | InspectionPEOTravelFromEndOdometer | TRAVEL_FROM_END_ODOMETER | — | — |
| 88 | InspectionPEOTravelFromStartOdometer | TRAVEL_FROM_START_ODOMETER | — | — |
| 89 | InspectionPEOTravelToActualDistance | TRAVEL_TO_ACTUAL_DISTANCE | — | — |
| 90 | InspectionPEOTravelToEndOdometer | TRAVEL_TO_END_ODOMETER | — | — |
| 91 | InspectionPEOTravelToStartOdometer | TRAVEL_TO_START_ODOMETER | — | — |

### [[psc_ins_inspection_type_b|PSC_INS_INSPECTION_TYPE_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InspectionTypePEOAgencyId | AGENCY_ID | — | — |
| 2 | InspectionTypePEOAssessmentType | ASSESSMENT_TYPE | — | — |
| 3 | InspectionTypePEOAutonumberRuleId | AUTONUMBER_RULE_ID | — | — |
| 4 | InspectionTypePEOBillType | BILL_TYPE | — | — |
| 5 | InspectionTypePEOBillableFlag | BILLABLE_FLAG | — | — |
| 6 | InspectionTypePEOChecklistGroup | CHECKLIST_GROUP | — | — |
| 7 | InspectionTypePEOChecklistId | CHECKLIST_ID | — | — |
| 8 | InspectionTypePEOChgSchedulePolicyHrs | CHG_SCHEDULE_POLICY_HRS | — | — |
| 9 | InspectionTypePEOContractorSignatureOpt | CONTRACTOR_SIGNATURE_OPT | — | — |
| 10 | InspectionTypePEOCreatedBy | CREATED_BY | — | — |
| 11 | InspectionTypePEOCreationDate | CREATION_DATE | — | — |
| 12 | InspectionTypePEODistrictType | DISTRICT_TYPE | — | — |
| 13 | InspectionTypePEOEnabledFlag | ENABLED_FLAG | — | — |
| 14 | InspectionTypePEOEstimatedDurationHrs | ESTIMATED_DURATION_HRS | — | — |
| 15 | InspectionTypePEOHideInspectorComment | HIDE_INSPECTOR_COMMENT | — | — |
| 16 | InspectionTypePEOInspectionType | INSPECTION_TYPE | — | — |
| 17 | InspectionTypePEOInspectorSignatureOpt | INSPECTOR_SIGNATURE_OPT | — | — |
| 18 | InspectionTypePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 19 | InspectionTypePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | InspectionTypePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 21 | InspectionTypePEOMaxScore | MAX_SCORE | — | — |
| 22 | InspectionTypePEOModuleId | MODULE_ID | — | — |
| 23 | InspectionTypePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 24 | InspectionTypePEOOpaPolicyName | OPA_POLICY_NAME | — | — |
| 25 | InspectionTypePEOOpaPolicyVersion | OPA_POLICY_VERSION | — | — |
| 26 | InspectionTypePEOOwnerSignatureOpt | OWNER_SIGNATURE_OPT | — | — |
| 27 | InspectionTypePEOPassingRule | PASSING_RULE | — | — |
| 28 | InspectionTypePEORatingMethod | RATING_METHOD | — | — |
| 29 | InspectionTypePEOSchedulingMethod | SCHEDULING_METHOD | — | — |
| 30 | InspectionTypePEOScoringMethod | SCORING_METHOD | — | — |

### [[psc_ins_inspect_status_b|PSC_INS_INSPECT_STATUS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InspectionStatusPEOAgencyId | AGENCY_ID | — | — |
| 2 | InspectionStatusPEOCreatedBy | CREATED_BY | — | — |
| 3 | InspectionStatusPEOCreationDate | CREATION_DATE | — | — |
| 4 | InspectionStatusPEOCustom1 | CUSTOM1 | — | — |
| 5 | InspectionStatusPEOCustom2 | CUSTOM2 | — | — |
| 6 | InspectionStatusPEOCustom3 | CUSTOM3 | — | — |
| 7 | InspectionStatusPEOCustom4 | CUSTOM4 | — | — |
| 8 | InspectionStatusPEOCustom5 | CUSTOM5 | — | — |
| 9 | InspectionStatusPEODeletedFlag | DELETED_FLAG | — | — |
| 10 | InspectionStatusPEOInspectionStatus | INSPECTION_STATUS | — | ✅ |
| 11 | InspectionStatusPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 12 | InspectionStatusPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | InspectionStatusPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | InspectionStatusPEOModuleId | MODULE_ID | — | — |
| 15 | InspectionStatusPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | InspectionStatusPEOSeedDataLock | SEED_DATA_LOCK | — | — |
| 17 | InspectionStatusPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 18 | InspectionStatusPEOSystemStatus | SYSTEM_STATUS | — | — |

### [[psc_ins_inspect_status_tl|PSC_INS_INSPECT_STATUS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InspectionStatusTLPEOAgencyId | AGENCY_ID | — | — |
| 2 | InspectionStatusTLPEOCreatedBy | CREATED_BY | — | — |
| 3 | InspectionStatusTLPEOCreationDate | CREATION_DATE | — | — |
| 4 | InspectionStatusTLPEODescription | DESCRIPTION | — | ✅ |
| 5 | InspectionStatusTLPEOLanguage | LANGUAGE | — | — |
| 6 | InspectionStatusTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | InspectionStatusTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | InspectionStatusTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | InspectionStatusTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | InspectionStatusTLPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 11 | InspectionStatusTLPEOSourceLang | SOURCE_LANG | — | — |
| 12 | InspectionStatusTLPEOSystemStatus | SYSTEM_STATUS | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
