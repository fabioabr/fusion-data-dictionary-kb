---
id: DOC-AR-PVO-SiteTaxRegistration
doc_type: system-doc
title: "SiteTaxRegistration — PVO Accounts Receivable"
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
  - SiteTaxRegistration
  - sitetaxregistration
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SiteTaxRegistration

## 📌 Visão Geral

Extrai os registros fiscais (inscrições estaduais, CNPJ) de sites de clientes por jurisdição e regime tributário. Fundamental para emissão correta de documentos fiscais e compliance tributário.

**Caminho:** `FscmTopModelAM.FinArCustomersPublicModelAM.SiteTaxRegistration`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 202 | 5 | 1 | 17 | 8% |

---

## 🔗 Tabelas Relacionadas

- [[hz_parties|HZ_PARTIES]] — 4 atributos (1 BICC)
- [[zx_jurisdictions_vl|ZX_JURISDICTIONS_VL]] — 32 atributos (2 BICC)
- [[zx_party_tax_profile|ZX_PARTY_TAX_PROFILE]] — 49 atributos (1 PKs, 2 BICC)
- [[zx_regimes_vl|ZX_REGIMES_VL]] — 65 atributos (3 BICC)
- [[zx_registrations|ZX_REGISTRATIONS]] — 52 atributos (9 BICC)

---

## ⚙️ Atributos

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxAuthPartyPartyId | PARTY_ID | — | — |
| 2 | TaxAuthPartyPartyName | PARTY_NAME | — | ✅ |
| 3 | TaxAuthPartyPartyNumber | PARTY_NUMBER | — | — |
| 4 | TaxAuthPartyPartyType | PARTY_TYPE | — | — |

### [[zx_jurisdictions_vl|ZX_JURISDICTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxJurisdictionAllowTaxRegistrationsFlag | ALLOW_TAX_REGISTRATIONS_FLAG | — | — |
| 2 | TaxJurisdictionCollTaxAuthorityId | COLL_TAX_AUTHORITY_ID | — | — |
| 3 | TaxJurisdictionCreatedBy | CREATED_BY | — | — |
| 4 | TaxJurisdictionCreationDate | CREATION_DATE | — | — |
| 5 | TaxJurisdictionDefaultFlgEffectiveFrom | DEFAULT_FLG_EFFECTIVE_FROM | — | — |
| 6 | TaxJurisdictionDefaultFlgEffectiveTo | DEFAULT_FLG_EFFECTIVE_TO | — | — |
| 7 | TaxJurisdictionDefaultJurisdictionFlag | DEFAULT_JURISDICTION_FLAG | — | — |
| 8 | TaxJurisdictionEffectiveFrom | EFFECTIVE_FROM | — | — |
| 9 | TaxJurisdictionEffectiveTo | EFFECTIVE_TO | — | — |
| 10 | TaxJurisdictionInnerCityJurisdictionFlag | INNER_CITY_JURISDICTION_FLAG | — | — |
| 11 | TaxJurisdictionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | TaxJurisdictionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | TaxJurisdictionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | TaxJurisdictionObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 15 | TaxJurisdictionObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 16 | TaxJurisdictionPrecedenceLevel | PRECEDENCE_LEVEL | — | — |
| 17 | TaxJurisdictionProgramAppName | PROGRAM_APP_NAME | — | — |
| 18 | TaxJurisdictionProgramLoginId | PROGRAM_LOGIN_ID | — | — |
| 19 | TaxJurisdictionProgramName | PROGRAM_NAME | — | — |
| 20 | TaxJurisdictionRecordTypeCode | RECORD_TYPE_CODE | — | — |
| 21 | TaxJurisdictionRepTaxAuthorityId | REP_TAX_AUTHORITY_ID | — | — |
| 22 | TaxJurisdictionRequestId | REQUEST_ID | — | — |
| 23 | TaxJurisdictionTax | TAX | — | — |
| 24 | TaxJurisdictionTaxAcctSrcJurisdictId | TAX_ACCT_SRC_JURISDICT_ID | — | — |
| 25 | TaxJurisdictionTaxExmptSrcJurisdictId | TAX_EXMPT_SRC_JURISDICT_ID | — | — |
| 26 | TaxJurisdictionTaxJurisdictionCode | TAX_JURISDICTION_CODE | — | — |
| 27 | TaxJurisdictionTaxJurisdictionId | TAX_JURISDICTION_ID | — | — |
| 28 | TaxJurisdictionTaxJurisdictionName | TAX_JURISDICTION_NAME | — | ✅ |
| 29 | TaxJurisdictionTaxRegimeCode | TAX_REGIME_CODE | — | — |
| 30 | TaxJurisdictionThrshldScheduleGrpLvlFlag | THRSHLD_SCHEDULE_GRP_LVL_FLAG | — | — |
| 31 | TaxJurisdictionWhtBucketLevelFlag | WHT_BUCKET_LEVEL_FLAG | — | — |
| 32 | TaxJurisdictionZoneGeographyId | ZONE_GEOGRAPHY_ID | — | — |

