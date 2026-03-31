---
id: DOC-HCM-896
doc_type: system-doc
title: "ZX_PARTY_TAX_PROFILE — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - ZX_PARTY_TAX_PROFILE
  - zx_party_tax_profile
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# ZX_PARTY_TAX_PROFILE

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ALLOW_AWT_FLAG | — | — | — | — | — | — |
| 2 | ALLOW_OFFSET_TAX_FLAG | — | — | — | — | — | — |
| 3 | ALLOW_ZERO_AMT_WHT_INV_FLAG | — | — | — | — | — | — |
| 4 | COLLECTING_AUTHORITY_FLAG | — | — | — | — | — | — |
| 5 | COUNTRY_CODE | — | — | — | — | — | — |
| 6 | CREATED_BY | — | — | — | — | — | — |
| 7 | CREATE_AWT_DISTS_TYPE_CODE | — | — | — | — | — | — |
| 8 | CREATE_AWT_INVOICES_TYPE_CODE | — | — | — | — | — | — |
| 9 | CREATION_DATE | — | — | — | — | — | — |
| 10 | CUSTOMER_FLAG | — | — | — | — | — | — |
| 11 | EFFECTIVE_FROM_USE_LE | — | — | — | — | — | — |
| 12 | FIRST_PARTY_LE_FLAG | — | — | — | — | — | — |
| 13 | INCLUSIVE_TAX_FLAG | — | — | — | — | — | — |
| 14 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 15 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 16 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 17 | LEGAL_ESTABLISHMENT_FLAG | — | — | — | — | — | — |
| 18 | MERGED_STATUS_CODE | — | — | — | — | — | — |
| 19 | MERGED_TO_PTP_ID | — | — | — | — | — | — |
| 20 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 21 | PARTY_ID | — | — | — | — | — | — |
| 22 | PARTY_TAX_PROFILE_ID | — | — | — | — | — | — |
| 23 | PARTY_TYPE_CODE | — | — | — | — | — | — |
| 24 | PROCESS_FOR_APPLICABILITY_FLAG | — | — | — | — | — | — |
| 25 | PROGRAM_APP_NAME | — | — | — | — | — | — |
| 26 | PROGRAM_LOGIN_ID | — | — | — | — | — | — |
| 27 | PROGRAM_NAME | — | — | — | — | — | — |
| 28 | PROVIDER_TYPE_CODE | — | — | — | — | — | — |
| 29 | RECORD_TYPE_CODE | — | — | — | — | — | — |
| 30 | REGISTRATION_TYPE_CODE | — | — | — | — | — | — |
| 31 | REPORTING_AUTHORITY_FLAG | — | — | — | — | — | — |
| 32 | REP_REGISTRATION_NUMBER | — | — | — | — | — | — |
| 33 | REQUEST_ID | — | — | — | — | — | — |
| 34 | ROUNDING_LEVEL_CODE | — | — | — | — | — | — |
| 35 | ROUNDING_RULE_CODE | — | — | — | — | — | — |
| 36 | SELF_ASSESS_FLAG | — | — | — | — | — | — |
| 37 | SITE_FLAG | — | — | — | — | — | — |
| 38 | SUPPLIER_FLAG | — | — | — | — | — | — |
| 39 | TAX_CLASSIFICATION_CODE | — | — | — | — | — | — |
| 40 | USE_LE_AS_SUBSCRIBER_FLAG | — | — | — | — | — | — |
| 41 | WHT_DATE_BASIS | — | — | — | — | — | — |
| 42 | WHT_EFFECTIVE_FROM_USE_LE | — | — | — | — | — | — |
| 43 | WHT_ROUNDING_LEVEL_CODE | — | — | — | — | — | — |
| 44 | WHT_ROUNDING_RULE_CODE | — | — | — | — | — | — |
| 45 | WHT_USE_LE_AS_SUBSCRIBER_FLAG | — | — | — | — | — | — |
| 46 | WITHHOLDING_START_DATE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[sitetaxclassification|SiteTaxClassification]] (AR · BICC: 2/43)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COLLECTING_AUTHORITY_FLAG | PartyTaxProfileCollectingAuthorityFlag | — |
| COUNTRY_CODE | PartyTaxProfileCountryCode | — |
| CREATE_AWT_DISTS_TYPE_CODE | PartyTaxProfileCreateAwtDistsTypeCode | — |
| CREATE_AWT_INVOICES_TYPE_CODE | PartyTaxProfileCreateAwtInvoicesTypeCode | — |
| CREATED_BY | PartyTaxProfileCreatedBy | — |
| CREATION_DATE | PartyTaxProfileCreationDate | — |
| CUSTOMER_FLAG | PartyTaxProfileCustomerFlag | — |
| EFFECTIVE_FROM_USE_LE | PartyTaxProfileEffectiveFromUseLe | — |
| FIRST_PARTY_LE_FLAG | PartyTaxProfileFirstPartyLeFlag | — |
| INCLUSIVE_TAX_FLAG | PartyTaxProfileInclusiveTaxFlag | — |
| LAST_UPDATE_DATE | PartyTaxProfileLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PartyTaxProfileLastUpdateLogin | — |
| LAST_UPDATED_BY | PartyTaxProfileLastUpdatedBy | — |
| LEGAL_ESTABLISHMENT_FLAG | PartyTaxProfileLegalEstablishmentFlag | — |
| MERGED_STATUS_CODE | PartyTaxProfileMergedStatusCode | — |
| MERGED_TO_PTP_ID | PartyTaxProfileMergedToPtpId | — |
| OBJECT_VERSION_NUMBER | PartyTaxProfileObjectVersionNumber | — |
| PARTY_ID | PartyTaxProfilePartyId | — |
| PARTY_TAX_PROFILE_ID | PartyTaxProfileId | ✅ |
| PARTY_TYPE_CODE | PartyTaxProfilePartyTypeCode | — |
| PROCESS_FOR_APPLICABILITY_FLAG | PartyTaxProfileProcessForApplicabilityFlag | — |
| PROGRAM_APP_NAME | PartyTaxProfileProgramAppName | — |
| PROGRAM_LOGIN_ID | PartyTaxProfileProgramLoginId | — |
| PROGRAM_NAME | PartyTaxProfileProgramName | — |
| PROVIDER_TYPE_CODE | PartyTaxProfileProviderTypeCode | — |
| RECORD_TYPE_CODE | PartyTaxProfileRecordTypeCode | — |
| REGISTRATION_TYPE_CODE | PartyTaxProfileRegistrationTypeCode | — |
| REP_REGISTRATION_NUMBER | PartyTaxProfileRepRegistrationNumber | — |
| REPORTING_AUTHORITY_FLAG | PartyTaxProfileReportingAuthorityFlag | — |
| REQUEST_ID | PartyTaxProfileRequestId | — |
| ROUNDING_LEVEL_CODE | PartyTaxProfileRoundingLevelCode | — |
| ROUNDING_RULE_CODE | PartyTaxProfileRoundingRuleCode | — |
| SELF_ASSESS_FLAG | PartyTaxProfileSelfAssessFlag | — |
| SITE_FLAG | PartyTaxProfileSiteFlag | — |
| SUPPLIER_FLAG | PartyTaxProfileSupplierFlag | — |
| TAX_CLASSIFICATION_CODE | PartyTaxProfileTaxClassificationCode | — |
| USE_LE_AS_SUBSCRIBER_FLAG | PartyTaxProfileUseLeAsSubscriberFlag | — |
| WHT_DATE_BASIS | PartyTaxProfileWhtDateBasis | — |
| WHT_EFFECTIVE_FROM_USE_LE | PartyTaxProfileWhtEffectiveFromUseLe | — |
| WHT_ROUNDING_LEVEL_CODE | PartyTaxProfileWhtRoundingLevelCode | — |
| WHT_ROUNDING_RULE_CODE | PartyTaxProfileWhtRoundingRuleCode | — |
| WHT_USE_LE_AS_SUBSCRIBER_FLAG | PartyTaxProfileWhtUseLeAsSubscriberFlag | — |
| WITHHOLDING_START_DATE | PartyTaxProfileWithholdingStartDate | — |

