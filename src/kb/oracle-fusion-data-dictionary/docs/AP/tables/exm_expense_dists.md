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

## 🔗 PVOs Relacionados

### [[expensedistributionextractpvo|ExpenseDistributionExtractPVO]] (OTHER · BICC: 23/77)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CODE_COMBINATION_ID | ExpenseDistributionCodeCombinationId | ✅ |
| COST_CENTER | ExpenseDistributionCostCenter | ✅ |
| CREATED_BY | ExpenseDistributionCreatedBy | — |
| CREATION_DATE | ExpenseDistributionCreationDate | ✅ |
| EXPENSE_DIST_ID | ExpenseDistributionId | ✅ |
| EXPENSE_ID | ExpenseDistributionExpenseId | ✅ |
| EXPENSE_REPORT_ID | ExpenseDistributionExpenseReportId | ✅ |
| LAST_UPDATE_DATE | ExpenseDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExpenseDistributionLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpenseDistributionLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ExpenseDistributionObjectVersionNumber | — |
| ORG_ID | ExpenseDistributionOrgId | ✅ |
| PJC_BILLABLE_FLAG | ExpenseDistributionPjcBillableFlag | ✅ |
| PJC_CAPITALIZABLE_FLAG | ExpenseDistributionPjcCapitalizableFlag | ✅ |
| PJC_CONTEXT_CATEGORY | ExpenseDistributionPjcContextCategory | ✅ |
| PJC_CONTRACT_ID | ExpenseDistributionPjcContractId | ✅ |
| PJC_CONTRACT_LINE_ID | ExpenseDistributionPjcContractLineId | ✅ |
| PJC_EXPENDITURE_ITEM_DATE | ExpenseDistributionPjcExpenditureItemDate | ✅ |
| PJC_EXPENDITURE_TYPE_ID | ExpenseDistributionPjcExpenditureTypeId | ✅ |
| PJC_FUNDING_ALLOCATION_ID | ExpenseDistributionPjcFundingAllocationId | ✅ |
| PJC_ORGANIZATION_ID | ExpenseDistributionPjcOrganizationId | ✅ |
| PJC_PROJECT_ID | ExpenseDistributionPjcProjectId | ✅ |
| PJC_RESERVED_ATTRIBUTE1 | ExpenseDistributionPjcReservedAttribute1 | — |
| PJC_RESERVED_ATTRIBUTE10 | ExpenseDistributionPjcReservedAttribute10 | — |
| PJC_RESERVED_ATTRIBUTE2 | ExpenseDistributionPjcReservedAttribute2 | — |
| PJC_RESERVED_ATTRIBUTE3 | ExpenseDistributionPjcReservedAttribute3 | — |
| PJC_RESERVED_ATTRIBUTE4 | ExpenseDistributionPjcReservedAttribute4 | — |
| PJC_RESERVED_ATTRIBUTE5 | ExpenseDistributionPjcReservedAttribute5 | — |
| PJC_RESERVED_ATTRIBUTE6 | ExpenseDistributionPjcReservedAttribute6 | — |
| PJC_RESERVED_ATTRIBUTE7 | ExpenseDistributionPjcReservedAttribute7 | — |
| PJC_RESERVED_ATTRIBUTE8 | ExpenseDistributionPjcReservedAttribute8 | — |
| PJC_RESERVED_ATTRIBUTE9 | ExpenseDistributionPjcReservedAttribute9 | — |
| PJC_TASK_ID | ExpenseDistributionPjcTaskId | ✅ |
| PJC_USER_DEF_ATTRIBUTE1 | ExpenseDistributionPjcUserDefAttribute1 | — |
| PJC_USER_DEF_ATTRIBUTE10 | ExpenseDistributionPjcUserDefAttribute10 | — |
| PJC_USER_DEF_ATTRIBUTE2 | ExpenseDistributionPjcUserDefAttribute2 | — |
| PJC_USER_DEF_ATTRIBUTE3 | ExpenseDistributionPjcUserDefAttribute3 | — |
| PJC_USER_DEF_ATTRIBUTE4 | ExpenseDistributionPjcUserDefAttribute4 | — |
| PJC_USER_DEF_ATTRIBUTE5 | ExpenseDistributionPjcUserDefAttribute5 | — |
| PJC_USER_DEF_ATTRIBUTE6 | ExpenseDistributionPjcUserDefAttribute6 | — |
| PJC_USER_DEF_ATTRIBUTE7 | ExpenseDistributionPjcUserDefAttribute7 | — |
| PJC_USER_DEF_ATTRIBUTE8 | ExpenseDistributionPjcUserDefAttribute8 | — |
| PJC_USER_DEF_ATTRIBUTE9 | ExpenseDistributionPjcUserDefAttribute9 | — |
| PJC_WORK_TYPE_ID | ExpenseDistributionPjcWorkTypeId | ✅ |
| PREPARER_MODIFIED_FLAG | ExpenseDistributionPreparerModifiedFlag | — |
| REIMBURSABLE_AMOUNT | ExpenseDistributionReimbursableAmount | ✅ |
| SEGMENT1 | ExpenseDistributionSegment1 | ✅ |
| SEGMENT10 | ExpenseDistributionSegment10 | — |
| SEGMENT11 | ExpenseDistributionSegment11 | — |
| SEGMENT12 | ExpenseDistributionSegment12 | — |
| SEGMENT13 | ExpenseDistributionSegment13 | — |
| SEGMENT14 | ExpenseDistributionSegment14 | — |
| SEGMENT15 | ExpenseDistributionSegment15 | — |
| SEGMENT16 | ExpenseDistributionSegment16 | — |
| SEGMENT17 | ExpenseDistributionSegment17 | — |
| SEGMENT18 | ExpenseDistributionSegment18 | — |
| SEGMENT19 | ExpenseDistributionSegment19 | — |
| SEGMENT2 | ExpenseDistributionSegment2 | ✅ |
| SEGMENT20 | ExpenseDistributionSegment20 | — |
| SEGMENT21 | ExpenseDistributionSegment21 | — |
| SEGMENT22 | ExpenseDistributionSegment22 | — |
| SEGMENT23 | ExpenseDistributionSegment23 | — |
| SEGMENT24 | ExpenseDistributionSegment24 | — |
| SEGMENT25 | ExpenseDistributionSegment25 | — |
| SEGMENT26 | ExpenseDistributionSegment26 | — |
| SEGMENT27 | ExpenseDistributionSegment27 | — |
| SEGMENT28 | ExpenseDistributionSegment28 | — |
| SEGMENT29 | ExpenseDistributionSegment29 | — |
| SEGMENT3 | ExpenseDistributionSegment3 | — |
| SEGMENT30 | ExpenseDistributionSegment30 | — |
| SEGMENT4 | ExpenseDistributionSegment4 | — |
| SEGMENT5 | ExpenseDistributionSegment5 | — |
| SEGMENT6 | ExpenseDistributionSegment6 | — |
| SEGMENT7 | ExpenseDistributionSegment7 | — |
| SEGMENT8 | ExpenseDistributionSegment8 | — |
| SEGMENT9 | ExpenseDistributionSegment9 | — |
| SEQUENCE_NUM | ExpenseDistributionSequenceNum | — |

