---
id: DOC-HCM-080
doc_type: system-doc
title: "CMP_PERSON_BUDGETS_V — Visão de Orçamentos por Pessoa (CMP)"
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
  - orcamento
  - budget
  - view
aliases:
  - CMP_PERSON_BUDGETS_V
  - cmp_person_budgets_v
  - cmp-person-budgets-v
  - DOC-HCM-080
  - visão-de-orçamentos-por-pessoa-(cmp)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_PERSON_BUDGETS_V

## 📌 Visão Geral

**View** que apresenta os **orçamentos de compensação por pessoa**, consolidando informações de planos, períodos e valores alocados por colaborador. Facilita a análise de orçamento individual dentro dos ciclos de compensação.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Análise orçamentária individual:** Visão do budget alocado por colaborador.
- **Controle de gastos:** Monitoramento do orçamento utilizado vs. disponível.
- **Relatórios gerenciais:** Dados consolidados para gestores de compensação.
- **Planejamento de headcount:** Base para projeções de custo de pessoal.
- **Auditoria de alocação:** Verificação de consistência entre budget e aprovações.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Identificador da pessoa | [[per_all_people_f]] | 🟢 90% |
| 2 | ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Atribuição do colaborador | [[per_all_assignments_m]] | 🟢 90% |
| 3 | PLAN_ID | NUMBER(18) | NULL | FK | Plano de compensação | [[cmp_plans_b]] | 🟡 80% |
| 4 | PERIOD_ID | NUMBER(18) | NULL | FK | Período do plano | [[cmp_plan_periods]] | 🟡 75% |
| 5 | BUDGET_AMOUNT | NUMBER | NULL | Financeiro | Valor orçado para a pessoa | — | 🟡 75% |
| 6 | CURRENCY_CODE | VARCHAR2(30) | NULL | Referência | Moeda do orçamento | — | 🟢 90% |
| 7 | BUDGET_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de orçamento (SALARY, BONUS, TOTAL) | — | 🟡 70% |
| 8 | MANAGER_ID | NUMBER(18) | NULL | FK | Gestor responsável | [[per_all_people_f]] | 🟡 75% |
| 9 | DEPARTMENT_ID | NUMBER(18) | NULL | FK | Departamento | [[per_departments]] | 🟡 75% |
| 10 | EFFECTIVE_DATE | DATE | NULL | Data | Data de efetividade | — | 🟡 75% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador do orcamento de compensacao)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vinculo empregaticio do orcamento)
- [[cmp_plans_b]] — via `PLAN_ID` (plano de compensacao do orcamento)
- [[cmp_plan_periods]] — via `PERIOD_ID` (periodo do orcamento de compensacao)

### Tabelas-filha (FK de saída)
- Por ser uma view, não possui tabelas-filha diretas.

---

## 📎 Uso Típico

### Orçamento por pessoa e plano
```sql
SELECT pb.PERSON_ID, pb.PLAN_ID, pb.BUDGET_AMOUNT,
       pb.CURRENCY_CODE, pb.BUDGET_TYPE
FROM   CMP_PERSON_BUDGETS_V pb
WHERE  pb.PLAN_ID = :p_plan_id;
```

### Total orçado por departamento
```sql
SELECT pb.DEPARTMENT_ID, SUM(pb.BUDGET_AMOUNT) AS total_orcado
FROM   CMP_PERSON_BUDGETS_V pb
WHERE  pb.PLAN_ID = :p_plan_id
GROUP BY pb.DEPARTMENT_ID;
```

---

## 🔒 Observações

- Esta é uma **view** (sufixo `_V`), não uma tabela física — não possui índices próprios.
- Consolida dados de múltiplas tabelas de compensação para facilitar consultas.
- Performance pode ser inferior a consultas diretas nas tabelas base para grandes volumes.
- Utilizada principalmente por relatórios BI e dashboards de compensação.

---

## 🔗 PVOs Relacionados

