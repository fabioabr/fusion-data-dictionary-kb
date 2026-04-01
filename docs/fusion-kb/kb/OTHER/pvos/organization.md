---
id: DOC-OTHER-PVO-Organization
doc_type: system-doc
title: "Organization — PVO Cross-Module"
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
  - Organization
  - organization
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# Organization

## 📌 Visão Geral

View Object para extração BICC de dados de Organization. Acessa as tabelas: HZ_ACCOUNT_ROLLUPS, HZ_ORGANIZATION_PROFILES, HZ_PARTIES.

**Caminho:** `FscmTopModelAM.PartiesAnalyticsAM.Organization`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 255 | 3 | 1 | 62 | 24% |

---

## 🔗 Tabelas Relacionadas

- [[hz_account_rollups|HZ_ACCOUNT_ROLLUPS]] — 106 atributos
- [[hz_organization_profiles|HZ_ORGANIZATION_PROFILES]] — 119 atributos (1 PKs, 62 BICC)
- [[hz_parties|HZ_PARTIES]] — 30 atributos

---

## ⚙️ Atributos

### [[hz_account_rollups|HZ_ACCOUNT_ROLLUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RollupArrFromActiveSubscriptions | ARR_FROM_ACTIVE_SUBSCRIPTIONS | — | — |
| 2 | RollupCallsMade | NUM_OF_CALL_MADE | — | — |
| 3 | RollupCorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 4 | RollupCreatedBy | CREATED_BY | — | — |
| 5 | RollupCreationDate | CREATION_DATE | — | — |
| 6 | RollupCurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 7 | RollupCurrencyCode | CURRENCY_CODE | — | — |
| 8 | RollupDateLastLeadCreated | DATE_LAST_LEAD_CREATED | — | — |
| 9 | RollupDateLastOptyClosed | DATE_LAST_OPTY_CLOSED | — | — |
| 10 | RollupDateNextOptyClosed | DATE_NEXT_OPTY_CLOSED | — | — |
| 11 | RollupEmailsSent | NUM_OF_EMAIL_SENT | — | — |
| 12 | RollupHierArrFromActiveSubs | HIER_ARR_FROM_ACTIVE_SUBS | — | — |
| 13 | RollupHierCallsMade | HIER_NUM_OF_CALL_MADE | — | — |
| 14 | RollupHierCurrentFiscalYearPotentialRevenueAmount | HIER_CURR_FY_POTENTIAL_REVENUE | — | — |
| 15 | RollupHierDateLastLeadCreated | HIER_DATE_LAST_LEAD_CREATED | — | — |
| 16 | RollupHierDateLastOptyClosed | HIER_DATE_LAST_OPTY_CLOSED | — | — |
| 17 | RollupHierDateNextOptyClosed | HIER_DATE_NEXT_OPTY_CLOSED | — | — |
| 18 | RollupHierEmailsSent | HIER_NUM_OF_EMAIL_SENT | — | — |
| 19 | RollupHierEmployeesTotal | HIER_EMPLOYEES_TOTAL | — | — |
| 20 | RollupHierLastCallMadeDate | HIER_LAST_CALL_MADE | — | — |
| 21 | RollupHierLastCompletedActivity | HIER_LAST_COMPLETED_ACTIVITY | — | — |
| 22 | RollupHierLastEmailSentDate | HIER_LAST_EMAIL_SENT | — | — |
| 23 | RollupHierLastTouchDate | HIER_LAST_TOUCH | — | — |
| 24 | RollupHierNextTaskDue | HIER_NEXT_TASK_DUE | — | — |
| 25 | RollupHierNumberOfActiveAssets | HIER_NUM_ACTIVE_ASSETS | — | — |
| 26 | RollupHierNumberOfActiveQuotes | HIER_NUM_ACTIVE_QUOTES | — | — |
| 27 | RollupHierNumberOfAssetsExpiringNextQuarter | HIER_ASSETS_EXP_NXT_QTR | — | — |
| 28 | RollupHierNumberOfContacts | HIER_NUM_CONTACTS | — | — |
| 29 | RollupHierNumberOfDecMakerContacts | HIER_NUM_OF_DEC_MAKER_CONTACTS | — | — |
| 30 | RollupHierNumberOfOpenActivities | HIER_NUM_OF_OPEN_ACTY | — | — |
| 31 | RollupHierNumberOfOpenCriticalSRWaitingSupport | HIER_NUM_OPEN_CR_SR_WAIT_SUPP | — | — |
| 32 | RollupHierNumberOfOpenCriticalServiceRequests | HIER_NUM_OF_OPEN_CRITICAL_SR | — | — |
| 33 | RollupHierNumberOfOpenHotLeads | HIER_NUM_OF_OPEN_HOT_LEAD | — | — |
| 34 | RollupHierNumberOfOpenLeads | HIER_NUM_OF_OPEN_LEAD | — | — |
| 35 | RollupHierNumberOfOpenOpportunities | HIER_NUM_OF_OPEN_OPTY | — | — |
| 36 | RollupHierNumberOfOpenServiceRequests | HIER_NUM_OF_OPEN_SR | — | — |
| 37 | RollupHierNumberOfQualHotLeads | HIER_NUM_OF_QUAL_HOT_LEADS | — | — |
| 38 | RollupHierNumberOfQualifiedLeads | HIER_NUMBER_OF_QUALIFIED_LEADS | — | — |
| 39 | RollupHierNumberOfSrClosePastWeek | HIER_NUM_OF_SR_CLOSE_PAST_WEEK | — | — |
| 40 | RollupHierNumberOfSubsExpNxtQtr | HIER_NUM_OF_SUBS_EXP_NXT_QTR | — | — |
| 41 | RollupHierNumberOfSubsExpQtr | HIER_NUMBER_OF_SUBS_EXP_QTR | — | — |
| 42 | RollupHierNumberOfSubscriptionsExpiredLastQuarter | HIER_NUM_SUBS_EXP_LAST_QTR | — | — |
| 43 | RollupHierNumberOfTouches | HIER_NUM_OF_TOUCHES | — | — |
| 44 | RollupHierPotentialRevenueOpenLeads | HIER_POTENTIAL_REV_OPEN_LEADS | — | — |
| 45 | RollupHierSumOfActiveAssetValue | HIER_SUM_ACTIVE_ASSETS | — | — |
| 46 | RollupHierSumOfActiveSubscriptionsMRR | HIER_SUM_OF_ACTIVE_SUBS_MRR | — | — |
| 47 | RollupHierSumOfActiveSubscriptionsTCV | HIER_SUM_OF_ACTIVE_SUBS_TCV | — | — |
| 48 | RollupHierSumOfClosedSubscriptionsMRR | HIER_SUM_OF_CLOSED_SUBS_MRR | — | — |
| 49 | RollupHierSumOfLapsedRenewalsMRR | HIER_SUM_OF_LAPSED_RENEW_MRR | — | — |
| 50 | RollupHierSumOfOpenLeadAmount | HIER_OPEN_LEAD_DEAL_AMT | — | — |
| 51 | RollupHierSumOfOpenOpportunitiesRevenue | HIER_OPEN_OPTY_REVENUE_AMT | — | — |
| 52 | RollupHierSumOfOpenOrderAmount | HIER_OPEN_ORDER_AMT | — | — |
| 53 | RollupHierSumOfUpcomingRenewalsMRR | HIER_SUM_OF_UPCOMING_RENEW_MRR | — | — |
| 54 | RollupHierSumOfWonOpportunitiesRevenue | HIER_WON_OPTY_REVENUE_AMT | — | — |
| 55 | RollupHierSumOfWonOrderAmount | HIER_WON_ORDER_AMT | — | — |
| 56 | RollupHierSumOpenOptyRevenueNxtQtr | HIER_SUM_OPEN_OPTY_REV_NXT_QTR | — | — |
| 57 | RollupHierSumOpenOptyRevenueQtr | HIER_SUM_OPEN_OPTY_REV_QTR | — | — |
| 58 | RollupHierSumOptyRevenueWonQtr | HIER_SUM_OPTY_REV_WON_QTR | — | — |
| 59 | RollupHierTotalCompletedActivities | HIER_TOTAL_COMPLETD_ACTIVITIES | — | — |
| 60 | RollupHierTotalNotes | HIER_TOTAL_NOTES | — | — |
| 61 | RollupLastCallMadeDate | LAST_CALL_MADE | — | — |
| 62 | RollupLastCompletedActivity | LAST_COMPLETED_ACTIVITY | — | — |
| 63 | RollupLastEmailSentDate | LAST_EMAIL_SENT | — | — |
| 64 | RollupLastTouchDate | LAST_TOUCH | — | — |
| 65 | RollupLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 66 | RollupLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 67 | RollupLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 68 | RollupNextAppointmentDate | NEXT_APPOINTMENT_DATE | — | — |
| 69 | RollupNextTaskDue | NEXT_TASK_DUE | — | — |
| 70 | RollupNumberOfActiveAssets | NUM_ACTIVE_ASSETS | — | — |
| 71 | RollupNumberOfActiveQuotes | NUM_ACTIVE_QUOTES | — | — |
| 72 | RollupNumberOfAssetsExpiringNextQuarter | ASSETS_EXP_NXT_QTR | — | — |
| 73 | RollupNumberOfContacts | NUM_CONTACTS | — | — |
| 74 | RollupNumberOfDecisionMakerContacts | NUM_OF_DECISION_MAKER_CONTACTS | — | — |
| 75 | RollupNumberOfOpenActivities | NUM_OF_OPEN_ACTY | — | — |
| 76 | RollupNumberOfOpenCriticalSRWaitingSupport | NUM_OPEN_CR_SR_WAIT_SUPP | — | — |
| 77 | RollupNumberOfOpenCriticalServiceRequests | NUM_OF_OPEN_CRITICAL_SR | — | — |
| 78 | RollupNumberOfOpenHotLeads | NUM_OF_OPEN_HOT_LEAD | — | — |
| 79 | RollupNumberOfOpenLeads | NUM_OF_OPEN_LEAD | — | — |
| 80 | RollupNumberOfOpenOpportunities | NUM_OF_OPEN_OPTY | — | — |
| 81 | RollupNumberOfOpenServiceRequests | NUM_OF_OPEN_SR | — | — |
| 82 | RollupNumberOfQualifiedHotLeads | NUMBER_OF_QUALIFIED_HOT_LEADS | — | — |
| 83 | RollupNumberOfQualifiedLeads | NUMBER_OF_QUALIFIED_LEADS | — | — |
| 84 | RollupNumberOfSrClosedPastWeek | NUM_OF_SR_CLOSED_PAST_WEEK | — | — |
| 85 | RollupNumberOfSubsExpNxtQtr | NUMBER_OF_SUBS_EXP_NXT_QTR | — | — |
| 86 | RollupNumberOfSubsExpQtr | NUMBER_OF_SUBS_EXP_QTR | — | — |
| 87 | RollupNumberOfSubscriptionsExpiredLastQuarter | NUM_SUBS_EXP_LAST_QTR | — | — |
| 88 | RollupNumberOfTouches | NUM_OF_TOUCHES | — | — |
| 89 | RollupOrganizationProfileId | ORGANIZATION_PROFILE_ID | — | — |
| 90 | RollupPotentialRevenueOpenLeads | POTENTIAL_REV_OPEN_LEADS | — | — |
| 91 | RollupSumOfActiveAssetValue | SUM_ACTIVE_ASSETS | — | — |
| 92 | RollupSumOfActiveSubscriptionsMRR | SUM_OF_ACTIVE_SUBS_MRR | — | — |
| 93 | RollupSumOfActiveSubscriptionsTCV | SUM_OF_ACTIVE_SUBS_TCV | — | — |
| 94 | RollupSumOfClosedSubscriptionsMRR | SUM_OF_CLOSED_SUBS_MRR | — | — |
| 95 | RollupSumOfLapsedRenewalsMRR | SUM_OF_LAPSED_RENEW_MRR | — | — |
| 96 | RollupSumOfOpenLeadAmount | OPEN_LEAD_DEAL_AMT | — | — |
| 97 | RollupSumOfOpenOpportunitiesRevenue | OPEN_OPTY_REVENUE_AMT | — | — |
| 98 | RollupSumOfOpenOrderAmount | OPEN_ORDER_AMT | — | — |
| 99 | RollupSumOfUpcomingRenewalsMRR | SUM_OF_UPCOMING_RENEW_MRR | — | — |
| 100 | RollupSumOfWonOpportunitiesRevenue | WON_OPTY_REVENUE_AMT | — | — |
| 101 | RollupSumOfWonOrderAmount | WON_ORDER_AMT | — | — |
| 102 | RollupSumOpenOptyRevenueNxtQtr | SUM_OPEN_OPTY_REVENUE_NXT_QTR | — | — |
| 103 | RollupSumOpenOptyRevenueThisQtr | SUM_OPEN_OPTY_REVENUE_THIS_QTR | — | — |
| 104 | RollupSumOptyRevenueWonThisQtr | SUM_OPTY_REVENUE_WON_THIS_QTR | — | — |
| 105 | RollupTotalCompletedActivities | TOTAL_COMPLETED_ACTIVITIES | — | — |
| 106 | RollupTotalNotes | TOTAL_NOTES | — | — |