### [[sitetaxexemption|SiteTaxExemption]] (AR · BICC: 2/49)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_AWT_FLAG | PartyTaxProfileAllowAwtFlag | — |
| ALLOW_OFFSET_TAX_FLAG | PartyTaxProfileAllowOffsetTaxFlag | — |
| ALLOW_ZERO_AMT_WHT_INV_FLAG | PartyTaxProfileAllowZeroAmtWhtInvFlag | — |
| COLLECTING_AUTHORITY_FLAG | PartyTaxProfileCollectingAuthorityFlag | — |
| COUNTRY_CODE | PartyTaxProfileCountryCode | — |
| CREATE_AWT_DISTS_TYPE_CODE | PartyTaxProfileCreateAwtDistsTypeCode | — |
| CREATE_AWT_INVOICES_TYPE_CODE | PartyTaxProfileCreateAwtInvoicesTypeCode | — |
| CREATED_BY | PartyTaxProfileCreatedBy | — |
| CREATION_DATE | PartyTaxProfileCreationDate | — |
| CUSTOMER_FLAG | PartyTaxProfileCustomerFlag | — |
| EFFECTIVE_FROM_USE_LE | PartyTaxProfileEffectiveFromUseLe | — |
| FIRST_PARTY_LE_FLAG | PartyTaxProfileFirstPartyLeFlag | — |
| INCLUSIVE_TAX_FLAG | PartyTaxProfileInclusiveTaxFlag | — |
| LAST_UPDATE_DATE | PartyTaxProfileLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PartyTaxProfileLastUpdateLogin | — |
| LAST_UPDATED_BY | PartyTaxProfileLastUpdatedBy | — |
| LEGAL_ESTABLISHMENT_FLAG | PartyTaxProfileLegalEstablishmentFlag | — |
| MERGED_STATUS_CODE | PartyTaxProfileMergedStatusCode | — |
| MERGED_TO_PTP_ID | PartyTaxProfileMergedToPtpId | — |
| OBJECT_VERSION_NUMBER | ContPartyTaxProfileObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | PartyTaxProfileObjectVersionNumber | — |
| PARTY_ID | PartyTaxProfilePartyId | — |
| PARTY_TAX_PROFILE_ID | ContPartyTaxProfilePartyTaxProfileId | — |
| PARTY_TAX_PROFILE_ID | PartyTaxProfileId | ✅ |
| PARTY_TYPE_CODE | ContPartyTaxProfilePartyTypeCode | — |
| PARTY_TYPE_CODE | PartyTaxProfilePartyTypeCode | — |
| PROCESS_FOR_APPLICABILITY_FLAG | PartyTaxProfileProcessForApplicabilityFlag | — |
| PROGRAM_APP_NAME | PartyTaxProfileProgramAppName | — |
| PROGRAM_LOGIN_ID | PartyTaxProfileProgramLoginId | — |
| PROGRAM_NAME | PartyTaxProfileProgramName | — |
| PROVIDER_TYPE_CODE | PartyTaxProfileProviderTypeCode | — |
| RECORD_TYPE_CODE | PartyTaxProfileRecordTypeCode | — |
| REGISTRATION_TYPE_CODE | PartyTaxProfileRegistrationTypeCode | — |
| REP_REGISTRATION_NUMBER | PartyTaxProfileRepRegistrationNumber | — |
| REPORTING_AUTHORITY_FLAG | PartyTaxProfileReportingAuthorityFlag | — |
| REQUEST_ID | PartyTaxProfileRequestId | — |
| ROUNDING_LEVEL_CODE | PartyTaxProfileRoundingLevelCode | — |
| ROUNDING_RULE_CODE | PartyTaxProfileRoundingRuleCode | — |
| SELF_ASSESS_FLAG | PartyTaxProfileSelfAssessFlag | — |
| SITE_FLAG | PartyTaxProfileSiteFlag | — |
| SUPPLIER_FLAG | PartyTaxProfileSupplierFlag | — |
| TAX_CLASSIFICATION_CODE | PartyTaxProfileTaxClassificationCode | — |
| USE_LE_AS_SUBSCRIBER_FLAG | PartyTaxProfileUseLeAsSubscriberFlag | — |
| WHT_DATE_BASIS | PartyTaxProfileWhtDateBasis | — |
| WHT_EFFECTIVE_FROM_USE_LE | PartyTaxProfileWhtEffectiveFromUseLe | — |
| WHT_ROUNDING_LEVEL_CODE | PartyTaxProfileWhtRoundingLevelCode | — |
| WHT_ROUNDING_RULE_CODE | PartyTaxProfileWhtRoundingRuleCode | — |
| WHT_USE_LE_AS_SUBSCRIBER_FLAG | PartyTaxProfileWhtUseLeAsSubscriberFlag | — |
| WITHHOLDING_START_DATE | PartyTaxProfileWithholdingStartDate | — |

