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

## 📚 Referências

- [Oracle Docs — CMP_PERSON_BUDGETS_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmppersonbudgetsv.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
