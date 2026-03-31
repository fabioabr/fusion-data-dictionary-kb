---
id: DOC-GL-PVO-AccrualPlanPVO
doc_type: system-doc
title: "AccrualPlanPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - AccrualPlanPVO
  - accrualplanpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AccrualPlanPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Accrual Plan. Acessa as tabelas: ANC_ABSENCE_PLANS_F, ANC_ABSENCE_PLANS_F_TL, ANC_ACCRUAL_BANDS_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GlobalAbsencesAM.AccrualPlanPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 440 | 3 | 3 | 21 | 5% |

---

## 🔗 Tabelas Relacionadas

- [[anc_absence_plans_f|ANC_ABSENCE_PLANS_F]] — 259 atributos (3 PKs, 14 BICC)
- [[anc_absence_plans_f_tl|ANC_ABSENCE_PLANS_F_TL]] — 15 atributos (3 BICC)
- [[anc_accrual_bands_f|ANC_ACCRUAL_BANDS_F]] — 166 atributos (4 BICC)

---

## ⚙️ Atributos

### [[anc_absence_plans_f|ANC_ABSENCE_PLANS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsenceDurationDefnId | ABSENCE_DURATION_DEFN_ID | — | — |
| 2 | AbsenceDurationFormulaId | ABSENCE_DURATION_FORMULA_ID | — | — |
| 3 | AbsencePlanId | ABSENCE_PLAN_ID | 🔑 | ✅ |
| 4 | AccDefinitionType | ACC_DEFINITION_TYPE | — | — |
| 5 | AccFormulaId | ACC_FORMULA_ID | — | — |
| 6 | AccNegativeBalFlag | ACC_NEGATIVE_BAL_FLAG | — | — |
| 7 | AccNegativeBalLimit | ACC_NEGATIVE_BAL_LIMIT | — | — |
| 8 | AccNegativeBalUom | ACC_NEGATIVE_BAL_UOM | — | — |
| 9 | AccPeriodFrequency | ACC_PERIOD_FREQUENCY | — | — |
| 10 | AccPeriodPayrollFreqId | ACC_PERIOD_PAYROLL_FREQ_ID | — | — |
| 11 | AccPeriodWfmCaledarId | ACC_PERIOD_WFM_CALEDAR_ID | — | — |
| 12 | AccrualMethodCd | ACCRUAL_METHOD_CD | — | ✅ |
| 13 | AccrualMode | ACCRUAL_MODE | — | — |
| 14 | AccrualPlanDPEODonationType | DONATION_TYPE | — | — |
| 15 | AccrualVestingCd | ACCRUAL_VESTING_CD | — | ✅ |
| 16 | AncAbsencePlansFAltcd | ANC_ABSENCE_PLANS_F_ALTCD | — | — |
| 17 | AncChar1 | ANC_CHAR1 | — | — |
| 18 | AncChar2 | ANC_CHAR2 | — | — |
| 19 | AncChar3 | ANC_CHAR3 | — | — |
| 20 | AncChar4 | ANC_CHAR4 | — | — |
| 21 | AncChar5 | ANC_CHAR5 | — | — |
| 22 | AncDate1 | ANC_DATE1 | — | — |
| 23 | AncDate2 | ANC_DATE2 | — | — |
| 24 | AncDate3 | ANC_DATE3 | — | — |
| 25 | AncDate4 | ANC_DATE4 | — | — |
| 26 | AncDate5 | ANC_DATE5 | — | — |
| 27 | AncNumber1 | ANC_NUMBER1 | — | — |
| 28 | AncNumber2 | ANC_NUMBER2 | — | — |
| 29 | AncNumber3 | ANC_NUMBER3 | — | — |
| 30 | AncNumber4 | ANC_NUMBER4 | — | — |
| 31 | AncNumber5 | ANC_NUMBER5 | — | — |
| 32 | AnniversaryEventFormulaId | ANNIVERSARY_EVENT_FORMULA_ID | — | — |
| 33 | AnniversaryEventRule | ANNIVERSARY_EVENT_RULE | — | — |
| 34 | Attribute1 | ATTRIBUTE1 | — | — |
| 35 | Attribute10 | ATTRIBUTE10 | — | — |
| 36 | Attribute11 | ATTRIBUTE11 | — | — |
| 37 | Attribute12 | ATTRIBUTE12 | — | — |
| 38 | Attribute13 | ATTRIBUTE13 | — | — |
| 39 | Attribute14 | ATTRIBUTE14 | — | — |
| 40 | Attribute15 | ATTRIBUTE15 | — | — |
| 41 | Attribute16 | ATTRIBUTE16 | — | — |
| 42 | Attribute17 | ATTRIBUTE17 | — | — |
| 43 | Attribute18 | ATTRIBUTE18 | — | — |
| 44 | Attribute19 | ATTRIBUTE19 | — | — |
| 45 | Attribute2 | ATTRIBUTE2 | — | — |
| 46 | Attribute20 | ATTRIBUTE20 | — | — |
| 47 | Attribute21 | ATTRIBUTE21 | — | — |
| 48 | Attribute22 | ATTRIBUTE22 | — | — |
| 49 | Attribute23 | ATTRIBUTE23 | — | — |
| 50 | Attribute24 | ATTRIBUTE24 | — | — |
| 51 | Attribute25 | ATTRIBUTE25 | — | — |
| 52 | Attribute26 | ATTRIBUTE26 | — | — |
| 53 | Attribute27 | ATTRIBUTE27 | — | — |
| 54 | Attribute28 | ATTRIBUTE28 | — | — |
| 55 | Attribute29 | ATTRIBUTE29 | — | — |
| 56 | Attribute3 | ATTRIBUTE3 | — | — |
| 57 | Attribute30 | ATTRIBUTE30 | — | — |
| 58 | Attribute4 | ATTRIBUTE4 | — | — |
| 59 | Attribute5 | ATTRIBUTE5 | — | — |
| 60 | Attribute6 | ATTRIBUTE6 | — | — |
| 61 | Attribute7 | ATTRIBUTE7 | — | — |
| 62 | Attribute8 | ATTRIBUTE8 | — | — |
| 63 | Attribute9 | ATTRIBUTE9 | — | — |
| 64 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 65 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 66 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 67 | AttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 68 | AttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 69 | AttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 70 | AttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 71 | AttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 72 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 73 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 74 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 75 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 76 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 77 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 78 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 79 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 80 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 81 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 82 | AttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 83 | AttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 84 | AttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 85 | AttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 86 | AttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 87 | AttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 88 | AttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 89 | AttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 90 | AttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 91 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 92 | AttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 93 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 94 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 95 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 96 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 97 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 98 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 99 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 100 | BalanceTransferFlag | BALANCE_TRANSFER_FLAG | — | — |
| 101 | CalendarStartDay | CALENDAR_START_DAY | — | — |
| 102 | CalendarStartMonth | CALENDAR_START_MONTH | — | — |
| 103 | CarryOverExpiredFlag | CARRY_OVER_EXPIRED_FLAG | — | — |
| 104 | CarryOverExpiredUnits | CARRY_OVER_EXPIRED_UNITS | — | ✅ |
| 105 | CarryOverExpiredUom | CARRY_OVER_EXPIRED_UOM | — | ✅ |
| 106 | CarryOverFlatAmt | CARRY_OVER_FLAT_AMT | — | ✅ |
| 107 | CarryOverFormulaId | CARRY_OVER_FORMULA_ID | — | — |
| 108 | CarryOverProrateFormulaId | CARRY_OVER_PRORATE_FORMULA_ID | — | — |
| 109 | CarryOverProrateRule | CARRY_OVER_PRORATE_RULE | — | — |
| 110 | CarryOverRule | CARRY_OVER_RULE | — | — |
| 111 | CashOutFlag | CASH_OUT_FLAG | — | — |
| 112 | CashoutRateFormulaId | CASHOUT_RATE_FORMULA_ID | — | — |
| 113 | CashoutRateId | CASHOUT_RATE_ID | — | — |
| 114 | CashoutRateRule | CASHOUT_RATE_RULE | — | — |
| 115 | CeilLimitFlatAmt | CEIL_LIMIT_FLAT_AMT | — | ✅ |
| 116 | CeilLimitFormulaId | CEIL_LIMIT_FORMULA_ID | — | — |
| 117 | CeilLimitProrateRule | CEIL_LIMIT_PRORATE_RULE | — | — |
| 118 | CeilLimitRule | CEIL_LIMIT_RULE | — | — |
| 119 | CeilLmtProrateFormulaId | CEIL_LMT_PRORATE_FORMULA_ID | — | — |
| 120 | CompExpAdjrsn | COMP_EXP_ADJRSN | — | — |
| 121 | CompMnulAdjrsn | COMP_MNUL_ADJRSN | — | — |
| 122 | CreatedBy | CREATED_BY | — | — |
| 123 | CreationDate | CREATION_DATE | — | — |
| 124 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 125 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 126 | EmpEnrlNegativeBalanceFlag | EMP_ENRL_NEGATIVE_BALANCE_FLAG | — | — |
| 127 | EmpEnrlPositiveBalanceFlag | EMP_ENRL_POSITIVE_BALANCE_FLAG | — | — |
| 128 | EmpEnrlTerminateEntlFlag | EMP_ENRL_TERMINATE_ENTL_FLAG | — | — |
| 129 | EnrollNegativeBalanceFlag | ENROLL_NEGATIVE_BALANCE_FLAG | — | — |
| 130 | EnrollPositiveBalanceFlag | ENROLL_POSITIVE_BALANCE_FLAG | — | — |
| 131 | EnrollTerminateEntlFlag | ENROLL_TERMINATE_ENTL_FLAG | — | — |
| 132 | EnrollmentEndFormulaId | ENROLLMENT_END_FORMULA_ID | — | — |
| 133 | EnrollmentEndRule | ENROLLMENT_END_RULE | — | — |
| 134 | EnrollmentStartFormulaId | ENROLLMENT_START_FORMULA_ID | — | — |
| 135 | EnrollmentStartRule | ENROLLMENT_START_RULE | — | — |
| 136 | EnterpriseId | ENTERPRISE_ID | — | — |
| 137 | EntitlementEndFormulaId | ENTITLEMENT_END_FORMULA_ID | — | — |
| 138 | EntitlementEndRule | ENTITLEMENT_END_RULE | — | — |
| 139 | EntitlementStartDate | ENTITLEMENT_START_DATE | — | — |
| 140 | EntlDefinitionType | ENTL_DEFINITION_TYPE | — | — |
| 141 | EntlFormulaId | ENTL_FORMULA_ID | — | — |
| 142 | EntlMethodCd | ENTL_METHOD_CD | — | ✅ |
| 143 | ExpirationActionCd | EXPIRATION_ACTION_CD | — | — |
| 144 | ExpirationLimit | EXPIRATION_LIMIT | — | — |
| 145 | ExpirationTermCd | EXPIRATION_TERM_CD | — | — |
| 146 | ExpirationUomCd | EXPIRATION_UOM_CD | — | — |
| 147 | Information1 | INFORMATION1 | — | — |
| 148 | Information10 | INFORMATION10 | — | — |
| 149 | Information11 | INFORMATION11 | — | — |
| 150 | Information12 | INFORMATION12 | — | — |
| 151 | Information13 | INFORMATION13 | — | — |
| 152 | Information14 | INFORMATION14 | — | — |
| 153 | Information15 | INFORMATION15 | — | — |
| 154 | Information16 | INFORMATION16 | — | — |
| 155 | Information17 | INFORMATION17 | — | — |
| 156 | Information18 | INFORMATION18 | — | — |
| 157 | Information19 | INFORMATION19 | — | — |
| 158 | Information2 | INFORMATION2 | — | — |
| 159 | Information20 | INFORMATION20 | — | — |
| 160 | Information21 | INFORMATION21 | — | — |
| 161 | Information22 | INFORMATION22 | — | — |
| 162 | Information23 | INFORMATION23 | — | — |
| 163 | Information24 | INFORMATION24 | — | — |
| 164 | Information25 | INFORMATION25 | — | — |
| 165 | Information26 | INFORMATION26 | — | — |
| 166 | Information27 | INFORMATION27 | — | — |
| 167 | Information28 | INFORMATION28 | — | — |
| 168 | Information29 | INFORMATION29 | — | — |
| 169 | Information3 | INFORMATION3 | — | — |
| 170 | Information30 | INFORMATION30 | — | — |
| 171 | Information4 | INFORMATION4 | — | — |
| 172 | Information5 | INFORMATION5 | — | — |
| 173 | Information6 | INFORMATION6 | — | — |
| 174 | Information7 | INFORMATION7 | — | — |
| 175 | Information8 | INFORMATION8 | — | — |
| 176 | Information9 | INFORMATION9 | — | — |
| 177 | InformationCategory | INFORMATION_CATEGORY | — | — |
| 178 | InformationDate1 | INFORMATION_DATE1 | — | — |
| 179 | InformationDate10 | INFORMATION_DATE10 | — | — |
| 180 | InformationDate11 | INFORMATION_DATE11 | — | — |
| 181 | InformationDate12 | INFORMATION_DATE12 | — | — |
| 182 | InformationDate13 | INFORMATION_DATE13 | — | — |
| 183 | InformationDate14 | INFORMATION_DATE14 | — | — |
| 184 | InformationDate15 | INFORMATION_DATE15 | — | — |
| 185 | InformationDate2 | INFORMATION_DATE2 | — | — |
| 186 | InformationDate3 | INFORMATION_DATE3 | — | — |
| 187 | InformationDate4 | INFORMATION_DATE4 | — | — |
| 188 | InformationDate5 | INFORMATION_DATE5 | — | — |
| 189 | InformationDate6 | INFORMATION_DATE6 | — | — |
| 190 | InformationDate7 | INFORMATION_DATE7 | — | — |
| 191 | InformationDate8 | INFORMATION_DATE8 | — | — |
| 192 | InformationDate9 | INFORMATION_DATE9 | — | — |
| 193 | InformationNumber1 | INFORMATION_NUMBER1 | — | — |
| 194 | InformationNumber10 | INFORMATION_NUMBER10 | — | — |
| 195 | InformationNumber11 | INFORMATION_NUMBER11 | — | — |
| 196 | InformationNumber12 | INFORMATION_NUMBER12 | — | — |
| 197 | InformationNumber13 | INFORMATION_NUMBER13 | — | — |
| 198 | InformationNumber14 | INFORMATION_NUMBER14 | — | — |
| 199 | InformationNumber15 | INFORMATION_NUMBER15 | — | — |
| 200 | InformationNumber16 | INFORMATION_NUMBER16 | — | — |
| 201 | InformationNumber17 | INFORMATION_NUMBER17 | — | — |
| 202 | InformationNumber18 | INFORMATION_NUMBER18 | — | — |
| 203 | InformationNumber19 | INFORMATION_NUMBER19 | — | — |
| 204 | InformationNumber2 | INFORMATION_NUMBER2 | — | — |
| 205 | InformationNumber20 | INFORMATION_NUMBER20 | — | — |
| 206 | InformationNumber3 | INFORMATION_NUMBER3 | — | — |
| 207 | InformationNumber4 | INFORMATION_NUMBER4 | — | — |
| 208 | InformationNumber5 | INFORMATION_NUMBER5 | — | — |
| 209 | InformationNumber6 | INFORMATION_NUMBER6 | — | — |
| 210 | InformationNumber7 | INFORMATION_NUMBER7 | — | — |
| 211 | InformationNumber8 | INFORMATION_NUMBER8 | — | — |
| 212 | InformationNumber9 | INFORMATION_NUMBER9 | — | — |
| 213 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 214 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 215 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 216 | LegislationCode | LEGISLATION_CODE | — | — |
| 217 | LegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 218 | LiabilityRateFormulaId | LIABILITY_RATE_FORMULA_ID | — | — |
| 219 | LiabilityRateId | LIABILITY_RATE_ID | — | — |
| 220 | LiabilityRateRule | LIABILITY_RATE_RULE | — | — |
| 221 | ModuleId | MODULE_ID | — | — |
| 222 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 223 | OtherAdjustmentFlag | OTHER_ADJUSTMENT_FLAG | — | — |
| 224 | OtherReasons | OTHER_REASONS | — | — |
| 225 | OverlapCd | OVERLAP_CD | — | — |
| 226 | PartialAccrualFormulaId | PARTIAL_ACCRUAL_FORMULA_ID | — | — |
| 227 | PayAdvancesFlag | PAY_ADVANCES_FLAG | — | — |
| 228 | PayRateFactor | PAY_RATE_FACTOR | — | — |
| 229 | PayoutRateFormulaId | PAYOUT_RATE_FORMULA_ID | — | — |
| 230 | PayoutRateId | PAYOUT_RATE_ID | — | — |
| 231 | PayoutRateRule | PAYOUT_RATE_RULE | — | — |
| 232 | PayrollImpactFlag | PAYROLL_IMPACT_FLAG | — | — |
| 233 | PayrollMappingId | PAYROLL_MAPPING_ID | — | — |
| 234 | PeriodUom | PERIOD_UOM | — | — |
| 235 | PlanActivationFlag | PLAN_ACTIVATION_FLAG | — | — |
| 236 | PlanMgmtCd | PLAN_MGMT_CD | — | — |
| 237 | PlanPeriodId | PLAN_PERIOD_ID | — | — |
| 238 | PlanPeriodType | PLAN_PERIOD_TYPE | — | ✅ |
| 239 | PlanStatus | PLAN_STATUS | — | ✅ |
| 240 | PlanUom | PLAN_UOM | — | ✅ |
| 241 | PlanUseFormulaId | PLAN_USE_FORMULA_ID | — | — |
| 242 | PlanUseRateId | PLAN_USE_RATE_ID | — | — |
| 243 | PlanUseRateRule | PLAN_USE_RATE_RULE | — | — |
| 244 | PrevEmpEntlFlag | PREV_EMP_ENTL_FLAG | — | — |
| 245 | PrevEmpUsageFlag | PREV_EMP_USAGE_FLAG | — | — |
| 246 | ProcessingLevelCd | PROCESSING_LEVEL_CD | — | — |
| 247 | ProrationFormulaId | PRORATION_FORMULA_ID | — | — |
| 248 | ProrationRule | PRORATION_RULE | — | — |
| 249 | RollBackwardEndFormulaId | ROLL_BACKWARD_END_FORMULA_ID | — | — |
| 250 | RollBackwardEndRule | ROLL_BACKWARD_END_RULE | — | — |
| 251 | RollForwardStartFormulaId | ROLL_FORWARD_START_FORMULA_ID | — | — |
| 252 | RollForwardStartRule | ROLL_FORWARD_START_RULE | — | — |
| 253 | RollPeriodDuration | ROLL_PERIOD_DURATION | — | — |
| 254 | StatutoryFlag | STATUTORY_FLAG | — | — |
| 255 | VestingPeriodDuration | VESTING_PERIOD_DURATION | — | — |
| 256 | VestingPeriodFormulaId | VESTING_PERIOD_FORMULA_ID | — | — |
| 257 | VestingPeriodUom | VESTING_PERIOD_UOM | — | — |
| 258 | WaitPeriodDurUnits | WAIT_PERIOD_DUR_UNITS | — | — |
| 259 | WaitPeriodDurUom | WAIT_PERIOD_DUR_UOM | — | — |

