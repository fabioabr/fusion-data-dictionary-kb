---
id: DOC-HCM-077
doc_type: system-doc
title: "CMP_CWB_PLAN_DEFINITIONS — Definições de Planos do Compensation Workbench"
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
  - cwb
  - plano-compensacao
  - salary-planning
aliases:
  - CMP_CWB_PLAN_DEFINITIONS
  - cmp_cwb_plan_definitions
  - cmp-cwb-plan-definitions
  - DOC-HCM-077
  - definições-de-planos-do-compensation-workbench
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_CWB_PLAN_DEFINITIONS

## 📌 Visão Geral

Armazena as **definições de planos do Compensation Workbench** (CWB). Cada registro define um plano de compensação com parâmetros de elegibilidade, período de vigência, orçamento e regras de alocação para ciclos de revisão salarial, bônus ou promoções.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuração de ciclos de compensação:** Definição dos parâmetros do plano CWB.
- **Controle de elegibilidade:** Regras que determinam quais colaboradores participam.
- **Gestão orçamentária:** Orçamento total alocado ao plano de compensação.
- **Workflow de aprovação:** Parâmetros de fluxo de aprovação do plano.
- **Integração com folha:** Configuração de como as decisões fluem para payroll.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PLAN_ID | NUMBER(18) | NOT NULL | PK | Identificador único do plano CWB | — | 🟢 95% |
| 2 | PLAN_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do plano CWB | — | 🟢 90% |
| 3 | PLAN_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do plano (SALARY, BONUS, STOCK) | — | 🟡 80% |
| 4 | STATUS | VARCHAR2(30) | NULL | Status | Status do plano (OPEN, CLOSED, PENDING) | — | 🟡 75% |
| 5 | PERIOD_START_DATE | DATE | NULL | Data | Data de início do período do plano | — | 🟡 80% |
| 6 | PERIOD_END_DATE | DATE | NULL | Data | Data de término do período do plano | — | 🟡 80% |
| 7 | BUDGET_POOL_AMOUNT | NUMBER | NULL | Financeiro | Valor total do pool orçamentário | — | 🟡 70% |
| 8 | CURRENCY_CODE | VARCHAR2(30) | NULL | Referência | Moeda do orçamento | — | 🟢 90% |
| 9 | BUSINESS_GROUP_ID | NUMBER(18) | NULL | FK | Grupo de negócios | [[per_business_groups]] | 🟡 75% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_business_groups]] — via `BUSINESS_GROUP_ID` (grupo de negócios)

### Tabelas-filha (FK de saída)
- [[cmp_cwb_person_rates]] — via `PLAN_ID` (taxas individuais)
- [[cmp_cwb_promotions]] — via `PLAN_ID` (promocoes do plano de compensacao CWB)

---

## 📎 Uso Típico

### Planos CWB ativos
```sql
SELECT pd.PLAN_ID, pd.PLAN_NAME, pd.PLAN_TYPE, pd.STATUS,
       pd.PERIOD_START_DATE, pd.PERIOD_END_DATE
FROM   CMP_CWB_PLAN_DEFINITIONS pd
WHERE  pd.STATUS = 'OPEN';
```

### Orçamento total por plano
```sql
SELECT pd.PLAN_NAME, pd.BUDGET_POOL_AMOUNT, pd.CURRENCY_CODE
FROM   CMP_CWB_PLAN_DEFINITIONS pd
WHERE  pd.PERIOD_START_DATE >= :p_start_date
ORDER BY pd.BUDGET_POOL_AMOUNT DESC;
```

---

## 🔒 Observações

- O `PLAN_TYPE` categoriza o plano — SALARY (revisão salarial), BONUS (bonificação) ou STOCK (ações).
- O `STATUS` controla o ciclo de vida: OPEN (em andamento), CLOSED (encerrado), PENDING (pendente).
- O `BUDGET_POOL_AMOUNT` define o teto de gastos para o ciclo.
- Planos CWB são a estrutura principal que agrega todas as decisões de compensação de um ciclo.

---

## 📚 Referências

- [Oracle Docs — CMP_CWB_PLAN_DEFINITIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpcwbplandefinitions.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
