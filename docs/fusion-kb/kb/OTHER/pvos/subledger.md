---
id: DOC-OTHER-PVO-SubLedger
doc_type: system-doc
title: "SubLedger — PVO Cross-Module"
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
  - SubLedger
  - subledger
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SubLedger

## 📌 Visão Geral

View Object para extração BICC de dados de Sub Ledger. Acessa as tabelas: CN_REPOSITORIES_ALL_B, CN_REPOSITORIES_ALL_TL, CN_SRP_COMP_PLANS_ALL (+3).

**Caminho:** `FscmTopModelAM.SrpCompPlanAM.SubLedger`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 218 | 6 | 1 | 121 | 56% |

---

## 🔗 Tabelas Relacionadas

- [[cn_repositories_all_b|CN_REPOSITORIES_ALL_B]] — 48 atributos (34 BICC)
- [[cn_repositories_all_tl|CN_REPOSITORIES_ALL_TL]] — 12 atributos (5 BICC)
- [[cn_srp_comp_plans_all|CN_SRP_COMP_PLANS_ALL]] — 34 atributos (7 BICC)
- [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]] — 42 atributos (9 BICC)
- [[cn_srp_subledger_all|CN_SRP_SUBLEDGER_ALL]] — 76 atributos (1 PKs, 62 BICC)
- [[hz_parties|HZ_PARTIES]] — 6 atributos (4 BICC)

---

## ⚙️ Atributos

### [[cn_repositories_all_b|CN_REPOSITORIES_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AggrTransRollup | AGGR_TRANS_ROLLUP | — | ✅ |
| 2 | ApplicationId | APPLICATION_ID | — | — |
| 3 | ApplicationType | APPLICATION_TYPE | — | ✅ |
| 4 | AttainmentSummary | ATTAINMENT_SUMMARY | — | — |
| 5 | AutoNotesPlanRule | AUTO_NOTES_PLAN_RULE | — | — |
| 6 | BatchRunnerStatus | BATCH_RUNNER_STATUS | — | ✅ |
| 7 | CalendarId | CALENDAR_ID | — | ✅ |
| 8 | ClassifyBatchOption | CLASSIFY_BATCH_OPTION | — | ✅ |
| 9 | ClassifyBatchSize | CLASSIFY_BATCH_SIZE | — | ✅ |
| 10 | ClassifyTransaction | CLASSIFY_TRANSACTION | — | ✅ |
| 11 | CnCommRatePrecision | CN_COMM_RATE_PRECISION | — | ✅ |
| 12 | CnConversionType | CN_CONVERSION_TYPE | — | — |
| 13 | CnCustPlanCompFlag | CN_CUST_PLAN_COMP_FLAG | — | ✅ |
| 14 | CnCustomAggrTrx | CN_CUSTOM_AGGR_TRX | — | ✅ |
| 15 | CnDisplayDraw | CN_DISPLAY_DRAW | — | ✅ |
| 16 | CommissionStatement | COMMISSION_STATEMENT | — | ✅ |
| 17 | CreatedBy3 | CREATED_BY | — | — |
| 18 | CreationDate3 | CREATION_DATE | — | — |
| 19 | CreditDetails | CREDIT_DETAILS | — | — |
| 20 | CustomTargetIncentive | CUSTOM_TARGET_INCENTIVE | — | ✅ |
| 21 | EarningDetails | EARNING_DETAILS | — | ✅ |
| 22 | EnableClassify | ENABLE_CLASSIFY | — | ✅ |
| 23 | EnableCredit | ENABLE_CREDIT | — | ✅ |
| 24 | FunctionalCurrency | FUNCTIONAL_CURRENCY | — | ✅ |
| 25 | LastUpdateDate3 | LAST_UPDATE_DATE | — | ✅ |
| 26 | LastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 27 | LastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 28 | ObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 29 | OrgId3 | ORG_ID | — | — |
| 30 | ParticipantBatchSize | PARTICIPANT_BATCH_SIZE | — | ✅ |
| 31 | PayPartBatchSize | PAY_PART_BATCH_SIZE | — | ✅ |
| 32 | PaymentConvType | PAYMENT_CONV_TYPE | — | ✅ |
| 33 | PaymentDateConv | PAYMENT_DATE_CONV | — | ✅ |
| 34 | PaymentDetails | PAYMENT_DETAILS | — | ✅ |
| 35 | PaysheetapprovalStatus | PAYSHEETAPPROVAL_STATUS | — | ✅ |
| 36 | PeriodTypeId | PERIOD_TYPE_ID | — | — |
| 37 | PlanApprovalStatus | PLAN_APPROVAL_STATUS | — | ✅ |
| 38 | ProcessCurrency | PROCESS_CURRENCY | — | ✅ |
| 39 | ReportHierarchyId | REPORT_HIERARCHY_ID | — | — |
| 40 | RepositoryId | REPOSITORY_ID | — | — |
| 41 | RepositoryType | REPOSITORY_TYPE | — | ✅ |
| 42 | ResetBalYear | RESET_BAL_YEAR | — | ✅ |
| 43 | RollupBatchSize | ROLLUP_BATCH_SIZE | — | ✅ |
| 44 | RollupUsing | ROLLUP_USING | — | ✅ |
| 45 | SrpRollupFlag | SRP_ROLLUP_FLAG | — | ✅ |
| 46 | Status | STATUS | — | ✅ |
| 47 | TrxRollupMethod | TRX_ROLLUP_METHOD | — | ✅ |
| 48 | YtdSummary | YTD_SUMMARY | — | ✅ |

