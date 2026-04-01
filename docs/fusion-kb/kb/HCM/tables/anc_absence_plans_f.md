---
id: DOC-HCM-003
doc_type: system-doc
title: "ANC_ABSENCE_PLANS_F — Planos de Ausência"
system: Oracle Fusion Cloud HCM
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
  - absence-management
  - planos-ausencia
  - absence-plans
  - accrual
aliases:
  - ANC_ABSENCE_PLANS_F
  - anc_absence_plans_f
  - planos-ausencia-hcm
  - absence-plans
  - anc-abs-plans
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ANC_ABSENCE_PLANS_F

## 📌 Visão Geral

Armazena os **planos de ausência** do módulo Absence Management. Um plano define as regras de acumulação, elegibilidade e saldo para um tipo específico de ausência (ex.: plano de férias com 30 dias anuais, plano de licença médica com regras de acúmulo mensal).

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição de políticas de ausência:** Configura regras de acumulação (accrual), teto de saldo, carência e carry-over.
- **Elegibilidade:** Define critérios de elegibilidade por cargo, departamento, legislação ou antiguidade.
- **Cálculo de saldos:** Base para o cálculo de saldo disponível de ausências por colaborador.
- **Compliance trabalhista:** Atende requisitos legais de férias, licenças e afastamentos por jurisdição.
- **Integração com folha:** Planos vinculados a elementos de folha de pagamento para desconto/pagamento.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ABSENCE_PLAN_ID | NUMBER(18) | NOT NULL | PK | Identificador único do plano de ausência | — | 🟢 95% |
| 2 | PLAN_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do plano de ausência | — | 🟢 90% |
| 3 | PLAN_STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status do plano (A — ativo, I — inativo) | — | 🟢 90% |
| 4 | ABSENCE_TYPE_ID | NUMBER(18) | NULL | FK | Tipo de ausência associado ao plano | [[anc_absence_types_f]] | 🟡 75% |
| 5 | LEGISLATION_CODE | VARCHAR2(30) | NULL | Classificação | Código da legislação aplicável | — | 🟢 90% |
| 6 | ACCRUAL_FREQUENCY | VARCHAR2(30) | NULL | Configuração | Frequência de acumulação (MONTHLY, YEARLY, etc.) | — | 🟡 70% |
| 7 | ACCRUAL_RATE | NUMBER | NULL | Configuração | Taxa de acumulação por período | — | 🟡 70% |
| 8 | MAX_CARRYOVER | NUMBER | NULL | Configuração | Máximo de saldo transferível entre períodos | — | 🟡 70% |
| 9 | CEILING_LIMIT | NUMBER | NULL | Configuração | Teto máximo de acumulação | — | 🟡 70% |
| 10 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 11 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 12 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 13 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 14 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 15 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 16 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[anc_absence_types_f]] — via `ABSENCE_TYPE_ID` (tipo de ausência associado)

### Tabelas-filha (FK de saída)
- [[anc_absence_plans_f_tl]] — via `ABSENCE_PLAN_ID` (traducoes multilingue do registro)
- [[anc_per_plan_enrollment]] — via `ABSENCE_PLAN_ID` (inscrições de colaboradores)
- [[anc_per_abs_plan_entries]] — via `ABSENCE_PLAN_ID` (entradas de plano por pessoa)
- [[anc_accrual_bands_f]] — via `ABSENCE_PLAN_ID` (faixas de acumulação)

---

## 📎 Uso Típico

### Planos de ausência ativos por legislação
```sql
SELECT ap.ABSENCE_PLAN_ID, ap.PLAN_NAME, ap.PLAN_STATUS,
       ap.ACCRUAL_FREQUENCY, ap.CEILING_LIMIT
FROM   ANC_ABSENCE_PLANS_F ap
WHERE  SYSDATE BETWEEN ap.EFFECTIVE_START_DATE AND ap.EFFECTIVE_END_DATE
  AND  ap.PLAN_STATUS = 'A'
  AND  ap.LEGISLATION_CODE = :p_legislation_code;
```