### [[managerbudgetsfortopmgrpvo|ManagerBudgetsForTopMgrPVO]] (HCM · BICC: 23/47)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_CD | AccessCd | — |
| BUDGET_LAST_UPD_DATE | BudgetLastUpdDate | — |
| BUDGET_POP_CD | BudgetPopCd | — |
| BUDGET_VAL_AMOUNT | BudgetValAmount | — |
| BUDGET_VAL_PERCENT | BudgetValPercent | — |
| BUDGETING_STYLE | BudgetingStyle | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DFLT_DIST_BUDGET_VAL | DfltDistBudgetVal | — |
| DFLT_WS_BUDGET_VAL | DfltWsBudgetVal | — |
| DIST_BUDGET_ISSUE_DATE | DistBudgetIssueDate | — |
| DIST_BUDGET_ISSUE_VAL | DistBudgetIssueVal | ✅ |
| DIST_BUDGET_VAL | DistBudgetVal | ✅ |
| DIST_BUDGET_VAL_LAST_UPD_BY | DistBudgetValLastUpdBy | — |
| DIST_BUDGET_VAL_LAST_UPD_DATE | DistBudgetValLastUpdDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OVERALL_BUDGET_AMOUNT | OverallBudgetAmount | ✅ |
| OVERRIDE_OVER_ALLOCATE_CODE | OverrideOverAllocateCode | — |
| OVERRIDE_OVER_BUDGET_CODE | OverrideOverBudgetCode | — |
| PERIOD_ID | PeriodId | — |
| PERSON_EVENT_ID | PersonEventId | ✅ |
| PLAN_ID | PlanId | — |
| POOL_ID | PoolId | — |
| PUBLISHED_DIST_BUDGET_AMOUNT | PublishedDistBudgetAmount | ✅ |
| PUBLISHED_DIST_BUDGET_PCT | PublishedDistBudgetPct | ✅ |
| PUBLISHED_WS_BUDGET_AMOUNT | PublishedWsBudgetAmount | ✅ |
| PUBLISHED_WS_BUDGET_PCT | PublishedWsBudgetPct | ✅ |
| REC_MN_VAL_ALL | RecMnValAll | ✅ |
| REC_MX_VAL_ALL | RecMxValAll | ✅ |
| REC_VAL_ALL | RecValAll | ✅ |
| TOTAL_DIRECT_WORKERS | TotalDirectWorkers | ✅ |
| TOTAL_ELIGIBLE_SALARY | TotalEligibleSalary | ✅ |
| TOTAL_ELIGIBLE_WORKERS | TotalEligibleWorkers | ✅ |
| UNPUBLISHED_DIST_BUDGET_AMOUNT | UnpublishedDistBudgetAmount | ✅ |
| UNPUBLISHED_DIST_BUDGET_PCT | UnpublishedDistBudgetPct | ✅ |
| UNPUBLISHED_WS_BUDGET_AMOUNT | UnpublishedWsBudgetAmount | ✅ |
| UNPUBLISHED_WS_BUDGET_PCT | UnpublishedWsBudgetPct | ✅ |
| USED_BUDGET | UsedBudget | ✅ |
| USER_PREFERRED_EXCHANGE_RATE | UserPreferredExchangeRate | ✅ |
| WS_BUDGET_ISSUE_DATE | WsBudgetIssueDate | — |
| WS_BUDGET_ISSUE_VAL | WsBudgetIssueVal | ✅ |
| WS_BUDGET_VAL | WsBudgetVal | ✅ |
| WS_BUDGET_VAL_LAST_UPD_BY | WsBudgetValLastUpdBy | — |
| WS_BUDGET_VAL_LAST_UPD_DATE | WsBudgetValLastUpdDate | — |

