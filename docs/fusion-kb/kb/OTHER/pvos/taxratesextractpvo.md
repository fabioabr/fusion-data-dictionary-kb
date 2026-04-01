---
id: DOC-OTHER-PVO-TaxRatesExtractPVO
doc_type: system-doc
title: "TaxRatesExtractPVO — PVO Cross-Module"
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
  - TaxRatesExtractPVO
  - taxratesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaxRatesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Tax Rates Extract. Acessa as tabelas: ZX_RATES_B, ZX_RATES_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ZxBiccExtractAM.TaxRatesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 80 | 2 | 1 | 54 | 68% |

---

## 🔗 Tabelas Relacionadas

- [[zx_rates_b|ZX_RATES_B]] — 70 atributos (1 PKs, 44 BICC)
- [[zx_rates_tl|ZX_RATES_TL]] — 10 atributos (10 BICC)

---

## ⚙️ Atributos

### [[zx_rates_b|ZX_RATES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxRatesActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | TaxRatesAdjForAdhocAmtCode | ADJ_FOR_ADHOC_AMT_CODE | — | ✅ |
| 3 | TaxRatesAllowAdhocTaxRateFlag | ALLOW_ADHOC_TAX_RATE_FLAG | — | ✅ |
| 4 | TaxRatesAllowExceptionsFlag | ALLOW_EXCEPTIONS_FLAG | — | ✅ |
| 5 | TaxRatesAllowExemptionsFlag | ALLOW_EXEMPTIONS_FLAG | — | ✅ |
| 6 | TaxRatesAttribute1 | ATTRIBUTE1 | — | — |
| 7 | TaxRatesAttribute10 | ATTRIBUTE10 | — | — |
| 8 | TaxRatesAttribute11 | ATTRIBUTE11 | — | — |
| 9 | TaxRatesAttribute12 | ATTRIBUTE12 | — | — |
| 10 | TaxRatesAttribute13 | ATTRIBUTE13 | — | — |
| 11 | TaxRatesAttribute14 | ATTRIBUTE14 | — | — |
| 12 | TaxRatesAttribute15 | ATTRIBUTE15 | — | — |
| 13 | TaxRatesAttribute2 | ATTRIBUTE2 | — | — |
| 14 | TaxRatesAttribute3 | ATTRIBUTE3 | — | — |
| 15 | TaxRatesAttribute4 | ATTRIBUTE4 | — | — |
| 16 | TaxRatesAttribute5 | ATTRIBUTE5 | — | — |
| 17 | TaxRatesAttribute6 | ATTRIBUTE6 | — | — |
| 18 | TaxRatesAttribute7 | ATTRIBUTE7 | — | — |
| 19 | TaxRatesAttribute8 | ATTRIBUTE8 | — | — |
| 20 | TaxRatesAttribute9 | ATTRIBUTE9 | — | — |
| 21 | TaxRatesAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | TaxRatesAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | TaxRatesAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 24 | TaxRatesAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 25 | TaxRatesAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 26 | TaxRatesAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 27 | TaxRatesAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 28 | TaxRatesAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 29 | TaxRatesAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 30 | TaxRatesAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 31 | TaxRatesAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 32 | TaxRatesContentOwnerId | CONTENT_OWNER_ID | — | ✅ |
| 33 | TaxRatesCreatedBy | CREATED_BY | — | ✅ |
| 34 | TaxRatesCreationDate | CREATION_DATE | — | ✅ |
| 35 | TaxRatesDefRecSettlementOptionCode | DEF_REC_SETTLEMENT_OPTION_CODE | — | ✅ |
| 36 | TaxRatesDefaultFlgEffectiveFrom | DEFAULT_FLG_EFFECTIVE_FROM | — | ✅ |
| 37 | TaxRatesDefaultFlgEffectiveTo | DEFAULT_FLG_EFFECTIVE_TO | — | ✅ |
| 38 | TaxRatesDefaultRateFlag | DEFAULT_RATE_FLAG | — | ✅ |
| 39 | TaxRatesDefaultRecRateCode | DEFAULT_REC_RATE_CODE | — | ✅ |
| 40 | TaxRatesDefaultRecTypeCode | DEFAULT_REC_TYPE_CODE | — | ✅ |
| 41 | TaxRatesDescription | DESCRIPTION | — | ✅ |
| 42 | TaxRatesEffectiveFrom | EFFECTIVE_FROM | — | ✅ |
| 43 | TaxRatesEffectiveTo | EFFECTIVE_TO | — | ✅ |
| 44 | TaxRatesInclusiveTaxFlag | INCLUSIVE_TAX_FLAG | — | ✅ |
| 45 | TaxRatesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 46 | TaxRatesLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 47 | TaxRatesLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 48 | TaxRatesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 49 | TaxRatesOffsetStatusCode | OFFSET_STATUS_CODE | — | ✅ |
| 50 | TaxRatesOffsetTax | OFFSET_TAX | — | ✅ |
| 51 | TaxRatesOffsetTaxRateCode | OFFSET_TAX_RATE_CODE | — | ✅ |
| 52 | TaxRatesPercentageRate | PERCENTAGE_RATE | — | ✅ |
| 53 | TaxRatesQuantityRate | QUANTITY_RATE | — | ✅ |
| 54 | TaxRatesRateTypeCode | RATE_TYPE_CODE | — | ✅ |
| 55 | TaxRatesRecordTypeCode | RECORD_TYPE_CODE | — | ✅ |
| 56 | TaxRatesRecoveryRuleCode | RECOVERY_RULE_CODE | — | ✅ |
| 57 | TaxRatesRecoveryTypeCode | RECOVERY_TYPE_CODE | — | ✅ |
| 58 | TaxRatesScheduleBasedRateFlag | SCHEDULE_BASED_RATE_FLAG | — | ✅ |
| 59 | TaxRatesSourceId | SOURCE_ID | — | ✅ |
| 60 | TaxRatesTax | TAX | — | ✅ |
| 61 | TaxRatesTaxClass | TAX_CLASS | — | ✅ |
| 62 | TaxRatesTaxInclusiveOverrideFlag | TAX_INCLUSIVE_OVERRIDE_FLAG | — | ✅ |
| 63 | TaxRatesTaxJurisdictionCode | TAX_JURISDICTION_CODE | — | ✅ |
| 64 | TaxRatesTaxRateCode | TAX_RATE_CODE | — | ✅ |
| 65 | TaxRatesTaxRateId | TAX_RATE_ID | 🔑 | ✅ |
| 66 | TaxRatesTaxRegimeCode | TAX_REGIME_CODE | — | ✅ |
| 67 | TaxRatesTaxStatusCode | TAX_STATUS_CODE | — | ✅ |
| 68 | TaxRatesTaxableBasisFormulaCode | TAXABLE_BASIS_FORMULA_CODE | — | ✅ |
| 69 | TaxRatesUomCode | UOM_CODE | — | ✅ |
| 70 | TaxRatesVatTransactionTypeCode | VAT_TRANSACTION_TYPE_CODE | — | ✅ |

### [[zx_rates_tl|ZX_RATES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxRatesTLCreatedBy | CREATED_BY | — | ✅ |
| 2 | TaxRatesTLCreationDate | CREATION_DATE | — | ✅ |
| 3 | TaxRatesTLDescription | DESCRIPTION | — | ✅ |
| 4 | TaxRatesTLLanguage | LANGUAGE | — | ✅ |
| 5 | TaxRatesTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | TaxRatesTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | TaxRatesTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | TaxRatesTLSourceLang | SOURCE_LANG | — | ✅ |
| 9 | TaxRatesTLTaxRateId | TAX_RATE_ID | — | ✅ |
| 10 | TaxRatesTLTaxRateName | TAX_RATE_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