### [[sitetaxregistration|SiteTaxRegistration]] (AR · BICC: 2/49)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_AWT_FLAG | PartyTaxProfileAllowAwtFlag | — |
| ALLOW_OFFSET_TAX_FLAG | PartyTaxProfileAllowOffsetTaxFlag | — |
| ALLOW_ZERO_AMT_WHT_INV_FLAG | PartyTaxProfileAllowZeroAmtWhtInvFlag | — |
| COLLECTING_AUTHORITY_FLAG | PartyTaxProfileCollectingAuthorityFlag | — |
| COUNTRY_CODE | PartyTaxProfileCountryCode | — |
| CREATE_AWT_DISTS_TYPE_CODE | PartyTaxProfileCreateAwtDistsTypeCode | — |
| CREATE_AWT_INVOICES_TYPE_CODE | PartyTaxProfileCreateAwtInvoicesTypeCode | — |
| CREATED_BY | PartyTaxProfileCreatedBy | — |
| CREATION_DATE | PartyTaxProfileCreationDate | — |
| CUSTOMER_FLAG | PartyTaxProfileCustomerFlag | — |
| EFFECTIVE_FROM_USE_LE | PartyTaxProfileEffectiveFromUseLe | — |
| FIRST_PARTY_LE_FLAG | PartyTaxProfileFirstPartyLeFlag | — |
| INCLUSIVE_TAX_FLAG | PartyTaxProfileInclusiveTaxFlag | — |
| LAST_UPDATE_DATE | PartyTaxProfileLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PartyTaxProfileLastUpdateLogin | — |
| LAST_UPDATED_BY | PartyTaxProfileLastUpdatedBy | — |
| LEGAL_ESTABLISHMENT_FLAG | PartyTaxProfileLegalEstablishmentFlag | — |
| MERGED_STATUS_CODE | PartyTaxProfileMergedStatusCode | — |
| MERGED_TO_PTP_ID | PartyTaxProfileMergedToPtpId | — |
| OBJECT_VERSION_NUMBER | PartyTaxProfileObjectVersionNumber | — |
| PARTY_ID | PartyTaxAuthProfPartyId | — |
| PARTY_ID | PartyTaxProfilePartyId | — |
| PARTY_TAX_PROFILE_ID | PartyTaxAuthProfPartyTaxProfileId | — |
| PARTY_TAX_PROFILE_ID | PartyTaxProfileId | ✅ |
| PARTY_TYPE_CODE | PartyTaxAuthProfPartyTypeCode | — |
| PARTY_TYPE_CODE | PartyTaxProfilePartyTypeCode | — |
| PROCESS_FOR_APPLICABILITY_FLAG | PartyTaxProfileProcessForApplicabilityFlag | — |
| PROGRAM_APP_NAME | PartyTaxProfileProgramAppName | — |
| PROGRAM_LOGIN_ID | PartyTaxProfileProgramLoginId | — |
| PROGRAM_NAME | PartyTaxProfileProgramName | — |
| PROVIDER_TYPE_CODE | PartyTaxProfileProviderTypeCode | — |
| RECORD_TYPE_CODE | PartyTaxProfileRecordTypeCode | — |
| REGISTRATION_TYPE_CODE | PartyTaxProfileRegistrationTypeCode | — |
| REP_REGISTRATION_NUMBER | PartyTaxProfileRepRegistrationNumber | — |
| REPORTING_AUTHORITY_FLAG | PartyTaxProfileReportingAuthorityFlag | — |
| REQUEST_ID | PartyTaxProfileRequestId | — |
| ROUNDING_LEVEL_CODE | PartyTaxProfileRoundingLevelCode | — |
| ROUNDING_RULE_CODE | PartyTaxProfileRoundingRuleCode | — |
| SELF_ASSESS_FLAG | PartyTaxProfileSelfAssessFlag | — |
| SITE_FLAG | PartyTaxProfileSiteFlag | — |
| SUPPLIER_FLAG | PartyTaxProfileSupplierFlag | — |
| TAX_CLASSIFICATION_CODE | PartyTaxProfileTaxClassificationCode | — |
| USE_LE_AS_SUBSCRIBER_FLAG | PartyTaxProfileUseLeAsSubscriberFlag | — |
| WHT_DATE_BASIS | PartyTaxProfileWhtDateBasis | — |
| WHT_EFFECTIVE_FROM_USE_LE | PartyTaxProfileWhtEffectiveFromUseLe | — |
| WHT_ROUNDING_LEVEL_CODE | PartyTaxProfileWhtRoundingLevelCode | — |
| WHT_ROUNDING_RULE_CODE | PartyTaxProfileWhtRoundingRuleCode | — |
| WHT_USE_LE_AS_SUBSCRIBER_FLAG | PartyTaxProfileWhtUseLeAsSubscriberFlag | — |
| WITHHOLDING_START_DATE | PartyTaxProfileWithholdingStartDate | — |

