---
id: DOC-HCM-PVO-Paysheet
doc_type: system-doc
title: "Paysheet — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - Paysheet
  - paysheet
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# Paysheet

## 📌 Visão Geral

Extrai folhas de pagamento de incentivos (paysheets) com componentes de plano, repositórios e participantes. Suporta detalhamento de cálculos de remuneração variável e comissões.

**Caminho:** `FscmTopModelAM.PaysheetAM.Paysheet`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 136 | 8 | 1 | 89 | 65% |

---

## 🔗 Tabelas Relacionadas

- [[cn_pay_groups_all_b|CN_PAY_GROUPS_ALL_B]] — 6 atributos (3 BICC)
- [[cn_pay_groups_all_tl|CN_PAY_GROUPS_ALL_TL]] — 7 atributos (3 BICC)
- [[cn_plan_components_all_b|CN_PLAN_COMPONENTS_ALL_B]] — 21 atributos (13 BICC)
- [[cn_repositories_all_b|CN_REPOSITORIES_ALL_B]] — 4 atributos (1 BICC)
- [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]] — 20 atributos (10 BICC)
- [[cn_tp_payruns_all|CN_TP_PAYRUNS_ALL]] — 12 atributos (6 BICC)
- [[cn_tp_paysheets_all|CN_TP_PAYSHEETS_ALL]] — 60 atributos (1 PKs, 48 BICC)
- [[hz_parties|HZ_PARTIES]] — 6 atributos (5 BICC)

---

## ⚙️ Atributos

### [[cn_pay_groups_all_b|CN_PAY_GROUPS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EndDate | END_DATE | — | ✅ |
| 2 | ObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 3 | OrgId2 | ORG_ID | — | — |
| 4 | PayGroupId1 | PAY_GROUP_ID | — | — |
| 5 | PayGroupType | PAY_GROUP_TYPE | — | ✅ |
| 6 | StartDate | START_DATE | — | ✅ |

### [[cn_pay_groups_all_tl|CN_PAY_GROUPS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | ✅ |
| 2 | Language | LANGUAGE | — | ✅ |
| 3 | ObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 4 | OrgId4 | ORG_ID | — | — |
| 5 | PayGroupId2 | PAY_GROUP_ID | — | — |
| 6 | PayGroupName | PAY_GROUP_NAME | — | ✅ |
| 7 | SourceLang | SOURCE_LANG | — | — |

### [[cn_plan_components_all_b|CN_PLAN_COMPONENTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApExpId | AP_EXP_ID | — | — |
| 2 | ApLiabId | AP_LIAB_ID | — | — |
| 3 | ApprovalStatus | APPROVAL_STATUS | — | ✅ |
| 4 | CalcVariableId | CALC_VARIABLE_ID | — | — |
| 5 | CalculationPhase | CALCULATION_PHASE | — | ✅ |
| 6 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 7 | DeleteFlag | DELETE_FLAG | — | ✅ |
| 8 | EarningTypeId | EARNING_TYPE_ID | — | ✅ |
| 9 | EndDate1 | END_DATE | — | — |
| 10 | IncentiveType | INCENTIVE_TYPE | — | ✅ |
| 11 | IncrementalType | INCREMENTAL_TYPE | — | ✅ |
| 12 | IndirectCredit | INDIRECT_CREDIT | — | ✅ |
| 13 | ObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 14 | OrgId3 | ORG_ID | — | — |
| 15 | PaymentGroupCode | PAYMENT_GROUP_CODE | — | ✅ |
| 16 | PlanCompStatus | PLAN_COMP_STATUS | — | ✅ |
| 17 | PlanComponentId | PLAN_COMPONENT_ID | — | — |
| 18 | ReportGroup | REPORT_GROUP | — | ✅ |
| 19 | SalesrepEnddatedFlag | SALESREP_ENDDATED_FLAG | — | ✅ |
| 20 | StartDate1 | START_DATE | — | — |
| 21 | ThirdpartyPayeeFlag | THIRDPARTY_PAYEE_FLAG | — | ✅ |