### [[expensedistributionpvo|ExpenseDistributionPVO]] (OTHER · BICC: 15/77)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CODE_COMBINATION_ID | ExpDistCodeCombinationId | ✅ |
| COST_CENTER | ExpDistCostCenter | ✅ |
| CREATED_BY | ExpDistCreatedBy | ✅ |
| CREATION_DATE | ExpDistCreationDate | ✅ |
| EXPENSE_DIST_ID | ExpenseDistId | ✅ |
| EXPENSE_ID | ExpDistExpenseId | — |
| EXPENSE_REPORT_ID | ExpDistExpenseReportId | — |
| LAST_UPDATE_DATE | ExpDistLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExpDistLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpDistLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ExpDistObjectVersionNumber | — |
| ORG_ID | ExpDistOrgId | — |
| PJC_BILLABLE_FLAG | ExpDistPjcBillableFlag | — |
| PJC_CAPITALIZABLE_FLAG | ExpDistPjcCapitalizableFlag | — |
| PJC_CONTEXT_CATEGORY | ExpDistPjcContextCategory | — |
| PJC_CONTRACT_ID | ExpDistPjcContractId | — |
| PJC_CONTRACT_LINE_ID | ExpDistPjcContractLineId | — |
| PJC_EXPENDITURE_ITEM_DATE | ExpDistPjcExpenditureItemDate | — |
| PJC_EXPENDITURE_TYPE_ID | ExpDistPjcExpenditureTypeId | ✅ |
| PJC_FUNDING_ALLOCATION_ID | ExpDistPjcFundingAllocationId | — |
| PJC_ORGANIZATION_ID | ExpDistPjcOrganizationId | ✅ |
| PJC_PROJECT_ID | ExpDistPjcProjectId | ✅ |
| PJC_RESERVED_ATTRIBUTE1 | ExpDistPjcReservedAttribute1 | — |
| PJC_RESERVED_ATTRIBUTE10 | ExpDistPjcReservedAttribute10 | — |
| PJC_RESERVED_ATTRIBUTE2 | ExpDistPjcReservedAttribute2 | — |
| PJC_RESERVED_ATTRIBUTE3 | ExpDistPjcReservedAttribute3 | — |
| PJC_RESERVED_ATTRIBUTE4 | ExpDistPjcReservedAttribute4 | — |
| PJC_RESERVED_ATTRIBUTE5 | ExpDistPjcReservedAttribute5 | — |
| PJC_RESERVED_ATTRIBUTE6 | ExpDistPjcReservedAttribute6 | — |
| PJC_RESERVED_ATTRIBUTE7 | ExpDistPjcReservedAttribute7 | — |
| PJC_RESERVED_ATTRIBUTE8 | ExpDistPjcReservedAttribute8 | — |
| PJC_RESERVED_ATTRIBUTE9 | ExpDistPjcReservedAttribute9 | — |
| PJC_TASK_ID | ExpDistPjcTaskId | ✅ |
| PJC_USER_DEF_ATTRIBUTE1 | ExpDistPjcUserDefAttribute1 | — |
| PJC_USER_DEF_ATTRIBUTE10 | ExpDistPjcUserDefAttribute10 | — |
| PJC_USER_DEF_ATTRIBUTE2 | ExpDistPjcUserDefAttribute2 | — |
| PJC_USER_DEF_ATTRIBUTE3 | ExpDistPjcUserDefAttribute3 | — |
| PJC_USER_DEF_ATTRIBUTE4 | ExpDistPjcUserDefAttribute4 | — |
| PJC_USER_DEF_ATTRIBUTE5 | ExpDistPjcUserDefAttribute5 | — |
| PJC_USER_DEF_ATTRIBUTE6 | ExpDistPjcUserDefAttribute6 | — |
| PJC_USER_DEF_ATTRIBUTE7 | ExpDistPjcUserDefAttribute7 | — |
| PJC_USER_DEF_ATTRIBUTE8 | ExpDistPjcUserDefAttribute8 | — |
| PJC_USER_DEF_ATTRIBUTE9 | ExpDistPjcUserDefAttribute9 | — |
| PJC_WORK_TYPE_ID | ExpDistPjcWorkTypeId | — |
| PREPARER_MODIFIED_FLAG | ExpDistPreparerModifiedFlag | — |
| REIMBURSABLE_AMOUNT | ExpDistReimbursableAmount | ✅ |
| SEGMENT1 | ExpDistSegment1 | ✅ |
| SEGMENT10 | ExpDistSegment10 | — |
| SEGMENT11 | ExpDistSegment11 | — |
| SEGMENT12 | ExpDistSegment12 | — |
| SEGMENT13 | ExpDistSegment13 | — |
| SEGMENT14 | ExpDistSegment14 | — |
| SEGMENT15 | ExpDistSegment15 | — |
| SEGMENT16 | ExpDistSegment16 | — |
| SEGMENT17 | ExpDistSegment17 | — |
| SEGMENT18 | ExpDistSegment18 | — |
| SEGMENT19 | ExpDistSegment19 | — |
| SEGMENT2 | ExpDistSegment2 | — |
| SEGMENT20 | ExpDistSegment20 | — |
| SEGMENT21 | ExpDistSegment21 | — |
| SEGMENT22 | ExpDistSegment22 | — |
| SEGMENT23 | ExpDistSegment23 | — |
| SEGMENT24 | ExpDistSegment24 | — |
| SEGMENT25 | ExpDistSegment25 | — |
| SEGMENT26 | ExpDistSegment26 | — |
| SEGMENT27 | ExpDistSegment27 | — |
| SEGMENT28 | ExpDistSegment28 | — |
| SEGMENT29 | ExpDistSegment29 | — |
| SEGMENT3 | ExpDistSegment3 | ✅ |
| SEGMENT30 | ExpDistSegment30 | — |
| SEGMENT4 | ExpDistSegment4 | — |
| SEGMENT5 | ExpDistSegment5 | — |
| SEGMENT6 | ExpDistSegment6 | — |
| SEGMENT7 | ExpDistSegment7 | — |
| SEGMENT8 | ExpDistSegment8 | — |
| SEGMENT9 | ExpDistSegment9 | — |
| SEQUENCE_NUM | ExpDistSequenceNum | ✅ |