### [[sitetaxreportingcode|SiteTaxReportingCode]] (AR · BICC: 2/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_AWT_FLAG | PartyTaxProfileAllowAwtFlag | — |
| ALLOW_OFFSET_TAX_FLAG | PartyTaxProfileAllowOffsetTaxFlag | — |
| ALLOW_ZERO_AMT_WHT_INV_FLAG | PartyTaxProfileAllowZeroAmtWhtInvFlag | — |
| COLLECTING_AUTHORITY_FLAG | PartyTaxProfileCollectingAuthorityFlag | — |
| COUNTRY_CODE | PartyTaxProfileCountryCode | — |
| CREATE_AWT_DISTS_TYPE_CODE | PartyTaxProfileCreateAwtDistsTypeCode | — |
| CREATE_AWT_INVOICES_TYPE_CODE | PartyTaxProfileCreateAwtInvoicesTypeCode | — |
| CREATED_BY | PartyTaxProfileCreatedBy | — |
| CREATION_DATE | PartyTaxProfileCreationDate | — |
| CUSTOMER_FLAG | PartyTaxProfileCustomerFlag | — |
| EFFECTIVE_FROM_USE_LE | PartyTaxProfileEffectiveFromUseLe | — |
| FIRST_PARTY_LE_FLAG | PartyTaxProfileFirstPartyLeFlag | — |
| INCLUSIVE_TAX_FLAG | PartyTaxProfileInclusiveTaxFlag | — |
| LAST_UPDATE_DATE | PartyTaxProfileLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PartyTaxProfileLastUpdateLogin | — |
| LAST_UPDATED_BY | PartyTaxProfileLastUpdatedBy | — |
| LEGAL_ESTABLISHMENT_FLAG | PartyTaxProfileLegalEstablishmentFlag | — |
| MERGED_STATUS_CODE | PartyTaxProfileMergedStatusCode | — |
| MERGED_TO_PTP_ID | PartyTaxProfileMergedToPtpId | — |
| OBJECT_VERSION_NUMBER | PartyTaxProfileObjectVersionNumber | — |
| PARTY_ID | PartyTaxProfilePartyId | — |
| PARTY_TAX_PROFILE_ID | PartyTaxProfileId | ✅ |
| PARTY_TYPE_CODE | PartyTaxProfilePartyTypeCode | — |
| PROCESS_FOR_APPLICABILITY_FLAG | PartyTaxProfileProcessForApplicabilityFlag | — |
| PROGRAM_APP_NAME | PartyTaxProfileProgramAppName | — |
| PROGRAM_LOGIN_ID | PartyTaxProfileProgramLoginId | — |
| PROGRAM_NAME | PartyTaxProfileProgramName | — |
| PROVIDER_TYPE_CODE | PartyTaxProfileProviderTypeCode | — |
| RECORD_TYPE_CODE | PartyTaxProfileRecordTypeCode | — |
| REGISTRATION_TYPE_CODE | PartyTaxProfileRegistrationTypeCode | — |
| REP_REGISTRATION_NUMBER | PartyTaxProfileRepRegistrationNumber | — |
| REPORTING_AUTHORITY_FLAG | PartyTaxProfileReportingAuthorityFlag | — |
| REQUEST_ID | PartyTaxProfileRequestId | — |
| ROUNDING_LEVEL_CODE | PartyTaxProfileRoundingLevelCode | — |
| ROUNDING_RULE_CODE | PartyTaxProfileRoundingRuleCode | — |
| SELF_ASSESS_FLAG | PartyTaxProfileSelfAssessFlag | — |
| SITE_FLAG | PartyTaxProfileSiteFlag | — |
| SUPPLIER_FLAG | PartyTaxProfileSupplierFlag | — |
| TAX_CLASSIFICATION_CODE | PartyTaxProfileTaxClassificationCode | — |
| USE_LE_AS_SUBSCRIBER_FLAG | PartyTaxProfileUseLeAsSubscriberFlag | — |
| WHT_DATE_BASIS | PartyTaxProfileWhtDateBasis | — |
| WHT_EFFECTIVE_FROM_USE_LE | PartyTaxProfileWhtEffectiveFromUseLe | — |
| WHT_ROUNDING_LEVEL_CODE | PartyTaxProfileWhtRoundingLevelCode | — |
| WHT_ROUNDING_RULE_CODE | PartyTaxProfileWhtRoundingRuleCode | — |
| WHT_USE_LE_AS_SUBSCRIBER_FLAG | PartyTaxProfileWhtUseLeAsSubscriberFlag | — |
| WITHHOLDING_START_DATE | PartyTaxProfileWithholdingStartDate | — |

### [[sitetaxvalidation|SiteTaxValidation]] (AR · BICC: 5/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_AWT_FLAG | PartyTaxProfileAllowAwtFlag | — |
| ALLOW_OFFSET_TAX_FLAG | PartyTaxProfileAllowOffsetTaxFlag | — |
| ALLOW_ZERO_AMT_WHT_INV_FLAG | PartyTaxProfileAllowZeroAmtWhtInvFlag | — |
| COLLECTING_AUTHORITY_FLAG | PartyTaxProfileCollectingAuthorityFlag | — |
| COUNTRY_CODE | PartyTaxProfileCountryCode | — |
| CREATE_AWT_DISTS_TYPE_CODE | PartyTaxProfileCreateAwtDistsTypeCode | — |
| CREATE_AWT_INVOICES_TYPE_CODE | PartyTaxProfileCreateAwtInvoicesTypeCode | — |
| CREATED_BY | PartyTaxProfileCreatedBy | — |
| CREATION_DATE | PartyTaxProfileCreationDate | — |
| CUSTOMER_FLAG | PartyTaxProfileCustomerFlag | — |
| EFFECTIVE_FROM_USE_LE | PartyTaxProfileEffectiveFromUseLe | — |
| FIRST_PARTY_LE_FLAG | PartyTaxProfileFirstPartyLeFlag | — |
| INCLUSIVE_TAX_FLAG | PartyTaxProfileInclusiveTaxFlag | ✅ |
| LAST_UPDATE_DATE | PartyTaxProfileLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PartyTaxProfileLastUpdateLogin | — |
| LAST_UPDATED_BY | PartyTaxProfileLastUpdatedBy | — |
| LEGAL_ESTABLISHMENT_FLAG | PartyTaxProfileLegalEstablishmentFlag | — |
| MERGED_STATUS_CODE | PartyTaxProfileMergedStatusCode | — |
| MERGED_TO_PTP_ID | PartyTaxProfileMergedToPtpId | — |
| OBJECT_VERSION_NUMBER | PartyTaxProfileObjectVersionNumber | — |
| PARTY_ID | PartyTaxProfilePartyId | — |
| PARTY_TAX_PROFILE_ID | PartyTaxProfileId | ✅ |
| PARTY_TYPE_CODE | PartyTaxProfilePartyTypeCode | — |
| PROCESS_FOR_APPLICABILITY_FLAG | PartyTaxProfileProcessForApplicabilityFlag | — |
| PROGRAM_APP_NAME | PartyTaxProfileProgramAppName | — |
| PROGRAM_LOGIN_ID | PartyTaxProfileProgramLoginId | — |
| PROGRAM_NAME | PartyTaxProfileProgramName | — |
| PROVIDER_TYPE_CODE | PartyTaxProfileProviderTypeCode | — |
| RECORD_TYPE_CODE | PartyTaxProfileRecordTypeCode | — |
| REGISTRATION_TYPE_CODE | PartyTaxProfileRegistrationTypeCode | — |
| REP_REGISTRATION_NUMBER | PartyTaxProfileRepRegistrationNumber | — |
| REPORTING_AUTHORITY_FLAG | PartyTaxProfileReportingAuthorityFlag | — |
| REQUEST_ID | PartyTaxProfileRequestId | — |
| ROUNDING_LEVEL_CODE | PartyTaxProfileRoundingLevelCode | ✅ |
| ROUNDING_RULE_CODE | PartyTaxProfileRoundingRuleCode | ✅ |
| SELF_ASSESS_FLAG | PartyTaxProfileSelfAssessFlag | — |
| SITE_FLAG | PartyTaxProfileSiteFlag | — |
| SUPPLIER_FLAG | PartyTaxProfileSupplierFlag | — |
| TAX_CLASSIFICATION_CODE | PartyTaxProfileTaxClassificationCode | — |
| USE_LE_AS_SUBSCRIBER_FLAG | PartyTaxProfileUseLeAsSubscriberFlag | — |
| WHT_DATE_BASIS | PartyTaxProfileWhtDateBasis | — |
| WHT_EFFECTIVE_FROM_USE_LE | PartyTaxProfileWhtEffectiveFromUseLe | — |
| WHT_ROUNDING_LEVEL_CODE | PartyTaxProfileWhtRoundingLevelCode | — |
| WHT_ROUNDING_RULE_CODE | PartyTaxProfileWhtRoundingRuleCode | — |
| WHT_USE_LE_AS_SUBSCRIBER_FLAG | PartyTaxProfileWhtUseLeAsSubscriberFlag | — |
| WITHHOLDING_START_DATE | PartyTaxProfileWithholdingStartDate | — |

