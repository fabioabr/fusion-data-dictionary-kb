---
id: DOC-AP-014
doc_type: system-doc
title: "AP_INVOICE_PAYMENTS_ALL — Pagamentos de Faturas"
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
  - pagamentos
  - invoice-payments
  - ap-payments
aliases:
  - AP_INVOICE_PAYMENTS_ALL
  - ap_invoice_payments_all
  - pagamentos-faturas-ap
  - invoice-payments-ap
  - pagamentos-ap
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_INVOICE_PAYMENTS_ALL

## 📌 Visão Geral

Armazena a relação entre **faturas e pagamentos** no módulo Accounts Payable. Cada registro representa a aplicação de um pagamento (check) a uma fatura específica, contendo o valor pago, desconto obtido, data e referência ao check ID. Uma fatura pode ter múltiplos pagamentos (pagamento parcial), e um check pode pagar múltiplas faturas.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de pagamentos:** Vincula cada pagamento emitido à fatura correspondente.
- **Pagamentos parciais:** Permite rastrear múltiplos pagamentos contra uma mesma fatura.
- **Descontos financeiros:** Registra descontos obtidos por pagamento antecipado.
- **Conciliação bancária:** Base para reconciliação de pagamentos com extratos bancários.
- **Auditoria de pagamentos:** Rastreabilidade completa de cada pagamento aplicado a faturas.
- **Relatórios de aging:** Suporte à análise de faturas pagas vs. pendentes.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INVOICE_PAYMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do pagamento da fatura | — | 🟢 100% |
| 2 | INVOICE_ID | NUMBER(18) | NOT NULL | FK | Fatura paga | [[ap_invoices_all]] | 🟢 100% |
| 3 | CHECK_ID | NUMBER(18) | NOT NULL | FK | Identificador do check/pagamento | [[ap_checks_all]] | 🟢 100% |
| 4 | PAYMENT_NUM | NUMBER | NOT NULL | Identificação | Número da parcela paga (payment schedule) | — | 🟢 100% |
| 5 | AMOUNT | NUMBER | NOT NULL | Financeiro | Valor pago na moeda da transação | — | 🟢 100% |
| 6 | PAYMENT_BASE_AMOUNT | NUMBER | NULL | Financeiro | Valor pago na moeda funcional (ledger) | — | 🟢 100% |
| 7 | DISCOUNT_TAKEN | NUMBER | NULL | Financeiro | Desconto financeiro obtido | — | 🟢 100% |
| 8 | DISCOUNT_LOST | NUMBER | NULL | Financeiro | Desconto financeiro perdido (fora do prazo) | — | 🟢 100% |
| 9 | EXCHANGE_RATE_TYPE | VARCHAR2(30) | NULL | Financeiro | Tipo de taxa de câmbio do pagamento | [[gl_daily_conversion_types]] | 🟢 100% |
| 10 | EXCHANGE_RATE | NUMBER | NULL | Financeiro | Taxa de câmbio aplicada no pagamento | — | 🟢 100% |
| 11 | EXCHANGE_DATE | DATE | NULL | Financeiro | Data da taxa de câmbio | — | 🟢 100% |
| 12 | ACCOUNTING_DATE | DATE | NOT NULL | Contabilidade | Data contábil do pagamento | — | 🟢 100% |
| 13 | PERIOD_NAME | VARCHAR2(15) | NULL | Contabilidade | Nome do período contábil | [[gl_period_statuses]] | 🟢 100% |
| 14 | ACCTS_PAY_CODE_COMBINATION_ID | NUMBER(18) | NULL | Contabilidade | Conta contábil de AP (liability) | [[gl_code_combinations]] | 🟢 100% |
| 15 | POSTED_FLAG | VARCHAR2(1) | NULL | Contabilidade | Indica se foi contabilizado no GL (Y/N) | — | 🟢 100% |
| 16 | ACCRUAL_POSTED_FLAG | VARCHAR2(1) | NULL | Contabilidade | Indica se accrual foi lançado (Y/N) | — | 🟢 100% |
| 17 | CASH_POSTED_FLAG | VARCHAR2(1) | NULL | Contabilidade | Indica se cash basis foi lançado (Y/N) | — | 🟢 100% |
| 18 | REVERSAL_FLAG | VARCHAR2(1) | NULL | Status | Indica se é reversão de pagamento (Y/N) | — | 🟢 100% |
| 19 | REVERSAL_INV_PMT_ID | NUMBER(18) | NULL | Referência cruzada | ID do pagamento original revertido | [[ap_invoice_payments_all]] | 🟢 100% |
| 20 | SET_OF_BOOKS_ID | NUMBER(18) | NULL | Contabilidade | Ledger (set of books) | [[gl_ledgers]] | 🟢 100% |
| 21 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 22 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 23 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 24 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 25 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 26 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 27 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 28 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ap_invoices_all]] — via `INVOICE_ID` (fatura liquidada pelo pagamento)
- [[ap_checks_all]] — via `CHECK_ID` (check/pagamento emitido)
- [[gl_code_combinations]] — via `ACCTS_PAY_CODE_COMBINATION_ID` (conta contábil de contas a pagar do pagamento)
- [[gl_daily_conversion_types]] — via `EXCHANGE_RATE_TYPE` (tipo de taxa de câmbio aplicada no pagamento)
- [[gl_ledgers]] — via `SET_OF_BOOKS_ID` (ledger contábil do pagamento)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do pagamento da fatura)

