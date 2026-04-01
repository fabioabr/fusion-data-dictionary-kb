---
id: DOC-OTHER-PVO-PrePaymentCosting
doc_type: system-doc
title: "PrePaymentCosting — PVO Cross-Module"
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
  - PrePaymentCosting
  - prepaymentcosting
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PrePaymentCosting

## 📌 Visão Geral

View Object para extração BICC de dados de Pre Payment Costing. Acessa as tabelas: PAY_PAYMENT_COSTS, PAY_PAYROLL_ACTIONS, PAY_PAYROLL_REL_ACTIONS (+4).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.CostResultsAM.PrePaymentCosting`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 106 | 7 | 1 | 40 | 38% |

---

## 🔗 Tabelas Relacionadas

- [[pay_payment_costs|PAY_PAYMENT_COSTS]] — 10 atributos (1 PKs, 7 BICC)
- [[pay_payroll_actions|PAY_PAYROLL_ACTIONS]] — 39 atributos (20 BICC)
- [[pay_payroll_rel_actions|PAY_PAYROLL_REL_ACTIONS]] — 14 atributos (5 BICC)
- [[pay_pay_relationships_dn|PAY_PAY_RELATIONSHIPS_DN]] — 14 atributos (4 BICC)
- [[pay_pre_payments|PAY_PRE_PAYMENTS]] — 14 atributos (2 BICC)
- [[pay_requests|PAY_REQUESTS]] — 13 atributos (2 BICC)
- [[per_legislative_data_groups|PER_LEGISLATIVE_DATA_GROUPS]] — 2 atributos

---

## ⚙️ Atributos

### [[pay_payment_costs|PAY_PAYMENT_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentCostAccountType | ACCOUNT_TYPE | — | ✅ |
| 2 | PaymentCostAccountingDate | ACCOUNTING_DATE | — | ✅ |
| 3 | PaymentCostCostAllocationKeyflexId | COST_ALLOCATION_KEYFLEX_ID | — | — |
| 4 | PaymentCostCurrencyCode | CURRENCY_CODE | — | ✅ |
| 5 | PaymentCostDebitOrCredit | DEBIT_OR_CREDIT | — | ✅ |
| 6 | PaymentCostId | PAYMENT_COST_ID | 🔑 | ✅ |
| 7 | PaymentCostPrePaymentId | PRE_PAYMENT_ID | — | — |
| 8 | PaymentCostSourceActionId | SOURCE_ACTION_ID | — | — |
| 9 | PaymentCostSourceType | SOURCE_TYPE | — | ✅ |
| 10 | PaymentCostValue | VALUE | — | ✅ |

### [[pay_payroll_actions|PAY_PAYROLL_ACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayActActionParameterGroupId | ACTION_PARAMETER_GROUP_ID | — | — |
| 2 | PayActActionPopulationStatus | ACTION_POPULATION_STATUS | — | ✅ |
| 3 | PayActActionSequence | ACTION_SEQUENCE | — | ✅ |
| 4 | PayActActionStatus | ACTION_STATUS | — | ✅ |
| 5 | PayActActionType | ACTION_TYPE | — | ✅ |
| 6 | PayActAssignmentSetId | ASSIGNMENT_SET_ID | — | — |
| 7 | PayActBatchProcessMode | BATCH_PROCESS_MODE | — | ✅ |
| 8 | PayActChequeProcedure | CHEQUE_PROCEDURE | — | ✅ |
| 9 | PayActConsolidationSetId | CONSOLIDATION_SET_ID | — | — |
| 10 | PayActCreatedBy | CREATED_BY | — | — |
| 11 | PayActCreationDate | CREATION_DATE | — | — |
| 12 | PayActCurrentChunkNumber | CURRENT_CHUNK_NUMBER | — | ✅ |
| 13 | PayActCurrentTask | CURRENT_TASK | — | ✅ |
| 14 | PayActDateEarned | DATE_EARNED | — | ✅ |
| 15 | PayActDisplayRunNumber | DISPLAY_RUN_NUMBER | — | ✅ |
| 16 | PayActEffectiveDate | EFFECTIVE_DATE | — | ✅ |
| 17 | PayActElementSetId | ELEMENT_SET_ID | — | — |
| 18 | PayActEndChequeNumber | END_CHEQUE_NUMBER | — | ✅ |
| 19 | PayActEndDate | END_DATE | — | ✅ |
| 20 | PayActFutureProcessMode | FUTURE_PROCESS_MODE | — | ✅ |
| 21 | PayActLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | PayActLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 23 | PayActLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 24 | PayActLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 25 | PayActLegislativeParameters | LEGISLATIVE_PARAMETERS | — | ✅ |
| 26 | PayActObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 27 | PayActOrgPaymentMethodId | ORG_PAYMENT_METHOD_ID | — | — |
| 28 | PayActOverridingDdDate | OVERRIDING_DD_DATE | — | ✅ |
| 29 | PayActPayRequestId | PAY_REQUEST_ID | — | — |
| 30 | PayActPaymentTypeId | PAYMENT_TYPE_ID | — | — |
| 31 | PayActPayrollActionId | PAYROLL_ACTION_ID | — | ✅ |
| 32 | PayActPayrollId | PAYROLL_ID | — | — |
| 33 | PayActReportCategoryId | REPORT_CATEGORY_ID | — | — |
| 34 | PayActReportFormatMappingId | REPORT_FORMAT_MAPPING_ID | — | — |
| 35 | PayActRetroDefinitionId | RETRO_DEFINITION_ID | — | — |
| 36 | PayActRunTypeId | RUN_TYPE_ID | — | — |
| 37 | PayActStartChequeNumber | START_CHEQUE_NUMBER | — | ✅ |
| 38 | PayActStartDate | START_DATE | — | ✅ |
| 39 | PayActTargetPayrollActionId | TARGET_PAYROLL_ACTION_ID | — | — |

### [[pay_payroll_rel_actions|PAY_PAYROLL_REL_ACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayRelActActionSequence | ACTION_SEQUENCE | — | — |
| 2 | PayRelActActionStatus | ACTION_STATUS | — | — |
| 3 | PayRelActChunkNumber | CHUNK_NUMBER | — | ✅ |
| 4 | PayRelActEndDate | END_DATE | — | ✅ |
| 5 | PayRelActObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | PayRelActPayrollActionId | PAYROLL_ACTION_ID | — | — |
| 7 | PayRelActPayrollRelActionId | PAYROLL_REL_ACTION_ID | — | ✅ |
| 8 | PayRelActPayrollRelationshipId | PAYROLL_RELATIONSHIP_ID | — | — |
| 9 | PayRelActPrePaymentId | PRE_PAYMENT_ID | — | — |
| 10 | PayRelActRetroComponentId | RETRO_COMPONENT_ID | — | — |
| 11 | PayRelActRunTypeId | RUN_TYPE_ID | — | — |
| 12 | PayRelActSerialNumber | SERIAL_NUMBER | — | ✅ |
| 13 | PayRelActSourceActionId | SOURCE_ACTION_ID | — | — |
| 14 | PayRelActStartDate | START_DATE | — | ✅ |

### [[pay_pay_relationships_dn|PAY_PAY_RELATIONSHIPS_DN]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayRelDnCreatedBy | CREATED_BY | — | — |
| 2 | PayRelDnCreationDate | CREATION_DATE | — | — |
| 3 | PayRelDnEndDate | END_DATE | — | ✅ |
| 4 | PayRelDnLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PayRelDnLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | PayRelDnLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | PayRelDnLegislativeDataGroupId1 | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 8 | PayRelDnObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | PayRelDnPayrollRelationshipId | PAYROLL_RELATIONSHIP_ID | — | — |
| 10 | PayRelDnPayrollRelationshipNumber | PAYROLL_RELATIONSHIP_NUMBER | — | ✅ |
| 11 | PayRelDnPayrollStatUnitId | PAYROLL_STAT_UNIT_ID | — | — |
| 12 | PayRelDnPersonId | PERSON_ID | — | — |
| 13 | PayRelDnRelationshipTypeId | RELATIONSHIP_TYPE_ID | — | — |
| 14 | PayRelDnStartDate | START_DATE | — | ✅ |

### [[pay_pre_payments|PAY_PRE_PAYMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrePaymentBaseCurrencyValue | BASE_CURRENCY_VALUE | — | ✅ |
| 2 | PrePaymentCalcBreakdownId | CALC_BREAKDOWN_ID | — | — |
| 3 | PrePaymentEffectiveDate | EFFECTIVE_DATE | — | ✅ |
| 4 | PrePaymentOrgPaymentMethodId | ORG_PAYMENT_METHOD_ID | — | — |
| 5 | PrePaymentPayeeBankAccountId | PAYEE_BANK_ACCOUNT_ID | — | — |
| 6 | PrePaymentPayeeOrgPaymentMethodId | PAYEE_ORG_PAYMENT_METHOD_ID | — | — |
| 7 | PrePaymentPayerBankAccountId | PAYER_BANK_ACCOUNT_ID | — | — |
| 8 | PrePaymentPayrollActionId | PAYROLL_ACTION_ID | — | — |
| 9 | PrePaymentPayrollRelActionId | PAYROLL_REL_ACTION_ID | — | — |
| 10 | PrePaymentPersonalPaymentMethodId | PERSONAL_PAYMENT_METHOD_ID | — | — |
| 11 | PrePaymentPrePaymentId | PRE_PAYMENT_ID | — | — |
| 12 | PrePaymentSourceActionId | SOURCE_ACTION_ID | — | — |
| 13 | PrePaymentThirdPartyPayeeId | THIRD_PARTY_PAYEE_ID | — | — |
| 14 | PrePaymentValue | VALUE | — | — |

### [[pay_requests|PAY_REQUESTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayReqCallId | CALL_ID | — | — |
| 2 | PayReqCallType | CALL_TYPE | — | ✅ |
| 3 | PayReqCreatedBy | CREATED_BY | — | — |
| 4 | PayReqCreationDate | CREATION_DATE | — | — |
| 5 | PayReqFlowInstanceId | FLOW_INSTANCE_ID | — | — |
| 6 | PayReqFlowTaskInstanceId | FLOW_TASK_INSTANCE_ID | — | — |
| 7 | PayReqLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PayReqLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | PayReqLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | PayReqObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | PayReqParamNameVals | PARAM_NAME_VALS | — | — |
| 12 | PayReqPayRequestId | PAY_REQUEST_ID | — | — |
| 13 | PayReqPayTaskActionId | PAY_TASK_ACTION_ID | — | — |

### [[per_legislative_data_groups|PER_LEGISLATIVE_DATA_GROUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LdgPEOCostAllocationIdFlexNum | COST_ALLOCATION_ID_FLEX_NUM | — | — |
| 2 | LdgPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
