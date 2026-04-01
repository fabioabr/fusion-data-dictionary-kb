---
id: DOC-AR-PVO-SiteTaxReportingCode
doc_type: system-doc
title: "SiteTaxReportingCode — PVO Accounts Receivable"
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
  - SiteTaxReportingCode
  - sitetaxreportingcode
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SiteTaxReportingCode

## 📌 Visão Geral

Extrai os códigos de reporte fiscal atribuídos a sites de clientes, classificando obrigações de declaração por tipo e jurisdição. Suporta a geração de obrigações acessórias e relatórios fiscais regulatórios.

**Caminho:** `FscmTopModelAM.FinArCustomersPublicModelAM.SiteTaxReportingCode`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 116 | 4 | 1 | 11 | 9% |

---

## 🔗 Tabelas Relacionadas

- [[zx_party_tax_profile|ZX_PARTY_TAX_PROFILE]] — 46 atributos (1 PKs, 2 BICC)
- [[zx_reporting_codes_vl|ZX_REPORTING_CODES_VL]] — 22 atributos (2 BICC)
- [[zx_reporting_types_vl|ZX_REPORTING_TYPES_VL]] — 29 atributos (3 BICC)
- [[zx_report_codes_assoc|ZX_REPORT_CODES_ASSOC]] — 19 atributos (4 BICC)

---

## ⚙️ Atributos

### [[zx_party_tax_profile|ZX_PARTY_TAX_PROFILE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyTaxProfileAllowAwtFlag | ALLOW_AWT_FLAG | — | — |
| 2 | PartyTaxProfileAllowOffsetTaxFlag | ALLOW_OFFSET_TAX_FLAG | — | — |
| 3 | PartyTaxProfileAllowZeroAmtWhtInvFlag | ALLOW_ZERO_AMT_WHT_INV_FLAG | — | — |
| 4 | PartyTaxProfileCollectingAuthorityFlag | COLLECTING_AUTHORITY_FLAG | — | — |
| 5 | PartyTaxProfileCountryCode | COUNTRY_CODE | — | — |
| 6 | PartyTaxProfileCreateAwtDistsTypeCode | CREATE_AWT_DISTS_TYPE_CODE | — | — |
| 7 | PartyTaxProfileCreateAwtInvoicesTypeCode | CREATE_AWT_INVOICES_TYPE_CODE | — | — |
| 8 | PartyTaxProfileCreatedBy | CREATED_BY | — | — |
| 9 | PartyTaxProfileCreationDate | CREATION_DATE | — | — |
| 10 | PartyTaxProfileCustomerFlag | CUSTOMER_FLAG | — | — |
| 11 | PartyTaxProfileEffectiveFromUseLe | EFFECTIVE_FROM_USE_LE | — | — |
| 12 | PartyTaxProfileFirstPartyLeFlag | FIRST_PARTY_LE_FLAG | — | — |
| 13 | PartyTaxProfileId | PARTY_TAX_PROFILE_ID | 🔑 | ✅ |
| 14 | PartyTaxProfileInclusiveTaxFlag | INCLUSIVE_TAX_FLAG | — | — |
| 15 | PartyTaxProfileLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | PartyTaxProfileLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | PartyTaxProfileLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | PartyTaxProfileLegalEstablishmentFlag | LEGAL_ESTABLISHMENT_FLAG | — | — |
| 19 | PartyTaxProfileMergedStatusCode | MERGED_STATUS_CODE | — | — |
| 20 | PartyTaxProfileMergedToPtpId | MERGED_TO_PTP_ID | — | — |
| 21 | PartyTaxProfileObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | PartyTaxProfilePartyId | PARTY_ID | — | — |
| 23 | PartyTaxProfilePartyTypeCode | PARTY_TYPE_CODE | — | — |
| 24 | PartyTaxProfileProcessForApplicabilityFlag | PROCESS_FOR_APPLICABILITY_FLAG | — | — |
| 25 | PartyTaxProfileProgramAppName | PROGRAM_APP_NAME | — | — |
| 26 | PartyTaxProfileProgramLoginId | PROGRAM_LOGIN_ID | — | — |
| 27 | PartyTaxProfileProgramName | PROGRAM_NAME | — | — |
| 28 | PartyTaxProfileProviderTypeCode | PROVIDER_TYPE_CODE | — | — |
| 29 | PartyTaxProfileRecordTypeCode | RECORD_TYPE_CODE | — | — |
| 30 | PartyTaxProfileRegistrationTypeCode | REGISTRATION_TYPE_CODE | — | — |
| 31 | PartyTaxProfileRepRegistrationNumber | REP_REGISTRATION_NUMBER | — | — |
| 32 | PartyTaxProfileReportingAuthorityFlag | REPORTING_AUTHORITY_FLAG | — | — |
| 33 | PartyTaxProfileRequestId | REQUEST_ID | — | — |
| 34 | PartyTaxProfileRoundingLevelCode | ROUNDING_LEVEL_CODE | — | — |
| 35 | PartyTaxProfileRoundingRuleCode | ROUNDING_RULE_CODE | — | — |
| 36 | PartyTaxProfileSelfAssessFlag | SELF_ASSESS_FLAG | — | — |
| 37 | PartyTaxProfileSiteFlag | SITE_FLAG | — | — |
| 38 | PartyTaxProfileSupplierFlag | SUPPLIER_FLAG | — | — |
| 39 | PartyTaxProfileTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 40 | PartyTaxProfileUseLeAsSubscriberFlag | USE_LE_AS_SUBSCRIBER_FLAG | — | — |
| 41 | PartyTaxProfileWhtDateBasis | WHT_DATE_BASIS | — | — |
| 42 | PartyTaxProfileWhtEffectiveFromUseLe | WHT_EFFECTIVE_FROM_USE_LE | — | — |
| 43 | PartyTaxProfileWhtRoundingLevelCode | WHT_ROUNDING_LEVEL_CODE | — | — |
| 44 | PartyTaxProfileWhtRoundingRuleCode | WHT_ROUNDING_RULE_CODE | — | — |
| 45 | PartyTaxProfileWhtUseLeAsSubscriberFlag | WHT_USE_LE_AS_SUBSCRIBER_FLAG | — | — |
| 46 | PartyTaxProfileWithholdingStartDate | WITHHOLDING_START_DATE | — | — |

