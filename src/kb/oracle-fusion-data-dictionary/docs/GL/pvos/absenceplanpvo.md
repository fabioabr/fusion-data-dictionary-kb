---
id: DOC-GL-PVO-AbsencePlanPVO
doc_type: system-doc
title: "AbsencePlanPVO — PVO General Ledger"
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
  - AbsencePlanPVO
  - absenceplanpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AbsencePlanPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Absence Plan. Acessa as tabelas: ANC_ABSENCE_PLANS_F, ANC_ABSENCE_PLANS_F_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GlobalAbsencesAM.AbsencePlanPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 118 | 2 | 2 | 110 | 93% |

---

## 🔗 Tabelas Relacionadas

- [[anc_absence_plans_f|ANC_ABSENCE_PLANS_F]] — 103 atributos (1 PKs, 99 BICC)
- [[anc_absence_plans_f_tl|ANC_ABSENCE_PLANS_F_TL]] — 15 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[anc_absence_plans_f|ANC_ABSENCE_PLANS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsenceDurationDefnId | ABSENCE_DURATION_DEFN_ID | — | ✅ |
| 2 | AbsencePlanId | ABSENCE_PLAN_ID | 🔑 | ✅ |
| 3 | AccDefinitionType | ACC_DEFINITION_TYPE | — | ✅ |
| 4 | AccFormulaId | ACC_FORMULA_ID | — | ✅ |
| 5 | AccNegativeBalFlag | ACC_NEGATIVE_BAL_FLAG | — | ✅ |
| 6 | AccNegativeBalLimit | ACC_NEGATIVE_BAL_LIMIT | — | ✅ |
| 7 | AccNegativeBalUom | ACC_NEGATIVE_BAL_UOM | — | ✅ |
| 8 | AccPeriodFrequency | ACC_PERIOD_FREQUENCY | — | ✅ |
| 9 | AccPeriodPayrollFreqId | ACC_PERIOD_PAYROLL_FREQ_ID | — | ✅ |
| 10 | AccPeriodWfmCaledarId | ACC_PERIOD_WFM_CALEDAR_ID | — | ✅ |
| 11 | AccrualMethodCd | ACCRUAL_METHOD_CD | — | ✅ |
| 12 | AccrualMode | ACCRUAL_MODE | — | ✅ |
| 13 | AccrualVestingCD | ACCRUAL_VESTING_CD | — | ✅ |
| 14 | AncAbsencePlansFAltcd | ANC_ABSENCE_PLANS_F_ALTCD | — | ✅ |
| 15 | AnniversaryEventFormulaId | ANNIVERSARY_EVENT_FORMULA_ID | — | ✅ |
| 16 | AnniversaryEventRule | ANNIVERSARY_EVENT_RULE | — | ✅ |
| 17 | BalanceTransferFlag | BALANCE_TRANSFER_FLAG | — | ✅ |
| 18 | CalendarStartDay | CALENDAR_START_DAY | — | ✅ |
| 19 | CalendarStartMonth | CALENDAR_START_MONTH | — | ✅ |
| 20 | CarryOverExpiredFlag | CARRY_OVER_EXPIRED_FLAG | — | ✅ |
| 21 | CarryOverExpiredUnits | CARRY_OVER_EXPIRED_UNITS | — | ✅ |
| 22 | CarryOverExpiredUom | CARRY_OVER_EXPIRED_UOM | — | ✅ |
| 23 | CarryOverFlatAmt | CARRY_OVER_FLAT_AMT | — | ✅ |
| 24 | CarryOverFormulaId | CARRY_OVER_FORMULA_ID | — | ✅ |
| 25 | CarryOverProrateFormulaId | CARRY_OVER_PRORATE_FORMULA_ID | — | ✅ |
| 26 | CarryOverProrateRule | CARRY_OVER_PRORATE_RULE | — | ✅ |
| 27 | CarryOverRule | CARRY_OVER_RULE | — | ✅ |
| 28 | CashOutFlag | CASH_OUT_FLAG | — | ✅ |
| 29 | CashoutRateFormulaId | CASHOUT_RATE_FORMULA_ID | — | ✅ |
| 30 | CashoutRateId | CASHOUT_RATE_ID | — | ✅ |
| 31 | CashoutRateRule | CASHOUT_RATE_RULE | — | ✅ |
| 32 | CeilLimitFlatAmt | CEIL_LIMIT_FLAT_AMT | — | ✅ |
| 33 | CeilLimitFormulaId | CEIL_LIMIT_FORMULA_ID | — | ✅ |
| 34 | CeilLimitProrateRule | CEIL_LIMIT_PRORATE_RULE | — | ✅ |
| 35 | CeilLimitRule | CEIL_LIMIT_RULE | — | ✅ |
| 36 | CeilLmtProrateFormulaId | CEIL_LMT_PRORATE_FORMULA_ID | — | ✅ |
| 37 | CreatedBy | CREATED_BY | — | ✅ |
| 38 | CreationDate | CREATION_DATE | — | ✅ |
| 39 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 40 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 41 | EmpEnrlNegativeBalanceFlag | EMP_ENRL_NEGATIVE_BALANCE_FLAG | — | ✅ |
| 42 | EmpEnrlPositiveBalanceFlag | EMP_ENRL_POSITIVE_BALANCE_FLAG | — | ✅ |
| 43 | EmpEnrlTerminateEntlFlag | EMP_ENRL_TERMINATE_ENTL_FLAG | — | ✅ |
| 44 | EnrollNegativeBalanceFlag | ENROLL_NEGATIVE_BALANCE_FLAG | — | ✅ |
| 45 | EnrollPositiveBalanceFlag | ENROLL_POSITIVE_BALANCE_FLAG | — | ✅ |
| 46 | EnrollTerminateEntlFlag | ENROLL_TERMINATE_ENTL_FLAG | — | ✅ |
| 47 | EnrollmentEndFormulaId | ENROLLMENT_END_FORMULA_ID | — | ✅ |
| 48 | EnrollmentEndRule | ENROLLMENT_END_RULE | — | ✅ |
| 49 | EnrollmentStartFormulaId | ENROLLMENT_START_FORMULA_ID | — | ✅ |
| 50 | EnrollmentStartRule | ENROLLMENT_START_RULE | — | ✅ |
| 51 | EnterpriseId | ENTERPRISE_ID | — | — |
| 52 | EntitlementEndFormulaId | ENTITLEMENT_END_FORMULA_ID | — | ✅ |
| 53 | EntitlementEndRule | ENTITLEMENT_END_RULE | — | ✅ |
| 54 | EntlDefinitionType | ENTL_DEFINITION_TYPE | — | ✅ |
| 55 | EntlFormulaId | ENTL_FORMULA_ID | — | ✅ |
| 56 | EntlMethodCd | ENTL_METHOD_CD | — | ✅ |
| 57 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 58 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 59 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 60 | LegislationCode | LEGISLATION_CODE | — | — |
| 61 | LegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 62 | LiabilityRateFormulaId | LIABILITY_RATE_FORMULA_ID | — | ✅ |
| 63 | LiabilityRateId | LIABILITY_RATE_ID | — | ✅ |
| 64 | LiabilityRateRule | LIABILITY_RATE_RULE | — | ✅ |
| 65 | ModuleId | MODULE_ID | — | — |
| 66 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 67 | OtherAdjustmentFlag | OTHER_ADJUSTMENT_FLAG | — | ✅ |
| 68 | OtherReasons | OTHER_REASONS | — | ✅ |
| 69 | OverlapCd | OVERLAP_CD | — | ✅ |
| 70 | PartialAccrualFormulaId | PARTIAL_ACCRUAL_FORMULA_ID | — | ✅ |
| 71 | PayAdvancesFlag | PAY_ADVANCES_FLAG | — | ✅ |
| 72 | PayRateFactor | PAY_RATE_FACTOR | — | ✅ |
| 73 | PayoutRateFormulaId | PAYOUT_RATE_FORMULA_ID | — | ✅ |
| 74 | PayoutRateId | PAYOUT_RATE_ID | — | ✅ |
| 75 | PayoutRateRule | PAYOUT_RATE_RULE | — | ✅ |
| 76 | PayrollImpactFlag | PAYROLL_IMPACT_FLAG | — | ✅ |
| 77 | PayrollMappingId | PAYROLL_MAPPING_ID | — | ✅ |
| 78 | PeriodUom | PERIOD_UOM | — | ✅ |
| 79 | PlanActivationFlag | PLAN_ACTIVATION_FLAG | — | ✅ |
| 80 | PlanMgmtCd | PLAN_MGMT_CD | — | ✅ |
| 81 | PlanPeriodId | PLAN_PERIOD_ID | — | ✅ |
| 82 | PlanPeriodType | PLAN_PERIOD_TYPE | — | ✅ |
| 83 | PlanStatus | PLAN_STATUS | — | ✅ |
| 84 | PlanUom | PLAN_UOM | — | ✅ |
| 85 | PlanUseFormulaId | PLAN_USE_FORMULA_ID | — | ✅ |
| 86 | PlanUseRateId | PLAN_USE_RATE_ID | — | ✅ |
| 87 | PlanUseRateRule | PLAN_USE_RATE_RULE | — | ✅ |
| 88 | PrevEmpEntlFlag | PREV_EMP_ENTL_FLAG | — | ✅ |
| 89 | PrevEmpUsageFlag | PREV_EMP_USAGE_FLAG | — | ✅ |
| 90 | ProcessingLevelCd | PROCESSING_LEVEL_CD | — | ✅ |
| 91 | ProrationFormulaId | PRORATION_FORMULA_ID | — | ✅ |
| 92 | ProrationRule | PRORATION_RULE | — | ✅ |
| 93 | RollBackwardEndFormulaId | ROLL_BACKWARD_END_FORMULA_ID | — | ✅ |
| 94 | RollBackwardEndRule | ROLL_BACKWARD_END_RULE | — | ✅ |
| 95 | RollForwardStartFormulaId | ROLL_FORWARD_START_FORMULA_ID | — | ✅ |
| 96 | RollForwardStartRule | ROLL_FORWARD_START_RULE | — | ✅ |
| 97 | RollPeriodDuration | ROLL_PERIOD_DURATION | — | ✅ |
| 98 | StatutoryFlag | STATUTORY_FLAG | — | ✅ |
| 99 | VestingPeriodDuration | VESTING_PERIOD_DURATION | — | ✅ |
| 100 | VestingPeriodFormulaId | VESTING_PERIOD_FORMULA_ID | — | ✅ |
| 101 | VestingPeriodUom | VESTING_PERIOD_UOM | — | ✅ |
| 102 | WaitPeriodDurUnits | WAIT_PERIOD_DUR_UNITS | — | ✅ |
| 103 | WaitPeriodDurUom | WAIT_PERIOD_DUR_UOM | — | ✅ |

### [[anc_absence_plans_f_tl|ANC_ABSENCE_PLANS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsencePlanId1 | ABSENCE_PLAN_ID | — | ✅ |
| 2 | CreatedBy1 | CREATED_BY | — | ✅ |
| 3 | CreationDate1 | CREATION_DATE | — | ✅ |
| 4 | Description | DESCRIPTION | — | ✅ |
| 5 | EffectiveEndDate1 | EFFECTIVE_END_DATE | — | ✅ |
| 6 | EffectiveStartDate1 | EFFECTIVE_START_DATE | — | ✅ |
| 7 | EnterpriseId1 | ENTERPRISE_ID | — | — |
| 8 | Language | LANGUAGE | 🔑 | ✅ |
| 9 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 11 | LastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 12 | ModuleId1 | MODULE_ID | — | — |
| 13 | Name | NAME | — | ✅ |
| 14 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 15 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
