---
id: DOC-AR-PVO-SiteTaxExemption
doc_type: system-doc
title: "SiteTaxExemption — PVO Accounts Receivable"
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
  - SiteTaxExemption
  - sitetaxexemption
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SiteTaxExemption

## 📌 Visão Geral

Extrai as isenções fiscais concedidas a sites de clientes, com jurisdição, regime tributário e período de validade. Essencial para aplicação correta de benefícios fiscais por localidade e conformidade tributária.

**Caminho:** `FscmTopModelAM.FinArCustomersPublicModelAM.SiteTaxExemption`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 188 | 8 | 1 | 25 | 13% |

---

## 🔗 Tabelas Relacionadas

- [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]] — 6 atributos (3 BICC)
- [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]] — 16 atributos (1 BICC)
- [[hz_parties|HZ_PARTIES]] — 5 atributos (1 BICC)
- [[inv_org_parameters|INV_ORG_PARAMETERS]] — 4 atributos (2 BICC)
- [[zx_exemptions|ZX_EXEMPTIONS]] — 37 atributos (12 BICC)
- [[zx_jurisdictions_vl|ZX_JURISDICTIONS_VL]] — 10 atributos (2 BICC)
- [[zx_party_tax_profile|ZX_PARTY_TAX_PROFILE]] — 49 atributos (1 PKs, 2 BICC)
- [[zx_regimes_vl|ZX_REGIMES_VL]] — 61 atributos (2 BICC)

---

## ⚙️ Atributos

### [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemInventoryItemFlag | INVENTORY_ITEM_FLAG | — | — |
| 2 | ItemInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 3 | ItemInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 4 | ItemItemNumber | ITEM_NUMBER | — | ✅ |
| 5 | ItemItemType | ITEM_TYPE | — | — |
| 6 | ItemOrganizationId | ORGANIZATION_ID | — | ✅ |

### [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationUnitBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | OrganizationUnitCreatedBy | CREATED_BY | — | — |
| 3 | OrganizationUnitCreationDate | CREATION_DATE | — | — |
| 4 | OrganizationUnitEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 5 | OrganizationUnitEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 6 | OrganizationUnitEstablishmentId | ESTABLISHMENT_ID | — | — |
| 7 | OrganizationUnitInternalAddressLine | INTERNAL_ADDRESS_LINE | — | — |
| 8 | OrganizationUnitInternalExternalFlag | INTERNAL_EXTERNAL_FLAG | — | — |
| 9 | OrganizationUnitLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | OrganizationUnitLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | OrganizationUnitLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | OrganizationUnitLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 13 | OrganizationUnitLocationId | LOCATION_ID | — | — |
| 14 | OrganizationUnitObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 15 | OrganizationUnitOrganizationId | ORGANIZATION_ID | — | — |
| 16 | OrganizationUnitType | TYPE | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyPartyId | PARTY_ID | — | — |
| 2 | PartyPartyName | PARTY_NAME | — | ✅ |
| 3 | PartyPartyNumber | PARTY_NUMBER | — | — |
| 4 | PartyPartyType | PARTY_TYPE | — | — |
| 5 | PartyPartyUniqueName | PARTY_UNIQUE_NAME | — | — |

### [[inv_org_parameters|INV_ORG_PARAMETERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemOrgParamInventoryFlag | INVENTORY_FLAG | — | — |
| 2 | ItemOrgParamOrganizationCode | ORGANIZATION_CODE | — | ✅ |
| 3 | ItemOrgParamOrganizationId | ORGANIZATION_ID | — | ✅ |
| 4 | ItemOrgParamSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |

