---
id: DOC-OTHER-PVO-Attainment
doc_type: system-doc
title: "Attainment — PVO Cross-Module"
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
  - Attainment
  - attainment
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# Attainment

## 📌 Visão Geral

View Object para extração BICC de dados de Attainment. Acessa as tabelas: CN_RATE_TABLE_VALUES_ALL, CN_REPOSITORIES_ALL_B, CN_REPOSITORIES_ALL_TL (+9).

**Caminho:** `FscmTopModelAM.TransactionManagementAM.Attainment`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 256 | 12 | 1 | 144 | 56% |

---

## 🔗 Tabelas Relacionadas

- [[cn_rate_table_values_all|CN_RATE_TABLE_VALUES_ALL]] — 8 atributos (1 BICC)
- [[cn_repositories_all_b|CN_REPOSITORIES_ALL_B]] — 43 atributos (18 BICC)
- [[cn_repositories_all_tl|CN_REPOSITORIES_ALL_TL]] — 8 atributos (4 BICC)
- [[cn_rs_rules_all_tl|CN_RS_RULES_ALL_TL]] — 2 atributos
- [[cn_srp_comp_plans_all|CN_SRP_COMP_PLANS_ALL]] — 11 atributos (6 BICC)
- [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]] — 25 atributos (13 BICC)
- [[cn_tp_credits_all|CN_TP_CREDITS_ALL]] — 17 atributos (12 BICC)
- [[cn_tp_measure_results_all|CN_TP_MEASURE_RESULTS_ALL]] — 52 atributos (1 PKs, 33 BICC)
- [[cn_tp_process_codes_b|CN_TP_PROCESS_CODES_B]] — 4 atributos (3 BICC)
- [[cn_tp_transactions_all|CN_TP_TRANSACTIONS_ALL]] — 65 atributos (41 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 15 atributos (8 BICC)
- [[hz_parties|HZ_PARTIES]] — 6 atributos (5 BICC)

---

## ⚙️ Atributos

### [[cn_rate_table_values_all|CN_RATE_TABLE_VALUES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ParentRateTableValueId | PARENT_RATE_TABLE_VALUE_ID | — | — |
| 2 | RateSequence | RATE_SEQUENCE | — | ✅ |
| 3 | RateTableValuePEOCommissionValue | COMMISSION_VALUE | — | — |
| 4 | RateTableValuePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | RateTableValuePEOOrgId | ORG_ID | — | — |
| 6 | RateTableValuePEORateTableId | RATE_TABLE_ID | — | — |
| 7 | RateTableValuePEORateTableValueId | RATE_TABLE_VALUE_ID | — | — |
| 8 | SrpFormRateTableId | SRP_FORM_RATE_TABLE_ID | — | — |

### [[cn_repositories_all_b|CN_REPOSITORIES_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AggrTransRollup | AGGR_TRANS_ROLLUP | — | — |
| 2 | ApplicationId | APPLICATION_ID | — | — |
| 3 | ApplicationType | APPLICATION_TYPE | — | — |
| 4 | AttainmentSummary | ATTAINMENT_SUMMARY | — | ✅ |
| 5 | AutoNotesPlanRule | AUTO_NOTES_PLAN_RULE | — | — |
| 6 | BatchRunnerStatus | BATCH_RUNNER_STATUS | — | — |
| 7 | CalendarId | CALENDAR_ID | — | — |
| 8 | ClassifyBatchOption | CLASSIFY_BATCH_OPTION | — | ✅ |
| 9 | ClassifyBatchSize | CLASSIFY_BATCH_SIZE | — | ✅ |
| 10 | ClassifyTransaction | CLASSIFY_TRANSACTION | — | ✅ |
| 11 | CnCommRatePrecision | CN_COMM_RATE_PRECISION | — | — |
| 12 | CnConversionType | CN_CONVERSION_TYPE | — | — |
| 13 | CnCustPlanCompFlag | CN_CUST_PLAN_COMP_FLAG | — | — |
| 14 | CnCustomAggrTrx | CN_CUSTOM_AGGR_TRX | — | — |
| 15 | CnDisplayDraw | CN_DISPLAY_DRAW | — | — |
| 16 | CommissionStatement | COMMISSION_STATEMENT | — | ✅ |
| 17 | CreditDetails | CREDIT_DETAILS | — | ✅ |
| 18 | CustomTargetIncentive | CUSTOM_TARGET_INCENTIVE | — | ✅ |
| 19 | EarningDetails | EARNING_DETAILS | — | ✅ |
| 20 | EnableClassify | ENABLE_CLASSIFY | — | — |
| 21 | EnableCredit | ENABLE_CREDIT | — | — |
| 22 | FunctionalCurrency | FUNCTIONAL_CURRENCY | — | ✅ |
| 23 | ParticipantBatchSize | PARTICIPANT_BATCH_SIZE | — | — |
| 24 | PayPartBatchSize | PAY_PART_BATCH_SIZE | — | ✅ |
| 25 | PaymentConvType | PAYMENT_CONV_TYPE | — | ✅ |
| 26 | PaymentDateConv | PAYMENT_DATE_CONV | — | ✅ |
| 27 | PaymentDetails | PAYMENT_DETAILS | — | ✅ |
| 28 | PaysheetapprovalStatus | PAYSHEETAPPROVAL_STATUS | — | ✅ |
| 29 | PeriodTypeId | PERIOD_TYPE_ID | — | — |
| 30 | PlanApprovalStatus | PLAN_APPROVAL_STATUS | — | ✅ |
| 31 | ProcessCurrency | PROCESS_CURRENCY | — | ✅ |
| 32 | ReportHierarchyId | REPORT_HIERARCHY_ID | — | — |
| 33 | RepositoriesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 34 | RepositoriesPEOOrgId | ORG_ID | — | — |
| 35 | RepositoriesPEORepositoryId | REPOSITORY_ID | — | — |
| 36 | RepositoryType | REPOSITORY_TYPE | — | — |
| 37 | ResetBalYear | RESET_BAL_YEAR | — | — |
| 38 | RollupBatchSize | ROLLUP_BATCH_SIZE | — | ✅ |
| 39 | RollupUsing | ROLLUP_USING | — | — |
| 40 | SrpRollupFlag | SRP_ROLLUP_FLAG | — | — |
| 41 | Status | STATUS | — | ✅ |
| 42 | TrxRollupMethod | TRX_ROLLUP_METHOD | — | — |
| 43 | YtdSummary | YTD_SUMMARY | — | — |

### [[cn_repositories_all_tl|CN_REPOSITORIES_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | — | ✅ |
| 2 | OrgName | ORG_NAME | — | ✅ |
| 3 | RepositoriesTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 4 | RepositoriesTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | RepositoriesTLPEOOrgId | ORG_ID | — | — |
| 6 | RepositoryId | REPOSITORY_ID | — | — |
| 7 | RepositoryName | REPOSITORY_NAME | — | ✅ |
| 8 | SourceLang | SOURCE_LANG | — | ✅ |

### [[cn_rs_rules_all_tl|CN_RS_RULES_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TxnClfsnRuleId | RULE_ID | — | — |
| 2 | TxnClfsnRuleName | NAME | — | — |

### [[cn_srp_comp_plans_all|CN_SRP_COMP_PLANS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApprovalStatus | APPROVAL_STATUS | — | ✅ |
| 2 | CompPlanId | COMP_PLAN_ID | — | — |
| 3 | CustomizedFlag | CUSTOMIZED_FLAG | — | ✅ |
| 4 | EndDate | END_DATE | — | ✅ |
| 5 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | RulePlanId | RULE_PLAN_ID | — | — |
| 7 | SrpCompPlanPEOSrpCompPlanId | SRP_COMP_PLAN_ID | — | — |
| 8 | SrpRuleId | SRP_RULE_ID | — | — |
| 9 | SrpRuleTypeCode | SRP_RULE_TYPE_CODE | — | ✅ |
| 10 | StartDate | START_DATE | — | ✅ |
| 11 | TargetIncentive | TARGET_INCENTIVE | — | ✅ |

### [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AnalystId | ANALYST_ID | — | ✅ |
| 2 | CompensationEndDate | COMPENSATION_END_DATE | — | ✅ |
| 3 | DisplayIdentifier | DISPLAY_IDENTIFIER | — | ✅ |
| 4 | HoldPaymentFlag | HOLD_PAYMENT_FLAG | — | ✅ |
| 5 | HoldReason | HOLD_REASON | — | ✅ |
| 6 | HrPersonNumber | HR_PERSON_NUMBER | — | ✅ |
| 7 | HrPrimaryWorkerNumber | HR_PRIMARY_WORKER_NUMBER | — | ✅ |
| 8 | ParticipantPEOEndDate | END_DATE | — | ✅ |
| 9 | ParticipantPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 10 | ParticipantPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 11 | ParticipantPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ParticipantPEOOrgId | ORG_ID | — | — |
| 13 | ParticipantPEOParticipantId | PARTICIPANT_ID | — | — |
| 14 | ParticipantPEORequestId | REQUEST_ID | — | — |
| 15 | ParticipantPEOStartDate | START_DATE | — | ✅ |
| 16 | ParticipantType | PARTICIPANT_TYPE | — | ✅ |
| 17 | PartyId | PARTY_ID | — | ✅ |
| 18 | PayeeOnly | PAYEE_ONLY | — | — |
| 19 | SourceSystem | SOURCE_SYSTEM | — | ✅ |
| 20 | SourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 21 | TxnPrcptAnalystId | ANALYST_ID | — | — |
| 22 | TxnPrcptObjectVersionNum | OBJECT_VERSION_NUMBER | — | — |
| 23 | TxnPrcptParticipantId | PARTICIPANT_ID | — | — |
| 24 | TxnPrcptPartyId | PARTY_ID | — | — |
| 25 | TxnPrcptSourceSystemId | SOURCE_SYSTEM_ID | — | — |

### [[cn_tp_credits_all|CN_TP_CREDITS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangedCreditFlag | CHANGED_CREDIT_FLAG | — | ✅ |
| 2 | CreditAmtFuncCurr | CREDIT_AMT_FUNC_CURR | — | ✅ |
| 3 | CreditAmtHomeCurr | CREDIT_AMT_HOME_CURR | — | ✅ |
| 4 | CreditAmtSourceCurr | CREDIT_AMT_SOURCE_CURR | — | ✅ |
| 5 | CreditDate | CREDIT_DATE | — | ✅ |
| 6 | CreditId1 | CREDIT_ID | — | — |
| 7 | CreditRuleId | CREDIT_RULE_ID | — | — |
| 8 | CreditType | CREDIT_TYPE | — | ✅ |
| 9 | DirectRuleId | DIRECT_RULE_ID | — | — |
| 10 | HomeCurrencyCode | HOME_CURRENCY_CODE | — | ✅ |
| 11 | NewCreditId | NEW_CREDIT_ID | — | — |
| 12 | RollupLevel | ROLLUP_LEVEL | — | ✅ |
| 13 | SourceCreditId | SOURCE_CREDIT_ID | — | ✅ |
| 14 | SourceToCalcCurrCnvrt | SOURCE_TO_CALC_CURR_CNVRT | — | ✅ |
| 15 | SourceToHomeCurrCnvrt | SOURCE_TO_HOME_CURR_CNVRT | — | ✅ |
| 16 | SummaryCreditId | SUMMARY_CREDIT_ID | — | — |
| 17 | TransactionAmtHomeCurr | TRANSACTION_AMT_HOME_CURR | — | ✅ |

### [[cn_tp_measure_results_all|CN_TP_MEASURE_RESULTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustmentComments | ADJUSTMENT_COMMENTS | — | ✅ |
| 2 | AdjustmentStatus | ADJUSTMENT_STATUS | — | ✅ |
| 3 | CalcCurrencyCode | CALC_CURRENCY_CODE | — | ✅ |
| 4 | CommissionValue | COMMISSION_VALUE | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | — |
| 6 | CreatedDuring | CREATED_DURING | — | ✅ |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | CreditAmtCalcCurr | CREDIT_AMT_CALC_CURR | — | ✅ |
| 9 | CreditFactor | CREDIT_FACTOR | — | ✅ |
| 10 | CreditId | CREDIT_ID | — | ✅ |
| 11 | CreditedParticipantId | CREDITED_PARTICIPANT_ID | — | — |
| 12 | EarningFactor | EARNING_FACTOR | — | ✅ |
| 13 | EarningId | EARNING_ID | — | — |
| 14 | EarningTypeId | EARNING_TYPE_ID | — | — |
| 15 | EligibleCatId | ELIGIBLE_CAT_ID | — | — |
| 16 | ErrorReason | ERROR_REASON | — | ✅ |
| 17 | EventFactorValue | EVENT_FACTOR_VALUE | — | ✅ |
| 18 | FormulaEcatId | FORMULA_ECAT_ID | — | — |
| 19 | FormulaId | FORMULA_ID | — | — |
| 20 | FormulaWeight | FORMULA_WEIGHT | — | ✅ |
| 21 | GrpByMeasureResultId | GRP_BY_MEASURE_RESULT_ID | — | — |
| 22 | InputAchieved | INPUT_ACHIEVED | — | ✅ |
| 23 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 24 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 25 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 27 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 28 | MeasureResultId | MEASURE_RESULT_ID | 🔑 | ✅ |
| 29 | MeasureType | MEASURE_TYPE | — | ✅ |
| 30 | ObjectStatus | OBJECT_STATUS | — | ✅ |
| 31 | OrgId | ORG_ID | — | ✅ |
| 32 | OutputAchieved | OUTPUT_ACHIEVED | — | ✅ |
| 33 | ParticipantId | PARTICIPANT_ID | — | — |
| 34 | PlanComponentId | PLAN_COMPONENT_ID | — | — |
| 35 | RateTableValueId | RATE_TABLE_VALUE_ID | — | — |
| 36 | ReasonCode | REASON_CODE | — | ✅ |
| 37 | RequestId | REQUEST_ID | — | — |
| 38 | RevenueType | REVENUE_TYPE | — | ✅ |
| 39 | RoleId | ROLE_ID | — | — |
| 40 | SourceEventDate | SOURCE_EVENT_DATE | — | ✅ |
| 41 | SourceEventPeriodId | SOURCE_EVENT_PERIOD_ID | — | ✅ |
| 42 | SourceMeasureResultId | SOURCE_MEASURE_RESULT_ID | — | ✅ |
| 43 | SourceOrgId | SOURCE_ORG_ID | — | — |
| 44 | SourceTrxNumber | SOURCE_TRX_NUMBER | — | ✅ |
| 45 | SplitPct | SPLIT_PCT | — | ✅ |
| 46 | SrpCompPlanId | SRP_COMP_PLAN_ID | — | — |
| 47 | TierSplits | TIER_SPLITS | — | ✅ |
| 48 | TransactionAmtCalcCurr | TRANSACTION_AMT_CALC_CURR | — | ✅ |
| 49 | TransactionId | TRANSACTION_ID | — | ✅ |
| 50 | TransactionQty | TRANSACTION_QTY | — | ✅ |
| 51 | TransactionType | TRANSACTION_TYPE | — | ✅ |
| 52 | WorkerId | WORKER_ID | — | ✅ |

### [[cn_tp_process_codes_b|CN_TP_PROCESS_CODES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClassificationFlag | CLASSIFICATION_FLAG | — | ✅ |
| 2 | CreditFlag | CREDIT_FLAG | — | ✅ |
| 3 | ProcessCode1 | PROCESS_CODE | — | — |
| 4 | RollupFlag | ROLLUP_FLAG | — | ✅ |

### [[cn_tp_transactions_all|CN_TP_TRANSACTIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AreaCode | AREA_CODE | — | ✅ |
| 2 | BookedDate | BOOKED_DATE | — | ✅ |
| 3 | ChangedTrxFlag | CHANGED_TRX_FLAG | — | ✅ |
| 4 | City | CITY | — | ✅ |
| 5 | ClsfnRuleId | CLSFN_RULE_ID | — | — |
| 6 | CollectionStatus | COLLECTION_STATUS | — | ✅ |
| 7 | Country | COUNTRY | — | ✅ |
| 8 | CustomerId | CUSTOMER_ID | — | — |
| 9 | DiscountPercentage | DISCOUNT_PERCENTAGE | — | ✅ |
| 10 | HoldFlag | HOLD_FLAG | — | ✅ |
| 11 | InventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 12 | InvoiceDate | INVOICE_DATE | — | ✅ |
| 13 | InvoiceNumber | INVOICE_NUMBER | — | ✅ |
| 14 | MarginPercentage | MARGIN_PERCENTAGE | — | ✅ |
| 15 | NewTransactionId | NEW_TRANSACTION_ID | — | — |
| 16 | OrderNumber | ORDER_NUMBER | — | ✅ |
| 17 | PostalCode | POSTAL_CODE | — | ✅ |
| 18 | PreserveCreditFlag | PRESERVE_CREDIT_FLAG | — | ✅ |
| 19 | ProcessCode | PROCESS_CODE | — | ✅ |
| 20 | Province | PROVINCE | — | ✅ |
| 21 | RollupDate | ROLLUP_DATE | — | ✅ |
| 22 | SalesChannel | SALES_CHANNEL | — | ✅ |
| 23 | SourceCurrencyCode | SOURCE_CURRENCY_CODE | — | ✅ |
| 24 | SourceToFuncCurrCnvrt | SOURCE_TO_FUNC_CURR_CNVRT | — | ✅ |
| 25 | SourceTrxId | SOURCE_TRX_ID | — | ✅ |
| 26 | SourceTrxLineId | SOURCE_TRX_LINE_ID | — | ✅ |
| 27 | SourceTrxSalesLineId | SOURCE_TRX_SALES_LINE_ID | — | ✅ |
| 28 | SourceType | SOURCE_TYPE | — | ✅ |
| 29 | State | STATE | — | ✅ |
| 30 | TerrId | TERR_ID | — | ✅ |
| 31 | TerrName | TERR_NAME | — | ✅ |
| 32 | TransactionAmtFuncCurr | TRANSACTION_AMT_FUNC_CURR | — | ✅ |
| 33 | TransactionAmtSourceCurr | TRANSACTION_AMT_SOURCE_CURR | — | ✅ |
| 34 | TransactionId1 | TRANSACTION_ID | — | — |
| 35 | TransactionPEOOrgId | ORG_ID | — | — |
| 36 | TransactionSubType | TRANSACTION_SUB_TYPE | — | ✅ |
| 37 | TxnAdjustmentComments | ADJUSTMENT_COMMENTS | — | ✅ |
| 38 | TxnAdjustmentStatus | ADJUSTMENT_STATUS | — | ✅ |
| 39 | TxnBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 40 | TxnBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 41 | TxnCreatedBy | CREATED_BY | — | — |
| 42 | TxnCreationDate | CREATION_DATE | — | ✅ |
| 43 | TxnCreditDate | CREDIT_DATE | — | ✅ |
| 44 | TxnEligibleCatId | ELIGIBLE_CAT_ID | — | — |
| 45 | TxnErrorCode | ERROR_CODE | — | — |
| 46 | TxnJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 47 | TxnJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 48 | TxnLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 49 | TxnLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 50 | TxnLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 51 | TxnObjectStatus | OBJECT_STATUS | — | — |
| 52 | TxnParticipantId | PARTICIPANT_ID | — | — |
| 53 | TxnReasonCode | REASON_CODE | — | ✅ |
| 54 | TxnRequestId | REQUEST_ID | — | — |
| 55 | TxnRoleId | ROLE_ID | — | — |
| 56 | TxnShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 57 | TxnShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 58 | TxnSourceEventDate | SOURCE_EVENT_DATE | — | ✅ |
| 59 | TxnSourceEventPeriodId | SOURCE_EVENT_PERIOD_ID | — | — |
| 60 | TxnSourceOrgId | SOURCE_ORG_ID | — | — |
| 61 | TxnSourceTrxNumber | SOURCE_TRX_NUMBER | — | — |
| 62 | TxnTransactionQty | TRANSACTION_QTY | — | — |
| 63 | TxnTransactionType | TRANSACTION_TYPE | — | — |
| 64 | TxnWorkerId | WORKER_ID | — | ✅ |
| 65 | UomCode | UOM_CODE | — | ✅ |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitId | BU_ID | — | — |
| 2 | BusinessUnitPEOStatus | STATUS | — | — |
| 3 | DateFrom | DATE_FROM | — | ✅ |
| 4 | DateTo | DATE_TO | — | ✅ |
| 5 | DefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | ✅ |
| 6 | DefaultSetId | DEFAULT_SET_ID | — | — |
| 7 | EnabledForHrFlag | ENABLED_FOR_HR_FLAG | — | ✅ |
| 8 | EnterpriseId | BUSINESS_GROUP_ID | — | — |
| 9 | FinancialsBusinessUnitId | FIN_BUSINESS_UNIT_ID | — | — |
| 10 | LegalEntityId | LEGAL_ENTITY_ID | — | — |
| 11 | LocationId | LOCATION_ID | — | ✅ |
| 12 | ManagerId | MANAGER_ID | — | ✅ |
| 13 | Name | BU_NAME | — | ✅ |
| 14 | PrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |
| 15 | ShortCode | SHORT_CODE | — | ✅ |

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
