---
id: DOC-HCM-908
doc_type: system-doc
title: "ZX_SCO_RATES — (título a preencher)"
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
  - ZX_SCO_RATES
  - zx_sco_rates
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# ZX_SCO_RATES

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACTIVE_FLAG | — | — | — | — | — | — |
| 2 | ADJ_FOR_ADHOC_AMT_CODE | — | — | — | — | — | — |
| 3 | ALLOW_ADHOC_TAX_RATE_FLAG | — | — | — | — | — | — |
| 4 | ALLOW_EXCEPTIONS_FLAG | — | — | — | — | — | — |
| 5 | ALLOW_EXEMPTIONS_FLAG | — | — | — | — | — | — |
| 6 | DEFAULT_FLG_EFFECTIVE_FROM | — | — | — | — | — | — |
| 7 | DEFAULT_FLG_EFFECTIVE_TO | — | — | — | — | — | — |
| 8 | DEFAULT_RATE_FLAG | — | — | — | — | — | — |
| 9 | DEFAULT_REC_RATE_CODE | — | — | — | — | — | — |
| 10 | DEFAULT_REC_TYPE_CODE | — | — | — | — | — | — |
| 11 | DEF_REC_SETTLEMENT_OPTION_CODE | — | — | — | — | — | — |
| 12 | DESCRIPTION | — | — | — | — | — | — |
| 13 | EFFECTIVE_FROM | — | — | — | — | — | — |
| 14 | EFFECTIVE_TO | — | — | — | — | — | — |
| 15 | INCLUSIVE_TAX_FLAG | — | — | — | — | — | — |
| 16 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 17 | OFFSET_STATUS_CODE | — | — | — | — | — | — |
| 18 | OFFSET_TAX | — | — | — | — | — | — |
| 19 | OFFSET_TAX_RATE_CODE | — | — | — | — | — | — |
| 20 | PERCENTAGE_RATE | — | — | — | — | — | — |
| 21 | PROGRAM_APP_NAME | — | — | — | — | — | — |
| 22 | PROGRAM_NAME | — | — | — | — | — | — |
| 23 | QUANTITY_RATE | — | — | — | — | — | — |
| 24 | RATE_TYPE_CODE | — | — | — | — | — | — |
| 25 | RECORD_TYPE_CODE | — | — | — | — | — | — |
| 26 | RECOVERY_RULE_CODE | — | — | — | — | — | — |
| 27 | RECOVERY_TYPE_CODE | — | — | — | — | — | — |
| 28 | SCHEDULE_BASED_RATE_FLAG | — | — | — | — | — | — |
| 29 | SDEFF_FROM | — | — | — | — | — | — |
| 30 | SDEFF_TO | — | — | — | — | — | — |
| 31 | TAX | — | — | — | — | — | — |
| 32 | TAXABLE_BASIS_FORMULA_CODE | — | — | — | — | — | — |
| 33 | TAX_CLASS | — | — | — | — | — | — |
| 34 | TAX_INCLUSIVE_OVERRIDE_FLAG | — | — | — | — | — | — |
| 35 | TAX_JURISDICTION_CODE | — | — | — | — | — | — |
| 36 | TAX_RATE_CODE | — | — | — | — | — | — |
| 37 | TAX_RATE_ID | — | — | — | — | — | — |
| 38 | TAX_RATE_NAME | — | — | — | — | — | — |
| 39 | TAX_REGIME_CODE | — | — | — | — | — | — |
| 40 | TAX_STATUS_CODE | — | — | — | — | — | — |
| 41 | UOM_CODE | — | — | — | — | — | — |
| 42 | VAT_TRANSACTION_TYPE_CODE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[miscreceiptdistributionpvo|MiscReceiptDistributionPVO]] (AR · BICC: 1/42)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | TaxRtScoActiveFlag | — |
| ADJ_FOR_ADHOC_AMT_CODE | TaxRtScoAdjForAdhocAmtCode | — |
| ALLOW_ADHOC_TAX_RATE_FLAG | TaxRtScoAllowAdhocTaxRateFlag | — |
| ALLOW_EXCEPTIONS_FLAG | TaxRtScoAllowExceptionsFlag | — |
| ALLOW_EXEMPTIONS_FLAG | TaxRtScoAllowExemptionsFlag | — |
| DEF_REC_SETTLEMENT_OPTION_CODE | TaxRtScoDefRecSettlementOptionCode | — |
| DEFAULT_FLG_EFFECTIVE_FROM | TaxRtScoDefaultFlgEffectiveFrom | — |
| DEFAULT_FLG_EFFECTIVE_TO | TaxRtScoDefaultFlgEffectiveTo | — |
| DEFAULT_RATE_FLAG | TaxRtScoDefaultRateFlag | — |
| DEFAULT_REC_RATE_CODE | TaxRtScoDefaultRecRateCode | — |
| DEFAULT_REC_TYPE_CODE | TaxRtScoDefaultRecTypeCode | — |
| DESCRIPTION | TaxRtScoDescription | — |
| EFFECTIVE_FROM | TaxRtScoEffectiveFrom | — |
| EFFECTIVE_TO | TaxRtScoEffectiveTo | — |
| INCLUSIVE_TAX_FLAG | TaxRtScoInclusiveTaxFlag | — |
| OBJECT_VERSION_NUMBER | TaxRtScoObjectVersionNumber | — |
| OFFSET_STATUS_CODE | TaxRtScoOffsetStatusCode | — |
| OFFSET_TAX | TaxRtScoOffsetTax | — |
| OFFSET_TAX_RATE_CODE | TaxRtScoOffsetTaxRateCode | — |
| PERCENTAGE_RATE | TaxRtScoPercentageRate | — |
| PROGRAM_APP_NAME | TaxRtScoProgramAppName | — |
| PROGRAM_NAME | TaxRtScoProgramName | — |
| QUANTITY_RATE | TaxRtScoQuantityRate | — |
| RATE_TYPE_CODE | TaxRtScoRateTypeCode | — |
| RECORD_TYPE_CODE | TaxRtScoRecordTypeCode | — |
| RECOVERY_RULE_CODE | TaxRtScoRecoveryRuleCode | — |
| RECOVERY_TYPE_CODE | TaxRtScoRecoveryTypeCode | — |
| SCHEDULE_BASED_RATE_FLAG | TaxRtScoScheduleBasedRateFlag | — |
| SDEFF_FROM | TaxRtScoSdeffFrom | — |
| SDEFF_TO | TaxRtScoSdeffTo | — |
| TAX | TaxRtScoTax | — |
| TAX_CLASS | TaxRtScoTaxClass | — |
| TAX_INCLUSIVE_OVERRIDE_FLAG | TaxRtScoTaxInclusiveOverrideFlag | — |
| TAX_JURISDICTION_CODE | TaxRtScoTaxJurisdictionCode | — |
| TAX_RATE_CODE | TaxRtScoTaxRateCode | — |
| TAX_RATE_ID | TaxRtScoTaxRateId | — |
| TAX_RATE_NAME | TaxRtScoTaxRateName | ✅ |
| TAX_REGIME_CODE | TaxRtScoTaxRegimeCode | — |
| TAX_STATUS_CODE | TaxRtScoTaxStatusCode | — |
| TAXABLE_BASIS_FORMULA_CODE | TaxRtScoTaxableBasisFormulaCode | — |
| UOM_CODE | TaxRtScoUomCode | — |
| VAT_TRANSACTION_TYPE_CODE | TaxRtScoVatTransactionTypeCode | — |