### Tabelas-filha (FK de saída)
- [[ap_invoice_payments_all]] — via `REVERSAL_INV_PMT_ID` (auto-referência para reversões)
- [[ap_payment_history_all]] — via `INVOICE_PAYMENT_ID` (histórico do pagamento)

---

## 📎 Uso Típico

### Pagamentos de uma fatura
```sql
SELECT aip.PAYMENT_NUM, aip.AMOUNT, aip.DISCOUNT_TAKEN,
       aip.ACCOUNTING_DATE, ac.CHECK_NUMBER
FROM   AP_INVOICE_PAYMENTS_ALL aip
JOIN   AP_CHECKS_ALL ac ON ac.CHECK_ID = aip.CHECK_ID
WHERE  aip.INVOICE_ID = :p_invoice_id
ORDER BY aip.ACCOUNTING_DATE;
```

### Total pago por período
```sql
SELECT SUM(aip.AMOUNT) AS total_pago,
       COUNT(DISTINCT aip.CHECK_ID) AS qtd_checks
FROM   AP_INVOICE_PAYMENTS_ALL aip
WHERE  aip.ACCOUNTING_DATE BETWEEN :start_date AND :end_date
  AND  aip.REVERSAL_FLAG IS NULL
  AND  aip.ORG_ID = :p_org_id;
```

### Filtros comuns
- `REVERSAL_FLAG IS NULL` — Exclui pagamentos revertidos
- `POSTED_FLAG = 'Y'` — Já contabilizados no GL
- `ACCOUNTING_DATE BETWEEN :start AND :end` — Período contábil

---

## 🔒 Observações

- A tabela implementa o relacionamento **N:N** entre faturas e checks: uma fatura pode ser paga por múltiplos checks, e um check pode pagar múltiplas faturas.
- O campo `REVERSAL_FLAG = 'Y'` indica um pagamento revertido (void), com `REVERSAL_INV_PMT_ID` apontando para o pagamento original.
- Os campos `DISCOUNT_TAKEN` e `DISCOUNT_LOST` registram descontos financeiros de pagamento antecipado, conforme condições de pagamento.
- A coluna `PAYMENT_NUM` referencia o número da parcela em [[ap_payment_schedules_all]].
- A tabela possui **Descriptive Flexfields (DFF)** via colunas `ATTRIBUTE1–15` para customizações por implementação.

---

## 📚 Referências

- [Oracle Docs — AP_INVOICE_PAYMENTS_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/apinvoicepaymentsall-10007.html)
- [[ap-module-data-dictionary]] — Dossiê do módulo AP