### [[cn_repositories_all_tl|CN_REPOSITORIES_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy4 | CREATED_BY | — | — |
| 2 | CreationDate4 | CREATION_DATE | — | — |
| 3 | Language | LANGUAGE | — | ✅ |
| 4 | LastUpdateDate4 | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 6 | LastUpdatedBy4 | LAST_UPDATED_BY | — | — |
| 7 | ObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 8 | OrgId4 | ORG_ID | — | — |
| 9 | OrgName | ORG_NAME | — | ✅ |
| 10 | RepositoryId1 | REPOSITORY_ID | — | — |
| 11 | RepositoryName | REPOSITORY_NAME | — | ✅ |
| 12 | SourceLang | SOURCE_LANG | — | ✅ |

### [[cn_srp_comp_plans_all|CN_SRP_COMP_PLANS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApprovalStatus | APPROVAL_STATUS | — | ✅ |
| 2 | Attribute1 | ATTRIBUTE1 | — | — |
| 3 | Attribute10 | ATTRIBUTE10 | — | — |
| 4 | Attribute11 | ATTRIBUTE11 | — | — |
| 5 | Attribute12 | ATTRIBUTE12 | — | — |
| 6 | Attribute13 | ATTRIBUTE13 | — | — |
| 7 | Attribute14 | ATTRIBUTE14 | — | — |
| 8 | Attribute15 | ATTRIBUTE15 | — | — |
| 9 | Attribute2 | ATTRIBUTE2 | — | — |
| 10 | Attribute3 | ATTRIBUTE3 | — | — |
| 11 | Attribute4 | ATTRIBUTE4 | — | — |
| 12 | Attribute5 | ATTRIBUTE5 | — | — |
| 13 | Attribute6 | ATTRIBUTE6 | — | — |
| 14 | Attribute7 | ATTRIBUTE7 | — | — |
| 15 | Attribute8 | ATTRIBUTE8 | — | — |
| 16 | Attribute9 | ATTRIBUTE9 | — | — |
| 17 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 18 | CompPlanId | COMP_PLAN_ID | — | — |
| 19 | CreatedBy1 | CREATED_BY | — | — |
| 20 | CreationDate1 | CREATION_DATE | — | — |
| 21 | CustomizedFlag | CUSTOMIZED_FLAG | — | ✅ |
| 22 | EndDate1 | END_DATE | — | — |
| 23 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 24 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 25 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 26 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 27 | OrgId1 | ORG_ID | — | — |
| 28 | ParticipantId1 | PARTICIPANT_ID | — | — |
| 29 | RulePlanId | RULE_PLAN_ID | — | ✅ |
| 30 | SrpCompPlanId1 | SRP_COMP_PLAN_ID | — | — |
| 31 | SrpRuleId | SRP_RULE_ID | — | ✅ |
| 32 | SrpRuleTypeCode | SRP_RULE_TYPE_CODE | — | ✅ |
| 33 | StartDate1 | START_DATE | — | — |
| 34 | TargetIncentive | TARGET_INCENTIVE | — | ✅ |