### [[zx_party_tax_profile|ZX_PARTY_TAX_PROFILE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyTaxAuthProfPartyId | PARTY_ID | — | — |
| 2 | PartyTaxAuthProfPartyTaxProfileId | PARTY_TAX_PROFILE_ID | — | — |
| 3 | PartyTaxAuthProfPartyTypeCode | PARTY_TYPE_CODE | — | — |
| 4 | PartyTaxProfileAllowAwtFlag | ALLOW_AWT_FLAG | — | — |
| 5 | PartyTaxProfileAllowOffsetTaxFlag | ALLOW_OFFSET_TAX_FLAG | — | — |
| 6 | PartyTaxProfileAllowZeroAmtWhtInvFlag | ALLOW_ZERO_AMT_WHT_INV_FLAG | — | — |
| 7 | PartyTaxProfileCollectingAuthorityFlag | COLLECTING_AUTHORITY_FLAG | — | — |
| 8 | PartyTaxProfileCountryCode | COUNTRY_CODE | — | — |
| 9 | PartyTaxProfileCreateAwtDistsTypeCode | CREATE_AWT_DISTS_TYPE_CODE | — | — |
| 10 | PartyTaxProfileCreateAwtInvoicesTypeCode | CREATE_AWT_INVOICES_TYPE_CODE | — | — |
| 11 | PartyTaxProfileCreatedBy | CREATED_BY | — | — |
| 12 | PartyTaxProfileCreationDate | CREATION_DATE | — | — |
| 13 | PartyTaxProfileCustomerFlag | CUSTOMER_FLAG | — | — |
| 14 | PartyTaxProfileEffectiveFromUseLe | EFFECTIVE_FROM_USE_LE | — | — |
| 15 | PartyTaxProfileFirstPartyLeFlag | FIRST_PARTY_LE_FLAG | — | — |
| 16 | PartyTaxProfileId | PARTY_TAX_PROFILE_ID | 🔑 | ✅ |
| 17 | PartyTaxProfileInclusiveTaxFlag | INCLUSIVE_TAX_FLAG | — | — |
| 18 | PartyTaxProfileLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | PartyTaxProfileLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | PartyTaxProfileLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 21 | PartyTaxProfileLegalEstablishmentFlag | LEGAL_ESTABLISHMENT_FLAG | — | — |
| 22 | PartyTaxProfileMergedStatusCode | MERGED_STATUS_CODE | — | — |
| 23 | PartyTaxProfileMergedToPtpId | MERGED_TO_PTP_ID | — | — |
| 24 | PartyTaxProfileObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 25 | PartyTaxProfilePartyId | PARTY_ID | — | — |
| 26 | PartyTaxProfilePartyTypeCode | PARTY_TYPE_CODE | — | — |
| 27 | PartyTaxProfileProcessForApplicabilityFlag | PROCESS_FOR_APPLICABILITY_FLAG | — | — |
| 28 | PartyTaxProfileProgramAppName | PROGRAM_APP_NAME | — | — |
| 29 | PartyTaxProfileProgramLoginId | PROGRAM_LOGIN_ID | — | — |
| 30 | PartyTaxProfileProgramName | PROGRAM_NAME | — | — |
| 31 | PartyTaxProfileProviderTypeCode | PROVIDER_TYPE_CODE | — | — |
| 32 | PartyTaxProfileRecordTypeCode | RECORD_TYPE_CODE | — | — |
| 33 | PartyTaxProfileRegistrationTypeCode | REGISTRATION_TYPE_CODE | — | — |
| 34 | PartyTaxProfileRepRegistrationNumber | REP_REGISTRATION_NUMBER | — | — |
| 35 | PartyTaxProfileReportingAuthorityFlag | REPORTING_AUTHORITY_FLAG | — | — |
| 36 | PartyTaxProfileRequestId | REQUEST_ID | — | — |
| 37 | PartyTaxProfileRoundingLevelCode | ROUNDING_LEVEL_CODE | — | — |
| 38 | PartyTaxProfileRoundingRuleCode | ROUNDING_RULE_CODE | — | — |
| 39 | PartyTaxProfileSelfAssessFlag | SELF_ASSESS_FLAG | — | — |
| 40 | PartyTaxProfileSiteFlag | SITE_FLAG | — | — |
| 41 | PartyTaxProfileSupplierFlag | SUPPLIER_FLAG | — | — |
| 42 | PartyTaxProfileTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 43 | PartyTaxProfileUseLeAsSubscriberFlag | USE_LE_AS_SUBSCRIBER_FLAG | — | — |
| 44 | PartyTaxProfileWhtDateBasis | WHT_DATE_BASIS | — | — |
| 45 | PartyTaxProfileWhtEffectiveFromUseLe | WHT_EFFECTIVE_FROM_USE_LE | — | — |
| 46 | PartyTaxProfileWhtRoundingLevelCode | WHT_ROUNDING_LEVEL_CODE | — | — |
| 47 | PartyTaxProfileWhtRoundingRuleCode | WHT_ROUNDING_RULE_CODE | — | — |
| 48 | PartyTaxProfileWhtUseLeAsSubscriberFlag | WHT_USE_LE_AS_SUBSCRIBER_FLAG | — | — |
| 49 | PartyTaxProfileWithholdingStartDate | WITHHOLDING_START_DATE | — | — |

