---
id: DOC-OTHER-PVO-TaxRegimeExtractPVO
doc_type: system-doc
title: "TaxRegimeExtractPVO — PVO Cross-Module"
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
  - TaxRegimeExtractPVO
  - taxregimeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaxRegimeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Tax Regime Extract. Acessa as tabelas: ZX_REGIMES_B, ZX_REGIMES_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ZxBiccExtractAM.TaxRegimeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 84 | 2 | 1 | 68 | 81% |

---

## 🔗 Tabelas Relacionadas

- [[zx_regimes_b|ZX_REGIMES_B]] — 75 atributos (1 PKs, 59 BICC)
- [[zx_regimes_tl|ZX_REGIMES_TL]] — 9 atributos (9 BICC)

---

## ⚙️ Atributos

### [[zx_regimes_b|ZX_REGIMES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxRegimeAllowExceptionsFlag | ALLOW_EXCEPTIONS_FLAG | — | ✅ |
| 2 | TaxRegimeAllowExemptionsFlag | ALLOW_EXEMPTIONS_FLAG | — | ✅ |
| 3 | TaxRegimeAllowRecoverabilityFlag | ALLOW_RECOVERABILITY_FLAG | — | ✅ |
| 4 | TaxRegimeAllowRoundingOverrideFlag | ALLOW_ROUNDING_OVERRIDE_FLAG | — | ✅ |
| 5 | TaxRegimeApplicabilityRuleFlag | APPLICABILITY_RULE_FLAG | — | ✅ |
| 6 | TaxRegimeAttribute1 | ATTRIBUTE1 | — | — |
| 7 | TaxRegimeAttribute10 | ATTRIBUTE10 | — | — |
| 8 | TaxRegimeAttribute11 | ATTRIBUTE11 | — | — |
| 9 | TaxRegimeAttribute12 | ATTRIBUTE12 | — | — |
| 10 | TaxRegimeAttribute13 | ATTRIBUTE13 | — | — |
| 11 | TaxRegimeAttribute14 | ATTRIBUTE14 | — | — |
| 12 | TaxRegimeAttribute15 | ATTRIBUTE15 | — | — |
| 13 | TaxRegimeAttribute2 | ATTRIBUTE2 | — | — |
| 14 | TaxRegimeAttribute3 | ATTRIBUTE3 | — | — |
| 15 | TaxRegimeAttribute4 | ATTRIBUTE4 | — | — |
| 16 | TaxRegimeAttribute5 | ATTRIBUTE5 | — | — |
| 17 | TaxRegimeAttribute6 | ATTRIBUTE6 | — | — |
| 18 | TaxRegimeAttribute7 | ATTRIBUTE7 | — | — |
| 19 | TaxRegimeAttribute8 | ATTRIBUTE8 | — | — |
| 20 | TaxRegimeAttribute9 | ATTRIBUTE9 | — | — |
| 21 | TaxRegimeAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | TaxRegimeBucketLevelFlag | BUCKET_LEVEL_FLAG | — | ✅ |
| 23 | TaxRegimeCollTaxAuthorityId | COLL_TAX_AUTHORITY_ID | — | ✅ |
| 24 | TaxRegimeCountryCode | COUNTRY_CODE | — | ✅ |
| 25 | TaxRegimeCountryOrGroupCode | COUNTRY_OR_GROUP_CODE | — | ✅ |
| 26 | TaxRegimeCreatedBy | CREATED_BY | — | ✅ |
| 27 | TaxRegimeCreationDate | CREATION_DATE | — | ✅ |
| 28 | TaxRegimeCrossRegimeCompoundingFlag | CROSS_REGIME_COMPOUNDING_FLAG | — | ✅ |
| 29 | TaxRegimeDefInclusiveTaxFlag | DEF_INCLUSIVE_TAX_FLAG | — | ✅ |
| 30 | TaxRegimeDefPlaceOfSupplyTypeCode | DEF_PLACE_OF_SUPPLY_TYPE_CODE | — | ✅ |
| 31 | TaxRegimeDefRecSettlementOptionCode | DEF_REC_SETTLEMENT_OPTION_CODE | — | ✅ |
| 32 | TaxRegimeDefRegistrPartyTypeCode | DEF_REGISTR_PARTY_TYPE_CODE | — | ✅ |
| 33 | TaxRegimeEffectiveFrom | EFFECTIVE_FROM | — | ✅ |
| 34 | TaxRegimeEffectiveTo | EFFECTIVE_TO | — | ✅ |
| 35 | TaxRegimeExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 36 | TaxRegimeExemptionProcessFlag | EXEMPTION_PROCESS_FLAG | — | ✅ |
| 37 | TaxRegimeGeographyId | GEOGRAPHY_ID | — | ✅ |
| 38 | TaxRegimeGeographyType | GEOGRAPHY_TYPE | — | ✅ |
| 39 | TaxRegimeHasOtherJurisdictionsFlag | HAS_OTHER_JURISDICTIONS_FLAG | — | ✅ |
| 40 | TaxRegimeHasSubRegimeFlag | HAS_SUB_REGIME_FLAG | — | ✅ |
| 41 | TaxRegimeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 42 | TaxRegimeLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 43 | TaxRegimeLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 44 | TaxRegimeMinimumAccountableUnit | MINIMUM_ACCOUNTABLE_UNIT | — | ✅ |
| 45 | TaxRegimeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 46 | TaxRegimeParentRegimeCode | PARENT_REGIME_CODE | — | ✅ |
| 47 | TaxRegimePeriodSetName | PERIOD_SET_NAME | — | ✅ |
| 48 | TaxRegimePlaceOfSupplyRuleFlag | PLACE_OF_SUPPLY_RULE_FLAG | — | ✅ |
| 49 | TaxRegimeRecordTypeCode | RECORD_TYPE_CODE | — | ✅ |
| 50 | TaxRegimeRegimePrecedence | REGIME_PRECEDENCE | — | ✅ |
| 51 | TaxRegimeRegimeTypeFlag | REGIME_TYPE_FLAG | — | ✅ |
| 52 | TaxRegimeRegistrationTypeRuleFlag | REGISTRATION_TYPE_RULE_FLAG | — | ✅ |
| 53 | TaxRegimeRegnNumSameAsLeFlag | REGN_NUM_SAME_AS_LE_FLAG | — | ✅ |
| 54 | TaxRegimeRepTaxAuthorityId | REP_TAX_AUTHORITY_ID | — | ✅ |
| 55 | TaxRegimeRoundingRuleCode | ROUNDING_RULE_CODE | — | ✅ |
| 56 | TaxRegimeTaxAccountPrecedenceCode | TAX_ACCOUNT_PRECEDENCE_CODE | — | ✅ |
| 57 | TaxRegimeTaxAmtThrshldFlag | TAX_AMT_THRSHLD_FLAG | — | ✅ |
| 58 | TaxRegimeTaxCalcRuleFlag | TAX_CALC_RULE_FLAG | — | ✅ |
| 59 | TaxRegimeTaxCurrencyCode | TAX_CURRENCY_CODE | — | ✅ |
| 60 | TaxRegimeTaxInclusiveOverrideFlag | TAX_INCLUSIVE_OVERRIDE_FLAG | — | ✅ |
| 61 | TaxRegimeTaxPrecision | TAX_PRECISION | — | ✅ |
| 62 | TaxRegimeTaxRateRuleFlag | TAX_RATE_RULE_FLAG | — | ✅ |
| 63 | TaxRegimeTaxRateThrshldFlag | TAX_RATE_THRSHLD_FLAG | — | ✅ |
| 64 | TaxRegimeTaxRegimeCode | TAX_REGIME_CODE | 🔑 | ✅ |
| 65 | TaxRegimeTaxRegimeId | TAX_REGIME_ID | — | ✅ |
| 66 | TaxRegimeTaxStatusRuleFlag | TAX_STATUS_RULE_FLAG | — | ✅ |
| 67 | TaxRegimeTaxableBasisRuleFlag | TAXABLE_BASIS_RULE_FLAG | — | ✅ |
| 68 | TaxRegimeTaxableBasisThrshldFlag | TAXABLE_BASIS_THRSHLD_FLAG | — | ✅ |
| 69 | TaxRegimeThrshldChkTmpltCode | THRSHLD_CHK_TMPLT_CODE | — | ✅ |
| 70 | TaxRegimeThrshldGroupingLvlCode | THRSHLD_GROUPING_LVL_CODE | — | ✅ |
| 71 | TaxRegimeUniquenessValidationLevel | UNIQUENESS_VALIDATION_LEVEL | — | ✅ |
| 72 | TaxRegimeUseLegalMsgFlag | USE_LEGAL_MSG_FLAG | — | ✅ |
| 73 | TaxRegimeUseTaxReportConfigFlag | USE_TAX_REPORT_CONFIG_FLAG | — | ✅ |
| 74 | TaxRegimeValidationLevel | VALIDATION_LEVEL | — | ✅ |
| 75 | TaxRegimeValidationType | VALIDATION_TYPE | — | ✅ |

### [[zx_regimes_tl|ZX_REGIMES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxRegimeTLCreatedBy1 | CREATED_BY | — | ✅ |
| 2 | TaxRegimeTLCreationDate1 | CREATION_DATE | — | ✅ |
| 3 | TaxRegimeTLLanguage | LANGUAGE | — | ✅ |
| 4 | TaxRegimeTLLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 5 | TaxRegimeTLLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | TaxRegimeTLLastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 7 | TaxRegimeTLSourceLang | SOURCE_LANG | — | ✅ |
| 8 | TaxRegimeTLTaxRegimeId | TAX_REGIME_ID | — | ✅ |
| 9 | TaxRegimeTLTaxRegimeName | TAX_REGIME_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