### [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | AnalystId | ANALYST_ID | — | — |
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
| 19 | CompensationEndDate | COMPENSATION_END_DATE | — | ✅ |
| 20 | CreatedBy2 | CREATED_BY | — | — |
| 21 | CreationDate2 | CREATION_DATE | — | — |
| 22 | DisplayIdentifier | DISPLAY_IDENTIFIER | — | — |
| 23 | EndDate2 | END_DATE | — | — |
| 24 | HoldPaymentFlag | HOLD_PAYMENT_FLAG | — | ✅ |
| 25 | HoldReason | HOLD_REASON | — | ✅ |
| 26 | HrPersonNumber | HR_PERSON_NUMBER | — | ✅ |
| 27 | HrPrimaryWorkerNumber | HR_PRIMARY_WORKER_NUMBER | — | ✅ |
| 28 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 29 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 30 | LastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 31 | LastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 32 | LastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 33 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 34 | OrgId2 | ORG_ID | — | — |
| 35 | ParticipantId2 | PARTICIPANT_ID | — | — |
| 36 | ParticipantType | PARTICIPANT_TYPE | — | ✅ |
| 37 | PartyId | PARTY_ID | — | — |
| 38 | PayeeOnly | PAYEE_ONLY | — | ✅ |
| 39 | RequestId | REQUEST_ID | — | — |
| 40 | SourceSystem | SOURCE_SYSTEM | — | — |
| 41 | SourceSystemId | SOURCE_SYSTEM_ID | — | — |
| 42 | StartDate2 | START_DATE | — | — |

