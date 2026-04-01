---
id: DOC-HCM-065
doc_type: system-doc
title: "CMP_BUDGET_POOLS_B — Pools de Orçamento de Compensação (Base)"
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
  - budget-pools
  - orcamento
  - pools
aliases:
  - CMP_BUDGET_POOLS_B
  - cmp_budget_pools_b
  - pools-orcamento-compensacao
  - budget-pools
  - cmp-budget-pools
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_BUDGET_POOLS_B

## 📌 Visão Geral

Armazena os **pools de orçamento** (budget pools) do módulo Compensation. Cada pool representa um orçamento alocado para distribuição de compensação (salário, bônus, stock options, etc.) durante ciclos de revisão.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (dados técnicos) — a tabela de traduções correspondente (`_TL`) contém os textos traduzidos.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Orçamento de compensação:** Define o valor disponível para distribuição por gestor/departamento.
- **Ciclos de revisão salarial:** Base para alocação de budget em merit increases.
- **Controle de gastos:** Limita os valores que gestores podem distribuir.
- **Planejamento de compensação:** Suporte ao Compensation Workbench (CWB).

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BUDGET_POOL_ID | NUMBER(18) | NOT NULL | PK | Identificador único do pool | — | 🟢 90% |
| 2 | PLAN_ID | NUMBER(18) | NOT NULL | FK | Plano de compensação | — | 🟢 90% |
| 3 | BUDGET_POOL_CD | VARCHAR2(30) | NULL | Código | Código do pool | — | 🟡 80% |
| 4 | POOL_AMOUNT | NUMBER | NULL | Financeiro | Valor total do pool | — | 🟡 80% |
| 5 | POOL_PERCENT | NUMBER | NULL | Percentual | Percentual do pool (alternativa ao valor fixo) | — | 🟡 75% |
| 6 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Moeda do pool | — | 🟢 85% |
| 7 | POOL_STATUS | VARCHAR2(30) | NULL | Classificação | Status (ACTIVE, CLOSED, DRAFT) | — | 🟡 75% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada direta (tabela de configuração raiz).

### Tabelas-filha (FK de saída)
- [[cmp_budget_pools_tl]] — via `BUDGET_POOL_ID` (traducoes multilingue do registro)
- [[cmp_cwb_person_info]] — via `BUDGET_POOL_ID` (alocações por pessoa)

---

## 📎 Uso Típico

### Pools de orçamento ativos
```sql
SELECT bp.BUDGET_POOL_ID, bp.BUDGET_POOL_CD, bp.POOL_AMOUNT,
       bp.CURRENCY_CODE, bp.POOL_STATUS
FROM   CMP_BUDGET_POOLS_B bp
WHERE  bp.POOL_STATUS = 'ACTIVE';
```

### Filtros comuns
- `POOL_STATUS = 'ACTIVE'` — Pools ativos
- `CURRENCY_CODE = 'BRL'` — Pools em reais

---

## 🔒 Observações

- Tabela base (`_B`): dados técnicos; nomes traduzidos estão em `CMP_BUDGET_POOLS_TL`.
- O pool pode ser definido por valor fixo (`POOL_AMOUNT`) ou percentual (`POOL_PERCENT`).
- Usado no Compensation Workbench (CWB) para controle de orçamento por gestor.

---

## 🔗 PVOs Relacionados

### [[budgetpoolpvo|BudgetPoolPVO]] (HCM · BICC: 18/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_ISSUE_FLAG | BudgetPoolPEOAutoIssueFlag | ✅ |
| BUDGETING_STYLE | BudgetPoolPEOBudgetingStyle | ✅ |
| CREATED_BY | BudgetPoolPEOCreatedBy | ✅ |
| CREATION_DATE | BudgetPoolPEOCreationDate | ✅ |
| LAST_UPDATE_DATE | BudgetPoolPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BudgetPoolPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BudgetPoolPEOLastUpdatedBy | ✅ |
| NON_MONETARY_UOM | BudgetPoolPEONonMonetaryUom | ✅ |
| OBJECT_VERSION_NUMBER | BudgetPoolPEOObjectVersionNumber | ✅ |
| ORDER_NUM | BudgetPoolPEOOrderNum | ✅ |
| OVER_ALLOCATE_TOLERANCE | BudgetPoolPEOOverAllocateTolerance | ✅ |
| OVER_BUDGET_TOLERANCE | BudgetPoolPEOOverBudgetTolerance | ✅ |
| PLAN_ID | BudgetPoolPEOPlanId | ✅ |
| POOL_ID | PoolId | ✅ |
| PREVENT_OVER_ALLOCATE_FLAG | BudgetPoolPEOPreventOverAllocateFlag | ✅ |
| PREVENT_OVER_BUDGET_FLAG | BudgetPoolPEOPreventOverBudgetFlag | ✅ |
| PRIMARY_COMPONENT_ID | BudgetPoolPEOPrimaryComponentId | ✅ |
| SYSTEM_ORDER_NUM | BudgetPoolPEOSystemOrderNum | ✅ |

---

## 📚 Referências

- [Oracle Docs — CMP_BUDGET_POOLS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpbudgetpoolsb.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