### [[receiptapplicationpvo|ReceiptApplicationPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | TaxRtScoActiveFlag | — |
| ADJ_FOR_ADHOC_AMT_CODE | TaxRtScoAdjForAdhocAmtCode | — |
| ALLOW_ADHOC_TAX_RATE_FLAG | TaxRtScoAllowAdhocTaxRateFlag | — |
| ALLOW_EXCEPTIONS_FLAG | TaxRtScoAllowExceptionsFlag | — |
| ALLOW_EXEMPTIONS_FLAG | TaxRtScoAllowExemptionsFlag | — |
| DEF_REC_SETTLEMENT_OPTION_CODE | TaxRtScoDefRecSettlementOptionCode | — |
| DEFAULT_FLG_EFFECTIVE_FROM | TaxRtScoDefaultFlgEffectiveFrom | — |
| DEFAULT_FLG_EFFECTIVE_TO | TaxRtScoDefaultFlgEffectiveTo | — |
| DEFAULT_RATE_FLAG | TaxRtScoDefaultRateFlag | — |
| DEFAULT_REC_RATE_CODE | TaxRtScoDefaultRecRateCode | — |
| DEFAULT_REC_TYPE_CODE | TaxRtScoDefaultRecTypeCode | — |
| DESCRIPTION | TaxRtScoDescription | — |
| EFFECTIVE_FROM | TaxRtScoEffectiveFrom | — |
| EFFECTIVE_TO | TaxRtScoEffectiveTo | — |
| INCLUSIVE_TAX_FLAG | TaxRtScoInclusiveTaxFlag | — |
| OBJECT_VERSION_NUMBER | TaxRtScoObjectVersionNumber | — |
| OFFSET_STATUS_CODE | TaxRtScoOffsetStatusCode | — |
| OFFSET_TAX | TaxRtScoOffsetTax | — |
| OFFSET_TAX_RATE_CODE | TaxRtScoOffsetTaxRateCode | — |
| PERCENTAGE_RATE | TaxRtScoPercentageRate | — |
| PROGRAM_APP_NAME | TaxRtScoProgramAppName | — |
| PROGRAM_NAME | TaxRtScoProgramName | — |
| QUANTITY_RATE | TaxRtScoQuantityRate | — |
| RATE_TYPE_CODE | TaxRtScoRateTypeCode | — |
| RECORD_TYPE_CODE | TaxRtScoRecordTypeCode | — |
| RECOVERY_RULE_CODE | TaxRtScoRecoveryRuleCode | — |
| RECOVERY_TYPE_CODE | TaxRtScoRecoveryTypeCode | — |
| SCHEDULE_BASED_RATE_FLAG | TaxRtScoScheduleBasedRateFlag | — |
| SDEFF_FROM | TaxRtScoSdeffFrom | — |
| SDEFF_TO | TaxRtScoSdeffTo | — |
| TAX | TaxRtScoTax | — |
| TAX_CLASS | TaxRtScoTaxClass | — |
| TAX_INCLUSIVE_OVERRIDE_FLAG | TaxRtScoTaxInclusiveOverrideFlag | — |
| TAX_JURISDICTION_CODE | TaxRtScoTaxJurisdictionCode | — |
| TAX_RATE_CODE | TaxRtScoTaxRateCode | — |
| TAX_RATE_ID | TaxRtScoTaxRateId | — |
| TAX_RATE_NAME | TaxRtScoTaxRateName | — |
| TAX_REGIME_CODE | TaxRtScoTaxRegimeCode | — |
| TAX_STATUS_CODE | TaxRtScoTaxStatusCode | — |
| TAXABLE_BASIS_FORMULA_CODE | TaxRtScoTaxableBasisFormulaCode | — |
| UOM_CODE | TaxRtScoUomCode | — |
| VAT_TRANSACTION_TYPE_CODE | TaxRtScoVatTransactionTypeCode | — |

