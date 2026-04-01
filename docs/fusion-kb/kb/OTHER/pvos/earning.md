---
id: DOC-OTHER-PVO-Earning
doc_type: system-doc
title: "Earning — PVO Cross-Module"
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
  - Earning
  - earning
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# Earning

## 📌 Visão Geral

View Object para extração BICC de dados de Earning. Acessa as tabelas: CN_RATE_TABLE_VALUES_ALL, CN_REPOSITORIES_ALL_B, CN_RS_RULES_ALL_TL (+9).

**Caminho:** `FscmTopModelAM.TransactionManagementAM.Earning`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 235 | 12 | 1 | 145 | 62% |

---

## 🔗 Tabelas Relacionadas

- [[cn_rate_table_values_all|CN_RATE_TABLE_VALUES_ALL]] — 8 atributos (2 BICC)
- [[cn_repositories_all_b|CN_REPOSITORIES_ALL_B]] — 4 atributos (1 BICC)
- [[cn_rs_rules_all_tl|CN_RS_RULES_ALL_TL]] — 11 atributos (6 BICC)
- [[cn_srp_comp_plans_all|CN_SRP_COMP_PLANS_ALL]] — 10 atributos (6 BICC)
- [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]] — 25 atributos (13 BICC)
- [[cn_tp_credits_all|CN_TP_CREDITS_ALL]] — 12 atributos (8 BICC)
- [[cn_tp_earnings_all_v|CN_TP_EARNINGS_ALL_V]] — 62 atributos (1 PKs, 44 BICC)
- [[cn_tp_process_codes_b|CN_TP_PROCESS_CODES_B]] — 12 atributos (6 BICC)
- [[cn_tp_process_codes_tl|CN_TP_PROCESS_CODES_TL]] — 5 atributos (4 BICC)
- [[cn_tp_transactions_all|CN_TP_TRANSACTIONS_ALL]] — 65 atributos (41 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 15 atributos (9 BICC)
- [[hz_parties|HZ_PARTIES]] — 6 atributos (5 BICC)

---

## ⚙️ Atributos

### [[cn_rate_table_values_all|CN_RATE_TABLE_VALUES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ParentRateTableValueId | PARENT_RATE_TABLE_VALUE_ID | — | — |
| 2 | RateSequence | RATE_SEQUENCE | — | ✅ |
| 3 | RateTableId | RATE_TABLE_ID | — | ✅ |
| 4 | RateTableValuePEOCommissionValue | COMMISSION_VALUE | — | — |
| 5 | RateTableValuePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | RateTableValuePEOOrgId | ORG_ID | — | — |
| 7 | RateTableValuePEORateTableValueId | RATE_TABLE_VALUE_ID | — | — |
| 8 | SrpFormRateTableId | SRP_FORM_RATE_TABLE_ID | — | — |

### [[cn_repositories_all_b|CN_REPOSITORIES_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FunctionalCurrency | FUNCTIONAL_CURRENCY | — | ✅ |
| 2 | RepositoriesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | RepositoriesPEOOrgId | ORG_ID | — | — |
| 4 | RepositoryId | REPOSITORY_ID | — | — |

### [[cn_rs_rules_all_tl|CN_RS_RULES_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClsfnRuleDescription | DESCRIPTION | — | ✅ |
| 2 | ClsfnRuleName | NAME | — | ✅ |
| 3 | ClsfnRuleTranslationPEORuleId | RULE_ID | — | — |
| 4 | CreditRuleDescription | DESCRIPTION | — | ✅ |
| 5 | CreditRuleName | NAME | — | ✅ |
| 6 | CreditRuleTranslationPEORuleId | RULE_ID | — | — |
| 7 | DirectRuleDescription | DESCRIPTION | — | ✅ |
| 8 | DirectRuleName | NAME | — | ✅ |
| 9 | RuleId | RULE_ID | — | — |
| 10 | TxnClfsnRuleId | RULE_ID | — | — |
| 11 | TxnClfsnRuleName | NAME | — | — |

### [[cn_srp_comp_plans_all|CN_SRP_COMP_PLANS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApprovalStatus | APPROVAL_STATUS | — | ✅ |
| 2 | CompPlanId | COMP_PLAN_ID | — | — |
| 3 | CustomizedFlag | CUSTOMIZED_FLAG | — | ✅ |
| 4 | EndDate | END_DATE | — | ✅ |
| 5 | RulePlanId | RULE_PLAN_ID | — | — |
| 6 | SrpCompPlanPEOSrpCompPlanId | SRP_COMP_PLAN_ID | — | — |
| 7 | SrpRuleId | SRP_RULE_ID | — | — |
| 8 | SrpRuleTypeCode | SRP_RULE_TYPE_CODE | — | ✅ |
| 9 | StartDate | START_DATE | — | ✅ |
| 10 | TargetIncentive | TARGET_INCENTIVE | — | ✅ |

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
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ParticipantPEOEndDate | END_DATE | — | ✅ |
| 10 | ParticipantPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 11 | ParticipantPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 12 | ParticipantPEOOrgId | ORG_ID | — | — |
| 13 | ParticipantPEOParticipantId | PARTICIPANT_ID | — | — |
| 14 | ParticipantPEORequestId | REQUEST_ID | — | — |
| 15 | ParticipantPEOStartDate | START_DATE | — | ✅ |
| 16 | ParticipantType | PARTICIPANT_TYPE | — | ✅ |
| 17 | PartyId | PARTY_ID | — | ✅ |
| 18 | PayeeOnly | PAYEE_ONLY | — | — |
| 19 | SourceSystem | SOURCE_SYSTEM | — | ✅ |
| 20 | SourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 21 | TxnObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | TxnPrcptAnalystId | ANALYST_ID | — | — |
| 23 | TxnPrcptParticipantId | PARTICIPANT_ID | — | — |
| 24 | TxnPrcptPartyId | PARTY_ID | — | — |
| 25 | TxnPrcptSourceSystemId | SOURCE_SYSTEM_ID | — | — |

### [[cn_tp_credits_all|CN_TP_CREDITS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreditAmtFuncCurr | CREDIT_AMT_FUNC_CURR | — | ✅ |
| 2 | CreditAmtHomeCurr | CREDIT_AMT_HOME_CURR | — | ✅ |
| 3 | CreditAmtSourceCurr | CREDIT_AMT_SOURCE_CURR | — | ✅ |
| 4 | CreditDate | CREDIT_DATE | — | ✅ |
| 5 | CreditId1 | CREDIT_ID | — | — |
| 6 | CreditRuleId | CREDIT_RULE_ID | — | — |
| 7 | CreditType | CREDIT_TYPE | — | ✅ |
| 8 | DirectRuleId | DIRECT_RULE_ID | — | — |
| 9 | RollupLevel | ROLLUP_LEVEL | — | ✅ |
| 10 | SourceCreditId | SOURCE_CREDIT_ID | — | ✅ |
| 11 | SummaryCreditId | SUMMARY_CREDIT_ID | — | — |
| 12 | TransactionAmtHomeCurr | TRANSACTION_AMT_HOME_CURR | — | ✅ |

### [[cn_tp_earnings_all_v|CN_TP_EARNINGS_ALL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustmentComments | ADJUSTMENT_COMMENTS | — | ✅ |
| 2 | AdjustmentStatus | ADJUSTMENT_STATUS | — | ✅ |
| 3 | CalcCurrencyCode | CALC_CURRENCY_CODE | — | ✅ |
| 4 | CalcToFuncCurrCnvrt | CALC_TO_FUNC_CURR_CNVRT | — | ✅ |
| 5 | CalcToHomeCurrCnvrt | CALC_TO_HOME_CURR_CNVRT | — | ✅ |
| 6 | CommAmtCalcCurr | COMM_AMT_CALC_CURR | — | ✅ |
| 7 | CommAmtFuncCurr | COMM_AMT_FUNC_CURR | — | ✅ |
| 8 | CommAmtHomeCurr | COMM_AMT_HOME_CURR | — | ✅ |
| 9 | CommissionValue | COMMISSION_VALUE | — | ✅ |
| 10 | CreatedBy | CREATED_BY | — | — |
| 11 | CreatedDuring | CREATED_DURING | — | ✅ |
| 12 | CreationDate | CREATION_DATE | — | ✅ |
| 13 | CreditAmtCalcCurr | CREDIT_AMT_CALC_CURR | — | ✅ |
| 14 | CreditFactor | CREDIT_FACTOR | — | ✅ |
| 15 | CreditId | CREDIT_ID | — | ✅ |
| 16 | CreditedParticipantId | CREDITED_PARTICIPANT_ID | — | — |
| 17 | EarningFactor | EARNING_FACTOR | — | ✅ |
| 18 | EarningId | EARNING_ID | 🔑 | ✅ |
| 19 | EarningType | EARNING_TYPE | — | ✅ |
| 20 | EarningTypeId | EARNING_TYPE_ID | — | — |
| 21 | EligibleCatId | ELIGIBLE_CAT_ID | — | — |
| 22 | ErrorReason | ERROR_REASON | — | ✅ |
| 23 | EventFactorValue | EVENT_FACTOR_VALUE | — | ✅ |
| 24 | FormulaEcatId | FORMULA_ECAT_ID | — | — |
| 25 | FormulaId | FORMULA_ID | — | — |
| 26 | FormulaWeight | FORMULA_WEIGHT | — | ✅ |
| 27 | HomeCurrencyCode | HOME_CURRENCY_CODE | — | ✅ |
| 28 | InputAchieved | INPUT_ACHIEVED | — | ✅ |
| 29 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 30 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 31 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 34 | ObjectStatus | OBJECT_STATUS | — | ✅ |
| 35 | OrgId | ORG_ID | — | ✅ |
| 36 | OutputAchieved | OUTPUT_ACHIEVED | — | ✅ |
| 37 | ParticipantId | PARTICIPANT_ID | — | — |
| 38 | PayPeriodId | PAY_PERIOD_ID | — | — |
| 39 | PendingDate | PENDING_DATE | — | ✅ |
| 40 | PendingStatus | PENDING_STATUS | — | ✅ |
| 41 | PlanComponentId | PLAN_COMPONENT_ID | — | — |
| 42 | PostingStatus | POSTING_STATUS | — | ✅ |
| 43 | ProcessCode | PROCESS_CODE | — | ✅ |
| 44 | RateTableValueId | RATE_TABLE_VALUE_ID | — | — |
| 45 | ReasonCode | REASON_CODE | — | ✅ |
| 46 | RequestId | REQUEST_ID | — | — |
| 47 | RevenueType | REVENUE_TYPE | — | ✅ |
| 48 | RoleId | ROLE_ID | — | — |
| 49 | SourceEarningId | SOURCE_EARNING_ID | — | ✅ |
| 50 | SourceEventDate | SOURCE_EVENT_DATE | — | ✅ |
| 51 | SourceEventPeriodId | SOURCE_EVENT_PERIOD_ID | — | ✅ |
| 52 | SourceOrgId | SOURCE_ORG_ID | — | — |
| 53 | SourceTrxNumber | SOURCE_TRX_NUMBER | — | ✅ |
| 54 | SplitPct | SPLIT_PCT | — | ✅ |
| 55 | SrpAlternatePayeeId | SRP_ALTERNATE_PAYEE_ID | — | — |
| 56 | SrpCompPlanId | SRP_COMP_PLAN_ID | — | — |
| 57 | TierSplits | TIER_SPLITS | — | ✅ |
| 58 | TransactionAmtCalcCurr | TRANSACTION_AMT_CALC_CURR | — | ✅ |
| 59 | TransactionId | TRANSACTION_ID | — | ✅ |
| 60 | TransactionQty | TRANSACTION_QTY | — | ✅ |
| 61 | TransactionType | TRANSACTION_TYPE | — | ✅ |
| 62 | WorkerId | WORKER_ID | — | ✅ |

### [[cn_tp_process_codes_b|CN_TP_PROCESS_CODES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CalculateFlag | CALCULATE_FLAG | — | ✅ |
| 2 | ClassificationFlag | CLASSIFICATION_FLAG | — | ✅ |
| 3 | CreditFlag | CREDIT_FLAG | — | ✅ |
| 4 | EligibleFlag | ELIGIBLE_FLAG | — | ✅ |
| 5 | EnabledFlag | ENABLED_FLAG | — | ✅ |
| 6 | ModuleId | MODULE_ID | — | — |
| 7 | ProcessCodePEOProcessCode | PROCESS_CODE | — | — |
| 8 | RollupFlag | ROLLUP_FLAG | — | ✅ |
| 9 | TxnClassificationFlag | CLASSIFICATION_FLAG | — | — |
| 10 | TxnCreditFlag | CREDIT_FLAG | — | — |
| 11 | TxnProcProcessCode | PROCESS_CODE | — | — |
| 12 | TxnRollupFlag | ROLLUP_FLAG | — | — |

### [[cn_tp_process_codes_tl|CN_TP_PROCESS_CODES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | ✅ |
| 2 | Language | LANGUAGE | — | ✅ |
| 3 | Name | NAME | — | ✅ |
| 4 | ProcessCodeTranslationPEOProcessCode | PROCESS_CODE | — | — |
| 5 | SourceLang | SOURCE_LANG | — | ✅ |

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
| 15 | NewTransactionId | NEW_TRANSACTION_ID | — | ✅ |
| 16 | OrderNumber | ORDER_NUMBER | — | ✅ |
| 17 | PostalCode | POSTAL_CODE | — | ✅ |
| 18 | PreserveCreditFlag | PRESERVE_CREDIT_FLAG | — | ✅ |
| 19 | Province | PROVINCE | — | ✅ |
| 20 | RollupDate | ROLLUP_DATE | — | ✅ |
| 21 | SalesChannel | SALES_CHANNEL | — | ✅ |
| 22 | SourceCurrencyCode | SOURCE_CURRENCY_CODE | — | ✅ |
| 23 | SourceToFuncCurrCnvrt | SOURCE_TO_FUNC_CURR_CNVRT | — | ✅ |
| 24 | SourceTrxId | SOURCE_TRX_ID | — | ✅ |
| 25 | SourceTrxLineId | SOURCE_TRX_LINE_ID | — | ✅ |
| 26 | SourceTrxSalesLineId | SOURCE_TRX_SALES_LINE_ID | — | ✅ |
| 27 | SourceType | SOURCE_TYPE | — | ✅ |
| 28 | State | STATE | — | ✅ |
| 29 | TerrId | TERR_ID | — | ✅ |
| 30 | TerrName | TERR_NAME | — | ✅ |
| 31 | TransactionAmtFuncCurr | TRANSACTION_AMT_FUNC_CURR | — | ✅ |
| 32 | TransactionAmtSourceCurr | TRANSACTION_AMT_SOURCE_CURR | — | ✅ |
| 33 | TransactionId1 | TRANSACTION_ID | — | — |
| 34 | TransactionPEOOrgId | ORG_ID | — | — |
| 35 | TransactionSubType | TRANSACTION_SUB_TYPE | — | ✅ |
| 36 | TxnAdjustmentComments | ADJUSTMENT_COMMENTS | — | ✅ |
| 37 | TxnAdjustmentStatus | ADJUSTMENT_STATUS | — | ✅ |
| 38 | TxnBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 39 | TxnBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 40 | TxnCreatedBy | CREATED_BY | — | — |
| 41 | TxnCreationDate | CREATION_DATE | — | ✅ |
| 42 | TxnCreditDate | CREDIT_DATE | — | ✅ |
| 43 | TxnEligibleCatId | ELIGIBLE_CAT_ID | — | — |
| 44 | TxnErrorCode | ERROR_CODE | — | — |
| 45 | TxnJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 46 | TxnJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 47 | TxnLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 48 | TxnLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 49 | TxnLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 50 | TxnObjectStatus | OBJECT_STATUS | — | — |
| 51 | TxnParticipantId | PARTICIPANT_ID | — | — |
| 52 | TxnProcessCode | PROCESS_CODE | — | ✅ |
| 53 | TxnReasonCode | REASON_CODE | — | — |
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
| 2 | BusinessUnitPEOName | BU_NAME | — | ✅ |
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
| 13 | PrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |
| 14 | ShortCode | SHORT_CODE | — | ✅ |
| 15 | Status | STATUS | — | ✅ |

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
