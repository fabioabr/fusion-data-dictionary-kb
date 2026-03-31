---
id: DOC-AR-PVO-AccountBankAccount
doc_type: system-doc
title: "AccountBankAccount — PVO Accounts Receivable"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ar
  - data-dictionary
  - pvo
  - bicc
aliases:
  - AccountBankAccount
  - accountbankaccount
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AccountBankAccount

## 📌 Visão Geral

Extrai as contas bancárias externas associadas a contas de clientes (customer accounts), incluindo dados de banco, agência, classificação e instrumentos de pagamento. Permite identificar os meios de recebimento cadastrados por cliente para conciliação bancária e gestão de cobranças.

**Caminho:** `FscmTopModelAM.FinArCustomersPublicModelAM.AccountBankAccount`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 497 | 6 | 1 | 29 | 6% |

---

## 🔗 Tabelas Relacionadas

- [[hz_contact_points|HZ_CONTACT_POINTS]] — 23 atributos (3 BICC)
- [[hz_organization_profiles|HZ_ORGANIZATION_PROFILES]] — 228 atributos (7 BICC)
- [[hz_parties|HZ_PARTIES]] — 164 atributos (2 BICC)
- [[iby_external_payers_all|IBY_EXTERNAL_PAYERS_ALL]] — 21 atributos (6 BICC)
- [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]] — 46 atributos (8 BICC)
- [[iby_pmt_instr_uses_all|IBY_PMT_INSTR_USES_ALL]] — 15 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[hz_contact_points|HZ_CONTACT_POINTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankBranchContactActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | BankBranchContactAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 3 | BankBranchContactContactPointId | CONTACT_POINT_ID | — | — |
| 4 | BankBranchContactContactPointPurpose | CONTACT_POINT_PURPOSE | — | — |
| 5 | BankBranchContactCreatedBy | CREATED_BY | — | — |
| 6 | BankBranchContactCreatedByModule | CREATED_BY_MODULE | — | — |
| 7 | BankBranchContactCreationDate | CREATION_DATE | — | — |
| 8 | BankBranchContactEftSwiftCode | EFT_SWIFT_CODE | — | ✅ |
| 9 | BankBranchContactEftUserNumber | EFT_USER_NUMBER | — | ✅ |
| 10 | BankBranchContactEndDate | END_DATE | — | — |
| 11 | BankBranchContactLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | BankBranchContactLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | BankBranchContactLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | BankBranchContactOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 15 | BankBranchContactOverallPrimaryFlag | OVERALL_PRIMARY_FLAG | — | — |
| 16 | BankBranchContactOwnerTableId | OWNER_TABLE_ID | — | — |
| 17 | BankBranchContactOwnerTableName | OWNER_TABLE_NAME | — | — |
| 18 | BankBranchContactPartyUsageCode | PARTY_USAGE_CODE | — | — |
| 19 | BankBranchContactPrimaryByPurpose | PRIMARY_BY_PURPOSE | — | — |
| 20 | BankBranchContactPrimaryFlag | PRIMARY_FLAG | — | — |
| 21 | BankBranchContactRelationshipId | RELATIONSHIP_ID | — | — |
| 22 | BankBranchContactStartDate | START_DATE | — | — |
| 23 | BankBranchContactStatus | STATUS | — | — |

### [[hz_organization_profiles|HZ_ORGANIZATION_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | BankAnalysisFy | ANALYSIS_FY | — | — |
| 3 | BankBankCode | BANK_CODE | — | — |
| 4 | BankBankOrBranchNumber | BANK_OR_BRANCH_NUMBER | — | ✅ |
| 5 | BankBranchActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 6 | BankBranchAnalysisFy | ANALYSIS_FY | — | — |
| 7 | BankBranchBankCode | BANK_CODE | — | — |
| 8 | BankBranchBankOrBranchNumber | BANK_OR_BRANCH_NUMBER | — | ✅ |
| 9 | BankBranchBranchCode | BRANCH_CODE | — | — |
| 10 | BankBranchBranchFlag | BRANCH_FLAG | — | — |
| 11 | BankBranchBusinessReport | BUSINESS_REPORT | — | — |
| 12 | BankBranchBusinessScope | BUSINESS_SCOPE | — | — |
| 13 | BankBranchCeoName | CEO_NAME | — | — |
| 14 | BankBranchCeoTitle | CEO_TITLE | — | — |
| 15 | BankBranchCertReasonCode | CERT_REASON_CODE | — | — |
| 16 | BankBranchCertificationLevel | CERTIFICATION_LEVEL | — | — |
| 17 | BankBranchCleanlinessScore | CLEANLINESS_SCORE | — | — |
| 18 | BankBranchCode | BRANCH_CODE | — | — |
| 19 | BankBranchComments | COMMENTS | — | — |
| 20 | BankBranchCompletenessScore | COMPLETENESS_SCORE | — | — |
| 21 | BankBranchConflictId | CONFLICT_ID | — | — |
| 22 | BankBranchCongDistCode | CONG_DIST_CODE | — | — |
| 23 | BankBranchContentSourceNumber | CONTENT_SOURCE_NUMBER | — | — |
| 24 | BankBranchControlYr | CONTROL_YR | — | — |
| 25 | BankBranchCorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 26 | BankBranchCorporationClass | CORPORATION_CLASS | — | — |
| 27 | BankBranchCreatedBy | CREATED_BY | — | — |
| 28 | BankBranchCreatedByModule | CREATED_BY_MODULE | — | — |
| 29 | BankBranchCreationDate | CREATION_DATE | — | — |
| 30 | BankBranchCurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 31 | BankBranchCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 32 | BankBranchCurrencyCode | CURRENCY_CODE | — | — |
| 33 | BankBranchDataCloudStatus | DATA_CLOUD_STATUS | — | — |
| 34 | BankBranchDataConfidenceScore | DATA_CONFIDENCE_SCORE | — | — |
| 35 | BankBranchDbRating | DB_RATING | — | — |
| 36 | BankBranchDisadv8aInd | DISADV_8A_IND | — | — |
| 37 | BankBranchDisplayedDunsPartyId | DISPLAYED_DUNS_PARTY_ID | — | — |
| 38 | BankBranchDoNotConfuseWith | DO_NOT_CONFUSE_WITH | — | — |
| 39 | BankBranchDomesticUltimateDunsNumC | DOMESTIC_ULTIMATE_DUNS_NUM_C | — | — |
| 40 | BankBranchDunsNumber | DUNS_NUMBER | — | — |
| 41 | BankBranchDunsNumberC | DUNS_NUMBER_C | — | — |
| 42 | BankBranchDuplicateIndicator | DUPLICATE_INDICATOR | — | — |
| 43 | BankBranchDuplicateScore | DUPLICATE_SCORE | — | — |
| 44 | BankBranchEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 45 | BankBranchEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 46 | BankBranchEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 47 | BankBranchEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 48 | BankBranchEmpAtPrimaryAdr | EMP_AT_PRIMARY_ADR | — | — |
| 49 | BankBranchEmpAtPrimaryAdrEstInd | EMP_AT_PRIMARY_ADR_EST_IND | — | — |
| 50 | BankBranchEmpAtPrimaryAdrMinInd | EMP_AT_PRIMARY_ADR_MIN_IND | — | — |
| 51 | BankBranchEmpAtPrimaryAdrText | EMP_AT_PRIMARY_ADR_TEXT | — | — |
| 52 | BankBranchEmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 53 | BankBranchEnquiryDuns | ENQUIRY_DUNS | — | — |
| 54 | BankBranchEnrichmentScore | ENRICHMENT_SCORE | — | — |
| 55 | BankBranchExportInd | EXPORT_IND | — | — |
| 56 | BankBranchFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 57 | BankBranchFlag | BRANCH_FLAG | — | — |
| 58 | BankBranchGlobalUltimateDunsNumC | GLOBAL_ULTIMATE_DUNS_NUM_C | — | — |
| 59 | BankBranchGrowthStrategyDesc | GROWTH_STRATEGY_DESC | — | — |
| 60 | BankBranchGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | — |
| 61 | BankBranchHomeCountry | HOME_COUNTRY | — | — |
| 62 | BankBranchHqBranchInd | HQ_BRANCH_IND | — | — |
| 63 | BankBranchImportInd | IMPORT_IND | — | — |
| 64 | BankBranchIncorpYear | INCORP_YEAR | — | — |
| 65 | BankBranchInternalFlag | INTERNAL_FLAG | — | — |
| 66 | BankBranchJgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 67 | BankBranchLaborSurplusInd | LABOR_SURPLUS_IND | — | — |
| 68 | BankBranchLastEnrichmentDate | LAST_ENRICHMENT_DATE | — | — |
| 69 | BankBranchLastScoreUpdateDate | LAST_SCORE_UPDATE_DATE | — | — |
| 70 | BankBranchLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 71 | BankBranchLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 72 | BankBranchLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 73 | BankBranchLegalStatus | LEGAL_STATUS | — | — |
| 74 | BankBranchLineOfBusiness | LINE_OF_BUSINESS | — | — |
| 75 | BankBranchLocalActivityCode | LOCAL_ACTIVITY_CODE | — | — |
| 76 | BankBranchLocalActivityCodeType | LOCAL_ACTIVITY_CODE_TYPE | — | — |
| 77 | BankBranchLocalBusIdenType | LOCAL_BUS_IDEN_TYPE | — | — |
| 78 | BankBranchLocalBusIdentifier | LOCAL_BUS_IDENTIFIER | — | — |
| 79 | BankBranchMinorityOwnedInd | MINORITY_OWNED_IND | — | — |
| 80 | BankBranchMinorityOwnedType | MINORITY_OWNED_TYPE | — | — |
| 81 | BankBranchMissionStatement | MISSION_STATEMENT | — | — |
| 82 | BankBranchNextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 83 | BankBranchObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 84 | BankBranchOobInd | OOB_IND | — | — |
| 85 | BankBranchOrganizationName | ORGANIZATION_NAME | — | ✅ |
| 86 | BankBranchOrganizationProfileId | ORGANIZATION_PROFILE_ID | — | — |
| 87 | BankBranchOrganizationSize | ORGANIZATION_SIZE | — | — |
| 88 | BankBranchOrganizationType | ORGANIZATION_TYPE | — | — |
| 89 | BankBranchParentDunsNumC | PARENT_DUNS_NUM_C | — | — |
| 90 | BankBranchParentSubInd | PARENT_SUB_IND | — | — |
| 91 | BankBranchPartyId | PARTY_ID | — | — |
| 92 | BankBranchPartyNumber | PARTY_NUMBER | — | — |
| 93 | BankBranchPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 94 | BankBranchPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 95 | BankBranchPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 96 | BankBranchPrincipalName | PRINCIPAL_NAME | — | — |
| 97 | BankBranchPrincipalTitle | PRINCIPAL_TITLE | — | — |
| 98 | BankBranchPublicPrivateOwnershipFlag | PUBLIC_PRIVATE_OWNERSHIP_FLAG | — | — |
| 99 | BankBranchRecencyScore | RECENCY_SCORE | — | — |
| 100 | BankBranchRegistrationType | REGISTRATION_TYPE | — | — |
| 101 | BankBranchRentOwnInd | RENT_OWN_IND | — | — |
| 102 | BankBranchRequestId | REQUEST_ID | — | — |
| 103 | BankBranchSeblUserKeyLoc | SEBL_USER_KEY_LOC | — | — |
| 104 | BankBranchSicCode | SIC_CODE | — | — |
| 105 | BankBranchSicCodeType | SIC_CODE_TYPE | — | — |
| 106 | BankBranchSmallBusInd | SMALL_BUS_IND | — | — |
| 107 | BankBranchStatus | STATUS | — | — |
| 108 | BankBranchStockSymbol | STOCK_SYMBOL | — | — |
| 109 | BankBranchSuffixOverriddenFlag | SUFFIX_OVERRIDDEN_FLAG | — | — |
| 110 | BankBranchTotalEmpEstInd | TOTAL_EMP_EST_IND | — | — |
| 111 | BankBranchTotalEmpMinInd | TOTAL_EMP_MIN_IND | — | — |
| 112 | BankBranchTotalEmployeesInd | TOTAL_EMPLOYEES_IND | — | — |
| 113 | BankBranchTotalEmployeesText | TOTAL_EMPLOYEES_TEXT | — | — |
| 114 | BankBranchTotalPayments | TOTAL_PAYMENTS | — | — |
| 115 | BankBranchTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 116 | BankBranchUniqueNameAlias | UNIQUE_NAME_ALIAS | — | — |
| 117 | BankBranchUniqueNameSuffix | UNIQUE_NAME_SUFFIX | — | — |
| 118 | BankBranchValidityScore | VALIDITY_SCORE | — | — |
| 119 | BankBranchWomanOwnedInd | WOMAN_OWNED_IND | — | — |
| 120 | BankBranchYearEstablished | YEAR_ESTABLISHED | — | — |
| 121 | BankBusinessReport | BUSINESS_REPORT | — | — |
| 122 | BankBusinessScope | BUSINESS_SCOPE | — | — |
| 123 | BankCeoName | CEO_NAME | — | — |
| 124 | BankCeoTitle | CEO_TITLE | — | — |
| 125 | BankCertReasonCode | CERT_REASON_CODE | — | — |
| 126 | BankCertificationLevel | CERTIFICATION_LEVEL | — | — |
| 127 | BankCleanlinessScore | CLEANLINESS_SCORE | — | — |
| 128 | BankComments | COMMENTS | — | — |
| 129 | BankCompletenessScore | COMPLETENESS_SCORE | — | — |
| 130 | BankConflictId | CONFLICT_ID | — | — |
| 131 | BankCongDistCode | CONG_DIST_CODE | — | — |
| 132 | BankContentSourceNumber | CONTENT_SOURCE_NUMBER | — | — |
| 133 | BankControlYr | CONTROL_YR | — | — |
| 134 | BankCorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 135 | BankCorporationClass | CORPORATION_CLASS | — | — |
| 136 | BankCreatedBy | CREATED_BY | — | — |
| 137 | BankCreatedByModule | CREATED_BY_MODULE | — | — |
| 138 | BankCreationDate | CREATION_DATE | — | — |
| 139 | BankCurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 140 | BankCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 141 | BankCurrencyCode | CURRENCY_CODE | — | — |
| 142 | BankDataCloudStatus | DATA_CLOUD_STATUS | — | — |
| 143 | BankDataConfidenceScore | DATA_CONFIDENCE_SCORE | — | — |
| 144 | BankDbRating | DB_RATING | — | — |
| 145 | BankDisadv8aInd | DISADV_8A_IND | — | — |
| 146 | BankDisplayedDunsPartyId | DISPLAYED_DUNS_PARTY_ID | — | — |
| 147 | BankDoNotConfuseWith | DO_NOT_CONFUSE_WITH | — | — |
| 148 | BankDomesticUltimateDunsNumC | DOMESTIC_ULTIMATE_DUNS_NUM_C | — | — |
| 149 | BankDunsNumber | DUNS_NUMBER | — | — |
| 150 | BankDunsNumberC | DUNS_NUMBER_C | — | — |
| 151 | BankDuplicateIndicator | DUPLICATE_INDICATOR | — | — |
| 152 | BankDuplicateScore | DUPLICATE_SCORE | — | — |
| 153 | BankEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 154 | BankEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 155 | BankEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 156 | BankEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 157 | BankEmpAtPrimaryAdr | EMP_AT_PRIMARY_ADR | — | — |
| 158 | BankEmpAtPrimaryAdrEstInd | EMP_AT_PRIMARY_ADR_EST_IND | — | — |
| 159 | BankEmpAtPrimaryAdrMinInd | EMP_AT_PRIMARY_ADR_MIN_IND | — | — |
| 160 | BankEmpAtPrimaryAdrText | EMP_AT_PRIMARY_ADR_TEXT | — | — |
| 161 | BankEmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 162 | BankEnquiryDuns | ENQUIRY_DUNS | — | — |
| 163 | BankEnrichmentScore | ENRICHMENT_SCORE | — | — |
| 164 | BankExportInd | EXPORT_IND | — | — |
| 165 | BankFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 166 | BankGlobalUltimateDunsNumC | GLOBAL_ULTIMATE_DUNS_NUM_C | — | — |
| 167 | BankGrowthStrategyDesc | GROWTH_STRATEGY_DESC | — | — |
| 168 | BankGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | — |
| 169 | BankHomeCountry | HOME_COUNTRY | — | ✅ |
| 170 | BankHqBranchInd | HQ_BRANCH_IND | — | — |
| 171 | BankImportInd | IMPORT_IND | — | — |
| 172 | BankIncorpYear | INCORP_YEAR | — | — |
| 173 | BankInternalFlag | INTERNAL_FLAG | — | — |
| 174 | BankJgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 175 | BankLaborSurplusInd | LABOR_SURPLUS_IND | — | — |
| 176 | BankLastEnrichmentDate | LAST_ENRICHMENT_DATE | — | — |
| 177 | BankLastScoreUpdateDate | LAST_SCORE_UPDATE_DATE | — | — |
| 178 | BankLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 179 | BankLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 180 | BankLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 181 | BankLegalStatus | LEGAL_STATUS | — | — |
| 182 | BankLineOfBusiness | LINE_OF_BUSINESS | — | — |
| 183 | BankLocalActivityCode | LOCAL_ACTIVITY_CODE | — | — |
| 184 | BankLocalActivityCodeType | LOCAL_ACTIVITY_CODE_TYPE | — | — |
| 185 | BankLocalBusIdenType | LOCAL_BUS_IDEN_TYPE | — | — |
| 186 | BankLocalBusIdentifier | LOCAL_BUS_IDENTIFIER | — | — |
| 187 | BankMinorityOwnedInd | MINORITY_OWNED_IND | — | — |
| 188 | BankMinorityOwnedType | MINORITY_OWNED_TYPE | — | — |
| 189 | BankMissionStatement | MISSION_STATEMENT | — | — |
| 190 | BankNextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 191 | BankObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 192 | BankOobInd | OOB_IND | — | — |
| 193 | BankOrganizationName | ORGANIZATION_NAME | — | ✅ |
| 194 | BankOrganizationProfileId | ORGANIZATION_PROFILE_ID | — | — |
| 195 | BankOrganizationSize | ORGANIZATION_SIZE | — | — |
| 196 | BankOrganizationType | ORGANIZATION_TYPE | — | — |
| 197 | BankParentDunsNumC | PARENT_DUNS_NUM_C | — | — |
| 198 | BankParentSubInd | PARENT_SUB_IND | — | — |
| 199 | BankPartyId | PARTY_ID | — | — |
| 200 | BankPartyNumber | PARTY_NUMBER | — | — |
| 201 | BankPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 202 | BankPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 203 | BankPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 204 | BankPrincipalName | PRINCIPAL_NAME | — | — |
| 205 | BankPrincipalTitle | PRINCIPAL_TITLE | — | — |
| 206 | BankPublicPrivateOwnershipFlag | PUBLIC_PRIVATE_OWNERSHIP_FLAG | — | — |
| 207 | BankRecencyScore | RECENCY_SCORE | — | — |
| 208 | BankRegistrationType | REGISTRATION_TYPE | — | — |
| 209 | BankRentOwnInd | RENT_OWN_IND | — | — |
| 210 | BankRequestId | REQUEST_ID | — | — |
| 211 | BankSeblUserKeyLoc | SEBL_USER_KEY_LOC | — | — |
| 212 | BankSicCode | SIC_CODE | — | — |
| 213 | BankSicCodeType | SIC_CODE_TYPE | — | — |
| 214 | BankSmallBusInd | SMALL_BUS_IND | — | — |
| 215 | BankStatus | STATUS | — | — |
| 216 | BankStockSymbol | STOCK_SYMBOL | — | — |
| 217 | BankSuffixOverriddenFlag | SUFFIX_OVERRIDDEN_FLAG | — | — |
| 218 | BankTotalEmpEstInd | TOTAL_EMP_EST_IND | — | — |
| 219 | BankTotalEmpMinInd | TOTAL_EMP_MIN_IND | — | — |
| 220 | BankTotalEmployeesInd | TOTAL_EMPLOYEES_IND | — | — |
| 221 | BankTotalEmployeesText | TOTAL_EMPLOYEES_TEXT | — | — |
| 222 | BankTotalPayments | TOTAL_PAYMENTS | — | — |
| 223 | BankTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 224 | BankUniqueNameAlias | UNIQUE_NAME_ALIAS | — | — |
| 225 | BankUniqueNameSuffix | UNIQUE_NAME_SUFFIX | — | — |
| 226 | BankValidityScore | VALIDITY_SCORE | — | — |
| 227 | BankWomanOwnedInd | WOMAN_OWNED_IND | — | — |
| 228 | BankYearEstablished | YEAR_ESTABLISHED | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankBranchNameAddress1 | ADDRESS1 | — | — |
| 2 | BankBranchNameAddress2 | ADDRESS2 | — | — |
| 3 | BankBranchNameAddress3 | ADDRESS3 | — | — |
| 4 | BankBranchNameAddress4 | ADDRESS4 | — | — |
| 5 | BankBranchNameAnalysisFy | ANALYSIS_FY | — | — |
| 6 | BankBranchNameCategoryCode | CATEGORY_CODE | — | — |
| 7 | BankBranchNameCeoName | CEO_NAME | — | — |
| 8 | BankBranchNameCertReasonCode | CERT_REASON_CODE | — | — |
| 9 | BankBranchNameCertificationLevel | CERTIFICATION_LEVEL | — | — |
| 10 | BankBranchNameCity | CITY | — | — |
| 11 | BankBranchNameComments | COMMENTS | — | — |
| 12 | BankBranchNameCountry | COUNTRY | — | — |
| 13 | BankBranchNameCounty | COUNTY | — | — |
| 14 | BankBranchNameCreatedBy | CREATED_BY | — | — |
| 15 | BankBranchNameCreatedByModule | CREATED_BY_MODULE | — | — |
| 16 | BankBranchNameCreationDate | CREATION_DATE | — | — |
| 17 | BankBranchNameCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 18 | BankBranchNameDateOfBirth | DATE_OF_BIRTH | — | — |
| 19 | BankBranchNameDunsNumberC | DUNS_NUMBER_C | — | — |
| 20 | BankBranchNameEmailAddress | EMAIL_ADDRESS | — | — |
| 21 | BankBranchNameEmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 22 | BankBranchNameFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 23 | BankBranchNameGender | GENDER | — | — |
| 24 | BankBranchNameGroupType | GROUP_TYPE | — | — |
| 25 | BankBranchNameGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | — |
| 26 | BankBranchNameHomeCountry | HOME_COUNTRY | — | — |
| 27 | BankBranchNameHqBranchInd | HQ_BRANCH_IND | — | — |
| 28 | BankBranchNameIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 29 | BankBranchNameIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | — |
| 30 | BankBranchNameInternalFlag | INTERNAL_FLAG | — | — |
| 31 | BankBranchNameJgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 32 | BankBranchNameLanguageName | LANGUAGE_NAME | — | — |
| 33 | BankBranchNameLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 34 | BankBranchNameLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 35 | BankBranchNameLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 36 | BankBranchNameMaritalStatus | MARITAL_STATUS | — | — |
| 37 | BankBranchNameMissionStatement | MISSION_STATEMENT | — | — |
| 38 | BankBranchNameNextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 39 | BankBranchNameObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 40 | BankBranchNameOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 41 | BankBranchNamePartyId | PARTY_ID | — | — |
| 42 | BankBranchNamePartyName | PARTY_NAME | — | — |
| 43 | BankBranchNamePartyNumber | PARTY_NUMBER | — | — |
| 44 | BankBranchNamePartyType | PARTY_TYPE | — | — |
| 45 | BankBranchNamePartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 46 | BankBranchNamePersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 47 | BankBranchNamePersonFirstName | PERSON_FIRST_NAME | — | — |
| 48 | BankBranchNamePersonLastName | PERSON_LAST_NAME | — | — |
| 49 | BankBranchNamePersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 50 | BankBranchNamePersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 51 | BankBranchNamePersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 52 | BankBranchNamePersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 53 | BankBranchNamePersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 54 | BankBranchNamePersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 55 | BankBranchNamePersonTitle | PERSON_TITLE | — | — |
| 56 | BankBranchNamePostalCode | POSTAL_CODE | — | — |
| 57 | BankBranchNamePrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 58 | BankBranchNamePreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 59 | BankBranchNamePreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 60 | BankBranchNamePreferredName | PREFERRED_NAME | — | — |
| 61 | BankBranchNamePreferredNameId | PREFERRED_NAME_ID | — | — |
| 62 | BankBranchNamePrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | — |
| 63 | BankBranchNamePrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 64 | BankBranchNamePrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 65 | BankBranchNamePrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 66 | BankBranchNamePrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 67 | BankBranchNamePrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 68 | BankBranchNamePrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | — |
| 69 | BankBranchNamePrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 70 | BankBranchNamePrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 71 | BankBranchNameProvince | PROVINCE | — | — |
| 72 | BankBranchNameSalutation | SALUTATION | — | — |
| 73 | BankBranchNameSicCode | SIC_CODE | — | — |
| 74 | BankBranchNameSicCodeType | SIC_CODE_TYPE | — | — |
| 75 | BankBranchNameState | STATE | — | — |
| 76 | BankBranchNameStatus | STATUS | — | — |
| 77 | BankBranchNameThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 78 | BankBranchNameTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 79 | BankBranchNameUrl | URL | — | — |
| 80 | BankBranchNameUserGuid | USER_GUID | — | — |
| 81 | BankBranchNameValidatedFlag | VALIDATED_FLAG | — | — |
| 82 | BankBranchNameYearEstablished | YEAR_ESTABLISHED | — | — |
| 83 | BankNameAddress1 | ADDRESS1 | — | — |
| 84 | BankNameAddress2 | ADDRESS2 | — | — |
| 85 | BankNameAddress3 | ADDRESS3 | — | — |
| 86 | BankNameAddress4 | ADDRESS4 | — | — |
| 87 | BankNameAnalysisFy | ANALYSIS_FY | — | — |
| 88 | BankNameCategoryCode | CATEGORY_CODE | — | — |
| 89 | BankNameCeoName | CEO_NAME | — | — |
| 90 | BankNameCertReasonCode | CERT_REASON_CODE | — | — |
| 91 | BankNameCertificationLevel | CERTIFICATION_LEVEL | — | — |
| 92 | BankNameCity | CITY | — | — |
| 93 | BankNameComments | COMMENTS | — | — |
| 94 | BankNameCountry | COUNTRY | — | — |
| 95 | BankNameCounty | COUNTY | — | — |
| 96 | BankNameCreatedBy | CREATED_BY | — | — |
| 97 | BankNameCreatedByModule | CREATED_BY_MODULE | — | — |
| 98 | BankNameCreationDate | CREATION_DATE | — | — |
| 99 | BankNameCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 100 | BankNameDateOfBirth | DATE_OF_BIRTH | — | — |
| 101 | BankNameDunsNumberC | DUNS_NUMBER_C | — | — |
| 102 | BankNameEmailAddress | EMAIL_ADDRESS | — | — |
| 103 | BankNameEmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 104 | BankNameFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 105 | BankNameGender | GENDER | — | — |
| 106 | BankNameGroupType | GROUP_TYPE | — | — |
| 107 | BankNameGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | — |
| 108 | BankNameHomeCountry | HOME_COUNTRY | — | — |
| 109 | BankNameHqBranchInd | HQ_BRANCH_IND | — | — |
| 110 | BankNameIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 111 | BankNameIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | — |
| 112 | BankNameInternalFlag | INTERNAL_FLAG | — | — |
| 113 | BankNameJgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 114 | BankNameLanguageName | LANGUAGE_NAME | — | — |
| 115 | BankNameLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 116 | BankNameLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 117 | BankNameLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 118 | BankNameMaritalStatus | MARITAL_STATUS | — | — |
| 119 | BankNameMissionStatement | MISSION_STATEMENT | — | — |
| 120 | BankNameNextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 121 | BankNameObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 122 | BankNameOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 123 | BankNamePartyId | PARTY_ID | — | — |
| 124 | BankNamePartyName | PARTY_NAME | — | — |
| 125 | BankNamePartyNumber | PARTY_NUMBER | — | — |
| 126 | BankNamePartyType | PARTY_TYPE | — | — |
| 127 | BankNamePartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 128 | BankNamePersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 129 | BankNamePersonFirstName | PERSON_FIRST_NAME | — | — |
| 130 | BankNamePersonLastName | PERSON_LAST_NAME | — | — |
| 131 | BankNamePersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 132 | BankNamePersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 133 | BankNamePersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 134 | BankNamePersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 135 | BankNamePersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 136 | BankNamePersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 137 | BankNamePersonTitle | PERSON_TITLE | — | — |
| 138 | BankNamePostalCode | POSTAL_CODE | — | — |
| 139 | BankNamePrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 140 | BankNamePreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 141 | BankNamePreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 142 | BankNamePreferredName | PREFERRED_NAME | — | — |
| 143 | BankNamePreferredNameId | PREFERRED_NAME_ID | — | — |
| 144 | BankNamePrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | — |
| 145 | BankNamePrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 146 | BankNamePrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 147 | BankNamePrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 148 | BankNamePrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 149 | BankNamePrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 150 | BankNamePrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | — |
| 151 | BankNamePrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 152 | BankNamePrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 153 | BankNameProvince | PROVINCE | — | — |
| 154 | BankNameSalutation | SALUTATION | — | — |
| 155 | BankNameSicCode | SIC_CODE | — | — |
| 156 | BankNameSicCodeType | SIC_CODE_TYPE | — | — |
| 157 | BankNameState | STATE | — | — |
| 158 | BankNameStatus | STATUS | — | — |
| 159 | BankNameThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 160 | BankNameTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 161 | BankNameUrl | URL | — | — |
| 162 | BankNameUserGuid | USER_GUID | — | — |
| 163 | BankNameValidatedFlag | VALIDATED_FLAG | — | — |
| 164 | BankNameYearEstablished | YEAR_ESTABLISHED | — | — |

### [[iby_external_payers_all|IBY_EXTERNAL_PAYERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayersAcctSiteUseId | ACCT_SITE_USE_ID | — | — |
| 2 | PayersBankChargeBearerCode | BANK_CHARGE_BEARER_CODE | — | ✅ |
| 3 | PayersCreatedBy | CREATED_BY | — | — |
| 4 | PayersCreationDate | CREATION_DATE | — | — |
| 5 | PayersCustAccountId | CUST_ACCOUNT_ID | — | — |
| 6 | PayersDebitAdviceDeliveryMethod | DEBIT_ADVICE_DELIVERY_METHOD | — | — |
| 7 | PayersDebitAdviceEmail | DEBIT_ADVICE_EMAIL | — | — |
| 8 | PayersDebitAdviceFax | DEBIT_ADVICE_FAX | — | — |
| 9 | PayersDirdebInstructionCode | DIRDEB_INSTRUCTION_CODE | — | ✅ |
| 10 | PayersExtPayerId | EXT_PAYER_ID | — | — |
| 11 | PayersLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | PayersLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | PayersLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | PayersLocalinstr | LOCALINSTR | — | ✅ |
| 15 | PayersObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | PayersOrgId | ORG_ID | — | — |
| 17 | PayersOrgType | ORG_TYPE | — | — |
| 18 | PayersPartyId | PARTY_ID | — | — |
| 19 | PayersPaymentFunction | PAYMENT_FUNCTION | — | — |
| 20 | PayersPurposeCode | PURPOSE_CODE | — | ✅ |
| 21 | PayersServiceLevel | SERVICE_LEVEL | — | ✅ |

### [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankAccountAccountClassification | ACCOUNT_CLASSIFICATION | — | — |
| 2 | BankAccountAccountSuffix | ACCOUNT_SUFFIX | — | — |
| 3 | BankAccountAgencyLocationCode | AGENCY_LOCATION_CODE | — | — |
| 4 | BankAccountBaMaskSetting | BA_MASK_SETTING | — | — |
| 5 | BankAccountBaNumElecSecSegmentId | BA_NUM_ELEC_SEC_SEGMENT_ID | — | — |
| 6 | BankAccountBaNumSecSegmentId | BA_NUM_SEC_SEGMENT_ID | — | — |
| 7 | BankAccountBaUnmaskLength | BA_UNMASK_LENGTH | — | — |
| 8 | BankAccountBankAccountName | BANK_ACCOUNT_NAME | — | ✅ |
| 9 | BankAccountBankAccountNameAlt | BANK_ACCOUNT_NAME_ALT | — | — |
| 10 | BankAccountBankAccountNum | BANK_ACCOUNT_NUM | — | — |
| 11 | BankAccountBankAccountNumElectronic | BANK_ACCOUNT_NUM_ELECTRONIC | — | — |
| 12 | BankAccountBankAccountType | BANK_ACCOUNT_TYPE | — | ✅ |
| 13 | BankAccountBankId | BANK_ID | — | — |
| 14 | BankAccountBranchId | BRANCH_ID | — | — |
| 15 | BankAccountCheckDigits | CHECK_DIGITS | — | ✅ |
| 16 | BankAccountCountryCode | COUNTRY_CODE | — | — |
| 17 | BankAccountCreatedBy | CREATED_BY | — | — |
| 18 | BankAccountCreationDate | CREATION_DATE | — | — |
| 19 | BankAccountCurrencyCode | CURRENCY_CODE | — | ✅ |
| 20 | BankAccountDescription | DESCRIPTION | — | ✅ |
| 21 | BankAccountEncrypted | ENCRYPTED | — | — |
| 22 | BankAccountEndDate | END_DATE | — | — |
| 23 | BankAccountExchangeRate | EXCHANGE_RATE | — | — |
| 24 | BankAccountExchangeRateAgreementNum | EXCHANGE_RATE_AGREEMENT_NUM | — | — |
| 25 | BankAccountExchangeRateAgreementType | EXCHANGE_RATE_AGREEMENT_TYPE | — | — |
| 26 | BankAccountExtBankAccountId | EXT_BANK_ACCOUNT_ID | — | — |
| 27 | BankAccountForeignPaymentUseFlag | FOREIGN_PAYMENT_USE_FLAG | — | — |
| 28 | BankAccountHedgingContractReference | HEDGING_CONTRACT_REFERENCE | — | — |
| 29 | BankAccountIban | IBAN | — | — |
| 30 | BankAccountIbanHash1 | IBAN_HASH1 | — | — |
| 31 | BankAccountIbanSecSegmentId | IBAN_SEC_SEGMENT_ID | — | — |
| 32 | BankAccountLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 33 | BankAccountLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 34 | BankAccountLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 35 | BankAccountMaskedBankAccountNum | MASKED_BANK_ACCOUNT_NUM | — | ✅ |
| 36 | BankAccountMaskedIban | MASKED_IBAN | — | ✅ |
| 37 | BankAccountObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 38 | BankAccountPaymentFactorFlag | PAYMENT_FACTOR_FLAG | — | — |
| 39 | BankAccountProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 40 | BankAccountProgramId | PROGRAM_ID | — | — |
| 41 | BankAccountProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 42 | BankAccountRequestId | REQUEST_ID | — | — |
| 43 | BankAccountSaltVersion | SALT_VERSION | — | — |
| 44 | BankAccountSecondaryAccountReference | SECONDARY_ACCOUNT_REFERENCE | — | — |
| 45 | BankAccountShortAcctName | SHORT_ACCT_NAME | — | — |
| 46 | BankAccountStartDate | START_DATE | — | — |

### [[iby_pmt_instr_uses_all|IBY_PMT_INSTR_USES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InstrumentPaymentUseId | INSTRUMENT_PAYMENT_USE_ID | 🔑 | ✅ |
| 2 | UseCreatedBy | CREATED_BY | — | — |
| 3 | UseCreationDate | CREATION_DATE | — | — |
| 4 | UseEndDate | END_DATE | — | — |
| 5 | UseExtPmtPartyId | EXT_PMT_PARTY_ID | — | — |
| 6 | UseInstrumentId | INSTRUMENT_ID | — | — |
| 7 | UseInstrumentType | INSTRUMENT_TYPE | — | — |
| 8 | UseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | UseLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | UseLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | UseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | UsePaymentFlow | PAYMENT_FLOW | — | — |
| 13 | UsePaymentFunction | PAYMENT_FUNCTION | — | — |
| 14 | UsePrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 15 | UseStartDate | START_DATE | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
