---
id: DOC-HCM-PVO-PayrollActionPVO
doc_type: system-doc
title: "PayrollActionPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PayrollActionPVO
  - payrollactionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PayrollActionPVO

## 📌 Visão Geral

Disponibiliza ações de processamento de folha de pagamento com tipo, sequência e status de população. Permite monitoramento e auditoria de etapas do ciclo de payroll.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBatchProcessCoreAM.PayrollActionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 50 | 1 | 1 | 50 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pay_payroll_actions|PAY_PAYROLL_ACTIONS]] — 50 atributos (1 PKs, 50 BICC)

---

## ⚙️ Atributos

### [[pay_payroll_actions|PAY_PAYROLL_ACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayrollActionPEOActionParameterGroupId | ACTION_PARAMETER_GROUP_ID | — | ✅ |
| 2 | PayrollActionPEOActionPopulationStatus | ACTION_POPULATION_STATUS | — | ✅ |
| 3 | PayrollActionPEOActionSequence | ACTION_SEQUENCE | — | ✅ |
| 4 | PayrollActionPEOActionStatus | ACTION_STATUS | — | ✅ |
| 5 | PayrollActionPEOActionType | ACTION_TYPE | — | ✅ |
| 6 | PayrollActionPEOAssignmentSetId | ASSIGNMENT_SET_ID | — | ✅ |
| 7 | PayrollActionPEOBatchProcessMode | BATCH_PROCESS_MODE | — | ✅ |
| 8 | PayrollActionPEOBipJobId | BIP_JOB_ID | — | ✅ |
| 9 | PayrollActionPEOChequeProcedure | CHEQUE_PROCEDURE | — | ✅ |
| 10 | PayrollActionPEOConsolidationSetId | CONSOLIDATION_SET_ID | — | ✅ |
| 11 | PayrollActionPEOCreatedBy | CREATED_BY | — | ✅ |
| 12 | PayrollActionPEOCreationDate | CREATION_DATE | — | ✅ |
| 13 | PayrollActionPEOCurrentChunkNumber | CURRENT_CHUNK_NUMBER | — | ✅ |
| 14 | PayrollActionPEOCurrentTask | CURRENT_TASK | — | ✅ |
| 15 | PayrollActionPEODateEarned | DATE_EARNED | — | ✅ |
| 16 | PayrollActionPEODednTimePeriodId | DEDN_TIME_PERIOD_ID | — | ✅ |
| 17 | PayrollActionPEODisplayRunNumber | DISPLAY_RUN_NUMBER | — | ✅ |
| 18 | PayrollActionPEOEarnTimePeriodId | EARN_TIME_PERIOD_ID | — | ✅ |
| 19 | PayrollActionPEOEffectiveDate | EFFECTIVE_DATE | — | ✅ |
| 20 | PayrollActionPEOEftExpiryDate | EFT_EXPIRY_DATE | — | ✅ |
| 21 | PayrollActionPEOEftFileReference | EFT_FILE_REFERENCE | — | ✅ |
| 22 | PayrollActionPEOElementSetId | ELEMENT_SET_ID | — | ✅ |
| 23 | PayrollActionPEOEndChequeNumber | END_CHEQUE_NUMBER | — | ✅ |
| 24 | PayrollActionPEOEndDate | END_DATE | — | ✅ |
| 25 | PayrollActionPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 26 | PayrollActionPEOFileName | FILE_NAME | — | ✅ |
| 27 | PayrollActionPEOFutureProcessMode | FUTURE_PROCESS_MODE | — | ✅ |
| 28 | PayrollActionPEOInterfaceTypeId | INTERFACE_TYPE_ID | — | ✅ |
| 29 | PayrollActionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | PayrollActionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 31 | PayrollActionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 32 | PayrollActionPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 33 | PayrollActionPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 34 | PayrollActionPEOLegislativeParameters | LEGISLATIVE_PARAMETERS | — | ✅ |
| 35 | PayrollActionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 36 | PayrollActionPEOOrgPaymentMethodId | ORG_PAYMENT_METHOD_ID | — | ✅ |
| 37 | PayrollActionPEOOverridingDdDate | OVERRIDING_DD_DATE | — | ✅ |
| 38 | PayrollActionPEOParentOrgPayMethodId | PARENT_ORG_PAY_METHOD_ID | — | ✅ |
| 39 | PayrollActionPEOPayRequestId | PAY_REQUEST_ID | — | ✅ |
| 40 | PayrollActionPEOPaymentReason | PAYMENT_REASON | — | ✅ |
| 41 | PayrollActionPEOPaymentTypeId | PAYMENT_TYPE_ID | — | ✅ |
| 42 | PayrollActionPEOPayrollActionId | PAYROLL_ACTION_ID | 🔑 | ✅ |
| 43 | PayrollActionPEOPayrollId | PAYROLL_ID | — | ✅ |
| 44 | PayrollActionPEOReportCategoryId | REPORT_CATEGORY_ID | — | ✅ |
| 45 | PayrollActionPEOReportFormatMappingId | REPORT_FORMAT_MAPPING_ID | — | ✅ |
| 46 | PayrollActionPEORetroDefinitionId | RETRO_DEFINITION_ID | — | ✅ |
| 47 | PayrollActionPEORunTypeId | RUN_TYPE_ID | — | ✅ |
| 48 | PayrollActionPEOStartChequeNumber | START_CHEQUE_NUMBER | — | ✅ |
| 49 | PayrollActionPEOStartDate | START_DATE | — | ✅ |
| 50 | PayrollActionPEOTargetPayrollActionId | TARGET_PAYROLL_ACTION_ID | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
