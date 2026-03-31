---
id: DOC-OTHER-PVO-TaxRegistrationExtractPVO
doc_type: system-doc
title: "TaxRegistrationExtractPVO — PVO Cross-Module"
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
  - TaxRegistrationExtractPVO
  - taxregistrationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaxRegistrationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Tax Registration Extract. Acessa as tabelas: ZX_REGISTRATIONS.

**Caminho:** `FscmTopModelAM.FinExtractAM.ZxBiccExtractAM.TaxRegistrationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 64 | 1 | 6 | 64 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[zx_registrations|ZX_REGISTRATIONS]] — 64 atributos (6 PKs, 64 BICC)

---

## ⚙️ Atributos

### [[zx_registrations|ZX_REGISTRATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxRegistrationAccountId | ACCOUNT_ID | — | ✅ |
| 2 | TaxRegistrationAccountSiteId | ACCOUNT_SITE_ID | — | ✅ |
| 3 | TaxRegistrationAccountTypeCode | ACCOUNT_TYPE_CODE | — | ✅ |
| 4 | TaxRegistrationAttribute1 | ATTRIBUTE1 | — | ✅ |
| 5 | TaxRegistrationAttribute10 | ATTRIBUTE10 | — | ✅ |
| 6 | TaxRegistrationAttribute11 | ATTRIBUTE11 | — | ✅ |
| 7 | TaxRegistrationAttribute12 | ATTRIBUTE12 | — | ✅ |
| 8 | TaxRegistrationAttribute13 | ATTRIBUTE13 | — | ✅ |
| 9 | TaxRegistrationAttribute14 | ATTRIBUTE14 | — | ✅ |
| 10 | TaxRegistrationAttribute15 | ATTRIBUTE15 | — | ✅ |
| 11 | TaxRegistrationAttribute2 | ATTRIBUTE2 | — | ✅ |
| 12 | TaxRegistrationAttribute3 | ATTRIBUTE3 | — | ✅ |
| 13 | TaxRegistrationAttribute4 | ATTRIBUTE4 | — | ✅ |
| 14 | TaxRegistrationAttribute5 | ATTRIBUTE5 | — | ✅ |
| 15 | TaxRegistrationAttribute6 | ATTRIBUTE6 | — | ✅ |
| 16 | TaxRegistrationAttribute7 | ATTRIBUTE7 | — | ✅ |
| 17 | TaxRegistrationAttribute8 | ATTRIBUTE8 | — | ✅ |
| 18 | TaxRegistrationAttribute9 | ATTRIBUTE9 | — | ✅ |
| 19 | TaxRegistrationAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 20 | TaxRegistrationBankAccountNum | BANK_ACCOUNT_NUM | — | ✅ |
| 21 | TaxRegistrationBankBranchId | BANK_BRANCH_ID | — | ✅ |
| 22 | TaxRegistrationBankId | BANK_ID | — | ✅ |
| 23 | TaxRegistrationCollTaxAuthorityId | COLL_TAX_AUTHORITY_ID | — | ✅ |
| 24 | TaxRegistrationCreatedBy | CREATED_BY | — | ✅ |
| 25 | TaxRegistrationCreationDate | CREATION_DATE | — | ✅ |
| 26 | TaxRegistrationDefaultRegistrationFlag | DEFAULT_REGISTRATION_FLAG | 🔑 | ✅ |
| 27 | TaxRegistrationEffectiveFrom | EFFECTIVE_FROM | — | ✅ |
| 28 | TaxRegistrationEffectiveTo | EFFECTIVE_TO | — | ✅ |
| 29 | TaxRegistrationHasTaxExemptionsFlag | HAS_TAX_EXEMPTIONS_FLAG | — | ✅ |
| 30 | TaxRegistrationInclusiveTaxFlag | INCLUSIVE_TAX_FLAG | — | ✅ |
| 31 | TaxRegistrationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | TaxRegistrationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 33 | TaxRegistrationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 34 | TaxRegistrationLegalLocationId | LEGAL_LOCATION_ID | — | ✅ |
| 35 | TaxRegistrationLegalRegistrationId | LEGAL_REGISTRATION_ID | — | ✅ |
| 36 | TaxRegistrationMaxSelfAssessDiffTolLimit | MAX_SELF_ASSESS_DIFF_TOL_LIMIT | — | ✅ |
| 37 | TaxRegistrationMergedToRegistrationId | MERGED_TO_REGISTRATION_ID | — | ✅ |
| 38 | TaxRegistrationMinSelfAssessDiffTolLimit | MIN_SELF_ASSESS_DIFF_TOL_LIMIT | — | ✅ |
| 39 | TaxRegistrationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 40 | TaxRegistrationPartyTaxProfileId | PARTY_TAX_PROFILE_ID | 🔑 | ✅ |
| 41 | TaxRegistrationRecordTypeCode | RECORD_TYPE_CODE | — | ✅ |
| 42 | TaxRegistrationRegistrationId | REGISTRATION_ID | 🔑 | ✅ |
| 43 | TaxRegistrationRegistrationNumber | REGISTRATION_NUMBER | — | ✅ |
| 44 | TaxRegistrationRegistrationReasonCode | REGISTRATION_REASON_CODE | — | ✅ |
| 45 | TaxRegistrationRegistrationSourceCode | REGISTRATION_SOURCE_CODE | — | ✅ |
| 46 | TaxRegistrationRegistrationStatusCode | REGISTRATION_STATUS_CODE | — | ✅ |
| 47 | TaxRegistrationRegistrationTypeCode | REGISTRATION_TYPE_CODE | — | ✅ |
| 48 | TaxRegistrationRepPartyTaxName | REP_PARTY_TAX_NAME | — | ✅ |
| 49 | TaxRegistrationRepTaxAuthorityId | REP_TAX_AUTHORITY_ID | — | ✅ |
| 50 | TaxRegistrationRequestId | REQUEST_ID | — | ✅ |
| 51 | TaxRegistrationRoundingLevelCode | ROUNDING_LEVEL_CODE | — | ✅ |
| 52 | TaxRegistrationRoundingRuleCode | ROUNDING_RULE_CODE | — | ✅ |
| 53 | TaxRegistrationSelfAssessDiffTolLmtFlag | SELF_ASSESS_DIFF_TOL_LMT_FLAG | — | ✅ |
| 54 | TaxRegistrationSelfAssessFlag | SELF_ASSESS_FLAG | — | ✅ |
| 55 | TaxRegistrationTax | TAX | 🔑 | ✅ |
| 56 | TaxRegistrationTaxAuthorityId | TAX_AUTHORITY_ID | — | ✅ |
| 57 | TaxRegistrationTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | ✅ |
| 58 | TaxRegistrationTaxJurisdictionCode | TAX_JURISDICTION_CODE | 🔑 | ✅ |
| 59 | TaxRegistrationTaxPointBasis | TAX_POINT_BASIS | — | ✅ |
| 60 | TaxRegistrationTaxRegimeCode | TAX_REGIME_CODE | 🔑 | ✅ |
| 61 | TaxRegistrationUniquenessValidationLevel | UNIQUENESS_VALIDATION_LEVEL | — | ✅ |
| 62 | TaxRegistrationValidationLevel | VALIDATION_LEVEL | — | ✅ |
| 63 | TaxRegistrationValidationRoutine | VALIDATION_ROUTINE | — | ✅ |
| 64 | TaxRegistrationValidationType | VALIDATION_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
