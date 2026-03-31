---
id: DOC-PO-PVO-SupplierSiteAssignmentsPVO
doc_type: system-doc
title: "SupplierSiteAssignmentsPVO — PVO Purchasing"
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
  - SupplierSiteAssignmentsPVO
  - suppliersiteassignmentspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierSiteAssignmentsPVO

## 📌 Visão Geral

Disponibiliza atribuições de sites de fornecedores por unidade de negócio para consulta, com condições de pagamento, ledger e configurações de faturamento. Garante uso de sites autorizados.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.SupplierSiteAssignmentsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 409 | 9 | 2 | 407 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ap_distribution_sets_all|AP_DISTRIBUTION_SETS_ALL]] — 12 atributos (12 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 40 atributos (40 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 80 atributos (80 BICC)
- [[hr_all_organization_units_f_vl|HR_ALL_ORGANIZATION_UNITS_F_VL]] — 4 atributos (2 BICC)
- [[hz_parties|HZ_PARTIES]] — 82 atributos (82 BICC)
- [[poz_site_assignments_all_m|POZ_SITE_ASSIGNMENTS_ALL_M]] — 28 atributos (1 PKs, 28 BICC)
- [[poz_suppliers|POZ_SUPPLIERS]] — 49 atributos (49 BICC)
- [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]] — 104 atributos (1 PKs, 104 BICC)
- [[zx_wht_tax_classification_v|ZX_WHT_TAX_CLASSIFICATION_V]] — 10 atributos (10 BICC)

---

## ⚙️ Atributos

### [[ap_distribution_sets_all|AP_DISTRIBUTION_SETS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApDistributionSetsAllCreatedBy | CREATED_BY | — | ✅ |
| 2 | ApDistributionSetsAllCreationDate | CREATION_DATE | — | ✅ |
| 3 | ApDistributionSetsAllDescription | DESCRIPTION | — | ✅ |
| 4 | ApDistributionSetsAllDistributionSetId | DISTRIBUTION_SET_ID | — | ✅ |
| 5 | ApDistributionSetsAllDistributionSetName | DISTRIBUTION_SET_NAME | — | ✅ |
| 6 | ApDistributionSetsAllInactiveDate | INACTIVE_DATE | — | ✅ |
| 7 | ApDistributionSetsAllLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ApDistributionSetsAllLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | ApDistributionSetsAllLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ApDistributionSetsAllObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ApDistributionSetsAllOrgId | ORG_ID | — | ✅ |
| 12 | ApDistributionSetsAllTotalPercentDistribution | TOTAL_PERCENT_DISTRIBUTION | — | ✅ |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillToBuBusinessUnitId | BU_ID | — | ✅ |
| 2 | BillToBuCreatedBy | CREATED_BY | — | ✅ |
| 3 | BillToBuCreationDate | CREATION_DATE | — | ✅ |
| 4 | BillToBuDateFrom | DATE_FROM | — | ✅ |
| 5 | BillToBuDateTo | DATE_TO | — | ✅ |
| 6 | BillToBuDefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | ✅ |
| 7 | BillToBuDefaultSetId | DEFAULT_SET_ID | — | ✅ |
| 8 | BillToBuEnabledForHrFlag | ENABLED_FOR_HR_FLAG | — | ✅ |
| 9 | BillToBuEnterpriseId | BUSINESS_GROUP_ID | — | ✅ |
| 10 | BillToBuFinancialsBusinessUnitId | FIN_BUSINESS_UNIT_ID | — | ✅ |
| 11 | BillToBuLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | BillToBuLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | BillToBuLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | BillToBuLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 15 | BillToBuLocationId | LOCATION_ID | — | ✅ |
| 16 | BillToBuManagerId | MANAGER_ID | — | ✅ |
| 17 | BillToBuName | BU_NAME | — | ✅ |
| 18 | BillToBuPrimaryLedgerId | PRIMARY_LEDGER_ID | — | ✅ |
| 19 | BillToBuShortCode | SHORT_CODE | — | ✅ |
| 20 | BillToBuStatus | STATUS | — | ✅ |
| 21 | ClientBuBusinessUnitId | BU_ID | — | ✅ |
| 22 | ClientBuCreatedBy | CREATED_BY | — | ✅ |
| 23 | ClientBuCreationDate | CREATION_DATE | — | ✅ |
| 24 | ClientBuDateFrom | DATE_FROM | — | ✅ |
| 25 | ClientBuDateTo | DATE_TO | — | ✅ |
| 26 | ClientBuDefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | ✅ |
| 27 | ClientBuDefaultSetId | DEFAULT_SET_ID | — | ✅ |
| 28 | ClientBuEnabledForHrFlag | ENABLED_FOR_HR_FLAG | — | ✅ |
| 29 | ClientBuEnterpriseId | BUSINESS_GROUP_ID | — | ✅ |
| 30 | ClientBuFinancialsBusinessUnitId | FIN_BUSINESS_UNIT_ID | — | ✅ |
| 31 | ClientBuLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | ClientBuLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 33 | ClientBuLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 34 | ClientBuLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 35 | ClientBuLocationId | LOCATION_ID | — | ✅ |
| 36 | ClientBuManagerId | MANAGER_ID | — | ✅ |
| 37 | ClientBuName | BU_NAME | — | ✅ |
| 38 | ClientBuPrimaryLedgerId | PRIMARY_LEDGER_ID | — | ✅ |
| 39 | ClientBuShortCode | SHORT_CODE | — | ✅ |
| 40 | ClientBuStatus | STATUS | — | ✅ |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlLedgersAccountedPeriodType | ACCOUNTED_PERIOD_TYPE | — | ✅ |
| 2 | GlLedgersAlcLedgerTypeCode | ALC_LEDGER_TYPE_CODE | — | ✅ |
| 3 | GlLedgersAllowIntercompanyPostFlag | ALLOW_INTERCOMPANY_POST_FLAG | — | ✅ |
| 4 | GlLedgersAutomaticallyCreatedFlag | AUTOMATICALLY_CREATED_FLAG | — | ✅ |
| 5 | GlLedgersAutorevAfterOpenPrdFlag | AUTOREV_AFTER_OPEN_PRD_FLAG | — | ✅ |
| 6 | GlLedgersBalSegColumnName | BAL_SEG_COLUMN_NAME | — | ✅ |
| 7 | GlLedgersBalSegValueOptionCode | BAL_SEG_VALUE_OPTION_CODE | — | ✅ |
| 8 | GlLedgersBalSegValueSetId | BAL_SEG_VALUE_SET_ID | — | ✅ |
| 9 | GlLedgersBudgetPeriodAvgRateType | BUDGET_PERIOD_AVG_RATE_TYPE | — | ✅ |
| 10 | GlLedgersBudgetPeriodEndRateType | BUDGET_PERIOD_END_RATE_TYPE | — | ✅ |
| 11 | GlLedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | ✅ |
| 12 | GlLedgersCompleteFlag | COMPLETE_FLAG | — | ✅ |
| 13 | GlLedgersCompletionStatusCode | COMPLETION_STATUS_CODE | — | ✅ |
| 14 | GlLedgersConfigurationId | CONFIGURATION_ID | — | ✅ |
| 15 | GlLedgersConsolidationLedgerFlag | CONSOLIDATION_LEDGER_FLAG | — | ✅ |
| 16 | GlLedgersCreateJeFlag | CREATE_JE_FLAG | — | ✅ |
| 17 | GlLedgersCreatedBy | CREATED_BY | — | ✅ |
| 18 | GlLedgersCreationDate | CREATION_DATE | — | ✅ |
| 19 | GlLedgersCriteriaSetId | CRITERIA_SET_ID | — | ✅ |
| 20 | GlLedgersCumTransCodeCombinationId | CUM_TRANS_CODE_COMBINATION_ID | — | ✅ |
| 21 | GlLedgersCurrencyCode | CURRENCY_CODE | — | ✅ |
| 22 | GlLedgersDailyTranslationRateType | DAILY_TRANSLATION_RATE_TYPE | — | ✅ |
| 23 | GlLedgersDescription | DESCRIPTION | — | ✅ |
| 24 | GlLedgersEnableAutomaticTaxFlag | ENABLE_AUTOMATIC_TAX_FLAG | — | ✅ |
| 25 | GlLedgersEnableAverageBalancesFlag | ENABLE_AVERAGE_BALANCES_FLAG | — | ✅ |
| 26 | GlLedgersEnableBudgetaryControlFlag | ENABLE_BUDGETARY_CONTROL_FLAG | — | ✅ |
| 27 | GlLedgersEnableJeApprovalFlag | ENABLE_JE_APPROVAL_FLAG | — | ✅ |
| 28 | GlLedgersEnableReconciliationFlag | ENABLE_RECONCILIATION_FLAG | — | ✅ |
| 29 | GlLedgersEnableRevalSsTrackFlag | ENABLE_REVAL_SS_TRACK_FLAG | — | ✅ |
| 30 | GlLedgersEnableSecondaryTrackFlag | ENABLE_SECONDARY_TRACK_FLAG | — | ✅ |
| 31 | GlLedgersFirstLedgerPeriodName | FIRST_LEDGER_PERIOD_NAME | — | ✅ |
| 32 | GlLedgersFutureEnterablePeriodsLimit | FUTURE_ENTERABLE_PERIODS_LIMIT | — | ✅ |
| 33 | GlLedgersImplicitAccessSetId | IMPLICIT_ACCESS_SET_ID | — | ✅ |
| 34 | GlLedgersImplicitLedgerSetId | IMPLICIT_LEDGER_SET_ID | — | ✅ |
| 35 | GlLedgersIntercoGainLossCcid | INTERCO_GAIN_LOSS_CCID | — | ✅ |
| 36 | GlLedgersJrnlsGroupByDateFlag | JRNLS_GROUP_BY_DATE_FLAG | — | ✅ |
| 37 | GlLedgersLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 38 | GlLedgersLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 39 | GlLedgersLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 40 | GlLedgersLatestEncumbranceYear | LATEST_ENCUMBRANCE_YEAR | — | ✅ |
| 41 | GlLedgersLatestOpenedPeriodName | LATEST_OPENED_PERIOD_NAME | — | ✅ |
| 42 | GlLedgersLeLedgerTypeCode | LE_LEDGER_TYPE_CODE | — | ✅ |
| 43 | GlLedgersLedgerAttributes | LEDGER_ATTRIBUTES | — | ✅ |
| 44 | GlLedgersLedgerCategoryCode | LEDGER_CATEGORY_CODE | — | ✅ |
| 45 | GlLedgersLedgerId | LEDGER_ID | — | ✅ |
| 46 | GlLedgersMgtSegColumnName | MGT_SEG_COLUMN_NAME | — | ✅ |
| 47 | GlLedgersMgtSegValueOptionCode | MGT_SEG_VALUE_OPTION_CODE | — | ✅ |
| 48 | GlLedgersMgtSegValueSetId | MGT_SEG_VALUE_SET_ID | — | ✅ |
| 49 | GlLedgersName | NAME | — | ✅ |
| 50 | GlLedgersNetIncomeCodeCombinationId | NET_INCOME_CODE_COMBINATION_ID | — | ✅ |
| 51 | GlLedgersObjectTypeCode | OBJECT_TYPE_CODE | — | ✅ |
| 52 | GlLedgersObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 53 | GlLedgersPeriodAverageRateType | PERIOD_AVERAGE_RATE_TYPE | — | ✅ |
| 54 | GlLedgersPeriodEndRateType | PERIOD_END_RATE_TYPE | — | ✅ |
| 55 | GlLedgersPeriodSetName | PERIOD_SET_NAME | — | ✅ |
| 56 | GlLedgersPopUpStatAccountFlag | POP_UP_STAT_ACCOUNT_FLAG | — | ✅ |
| 57 | GlLedgersPriorPrdNotificationFlag | PRIOR_PRD_NOTIFICATION_FLAG | — | ✅ |
| 58 | GlLedgersRequireBudgetJournalsFlag | REQUIRE_BUDGET_JOURNALS_FLAG | — | ✅ |
| 59 | GlLedgersResEncumbCodeCombinationId | RES_ENCUMB_CODE_COMBINATION_ID | — | ✅ |
| 60 | GlLedgersRetEarnCodeCombinationId | RET_EARN_CODE_COMBINATION_ID | — | ✅ |
| 61 | GlLedgersRevalFromPriLgrCurr | REVAL_FROM_PRI_LGR_CURR | — | ✅ |
| 62 | GlLedgersRoundingCodeCombinationId | ROUNDING_CODE_COMBINATION_ID | — | ✅ |
| 63 | GlLedgersShortName | SHORT_NAME | — | ✅ |
| 64 | GlLedgersSlaAccountingMethodCode | SLA_ACCOUNTING_METHOD_CODE | — | ✅ |
| 65 | GlLedgersSlaAccountingMethodType | SLA_ACCOUNTING_METHOD_TYPE | — | ✅ |
| 66 | GlLedgersSlaBalByLedgerCurrFlag | SLA_BAL_BY_LEDGER_CURR_FLAG | — | ✅ |
| 67 | GlLedgersSlaDescriptionLanguage | SLA_DESCRIPTION_LANGUAGE | — | ✅ |
| 68 | GlLedgersSlaEnteredCurBalSusCcid | SLA_ENTERED_CUR_BAL_SUS_CCID | — | ✅ |
| 69 | GlLedgersSlaLedgerCashBasisFlag | SLA_LEDGER_CASH_BASIS_FLAG | — | ✅ |
| 70 | GlLedgersSlaLedgerCurBalSusCcid | SLA_LEDGER_CUR_BAL_SUS_CCID | — | ✅ |
| 71 | GlLedgersSlaSequencingFlag | SLA_SEQUENCING_FLAG | — | ✅ |
| 72 | GlLedgersSuspenseAllowedFlag | SUSPENSE_ALLOWED_FLAG | — | ✅ |
| 73 | GlLedgersThresholdAmount | THRESHOLD_AMOUNT | — | ✅ |
| 74 | GlLedgersTrackRoundingImbalanceFlag | TRACK_ROUNDING_IMBALANCE_FLAG | — | ✅ |
| 75 | GlLedgersTransactionCalendarId | TRANSACTION_CALENDAR_ID | — | ✅ |
| 76 | GlLedgersTranslateEodFlag | TRANSLATE_EOD_FLAG | — | ✅ |
| 77 | GlLedgersTranslateQatdFlag | TRANSLATE_QATD_FLAG | — | ✅ |
| 78 | GlLedgersTranslateYatdFlag | TRANSLATE_YATD_FLAG | — | ✅ |
| 79 | GlLedgersUssglOptionCode | USSGL_OPTION_CODE | — | ✅ |
| 80 | GlLedgersValidateJournalRefDate | VALIDATE_JOURNAL_REF_DATE | — | ✅ |

### [[hr_all_organization_units_f_vl|HR_ALL_ORGANIZATION_UNITS_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitBusinessUnitId | ORGANIZATION_ID | — | ✅ |
| 2 | BusinessUnitName | NAME | — | ✅ |
| 3 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | EffectiveStartDate | EFFECTIVE_START_DATE | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupplierPartyAddress1 | ADDRESS1 | — | ✅ |
| 2 | SupplierPartyAddress2 | ADDRESS2 | — | ✅ |
| 3 | SupplierPartyAddress3 | ADDRESS3 | — | ✅ |
| 4 | SupplierPartyAddress4 | ADDRESS4 | — | ✅ |
| 5 | SupplierPartyAnalysisFy | ANALYSIS_FY | — | ✅ |
| 6 | SupplierPartyCategoryCode | CATEGORY_CODE | — | ✅ |
| 7 | SupplierPartyCeoName | CEO_NAME | — | ✅ |
| 8 | SupplierPartyCertReasonCode | CERT_REASON_CODE | — | ✅ |
| 9 | SupplierPartyCertificationLevel | CERTIFICATION_LEVEL | — | ✅ |
| 10 | SupplierPartyCity | CITY | — | ✅ |
| 11 | SupplierPartyComments | COMMENTS | — | ✅ |
| 12 | SupplierPartyCountry | COUNTRY | — | ✅ |
| 13 | SupplierPartyCounty | COUNTY | — | ✅ |
| 14 | SupplierPartyCreatedBy | CREATED_BY | — | ✅ |
| 15 | SupplierPartyCreatedByModule | CREATED_BY_MODULE | — | ✅ |
| 16 | SupplierPartyCreationDate | CREATION_DATE | — | ✅ |
| 17 | SupplierPartyCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | ✅ |
| 18 | SupplierPartyDateOfBirth | DATE_OF_BIRTH | — | ✅ |
| 19 | SupplierPartyDunsNumberC | DUNS_NUMBER_C | — | ✅ |
| 20 | SupplierPartyEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 21 | SupplierPartyEmployeesTotal | EMPLOYEES_TOTAL | — | ✅ |
| 22 | SupplierPartyFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | ✅ |
| 23 | SupplierPartyGender | GENDER | — | ✅ |
| 24 | SupplierPartyGroupType | GROUP_TYPE | — | ✅ |
| 25 | SupplierPartyGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | ✅ |
| 26 | SupplierPartyHomeCountry | HOME_COUNTRY | — | ✅ |
| 27 | SupplierPartyHqBranchInd | HQ_BRANCH_IND | — | ✅ |
| 28 | SupplierPartyIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | ✅ |
| 29 | SupplierPartyIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | ✅ |
| 30 | SupplierPartyInternalFlag | INTERNAL_FLAG | — | ✅ |
| 31 | SupplierPartyJgzzFiscalCode | JGZZ_FISCAL_CODE | — | ✅ |
| 32 | SupplierPartyLanguageName | LANGUAGE_NAME | — | ✅ |
| 33 | SupplierPartyLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 34 | SupplierPartyLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 35 | SupplierPartyLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 36 | SupplierPartyMaritalStatus | MARITAL_STATUS | — | ✅ |
| 37 | SupplierPartyMissionStatement | MISSION_STATEMENT | — | ✅ |
| 38 | SupplierPartyNextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | ✅ |
| 39 | SupplierPartyObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 40 | SupplierPartyOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | ✅ |
| 41 | SupplierPartyPartyId | PARTY_ID | — | ✅ |
| 42 | SupplierPartyPartyName | PARTY_NAME | — | ✅ |
| 43 | SupplierPartyPartyNumber | PARTY_NUMBER | — | ✅ |
| 44 | SupplierPartyPartyType | PARTY_TYPE | — | ✅ |
| 45 | SupplierPartyPartyUniqueName | PARTY_UNIQUE_NAME | — | ✅ |
| 46 | SupplierPartyPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | ✅ |
| 47 | SupplierPartyPersonFirstName | PERSON_FIRST_NAME | — | ✅ |
| 48 | SupplierPartyPersonLastName | PERSON_LAST_NAME | — | ✅ |
| 49 | SupplierPartyPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | ✅ |
| 50 | SupplierPartyPersonMiddleName | PERSON_MIDDLE_NAME | — | ✅ |
| 51 | SupplierPartyPersonNameSuffix | PERSON_NAME_SUFFIX | — | ✅ |
| 52 | SupplierPartyPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | ✅ |
| 53 | SupplierPartyPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | ✅ |
| 54 | SupplierPartyPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | ✅ |
| 55 | SupplierPartyPersonTitle | PERSON_TITLE | — | ✅ |
| 56 | SupplierPartyPostalCode | POSTAL_CODE | — | ✅ |
| 57 | SupplierPartyPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | ✅ |
| 58 | SupplierPartyPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | ✅ |
| 59 | SupplierPartyPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | ✅ |
| 60 | SupplierPartyPreferredName | PREFERRED_NAME | — | ✅ |
| 61 | SupplierPartyPreferredNameId | PREFERRED_NAME_ID | — | ✅ |
| 62 | SupplierPartyPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | ✅ |
| 63 | SupplierPartyPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | ✅ |
| 64 | SupplierPartyPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | ✅ |
| 65 | SupplierPartyPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | ✅ |
| 66 | SupplierPartyPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | ✅ |
| 67 | SupplierPartyPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | ✅ |
| 68 | SupplierPartyPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | ✅ |
| 69 | SupplierPartyPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | ✅ |
| 70 | SupplierPartyPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | ✅ |
| 71 | SupplierPartyProvince | PROVINCE | — | ✅ |
| 72 | SupplierPartySalutation | SALUTATION | — | ✅ |
| 73 | SupplierPartySicCode | SIC_CODE | — | ✅ |
| 74 | SupplierPartySicCodeType | SIC_CODE_TYPE | — | ✅ |
| 75 | SupplierPartyState | STATE | — | ✅ |
| 76 | SupplierPartyStatus | STATUS | — | ✅ |
| 77 | SupplierPartyThirdPartyFlag | THIRD_PARTY_FLAG | — | ✅ |
| 78 | SupplierPartyTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | ✅ |
| 79 | SupplierPartyUrl | URL | — | ✅ |
| 80 | SupplierPartyUserGuid | USER_GUID | — | ✅ |
| 81 | SupplierPartyValidatedFlag | VALIDATED_FLAG | — | ✅ |
| 82 | SupplierPartyYearEstablished | YEAR_ESTABLISHED | — | ✅ |

### [[poz_site_assignments_all_m|POZ_SITE_ASSIGNMENTS_ALL_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentId | ASSIGNMENT_ID | 🔑 | ✅ |
| 2 | SupplierSiteAssignmentsAcctsPayCodeCombinationId | ACCTS_PAY_CODE_COMBINATION_ID | — | ✅ |
| 3 | SupplierSiteAssignmentsAllowAwtFlag | ALLOW_AWT_FLAG | — | ✅ |
| 4 | SupplierSiteAssignmentsAssignmentSpkId | ASSIGNMENT_SPK_ID | — | ✅ |
| 5 | SupplierSiteAssignmentsAwtGroupId | AWT_GROUP_ID | — | ✅ |
| 6 | SupplierSiteAssignmentsBillToBuId | BILL_TO_BU_ID | — | ✅ |
| 7 | SupplierSiteAssignmentsBillToLocationId | BILL_TO_LOCATION_ID | — | ✅ |
| 8 | SupplierSiteAssignmentsBuId | BU_ID | — | ✅ |
| 9 | SupplierSiteAssignmentsCreatedBy | CREATED_BY | — | ✅ |
| 10 | SupplierSiteAssignmentsCreationDate | CREATION_DATE | — | ✅ |
| 11 | SupplierSiteAssignmentsDistributionSetId | DISTRIBUTION_SET_ID | — | ✅ |
| 12 | SupplierSiteAssignmentsEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 13 | SupplierSiteAssignmentsEffectiveSequence | EFFECTIVE_SEQUENCE | — | ✅ |
| 14 | SupplierSiteAssignmentsEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 15 | SupplierSiteAssignmentsFutureDatedPaymentCcid | FUTURE_DATED_PAYMENT_CCID | — | ✅ |
| 16 | SupplierSiteAssignmentsInactiveDate | INACTIVE_DATE | — | ✅ |
| 17 | SupplierSiteAssignmentsJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 18 | SupplierSiteAssignmentsJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 19 | SupplierSiteAssignmentsJobSubmissionDate | JOB_SUBMISSION_DATE | — | ✅ |
| 20 | SupplierSiteAssignmentsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | SupplierSiteAssignmentsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 22 | SupplierSiteAssignmentsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 23 | SupplierSiteAssignmentsMergeRequestId | MERGE_REQUEST_ID | — | ✅ |
| 24 | SupplierSiteAssignmentsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 25 | SupplierSiteAssignmentsPrepayCodeCombinationId | PREPAY_CODE_COMBINATION_ID | — | ✅ |
| 26 | SupplierSiteAssignmentsRequestId | REQUEST_ID | — | ✅ |
| 27 | SupplierSiteAssignmentsShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 28 | SupplierSiteAssignmentsVendorSiteId | VENDOR_SITE_ID | — | ✅ |

### [[poz_suppliers|POZ_SUPPLIERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupplierAllowAwtFlag | ALLOW_AWT_FLAG | — | ✅ |
| 2 | SupplierAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | ✅ |
| 3 | SupplierApTaxRoundingRule | AP_TAX_ROUNDING_RULE | — | ✅ |
| 4 | SupplierAutoTaxCalcFlag | AUTO_TAX_CALC_FLAG | — | ✅ |
| 5 | SupplierAutoTaxCalcOverride | AUTO_TAX_CALC_OVERRIDE | — | ✅ |
| 6 | SupplierAwtGroupId | AWT_GROUP_ID | — | ✅ |
| 7 | SupplierBusinessRelationship | BUSINESS_RELATIONSHIP | — | ✅ |
| 8 | SupplierCorporateWebsite | CORPORATE_WEBSITE | — | ✅ |
| 9 | SupplierCreatedBy | CREATED_BY | — | ✅ |
| 10 | SupplierCreationDate | CREATION_DATE | — | ✅ |
| 11 | SupplierCreationSource | CREATION_SOURCE | — | ✅ |
| 12 | SupplierCustomerNum | CUSTOMER_NUM | — | ✅ |
| 13 | SupplierEmployeeId | EMPLOYEE_ID | — | ✅ |
| 14 | SupplierEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 15 | SupplierFederalReportableFlag | FEDERAL_REPORTABLE_FLAG | — | ✅ |
| 16 | SupplierIncomeTaxIdFlag | INCOME_TAX_ID_FLAG | — | ✅ |
| 17 | SupplierLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | SupplierLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 19 | SupplierLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 20 | SupplierMinOrderAmount | MIN_ORDER_AMOUNT | — | ✅ |
| 21 | SupplierNameControl | NAME_CONTROL | — | ✅ |
| 22 | SupplierNiNumber | NI_NUMBER | — | ✅ |
| 23 | SupplierObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 24 | SupplierOffsetTaxFlag | OFFSET_TAX_FLAG | — | ✅ |
| 25 | SupplierOffsetVatCode | OFFSET_VAT_CODE | — | ✅ |
| 26 | SupplierOneTimeFlag | ONE_TIME_FLAG | — | ✅ |
| 27 | SupplierOrganizationTypeLookupCode | ORGANIZATION_TYPE_LOOKUP_CODE | — | ✅ |
| 28 | SupplierParentPartyId | PARENT_PARTY_ID | — | ✅ |
| 29 | SupplierParentVendorId | PARENT_VENDOR_ID | — | ✅ |
| 30 | SupplierPartyId | PARTY_ID | — | ✅ |
| 31 | SupplierProgramApplicationId | PROGRAM_APPLICATION_ID | — | ✅ |
| 32 | SupplierProgramId | PROGRAM_ID | — | ✅ |
| 33 | SupplierProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 34 | SupplierRequestId | REQUEST_ID | — | ✅ |
| 35 | SupplierReviewType | REVIEW_TYPE | — | ✅ |
| 36 | SupplierSegment1 | SEGMENT1 | — | ✅ |
| 37 | SupplierSpendAuthReviewStatus | SPEND_AUTH_REVIEW_STATUS | — | ✅ |
| 38 | SupplierStandardIndustryClass | STANDARD_INDUSTRY_CLASS | — | ✅ |
| 39 | SupplierStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 40 | SupplierStateReportableFlag | STATE_REPORTABLE_FLAG | — | ✅ |
| 41 | SupplierTaxReportingName | TAX_REPORTING_NAME | — | ✅ |
| 42 | SupplierTaxVerificationDate | TAX_VERIFICATION_DATE | — | ✅ |
| 43 | SupplierTaxpayerCountry | TAXPAYER_COUNTRY | — | ✅ |
| 44 | SupplierType1099 | TYPE_1099 | — | ✅ |
| 45 | SupplierVatCode | VAT_CODE | — | ✅ |
| 46 | SupplierVendorId | VENDOR_ID | — | ✅ |
| 47 | SupplierVendorTypeLookupCode | VENDOR_TYPE_LOOKUP_CODE | — | ✅ |
| 48 | SupplierWithholdingStartDate | WITHHOLDING_START_DATE | — | ✅ |
| 49 | SupplierWithholdingStatusLookupCode | WITHHOLDING_STATUS_LOOKUP_CODE | — | ✅ |

### [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupplierSiteAllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | ✅ |
| 2 | SupplierSiteAllowUnorderedReceiptsFlag | ALLOW_UNORDERED_RECEIPTS_FLAG | — | ✅ |
| 3 | SupplierSiteAlwaysTakeDiscFlag | ALWAYS_TAKE_DISC_FLAG | — | ✅ |
| 4 | SupplierSiteAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | ✅ |
| 5 | SupplierSiteApTaxRoundingRule | AP_TAX_ROUNDING_RULE | — | ✅ |
| 6 | SupplierSiteAreaCode | AREA_CODE | — | ✅ |
| 7 | SupplierSiteAttentionArFlag | ATTENTION_AR_FLAG | — | ✅ |
| 8 | SupplierSiteAutoCalculateInterestFlag | AUTO_CALCULATE_INTEREST_FLAG | — | ✅ |
| 9 | SupplierSiteAutoTaxCalcFlag | AUTO_TAX_CALC_FLAG | — | ✅ |
| 10 | SupplierSiteAutoTaxCalcOverride | AUTO_TAX_CALC_OVERRIDE | — | ✅ |
| 11 | SupplierSiteB2bSiteCode | B2B_SITE_CODE | — | ✅ |
| 12 | SupplierSiteBankChargeBearer | BANK_CHARGE_BEARER | — | ✅ |
| 13 | SupplierSiteCarrierId | CARRIER_ID | — | ✅ |
| 14 | SupplierSiteCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | ✅ |
| 15 | SupplierSiteCreateDebitMemoFlag | CREATE_DEBIT_MEMO_FLAG | — | ✅ |
| 16 | SupplierSiteCreatedBy | CREATED_BY | — | ✅ |
| 17 | SupplierSiteCreationDate | CREATION_DATE | — | ✅ |
| 18 | SupplierSiteCustomerNum | CUSTOMER_NUM | — | ✅ |
| 19 | SupplierSiteDaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | ✅ |
| 20 | SupplierSiteDaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | ✅ |
| 21 | SupplierSiteDefaultPaySiteId | DEFAULT_PAY_SITE_ID | — | ✅ |
| 22 | SupplierSiteEceTpLocationCode | ECE_TP_LOCATION_CODE | — | ✅ |
| 23 | SupplierSiteEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 24 | SupplierSiteEffectiveSequence | EFFECTIVE_SEQUENCE | — | ✅ |
| 25 | SupplierSiteEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 26 | SupplierSiteEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 27 | SupplierSiteEnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | ✅ |
| 28 | SupplierSiteExcludeFreightFromDiscount | EXCLUDE_FREIGHT_FROM_DISCOUNT | — | ✅ |
| 29 | SupplierSiteExcludeTaxFromDiscount | EXCLUDE_TAX_FROM_DISCOUNT | — | ✅ |
| 30 | SupplierSiteFax | FAX | — | ✅ |
| 31 | SupplierSiteFaxAreaCode | FAX_AREA_CODE | — | ✅ |
| 32 | SupplierSiteFaxCountryCode | FAX_COUNTRY_CODE | — | ✅ |
| 33 | SupplierSiteFobLookupCode | FOB_LOOKUP_CODE | — | ✅ |
| 34 | SupplierSiteFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | ✅ |
| 35 | SupplierSiteGaplessInvNumFlag | GAPLESS_INV_NUM_FLAG | — | ✅ |
| 36 | SupplierSiteHoldAllPaymentsFlag | HOLD_ALL_PAYMENTS_FLAG | — | ✅ |
| 37 | SupplierSiteHoldBy | HOLD_BY | — | ✅ |
| 38 | SupplierSiteHoldDate | HOLD_DATE | — | ✅ |
| 39 | SupplierSiteHoldFlag | HOLD_FLAG | — | ✅ |
| 40 | SupplierSiteHoldFuturePaymentsFlag | HOLD_FUTURE_PAYMENTS_FLAG | — | ✅ |
| 41 | SupplierSiteHoldReason | HOLD_REASON | — | ✅ |
| 42 | SupplierSiteHoldUnmatchedInvoicesFlag | HOLD_UNMATCHED_INVOICES_FLAG | — | ✅ |
| 43 | SupplierSiteInactiveDate | INACTIVE_DATE | — | ✅ |
| 44 | SupplierSiteInspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | ✅ |
| 45 | SupplierSiteInvoiceAmountLimit | INVOICE_AMOUNT_LIMIT | — | ✅ |
| 46 | SupplierSiteInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 47 | SupplierSiteJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 48 | SupplierSiteJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 49 | SupplierSiteLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 50 | SupplierSiteLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 51 | SupplierSiteLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 52 | SupplierSiteLocationId | LOCATION_ID | — | ✅ |
| 53 | SupplierSiteMatchOption | MATCH_OPTION | — | ✅ |
| 54 | SupplierSiteObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 55 | SupplierSiteOffsetTaxFlag | OFFSET_TAX_FLAG | — | ✅ |
| 56 | SupplierSiteOffsetVatCode | OFFSET_VAT_CODE | — | ✅ |
| 57 | SupplierSitePartySiteId | PARTY_SITE_ID | — | ✅ |
| 58 | SupplierSitePayDateBasisLookupCode | PAY_DATE_BASIS_LOOKUP_CODE | — | ✅ |
| 59 | SupplierSitePayGroupLookupCode | PAY_GROUP_LOOKUP_CODE | — | ✅ |
| 60 | SupplierSitePayOnCode | PAY_ON_CODE | — | ✅ |
| 61 | SupplierSitePayOnReceiptSummaryCode | PAY_ON_RECEIPT_SUMMARY_CODE | — | ✅ |
| 62 | SupplierSitePaySiteFlag | PAY_SITE_FLAG | — | ✅ |
| 63 | SupplierSitePaymentCurrencyCode | PAYMENT_CURRENCY_CODE | — | ✅ |
| 64 | SupplierSitePaymentHoldDate | PAYMENT_HOLD_DATE | — | ✅ |
| 65 | SupplierSitePaymentPriority | PAYMENT_PRIORITY | — | ✅ |
| 66 | SupplierSitePcardSiteFlag | PCARD_SITE_FLAG | — | ✅ |
| 67 | SupplierSitePhone | PHONE | — | ✅ |
| 68 | SupplierSitePhoneCountryCode | PHONE_COUNTRY_CODE | — | ✅ |
| 69 | SupplierSitePhoneExtension | PHONE_EXTENSION | — | ✅ |
| 70 | SupplierSitePrcBuId | PRC_BU_ID | — | ✅ |
| 71 | SupplierSitePrimaryPaySiteFlag | PRIMARY_PAY_SITE_FLAG | — | ✅ |
| 72 | SupplierSiteProgramApplicationId | PROGRAM_APPLICATION_ID | — | ✅ |
| 73 | SupplierSiteProgramId | PROGRAM_ID | — | ✅ |
| 74 | SupplierSiteProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 75 | SupplierSitePurchasingHoldReason | PURCHASING_HOLD_REASON | — | ✅ |
| 76 | SupplierSitePurchasingSiteFlag | PURCHASING_SITE_FLAG | — | ✅ |
| 77 | SupplierSiteQtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | ✅ |
| 78 | SupplierSiteQtyRcvTolerance | QTY_RCV_TOLERANCE | — | ✅ |
| 79 | SupplierSiteReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | ✅ |
| 80 | SupplierSiteReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | ✅ |
| 81 | SupplierSiteReceivingRoutingId | RECEIVING_ROUTING_ID | — | ✅ |
| 82 | SupplierSiteRequestId | REQUEST_ID | — | ✅ |
| 83 | SupplierSiteRetainageRate | RETAINAGE_RATE | — | ✅ |
| 84 | SupplierSiteRfqOnlySiteFlag | RFQ_ONLY_SITE_FLAG | — | ✅ |
| 85 | SupplierSiteSellingCompanyIdentifier | SELLING_COMPANY_IDENTIFIER | — | ✅ |
| 86 | SupplierSiteServicesToleranceId | SERVICES_TOLERANCE_ID | — | ✅ |
| 87 | SupplierSiteShipViaLookupCode | SHIP_VIA_LOOKUP_CODE | — | ✅ |
| 88 | SupplierSiteShippingControl | SHIPPING_CONTROL | — | ✅ |
| 89 | SupplierSiteShippingNetworkLocation | SHIPPING_NETWORK_LOCATION | — | ✅ |
| 90 | SupplierSiteSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | ✅ |
| 91 | SupplierSiteTaxCountryCode | TAX_COUNTRY_CODE | — | ✅ |
| 92 | SupplierSiteTaxReportingSiteFlag | TAX_REPORTING_SITE_FLAG | — | ✅ |
| 93 | SupplierSiteTelex | TELEX | — | ✅ |
| 94 | SupplierSiteTermsDateBasis | TERMS_DATE_BASIS | — | ✅ |
| 95 | SupplierSiteTermsId | TERMS_ID | — | ✅ |
| 96 | SupplierSiteToleranceId | TOLERANCE_ID | — | ✅ |
| 97 | SupplierSiteTpHeaderId | TP_HEADER_ID | — | ✅ |
| 98 | SupplierSiteVatCode | VAT_CODE | — | ✅ |
| 99 | SupplierSiteVatRegistrationNum | VAT_REGISTRATION_NUM | — | ✅ |
| 100 | SupplierSiteVendorId | VENDOR_ID | — | ✅ |
| 101 | SupplierSiteVendorSiteCode | VENDOR_SITE_CODE | — | ✅ |
| 102 | SupplierSiteVendorSiteCodeAlt | VENDOR_SITE_CODE_ALT | — | ✅ |
| 103 | SupplierSiteVendorSiteId | VENDOR_SITE_ID | 🔑 | ✅ |
| 104 | SupplierSiteVendorSiteSpkId | VENDOR_SITE_SPK_ID | — | ✅ |

### [[zx_wht_tax_classification_v|ZX_WHT_TAX_CLASSIFICATION_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApAwtGroupsCreatedBy | CREATED_BY | — | ✅ |
| 2 | ApAwtGroupsCreationDate | CREATION_DATE | — | ✅ |
| 3 | ApAwtGroupsDescription | DESCRIPTION | — | ✅ |
| 4 | ApAwtGroupsGroupId | GROUP_ID | — | ✅ |
| 5 | ApAwtGroupsInactiveDate | INACTIVE_DATE | — | ✅ |
| 6 | ApAwtGroupsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ApAwtGroupsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | ApAwtGroupsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ApAwtGroupsName | NAME | — | ✅ |
| 10 | ApAwtGroupsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
