---
id: DOC-AP-035
doc_type: system-doc
title: "EXM_EXPENSE_REPORTS — Relatórios de Despesa (Cabeçalho)"
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
  - relatorios-despesa
  - expense-reports
  - reembolso
aliases:
  - EXM_EXPENSE_REPORTS
  - exm_expense_reports
  - relatorios-despesa-exm
  - exm-expense-reports
  - expense-report-headers
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# EXM_EXPENSE_REPORTS

## 📌 Visão Geral

Armazena os **cabeçalhos de relatórios de despesa** (Expense Reports) do módulo Expense Management. Cada registro representa um relatório submetido por um funcionário para reembolso de despesas corporativas, contendo informações gerais como data, propósito da viagem, status de aprovação, totais e referência ao funcionário solicitante.

> [!note] Ciclo de vida
> O relatório de despesa passa pelas fases: rascunho → submetido → em aprovação → aprovado → pago. O status é rastreado nesta tabela.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Solicitação de reembolso:** Agrupamento de despesas individuais em um relatório formal para aprovação.
- **Workflow de aprovação:** Controle do ciclo de aprovação hierárquica ou por políticas.
- **Geração de fatura de reembolso:** Após aprovação, o relatório gera uma fatura em [[ap_invoices_all]] para pagamento.
- **Controle de adiantamentos:** Vinculação a cash advances (adiantamentos) já concedidos ao funcionário.
- **Análise de gastos corporativos:** Base para dashboards de despesas por funcionário, departamento e período.
- **Compliance e auditoria:** Rastreamento de aprovações, políticas violadas e exceções.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | EXPENSE_REPORT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do relatório de despesa | — | 🟢 95% |
| 2 | EXPENSE_REPORT_NUM | VARCHAR2(50) | NOT NULL | Identificação | Número do relatório de despesa visível ao usuário | — | 🟢 95% |
| 3 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Funcionário que submeteu o relatório | [[per_person_names_f_v]] | 🟢 95% |
| 4 | EXPENSE_TEMPLATE_ID | NUMBER(18) | NULL | FK | Template de despesa utilizado | [[exm_expense_templates]] | 🟡 75% |
| 5 | PURPOSE | VARCHAR2(240) | NULL | Texto livre | Propósito/finalidade do relatório (ex: "Viagem São Paulo — reunião cliente") | — | 🟢 90% |
| 6 | EXPENSE_STATUS_CODE | VARCHAR2(30) | NOT NULL | Classificação | Status do relatório: SAVED, SUBMITTED, MGRPAYAPPR, INVOICED, PAID, etc. | — | 🟢 95% |
| 7 | APPROVAL_STATUS | VARCHAR2(30) | NULL | Classificação | Status de aprovação: APPROVED, REJECTED, PENDING, etc. | — | 🟢 85% |
| 8 | REPORT_SUBMIT_DATE | DATE | NULL | Data | Data de submissão do relatório | — | 🟢 90% |
| 9 | EXPENSE_REPORT_DATE | DATE | NOT NULL | Data | Data do relatório (informada pelo funcionário) | — | 🟢 90% |
| 10 | TOTAL | NUMBER | NULL | Financeiro | Valor total do relatório na moeda de reembolso | — | 🟢 95% |
| 11 | REIMBURSEMENT_CURRENCY_CODE | VARCHAR2(15) | NULL | Moeda | Moeda de reembolso | — | 🟢 90% |
| 12 | ACCTD_TOTAL | NUMBER | NULL | Financeiro | Valor total na moeda funcional | — | 🟡 75% |
| 13 | AMOUNT_DUE_EMPLOYEE | NUMBER | NULL | Financeiro | Valor devido ao funcionário (descontados adiantamentos) | — | 🟢 85% |
| 14 | AMOUNT_DUE_CCARD_COMPANY | NUMBER | NULL | Financeiro | Valor devido à empresa de cartão corporativo | — | 🟢 85% |
| 15 | ADVANCE_AMOUNT_APPLIED | NUMBER | NULL | Financeiro | Valor de adiantamento abatido | — | 🟡 80% |
| 16 | OVERRIDE_APPROVER_ID | NUMBER(18) | NULL | FK | Aprovador substituto designado | [[per_person_names_f_v]] | 🟡 75% |
| 17 | COST_CENTER | VARCHAR2(25) | NULL | Contabilidade | Centro de custo padrão do relatório | — | 🟡 80% |
| 18 | LOCATION_ID | NUMBER(18) | NULL | FK | Localização do funcionário | [[hr_locations]] | 🟡 75% |
| 19 | INVOICE_ID | NUMBER(18) | NULL | FK | Fatura de reembolso gerada | [[ap_invoices_all]] | 🟢 85% |
| 20 | POLICY_VIOLATION_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se houve violação de política (Y/N) | — | 🟡 75% |
| 21 | RECEIPTS_STATUS | VARCHAR2(30) | NULL | Classificação | Status de comprovantes: REQUIRED, RECEIVED, WAIVED | — | 🟡 70% |
| 22 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 95% |
| 23 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 24 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 25 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 26 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 27 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_person_names_f_v]] — via `PERSON_ID` (funcionário solicitante)
- [[exm_expense_templates]] — via `EXPENSE_TEMPLATE_ID` (template utilizado)
- [[hr_locations]] — via `LOCATION_ID` (localização do funcionário)
- [[ap_invoices_all]] — via `INVOICE_ID` (fatura de reembolso gerada)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do relatório de despesas)