### [[cn_srp_subledger_all|CN_SRP_SUBLEDGER_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Balance1Bbc | BALANCE1_BBC | — | ✅ |
| 2 | Balance1Bbd | BALANCE1_BBD | — | ✅ |
| 3 | Balance1Ctd | BALANCE1_CTD | — | ✅ |
| 4 | Balance1Dtd | BALANCE1_DTD | — | ✅ |
| 5 | Balance2Bbc | BALANCE2_BBC | — | ✅ |
| 6 | Balance2Bbd | BALANCE2_BBD | — | ✅ |
| 7 | Balance2Ctd | BALANCE2_CTD | — | ✅ |
| 8 | Balance2Dtd | BALANCE2_DTD | — | ✅ |
| 9 | Balance3Bbc | BALANCE3_BBC | — | ✅ |
| 10 | Balance3Bbd | BALANCE3_BBD | — | ✅ |
| 11 | Balance3Ctd | BALANCE3_CTD | — | ✅ |
| 12 | Balance3Dtd | BALANCE3_DTD | — | ✅ |
| 13 | Balance4Bbc | BALANCE4_BBC | — | ✅ |
| 14 | Balance4Bbd | BALANCE4_BBD | — | ✅ |
| 15 | Balance4Ctd | BALANCE4_CTD | — | ✅ |
| 16 | Balance4Dtd | BALANCE4_DTD | — | ✅ |
| 17 | Balance5Bbc | BALANCE5_BBC | — | ✅ |
| 18 | Balance5Bbd | BALANCE5_BBD | — | ✅ |
| 19 | Balance5Ctd | BALANCE5_CTD | — | ✅ |
| 20 | Balance5Dtd | BALANCE5_DTD | — | ✅ |
| 21 | BonusEarnedBbc | BONUS_EARNED_BBC | — | ✅ |
| 22 | BonusEarnedBbd | BONUS_EARNED_BBD | — | ✅ |
| 23 | BonusEarnedCtd | BONUS_EARNED_CTD | — | ✅ |
| 24 | BonusEarnedDtd | BONUS_EARNED_DTD | — | ✅ |
| 25 | CashBbc | CASH_BBC | — | ✅ |
| 26 | CashBbd | CASH_BBD | — | ✅ |
| 27 | CashCtd | CASH_CTD | — | ✅ |
| 28 | CashDtd | CASH_DTD | — | ✅ |
| 29 | CommissionEarnedBbc | COMMISSION_EARNED_BBC | — | ✅ |
| 30 | CommissionEarnedBbd | COMMISSION_EARNED_BBD | — | ✅ |
| 31 | CommissionEarnedCtd | COMMISSION_EARNED_CTD | — | ✅ |
| 32 | CommissionEarnedDtd | COMMISSION_EARNED_DTD | — | ✅ |
| 33 | ConsistencyFlag | CONSISTENCY_FLAG | — | ✅ |
| 34 | CreatedBy | CREATED_BY | — | — |
| 35 | CreationDate | CREATION_DATE | — | — |
| 36 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 37 | DrawNonrecBbc | DRAW_NONREC_BBC | — | ✅ |
| 38 | DrawNonrecBbd | DRAW_NONREC_BBD | — | ✅ |
| 39 | DrawNonrecCtd | DRAW_NONREC_CTD | — | ✅ |
| 40 | DrawNonrecDtd | DRAW_NONREC_DTD | — | ✅ |
| 41 | DrawPayableBbc | DRAW_PAYABLE_BBC | — | ✅ |
| 42 | DrawPayableBbd | DRAW_PAYABLE_BBD | — | ✅ |
| 43 | DrawPayableCtd | DRAW_PAYABLE_CTD | — | ✅ |
| 44 | DrawPayableDtd | DRAW_PAYABLE_DTD | — | ✅ |
| 45 | DueBbc | DUE_BBC | — | ✅ |
| 46 | DueBbd | DUE_BBD | — | ✅ |
| 47 | DueCtd | DUE_CTD | — | ✅ |
| 48 | DueDtd | DUE_DTD | — | ✅ |
| 49 | EarningTypeId | EARNING_TYPE_ID | — | — |
| 50 | EndDate | END_DATE | — | ✅ |
| 51 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 52 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 53 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 54 | MiscEarnedBbc | MISC_EARNED_BBC | — | ✅ |
| 55 | MiscEarnedBbd | MISC_EARNED_BBD | — | ✅ |
| 56 | MiscEarnedCtd | MISC_EARNED_CTD | — | ✅ |
| 57 | MiscEarnedDtd | MISC_EARNED_DTD | — | ✅ |
| 58 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 59 | OrgId | ORG_ID | — | ✅ |
| 60 | PaidFlag | PAID_FLAG | — | ✅ |
| 61 | ParticipantId | PARTICIPANT_ID | — | ✅ |
| 62 | PayGroupId | PAY_GROUP_ID | — | — |
| 63 | PayrollDueBbc | PAYROLL_DUE_BBC | — | ✅ |
| 64 | PayrollDueBbd | PAYROLL_DUE_BBD | — | ✅ |
| 65 | PayrollDueCtd | PAYROLL_DUE_CTD | — | ✅ |
| 66 | PayrollDueDtd | PAYROLL_DUE_DTD | — | ✅ |
| 67 | PayrollTransferBbc | PAYROLL_TRANSFER_BBC | — | — |
| 68 | PayrollTransferBbd | PAYROLL_TRANSFER_BBD | — | — |
| 69 | PayrollTransferCtd | PAYROLL_TRANSFER_CTD | — | — |
| 70 | PayrollTransferDtd | PAYROLL_TRANSFER_DTD | — | — |
| 71 | PeriodId | PERIOD_ID | — | — |
| 72 | PlanComponentId | PLAN_COMPONENT_ID | — | ✅ |
| 73 | RoleId | ROLE_ID | — | — |
| 74 | SrpCompPlanId | SRP_COMP_PLAN_ID | — | — |
| 75 | SrpSubledgerId | SRP_SUBLEDGER_ID | 🔑 | ✅ |
| 76 | StartDate | START_DATE | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ParticipantFirstName | PERSON_FIRST_NAME | — | ✅ |
| 2 | ParticipantLastName | PERSON_LAST_NAME | — | ✅ |
| 3 | ParticipantName | PARTY_NAME | — | ✅ |
| 4 | ParticipantPartyPEOPartyId | PARTY_ID | — | — |
| 5 | PartyNumber | PARTY_NUMBER | — | — |
| 6 | UserGuid | USER_GUID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
