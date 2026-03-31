---
id: DOC-OTHER-PVO-RetroElementEntry
doc_type: system-doc
title: "RetroElementEntry — PVO Cross-Module"
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
  - RetroElementEntry
  - retroelemententry
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RetroElementEntry

## 📌 Visão Geral

View Object para extração BICC de dados de Retro Element Entry. Acessa as tabelas: PAY_ASSIGNED_PAYROLLS_F, PAY_ELEMENT_CRITERIA, PAY_ELEMENT_ENTRIES_F (+7).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBatchProcessCoreAM.RetroElementEntry`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 124 | 10 | 3 | 34 | 27% |

---

## 🔗 Tabelas Relacionadas

- [[pay_assigned_payrolls_f|PAY_ASSIGNED_PAYROLLS_F]] — 7 atributos (1 BICC)
- [[pay_element_criteria|PAY_ELEMENT_CRITERIA]] — 16 atributos
- [[pay_element_entries_f|PAY_ELEMENT_ENTRIES_F]] — 16 atributos (6 BICC)
- [[pay_element_entry_values_f|PAY_ELEMENT_ENTRY_VALUES_F]] — 13 atributos (3 PKs, 5 BICC)
- [[pay_entry_usages|PAY_ENTRY_USAGES]] — 9 atributos (2 BICC)
- [[pay_flow_task_instances|PAY_FLOW_TASK_INSTANCES]] — 5 atributos
- [[pay_payroll_actions|PAY_PAYROLL_ACTIONS]] — 33 atributos (18 BICC)
- [[pay_payroll_rel_actions|PAY_PAYROLL_REL_ACTIONS]] — 14 atributos (2 BICC)
- [[pay_pay_relationships_dn|PAY_PAY_RELATIONSHIPS_DN]] — 3 atributos
- [[pay_requests|PAY_REQUESTS]] — 8 atributos

---

## ⚙️ Atributos

### [[pay_assigned_payrolls_f|PAY_ASSIGNED_PAYROLLS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignedPayrollAsgInformationType | ASG_INFORMATION_TYPE | — | — |
| 2 | AssignedPayrollAssignedPayrollId | ASSIGNED_PAYROLL_ID | — | — |
| 3 | AssignedPayrollEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | AssignedPayrollEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | AssignedPayrollElementCriteriaId | ELEMENT_CRITERIA_ID | — | — |
| 6 | AssignedPayrollPrimaryFlag | PRIMARY_FLAG | — | — |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[pay_element_criteria|PAY_ELEMENT_CRITERIA]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ElementCriteriaCollectiveAgreementId | COLLECTIVE_AGREEMENT_ID | — | — |
| 2 | ElementCriteriaCriteriaType | CRITERIA_TYPE | — | — |
| 3 | ElementCriteriaElementCriteriaId | ELEMENT_CRITERIA_ID | — | — |
| 4 | ElementCriteriaEmploymentCategory | EMPLOYMENT_CATEGORY | — | — |
| 5 | ElementCriteriaGradeId | GRADE_ID | — | — |
| 6 | ElementCriteriaJobId | JOB_ID | — | — |
| 7 | ElementCriteriaLegalEmployerId | LEGAL_EMPLOYER_ID | — | — |
| 8 | ElementCriteriaLinkLevel | LINK_LEVEL | — | — |
| 9 | ElementCriteriaLinkToAllPayrollsFlag | LINK_TO_ALL_PAYROLLS_FLAG | — | — |
| 10 | ElementCriteriaLocationId | LOCATION_ID | — | — |
| 11 | ElementCriteriaOrganizationId | ORGANIZATION_ID | — | — |
| 12 | ElementCriteriaPayrollId | PAYROLL_ID | — | — |
| 13 | ElementCriteriaPayrollStatUnitId | PAYROLL_STAT_UNIT_ID | — | — |
| 14 | ElementCriteriaPeopleGroupId | PEOPLE_GROUP_ID | — | — |
| 15 | ElementCriteriaPositionId | POSITION_ID | — | — |
| 16 | ElementCriteriaRelationshipTypeId | RELATIONSHIP_TYPE_ID | — | — |

### [[pay_element_entries_f|PAY_ELEMENT_ENTRIES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ElementEntryAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | ElementEntryBalanceAdjCostFlag | BALANCE_ADJ_COST_FLAG | — | ✅ |
| 3 | ElementEntryBatchId | BATCH_ID | — | — |
| 4 | ElementEntryCreatorId | CREATOR_ID | — | — |
| 5 | ElementEntryCreatorType | CREATOR_TYPE | — | ✅ |
| 6 | ElementEntryDateEarned | DATE_EARNED | — | ✅ |
| 7 | ElementEntryEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | ElementEntryEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 9 | ElementEntryElementEntryId | ELEMENT_ENTRY_ID | — | — |
| 10 | ElementEntryElementTypeId | ELEMENT_TYPE_ID | — | — |
| 11 | ElementEntryEntryInformationCategory | ENTRY_INFORMATION_CATEGORY | — | — |
| 12 | ElementEntryEntryType | ENTRY_TYPE | — | ✅ |
| 13 | ElementEntryPersonId | PERSON_ID | — | — |
| 14 | ElementEntryReason | REASON | — | ✅ |
| 15 | ElementEntrySubpriority | SUBPRIORITY | — | — |
| 16 | ElementEntryTargetEntryId | TARGET_ENTRY_ID | — | — |

### [[pay_element_entry_values_f|PAY_ELEMENT_ENTRY_VALUES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | ElementEntryValueCreatedBy | CREATED_BY | — | — |
| 4 | ElementEntryValueCreationDate | CREATION_DATE | — | — |
| 5 | ElementEntryValueElementEntryId | ELEMENT_ENTRY_ID | — | — |
| 6 | ElementEntryValueEntryUsageId | ENTRY_USAGE_ID | — | — |
| 7 | ElementEntryValueId | ELEMENT_ENTRY_VALUE_ID | 🔑 | ✅ |
| 8 | ElementEntryValueInputValueId | INPUT_VALUE_ID | — | — |
| 9 | ElementEntryValueLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | ElementEntryValueLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | ElementEntryValueLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | ElementEntryValueObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | ElementEntryValueScreenEntryValue | SCREEN_ENTRY_VALUE | — | ✅ |

### [[pay_entry_usages|PAY_ENTRY_USAGES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EntryUsagePEOAssignedPayrollId | ASSIGNED_PAYROLL_ID | — | — |
| 2 | EntryUsagePEODateFrom | DATE_FROM | — | — |
| 3 | EntryUsagePEODateTo | DATE_TO | — | — |
| 4 | EntryUsagePEOElementEntryId | ELEMENT_ENTRY_ID | — | — |
| 5 | EntryUsagePEOEntryUsageId | ENTRY_USAGE_ID | — | — |
| 6 | EntryUsagePEOPayrollAssignmentId | PAYROLL_ASSIGNMENT_ID | — | ✅ |
| 7 | EntryUsagePEOPayrollRelationshipId | PAYROLL_RELATIONSHIP_ID | — | — |
| 8 | EntryUsagePEOPayrollTermId | PAYROLL_TERM_ID | — | ✅ |
| 9 | EntryUsagePEOUsageLevel | USAGE_LEVEL | — | — |

### [[pay_flow_task_instances|PAY_FLOW_TASK_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FlowTaskInstanceBaseFlowTaskId | BASE_FLOW_TASK_ID | — | — |
| 2 | FlowTaskInstanceEssServiceExecId | ESS_SERVICE_EXEC_ID | — | — |
| 3 | FlowTaskInstanceFlowInstanceId | FLOW_INSTANCE_ID | — | — |
| 4 | FlowTaskInstanceFlowTaskInstanceId | FLOW_TASK_INSTANCE_ID | — | — |
| 5 | FlowTaskInstanceStatus | STATUS | — | — |

### [[pay_payroll_actions|PAY_PAYROLL_ACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayrollActionActionParameterGroupId | ACTION_PARAMETER_GROUP_ID | — | — |
| 2 | PayrollActionActionPopulationStatus | ACTION_POPULATION_STATUS | — | ✅ |
| 3 | PayrollActionActionSequence | ACTION_SEQUENCE | — | ✅ |
| 4 | PayrollActionActionStatus | ACTION_STATUS | — | ✅ |
| 5 | PayrollActionActionType | ACTION_TYPE | — | ✅ |
| 6 | PayrollActionAssignmentSetId | ASSIGNMENT_SET_ID | — | — |
| 7 | PayrollActionBatchProcessMode | BATCH_PROCESS_MODE | — | ✅ |
| 8 | PayrollActionChequeProcedure | CHEQUE_PROCEDURE | — | ✅ |
| 9 | PayrollActionConsolidationSetId | CONSOLIDATION_SET_ID | — | — |
| 10 | PayrollActionCurrentChunkNumber | CURRENT_CHUNK_NUMBER | — | ✅ |
| 11 | PayrollActionCurrentTask | CURRENT_TASK | — | ✅ |
| 12 | PayrollActionDateEarned | DATE_EARNED | — | ✅ |
| 13 | PayrollActionDisplayRunNumber | DISPLAY_RUN_NUMBER | — | ✅ |
| 14 | PayrollActionEffectiveDate | EFFECTIVE_DATE | — | ✅ |
| 15 | PayrollActionElementSetId | ELEMENT_SET_ID | — | — |
| 16 | PayrollActionEndChequeNumber | END_CHEQUE_NUMBER | — | ✅ |
| 17 | PayrollActionEndDate | END_DATE | — | ✅ |
| 18 | PayrollActionFutureProcessMode | FUTURE_PROCESS_MODE | — | ✅ |
| 19 | PayrollActionLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 20 | PayrollActionLegislativeParameters | LEGISLATIVE_PARAMETERS | — | ✅ |
| 21 | PayrollActionOrgPaymentMethodId | ORG_PAYMENT_METHOD_ID | — | — |
| 22 | PayrollActionOverridingDdDate | OVERRIDING_DD_DATE | — | ✅ |
| 23 | PayrollActionPayRequestId | PAY_REQUEST_ID | — | — |
| 24 | PayrollActionPaymentTypeId | PAYMENT_TYPE_ID | — | — |
| 25 | PayrollActionPayrollActionId | PAYROLL_ACTION_ID | — | — |
| 26 | PayrollActionPayrollId | PAYROLL_ID | — | — |
| 27 | PayrollActionReportCategoryId | REPORT_CATEGORY_ID | — | — |
| 28 | PayrollActionReportFormatMappingId | REPORT_FORMAT_MAPPING_ID | — | — |
| 29 | PayrollActionRetroDefinitionId | RETRO_DEFINITION_ID | — | — |
| 30 | PayrollActionRunTypeId | RUN_TYPE_ID | — | — |
| 31 | PayrollActionStartChequeNumber | START_CHEQUE_NUMBER | — | ✅ |
| 32 | PayrollActionStartDate | START_DATE | — | ✅ |
| 33 | PayrollActionTargetPayrollActionId | TARGET_PAYROLL_ACTION_ID | — | — |

### [[pay_payroll_rel_actions|PAY_PAYROLL_REL_ACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayrollRelationshipActionSequence | ACTION_SEQUENCE | — | ✅ |
| 2 | PayrollRelationshipActionStatus | ACTION_STATUS | — | ✅ |
| 3 | PayrollRelationshipChunkNumber | CHUNK_NUMBER | — | — |
| 4 | PayrollRelationshipEndDate | END_DATE | — | — |
| 5 | PayrollRelationshipObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | PayrollRelationshipPayrollActionId | PAYROLL_ACTION_ID | — | — |
| 7 | PayrollRelationshipPayrollRelActionId | PAYROLL_REL_ACTION_ID | — | — |
| 8 | PayrollRelationshipPayrollRelationshipId | PAYROLL_RELATIONSHIP_ID | — | — |
| 9 | PayrollRelationshipPrePaymentId | PRE_PAYMENT_ID | — | — |
| 10 | PayrollRelationshipRetroComponentId | RETRO_COMPONENT_ID | — | — |
| 11 | PayrollRelationshipRunTypeId | RUN_TYPE_ID | — | — |
| 12 | PayrollRelationshipSerialNumber | SERIAL_NUMBER | — | — |
| 13 | PayrollRelationshipSourceActionId | SOURCE_ACTION_ID | — | — |
| 14 | PayrollRelationshipStartDate | START_DATE | — | — |

### [[pay_pay_relationships_dn|PAY_PAY_RELATIONSHIPS_DN]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayrollRelationshipPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 2 | PayrollRelationshipPEOPayrollRelationshipId | PAYROLL_RELATIONSHIP_ID | — | — |
| 3 | PayrollRelationshipPEOPersonId | PERSON_ID | — | — |

### [[pay_requests|PAY_REQUESTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 2 | RequestCallId | CALL_ID | — | — |
| 3 | RequestCallType | CALL_TYPE | — | — |
| 4 | RequestFlowInstanceId | FLOW_INSTANCE_ID | — | — |
| 5 | RequestFlowTaskInstanceId | FLOW_TASK_INSTANCE_ID | — | — |
| 6 | RequestParamNameVals | PARAM_NAME_VALS | — | — |
| 7 | RequestPayRequestId | PAY_REQUEST_ID | — | — |
| 8 | RequestPayTaskActionId | PAY_TASK_ACTION_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
