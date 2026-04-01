---
id: DOC-AP-PVO-PrePayments
doc_type: system-doc
title: "PrePayments — PVO Accounts Payable"
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
  - PrePayments
  - prepayments
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PrePayments

## 📌 Visão Geral

Extrai os registros de pré-pagamentos da folha de pagamento, incluindo ações de payroll, relacionamento trabalhista e requisições vinculadas. Permite controlar os processamentos de pagamento antecipado na folha e garantir a correta liquidação dos valores.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PaymentResultsAM.PrePayments`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 95 | 5 | 1 | 38 | 40% |

---

## 🔗 Tabelas Relacionadas

- [[pay_payroll_actions|PAY_PAYROLL_ACTIONS]] — 40 atributos (20 BICC)
- [[pay_payroll_rel_actions|PAY_PAYROLL_REL_ACTIONS]] — 14 atributos (7 BICC)
- [[pay_pay_relationships_dn|PAY_PAY_RELATIONSHIPS_DN]] — 14 atributos (4 BICC)
- [[pay_pre_payments|PAY_PRE_PAYMENTS]] — 14 atributos (1 PKs, 4 BICC)
- [[pay_requests|PAY_REQUESTS]] — 13 atributos (3 BICC)

---

## ⚙️ Atributos

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
| 40 | RunActPayrollActionId | PAYROLL_ACTION_ID | — | — |

### [[pay_payroll_rel_actions|PAY_PAYROLL_REL_ACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayRelActActionSequence | ACTION_SEQUENCE | — | ✅ |
| 2 | PayRelActActionStatus | ACTION_STATUS | — | ✅ |
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
| 1 | PayRelDNCreatedBy | CREATED_BY | — | — |
| 2 | PayRelDNCreationDate | CREATION_DATE | — | — |
| 3 | PayRelDNEndDate | END_DATE | — | ✅ |
| 4 | PayRelDNLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PayRelDNLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | PayRelDNLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | PayRelDNLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 8 | PayRelDNObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | PayRelDNPayrollRelationshipId | PAYROLL_RELATIONSHIP_ID | — | — |
| 10 | PayRelDNPayrollRelationshipNumber | PAYROLL_RELATIONSHIP_NUMBER | — | ✅ |
| 11 | PayRelDNPayrollStatUnitId | PAYROLL_STAT_UNIT_ID | — | — |
| 12 | PayRelDNPersonId | PERSON_ID | — | — |
| 13 | PayRelDNRelationshipTypeId | RELATIONSHIP_TYPE_ID | — | — |
| 14 | PayRelDNStartDate | START_DATE | — | ✅ |

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
| 11 | PrePaymentPrePaymentId | PRE_PAYMENT_ID | 🔑 | ✅ |
| 12 | PrePaymentSourceActionId | SOURCE_ACTION_ID | — | — |
| 13 | PrePaymentThirdPartyPayeeId | THIRD_PARTY_PAYEE_ID | — | — |
| 14 | PrePaymentValue | VALUE | — | ✅ |

### [[pay_requests|PAY_REQUESTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayReqCallId | CALL_ID | — | ✅ |
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

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
