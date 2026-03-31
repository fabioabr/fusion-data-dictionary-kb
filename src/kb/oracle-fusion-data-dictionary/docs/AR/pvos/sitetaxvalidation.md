---
id: DOC-AR-PVO-SiteTaxValidation
doc_type: system-doc
title: "SiteTaxValidation — PVO Accounts Receivable"
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
  - SiteTaxValidation
  - sitetaxvalidation
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SiteTaxValidation

## 📌 Visão Geral

Extrai as validações de identificação fiscal (tax IDs) de sites de clientes. Garante a integridade dos dados cadastrais fiscais para emissão de documentos e cumprimento de obrigações regulatórias.

**Caminho:** `FscmTopModelAM.FinArCustomersPublicModelAM.SiteTaxValidation`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 60 | 2 | 1 | 10 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[zx_party_taxpayer_idntfs|ZX_PARTY_TAXPAYER_IDNTFS]] — 14 atributos (5 BICC)
- [[zx_party_tax_profile|ZX_PARTY_TAX_PROFILE]] — 46 atributos (1 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[zx_party_taxpayer_idntfs|ZX_PARTY_TAXPAYER_IDNTFS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyTaxpayerIdentCountryCode | COUNTRY_CODE | — | — |
| 2 | PartyTaxpayerIdentCreatedBy | CREATED_BY | — | — |
| 3 | PartyTaxpayerIdentCreationDate | CREATION_DATE | — | — |
| 4 | PartyTaxpayerIdentEffectiveFrom | EFFECTIVE_FROM | — | ✅ |
| 5 | PartyTaxpayerIdentEffectiveTo | EFFECTIVE_TO | — | ✅ |
| 6 | PartyTaxpayerIdentEntityId | ENTITY_ID | — | — |
| 7 | PartyTaxpayerIdentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PartyTaxpayerIdentLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | PartyTaxpayerIdentLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | PartyTaxpayerIdentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | PartyTaxpayerIdentRecordTypeCode | RECORD_TYPE_CODE | — | — |
| 12 | PartyTaxpayerIdentReportingTypeCode | REPORTING_TYPE_CODE | — | ✅ |
| 13 | PartyTaxpayerIdentTaxPayerNumber | TAX_PAYER_NUMBER | — | ✅ |
| 14 | PartyTaxpayerIdntfsId | PARTY_TAXPAYER_IDNTFS_ID | — | — |

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
| 14 | PartyTaxProfileInclusiveTaxFlag | INCLUSIVE_TAX_FLAG | — | ✅ |
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
| 34 | PartyTaxProfileRoundingLevelCode | ROUNDING_LEVEL_CODE | — | ✅ |
| 35 | PartyTaxProfileRoundingRuleCode | ROUNDING_RULE_CODE | — | ✅ |
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

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