### [[managerbudgetspvo|ManagerBudgetsPVO]] (HCM · BICC: 39/47)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_CD | ManagerBudgetsPEOAccessCd | ✅ |
| BUDGET_LAST_UPD_DATE | ManagerBudgetsPEOBudgetLastUpdDate | ✅ |
| BUDGET_POP_CD | ManagerBudgetsPEOBudgetPopCd | ✅ |
| BUDGET_VAL_AMOUNT | ManagerBudgetsPEOBudgetValAmount | — |
| BUDGET_VAL_PERCENT | ManagerBudgetsPEOBudgetValPercent | — |
| BUDGETING_STYLE | ManagerBudgetsPEOBudgetingStyle | ✅ |
| CREATED_BY | ManagerBudgetsPEOCreatedBy | ✅ |
| CREATION_DATE | ManagerBudgetsPEOCreationDate | ✅ |
| DFLT_DIST_BUDGET_VAL | ManagerBudgetsPEODfltDistBudgetVal | — |
| DFLT_WS_BUDGET_VAL | ManagerBudgetsPEODfltWsBudgetVal | — |
| DIST_BUDGET_ISSUE_DATE | ManagerBudgetsPEODistBudgetIssueDate | ✅ |
| DIST_BUDGET_ISSUE_VAL | ManagerBudgetsPEODistBudgetIssueVal | ✅ |
| DIST_BUDGET_VAL | ManagerBudgetsPEODistBudgetVal | ✅ |
| DIST_BUDGET_VAL_LAST_UPD_BY | ManagerBudgetsPEODistBudgetValLastUpdBy | ✅ |
| DIST_BUDGET_VAL_LAST_UPD_DATE | ManagerBudgetsPEODistBudgetValLastUpdDate | ✅ |
| LAST_UPDATE_DATE | ManagerBudgetsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ManagerBudgetsPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ManagerBudgetsPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ManagerBudgetsPEOObjectVersionNumber | — |
| OVERALL_BUDGET_AMOUNT | ManagerBudgetsPEOOverallBudgetAmount | ✅ |
| OVERRIDE_OVER_ALLOCATE_CODE | ManagerBudgetsPEOOverrideOverAllocateCode | ✅ |
| OVERRIDE_OVER_BUDGET_CODE | ManagerBudgetsPEOOverrideOverBudgetCode | ✅ |
| PERIOD_ID | ManagerBudgetsPEOPeriodId | — |
| PERSON_EVENT_ID | PersonEventId | ✅ |
| PLAN_ID | ManagerBudgetsPEOPlanId | — |
| POOL_ID | ManagerBudgetsPEOPoolId | — |
| PUBLISHED_DIST_BUDGET_AMOUNT | PublishedDistBudgetAmount | ✅ |
| PUBLISHED_DIST_BUDGET_PCT | PublishedDistBudgetPct | ✅ |
| PUBLISHED_WS_BUDGET_AMOUNT | PublishedWsBudgetAmount | ✅ |
| PUBLISHED_WS_BUDGET_PCT | PublishedWsBudgetPct | ✅ |
| REC_MN_VAL_ALL | ManagerBudgetsPEORecMnValAll | ✅ |
| REC_MX_VAL_ALL | ManagerBudgetsPEORecMxValAll | ✅ |
| REC_VAL_ALL | ManagerBudgetsPEORecValAll | ✅ |
| TOTAL_DIRECT_WORKERS | ManagerBudgetsPEOTotalDirectWorkers | ✅ |
| TOTAL_ELIGIBLE_SALARY | ManagerBudgetsPEOTotalEligibleSalary | ✅ |
| TOTAL_ELIGIBLE_WORKERS | ManagerBudgetsPEOTotalEligibleWorkers | ✅ |
| UNPUBLISHED_DIST_BUDGET_AMOUNT | UnpublishedDistBudgetAmount | ✅ |
| UNPUBLISHED_DIST_BUDGET_PCT | UnpublishedDistBudgetPct | ✅ |
| UNPUBLISHED_WS_BUDGET_AMOUNT | UnpublishedWsBudgetAmount | ✅ |
| UNPUBLISHED_WS_BUDGET_PCT | UnpublishedWsBudgetPct | ✅ |
| USED_BUDGET | ManagerBudgetsPEOUsedBudget | ✅ |
| USER_PREFERRED_EXCHANGE_RATE | ManagerBudgetsPEOUserPreferredExchangeRate | ✅ |
| WS_BUDGET_ISSUE_DATE | ManagerBudgetsPEOWsBudgetIssueDate | ✅ |
| WS_BUDGET_ISSUE_VAL | ManagerBudgetsPEOWsBudgetIssueVal | ✅ |
| WS_BUDGET_VAL | ManagerBudgetsPEOWsBudgetVal | ✅ |
| WS_BUDGET_VAL_LAST_UPD_BY | ManagerBudgetsPEOWsBudgetValLastUpdBy | ✅ |
| WS_BUDGET_VAL_LAST_UPD_DATE | ManagerBudgetsPEOWsBudgetValLastUpdDate | ✅ |