### [[zx_regimes_vl|ZX_REGIMES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxRegimeAllowExceptionsFlag | ALLOW_EXCEPTIONS_FLAG | — | — |
| 2 | TaxRegimeAllowExemptionsFlag | ALLOW_EXEMPTIONS_FLAG | — | — |
| 3 | TaxRegimeAllowRecoverabilityFlag | ALLOW_RECOVERABILITY_FLAG | — | — |
| 4 | TaxRegimeAllowRoundingOverrideFlag | ALLOW_ROUNDING_OVERRIDE_FLAG | — | — |
| 5 | TaxRegimeApplicabilityRuleFlag | APPLICABILITY_RULE_FLAG | — | — |
| 6 | TaxRegimeAutoPrvnFlag | AUTO_PRVN_FLAG | — | — |
| 7 | TaxRegimeBucketLevelFlag | BUCKET_LEVEL_FLAG | — | — |
| 8 | TaxRegimeCollTaxAuthorityId | COLL_TAX_AUTHORITY_ID | — | — |
| 9 | TaxRegimeCountryCode | COUNTRY_CODE | — | — |
| 10 | TaxRegimeCountryOrGroupCode | COUNTRY_OR_GROUP_CODE | — | — |
| 11 | TaxRegimeCreatedBy | CREATED_BY | — | — |
| 12 | TaxRegimeCreationDate | CREATION_DATE | — | — |
| 13 | TaxRegimeCrossRegimeCompoundingFlag | CROSS_REGIME_COMPOUNDING_FLAG | — | — |
| 14 | TaxRegimeDefInclusiveTaxFlag | DEF_INCLUSIVE_TAX_FLAG | — | — |
| 15 | TaxRegimeDefPlaceOfSupplyTypeCode | DEF_PLACE_OF_SUPPLY_TYPE_CODE | — | — |
| 16 | TaxRegimeDefRecSettlementOptionCode | DEF_REC_SETTLEMENT_OPTION_CODE | — | — |
| 17 | TaxRegimeDefRegistrPartyTypeCode | DEF_REGISTR_PARTY_TYPE_CODE | — | — |
| 18 | TaxRegimeEffectiveFrom | EFFECTIVE_FROM | — | — |
| 19 | TaxRegimeEffectiveTo | EFFECTIVE_TO | — | — |
| 20 | TaxRegimeExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 21 | TaxRegimeExemptionProcessFlag | EXEMPTION_PROCESS_FLAG | — | — |
| 22 | TaxRegimeGeographyId | GEOGRAPHY_ID | — | — |
| 23 | TaxRegimeGeographyType | GEOGRAPHY_TYPE | — | — |
| 24 | TaxRegimeHasExchRateDateRuleFlag | HAS_EXCH_RATE_DATE_RULE_FLAG | — | — |
| 25 | TaxRegimeHasOtherJurisdictionsFlag | HAS_OTHER_JURISDICTIONS_FLAG | — | — |
| 26 | TaxRegimeHasSubRegimeFlag | HAS_SUB_REGIME_FLAG | — | — |
| 27 | TaxRegimeHasTaxDetDateRuleFlag | HAS_TAX_DET_DATE_RULE_FLAG | — | — |
| 28 | TaxRegimeHasTaxPointDateRuleFlag | HAS_TAX_POINT_DATE_RULE_FLAG | — | — |
| 29 | TaxRegimeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | TaxRegimeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 31 | TaxRegimeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 32 | TaxRegimeMinimumAccountableUnit | MINIMUM_ACCOUNTABLE_UNIT | — | — |
| 33 | TaxRegimeObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 34 | TaxRegimeObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 35 | TaxRegimeParentRegimeCode | PARENT_REGIME_CODE | — | — |
| 36 | TaxRegimePeriodSetName | PERIOD_SET_NAME | — | — |
| 37 | TaxRegimePlaceOfSupplyRuleFlag | PLACE_OF_SUPPLY_RULE_FLAG | — | — |
| 38 | TaxRegimeProgramAppName | PROGRAM_APP_NAME | — | — |
| 39 | TaxRegimeProgramLoginId | PROGRAM_LOGIN_ID | — | — |
| 40 | TaxRegimeProgramName | PROGRAM_NAME | — | — |
| 41 | TaxRegimeRecordTypeCode | RECORD_TYPE_CODE | — | — |
| 42 | TaxRegimeRegimePrecedence | REGIME_PRECEDENCE | — | — |
| 43 | TaxRegimeRegimeTypeFlag | REGIME_TYPE_FLAG | — | ✅ |
| 44 | TaxRegimeRegistrationTypeRuleFlag | REGISTRATION_TYPE_RULE_FLAG | — | — |
| 45 | TaxRegimeRegnNumSameAsLeFlag | REGN_NUM_SAME_AS_LE_FLAG | — | — |
| 46 | TaxRegimeRepTaxAuthorityId | REP_TAX_AUTHORITY_ID | — | — |
| 47 | TaxRegimeRequestId | REQUEST_ID | — | — |
| 48 | TaxRegimeTaxAccountPrecedenceCode | TAX_ACCOUNT_PRECEDENCE_CODE | — | — |
| 49 | TaxRegimeTaxAmtThrshldFlag | TAX_AMT_THRSHLD_FLAG | — | — |
| 50 | TaxRegimeTaxCalcRuleFlag | TAX_CALC_RULE_FLAG | — | — |
| 51 | TaxRegimeTaxCurrencyCode | TAX_CURRENCY_CODE | — | — |
| 52 | TaxRegimeTaxInclusiveOverrideFlag | TAX_INCLUSIVE_OVERRIDE_FLAG | — | — |
| 53 | TaxRegimeTaxPrecision | TAX_PRECISION | — | — |
| 54 | TaxRegimeTaxRateRuleFlag | TAX_RATE_RULE_FLAG | — | — |
| 55 | TaxRegimeTaxRateThrshldFlag | TAX_RATE_THRSHLD_FLAG | — | — |
| 56 | TaxRegimeTaxRegimeCode | TAX_REGIME_CODE | — | — |
| 57 | TaxRegimeTaxRegimeId | TAX_REGIME_ID | — | — |
| 58 | TaxRegimeTaxRegimeName | TAX_REGIME_NAME | — | ✅ |
| 59 | TaxRegimeTaxStatusRuleFlag | TAX_STATUS_RULE_FLAG | — | — |
| 60 | TaxRegimeTaxableBasisRuleFlag | TAXABLE_BASIS_RULE_FLAG | — | — |
| 61 | TaxRegimeTaxableBasisThrshldFlag | TAXABLE_BASIS_THRSHLD_FLAG | — | — |
| 62 | TaxRegimeThrshldChkTmpltCode | THRSHLD_CHK_TMPLT_CODE | — | — |
| 63 | TaxRegimeThrshldGroupingLvlCode | THRSHLD_GROUPING_LVL_CODE | — | — |
| 64 | TaxRegimeUseLegalMsgFlag | USE_LEGAL_MSG_FLAG | — | — |
| 65 | TaxRegimeUseTaxReportConfigFlag | USE_TAX_REPORT_CONFIG_FLAG | — | — |