### Filtros comuns
- `PLAN_STATUS = 'A'` — Planos ativos
- `LEGISLATION_CODE = 'BR'` — Planos para legislação brasileira
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Registros vigentes

---

## 🔒 Observações

- Tabela date-effective: sempre filtrar por vigência.
- O plano define as regras; a inscrição do colaborador está em `ANC_PER_PLAN_ENROLLMENT`.
- Campos de acumulação (`ACCRUAL_FREQUENCY`, `ACCRUAL_RATE`, `MAX_CARRYOVER`, `CEILING_LIMIT`) podem ter valores nulos se o plano não usar acumulação automática.
- Planos podem ser associados a elementos de folha via integração Payroll.

---

## 🔗 PVOs Relacionados

### [[absenceplanpvo|AbsencePlanPVO]] (GL · BICC: 99/103)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ABSENCE_DURATION_DEFN_ID | AbsenceDurationDefnId | ✅ |
| ABSENCE_PLAN_ID | AbsencePlanId | ✅ |
| ACC_DEFINITION_TYPE | AccDefinitionType | ✅ |
| ACC_FORMULA_ID | AccFormulaId | ✅ |
| ACC_NEGATIVE_BAL_FLAG | AccNegativeBalFlag | ✅ |
| ACC_NEGATIVE_BAL_LIMIT | AccNegativeBalLimit | ✅ |
| ACC_NEGATIVE_BAL_UOM | AccNegativeBalUom | ✅ |
| ACC_PERIOD_FREQUENCY | AccPeriodFrequency | ✅ |
| ACC_PERIOD_PAYROLL_FREQ_ID | AccPeriodPayrollFreqId | ✅ |
| ACC_PERIOD_WFM_CALEDAR_ID | AccPeriodWfmCaledarId | ✅ |
| ACCRUAL_METHOD_CD | AccrualMethodCd | ✅ |
| ACCRUAL_MODE | AccrualMode | ✅ |
| ACCRUAL_VESTING_CD | AccrualVestingCD | ✅ |
| ANC_ABSENCE_PLANS_F_ALTCD | AncAbsencePlansFAltcd | ✅ |
| ANNIVERSARY_EVENT_FORMULA_ID | AnniversaryEventFormulaId | ✅ |
| ANNIVERSARY_EVENT_RULE | AnniversaryEventRule | ✅ |
| BALANCE_TRANSFER_FLAG | BalanceTransferFlag | ✅ |
| CALENDAR_START_DAY | CalendarStartDay | ✅ |
| CALENDAR_START_MONTH | CalendarStartMonth | ✅ |
| CARRY_OVER_EXPIRED_FLAG | CarryOverExpiredFlag | ✅ |
| CARRY_OVER_EXPIRED_UNITS | CarryOverExpiredUnits | ✅ |
| CARRY_OVER_EXPIRED_UOM | CarryOverExpiredUom | ✅ |
| CARRY_OVER_FLAT_AMT | CarryOverFlatAmt | ✅ |
| CARRY_OVER_FORMULA_ID | CarryOverFormulaId | ✅ |
| CARRY_OVER_PRORATE_FORMULA_ID | CarryOverProrateFormulaId | ✅ |
| CARRY_OVER_PRORATE_RULE | CarryOverProrateRule | ✅ |
| CARRY_OVER_RULE | CarryOverRule | ✅ |
| CASH_OUT_FLAG | CashOutFlag | ✅ |
| CASHOUT_RATE_FORMULA_ID | CashoutRateFormulaId | ✅ |
| CASHOUT_RATE_ID | CashoutRateId | ✅ |
| CASHOUT_RATE_RULE | CashoutRateRule | ✅ |
| CEIL_LIMIT_FLAT_AMT | CeilLimitFlatAmt | ✅ |
| CEIL_LIMIT_FORMULA_ID | CeilLimitFormulaId | ✅ |
| CEIL_LIMIT_PRORATE_RULE | CeilLimitProrateRule | ✅ |
| CEIL_LIMIT_RULE | CeilLimitRule | ✅ |
| CEIL_LMT_PRORATE_FORMULA_ID | CeilLmtProrateFormulaId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| EMP_ENRL_NEGATIVE_BALANCE_FLAG | EmpEnrlNegativeBalanceFlag | ✅ |
| EMP_ENRL_POSITIVE_BALANCE_FLAG | EmpEnrlPositiveBalanceFlag | ✅ |
| EMP_ENRL_TERMINATE_ENTL_FLAG | EmpEnrlTerminateEntlFlag | ✅ |
| ENROLL_NEGATIVE_BALANCE_FLAG | EnrollNegativeBalanceFlag | ✅ |
| ENROLL_POSITIVE_BALANCE_FLAG | EnrollPositiveBalanceFlag | ✅ |
| ENROLL_TERMINATE_ENTL_FLAG | EnrollTerminateEntlFlag | ✅ |
| ENROLLMENT_END_FORMULA_ID | EnrollmentEndFormulaId | ✅ |
| ENROLLMENT_END_RULE | EnrollmentEndRule | ✅ |
| ENROLLMENT_START_FORMULA_ID | EnrollmentStartFormulaId | ✅ |
| ENROLLMENT_START_RULE | EnrollmentStartRule | ✅ |
| ENTERPRISE_ID | EnterpriseId | — |
| ENTITLEMENT_END_FORMULA_ID | EntitlementEndFormulaId | ✅ |
| ENTITLEMENT_END_RULE | EntitlementEndRule | ✅ |
| ENTL_DEFINITION_TYPE | EntlDefinitionType | ✅ |
| ENTL_FORMULA_ID | EntlFormulaId | ✅ |
| ENTL_METHOD_CD | EntlMethodCd | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEGISLATION_CODE | LegislationCode | — |
| LEGISLATIVE_DATA_GROUP_ID | LegislativeDataGroupId | ✅ |
| LIABILITY_RATE_FORMULA_ID | LiabilityRateFormulaId | ✅ |
| LIABILITY_RATE_ID | LiabilityRateId | ✅ |
| LIABILITY_RATE_RULE | LiabilityRateRule | ✅ |
| MODULE_ID | ModuleId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OTHER_ADJUSTMENT_FLAG | OtherAdjustmentFlag | ✅ |
| OTHER_REASONS | OtherReasons | ✅ |
| OVERLAP_CD | OverlapCd | ✅ |
| PARTIAL_ACCRUAL_FORMULA_ID | PartialAccrualFormulaId | ✅ |
| PAY_ADVANCES_FLAG | PayAdvancesFlag | ✅ |
| PAY_RATE_FACTOR | PayRateFactor | ✅ |
| PAYOUT_RATE_FORMULA_ID | PayoutRateFormulaId | ✅ |
| PAYOUT_RATE_ID | PayoutRateId | ✅ |
| PAYOUT_RATE_RULE | PayoutRateRule | ✅ |
| PAYROLL_IMPACT_FLAG | PayrollImpactFlag | ✅ |
| PAYROLL_MAPPING_ID | PayrollMappingId | ✅ |
| PERIOD_UOM | PeriodUom | ✅ |
| PLAN_ACTIVATION_FLAG | PlanActivationFlag | ✅ |
| PLAN_MGMT_CD | PlanMgmtCd | ✅ |
| PLAN_PERIOD_ID | PlanPeriodId | ✅ |
| PLAN_PERIOD_TYPE | PlanPeriodType | ✅ |
| PLAN_STATUS | PlanStatus | ✅ |
| PLAN_UOM | PlanUom | ✅ |
| PLAN_USE_FORMULA_ID | PlanUseFormulaId | ✅ |
| PLAN_USE_RATE_ID | PlanUseRateId | ✅ |
| PLAN_USE_RATE_RULE | PlanUseRateRule | ✅ |
| PREV_EMP_ENTL_FLAG | PrevEmpEntlFlag | ✅ |
| PREV_EMP_USAGE_FLAG | PrevEmpUsageFlag | ✅ |
| PROCESSING_LEVEL_CD | ProcessingLevelCd | ✅ |
| PRORATION_FORMULA_ID | ProrationFormulaId | ✅ |
| PRORATION_RULE | ProrationRule | ✅ |
| ROLL_BACKWARD_END_FORMULA_ID | RollBackwardEndFormulaId | ✅ |
| ROLL_BACKWARD_END_RULE | RollBackwardEndRule | ✅ |
| ROLL_FORWARD_START_FORMULA_ID | RollForwardStartFormulaId | ✅ |
| ROLL_FORWARD_START_RULE | RollForwardStartRule | ✅ |
| ROLL_PERIOD_DURATION | RollPeriodDuration | ✅ |
| STATUTORY_FLAG | StatutoryFlag | ✅ |
| VESTING_PERIOD_DURATION | VestingPeriodDuration | ✅ |
| VESTING_PERIOD_FORMULA_ID | VestingPeriodFormulaId | ✅ |
| VESTING_PERIOD_UOM | VestingPeriodUom | ✅ |
| WAIT_PERIOD_DUR_UNITS | WaitPeriodDurUnits | ✅ |
| WAIT_PERIOD_DUR_UOM | WaitPeriodDurUom | ✅ |

