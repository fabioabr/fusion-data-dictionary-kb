---
id: DOC-OTHER-PVO-WithholdingDetailTaxLineExtractPVO
doc_type: system-doc
title: "WithholdingDetailTaxLineExtractPVO — PVO Cross-Module"
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
  - WithholdingDetailTaxLineExtractPVO
  - withholdingdetailtaxlineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WithholdingDetailTaxLineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Withholding Detail Tax Line Extract. Acessa as tabelas: ZX_WITHHOLDING_LINES.

**Caminho:** `FscmTopModelAM.FinExtractAM.ZxBiccExtractAM.WithholdingDetailTaxLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 274 | 1 | 1 | 217 | 79% |

---

## 🔗 Tabelas Relacionadas

- [[zx_withholding_lines|ZX_WITHHOLDING_LINES]] — 274 atributos (1 PKs, 217 BICC)

---

## ⚙️ Atributos

### [[zx_withholding_lines|ZX_WITHHOLDING_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WithholdingDetailTaxLineAdjustedDocTaxLineId | ADJUSTED_DOC_TAX_LINE_ID | — | ✅ |
| 2 | WithholdingDetailTaxLineApplicationId | APPLICATION_ID | — | ✅ |
| 3 | WithholdingDetailTaxLineAppliedFromApplicationId | APPLIED_FROM_APPLICATION_ID | — | ✅ |
| 4 | WithholdingDetailTaxLineAppliedFromEntityCode | APPLIED_FROM_ENTITY_CODE | — | ✅ |
| 5 | WithholdingDetailTaxLineAppliedFromEventClassCode | APPLIED_FROM_EVENT_CLASS_CODE | — | ✅ |
| 6 | WithholdingDetailTaxLineAppliedFromLineId | APPLIED_FROM_LINE_ID | — | ✅ |
| 7 | WithholdingDetailTaxLineAppliedFromTrxId | APPLIED_FROM_TRX_ID | — | ✅ |
| 8 | WithholdingDetailTaxLineAppliedFromTrxLevelType | APPLIED_FROM_TRX_LEVEL_TYPE | — | ✅ |
| 9 | WithholdingDetailTaxLineAppliedFromTrxNumber | APPLIED_FROM_TRX_NUMBER | — | ✅ |
| 10 | WithholdingDetailTaxLineAssociatedChildFrozenFlag | ASSOCIATED_CHILD_FROZEN_FLAG | — | ✅ |
| 11 | WithholdingDetailTaxLineAttribute1 | ATTRIBUTE1 | — | — |
| 12 | WithholdingDetailTaxLineAttribute10 | ATTRIBUTE10 | — | — |
| 13 | WithholdingDetailTaxLineAttribute11 | ATTRIBUTE11 | — | — |
| 14 | WithholdingDetailTaxLineAttribute12 | ATTRIBUTE12 | — | — |
| 15 | WithholdingDetailTaxLineAttribute13 | ATTRIBUTE13 | — | — |
| 16 | WithholdingDetailTaxLineAttribute14 | ATTRIBUTE14 | — | — |
| 17 | WithholdingDetailTaxLineAttribute15 | ATTRIBUTE15 | — | — |
| 18 | WithholdingDetailTaxLineAttribute2 | ATTRIBUTE2 | — | — |
| 19 | WithholdingDetailTaxLineAttribute3 | ATTRIBUTE3 | — | — |
| 20 | WithholdingDetailTaxLineAttribute4 | ATTRIBUTE4 | — | — |
| 21 | WithholdingDetailTaxLineAttribute5 | ATTRIBUTE5 | — | — |
| 22 | WithholdingDetailTaxLineAttribute6 | ATTRIBUTE6 | — | — |
| 23 | WithholdingDetailTaxLineAttribute7 | ATTRIBUTE7 | — | — |
| 24 | WithholdingDetailTaxLineAttribute8 | ATTRIBUTE8 | — | — |
| 25 | WithholdingDetailTaxLineAttribute9 | ATTRIBUTE9 | — | — |
| 26 | WithholdingDetailTaxLineAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 27 | WithholdingDetailTaxLineAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 28 | WithholdingDetailTaxLineAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 29 | WithholdingDetailTaxLineAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 30 | WithholdingDetailTaxLineAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 31 | WithholdingDetailTaxLineAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 32 | WithholdingDetailTaxLineAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 33 | WithholdingDetailTaxLineAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 34 | WithholdingDetailTaxLineAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 35 | WithholdingDetailTaxLineAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 36 | WithholdingDetailTaxLineAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 37 | WithholdingDetailTaxLineBasisResultId | BASIS_RESULT_ID | — | ✅ |
| 38 | WithholdingDetailTaxLineCalTaxAmt | CAL_TAX_AMT | — | ✅ |
| 39 | WithholdingDetailTaxLineCalTaxAmtFunclCurr | CAL_TAX_AMT_FUNCL_CURR | — | ✅ |
| 40 | WithholdingDetailTaxLineCalTaxAmtTaxCurr | CAL_TAX_AMT_TAX_CURR | — | ✅ |
| 41 | WithholdingDetailTaxLineCalTaxableAmt | CAL_TAXABLE_AMT | — | ✅ |
| 42 | WithholdingDetailTaxLineCalcResultId | CALC_RESULT_ID | — | ✅ |
| 43 | WithholdingDetailTaxLineCancelFlag | CANCEL_FLAG | — | ✅ |
| 44 | WithholdingDetailTaxLineCashDiscountApplicableFlag | CASH_DISCOUNT_APPLICABLE_FLAG | — | ✅ |
| 45 | WithholdingDetailTaxLineChar1 | CHAR1 | — | ✅ |
| 46 | WithholdingDetailTaxLineChar10 | CHAR10 | — | ✅ |
| 47 | WithholdingDetailTaxLineChar2 | CHAR2 | — | ✅ |
| 48 | WithholdingDetailTaxLineChar3 | CHAR3 | — | ✅ |
| 49 | WithholdingDetailTaxLineChar4 | CHAR4 | — | ✅ |
| 50 | WithholdingDetailTaxLineChar5 | CHAR5 | — | ✅ |
| 51 | WithholdingDetailTaxLineChar6 | CHAR6 | — | ✅ |
| 52 | WithholdingDetailTaxLineChar7 | CHAR7 | — | ✅ |
| 53 | WithholdingDetailTaxLineChar8 | CHAR8 | — | ✅ |
| 54 | WithholdingDetailTaxLineChar9 | CHAR9 | — | ✅ |
| 55 | WithholdingDetailTaxLineCheckrunId | CHECKRUN_ID | — | ✅ |
| 56 | WithholdingDetailTaxLineCompoundingDepTaxFlag | COMPOUNDING_DEP_TAX_FLAG | — | ✅ |
| 57 | WithholdingDetailTaxLineCompoundingTaxFlag | COMPOUNDING_TAX_FLAG | — | ✅ |
| 58 | WithholdingDetailTaxLineCompoundingTaxMissFlag | COMPOUNDING_TAX_MISS_FLAG | — | ✅ |
| 59 | WithholdingDetailTaxLineContentOwnerId | CONTENT_OWNER_ID | — | ✅ |
| 60 | WithholdingDetailTaxLineCopiedFromOtherDocFlag | COPIED_FROM_OTHER_DOC_FLAG | — | ✅ |
| 61 | WithholdingDetailTaxLineCreatedBy | CREATED_BY | — | ✅ |
| 62 | WithholdingDetailTaxLineCreationDate | CREATION_DATE | — | ✅ |
| 63 | WithholdingDetailTaxLineCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 64 | WithholdingDetailTaxLineCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 65 | WithholdingDetailTaxLineCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 66 | WithholdingDetailTaxLineDate1 | DATE1 | — | ✅ |
| 67 | WithholdingDetailTaxLineDate10 | DATE10 | — | ✅ |
| 68 | WithholdingDetailTaxLineDate2 | DATE2 | — | ✅ |
| 69 | WithholdingDetailTaxLineDate3 | DATE3 | — | ✅ |
| 70 | WithholdingDetailTaxLineDate4 | DATE4 | — | ✅ |
| 71 | WithholdingDetailTaxLineDate5 | DATE5 | — | ✅ |
| 72 | WithholdingDetailTaxLineDate6 | DATE6 | — | ✅ |
| 73 | WithholdingDetailTaxLineDate7 | DATE7 | — | ✅ |
| 74 | WithholdingDetailTaxLineDate8 | DATE8 | — | ✅ |
| 75 | WithholdingDetailTaxLineDate9 | DATE9 | — | ✅ |
| 76 | WithholdingDetailTaxLineDeleteFlag | DELETE_FLAG | — | ✅ |
| 77 | WithholdingDetailTaxLineDirectRateResultId | DIRECT_RATE_RESULT_ID | — | ✅ |
| 78 | WithholdingDetailTaxLineDiscountAmt | DISCOUNT_AMT | — | ✅ |
| 79 | WithholdingDetailTaxLineDocEventStatus | DOC_EVENT_STATUS | — | ✅ |
| 80 | WithholdingDetailTaxLineEnforceFromNaturalAcctFlag | ENFORCE_FROM_NATURAL_ACCT_FLAG | — | ✅ |
| 81 | WithholdingDetailTaxLineEntityCode | ENTITY_CODE | — | ✅ |
| 82 | WithholdingDetailTaxLineEstablishmentId | ESTABLISHMENT_ID | — | ✅ |
| 83 | WithholdingDetailTaxLineEvalExmptResultId | EVAL_EXMPT_RESULT_ID | — | ✅ |
| 84 | WithholdingDetailTaxLineEventClassCode | EVENT_CLASS_CODE | — | ✅ |
| 85 | WithholdingDetailTaxLineEventTypeCode | EVENT_TYPE_CODE | — | ✅ |
| 86 | WithholdingDetailTaxLineExceptionRate | EXCEPTION_RATE | — | ✅ |
| 87 | WithholdingDetailTaxLineExemptCertificateNumber | EXEMPT_CERTIFICATE_NUMBER | — | ✅ |
| 88 | WithholdingDetailTaxLineExemptRateModifier | EXEMPT_RATE_MODIFIER | — | ✅ |
| 89 | WithholdingDetailTaxLineExemptReason | EXEMPT_REASON | — | ✅ |
| 90 | WithholdingDetailTaxLineExemptReasonCode | EXEMPT_REASON_CODE | — | ✅ |
| 91 | WithholdingDetailTaxLineGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 92 | WithholdingDetailTaxLineGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 93 | WithholdingDetailTaxLineGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 94 | WithholdingDetailTaxLineGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 95 | WithholdingDetailTaxLineGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 96 | WithholdingDetailTaxLineGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 97 | WithholdingDetailTaxLineGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 98 | WithholdingDetailTaxLineGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 99 | WithholdingDetailTaxLineGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 100 | WithholdingDetailTaxLineGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 101 | WithholdingDetailTaxLineGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 102 | WithholdingDetailTaxLineGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 103 | WithholdingDetailTaxLineGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 104 | WithholdingDetailTaxLineGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 105 | WithholdingDetailTaxLineGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 106 | WithholdingDetailTaxLineGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 107 | WithholdingDetailTaxLineGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 108 | WithholdingDetailTaxLineGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 109 | WithholdingDetailTaxLineGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 110 | WithholdingDetailTaxLineGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 111 | WithholdingDetailTaxLineGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 112 | WithholdingDetailTaxLineGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 113 | WithholdingDetailTaxLineGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 114 | WithholdingDetailTaxLineGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 115 | WithholdingDetailTaxLineGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 116 | WithholdingDetailTaxLineGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 117 | WithholdingDetailTaxLineGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 118 | WithholdingDetailTaxLineGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 119 | WithholdingDetailTaxLineGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 120 | WithholdingDetailTaxLineGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 121 | WithholdingDetailTaxLineGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 122 | WithholdingDetailTaxLineHistoricalFlag | HISTORICAL_FLAG | — | ✅ |
| 123 | WithholdingDetailTaxLineHqEstbPartyTaxProfId | HQ_ESTB_PARTY_TAX_PROF_ID | — | ✅ |
| 124 | WithholdingDetailTaxLineHqEstbRegNumber | HQ_ESTB_REG_NUMBER | — | ✅ |
| 125 | WithholdingDetailTaxLineIndirectTaxLineId | INDIRECT_TAX_LINE_ID | — | ✅ |
| 126 | WithholdingDetailTaxLineInternalOrgLocationId | INTERNAL_ORG_LOCATION_ID | — | ✅ |
| 127 | WithholdingDetailTaxLineInternalOrganizationId | INTERNAL_ORGANIZATION_ID | — | ✅ |
| 128 | WithholdingDetailTaxLineLastManualEntry | LAST_MANUAL_ENTRY | — | ✅ |
| 129 | WithholdingDetailTaxLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 130 | WithholdingDetailTaxLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 131 | WithholdingDetailTaxLineLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 132 | WithholdingDetailTaxLineLedgerId | LEDGER_ID | — | ✅ |
| 133 | WithholdingDetailTaxLineLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 134 | WithholdingDetailTaxLineLegalEntityTaxRegNumber | LEGAL_ENTITY_TAX_REG_NUMBER | — | ✅ |
| 135 | WithholdingDetailTaxLineLegalMsgAppl2Id | LEGAL_MSG_APPL_2_ID | — | ✅ |
| 136 | WithholdingDetailTaxLineLegalMsgBasisId | LEGAL_MSG_BASIS_ID | — | ✅ |
| 137 | WithholdingDetailTaxLineLegalMsgCalcId | LEGAL_MSG_CALC_ID | — | ✅ |
| 138 | WithholdingDetailTaxLineLegalMsgExmptId | LEGAL_MSG_EXMPT_ID | — | ✅ |
| 139 | WithholdingDetailTaxLineLegalMsgPosId | LEGAL_MSG_POS_ID | — | ✅ |
| 140 | WithholdingDetailTaxLineLegalMsgRateId | LEGAL_MSG_RATE_ID | — | ✅ |
| 141 | WithholdingDetailTaxLineLegalMsgStatusId | LEGAL_MSG_STATUS_ID | — | ✅ |
| 142 | WithholdingDetailTaxLineLegalMsgThresholdId | LEGAL_MSG_THRESHOLD_ID | — | ✅ |
| 143 | WithholdingDetailTaxLineLegalMsgTrnId | LEGAL_MSG_TRN_ID | — | ✅ |
| 144 | WithholdingDetailTaxLineLineAmt | LINE_AMT | — | ✅ |
| 145 | WithholdingDetailTaxLineLineAssessableValue | LINE_ASSESSABLE_VALUE | — | ✅ |
| 146 | WithholdingDetailTaxLineManuallyEnteredFlag | MANUALLY_ENTERED_FLAG | — | ✅ |
| 147 | WithholdingDetailTaxLineMinimumAccountableUnit | MINIMUM_ACCOUNTABLE_UNIT | — | ✅ |
| 148 | WithholdingDetailTaxLineMultipleJurisdictionsFlag | MULTIPLE_JURISDICTIONS_FLAG | — | ✅ |
| 149 | WithholdingDetailTaxLineNumeric1 | NUMERIC1 | — | ✅ |
| 150 | WithholdingDetailTaxLineNumeric10 | NUMERIC10 | — | ✅ |
| 151 | WithholdingDetailTaxLineNumeric2 | NUMERIC2 | — | ✅ |
| 152 | WithholdingDetailTaxLineNumeric3 | NUMERIC3 | — | ✅ |
| 153 | WithholdingDetailTaxLineNumeric4 | NUMERIC4 | — | ✅ |
| 154 | WithholdingDetailTaxLineNumeric5 | NUMERIC5 | — | ✅ |
| 155 | WithholdingDetailTaxLineNumeric6 | NUMERIC6 | — | ✅ |
| 156 | WithholdingDetailTaxLineNumeric7 | NUMERIC7 | — | ✅ |
| 157 | WithholdingDetailTaxLineNumeric8 | NUMERIC8 | — | ✅ |
| 158 | WithholdingDetailTaxLineNumeric9 | NUMERIC9 | — | ✅ |
| 159 | WithholdingDetailTaxLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 160 | WithholdingDetailTaxLineOrigTaxAmt | ORIG_TAX_AMT | — | ✅ |
| 161 | WithholdingDetailTaxLineOrigTaxAmtTaxCurr | ORIG_TAX_AMT_TAX_CURR | — | ✅ |
| 162 | WithholdingDetailTaxLineOrigTaxJurisdictionCode | ORIG_TAX_JURISDICTION_CODE | — | ✅ |
| 163 | WithholdingDetailTaxLineOrigTaxJurisdictionId | ORIG_TAX_JURISDICTION_ID | — | ✅ |
| 164 | WithholdingDetailTaxLineOrigTaxRate | ORIG_TAX_RATE | — | ✅ |
| 165 | WithholdingDetailTaxLineOrigTaxRateCode | ORIG_TAX_RATE_CODE | — | ✅ |
| 166 | WithholdingDetailTaxLineOrigTaxRateId | ORIG_TAX_RATE_ID | — | ✅ |
| 167 | WithholdingDetailTaxLineOrigTaxStatusCode | ORIG_TAX_STATUS_CODE | — | ✅ |
| 168 | WithholdingDetailTaxLineOrigTaxStatusId | ORIG_TAX_STATUS_ID | — | ✅ |
| 169 | WithholdingDetailTaxLineOrigTaxableAmt | ORIG_TAXABLE_AMT | — | ✅ |
| 170 | WithholdingDetailTaxLineOrigTaxableAmtTaxCurr | ORIG_TAXABLE_AMT_TAX_CURR | — | ✅ |
| 171 | WithholdingDetailTaxLineOtherDocLineAmt | OTHER_DOC_LINE_AMT | — | ✅ |
| 172 | WithholdingDetailTaxLineOtherDocLineTaxAmt | OTHER_DOC_LINE_TAX_AMT | — | ✅ |
| 173 | WithholdingDetailTaxLineOtherDocLineTaxableAmt | OTHER_DOC_LINE_TAXABLE_AMT | — | ✅ |
| 174 | WithholdingDetailTaxLineOtherDocSource | OTHER_DOC_SOURCE | — | ✅ |
| 175 | WithholdingDetailTaxLineOverriddenFlag | OVERRIDDEN_FLAG | — | ✅ |
| 176 | WithholdingDetailTaxLinePaymentAmt | PAYMENT_AMT | — | ✅ |
| 177 | WithholdingDetailTaxLinePaymentDate | PAYMENT_DATE | — | ✅ |
| 178 | WithholdingDetailTaxLinePaymentId | PAYMENT_ID | — | ✅ |
| 179 | WithholdingDetailTaxLinePlaceOfSupplyResultId | PLACE_OF_SUPPLY_RESULT_ID | — | ✅ |
| 180 | WithholdingDetailTaxLinePlaceOfSupplyTypeCode | PLACE_OF_SUPPLY_TYPE_CODE | — | ✅ |
| 181 | WithholdingDetailTaxLinePrdTotalTaxAmt | PRD_TOTAL_TAX_AMT | — | ✅ |
| 182 | WithholdingDetailTaxLinePrdTotalTaxAmtFunclCurr | PRD_TOTAL_TAX_AMT_FUNCL_CURR | — | ✅ |
| 183 | WithholdingDetailTaxLinePrdTotalTaxAmtTaxCurr | PRD_TOTAL_TAX_AMT_TAX_CURR | — | ✅ |
| 184 | WithholdingDetailTaxLinePrecision | PRECISION | — | ✅ |
| 185 | WithholdingDetailTaxLinePurgeFlag | PURGE_FLAG | — | ✅ |
| 186 | WithholdingDetailTaxLineRateResultId | RATE_RESULT_ID | — | ✅ |
| 187 | WithholdingDetailTaxLineRecalcRequiredFlag | RECALC_REQUIRED_FLAG | — | ✅ |
| 188 | WithholdingDetailTaxLineRecordTypeCode | RECORD_TYPE_CODE | — | ✅ |
| 189 | WithholdingDetailTaxLineRegistrationPartyType | REGISTRATION_PARTY_TYPE | — | ✅ |
| 190 | WithholdingDetailTaxLineReportingPeriodId | REPORTING_PERIOD_ID | — | ✅ |
| 191 | WithholdingDetailTaxLineReversedTaxLineId | REVERSED_TAX_LINE_ID | — | ✅ |
| 192 | WithholdingDetailTaxLineRoundingLevelCode | ROUNDING_LEVEL_CODE | — | ✅ |
| 193 | WithholdingDetailTaxLineRoundingLvlPartyTaxProfId | ROUNDING_LVL_PARTY_TAX_PROF_ID | — | ✅ |
| 194 | WithholdingDetailTaxLineRoundingLvlPartyType | ROUNDING_LVL_PARTY_TYPE | — | ✅ |
| 195 | WithholdingDetailTaxLineRoundingRuleCode | ROUNDING_RULE_CODE | — | ✅ |
| 196 | WithholdingDetailTaxLineStatusResultId | STATUS_RESULT_ID | — | ✅ |
| 197 | WithholdingDetailTaxLineSummaryTaxLineId | SUMMARY_TAX_LINE_ID | — | ✅ |
| 198 | WithholdingDetailTaxLineTax | TAX | — | ✅ |
| 199 | WithholdingDetailTaxLineTaxAmt | TAX_AMT | — | ✅ |
| 200 | WithholdingDetailTaxLineTaxAmtFunclCurr | TAX_AMT_FUNCL_CURR | — | ✅ |
| 201 | WithholdingDetailTaxLineTaxAmtTaxCurr | TAX_AMT_TAX_CURR | — | ✅ |
| 202 | WithholdingDetailTaxLineTaxApplicabilityResultId | TAX_APPLICABILITY_RESULT_ID | — | ✅ |
| 203 | WithholdingDetailTaxLineTaxApportionmentFlag | TAX_APPORTIONMENT_FLAG | — | ✅ |
| 204 | WithholdingDetailTaxLineTaxApportionmentLineNumber | TAX_APPORTIONMENT_LINE_NUMBER | — | ✅ |
| 205 | WithholdingDetailTaxLineTaxBaseModifierRate | TAX_BASE_MODIFIER_RATE | — | ✅ |
| 206 | WithholdingDetailTaxLineTaxCalculationFormula | TAX_CALCULATION_FORMULA | — | ✅ |
| 207 | WithholdingDetailTaxLineTaxCode | TAX_CODE | — | ✅ |
| 208 | WithholdingDetailTaxLineTaxCurrencyCode | TAX_CURRENCY_CODE | — | ✅ |
| 209 | WithholdingDetailTaxLineTaxCurrencyConversionDate | TAX_CURRENCY_CONVERSION_DATE | — | ✅ |
| 210 | WithholdingDetailTaxLineTaxCurrencyConversionRate | TAX_CURRENCY_CONVERSION_RATE | — | ✅ |
| 211 | WithholdingDetailTaxLineTaxCurrencyConversionType | TAX_CURRENCY_CONVERSION_TYPE | — | ✅ |
| 212 | WithholdingDetailTaxLineTaxDate | TAX_DATE | — | ✅ |
| 213 | WithholdingDetailTaxLineTaxDateRuleId | TAX_DATE_RULE_ID | — | ✅ |
| 214 | WithholdingDetailTaxLineTaxDetermineDate | TAX_DETERMINE_DATE | — | ✅ |
| 215 | WithholdingDetailTaxLineTaxEventClassCode | TAX_EVENT_CLASS_CODE | — | ✅ |
| 216 | WithholdingDetailTaxLineTaxEventTypeCode | TAX_EVENT_TYPE_CODE | — | ✅ |
| 217 | WithholdingDetailTaxLineTaxExceptionId | TAX_EXCEPTION_ID | — | ✅ |
| 218 | WithholdingDetailTaxLineTaxExemptionId | TAX_EXEMPTION_ID | — | ✅ |
| 219 | WithholdingDetailTaxLineTaxId | TAX_ID | — | ✅ |
| 220 | WithholdingDetailTaxLineTaxJurisdictionCode | TAX_JURISDICTION_CODE | — | ✅ |
| 221 | WithholdingDetailTaxLineTaxJurisdictionId | TAX_JURISDICTION_ID | — | ✅ |
| 222 | WithholdingDetailTaxLineTaxLineId | TAX_LINE_ID | 🔑 | ✅ |
| 223 | WithholdingDetailTaxLineTaxLineNumber | TAX_LINE_NUMBER | — | ✅ |
| 224 | WithholdingDetailTaxLineTaxPointDate | TAX_POINT_DATE | — | ✅ |
| 225 | WithholdingDetailTaxLineTaxRate | TAX_RATE | — | ✅ |
| 226 | WithholdingDetailTaxLineTaxRateBeforeException | TAX_RATE_BEFORE_EXCEPTION | — | ✅ |
| 227 | WithholdingDetailTaxLineTaxRateBeforeExemption | TAX_RATE_BEFORE_EXEMPTION | — | ✅ |
| 228 | WithholdingDetailTaxLineTaxRateCode | TAX_RATE_CODE | — | ✅ |
| 229 | WithholdingDetailTaxLineTaxRateId | TAX_RATE_ID | — | ✅ |
| 230 | WithholdingDetailTaxLineTaxRateNameBeforeException | TAX_RATE_NAME_BEFORE_EXCEPTION | — | ✅ |
| 231 | WithholdingDetailTaxLineTaxRateNameBeforeExemption | TAX_RATE_NAME_BEFORE_EXEMPTION | — | ✅ |
| 232 | WithholdingDetailTaxLineTaxRateSchedId | TAX_RATE_SCHED_ID | — | ✅ |
| 233 | WithholdingDetailTaxLineTaxRateType | TAX_RATE_TYPE | — | ✅ |
| 234 | WithholdingDetailTaxLineTaxRegNumDetResultId | TAX_REG_NUM_DET_RESULT_ID | — | ✅ |
| 235 | WithholdingDetailTaxLineTaxRegimeCode | TAX_REGIME_CODE | — | ✅ |
| 236 | WithholdingDetailTaxLineTaxRegimeId | TAX_REGIME_ID | — | ✅ |
| 237 | WithholdingDetailTaxLineTaxRegimeTemplateId | TAX_REGIME_TEMPLATE_ID | — | ✅ |
| 238 | WithholdingDetailTaxLineTaxRegistrationId | TAX_REGISTRATION_ID | — | ✅ |
| 239 | WithholdingDetailTaxLineTaxRegistrationNumber | TAX_REGISTRATION_NUMBER | — | ✅ |
| 240 | WithholdingDetailTaxLineTaxStatusCode | TAX_STATUS_CODE | — | ✅ |
| 241 | WithholdingDetailTaxLineTaxStatusId | TAX_STATUS_ID | — | ✅ |
| 242 | WithholdingDetailTaxLineTaxThrehldsSchdlCntrlId | TAX_THREHLDS_SCHDL_CNTRL_ID | — | ✅ |
| 243 | WithholdingDetailTaxLineTaxTypeCode | TAX_TYPE_CODE | — | ✅ |
| 244 | WithholdingDetailTaxLineTaxableAmt | TAXABLE_AMT | — | ✅ |
| 245 | WithholdingDetailTaxLineTaxableAmtFunclCurr | TAXABLE_AMT_FUNCL_CURR | — | ✅ |
| 246 | WithholdingDetailTaxLineTaxableAmtTaxCurr | TAXABLE_AMT_TAX_CURR | — | ✅ |
| 247 | WithholdingDetailTaxLineTaxableBasisFormula | TAXABLE_BASIS_FORMULA | — | ✅ |
| 248 | WithholdingDetailTaxLineTaxingJurisGeographyId | TAXING_JURIS_GEOGRAPHY_ID | — | ✅ |
| 249 | WithholdingDetailTaxLineThreshResultId | THRESH_RESULT_ID | — | ✅ |
| 250 | WithholdingDetailTaxLineTrxCurrencyCode | TRX_CURRENCY_CODE | — | ✅ |
| 251 | WithholdingDetailTaxLineTrxDate | TRX_DATE | — | ✅ |
| 252 | WithholdingDetailTaxLineTrxId | TRX_ID | — | ✅ |
| 253 | WithholdingDetailTaxLineTrxIdLevel2 | TRX_ID_LEVEL2 | — | ✅ |
| 254 | WithholdingDetailTaxLineTrxIdLevel3 | TRX_ID_LEVEL3 | — | ✅ |
| 255 | WithholdingDetailTaxLineTrxIdLevel4 | TRX_ID_LEVEL4 | — | ✅ |
| 256 | WithholdingDetailTaxLineTrxIdLevel5 | TRX_ID_LEVEL5 | — | ✅ |
| 257 | WithholdingDetailTaxLineTrxIdLevel6 | TRX_ID_LEVEL6 | — | ✅ |
| 258 | WithholdingDetailTaxLineTrxLevelType | TRX_LEVEL_TYPE | — | ✅ |
| 259 | WithholdingDetailTaxLineTrxLineDate | TRX_LINE_DATE | — | ✅ |
| 260 | WithholdingDetailTaxLineTrxLineId | TRX_LINE_ID | — | ✅ |
| 261 | WithholdingDetailTaxLineTrxLineNumber | TRX_LINE_NUMBER | — | ✅ |
| 262 | WithholdingDetailTaxLineTrxLineQuantity | TRX_LINE_QUANTITY | — | ✅ |
| 263 | WithholdingDetailTaxLineTrxNumber | TRX_NUMBER | — | ✅ |
| 264 | WithholdingDetailTaxLineTrxUserKeyLevel1 | TRX_USER_KEY_LEVEL1 | — | ✅ |
| 265 | WithholdingDetailTaxLineTrxUserKeyLevel2 | TRX_USER_KEY_LEVEL2 | — | ✅ |
| 266 | WithholdingDetailTaxLineTrxUserKeyLevel3 | TRX_USER_KEY_LEVEL3 | — | ✅ |
| 267 | WithholdingDetailTaxLineTrxUserKeyLevel4 | TRX_USER_KEY_LEVEL4 | — | ✅ |
| 268 | WithholdingDetailTaxLineTrxUserKeyLevel5 | TRX_USER_KEY_LEVEL5 | — | ✅ |
| 269 | WithholdingDetailTaxLineTrxUserKeyLevel6 | TRX_USER_KEY_LEVEL6 | — | ✅ |
| 270 | WithholdingDetailTaxLineTxblThrshldGrpLvlCode | TXBL_THRSHLD_GRP_LVL_CODE | — | ✅ |
| 271 | WithholdingDetailTaxLineUnitPrice | UNIT_PRICE | — | ✅ |
| 272 | WithholdingDetailTaxLineUnroundedTaxAmt | UNROUNDED_TAX_AMT | — | ✅ |
| 273 | WithholdingDetailTaxLineUnroundedTaxableAmt | UNROUNDED_TAXABLE_AMT | — | ✅ |
| 274 | WithholdingDetailTaxLineWhtGroupId | WHT_GROUP_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