### [[cn_repositories_all_b|CN_REPOSITORIES_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FunctionalCurrency | FUNCTIONAL_CURRENCY | — | ✅ |
| 2 | ObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |
| 3 | OrgId5 | ORG_ID | — | — |
| 4 | RepositoryId | REPOSITORY_ID | — | — |

### [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | AnalystId | ANALYST_ID | — | ✅ |
| 3 | CompensationEndDate | COMPENSATION_END_DATE | — | ✅ |
| 4 | DisplayIdentifier | DISPLAY_IDENTIFIER | — | ✅ |
| 5 | EndDate2 | END_DATE | — | — |
| 6 | HoldPaymentFlag | HOLD_PAYMENT_FLAG | — | ✅ |
| 7 | HoldReason | HOLD_REASON | — | ✅ |
| 8 | HrPersonNumber | HR_PERSON_NUMBER | — | — |
| 9 | HrPrimaryWorkerNumber | HR_PRIMARY_WORKER_NUMBER | — | — |
| 10 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 11 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 12 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 13 | ParticipantId1 | PARTICIPANT_ID | — | — |
| 14 | ParticipantType | PARTICIPANT_TYPE | — | ✅ |
| 15 | PartyId | PARTY_ID | — | ✅ |
| 16 | PayeeOnly | PAYEE_ONLY | — | — |
| 17 | RequestId | REQUEST_ID | — | — |
| 18 | SourceSystem | SOURCE_SYSTEM | — | ✅ |
| 19 | SourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 20 | StartDate2 | START_DATE | — | — |

### [[cn_tp_payruns_all|CN_TP_PAYRUNS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustComments1 | ADJUST_COMMENTS | — | — |
| 2 | AdjustStatus1 | ADJUST_STATUS | — | — |
| 3 | IncentiveTypeCode | INCENTIVE_TYPE_CODE | — | ✅ |
| 4 | ObjectStatus1 | OBJECT_STATUS | — | ✅ |
| 5 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 6 | OrgId1 | ORG_ID | — | — |
| 7 | PayDate | PAY_DATE | — | ✅ |
| 8 | PayGroupId | PAY_GROUP_ID | — | ✅ |
| 9 | PayPeriodId | PAY_PERIOD_ID | — | — |
| 10 | PayrunId1 | PAYRUN_ID | — | — |
| 11 | PayrunMode | PAYRUN_MODE | — | ✅ |
| 12 | PayrunName | PAYRUN_NAME | — | ✅ |

