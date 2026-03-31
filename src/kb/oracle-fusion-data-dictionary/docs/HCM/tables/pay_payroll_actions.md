---
id: DOC-HCM-588
doc_type: system-doc
title: "PAY_PAYROLL_ACTIONS — Acoes de Folha de Pagamento"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: "Técnico"
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - payroll
  - payroll-actions
  - acoes-folha
  - pay-actions
aliases:
  - PAY_PAYROLL_ACTIONS
  - pay_payroll_actions
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_PAYROLL_ACTIONS

## 📌 Visão Geral

Armazena as **acoes de folha** (payroll actions) que representam cada execucao de processamento. Cada acao corresponde a um ciclo de calculo, retroativo, QuickPay, ou processamento especial.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Registro de cada execucao de processamento de folha
- Controle de status e parametros de processamento
- Auditoria de ciclos de calculo de folha
- Base para rastreamento de resultados de calculo

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PAYROLL_ACTION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da acao | --- | 🟢 95% |
| 2 | PAYROLL_ID | NUMBER(18) | NOT NULL | FK | ID da folha de pagamento | PAY_ALL_PAYROLLS_F | 🟢 95% |
| 3 | ACTION_TYPE | VARCHAR2(30) | NOT NULL | Classificacao | Tipo de acao (R=Regular, Q=QuickPay, B=Balance Adj) | --- | 🟢 90% |
| 4 | ACTION_STATUS | VARCHAR2(1) | NOT NULL | Classificacao | Status (C=Complete, E=Error, U=Unprocessed) | --- | 🟢 90% |
| 5 | TIME_PERIOD_ID | NUMBER(18) | NULL | FK | ID do periodo de tempo | PAY_TIME_PERIODS | 🟢 85% |
| 6 | EFFECTIVE_DATE | DATE | NULL | Vigencia | Data efetiva da acao | --- | 🟢 90% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_all_payrolls_f]] --- via `PAYROLL_ID` (folha de pagamento da ação processada)
- [[pay_time_periods]] --- via `TIME_PERIOD_ID` (período de tempo da ação de folha)

### Tabelas-filha (FK de saída)
- [[pay_payroll_rel_actions]] --- via `PAYROLL_ACTION_ID` (ações por relacionamento da ação de folha)
- [[pay_run_results]] --- via `PAYROLL_ACTION_ID` (resultados de cálculo da ação de folha)

---

## 📎 Uso Típico

