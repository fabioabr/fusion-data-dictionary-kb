---
id: DOC-AP-033
doc_type: system-doc
title: "EXM_EXPENSES — Linhas de Despesa de Relatórios de Despesa"
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
  - despesas
  - expenses
  - expense-management
aliases:
  - EXM_EXPENSES
  - exm_expenses
  - linhas-despesa-exm
  - exm-expenses
  - expense-lines
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# EXM_EXPENSES

## 📌 Visão Geral

Armazena as **linhas individuais de despesa** dentro de relatórios de despesa (Expense Reports) no módulo de Expense Management do Oracle Fusion. Cada registro representa um item de gasto — viagem, hospedagem, alimentação, combustível, etc. — com valor, data, tipo de despesa, justificativa e referências a projeto/tarefa quando aplicável.

> [!note] Expense Management
> O módulo EXM (Expense Management) faz parte do Accounts Payable, gerenciando o ciclo de vida de despesas de funcionários: criação → aprovação → reembolso.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de despesas:** Detalhamento de cada item de gasto dentro de um relatório de despesa.
- **Categorização de gastos:** Classificação por tipo de despesa (viagem, alimentação, hospedagem, etc.).
- **Alocação a projetos:** Vinculação de despesas a projetos e tarefas para capitalização ou custeio.
- **Validação de políticas:** Verificação de limites por tipo de despesa e categoria.
- **Geração de fatura de reembolso:** Base para criação da invoice de reembolso em [[ap_invoices_all]].
- **Auditoria e compliance:** Rastreamento de recibos, justificativas e comprovantes por linha.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | EXPENSE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da linha de despesa | — | 🟢 95% |
| 2 | EXPENSE_REPORT_ID | NUMBER(18) | NOT NULL | FK | Relatório de despesa ao qual pertence | [[exm_expense_reports]] | 🟢 95% |
| 3 | EXPENSE_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo/categoria da despesa | [[exm_expense_types]] | 🟢 95% |
| 4 | EXPENSE_TEMPLATE_ID | NUMBER(18) | NULL | FK | Template de despesa utilizado | [[exm_expense_templates]] | 🟡 75% |
| 5 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição/justificativa da despesa | — | 🟢 90% |
| 6 | START_DATE | DATE | NOT NULL | Data | Data de início da despesa (ou data do gasto) | — | 🟢 95% |
| 7 | END_DATE | DATE | NULL | Data | Data de término (para despesas multi-dia como hospedagem) | — | 🟢 90% |
| 8 | RECEIPT_AMOUNT | NUMBER | NULL | Financeiro | Valor do recibo na moeda do recibo | — | 🟢 90% |
| 9 | RECEIPT_CURRENCY_CODE | VARCHAR2(15) | NULL | Moeda | Moeda do recibo | — | 🟢 90% |
| 10 | REIMBURSABLE_AMOUNT | NUMBER | NULL | Financeiro | Valor reembolsável na moeda de reembolso | — | 🟢 90% |
| 11 | REIMBURSEMENT_CURRENCY_CODE | VARCHAR2(15) | NULL | Moeda | Moeda de reembolso | — | 🟢 85% |
| 12 | EXCHANGE_RATE | NUMBER | NULL | Moeda | Taxa de câmbio do recibo para moeda de reembolso | — | 🟢 85% |
| 13 | LOCATION | VARCHAR2(240) | NULL | Localização | Local onde a despesa ocorreu (cidade, país) | — | 🟢 85% |
| 14 | MERCHANT_NAME | VARCHAR2(240) | NULL | Fornecedor | Nome do estabelecimento/fornecedor | — | 🟢 85% |
| 15 | RECEIPT_REQUIRED_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se comprovante é obrigatório (Y/N) | — | 🟡 80% |
| 16 | RECEIPT_MISSING_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se comprovante está ausente (Y/N) | — | 🟡 75% |
| 17 | JUSTIFICATION | VARCHAR2(2000) | NULL | Texto livre | Justificativa detalhada para a despesa | — | 🟡 75% |
| 18 | PROJECT_ID | NUMBER(18) | NULL | FK | Projeto associado à despesa | [[pjf_projects_all_b]] | 🟢 85% |
| 19 | TASK_ID | NUMBER(18) | NULL | FK | Tarefa do projeto | [[pjf_proj_elements_b]] | 🟢 85% |
| 20 | EXPENDITURE_TYPE_ID | NUMBER(18) | NULL | FK | Tipo de gasto para contabilidade de projetos | [[pjf_exp_types_tl]] | 🟡 75% |
| 21 | ITEMIZATION_PARENT_ID | NUMBER(18) | NULL | Referência | ID da despesa-pai (para linhas itemizadas/detalhadas) | — | 🟡 70% |
| 22 | NUMBER_OF_DAYS | NUMBER | NULL | Quantidade | Número de dias (para per diem) | — | 🟡 75% |
| 23 | DAILY_AMOUNT | NUMBER | NULL | Financeiro | Valor diário (per diem) | — | 🟡 75% |
| 24 | PERSONAL_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se a despesa é pessoal/não reembolsável (Y/N) | — | 🟡 70% |
| 25 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 95% |
| 26 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 27 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 28 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 29 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 30 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[exm_expense_reports]] — via `EXPENSE_REPORT_ID` (relatório de despesa)
- [[exm_expense_types]] — via `EXPENSE_TYPE_ID` (tipo de despesa)
- [[exm_expense_templates]] — via `EXPENSE_TEMPLATE_ID` (template utilizado)
- [[pjf_projects_all_b]] — via `PROJECT_ID` (projeto associado)
- [[pjf_proj_elements_b]] — via `TASK_ID` (tarefa do projeto)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da linha de despesa)