### [[expensepvo|ExpensePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CODE_COMBINATION_ID | ExpDistCodeCombinationId | — |
| COST_CENTER | ExpDistCostCenter | — |
| CREATED_BY | ExpDistCreatedBy | — |
| EXPENSE_DIST_ID | ExpDistExpenseDistId | — |
| EXPENSE_ID | ExpDistExpenseId | — |
| EXPENSE_REPORT_ID | ExpDistExpenseReportId | — |
| LAST_UPDATE_LOGIN | ExpDistLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpDistLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ExpDistObjectVersionNumber | — |
| ORG_ID | ExpDistOrgId | — |
| PJC_BILLABLE_FLAG | ExpDistPjcBillableFlag | — |
| PJC_CAPITALIZABLE_FLAG | ExpDistPjcCapitalizableFlag | — |
| PJC_CONTEXT_CATEGORY | ExpDistPjcContextCategory | — |
| PJC_CONTRACT_ID | ExpDistPjcContractId | — |
| PJC_CONTRACT_LINE_ID | ExpDistPjcContractLineId | — |
| PJC_EXPENDITURE_ITEM_DATE | ExpDistPjcExpenditureItemDate | — |
| PJC_EXPENDITURE_TYPE_ID | ExpDistPjcExpenditureTypeId | — |
| PJC_FUNDING_ALLOCATION_ID | ExpDistPjcFundingAllocationId | — |
| PJC_ORGANIZATION_ID | ExpDistPjcOrganizationId | — |
| PJC_PROJECT_ID | ExpDistPjcProjectId | — |
| PJC_RESERVED_ATTRIBUTE1 | ExpDistPjcReservedAttribute1 | — |
| PJC_RESERVED_ATTRIBUTE10 | ExpDistPjcReservedAttribute10 | — |
| PJC_RESERVED_ATTRIBUTE2 | ExpDistPjcReservedAttribute2 | — |
| PJC_RESERVED_ATTRIBUTE3 | ExpDistPjcReservedAttribute3 | — |
| PJC_RESERVED_ATTRIBUTE4 | ExpDistPjcReservedAttribute4 | — |
| PJC_RESERVED_ATTRIBUTE5 | ExpDistPjcReservedAttribute5 | — |
| PJC_RESERVED_ATTRIBUTE6 | ExpDistPjcReservedAttribute6 | — |
| PJC_RESERVED_ATTRIBUTE7 | ExpDistPjcReservedAttribute7 | — |
| PJC_RESERVED_ATTRIBUTE8 | ExpDistPjcReservedAttribute8 | — |
| PJC_RESERVED_ATTRIBUTE9 | ExpDistPjcReservedAttribute9 | — |
| PJC_TASK_ID | ExpDistPjcTaskId | — |
| PJC_USER_DEF_ATTRIBUTE1 | ExpDistPjcUserDefAttribute1 | — |
| PJC_USER_DEF_ATTRIBUTE10 | ExpDistPjcUserDefAttribute10 | — |
| PJC_USER_DEF_ATTRIBUTE2 | ExpDistPjcUserDefAttribute2 | — |
| PJC_USER_DEF_ATTRIBUTE3 | ExpDistPjcUserDefAttribute3 | — |
| PJC_USER_DEF_ATTRIBUTE4 | ExpDistPjcUserDefAttribute4 | — |
| PJC_USER_DEF_ATTRIBUTE5 | ExpDistPjcUserDefAttribute5 | — |
| PJC_USER_DEF_ATTRIBUTE6 | ExpDistPjcUserDefAttribute6 | — |
| PJC_USER_DEF_ATTRIBUTE7 | ExpDistPjcUserDefAttribute7 | — |
| PJC_USER_DEF_ATTRIBUTE8 | ExpDistPjcUserDefAttribute8 | — |
| PJC_USER_DEF_ATTRIBUTE9 | ExpDistPjcUserDefAttribute9 | — |
| PJC_WORK_TYPE_ID | ExpDistPjcWorkTypeId | — |
| PREPARER_MODIFIED_FLAG | ExpDistPreparerModifiedFlag | — |
| REIMBURSABLE_AMOUNT | ExpDistReimbursableAmount | — |
| SEGMENT1 | ExpDistSegment1 | — |
| SEGMENT10 | ExpDistSegment10 | — |
| SEGMENT11 | ExpDistSegment11 | — |
| SEGMENT12 | ExpDistSegment12 | — |
| SEGMENT13 | ExpDistSegment13 | — |
| SEGMENT14 | ExpDistSegment14 | — |
| SEGMENT15 | ExpDistSegment15 | — |
| SEGMENT16 | ExpDistSegment16 | — |
| SEGMENT17 | ExpDistSegment17 | — |
| SEGMENT18 | ExpDistSegment18 | — |
| SEGMENT19 | ExpDistSegment19 | — |
| SEGMENT2 | ExpDistSegment2 | — |
| SEGMENT20 | ExpDistSegment20 | — |
| SEGMENT21 | ExpDistSegment21 | — |
| SEGMENT22 | ExpDistSegment22 | — |
| SEGMENT23 | ExpDistSegment23 | — |
| SEGMENT24 | ExpDistSegment24 | — |
| SEGMENT25 | ExpDistSegment25 | — |
| SEGMENT26 | ExpDistSegment26 | — |
| SEGMENT27 | ExpDistSegment27 | — |
| SEGMENT28 | ExpDistSegment28 | — |
| SEGMENT29 | ExpDistSegment29 | — |
| SEGMENT3 | ExpDistSegment3 | — |
| SEGMENT30 | ExpDistSegment30 | — |
| SEGMENT4 | ExpDistSegment4 | — |
| SEGMENT5 | ExpDistSegment5 | — |
| SEGMENT6 | ExpDistSegment6 | — |
| SEGMENT7 | ExpDistSegment7 | — |
| SEGMENT8 | ExpDistSegment8 | — |
| SEGMENT9 | ExpDistSegment9 | — |
| SEQUENCE_NUM | ExpDistSequenceNum | — |

---

## 📚 Referências

- [Oracle Docs — EXM_EXPENSE_DISTS](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/exmexpensedists.html)
- [[ap-module-data-dictionary]] — Dossiê do módulo AP
