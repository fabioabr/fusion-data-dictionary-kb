---
id: DOC-OTHER-PVO-ContractDeliverable
doc_type: system-doc
title: "ContractDeliverable — PVO Cross-Module"
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
  - ContractDeliverable
  - contractdeliverable
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContractDeliverable

## 📌 Visão Geral

View Object para extração BICC de dados de Contract Deliverable. Acessa as tabelas: HR_ORGANIZATION_V, HZ_PARTIES, OKC_DELIVERABLES (+3).

**Caminho:** `FscmTopModelAM.ContractsCoreAM.ContractDeliverable`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 207 | 6 | 1 | 196 | 95% |

---

## 🔗 Tabelas Relacionadas

- [[hr_organization_v|HR_ORGANIZATION_V]] — 6 atributos (2 BICC)
- [[hz_parties|HZ_PARTIES]] — 82 atributos (80 BICC)
- [[okc_deliverables|OKC_DELIVERABLES]] — 67 atributos (1 PKs, 67 BICC)
- [[okc_deliverable_types_b|OKC_DELIVERABLE_TYPES_B]] — 8 atributos (8 BICC)
- [[okc_deliverable_types_tl|OKC_DELIVERABLE_TYPES_TL]] — 11 atributos (11 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 33 atributos (28 BICC)

---

## ⚙️ Atributos

### [[hr_organization_v|HR_ORGANIZATION_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InternalPartyClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | InternalPartyEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | InternalPartyEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | InternalPartyObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | InternalPartyOrgId | ORGANIZATION_ID | — | ✅ |
| 6 | InternlPartyName | NAME | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExternalPartyPEOPartyId | PARTY_ID | — | ✅ |
| 2 | ExternalPartyPEOPartyName | PARTY_NAME | — | ✅ |
| 3 | InternalPartyContactPartyPEOPartyId | PARTY_ID | — | — |
| 4 | InternalPartyContactPartyPEOPartyName | PARTY_NAME | — | — |
| 5 | PartyPEOAnalysisFy | ANALYSIS_FY | — | ✅ |
| 6 | PartyPEOCategoryCode | CATEGORY_CODE | — | ✅ |
| 7 | PartyPEOCeoName | CEO_NAME | — | ✅ |
| 8 | PartyPEOCertReasonCode | CERT_REASON_CODE | — | ✅ |
| 9 | PartyPEOCertificationLevel | CERTIFICATION_LEVEL | — | ✅ |
| 10 | PartyPEOCity | CITY | — | ✅ |
| 11 | PartyPEOComments | COMMENTS | — | ✅ |
| 12 | PartyPEOCountry | COUNTRY | — | ✅ |
| 13 | PartyPEOCounty | COUNTY | — | ✅ |
| 14 | PartyPEOCreatedBy | CREATED_BY | — | ✅ |
| 15 | PartyPEOCreatedByModule | CREATED_BY_MODULE | — | ✅ |
| 16 | PartyPEOCreationDate | CREATION_DATE | — | ✅ |
| 17 | PartyPEOCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | ✅ |
| 18 | PartyPEODateOfBirth | DATE_OF_BIRTH | — | ✅ |
| 19 | PartyPEODunsNumberC | DUNS_NUMBER_C | — | ✅ |
| 20 | PartyPEOEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 21 | PartyPEOEmployeesTotal | EMPLOYEES_TOTAL | — | ✅ |
| 22 | PartyPEOFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | ✅ |
| 23 | PartyPEOGender | GENDER | — | ✅ |
| 24 | PartyPEOGroupType | GROUP_TYPE | — | ✅ |
| 25 | PartyPEOGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | ✅ |
| 26 | PartyPEOHomeCountry | HOME_COUNTRY | — | ✅ |
| 27 | PartyPEOHqBranchInd | HQ_BRANCH_IND | — | ✅ |
| 28 | PartyPEOIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | ✅ |
| 29 | PartyPEOIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | ✅ |
| 30 | PartyPEOInternalFlag | INTERNAL_FLAG | — | ✅ |
| 31 | PartyPEOJgzzFiscalCode | JGZZ_FISCAL_CODE | — | ✅ |
| 32 | PartyPEOLanguageName | LANGUAGE_NAME | — | ✅ |
| 33 | PartyPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 34 | PartyPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 35 | PartyPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 36 | PartyPEOMaritalStatus | MARITAL_STATUS | — | ✅ |
| 37 | PartyPEOMissionStatement | MISSION_STATEMENT | — | ✅ |
| 38 | PartyPEONextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | ✅ |
| 39 | PartyPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 40 | PartyPEOOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | ✅ |
| 41 | PartyPEOPartyId | PARTY_ID | — | ✅ |
| 42 | PartyPEOPartyName | PARTY_NAME | — | ✅ |
| 43 | PartyPEOPartyNumber | PARTY_NUMBER | — | ✅ |
| 44 | PartyPEOPartyType | PARTY_TYPE | — | ✅ |
| 45 | PartyPEOPartyUniqueName | PARTY_UNIQUE_NAME | — | ✅ |
| 46 | PartyPEOPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | ✅ |
| 47 | PartyPEOPersonFirstName | PERSON_FIRST_NAME | — | ✅ |
| 48 | PartyPEOPersonLastName | PERSON_LAST_NAME | — | ✅ |
| 49 | PartyPEOPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | ✅ |
| 50 | PartyPEOPersonMiddleName | PERSON_MIDDLE_NAME | — | ✅ |
| 51 | PartyPEOPersonNameSuffix | PERSON_NAME_SUFFIX | — | ✅ |
| 52 | PartyPEOPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | ✅ |
| 53 | PartyPEOPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | ✅ |
| 54 | PartyPEOPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | ✅ |
| 55 | PartyPEOPersonTitle | PERSON_TITLE | — | ✅ |
| 56 | PartyPEOPostalCode | POSTAL_CODE | — | ✅ |
| 57 | PartyPEOPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | ✅ |
| 58 | PartyPEOPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | ✅ |
| 59 | PartyPEOPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | ✅ |
| 60 | PartyPEOPreferredName | PREFERRED_NAME | — | ✅ |
| 61 | PartyPEOPreferredNameId | PREFERRED_NAME_ID | — | ✅ |
| 62 | PartyPEOPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | ✅ |
| 63 | PartyPEOPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | ✅ |
| 64 | PartyPEOPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | ✅ |
| 65 | PartyPEOPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | ✅ |
| 66 | PartyPEOPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | ✅ |
| 67 | PartyPEOPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | ✅ |
| 68 | PartyPEOPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | ✅ |
| 69 | PartyPEOPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | ✅ |
| 70 | PartyPEOPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | ✅ |
| 71 | PartyPEOProvince | PROVINCE | — | ✅ |
| 72 | PartyPEOSalutation | SALUTATION | — | ✅ |
| 73 | PartyPEOSicCode | SIC_CODE | — | ✅ |
| 74 | PartyPEOSicCodeType | SIC_CODE_TYPE | — | ✅ |
| 75 | PartyPEOState | STATE | — | ✅ |
| 76 | PartyPEOStatus | STATUS | — | ✅ |
| 77 | PartyPEOThirdPartyFlag | THIRD_PARTY_FLAG | — | ✅ |
| 78 | PartyPEOTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | ✅ |
| 79 | PartyPEOUrl | URL | — | ✅ |
| 80 | PartyPEOUserGuid | USER_GUID | — | ✅ |
| 81 | PartyPEOValidatedFlag | VALIDATED_FLAG | — | ✅ |
| 82 | PartyPEOYearEstablished | YEAR_ESTABLISHED | — | ✅ |

### [[okc_deliverables|OKC_DELIVERABLES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractDeliverablePEOActualDueDate | ACTUAL_DUE_DATE | — | ✅ |
| 2 | ContractDeliverablePEOAmendmentOperation | AMENDMENT_OPERATION | — | ✅ |
| 3 | ContractDeliverablePEOBusinessDocumentId | BUSINESS_DOCUMENT_ID | — | ✅ |
| 4 | ContractDeliverablePEOBusinessDocumentLineId | BUSINESS_DOCUMENT_LINE_ID | — | ✅ |
| 5 | ContractDeliverablePEOBusinessDocumentNumber | BUSINESS_DOCUMENT_NUMBER | — | ✅ |
| 6 | ContractDeliverablePEOBusinessDocumentType | BUSINESS_DOCUMENT_TYPE | — | ✅ |
| 7 | ContractDeliverablePEOBusinessDocumentVersion | BUSINESS_DOCUMENT_VERSION | — | ✅ |
| 8 | ContractDeliverablePEOComments | COMMENTS | — | ✅ |
| 9 | ContractDeliverablePEOCompletedNotificationId | COMPLETED_NOTIFICATION_ID | — | ✅ |
| 10 | ContractDeliverablePEOContractTypeId | CONTRACT_TYPE_ID | — | ✅ |
| 11 | ContractDeliverablePEOCreatedBy | CREATED_BY | — | ✅ |
| 12 | ContractDeliverablePEOCreationDate | CREATION_DATE | — | ✅ |
| 13 | ContractDeliverablePEODeliverableLanguage | DELIVERABLE_LANGUAGE | — | ✅ |
| 14 | ContractDeliverablePEODeliverableName | DELIVERABLE_NAME | — | ✅ |
| 15 | ContractDeliverablePEODeliverableStatus | DELIVERABLE_STATUS | — | ✅ |
| 16 | ContractDeliverablePEODeliverableType | DELIVERABLE_TYPE | — | ✅ |
| 17 | ContractDeliverablePEODescription | DESCRIPTION | — | ✅ |
| 18 | ContractDeliverablePEODisableNotificationsYn | DISABLE_NOTIFICATIONS_YN | — | ✅ |
| 19 | ContractDeliverablePEODisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 20 | ContractDeliverablePEOEndEventDate | END_EVENT_DATE | — | ✅ |
| 21 | ContractDeliverablePEOEscalationAssignee | ESCALATION_ASSIGNEE | — | ✅ |
| 22 | ContractDeliverablePEOEscalationNotificationId | ESCALATION_NOTIFICATION_ID | — | ✅ |
| 23 | ContractDeliverablePEOExternalPartyContactId | EXTERNAL_PARTY_CONTACT_ID | — | ✅ |
| 24 | ContractDeliverablePEOExternalPartyId | EXTERNAL_PARTY_ID | — | ✅ |
| 25 | ContractDeliverablePEOExternalPartyRole | EXTERNAL_PARTY_ROLE | — | ✅ |
| 26 | ContractDeliverablePEOExternalPartySiteId | EXTERNAL_PARTY_SITE_ID | — | ✅ |
| 27 | ContractDeliverablePEOFixedDueDateYn | FIXED_DUE_DATE_YN | — | ✅ |
| 28 | ContractDeliverablePEOFixedEndDate | FIXED_END_DATE | — | ✅ |
| 29 | ContractDeliverablePEOFixedStartDate | FIXED_START_DATE | — | ✅ |
| 30 | ContractDeliverablePEOInternalPartyContactId | INTERNAL_PARTY_CONTACT_ID | — | ✅ |
| 31 | ContractDeliverablePEOInternalPartyId | INTERNAL_PARTY_ID | — | ✅ |
| 32 | ContractDeliverablePEOLastAmendmentDate | LAST_AMENDMENT_DATE | — | ✅ |
| 33 | ContractDeliverablePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 34 | ContractDeliverablePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 35 | ContractDeliverablePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 36 | ContractDeliverablePEOManageYn | MANAGE_YN | — | ✅ |
| 37 | ContractDeliverablePEOManuallyActivatedYn | MANUALLY_ACTIVATED_YN | — | ✅ |
| 38 | ContractDeliverablePEONotifyCompletedYn | NOTIFY_COMPLETED_YN | — | ✅ |
| 39 | ContractDeliverablePEONotifyEscalationUom | NOTIFY_ESCALATION_UOM | — | ✅ |
| 40 | ContractDeliverablePEONotifyEscalationValue | NOTIFY_ESCALATION_VALUE | — | ✅ |
| 41 | ContractDeliverablePEONotifyEscalationYn | NOTIFY_ESCALATION_YN | — | ✅ |
| 42 | ContractDeliverablePEONotifyOverdueYn | NOTIFY_OVERDUE_YN | — | ✅ |
| 43 | ContractDeliverablePEONotifyPriorDueDateUom | NOTIFY_PRIOR_DUE_DATE_UOM | — | ✅ |
| 44 | ContractDeliverablePEONotifyPriorDueDateValue | NOTIFY_PRIOR_DUE_DATE_VALUE | — | ✅ |
| 45 | ContractDeliverablePEONotifyPriorDueDateYn | NOTIFY_PRIOR_DUE_DATE_YN | — | ✅ |
| 46 | ContractDeliverablePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 47 | ContractDeliverablePEOOriginalDeliverableId | ORIGINAL_DELIVERABLE_ID | — | ✅ |
| 48 | ContractDeliverablePEOOverdueNotificationId | OVERDUE_NOTIFICATION_ID | — | ✅ |
| 49 | ContractDeliverablePEOPriorNotificationId | PRIOR_NOTIFICATION_ID | — | ✅ |
| 50 | ContractDeliverablePEORecurringDelParentId | RECURRING_DEL_PARENT_ID | — | ✅ |
| 51 | ContractDeliverablePEORecurringYn | RECURRING_YN | — | ✅ |
| 52 | ContractDeliverablePEORelativeEndDateDuration | RELATIVE_END_DATE_DURATION | — | ✅ |
| 53 | ContractDeliverablePEORelativeEndDateEventId | RELATIVE_END_DATE_EVENT_ID | — | ✅ |
| 54 | ContractDeliverablePEORelativeEndDateUom | RELATIVE_END_DATE_UOM | — | ✅ |
| 55 | ContractDeliverablePEORelativeStDateDuration | RELATIVE_ST_DATE_DURATION | — | ✅ |
| 56 | ContractDeliverablePEORelativeStDateEventId | RELATIVE_ST_DATE_EVENT_ID | — | ✅ |
| 57 | ContractDeliverablePEORelativeStDateUom | RELATIVE_ST_DATE_UOM | — | ✅ |
| 58 | ContractDeliverablePEORepeatingDayOfMonth | REPEATING_DAY_OF_MONTH | — | ✅ |
| 59 | ContractDeliverablePEORepeatingDayOfWeek | REPEATING_DAY_OF_WEEK | — | ✅ |
| 60 | ContractDeliverablePEORepeatingDuration | REPEATING_DURATION | — | ✅ |
| 61 | ContractDeliverablePEORepeatingFrequencyUom | REPEATING_FREQUENCY_UOM | — | ✅ |
| 62 | ContractDeliverablePEORequesterId | REQUESTER_ID | — | ✅ |
| 63 | ContractDeliverablePEOResponsibleParty | RESPONSIBLE_PARTY | — | ✅ |
| 64 | ContractDeliverablePEOStartEventDate | START_EVENT_DATE | — | ✅ |
| 65 | ContractDeliverablePEOStatusChangeNotes | STATUS_CHANGE_NOTES | — | ✅ |
| 66 | ContractDeliverablePEOSummaryAmendOperationCode | SUMMARY_AMEND_OPERATION_CODE | — | ✅ |
| 67 | DeliverableId | DELIVERABLE_ID | 🔑 | ✅ |

### [[okc_deliverable_types_b|OKC_DELIVERABLE_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractDeliverableTypeBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ContractDeliverableTypeBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ContractDeliverableTypeBasePEODeliverableTypeCode | DELIVERABLE_TYPE_CODE | — | ✅ |
| 4 | ContractDeliverableTypeBasePEOInternalFlag | INTERNAL_FLAG | — | ✅ |
| 5 | ContractDeliverableTypeBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ContractDeliverableTypeBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ContractDeliverableTypeBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ContractDeliverableTypeBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

### [[okc_deliverable_types_tl|OKC_DELIVERABLE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractDeliverableTypeTransPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ContractDeliverableTypeTransPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ContractDeliverableTypeTransPEODeliverableTypeCode | DELIVERABLE_TYPE_CODE | — | ✅ |
| 4 | ContractDeliverableTypeTransPEODescription | DESCRIPTION | — | ✅ |
| 5 | ContractDeliverableTypeTransPEOLanguage | LANGUAGE | — | ✅ |
| 6 | ContractDeliverableTypeTransPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ContractDeliverableTypeTransPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | ContractDeliverableTypeTransPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ContractDeliverableTypeTransPEOName | NAME | — | ✅ |
| 10 | ContractDeliverableTypeTransPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ContractDeliverableTypeTransPEOSourceLang | SOURCE_LANG | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | IPCPersonNamePEODisplayName | DISPLAY_NAME | — | ✅ |
| 4 | IPCPersonNamePEONameType | NAME_TYPE | — | — |
| 5 | PersonId | PERSON_ID | — | — |
| 6 | PersonNameId | PERSON_NAME_ID | — | ✅ |
| 7 | PersonNameId1 | PERSON_NAME_ID | — | — |
| 8 | PersonNamePEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 9 | PersonNamePEOCreatedBy | CREATED_BY | — | ✅ |
| 10 | PersonNamePEOCreationDate | CREATION_DATE | — | ✅ |
| 11 | PersonNamePEODisplayName | DISPLAY_NAME | — | ✅ |
| 12 | PersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 13 | PersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 14 | PersonNamePEOFirstName | FIRST_NAME | — | ✅ |
| 15 | PersonNamePEOFullName | FULL_NAME | — | ✅ |
| 16 | PersonNamePEOHonors | HONORS | — | ✅ |
| 17 | PersonNamePEOKnownAs | KNOWN_AS | — | ✅ |
| 18 | PersonNamePEOLastName | LAST_NAME | — | ✅ |
| 19 | PersonNamePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | PersonNamePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 21 | PersonNamePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 22 | PersonNamePEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 23 | PersonNamePEOListName | LIST_NAME | — | ✅ |
| 24 | PersonNamePEOMiddleNames | MIDDLE_NAMES | — | ✅ |
| 25 | PersonNamePEOMilitaryRank | MILITARY_RANK | — | ✅ |
| 26 | PersonNamePEONameType | NAME_TYPE | — | ✅ |
| 27 | PersonNamePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 28 | PersonNamePEOOrderName | ORDER_NAME | — | ✅ |
| 29 | PersonNamePEOPersonId | PERSON_ID | — | ✅ |
| 30 | PersonNamePEOPreNameAdjunct | PRE_NAME_ADJUNCT | — | ✅ |
| 31 | PersonNamePEOPreviousLastName | PREVIOUS_LAST_NAME | — | ✅ |
| 32 | PersonNamePEOSuffix | SUFFIX | — | ✅ |
| 33 | PersonNamePEOTitle | TITLE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
