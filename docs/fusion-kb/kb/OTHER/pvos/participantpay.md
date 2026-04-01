---
id: DOC-OTHER-PVO-ParticipantPay
doc_type: system-doc
title: "ParticipantPay — PVO Cross-Module"
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
  - ParticipantPay
  - participantpay
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ParticipantPay

## 📌 Visão Geral

View Object para extração BICC de dados de Participant Pay. Acessa as tabelas: CN_REPOSITORIES_ALL_B, CN_RS_RULES_ALL_TL, CN_SRP_COMP_PLANS_ALL (+10).

**Caminho:** `FscmTopModelAM.PaysheetAM.ParticipantPay`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 357 | 13 | 1 | 180 | 50% |

---

## 🔗 Tabelas Relacionadas

- [[cn_repositories_all_b|CN_REPOSITORIES_ALL_B]] — 4 atributos (1 BICC)
- [[cn_rs_rules_all_tl|CN_RS_RULES_ALL_TL]] — 4 atributos (1 BICC)
- [[cn_srp_comp_plans_all|CN_SRP_COMP_PLANS_ALL]] — 18 atributos (7 BICC)
- [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]] — 25 atributos (11 BICC)
- [[cn_tp_credits_all|CN_TP_CREDITS_ALL]] — 5 atributos (1 BICC)
- [[cn_tp_earnings_all_v|CN_TP_EARNINGS_ALL_V]] — 57 atributos (32 BICC)
- [[cn_tp_participant_pay_all|CN_TP_PARTICIPANT_PAY_ALL]] — 61 atributos (1 PKs, 31 BICC)
- [[cn_tp_payruns_all|CN_TP_PAYRUNS_ALL]] — 33 atributos (5 BICC)
- [[cn_tp_paysheets_all|CN_TP_PAYSHEETS_ALL]] — 71 atributos (37 BICC)
- [[cn_tp_process_codes_b|CN_TP_PROCESS_CODES_B]] — 4 atributos (3 BICC)
- [[cn_tp_transactions_all|CN_TP_TRANSACTIONS_ALL]] — 65 atributos (43 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 4 atributos (3 BICC)
- [[hz_parties|HZ_PARTIES]] — 6 atributos (5 BICC)

---

## ⚙️ Atributos

### [[cn_repositories_all_b|CN_REPOSITORIES_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FunctionalCurrency | FUNCTIONAL_CURRENCY | — | ✅ |
| 2 | ObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 3 | OrgId6 | ORG_ID | — | — |
| 4 | RepositoryId | REPOSITORY_ID | — | — |

### [[cn_rs_rules_all_tl|CN_RS_RULES_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClsfnRuleName | NAME | — | ✅ |
| 2 | RuleId | RULE_ID | — | — |
| 3 | TxnClfsnRuleId | RULE_ID | — | — |
| 4 | TxnClfsnRuleName | NAME | — | — |

### [[cn_srp_comp_plans_all|CN_SRP_COMP_PLANS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApprovalStatus | APPROVAL_STATUS | — | ✅ |
| 2 | CompPlanId | COMP_PLAN_ID | — | — |
| 3 | CreatedBy4 | CREATED_BY | — | — |
| 4 | CreationDate4 | CREATION_DATE | — | — |
| 5 | CustomizedFlag | CUSTOMIZED_FLAG | — | ✅ |
| 6 | EndDate | END_DATE | — | ✅ |
| 7 | LastUpdateDate4 | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 9 | LastUpdatedBy4 | LAST_UPDATED_BY | — | — |
| 10 | ObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 11 | OrgId4 | ORG_ID | — | — |
| 12 | ParticipantId2 | PARTICIPANT_ID | — | — |
| 13 | RulePlanId | RULE_PLAN_ID | — | — |
| 14 | SrpCompPlanId1 | SRP_COMP_PLAN_ID | — | — |
| 15 | SrpRuleId | SRP_RULE_ID | — | — |
| 16 | SrpRuleTypeCode | SRP_RULE_TYPE_CODE | — | ✅ |
| 17 | StartDate | START_DATE | — | ✅ |
| 18 | TargetIncentive | TARGET_INCENTIVE | — | ✅ |

### [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | AnalystId | ANALYST_ID | — | ✅ |
| 3 | CompensationEndDate | COMPENSATION_END_DATE | — | ✅ |
| 4 | DisplayIdentifier | DISPLAY_IDENTIFIER | — | ✅ |
| 5 | EndDate1 | END_DATE | — | — |
| 6 | HoldPaymentFlag | HOLD_PAYMENT_FLAG | — | ✅ |
| 7 | HoldReason | HOLD_REASON | — | ✅ |
| 8 | HrPersonNumber | HR_PERSON_NUMBER | — | ✅ |
| 9 | HrPrimaryWorkerNumber | HR_PRIMARY_WORKER_NUMBER | — | ✅ |
| 10 | JobDefinitionName2 | JOB_DEFINITION_NAME | — | — |
| 11 | JobDefinitionPackage2 | JOB_DEFINITION_PACKAGE | — | — |
| 12 | ObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 13 | ParticipantId4 | PARTICIPANT_ID | — | — |
| 14 | ParticipantType | PARTICIPANT_TYPE | — | — |
| 15 | PartyId | PARTY_ID | — | ✅ |
| 16 | PayeeOnly | PAYEE_ONLY | — | — |
| 17 | RequestId2 | REQUEST_ID | — | — |
| 18 | SourceSystem | SOURCE_SYSTEM | — | ✅ |
| 19 | SourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 20 | StartDate1 | START_DATE | — | — |
| 21 | TxnPrcptAnalystId | ANALYST_ID | — | — |
| 22 | TxnPrcptObjectVersionNum | OBJECT_VERSION_NUMBER | — | — |
| 23 | TxnPrcptParticipantId | PARTICIPANT_ID | — | — |
| 24 | TxnPrcptPartyId | PARTY_ID | — | — |
| 25 | TxnPrcptSourceSystemId | SOURCE_SYSTEM_ID | — | — |

### [[cn_tp_credits_all|CN_TP_CREDITS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreditId1 | CREDIT_ID | — | — |
| 2 | CreditPEOCreditType | CREDIT_TYPE | — | — |
| 3 | CreditRuleId | CREDIT_RULE_ID | — | — |
| 4 | DirectRuleId | DIRECT_RULE_ID | — | — |
| 5 | RollupLevel | ROLLUP_LEVEL | — | ✅ |

### [[cn_tp_earnings_all_v|CN_TP_EARNINGS_ALL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustmentComments | ADJUSTMENT_COMMENTS | — | ✅ |
| 2 | AdjustmentStatus | ADJUSTMENT_STATUS | — | ✅ |
| 3 | CalcCurrencyCode | CALC_CURRENCY_CODE | — | ✅ |
| 4 | CalcToFuncCurrCnvrt | CALC_TO_FUNC_CURR_CNVRT | — | ✅ |
| 5 | CalcToHomeCurrCnvrt | CALC_TO_HOME_CURR_CNVRT | — | ✅ |
| 6 | CommissionValue1 | COMMISSION_VALUE | — | — |
| 7 | CreatedBy3 | CREATED_BY | — | — |
| 8 | CreatedDuring | CREATED_DURING | — | — |
| 9 | CreationDate3 | CREATION_DATE | — | — |
| 10 | CreditFactor | CREDIT_FACTOR | — | ✅ |
| 11 | CreditId | CREDIT_ID | — | ✅ |
| 12 | CreditedParticipantId1 | CREDITED_PARTICIPANT_ID | — | — |
| 13 | EarningFactor | EARNING_FACTOR | — | ✅ |
| 14 | EarningId1 | EARNING_ID | — | — |
| 15 | EarningType | EARNING_TYPE | — | ✅ |
| 16 | EarningTypeId | EARNING_TYPE_ID | — | ✅ |
| 17 | EligibleCatId | ELIGIBLE_CAT_ID | — | ✅ |
| 18 | ErrorReason | ERROR_REASON | — | ✅ |
| 19 | EventFactorValue | EVENT_FACTOR_VALUE | — | ✅ |
| 20 | FormulaEcatId | FORMULA_ECAT_ID | — | ✅ |
| 21 | FormulaId | FORMULA_ID | — | — |
| 22 | FormulaWeight | FORMULA_WEIGHT | — | ✅ |
| 23 | HomeCurrencyCode2 | HOME_CURRENCY_CODE | — | — |
| 24 | InputAchieved | INPUT_ACHIEVED | — | ✅ |
| 25 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 26 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 27 | LastUpdateDate3 | LAST_UPDATE_DATE | — | ✅ |
| 28 | LastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 29 | LastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 30 | ObjectStatus3 | OBJECT_STATUS | — | ✅ |
| 31 | OrgId3 | ORG_ID | — | — |
| 32 | OutputAchieved | OUTPUT_ACHIEVED | — | ✅ |
| 33 | ParticipantId1 | PARTICIPANT_ID | — | — |
| 34 | PayPeriodId2 | PAY_PERIOD_ID | — | — |
| 35 | PendingDate | PENDING_DATE | — | ✅ |
| 36 | PendingStatus | PENDING_STATUS | — | ✅ |
| 37 | PlanComponentId1 | PLAN_COMPONENT_ID | — | — |
| 38 | PostingStatus | POSTING_STATUS | — | ✅ |
| 39 | ProcessCode | PROCESS_CODE | — | ✅ |
| 40 | RateTableValueId | RATE_TABLE_VALUE_ID | — | — |
| 41 | ReasonCode | REASON_CODE | — | ✅ |
| 42 | RequestId | REQUEST_ID | — | — |
| 43 | RevenueType | REVENUE_TYPE | — | ✅ |
| 44 | RoleId1 | ROLE_ID | — | — |
| 45 | SourceEarningId1 | SOURCE_EARNING_ID | — | — |
| 46 | SourceEventDate1 | SOURCE_EVENT_DATE | — | — |
| 47 | SourceEventPeriodId | SOURCE_EVENT_PERIOD_ID | — | — |
| 48 | SourceOrgId2 | SOURCE_ORG_ID | — | — |
| 49 | SourceTrxNumber1 | SOURCE_TRX_NUMBER | — | — |
| 50 | SplitPct | SPLIT_PCT | — | ✅ |
| 51 | SrpAlternatePayeeId | SRP_ALTERNATE_PAYEE_ID | — | — |
| 52 | SrpCompPlanId | SRP_COMP_PLAN_ID | — | ✅ |
| 53 | TierSplits | TIER_SPLITS | — | ✅ |
| 54 | TransactionId | TRANSACTION_ID | — | ✅ |
| 55 | TransactionQty | TRANSACTION_QTY | — | ✅ |
| 56 | TransactionType1 | TRANSACTION_TYPE | — | — |
| 57 | WorkerId | WORKER_ID | — | ✅ |

### [[cn_tp_participant_pay_all|CN_TP_PARTICIPANT_PAY_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustComments | ADJUST_COMMENTS | — | ✅ |
| 2 | AdjustStatus | ADJUST_STATUS | — | ✅ |
| 3 | Attribute1 | ATTRIBUTE1 | — | — |
| 4 | Attribute10 | ATTRIBUTE10 | — | — |
| 5 | Attribute11 | ATTRIBUTE11 | — | — |
| 6 | Attribute12 | ATTRIBUTE12 | — | — |
| 7 | Attribute13 | ATTRIBUTE13 | — | — |
| 8 | Attribute14 | ATTRIBUTE14 | — | — |
| 9 | Attribute15 | ATTRIBUTE15 | — | — |
| 10 | Attribute2 | ATTRIBUTE2 | — | — |
| 11 | Attribute3 | ATTRIBUTE3 | — | — |
| 12 | Attribute4 | ATTRIBUTE4 | — | — |
| 13 | Attribute5 | ATTRIBUTE5 | — | — |
| 14 | Attribute6 | ATTRIBUTE6 | — | — |
| 15 | Attribute7 | ATTRIBUTE7 | — | — |
| 16 | Attribute8 | ATTRIBUTE8 | — | — |
| 17 | Attribute9 | ATTRIBUTE9 | — | — |
| 18 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 19 | CommAmtCalcCurr | COMM_AMT_CALC_CURR | — | ✅ |
| 20 | CommissionValue | COMMISSION_VALUE | — | ✅ |
| 21 | CreatedBy | CREATED_BY | — | — |
| 22 | CreationDate | CREATION_DATE | — | — |
| 23 | CreditTypeId | CREDIT_TYPE_ID | — | ✅ |
| 24 | CreditedEmployeeNumber | CREDITED_EMPLOYEE_NUMBER | — | ✅ |
| 25 | CreditedParticipantId | CREDITED_PARTICIPANT_ID | — | — |
| 26 | EarningId | EARNING_ID | — | ✅ |
| 27 | ExpenseCcid | EXPENSE_CCID | — | ✅ |
| 28 | HoldFlag | HOLD_FLAG | — | ✅ |
| 29 | HomeCurrencyCode | HOME_CURRENCY_CODE | — | ✅ |
| 30 | IncentiveTypeCode | INCENTIVE_TYPE_CODE | — | ✅ |
| 31 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 34 | LiabilityCcid | LIABILITY_CCID | — | ✅ |
| 35 | ManualAdjReasonCode | MANUAL_ADJ_REASON_CODE | — | ✅ |
| 36 | ObjectStatus | OBJECT_STATUS | — | ✅ |
| 37 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 38 | OrgId | ORG_ID | — | — |
| 39 | ParticipantPayId | PARTICIPANT_PAY_ID | 🔑 | ✅ |
| 40 | PayAmtFuncCurr | PAY_AMT_FUNC_CURR | — | ✅ |
| 41 | PayAmtHomeCurr | PAY_AMT_HOME_CURR | — | ✅ |
| 42 | PayAmtPayCurr | PAY_AMT_PAY_CURR | — | ✅ |
| 43 | PayCurrencyCode | PAY_CURRENCY_CODE | — | ✅ |
| 44 | PayElementTypeId | PAY_ELEMENT_TYPE_ID | — | — |
| 45 | PayPeriodId | PAY_PERIOD_ID | — | — |
| 46 | PayToFuncCurrCnvrt | PAY_TO_FUNC_CURR_CNVRT | — | ✅ |
| 47 | PayToHomeCurrCnvrt | PAY_TO_HOME_CURR_CNVRT | — | ✅ |
| 48 | PayeeEmployeeNumber | PAYEE_EMPLOYEE_NUMBER | — | ✅ |
| 49 | PayeeParticipantId | PAYEE_PARTICIPANT_ID | — | ✅ |
| 50 | PayrunId | PAYRUN_ID | — | — |
| 51 | PlanComponentId | PLAN_COMPONENT_ID | — | — |
| 52 | RecoverableFlag | RECOVERABLE_FLAG | — | ✅ |
| 53 | RoleId | ROLE_ID | — | — |
| 54 | SourceEarningId | SOURCE_EARNING_ID | — | — |
| 55 | SourceEventDate | SOURCE_EVENT_DATE | — | ✅ |
| 56 | SourceOrgId | SOURCE_ORG_ID | — | — |
| 57 | SourceTrxNumber | SOURCE_TRX_NUMBER | — | ✅ |
| 58 | SourceType | SOURCE_TYPE | — | ✅ |
| 59 | SrpPlanAssignId | SRP_PLAN_ASSIGN_ID | — | — |
| 60 | TransactionType | TRANSACTION_TYPE | — | ✅ |
| 61 | WaiveFlag | WAIVE_FLAG | — | ✅ |

### [[cn_tp_payruns_all|CN_TP_PAYRUNS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustComments1 | ADJUST_COMMENTS | — | — |
| 2 | AdjustStatus1 | ADJUST_STATUS | — | — |
| 3 | Attribute101 | ATTRIBUTE10 | — | — |
| 4 | Attribute111 | ATTRIBUTE11 | — | — |
| 5 | Attribute121 | ATTRIBUTE12 | — | — |
| 6 | Attribute131 | ATTRIBUTE13 | — | — |
| 7 | Attribute141 | ATTRIBUTE14 | — | — |
| 8 | Attribute151 | ATTRIBUTE15 | — | — |
| 9 | Attribute16 | ATTRIBUTE1 | — | — |
| 10 | Attribute21 | ATTRIBUTE2 | — | — |
| 11 | Attribute31 | ATTRIBUTE3 | — | — |
| 12 | Attribute41 | ATTRIBUTE4 | — | — |
| 13 | Attribute51 | ATTRIBUTE5 | — | — |
| 14 | Attribute61 | ATTRIBUTE6 | — | — |
| 15 | Attribute71 | ATTRIBUTE7 | — | — |
| 16 | Attribute81 | ATTRIBUTE8 | — | — |
| 17 | Attribute91 | ATTRIBUTE9 | — | — |
| 18 | AttributeCategory1 | ATTRIBUTE_CATEGORY | — | — |
| 19 | CreatedBy1 | CREATED_BY | — | — |
| 20 | CreationDate1 | CREATION_DATE | — | — |
| 21 | IncentiveTypeCode1 | INCENTIVE_TYPE_CODE | — | — |
| 22 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 23 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 24 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 25 | ObjectStatus1 | OBJECT_STATUS | — | ✅ |
| 26 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 27 | OrgId1 | ORG_ID | — | — |
| 28 | PayDate | PAY_DATE | — | ✅ |
| 29 | PayGroupId | PAY_GROUP_ID | — | — |
| 30 | PayPeriodId1 | PAY_PERIOD_ID | — | — |
| 31 | PayrunId1 | PAYRUN_ID | — | — |
| 32 | PayrunMode | PAYRUN_MODE | — | ✅ |
| 33 | PayrunName | PAYRUN_NAME | — | ✅ |

### [[cn_tp_paysheets_all|CN_TP_PAYSHEETS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustComments2 | ADJUST_COMMENTS | — | — |
| 2 | AdjustStatus2 | ADJUST_STATUS | — | — |
| 3 | Attribute102 | ATTRIBUTE10 | — | — |
| 4 | Attribute112 | ATTRIBUTE11 | — | — |
| 5 | Attribute122 | ATTRIBUTE12 | — | — |
| 6 | Attribute132 | ATTRIBUTE13 | — | — |
| 7 | Attribute142 | ATTRIBUTE14 | — | — |
| 8 | Attribute152 | ATTRIBUTE15 | — | — |
| 9 | Attribute17 | ATTRIBUTE1 | — | — |
| 10 | Attribute22 | ATTRIBUTE2 | — | — |
| 11 | Attribute32 | ATTRIBUTE3 | — | — |
| 12 | Attribute42 | ATTRIBUTE4 | — | — |
| 13 | Attribute52 | ATTRIBUTE5 | — | — |
| 14 | Attribute62 | ATTRIBUTE6 | — | — |
| 15 | Attribute72 | ATTRIBUTE7 | — | — |
| 16 | Attribute82 | ATTRIBUTE8 | — | — |
| 17 | Attribute92 | ATTRIBUTE9 | — | — |
| 18 | AttributeCategory2 | ATTRIBUTE_CATEGORY | — | — |
| 19 | BbPmtRecoveryPlans | BB_PMT_RECOVERY_PLANS | — | ✅ |
| 20 | BbPriorPeriodAdj | BB_PRIOR_PERIOD_ADJ | — | — |
| 21 | BonusDueBb | BONUS_DUE_BB | — | ✅ |
| 22 | BonusPaid | BONUS_PAID | — | ✅ |
| 23 | BonusPtd | BONUS_PTD | — | ✅ |
| 24 | CommDraw | COMM_DRAW | — | ✅ |
| 25 | CommDueBb | COMM_DUE_BB | — | ✅ |
| 26 | CommNrec | COMM_NREC | — | ✅ |
| 27 | CommPaid | COMM_PAID | — | ✅ |
| 28 | CommPtd | COMM_PTD | — | ✅ |
| 29 | CostCenterId | COST_CENTER_ID | — | — |
| 30 | CreatedBy2 | CREATED_BY | — | — |
| 31 | CreationDate2 | CREATION_DATE | — | — |
| 32 | CreditTypeId1 | CREDIT_TYPE_ID | — | — |
| 33 | CurrentEarnings | CURRENT_EARNINGS | — | ✅ |
| 34 | CurrentEarningsDue | CURRENT_EARNINGS_DUE | — | ✅ |
| 35 | DrawPaid | DRAW_PAID | — | ✅ |
| 36 | EmployeeNumber | EMPLOYEE_NUMBER | — | ✅ |
| 37 | HeldAmount | HELD_AMOUNT | — | ✅ |
| 38 | HomeCurrencyCode1 | HOME_CURRENCY_CODE | — | — |
| 39 | LastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 40 | LastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 41 | LastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 42 | MinimumAmount | MINIMUM_AMOUNT | — | ✅ |
| 43 | ObjectStatus2 | OBJECT_STATUS | — | ✅ |
| 44 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 45 | OrgId2 | ORG_ID | — | — |
| 46 | ParticipantId | PARTICIPANT_ID | — | — |
| 47 | PayAmtAdjFuncCurr | PAY_AMT_ADJ_FUNC_CURR | — | ✅ |
| 48 | PayAmtAdjHomeCurr | PAY_AMT_ADJ_HOME_CURR | — | ✅ |
| 49 | PayAmtAdjPayCurr | PAY_AMT_ADJ_PAY_CURR | — | ✅ |
| 50 | PayCurrencyCode1 | PAY_CURRENCY_CODE | — | ✅ |
| 51 | PayToFuncCurrCnvrt1 | PAY_TO_FUNC_CURR_CNVRT | — | — |
| 52 | PayToHomeCurrCnvrt1 | PAY_TO_HOME_CURR_CNVRT | — | — |
| 53 | PayeeBonusDueBb | PAYEE_BONUS_DUE_BB | — | ✅ |
| 54 | PayeeBonusPaid | PAYEE_BONUS_PAID | — | ✅ |
| 55 | PayeeBonusPtd | PAYEE_BONUS_PTD | — | ✅ |
| 56 | PayeeCommDueBb | PAYEE_COMM_DUE_BB | — | ✅ |
| 57 | PayeeCommPaid | PAYEE_COMM_PAID | — | ✅ |
| 58 | PayeeCommPtd | PAYEE_COMM_PTD | — | ✅ |
| 59 | PayrunId2 | PAYRUN_ID | — | — |
| 60 | PaysheetId | PAYSHEET_ID | — | — |
| 61 | PmtAmountAdjNrec | PMT_AMOUNT_ADJ_NREC | — | ✅ |
| 62 | PmtAmountAdjRec | PMT_AMOUNT_ADJ_REC | — | ✅ |
| 63 | PmtAmountCalc | PMT_AMOUNT_CALC | — | ✅ |
| 64 | PmtAmountRecovery | PMT_AMOUNT_RECOVERY | — | ✅ |
| 65 | QuotaId | QUOTA_ID | — | ✅ |
| 66 | RegBonusDueBb | REG_BONUS_DUE_BB | — | ✅ |
| 67 | RegBonusPaid | REG_BONUS_PAID | — | ✅ |
| 68 | RegBonusPtd | REG_BONUS_PTD | — | ✅ |
| 69 | RegBonusRec | REG_BONUS_REC | — | ✅ |
| 70 | RegBonusToRec | REG_BONUS_TO_REC | — | ✅ |
| 71 | SourceOrgId1 | SOURCE_ORG_ID | — | — |

### [[cn_tp_process_codes_b|CN_TP_PROCESS_CODES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClassificationFlag | CLASSIFICATION_FLAG | — | ✅ |
| 2 | CreditFlag | CREDIT_FLAG | — | ✅ |
| 3 | ProcessCode2 | PROCESS_CODE | — | — |
| 4 | RollupFlag | ROLLUP_FLAG | — | ✅ |

### [[cn_tp_transactions_all|CN_TP_TRANSACTIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustmentComments1 | ADJUSTMENT_COMMENTS | — | ✅ |
| 2 | AdjustmentStatus1 | ADJUSTMENT_STATUS | — | ✅ |
| 3 | AreaCode | AREA_CODE | — | ✅ |
| 4 | BillToAddressId | BILL_TO_ADDRESS_ID | — | ✅ |
| 5 | BillToContactId | BILL_TO_CONTACT_ID | — | ✅ |
| 6 | BookedDate | BOOKED_DATE | — | ✅ |
| 7 | ChangedTrxFlag | CHANGED_TRX_FLAG | — | ✅ |
| 8 | City | CITY | — | ✅ |
| 9 | ClsfnRuleId | CLSFN_RULE_ID | — | — |
| 10 | CollectionStatus | COLLECTION_STATUS | — | ✅ |
| 11 | Country | COUNTRY | — | ✅ |
| 12 | CreditDate | CREDIT_DATE | — | ✅ |
| 13 | CustomerId | CUSTOMER_ID | — | — |
| 14 | DiscountPercentage | DISCOUNT_PERCENTAGE | — | ✅ |
| 15 | EligibleCatId1 | ELIGIBLE_CAT_ID | — | — |
| 16 | HoldFlag1 | HOLD_FLAG | — | ✅ |
| 17 | InventoryItemId | INVENTORY_ITEM_ID | — | — |
| 18 | InvoiceDate | INVOICE_DATE | — | ✅ |
| 19 | InvoiceNumber | INVOICE_NUMBER | — | ✅ |
| 20 | JobDefinitionName1 | JOB_DEFINITION_NAME | — | — |
| 21 | JobDefinitionPackage1 | JOB_DEFINITION_PACKAGE | — | — |
| 22 | MarginPercentage | MARGIN_PERCENTAGE | — | ✅ |
| 23 | NewTransactionId | NEW_TRANSACTION_ID | — | — |
| 24 | ObjectStatus4 | OBJECT_STATUS | — | ✅ |
| 25 | OrderNumber | ORDER_NUMBER | — | ✅ |
| 26 | OrgId5 | ORG_ID | — | — |
| 27 | ParticipantId3 | PARTICIPANT_ID | — | — |
| 28 | PostalCode | POSTAL_CODE | — | ✅ |
| 29 | PreserveCreditFlag | PRESERVE_CREDIT_FLAG | — | ✅ |
| 30 | ProcessCode1 | PROCESS_CODE | — | ✅ |
| 31 | Province | PROVINCE | — | ✅ |
| 32 | ReasonCode1 | REASON_CODE | — | ✅ |
| 33 | RequestId1 | REQUEST_ID | — | — |
| 34 | RoleId2 | ROLE_ID | — | — |
| 35 | RollupDate | ROLLUP_DATE | — | ✅ |
| 36 | SalesChannel | SALES_CHANNEL | — | ✅ |
| 37 | ShipToAddressId | SHIP_TO_ADDRESS_ID | — | ✅ |
| 38 | ShipToContactId | SHIP_TO_CONTACT_ID | — | ✅ |
| 39 | SourceCurrencyCode | SOURCE_CURRENCY_CODE | — | ✅ |
| 40 | SourceEventDate2 | SOURCE_EVENT_DATE | — | ✅ |
| 41 | SourceEventPeriodId1 | SOURCE_EVENT_PERIOD_ID | — | — |
| 42 | SourceOrgId3 | SOURCE_ORG_ID | — | — |
| 43 | SourceToFuncCurrCnvrt | SOURCE_TO_FUNC_CURR_CNVRT | — | ✅ |
| 44 | SourceTrxId | SOURCE_TRX_ID | — | ✅ |
| 45 | SourceTrxLineId | SOURCE_TRX_LINE_ID | — | ✅ |
| 46 | SourceTrxNumber2 | SOURCE_TRX_NUMBER | — | — |
| 47 | SourceTrxSalesLineId | SOURCE_TRX_SALES_LINE_ID | — | ✅ |
| 48 | SourceType1 | SOURCE_TYPE | — | ✅ |
| 49 | State | STATE | — | ✅ |
| 50 | TerrId | TERR_ID | — | ✅ |
| 51 | TerrName | TERR_NAME | — | ✅ |
| 52 | TransactionId1 | TRANSACTION_ID | — | — |
| 53 | TransactionQty1 | TRANSACTION_QTY | — | — |
| 54 | TransactionSubType | TRANSACTION_SUB_TYPE | — | ✅ |
| 55 | TransactionType2 | TRANSACTION_TYPE | — | — |
| 56 | TxnCreatedBy | CREATED_BY | — | — |
| 57 | TxnCreationDate | CREATION_DATE | — | ✅ |
| 58 | TxnErrorCode | ERROR_CODE | — | — |
| 59 | TxnLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 60 | TxnLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 61 | TxnLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 62 | TxnTransactionAmtFuncCurr | TRANSACTION_AMT_FUNC_CURR | — | — |
| 63 | TxnTransactionAmtSourceCurr | TRANSACTION_AMT_SOURCE_CURR | — | — |
| 64 | UomCode | UOM_CODE | — | ✅ |
| 65 | WorkerId1 | WORKER_ID | — | ✅ |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitId | BU_ID | — | — |
| 2 | LocationId | LOCATION_ID | — | ✅ |
| 3 | ManagerId | MANAGER_ID | — | ✅ |
| 4 | Name | BU_NAME | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ParticipantFirstName | PERSON_FIRST_NAME | — | ✅ |
| 2 | ParticipantLastName | PERSON_LAST_NAME | — | ✅ |
| 3 | ParticipantName | PARTY_NAME | — | ✅ |
| 4 | ParticipantPartyPEOPartyId | PARTY_ID | — | — |
| 5 | PartyNumber | PARTY_NUMBER | — | ✅ |
| 6 | UserGuid | USER_GUID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
