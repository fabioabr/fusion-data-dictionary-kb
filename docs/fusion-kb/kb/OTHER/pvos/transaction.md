---
id: DOC-OTHER-PVO-Transaction
doc_type: system-doc
title: "Transaction — PVO Cross-Module"
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
  - Transaction
  - transaction
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# Transaction

## 📌 Visão Geral

View Object para extração BICC de dados de Transaction. Acessa as tabelas: CN_REPOSITORIES_ALL_B, CN_RS_RULES_ALL_TL, CN_SRP_PARTICIPANTS_ALL (+5).

**Caminho:** `FscmTopModelAM.TransactionManagementAM.Transaction`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 165 | 8 | 1 | 110 | 67% |

---

## 🔗 Tabelas Relacionadas

- [[cn_repositories_all_b|CN_REPOSITORIES_ALL_B]] — 43 atributos (18 BICC)
- [[cn_rs_rules_all_tl|CN_RS_RULES_ALL_TL]] — 3 atributos (2 BICC)
- [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]] — 20 atributos (13 BICC)
- [[cn_tp_process_codes_b|CN_TP_PROCESS_CODES_B]] — 8 atributos (6 BICC)
- [[cn_tp_process_codes_tl|CN_TP_PROCESS_CODES_TL]] — 5 atributos (4 BICC)
- [[cn_tp_transactions_all|CN_TP_TRANSACTIONS_ALL]] — 65 atributos (1 PKs, 53 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 15 atributos (9 BICC)
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
| 23 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
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
| 35 | RepositoriesPEOStatus | STATUS | — | ✅ |
| 36 | RepositoryId | REPOSITORY_ID | — | — |
| 37 | RepositoryType | REPOSITORY_TYPE | — | — |
| 38 | ResetBalYear | RESET_BAL_YEAR | — | — |
| 39 | RollupBatchSize | ROLLUP_BATCH_SIZE | — | ✅ |
| 40 | RollupUsing | ROLLUP_USING | — | — |
| 41 | SrpRollupFlag | SRP_ROLLUP_FLAG | — | — |
| 42 | TrxRollupMethod | TRX_ROLLUP_METHOD | — | — |
| 43 | YtdSummary | YTD_SUMMARY | — | — |

### [[cn_rs_rules_all_tl|CN_RS_RULES_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RuleId | RULE_ID | — | — |
| 2 | RulesTranslationPEODescription | DESCRIPTION | — | ✅ |
| 3 | RulesTranslationPEOName | NAME | — | ✅ |

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
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ParticipantPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 11 | ParticipantPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 12 | ParticipantPEOOrgId | ORG_ID | — | — |
| 13 | ParticipantPEOParticipantId | PARTICIPANT_ID | — | — |
| 14 | ParticipantPEORequestId | REQUEST_ID | — | — |
| 15 | ParticipantType | PARTICIPANT_TYPE | — | ✅ |
| 16 | PartyId | PARTY_ID | — | ✅ |
| 17 | PayeeOnly | PAYEE_ONLY | — | — |
| 18 | SourceSystem | SOURCE_SYSTEM | — | ✅ |
| 19 | SourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 20 | StartDate | START_DATE | — | ✅ |

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
| 1 | AdjustmentComments | ADJUSTMENT_COMMENTS | — | ✅ |
| 2 | AdjustmentStatus | ADJUSTMENT_STATUS | — | ✅ |
| 3 | AreaCode | AREA_CODE | — | ✅ |
| 4 | BillToAddressId | BILL_TO_ADDRESS_ID | — | ✅ |
| 5 | BillToContactId | BILL_TO_CONTACT_ID | — | ✅ |
| 6 | BookedDate | BOOKED_DATE | — | ✅ |
| 7 | ChangedTrxFlag | CHANGED_TRX_FLAG | — | ✅ |
| 8 | City | CITY | — | ✅ |
| 9 | ClsfnRuleId | CLSFN_RULE_ID | — | — |
| 10 | CollectionStatus | COLLECTION_STATUS | — | ✅ |
| 11 | Country | COUNTRY | — | ✅ |
| 12 | CreatedBy | CREATED_BY | — | — |
| 13 | CreationDate | CREATION_DATE | — | ✅ |
| 14 | CreditDate | CREDIT_DATE | — | ✅ |
| 15 | CustomerId | CUSTOMER_ID | — | — |
| 16 | DiscountPercentage | DISCOUNT_PERCENTAGE | — | ✅ |
| 17 | EligibleCatId | ELIGIBLE_CAT_ID | — | — |
| 18 | ErrorCode | ERROR_CODE | — | ✅ |
| 19 | HoldFlag | HOLD_FLAG | — | ✅ |
| 20 | InventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 21 | InvoiceDate | INVOICE_DATE | — | ✅ |
| 22 | InvoiceNumber | INVOICE_NUMBER | — | ✅ |
| 23 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 24 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 25 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 27 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 28 | MarginPercentage | MARGIN_PERCENTAGE | — | ✅ |
| 29 | NewTransactionId | NEW_TRANSACTION_ID | — | — |
| 30 | ObjectStatus | OBJECT_STATUS | — | ✅ |
| 31 | OrderNumber | ORDER_NUMBER | — | ✅ |
| 32 | OrgId | ORG_ID | — | ✅ |
| 33 | ParticipantId | PARTICIPANT_ID | — | — |
| 34 | PostalCode | POSTAL_CODE | — | ✅ |
| 35 | PreserveCreditFlag | PRESERVE_CREDIT_FLAG | — | ✅ |
| 36 | ProcessCode | PROCESS_CODE | — | ✅ |
| 37 | Province | PROVINCE | — | ✅ |
| 38 | ReasonCode | REASON_CODE | — | ✅ |
| 39 | RequestId | REQUEST_ID | — | — |
| 40 | RoleId | ROLE_ID | — | — |
| 41 | RollupDate | ROLLUP_DATE | — | ✅ |
| 42 | SalesChannel | SALES_CHANNEL | — | ✅ |
| 43 | ShipToAddressId | SHIP_TO_ADDRESS_ID | — | ✅ |
| 44 | ShipToContactId | SHIP_TO_CONTACT_ID | — | ✅ |
| 45 | SourceCurrencyCode | SOURCE_CURRENCY_CODE | — | ✅ |
| 46 | SourceEventDate | SOURCE_EVENT_DATE | — | ✅ |
| 47 | SourceEventPeriodId | SOURCE_EVENT_PERIOD_ID | — | ✅ |
| 48 | SourceOrgId | SOURCE_ORG_ID | — | — |
| 49 | SourceToFuncCurrCnvrt | SOURCE_TO_FUNC_CURR_CNVRT | — | ✅ |
| 50 | SourceTrxId | SOURCE_TRX_ID | — | ✅ |
| 51 | SourceTrxLineId | SOURCE_TRX_LINE_ID | — | ✅ |
| 52 | SourceTrxNumber | SOURCE_TRX_NUMBER | — | ✅ |
| 53 | SourceTrxSalesLineId | SOURCE_TRX_SALES_LINE_ID | — | ✅ |
| 54 | SourceType | SOURCE_TYPE | — | ✅ |
| 55 | State | STATE | — | ✅ |
| 56 | TerrId | TERR_ID | — | ✅ |
| 57 | TerrName | TERR_NAME | — | ✅ |
| 58 | TransactionAmtFuncCurr | TRANSACTION_AMT_FUNC_CURR | — | ✅ |
| 59 | TransactionAmtSourceCurr | TRANSACTION_AMT_SOURCE_CURR | — | ✅ |
| 60 | TransactionId | TRANSACTION_ID | 🔑 | ✅ |
| 61 | TransactionQty | TRANSACTION_QTY | — | ✅ |
| 62 | TransactionSubType | TRANSACTION_SUB_TYPE | — | ✅ |
| 63 | TransactionType | TRANSACTION_TYPE | — | ✅ |
| 64 | UomCode | UOM_CODE | — | ✅ |
| 65 | WorkerId | WORKER_ID | — | ✅ |

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