### [[zx_reporting_codes_vl|ZX_REPORTING_CODES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxRepCodeCreatedBy | CREATED_BY | — | — |
| 2 | TaxRepCodeCreationDate | CREATION_DATE | — | — |
| 3 | TaxRepCodeEffectiveFrom | EFFECTIVE_FROM | — | — |
| 4 | TaxRepCodeEffectiveTo | EFFECTIVE_TO | — | — |
| 5 | TaxRepCodeExceptionCode | EXCEPTION_CODE | — | — |
| 6 | TaxRepCodeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | TaxRepCodeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | TaxRepCodeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | TaxRepCodeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | TaxRepCodeProgramAppName | PROGRAM_APP_NAME | — | — |
| 11 | TaxRepCodeProgramLoginId | PROGRAM_LOGIN_ID | — | — |
| 12 | TaxRepCodeProgramName | PROGRAM_NAME | — | — |
| 13 | TaxRepCodeRecordTypeCode | RECORD_TYPE_CODE | — | — |
| 14 | TaxRepCodeReportingCodeCharValue | REPORTING_CODE_CHAR_VALUE | — | — |
| 15 | TaxRepCodeReportingCodeDateValue | REPORTING_CODE_DATE_VALUE | — | — |
| 16 | TaxRepCodeReportingCodeId | REPORTING_CODE_ID | — | — |
| 17 | TaxRepCodeReportingCodeName | REPORTING_CODE_NAME | — | ✅ |
| 18 | TaxRepCodeReportingCodeNumValue | REPORTING_CODE_NUM_VALUE | — | — |
| 19 | TaxRepCodeReportingTypeId | REPORTING_TYPE_ID | — | — |
| 20 | TaxRepCodeRequestId | REQUEST_ID | — | — |
| 21 | TaxRepCodeSignFlag | SIGN_FLAG | — | — |
| 22 | TaxRepCodeValueTypeCode | VALUE_TYPE_CODE | — | — |

