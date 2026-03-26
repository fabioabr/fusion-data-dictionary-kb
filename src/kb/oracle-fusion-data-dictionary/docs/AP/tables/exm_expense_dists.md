---
id: DOC-AP-034
doc_type: system-doc
title: "EXM_EXPENSE_DISTS — Distribuições Contábeis de Despesas"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - accounts-payable
  - data-dictionary
  - distribuicoes
  - expense-distributions
  - contabilidade
aliases:
  - EXM_EXPENSE_DISTS
  - exm_expense_dists
  - distribuicoes-despesa-exm
  - exm-expense-distributions
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# EXM_EXPENSE_DISTS

## 📌 Visão Geral

Armazena as **distribuições contábeis** das linhas de despesa do módulo Expense Management. Cada registro representa a alocação de uma linha de despesa a uma combinação de contas contábeis (CCID), projeto, tarefa e/ou centro de custo. Permite rateio de uma única despesa em múltiplas contas ou projetos.

> [!note] Distribuições
> Similar ao padrão `AP_INVOICE_DISTRIBUTIONS_ALL` para faturas, esta tabela detalha o "para onde vai" contabilmente cada linha de despesa.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Contabilização de despesas:** Alocação de valores a contas contábeis específicas no GL.
- **Rateio por centro de custo:** Distribuição de uma despesa entre múltiplos departamentos.
- **Alocação a projetos:** Distribuição de despesas a projetos e tarefas para capitalização ou custeio.
- **Geração de invoice de reembolso:** Base para criação das distribuições da fatura em [[ap_invoice_distributions_all]].
- **Reconciliação contábil:** Rastreamento da conta debitada para cada item de despesa.
- **Reporting fiscal:** Suporte a relatórios de gastos por conta, departamento e projeto.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | EXPENSE_DIST_ID | NUMBER(18) | NOT NULL | PK | Identificador único da distribuição | — | 🟢 95% |
| 2 | EXPENSE_ID | NUMBER(18) | NOT NULL | FK | Linha de despesa de origem | [[exm_expenses]] | 🟢 95% |
| 3 | EXPENSE_REPORT_ID | NUMBER(18) | NOT NULL | FK | Relatório de despesa | [[exm_expense_reports]] | 🟢 90% |
| 4 | LINE_NUMBER | NUMBER | NULL | Identificação | Número sequencial da distribuição dentro da despesa | — | 🟡 80% |
| 5 | CODE_COMBINATION_ID | NUMBER(18) | NULL | Contabilidade | Combinação de contas contábeis (CCID) — conta de débito | [[gl_code_combinations]] | 🟢 90% |
| 6 | AMOUNT | NUMBER | NOT NULL | Financeiro | Valor da distribuição na moeda de reembolso | — | 🟢 95% |
| 7 | ACCTD_AMOUNT | NUMBER | NULL | Financeiro | Valor na moeda funcional (ledger currency) | — | 🟡 80% |
| 8 | DIST_PERCENT | NUMBER | NULL | Rateio | Percentual de distribuição da linha | — | 🟡 75% |
| 9 | PROJECT_ID | NUMBER(18) | NULL | FK | Projeto associado à distribuição | [[pjf_projects_all_b]] | 🟢 85% |
| 10 | TASK_ID | NUMBER(18) | NULL | FK | Tarefa do projeto | [[pjf_proj_elements_b]] | 🟢 85% |
| 11 | EXPENDITURE_TYPE_ID | NUMBER(18) | NULL | FK | Tipo de gasto para contabilidade de projetos | [[pjf_exp_types_tl]] | 🟡 75% |
| 12 | EXPENDITURE_ORGANIZATION_ID | NUMBER(18) | NULL | FK | Organização de gasto (para costing) | [[hr_all_organization_units_f]] | 🟡 75% |
| 13 | EXPENDITURE_ITEM_DATE | DATE | NULL | Data | Data do item de gasto (para contabilidade de projetos) | — | 🟡 75% |
| 14 | COST_CENTER | VARCHAR2(25) | NULL | Contabilidade | Segmento de centro de custo | — | 🟡 70% |
| 15 | AWARD_ID | NUMBER(18) | NULL | FK | Identificador de grant/award (se aplicável) | — | 🟡 60% |
| 16 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 95% |
| 17 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 18 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 19 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 20 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 21 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[exm_expenses]] — via `EXPENSE_ID` (linha de despesa de origem)
- [[exm_expense_reports]] — via `EXPENSE_REPORT_ID` (relatório de despesa)
- [[gl_code_combinations]] — via `CODE_COMBINATION_ID` (conta contábil da distribuição de despesa)
- [[pjf_projects_all_b]] — via `PROJECT_ID` (projeto ao qual a despesa é imputada)
- [[pjf_proj_elements_b]] — via `TASK_ID` (tarefa do projeto)
- [[hr_all_organization_units_f]] — via `ORG_ID`, `EXPENDITURE_ORGANIZATION_ID` (business unit, organização de gasto)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha direta identificada — tabela de detalhe terminal.

---

## 📎 Uso Típico

### Distribuições contábeis de um relatório de despesa
```sql
SELECT ed.EXPENSE_DIST_ID, e.DESCRIPTION,
       ed.CODE_COMBINATION_ID, ed.AMOUNT, ed.DIST_PERCENT
FROM   EXM_EXPENSE_DISTS ed
JOIN   EXM_EXPENSES e ON e.EXPENSE_ID = ed.EXPENSE_ID
WHERE  ed.EXPENSE_REPORT_ID = :p_report_id
ORDER BY ed.EXPENSE_ID, ed.LINE_NUMBER;
```

### Total distribuído por conta contábil
```sql
SELECT gcc.CONCATENATED_SEGMENTS, SUM(ed.AMOUNT) AS total_dist
FROM   EXM_EXPENSE_DISTS ed
JOIN   GL_CODE_COMBINATIONS gcc ON gcc.CODE_COMBINATION_ID = ed.CODE_COMBINATION_ID
WHERE  ed.ORG_ID = :p_org_id
GROUP BY gcc.CONCATENATED_SEGMENTS
ORDER BY total_dist DESC;
```

### Filtros comuns
- `PROJECT_ID IS NOT NULL` — Distribuições alocadas a projetos
- `DIST_PERCENT = 100` — Distribuições sem rateio (100% para uma conta)

---

## 🔒 Observações

- Uma linha de despesa (`EXM_EXPENSES`) pode ter **múltiplas distribuições** quando há rateio entre centros de custo, projetos ou contas contábeis.
- A soma de `AMOUNT` de todas as distribuições de uma despesa deve ser igual ao `REIMBURSABLE_AMOUNT` da linha correspondente em [[exm_expenses]].
- Quando a despesa é associada a um projeto, os campos `PROJECT_ID`, `TASK_ID`, `EXPENDITURE_TYPE_ID` e `EXPENDITURE_ITEM_DATE` são obrigatórios para integração com o módulo Projects.
- O `CODE_COMBINATION_ID` é geralmente derivado automaticamente do tipo de despesa e das regras de account derivation da organização.

---

## 📚 Referências

- [Oracle Docs — EXM_EXPENSE_DISTS](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/exmexpensedists.html)
- [[ap-module-data-dictionary]] — Dossiê do módulo AP