### [[zx_exemptions|ZX_EXEMPTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxExemptionContentOwnerId | CONTENT_OWNER_ID | — | — |
| 2 | TaxExemptionCreatedBy | CREATED_BY | — | — |
| 3 | TaxExemptionCreationDate | CREATION_DATE | — | ✅ |
| 4 | TaxExemptionCustAccountId | CUST_ACCOUNT_ID | — | — |
| 5 | TaxExemptionDetFactorTemplCode | DET_FACTOR_TEMPL_CODE | — | — |
| 6 | TaxExemptionDuplicateExemption | DUPLICATE_EXEMPTION | — | — |
| 7 | TaxExemptionEffectiveFrom | EFFECTIVE_FROM | — | ✅ |
| 8 | TaxExemptionEffectiveTo | EFFECTIVE_TO | — | ✅ |
| 9 | TaxExemptionExemptCertificateNumber | EXEMPT_CERTIFICATE_NUMBER | — | ✅ |
| 10 | TaxExemptionExemptReasonCode | EXEMPT_REASON_CODE | — | ✅ |
| 11 | TaxExemptionExemptionStatusCode | EXEMPTION_STATUS_CODE | — | — |
| 12 | TaxExemptionExemptionTypeCode | EXEMPTION_TYPE_CODE | — | ✅ |
| 13 | TaxExemptionExemptionUsageCode | EXEMPTION_USAGE_CODE | — | — |
| 14 | TaxExemptionId | TAX_EXEMPTION_ID | — | — |
| 15 | TaxExemptionInventoryOrgId | INVENTORY_ORG_ID | — | — |
| 16 | TaxExemptionIssueFlag | ISSUE_FLAG | — | — |
| 17 | TaxExemptionIssuingTaxAuthorityId | ISSUING_TAX_AUTHORITY_ID | — | — |
| 18 | TaxExemptionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | TaxExemptionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | TaxExemptionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 21 | TaxExemptionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | TaxExemptionPartyTaxProfileId | PARTY_TAX_PROFILE_ID | — | — |
| 23 | TaxExemptionPrintFlag | PRINT_FLAG | — | — |
| 24 | TaxExemptionProductId | PRODUCT_ID | — | — |
| 25 | TaxExemptionProgramAppName | PROGRAM_APP_NAME | — | — |
| 26 | TaxExemptionProgramLoginId | PROGRAM_LOGIN_ID | — | — |
| 27 | TaxExemptionProgramName | PROGRAM_NAME | — | — |
| 28 | TaxExemptionProtocolNumberSeq | PROTOCOL_NUMBER_SEQ | — | — |
| 29 | TaxExemptionRateModifier | RATE_MODIFIER | — | ✅ |
| 30 | TaxExemptionRecordTypeCode | RECORD_TYPE_CODE | — | — |
| 31 | TaxExemptionRequestId | REQUEST_ID | — | — |
| 32 | TaxExemptionSiteUseId | SITE_USE_ID | — | — |
| 33 | TaxExemptionTax | TAX | — | ✅ |
| 34 | TaxExemptionTaxJurisdictionId | TAX_JURISDICTION_ID | — | — |
| 35 | TaxExemptionTaxRateCode | TAX_RATE_CODE | — | ✅ |
| 36 | TaxExemptionTaxRegimeCode | TAX_REGIME_CODE | — | ✅ |
| 37 | TaxExemptionTaxStatusCode | TAX_STATUS_CODE | — | ✅ |

### [[zx_jurisdictions_vl|ZX_JURISDICTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxJurisdictionEffectiveFrom | EFFECTIVE_FROM | — | — |
| 2 | TaxJurisdictionEffectiveTo | EFFECTIVE_TO | — | — |
| 3 | TaxJurisdictionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | TaxJurisdictionTax | TAX | — | — |
| 5 | TaxJurisdictionTaxAcctSrcJurisdictId | TAX_ACCT_SRC_JURISDICT_ID | — | — |
| 6 | TaxJurisdictionTaxExmptSrcJurisdictId | TAX_EXMPT_SRC_JURISDICT_ID | — | — |
| 7 | TaxJurisdictionTaxJurisdictionCode | TAX_JURISDICTION_CODE | — | ✅ |
| 8 | TaxJurisdictionTaxJurisdictionId | TAX_JURISDICTION_ID | — | — |
| 9 | TaxJurisdictionTaxJurisdictionName | TAX_JURISDICTION_NAME | — | ✅ |
| 10 | TaxJurisdictionTaxRegimeCode | TAX_REGIME_CODE | — | — |

