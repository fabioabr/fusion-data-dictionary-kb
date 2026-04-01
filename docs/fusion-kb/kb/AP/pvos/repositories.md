---
id: DOC-AP-PVO-Repositories
doc_type: system-doc
title: "Repositories — PVO Accounts Payable"
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
  - Repositories
  - repositories
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# Repositories

## 📌 Visão Geral

Extrai os repositórios de dados de compensação por incentivos (ICM), incluindo configurações, períodos de coleta, participantes e regras de processamento. Permite administrar e auditar os repositórios que armazenam dados de vendas e transações para cálculo de comissões.

**Caminho:** `FscmTopModelAM.ApplicationSetupAM.Repositories`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 78 | 2 | 2 | 78 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cn_repositories_all_b|CN_REPOSITORIES_ALL_B]] — 66 atributos (2 PKs, 66 BICC)
- [[cn_repositories_all_tl|CN_REPOSITORIES_ALL_TL]] — 12 atributos (12 BICC)

---

## ⚙️ Atributos

### [[cn_repositories_all_b|CN_REPOSITORIES_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AggrTransRollup | AGGR_TRANS_ROLLUP | — | ✅ |
| 2 | AnalystHierarchyDepth | ANALYST_HIERARCHY_DEPTH | — | ✅ |
| 3 | AnalystSecurity | ANALYST_SECURITY | — | ✅ |
| 4 | ApplicationId | APPLICATION_ID | — | ✅ |
| 5 | ApplicationType | APPLICATION_TYPE | — | ✅ |
| 6 | AttainmentSummary | ATTAINMENT_SUMMARY | — | ✅ |
| 7 | AutoNotesPlanRule | AUTO_NOTES_PLAN_RULE | — | ✅ |
| 8 | BatchRunnerStatus | BATCH_RUNNER_STATUS | — | ✅ |
| 9 | CalcBatchSize | CALC_BATCH_SIZE | — | ✅ |
| 10 | CalendarId | CALENDAR_ID | — | ✅ |
| 11 | ClassifyBatchOption | CLASSIFY_BATCH_OPTION | — | ✅ |
| 12 | ClassifyBatchSize | CLASSIFY_BATCH_SIZE | — | ✅ |
| 13 | ClassifyTransaction | CLASSIFY_TRANSACTION | — | ✅ |
| 14 | CnCommRatePrecision | CN_COMM_RATE_PRECISION | — | ✅ |
| 15 | CnConversionType | CN_CONVERSION_TYPE | — | ✅ |
| 16 | CnCustPlanCompFlag | CN_CUST_PLAN_COMP_FLAG | — | ✅ |
| 17 | CnCustomAggrTrx | CN_CUSTOM_AGGR_TRX | — | ✅ |
| 18 | CnDisplayDraw | CN_DISPLAY_DRAW | — | ✅ |
| 19 | CollCanTrxZero | COLL_CAN_TRX_ZERO | — | ✅ |
| 20 | CollConvType | COLL_CONV_TYPE | — | ✅ |
| 21 | CommissionStatement | COMMISSION_STATEMENT | — | ✅ |
| 22 | CreatedBy | CREATED_BY | — | ✅ |
| 23 | CreationDate | CREATION_DATE | — | ✅ |
| 24 | CreditDetails | CREDIT_DETAILS | — | ✅ |
| 25 | CustomRollupProcedure | CUSTOM_ROLLUP_PROCEDURE | — | ✅ |
| 26 | CustomTargetIncentive | CUSTOM_TARGET_INCENTIVE | — | ✅ |
| 27 | DefaultPlanDocTemplate | DEFAULT_PLAN_DOC_TEMPLATE | — | ✅ |
| 28 | EarningDetails | EARNING_DETAILS | — | ✅ |
| 29 | EnableClassify | ENABLE_CLASSIFY | — | ✅ |
| 30 | EnableCredit | ENABLE_CREDIT | — | ✅ |
| 31 | EnableNegativePay | ENABLE_NEGATIVE_PAY | — | ✅ |
| 32 | FunctionalCurrency | FUNCTIONAL_CURRENCY | — | ✅ |
| 33 | HrSuperHierarchyDepth | HR_SUPER_HIERARCHY_DEPTH | — | ✅ |
| 34 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 35 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 36 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 37 | MaxPmtApprAmt | MAX_PMT_APPR_AMT | — | ✅ |
| 38 | MinPmtApprAmt | MIN_PMT_APPR_AMT | — | ✅ |
| 39 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 40 | OrgId | ORG_ID | 🔑 | ✅ |
| 41 | ParticipantBatchSize | PARTICIPANT_BATCH_SIZE | — | ✅ |
| 42 | PayPartBatchSize | PAY_PART_BATCH_SIZE | — | ✅ |
| 43 | PaymentConvType | PAYMENT_CONV_TYPE | — | ✅ |
| 44 | PaymentDateConv | PAYMENT_DATE_CONV | — | ✅ |
| 45 | PaymentDetails | PAYMENT_DETAILS | — | ✅ |
| 46 | PaymentHomeCurrencyAmount | PAYMENT_HOME_CURRENCY_AMOUNT | — | ✅ |
| 47 | PaysheetapprovalStatus | PAYSHEETAPPROVAL_STATUS | — | ✅ |
| 48 | PeriodTypeId | PERIOD_TYPE_ID | — | ✅ |
| 49 | PlanApprovalEnableFlag | PLAN_APPROVAL_ENABLE_FLAG | — | ✅ |
| 50 | PlanApprovalStatus | PLAN_APPROVAL_STATUS | — | ✅ |
| 51 | PlanCompCustomizedOption | CN_CUST_PLAN_COMP_OPTION | — | ✅ |
| 52 | PlanImportResolve | PLAN_IMPORT_RESOLVE | — | ✅ |
| 53 | ProcessCurrency | PROCESS_CURRENCY | — | ✅ |
| 54 | ReportHierarchyId | REPORT_HIERARCHY_ID | — | ✅ |
| 55 | RepositoryId | REPOSITORY_ID | 🔑 | ✅ |
| 56 | RepositoryType | REPOSITORY_TYPE | — | ✅ |
| 57 | ResetBalYear | RESET_BAL_YEAR | — | ✅ |
| 58 | RoleAsgnReviewNew | ROLE_ASGN_REVIEW_NEW | — | ✅ |
| 59 | RoleAsgnReviewOld | ROLE_ASGN_REVIEW_OLD | — | ✅ |
| 60 | RollupBatchSize | ROLLUP_BATCH_SIZE | — | ✅ |
| 61 | RollupUsing | ROLLUP_USING | — | ✅ |
| 62 | SrpRollupFlag | SRP_ROLLUP_FLAG | — | ✅ |
| 63 | Status | STATUS | — | ✅ |
| 64 | TrxCalcMethod | TRX_CALC_METHOD | — | ✅ |
| 65 | TrxRollupMethod | TRX_ROLLUP_METHOD | — | ✅ |
| 66 | YtdSummary | YTD_SUMMARY | — | ✅ |

### [[cn_repositories_all_tl|CN_REPOSITORIES_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReposTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ReposTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ReposTLPEOLanguage | LANGUAGE | — | ✅ |
| 4 | ReposTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ReposTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | ReposTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ReposTLPEOObjVerNum | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | ReposTLPEOOrgId | ORG_ID | — | ✅ |
| 9 | ReposTLPEOOrgName | ORG_NAME | — | ✅ |
| 10 | ReposTLPEORepositoryId | REPOSITORY_ID | — | ✅ |
| 11 | ReposTLPEORepositoryName | REPOSITORY_NAME | — | ✅ |
| 12 | ReposTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