### Acoes completadas de uma folha
```sql
SELECT pa.PAYROLL_ACTION_ID, pa.ACTION_TYPE, pa.ACTION_STATUS, pa.EFFECTIVE_DATE
FROM   PAY_PAYROLL_ACTIONS pa
WHERE  pa.PAYROLL_ID = :p_payroll_id
  AND  pa.ACTION_STATUS = 'C'
ORDER BY pa.EFFECTIVE_DATE DESC;
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[paymentactionpvo|PaymentActionPVO]] (HCM · BICC: 5/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_POPULATION_STATUS | PayrollActionPEOActionPopulationStatus | — |
| ACTION_SEQUENCE | PayrollActionPEOActionSequence | — |
| ACTION_STATUS | PayrollActionPEOActionStatus | — |
| ACTION_TYPE | PayrollActionPEOActionType | ✅ |
| BATCH_PROCESS_MODE | PayrollActionPEOBatchProcessMode | — |
| CHEQUE_PROCEDURE | PayrollActionPEOChequeProcedure | — |
| CONSOLIDATION_SET_ID | PayrollActionPEOConsolidationSetId | — |
| CURRENT_CHUNK_NUMBER | PayrollActionPEOCurrentChunkNumber | — |
| CURRENT_TASK | PayrollActionPEOCurrentTask | — |
| DATE_EARNED | PayrollActionPEODateEarned | ✅ |
| DEDN_TIME_PERIOD_ID | PayrollActionPEODednTimePeriodId | — |
| DISPLAY_RUN_NUMBER | PayrollActionPEODisplayRunNumber | — |
| EARN_TIME_PERIOD_ID | PayrollActionPEOEarnTimePeriodId | — |
| EFFECTIVE_DATE | PayrollActionPEOEffectiveDate | ✅ |
| ELEMENT_SET_ID | PayrollActionPEOElementSetId | — |
| END_CHEQUE_NUMBER | PayrollActionPEOEndChequeNumber | — |
| END_DATE | PayrollActionPEOEndDate | — |
| FUTURE_PROCESS_MODE | PayrollActionPEOFutureProcessMode | — |
| LEGISLATIVE_DATA_GROUP_ID | PayrollActionPEOLegislativeDataGroupId | — |
| LEGISLATIVE_PARAMETERS | PayrollActionPEOLegislativeParameters | ✅ |
| ORG_PAYMENT_METHOD_ID | PayrollActionPEOOrgPaymentMethodId | — |
| OVERRIDING_DD_DATE | PayrollActionPEOOverridingDdDate | — |
| PAY_REQUEST_ID | PayrollActionPEOPayRequestId | — |
| PAYMENT_TYPE_ID | PayrollActionPEOPaymentTypeId | — |
| PAYROLL_ACTION_ID | PayrollActionPEOPayrollActionId | ✅ |
| PAYROLL_ID | PayrollActionPEOPayrollId | — |
| RUN_TYPE_ID | PayrollActionPEORunTypeId | — |
| START_CHEQUE_NUMBER | PayrollActionPEOStartChequeNumber | — |
| START_DATE | PayrollActionPEOStartDate | — |
| TARGET_PAYROLL_ACTION_ID | PayrollActionPEOTargetPayrollActionId | — |

### [[payrollactionpvo|PayrollActionPVO]] (HCM · BICC: 50/50)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_PARAMETER_GROUP_ID | PayrollActionPEOActionParameterGroupId | ✅ |
| ACTION_POPULATION_STATUS | PayrollActionPEOActionPopulationStatus | ✅ |
| ACTION_SEQUENCE | PayrollActionPEOActionSequence | ✅ |
| ACTION_STATUS | PayrollActionPEOActionStatus | ✅ |
| ACTION_TYPE | PayrollActionPEOActionType | ✅ |
| ASSIGNMENT_SET_ID | PayrollActionPEOAssignmentSetId | ✅ |
| BATCH_PROCESS_MODE | PayrollActionPEOBatchProcessMode | ✅ |
| BIP_JOB_ID | PayrollActionPEOBipJobId | ✅ |
| CHEQUE_PROCEDURE | PayrollActionPEOChequeProcedure | ✅ |
| CONSOLIDATION_SET_ID | PayrollActionPEOConsolidationSetId | ✅ |
| CREATED_BY | PayrollActionPEOCreatedBy | ✅ |
| CREATION_DATE | PayrollActionPEOCreationDate | ✅ |
| CURRENT_CHUNK_NUMBER | PayrollActionPEOCurrentChunkNumber | ✅ |
| CURRENT_TASK | PayrollActionPEOCurrentTask | ✅ |
| DATE_EARNED | PayrollActionPEODateEarned | ✅ |
| DEDN_TIME_PERIOD_ID | PayrollActionPEODednTimePeriodId | ✅ |
| DISPLAY_RUN_NUMBER | PayrollActionPEODisplayRunNumber | ✅ |
| EARN_TIME_PERIOD_ID | PayrollActionPEOEarnTimePeriodId | ✅ |
| EFFECTIVE_DATE | PayrollActionPEOEffectiveDate | ✅ |
| EFT_EXPIRY_DATE | PayrollActionPEOEftExpiryDate | ✅ |
| EFT_FILE_REFERENCE | PayrollActionPEOEftFileReference | ✅ |
| ELEMENT_SET_ID | PayrollActionPEOElementSetId | ✅ |
| END_CHEQUE_NUMBER | PayrollActionPEOEndChequeNumber | ✅ |
| END_DATE | PayrollActionPEOEndDate | ✅ |
| ENTERPRISE_ID | PayrollActionPEOEnterpriseId | ✅ |
| FILE_NAME | PayrollActionPEOFileName | ✅ |
| FUTURE_PROCESS_MODE | PayrollActionPEOFutureProcessMode | ✅ |
| INTERFACE_TYPE_ID | PayrollActionPEOInterfaceTypeId | ✅ |
| LAST_UPDATE_DATE | PayrollActionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PayrollActionPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PayrollActionPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | PayrollActionPEOLegislationCode | ✅ |
| LEGISLATIVE_DATA_GROUP_ID | PayrollActionPEOLegislativeDataGroupId | ✅ |
| LEGISLATIVE_PARAMETERS | PayrollActionPEOLegislativeParameters | ✅ |
| OBJECT_VERSION_NUMBER | PayrollActionPEOObjectVersionNumber | ✅ |
| ORG_PAYMENT_METHOD_ID | PayrollActionPEOOrgPaymentMethodId | ✅ |
| OVERRIDING_DD_DATE | PayrollActionPEOOverridingDdDate | ✅ |
| PARENT_ORG_PAY_METHOD_ID | PayrollActionPEOParentOrgPayMethodId | ✅ |
| PAY_REQUEST_ID | PayrollActionPEOPayRequestId | ✅ |
| PAYMENT_REASON | PayrollActionPEOPaymentReason | ✅ |
| PAYMENT_TYPE_ID | PayrollActionPEOPaymentTypeId | ✅ |
| PAYROLL_ACTION_ID | PayrollActionPEOPayrollActionId | ✅ |
| PAYROLL_ID | PayrollActionPEOPayrollId | ✅ |
| REPORT_CATEGORY_ID | PayrollActionPEOReportCategoryId | ✅ |
| REPORT_FORMAT_MAPPING_ID | PayrollActionPEOReportFormatMappingId | ✅ |
| RETRO_DEFINITION_ID | PayrollActionPEORetroDefinitionId | ✅ |
| RUN_TYPE_ID | PayrollActionPEORunTypeId | ✅ |
| START_CHEQUE_NUMBER | PayrollActionPEOStartChequeNumber | ✅ |
| START_DATE | PayrollActionPEOStartDate | ✅ |
| TARGET_PAYROLL_ACTION_ID | PayrollActionPEOTargetPayrollActionId | ✅ |

### [[payrollruncosting|PayrollRunCosting]] (GL · BICC: 18/41)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_PARAMETER_GROUP_ID | PayActActionParameterGroupId | — |
| ACTION_POPULATION_STATUS | PayActActionPopulationStatus | ✅ |
| ACTION_SEQUENCE | PayActActionSequence | ✅ |
| ACTION_STATUS | PayActActionStatus | ✅ |
| ACTION_TYPE | PayActActionType | ✅ |
| ASSIGNMENT_SET_ID | PayActAssignmentSetId | — |
| BATCH_PROCESS_MODE | PayActBatchProcessMode | ✅ |
| CHEQUE_PROCEDURE | PayActChequeProcedure | ✅ |
| CONSOLIDATION_SET_ID | PayActConsolidationSetId | — |
| CREATED_BY | PayActCreatedBy | — |
| CREATION_DATE | PayActCreationDate | — |
| CURRENT_CHUNK_NUMBER | PayActCurrentChunkNumber | ✅ |
| CURRENT_TASK | PayActCurrentTask | ✅ |
| DATE_EARNED | PayActDateEarned | ✅ |
| DEDN_TIME_PERIOD_ID | PayrollActionPEODednTimePeriodId | — |
| DISPLAY_RUN_NUMBER | PayActDisplayRunNumber | ✅ |
| EARN_TIME_PERIOD_ID | PayrollActionPEOEarnTimePeriodId | — |
| EFFECTIVE_DATE | PayActEffectiveDate | ✅ |
| ELEMENT_SET_ID | PayActElementSetId | — |
| END_CHEQUE_NUMBER | PayActEndChequeNumber | ✅ |
| END_DATE | PayActEndDate | — |
| FUTURE_PROCESS_MODE | PayActFutureProcessMode | ✅ |
| LAST_UPDATE_DATE | PayActLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PayActLastUpdateLogin | — |
| LAST_UPDATED_BY | PayActLastUpdatedBy | — |
| LEGISLATIVE_DATA_GROUP_ID | PayActLegislativeDataGroupId | — |
| LEGISLATIVE_PARAMETERS | PayActLegislativeParameters | ✅ |
| OBJECT_VERSION_NUMBER | PayActObjectVersionNumber | — |
| ORG_PAYMENT_METHOD_ID | PayActOrgPaymentMethodId | — |
| OVERRIDING_DD_DATE | PayActOverridingDdDate | ✅ |
| PAY_REQUEST_ID | PayActPayRequestId | — |
| PAYMENT_TYPE_ID | PayActPaymentTypeId | — |
| PAYROLL_ACTION_ID | PayActPayrollActionId | ✅ |
| PAYROLL_ID | PayActPayrollId | — |
| REPORT_CATEGORY_ID | PayActReportCategoryId | — |
| REPORT_FORMAT_MAPPING_ID | PayActReportFormatMappingId | — |
| RETRO_DEFINITION_ID | PayActRetroDefinitionId | — |
| RUN_TYPE_ID | PayActRunTypeId | — |
| START_CHEQUE_NUMBER | PayActStartChequeNumber | ✅ |
| START_DATE | PayActStartDate | — |
| TARGET_PAYROLL_ACTION_ID | PayActTargetPayrollActionId | — |

### [[prepaymentcosting|PrePaymentCosting]] (GL · BICC: 20/39)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_PARAMETER_GROUP_ID | PayActActionParameterGroupId | — |
| ACTION_POPULATION_STATUS | PayActActionPopulationStatus | ✅ |
| ACTION_SEQUENCE | PayActActionSequence | ✅ |
| ACTION_STATUS | PayActActionStatus | ✅ |
| ACTION_TYPE | PayActActionType | ✅ |
| ASSIGNMENT_SET_ID | PayActAssignmentSetId | — |
| BATCH_PROCESS_MODE | PayActBatchProcessMode | ✅ |
| CHEQUE_PROCEDURE | PayActChequeProcedure | ✅ |
| CONSOLIDATION_SET_ID | PayActConsolidationSetId | — |
| CREATED_BY | PayActCreatedBy | — |
| CREATION_DATE | PayActCreationDate | — |
| CURRENT_CHUNK_NUMBER | PayActCurrentChunkNumber | ✅ |
| CURRENT_TASK | PayActCurrentTask | ✅ |
| DATE_EARNED | PayActDateEarned | ✅ |
| DISPLAY_RUN_NUMBER | PayActDisplayRunNumber | ✅ |
| EFFECTIVE_DATE | PayActEffectiveDate | ✅ |
| ELEMENT_SET_ID | PayActElementSetId | — |
| END_CHEQUE_NUMBER | PayActEndChequeNumber | ✅ |
| END_DATE | PayActEndDate | ✅ |
| FUTURE_PROCESS_MODE | PayActFutureProcessMode | ✅ |
| LAST_UPDATE_DATE | PayActLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PayActLastUpdateLogin | — |
| LAST_UPDATED_BY | PayActLastUpdatedBy | — |
| LEGISLATIVE_DATA_GROUP_ID | PayActLegislativeDataGroupId | — |
| LEGISLATIVE_PARAMETERS | PayActLegislativeParameters | ✅ |
| OBJECT_VERSION_NUMBER | PayActObjectVersionNumber | — |
| ORG_PAYMENT_METHOD_ID | PayActOrgPaymentMethodId | — |
| OVERRIDING_DD_DATE | PayActOverridingDdDate | ✅ |
| PAY_REQUEST_ID | PayActPayRequestId | — |
| PAYMENT_TYPE_ID | PayActPaymentTypeId | — |
| PAYROLL_ACTION_ID | PayActPayrollActionId | ✅ |
| PAYROLL_ID | PayActPayrollId | — |
| REPORT_CATEGORY_ID | PayActReportCategoryId | — |
| REPORT_FORMAT_MAPPING_ID | PayActReportFormatMappingId | — |
| RETRO_DEFINITION_ID | PayActRetroDefinitionId | — |
| RUN_TYPE_ID | PayActRunTypeId | — |
| START_CHEQUE_NUMBER | PayActStartChequeNumber | ✅ |
| START_DATE | PayActStartDate | ✅ |
| TARGET_PAYROLL_ACTION_ID | PayActTargetPayrollActionId | — |

### [[prepayments|PrePayments]] (AP · BICC: 20/40)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_PARAMETER_GROUP_ID | PayActActionParameterGroupId | — |
| ACTION_POPULATION_STATUS | PayActActionPopulationStatus | ✅ |
| ACTION_SEQUENCE | PayActActionSequence | ✅ |
| ACTION_STATUS | PayActActionStatus | ✅ |
| ACTION_TYPE | PayActActionType | ✅ |
| ASSIGNMENT_SET_ID | PayActAssignmentSetId | — |
| BATCH_PROCESS_MODE | PayActBatchProcessMode | ✅ |
| CHEQUE_PROCEDURE | PayActChequeProcedure | ✅ |
| CONSOLIDATION_SET_ID | PayActConsolidationSetId | — |
| CREATED_BY | PayActCreatedBy | — |
| CREATION_DATE | PayActCreationDate | — |
| CURRENT_CHUNK_NUMBER | PayActCurrentChunkNumber | ✅ |
| CURRENT_TASK | PayActCurrentTask | ✅ |
| DATE_EARNED | PayActDateEarned | ✅ |
| DISPLAY_RUN_NUMBER | PayActDisplayRunNumber | ✅ |
| EFFECTIVE_DATE | PayActEffectiveDate | ✅ |
| ELEMENT_SET_ID | PayActElementSetId | — |
| END_CHEQUE_NUMBER | PayActEndChequeNumber | ✅ |
| END_DATE | PayActEndDate | ✅ |
| FUTURE_PROCESS_MODE | PayActFutureProcessMode | ✅ |
| LAST_UPDATE_DATE | PayActLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PayActLastUpdateLogin | — |
| LAST_UPDATED_BY | PayActLastUpdatedBy | — |
| LEGISLATIVE_DATA_GROUP_ID | PayActLegislativeDataGroupId | — |
| LEGISLATIVE_PARAMETERS | PayActLegislativeParameters | ✅ |
| OBJECT_VERSION_NUMBER | PayActObjectVersionNumber | — |
| ORG_PAYMENT_METHOD_ID | PayActOrgPaymentMethodId | — |
| OVERRIDING_DD_DATE | PayActOverridingDdDate | ✅ |
| PAY_REQUEST_ID | PayActPayRequestId | — |
| PAYMENT_TYPE_ID | PayActPaymentTypeId | — |
| PAYROLL_ACTION_ID | PayActPayrollActionId | ✅ |
| PAYROLL_ACTION_ID | RunActPayrollActionId | — |
| PAYROLL_ID | PayActPayrollId | — |
| REPORT_CATEGORY_ID | PayActReportCategoryId | — |
| REPORT_FORMAT_MAPPING_ID | PayActReportFormatMappingId | — |
| RETRO_DEFINITION_ID | PayActRetroDefinitionId | — |
| RUN_TYPE_ID | PayActRunTypeId | — |
| START_CHEQUE_NUMBER | PayActStartChequeNumber | ✅ |
| START_DATE | PayActStartDate | ✅ |
| TARGET_PAYROLL_ACTION_ID | PayActTargetPayrollActionId | — |

### [[retroelemententry|RetroElementEntry]] (HCM · BICC: 18/33)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_PARAMETER_GROUP_ID | PayrollActionActionParameterGroupId | — |
| ACTION_POPULATION_STATUS | PayrollActionActionPopulationStatus | ✅ |
| ACTION_SEQUENCE | PayrollActionActionSequence | ✅ |
| ACTION_STATUS | PayrollActionActionStatus | ✅ |
| ACTION_TYPE | PayrollActionActionType | ✅ |
| ASSIGNMENT_SET_ID | PayrollActionAssignmentSetId | — |
| BATCH_PROCESS_MODE | PayrollActionBatchProcessMode | ✅ |
| CHEQUE_PROCEDURE | PayrollActionChequeProcedure | ✅ |
| CONSOLIDATION_SET_ID | PayrollActionConsolidationSetId | — |
| CURRENT_CHUNK_NUMBER | PayrollActionCurrentChunkNumber | ✅ |
| CURRENT_TASK | PayrollActionCurrentTask | ✅ |
| DATE_EARNED | PayrollActionDateEarned | ✅ |
| DISPLAY_RUN_NUMBER | PayrollActionDisplayRunNumber | ✅ |
| EFFECTIVE_DATE | PayrollActionEffectiveDate | ✅ |
| ELEMENT_SET_ID | PayrollActionElementSetId | — |
| END_CHEQUE_NUMBER | PayrollActionEndChequeNumber | ✅ |
| END_DATE | PayrollActionEndDate | ✅ |
| FUTURE_PROCESS_MODE | PayrollActionFutureProcessMode | ✅ |
| LEGISLATIVE_DATA_GROUP_ID | PayrollActionLegislativeDataGroupId | — |
| LEGISLATIVE_PARAMETERS | PayrollActionLegislativeParameters | ✅ |
| ORG_PAYMENT_METHOD_ID | PayrollActionOrgPaymentMethodId | — |
| OVERRIDING_DD_DATE | PayrollActionOverridingDdDate | ✅ |
| PAY_REQUEST_ID | PayrollActionPayRequestId | — |
| PAYMENT_TYPE_ID | PayrollActionPaymentTypeId | — |
| PAYROLL_ACTION_ID | PayrollActionPayrollActionId | — |
| PAYROLL_ID | PayrollActionPayrollId | — |
| REPORT_CATEGORY_ID | PayrollActionReportCategoryId | — |
| REPORT_FORMAT_MAPPING_ID | PayrollActionReportFormatMappingId | — |
| RETRO_DEFINITION_ID | PayrollActionRetroDefinitionId | — |
| RUN_TYPE_ID | PayrollActionRunTypeId | — |
| START_CHEQUE_NUMBER | PayrollActionStartChequeNumber | ✅ |
| START_DATE | PayrollActionStartDate | ✅ |
| TARGET_PAYROLL_ACTION_ID | PayrollActionTargetPayrollActionId | — |

---

## 📚 Referências

- [Oracle Docs — PAY_PAYROLL_ACTIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paypayrollactions.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