### [[zx_party_tax_profile|ZX_PARTY_TAX_PROFILE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContPartyTaxProfileObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | ContPartyTaxProfilePartyTaxProfileId | PARTY_TAX_PROFILE_ID | — | — |
| 3 | ContPartyTaxProfilePartyTypeCode | PARTY_TYPE_CODE | — | — |
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
| 1 | TaxRegimeCollTaxAuthorityId | COLL_TAX_AUTHORITY_ID | — | — |
| 2 | TaxRegimeCountryCode | COUNTRY_CODE | — | — |
| 3 | TaxRegimeCountryOrGroupCode | COUNTRY_OR_GROUP_CODE | — | — |
| 4 | TaxRegimeCreatedBy | CREATED_BY | — | — |
| 5 | TaxRegimeCreationDate | CREATION_DATE | — | — |
| 6 | TaxRegimeCrossRegimeCompoundingFlag | CROSS_REGIME_COMPOUNDING_FLAG | — | — |
| 7 | TaxRegimeDefInclusiveTaxFlag | DEF_INCLUSIVE_TAX_FLAG | — | — |
| 8 | TaxRegimeDefPlaceOfSupplyTypeCode | DEF_PLACE_OF_SUPPLY_TYPE_CODE | — | — |
| 9 | TaxRegimeDefRecSettlementOptionCode | DEF_REC_SETTLEMENT_OPTION_CODE | — | — |
| 10 | TaxRegimeDefRegistrPartyTypeCode | DEF_REGISTR_PARTY_TYPE_CODE | — | — |
| 11 | TaxRegimeEffectiveFrom | EFFECTIVE_FROM | — | — |
| 12 | TaxRegimeEffectiveTo | EFFECTIVE_TO | — | — |
| 13 | TaxRegimeExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 14 | TaxRegimeExemptionProcessFlag | EXEMPTION_PROCESS_FLAG | — | — |
| 15 | TaxRegimeGeographyId | GEOGRAPHY_ID | — | — |
| 16 | TaxRegimeGeographyType | GEOGRAPHY_TYPE | — | — |
| 17 | TaxRegimeHasExchRateDateRuleFlag | HAS_EXCH_RATE_DATE_RULE_FLAG | — | — |
| 18 | TaxRegimeHasOtherJurisdictionsFlag | HAS_OTHER_JURISDICTIONS_FLAG | — | — |
| 19 | TaxRegimeHasSubRegimeFlag | HAS_SUB_REGIME_FLAG | — | — |
| 20 | TaxRegimeHasTaxDetDateRuleFlag | HAS_TAX_DET_DATE_RULE_FLAG | — | — |
| 21 | TaxRegimeHasTaxPointDateRuleFlag | HAS_TAX_POINT_DATE_RULE_FLAG | — | — |
| 22 | TaxRegimeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | TaxRegimeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 24 | TaxRegimeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 25 | TaxRegimeMinimumAccountableUnit | MINIMUM_ACCOUNTABLE_UNIT | — | — |
| 26 | TaxRegimeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 27 | TaxRegimeParentRegimeCode | PARENT_REGIME_CODE | — | — |
| 28 | TaxRegimePeriodSetName | PERIOD_SET_NAME | — | — |
| 29 | TaxRegimePlaceOfSupplyRuleFlag | PLACE_OF_SUPPLY_RULE_FLAG | — | — |
| 30 | TaxRegimeProgramAppName | PROGRAM_APP_NAME | — | — |
| 31 | TaxRegimeProgramLoginId | PROGRAM_LOGIN_ID | — | — |
| 32 | TaxRegimeProgramName | PROGRAM_NAME | — | — |
| 33 | TaxRegimeRecordTypeCode | RECORD_TYPE_CODE | — | — |
| 34 | TaxRegimeRegimePrecedence | REGIME_PRECEDENCE | — | — |
| 35 | TaxRegimeRegimeTypeFlag | REGIME_TYPE_FLAG | — | — |
| 36 | TaxRegimeRegistrationTypeRuleFlag | REGISTRATION_TYPE_RULE_FLAG | — | — |
| 37 | TaxRegimeRegnNumSameAsLeFlag | REGN_NUM_SAME_AS_LE_FLAG | — | — |
| 38 | TaxRegimeRepTaxAuthorityId | REP_TAX_AUTHORITY_ID | — | — |
| 39 | TaxRegimeRequestId | REQUEST_ID | — | — |
| 40 | TaxRegimeRoundingRuleCode | ROUNDING_RULE_CODE | — | — |
| 41 | TaxRegimeTaxAccountPrecedenceCode | TAX_ACCOUNT_PRECEDENCE_CODE | — | — |
| 42 | TaxRegimeTaxAmtThrshldFlag | TAX_AMT_THRSHLD_FLAG | — | — |
| 43 | TaxRegimeTaxCalcRuleFlag | TAX_CALC_RULE_FLAG | — | — |
| 44 | TaxRegimeTaxCurrencyCode | TAX_CURRENCY_CODE | — | — |
| 45 | TaxRegimeTaxInclusiveOverrideFlag | TAX_INCLUSIVE_OVERRIDE_FLAG | — | — |
| 46 | TaxRegimeTaxPrecision | TAX_PRECISION | — | — |
| 47 | TaxRegimeTaxRateRuleFlag | TAX_RATE_RULE_FLAG | — | — |
| 48 | TaxRegimeTaxRateThrshldFlag | TAX_RATE_THRSHLD_FLAG | — | — |
| 49 | TaxRegimeTaxRegimeCode | TAX_REGIME_CODE | — | — |
| 50 | TaxRegimeTaxRegimeId | TAX_REGIME_ID | — | — |
| 51 | TaxRegimeTaxRegimeName | TAX_REGIME_NAME | — | ✅ |
| 52 | TaxRegimeTaxStatusRuleFlag | TAX_STATUS_RULE_FLAG | — | — |
| 53 | TaxRegimeTaxableBasisRuleFlag | TAXABLE_BASIS_RULE_FLAG | — | — |
| 54 | TaxRegimeTaxableBasisThrshldFlag | TAXABLE_BASIS_THRSHLD_FLAG | — | — |
| 55 | TaxRegimeThrshldChkTmpltCode | THRSHLD_CHK_TMPLT_CODE | — | — |
| 56 | TaxRegimeThrshldGroupingLvlCode | THRSHLD_GROUPING_LVL_CODE | — | — |
| 57 | TaxRegimeUniquenessValidationLevel | UNIQUENESS_VALIDATION_LEVEL | — | — |
| 58 | TaxRegimeUseLegalMsgFlag | USE_LEGAL_MSG_FLAG | — | — |
| 59 | TaxRegimeUseTaxReportConfigFlag | USE_TAX_REPORT_CONFIG_FLAG | — | — |
| 60 | TaxRegimeValidationLevel | VALIDATION_LEVEL | — | — |
| 61 | TaxRegimeValidationType | VALIDATION_TYPE | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