### [[supplierpvo|SupplierPVO]] (PO · BICC: 3/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COUNTRY_CODE | PartyTaxProfileGenericCountryCode | ✅ |
| PARTY_ID | PartyTaxProfileGenericPartyId | — |
| PARTY_TAX_PROFILE_ID | PartyTaxProfileGenericPartyTaxProfileId | — |
| PARTY_TYPE_CODE | PartyTaxProfileGenericPartyTypeCode | — |
| REP_REGISTRATION_NUMBER | PartyTaxProfileGenericRepRegistrationNumber | ✅ |
| TAX_CLASSIFICATION_CODE | PartyTaxProfileGenericTaxClassificationCode | ✅ |

### [[taxclassification|TaxClassification]] (AR · BICC: 2/43)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COLLECTING_AUTHORITY_FLAG | PartyTaxProfileCollectingAuthorityFlag | — |
| COUNTRY_CODE | PartyTaxProfileCountryCode | — |
| CREATE_AWT_DISTS_TYPE_CODE | PartyTaxProfileCreateAwtDistsTypeCode | — |
| CREATE_AWT_INVOICES_TYPE_CODE | PartyTaxProfileCreateAwtInvoicesTypeCode | — |
| CREATED_BY | PartyTaxProfileCreatedBy | — |
| CREATION_DATE | PartyTaxProfileCreationDate | — |
| CUSTOMER_FLAG | PartyTaxProfileCustomerFlag | — |
| EFFECTIVE_FROM_USE_LE | PartyTaxProfileEffectiveFromUseLe | — |
| FIRST_PARTY_LE_FLAG | PartyTaxProfileFirstPartyLeFlag | — |
| INCLUSIVE_TAX_FLAG | PartyTaxProfileInclusiveTaxFlag | — |
| LAST_UPDATE_DATE | PartyTaxProfileLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PartyTaxProfileLastUpdateLogin | — |
| LAST_UPDATED_BY | PartyTaxProfileLastUpdatedBy | — |
| LEGAL_ESTABLISHMENT_FLAG | PartyTaxProfileLegalEstablishmentFlag | — |
| MERGED_STATUS_CODE | PartyTaxProfileMergedStatusCode | — |
| MERGED_TO_PTP_ID | PartyTaxProfileMergedToPtpId | — |
| OBJECT_VERSION_NUMBER | PartyTaxProfileObjectVersionNumber | — |
| PARTY_ID | PartyTaxProfilePartyId | — |
| PARTY_TAX_PROFILE_ID | PartyTaxProfileId | ✅ |
| PARTY_TYPE_CODE | PartyTaxProfilePartyTypeCode | — |
| PROCESS_FOR_APPLICABILITY_FLAG | PartyTaxProfileProcessForApplicabilityFlag | — |
| PROGRAM_APP_NAME | PartyTaxProfileProgramAppName | — |
| PROGRAM_LOGIN_ID | PartyTaxProfileProgramLoginId | — |
| PROGRAM_NAME | PartyTaxProfileProgramName | — |
| PROVIDER_TYPE_CODE | PartyTaxProfileProviderTypeCode | — |
| RECORD_TYPE_CODE | PartyTaxProfileRecordTypeCode | — |
| REGISTRATION_TYPE_CODE | PartyTaxProfileRegistrationTypeCode | — |
| REP_REGISTRATION_NUMBER | PartyTaxProfileRepRegistrationNumber | — |
| REPORTING_AUTHORITY_FLAG | PartyTaxProfileReportingAuthorityFlag | — |
| REQUEST_ID | PartyTaxProfileRequestId | — |
| ROUNDING_LEVEL_CODE | PartyTaxProfileRoundingLevelCode | — |
| ROUNDING_RULE_CODE | PartyTaxProfileRoundingRuleCode | — |
| SELF_ASSESS_FLAG | PartyTaxProfileSelfAssessFlag | — |
| SITE_FLAG | PartyTaxProfileSiteFlag | — |
| SUPPLIER_FLAG | PartyTaxProfileSupplierFlag | — |
| TAX_CLASSIFICATION_CODE | PartyTaxProfileTaxClassificationCode | — |
| USE_LE_AS_SUBSCRIBER_FLAG | PartyTaxProfileUseLeAsSubscriberFlag | — |
| WHT_DATE_BASIS | PartyTaxProfileWhtDateBasis | — |
| WHT_EFFECTIVE_FROM_USE_LE | PartyTaxProfileWhtEffectiveFromUseLe | — |
| WHT_ROUNDING_LEVEL_CODE | PartyTaxProfileWhtRoundingLevelCode | — |
| WHT_ROUNDING_RULE_CODE | PartyTaxProfileWhtRoundingRuleCode | — |
| WHT_USE_LE_AS_SUBSCRIBER_FLAG | PartyTaxProfileWhtUseLeAsSubscriberFlag | — |
| WITHHOLDING_START_DATE | PartyTaxProfileWithholdingStartDate | — |