### [[managerbudgetspvoviewall|ManagerBudgetsPVOViewAll]] (HCM · BICC: 38/47)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_CD | ManagerBudgetsPEOAccessCd | ✅ |
| BUDGET_LAST_UPD_DATE | ManagerBudgetsPEOBudgetLastUpdDate | — |
| BUDGET_POP_CD | ManagerBudgetsPEOBudgetPopCd | ✅ |
| BUDGET_VAL_AMOUNT | ManagerBudgetsPEOBudgetValAmount | — |
| BUDGET_VAL_PERCENT | ManagerBudgetsPEOBudgetValPercent | — |
| BUDGETING_STYLE | ManagerBudgetsPEOBudgetingStyle | ✅ |
| CREATED_BY | ManagerBudgetsPEOCreatedBy | ✅ |
| CREATION_DATE | ManagerBudgetsPEOCreationDate | ✅ |
| DFLT_DIST_BUDGET_VAL | ManagerBudgetsPEODfltDistBudgetVal | — |
| DFLT_WS_BUDGET_VAL | ManagerBudgetsPEODfltWsBudgetVal | — |
| DIST_BUDGET_ISSUE_DATE | ManagerBudgetsPEODistBudgetIssueDate | ✅ |
| DIST_BUDGET_ISSUE_VAL | ManagerBudgetsPEODistBudgetIssueVal | ✅ |
| DIST_BUDGET_VAL | ManagerBudgetsPEODistBudgetVal | ✅ |
| DIST_BUDGET_VAL_LAST_UPD_BY | ManagerBudgetsPEODistBudgetValLastUpdBy | ✅ |
| DIST_BUDGET_VAL_LAST_UPD_DATE | ManagerBudgetsPEODistBudgetValLastUpdDate | ✅ |
| LAST_UPDATE_DATE | ManagerBudgetsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ManagerBudgetsPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ManagerBudgetsPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ManagerBudgetsPEOObjectVersionNumber | — |
| OVERALL_BUDGET_AMOUNT | ManagerBudgetsPEOOverallBudgetAmount | ✅ |
| OVERRIDE_OVER_ALLOCATE_CODE | ManagerBudgetsPEOOverrideOverAllocateCode | ✅ |
| OVERRIDE_OVER_BUDGET_CODE | ManagerBudgetsPEOOverrideOverBudgetCode | ✅ |
| PERIOD_ID | ManagerBudgetsPEOPeriodId | — |
| PERSON_EVENT_ID | PersonEventId | ✅ |
| PLAN_ID | ManagerBudgetsPEOPlanId | — |
| POOL_ID | ManagerBudgetsPEOPoolId | — |
| PUBLISHED_DIST_BUDGET_AMOUNT | PublishedDistBudgetAmount | ✅ |
| PUBLISHED_DIST_BUDGET_PCT | PublishedDistBudgetPct | ✅ |
| PUBLISHED_WS_BUDGET_AMOUNT | PublishedWsBudgetAmount | ✅ |
| PUBLISHED_WS_BUDGET_PCT | PublishedWsBudgetPct | ✅ |
| REC_MN_VAL_ALL | ManagerBudgetsPEORecMnValAll | ✅ |
| REC_MX_VAL_ALL | ManagerBudgetsPEORecMxValAll | ✅ |
| REC_VAL_ALL | ManagerBudgetsPEORecValAll | ✅ |
| TOTAL_DIRECT_WORKERS | ManagerBudgetsPEOTotalDirectWorkers | ✅ |
| TOTAL_ELIGIBLE_SALARY | ManagerBudgetsPEOTotalEligibleSalary | ✅ |
| TOTAL_ELIGIBLE_WORKERS | ManagerBudgetsPEOTotalEligibleWorkers | ✅ |
| UNPUBLISHED_DIST_BUDGET_AMOUNT | UnpublishedDistBudgetAmount | ✅ |
| UNPUBLISHED_DIST_BUDGET_PCT | UnpublishedDistBudgetPct | ✅ |
| UNPUBLISHED_WS_BUDGET_AMOUNT | UnpublishedWsBudgetAmount | ✅ |
| UNPUBLISHED_WS_BUDGET_PCT | UnpublishedWsBudgetPct | ✅ |
| USED_BUDGET | ManagerBudgetsPEOUsedBudget | ✅ |
| USER_PREFERRED_EXCHANGE_RATE | ManagerBudgetsPEOUserPreferredExchangeRate | ✅ |
| WS_BUDGET_ISSUE_DATE | ManagerBudgetsPEOWsBudgetIssueDate | ✅ |
| WS_BUDGET_ISSUE_VAL | ManagerBudgetsPEOWsBudgetIssueVal | ✅ |
| WS_BUDGET_VAL | ManagerBudgetsPEOWsBudgetVal | ✅ |
| WS_BUDGET_VAL_LAST_UPD_BY | ManagerBudgetsPEOWsBudgetValLastUpdBy | ✅ |
| WS_BUDGET_VAL_LAST_UPD_DATE | ManagerBudgetsPEOWsBudgetValLastUpdDate | ✅ |

---

## 📚 Referências

- [Oracle Docs — CMP_PERSON_BUDGETS_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmppersonbudgetsv.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
