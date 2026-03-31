---
id: DOC-OTHER-PVO-Credit
doc_type: system-doc
title: "Credit — PVO Cross-Module"
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
  - Credit
  - credit
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# Credit

## 📌 Visão Geral

View Object para extração BICC de dados de Credit. Acessa as tabelas: CN_REPOSITORIES_ALL_B, CN_REPOSITORIES_ALL_TL, CN_RS_RULES_ALL_TL (+7).

**Caminho:** `FscmTopModelAM.TransactionManagementAM.Credit`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 251 | 10 | 1 | 150 | 60% |

---

## 🔗 Tabelas Relacionadas

- [[cn_repositories_all_b|CN_REPOSITORIES_ALL_B]] — 43 atributos (18 BICC)
- [[cn_repositories_all_tl|CN_REPOSITORIES_ALL_TL]] — 8 atributos (2 BICC)
- [[cn_rs_rules_all_tl|CN_RS_RULES_ALL_TL]] — 11 atributos (6 BICC)
- [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]] — 25 atributos (13 BICC)
- [[cn_tp_credits_all|CN_TP_CREDITS_ALL]] — 62 atributos (1 PKs, 47 BICC)
- [[cn_tp_process_codes_b|CN_TP_PROCESS_CODES_B]] — 12 atributos (6 BICC)
- [[cn_tp_process_codes_tl|CN_TP_PROCESS_CODES_TL]] — 5 atributos (2 BICC)
- [[cn_tp_transactions_all|CN_TP_TRANSACTIONS_ALL]] — 65 atributos (43 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 14 atributos (8 BICC)
- [[hz_parties|HZ_PARTIES]] — 6 atributos (5 BICC)

---

## ⚙️ Atributos

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
| 23 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 24 | ParticipantBatchSize | PARTICIPANT_BATCH_SIZE | — | — |
| 25 | PayPartBatchSize | PAY_PART_BATCH_SIZE | — | ✅ |
| 26 | PaymentConvType | PAYMENT_CONV_TYPE | — | ✅ |
| 27 | PaymentDateConv | PAYMENT_DATE_CONV | — | ✅ |
| 28 | PaymentDetails | PAYMENT_DETAILS | — | ✅ |
| 29 | PaysheetapprovalStatus | PAYSHEETAPPROVAL_STATUS | — | ✅ |
| 30 | PeriodTypeId | PERIOD_TYPE_ID | — | — |
| 31 | PlanApprovalStatus | PLAN_APPROVAL_STATUS | — | ✅ |
| 32 | ProcessCurrency | PROCESS_CURRENCY | — | ✅ |
| 33 | ReportHierarchyId | REPORT_HIERARCHY_ID | — | — |
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
| 1 | OrgName | ORG_NAME | — | ✅ |
| 2 | RepositoriesTLPEOLanguage | LANGUAGE | — | — |
| 3 | RepositoriesTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 4 | RepositoriesTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | RepositoriesTLPEOOrgId | ORG_ID | — | — |
| 6 | RepositoriesTLPEOSourceLang | SOURCE_LANG | — | — |
| 7 | RepositoryId | REPOSITORY_ID | — | — |
| 8 | RepositoryName | REPOSITORY_NAME | — | ✅ |

### [[cn_rs_rules_all_tl|CN_RS_RULES_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClfsnRuleDescription | DESCRIPTION | — | ✅ |
| 2 | ClfsnRuleName | NAME | — | ✅ |
| 3 | ClfsnRulesTranslationPEORuleId | RULE_ID | — | — |
| 4 | CreditRuleDescription | DESCRIPTION | — | ✅ |
| 5 | CreditRuleName | NAME | — | ✅ |
| 6 | CreditRulesTranslationPEORuleId | RULE_ID | — | — |
| 7 | DirectRuleDescription | DESCRIPTION | — | ✅ |
| 8 | DirectRuleName | NAME | — | ✅ |
| 9 | RuleId | RULE_ID | — | — |
| 10 | TxnClfsnRuleId | RULE_ID | — | — |
| 11 | TxnClfsnRuleName | NAME | — | — |

### [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AnalystId | ANALYST_ID | — | ✅ |
| 2 | CompensationEndDate | COMPENSATION_END_DATE | — | ✅ |
| 3 | DisplayIdentifier | DISPLAY_IDENTIFIER | — | ✅ |
| 4 | EndDate | END_DATE | — | ✅ |
| 5 | HoldPaymentFlag | HOLD_PAYMENT_FLAG | — | ✅ |
| 6 | HoldReason | HOLD_REASON | — | ✅ |
| 7 | HrPersonNumber | HR_PERSON_NUMBER | — | ✅ |
| 8 | HrPrimaryWorkerNumber | HR_PRIMARY_WORKER_NUMBER | — | ✅ |
| 9 | ParticipantPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 10 | ParticipantPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 11 | ParticipantPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ParticipantPEOOrgId | ORG_ID | — | — |
| 13 | ParticipantPEOParticipantId | PARTICIPANT_ID | — | — |
| 14 | ParticipantPEORequestId | REQUEST_ID | — | — |
| 15 | ParticipantType | PARTICIPANT_TYPE | — | ✅ |
| 16 | PartyId | PARTY_ID | — | ✅ |
| 17 | PayeeOnly | PAYEE_ONLY | — | — |
| 18 | SourceSystem | SOURCE_SYSTEM | — | ✅ |
| 19 | SourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 20 | StartDate | START_DATE | — | ✅ |
| 21 | TxnObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | TxnParticipantAnalystId | ANALYST_ID | — | — |
| 23 | TxnParticipantId | PARTICIPANT_ID | — | — |
| 24 | TxnParticipantPartyId | PARTY_ID | — | — |
| 25 | TxnParticipantSourceSystemId | SOURCE_SYSTEM_ID | — | — |

### [[cn_tp_credits_all|CN_TP_CREDITS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustmentComments | ADJUSTMENT_COMMENTS | — | ✅ |
| 2 | AdjustmentStatus | ADJUSTMENT_STATUS | — | ✅ |
| 3 | CalcCurrencyCode | CALC_CURRENCY_CODE | — | ✅ |
| 4 | CalcToFuncCurrCnvrt | CALC_TO_FUNC_CURR_CNVRT | — | ✅ |
| 5 | CalcToHomeCurrCnvrt | CALC_TO_HOME_CURR_CNVRT | — | ✅ |
| 6 | CalcToSourceCurrCnvrt | CALC_TO_SOURCE_CURR_CNVRT | — | ✅ |
| 7 | ChangedCreditFlag | CHANGED_CREDIT_FLAG | — | ✅ |
| 8 | ClsfnRuleId | CLSFN_RULE_ID | — | — |
| 9 | CollectionStatus | COLLECTION_STATUS | — | ✅ |
| 10 | CreatedBy | CREATED_BY | — | — |
| 11 | CreatedDuring | CREATED_DURING | — | ✅ |
| 12 | CreationDate | CREATION_DATE | — | ✅ |
| 13 | CreditAmtCalcCurr | CREDIT_AMT_CALC_CURR | — | ✅ |
| 14 | CreditAmtFuncCurr | CREDIT_AMT_FUNC_CURR | — | ✅ |
| 15 | CreditAmtHomeCurr | CREDIT_AMT_HOME_CURR | — | ✅ |
| 16 | CreditAmtSourceCurr | CREDIT_AMT_SOURCE_CURR | — | ✅ |
| 17 | CreditDate | CREDIT_DATE | — | ✅ |
| 18 | CreditHoldFlag | HOLD_FLAG | — | — |
| 19 | CreditId | CREDIT_ID | 🔑 | ✅ |
| 20 | CreditRuleId | CREDIT_RULE_ID | — | — |
| 21 | CreditType | CREDIT_TYPE | — | ✅ |
| 22 | CreditedParticipantId | CREDITED_PARTICIPANT_ID | — | ✅ |
| 23 | DirectRuleId | DIRECT_RULE_ID | — | — |
| 24 | EligibleCatId | ELIGIBLE_CAT_ID | — | — |
| 25 | ErrorCode | ERROR_CODE | — | ✅ |
| 26 | HomeCurrencyCode | HOME_CURRENCY_CODE | — | ✅ |
| 27 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 28 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 29 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 31 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 32 | NewCreditId | NEW_CREDIT_ID | — | ✅ |
| 33 | ObjectStatus | OBJECT_STATUS | — | ✅ |
| 34 | OrgId | ORG_ID | — | ✅ |
| 35 | ParticipantId | PARTICIPANT_ID | — | — |
| 36 | ProcessCode | PROCESS_CODE | — | ✅ |
| 37 | ReasonCode | REASON_CODE | — | ✅ |
| 38 | RequestId | REQUEST_ID | — | — |
| 39 | RevenueType | REVENUE_TYPE | — | ✅ |
| 40 | RoleId | ROLE_ID | — | — |
| 41 | RollupDate | ROLLUP_DATE | — | ✅ |
| 42 | RollupLevel | ROLLUP_LEVEL | — | ✅ |
| 43 | SourceCreditId | SOURCE_CREDIT_ID | — | ✅ |
| 44 | SourceCurrencyCode | SOURCE_CURRENCY_CODE | — | ✅ |
| 45 | SourceEventDate | SOURCE_EVENT_DATE | — | ✅ |
| 46 | SourceEventPeriodId | SOURCE_EVENT_PERIOD_ID | — | ✅ |
| 47 | SourceOrgId | SOURCE_ORG_ID | — | — |
| 48 | SourceToCalcCurrCnvrt | SOURCE_TO_CALC_CURR_CNVRT | — | ✅ |
| 49 | SourceToFuncCurrCnvrt | SOURCE_TO_FUNC_CURR_CNVRT | — | ✅ |
| 50 | SourceToHomeCurrCnvrt | SOURCE_TO_HOME_CURR_CNVRT | — | ✅ |
| 51 | SourceTrxNumber | SOURCE_TRX_NUMBER | — | ✅ |
| 52 | SourceType | SOURCE_TYPE | — | ✅ |
| 53 | SplitPct | SPLIT_PCT | — | ✅ |
| 54 | SummaryCreditId | SUMMARY_CREDIT_ID | — | — |
| 55 | TransactionAmtCalcCurr | TRANSACTION_AMT_CALC_CURR | — | ✅ |
| 56 | TransactionAmtFuncCurr | TRANSACTION_AMT_FUNC_CURR | — | ✅ |
| 57 | TransactionAmtHomeCurr | TRANSACTION_AMT_HOME_CURR | — | ✅ |
| 58 | TransactionAmtSourceCurr | TRANSACTION_AMT_SOURCE_CURR | — | ✅ |
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
| 11 | TxnProcessCode | PROCESS_CODE | — | — |
| 12 | TxnRollupFlag | ROLLUP_FLAG | — | — |

### [[cn_tp_process_codes_tl|CN_TP_PROCESS_CODES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcessCodeTranslationPEODescription | DESCRIPTION | — | ✅ |
| 2 | ProcessCodeTranslationPEOLanguage | LANGUAGE | — | — |
| 3 | ProcessCodeTranslationPEOName | NAME | — | ✅ |
| 4 | ProcessCodeTranslationPEOProcessCode | PROCESS_CODE | — | — |
| 5 | ProcessCodeTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[cn_tp_transactions_all|CN_TP_TRANSACTIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AreaCode | AREA_CODE | — | ✅ |
| 2 | BookedDate | BOOKED_DATE | — | ✅ |
| 3 | ChangedTrxFlag | CHANGED_TRX_FLAG | — | ✅ |
| 4 | City | CITY | — | ✅ |
| 5 | Country | COUNTRY | — | ✅ |
| 6 | CustomerId | CUSTOMER_ID | — | — |
| 7 | DiscountPercentage | DISCOUNT_PERCENTAGE | — | ✅ |
| 8 | HoldFlag | HOLD_FLAG | — | ✅ |
| 9 | InventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 10 | InvoiceDate | INVOICE_DATE | — | ✅ |
| 11 | InvoiceNumber | INVOICE_NUMBER | — | ✅ |
| 12 | MarginPercentage | MARGIN_PERCENTAGE | — | ✅ |
| 13 | NewTransactionId | NEW_TRANSACTION_ID | — | ✅ |
| 14 | OrderNumber | ORDER_NUMBER | — | ✅ |
| 15 | PostalCode | POSTAL_CODE | — | ✅ |
| 16 | PreserveCreditFlag | PRESERVE_CREDIT_FLAG | — | ✅ |
| 17 | Province | PROVINCE | — | ✅ |
| 18 | SalesChannel | SALES_CHANNEL | — | ✅ |
| 19 | SourceTrxId | SOURCE_TRX_ID | — | ✅ |
| 20 | SourceTrxLineId | SOURCE_TRX_LINE_ID | — | ✅ |
| 21 | SourceTrxSalesLineId | SOURCE_TRX_SALES_LINE_ID | — | ✅ |
| 22 | State | STATE | — | ✅ |
| 23 | TerrId | TERR_ID | — | ✅ |
| 24 | TerrName | TERR_NAME | — | ✅ |
| 25 | TransactionId1 | TRANSACTION_ID | — | ✅ |
| 26 | TransactionPEOAdjustmentComments | ADJUSTMENT_COMMENTS | — | ✅ |
| 27 | TransactionPEOAdjustmentStatus | ADJUSTMENT_STATUS | — | ✅ |
| 28 | TransactionPEOClsfnRuleId | CLSFN_RULE_ID | — | — |
| 29 | TransactionPEOCollectionStatus | COLLECTION_STATUS | — | ✅ |
| 30 | TransactionPEOCreditDate | CREDIT_DATE | — | ✅ |
| 31 | TransactionPEOEligibleCatId | ELIGIBLE_CAT_ID | — | — |
| 32 | TransactionPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 33 | TransactionPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 34 | TransactionPEOObjectStatus | OBJECT_STATUS | — | — |
| 35 | TransactionPEOOrgId | ORG_ID | — | — |
| 36 | TransactionPEOParticipantId | PARTICIPANT_ID | — | — |
| 37 | TransactionPEOProcessCode | PROCESS_CODE | — | ✅ |
| 38 | TransactionPEOReasonCode | REASON_CODE | — | ✅ |
| 39 | TransactionPEORequestId | REQUEST_ID | — | — |
| 40 | TransactionPEORoleId | ROLE_ID | — | — |
| 41 | TransactionPEORollupDate | ROLLUP_DATE | — | ✅ |
| 42 | TransactionPEOSourceCurrencyCode | SOURCE_CURRENCY_CODE | — | ✅ |
| 43 | TransactionPEOSourceEventDate | SOURCE_EVENT_DATE | — | ✅ |
| 44 | TransactionPEOSourceEventPeriodId | SOURCE_EVENT_PERIOD_ID | — | — |
| 45 | TransactionPEOSourceOrgId | SOURCE_ORG_ID | — | — |
| 46 | TransactionPEOSourceToFuncCurrCnvrt | SOURCE_TO_FUNC_CURR_CNVRT | — | ✅ |
| 47 | TransactionPEOSourceTrxNumber | SOURCE_TRX_NUMBER | — | — |
| 48 | TransactionPEOSourceType | SOURCE_TYPE | — | ✅ |
| 49 | TransactionPEOTransactionAmtFuncCurr | TRANSACTION_AMT_FUNC_CURR | — | ✅ |
| 50 | TransactionPEOTransactionAmtSourceCurr | TRANSACTION_AMT_SOURCE_CURR | — | ✅ |
| 51 | TransactionPEOTransactionQty | TRANSACTION_QTY | — | ✅ |
| 52 | TransactionPEOTransactionType | TRANSACTION_TYPE | — | — |
| 53 | TransactionPEOWorkerId | WORKER_ID | — | — |
| 54 | TransactionSubType | TRANSACTION_SUB_TYPE | — | ✅ |
| 55 | TxnBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 56 | TxnBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 57 | TxnCreatedBy | CREATED_BY | — | — |
| 58 | TxnCreationDate | CREATION_DATE | — | ✅ |
| 59 | TxnErrorCode | ERROR_CODE | — | — |
| 60 | TxnLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 61 | TxnLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 62 | TxnLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 63 | TxnShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 64 | TxnShipToContactId | SHIP_TO_CONTACT_ID | — | — |
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