### [[taxexemption|TaxExemption]] (AR · BICC: 2/49)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_AWT_FLAG | PartyTaxProfileAllowAwtFlag | — |
| ALLOW_OFFSET_TAX_FLAG | PartyTaxProfileAllowOffsetTaxFlag | — |
| ALLOW_ZERO_AMT_WHT_INV_FLAG | PartyTaxProfileAllowZeroAmtWhtInvFlag | — |
| COLLECTING_AUTHORITY_FLAG | PartyTaxProfileCollectingAuthorityFlag | — |
| COUNTRY_CODE | PartyTaxProfileCountryCode | — |
| CREATE_AWT_DISTS_TYPE_CODE | PartyTaxProfileCreateAwtDistsTypeCode | — |
| CREATE_AWT_INVOICES_TYPE_CODE | PartyTaxProfileCreateAwtInvoicesTypeCode | — |
| CREATED_BY | PartyTaxProfileCreatedBy | — |
| CREATION_DATE | PartyTaxProfileCreationDate | — |
| CUSTOMER_FLAG | PartyTaxProfileCustomerFlag | — |
| EFFECTIVE_FROM_USE_LE | PartyTaxProfileEffectiveFromUseLe | — |
| FIRST_PARTY_LE_FLAG | PartyTaxProfileFirstPartyLeFlag | — |
| INCLUSIVE_TAX_FLAG | PartyTaxProfileInclusiveTaxFlag | — |
| LAST_UPDATE_DATE | PartyTaxProfileLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PartyTaxProfileLastUpdateLogin | — |
| LAST_UPDATED_BY | PartyTaxProfileLastUpdatedBy | — |
| LEGAL_ESTABLISHMENT_FLAG | PartyTaxProfileLegalEstablishmentFlag | — |
| MERGED_STATUS_CODE | PartyTaxProfileMergedStatusCode | — |
| MERGED_TO_PTP_ID | PartyTaxProfileMergedToPtpId | — |
| OBJECT_VERSION_NUMBER | ContPartyTaxProfileObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | PartyTaxProfileObjectVersionNumber | — |
| PARTY_ID | PartyTaxProfilePartyId | — |
| PARTY_TAX_PROFILE_ID | ContPartyTaxProfilePartyTaxProfileId | — |
| PARTY_TAX_PROFILE_ID | PartyTaxProfileId | ✅ |
| PARTY_TYPE_CODE | ContPartyTaxProfilePartyTypeCode | — |
| PARTY_TYPE_CODE | PartyTaxProfilePartyTypeCode | — |
| PROCESS_FOR_APPLICABILITY_FLAG | PartyTaxProfileProcessForApplicabilityFlag | — |
| PROGRAM_APP_NAME | PartyTaxProfileProgramAppName | — |
| PROGRAM_LOGIN_ID | PartyTaxProfileProgramLoginId | — |
| PROGRAM_NAME | PartyTaxProfileProgramName | — |
| PROVIDER_TYPE_CODE | PartyTaxProfileProviderTypeCode | — |
| RECORD_TYPE_CODE | PartyTaxProfileRecordTypeCode | — |
| REGISTRATION_TYPE_CODE | PartyTaxProfileRegistrationTypeCode | — |
| REP_REGISTRATION_NUMBER | PartyTaxProfileRepRegistrationNumber | — |
| REPORTING_AUTHORITY_FLAG | PartyTaxProfileReportingAuthorityFlag | — |
| REQUEST_ID | PartyTaxProfileRequestId | — |
| ROUNDING_LEVEL_CODE | PartyTaxProfileRoundingLevelCode | — |
| ROUNDING_RULE_CODE | PartyTaxProfileRoundingRuleCode | — |
| SELF_ASSESS_FLAG | PartyTaxProfileSelfAssessFlag | — |
| SITE_FLAG | PartyTaxProfileSiteFlag | — |
| SUPPLIER_FLAG | PartyTaxProfileSupplierFlag | — |
| TAX_CLASSIFICATION_CODE | PartyTaxProfileTaxClassificationCode | — |
| USE_LE_AS_SUBSCRIBER_FLAG | PartyTaxProfileUseLeAsSubscriberFlag | — |
| WHT_DATE_BASIS | PartyTaxProfileWhtDateBasis | — |
| WHT_EFFECTIVE_FROM_USE_LE | PartyTaxProfileWhtEffectiveFromUseLe | — |
| WHT_ROUNDING_LEVEL_CODE | PartyTaxProfileWhtRoundingLevelCode | — |
| WHT_ROUNDING_RULE_CODE | PartyTaxProfileWhtRoundingRuleCode | — |
| WHT_USE_LE_AS_SUBSCRIBER_FLAG | PartyTaxProfileWhtUseLeAsSubscriberFlag | — |
| WITHHOLDING_START_DATE | PartyTaxProfileWithholdingStartDate | — |