### Tabelas-filha (FK de saída)
- [[exm_expenses]] — via `EXPENSE_REPORT_ID` (linhas de despesa do relatório)
- [[exm_expense_dists]] — via `EXPENSE_REPORT_ID` (distribuições contábeis)

---

## 📎 Uso Típico

### Relatórios de despesa por funcionário e status
```sql
SELECT er.EXPENSE_REPORT_NUM, er.PURPOSE, er.EXPENSE_REPORT_DATE,
       er.TOTAL, er.REIMBURSEMENT_CURRENCY_CODE,
       er.EXPENSE_STATUS_CODE
FROM   EXM_EXPENSE_REPORTS er
WHERE  er.PERSON_ID = :p_person_id
ORDER BY er.EXPENSE_REPORT_DATE DESC;
```

### Total de despesas aprovadas por período
```sql
SELECT SUM(er.TOTAL) AS total_aprovado,
       COUNT(*) AS qtd_relatorios
FROM   EXM_EXPENSE_REPORTS er
WHERE  er.EXPENSE_STATUS_CODE IN ('MGRPAYAPPR', 'INVOICED', 'PAID')
  AND  er.EXPENSE_REPORT_DATE BETWEEN :start_date AND :end_date
  AND  er.ORG_ID = :p_org_id;
```

### Relatórios com violação de política
```sql
SELECT er.EXPENSE_REPORT_NUM, er.PURPOSE, er.TOTAL,
       p.DISPLAY_NAME AS funcionario
FROM   EXM_EXPENSE_REPORTS er
JOIN   PER_PERSON_NAMES_F_V p ON p.PERSON_ID = er.PERSON_ID
WHERE  er.POLICY_VIOLATION_FLAG = 'Y'
  AND  er.ORG_ID = :p_org_id;
```

### Filtros comuns
- `EXPENSE_STATUS_CODE = 'SUBMITTED'` — Relatórios submetidos (pendentes de aprovação)
- `EXPENSE_STATUS_CODE = 'MGRPAYAPPR'` — Aprovados pelo gestor
- `EXPENSE_STATUS_CODE = 'PAID'` — Reembolsados
- `POLICY_VIOLATION_FLAG = 'Y'` — Com violação de política

---

## 🔒 Observações

- O ciclo de vida do relatório é: **SAVED** (rascunho) → **SUBMITTED** (submetido) → **MGRPAYAPPR** (aprovado) → **INVOICED** (fatura gerada) → **PAID** (pago).
- Quando aprovado, o sistema gera automaticamente uma fatura em [[ap_invoices_all]], cujo `INVOICE_ID` é gravado nesta tabela.
- O campo `AMOUNT_DUE_EMPLOYEE` desconta qualquer adiantamento (`ADVANCE_AMOUNT_APPLIED`) do total.
- `AMOUNT_DUE_CCARD_COMPANY` é usado quando a empresa paga diretamente à operadora de cartão corporativo.
- O `OVERRIDE_APPROVER_ID` permite designar um aprovador diferente do gestor hierárquico.

---

## 📚 Referências

- [Oracle Docs — EXM_EXPENSE_REPORTS](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/exmexpensereports.html)
- [[ap-module-data-dictionary]] — Dossiê do módulo AP