### [[accrualplanpvo|AccrualPlanPVO]] (GL · BICC: 14/259)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ABSENCE_DURATION_DEFN_ID | AbsenceDurationDefnId | — |
| ABSENCE_DURATION_FORMULA_ID | AbsenceDurationFormulaId | — |
| ABSENCE_PLAN_ID | AbsencePlanId | ✅ |
| ACC_DEFINITION_TYPE | AccDefinitionType | — |
| ACC_FORMULA_ID | AccFormulaId | — |
| ACC_NEGATIVE_BAL_FLAG | AccNegativeBalFlag | — |
| ACC_NEGATIVE_BAL_LIMIT | AccNegativeBalLimit | — |
| ACC_NEGATIVE_BAL_UOM | AccNegativeBalUom | — |
| ACC_PERIOD_FREQUENCY | AccPeriodFrequency | — |
| ACC_PERIOD_PAYROLL_FREQ_ID | AccPeriodPayrollFreqId | — |
| ACC_PERIOD_WFM_CALEDAR_ID | AccPeriodWfmCaledarId | — |
| ACCRUAL_METHOD_CD | AccrualMethodCd | ✅ |
| ACCRUAL_MODE | AccrualMode | — |
| ACCRUAL_VESTING_CD | AccrualVestingCd | ✅ |
| ANC_ABSENCE_PLANS_F_ALTCD | AncAbsencePlansFAltcd | — |
| ANC_CHAR1 | AncChar1 | — |
| ANC_CHAR2 | AncChar2 | — |
| ANC_CHAR3 | AncChar3 | — |
| ANC_CHAR4 | AncChar4 | — |
| ANC_CHAR5 | AncChar5 | — |
| ANC_DATE1 | AncDate1 | — |
| ANC_DATE2 | AncDate2 | — |
| ANC_DATE3 | AncDate3 | — |
| ANC_DATE4 | AncDate4 | — |
| ANC_DATE5 | AncDate5 | — |
| ANC_NUMBER1 | AncNumber1 | — |
| ANC_NUMBER2 | AncNumber2 | — |
| ANC_NUMBER3 | AncNumber3 | — |
| ANC_NUMBER4 | AncNumber4 | — |
| ANC_NUMBER5 | AncNumber5 | — |
| ANNIVERSARY_EVENT_FORMULA_ID | AnniversaryEventFormulaId | — |
| ANNIVERSARY_EVENT_RULE | AnniversaryEventRule | — |
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE21 | Attribute21 | — |
| ATTRIBUTE22 | Attribute22 | — |
| ATTRIBUTE23 | Attribute23 | — |
| ATTRIBUTE24 | Attribute24 | — |
| ATTRIBUTE25 | Attribute25 | — |
| ATTRIBUTE26 | Attribute26 | — |
| ATTRIBUTE27 | Attribute27 | — |
| ATTRIBUTE28 | Attribute28 | — |
| ATTRIBUTE29 | Attribute29 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE30 | Attribute30 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE11 | AttributeDate11 | — |
| ATTRIBUTE_DATE12 | AttributeDate12 | — |
| ATTRIBUTE_DATE13 | AttributeDate13 | — |
| ATTRIBUTE_DATE14 | AttributeDate14 | — |
| ATTRIBUTE_DATE15 | AttributeDate15 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_DATE6 | AttributeDate6 | — |
| ATTRIBUTE_DATE7 | AttributeDate7 | — |
| ATTRIBUTE_DATE8 | AttributeDate8 | — |
| ATTRIBUTE_DATE9 | AttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| BALANCE_TRANSFER_FLAG | BalanceTransferFlag | — |
| CALENDAR_START_DAY | CalendarStartDay | — |
| CALENDAR_START_MONTH | CalendarStartMonth | — |
| CARRY_OVER_EXPIRED_FLAG | CarryOverExpiredFlag | — |
| CARRY_OVER_EXPIRED_UNITS | CarryOverExpiredUnits | ✅ |
| CARRY_OVER_EXPIRED_UOM | CarryOverExpiredUom | ✅ |
| CARRY_OVER_FLAT_AMT | CarryOverFlatAmt | ✅ |
| CARRY_OVER_FORMULA_ID | CarryOverFormulaId | — |
| CARRY_OVER_PRORATE_FORMULA_ID | CarryOverProrateFormulaId | — |
| CARRY_OVER_PRORATE_RULE | CarryOverProrateRule | — |
| CARRY_OVER_RULE | CarryOverRule | — |
| CASH_OUT_FLAG | CashOutFlag | — |
| CASHOUT_RATE_FORMULA_ID | CashoutRateFormulaId | — |
| CASHOUT_RATE_ID | CashoutRateId | — |
| CASHOUT_RATE_RULE | CashoutRateRule | — |
| CEIL_LIMIT_FLAT_AMT | CeilLimitFlatAmt | ✅ |
| CEIL_LIMIT_FORMULA_ID | CeilLimitFormulaId | — |
| CEIL_LIMIT_PRORATE_RULE | CeilLimitProrateRule | — |
| CEIL_LIMIT_RULE | CeilLimitRule | — |
| CEIL_LMT_PRORATE_FORMULA_ID | CeilLmtProrateFormulaId | — |
| COMP_EXP_ADJRSN | CompExpAdjrsn | — |
| COMP_MNUL_ADJRSN | CompMnulAdjrsn | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DONATION_TYPE | AccrualPlanDPEODonationType | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| EMP_ENRL_NEGATIVE_BALANCE_FLAG | EmpEnrlNegativeBalanceFlag | — |
| EMP_ENRL_POSITIVE_BALANCE_FLAG | EmpEnrlPositiveBalanceFlag | — |
| EMP_ENRL_TERMINATE_ENTL_FLAG | EmpEnrlTerminateEntlFlag | — |
| ENROLL_NEGATIVE_BALANCE_FLAG | EnrollNegativeBalanceFlag | — |
| ENROLL_POSITIVE_BALANCE_FLAG | EnrollPositiveBalanceFlag | — |
| ENROLL_TERMINATE_ENTL_FLAG | EnrollTerminateEntlFlag | — |
| ENROLLMENT_END_FORMULA_ID | EnrollmentEndFormulaId | — |
| ENROLLMENT_END_RULE | EnrollmentEndRule | — |
| ENROLLMENT_START_FORMULA_ID | EnrollmentStartFormulaId | — |
| ENROLLMENT_START_RULE | EnrollmentStartRule | — |
| ENTERPRISE_ID | EnterpriseId | — |
| ENTITLEMENT_END_FORMULA_ID | EntitlementEndFormulaId | — |
| ENTITLEMENT_END_RULE | EntitlementEndRule | — |
| ENTITLEMENT_START_DATE | EntitlementStartDate | — |
| ENTL_DEFINITION_TYPE | EntlDefinitionType | — |
| ENTL_FORMULA_ID | EntlFormulaId | — |
| ENTL_METHOD_CD | EntlMethodCd | ✅ |
| EXPIRATION_ACTION_CD | ExpirationActionCd | — |
| EXPIRATION_LIMIT | ExpirationLimit | — |
| EXPIRATION_TERM_CD | ExpirationTermCd | — |
| EXPIRATION_UOM_CD | ExpirationUomCd | — |
| INFORMATION1 | Information1 | — |
| INFORMATION10 | Information10 | — |
| INFORMATION11 | Information11 | — |
| INFORMATION12 | Information12 | — |
| INFORMATION13 | Information13 | — |
| INFORMATION14 | Information14 | — |
| INFORMATION15 | Information15 | — |
| INFORMATION16 | Information16 | — |
| INFORMATION17 | Information17 | — |
| INFORMATION18 | Information18 | — |
| INFORMATION19 | Information19 | — |
| INFORMATION2 | Information2 | — |
| INFORMATION20 | Information20 | — |
| INFORMATION21 | Information21 | — |
| INFORMATION22 | Information22 | — |
| INFORMATION23 | Information23 | — |
| INFORMATION24 | Information24 | — |
| INFORMATION25 | Information25 | — |
| INFORMATION26 | Information26 | — |
| INFORMATION27 | Information27 | — |
| INFORMATION28 | Information28 | — |
| INFORMATION29 | Information29 | — |
| INFORMATION3 | Information3 | — |
| INFORMATION30 | Information30 | — |
| INFORMATION4 | Information4 | — |
| INFORMATION5 | Information5 | — |
| INFORMATION6 | Information6 | — |
| INFORMATION7 | Information7 | — |
| INFORMATION8 | Information8 | — |
| INFORMATION9 | Information9 | — |
| INFORMATION_CATEGORY | InformationCategory | — |
| INFORMATION_DATE1 | InformationDate1 | — |
| INFORMATION_DATE10 | InformationDate10 | — |
| INFORMATION_DATE11 | InformationDate11 | — |
| INFORMATION_DATE12 | InformationDate12 | — |
| INFORMATION_DATE13 | InformationDate13 | — |
| INFORMATION_DATE14 | InformationDate14 | — |
| INFORMATION_DATE15 | InformationDate15 | — |
| INFORMATION_DATE2 | InformationDate2 | — |
| INFORMATION_DATE3 | InformationDate3 | — |
| INFORMATION_DATE4 | InformationDate4 | — |
| INFORMATION_DATE5 | InformationDate5 | — |
| INFORMATION_DATE6 | InformationDate6 | — |
| INFORMATION_DATE7 | InformationDate7 | — |
| INFORMATION_DATE8 | InformationDate8 | — |
| INFORMATION_DATE9 | InformationDate9 | — |
| INFORMATION_NUMBER1 | InformationNumber1 | — |
| INFORMATION_NUMBER10 | InformationNumber10 | — |
| INFORMATION_NUMBER11 | InformationNumber11 | — |
| INFORMATION_NUMBER12 | InformationNumber12 | — |
| INFORMATION_NUMBER13 | InformationNumber13 | — |
| INFORMATION_NUMBER14 | InformationNumber14 | — |
| INFORMATION_NUMBER15 | InformationNumber15 | — |
| INFORMATION_NUMBER16 | InformationNumber16 | — |
| INFORMATION_NUMBER17 | InformationNumber17 | — |
| INFORMATION_NUMBER18 | InformationNumber18 | — |
| INFORMATION_NUMBER19 | InformationNumber19 | — |
| INFORMATION_NUMBER2 | InformationNumber2 | — |
| INFORMATION_NUMBER20 | InformationNumber20 | — |
| INFORMATION_NUMBER3 | InformationNumber3 | — |
| INFORMATION_NUMBER4 | InformationNumber4 | — |
| INFORMATION_NUMBER5 | InformationNumber5 | — |
| INFORMATION_NUMBER6 | InformationNumber6 | — |
| INFORMATION_NUMBER7 | InformationNumber7 | — |
| INFORMATION_NUMBER8 | InformationNumber8 | — |
| INFORMATION_NUMBER9 | InformationNumber9 | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LEGISLATION_CODE | LegislationCode | — |
| LEGISLATIVE_DATA_GROUP_ID | LegislativeDataGroupId | — |
| LIABILITY_RATE_FORMULA_ID | LiabilityRateFormulaId | — |
| LIABILITY_RATE_ID | LiabilityRateId | — |
| LIABILITY_RATE_RULE | LiabilityRateRule | — |
| MODULE_ID | ModuleId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OTHER_ADJUSTMENT_FLAG | OtherAdjustmentFlag | — |
| OTHER_REASONS | OtherReasons | — |
| OVERLAP_CD | OverlapCd | — |
| PARTIAL_ACCRUAL_FORMULA_ID | PartialAccrualFormulaId | — |
| PAY_ADVANCES_FLAG | PayAdvancesFlag | — |
| PAY_RATE_FACTOR | PayRateFactor | — |
| PAYOUT_RATE_FORMULA_ID | PayoutRateFormulaId | — |
| PAYOUT_RATE_ID | PayoutRateId | — |
| PAYOUT_RATE_RULE | PayoutRateRule | — |
| PAYROLL_IMPACT_FLAG | PayrollImpactFlag | — |
| PAYROLL_MAPPING_ID | PayrollMappingId | — |
| PERIOD_UOM | PeriodUom | — |
| PLAN_ACTIVATION_FLAG | PlanActivationFlag | — |
| PLAN_MGMT_CD | PlanMgmtCd | — |
| PLAN_PERIOD_ID | PlanPeriodId | — |
| PLAN_PERIOD_TYPE | PlanPeriodType | ✅ |
| PLAN_STATUS | PlanStatus | ✅ |
| PLAN_UOM | PlanUom | ✅ |
| PLAN_USE_FORMULA_ID | PlanUseFormulaId | — |
| PLAN_USE_RATE_ID | PlanUseRateId | — |
| PLAN_USE_RATE_RULE | PlanUseRateRule | — |
| PREV_EMP_ENTL_FLAG | PrevEmpEntlFlag | — |
| PREV_EMP_USAGE_FLAG | PrevEmpUsageFlag | — |
| PROCESSING_LEVEL_CD | ProcessingLevelCd | — |
| PRORATION_FORMULA_ID | ProrationFormulaId | — |
| PRORATION_RULE | ProrationRule | — |
| ROLL_BACKWARD_END_FORMULA_ID | RollBackwardEndFormulaId | — |
| ROLL_BACKWARD_END_RULE | RollBackwardEndRule | — |
| ROLL_FORWARD_START_FORMULA_ID | RollForwardStartFormulaId | — |
| ROLL_FORWARD_START_RULE | RollForwardStartRule | — |
| ROLL_PERIOD_DURATION | RollPeriodDuration | — |
| STATUTORY_FLAG | StatutoryFlag | — |
| VESTING_PERIOD_DURATION | VestingPeriodDuration | — |
| VESTING_PERIOD_FORMULA_ID | VestingPeriodFormulaId | — |
| VESTING_PERIOD_UOM | VestingPeriodUom | — |
| WAIT_PERIOD_DUR_UNITS | WaitPeriodDurUnits | — |
| WAIT_PERIOD_DUR_UOM | WaitPeriodDurUom | — |

---

## 📚 Referências

- [Oracle Docs — ANC_ABSENCE_PLANS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ancabsenceplansf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