### [[taxregistration|TaxRegistration]] (AR · BICC: 4/49)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_AWT_FLAG | PartyTaxProfileAllowAwtFlag | — |
| ALLOW_OFFSET_TAX_FLAG | PartyTaxProfileAllowOffsetTaxFlag | — |
| ALLOW_ZERO_AMT_WHT_INV_FLAG | PartyTaxProfileAllowZeroAmtWhtInvFlag | — |
| COLLECTING_AUTHORITY_FLAG | PartyTaxProfileCollectingAuthorityFlag | — |
| COUNTRY_CODE | PartyTaxProfileCountryCode | ✅ |
| CREATE_AWT_DISTS_TYPE_CODE | PartyTaxProfileCreateAwtDistsTypeCode | — |
| CREATE_AWT_INVOICES_TYPE_CODE | PartyTaxProfileCreateAwtInvoicesTypeCode | — |
| CREATED_BY | PartyTaxProfileCreatedBy | — |
| CREATION_DATE | PartyTaxProfileCreationDate | — |
| CUSTOMER_FLAG | PartyTaxProfileCustomerFlag | — |
| EFFECTIVE_FROM_USE_LE | PartyTaxProfileEffectiveFromUseLe | — |
| FIRST_PARTY_LE_FLAG | PartyTaxProfileFirstPartyLeFlag | — |
| INCLUSIVE_TAX_FLAG | PartyTaxProfileInclusiveTaxFlag | — |
| LAST_UPDATE_DATE | PartyTaxProfileLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PartyTaxProfileLastUpdateLogin | — |
| LAST_UPDATED_BY | PartyTaxProfileLastUpdatedBy | — |
| LEGAL_ESTABLISHMENT_FLAG | PartyTaxProfileLegalEstablishmentFlag | — |
| MERGED_STATUS_CODE | PartyTaxProfileMergedStatusCode | — |
| MERGED_TO_PTP_ID | PartyTaxProfileMergedToPtpId | — |
| OBJECT_VERSION_NUMBER | PartyTaxProfileObjectVersionNumber | — |
| PARTY_ID | PartyTaxAuthProfPartyId | — |
| PARTY_ID | PartyTaxProfilePartyId | — |
| PARTY_TAX_PROFILE_ID | PartyTaxAuthProfPartyTaxProfileId | — |
| PARTY_TAX_PROFILE_ID | PartyTaxProfileId | ✅ |
| PARTY_TYPE_CODE | PartyTaxAuthProfPartyTypeCode | — |
| PARTY_TYPE_CODE | PartyTaxProfilePartyTypeCode | — |
| PROCESS_FOR_APPLICABILITY_FLAG | PartyTaxProfileProcessForApplicabilityFlag | — |
| PROGRAM_APP_NAME | PartyTaxProfileProgramAppName | — |
| PROGRAM_LOGIN_ID | PartyTaxProfileProgramLoginId | — |
| PROGRAM_NAME | PartyTaxProfileProgramName | — |
| PROVIDER_TYPE_CODE | PartyTaxProfileProviderTypeCode | — |
| RECORD_TYPE_CODE | PartyTaxProfileRecordTypeCode | — |
| REGISTRATION_TYPE_CODE | PartyTaxProfileRegistrationTypeCode | — |
| REP_REGISTRATION_NUMBER | PartyTaxProfileRepRegistrationNumber | ✅ |
| REPORTING_AUTHORITY_FLAG | PartyTaxProfileReportingAuthorityFlag | — |
| REQUEST_ID | PartyTaxProfileRequestId | — |
| ROUNDING_LEVEL_CODE | PartyTaxProfileRoundingLevelCode | — |
| ROUNDING_RULE_CODE | PartyTaxProfileRoundingRuleCode | — |
| SELF_ASSESS_FLAG | PartyTaxProfileSelfAssessFlag | — |
| SITE_FLAG | PartyTaxProfileSiteFlag | — |
| SUPPLIER_FLAG | PartyTaxProfileSupplierFlag | — |
| TAX_CLASSIFICATION_CODE | PartyTaxProfileTaxClassificationCode | — |
| USE_LE_AS_SUBSCRIBER_FLAG | PartyTaxProfileUseLeAsSubscriberFlag | — |
| WHT_DATE_BASIS | PartyTaxProfileWhtDateBasis | — |
| WHT_EFFECTIVE_FROM_USE_LE | PartyTaxProfileWhtEffectiveFromUseLe | — |
| WHT_ROUNDING_LEVEL_CODE | PartyTaxProfileWhtRoundingLevelCode | — |
| WHT_ROUNDING_RULE_CODE | PartyTaxProfileWhtRoundingRuleCode | — |
| WHT_USE_LE_AS_SUBSCRIBER_FLAG | PartyTaxProfileWhtUseLeAsSubscriberFlag | — |
| WITHHOLDING_START_DATE | PartyTaxProfileWithholdingStartDate | — |

### [[taxreportingcode|TaxReportingCode]] (AR · BICC: 2/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_AWT_FLAG | PartyTaxProfileAllowAwtFlag | — |
| ALLOW_OFFSET_TAX_FLAG | PartyTaxProfileAllowOffsetTaxFlag | — |
| ALLOW_ZERO_AMT_WHT_INV_FLAG | PartyTaxProfileAllowZeroAmtWhtInvFlag | — |
| COLLECTING_AUTHORITY_FLAG | PartyTaxProfileCollectingAuthorityFlag | — |
| COUNTRY_CODE | PartyTaxProfileCountryCode | — |
| CREATE_AWT_DISTS_TYPE_CODE | PartyTaxProfileCreateAwtDistsTypeCode | — |
| CREATE_AWT_INVOICES_TYPE_CODE | PartyTaxProfileCreateAwtInvoicesTypeCode | — |
| CREATED_BY | PartyTaxProfileCreatedBy | — |
| CREATION_DATE | PartyTaxProfileCreationDate | — |
| CUSTOMER_FLAG | PartyTaxProfileCustomerFlag | — |
| EFFECTIVE_FROM_USE_LE | PartyTaxProfileEffectiveFromUseLe | — |
| FIRST_PARTY_LE_FLAG | PartyTaxProfileFirstPartyLeFlag | — |
| INCLUSIVE_TAX_FLAG | PartyTaxProfileInclusiveTaxFlag | — |
| LAST_UPDATE_DATE | PartyTaxProfileLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PartyTaxProfileLastUpdateLogin | — |
| LAST_UPDATED_BY | PartyTaxProfileLastUpdatedBy | — |
| LEGAL_ESTABLISHMENT_FLAG | PartyTaxProfileLegalEstablishmentFlag | — |
| MERGED_STATUS_CODE | PartyTaxProfileMergedStatusCode | — |
| MERGED_TO_PTP_ID | PartyTaxProfileMergedToPtpId | — |
| OBJECT_VERSION_NUMBER | PartyTaxProfileObjectVersionNumber | — |
| PARTY_ID | PartyTaxProfilePartyId | — |
| PARTY_TAX_PROFILE_ID | PartyTaxProfileId | ✅ |
| PARTY_TYPE_CODE | PartyTaxProfilePartyTypeCode | — |
| PROCESS_FOR_APPLICABILITY_FLAG | PartyTaxProfileProcessForApplicabilityFlag | — |
| PROGRAM_APP_NAME | PartyTaxProfileProgramAppName | — |
| PROGRAM_LOGIN_ID | PartyTaxProfileProgramLoginId | — |
| PROGRAM_NAME | PartyTaxProfileProgramName | — |
| PROVIDER_TYPE_CODE | PartyTaxProfileProviderTypeCode | — |
| RECORD_TYPE_CODE | PartyTaxProfileRecordTypeCode | — |
| REGISTRATION_TYPE_CODE | PartyTaxProfileRegistrationTypeCode | — |
| REP_REGISTRATION_NUMBER | PartyTaxProfileRepRegistrationNumber | — |
| REPORTING_AUTHORITY_FLAG | PartyTaxProfileReportingAuthorityFlag | — |
| REQUEST_ID | PartyTaxProfileRequestId | — |
| ROUNDING_LEVEL_CODE | PartyTaxProfileRoundingLevelCode | — |
| ROUNDING_RULE_CODE | PartyTaxProfileRoundingRuleCode | — |
| SELF_ASSESS_FLAG | PartyTaxProfileSelfAssessFlag | — |
| SITE_FLAG | PartyTaxProfileSiteFlag | — |
| SUPPLIER_FLAG | PartyTaxProfileSupplierFlag | — |
| TAX_CLASSIFICATION_CODE | PartyTaxProfileTaxClassificationCode | — |
| USE_LE_AS_SUBSCRIBER_FLAG | PartyTaxProfileUseLeAsSubscriberFlag | — |
| WHT_DATE_BASIS | PartyTaxProfileWhtDateBasis | — |
| WHT_EFFECTIVE_FROM_USE_LE | PartyTaxProfileWhtEffectiveFromUseLe | — |
| WHT_ROUNDING_LEVEL_CODE | PartyTaxProfileWhtRoundingLevelCode | — |
| WHT_ROUNDING_RULE_CODE | PartyTaxProfileWhtRoundingRuleCode | — |
| WHT_USE_LE_AS_SUBSCRIBER_FLAG | PartyTaxProfileWhtUseLeAsSubscriberFlag | — |
| WITHHOLDING_START_DATE | PartyTaxProfileWithholdingStartDate | — |

