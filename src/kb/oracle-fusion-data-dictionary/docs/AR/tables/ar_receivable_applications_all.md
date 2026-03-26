---
id: DOC-AR-020
doc_type: system-doc
title: "AR_RECEIVABLE_APPLICATIONS_ALL — Aplicações de Recebimentos e Créditos"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - accounts-receivable
  - data-dictionary
  - aplicacoes
  - receivable-applications
  - cash-application
aliases:
  - AR_RECEIVABLE_APPLICATIONS_ALL
  - ar_receivable_applications_all
  - aplicacoes-recebimentos-ar
  - receivable-applications
  - cash-application
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_RECEIVABLE_APPLICATIONS_ALL

## 📌 Visão Geral

Armazena as **aplicações de recebimentos e notas de crédito a faturas** no módulo Accounts Receivable. Cada registro representa uma aplicação individual — a alocação de um valor recebido (cash receipt) ou crédito (credit memo) contra uma fatura específica. O campo `APPLICATION_TYPE` distingue entre aplicações de caixa (CASH) e de credit memo (CM). É a tabela central para entender **como os recebimentos foram distribuídos** entre as faturas.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Aplicação de recebimentos:** Vinculação de pagamentos recebidos a faturas específicas, reduzindo o saldo em aberto.
- **Aplicação de credit memos:** Alocação de notas de crédito contra faturas para compensação.
- **Descontos:** Registro de descontos concedidos (earned) e não-concedidos (unearned) na aplicação.
- **Reconciliação AR:** Base para conciliar saldos de recebimentos × faturas × GL.
- **Relatórios de aging:** Impacto direto no cálculo de saldos em aberto em [[ar_payment_schedules_all]].
- **Auditoria:** Rastreabilidade completa de cada alocação de valor.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RECEIVABLE_APPLICATION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da aplicação | — | 🟢 100% |
| 2 | CASH_RECEIPT_ID | NUMBER(18) | NULL | FK | Recebimento de caixa aplicado (quando APPLICATION_TYPE = CASH) | [[ar_cash_receipts_all]] | 🟢 100% |
| 3 | APPLIED_CUSTOMER_TRX_ID | NUMBER(18) | NULL | FK | Transação (fatura) na qual o valor foi aplicado | [[ra_customer_trx_all]] | 🟢 100% |
| 4 | APPLIED_PAYMENT_SCHEDULE_ID | NUMBER(18) | NULL | FK | Schedule de pagamento da fatura aplicada | [[ar_payment_schedules_all]] | 🟢 100% |
| 5 | APPLICATION_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo da aplicação: CASH (recebimento) ou CM (credit memo) | — | 🟢 100% |
| 6 | STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status da aplicação (APP/UNAPP/ACC/ACTIVITY/OTHER ACC) | — | 🟢 100% |
| 7 | AMOUNT_APPLIED | NUMBER | NULL | Financeiro | Valor aplicado na moeda da fatura | — | 🟢 100% |
| 8 | AMOUNT_APPLIED_FROM | NUMBER | NULL | Financeiro | Valor aplicado na moeda do recebimento (cross-currency) | — | 🟢 100% |
| 9 | ACCTD_AMOUNT_APPLIED_FROM | NUMBER | NULL | Financeiro | Valor aplicado na moeda funcional | — | 🟢 100% |
| 10 | ACCTD_AMOUNT_APPLIED_TO | NUMBER | NULL | Financeiro | Valor aplicado na moeda funcional (lado da fatura) | — | 🟢 100% |
| 11 | APPLY_DATE | DATE | NOT NULL | Data | Data da aplicação | — | 🟢 100% |
| 12 | GL_DATE | DATE | NOT NULL | Contabilidade | Data contábil (General Ledger) | — | 🟢 100% |
| 13 | GL_POSTED_DATE | DATE | NULL | Contabilidade | Data em que foi contabilizado no GL | — | 🟢 100% |
| 14 | POSTING_CONTROL_ID | NUMBER(18) | NULL | Contabilidade | ID do processo de posting | — | 🟢 100% |
| 15 | CODE_COMBINATION_ID | NUMBER(18) | NULL | Contabilidade | Combinação de contas contábeis (CCID) | [[gl_code_combinations]] | 🟢 100% |
| 16 | PAYMENT_SCHEDULE_ID | NUMBER(18) | NULL | FK | Schedule de pagamento do recebimento/credit memo | [[ar_payment_schedules_all]] | 🟢 100% |
| 17 | CUSTOMER_TRX_ID | NUMBER(18) | NULL | FK | Transação de origem do credit memo (quando APPLICATION_TYPE = CM) | [[ra_customer_trx_all]] | 🟢 100% |
| 18 | DISPLAY_FLAG | VARCHAR2(1) | NULL | Controle | Indica se a aplicação é exibida na UI (Y/N) | — | 🟢 100% |
| 19 | APPLICATION_RULE | VARCHAR2(30) | NULL | Classificação | Regra utilizada na aplicação (e.g., LINE FIRST, PRORATE) | — | 🟢 100% |
| 20 | EARNED_DISCOUNT_TAKEN | NUMBER | NULL | Financeiro | Desconto concedido (earned discount) | — | 🟢 100% |
| 21 | UNEARNED_DISCOUNT_TAKEN | NUMBER | NULL | Financeiro | Desconto não-concedido (unearned discount) | — | 🟢 100% |
| 22 | EARNED_DISCOUNT_CCID | NUMBER(18) | NULL | Contabilidade | CCID do desconto concedido | [[gl_code_combinations]] | 🟢 100% |
| 23 | UNEARNED_DISCOUNT_CCID | NUMBER(18) | NULL | Contabilidade | CCID do desconto não-concedido | [[gl_code_combinations]] | 🟢 100% |
| 24 | DAYS_LATE | NUMBER | NULL | Financeiro | Dias de atraso no pagamento | — | 🟢 100% |
| 25 | COMMENTS | VARCHAR2(2000) | NULL | Texto livre | Comentários sobre a aplicação | — | 🟢 100% |
| 26 | APPLIED_CUSTOMER_TRX_LINE_ID | NUMBER(18) | NULL | FK | Linha específica da fatura aplicada (line-level) | [[ra_customer_trx_lines_all]] | 🟢 100% |
| 27 | REVERSAL_GL_DATE | DATE | NULL | Contabilidade | Data contábil da reversão da aplicação | — | 🟢 100% |
| 28 | LINK_TO_CUSTOMER_TRX_ID | NUMBER(18) | NULL | Referência cruzada | Transação vinculada (para on-account credit) | [[ra_customer_trx_all]] | 🟢 100% |
| 29 | ON_ACCOUNT_CUSTOMER | NUMBER(18) | NULL | Cliente | Conta do cliente para crédito on-account | [[hz_cust_accounts]] | 🟢 100% |
| 30 | RECEIVABLES_TRX_ID | NUMBER(18) | NULL | Classificação | Tipo de atividade de recebimento | [[ar_receivables_trx_all]] | 🟢 100% |
| 31 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 32 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 33 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 34 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 35 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 36 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 37 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 38 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |
| 39 | GLOBAL_ATTRIBUTE1–20 | VARCHAR2(150) | NULL | DFF | Atributos globais (localizações por país) | — | 🟢 100% |
| 40 | GLOBAL_ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Global Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ar_cash_receipts_all]] — via `CASH_RECEIPT_ID` (recebimento de caixa)
- [[ra_customer_trx_all]] — via `APPLIED_CUSTOMER_TRX_ID` (fatura aplicada) e `CUSTOMER_TRX_ID` (credit memo)
- [[ar_payment_schedules_all]] — via `APPLIED_PAYMENT_SCHEDULE_ID` e `PAYMENT_SCHEDULE_ID` (parcela contra a qual o pagamento foi aplicado)
- [[ra_customer_trx_lines_all]] — via `APPLIED_CUSTOMER_TRX_LINE_ID` (linha da fatura)
- [[gl_code_combinations]] — via `CODE_COMBINATION_ID`, `EARNED_DISCOUNT_CCID`, `UNEARNED_DISCOUNT_CCID` (conta contábil da aplicação de recebível)
- [[ar_receivables_trx_all]] — via `RECEIVABLES_TRX_ID` (atividade de recebimento)
- [[hz_cust_accounts]] — via `ON_ACCOUNT_CUSTOMER` (cliente on-account)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da aplicação de recebível)