### [[receiptheaderpvo|ReceiptHeaderPVO]] (AR · BICC: 1/42)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | TaxRtScoActiveFlag | — |
| ADJ_FOR_ADHOC_AMT_CODE | TaxRtScoAdjForAdhocAmtCode | — |
| ALLOW_ADHOC_TAX_RATE_FLAG | TaxRtScoAllowAdhocTaxRateFlag | — |
| ALLOW_EXCEPTIONS_FLAG | TaxRtScoAllowExceptionsFlag | — |
| ALLOW_EXEMPTIONS_FLAG | TaxRtScoAllowExemptionsFlag | — |
| DEF_REC_SETTLEMENT_OPTION_CODE | TaxRtScoDefRecSettlementOptionCode | — |
| DEFAULT_FLG_EFFECTIVE_FROM | TaxRtScoDefaultFlgEffectiveFrom | — |
| DEFAULT_FLG_EFFECTIVE_TO | TaxRtScoDefaultFlgEffectiveTo | — |
| DEFAULT_RATE_FLAG | TaxRtScoDefaultRateFlag | — |
| DEFAULT_REC_RATE_CODE | TaxRtScoDefaultRecRateCode | — |
| DEFAULT_REC_TYPE_CODE | TaxRtScoDefaultRecTypeCode | — |
| DESCRIPTION | TaxRtScoDescription | — |
| EFFECTIVE_FROM | TaxRtScoEffectiveFrom | — |
| EFFECTIVE_TO | TaxRtScoEffectiveTo | — |
| INCLUSIVE_TAX_FLAG | TaxRtScoInclusiveTaxFlag | — |
| OBJECT_VERSION_NUMBER | TaxRtScoObjectVersionNumber | — |
| OFFSET_STATUS_CODE | TaxRtScoOffsetStatusCode | — |
| OFFSET_TAX | TaxRtScoOffsetTax | — |
| OFFSET_TAX_RATE_CODE | TaxRtScoOffsetTaxRateCode | — |
| PERCENTAGE_RATE | TaxRtScoPercentageRate | — |
| PROGRAM_APP_NAME | TaxRtScoProgramAppName | — |
| PROGRAM_NAME | TaxRtScoProgramName | — |
| QUANTITY_RATE | TaxRtScoQuantityRate | — |
| RATE_TYPE_CODE | TaxRtScoRateTypeCode | — |
| RECORD_TYPE_CODE | TaxRtScoRecordTypeCode | — |
| RECOVERY_RULE_CODE | TaxRtScoRecoveryRuleCode | — |
| RECOVERY_TYPE_CODE | TaxRtScoRecoveryTypeCode | — |
| SCHEDULE_BASED_RATE_FLAG | TaxRtScoScheduleBasedRateFlag | — |
| SDEFF_FROM | TaxRtScoSdeffFrom | — |
| SDEFF_TO | TaxRtScoSdeffTo | — |
| TAX | TaxRtScoTax | — |
| TAX_CLASS | TaxRtScoTaxClass | — |
| TAX_INCLUSIVE_OVERRIDE_FLAG | TaxRtScoTaxInclusiveOverrideFlag | — |
| TAX_JURISDICTION_CODE | TaxRtScoTaxJurisdictionCode | — |
| TAX_RATE_CODE | TaxRtScoTaxRateCode | — |
| TAX_RATE_ID | TaxRtScoTaxRateId | — |
| TAX_RATE_NAME | TaxRtScoTaxRateName | ✅ |
| TAX_REGIME_CODE | TaxRtScoTaxRegimeCode | — |
| TAX_STATUS_CODE | TaxRtScoTaxStatusCode | — |
| TAXABLE_BASIS_FORMULA_CODE | TaxRtScoTaxableBasisFormulaCode | — |
| UOM_CODE | TaxRtScoUomCode | — |
| VAT_TRANSACTION_TYPE_CODE | TaxRtScoVatTransactionTypeCode | — |