### [[cn_tp_paysheets_all|CN_TP_PAYSHEETS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustComments | ADJUST_COMMENTS | — | ✅ |
| 2 | AdjustStatus | ADJUST_STATUS | — | ✅ |
| 3 | BbPmtRecoveryPlans | BB_PMT_RECOVERY_PLANS | — | ✅ |
| 4 | BbPriorPeriodAdj | BB_PRIOR_PERIOD_ADJ | — | ✅ |
| 5 | BonusDueBb | BONUS_DUE_BB | — | ✅ |
| 6 | BonusPaid | BONUS_PAID | — | ✅ |
| 7 | BonusPtd | BONUS_PTD | — | ✅ |
| 8 | CommDraw | COMM_DRAW | — | ✅ |
| 9 | CommDueBb | COMM_DUE_BB | — | ✅ |
| 10 | CommNrec | COMM_NREC | — | ✅ |
| 11 | CommPaid | COMM_PAID | — | ✅ |
| 12 | CommPtd | COMM_PTD | — | ✅ |
| 13 | CostCenterId | COST_CENTER_ID | — | — |
| 14 | CreatedBy | CREATED_BY | — | — |
| 15 | CreationDate | CREATION_DATE | — | — |
| 16 | CreditTypeId | CREDIT_TYPE_ID | — | ✅ |
| 17 | CurrentEarnings | CURRENT_EARNINGS | — | ✅ |
| 18 | CurrentEarningsDue | CURRENT_EARNINGS_DUE | — | ✅ |
| 19 | DrawPaid | DRAW_PAID | — | ✅ |
| 20 | EmployeeNumber | EMPLOYEE_NUMBER | — | ✅ |
| 21 | HeldAmount | HELD_AMOUNT | — | ✅ |
| 22 | HomeCurrencyCode | HOME_CURRENCY_CODE | — | ✅ |
| 23 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 25 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 26 | MinimumAmount | MINIMUM_AMOUNT | — | ✅ |
| 27 | ObjectStatus | OBJECT_STATUS | — | ✅ |
| 28 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 29 | OrgId | ORG_ID | — | ✅ |
| 30 | ParticipantId | PARTICIPANT_ID | — | — |
| 31 | PayAmtAdjFuncCurr | PAY_AMT_ADJ_FUNC_CURR | — | ✅ |
| 32 | PayAmtAdjHomeCurr | PAY_AMT_ADJ_HOME_CURR | — | ✅ |
| 33 | PayAmtAdjPayCurr | PAY_AMT_ADJ_PAY_CURR | — | ✅ |
| 34 | PayCurrencyCode | PAY_CURRENCY_CODE | — | ✅ |
| 35 | PayToFuncCurrCnvrt | PAY_TO_FUNC_CURR_CNVRT | — | ✅ |
| 36 | PayToHomeCurrCnvrt | PAY_TO_HOME_CURR_CNVRT | — | ✅ |
| 37 | PayeeBonusDueBb | PAYEE_BONUS_DUE_BB | — | ✅ |
| 38 | PayeeBonusPaid | PAYEE_BONUS_PAID | — | ✅ |
| 39 | PayeeBonusPtd | PAYEE_BONUS_PTD | — | ✅ |
| 40 | PayeeCommDueBb | PAYEE_COMM_DUE_BB | — | ✅ |
| 41 | PayeeCommPaid | PAYEE_COMM_PAID | — | ✅ |
| 42 | PayeeCommPtd | PAYEE_COMM_PTD | — | ✅ |
| 43 | PaymentDate | ATTRIBUTE14 | — | ✅ |
| 44 | PaymentMethod | ATTRIBUTE15 | — | ✅ |
| 45 | PaymentReferenceNumber | ATTRIBUTE13 | — | ✅ |
| 46 | PayrunId | PAYRUN_ID | — | — |
| 47 | PaysheetId | PAYSHEET_ID | 🔑 | ✅ |
| 48 | PmtAmountAdjNrec | PMT_AMOUNT_ADJ_NREC | — | ✅ |
| 49 | PmtAmountAdjRec | PMT_AMOUNT_ADJ_REC | — | ✅ |
| 50 | PmtAmountCalc | PMT_AMOUNT_CALC | — | ✅ |
| 51 | PmtAmountRecovery | PMT_AMOUNT_RECOVERY | — | ✅ |
| 52 | QuotaId | QUOTA_ID | — | — |
| 53 | RegBonusDueBb | REG_BONUS_DUE_BB | — | ✅ |
| 54 | RegBonusPaid | REG_BONUS_PAID | — | ✅ |
| 55 | RegBonusPtd | REG_BONUS_PTD | — | ✅ |
| 56 | RegBonusRec | REG_BONUS_REC | — | ✅ |
| 57 | RegBonusToRec | REG_BONUS_TO_REC | — | ✅ |
| 58 | SourceOrgId | SOURCE_ORG_ID | — | — |
| 59 | TotalAmtHomeCurrency | TOTAL_AMT_HOME_CURRENCY | — | — |
| 60 | TotalAmtPayToHomeCnvrt | TOTAL_AMT_PAY_TO_HOME_CNVRT | — | — |

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

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