### Tabelas-filha (FK de saída)
- [[ar_distributions_all]] — via `SOURCE_ID` onde `SOURCE_TABLE = 'RA'` (distribuições contábeis)

---

## 📎 Uso Típico

### Aplicações de um recebimento
```sql
SELECT ra.STATUS, ra.APPLICATION_TYPE, ra.AMOUNT_APPLIED,
       ra.APPLY_DATE, ct.TRX_NUMBER
FROM   AR_RECEIVABLE_APPLICATIONS_ALL ra
LEFT JOIN RA_CUSTOMER_TRX_ALL ct ON ct.CUSTOMER_TRX_ID = ra.APPLIED_CUSTOMER_TRX_ID
WHERE  ra.CASH_RECEIPT_ID = :p_cash_receipt_id
  AND  ra.DISPLAY_FLAG = 'Y';
```

### Faturas com aplicações de recebimento
```sql
SELECT ct.TRX_NUMBER, cr.RECEIPT_NUMBER,
       ra.AMOUNT_APPLIED, ra.APPLY_DATE, ra.STATUS
FROM   AR_RECEIVABLE_APPLICATIONS_ALL ra
JOIN   RA_CUSTOMER_TRX_ALL ct ON ct.CUSTOMER_TRX_ID = ra.APPLIED_CUSTOMER_TRX_ID
JOIN   AR_CASH_RECEIPTS_ALL cr ON cr.CASH_RECEIPT_ID = ra.CASH_RECEIPT_ID
WHERE  ra.APPLICATION_TYPE = 'CASH'
  AND  ra.STATUS = 'APP'
  AND  ra.ORG_ID = :p_org_id;
```

### Filtros comuns
- `APPLICATION_TYPE = 'CASH'` — Aplicações de recebimento
- `APPLICATION_TYPE = 'CM'` — Aplicações de credit memo
- `STATUS = 'APP'` — Aplicações efetivadas
- `DISPLAY_FLAG = 'Y'` — Aplicações visíveis na UI

---

## 🔒 Observações

- Os campos `AMOUNT_APPLIED` e `AMOUNT_APPLIED_FROM` diferem em aplicações **cross-currency**: `AMOUNT_APPLIED` é na moeda da fatura, `AMOUNT_APPLIED_FROM` na moeda do recebimento.
- O `STATUS` pode ser: **APP** (aplicado), **UNAPP** (não-aplicado), **ACC** (on-account), **ACTIVITY** (atividade), **OTHER ACC** (outra conta).
- Registros com `DISPLAY_FLAG = 'N'` são internos ao sistema (e.g., reversões internas) — não devem aparecer em relatórios de usuário.
- O campo `APPLICATION_RULE` indica a regra de alocação: **LINE FIRST** (aplica primeiro em linhas), **PRORATE** (distribui proporcional), etc.
- Descontos (earned/unearned) são registrados junto com a aplicação e impactam contas contábeis separadas.

---

## 📚 Referências

- [Oracle Docs — AR_RECEIVABLE_APPLICATIONS_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/arreceivableapplicationsall-10021.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
