---
id: DOC-OTHER-PVO-SummaryTaxLineExtractPVO
doc_type: system-doc
title: "SummaryTaxLineExtractPVO — PVO Cross-Module"
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
  - SummaryTaxLineExtractPVO
  - summarytaxlineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SummaryTaxLineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Summary Tax Line Extract. Acessa as tabelas: ZX_LINES_SUMMARY.

**Caminho:** `FscmTopModelAM.FinExtractAM.ZxBiccExtractAM.SummaryTaxLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 157 | 1 | 1 | 110 | 70% |

---

## 🔗 Tabelas Relacionadas

- [[zx_lines_summary|ZX_LINES_SUMMARY]] — 157 atributos (1 PKs, 110 BICC)

---

## ⚙️ Atributos

### [[zx_lines_summary|ZX_LINES_SUMMARY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SummaryTaxLineAdjDocHdrTrxUserKey1 | ADJ_DOC_HDR_TRX_USER_KEY1 | — | ✅ |
| 2 | SummaryTaxLineAdjDocHdrTrxUserKey2 | ADJ_DOC_HDR_TRX_USER_KEY2 | — | ✅ |
| 3 | SummaryTaxLineAdjDocHdrTrxUserKey3 | ADJ_DOC_HDR_TRX_USER_KEY3 | — | ✅ |
| 4 | SummaryTaxLineAdjDocHdrTrxUserKey4 | ADJ_DOC_HDR_TRX_USER_KEY4 | — | ✅ |
| 5 | SummaryTaxLineAdjDocHdrTrxUserKey5 | ADJ_DOC_HDR_TRX_USER_KEY5 | — | ✅ |
| 6 | SummaryTaxLineAdjDocHdrTrxUserKey6 | ADJ_DOC_HDR_TRX_USER_KEY6 | — | ✅ |
| 7 | SummaryTaxLineAdjustTaxAmtFlag | ADJUST_TAX_AMT_FLAG | — | ✅ |
| 8 | SummaryTaxLineAdjustedDocApplicationId | ADJUSTED_DOC_APPLICATION_ID | — | ✅ |
| 9 | SummaryTaxLineAdjustedDocEntityCode | ADJUSTED_DOC_ENTITY_CODE | — | ✅ |
| 10 | SummaryTaxLineAdjustedDocEventClassCode | ADJUSTED_DOC_EVENT_CLASS_CODE | — | ✅ |
| 11 | SummaryTaxLineAdjustedDocTrxId | ADJUSTED_DOC_TRX_ID | — | ✅ |
| 12 | SummaryTaxLineAdjustedDocTrxLevelType | ADJUSTED_DOC_TRX_LEVEL_TYPE | — | ✅ |
| 13 | SummaryTaxLineAppFromLinTrxUserKey1 | APP_FROM_LIN_TRX_USER_KEY1 | — | ✅ |
| 14 | SummaryTaxLineAppFromLinTrxUserKey2 | APP_FROM_LIN_TRX_USER_KEY2 | — | ✅ |
| 15 | SummaryTaxLineAppFromLinTrxUserKey3 | APP_FROM_LIN_TRX_USER_KEY3 | — | ✅ |
| 16 | SummaryTaxLineAppFromLinTrxUserKey4 | APP_FROM_LIN_TRX_USER_KEY4 | — | ✅ |
| 17 | SummaryTaxLineAppFromLinTrxUserKey5 | APP_FROM_LIN_TRX_USER_KEY5 | — | ✅ |
| 18 | SummaryTaxLineAppFromLinTrxUserKey6 | APP_FROM_LIN_TRX_USER_KEY6 | — | ✅ |
| 19 | SummaryTaxLineAppToHdrTrxUserKey1 | APP_TO_HDR_TRX_USER_KEY1 | — | ✅ |
| 20 | SummaryTaxLineAppToHdrTrxUserKey2 | APP_TO_HDR_TRX_USER_KEY2 | — | ✅ |
| 21 | SummaryTaxLineAppToHdrTrxUserKey3 | APP_TO_HDR_TRX_USER_KEY3 | — | ✅ |
| 22 | SummaryTaxLineAppToHdrTrxUserKey4 | APP_TO_HDR_TRX_USER_KEY4 | — | ✅ |
| 23 | SummaryTaxLineAppToHdrTrxUserKey5 | APP_TO_HDR_TRX_USER_KEY5 | — | ✅ |
| 24 | SummaryTaxLineAppToHdrTrxUserKey6 | APP_TO_HDR_TRX_USER_KEY6 | — | ✅ |
| 25 | SummaryTaxLineAppToLinTrxUserKey1 | APP_TO_LIN_TRX_USER_KEY1 | — | ✅ |
| 26 | SummaryTaxLineAppToLinTrxUserKey2 | APP_TO_LIN_TRX_USER_KEY2 | — | ✅ |
| 27 | SummaryTaxLineAppToLinTrxUserKey3 | APP_TO_LIN_TRX_USER_KEY3 | — | ✅ |
| 28 | SummaryTaxLineAppToLinTrxUserKey4 | APP_TO_LIN_TRX_USER_KEY4 | — | ✅ |
| 29 | SummaryTaxLineAppToLinTrxUserKey5 | APP_TO_LIN_TRX_USER_KEY5 | — | ✅ |
| 30 | SummaryTaxLineAppToLinTrxUserKey6 | APP_TO_LIN_TRX_USER_KEY6 | — | ✅ |
| 31 | SummaryTaxLineApplicationId | APPLICATION_ID | — | ✅ |
| 32 | SummaryTaxLineAppliedFromApplicationId | APPLIED_FROM_APPLICATION_ID | — | ✅ |
| 33 | SummaryTaxLineAppliedFromEntityCode | APPLIED_FROM_ENTITY_CODE | — | ✅ |
| 34 | SummaryTaxLineAppliedFromEventClassCode | APPLIED_FROM_EVENT_CLASS_CODE | — | ✅ |
| 35 | SummaryTaxLineAppliedFromLineId | APPLIED_FROM_LINE_ID | — | ✅ |
| 36 | SummaryTaxLineAppliedFromTrxId | APPLIED_FROM_TRX_ID | — | ✅ |
| 37 | SummaryTaxLineAppliedFromTrxLevelType | APPLIED_FROM_TRX_LEVEL_TYPE | — | ✅ |
| 38 | SummaryTaxLineAppliedToApplicationId | APPLIED_TO_APPLICATION_ID | — | ✅ |
| 39 | SummaryTaxLineAppliedToEntityCode | APPLIED_TO_ENTITY_CODE | — | ✅ |
| 40 | SummaryTaxLineAppliedToEventClassCode | APPLIED_TO_EVENT_CLASS_CODE | — | ✅ |
| 41 | SummaryTaxLineAppliedToLineId | APPLIED_TO_LINE_ID | — | ✅ |
| 42 | SummaryTaxLineAppliedToTrxId | APPLIED_TO_TRX_ID | — | ✅ |
| 43 | SummaryTaxLineAppliedToTrxLevelType | APPLIED_TO_TRX_LEVEL_TYPE | — | ✅ |
| 44 | SummaryTaxLineAssociatedChildFrozenFlag | ASSOCIATED_CHILD_FROZEN_FLAG | — | ✅ |
| 45 | SummaryTaxLineAttribute1 | ATTRIBUTE1 | — | — |
| 46 | SummaryTaxLineAttribute10 | ATTRIBUTE10 | — | — |
| 47 | SummaryTaxLineAttribute11 | ATTRIBUTE11 | — | — |
| 48 | SummaryTaxLineAttribute12 | ATTRIBUTE12 | — | — |
| 49 | SummaryTaxLineAttribute13 | ATTRIBUTE13 | — | — |
| 50 | SummaryTaxLineAttribute14 | ATTRIBUTE14 | — | — |
| 51 | SummaryTaxLineAttribute15 | ATTRIBUTE15 | — | — |
| 52 | SummaryTaxLineAttribute2 | ATTRIBUTE2 | — | — |
| 53 | SummaryTaxLineAttribute3 | ATTRIBUTE3 | — | — |
| 54 | SummaryTaxLineAttribute4 | ATTRIBUTE4 | — | — |
| 55 | SummaryTaxLineAttribute5 | ATTRIBUTE5 | — | — |
| 56 | SummaryTaxLineAttribute6 | ATTRIBUTE6 | — | — |
| 57 | SummaryTaxLineAttribute7 | ATTRIBUTE7 | — | — |
| 58 | SummaryTaxLineAttribute8 | ATTRIBUTE8 | — | — |
| 59 | SummaryTaxLineAttribute9 | ATTRIBUTE9 | — | — |
| 60 | SummaryTaxLineAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 61 | SummaryTaxLineAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 62 | SummaryTaxLineAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 63 | SummaryTaxLineAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 64 | SummaryTaxLineAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 65 | SummaryTaxLineAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 66 | SummaryTaxLineAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 67 | SummaryTaxLineAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 68 | SummaryTaxLineAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 69 | SummaryTaxLineAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 70 | SummaryTaxLineAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 71 | SummaryTaxLineCancelFlag | CANCEL_FLAG | — | ✅ |
| 72 | SummaryTaxLineCompoundingTaxFlag | COMPOUNDING_TAX_FLAG | — | ✅ |
| 73 | SummaryTaxLineContentOwnerId | CONTENT_OWNER_ID | — | ✅ |
| 74 | SummaryTaxLineCopiedFromOtherDocFlag | COPIED_FROM_OTHER_DOC_FLAG | — | ✅ |
| 75 | SummaryTaxLineCreatedBy | CREATED_BY | — | ✅ |
| 76 | SummaryTaxLineCreationDate | CREATION_DATE | — | ✅ |
| 77 | SummaryTaxLineCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 78 | SummaryTaxLineCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 79 | SummaryTaxLineCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 80 | SummaryTaxLineDeleteFlag | DELETE_FLAG | — | ✅ |
| 81 | SummaryTaxLineEntityCode | ENTITY_CODE | — | ✅ |
| 82 | SummaryTaxLineEstablishmentId | ESTABLISHMENT_ID | — | ✅ |
| 83 | SummaryTaxLineEventClassCode | EVENT_CLASS_CODE | — | ✅ |
| 84 | SummaryTaxLineExceptionRate | EXCEPTION_RATE | — | ✅ |
| 85 | SummaryTaxLineExemptCertificateNumber | EXEMPT_CERTIFICATE_NUMBER | — | ✅ |
| 86 | SummaryTaxLineExemptRateModifier | EXEMPT_RATE_MODIFIER | — | ✅ |
| 87 | SummaryTaxLineExemptReason | EXEMPT_REASON | — | ✅ |
| 88 | SummaryTaxLineExemptReasonCode | EXEMPT_REASON_CODE | — | ✅ |
| 89 | SummaryTaxLineGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 90 | SummaryTaxLineGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 91 | SummaryTaxLineGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 92 | SummaryTaxLineGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 93 | SummaryTaxLineGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 94 | SummaryTaxLineGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 95 | SummaryTaxLineGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 96 | SummaryTaxLineGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 97 | SummaryTaxLineGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 98 | SummaryTaxLineGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 99 | SummaryTaxLineGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 100 | SummaryTaxLineGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 101 | SummaryTaxLineGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 102 | SummaryTaxLineGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 103 | SummaryTaxLineGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 104 | SummaryTaxLineGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 105 | SummaryTaxLineGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 106 | SummaryTaxLineGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 107 | SummaryTaxLineGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 108 | SummaryTaxLineGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 109 | SummaryTaxLineGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 110 | SummaryTaxLineHistoricalFlag | HISTORICAL_FLAG | — | ✅ |
| 111 | SummaryTaxLineInternalOrganizationId | INTERNAL_ORGANIZATION_ID | — | ✅ |
| 112 | SummaryTaxLineLastManualEntry | LAST_MANUAL_ENTRY | — | ✅ |
| 113 | SummaryTaxLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 114 | SummaryTaxLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 115 | SummaryTaxLineLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 116 | SummaryTaxLineLedgerId | LEDGER_ID | — | ✅ |
| 117 | SummaryTaxLineLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 118 | SummaryTaxLineManuallyEnteredFlag | MANUALLY_ENTERED_FLAG | — | ✅ |
| 119 | SummaryTaxLineMrcTaxLineFlag | MRC_TAX_LINE_FLAG | — | ✅ |
| 120 | SummaryTaxLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 121 | SummaryTaxLineOverriddenFlag | OVERRIDDEN_FLAG | — | ✅ |
| 122 | SummaryTaxLineRecordTypeCode | RECORD_TYPE_CODE | — | ✅ |
| 123 | SummaryTaxLineReportingOnlyFlag | REPORTING_ONLY_FLAG | — | ✅ |
| 124 | SummaryTaxLineSelfAssessedFlag | SELF_ASSESSED_FLAG | — | ✅ |
| 125 | SummaryTaxLineSummarizationTemplateId | SUMMARIZATION_TEMPLATE_ID | — | ✅ |
| 126 | SummaryTaxLineSummaryTaxLineId | SUMMARY_TAX_LINE_ID | 🔑 | ✅ |
| 127 | SummaryTaxLineSummaryTaxLineNumber | SUMMARY_TAX_LINE_NUMBER | — | ✅ |
| 128 | SummaryTaxLineTax | TAX | — | ✅ |
| 129 | SummaryTaxLineTaxAmt | TAX_AMT | — | ✅ |
| 130 | SummaryTaxLineTaxAmtFunclCurr | TAX_AMT_FUNCL_CURR | — | ✅ |
| 131 | SummaryTaxLineTaxAmtIncludedFlag | TAX_AMT_INCLUDED_FLAG | — | ✅ |
| 132 | SummaryTaxLineTaxAmtTaxCurr | TAX_AMT_TAX_CURR | — | ✅ |
| 133 | SummaryTaxLineTaxCalculationFormula | TAX_CALCULATION_FORMULA | — | ✅ |
| 134 | SummaryTaxLineTaxExceptionId | TAX_EXCEPTION_ID | — | ✅ |
| 135 | SummaryTaxLineTaxExemptionId | TAX_EXEMPTION_ID | — | ✅ |
| 136 | SummaryTaxLineTaxJurisdictionCode | TAX_JURISDICTION_CODE | — | ✅ |
| 137 | SummaryTaxLineTaxOnlyLineFlag | TAX_ONLY_LINE_FLAG | — | ✅ |
| 138 | SummaryTaxLineTaxProviderId | TAX_PROVIDER_ID | — | ✅ |
| 139 | SummaryTaxLineTaxRate | TAX_RATE | — | ✅ |
| 140 | SummaryTaxLineTaxRateBeforeException | TAX_RATE_BEFORE_EXCEPTION | — | ✅ |
| 141 | SummaryTaxLineTaxRateBeforeExemption | TAX_RATE_BEFORE_EXEMPTION | — | ✅ |
| 142 | SummaryTaxLineTaxRateCode | TAX_RATE_CODE | — | ✅ |
| 143 | SummaryTaxLineTaxRateId | TAX_RATE_ID | — | ✅ |
| 144 | SummaryTaxLineTaxRateNameBeforeException | TAX_RATE_NAME_BEFORE_EXCEPTION | — | ✅ |
| 145 | SummaryTaxLineTaxRateNameBeforeExemption | TAX_RATE_NAME_BEFORE_EXEMPTION | — | ✅ |
| 146 | SummaryTaxLineTaxRegimeCode | TAX_REGIME_CODE | — | ✅ |
| 147 | SummaryTaxLineTaxStatusCode | TAX_STATUS_CODE | — | ✅ |
| 148 | SummaryTaxLineTaxableBasisFormula | TAXABLE_BASIS_FORMULA | — | ✅ |
| 149 | SummaryTaxLineTotalNrecTaxAmt | TOTAL_NREC_TAX_AMT | — | ✅ |
| 150 | SummaryTaxLineTotalNrecTaxAmtFunclCurr | TOTAL_NREC_TAX_AMT_FUNCL_CURR | — | ✅ |
| 151 | SummaryTaxLineTotalNrecTaxAmtTaxCurr | TOTAL_NREC_TAX_AMT_TAX_CURR | — | ✅ |
| 152 | SummaryTaxLineTotalRecTaxAmt | TOTAL_REC_TAX_AMT | — | ✅ |
| 153 | SummaryTaxLineTotalRecTaxAmtFunclCurr | TOTAL_REC_TAX_AMT_FUNCL_CURR | — | ✅ |
| 154 | SummaryTaxLineTotalRecTaxAmtTaxCurr | TOTAL_REC_TAX_AMT_TAX_CURR | — | ✅ |
| 155 | SummaryTaxLineTrxId | TRX_ID | — | ✅ |
| 156 | SummaryTaxLineTrxLevelType | TRX_LEVEL_TYPE | — | ✅ |
| 157 | SummaryTaxLineTrxNumber | TRX_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