### [[zx_reporting_types_vl|ZX_REPORTING_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxReportingTypeCountryCode | COUNTRY_CODE | — | — |
| 2 | TaxReportingTypeCreatedBy | CREATED_BY | — | — |
| 3 | TaxReportingTypeCreationDate | CREATION_DATE | — | — |
| 4 | TaxReportingTypeEffectiveFrom | EFFECTIVE_FROM | — | — |
| 5 | TaxReportingTypeEffectiveTo | EFFECTIVE_TO | — | — |
| 6 | TaxReportingTypeFormatMask | FORMAT_MASK | — | — |
| 7 | TaxReportingTypeHasReportingCodesFlag | HAS_REPORTING_CODES_FLAG | — | — |
| 8 | TaxReportingTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | TaxReportingTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | TaxReportingTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | TaxReportingTypeLegalMessageFlag | LEGAL_MESSAGE_FLAG | — | — |
| 12 | TaxReportingTypeMaxLength | MAX_LENGTH | — | — |
| 13 | TaxReportingTypeMinLength | MIN_LENGTH | — | — |
| 14 | TaxReportingTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | TaxReportingTypeProgramAppName | PROGRAM_APP_NAME | — | — |
| 16 | TaxReportingTypeProgramLoginId | PROGRAM_LOGIN_ID | — | — |
| 17 | TaxReportingTypeProgramName | PROGRAM_NAME | — | — |
| 18 | TaxReportingTypeRecordTypeCode | RECORD_TYPE_CODE | — | — |
| 19 | TaxReportingTypeRegistrationType | REGISTRATION_TYPE | — | — |
| 20 | TaxReportingTypeReportingTypeCode | REPORTING_TYPE_CODE | — | ✅ |
| 21 | TaxReportingTypeReportingTypeDatatypeCode | REPORTING_TYPE_DATATYPE_CODE | — | ✅ |
| 22 | TaxReportingTypeReportingTypeId | REPORTING_TYPE_ID | — | — |
| 23 | TaxReportingTypeReportingTypeName | REPORTING_TYPE_NAME | — | — |
| 24 | TaxReportingTypeRequestId | REQUEST_ID | — | — |
| 25 | TaxReportingTypeTax | TAX | — | — |
| 26 | TaxReportingTypeTaxRegimeCode | TAX_REGIME_CODE | — | — |
| 27 | TaxReportingTypeUniquenessValidationLevel | UNIQUENESS_VALIDATION_LEVEL | — | — |
| 28 | TaxReportingTypeValidationLevel | VALIDATION_LEVEL | — | — |
| 29 | TaxReportingTypeValidationRoutine | VALIDATION_ROUTINE | — | — |

### [[zx_report_codes_assoc|ZX_REPORT_CODES_ASSOC]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxReportCodeAssocCreatedBy | CREATED_BY | — | — |
| 2 | TaxReportCodeAssocCreationDate | CREATION_DATE | — | — |
| 3 | TaxReportCodeAssocDataFile | DATA_FILE | — | — |
| 4 | TaxReportCodeAssocEffectiveFrom | EFFECTIVE_FROM | — | ✅ |
| 5 | TaxReportCodeAssocEffectiveTo | EFFECTIVE_TO | — | ✅ |
| 6 | TaxReportCodeAssocEntityCode | ENTITY_CODE | — | — |
| 7 | TaxReportCodeAssocEntityId | ENTITY_ID | — | — |
| 8 | TaxReportCodeAssocExceptionCode | EXCEPTION_CODE | — | — |
| 9 | TaxReportCodeAssocLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | TaxReportCodeAssocLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | TaxReportCodeAssocLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | TaxReportCodeAssocObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | TaxReportCodeAssocProcessFileId | PROCESS_FILE_ID | — | — |
| 14 | TaxReportCodeAssocReportCodeDateValue | REPORTING_CODE_DATE_VALUE | — | — |
| 15 | TaxReportCodeAssocReportingCodeAssocId | REPORTING_CODE_ASSOC_ID | — | — |
| 16 | TaxReportCodeAssocReportingCodeCharValue | REPORTING_CODE_CHAR_VALUE | — | ✅ |
| 17 | TaxReportCodeAssocReportingCodeId | REPORTING_CODE_ID | — | — |
| 18 | TaxReportCodeAssocReportingCodeNumValue | REPORTING_CODE_NUM_VALUE | — | — |
| 19 | TaxReportCodeAssocReportingTypeId | REPORTING_TYPE_ID | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
