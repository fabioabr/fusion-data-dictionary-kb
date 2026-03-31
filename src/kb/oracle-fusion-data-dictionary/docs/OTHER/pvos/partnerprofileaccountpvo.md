---
id: DOC-OTHER-PVO-PartnerProfileAccountPVO
doc_type: system-doc
title: "PartnerProfileAccountPVO — PVO Cross-Module"
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
  - PartnerProfileAccountPVO
  - partnerprofileaccountpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PartnerProfileAccountPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Partner Profile Account. Acessa as tabelas: HZ_ORGANIZATION_PROFILES, HZ_PARTIES, HZ_PERSON_PROFILES (+2).

**Caminho:** `FscmTopModelAM.PartnerCenterAnalyticsAM.PartnerProfileAccountPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 105 | 5 | 1 | 84 | 80% |

---

## 🔗 Tabelas Relacionadas

- [[hz_organization_profiles|HZ_ORGANIZATION_PROFILES]] — 40 atributos (37 BICC)
- [[hz_parties|HZ_PARTIES]] — 22 atributos (18 BICC)
- [[hz_person_profiles|HZ_PERSON_PROFILES]] — 5 atributos (4 BICC)
- [[zpm_partner_accounts|ZPM_PARTNER_ACCOUNTS]] — 3 atributos (2 BICC)
- [[zpm_partner_profiles|ZPM_PARTNER_PROFILES]] — 35 atributos (1 PKs, 23 BICC)

---

## ⚙️ Atributos

### [[hz_organization_profiles|HZ_ORGANIZATION_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AnalysisFy | ANALYSIS_FY | — | ✅ |
| 2 | BusinessScope | BUSINESS_SCOPE | — | ✅ |
| 3 | CeoName | CEO_NAME | — | ✅ |
| 4 | CeoTitle | CEO_TITLE | — | ✅ |
| 5 | CertReasonCode | CERT_REASON_CODE | — | ✅ |
| 6 | CertificationLevel | CERTIFICATION_LEVEL | — | ✅ |
| 7 | ControlYr | CONTROL_YR | — | ✅ |
| 8 | CurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | ✅ |
| 9 | DbRating | DB_RATING | — | ✅ |
| 10 | DunsNumberC | DUNS_NUMBER_C | — | ✅ |
| 11 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 12 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 13 | EmployeesTotal | EMPLOYEES_TOTAL | — | ✅ |
| 14 | ExportInd | EXPORT_IND | — | ✅ |
| 15 | FiscalYearendMonth | FISCAL_YEAREND_MONTH | — | ✅ |
| 16 | GsaIndicatorFlag | GSA_INDICATOR_FLAG | — | ✅ |
| 17 | HomeCountry | HOME_COUNTRY | — | ✅ |
| 18 | IncorpYear | INCORP_YEAR | — | ✅ |
| 19 | JgzzFiscalCode | JGZZ_FISCAL_CODE | — | ✅ |
| 20 | LegalStatus | LEGAL_STATUS | — | ✅ |
| 21 | LineOfBusiness | LINE_OF_BUSINESS | — | ✅ |
| 22 | MinorityOwnedInd | MINORITY_OWNED_IND | — | ✅ |
| 23 | MinorityOwnedType | MINORITY_OWNED_TYPE | — | ✅ |
| 24 | NextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | ✅ |
| 25 | OrganizationName | ORGANIZATION_NAME | — | ✅ |
| 26 | OrganizationProfileId | ORGANIZATION_PROFILE_ID | — | — |
| 27 | OrganizationSize | ORGANIZATION_SIZE | — | ✅ |
| 28 | PartyId | PARTY_ID | — | — |
| 29 | PrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 30 | PreferredContactMethod | PREFERRED_CONTACT_METHOD | — | ✅ |
| 31 | PrincipalName | PRINCIPAL_NAME | — | ✅ |
| 32 | PrincipalTitle | PRINCIPAL_TITLE | — | ✅ |
| 33 | PublicPrivateOwnershipFlag | PUBLIC_PRIVATE_OWNERSHIP_FLAG | — | ✅ |
| 34 | RegistrationType | REGISTRATION_TYPE | — | ✅ |
| 35 | SmallBusInd | SMALL_BUS_IND | — | ✅ |
| 36 | StockSymbol | STOCK_SYMBOL | — | ✅ |
| 37 | TotalEmployeesInd | TOTAL_EMPLOYEES_IND | — | ✅ |
| 38 | TotalEmployeesText | TOTAL_EMPLOYEES_TEXT | — | ✅ |
| 39 | UniqueNameSuffix | UNIQUE_NAME_SUFFIX | — | ✅ |
| 40 | YearEstablished | YEAR_ESTABLISHED | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChannelManagerPartyPEOPartyId | PARTY_ID | — | ✅ |
| 2 | ChannelManagerPartyPEOPartyName | PARTY_NAME | — | ✅ |
| 3 | IdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | — |
| 4 | ParentPartyId | PARTY_ID | — | ✅ |
| 5 | ParentPartyName | PARTY_NAME | — | ✅ |
| 6 | PartnerIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 7 | PartnerPartyPEOAddress1 | ADDRESS1 | — | ✅ |
| 8 | PartnerPartyPEOAddress2 | ADDRESS2 | — | ✅ |
| 9 | PartnerPartyPEOAddress3 | ADDRESS3 | — | ✅ |
| 10 | PartnerPartyPEOAddress4 | ADDRESS4 | — | ✅ |
| 11 | PartnerPartyPEOCity | CITY | — | ✅ |
| 12 | PartnerPartyPEOCountry | COUNTRY | — | ✅ |
| 13 | PartnerPartyPEOCounty | COUNTY | — | ✅ |
| 14 | PartnerPartyPEOPartyId | PARTY_ID | — | ✅ |
| 15 | PartnerPartyPEOPartyName | PARTY_NAME | — | ✅ |
| 16 | PartnerPartyPEOPostalCode | POSTAL_CODE | — | ✅ |
| 17 | PartnerPartyPEOProvince | PROVINCE | — | ✅ |
| 18 | PartnerPartyPEOState | STATE | — | ✅ |
| 19 | PartyNumber | PARTY_NUMBER | — | ✅ |
| 20 | PrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 21 | PrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 22 | Url | URL | — | ✅ |

### [[hz_person_profiles|HZ_PERSON_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChannelManagerPersonPEOPartyId | PARTY_ID | — | ✅ |
| 2 | ChannelManagerPersonPEOPartyName | PERSON_NAME | — | ✅ |
| 3 | ChannelManagerPersonPEOPersonProfileId | PERSON_PROFILE_ID | — | ✅ |
| 4 | ChannelMgrEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 5 | ChannelMgrEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |

### [[zpm_partner_accounts|ZPM_PARTNER_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartnerAccountPEOAccountDirectorId | ACCOUNT_DIRECTOR_ID | — | ✅ |
| 2 | PartnerAccountPEOPartnerAccountId | PARTNER_ACCOUNT_ID | — | ✅ |
| 3 | PartnerPartyId | PARTNER_PARTY_ID | — | — |

### [[zpm_partner_profiles|ZPM_PARTNER_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LastTerritoryAssignedDate | LAST_TERRITORY_ASSIGNED_DATE | — | ✅ |
| 2 | LockTerritoryAssignment | LOCK_TERRITORY_ASSIGNMENT | — | ✅ |
| 3 | ParentPartnerPartyId | PARENT_PARTNER_PARTY_ID | — | ✅ |
| 4 | PartnerProfilePEOAnnualRevenue | ANNUAL_REVENUE | — | ✅ |
| 5 | PartnerProfilePEOCompanyNumber | COMPANY_NUMBER | — | ✅ |
| 6 | PartnerProfilePEOComplianceReviewedDate | COMPLIANCE_REVIEWED_DATE | — | ✅ |
| 7 | PartnerProfilePEOComplianceStatus | COMPLIANCE_STATUS | — | ✅ |
| 8 | PartnerProfilePEOCorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 9 | PartnerProfilePEOCreatedBy | CREATED_BY | — | ✅ |
| 10 | PartnerProfilePEOCreationDate | CREATION_DATE | — | ✅ |
| 11 | PartnerProfilePEOCurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 12 | PartnerProfilePEOCurrencyCode | CURRENCY_CODE | — | — |
| 13 | PartnerProfilePEODescription | DESCRIPTION | — | ✅ |
| 14 | PartnerProfilePEOEligibleForPublicProfile | ELIGIBLE_FOR_PUBLIC_PROFILE | — | — |
| 15 | PartnerProfilePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | PartnerProfilePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | PartnerProfilePEOLocation | LOCATION | — | ✅ |
| 18 | PartnerProfilePEOOpportunitiesWonPriorYear | OPPORTUNITIES_WON_PRIOR_YEAR | — | ✅ |
| 19 | PartnerProfilePEOOpportunitiesWonYtd | OPPORTUNITIES_WON_YTD | — | ✅ |
| 20 | PartnerProfilePEOPartnerLevel | PARTNER_LEVEL | — | ✅ |
| 21 | PartnerProfilePEOPartnerStatus | STATUS | — | ✅ |
| 22 | PartnerProfilePEOPartnerSummary | PARTNER_SUMMARY | — | ✅ |
| 23 | PartnerProfilePEOPartyId | PARTY_ID | 🔑 | ✅ |
| 24 | PartnerProfilePEOPublicAddressId | PUBLIC_ADDRESS_ID | — | — |
| 25 | PartnerProfilePEOPublicContactId | PUBLIC_CONTACT_ID | — | — |
| 26 | PartnerProfilePEOPublicEmailId | PUBLIC_EMAIL_ID | — | — |
| 27 | PartnerProfilePEOPublicFaxId | PUBLIC_FAX_ID | — | — |
| 28 | PartnerProfilePEOPublicPhoneId | PUBLIC_PHONE_ID | — | — |
| 29 | PartnerProfilePEOPublicStatus | PUBLIC_STATUS | — | — |
| 30 | PartnerProfilePEOSolutionOverview | SOLUTION_OVERVIEW | — | — |
| 31 | PartnerProfilePEOSynergy | SYNERGY | — | — |
| 32 | PartnerProfilePEOTierId | TIER_ID | — | ✅ |
| 33 | ReassignTerritory | REASSIGN_TERRITORY | — | ✅ |
| 34 | TreeCode | TREE_CODE | — | ✅ |
| 35 | TreeStructureCode | TREE_STRUCTURE_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
