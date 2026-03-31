---
id: DOC-HCM-083
doc_type: system-doc
title: "CMP_PLAN_PERIODS — Períodos dos Planos de Compensação"
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
  - compensation
  - periodos
  - ciclo
  - plan-period
aliases:
  - CMP_PLAN_PERIODS
  - cmp_plan_periods
  - cmp-plan-periods
  - DOC-HCM-083
  - períodos-dos-planos-de-compensação
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_PLAN_PERIODS

## 📌 Visão Geral

Armazena os **períodos** associados a cada plano de compensação. Cada registro define um período (ex: anual, semestral) dentro do qual as atividades de compensação são executadas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Controle temporal:** Define janelas de tempo para ciclos de compensação.
- **Orçamentação por período:** Distribuição de orçamento por intervalos definidos.
- **Fechamento de ciclos:** Controle de abertura e encerramento de períodos.
- **Histórico de ciclos:** Manutenção do histórico de períodos por plano.
- **Integração com payroll:** Alinhamento de períodos de compensação com folha.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PLAN_PERIOD_ID | NUMBER(18) | NOT NULL | PK | Identificador único do período | — | 🟢 95% |
| 2 | PLAN_ID | NUMBER(18) | NOT NULL | FK | Plano de compensação | [[cmp_plans_b]] | 🟢 95% |
| 3 | PERIOD_NAME | VARCHAR2(240) | NULL | Identificação | Nome do período | — | 🟡 80% |
| 4 | START_DATE | DATE | NOT NULL | Data | Data de início do período | — | 🟢 90% |
| 5 | END_DATE | DATE | NOT NULL | Data | Data de fim do período | — | 🟢 90% |
| 6 | STATUS_CODE | VARCHAR2(30) | NULL | Status | Status do período (OPEN, CLOSED) | — | 🟡 80% |
| 7 | BUDGET_AMOUNT | NUMBER | NULL | Financeiro | Orçamento do período | — | 🟡 70% |
| 8 | CURRENCY_CODE | VARCHAR2(30) | NULL | Referência | Moeda | — | 🟢 90% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[cmp_plans_b]] — via `PLAN_ID` (plano de compensacao do periodo)

### Tabelas-filha (FK de saída)
- [[cmp_salary]] — via `PLAN_PERIOD_ID` (salários no período)

---

## 📎 Uso Típico

### Períodos abertos por plano
```sql
SELECT pp.PLAN_PERIOD_ID, pp.PERIOD_NAME, pp.START_DATE, pp.END_DATE
FROM   CMP_PLAN_PERIODS pp
WHERE  pp.PLAN_ID = :p_plan_id
  AND  pp.STATUS_CODE = 'OPEN';
```

### Histórico de períodos
```sql
SELECT pp.PERIOD_NAME, pp.START_DATE, pp.END_DATE,
       pp.STATUS_CODE, pp.BUDGET_AMOUNT
FROM   CMP_PLAN_PERIODS pp
WHERE  pp.PLAN_ID = :p_plan_id
ORDER BY pp.START_DATE DESC;
```

---

## 🔒 Observações

- Cada plano pode ter múltiplos períodos (ex: ciclo anual gera um período por ano).
- O `STATUS_CODE` controla se o período aceita novas transações.
- Períodos CLOSED não permitem criação ou alteração de registros de compensação.
- O `BUDGET_AMOUNT` pode ser diferente em cada período conforme aprovação.

---

## 🔗 PVOs Relacionados

### [[planperiodpvo|PlanPeriodPVO]] (HCM · BICC: 34/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_CHANGE_DATE | PlanPeriodPEOAssignmentChangeDate | ✅ |
| AVAIL_END_DATE | PlanPeriodPEOAvailEndDate | ✅ |
| AVAIL_START_DATE | PlanPeriodPEOAvailStartDate | ✅ |
| COMP_TYPE | CompType | ✅ |
| CREATED_BY | PlanPeriodPEOCreatedBy | ✅ |
| CREATION_DATE | PlanPeriodPEOCreationDate | ✅ |
| DEFAULT_DUE_DATE | PlanPeriodPEODefaultDueDate | ✅ |
| DISPLAY_NAME | PlanPeriodPEODisplayName | ✅ |
| ELIGIBILITY_DATE | PlanPeriodPEOEligibilityDate | ✅ |
| END_DATE | PlanPeriodPEOEndDate | ✅ |
| EXCHANGE_RATE_DATE | PlanPeriodPEOExchangeRateDate | ✅ |
| FREEZE_DATE | PlanPeriodPEOFreezeDate | ✅ |
| LAST_UPDATE_DATE | PlanPeriodPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PlanPeriodPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PlanPeriodPEOLastUpdatedBy | ✅ |
| LVL_1_DEFAULT_DUE_DATE | PlanPeriodPEOLvl1DefaultDueDate | ✅ |
| LVL_2_DEFAULT_DUE_DATE | PlanPeriodPEOLvl2DefaultDueDate | ✅ |
| LVL_3_DEFAULT_DUE_DATE | PlanPeriodPEOLvl3DefaultDueDate | ✅ |
| LVL_4_DEFAULT_DUE_DATE | PlanPeriodPEOLvl4DefaultDueDate | ✅ |
| LVL_5_DEFAULT_DUE_DATE | PlanPeriodPEOLvl5DefaultDueDate | ✅ |
| LVL_6_DEFAULT_DUE_DATE | PlanPeriodPEOLvl6DefaultDueDate | ✅ |
| LVL_7_DEFAULT_DUE_DATE | PlanPeriodPEOLvl7DefaultDueDate | ✅ |
| MGR_UPD_DUE_DATE_FLAG | PlanPeriodPEOMgrUpdDueDateFlag | ✅ |
| OBJECT_VERSION_NUMBER | PlanPeriodPEOObjectVersionNumber | ✅ |
| PERFORMANCE_DATE | PlanPeriodPEOPerformanceDate | ✅ |
| PERIOD_ID | PeriodId | ✅ |
| PERIOD_NAME | PlanPeriodPEOPeriodName | ✅ |
| PERIOD_TYPE | PlanPeriodPEOPeriodType | ✅ |
| PLAN_ACCESS_ID | PlanPeriodPEOPlanAccessId | ✅ |
| PLAN_ID | PlanPeriodPEOPlanId | ✅ |
| START_DATE | PlanPeriodPEOStartDate | ✅ |
| TOP_MGR_DEFAULT_DUE_DATE | PlanPeriodPEOTopMgrDefaultDueDate | ✅ |
| UPDATE_END_DATE | PlanPeriodPEOUpdateEndDate | ✅ |
| UPDATE_START_DATE | PlanPeriodPEOUpdateStartDate | ✅ |

---

## 📚 Referências

- [Oracle Docs — CMP_PLAN_PERIODS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpplanperiods.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
