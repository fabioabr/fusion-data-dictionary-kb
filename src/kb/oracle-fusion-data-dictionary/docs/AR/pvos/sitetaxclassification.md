---
id: DOC-AR-PVO-SiteTaxClassification
doc_type: system-doc
title: "SiteTaxClassification — PVO Accounts Receivable"
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
  - SiteTaxClassification
  - sitetaxclassification
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SiteTaxClassification

## 📌 Visão Geral

Extrai as classificações fiscais atribuídas a sites de clientes, com categorias e tipos fiscais. Determina o tratamento tributário aplicável por localidade do cliente para cálculo correto de impostos.

**Caminho:** `FscmTopModelAM.FinArCustomersPublicModelAM.SiteTaxClassification`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 94 | 4 | 1 | 10 | 11% |

---

## 🔗 Tabelas Relacionadas

- [[hz_class_category_codes_v|HZ_CLASS_CATEGORY_CODES_V]] — 8 atributos (1 BICC)
- [[hz_code_assignments|HZ_CODE_ASSIGNMENTS]] — 18 atributos (4 BICC)
- [[zx_fc_types_vl|ZX_FC_TYPES_VL]] — 25 atributos (3 BICC)
- [[zx_party_tax_profile|ZX_PARTY_TAX_PROFILE]] — 43 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[hz_class_category_codes_v|HZ_CLASS_CATEGORY_CODES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClassCatCodeClassCategory | CLASS_CATEGORY | — | — |
| 2 | ClassCatCodeClassCode | CLASS_CODE | — | — |
| 3 | ClassCatCodeDescription | DESCRIPTION | — | — |
| 4 | ClassCatCodeEndDateActive | END_DATE_ACTIVE | — | — |
| 5 | ClassCatCodeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | ClassCatCodeMeaning | MEANING | — | ✅ |
| 7 | ClassCatCodeStartDateActive | START_DATE_ACTIVE | — | — |
| 8 | ClassCatCodeViewApplicationId | VIEW_APPLICATION_ID | — | — |

### [[hz_code_assignments|HZ_CODE_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CodeAssignmentClassCategory | CLASS_CATEGORY | — | — |
| 2 | CodeAssignmentClassCode | CLASS_CODE | — | ✅ |
| 3 | CodeAssignmentCodeAssignmentId | CODE_ASSIGNMENT_ID | — | — |
| 4 | CodeAssignmentCreatedBy | CREATED_BY | — | — |
| 5 | CodeAssignmentCreatedByModule | CREATED_BY_MODULE | — | — |
| 6 | CodeAssignmentCreationDate | CREATION_DATE | — | — |
| 7 | CodeAssignmentEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 8 | CodeAssignmentJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 9 | CodeAssignmentJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 10 | CodeAssignmentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | CodeAssignmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | CodeAssignmentLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | CodeAssignmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | CodeAssignmentOwnerTableId | OWNER_TABLE_ID | — | — |
| 15 | CodeAssignmentPrimaryFlag | PRIMARY_FLAG | — | — |
| 16 | CodeAssignmentRank | RANK | — | — |
| 17 | CodeAssignmentStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 18 | CodeAssignmentStatus | STATUS | — | — |

### [[zx_fc_types_vl|ZX_FC_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalClassTypeClassificationTypeCategCode | CLASSIFICATION_TYPE_CATEG_CODE | — | — |
| 2 | FiscalClassTypeClassificationTypeCode | CLASSIFICATION_TYPE_CODE | — | ✅ |
| 3 | FiscalClassTypeClassificationTypeGroupCode | CLASSIFICATION_TYPE_GROUP_CODE | — | — |
| 4 | FiscalClassTypeClassificationTypeId | CLASSIFICATION_TYPE_ID | — | — |
| 5 | FiscalClassTypeClassificationTypeLevelCode | CLASSIFICATION_TYPE_LEVEL_CODE | — | — |
| 6 | FiscalClassTypeClassificationTypeName | CLASSIFICATION_TYPE_NAME | — | ✅ |
| 7 | FiscalClassTypeCreatedBy | CREATED_BY | — | — |
| 8 | FiscalClassTypeCreationDate | CREATION_DATE | — | — |
| 9 | FiscalClassTypeDelimiter | DELIMITER | — | — |
| 10 | FiscalClassTypeEffectiveFrom | EFFECTIVE_FROM | — | — |
| 11 | FiscalClassTypeEffectiveTo | EFFECTIVE_TO | — | — |
| 12 | FiscalClassTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | FiscalClassTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | FiscalClassTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | FiscalClassTypeNumCharacters | NUM_CHARACTERS | — | — |
| 16 | FiscalClassTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | FiscalClassTypeOwnerIdChar | OWNER_ID_CHAR | — | — |
| 18 | FiscalClassTypeOwnerIdNum | OWNER_ID_NUM | — | — |
| 19 | FiscalClassTypeOwnerTableCode | OWNER_TABLE_CODE | — | — |
| 20 | FiscalClassTypeProgramAppName | PROGRAM_APP_NAME | — | — |
| 21 | FiscalClassTypeProgramLoginId | PROGRAM_LOGIN_ID | — | — |
| 22 | FiscalClassTypeProgramName | PROGRAM_NAME | — | — |
| 23 | FiscalClassTypeRecordTypeCode | RECORD_TYPE_CODE | — | — |
| 24 | FiscalClassTypeRequestId | REQUEST_ID | — | — |
| 25 | FiscalClassTypeStartPosition | START_POSITION | — | — |

### [[zx_party_tax_profile|ZX_PARTY_TAX_PROFILE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyTaxProfileCollectingAuthorityFlag | COLLECTING_AUTHORITY_FLAG | — | — |
| 2 | PartyTaxProfileCountryCode | COUNTRY_CODE | — | — |
| 3 | PartyTaxProfileCreateAwtDistsTypeCode | CREATE_AWT_DISTS_TYPE_CODE | — | — |
| 4 | PartyTaxProfileCreateAwtInvoicesTypeCode | CREATE_AWT_INVOICES_TYPE_CODE | — | — |
| 5 | PartyTaxProfileCreatedBy | CREATED_BY | — | — |
| 6 | PartyTaxProfileCreationDate | CREATION_DATE | — | — |
| 7 | PartyTaxProfileCustomerFlag | CUSTOMER_FLAG | — | — |
| 8 | PartyTaxProfileEffectiveFromUseLe | EFFECTIVE_FROM_USE_LE | — | — |
| 9 | PartyTaxProfileFirstPartyLeFlag | FIRST_PARTY_LE_FLAG | — | — |
| 10 | PartyTaxProfileId | PARTY_TAX_PROFILE_ID | 🔑 | ✅ |
| 11 | PartyTaxProfileInclusiveTaxFlag | INCLUSIVE_TAX_FLAG | — | — |
| 12 | PartyTaxProfileLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | PartyTaxProfileLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | PartyTaxProfileLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | PartyTaxProfileLegalEstablishmentFlag | LEGAL_ESTABLISHMENT_FLAG | — | — |
| 16 | PartyTaxProfileMergedStatusCode | MERGED_STATUS_CODE | — | — |
| 17 | PartyTaxProfileMergedToPtpId | MERGED_TO_PTP_ID | — | — |
| 18 | PartyTaxProfileObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | PartyTaxProfilePartyId | PARTY_ID | — | — |
| 20 | PartyTaxProfilePartyTypeCode | PARTY_TYPE_CODE | — | — |
| 21 | PartyTaxProfileProcessForApplicabilityFlag | PROCESS_FOR_APPLICABILITY_FLAG | — | — |
| 22 | PartyTaxProfileProgramAppName | PROGRAM_APP_NAME | — | — |
| 23 | PartyTaxProfileProgramLoginId | PROGRAM_LOGIN_ID | — | — |
| 24 | PartyTaxProfileProgramName | PROGRAM_NAME | — | — |
| 25 | PartyTaxProfileProviderTypeCode | PROVIDER_TYPE_CODE | — | — |
| 26 | PartyTaxProfileRecordTypeCode | RECORD_TYPE_CODE | — | — |
| 27 | PartyTaxProfileRegistrationTypeCode | REGISTRATION_TYPE_CODE | — | — |
| 28 | PartyTaxProfileRepRegistrationNumber | REP_REGISTRATION_NUMBER | — | — |
| 29 | PartyTaxProfileReportingAuthorityFlag | REPORTING_AUTHORITY_FLAG | — | — |
| 30 | PartyTaxProfileRequestId | REQUEST_ID | — | — |
| 31 | PartyTaxProfileRoundingLevelCode | ROUNDING_LEVEL_CODE | — | — |
| 32 | PartyTaxProfileRoundingRuleCode | ROUNDING_RULE_CODE | — | — |
| 33 | PartyTaxProfileSelfAssessFlag | SELF_ASSESS_FLAG | — | — |
| 34 | PartyTaxProfileSiteFlag | SITE_FLAG | — | — |
| 35 | PartyTaxProfileSupplierFlag | SUPPLIER_FLAG | — | — |
| 36 | PartyTaxProfileTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 37 | PartyTaxProfileUseLeAsSubscriberFlag | USE_LE_AS_SUBSCRIBER_FLAG | — | — |
| 38 | PartyTaxProfileWhtDateBasis | WHT_DATE_BASIS | — | — |
| 39 | PartyTaxProfileWhtEffectiveFromUseLe | WHT_EFFECTIVE_FROM_USE_LE | — | — |
| 40 | PartyTaxProfileWhtRoundingLevelCode | WHT_ROUNDING_LEVEL_CODE | — | — |
| 41 | PartyTaxProfileWhtRoundingRuleCode | WHT_ROUNDING_RULE_CODE | — | — |
| 42 | PartyTaxProfileWhtUseLeAsSubscriberFlag | WHT_USE_LE_AS_SUBSCRIBER_FLAG | — | — |
| 43 | PartyTaxProfileWithholdingStartDate | WITHHOLDING_START_DATE | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