### [[hz_organization_profiles|HZ_ORGANIZATION_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccountScore | ACCOUNT_SCORE | — | — |
| 2 | AccountScoringTier | ACCOUNT_SCORING_TIER | — | — |
| 3 | ActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 4 | AnalysisFy | ANALYSIS_FY | — | ✅ |
| 5 | BankCode | BANK_CODE | — | ✅ |
| 6 | BankOrBranchNumber | BANK_OR_BRANCH_NUMBER | — | ✅ |
| 7 | BranchCode | BRANCH_CODE | — | ✅ |
| 8 | BranchFlag | BRANCH_FLAG | — | — |
| 9 | BusinessReport | BUSINESS_REPORT | — | — |
| 10 | BusinessScope | BUSINESS_SCOPE | — | ✅ |
| 11 | CeoName | CEO_NAME | — | ✅ |
| 12 | CeoTitle | CEO_TITLE | — | ✅ |
| 13 | CertReasonCode | CERT_REASON_CODE | — | — |
| 14 | CertificationLevel | CERTIFICATION_LEVEL | — | — |
| 15 | CleanlinessScore | CLEANLINESS_SCORE | — | — |
| 16 | Comments | COMMENTS | — | — |
| 17 | CompletenessScore | COMPLETENESS_SCORE | — | — |
| 18 | ConflictId | CONFLICT_ID | — | — |
| 19 | CongDistCode | CONG_DIST_CODE | — | ✅ |
| 20 | ContentSourceNumber | CONTENT_SOURCE_NUMBER | — | — |
| 21 | ControlYr | CONTROL_YR | — | ✅ |
| 22 | CorpCurrencyCode | CORP_CURRENCY_CODE | — | ✅ |
| 23 | CorporationClass | CORPORATION_CLASS | — | ✅ |
| 24 | CreatedBy | CREATED_BY | — | — |
| 25 | CreatedByModule | CREATED_BY_MODULE | — | — |
| 26 | CreationDate | CREATION_DATE | — | — |
| 27 | CurcyConvRateType | CURCY_CONV_RATE_TYPE | — | ✅ |
| 28 | CurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 29 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 30 | DataCloudStatus | DATA_CLOUD_STATUS | — | — |
| 31 | DataConfidenceScore | DATA_CONFIDENCE_SCORE | — | — |
| 32 | DbRating | DB_RATING | — | ✅ |
| 33 | Description | DESCRIPTION | — | — |
| 34 | Disadv8aInd | DISADV_8A_IND | — | ✅ |
| 35 | DisplayedDunsPartyId | DISPLAYED_DUNS_PARTY_ID | — | ✅ |
| 36 | DoNotConfuseWith | DO_NOT_CONFUSE_WITH | — | ✅ |
| 37 | DomesticUltimateDunsNumC | DOMESTIC_ULTIMATE_DUNS_NUM_C | — | ✅ |
| 38 | DunsNumberC | DUNS_NUMBER_C | — | — |
| 39 | DuplicateIndicator | DUPLICATE_INDICATOR | — | — |
| 40 | DuplicateScore | DUPLICATE_SCORE | — | — |
| 41 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 42 | EffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 43 | EffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 44 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 45 | EmpAtPrimaryAdr | EMP_AT_PRIMARY_ADR | — | — |
| 46 | EmpAtPrimaryAdrEstInd | EMP_AT_PRIMARY_ADR_EST_IND | — | — |
| 47 | EmpAtPrimaryAdrMinInd | EMP_AT_PRIMARY_ADR_MIN_IND | — | — |
| 48 | EmpAtPrimaryAdrText | EMP_AT_PRIMARY_ADR_TEXT | — | — |
| 49 | EmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 50 | EnquiryDuns | ENQUIRY_DUNS | — | ✅ |
| 51 | EnrichmentScore | ENRICHMENT_SCORE | — | — |
| 52 | ExportInd | EXPORT_IND | — | ✅ |
| 53 | FiscalYearendMonth | FISCAL_YEAREND_MONTH | — | ✅ |
| 54 | GlobalUltimateDunsNumC | GLOBAL_ULTIMATE_DUNS_NUM_C | — | ✅ |
| 55 | GrowthStrategyDesc | GROWTH_STRATEGY_DESC | — | — |
| 56 | GsaIndicatorFlag | GSA_INDICATOR_FLAG | — | ✅ |
| 57 | HomeCountry | HOME_COUNTRY | — | ✅ |
| 58 | HqBranchInd | HQ_BRANCH_IND | — | ✅ |
| 59 | ImportInd | IMPORT_IND | — | ✅ |
| 60 | IncorpYear | INCORP_YEAR | — | ✅ |
| 61 | InternalFlag | INTERNAL_FLAG | — | ✅ |
| 62 | JgzzFiscalCode | JGZZ_FISCAL_CODE | — | ✅ |
| 63 | LaborSurplusInd | LABOR_SURPLUS_IND | — | ✅ |
| 64 | LastAssignedDate | LAST_ASSIGNED_DATE | — | — |
| 65 | LastEnrichmentDate | LAST_ENRICHMENT_DATE | — | — |
| 66 | LastScoreUpdateDate | LAST_SCORE_UPDATE_DATE | — | — |
| 67 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 68 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 69 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 70 | LegalStatus | LEGAL_STATUS | — | ✅ |
| 71 | LineOfBusiness | LINE_OF_BUSINESS | — | ✅ |
| 72 | LocalActivityCode | LOCAL_ACTIVITY_CODE | — | — |
| 73 | LocalActivityCodeType | LOCAL_ACTIVITY_CODE_TYPE | — | — |
| 74 | LocalBusIdenType | LOCAL_BUS_IDEN_TYPE | — | ✅ |
| 75 | LocalBusIdentifier | LOCAL_BUS_IDENTIFIER | — | ✅ |
| 76 | MinorityOwnedInd | MINORITY_OWNED_IND | — | ✅ |
| 77 | MinorityOwnedType | MINORITY_OWNED_TYPE | — | ✅ |
| 78 | MissionStatement | MISSION_STATEMENT | — | ✅ |
| 79 | NamedFlag | NAMED_FLAG | — | — |
| 80 | NextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 81 | OobInd | OOB_IND | — | ✅ |
| 82 | OrganizationName | ORGANIZATION_NAME | — | ✅ |
| 83 | OrganizationProfileId | ORGANIZATION_PROFILE_ID | 🔑 | ✅ |
| 84 | OrganizationSize | ORGANIZATION_SIZE | — | ✅ |
| 85 | OrganizationType | ORGANIZATION_TYPE | — | ✅ |
| 86 | OwnerPartyId | OWNER_PARTY_ID | — | — |
| 87 | ParentDunsNumC | PARENT_DUNS_NUM_C | — | ✅ |
| 88 | ParentSubInd | PARENT_SUB_IND | — | ✅ |
| 89 | PartyId | PARTY_ID | — | — |
| 90 | PartyNumber | PARTY_NUMBER | — | ✅ |
| 91 | PrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | ✅ |
| 92 | PreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 93 | PreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 94 | PrincipalName | PRINCIPAL_NAME | — | ✅ |
| 95 | PrincipalTitle | PRINCIPAL_TITLE | — | ✅ |
| 96 | PublicPrivateOwnershipFlag | PUBLIC_PRIVATE_OWNERSHIP_FLAG | — | ✅ |
| 97 | RecencyScore | RECENCY_SCORE | — | — |
| 98 | RegistrationType | REGISTRATION_TYPE | — | ✅ |
| 99 | RentOwnInd | RENT_OWN_IND | — | ✅ |
| 100 | SalesProfileStatus | SALES_PROFILE_STATUS | — | — |
| 101 | SalesProfileType | SALES_PROFILE_TYPE | — | — |
| 102 | SeblUserKeyLoc | SEBL_USER_KEY_LOC | — | — |
| 103 | SicCode | SIC_CODE | — | — |
| 104 | SicCodeType | SIC_CODE_TYPE | — | — |
| 105 | SmallBusInd | SMALL_BUS_IND | — | ✅ |
| 106 | Status | STATUS | — | — |
| 107 | StockSymbol | STOCK_SYMBOL | — | ✅ |
| 108 | SuffixOverriddenFlag | SUFFIX_OVERRIDDEN_FLAG | — | ✅ |
| 109 | TotalEmpEstInd | TOTAL_EMP_EST_IND | — | — |
| 110 | TotalEmpMinInd | TOTAL_EMP_MIN_IND | — | — |
| 111 | TotalEmployeesInd | TOTAL_EMPLOYEES_IND | — | — |
| 112 | TotalEmployeesText | TOTAL_EMPLOYEES_TEXT | — | — |
| 113 | TotalPayments | TOTAL_PAYMENTS | — | ✅ |
| 114 | TradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | ✅ |
| 115 | UniqueNameAlias | UNIQUE_NAME_ALIAS | — | ✅ |
| 116 | UniqueNameSuffix | UNIQUE_NAME_SUFFIX | — | ✅ |
| 117 | ValidityScore | VALIDITY_SCORE | — | — |
| 118 | WomanOwnedInd | WOMAN_OWNED_IND | — | ✅ |
| 119 | YearEstablished | YEAR_ESTABLISHED | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgOwnerPartyId | PARTY_ID | — | — |
| 2 | OrgOwnerPartyName | PARTY_NAME | — | — |
| 3 | OrgPartyPartyId | PARTY_ID | — | — |
| 4 | OrgPartyPartyNumberKey | PARTY_NUMBER | — | — |
| 5 | OrgPartyPartyType | PARTY_TYPE | — | — |
| 6 | OrgPartyPartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 7 | OrgPartyPreferredName | PREFERRED_NAME | — | — |
| 8 | OrgPartyPrimaryAddressCity | CITY | — | — |
| 9 | OrgPartyPrimaryAddressCountry | COUNTRY | — | — |
| 10 | OrgPartyPrimaryAddressCounty | COUNTY | — | — |
| 11 | OrgPartyPrimaryAddressLine1 | ADDRESS1 | — | — |
| 12 | OrgPartyPrimaryAddressLine2 | ADDRESS2 | — | — |
| 13 | OrgPartyPrimaryAddressLine3 | ADDRESS3 | — | — |
| 14 | OrgPartyPrimaryAddressLine4 | ADDRESS4 | — | — |
| 15 | OrgPartyPrimaryAddressPostalCode | POSTAL_CODE | — | — |
| 16 | OrgPartyPrimaryAddressProvince | PROVINCE | — | — |
| 17 | OrgPartyPrimaryAddressState | STATE | — | — |
| 18 | OrgPartyPrimaryCustClassification | CATEGORY_CODE | — | — |
| 19 | OrgPartyPrimaryEmailAddress | EMAIL_ADDRESS | — | — |
| 20 | OrgPartyPrimaryLanguage | LANGUAGE_NAME | — | — |
| 21 | OrgPartyPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 22 | OrgPartyPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 23 | OrgPartyPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 24 | OrgPartyPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 25 | OrgPartyPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | — |
| 26 | OrgPartyPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 27 | OrgPartyPrimaryUrl | URL | — | — |
| 28 | OrgPartyStatus | STATUS | — | — |
| 29 | OrgPartyThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 30 | OrgPartyValidatedFlag | VALIDATED_FLAG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