### Tabelas-filha (FK de saída)
- [[exm_expense_dists]] — via `EXPENSE_ID` (distribuições contábeis da despesa)

---

## 📎 Uso Típico

### Despesas de um relatório com tipo e valor
```sql
SELECT e.EXPENSE_ID, e.START_DATE, et.EXPENSE_TYPE_NAME,
       e.RECEIPT_AMOUNT, e.RECEIPT_CURRENCY_CODE,
       e.REIMBURSABLE_AMOUNT, e.MERCHANT_NAME
FROM   EXM_EXPENSES e
JOIN   EXM_EXPENSE_TYPES et ON et.EXPENSE_TYPE_ID = e.EXPENSE_TYPE_ID
WHERE  e.EXPENSE_REPORT_ID = :p_report_id
ORDER BY e.START_DATE;
```

### Total de despesas por tipo em um período
```sql
SELECT et.EXPENSE_TYPE_NAME,
       SUM(e.REIMBURSABLE_AMOUNT) AS total_reembolsavel,
       COUNT(*) AS qtd_itens
FROM   EXM_EXPENSES e
JOIN   EXM_EXPENSE_TYPES et ON et.EXPENSE_TYPE_ID = e.EXPENSE_TYPE_ID
WHERE  e.START_DATE BETWEEN :start_date AND :end_date
  AND  e.ORG_ID = :p_org_id
GROUP BY et.EXPENSE_TYPE_NAME
ORDER BY total_reembolsavel DESC;
```

### Filtros comuns
- `PERSONAL_FLAG = 'N'` — Despesas corporativas (reembolsáveis)
- `RECEIPT_MISSING_FLAG = 'Y'` — Despesas sem comprovante
- `PROJECT_ID IS NOT NULL` — Despesas alocadas a projetos

---

## 🔒 Observações

- Cada linha de despesa pode ser **itemizada** (detalhada em sub-linhas) usando `ITEMIZATION_PARENT_ID` para vincular sub-itens ao item principal.
- O campo `PERSONAL_FLAG = 'Y'` indica despesas pessoais incluídas no relatório para transparência, mas que **não serão reembolsadas**.
- `RECEIPT_AMOUNT` é na moeda do recibo (local), enquanto `REIMBURSABLE_AMOUNT` é na moeda de reembolso do funcionário.
- Despesas de **per diem** utilizam `NUMBER_OF_DAYS` × `DAILY_AMOUNT` para cálculo automático.
- A tabela [[exm_expense_dists]] contém as distribuições contábeis (rateio por CCID, projeto, etc.) para cada linha.

---

## 📚 Referências

- [Oracle Docs — EXM_EXPENSES](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/exmexpenses.html)
- [[ap-module-data-dictionary]] — Dossiê do módulo AP