### [[zx_registrations|ZX_REGISTRATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RegistrationId | REGISTRATION_ID | — | — |
| 2 | TaxRegistrationAccountId | ACCOUNT_ID | — | — |
| 3 | TaxRegistrationAccountSiteId | ACCOUNT_SITE_ID | — | — |
| 4 | TaxRegistrationAccountTypeCode | ACCOUNT_TYPE_CODE | — | — |
| 5 | TaxRegistrationBankAccountNum | BANK_ACCOUNT_NUM | — | — |
| 6 | TaxRegistrationBankBranchId | BANK_BRANCH_ID | — | — |
| 7 | TaxRegistrationBankId | BANK_ID | — | — |
| 8 | TaxRegistrationCollTaxAuthorityId | COLL_TAX_AUTHORITY_ID | — | — |
| 9 | TaxRegistrationCreatedBy | CREATED_BY | — | — |
| 10 | TaxRegistrationCreationDate | CREATION_DATE | — | — |
| 11 | TaxRegistrationDefaultRegistrationFlag | DEFAULT_REGISTRATION_FLAG | — | ✅ |
| 12 | TaxRegistrationEffectiveFrom | EFFECTIVE_FROM | — | ✅ |
| 13 | TaxRegistrationEffectiveTo | EFFECTIVE_TO | — | ✅ |
| 14 | TaxRegistrationHasTaxExemptionsFlag | HAS_TAX_EXEMPTIONS_FLAG | — | — |
| 15 | TaxRegistrationInclusiveTaxFlag | INCLUSIVE_TAX_FLAG | — | — |
| 16 | TaxRegistrationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | TaxRegistrationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | TaxRegistrationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | TaxRegistrationLegalLocationId | LEGAL_LOCATION_ID | — | — |
| 20 | TaxRegistrationLegalRegistrationId | LEGAL_REGISTRATION_ID | — | — |
| 21 | TaxRegistrationMaxSelfAssessDiffTolLimit | MAX_SELF_ASSESS_DIFF_TOL_LIMIT | — | — |
| 22 | TaxRegistrationMergedToRegistrationId | MERGED_TO_REGISTRATION_ID | — | — |
| 23 | TaxRegistrationMinSelfAssessDiffTolLimit | MIN_SELF_ASSESS_DIFF_TOL_LIMIT | — | — |
| 24 | TaxRegistrationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 25 | TaxRegistrationPartyTaxProfileId | PARTY_TAX_PROFILE_ID | — | — |
| 26 | TaxRegistrationProgramAppName | PROGRAM_APP_NAME | — | — |
| 27 | TaxRegistrationProgramLoginId | PROGRAM_LOGIN_ID | — | — |
| 28 | TaxRegistrationProgramName | PROGRAM_NAME | — | — |
| 29 | TaxRegistrationRecordTypeCode | RECORD_TYPE_CODE | — | — |
| 30 | TaxRegistrationRegistrationNumber | REGISTRATION_NUMBER | — | ✅ |
| 31 | TaxRegistrationRegistrationReasonCode | REGISTRATION_REASON_CODE | — | — |
| 32 | TaxRegistrationRegistrationSourceCode | REGISTRATION_SOURCE_CODE | — | — |
| 33 | TaxRegistrationRegistrationStatusCode | REGISTRATION_STATUS_CODE | — | — |
| 34 | TaxRegistrationRegistrationTypeCode | REGISTRATION_TYPE_CODE | — | ✅ |
| 35 | TaxRegistrationRepPartyTaxName | REP_PARTY_TAX_NAME | — | — |
| 36 | TaxRegistrationRepTaxAuthorityId | REP_TAX_AUTHORITY_ID | — | — |
| 37 | TaxRegistrationRequestId | REQUEST_ID | — | — |
| 38 | TaxRegistrationRoundingLevelCode | ROUNDING_LEVEL_CODE | — | — |
| 39 | TaxRegistrationRoundingRuleCode | ROUNDING_RULE_CODE | — | — |
| 40 | TaxRegistrationSelfAssessDiffTolLmtFlag | SELF_ASSESS_DIFF_TOL_LMT_FLAG | — | — |
| 41 | TaxRegistrationSelfAssessFlag | SELF_ASSESS_FLAG | — | — |
| 42 | TaxRegistrationTax | TAX | — | ✅ |
| 43 | TaxRegistrationTaxAuthorityId | TAX_AUTHORITY_ID | — | — |
| 44 | TaxRegistrationTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 45 | TaxRegistrationTaxJurisdictionCode | TAX_JURISDICTION_CODE | — | ✅ |
| 46 | TaxRegistrationTaxPointBasis | TAX_POINT_BASIS | — | — |
| 47 | TaxRegistrationTaxRegimeCode | TAX_REGIME_CODE | — | ✅ |
| 48 | TaxRegistrationUniquenessValidationLevel | UNIQUENESS_VALIDATION_LEVEL | — | — |
| 49 | TaxRegistrationValidationLevel | VALIDATION_LEVEL | — | — |
| 50 | TaxRegistrationValidationRoutine | VALIDATION_ROUTINE | — | — |
| 51 | TaxRegistrationValidationRule | VALIDATION_RULE | — | — |
| 52 | TaxRegistrationValidationType | VALIDATION_TYPE | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
