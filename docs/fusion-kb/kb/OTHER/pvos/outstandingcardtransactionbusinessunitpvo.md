---
id: DOC-OTHER-PVO-OutstandingCardTransactionBusinessUnitPVO
doc_type: system-doc
title: "OutstandingCardTransactionBusinessUnitPVO — PVO Cross-Module"
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
  - OutstandingCardTransactionBusinessUnitPVO
  - outstandingcardtransactionbusinessunitpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OutstandingCardTransactionBusinessUnitPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Outstanding Card Transaction Business Unit. Acessa as tabelas: FND_SETID_SETS_VL, GL_LEDGERS, HR_ALL_ORGANIZATION_UNITS_F (+8).

**Caminho:** `FscmTopModelAM.FinFunBusinessUnitsAM.OutstandingCardTransactionBusinessUnitPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 194 | 11 | 3 | 14 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_setid_sets_vl|FND_SETID_SETS_VL]] — 4 atributos
- [[gl_ledgers|GL_LEDGERS]] — 59 atributos
- [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]] — 20 atributos (3 PKs, 5 BICC)
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 22 atributos (2 BICC)
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 11 atributos (1 BICC)
- [[hr_org_unit_classifications_f|HR_ORG_UNIT_CLASSIFICATIONS_F]] — 16 atributos (2 BICC)
- [[per_location_details_f|PER_LOCATION_DETAILS_F]] — 4 atributos (1 BICC)
- [[per_location_details_f_tl|PER_LOCATION_DETAILS_F_TL]] — 7 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 29 atributos (3 BICC)
- [[per_users|PER_USERS]] — 10 atributos
- [[xle_entity_profiles|XLE_ENTITY_PROFILES]] — 12 atributos

---

## ⚙️ Atributos

### [[fnd_setid_sets_vl|FND_SETID_SETS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SetIdSetsDescription | DESCRIPTION | — | — |
| 2 | SetIdSetsSetCode | SET_CODE | — | — |
| 3 | SetIdSetsSetId | SET_ID | — | — |
| 4 | SetIdSetsSetName | SET_NAME | — | — |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgerAccountedPeriodType | ACCOUNTED_PERIOD_TYPE | — | — |
| 2 | LedgerAlcLedgerTypeCode | ALC_LEDGER_TYPE_CODE | — | — |
| 3 | LedgerAllowIntercompanyPostFlag | ALLOW_INTERCOMPANY_POST_FLAG | — | — |
| 4 | LedgerAutomaticallyCreatedFlag | AUTOMATICALLY_CREATED_FLAG | — | — |
| 5 | LedgerAutorevAfterOpenPrdFlag | AUTOREV_AFTER_OPEN_PRD_FLAG | — | — |
| 6 | LedgerBalSegColumnName | BAL_SEG_COLUMN_NAME | — | — |
| 7 | LedgerBalSegValueOptionCode | BAL_SEG_VALUE_OPTION_CODE | — | — |
| 8 | LedgerBudgetPeriodAvgRateType | BUDGET_PERIOD_AVG_RATE_TYPE | — | — |
| 9 | LedgerBudgetPeriodEndRateType | BUDGET_PERIOD_END_RATE_TYPE | — | — |
| 10 | LedgerCompleteFlag | COMPLETE_FLAG | — | — |
| 11 | LedgerCompletionStatusCode | COMPLETION_STATUS_CODE | — | — |
| 12 | LedgerConsolidationLedgerFlag | CONSOLIDATION_LEDGER_FLAG | — | — |
| 13 | LedgerCreateJeFlag | CREATE_JE_FLAG | — | — |
| 14 | LedgerCurrencyCode | CURRENCY_CODE | — | — |
| 15 | LedgerDailyTranslationRateType | DAILY_TRANSLATION_RATE_TYPE | — | — |
| 16 | LedgerDescription | DESCRIPTION | — | — |
| 17 | LedgerEnableAutomaticTaxFlag | ENABLE_AUTOMATIC_TAX_FLAG | — | — |
| 18 | LedgerEnableAverageBalancesFlag | ENABLE_AVERAGE_BALANCES_FLAG | — | — |
| 19 | LedgerEnableBudgetaryControlFlag | ENABLE_BUDGETARY_CONTROL_FLAG | — | — |
| 20 | LedgerEnableJeApprovalFlag | ENABLE_JE_APPROVAL_FLAG | — | — |
| 21 | LedgerEnableReconciliationFlag | ENABLE_RECONCILIATION_FLAG | — | — |
| 22 | LedgerEnableRevalSsTrackFlag | ENABLE_REVAL_SS_TRACK_FLAG | — | — |
| 23 | LedgerEnableSecondaryTrackFlag | ENABLE_SECONDARY_TRACK_FLAG | — | — |
| 24 | LedgerFirstLedgerPeriodName | FIRST_LEDGER_PERIOD_NAME | — | — |
| 25 | LedgerFutureEnterablePeriodsLimit | FUTURE_ENTERABLE_PERIODS_LIMIT | — | — |
| 26 | LedgerJrnlsGroupByDateFlag | JRNLS_GROUP_BY_DATE_FLAG | — | — |
| 27 | LedgerLatestEncumbranceYear | LATEST_ENCUMBRANCE_YEAR | — | — |
| 28 | LedgerLatestOpenedPeriodName | LATEST_OPENED_PERIOD_NAME | — | — |
| 29 | LedgerLeLedgerTypeCode | LE_LEDGER_TYPE_CODE | — | — |
| 30 | LedgerLedgerAttributes | LEDGER_ATTRIBUTES | — | — |
| 31 | LedgerLedgerCategoryCode | LEDGER_CATEGORY_CODE | — | — |
| 32 | LedgerLedgerId | LEDGER_ID | — | — |
| 33 | LedgerMgtSegColumnName | MGT_SEG_COLUMN_NAME | — | — |
| 34 | LedgerMgtSegValueOptionCode | MGT_SEG_VALUE_OPTION_CODE | — | — |
| 35 | LedgerName | NAME | — | — |
| 36 | LedgerObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 37 | LedgerObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 38 | LedgerPeriodAverageRateType | PERIOD_AVERAGE_RATE_TYPE | — | — |
| 39 | LedgerPeriodEndRateType | PERIOD_END_RATE_TYPE | — | — |
| 40 | LedgerPeriodSetName | PERIOD_SET_NAME | — | — |
| 41 | LedgerPopUpStatAccountFlag | POP_UP_STAT_ACCOUNT_FLAG | — | — |
| 42 | LedgerPriorPrdNotificationFlag | PRIOR_PRD_NOTIFICATION_FLAG | — | — |
| 43 | LedgerRequireBudgetJournalsFlag | REQUIRE_BUDGET_JOURNALS_FLAG | — | — |
| 44 | LedgerRevalFromPriLgrCurr | REVAL_FROM_PRI_LGR_CURR | — | — |
| 45 | LedgerShortName | SHORT_NAME | — | — |
| 46 | LedgerSlaAccountingMethodCode | SLA_ACCOUNTING_METHOD_CODE | — | — |
| 47 | LedgerSlaAccountingMethodType | SLA_ACCOUNTING_METHOD_TYPE | — | — |
| 48 | LedgerSlaBalByLedgerCurrFlag | SLA_BAL_BY_LEDGER_CURR_FLAG | — | — |
| 49 | LedgerSlaDescriptionLanguage | SLA_DESCRIPTION_LANGUAGE | — | — |
| 50 | LedgerSlaLedgerCashBasisFlag | SLA_LEDGER_CASH_BASIS_FLAG | — | — |
| 51 | LedgerSlaSequencingFlag | SLA_SEQUENCING_FLAG | — | — |
| 52 | LedgerSuspenseAllowedFlag | SUSPENSE_ALLOWED_FLAG | — | — |
| 53 | LedgerThresholdAmount | THRESHOLD_AMOUNT | — | — |
| 54 | LedgerTrackRoundingImbalanceFlag | TRACK_ROUNDING_IMBALANCE_FLAG | — | — |
| 55 | LedgerTranslateEodFlag | TRANSLATE_EOD_FLAG | — | — |
| 56 | LedgerTranslateQatdFlag | TRANSLATE_QATD_FLAG | — | — |
| 57 | LedgerTranslateYatdFlag | TRANSLATE_YATD_FLAG | — | — |
| 58 | LedgerUssglOptionCode | USSGL_OPTION_CODE | — | — |
| 59 | LedgerValidateJournalRefDate | VALIDATE_JOURNAL_REF_DATE | — | — |

### [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitCreatedBy | CREATED_BY | — | — |
| 2 | BusinessUnitCreationDate | CREATION_DATE | — | ✅ |
| 3 | BusinessUnitDateFrom | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 4 | BusinessUnitDateTo | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 5 | BusinessUnitEnterpriseId | BUSINESS_GROUP_ID | — | — |
| 6 | BusinessUnitId | ORGANIZATION_ID | 🔑 | ✅ |
| 7 | BusinessUnitLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | BusinessUnitLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | BusinessUnitLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | BusinessUnitLocationId | LOCATION_ID | — | — |
| 11 | OrganizationUnitActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 12 | OrganizationUnitCostAllocationKeyflexId | COST_ALLOCATION_KEYFLEX_ID | — | — |
| 13 | OrganizationUnitCreatedBy | CREATED_BY | — | — |
| 14 | OrganizationUnitCreationDate | CREATION_DATE | — | — |
| 15 | OrganizationUnitEstablishmentId | ESTABLISHMENT_ID | — | — |
| 16 | OrganizationUnitInternalAddressLine | INTERNAL_ADDRESS_LINE | — | — |
| 17 | OrganizationUnitInternalExternalFlag | INTERNAL_EXTERNAL_FLAG | — | — |
| 18 | OrganizationUnitLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 19 | OrganizationUnitObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | OrganizationUnitType | TYPE | — | — |

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitDefaultCurrencyCode | ORG_INFORMATION8 | — | — |
| 2 | BusinessUnitDefaultSetId | ORG_INFORMATION4 | — | — |
| 3 | BusinessUnitEnabledForHrFlag | ORG_INFORMATION6 | — | — |
| 4 | BusinessUnitFinancialsBusinessUnitId | ORG_INFORMATION7 | — | — |
| 5 | BusinessUnitLegalEntityId | ORG_INFORMATION2 | — | — |
| 6 | BusinessUnitManagerId | ORG_INFORMATION1 | — | — |
| 7 | BusinessUnitPrimaryLedgerId | ORG_INFORMATION3 | — | — |
| 8 | OrganizationInformationActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 9 | OrganizationInformationBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 10 | OrganizationInformationCreatedBy | CREATED_BY | — | — |
| 11 | OrganizationInformationCreationDate | CREATION_DATE | — | — |
| 12 | OrganizationInformationEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 13 | OrganizationInformationEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 14 | OrganizationInformationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | OrganizationInformationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | OrganizationInformationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | OrganizationInformationLegislationCode | LEGISLATION_CODE | — | — |
| 18 | OrganizationInformationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | OrganizationInformationOrgInformation5 | ORG_INFORMATION5 | — | — |
| 20 | OrganizationInformationOrgInformation9 | ORG_INFORMATION9 | — | — |
| 21 | OrganizationInformationOrgInformationId | ORG_INFORMATION_ID | — | — |
| 22 | OrganizationInformationOrganizationId | ORGANIZATION_ID | — | — |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitName | NAME | — | — |
| 2 | FinBuBusinessUnitId | ORGANIZATION_ID | — | — |
| 3 | FinBuEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | FinBuEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 5 | FinBuLanguage | LANGUAGE | — | — |
| 6 | FinBuName | NAME | — | — |
| 7 | FinBuShortCode | NAME | — | — |
| 8 | OrganizationUnitTranslationEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 9 | OrganizationUnitTranslationEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 10 | OrganizationUnitTranslationLanguage | LANGUAGE | — | — |
| 11 | OrganizationUnitTranslationOrganizationId | ORGANIZATION_ID | — | — |

### [[hr_org_unit_classifications_f|HR_ORG_UNIT_CLASSIFICATIONS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitStatus | STATUS | — | — |
| 2 | OrgUnitClassificationActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 3 | OrgUnitClassificationBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | OrgUnitClassificationClassificationCode | CLASSIFICATION_CODE | — | — |
| 5 | OrgUnitClassificationCreatedBy | CREATED_BY | — | — |
| 6 | OrgUnitClassificationCreationDate | CREATION_DATE | — | — |
| 7 | OrgUnitClassificationEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | OrgUnitClassificationEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 9 | OrgUnitClassificationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | OrgUnitClassificationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | OrgUnitClassificationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | OrgUnitClassificationLegislationCode | LEGISLATION_CODE | — | — |
| 13 | OrgUnitClassificationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | OrgUnitClassificationOrgUnitClassificationId | ORG_UNIT_CLASSIFICATION_ID | — | — |
| 15 | OrgUnitClassificationOrganizationId | ORGANIZATION_ID | — | — |
| 16 | OrgUnitClassificationSetId | SET_ID | — | — |

### [[per_location_details_f|PER_LOCATION_DETAILS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocDetailsEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | LocDetailsEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | LocDetailsLocationDetailsId | LOCATION_DETAILS_ID | — | — |
| 4 | LocDetailsLocationId | LOCATION_ID | — | — |

### [[per_location_details_f_tl|PER_LOCATION_DETAILS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocDetailsDescription | DESCRIPTION | — | — |
| 2 | LocDetailsLocationCode | LOCATION_CODE | — | — |
| 3 | LocDetailsLocationName | LOCATION_NAME | — | — |
| 4 | LocDetailsTLEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 5 | LocDetailsTLEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 6 | LocDetailsTLLanguage | LANGUAGE | — | — |
| 7 | LocDetailsTLLocationDetailsId | LOCATION_DETAILS_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | — |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonRefDisplayName | DISPLAY_NAME | — | — |
| 7 | PersonRefEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PersonRefEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 9 | PersonRefFirstName | FIRST_NAME | — | — |
| 10 | PersonRefFullName | FULL_NAME | — | — |
| 11 | PersonRefHonors | HONORS | — | — |
| 12 | PersonRefKnownAs | KNOWN_AS | — | — |
| 13 | PersonRefLastName | LAST_NAME | — | — |
| 14 | PersonRefLegislationCode | LEGISLATION_CODE | — | — |
| 15 | PersonRefListName | LIST_NAME | — | — |
| 16 | PersonRefMiddleNames | MIDDLE_NAMES | — | — |
| 17 | PersonRefMilitaryRank | MILITARY_RANK | — | — |
| 18 | PersonRefNameType | NAME_TYPE | — | — |
| 19 | PersonRefOrderName | ORDER_NAME | — | — |
| 20 | PersonRefPersonNameId | PERSON_NAME_ID | — | — |
| 21 | PersonRefPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 22 | PersonRefPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 23 | PersonRefSuffix | SUFFIX | — | — |
| 24 | PersonRefTitle | TITLE | — | — |
| 25 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | — |
| 26 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 27 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 28 | PersonUpdatedByPersonId | PERSON_ID | — | — |
| 29 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | UserCreatedByPersonId | PERSON_ID | — | — |
| 3 | UserCreatedByUserGuid | USER_GUID | — | — |
| 4 | UserCreatedByUserId | USER_ID | — | — |
| 5 | UserCreatedByUsername | USERNAME | — | — |
| 6 | UserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 8 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 9 | UserUpdatedByUserId | USER_ID | — | — |
| 10 | UserUpdatedByUsername | USERNAME | — | — |

### [[xle_entity_profiles|XLE_ENTITY_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LegalEntityActivityCode | ACTIVITY_CODE | — | — |
| 2 | LegalEntityEffectiveFrom | EFFECTIVE_FROM | — | — |
| 3 | LegalEntityEffectiveTo | EFFECTIVE_TO | — | — |
| 4 | LegalEntityLegalEmployerFlag | LEGAL_EMPLOYER_FLAG | — | — |
| 5 | LegalEntityLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 6 | LegalEntityLegalEntityIdentifier | LEGAL_ENTITY_IDENTIFIER | — | — |
| 7 | LegalEntityName | NAME | — | — |
| 8 | LegalEntityObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | LegalEntityPsuFlag | PSU_FLAG | — | — |
| 10 | LegalEntitySubActivityCode | SUB_ACTIVITY_CODE | — | — |
| 11 | LegalEntityTransactingEntityFlag | TRANSACTING_ENTITY_FLAG | — | — |
| 12 | LegalEntityTypeOfCompany | TYPE_OF_COMPANY | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