### [[taxvalidation|TaxValidation]] (AR · BICC: 5/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_AWT_FLAG | PartyTaxProfileAllowAwtFlag | — |
| ALLOW_OFFSET_TAX_FLAG | PartyTaxProfileAllowOffsetTaxFlag | — |
| ALLOW_ZERO_AMT_WHT_INV_FLAG | PartyTaxProfileAllowZeroAmtWhtInvFlag | — |
| COLLECTING_AUTHORITY_FLAG | PartyTaxProfileCollectingAuthorityFlag | — |
| COUNTRY_CODE | PartyTaxProfileCountryCode | — |
| CREATE_AWT_DISTS_TYPE_CODE | PartyTaxProfileCreateAwtDistsTypeCode | — |
| CREATE_AWT_INVOICES_TYPE_CODE | PartyTaxProfileCreateAwtInvoicesTypeCode | — |
| CREATED_BY | PartyTaxProfileCreatedBy | — |
| CREATION_DATE | PartyTaxProfileCreationDate | — |
| CUSTOMER_FLAG | PartyTaxProfileCustomerFlag | — |
| EFFECTIVE_FROM_USE_LE | PartyTaxProfileEffectiveFromUseLe | — |
| FIRST_PARTY_LE_FLAG | PartyTaxProfileFirstPartyLeFlag | — |
| INCLUSIVE_TAX_FLAG | PartyTaxProfileInclusiveTaxFlag | ✅ |
| LAST_UPDATE_DATE | PartyTaxProfileLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PartyTaxProfileLastUpdateLogin | — |
| LAST_UPDATED_BY | PartyTaxProfileLastUpdatedBy | — |
| LEGAL_ESTABLISHMENT_FLAG | PartyTaxProfileLegalEstablishmentFlag | — |
| MERGED_STATUS_CODE | PartyTaxProfileMergedStatusCode | — |
| MERGED_TO_PTP_ID | PartyTaxProfileMergedToPtpId | — |
| OBJECT_VERSION_NUMBER | PartyTaxProfileObjectVersionNumber | — |
| PARTY_ID | PartyTaxProfilePartyId | — |
| PARTY_TAX_PROFILE_ID | PartyTaxProfileId | ✅ |
| PARTY_TYPE_CODE | PartyTaxProfilePartyTypeCode | — |
| PROCESS_FOR_APPLICABILITY_FLAG | PartyTaxProfileProcessForApplicabilityFlag | — |
| PROGRAM_APP_NAME | PartyTaxProfileProgramAppName | — |
| PROGRAM_LOGIN_ID | PartyTaxProfileProgramLoginId | — |
| PROGRAM_NAME | PartyTaxProfileProgramName | — |
| PROVIDER_TYPE_CODE | PartyTaxProfileProviderTypeCode | — |
| RECORD_TYPE_CODE | PartyTaxProfileRecordTypeCode | — |
| REGISTRATION_TYPE_CODE | PartyTaxProfileRegistrationTypeCode | — |
| REP_REGISTRATION_NUMBER | PartyTaxProfileRepRegistrationNumber | — |
| REPORTING_AUTHORITY_FLAG | PartyTaxProfileReportingAuthorityFlag | — |
| REQUEST_ID | PartyTaxProfileRequestId | — |
| ROUNDING_LEVEL_CODE | PartyTaxProfileRoundingLevelCode | ✅ |
| ROUNDING_RULE_CODE | PartyTaxProfileRoundingRuleCode | ✅ |
| SELF_ASSESS_FLAG | PartyTaxProfileSelfAssessFlag | — |
| SITE_FLAG | PartyTaxProfileSiteFlag | — |
| SUPPLIER_FLAG | PartyTaxProfileSupplierFlag | — |
| TAX_CLASSIFICATION_CODE | PartyTaxProfileTaxClassificationCode | — |
| USE_LE_AS_SUBSCRIBER_FLAG | PartyTaxProfileUseLeAsSubscriberFlag | — |
| WHT_DATE_BASIS | PartyTaxProfileWhtDateBasis | — |
| WHT_EFFECTIVE_FROM_USE_LE | PartyTaxProfileWhtEffectiveFromUseLe | — |
| WHT_ROUNDING_LEVEL_CODE | PartyTaxProfileWhtRoundingLevelCode | — |
| WHT_ROUNDING_RULE_CODE | PartyTaxProfileWhtRoundingRuleCode | — |
| WHT_USE_LE_AS_SUBSCRIBER_FLAG | PartyTaxProfileWhtUseLeAsSubscriberFlag | — |
| WITHHOLDING_START_DATE | PartyTaxProfileWithholdingStartDate | — |

### [[withholdingbucketpvo|WithholdingBucketPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PARTY_ID | PartyTaxProfilePartyId | — |
| PARTY_TAX_PROFILE_ID | PartyTaxProfilePartyTaxProfileId | — |
| PARTY_TYPE_CODE | PartyTaxProfilePartyTypeCode | — |