### [[anc_absence_plans_f_tl|ANC_ABSENCE_PLANS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsencePlanId1 | ABSENCE_PLAN_ID | — | — |
| 2 | CreatedBy1 | CREATED_BY | — | — |
| 3 | CreationDate1 | CREATION_DATE | — | — |
| 4 | Description | DESCRIPTION | — | — |
| 5 | EffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 6 | EffectiveStartDate1 | EFFECTIVE_START_DATE | — | ✅ |
| 7 | EnterpriseId1 | ENTERPRISE_ID | — | — |
| 8 | Language | LANGUAGE | — | — |
| 9 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 11 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 12 | ModuleId1 | MODULE_ID | — | — |
| 13 | Name | NAME | — | ✅ |
| 14 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 15 | SourceLang | SOURCE_LANG | — | — |

### [[anc_accrual_bands_f|ANC_ACCRUAL_BANDS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsencePlanId2 | ABSENCE_PLAN_ID | — | — |
| 2 | AccBandSequence | ACC_BAND_SEQUENCE | — | ✅ |
| 3 | AccCarryoverLimit | ACC_CARRYOVER_LIMIT | — | — |
| 4 | AccInputExpression | ACC_INPUT_EXPRESSION | — | — |
| 5 | AccOutputFormulaId | ACC_OUTPUT_FORMULA_ID | — | — |
| 6 | AccrualBandId | ACCRUAL_BAND_ID | — | — |
| 7 | AccrualCeiling | ACCRUAL_CEILING | — | — |
| 8 | AccrualRate | ACCRUAL_RATE | — | ✅ |
| 9 | AncAccrualBandsFAltcd | ANC_ACCRUAL_BANDS_F_ALTCD | — | — |
| 10 | AncChar11 | ANC_CHAR1 | — | — |
| 11 | AncChar21 | ANC_CHAR2 | — | — |
| 12 | AncChar31 | ANC_CHAR3 | — | — |
| 13 | AncChar41 | ANC_CHAR4 | — | — |
| 14 | AncChar51 | ANC_CHAR5 | — | — |
| 15 | AncDate11 | ANC_DATE1 | — | — |
| 16 | AncDate21 | ANC_DATE2 | — | — |
| 17 | AncDate31 | ANC_DATE3 | — | — |
| 18 | AncDate41 | ANC_DATE4 | — | — |
| 19 | AncDate51 | ANC_DATE5 | — | — |
| 20 | AncNumber11 | ANC_NUMBER1 | — | — |
| 21 | AncNumber21 | ANC_NUMBER2 | — | — |
| 22 | AncNumber31 | ANC_NUMBER3 | — | — |
| 23 | AncNumber41 | ANC_NUMBER4 | — | — |
| 24 | AncNumber51 | ANC_NUMBER5 | — | — |
| 25 | Attribute101 | ATTRIBUTE10 | — | — |
| 26 | Attribute110 | ATTRIBUTE1 | — | — |
| 27 | Attribute111 | ATTRIBUTE11 | — | — |
| 28 | Attribute121 | ATTRIBUTE12 | — | — |
| 29 | Attribute131 | ATTRIBUTE13 | — | — |
| 30 | Attribute141 | ATTRIBUTE14 | — | — |
| 31 | Attribute151 | ATTRIBUTE15 | — | — |
| 32 | Attribute161 | ATTRIBUTE16 | — | — |
| 33 | Attribute171 | ATTRIBUTE17 | — | — |
| 34 | Attribute181 | ATTRIBUTE18 | — | — |
| 35 | Attribute191 | ATTRIBUTE19 | — | — |
| 36 | Attribute201 | ATTRIBUTE20 | — | — |
| 37 | Attribute210 | ATTRIBUTE2 | — | — |
| 38 | Attribute211 | ATTRIBUTE21 | — | — |
| 39 | Attribute221 | ATTRIBUTE22 | — | — |
| 40 | Attribute231 | ATTRIBUTE23 | — | — |
| 41 | Attribute241 | ATTRIBUTE24 | — | — |
| 42 | Attribute251 | ATTRIBUTE25 | — | — |
| 43 | Attribute261 | ATTRIBUTE26 | — | — |
| 44 | Attribute271 | ATTRIBUTE27 | — | — |
| 45 | Attribute281 | ATTRIBUTE28 | — | — |
| 46 | Attribute291 | ATTRIBUTE29 | — | — |
| 47 | Attribute301 | ATTRIBUTE30 | — | — |
| 48 | Attribute31 | ATTRIBUTE3 | — | — |
| 49 | Attribute41 | ATTRIBUTE4 | — | — |
| 50 | Attribute51 | ATTRIBUTE5 | — | — |
| 51 | Attribute61 | ATTRIBUTE6 | — | — |
| 52 | Attribute71 | ATTRIBUTE7 | — | — |
| 53 | Attribute81 | ATTRIBUTE8 | — | — |
| 54 | Attribute91 | ATTRIBUTE9 | — | — |
| 55 | AttributeCategory1 | ATTRIBUTE_CATEGORY | — | — |
| 56 | AttributeDate101 | ATTRIBUTE_DATE10 | — | — |
| 57 | AttributeDate111 | ATTRIBUTE_DATE11 | — | — |
| 58 | AttributeDate121 | ATTRIBUTE_DATE12 | — | — |
| 59 | AttributeDate131 | ATTRIBUTE_DATE13 | — | — |
| 60 | AttributeDate141 | ATTRIBUTE_DATE14 | — | — |
| 61 | AttributeDate151 | ATTRIBUTE_DATE15 | — | — |
| 62 | AttributeDate16 | ATTRIBUTE_DATE1 | — | — |
| 63 | AttributeDate21 | ATTRIBUTE_DATE2 | — | — |
| 64 | AttributeDate31 | ATTRIBUTE_DATE3 | — | — |
| 65 | AttributeDate41 | ATTRIBUTE_DATE4 | — | — |
| 66 | AttributeDate51 | ATTRIBUTE_DATE5 | — | — |
| 67 | AttributeDate61 | ATTRIBUTE_DATE6 | — | — |
| 68 | AttributeDate71 | ATTRIBUTE_DATE7 | — | — |
| 69 | AttributeDate81 | ATTRIBUTE_DATE8 | — | — |
| 70 | AttributeDate91 | ATTRIBUTE_DATE9 | — | — |
| 71 | AttributeNumber101 | ATTRIBUTE_NUMBER10 | — | — |
| 72 | AttributeNumber110 | ATTRIBUTE_NUMBER1 | — | — |
| 73 | AttributeNumber111 | ATTRIBUTE_NUMBER11 | — | — |
| 74 | AttributeNumber121 | ATTRIBUTE_NUMBER12 | — | — |
| 75 | AttributeNumber131 | ATTRIBUTE_NUMBER13 | — | — |
| 76 | AttributeNumber141 | ATTRIBUTE_NUMBER14 | — | — |
| 77 | AttributeNumber151 | ATTRIBUTE_NUMBER15 | — | — |
| 78 | AttributeNumber161 | ATTRIBUTE_NUMBER16 | — | — |
| 79 | AttributeNumber171 | ATTRIBUTE_NUMBER17 | — | — |
| 80 | AttributeNumber181 | ATTRIBUTE_NUMBER18 | — | — |
| 81 | AttributeNumber191 | ATTRIBUTE_NUMBER19 | — | — |
| 82 | AttributeNumber201 | ATTRIBUTE_NUMBER20 | — | — |
| 83 | AttributeNumber21 | ATTRIBUTE_NUMBER2 | — | — |
| 84 | AttributeNumber31 | ATTRIBUTE_NUMBER3 | — | — |
| 85 | AttributeNumber41 | ATTRIBUTE_NUMBER4 | — | — |
| 86 | AttributeNumber51 | ATTRIBUTE_NUMBER5 | — | — |
| 87 | AttributeNumber61 | ATTRIBUTE_NUMBER6 | — | — |
| 88 | AttributeNumber71 | ATTRIBUTE_NUMBER7 | — | — |
| 89 | AttributeNumber81 | ATTRIBUTE_NUMBER8 | — | — |
| 90 | AttributeNumber91 | ATTRIBUTE_NUMBER9 | — | — |
| 91 | CreatedBy2 | CREATED_BY | — | — |
| 92 | CreationDate2 | CREATION_DATE | — | — |
| 93 | EffectiveEndDate2 | EFFECTIVE_END_DATE | — | — |
| 94 | EffectiveStartDate2 | EFFECTIVE_START_DATE | — | ✅ |
| 95 | EnterpriseId2 | ENTERPRISE_ID | — | — |
| 96 | Information101 | INFORMATION10 | — | — |
| 97 | Information110 | INFORMATION1 | — | — |
| 98 | Information111 | INFORMATION11 | — | — |
| 99 | Information121 | INFORMATION12 | — | — |
| 100 | Information131 | INFORMATION13 | — | — |
| 101 | Information141 | INFORMATION14 | — | — |
| 102 | Information151 | INFORMATION15 | — | — |
| 103 | Information161 | INFORMATION16 | — | — |
| 104 | Information171 | INFORMATION17 | — | — |
| 105 | Information181 | INFORMATION18 | — | — |
| 106 | Information191 | INFORMATION19 | — | — |
| 107 | Information201 | INFORMATION20 | — | — |
| 108 | Information210 | INFORMATION2 | — | — |
| 109 | Information211 | INFORMATION21 | — | — |
| 110 | Information221 | INFORMATION22 | — | — |
| 111 | Information231 | INFORMATION23 | — | — |
| 112 | Information241 | INFORMATION24 | — | — |
| 113 | Information251 | INFORMATION25 | — | — |
| 114 | Information261 | INFORMATION26 | — | — |
| 115 | Information271 | INFORMATION27 | — | — |
| 116 | Information281 | INFORMATION28 | — | — |
| 117 | Information291 | INFORMATION29 | — | — |
| 118 | Information301 | INFORMATION30 | — | — |
| 119 | Information31 | INFORMATION3 | — | — |
| 120 | Information41 | INFORMATION4 | — | — |
| 121 | Information51 | INFORMATION5 | — | — |
| 122 | Information61 | INFORMATION6 | — | — |
| 123 | Information71 | INFORMATION7 | — | — |
| 124 | Information81 | INFORMATION8 | — | — |
| 125 | Information91 | INFORMATION9 | — | — |
| 126 | InformationCategory1 | INFORMATION_CATEGORY | — | — |
| 127 | InformationDate101 | INFORMATION_DATE10 | — | — |
| 128 | InformationDate111 | INFORMATION_DATE11 | — | — |
| 129 | InformationDate121 | INFORMATION_DATE12 | — | — |
| 130 | InformationDate131 | INFORMATION_DATE13 | — | — |
| 131 | InformationDate141 | INFORMATION_DATE14 | — | — |
| 132 | InformationDate151 | INFORMATION_DATE15 | — | — |
| 133 | InformationDate16 | INFORMATION_DATE1 | — | — |
| 134 | InformationDate21 | INFORMATION_DATE2 | — | — |
| 135 | InformationDate31 | INFORMATION_DATE3 | — | — |
| 136 | InformationDate41 | INFORMATION_DATE4 | — | — |
| 137 | InformationDate51 | INFORMATION_DATE5 | — | — |
| 138 | InformationDate61 | INFORMATION_DATE6 | — | — |
| 139 | InformationDate71 | INFORMATION_DATE7 | — | — |
| 140 | InformationDate81 | INFORMATION_DATE8 | — | — |
| 141 | InformationDate91 | INFORMATION_DATE9 | — | — |
| 142 | InformationNumber101 | INFORMATION_NUMBER10 | — | — |
| 143 | InformationNumber110 | INFORMATION_NUMBER1 | — | — |
| 144 | InformationNumber111 | INFORMATION_NUMBER11 | — | — |
| 145 | InformationNumber121 | INFORMATION_NUMBER12 | — | — |
| 146 | InformationNumber131 | INFORMATION_NUMBER13 | — | — |
| 147 | InformationNumber141 | INFORMATION_NUMBER14 | — | — |
| 148 | InformationNumber151 | INFORMATION_NUMBER15 | — | — |
| 149 | InformationNumber161 | INFORMATION_NUMBER16 | — | — |
| 150 | InformationNumber171 | INFORMATION_NUMBER17 | — | — |
| 151 | InformationNumber181 | INFORMATION_NUMBER18 | — | — |
| 152 | InformationNumber191 | INFORMATION_NUMBER19 | — | — |
| 153 | InformationNumber201 | INFORMATION_NUMBER20 | — | — |
| 154 | InformationNumber21 | INFORMATION_NUMBER2 | — | — |
| 155 | InformationNumber31 | INFORMATION_NUMBER3 | — | — |
| 156 | InformationNumber41 | INFORMATION_NUMBER4 | — | — |
| 157 | InformationNumber51 | INFORMATION_NUMBER5 | — | — |
| 158 | InformationNumber61 | INFORMATION_NUMBER6 | — | — |
| 159 | InformationNumber71 | INFORMATION_NUMBER7 | — | — |
| 160 | InformationNumber81 | INFORMATION_NUMBER8 | — | — |
| 161 | InformationNumber91 | INFORMATION_NUMBER9 | — | — |
| 162 | LastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 163 | LastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 164 | LastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 165 | ModuleId2 | MODULE_ID | — | — |
| 166 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
