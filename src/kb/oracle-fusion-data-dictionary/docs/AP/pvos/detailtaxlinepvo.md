---
id: DOC-AP-PVO-DetailTaxLinePVO
doc_type: system-doc
title: "DetailTaxLinePVO — PVO Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ap
  - data-dictionary
  - pvo
  - bicc
aliases:
  - DetailTaxLinePVO
  - detailtaxlinepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DetailTaxLinePVO

## 📌 Visão Geral

Extrai as linhas detalhadas de impostos calculados sobre transações financeiras, incluindo regime fiscal, jurisdição, alíquota, base de cálculo e valores retidos. Essencial para conformidade tributária, apuração de impostos e auditoria fiscal de contas a pagar.

**Caminho:** `FscmTopModelAM.FinApInvTransactionsAM.DetailTaxLinePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 198 | 1 | 1 | 20 | 10% |

---

## 🔗 Tabelas Relacionadas

- [[zx_lines|ZX_LINES]] — 198 atributos (1 PKs, 20 BICC)

---

## ⚙️ Atributos

### [[zx_lines|ZX_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DetailTaxLineAccountSourceTaxRateId | ACCOUNT_SOURCE_TAX_RATE_ID | — | — |
| 2 | DetailTaxLineAdjustedDocApplicationId | ADJUSTED_DOC_APPLICATION_ID | — | — |
| 3 | DetailTaxLineAdjustedDocDate | ADJUSTED_DOC_DATE | — | — |
| 4 | DetailTaxLineAdjustedDocEntityCode | ADJUSTED_DOC_ENTITY_CODE | — | — |
| 5 | DetailTaxLineAdjustedDocEventClassCode | ADJUSTED_DOC_EVENT_CLASS_CODE | — | — |
| 6 | DetailTaxLineAdjustedDocLineId | ADJUSTED_DOC_LINE_ID | — | — |
| 7 | DetailTaxLineAdjustedDocNumber | ADJUSTED_DOC_NUMBER | — | — |
| 8 | DetailTaxLineAdjustedDocTaxLineId | ADJUSTED_DOC_TAX_LINE_ID | — | — |
| 9 | DetailTaxLineAdjustedDocTrxId | ADJUSTED_DOC_TRX_ID | — | — |
| 10 | DetailTaxLineAdjustedDocTrxLevelType | ADJUSTED_DOC_TRX_LEVEL_TYPE | — | — |
| 11 | DetailTaxLineApplicationId | APPLICATION_ID | — | — |
| 12 | DetailTaxLineAppliedFromApplicationId | APPLIED_FROM_APPLICATION_ID | — | — |
| 13 | DetailTaxLineAppliedFromEntityCode | APPLIED_FROM_ENTITY_CODE | — | — |
| 14 | DetailTaxLineAppliedFromEventClassCode | APPLIED_FROM_EVENT_CLASS_CODE | — | — |
| 15 | DetailTaxLineAppliedFromLineId | APPLIED_FROM_LINE_ID | — | — |
| 16 | DetailTaxLineAppliedFromTrxId | APPLIED_FROM_TRX_ID | — | — |
| 17 | DetailTaxLineAppliedFromTrxLevelType | APPLIED_FROM_TRX_LEVEL_TYPE | — | — |
| 18 | DetailTaxLineAppliedFromTrxNumber | APPLIED_FROM_TRX_NUMBER | — | — |
| 19 | DetailTaxLineAppliedToApplicationId | APPLIED_TO_APPLICATION_ID | — | — |
| 20 | DetailTaxLineAppliedToEntityCode | APPLIED_TO_ENTITY_CODE | — | — |
| 21 | DetailTaxLineAppliedToEventClassCode | APPLIED_TO_EVENT_CLASS_CODE | — | — |
| 22 | DetailTaxLineAppliedToLineId | APPLIED_TO_LINE_ID | — | — |
| 23 | DetailTaxLineAppliedToTrxId | APPLIED_TO_TRX_ID | — | — |
| 24 | DetailTaxLineAppliedToTrxLevelType | APPLIED_TO_TRX_LEVEL_TYPE | — | — |
| 25 | DetailTaxLineAppliedToTrxNumber | APPLIED_TO_TRX_NUMBER | — | — |
| 26 | DetailTaxLineAssociatedChildFrozenFlag | ASSOCIATED_CHILD_FROZEN_FLAG | — | — |
| 27 | DetailTaxLineAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 28 | DetailTaxLineBasisResultId | BASIS_RESULT_ID | — | — |
| 29 | DetailTaxLineCalTaxAmt | CAL_TAX_AMT | — | — |
| 30 | DetailTaxLineCalTaxAmtFunclCurr | CAL_TAX_AMT_FUNCL_CURR | — | — |
| 31 | DetailTaxLineCalTaxAmtTaxCurr | CAL_TAX_AMT_TAX_CURR | — | — |
| 32 | DetailTaxLineCalTaxableAmt | CAL_TAXABLE_AMT | — | — |
| 33 | DetailTaxLineCalcResultId | CALC_RESULT_ID | — | — |
| 34 | DetailTaxLineCancelFlag | CANCEL_FLAG | — | ✅ |
| 35 | DetailTaxLineCompoundingDepTaxFlag | COMPOUNDING_DEP_TAX_FLAG | — | — |
| 36 | DetailTaxLineCompoundingTaxFlag | COMPOUNDING_TAX_FLAG | — | — |
| 37 | DetailTaxLineCopiedFromOtherDocFlag | COPIED_FROM_OTHER_DOC_FLAG | — | — |
| 38 | DetailTaxLineCreatedBy | CREATED_BY | — | — |
| 39 | DetailTaxLineCreationDate | CREATION_DATE | — | — |
| 40 | DetailTaxLineDeleteFlag | DELETE_FLAG | — | — |
| 41 | DetailTaxLineDocEventStatus | DOC_EVENT_STATUS | — | — |
| 42 | DetailTaxLineEntityCode | ENTITY_CODE | — | — |
| 43 | DetailTaxLineEstablishmentId | ESTABLISHMENT_ID | — | — |
| 44 | DetailTaxLineEvalExcptResultId | EVAL_EXCPT_RESULT_ID | — | — |
| 45 | DetailTaxLineEvalExmptResultId | EVAL_EXMPT_RESULT_ID | — | — |
| 46 | DetailTaxLineEventClassCode | EVENT_CLASS_CODE | — | — |
| 47 | DetailTaxLineEventTypeCode | EVENT_TYPE_CODE | — | — |
| 48 | DetailTaxLineExceptionRate | EXCEPTION_RATE | — | — |
| 49 | DetailTaxLineExemptCertificateNumber | EXEMPT_CERTIFICATE_NUMBER | — | — |
| 50 | DetailTaxLineExemptReason | EXEMPT_REASON | — | — |
| 51 | DetailTaxLineExemptReasonCode | EXEMPT_REASON_CODE | — | — |
| 52 | DetailTaxLineFreezeUntilOverriddenFlag | FREEZE_UNTIL_OVERRIDDEN_FLAG | — | — |
| 53 | DetailTaxLineHistoricalFlag | HISTORICAL_FLAG | — | — |
| 54 | DetailTaxLineHqEstbPartyTaxProfId | HQ_ESTB_PARTY_TAX_PROF_ID | — | — |
| 55 | DetailTaxLineHqEstbRegNumber | HQ_ESTB_REG_NUMBER | — | — |
| 56 | DetailTaxLineInternalOrganizationId | INTERNAL_ORGANIZATION_ID | — | — |
| 57 | DetailTaxLineItemDistChangedFlag | ITEM_DIST_CHANGED_FLAG | — | — |
| 58 | DetailTaxLineLastManualEntry | LAST_MANUAL_ENTRY | — | — |
| 59 | DetailTaxLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 60 | DetailTaxLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 61 | DetailTaxLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 62 | DetailTaxLineLedgerId | LEDGER_ID | — | — |
| 63 | DetailTaxLineLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 64 | DetailTaxLineLegalEntityTaxRegNumber | LEGAL_ENTITY_TAX_REG_NUMBER | — | — |
| 65 | DetailTaxLineLegalMessageAppl2 | LEGAL_MESSAGE_APPL_2 | — | — |
| 66 | DetailTaxLineLegalMessageBasis | LEGAL_MESSAGE_BASIS | — | — |
| 67 | DetailTaxLineLegalMessageCalc | LEGAL_MESSAGE_CALC | — | — |
| 68 | DetailTaxLineLegalMessageExcpt | LEGAL_MESSAGE_EXCPT | — | — |
| 69 | DetailTaxLineLegalMessageExmpt | LEGAL_MESSAGE_EXMPT | — | — |
| 70 | DetailTaxLineLegalMessagePos | LEGAL_MESSAGE_POS | — | — |
| 71 | DetailTaxLineLegalMessageRate | LEGAL_MESSAGE_RATE | — | — |
| 72 | DetailTaxLineLegalMessageStatus | LEGAL_MESSAGE_STATUS | — | — |
| 73 | DetailTaxLineLegalMessageThreshold | LEGAL_MESSAGE_THRESHOLD | — | — |
| 74 | DetailTaxLineLegalMessageTrn | LEGAL_MESSAGE_TRN | — | — |
| 75 | DetailTaxLineLegalReportingStatus | LEGAL_REPORTING_STATUS | — | — |
| 76 | DetailTaxLineLineAmt | LINE_AMT | — | — |
| 77 | DetailTaxLineLineAssessableValue | LINE_ASSESSABLE_VALUE | — | — |
| 78 | DetailTaxLineMrcLinkToTaxLineId | MRC_LINK_TO_TAX_LINE_ID | — | — |
| 79 | DetailTaxLineMrcTaxLineFlag | MRC_TAX_LINE_FLAG | — | — |
| 80 | DetailTaxLineMultipleJurisdictionsFlag | MULTIPLE_JURISDICTIONS_FLAG | — | — |
| 81 | DetailTaxLineNrecTaxAmtTaxCurr | NREC_TAX_AMT_TAX_CURR | — | — |
| 82 | DetailTaxLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 83 | DetailTaxLineOffsetFlag | OFFSET_FLAG | — | — |
| 84 | DetailTaxLineOffsetLinkToTaxLineId | OFFSET_LINK_TO_TAX_LINE_ID | — | — |
| 85 | DetailTaxLineOrigSelfAssessedFlag | ORIG_SELF_ASSESSED_FLAG | — | — |
| 86 | DetailTaxLineOrigTaxAmtIncludedFlag | ORIG_TAX_AMT_INCLUDED_FLAG | — | — |
| 87 | DetailTaxLineOrigTaxAmtTaxCurr | ORIG_TAX_AMT_TAX_CURR | — | — |
| 88 | DetailTaxLineOrigTaxJurisdictionCode | ORIG_TAX_JURISDICTION_CODE | — | — |
| 89 | DetailTaxLineOrigTaxRate | ORIG_TAX_RATE | — | — |
| 90 | DetailTaxLineOrigTaxRateCode | ORIG_TAX_RATE_CODE | — | — |
| 91 | DetailTaxLineOrigTaxRateId | ORIG_TAX_RATE_ID | — | — |
| 92 | DetailTaxLineOrigTaxStatusCode | ORIG_TAX_STATUS_CODE | — | — |
| 93 | DetailTaxLineOrigTaxStatusId | ORIG_TAX_STATUS_ID | — | — |
| 94 | DetailTaxLineOrigTaxableAmtTaxCurr | ORIG_TAXABLE_AMT_TAX_CURR | — | — |
| 95 | DetailTaxLineOtherDocLineAmt | OTHER_DOC_LINE_AMT | — | — |
| 96 | DetailTaxLineOtherDocSource | OTHER_DOC_SOURCE | — | — |
| 97 | DetailTaxLineOverriddenFlag | OVERRIDDEN_FLAG | — | — |
| 98 | DetailTaxLinePlaceOfSupply | PLACE_OF_SUPPLY | — | — |
| 99 | DetailTaxLinePlaceOfSupplyResultId | PLACE_OF_SUPPLY_RESULT_ID | — | — |
| 100 | DetailTaxLinePlaceOfSupplyTypeCode | PLACE_OF_SUPPLY_TYPE_CODE | — | — |
| 101 | DetailTaxLinePrdTotalTaxAmtTaxCurr | PRD_TOTAL_TAX_AMT_TAX_CURR | — | — |
| 102 | DetailTaxLinePrecision | PRECISION | — | — |
| 103 | DetailTaxLineProcessForRecoveryFlag | PROCESS_FOR_RECOVERY_FLAG | — | — |
| 104 | DetailTaxLineProrationCode | PRORATION_CODE | — | — |
| 105 | DetailTaxLineRateResultId | RATE_RESULT_ID | — | — |
| 106 | DetailTaxLineRecTaxAmt | REC_TAX_AMT | — | — |
| 107 | DetailTaxLineRecalcRequiredFlag | RECALC_REQUIRED_FLAG | — | — |
| 108 | DetailTaxLineRecordTypeCode | RECORD_TYPE_CODE | — | — |
| 109 | DetailTaxLineRefDocApplicationId | REF_DOC_APPLICATION_ID | — | — |
| 110 | DetailTaxLineRefDocEntityCode | REF_DOC_ENTITY_CODE | — | — |
| 111 | DetailTaxLineRefDocEventClassCode | REF_DOC_EVENT_CLASS_CODE | — | — |
| 112 | DetailTaxLineRefDocLineId | REF_DOC_LINE_ID | — | — |
| 113 | DetailTaxLineRefDocLineQuantity | REF_DOC_LINE_QUANTITY | — | — |
| 114 | DetailTaxLineRegistrationPartyType | REGISTRATION_PARTY_TYPE | — | — |
| 115 | DetailTaxLineRelatedDocApplicationId | RELATED_DOC_APPLICATION_ID | — | — |
| 116 | DetailTaxLineRelatedDocDate | RELATED_DOC_DATE | — | — |
| 117 | DetailTaxLineRelatedDocEntityCode | RELATED_DOC_ENTITY_CODE | — | — |
| 118 | DetailTaxLineRelatedDocEventClassCode | RELATED_DOC_EVENT_CLASS_CODE | — | — |
| 119 | DetailTaxLineRelatedDocTrxId | RELATED_DOC_TRX_ID | — | — |
| 120 | DetailTaxLineRelatedDocTrxLevelType | RELATED_DOC_TRX_LEVEL_TYPE | — | — |
| 121 | DetailTaxLineReportingCurrencyCode | REPORTING_CURRENCY_CODE | — | ✅ |
| 122 | DetailTaxLineReportingOnlyFlag | REPORTING_ONLY_FLAG | — | — |
| 123 | DetailTaxLineReportingPeriodId | REPORTING_PERIOD_ID | — | — |
| 124 | DetailTaxLineReversedTaxLineId | REVERSED_TAX_LINE_ID | — | — |
| 125 | DetailTaxLineRoundingLvlPartyType | ROUNDING_LVL_PARTY_TYPE | — | — |
| 126 | DetailTaxLineRoundingRuleCode | ROUNDING_RULE_CODE | — | — |
| 127 | DetailTaxLineSelfAssessedFlag | SELF_ASSESSED_FLAG | — | ✅ |
| 128 | DetailTaxLineStatusResultId | STATUS_RESULT_ID | — | — |
| 129 | DetailTaxLineSummaryTaxLineId | SUMMARY_TAX_LINE_ID | — | — |
| 130 | DetailTaxLineTaxAmt | TAX_AMT | — | ✅ |
| 131 | DetailTaxLineTaxAmtFunclCurr | TAX_AMT_FUNCL_CURR | — | ✅ |
| 132 | DetailTaxLineTaxAmtIncludedFlag | TAX_AMT_INCLUDED_FLAG | — | ✅ |
| 133 | DetailTaxLineTaxAmtTaxCurr | TAX_AMT_TAX_CURR | — | ✅ |
| 134 | DetailTaxLineTaxApplicabilityResultId | TAX_APPLICABILITY_RESULT_ID | — | — |
| 135 | DetailTaxLineTaxApportionmentFlag | TAX_APPORTIONMENT_FLAG | — | — |
| 136 | DetailTaxLineTaxApportionmentLineNumber | TAX_APPORTIONMENT_LINE_NUMBER | — | — |
| 137 | DetailTaxLineTaxBaseModifierRate | TAX_BASE_MODIFIER_RATE | — | — |
| 138 | DetailTaxLineTaxCalculationFormula | TAX_CALCULATION_FORMULA | — | — |
| 139 | DetailTaxLineTaxCode | TAX_CODE | — | — |
| 140 | DetailTaxLineTaxCurrencyCode | TAX_CURRENCY_CODE | — | ✅ |
| 141 | DetailTaxLineTaxCurrencyConversionDate | TAX_CURRENCY_CONVERSION_DATE | — | — |
| 142 | DetailTaxLineTaxCurrencyConversionRate | TAX_CURRENCY_CONVERSION_RATE | — | — |
| 143 | DetailTaxLineTaxCurrencyConversionType | TAX_CURRENCY_CONVERSION_TYPE | — | — |
| 144 | DetailTaxLineTaxDate | TAX_DATE | — | — |
| 145 | DetailTaxLineTaxDateRuleId | TAX_DATE_RULE_ID | — | — |
| 146 | DetailTaxLineTaxDetermineDate | TAX_DETERMINE_DATE | — | — |
| 147 | DetailTaxLineTaxEventClassCode | TAX_EVENT_CLASS_CODE | — | — |
| 148 | DetailTaxLineTaxEventTypeCode | TAX_EVENT_TYPE_CODE | — | — |
| 149 | DetailTaxLineTaxExceptionId | TAX_EXCEPTION_ID | — | — |
| 150 | DetailTaxLineTaxExemptionId | TAX_EXEMPTION_ID | — | — |
| 151 | DetailTaxLineTaxHoldCode | TAX_HOLD_CODE | — | — |
| 152 | DetailTaxLineTaxHoldReleasedCode | TAX_HOLD_RELEASED_CODE | — | — |
| 153 | DetailTaxLineTaxId | TAX_ID | — | ✅ |
| 154 | DetailTaxLineTaxJurisdictionCode | TAX_JURISDICTION_CODE | — | ✅ |
| 155 | DetailTaxLineTaxJurisdictionId | TAX_JURISDICTION_ID | — | ✅ |
| 156 | DetailTaxLineTaxLineId1 | TAX_LINE_ID | — | — |
| 157 | DetailTaxLineTaxLineNumber | TAX_LINE_NUMBER | — | — |
| 158 | DetailTaxLineTaxOnlyLineFlag | TAX_ONLY_LINE_FLAG | — | ✅ |
| 159 | DetailTaxLineTaxPointBasis | TAX_POINT_BASIS | — | — |
| 160 | DetailTaxLineTaxPointDate | TAX_POINT_DATE | — | — |
| 161 | DetailTaxLineTaxProviderId | TAX_PROVIDER_ID | — | — |
| 162 | DetailTaxLineTaxRate | TAX_RATE | — | ✅ |
| 163 | DetailTaxLineTaxRateBeforeException | TAX_RATE_BEFORE_EXCEPTION | — | — |
| 164 | DetailTaxLineTaxRateBeforeExemption | TAX_RATE_BEFORE_EXEMPTION | — | — |
| 165 | DetailTaxLineTaxRateCode | TAX_RATE_CODE | — | ✅ |
| 166 | DetailTaxLineTaxRateId | TAX_RATE_ID | — | ✅ |
| 167 | DetailTaxLineTaxRateNameBeforeException | TAX_RATE_NAME_BEFORE_EXCEPTION | — | — |
| 168 | DetailTaxLineTaxRateNameBeforeExemption | TAX_RATE_NAME_BEFORE_EXEMPTION | — | — |
| 169 | DetailTaxLineTaxRateType | TAX_RATE_TYPE | — | — |
| 170 | DetailTaxLineTaxRegNumDetResultId | TAX_REG_NUM_DET_RESULT_ID | — | — |
| 171 | DetailTaxLineTaxRegimeCode | TAX_REGIME_CODE | — | ✅ |
| 172 | DetailTaxLineTaxRegimeId | TAX_REGIME_ID | — | ✅ |
| 173 | DetailTaxLineTaxRegimeTemplateId | TAX_REGIME_TEMPLATE_ID | — | — |
| 174 | DetailTaxLineTaxRegistrationId | TAX_REGISTRATION_ID | — | — |
| 175 | DetailTaxLineTaxRegistrationNumber | TAX_REGISTRATION_NUMBER | — | — |
| 176 | DetailTaxLineTaxStatusCode | TAX_STATUS_CODE | — | — |
| 177 | DetailTaxLineTaxStatusId | TAX_STATUS_ID | — | ✅ |
| 178 | DetailTaxLineTaxTypeCode | TAX_TYPE_CODE | — | — |
| 179 | DetailTaxLineTaxableAmt | TAXABLE_AMT | — | — |
| 180 | DetailTaxLineTaxableAmtFunclCurr | TAXABLE_AMT_FUNCL_CURR | — | — |
| 181 | DetailTaxLineTaxableAmtTaxCurr | TAXABLE_AMT_TAX_CURR | — | — |
| 182 | DetailTaxLineTaxableBasisFormula | TAXABLE_BASIS_FORMULA | — | — |
| 183 | DetailTaxLineTaxingJurisGeographyId | TAXING_JURIS_GEOGRAPHY_ID | — | — |
| 184 | DetailTaxLineThreshResultId | THRESH_RESULT_ID | — | — |
| 185 | DetailTaxLineTrxCurrencyCode | TRX_CURRENCY_CODE | — | — |
| 186 | DetailTaxLineTrxDate | TRX_DATE | — | — |
| 187 | DetailTaxLineTrxId | TRX_ID | — | — |
| 188 | DetailTaxLineTrxLevelType | TRX_LEVEL_TYPE | — | — |
| 189 | DetailTaxLineTrxLineDate | TRX_LINE_DATE | — | — |
| 190 | DetailTaxLineTrxLineId | TRX_LINE_ID | — | — |
| 191 | DetailTaxLineTrxLineIndex | TRX_LINE_INDEX | — | — |
| 192 | DetailTaxLineTrxLineNumber | TRX_LINE_NUMBER | — | — |
| 193 | DetailTaxLineTrxLineQuantity | TRX_LINE_QUANTITY | — | — |
| 194 | DetailTaxLineTrxNumber | TRX_NUMBER | — | — |
| 195 | DetailTaxLineUnitPrice | UNIT_PRICE | — | — |
| 196 | DetailTaxLineUnroundedTaxAmt | UNROUNDED_TAX_AMT | — | — |
| 197 | DetailTaxLineUnroundedTaxableAmt | UNROUNDED_TAXABLE_AMT | — | — |
| 198 | TaxLineId | TAX_LINE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
