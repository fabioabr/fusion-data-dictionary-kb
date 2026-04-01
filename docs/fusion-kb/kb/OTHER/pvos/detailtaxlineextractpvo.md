---
id: DOC-OTHER-PVO-DetailTaxLineExtractPVO
doc_type: system-doc
title: "DetailTaxLineExtractPVO — PVO Cross-Module"
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
  - DetailTaxLineExtractPVO
  - detailtaxlineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DetailTaxLineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Detail Tax Line Extract. Acessa as tabelas: ZX_LINES.

**Caminho:** `FscmTopModelAM.FinExtractAM.ZxBiccExtractAM.DetailTaxLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 300 | 1 | 1 | 243 | 81% |

---

## 🔗 Tabelas Relacionadas

- [[zx_lines|ZX_LINES]] — 300 atributos (1 PKs, 243 BICC)

---

## ⚙️ Atributos

### [[zx_lines|ZX_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DetailTaxLineAccountSourceTaxRateId | ACCOUNT_SOURCE_TAX_RATE_ID | — | ✅ |
| 2 | DetailTaxLineAdjustedDocApplicationId | ADJUSTED_DOC_APPLICATION_ID | — | ✅ |
| 3 | DetailTaxLineAdjustedDocDate | ADJUSTED_DOC_DATE | — | ✅ |
| 4 | DetailTaxLineAdjustedDocEntityCode | ADJUSTED_DOC_ENTITY_CODE | — | ✅ |
| 5 | DetailTaxLineAdjustedDocEventClassCode | ADJUSTED_DOC_EVENT_CLASS_CODE | — | ✅ |
| 6 | DetailTaxLineAdjustedDocLineId | ADJUSTED_DOC_LINE_ID | — | ✅ |
| 7 | DetailTaxLineAdjustedDocNumber | ADJUSTED_DOC_NUMBER | — | ✅ |
| 8 | DetailTaxLineAdjustedDocTaxLineId | ADJUSTED_DOC_TAX_LINE_ID | — | ✅ |
| 9 | DetailTaxLineAdjustedDocTrxId | ADJUSTED_DOC_TRX_ID | — | ✅ |
| 10 | DetailTaxLineAdjustedDocTrxLevelType | ADJUSTED_DOC_TRX_LEVEL_TYPE | — | ✅ |
| 11 | DetailTaxLineApplicationId | APPLICATION_ID | — | ✅ |
| 12 | DetailTaxLineAppliedFromApplicationId | APPLIED_FROM_APPLICATION_ID | — | ✅ |
| 13 | DetailTaxLineAppliedFromEntityCode | APPLIED_FROM_ENTITY_CODE | — | ✅ |
| 14 | DetailTaxLineAppliedFromEventClassCode | APPLIED_FROM_EVENT_CLASS_CODE | — | ✅ |
| 15 | DetailTaxLineAppliedFromLineId | APPLIED_FROM_LINE_ID | — | ✅ |
| 16 | DetailTaxLineAppliedFromTrxId | APPLIED_FROM_TRX_ID | — | ✅ |
| 17 | DetailTaxLineAppliedFromTrxLevelType | APPLIED_FROM_TRX_LEVEL_TYPE | — | ✅ |
| 18 | DetailTaxLineAppliedFromTrxNumber | APPLIED_FROM_TRX_NUMBER | — | ✅ |
| 19 | DetailTaxLineAppliedToApplicationId | APPLIED_TO_APPLICATION_ID | — | ✅ |
| 20 | DetailTaxLineAppliedToEntityCode | APPLIED_TO_ENTITY_CODE | — | ✅ |
| 21 | DetailTaxLineAppliedToEventClassCode | APPLIED_TO_EVENT_CLASS_CODE | — | ✅ |
| 22 | DetailTaxLineAppliedToLineId | APPLIED_TO_LINE_ID | — | ✅ |
| 23 | DetailTaxLineAppliedToTrxId | APPLIED_TO_TRX_ID | — | ✅ |
| 24 | DetailTaxLineAppliedToTrxLevelType | APPLIED_TO_TRX_LEVEL_TYPE | — | ✅ |
| 25 | DetailTaxLineAppliedToTrxNumber | APPLIED_TO_TRX_NUMBER | — | ✅ |
| 26 | DetailTaxLineAssociatedChildFrozenFlag | ASSOCIATED_CHILD_FROZEN_FLAG | — | ✅ |
| 27 | DetailTaxLineAttribute1 | ATTRIBUTE1 | — | — |
| 28 | DetailTaxLineAttribute10 | ATTRIBUTE10 | — | — |
| 29 | DetailTaxLineAttribute11 | ATTRIBUTE11 | — | — |
| 30 | DetailTaxLineAttribute12 | ATTRIBUTE12 | — | — |
| 31 | DetailTaxLineAttribute13 | ATTRIBUTE13 | — | — |
| 32 | DetailTaxLineAttribute14 | ATTRIBUTE14 | — | — |
| 33 | DetailTaxLineAttribute15 | ATTRIBUTE15 | — | — |
| 34 | DetailTaxLineAttribute2 | ATTRIBUTE2 | — | — |
| 35 | DetailTaxLineAttribute3 | ATTRIBUTE3 | — | — |
| 36 | DetailTaxLineAttribute4 | ATTRIBUTE4 | — | — |
| 37 | DetailTaxLineAttribute5 | ATTRIBUTE5 | — | — |
| 38 | DetailTaxLineAttribute6 | ATTRIBUTE6 | — | — |
| 39 | DetailTaxLineAttribute7 | ATTRIBUTE7 | — | — |
| 40 | DetailTaxLineAttribute8 | ATTRIBUTE8 | — | — |
| 41 | DetailTaxLineAttribute9 | ATTRIBUTE9 | — | — |
| 42 | DetailTaxLineAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 43 | DetailTaxLineAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 44 | DetailTaxLineAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 45 | DetailTaxLineAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 46 | DetailTaxLineAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 47 | DetailTaxLineAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 48 | DetailTaxLineAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 49 | DetailTaxLineAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 50 | DetailTaxLineAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 51 | DetailTaxLineAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 52 | DetailTaxLineAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 53 | DetailTaxLineBasisResultId | BASIS_RESULT_ID | — | ✅ |
| 54 | DetailTaxLineCalTaxAmt | CAL_TAX_AMT | — | ✅ |
| 55 | DetailTaxLineCalTaxAmtFunclCurr | CAL_TAX_AMT_FUNCL_CURR | — | ✅ |
| 56 | DetailTaxLineCalTaxAmtTaxCurr | CAL_TAX_AMT_TAX_CURR | — | ✅ |
| 57 | DetailTaxLineCalTaxableAmt | CAL_TAXABLE_AMT | — | ✅ |
| 58 | DetailTaxLineCalcResultId | CALC_RESULT_ID | — | ✅ |
| 59 | DetailTaxLineCancelFlag | CANCEL_FLAG | — | ✅ |
| 60 | DetailTaxLineCompoundingDepTaxFlag | COMPOUNDING_DEP_TAX_FLAG | — | ✅ |
| 61 | DetailTaxLineCompoundingTaxFlag | COMPOUNDING_TAX_FLAG | — | ✅ |
| 62 | DetailTaxLineCompoundingTaxMissFlag | COMPOUNDING_TAX_MISS_FLAG | — | ✅ |
| 63 | DetailTaxLineContentOwnerId | CONTENT_OWNER_ID | — | ✅ |
| 64 | DetailTaxLineCopiedFromOtherDocFlag | COPIED_FROM_OTHER_DOC_FLAG | — | ✅ |
| 65 | DetailTaxLineCreatedBy | CREATED_BY | — | ✅ |
| 66 | DetailTaxLineCreationDate | CREATION_DATE | — | ✅ |
| 67 | DetailTaxLineCtrlTotalLineTxAmt | CTRL_TOTAL_LINE_TX_AMT | — | ✅ |
| 68 | DetailTaxLineCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 69 | DetailTaxLineCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 70 | DetailTaxLineCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 71 | DetailTaxLineDeleteFlag | DELETE_FLAG | — | ✅ |
| 72 | DetailTaxLineDirectRateResultId | DIRECT_RATE_RESULT_ID | — | ✅ |
| 73 | DetailTaxLineDocEventStatus | DOC_EVENT_STATUS | — | ✅ |
| 74 | DetailTaxLineEnforceFromNaturalAcctFlag | ENFORCE_FROM_NATURAL_ACCT_FLAG | — | ✅ |
| 75 | DetailTaxLineEntityCode | ENTITY_CODE | — | ✅ |
| 76 | DetailTaxLineEstablishmentId | ESTABLISHMENT_ID | — | ✅ |
| 77 | DetailTaxLineEvalExcptResultId | EVAL_EXCPT_RESULT_ID | — | ✅ |
| 78 | DetailTaxLineEvalExmptResultId | EVAL_EXMPT_RESULT_ID | — | ✅ |
| 79 | DetailTaxLineEventClassCode | EVENT_CLASS_CODE | — | ✅ |
| 80 | DetailTaxLineEventTypeCode | EVENT_TYPE_CODE | — | ✅ |
| 81 | DetailTaxLineExceptionRate | EXCEPTION_RATE | — | ✅ |
| 82 | DetailTaxLineExemptCertificateNumber | EXEMPT_CERTIFICATE_NUMBER | — | ✅ |
| 83 | DetailTaxLineExemptRateModifier | EXEMPT_RATE_MODIFIER | — | ✅ |
| 84 | DetailTaxLineExemptReason | EXEMPT_REASON | — | ✅ |
| 85 | DetailTaxLineExemptReasonCode | EXEMPT_REASON_CODE | — | ✅ |
| 86 | DetailTaxLineFreezeUntilOverriddenFlag | FREEZE_UNTIL_OVERRIDDEN_FLAG | — | ✅ |
| 87 | DetailTaxLineGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 88 | DetailTaxLineGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 89 | DetailTaxLineGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 90 | DetailTaxLineGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 91 | DetailTaxLineGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 92 | DetailTaxLineGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 93 | DetailTaxLineGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 94 | DetailTaxLineGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 95 | DetailTaxLineGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 96 | DetailTaxLineGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 97 | DetailTaxLineGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 98 | DetailTaxLineGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 99 | DetailTaxLineGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 100 | DetailTaxLineGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 101 | DetailTaxLineGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 102 | DetailTaxLineGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 103 | DetailTaxLineGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 104 | DetailTaxLineGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 105 | DetailTaxLineGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 106 | DetailTaxLineGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 107 | DetailTaxLineGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 108 | DetailTaxLineGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 109 | DetailTaxLineGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 110 | DetailTaxLineGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 111 | DetailTaxLineGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 112 | DetailTaxLineGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 113 | DetailTaxLineGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 114 | DetailTaxLineGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 115 | DetailTaxLineGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 116 | DetailTaxLineGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 117 | DetailTaxLineGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 118 | DetailTaxLineHistoricalFlag | HISTORICAL_FLAG | — | ✅ |
| 119 | DetailTaxLineHqEstbPartyTaxProfId | HQ_ESTB_PARTY_TAX_PROF_ID | — | ✅ |
| 120 | DetailTaxLineHqEstbRegNumber | HQ_ESTB_REG_NUMBER | — | ✅ |
| 121 | DetailTaxLineInterfaceEntityCode | INTERFACE_ENTITY_CODE | — | ✅ |
| 122 | DetailTaxLineInterfaceTaxLineId | INTERFACE_TAX_LINE_ID | — | ✅ |
| 123 | DetailTaxLineInternalOrgLocationId | INTERNAL_ORG_LOCATION_ID | — | ✅ |
| 124 | DetailTaxLineInternalOrganizationId | INTERNAL_ORGANIZATION_ID | — | ✅ |
| 125 | DetailTaxLineItemDistChangedFlag | ITEM_DIST_CHANGED_FLAG | — | ✅ |
| 126 | DetailTaxLineLastManualEntry | LAST_MANUAL_ENTRY | — | ✅ |
| 127 | DetailTaxLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 128 | DetailTaxLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 129 | DetailTaxLineLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 130 | DetailTaxLineLedgerId | LEDGER_ID | — | ✅ |
| 131 | DetailTaxLineLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 132 | DetailTaxLineLegalEntityTaxRegNumber | LEGAL_ENTITY_TAX_REG_NUMBER | — | ✅ |
| 133 | DetailTaxLineLegalJustificationText1 | LEGAL_JUSTIFICATION_TEXT1 | — | ✅ |
| 134 | DetailTaxLineLegalJustificationText2 | LEGAL_JUSTIFICATION_TEXT2 | — | ✅ |
| 135 | DetailTaxLineLegalJustificationText3 | LEGAL_JUSTIFICATION_TEXT3 | — | ✅ |
| 136 | DetailTaxLineLegalMessageAppl2 | LEGAL_MESSAGE_APPL_2 | — | ✅ |
| 137 | DetailTaxLineLegalMessageBasis | LEGAL_MESSAGE_BASIS | — | ✅ |
| 138 | DetailTaxLineLegalMessageCalc | LEGAL_MESSAGE_CALC | — | ✅ |
| 139 | DetailTaxLineLegalMessageExcpt | LEGAL_MESSAGE_EXCPT | — | ✅ |
| 140 | DetailTaxLineLegalMessageExmpt | LEGAL_MESSAGE_EXMPT | — | ✅ |
| 141 | DetailTaxLineLegalMessagePos | LEGAL_MESSAGE_POS | — | ✅ |
| 142 | DetailTaxLineLegalMessageRate | LEGAL_MESSAGE_RATE | — | ✅ |
| 143 | DetailTaxLineLegalMessageStatus | LEGAL_MESSAGE_STATUS | — | ✅ |
| 144 | DetailTaxLineLegalMessageThreshold | LEGAL_MESSAGE_THRESHOLD | — | ✅ |
| 145 | DetailTaxLineLegalMessageTrn | LEGAL_MESSAGE_TRN | — | ✅ |
| 146 | DetailTaxLineLegalReportingStatus | LEGAL_REPORTING_STATUS | — | ✅ |
| 147 | DetailTaxLineLineAmt | LINE_AMT | — | ✅ |
| 148 | DetailTaxLineLineAssessableValue | LINE_ASSESSABLE_VALUE | — | ✅ |
| 149 | DetailTaxLineManuallyEnteredFlag | MANUALLY_ENTERED_FLAG | — | ✅ |
| 150 | DetailTaxLineMinimumAccountableUnit | MINIMUM_ACCOUNTABLE_UNIT | — | ✅ |
| 151 | DetailTaxLineMrcLinkToTaxLineId | MRC_LINK_TO_TAX_LINE_ID | — | ✅ |
| 152 | DetailTaxLineMrcTaxLineFlag | MRC_TAX_LINE_FLAG | — | ✅ |
| 153 | DetailTaxLineMultipleJurisdictionsFlag | MULTIPLE_JURISDICTIONS_FLAG | — | ✅ |
| 154 | DetailTaxLineNrecTaxAmt | NREC_TAX_AMT | — | ✅ |
| 155 | DetailTaxLineNrecTaxAmtFunclCurr | NREC_TAX_AMT_FUNCL_CURR | — | ✅ |
| 156 | DetailTaxLineNrecTaxAmtTaxCurr | NREC_TAX_AMT_TAX_CURR | — | ✅ |
| 157 | DetailTaxLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 158 | DetailTaxLineOffsetFlag | OFFSET_FLAG | — | ✅ |
| 159 | DetailTaxLineOffsetLinkToTaxLineId | OFFSET_LINK_TO_TAX_LINE_ID | — | ✅ |
| 160 | DetailTaxLineOffsetTaxRateCode | OFFSET_TAX_RATE_CODE | — | ✅ |
| 161 | DetailTaxLineOrigSelfAssessedFlag | ORIG_SELF_ASSESSED_FLAG | — | ✅ |
| 162 | DetailTaxLineOrigTaxAmt | ORIG_TAX_AMT | — | ✅ |
| 163 | DetailTaxLineOrigTaxAmtIncludedFlag | ORIG_TAX_AMT_INCLUDED_FLAG | — | ✅ |
| 164 | DetailTaxLineOrigTaxAmtTaxCurr | ORIG_TAX_AMT_TAX_CURR | — | ✅ |
| 165 | DetailTaxLineOrigTaxJurisdictionCode | ORIG_TAX_JURISDICTION_CODE | — | ✅ |
| 166 | DetailTaxLineOrigTaxJurisdictionId | ORIG_TAX_JURISDICTION_ID | — | ✅ |
| 167 | DetailTaxLineOrigTaxPointDate | ORIG_TAX_POINT_DATE | — | ✅ |
| 168 | DetailTaxLineOrigTaxRate | ORIG_TAX_RATE | — | ✅ |
| 169 | DetailTaxLineOrigTaxRateCode | ORIG_TAX_RATE_CODE | — | ✅ |
| 170 | DetailTaxLineOrigTaxRateId | ORIG_TAX_RATE_ID | — | ✅ |
| 171 | DetailTaxLineOrigTaxStatusCode | ORIG_TAX_STATUS_CODE | — | ✅ |
| 172 | DetailTaxLineOrigTaxStatusId | ORIG_TAX_STATUS_ID | — | ✅ |
| 173 | DetailTaxLineOrigTaxableAmt | ORIG_TAXABLE_AMT | — | ✅ |
| 174 | DetailTaxLineOrigTaxableAmtTaxCurr | ORIG_TAXABLE_AMT_TAX_CURR | — | ✅ |
| 175 | DetailTaxLineOtherDocLineAmt | OTHER_DOC_LINE_AMT | — | ✅ |
| 176 | DetailTaxLineOtherDocLineTaxAmt | OTHER_DOC_LINE_TAX_AMT | — | ✅ |
| 177 | DetailTaxLineOtherDocLineTaxableAmt | OTHER_DOC_LINE_TAXABLE_AMT | — | ✅ |
| 178 | DetailTaxLineOtherDocSource | OTHER_DOC_SOURCE | — | ✅ |
| 179 | DetailTaxLineOverriddenFlag | OVERRIDDEN_FLAG | — | ✅ |
| 180 | DetailTaxLinePlaceOfSupply | PLACE_OF_SUPPLY | — | ✅ |
| 181 | DetailTaxLinePlaceOfSupplyResultId | PLACE_OF_SUPPLY_RESULT_ID | — | ✅ |
| 182 | DetailTaxLinePlaceOfSupplyTypeCode | PLACE_OF_SUPPLY_TYPE_CODE | — | ✅ |
| 183 | DetailTaxLinePrdTotalTaxAmt | PRD_TOTAL_TAX_AMT | — | ✅ |
| 184 | DetailTaxLinePrdTotalTaxAmtFunclCurr | PRD_TOTAL_TAX_AMT_FUNCL_CURR | — | ✅ |
| 185 | DetailTaxLinePrdTotalTaxAmtTaxCurr | PRD_TOTAL_TAX_AMT_TAX_CURR | — | ✅ |
| 186 | DetailTaxLinePrecision | PRECISION | — | ✅ |
| 187 | DetailTaxLineProcessForRecoveryFlag | PROCESS_FOR_RECOVERY_FLAG | — | ✅ |
| 188 | DetailTaxLinePurgeFlag | PURGE_FLAG | — | ✅ |
| 189 | DetailTaxLineRateResultId | RATE_RESULT_ID | — | ✅ |
| 190 | DetailTaxLineRecTaxAmt | REC_TAX_AMT | — | ✅ |
| 191 | DetailTaxLineRecTaxAmtFunclCurr | REC_TAX_AMT_FUNCL_CURR | — | ✅ |
| 192 | DetailTaxLineRecTaxAmtTaxCurr | REC_TAX_AMT_TAX_CURR | — | ✅ |
| 193 | DetailTaxLineRecalcRequiredFlag | RECALC_REQUIRED_FLAG | — | ✅ |
| 194 | DetailTaxLineRecordTypeCode | RECORD_TYPE_CODE | — | ✅ |
| 195 | DetailTaxLineRefDocApplicationId | REF_DOC_APPLICATION_ID | — | ✅ |
| 196 | DetailTaxLineRefDocEntityCode | REF_DOC_ENTITY_CODE | — | ✅ |
| 197 | DetailTaxLineRefDocEventClassCode | REF_DOC_EVENT_CLASS_CODE | — | ✅ |
| 198 | DetailTaxLineRefDocLineId | REF_DOC_LINE_ID | — | ✅ |
| 199 | DetailTaxLineRefDocLineQuantity | REF_DOC_LINE_QUANTITY | — | ✅ |
| 200 | DetailTaxLineRefDocTrxId | REF_DOC_TRX_ID | — | ✅ |
| 201 | DetailTaxLineRefDocTrxLevelType | REF_DOC_TRX_LEVEL_TYPE | — | ✅ |
| 202 | DetailTaxLineRegistrationPartyType | REGISTRATION_PARTY_TYPE | — | ✅ |
| 203 | DetailTaxLineRelatedDocApplicationId | RELATED_DOC_APPLICATION_ID | — | ✅ |
| 204 | DetailTaxLineRelatedDocDate | RELATED_DOC_DATE | — | ✅ |
| 205 | DetailTaxLineRelatedDocEntityCode | RELATED_DOC_ENTITY_CODE | — | ✅ |
| 206 | DetailTaxLineRelatedDocEventClassCode | RELATED_DOC_EVENT_CLASS_CODE | — | ✅ |
| 207 | DetailTaxLineRelatedDocNumber | RELATED_DOC_NUMBER | — | ✅ |
| 208 | DetailTaxLineRelatedDocTrxId | RELATED_DOC_TRX_ID | — | ✅ |
| 209 | DetailTaxLineReportableFlag | REPORTABLE_FLAG | — | ✅ |
| 210 | DetailTaxLineReportingCurrencyCode | REPORTING_CURRENCY_CODE | — | ✅ |
| 211 | DetailTaxLineReportingOnlyFlag | REPORTING_ONLY_FLAG | — | ✅ |
| 212 | DetailTaxLineReportingPeriodId | REPORTING_PERIOD_ID | — | ✅ |
| 213 | DetailTaxLineReversedTaxLineId | REVERSED_TAX_LINE_ID | — | ✅ |
| 214 | DetailTaxLineRoundingLevelCode | ROUNDING_LEVEL_CODE | — | ✅ |
| 215 | DetailTaxLineRoundingLvlPartyTaxProfId | ROUNDING_LVL_PARTY_TAX_PROF_ID | — | ✅ |
| 216 | DetailTaxLineRoundingLvlPartyType | ROUNDING_LVL_PARTY_TYPE | — | ✅ |
| 217 | DetailTaxLineRoundingRuleCode | ROUNDING_RULE_CODE | — | ✅ |
| 218 | DetailTaxLineSelfAssessedFlag | SELF_ASSESSED_FLAG | — | ✅ |
| 219 | DetailTaxLineStatusResultId | STATUS_RESULT_ID | — | ✅ |
| 220 | DetailTaxLineSummaryTaxLineId | SUMMARY_TAX_LINE_ID | — | ✅ |
| 221 | DetailTaxLineSyncWithPrvdrFlag | SYNC_WITH_PRVDR_FLAG | — | ✅ |
| 222 | DetailTaxLineTax | TAX | — | ✅ |
| 223 | DetailTaxLineTaxAmt | TAX_AMT | — | ✅ |
| 224 | DetailTaxLineTaxAmtFunclCurr | TAX_AMT_FUNCL_CURR | — | ✅ |
| 225 | DetailTaxLineTaxAmtIncludedFlag | TAX_AMT_INCLUDED_FLAG | — | ✅ |
| 226 | DetailTaxLineTaxAmtTaxCurr | TAX_AMT_TAX_CURR | — | ✅ |
| 227 | DetailTaxLineTaxApplicabilityResultId | TAX_APPLICABILITY_RESULT_ID | — | ✅ |
| 228 | DetailTaxLineTaxApportionmentFlag | TAX_APPORTIONMENT_FLAG | — | ✅ |
| 229 | DetailTaxLineTaxApportionmentLineNumber | TAX_APPORTIONMENT_LINE_NUMBER | — | ✅ |
| 230 | DetailTaxLineTaxBaseModifierRate | TAX_BASE_MODIFIER_RATE | — | ✅ |
| 231 | DetailTaxLineTaxCalculationFormula | TAX_CALCULATION_FORMULA | — | ✅ |
| 232 | DetailTaxLineTaxCode | TAX_CODE | — | ✅ |
| 233 | DetailTaxLineTaxCurrencyCode | TAX_CURRENCY_CODE | — | ✅ |
| 234 | DetailTaxLineTaxCurrencyConversionDate | TAX_CURRENCY_CONVERSION_DATE | — | ✅ |
| 235 | DetailTaxLineTaxCurrencyConversionRate | TAX_CURRENCY_CONVERSION_RATE | — | ✅ |
| 236 | DetailTaxLineTaxCurrencyConversionType | TAX_CURRENCY_CONVERSION_TYPE | — | ✅ |
| 237 | DetailTaxLineTaxDate | TAX_DATE | — | ✅ |
| 238 | DetailTaxLineTaxDateRuleId | TAX_DATE_RULE_ID | — | ✅ |
| 239 | DetailTaxLineTaxDetermineDate | TAX_DETERMINE_DATE | — | ✅ |
| 240 | DetailTaxLineTaxEventClassCode | TAX_EVENT_CLASS_CODE | — | ✅ |
| 241 | DetailTaxLineTaxEventTypeCode | TAX_EVENT_TYPE_CODE | — | ✅ |
| 242 | DetailTaxLineTaxExceptionId | TAX_EXCEPTION_ID | — | ✅ |
| 243 | DetailTaxLineTaxExemptionId | TAX_EXEMPTION_ID | — | ✅ |
| 244 | DetailTaxLineTaxHoldCode | TAX_HOLD_CODE | — | ✅ |
| 245 | DetailTaxLineTaxHoldReleasedCode | TAX_HOLD_RELEASED_CODE | — | ✅ |
| 246 | DetailTaxLineTaxId | TAX_ID | — | ✅ |
| 247 | DetailTaxLineTaxJurisdictionCode | TAX_JURISDICTION_CODE | — | ✅ |
| 248 | DetailTaxLineTaxJurisdictionId | TAX_JURISDICTION_ID | — | ✅ |
| 249 | DetailTaxLineTaxLineId | TAX_LINE_ID | 🔑 | ✅ |
| 250 | DetailTaxLineTaxLineNumber | TAX_LINE_NUMBER | — | ✅ |
| 251 | DetailTaxLineTaxOnlyLineFlag | TAX_ONLY_LINE_FLAG | — | ✅ |
| 252 | DetailTaxLineTaxPointBasis | TAX_POINT_BASIS | — | ✅ |
| 253 | DetailTaxLineTaxPointDate | TAX_POINT_DATE | — | ✅ |
| 254 | DetailTaxLineTaxProviderId | TAX_PROVIDER_ID | — | ✅ |
| 255 | DetailTaxLineTaxRate | TAX_RATE | — | ✅ |
| 256 | DetailTaxLineTaxRateBeforeException | TAX_RATE_BEFORE_EXCEPTION | — | ✅ |
| 257 | DetailTaxLineTaxRateBeforeExemption | TAX_RATE_BEFORE_EXEMPTION | — | ✅ |
| 258 | DetailTaxLineTaxRateCode | TAX_RATE_CODE | — | ✅ |
| 259 | DetailTaxLineTaxRateId | TAX_RATE_ID | — | ✅ |
| 260 | DetailTaxLineTaxRateNameBeforeException | TAX_RATE_NAME_BEFORE_EXCEPTION | — | ✅ |
| 261 | DetailTaxLineTaxRateNameBeforeExemption | TAX_RATE_NAME_BEFORE_EXEMPTION | — | ✅ |
| 262 | DetailTaxLineTaxRateType | TAX_RATE_TYPE | — | ✅ |
| 263 | DetailTaxLineTaxRegNumDetResultId | TAX_REG_NUM_DET_RESULT_ID | — | ✅ |
| 264 | DetailTaxLineTaxRegimeCode | TAX_REGIME_CODE | — | ✅ |
| 265 | DetailTaxLineTaxRegimeId | TAX_REGIME_ID | — | ✅ |
| 266 | DetailTaxLineTaxRegimeTemplateId | TAX_REGIME_TEMPLATE_ID | — | ✅ |
| 267 | DetailTaxLineTaxRegistrationId | TAX_REGISTRATION_ID | — | ✅ |
| 268 | DetailTaxLineTaxRegistrationNumber | TAX_REGISTRATION_NUMBER | — | ✅ |
| 269 | DetailTaxLineTaxStatusCode | TAX_STATUS_CODE | — | ✅ |
| 270 | DetailTaxLineTaxStatusId | TAX_STATUS_ID | — | ✅ |
| 271 | DetailTaxLineTaxTypeCode | TAX_TYPE_CODE | — | ✅ |
| 272 | DetailTaxLineTaxableAmt | TAXABLE_AMT | — | ✅ |
| 273 | DetailTaxLineTaxableAmtFunclCurr | TAXABLE_AMT_FUNCL_CURR | — | ✅ |
| 274 | DetailTaxLineTaxableAmtTaxCurr | TAXABLE_AMT_TAX_CURR | — | ✅ |
| 275 | DetailTaxLineTaxableBasisFormula | TAXABLE_BASIS_FORMULA | — | ✅ |
| 276 | DetailTaxLineTaxingJurisGeographyId | TAXING_JURIS_GEOGRAPHY_ID | — | ✅ |
| 277 | DetailTaxLineThreshResultId | THRESH_RESULT_ID | — | ✅ |
| 278 | DetailTaxLineTrxCurrencyCode | TRX_CURRENCY_CODE | — | ✅ |
| 279 | DetailTaxLineTrxDate | TRX_DATE | — | ✅ |
| 280 | DetailTaxLineTrxId | TRX_ID | — | ✅ |
| 281 | DetailTaxLineTrxIdLevel2 | TRX_ID_LEVEL2 | — | ✅ |
| 282 | DetailTaxLineTrxIdLevel3 | TRX_ID_LEVEL3 | — | ✅ |
| 283 | DetailTaxLineTrxIdLevel4 | TRX_ID_LEVEL4 | — | ✅ |
| 284 | DetailTaxLineTrxIdLevel5 | TRX_ID_LEVEL5 | — | ✅ |
| 285 | DetailTaxLineTrxIdLevel6 | TRX_ID_LEVEL6 | — | ✅ |
| 286 | DetailTaxLineTrxLevelType | TRX_LEVEL_TYPE | — | ✅ |
| 287 | DetailTaxLineTrxLineDate | TRX_LINE_DATE | — | ✅ |
| 288 | DetailTaxLineTrxLineId | TRX_LINE_ID | — | ✅ |
| 289 | DetailTaxLineTrxLineNumber | TRX_LINE_NUMBER | — | ✅ |
| 290 | DetailTaxLineTrxLineQuantity | TRX_LINE_QUANTITY | — | ✅ |
| 291 | DetailTaxLineTrxNumber | TRX_NUMBER | — | ✅ |
| 292 | DetailTaxLineTrxUserKeyLevel1 | TRX_USER_KEY_LEVEL1 | — | ✅ |
| 293 | DetailTaxLineTrxUserKeyLevel2 | TRX_USER_KEY_LEVEL2 | — | ✅ |
| 294 | DetailTaxLineTrxUserKeyLevel3 | TRX_USER_KEY_LEVEL3 | — | ✅ |
| 295 | DetailTaxLineTrxUserKeyLevel4 | TRX_USER_KEY_LEVEL4 | — | ✅ |
| 296 | DetailTaxLineTrxUserKeyLevel5 | TRX_USER_KEY_LEVEL5 | — | ✅ |
| 297 | DetailTaxLineTrxUserKeyLevel6 | TRX_USER_KEY_LEVEL6 | — | ✅ |
| 298 | DetailTaxLineUnitPrice | UNIT_PRICE | — | ✅ |
| 299 | DetailTaxLineUnroundedTaxAmt | UNROUNDED_TAX_AMT | — | ✅ |
| 300 | DetailTaxLineUnroundedTaxableAmt | UNROUNDED_TAXABLE_AMT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
