---
id: DOC-PO-PVO-RequisitionActionHistoryPVO
doc_type: system-doc
title: "RequisitionActionHistoryPVO — PVO Purchasing"
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
  - RequisitionActionHistoryPVO
  - requisitionactionhistorypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RequisitionActionHistoryPVO

## 📌 Visão Geral

Extrai o histórico de ações em requisições de compra (submissão, aprovação, rejeição, devolução), com datas e responsáveis. Permite auditoria do fluxo de aprovação e identificação de gargalos.

**Caminho:** `FscmTopModelAM.PrcPoPublicViewAM.RequisitionActionHistoryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 476 | 6 | 5 | 19 | 4% |

---

## 🔗 Tabelas Relacionadas

- [[hz_parties|HZ_PARTIES]] — 140 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 124 atributos (3 BICC)
- [[por_requisition_headers_all|POR_REQUISITION_HEADERS_ALL]] — 27 atributos (1 BICC)
- [[po_action_history|PO_ACTION_HISTORY]] — 23 atributos (5 PKs, 10 BICC)
- [[po_headers_all|PO_HEADERS_ALL]] — 114 atributos (1 BICC)
- [[po_versions|PO_VERSIONS]] — 48 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Address1 | ADDRESS1 | — | — |
| 2 | Address2 | ADDRESS2 | — | — |
| 3 | Address3 | ADDRESS3 | — | — |
| 4 | Address4 | ADDRESS4 | — | — |
| 5 | AnalysisFy | ANALYSIS_FY | — | — |
| 6 | Attribute101 | ATTRIBUTE10 | — | — |
| 7 | Attribute110 | ATTRIBUTE1 | — | — |
| 8 | Attribute111 | ATTRIBUTE11 | — | — |
| 9 | Attribute121 | ATTRIBUTE12 | — | — |
| 10 | Attribute131 | ATTRIBUTE13 | — | — |
| 11 | Attribute141 | ATTRIBUTE14 | — | — |
| 12 | Attribute151 | ATTRIBUTE15 | — | — |
| 13 | Attribute161 | ATTRIBUTE16 | — | — |
| 14 | Attribute171 | ATTRIBUTE17 | — | — |
| 15 | Attribute181 | ATTRIBUTE18 | — | — |
| 16 | Attribute191 | ATTRIBUTE19 | — | — |
| 17 | Attribute201 | ATTRIBUTE20 | — | — |
| 18 | Attribute210 | ATTRIBUTE2 | — | — |
| 19 | Attribute211 | ATTRIBUTE21 | — | — |
| 20 | Attribute221 | ATTRIBUTE22 | — | — |
| 21 | Attribute231 | ATTRIBUTE23 | — | — |
| 22 | Attribute241 | ATTRIBUTE24 | — | — |
| 23 | Attribute251 | ATTRIBUTE25 | — | — |
| 24 | Attribute261 | ATTRIBUTE26 | — | — |
| 25 | Attribute271 | ATTRIBUTE27 | — | — |
| 26 | Attribute281 | ATTRIBUTE28 | — | — |
| 27 | Attribute291 | ATTRIBUTE29 | — | — |
| 28 | Attribute301 | ATTRIBUTE30 | — | — |
| 29 | Attribute31 | ATTRIBUTE3 | — | — |
| 30 | Attribute41 | ATTRIBUTE4 | — | — |
| 31 | Attribute51 | ATTRIBUTE5 | — | — |
| 32 | Attribute61 | ATTRIBUTE6 | — | — |
| 33 | Attribute71 | ATTRIBUTE7 | — | — |
| 34 | Attribute81 | ATTRIBUTE8 | — | — |
| 35 | Attribute91 | ATTRIBUTE9 | — | — |
| 36 | AttributeCategory1 | ATTRIBUTE_CATEGORY | — | — |
| 37 | AttributeDate101 | ATTRIBUTE_DATE10 | — | — |
| 38 | AttributeDate111 | ATTRIBUTE_DATE11 | — | — |
| 39 | AttributeDate121 | ATTRIBUTE_DATE12 | — | — |
| 40 | AttributeDate16 | ATTRIBUTE_DATE1 | — | — |
| 41 | AttributeDate21 | ATTRIBUTE_DATE2 | — | — |
| 42 | AttributeDate31 | ATTRIBUTE_DATE3 | — | — |
| 43 | AttributeDate41 | ATTRIBUTE_DATE4 | — | — |
| 44 | AttributeDate51 | ATTRIBUTE_DATE5 | — | — |
| 45 | AttributeDate61 | ATTRIBUTE_DATE6 | — | — |
| 46 | AttributeDate71 | ATTRIBUTE_DATE7 | — | — |
| 47 | AttributeDate81 | ATTRIBUTE_DATE8 | — | — |
| 48 | AttributeDate91 | ATTRIBUTE_DATE9 | — | — |
| 49 | AttributeNumber101 | ATTRIBUTE_NUMBER10 | — | — |
| 50 | AttributeNumber110 | ATTRIBUTE_NUMBER1 | — | — |
| 51 | AttributeNumber111 | ATTRIBUTE_NUMBER11 | — | — |
| 52 | AttributeNumber121 | ATTRIBUTE_NUMBER12 | — | — |
| 53 | AttributeNumber21 | ATTRIBUTE_NUMBER2 | — | — |
| 54 | AttributeNumber31 | ATTRIBUTE_NUMBER3 | — | — |
| 55 | AttributeNumber41 | ATTRIBUTE_NUMBER4 | — | — |
| 56 | AttributeNumber51 | ATTRIBUTE_NUMBER5 | — | — |
| 57 | AttributeNumber61 | ATTRIBUTE_NUMBER6 | — | — |
| 58 | AttributeNumber71 | ATTRIBUTE_NUMBER7 | — | — |
| 59 | AttributeNumber81 | ATTRIBUTE_NUMBER8 | — | — |
| 60 | AttributeNumber91 | ATTRIBUTE_NUMBER9 | — | — |
| 61 | CategoryCode | CATEGORY_CODE | — | — |
| 62 | CeoName | CEO_NAME | — | — |
| 63 | CertReasonCode | CERT_REASON_CODE | — | — |
| 64 | CertificationLevel | CERTIFICATION_LEVEL | — | — |
| 65 | City | CITY | — | — |
| 66 | Comments | COMMENTS | — | — |
| 67 | Country | COUNTRY | — | — |
| 68 | County | COUNTY | — | — |
| 69 | CreatedBy1 | CREATED_BY | — | — |
| 70 | CreatedByModule | CREATED_BY_MODULE | — | — |
| 71 | CreationDate1 | CREATION_DATE | — | — |
| 72 | CurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 73 | DateOfBirth | DATE_OF_BIRTH | — | — |
| 74 | DunsNumberC | DUNS_NUMBER_C | — | — |
| 75 | EmailAddress | EMAIL_ADDRESS | — | — |
| 76 | EmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 77 | FiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 78 | Gender | GENDER | — | — |
| 79 | GroupType | GROUP_TYPE | — | — |
| 80 | GsaIndicatorFlag | GSA_INDICATOR_FLAG | — | — |
| 81 | HomeCountry | HOME_COUNTRY | — | — |
| 82 | HqBranchInd | HQ_BRANCH_IND | — | — |
| 83 | IdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 84 | IdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | — |
| 85 | InternalFlag | INTERNAL_FLAG | — | — |
| 86 | JgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 87 | LanguageName | LANGUAGE_NAME | — | — |
| 88 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 89 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 90 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 91 | MaritalStatus | MARITAL_STATUS | — | — |
| 92 | MissionStatement | MISSION_STATEMENT | — | — |
| 93 | NextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 94 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 95 | OrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 96 | PartyId | PARTY_ID | — | — |
| 97 | PartyName | PARTY_NAME | — | ✅ |
| 98 | PartyNumber | PARTY_NUMBER | — | — |
| 99 | PartyType | PARTY_TYPE | — | — |
| 100 | PartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 101 | PersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 102 | PersonFirstName | PERSON_FIRST_NAME | — | — |
| 103 | PersonLastName | PERSON_LAST_NAME | — | — |
| 104 | PersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 105 | PersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 106 | PersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 107 | PersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 108 | PersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 109 | PersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 110 | PersonTitle | PERSON_TITLE | — | — |
| 111 | PersonalAddressFlag | PERSONAL_ADDRESS_FLAG | — | — |
| 112 | PersonalEmailFlag | PERSONAL_EMAIL_FLAG | — | — |
| 113 | PersonalPhoneFlag | PERSONAL_PHONE_FLAG | — | — |
| 114 | PostalCode | POSTAL_CODE | — | — |
| 115 | PrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 116 | PreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 117 | PreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 118 | PreferredName | PREFERRED_NAME | — | — |
| 119 | PreferredNameId | PREFERRED_NAME_ID | — | — |
| 120 | PrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | — |
| 121 | PrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 122 | PrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 123 | PrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 124 | PrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 125 | PrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 126 | PrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | — |
| 127 | PrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 128 | PrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 129 | Province | PROVINCE | — | — |
| 130 | Salutation | SALUTATION | — | — |
| 131 | SicCode | SIC_CODE | — | — |
| 132 | SicCodeType | SIC_CODE_TYPE | — | — |
| 133 | State | STATE | — | — |
| 134 | Status | STATUS | — | — |
| 135 | ThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 136 | TradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 137 | Url | URL | — | — |
| 138 | UserGuid | USER_GUID | — | — |
| 139 | ValidatedFlag | VALIDATED_FLAG | — | — |
| 140 | YearEstablished | YEAR_ESTABLISHED | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute1 | ATTRIBUTE1 | — | — |
| 2 | Attribute10 | ATTRIBUTE10 | — | — |
| 3 | Attribute11 | ATTRIBUTE11 | — | — |
| 4 | Attribute12 | ATTRIBUTE12 | — | — |
| 5 | Attribute13 | ATTRIBUTE13 | — | — |
| 6 | Attribute14 | ATTRIBUTE14 | — | — |
| 7 | Attribute15 | ATTRIBUTE15 | — | — |
| 8 | Attribute16 | ATTRIBUTE16 | — | — |
| 9 | Attribute17 | ATTRIBUTE17 | — | — |
| 10 | Attribute18 | ATTRIBUTE18 | — | — |
| 11 | Attribute19 | ATTRIBUTE19 | — | — |
| 12 | Attribute2 | ATTRIBUTE2 | — | — |
| 13 | Attribute20 | ATTRIBUTE20 | — | — |
| 14 | Attribute21 | ATTRIBUTE21 | — | — |
| 15 | Attribute22 | ATTRIBUTE22 | — | — |
| 16 | Attribute23 | ATTRIBUTE23 | — | — |
| 17 | Attribute24 | ATTRIBUTE24 | — | — |
| 18 | Attribute25 | ATTRIBUTE25 | — | — |
| 19 | Attribute26 | ATTRIBUTE26 | — | — |
| 20 | Attribute27 | ATTRIBUTE27 | — | — |
| 21 | Attribute28 | ATTRIBUTE28 | — | — |
| 22 | Attribute29 | ATTRIBUTE29 | — | — |
| 23 | Attribute3 | ATTRIBUTE3 | — | — |
| 24 | Attribute30 | ATTRIBUTE30 | — | — |
| 25 | Attribute4 | ATTRIBUTE4 | — | — |
| 26 | Attribute5 | ATTRIBUTE5 | — | — |
| 27 | Attribute6 | ATTRIBUTE6 | — | — |
| 28 | Attribute7 | ATTRIBUTE7 | — | — |
| 29 | Attribute8 | ATTRIBUTE8 | — | — |
| 30 | Attribute9 | ATTRIBUTE9 | — | — |
| 31 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 32 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 33 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 34 | AttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 35 | AttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 36 | AttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 37 | AttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 38 | AttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 39 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 40 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 41 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 42 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 43 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 44 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 45 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 46 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 47 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 48 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 49 | AttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 50 | AttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 51 | AttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 52 | AttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 53 | AttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 54 | AttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 55 | AttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 56 | AttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 57 | AttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 58 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 59 | AttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 60 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 61 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 62 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 63 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 64 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 65 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 66 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 67 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 68 | CreatedBy | CREATED_BY | — | — |
| 69 | CreationDate | CREATION_DATE | — | — |
| 70 | DisplayName | DISPLAY_NAME | — | ✅ |
| 71 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 72 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 73 | FirstName | FIRST_NAME | — | — |
| 74 | FullName | FULL_NAME | — | — |
| 75 | Honors | HONORS | — | — |
| 76 | KnownAs | KNOWN_AS | — | — |
| 77 | LastName | LAST_NAME | — | — |
| 78 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 79 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 80 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 81 | LegislationCode | LEGISLATION_CODE | — | — |
| 82 | ListName | LIST_NAME | — | — |
| 83 | MiddleNames | MIDDLE_NAMES | — | — |
| 84 | MilitaryRank | MILITARY_RANK | — | — |
| 85 | NamInformation1 | NAM_INFORMATION1 | — | — |
| 86 | NamInformation10 | NAM_INFORMATION10 | — | — |
| 87 | NamInformation11 | NAM_INFORMATION11 | — | — |
| 88 | NamInformation12 | NAM_INFORMATION12 | — | — |
| 89 | NamInformation13 | NAM_INFORMATION13 | — | — |
| 90 | NamInformation14 | NAM_INFORMATION14 | — | — |
| 91 | NamInformation15 | NAM_INFORMATION15 | — | — |
| 92 | NamInformation16 | NAM_INFORMATION16 | — | — |
| 93 | NamInformation17 | NAM_INFORMATION17 | — | — |
| 94 | NamInformation18 | NAM_INFORMATION18 | — | — |
| 95 | NamInformation19 | NAM_INFORMATION19 | — | — |
| 96 | NamInformation2 | NAM_INFORMATION2 | — | — |
| 97 | NamInformation20 | NAM_INFORMATION20 | — | — |
| 98 | NamInformation21 | NAM_INFORMATION21 | — | — |
| 99 | NamInformation22 | NAM_INFORMATION22 | — | — |
| 100 | NamInformation23 | NAM_INFORMATION23 | — | — |
| 101 | NamInformation24 | NAM_INFORMATION24 | — | — |
| 102 | NamInformation25 | NAM_INFORMATION25 | — | — |
| 103 | NamInformation26 | NAM_INFORMATION26 | — | — |
| 104 | NamInformation27 | NAM_INFORMATION27 | — | — |
| 105 | NamInformation28 | NAM_INFORMATION28 | — | — |
| 106 | NamInformation29 | NAM_INFORMATION29 | — | — |
| 107 | NamInformation3 | NAM_INFORMATION3 | — | — |
| 108 | NamInformation30 | NAM_INFORMATION30 | — | — |
| 109 | NamInformation4 | NAM_INFORMATION4 | — | — |
| 110 | NamInformation5 | NAM_INFORMATION5 | — | — |
| 111 | NamInformation6 | NAM_INFORMATION6 | — | — |
| 112 | NamInformation7 | NAM_INFORMATION7 | — | — |
| 113 | NamInformation8 | NAM_INFORMATION8 | — | — |
| 114 | NamInformation9 | NAM_INFORMATION9 | — | — |
| 115 | NamInformationCategory | NAM_INFORMATION_CATEGORY | — | — |
| 116 | NameType | NAME_TYPE | — | — |
| 117 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 118 | OrderName | ORDER_NAME | — | — |
| 119 | PersonId | PERSON_ID | — | — |
| 120 | PersonNameId | PERSON_NAME_ID | — | — |
| 121 | PreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 122 | PreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 123 | Suffix | SUFFIX | — | — |
| 124 | Title | TITLE | — | — |

### [[por_requisition_headers_all|POR_REQUISITION_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequisitionHeaderActiveRequisitionFlag | ACTIVE_REQUISITION_FLAG | — | — |
| 2 | RequisitionHeaderApprovedDate | APPROVED_DATE | — | — |
| 3 | RequisitionHeaderChangePendingFlag | CHANGE_PENDING_FLAG | — | — |
| 4 | RequisitionHeaderCreatedBy | CREATED_BY | — | — |
| 5 | RequisitionHeaderCreationDate | CREATION_DATE | — | — |
| 6 | RequisitionHeaderDescription | DESCRIPTION | — | — |
| 7 | RequisitionHeaderDocumentStatus | DOCUMENT_STATUS | — | — |
| 8 | RequisitionHeaderEmergencyPoNumber | EMERGENCY_PO_NUMBER | — | — |
| 9 | RequisitionHeaderEmergencyReqFlag | EMERGENCY_REQ_FLAG | — | — |
| 10 | RequisitionHeaderInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 11 | RequisitionHeaderInterfaceSourceLineId | INTERFACE_SOURCE_LINE_ID | — | — |
| 12 | RequisitionHeaderJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 13 | RequisitionHeaderJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 14 | RequisitionHeaderJustification | JUSTIFICATION | — | — |
| 15 | RequisitionHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | RequisitionHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | RequisitionHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | RequisitionHeaderModifyingApproverId | MODIFYING_APPROVER_ID | — | — |
| 19 | RequisitionHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | RequisitionHeaderPcardId | PCARD_ID | — | — |
| 21 | RequisitionHeaderPrcBuId | PRC_BU_ID | — | — |
| 22 | RequisitionHeaderPreparerId | PREPARER_ID | — | — |
| 23 | RequisitionHeaderReqBuId | REQ_BU_ID | — | — |
| 24 | RequisitionHeaderRequestId | REQUEST_ID | — | — |
| 25 | RequisitionHeaderRequisitionHeaderId | REQUISITION_HEADER_ID | — | — |
| 26 | RequisitionHeaderRequisitionNumber | REQUISITION_NUMBER | — | — |
| 27 | RequisitionHeaderSubmissionDate | SUBMISSION_DATE | — | — |

### [[po_action_history|PO_ACTION_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectId | OBJECT_ID | 🔑 | ✅ |
| 2 | ObjectSubTypeCode | OBJECT_SUB_TYPE_CODE | 🔑 | ✅ |
| 3 | ObjectTypeCode | OBJECT_TYPE_CODE | 🔑 | ✅ |
| 4 | PurchasingActionHistoryActionCode | ACTION_CODE | 🔑 | ✅ |
| 5 | PurchasingActionHistoryActionDate | ACTION_DATE | — | ✅ |
| 6 | PurchasingActionHistoryActionLevel | ACTION_LEVEL | — | — |
| 7 | PurchasingActionHistoryAssignmentDate | ASSIGNMENT_DATE | — | ✅ |
| 8 | PurchasingActionHistoryCreatedBy | CREATED_BY | — | — |
| 9 | PurchasingActionHistoryCreationDate | CREATION_DATE | — | — |
| 10 | PurchasingActionHistoryIdentificationKey | IDENTIFICATION_KEY | — | — |
| 11 | PurchasingActionHistoryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | PurchasingActionHistoryLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | PurchasingActionHistoryLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | PurchasingActionHistoryNote | NOTE | — | ✅ |
| 15 | PurchasingActionHistoryObjectRevisionNum | OBJECT_REVISION_NUM | — | — |
| 16 | PurchasingActionHistoryObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | PurchasingActionHistoryOfflineCode | OFFLINE_CODE | — | — |
| 18 | PurchasingActionHistoryPerformerId | PERFORMER_ID | — | — |
| 19 | PurchasingActionHistoryPoVersionId | PO_VERSION_ID | — | — |
| 20 | PurchasingActionHistoryProgramDate | PROGRAM_DATE | — | — |
| 21 | PurchasingActionHistoryRoleCode | ROLE_CODE | — | ✅ |
| 22 | PurchasingActionHistorySupplierAccessibleFlag | SUPPLIER_ACCESSIBLE_FLAG | — | — |
| 23 | SequenceNum | SEQUENCE_NUM | 🔑 | ✅ |

### [[po_headers_all|PO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchasingDocumentHeaderAcceptanceDueDate | ACCEPTANCE_DUE_DATE | — | — |
| 2 | PurchasingDocumentHeaderAcceptanceRequiredFlag | ACCEPTANCE_REQUIRED_FLAG | — | — |
| 3 | PurchasingDocumentHeaderAcceptanceWithinDays | ACCEPTANCE_WITHIN_DAYS | — | — |
| 4 | PurchasingDocumentHeaderAgentId | AGENT_ID | — | — |
| 5 | PurchasingDocumentHeaderAmountLimit | AMOUNT_LIMIT | — | — |
| 6 | PurchasingDocumentHeaderAmountReleased | AMOUNT_RELEASED | — | — |
| 7 | PurchasingDocumentHeaderApprovedDate | APPROVED_DATE | — | — |
| 8 | PurchasingDocumentHeaderApprovedFlag | APPROVED_FLAG | — | — |
| 9 | PurchasingDocumentHeaderAutoSourcingFlag | AUTO_SOURCING_FLAG | — | — |
| 10 | PurchasingDocumentHeaderBillToLocationId | BILL_TO_LOCATION_ID | — | — |
| 11 | PurchasingDocumentHeaderBilltoBuId | BILLTO_BU_ID | — | — |
| 12 | PurchasingDocumentHeaderBlanketTotalAmount | BLANKET_TOTAL_AMOUNT | — | — |
| 13 | PurchasingDocumentHeaderCancelFlag | CANCEL_FLAG | — | — |
| 14 | PurchasingDocumentHeaderCarrierId | CARRIER_ID | — | — |
| 15 | PurchasingDocumentHeaderCatAdminAuthEnabledFlag | CAT_ADMIN_AUTH_ENABLED_FLAG | — | — |
| 16 | PurchasingDocumentHeaderCbcAccountingDate | CBC_ACCOUNTING_DATE | — | — |
| 17 | PurchasingDocumentHeaderChangeRequestedBy | CHANGE_REQUESTED_BY | — | — |
| 18 | PurchasingDocumentHeaderChangeSummary | CHANGE_SUMMARY | — | — |
| 19 | PurchasingDocumentHeaderClosedDate | CLOSED_DATE | — | — |
| 20 | PurchasingDocumentHeaderComments | COMMENTS | — | — |
| 21 | PurchasingDocumentHeaderConfirmingOrderFlag | CONFIRMING_ORDER_FLAG | — | — |
| 22 | PurchasingDocumentHeaderConsignedConsumptionFlag | CONSIGNED_CONSUMPTION_FLAG | — | — |
| 23 | PurchasingDocumentHeaderConsumeReqDemandFlag | CONSUME_REQ_DEMAND_FLAG | — | — |
| 24 | PurchasingDocumentHeaderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 25 | PurchasingDocumentHeaderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 26 | PurchasingDocumentHeaderContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 27 | PurchasingDocumentHeaderCpaReference | CPA_REFERENCE | — | — |
| 28 | PurchasingDocumentHeaderCreatedBy | CREATED_BY | — | — |
| 29 | PurchasingDocumentHeaderCreatedLanguage | CREATED_LANGUAGE | — | — |
| 30 | PurchasingDocumentHeaderCreationDate | CREATION_DATE | — | — |
| 31 | PurchasingDocumentHeaderCurrencyCode | CURRENCY_CODE | — | — |
| 32 | PurchasingDocumentHeaderCurrentVersionId | CURRENT_VERSION_ID | — | — |
| 33 | PurchasingDocumentHeaderDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 34 | PurchasingDocumentHeaderDocumentCreationMethod | DOCUMENT_CREATION_METHOD | — | — |
| 35 | PurchasingDocumentHeaderDocumentStatus | DOCUMENT_STATUS | — | — |
| 36 | PurchasingDocumentHeaderEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 37 | PurchasingDocumentHeaderEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 38 | PurchasingDocumentHeaderEmailAddress | EMAIL_ADDRESS | — | — |
| 39 | PurchasingDocumentHeaderEnabledFlag | ENABLED_FLAG | — | — |
| 40 | PurchasingDocumentHeaderEncumbranceRequiredFlag | ENCUMBRANCE_REQUIRED_FLAG | — | — |
| 41 | PurchasingDocumentHeaderEndDate | END_DATE | — | — |
| 42 | PurchasingDocumentHeaderFax | FAX | — | — |
| 43 | PurchasingDocumentHeaderFirmDate | FIRM_DATE | — | — |
| 44 | PurchasingDocumentHeaderFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 45 | PurchasingDocumentHeaderFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 46 | PurchasingDocumentHeaderFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 47 | PurchasingDocumentHeaderFromHeaderId | FROM_HEADER_ID | — | — |
| 48 | PurchasingDocumentHeaderFromTypeLookupCode | FROM_TYPE_LOOKUP_CODE | — | — |
| 49 | PurchasingDocumentHeaderFrozenFlag | FROZEN_FLAG | — | — |
| 50 | PurchasingDocumentHeaderGenerateOrdersAutomatic | GENERATE_ORDERS_AUTOMATIC | — | — |
| 51 | PurchasingDocumentHeaderGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 52 | PurchasingDocumentHeaderGroupRequisitionLines | GROUP_REQUISITION_LINES | — | — |
| 53 | PurchasingDocumentHeaderGroupRequisitions | GROUP_REQUISITIONS | — | — |
| 54 | PurchasingDocumentHeaderInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 55 | PurchasingDocumentHeaderJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 56 | PurchasingDocumentHeaderJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 57 | PurchasingDocumentHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 58 | PurchasingDocumentHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 59 | PurchasingDocumentHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 60 | PurchasingDocumentHeaderLastUpdatedProgram | LAST_UPDATED_PROGRAM | — | — |
| 61 | PurchasingDocumentHeaderMinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 62 | PurchasingDocumentHeaderNoteToAuthorizer | NOTE_TO_AUTHORIZER | — | — |
| 63 | PurchasingDocumentHeaderNoteToReceiver | NOTE_TO_RECEIVER | — | — |
| 64 | PurchasingDocumentHeaderNoteToVendor | NOTE_TO_VENDOR | — | — |
| 65 | PurchasingDocumentHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 66 | PurchasingDocumentHeaderOrchestrationOrderFlag | ORCHESTRATION_ORDER_FLAG | — | — |
| 67 | PurchasingDocumentHeaderPayOnCode | PAY_ON_CODE | — | — |
| 68 | PurchasingDocumentHeaderPcardId | PCARD_ID | — | — |
| 69 | PurchasingDocumentHeaderPendingSignatureFlag | PENDING_SIGNATURE_FLAG | — | — |
| 70 | PurchasingDocumentHeaderPoHeaderId | PO_HEADER_ID | — | — |
| 71 | PurchasingDocumentHeaderPrcBuId | PRC_BU_ID | — | — |
| 72 | PurchasingDocumentHeaderPriceUpdateTolerance | PRICE_UPDATE_TOLERANCE | — | — |
| 73 | PurchasingDocumentHeaderProgramAppName | PROGRAM_APP_NAME | — | — |
| 74 | PurchasingDocumentHeaderProgramName | PROGRAM_NAME | — | — |
| 75 | PurchasingDocumentHeaderRate | RATE | — | — |
| 76 | PurchasingDocumentHeaderRateDate | RATE_DATE | — | — |
| 77 | PurchasingDocumentHeaderRateType | RATE_TYPE | — | — |
| 78 | PurchasingDocumentHeaderReferenceNum | REFERENCE_NUM | — | — |
| 79 | PurchasingDocumentHeaderReleaseMethod | RELEASE_METHOD | — | — |
| 80 | PurchasingDocumentHeaderReqBuId | REQ_BU_ID | — | — |
| 81 | PurchasingDocumentHeaderRequestId | REQUEST_ID | — | — |
| 82 | PurchasingDocumentHeaderRetroPriceApplyUpdatesFlag | RETRO_PRICE_APPLY_UPDATES_FLAG | — | — |
| 83 | PurchasingDocumentHeaderRetroPriceCommUpdatesFlag | RETRO_PRICE_COMM_UPDATES_FLAG | — | — |
| 84 | PurchasingDocumentHeaderReviewAutogeneratedReleases | REVIEW_AUTOGENERATED_RELEASES | — | — |
| 85 | PurchasingDocumentHeaderRevisedDate | REVISED_DATE | — | — |
| 86 | PurchasingDocumentHeaderRevisionNum | REVISION_NUM | — | — |
| 87 | PurchasingDocumentHeaderSegment1 | SEGMENT1 | — | — |
| 88 | PurchasingDocumentHeaderSegment2 | SEGMENT2 | — | — |
| 89 | PurchasingDocumentHeaderSegment3 | SEGMENT3 | — | — |
| 90 | PurchasingDocumentHeaderSegment4 | SEGMENT4 | — | — |
| 91 | PurchasingDocumentHeaderSegment5 | SEGMENT5 | — | — |
| 92 | PurchasingDocumentHeaderShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 93 | PurchasingDocumentHeaderShippingControl | SHIPPING_CONTROL | — | — |
| 94 | PurchasingDocumentHeaderSoldtoLeId | SOLDTO_LE_ID | — | — |
| 95 | PurchasingDocumentHeaderStartDate | START_DATE | — | — |
| 96 | PurchasingDocumentHeaderStyleId | STYLE_ID | — | — |
| 97 | PurchasingDocumentHeaderSubmitApprovalAutomatic | SUBMIT_APPROVAL_AUTOMATIC | — | — |
| 98 | PurchasingDocumentHeaderSubmitDate | SUBMIT_DATE | — | — |
| 99 | PurchasingDocumentHeaderSummaryFlag | SUMMARY_FLAG | — | — |
| 100 | PurchasingDocumentHeaderSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | — |
| 101 | PurchasingDocumentHeaderTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 102 | PurchasingDocumentHeaderTaxDocumentSubtype | TAX_DOCUMENT_SUBTYPE | — | — |
| 103 | PurchasingDocumentHeaderTermsId | TERMS_ID | — | — |
| 104 | PurchasingDocumentHeaderTypeLookupCode | TYPE_LOOKUP_CODE | — | — |
| 105 | PurchasingDocumentHeaderUpdateSourcingRulesFlag | UPDATE_SOURCING_RULES_FLAG | — | — |
| 106 | PurchasingDocumentHeaderUseNeedByDate | USE_NEED_BY_DATE | — | — |
| 107 | PurchasingDocumentHeaderUseShipTo | USE_SHIP_TO | — | — |
| 108 | PurchasingDocumentHeaderVendorContactId | VENDOR_CONTACT_ID | — | — |
| 109 | PurchasingDocumentHeaderVendorId | VENDOR_ID | — | — |
| 110 | PurchasingDocumentHeaderVendorOrderNum | VENDOR_ORDER_NUM | — | — |
| 111 | PurchasingDocumentHeaderVendorSiteId | VENDOR_SITE_ID | — | — |
| 112 | PurchasingDocumentHeaderXmlChangeSendDate | XML_CHANGE_SEND_DATE | — | — |
| 113 | PurchasingDocumentHeaderXmlFlag | XML_FLAG | — | — |
| 114 | PurchasingDocumentHeaderXmlSendDate | XML_SEND_DATE | — | — |

### [[po_versions|PO_VERSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchasingDocumentVersionAcceptedDate | ACCEPTED_DATE | — | — |
| 2 | PurchasingDocumentVersionApprovedDate | APPROVED_DATE | — | — |
| 3 | PurchasingDocumentVersionBaseVersionId | BASE_VERSION_ID | — | — |
| 4 | PurchasingDocumentVersionCancelBackingReqFlag | CANCEL_BACKING_REQ_FLAG | — | — |
| 5 | PurchasingDocumentVersionCancelDocFlag | CANCEL_DOC_FLAG | — | — |
| 6 | PurchasingDocumentVersionChangeOrderDesc | CHANGE_ORDER_DESC | — | — |
| 7 | PurchasingDocumentVersionChangeOrderStatus | CHANGE_ORDER_STATUS | — | — |
| 8 | PurchasingDocumentVersionChangeOrderType | CHANGE_ORDER_TYPE | — | — |
| 9 | PurchasingDocumentVersionCoCanceledByRole | CO_CANCELED_BY_ROLE | — | — |
| 10 | PurchasingDocumentVersionCoCanceledByUserId | CO_CANCELED_BY_USER_ID | — | — |
| 11 | PurchasingDocumentVersionCoCanceledFlag | CO_CANCELED_FLAG | — | — |
| 12 | PurchasingDocumentVersionCoNum | CO_NUM | — | ✅ |
| 13 | PurchasingDocumentVersionCoSequence | CO_SEQUENCE | — | — |
| 14 | PurchasingDocumentVersionCommunicatedDate | COMMUNICATED_DATE | — | — |
| 15 | PurchasingDocumentVersionCommunicatedToSupplier | COMMUNICATED_TO_SUPPLIER | — | — |
| 16 | PurchasingDocumentVersionCounterproposalFlag | COUNTERPROPOSAL_FLAG | — | — |
| 17 | PurchasingDocumentVersionCreatedBy | CREATED_BY | — | — |
| 18 | PurchasingDocumentVersionCreatedByProgramName | CREATED_BY_PROGRAM_NAME | — | — |
| 19 | PurchasingDocumentVersionCreationDate | CREATION_DATE | — | — |
| 20 | PurchasingDocumentVersionDocumentDate | DOCUMENT_DATE | — | — |
| 21 | PurchasingDocumentVersionEsignEnvOwnerEmailId | ESIGN_ENV_OWNER_EMAIL_ID | — | — |
| 22 | PurchasingDocumentVersionEsignEnvelopeId | ESIGN_ENVELOPE_ID | — | — |
| 23 | PurchasingDocumentVersionEsignEnvelopeOwner | ESIGN_ENVELOPE_OWNER | — | — |
| 24 | PurchasingDocumentVersionEsignEnvelopeStatus | ESIGN_ENVELOPE_STATUS | — | — |
| 25 | PurchasingDocumentVersionExternalSystemFlag | EXTERNAL_SYSTEM_FLAG | — | — |
| 26 | PurchasingDocumentVersionFundsStatus | FUNDS_STATUS | — | — |
| 27 | PurchasingDocumentVersionJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 28 | PurchasingDocumentVersionJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 29 | PurchasingDocumentVersionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | PurchasingDocumentVersionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 31 | PurchasingDocumentVersionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 32 | PurchasingDocumentVersionModifiedFlag | MODIFIED_FLAG | — | — |
| 33 | PurchasingDocumentVersionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 34 | PurchasingDocumentVersionOnlineReportId | ONLINE_REPORT_ID | — | — |
| 35 | PurchasingDocumentVersionOriginatorId | ORIGINATOR_ID | — | — |
| 36 | PurchasingDocumentVersionOriginatorRole | ORIGINATOR_ROLE | — | — |
| 37 | PurchasingDocumentVersionPendingResponseRole | PENDING_RESPONSE_ROLE | — | — |
| 38 | PurchasingDocumentVersionPoHeaderId | PO_HEADER_ID | — | — |
| 39 | PurchasingDocumentVersionProcessedDate | PROCESSED_DATE | — | — |
| 40 | PurchasingDocumentVersionProgramAppName | PROGRAM_APP_NAME | — | — |
| 41 | PurchasingDocumentVersionProgramName | PROGRAM_NAME | — | — |
| 42 | PurchasingDocumentVersionRejectedFlag | REJECTED_FLAG | — | — |
| 43 | PurchasingDocumentVersionRequestDate | REQUEST_DATE | — | — |
| 44 | PurchasingDocumentVersionRequestId | REQUEST_ID | — | — |
| 45 | PurchasingDocumentVersionRevisionNum | REVISION_NUM | — | — |
| 46 | PurchasingDocumentVersionSubmittedDate | SUBMITTED_DATE | — | — |
| 47 | PurchasingDocumentVersionVersionId | VERSION_ID | — | — |
| 48 | PurchasingDocumentVersionWithdrawnFlag | WITHDRAWN_FLAG | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
