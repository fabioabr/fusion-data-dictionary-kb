---
id: DOC-OTHER-PVO-TransactionTaxExtractPVO
doc_type: system-doc
title: "TransactionTaxExtractPVO — PVO Cross-Module"
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
  - TransactionTaxExtractPVO
  - transactiontaxextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionTaxExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transaction Tax Extract. Acessa as tabelas: ZX_TAXES_B, ZX_TAXES_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ZxBiccExtractAM.TransactionTaxExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 126 | 2 | 1 | 110 | 87% |

---

## 🔗 Tabelas Relacionadas

- [[zx_taxes_b|ZX_TAXES_B]] — 117 atributos (1 PKs, 101 BICC)
- [[zx_taxes_tl|ZX_TAXES_TL]] — 9 atributos (9 BICC)

---

## ⚙️ Atributos

### [[zx_taxes_b|ZX_TAXES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionTaxBaseAllowDupRegnNumFlag | ALLOW_DUP_REGN_NUM_FLAG | — | ✅ |
| 2 | TransactionTaxBaseAllowExceptionsFlag | ALLOW_EXCEPTIONS_FLAG | — | ✅ |
| 3 | TransactionTaxBaseAllowExemptionsFlag | ALLOW_EXEMPTIONS_FLAG | — | ✅ |
| 4 | TransactionTaxBaseAllowManualEntryFlag | ALLOW_MANUAL_ENTRY_FLAG | — | ✅ |
| 5 | TransactionTaxBaseAllowMassCreateFlag | ALLOW_MASS_CREATE_FLAG | — | ✅ |
| 6 | TransactionTaxBaseAllowRecoverabilityFlag | ALLOW_RECOVERABILITY_FLAG | — | ✅ |
| 7 | TransactionTaxBaseAllowRoundingOverrideFlag | ALLOW_ROUNDING_OVERRIDE_FLAG | — | ✅ |
| 8 | TransactionTaxBaseAllowTaxOverrideFlag | ALLOW_TAX_OVERRIDE_FLAG | — | ✅ |
| 9 | TransactionTaxBaseAllowZeroAmtWhtInvFlag | ALLOW_ZERO_AMT_WHT_INV_FLAG | — | ✅ |
| 10 | TransactionTaxBaseApplicabilityRuleFlag | APPLICABILITY_RULE_FLAG | — | ✅ |
| 11 | TransactionTaxBaseApplicableByDefaultFlag | APPLICABLE_BY_DEFAULT_FLAG | — | ✅ |
| 12 | TransactionTaxBaseAppliedAmtHandlingFlag | APPLIED_AMT_HANDLING_FLAG | — | ✅ |
| 13 | TransactionTaxBaseAttribute1 | ATTRIBUTE1 | — | — |
| 14 | TransactionTaxBaseAttribute10 | ATTRIBUTE10 | — | — |
| 15 | TransactionTaxBaseAttribute11 | ATTRIBUTE11 | — | — |
| 16 | TransactionTaxBaseAttribute12 | ATTRIBUTE12 | — | — |
| 17 | TransactionTaxBaseAttribute13 | ATTRIBUTE13 | — | — |
| 18 | TransactionTaxBaseAttribute14 | ATTRIBUTE14 | — | — |
| 19 | TransactionTaxBaseAttribute15 | ATTRIBUTE15 | — | — |
| 20 | TransactionTaxBaseAttribute2 | ATTRIBUTE2 | — | — |
| 21 | TransactionTaxBaseAttribute3 | ATTRIBUTE3 | — | — |
| 22 | TransactionTaxBaseAttribute4 | ATTRIBUTE4 | — | — |
| 23 | TransactionTaxBaseAttribute5 | ATTRIBUTE5 | — | — |
| 24 | TransactionTaxBaseAttribute6 | ATTRIBUTE6 | — | — |
| 25 | TransactionTaxBaseAttribute7 | ATTRIBUTE7 | — | — |
| 26 | TransactionTaxBaseAttribute8 | ATTRIBUTE8 | — | — |
| 27 | TransactionTaxBaseAttribute9 | ATTRIBUTE9 | — | — |
| 28 | TransactionTaxBaseAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 29 | TransactionTaxBaseCalcOnlyFlag | CALC_ONLY_FLAG | — | ✅ |
| 30 | TransactionTaxBaseChargeLineHandlingCode | CHARGE_LINE_HANDLING_CODE | — | ✅ |
| 31 | TransactionTaxBaseCollTaxAuthorityId | COLL_TAX_AUTHORITY_ID | — | ✅ |
| 32 | TransactionTaxBaseCompoundingPrecedence | COMPOUNDING_PRECEDENCE | — | ✅ |
| 33 | TransactionTaxBaseContentOwnerId | CONTENT_OWNER_ID | — | ✅ |
| 34 | TransactionTaxBaseCreatedBy | CREATED_BY | — | ✅ |
| 35 | TransactionTaxBaseCreationDate | CREATION_DATE | — | ✅ |
| 36 | TransactionTaxBaseDefInclusiveTaxFlag | DEF_INCLUSIVE_TAX_FLAG | — | ✅ |
| 37 | TransactionTaxBaseDefPlaceOfSupplyTypeCode | DEF_PLACE_OF_SUPPLY_TYPE_CODE | — | ✅ |
| 38 | TransactionTaxBaseDefPrimaryRecRateCode | DEF_PRIMARY_REC_RATE_CODE | — | ✅ |
| 39 | TransactionTaxBaseDefRecSettlementOptionCode | DEF_REC_SETTLEMENT_OPTION_CODE | — | ✅ |
| 40 | TransactionTaxBaseDefRegistrPartyTypeCode | DEF_REGISTR_PARTY_TYPE_CODE | — | ✅ |
| 41 | TransactionTaxBaseDefSecondaryRecRateCode | DEF_SECONDARY_REC_RATE_CODE | — | ✅ |
| 42 | TransactionTaxBaseDefTaxCalcFormula | DEF_TAX_CALC_FORMULA | — | ✅ |
| 43 | TransactionTaxBaseDefTaxableBasisFormula | DEF_TAXABLE_BASIS_FORMULA | — | ✅ |
| 44 | TransactionTaxBaseDirectRateRuleFlag | DIRECT_RATE_RULE_FLAG | — | ✅ |
| 45 | TransactionTaxBaseEffectiveFrom | EFFECTIVE_FROM | — | ✅ |
| 46 | TransactionTaxBaseEffectiveTo | EFFECTIVE_TO | — | ✅ |
| 47 | TransactionTaxBaseExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 48 | TransactionTaxBaseHasOtherJurisdictionsFlag | HAS_OTHER_JURISDICTIONS_FLAG | — | ✅ |
| 49 | TransactionTaxBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 50 | TransactionTaxBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 51 | TransactionTaxBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 52 | TransactionTaxBaseLegalReportingStatusDefVal | LEGAL_REPORTING_STATUS_DEF_VAL | — | ✅ |
| 53 | TransactionTaxBaseLiveForProcessingFlag | LIVE_FOR_PROCESSING_FLAG | — | ✅ |
| 54 | TransactionTaxBaseMaxTaxAmtThrshld | MAX_TAX_AMT_THRSHLD | — | ✅ |
| 55 | TransactionTaxBaseMaxTaxRateThrshld | MAX_TAX_RATE_THRSHLD | — | ✅ |
| 56 | TransactionTaxBaseMaxTxblBsisThrshld | MAX_TXBL_BSIS_THRSHLD | — | ✅ |
| 57 | TransactionTaxBaseMinTaxAmtThrshld | MIN_TAX_AMT_THRSHLD | — | ✅ |
| 58 | TransactionTaxBaseMinTaxRateThrshld | MIN_TAX_RATE_THRSHLD | — | ✅ |
| 59 | TransactionTaxBaseMinTxblBsisThrshld | MIN_TXBL_BSIS_THRSHLD | — | ✅ |
| 60 | TransactionTaxBaseMinimumAccountableUnit | MINIMUM_ACCOUNTABLE_UNIT | — | ✅ |
| 61 | TransactionTaxBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 62 | TransactionTaxBaseOffsetTaxFlag | OFFSET_TAX_FLAG | — | ✅ |
| 63 | TransactionTaxBaseOverrideGeographyType | OVERRIDE_GEOGRAPHY_TYPE | — | ✅ |
| 64 | TransactionTaxBaseParentGeographyId | PARENT_GEOGRAPHY_ID | — | ✅ |
| 65 | TransactionTaxBaseParentGeographyType | PARENT_GEOGRAPHY_TYPE | — | ✅ |
| 66 | TransactionTaxBasePeriodSetName | PERIOD_SET_NAME | — | ✅ |
| 67 | TransactionTaxBasePlaceOfSupplyRuleFlag | PLACE_OF_SUPPLY_RULE_FLAG | — | ✅ |
| 68 | TransactionTaxBasePrimaryRecRateDetRuleFlag | PRIMARY_REC_RATE_DET_RULE_FLAG | — | ✅ |
| 69 | TransactionTaxBasePrimaryRecTypeRuleFlag | PRIMARY_REC_TYPE_RULE_FLAG | — | ✅ |
| 70 | TransactionTaxBasePrimaryRecoveryTypeCode | PRIMARY_RECOVERY_TYPE_CODE | — | ✅ |
| 71 | TransactionTaxBasePrintOnInvoiceFlag | PRINT_ON_INVOICE_FLAG | — | ✅ |
| 72 | TransactionTaxBaseProcessWhtFlag | PROCESS_WHT_FLAG | — | ✅ |
| 73 | TransactionTaxBaseRecordTypeCode | RECORD_TYPE_CODE | — | ✅ |
| 74 | TransactionTaxBaseRecoveryRateOverrideFlag | RECOVERY_RATE_OVERRIDE_FLAG | — | ✅ |
| 75 | TransactionTaxBaseRegistrationTypeRuleFlag | REGISTRATION_TYPE_RULE_FLAG | — | ✅ |
| 76 | TransactionTaxBaseRegnNumSameAsLeFlag | REGN_NUM_SAME_AS_LE_FLAG | — | ✅ |
| 77 | TransactionTaxBaseRepTaxAuthorityId | REP_TAX_AUTHORITY_ID | — | ✅ |
| 78 | TransactionTaxBaseReportingOnlyFlag | REPORTING_ONLY_FLAG | — | ✅ |
| 79 | TransactionTaxBaseRoundingRuleCode | ROUNDING_RULE_CODE | — | ✅ |
| 80 | TransactionTaxBaseSecRecRateDetRuleFlag | SEC_REC_RATE_DET_RULE_FLAG | — | ✅ |
| 81 | TransactionTaxBaseSecondaryRecTypeRuleFlag | SECONDARY_REC_TYPE_RULE_FLAG | — | ✅ |
| 82 | TransactionTaxBaseSecondaryRecoveryTypeCode | SECONDARY_RECOVERY_TYPE_CODE | — | ✅ |
| 83 | TransactionTaxBaseSelfAssessDiffTax | SELF_ASSESS_DIFF_TAX | — | ✅ |
| 84 | TransactionTaxBaseSourceTaxFlag | SOURCE_TAX_FLAG | — | ✅ |
| 85 | TransactionTaxBaseSpecialInclusiveTaxFlag | SPECIAL_INCLUSIVE_TAX_FLAG | — | ✅ |
| 86 | TransactionTaxBaseTax | TAX | — | ✅ |
| 87 | TransactionTaxBaseTaxAccountCreateMethodCode | TAX_ACCOUNT_CREATE_METHOD_CODE | — | ✅ |
| 88 | TransactionTaxBaseTaxAccountSourceTax | TAX_ACCOUNT_SOURCE_TAX | — | ✅ |
| 89 | TransactionTaxBaseTaxAmtThrshldFlag | TAX_AMT_THRSHLD_FLAG | — | ✅ |
| 90 | TransactionTaxBaseTaxAuthInvCreationPoint | TAX_AUTH_INV_CREATION_POINT | — | ✅ |
| 91 | TransactionTaxBaseTaxCalcRuleFlag | TAX_CALC_RULE_FLAG | — | ✅ |
| 92 | TransactionTaxBaseTaxCurrencyCode | TAX_CURRENCY_CODE | — | ✅ |
| 93 | TransactionTaxBaseTaxExmptCrMethodCode | TAX_EXMPT_CR_METHOD_CODE | — | ✅ |
| 94 | TransactionTaxBaseTaxExmptSourceTax | TAX_EXMPT_SOURCE_TAX | — | ✅ |
| 95 | TransactionTaxBaseTaxId | TAX_ID | 🔑 | ✅ |
| 96 | TransactionTaxBaseTaxInclusiveOverrideFlag | TAX_INCLUSIVE_OVERRIDE_FLAG | — | ✅ |
| 97 | TransactionTaxBaseTaxPointBasis | TAX_POINT_BASIS | — | ✅ |
| 98 | TransactionTaxBaseTaxPrecision | TAX_PRECISION | — | ✅ |
| 99 | TransactionTaxBaseTaxRateRuleFlag | TAX_RATE_RULE_FLAG | — | ✅ |
| 100 | TransactionTaxBaseTaxRateThrshldFlag | TAX_RATE_THRSHLD_FLAG | — | ✅ |
| 101 | TransactionTaxBaseTaxRegimeCode | TAX_REGIME_CODE | — | ✅ |
| 102 | TransactionTaxBaseTaxStatusRuleFlag | TAX_STATUS_RULE_FLAG | — | ✅ |
| 103 | TransactionTaxBaseTaxTypeCode | TAX_TYPE_CODE | — | ✅ |
| 104 | TransactionTaxBaseTaxableAmtMau | TAXABLE_AMT_MAU | — | ✅ |
| 105 | TransactionTaxBaseTaxableBasisRuleFlag | TAXABLE_BASIS_RULE_FLAG | — | ✅ |
| 106 | TransactionTaxBaseThrshldChkTmpltCode | THRSHLD_CHK_TMPLT_CODE | — | ✅ |
| 107 | TransactionTaxBaseThrshldGroupingLvlCode | THRSHLD_GROUPING_LVL_CODE | — | ✅ |
| 108 | TransactionTaxBaseThrshldScheduleGrpLvlFlag | THRSHLD_SCHEDULE_GRP_LVL_FLAG | — | ✅ |
| 109 | TransactionTaxBaseTxblBsisThrshldFlag | TXBL_BSIS_THRSHLD_FLAG | — | ✅ |
| 110 | TransactionTaxBaseUniquenessValidationLevel | UNIQUENESS_VALIDATION_LEVEL | — | ✅ |
| 111 | TransactionTaxBaseUseLegalMsgFlag | USE_LEGAL_MSG_FLAG | — | ✅ |
| 112 | TransactionTaxBaseValidationLevel | VALIDATION_LEVEL | — | ✅ |
| 113 | TransactionTaxBaseValidationType | VALIDATION_TYPE | — | ✅ |
| 114 | TransactionTaxBaseWhtBucketLevelFlag | WHT_BUCKET_LEVEL_FLAG | — | ✅ |
| 115 | TransactionTaxBaseWhtCalcPointFlag | WHT_CALC_POINT_FLAG | — | ✅ |
| 116 | TransactionTaxBaseWhtDateBasis | WHT_DATE_BASIS | — | ✅ |
| 117 | TransactionTaxBaseZoneGeographyType | ZONE_GEOGRAPHY_TYPE | — | ✅ |

### [[zx_taxes_tl|ZX_TAXES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionTaxTLCreatedBy | CREATED_BY | — | ✅ |
| 2 | TransactionTaxTLCreationDate | CREATION_DATE | — | ✅ |
| 3 | TransactionTaxTLLanguage | LANGUAGE | — | ✅ |
| 4 | TransactionTaxTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | TransactionTaxTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | TransactionTaxTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | TransactionTaxTLSourceLang | SOURCE_LANG | — | ✅ |
| 8 | TransactionTaxTLTaxFullName | TAX_FULL_NAME | — | ✅ |
| 9 | TransactionTaxTLTaxId | TAX_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
