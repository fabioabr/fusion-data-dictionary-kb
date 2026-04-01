---
id: DOC-OTHER-PVO-PaymentActionPVO
doc_type: system-doc
title: "PaymentActionPVO — PVO Cross-Module"
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
  - PaymentActionPVO
  - paymentactionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PaymentActionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Payment Action. Acessa as tabelas: PAY_PAYROLL_ACTIONS, PAY_PAYROLL_REL_ACTIONS, PAY_PAY_RELATIONSHIPS_DN (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBatchProcessCoreAM.PaymentActionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 58 | 4 | 4 | 10 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[pay_payroll_actions|PAY_PAYROLL_ACTIONS]] — 30 atributos (1 PKs, 5 BICC)
- [[pay_payroll_rel_actions|PAY_PAYROLL_REL_ACTIONS]] — 12 atributos (2 PKs, 3 BICC)
- [[pay_pay_relationships_dn|PAY_PAY_RELATIONSHIPS_DN]] — 9 atributos (1 PKs, 2 BICC)
- [[pay_requests|PAY_REQUESTS]] — 7 atributos

---

## ⚙️ Atributos

### [[pay_payroll_actions|PAY_PAYROLL_ACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayrollActionPEOActionPopulationStatus | ACTION_POPULATION_STATUS | — | — |
| 2 | PayrollActionPEOActionSequence | ACTION_SEQUENCE | — | — |
| 3 | PayrollActionPEOActionStatus | ACTION_STATUS | — | — |
| 4 | PayrollActionPEOActionType | ACTION_TYPE | — | ✅ |
| 5 | PayrollActionPEOBatchProcessMode | BATCH_PROCESS_MODE | — | — |
| 6 | PayrollActionPEOChequeProcedure | CHEQUE_PROCEDURE | — | — |
| 7 | PayrollActionPEOConsolidationSetId | CONSOLIDATION_SET_ID | — | — |
| 8 | PayrollActionPEOCurrentChunkNumber | CURRENT_CHUNK_NUMBER | — | — |
| 9 | PayrollActionPEOCurrentTask | CURRENT_TASK | — | — |
| 10 | PayrollActionPEODateEarned | DATE_EARNED | — | ✅ |
| 11 | PayrollActionPEODednTimePeriodId | DEDN_TIME_PERIOD_ID | — | — |
| 12 | PayrollActionPEODisplayRunNumber | DISPLAY_RUN_NUMBER | — | — |
| 13 | PayrollActionPEOEarnTimePeriodId | EARN_TIME_PERIOD_ID | — | — |
| 14 | PayrollActionPEOEffectiveDate | EFFECTIVE_DATE | — | ✅ |
| 15 | PayrollActionPEOElementSetId | ELEMENT_SET_ID | — | — |
| 16 | PayrollActionPEOEndChequeNumber | END_CHEQUE_NUMBER | — | — |
| 17 | PayrollActionPEOEndDate | END_DATE | — | — |
| 18 | PayrollActionPEOFutureProcessMode | FUTURE_PROCESS_MODE | — | — |
| 19 | PayrollActionPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 20 | PayrollActionPEOLegislativeParameters | LEGISLATIVE_PARAMETERS | — | ✅ |
| 21 | PayrollActionPEOOrgPaymentMethodId | ORG_PAYMENT_METHOD_ID | — | — |
| 22 | PayrollActionPEOOverridingDdDate | OVERRIDING_DD_DATE | — | — |
| 23 | PayrollActionPEOPayRequestId | PAY_REQUEST_ID | — | — |
| 24 | PayrollActionPEOPaymentTypeId | PAYMENT_TYPE_ID | — | — |
| 25 | PayrollActionPEOPayrollActionId | PAYROLL_ACTION_ID | 🔑 | ✅ |
| 26 | PayrollActionPEOPayrollId | PAYROLL_ID | — | — |
| 27 | PayrollActionPEORunTypeId | RUN_TYPE_ID | — | — |
| 28 | PayrollActionPEOStartChequeNumber | START_CHEQUE_NUMBER | — | — |
| 29 | PayrollActionPEOStartDate | START_DATE | — | — |
| 30 | PayrollActionPEOTargetPayrollActionId | TARGET_PAYROLL_ACTION_ID | — | — |

### [[pay_payroll_rel_actions|PAY_PAYROLL_REL_ACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayrollRelationshipActionPEOActionSequence | ACTION_SEQUENCE | — | — |
| 2 | PayrollRelationshipActionPEOActionStatus | ACTION_STATUS | — | — |
| 3 | PayrollRelationshipActionPEOChunkNumber | CHUNK_NUMBER | — | — |
| 4 | PayrollRelationshipActionPEOEndDate | END_DATE | — | — |
| 5 | PayrollRelationshipActionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | PayrollRelationshipActionPEOPayrollRelActionId | PAYROLL_REL_ACTION_ID | 🔑 | ✅ |
| 7 | PayrollRelationshipActionPEOPayrollRelationshipId | PAYROLL_RELATIONSHIP_ID | — | — |
| 8 | PayrollRelationshipActionPEOPrePaymentId | PRE_PAYMENT_ID | — | — |
| 9 | PayrollRelationshipActionPEORunTypeId | RUN_TYPE_ID | — | — |
| 10 | PayrollRelationshipActionPEOSerialNumber | SERIAL_NUMBER | — | ✅ |
| 11 | PayrollRelationshipActionPEOSourceActionId | SOURCE_ACTION_ID | — | — |
| 12 | PayrollRelationshipActionPEOStartDate | START_DATE | 🔑 | ✅ |

### [[pay_pay_relationships_dn|PAY_PAY_RELATIONSHIPS_DN]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | PayrollRelationshipId | PAYROLL_RELATIONSHIP_ID | 🔑 | ✅ |
| 3 | PayrollRelationshipPEOEndDate | END_DATE | — | — |
| 4 | PayrollRelationshipPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 5 | PayrollRelationshipPEOPayrollRelationshipNumber | PAYROLL_RELATIONSHIP_NUMBER | — | ✅ |
| 6 | PayrollRelationshipPEOPayrollStatUnitId | PAYROLL_STAT_UNIT_ID | — | — |
| 7 | PayrollRelationshipPEOPersonId | PERSON_ID | — | — |
| 8 | PayrollRelationshipPEORelationshipTypeId | RELATIONSHIP_TYPE_ID | — | — |
| 9 | PayrollRelationshipPEOStartDate | START_DATE | — | — |

### [[pay_requests|PAY_REQUESTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayRequestPEOCallId | CALL_ID | — | — |
| 2 | PayRequestPEOCallType | CALL_TYPE | — | — |
| 3 | PayRequestPEOFlowInstanceId | FLOW_INSTANCE_ID | — | — |
| 4 | PayRequestPEOFlowTaskInstanceId | FLOW_TASK_INSTANCE_ID | — | — |
| 5 | PayRequestPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 6 | PayRequestPEOPayRequestId | PAY_REQUEST_ID | — | — |
| 7 | PayRequestPEOPayTaskActionId | PAY_TASK_ACTION_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
